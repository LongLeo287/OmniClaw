---
id: github.com-supabase-agent-skills-7545b4c4-knowledg
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:24.880901
---

# KNOWLEDGE EXTRACT: github.com_supabase_agent-skills_7545b4c4
> **Extracted on:** 2026-04-01 09:59:24
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007520540/github.com_supabase_agent-skills_7545b4c4

---

## File: `.gitignore`
```
node_modules/
dist/
*.log
.DS_Store
.env

# IDE/Editor directories
.vscode/
.cursor/
.windsurf/
.trae/

# AI Agent directories
.agent/
.agents/
.codex/
.gemini/
.goose/
.kiro/
.opencode/

# Generated skills in any dot directory
.*/skills/
.claude/
```

## File: `.mcp.json`
```json
{
	"mcpServers": {
		"supabase": {
			"type": "http",
			"url": "https://mcp.supabase.com/mcp?features=docs"
		}
	}
}
```

## File: `AGENTS.md`
```markdown
# AGENTS.md

Guidance for AI coding agents working with this repository.

> **Note:** `CLAUDE.md` is a symlink to this file.

## Prerequisites

This project uses [mise](https://mise.jdx.dev/) to manage tool versions,
environment variables, and project tasks. Run `mise install` to set up the
correct tool versions from `mise.toml`.

## Repository Structure

```
skills/
  {skill-name}/
    SKILL.md              # Required: skill manifest (Agent Skills spec)
    AGENTS.md             # Generated: SKILL.md body (frontmatter stripped)
    CLAUDE.md             # Generated: symlink to AGENTS.md
    references/
      _sections.md        # Required: section definitions
      {prefix}-{name}.md  # Reference files

packages/
  skills-build/           # Generic build system for all skills
  evals/                  # LLM evaluation system for skills
```

## Commands

All tasks are defined in `mise.toml` and can be run with `mise run` (or via
`npm run` which delegates to the same commands).

```bash
mise install                     # Install tool versions (Node.js)
mise run install                 # Install all npm dependencies
mise run build                   # Build all skills
mise run validate                # Validate all skills
mise run check                   # Format and lint (auto-fix)
mise run test                    # Run tests
mise run eval                    # Run all LLM evals
mise run eval:code-fix           # Run code-fix evals only
mise run eval:workflow            # Run workflow evals only
```

Tasks with `sources`/`outputs` defined in `mise.toml` skip automatically when
nothing has changed.

**Before completing any task**, run `mise run check` and `mise run build` to
ensure CI passes.

## Creating a New Skill

Skills follow the [Agent Skills Open Standard](https://agentskills.io/).

1. Create directory: `mkdir -p skills/{skill-name}/references`
2. Create `SKILL.md` following the format below
3. Add `references/_sections.md` defining sections
4. Add reference files: `{prefix}-{reference-name}.md`
5. Run `mise run build`

---

## Writing SKILL.md Files

SKILL.md is the core of every skill. It consists of **YAML frontmatter**
followed by **Markdown instructions**.

### Frontmatter (Required)

```yaml
---
name: skill-name
description: What this skill does and when to use it.
---
```

| Field         | Required | Constraints                                                                     |
| ------------- | -------- | ------------------------------------------------------------------------------- |
| `name`        | Yes      | 1-64 chars. Lowercase alphanumeric and hyphens only. Must match directory name. |
| `description` | Yes      | 1-1024 chars. Describe what the skill does AND when to use it.                  |
| `license`     | No       | License name or reference to bundled license file.                              |
| `metadata`    | No       | Arbitrary key-value pairs (e.g., `author`, `version`).                          |

### Name Field Rules

- Lowercase letters, numbers, and hyphens only (`a-z`, `0-9`, `-`)
- Must not start or end with `-`
- Must not contain consecutive hyphens (`--`)
- Must match the parent directory name

```yaml
# Valid
name: pdf-processing
name: data-analysis

# Invalid
name: PDF-Processing # uppercase not allowed
name: -pdf # cannot start with hyphen
name: pdf--processing # consecutive hyphens not allowed
```

### Description Field (Critical)

The description is the **primary trigger mechanism**. Claude uses it to decide
when to activate the skill.

**Include both:**

1. What the skill does
2. Specific triggers/contexts for when to use it

```yaml
# Good - comprehensive and trigger-rich
description: >
  Supabase database best practices for schema design, RLS policies,
  indexing, and query optimization. Use when working with Supabase
  projects, writing PostgreSQL migrations, configuring Row Level Security,
  or optimizing database performance.

# Bad - too vague
description: Helps with databases.
```

**Do not put "when to use" in the body.** The body loads only after triggering,
so trigger context must be in the description.

### Body Content

The Markdown body contains instructions for using the skill. Write
concisely—Claude is already capable. Only add context Claude doesn't already
have.

**Guidelines:**

- Use imperative form ("Create the table", not "You should create the table")
- Keep under 500 lines; move detailed content to `references/`
- Prefer concise examples over verbose explanations
- Challenge each paragraph: "Does this justify its token cost?"

**Recommended structure:**

1. Quick start or core workflow
2. Key patterns with examples
3. Links to reference files for advanced topics

```markdown
## Quick Start

Create a table with RLS:

[concise code example]

## Common Patterns

### Authentication

[pattern with example]

## Advanced Topics

- **Complex policies**: See
  [references/rls-patterns.md](rls-patterns.md)
- **Performance tuning**: See
  [references/optimization.md](optimization.md)
```

### Progressive Disclosure

Skills use three loading levels:

1. **Metadata** (~100 tokens) - Always loaded for all skills
2. **Body** (<5k tokens recommended) - Loaded when skill triggers
3. **References** (as needed) - Loaded on demand by Claude

Keep SKILL.md lean. Move detailed reference material to separate files and link
to them.

---

## Reference File Format

Reference files in `references/` extend skills with detailed documentation.

```markdown
---
title: Action-Oriented Title
impact: CRITICAL|HIGH|MEDIUM-HIGH|MEDIUM|LOW-MEDIUM|LOW
impactDescription: Quantified benefit
tags: keywords
---

## Title

1-2 sentence explanation.

**Incorrect:** \`\`\`sql -- bad example \`\`\`

**Correct:** \`\`\`sql -- good example \`\`\`
```

## What NOT to Include

Skills should only contain essential files. Do NOT create:

- README.md
- INSTALLATION_GUIDE.md
- QUICK_REFERENCE.md
- CHANGELOG.md

The skill should contain only what an AI agent needs to do the job.
```

## File: `CLAUDE.md`
```markdown
AGENTS.md
```

## File: `CONTRIBUTING.md`
```markdown
# CONTRIBUTING.md

Thank you for contributing to Supabase Agent Skills! Here's how to get started:

