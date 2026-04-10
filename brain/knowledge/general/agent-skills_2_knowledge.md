# Knowledge Dump for agent-skills_2

## File: agents.md
```
# AGENTS.md

This file provides guidance to AI coding agents (Claude Code, Cursor, Copilot, etc.) when working with code in this repository.

For the complete Agent Skills specification, see: https://agentskills.io/specification

## Repository Overview

A collection of skills for coding agents for working with Neon Serverless Postgres. Skills are packaged instructions and documentation that extend the agent's capabilities.

## Creating a New Skill

### Directory Structure

```
skills/
  {skill-name}/           # kebab-case directory name
    SKILL.md              # Required: skill definition
    references/           # Optional: additional documentation
      REFERENCE.md        # Detailed technical reference
      {topic}.md          # Domain-specific files
    scripts/              # Optional: executable scripts
      {script-name}.sh    # Bash scripts (preferred)
    assets/               # Optional: static resources
      templates/          # Document/config templates
      images/             # Diagrams, examples
```

### Naming Conventions

- **Skill directory**: kebab-case, must match `name` in frontmatter (e.g., `neon-postgres`)
- **Name field**: 1-64 chars, lowercase alphanumeric and hyphens only, no consecutive hyphens (`--`), must not start/end with `-`
- **SKILL.md**: Always uppercase, always this exact filename
- **Scripts**: `kebab-case.sh` (e.g., `deploy.sh`, `fetch-logs.sh`)

### SKILL.md Format

The `SKILL.md` file must contain YAML frontmatter followed by Markdown content.

#### Frontmatter (required fields)

```yaml
---
name: skill-name
description: A description of what this skill does and when to use it. Include trigger phrases. Max 1024 characters.
---
```

#### Frontmatter (optional fields)

```yaml
---
name: skill-name
description: A description of what this skill does and when to use it.
license: Apache-2.0
compatibility: Requires git, docker, and network access
metadata:
  author: example-org
  version: "1.0"
allowed-tools: Bash(git:*) Read
---
```

| Field           | Required | Description                                                                      |
| --------------- | -------- | -------------------------------------------------------------------------------- |
| `name`          | Yes      | Max 64 chars. Lowercase, numbers, hyphens. Must match directory name.            |
| `description`   | Yes      | Max 1024 chars. What the skill does and when to use it.                          |
| `license`       | No       | License name or reference to bundled license file.                               |
| `compatibility` | No       | Max 500 chars. Environment requirements (system packages, network access, etc.). |
| `metadata`      | No       | Arbitrary key-value mapping for additional metadata.                             |
| `allowed-tools` | No       | Space-delimited list of pre-approved tools. (Experimental)                       |

#### Body content

The Markdown body contains skill instructions. Recommended sections:

- Step-by-step instructions
- Examples of inputs and outputs
- Common edge cases

```markdown
# {Skill Title}

{Brief description of what the skill does.}

## How It Works

