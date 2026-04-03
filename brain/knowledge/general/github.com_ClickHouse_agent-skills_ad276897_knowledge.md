---
id: github.com-clickhouse-agent-skills-ad276897-knowle
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:39.927120
---

# KNOWLEDGE EXTRACT: github.com_ClickHouse_agent-skills_ad276897
> **Extracted on:** 2026-04-01 15:45:28
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007524743/github.com_ClickHouse_agent-skills_ad276897

---

## File: `.gitignore`
```
.DS_Store
node_modules/
*.log
dist/
build/
.env
.env.*
!.env.example
bun.lockb

# Build artifacts
packages/*/bin/
packages/*/dist/
packages/*/build/

# Temporary files
*.tmp
*.swp
*.swo
*~

# IDE
.vscode/
.idea/
*.sublime-*
```

## File: `AGENTS.md`
```markdown
# AGENTS.md

This file provides guidance to AI coding agents (Claude Code, Cursor, Copilot, etc.) when working with code in this repository.

## Repository Overview

A collection of skills for AI agents working with ClickHouse databases. Skills are packaged instructions and guidelines that extend agent capabilities for database design, query optimization, and operational best practices.

## Repository Structure

```
agent-skills/
├── skills/
│   └── clickhouse-best-practices/   # ClickHouse optimization guidelines
│       ├── SKILL.md                 # Skill definition (overview)
│       ├── AGENTS.md                # Full compiled guide (generated)
│       ├── metadata.json            # Version, organization, abstract
│       ├── README.md                # Maintainer guide
│       └── rules/                   # Individual rule files
│           ├── _sections.md         # Section metadata
│           ├── _template.md         # Template for new rules
│           └── *.md                 # Rule files (e.g., query-use-prewhere.md)
├── packages/
│   └── clickhouse-best-practices-build/  # Build tooling
│       ├── package.json             # Bun scripts
│       ├── tsconfig.json            # TypeScript config
│       └── src/
│           ├── config.ts            # Path configuration
│           ├── types.ts             # Type definitions
│           ├── parser.ts            # Markdown parser
│           ├── build.ts             # Build script
│           ├── validate.ts          # Rule validator
│           ├── validate-sql.ts      # SQL syntax validator
│           └── check-links.ts       # Internal link checker
└── .github/
    └── workflows/
        └── clickhouse-best-practices-ci.yml  # CI workflow
```

## Creating a New Skill

### Directory Structure

```
skills/
  {skill-name}/           # kebab-case directory name
    SKILL.md              # Required: skill definition
    AGENTS.md             # Generated: full compiled guide
    metadata.json         # Required: version, organization, abstract
    README.md             # Required: maintainer guide
    rules/                # Required: rule files
      _sections.md        # Section metadata
      _template.md        # Template for new rules
      *.md                # Individual rules
```

### Naming Conventions

- **Skill directory**: `kebab-case` (e.g., `clickhouse-best-practices`)
- **SKILL.md**: Always uppercase, always this exact filename
- **Rule files**: `{section-prefix}-{descriptive-name}.md` (e.g., `query-use-prewhere.md`)
- **Section prefixes**: Match the section IDs defined in `_sections.md`

### SKILL.md Format

```markdown
---
name: {skill-name}
description: {One sentence describing when to use this skill. Include trigger phrases.}
license: MIT
metadata:
  author: {organization}
  version: "{version}"
---

# {Skill Title}

{Brief description of what the skill does.}

## When to Apply

Reference these guidelines when:
- {Use case 1}
- {Use case 2}

## Rule Categories by Priority

| Priority | Category | Impact | Prefix |
|----------|----------|--------|--------|
| 1 | {Category} | {Impact} | `{prefix}-` |

## Quick Reference

{Brief overview of each category and key rules}

## How to Use

{Instructions on reading individual rule files}

## Full Compiled Document

For the complete guide with all rules expanded: `AGENTS.md`
```

### Rule File Format

Use the template in `rules/_template.md`. Each rule file must have:

1. **YAML frontmatter**:
   ```yaml
   ---
   title: Rule Title
   impact: CRITICAL | HIGH | MEDIUM-HIGH | MEDIUM | LOW-MEDIUM | LOW
   impactDescription: Optional (e.g., "10-100× query speedup")
   tags: skill, category, specific-tags
   ---
   ```

2. **Rule structure**:
   - Brief explanation of why it matters
   - **Incorrect:** code example showing the anti-pattern
   - **Correct:** code example showing the best practice
   - Additional context, trade-offs, or when to apply
   - Reference links (optional)

### Best Practices for Context Efficiency

Skills are loaded on-demand — only the skill name and description are loaded at startup. The full `SKILL.md` loads into context only when the agent decides the skill is relevant. To minimize context usage:

- **Keep SKILL.md under 500 lines** — put detailed reference material in separate files
- **Write specific descriptions** — helps the agent know exactly when to activate the skill
- **Use progressive disclosure** — reference supporting files that get read only when needed
- **Individual rule files** — allows agents to read only relevant rules on-demand
- **File references work one level deep** — link directly from SKILL.md to supporting files

### Build System Requirements

Each skill should have a build package that:
- Validates rule structure and content
- Validates code examples (e.g., SQL syntax for database skills)
- Checks internal links
- Generates the compiled `AGENTS.md` file

For ClickHouse Best Practices, the build system:
- Uses Bun for fast execution
- Downloads ClickHouse binary for real SQL validation
- Parses markdown with YAML frontmatter
- Generates table of contents and numbered sections
- Supports version management

### Development Workflow

1. **Add a rule**: Create a new `.md` file in `rules/` following the template
2. **Validate**: Run `bun run validate` to check structure
3. **Validate code**: Run skill-specific validators (e.g., `bun run validate-sql`)
4. **Check links**: Run `bun run check-links`
5. **Build**: Run `bun run build` to generate `AGENTS.md`
6. **Test**: Verify the generated documentation is correct

### CI/CD Integration

Set up GitHub Actions (or similar) to:
1. Install dependencies
2. Run all validation scripts
3. Build documentation
4. Upload artifacts

See `.github/workflows/clickhouse-best-practices-ci.yml` for an example.

## Contributing Guidelines

- Keep rules focused and actionable
- Use real code that can be executed (avoid pseudo-code)
- Include performance metrics when possible
- Reference official documentation where relevant
- Test code examples before committing
- Follow the existing style and structure

## Impact Levels

Choose the appropriate impact level for rules:

- **CRITICAL**: 10× or more improvement, or prevents serious issues
- **HIGH**: 2-10× improvement, or significantly impacts scalability
- **MEDIUM-HIGH**: 25-100% improvement, or important for specific workloads
- **MEDIUM**: 10-25% improvement, or helpful for maintainability
- **LOW-MEDIUM**: 5-10% improvement, or nice-to-have optimizations
- **LOW**: Minor improvements or edge cases
```

## File: `AI_POLICY.md`
```markdown
# ClickHouse AI Policy

You can use AI for ClickHouse development. We welcome and embrace AI usage, as well as research and experiments with the frontier AI models and novel methods of AI applications for software engineering.

You don't have to disclose your usage of AI. You can tell about it, share your experience, and show the methods, but it is not required. AI is a normal developer's tool, similar to an IDE, an OS, or a keyboard. We don't judge your work on the basis of the usage of AI, but we recommend taking efforts to filter out slop before sending a pull request; otherwise, it may negatively affect your reputation as an engineer.

When sending generated code, you take the responsibility in the same way as for the code you have manually typed. Take efforts to read and review the code before sending - otherwise it is disrespectful to maintainers. Take efforts to understand the code base, with or without the help of AI. Low-effort pull requests that require high effort from maintainers will be closed. Do not use AI to automate your responses to maintainers.

Prefer using AI for improving the code base, such as removing and simplifying code, improving the build speed, improving continuous integration tools and quality checks, reverting bad modifications, security research, and bug fixing. Keep in mind that using AI for implementing big features requires as much design consideration as without AI.

When using AI, the same rules around intellectual property apply as with manually written code. Do not copy, reproduce, or include code belonging to others unless its license explicitly permits this use and all license requirements are met. You are responsible for ensuring that you have all required permissions for any submitted code, whether AI-generated or not.

We will be happy to participate in research and experiments with AI models and their application methods on top of the ClickHouse code base. It could be: - benchmarks and comparisons of models, testing of models by solving identical tasks, AI reproducibility studies, performance of agentic loops, AI sandboxing, etc. ClickHouse provides an extremely comprehensive test suite to fulfill these studies, and it is one of the most actively developed open-source software in the world. If you want to share your research, you can send a letter to ai@clickhouse.com.
```

## File: `LICENSE`
```
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
```

## File: `NOTICE`
```
Agent Skills for ClickHouse

This repository includes software developed at Vercel, Inc.
(https://github.com/vercel/agent-skills)

Some files in packages/clickhouse-best-practices-build/src/ are
adapted from the Vercel Agent Skills project:
- types.ts
- parser.ts
- build.ts
- validate.ts

Copyright (c) Vercel, Inc.
Licensed under the MIT License

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
# ClickHouse Agent Skills

The official Agent Skills for [ClickHouse](https://clickhouse.com/). These skills help LLMs and agents to adopt best practices when working with ClickHouse.

You can use these skills with open-source ClickHouse and managed ClickHouse Cloud. [Try ClickHouse Cloud with $300 in free credits](https://clickhouse.com/cloud?utm_medium=github&utm_source=github&utm_ref=agent-skills).

## Installation

```bash
npx skills add clickhouse/agent-skills
```

The CLI auto-detects installed agents and prompts you to select where to install.

## What is this?

Agent Skills are packaged instructions that extend AI coding agents (Claude Code, Cursor, Copilot, etc.) with domain-specific expertise. This repository provides skills for ClickHouse databases—covering schema design, query optimization, and data ingestion patterns.

When an agent loads these skills, it gains knowledge of ClickHouse best practices and can apply them while helping you design tables, write queries, or troubleshoot performance issues.

Skills follow the open specification at [agentskills.io](https://agentskills.io).

## Available Skills

### ClickHouse Best Practices

**28 rules** covering schema design, query optimization, and data ingestion—prioritized by impact.

| Category | Rules | Impact |
|----------|-------|--------|
| Primary Key Selection | 4 | CRITICAL |
| Data Type Selection | 5 | CRITICAL |
| JOIN Optimization | 5 | CRITICAL |
| Insert Batching | 1 | CRITICAL |
| Mutation Avoidance | 2 | CRITICAL |
| Partitioning Strategy | 4 | HIGH |
| Skipping Indices | 1 | HIGH |
| Materialized Views | 2 | HIGH |
| Async Inserts | 2 | HIGH |
| OPTIMIZE Avoidance | 1 | HIGH |
| JSON Usage | 1 | MEDIUM |

**Location:** [`skills/clickhouse-best-practices/`](./skills/clickhouse-best-practices/)

**For humans:** Read [SKILL.md](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md) for an overview, or [AGENTS.md](../../../.claude/skills/supabase-postgres-best-practices/AGENTS.md) for the complete compiled guide.

**For agents:** The skill activates automatically when you work with ClickHouse—creating tables, writing queries, or designing data pipelines.

## Quick Start

After installation, your AI agent will reference these best practices when:

- Creating new tables with `CREATE TABLE`
- Choosing `ORDER BY` / `PRIMARY KEY` columns
- Selecting data types for columns
- Optimizing slow queries
- Writing or tuning JOINs
- Designing data ingestion pipelines
- Handling updates or deletes

Example prompt:
> "Create a table for storing user events with fields for user_id, event_type, properties (JSON), and timestamp"

The agent will apply relevant rules like proper column ordering in the primary key, appropriate data types, and partitioning strategy.

## Supported Agents

Skills are **agent-agnostic**—the same skill works across all supported AI coding assistants:

| Agent | Config Directory |
|-------|------------------|
| [Claude Code](https://claude.ai/code) | `.claude/skills/` |
| [Cursor](https://cursor.sh) | `.cursor/skills/` |
| [Windsurf](https://codeium.com/windsurf) | `.windsurf/skills/` |
| [GitHub Copilot](https://github.com/features/copilot) | `.github/skills/` |
| [Gemini CLI](https://github.com/google-gemini/gemini-cli) | `.gemini/skills/` |
| [Cline](https://github.com/cline/cline) | `.cline/skills/` |
| [Codex](https://openai.com/codex) | `.codex/skills/` |
| [Goose](https://github.com/block/goose) | `.goose/skills/` |
| [Roo Code](https://roo.ai) | `.roo/skills/` |
| [OpenHands](https://github.com/All-Hands-AI/OpenHands) | `.openhands/skills/` |

And 13 more including Amp, Kiro CLI, Trae, Zencoder, and others.

The installer detects which agents you have by checking for their configuration directories. If an agent isn't listed, either install it first or create its config directory manually (e.g., `mkdir -p ~/.cursor`).

## License

Apache 2.0 — see [LICENSE](./LICENSE) for details.
```

## File: `packages/clickhouse-best-practices-build/bun.lock`
```
{
  "lockfileVersion": 1,
  "configVersion": 1,
  "workspaces": {
    "": {
      "name": "clickhouse-best-practices-build",
      "devDependencies": {
        "@types/node": "^20.0.0",
        "typescript": "^5.3.0",
      },
    },
  },
  "packages": {
    "@types/node": ["@types/node@20.19.30", "", { "dependencies": { "undici-types": "~6.21.0" } }, "sha512-WJtwWJu7UdlvzEAUm484QNg5eAoq5QR08KDNx7g45Usrs2NtOPiX8ugDqmKdXkyL03rBqU5dYNYVQetEpBHq2g=="],

    "typescript": ["typescript@5.9.3", "", { "bin": { "tsc": "bin/tsc", "tsserver": "bin/tsserver" } }, "sha512-jl1vZzPDinLr9eUt3J/t7V6FgNEw9QjvBPdysz9KfQDD41fQrC2Y4vKQdiaUpFT4bXlb1RHhLpp8wtm6M5TgSw=="],

    "undici-types": ["undici-types@6.21.0", "", {}, "sha512-iwDZqg0QAGrg9Rav5H4n0M64c3mkR59cJ6wQp+7C4nI0gsmExaedaYLNO44eT4AtBBwjbTiGPMlt2Md0T9H9JQ=="],
  }
}
```

## File: `packages/clickhouse-best-practices-build/package.json`
```json
{
  "name": "clickhouse-best-practices-build",
  "version": "0.1.0",
  "description": "Build tooling for ClickHouse Best Practices skill",
  "type": "module",
  "scripts": {
    "build": "bun run build-agents",
    "build-agents": "bun src/build.ts",
    "validate": "bun src/validate.ts",
    "validate-sql": "bun src/validate-sql.ts",
    "check-links": "bun src/check-links.ts",
    "check-external-links": "bun src/check-external-links.ts",
    "dev": "bun run build && bun run validate"
  },
  "keywords": [
    "clickhouse",
    "performance",
    "guidelines",
    "llm",
    "agents"
  ],
  "license": "Apache-2.0",
  "devDependencies": {
    "@types/node": "^20.0.0",
    "typescript": "^5.3.0"
  }
}
```

## File: `packages/clickhouse-best-practices-build/tsconfig.json`
```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "ESNext",
    "lib": ["ES2022"],
    "moduleResolution": "node",
    "esModuleInterop": true,
    "strict": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true,
    "outDir": "./dist",
    "rootDir": "./src"
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}
```

## File: `packages/clickhouse-best-practices-build/src/build.ts`
```typescript
#!/usr/bin/env node
/**
 * Build script to compile individual rule files into AGENTS.md
 *
 * Adapted from github.com/vercel/agent-skills
 * Copyright (c) Vercel, Inc.
 * Licensed under MIT License
 */

import { readdir, readFile, writeFile } from 'fs/promises'
import { join } from 'path'
import { Rule, Section, GuidelinesDocument, ImpactLevel } from './types.js'
import { parseRuleFile, RuleFile } from './parser.js'
import { RULES_DIR, METADATA_FILE, OUTPUT_FILE, SKILL_DIR } from './config.js'

// Parse command line arguments
const args = process.argv.slice(2)
const upgradeVersion = args.includes('--upgrade-version')

/**
 * Increment a semver-style version string (e.g., "0.1.0" -> "0.1.1", "1.0" -> "1.1")
 */
function incrementVersion(version: string): string {
  const parts = version.split('.').map(Number)
  // Increment the last part
  parts[parts.length - 1]++
  return parts.join('.')
}

/**
 * Generate markdown from rules
 */
function generateMarkdown(
  sections: Section[],
  metadata: {
    version: string
    organization: string
    date: string
    abstract: string
    references?: string[]
    clickhouseVersion?: string
  }
): string {
  let md = `# ClickHouse Best Practices\n\n`
  md += `**Version ${metadata.version}**  \n`
  md += `${metadata.organization}  \n`
  md += `${metadata.date}\n`
  if (metadata.clickhouseVersion) {
    md += `ClickHouse ${metadata.clickhouseVersion}\n`
  }
  md += `\n`
  md += `> **Note:**  \n`
  md += `> This document is mainly for agents and LLMs to follow when designing,  \n`
  md += `> optimizing, or maintaining ClickHouse databases. Humans may also find it  \n`
  md += `> useful, but guidance here is optimized for automation and consistency by  \n`
  md += `> AI-assisted workflows.\n\n`
  md += `---\n\n`
  md += `## Abstract\n\n`
  md += `${metadata.abstract}\n\n`
  md += `---\n\n`
  md += `## Table of Contents\n\n`

  // Generate TOC
  sections.forEach((section) => {
    md += `${section.number}. [${section.title}](#${
      section.number
    }-${section.title.toLowerCase().replace(/\s+/g, '-')}) — **${
      section.impact
    }**\n`
    section.rules.forEach((rule) => {
      // GitHub generates anchors from the full heading text: "1.1 Title" -> "#11-title"
      const anchor = `${rule.id} ${rule.title}`
        .toLowerCase()
        .replace(/\s+/g, '-')
        .replace(/[^\w-]/g, '') // Remove special characters except hyphens
      md += `   - ${rule.id} [${rule.title}](#${anchor})\n`
    })
  })

  md += `\n---\n\n`

  // Generate sections
  sections.forEach((section) => {
    md += `## ${section.number}. ${section.title}\n\n`
    md += `**Impact: ${section.impact}${
      section.impactDescription ? ` (${section.impactDescription})` : ''
    }**\n\n`
    if (section.introduction) {
      md += `${section.introduction}\n\n`
    }

    section.rules.forEach((rule) => {
      md += `### ${rule.id} ${rule.title}\n\n`
      md += `**Impact: ${rule.impact}${
        rule.impactDescription ? ` (${rule.impactDescription})` : ''
      }**\n\n`
      md += `${rule.explanation}\n\n`

      rule.examples.forEach((example) => {
        if (example.description) {
          md += `**${example.label}: ${example.description}**\n\n`
        } else {
          md += `**${example.label}:**\n\n`
        }
        // Only generate code block if there's actual code
        if (example.code && example.code.trim()) {
          md += `\`\`\`${example.language || 'sql'}\n`
          md += `${example.code}\n`
          md += `\`\`\`\n\n`
        }
        if (example.additionalText) {
          md += `${example.additionalText}\n\n`
        }
      })

      if (rule.references && rule.references.length > 0) {
        md += `Reference: ${rule.references
          .map((ref) => `[${ref}](${ref})`)
          .join(', ')}\n\n`
      }
    })

    md += `---\n\n`
  })

  // Add references section
  if (metadata.references && metadata.references.length > 0) {
    md += `## References\n\n`
    metadata.references.forEach((ref, i) => {
      md += `${i + 1}. [${ref}](${ref})\n`
    })
  }

  return md
}

/**
 * Main build function
 */
