---
id: codebuffai-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:07.443699
---

# KNOWLEDGE EXTRACT: CodebuffAI
> **Extracted on:** 2026-03-30 17:34:53
> **Source:** CodebuffAI

---

## File: `codebuff-community.md`
```markdown
# 📦 CodebuffAI/codebuff-community [🔖 PENDING/APPROVE]
🔗 https://github.com/CodebuffAI/codebuff-community


## Meta
- **Stars:** ⭐ 37 | **Forks:** 🍴 9
- **Language:** TypeScript | **License:** MIT
- **Last updated:** 2026-03-06
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A showcase of Codebuff projects created by our community

## README (trích đầu)
```
# Codebuff Community

Welcome to the [Codebuff](https://codebuff.com) community repository! This is where you'll find starter templates and showcase projects created by our community.

## Getting Started

First, install Codebuff globally:

```bash
npm install -g codebuff
```

## Starting a Project

Use codebuff to create a new project from a template. Templates are the names of subdirectories in `/starter-templates` or `/showcase`:
```bash
codebuff --create nextjs my-project
```

OR

You can also start codebuff in an existing project directory:
```bash
cd my-project
codebuff
```

## Repository Structure

### `/starter-templates`

A collection of pre-configured project templates for various tech stacks. These templates provide a solid foundation for building new projects with best practices and common configurations already set up.

### `/showcase`

A curated collection of projects built by the community using Codebuff. Get inspired by what others have created!

## Contributing

We'd love to see what you build with Codebuff! You can contribute in two ways:

1. **Add a Starter Template**: Have a well-structured project setup that others might find useful? Share it as a starter template!

2. **Share Your Project**: Built something cool with Codebuff? Open a PR with a submodule linking to your public repo (if you don't know what that means, ask Codebuff to do it for you). Help us inspire others!

To contribute:
1. Fork this repository
2. Add your project to either `/starter-templates` or `/showcase`. For showcase projects, you can either:
   - Copy your project files directly into the showcase directory
   - Add your GitHub repository as a git submodule in the showcase directory
3. Submit a pull request

Please ensure your contribution includes clear documentation and follows our existing structure.

## License

This repository is MIT licensed. See [LICENSE](./LICENSE) for details.

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `codebuff.md`
```markdown
# 📦 CodebuffAI/codebuff [🔖 PENDING/APPROVE]
🔗 https://github.com/CodebuffAI/codebuff
🌐 https://codebuff.com

## Meta
- **Stars:** ⭐ 4338 | **Forks:** 🍴 491
- **Language:** TypeScript | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Generate code from the terminal!

## README (trích đầu)
```
# Codebuff & Freebuff

**[Codebuff](https://codebuff.com)** is an open-source AI coding assistant that edits your codebase through natural language instructions. **[Freebuff](https://www.npmjs.com/package/freebuff)** is the free, ad-supported version — no subscription, no credits, no configuration.

Instead of using one model for everything, Codebuff coordinates specialized agents that work together to understand your project and make precise changes.

<div align="center">
  <img src="./assets/codebuff-vs-claude-code.png" alt="Codebuff vs Claude Code" width="400">
</div>

Codebuff beats Claude Code at 61% vs 53% on [our evals](../../../README.md) across 175+ coding tasks over multiple open-source repos that simulate real-world tasks.


## How it works

When you ask Codebuff to "add authentication to my API," it might invoke:

1. A **File Picker Agent** to scan your codebase to understand the architecture and find relevant files
2. A **Planner Agent** to plan which files need changes and in what order
3. An **Editor Agent** to make precise edits
4. A **Reviewer Agent** to validate changes

<div align="center">
  <img src="./assets/multi-agents.png" alt="Codebuff Multi-Agents" width="250">
</div>

This multi-agent approach gives you better context understanding, more accurate edits, and fewer errors compared to single-model tools.

## CLI: Install and start coding

Install:

```bash
npm install -g codebuff
```

Run:

```bash
cd your-project
codebuff
```

Then just tell Codebuff what you want and it handles the rest:

- "Fix the SQL injection vulnerability in user registration"
- "Add rate limiting to all API endpoints"
- "Refactor the database connection code for better performance"

Codebuff will find the right files, makes changes across your codebase, and runs tests to make sure nothing breaks.

## Create custom agents

To get started building your own agents, start Codebuff and run the `/init` command:

```bash
codebuff
```

Then inside the CLI:

```
/init
```

This creates:
```
knowledge.md               # Project context for Codebuff
.agents/
└── types/                 # TypeScript type definitions
    ├── agent-definition.ts
    ├── tools.ts
    └── util-types.ts
```

You can write agent definition files that give you maximum control over agent behavior.

Implement your workflows by specifying tools, which agents can be spawned, and prompts. We even have TypeScript generators for more programmatic control.

For example, here's a `git-committer` agent that creates git commits based on the current git state. Notice that it runs `git diff` and `git log` to analyze changes, but then hands control over to the LLM to craft a meaningful commit message and perform the actual commit.

```typescript
export default {
  id: 'git-committer',
  displayName: 'Git Committer',
  model: 'openai/gpt-5-nano',
  toolNames: ['read_files', 'run_terminal_command', 'end_turn'],

  instructionsPrompt:
    'You create meaningful git commits by analyzing changes, reading 
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