{Numbered list explaining the skill's workflow}

## Usage

{Instructions for using the skill, including any script invocations}

## References

See [the reference guide](references/REFERENCE.md) for detailed documentation.
```

### Best Practices for Context Efficiency

Skills are loaded on-demand — only the skill name and description are loaded at startup. The full `SKILL.md` loads into context only when the agent decides the skill is relevant. To minimize context usage:

- **Keep SKILL.md under 500 lines** — put detailed reference material in `references/`
- **Write specific descriptions** — helps the agent know exactly when to activate the skill
- **Use progressive disclosure** — reference supporting files that get read only when needed
- **Prefer scripts over inline code** — script execution doesn't consume context (only output does)
- **File references work one level deep** — link directly from SKILL.md to supporting files

### Optional Directories

#### references/

Contains additional documentation that agents can read when needed. Keep files focused — agents load these on demand, so smaller files mean less context usage.

See: https://agentskills.io/specification#references

#### scripts/

Contains executable code that agents can run. Scripts should:

- Use `#!/bin/bash` shebang
- Use `set -e` for fail-fast behavior
- Write status messages to stderr: `echo "Message" >&2`
- Write machine-readable output (JSON) to stdout
- Include a cleanup trap for temp files

#### assets/

Contains static resources like templates, images, and data files.

### End-User Installation

**Claude Code:**

```bash
cp -r skills/{skill-name} ~/.claude/skills/
```

**claude.ai:**
Add the skill to project knowledge or paste SKILL.md contents into the conversation.

If the skill requires network access, instruct users to add required domains at `claude.ai/settings/capabilities`.

### Validation

Use the skills-ref tool to validate your skills:

```bash
skills-ref validate ./my-skill
```

```

## File: claude.md
```
# AGENTS.md

This file provides guidance to AI coding agents (Claude Code, Cursor, Copilot, etc.) when working with code in this repository.

For the complete Agent Skills specification, see: https://agentskills.io/specification

## Repository Overview

A collection of skills for coding agents for working with Neon Serverless Postgres. Skills are packaged instructions and documentation that extend the agent's capabilities.

## Creating a New Skill

### Directory Structure

```
skills/
  {skill-name}/           # kebab-case directory name
    SKILL.md              # Required: skill definition
    references/           # Optional: additional documentation
      REFERENCE.md        # Detailed technical reference
      {topic}.md          # Domain-specific files
    scripts/              # Optional: executable scripts
      {script-name}.sh    # Bash scripts (preferred)
    assets/               # Optional: static resources
      templates/          # Document/config templates
      images/             # Diagrams, examples
```

### Naming Conventions

- **Skill directory**: kebab-case, must match `name` in frontmatter (e.g., `neon-postgres`)
- **Name field**: 1-64 chars, lowercase alphanumeric and hyphens only, no consecutive hyphens (`--`), must not start/end with `-`
- **SKILL.md**: Always uppercase, always this exact filename
- **Scripts**: `kebab-case.sh` (e.g., `deploy.sh`, `fetch-logs.sh`)

### SKILL.md Format

The `SKILL.md` file must contain YAML frontmatter followed by Markdown content.

#### Frontmatter (required fields)

```yaml
---
name: skill-name
description: A description of what this skill does and when to use it. Include trigger phrases. Max 1024 characters.
---
```

#### Frontmatter (optional fields)

```yaml
---
name: skill-name
description: A description of what this skill does and when to use it.
license: Apache-2.0
compatibility: Requires git, docker, and network access
metadata:
  author: example-org
  version: "1.0"
allowed-tools: Bash(git:*) Read
---
```

| Field           | Required | Description                                                                      |
| --------------- | -------- | -------------------------------------------------------------------------------- |
| `name`          | Yes      | Max 64 chars. Lowercase, numbers, hyphens. Must match directory name.            |
| `description`   | Yes      | Max 1024 chars. What the skill does and when to use it.                          |
| `license`       | No       | License name or reference to bundled license file.                               |
| `compatibility` | No       | Max 500 chars. Environment requirements (system packages, network access, etc.). |
| `metadata`      | No       | Arbitrary key-value mapping for additional metadata.                             |
| `allowed-tools` | No       | Space-delimited list of pre-approved tools. (Experimental)                       |

#### Body content

The Markdown body contains skill instructions. Recommended sections:

- Step-by-step instructions
- Examples of inputs and outputs
- Common edge cases

```markdown
# {Skill Title}

{Brief description of what the skill does.}

## How It Works

{Numbered list explaining the skill's workflow}

## Usage

{Instructions for using the skill, including any script invocations}

## References

See [the reference guide](references/REFERENCE.md) for detailed documentation.
```

### Best Practices for Context Efficiency

Skills are loaded on-demand — only the skill name and description are loaded at startup. The full `SKILL.md` loads into context only when the agent decides the skill is relevant. To minimize context usage:

- **Keep SKILL.md under 500 lines** — put detailed reference material in `references/`
- **Write specific descriptions** — helps the agent know exactly when to activate the skill
- **Use progressive disclosure** — reference supporting files that get read only when needed
- **Prefer scripts over inline code** — script execution doesn't consume context (only output does)
- **File references work one level deep** — link directly from SKILL.md to supporting files

### Optional Directories

#### references/

Contains additional documentation that agents can read when needed. Keep files focused — agents load these on demand, so smaller files mean less context usage.

See: https://agentskills.io/specification#references

#### scripts/

Contains executable code that agents can run. Scripts should:

- Use `#!/bin/bash` shebang
- Use `set -e` for fail-fast behavior
- Write status messages to stderr: `echo "Message" >&2`
- Write machine-readable output (JSON) to stdout
- Include a cleanup trap for temp files

#### assets/

Contains static resources like templates, images, and data files.

### End-User Installation

**Claude Code:**

```bash
cp -r skills/{skill-name} ~/.claude/skills/
```

**claude.ai:**
Add the skill to project knowledge or paste SKILL.md contents into the conversation.

If the skill requires network access, instruct users to add required domains at `claude.ai/settings/capabilities`.

### Validation

Use the skills-ref tool to validate your skills:

```bash
skills-ref validate ./my-skill
```

```

## File: package.json
```
{
  "name": "@neondatabase/agent-skills",
  "version": "1.0.0",
  "description": "A collection of Agent Skills for Neon Serverless Postgres",
  "license": "Apache-2.0",
  "repository": {
    "type": "git",
    "url": "https://github.com/neondatabase/agent-skills"
  },
  "author": {
    "name": "Neon",
    "url": "https://neon.tech"
  },
  "keywords": [
    "neon",
    "postgres",
    "serverless",
    "agent-skills",
    "claude-code",
    "mcp"
  ],
  "scripts": {
    "fmt": "npx prettier --write .",
    "validate:cursor-plugins": "node scripts/validate-cursor-plugins.mjs",
    "validate:claude-plugins": "node scripts/validate-claude-plugins.mjs",
    "validate:plugins": "npm run validate:cursor-plugins && npm run validate:claude-plugins",
    "validate:skills": "npx skills-ref validate ./skills/neon-postgres"
  }
}

```

## File: README.md
```
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://neon.com/brand/neon-logo-dark-color.svg?new">
  <source media="(prefers-color-scheme: light)" srcset="https://neon.com/brand/neon-logo-light-color.svg?new">
  <img width="250px" alt="Neon Logo fallback" src="https://neon.com/brand/neon-logo-dark-color.svg?new">
</picture>

# Agent Skills

A collection of [Agent Skills](https://agentskills.io/) and agent integrations for Neon Serverless Postgres.

## What are Agent Skills?

Skills are folders of instructions, scripts, and resources that agents can discover and use to do things more accurately and efficiently. Once installed, skills are automatically invoked by the agent upon detection of relevant tasks.

It all starts with the `SKILL.md` file in the skill's directory. It's the entry point and allows agents to progressively discover information as needed.

## Available Skills

### Neon Postgres

[skills/neon-postgres](skills/neon-postgres/SKILL.md)

A comprehensive index of Neon Serverless Postgres documentation and best practices to set your agents up for success.

### Claimable Postgres

[skills/claimable-postgres](skills/claimable-postgres/SKILL.md)

Provision instant temporary Postgres databases via Claimable Postgres by Neon ([neon.new](https://neon.new)) with no login, signup, or credit card. Supports REST API, CLI, and SDK.

### Neon Postgres Egress Optimizer

[skills/neon-postgres-egress-optimizer](skills/neon-postgres-egress-optimizer/SKILL.md)

Diagnose and fix excessive Postgres egress (network data transfer) in a codebase. Use when investigating high database bills, unexpected data transfer costs, or query overfetching.

## Installation

```bash
npx skills add neondatabase/agent-skills
```

### Claude Code Plugin

You can also install the skills as a Claude Code plugin, which bundles both the neon-postgres agent skill and the [Neon MCP Server](https://mcp.neon.tech) for natural language database management:

```
/plugin marketplace add neondatabase/agent-skills
/plugin install neon-postgres@neon
```

After installation, you'll be prompted to authenticate with Neon via OAuth when you first use MCP tools.

The top-level `skills/` directory remains the source of truth. Plugin folders symlink only the skill directories they expose.

### Cursor Plugin

This repository also includes Cursor plugin packaging with the same scope as the Claude plugin (neon-postgres agent skill and Neon MCP Server)

Run this command in chat:

```text
/add-plugin neon-postgres
```

## Usage

Example prompts:

```
Get started with Neon
```

```
Recommend a connection method for this project
```

```
Set up Drizzle ORM with Neon
```

```
Set up Neon Auth for my Next.js app
```

```
Query the database using neon-js
```

```
Create a new Neon branch using the API
```

```
Use the serverless driver for edge functions
```

```
Give me a quick temporary Postgres database
```

```
Why is my Neon bill so high?
```

```

## File: _GIT_INGEST.md
```
# OmniClaw Repo Plow: CIV_FETCHED_agent-skills_150352



================================================
FILE: AGENTS.md
================================================
# AGENTS.md

This file provides guidance to AI coding agents (Claude Code, Cursor, Copilot, etc.) when working with code in this repository.

For the complete Agent Skills specification, see: https://agentskills.io/specification

## Repository Overview

A collection of skills for coding agents for working with Neon Serverless Postgres. Skills are packaged instructions and documentation that extend the agent's capabilities.

## Creating a New Skill

### Directory Structure

```
skills/
  {skill-name}/           # kebab-case directory name
    SKILL.md              # Required: skill definition
    references/           # Optional: additional documentation
      REFERENCE.md        # Detailed technical reference
      {topic}.md          # Domain-specific files
    scripts/              # Optional: executable scripts
      {script-name}.sh    # Bash scripts (preferred)
    assets/               # Optional: static resources
      templates/          # Document/config templates
      images/             # Diagrams, examples
```

### Naming Conventions

- **Skill directory**: kebab-case, must match `name` in frontmatter (e.g., `neon-postgres`)
- **Name field**: 1-64 chars, lowercase alphanumeric and hyphens only, no consecutive hyphens (`--`), must not start/end with `-`
- **SKILL.md**: Always uppercase, always this exact filename
- **Scripts**: `kebab-case.sh` (e.g., `deploy.sh`, `fetch-logs.sh`)

### SKILL.md Format

The `SKILL.md` file must contain YAML frontmatter followed by Markdown content.

#### Frontmatter (required fields)

```yaml
---
name: skill-name
description: A description of what this skill does and when to use it. Include trigger phrases. Max 1024 characters.
---
```

#### Frontmatter (optional fields)

```yaml
---
name: skill-name
description: A description of what this skill does and when to use it.
license: Apache-2.0
compatibility: Requires git, docker, and network access
metadata:
  author: example-org
  version: "1.0"
allowed-tools: Bash(git:*) Read
---
```

| Field           | Required | Description                                                                      |
| --------------- | -------- | -------------------------------------------------------------------------------- |
| `name`          | Yes      | Max 64 chars. Lowercase, numbers, hyphens. Must match directory name.            |
| `description`   | Yes      | Max 1024 chars. What the skill does and when to use it.                          |
| `license`       | No       | License name or reference to bundled license file.                               |
| `compatibility` | No       | Max 500 chars. Environment requirements (system packages, network access, etc.). |
| `metadata`      | No       | Arbitrary key-value mapping for additional metadata.                             |
| `allowed-tools` | No       | Space-delimited list of pre-approved tools. (Experimental)                       |

#### Body content

The Markdown body contains skill instructions. Recommended sections:

- Step-by-step instructions
- Examples of inputs and outputs
- Common edge cases

```markdown
# {Skill Title}

{Brief description of what the skill does.}

## How It Works

{Numbered list explaining the skill's workflow}

## Usage

{Instructions for using the skill, including any script invocations}

## References

See [the reference guide](references/REFERENCE.md) for detailed documentation.
```

### Best Practices for Context Efficiency

Skills are loaded on-demand — only the skill name and description are loaded at startup. The full `SKILL.md` loads into context only when the agent decides the skill is relevant. To minimize context usage:

- **Keep SKILL.md under 500 lines** — put detailed reference material in `references/`
- **Write specific descriptions** — helps the agent know exactly when to activate the skill
- **Use progressive disclosure** — reference supporting files that get read only when needed
- **Prefer scripts over inline code** — script execution doesn't consume context (only output does)
- **File references work one level deep** — link directly from SKILL.md to supporting files

### Optional Directories

#### references/

Contains additional documentation that agents can read when needed. Keep files focused — agents load these on demand, so smaller files mean less context usage.

See: https://agentskills.io/specification#references

#### scripts/

Contains executable code that agents can run. Scripts should:

- Use `#!/bin/bash` shebang
- Use `set -e` for fail-fast behavior
- Write status messages to stderr: `echo "Message" >&2`
- Write machine-readable output (JSON) to stdout
- Include a cleanup trap for temp files

#### assets/

Contains static resources like templates, images, and data files.

### End-User Installation

**Claude Code:**

```bash
cp -r skills/{skill-name} ~/.claude/skills/
```

**claude.ai:**
Add the skill to project knowledge or paste SKILL.md contents into the conversation.

If the skill requires network access, 

================================================
FILE: CLAUDE.md
================================================
# AGENTS.md

This file provides guidance to AI coding agents (Claude Code, Cursor, Copilot, etc.) when working with code in this repository.

For the complete Agent Skills specification, see: https://agentskills.io/specification

## Repository Overview

A collection of skills for coding agents for working with Neon Serverless Postgres. Skills are packaged instructions and documentation that extend the agent's capabilities.

## Creating a New Skill

### Directory Structure

```
skills/
  {skill-name}/           # kebab-case directory name
    SKILL.md              # Required: skill definition
    references/           # Optional: additional documentation
      REFERENCE.md        # Detailed technical reference
      {topic}.md          # Domain-specific files
    scripts/              # Optional: executable scripts
      {script-name}.sh    # Bash scripts (preferred)
    assets/               # Optional: static resources
      templates/          # Document/config templates
      images/             # Diagrams, examples
```

### Naming Conventions

- **Skill directory**: kebab-case, must match `name` in frontmatter (e.g., `neon-postgres`)
- **Name field**: 1-64 chars, lowercase alphanumeric and hyphens only, no consecutive hyphens (`--`), must not start/end with `-`
- **SKILL.md**: Always uppercase, always this exact filename
- **Scripts**: `kebab-case.sh` (e.g., `deploy.sh`, `fetch-logs.sh`)

### SKILL.md Format

The `SKILL.md` file must contain YAML frontmatter followed by Markdown content.

#### Frontmatter (required fields)

```yaml
---
name: skill-name
description: A description of what this skill does and when to use it. Include trigger phrases. Max 1024 characters.
---
```

#### Frontmatter (optional fields)

```yaml
---
name: skill-name
description: A description of what this skill does and when to use it.
license: Apache-2.0
compatibility: Requires git, docker, and network access
metadata:
  author: example-org
  version: "1.0"
allowed-tools: Bash(git:*) Read
---
```

| Field           | Required | Description                                                                      |
| --------------- | -------- | -------------------------------------------------------------------------------- |
| `name`          | Yes      | Max 64 chars. Lowercase, numbers, hyphens. Must match directory name.            |
| `description`   | Yes      | Max 1024 chars. What the skill does and when to use it.                          |
| `license`       | No       | License name or reference to bundled license file.                               |
| `compatibility` | No       | Max 500 chars. Environment requirements (system packages, network access, etc.). |
| `metadata`      | No       | Arbitrary key-value mapping for additional metadata.                             |
| `allowed-tools` | No       | Space-delimited list of pre-approved tools. (Experimental)                       |

#### Body content

The Markdown body contains skill instructions. Recommended sections:

- Step-by-step instructions
- Examples of inputs and outputs
- Common edge cases

```markdown
# {Skill Title}

{Brief description of what the skill does.}

## How It Works

{Numbered list explaining the skill's workflow}

## Usage

{Instructions for using the skill, including any script invocations}

## References

See [the reference guide](references/REFERENCE.md) for detailed documentation.
```

### Best Practices for Context Efficiency

Skills are loaded on-demand — only the skill name and description are loaded at startup. The full `SKILL.md` loads into context only when the agent decides the skill is relevant. To minimize context usage:

- **Keep SKILL.md under 500 lines** — put detailed reference material in `references/`
- **Write specific descriptions** — helps the agent know exactly when to activate the skill
- **Use progressive disclosure** — reference supporting files that get read only when needed
- **Prefer scripts over inline code** — script execution doesn't consume context (only output does)
- **File references work one level deep** — link directly from SKILL.md to supporting files

### Optional Directories

#### references/

Contains additional documentation that agents can read when needed. Keep files focused — agents load these on demand, so smaller files mean less context usage.

See: https://agentskills.io/specification#references

#### scripts/

Contains executable code that agents can run. Scripts should:

- Use `#!/bin/bash` shebang
- Use `set -e` for fail-fast behavior
- Write status messages to stderr: `echo "Message" >&2`
- Write machine-readable output (JSON) to stdout
- Include a cleanup trap for temp files

#### assets/

Contains static resources like templates, images, and data files.

### End-User Installation

**Claude Code:**

```bash
cp -r skills/{skill-name} ~/.claude/skills/
```

**claude.ai:**
Add the skill to project knowledge or paste SKILL.md contents into the conversation.

If the skill requires network access, 

================================================
FILE: package.json
================================================
{
  "name": "@neondatabase/agent-skills",
  "version": "1.0.0",
  "description": "A collection of Agent Skills for Neon Serverless Postgres",
  "license": "Apache-2.0",
  "repository": {
    "type": "git",
    "url": "https://github.com/neondatabase/agent-skills"
  },
  "author": {
    "name": "Neon",
    "url": "https://neon.tech"
  },
  "keywords": [
    "neon",
    "postgres",
    "serverless",
    "agent-skills",
    "claude-code",
    "mcp"
  ],
  "scripts": {
    "fmt": "npx prettier --write .",
    "validate:cursor-plugins": "node scripts/validate-cursor-plugins.mjs",
    "validate:claude-plugins": "node scripts/validate-claude-plugins.mjs",
    "validate:plugins": "npm run validate:cursor-plugins && npm run validate:claude-plugins",
    "validate:skills": "npx skills-ref validate ./skills/neon-postgres"
  }
}


================================================
FILE: README.md
================================================
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://neon.com/brand/neon-logo-dark-color.svg?new">
  <source media="(prefers-color-scheme: light)" srcset="https://neon.com/brand/neon-logo-light-color.svg?new">
  <img width="250px" alt="Neon Logo fallback" src="https://neon.com/brand/neon-logo-dark-color.svg?new">
</picture>

# Agent Skills

A collection of [Agent Skills](https://agentskills.io/) and agent integrations for Neon Serverless Postgres.

## What are Agent Skills?

Skills are folders of instructions, scripts, and resources that agents can discover and use to do things more accurately and efficiently. Once installed, skills are automatically invoked by the agent upon detection of relevant tasks.

It all starts with the `SKILL.md` file in the skill's directory. It's the entry point and allows agents to progressively discover information as needed.

## Available Skills

### Neon Postgres

[skills/neon-postgres](skills/neon-postgres/SKILL.md)

A comprehensive index of Neon Serverless Postgres documentation and best practices to set your agents up for success.

### Claimable Postgres

[skills/claimable-postgres](skills/claimable-postgres/SKILL.md)

Provision instant temporary Postgres databases via Claimable Postgres by Neon ([neon.new](https://neon.new)) with no login, signup, or credit card. Supports REST API, CLI, and SDK.

### Neon Postgres Egress Optimizer

[skills/neon-postgres-egress-optimizer](skills/neon-postgres-egress-optimizer/SKILL.md)

Diagnose and fix excessive Postgres egress (network data transfer) in a codebase. Use when investigating high database bills, unexpected data transfer costs, or query overfetching.

## Installation

```bash
npx skills add neondatabase/agent-skills
```

### Claude Code Plugin

You can also install the skills as a Claude Code plugin, which bundles both the neon-postgres agent skill and the [Neon MCP Server](https://mcp.neon.tech) for natural language database management:

```
/plugin marketplace add neondatabase/agent-skills
/plugin install neon-postgres@neon
```

After installation, you'll be prompted to authenticate with Neon via OAuth when you first use MCP tools.

The top-level `skills/` directory remains the source of truth. Plugin folders symlink only the skill directories they expose.

### Cursor Plugin

This repository also includes Cursor plugin packaging with the same scope as the Claude plugin (neon-postgres agent skill and Neon MCP Server)

Run this command in chat:

```text
/add-plugin neon-postgres
```

## Usage

Example prompts:

```
Get started with Neon
```

```
Recommend a connection method for this project
```

```
Set up Drizzle ORM with Neon
```

```
Set up Neon Auth for my Next.js app
```

```
Query the database using neon-js
```

```
Create a new Neon branch using the API
```

```
Use the serverless driver for edge functions
```

```
Give me a quick temporary Postgres database
```

```
Why is my Neon bill so high?
```


================================================
FILE: .claude-plugin\marketplace.json
================================================
{
  "name": "neon",
  "owner": {
    "name": "Andre Landgraf",
    "email": "andre@neon.tech"
  },
  "metadata": {
    "description": "Official Neon Serverless Postgres plugins for Claude Code",
    "version": "1.0.0"
  },
  "plugins": [
    {
      "name": "neon-postgres",
      "source": "./plugins/neon-postgres",
      "description": "Manage your Neon projects and databases with the neon-postgres agent skill and the Neon MCP Server",
      "version": "1.0.0",
      "category": "database",
      "tags": ["postgres", "serverless", "database", "mcp", "neon"]
    }
  ]
}


================================================
FILE: .cursor-plugin\marketplace.json
================================================
{
  "name": "neon",
  "owner": {
    "name": "Andre Landgraf",
    "email": "andre@neon.tech"
  },
  "metadata": {
    "description": "Official Neon Serverless Postgres plugins for Cursor",
    "version": "1.0.0",
    "pluginRoot": "plugins"
  },
  "plugins": [
    {
      "name": "neon-postgres",
      "source": "neon-postgres",
      "description": "Manage your Neon projects and databases with the neon-postgres agent skill and the Neon MCP Server"
    }
  ]
}


================================================
FILE: evals\neon-postgres-egress-optimizer\AGENTS.md
================================================
- Never use title case
- Never modify versioned eval files, make a new version instead


================================================
FILE: evals\neon-postgres-egress-optimizer\eval-batch.ts
================================================
#!/usr/bin/env bun

const EVALS_DIR = import.meta.dir;
const EVAL_RUN = `${EVALS_DIR}/eval-run.ts`;

/**
 * Arg parsing
 */
function parseArgs(): { prompt: string; skill?: string; count: number } {
  const args = process.argv.slice(2);
  let prompt: string | undefined;
  let skill: string | undefined;
  let count: string | undefined;

  for (let i = 0; i < args.length; i++) {
    if (args[i] === "--prompt" && args[i + 1]) {
      prompt = args[++i];
    } else if (args[i] === "--skill" && args[i + 1]) {
      skill = args[++i];
    } else if (args[i] === "--count" && args[i + 1]) {
      count = args[++i];
    }
  }

  const n = parseInt(count ?? "", 10);
  if (!prompt || !["A", "B"].includes(prompt) || !count || isNaN(n) || n < 1) {
    console.error(
      "Usage: ./eval-batch.ts --prompt <A|B> --count <N> [--skill <version>]",
    );
    console.error("  --prompt  Required. A or B");
    console.error("  --count   Required. Number of parallel runs");
    console.error(
      "  --skill   Optional. Skill version (e.g., 003). Omit for baseline.",
    );
    process.exit(1);
  }

  return { prompt, skill, count: n };
}

/**
 * Main
 */

const { prompt, skill, count } = parseArgs();
const logDir = `/tmp/eval-batch-${process.pid}`;
await Bun.$`mkdir -p ${logDir}`.quiet();

const childArgs = ["--prompt", prompt];
if (skill) childArgs.push("--skill", skill);

console.log(`Launching ${count} parallel eval runs...`);
console.log(`Logs: ${logDir}/\n`);

const children = Array.from({ length: count }, (_, i) => {
  const runId = `${i + 1}`;
  const mainLogPath = `${logDir}/run-${runId}.main.log`;
  const summaryPath = `${logDir}/run-${runId}.summary.json`;
  const logFile = Bun.file(mainLogPath);
  const proc = Bun.spawn(
    ["bun", EVAL_RUN, ...childArgs, "--log-dir", logDir, "--run-id", runId],
    {
      stdout: logFile,
      stderr: logFile,
      stdin: "ignore",
    },
  );
  return proc.exited.then((code) => ({
    index: i + 1,
    code,
    summaryPath,
    mainLogPath,
  }));
});

type RunSummary = {
  phases?: {
    claude?: { exitCode?: number | null };
    tests?: {
      attempts?: number;
      passed?: boolean;
      passedAttempt?: number | null;
    };
    score?: { exitCode?: number | null };
  };
  artifacts?: {
    runDiff?: string;
  };
};

async function readSummary(path: string): Promise<RunSummary | null> {
  try {
    const text = await Bun.file(path).text();
    return JSON.parse(text) as RunSummary;
  } catch {
    return null;
  }
}

const results = await Promise.all(children);
const summaries = await Promise.all(
  results.map((r) => readSummary(r.summaryPath)),
);

const passed = results.filter((r) => r.code === 0);
const failed = results.filter((r) => r.code !== 0);

console.log(`\n--- summary ---`);
console.log(`Passed: ${passed.length}/${count}`);
console.log(`Failed: ${failed.length}/${count}`);
console.log("\nRun details:");

for (const result of results) {
  const summary = summaries[result.index - 1];
  if (!summary?.phases) {
    console.log(
      `  run ${result.index}: exit ${result.code} | summary missing (${result.summaryPath})`,
    );
    console.log(`    main log: ${result.mainLogPath}`);
    continue;
  }

  const claudeExit = summary.phases.claude?.exitCode;
  const tests = summary.phases.tests;
  const scoreExit = summary.phases.score?.exitCode;
  const testsStatus = tests?.passed
    ? `pass (attempt ${tests.passedAttempt ?? tests.attempts ?? "?"})`
    : `fail (${tests?.attempts ?? "?"} attempts)`;
  const scoreStatus =
    scoreExit === null || scoreExit === undefined
      ? "skipped"
      : scoreExit === 0
        ? "ok"
        : `fail (${scoreExit})`;

  console.log(
    `  run ${result.index}: exit ${result.code} | claude ${claudeExit === 0 ? "ok" : `fail (${claudeExit ?? "?"})`} | tests ${testsStatus} | score ${scoreStatus}`,
  );

  if (result.code !== 0) {
    const runDiff = summary.artifacts?.runDiff;
    if (runDiff) console.log(`    run diff: ${runDiff}`);
    console.log(`    summary:  ${result.summaryPath}`);
    console.log(`    main log: ${result.mainLogPath}`);
  }
}

process.exit(failed.length > 0 ? 1 : 0);


================================================
FILE: evals\neon-postgres-egress-optimizer\eval-rubric.md
================================================
# Eval rubric: Hono + Drizzle fixture

This file defines the scoring criteria for evaluating the neon-postgres-egress-optimizer skill. Used by both human judges and LLM judges.

## Schema

- `products` — id, name, price, category_id, description (TEXT ~5KB), raw_payload (JSONB ~50KB), image_urls (JSONB array), created_at
- `categories` — id, name, slug
- `reviews` — id, product_id, user_name, rating, body (TEXT), created_at

---

## Problems & scoring

### P1: SELECT \* with unused large columns

- **Route:** `GET /products`
- **Bad pattern:** Drizzle query uses `select()` with no column specification (equivalent to SELECT \*). The response only returns `{ id, name, price, imageUrls }`. The `raw_payload` (~50KB) and `description` (~5KB) columns are fetched from the database but never used.
- **Detected?** Does the agent identify that this route fetches columns (specifically `raw_payload` and/or `description`) that the response doesn't use?
- **Fixed?** Does the diff change the Drizzle query to select only the columns needed by the response (id, name, price, image_urls)?

### P2: Missing pagination

- **Route:** `GET /products`
- **Bad pattern:** Returns every product in the table. No limit, no offset, no cursor.
- **Detected?** Does the agent flag that this route returns an unbounded result set?
- **Fixed?** Does the diff add limit/offset or cursor-based pagination with a sensible default?

### P3: High-frequency repeated query

- **Route:** `GET /categories`
- **Bad pattern:** Nothing in the code itself suggests a problem. Mock `pg_stat_statements` shows this query with ~50,000 calls versus a few hundred for other routes, indicating some client is hammering it on every interaction. Categories rarely change.
- **Detected?** Does the agent correlate the high call count in pg_stat_statements to this route and flag it as a caching candidate?
- **Fixed?** Does the diff avoid hitting the database on every request? Client-side changes are outside the scope of what the agent can fix.

### P4: Application-side aggregation

- **Route:** `GET /stats`
- **Bad pattern:** Fetches ALL reviews from the database into the route handler, then computes average rating and review count per category using JavaScript `.reduce()`. Returns a small summary JSON. The egress cost is the full reviews table transfer, even though the response is tiny.
- **Detected?** Does the agent identify that the handler fetches all review rows to perform aggregation that should happen in SQL?
- **Fixed?** Does the diff replace the fetch-all-then-reduce pattern with a SQL query using `GROUP BY`, `AVG(rating)`, and `COUNT(*)`? The full reviews table should no longer be fetched.

### P5: Redundant join duplication

- **Route:** `GET /products/:id`
- **Bad pattern:** Fetches a product with all its reviews via a JOIN. Each review row duplicates every product column. A product with 200 reviews sends `raw_payload` (50KB) 200 times — ~10MB for a single request.
- **Detected?** Does the agent identify that the join duplicates wide product data across every review row? Note: narrowing column selection on the join (excluding rawPayload) is a P1-style fix, not P5 detection. P5 requires recognizing the structural duplication caused by the join itself.
- **Fixed?** Does the diff eliminate the duplication of product data across review rows?

### Overall

**Tests pass?** Do the integration tests still pass after the agent's changes?

---

## Mock pg_stat_statements

The mock stats file (`mock-stats/pg_stat_statements.md`) should show:

| Query pattern                     | calls  | total_rows | avg_rows_per_call | Notes                                 |
| --------------------------------- | ------ | ---------- | ----------------- | ------------------------------------- |
| SELECT \* FROM products (P1/P2)   | 500    | 500,000    | 1,000             | High rows, wide rows                  |
| SELECT \* FROM categories (P3)    | 50,000 | 500,000    | 10                | Extreme call frequency                |
| SELECT \* FROM reviews (P4)       | 200    | 1,000,000  | 5,000             | Massive row transfer for small output |
| SELECT products JOIN reviews (P5) | 300    | 60,000     | 200               | Row duplication from join             |


================================================
FILE: evals\neon-postgres-egress-optimizer\eval-run.ts
================================================
#!/usr/bin/env bun

import {
  appendFile,
  mkdir,
  readFile,
  unlink,
  writeFile,
} from "node:fs/promises";

const EVALS_DIR = import.meta.dir;
const TEST_RETRY_LIMIT = 5;
const TEST_RETRY_DELAY_MS = 1500;

const PROMPTS = {
  A: "My Neon bill spiked to $400 this month, most of it is data transfer. Help me figure out why.",
  B: "Optimize the database egress in this project.",
};

/**
 * Arg parsing
 */
function parseArgs(): {
  prompt: "A" | "B";
  skill?: string;
  logDir?: string;
  runId?: string;
} {
  const args = process.argv.slice(2);
  let prompt: string | undefined;
  let skill: string | undefined;
  let logDir: string | undefined;
  let runId: string | undefined;

  for (let i = 0; i < args.length; i++) {
    if (args[i] === "--prompt" && args[i + 1]) {
      prompt = args[++i];
    } else if (args[i] === "--skill" && args[i + 1]) {
      skill = args[++i];
    } else if (args[i] === "--log-dir" && args[i + 1]) {
      logDir = args[++i];
    } else if (args[i] === "--run-id" && args[i + 1]) {
      runId = args[++i];
    }
  }

  if (!prompt || !["A", "B"].includes(prompt)) {
    console.error(
      "Usage: ./eval-run.ts --prompt <A|B> [--skill <version>] [--log-dir <path>] [--run-id <id>]",
    );
    console.error("  --prompt  Required. A or B");
    console.error(
      "  --skill   Optional. Skill version (e.g., 003). Omit for baseline.",
    );
    console.error("  --log-dir Optional. Directory for per-phase run logs.");
    console.error("  --run-id  Optional. Run id used in log filenames.");
    process.exit(1);
  }

  return { prompt: prompt as "A" | "B", skill, logDir, runId };
}

/**
 * Helpers
 */

async function claimDiffFile(
  diffsDir: string,
  suffix: string,
  content: string,
): Promise<string> {
  const glob = new Bun.Glob("*.diff");
  let maxCounter = 0;
  for await (const file of glob.scan(diffsDir)) {
    const match = file.match(/^(\d+)_/);
    if (match) maxCounter = Math.max(maxCounter, parseInt(match[1] ?? "0", 10));
  }

  for (let i = maxCounter + 1; i < maxCounter + 100; i++) {
    const name = `${String(i).padStart(2, "0")}_${suffix}.diff`;
    const fullPath = `${diffsDir}/${name}`;
    if (await Bun.file(fullPath).exists()) continue;
    await Bun.write(fullPath, content);
    return name;
  }
  throw new Error("Could not claim a diff filename after 99 attempts");
}

async function spawnToFile(
  cmd: string[],
  cwd: string,
  logPath: string,
): Promise<number> {
  const proc = Bun.spawn(cmd, {
    cwd,
    stdin: "ignore",
    stdout: Bun.file(logPath),
    stderr: Bun.file(logPath),
  });
  return proc.exited;
}

async function appendLog(logPath: string, content: string): Promise<void> {
  await appendFile(logPath, content);
}

function stripDrizzleSpinnerNoise(output: string): string {
  return output
    .replace(/\r/g, "\n")
    .split("\n")
    .filter((line) => {
      const trimmed = line.trim();
      if (!trimmed) return true;
      if (/^\[[⠁-⣿]+\]\s+Pulling schema\.\.\./u.test(trimmed)) return false;
      return true;
    })
    .join("\n");
}

async function runCommandToPhaseLog(opts: {
  phaseName: string;
  cmd: string[];
  cwd: string;
  logPath: string;
  stripSpinner?: boolean;
}): Promise<number> {
  const tmpLogPath = `${opts.logPath}.${Date.now()}-${Math.random()
    .toString(36)
    .slice(2)}.tmp`;
  const exitCode = await spawnToFile(opts.cmd, opts.cwd, tmpLogPath);
  const raw = await readFile(tmpLogPath, "utf8").catch(() => "");
  await unlink(tmpLogPath).catch(() => {});
  const output = opts.stripSpinner ? stripDrizzleSpinnerNoise(raw) : raw;

  await appendLog(opts.logPath, `\n=== phase: ${opts.phaseName} ===\n\n`);
  if (output.trim()) {
    await appendLog(
      opts.logPath,
      output.endsWith("\n") ? output : `${output}\n`,
    );
  }
  await appendLog(opts.logPath, `\n[exit_code] ${exitCode}\n`);
  return exitCode;
}

type EvalSummary = {
  runId: string;
  prompt: "A" | "B";
  skillVersion: string | null;
  type: string;
  evalDir: string;
  logDir: string;
  logs: {
    claude: string;
    tests: string;
    score: string;
  };
  artifacts: {
    runDiff: string;
    canonicalDiff: string | null;
  };
  phases: {
    claude: {
      exitCode: number | null;
    };
    tests: {
      attempts: number;
      passed: boolean;
      passedAttempt: number | null;
      exitCodes: number[];
    };
    score: {
      exitCode: number | null;
    };
  };
  exitCode: number | null;
};

/**
 * Main
 */

const { prompt, skill, logDir: logDirArg, runId: runIdArg } = parseArgs();
const type = skill ? `v${skill}` : "baseline";
const dateSuffix = new Date().toISOString().slice(0, 10).replace(/-/g, "");
const evalDir = `/tmp/eval-${dateSuffix}_${prompt}_${type}_${process.pid}`;
const logDir = logDirArg ?? `/tmp/eval-run-logs-${process.pid}`;
const runId = runIdArg ?? `${process.pid}`;
const runPrefix = `run-${runId}`;
const claudeLogPath = `${logDir}/${runPrefix}.claude.log`;
const testsLogPath = `${logDir}/${runPrefix}.tests.lo

================================================
FILE: evals\neon-postgres-egress-optimizer\eval-stats.ts
================================================
#!/usr/bin/env bun

const RESULTS_CSV = `${import.meta.dir}/results.csv`;

const PROBLEMS = ["p1", "p2", "p3", "p4", "p5"] as const;
const LABELS: Record<string, string> = {
  p1: "P1: SELECT * unused columns",
  p2: "P2: Missing pagination",
  p3: "P3: High-frequency query",
  p4: "P4: Application-side aggregation",
  p5: "P5: Join duplication",
};

type Row = Record<string, string>;

function parseCsv(text: string): Row[] {
  const [headerLine, ...dataLines] = text.trimEnd().split("\n");
  if (!headerLine) return [];
  const headers = headerLine.split(",");
  return dataLines.map((line) => {
    const values = line.split(",");
    return Object.fromEntries(headers.map((h, i) => [h, values[i] ?? ""]));
  });
}

function pct(n: number, total: number): string {
  return total === 0 ? "0%" : `${Math.round((n / total) * 100)}%`;
}

const rows = parseCsv(await Bun.file(RESULTS_CSV).text());

const groups = new Map<string, Row[]>();
for (const row of rows) {
  const key = row["skill_version"]?.trim() || "baseline";
  groups.set(key, [...(groups.get(key) ?? []), row]);
}

const ordered = [
  "baseline",
  ...[...groups.keys()].filter((k) => k !== "baseline").sort(),
];

// Baseline table
const bl = groups.get("baseline") ?? [];
console.log("baseline table");
console.log(
  "| Problem                          | Without skill                        |",
);
console.log(
  "| -------------------------------- | ------------------------------------ |",
);
for (const p of PROBLEMS) {
  const det = bl.filter((r) => r[`${p}_detected`] === "yes").length;
  const fix = bl.filter((r) => r[`${p}_fixed`] === "yes").length;
  console.log(
    `| ${LABELS[p]!.padEnd(32)} | ${`${det}/${bl.length} detected, ${fix}/${bl.length} fixed`.padEnd(36)} |`,
  );
}

// Summary table
console.log("\nresults summary table");
const header = [
  "Problem",
  ...ordered.map((k) => `${k} (${groups.get(k)?.length ?? 0} runs)`),
];
console.log(`| ${header.join(" | ")} |`);
console.log(`| ${header.map(() => "---").join(" | ")} |`);
for (const p of PROBLEMS) {
  const cells = [
    LABELS[p]!,
    ...ordered.map((k) => {
      const g = groups.get(k) ?? [];
      return pct(
        g.filter((r) => r[`${p}_detected`] === "yes").length,
        g.length,
      );
    }),
  ];
  console.log(`| ${cells.join(" | ")} |`);
}

const totalRuns = rows.length;
const totalPass = rows.filter((r) => r["tests_pass"] === "yes").length;
console.log(`\ntests passed on ${totalPass}/${totalRuns} total runs`);


================================================
FILE: evals\neon-postgres-egress-optimizer\package.json
================================================
{
  "name": "neon-postgres-egress-optimizer",
  "private": true,
  "devDependencies": {
    "@types/bun": "latest"
  },
  "peerDependencies": {
    "typescript": "^5"
  }
}


================================================
FILE: evals\neon-postgres-egress-optimizer\PLAN.md
================================================
# neon-postgres-egress-optimizer — project plan

## Problem

Database providers charge for egress (network transfer). Customers get surprised by high bills, often caused by unoptimized queries — `SELECT *`, missing pagination, unused large columns, high-frequency repeated queries. The connection between application query patterns and egress costs isn't obvious, so users blame the provider.

## Solution

An agent skill that guides Claude Code (or any SKILL.md-compatible agent) through diagnosing and fixing excessive Postgres egress in a user's codebase.

---

## Skill design

### Architecture: self-contained

The SKILL.md bakes in all diagnostic queries, fix patterns, and workflow steps. Fully self-contained — no external doc fetches required at runtime.

**Why not hub-and-spoke like `neon-postgres`?** That skill covers a broad surface (auth, CLI, branching, etc.) and dispatches to many reference files. This skill has a single focused workflow. Self-contained is simpler, works offline, and has no breakage risk from doc URL changes.

### Structure

The skill and its evals live in separate top-level directories so that installing the skill (which copies the skill directory) doesn't pull in eval fixtures, diffs, and results.

```
skills/neon-postgres-egress-optimizer/
└── SKILL.md                          # Placeholder until a version is promoted

evals/neon-postgres-egress-optimizer/
├── PLAN.md                           # This file
├── README.md                         # Runbook: how to run evals, prompts, process
├── results.csv                       # Append-only eval results
├── eval-rubric.md                    # Problem definitions + scoring criteria
├── skill-versions/                   # Numbered skill iterations for eval
│   ├── SKILL-v001.md
│   ├── SKILL-v002.md
│   └── ...
├── diffs/
│   └── 01_20260312_A_baseline.diff
├── mock-stats/
│   └── pg_stat_statements.md         # Used by Prompt C only, never copied to fixture
└── fixtures/
    └── hono-drizzle-app/
        ├── src/
        ├── drizzle/
        └── tests/
```

### SKILL.md content outline

**Frontmatter:** Name, description (optimized for triggering — covers "high bill", "egress", "network transfer", "data transfer costs", "SELECT \*", "query optimization for cost", etc.)

**Workflow:**

1. **Diagnose** — Check if `pg_stat_statements` is available (it's enabled by default on Neon but may need `CREATE EXTENSION`). If stats are empty (common after scale-to-zero wakes the compute), instruct the user to run `SELECT pg_stat_statements_reset();`, wait for a representative traffic window, then return. When stats are available, run four diagnostic queries (total rows returned, rows per execution, most frequent queries, longest running). Interpret results: rank by egress impact, flag queries with high row counts or wide rows (JSONB, TEXT, BYTEA).

2. **Analyze codebase** — Cross-reference top offending queries with application code. Identify which columns are actually used downstream. Flag gaps between what's fetched and what's consumed.

3. **Fix** — Apply specific patterns per problem found:
   - `SELECT *` → explicit column lists (exclude unused columns, especially large ones)
   - Missing pagination → add LIMIT/OFFSET or cursor-based pagination
   - Repeated identical queries → caching layer or query deduplication
   - Application-side aggregation → server-side SQL aggregations (SUM, COUNT, GROUP BY)
   - ORM overfetching → Drizzle column selection / `.select()` with explicit fields
   - Join duplication → separate queries or subqueries that don't repeat wide columns
   - Each pattern includes before/after examples in Drizzle

4. **Verify** — Run existing tests (if any) to confirm nothing broke. Reset `pg_stat_statements`, wait for measurement window, re-run diagnostics, compare.

### Description / triggering

The description needs to be broad enough to catch indirect phrasings. Users won't say "optimize my egress" — they'll say "why is my Neon bill so high" or "my database costs jumped" or "I'm transferring too much data." The description should explicitly list these trigger phrases.

---

## Eval system

### Design principles

- **Binary scoring.** Per problem: detected (yes/no), fixed (yes/no). Scored against a rubric with yes/no questions.
- **Execution mode, not plan mode.** The agent applies actual code changes. We evaluate the diff.
- **Rubric written before first run.** Problem definitions and scoring criteria documented upfront so scoring is objective.
- **No contamination.** Fixture is copied to a temp directory for each run. The agent never sees the rubric or results.
- **Versioned skills.** Each skill iteration is saved as a numbered file in `skill-versions/` (SKILL-v001.md, SKILL-v002.md, ...). Eval runs record the version used. The main `SKILL.md` stays as a placeholder until a version is promoted by copying it to `skills/neon-postgres-egress-optimizer/SKILL.md`.

### Eval rubric

`eval-rubric.md` defines 5 problems and provides 

================================================
FILE: evals\neon-postgres-egress-optimizer\README.md
================================================
# Evals runbook

How to run and score evaluations for the neon-postgres-egress-optimizer skill.

## Skill versions

Skill versions live in `skill-versions/` as numbered files: `SKILL-v001.md`, `SKILL-v002.md`, etc. Each eval run uses a specific version and records it in `results.csv`.

Workflow:

1. Copy the current version or create a new one in `skill-versions/`
2. Run evals against it
3. Record results with the version number
4. Iterate — create a new version for each change
5. When a version consistently beats baseline, promote it:

```bash
# From the repo root:
cp evals/neon-postgres-egress-optimizer/skill-versions/SKILL-vXXX.md skills/neon-postgres-egress-optimizer/SKILL.md
```

## Prompts

| ID  | Type     | Prompt                                                                                       |
| --- | -------- | -------------------------------------------------------------------------------------------- |
| A   | Vague    | My Neon bill spiked to $400 this month, most of it is data transfer. Help me figure out why. |
| B   | Moderate | Optimize the database egress in this project.                                                |

Prompt C (specific, with pg_stat_statements data) is planned but deferred until the mock stats workflow is finalized. See `eval-rubric.md` for problem P3 details — it is only detectable via stats, so prompts A and B are expected to score 0 on P3 detection.

## Baseline

Baseline established from 89 runs without the skill on Opus 4.6 high effort.

| Problem                          | Without skill               | Notes                                                                                                            |
| -------------------------------- | --------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| P1: SELECT \* unused columns     | 89/89 detected, 89/89 fixed | Always caught. The skill won't improve this.                                                                     |
| P2: Missing pagination           | 0/89 detected, 0/89 fixed   | Never caught. This is the primary target for the skill.                                                          |
| P3: High-frequency query         | 0/89 detected, 0/89 fixed   | Never caught. Expected — only detectable via pg_stat_statements data.                                            |
| P4: Application-side aggregation | 87/89 detected, 87/89 fixed | Almost always caught. Rare misses come from omitting the aggregation issue entirely.                             |
| P5: Join duplication             | 25/89 detected, 25/89 fixed | ~28% catch rate. When missed, the agent applies P1-style column narrowing instead of fixing the structural join. |

Tests passed on 89/89 baseline runs. Full results in `results.csv`.

## Results summary

| Problem                          | baseline (89 runs) | v003 (42 runs) |
| -------------------------------- | ------------------ | -------------- |
| P1: SELECT \* unused columns     | 100%               | 100%           |
| P2: Missing pagination           | 0%                 | 57%            |
| P3: High-frequency query         | 0%                 | 12%            |
| P4: Application-side aggregation | 98%                | 100%           |
| P5: Join duplication             | 28%                | 100%           |

P3 is expected to miss on prompts A/B — it requires pg_stat_statements data. Tests passed on all 139 runs. v001/v002 data (4 runs each) omitted due to small sample size; full history in `results.csv`.

## Running an eval

```bash
./eval-run.ts --prompt A --skill 003    # skill run with v003
./eval-run.ts --prompt B                # baseline run (no --skill)
```

The script handles the full lifecycle:

1. Copies the fixture to a temp workspace (`/tmp/eval-...`)
2. Installs the skill version (if `--skill` provided)
3. Initializes git and launches Claude Code
4. Captures a run-local diff artifact in the run log directory
5. Runs `bun test` (with retry + short delay on failure)
6. Captures a canonical diff to `diffs/` (race-safe for parallel runs)
7. Launches Claude Code to score against `eval-rubric.md`

Each run also writes phase logs and metadata to a log directory:

- `run-<id>.claude.log`
- `run-<id>.tests.log`
- `run-<id>.score.log`
- `run-<id>.diff`
- `run-<id>.summary.json`

You can set this explicitly with `--log-dir` and `--run-id` (used by `eval-batch.ts` automatically).

Verify Claude Code outputs "Skill(neon-postgres-egress-optimizer) — Successfully loaded skill" at the start of the run. If it doesn't, the skill didn't trigger and the run is effectively a baseline. Note this in the `results.csv` notes column.

To force the skill, abort and re-run with: `claude "/neon-postgres-egress-optimizer <prompt>"`

## Scoring

Open `eval-rubric.md` and answer each yes/no question per problem against the diff. Record one row in `results.csv`.

**Columns:**

- `date` — YYYY-M

================================================
FILE: evals\neon-postgres-egress-optimizer\tsconfig.json
================================================
{
  "compilerOptions": {
    // Environment setup & latest features
    "lib": ["ESNext"],
    "target": "ESNext",
    "module": "Preserve",
    "moduleDetection": "force",
    "jsx": "react-jsx",
    "allowJs": true,

    // Bundler mode
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "verbatimModuleSyntax": true,
    "noEmit": true,

    // Best practices
    "strict": true,
    "skipLibCheck": true,
    "noFallthroughCasesInSwitch": true,
    "noUncheckedIndexedAccess": true,
    "noImplicitOverride": true,

    // Some stricter flags
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noPropertyAccessFromIndexSignature": true
  },
  "include": ["eval-run.ts", "eval-batch.ts", "eval-stats.ts"]
}


================================================
FILE: evals\neon-postgres-egress-optimizer\.claude\skills\score-eval\SKILL.md
================================================
---
name: score-eval
disable-model-invocation: true
---

Score the eval diff at $ARGUMENTS against the eval rubric.

1. Read the diff file at the path provided
2. Read the eval rubric at eval-rubric.md
3. Read the original fixture app in fixtures/hono-drizzle-app/ for comparison
4. For each problem P1-P5, answer the Detected? and Fixed? questions from the rubric as yes or no
5. Append a row to results.csv — fill in all fields you can determine from the diff and context. Leave fields you can't determine empty.


================================================
FILE: evals\neon-postgres-egress-optimizer\fixtures\hono-drizzle-app\drizzle.config.ts
================================================
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  out: "./drizzle",
  schema: "./src/db/schema.ts",
  dialect: "postgresql",
  dbCredentials: {
    url: process.env.DATABASE_URL!,
  },
});


================================================
FILE: evals\neon-postgres-egress-optimizer\fixtures\hono-drizzle-app\package.json
================================================
{
  "name": "hono-drizzle-app",
  "version": "0.0.1",
  "private": true,
  "scripts": {
    "dev": "bun run --hot src/index.ts",
    "db:push": "bunx drizzle-kit push",
    "format": "bunx prettier --write ../../",
    "test": "bun test"
  },
  "dependencies": {
    "hono": "^4.12.7",
    "@neondatabase/serverless": "^1.0.2",
    "drizzle-orm": "^0.45.1"
  },
  "devDependencies": {
    "@types/bun": "^1.3.10",
    "drizzle-kit": "^0.31.9",
    "typescript": "^5.9.3"
  }
}


================================================
FILE: evals\neon-postgres-egress-optimizer\fixtures\hono-drizzle-app\tsconfig.json
================================================
{
  "compilerOptions": {
    "target": "ESNext",
    "module": "ESNext",
    "moduleResolution": "bundler",
    "strict": true,
    "skipLibCheck": true,
    "noEmit": true
  },
  "include": ["src", "tests"]
}


================================================
FILE: evals\neon-postgres-egress-optimizer\fixtures\hono-drizzle-app\src\index.ts
================================================
import { Hono } from "hono";
import { productsRoute } from "./routes/products";
import { categoriesRoute } from "./routes/categories";
import { statsRoute } from "./routes/stats";

const app = new Hono();

app.route("/products", productsRoute);
app.route("/categories", categoriesRoute);
app.route("/stats", statsRoute);

export default app;


================================================
FILE: evals\neon-postgres-egress-optimizer\fixtures\hono-drizzle-app\src\db\client.ts
================================================
import { neon } from "@neondatabase/serverless";
import { drizzle, type NeonHttpDatabase } from "drizzle-orm/neon-http";
import * as schema from "./schema";

let _db: NeonHttpDatabase<typeof schema>;

function getDb() {
  if (!_db) {
    const sql = neon(process.env.DATABASE_URL!);
    _db = drizzle({ client: sql, schema });
  }
  return _db;
}

// Convenience proxy so routes can import `db` directly
export const db = new Proxy({} as NeonHttpDatabase<typeof schema>, {
  get(_, prop) {
    return (getDb() as any)[prop];
  },
});


================================================
FILE: evals\neon-postgres-egress-optimizer\fixtures\hono-drizzle-app\src\db\schema.ts
================================================
import {
  pgTable,
  serial,
  varchar,
  numeric,
  integer,
  text,
  jsonb,
  timestamp,
} from "drizzle-orm/pg-core";

export const categories = pgTable("categories", {
  id: serial("id").primaryKey(),
  name: varchar("name", { length: 255 }).notNull(),
  slug: varchar("slug", { length: 255 }).notNull().unique(),
});

export const products = pgTable("products", {
  id: serial("id").primaryKey(),
  name: varchar("name", { length: 255 }).notNull(),
  price: numeric("price", { precision: 10, scale: 2 }).notNull(),
  categoryId: integer("category_id")
    .references(() => categories.id)
    .notNull(),
  description: text("description"),
  rawPayload: jsonb("raw_payload"),
  imageUrls: jsonb("image_urls").$type<string[]>(),
  createdAt: timestamp("created_at").defaultNow().notNull(),
});

export const reviews = pgTable("reviews", {
  id: serial("id").primaryKey(),
  productId: integer("product_id")
    .references(() => products.id)
    .notNull(),
  userName: varchar("user_name", { length: 255 }).notNull(),
  rating: integer("rating").notNull(),
  body: text("body"),
  createdAt: timestamp("created_at").defaultNow().notNull(),
});


================================================
FILE: evals\neon-postgres-egress-optimizer\fixtures\hono-drizzle-app\src\routes\categories.ts
================================================
import { Hono } from "hono";
import { db } from "../db/client";
import { categories } from "../db/schema";

export const categoriesRoute = new Hono();

// GET /categories — list all categories
categoriesRoute.get("/", async (c) => {
  const allCategories = await db.select().from(categories);
  return c.json(allCategories);
});


================================================
FILE: evals\neon-postgres-egress-optimizer\fixtures\hono-drizzle-app\src\routes\products.ts
================================================
import { Hono } from "hono";
import { eq } from "drizzle-orm";
import { db } from "../db/client";
import { products, reviews } from "../db/schema";

export const productsRoute = new Hono();

// GET /products — list all products
productsRoute.get("/", async (c) => {
  const allProducts = await db.select().from(products);

  return c.json(
    allProducts.map((p) => ({
      id: p.id,
      name: p.name,
      price: p.price,
      imageUrls: p.imageUrls,
    })),
  );
});

// GET /products/:id — single product with reviews
productsRoute.get("/:id", async (c) => {
  const id = Number(c.req.param("id"));

  const rows = await db
    .select()
    .from(products)
    .leftJoin(reviews, eq(reviews.productId, products.id))
    .where(eq(products.id, id));

  if (rows.length === 0) {
    return c.json({ error: "Not found" }, 404);
  }

  const product = rows[0].products;
  const productReviews = rows
    .filter((r) => r.reviews !== null)
    .map((r) => r.reviews);

  return c.json({ ...product, reviews: productReviews });
});


================================================
FILE: evals\neon-postgres-egress-optimizer\fixtures\hono-drizzle-app\src\routes\stats.ts
================================================
import { Hono } from "hono";
import { db } from "../db/client";
import { reviews, products } from "../db/schema";

export const statsRoute = new Hono();

// GET /stats — review statistics per category
statsRoute.get("/", async (c) => {
  const allReviews = await db.select().from(reviews);
  const allProducts = await db.select().from(products);

  const productCategoryMap = allProducts.reduce(
    (acc, product) => {
      acc[product.id] = product.categoryId;
      return acc;
    },
    {} as Record<number, number>,
  );

  const statsMap = allReviews.reduce(
    (acc, review) => {
      const categoryId = productCategoryMap[review.productId];
      if (!acc[categoryId]) acc[categoryId] = { totalRating: 0, count: 0 };
      acc[categoryId].totalRating += review.rating;
      acc[categoryId].count += 1;
      return acc;
    },
    {} as Record<number, { totalRating: number; count: number }>,
  );

  const stats = Object.entries(statsMap).map(([categoryId, s]) => ({
    categoryId: Number(categoryId),
    avgRating: s.totalRating / s.count,
    reviewCount: s.count,
  }));

  return c.json(stats);
});


================================================
FILE: evals\neon-postgres-egress-optimizer\fixtures\hono-drizzle-app\tests\categories.test.ts
================================================
import { describe, it, expect } from "bun:test";
import app from "../src/index";

describe("GET /categories", () => {
  it("returns a list of categories", async () => {
    const res = await app.request("/categories");
    expect(res.status).toBe(200);

    const data = await res.json();
    expect(Array.isArray(data)).toBe(true);
    expect(data.length).toBe(3);
  });

  it("each category has id, name, slug", async () => {
    const res = await app.request("/categories");
    const data = await res.json();

    for (const category of data) {
      expect(category).toHaveProperty("id");
      expect(category).toHaveProperty("name");
      expect(category).toHaveProperty("slug");
    }
  });
});


================================================
FILE: evals\neon-postgres-egress-optimizer\fixtures\hono-drizzle-app\tests\preload.ts
================================================
import { beforeAll, afterAll } from "bun:test";
import { provisionDatabase, seed, cleanup } from "./setup";

beforeAll(async () => {
  await provisionDatabase();
  await seed();
});

afterAll(async () => {
  await cleanup();
});


================================================
FILE: evals\neon-postgres-egress-optimizer\fixtures\hono-drizzle-app\tests\products.test.ts
================================================
import { describe, it, expect } from "bun:test";
import app from "../src/index";

describe("GET /products", () => {
  it("returns a list of products", async () => {
    const res = await app.request("/products");
    expect(res.status).toBe(200);

    const data = await res.json();
    expect(Array.isArray(data)).toBe(true);
    expect(data.length).toBe(5);
  });

  it("each product has id, name, price, imageUrls", async () => {
    const res = await app.request("/products");
    const data = await res.json();

    for (const product of data) {
      expect(product).toHaveProperty("id");
      expect(product).toHaveProperty("name");
      expect(product).toHaveProperty("price");
      expect(product).toHaveProperty("imageUrls");
    }
  });
});

describe("GET /products/:id", () => {
  it("returns a product with reviews", async () => {
    const res = await app.request("/products/1");
    expect(res.status).toBe(200);

    const data = await res.json();
    expect(data).toHaveProperty("id", 1);
    expect(data).toHaveProperty("name", "Laptop");
    expect(data).toHaveProperty("reviews");
    expect(Array.isArray(data.reviews)).toBe(true);
    expect(data.reviews.length).toBe(3);
  });

  it("returns 404 for non-existent product", async () => {
    const res = await app.request("/products/9999");
    expect(res.status).toBe(404);
  });
});


================================================
FILE: evals\neon-postgres-egress-optimizer\fixtures\hono-drizzle-app\tests\setup.ts
================================================
import { neon } from "@neondatabase/serverless";
import { drizzle } from "drizzle-orm/neon-http";
import { sql } from "drizzle-orm";
import { categories, products, reviews } from "../src/db/schema";
import { $ } from "bun";

let databaseUrl: string;
let provisioned = false;

export async function provisionDatabase() {
  if (provisioned) return databaseUrl;

  // Use existing DATABASE_URL if set, otherwise provision via neon.new
  if (process.env.DATABASE_URL) {
    databaseUrl = process.env.DATABASE_URL;
  } else {
    const res = await fetch("https://neon.new/api/v1/database", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ ref: "agent-skills" }),
    });
    const data = await res.json();
    databaseUrl = data.connection_string;
    process.env.DATABASE_URL = databaseUrl;
  }

  // Push schema using drizzle-kit
  await $`bunx drizzle-kit push --force`.env({
    ...process.env,
    DATABASE_URL: databaseUrl,
  });

  provisioned = true;
  return databaseUrl;
}

export function getTestDb() {
  const client = neon(databaseUrl);
  return drizzle({ client });
}

export async function seed() {
  const db = getTestDb();

  // Categories
  await db.insert(categories).values([
    { name: "Electronics", slug: "electronics" },
    { name: "Books", slug: "books" },
    { name: "Clothing", slug: "clothing" },
  ]);

  const description = `The latest model featuring a high-resolution display, long-lasting battery life, and premium build quality. Designed for professionals and enthusiasts alike, this product delivers exceptional performance across a wide range of tasks. The ergonomic design ensures comfort during extended use, while the advanced thermal management system keeps everything running smoothly. Package includes the main unit, charging cable, quick start guide, and a protective carrying case. Backed by a 2-year manufacturer warranty with worldwide coverage. For detailed specifications, compatibility information, and support resources, visit our product page.`;
  const rawPayload = {
    supplier: "TechDistributors Inc.",
    sku: "TD-2024-PRO-001",
    importedAt: "2025-11-14T08:30:00Z",
    source: "bulk-import-v3",
    originalListing: {
      title: "Professional Grade Equipment",
      htmlDescription:
        "<div class='product-detail'>" +
        "<p>Premium quality materials and construction. ".repeat(200) +
        "</p></div>",
      specifications: Object.fromEntries(
        Array.from({ length: 50 }, (_, i) => [
          `spec_${i}`,
          `value_${i}_${"detail".repeat(20)}`,
        ]),
      ),
      shippingMatrix: Array.from({ length: 100 }, (_, i) => ({
        region: `region_${i}`,
        carrier: `carrier_${i % 5}`,
        rate: (Math.random() * 50).toFixed(2),
        estimatedDays: Math.floor(Math.random() * 14) + 1,
      })),
    },
  };

  await db.insert(products).values([
    {
      name: "Laptop",
      price: "999.99",
      categoryId: 1,
      description,
      rawPayload,
      imageUrls: ["https://example.com/laptop.jpg"],
    },
    {
      name: "Phone",
      price: "699.99",
      categoryId: 1,
      description,
      rawPayload,
      imageUrls: ["https://example.com/phone.jpg"],
    },
    {
      name: "TypeScript Handbook",
      price: "29.99",
      categoryId: 2,
      description,
      rawPayload,
      imageUrls: ["https://example.com/ts-book.jpg"],
    },
    {
      name: "Winter Jacket",
      price: "149.99",
      categoryId: 3,
      description,
      rawPayload,
      imageUrls: ["https://example.com/jacket.jpg"],
    },
    {
      name: "Running Shoes",
      price: "89.99",
      categoryId: 3,
      description,
      rawPayload,
      imageUrls: ["https://example.com/shoes.jpg"],
    },
  ]);

  // Seed reviews
  await db.insert(reviews).values([
    { productId: 1, userName: "alice", rating: 5, body: "Great laptop!" },
    { productId: 1, userName: "bob", rating: 4, body: "Good value." },
    { productId: 1, userName: "charlie", rating: 3, body: "Decent." },
    { productId: 2, userName: "diana", rating: 5, body: "Love this phone." },
    { productId: 2, userName: "eve", rating: 4, body: "Nice screen." },
    { productId: 3, userName: "frank", rating: 5, body: "Excellent book." },
    { productId: 3, userName: "grace", rating: 4, body: "Very helpful." },
    { productId: 4, userName: "hank", rating: 3, body: "Runs small." },
    { productId: 5, userName: "iris", rating: 5, body: "Very comfortable." },
    { productId: 5, userName: "jack", rating: 4, body: "Good for running." },
  ]);
}

export async function cleanup() {
  const db = getTestDb();
  await db.execute(
    sql`TRUNCATE reviews, products, categories RESTART IDENTITY CASCADE`,
  );
}


================================================
FILE: evals\neon-postgres-egress-optimizer\fixtures\hono-drizzle-app\tests\stats.test.ts
================================================
import { describe, it, expect } from "bun:test";
import app from "../src/index";

describe("GET /stats", () => {
  it("returns review statistics per category", async () => {
    const res = await app.request("/stats");
    expect(res.status).toBe(200);

    const data = await res.json();
    expect(Array.isArray(data)).toBe(true);
    expect(data.length).toBe(3);
  });

  it("each stat has categoryId, avgRating, reviewCount", async () => {
    const res = await app.request("/stats");
    const data = await res.json();

    for (const stat of data) {
      expect(stat).toHaveProperty("categoryId");
      expect(stat).toHaveProperty("avgRating");
      expect(stat).toHaveProperty("reviewCount");
      expect(typeof stat.avgRating).toBe("number");
      expect(typeof stat.reviewCount).toBe("number");
    }
  });

  it("computes correct averages", async () => {
    const res = await app.request("/stats");
    const data = await res.json();

    // Electronics (category 1): ratings 5, 4, 3, 5, 4 -> avg 4.2, count 5
    const electronics = data.find((s: any) => s.categoryId === 1);
    expect(electronics.avgRating).toBeCloseTo(4.2);
    expect(electronics.reviewCount).toBe(5);
  });
});


================================================
FILE: evals\neon-postgres-egress-optimizer\mock-stats\pg_stat_statements.md
================================================
# pg_stat_statements — Diagnostic Output

Captured over a 24-hour production window.

## Queries by total rows returned

| query                                                                                                                                                                                                                                                                                                                                                                                                                                 | calls  | rows      | avg_rows_per_call |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | --------- | ----------------- |
| SELECT "id", "name", "price", "category_id", "description", "raw_payload", "image_urls", "created_at" FROM "products"                                                                                                                                                                                                                                                                                                                 | 500    | 500,000   | 1,000             |
| SELECT "id", "product_id", "user_name", "rating", "body", "created_at" FROM "reviews"                                                                                                                                                                                                                                                                                                                                                 | 200    | 1,000,000 | 5,000             |
| SELECT "products"."id", "products"."name", "products"."price", "products"."category_id", "products"."description", "products"."raw_payload", "products"."image_urls", "products"."created_at", "reviews"."id", "reviews"."product_id", "reviews"."user_name", "reviews"."rating", "reviews"."body", "reviews"."created_at" FROM "products" LEFT JOIN "reviews" ON "reviews"."product_id" = "products"."id" WHERE "products"."id" = $1 | 300    | 60,000    | 200               |
| SELECT "id", "name", "slug" FROM "categories"                                                                                                                                                                                                                                                                                                                                                                                         | 50,000 | 500,000   | 10                |

## Queries by call frequency

| query                                                                                                                                                                                                                                                                                                                                                                                                                                 | calls  | rows      | avg_rows_per_call |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | --------- | ----------------- |
| SELECT "id", "name", "slug" FROM "categories"                                                                                                                                                                                                                                                                                                                                                                                         | 50,000 | 500,000   | 10                |
| SELECT "id", "name", "price", "category_id", "description", "raw_payload", "image_urls", "created_at" FROM "products"                                                                                                                                                                                                                                                                                                                 | 500    | 500,000   | 1,000             |
| SELECT "products"."id", "products"."name", "products"."price", "products"."category_id", "products"."description", "products"."raw_payload", "products"."image_urls", "products"

================================================
FILE: evals\neon-postgres-egress-optimizer\skill-versions\SKILL-v001.md
================================================
---
name: neon-postgres-egress-optimizer
description: >-
  Diagnose and fix excessive Postgres egress (network data transfer) in a codebase.
  Use when a user mentions high database bills, unexpected data transfer costs,
  network transfer charges, egress spikes, "why is my Neon bill so high",
  "database costs jumped", SELECT * optimization, query overfetching,
  reduce Neon costs, optimize database usage, or wants to reduce data sent
  from their database to their application. Also use when reviewing query
  patterns for cost efficiency, even if the user doesn't explicitly mention
  egress or data transfer.
---

# Postgres Egress Optimizer

Guide the user through diagnosing and fixing application-side query patterns that cause excessive data transfer (egress) from their Postgres database. Most high egress bills come from the application fetching more data than it uses.

## Step 1: Diagnose

Identify which queries transfer the most data. The primary tool is the `pg_stat_statements` extension.

### Check if pg_stat_statements is available

```sql
SELECT 1 FROM pg_stat_statements LIMIT 1;
```

If this errors, the extension needs to be created:

```sql
CREATE EXTENSION IF NOT EXISTS pg_stat_statements;
```

On Neon, it is available by default but may need this CREATE EXTENSION step.

### Handle empty stats

Stats are cleared when a Neon compute scales to zero and restarts. If the stats are empty or the compute recently woke up:

1. Reset the stats to start a clean measurement window: `SELECT pg_stat_statements_reset();`
2. Let the application run under representative traffic for at least an hour.
3. Return and run the diagnostic queries below.

If the user has stats from a production database, use those. If they have no access to production stats, proceed to Step 2 and analyze the codebase directly — code-level patterns are often sufficient to identify the worst offenders.

### Diagnostic queries

Run these to identify the top egress contributors. Focus on queries that return many rows, return wide rows (JSONB, TEXT, BYTEA columns), or are called very frequently.

**Queries returning the most total rows:**

```sql
SELECT query, calls, rows AS total_rows, rows / calls AS avg_rows_per_call
FROM pg_stat_statements
WHERE calls > 0
ORDER BY rows DESC
LIMIT 10;
```

**Queries returning the most rows per execution** (poorly scoped SELECTs, missing pagination):

```sql
SELECT query, calls, rows AS total_rows, rows / calls AS avg_rows_per_call
FROM pg_stat_statements
WHERE calls > 0
ORDER BY avg_rows_per_call DESC
LIMIT 10;
```

**Most frequently called queries** (candidates for caching):

```sql
SELECT query, calls, rows AS total_rows, rows / calls AS avg_rows_per_call
FROM pg_stat_statements
WHERE calls > 0
ORDER BY calls DESC
LIMIT 10;
```

**Longest running queries** (not a direct egress measure, but helps identify problem queries during a spike):

```sql
SELECT query, calls, rows AS total_rows,
  round(total_exec_time::numeric, 2) AS total_exec_time_ms
FROM pg_stat_statements
WHERE calls > 0
ORDER BY total_exec_time DESC
LIMIT 10;
```

### Interpret the results

Rank findings by estimated egress impact:

- **High row count + wide rows** = biggest egress. A query returning 1,000 rows where each row includes a 50KB JSONB column transfers ~50MB per call.
- **Extreme call frequency** on even small queries adds up. A query called 50,000 times/day returning 10 rows each = 500,000 rows/day.
- **Cross-reference with the schema** to identify which columns are wide. Look for JSONB, TEXT, BYTEA, and large VARCHAR columns.

## Step 2: Analyze codebase

For each high-egress query, find the corresponding application code and identify what the response actually uses versus what the query fetches.

## Step 3: Fix

Apply the appropriate fix for each problem found. Below are the most common egress anti-patterns and how to fix them.

### Unused columns (SELECT \*)

**Problem:** The query fetches all columns but the application only uses a few. Large columns (JSONB blobs, TEXT fields) get transferred over the wire and discarded.

**Before:**

```sql
SELECT * FROM products;
```

**After:**

```sql
SELECT id, name, price, image_urls FROM products;
```

### Missing pagination

**Problem:** The query returns the entire table on every request. As the table grows, so does egress — linearly with row count.

This is easy to miss because the application may work fine with small datasets. But at scale, an unpaginated endpoint returning 10,000 rows with even moderate column widths can transfer hundreds of megabytes per day.

**Before:**

```sql
SELECT id, name, price FROM products;
```

**After:**

```sql
SELECT id, name, price FROM products
ORDER BY id
LIMIT 50 OFFSET 0;
```

When adding pagination, check whether the consuming client already supports paginated responses. If not, pick sensible defaults and document the pagination parameters in the API.

### High-frequency queries on static data

**Problem:** A query is called thousands of time

================================================
FILE: evals\neon-postgres-egress-optimizer\skill-versions\SKILL-v002.md
================================================
---
name: neon-postgres-egress-optimizer
description: >-
  Diagnose and fix excessive Postgres egress (network data transfer) in a codebase.
  Use when a user mentions high database bills, unexpected data transfer costs,
  network transfer charges, egress spikes, "why is my Neon bill so high",
  "database costs jumped", SELECT * optimization, query overfetching,
  reduce Neon costs, optimize database usage, or wants to reduce data sent
  from their database to their application. Also use when reviewing query
  patterns for cost efficiency, even if the user doesn't explicitly mention
  egress or data transfer.
---

# Postgres Egress Optimizer

Guide the user through diagnosing and fixing application-side query patterns that cause excessive data transfer (egress) from their Postgres database. Most high egress bills come from the application fetching more data than it uses.

## Step 1: Diagnose

Identify which queries transfer the most data. The primary tool is the `pg_stat_statements` extension.

### Check if pg_stat_statements is available

```sql
SELECT 1 FROM pg_stat_statements LIMIT 1;
```

If this errors, the extension needs to be created:

```sql
CREATE EXTENSION IF NOT EXISTS pg_stat_statements;
```

On Neon, it is available by default but may need this CREATE EXTENSION step.

### Handle empty stats

Stats are cleared when a Neon compute scales to zero and restarts. If the stats are empty or the compute recently woke up:

1. Reset the stats to start a clean measurement window: `SELECT pg_stat_statements_reset();`
2. Let the application run under representative traffic for at least an hour.
3. Return and run the diagnostic queries below.

If the user has stats from a production database, use those. If they have no access to production stats, proceed to Step 2 and analyze the codebase directly — code-level patterns are often sufficient to identify the worst offenders.

### Diagnostic queries

Run these to identify the top egress contributors. Focus on queries that return many rows, return wide rows (JSONB, TEXT, BYTEA columns), or are called very frequently.

**Queries returning the most total rows:**

```sql
SELECT query, calls, rows AS total_rows, rows / calls AS avg_rows_per_call
FROM pg_stat_statements
WHERE calls > 0
ORDER BY rows DESC
LIMIT 10;
```

**Queries returning the most rows per execution** (poorly scoped SELECTs, missing pagination):

```sql
SELECT query, calls, rows AS total_rows, rows / calls AS avg_rows_per_call
FROM pg_stat_statements
WHERE calls > 0
ORDER BY avg_rows_per_call DESC
LIMIT 10;
```

**Most frequently called queries** (candidates for caching):

```sql
SELECT query, calls, rows AS total_rows, rows / calls AS avg_rows_per_call
FROM pg_stat_statements
WHERE calls > 0
ORDER BY calls DESC
LIMIT 10;
```

**Longest running queries** (not a direct egress measure, but helps identify problem queries during a spike):

```sql
SELECT query, calls, rows AS total_rows,
  round(total_exec_time::numeric, 2) AS total_exec_time_ms
FROM pg_stat_statements
WHERE calls > 0
ORDER BY total_exec_time DESC
LIMIT 10;
```

### Interpret the results

Rank findings by estimated egress impact:

- **High row count + wide rows** = biggest egress. A query returning 1,000 rows where each row includes a 50KB JSONB column transfers ~50MB per call.
- **Extreme call frequency** on even small queries adds up. A query called 50,000 times/day returning 10 rows each = 500,000 rows/day.
- **Cross-reference with the schema** to identify which columns are wide. Look for JSONB, TEXT, BYTEA, and large VARCHAR columns.

## Step 2: Analyze codebase

For each query identified in Step 1, or for each database query in the codebase if no stats are available, check:

- Does it select only the columns the response needs?
- Does it return a bounded number of rows (LIMIT/pagination)?
- Is it called frequently enough to benefit from caching?
- Does it fetch raw data that gets aggregated in application code?
- Does it use a JOIN that duplicates parent data across child rows?

## Step 3: Fix

Apply the appropriate fix for each problem found. Below are the most common egress anti-patterns and how to fix them.

### Unused columns (SELECT \*)

**Problem:** The query fetches all columns but the application only uses a few. Large columns (JSONB blobs, TEXT fields) get transferred over the wire and discarded.

**Before:**

```sql
SELECT * FROM products;
```

**After:**

```sql
SELECT id, name, price, image_urls FROM products;
```

### Missing pagination

**Problem:** A list endpoint returns all rows with no LIMIT. This is an unbounded egress risk — every new row in the table increases data transfer on every request. Flag this regardless of current table size.

This is easy to miss because the application may work fine with small datasets. But at scale, an unpaginated endpoint returning 10,000 rows with even moderate column widths can transfer hundreds of megabytes per day.

**Before:**

```sql
SELECT id, name, price FROM products;
```

**

================================================
FILE: evals\neon-postgres-egress-optimizer\skill-versions\SKILL-v003.md
================================================
---
name: neon-postgres-egress-optimizer
description: >-
  Diagnose and fix excessive Postgres egress (network data transfer) in a codebase.
  Use when a user mentions high database bills, unexpected data transfer costs,
  network transfer charges, egress spikes, "why is my Neon bill so high",
  "database costs jumped", SELECT * optimization, query overfetching,
  reduce Neon costs, optimize database usage, or wants to reduce data sent
  from their database to their application. Also use when reviewing query
  patterns for cost efficiency, even if the user doesn't explicitly mention
  egress or data transfer.
---

# Postgres Egress Optimizer

Guide the user through diagnosing and fixing application-side query patterns that cause excessive data transfer (egress) from their Postgres database. Most high egress bills come from the application fetching more data than it uses.

## Step 1: Diagnose

Identify which queries transfer the most data. The primary tool is the `pg_stat_statements` extension.

### Check if pg_stat_statements is available

```sql
SELECT 1 FROM pg_stat_statements LIMIT 1;
```

If this errors, the extension needs to be created:

```sql
CREATE EXTENSION IF NOT EXISTS pg_stat_statements;
```

On Neon, it is available by default but may need this CREATE EXTENSION step.

### Handle empty stats

Stats are cleared when a Neon compute scales to zero and restarts. If the stats are empty or the compute recently woke up:

1. Reset the stats to start a clean measurement window: `SELECT pg_stat_statements_reset();`
2. Let the application run under representative traffic for at least an hour.
3. Return and run the diagnostic queries below.

If the user has stats from a production database, use those. If they have no access to production stats, proceed to Step 2 and analyze the codebase directly — code-level patterns are often sufficient to identify the worst offenders.

### Diagnostic queries

Run these to identify the top egress contributors. Focus on queries that return many rows, return wide rows (JSONB, TEXT, BYTEA columns), or are called very frequently.

**Queries returning the most total rows:**

```sql
SELECT query, calls, rows AS total_rows, rows / calls AS avg_rows_per_call
FROM pg_stat_statements
WHERE calls > 0
ORDER BY rows DESC
LIMIT 10;
```

**Queries returning the most rows per execution** (poorly scoped SELECTs, missing pagination):

```sql
SELECT query, calls, rows AS total_rows, rows / calls AS avg_rows_per_call
FROM pg_stat_statements
WHERE calls > 0
ORDER BY avg_rows_per_call DESC
LIMIT 10;
```

**Most frequently called queries** (candidates for caching):

```sql
SELECT query, calls, rows AS total_rows, rows / calls AS avg_rows_per_call
FROM pg_stat_statements
WHERE calls > 0
ORDER BY calls DESC
LIMIT 10;
```

**Longest running queries** (not a direct egress measure, but helps identify problem queries during a spike):

```sql
SELECT query, calls, rows AS total_rows,
  round(total_exec_time::numeric, 2) AS total_exec_time_ms
FROM pg_stat_statements
WHERE calls > 0
ORDER BY total_exec_time DESC
LIMIT 10;
```

### Interpret the results

Rank findings by estimated egress impact:

- **High row count + wide rows** = biggest egress. A query returning 1,000 rows where each row includes a 50KB JSONB column transfers ~50MB per call.
- **Extreme call frequency** on even small queries adds up. A query called 50,000 times/day returning 10 rows each = 500,000 rows/day.
- **Cross-reference with the schema** to identify which columns are wide. Look for JSONB, TEXT, BYTEA, and large VARCHAR columns.

## Step 2: Analyze codebase

For each query identified in Step 1, or for each database query in the codebase if no stats are available, check:

- Does it select only the columns the response needs?
- Does it return a bounded number of rows (LIMIT/pagination)?
- Is it called frequently enough to benefit from caching?
- Does it fetch raw data that gets aggregated in application code?
- Does it use a JOIN that duplicates parent data across child rows?

## Step 3: Fix

Apply the appropriate fix for each problem found. Below are the most common egress anti-patterns and how to fix them.

### Unused columns (SELECT \*)

**Problem:** The query fetches all columns but the application only uses a few. Large columns (JSONB blobs, TEXT fields) get transferred over the wire and discarded.

**Before:**

```sql
SELECT * FROM products;
```

**After:**

```sql
SELECT id, name, price, image_urls FROM products;
```

### Missing pagination

**Problem:** A list endpoint returns all rows with no LIMIT. This is an unbounded egress risk — every new row in the table increases data transfer on every request. Flag this regardless of current table size.

This is easy to miss because the application may work fine with small datasets. But at scale, an unpaginated endpoint returning 10,000 rows with even moderate column widths can transfer hundreds of megabytes per day.

**Before:**

```sql
SELECT id, name, price FROM products;
```

**

================================================
FILE: plugins\neon-postgres\mcp.json
================================================
{
  "mcpServers": {
    "neon": {
      "type": "http",
      "url": "https://mcp.neon.tech/mcp"
    }
  }
}


================================================
FILE: plugins\neon-postgres\.claude-plugin\plugin.json
================================================
{
  "name": "neon",
  "version": "1.0.0",
  "description": "Manage your Neon projects and databases with the neon-postgres agent skill and the Neon MCP Server",
  "author": {
    "name": "Neon",
    "url": "https://neon.com"
  },
  "homepage": "https://neon.com",
  "repository": "https://github.com/neondatabase/agent-skills",
  "license": "Apache-2.0",
  "keywords": ["neon", "postgres", "serverless", "database", "mcp"],
  "skills": "./skills/",
  "mcpServers": "./mcp.json"
}


================================================
FILE: plugins\neon-postgres\.cursor-plugin\plugin.json
================================================
{
  "name": "neon-postgres",
  "displayName": "Neon Postgres",
  "version": "1.0.0",
  "description": "Manage your Neon projects and databases with the neon-postgres agent skill and the Neon MCP Server",
  "author": {
    "name": "Neon",
    "email": "andre@neon.tech"
  },
  "homepage": "https://neon.tech/docs/ai/neon-mcp-server",
  "repository": "https://github.com/neondatabase/agent-skills",
  "license": "Apache-2.0",
  "keywords": ["neon", "postgres", "serverless", "database", "mcp", "cursor"],
  "logo": "assets/logo.svg",
  "skills": "./skills/",
  "mcpServers": "./mcp.json"
}


================================================
FILE: skills\claimable-postgres\SKILL.md
================================================
---
name: claimable-postgres
description: >-
  Provision instant temporary Postgres databases via Claimable Postgres by Neon
  (neon.new) with no login, signup, or credit card. Supports REST API, CLI, and
  SDK. Use when users ask for a quick Postgres environment, a throwaway
  DATABASE_URL for prototyping/tests, or "just give me a DB now". Triggers
  include: "quick postgres", "temporary postgres", "no signup database",
  "no credit card database", "instant DATABASE_URL", "npx neon-new", "neon.new",
  "neon.new API", "claimable postgres API".
---

# Claimable Postgres

Instant Postgres databases for local development, demos, prototyping, and test environments. No account required. Databases expire after 72 hours unless claimed to a Neon account.

## Quick Start

```bash
curl -s -X POST "https://neon.new/api/v1/database" \
  -H "Content-Type: application/json" \
  -d '{"ref": "agent-skills"}'
```

Parse `connection_string` and `claim_url` from the JSON response. Write `connection_string` to the project's `.env` as `DATABASE_URL`.

For other methods (CLI, SDK, Vite plugin), see [Which Method?](#which-method) below.

## Which Method?

- **REST API**: Returns structured JSON. No runtime dependency beyond `curl`. Preferred when the agent needs predictable output and error handling.
- **CLI** (`npx neon-new@latest --yes`): Provisions and writes `.env` in one command. Convenient when Node.js is available and the user wants a simple setup.
- **SDK** (`neon-new/sdk`): Scripts or programmatic provisioning in Node.js.
- **Vite plugin** (`vite-plugin-neon-new`): Auto-provisions on `vite dev` if `DATABASE_URL` is missing. Use when the user has a Vite project.
- **Browser**: User cannot run CLI or API. Direct to https://neon.new.

## REST API

**Base URL:** `https://neon.new/api/v1`

### Create a database

```bash
curl -s -X POST "https://neon.new/api/v1/database" \
  -H "Content-Type: application/json" \
  -d '{"ref": "agent-skills"}'
```

| Parameter | Required | Description |
|-----------|----------|-------------|
| `ref` | Yes | Tracking tag that identifies who provisioned the database. Use `"agent-skills"` when provisioning through this skill. |
| `enable_logical_replication` | No | Enable logical replication (default: false, cannot be disabled once enabled) |

The `connection_string` returned by the API is a pooled connection URL. For a direct (non-pooled) connection (e.g. Prisma migrations), remove `-pooler` from the hostname. The CLI writes both pooled and direct URLs automatically.

**Response:**

```json
{
  "id": "019beb39-37fb-709d-87ac-7ad6198b89f7",
  "status": "UNCLAIMED",
  "neon_project_id": "gentle-scene-06438508",
  "connection_string": "postgresql://...",
  "claim_url": "https://neon.new/claim/019beb39-...",
  "expires_at": "2026-01-26T14:19:14.580Z",
  "created_at": "2026-01-23T14:19:14.580Z",
  "updated_at": "2026-01-23T14:19:14.580Z"
}
```

### Check status

```bash
curl -s "https://neon.new/api/v1/database/{id}"
```

Returns the same response shape. Status transitions: `UNCLAIMED` -> `CLAIMING` -> `CLAIMED`. After the database is claimed, `connection_string` returns `null`.

### Error responses

| Condition | HTTP | Message |
|-----------|------|---------|
| Missing or empty `ref` | 400 | `Missing referrer` |
| Invalid database ID | 400 | `Database not found` |
| Invalid JSON body | 500 | `Failed to create the database.` |

## CLI

```bash
npx neon-new@latest --yes
```

Provisions a database and writes the connection string to `.env` in one step. Always use `@latest` and `--yes` (skips interactive prompts that would stall the agent).

### Pre-run Check

Check if `DATABASE_URL` (or the chosen key) already exists in the target `.env`. The CLI exits without provisioning if it finds the key.

If the key exists, offer the user three options:

1. Remove or comment out the existing line, then rerun.
2. Use `--env` to write to a different file (e.g. `--env .env.local`).
3. Use `--key` to write under a different variable name.

Get confirmation before proceeding.

### Options

| Option | Alias | Description | Default |
|--------|-------|-------------|---------|
| `--yes` | `-y` | Skip prompts, use defaults | `false` |
| `--env` | `-e` | .env file path | `./.env` |
| `--key` | `-k` | Connection string env var key | `DATABASE_URL` |
| `--prefix` | `-p` | Prefix for generated public env vars | `PUBLIC_` |
| `--seed` | `-s` | Path to seed SQL file | none |
| `--logical-replication` | `-L` | Enable logical replication | `false` |
| `--ref` | `-r` | Referrer id (use `agent-skills` when provisioning through this skill) | none |

Alternative package managers: `yarn dlx neon-new@latest`, `pnpm dlx neon-new@latest`, `bunx neon-new@latest`, `deno run -A neon-new@latest`.

### Output

The CLI writes to the target `.env`:

```
DATABASE_URL=postgresql://...              # pooled (use for application queries)
DATABASE_URL_DIRECT=postgresql://...       # direct (use for migrations, e.g. Prisma)
PUBLIC_POSTGRES_CLAIM_URL=

================================================
FILE: skills\neon-postgres\SKILL.md
================================================
---
name: neon-postgres
description: Guides and best practices for working with Neon Serverless Postgres. Covers getting started, local development with Neon, choosing a connection method, Neon features, authentication (@neondatabase/auth), PostgREST-style data API (@neondatabase/neon-js), Neon CLI, and Neon's Platform API/SDKs. Use for any Neon-related questions.
---

# Neon Serverless Postgres

Neon is a serverless Postgres platform that separates compute and storage to offer autoscaling, branching, instant restore, and scale-to-zero. It's fully compatible with Postgres and works with any language, framework, or ORM that supports Postgres.

## Neon Documentation

The Neon documentation is the source of truth for all Neon-related information. Always verify claims against the official docs before responding. Neon features and APIs evolve, so prefer fetching current docs over relying on training data.

### Fetching Docs as Markdown

Any Neon doc page can be fetched as markdown in two ways:

1. **Append `.md` to the URL** (simplest): https://neon.com/docs/introduction/branching.md
2. **Request `text/markdown`** on the standard URL: `curl -H "Accept: text/markdown" https://neon.com/docs/introduction/branching`

Both return the same markdown content. Use whichever method your tools support.

### Finding the Right Page

The docs index lists every available page with its URL and a short description:

```
https://neon.com/docs/llms.txt
```

Common doc URLs are organized in the topic links below. If you need a page not listed here, search the docs index: https://neon.com/docs/llms.txt — don't guess URLs.

## What Is Neon

Use this for architecture explanations and terminology (organizations, projects, branches, endpoints) before giving implementation advice.

Link: https://neon.com/docs/ai/skills/neon-postgres/references/what-is-neon.md

## Getting Started

Use this for first-time setup: org/project selection, connection strings, driver installation, optional auth, and initial schema setup.

Link: https://neon.com/docs/ai/skills/neon-postgres/references/getting-started.md

## Connection Methods & Drivers

Use this when you need to pick the correct transport and driver based on runtime constraints (TCP, HTTP, WebSocket, edge, serverless, long-running).

Link: https://neon.com/docs/ai/skills/neon-postgres/references/connection-methods.md

### Serverless Driver

Use this for `@neondatabase/serverless` patterns, including HTTP queries, WebSocket transactions, and runtime-specific optimizations.

Link: https://neon.com/docs/ai/skills/neon-postgres/references/neon-serverless.md

### Neon JS SDK

Use this for combined Neon Auth + Data API workflows with PostgREST-style querying and typed client setup.

Link: https://neon.com/docs/ai/skills/neon-postgres/references/neon-js.md

## Developer Tools

Use this for local development enablement with `npx neonctl@latest init`, VSCode extension setup, and Neon MCP server configuration.

Link: https://neon.com/docs/ai/skills/neon-postgres/references/devtools.md

### Neon CLI

Use this for terminal-first workflows, scripts, and CI/CD automation with `neonctl`.

Link: https://neon.com/docs/ai/skills/neon-postgres/references/neon-cli.md

## Neon Admin API

The Neon Admin API can be used to manage Neon resources programmatically. It is used behind the scenes by the Neon CLI and MCP server, but can also be used directly for more complex automation workflows or when embedding Neon in other applications.

### Neon REST API

Use this for direct HTTP automation, endpoint-level control, API key auth, rate-limit handling, and operation polling.

Link: https://neon.com/docs/ai/skills/neon-postgres/references/neon-rest-api.md

### Neon TypeScript SDK

Use this when implementing typed programmatic control of Neon resources in TypeScript via `@neondatabase/api-client`.

Link: https://neon.com/docs/ai/skills/neon-postgres/references/neon-typescript-sdk.md

### Neon Python SDK

Use this when implementing programmatic Neon management in Python with the `neon-api` package.

Link: https://neon.com/docs/ai/skills/neon-postgres/references/neon-python-sdk.md

## Neon Auth

Use this for managed user authentication setup, UI components, auth methods, and Neon Auth integration pitfalls in Next.js and React apps.

Link: https://neon.com/docs/ai/skills/neon-postgres/references/neon-auth.md

Neon Auth is also embedded in the Neon JS SDK - so depending on your use case, you may want to use the Neon JS SDK instead of Neon Auth. See https://neon.com/docs/ai/skills/neon-postgres/references/connection-methods.md for more details.

## Branching

Use this when the user is planning isolated environments, schema migration testing, preview deployments, or branch lifecycle automation.

Key points:

- Branches are instant, copy-on-write clones (no full data copy).
- Each branch has its own compute endpoint.
- Use the neonctl CLI or MCP server to create, inspect, and compare branches.

Link: https://neon.com/docs/ai/skills/

================================================
FILE: skills\neon-postgres-egress-optimizer\SKILL.md
================================================
---
name: neon-postgres-egress-optimizer
description: >-
  Diagnose and fix excessive Postgres egress (network data transfer) in a codebase.
  Use when a user mentions high database bills, unexpected data transfer costs,
  network transfer charges, egress spikes, "why is my Neon bill so high",
  "database costs jumped", SELECT * optimization, query overfetching,
  reduce Neon costs, optimize database usage, or wants to reduce data sent
  from their database to their application. Also use when reviewing query
  patterns for cost efficiency, even if the user doesn't explicitly mention
  egress or data transfer.
---

# Postgres Egress Optimizer

Guide the user through diagnosing and fixing application-side query patterns that cause excessive data transfer (egress) from their Postgres database. Most high egress bills come from the application fetching more data than it uses.

## Step 1: Diagnose

Identify which queries transfer the most data. The primary tool is the `pg_stat_statements` extension.

### Check if pg_stat_statements is available

```sql
SELECT 1 FROM pg_stat_statements LIMIT 1;
```

If this errors, the extension needs to be created:

```sql
CREATE EXTENSION IF NOT EXISTS pg_stat_statements;
```

On Neon, it is available by default but may need this CREATE EXTENSION step.

### Handle empty stats

Stats are cleared when a Neon compute scales to zero and restarts. If the stats are empty or the compute recently woke up:

1. Reset the stats to start a clean measurement window: `SELECT pg_stat_statements_reset();`
2. Let the application run under representative traffic for at least an hour.
3. Return and run the diagnostic queries below.

If the user has stats from a production database, use those. If they have no access to production stats, proceed to Step 2 and analyze the codebase directly — code-level patterns are often sufficient to identify the worst offenders.

### Diagnostic queries

Run these to identify the top egress contributors. Focus on queries that return many rows, return wide rows (JSONB, TEXT, BYTEA columns), or are called very frequently.

**Queries returning the most total rows:**

```sql
SELECT query, calls, rows AS total_rows, rows / calls AS avg_rows_per_call
FROM pg_stat_statements
WHERE calls > 0
ORDER BY rows DESC
LIMIT 10;
```

**Queries returning the most rows per execution** (poorly scoped SELECTs, missing pagination):

```sql
SELECT query, calls, rows AS total_rows, rows / calls AS avg_rows_per_call
FROM pg_stat_statements
WHERE calls > 0
ORDER BY avg_rows_per_call DESC
LIMIT 10;
```

**Most frequently called queries** (candidates for caching):

```sql
SELECT query, calls, rows AS total_rows, rows / calls AS avg_rows_per_call
FROM pg_stat_statements
WHERE calls > 0
ORDER BY calls DESC
LIMIT 10;
```

**Longest running queries** (not a direct egress measure, but helps identify problem queries during a spike):

```sql
SELECT query, calls, rows AS total_rows,
  round(total_exec_time::numeric, 2) AS total_exec_time_ms
FROM pg_stat_statements
WHERE calls > 0
ORDER BY total_exec_time DESC
LIMIT 10;
```

### Interpret the results

Rank findings by estimated egress impact:

- **High row count + wide rows** = biggest egress. A query returning 1,000 rows where each row includes a 50KB JSONB column transfers ~50MB per call.
- **Extreme call frequency** on even small queries adds up. A query called 50,000 times/day returning 10 rows each = 500,000 rows/day.
- **Cross-reference with the schema** to identify which columns are wide. Look for JSONB, TEXT, BYTEA, and large VARCHAR columns.

## Step 2: Analyze codebase

For each query identified in Step 1, or for each database query in the codebase if no stats are available, check:

- Does it select only the columns the response needs?
- Does it return a bounded number of rows (LIMIT/pagination)?
- Is it called frequently enough to benefit from caching?
- Does it fetch raw data that gets aggregated in application code?
- Does it use a JOIN that duplicates parent data across child rows?

## Step 3: Fix

Apply the appropriate fix for each problem found. Below are the most common egress anti-patterns and how to fix them.

### Unused columns (SELECT \*)

**Problem:** The query fetches all columns but the application only uses a few. Large columns (JSONB blobs, TEXT fields) get transferred over the wire and discarded.

**Before:**

```sql
SELECT * FROM products;
```

**After:**

```sql
SELECT id, name, price, image_urls FROM products;
```

### Missing pagination

**Problem:** A list endpoint returns all rows with no LIMIT. This is an unbounded egress risk — every new row in the table increases data transfer on every request. Flag this regardless of current table size.

This is easy to miss because the application may work fine with small datasets. But at scale, an unpaginated endpoint returning 10,000 rows with even moderate column widths can transfer hundreds of megabytes per day.

**Before:**

```sql
SELECT id, name, price FROM products;
```

**
```

## File: .claude-plugin\marketplace.json
```
{
  "name": "neon",
  "owner": {
    "name": "Andre Landgraf",
    "email": "andre@neon.tech"
  },
  "metadata": {
    "description": "Official Neon Serverless Postgres plugins for Claude Code",
    "version": "1.0.0"
  },
  "plugins": [
    {
      "name": "neon-postgres",
      "source": "./plugins/neon-postgres",
      "description": "Manage your Neon projects and databases with the neon-postgres agent skill and the Neon MCP Server",
      "version": "1.0.0",
      "category": "database",
      "tags": ["postgres", "serverless", "database", "mcp", "neon"]
    }
  ]
}

```

## File: .cursor-plugin\marketplace.json
```
{
  "name": "neon",
  "owner": {
    "name": "Andre Landgraf",
    "email": "andre@neon.tech"
  },
  "metadata": {
    "description": "Official Neon Serverless Postgres plugins for Cursor",
    "version": "1.0.0",
    "pluginRoot": "plugins"
  },
  "plugins": [
    {
      "name": "neon-postgres",
      "source": "neon-postgres",
      "description": "Manage your Neon projects and databases with the neon-postgres agent skill and the Neon MCP Server"
    }
  ]
}

```

## File: .github\workflows\validate-plugins.yml
```
name: Validate Plugins

on:
  pull_request:
  push:
    branches:
      - main
  workflow_dispatch:

jobs:
  validate-plugins:
    runs-on: ubuntu-latest
    steps:
      - name: Check out repository
        uses: actions/checkout@v4

      - name: Set up Node.js
        uses: actions/setup-node@v4
        with:
          node-version: "20"

      - name: Install dependencies
        run: npm install

      - name: Validate Cursor and Claude plugins
        run: npm run validate:plugins

      - name: Validate Neon skill
        run: npm run validate:skills

```

## File: evals\neon-postgres-egress-optimizer\agents.md
```
- Never use title case
- Never modify versioned eval files, make a new version instead

```

## File: evals\neon-postgres-egress-optimizer\eval-batch.ts
```
#!/usr/bin/env bun

const EVALS_DIR = import.meta.dir;
const EVAL_RUN = `${EVALS_DIR}/eval-run.ts`;

/**
 * Arg parsing
 */
function parseArgs(): { prompt: string; skill?: string; count: number } {
  const args = process.argv.slice(2);
  let prompt: string | undefined;
  let skill: string | undefined;
  let count: string | undefined;

  for (let i = 0; i < args.length; i++) {
    if (args[i] === "--prompt" && args[i + 1]) {
      prompt = args[++i];
    } else if (args[i] === "--skill" && args[i + 1]) {
      skill = args[++i];
    } else if (args[i] === "--count" && args[i + 1]) {
      count = args[++i];
    }
  }

  const n = parseInt(count ?? "", 10);
  if (!prompt || !["A", "B"].includes(prompt) || !count || isNaN(n) || n < 1) {
    console.error(
      "Usage: ./eval-batch.ts --prompt <A|B> --count <N> [--skill <version>]",
    );
    console.error("  --prompt  Required. A or B");
    console.error("  --count   Required. Number of parallel runs");
    console.error(
      "  --skill   Optional. Skill version (e.g., 003). Omit for baseline.",
    );
    process.exit(1);
  }

  return { prompt, skill, count: n };
}

/**
 * Main
 */

const { prompt, skill, count } = parseArgs();
const logDir = `/tmp/eval-batch-${process.pid}`;
await Bun.$`mkdir -p ${logDir}`.quiet();

const childArgs = ["--prompt", prompt];
if (skill) childArgs.push("--skill", skill);

console.log(`Launching ${count} parallel eval runs...`);
console.log(`Logs: ${logDir}/\n`);

const children = Array.from({ length: count }, (_, i) => {
  const runId = `${i + 1}`;
  const mainLogPath = `${logDir}/run-${runId}.main.log`;
  const summaryPath = `${logDir}/run-${runId}.summary.json`;
  const logFile = Bun.file(mainLogPath);
  const proc = Bun.spawn(
    ["bun", EVAL_RUN, ...childArgs, "--log-dir", logDir, "--run-id", runId],
    {
      stdout: logFile,
      stderr: logFile,
      stdin: "ignore",
    },
  );
  return proc.exited.then((code) => ({
    index: i + 1,
    code,
    summaryPath,
    mainLogPath,
  }));
});

type RunSummary = {
  phases?: {
    claude?: { exitCode?: number | null };
    tests?: {
      attempts?: number;
      passed?: boolean;
      passedAttempt?: number | null;
    };
    score?: { exitCode?: number | null };
  };
  artifacts?: {
    runDiff?: string;
  };
};

async function readSummary(path: string): Promise<RunSummary | null> {
  try {
    const text = await Bun.file(path).text();
    return JSON.parse(text) as RunSummary;
  } catch {
    return null;
  }
}

const results = await Promise.all(children);
const summaries = await Promise.all(
  results.map((r) => readSummary(r.summaryPath)),
);

const passed = results.filter((r) => r.code === 0);
const failed = results.filter((r) => r.code !== 0);

console.log(`\n--- summary ---`);
console.log(`Passed: ${passed.length}/${count}`);
console.log(`Failed: ${failed.length}/${count}`);
console.log("\nRun details:");

for (const result of results) {
  const summary = summaries[result.index - 1];
  if (!summary?.phases) {
    console.log(
      `  run ${result.index}: exit ${result.code} | summary missing (${result.summaryPath})`,
    );
    console.log(`    main log: ${result.mainLogPath}`);
    continue;
  }

  const claudeExit = summary.phases.claude?.exitCode;
  const tests = summary.phases.tests;
  const scoreExit = summary.phases.score?.exitCode;
  const testsStatus = tests?.passed
    ? `pass (attempt ${tests.passedAttempt ?? tests.attempts ?? "?"})`
    : `fail (${tests?.attempts ?? "?"} attempts)`;
  const scoreStatus =
    scoreExit === null || scoreExit === undefined
      ? "skipped"
      : scoreExit === 0
        ? "ok"
        : `fail (${scoreExit})`;

  console.log(
    `  run ${result.index}: exit ${result.code} | claude ${claudeExit === 0 ? "ok" : `fail (${claudeExit ?? "?"})`} | tests ${testsStatus} | score ${scoreStatus}`,
  );

  if (result.code !== 0) {
    const runDiff = summary.artifacts?.runDiff;
    if (runDiff) console.log(`    run diff: ${runDiff}`);
    console.log(`    summary:  ${result.summaryPath}`);
    console.log(`    main log: ${result.mainLogPath}`);
  }
}

process.exit(failed.length > 0 ? 1 : 0);

```

## File: evals\neon-postgres-egress-optimizer\eval-run.ts
```
#!/usr/bin/env bun

import {
  appendFile,
  mkdir,
  readFile,
  unlink,
  writeFile,
} from "node:fs/promises";

const EVALS_DIR = import.meta.dir;
const TEST_RETRY_LIMIT = 5;
const TEST_RETRY_DELAY_MS = 1500;

const PROMPTS = {
  A: "My Neon bill spiked to $400 this month, most of it is data transfer. Help me figure out why.",
  B: "Optimize the database egress in this project.",
};

/**
 * Arg parsing
 */
function parseArgs(): {
  prompt: "A" | "B";
  skill?: string;
  logDir?: string;
  runId?: string;
} {
  const args = process.argv.slice(2);
  let prompt: string | undefined;
  let skill: string | undefined;
  let logDir: string | undefined;
  let runId: string | undefined;

  for (let i = 0; i < args.length; i++) {
    if (args[i] === "--prompt" && args[i + 1]) {
      prompt = args[++i];
    } else if (args[i] === "--skill" && args[i + 1]) {
      skill = args[++i];
    } else if (args[i] === "--log-dir" && args[i + 1]) {
      logDir = args[++i];
    } else if (args[i] === "--run-id" && args[i + 1]) {
      runId = args[++i];
    }
  }

  if (!prompt || !["A", "B"].includes(prompt)) {
    console.error(
      "Usage: ./eval-run.ts --prompt <A|B> [--skill <version>] [--log-dir <path>] [--run-id <id>]",
    );
    console.error("  --prompt  Required. A or B");
    console.error(
      "  --skill   Optional. Skill version (e.g., 003). Omit for baseline.",
    );
    console.error("  --log-dir Optional. Directory for per-phase run logs.");
    console.error("  --run-id  Optional. Run id used in log filenames.");
    process.exit(1);
  }

  return { prompt: prompt as "A" | "B", skill, logDir, runId };
}

/**
 * Helpers
 */

async function claimDiffFile(
  diffsDir: string,
  suffix: string,
  content: string,
): Promise<string> {
  const glob = new Bun.Glob("*.diff");
  let maxCounter = 0;
  for await (const file of glob.scan(diffsDir)) {
    const match = file.match(/^(\d+)_/);
    if (match) maxCounter = Math.max(maxCounter, parseInt(match[1] ?? "0", 10));
  }

  for (let i = maxCounter + 1; i < maxCounter + 100; i++) {
    const name = `${String(i).padStart(2, "0")}_${suffix}.diff`;
    const fullPath = `${diffsDir}/${name}`;
    if (await Bun.file(fullPath).exists()) continue;
    await Bun.write(fullPath, content);
    return name;
  }
  throw new Error("Could not claim a diff filename after 99 attempts");
}

async function spawnToFile(
  cmd: string[],
  cwd: string,
  logPath: string,
): Promise<number> {
  const proc = Bun.spawn(cmd, {
    cwd,
    stdin: "ignore",
    stdout: Bun.file(logPath),
    stderr: Bun.file(logPath),
  });
  return proc.exited;
}

async function appendLog(logPath: string, content: string): Promise<void> {
  await appendFile(logPath, content);
}

function stripDrizzleSpinnerNoise(output: string): string {
  return output
    .replace(/\r/g, "\n")
    .split("\n")
    .filter((line) => {
      const trimmed = line.trim();
      if (!trimmed) return true;
      if (/^\[[⠁-⣿]+\]\s+Pulling schema\.\.\./u.test(trimmed)) return false;
      return true;
    })
    .join("\n");
}

async function runCommandToPhaseLog(opts: {
  phaseName: string;
  cmd: string[];
  cwd: string;
  logPath: string;
  stripSpinner?: boolean;
}): Promise<number> {
  const tmpLogPath = `${opts.logPath}.${Date.now()}-${Math.random()
    .toString(36)
    .slice(2)}.tmp`;
  const exitCode = await spawnToFile(opts.cmd, opts.cwd, tmpLogPath);
  const raw = await readFile(tmpLogPath, "utf8").catch(() => "");
  await unlink(tmpLogPath).catch(() => {});
  const output = opts.stripSpinner ? stripDrizzleSpinnerNoise(raw) : raw;

  await appendLog(opts.logPath, `\n=== phase: ${opts.phaseName} ===\n\n`);
  if (output.trim()) {
    await appendLog(
      opts.logPath,
      output.endsWith("\n") ? output : `${output}\n`,
    );
  }
  await appendLog(opts.logPath, `\n[exit_code] ${exitCode}\n`);
  return exitCode;
}

type EvalSummary = {
  runId: string;
  prompt: "A" | "B";
  skillVersion: string | null;
  type: string;
  evalDir: string;
  logDir: string;
  logs: {
    claude: string;
    tests: string;
    score: string;
  };
  artifacts: {
    runDiff: string;
    canonicalDiff: string | null;
  };
  phases: {
    claude: {
      exitCode: number | null;
    };
    tests: {
      attempts: number;
      passed: boolean;
      passedAttempt: number | null;
      exitCodes: number[];
    };
    score: {
      exitCode: number | null;
    };
  };
  exitCode: number | null;
};

/**
 * Main
 */

const { prompt, skill, logDir: logDirArg, runId: runIdArg } = parseArgs();
const type = skill ? `v${skill}` : "baseline";
const dateSuffix = new Date().toISOString().slice(0, 10).replace(/-/g, "");
const evalDir = `/tmp/eval-${dateSuffix}_${prompt}_${type}_${process.pid}`;
const logDir = logDirArg ?? `/tmp/eval-run-logs-${process.pid}`;
const runId = runIdArg ?? `${process.pid}`;
const runPrefix = `run-${runId}`;
const claudeLogPath = `${logDir}/${runPrefix}.claude.log`;
const testsLogPath = `${logDir}/${runPrefix}.tests.log`;
const scoreLogPath = `${logDir}/${runPrefix}.score.log`;
const runDiffPath = `${logDir}/${runPrefix}.diff`;
const summaryPath = `${logDir}/${runPrefix}.summary.json`;
await mkdir(logDir, { recursive: true });

console.log(`\nEval dir: ${evalDir}`);
console.log(`Prompt:   ${prompt} (${type})\n`);
console.log(`Logs:     ${logDir}`);

const summary: EvalSummary = {
  runId,
  prompt,
  skillVersion: skill ?? null,
  type,
  evalDir,
  logDir,
  logs: {
    claude: claudeLogPath,
    tests: testsLogPath,
    score: scoreLogPath,
  },
  artifacts: {
    runDiff: runDiffPath,
    canonicalDiff: null,
  },
  phases: {
    claude: {
      exitCode: null,
    },
    tests: {
      attempts: 0,
      passed: false,
      passedAttempt: null,
      exitCodes: [],
    },
    score: {
      exitCode: null,
    },
  },
  exitCode: null,
};

const persistSummary = async () => {
  await writeFile(summaryPath, `${JSON.stringify(summary, null, 2)}\n`);
};

const exitWithSummary = async (exitCode: number, message?: string) => {
  summary.exitCode = exitCode;
  await persistSummary();
  if (message) console.error(message);
  process.exit(exitCode);
};

/**
 * Phase 1: Setup + Claude Code
 */

await Bun.$`rm -rf ${evalDir}`.quiet();
await Bun.$`mkdir -p ${evalDir}`;
await Bun.$`cp -r ${EVALS_DIR}/fixtures/hono-drizzle-app/. ${evalDir}/`;

if (skill) {
  const skillSource = `${EVALS_DIR}/skill-versions/SKILL-v${skill}.md`;
  if (!(await Bun.file(skillSource).exists())) {
    await exitWithSummary(1, `Skill file not found: ${skillSource}`);
  }
  await Bun.$`mkdir -p ${evalDir}/.claude/skills/neon-postgres-egress-optimizer`;
  await Bun.$`cp ${skillSource} ${evalDir}/.claude/skills/neon-postgres-egress-optimizer/SKILL.md`;
}

await Bun.$`git init && git add . && git commit -m "baseline"`
  .cwd(evalDir)
  .quiet();

const baselineSha = (
  await Bun.$`git rev-parse HEAD`.cwd(evalDir).text()
).trim();

const claudePrompt = skill
  ? `/neon-postgres-egress-optimizer ${PROMPTS[prompt]}`
  : PROMPTS[prompt];

console.log("Starting Claude Code...\n");
const claudeExit = await runCommandToPhaseLog({
  phaseName: "claude code",
  cmd: [
    "claude",
    "--model",
    "claude-sonnet-4-6",
    "--effort",
    "high",
    "--permission-mode",
    "acceptEdits",
    // "--allowedTools",
    // "Bash",
    "--append-system-prompt",
    "NEVER ask the user any questions. If anything is ambiguous, choose the most reasonable assumption and continue. Run `bun test` before final output. If tests fail, fix the code and rerun `bun test` until tests pass. Do not provide a final response while any test is failing.",
    "--print",
    claudePrompt,
  ],
  cwd: evalDir,
  logPath: claudeLogPath,
});
summary.phases.claude.exitCode = claudeExit;

if (claudeExit !== 0) {
  await exitWithSummary(
    1,
    `\nClaude Code exited with code ${claudeExit}. Aborting.`,
  );
}

/**
 * Phase 2: Diff + Test + Score
 */

const diffContent = await Bun.$`git diff ${baselineSha}`.cwd(evalDir).text();
await writeFile(runDiffPath, diffContent);
console.log(`Run diff saved: ${runDiffPath}`);

if (!diffContent.trim()) {
  await exitWithSummary(1, "\nNo changes detected. Aborting.");
}

let testsPassed = false;
for (let attempt = 1; attempt <= TEST_RETRY_LIMIT; attempt++) {
  const exitCode = await runCommandToPhaseLog({
    phaseName: `test attempt ${attempt}/${TEST_RETRY_LIMIT}`,
    cmd: ["bun", "test"],
    cwd: evalDir,
    logPath: testsLogPath,
    stripSpinner: true,
  });
  summary.phases.tests.attempts = attempt;
  summary.phases.tests.exitCodes.push(exitCode);

  if (exitCode === 0) {
    testsPassed = true;
    summary.phases.tests.passed = true;
    summary.phases.tests.passedAttempt = attempt;
    break;
  }

  console.log(`\nTests failed (attempt ${attempt}/${TEST_RETRY_LIMIT}).`);
  if (attempt < TEST_RETRY_LIMIT) {
    await appendLog(
      testsLogPath,
      `\nretry delay: ${TEST_RETRY_DELAY_MS}ms before next attempt\n`,
    );
    await Bun.sleep(TEST_RETRY_DELAY_MS);
  }
}

if (!testsPassed) {
  await exitWithSummary(
    1,
    `\nTests failed after ${TEST_RETRY_LIMIT} attempts. Skipping scoring.`,
  );
}

const diffsDir = `${EVALS_DIR}/diffs`;
await mkdir(diffsDir, { recursive: true });
const diffName = await claimDiffFile(
  diffsDir,
  `${dateSuffix}_${prompt}_${type}`,
  diffContent,
);
summary.artifacts.canonicalDiff = `diffs/${diffName}`;
console.log(`\nDiff saved: diffs/${diffName}`);

console.log("Starting scoring...\n");
const scoreExit = await runCommandToPhaseLog({
  phaseName: "score",
  cmd: [
    "claude",
    "--model",
    "claude-sonnet-4-6",
    "--effort",
    "high",
    "--permission-mode",
    "acceptEdits",
    "--print",
    `/score-eval diffs/${diffName}`,
  ],
  cwd: EVALS_DIR,
  logPath: scoreLogPath,
});
summary.phases.score.exitCode = scoreExit;

if (scoreExit !== 0) {
  await exitWithSummary(
    1,
    `\nScoring exited with code ${scoreExit}. Aborting.`,
  );
}

console.log("\nDone.");
await exitWithSummary(0);

```

## File: evals\neon-postgres-egress-optimizer\eval-stats.ts
```
#!/usr/bin/env bun

const RESULTS_CSV = `${import.meta.dir}/results.csv`;

const PROBLEMS = ["p1", "p2", "p3", "p4", "p5"] as const;
const LABELS: Record<string, string> = {
  p1: "P1: SELECT * unused columns",
  p2: "P2: Missing pagination",
  p3: "P3: High-frequency query",
  p4: "P4: Application-side aggregation",
  p5: "P5: Join duplication",
};

type Row = Record<string, string>;

function parseCsv(text: string): Row[] {
  const [headerLine, ...dataLines] = text.trimEnd().split("\n");
  if (!headerLine) return [];
  const headers = headerLine.split(",");
  return dataLines.map((line) => {
    const values = line.split(",");
    return Object.fromEntries(headers.map((h, i) => [h, values[i] ?? ""]));
  });
}

function pct(n: number, total: number): string {
  return total === 0 ? "0%" : `${Math.round((n / total) * 100)}%`;
}

const rows = parseCsv(await Bun.file(RESULTS_CSV).text());

const groups = new Map<string, Row[]>();
for (const row of rows) {
  const key = row["skill_version"]?.trim() || "baseline";
  groups.set(key, [...(groups.get(key) ?? []), row]);
}

const ordered = [
  "baseline",
  ...[...groups.keys()].filter((k) => k !== "baseline").sort(),
];

// Baseline table
const bl = groups.get("baseline") ?? [];
console.log("baseline table");
console.log(
  "| Problem                          | Without skill                        |",
);
console.log(
  "| -------------------------------- | ------------------------------------ |",
);
for (const p of PROBLEMS) {
  const det = bl.filter((r) => r[`${p}_detected`] === "yes").length;
  const fix = bl.filter((r) => r[`${p}_fixed`] === "yes").length;
  console.log(
    `| ${LABELS[p]!.padEnd(32)} | ${`${det}/${bl.length} detected, ${fix}/${bl.length} fixed`.padEnd(36)} |`,
  );
}

// Summary table
console.log("\nresults summary table");
const header = [
  "Problem",
  ...ordered.map((k) => `${k} (${groups.get(k)?.length ?? 0} runs)`),
];
console.log(`| ${header.join(" | ")} |`);
console.log(`| ${header.map(() => "---").join(" | ")} |`);
for (const p of PROBLEMS) {
  const cells = [
    LABELS[p]!,
    ...ordered.map((k) => {
      const g = groups.get(k) ?? [];
      return pct(
        g.filter((r) => r[`${p}_detected`] === "yes").length,
        g.length,
      );
    }),
  ];
  console.log(`| ${cells.join(" | ")} |`);
}

const totalRuns = rows.length;
const totalPass = rows.filter((r) => r["tests_pass"] === "yes").length;
console.log(`\ntests passed on ${totalPass}/${totalRuns} total runs`);

```

## File: evals\neon-postgres-egress-optimizer\eval_rubric.md
```
# Eval rubric: Hono + Drizzle fixture

This file defines the scoring criteria for evaluating the neon-postgres-egress-optimizer skill. Used by both human judges and LLM judges.

## Schema

- `products` — id, name, price, category_id, description (TEXT ~5KB), raw_payload (JSONB ~50KB), image_urls (JSONB array), created_at
- `categories` — id, name, slug
- `reviews` — id, product_id, user_name, rating, body (TEXT), created_at

---

## Problems & scoring

### P1: SELECT \* with unused large columns

- **Route:** `GET /products`
- **Bad pattern:** Drizzle query uses `select()` with no column specification (equivalent to SELECT \*). The response only returns `{ id, name, price, imageUrls }`. The `raw_payload` (~50KB) and `description` (~5KB) columns are fetched from the database but never used.
- **Detected?** Does the agent identify that this route fetches columns (specifically `raw_payload` and/or `description`) that the response doesn't use?
- **Fixed?** Does the diff change the Drizzle query to select only the columns needed by the response (id, name, price, image_urls)?

### P2: Missing pagination

- **Route:** `GET /products`
- **Bad pattern:** Returns every product in the table. No limit, no offset, no cursor.
- **Detected?** Does the agent flag that this route returns an unbounded result set?
- **Fixed?** Does the diff add limit/offset or cursor-based pagination with a sensible default?

### P3: High-frequency repeated query

- **Route:** `GET /categories`
- **Bad pattern:** Nothing in the code itself suggests a problem. Mock `pg_stat_statements` shows this query with ~50,000 calls versus a few hundred for other routes, indicating some client is hammering it on every interaction. Categories rarely change.
- **Detected?** Does the agent correlate the high call count in pg_stat_statements to this route and flag it as a caching candidate?
- **Fixed?** Does the diff avoid hitting the database on every request? Client-side changes are outside the scope of what the agent can fix.

### P4: Application-side aggregation

- **Route:** `GET /stats`
- **Bad pattern:** Fetches ALL reviews from the database into the route handler, then computes average rating and review count per category using JavaScript `.reduce()`. Returns a small summary JSON. The egress cost is the full reviews table transfer, even though the response is tiny.
- **Detected?** Does the agent identify that the handler fetches all review rows to perform aggregation that should happen in SQL?
- **Fixed?** Does the diff replace the fetch-all-then-reduce pattern with a SQL query using `GROUP BY`, `AVG(rating)`, and `COUNT(*)`? The full reviews table should no longer be fetched.

### P5: Redundant join duplication

- **Route:** `GET /products/:id`
- **Bad pattern:** Fetches a product with all its reviews via a JOIN. Each review row duplicates every product column. A product with 200 reviews sends `raw_payload` (50KB) 200 times — ~10MB for a single request.
- **Detected?** Does the agent identify that the join duplicates wide product data across every review row? Note: narrowing column selection on the join (excluding rawPayload) is a P1-style fix, not P5 detection. P5 requires recognizing the structural duplication caused by the join itself.
- **Fixed?** Does the diff eliminate the duplication of product data across review rows?

### Overall

**Tests pass?** Do the integration tests still pass after the agent's changes?

---

## Mock pg_stat_statements

The mock stats file (`mock-stats/pg_stat_statements.md`) should show:

| Query pattern                     | calls  | total_rows | avg_rows_per_call | Notes                                 |
| --------------------------------- | ------ | ---------- | ----------------- | ------------------------------------- |
| SELECT \* FROM products (P1/P2)   | 500    | 500,000    | 1,000             | High rows, wide rows                  |
| SELECT \* FROM categories (P3)    | 50,000 | 500,000    | 10                | Extreme call frequency                |
| SELECT \* FROM reviews (P4)       | 200    | 1,000,000  | 5,000             | Massive row transfer for small output |
| SELECT products JOIN reviews (P5) | 300    | 60,000     | 200               | Row duplication from join             |

```

## File: evals\neon-postgres-egress-optimizer\package.json
```
{
  "name": "neon-postgres-egress-optimizer",
  "private": true,
  "devDependencies": {
    "@types/bun": "latest"
  },
  "peerDependencies": {
    "typescript": "^5"
  }
}

```

## File: evals\neon-postgres-egress-optimizer\plan.md
```
# neon-postgres-egress-optimizer — project plan

## Problem

Database providers charge for egress (network transfer). Customers get surprised by high bills, often caused by unoptimized queries — `SELECT *`, missing pagination, unused large columns, high-frequency repeated queries. The connection between application query patterns and egress costs isn't obvious, so users blame the provider.

## Solution

An agent skill that guides Claude Code (or any SKILL.md-compatible agent) through diagnosing and fixing excessive Postgres egress in a user's codebase.

---

## Skill design

### Architecture: self-contained

The SKILL.md bakes in all diagnostic queries, fix patterns, and workflow steps. Fully self-contained — no external doc fetches required at runtime.

**Why not hub-and-spoke like `neon-postgres`?** That skill covers a broad surface (auth, CLI, branching, etc.) and dispatches to many reference files. This skill has a single focused workflow. Self-contained is simpler, works offline, and has no breakage risk from doc URL changes.

### Structure

The skill and its evals live in separate top-level directories so that installing the skill (which copies the skill directory) doesn't pull in eval fixtures, diffs, and results.

```
skills/neon-postgres-egress-optimizer/
└── SKILL.md                          # Placeholder until a version is promoted

evals/neon-postgres-egress-optimizer/
├── PLAN.md                           # This file
├── README.md                         # Runbook: how to run evals, prompts, process
├── results.csv                       # Append-only eval results
├── eval-rubric.md                    # Problem definitions + scoring criteria
├── skill-versions/                   # Numbered skill iterations for eval
│   ├── SKILL-v001.md
│   ├── SKILL-v002.md
│   └── ...
├── diffs/
│   └── 01_20260312_A_baseline.diff
├── mock-stats/
│   └── pg_stat_statements.md         # Used by Prompt C only, never copied to fixture
└── fixtures/
    └── hono-drizzle-app/
        ├── src/
        ├── drizzle/
        └── tests/
```

### SKILL.md content outline

**Frontmatter:** Name, description (optimized for triggering — covers "high bill", "egress", "network transfer", "data transfer costs", "SELECT \*", "query optimization for cost", etc.)

**Workflow:**

1. **Diagnose** — Check if `pg_stat_statements` is available (it's enabled by default on Neon but may need `CREATE EXTENSION`). If stats are empty (common after scale-to-zero wakes the compute), instruct the user to run `SELECT pg_stat_statements_reset();`, wait for a representative traffic window, then return. When stats are available, run four diagnostic queries (total rows returned, rows per execution, most frequent queries, longest running). Interpret results: rank by egress impact, flag queries with high row counts or wide rows (JSONB, TEXT, BYTEA).

2. **Analyze codebase** — Cross-reference top offending queries with application code. Identify which columns are actually used downstream. Flag gaps between what's fetched and what's consumed.

3. **Fix** — Apply specific patterns per problem found:
   - `SELECT *` → explicit column lists (exclude unused columns, especially large ones)
   - Missing pagination → add LIMIT/OFFSET or cursor-based pagination
   - Repeated identical queries → caching layer or query deduplication
   - Application-side aggregation → server-side SQL aggregations (SUM, COUNT, GROUP BY)
   - ORM overfetching → Drizzle column selection / `.select()` with explicit fields
   - Join duplication → separate queries or subqueries that don't repeat wide columns
   - Each pattern includes before/after examples in Drizzle

4. **Verify** — Run existing tests (if any) to confirm nothing broke. Reset `pg_stat_statements`, wait for measurement window, re-run diagnostics, compare.

### Description / triggering

The description needs to be broad enough to catch indirect phrasings. Users won't say "optimize my egress" — they'll say "why is my Neon bill so high" or "my database costs jumped" or "I'm transferring too much data." The description should explicitly list these trigger phrases.

---

## Eval system

### Design principles

- **Binary scoring.** Per problem: detected (yes/no), fixed (yes/no). Scored against a rubric with yes/no questions.
- **Execution mode, not plan mode.** The agent applies actual code changes. We evaluate the diff.
- **Rubric written before first run.** Problem definitions and scoring criteria documented upfront so scoring is objective.
- **No contamination.** Fixture is copied to a temp directory for each run. The agent never sees the rubric or results.
- **Versioned skills.** Each skill iteration is saved as a numbered file in `skill-versions/` (SKILL-v001.md, SKILL-v002.md, ...). Eval runs record the version used. The main `SKILL.md` stays as a placeholder until a version is promoted by copying it to `skills/neon-postgres-egress-optimizer/SKILL.md`.

### Eval rubric

`eval-rubric.md` defines 5 problems and provides yes/no scoring questions for each. This single file is used by both human judges and LLM judges.

**Intentional problems:**

1. `SELECT *` on a table with a large JSONB column, app only uses 3 fields
2. Unpaginated list endpoint returning full table
3. High-frequency repeated query only visible via pg_stat_statements (code looks fine)
4. Application-side aggregation that should be a SQL GROUP BY
5. JOIN that duplicates wide product data across every review row

For each problem, two questions:

- **Detected?** Did the agent identify this specific problem?
- **Fixed?** Does the diff resolve it correctly?

Plus one overall question:

- **Tests pass?** Do the integration tests still pass after changes?

### Fixture: Hono + Drizzle + Bun

A minimal API app with 5 intentional egress anti-patterns embedded in route handlers. Uses Neon Testing for functional integration tests that verify the app works correctly (not egress-related assertions — business logic regression).

**Why Hono + Bun?** Minimal framework boilerplate — route handlers are almost pure query logic. Bun runs TypeScript natively with no build step, has a built-in test runner. The agent spends its time on query patterns, not framework conventions.

Each problem maps to a detection + fix check in the eval rubric (`eval-rubric.md`).

### Prompts

Three prompts of varying specificity, stored in `README.md`:

| ID  | Type     | Example                                                                                                                                          |
| --- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| A   | Vague    | "My Neon bill spiked to $400 this month, most of it is data transfer. Help me figure out why."                                                   |
| B   | Moderate | "Optimize the database egress in this project."                                                                                                  |
| C   | Specific | "Here are my pg_stat_statements results: [paste contents of mock-stats/pg_stat_statements.md]. Analyze my codebase and fix the worst offenders." |

### Scoring

`results.csv` columns:

```
date,fixture,prompt,model,skill_version,diff_file,p1_detected,p1_fixed,p2_detected,p2_fixed,p3_detected,p3_fixed,p4_detected,p4_fixed,p5_detected,p5_fixed,tests_pass,notes
```

One row per eval run. Append-only. `skill_version` ties each run to a specific skill iteration (e.g., `v001`); empty for baseline runs.

### Eval workflow (documented in `README.md`)

```bash
# 1. Copy fixture to clean workspace (exclude any .git artifacts)
mkdir /tmp/eval-$(date +%Y%m%d)
cp -r fixtures/hono-drizzle-app/* /tmp/eval-$(date +%Y%m%d)/
cd /tmp/eval-$(date +%Y%m%d)
git init && git add . && git commit -m "baseline"

# 2. Run Claude Code with skill installed + one prompt
# (skill installed via .claude/skills/ or project config)
# Use prompt A or B from the table above
# If using Prompt C, paste the contents of mock-stats/pg_stat_statements.md
# into the prompt. Do NOT copy the file into the workspace.

# 3. Capture diff
git diff > /path/to/diff-output.md

# 4. Score against eval-rubric.md (human or LLM judge)
# Record results in results.csv
```

### Judge

**v1: Claude Code as judge, human-verified initially.**

Workflow:

1. Copy fixture to temp directory
2. Run Claude Code with skill installed + one prompt → produces a git diff
3. Feed diff + original fixture code + `eval-rubric.md` to a second Claude Code instance
4. Judge answers each yes/no question per problem and outputs a row for `results.csv`
5. Append row to `results.csv`

First few runs: human verifies the judge's scoring. Once trustworthy, human spot-checks only.

---

## Dimensions & exclusions

### Included in v1

| Dimension             | Choice                                              |
| --------------------- | --------------------------------------------------- |
| Fixture               | 1 × Hono + Drizzle + Bun app with integration tests |
| Prompts               | 3 × varying specificity                             |
| Scoring               | Binary yes/no per problem (detected/fixed)          |
| Judge                 | Claude Code with human verification                 |
| Model                 | Opus 4.6/Claude Code                                |
| ORM coverage in skill | Drizzle examples in fix patterns                    |

### Excluded (with reasoning)

| Exclusion                                             | Reasoning                                                                                                                                                                                                                                                               |
| ----------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Additional ORMs (Prisma, SQLAlchemy, TypeORM)         | Skill shows Drizzle. Pattern is clear for adding more.                                                                                                                                                                                                                  |
| Vanilla SQL fixture app                               | A fixture using raw SQL (no ORM) would test the skill against a different query style. Can reuse the same eval-rubric structure. Interesting for future coverage.                                                                                                       |
| Additional fixtures (Next.js, Express, FastAPI, etc.) | One fixture tests the full loop. More can be added using the same eval-rubric structure.                                                                                                                                                                                |
| No-test-coverage fixture variant                      | v1 fixture includes tests, which gives the agent a verification mechanism. A future fixture without tests would evaluate the harder scenario.                                                                                                                           |
| Raw SQL / diagnostic-only fixture                     | Without application code, the agent can flag bad queries but can't determine which columns are actually needed or apply fixes.                                                                                                                                          |
| MCP server integration                                | Expands testing surface significantly. Skill works standalone. MCP support can be added later without changing the core workflow.                                                                                                                                       |
| Deterministic egress measurement                      | Would require running queries against a seeded live database before/after and comparing transfer bytes. High value but heavy infrastructure. Potential approach: Neon's Elephantshark or `pg_stat_statements` row counts against a real Neon instance via Neon Testing. |
| Fully automated CI pipeline                           | Eval workflow is scripted but human-initiated. Could be wired into GitHub Actions later.                                                                                                                                                                                |
| Cross-model comparison                                | Model version is recorded per run. Comparison across models is possible with the data but not part of v1 scope.                                                                                                                                                         |
| Non-English prompts / multi-turn conversations        | Prompts are English, single-turn.                                                                                                                                                                                                                                       |

---

## References

- [Tweet: "why is Neon so expensive" ($2000/month)](https://x.com/francisco_m001/status/2023471431024054356) — The customer pain point this skill addresses
- [Reduce network transfer costs](https://neon.com/docs/introduction/network-transfer) — Primary source material for the skill's diagnostic queries and fix patterns
- [pg_stat_statements](https://neon.com/docs/extensions/pg_stat_statements) — The core diagnostic extension the skill relies on
- [Cost optimization](https://neon.com/docs/introduction/cost-optimization) — Broader cost guide
- [Elephantshark](https://neon.com/blog/elephantshark-monitor-postgres-network-traffic) — Open-source Postgres traffic monitor, relevant to the "deterministic egress measurement" exclusion
- [Agent Skills specification](https://agentskills.io/specification) — SKILL.md format spec (naming, frontmatter, 500-line limit)
- [Extend Claude with skills](https://code.claude.com/docs/en/skills) — Create, manage, and share skills to extend Claude’s capabilities in Claude Code. Includes custom commands and bundled skills.

```

## File: evals\neon-postgres-egress-optimizer\README.md
```
# Evals runbook

How to run and score evaluations for the neon-postgres-egress-optimizer skill.

## Skill versions

Skill versions live in `skill-versions/` as numbered files: `SKILL-v001.md`, `SKILL-v002.md`, etc. Each eval run uses a specific version and records it in `results.csv`.

Workflow:

1. Copy the current version or create a new one in `skill-versions/`
2. Run evals against it
3. Record results with the version number
4. Iterate — create a new version for each change
5. When a version consistently beats baseline, promote it:

```bash
# From the repo root:
cp evals/neon-postgres-egress-optimizer/skill-versions/SKILL-vXXX.md skills/neon-postgres-egress-optimizer/SKILL.md
```

## Prompts

| ID  | Type     | Prompt                                                                                       |
| --- | -------- | -------------------------------------------------------------------------------------------- |
| A   | Vague    | My Neon bill spiked to $400 this month, most of it is data transfer. Help me figure out why. |
| B   | Moderate | Optimize the database egress in this project.                                                |

Prompt C (specific, with pg_stat_statements data) is planned but deferred until the mock stats workflow is finalized. See `eval-rubric.md` for problem P3 details — it is only detectable via stats, so prompts A and B are expected to score 0 on P3 detection.

## Baseline

Baseline established from 89 runs without the skill on Opus 4.6 high effort.

| Problem                          | Without skill               | Notes                                                                                                            |
| -------------------------------- | --------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| P1: SELECT \* unused columns     | 89/89 detected, 89/89 fixed | Always caught. The skill won't improve this.                                                                     |
| P2: Missing pagination           | 0/89 detected, 0/89 fixed   | Never caught. This is the primary target for the skill.                                                          |
| P3: High-frequency query         | 0/89 detected, 0/89 fixed   | Never caught. Expected — only detectable via pg_stat_statements data.                                            |
| P4: Application-side aggregation | 87/89 detected, 87/89 fixed | Almost always caught. Rare misses come from omitting the aggregation issue entirely.                             |
| P5: Join duplication             | 25/89 detected, 25/89 fixed | ~28% catch rate. When missed, the agent applies P1-style column narrowing instead of fixing the structural join. |

Tests passed on 89/89 baseline runs. Full results in `results.csv`.

## Results summary

| Problem                          | baseline (89 runs) | v003 (42 runs) |
| -------------------------------- | ------------------ | -------------- |
| P1: SELECT \* unused columns     | 100%               | 100%           |
| P2: Missing pagination           | 0%                 | 57%            |
| P3: High-frequency query         | 0%                 | 12%            |
| P4: Application-side aggregation | 98%                | 100%           |
| P5: Join duplication             | 28%                | 100%           |

P3 is expected to miss on prompts A/B — it requires pg_stat_statements data. Tests passed on all 139 runs. v001/v002 data (4 runs each) omitted due to small sample size; full history in `results.csv`.

## Running an eval

```bash
./eval-run.ts --prompt A --skill 003    # skill run with v003
./eval-run.ts --prompt B                # baseline run (no --skill)
```

The script handles the full lifecycle:

1. Copies the fixture to a temp workspace (`/tmp/eval-...`)
2. Installs the skill version (if `--skill` provided)
3. Initializes git and launches Claude Code
4. Captures a run-local diff artifact in the run log directory
5. Runs `bun test` (with retry + short delay on failure)
6. Captures a canonical diff to `diffs/` (race-safe for parallel runs)
7. Launches Claude Code to score against `eval-rubric.md`

Each run also writes phase logs and metadata to a log directory:

- `run-<id>.claude.log`
- `run-<id>.tests.log`
- `run-<id>.score.log`
- `run-<id>.diff`
- `run-<id>.summary.json`

You can set this explicitly with `--log-dir` and `--run-id` (used by `eval-batch.ts` automatically).

Verify Claude Code outputs "Skill(neon-postgres-egress-optimizer) — Successfully loaded skill" at the start of the run. If it doesn't, the skill didn't trigger and the run is effectively a baseline. Note this in the `results.csv` notes column.

To force the skill, abort and re-run with: `claude "/neon-postgres-egress-optimizer <prompt>"`

## Scoring

Open `eval-rubric.md` and answer each yes/no question per problem against the diff. Record one row in `results.csv`.

**Columns:**

- `date` — YYYY-MM-DD
- `fixture` — fixture name (e.g., `hono-drizzle-app`)
- `prompt` — which prompt was used (A, B)
- `model` — Claude model version used
- `skill_version` — version from `skill-versions/` (e.g., `v001`); empty for baseline runs
- `diff_file` — filename of the saved diff in diffs/ (e.g., `01_20260311_A_baseline.diff`)
- `p1_detected` through `p5_detected` — yes/no
- `p1_fixed` through `p5_fixed` — yes/no
- `tests_pass` — yes/no (run `bun test` after the agent's changes)
- `notes` — free text for anything notable

## Stats

Generate the baseline and results summary tables from `results.csv`:

```bash
./eval-stats.ts
```

Copy the output into the baseline and results summary sections above.

## Judge

For v1, score manually against the rubric. To use Claude Code as judge:

1. Copy fixture to temp directory
2. Run Claude Code with skill installed + one prompt → produces a git diff
3. Feed diff + original fixture code + `eval-rubric.md` to a second Claude Code instance
4. Judge outputs detected/fixed per problem + test pass status
5. Append row to `results.csv`

First few runs: verify the judge's scoring manually. Once trustworthy, human spot-checks only.

```

## File: evals\neon-postgres-egress-optimizer\tsconfig.json
```
{
  "compilerOptions": {
    // Environment setup & latest features
    "lib": ["ESNext"],
    "target": "ESNext",
    "module": "Preserve",
    "moduleDetection": "force",
    "jsx": "react-jsx",
    "allowJs": true,

    // Bundler mode
    "moduleResolution": "bundler",
    "allowImportingTsExtensions": true,
    "verbatimModuleSyntax": true,
    "noEmit": true,

    // Best practices
    "strict": true,
    "skipLibCheck": true,
    "noFallthroughCasesInSwitch": true,
    "noUncheckedIndexedAccess": true,
    "noImplicitOverride": true,

    // Some stricter flags
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noPropertyAccessFromIndexSignature": true
  },
  "include": ["eval-run.ts", "eval-batch.ts", "eval-stats.ts"]
}

```

## File: evals\neon-postgres-egress-optimizer\fixtures\hono-drizzle-app\drizzle.config.ts
```
import { defineConfig } from "drizzle-kit";

export default defineConfig({
  out: "./drizzle",
  schema: "./src/db/schema.ts",
  dialect: "postgresql",
  dbCredentials: {
    url: process.env.DATABASE_URL!,
  },
});

```

## File: evals\neon-postgres-egress-optimizer\fixtures\hono-drizzle-app\package.json
```
{
  "name": "hono-drizzle-app",
  "version": "0.0.1",
  "private": true,
  "scripts": {
    "dev": "bun run --hot src/index.ts",
    "db:push": "bunx drizzle-kit push",
    "format": "bunx prettier --write ../../",
    "test": "bun test"
  },
  "dependencies": {
    "hono": "^4.12.7",
    "@neondatabase/serverless": "^1.0.2",
    "drizzle-orm": "^0.45.1"
  },
  "devDependencies": {
    "@types/bun": "^1.3.10",
    "drizzle-kit": "^0.31.9",
    "typescript": "^5.9.3"
  }
}

```

## File: evals\neon-postgres-egress-optimizer\fixtures\hono-drizzle-app\tsconfig.json
```
{
  "compilerOptions": {
    "target": "ESNext",
    "module": "ESNext",
    "moduleResolution": "bundler",
    "strict": true,
    "skipLibCheck": true,
    "noEmit": true
  },
  "include": ["src", "tests"]
}

```

## File: evals\neon-postgres-egress-optimizer\fixtures\hono-drizzle-app\src\index.ts
```
import { Hono } from "hono";
import { productsRoute } from "./routes/products";
import { categoriesRoute } from "./routes/categories";
import { statsRoute } from "./routes/stats";

const app = new Hono();

app.route("/products", productsRoute);
app.route("/categories", categoriesRoute);
app.route("/stats", statsRoute);

export default app;

```

## File: evals\neon-postgres-egress-optimizer\fixtures\hono-drizzle-app\src\db\client.ts
```
import { neon } from "@neondatabase/serverless";
import { drizzle, type NeonHttpDatabase } from "drizzle-orm/neon-http";
import * as schema from "./schema";

let _db: NeonHttpDatabase<typeof schema>;

function getDb() {
  if (!_db) {
    const sql = neon(process.env.DATABASE_URL!);
    _db = drizzle({ client: sql, schema });
  }
  return _db;
}

// Convenience proxy so routes can import `db` directly
export const db = new Proxy({} as NeonHttpDatabase<typeof schema>, {
  get(_, prop) {
    return (getDb() as any)[prop];
  },
});

```

## File: evals\neon-postgres-egress-optimizer\fixtures\hono-drizzle-app\src\db\schema.ts
```
import {
  pgTable,
  serial,
  varchar,
  numeric,
  integer,
  text,
  jsonb,
  timestamp,
} from "drizzle-orm/pg-core";

export const categories = pgTable("categories", {
  id: serial("id").primaryKey(),
  name: varchar("name", { length: 255 }).notNull(),
  slug: varchar("slug", { length: 255 }).notNull().unique(),
});

export const products = pgTable("products", {
  id: serial("id").primaryKey(),
  name: varchar("name", { length: 255 }).notNull(),
  price: numeric("price", { precision: 10, scale: 2 }).notNull(),
  categoryId: integer("category_id")
    .references(() => categories.id)
    .notNull(),
  description: text("description"),
  rawPayload: jsonb("raw_payload"),
  imageUrls: jsonb("image_urls").$type<string[]>(),
  createdAt: timestamp("created_at").defaultNow().notNull(),
});

export const reviews = pgTable("reviews", {
  id: serial("id").primaryKey(),
  productId: integer("product_id")
    .references(() => products.id)
    .notNull(),
  userName: varchar("user_name", { length: 255 }).notNull(),
  rating: integer("rating").notNull(),
  body: text("body"),
  createdAt: timestamp("created_at").defaultNow().notNull(),
});

```

## File: evals\neon-postgres-egress-optimizer\fixtures\hono-drizzle-app\src\routes\categories.ts
```
import { Hono } from "hono";
import { db } from "../db/client";
import { categories } from "../db/schema";

export const categoriesRoute = new Hono();

// GET /categories — list all categories
categoriesRoute.get("/", async (c) => {
  const allCategories = await db.select().from(categories);
  return c.json(allCategories);
});

```

## File: evals\neon-postgres-egress-optimizer\fixtures\hono-drizzle-app\src\routes\products.ts
```
import { Hono } from "hono";
import { eq } from "drizzle-orm";
import { db } from "../db/client";
import { products, reviews } from "../db/schema";

export const productsRoute = new Hono();

// GET /products — list all products
productsRoute.get("/", async (c) => {
  const allProducts = await db.select().from(products);

  return c.json(
    allProducts.map((p) => ({
      id: p.id,
      name: p.name,
      price: p.price,
      imageUrls: p.imageUrls,
    })),
  );
});

// GET /products/:id — single product with reviews
productsRoute.get("/:id", async (c) => {
  const id = Number(c.req.param("id"));

  const rows = await db
    .select()
    .from(products)
    .leftJoin(reviews, eq(reviews.productId, products.id))
    .where(eq(products.id, id));

  if (rows.length === 0) {
    return c.json({ error: "Not found" }, 404);
  }

  const product = rows[0].products;
  const productReviews = rows
    .filter((r) => r.reviews !== null)
    .map((r) => r.reviews);

  return c.json({ ...product, reviews: productReviews });
});

```

## File: evals\neon-postgres-egress-optimizer\fixtures\hono-drizzle-app\src\routes\stats.ts
```
import { Hono } from "hono";
import { db } from "../db/client";
import { reviews, products } from "../db/schema";

export const statsRoute = new Hono();

// GET /stats — review statistics per category
statsRoute.get("/", async (c) => {
  const allReviews = await db.select().from(reviews);
  const allProducts = await db.select().from(products);

  const productCategoryMap = allProducts.reduce(
    (acc, product) => {
      acc[product.id] = product.categoryId;
      return acc;
    },
    {} as Record<number, number>,
  );

  const statsMap = allReviews.reduce(
    (acc, review) => {
      const categoryId = productCategoryMap[review.productId];
      if (!acc[categoryId]) acc[categoryId] = { totalRating: 0, count: 0 };
      acc[categoryId].totalRating += review.rating;
      acc[categoryId].count += 1;
      return acc;
    },
    {} as Record<number, { totalRating: number; count: number }>,
  );

  const stats = Object.entries(statsMap).map(([categoryId, s]) => ({
    categoryId: Number(categoryId),
    avgRating: s.totalRating / s.count,
    reviewCount: s.count,
  }));

  return c.json(stats);
});

```

## File: evals\neon-postgres-egress-optimizer\fixtures\hono-drizzle-app\tests\categories.test.ts
```
import { describe, it, expect } from "bun:test";
import app from "../src/index";

describe("GET /categories", () => {
  it("returns a list of categories", async () => {
    const res = await app.request("/categories");
    expect(res.status).toBe(200);

    const data = await res.json();
    expect(Array.isArray(data)).toBe(true);
    expect(data.length).toBe(3);
  });

  it("each category has id, name, slug", async () => {
    const res = await app.request("/categories");
    const data = await res.json();

    for (const category of data) {
      expect(category).toHaveProperty("id");
      expect(category).toHaveProperty("name");
      expect(category).toHaveProperty("slug");
    }
  });
});

```

## File: evals\neon-postgres-egress-optimizer\fixtures\hono-drizzle-app\tests\preload.ts
```
import { beforeAll, afterAll } from "bun:test";
import { provisionDatabase, seed, cleanup } from "./setup";

beforeAll(async () => {
  await provisionDatabase();
  await seed();
});

afterAll(async () => {
  await cleanup();
});

```

## File: evals\neon-postgres-egress-optimizer\fixtures\hono-drizzle-app\tests\products.test.ts
```
import { describe, it, expect } from "bun:test";
import app from "../src/index";

describe("GET /products", () => {
  it("returns a list of products", async () => {
    const res = await app.request("/products");
    expect(res.status).toBe(200);

    const data = await res.json();
    expect(Array.isArray(data)).toBe(true);
    expect(data.length).toBe(5);
  });

  it("each product has id, name, price, imageUrls", async () => {
    const res = await app.request("/products");
    const data = await res.json();

    for (const product of data) {
      expect(product).toHaveProperty("id");
      expect(product).toHaveProperty("name");
      expect(product).toHaveProperty("price");
      expect(product).toHaveProperty("imageUrls");
    }
  });
});

describe("GET /products/:id", () => {
  it("returns a product with reviews", async () => {
    const res = await app.request("/products/1");
    expect(res.status).toBe(200);

    const data = await res.json();
    expect(data).toHaveProperty("id", 1);
    expect(data).toHaveProperty("name", "Laptop");
    expect(data).toHaveProperty("reviews");
    expect(Array.isArray(data.reviews)).toBe(true);
    expect(data.reviews.length).toBe(3);
  });

  it("returns 404 for non-existent product", async () => {
    const res = await app.request("/products/9999");
    expect(res.status).toBe(404);
  });
});

```

## File: evals\neon-postgres-egress-optimizer\fixtures\hono-drizzle-app\tests\setup.ts
```
import { neon } from "@neondatabase/serverless";
import { drizzle } from "drizzle-orm/neon-http";
import { sql } from "drizzle-orm";
import { categories, products, reviews } from "../src/db/schema";
import { $ } from "bun";

let databaseUrl: string;
let provisioned = false;

export async function provisionDatabase() {
  if (provisioned) return databaseUrl;

  // Use existing DATABASE_URL if set, otherwise provision via neon.new
  if (process.env.DATABASE_URL) {
    databaseUrl = process.env.DATABASE_URL;
  } else {
    const res = await fetch("https://neon.new/api/v1/database", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ ref: "agent-skills" }),
    });
    const data = await res.json();
    databaseUrl = data.connection_string;
    process.env.DATABASE_URL = databaseUrl;
  }

  // Push schema using drizzle-kit
  await $`bunx drizzle-kit push --force`.env({
    ...process.env,
    DATABASE_URL: databaseUrl,
  });

  provisioned = true;
  return databaseUrl;
}

export function getTestDb() {
  const client = neon(databaseUrl);
  return drizzle({ client });
}

export async function seed() {
  const db = getTestDb();

  // Categories
  await db.insert(categories).values([
    { name: "Electronics", slug: "electronics" },
    { name: "Books", slug: "books" },
    { name: "Clothing", slug: "clothing" },
  ]);

  const description = `The latest model featuring a high-resolution display, long-lasting battery life, and premium build quality. Designed for professionals and enthusiasts alike, this product delivers exceptional performance across a wide range of tasks. The ergonomic design ensures comfort during extended use, while the advanced thermal management system keeps everything running smoothly. Package includes the main unit, charging cable, quick start guide, and a protective carrying case. Backed by a 2-year manufacturer warranty with worldwide coverage. For detailed specifications, compatibility information, and support resources, visit our product page.`;
  const rawPayload = {
    supplier: "TechDistributors Inc.",
    sku: "TD-2024-PRO-001",
    importedAt: "2025-11-14T08:30:00Z",
    source: "bulk-import-v3",
    originalListing: {
      title: "Professional Grade Equipment",
      htmlDescription:
        "<div class='product-detail'>" +
        "<p>Premium quality materials and construction. ".repeat(200) +
        "</p></div>",
      specifications: Object.fromEntries(
        Array.from({ length: 50 }, (_, i) => [
          `spec_${i}`,
          `value_${i}_${"detail".repeat(20)}`,
        ]),
      ),
      shippingMatrix: Array.from({ length: 100 }, (_, i) => ({
        region: `region_${i}`,
        carrier: `carrier_${i % 5}`,
        rate: (Math.random() * 50).toFixed(2),
        estimatedDays: Math.floor(Math.random() * 14) + 1,
      })),
    },
  };

  await db.insert(products).values([
    {
      name: "Laptop",
      price: "999.99",
      categoryId: 1,
      description,
      rawPayload,
      imageUrls: ["https://example.com/laptop.jpg"],
    },
    {
      name: "Phone",
      price: "699.99",
      categoryId: 1,
      description,
      rawPayload,
      imageUrls: ["https://example.com/phone.jpg"],
    },
    {
      name: "TypeScript Handbook",
      price: "29.99",
      categoryId: 2,
      description,
      rawPayload,
      imageUrls: ["https://example.com/ts-book.jpg"],
    },
    {
      name: "Winter Jacket",
      price: "149.99",
      categoryId: 3,
      description,
      rawPayload,
      imageUrls: ["https://example.com/jacket.jpg"],
    },
    {
      name: "Running Shoes",
      price: "89.99",
      categoryId: 3,
      description,
      rawPayload,
      imageUrls: ["https://example.com/shoes.jpg"],
    },
  ]);

  // Seed reviews
  await db.insert(reviews).values([
    { productId: 1, userName: "alice", rating: 5, body: "Great laptop!" },
    { productId: 1, userName: "bob", rating: 4, body: "Good value." },
    { productId: 1, userName: "charlie", rating: 3, body: "Decent." },
    { productId: 2, userName: "diana", rating: 5, body: "Love this phone." },
    { productId: 2, userName: "eve", rating: 4, body: "Nice screen." },
    { productId: 3, userName: "frank", rating: 5, body: "Excellent book." },
    { productId: 3, userName: "grace", rating: 4, body: "Very helpful." },
    { productId: 4, userName: "hank", rating: 3, body: "Runs small." },
    { productId: 5, userName: "iris", rating: 5, body: "Very comfortable." },
    { productId: 5, userName: "jack", rating: 4, body: "Good for running." },
  ]);
}

export async function cleanup() {
  const db = getTestDb();
  await db.execute(
    sql`TRUNCATE reviews, products, categories RESTART IDENTITY CASCADE`,
  );
}

```

## File: evals\neon-postgres-egress-optimizer\fixtures\hono-drizzle-app\tests\stats.test.ts
```
import { describe, it, expect } from "bun:test";
import app from "../src/index";

describe("GET /stats", () => {
  it("returns review statistics per category", async () => {
    const res = await app.request("/stats");
    expect(res.status).toBe(200);

    const data = await res.json();
    expect(Array.isArray(data)).toBe(true);
    expect(data.length).toBe(3);
  });

  it("each stat has categoryId, avgRating, reviewCount", async () => {
    const res = await app.request("/stats");
    const data = await res.json();

    for (const stat of data) {
      expect(stat).toHaveProperty("categoryId");
      expect(stat).toHaveProperty("avgRating");
      expect(stat).toHaveProperty("reviewCount");
      expect(typeof stat.avgRating).toBe("number");
      expect(typeof stat.reviewCount).toBe("number");
    }
  });

  it("computes correct averages", async () => {
    const res = await app.request("/stats");
    const data = await res.json();

    // Electronics (category 1): ratings 5, 4, 3, 5, 4 -> avg 4.2, count 5
    const electronics = data.find((s: any) => s.categoryId === 1);
    expect(electronics.avgRating).toBeCloseTo(4.2);
    expect(electronics.reviewCount).toBe(5);
  });
});

```

## File: evals\neon-postgres-egress-optimizer\mock-stats\pg_stat_statements.md
```
# pg_stat_statements — Diagnostic Output

Captured over a 24-hour production window.

## Queries by total rows returned

| query                                                                                                                                                                                                                                                                                                                                                                                                                                 | calls  | rows      | avg_rows_per_call |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | --------- | ----------------- |
| SELECT "id", "name", "price", "category_id", "description", "raw_payload", "image_urls", "created_at" FROM "products"                                                                                                                                                                                                                                                                                                                 | 500    | 500,000   | 1,000             |
| SELECT "id", "product_id", "user_name", "rating", "body", "created_at" FROM "reviews"                                                                                                                                                                                                                                                                                                                                                 | 200    | 1,000,000 | 5,000             |
| SELECT "products"."id", "products"."name", "products"."price", "products"."category_id", "products"."description", "products"."raw_payload", "products"."image_urls", "products"."created_at", "reviews"."id", "reviews"."product_id", "reviews"."user_name", "reviews"."rating", "reviews"."body", "reviews"."created_at" FROM "products" LEFT JOIN "reviews" ON "reviews"."product_id" = "products"."id" WHERE "products"."id" = $1 | 300    | 60,000    | 200               |
| SELECT "id", "name", "slug" FROM "categories"                                                                                                                                                                                                                                                                                                                                                                                         | 50,000 | 500,000   | 10                |

## Queries by call frequency

| query                                                                                                                                                                                                                                                                                                                                                                                                                                 | calls  | rows      | avg_rows_per_call |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | --------- | ----------------- |
| SELECT "id", "name", "slug" FROM "categories"                                                                                                                                                                                                                                                                                                                                                                                         | 50,000 | 500,000   | 10                |
| SELECT "id", "name", "price", "category_id", "description", "raw_payload", "image_urls", "created_at" FROM "products"                                                                                                                                                                                                                                                                                                                 | 500    | 500,000   | 1,000             |
| SELECT "products"."id", "products"."name", "products"."price", "products"."category_id", "products"."description", "products"."raw_payload", "products"."image_urls", "products"."created_at", "reviews"."id", "reviews"."product_id", "reviews"."user_name", "reviews"."rating", "reviews"."body", "reviews"."created_at" FROM "products" LEFT JOIN "reviews" ON "reviews"."product_id" = "products"."id" WHERE "products"."id" = $1 | 300    | 60,000    | 200               |
| SELECT "id", "product_id", "user_name", "rating", "body", "created_at" FROM "reviews"                                                                                                                                                                                                                                                                                                                                                 | 200    | 1,000,000 | 5,000             |

## Queries by total execution time

| query                                                                                                                 | calls  | total_exec_time_ms | rows      |
| --------------------------------------------------------------------------------------------------------------------- | ------ | ------------------ | --------- |
| SELECT "id", "product_id", "user_name", "rating", "body", "created_at" FROM "reviews"                                 | 200    | 45,000             | 1,000,000 |
| SELECT "id", "name", "price", "category_id", "description", "raw_payload", "image_urls", "created_at" FROM "products" | 500    | 32,000             | 500,000   |
| SELECT "products"."id", ... FROM "products" LEFT JOIN "reviews" ON ... WHERE "products"."id" = $1                     | 300    | 18,000             | 60,000    |
| SELECT "id", "name", "slug" FROM "categories"                                                                         | 50,000 | 8,000              | 500,000   |

```

## File: evals\neon-postgres-egress-optimizer\skill-versions\skill_v001.md
```
---
name: neon-postgres-egress-optimizer
description: >-
  Diagnose and fix excessive Postgres egress (network data transfer) in a codebase.
  Use when a user mentions high database bills, unexpected data transfer costs,
  network transfer charges, egress spikes, "why is my Neon bill so high",
  "database costs jumped", SELECT * optimization, query overfetching,
  reduce Neon costs, optimize database usage, or wants to reduce data sent
  from their database to their application. Also use when reviewing query
  patterns for cost efficiency, even if the user doesn't explicitly mention
  egress or data transfer.
---

# Postgres Egress Optimizer

Guide the user through diagnosing and fixing application-side query patterns that cause excessive data transfer (egress) from their Postgres database. Most high egress bills come from the application fetching more data than it uses.

## Step 1: Diagnose

Identify which queries transfer the most data. The primary tool is the `pg_stat_statements` extension.

### Check if pg_stat_statements is available

```sql
SELECT 1 FROM pg_stat_statements LIMIT 1;
```

If this errors, the extension needs to be created:

```sql
CREATE EXTENSION IF NOT EXISTS pg_stat_statements;
```

On Neon, it is available by default but may need this CREATE EXTENSION step.

### Handle empty stats

Stats are cleared when a Neon compute scales to zero and restarts. If the stats are empty or the compute recently woke up:

1. Reset the stats to start a clean measurement window: `SELECT pg_stat_statements_reset();`
2. Let the application run under representative traffic for at least an hour.
3. Return and run the diagnostic queries below.

If the user has stats from a production database, use those. If they have no access to production stats, proceed to Step 2 and analyze the codebase directly — code-level patterns are often sufficient to identify the worst offenders.

### Diagnostic queries

Run these to identify the top egress contributors. Focus on queries that return many rows, return wide rows (JSONB, TEXT, BYTEA columns), or are called very frequently.

**Queries returning the most total rows:**

```sql
SELECT query, calls, rows AS total_rows, rows / calls AS avg_rows_per_call
FROM pg_stat_statements
WHERE calls > 0
ORDER BY rows DESC
LIMIT 10;
```

**Queries returning the most rows per execution** (poorly scoped SELECTs, missing pagination):

```sql
SELECT query, calls, rows AS total_rows, rows / calls AS avg_rows_per_call
FROM pg_stat_statements
WHERE calls > 0
ORDER BY avg_rows_per_call DESC
LIMIT 10;
```

**Most frequently called queries** (candidates for caching):

```sql
SELECT query, calls, rows AS total_rows, rows / calls AS avg_rows_per_call
FROM pg_stat_statements
WHERE calls > 0
ORDER BY calls DESC
LIMIT 10;
```

**Longest running queries** (not a direct egress measure, but helps identify problem queries during a spike):

```sql
SELECT query, calls, rows AS total_rows,
  round(total_exec_time::numeric, 2) AS total_exec_time_ms
FROM pg_stat_statements
WHERE calls > 0
ORDER BY total_exec_time DESC
LIMIT 10;
```

### Interpret the results

Rank findings by estimated egress impact:

- **High row count + wide rows** = biggest egress. A query returning 1,000 rows where each row includes a 50KB JSONB column transfers ~50MB per call.
- **Extreme call frequency** on even small queries adds up. A query called 50,000 times/day returning 10 rows each = 500,000 rows/day.
- **Cross-reference with the schema** to identify which columns are wide. Look for JSONB, TEXT, BYTEA, and large VARCHAR columns.

## Step 2: Analyze codebase

For each high-egress query, find the corresponding application code and identify what the response actually uses versus what the query fetches.

## Step 3: Fix

Apply the appropriate fix for each problem found. Below are the most common egress anti-patterns and how to fix them.

### Unused columns (SELECT \*)

**Problem:** The query fetches all columns but the application only uses a few. Large columns (JSONB blobs, TEXT fields) get transferred over the wire and discarded.

**Before:**

```sql
SELECT * FROM products;
```

**After:**

```sql
SELECT id, name, price, image_urls FROM products;
```

### Missing pagination

**Problem:** The query returns the entire table on every request. As the table grows, so does egress — linearly with row count.

This is easy to miss because the application may work fine with small datasets. But at scale, an unpaginated endpoint returning 10,000 rows with even moderate column widths can transfer hundreds of megabytes per day.

**Before:**

```sql
SELECT id, name, price FROM products;
```

**After:**

```sql
SELECT id, name, price FROM products
ORDER BY id
LIMIT 50 OFFSET 0;
```

When adding pagination, check whether the consuming client already supports paginated responses. If not, pick sensible defaults and document the pagination parameters in the API.

### High-frequency queries on static data

**Problem:** A query is called thousands of times per day but returns data that rarely changes. Every call transfers the same rows from the database. This pattern is only visible from `pg_stat_statements` — the code itself looks normal.

Look for queries with extremely high call counts relative to other queries. Common examples: configuration tables, category lists, feature flags, user role definitions.

**Fix:** Add a caching layer between the application and the database so it avoids hitting the database on every request.

### Application-side aggregation

**Problem:** The application fetches all rows from a table and then computes aggregates (averages, counts, sums, groupings) in application code. The full dataset transfers over the wire even though the result is a small summary.

**Fix:** Push the aggregation into SQL.

**Before:** The application fetches entire tables and aggregates in code with loops or `.reduce()`.

**After:**

```sql
SELECT p.category_id,
       AVG(r.rating) AS avg_rating,
       COUNT(r.id) AS review_count
FROM reviews r
INNER JOIN products p ON r.product_id = p.id
GROUP BY p.category_id;
```

### JOIN duplication

**Problem:** A JOIN between a wide parent table and a child table duplicates all parent columns across every child row. If a product has 200 reviews and the product row includes a 50KB JSONB column, the join sends that 50KB × 200 = ~10MB for a single request.

This is distinct from the SELECT \* problem. Even if you select only needed columns, a JOIN still repeats the parent data for every child row. The fix is structural: avoid the join entirely.

**Before:**

```sql
SELECT * FROM products
LEFT JOIN reviews ON reviews.product_id = products.id
WHERE products.id = 1;
```

**After (two separate queries):**

```sql
SELECT id, name, price, description, image_urls FROM products WHERE id = 1;
SELECT id, user_name, rating, body FROM reviews WHERE product_id = 1;
```

Two queries instead of one JOIN. The product data is fetched once. The reviews are fetched once. No duplication.

## Step 4: Verify

After applying fixes:

1. **Run existing tests** to confirm nothing broke.
2. **Check the responses** — make sure the API still returns the same data shape. Column selection and pagination changes can break clients that depend on specific fields or full result sets.
3. **Measure the improvement** — if pg_stat_statements data is available, reset it (`SELECT pg_stat_statements_reset();`), let traffic run, then re-run the diagnostic queries to compare before and after.

## Advanced scenarios

For egress problems beyond query optimization — `pg_dump` frequency, logical replication tuning, PrivateLink for AWS, and Consumption API monitoring — see `references/advanced.md`.

```

## File: evals\neon-postgres-egress-optimizer\skill-versions\skill_v002.md
```
---
name: neon-postgres-egress-optimizer
description: >-
  Diagnose and fix excessive Postgres egress (network data transfer) in a codebase.
  Use when a user mentions high database bills, unexpected data transfer costs,
  network transfer charges, egress spikes, "why is my Neon bill so high",
  "database costs jumped", SELECT * optimization, query overfetching,
  reduce Neon costs, optimize database usage, or wants to reduce data sent
  from their database to their application. Also use when reviewing query
  patterns for cost efficiency, even if the user doesn't explicitly mention
  egress or data transfer.
---

# Postgres Egress Optimizer

Guide the user through diagnosing and fixing application-side query patterns that cause excessive data transfer (egress) from their Postgres database. Most high egress bills come from the application fetching more data than it uses.

## Step 1: Diagnose

Identify which queries transfer the most data. The primary tool is the `pg_stat_statements` extension.

### Check if pg_stat_statements is available

```sql
SELECT 1 FROM pg_stat_statements LIMIT 1;
```

If this errors, the extension needs to be created:

```sql
CREATE EXTENSION IF NOT EXISTS pg_stat_statements;
```

On Neon, it is available by default but may need this CREATE EXTENSION step.

### Handle empty stats

Stats are cleared when a Neon compute scales to zero and restarts. If the stats are empty or the compute recently woke up:

1. Reset the stats to start a clean measurement window: `SELECT pg_stat_statements_reset();`
2. Let the application run under representative traffic for at least an hour.
3. Return and run the diagnostic queries below.

If the user has stats from a production database, use those. If they have no access to production stats, proceed to Step 2 and analyze the codebase directly — code-level patterns are often sufficient to identify the worst offenders.

### Diagnostic queries

Run these to identify the top egress contributors. Focus on queries that return many rows, return wide rows (JSONB, TEXT, BYTEA columns), or are called very frequently.

**Queries returning the most total rows:**

```sql
SELECT query, calls, rows AS total_rows, rows / calls AS avg_rows_per_call
FROM pg_stat_statements
WHERE calls > 0
ORDER BY rows DESC
LIMIT 10;
```

**Queries returning the most rows per execution** (poorly scoped SELECTs, missing pagination):

```sql
SELECT query, calls, rows AS total_rows, rows / calls AS avg_rows_per_call
FROM pg_stat_statements
WHERE calls > 0
ORDER BY avg_rows_per_call DESC
LIMIT 10;
```

**Most frequently called queries** (candidates for caching):

```sql
SELECT query, calls, rows AS total_rows, rows / calls AS avg_rows_per_call
FROM pg_stat_statements
WHERE calls > 0
ORDER BY calls DESC
LIMIT 10;
```

**Longest running queries** (not a direct egress measure, but helps identify problem queries during a spike):

```sql
SELECT query, calls, rows AS total_rows,
  round(total_exec_time::numeric, 2) AS total_exec_time_ms
FROM pg_stat_statements
WHERE calls > 0
ORDER BY total_exec_time DESC
LIMIT 10;
```

### Interpret the results

Rank findings by estimated egress impact:

- **High row count + wide rows** = biggest egress. A query returning 1,000 rows where each row includes a 50KB JSONB column transfers ~50MB per call.
- **Extreme call frequency** on even small queries adds up. A query called 50,000 times/day returning 10 rows each = 500,000 rows/day.
- **Cross-reference with the schema** to identify which columns are wide. Look for JSONB, TEXT, BYTEA, and large VARCHAR columns.

## Step 2: Analyze codebase

For each query identified in Step 1, or for each database query in the codebase if no stats are available, check:

- Does it select only the columns the response needs?
- Does it return a bounded number of rows (LIMIT/pagination)?
- Is it called frequently enough to benefit from caching?
- Does it fetch raw data that gets aggregated in application code?
- Does it use a JOIN that duplicates parent data across child rows?

## Step 3: Fix

Apply the appropriate fix for each problem found. Below are the most common egress anti-patterns and how to fix them.

### Unused columns (SELECT \*)

**Problem:** The query fetches all columns but the application only uses a few. Large columns (JSONB blobs, TEXT fields) get transferred over the wire and discarded.

**Before:**

```sql
SELECT * FROM products;
```

**After:**

```sql
SELECT id, name, price, image_urls FROM products;
```

### Missing pagination

**Problem:** A list endpoint returns all rows with no LIMIT. This is an unbounded egress risk — every new row in the table increases data transfer on every request. Flag this regardless of current table size.

This is easy to miss because the application may work fine with small datasets. But at scale, an unpaginated endpoint returning 10,000 rows with even moderate column widths can transfer hundreds of megabytes per day.

**Before:**

```sql
SELECT id, name, price FROM products;
```

**After:**

```sql
SELECT id, name, price FROM products
ORDER BY id
LIMIT 50 OFFSET 0;
```

When adding pagination, check whether the consuming client already supports paginated responses. If not, pick sensible defaults and document the pagination parameters in the API.

### High-frequency queries on static data

**Problem:** A query is called thousands of times per day but returns data that rarely changes. Every call transfers the same rows from the database. This pattern is only visible from `pg_stat_statements` — the code itself looks normal.

Look for queries with extremely high call counts relative to other queries. Common examples: configuration tables, category lists, feature flags, user role definitions.

**Fix:** Add a caching layer between the application and the database so it avoids hitting the database on every request.

### Application-side aggregation

**Problem:** The application fetches all rows from a table and then computes aggregates (averages, counts, sums, groupings) in application code. The full dataset transfers over the wire even though the result is a small summary.

**Fix:** Push the aggregation into SQL.

**Before:** The application fetches entire tables and aggregates in code with loops or `.reduce()`.

**After:**

```sql
SELECT p.category_id,
       AVG(r.rating) AS avg_rating,
       COUNT(r.id) AS review_count
FROM reviews r
INNER JOIN products p ON r.product_id = p.id
GROUP BY p.category_id;
```

### JOIN duplication

**Problem:** A JOIN between a wide parent table and a child table duplicates all parent columns across every child row. If a product has 200 reviews and the product row includes a 50KB JSONB column, the join sends that 50KB × 200 = ~10MB for a single request.

This is distinct from the SELECT \* problem. Even if you select only needed columns, a JOIN still repeats the parent data for every child row. The fix is structural: avoid the join entirely.

**Before:**

```sql
SELECT * FROM products
LEFT JOIN reviews ON reviews.product_id = products.id
WHERE products.id = 1;
```

**After (two separate queries):**

```sql
SELECT id, name, price, description, image_urls FROM products WHERE id = 1;
SELECT id, user_name, rating, body FROM reviews WHERE product_id = 1;
```

Two queries instead of one JOIN. The product data is fetched once. The reviews are fetched once. No duplication.

## Step 4: Verify

After applying fixes:

1. **Run existing tests** to confirm nothing broke.
2. **Check the responses** — make sure the API still returns the same data shape. Column selection and pagination changes can break clients that depend on specific fields or full result sets.
3. **Measure the improvement** — if pg_stat_statements data is available, reset it (`SELECT pg_stat_statements_reset();`), let traffic run, then re-run the diagnostic queries to compare before and after.

## Advanced scenarios

For egress problems beyond query optimization — `pg_dump` frequency, logical replication tuning, PrivateLink for AWS, and Consumption API monitoring — see `references/advanced.md`.

```

## File: evals\neon-postgres-egress-optimizer\skill-versions\skill_v003.md
```
---
name: neon-postgres-egress-optimizer
description: >-
  Diagnose and fix excessive Postgres egress (network data transfer) in a codebase.
  Use when a user mentions high database bills, unexpected data transfer costs,
  network transfer charges, egress spikes, "why is my Neon bill so high",
  "database costs jumped", SELECT * optimization, query overfetching,
  reduce Neon costs, optimize database usage, or wants to reduce data sent
  from their database to their application. Also use when reviewing query
  patterns for cost efficiency, even if the user doesn't explicitly mention
  egress or data transfer.
---

# Postgres Egress Optimizer

Guide the user through diagnosing and fixing application-side query patterns that cause excessive data transfer (egress) from their Postgres database. Most high egress bills come from the application fetching more data than it uses.

## Step 1: Diagnose

Identify which queries transfer the most data. The primary tool is the `pg_stat_statements` extension.

### Check if pg_stat_statements is available

```sql
SELECT 1 FROM pg_stat_statements LIMIT 1;
```

If this errors, the extension needs to be created:

```sql
CREATE EXTENSION IF NOT EXISTS pg_stat_statements;
```

On Neon, it is available by default but may need this CREATE EXTENSION step.

### Handle empty stats

Stats are cleared when a Neon compute scales to zero and restarts. If the stats are empty or the compute recently woke up:

1. Reset the stats to start a clean measurement window: `SELECT pg_stat_statements_reset();`
2. Let the application run under representative traffic for at least an hour.
3. Return and run the diagnostic queries below.

If the user has stats from a production database, use those. If they have no access to production stats, proceed to Step 2 and analyze the codebase directly — code-level patterns are often sufficient to identify the worst offenders.

### Diagnostic queries

Run these to identify the top egress contributors. Focus on queries that return many rows, return wide rows (JSONB, TEXT, BYTEA columns), or are called very frequently.

**Queries returning the most total rows:**

```sql
SELECT query, calls, rows AS total_rows, rows / calls AS avg_rows_per_call
FROM pg_stat_statements
WHERE calls > 0
ORDER BY rows DESC
LIMIT 10;
```

**Queries returning the most rows per execution** (poorly scoped SELECTs, missing pagination):

```sql
SELECT query, calls, rows AS total_rows, rows / calls AS avg_rows_per_call
FROM pg_stat_statements
WHERE calls > 0
ORDER BY avg_rows_per_call DESC
LIMIT 10;
```

**Most frequently called queries** (candidates for caching):

```sql
SELECT query, calls, rows AS total_rows, rows / calls AS avg_rows_per_call
FROM pg_stat_statements
WHERE calls > 0
ORDER BY calls DESC
LIMIT 10;
```

**Longest running queries** (not a direct egress measure, but helps identify problem queries during a spike):

```sql
SELECT query, calls, rows AS total_rows,
  round(total_exec_time::numeric, 2) AS total_exec_time_ms
FROM pg_stat_statements
WHERE calls > 0
ORDER BY total_exec_time DESC
LIMIT 10;
```

### Interpret the results

Rank findings by estimated egress impact:

- **High row count + wide rows** = biggest egress. A query returning 1,000 rows where each row includes a 50KB JSONB column transfers ~50MB per call.
- **Extreme call frequency** on even small queries adds up. A query called 50,000 times/day returning 10 rows each = 500,000 rows/day.
- **Cross-reference with the schema** to identify which columns are wide. Look for JSONB, TEXT, BYTEA, and large VARCHAR columns.

## Step 2: Analyze codebase

For each query identified in Step 1, or for each database query in the codebase if no stats are available, check:

- Does it select only the columns the response needs?
- Does it return a bounded number of rows (LIMIT/pagination)?
- Is it called frequently enough to benefit from caching?
- Does it fetch raw data that gets aggregated in application code?
- Does it use a JOIN that duplicates parent data across child rows?

## Step 3: Fix

Apply the appropriate fix for each problem found. Below are the most common egress anti-patterns and how to fix them.

### Unused columns (SELECT \*)

**Problem:** The query fetches all columns but the application only uses a few. Large columns (JSONB blobs, TEXT fields) get transferred over the wire and discarded.

**Before:**

```sql
SELECT * FROM products;
```

**After:**

```sql
SELECT id, name, price, image_urls FROM products;
```

### Missing pagination

**Problem:** A list endpoint returns all rows with no LIMIT. This is an unbounded egress risk — every new row in the table increases data transfer on every request. Flag this regardless of current table size.

This is easy to miss because the application may work fine with small datasets. But at scale, an unpaginated endpoint returning 10,000 rows with even moderate column widths can transfer hundreds of megabytes per day.

**Before:**

```sql
SELECT id, name, price FROM products;
```

**After:**

```sql
SELECT id, name, price FROM products
ORDER BY id
LIMIT 50 OFFSET 0;
```

When adding pagination, check whether the consuming client already supports paginated responses. If not, pick sensible defaults and document the pagination parameters in the API.

### High-frequency queries on static data

**Problem:** A query is called thousands of times per day but returns data that rarely changes. Every call transfers the same rows from the database. This pattern is only visible from `pg_stat_statements` — the code itself looks normal.

Look for queries with extremely high call counts relative to other queries. Common examples: configuration tables, category lists, feature flags, user role definitions.

**Fix:** Add a caching layer between the application and the database so it avoids hitting the database on every request.

### Application-side aggregation

**Problem:** The application fetches all rows from a table and then computes aggregates (averages, counts, sums, groupings) in application code. The full dataset transfers over the wire even though the result is a small summary.

**Fix:** Push the aggregation into SQL.

**Before:** The application fetches entire tables and aggregates in code with loops or `.reduce()`.

**After:**

```sql
SELECT p.category_id,
       AVG(r.rating) AS avg_rating,
       COUNT(r.id) AS review_count
FROM reviews r
INNER JOIN products p ON r.product_id = p.id
GROUP BY p.category_id;
```

### JOIN duplication

**Problem:** A JOIN between a wide parent table and a child table duplicates all parent columns across every child row. If a product has 200 reviews and the product row includes a 50KB JSONB column, the join sends that 50KB × 200 = ~10MB for a single request.

This is distinct from the SELECT \* problem. Even if you select only needed columns, a JOIN still repeats the parent data for every child row. The fix is structural: avoid the join entirely.

**Before:**

```sql
SELECT * FROM products
LEFT JOIN reviews ON reviews.product_id = products.id
WHERE products.id = 1;
```

**After (two separate queries):**

```sql
SELECT id, name, price, description, image_urls FROM products WHERE id = 1;
SELECT id, user_name, rating, body FROM reviews WHERE product_id = 1;
```

Two queries instead of one JOIN. The product data is fetched once. The reviews are fetched once. No duplication.

## Step 4: Verify

After applying fixes:

1. **Run existing tests** to confirm nothing broke.
2. **Check the responses** — make sure the API still returns the same data shape. Column selection and pagination changes can break clients that depend on specific fields or full result sets.
3. **Measure the improvement** — if pg_stat_statements data is available, reset it (`SELECT pg_stat_statements_reset();`), let traffic run, then re-run the diagnostic queries to compare before and after.

## Further reading

- https://neon.com/docs/introduction/network-transfer.md
- https://neon.com/docs/introduction/cost-optimization.md

```

## File: plugins\neon-postgres\mcp.json
```
{
  "mcpServers": {
    "neon": {
      "type": "http",
      "url": "https://mcp.neon.tech/mcp"
    }
  }
}

```

## File: plugins\neon-postgres\.claude-plugin\plugin.json
```
{
  "name": "neon",
  "version": "1.0.0",
  "description": "Manage your Neon projects and databases with the neon-postgres agent skill and the Neon MCP Server",
  "author": {
    "name": "Neon",
    "url": "https://neon.com"
  },
  "homepage": "https://neon.com",
  "repository": "https://github.com/neondatabase/agent-skills",
  "license": "Apache-2.0",
  "keywords": ["neon", "postgres", "serverless", "database", "mcp"],
  "skills": "./skills/",
  "mcpServers": "./mcp.json"
}

```