async function build() {
  try {
    console.log('Building AGENTS.md from rules...')
    console.log(`Rules directory: ${RULES_DIR}`)
    console.log(`Output file: ${OUTPUT_FILE}`)

    // Read all rule files (exclude files starting with _ and README.md)
    const files = await readdir(RULES_DIR)
    const ruleFiles = files
      .filter(
        (f) => f.endsWith('.md') && !f.startsWith('_') && f !== 'README.md'
      )
      .sort() // Sort filenames for consistent ordering across systems

    const ruleData: RuleFile[] = []
    for (const file of ruleFiles) {
      const filePath = join(RULES_DIR, file)
      try {
        const parsed = await parseRuleFile(filePath)
        ruleData.push(parsed)
      } catch (error) {
        console.error(`Error parsing ${file}:`, error)
      }
    }

    // Group rules by section
    const sectionsMap = new Map<number, Section>()

    ruleData.forEach(({ section, rule }) => {
      if (!sectionsMap.has(section)) {
        sectionsMap.set(section, {
          number: section,
          title: `Section ${section}`, // Will be overridden by section metadata
          impact: rule.impact,
          rules: [],
        })
      }
      sectionsMap.get(section)!.rules.push(rule)
    })

    // Sort rules within each section by title (using en-US locale for consistency across environments)
    sectionsMap.forEach((section) => {
      section.rules.sort((a, b) =>
        a.title.localeCompare(b.title, 'en-US', { sensitivity: 'base' })
      )

      // Assign IDs based on sorted order
      section.rules.forEach((rule, index) => {
        rule.id = `${section.number}.${index + 1}`
        rule.subsection = index + 1
      })
    })

    // Convert to array and sort
    const sections = Array.from(sectionsMap.values()).sort(
      (a, b) => a.number - b.number
    )

    // Read section metadata from consolidated _sections.md file
    const sectionsFile = join(RULES_DIR, '_sections.md')
    try {
      const sectionsContent = await readFile(sectionsFile, 'utf-8')

      // Parse sections using regex to match each section block
      const sectionBlocks = sectionsContent
        .split(/(?=^## \d+\. )/m)
        .filter(Boolean)

      for (const block of sectionBlocks) {
        // Extract section number and title, removing section ID in parentheses
        const headerMatch = block.match(
          /^## (\d+)\.\s+(.+?)(?:\s+\([^)]+\))?$/m
        )
        if (!headerMatch) continue

        const sectionNumber = parseInt(headerMatch[1])
        const sectionTitle = headerMatch[2].trim() // Strip (id) for output

        // Extract impact (format: **Impact:** CRITICAL)
        const impactMatch = block.match(/\*\*Impact:\*\*\s+(\w+(?:-\w+)?)/i)
        const impactLevel = impactMatch
          ? (impactMatch[1].toUpperCase().replace(/-/g, '-') as ImpactLevel)
          : 'MEDIUM'

        // Extract description (format: **Description:** text)
        const descMatch = block.match(
          /\*\*Description:\*\*\s+(.+?)(?=\n\n##|$)/s
        )
        const description = descMatch ? descMatch[1].trim() : ''

        // Update section if it exists
        const section = sections.find((s) => s.number === sectionNumber)
        if (section) {
          section.title = sectionTitle
          section.impact = impactLevel
          section.introduction = description
        }
      }
    } catch (error) {
      console.warn(
        'Warning: Could not read _sections.md, using defaults',
        error
      )
    }

    // Read metadata
    let metadata
    try {
      const metadataContent = await readFile(METADATA_FILE, 'utf-8')
      metadata = JSON.parse(metadataContent)
    } catch {
      metadata = {
        version: '0.1.0',
        organization: 'ClickHouse Inc',
        date: new Date().toLocaleDateString('en-US', {
          month: 'long',
          year: 'numeric',
        }),
        clickhouseVersion: '24.1+',
        abstract:
          'Performance optimization guide for ClickHouse databases, ordered by impact.',
      }
    }

    // Upgrade version if flag is passed
    if (upgradeVersion) {
      const oldVersion = metadata.version
      metadata.version = incrementVersion(oldVersion)
      console.log(`Upgrading version: ${oldVersion} -> ${metadata.version}`)

      // Write updated metadata.json
      await writeFile(METADATA_FILE, JSON.stringify(metadata, null, 2) + '\n', 'utf-8')
      console.log(`✓ Updated metadata.json`)

      // Update SKILL.md frontmatter
      const skillFile = join(SKILL_DIR, 'SKILL.md')
      const skillContent = await readFile(skillFile, 'utf-8')
      const updatedSkillContent = skillContent.replace(
        /^(---[\s\S]*?version:\s*)"[^"]*"([\s\S]*?---)$/m,
        `$1"${metadata.version}"$2`
      )
      await writeFile(skillFile, updatedSkillContent, 'utf-8')
      console.log(`✓ Updated SKILL.md`)
    }

    // Generate markdown
    const markdown = generateMarkdown(sections, metadata)

    // Write output
    await writeFile(OUTPUT_FILE, markdown, 'utf-8')

    console.log(
      `✓ Built AGENTS.md with ${sections.length} sections and ${ruleData.length} rules`
    )
  } catch (error) {
    console.error('Build failed:', error)
    process.exit(1)
  }
}

build()
```

## File: `packages/clickhouse-best-practices-build/src/check-external-links.ts`
```typescript
#!/usr/bin/env node
/**
 * Check for broken external HTTP/HTTPS links in skill files
 *
 * This script:
 * - Scans all .md and .json files in the skills directory
 * - Extracts HTTP/HTTPS URLs from markdown links and JSON fields
 * - Validates each URL returns a 2XX status code
 * - Processes links asynchronously in batches (max 5 concurrent)
 * - Retries failed links with exponential backoff
 * - Reports detailed errors for any broken links
 */

import { readdir, readFile } from 'fs/promises'
import { join, relative } from 'path'
import { SKILL_DIR } from './config.js'

interface LinkInfo {
  url: string
  source: {
    skill: string
    file: string
  }
}

interface LinkCheckResult {
  url: string
  success: boolean
  statusCode?: number
  error?: string
  source: { skill: string, file: string }
  retriesUsed: number
}

const TIMEOUT_MS = 10000 // 10 seconds
const MAX_RETRIES = 2 // Try up to 2 additional times after initial failure
const CONCURRENCY = 5 // Max concurrent requests per batch
const RETRY_DELAYS = [100, 200, 400] // Exponential backoff delays in ms

/**
 * Extract markdown links from content
 */
function extractMarkdownLinks(content: string): string[] {
  const linkRegex = /\[([^\]]+)\]\(([^)]+)\)/g
  const links: string[] = []
  let match

  while ((match = linkRegex.exec(content)) !== null) {
    links.push(match[2])
  }

  return links
}

/**
 * Extract URLs from JSON content (recursively)
 */
function extractJsonUrls(obj: any, urls: string[] = []): string[] {
  if (typeof obj === 'string') {
    if (obj.startsWith('http://') || obj.startsWith('https://')) {
      urls.push(obj)
    }
  } else if (Array.isArray(obj)) {
    for (const item of obj) {
      extractJsonUrls(item, urls)
    }
  } else if (obj !== null && typeof obj === 'object') {
    for (const value of Object.values(obj)) {
      extractJsonUrls(value, urls)
    }
  }
  return urls
}

/**
 * Check if a URL is external (HTTP/HTTPS)
 */
function isExternalUrl(url: string): boolean {
  return url.startsWith('http://') || url.startsWith('https://')
}

/**
 * Sleep for specified milliseconds
 */
function sleep(ms: number): Promise<void> {
  return new Promise(resolve => setTimeout(resolve, ms))
}

/**
 * Validate a single URL with retry logic
 */
async function validateUrl(
  url: string,
  source: { skill: string, file: string },
  timeout: number = TIMEOUT_MS,
  maxRetries: number = MAX_RETRIES
): Promise<LinkCheckResult> {
  let lastError: string = ''
  let lastStatusCode: number | undefined
  let retriesUsed = 0

  for (let attempt = 0; attempt <= maxRetries; attempt++) {
    if (attempt > 0) {
      // Wait before retry with exponential backoff
      const delay = RETRY_DELAYS[Math.min(attempt - 1, RETRY_DELAYS.length - 1)]
      await sleep(delay)
      retriesUsed++
    }

    try {
      const controller = new AbortController()
      const timeoutId = setTimeout(() => controller.abort(), timeout)

      try {
        // Try HEAD request first (faster, less bandwidth)
        let response = await fetch(url, {
          method: 'HEAD',
          signal: controller.signal,
          redirect: 'follow'
        })

        // If HEAD fails or returns error, try GET
        if (!response.ok) {
          const headStatusCode = response.status
          response = await fetch(url, {
            method: 'GET',
            signal: controller.signal,
            redirect: 'follow'
          })

          // If GET succeeded but HEAD failed, use GET result
          if (response.ok) {
            clearTimeout(timeoutId)
            return {
              url,
              success: true,
              statusCode: response.status,
              source,
              retriesUsed
            }
          }

          // Both failed, use GET status
          lastStatusCode = response.status
        } else {
          // HEAD succeeded
          clearTimeout(timeoutId)
          return {
            url,
            success: true,
            statusCode: response.status,
            source,
            retriesUsed
          }
        }

        clearTimeout(timeoutId)

        // Check if status code is 2XX
        if (response.status >= 200 && response.status < 300) {
          return {
            url,
            success: true,
            statusCode: response.status,
            source,
            retriesUsed
          }
        }

        lastStatusCode = response.status
        lastError = `${response.status} ${response.statusText}`
      } catch (fetchError: any) {
        clearTimeout(timeoutId)
        throw fetchError
      }
    } catch (error: any) {
      if (error.name === 'AbortError') {
        lastError = 'Request timeout'
      } else if (error.code === 'ENOTFOUND') {
        lastError = 'DNS lookup failed'
      } else if (error.code === 'ECONNREFUSED') {
        lastError = 'Connection refused'
      } else {
        lastError = error.message || 'Unknown error'
      }
    }
  }

  // All retries exhausted
  return {
    url,
    success: false,
    statusCode: lastStatusCode,
    error: lastError,
    source,
    retriesUsed
  }
}

/**
 * Validate URLs in batches with concurrency limit
 */
async function validateUrlsBatch(
  linkInfos: LinkInfo[],
  concurrency: number
): Promise<LinkCheckResult[]> {
  const results: LinkCheckResult[] = []

  // Process in batches
  for (let i = 0; i < linkInfos.length; i += concurrency) {
    const batch = linkInfos.slice(i, i + concurrency)
    const batchResults = await Promise.allSettled(
      batch.map(info => validateUrl(info.url, info.source))
    )

    for (const result of batchResults) {
      if (result.status === 'fulfilled') {
        results.push(result.value)
      } else {
        // This shouldn't happen as validateUrl catches all errors
        // but handle it just in case
        const info = batch[results.length % batch.length]
        results.push({
          url: info.url,
          success: false,
          error: result.reason?.message || 'Unknown error',
          source: info.source,
          retriesUsed: 0
        })
      }
    }

    // Show progress
    console.log(`Checked ${Math.min(i + concurrency, linkInfos.length)}/${linkInfos.length} links...`)
  }

  return results
}

/**
 * Print summary table of results
 */
function printSummaryTable(results: LinkCheckResult[]): void {
  console.log('\n' + '='.repeat(80))
  console.log('External Links Check Summary')
  console.log('='.repeat(80) + '\n')

  // Sort: failures first, then by URL
  const sortedResults = [...results].sort((a, b) => {
    if (a.success !== b.success) {
      return a.success ? 1 : -1
    }
    return a.url.localeCompare(b.url)
  })

  // Print table header
  console.log('┌─────────────────────────────────────────────────────────────────────────────┐')
  console.log('│ URL                                                      │ Status │ Source  │')
  console.log('├──────────────────────────────────────────────────────────┼────────┼─────────┤')

  for (const result of sortedResults) {
    const truncatedUrl = result.url.length > 56
      ? result.url.substring(0, 53) + '...'
      : result.url
    const statusText = result.success
      ? `${result.statusCode} ✓`
      : result.statusCode
        ? `${result.statusCode} ✗`
        : 'ERR ✗'
    const sourceFile = result.source.file.length > 12
      ? '...' + result.source.file.substring(result.source.file.length - 9)
      : result.source.file

    console.log(
      `│ ${truncatedUrl.padEnd(56)} │ ${statusText.padEnd(6)} │ ${sourceFile.padEnd(7)} │`
    )
  }

  console.log('└──────────────────────────────────────────────────────────┴────────┴─────────┘')

  // Print summary counts
  const passed = results.filter(r => r.success).length
  const failed = results.filter(r => !r.success).length
  console.log(`\nSummary: ${results.length} links checked, ${passed} passed, ${failed} failed`)
}

/**
 * Print detailed error information
 */
function printDetailedErrors(results: LinkCheckResult[]): void {
  const failures = results.filter(r => !r.success)

  if (failures.length === 0) {
    return
  }

  console.log('\n✗ External link checking failed:\n')

  for (const failure of failures) {
    console.log(`  ${failure.source.file}`)
    console.log(`    Link: ${failure.url}`)
    if (failure.statusCode) {
      console.log(`    Status: ${failure.statusCode}`)
    }
    if (failure.error) {
      console.log(`    Error: ${failure.error}`)
    }
    console.log(`    (Verified with ${failure.retriesUsed} retries)`)
    console.log('')
  }
}

/**
 * Recursively find all files with given extensions
 * Excludes files starting with underscore (templates and metadata)
 */
async function findFiles(dir: string, extensions: string[]): Promise<string[]> {
  const files: string[] = []

  async function walk(currentDir: string): Promise<void> {
    const entries = await readdir(currentDir, { withFileTypes: true })

    for (const entry of entries) {
      const fullPath = join(currentDir, entry.name)

      if (entry.isDirectory()) {
        await walk(fullPath)
      } else if (entry.isFile()) {
        // Skip files starting with underscore (templates, metadata)
        if (entry.name.startsWith('_')) {
          continue
        }

        const hasExtension = extensions.some(ext => entry.name.endsWith(ext))
        if (hasExtension) {
          files.push(fullPath)
        }
      }
    }
  }

  await walk(dir)
  return files
}

/**
 * Main external link checking function
 */
async function checkExternalLinks(): Promise<void> {
  try {
    console.log('Checking external links...')
    console.log(`Skill directory: ${SKILL_DIR}\n`)

    // Find all .md and .json files
    const files = await findFiles(SKILL_DIR, ['.md', '.json'])
    console.log(`Found ${files.length} files to scan\n`)

    // Collect all external links with their sources
    const linkMap = new Map<string, LinkInfo>()

    for (const filePath of files) {
      const content = await readFile(filePath, 'utf-8')
      const relativePath = relative(SKILL_DIR, filePath)
      let urls: string[] = []

      if (filePath.endsWith('.md')) {
        urls = extractMarkdownLinks(content).filter(isExternalUrl)
      } else if (filePath.endsWith('.json')) {
        try {
          const jsonData = JSON.parse(content)
          urls = extractJsonUrls(jsonData).filter(isExternalUrl)
        } catch (error) {
          console.warn(`Warning: Could not parse JSON file ${relativePath}`)
          continue
        }
      }

      // Add to map (deduplicate URLs, but keep first source)
      for (const url of urls) {
        if (!linkMap.has(url)) {
          linkMap.set(url, {
            url,
            source: {
              skill: 'clickhouse-best-practices',
              file: relativePath
            }
          })
        }
      }
    }

    const uniqueLinks = Array.from(linkMap.values())

    if (uniqueLinks.length === 0) {
      console.log('No external links found')
      return
    }

    console.log(`Found ${uniqueLinks.length} unique external links\n`)

    // Validate all URLs in batches
    const results = await validateUrlsBatch(uniqueLinks, CONCURRENCY)

    // Print summary table
    printSummaryTable(results)

    // Check for failures
    const failures = results.filter(r => !r.success)

    if (failures.length > 0) {
      printDetailedErrors(results)
      process.exit(1)
    } else {
      console.log(`\n✓ All ${results.length} external links are valid`)
    }
  } catch (error) {
    console.error('External link checking failed:', error)
    process.exit(1)
  }
}

checkExternalLinks()
```

## File: `packages/clickhouse-best-practices-build/src/check-links.ts`
```typescript
#!/usr/bin/env node
/**
 * Check for broken internal links in rule files
 */

import { readdir, readFile } from 'fs/promises'
import { join, basename } from 'path'
import { RULES_DIR } from './config.js'

interface LinkError {
  file: string
  link: string
  message: string
}

/**
 * Extract markdown links from content
 */
function extractLinks(content: string): string[] {
  const linkRegex = /\[([^\]]+)\]\(([^)]+)\)/g
  const links: string[] = []
  let match

  while ((match = linkRegex.exec(content)) !== null) {
    links.push(match[2])
  }

  return links
}

/**
 * Check if a link is internal (relative path or anchor)
 */
function isInternalLink(link: string): boolean {
  return !link.startsWith('http://') && !link.startsWith('https://')
}

/**
 * Main link checking function
 */
async function checkLinks() {
  try {
    console.log('Checking internal links in rule files...')
    console.log(`Rules directory: ${RULES_DIR}`)

    // Read all rule files
    const files = await readdir(RULES_DIR)
    const ruleFiles = files.filter(f => f.endsWith('.md'))

    // Build a set of available files (for reference checking)
    const availableFiles = new Set(ruleFiles.map(f => basename(f, '.md')))

    const allErrors: LinkError[] = []

    for (const file of ruleFiles) {
      const filePath = join(RULES_DIR, file)
      const content = await readFile(filePath, 'utf-8')

      // Extract all links
      const links = extractLinks(content)

      // Check internal links
      for (const link of links) {
        if (isInternalLink(link)) {
          // Check if it's a reference to another rule file
          if (link.endsWith('.md')) {
            const referencedFile = basename(link)
            if (!ruleFiles.includes(referencedFile)) {
              allErrors.push({
                file,
                link,
                message: `Referenced file does not exist: ${referencedFile}`
              })
            }
          }
          // Check if it's a reference to a rule by ID (e.g., #21-use-prewhere)
          else if (link.startsWith('#')) {
            // Extract the rule file name from anchor if it follows pattern #section-title
            const anchorMatch = link.match(/^#(\w+)/)
            if (anchorMatch) {
              const prefix = anchorMatch[1]
              // Check if there's a file starting with this prefix
              const hasMatchingFile = ruleFiles.some(f => f.startsWith(prefix))
              if (!hasMatchingFile && !link.match(/^\d+-\d+/)) {
                // Only warn if it's not a standard section anchor (like #1-schema-design)
                // and there's no matching file
                // Skip this check as it's too strict for section anchors
              }
            }
          }
        }
      }
    }

    if (allErrors.length > 0) {
      console.error('\n✗ Link checking failed:\n')
      allErrors.forEach(error => {
        console.error(`  ${error.file}`)
        console.error(`    Link: ${error.link}`)
        console.error(`    ${error.message}`)
        console.error('')
      })
      process.exit(1)
    } else {
      console.log(`✓ All internal links are valid`)
    }
  } catch (error) {
    console.error('Link checking failed:', error)
    process.exit(1)
  }
}

checkLinks()
```

## File: `packages/clickhouse-best-practices-build/src/config.ts`
```typescript
/**
 * Configuration for the build tooling
 */

import { join, dirname } from 'path'
import { fileURLToPath } from 'url'

const __dirname = dirname(fileURLToPath(import.meta.url))

// Path to the skill directory (relative to this package)
export const SKILL_DIR = join(__dirname, '../../..', 'skills/clickhouse-best-practices')
export const BUILD_DIR = join(__dirname, '..')
export const RULES_DIR = join(SKILL_DIR, 'rules')
export const METADATA_FILE = join(SKILL_DIR, 'metadata.json')
export const OUTPUT_FILE = join(SKILL_DIR, 'AGENTS.md')
```

## File: `packages/clickhouse-best-practices-build/src/parser.ts`
```typescript
/**
 * Parser for rule markdown files
 *
 * Adapted from github.com/vercel/agent-skills
 * Copyright (c) Vercel, Inc.
 * Licensed under MIT License
 */

import { readFile } from 'fs/promises'
import { basename } from 'path'
import { Rule, ImpactLevel } from './types.js'

export interface RuleFile {
  section: number
  subsection?: number
  rule: Rule
}

/**
 * Parse a rule markdown file into a Rule object
 */
export async function parseRuleFile(filePath: string): Promise<RuleFile> {
  const rawContent = await readFile(filePath, 'utf-8')
  // Normalize Windows CRLF line endings to LF for consistent parsing
  const content = rawContent.replace(/\r\n/g, '\n')
  const lines = content.split('\n')

  // Extract frontmatter if present
  let frontmatter: Record<string, any> = {}
  let contentStart = 0

  if (content.startsWith('---')) {
    const frontmatterEnd = content.indexOf('---', 3)
    if (frontmatterEnd !== -1) {
      const frontmatterText = content.slice(3, frontmatterEnd).trim()
      frontmatterText.split('\n').forEach((line) => {
        const [key, ...valueParts] = line.split(':')
        if (key && valueParts.length) {
          const value = valueParts.join(':').trim()
          frontmatter[key.trim()] = value.replace(/^["']|["']$/g, '')
        }
      })
      contentStart = frontmatterEnd + 3
    }
  }

  // Parse the rule content
  const ruleContent = content.slice(contentStart).trim()
  const ruleLines = ruleContent.split('\n')

  // Extract title (first # or ## heading)
  let title = ''
  let titleLine = 0
  for (let i = 0; i < ruleLines.length; i++) {
    if (ruleLines[i].startsWith('##')) {
      title = ruleLines[i].replace(/^##+\s*/, '').trim()
      titleLine = i
      break
    }
  }

  // Extract impact
  let impact: Rule['impact'] = 'MEDIUM'
  let impactDescription = ''
  let explanation = ''
  let examples: Rule['examples'] = []
  let references: string[] = []

  // Parse content after title
  let currentExample: {
    label: string
    description?: string
    code: string
    language?: string
    additionalText?: string
  } | null = null
  let inCodeBlock = false
  let codeBlockLanguage = 'sql'
  let codeBlockContent: string[] = []
  let afterCodeBlock = false
  let additionalText: string[] = []
  let hasCodeBlockForCurrentExample = false

  for (let i = titleLine + 1; i < ruleLines.length; i++) {
    const line = ruleLines[i]

    // Impact line
    if (line.includes('**Impact:')) {
      const match = line.match(
        /\*\*Impact:\s*(\w+(?:-\w+)?)\s*(?:\(([^)]+)\))?/i
      )
      if (match) {
        impact = match[1].toUpperCase().replace(/-/g, '-') as ImpactLevel
        impactDescription = match[2] || ''
      }
      continue
    }

    // Code block start
    if (line.startsWith('```')) {
      if (inCodeBlock) {
        // End of code block
        if (currentExample) {
          currentExample.code = codeBlockContent.join('\n')
          currentExample.language = codeBlockLanguage
        }
        codeBlockContent = []
        inCodeBlock = false
        afterCodeBlock = true
      } else {
        // Start of code block
        inCodeBlock = true
        hasCodeBlockForCurrentExample = true
        codeBlockLanguage = line.slice(3).trim() || 'sql'
        codeBlockContent = []
        afterCodeBlock = false
      }
      continue
    }

    if (inCodeBlock) {
      codeBlockContent.push(line)
      continue
    }

    // Example label (Incorrect, Correct, Example, Usage, Implementation, etc.)
    // Match pattern: **Label:** or **Label (description):** at end of line
    // This distinguishes example labels from inline bold text like "**Trade-off:** some text"
    const labelMatch = line.match(/^\*\*([^:]+?):\*?\*?$/)
    if (labelMatch) {
      // Save previous example if it exists
      if (currentExample) {
        if (additionalText.length > 0) {
          currentExample.additionalText = additionalText.join('\n\n')
          additionalText = []
        }
        examples.push(currentExample)
      }
      afterCodeBlock = false
      hasCodeBlockForCurrentExample = false

      const fullLabel = labelMatch[1].trim()
      // Try to extract description from parentheses if present (handles simple cases)
      // For nested parentheses like "Incorrect (O(n) per lookup)", we keep the full label
      const descMatch = fullLabel.match(
        /^([A-Za-z]+(?:\s+[A-Za-z]+)*)\s*\(([^()]+)\)$/
      )
      currentExample = {
        label: descMatch ? descMatch[1].trim() : fullLabel,
        description: descMatch ? descMatch[2].trim() : undefined,
        code: '',
        language: codeBlockLanguage,
      }
      continue
    }

    // Reference links
    if (line.startsWith('Reference:') || line.startsWith('References:')) {
      // Save current example before processing references
      if (currentExample) {
        if (additionalText.length > 0) {
          currentExample.additionalText = additionalText.join('\n\n')
          additionalText = []
        }
        examples.push(currentExample)
        currentExample = null
      }

      const refMatch = line.match(/\[([^\]]+)\]\(([^)]+)\)/g)
      if (refMatch) {
        references.push(
          ...refMatch.map((ref) => {
            const m = ref.match(/\[([^\]]+)\]\(([^)]+)\)/)
            return m ? m[2] : ref
          })
        )
      }
      continue
    }

    // Regular text (explanation or additional context after examples)
    if (line.trim() && !line.startsWith('#')) {
      if (!currentExample && !inCodeBlock) {
        // Main explanation before any examples
        explanation += (explanation ? '\n\n' : '') + line
      } else if (currentExample && (afterCodeBlock || !hasCodeBlockForCurrentExample)) {
        // Text after a code block, or text in a section without a code block
        // (e.g., "When NOT to use this pattern:" with bullet points instead of code)
        additionalText.push(line)
      }
    }
  }

  // Handle last example if still open
  if (currentExample) {
    if (additionalText.length > 0) {
      currentExample.additionalText = additionalText.join('\n\n')
    }
    examples.push(currentExample)
  }

  // Infer section from filename patterns
  // Pattern: area-description.md where area determines section
  const filename = basename(filePath)
  const sectionMap: Record<string, number> = {
    schema: 1,
    query: 2,
    insert: 3,
    table: 4,
    index: 5,
    materialized: 6,
    cluster: 7,
    ops: 8,
    performance: 9,
  }

  // Extract area from filename (first part before first dash)
  const area = filename.split('-')[0]
  const section = frontmatter.section || sectionMap[area] || 0

  const rule: Rule = {
    id: '', // Will be assigned by build script based on sorted order
    title: frontmatter.title || title,
    section: section,
    subsection: undefined,
    impact: frontmatter.impact || impact,
    impactDescription: frontmatter.impactDescription || impactDescription,
    explanation: frontmatter.explanation || explanation.trim(),
    examples,
    references: frontmatter.references
      ? frontmatter.references.split(',').map((r: string) => r.trim())
      : references,
    tags: frontmatter.tags
      ? frontmatter.tags.split(',').map((t: string) => t.trim())
      : undefined,
  }

  return {
    section,
    subsection: 0,
    rule,
  }
}
```

## File: `packages/clickhouse-best-practices-build/src/types.ts`
```typescript
/**
 * Type definitions for ClickHouse Best Practices rules
 *
 * Adapted from github.com/vercel/agent-skills
 * Copyright (c) Vercel, Inc.
 * Licensed under MIT License
 */

