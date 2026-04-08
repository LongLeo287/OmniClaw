# Contributing to Awesome OpenClaw Agents

We welcome community agents! Submit yours and get it listed on [crewclaw.com/agents](https://crewclaw.com/agents?utm_source=github&utm_medium=contributing&utm_campaign=submit).

---

## Agent File System

Each agent is more than a prompt. It's a full operating system.

```
agents/[category]/[agent-name]/
├── SOUL.md          ← Identity & personality (required)
├── README.md        ← Description & use cases (required)
├── AGENTS.md        ← Operating rules & instructions (optional)
├── HEARTBEAT.md     ← Wake-up checklist (optional)
└── WORKING.md       ← Starting task template (optional)
```

**SOUL.md** and **README.md** are required. The rest are optional but make your agent production-ready.

---

## Submit Your Agent

### Option 1: Pull Request (recommended)

**Step 1:** Fork & clone

```bash
git clone https://github.com/YOUR-USERNAME/awesome-openclaw-agents.git
cd awesome-openclaw-agents
```

**Step 2:** Create your agent folder

```bash
mkdir -p agents/[category]/[agent-name]
```

Categories: `business`, `creative`, `data`, `development`, `devops`, `ecommerce`, `education`, `finance`, `freelance`, `healthcare`, `hr`, `legal`, `marketing`, `personal`, `productivity`, `real-estate`, `saas`, `security`

**Step 3:** Write your SOUL.md (required)

Who is this agent? What's their personality?

```markdown
# Agent Name

Brief description of the agent.

## Core Identity

- **Role:** What the agent does
- **Personality:** How it behaves
- **Communication:** How it talks

## Responsibilities

1. **Primary Task**
   - Detail 1
   - Detail 2

## Behavioral Guidelines

### Do:
- Good behavior 1

### Don't:
- Bad behavior 1

## Example Interactions

**User:** Example prompt
**Agent:** Example response
```

**Step 4:** Write your README.md (required)

```markdown
# Agent Name

> One-line description

## Overview

What this agent does and why it's useful.

## Use Cases

| Request | Output |
|---------|--------|
| Example 1 | Result 1 |

## Files

| File | Purpose |
|------|---------|
| SOUL.md | Agent identity and personality |
| AGENTS.md | Operating rules |
| HEARTBEAT.md | Wake-up checklist |
| WORKING.md | Starting task |

## Author

Created by [@your-username](https://github.com/your-username)
```

**Step 5:** Add AGENTS.md (optional)

How should the agent operate? What are the rules?

```markdown
# AGENTS.md — Operating Rules

## Workspace
- Read/write files in your workspace directory
- Store findings in memory/ folder
- Log daily activity in memory/YYYY-MM-DD.md

## Communication
- Post updates to task threads
- Use @mentions to notify other agents
- Keep messages concise and actionable

## Tools
- File system: read, write, search
- Shell: run scripts, check logs
- Web: browse, research, fetch data

## Rules
- Always check WORKING.md on startup
- Update WORKING.md after completing a task
- Never make decisions outside your domain
- Ask for clarification instead of guessing
```

**Step 6:** Add HEARTBEAT.md (optional)

What should the agent check every time it wakes up?

```markdown
# HEARTBEAT.md — Wake-Up Checklist

## On Wake
- [ ] Read WORKING.md for current task
- [ ] Check for @mentions and notifications
- [ ] Review assigned tasks

## Periodic
- [ ] Scan activity feed for relevant updates
- [ ] Check if blocked tasks can be unblocked
- [ ] Update daily notes in memory/

## Stand Down
- If no tasks and no mentions, reply HEARTBEAT_OK
```

**Step 7:** Add WORKING.md (optional)

What's the agent's starting state?

```markdown
# WORKING.md — Current State

## Current Task
No active task. Waiting for assignment.

## Context
- Agent deployed and ready
- All integrations connected

## Next Steps
1. Check task board for new assignments
2. Review any pending @mentions
3. Begin work on highest priority item
```

**Step 8:** Add entry to `agents.json`

```json
{
  "id": "your-agent-name",
  "category": "category",
  "name": "Your Agent Name",
  "role": "One-line role description",
  "path": "agents/category/your-agent-name/SOUL.md",
  "deploy": "https://crewclaw.com/create-agent"
}
```

**Step 9:** Submit PR

```bash
git add .
git commit -m "Add [AgentName] agent template"
git push origin main
```

### Option 2: Issue

Don't want to set up a PR? Use the **[Submit Your Agent](https://github.com/mergisi/awesome-openclaw-agents/issues/new?template=agent-submission.md)** issue template. Paste your SOUL.md and we'll add it for you.

---

## What Happens After Merge

1. Your agent appears in the [registry](https://github.com/mergisi/awesome-openclaw-agents/tree/main/agents)
2. Listed on [crewclaw.com/agents](https://crewclaw.com/agents?utm_source=github&utm_medium=contributing&utm_campaign=listed) with deploy button
3. You get credited as the author
4. Community can deploy your agent with one click

---

## Submission Tiers

| Tier | Files | Badge |
|------|-------|-------|
| Basic | SOUL.md + README.md | Community Agent |
| Standard | + AGENTS.md | Production Agent |
| Full | + HEARTBEAT.md + WORKING.md | Full Agent OS |

Full submissions get highlighted in the registry.

---

## Style Guidelines

- **Agent names:** Descriptive. `CodeReviewer` not `CR`
- **SOUL.md:** Clear headers, example interactions, specific behavioral guidelines
- **AGENTS.md:** Concrete rules, not vague suggestions
- **HEARTBEAT.md:** Actionable checklist, not prose
- **README:** Start with name + one-liner, include use case table, credit author

---

## PR Checklist

- [ ] SOUL.md follows the template above
- [ ] README.md included
- [ ] Entry added to `agents.json`
- [ ] Agent tested (works with OpenClaw or similar framework)
- [ ] No broken links
- [ ] (Optional) AGENTS.md, HEARTBEAT.md, WORKING.md included

---

## Review Process

1. Maintainer reviews within 48 hours
2. Feedback if changes needed
3. Merged and deployed to crewclaw.com/agents

Questions? [Open a discussion](https://github.com/mergisi/awesome-openclaw-agents/discussions).