[1. Getting Started](#getting-started) | [2. Issues](#issues) |
[3. Pull Requests](#pull-requests) | [4. Contributing New References](#contributing-new-references) |
[5. Creating a New Skill](#creating-a-new-skill)

## Getting Started

To ensure a positive and inclusive environment, please read our
[code of conduct](https://github.com/supabase/.github/blob/main/CODE_OF_CONDUCT.md)
before contributing.

### Setup

This project uses [mise](https://mise.jdx.dev/) to manage tool versions,
environment variables, and project tasks. Install mise, then run from the
repository root:

```bash
mise install        # Install Node.js (version defined in mise.toml)
mise run install    # Install all npm dependencies
```

For LLM evals, copy the env example and add your API keys:

```bash
cp packages/evals/.env.example packages/evals/.env
# Edit packages/evals/.env with your ANTHROPIC_API_KEY and OPENAI_API_KEY
```

mise automatically loads `.env` files defined in `mise.toml`.

## Issues

If you find a typo, have a suggestion for a new skill/reference, or want to improve
existing skills/references, please create an Issue.

- Please search
  [existing Issues](https://github.com/supabase/agent-skills/issues) before
  creating a new one.
- Please include a clear description of the problem or suggestion.
- Tag your issue appropriately (e.g., `bug`, `question`, `enhancement`,
  `new-reference`, `new-skill`, `documentation`).

## Pull Requests

We actively welcome your Pull Requests! Here's what to keep in mind:

- If you're fixing an Issue, make sure someone else hasn't already created a PR
  for it. Link your PR to the related Issue(s).
- We will always try to accept the first viable PR that resolves the Issue.
- If you're new, we encourage you to take a look at issues tagged with
  [good first issue](https://github.com/supabase/agent-skills/labels/good%20first%20issue).
- If you're proposing a significant new skill or major changes, please open a
  [Discussion](https://github.com/orgs/supabase/discussions/new/choose) first to
  gather feedback before investing time in implementation.

### Pre-Flight Checks

Before submitting your PR, make sure you have the right tooling and run these
checks:

```bash
mise install       # Ensure correct Node.js version
mise run check     # Format and lint (auto-fix)
mise run validate  # Check reference format and structure
mise run build     # Generate AGENTS.md from references
```

All commands must complete successfully.

## Contributing New References

To add a reference to an existing skill:

1. Navigate to `skills/{skill-name}/references/`
2. Copy `_template.md` to `{prefix}-{your-reference-name}.md`
3. Fill in the frontmatter (title, impact, tags)
4. Write explanation and examples (Incorrect/Correct)
5. Run validation and build:

```bash
mise run validate
mise run build
```

## Creating a New Skill

Skills follow the [Agent Skills Open Standard](https://agentskills.io/).

### 1. Create the directory structure

```bash
mkdir -p skills/my-skill/references
```

### 2. Create SKILL.md

```yaml
---
name: my-skill
description: Brief description of what this skill does and when to use it.
license: MIT
metadata:
  author: your-org
  version: "1.0.0"
  organization: Your Org
  date: January 2026
  abstract: Detailed description of this skill for the compiled AGENTS.md.
---

# My Skill

Instructions for agents using this skill.

## References

- https://example.com/docs
```

### 3. Create references/_sections.md

```markdown
## 1. First Category (first)
**Impact:** HIGH
**Description:** What this category covers.

## 2. Second Category (second)
**Impact:** MEDIUM
**Description:** What this category covers.
```

### 4. Create reference files

Name files as `{prefix}-{reference-name}.md` where prefix matches a section.

Example: `first-example-reference.md` for section "First Category"

### 5. Build

```bash
mise run build
```

The build system auto-discovers skills by looking for `SKILL.md` files.

## Questions or Feedback?

- Open an Issue for bugs or suggestions
- Start a Discussion for broader topics or proposals
- Check existing Issues and Discussions before creating new ones

## License

By contributing to this repository, you agree that your contributions will be
licensed under the MIT License.
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2026 Supabase

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
![Supabase Agent Skills](assets/og.png)

# Supabase Agent Skills


Agent Skills to help developers using AI agents with Supabase. Agent Skills are
folders of instructions, scripts, and resources that agents like Claude Code,
Cursor, Github Copilot, etc... can discover and use to do things more accurately
and efficiently.

The skills in this repo follow the [Agent Skills](https://agentskills.io/)
format.

## Installation

```bash
npx skills add supabase/agent-skills
```

### Claude Code Plugin

You can also install the skills in this repo as Claude Code plugins

```bash
/plugin marketplace add supabase/agent-skills
/plugin install postgres-best-practices@supabase-agent-skills
```

## Available Skills

<details>
<summary><strong>supabase-postgres-best-practices</strong></summary>

Postgres performance optimization guidelines from Supabase. Contains references
across 8 categories, prioritized by impact.

**Use when:**

- Writing SQL queries or designing schemas
- Implementing indexes or query optimization
- Reviewing database performance issues
- Configuring connection pooling or scaling
- Working with Row-Level Security (RLS)

**Categories covered:**

- Query Performance (Critical)
- Connection Management (Critical)
- Schema Design (High)
- Concurrency & Locking (Medium-High)
- Security & RLS (Medium-High)
- Data Access Patterns (Medium)
- Monitoring & Diagnostics (Low-Medium)
- Advanced Features (Low)

</details>

## Usage

Skills are automatically available once installed. The agent will use them when
relevant tasks are detected.

**Examples:**

```
Optimize this Postgres query
```

```
Review my schema for performance issues
```

```
Help me add proper indexes to this table
```

## Skill Structure

Each skill follows the [Agent Skills Open Standard](https://agentskills.io/):

- `SKILL.md` - Required skill manifest with frontmatter (name, description, metadata)
- `AGENTS.md` - Compiled references document (generated)
- `references/` - Individual reference files
```

## File: `biome.json`
```json
{
	"$schema": "https://biomejs.dev/schemas/2.3.11/schema.json",
	"vcs": {
		"enabled": true,
		"clientKind": "git",
		"useIgnoreFile": true
	},
	"files": {
		"ignoreUnknown": false
	},
	"formatter": {
		"enabled": true,
		"indentStyle": "tab"
	},
	"linter": {
		"enabled": true,
		"rules": {
			"recommended": true
		}
	},
	"javascript": {
		"formatter": {
			"quoteStyle": "double"
		}
	},
	"assist": {
		"enabled": true,
		"actions": {
			"source": {
				"organizeImports": "on"
			}
		}
	}
}
```

## File: `mise.lock`
```
[[tools.node]]
version = "24.13.0"
backend = "core:node"
"platforms.linux-arm64" = { checksum = "sha256:0f6d40b94c6a2eb6b4c240ffc8b9fd3ada7ab044c177dd413c06e1ef9a63f081", url = "https://nodejs.org/dist/v24.13.0/node-v24.13.0-linux-arm64.tar.gz"}
"platforms.linux-x64" = { checksum = "sha256:6223aad1a81f9d1e7b682c59d12e2de233f7b4c37475cd40d1c89c42b737ffa8", url = "https://nodejs.org/dist/v24.13.0/node-v24.13.0-linux-x64.tar.gz"}
"platforms.macos-arm64" = { checksum = "sha256:d595961e563fcae057d4a0fb992f175a54d97fcc4a14dc2d474d92ddeea3b9f8", url = "https://nodejs.org/dist/v24.13.0/node-v24.13.0-darwin-arm64.tar.gz"}
"platforms.macos-x64" = { checksum = "sha256:6f03c1b48ddbe1b129a6f8038be08e0899f05f17185b4d3e4350180ab669a7f3", url = "https://nodejs.org/dist/v24.13.0/node-v24.13.0-darwin-x64.tar.gz"}
"platforms.windows-x64" = { checksum = "sha256:ca2742695be8de44027d71b3f53a4bdb36009b95575fe1ae6f7f0b5ce091cb88", url = "https://nodejs.org/dist/v24.13.0/node-v24.13.0-win-x64.zip"}
```

## File: `mise.toml`
```
[settings]
experimental = true
lockfile = true

[tools]
node = "lts"

[env]
_.path = ["{{config_root}}/node_modules/.bin"]
_.file = [".env", "packages/evals/.env"]

# ── Root tasks ────────────────────────────────────────────────────────

[tasks.install]
description = "Install all dependencies"
run = "npm install && npm --prefix packages/skills-build install && npm --prefix packages/evals install"
sources = ["package.json", "packages/skills-build/package.json", "packages/evals/package.json"]
outputs = ["node_modules/.package-lock.json"]

[tasks.validate]
description = "Validate all skills"
run = "npm --prefix packages/skills-build run validate"
sources = ["skills/**/SKILL.md", "skills/**/references/**"]

[tasks.build]
description = "Build all skills"
run = "npm --prefix packages/skills-build run build"
sources = ["skills/**/SKILL.md", "skills/**/references/**", "packages/skills-build/src/**"]
outputs = ["skills/**/AGENTS.md"]

[tasks.check]
description = "Format and lint (auto-fix)"
run = "biome check --write ."
sources = ["**/*.ts", "**/*.js", "**/*.json", "biome.json"]

[tasks."ci:check"]
description = "CI format and lint check"
run = "biome ci ."
sources = ["**/*.ts", "**/*.js", "**/*.json", "biome.json"]

[tasks.test]
description = "Run tests"
run = "vitest run"
sources = ["test/**", "skills/**"]

# ── Eval tasks ────────────────────────────────────────────────────────

[tasks.eval]
description = "Run all evals"
run = "tsx packages/evals/src/cli.ts"
sources = ["packages/evals/src/**", "skills/**/references/**"]

[tasks."eval:code-fix"]
description = "Run code-fix evals"
run = "tsx packages/evals/src/cli.ts --type code-fix"
sources = ["packages/evals/src/**", "skills/**/references/**"]

[tasks."eval:workflow"]
description = "Run workflow evals"
run = "tsx packages/evals/src/cli.ts --type workflow"
sources = ["packages/evals/src/**", "skills/**/references/**"]
```

## File: `package.json`
```json
{
	"name": "supabase-agent-skills",
	"version": "1.0.0",
	"author": "Supabase",
	"license": "MIT",
	"description": "Official Supabase agent skills",
	"scripts": {
		"build": "npm --prefix packages/skills-build run build",
		"validate": "npm --prefix packages/skills-build run validate",
		"format": "biome format --write .",
		"format:check": "biome format .",
		"lint": "biome lint --write .",
		"lint:check": "biome lint .",
		"check": "biome check --write .",
		"ci:check": "biome ci .",
		"test": "vitest run",
		"test:sanity": "vitest run test/sanity.test.ts"
	},
	"devDependencies": {
		"@biomejs/biome": "2.3.11",
		"vitest": "^3.0.0"
	}
}
```

## File: `vitest.config.ts`
```typescript
import { defineConfig } from "vitest/config";

export default defineConfig({
	test: {
		testTimeout: 180000, // 3 minute timeout for sanity tests
		hookTimeout: 180000,
	},
});
```

## File: `packages/skills-build/package.json`
```json
{
	"name": "skills-build",
	"version": "1.0.0",
	"type": "module",
	"author": "Supabase",
	"license": "MIT",
	"description": "Generic build system for Supabase agent skills",
	"scripts": {
		"build": "tsx src/build.ts",
		"validate": "tsx src/validate.ts",
		"dev": "npm run validate && npm run build"
	},
	"devDependencies": {
		"@types/node": "^20.10.0",
		"tsx": "^4.7.0",
		"typescript": "^5.3.0"
	}
}
```

## File: `packages/skills-build/tsconfig.json`
```json
{
	"compilerOptions": {
		"target": "ES2022",
		"module": "ESNext",
		"moduleResolution": "bundler",
		"esModuleInterop": true,
		"strict": true,
		"skipLibCheck": true,
		"outDir": "dist",
		"rootDir": "src",
		"declaration": true,
		"resolveJsonModule": true
	},
	"include": ["src/**/*"],
	"exclude": ["node_modules", "dist"]
}
```

## File: `packages/skills-build/src/build.ts`
```typescript
import {
	existsSync,
	lstatSync,
	readdirSync,
	readFileSync,
	statSync,
	symlinkSync,
	unlinkSync,
	writeFileSync,
} from "node:fs";
import { join } from "node:path";
import {
	discoverSkills,
	getSkillPaths,
	type SkillPaths,
	validateSkillExists,
} from "./config.js";
import type { Section } from "./types.js";

/**
 * Generate SECTION_MAP from parsed sections
 */
function generateSectionMap(sections: Section[]): Record<string, number> {
	const map: Record<string, number> = {};
	for (const section of sections) {
		map[section.prefix] = section.number;
	}
	return map;
}

/**
 * Get all markdown files from a directory (flat, no subdirectories)
 */
function getMarkdownFiles(dir: string): string[] {
	const files: string[] = [];

	if (!existsSync(dir)) {
		return files;
	}

	const entries = readdirSync(dir);

	for (const entry of entries) {
		// Skip files starting with underscore
		if (entry.startsWith("_")) {
			continue;
		}

		const fullPath = join(dir, entry);
		const stat = statSync(fullPath);

		// Only include files, skip directories
		if (stat.isFile() && entry.endsWith(".md")) {
			files.push(fullPath);
		}
	}

	return files;
}

/**
 * @deprecated Use getMarkdownFiles instead - nested directories are not supported
 */
function getMarkdownFilesRecursive(dir: string): string[] {
	return getMarkdownFiles(dir);
}

/**
 * Parse section definitions from _sections.md (legacy function for validation)
 */
function parseSections(rulesDir: string): Section[] {
	const sectionsFile = join(rulesDir, "_sections.md");
	if (!existsSync(sectionsFile)) {
		return [];
	}
	return parseSectionsFromFile(sectionsFile);
}

/**
 * Extract the markdown body from SKILL.md (everything after frontmatter)
 */
function extractSkillBody(content: string): string {
	if (!content.startsWith("---")) {
		return content.trim();
	}

	const endIndex = content.indexOf("---", 3);
	if (endIndex === -1) {
		return content.trim();
	}

	return content.slice(endIndex + 3).trim();
}

/**
 * Parse section definitions from a _sections.md file
 */
function parseSectionsFromFile(filePath: string): Section[] {
	const content = readFileSync(filePath, "utf-8");
	const sections: Section[] = [];

	const sectionMatches = content.matchAll(
		/##\s+(\d+)\.\s+([^\n(]+)\s*\((\w+)\)\s*\n\*\*Impact:\*\*\s*(\w+(?:-\w+)?)\s*\n\*\*Description:\*\*\s*([^\n]+)/g,
	);

	for (const match of sectionMatches) {
		sections.push({
			number: parseInt(match[1], 10),
			title: match[2].trim(),
			prefix: match[3].trim(),
			impact: match[4].trim() as Section["impact"],
			description: match[5].trim(),
		});
	}

	return sections;
}

/**
 * Parse _sections.md from references directory root only
 * Note: Nested directories are not supported - all reference files should be in references/ root
 */
function parseAllSections(referencesDir: string): Section[] {
	const sectionsFile = join(referencesDir, "_sections.md");
	if (existsSync(sectionsFile)) {
		return parseSectionsFromFile(sectionsFile);
	}
	return [];
}

/**
 * Get all reference files from references/ root (excluding _sections.md)
 * Note: Nested directories are not supported - all reference files should be in references/ root
 */
function getReferenceFiles(referencesDir: string): string[] {
	const files: string[] = [];

	if (!existsSync(referencesDir)) {
		return files;
	}

	const entries = readdirSync(referencesDir);

	for (const entry of entries) {
		// Skip files starting with underscore
		if (entry.startsWith("_")) {
			continue;
		}

		const fullPath = join(referencesDir, entry);
		const stat = statSync(fullPath);

		// Only include files at root level, skip directories
		if (stat.isFile() && entry.endsWith(".md")) {
			files.push(fullPath);
		}
	}

	return files;
}

/**
 * Parse the SKILL.md body into its H1 title and the content after it.
 * Returns the title text and the remaining body content.
 */
function parseSkillBodySections(body: string): {
	title: string | null;
	content: string;
} {
	const lines = body.split("\n");
	const firstLine = lines[0]?.trim() ?? "";

	const h1Match = firstLine.match(/^#\s+(.+)$/);
	if (!h1Match) {
		return { title: null, content: body };
	}

	const content = lines.slice(1).join("\n").trim();
	return { title: h1Match[1].trim(), content };
}

/**
 * Create a symlink, removing any existing file or symlink at the target path
 */
function createSymlink(symlinkPath: string, target: string): void {
	if (existsSync(symlinkPath)) {
		const stat = lstatSync(symlinkPath);
		if (stat.isSymbolicLink() || stat.isFile()) {
			unlinkSync(symlinkPath);
		}
	}

	symlinkSync(target, symlinkPath);
}

/**
 * Build AGENTS.md for a specific skill
 *
 * Structure: H1 Title > Structure > Usage > rest of SKILL.md body
 * CLAUDE.md = symlink to AGENTS.md.
 */
function buildSkill(paths: SkillPaths): void {
	console.log(`[${paths.name}] Building AGENTS.md...`);

	// Read SKILL.md and strip frontmatter
	const skillContent = existsSync(paths.skillFile)
		? readFileSync(paths.skillFile, "utf-8")
		: "";
	const body = extractSkillBody(skillContent);
	const { title, content: skillBodyContent } = parseSkillBodySections(body);

	const output: string[] = [];

	// 1. Title (from SKILL.md H1)
	if (title) {
		output.push(`# ${title}\n`);
	}

	// 2. Structure
	output.push(`## Structure\n`);
	output.push("```");
	output.push(`${paths.name}/`);
	output.push(`  SKILL.md       # Main skill file - read this first`);
	output.push(`  AGENTS.md      # This navigation guide`);
	output.push(`  CLAUDE.md      # Symlink to AGENTS.md`);
	if (existsSync(paths.referencesDir)) {
		output.push(`  references/    # Detailed reference files`);
	}
	output.push("```\n");

	// 3. Usage
	output.push(`## Usage\n`);
	output.push(`1. Read \`SKILL.md\` for the main skill instructions`);
	output.push(
		`2. Browse \`references/\` for detailed documentation on specific topics`,
	);
	output.push(
		`3. Reference files are loaded on-demand - read only what you need\n`,
	);

	// 4. Rest of SKILL.md body (after H1 title)
	if (skillBodyContent) {
		output.push(skillBodyContent);
		output.push("");
	}

	// Write AGENTS.md
	writeFileSync(paths.agentsOutput, output.join("\n"));
	console.log(`  Generated: ${paths.agentsOutput}`);

	// Create CLAUDE.md -> AGENTS.md symlink
	createSymlink(paths.claudeSymlink, "AGENTS.md");
	console.log(`  Created symlink: CLAUDE.md -> AGENTS.md`);
}

// Run build when executed directly
const isMainModule =
	process.argv[1]?.endsWith("build.ts") ||
	process.argv[1]?.endsWith("build.js");

if (isMainModule) {
	const targetSkill = process.argv[2];

	if (targetSkill) {
		// Build specific skill
		if (!validateSkillExists(targetSkill)) {
			console.error(`Error: Skill "${targetSkill}" not found in skills/`);
			const available = discoverSkills();
			if (available.length > 0) {
				console.error(`Available skills: ${available.join(", ")}`);
			}
			process.exit(1);
		}
		buildSkill(getSkillPaths(targetSkill));
	} else {
		// Build all skills
		const skills = discoverSkills();
		if (skills.length === 0) {
			console.log("No skills found in skills/ directory.");
			process.exit(0);
		}

		console.log(`Found ${skills.length} skill(s): ${skills.join(", ")}\n`);
		for (const skill of skills) {
			buildSkill(getSkillPaths(skill));
			console.log("");
		}
	}

	console.log("✅ Done!");
}

export {
	buildSkill,
	extractSkillBody,
	generateSectionMap,
	getMarkdownFiles,
	getMarkdownFilesRecursive, // deprecated, use getMarkdownFiles
	getReferenceFiles,
	parseAllSections,
	parseSkillBodySections,
	parseSections,
};
```

## File: `packages/skills-build/src/config.ts`
```typescript
import { existsSync, readdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

// Build package directory
export const BUILD_DIR = join(__dirname, "..");

// Skills root directory
export const SKILLS_ROOT = join(BUILD_DIR, "../../skills");

// Skill paths interface
export interface SkillPaths {
	name: string;
	skillDir: string;
	referencesDir: string;
	agentsOutput: string;
	claudeSymlink: string;
	skillFile: string;
}

// Discover all valid skills (directories with SKILL.md per Agent Skills spec)
export function discoverSkills(): string[] {
	if (!existsSync(SKILLS_ROOT)) return [];

	return readdirSync(SKILLS_ROOT, { withFileTypes: true })
		.filter((d) => d.isDirectory())
		.filter((d) => existsSync(join(SKILLS_ROOT, d.name, "SKILL.md")))
		.map((d) => d.name);
}

// Get paths for a specific skill
export function getSkillPaths(skillName: string): SkillPaths {
	const skillDir = join(SKILLS_ROOT, skillName);
	return {
		name: skillName,
		skillDir,
		referencesDir: join(skillDir, "references"),
		agentsOutput: join(skillDir, "AGENTS.md"),
		claudeSymlink: join(skillDir, "CLAUDE.md"),
		skillFile: join(skillDir, "SKILL.md"),
	};
}

// Validate skill exists
export function validateSkillExists(skillName: string): boolean {
	const paths = getSkillPaths(skillName);
	return existsSync(paths.skillFile);
}

// Valid impact levels in priority order
export const IMPACT_LEVELS = [
	"CRITICAL",
	"HIGH",
	"MEDIUM-HIGH",
	"MEDIUM",
	"LOW-MEDIUM",
	"LOW",
] as const;
```

## File: `packages/skills-build/src/parser.ts`
```typescript
import { readFileSync } from "node:fs";
import { basename } from "node:path";
import { IMPACT_LEVELS } from "./config.js";
import type { CodeExample, ImpactLevel, ParseResult, Rule } from "./types.js";

/**
 * Parse YAML-style frontmatter from markdown content
 */
function parseFrontmatter(content: string): {
	frontmatter: Record<string, string>;
	body: string;
} {
	const frontmatter: Record<string, string> = {};

	if (!content.startsWith("---")) {
		return { frontmatter, body: content };
	}

	const endIndex = content.indexOf("---", 3);
	if (endIndex === -1) {
		return { frontmatter, body: content };
	}

	const frontmatterContent = content.slice(3, endIndex).trim();
	const body = content.slice(endIndex + 3).trim();

	for (const line of frontmatterContent.split("\n")) {
		const colonIndex = line.indexOf(":");
		if (colonIndex === -1) continue;

		const key = line.slice(0, colonIndex).trim();
		let value = line.slice(colonIndex + 1).trim();

		// Strip quotes
		if (
			(value.startsWith('"') && value.endsWith('"')) ||
			(value.startsWith("'") && value.endsWith("'"))
		) {
			value = value.slice(1, -1);
		}

		frontmatter[key] = value;
	}

	return { frontmatter, body };
}

/**
 * Extract section number from filename prefix
 */
function getSectionFromFilename(
	filename: string,
	sectionMap: Record<string, number>,
): number | null {
	const base = basename(filename, ".md");
	const prefix = base.split("-")[0];
	return sectionMap[prefix] ?? null;
}

/**
 * Extract code examples from markdown body
 */
function extractExamples(body: string): CodeExample[] {
	const examples: CodeExample[] = [];
	const lines = body.split("\n");

	let currentLabel = "";
	let currentDescription = "";
	let inCodeBlock = false;
	let codeBlockLang = "";
	let codeBlockContent: string[] = [];
	let additionalText: string[] = [];

	for (let i = 0; i < lines.length; i++) {
		const line = lines[i];

		// Check for example label: **Label:** or **Label (description):**
		const labelMatch = line.match(
			/^\*\*([^*]+?)(?:\s*\(([^)]+)\))?\s*:\*\*\s*$/,
		);
		if (labelMatch && !inCodeBlock) {
			// Save previous example if exists
			if (currentLabel && codeBlockContent.length > 0) {
				examples.push({
					label: currentLabel,
					description: currentDescription || undefined,
					code: codeBlockContent.join("\n"),
					language: codeBlockLang || undefined,
					additionalText:
						additionalText.length > 0
							? additionalText.join("\n").trim()
							: undefined,
				});
			}

			currentLabel = labelMatch[1].trim();
			currentDescription = labelMatch[2]?.trim() || "";
			codeBlockContent = [];
			codeBlockLang = "";
			additionalText = [];
			continue;
		}

		// Check for code block start
		if (line.startsWith("```") && !inCodeBlock) {
			inCodeBlock = true;
			codeBlockLang = line.slice(3).trim();
			continue;
		}

		// Check for code block end
		if (line.startsWith("```") && inCodeBlock) {
			inCodeBlock = false;
			continue;
		}

		// Collect code block content
		if (inCodeBlock) {
			codeBlockContent.push(line);
			continue;
		}

		// Collect additional text after code block (before next label)
		if (currentLabel && codeBlockContent.length > 0 && line.trim()) {
			// Stop collecting if we hit a heading or reference
			if (line.startsWith("#") || line.startsWith("Reference")) {
				continue;
			}
			additionalText.push(line);
		}
	}

	// Save last example
	if (currentLabel && codeBlockContent.length > 0) {
		examples.push({
			label: currentLabel,
			description: currentDescription || undefined,
			code: codeBlockContent.join("\n"),
			language: codeBlockLang || undefined,
			additionalText:
				additionalText.length > 0
					? additionalText.join("\n").trim()
					: undefined,
		});
	}

	return examples;
}

/**
 * Extract title from first ## heading
 */
function extractTitle(body: string): string | null {
	const match = body.match(/^##\s+(.+)$/m);
	return match ? match[1].trim() : null;
}

/**
 * Extract explanation (content between title and first example)
 */
function extractExplanation(body: string): string {
	const lines = body.split("\n");
	const explanationLines: string[] = [];
	let foundTitle = false;

	for (const line of lines) {
		if (line.startsWith("## ")) {
			foundTitle = true;
			continue;
		}

		if (!foundTitle) continue;

		// Stop at first example label or code block
		if (line.match(/^\*\*[^*]+:\*\*/) || line.startsWith("```")) {
			break;
		}

		explanationLines.push(line);
	}

	return explanationLines.join("\n").trim();
}

/**
 * Extract references from body
 */
function extractReferences(body: string): string[] {
	const references: string[] = [];
	const lines = body.split("\n");

	for (const line of lines) {
		// Match "Reference: [text](url)" or "- [text](url)" after "References:"
		const refMatch = line.match(/Reference:\s*\[([^\]]+)\]\(([^)]+)\)/);
		if (refMatch) {
			references.push(refMatch[2]);
			continue;
		}

		// Match list items under References section
		const listMatch = line.match(/^-\s*\[([^\]]+)\]\(([^)]+)\)/);
		if (listMatch) {
			references.push(listMatch[2]);
		}
	}

	return references;
}

/**
 * Parse a rule file and return structured data
 */
export function parseRuleFile(
	filePath: string,
	sectionMap: Record<string, number>,
): ParseResult {
	const errors: string[] = [];
	const warnings: string[] = [];

	try {
		const content = readFileSync(filePath, "utf-8");
		const { frontmatter, body } = parseFrontmatter(content);

		// Extract section from filename
		const section = getSectionFromFilename(filePath, sectionMap);
		if (section === null) {
			errors.push(
				`Could not determine section from filename: ${basename(filePath)}`,
			);
			return { success: false, errors, warnings };
		}

		// Get title from frontmatter or body
		const title = frontmatter.title || extractTitle(body);
		if (!title) {
			errors.push("Missing title in frontmatter or body");
			return { success: false, errors, warnings };
		}

		// Get impact level
		const impact = frontmatter.impact as ImpactLevel;
		if (!impact || !IMPACT_LEVELS.includes(impact)) {
			errors.push(
				`Invalid or missing impact level: ${impact}. Must be one of: ${IMPACT_LEVELS.join(", ")}`,
			);
			return { success: false, errors, warnings };
		}

		// Extract other fields
		const explanation = extractExplanation(body);
		const examples = extractExamples(body);

		const tags = frontmatter.tags?.split(",").map((t) => t.trim()) || [];

		// Validation warnings
		if (!explanation || explanation.length < 20) {
			warnings.push("Explanation is very short or missing");
		}

		if (examples.length === 0) {
			warnings.push("No code examples found");
		}

		const rule: Rule = {
			id: "", // Will be assigned during build
			title,
			section,
			impact,
			impactDescription: frontmatter.impactDescription,
			explanation,
			examples,
			references: extractReferences(body),
			tags: tags.length > 0 ? tags : undefined,
		};

		return { success: true, rule, errors, warnings };
	} catch (error) {
		errors.push(`Failed to parse file: ${error}`);
		return { success: false, errors, warnings };
	}
}
```

## File: `packages/skills-build/src/types.ts`
```typescript
export type ImpactLevel =
	| "CRITICAL"
	| "HIGH"
	| "MEDIUM-HIGH"
	| "MEDIUM"
	| "LOW-MEDIUM"
	| "LOW";

export interface CodeExample {
	label: string;
	description?: string;
	code: string;
	language?: string;
	additionalText?: string;
}

export interface Rule {
	id: string;
	title: string;
	section: number;
	subsection?: number;
	impact: ImpactLevel;
	impactDescription?: string;
	explanation: string;
	examples: CodeExample[];
	references?: string[];
	tags?: string[];
	supabaseNotes?: string;
}

export interface Section {
	number: number;
	title: string;
	prefix: string;
	impact: ImpactLevel;
	description: string;
}

export interface Metadata {
	version: string;
	organization: string;
	date: string;
	abstract: string;
	references: string[];
	maintainers?: string[];
}

export interface ParseResult {
	success: boolean;
	rule?: Rule;
	errors: string[];
	warnings: string[];
}

export interface ValidationResult {
	valid: boolean;
	errors: string[];
	warnings: string[];
}
```

## File: `packages/skills-build/src/validate.ts`
```typescript
import { existsSync, readFileSync } from "node:fs";
import { basename } from "node:path";
import {
	extractSkillBody,
	generateSectionMap,
	getMarkdownFiles,
	parseAllSections,
	parseSections,
	parseSkillBodySections,
} from "./build.js";
import {
	discoverSkills,
	getSkillPaths,
	IMPACT_LEVELS,
	type SkillPaths,
	validateSkillExists,
} from "./config.js";
import { parseRuleFile } from "./parser.js";
import type { ValidationResult } from "./types.js";

/**
 * Check if an example label indicates a "bad" pattern
 */
function isBadExample(label: string): boolean {
	const lower = label.toLowerCase();
	return (
		lower.includes("incorrect") ||
		lower.includes("wrong") ||
		lower.includes("bad")
	);
}

/**
 * Check if an example label indicates a "good" pattern
 */
function isGoodExample(label: string): boolean {
	const lower = label.toLowerCase();
	return (
		lower.includes("correct") ||
		lower.includes("good") ||
		lower.includes("usage") ||
		lower.includes("implementation") ||
		lower.includes("example") ||
		lower.includes("recommended")
	);
}

/**
 * Validate a single rule file
 */
export function validateRuleFile(
	filePath: string,
	sectionMap?: Record<string, number>,
	referencesDir?: string,
): ValidationResult {
	const errors: string[] = [];
	const warnings: string[] = [];

	// Generate section map if not provided
	if (!sectionMap && referencesDir) {
		const sections = parseSections(referencesDir);
		sectionMap = generateSectionMap(sections);
	} else if (!sectionMap) {
		sectionMap = {};
	}

	const result = parseRuleFile(filePath, sectionMap);

	// Add parser errors and warnings
	errors.push(...result.errors);
	warnings.push(...result.warnings);

	if (!result.success || !result.rule) {
		return { valid: false, errors, warnings };
	}

	const rule = result.rule;

	// Validate title
	if (!rule.title || rule.title.trim().length === 0) {
		errors.push("Missing or empty title");
	}

	// Validate explanation
	if (!rule.explanation || rule.explanation.trim().length === 0) {
		errors.push("Missing or empty explanation");
	} else if (rule.explanation.length < 50) {
		warnings.push("Explanation is shorter than 50 characters");
	}

	// Validate examples
	if (rule.examples.length === 0) {
		errors.push(
			"Missing examples (need at least one bad and one good example)",
		);
	} else {
		const hasBad = rule.examples.some((e) => isBadExample(e.label));
		const hasGood = rule.examples.some((e) => isGoodExample(e.label));

		if (!hasBad && !hasGood) {
			errors.push("Missing bad/incorrect and good/correct examples");
		} else if (!hasBad) {
			warnings.push("Missing bad/incorrect example (recommended for clarity)");
		} else if (!hasGood) {
			errors.push("Missing good/correct example");
		}

		// Check for code in examples
		const hasCode = rule.examples.some(
			(e) => e.code && e.code.trim().length > 0,
		);
		if (!hasCode) {
			errors.push("Examples have no code");
		}

		// Check for language specification
		for (const example of rule.examples) {
			if (example.code && !example.language) {
				warnings.push(
					`Example "${example.label}" missing language specification`,
				);
			}
		}
	}

	// Validate impact level
	if (!IMPACT_LEVELS.includes(rule.impact)) {
		errors.push(
			`Invalid impact level: ${rule.impact}. Must be one of: ${IMPACT_LEVELS.join(", ")}`,
		);
	}

	// Warning for missing impact description
	if (!rule.impactDescription) {
		warnings.push(
			"Missing impactDescription (recommended for quantifying benefit)",
		);
	}

	return {
		valid: errors.length === 0,
		errors,
		warnings,
	};
}

/**
 * Extract the `name` field from SKILL.md frontmatter
 */
function extractSkillName(skillFilePath: string): string | null {
	if (!existsSync(skillFilePath)) return null;

	const content = readFileSync(skillFilePath, "utf-8");
	if (!content.startsWith("---")) return null;

	const endIndex = content.indexOf("---", 3);
	if (endIndex === -1) return null;

	const frontmatter = content.slice(3, endIndex);
	for (const line of frontmatter.split("\n")) {
		const match = line.match(/^name:\s*(.+)/);
		if (match) return match[1].trim();
	}
	return null;
}

/**
 * Convert a title to kebab-case (e.g., "Supabase Postgres Best Practices" -> "supabase-postgres-best-practices")
 */
function titleToKebab(title: string): string {
	return title
		.toLowerCase()
		.replace(/[^a-z0-9]+/g, "-")
		.replace(/^-|-$/g, "");
}

/**
 * Validate SKILL.md structure:
 * - `name` field matches directory name (kebab-case)
 * - Body starts with an H1 heading
 * - H1 title in kebab-case matches directory name
 */
function validateSkillStructure(paths: SkillPaths): string[] {
	const errors: string[] = [];
	const skillName = extractSkillName(paths.skillFile);

	if (!skillName) {
		errors.push("SKILL.md is missing the `name` field in frontmatter");
		return errors;
	}

	if (skillName !== paths.name) {
		errors.push(
			`SKILL.md name "${skillName}" does not match directory name "${paths.name}"`,
		);
	}

	// Validate kebab-case format
	if (!/^[a-z0-9]+(-[a-z0-9]+)*$/.test(paths.name)) {
		errors.push(
			`Directory name "${paths.name}" is not valid kebab-case (lowercase alphanumeric and hyphens only, no leading/trailing/consecutive hyphens)`,
		);
	}

	// Validate body starts with H1 and title matches directory name in kebab-case
	if (existsSync(paths.skillFile)) {
		const content = readFileSync(paths.skillFile, "utf-8");
		const body = extractSkillBody(content);
		const { title } = parseSkillBodySections(body);

		if (!title) {
			errors.push(
				"SKILL.md body must start with an H1 heading (e.g., `# Skill Title`)",
			);
		} else {
			const kebabTitle = titleToKebab(title);
			if (kebabTitle !== paths.name) {
				errors.push(
					`H1 title "${title}" in kebab-case is "${kebabTitle}", but directory name is "${paths.name}"`,
				);
			}
		}
	}

	return errors;
}

/**
 * Validate all reference files for a skill
 */
function validateSkill(paths: SkillPaths): boolean {
	console.log(`[${paths.name}] Validating...`);

	// Validate skill structure (name, kebab-case, H1 heading)
	const nameErrors = validateSkillStructure(paths);
	if (nameErrors.length > 0) {
		for (const error of nameErrors) {
			console.log(`  ERROR: ${error}`);
		}
		return false;
	}

	// Check if references directory exists
	if (!existsSync(paths.referencesDir)) {
		console.log(`  No references directory found.`);
		return true;
	}

	// Get section map (including from subdirectories)
	const sections = parseAllSections(paths.referencesDir);
	const sectionMap = generateSectionMap(sections);

	// Get all markdown files from references/ root (excluding _ prefixed files)
	const files = getMarkdownFiles(paths.referencesDir);

	if (files.length === 0) {
		console.log(`  No rule files found.`);
		return true;
	}

	let validFiles = 0;
	let invalidFiles = 0;
	let hasErrors = false;

	for (const file of files) {
		const result = validateRuleFile(file, sectionMap, paths.referencesDir);
		const filename = basename(file);

		if (result.valid) {
			validFiles++;
		} else {
			invalidFiles++;
		}

		if (!result.valid || result.warnings.length > 0) {
			console.log(`\n  ${filename}:`);

			for (const error of result.errors) {
				console.log(`    ERROR: ${error}`);
				hasErrors = true;
			}

			for (const warning of result.warnings) {
				console.log(`    WARNING: ${warning}`);
			}
		}
	}

	console.log(
		`\n  Total: ${files.length} | Valid: ${validFiles} | Invalid: ${invalidFiles}`,
	);

	return !hasErrors;
}

// Run validation when executed directly
const isMainModule =
	process.argv[1]?.endsWith("validate.ts") ||
	process.argv[1]?.endsWith("validate.js");

if (isMainModule) {
	const targetSkill = process.argv[2];

	if (targetSkill) {
		// Validate specific skill
		if (!validateSkillExists(targetSkill)) {
			console.error(`Error: Skill "${targetSkill}" not found in skills/`);
			const available = discoverSkills();
			if (available.length > 0) {
				console.error(`Available skills: ${available.join(", ")}`);
			}
			process.exit(1);
		}

		const valid = validateSkill(getSkillPaths(targetSkill));
		console.log(valid ? "\n✅ Validation passed!" : "\n❌ Validation failed.");
		process.exit(valid ? 0 : 1);
	} else {
		// Validate all skills
		const skills = discoverSkills();
		if (skills.length === 0) {
			console.log("No skills found in skills/ directory.");
			process.exit(0);
		}

		console.log(`Found ${skills.length} skill(s): ${skills.join(", ")}\n`);

		let allValid = true;
		for (const skill of skills) {
			if (!validateSkill(getSkillPaths(skill))) {
				allValid = false;
			}
			console.log("");
		}

		console.log(
			allValid ? "✅ All validations passed!" : "❌ Some validations failed.",
		);
		process.exit(allValid ? 0 : 1);
	}
}

export { validateSkill };
```

## File: `skills/supabase-postgres-best-practices/AGENTS.md`
```markdown
# Supabase Postgres Best Practices

## Structure

```
supabase-postgres-best-practices/
  SKILL.md       # Main skill file - read this first
  AGENTS.md      # This navigation guide
  CLAUDE.md      # Symlink to AGENTS.md
  references/    # Detailed reference files
```

## Usage

1. Read `SKILL.md` for the main skill instructions
2. Browse `references/` for detailed documentation on specific topics
3. Reference files are loaded on-demand - read only what you need

Comprehensive performance optimization guide for Postgres, maintained by Supabase. Contains rules across 8 categories, prioritized by impact to guide automated query optimization and schema design.

## When to Apply

Reference these guidelines when:
- Writing SQL queries or designing schemas
- Implementing indexes or query optimization
- Reviewing database performance issues
- Configuring connection pooling or scaling
- Optimizing for Postgres-specific features
- Working with Row-Level Security (RLS)

## Rule Categories by Priority

| Priority | Category | Impact | Prefix |
|----------|----------|--------|--------|
| 1 | Query Performance | CRITICAL | `query-` |
| 2 | Connection Management | CRITICAL | `conn-` |
| 3 | Security & RLS | CRITICAL | `security-` |
| 4 | Schema Design | HIGH | `schema-` |
| 5 | Concurrency & Locking | MEDIUM-HIGH | `lock-` |
| 6 | Data Access Patterns | MEDIUM | `data-` |
| 7 | Monitoring & Diagnostics | LOW-MEDIUM | `monitor-` |
| 8 | Advanced Features | LOW | `advanced-` |

## How to Use

Read individual rule files for detailed explanations and SQL examples:

```
references/query-missing-indexes.md
references/schema-partial-indexes.md
references/_sections.md
```

Each rule file contains:
- Brief explanation of why it matters
- Incorrect SQL example with explanation
- Correct SQL example with explanation
- Optional EXPLAIN output or metrics
- Additional context and references
- Supabase-specific notes (when applicable)

## References

- https://www.postgresql.org/docs/current/
- https://supabase.com/docs
- https://wiki.postgresql.org/wiki/Performance_Optimization
- https://supabase.com/docs/guides/database/overview
- https://supabase.com/docs/guides/auth/row-level-security
```

## File: `skills/supabase-postgres-best-practices/CLAUDE.md`
```markdown
AGENTS.md
```

## File: `skills/supabase-postgres-best-practices/README.md`
```markdown
# Supabase Postgres Best Practices - Contributor Guide

This skill contains Postgres performance optimization references optimized for
AI agents and LLMs. It follows the [Agent Skills Open Standard](https://agentskills.io/).

## Quick Start

```bash
# From repository root
npm install

# Validate existing references
npm run validate

# Build AGENTS.md
npm run build
```

## Creating a New Reference

1. **Choose a section prefix** based on the category:
   - `query-` Query Performance (CRITICAL)
   - `conn-` Connection Management (CRITICAL)
   - `security-` Security & RLS (CRITICAL)
   - `schema-` Schema Design (HIGH)
   - `lock-` Concurrency & Locking (MEDIUM-HIGH)
   - `data-` Data Access Patterns (MEDIUM)
   - `monitor-` Monitoring & Diagnostics (LOW-MEDIUM)
   - `advanced-` Advanced Features (LOW)

2. **Copy the template**:
   ```bash
   cp references/_template.md references/query-your-reference-name.md
   ```

3. **Fill in the content** following the template structure

4. **Validate and build**:
   ```bash
   npm run validate
   npm run build
   ```

5. **Review** the generated `AGENTS.md`

## Skill Structure

```
skills/supabase-postgres-best-practices/
├── SKILL.md           # Agent-facing skill manifest (Agent Skills spec)
├── AGENTS.md          # [GENERATED] Compiled references document
├── README.md          # This file
└── references/
    ├── _template.md      # Reference template
    ├── _sections.md      # Section definitions
    ├── _contributing.md  # Writing guidelines
    └── *.md              # Individual references

packages/skills-build/
├── src/               # Generic build system source
└── package.json       # NPM scripts
```

## Reference File Structure

See `references/_template.md` for the complete template. Key elements:

````markdown
---
title: Clear, Action-Oriented Title
impact: CRITICAL|HIGH|MEDIUM-HIGH|MEDIUM|LOW-MEDIUM|LOW
impactDescription: Quantified benefit (e.g., "10-100x faster")
tags: relevant, keywords
---

## [Title]

[1-2 sentence explanation]

**Incorrect (description):**

```sql
-- Comment explaining what's wrong
[Bad SQL example]
```
````

**Correct (description):**

```sql
-- Comment explaining why this is better
[Good SQL example]
```

```
## Writing Guidelines

See `references/_contributing.md` for detailed guidelines. Key principles:

1. **Show concrete transformations** - "Change X to Y", not abstract advice
2. **Error-first structure** - Show the problem before the solution
3. **Quantify impact** - Include specific metrics (10x faster, 50% smaller)
4. **Self-contained examples** - Complete, runnable SQL
5. **Semantic naming** - Use meaningful names (users, email), not (table1, col1)

## Impact Levels

| Level | Improvement | Examples |
|-------|-------------|----------|
| CRITICAL | 10-100x | Missing indexes, connection exhaustion |
| HIGH | 5-20x | Wrong index types, poor partitioning |
| MEDIUM-HIGH | 2-5x | N+1 queries, RLS optimization |
| MEDIUM | 1.5-3x | Redundant indexes, stale statistics |
| LOW-MEDIUM | 1.2-2x | VACUUM tuning, config tweaks |
| LOW | Incremental | Advanced patterns, edge cases |
```
```

## File: `skills/supabase-postgres-best-practices/SKILL.md`
```markdown
---
name: supabase-postgres-best-practices
description: Postgres performance optimization and best practices from Supabase. Use this skill when writing, reviewing, or optimizing Postgres queries, schema designs, or database configurations.
license: MIT
metadata:
  author: supabase
  version: "1.1.0"
  organization: Supabase
  date: January 2026
  abstract: Comprehensive Postgres performance optimization guide for developers using Supabase and Postgres. Contains performance rules across 8 categories, prioritized by impact from critical (query performance, connection management) to incremental (advanced features). Each rule includes detailed explanations, incorrect vs. correct SQL examples, query plan analysis, and specific performance metrics to guide automated optimization and code generation.
---

# Supabase Postgres Best Practices

Comprehensive performance optimization guide for Postgres, maintained by Supabase. Contains rules across 8 categories, prioritized by impact to guide automated query optimization and schema design.

## When to Apply

Reference these guidelines when:
- Writing SQL queries or designing schemas
- Implementing indexes or query optimization
- Reviewing database performance issues
- Configuring connection pooling or scaling
- Optimizing for Postgres-specific features
- Working with Row-Level Security (RLS)

## Rule Categories by Priority

| Priority | Category | Impact | Prefix |
|----------|----------|--------|--------|
| 1 | Query Performance | CRITICAL | `query-` |
| 2 | Connection Management | CRITICAL | `conn-` |
| 3 | Security & RLS | CRITICAL | `security-` |
| 4 | Schema Design | HIGH | `schema-` |
| 5 | Concurrency & Locking | MEDIUM-HIGH | `lock-` |
| 6 | Data Access Patterns | MEDIUM | `data-` |
| 7 | Monitoring & Diagnostics | LOW-MEDIUM | `monitor-` |
| 8 | Advanced Features | LOW | `advanced-` |

## How to Use

Read individual rule files for detailed explanations and SQL examples:

```
references/query-missing-indexes.md
references/schema-partial-indexes.md
references/_sections.md
```

Each rule file contains:
- Brief explanation of why it matters
- Incorrect SQL example with explanation
- Correct SQL example with explanation
- Optional EXPLAIN output or metrics
- Additional context and references
- Supabase-specific notes (when applicable)

## References

- https://www.postgresql.org/docs/current/
- https://supabase.com/docs
- https://wiki.postgresql.org/wiki/Performance_Optimization
- https://supabase.com/docs/guides/database/overview
- https://supabase.com/docs/guides/auth/row-level-security
```

## File: `skills/supabase-postgres-best-practices/references/_contributing.md`
```markdown
# Writing Guidelines for Postgres References

This document provides guidelines for creating effective Postgres best
practice references that work well with AI agents and LLMs.

## Key Principles

### 1. Concrete Transformation Patterns

Show exact SQL rewrites. Avoid philosophical advice.

**Good:** "Use `WHERE id = ANY(ARRAY[...])` instead of
`WHERE id IN (SELECT ...)`" **Bad:** "Design good schemas"

### 2. Error-First Structure

Always show the problematic pattern first, then the solution. This trains agents
to recognize anti-patterns.

```markdown
**Incorrect (sequential queries):** [bad example]

**Correct (batched query):** [good example]
```

### 3. Quantified Impact

Include specific metrics. Helps agents prioritize fixes.

**Good:** "10x faster queries", "50% smaller index", "Eliminates N+1" 
**Bad:** "Faster", "Better", "More efficient"

### 4. Self-Contained Examples

Examples should be complete and runnable (or close to it). Include `CREATE TABLE`
if context is needed.

```sql
-- Include table definition when needed for clarity
CREATE TABLE users (
  id bigint PRIMARY KEY,
  email text NOT NULL,
  deleted_at timestamptz
);

-- Now show the index
CREATE INDEX users_active_email_idx ON users(email) WHERE deleted_at IS NULL;
```

### 5. Semantic Naming

Use meaningful table/column names. Names carry intent for LLMs.

**Good:** `users`, `email`, `created_at`, `is_active`
**Bad:** `table1`, `col1`, `field`, `flag`

---

## Code Example Standards

### SQL Formatting

```sql
-- Use lowercase keywords, clear formatting
CREATE INDEX CONCURRENTLY users_email_idx
  ON users(email)
  WHERE deleted_at IS NULL;

-- Not cramped or ALL CAPS
CREATE INDEX CONCURRENTLY USERS_EMAIL_IDX ON USERS(EMAIL) WHERE DELETED_AT IS NULL;
```

### Comments

- Explain _why_, not _what_
- Highlight performance implications
- Point out common pitfalls

### Language Tags

- `sql` - Standard SQL queries
- `plpgsql` - Stored procedures/functions
- `typescript` - Application code (when needed)
- `python` - Application code (when needed)

---

## When to Include Application Code

**Default: SQL Only**

Most references should focus on pure SQL patterns. This keeps examples portable.

**Include Application Code When:**

- Connection pooling configuration
- Transaction management in application context
- ORM anti-patterns (N+1 in Prisma/TypeORM)
- Prepared statement usage

**Format for Mixed Examples:**

````markdown
**Incorrect (N+1 in application):**

```typescript
for (const user of users) {
  const posts = await db.query("SELECT * FROM posts WHERE user_id = $1", [
    user.id,
  ]);
}
```
````

**Correct (batch query):**

```typescript
const posts = await db.query("SELECT * FROM posts WHERE user_id = ANY($1)", [
  userIds,
]);
```

---

## Impact Level Guidelines

| Level | Improvement | Use When |
|-------|-------------|----------|
| **CRITICAL** | 10-100x | Missing indexes, connection exhaustion, sequential scans on large tables |
| **HIGH** | 5-20x | Wrong index types, poor partitioning, missing covering indexes |
| **MEDIUM-HIGH** | 2-5x | N+1 queries, inefficient pagination, RLS optimization |
| **MEDIUM** | 1.5-3x | Redundant indexes, query plan instability |
| **LOW-MEDIUM** | 1.2-2x | VACUUM tuning, configuration tweaks |
| **LOW** | Incremental | Advanced patterns, edge cases |

---

## Reference Standards

**Primary Sources:**

- Official Postgres documentation
- Supabase documentation
- Postgres wiki
- Established blogs (2ndQuadrant, Crunchy Data)

**Format:**

```markdown
Reference:
[Postgres Indexes](https://www.postgresql.org/docs/current/indexes.html)
```

---

## Review Checklist

Before submitting a reference:

- [ ] Title is clear and action-oriented
- [ ] Impact level matches the performance gain
- [ ] impactDescription includes quantification
- [ ] Explanation is concise (1-2 sentences)
- [ ] Has at least 1 **Incorrect** SQL example
- [ ] Has at least 1 **Correct** SQL example
- [ ] SQL uses semantic naming
- [ ] Comments explain _why_, not _what_
- [ ] Trade-offs mentioned if applicable
- [ ] Reference links included
- [ ] `npm run validate` passes
- [ ] `npm run build` generates correct output
```

## File: `skills/supabase-postgres-best-practices/references/_sections.md`
```markdown
# Section Definitions

This file defines the rule categories for Postgres best practices. Rules are automatically assigned to sections based on their filename prefix.

Take the examples below as pure demonstrative. Replace each section with the actual rule categories for Postgres best practices.

---

## 1. Query Performance (query)
**Impact:** CRITICAL
**Description:** Slow queries, missing indexes, inefficient query plans. The most common source of Postgres performance issues.

## 2. Connection Management (conn)
**Impact:** CRITICAL
**Description:** Connection pooling, limits, and serverless strategies. Critical for applications with high concurrency or serverless deployments.

## 3. Security & RLS (security)
**Impact:** CRITICAL
**Description:** Row-Level Security policies, privilege management, and authentication patterns.

## 4. Schema Design (schema)
**Impact:** HIGH
**Description:** Table design, index strategies, partitioning, and data type selection. Foundation for long-term performance.

## 5. Concurrency & Locking (lock)
**Impact:** MEDIUM-HIGH
**Description:** Transaction management, isolation levels, deadlock prevention, and lock contention patterns.

## 6. Data Access Patterns (data)
**Impact:** MEDIUM
**Description:** N+1 query elimination, batch operations, cursor-based pagination, and efficient data fetching.

## 7. Monitoring & Diagnostics (monitor)
**Impact:** LOW-MEDIUM
**Description:** Using pg_stat_statements, EXPLAIN ANALYZE, metrics collection, and performance diagnostics.

## 8. Advanced Features (advanced)
**Impact:** LOW
**Description:** Full-text search, JSONB optimization, PostGIS, extensions, and advanced Postgres features.
```

## File: `skills/supabase-postgres-best-practices/references/_template.md`
```markdown
---
title: Clear, Action-Oriented Title (e.g., "Use Partial Indexes for Filtered Queries")
impact: MEDIUM
impactDescription: 5-20x query speedup for filtered queries
tags: indexes, query-optimization, performance
---

## [Rule Title]

[1-2 sentence explanation of the problem and why it matters. Focus on performance impact.]

**Incorrect (describe the problem):**

```sql
-- Comment explaining what makes this slow/problematic
CREATE INDEX users_email_idx ON users(email);

SELECT * FROM users WHERE email = 'user@example.com' AND deleted_at IS NULL;
-- This scans deleted records unnecessarily
```

**Correct (describe the solution):**

```sql
-- Comment explaining why this is better
CREATE INDEX users_active_email_idx ON users(email) WHERE deleted_at IS NULL;

SELECT * FROM users WHERE email = 'user@example.com' AND deleted_at IS NULL;
-- Only indexes active users, 10x smaller index, faster queries
```

[Optional: Additional context, edge cases, or trade-offs]

Reference: [Postgres Docs](https://www.postgresql.org/docs/current/)
```

## File: `skills/supabase-postgres-best-practices/references/advanced-full-text-search.md`
```markdown
---
title: Use tsvector for Full-Text Search
impact: MEDIUM
impactDescription: 100x faster than LIKE, with ranking support
tags: full-text-search, tsvector, gin, search
---

## Use tsvector for Full-Text Search

LIKE with wildcards can't use indexes. Full-text search with tsvector is orders of magnitude faster.

**Incorrect (LIKE pattern matching):**

```sql
-- Cannot use index, scans all rows
select * from articles where content like '%postgresql%';

-- Case-insensitive makes it worse
select * from articles where lower(content) like '%postgresql%';
```

**Correct (full-text search with tsvector):**

```sql
-- Add tsvector column and index
alter table articles add column search_vector tsvector
  generated always as (to_tsvector('english', coalesce(title,'') || ' ' || coalesce(content,''))) stored;

create index articles_search_idx on articles using gin (search_vector);

-- Fast full-text search
select * from articles
where search_vector @@ to_tsquery('english', 'postgresql & performance');

-- With ranking
select *, ts_rank(search_vector, query) as rank
from articles, to_tsquery('english', 'postgresql') query
where search_vector @@ query
order by rank desc;
```

Search multiple terms:

```sql
-- AND: both terms required
to_tsquery('postgresql & performance')

-- OR: either term
to_tsquery('postgresql | mysql')

-- Prefix matching
to_tsquery('post:*')
```

Reference: [Full Text Search](https://supabase.com/docs/guides/database/full-text-search)
```

## File: `skills/supabase-postgres-best-practices/references/advanced-jsonb-indexing.md`
```markdown
---
title: Index JSONB Columns for Efficient Querying
impact: MEDIUM
impactDescription: 10-100x faster JSONB queries with proper indexing
tags: jsonb, gin, indexes, json
---

## Index JSONB Columns for Efficient Querying

JSONB queries without indexes scan the entire table. Use GIN indexes for containment queries.

**Incorrect (no index on JSONB):**

```sql
create table products (
  id bigint primary key,
  attributes jsonb
);

-- Full table scan for every query
select * from products where attributes @> '{"color": "red"}';
select * from products where attributes->>'brand' = 'Nike';
```

**Correct (GIN index for JSONB):**

```sql
-- GIN index for containment operators (@>, ?, ?&, ?|)
create index products_attrs_gin on products using gin (attributes);

-- Now containment queries use the index
select * from products where attributes @> '{"color": "red"}';

-- For specific key lookups, use expression index
create index products_brand_idx on products ((attributes->>'brand'));
select * from products where attributes->>'brand' = 'Nike';
```

Choose the right operator class:

```sql
-- jsonb_ops (default): supports all operators, larger index
create index idx1 on products using gin (attributes);

-- jsonb_path_ops: only @> operator, but 2-3x smaller index
create index idx2 on products using gin (attributes jsonb_path_ops);
```

Reference: [JSONB Indexes](https://www.postgresql.org/docs/current/datatype-json.html#JSON-INDEXING)
```

## File: `skills/supabase-postgres-best-practices/references/conn-idle-timeout.md`
```markdown
---
title: Configure Idle Connection Timeouts
impact: HIGH
impactDescription: Reclaim 30-50% of connection slots from idle clients
tags: connections, timeout, idle, resource-management
---

## Configure Idle Connection Timeouts

Idle connections waste resources. Configure timeouts to automatically reclaim them.

**Incorrect (connections held indefinitely):**

```sql
-- No timeout configured
show idle_in_transaction_session_timeout;  -- 0 (disabled)

-- Connections stay open forever, even when idle
select pid, state, state_change, query
from pg_stat_activity
where state = 'idle in transaction';
-- Shows transactions idle for hours, holding locks
```

**Correct (automatic cleanup of idle connections):**

```sql
-- Terminate connections idle in transaction after 30 seconds
alter system set idle_in_transaction_session_timeout = '30s';

-- Terminate completely idle connections after 10 minutes
alter system set idle_session_timeout = '10min';

-- Reload configuration
select pg_reload_conf();
```

For pooled connections, configure at the pooler level:

```ini
# pgbouncer.ini
server_idle_timeout = 60
client_idle_timeout = 300
```

Reference: [Connection Timeouts](https://www.postgresql.org/docs/current/runtime-config-client.html#GUC-IDLE-IN-TRANSACTION-SESSION-TIMEOUT)
```

## File: `skills/supabase-postgres-best-practices/references/conn-limits.md`
```markdown
---
title: Set Appropriate Connection Limits
impact: CRITICAL
impactDescription: Prevent database crashes and memory exhaustion
tags: connections, max-connections, limits, stability
---

## Set Appropriate Connection Limits

Too many connections exhaust memory and degrade performance. Set limits based on available resources.

**Incorrect (unlimited or excessive connections):**

```sql
-- Default max_connections = 100, but often increased blindly
show max_connections;  -- 500 (way too high for 4GB RAM)

-- Each connection uses 1-3MB RAM
-- 500 connections * 2MB = 1GB just for connections!
-- Out of memory errors under load
```

**Correct (calculate based on resources):**

```sql
-- Formula: max_connections = (RAM in MB / 5MB per connection) - reserved
-- For 4GB RAM: (4096 / 5) - 10 = ~800 theoretical max
-- But practically, 100-200 is better for query performance

-- Recommended settings for 4GB RAM
alter system set max_connections = 100;

-- Also set work_mem appropriately
-- work_mem * max_connections should not exceed 25% of RAM
alter system set work_mem = '8MB';  -- 8MB * 100 = 800MB max
```

Monitor connection usage:

```sql
select count(*), state from pg_stat_activity group by state;
```

Reference: [Database Connections](https://supabase.com/docs/guides/platform/performance#connection-management)
```

## File: `skills/supabase-postgres-best-practices/references/conn-pooling.md`
```markdown
---
title: Use Connection Pooling for All Applications
impact: CRITICAL
impactDescription: Handle 10-100x more concurrent users
tags: connection-pooling, pgbouncer, performance, scalability
---

## Use Connection Pooling for All Applications

Postgres connections are expensive (1-3MB RAM each). Without pooling, applications exhaust connections under load.

**Incorrect (new connection per request):**

```sql
-- Each request creates a new connection
-- Application code: db.connect() per request
-- Result: 500 concurrent users = 500 connections = crashed database

-- Check current connections
select count(*) from pg_stat_activity;  -- 487 connections!
```

**Correct (connection pooling):**

```sql
-- Use a pooler like PgBouncer between app and database
-- Application connects to pooler, pooler reuses a small pool to Postgres

-- Configure pool_size based on: (CPU cores * 2) + spindle_count
-- Example for 4 cores: pool_size = 10

-- Result: 500 concurrent users share 10 actual connections
select count(*) from pg_stat_activity;  -- 10 connections
```

Pool modes:

- **Transaction mode**: connection returned after each transaction (best for most apps)
- **Session mode**: connection held for entire session (needed for prepared statements, temp tables)

Reference: [Connection Pooling](https://supabase.com/docs/guides/database/connecting-to-postgres#connection-pooler)
```

## File: `skills/supabase-postgres-best-practices/references/conn-prepared-statements.md`
```markdown
---
title: Use Prepared Statements Correctly with Pooling
impact: HIGH
impactDescription: Avoid prepared statement conflicts in pooled environments
tags: prepared-statements, connection-pooling, transaction-mode
---

## Use Prepared Statements Correctly with Pooling

Prepared statements are tied to individual database connections. In transaction-mode pooling, connections are shared, causing conflicts.

**Incorrect (named prepared statements with transaction pooling):**

```sql
-- Named prepared statement
prepare get_user as select * from users where id = $1;

-- In transaction mode pooling, next request may get different connection
execute get_user(123);
-- ERROR: prepared statement "get_user" does not exist
```

**Correct (use unnamed statements or session mode):**

```sql
-- Option 1: Use unnamed prepared statements (most ORMs do this automatically)
-- The query is prepared and executed in a single protocol message

-- Option 2: Deallocate after use in transaction mode
prepare get_user as select * from users where id = $1;
execute get_user(123);
deallocate get_user;

-- Option 3: Use session mode pooling (port 5432 vs 6543)
-- Connection is held for entire session, prepared statements persist
```

Check your driver settings:

```sql
-- Many drivers use prepared statements by default
-- Node.js pg: { prepare: false } to disable
-- JDBC: prepareThreshold=0 to disable
```

Reference: [Prepared Statements with Pooling](https://supabase.com/docs/guides/database/connecting-to-postgres#connection-pool-modes)
```

## File: `skills/supabase-postgres-best-practices/references/data-batch-inserts.md`
```markdown
---
title: Batch INSERT Statements for Bulk Data
impact: MEDIUM
impactDescription: 10-50x faster bulk inserts
tags: batch, insert, bulk, performance, copy
---

## Batch INSERT Statements for Bulk Data

Individual INSERT statements have high overhead. Batch multiple rows in single statements or use COPY.

**Incorrect (individual inserts):**

```sql
-- Each insert is a separate transaction and round trip
insert into events (user_id, action) values (1, 'click');
insert into events (user_id, action) values (1, 'view');
insert into events (user_id, action) values (2, 'click');
-- ... 1000 more individual inserts

-- 1000 inserts = 1000 round trips = slow
```

**Correct (batch insert):**

```sql
-- Multiple rows in single statement
insert into events (user_id, action) values
  (1, 'click'),
  (1, 'view'),
  (2, 'click'),
  -- ... up to ~1000 rows per batch
  (999, 'view');

-- One round trip for 1000 rows
```

For large imports, use COPY:

```sql
-- COPY is fastest for bulk loading
copy events (user_id, action, created_at)
from '/path/to/data.csv'
with (format csv, header true);

-- Or from stdin in application
copy events (user_id, action) from stdin with (format csv);
1,click
1,view
2,click
\.
```

Reference: [COPY](https://www.postgresql.org/docs/current/sql-copy.html)
```

## File: `skills/supabase-postgres-best-practices/references/data-n-plus-one.md`
```markdown
---
title: Eliminate N+1 Queries with Batch Loading
impact: MEDIUM-HIGH
impactDescription: 10-100x fewer database round trips
tags: n-plus-one, batch, performance, queries
---

## Eliminate N+1 Queries with Batch Loading

N+1 queries execute one query per item in a loop. Batch them into a single query using arrays or JOINs.

**Incorrect (N+1 queries):**

```sql
-- First query: get all users
select id from users where active = true;  -- Returns 100 IDs

-- Then N queries, one per user
select * from orders where user_id = 1;
select * from orders where user_id = 2;
select * from orders where user_id = 3;
-- ... 97 more queries!

-- Total: 101 round trips to database
```

**Correct (single batch query):**

```sql
-- Collect IDs and query once with ANY
select * from orders where user_id = any(array[1, 2, 3, ...]);

-- Or use JOIN instead of loop
select u.id, u.name, o.*
from users u
left join orders o on o.user_id = u.id
where u.active = true;

-- Total: 1 round trip
```

Application pattern:

```sql
-- Instead of looping in application code:
-- for user in users: db.query("SELECT * FROM orders WHERE user_id = $1", user.id)

-- Pass array parameter:
select * from orders where user_id = any($1::bigint[]);
-- Application passes: [1, 2, 3, 4, 5, ...]
```

Reference: [N+1 Query Problem](https://supabase.com/docs/guides/database/query-optimization)
```

## File: `skills/supabase-postgres-best-practices/references/data-pagination.md`
```markdown
---
title: Use Cursor-Based Pagination Instead of OFFSET
impact: MEDIUM-HIGH
impactDescription: Consistent O(1) performance regardless of page depth
tags: pagination, cursor, keyset, offset, performance
---

## Use Cursor-Based Pagination Instead of OFFSET

OFFSET-based pagination scans all skipped rows, getting slower on deeper pages. Cursor pagination is O(1).

**Incorrect (OFFSET pagination):**

```sql
-- Page 1: scans 20 rows
select * from products order by id limit 20 offset 0;

-- Page 100: scans 2000 rows to skip 1980
select * from products order by id limit 20 offset 1980;

-- Page 10000: scans 200,000 rows!
select * from products order by id limit 20 offset 199980;
```

**Correct (cursor/keyset pagination):**

```sql
-- Page 1: get first 20
select * from products order by id limit 20;
-- Application stores last_id = 20

-- Page 2: start after last ID
select * from products where id > 20 order by id limit 20;
-- Uses index, always fast regardless of page depth

-- Page 10000: same speed as page 1
select * from products where id > 199980 order by id limit 20;
```

For multi-column sorting:

```sql
-- Cursor must include all sort columns
select * from products
where (created_at, id) > ('2024-01-15 10:00:00', 12345)
order by created_at, id
limit 20;
```

Reference: [Pagination](https://supabase.com/docs/guides/database/pagination)
```

## File: `skills/supabase-postgres-best-practices/references/data-upsert.md`
```markdown
---
title: Use UPSERT for Insert-or-Update Operations
impact: MEDIUM
impactDescription: Atomic operation, eliminates race conditions
tags: upsert, on-conflict, insert, update
---

## Use UPSERT for Insert-or-Update Operations

Using separate SELECT-then-INSERT/UPDATE creates race conditions. Use INSERT ... ON CONFLICT for atomic upserts.

**Incorrect (check-then-insert race condition):**

```sql
-- Race condition: two requests check simultaneously
select * from settings where user_id = 123 and key = 'theme';
-- Both find nothing

-- Both try to insert
insert into settings (user_id, key, value) values (123, 'theme', 'dark');
-- One succeeds, one fails with duplicate key error!
```

**Correct (atomic UPSERT):**

```sql
-- Single atomic operation
insert into settings (user_id, key, value)
values (123, 'theme', 'dark')
on conflict (user_id, key)
do update set value = excluded.value, updated_at = now();

-- Returns the inserted/updated row
insert into settings (user_id, key, value)
values (123, 'theme', 'dark')
on conflict (user_id, key)
do update set value = excluded.value
returning *;
```

Insert-or-ignore pattern:

```sql
-- Insert only if not exists (no update)
insert into page_views (page_id, user_id)
values (1, 123)
on conflict (page_id, user_id) do nothing;
```

Reference: [INSERT ON CONFLICT](https://www.postgresql.org/docs/current/sql-insert.html#SQL-ON-CONFLICT)
```

## File: `skills/supabase-postgres-best-practices/references/lock-advisory.md`
```markdown
---
title: Use Advisory Locks for Application-Level Locking
impact: MEDIUM
impactDescription: Efficient coordination without row-level lock overhead
tags: advisory-locks, coordination, application-locks
---

## Use Advisory Locks for Application-Level Locking

Advisory locks provide application-level coordination without requiring database rows to lock.

**Incorrect (creating rows just for locking):**

```sql
-- Creating dummy rows to lock on
create table resource_locks (
  resource_name text primary key
);

insert into resource_locks values ('report_generator');

-- Lock by selecting the row
select * from resource_locks where resource_name = 'report_generator' for update;
```

**Correct (advisory locks):**

```sql
-- Session-level advisory lock (released on disconnect or unlock)
select pg_advisory_lock(hashtext('report_generator'));
-- ... do exclusive work ...
select pg_advisory_unlock(hashtext('report_generator'));

-- Transaction-level lock (released on commit/rollback)
begin;
select pg_advisory_xact_lock(hashtext('daily_report'));
-- ... do work ...
commit;  -- Lock automatically released
```

Try-lock for non-blocking operations:

```sql
-- Returns immediately with true/false instead of waiting
select pg_try_advisory_lock(hashtext('resource_name'));

-- Use in application
if (acquired) {
  -- Do work
  select pg_advisory_unlock(hashtext('resource_name'));
} else {
  -- Skip or retry later
}
```

Reference: [Advisory Locks](https://www.postgresql.org/docs/current/explicit-locking.html#ADVISORY-LOCKS)
```

## File: `skills/supabase-postgres-best-practices/references/lock-deadlock-prevention.md`
```markdown
---
title: Prevent Deadlocks with Consistent Lock Ordering
impact: MEDIUM-HIGH
impactDescription: Eliminate deadlock errors, improve reliability
tags: deadlocks, locking, transactions, ordering
---

## Prevent Deadlocks with Consistent Lock Ordering

Deadlocks occur when transactions lock resources in different orders. Always
acquire locks in a consistent order.

**Incorrect (inconsistent lock ordering):**

```sql
-- Transaction A                    -- Transaction B
begin;                              begin;
update accounts                     update accounts
set balance = balance - 100         set balance = balance - 50
where id = 1;                       where id = 2;  -- B locks row 2

update accounts                     update accounts
set balance = balance + 100         set balance = balance + 50
where id = 2;  -- A waits for B     where id = 1;  -- B waits for A

-- DEADLOCK! Both waiting for each other
```

**Correct (lock rows in consistent order first):**

```sql
-- Explicitly acquire locks in ID order before updating
begin;
select * from accounts where id in (1, 2) order by id for update;

-- Now perform updates in any order - locks already held
update accounts set balance = balance - 100 where id = 1;
update accounts set balance = balance + 100 where id = 2;
commit;
```

Alternative: use a single statement to update atomically:

```sql
-- Single statement acquires all locks atomically
begin;
update accounts
set balance = balance + case id
  when 1 then -100
  when 2 then 100
end
where id in (1, 2);
commit;
```

Detect deadlocks in logs:

```sql
-- Check for recent deadlocks
select * from pg_stat_database where deadlocks > 0;

-- Enable deadlock logging
set log_lock_waits = on;
set deadlock_timeout = '1s';
```

Reference:
[Deadlocks](https://www.postgresql.org/docs/current/explicit-locking.html#LOCKING-DEADLOCKS)
```

## File: `skills/supabase-postgres-best-practices/references/lock-short-transactions.md`
```markdown
---
title: Keep Transactions Short to Reduce Lock Contention
impact: MEDIUM-HIGH
impactDescription: 3-5x throughput improvement, fewer deadlocks
tags: transactions, locking, contention, performance
---

## Keep Transactions Short to Reduce Lock Contention

Long-running transactions hold locks that block other queries. Keep transactions as short as possible.

**Incorrect (long transaction with external calls):**

```sql
begin;
select * from orders where id = 1 for update;  -- Lock acquired

-- Application makes HTTP call to payment API (2-5 seconds)
-- Other queries on this row are blocked!

update orders set status = 'paid' where id = 1;
commit;  -- Lock held for entire duration
```

**Correct (minimal transaction scope):**

```sql
-- Validate data and call APIs outside transaction
-- Application: response = await paymentAPI.charge(...)

-- Only hold lock for the actual update
begin;
update orders
set status = 'paid', payment_id = $1
where id = $2 and status = 'pending'
returning *;
commit;  -- Lock held for milliseconds
```

Use `statement_timeout` to prevent runaway transactions:

```sql
-- Abort queries running longer than 30 seconds
set statement_timeout = '30s';

-- Or per-session
set local statement_timeout = '5s';
```

Reference: [Transaction Management](https://www.postgresql.org/docs/current/tutorial-transactions.html)
```

## File: `skills/supabase-postgres-best-practices/references/lock-skip-locked.md`
```markdown
---
title: Use SKIP LOCKED for Non-Blocking Queue Processing
impact: MEDIUM-HIGH
impactDescription: 10x throughput for worker queues
tags: skip-locked, queue, workers, concurrency
---

## Use SKIP LOCKED for Non-Blocking Queue Processing

When multiple workers process a queue, SKIP LOCKED allows workers to process different rows without waiting.

**Incorrect (workers block each other):**

```sql
-- Worker 1 and Worker 2 both try to get next job
begin;
select * from jobs where status = 'pending' order by created_at limit 1 for update;
-- Worker 2 waits for Worker 1's lock to release!
```

**Correct (SKIP LOCKED for parallel processing):**

```sql
-- Each worker skips locked rows and gets the next available
begin;
select * from jobs
where status = 'pending'
order by created_at
limit 1
for update skip locked;

-- Worker 1 gets job 1, Worker 2 gets job 2 (no waiting)

update jobs set status = 'processing' where id = $1;
commit;
```

Complete queue pattern:

```sql
-- Atomic claim-and-update in one statement
update jobs
set status = 'processing', worker_id = $1, started_at = now()
where id = (
  select id from jobs
  where status = 'pending'
  order by created_at
  limit 1
  for update skip locked
)
returning *;
```

Reference: [SELECT FOR UPDATE SKIP LOCKED](https://www.postgresql.org/docs/current/sql-select.html#SQL-FOR-UPDATE-SHARE)
```

## File: `skills/supabase-postgres-best-practices/references/monitor-explain-analyze.md`
```markdown
---
title: Use EXPLAIN ANALYZE to Diagnose Slow Queries
impact: LOW-MEDIUM
impactDescription: Identify exact bottlenecks in query execution
tags: explain, analyze, diagnostics, query-plan
---

## Use EXPLAIN ANALYZE to Diagnose Slow Queries

EXPLAIN ANALYZE executes the query and shows actual timings, revealing the true performance bottlenecks.

**Incorrect (guessing at performance issues):**

```sql
-- Query is slow, but why?
select * from orders where customer_id = 123 and status = 'pending';
-- "It must be missing an index" - but which one?
```

**Correct (use EXPLAIN ANALYZE):**

```sql
explain (analyze, buffers, format text)
select * from orders where customer_id = 123 and status = 'pending';

-- Output reveals the issue:
-- Seq Scan on orders (cost=0.00..25000.00 rows=50 width=100) (actual time=0.015..450.123 rows=50 loops=1)
--   Filter: ((customer_id = 123) AND (status = 'pending'::text))
--   Rows Removed by Filter: 999950
--   Buffers: shared hit=5000 read=15000
-- Planning Time: 0.150 ms
-- Execution Time: 450.500 ms
```

Key things to look for:

```sql
-- Seq Scan on large tables = missing index
-- Rows Removed by Filter = poor selectivity or missing index
-- Buffers: read >> hit = data not cached, needs more memory
-- Nested Loop with high loops = consider different join strategy
-- Sort Method: external merge = work_mem too low
```

Reference: [EXPLAIN](https://supabase.com/docs/guides/database/inspect)
```

## File: `skills/supabase-postgres-best-practices/references/monitor-pg-stat-statements.md`
```markdown
---
title: Enable pg_stat_statements for Query Analysis
impact: LOW-MEDIUM
impactDescription: Identify top resource-consuming queries
tags: pg-stat-statements, monitoring, statistics, performance
---

## Enable pg_stat_statements for Query Analysis

pg_stat_statements tracks execution statistics for all queries, helping identify slow and frequent queries.

**Incorrect (no visibility into query patterns):**

```sql
-- Database is slow, but which queries are the problem?
-- No way to know without pg_stat_statements
```

**Correct (enable and query pg_stat_statements):**

```sql
-- Enable the extension
create extension if not exists pg_stat_statements;

-- Find slowest queries by total time
select
  calls,
  round(total_exec_time::numeric, 2) as total_time_ms,
  round(mean_exec_time::numeric, 2) as mean_time_ms,
  query
from pg_stat_statements
order by total_exec_time desc
limit 10;

-- Find most frequent queries
select calls, query
from pg_stat_statements
order by calls desc
limit 10;

-- Reset statistics after optimization
select pg_stat_statements_reset();
```

Key metrics to monitor:

```sql
-- Queries with high mean time (candidates for optimization)
select query, mean_exec_time, calls
from pg_stat_statements
where mean_exec_time > 100  -- > 100ms average
order by mean_exec_time desc;
```

Reference: [pg_stat_statements](https://supabase.com/docs/guides/database/extensions/pg_stat_statements)
```

## File: `skills/supabase-postgres-best-practices/references/monitor-vacuum-analyze.md`
```markdown
---
title: Maintain Table Statistics with VACUUM and ANALYZE
impact: MEDIUM
impactDescription: 2-10x better query plans with accurate statistics
tags: vacuum, analyze, statistics, maintenance, autovacuum
---

## Maintain Table Statistics with VACUUM and ANALYZE

Outdated statistics cause the query planner to make poor decisions. VACUUM reclaims space, ANALYZE updates statistics.

**Incorrect (stale statistics):**

```sql
-- Table has 1M rows but stats say 1000
-- Query planner chooses wrong strategy
explain select * from orders where status = 'pending';
-- Shows: Seq Scan (because stats show small table)
-- Actually: Index Scan would be much faster
```

**Correct (maintain fresh statistics):**

```sql
-- Manually analyze after large data changes
analyze orders;

-- Analyze specific columns used in WHERE clauses
analyze orders (status, created_at);

-- Check when tables were last analyzed
select
  relname,
  last_vacuum,
  last_autovacuum,
  last_analyze,
  last_autoanalyze
from pg_stat_user_tables
order by last_analyze nulls first;
```

Autovacuum tuning for busy tables:

```sql
-- Increase frequency for high-churn tables
alter table orders set (
  autovacuum_vacuum_scale_factor = 0.05,     -- Vacuum at 5% dead tuples (default 20%)
  autovacuum_analyze_scale_factor = 0.02     -- Analyze at 2% changes (default 10%)
);

-- Check autovacuum status
select * from pg_stat_progress_vacuum;
```

Reference: [VACUUM](https://supabase.com/docs/guides/database/database-size#vacuum-operations)
```

## File: `skills/supabase-postgres-best-practices/references/query-composite-indexes.md`
```markdown
---
title: Create Composite Indexes for Multi-Column Queries
impact: HIGH
impactDescription: 5-10x faster multi-column queries
tags: indexes, composite-index, multi-column, query-optimization
---

## Create Composite Indexes for Multi-Column Queries

When queries filter on multiple columns, a composite index is more efficient than separate single-column indexes.

**Incorrect (separate indexes require bitmap scan):**

```sql
-- Two separate indexes
create index orders_status_idx on orders (status);
create index orders_created_idx on orders (created_at);

-- Query must combine both indexes (slower)
select * from orders where status = 'pending' and created_at > '2024-01-01';
```

**Correct (composite index):**

```sql
-- Single composite index (leftmost column first for equality checks)
create index orders_status_created_idx on orders (status, created_at);

-- Query uses one efficient index scan
select * from orders where status = 'pending' and created_at > '2024-01-01';
```

**Column order matters** - place equality columns first, range columns last:

```sql
-- Good: status (=) before created_at (>)
create index idx on orders (status, created_at);

-- Works for: WHERE status = 'pending'
-- Works for: WHERE status = 'pending' AND created_at > '2024-01-01'
-- Does NOT work for: WHERE created_at > '2024-01-01' (leftmost prefix rule)
```

Reference: [Multicolumn Indexes](https://www.postgresql.org/docs/current/indexes-multicolumn.html)
```

## File: `skills/supabase-postgres-best-practices/references/query-covering-indexes.md`
```markdown
---
title: Use Covering Indexes to Avoid Table Lookups
impact: MEDIUM-HIGH
impactDescription: 2-5x faster queries by eliminating heap fetches
tags: indexes, covering-index, include, index-only-scan
---

## Use Covering Indexes to Avoid Table Lookups

Covering indexes include all columns needed by a query, enabling index-only scans that skip the table entirely.

**Incorrect (index scan + heap fetch):**

```sql
create index users_email_idx on users (email);

-- Must fetch name and created_at from table heap
select email, name, created_at from users where email = 'user@example.com';
```

**Correct (index-only scan with INCLUDE):**

```sql
-- Include non-searchable columns in the index
create index users_email_idx on users (email) include (name, created_at);

-- All columns served from index, no table access needed
select email, name, created_at from users where email = 'user@example.com';
```

Use INCLUDE for columns you SELECT but don't filter on:

```sql
-- Searching by status, but also need customer_id and total
create index orders_status_idx on orders (status) include (customer_id, total);

select status, customer_id, total from orders where status = 'shipped';
```

Reference: [Index-Only Scans](https://www.postgresql.org/docs/current/indexes-index-only-scans.html)
```

## File: `skills/supabase-postgres-best-practices/references/query-index-types.md`
```markdown
---
title: Choose the Right Index Type for Your Data
impact: HIGH
impactDescription: 10-100x improvement with correct index type
tags: indexes, btree, gin, gist, brin, hash, index-types
---

## Choose the Right Index Type for Your Data

Different index types excel at different query patterns. The default B-tree isn't always optimal.

**Incorrect (B-tree for JSONB containment):**

```sql
-- B-tree cannot optimize containment operators
create index products_attrs_idx on products (attributes);
select * from products where attributes @> '{"color": "red"}';
-- Full table scan - B-tree doesn't support @> operator
```

**Correct (GIN for JSONB):**

```sql
-- GIN supports @>, ?, ?&, ?| operators
create index products_attrs_idx on products using gin (attributes);
select * from products where attributes @> '{"color": "red"}';
```

Index type guide:

```sql
-- B-tree (default): =, <, >, BETWEEN, IN, IS NULL
create index users_created_idx on users (created_at);

-- GIN: arrays, JSONB, full-text search
create index posts_tags_idx on posts using gin (tags);

-- GiST: geometric data, range types, nearest-neighbor (KNN) queries
create index locations_idx on places using gist (location);

-- BRIN: large time-series tables (10-100x smaller)
create index events_time_idx on events using brin (created_at);

-- Hash: equality-only (slightly faster than B-tree for =)
create index sessions_token_idx on sessions using hash (token);
```

Reference: [Index Types](https://www.postgresql.org/docs/current/indexes-types.html)
```

## File: `skills/supabase-postgres-best-practices/references/query-missing-indexes.md`
```markdown
---
title: Add Indexes on WHERE and JOIN Columns
impact: CRITICAL
impactDescription: 100-1000x faster queries on large tables
tags: indexes, performance, sequential-scan, query-optimization
---

## Add Indexes on WHERE and JOIN Columns

Queries filtering or joining on unindexed columns cause full table scans, which become exponentially slower as tables grow.

**Incorrect (sequential scan on large table):**

```sql
-- No index on customer_id causes full table scan
select * from orders where customer_id = 123;

-- EXPLAIN shows: Seq Scan on orders (cost=0.00..25000.00 rows=100 width=85)
```

**Correct (index scan):**

```sql
-- Create index on frequently filtered column
create index orders_customer_id_idx on orders (customer_id);

select * from orders where customer_id = 123;

-- EXPLAIN shows: Index Scan using orders_customer_id_idx (cost=0.42..8.44 rows=100 width=85)
```

For JOIN columns, always index the foreign key side:

```sql
-- Index the referencing column
create index orders_customer_id_idx on orders (customer_id);

select c.name, o.total
from customers c
join orders o on o.customer_id = c.id;
```

Reference: [Query Optimization](https://supabase.com/docs/guides/database/query-optimization)
```

## File: `skills/supabase-postgres-best-practices/references/query-partial-indexes.md`
```markdown
---
title: Use Partial Indexes for Filtered Queries
impact: HIGH
impactDescription: 5-20x smaller indexes, faster writes and queries
tags: indexes, partial-index, query-optimization, storage
---

## Use Partial Indexes for Filtered Queries

Partial indexes only include rows matching a WHERE condition, making them smaller and faster when queries consistently filter on the same condition.

**Incorrect (full index includes irrelevant rows):**

```sql
-- Index includes all rows, even soft-deleted ones
create index users_email_idx on users (email);

-- Query always filters active users
select * from users where email = 'user@example.com' and deleted_at is null;
```

**Correct (partial index matches query filter):**

```sql
-- Index only includes active users
create index users_active_email_idx on users (email)
where deleted_at is null;

-- Query uses the smaller, faster index
select * from users where email = 'user@example.com' and deleted_at is null;
```

Common use cases for partial indexes:

```sql
-- Only pending orders (status rarely changes once completed)
create index orders_pending_idx on orders (created_at)
where status = 'pending';

-- Only non-null values
create index products_sku_idx on products (sku)
where sku is not null;
```

Reference: [Partial Indexes](https://www.postgresql.org/docs/current/indexes-partial.html)
```

## File: `skills/supabase-postgres-best-practices/references/schema-constraints.md`
```markdown
---
title: Add Constraints Safely in Migrations
impact: HIGH
impactDescription: Prevents migration failures and enables idempotent schema changes
tags: constraints, migrations, schema, alter-table
---

## Add Constraints Safely in Migrations

PostgreSQL does not support `ADD CONSTRAINT IF NOT EXISTS`. Migrations using this syntax will fail.

**Incorrect (causes syntax error):**

```sql
-- ERROR: syntax error at or near "not" (SQLSTATE 42601)
alter table public.profiles
add constraint if not exists profiles_birthchart_id_unique unique (birthchart_id);
```

**Correct (idempotent constraint creation):**

```sql
-- Use DO block to check before adding
do $$
begin
  if not exists (
    select 1 from pg_constraint
    where conname = 'profiles_birthchart_id_unique'
    and conrelid = 'public.profiles'::regclass
  ) then
    alter table public.profiles
    add constraint profiles_birthchart_id_unique unique (birthchart_id);
  end if;
end $$;
```

For all constraint types:

```sql
-- Check constraints
do $$
begin
  if not exists (
    select 1 from pg_constraint
    where conname = 'check_age_positive'
  ) then
    alter table users add constraint check_age_positive check (age > 0);
  end if;
end $$;

-- Foreign keys
do $$
begin
  if not exists (
    select 1 from pg_constraint
    where conname = 'profiles_birthchart_id_fkey'
  ) then
    alter table profiles
    add constraint profiles_birthchart_id_fkey
    foreign key (birthchart_id) references birthcharts(id);
  end if;
end $$;
```

Check if constraint exists:

```sql
-- Query to check constraint existence
select conname, contype, pg_get_constraintdef(oid)
from pg_constraint
where conrelid = 'public.profiles'::regclass;

-- contype values:
-- 'p' = PRIMARY KEY
-- 'f' = FOREIGN KEY
-- 'u' = UNIQUE
-- 'c' = CHECK
```

Reference: [Constraints](https://www.postgresql.org/docs/current/ddl-constraints.html)
```

## File: `skills/supabase-postgres-best-practices/references/schema-data-types.md`
```markdown
---
title: Choose Appropriate Data Types
impact: HIGH
impactDescription: 50% storage reduction, faster comparisons
tags: data-types, schema, storage, performance
---

## Choose Appropriate Data Types

Using the right data types reduces storage, improves query performance, and prevents bugs.

**Incorrect (wrong data types):**

```sql
create table users (
  id int,                    -- Will overflow at 2.1 billion
  email varchar(255),        -- Unnecessary length limit
  created_at timestamp,      -- Missing timezone info
  is_active varchar(5),      -- String for boolean
  price varchar(20)          -- String for numeric
);
```

**Correct (appropriate data types):**

```sql
create table users (
  id bigint generated always as identity primary key,  -- 9 quintillion max
  email text,                     -- No artificial limit, same performance as varchar
  created_at timestamptz,         -- Always store timezone-aware timestamps
  is_active boolean default true, -- 1 byte vs variable string length
  price numeric(10,2)             -- Exact decimal arithmetic
);
```

Key guidelines:

```sql
-- IDs: use bigint, not int (future-proofing)
-- Strings: use text, not varchar(n) unless constraint needed
-- Time: use timestamptz, not timestamp
-- Money: use numeric, not float (precision matters)
-- Enums: use text with check constraint or create enum type
```

Reference: [Data Types](https://www.postgresql.org/docs/current/datatype.html)
```

## File: `skills/supabase-postgres-best-practices/references/schema-foreign-key-indexes.md`
```markdown
---
title: Index Foreign Key Columns
impact: HIGH
impactDescription: 10-100x faster JOINs and CASCADE operations
tags: foreign-key, indexes, joins, schema
---

## Index Foreign Key Columns

Postgres does not automatically index foreign key columns. Missing indexes cause slow JOINs and CASCADE operations.

**Incorrect (unindexed foreign key):**

```sql
create table orders (
  id bigint generated always as identity primary key,
  customer_id bigint references customers(id) on delete cascade,
  total numeric(10,2)
);

-- No index on customer_id!
-- JOINs and ON DELETE CASCADE both require full table scan
select * from orders where customer_id = 123;  -- Seq Scan
delete from customers where id = 123;          -- Locks table, scans all orders
```

**Correct (indexed foreign key):**

```sql
create table orders (
  id bigint generated always as identity primary key,
  customer_id bigint references customers(id) on delete cascade,
  total numeric(10,2)
);

-- Always index the FK column
create index orders_customer_id_idx on orders (customer_id);

-- Now JOINs and cascades are fast
select * from orders where customer_id = 123;  -- Index Scan
delete from customers where id = 123;          -- Uses index, fast cascade
```

Find missing FK indexes:

```sql
select
  conrelid::regclass as table_name,
  a.attname as fk_column
from pg_constraint c
join pg_attribute a on a.attrelid = c.conrelid and a.attnum = any(c.conkey)
where c.contype = 'f'
  and not exists (
    select 1 from pg_index i
    where i.indrelid = c.conrelid and a.attnum = any(i.indkey)
  );
```

Reference: [Foreign Keys](https://www.postgresql.org/docs/current/ddl-constraints.html#DDL-CONSTRAINTS-FK)
```

## File: `skills/supabase-postgres-best-practices/references/schema-lowercase-identifiers.md`
```markdown
---
title: Use Lowercase Identifiers for Compatibility
impact: MEDIUM
impactDescription: Avoid case-sensitivity bugs with tools, ORMs, and AI assistants
tags: naming, identifiers, case-sensitivity, schema, conventions
---

## Use Lowercase Identifiers for Compatibility

PostgreSQL folds unquoted identifiers to lowercase. Quoted mixed-case identifiers require quotes forever and cause issues with tools, ORMs, and AI assistants that may not recognize them.

**Incorrect (mixed-case identifiers):**

```sql
-- Quoted identifiers preserve case but require quotes everywhere
CREATE TABLE "Users" (
  "userId" bigint PRIMARY KEY,
  "firstName" text,
  "lastName" text
);

-- Must always quote or queries fail
SELECT "firstName" FROM "Users" WHERE "userId" = 1;

-- This fails - Users becomes users without quotes
SELECT firstName FROM Users;
-- ERROR: relation "users" does not exist
```

**Correct (lowercase snake_case):**

```sql
-- Unquoted lowercase identifiers are portable and tool-friendly
CREATE TABLE users (
  user_id bigint PRIMARY KEY,
  first_name text,
  last_name text
);

-- Works without quotes, recognized by all tools
SELECT first_name FROM users WHERE user_id = 1;
```

Common sources of mixed-case identifiers:

```sql
-- ORMs often generate quoted camelCase - configure them to use snake_case
-- Migrations from other databases may preserve original casing
-- Some GUI tools quote identifiers by default - disable this

-- If stuck with mixed-case, create views as a compatibility layer
CREATE VIEW users AS SELECT "userId" AS user_id, "firstName" AS first_name FROM "Users";
```

Reference: [Identifiers and Key Words](https://www.postgresql.org/docs/current/sql-syntax-lexical.html#SQL-SYNTAX-IDENTIFIERS)
```

## File: `skills/supabase-postgres-best-practices/references/schema-partitioning.md`
```markdown
---
title: Partition Large Tables for Better Performance
impact: MEDIUM-HIGH
impactDescription: 5-20x faster queries and maintenance on large tables
tags: partitioning, large-tables, time-series, performance
---

## Partition Large Tables for Better Performance

Partitioning splits a large table into smaller pieces, improving query performance and maintenance operations.

**Incorrect (single large table):**

```sql
create table events (
  id bigint generated always as identity,
  created_at timestamptz,
  data jsonb
);

-- 500M rows, queries scan everything
select * from events where created_at > '2024-01-01';  -- Slow
vacuum events;  -- Takes hours, locks table
```

**Correct (partitioned by time range):**

```sql
create table events (
  id bigint generated always as identity,
  created_at timestamptz not null,
  data jsonb
) partition by range (created_at);

-- Create partitions for each month
create table events_2024_01 partition of events
  for values from ('2024-01-01') to ('2024-02-01');

create table events_2024_02 partition of events
  for values from ('2024-02-01') to ('2024-03-01');

-- Queries only scan relevant partitions
select * from events where created_at > '2024-01-15';  -- Only scans events_2024_01+

-- Drop old data instantly
drop table events_2023_01;  -- Instant vs DELETE taking hours
```

When to partition:

- Tables > 100M rows
- Time-series data with date-based queries
- Need to efficiently drop old data

Reference: [Table Partitioning](https://www.postgresql.org/docs/current/ddl-partitioning.html)
```

## File: `skills/supabase-postgres-best-practices/references/schema-primary-keys.md`
```markdown
---
title: Select Optimal Primary Key Strategy
impact: HIGH
impactDescription: Better index locality, reduced fragmentation
tags: primary-key, identity, uuid, serial, schema
---

## Select Optimal Primary Key Strategy

Primary key choice affects insert performance, index size, and replication
efficiency.

**Incorrect (problematic PK choices):**

```sql
-- identity is the SQL-standard approach
create table users (
  id serial primary key  -- Works, but IDENTITY is recommended
);

-- Random UUIDs (v4) cause index fragmentation
create table orders (
  id uuid default gen_random_uuid() primary key  -- UUIDv4 = random = scattered inserts
);
```

**Correct (optimal PK strategies):**

```sql
-- Use IDENTITY for sequential IDs (SQL-standard, best for most cases)
create table users (
  id bigint generated always as identity primary key
);

-- For distributed systems needing UUIDs, use UUIDv7 (time-ordered)
-- Requires pg_uuidv7 extension: create extension pg_uuidv7;
create table orders (
  id uuid default uuid_generate_v7() primary key  -- Time-ordered, no fragmentation
);

-- Alternative: time-prefixed IDs for sortable, distributed IDs (no extension needed)
create table events (
  id text default concat(
    to_char(now() at time zone 'utc', 'YYYYMMDDHH24MISSMS'),
    gen_random_uuid()::text
  ) primary key
);
```

Guidelines:

- Single database: `bigint identity` (sequential, 8 bytes, SQL-standard)
- Distributed/exposed IDs: UUIDv7 (requires pg_uuidv7) or ULID (time-ordered, no
  fragmentation)
- `serial` works but `identity` is SQL-standard and preferred for new
  applications
- Avoid random UUIDs (v4) as primary keys on large tables (causes index
  fragmentation)

Reference:
[Identity Columns](https://www.postgresql.org/docs/current/sql-createtable.html#SQL-CREATETABLE-PARMS-GENERATED-IDENTITY)
```

## File: `skills/supabase-postgres-best-practices/references/security-privileges.md`
```markdown
---
title: Apply Principle of Least Privilege
impact: MEDIUM
impactDescription: Reduced attack surface, better audit trail
tags: privileges, security, roles, permissions
---

## Apply Principle of Least Privilege

Grant only the minimum permissions required. Never use superuser for application queries.

**Incorrect (overly broad permissions):**

```sql
-- Application uses superuser connection
-- Or grants ALL to application role
grant all privileges on all tables in schema public to app_user;
grant all privileges on all sequences in schema public to app_user;

-- Any SQL injection becomes catastrophic
-- drop table users; cascades to everything
```

**Correct (minimal, specific grants):**

```sql
-- Create role with no default privileges
create role app_readonly nologin;

-- Grant only SELECT on specific tables
grant usage on schema public to app_readonly;
grant select on public.products, public.categories to app_readonly;

-- Create role for writes with limited scope
create role app_writer nologin;
grant usage on schema public to app_writer;
grant select, insert, update on public.orders to app_writer;
grant usage on sequence orders_id_seq to app_writer;
-- No DELETE permission

-- Login role inherits from these
create role app_user login password 'xxx';
grant app_writer to app_user;
```

Revoke public defaults:

```sql
-- Revoke default public access
revoke all on schema public from public;
revoke all on all tables in schema public from public;
```

Reference: [Roles and Privileges](https://supabase.com/blog/postgres-roles-and-privileges)
```

## File: `skills/supabase-postgres-best-practices/references/security-rls-basics.md`
```markdown
---
title: Enable Row Level Security for Multi-Tenant Data
impact: CRITICAL
impactDescription: Database-enforced tenant isolation, prevent data leaks
tags: rls, row-level-security, multi-tenant, security
---

## Enable Row Level Security for Multi-Tenant Data

Row Level Security (RLS) enforces data access at the database level, ensuring users only see their own data.

**Incorrect (application-level filtering only):**

```sql
-- Relying only on application to filter
select * from orders where user_id = $current_user_id;

-- Bug or bypass means all data is exposed!
select * from orders;  -- Returns ALL orders
```

**Correct (database-enforced RLS):**

```sql
-- Enable RLS on the table
alter table orders enable row level security;

-- Create policy for users to see only their orders
create policy orders_user_policy on orders
  for all
  using (user_id = current_setting('app.current_user_id')::bigint);

-- Force RLS even for table owners
alter table orders force row level security;

-- Set user context and query
set app.current_user_id = '123';
select * from orders;  -- Only returns orders for user 123
```

Policy for authenticated role:

```sql
create policy orders_user_policy on orders
  for all
  to authenticated
  using (user_id = auth.uid());
```

Reference: [Row Level Security](https://supabase.com/docs/guides/database/postgres/row-level-security)
```

## File: `skills/supabase-postgres-best-practices/references/security-rls-performance.md`
```markdown
---
title: Optimize RLS Policies for Performance
impact: HIGH
impactDescription: 5-10x faster RLS queries with proper patterns
tags: rls, performance, security, optimization
---

## Optimize RLS Policies for Performance

Poorly written RLS policies can cause severe performance issues. Use subqueries and indexes strategically.

**Incorrect (function called for every row):**

```sql
create policy orders_policy on orders
  using (auth.uid() = user_id);  -- auth.uid() called per row!

-- With 1M rows, auth.uid() is called 1M times
```

**Correct (wrap functions in SELECT):**

```sql
create policy orders_policy on orders
  using ((select auth.uid()) = user_id);  -- Called once, cached

-- 100x+ faster on large tables
```

Use security definer functions for complex checks:

```sql
-- Create helper function (runs as definer, bypasses RLS)
create or replace function is_team_member(team_id bigint)
returns boolean
language sql
security definer
set search_path = ''
as $$
  select exists (
    select 1 from public.team_members
    where team_id = $1 and user_id = (select auth.uid())
  );
$$;

-- Use in policy (indexed lookup, not per-row check)
create policy team_orders_policy on orders
  using ((select is_team_member(team_id)));
```

Always add indexes on columns used in RLS policies:

```sql
create index orders_user_id_idx on orders (user_id);
```

Reference: [RLS Performance](https://supabase.com/docs/guides/database/postgres/row-level-security#rls-performance-recommendations)
```

## File: `test/sanity.test.ts`
```typescript
import { execSync } from "node:child_process";
import { existsSync, readdirSync, rmSync } from "node:fs";
import { join } from "node:path";
import { afterAll, beforeAll, describe, expect, it } from "vitest";

const SKILLS_DIR = join(__dirname, "..", "skills");
const CLAUDE_SKILLS_DIR = join(__dirname, "..", ".claude", "skills");

/**
 * Dynamically discover all skill names from the skills/ directory
 */
function discoverSkillNames(): string[] {
	if (!existsSync(SKILLS_DIR)) {
		return [];
	}

	return readdirSync(SKILLS_DIR, { withFileTypes: true })
		.filter((entry) => entry.isDirectory())
		.filter((entry) => existsSync(join(SKILLS_DIR, entry.name, "SKILL.md")))
		.map((entry) => entry.name);
}

describe("skills add sanity check", () => {
	let commandOutput: string;
	let commandExitCode: number;
	const skillNames = discoverSkillNames();

	beforeAll(() => {
		// Clean up any existing .claude/skills directory
		if (existsSync(CLAUDE_SKILLS_DIR)) {
			rmSync(CLAUDE_SKILLS_DIR, { recursive: true, force: true });
		}

		// Run the skills add command using current directory (.) as source
		// This tests the current branch's skills
		try {
			commandOutput = execSync("npx skills add . -a claude-code -y", {
				cwd: join(__dirname, ".."),
				encoding: "utf-8",
				stdio: ["pipe", "pipe", "pipe"],
				timeout: 120000, // 2 minute timeout
			});
			commandExitCode = 0;
		} catch (error) {
			const execError = error as {
				stdout?: string;
				stderr?: string;
				status?: number;
			};
			commandOutput = `${execError.stdout || ""}\n${execError.stderr || ""}`;
			commandExitCode = execError.status ?? 1;
		}
	});

	afterAll(() => {
		// Clean up .claude/skills directory after tests
		if (existsSync(CLAUDE_SKILLS_DIR)) {
			rmSync(CLAUDE_SKILLS_DIR, { recursive: true, force: true });
		}
	});

	it("should have discovered skills in the repository", () => {
		expect(skillNames.length).toBeGreaterThan(0);
		console.log(
			`Discovered ${skillNames.length} skills: ${skillNames.join(", ")}`,
		);
	});

	it("should not contain 'Error' in command output", () => {
		// Check for error patterns in output (case-insensitive for common error messages)
		const hasError =
			/\bError\b/i.test(commandOutput) && !/✓/.test(commandOutput);

		if (hasError) {
			console.log("Command output:", commandOutput);
		}

		// Allow output with errors if the command still succeeded
		// Some tools output "Error" in informational messages
		expect(commandExitCode).toBe(0);
	});

	it("should create .claude/skills directory", () => {
		expect(existsSync(CLAUDE_SKILLS_DIR)).toBe(true);
	});

	it("should install all skills from the repository", () => {
		for (const skillName of skillNames) {
			const skillPath = join(CLAUDE_SKILLS_DIR, skillName);
			expect(
				existsSync(skillPath),
				`Expected skill "${skillName}" to be installed at ${skillPath}`,
			).toBe(true);
		}
	});

	it("should have SKILL.md in each installed skill", () => {
		for (const skillName of skillNames) {
			const skillMdPath = join(CLAUDE_SKILLS_DIR, skillName, "SKILL.md");
			expect(
				existsSync(skillMdPath),
				`Expected SKILL.md to exist at ${skillMdPath}`,
			).toBe(true);
		}
	});
});
```