export type ImpactLevel = 'CRITICAL' | 'HIGH' | 'MEDIUM-HIGH' | 'MEDIUM' | 'LOW-MEDIUM' | 'LOW'

export interface CodeExample {
  label: string // e.g., "Incorrect", "Correct", "Example"
  description?: string // Optional description before code
  code: string
  language?: string // Default: 'sql'
  additionalText?: string // Optional text after code block (explanations, reasons)
}

export interface Rule {
  id: string // e.g., "1.1", "2.3"
  title: string
  section: number // Main section number (1-8)
  subsection?: number // Subsection number within section
  impact: ImpactLevel
  impactDescription?: string // e.g., "2-10× improvement"
  explanation: string
  examples: CodeExample[]
  references?: string[] // URLs or citations
  tags?: string[] // For categorization/search
}

export interface Section {
  number: number
  title: string
  impact: ImpactLevel
  impactDescription?: string
  introduction?: string
  rules: Rule[]
}

export interface GuidelinesDocument {
  version: string
  organization: string
  date: string
  abstract: string
  sections: Section[]
  references?: string[]
  clickhouseVersion?: string
}
```

## File: `packages/clickhouse-best-practices-build/src/validate-sql.ts`
```typescript
#!/usr/bin/env node
/**
 * Validate SQL syntax in rule files using ClickHouse binary
 */

import { readdir, readFile, writeFile, mkdir, chmod, stat } from 'fs/promises'
import { join } from 'path'
import { tmpdir } from 'os'
import { exec } from 'child_process'
import { promisify } from 'util'
import { parseRuleFile } from './parser.js'
import { RULES_DIR, BUILD_DIR } from './config.js'

const execAsync = promisify(exec)

const CLICKHOUSE_VERSION = '24.1.8.22'
const CLICKHOUSE_BINARY_NAME = 'clickhouse'
const CLICKHOUSE_DIR = join(BUILD_DIR, 'bin')
const CLICKHOUSE_BINARY = join(CLICKHOUSE_DIR, CLICKHOUSE_BINARY_NAME)

interface SQLValidationError {
  file: string
  ruleTitle: string
  exampleLabel: string
  error: string
  sql: string
}

/**
 * Detect the current platform
 */
function getPlatform(): 'macos' | 'linux' | 'unsupported' {
  const platform = process.platform
  if (platform === 'darwin') return 'macos'
  if (platform === 'linux') return 'linux'
  return 'unsupported'
}

/**
 * Get the download URL for ClickHouse binary
 */
function getDownloadUrl(): string | null {
  const platform = getPlatform()
  if (platform === 'macos') {
    return `https://github.com/ClickHouse/ClickHouse/releases/download/v${CLICKHOUSE_VERSION}/clickhouse-macos`
  } else if (platform === 'linux') {
    return `https://github.com/ClickHouse/ClickHouse/releases/download/v${CLICKHOUSE_VERSION}/clickhouse`
  }
  return null
}

/**
 * Download ClickHouse binary if not present
 */
async function ensureClickHouse(): Promise<boolean> {
  try {
    // Check if binary already exists
    await stat(CLICKHOUSE_BINARY)
    console.log('✓ ClickHouse binary found')
    return true
  } catch {
    // Binary doesn't exist, need to download
    console.log('Downloading ClickHouse binary...')

    const url = getDownloadUrl()
    if (!url) {
      console.error('✗ Unsupported platform. SQL validation requires macOS or Linux.')
      return false
    }

    try {
      // Create bin directory if it doesn't exist
      await mkdir(CLICKHOUSE_DIR, { recursive: true })

      // Download using curl
      await execAsync(`curl -L -o "${CLICKHOUSE_BINARY}" "${url}"`)

      // Make executable
      await chmod(CLICKHOUSE_BINARY, 0o755)

      console.log('✓ ClickHouse binary downloaded')
      return true
    } catch (error) {
      console.error('✗ Failed to download ClickHouse binary:', error)
      return false
    }
  }
}

/**
 * Check if SQL contains dangerous patterns that could access external resources
 * Handles various obfuscation techniques: comments, whitespace, case variations
 */
