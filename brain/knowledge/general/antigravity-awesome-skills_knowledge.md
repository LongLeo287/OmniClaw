---
id: antigravity-awesome-skills-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:18:47.205884
---

# 📦 sickn33/antigravity-awesome-skills [GRAPHQL — Stream 4]
🔗 https://github.com/sickn33/antigravity-awesome-skills

## Meta
- **Size:** ~44 MB | **Stars:** ⭐ 28778 | **Forks:** 🍴 4818
- **Language:** Python | **License:** MIT
- **Updated:** 2026-03-30
- **Topics:** agentic-skills, ai-agents, antigravity, claude-code, mcp, ai-workflows, codex-cli, developer-tools, gemini-cli, skill-library

## Description:
Installable GitHub library of 1,326+ agentic skills for Claude Code, Cursor, Codex CLI, Gemini CLI, Antigravity, and more. Includes installer CLI, bundles, workflows, and official/community skill collections.

## README (FULL)
```markdown
<!-- registry-sync: version=9.2.0; skills=1340; stars=28354; updated_at=2026-03-29T16:41:05+00:00 -->
# 🌌 Antigravity Awesome Skills: 1,340+ Agentic Skills for Claude Code, Gemini CLI, Cursor, Copilot & More

> **Installable GitHub library of 1,340+ agentic skills for Claude Code, Cursor, Codex CLI, Gemini CLI, Antigravity, and other AI coding assistants.**

Antigravity Awesome Skills is a GitHub repository and installer CLI for reusable `SKILL.md` playbooks. Instead of collecting random prompts, you get a searchable, installable skill library for planning, coding, debugging, testing, security review, infrastructure work, product workflows, and growth tasks across the major AI coding assistants.

**Start here:** [Star the repo](https://github.com/sickn33/antigravity-awesome-skills/stargazers) · [Install in 1 minute](#installation) · [Plugins for Claude Code and Codex](../../../core/security/QUARANTINE/vetted/repos/claude_code_game_studios/docs/engine_reference/unity/PLUGINS.md) · [Choose your tool](#choose-your-tool) · [Best skills by tool](#best-skills-by-tool) · [Bundles](../../../core/security/QUARANTINE/vetted/repos/openclaw/docs/plugins/bundles.md) · [Workflows](workflows.md)

[![GitHub stars](https://img.shields.io/badge/⭐%2028%2C000%2B%20Stars-gold?style=for-the-badge)](https://github.com/sickn33/antigravity-awesome-skills/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Anthropic-purple)](https://claude.ai)
[![Cursor](https://img.shields.io/badge/Cursor-AI%20IDE-orange)](https://cursor.sh)
[![Codex CLI](https://img.shields.io/badge/Codex%20CLI-OpenAI-green)](https://github.com/openai/codex)
[![Gemini CLI](https://img.shields.io/badge/Gemini%20CLI-Google-blue)](https://github.com/google-gemini/gemini-cli)
[![Latest Release](https://img.shields.io/github/v/release/sickn33/antigravity-awesome-skills?display_name=tag&style=for-the-badge)](https://github.com/sickn33/antigravity-awesome-skills/releases/latest)
[![Install with NPX](https://img.shields.io/badge/Install-npx%20antigravity--awesome--skills-black?style=for-the-badge&logo=npm)](#installation)
[![Kiro](https://img.shields.io/badge/Kiro-AWS-orange?style=for-the-badge)](https://kiro.dev)
[![Copilot](https://img.shields.io/badge/Copilot-GitHub-lightblue?style=for-the-badge)](https://github.com/features/copilot)
[![OpenCode](https://img.shields.io/badge/OpenCode-CLI-gray?style=for-the-badge)](https://github.com/opencode-ai/opencode)
[![Antigravity](https://img.shields.io/badge/Antigravity-AI%20IDE-red?style=for-the-badge)](https://github.com/sickn33/antigravity-awesome-skills)

**Current release: V9.2.0.** Trusted by 28k+ GitHub stargazers, this repository combines official and community skill collections with bundles, workflows, installation paths, and docs that help you go from first install to daily use quickly.

## Why Developers Star This Repo

- **Installable, not just inspirational**: use `npx antigravity-awesome-skills` to put skills where your tool expects them.
- **Built for major agent workflows**: Claude Code, Cursor, Codex CLI, Gemini CLI, Antigravity, Kiro, OpenCode, Copilot, and more.
- **Broad coverage with real utility**: 1,340+ skills across development, testing, security, infrastructure, product, and marketing.
- **Faster onboarding**: bundles and workflows reduce the time from "I found this repo" to "I used my first skill".
- **Useful whether you want breadth or curation**: browse the full catalog, start with top bundles, or compare alternatives before installing.

## Table of Contents

- [🚀 New Here? Start Here!](#new-here-start-here)
- [📖 Complete Usage Guide](usage.md) - **Start here if confused after installation!**
- [🧠 Core Concepts](#core-concepts)
- [🔌 Compatibility &amp; Invocation](#compatibility--invocation)
- [🛠️ Installation](#installation)
- [🧩 Plugins For Claude Code And Codex](#plugins-for-claude-code-and-codex)
- [🧭 Integration Guides](#integration-guides)
- [🧰 Best Skills By Tool](#best-skills-by-tool)
- [❓ Quick FAQ](#quick-faq)
- [🛡️ Security Posture](#security-posture)
- [🧯 Troubleshooting](#troubleshooting)
- [🎁 Curated Collections (Bundles)](#curated-collections)
- [🧭 Antigravity Workflows](#antigravity-workflows)
- [⚖️ Alternatives &amp; Comparisons](#alternatives--comparisons)
- [📦 Features & Categories](#features--categories)
- [📚 Browse 1,340+ Skills](#browse-1340-skills)
- [🤝 Contributing](#contributing)
- [💬 Community](#community)
- [☕ Support the Project](#support-the-project)
- [🏆 Credits &amp; Sources](#credits--sources)
- [👥 Repo Contributors](#repo-contributors)
- [⚖️ License](#license)
- [🌟 Star History](#star-history)

---

## New Here? Start Here!

If you searched for **Claude Code skills**, **Cursor skills**, **Codex CLI skills**, **Gemini CLI skills**, or **AI agent skills on GitHub**, this is the fastest path to installing a serious working library and using it the same day.

### 1. 🐣 Context: What is this?

**Antigravity Awesome Skills** (Release 9.2.0) is a large, installable skill library for AI coding assistants. It includes onboarding docs, bundles, workflows, generated catalogs, and a CLI installer so you can move from discovery to actual usage without manually stitching together dozens of repos.

AI agents are smart, but they still need **task-specific operating instructions**. Skills are focused markdown playbooks that teach an agent how to perform a workflow repeatedly and with better context, whether that means deployment, API design, testing, product strategy, SEO, or documentation.

### 2. ⚡️ Quick Start (1 minute)

Install once; then use Starter Packs in [brain/knowledge/docs_legacy/users/bundles.md](../../../core/security/QUARANTINE/vetted/repos/openclaw/docs/plugins/bundles.md) to focus on your role.

1. **Install**:

   ```bash
   # Default: ~/.gemini/antigravity/skills (Antigravity global). Use --path for other locations.
   npx antigravity-awesome-skills
   ```
   The npm installer uses a shallow clone by default so first-run installs stay lighter than a full repository history checkout.
2. **Verify**:

   ```bash
   test -d ~/.gemini/antigravity/skills && echo "Skills installed in ~/.gemini/antigravity/skills"
   ```
3. **Run your first skill**:

   > "Use **@brainstorming** to plan a SaaS MVP."
   >
4. **Pick a bundle**:

   - **Web Dev?** start with `Web Wizard`.
   - **Security?** start with `Security Engineer`.
   - **General use?** start with `Essentials`.

### 3. 🧠 How to use

Once installed, just ask your agent naturally:

> "Use the **@brainstorming** skill to help me plan a SaaS."
> "Run **@lint-and-validate** on this file."

👉 **NEW:** [**Complete Usage Guide - Read This First!**](usage.md) (answers: "What do I do after installation?", "How do I execute skills?", "What should prompts look like?")

👉 **[Full Getting Started Guide](../bmad_repo/getting-started.md)**

---

## Core Concepts

Before you compare bundles or start installing tool-specific paths, it helps to separate four ideas:

- **Skills**: reusable `SKILL.md` playbooks that teach an AI assistant how to execute a workflow well.
- **MCP tools**: integrations and external capabilities the assistant can call. Tools provide actions; skills provide operating instructions.
- **Plugins**: installable, marketplace-friendly distributions of the repository for Claude Code and Codex, including root plugins and curated bundle plugins.
- **Bundles**: curated recommendations for which skills to start with for a role or domain.
- **Workflows**: ordered execution playbooks that show how to combine multiple skills step by step.

If you want the clearest explanation of **skills vs MCP/tools**, start here:

- [Skills vs MCP Tools](brain/knowledge/docs_legacy/users/skills-vs-mcp-tools.md)
- [Plugins for Claude Code and Codex](../../../core/security/QUARANTINE/vetted/repos/claude_code_game_studios/docs/engine_reference/unity/PLUGINS.md)
- [Bundles](../../../core/security/QUARANTINE/vetted/repos/openclaw/docs/plugins/bundles.md)
- [Workflows](workflows.md)

## Integration Guides

If your real question is "how do I use Antigravity Awesome Skills with my tool?", use the matching guide:

- **[Claude Code](brain/knowledge/docs_legacy/users/claude-code-skills.md)**: install paths, starter prompts, plugin marketplace flow, and first-use guidance.
- **[Cursor](brain/knowledge/docs_legacy/users/cursor-skills.md)**: chat-first usage, frontend/full-stack starter skills, and practical prompts.
- **[Codex CLI](brain/knowledge/docs_legacy/users/codex-cli-skills.md)**: planning, implementation, debugging, testing, and review loops for local coding work.
- **[Gemini CLI](brain/knowledge/docs_legacy/users/gemini-cli-skills.md)**: broad engineering, agent systems, integrations, and AI workflow coverage.
- **[AI agent skills guide](brain/knowledge/docs_legacy/users/ai-agent-skills.md)**: how to evaluate this repo against broader or narrower alternatives.

## Quick FAQ

### What is Antigravity Awesome Skills?

It is an installable GitHub library of reusable `SKILL.md` playbooks for Claude Code, Cursor, Codex CLI, Gemini CLI, Antigravity, and related AI coding assistants.

### How do I install it?

Use `npx antigravity-awesome-skills`, or a tool-specific flag like `--codex`, `--cursor`, `--gemini`, or `--claude` when you want the installer to target a specific skills directory.

### What is the difference between skills and MCP tools?

Skills are reusable playbooks that tell an AI assistant how to execute a workflow. MCP tools expose external systems or actions the assistant can call. Skills guide behavior; MCP tools provide capabilities.

### What is the difference between bundles and workflows?

Bundles are curated sets of recommended skills. Workflows are ordered execution playbooks for concrete outcomes.

For the expanded version, read [FAQ](faq.md).

---

## Compatibility & Invocation

These skills follow the universal **SKILL.md** format and work with any AI coding assistant that supports agentic skills.

| Tool                  | Type | Invocation Example                  | Path                                                                      |
| :-------------------- | :--- | :---------------------------------- | :------------------------------------------------------------------------ |
| **Claude Code** | CLI  | `>> /skill-name help me...`       | `.claude/skills/`                                                       |
| **Gemini CLI**  | CLI  | `(User Prompt) Use skill-name...` | `.gemini/skills/`                                                       |
| **Codex CLI**   | CLI  | `(User Prompt) Use skill-name...` | `.codex/skills/`                                                        |
| **Kiro CLI**    | CLI  | `(Auto) Skills load on-demand`    | Global:`~/.kiro/skills/` · Workspace: `.kiro/skills/`                |
| **Kiro IDE**    | IDE  | `/skill-name or (Auto)`           | Global:`~/.kiro/skills/` · Workspace: `.kiro/skills/`                |
| **Antigravity** | IDE  | `(Agent Mode) Use skill...`       | Global:`~/.gemini/antigravity/skills/` · Workspace: `.agent/skills/` |
| **Cursor**      | IDE  | `@skill-name (in Chat)`           | `.cursor/skills/`                                                       |
| **Copilot**     | Ext  | `(Paste content manually)`        | N/A                                                                       |
| **OpenCode**    | CLI  | `opencode run @skill-name`        | `.agents/skills/`                                                       |
| **AdaL CLI**    | CLI  | `(Auto) Skills load on-demand`    | `.adal/skills/`                                                         |

> [!TIP]
> **Default installer path**: `~/.gemini/antigravity/skills` (Antigravity global). Use `--path ~/.agent/skills` for workspace-specific install. For manual clone, `.agent/skills/` works as workspace path for Antigravity.
> **OpenCode Path Update**: opencode path is changed to `.agents/skills` for global skills. See [Place Files](https://opencode.ai/brain/knowledge/docs_legacy/skills/#place-files) directive on OpenCode Docs.

> [!TIP]
> **Windows Users**: use the standard install commands. The legacy `core.symlinks=true` / Developer Mode workaround is no longer required for this repository.

## Installation

To use these skills with **Claude Code**, **Gemini CLI**, **Codex CLI**, **Kiro CLI**, **Kiro IDE**, **Cursor**, **Antigravity**, **OpenCode**, or **AdaL**:

### Option A: npx (recommended)

```bash
npx antigravity-awesome-skills
```

2. Verify the default install:

```bash
test -d ~/.gemini/antigravity/skills && echo "Skills installed"
```

3. Use your first skill:

```text
Use @brainstorming to plan a SaaS MVP.
```

4. Browse starter collections in [`brain/knowledge/docs_legacy/users/bundles.md`](../../../core/security/QUARANTINE/vetted/repos/openclaw/docs/plugins/bundles.md) and execution playbooks in [`brain/knowledge/docs_legacy/users/workflows.md`](workflows.md).

### Option B: Claude Code plugin marketplace

If you use Claude Code and prefer the plugin marketplace flow, this repository now ships a root `.claude-plugin/marketplace.json`:

```text
/plugin marketplace add sickn33/antigravity-awesome-skills
/plugin install antigravity-awesome-skills
```

This installs the same repository-backed skill library through Claude Code's plugin marketplace entrypoint.

The Claude plugin is a plugin-safe filtered distribution of the repo. Skills that still contain host-specific paths or undeclared setup remain in the repository, but are excluded from the plugin until they are hardened.

### Option C: Codex plugin marketplace metadata

If you use Codex and prefer a marketplace-style plugin source instead of copying skills into `.codex/skills/`, this repository now ships:

- `.agents/plugins/marketplace.json`
- `plugins/antigravity-awesome-skills/.codex-plugin/plugin.json`

The Codex plugin points at the same curated `skills/` tree through a repo-local plugin entry, so the library can be exposed as an installable Codex plugin source without duplicating the catalog.

Bundle users can also install focused Claude Code and Codex bundle plugins from the generated marketplace metadata instead of taking the full library at once.

Like the Claude distribution, the Codex plugin only exposes plugin-safe skills. Repo-only skills are still available through clone or installer flows while they are being hardened for marketplace use.

## Plugins for Claude Code and Codex

Release `9.0.0` formalizes plugins as a first-class distribution model for this repository.

- The **full library install** remains the broadest path: use `npx antigravity-awesome-skills --claude` or `--codex` when you want the largest available catalog.
- The **root plugin** gives Claude Code or Codex a marketplace-friendly installable distribution of the repository.
- **Bundle plugins** give you narrower role-based installs such as `Essentials`, `Security Engineer`, or `Web Wizard`.
- Plugin distributions are intentionally **plugin-safe**. Skills that still depend on host-specific paths, undeclared setup, or extra hardening remain in the repository, but stay out of marketplace publication until they are ready.

If you want the full explanation of root plugins, bundle plugins, full-library installs, and the difference between Claude Code and Codex plugin surfaces, read:

- [Plugins for Claude Code and Codex](../../../core/security/QUARANTINE/vetted/repos/claude_code_game_studios/docs/engine_reference/unity/PLUGINS.md)

## Choose Your Tool

| Tool           | Install                                            
```

---
*Stream 4: GraphQL Direct Mode | Extracted: 2026-03-30 22:15 | AI OS Corp*
