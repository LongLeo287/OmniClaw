---
id: Product-Manager-Skills
type: knowledge
owner: OA_Triage
---
# Product-Manager-Skills
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<a id="pmskills"></a>
# Product Manager Skills

![GitHub stars](https://img.shields.io/github/stars/deanpeters/Product-Manager-Skills?style=flat-square)
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey?style=flat-square)](https://github.com/deanpeters/Product-Manager-Skills/blob/main/LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)](https://github.com/deanpeters/Product-Manager-Skills/blob/main/CONTRIBUTING.md)
[![Version](https://img.shields.io/badge/version-v0.75-blue?style=flat-square)](https://github.com/deanpeters/Product-Manager-Skills)
[![Claude Code Plugin](https://img.shields.io/badge/Claude%20Code-Plugin%20Marketplace-5C4EE5?style=flat-square)](https://code.claude.com/docs/en/plugin-marketplaces)
![Skills](https://img.shields.io/badge/skills-47-informational?style=flat-square)
![Commands](https://img.shields.io/badge/commands-6-informational?style=flat-square)
![Streamlit Beta](https://img.shields.io/badge/streamlit-beta-orange?style=flat-square)

```text
╔════════════════════════════════════════════════════════════════════╗
║                                                                    ║
║   ██████╗ ███╗   ███╗    ███████╗██╗  ██╗██╗██╗     ██╗     ███████╗
║   ██╔══██╗████╗ ████║    ██╔════╝██║ ██╔╝██║██║     ██║     ██╔════╝
║   ██████╔╝██╔████╔██║    ███████╗█████╔╝ ██║██║     ██║     ███████╗
║   ██╔═══╝ ██║╚██╔╝██║    ╚════██║██╔═██╗ ██║██║     ██║     ╚════██║
║   ██║     ██║ ╚═╝ ██║    ███████║██║  ██╗██║███████╗███████╗███████║
║   ╚═╝     ╚═╝     ╚═╝    ╚══════╝╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚══════╝
║                                                                    ║
║   47 battle-tested skills + 6 command workflows                    ║
║   Claude Code • Cursor • Codex  • n8n • OpenClaw • and more ...    ║
║                                                                    ║
║   v0.75 • Mar 17, 2026 • CC BY-NC-SA 4.0                           ║
╚════════════════════════════════════════════════════════════════════╝
```

**Help product managers become more awesome at their craft — and help them send the ladder down to others.**

Battle-tested PM frameworks that teach both you and your AI agents how to do product management work at a professional level. You learn the *why*. Your agents execute the *how*. Everyone gets better.

Frame problems, hunt opportunities, scaffold validation experiments, and kill bad bets fast. With frameworks from Teresa Torres, Geoffrey Moore, Amazon, MITRE, and much more from product management's greatest hits.

---

## 📣 Updates & Announcements

### Mar 17, 2026 — v0.75 Pedagogic-First: Restoring What This Repo Is Actually For

I want to apologize  to a contributor who recently submitted a well-intentioned and well-coded improvement that stripped learning scaffolding in favor of tighter copy. It wasn't their fault — the docs they read never crisply stated that pedagogic value is non-negotiable. We fixed that. I will work with that contribution to bring in its efficiencies while retaining the learning aspects of the skills.

**What this repo is actually for:** As much as this repo is for adding skills to your agent, it's equally tasked to help product managers become more awesome at their craft, and helping them send the ladder down to others. Skills here serve both goals: they make your agent more capable, and they make you more knowledgeable about why the framework works. Neither is a byproduct of the other.

**ABC — Always Be Coaching** is a key governing principle. Every skill should leave the person using it knowing more than when they started. Stripping explanation to tighten output is a defect, not an improvement.

What changed in v0.75:
- `README.md` — Mission statement updated to name both audiences: human PMs and AI agents
- `CONTRIBUTING.md` — New Design Philosophy section so contributors know what they're protecting
- `CLAUDE.md` — Pedagogic-first added to the agent's mandate, not just the style guide
- `AGENTS.md` — New Operating Philosophy section so coding agents don't optimize away the teaching

Release note: [`docs/announcements/2026-03-17-v0-75-pedagogic-first.md`](docs/announcements/2026-03-17-v0-75-pedagogic-first.md)

**Now available:** Install skills directly from Claude Code via the plugin marketplace:
```bash
/plugin marketplace add deanpeters/Product-Manager-Skills
/plugin install jobs-to-be-done@pm-skills
```

---

### Mar 9, 2026 — v0.7 Sharper Skills, Faster Discovery

This release is about making the library easier to trust and easier to use.

As this repo grows, the standard has to rise with it. So v0.7 focuses on the parts users actually feel:
- finding the right skill faster,
- understanding when to use it,
- getting cleaner activation behavior,
- and trusting that the repo is being actively tightened, not just expanded.

#### Why it matters:
1. You spend less time guessing which skill to use.
2. Skills are more likely to show up in the situations where you actually need them.
3. The library becomes easier to navigate as it grows, not more chaotic.
4. Quality becomes a maintained promise, not a one-time cleanup.

#### What shipped:
- Trigger-oriented description updates across the skill library so skills answer both "what it does" and "use this when..."
- New `intent` frontmatter field so every skill can keep a sharp trigger description and a richer deeper-purpose summary
- New trigger-readiness auditing in `scripts/check-skill-triggers.py`
- Trigger checks wired into `scripts/test-library.sh`
- New `find-a-skill.sh --mode trigger` for discovering skills by use-case language, `best_for`, and `scenarios`
- New Streamlit (beta) `Find My Skill` mode so users can describe a situation in plain English and get recommended skills with clear next actions
- Streamlit navigation now separates `Learn`, `Find My Skill`, and `Run Skills` so first-time users can move from confusion to action faster
- Contributor docs updated so future skills follow the same tighter standard
- Cross-checked the tighter standard against Anthropic's [Complete Guide to Building Skills for Claude](https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf)

Release note: [`docs/announcements/2026-03-09-v0-7-skill-quality-trigger-clarity.md`](docs/announcements/2026-03-09-v0-7-skill-quality-trigger-clarity.md)

---

### Mar 8, 2026 — v0.65 You Asked, We Listened: Setup + Integration Everywhere

You asked, we listened. We took a moment to create comprehensive instructions on how to install, integrate, or otherwise use any one or all of these skills.

What shipped:
- `docs/Using PM Skills 101.md` as the complete beginner-first guide
- `docs/Platform Guides for PMs.md` as the pick-your-tool index
- `docs/Using PM Skills with Slash Commands 101.md` for Claude `/slash` workflows like `/pm-story` and `/pm-prd`
- New PM-friendly platform docs for Claude Code, Claude Desktop, Claude Cowork, ChatGPT Desktop, OpenClaw, n8n, LangFlow, and Python agents
- Updated `START_HERE.md` with comfort-level paths (chat-first, terminal-first, automation-first)

How to make the best use of this release:
1. Start with [`docs/Using PM Skills 101.md`](docs/Using%20PM%20Skills%20101.md)
2. Choose your platform in [`docs/Platform Guides for PMs.md`](docs/Platform%20Guides%20for%20PMs.md)
3. Run one real task with one skill before scaling to multi-skill workflows

Release note: [`docs/announcements/2026-03-08-v0-65-onboarding-integration-guides.md`](docs/announcements/2026-03-08-v0-65-onboarding-integration-guides.md)

---

### Mar 6, 2026 — v0.6 Navigation + Commands

We added a command layer and fast navigation system while keeping skills as the source of truth.

What shipped:
- `START_HERE.md` for 60-second onboarding
- `commands/` directory with reusable multi-skill workflows
- `catalog/` generated indexes for quick browsing
- New helper scripts: `run-pm.sh`, `find-a-command.sh`, `test-library.sh`, and `generate-catalog.py`
- Command validation with `scripts/check-command-metadata.py`

Release note draft: [`docs/announcements/2026-03-06-v0-6-navigation-commands.md`](docs/announcements/2026-03-06-v0-6-navigation-commands.md)

---

### Feb 27, 2026 — v0.5 Streamlit (beta) Playground

We launched a new **Streamlit (beta)** interface for local skill test-driving.

What shipped:
- Local playground at `app/main.py` with guided browsing and session flows
- Multi-provider support (Anthropic, OpenAI, Ollama) with provider/model picker
- Environment-variable-only API handling (`app/.env.example`) for safer defaults
- Workflow UX upgrades (phase detection fix, per-phase output persistence, run-all phases control)
- Fast-model quality warnings on long workflows (especially PRD-style runs)

Docs:
- [`app/STREAMLIT_INTERFACE.md`](app/STREAMLIT_INTERFACE.md)
- [`app/.env.example`](app/.env.example)

Feedback welcome:
- [GitHub Issues](https://github.com/deanpeters/Product-Manager-Skills/issues)
- [Dean on LinkedIn](https://linkedin.com/in/deanpeters)

---

<a id="leaderskills"></a>
### Feb 27, 2026 — v0.5 Career & Leadership Skills Suite

Four new skills covering the full product leadership career arc — from PM to Director to VP/CPO — distilled from two episodes of [The Product Porch](https://the-product-porch-43ca35c0.simplecast.com) podcast.

**Based on Episode 42 — [From PM to Director: How to Make the Shift (Part 1)](https://the-product-porch-43ca35c0.simplecast.com/episodes/from-product-manager-to-director-how-to-make-the-shift-part-1):**
- [`altitude-horizon-framework`](skills/altitude-horizon-framework/SKILL.md) (Component) — The core mental model: altitude (scope) and horizon (time), the waiter-to-operator shift, four transition zones, named failure modes, and the Cascading Context Map
- [`director-readiness-advisor`](skills/director-readiness-advisor/SKILL.md) (Interactive) — Coaches PMs and new Directors across four situations: preparing, interviewing, newly landed, and recalibrating

**Based on Episode 43 — [Becoming a VP & CPO: Leading Product at the Executive Level (Part 2)](https://the-product-porch-43ca35c0.simplecast.com/episodes/becoming-a-vp-cpo-leading-product-at-the-executive-level-part-2):**
- [`executive-onboarding-playbook`](skills/executive-onboarding-playbook/SKILL.md) (Workflow) — A 30-60-90 day diagnostic playbook for VP/CPO transitions: diagnose before acting, surface unwritten strategy, assess people, act with evidence
- [`vp-cpo-readiness-advisor`](skills/vp-cpo-readiness-advisor/SKILL.md) (Interactive) — Coaches Directors and executives through the VP/CPO transition, including the CEO interview framework for evaluating roles before accepting

---

### Feb 10, 2026 — v0.4 Facilitation Protocol Fix

We found and fixed a facilitation regression in interactive flows.

What happened:
- We expected guided, step-by-step facilitation with progressive context handling.
- In practice, a brevity-focused rewrite path stripped out parts of the original facilitation modality (especially the "walk through questions" behavior).

What we changed in v0.4:
- Standardized a canonical facilitation protocol in [`skills/workshop-facilitation/SKILL.md`](skills/workshop-facilitation/SKILL.md).
- Rolled that source-of-truth linkage across interactive skills and facilitation-heavy workflow skills.
- Added mandatory session heads-up, `Context dump` bypass, and `Best guess` mode.
- Added stronger progress labels, interruption handling, and decision-point recommendation rules.

Credit:
- Codex identified the protocol mismatch and implemented the fix across the repo.

Announcement draft: [`docs/announcements/2026-02-10-v0-4-facilitation-fix.md`](docs/announcements/2026-02-10-v0-4-facilitation-fix.md)

---

### Feb 8, 2026 — LinkedIn Launch

**Post title:** Product Management Skills for Your Agents
**Subtitle:** Because "just prompt better" is not a strategy.

Still rewriting PM prompts and getting generic AI output? I built a reusable PM Skills repo to help you make sharper decisions, docs, and outcomes faster.

- Full announcement draft: [`docs/announcements/2026-02-08-linkedin-launch.md`](docs/announcements/2026-02-08-linkedin-launch.md)
- Substack article draft: [`docs/announcements/2026-02-08-substack-savage-launch.md`](docs/announcements/2026-02-08-substack-savage-launch.md)
- Announcements index: [`docs/announcements/README.md`](docs/announcements/README.md)
- Skills repo: [Product Manager Skills](https://github.com/deanpeters/Product-Manager-Skills)
- Prior prompts repo: [Product Manager Prompts](https://github.com/deanpeters/product-manager-prompts)

---

## 🎯 What This Is

**47 ready-to-use PM skills + reusable command workflows** that teach both you and your AI agents how to do product management work at a professional level — so the PM understands the *why* and the agent can execute the *how*.

Instead of saying *"Write a PRD"* and hoping for the best, you and your agent both know:
- ✅ How to structure a PRD and why each section earns its place
- ✅ What questions to ask stakeholders and what you're listening for
- ✅ Which prioritization framework to use (and when each one breaks down)
- ✅ How to run customer discovery interviews and what signals matter
- ✅ How to break down epics using proven patterns — and the tradeoffs of each

**Result:** You work faster, with better consistency, at a higher strategic level — and you can explain why.

**Works with:** Claude Code, Cowork, OpenAI Codex, ChatGPT, Gemini, and any AI agent that can read structured knowledge.

---

## 🎓 Design Philosophy — Pedagogic and Practical in Equal Measure

As much as this repo is for adding skills to your agent, it's equally tasked to **help product managers become more awesome at their craft — and to help them send the ladder down to others.**

Skills here serve both goals simultaneously. They equip AI agents to do PM work at a professional level, and they teach the human PM the *why* behind the framework — so they can explain it, adapt it, and pass it on.

**ABC — Always Be Coaching** is a key governing principle. Every skill should leave the person using it knowing more than when they started.

This means:
- Skills explain reasoning, not just steps
- Examples show the thinking, not just the output
- Anti-patterns name the failure mode so you recognize it in the wild
- Interactive skills coach through discovery — they don't just collect answers

**An edit that strips learning scaffolding to tighten copy is a defect, not an improvement.**

---

## ⚡ Start in 60 Seconds

New here? Start with [`START_HERE.md`](START_HERE.md).

```bash
# Run a skill (artifact/analysis)
./scripts/run-pm.sh skill prioritization-advisor "We have 12 requests and one sprint"

# Run a command (multi-skill workflow)
./scripts/run-pm.sh command discover "Reduce onboarding drop-off for self-serve users"
```

Need discovery first?

```bash
./scripts/find-a-skill.sh --keyword onboarding
./scripts/find-a-command.sh --keyword road
... [TRUNCATED]
```

### File: app\main.py
```py
"""PM Skills Playground — Streamlit app for browsing and test-driving PM skills.

Usage:
    cd /path/to/product-manager-skills
    pip install -r app/requirements.txt
    streamlit run app/main.py
"""

import os
import re
from pathlib import Path

import anthropic
import streamlit as st
import yaml
from dotenv import load_dotenv
try:
    from openai import AuthenticationError as OpenAIAuthenticationError
    from openai import OpenAI
except ImportError:  # pragma: no cover - optional dependency for multi-provider mode
    OpenAI = None

    class OpenAIAuthenticationError(Exception):
        pass

load_dotenv(Path(__file__).parent / ".env")

# ─── Constants ────────────────────────────────────────────────────────────────

SKILLS_DIR = Path(__file__).parent.parent / "skills"
DOCS_DIR = Path(__file__).parent.parent / "docs"
ROOT_DIR = Path(__file__).parent.parent
PROVIDERS = {
    "anthropic": {
        "label": "Anthropic",
        "key_env": "ANTHROPIC_API_KEY",
        "default_model_env": "ANTHROPIC_MODEL",
        "models_env": "ANTHROPIC_MODELS",
        "default_models": ["claude-haiku-4-5-20251001", "claude-sonnet-4-6"],
        "model_help": {
            "claude-haiku-4-5-20251001": "Fast (cheaper; may miss depth in long workflows)",
            "claude-sonnet-4-6": "Capable (best for full workflow quality)",
        },
    },
}
if OpenAI is not None:
    PROVIDERS["openai"] = {
        "label": "OpenAI",
        "key_env": "OPENAI_API_KEY",
        "default_model_env": "OPENAI_MODEL",
        "models_env": "OPENAI_MODELS",
        "default_models": ["gpt-4o-mini", "gpt-4o"],
        "model_help": {
            "gpt-4o-mini": "Fast (cheaper; may miss depth in long workflows)",
            "gpt-4o": "Capable (best for full workflow quality)",
        },
    }
    PROVIDERS["ollama"] = {
        "label": "Ollama",
        "key_env": None,
        "default_model_env": "OLLAMA_MODEL",
        "models_env": "OLLAMA_MODELS",
        "default_models": ["qwen2.5:latest", "llama3.2:latest"],
        "model_help": {
            "qwen2.5:latest": "Fast (local; may miss depth in long workflows)",
            "llama3.2:latest": "Capable (local; best for full workflow quality)",
        },
    }

THEMES = {
    "career-leadership": {
        "label": "Career & Leadership",
        "icon": "🚀",
        "description": "PM→Director→VP/CPO transitions, readiness advisors, executive onboarding",
    },
    "discovery-research": {
        "label": "Discovery & Research",
        "icon": "🔍",
        "description": "Customer interviews, opportunity mapping, problem framing, jobs-to-be-done",
    },
    "strategy-positioning": {
        "label": "Strategy & Positioning",
        "icon": "🎯",
        "description": "Positioning, roadmaps, product strategy, market analysis",
    },
    "pm-artifacts": {
        "label": "Writing PM Artifacts",
        "icon": "📝",
        "description": "User stories, PRDs, epics, press releases, personas, storyboards",
    },
    "finance-metrics": {
        "label": "Finance & Metrics",
        "icon": "📊",
        "description": "SaaS metrics, unit economics, pricing, business health",
    },
    "ai-agents": {
        "label": "AI & Agents",
        "icon": "🤖",
        "description": "AI-shaped thinking, agent orchestration, context engineering, PoL probes",
    },
    "workshops-facilitation": {
        "label": "Workshops & Facilitation",
        "icon": "🎭",
        "description": "Journey mapping, facilitation, canvas tools, story mapping workshops",
    },
}

TYPE_BADGES = {
    "component": ("🧱", "Component"),
    "interactive": ("🔄", "Interactive"),
    "workflow": ("🎭", "Workflow"),
}

GUIDE_GROUPS = [
    {
        "label": "Start Here",
        "guides": [
            {
                "id": "start_here",
                "title": "Start Here",
                "path": ROOT_DIR / "START_HERE.md",
                "summary": "Fastest path from zero to first useful output.",
            },
            {
                "id": "pm_skills_101",
                "title": "Using PM Skills 101",
                "path": DOCS_DIR / "Using PM Skills 101.md",
                "summary": "Beginner-first orientation and platform install patterns.",
            },
            {
                "id": "platform_guides",
                "title": "Platform Guides for PMs",
                "path": DOCS_DIR / "Platform Guides for PMs.md",
                "summary": "Pick-your-tool index for all supported harnesses.",
            },
        ],
    },
    {
        "label": "Core Platforms",
        "guides": [
            {
                "id": "claude",
                "title": "Using PM Skills with Claude",
                "path": DOCS_DIR / "Using PM Skills with Claude.md",
                "summary": "Claude setup across Code, Desktop, and Cowork.",
            },
            {
                "id": "codex",
                "title": "Using PM Skills with Codex",
                "path": DOCS_DIR / "Using PM Skills with Codex.md",
                "summary": "Run skills via local paths or GitHub-connected Codex.",
            },
            {
                "id": "chatgpt",
                "title": "Using PM Skills with ChatGPT",
                "path": DOCS_DIR / "Using PM Skills with ChatGPT.md",
                "summary": "Projects, GPT Knowledge, and GitHub-connected usage.",
            },
        ],
    },
    {
        "label": "Claude + Chat Apps",
        "guides": [
            {
                "id": "claude_code",
                "title": "Using PM Skills with Claude Code",
                "path": DOCS_DIR / "Using PM Skills with Claude Code.md",
                "summary": "CLI-first usage with direct file path workflows.",
            },
            {
                "id": "claude_desktop",
                "title": "Using PM Skills with Claude Desktop",
                "path": DOCS_DIR / "Using PM Skills with Claude Desktop.md",
                "summary": "No-code upload flow and starter usage patterns.",
            },
            {
                "id": "claude_cowork",
                "title": "Using PM Skills with Claude Cowork",
                "path": DOCS_DIR / "Using PM Skills with Claude Cowork.md",
                "summary": "Knowledge-module style workspace usage.",
            },
            {
                "id": "claude_slash",
                "title": "Using PM Skills with Slash Commands 101",
                "path": DOCS_DIR / "Using PM Skills with Slash Commands 101.md",
                "summary": "Turn PM skills into reusable /commands.",
            },
            {
                "id": "chatgpt_desktop",
                "title": "Using PM Skills with ChatGPT Desktop",
                "path": DOCS_DIR / "Using PM Skills with ChatGPT Desktop.md",
                "summary": "Project-first setup in desktop chat workflows.",
            },
        ],
    },
    {
        "label": "Automation + Agent Harnesses",
        "guides": [
            {
                "id": "n8n",
                "title": "Using PM Skills with n8n",
                "path": DOCS_DIR / "Using PM Skills with n8n.md",
                "summary": "Repeatable AI workflows with skill injection patterns.",
            },
            {
                "id": "langflow",
                "title": "Using PM Skills with LangFlow",
                "path": DOCS_DIR / "Using PM Skills with LangFlow.md",
                "summary": "Visual prompt-chain setup with skill context.",
            },
            {
                "id": "python_agents",
                "title": "Using PM Skills with Python Agents",
                "path": DOCS_DIR / "Using PM Skills with Python Agents.md",
                "summary": "Embed skill files into custom agent pipelines.",
            },
            {
                "id": "openclaw",
                "title": "Using PM Skills with OpenClaw",
                "path": DOCS_DIR / "Using PM Skills with OpenClaw.md",
                "summary": "System prompt and router patterns for self-hosted agents.",
            },
            {
                "id": "cursor",
                "title": "Using PM Skills with Cursor",
                "path": DOCS_DIR / "Using PM Skills with Cursor.md",
                "summary": "Persistent rules plus @file invocation pattern.",
            },
            {
                "id": "windsurf",
                "title": "Using PM Skills with Windsurf",
                "path": DOCS_DIR / "Using PM Skills with Windsurf.md",
                "summary": "Cascade rules and context-aware multi-step usage.",
            },
            {
                "id": "bolt",
                "title": "Using PM Skills with Bolt",
                "path": DOCS_DIR / "Using PM Skills with Bolt.md",
                "summary": "Problem-first prompts before prototype generation.",
            },
            {
                "id": "replit",
                "title": "Using PM Skills with Replit Agent",
                "path": DOCS_DIR / "Using PM Skills with Replit Agent.md",
                "summary": "System prompt guardrails for iterative build loops.",
            },
            {
                "id": "make",
                "title": "Using PM Skills with Make.com",
                "path": DOCS_DIR / "Using PM Skills with Make.com.md",
                "summary": "No-code scenario design with skill-driven AI modules.",
            },
            {
                "id": "devin",
                "title": "Using PM Skills with Devin",
                "path": DOCS_DIR / "Using PM Skills with Devin.md",
                "summary": "Keep autonomous execution aligned with PM guardrails.",
            },
            {
                "id": "crewai",
                "title": "Using PM Skills with CrewAI",
                "path": DOCS_DIR / "Using PM Skills with CrewAI.md",
                "summary": "Map skills to multi-agent roles and orchestration.",
            },
            {
                "id": "gemini",
                "title": "Using PM Skills with Gemini",
                "path": DOCS_DIR / "Using PM Skills with Gemini.md",
                "summary": "Gemini CLI, AI Studio, and persistent context patterns.",
            },
        ],
    },
]

LEARN_TO_RUN_SKILLS = [
    ("prioritization-advisor", "Interactive"),
    ("user-story", "Component"),
    ("prd-development", "Workflow"),
]

FIND_MY_SKILL_PROMPTS = [
    "I need to figure out why activation is dropping for new users.",
    "Help me decide whether this feature is worth building.",
    "I need to turn discovery notes into a PRD my engineers can use.",
    "We need a clearer prioritization framework for roadmap decisions.",
]

# ─── Skill Loading ─────────────────────────────────────────────────────────────

@st.cache_data
def load_skills():
    """Parse all SKILL.md files. Returns list of skill dicts."""
    skills = []
    for skill_dir in sorted(SKILLS_DIR.iterdir()):
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.exists():
            continue
        text = skill_file.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            continue
        parts = text.split("---", 2)
        if len(parts) < 3:
            continue
        try:
            fm = yaml.safe_load(parts[1]) or {}
        except yaml.YAMLError:
            continue

        body = parts[2].strip()

        # Extract ## sections into a dict
        sections: dict[str, str] = {}
        current: str | None = None
        buf: list[str] = []
        for line in body.split("\n"):
            if line.startswith("## "):
                if current is not None:
                    sections[current] = "\n".join(buf).strip()
                current = line[3:].strip()
                buf = []
            else:
                buf.append(line)
        if current is not None:
            sections[current] = "\n".join(buf).strip()

        # First non-empty paragraph of Purpose as a short excerpt
        purpose_text = sections.get("Purpose", "")
        purpose_short = next(
            (p.strip() for p in purpose_text.split("\n\n") if p.strip()), ""
        )

        skills.append(
            {
                "name": fm.get("name", skill_dir.name),
                "description": fm.get("description", ""),
                "intent": fm.get("intent", ""),
                "type": fm.get("type", "component"),
                "theme": fm.get("theme"),
                "best_for": fm.get("best_for") or [],
                "scenarios": fm.get("scenarios") or [],
                "estimated_time": fm.get("estimated_time"),
                "body": body,
                "sections": sections,
                "purpose_short": purpose_short,
                "has_examples": (skill_dir / "examples").exists(),
            }
        )
    return skills


@st.cache_data
def load_guide_markdown(path_str: str) -> str:
    path = Path(path_str)
    if not path.exists():
        return f"# Missing guide\n\nCould not find `{path}`."
    return path.read_text(encoding="utf-8")


# ─── API ──────────────────────────────────────────────────────────────────────

def _csv_models(raw: str) -> list[str]:
    values = [m.strip() for m in raw.split(",") if m.strip()]
    return list(dict.fromkeys(values))


def provider_key(provider: str) -> str:
    env_key = PROVIDERS[provider]["key_env"]
    if not env_key:
        # Ollama can run without auth; OpenAI-compatible clients still require a placeholder key.
        return os.getenv("OLLAMA_API_KEY", "ollama").strip()
    return os.getenv(env_key, "").strip()


def provider_enabled(provider: str) -> bool:
    if provider != "ollama":
        return bool(provider_key(provider))

    enabled_flag = os.getenv("OLLAMA_ENABLED", "").strip().lower()
    has_base = bool(os.getenv("OLLAMA_BASE_URL", "").strip())
    return enabled_flag in {"1", "true", "yes", "on"} or has_base


def ollama_base_url() -> str:
    base = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434").strip().rstrip("/")
    if base.endswith("/v1"):
        return base
    return f"{base}/v1"


def available_providers() -> list[str]:
    return [p for p in PROVIDERS if provider_enabled(p)]


def provider_default_model(provider: str) -> str:
    env_name = PROVIDERS[provider]["default_model_env"]
    return os.getenv(env_name, "").strip() or PROVIDERS[provider]["default_models"][0]


def provider_model_options(provider: str) -> list[str]:
    env_models_name = PROVIDERS[provider]["models_env"]
    env_models_raw = os.getenv(env_models_name, "")
    models = list(PROVIDERS[provider]["default_models"])
    if env_models_raw:
        models.extend(_csv_models(env_models_raw))
    default_model = provider_default_model(provider)
    if default_model not in models:
        models.insert(0, default_model)
    return list(dict.fromkeys(models))


def provider_model_help(provider: str) -> dict[str, str]:
    return PROVIDERS[provider]["model_help"]


... [TRUNCATED]
```

### File: app\requirements.txt
```txt
streamlit>=1.32.0
anthropic>=0.40.0
openai>=1.40.0
pyyaml>=6.0
python-dotenv>=1.0.0

```

### File: catalog\README.md
```md
# Catalog Artifacts

These files are generated navigation indexes for skills and commands.

- `skills-index.yaml` - machine-readable skill metadata index
- `commands-index.yaml` - machine-readable command metadata index
- `skills-by-type.md` - human-readable browse view by skill type
- `commands.md` - human-readable command catalog

Regenerate any time skills or commands change:

```bash
python3 scripts/generate-catalog.py
```

```

### File: commands\README.md
```md
# Commands

Commands are reusable workflow wrappers over one or more local PM skills.

- Skills remain the source of truth for frameworks and pedagogy.
- Commands are lightweight orchestration for fast execution.
- Commands are written as markdown with frontmatter and can be used in any agent by referencing the file path.

## Command Format

Each command file should include frontmatter:

```yaml
---
name: command-name
description: What this command does
argument-hint: "<what the user should provide>"
uses:
  - skill-name
  - another-skill
outputs:
  - Output artifact 1
  - Output artifact 2
---
```

## Available Commands (v1)

- `discover`
- `strategy`
- `write-prd`
- `plan-roadmap`
- `prioritize`
- `leadership-transition`

## Validation

```bash
python3 scripts/check-command-metadata.py
```

## Discovery

```bash
./scripts/find-a-command.sh --list-all
./scripts/find-a-command.sh --keyword roadmap
```

```

### File: scripts\README.md
```md
# Scripts Guide (For PMs)

This folder contains helper scripts so you can use the PM skills library without writing code.

If you are new to terminals, start with the commands in `Quick Start` and `Common Tasks`.

## Quick Start

1. Open this repo in VS Code.
2. Open Terminal in VS Code (`Terminal` -> `New Terminal`).
3. Confirm you are in the repo root:

```bash
pwd
```

Your path should end with `product-manager-skills`.

4. List available scripts:

```bash
ls scripts
```

## Common Tasks

Use these exactly as written, then replace the example text in quotes.

### Find the right skill

```bash
./scripts/find-a-skill.sh --keyword onboarding
```

### Find by trigger language and example situations

```bash
./scripts/find-a-skill.sh --mode trigger onboarding
```

### Find a reusable workflow command

```bash
./scripts/find-a-command.sh --keyword roadmap
```

### Generate a prompt from a skill (safest starting point)

This prints a ready-to-use prompt. Great if you are using Claude or Codex in an app window.

```bash
./scripts/run-pm.sh skill prd-development "Create a PRD for improving mobile onboarding" --agent print
```

### Run directly in Claude Code CLI (if installed)

```bash
./scripts/run-pm.sh command discover "Reduce onboarding drop-off for self-serve users" --agent claude
```

### Run directly in Codex CLI (if installed)

```bash
./scripts/run-pm.sh command write-prd "Design requirements for a new admin analytics dashboard" --agent codex
```

### Validate one skill before committing

```bash
./scripts/test-a-skill.sh --skill user-story --smoke
```

### Audit trigger wording before upload

```bash
python3 scripts/check-skill-triggers.py skills/user-story/SKILL.md --show-cases
```

### Validate the full library

```bash
./scripts/test-library.sh --smoke
```

### Build upload-ready Claude skill ZIPs

```bash
./scripts/zip-a-skill.sh --skill user-story
```

## Power Move: Chain Scripts

Each script is useful alone. Chained together, they become a repeatable PM workflow.

### Example 1: From idea to AI prompt in under 2 minutes

1. Find a relevant command:

```bash
./scripts/find-a-command.sh --keyword onboarding
```

2. Run it with your context:

```bash
./scripts/run-pm.sh command discover "Improve activation for self-serve trial users" --agent print
```

### Example 2: Create, validate, and package a new skill

1. Generate from source notes:

```bash
./scripts/add-a-skill.sh research/your-framework.md
```

2. Validate the new skill:

```bash
./scripts/test-a-skill.sh --skill your-skill-name --smoke
```

3. Build Claude upload zip:

```bash
./scripts/zip-a-skill.sh --skill your-skill-name
```

### Example 3: Pre-release quality gate

Run one command before a release or PR:

```bash
./scripts/test-library.sh --smoke
```

## Chaining with AI Tools

The same script chain works across tools. The main pattern is:

1. Discover (`find-a-skill.sh` or `find-a-command.sh`)
2. Generate a high-quality prompt (`run-pm.sh`)
3. Execute in your AI tool
4. Validate outputs (`test-a-skill.sh` or `test-library.sh`)

### Claude Code

Run directly from terminal:

```bash
./scripts/find-a-command.sh --keyword roadmap
./scripts/run-pm.sh command plan-roadmap "Q3 strategy for enterprise expansion" --agent claude
```

### Codex

Run directly from terminal:

```bash
./scripts/find-a-command.sh --keyword discovery
./scripts/run-pm.sh command discover "Diagnose activation drop-off in onboarding" --agent codex
```

### VS Code

Use terminal + chat together:

```bash
./scripts/find-a-skill.sh --keyword user-story
./scripts/run-pm.sh skill user-story "Write stories for checkout optimization" --agent print
```

Paste the printed prompt into your AI chat panel in VS Code.

### Cursor

Use the same print-and-paste flow:

```bash
./scripts/find-a-command.sh --keyword prd
./scripts/run-pm.sh command write-prd "Create a PRD for analytics alerts" --agent print
```

Paste the printed prompt into Cursor chat.

### AntiGravity

Use print-and-paste unless your AntiGravity setup has its own CLI bridge:

```bash
./scripts/find-a-command.sh --keyword strategy
./scripts/run-pm.sh command strategy "Define positioning for AI assistant add-on" --agent print
```

Paste the printed prompt into AntiGravity.

### Optional: one-line clipboard handoff (macOS)

If you want faster chaining into any chat UI:

```bash
./scripts/run-pm.sh command discover "Improve trial-to-paid conversion" --agent print | pbcopy
```

## Script Cheat Sheet

- `add-a-skill.sh`: Generate skills from notes or source content.
- `build-a-skill.sh`: Guided wizard to create a skill step by step.
- `find-a-skill.sh`: Search skills by keyword, name, or type.
- `find-a-skill.sh --mode trigger`: Search using trigger-oriented frontmatter like `description`, `best_for`, and `scenarios`.
- `find-a-command.sh`: Search workflow commands.
- `run-pm.sh`: Turn skills/commands into prompts or run in Claude/Codex CLI.
- `test-a-skill.sh`: Validate one skill's quality and structure.
- `test-library.sh`: Validate skills, commands, and catalog output together.
- `check-skill-triggers.py`: Audit description quality and sample trigger cases.
- `zip-a-skill.sh`: Build upload-ready ZIP files for Claude web.
- `package-claude-skills.sh`: Advanced packaging helper (unpacked format).
- `check-skill-metadata.py`: Validate skill frontmatter and required sections.
- `check-command-metadata.py`: Validate command metadata and skill references.
- `generate-catalog.py`: Rebuild `catalog/` indexes.

## Troubleshooting

- `Error: 'claude' command not found`:
  Use `--agent print` and paste the output prompt into Claude manually.
- `Error: 'codex' command not found`:
  Use `--agent print` and paste the output prompt into Codex manually.
- `Error: Skill not found`:
  Run `./scripts/find-a-skill.sh --list-all` and use an exact skill name.
- `Error: Command not found`:
  Run `./scripts/find-a-command.sh --list-all` and use an exact command name.
- `Permission denied`:
  Run `chmod +x ./scripts/*.sh`.
- Paths look broken:
  Run commands from the repo root (`/Users/deanpeters/Code/product-manager-skills`).

## Safety Notes

- These scripts are intended to be deterministic and local-first.
- Read scripts before running if you are unsure, especially in shared environments.
- Repo frontmatter includes `intent` for local authoring, but Claude upload packaging strips unsupported keys and keeps the trigger-oriented `description`.

## Related Docs

- [`../README.md`](../README.md)
- [`../docs/Add-a-Skill Utility Guide.md`](../docs/Add-a-Skill%20Utility%20Guide.md)
- [`../docs/Platform Guides for PMs.md`](../docs/Platform%20Guides%20for%20PMs.md)
- [`../docs/Using PM Skills with Claude Code.md`](../docs/Using%20PM%20Skills%20with%20Claude%20Code.md)
- [`../docs/Using PM Skills with Codex.md`](../docs/Using%20PM%20Skills%20with%20Codex.md)
- [`../docs/Using PM Skills with Cursor.md`](../docs/Using%20PM%20Skills%20with%20Cursor.md)

```

### File: AGENTS.md
```md
# Repository Guidelines

## Operating Philosophy — Pedagogic and Practical in Equal Measure

As much as this repo is for adding skills to your agent, it's equally tasked to **help product managers become more awesome at their craft — and to help them send the ladder down to others.**

Skills here serve both goals simultaneously. The PM using a skill should finish knowing more than when they started — not just have a completed artifact. The reasoning embedded in a skill is what makes the output trustworthy, explainable, and transferable to the next person.

**ABC — Always Be Coaching** is a key governing principle.

This has direct implications for how you work in this repo as an agent:

- **Do not optimize for brevity at the cost of explanation.** Stripping learning scaffolding to tighten a skill is a defect, not an improvement.
- **Anti-patterns are load-bearing.** They teach the human what to watch for in the wild. Do not remove them.
- **Examples show reasoning, not just outputs.** A shorter example that hides the thinking is worse than a longer one that shows it.
- **The dual audience is always both:** the human PM building judgment and the AI agent executing the work. Never optimize for one at the expense of the other.

If you are making efficiency improvements, tighten fluff — not lessons. If you are unsure which is which, leave it in.

---

## Project Structure & Module Organization
- `skills/<skill-name>/SKILL.md` holds each skill. Skill folders use lowercase kebab-case names (e.g., `skills/user-story/SKILL.md`).
- `commands/<command-name>.md` holds reusable orchestration commands that chain local skills.
- `catalog/` holds generated indexes for fast browsing (`skills-by-type.md`, `commands.md`, and YAML indexes).
- `research/` contains reference essays that inform skills.
- `docs/` contains usage guides, including `docs/Using PM Skills with Codex.md`.
- `app/` contains the Streamlit (beta) playground (`app/main.py`) and setup docs (`app/STREAMLIT_INTERFACE.md`).
- Root docs like `README.md`, `CONTRIBUTING.md`, `PLANS.md`, and `CLAUDE.md` explain catalog, contribution flow, and skill distillation.

## Build, Test, and Development Commands
This is a Markdown-first repository with no build system or automated tests.
- `rg --files` lists all files quickly.
- `rg "SKILL.md"` finds skill definitions.
- `rg "skill-name"` verifies references before submitting.
- `./scripts/find-a-command.sh --list-all` lists available workflow commands.
- `./scripts/test-library.sh` validates skills + commands and regenerates catalogs.
- `streamlit run app/main.py` launches the Streamlit (beta) skill playground.

## Coding Style & Naming Conventions
- Write in Markdown with clear headings and short paragraphs.
- Skills must follow the standard sections: Purpose, Key Concepts, Application, Examples, Common Pitfalls, References.
- Include frontmatter fields (`name`, `description`, `type`) at the top of each skill file.
- Keep `name` <= 64 characters and `description` <= 200 characters for Claude web upload compatibility.
- Ensure the skill folder name matches the frontmatter `name` exactly (lowercase kebab-case).
- Use fenced code blocks with language tags for commands or templates.
- Keep language concise and opinionated; avoid filler.

### Interactive Skills
**What:** Multi-turn conversational flows that gather context through sequential questioning and offer intelligent next-step recommendations.

**Characteristics:**
- Asks questions one at a time (or in small batches)
- Uses answers to inform subsequent questions
- Offers **enumerated, context-aware recommendations** for next steps
- Allows user to select by number ("1", "2 & 4") or provide custom input
- Adapts based on user choices

## Testing Guidelines
No automated tests exist. Validate changes by:
- Ensuring linked skill paths resolve (e.g., `skills/prd-development/SKILL.md`).
- Confirming examples and references are accurate and consistent.
- Skimming for structure compliance and readability.
- For Claude web upload, ensure frontmatter is valid YAML and use the packaging helper to generate `Skill.md` copies.

## Operating Principle (Dogfood First)
- Use this repo's own definitions, scripts, and standards before making structural decisions.
- If deciding skill type/category, anchor to local criteria in `README.md`, `CLAUDE.md`, and relevant `SKILL.md` files.
- Prefer proving decisions with repo tools (`scripts/find-a-skill.sh`, `scripts/test-a-skill.sh`, `scripts/check-skill-metadata.py`) over opinion.

## Cross-Repo Boundary
- This repository is the shared PM skills library, not the Productside playbook distribution repo.
- Productside playbook skill content must be created/edited in `/Users/deanpeters/Code/productside_playbook_skills`.
- When supporting Productside work, treat this repo as read-only reference/tooling unless explicitly asked to change this repo.

## Claude Custom Skills Compatibility
- Claude web uploads require `Skill.md` (case-sensitive). Use `scripts/package-claude-skills.sh`.
- Any scripts under a skill should be deterministic, avoid network calls, and be documented in the skill.
- Review skills and scripts for safety before sharing or running.

## Commit & Pull Request Guidelines
- Commit messages in history use the imperative voice with a clear subject (e.g., `Add agent-orchestration-advisor skill`), sometimes followed by an issue tag and an em dash for context.
- PRs should include a short summary, link relevant issues, and note skill type (component/interactive/workflow).
- If adding a new skill, update the catalog in `README.md` to keep counts and tables accurate.

## Release Checklist
- Update skill counts and tables in `README.md`.
- Ensure new skills are linked in the correct section (Component/Interactive/Workflow).
- Spot-check cross-links from `README.md` and `CONTRIBUTING.md`.
- Confirm any renamed skills update paths and references.
- If Streamlit beta changed, update `app/STREAMLIT_INTERFACE.md`, `app/.env.example`, and release notes in `README.md`/`docs/announcements/`.

## Skill Quality Expectations
- **Pedagogic first:** The PM using this skill should know more when they finish than when they started.
- Agent-ready, self-contained, and practical.
- Include at least one concrete example that shows reasoning, not just output.
- Include at least one explicit anti-pattern — this is not optional decoration.
- Define jargon on first use and keep tradeoffs explicit.
- Do not remove explanation, anti-patterns, or examples in the name of brevity. That is the mission, not the padding.

```

### File: CLAUDE.md
```md
# CLAUDE.md — Skill Distillation Protocol

**Purpose:** Instructions for Claude on how to collaborate with Dean to convert raw PM content into formalized skills for this repository.

---

## Project Status (Last updated: Wed Mar 18 2026)

### Current State: v0.75 Released + Pedagogic-First Philosophy Restored

**Released: 46 Skills (Feb 27, 2026)**
- 20 Component Skills (templates/artifacts + finance metrics + career frameworks)
- 20 Interactive Skills (guided discovery + finance advisors + career advisors)
- 6 Workflow Skills (end-to-end processes + meta skill-authoring + executive onboarding)
- License: CC BY-NC-SA 4.0
- All skills restructured to Anthropic-compliant format (`skills/skill-name/SKILL.md`)

**Streamlit (beta) Playground (Feb 27, 2026)**
- Local app in `app/main.py` for browsing and running skills before install
- Environment-variable key handling (no in-app key entry), with provider/model selection
- Provider support: Anthropic, OpenAI, and Ollama
- Workflow UX improvements: phase detection, run-all phases, per-phase output tracking
- Feedback channels linked in-app: GitHub Issues + LinkedIn

**Phase 8: Career & Leadership Skills (COMPLETE)** ✅
- ✅ **4 Skills Released (Feb 27, 2026)** — distilled from two episodes of [The Product Porch](https://the-product-porch-43ca35c0.simplecast.com) podcast
  - [`altitude-horizon-framework`](skills/altitude-horizon-framework/SKILL.md) (Component) — PM→Director mental model: altitude/horizon axes, waiter-to-operator shift, four transition zones, Cascading Context Map. Based on [E42](https://the-product-porch-43ca35c0.simplecast.com/episodes/from-product-manager-to-director-how-to-make-the-shift-part-1)
  - [`director-readiness-advisor`](skills/director-readiness-advisor/SKILL.md) (Interactive) — Coaching across four situations: preparing, interviewing, newly landed, recalibrating. Based on E42
  - [`executive-onboarding-playbook`](skills/executive-onboarding-playbook/SKILL.md) (Workflow) — 30-60-90 day diagnostic playbook for VP/CPO transitions. Based on [E43](https://the-product-porch-43ca35c0.simplecast.com/episodes/becoming-a-vp-cpo-leading-product-at-the-executive-level-part-2)
  - [`vp-cpo-readiness-advisor`](skills/vp-cpo-readiness-advisor/SKILL.md) (Interactive) — Director→VP/CPO coaching; includes CEO interview framework. Based on E43
- **Source transcripts:** `research/product_porch_transcript.making-the-shift-from-pm-to-director-of-product.md` and `research/product_porch_transcript.becoming-a-vp-or-cpo-of-product-at-executive-level.md`
- **Potential follow-on:** VP/CPO→C-suite transition (separate skill set, not yet sourced)

**Phase 6: AI PM Orchestrator Skills (In Progress)**
- ✅ **Skill #34: agent-orchestration-advisor** (Interactive) — Complete
  - Guides multi-agent workflow design
  - Covers 4 dimensions: Multi-Agent Workflows, Cross-Functional AI Pods, Launch Control Tower, Strategic Intent Alignment
  - References context-engineering-advisor as prerequisite
- 📋 **Remaining Skills (Planned):**
  - `ai-product-evals` (Component) — Evaluation frameworks template
  - `ai-observability-framework` (Component) — Tracing and logging guide
  - `ai-maintenance-planning` (Component) — Model drift maintenance template
  - `ai-product-orchestrator` (Workflow) — Complete end-to-end AI PM process

**Phase 7: Finance for Product Managers (COMPLETE)** ✅
- ✅ **7 Skills Released (Feb 8, 2026)**
  - Foundation: 3 component skills covering 32 SaaS finance metrics
  - Decision Frameworks: 3 interactive advisors (feature, channel, pricing)
  - Advanced: 1 comprehensive business health diagnostic
  - Total: 4,290 lines across 7 skills
  - See `docs/Finance Suite Summary.md` for complete overview

**Recent Updates:**
- ✅ **v0.75 Released (Mar 17, 2026):** Restored pedagogic-first philosophy across all governance docs
  - Added Design Philosophy section to `CLAUDE.md`, `CONTRIBUTING.md`, `AGENTS.md`, and `README.md`
  - ABC (Always Be Coaching) and "send the ladder down" named as governing principles throughout
  - Equal-footing framing: agent capability and human PM learning are co-equal goals, neither is a byproduct
  - Named the anti-pattern explicitly: efficiency edits that strip learning scaffolding are defects
  - Added pedagogic checklist item and negative content-removal check to `CONTRIBUTING.md`
  - Added naming conventions (no contributor handles/prefixes) to `CONTRIBUTING.md`
  - Named protected sections explicitly: "Why This Works," Anti-Patterns, consequence chains, educational preambles
  - Added note on external scoring tools optimizing for the wrong rubric
  - Claude Code plugin marketplace badge and coming-soon install snippet added to `README.md`
  - Release note: `docs/announcements/2026-03-17-v0-75-pedagogic-first.md`
- **Open PRs (as of Mar 18, 2026):**
  - #1 KNE-AI — `pm-skill-creator` interactive skill — approved pending rename of frontmatter `name` to `pm-skill-creator`
  - ✅ #2 markphelps — Claude Code plugin marketplace (`marketplace.json`) — **merged Mar 18, 2026**; `.claude-plugin/marketplace.json` now in main
  - #3 popey — efficiency improvements across 46 skills — sent back; structural table consolidations welcome, pedagogic content (Why This Works, Anti-Patterns, educational preambles) must be restored
- ✅ **v0.7 Released (Mar 9, 2026):** Tightened skill quality and discovery standards across the full library
  - Standardized trigger-oriented `description` language so skills more clearly answer "use this when..."
  - Added repo-standard `intent` frontmatter to preserve richer meaning without weakening trigger metadata
  - Added `scripts/check-skill-triggers.py` and wired trigger-readiness checks into `scripts/test-library.sh`
  - Added `find-a-skill.sh --mode trigger` so skill discovery can leverage `description`, `best_for`, and `scenarios`
  - Updated skill-authoring docs and templates so the stronger standard is maintained going forward
- ✅ **v0.5 Streamlit (beta) update (Feb 27, 2026):** Added local playground, multi-provider model selection, and workflow UX fixes for phase-based skills (notably PRD flow behavior)
- ✅ **v0.5 Released (Feb 27, 2026):** Added 4 Career & Leadership skills (Phase 8) distilled from The Product Porch podcast episodes on PM→Director and Director→VP/CPO transitions
- ✅ **v0.4 Released (Feb 10, 2026):** Fixed facilitation protocol regression and standardized guided interaction behavior
  - Root cause: brevity-focused rewriting could strip facilitation modality details from interactive flows
  - Resolution: established `skills/workshop-facilitation/SKILL.md` as source of truth and linked it across interactive and facilitation-heavy workflow skills
  - Added heads-up start, context-dump bypass, best-guess mode, progress labels, and interruption handling
  - Implemented by Codex after diagnosing expected-vs-actual facilitation mismatch
- ✅ **Phase 7 Complete:** 7 finance skills released (Feb 8, 2026)
- All skills alphabetically ordered within each category (Component, Interactive, Workflow)
- Enhanced documentation in `/docs`:
  - `Using PM Skills with Claude.md` — Comprehensive guide for Claude Code (CLI) and Claude Cowork (workspace)
  - `Using PM Skills with Codex.md` — Guide for OpenAI Codex
  - `Building PM Skills.md` — Contributor guide
  - `Finance Suite Summary.md` — Complete overview of 7 finance skills (NEW)
- Streamlit beta documentation in `/app`:
  - `app/STREAMLIT_INTERFACE.md` — App architecture, setup, and deployment notes
  - `app/.env.example` — Multi-provider key/model configuration template
- Updated `CONTRIBUTING.md` with enhanced guidelines
- Research documents added to `/research`:
  - `Context Engineering for Product Managers.md`
  - `The Product Manager as an Orchestrator.md`
  - `finance/` — 4 finance research documents (3,014 lines)

**Source Materials for Phase 6:**
- Dean's Substack articles:
  - "Vibe First, Validate Fast, Verify Fit" (PoL Probes)
  - "AI-First Is Cute. AI-Shaped Is Survival." (5 competencies)
  - "Context Stuffing Is Not Context Engineering"
- Teresa Torres: *Continuous Discovery Habits* (5 AI PM disciplines)
- Marty Cagan: *Empowered* (4 big risks in AI era)
- Productside Blueprint: Orchestration framework

**Source Materials for Phase 7 (Finance):**
- `research/finance/Finance for Product Managers.md` — 32 metrics with quizzes
- `research/finance/Finance_QuickRef.md` — One-page lookup table
- `research/finance/Finance_For_PMs.Putting_It_Together_Synthesis.md` — Decision frameworks
- `research/finance/Finance_Metrics_Additions_Reference.md` — Common mistakes reference

**What's Next:**
- Complete remaining Phase 6 skills (evals, observability, maintenance)
- Build final workflow skill that orchestrates all 5 AI PM disciplines
- Potential Phase 8: Pricing & Monetization Suite (7 comprehensive pricing skills)
  - Value-based pricing framework
  - Willingness-to-pay research
  - Packaging architecture advisor
  - Pricing psychology guide
  - Price testing methodology
  - Competitive pricing analysis
  - Monetization model advisor

**Important Notes for Claude:**
- Always check `git status` and recent commits before starting new work
- Dogfood first: use this repo's own standards/scripts/skill definitions as the source of truth before making recommendations
- For facilitation behavior changes, update `skills/workshop-facilitation/SKILL.md` first, then use `docs/maintenance/facilitation-scope.md` to find and patch all linked skills
- For category decisions (Component vs Interactive vs Workflow), anchor to criteria in this file and `README.md` before giving an answer
- Prefer evidence from local tools (`scripts/find-a-skill.sh`, `scripts/test-a-skill.sh`, `scripts/check-skill-metadata.py`) over subjective preference
- Skills must follow standard anatomy: Purpose, Key Concepts, Application, Examples, Common Pitfalls, References
- Interactive skills require 3-5 adaptive questions, enumerated options (3-5 choices), handle single/multi-selection
- All skills include YAML frontmatter: `name`, `description`, `intent`, `type`
- Cross-reference related skills in References section
- For Claude web custom skills: keep `name` <= 64 chars and `description` <= 200 chars, and ensure folder name matches `name`
- Claude web uploads require `Skill.md` (case-sensitive); use `scripts/package-claude-skills.sh`
- Scripts should be deterministic, avoid network calls, and be documented in the skill file
- If Streamlit beta behavior or provider support changes, update both `app/STREAMLIT_INTERFACE.md` and README release notes in the same PR

**Automation Tools:**
- **`scripts/add-a-skill.sh`** — Agent-agnostic utility for automated skill creation
  - Converts raw PM content into skills via 8-step workflow
  - Supports Claude Code, Manual mode (`--agent manual`), and custom adapters
  - Includes analysis, planning, generation, validation, and documentation steps
  - See `docs/Add-a-Skill Utility Guide.md` for complete guide
  - Use for semi-automated skill creation from research documents or workshop notes
- **`scripts/build-a-skill.sh`** — Interactive wizard for guided skill construction
  - Prompts section-by-section (Purpose → References)
  - Writes deterministic files (`SKILL.md` + optional examples/template)
  - Validates strict conformance before optional git staging
- **`scripts/find-a-skill.sh`** — Ranked skill discovery helper
  - Search by name, type, and keyword
  - Ranking priority: exact name > frontmatter > section text
- **`scripts/test-a-skill.sh`** — Skill quality gate
  - Runs strict conformance checks (`check-skill-metadata.py`)
  - Verifies linked `skills/*/SKILL.md` references resolve
  - Optional `--smoke` checks for section/readiness quality

---

## Design Philosophy — Pedagogic and Practical in Equal Measure

As much as this repo is for adding skills to your agent, it's equally tasked to **help product managers become more awesome at their craft — and to help them send the ladder down to others.**

Skills here serve both goals simultaneously. They equip AI agents to do PM work at a professional level, and they teach the human PM the *why* behind the framework — so they can explain it, adapt it, and pass it on. Neither goal is optional. Neither is more important than the other.

**ABC — Always Be Coaching** is a key governing principle. Every skill should leave the person using it knowing more than when they started. The same applies to how you work as an agent in this repo: coaching is not optional, it is the work.

This means:
- Explanation is load-bearing, not decorative
- Anti-patterns are as important as correct patterns
- Examples show reasoning, not just outputs
- Stripping learning scaffolding to tighten copy is a defect, not an improvement

The dual audience is always both: **the human PM building judgment** and **the AI agent executing the work.** Never optimize for one at the expense of the other.

---

## Your Role

You are Dean's **pedagogic collaborator and skill extraction partner**. Your job is to take messy, real-world PM content (prompts, flows, frameworks, workshop notes) and distill it into **clean, agent-ready skills that also teach the humans who use them**.

You are **not** a passive transcriber. You:
- Ask clarifying questions when the logic is ambiguous
- Identify missing pieces (prerequisites, failure modes, examples)
- Push back when structure is weak or tone drifts generic
- Push back when explanation is stripped in favor of brevity
- Suggest better frameworks when you see them
- Preserve the teaching in every edit — the lesson is the point

If you are using Codex to work with this repo, see `docs/Using PM Skills with Codex.md` for the recommended workflow.

---

## What Dean Will Provide

Dean will supply one or more of these:
- **Multi-turn prompt sequences** (e.g., a 5-step discovery interview flow)
- **Workshop frameworks** (e.g., roadmap planning canvas)
- **Decision trees** (e.g., "How to choose the right metric")
- **Real client artifacts** (anonymized PRDs, stakeholder maps, discovery notes)
- **Rough notes or transcripts** from sessions
- **Individual artifact templates** (user stories, positioning statements, epics)

Your job: **turn it into a skill.**

---

## Three Types of Skills

### Component Skills
**What:** Individual deliverables or artifacts (user stories, epics, positioning statements, PRD sections, OKRs, etc.)

**Characteristics:**
- Self-contained, reusable building blocks
- Simpler structure (still has steps, but fewer moving parts)
- Focuses on "how to create X well"
- Gets referenced by workflow skills

**Example:** `user-story.md` — how to write a proper user story with acceptance criteria

---

### Workflow Skills
**What:** Multi-step processes or frameworks (discovery interviews, roadmap planning, stakeholder analysis, etc.)

**Characteristics:**
- Orchestrates multiple activities
- Often references component skills
- Includes decision points and branching logic
- Focuses on "how to complete process Y"

**Exam
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