function containsDangerousPatterns(sql: string): string | null {
  // Remove comments to prevent bypass via file/**/() or file--\n()
  const sqlNoComments = sql
    .replace(/\/\*[\s\S]*?\*\//g, ' ')  // Remove /* */ comments
    .replace(/--[^\n]*/g, ' ')           // Remove -- comments
    .replace(/\s+/g, ' ')                // Normalize whitespace

  const dangerous = [
    // File and network access
    { pattern: /\bfile\s*\(/i, description: 'file() table function (file system access)' },
    { pattern: /\burl\s*\(/i, description: 'url() table function (HTTP access)' },
    { pattern: /\bs3\s*\(/i, description: 's3() table function (cloud storage access)' },

    // Database connections
    { pattern: /\bmysql\s*\(/i, description: 'mysql() table function (database access)' },
    { pattern: /\bpostgresql\s*\(/i, description: 'postgresql() table function (database access)' },
    { pattern: /\bmongodb\s*\(/i, description: 'mongodb() table function (database access)' },
    { pattern: /\bhdfs\s*\(/i, description: 'hdfs() table function (HDFS access)' },
    { pattern: /\bodbc\s*\(/i, description: 'odbc() table function (ODBC access)' },
    { pattern: /\bjdbc\s*\(/i, description: 'jdbc() table function (JDBC access)' },

    // Command execution and remote access
    { pattern: /\bexecutable\s*\(/i, description: 'executable() table function (command execution)' },
    { pattern: /\bremote\s*\(/i, description: 'remote() table function (remote server access)' },
    { pattern: /\bcluster\s*\(/i, description: 'cluster() table function (cluster access)' },
    { pattern: /\binput\s*\(/i, description: 'input() table function (stdin access)' },

    // Timing and error-based exfiltration
    { pattern: /\bsleep\s*\(/i, description: 'sleep() function (timing attack vector)' },
    { pattern: /\bthrowIf\s*\(/i, description: 'throwIf() function (error-based exfiltration)' },

    // Note: system.* tables are allowed as they're commonly used in examples
    // and clickhouse-local runs in isolation with no sensitive data
  ]

  for (const { pattern, description } of dangerous) {
    if (pattern.test(sqlNoComments)) {
      return `Security: SQL contains dangerous pattern: ${description}`
    }
  }

  return null
}

/**
 * Validate a single SQL snippet
 */
async function validateSQL(sql: string): Promise<string | null> {
  // First check for dangerous patterns
  const dangerousPattern = containsDangerousPatterns(sql)
  if (dangerousPattern) {
    return dangerousPattern
  }

  // Write SQL to temporary file
  const tmpFile = join(tmpdir(), `clickhouse-validate-${Date.now()}.sql`)
  await writeFile(tmpFile, sql, 'utf-8')

  try {
    // Run clickhouse-local with the SQL file in restricted mode
    // Security restrictions to prevent arbitrary file/network access:
    // - readonly=2: Strictest readonly mode, blocks DDL and writes
    // - allow_introspection_functions=0: Blocks introspection functions
    // - allow_ddl=0: Explicitly disable DDL operations
    // - max_execution_time=10: Kill queries after 10 seconds (DoS protection)
    // - max_memory_usage=100000000: Limit memory to 100MB (DoS protection)
    // - max_rows_to_read=1000000: Limit rows read (DoS protection)
    // - user_files_path: Set to nonexistent path to block file() function
    // - format_schema_path: Set to nonexistent path to block schema loading
    // Note: Pattern blocking provides primary defense; these are secondary
    const { stderr } = await execAsync(
      `"${CLICKHOUSE_BINARY}" local --query-file "${tmpFile}" --output-format Null ` +
      `--readonly=2 --allow_introspection_functions=0 --allow_ddl=0 ` +
      `--max_execution_time=10 --max_memory_usage=100000000 --max_rows_to_read=1000000 ` +
      `--user_files_path="/dev/null" --format_schema_path="/dev/null" ` +
      `2>&1 || true`
    )

    // ClickHouse returns errors in stderr
    if (stderr && (stderr.includes('Exception') || stderr.includes('Error'))) {
      return stderr.trim()
    }

    return null
  } catch (error) {
    if (error instanceof Error) {
      return error.message
    }
    return String(error)
  } finally {
    // Clean up temp file
    try {
      await execAsync(`rm -f "${tmpFile}"`)
    } catch {}
  }
}

/**
 * Main validation function
 */
async function validateSQLInRules() {
  try {
    console.log('Validating SQL syntax in rule files...')
    console.log(`Rules directory: ${RULES_DIR}`)

    // Ensure ClickHouse binary is available
    const hasClickHouse = await ensureClickHouse()
    if (!hasClickHouse) {
      console.warn('⚠ Skipping SQL validation (ClickHouse binary not available)')
      process.exit(0)
    }

    // Read all rule files
    const files = await readdir(RULES_DIR)
    const ruleFiles = files.filter(f => f.endsWith('.md') && !f.startsWith('_') && f !== 'README.md')

    const allErrors: SQLValidationError[] = []
    let totalSQLExamples = 0

    for (const file of ruleFiles) {
      const filePath = join(RULES_DIR, file)
      try {
        const { rule } = await parseRuleFile(filePath)

        // Extract SQL examples
        for (const example of rule.examples) {
          if (example.code && example.code.trim() && (example.language === 'sql' || !example.language)) {
            totalSQLExamples++
            const error = await validateSQL(example.code)

            if (error) {
              allErrors.push({
                file,
                ruleTitle: rule.title,
                exampleLabel: example.label,
                error,
                sql: example.code.slice(0, 100) + (example.code.length > 100 ? '...' : '')
              })
            }
          }
        }
      } catch (error) {
        console.error(`Error processing ${file}:`, error)
      }
    }

    if (allErrors.length > 0) {
      console.error('\n✗ SQL validation failed:\n')
      allErrors.forEach(error => {
        console.error(`  ${error.file} (${error.ruleTitle})`)
        console.error(`    Example: ${error.exampleLabel}`)
        console.error(`    SQL: ${error.sql}`)
        console.error(`    Error: ${error.error}`)
        console.error('')
      })
      process.exit(1)
    } else {
      console.log(`✓ All ${totalSQLExamples} SQL examples are valid`)
    }
  } catch (error) {
    console.error('SQL validation failed:', error)
    process.exit(1)
  }
}

validateSQLInRules()
```

## File: `packages/clickhouse-best-practices-build/src/validate.ts`
```typescript
#!/usr/bin/env node
/**
 * Validate rule files follow the correct structure
 *
 * Adapted from github.com/vercel/agent-skills
 * Copyright (c) Vercel, Inc.
 * Licensed under MIT License
 */

import { readdir } from 'fs/promises'
import { join } from 'path'
import { Rule } from './types.js'
import { parseRuleFile } from './parser.js'
import { RULES_DIR } from './config.js'

interface ValidationError {
  file: string
  ruleId?: string
  message: string
}

/**
 * Validate a rule
 */
function validateRule(rule: Rule, file: string): ValidationError[] {
  const errors: ValidationError[] = []

  // Note: rule.id is auto-generated during build, not required in source files

  if (!rule.title || rule.title.trim().length === 0) {
    errors.push({ file, ruleId: rule.id, message: 'Missing or empty title' })
  }

  if (!rule.explanation || rule.explanation.trim().length === 0) {
    errors.push({ file, ruleId: rule.id, message: 'Missing or empty explanation' })
  }

  if (!rule.examples || rule.examples.length === 0) {
    errors.push({ file, ruleId: rule.id, message: 'Missing examples (need at least one bad and one good example)' })
  } else {
    // Filter out informational examples (notes, trade-offs, etc.) that don't have code
    const codeExamples = rule.examples.filter(e => e.code && e.code.trim().length > 0)

    const hasBad = codeExamples.some(e =>
      e.label.toLowerCase().includes('incorrect') ||
      e.label.toLowerCase().includes('wrong') ||
      e.label.toLowerCase().includes('bad')
    )
    const hasGood = codeExamples.some(e =>
      e.label.toLowerCase().includes('correct') ||
      e.label.toLowerCase().includes('good') ||
      e.label.toLowerCase().includes('usage') ||
      e.label.toLowerCase().includes('implementation') ||
      e.label.toLowerCase().includes('example')
    )

    if (codeExamples.length === 0) {
      errors.push({ file, ruleId: rule.id, message: 'Missing code examples' })
    } else if (!hasBad && !hasGood) {
      errors.push({ file, ruleId: rule.id, message: 'Missing bad/incorrect or good/correct examples' })
    }
  }

  const validImpacts: Rule['impact'][] = ['CRITICAL', 'HIGH', 'MEDIUM-HIGH', 'MEDIUM', 'LOW-MEDIUM', 'LOW']
  if (!validImpacts.includes(rule.impact)) {
    errors.push({ file, ruleId: rule.id, message: `Invalid impact level: ${rule.impact}. Must be one of: ${validImpacts.join(', ')}` })
  }

  return errors
}

/**
 * Main validation function
 */
async function validate() {
  try {
    console.log('Validating rule files...')
    console.log(`Rules directory: ${RULES_DIR}`)

    const files = await readdir(RULES_DIR)
    const ruleFiles = files.filter(f => f.endsWith('.md') && !f.startsWith('_'))

    const allErrors: ValidationError[] = []

    for (const file of ruleFiles) {
      const filePath = join(RULES_DIR, file)
      try {
        const { rule } = await parseRuleFile(filePath)
        const errors = validateRule(rule, file)
        allErrors.push(...errors)
      } catch (error) {
        allErrors.push({
          file,
          message: `Failed to parse: ${error instanceof Error ? error.message : String(error)}`
        })
      }
    }

    if (allErrors.length > 0) {
      console.error('\n✗ Validation failed:\n')
      allErrors.forEach(error => {
        console.error(`  ${error.file}${error.ruleId ? ` (${error.ruleId})` : ''}: ${error.message}`)
      })
      process.exit(1)
    } else {
      console.log(`✓ All ${ruleFiles.length} rule files are valid`)
    }
  } catch (error) {
    console.error('Validation failed:', error)
    process.exit(1)
  }
}

validate()
```

## File: `skills/clickhouse-best-practices/AGENTS.md`
```markdown
# ClickHouse Best Practices

**Version 0.1.0**  
ClickHouse Inc  
January 2026
ClickHouse 24.1+

> **Note:**  
> This document is mainly for agents and LLMs to follow when designing,  
> optimizing, or maintaining ClickHouse databases. Humans may also find it  
> useful, but guidance here is optimized for automation and consistency by  
> AI-assisted workflows.

---

## Abstract

Comprehensive best practices for ClickHouse database optimization. Covers schema design, query optimization, table engines, indexing strategies, materialized views, distributed operations, and operational best practices. Each rule includes detailed explanations, SQL examples comparing incorrect vs. correct implementations, and specific impact metrics to guide database design and query optimization.

---

## Table of Contents

1. [Schema Design](#1-schema-design) — **CRITICAL**
   - 1.1 [Avoid Nullable Unless Semantically Required](#11-avoid-nullable-unless-semantically-required)
   - 1.2 [Consider Starting Without Partitioning](#12-consider-starting-without-partitioning)
   - 1.3 [Filter on ORDER BY Columns in Queries](#13-filter-on-order-by-columns-in-queries)
   - 1.4 [Keep Partition Cardinality Low (100-1,000 Values)](#14-keep-partition-cardinality-low-100-1000-values)
   - 1.5 [Minimize Bit-Width for Numeric Types](#15-minimize-bit-width-for-numeric-types)
   - 1.6 [Order Columns by Cardinality (Low to High)](#16-order-columns-by-cardinality-low-to-high)
   - 1.7 [Plan PRIMARY KEY Before Table Creation](#17-plan-primary-key-before-table-creation)
   - 1.8 [Prioritize Filter Columns in ORDER BY](#18-prioritize-filter-columns-in-order-by)
   - 1.9 [Understand Partition Query Performance Trade-offs](#19-understand-partition-query-performance-trade-offs)
   - 1.10 [Use Enum for Finite Value Sets](#110-use-enum-for-finite-value-sets)
   - 1.11 [Use JSON Type for Dynamic Schemas](#111-use-json-type-for-dynamic-schemas)
   - 1.12 [Use LowCardinality for Repeated Strings](#112-use-lowcardinality-for-repeated-strings)
   - 1.13 [Use Native Types Instead of String](#113-use-native-types-instead-of-string)
   - 1.14 [Use Partitioning for Data Lifecycle Management](#114-use-partitioning-for-data-lifecycle-management)
2. [Query Optimization](#2-query-optimization) — **CRITICAL**
   - 2.1 [Choose the Right JOIN Algorithm](#21-choose-the-right-join-algorithm)
   - 2.2 [Consider Alternatives to JOINs](#22-consider-alternatives-to-joins)
   - 2.3 [Filter Tables Before Joining](#23-filter-tables-before-joining)
   - 2.4 [Optimize NULL Handling in Outer JOINs](#24-optimize-null-handling-in-outer-joins)
   - 2.5 [Use ANY JOIN When Only One Match Needed](#25-use-any-join-when-only-one-match-needed)
   - 2.6 [Use Data Skipping Indices for Non-ORDER BY Filters](#26-use-data-skipping-indices-for-non-order-by-filters)
   - 2.7 [Use Incremental MVs for Real-Time Aggregations](#27-use-incremental-mvs-for-real-time-aggregations)
   - 2.8 [Use Refreshable MVs for Complex Joins and Batch Workflows](#28-use-refreshable-mvs-for-complex-joins-and-batch-workflows)
3. [Insert Strategy](#3-insert-strategy) — **CRITICAL**
   - 3.1 [Avoid ALTER TABLE DELETE](#31-avoid-alter-table-delete)
   - 3.2 [Avoid ALTER TABLE UPDATE](#32-avoid-alter-table-update)
   - 3.3 [Avoid OPTIMIZE TABLE FINAL](#33-avoid-optimize-table-final)
   - 3.4 [Batch Inserts Appropriately (10K-100K rows)](#34-batch-inserts-appropriately-10k-100k-rows)
   - 3.5 [Use Async Inserts for High-Frequency Small Batches](#35-use-async-inserts-for-high-frequency-small-batches)
   - 3.6 [Use Native Format for Best Insert Performance](#36-use-native-format-for-best-insert-performance)

---

## 1. Schema Design

**Impact: CRITICAL**

Proper schema design is foundational to ClickHouse performance. ORDER BY is immutable after table creation; wrong choices require full data migration. Includes primary key selection, data types, partitioning strategy, and JSON usage. Column types and ordering can impact query speed by orders of magnitude.

### 1.1 Avoid Nullable Unless Semantically Required

**Impact: HIGH (Nullable adds storage overhead; use DEFAULT values instead)**

Nullable columns maintain a separate UInt8 column for tracking null values, increasing storage and degrading performance. Use DEFAULT values instead when feasible.

**Incorrect: Nullable everywhere**

```sql
CREATE TABLE users (
    id Nullable(UInt64),              -- IDs should never be null
    name Nullable(String),            -- Empty string is fine
    age Nullable(UInt8),              -- 0 is a valid default
    login_count Nullable(UInt32)      -- 0 is a valid default
)
```

**Correct: DEFAULT values, Nullable only when semantic**

```sql
CREATE TABLE users (
    id UInt64,                                    -- Never null
    name String DEFAULT '',                       -- Empty = unknown
    age UInt8 DEFAULT 0,                          -- 0 = unknown
    login_count UInt32 DEFAULT 0,                 -- 0 = never logged in
    deleted_at Nullable(DateTime),                -- NULL = not deleted (semantic!)
    parent_id Nullable(UInt64)                    -- NULL = no parent (semantic!)
)
```

**When Nullable IS appropriate:**

| Use Case | Why |

|----------|-----|

| `deleted_at` | NULL = "not deleted", timestamp = "deleted at X" |

| `parent_id` | NULL = "no parent", value = "has parent" |

| `discount_percent` | NULL = "no discount", 0 = "0% discount" |

**Defaults instead of Nullable:**

| Type | Default |

|------|---------|

| String | `''` (empty string) |

| UInt*/Int* | `0` |

| DateTime | `now()` or `toDateTime(0)` |

| UUID | `generateUUIDv4()` |

Reference: [https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/select-data-types](https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/select-data-types)

### 1.2 Consider Starting Without Partitioning

**Impact: MEDIUM (Add partitioning later when you have clear lifecycle requirements)**

Start without partitioning and add it later only if:

- You have clear data lifecycle requirements (retention, archiving)

- Your access patterns clearly benefit from partition pruning

- You understand the cardinality implications

**Example: start simple**

```sql
-- Start simple, no partitioning
CREATE TABLE events (
    timestamp DateTime,
    event_type LowCardinality(String),
    user_id UInt64
)
ENGINE = MergeTree()
ORDER BY (event_type, timestamp);

-- Add partitioning later if needed for lifecycle management
-- (requires table recreation or materialized view migration)
```

**When to add partitioning:**

| Need | Add Partitioning? |

|------|-------------------|

| Time-based data retention | Yes |

| Archive old data to cold storage | Yes |

| Query performance on time ranges | Maybe (test first) |

| No specific lifecycle needs | No |

Reference: [https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/choosing-a-partitioning-key](https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/choosing-a-partitioning-key)

### 1.3 Filter on ORDER BY Columns in Queries

**Impact: CRITICAL (Skipping prefix columns prevents index usage)**

Even with good schema design, queries must use ORDER BY columns to benefit. Skipping prefix columns or filtering on non-ORDER BY columns prevents index usage.

**Incorrect: skips prefix or uses non-ORDER BY columns**

```sql
-- Given: ORDER BY (tenant_id, event_type, timestamp)

-- Skips prefix columns - can't use index effectively
SELECT * FROM events WHERE event_type = 'click';

-- Filter on column not in ORDER BY - full table scan
SELECT * FROM events WHERE user_agent LIKE '%Chrome%';
```

**Correct: uses ORDER BY prefix**

```sql
-- Given: ORDER BY (tenant_id, event_type, timestamp)

-- Full prefix match - best performance
SELECT * FROM events
WHERE tenant_id = 123 AND event_type = 'click';

-- Partial prefix - still uses index
SELECT * FROM events WHERE tenant_id = 123;

-- Range on later column after equality on earlier
SELECT * FROM events
WHERE tenant_id = 123 AND event_type = 'click' AND timestamp >= '2024-01-01';
```

**Index usage reference:**

| Filter | Index Used? |

|--------|-------------|

| `WHERE tenant_id = 123` | Full |

| `WHERE tenant_id = 123 AND event_type = 'click'` | Full |

| `WHERE event_type = 'click'` | None (skipped prefix) |

| `WHERE timestamp > '2024-01-01'` | None (skipped both) |

Reference: [https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/choosing-a-primary-key](https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/choosing-a-primary-key)

### 1.4 Keep Partition Cardinality Low (100-1,000 Values)

**Impact: HIGH (Too many partitions cause part explosion and 'too many parts' errors)**

Too many distinct partition values create excessive data parts, eventually triggering "too many parts" errors. ClickHouse enforces limits via `max_parts_in_total` and `parts_to_throw_insert` settings.

**Incorrect: high cardinality partitioning**

```sql
-- High cardinality = too many partitions
CREATE TABLE events (...)
ENGINE = MergeTree()
PARTITION BY user_id  -- Millions of partitions!
ORDER BY (timestamp);

-- Daily partitions can grow unbounded over years
CREATE TABLE logs (...)
ENGINE = MergeTree()
PARTITION BY toDate(timestamp)  -- 3650 partitions over 10 years
ORDER BY (service, timestamp);
```

**Correct: bounded cardinality**

```sql
-- Monthly partitions = 12 per year, bounded cardinality
CREATE TABLE events (
    timestamp DateTime,
    event_type LowCardinality(String),
    user_id UInt64
)
ENGINE = MergeTree()
PARTITION BY toStartOfMonth(timestamp)
ORDER BY (event_type, timestamp);
```

**Validation:**

```sql
-- Check partition count and health
SELECT
    partition,
    count() as parts,
    sum(rows) as rows,
    formatReadableSize(sum(bytes_on_disk)) as size
FROM system.parts
WHERE table = 'events' AND active
GROUP BY partition
ORDER BY partition;

-- Warning signs: hundreds or thousands of partitions
```

Reference: [https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/choosing-a-partitioning-key](https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/choosing-a-partitioning-key)

### 1.5 Minimize Bit-Width for Numeric Types

**Impact: HIGH (Smaller types reduce storage and improve cache efficiency)**

Select the smallest numeric type that accommodates your data range. Prefer unsigned types when negative values aren't needed.

**Incorrect: oversized types**

```sql
CREATE TABLE metrics (
    status_code Int64,        -- HTTP codes are 100-599
    age Int64,                -- Human age fits in UInt8
    year Int64,               -- Years fit in UInt16
    item_count Int64          -- Often small numbers
)
```

**Correct: right-sized types**

```sql
CREATE TABLE metrics (
    status_code UInt16,       -- 0-65,535 (HTTP codes fit easily)
    age UInt8,                -- 0-255 (sufficient for age)
    year UInt16,              -- 0-65,535 (sufficient for years)
    item_count UInt32         -- 0-4 billion (adjust based on actual max)
)
```

**Numeric Type Reference:**

| Type | Range | Bytes |

|------|-------|-------|

| UInt8 | 0 to 255 | 1 |

| UInt16 | 0 to 65,535 | 2 |

| UInt32 | 0 to 4.3 billion | 4 |

| UInt64 | 0 to 18 quintillion | 8 |

| Int8 | -128 to 127 | 1 |

| Int16 | -32,768 to 32,767 | 2 |

| Int32 | -2.1 billion to 2.1 billion | 4 |

| Int64 | -9 quintillion to 9 quintillion | 8 |

Reference: [https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/select-data-types](https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/select-data-types)

### 1.6 Order Columns by Cardinality (Low to High)

**Impact: CRITICAL (Enables granule skipping; high-cardinality first prevents index pruning)**

Since the sparse primary index operates on data blocks (granules) rather than individual rows, low-cardinality leading columns create more useful index entries that can skip entire blocks. Place lower-cardinality columns before higher-cardinality ones in the ordering key.

**Incorrect: high cardinality first**

```sql
-- UUID first means no pruning benefit
CREATE TABLE events (...)
ENGINE = MergeTree()
ORDER BY (event_id, event_type, timestamp);
-- Every granule has different event_id values, index can't skip anything
```

**Correct: low cardinality first**

```sql
-- Low cardinality first enables pruning
CREATE TABLE events (...)
ENGINE = MergeTree()
ORDER BY (event_type, event_date, event_id);
-- Index can skip entire event_type groups
```

**Column Order Guidelines:**

| Position | Cardinality | Examples |

|----------|-------------|----------|

| 1st | Low (few distinct values) | event_type, status, country |

| 2nd | Date (coarse granularity) | toDate(timestamp) |

| 3rd+ | Medium-High | user_id, session_id |

| Last | High (if needed) | event_id, uuid |

**Tip:** Use `toDate(timestamp)` instead of raw `DateTime` columns when day-level filtering suffices - this reduces index size from 32-bit to 16-bit representations.

Reference: [https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/choosing-a-primary-key](https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/choosing-a-primary-key)

### 1.7 Plan PRIMARY KEY Before Table Creation

**Impact: CRITICAL (ORDER BY is immutable; wrong choice requires full data migration)**

ClickHouse's ORDER BY clause defines physical data ordering and the sparse index. Unlike other databases, **ORDER BY cannot be modified after table creation**. A wrong choice requires creating a new table and migrating all data.

**Incorrect: arbitrary ORDER BY without query analysis**

```sql
-- Creating table without analyzing query patterns
CREATE TABLE events (
    event_id UUID,
    user_id UInt64,
    timestamp DateTime
)
ENGINE = MergeTree()
ORDER BY (event_id);  -- Chosen arbitrarily

-- Later: "Most queries filter by user_id!"
-- Cannot fix with: ALTER TABLE events MODIFY ORDER BY (user_id, timestamp)
-- ERROR: Cannot modify ORDER BY
```

**Correct: query-driven ORDER BY selection**

```sql
-- Step 1: Document query patterns BEFORE creating table
/*
Query Analysis:
- 60% of queries: WHERE user_id = ? AND timestamp BETWEEN ? AND ?
- 25% of queries: WHERE event_type = ? AND timestamp > ?
- 15% of queries: WHERE event_id = ?

Conclusion: user_id and event_type are primary filters
*/

-- Step 2: Create table with correct ORDER BY
CREATE TABLE events (
    event_id UUID DEFAULT generateUUIDv4(),
    user_id UInt64,
    event_type LowCardinality(String),
    timestamp DateTime,
    event_date Date DEFAULT toDate(timestamp)
)
ENGINE = MergeTree()
PARTITION BY toYYYYMM(event_date)
ORDER BY (user_id, event_date, event_id);
```

**Pre-creation checklist:**

- [ ] Listed top 5-10 query patterns

- [ ] Identified columns in WHERE clauses with frequency

- [ ] Prioritized columns that exclude large numbers of rows

- [ ] Ordered columns by cardinality (low first, high last)

- [ ] Limited to 4-5 key columns (typically sufficient)

Reference: [https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/choosing-a-primary-key](https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/choosing-a-primary-key)

### 1.8 Prioritize Filter Columns in ORDER BY

**Impact: CRITICAL (Columns not in ORDER BY cause full table scans)**

Prioritize columns frequently used in query filters (WHERE clause), especially those that exclude large numbers of rows. Queries filtering on columns not in ORDER BY result in full table scans.

**Incorrect: ORDER BY doesn't match query patterns**

```sql
-- If most queries filter by tenant_id:
CREATE TABLE events (...)
ENGINE = MergeTree()
ORDER BY (event_id);  -- Queries by tenant_id will full-scan!
```

**Correct: ORDER BY matches filter patterns**

```sql
-- ORDER BY matches query filter patterns
CREATE TABLE events (...)
ENGINE = MergeTree()
ORDER BY (tenant_id, event_date, event_id);

-- Query now uses primary index:
SELECT * FROM events WHERE tenant_id = 123 AND event_date >= '2024-01-01';
```

**Validation:**

```sql
-- Verify index usage
EXPLAIN indexes = 1
SELECT * FROM events WHERE tenant_id = 123;
-- Look for "PrimaryKey" with Key Condition
```

Reference: [https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/choosing-a-primary-key](https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/choosing-a-primary-key)

### 1.9 Understand Partition Query Performance Trade-offs

**Impact: MEDIUM (Partition pruning helps some queries; spanning many partitions hurts others)**

Partitioning can help or hurt query performance:

- **Potential improvement**: Queries filtering by partition key may benefit from partition pruning

- **Potential degradation**: Queries spanning many partitions increase total parts scanned

ClickHouse automatically builds **MinMax indexes** on partition columns. Data merges occur **within partitions only**, not across them.

**Incorrect: query scans all partitions**

```sql
-- Query must scan all partitions
SELECT count(*) FROM events
WHERE event_type = 'click';  -- No partition pruning
```

**Correct: query prunes to single partition**

```sql
-- Query prunes to single partition
SELECT count(*) FROM events
WHERE timestamp >= '2024-01-01' AND timestamp < '2024-02-01'
  AND event_type = 'click';
```

Reference: [https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/choosing-a-partitioning-key](https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/choosing-a-partitioning-key)

### 1.10 Use Enum for Finite Value Sets

**Impact: MEDIUM (Insert-time validation and natural ordering; 1-2 bytes storage)**

Enum types provide validation at insert time and enable queries that exploit natural ordering. Use Enum8 (up to 256 values) or Enum16 (up to 65,536 values).

**Incorrect: String without validation**

```sql
CREATE TABLE orders (
    status String    -- No validation, typos like "shiped" allowed
)

-- Ordering requires CASE statements
SELECT * FROM orders ORDER BY
    CASE status
        WHEN 'pending' THEN 1
        WHEN 'processing' THEN 2
        WHEN 'shipped' THEN 3
    END;
```

**Correct: Enum with validation and ordering**

```sql
CREATE TABLE orders (
    status Enum8('pending' = 1, 'processing' = 2, 'shipped' = 3, 'delivered' = 4)
)

-- Insert validation: invalid values rejected
INSERT INTO orders VALUES ('shiped');  -- ERROR: Unknown element 'shiped'

-- Natural ordering works automatically
SELECT * FROM orders ORDER BY status;  -- Orders by enum value (1, 2, 3, 4)

-- Comparisons use natural order
SELECT * FROM orders WHERE status > 'processing';  -- shipped and delivered
```

**Enum Guidelines:**

| Scenario | Use |

|----------|-----|

| Fixed set of values known at schema time | Enum8/Enum16 |

| Values may change frequently | LowCardinality(String) |

| Need insert-time validation | Enum |

| Need natural ordering in queries | Enum |

| < 256 distinct values | Enum8 (1 byte) |

| 256-65,536 distinct values | Enum16 (2 bytes) |

Reference: [https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/select-data-types](https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/select-data-types)

### 1.11 Use JSON Type for Dynamic Schemas

**Impact: MEDIUM (Field-level querying for semi-structured data; use typed columns for known schemas)**

ClickHouse's JSON type splits JSON objects into separate sub-columns, enabling field-level query optimization. Use it for truly dynamic data, not everything.

**Incorrect: schema bloat or opaque String**

```sql
-- BAD: Hundreds of nullable columns for event properties
CREATE TABLE events (
    event_id UUID,
    prop_page_url Nullable(String),
    prop_button_id Nullable(String),
    -- ... 100 more nullable columns
)

-- BAD: JSON as String when you need field queries
CREATE TABLE events (
    event_id UUID,
    properties String  -- No field-level optimization
)
```

**Correct: JSON for dynamic, typed for known**

```sql
-- Use JSON type for dynamic properties
CREATE TABLE events (
    event_id UUID DEFAULT generateUUIDv4(),
    event_type LowCardinality(String),
    timestamp DateTime DEFAULT now(),
    properties JSON  -- Flexible schema with type inference
)
ENGINE = MergeTree()
ORDER BY (event_type, timestamp);

-- Query JSON paths directly
SELECT
    event_type,
    properties.url as page_url,
    properties.amount as purchase_amount
FROM events
WHERE event_type = 'page_view' AND properties.url = '/home';
```

**When to use JSON:**

```sql
CREATE TABLE events (
    properties JSON(
        url String,
        amount Float64,
        product_id UInt64
    )
)
```

| Scenario | Use JSON? |

|----------|-----------|

| Data structure varies unpredictably | Yes |

| Field types/schemas change over time | Yes |

| Need field-level querying | Yes |

| Fixed, known schema | No (use typed columns) |

| JSON as opaque blob (no field queries) | No (use String) |

**Optimization: specify types for known paths:**

Reference: [https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/use-json-where-appropriate](https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/use-json-where-appropriate)

### 1.12 Use LowCardinality for Repeated Strings

**Impact: HIGH (Dictionary encoding for <10K unique values; significant storage reduction)**

String columns with repeated values store each value repeatedly. LowCardinality uses dictionary encoding for significant storage reduction.

**Incorrect: plain String for repeated values**

```sql
CREATE TABLE events (
    country String,       -- "United States" stored 500M times
    browser String,       -- "Chrome" stored 300M times
    event_type String     -- "page_view" stored 800M times
)
```

**Correct: LowCardinality for low unique counts**

```sql
CREATE TABLE events (
    country LowCardinality(String),      -- ~200 unique values
    browser LowCardinality(String),      -- ~50 unique values
    event_type LowCardinality(String)    -- ~100 unique values
)
```

**When to use LowCardinality:**

```sql
-- Check cardinality before deciding
SELECT uniq(column_name) FROM table_name;
```

| Unique Values | Recommendation |

|---------------|----------------|

| < 10,000 | Use LowCardinality |

| > 10,000 | Use regular String |

**LowCardinality vs FixedString:**

```sql
-- FixedString: Only for truly fixed-length data
country_code FixedString(2),    -- "US", "DE", "JP" - always 2 chars

-- LowCardinality: For variable-length low-cardinality strings
country_name LowCardinality(String),  -- "United States", "Germany"
```

Reserve `FixedString` for strictly fixed-length data (e.g., 2-char country codes). For most low-cardinality text, `LowCardinality(String)` outperforms `FixedString`.

Reference: [https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/select-data-types](https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/select-data-types)

### 1.13 Use Native Types Instead of String

**Impact: CRITICAL (2-10x storage reduction; enables compression and correct semantics)**

Using String for all data wastes storage, prevents compression optimization, and makes comparisons slower. ClickHouse's column-oriented architecture benefits directly from optimal type selection.

**Incorrect: String for everything**

```sql
CREATE TABLE events (
    event_id String,        -- "550e8400-e29b-41d4-a716-446655440000" = 36 bytes
    user_id String,         -- "12345" = 5 bytes (no numeric operations)
    created_at String,      -- "2024-01-15 10:30:00" = 19 bytes
    count String,           -- "42" - can't do math!
    is_active String        -- "true" = 4 bytes
)
```

**Correct: native types**

```sql
CREATE TABLE events (
    event_id UUID DEFAULT generateUUIDv4(),     -- 16 bytes (vs 36)
    user_id UInt64,                              -- 8 bytes, numeric ops
    created_at DateTime DEFAULT now(),           -- 4 bytes (vs 19)
    count UInt32 DEFAULT 0,                      -- 4 bytes, math works
    is_active Bool DEFAULT true                  -- 1 byte (vs 4)
)
```

**Type Selection Quick Reference:**

| Data | Use | Avoid |

|------|-----|-------|

| Sequential IDs | UInt32/UInt64 | String |

| UUIDs | UUID | String |

| Status/Category | Enum8 or LowCardinality(String) | String |

| Timestamps | DateTime | DateTime64, String |

| Dates only | Date or Date32 | DateTime, String |

| Counts | UInt8/16/32 (smallest that fits) | Int64, String |

| Money | Decimal(P,S) or Int64 (cents) | Float64, String |

| Booleans | Bool or UInt8 | String |

Reference: [https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/select-data-types](https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/select-data-types)

### 1.14 Use Partitioning for Data Lifecycle Management

**Impact: HIGH (DROP PARTITION is instant; DELETE is expensive row-by-row scan)**

Partitioning is **primarily a data management technique, not a query optimization tool**. It excels at:

- **Dropping data**: Remove entire partitions as single metadata operations

- **TTL retention**: Implement time-based retention policies efficiently

- **Tiered storage**: Move old partitions to cold storage

- **Archiving**: Move partitions between tables

**Incorrect: no time alignment for lifecycle**

```sql
-- Cannot efficiently drop old data by time
CREATE TABLE events (...)
ENGINE = MergeTree()
PARTITION BY event_type  -- No time alignment
ORDER BY (timestamp);

-- Slow: must scan and delete row by row
DELETE FROM events WHERE timestamp < '2023-01-01';
```

**Correct: time-based for lifecycle**

```sql
CREATE TABLE events (
    timestamp DateTime,
    event_type LowCardinality(String)
)
ENGINE = MergeTree()
PARTITION BY toStartOfMonth(timestamp)
ORDER BY (event_type, timestamp)
TTL timestamp + INTERVAL 1 YEAR DELETE;  -- Drops whole partitions

-- Fast: metadata-only operation
ALTER TABLE events DROP PARTITION '202301';

-- Archive to cold storage
ALTER TABLE events_archive ATTACH PARTITION '202301' FROM events;
```

Reference: [https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/choosing-a-partitioning-key](https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/choosing-a-partitioning-key)

---

## 2. Query Optimization

**Impact: CRITICAL**

Query patterns dramatically affect performance. JOIN algorithms, filtering strategies, skipping indices, and materialized views can reduce query time from minutes to milliseconds. Pre-computed aggregations read thousands of rows instead of billions.

### 2.1 Choose the Right JOIN Algorithm

**Impact: CRITICAL (Wrong algorithm causes OOM; right algorithm handles large tables efficiently)**

ClickHouse's default hash join loads the RIGHT table entirely into memory. Choose the right algorithm based on table sizes and constraints.

**Algorithm selection:**

| Algorithm | Best For | Trade-off |

|-----------|----------|-----------|

| `parallel_hash` | Small-to-medium in-memory tables | Default since 24.11; fast, concurrent |

| `hash` | General purpose, all join types | Single-threaded hash table build |

| `direct` | Dictionary lookups (INNER/LEFT only) | Fastest; no hash table construction |

| `full_sorting_merge` | Tables already sorted on join key | Skips sort if pre-ordered; low memory |

| `partial_merge` | Large tables, memory-constrained | Minimized memory; slower execution |

| `grace_hash` | Large datasets, tunable memory | Flexible; disk-spilling capability |

| `auto` | Adaptive algorithm selection | Tries hash first, falls back on memory pressure |

**Example usage:**

```sql
-- Let ClickHouse choose automatically
SET join_algorithm = 'auto';

-- For large-to-large joins where memory is constrained
SET join_algorithm = 'partial_merge';
SELECT * FROM large_a JOIN large_b ON large_b.id = large_a.id;

-- When joining by primary key columns, sort-merge skips sorting step
SET join_algorithm = 'full_sorting_merge';
SELECT * FROM table_a a JOIN table_b b ON b.pk_col = a.pk_col;
```

**Note:** ClickHouse 24.12+ automatically positions smaller tables on the right side. For earlier versions, manually ensure the smaller table is on the RIGHT.

Reference: [https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/minimize-optimize-joins](https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/minimize-optimize-joins)

### 2.2 Consider Alternatives to JOINs

**Impact: CRITICAL (Dictionaries and denormalization shift work from query time to insert time)**

Repeated JOINs to dimension tables add overhead. Dictionaries or denormalization shift computational work from query time to insert/pre-processing time.

**Incorrect: JOIN on every query**

```sql
-- JOIN on every query
SELECT o.order_id, c.name, c.email
FROM orders o
JOIN customers c ON c.id = o.customer_id
WHERE o.created_at > '2024-01-01';
```

**Correct - Dictionary Lookup:**

```sql
-- Create dictionary
CREATE DICTIONARY customer_dict (
    id UInt64,
    name String,
    email String
)
PRIMARY KEY id
SOURCE(CLICKHOUSE(TABLE 'customers'))
LAYOUT(HASHED())
LIFETIME(MIN 300 MAX 360);

-- Use dictGet instead of JOIN (uses direct join algorithm - fastest)
SELECT
    order_id,
    dictGet('customer_dict', 'name', customer_id) as customer_name,
    dictGet('customer_dict', 'email', customer_id) as customer_email
FROM orders
WHERE created_at > '2024-01-01';
```

**Correct - Denormalization:**

```sql
-- Denormalized table with materialized view
CREATE MATERIALIZED VIEW orders_enriched_mv TO orders_enriched AS
SELECT
    o.order_id, o.customer_id,
    c.name as customer_name,
    c.email as customer_email,
    o.total, o.created_at
FROM orders o
JOIN customers c ON c.id = o.customer_id;
```

**Approach comparison:**

| Approach | Use Case | Performance |

|----------|----------|-------------|

| Dictionary | Frequent lookups to small dimension | Fastest (in-memory) |

| Denormalization | Analytics always need enriched data | Fast (no join at query) |

| IN subquery | Existence filtering | Often faster than JOIN |

| JOIN | Infrequent or complex joins | Acceptable |

**Critical dictionary caveat:** Dictionaries silently deduplicate duplicate keys, retaining only the final value. Only use when source has unique keys.

Reference: [https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/minimize-optimize-joins](https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/minimize-optimize-joins)

### 2.3 Filter Tables Before Joining

**Impact: CRITICAL (Joining full tables then filtering wastes resources)**

Joining full tables then filtering wastes resources. Add filtering in `WHERE` or `JOIN ON` clauses. If automatic pushdown fails, restructure as a subquery.

**Incorrect: join then filter**

```sql
-- Joins entire tables, then filters
SELECT o.order_id, c.name, o.total
FROM orders o
JOIN customers c ON c.id = o.customer_id
WHERE o.created_at > '2024-01-01' AND c.country = 'US';
```

**Correct: filter in subqueries before joining**

```sql
-- Filter in subqueries before joining
SELECT o.order_id, c.name, o.total
FROM (
    SELECT order_id, customer_id, total
    FROM orders
    WHERE created_at > '2024-01-01'
) o
JOIN (
    SELECT id, name
    FROM customers
    WHERE country = 'US'
) c ON c.id = o.customer_id;
```

**Even better - aggregate before joining:**

```sql
SELECT c.country, o.total_revenue
FROM (
    SELECT customer_id, sum(total) as total_revenue
    FROM orders
    WHERE created_at > '2024-01-01'
    GROUP BY customer_id
) o
JOIN customers c ON c.id = o.customer_id;
```

Reference: [https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/minimize-optimize-joins](https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/minimize-optimize-joins)

### 2.4 Optimize NULL Handling in Outer JOINs

**Impact: MEDIUM (Default values instead of NULL reduces memory overhead)**

Set `join_use_nulls = 0` to use default column values instead of NULL markers, reducing memory overhead compared to Nullable wrappers.

**Example:**

```sql
-- Use default values instead of NULLs for non-matching rows
SET join_use_nulls = 0;

SELECT o.order_id, c.name
FROM orders o
LEFT JOIN customers c ON c.id = o.customer_id;
-- Non-matching rows get '' for name instead of NULL
```

**When to use:**

| Setting | Behavior | Use Case |

|---------|----------|----------|

| `join_use_nulls = 0` | Default values (empty string, 0) for non-matches | When you can handle default values |

| `join_use_nulls = 1` (default) | NULL for non-matches | When you need to distinguish "no match" from "matched with default" |

Reference: [https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/minimize-optimize-joins](https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/minimize-optimize-joins)

### 2.5 Use ANY JOIN When Only One Match Needed

**Impact: HIGH (Returns first match only; less memory and faster execution)**

Use `ANY` JOINs when you only need a single match rather than all matches. They consume less memory and execute faster.

**Incorrect: returns all matches**

```sql
-- Returns all matching rows, uses more memory
SELECT o.order_id, c.name
FROM orders o
LEFT JOIN customers c ON c.id = o.customer_id;
```

**Correct: returns first match only**

```sql
-- Returns only first match per row, faster and less memory
SELECT o.order_id, c.name
FROM orders o
LEFT ANY JOIN customers c ON c.id = o.customer_id;
```

**ANY JOIN types:**

| Type | Behavior |

|------|----------|

| `LEFT ANY JOIN` | At most one match from right table |

| `INNER ANY JOIN` | At most one match, only matching rows |

| `RIGHT ANY JOIN` | At most one match from left table |

Reference: [https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/minimize-optimize-joins](https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/minimize-optimize-joins)

### 2.6 Use Data Skipping Indices for Non-ORDER BY Filters

**Impact: HIGH (Up to 60x faster queries by skipping irrelevant granules)**

Queries filtering on columns not in ORDER BY cannot use the primary index and result in full scans. Data skipping indices store metadata about blocks and skip granules that definitely don't match.

**Important:** Skip indices should be considered **after** optimizing data types, primary key selection, and materialized views.

**When to use:**

- High overall cardinality but low cardinality within blocks

- Rare values critical for search (error codes, specific IDs)

- Column correlates with primary key

**When NOT to use:**

- As a first optimization step

- Matching values scattered across many blocks

- Without testing on real data

**Incorrect: filtering on non-ORDER BY column**

```sql
CREATE TABLE events (
    event_type LowCardinality(String),
    timestamp DateTime,
    user_id UInt64    -- Not in ORDER BY
)
ENGINE = MergeTree()
ORDER BY (event_type, toDate(timestamp));

-- Query filters on user_id - scans all matching event_type
SELECT * FROM events
WHERE event_type = 'click' AND user_id = 12345;
```

**Correct: add skipping index**

```sql
CREATE TABLE events (
    event_type LowCardinality(String),
    timestamp DateTime,
    user_id UInt64,
    INDEX idx_user_id user_id TYPE bloom_filter GRANULARITY 4
)
ENGINE = MergeTree()
ORDER BY (event_type, toDate(timestamp));

-- Or add to existing table
ALTER TABLE events ADD INDEX idx_user_id user_id TYPE bloom_filter GRANULARITY 4;
ALTER TABLE events MATERIALIZE INDEX idx_user_id;
```

**Index types:**

| Type | Best For | Example Filter |

|------|----------|----------------|

| `bloom_filter` | Equality on high-cardinality | `WHERE user_id = 123` |

| `set(N)` | Low cardinality (N unique values) | `WHERE status IN ('a','b')` |

| `minmax` | Range queries | `WHERE amount > 1000` |

| `ngrambf_v1` | Text search | `WHERE text LIKE '%term%'` |

| `tokenbf_v1` | Token search | `WHERE hasToken(text, 'word')` |

**Validation:**

```sql
EXPLAIN indexes = 1
SELECT * FROM events WHERE user_id = 12345;
-- Look for "Skip" in output showing granules skipped
```

Reference: [https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/use-data-skipping-indices-where-appropriate](https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/use-data-skipping-indices-where-appropriate)

### 2.7 Use Incremental MVs for Real-Time Aggregations

**Impact: HIGH (Read thousands of rows instead of billions; minimal cluster overhead)**

Incremental MVs automatically apply the view's query to new data blocks at insert time. Results are written to a target table and partial results merge over time.

**Incorrect: full aggregation on every query**

```sql
-- Full aggregation on every dashboard load
SELECT
    event_type,
    toStartOfHour(timestamp) as hour,
    count() as events,
    uniq(user_id) as unique_users
FROM events
WHERE timestamp >= now() - INTERVAL 7 DAY
GROUP BY event_type, hour;
-- Scans 7 days of data every time (billions of rows)
```

**Correct: incremental MV with pre-aggregation**

```sql
-- Create target table for aggregated data
CREATE TABLE events_hourly (
    event_type LowCardinality(String),
    hour DateTime,
    events AggregateFunction(count),
    unique_users AggregateFunction(uniq, UInt64)
)
ENGINE = AggregatingMergeTree()
ORDER BY (event_type, hour);

-- Create materialized view to populate incrementally
CREATE MATERIALIZED VIEW events_hourly_mv TO events_hourly AS
SELECT
    event_type,
    toStartOfHour(timestamp) as hour,
    countState() as events,
    uniqState(user_id) as unique_users
FROM events
GROUP BY event_type, hour;

-- Query the pre-aggregated data
SELECT
    event_type, hour,
    countMerge(events) as events,
    uniqMerge(unique_users) as unique_users
FROM events_hourly
WHERE hour >= now() - INTERVAL 7 DAY
GROUP BY event_type, hour;
-- Reads thousands of rows instead of billions
```

**Key points:**

- Use `-State` functions in MV, `-Merge` functions in query

- Incremental - existing data not automatically included (backfill separately)

- Minimal cluster overhead at insert time

Reference: [https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/use-materialized-views](https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/use-materialized-views)

### 2.8 Use Refreshable MVs for Complex Joins and Batch Workflows

**Impact: HIGH (Sub-millisecond queries with periodic refresh; ideal for complex joins)**

Refreshable MVs execute queries periodically on a schedule. The full query re-executes and overwrites (or appends to) the target table.

**Best for:**

- Sub-millisecond latency where minor staleness is acceptable

- Caching "top N" results or lookup tables

- Complex multi-table joins requiring denormalization

- Batch workflows and DAG dependencies

**Incorrect: expensive join on every request**

```sql
-- Complex join executed on every request
SELECT
    o.order_id, o.total,
    c.name as customer_name,
    p.name as product_name
FROM orders o
JOIN customers c ON o.customer_id = c.id
JOIN products p ON o.product_id = p.id
WHERE o.created_at >= now() - INTERVAL 1 DAY;
```

**Correct: refreshable MV**

```sql
-- Create refreshable MV that runs every 5 minutes
CREATE MATERIALIZED VIEW orders_denormalized
REFRESH EVERY 5 MINUTE
ENGINE = MergeTree()
ORDER BY (created_at, order_id)
AS SELECT
    o.order_id, o.created_at, o.total,
    c.name as customer_name, c.segment,
    p.name as product_name
FROM orders o
JOIN customers c ON o.customer_id = c.id
JOIN products p ON o.product_id = p.id
WHERE o.created_at >= now() - INTERVAL 1 DAY;

-- Query the pre-joined data (sub-millisecond)
SELECT * FROM orders_denormalized WHERE segment = 'enterprise';
```

**APPEND vs REPLACE modes:**

| Mode | Behavior | Use Case |

|------|----------|----------|

| `REPLACE` (default) | Overwrites previous contents | Current state, lookup tables |

| `APPEND` | Adds new rows to existing data | Periodic snapshots, historical accumulation |

**Critical warning:** Query should run quickly compared to refresh interval. Don't schedule every 10 seconds if the query takes 10+ seconds.

Reference: [https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/use-materialized-views](https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/use-materialized-views)

---

## 3. Insert Strategy

**Impact: CRITICAL**

Each INSERT creates a data part. Single-row inserts overwhelm the merge process. Proper batching (10K-100K rows), async inserts for high-frequency writes, mutation avoidance, and letting background merges work are essential for stable cluster performance.

### 3.1 Avoid ALTER TABLE DELETE

**Impact: CRITICAL (Use lightweight DELETE, CollapsingMergeTree, or DROP PARTITION instead)**

`ALTER TABLE DELETE` is a mutation that rewrites entire data parts. Use alternatives like lightweight DELETE, CollapsingMergeTree, or DROP PARTITION.

**Incorrect: mutation delete**

```sql
-- Mutation delete for cleanup
ALTER TABLE orders DELETE WHERE status = 'cancelled';

-- Time-based cleanup via mutation (very expensive)
ALTER TABLE sessions DELETE WHERE created_at < now() - INTERVAL 7 DAY;
```

**Correct - CollapsingMergeTree:**

```sql
CREATE TABLE orders (
    order_id UInt64,
    customer_id UInt64,
    total Decimal(10,2),
    sign Int8  -- 1 = active, -1 = deleted
)
ENGINE = CollapsingMergeTree(sign)
ORDER BY order_id;

-- Insert order
INSERT INTO orders VALUES (123, 456, 99.99, 1);

-- "Delete" by inserting with sign = -1
INSERT INTO orders VALUES (123, 456, 99.99, -1);

-- Query collapses +1 and -1 pairs
SELECT order_id, sum(total * sign) as total
FROM orders GROUP BY order_id HAVING sum(sign) > 0;
```

**Correct - Lightweight Deletes (23.3+):**

```sql
-- Marks rows, doesn't rewrite immediately
DELETE FROM orders WHERE status = 'cancelled';
-- Physical deletion happens during normal merges
```

**Correct - DROP PARTITION for Bulk Deletion:**

```sql
-- Instant deletion of old data
ALTER TABLE events DROP PARTITION '202301';

-- Much faster than:
ALTER TABLE events DELETE WHERE toYYYYMM(timestamp) = 202301;
```

**Delete strategy comparison:**

| Method | Speed | When to Use |

|--------|-------|-------------|

| ALTER DELETE | Slow | Rare corrections only |

| CollapsingMergeTree | Fast | Frequent soft deletes |

| Lightweight DELETE | Medium | Occasional deletes |

| DROP PARTITION | Instant | Bulk deletion by partition |

Reference: [https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/avoid-mutations](https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/avoid-mutations)

### 3.2 Avoid ALTER TABLE UPDATE

**Impact: CRITICAL (Mutations rewrite entire parts; use ReplacingMergeTree instead)**

`ALTER TABLE UPDATE` is a mutation - an asynchronous background process that rewrites entire data parts affected by the change. This is extremely expensive for frequent or large-scale operations.

**Why mutations are problematic:**

- **Write amplification:** Rewrite complete parts even for minor changes

- **Disk I/O spike:** Degrades overall cluster performance

- **No rollback:** Cannot be rolled back after submission

- **Inconsistent reads:** SELECT may read mix of mutated and unmutated parts

**Incorrect: mutation for updates**

```sql
-- Rewrites potentially huge amounts of data
ALTER TABLE users UPDATE status = 'inactive'
WHERE last_login < now() - INTERVAL 90 DAY;

-- Frequent row updates via mutation
ALTER TABLE inventory UPDATE quantity = quantity - 1
WHERE product_id = 123;
-- If product exists across 100 parts, rewrites ALL 100 parts
```

**Correct: ReplacingMergeTree**

```sql
-- Table design for updates
CREATE TABLE users (
    user_id UInt64,
    name String,
    status LowCardinality(String),
    updated_at DateTime DEFAULT now()
)
ENGINE = ReplacingMergeTree(updated_at)
ORDER BY user_id;

-- "Update" by inserting new version
INSERT INTO users (user_id, name, status)
VALUES (123, 'John', 'inactive');

-- Query with FINAL to get latest version
SELECT * FROM users FINAL WHERE user_id = 123;

-- Or use aggregation
SELECT user_id, argMax(status, updated_at) as status
FROM users GROUP BY user_id;
```

Reference: [https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/avoid-mutations](https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/avoid-mutations)

### 3.3 Avoid OPTIMIZE TABLE FINAL

**Impact: HIGH (Forces expensive merge of all parts; let background merges work)**

`OPTIMIZE TABLE ... FINAL` forces immediate merge of all parts into one part per partition. This is resource-intensive and rarely necessary. ClickHouse already performs smart background merges.

**Note:** `OPTIMIZE FINAL` is not the same as `FINAL`. The `FINAL` modifier in SELECT queries may be necessary for deduplicated results in ReplacingMergeTree and is generally fine to use.

**Incorrect: OPTIMIZE FINAL after inserts**

```sql
-- Running OPTIMIZE FINAL after every batch insert
INSERT INTO events SELECT * FROM staging_events;
OPTIMIZE TABLE events FINAL;  -- Expensive and unnecessary!

-- Scheduled OPTIMIZE FINAL jobs
-- Cron: 0 * * * * clickhouse-client -q "OPTIMIZE TABLE events FINAL"
```

**Correct: let background merges work**

```sql
-- Let background merges handle optimization
INSERT INTO events SELECT * FROM staging_events;
-- Done! ClickHouse merges automatically

-- For ReplacingMergeTree deduplication, use FINAL in queries
SELECT * FROM events FINAL WHERE user_id = 123;
-- Instead of running OPTIMIZE FINAL to deduplicate
```

**Problems with OPTIMIZE FINAL:**

- Rewrites entire partition regardless of need

- Ignores the ~150 GB part size safeguard

- Can cause memory pressure or OOM errors

- Lengthy execution time for large datasets

**When OPTIMIZE FINAL may be acceptable:**

- Finalizing data before table freezing

- Preparing data for export operations

- One-time operations, not regular workflows

**Better alternatives:**

| Need | Alternative |

|------|-------------|

| Deduplicate ReplacingMergeTree | Use `FINAL` modifier in SELECT |

| Reduce part count | Rely on background merges |

Reference: [https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/avoid-optimize-final](https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/avoid-optimize-final)

### 3.4 Batch Inserts Appropriately (10K-100K rows)

**Impact: CRITICAL (Each INSERT creates a part; single-row inserts overwhelm merge process)**

Each INSERT creates a new data part. Single-row or small-batch inserts create thousands of tiny parts, overwhelming the merge process and causing cluster instability.

**Incorrect: single-row or tiny batches**

```python
# Single-row inserts - creates 10,000 parts!
for event in events:
    client.execute("INSERT INTO events VALUES", [event])

# Tiny batches - still too many parts
for batch in chunks(events, 100):  # 100 rows per INSERT
    client.execute("INSERT INTO events VALUES", batch)
```

**Correct: proper batch size**

```python
# Ideal batch size: 10,000-100,000 rows
BATCH_SIZE = 10_000
for batch in chunks(events, BATCH_SIZE):
    client.execute("INSERT INTO events VALUES", batch)
```

**Recommended batch sizes:**

| Threshold | Value |

|-----------|-------|

| Minimum | 1,000 rows |

| Ideal range | 10,000-100,000 rows |

| Insert rate (sync) | ~1 insert per second |

**Validation:**

```sql
-- Monitor part count (>3000 per partition blocks inserts)
SELECT table, count() as parts, sum(rows) as total_rows
FROM system.parts
WHERE active AND database = 'default'
GROUP BY table
ORDER BY parts DESC;
```

Reference: [https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/selecting-an-insert-strategy](https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/selecting-an-insert-strategy)

### 3.5 Use Async Inserts for High-Frequency Small Batches

**Impact: HIGH (Server-side buffering when client batching isn't practical)**

When client-side batching isn't practical, async inserts buffer server-side and create larger parts automatically.

**Incorrect: small batches without async**

```python
# Small batches without async_insert - creates too many parts
for batch in chunks(events, 100):
    client.execute("INSERT INTO events VALUES", batch)
```

**Correct: enable async inserts**

```sql
-- Configure server-side for specific users
ALTER USER my_app_user SETTINGS
    async_insert = 1,
    wait_for_async_insert = 1,
    async_insert_max_data_size = 10000000,  -- Flush at 10MB
    async_insert_busy_timeout_ms = 1000;    -- Flush after 1s
```

**Flush conditions: whichever occurs first**

- Buffer reaches `async_insert_max_data_size`

- Time threshold `async_insert_busy_timeout_ms` elapses

- Maximum insert queries accumulate

**Return modes:**

| Setting | Behavior | Use Case |

|---------|----------|----------|

| `wait_for_async_insert=1` | Waits for flush, confirms durability | **Recommended** |

| `wait_for_async_insert=0` | Fire-and-forget, unaware of errors | **Risky** - only if you accept data loss |

Reference: [https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/selecting-an-insert-strategy](https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/selecting-an-insert-strategy)

### 3.6 Use Native Format for Best Insert Performance

**Impact: MEDIUM (Native format is most efficient; JSONEachRow is expensive to parse)**

Data format affects insert performance. Native format is column-oriented with minimal parsing overhead.

**Performance Ranking: fastest to slowest**

| Format | Notes |

|--------|-------|

| **Native** | Most efficient. Column-oriented, minimal parsing. Recommended. |

| **RowBinary** | Efficient row-based alternative |

| **JSONEachRow** | Easier to use but expensive to parse |

**Example:**

```python
# Use Native format for best performance
client.execute("INSERT INTO events VALUES", data, settings={'input_format': 'Native'})
```

Reference: [https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/selecting-an-insert-strategy](https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/selecting-an-insert-strategy)

---

## References

1. [https://clickhouse.com/docs](https://clickhouse.com/docs)
2. [https://github.com/ClickHouse/ClickHouse](https://github.com/ClickHouse/ClickHouse)
```

## File: `skills/clickhouse-best-practices/README.md`
```markdown
# ClickHouse Best Practices

Agent skill providing comprehensive ClickHouse guidance for schema design, query optimization, and data ingestion.

## Installation

```bash
npx skills add ClickHouse/clickhouse-agent-skills
```

## What's Included

**28 atomic rules** organized by prefix:

| Prefix | Count | Coverage |
|--------|-------|----------|
| `schema-pk-*` | 4 | PRIMARY KEY selection, cardinality ordering |
| `schema-types-*` | 5 | Data types, LowCardinality, Nullable |
| `schema-partition-*` | 4 | Partitioning strategy, lifecycle management |
| `schema-json-*` | 1 | JSON type usage |
| `query-join-*` | 5 | JOIN algorithms, filtering, alternatives |
| `query-index-*` | 1 | Data skipping indices |
| `query-mv-*` | 2 | Incremental and refreshable MVs |
| `insert-batch-*` | 1 | Batch sizing (10K-100K rows) |
| `insert-async-*` | 2 | Async inserts, data formats |
| `insert-mutation-*` | 2 | Mutation avoidance |
| `insert-optimize-*` | 1 | OPTIMIZE FINAL avoidance |

## Trigger Phrases

This skill activates when you:
- "Create a table for..."
- "Optimize this query..."
- "Design a schema for..."
- "Why is this query slow?"
- "How should I insert data into..."
- "Should I use UPDATE or..."

## Files

| File | Purpose |
|------|---------|
| `SKILL.md` | Quick reference and decision frameworks |
| `AGENTS.md` | Complete rule reference (auto-generated) |
| `rules/*.md` | Individual rule definitions |

## Related Documentation

All rules link to official ClickHouse documentation:
- [ClickHouse Best Practices](https://clickhouse.com/brain/knowledge/docs_legacy/best-practices)
```

## File: `skills/clickhouse-best-practices/SKILL.md`
```markdown
---
name: clickhouse-best-practices
description: MUST USE when reviewing ClickHouse schemas, queries, or configurations. Contains 28 rules that MUST be checked before providing recommendations. Always read relevant rule files and cite specific rules in responses.
license: Apache-2.0
metadata:
  author: ClickHouse Inc
  version: "0.3.0"
---

# ClickHouse Best Practices

Comprehensive guidance for ClickHouse covering schema design, query optimization, and data ingestion. Contains 28 rules across 3 main categories (schema, query, insert), prioritized by impact.

> **Official docs:** [ClickHouse Best Practices](https://clickhouse.com/brain/knowledge/docs_legacy/best-practices)

## IMPORTANT: How to Apply This Skill

**Before answering ClickHouse questions, follow this priority order:**

1. **Check for applicable rules** in the `rules/` directory
2. **If rules exist:** Apply them and cite them in your response using "Per `rule-name`..."
3. **If no rule exists:** Use the LLM's ClickHouse knowledge or search documentation
4. **If uncertain:** Use web search for current best practices
5. **Always cite your source:** rule name, "general ClickHouse guidance", or URL

**Why rules take priority:** ClickHouse has specific behaviors (columnar storage, sparse indexes, merge tree mechanics) where general database intuition can be misleading. The rules encode validated, ClickHouse-specific guidance.

### For Formal Reviews

When performing a formal review of schemas, queries, or data ingestion:

---

## Review Procedures

### For Schema Reviews (CREATE TABLE, ALTER TABLE)

**Read these rule files in order:**

1. `rules/schema-pk-plan-before-creation.md` - ORDER BY is immutable
2. `rules/schema-pk-cardinality-order.md` - Column ordering in keys
3. `rules/schema-pk-prioritize-filters.md` - Filter column inclusion
4. `rules/schema-types-native-types.md` - Proper type selection
5. `rules/schema-types-minimize-bitwidth.md` - Numeric type sizing
6. `rules/schema-types-lowcardinality.md` - LowCardinality usage
7. `rules/schema-types-avoid-nullable.md` - Nullable vs DEFAULT
8. `rules/schema-partition-low-cardinality.md` - Partition count limits
9. `rules/schema-partition-lifecycle.md` - Partitioning purpose

**Check for:**
- [ ] PRIMARY KEY / ORDER BY column order (low-to-high cardinality)
- [ ] Data types match actual data ranges
- [ ] LowCardinality applied to appropriate string columns
- [ ] Partition key cardinality bounded (100-1,000 values)
- [ ] ReplacingMergeTree has version column if used

### For Query Reviews (SELECT, JOIN, aggregations)

**Read these rule files:**

1. `rules/query-join-choose-algorithm.md` - Algorithm selection
2. `rules/query-join-filter-before.md` - Pre-join filtering
3. `rules/query-join-use-any.md` - ANY vs regular JOIN
4. `rules/query-index-skipping-indices.md` - Secondary index usage
5. `rules/schema-pk-filter-on-orderby.md` - Filter alignment with ORDER BY

**Check for:**
- [ ] Filters use ORDER BY prefix columns
- [ ] JOINs filter tables before joining (not after)
- [ ] Correct JOIN algorithm for table sizes
- [ ] Skipping indices for non-ORDER BY filter columns

### For Insert Strategy Reviews (data ingestion, updates, deletes)

**Read these rule files:**

1. `rules/insert-batch-size.md` - Batch sizing requirements
2. `rules/insert-mutation-avoid-update.md` - UPDATE alternatives
3. `rules/insert-mutation-avoid-delete.md` - DELETE alternatives
4. `rules/insert-async-small-batches.md` - Async insert usage
5. `rules/insert-optimize-avoid-final.md` - OPTIMIZE TABLE risks

**Check for:**
- [ ] Batch size 10K-100K rows per INSERT
- [ ] No ALTER TABLE UPDATE for frequent changes
- [ ] ReplacingMergeTree or CollapsingMergeTree for update patterns
- [ ] Async inserts enabled for high-frequency small batches

---

## Output Format

Structure your response as follows:

```
## Rules Checked
- `rule-name-1` - Compliant / Violation found
- `rule-name-2` - Compliant / Violation found
...

## Findings

### Violations
- **`rule-name`**: Description of the issue
  - Current: [what the code does]
  - Required: [what it should do]
  - Fix: [specific correction]

### Compliant
- `rule-name`: Brief note on why it's correct

## Recommendations
[Prioritized list of changes, citing rules]
```

---

## Rule Categories by Priority

| Priority | Category | Impact | Prefix | Rule Count |
|----------|----------|--------|--------|------------|
| 1 | Primary Key Selection | CRITICAL | `schema-pk-` | 4 |
| 2 | Data Type Selection | CRITICAL | `schema-types-` | 5 |
| 3 | JOIN Optimization | CRITICAL | `query-join-` | 5 |
| 4 | Insert Batching | CRITICAL | `insert-batch-` | 1 |
| 5 | Mutation Avoidance | CRITICAL | `insert-mutation-` | 2 |
| 6 | Partitioning Strategy | HIGH | `schema-partition-` | 4 |
| 7 | Skipping Indices | HIGH | `query-index-` | 1 |
| 8 | Materialized Views | HIGH | `query-mv-` | 2 |
| 9 | Async Inserts | HIGH | `insert-async-` | 2 |
| 10 | OPTIMIZE Avoidance | HIGH | `insert-optimize-` | 1 |
| 11 | JSON Usage | MEDIUM | `schema-json-` | 1 |

---

## Quick Reference

### Schema Design - Primary Key (CRITICAL)

- `schema-pk-plan-before-creation` - Plan ORDER BY before table creation (immutable)
- `schema-pk-cardinality-order` - Order columns low-to-high cardinality
- `schema-pk-prioritize-filters` - Include frequently filtered columns
- `schema-pk-filter-on-orderby` - Query filters must use ORDER BY prefix

### Schema Design - Data Types (CRITICAL)

- `schema-types-native-types` - Use native types, not String for everything
- `schema-types-minimize-bitwidth` - Use smallest numeric type that fits
- `schema-types-lowcardinality` - LowCardinality for <10K unique strings
- `schema-types-enum` - Enum for finite value sets with validation
- `schema-types-avoid-nullable` - Avoid Nullable; use DEFAULT instead

### Schema Design - Partitioning (HIGH)

- `schema-partition-low-cardinality` - Keep partition count 100-1,000
- `schema-partition-lifecycle` - Use partitioning for data lifecycle, not queries
- `schema-partition-query-tradeoffs` - Understand partition pruning trade-offs
- `schema-partition-start-without` - Consider starting without partitioning

### Schema Design - JSON (MEDIUM)

- `schema-json-when-to-use` - JSON for dynamic schemas; typed columns for known

### Query Optimization - JOINs (CRITICAL)

- `query-join-choose-algorithm` - Select algorithm based on table sizes
- `query-join-use-any` - ANY JOIN when only one match needed
- `query-join-filter-before` - Filter tables before joining
- `query-join-consider-alternatives` - Dictionaries/denormalization vs JOIN
- `query-join-null-handling` - join_use_nulls=0 for default values

### Query Optimization - Indices (HIGH)

- `query-index-skipping-indices` - Skipping indices for non-ORDER BY filters

### Query Optimization - Materialized Views (HIGH)

- `query-mv-incremental` - Incremental MVs for real-time aggregations
- `query-mv-refreshable` - Refreshable MVs for complex joins

### Insert Strategy - Batching (CRITICAL)

- `insert-batch-size` - Batch 10K-100K rows per INSERT

### Insert Strategy - Async (HIGH)

- `insert-async-small-batches` - Async inserts for high-frequency small batches
- `insert-format-native` - Native format for best performance

### Insert Strategy - Mutations (CRITICAL)

- `insert-mutation-avoid-update` - ReplacingMergeTree instead of ALTER UPDATE
- `insert-mutation-avoid-delete` - Lightweight DELETE or DROP PARTITION

### Insert Strategy - Optimization (HIGH)

- `insert-optimize-avoid-final` - Let background merges work

---

## When to Apply

This skill activates when you encounter:

- `CREATE TABLE` statements
- `ALTER TABLE` modifications
- `ORDER BY` or `PRIMARY KEY` discussions
- Data type selection questions
- Slow query troubleshooting
- JOIN optimization requests
- Data ingestion pipeline design
- Update/delete strategy questions
- ReplacingMergeTree or other specialized engine usage
- Partitioning strategy decisions

---

## Rule File Structure

Each rule file in `rules/` contains:

- **YAML frontmatter**: title, impact level, tags
- **Brief explanation**: Why this rule matters
- **Incorrect example**: Anti-pattern with explanation
- **Correct example**: Best practice with explanation
- **Additional context**: Trade-offs, when to apply, references

---

## Full Compiled Document

For the complete guide with all rules expanded inline: `AGENTS.md`

Use `AGENTS.md` when you need to check multiple rules quickly without reading individual files.
```

## File: `skills/clickhouse-best-practices/metadata.json`
```json
{
  "version": "0.1.0",
  "organization": "ClickHouse Inc",
  "date": "January 2026",
  "clickhouseVersion": "24.1+",
  "abstract": "Comprehensive best practices for ClickHouse database optimization. Covers schema design, query optimization, table engines, indexing strategies, materialized views, distributed operations, and operational best practices. Each rule includes detailed explanations, SQL examples comparing incorrect vs. correct implementations, and specific impact metrics to guide database design and query optimization.",
  "references": [
    "https://clickhouse.com/docs",
    "https://github.com/ClickHouse/ClickHouse"
  ]
}
```

## File: `skills/clickhouse-best-practices/rules/_sections.md`
```markdown
# Sections

This file defines all sections, their ordering, impact levels, and descriptions.
The section ID (in parentheses) is the filename prefix used to group rules.

---

## 1. Schema Design (schema)

**Impact:** CRITICAL

**Description:** Proper schema design is foundational to ClickHouse performance. ORDER BY is immutable after table creation; wrong choices require full data migration. Includes primary key selection, data types, partitioning strategy, and JSON usage. Column types and ordering can impact query speed by orders of magnitude.

## 2. Query Optimization (query)

**Impact:** CRITICAL

**Description:** Query patterns dramatically affect performance. JOIN algorithms, filtering strategies, skipping indices, and materialized views can reduce query time from minutes to milliseconds. Pre-computed aggregations read thousands of rows instead of billions.

## 3. Insert Strategy (insert)

**Impact:** CRITICAL

**Description:** Each INSERT creates a data part. Single-row inserts overwhelm the merge process. Proper batching (10K-100K rows), async inserts for high-frequency writes, mutation avoidance, and letting background merges work are essential for stable cluster performance.
```

## File: `skills/clickhouse-best-practices/rules/_template.md`
```markdown
---
title: Rule Title Here
impact: CRITICAL | HIGH | MEDIUM | LOW
impactDescription: "Quantified improvement (e.g., 10x faster queries)"
tags: [tag1, tag2]
---

## Rule Title Here

**Impact: CRITICAL** (optional description)

Brief explanation of the rule and why it matters. This should be clear and concise, explaining the performance implications.

**Incorrect (description of what's wrong):**

```sql
-- Bad: description
SELECT * FROM table;
```

**Correct (description of what's right):**

```sql
-- Good: description
SELECT * FROM table;
```

Reference: [Official Docs](https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/...)
```

## File: `skills/clickhouse-best-practices/rules/insert-async-small-batches.md`
```markdown
---
title: Use Async Inserts for High-Frequency Small Batches
impact: HIGH
impactDescription: "Server-side buffering when client batching isn't practical"
tags: [insert, async, buffering, small-batches]
---

## Use Async Inserts for High-Frequency Small Batches

**Impact: HIGH**

When client-side batching isn't practical, async inserts buffer server-side and create larger parts automatically.

**Incorrect (small batches without async):**

```python
# Small batches without async_insert - creates too many parts
for batch in chunks(events, 100):
    client.execute("INSERT INTO events VALUES", batch)
```

**Correct (enable async inserts):**

```python
# Enable async_insert with safe defaults
client.execute("SET async_insert = 1")
client.execute("SET wait_for_async_insert = 1")  # Confirms durability

for batch in chunks(events, 100):
    client.execute("INSERT INTO events VALUES", batch)
# Server buffers and creates larger parts automatically
```

```sql
-- Configure server-side for specific users
ALTER USER my_app_user SETTINGS
    async_insert = 1,
    wait_for_async_insert = 1,
    async_insert_max_data_size = 10000000,  -- Flush at 10MB
    async_insert_busy_timeout_ms = 1000;    -- Flush after 1s
```

**Flush conditions (whichever occurs first):**
- Buffer reaches `async_insert_max_data_size`
- Time threshold `async_insert_busy_timeout_ms` elapses
- Maximum insert queries accumulate

**Return modes:**

| Setting | Behavior | Use Case |
|---------|----------|----------|
| `wait_for_async_insert=1` | Waits for flush, confirms durability | **Recommended** |
| `wait_for_async_insert=0` | Fire-and-forget, unaware of errors | **Risky** - only if you accept data loss |

Reference: [Selecting an Insert Strategy](https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/selecting-an-insert-strategy)
```

## File: `skills/clickhouse-best-practices/rules/insert-batch-size.md`
```markdown
---
title: Batch Inserts Appropriately (10K-100K rows)
impact: CRITICAL
impactDescription: "Each INSERT creates a part; single-row inserts overwhelm merge process"
tags: [insert, batching, parts, performance]
---

## Batch Inserts Appropriately (10K-100K rows)

**Impact: CRITICAL**

Each INSERT creates a new data part. Single-row or small-batch inserts create thousands of tiny parts, overwhelming the merge process and causing cluster instability.

**Incorrect (single-row or tiny batches):**

```python
# Single-row inserts - creates 10,000 parts!
for event in events:
    client.execute("INSERT INTO events VALUES", [event])

# Tiny batches - still too many parts
for batch in chunks(events, 100):  # 100 rows per INSERT
    client.execute("INSERT INTO events VALUES", batch)
```

**Correct (proper batch size):**

```python
# Ideal batch size: 10,000-100,000 rows
BATCH_SIZE = 10_000
for batch in chunks(events, BATCH_SIZE):
    client.execute("INSERT INTO events VALUES", batch)
```

**Recommended batch sizes:**

| Threshold | Value |
|-----------|-------|
| Minimum | 1,000 rows |
| Ideal range | 10,000-100,000 rows |
| Insert rate (sync) | ~1 insert per second |

**Validation:**

```sql
-- Monitor part count (>3000 per partition blocks inserts)
SELECT table, count() as parts, sum(rows) as total_rows
FROM system.parts
WHERE active AND database = 'default'
GROUP BY table
ORDER BY parts DESC;
```

Reference: [Selecting an Insert Strategy](https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/selecting-an-insert-strategy)
```

## File: `skills/clickhouse-best-practices/rules/insert-format-native.md`
```markdown
---
title: Use Native Format for Best Insert Performance
impact: MEDIUM
impactDescription: "Native format is most efficient; JSONEachRow is expensive to parse"
tags: [insert, format, Native, performance]
---

## Use Native Format for Best Insert Performance

**Impact: MEDIUM**

Data format affects insert performance. Native format is column-oriented with minimal parsing overhead.

**Performance Ranking (fastest to slowest):**

| Format | Notes |
|--------|-------|
| **Native** | Most efficient. Column-oriented, minimal parsing. Recommended. |
| **RowBinary** | Efficient row-based alternative |
| **JSONEachRow** | Easier to use but expensive to parse |

**Example:**

```python
# Use Native format for best performance
client.execute("INSERT INTO events VALUES", data, settings={'input_format': 'Native'})
```

Reference: [Selecting an Insert Strategy](https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/selecting-an-insert-strategy)
```

## File: `skills/clickhouse-best-practices/rules/insert-mutation-avoid-delete.md`
```markdown
---
title: Avoid ALTER TABLE DELETE
impact: CRITICAL
impactDescription: "Use lightweight DELETE, CollapsingMergeTree, or DROP PARTITION instead"
tags: [insert, mutation, DELETE, CollapsingMergeTree]
---

## Avoid ALTER TABLE DELETE

**Impact: CRITICAL**

`ALTER TABLE DELETE` is a mutation that rewrites entire data parts. Use alternatives like lightweight DELETE, CollapsingMergeTree, or DROP PARTITION.

**Incorrect (mutation delete):**

```sql
-- Mutation delete for cleanup
ALTER TABLE orders DELETE WHERE status = 'cancelled';

-- Time-based cleanup via mutation (very expensive)
ALTER TABLE sessions DELETE WHERE created_at < now() - INTERVAL 7 DAY;
```

**Correct - CollapsingMergeTree:**

```sql
CREATE TABLE orders (
    order_id UInt64,
    customer_id UInt64,
    total Decimal(10,2),
    sign Int8  -- 1 = active, -1 = deleted
)
ENGINE = CollapsingMergeTree(sign)
ORDER BY order_id;

-- Insert order
INSERT INTO orders VALUES (123, 456, 99.99, 1);

-- "Delete" by inserting with sign = -1
INSERT INTO orders VALUES (123, 456, 99.99, -1);

-- Query collapses +1 and -1 pairs
SELECT order_id, sum(total * sign) as total
FROM orders GROUP BY order_id HAVING sum(sign) > 0;
```

**Correct - Lightweight Deletes (23.3+):**

```sql
-- Marks rows, doesn't rewrite immediately
DELETE FROM orders WHERE status = 'cancelled';
-- Physical deletion happens during normal merges
```

**Correct - DROP PARTITION for Bulk Deletion:**

```sql
-- Instant deletion of old data
ALTER TABLE events DROP PARTITION '202301';

-- Much faster than:
ALTER TABLE events DELETE WHERE toYYYYMM(timestamp) = 202301;
```

**Delete strategy comparison:**

| Method | Speed | When to Use |
|--------|-------|-------------|
| ALTER DELETE | Slow | Rare corrections only |
| CollapsingMergeTree | Fast | Frequent soft deletes |
| Lightweight DELETE | Medium | Occasional deletes |
| DROP PARTITION | Instant | Bulk deletion by partition |

Reference: [Avoid Mutations](https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/avoid-mutations)
```

## File: `skills/clickhouse-best-practices/rules/insert-mutation-avoid-update.md`
```markdown
---
title: Avoid ALTER TABLE UPDATE
impact: CRITICAL
impactDescription: "Mutations rewrite entire parts; use ReplacingMergeTree instead"
tags: [insert, mutation, UPDATE, ReplacingMergeTree]
---

## Avoid ALTER TABLE UPDATE

**Impact: CRITICAL**

`ALTER TABLE UPDATE` is a mutation - an asynchronous background process that rewrites entire data parts affected by the change. This is extremely expensive for frequent or large-scale operations.

**Why mutations are problematic:**
- **Write amplification:** Rewrite complete parts even for minor changes
- **Disk I/O spike:** Degrades overall cluster performance
- **No rollback:** Cannot be rolled back after submission
- **Inconsistent reads:** SELECT may read mix of mutated and unmutated parts

**Incorrect (mutation for updates):**

```sql
-- Rewrites potentially huge amounts of data
ALTER TABLE users UPDATE status = 'inactive'
WHERE last_login < now() - INTERVAL 90 DAY;

-- Frequent row updates via mutation
ALTER TABLE inventory UPDATE quantity = quantity - 1
WHERE product_id = 123;
-- If product exists across 100 parts, rewrites ALL 100 parts
```

**Correct (ReplacingMergeTree):**

```sql
-- Table design for updates
CREATE TABLE users (
    user_id UInt64,
    name String,
    status LowCardinality(String),
    updated_at DateTime DEFAULT now()
)
ENGINE = ReplacingMergeTree(updated_at)
ORDER BY user_id;

-- "Update" by inserting new version
INSERT INTO users (user_id, name, status)
VALUES (123, 'John', 'inactive');

-- Query with FINAL to get latest version
SELECT * FROM users FINAL WHERE user_id = 123;

-- Or use aggregation
SELECT user_id, argMax(status, updated_at) as status
FROM users GROUP BY user_id;
```

Reference: [Avoid Mutations](https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/avoid-mutations)
```

## File: `skills/clickhouse-best-practices/rules/insert-optimize-avoid-final.md`
```markdown
---
title: Avoid OPTIMIZE TABLE FINAL
impact: HIGH
impactDescription: "Forces expensive merge of all parts; let background merges work"
tags: [insert, OPTIMIZE, merge, performance]
---

## Avoid OPTIMIZE TABLE FINAL

**Impact: HIGH**

`OPTIMIZE TABLE ... FINAL` forces immediate merge of all parts into one part per partition. This is resource-intensive and rarely necessary. ClickHouse already performs smart background merges.

**Note:** `OPTIMIZE FINAL` is not the same as `FINAL`. The `FINAL` modifier in SELECT queries may be necessary for deduplicated results in ReplacingMergeTree and is generally fine to use.

**Incorrect (OPTIMIZE FINAL after inserts):**

```sql
-- Running OPTIMIZE FINAL after every batch insert
INSERT INTO events SELECT * FROM staging_events;
OPTIMIZE TABLE events FINAL;  -- Expensive and unnecessary!

-- Scheduled OPTIMIZE FINAL jobs
-- Cron: 0 * * * * clickhouse-client -q "OPTIMIZE TABLE events FINAL"
```

**Correct (let background merges work):**

```sql
-- Let background merges handle optimization
INSERT INTO events SELECT * FROM staging_events;
-- Done! ClickHouse merges automatically

-- For ReplacingMergeTree deduplication, use FINAL in queries
SELECT * FROM events FINAL WHERE user_id = 123;
-- Instead of running OPTIMIZE FINAL to deduplicate
```

**Problems with OPTIMIZE FINAL:**
- Rewrites entire partition regardless of need
- Ignores the ~150 GB part size safeguard
- Can cause memory pressure or OOM errors
- Lengthy execution time for large datasets

**When OPTIMIZE FINAL may be acceptable:**
- Finalizing data before table freezing
- Preparing data for export operations
- One-time operations, not regular workflows

**Better alternatives:**

| Need | Alternative |
|------|-------------|
| Deduplicate ReplacingMergeTree | Use `FINAL` modifier in SELECT |
| Reduce part count | Rely on background merges |

Reference: [Avoid OPTIMIZE FINAL](https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/avoid-optimize-final)
```

## File: `skills/clickhouse-best-practices/rules/query-index-skipping-indices.md`
```markdown
---
title: Use Data Skipping Indices for Non-ORDER BY Filters
impact: HIGH
impactDescription: "Up to 60x faster queries by skipping irrelevant granules"
tags: [query, index, skipping, bloom_filter]
---

## Use Data Skipping Indices for Non-ORDER BY Filters

**Impact: HIGH**

Queries filtering on columns not in ORDER BY cannot use the primary index and result in full scans. Data skipping indices store metadata about blocks and skip granules that definitely don't match.

**Important:** Skip indices should be considered **after** optimizing data types, primary key selection, and materialized views.

**When to use:**
- High overall cardinality but low cardinality within blocks
- Rare values critical for search (error codes, specific IDs)
- Column correlates with primary key

**When NOT to use:**
- As a first optimization step
- Matching values scattered across many blocks
- Without testing on real data

**Incorrect (filtering on non-ORDER BY column):**

```sql
CREATE TABLE events (
    event_type LowCardinality(String),
    timestamp DateTime,
    user_id UInt64    -- Not in ORDER BY
)
ENGINE = MergeTree()
ORDER BY (event_type, toDate(timestamp));

-- Query filters on user_id - scans all matching event_type
SELECT * FROM events
WHERE event_type = 'click' AND user_id = 12345;
```

**Correct (add skipping index):**

```sql
CREATE TABLE events (
    event_type LowCardinality(String),
    timestamp DateTime,
    user_id UInt64,
    INDEX idx_user_id user_id TYPE bloom_filter GRANULARITY 4
)
ENGINE = MergeTree()
ORDER BY (event_type, toDate(timestamp));

-- Or add to existing table
ALTER TABLE events ADD INDEX idx_user_id user_id TYPE bloom_filter GRANULARITY 4;
ALTER TABLE events MATERIALIZE INDEX idx_user_id;
```

**Index types:**

| Type | Best For | Example Filter |
|------|----------|----------------|
| `bloom_filter` | Equality on high-cardinality | `WHERE user_id = 123` |
| `set(N)` | Low cardinality (N unique values) | `WHERE status IN ('a','b')` |
| `minmax` | Range queries | `WHERE amount > 1000` |
| `ngrambf_v1` | Text search | `WHERE text LIKE '%term%'` |
| `tokenbf_v1` | Token search | `WHERE hasToken(text, 'word')` |

**Validation:**

```sql
EXPLAIN indexes = 1
SELECT * FROM events WHERE user_id = 12345;
-- Look for "Skip" in output showing granules skipped
```

Reference: [Use Data Skipping Indices Where Appropriate](https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/use-data-skipping-indices-where-appropriate)
```

## File: `skills/clickhouse-best-practices/rules/query-join-choose-algorithm.md`
```markdown
---
title: Choose the Right JOIN Algorithm
impact: CRITICAL
impactDescription: "Wrong algorithm causes OOM; right algorithm handles large tables efficiently"
tags: [query, JOIN, algorithm, memory]
---

## Choose the Right JOIN Algorithm

**Impact: CRITICAL**

ClickHouse's default hash join loads the RIGHT table entirely into memory. Choose the right algorithm based on table sizes and constraints.

**Algorithm selection:**

| Algorithm | Best For | Trade-off |
|-----------|----------|-----------|
| `parallel_hash` | Small-to-medium in-memory tables | Default since 24.11; fast, concurrent |
| `hash` | General purpose, all join types | Single-threaded hash table build |
| `direct` | Dictionary lookups (INNER/LEFT only) | Fastest; no hash table construction |
| `full_sorting_merge` | Tables already sorted on join key | Skips sort if pre-ordered; low memory |
| `partial_merge` | Large tables, memory-constrained | Minimized memory; slower execution |
| `grace_hash` | Large datasets, tunable memory | Flexible; disk-spilling capability |
| `auto` | Adaptive algorithm selection | Tries hash first, falls back on memory pressure |

**Example usage:**

```sql
-- Let ClickHouse choose automatically
SET join_algorithm = 'auto';

-- For large-to-large joins where memory is constrained
SET join_algorithm = 'partial_merge';
SELECT * FROM large_a JOIN large_b ON large_b.id = large_a.id;

-- When joining by primary key columns, sort-merge skips sorting step
SET join_algorithm = 'full_sorting_merge';
SELECT * FROM table_a a JOIN table_b b ON b.pk_col = a.pk_col;
```

**Note:** ClickHouse 24.12+ automatically positions smaller tables on the right side. For earlier versions, manually ensure the smaller table is on the RIGHT.

Reference: [Minimize and Optimize JOINs](https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/minimize-optimize-joins)
```

## File: `skills/clickhouse-best-practices/rules/query-join-consider-alternatives.md`
```markdown
---
title: Consider Alternatives to JOINs
impact: CRITICAL
impactDescription: "Dictionaries and denormalization shift work from query time to insert time"
tags: [query, JOIN, dictionary, denormalization]
---

## Consider Alternatives to JOINs

**Impact: CRITICAL**

Repeated JOINs to dimension tables add overhead. Dictionaries or denormalization shift computational work from query time to insert/pre-processing time.

**Incorrect (JOIN on every query):**

```sql
-- JOIN on every query
SELECT o.order_id, c.name, c.email
FROM orders o
JOIN customers c ON c.id = o.customer_id
WHERE o.created_at > '2024-01-01';
```

**Correct - Dictionary Lookup:**

```sql
-- Create dictionary
CREATE DICTIONARY customer_dict (
    id UInt64,
    name String,
    email String
)
PRIMARY KEY id
SOURCE(CLICKHOUSE(TABLE 'customers'))
LAYOUT(HASHED())
LIFETIME(MIN 300 MAX 360);

-- Use dictGet instead of JOIN (uses direct join algorithm - fastest)
SELECT
    order_id,
    dictGet('customer_dict', 'name', customer_id) as customer_name,
    dictGet('customer_dict', 'email', customer_id) as customer_email
FROM orders
WHERE created_at > '2024-01-01';
```

**Correct - Denormalization:**

```sql
-- Denormalized table with materialized view
CREATE MATERIALIZED VIEW orders_enriched_mv TO orders_enriched AS
SELECT
    o.order_id, o.customer_id,
    c.name as customer_name,
    c.email as customer_email,
    o.total, o.created_at
FROM orders o
JOIN customers c ON c.id = o.customer_id;
```

**Approach comparison:**

| Approach | Use Case | Performance |
|----------|----------|-------------|
| Dictionary | Frequent lookups to small dimension | Fastest (in-memory) |
| Denormalization | Analytics always need enriched data | Fast (no join at query) |
| IN subquery | Existence filtering | Often faster than JOIN |
| JOIN | Infrequent or complex joins | Acceptable |

**Critical dictionary caveat:** Dictionaries silently deduplicate duplicate keys, retaining only the final value. Only use when source has unique keys.

Reference: [Minimize and Optimize JOINs](https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/minimize-optimize-joins)
```

## File: `skills/clickhouse-best-practices/rules/query-join-filter-before.md`
```markdown
---
title: Filter Tables Before Joining
impact: CRITICAL
impactDescription: "Joining full tables then filtering wastes resources"
tags: [query, JOIN, filtering, subquery]
---

## Filter Tables Before Joining

**Impact: CRITICAL**

Joining full tables then filtering wastes resources. Add filtering in `WHERE` or `JOIN ON` clauses. If automatic pushdown fails, restructure as a subquery.

**Incorrect (join then filter):**

```sql
-- Joins entire tables, then filters
SELECT o.order_id, c.name, o.total
FROM orders o
JOIN customers c ON c.id = o.customer_id
WHERE o.created_at > '2024-01-01' AND c.country = 'US';
```

**Correct (filter in subqueries before joining):**

```sql
-- Filter in subqueries before joining
SELECT o.order_id, c.name, o.total
FROM (
    SELECT order_id, customer_id, total
    FROM orders
    WHERE created_at > '2024-01-01'
) o
JOIN (
    SELECT id, name
    FROM customers
    WHERE country = 'US'
) c ON c.id = o.customer_id;
```

**Even better - aggregate before joining:**

```sql
SELECT c.country, o.total_revenue
FROM (
    SELECT customer_id, sum(total) as total_revenue
    FROM orders
    WHERE created_at > '2024-01-01'
    GROUP BY customer_id
) o
JOIN customers c ON c.id = o.customer_id;
```

Reference: [Minimize and Optimize JOINs](https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/minimize-optimize-joins)
```

## File: `skills/clickhouse-best-practices/rules/query-join-null-handling.md`
```markdown
---
title: Optimize NULL Handling in Outer JOINs
impact: MEDIUM
impactDescription: "Default values instead of NULL reduces memory overhead"
tags: [query, JOIN, NULL, memory]
---

## Optimize NULL Handling in Outer JOINs

**Impact: MEDIUM**

Set `join_use_nulls = 0` to use default column values instead of NULL markers, reducing memory overhead compared to Nullable wrappers.

**Example:**

```sql
-- Use default values instead of NULLs for non-matching rows
SET join_use_nulls = 0;

SELECT o.order_id, c.name
FROM orders o
LEFT JOIN customers c ON c.id = o.customer_id;
-- Non-matching rows get '' for name instead of NULL
```

**When to use:**

| Setting | Behavior | Use Case |
|---------|----------|----------|
| `join_use_nulls = 0` | Default values (empty string, 0) for non-matches | When you can handle default values |
| `join_use_nulls = 1` (default) | NULL for non-matches | When you need to distinguish "no match" from "matched with default" |

Reference: [Minimize and Optimize JOINs](https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/minimize-optimize-joins)
```

## File: `skills/clickhouse-best-practices/rules/query-join-use-any.md`
```markdown
---
title: Use ANY JOIN When Only One Match Needed
impact: HIGH
impactDescription: "Returns first match only; less memory and faster execution"
tags: [query, JOIN, ANY, performance]
---

## Use ANY JOIN When Only One Match Needed

**Impact: HIGH**

Use `ANY` JOINs when you only need a single match rather than all matches. They consume less memory and execute faster.

**Incorrect (returns all matches):**

```sql
-- Returns all matching rows, uses more memory
SELECT o.order_id, c.name
FROM orders o
LEFT JOIN customers c ON c.id = o.customer_id;
```

**Correct (returns first match only):**

```sql
-- Returns only first match per row, faster and less memory
SELECT o.order_id, c.name
FROM orders o
LEFT ANY JOIN customers c ON c.id = o.customer_id;
```

**ANY JOIN types:**

| Type | Behavior |
|------|----------|
| `LEFT ANY JOIN` | At most one match from right table |
| `INNER ANY JOIN` | At most one match, only matching rows |
| `RIGHT ANY JOIN` | At most one match from left table |

Reference: [Minimize and Optimize JOINs](https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/minimize-optimize-joins)
```

## File: `skills/clickhouse-best-practices/rules/query-mv-incremental.md`
```markdown
---
title: Use Incremental MVs for Real-Time Aggregations
impact: HIGH
impactDescription: "Read thousands of rows instead of billions; minimal cluster overhead"
tags: [query, materialized-view, aggregation, real-time]
---

## Use Incremental MVs for Real-Time Aggregations

**Impact: HIGH**

Incremental MVs automatically apply the view's query to new data blocks at insert time. Results are written to a target table and partial results merge over time.

**Incorrect (full aggregation on every query):**

```sql
-- Full aggregation on every dashboard load
SELECT
    event_type,
    toStartOfHour(timestamp) as hour,
    count() as events,
    uniq(user_id) as unique_users
FROM events
WHERE timestamp >= now() - INTERVAL 7 DAY
GROUP BY event_type, hour;
-- Scans 7 days of data every time (billions of rows)
```

**Correct (incremental MV with pre-aggregation):**

```sql
-- Create target table for aggregated data
CREATE TABLE events_hourly (
    event_type LowCardinality(String),
    hour DateTime,
    events AggregateFunction(count),
    unique_users AggregateFunction(uniq, UInt64)
)
ENGINE = AggregatingMergeTree()
ORDER BY (event_type, hour);

-- Create materialized view to populate incrementally
CREATE MATERIALIZED VIEW events_hourly_mv TO events_hourly AS
SELECT
    event_type,
    toStartOfHour(timestamp) as hour,
    countState() as events,
    uniqState(user_id) as unique_users
FROM events
GROUP BY event_type, hour;

-- Query the pre-aggregated data
SELECT
    event_type, hour,
    countMerge(events) as events,
    uniqMerge(unique_users) as unique_users
FROM events_hourly
WHERE hour >= now() - INTERVAL 7 DAY
GROUP BY event_type, hour;
-- Reads thousands of rows instead of billions
```

**Key points:**
- Use `-State` functions in MV, `-Merge` functions in query
- Incremental - existing data not automatically included (backfill separately)
- Minimal cluster overhead at insert time

Reference: [Use Materialized Views](https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/use-materialized-views)
```

## File: `skills/clickhouse-best-practices/rules/query-mv-refreshable.md`
```markdown
---
title: Use Refreshable MVs for Complex Joins and Batch Workflows
impact: HIGH
impactDescription: "Sub-millisecond queries with periodic refresh; ideal for complex joins"
tags: [query, materialized-view, refresh, batch]
---

## Use Refreshable MVs for Complex Joins and Batch Workflows

**Impact: HIGH**

Refreshable MVs execute queries periodically on a schedule. The full query re-executes and overwrites (or appends to) the target table.

**Best for:**
- Sub-millisecond latency where minor staleness is acceptable
- Caching "top N" results or lookup tables
- Complex multi-table joins requiring denormalization
- Batch workflows and DAG dependencies

**Incorrect (expensive join on every request):**

```sql
-- Complex join executed on every request
SELECT
    o.order_id, o.total,
    c.name as customer_name,
    p.name as product_name
FROM orders o
JOIN customers c ON o.customer_id = c.id
JOIN products p ON o.product_id = p.id
WHERE o.created_at >= now() - INTERVAL 1 DAY;
```

**Correct (refreshable MV):**

```sql
-- Create refreshable MV that runs every 5 minutes
CREATE MATERIALIZED VIEW orders_denormalized
REFRESH EVERY 5 MINUTE
ENGINE = MergeTree()
ORDER BY (created_at, order_id)
AS SELECT
    o.order_id, o.created_at, o.total,
    c.name as customer_name, c.segment,
    p.name as product_name
FROM orders o
JOIN customers c ON o.customer_id = c.id
JOIN products p ON o.product_id = p.id
WHERE o.created_at >= now() - INTERVAL 1 DAY;

-- Query the pre-joined data (sub-millisecond)
SELECT * FROM orders_denormalized WHERE segment = 'enterprise';
```

**APPEND vs REPLACE modes:**

| Mode | Behavior | Use Case |
|------|----------|----------|
| `REPLACE` (default) | Overwrites previous contents | Current state, lookup tables |
| `APPEND` | Adds new rows to existing data | Periodic snapshots, historical accumulation |

**Critical warning:** Query should run quickly compared to refresh interval. Don't schedule every 10 seconds if the query takes 10+ seconds.

Reference: [Use Materialized Views](https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/use-materialized-views)
```

## File: `skills/clickhouse-best-practices/rules/schema-json-when-to-use.md`
```markdown
---
title: Use JSON Type for Dynamic Schemas
impact: MEDIUM
impactDescription: "Field-level querying for semi-structured data; use typed columns for known schemas"
tags: [schema, JSON, semi-structured, flexibility]
---

## Use JSON Type for Dynamic Schemas

**Impact: MEDIUM**

ClickHouse's JSON type splits JSON objects into separate sub-columns, enabling field-level query optimization. Use it for truly dynamic data, not everything.

**Incorrect (schema bloat or opaque String):**

```sql
-- BAD: Hundreds of nullable columns for event properties
CREATE TABLE events (
    event_id UUID,
    prop_page_url Nullable(String),
    prop_button_id Nullable(String),
    -- ... 100 more nullable columns
)

-- BAD: JSON as String when you need field queries
CREATE TABLE events (
    event_id UUID,
    properties String  -- No field-level optimization
)
```

**Correct (JSON for dynamic, typed for known):**

```sql
-- Use JSON type for dynamic properties
CREATE TABLE events (
    event_id UUID DEFAULT generateUUIDv4(),
    event_type LowCardinality(String),
    timestamp DateTime DEFAULT now(),
    properties JSON  -- Flexible schema with type inference
)
ENGINE = MergeTree()
ORDER BY (event_type, timestamp);

-- Query JSON paths directly
SELECT
    event_type,
    properties.url as page_url,
    properties.amount as purchase_amount
FROM events
WHERE event_type = 'page_view' AND properties.url = '/home';
```

**When to use JSON:**

| Scenario | Use JSON? |
|----------|-----------|
| Data structure varies unpredictably | Yes |
| Field types/schemas change over time | Yes |
| Need field-level querying | Yes |
| Fixed, known schema | No (use typed columns) |
| JSON as opaque blob (no field queries) | No (use String) |

**Optimization: specify types for known paths:**

```sql
CREATE TABLE events (
    properties JSON(
        url String,
        amount Float64,
        product_id UInt64
    )
)
```

Reference: [Use JSON Where Appropriate](https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/use-json-where-appropriate)
```

## File: `skills/clickhouse-best-practices/rules/schema-partition-lifecycle.md`
```markdown
---
title: Use Partitioning for Data Lifecycle Management
impact: HIGH
impactDescription: "DROP PARTITION is instant; DELETE is expensive row-by-row scan"
tags: [schema, partitioning, TTL, data-management]
---

## Use Partitioning for Data Lifecycle Management

**Impact: HIGH**

Partitioning is **primarily a data management technique, not a query optimization tool**. It excels at:
- **Dropping data**: Remove entire partitions as single metadata operations
- **TTL retention**: Implement time-based retention policies efficiently
- **Tiered storage**: Move old partitions to cold storage
- **Archiving**: Move partitions between tables

**Incorrect (no time alignment for lifecycle):**

```sql
-- Cannot efficiently drop old data by time
CREATE TABLE events (...)
ENGINE = MergeTree()
PARTITION BY event_type  -- No time alignment
ORDER BY (timestamp);

-- Slow: must scan and delete row by row
DELETE FROM events WHERE timestamp < '2023-01-01';
```

**Correct (time-based for lifecycle):**

```sql
CREATE TABLE events (
    timestamp DateTime,
    event_type LowCardinality(String)
)
ENGINE = MergeTree()
PARTITION BY toStartOfMonth(timestamp)
ORDER BY (event_type, timestamp)
TTL timestamp + INTERVAL 1 YEAR DELETE;  -- Drops whole partitions

-- Fast: metadata-only operation
ALTER TABLE events DROP PARTITION '202301';

-- Archive to cold storage
ALTER TABLE events_archive ATTACH PARTITION '202301' FROM events;
```

Reference: [Choosing a Partitioning Key](https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/choosing-a-partitioning-key)
```

## File: `skills/clickhouse-best-practices/rules/schema-partition-low-cardinality.md`
```markdown
---
title: Keep Partition Cardinality Low (100-1,000 Values)
impact: HIGH
impactDescription: "Too many partitions cause part explosion and 'too many parts' errors"
tags: [schema, partitioning, parts]
---

## Keep Partition Cardinality Low (100-1,000 Values)

**Impact: HIGH**

Too many distinct partition values create excessive data parts, eventually triggering "too many parts" errors. ClickHouse enforces limits via `max_parts_in_total` and `parts_to_throw_insert` settings.

**Incorrect (high cardinality partitioning):**

```sql
-- High cardinality = too many partitions
CREATE TABLE events (...)
ENGINE = MergeTree()
PARTITION BY user_id  -- Millions of partitions!
ORDER BY (timestamp);

-- Daily partitions can grow unbounded over years
CREATE TABLE logs (...)
ENGINE = MergeTree()
PARTITION BY toDate(timestamp)  -- 3650 partitions over 10 years
ORDER BY (service, timestamp);
```

**Correct (bounded cardinality):**

```sql
-- Monthly partitions = 12 per year, bounded cardinality
CREATE TABLE events (
    timestamp DateTime,
    event_type LowCardinality(String),
    user_id UInt64
)
ENGINE = MergeTree()
PARTITION BY toStartOfMonth(timestamp)
ORDER BY (event_type, timestamp);
```

**Validation:**

```sql
-- Check partition count and health
SELECT
    partition,
    count() as parts,
    sum(rows) as rows,
    formatReadableSize(sum(bytes_on_disk)) as size
FROM system.parts
WHERE table = 'events' AND active
GROUP BY partition
ORDER BY partition;

-- Warning signs: hundreds or thousands of partitions
```

Reference: [Choosing a Partitioning Key](https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/choosing-a-partitioning-key)
```

## File: `skills/clickhouse-best-practices/rules/schema-partition-query-tradeoffs.md`
```markdown
---
title: Understand Partition Query Performance Trade-offs
impact: MEDIUM
impactDescription: "Partition pruning helps some queries; spanning many partitions hurts others"
tags: [schema, partitioning, query, performance]
---

## Understand Partition Query Performance Trade-offs

**Impact: MEDIUM**

Partitioning can help or hurt query performance:
- **Potential improvement**: Queries filtering by partition key may benefit from partition pruning
- **Potential degradation**: Queries spanning many partitions increase total parts scanned

ClickHouse automatically builds **MinMax indexes** on partition columns. Data merges occur **within partitions only**, not across them.

**Incorrect (query scans all partitions):**

```sql
-- Query must scan all partitions
SELECT count(*) FROM events
WHERE event_type = 'click';  -- No partition pruning
```

**Correct (query prunes to single partition):**

```sql
-- Query prunes to single partition
SELECT count(*) FROM events
WHERE timestamp >= '2024-01-01' AND timestamp < '2024-02-01'
  AND event_type = 'click';
```

Reference: [Choosing a Partitioning Key](https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/choosing-a-partitioning-key)
```

## File: `skills/clickhouse-best-practices/rules/schema-partition-start-without.md`
```markdown
---
title: Consider Starting Without Partitioning
impact: MEDIUM
impactDescription: "Add partitioning later when you have clear lifecycle requirements"
tags: [schema, partitioning, simplicity]
---

## Consider Starting Without Partitioning

**Impact: MEDIUM**

Start without partitioning and add it later only if:
- You have clear data lifecycle requirements (retention, archiving)
- Your access patterns clearly benefit from partition pruning
- You understand the cardinality implications

**Example (start simple):**

```sql
-- Start simple, no partitioning
CREATE TABLE events (
    timestamp DateTime,
    event_type LowCardinality(String),
    user_id UInt64
)
ENGINE = MergeTree()
ORDER BY (event_type, timestamp);

-- Add partitioning later if needed for lifecycle management
-- (requires table recreation or materialized view migration)
```

**When to add partitioning:**

| Need | Add Partitioning? |
|------|-------------------|
| Time-based data retention | Yes |
| Archive old data to cold storage | Yes |
| Query performance on time ranges | Maybe (test first) |
| No specific lifecycle needs | No |

Reference: [Choosing a Partitioning Key](https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/choosing-a-partitioning-key)
```

## File: `skills/clickhouse-best-practices/rules/schema-pk-cardinality-order.md`
```markdown
---
title: Order Columns by Cardinality (Low to High)
impact: CRITICAL
impactDescription: "Enables granule skipping; high-cardinality first prevents index pruning"
tags: [schema, primary-key, cardinality, ORDER BY]
---

## Order Columns by Cardinality (Low to High)

**Impact: CRITICAL**

Since the sparse primary index operates on data blocks (granules) rather than individual rows, low-cardinality leading columns create more useful index entries that can skip entire blocks. Place lower-cardinality columns before higher-cardinality ones in the ordering key.

**Incorrect (high cardinality first):**

```sql
-- UUID first means no pruning benefit
CREATE TABLE events (...)
ENGINE = MergeTree()
ORDER BY (event_id, event_type, timestamp);
-- Every granule has different event_id values, index can't skip anything
```

**Correct (low cardinality first):**

```sql
-- Low cardinality first enables pruning
CREATE TABLE events (...)
ENGINE = MergeTree()
ORDER BY (event_type, event_date, event_id);
-- Index can skip entire event_type groups
```

**Column Order Guidelines:**

| Position | Cardinality | Examples |
|----------|-------------|----------|
| 1st | Low (few distinct values) | event_type, status, country |
| 2nd | Date (coarse granularity) | toDate(timestamp) |
| 3rd+ | Medium-High | user_id, session_id |
| Last | High (if needed) | event_id, uuid |

**Tip:** Use `toDate(timestamp)` instead of raw `DateTime` columns when day-level filtering suffices - this reduces index size from 32-bit to 16-bit representations.

Reference: [Choosing a Primary Key](https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/choosing-a-primary-key)
```

## File: `skills/clickhouse-best-practices/rules/schema-pk-filter-on-orderby.md`
```markdown
---
title: Filter on ORDER BY Columns in Queries
impact: CRITICAL
impactDescription: "Skipping prefix columns prevents index usage"
tags: [schema, primary-key, WHERE, query]
---

## Filter on ORDER BY Columns in Queries

**Impact: CRITICAL**

Even with good schema design, queries must use ORDER BY columns to benefit. Skipping prefix columns or filtering on non-ORDER BY columns prevents index usage.

**Incorrect (skips prefix or uses non-ORDER BY columns):**

```sql
-- Given: ORDER BY (tenant_id, event_type, timestamp)

-- Skips prefix columns - can't use index effectively
SELECT * FROM events WHERE event_type = 'click';

-- Filter on column not in ORDER BY - full table scan
SELECT * FROM events WHERE user_agent LIKE '%Chrome%';
```

**Correct (uses ORDER BY prefix):**

```sql
-- Given: ORDER BY (tenant_id, event_type, timestamp)

-- Full prefix match - best performance
SELECT * FROM events
WHERE tenant_id = 123 AND event_type = 'click';

-- Partial prefix - still uses index
SELECT * FROM events WHERE tenant_id = 123;

-- Range on later column after equality on earlier
SELECT * FROM events
WHERE tenant_id = 123 AND event_type = 'click' AND timestamp >= '2024-01-01';
```

**Index usage reference:**

| Filter | Index Used? |
|--------|-------------|
| `WHERE tenant_id = 123` | Full |
| `WHERE tenant_id = 123 AND event_type = 'click'` | Full |
| `WHERE event_type = 'click'` | None (skipped prefix) |
| `WHERE timestamp > '2024-01-01'` | None (skipped both) |

Reference: [Choosing a Primary Key](https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/choosing-a-primary-key)
```

## File: `skills/clickhouse-best-practices/rules/schema-pk-plan-before-creation.md`
```markdown
---
title: Plan PRIMARY KEY Before Table Creation
impact: CRITICAL
impactDescription: "ORDER BY is immutable; wrong choice requires full data migration"
tags: [schema, primary-key, ORDER BY]
---

## Plan PRIMARY KEY Before Table Creation

**Impact: CRITICAL** (immutable after creation)

ClickHouse's ORDER BY clause defines physical data ordering and the sparse index. Unlike other databases, **ORDER BY cannot be modified after table creation**. A wrong choice requires creating a new table and migrating all data.

**Incorrect (arbitrary ORDER BY without query analysis):**

```sql
-- Creating table without analyzing query patterns
CREATE TABLE events (
    event_id UUID,
    user_id UInt64,
    timestamp DateTime
)
ENGINE = MergeTree()
ORDER BY (event_id);  -- Chosen arbitrarily

-- Later: "Most queries filter by user_id!"
-- Cannot fix with: ALTER TABLE events MODIFY ORDER BY (user_id, timestamp)
-- ERROR: Cannot modify ORDER BY
```

**Correct (query-driven ORDER BY selection):**

```sql
-- Step 1: Document query patterns BEFORE creating table
/*
Query Analysis:
- 60% of queries: WHERE user_id = ? AND timestamp BETWEEN ? AND ?
- 25% of queries: WHERE event_type = ? AND timestamp > ?
- 15% of queries: WHERE event_id = ?

Conclusion: user_id and event_type are primary filters
*/

-- Step 2: Create table with correct ORDER BY
CREATE TABLE events (
    event_id UUID DEFAULT generateUUIDv4(),
    user_id UInt64,
    event_type LowCardinality(String),
    timestamp DateTime,
    event_date Date DEFAULT toDate(timestamp)
)
ENGINE = MergeTree()
PARTITION BY toYYYYMM(event_date)
ORDER BY (user_id, event_date, event_id);
```

**Pre-creation checklist:**
- [ ] Listed top 5-10 query patterns
- [ ] Identified columns in WHERE clauses with frequency
- [ ] Prioritized columns that exclude large numbers of rows
- [ ] Ordered columns by cardinality (low first, high last)
- [ ] Limited to 4-5 key columns (typically sufficient)

Reference: [Choosing a Primary Key](https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/choosing-a-primary-key)
```

## File: `skills/clickhouse-best-practices/rules/schema-pk-prioritize-filters.md`
```markdown
---
title: Prioritize Filter Columns in ORDER BY
impact: CRITICAL
impactDescription: "Columns not in ORDER BY cause full table scans"
tags: [schema, primary-key, WHERE, filtering]
---

## Prioritize Filter Columns in ORDER BY

**Impact: CRITICAL**

Prioritize columns frequently used in query filters (WHERE clause), especially those that exclude large numbers of rows. Queries filtering on columns not in ORDER BY result in full table scans.

**Incorrect (ORDER BY doesn't match query patterns):**

```sql
-- If most queries filter by tenant_id:
CREATE TABLE events (...)
ENGINE = MergeTree()
ORDER BY (event_id);  -- Queries by tenant_id will full-scan!
```

**Correct (ORDER BY matches filter patterns):**

```sql
-- ORDER BY matches query filter patterns
CREATE TABLE events (...)
ENGINE = MergeTree()
ORDER BY (tenant_id, event_date, event_id);

-- Query now uses primary index:
SELECT * FROM events WHERE tenant_id = 123 AND event_date >= '2024-01-01';
```

**Validation:**

```sql
-- Verify index usage
EXPLAIN indexes = 1
SELECT * FROM events WHERE tenant_id = 123;
-- Look for "PrimaryKey" with Key Condition
```

Reference: [Choosing a Primary Key](https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/choosing-a-primary-key)
```

## File: `skills/clickhouse-best-practices/rules/schema-types-avoid-nullable.md`
```markdown
---
title: Avoid Nullable Unless Semantically Required
impact: HIGH
impactDescription: "Nullable adds storage overhead; use DEFAULT values instead"
tags: [schema, data-types, Nullable, DEFAULT]
---

## Avoid Nullable Unless Semantically Required

**Impact: HIGH**

Nullable columns maintain a separate UInt8 column for tracking null values, increasing storage and degrading performance. Use DEFAULT values instead when feasible.

**Incorrect (Nullable everywhere):**

```sql
CREATE TABLE users (
    id Nullable(UInt64),              -- IDs should never be null
    name Nullable(String),            -- Empty string is fine
    age Nullable(UInt8),              -- 0 is a valid default
    login_count Nullable(UInt32)      -- 0 is a valid default
)
```

**Correct (DEFAULT values, Nullable only when semantic):**

```sql
CREATE TABLE users (
    id UInt64,                                    -- Never null
    name String DEFAULT '',                       -- Empty = unknown
    age UInt8 DEFAULT 0,                          -- 0 = unknown
    login_count UInt32 DEFAULT 0,                 -- 0 = never logged in
    deleted_at Nullable(DateTime),                -- NULL = not deleted (semantic!)
    parent_id Nullable(UInt64)                    -- NULL = no parent (semantic!)
)
```

**When Nullable IS appropriate:**

| Use Case | Why |
|----------|-----|
| `deleted_at` | NULL = "not deleted", timestamp = "deleted at X" |
| `parent_id` | NULL = "no parent", value = "has parent" |
| `discount_percent` | NULL = "no discount", 0 = "0% discount" |

**Defaults instead of Nullable:**

| Type | Default |
|------|---------|
| String | `''` (empty string) |
| UInt*/Int* | `0` |
| DateTime | `now()` or `toDateTime(0)` |
| UUID | `generateUUIDv4()` |

Reference: [Select Data Types](https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/select-data-types)
```

## File: `skills/clickhouse-best-practices/rules/schema-types-enum.md`
```markdown
---
title: Use Enum for Finite Value Sets
impact: MEDIUM
impactDescription: "Insert-time validation and natural ordering; 1-2 bytes storage"
tags: [schema, data-types, Enum, validation]
---

## Use Enum for Finite Value Sets

**Impact: MEDIUM**

Enum types provide validation at insert time and enable queries that exploit natural ordering. Use Enum8 (up to 256 values) or Enum16 (up to 65,536 values).

**Incorrect (String without validation):**

```sql
CREATE TABLE orders (
    status String    -- No validation, typos like "shiped" allowed
)

-- Ordering requires CASE statements
SELECT * FROM orders ORDER BY
    CASE status
        WHEN 'pending' THEN 1
        WHEN 'processing' THEN 2
        WHEN 'shipped' THEN 3
    END;
```

**Correct (Enum with validation and ordering):**

```sql
CREATE TABLE orders (
    status Enum8('pending' = 1, 'processing' = 2, 'shipped' = 3, 'delivered' = 4)
)

-- Insert validation: invalid values rejected
INSERT INTO orders VALUES ('shiped');  -- ERROR: Unknown element 'shiped'

-- Natural ordering works automatically
SELECT * FROM orders ORDER BY status;  -- Orders by enum value (1, 2, 3, 4)

-- Comparisons use natural order
SELECT * FROM orders WHERE status > 'processing';  -- shipped and delivered
```

**Enum Guidelines:**

| Scenario | Use |
|----------|-----|
| Fixed set of values known at schema time | Enum8/Enum16 |
| Values may change frequently | LowCardinality(String) |
| Need insert-time validation | Enum |
| Need natural ordering in queries | Enum |
| < 256 distinct values | Enum8 (1 byte) |
| 256-65,536 distinct values | Enum16 (2 bytes) |

Reference: [Select Data Types](https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/select-data-types)
```

## File: `skills/clickhouse-best-practices/rules/schema-types-lowcardinality.md`
```markdown
---
title: Use LowCardinality for Repeated Strings
impact: HIGH
impactDescription: "Dictionary encoding for <10K unique values; significant storage reduction"
tags: [schema, data-types, LowCardinality, storage]
---

## Use LowCardinality for Repeated Strings

**Impact: HIGH**

String columns with repeated values store each value repeatedly. LowCardinality uses dictionary encoding for significant storage reduction.

**Incorrect (plain String for repeated values):**

```sql
CREATE TABLE events (
    country String,       -- "United States" stored 500M times
    browser String,       -- "Chrome" stored 300M times
    event_type String     -- "page_view" stored 800M times
)
```

**Correct (LowCardinality for low unique counts):**

```sql
CREATE TABLE events (
    country LowCardinality(String),      -- ~200 unique values
    browser LowCardinality(String),      -- ~50 unique values
    event_type LowCardinality(String)    -- ~100 unique values
)
```

**When to use LowCardinality:**

| Unique Values | Recommendation |
|---------------|----------------|
| < 10,000 | Use LowCardinality |
| > 10,000 | Use regular String |

```sql
-- Check cardinality before deciding
SELECT uniq(column_name) FROM table_name;
```

**LowCardinality vs FixedString:**

Reserve `FixedString` for strictly fixed-length data (e.g., 2-char country codes). For most low-cardinality text, `LowCardinality(String)` outperforms `FixedString`.

```sql
-- FixedString: Only for truly fixed-length data
country_code FixedString(2),    -- "US", "DE", "JP" - always 2 chars

-- LowCardinality: For variable-length low-cardinality strings
country_name LowCardinality(String),  -- "United States", "Germany"
```

Reference: [Select Data Types](https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/select-data-types)
```

## File: `skills/clickhouse-best-practices/rules/schema-types-minimize-bitwidth.md`
```markdown
---
title: Minimize Bit-Width for Numeric Types
impact: HIGH
impactDescription: "Smaller types reduce storage and improve cache efficiency"
tags: [schema, data-types, numeric, storage]
---

## Minimize Bit-Width for Numeric Types

**Impact: HIGH**

Select the smallest numeric type that accommodates your data range. Prefer unsigned types when negative values aren't needed.

**Incorrect (oversized types):**

```sql
CREATE TABLE metrics (
    status_code Int64,        -- HTTP codes are 100-599
    age Int64,                -- Human age fits in UInt8
    year Int64,               -- Years fit in UInt16
    item_count Int64          -- Often small numbers
)
```

**Correct (right-sized types):**

```sql
CREATE TABLE metrics (
    status_code UInt16,       -- 0-65,535 (HTTP codes fit easily)
    age UInt8,                -- 0-255 (sufficient for age)
    year UInt16,              -- 0-65,535 (sufficient for years)
    item_count UInt32         -- 0-4 billion (adjust based on actual max)
)
```

**Numeric Type Reference:**

| Type | Range | Bytes |
|------|-------|-------|
| UInt8 | 0 to 255 | 1 |
| UInt16 | 0 to 65,535 | 2 |
| UInt32 | 0 to 4.3 billion | 4 |
| UInt64 | 0 to 18 quintillion | 8 |
| Int8 | -128 to 127 | 1 |
| Int16 | -32,768 to 32,767 | 2 |
| Int32 | -2.1 billion to 2.1 billion | 4 |
| Int64 | -9 quintillion to 9 quintillion | 8 |

Reference: [Select Data Types](https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/select-data-types)
```

## File: `skills/clickhouse-best-practices/rules/schema-types-native-types.md`
```markdown
---
title: Use Native Types Instead of String
impact: CRITICAL
impactDescription: "2-10x storage reduction; enables compression and correct semantics"
tags: [schema, data-types, storage]
---

## Use Native Types Instead of String

**Impact: CRITICAL**

Using String for all data wastes storage, prevents compression optimization, and makes comparisons slower. ClickHouse's column-oriented architecture benefits directly from optimal type selection.

**Incorrect (String for everything):**

```sql
CREATE TABLE events (
    event_id String,        -- "550e8400-e29b-41d4-a716-446655440000" = 36 bytes
    user_id String,         -- "12345" = 5 bytes (no numeric operations)
    created_at String,      -- "2024-01-15 10:30:00" = 19 bytes
    count String,           -- "42" - can't do math!
    is_active String        -- "true" = 4 bytes
)
```

**Correct (native types):**

```sql
CREATE TABLE events (
    event_id UUID DEFAULT generateUUIDv4(),     -- 16 bytes (vs 36)
    user_id UInt64,                              -- 8 bytes, numeric ops
    created_at DateTime DEFAULT now(),           -- 4 bytes (vs 19)
    count UInt32 DEFAULT 0,                      -- 4 bytes, math works
    is_active Bool DEFAULT true                  -- 1 byte (vs 4)
)
```

**Type Selection Quick Reference:**

| Data | Use | Avoid |
|------|-----|-------|
| Sequential IDs | UInt32/UInt64 | String |
| UUIDs | UUID | String |
| Status/Category | Enum8 or LowCardinality(String) | String |
| Timestamps | DateTime | DateTime64, String |
| Dates only | Date or Date32 | DateTime, String |
| Counts | UInt8/16/32 (smallest that fits) | Int64, String |
| Money | Decimal(P,S) or Int64 (cents) | Float64, String |
| Booleans | Bool or UInt8 | String |

Reference: [Select Data Types](https://clickhouse.com/brain/knowledge/docs_legacy/best-practices/select-data-types)
```

