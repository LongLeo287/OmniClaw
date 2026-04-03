---
id: github.com-millionco-react-doctor-864a120e-knowled
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:27:59.198399
---

# KNOWLEDGE EXTRACT: github.com_millionco_react-doctor_864a120e
> **Extracted on:** 2026-04-01 13:09:53
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007522319/github.com_millionco_react-doctor_864a120e

---

## File: `.gitignore`
```
node_modules
dist
*.log
.DS_Store
.agents
.cursor
```

## File: `.npmrc`
```
shamefully-hoist=true
```

## File: `.oxlintrc.json`
```json
{
  "plugins": ["typescript", "react", "import"],
  "rules": {}
}
```

## File: `AGENTS.md`
```markdown
## General Rules

- MUST: Use @antfu/ni. Use `ni` to install, `nr SCRIPT_NAME` to run. `nun` to uninstall.
- MUST: Use TypeScript interfaces over types.
- MUST: Keep all types in the global scope.
- MUST: Use arrow functions over function declarations
- MUST: Never comment unless absolutely necessary.
  - If the code is a hack (like a setTimeout or potentially confusing code), it must be prefixed with // HACK: reason for hack
- MUST: Use kebab-case for files
- MUST: Use descriptive names for variables (avoid shorthands, or 1-2 character names).
  - Example: for .map(), you can use `innerX` instead of `x`
  - Example: instead of `moved` use `didPositionChange`
- MUST: Frequently re-evaluate and refactor variable names to be more accurate and descriptive.
- MUST: Do not type cast ("as") unless absolutely necessary
- MUST: Remove unused code and don't repeat yourself.
- MUST: Always search the codebase, think of many solutions, then implement the most _elegant_ solution.
- MUST: Put all magic numbers in `constants.ts` using `SCREAMING_SNAKE_CASE` with unit suffixes (`_MS`, `_PX`).
- MUST: Put small, focused utility functions in `utils/` with one utility per file.
- MUST: Use Boolean over !!.

## Testing

Run checks always before committing with:

```bash
pnpm test # runs e2e tests
pnpm lint
pnpm typecheck # runs type checking
pnpm format
```
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2026 Aiden Bai

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
packages/react-doctor/README.md
```

## File: `action.yml`
```yaml
name: "React Doctor"
description: "Scan React codebases for security, performance, and correctness issues"
branding:
  icon: "activity"
  color: "blue"

inputs:
  directory:
    description: "Project directory to scan"
    default: "."
  verbose:
    description: "Show file details per rule"
    default: "true"
  project:
    description: "Workspace project(s) to scan (comma-separated)"
    required: false
  diff:
    description: "Base branch for diff mode (e.g. main). Only files changed vs this branch are scanned."
    required: false
  github-token:
    description: "GitHub token for posting PR comments. When set on pull_request events, findings are posted as a PR comment."
    required: false
  fail-on:
    description: "Exit with error code on diagnostics: error, warning, none"
    default: "error"
  node-version:
    description: "Node.js version to use"
    default: "20"

outputs:
  score:
    description: "Health score (0-100)"
    value: ${{ steps.score.outputs.score }}

runs:
  using: "composite"
  steps:
    - uses: actions/setup-node@v4
      with:
        node-version: ${{ inputs.node-version }}

    - shell: bash
      env:
        INPUT_DIRECTORY: ${{ inputs.directory }}
        INPUT_VERBOSE: ${{ inputs.verbose }}
        INPUT_PROJECT: ${{ inputs.project }}
        INPUT_DIFF: ${{ inputs.diff }}
        INPUT_GITHUB_TOKEN: ${{ inputs.github-token }}
        INPUT_FAIL_ON: ${{ inputs.fail-on }}
      run: |
        FLAGS="--fail-on $INPUT_FAIL_ON"
        if [ "$INPUT_VERBOSE" = "true" ]; then FLAGS="$FLAGS --verbose"; fi
        if [ -n "$INPUT_PROJECT" ]; then FLAGS="$FLAGS --project $INPUT_PROJECT"; fi
        if [ -n "$INPUT_DIFF" ]; then FLAGS="$FLAGS --diff $INPUT_DIFF"; fi

        if [ -n "$INPUT_GITHUB_TOKEN" ]; then
          npx -y react-doctor@latest "$INPUT_DIRECTORY" $FLAGS | tee /tmp/react-doctor-output.txt
        else
          npx -y react-doctor@latest "$INPUT_DIRECTORY" $FLAGS
        fi

    - id: score
      if: always()
      shell: bash
      env:
        INPUT_DIRECTORY: ${{ inputs.directory }}
      run: |
        SCORE=$(npx -y react-doctor@latest "$INPUT_DIRECTORY" --score 2>/dev/null | tail -1 | tr -d '[:space:]')
        if [[ -n "$SCORE" && "$SCORE" =~ ^[0-9]+$ ]]; then
          echo "score=$SCORE" >> "$GITHUB_OUTPUT"
        fi

    - if: ${{ inputs.github-token != '' && github.event_name == 'pull_request' }}
      uses: actions/github-script@v7
      with:
        github-token: ${{ inputs.github-token }}
        script: |
          const fs = require("fs");
          const path = "/tmp/react-doctor-output.txt";
          if (!fs.existsSync(path)) return;
          const output = fs.readFileSync(path, "utf8").trim();
          if (!output) return;

          const marker = "<!-- react-doctor -->";
          const body = `${marker}\n## 🩺 React Doctor\n\n\`\`\`\n${output}\n\`\`\``;

          const { data: comments } = await github.rest.issues.listComments({
            ...context.repo,
            issue_number: context.issue.number,
          });
          const prev = comments.find((c) => c.body?.startsWith(marker));
          if (prev) {
            await github.rest.issues.deleteComment({
              ...context.repo,
              comment_id: prev.id,
            });
          }

          await github.rest.issues.createComment({
            ...context.repo,
            issue_number: context.issue.number,
            body,
          });
```

## File: `package.json`
```json
{
  "name": "react-doctor",
  "private": true,
  "homepage": "https://github.com/aidenybai/react-doctor#readme",
  "bugs": {
    "url": "https://github.com/aidenybai/react-doctor/issues"
  },
  "repository": {
    "type": "git",
    "url": "https://github.com/aidenybai/react-doctor.git"
  },
  "scripts": {
    "dev": "pnpm --filter react-doctor run dev",
    "build": "pnpm --filter react-doctor run build",
    "test": "pnpm --filter react-doctor run test",
    "lint": "oxlint",
    "lint:fix": "oxlint --fix",
    "format": "oxfmt",
    "format:check": "oxfmt --check",
    "changeset": "changeset",
    "version": "changeset version",
    "release": "pnpm build && changeset publish"
  },
  "dependencies": {
    "commander": "^14.0.3",
    "knip": "^5.83.1",
    "picocolors": "^1.1.1"
  },
  "devDependencies": {
    "@changesets/cli": "^2.27.0",
    "eslint-plugin-react-hooks": "^7.0.1",
    "oxfmt": "^0.32.0",
    "oxlint": "^1.47.0",
    "tsdown": "^0.20.3",
    "typescript": "^5.7.0",
    "vitest": "^4.0.18"
  },
  "packageManager": "pnpm@10.29.1"
}
```

## File: `pnpm-workspace.yaml`
```yaml
packages:
  - "packages/*"
```

## File: `tsconfig.json`
```json
{
  "compilerOptions": {
    "strict": true,
    "target": "ESNext",
    "module": "ESNext",
    "moduleResolution": "bundler",
    "declaration": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true
  }
}
```

## File: `packages/react-doctor/CHANGELOG.md`
```markdown
# react-doctor

## 0.0.30

### Patch Changes

- fix issues

## 0.0.29

### Patch Changes

- fix

## 0.0.28

### Patch Changes

- fix

## 0.0.27

### Patch Changes

- cleanip

## 0.0.26

### Patch Changes

- fix

## 0.0.25

### Patch Changes

- fix

## 0.0.24

### Patch Changes

- fix

## 0.0.23

### Patch Changes

- fix issues

## 0.0.22

### Patch Changes

- fix

## 0.0.21

### Patch Changes

- offline flag

## 0.0.20

### Patch Changes

- log err

## 0.0.19

### Patch Changes

- fix issues

## 0.0.18

### Patch Changes

- fix

## 0.0.17

### Patch Changes

- add lopgging

## 0.0.16

### Patch Changes

- fix: log lint errors

## 0.0.15

### Patch Changes

- export node api

## 0.0.14

### Patch Changes

- fix repo

## 0.0.13

### Patch Changes

- fix: skill

## 0.0.12

### Patch Changes

- fix

## 0.0.11

### Patch Changes

- fix: enviroment vars

## 0.0.10

### Patch Changes

- almost ready

## 0.0.9

### Patch Changes

- fix

## 0.0.8

### Patch Changes

- react doctor

## 0.0.7

### Patch Changes

- fix: deeplinking

## 0.0.6

### Patch Changes

- fix: improvements

## 0.0.5

### Patch Changes

- scores

## 0.0.4

### Patch Changes

- fix

## 0.0.3

### Patch Changes

- fix: noisiness

## 0.0.2

### Patch Changes

- init

## 0.0.1

### Patch Changes

- init
```

## File: `packages/react-doctor/README.md`
```markdown
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/react-doctor-readme-logo-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/react-doctor-readme-logo-light.svg">
  <img alt="React Doctor" src="./assets/react-doctor-readme-logo-light.svg" width="180" height="40">
</picture>

[![version](https://img.shields.io/npm/v/react-doctor?style=flat&colorA=000000&colorB=000000)](https://npmjs.com/package/react-doctor)
[![downloads](https://img.shields.io/npm/dt/react-doctor.svg?style=flat&colorA=000000&colorB=000000)](https://npmjs.com/package/react-doctor)

Let coding agents diagnose and fix your React code.

One command scans your codebase for security, performance, correctness, and architecture issues, then outputs a **0–100 score** with actionable diagnostics.

### [See it in action →](https://react.doctor)

https://github.com/user-attachments/assets/07cc88d9-9589-44c3-aa73-5d603cb1c570

## How it works

React Doctor detects your framework (Next.js, Vite, Remix, etc.), React version, and compiler setup, then runs two analysis passes **in parallel**:

1. **Lint**: Checks 60+ rules across state & effects, performance, architecture, bundle size, security, correctness, accessibility, and framework-specific categories (Next.js, React Native). Rules are toggled automatically based on your project setup.
2. **Dead code**: Detects unused files, exports, types, and duplicates.

Diagnostics are filtered through your config, then scored by severity (errors weigh more than warnings) to produce a **0–100 health score** (75+ Great, 50–74 Needs work, <50 Critical).

## Install

Run this at your project root:

```bash
npx -y react-doctor@latest .
```

Use `--verbose` to see affected files and line numbers:

```bash
npx -y react-doctor@latest . --verbose
```

## Install for your coding agent

Teach your coding agent all 47+ React best practice rules:

```bash
curl -fsSL https://react.doctor/install-skill.sh | bash
```

Supports Cursor, Claude Code, Amp Code, Codex, Gemini CLI, OpenCode, Windsurf, and Antigravity.

## GitHub Actions

```yaml
- uses: actions/checkout@v5
  with:
    fetch-depth: 0 # required for --diff
- uses: millionco/react-doctor@main
  with:
    diff: main
    github-token: ${{ secrets.GITHUB_TOKEN }}
```

| Input          | Default | Description                                                       |
| -------------- | ------- | ----------------------------------------------------------------- |
| `directory`    | `.`     | Project directory to scan                                         |
| `verbose`      | `true`  | Show file details per rule                                        |
| `project`      |         | Workspace project(s) to scan (comma-separated)                    |
| `diff`         |         | Base branch for diff mode. Only changed files are scanned         |
| `github-token` |         | When set on `pull_request` events, posts findings as a PR comment |
| `node-version` | `20`    | Node.js version to use                                            |

The action outputs a `score` (0–100) you can use in subsequent steps.

## Options

```
Usage: react-doctor [directory] [options]

Options:
  -v, --version     display the version number
  --no-lint         skip linting
  --no-dead-code    skip dead code detection
  --verbose         show file details per rule
  --score           output only the score
  -y, --yes         skip prompts, scan all workspace projects
  --project <name>  select workspace project (comma-separated for multiple)
  --diff [base]     scan only files changed vs base branch
  --ami             enable Ami-related prompts
  --fix             open Ami to auto-fix all issues
  -h, --help        display help for command
```

## Configuration

Create a `react-doctor.config.json` in your project root to customize behavior:

```json
{
  "ignore": {
    "rules": ["react/no-danger", "jsx-a11y/no-autofocus", "knip/exports"],
    "files": ["src/generated/**"]
  }
}
```

You can also use the `"reactDoctor"` key in your `package.json` instead:

```json
{
  "reactDoctor": {
    "ignore": {
      "rules": ["react/no-danger"]
    }
  }
}
```

If both exist, `react-doctor.config.json` takes precedence.

### Config options

| Key            | Type                | Default | Description                                                                                                                         |
| -------------- | ------------------- | ------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `ignore.rules` | `string[]`          | `[]`    | Rules to suppress, using the `plugin/rule` format shown in diagnostic output (e.g. `react/no-danger`, `knip/exports`, `knip/types`) |
| `ignore.files` | `string[]`          | `[]`    | File paths to exclude, supports glob patterns (`src/generated/**`, `**/*.test.tsx`)                                                 |
| `lint`         | `boolean`           | `true`  | Enable/disable lint checks (same as `--no-lint`)                                                                                    |
| `deadCode`     | `boolean`           | `true`  | Enable/disable dead code detection (same as `--no-dead-code`)                                                                       |
| `verbose`      | `boolean`           | `false` | Show file details per rule (same as `--verbose`)                                                                                    |
| `diff`         | `boolean \| string` | —       | Force diff mode (`true`) or pin a base branch (`"main"`). Set to `false` to disable auto-detection.                                 |

CLI flags always override config values.

## Node.js API

You can also use React Doctor programmatically:

```js
import { diagnose } from "react-doctor/api";

const result = await diagnose("./path/to/your/react-project");

console.log(result.score); // { score: 82, label: "Good" } or null
console.log(result.diagnostics); // Array of Diagnostic objects
console.log(result.project); // Detected framework, React version, etc.
```

The `diagnose` function accepts an optional second argument:

```js
const result = await diagnose(".", {
  lint: true, // run lint checks (default: true)
  deadCode: true, // run dead code detection (default: true)
});
```

Each diagnostic has the following shape:

```ts
interface Diagnostic {
  filePath: string;
  plugin: string;
  rule: string;
  severity: "error" | "warning";
  message: string;
  help: string;
  line: number;
  column: number;
  category: string;
}
```

## [Scores for popular open-source projects](https://react.doctor/leaderboard)

| Project                                                | Score  | Share                                                                                   |
| ------------------------------------------------------ | ------ | --------------------------------------------------------------------------------------- |
| [tldraw](https://github.com/tldraw/tldraw)             | **84** | [view](https://www.react.doctor/share?p=tldraw&s=84&e=98&w=139&f=40)                    |
| [excalidraw](https://github.com/excalidraw/excalidraw) | **84** | [view](https://www.react.doctor/share?p=%40excalidraw%2Fexcalidraw&s=84&e=2&w=196&f=80) |
| [twenty](https://github.com/twentyhq/twenty)           | **78** | [view](https://www.react.doctor/share?p=twenty-front&s=78&e=99&w=293&f=268)             |
| [plane](https://github.com/makeplane/plane)            | **78** | [view](https://www.react.doctor/share?p=web&s=78&e=7&w=525&f=292)                       |
| [formbricks](https://github.com/formbricks/formbricks) | **75** | [view](https://www.react.doctor/share?p=%40formbricks%2Fweb&s=75&e=15&w=389&f=242)      |
| [posthog](https://github.com/PostHog/posthog)          | **72** | [view](https://www.react.doctor/share?p=%40posthog%2Ffrontend&s=72&e=82&w=1177&f=585)   |
| [supabase](https://github.com/supabase/supabase)       | **69** | [view](https://www.react.doctor/share?p=studio&s=69&e=74&w=1087&f=566)                  |
| [onlook](https://github.com/onlook-dev/onlook)         | **69** | [view](https://www.react.doctor/share?p=%40onlook%2Fweb-client&s=69&e=64&w=418&f=178)   |
| [payload](https://github.com/payloadcms/payload)       | **68** | [view](https://www.react.doctor/share?p=%40payloadcms%2Fui&s=68&e=139&w=408&f=298)      |
| [sentry](https://github.com/getsentry/sentry)          | **64** | [view](https://www.react.doctor/share?p=sentry&s=64&e=94&w=1345&f=818)                  |
| [cal.com](https://github.com/calcom/cal.com)           | **63** | [view](https://www.react.doctor/share?p=%40calcom%2Fweb&s=63&e=31&w=558&f=311)          |
| [dub](https://github.com/dubinc/dub)                   | **62** | [view](https://www.react.doctor/share?p=web&s=62&e=52&w=966&f=457)                      |

## Contributing

Want to contribute? Check out the codebase and submit a PR.

```bash
git clone https://github.com/millionco/react-doctor
cd react-doctor
pnpm install
pnpm -r run build
```

Run locally:

```bash
node packages/react-doctor/dist/cli.js /path/to/your/react-project
```

### License

React Doctor is MIT-licensed open-source software.
```

## File: `packages/react-doctor/package.json`
```json
{
  "name": "react-doctor",
  "version": "0.0.30",
  "description": "Diagnose and fix performance issues in your React app",
  "keywords": [
    "diagnostics",
    "linter",
    "nextjs",
    "performance",
    "react"
  ],
  "homepage": "https://github.com/aidenybai/react-doctor#readme",
  "bugs": {
    "url": "https://github.com/aidenybai/react-doctor/issues"
  },
  "license": "MIT",
  "author": "Aiden Bai",
  "repository": {
    "type": "git",
    "url": "https://github.com/aidenybai/react-doctor.git",
    "directory": "packages/react-doctor"
  },
  "bin": {
    "react-doctor": "./dist/cli.js"
  },
  "files": [
    "dist"
  ],
  "type": "module",
  "exports": {
    ".": {
      "types": "./dist/cli.d.ts",
      "default": "./dist/cli.js"
    },
    "./api": {
      "types": "./dist/index.d.ts",
      "default": "./dist/index.js"
    },
    "./oxlint-plugin": {
      "types": "./dist/react-doctor-plugin.d.ts",
      "default": "./dist/react-doctor-plugin.js"
    }
  },
  "scripts": {
    "dev": "tsdown --watch",
    "build": "rm -rf dist && NODE_ENV=production tsdown",
    "typecheck": "tsc --noEmit",
    "test": "pnpm build && vitest run"
  },
  "dependencies": {
    "commander": "^14.0.3",
    "eslint-plugin-react-hooks": "^7.0.1",
    "knip": "^5.83.1",
    "ora": "^9.3.0",
    "oxlint": "^1.47.0",
    "picocolors": "^1.1.1",
    "prompts": "^2.4.2",
    "typescript": ">=5.0.4 <7"
  },
  "devDependencies": {
    "@types/prompts": "^2.4.9",
    "tsdown": "^0.20.3"
  }
}
```

## File: `packages/react-doctor/tsconfig.json`
```json
{
  "extends": "../../tsconfig.json",
  "compilerOptions": {
    "noEmit": true,
    "declarationMap": true
  },
  "include": ["src"]
}
```

## File: `packages/react-doctor/tsdown.config.ts`
```typescript
import fs from "node:fs";
import { defineConfig } from "tsdown";

const packageJson = JSON.parse(fs.readFileSync("package.json", "utf8")) as {
  version: string;
};

export default defineConfig([
  {
    entry: {
      cli: "./src/cli.ts",
    },
    external: ["oxlint", "knip", "knip/session"],
    dts: true,
    target: "node18",
    platform: "node",
    env: {
      VERSION: process.env.VERSION ?? packageJson.version,
    },
    fixedExtension: false,
    banner: "#!/usr/bin/env node",
  },
  {
    entry: {
      index: "./src/index.ts",
    },
    external: ["oxlint", "knip", "knip/session"],
    dts: true,
    target: "node18",
    platform: "node",
    fixedExtension: false,
  },
  {
    entry: {
      "react-doctor-plugin": "./src/plugin/index.ts",
    },
    target: "node18",
    platform: "node",
    fixedExtension: false,
  },
]);
```

## File: `packages/react-doctor/vitest.config.ts`
```typescript
import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    testTimeout: 30_000,
  },
});
```

## File: `packages/react-doctor/src/cli.ts`
```typescript
import { execSync } from "node:child_process";
import { existsSync } from "node:fs";
import os from "node:os";
import path from "node:path";
import { Command } from "commander";
import { AMI_INSTALL_URL, AMI_RELEASES_URL, AMI_WEBSITE_URL, OPEN_BASE_URL } from "./constants.js";
import { scan } from "./scan.js";
import type {
  Diagnostic,
  DiffInfo,
  EstimatedScoreResult,
  FailOnLevel,
  ReactDoctorConfig,
  ScanOptions,
} from "./types.js";
import { fetchEstimatedScore } from "./utils/calculate-score.js";
import { colorizeByScore } from "./utils/colorize-by-score.js";
import { createFramedLine, renderFramedBoxString } from "./utils/framed-box.js";
import { filterSourceFiles, getDiffInfo } from "./utils/get-diff-files.js";
import { handleError } from "./utils/handle-error.js";
import { highlighter } from "./utils/highlighter.js";
import { loadConfig } from "./utils/load-config.js";
import { logger } from "./utils/logger.js";
import { clearSelectBanner, prompts, setSelectBanner } from "./utils/prompts.js";
import { selectProjects } from "./utils/select-projects.js";
import { maybePromptSkillInstall } from "./utils/skill-prompt.js";

const VERSION = process.env.VERSION ?? "0.0.0";

interface CliFlags {
  lint: boolean;
  deadCode: boolean;
  verbose: boolean;
  score: boolean;
  fix: boolean;
  yes: boolean;
  offline: boolean;
  ami: boolean;
  project?: string;
  diff?: boolean | string;
  failOn: string;
}

const VALID_FAIL_ON_LEVELS = new Set<FailOnLevel>(["error", "warning", "none"]);

const isValidFailOnLevel = (level: string): level is FailOnLevel =>
  VALID_FAIL_ON_LEVELS.has(level as FailOnLevel);

const shouldFailForDiagnostics = (diagnostics: Diagnostic[], failOnLevel: FailOnLevel): boolean => {
  if (failOnLevel === "none") return false;
  if (failOnLevel === "warning") return diagnostics.length > 0;
  return diagnostics.some((diagnostic) => diagnostic.severity === "error");
};

const exitWithFixHint = () => {
  logger.break();
  logger.log("Cancelled.");
  logger.dim("Run `npx react-doctor@latest --fix` to fix issues.");
  logger.break();
  process.exit(0);
};

process.on("SIGINT", exitWithFixHint);
process.on("SIGTERM", exitWithFixHint);

const AUTOMATED_ENVIRONMENT_VARIABLES = [
  "CI",
  "CLAUDECODE",
  "CURSOR_AGENT",
  "CODEX_CI",
  "OPENCODE",
  "AMP_HOME",
  "AMI",
];

const isAutomatedEnvironment = (): boolean =>
  AUTOMATED_ENVIRONMENT_VARIABLES.some((envVariable) => Boolean(process.env[envVariable]));

const resolveCliScanOptions = (
  flags: CliFlags,
  userConfig: ReactDoctorConfig | null,
  programInstance: Command,
): ScanOptions => {
  const isCliOverride = (optionName: string) =>
    programInstance.getOptionValueSource(optionName) === "cli";

  return {
    lint: isCliOverride("lint") ? flags.lint : (userConfig?.lint ?? true),
    deadCode: isCliOverride("deadCode") ? flags.deadCode : (userConfig?.deadCode ?? true),
    verbose: isCliOverride("verbose") ? Boolean(flags.verbose) : (userConfig?.verbose ?? false),
    scoreOnly: flags.score,
    offline: flags.offline,
  };
};

const resolveDiffMode = async (
  diffInfo: DiffInfo | null,
  effectiveDiff: boolean | string | undefined,
  shouldSkipPrompts: boolean,
  isScoreOnly: boolean,
): Promise<boolean> => {
  if (effectiveDiff !== undefined && effectiveDiff !== false) {
    if (diffInfo) return true;
    if (!isScoreOnly) {
      logger.warn("No feature branch or uncommitted changes detected. Running full scan.");
      logger.break();
    }
    return false;
  }

  if (effectiveDiff === false || !diffInfo) return false;

  const changedSourceFiles = filterSourceFiles(diffInfo.changedFiles);
  if (changedSourceFiles.length === 0) return false;
  if (shouldSkipPrompts) return true;
  if (isScoreOnly) return false;

  const promptMessage = diffInfo.isCurrentChanges
    ? `Found ${changedSourceFiles.length} uncommitted changed files. Only scan current changes?`
    : `On branch ${diffInfo.currentBranch} (${changedSourceFiles.length} changed files vs ${diffInfo.baseBranch}). Only scan this branch?`;

  const { shouldScanChangedOnly } = await prompts({
    type: "confirm",
    name: "shouldScanChangedOnly",
    message: promptMessage,
    initial: true,
  });
  return Boolean(shouldScanChangedOnly);
};

const program = new Command()
  .name("react-doctor")
  .description("Diagnose React codebase health")
  .version(VERSION, "-v, --version", "display the version number")
  .argument("[directory]", "project directory to scan", ".")
  .option("--lint", "enable linting")
  .option("--no-lint", "skip linting")
  .option("--dead-code", "enable dead code detection")
  .option("--no-dead-code", "skip dead code detection")
  .option("--verbose", "show file details per rule")
  .option("--score", "output only the score")
  .option("-y, --yes", "skip prompts, scan all workspace projects")
  .option("--project <name>", "select workspace project (comma-separated for multiple)")
  .option("--diff [base]", "scan only files changed vs base branch")
  .option("--offline", "skip telemetry (anonymous, not stored, only used to calculate score)")
  .option("--ami", "enable Ami-related prompts")
  .option("--fail-on <level>", "exit with error code on diagnostics: error, warning, none", "none")
  .option("--fix", "open Ami to auto-fix all issues")
  .action(async (directory: string, flags: CliFlags) => {
    const isScoreOnly = flags.score;

    try {
      const resolvedDirectory = path.resolve(directory);
      const userConfig = loadConfig(resolvedDirectory);

      if (!isScoreOnly) {
        logger.log(`react-doctor v${VERSION}`);
        logger.break();
      }

      const scanOptions = resolveCliScanOptions(flags, userConfig, program);
      const shouldSkipPrompts = flags.yes || isAutomatedEnvironment() || !process.stdin.isTTY;
      const shouldSkipAmiPrompts = shouldSkipPrompts || !flags.ami;
      const projectDirectories = await selectProjects(
        resolvedDirectory,
        flags.project,
        shouldSkipPrompts,
      );

      const isDiffCliOverride = program.getOptionValueSource("diff") === "cli";
      const effectiveDiff = isDiffCliOverride ? flags.diff : userConfig?.diff;
      const explicitBaseBranch = typeof effectiveDiff === "string" ? effectiveDiff : undefined;
      const diffInfo = getDiffInfo(resolvedDirectory, explicitBaseBranch);
      const isDiffMode = await resolveDiffMode(
        diffInfo,
        effectiveDiff,
        shouldSkipPrompts,
        isScoreOnly,
      );

      if (isDiffMode && diffInfo && !isScoreOnly) {
        if (diffInfo.isCurrentChanges) {
          logger.log("Scanning uncommitted changes");
        } else {
          logger.log(
            `Scanning changes: ${highlighter.info(diffInfo.currentBranch)} → ${highlighter.info(diffInfo.baseBranch)}`,
          );
        }
        logger.break();
      }

      const allDiagnostics: Diagnostic[] = [];

      for (const projectDirectory of projectDirectories) {
        let includePaths: string[] | undefined;
        if (isDiffMode) {
          const projectDiffInfo = getDiffInfo(projectDirectory, explicitBaseBranch);
          if (projectDiffInfo) {
            const changedSourceFiles = filterSourceFiles(projectDiffInfo.changedFiles);
            if (changedSourceFiles.length === 0) {
              if (!isScoreOnly) {
                logger.dim(`No changed source files in ${projectDirectory}, skipping.`);
                logger.break();
              }
              continue;
            }
            includePaths = changedSourceFiles;
          }
        }

        if (!isScoreOnly) {
          logger.dim(`Scanning ${projectDirectory}...`);
          logger.break();
        }
        const scanResult = await scan(projectDirectory, { ...scanOptions, includePaths });
        allDiagnostics.push(...scanResult.diagnostics);
        if (!isScoreOnly) {
          logger.break();
        }
      }

      const resolvedFailOn =
        program.getOptionValueSource("failOn") === "cli"
          ? flags.failOn
          : (userConfig?.failOn ?? flags.failOn);
      const effectiveFailOn: FailOnLevel = isValidFailOnLevel(resolvedFailOn)
        ? resolvedFailOn
        : "none";

      if (shouldFailForDiagnostics(allDiagnostics, effectiveFailOn)) {
        process.exitCode = 1;
      }

      if (flags.fix) {
        openAmiToFix(resolvedDirectory);
      }

      if (!isScoreOnly && !shouldSkipAmiPrompts && !flags.fix) {
        await maybePromptSkillInstall(shouldSkipAmiPrompts);
        const estimatedScoreResult = flags.offline
          ? null
          : await fetchEstimatedScore(allDiagnostics);
        await maybePromptFix(resolvedDirectory, allDiagnostics, estimatedScoreResult);
      }
    } catch (error) {
      handleError(error);
    }
  })
  .addHelpText(
    "after",
    `
${highlighter.dim("Learn more:")}
  ${highlighter.info("https://github.com/millionco/react-doctor")}
`,
  );

const DEEPLINK_FIX_PROMPT = "/{slash-command:ami:react-doctor}";

const isAmiInstalled = (): boolean => {
  if (process.platform === "darwin") {
    return (
      existsSync("/Applications/Ami.app") ||
      existsSync(path.join(os.homedir(), "Applications", "Ami.app"))
    );
  }

  if (process.platform === "win32") {
    const { LOCALAPPDATA, PROGRAMFILES } = process.env;
    return (
      Boolean(LOCALAPPDATA && existsSync(path.join(LOCALAPPDATA, "Programs", "Ami", "Ami.exe"))) ||
      Boolean(PROGRAMFILES && existsSync(path.join(PROGRAMFILES, "Ami", "Ami.exe")))
    );
  }

  try {
    execSync("which ami", { stdio: "ignore" });
    return true;
  } catch {
    return false;
  }
};

const installAmi = (): void => {
  logger.log("Installing Ami...");
  logger.break();
  try {
    execSync(`curl -fsSL ${AMI_INSTALL_URL} | bash`, { stdio: "inherit" });
  } catch {
    logger.error(`Failed to install Ami. Visit ${AMI_WEBSITE_URL} to install manually.`);
    process.exit(1);
  }
  logger.break();
};

const openUrl = (url: string): void => {
  if (process.platform === "win32") {
    // HACK: cmd.exe interprets %XX% as env var expansion, which mangles encoded URLs.
    // Escaping % as %% produces literal % in cmd output.
    const cmdEscapedUrl = url.replace(/%/g, "%%");
    execSync(`start "" "${cmdEscapedUrl}"`, { stdio: "ignore" });
    return;
  }
  const openCommand = process.platform === "darwin" ? `open "${url}"` : `xdg-open "${url}"`;
  execSync(openCommand, { stdio: "ignore" });
};

const buildDeeplinkParams = (directory: string): URLSearchParams => {
  const params = new URLSearchParams();
  params.set("cwd", path.resolve(directory));
  params.set("prompt", DEEPLINK_FIX_PROMPT);
  params.set("mode", "agent");
  params.set("autoSubmit", "true");
  params.set("source", "react-doctor");
  return params;
};

const buildDeeplink = (directory: string): string =>
  `ami://open-project?${buildDeeplinkParams(directory).toString()}`;

const buildWebDeeplink = (directory: string): string =>
  `${OPEN_BASE_URL}?${buildDeeplinkParams(directory).toString()}`;

const openAmiToFix = (directory: string): void => {
  const isInstalled = isAmiInstalled();
  const deeplink = buildDeeplink(directory);
  const webDeeplink = buildWebDeeplink(directory);

  if (!isInstalled) {
    if (process.platform === "darwin") {
      installAmi();
      if (isAmiInstalled()) {
        logger.success("Ami installed successfully.");
      } else {
        logger.error("Installation could not be verified.");
        logger.dim(`Install manually at ${highlighter.info(AMI_WEBSITE_URL)}`);
      }
    } else {
      logger.error("Ami is not installed.");
      logger.dim(`Download at ${highlighter.info(AMI_RELEASES_URL)}`);
    }
    logger.break();
    logger.dim("Open this link to start fixing:");
    logger.info(webDeeplink);
    return;
  }

  logger.log("Opening Ami...");

  try {
    openUrl(deeplink);
    logger.success("Ami opened. Fixing your issues now.");
  } catch {
    logger.break();
    logger.dim("Could not open Ami automatically. Open this link instead:");
    logger.info(webDeeplink);
  }
};

const FIX_METHOD_AMI = "ami";
const FIX_COMMAND_HINT = "npx react-doctor@latest --fix";

const buildAmiBanner = (
  issueCount: number,
  currentScore: number,
  estimatedScore: number,
): string => {
  const currentScoreDisplay = colorizeByScore(String(currentScore), currentScore);
  const estimatedScoreDisplay = colorizeByScore(`~${estimatedScore}`, estimatedScore);
  const issueLabel = issueCount === 1 ? "issue" : "issues";

  return renderFramedBoxString([
    createFramedLine(
      `Score: ${currentScore} → ~${estimatedScore}`,
      `Score: ${currentScoreDisplay} ${highlighter.dim("→")} ${estimatedScoreDisplay}`,
    ),
    createFramedLine(""),
    createFramedLine(
      `Ami is a coding agent built for React. It reads`,
      `${highlighter.info("Ami")} is a coding agent built for React. It reads`,
    ),
    createFramedLine("your react-doctor report, understands your codebase,"),
    createFramedLine(
      `and fixes ${issueCount} ${issueLabel} one by one — then re-runs the`,
      `and fixes ${highlighter.warn(String(issueCount))} ${issueLabel} one by one — then re-runs the`,
    ),
    createFramedLine("scan to verify the score improved."),
    createFramedLine(""),
    createFramedLine(
      `Free to use. ${AMI_WEBSITE_URL}`,
      `Free to use. ${highlighter.info(AMI_WEBSITE_URL)}`,
    ),
  ]);
};

const buildSkipBanner = (issueCount: number, estimatedScore: number): string => {
  const issueLabel = issueCount === 1 ? "issue" : "issues";
  const estimatedScoreDisplay = colorizeByScore(`~${estimatedScore}`, estimatedScore);

  return renderFramedBoxString([
    createFramedLine(
      `Skip fixing ${issueCount} ${issueLabel} and reaching ~${estimatedScore}?`,
      `Skip fixing ${highlighter.warn(String(issueCount))} ${issueLabel} and reaching ${estimatedScoreDisplay}?`,
    ),
    createFramedLine(""),
    createFramedLine(
      `Run ${FIX_COMMAND_HINT} anytime to come back.`,
      `Run ${highlighter.info(FIX_COMMAND_HINT)} anytime to come back.`,
    ),
  ]);
};

const configureFixBanners = (
  issueCount: number,
  estimatedScoreResult: EstimatedScoreResult,
): void => {
  const { currentScore, estimatedScore } = estimatedScoreResult;
  setSelectBanner(buildAmiBanner(issueCount, currentScore, estimatedScore), 0);
  setSelectBanner(buildSkipBanner(issueCount, estimatedScore), 1);
};

const maybePromptFix = async (
  directory: string,
  diagnostics: Diagnostic[],
  estimatedScoreResult: EstimatedScoreResult | null,
): Promise<void> => {
  if (diagnostics.length === 0) return;

  logger.break();

  if (estimatedScoreResult) {
    configureFixBanners(diagnostics.length, estimatedScoreResult);
  }

  const { fixMethod } = await prompts({
    type: "select",
    name: "fixMethod",
    message: "Fix issues?",
    choices: [
      {
        title: "Use Ami (recommended)",
        description: "Optimized coding agent for React Doctor",
        value: FIX_METHOD_AMI,
      },
      { title: "Skip", value: "skip" },
    ],
  });

  clearSelectBanner();

  if (fixMethod === FIX_METHOD_AMI) {
    openAmiToFix(directory);
  } else {
    logger.break();
    logger.dim(`  Run ${highlighter.info(FIX_COMMAND_HINT)} anytime to fix issues.`);
  }
};

const fixAction = (directory: string) => {
  try {
    openAmiToFix(directory);
  } catch (error) {
    handleError(error);
  }
};

const fixCommand = new Command("fix")
  .description("Open Ami to auto-fix react-doctor issues")
  .argument("[directory]", "project directory", ".")
  .action(fixAction);

const installAmiCommand = new Command("install-ami")
  .description("Install Ami and open it to auto-fix issues")
  .argument("[directory]", "project directory", ".")
  .action(fixAction);

program.addCommand(fixCommand);
program.addCommand(installAmiCommand);

const main = async () => {
  await program.parseAsync();
};

main();
```

## File: `packages/react-doctor/src/constants.ts`
```typescript
export const SOURCE_FILE_PATTERN = /\.(tsx?|jsx?)$/;

export const JSX_FILE_PATTERN = /\.(tsx|jsx)$/;

export const MILLISECONDS_PER_SECOND = 1000;

export const ERROR_PREVIEW_LENGTH_CHARS = 200;

export const PERFECT_SCORE = 100;

export const SCORE_GOOD_THRESHOLD = 75;

export const SCORE_OK_THRESHOLD = 50;

export const SCORE_BAR_WIDTH_CHARS = 50;

export const SUMMARY_BOX_HORIZONTAL_PADDING_CHARS = 1;

export const SUMMARY_BOX_OUTER_INDENT_CHARS = 2;

export const SCORE_API_URL = "https://www.react.doctor/api/score";

export const ESTIMATE_SCORE_API_URL = "https://www.react.doctor/api/estimate-score";

export const SHARE_BASE_URL = "https://www.react.doctor/share";

export const OPEN_BASE_URL = "https://www.react.doctor/open";

export const FETCH_TIMEOUT_MS = 10_000;

export const GIT_LS_FILES_MAX_BUFFER_BYTES = 50 * 1024 * 1024;

// HACK: Windows CreateProcessW limits total command-line length to 32,767 chars.
// Use a conservative threshold to leave room for the executable path and quoting overhead.
export const SPAWN_ARGS_MAX_LENGTH_CHARS = 24_000;

export const OFFLINE_MESSAGE =
  "You are offline, could not calculate score. Reconnect to calculate.";

export const DEFAULT_BRANCH_CANDIDATES = ["main", "master"];

export const ERROR_RULE_PENALTY = 1.5;

export const WARNING_RULE_PENALTY = 0.75;

export const ERROR_ESTIMATED_FIX_RATE = 0.85;

export const WARNING_ESTIMATED_FIX_RATE = 0.8;

export const MAX_KNIP_RETRIES = 5;

export const OXLINT_NODE_REQUIREMENT = "^20.19.0 || >=22.12.0";

export const OXLINT_RECOMMENDED_NODE_MAJOR = 24;

export const IGNORED_DIRECTORIES = new Set(["node_modules", "dist", "build", "coverage"]);

export const AMI_WEBSITE_URL = "https://ami.dev";

export const AMI_INSTALL_URL = `${AMI_WEBSITE_URL}/install.sh`;

export const AMI_RELEASES_URL = "https://github.com/millionco/ami-releases/releases";
```

## File: `packages/react-doctor/src/index.ts`
```typescript
import path from "node:path";
import { performance } from "node:perf_hooks";
import type { Diagnostic, DiffInfo, ProjectInfo, ReactDoctorConfig, ScoreResult } from "./types.js";
import { calculateScore } from "./utils/calculate-score.js";
import { combineDiagnostics, computeJsxIncludePaths } from "./utils/combine-diagnostics.js";
import { discoverProject } from "./utils/discover-project.js";
import { loadConfig } from "./utils/load-config.js";
import { resolveLintIncludePaths } from "./utils/resolve-lint-include-paths.js";
import { runKnip } from "./utils/run-knip.js";
import { runOxlint } from "./utils/run-oxlint.js";

export type { Diagnostic, DiffInfo, ProjectInfo, ReactDoctorConfig, ScoreResult };
export { getDiffInfo, filterSourceFiles } from "./utils/get-diff-files.js";

export interface DiagnoseOptions {
  lint?: boolean;
  deadCode?: boolean;
  includePaths?: string[];
}

export interface DiagnoseResult {
  diagnostics: Diagnostic[];
  score: ScoreResult | null;
  project: ProjectInfo;
  elapsedMilliseconds: number;
}

export const diagnose = async (
  directory: string,
  options: DiagnoseOptions = {},
): Promise<DiagnoseResult> => {
  const { includePaths = [] } = options;
  const isDiffMode = includePaths.length > 0;

  const startTime = performance.now();
  const resolvedDirectory = path.resolve(directory);
  const projectInfo = discoverProject(resolvedDirectory);
  const userConfig = loadConfig(resolvedDirectory);

  const effectiveLint = options.lint ?? userConfig?.lint ?? true;
  const effectiveDeadCode = options.deadCode ?? userConfig?.deadCode ?? true;

  if (!projectInfo.reactVersion) {
    throw new Error("No React dependency found in package.json");
  }

  const jsxIncludePaths = computeJsxIncludePaths(includePaths);
  const lintIncludePaths =
    jsxIncludePaths ?? resolveLintIncludePaths(resolvedDirectory, userConfig);

  const emptyDiagnostics: Diagnostic[] = [];

  const lintPromise = effectiveLint
    ? runOxlint(
        resolvedDirectory,
        projectInfo.hasTypeScript,
        projectInfo.framework,
        projectInfo.hasReactCompiler,
        lintIncludePaths,
      ).catch((error: unknown) => {
        console.error("Lint failed:", error);
        return emptyDiagnostics;
      })
    : Promise.resolve(emptyDiagnostics);

  const deadCodePromise =
    effectiveDeadCode && !isDiffMode
      ? runKnip(resolvedDirectory).catch((error: unknown) => {
          console.error("Dead code analysis failed:", error);
          return emptyDiagnostics;
        })
      : Promise.resolve(emptyDiagnostics);

  const [lintDiagnostics, deadCodeDiagnostics] = await Promise.all([lintPromise, deadCodePromise]);
  const diagnostics = combineDiagnostics(
    lintDiagnostics,
    deadCodeDiagnostics,
    resolvedDirectory,
    isDiffMode,
    userConfig,
  );

  const elapsedMilliseconds = performance.now() - startTime;
  const score = await calculateScore(diagnostics);

  return {
    diagnostics,
    score,
    project: projectInfo,
    elapsedMilliseconds,
  };
};
```

## File: `packages/react-doctor/src/knip.d.ts`
```typescript
declare module "knip" {
  import type { MainOptions } from "knip/session";
  export const main: (
    options: MainOptions,
  ) => Promise<{ issues: unknown; counters: Record<string, number> }>;
}
```

## File: `packages/react-doctor/src/oxlint-config.ts`
```typescript
import { createRequire } from "node:module";
import type { Framework } from "./types.js";

const esmRequire = createRequire(import.meta.url);

const NEXTJS_RULES: Record<string, string> = {
  "react-doctor/nextjs-no-img-element": "warn",
  "react-doctor/nextjs-async-client-component": "error",
  "react-doctor/nextjs-no-a-element": "warn",
  "react-doctor/nextjs-no-use-search-params-without-suspense": "warn",
  "react-doctor/nextjs-no-client-fetch-for-server-data": "warn",
  "react-doctor/nextjs-missing-metadata": "warn",
  "react-doctor/nextjs-no-client-side-redirect": "warn",
  "react-doctor/nextjs-no-redirect-in-try-catch": "warn",
  "react-doctor/nextjs-image-missing-sizes": "warn",
  "react-doctor/nextjs-no-native-script": "warn",
  "react-doctor/nextjs-inline-script-missing-id": "warn",
  "react-doctor/nextjs-no-font-link": "warn",
  "react-doctor/nextjs-no-css-link": "warn",
  "react-doctor/nextjs-no-polyfill-script": "warn",
  "react-doctor/nextjs-no-head-import": "error",
  "react-doctor/nextjs-no-side-effect-in-get-handler": "error",
};

const REACT_NATIVE_RULES: Record<string, string> = {
  "react-doctor/rn-no-raw-text": "error",
  "react-doctor/rn-no-deprecated-modules": "error",
  "react-doctor/rn-no-legacy-expo-packages": "warn",
  "react-doctor/rn-no-dimensions-get": "warn",
  "react-doctor/rn-no-inline-flatlist-renderitem": "warn",
  "react-doctor/rn-no-legacy-shadow-styles": "warn",
  "react-doctor/rn-prefer-reanimated": "warn",
  "react-doctor/rn-no-single-element-style-array": "warn",
};

const REACT_COMPILER_RULES: Record<string, string> = {
  "react-hooks-js/set-state-in-render": "error",
  "react-hooks-js/immutability": "error",
  "react-hooks-js/refs": "error",
  "react-hooks-js/purity": "error",
  "react-hooks-js/hooks": "error",
  "react-hooks-js/set-state-in-effect": "error",
  "react-hooks-js/globals": "error",
  "react-hooks-js/error-boundaries": "error",
  "react-hooks-js/preserve-manual-memoization": "error",
  "react-hooks-js/unsupported-syntax": "error",
  "react-hooks-js/component-hook-factories": "error",
  "react-hooks-js/static-components": "error",
  "react-hooks-js/use-memo": "error",
  "react-hooks-js/void-use-memo": "error",
  "react-hooks-js/incompatible-library": "error",
  "react-hooks-js/todo": "error",
};

interface OxlintConfigOptions {
  pluginPath: string;
  framework: Framework;
  hasReactCompiler: boolean;
}

export const createOxlintConfig = ({
  pluginPath,
  framework,
  hasReactCompiler,
}: OxlintConfigOptions) => ({
  categories: {
    correctness: "off",
    suspicious: "off",
    pedantic: "off",
    perf: "off",
    restriction: "off",
    style: "off",
    nursery: "off",
  },
  plugins: ["react", "jsx-a11y", ...(hasReactCompiler ? [] : ["react-perf"])],
  jsPlugins: [
    ...(hasReactCompiler
      ? [{ name: "react-hooks-js", specifier: esmRequire.resolve("eslint-plugin-react-hooks") }]
      : []),
    pluginPath,
  ],
  rules: {
    "react/rules-of-hooks": "error",
    "react/no-direct-mutation-state": "error",
    "react/jsx-no-duplicate-props": "error",
    "react/jsx-key": "error",
    "react/no-children-prop": "warn",
    "react/no-danger": "warn",
    "react/jsx-no-script-url": "error",
    "react/no-render-return-value": "warn",
    "react/no-string-refs": "warn",
    "react/no-is-mounted": "warn",
    "react/require-render-return": "error",
    "react/no-unknown-property": "warn",

    "jsx-a11y/alt-text": "error",
    "jsx-a11y/anchor-is-valid": "warn",
    "jsx-a11y/click-events-have-key-events": "warn",
    "jsx-a11y/no-static-element-interactions": "warn",
    "jsx-a11y/no-noninteractive-element-interactions": "warn",
    "jsx-a11y/role-has-required-aria-props": "error",
    "jsx-a11y/no-autofocus": "warn",
    "jsx-a11y/heading-has-content": "warn",
    "jsx-a11y/html-has-lang": "warn",
    "jsx-a11y/no-redundant-roles": "warn",
    "jsx-a11y/scope": "warn",
    "jsx-a11y/tabindex-no-positive": "warn",
    "jsx-a11y/label-has-associated-control": "warn",
    "jsx-a11y/no-distracting-elements": "error",
    "jsx-a11y/iframe-has-title": "warn",

    ...(hasReactCompiler ? REACT_COMPILER_RULES : {}),

    "react-doctor/no-derived-state-effect": "error",
    "react-doctor/no-fetch-in-effect": "error",
    "react-doctor/no-cascading-set-state": "warn",
    "react-doctor/no-effect-event-handler": "warn",
    "react-doctor/no-derived-useState": "warn",
    "react-doctor/prefer-useReducer": "warn",
    "react-doctor/rerender-lazy-state-init": "warn",
    "react-doctor/rerender-functional-setstate": "warn",
    "react-doctor/rerender-dependencies": "error",

    "react-doctor/no-giant-component": "warn",
    "react-doctor/no-render-in-render": "warn",
    "react-doctor/no-nested-component-definition": "error",

    "react-doctor/no-usememo-simple-expression": "warn",
    "react-doctor/no-layout-property-animation": "error",
    "react-doctor/rerender-memo-with-default-value": "warn",
    "react-doctor/rendering-animate-svg-wrapper": "warn",
    "react-doctor/no-inline-prop-on-memo-component": "warn",
    "react-doctor/rendering-hydration-no-flicker": "warn",

    "react-doctor/no-transition-all": "warn",
    "react-doctor/no-global-css-variable-animation": "error",
    "react-doctor/no-large-animated-blur": "warn",
    "react-doctor/no-scale-from-zero": "warn",
    "react-doctor/no-permanent-will-change": "warn",

    "react-doctor/no-secrets-in-client-code": "error",

    "react-doctor/no-barrel-import": "warn",
    "react-doctor/no-full-lodash-import": "warn",
    "react-doctor/no-moment": "warn",
    "react-doctor/prefer-dynamic-import": "warn",
    "react-doctor/use-lazy-motion": "warn",
    "react-doctor/no-undeferred-third-party": "warn",

    "react-doctor/no-array-index-as-key": "warn",
    "react-doctor/rendering-conditional-render": "warn",
    "react-doctor/no-prevent-default": "warn",

    "react-doctor/server-auth-actions": "error",
    "react-doctor/server-after-nonblocking": "warn",

    "react-doctor/client-passive-event-listeners": "warn",

    "react-doctor/async-parallel": "warn",
    ...(framework === "nextjs" ? NEXTJS_RULES : {}),
    ...(framework === "expo" || framework === "react-native" ? REACT_NATIVE_RULES : {}),
  },
});
```

## File: `packages/react-doctor/src/scan.ts`
```typescript
import { randomUUID } from "node:crypto";
import { mkdirSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { performance } from "node:perf_hooks";
import {
  MILLISECONDS_PER_SECOND,
  OFFLINE_MESSAGE,
  OXLINT_NODE_REQUIREMENT,
  OXLINT_RECOMMENDED_NODE_MAJOR,
  PERFECT_SCORE,
  SCORE_BAR_WIDTH_CHARS,
  SCORE_GOOD_THRESHOLD,
  SCORE_OK_THRESHOLD,
  SHARE_BASE_URL,
} from "./constants.js";
import type {
  Diagnostic,
  ProjectInfo,
  ReactDoctorConfig,
  ScanOptions,
  ScanResult,
  ScoreResult,
} from "./types.js";
import { calculateScore, calculateScoreLocally } from "./utils/calculate-score.js";
import { colorizeByScore } from "./utils/colorize-by-score.js";
import { combineDiagnostics, computeJsxIncludePaths } from "./utils/combine-diagnostics.js";
import { discoverProject, formatFrameworkName } from "./utils/discover-project.js";
import { type FramedLine, createFramedLine, printFramedBox } from "./utils/framed-box.js";
import { groupBy } from "./utils/group-by.js";
import { highlighter } from "./utils/highlighter.js";
import { indentMultilineText } from "./utils/indent-multiline-text.js";
import { loadConfig } from "./utils/load-config.js";
import { logger } from "./utils/logger.js";
import { prompts } from "./utils/prompts.js";
import {
  installNodeViaNvm,
  isNvmInstalled,
  resolveNodeForOxlint,
} from "./utils/resolve-compatible-node.js";
import { resolveLintIncludePaths } from "./utils/resolve-lint-include-paths.js";
import { runKnip } from "./utils/run-knip.js";
import { runOxlint } from "./utils/run-oxlint.js";
import { spinner } from "./utils/spinner.js";

interface ScoreBarSegments {
  filledSegment: string;
  emptySegment: string;
}

const SEVERITY_ORDER: Record<Diagnostic["severity"], number> = {
  error: 0,
  warning: 1,
};

const colorizeBySeverity = (text: string, severity: Diagnostic["severity"]): string =>
  severity === "error" ? highlighter.error(text) : highlighter.warn(text);

const sortBySeverity = (diagnosticGroups: [string, Diagnostic[]][]): [string, Diagnostic[]][] =>
  diagnosticGroups.toSorted(([, diagnosticsA], [, diagnosticsB]) => {
    const severityA = SEVERITY_ORDER[diagnosticsA[0].severity];
    const severityB = SEVERITY_ORDER[diagnosticsB[0].severity];
    return severityA - severityB;
  });

const collectAffectedFiles = (diagnostics: Diagnostic[]): Set<string> =>
  new Set(diagnostics.map((diagnostic) => diagnostic.filePath));

const buildFileLineMap = (diagnostics: Diagnostic[]): Map<string, number[]> => {
  const fileLines = new Map<string, number[]>();
  for (const diagnostic of diagnostics) {
    const lines = fileLines.get(diagnostic.filePath) ?? [];
    if (diagnostic.line > 0) {
      lines.push(diagnostic.line);
    }
    fileLines.set(diagnostic.filePath, lines);
  }
  return fileLines;
};

const printDiagnostics = (diagnostics: Diagnostic[], isVerbose: boolean): void => {
  const ruleGroups = groupBy(
    diagnostics,
    (diagnostic) => `${diagnostic.plugin}/${diagnostic.rule}`,
  );

  const sortedRuleGroups = sortBySeverity([...ruleGroups.entries()]);

  for (const [, ruleDiagnostics] of sortedRuleGroups) {
    const firstDiagnostic = ruleDiagnostics[0];
    const severitySymbol = firstDiagnostic.severity === "error" ? "✗" : "⚠";
    const icon = colorizeBySeverity(severitySymbol, firstDiagnostic.severity);
    const count = ruleDiagnostics.length;
    const countLabel = count > 1 ? colorizeBySeverity(` (${count})`, firstDiagnostic.severity) : "";

    logger.log(`  ${icon} ${firstDiagnostic.message}${countLabel}`);
    if (firstDiagnostic.help) {
      logger.dim(indentMultilineText(firstDiagnostic.help, "    "));
    }

    if (isVerbose) {
      const fileLines = buildFileLineMap(ruleDiagnostics);

      for (const [filePath, lines] of fileLines) {
        const lineLabel = lines.length > 0 ? `: ${lines.join(", ")}` : "";
        logger.dim(`    ${filePath}${lineLabel}`);
      }
    }

    logger.break();
  }
};

const formatElapsedTime = (elapsedMilliseconds: number): string => {
  if (elapsedMilliseconds < MILLISECONDS_PER_SECOND) {
    return `${Math.round(elapsedMilliseconds)}ms`;
  }
  return `${(elapsedMilliseconds / MILLISECONDS_PER_SECOND).toFixed(1)}s`;
};

const formatRuleSummary = (ruleKey: string, ruleDiagnostics: Diagnostic[]): string => {
  const firstDiagnostic = ruleDiagnostics[0];
  const fileLines = buildFileLineMap(ruleDiagnostics);

  const sections = [
    `Rule: ${ruleKey}`,
    `Severity: ${firstDiagnostic.severity}`,
    `Category: ${firstDiagnostic.category}`,
    `Count: ${ruleDiagnostics.length}`,
    "",
    firstDiagnostic.message,
  ];

  if (firstDiagnostic.help) {
    sections.push("", `Suggestion: ${firstDiagnostic.help}`);
  }

  sections.push("", "Files:");
  for (const [filePath, lines] of fileLines) {
    const lineLabel = lines.length > 0 ? `: ${lines.join(", ")}` : "";
    sections.push(`  ${filePath}${lineLabel}`);
  }

  return sections.join("\n") + "\n";
};

const writeDiagnosticsDirectory = (diagnostics: Diagnostic[]): string => {
  const outputDirectory = join(tmpdir(), `react-doctor-${randomUUID()}`);
  mkdirSync(outputDirectory);

  const ruleGroups = groupBy(
    diagnostics,
    (diagnostic) => `${diagnostic.plugin}/${diagnostic.rule}`,
  );
  const sortedRuleGroups = sortBySeverity([...ruleGroups.entries()]);

  for (const [ruleKey, ruleDiagnostics] of sortedRuleGroups) {
    const fileName = ruleKey.replace(/\//g, "--") + ".txt";
    writeFileSync(join(outputDirectory, fileName), formatRuleSummary(ruleKey, ruleDiagnostics));
  }

  writeFileSync(join(outputDirectory, "diagnostics.json"), JSON.stringify(diagnostics, null, 2));

  return outputDirectory;
};

const buildScoreBarSegments = (score: number): ScoreBarSegments => {
  const filledCount = Math.round((score / PERFECT_SCORE) * SCORE_BAR_WIDTH_CHARS);
  const emptyCount = SCORE_BAR_WIDTH_CHARS - filledCount;

  return {
    filledSegment: "█".repeat(filledCount),
    emptySegment: "░".repeat(emptyCount),
  };
};

const buildPlainScoreBar = (score: number): string => {
  const { filledSegment, emptySegment } = buildScoreBarSegments(score);
  return `${filledSegment}${emptySegment}`;
};

const buildScoreBar = (score: number): string => {
  const { filledSegment, emptySegment } = buildScoreBarSegments(score);
  return colorizeByScore(filledSegment, score) + highlighter.dim(emptySegment);
};

const printScoreGauge = (score: number, label: string): void => {
  const scoreDisplay = colorizeByScore(`${score}`, score);
  const labelDisplay = colorizeByScore(label, score);
  logger.log(`  ${scoreDisplay} / ${PERFECT_SCORE}  ${labelDisplay}`);
  logger.break();
  logger.log(`  ${buildScoreBar(score)}`);
  logger.break();
};

const getDoctorFace = (score: number): string[] => {
  if (score >= SCORE_GOOD_THRESHOLD) return ["◠ ◠", " ▽ "];
  if (score >= SCORE_OK_THRESHOLD) return ["• •", " ─ "];
  return ["x x", " ▽ "];
};

const printBranding = (score?: number): void => {
  if (score !== undefined) {
    const [eyes, mouth] = getDoctorFace(score);
    const colorize = (text: string) => colorizeByScore(text, score);
    logger.log(colorize("  ┌─────┐"));
    logger.log(colorize(`  │ ${eyes} │`));
    logger.log(colorize(`  │ ${mouth} │`));
    logger.log(colorize("  └─────┘"));
  }
  logger.log(`  React Doctor ${highlighter.dim("(www.react.doctor)")}`);
  logger.break();
};

const buildShareUrl = (
  diagnostics: Diagnostic[],
  scoreResult: ScoreResult | null,
  projectName: string,
): string => {
  const errorCount = diagnostics.filter((diagnostic) => diagnostic.severity === "error").length;
  const warningCount = diagnostics.filter((diagnostic) => diagnostic.severity === "warning").length;
  const affectedFileCount = collectAffectedFiles(diagnostics).size;

  const params = new URLSearchParams();
  params.set("p", projectName);
  if (scoreResult) params.set("s", String(scoreResult.score));
  if (errorCount > 0) params.set("e", String(errorCount));
  if (warningCount > 0) params.set("w", String(warningCount));
  if (affectedFileCount > 0) params.set("f", String(affectedFileCount));

  return `${SHARE_BASE_URL}?${params.toString()}`;
};

const buildBrandingLines = (
  scoreResult: ScoreResult | null,
  noScoreMessage: string,
): FramedLine[] => {
  const lines: FramedLine[] = [];

  if (scoreResult) {
    const [eyes, mouth] = getDoctorFace(scoreResult.score);
    const scoreColorizer = (text: string): string => colorizeByScore(text, scoreResult.score);

    lines.push(createFramedLine("┌─────┐", scoreColorizer("┌─────┐")));
    lines.push(createFramedLine(`│ ${eyes} │`, scoreColorizer(`│ ${eyes} │`)));
    lines.push(createFramedLine(`│ ${mouth} │`, scoreColorizer(`│ ${mouth} │`)));
    lines.push(createFramedLine("└─────┘", scoreColorizer("└─────┘")));
    lines.push(
      createFramedLine(
        "React Doctor (www.react.doctor)",
        `React Doctor ${highlighter.dim("(www.react.doctor)")}`,
      ),
    );
    lines.push(createFramedLine(""));

    const scoreLinePlainText = `${scoreResult.score} / ${PERFECT_SCORE}  ${scoreResult.label}`;
    const scoreLineRenderedText = `${colorizeByScore(String(scoreResult.score), scoreResult.score)} / ${PERFECT_SCORE}  ${colorizeByScore(scoreResult.label, scoreResult.score)}`;
    lines.push(createFramedLine(scoreLinePlainText, scoreLineRenderedText));
    lines.push(createFramedLine(""));
    lines.push(
      createFramedLine(buildPlainScoreBar(scoreResult.score), buildScoreBar(scoreResult.score)),
    );
    lines.push(createFramedLine(""));
  } else {
    lines.push(
      createFramedLine(
        "React Doctor (www.react.doctor)",
        `React Doctor ${highlighter.dim("(www.react.doctor)")}`,
      ),
    );
    lines.push(createFramedLine(""));
    lines.push(createFramedLine(noScoreMessage, highlighter.dim(noScoreMessage)));
    lines.push(createFramedLine(""));
  }

  return lines;
};

const buildCountsSummaryLine = (
  diagnostics: Diagnostic[],
  totalSourceFileCount: number,
  elapsedMilliseconds: number,
): FramedLine => {
  const errorCount = diagnostics.filter((diagnostic) => diagnostic.severity === "error").length;
  const warningCount = diagnostics.filter((diagnostic) => diagnostic.severity === "warning").length;
  const affectedFileCount = collectAffectedFiles(diagnostics).size;
  const elapsed = formatElapsedTime(elapsedMilliseconds);

  const plainParts: string[] = [];
  const renderedParts: string[] = [];

  if (errorCount > 0) {
    const errorText = `✗ ${errorCount} error${errorCount === 1 ? "" : "s"}`;
    plainParts.push(errorText);
    renderedParts.push(highlighter.error(errorText));
  }
  if (warningCount > 0) {
    const warningText = `⚠ ${warningCount} warning${warningCount === 1 ? "" : "s"}`;
    plainParts.push(warningText);
    renderedParts.push(highlighter.warn(warningText));
  }

  const fileCountText =
    totalSourceFileCount > 0
      ? `across ${affectedFileCount}/${totalSourceFileCount} files`
      : `across ${affectedFileCount} file${affectedFileCount === 1 ? "" : "s"}`;
  const elapsedTimeText = `in ${elapsed}`;

  plainParts.push(fileCountText, elapsedTimeText);
  renderedParts.push(highlighter.dim(fileCountText), highlighter.dim(elapsedTimeText));

  return createFramedLine(plainParts.join("  "), renderedParts.join("  "));
};

const printSummary = (
  diagnostics: Diagnostic[],
  elapsedMilliseconds: number,
  scoreResult: ScoreResult | null,
  projectName: string,
  totalSourceFileCount: number,
  noScoreMessage: string,
  isOffline: boolean,
): void => {
  const summaryFramedLines = [
    ...buildBrandingLines(scoreResult, noScoreMessage),
    buildCountsSummaryLine(diagnostics, totalSourceFileCount, elapsedMilliseconds),
  ];
  printFramedBox(summaryFramedLines);

  try {
    const diagnosticsDirectory = writeDiagnosticsDirectory(diagnostics);
    logger.break();
    logger.dim(`  Full diagnostics written to ${diagnosticsDirectory}`);
  } catch {
    logger.break();
  }

  if (!isOffline) {
    const shareUrl = buildShareUrl(diagnostics, scoreResult, projectName);
    logger.break();
    logger.dim(`  Share your results: ${highlighter.info(shareUrl)}`);
  }
};

const resolveOxlintNode = async (
  isLintEnabled: boolean,
  isScoreOnly: boolean,
): Promise<string | null> => {
  if (!isLintEnabled) return null;

  const nodeResolution = resolveNodeForOxlint();

  if (nodeResolution) {
    if (!nodeResolution.isCurrentNode && !isScoreOnly) {
      logger.warn(
        `Node ${process.version} is unsupported by oxlint. Using Node ${nodeResolution.version} from nvm.`,
      );
      logger.break();
    }
    return nodeResolution.binaryPath;
  }

  if (isScoreOnly) return null;

  logger.warn(
    `Node ${process.version} is not compatible with oxlint (requires ${OXLINT_NODE_REQUIREMENT}). Lint checks will be skipped.`,
  );

  if (isNvmInstalled() && process.stdin.isTTY) {
    const { shouldInstallNode } = await prompts({
      type: "confirm",
      name: "shouldInstallNode",
      message: `Install Node ${OXLINT_RECOMMENDED_NODE_MAJOR} via nvm to enable lint checks?`,
      initial: true,
    });

    if (shouldInstallNode) {
      logger.break();
      const freshResolution = installNodeViaNvm() ? resolveNodeForOxlint() : null;
      if (freshResolution) {
        logger.break();
        logger.success(`Node ${freshResolution.version} installed. Using it for lint checks.`);
        logger.break();
        return freshResolution.binaryPath;
      }
      logger.break();
      logger.warn("Failed to install Node via nvm. Skipping lint checks.");
      logger.break();
      return null;
    }
  } else if (isNvmInstalled()) {
    logger.dim(`  Run: nvm install ${OXLINT_RECOMMENDED_NODE_MAJOR}`);
  } else {
    logger.dim(
      `  Install nvm (https://github.com/nvm-sh/nvm) and run: nvm install ${OXLINT_RECOMMENDED_NODE_MAJOR}`,
    );
  }

  logger.break();
  return null;
};

interface ResolvedScanOptions {
  lint: boolean;
  deadCode: boolean;
  verbose: boolean;
  scoreOnly: boolean;
  offline: boolean;
  includePaths: string[];
}

const mergeScanOptions = (
  inputOptions: ScanOptions,
  userConfig: ReactDoctorConfig | null,
): ResolvedScanOptions => ({
  lint: inputOptions.lint ?? userConfig?.lint ?? true,
  deadCode: inputOptions.deadCode ?? userConfig?.deadCode ?? true,
  verbose: inputOptions.verbose ?? userConfig?.verbose ?? false,
  scoreOnly: inputOptions.scoreOnly ?? false,
  offline: inputOptions.offline ?? false,
  includePaths: inputOptions.includePaths ?? [],
});

const printProjectDetection = (
  projectInfo: ProjectInfo,
  userConfig: ReactDoctorConfig | null,
  isDiffMode: boolean,
  includePaths: string[],
  lintSourceFileCount?: number,
): void => {
  const frameworkLabel = formatFrameworkName(projectInfo.framework);
  const languageLabel = projectInfo.hasTypeScript ? "TypeScript" : "JavaScript";

  const completeStep = (message: string) => {
    spinner(message).start().succeed(message);
  };

  completeStep(`Detecting framework. Found ${highlighter.info(frameworkLabel)}.`);
  completeStep(
    `Detecting React version. Found ${highlighter.info(`React ${projectInfo.reactVersion}`)}.`,
  );
  completeStep(`Detecting language. Found ${highlighter.info(languageLabel)}.`);
  completeStep(
    `Detecting React Compiler. ${projectInfo.hasReactCompiler ? highlighter.info("Found React Compiler.") : "Not found."}`,
  );

  if (isDiffMode) {
    completeStep(`Scanning ${highlighter.info(`${includePaths.length}`)} changed source files.`);
  } else {
    completeStep(
      `Found ${highlighter.info(`${lintSourceFileCount ?? projectInfo.sourceFileCount}`)} source files.`,
    );
  }

  if (userConfig) {
    completeStep(`Loaded ${highlighter.info("react-doctor config")}.`);
  }

  logger.break();
};

export const scan = async (
  directory: string,
  inputOptions: ScanOptions = {},
): Promise<ScanResult> => {
  const startTime = performance.now();
  const projectInfo = discoverProject(directory);
  const userConfig = loadConfig(directory);
  const options = mergeScanOptions(inputOptions, userConfig);
  const { includePaths } = options;
  const isDiffMode = includePaths.length > 0;

  if (!projectInfo.reactVersion) {
    throw new Error("No React dependency found in package.json");
  }

  const jsxIncludePaths = computeJsxIncludePaths(includePaths);
  const lintIncludePaths = jsxIncludePaths ?? resolveLintIncludePaths(directory, userConfig);
  const lintSourceFileCount = lintIncludePaths?.length ?? projectInfo.sourceFileCount;

  if (!options.scoreOnly) {
    printProjectDetection(projectInfo, userConfig, isDiffMode, includePaths, lintSourceFileCount);
  }

  let didLintFail = false;
  let didDeadCodeFail = false;

  const resolvedNodeBinaryPath = await resolveOxlintNode(options.lint, options.scoreOnly);
  if (options.lint && !resolvedNodeBinaryPath) didLintFail = true;

  const lintPromise = resolvedNodeBinaryPath
    ? (async () => {
        const lintSpinner = options.scoreOnly ? null : spinner("Running lint checks...").start();
        try {
          const lintDiagnostics = await runOxlint(
            directory,
            projectInfo.hasTypeScript,
            projectInfo.framework,
            projectInfo.hasReactCompiler,
            lintIncludePaths,
            resolvedNodeBinaryPath,
          );
          lintSpinner?.succeed("Running lint checks.");
          return lintDiagnostics;
        } catch (error) {
          didLintFail = true;
          if (!options.scoreOnly) {
            const errorMessage = error instanceof Error ? error.message : String(error);
            const isNativeBindingError = errorMessage.includes("native binding");

            if (isNativeBindingError) {
              lintSpinner?.fail(
                `Lint checks failed — oxlint native binding not found (Node ${process.version}).`,
              );
              logger.dim(
                `  Upgrade to Node ${OXLINT_NODE_REQUIREMENT} or run: npx -p oxlint@latest react-doctor@latest`,
              );
            } else {
              lintSpinner?.fail("Lint checks failed (non-fatal, skipping).");
              logger.error(errorMessage);
            }
          }
          return [];
        }
      })()
    : Promise.resolve<Diagnostic[]>([]);

  const deadCodePromise =
    options.deadCode && !isDiffMode
      ? (async () => {
          const deadCodeSpinner = options.scoreOnly
            ? null
            : spinner("Detecting dead code...").start();
          try {
            const knipDiagnostics = await runKnip(directory);
            deadCodeSpinner?.succeed("Detecting dead code.");
            return knipDiagnostics;
          } catch (error) {
            didDeadCodeFail = true;
            if (!options.scoreOnly) {
              deadCodeSpinner?.fail("Dead code detection failed (non-fatal, skipping).");
              logger.error(String(error));
            }
            return [];
          }
        })()
      : Promise.resolve<Diagnostic[]>([]);

  const [lintDiagnostics, deadCodeDiagnostics] = await Promise.all([lintPromise, deadCodePromise]);
  const diagnostics = combineDiagnostics(
    lintDiagnostics,
    deadCodeDiagnostics,
    directory,
    isDiffMode,
    userConfig,
  );

  const elapsedMilliseconds = performance.now() - startTime;

  const skippedChecks: string[] = [];
  if (didLintFail) skippedChecks.push("lint");
  if (didDeadCodeFail) skippedChecks.push("dead code");
  const hasSkippedChecks = skippedChecks.length > 0;

  const scoreResult = options.offline
    ? calculateScoreLocally(diagnostics)
    : await calculateScore(diagnostics);
  const noScoreMessage = OFFLINE_MESSAGE;

  if (options.scoreOnly) {
    if (scoreResult) {
      logger.log(`${scoreResult.score}`);
    } else {
      logger.dim(noScoreMessage);
    }
    return { diagnostics, scoreResult, skippedChecks };
  }

  if (diagnostics.length === 0) {
    if (hasSkippedChecks) {
      const skippedLabel = skippedChecks.join(" and ");
      logger.warn(
        `No issues detected, but ${skippedLabel} checks failed — results are incomplete.`,
      );
    } else {
      logger.success("No issues found!");
    }
    logger.break();
    if (hasSkippedChecks) {
      printBranding();
      logger.dim("  Score not shown — some checks could not complete.");
    } else if (scoreResult) {
      printBranding(scoreResult.score);
      printScoreGauge(scoreResult.score, scoreResult.label);
    } else {
      logger.dim(`  ${noScoreMessage}`);
    }
    return { diagnostics, scoreResult, skippedChecks };
  }

  printDiagnostics(diagnostics, options.verbose);

  const displayedSourceFileCount = isDiffMode ? includePaths.length : lintSourceFileCount;

  printSummary(
    diagnostics,
    elapsedMilliseconds,
    scoreResult,
    projectInfo.projectName,
    displayedSourceFileCount,
    noScoreMessage,
    options.offline,
  );

  if (hasSkippedChecks) {
    const skippedLabel = skippedChecks.join(" and ");
    logger.break();
    logger.warn(`  Note: ${skippedLabel} checks failed — score may be incomplete.`);
  }

  return { diagnostics, scoreResult, skippedChecks };
};
```

## File: `packages/react-doctor/src/types.ts`
```typescript
export type FailOnLevel = "error" | "warning" | "none";

export type Framework =
  | "nextjs"
  | "vite"
  | "cra"
  | "remix"
  | "gatsby"
  | "expo"
  | "react-native"
  | "unknown";

export interface ProjectInfo {
  rootDirectory: string;
  projectName: string;
  reactVersion: string | null;
  framework: Framework;
  hasTypeScript: boolean;
  hasReactCompiler: boolean;
  sourceFileCount: number;
}

export interface OxlintSpan {
  offset: number;
  length: number;
  line: number;
  column: number;
}

export interface OxlintLabel {
  label: string;
  span: OxlintSpan;
}

export interface OxlintDiagnostic {
  message: string;
  code: string;
  severity: "warning" | "error";
  causes: string[];
  url: string;
  help: string;
  filename: string;
  labels: OxlintLabel[];
  related: unknown[];
}

export interface OxlintOutput {
  diagnostics: OxlintDiagnostic[];
  number_of_files: number;
  number_of_rules: number;
}

export interface Diagnostic {
  filePath: string;
  plugin: string;
  rule: string;
  severity: "error" | "warning";
  message: string;
  help: string;
  line: number;
  column: number;
  category: string;
  weight?: number;
}

export interface PackageJson {
  name?: string;
  dependencies?: Record<string, string>;
  devDependencies?: Record<string, string>;
  peerDependencies?: Record<string, string>;
  workspaces?: string[] | { packages: string[] };
}

export interface DependencyInfo {
  reactVersion: string | null;
  framework: Framework;
}

export interface KnipIssue {
  filePath: string;
  symbol: string;
  type: string;
}

export interface KnipIssueRecords {
  [workspace: string]: {
    [filePath: string]: KnipIssue;
  };
}

export interface ScoreResult {
  score: number;
  label: string;
}

export interface ScanResult {
  diagnostics: Diagnostic[];
  scoreResult: ScoreResult | null;
  skippedChecks: string[];
}

export interface EstimatedScoreResult {
  currentScore: number;
  currentLabel: string;
  estimatedScore: number;
  estimatedLabel: string;
}

export interface ScanOptions {
  lint?: boolean;
  deadCode?: boolean;
  verbose?: boolean;
  scoreOnly?: boolean;
  offline?: boolean;
  includePaths?: string[];
}

export interface DiffInfo {
  currentBranch: string;
  baseBranch: string;
  changedFiles: string[];
  isCurrentChanges?: boolean;
}

export interface HandleErrorOptions {
  shouldExit: boolean;
}

export interface WorkspacePackage {
  name: string;
  directory: string;
}

export interface PromptMultiselectChoiceState {
  selected?: boolean;
  disabled?: boolean;
}

export interface PromptMultiselectContext {
  maxChoices?: number;
  cursor: number;
  value: PromptMultiselectChoiceState[];
  bell: () => void;
  render: () => void;
}

export interface KnipResults {
  issues: {
    files: Set<string>;
    dependencies: KnipIssueRecords;
    devDependencies: KnipIssueRecords;
    unlisted: KnipIssueRecords;
    exports: KnipIssueRecords;
    types: KnipIssueRecords;
    duplicates: KnipIssueRecords;
  };
  counters: Record<string, number>;
}

export interface CleanedDiagnostic {
  message: string;
  help: string;
}

export interface ReactDoctorIgnoreConfig {
  rules?: string[];
  files?: string[];
}

export interface ReactDoctorConfig {
  ignore?: ReactDoctorIgnoreConfig;
  lint?: boolean;
  deadCode?: boolean;
  verbose?: boolean;
  diff?: boolean | string;
  failOn?: FailOnLevel;
}
```

## File: `packages/react-doctor/src/plugin/constants.ts`
```typescript
export const GIANT_COMPONENT_LINE_THRESHOLD = 300;
export const CASCADING_SET_STATE_THRESHOLD = 3;
export const RELATED_USE_STATE_THRESHOLD = 5;
export const DEEP_NESTING_THRESHOLD = 3;
export const DUPLICATE_STORAGE_READ_THRESHOLD = 2;
export const SEQUENTIAL_AWAIT_THRESHOLD = 3;
export const SECRET_MIN_LENGTH_CHARS = 8;
export const AUTH_CHECK_LOOKAHEAD_STATEMENTS = 3;

export const LAYOUT_PROPERTIES = new Set([
  "width",
  "height",
  "top",
  "left",
  "right",
  "bottom",
  "padding",
  "paddingTop",
  "paddingRight",
  "paddingBottom",
  "paddingLeft",
  "margin",
  "marginTop",
  "marginRight",
  "marginBottom",
  "marginLeft",
  "borderWidth",
  "fontSize",
  "lineHeight",
  "gap",
]);

export const MOTION_ANIMATE_PROPS = new Set([
  "animate",
  "initial",
  "exit",
  "whileHover",
  "whileTap",
  "whileFocus",
  "whileDrag",
  "whileInView",
]);

export const HEAVY_LIBRARIES = new Set([
  "@monaco-editor/react",
  "monaco-editor",
  "recharts",
  "@react-pdf/renderer",
  "react-quill",
  "@codemirror/view",
  "@codemirror/state",
  "chart.js",
  "react-chartjs-2",
  "@toast-ui/editor",
  "draft-js",
]);

export const FETCH_CALLEE_NAMES = new Set(["fetch"]);
export const FETCH_MEMBER_OBJECTS = new Set(["axios", "ky", "got"]);
export const INDEX_PARAMETER_NAMES = new Set(["index", "idx", "i"]);
export const BARREL_INDEX_SUFFIXES = [
  "/index",
  "/index.js",
  "/index.ts",
  "/index.tsx",
  "/index.mjs",
];
export const PASSIVE_EVENT_NAMES = new Set([
  "scroll",
  "wheel",
  "touchstart",
  "touchmove",
  "touchend",
]);

export const LOOP_TYPES = [
  "ForStatement",
  "ForInStatement",
  "ForOfStatement",
  "WhileStatement",
  "DoWhileStatement",
];

export const AUTH_FUNCTION_NAMES = new Set([
  "auth",
  "getSession",
  "getServerSession",
  "getUser",
  "requireAuth",
  "checkAuth",
  "verifyAuth",
  "authenticate",
  "currentUser",
  "getAuth",
  "validateSession",
]);

export const SECRET_PATTERNS = [
  /^sk_live_/,
  /^sk_test_/,
  /^AKIA[0-9A-Z]{16}$/,
  /^ghp_[a-zA-Z0-9]{36}$/,
  /^gho_[a-zA-Z0-9]{36}$/,
  /^github_pat_/,
  /^glpat-/,
  /^xox[bporas]-/,
  /^sk-[a-zA-Z0-9]{32,}$/,
];

export const SECRET_VARIABLE_PATTERN = /(?:api_?key|secret|token|password|credential|auth)/i;

export const SECRET_FALSE_POSITIVE_SUFFIXES = new Set([
  "modal",
  "label",
  "text",
  "title",
  "name",
  "id",
  "key",
  "url",
  "path",
  "route",
  "page",
  "param",
  "field",
  "column",
  "header",
  "placeholder",
  "description",
  "type",
  "icon",
  "class",
  "style",
  "variant",
  "event",
  "action",
  "status",
  "state",
  "mode",
  "flag",
  "option",
  "config",
  "message",
  "error",
  "display",
  "view",
  "component",
  "element",
  "container",
  "wrapper",
  "button",
  "link",
  "input",
  "select",
  "dialog",
  "menu",
  "form",
  "step",
  "index",
  "count",
  "length",
  "role",
  "scope",
  "context",
  "provider",
  "ref",
  "handler",
  "query",
  "schema",
  "constant",
]);

export const LOADING_STATE_PATTERN = /^(?:isLoading|isPending)$/;

export const GENERIC_EVENT_SUFFIXES = new Set(["Click", "Change", "Input", "Blur", "Focus"]);

export const TRIVIAL_INITIALIZER_NAMES = new Set([
  "Boolean",
  "String",
  "Number",
  "Array",
  "Object",
  "parseInt",
  "parseFloat",
]);

export const SETTER_PATTERN = /^set[A-Z]/;
export const RENDER_FUNCTION_PATTERN = /^render[A-Z]/;
export const UPPERCASE_PATTERN = /^[A-Z]/;
export const PAGE_FILE_PATTERN = /\/page\.(tsx?|jsx?)$/;
export const PAGE_OR_LAYOUT_FILE_PATTERN = /\/(page|layout)\.(tsx?|jsx?)$/;

export const INTERNAL_PAGE_PATH_PATTERN =
  /\/(?:(?:\((?:dashboard|admin|settings|account|internal|manage|console|portal|auth|onboarding|app|ee|protected)\))|(?:dashboard|admin|settings|account|internal|manage|console|portal))\//i;

export const TEST_FILE_PATTERN = /\.(?:test|spec|stories)\.[tj]sx?$/;
export const OG_ROUTE_PATTERN = /\/og\b/i;

export const PAGES_DIRECTORY_PATTERN = /\/pages\//;
export const SERVER_ACTION_FILE_PATTERN = /actions?\.(tsx?|jsx?)$/;
export const SERVER_ACTION_DIRECTORY_PATTERN = /\/actions\//;

export const NEXTJS_NAVIGATION_FUNCTIONS = new Set([
  "redirect",
  "permanentRedirect",
  "notFound",
  "forbidden",
  "unauthorized",
]);

export const GOOGLE_FONTS_PATTERN = /fonts\.googleapis\.com/;

export const POLYFILL_SCRIPT_PATTERN = /polyfill\.io|polyfill\.min\.js|cdn\.polyfill/;

export const EXECUTABLE_SCRIPT_TYPES = new Set([
  "text/javascript",
  "application/javascript",
  "module",
]);

export const APP_DIRECTORY_PATTERN = /\/app\//;

export const ROUTE_HANDLER_FILE_PATTERN = /\/route\.(tsx?|jsx?)$/;

export const MUTATION_METHOD_NAMES = new Set([
  "create",
  "insert",
  "insertInto",
  "update",
  "upsert",
  "delete",
  "remove",
  "destroy",
  "set",
  "append",
]);

export const MUTATING_HTTP_METHODS = new Set(["POST", "PUT", "DELETE", "PATCH"]);

export const MUTATING_ROUTE_SEGMENTS = new Set([
  "logout",
  "log-out",
  "signout",
  "sign-out",
  "unsubscribe",
  "delete",
  "remove",
  "revoke",
  "cancel",
  "deactivate",
]);

export const EFFECT_HOOK_NAMES = new Set(["useEffect", "useLayoutEffect"]);
export const HOOKS_WITH_DEPS = new Set(["useEffect", "useLayoutEffect", "useMemo", "useCallback"]);
export const CHAINABLE_ITERATION_METHODS = new Set(["map", "filter", "forEach", "flatMap"]);
export const STORAGE_OBJECTS = new Set(["localStorage", "sessionStorage"]);

export const LARGE_BLUR_THRESHOLD_PX = 10;
export const BLUR_VALUE_PATTERN = /blur\((\d+(?:\.\d+)?)px\)/;
export const ANIMATION_CALLBACK_NAMES = new Set(["requestAnimationFrame", "setInterval"]);
export const MOTION_LIBRARY_PACKAGES = new Set(["framer-motion", "motion"]);

export const RAW_TEXT_PREVIEW_MAX_CHARS = 30;

export const REACT_NATIVE_TEXT_COMPONENTS = new Set(["Text", "TextInput"]);

export const DEPRECATED_RN_MODULE_REPLACEMENTS: Record<string, string> = {
  AsyncStorage: "@react-native-async-storage/async-storage",
  Picker: "@react-native-picker/picker",
  PickerIOS: "@react-native-picker/picker",
  DatePickerIOS: "@react-native-community/datetimepicker",
  DatePickerAndroid: "@react-native-community/datetimepicker",
  ProgressBarAndroid: "a community alternative",
  ProgressViewIOS: "a community alternative",
  SafeAreaView: "react-native-safe-area-context",
  Slider: "@react-native-community/slider",
  ViewPagerAndroid: "react-native-pager-view",
  WebView: "react-native-webview",
  NetInfo: "@react-native-community/netinfo",
  CameraRoll: "@react-native-camera-roll/camera-roll",
  Clipboard: "@react-native-clipboard/clipboard",
  ImageEditor: "@react-native-community/image-editor",
  MaskedViewIOS: "@react-native-masked-view/masked-view",
};

export const LEGACY_EXPO_PACKAGE_REPLACEMENTS: Record<string, string> = {
  "expo-av": "expo-audio for audio and expo-video for video",
  "expo-permissions": "the permissions API in each module (e.g. Camera.requestPermissionsAsync())",
  "@expo/vector-icons":
    "expo-symbols or expo-image (see https://docs.expo.dev/versions/latest/sdk/symbols/)",
};

export const REACT_NATIVE_LIST_COMPONENTS = new Set([
  "FlatList",
  "SectionList",
  "VirtualizedList",
  "FlashList",
]);

export const LEGACY_SHADOW_STYLE_PROPERTIES = new Set([
  "shadowColor",
  "shadowOffset",
  "shadowOpacity",
  "shadowRadius",
  "elevation",
]);
```

## File: `packages/react-doctor/src/plugin/helpers.ts`
```typescript
import {
  FETCH_CALLEE_NAMES,
  FETCH_MEMBER_OBJECTS,
  LOOP_TYPES,
  MUTATING_HTTP_METHODS,
  MUTATION_METHOD_NAMES,
  SETTER_PATTERN,
  UPPERCASE_PATTERN,
} from "./constants.js";
import type { EsTreeNode, RuleVisitors } from "./types.js";

export const walkAst = (node: EsTreeNode, visitor: (child: EsTreeNode) => void): void => {
  if (!node || typeof node !== "object") return;
  visitor(node);
  for (const key of Object.keys(node)) {
    if (key === "parent") continue;
    const child = node[key];
    if (Array.isArray(child)) {
      for (const item of child) {
        if (item && typeof item === "object" && item.type) {
          walkAst(item, visitor);
        }
      }
    } else if (child && typeof child === "object" && child.type) {
      walkAst(child, visitor);
    }
  }
};

export const isSetterIdentifier = (name: string): boolean => SETTER_PATTERN.test(name);

export const isUppercaseName = (name: string): boolean => UPPERCASE_PATTERN.test(name);

export const isMemberProperty = (node: EsTreeNode, propertyName: string): boolean =>
  node.type === "MemberExpression" &&
  node.property?.type === "Identifier" &&
  node.property.name === propertyName;

export const getEffectCallback = (node: EsTreeNode): EsTreeNode | null => {
  if (!node.arguments?.length) return null;
  const callback = node.arguments[0];
  if (callback.type === "ArrowFunctionExpression" || callback.type === "FunctionExpression") {
    return callback;
  }
  return null;
};

export const getCallbackStatements = (callback: EsTreeNode): EsTreeNode[] => {
  if (callback.body?.type === "BlockStatement") {
    return callback.body.body ?? [];
  }
  return callback.body ? [callback.body] : [];
};

export const countSetStateCalls = (node: EsTreeNode): number => {
  let setStateCallCount = 0;
  walkAst(node, (child) => {
    if (
      child.type === "CallExpression" &&
      child.callee?.type === "Identifier" &&
      isSetterIdentifier(child.callee.name)
    ) {
      setStateCallCount++;
    }
  });
  return setStateCallCount;
};

export const isSimpleExpression = (node: EsTreeNode | null): boolean => {
  if (!node) return false;
  switch (node.type) {
    case "Identifier":
    case "Literal":
    case "TemplateLiteral":
      return true;
    case "BinaryExpression":
      return isSimpleExpression(node.left) && isSimpleExpression(node.right);
    case "UnaryExpression":
      return isSimpleExpression(node.argument);
    case "MemberExpression":
      return !node.computed;
    case "ConditionalExpression":
      return (
        isSimpleExpression(node.test) &&
        isSimpleExpression(node.consequent) &&
        isSimpleExpression(node.alternate)
      );
    default:
      return false;
  }
};

export const isComponentDeclaration = (node: EsTreeNode): boolean =>
  node.type === "FunctionDeclaration" && Boolean(node.id?.name) && isUppercaseName(node.id.name);

export const isComponentAssignment = (node: EsTreeNode): boolean =>
  node.type === "VariableDeclarator" &&
  node.id?.type === "Identifier" &&
  isUppercaseName(node.id.name) &&
  Boolean(node.init) &&
  (node.init.type === "ArrowFunctionExpression" || node.init.type === "FunctionExpression");

export const isHookCall = (node: EsTreeNode, hookName: string | Set<string>): boolean =>
  node.type === "CallExpression" &&
  node.callee?.type === "Identifier" &&
  (typeof hookName === "string" ? node.callee.name === hookName : hookName.has(node.callee.name));

export const hasDirective = (programNode: EsTreeNode, directive: string): boolean =>
  Boolean(
    programNode.body?.some(
      (statement: EsTreeNode) =>
        statement.type === "ExpressionStatement" &&
        statement.expression?.type === "Literal" &&
        statement.expression.value === directive,
    ),
  );

export const hasUseServerDirective = (node: EsTreeNode): boolean => {
  if (node.body?.type !== "BlockStatement") return false;
  return Boolean(
    node.body.body?.some(
      (statement: EsTreeNode) =>
        statement.type === "ExpressionStatement" && statement.directive === "use server",
    ),
  );
};

export const containsFetchCall = (node: EsTreeNode): boolean => {
  let didFindFetchCall = false;
  walkAst(node, (child) => {
    if (didFindFetchCall || child.type !== "CallExpression") return;
    if (child.callee?.type === "Identifier" && FETCH_CALLEE_NAMES.has(child.callee.name)) {
      didFindFetchCall = true;
    }
    if (
      child.callee?.type === "MemberExpression" &&
      child.callee.object?.type === "Identifier" &&
      FETCH_MEMBER_OBJECTS.has(child.callee.object.name)
    ) {
      didFindFetchCall = true;
    }
  });
  return didFindFetchCall;
};

export const findJsxAttribute = (
  attributes: EsTreeNode[],
  attributeName: string,
): EsTreeNode | undefined =>
  attributes?.find(
    (attr: EsTreeNode) =>
      attr.type === "JSXAttribute" &&
      attr.name?.type === "JSXIdentifier" &&
      attr.name.name === attributeName,
  );

export const hasJsxAttribute = (attributes: EsTreeNode[], attributeName: string): boolean =>
  Boolean(findJsxAttribute(attributes, attributeName));

export const createLoopAwareVisitors = (
  innerVisitors: Record<string, (node: EsTreeNode) => void>,
): RuleVisitors => {
  let loopDepth = 0;
  const incrementLoopDepth = (): void => {
    loopDepth++;
  };
  const decrementLoopDepth = (): void => {
    loopDepth--;
  };

  const visitors: RuleVisitors = {};

  for (const loopType of LOOP_TYPES) {
    visitors[loopType] = incrementLoopDepth;
    visitors[`${loopType}:exit`] = decrementLoopDepth;
  }

  for (const [nodeType, handler] of Object.entries(innerVisitors)) {
    visitors[nodeType] = (node: EsTreeNode) => {
      if (loopDepth > 0) handler(node);
    };
  }

  return visitors;
};

const isCookiesOrHeadersCall = (node: EsTreeNode, methodName: string): boolean => {
  if (node.type !== "CallExpression" || node.callee?.type !== "MemberExpression") return false;
  const { object, property } = node.callee;
  if (property?.type !== "Identifier" || !MUTATION_METHOD_NAMES.has(property.name)) return false;
  if (object?.type !== "CallExpression" || object.callee?.type !== "Identifier") return false;
  return object.callee.name === methodName;
};

const isMutatingDbCall = (node: EsTreeNode): boolean => {
  if (node.type !== "CallExpression" || node.callee?.type !== "MemberExpression") return false;
  const { property } = node.callee;
  return property?.type === "Identifier" && MUTATION_METHOD_NAMES.has(property.name);
};

const isMutatingFetchCall = (node: EsTreeNode): boolean => {
  if (node.type !== "CallExpression") return false;
  if (node.callee?.type !== "Identifier" || node.callee.name !== "fetch") return false;
  const optionsArgument = node.arguments?.[1];
  if (!optionsArgument || optionsArgument.type !== "ObjectExpression") return false;
  return optionsArgument.properties?.some(
    (property: EsTreeNode) =>
      property.type === "Property" &&
      property.key?.type === "Identifier" &&
      property.key.name === "method" &&
      property.value?.type === "Literal" &&
      typeof property.value.value === "string" &&
      MUTATING_HTTP_METHODS.has(property.value.value.toUpperCase()),
  );
};

export const findSideEffect = (node: EsTreeNode): string | null => {
  let sideEffectDescription: string | null = null;
  walkAst(node, (child: EsTreeNode) => {
    if (sideEffectDescription) return;
    if (isCookiesOrHeadersCall(child, "cookies")) {
      const methodName = child.callee.property.name;
      sideEffectDescription = `cookies().${methodName}()`;
    } else if (isCookiesOrHeadersCall(child, "headers")) {
      const methodName = child.callee.property.name;
      sideEffectDescription = `headers().${methodName}()`;
    } else if (isMutatingFetchCall(child)) {
      const methodProperty = child.arguments[1].properties.find(
        (property: EsTreeNode) =>
          property.key?.type === "Identifier" && property.key.name === "method",
      );
      sideEffectDescription = `fetch() with method ${methodProperty.value.value}`;
    } else if (isMutatingDbCall(child)) {
      const methodName = child.callee.property.name;
      const objectName =
        child.callee.object?.type === "Identifier" ? child.callee.object.name : null;
      sideEffectDescription = objectName ? `${objectName}.${methodName}()` : `.${methodName}()`;
    }
  });
  return sideEffectDescription;
};

export const extractDestructuredPropNames = (params: EsTreeNode[]): Set<string> => {
  const propNames = new Set<string>();
  for (const param of params) {
    if (param.type === "ObjectPattern") {
      for (const property of param.properties ?? []) {
        if (property.type === "Property" && property.key?.type === "Identifier") {
          propNames.add(property.key.name);
        }
      }
    } else if (param.type === "Identifier") {
      propNames.add(param.name);
    }
  }
  return propNames;
};
```

## File: `packages/react-doctor/src/plugin/index.ts`
```typescript
import {
  noGiantComponent,
  noNestedComponentDefinition,
  noRenderInRender,
} from "./rules/architecture.js";
import {
  noBarrelImport,
  noFullLodashImport,
  noMoment,
  noUndeferredThirdParty,
  preferDynamicImport,
  useLazyMotion,
} from "./rules/bundle-size.js";
import { clientPassiveEventListeners } from "./rules/client.js";
import {
  noArrayIndexAsKey,
  noPreventDefault,
  renderingConditionalRender,
} from "./rules/correctness.js";
import {
  asyncParallel,
  jsBatchDomCss,
  jsCacheStorage,
  jsCombineIterations,
  jsEarlyExit,
  jsHoistRegexp,
  jsIndexMaps,
  jsMinMaxLoop,
  jsSetMapLookups,
  jsTosortedImmutable,
} from "./rules/js-performance.js";
import {
  nextjsAsyncClientComponent,
  nextjsImageMissingSizes,
  nextjsInlineScriptMissingId,
  nextjsMissingMetadata,
  nextjsNoAElement,
  nextjsNoClientFetchForServerData,
  nextjsNoClientSideRedirect,
  nextjsNoCssLink,
  nextjsNoFontLink,
  nextjsNoHeadImport,
  nextjsNoImgElement,
  nextjsNoNativeScript,
  nextjsNoPolyfillScript,
  nextjsNoRedirectInTryCatch,
  nextjsNoSideEffectInGetHandler,
  nextjsNoUseSearchParamsWithoutSuspense,
} from "./rules/nextjs.js";
import {
  noGlobalCssVariableAnimation,
  noLargeAnimatedBlur,
  noLayoutPropertyAnimation,
  noPermanentWillChange,
  noScaleFromZero,
  noTransitionAll,
  noUsememoSimpleExpression,
  renderingAnimateSvgWrapper,
  noInlinePropOnMemoComponent,
  renderingHydrationNoFlicker,
  rerenderMemoWithDefaultValue,
} from "./rules/performance.js";
import {
  rnNoRawText,
  rnNoDeprecatedModules,
  rnNoLegacyExpoPackages,
  rnNoDimensionsGet,
  rnNoInlineFlatlistRenderitem,
  rnNoLegacyShadowStyles,
  rnPreferReanimated,
  rnNoSingleElementStyleArray,
} from "./rules/react-native.js";
import { noEval, noSecretsInClientCode } from "./rules/security.js";
import { serverAfterNonblocking, serverAuthActions } from "./rules/server.js";
import {
  noCascadingSetState,
  noDerivedStateEffect,
  noDerivedUseState,
  noEffectEventHandler,
  noFetchInEffect,
  preferUseReducer,
  rerenderDependencies,
  rerenderFunctionalSetstate,
  rerenderLazyStateInit,
} from "./rules/state-and-effects.js";
import type { RulePlugin } from "./types.js";

const plugin: RulePlugin = {
  meta: { name: "react-doctor" },
  rules: {
    "no-derived-state-effect": noDerivedStateEffect,
    "no-fetch-in-effect": noFetchInEffect,
    "no-cascading-set-state": noCascadingSetState,
    "no-effect-event-handler": noEffectEventHandler,
    "no-derived-useState": noDerivedUseState,
    "prefer-useReducer": preferUseReducer,
    "rerender-lazy-state-init": rerenderLazyStateInit,
    "rerender-functional-setstate": rerenderFunctionalSetstate,
    "rerender-dependencies": rerenderDependencies,

    "no-giant-component": noGiantComponent,
    "no-render-in-render": noRenderInRender,
    "no-nested-component-definition": noNestedComponentDefinition,

    "no-usememo-simple-expression": noUsememoSimpleExpression,
    "no-layout-property-animation": noLayoutPropertyAnimation,
    "rerender-memo-with-default-value": rerenderMemoWithDefaultValue,
    "rendering-animate-svg-wrapper": renderingAnimateSvgWrapper,
    "no-inline-prop-on-memo-component": noInlinePropOnMemoComponent,
    "rendering-hydration-no-flicker": renderingHydrationNoFlicker,

    "no-transition-all": noTransitionAll,
    "no-global-css-variable-animation": noGlobalCssVariableAnimation,
    "no-large-animated-blur": noLargeAnimatedBlur,
    "no-scale-from-zero": noScaleFromZero,
    "no-permanent-will-change": noPermanentWillChange,

    "no-eval": noEval,
    "no-secrets-in-client-code": noSecretsInClientCode,

    "no-barrel-import": noBarrelImport,
    "no-full-lodash-import": noFullLodashImport,
    "no-moment": noMoment,
    "prefer-dynamic-import": preferDynamicImport,
    "use-lazy-motion": useLazyMotion,
    "no-undeferred-third-party": noUndeferredThirdParty,

    "no-array-index-as-key": noArrayIndexAsKey,
    "rendering-conditional-render": renderingConditionalRender,
    "no-prevent-default": noPreventDefault,

    "nextjs-no-img-element": nextjsNoImgElement,
    "nextjs-async-client-component": nextjsAsyncClientComponent,
    "nextjs-no-a-element": nextjsNoAElement,
    "nextjs-no-use-search-params-without-suspense": nextjsNoUseSearchParamsWithoutSuspense,
    "nextjs-no-client-fetch-for-server-data": nextjsNoClientFetchForServerData,
    "nextjs-missing-metadata": nextjsMissingMetadata,
    "nextjs-no-client-side-redirect": nextjsNoClientSideRedirect,
    "nextjs-no-redirect-in-try-catch": nextjsNoRedirectInTryCatch,
    "nextjs-image-missing-sizes": nextjsImageMissingSizes,
    "nextjs-no-native-script": nextjsNoNativeScript,
    "nextjs-inline-script-missing-id": nextjsInlineScriptMissingId,
    "nextjs-no-font-link": nextjsNoFontLink,
    "nextjs-no-css-link": nextjsNoCssLink,
    "nextjs-no-polyfill-script": nextjsNoPolyfillScript,
    "nextjs-no-head-import": nextjsNoHeadImport,
    "nextjs-no-side-effect-in-get-handler": nextjsNoSideEffectInGetHandler,

    "server-auth-actions": serverAuthActions,
    "server-after-nonblocking": serverAfterNonblocking,

    "client-passive-event-listeners": clientPassiveEventListeners,

    "js-combine-iterations": jsCombineIterations,
    "js-tosorted-immutable": jsTosortedImmutable,
    "js-hoist-regexp": jsHoistRegexp,
    "js-min-max-loop": jsMinMaxLoop,
    "js-set-map-lookups": jsSetMapLookups,
    "js-batch-dom-css": jsBatchDomCss,
    "js-index-maps": jsIndexMaps,
    "js-cache-storage": jsCacheStorage,
    "js-early-exit": jsEarlyExit,
    "async-parallel": asyncParallel,

    "rn-no-raw-text": rnNoRawText,
    "rn-no-deprecated-modules": rnNoDeprecatedModules,
    "rn-no-legacy-expo-packages": rnNoLegacyExpoPackages,
    "rn-no-dimensions-get": rnNoDimensionsGet,
    "rn-no-inline-flatlist-renderitem": rnNoInlineFlatlistRenderitem,
    "rn-no-legacy-shadow-styles": rnNoLegacyShadowStyles,
    "rn-prefer-reanimated": rnPreferReanimated,
    "rn-no-single-element-style-array": rnNoSingleElementStyleArray,
  },
};

export default plugin;
```

## File: `packages/react-doctor/src/plugin/types.ts`
```typescript
export interface ReportDescriptor {
  node: EsTreeNode;
  message: string;
}

export interface RuleContext {
  report: (descriptor: ReportDescriptor) => void;
  getFilename?: () => string;
}

export interface RuleVisitors {
  [selector: string]: ((node: EsTreeNode) => void) | (() => void);
}

export interface Rule {
  create: (context: RuleContext) => RuleVisitors;
}

export interface RulePlugin {
  meta: { name: string };
  rules: Record<string, Rule>;
}

export interface EsTreeNode {
  type: string;
  [key: string]: any;
}
```

## File: `packages/react-doctor/src/plugin/rules/architecture.ts`
```typescript
import {
  GENERIC_EVENT_SUFFIXES,
  GIANT_COMPONENT_LINE_THRESHOLD,
  RENDER_FUNCTION_PATTERN,
} from "../constants.js";
import { isComponentAssignment, isComponentDeclaration, isUppercaseName } from "../helpers.js";
import type { EsTreeNode, Rule, RuleContext } from "../types.js";

export const noGenericHandlerNames: Rule = {
  create: (context: RuleContext) => ({
    JSXAttribute(node: EsTreeNode) {
      if (node.name?.type !== "JSXIdentifier" || !node.name.name.startsWith("on")) return;
      if (!node.value || node.value.type !== "JSXExpressionContainer") return;

      const eventSuffix = node.name.name.slice(2);
      if (!GENERIC_EVENT_SUFFIXES.has(eventSuffix)) return;

      const mirroredHandlerName = `handle${eventSuffix}`;
      const expression = node.value.expression;
      if (expression?.type === "Identifier" && expression.name === mirroredHandlerName) {
        context.report({
          node,
          message: `Non-descriptive handler name "${expression.name}" — name should describe what it does, not when it runs`,
        });
      }
    },
  }),
};

export const noGiantComponent: Rule = {
  create: (context: RuleContext) => {
    const reportOversizedComponent = (
      nameNode: EsTreeNode,
      componentName: string,
      bodyNode: EsTreeNode,
    ): void => {
      if (!bodyNode.loc) return;
      const lineCount = bodyNode.loc.end.line - bodyNode.loc.start.line + 1;
      if (lineCount > GIANT_COMPONENT_LINE_THRESHOLD) {
        context.report({
          node: nameNode,
          message: `Component "${componentName}" is ${lineCount} lines — consider breaking it into smaller focused components`,
        });
      }
    };

    return {
      FunctionDeclaration(node: EsTreeNode) {
        if (!node.id?.name || !isUppercaseName(node.id.name)) return;
        reportOversizedComponent(node.id, node.id.name, node);
      },
      VariableDeclarator(node: EsTreeNode) {
        if (!isComponentAssignment(node)) return;
        reportOversizedComponent(node.id, node.id.name, node.init);
      },
    };
  },
};

export const noRenderInRender: Rule = {
  create: (context: RuleContext) => ({
    JSXExpressionContainer(node: EsTreeNode) {
      const expression = node.expression;
      if (expression?.type !== "CallExpression") return;

      let calleeName: string | null = null;
      if (expression.callee?.type === "Identifier") {
        calleeName = expression.callee.name;
      } else if (
        expression.callee?.type === "MemberExpression" &&
        expression.callee.property?.type === "Identifier"
      ) {
        calleeName = expression.callee.property.name;
      }

      if (calleeName && RENDER_FUNCTION_PATTERN.test(calleeName)) {
        context.report({
          node: expression,
          message: `Inline render function "${calleeName}()" — extract to a separate component for proper reconciliation`,
        });
      }
    },
  }),
};

export const noNestedComponentDefinition: Rule = {
  create: (context: RuleContext) => {
    const componentStack: string[] = [];

    return {
      FunctionDeclaration(node: EsTreeNode) {
        if (!isComponentDeclaration(node)) return;
        if (componentStack.length > 0) {
          context.report({
            node: node.id,
            message: `Component "${node.id.name}" defined inside "${componentStack[componentStack.length - 1]}" — creates new instance every render, destroying state`,
          });
        }
        componentStack.push(node.id.name);
      },
      "FunctionDeclaration:exit"(node: EsTreeNode) {
        if (isComponentDeclaration(node)) componentStack.pop();
      },
      VariableDeclarator(node: EsTreeNode) {
        if (!isComponentAssignment(node)) return;
        if (componentStack.length > 0) {
          context.report({
            node: node.id,
            message: `Component "${node.id.name}" defined inside "${componentStack[componentStack.length - 1]}" — creates new instance every render, destroying state`,
          });
        }
        componentStack.push(node.id.name);
      },
      "VariableDeclarator:exit"(node: EsTreeNode) {
        if (isComponentAssignment(node)) componentStack.pop();
      },
    };
  },
};
```

## File: `packages/react-doctor/src/plugin/rules/bundle-size.ts`
```typescript
import { BARREL_INDEX_SUFFIXES, HEAVY_LIBRARIES } from "../constants.js";
import { findJsxAttribute, hasJsxAttribute } from "../helpers.js";
import type { EsTreeNode, Rule, RuleContext } from "../types.js";

export const noBarrelImport: Rule = {
  create: (context: RuleContext) => {
    let didReportForFile = false;

    return {
      ImportDeclaration(node: EsTreeNode) {
        if (didReportForFile) return;

        const source = node.source?.value;
        if (typeof source !== "string" || !source.startsWith(".")) return;

        if (BARREL_INDEX_SUFFIXES.some((suffix) => source.endsWith(suffix))) {
          didReportForFile = true;
          context.report({
            node,
            message:
              "Import from barrel/index file — import directly from the source module for better tree-shaking",
          });
        }
      },
    };
  },
};

export const noFullLodashImport: Rule = {
  create: (context: RuleContext) => ({
    ImportDeclaration(node: EsTreeNode) {
      const source = node.source?.value;
      if (source === "lodash" || source === "lodash-es") {
        context.report({
          node,
          message: "Importing entire lodash library — import from 'lodash/functionName' instead",
        });
      }
    },
  }),
};

export const noMoment: Rule = {
  create: (context: RuleContext) => ({
    ImportDeclaration(node: EsTreeNode) {
      if (node.source?.value === "moment") {
        context.report({
          node,
          message: 'moment.js is 300kb+ — use "date-fns" or "dayjs" instead',
        });
      }
    },
  }),
};

export const preferDynamicImport: Rule = {
  create: (context: RuleContext) => ({
    ImportDeclaration(node: EsTreeNode) {
      const source = node.source?.value;
      if (typeof source === "string" && HEAVY_LIBRARIES.has(source)) {
        context.report({
          node,
          message: `"${source}" is a heavy library — use React.lazy() or next/dynamic for code splitting`,
        });
      }
    },
  }),
};

export const useLazyMotion: Rule = {
  create: (context: RuleContext) => ({
    ImportDeclaration(node: EsTreeNode) {
      const source = node.source?.value;
      if (source !== "framer-motion" && source !== "motion/react") return;

      const hasFullMotionImport = node.specifiers?.some(
        (specifier: EsTreeNode) =>
          specifier.type === "ImportSpecifier" && specifier.imported?.name === "motion",
      );

      if (hasFullMotionImport) {
        context.report({
          node,
          message: 'Import "m" with LazyMotion instead of "motion" — saves ~30kb in bundle size',
        });
      }
    },
  }),
};

export const noUndeferredThirdParty: Rule = {
  create: (context: RuleContext) => ({
    JSXOpeningElement(node: EsTreeNode) {
      if (node.name?.type !== "JSXIdentifier" || node.name.name !== "script") return;
      const attributes = node.attributes ?? [];
      if (!findJsxAttribute(attributes, "src")) return;

      if (!hasJsxAttribute(attributes, "defer") && !hasJsxAttribute(attributes, "async")) {
        context.report({
          node,
          message:
            "Synchronous <script> with src — add defer or async to avoid blocking first paint",
        });
      }
    },
  }),
};
```

## File: `packages/react-doctor/src/plugin/rules/client.ts`
```typescript
import { PASSIVE_EVENT_NAMES } from "../constants.js";
import { isMemberProperty } from "../helpers.js";
import type { EsTreeNode, Rule, RuleContext } from "../types.js";

export const clientPassiveEventListeners: Rule = {
  create: (context: RuleContext) => ({
    CallExpression(node: EsTreeNode) {
      if (!isMemberProperty(node.callee, "addEventListener")) return;
      if (node.arguments?.length < 2) return;

      const eventNameNode = node.arguments[0];
      if (eventNameNode.type !== "Literal" || !PASSIVE_EVENT_NAMES.has(eventNameNode.value)) return;

      const eventName = eventNameNode.value;
      const optionsArgument = node.arguments[2];

      if (!optionsArgument) {
        context.report({
          node,
          message: `"${eventName}" listener without { passive: true } — blocks scrolling performance`,
        });
        return;
      }

      if (optionsArgument.type !== "ObjectExpression") return;

      const hasPassiveTrue = optionsArgument.properties?.some(
        (property: EsTreeNode) =>
          property.type === "Property" &&
          property.key?.type === "Identifier" &&
          property.key.name === "passive" &&
          property.value?.type === "Literal" &&
          property.value.value === true,
      );

      if (!hasPassiveTrue) {
        context.report({
          node,
          message: `"${eventName}" listener without { passive: true } — blocks scrolling performance`,
        });
      }
    },
  }),
};
```

## File: `packages/react-doctor/src/plugin/rules/correctness.ts`
```typescript
import { INDEX_PARAMETER_NAMES } from "../constants.js";
import { findJsxAttribute, walkAst } from "../helpers.js";
import type { EsTreeNode, Rule, RuleContext } from "../types.js";

const extractIndexName = (node: EsTreeNode): string | null => {
  if (node.type === "Identifier" && INDEX_PARAMETER_NAMES.has(node.name)) return node.name;

  if (node.type === "TemplateLiteral") {
    const indexExpression = node.expressions?.find(
      (expression: EsTreeNode) =>
        expression.type === "Identifier" && INDEX_PARAMETER_NAMES.has(expression.name),
    );
    if (indexExpression) return indexExpression.name;
  }

  if (
    node.type === "CallExpression" &&
    node.callee?.type === "MemberExpression" &&
    node.callee.object?.type === "Identifier" &&
    INDEX_PARAMETER_NAMES.has(node.callee.object.name) &&
    node.callee.property?.type === "Identifier" &&
    node.callee.property.name === "toString"
  )
    return node.callee.object.name;

  if (
    node.type === "CallExpression" &&
    node.callee?.type === "Identifier" &&
    node.callee.name === "String" &&
    node.arguments?.[0]?.type === "Identifier" &&
    INDEX_PARAMETER_NAMES.has(node.arguments[0].name)
  )
    return node.arguments[0].name;

  return null;
};

const isInsideStaticPlaceholderMap = (node: EsTreeNode): boolean => {
  let current = node;
  while (current.parent) {
    current = current.parent;
    if (
      current.type === "CallExpression" &&
      current.callee?.type === "MemberExpression" &&
      current.callee.property?.name === "map"
    ) {
      const receiver = current.callee.object;
      if (receiver?.type === "CallExpression") {
        const callee = receiver.callee;
        if (
          callee?.type === "MemberExpression" &&
          callee.object?.type === "Identifier" &&
          callee.object.name === "Array" &&
          callee.property?.name === "from"
        )
          return true;
      }
      if (
        receiver?.type === "NewExpression" &&
        receiver.callee?.type === "Identifier" &&
        receiver.callee.name === "Array"
      )
        return true;
    }
  }
  return false;
};

export const noArrayIndexAsKey: Rule = {
  create: (context: RuleContext) => ({
    JSXAttribute(node: EsTreeNode) {
      if (node.name?.type !== "JSXIdentifier" || node.name.name !== "key") return;
      if (!node.value || node.value.type !== "JSXExpressionContainer") return;

      const indexName = extractIndexName(node.value.expression);
      if (!indexName) return;
      if (isInsideStaticPlaceholderMap(node)) return;

      context.report({
        node,
        message: `Array index "${indexName}" used as key — causes bugs when list is reordered or filtered`,
      });
    },
  }),
};

const PREVENT_DEFAULT_ELEMENTS: Record<string, string> = {
  form: "onSubmit",
  a: "onClick",
};

const containsPreventDefaultCall = (node: EsTreeNode): boolean => {
  let didFindPreventDefault = false;
  walkAst(node, (child) => {
    if (didFindPreventDefault) return;
    if (
      child.type === "CallExpression" &&
      child.callee?.type === "MemberExpression" &&
      child.callee.property?.type === "Identifier" &&
      child.callee.property.name === "preventDefault"
    ) {
      didFindPreventDefault = true;
    }
  });
  return didFindPreventDefault;
};

export const noPreventDefault: Rule = {
  create: (context: RuleContext) => ({
    JSXOpeningElement(node: EsTreeNode) {
      const elementName = node.name?.type === "JSXIdentifier" ? node.name.name : null;
      if (!elementName) return;

      const targetEventProp = PREVENT_DEFAULT_ELEMENTS[elementName];
      if (!targetEventProp) return;

      const eventAttribute = findJsxAttribute(node.attributes ?? [], targetEventProp);
      if (!eventAttribute?.value || eventAttribute.value.type !== "JSXExpressionContainer") return;

      const expression = eventAttribute.value.expression;
      if (
        expression?.type !== "ArrowFunctionExpression" &&
        expression?.type !== "FunctionExpression"
      )
        return;

      if (!containsPreventDefaultCall(expression)) return;

      const message =
        elementName === "form"
          ? "preventDefault() on <form> onSubmit — form won't work without JavaScript. Consider using a server action for progressive enhancement"
          : "preventDefault() on <a> onClick — use a <button> or routing component instead";

      context.report({ node, message });
    },
  }),
};

export const renderingConditionalRender: Rule = {
  create: (context: RuleContext) => ({
    LogicalExpression(node: EsTreeNode) {
      if (node.operator !== "&&") return;

      const isRightJsx = node.right?.type === "JSXElement" || node.right?.type === "JSXFragment";
      if (!isRightJsx) return;

      if (
        node.left?.type === "MemberExpression" &&
        node.left.property?.type === "Identifier" &&
        node.left.property.name === "length"
      ) {
        context.report({
          node,
          message:
            "Conditional rendering with .length can render '0' — use .length > 0 or Boolean(.length)",
        });
      }
    },
  }),
};
```

## File: `packages/react-doctor/src/plugin/rules/js-performance.ts`
```typescript
import {
  CHAINABLE_ITERATION_METHODS,
  DEEP_NESTING_THRESHOLD,
  DUPLICATE_STORAGE_READ_THRESHOLD,
  SEQUENTIAL_AWAIT_THRESHOLD,
  STORAGE_OBJECTS,
  TEST_FILE_PATTERN,
} from "../constants.js";
import { createLoopAwareVisitors, isMemberProperty, walkAst } from "../helpers.js";
import type { EsTreeNode, Rule, RuleContext } from "../types.js";

export const jsCombineIterations: Rule = {
  create: (context: RuleContext) => ({
    CallExpression(node: EsTreeNode) {
      if (node.callee?.type !== "MemberExpression" || node.callee.property?.type !== "Identifier")
        return;

      const outerMethod = node.callee.property.name;
      if (!CHAINABLE_ITERATION_METHODS.has(outerMethod)) return;

      const innerCall = node.callee.object;
      if (
        innerCall?.type !== "CallExpression" ||
        innerCall.callee?.type !== "MemberExpression" ||
        innerCall.callee.property?.type !== "Identifier"
      )
        return;

      const innerMethod = innerCall.callee.property.name;
      if (!CHAINABLE_ITERATION_METHODS.has(innerMethod)) return;

      context.report({
        node,
        message: `.${innerMethod}().${outerMethod}() iterates the array twice — combine into a single loop with .reduce() or for...of`,
      });
    },
  }),
};

export const jsTosortedImmutable: Rule = {
  create: (context: RuleContext) => ({
    CallExpression(node: EsTreeNode) {
      if (!isMemberProperty(node.callee, "sort")) return;

      const receiver = node.callee.object;
      if (
        receiver?.type === "ArrayExpression" &&
        receiver.elements?.length === 1 &&
        receiver.elements[0]?.type === "SpreadElement"
      ) {
        context.report({
          node,
          message: "[...array].sort() — use array.toSorted() for immutable sorting (ES2023)",
        });
      }
    },
  }),
};

export const jsHoistRegexp: Rule = {
  create: (context: RuleContext) =>
    createLoopAwareVisitors({
      NewExpression(node: EsTreeNode) {
        if (node.callee?.type === "Identifier" && node.callee.name === "RegExp") {
          context.report({
            node,
            message: "new RegExp() inside a loop — hoist to a module-level constant",
          });
        }
      },
    }),
};

export const jsMinMaxLoop: Rule = {
  create: (context: RuleContext) => ({
    MemberExpression(node: EsTreeNode) {
      if (!node.computed) return;

      const object = node.object;
      if (object?.type !== "CallExpression" || !isMemberProperty(object.callee, "sort")) return;

      const isFirstElement = node.property?.type === "Literal" && node.property.value === 0;
      const isLastElement =
        node.property?.type === "BinaryExpression" &&
        node.property.operator === "-" &&
        node.property.right?.type === "Literal" &&
        node.property.right.value === 1;

      if (isFirstElement || isLastElement) {
        const targetFunction = isFirstElement ? "min" : "max";
        context.report({
          node,
          message: `array.sort()[${isFirstElement ? "0" : "length-1"}] for min/max — use Math.${targetFunction}(...array) instead (O(n) vs O(n log n))`,
        });
      }
    },
  }),
};

export const jsSetMapLookups: Rule = {
  create: (context: RuleContext) =>
    createLoopAwareVisitors({
      CallExpression(node: EsTreeNode) {
        if (node.callee?.type !== "MemberExpression" || node.callee.property?.type !== "Identifier")
          return;
        const methodName = node.callee.property.name;
        if (methodName === "includes" || methodName === "indexOf") {
          context.report({
            node,
            message: `array.${methodName}() in a loop is O(n) per call — convert to a Set for O(1) lookups`,
          });
        }
      },
    }),
};

export const jsBatchDomCss: Rule = {
  create: (context: RuleContext) => {
    const isStyleAssignment = (node: EsTreeNode): boolean =>
      node.type === "ExpressionStatement" &&
      node.expression?.type === "AssignmentExpression" &&
      node.expression.left?.type === "MemberExpression" &&
      node.expression.left.object?.type === "MemberExpression" &&
      node.expression.left.object.property?.type === "Identifier" &&
      node.expression.left.object.property.name === "style";

    return {
      BlockStatement(node: EsTreeNode) {
        const statements = node.body ?? [];
        for (let statementIndex = 1; statementIndex < statements.length; statementIndex++) {
          if (
            isStyleAssignment(statements[statementIndex]) &&
            isStyleAssignment(statements[statementIndex - 1])
          ) {
            context.report({
              node: statements[statementIndex],
              message:
                "Multiple sequential element.style assignments — batch with cssText or classList for fewer reflows",
            });
          }
        }
      },
    };
  },
};

export const jsIndexMaps: Rule = {
  create: (context: RuleContext) =>
    createLoopAwareVisitors({
      CallExpression(node: EsTreeNode) {
        if (node.callee?.type !== "MemberExpression" || node.callee.property?.type !== "Identifier")
          return;
        const methodName = node.callee.property.name;
        if (methodName === "find" || methodName === "findIndex") {
          context.report({
            node,
            message: `array.${methodName}() in a loop is O(n*m) — build a Map for O(1) lookups`,
          });
        }
      },
    }),
};

export const jsCacheStorage: Rule = {
  create: (context: RuleContext) => {
    const storageReadCounts = new Map<string, number>();

    return {
      CallExpression(node: EsTreeNode) {
        if (!isMemberProperty(node.callee, "getItem")) return;
        if (
          node.callee.object?.type !== "Identifier" ||
          !STORAGE_OBJECTS.has(node.callee.object.name)
        )
          return;
        if (node.arguments?.[0]?.type !== "Literal") return;

        const storageKey = String(node.arguments[0].value);
        const readCount = (storageReadCounts.get(storageKey) ?? 0) + 1;
        storageReadCounts.set(storageKey, readCount);

        if (readCount === DUPLICATE_STORAGE_READ_THRESHOLD) {
          const storageName = node.callee.object.name;
          context.report({
            node,
            message: `${storageName}.getItem("${storageKey}") called multiple times — cache the result in a variable`,
          });
        }
      },
    };
  },
};

export const jsEarlyExit: Rule = {
  create: (context: RuleContext) => ({
    IfStatement(node: EsTreeNode) {
      if (node.consequent?.type !== "BlockStatement" || !node.consequent.body) return;

      let nestingDepth = 0;
      let currentBlock = node.consequent;
      while (currentBlock?.type === "BlockStatement" && currentBlock.body?.length === 1) {
        const innerStatement = currentBlock.body[0];
        if (innerStatement.type !== "IfStatement") break;
        nestingDepth++;
        currentBlock = innerStatement.consequent;
      }

      if (nestingDepth >= DEEP_NESTING_THRESHOLD) {
        context.report({
          node,
          message: `${nestingDepth + 1} levels of nested if statements — use early returns to flatten`,
        });
      }
    },
  }),
};

export const asyncParallel: Rule = {
  create: (context: RuleContext) => {
    const filename = context.getFilename?.() ?? "";
    const isTestFile = TEST_FILE_PATTERN.test(filename);

    return {
      BlockStatement(node: EsTreeNode) {
        if (isTestFile) return;
        const consecutiveAwaitStatements: EsTreeNode[] = [];

        const flushConsecutiveAwaits = (): void => {
          if (consecutiveAwaitStatements.length >= SEQUENTIAL_AWAIT_THRESHOLD) {
            reportIfIndependent(consecutiveAwaitStatements, context);
          }
          consecutiveAwaitStatements.length = 0;
        };

        for (const statement of node.body ?? []) {
          const isAwaitStatement =
            (statement.type === "VariableDeclaration" &&
              statement.declarations?.length === 1 &&
              statement.declarations[0].init?.type === "AwaitExpression") ||
            (statement.type === "ExpressionStatement" &&
              statement.expression?.type === "AwaitExpression");

          if (isAwaitStatement) {
            consecutiveAwaitStatements.push(statement);
          } else {
            flushConsecutiveAwaits();
          }
        }
        flushConsecutiveAwaits();
      },
    };
  },
};

const reportIfIndependent = (statements: EsTreeNode[], context: RuleContext): void => {
  const declaredNames = new Set<string>();

  for (const statement of statements) {
    if (statement.type !== "VariableDeclaration") continue;
    const declarator = statement.declarations[0];
    const awaitArgument = declarator.init?.argument;

    let referencesEarlierResult = false;
    walkAst(awaitArgument, (child: EsTreeNode) => {
      if (child.type === "Identifier" && declaredNames.has(child.name)) {
        referencesEarlierResult = true;
      }
    });

    if (referencesEarlierResult) return;

    if (declarator.id?.type === "Identifier") {
      declaredNames.add(declarator.id.name);
    }
  }

  context.report({
    node: statements[0],
    message: `${statements.length} sequential await statements that appear independent — use Promise.all() for parallel execution`,
  });
};
```

## File: `packages/react-doctor/src/plugin/rules/nextjs.ts`
```typescript
import {
  APP_DIRECTORY_PATTERN,
  EFFECT_HOOK_NAMES,
  EXECUTABLE_SCRIPT_TYPES,
  GOOGLE_FONTS_PATTERN,
  INTERNAL_PAGE_PATH_PATTERN,
  MUTATING_ROUTE_SEGMENTS,
  NEXTJS_NAVIGATION_FUNCTIONS,
  OG_ROUTE_PATTERN,
  PAGE_FILE_PATTERN,
  PAGE_OR_LAYOUT_FILE_PATTERN,
  PAGES_DIRECTORY_PATTERN,
  POLYFILL_SCRIPT_PATTERN,
  ROUTE_HANDLER_FILE_PATTERN,
} from "../constants.js";
import {
  containsFetchCall,
  findJsxAttribute,
  findSideEffect,
  getEffectCallback,
  hasDirective,
  hasJsxAttribute,
  isComponentAssignment,
  isHookCall,
  isMemberProperty,
  isUppercaseName,
  walkAst,
} from "../helpers.js";
import type { EsTreeNode, Rule, RuleContext } from "../types.js";

export const nextjsNoImgElement: Rule = {
  create: (context: RuleContext) => {
    const filename = context.getFilename?.() ?? "";
    const isOgRoute = OG_ROUTE_PATTERN.test(filename);

    return {
      JSXOpeningElement(node: EsTreeNode) {
        if (isOgRoute) return;
        if (node.name?.type === "JSXIdentifier" && node.name.name === "img") {
          context.report({
            node,
            message:
              "Use next/image instead of <img> — provides automatic optimization, lazy loading, and responsive srcset",
          });
        }
      },
    };
  },
};

export const nextjsAsyncClientComponent: Rule = {
  create: (context: RuleContext) => {
    let fileHasUseClient = false;

    return {
      Program(programNode: EsTreeNode) {
        fileHasUseClient = hasDirective(programNode, "use client");
      },
      FunctionDeclaration(node: EsTreeNode) {
        if (!fileHasUseClient || !node.async) return;
        if (!node.id?.name || !isUppercaseName(node.id.name)) return;
        context.report({
          node,
          message: `Async client component "${node.id.name}" — client components cannot be async`,
        });
      },
      VariableDeclarator(node: EsTreeNode) {
        if (!fileHasUseClient) return;
        if (!isComponentAssignment(node) || !node.init?.async) return;
        context.report({
          node,
          message: `Async client component "${node.id.name}" — client components cannot be async`,
        });
      },
    };
  },
};

export const nextjsNoAElement: Rule = {
  create: (context: RuleContext) => ({
    JSXOpeningElement(node: EsTreeNode) {
      if (node.name?.type !== "JSXIdentifier" || node.name.name !== "a") return;

      const hrefAttribute = findJsxAttribute(node.attributes ?? [], "href");
      if (!hrefAttribute?.value) return;

      let hrefValue = null;
      if (hrefAttribute.value.type === "Literal") {
        hrefValue = hrefAttribute.value.value;
      } else if (
        hrefAttribute.value.type === "JSXExpressionContainer" &&
        hrefAttribute.value.expression?.type === "Literal"
      ) {
        hrefValue = hrefAttribute.value.expression.value;
      }

      if (typeof hrefValue === "string" && hrefValue.startsWith("/")) {
        context.report({
          node,
          message:
            "Use next/link instead of <a> for internal links — enables client-side navigation and prefetching",
        });
      }
    },
  }),
};

export const nextjsNoUseSearchParamsWithoutSuspense: Rule = {
  create: (context: RuleContext) => ({
    CallExpression(node: EsTreeNode) {
      if (!isHookCall(node, "useSearchParams")) return;
      context.report({
        node,
        message:
          "useSearchParams() requires a <Suspense> boundary — without one, the entire page bails out to client-side rendering",
      });
    },
  }),
};

export const nextjsNoClientFetchForServerData: Rule = {
  create: (context: RuleContext) => {
    let fileHasUseClient = false;

    return {
      Program(programNode: EsTreeNode) {
        fileHasUseClient = hasDirective(programNode, "use client");
      },
      CallExpression(node: EsTreeNode) {
        if (!fileHasUseClient || !isHookCall(node, EFFECT_HOOK_NAMES)) return;

        const callback = getEffectCallback(node);
        if (!callback || !containsFetchCall(callback)) return;

        const filename = context.getFilename?.() ?? "";
        const isPageOrLayoutFile =
          PAGE_OR_LAYOUT_FILE_PATTERN.test(filename) || PAGES_DIRECTORY_PATTERN.test(filename);

        if (isPageOrLayoutFile) {
          context.report({
            node,
            message:
              "useEffect + fetch in a page/layout — fetch data server-side with a server component instead",
          });
        }
      },
    };
  },
};

export const nextjsMissingMetadata: Rule = {
  create: (context: RuleContext) => ({
    Program(programNode: EsTreeNode) {
      const filename = context.getFilename?.() ?? "";
      if (!PAGE_FILE_PATTERN.test(filename)) return;
      if (INTERNAL_PAGE_PATH_PATTERN.test(filename)) return;

      const hasMetadataExport = programNode.body?.some((statement: EsTreeNode) => {
        if (statement.type !== "ExportNamedDeclaration") return false;
        const declaration = statement.declaration;
        if (declaration?.type === "VariableDeclaration") {
          return declaration.declarations?.some(
            (declarator: EsTreeNode) =>
              declarator.id?.type === "Identifier" &&
              (declarator.id.name === "metadata" || declarator.id.name === "generateMetadata"),
          );
        }
        if (declaration?.type === "FunctionDeclaration") {
          return declaration.id?.name === "generateMetadata";
        }
        return false;
      });

      if (!hasMetadataExport) {
        context.report({
          node: programNode,
          message: "Page without metadata or generateMetadata export — hurts SEO",
        });
      }
    },
  }),
};

const isClientSideRedirect = (node: EsTreeNode): boolean => {
  if (node.type === "CallExpression" && node.callee?.type === "MemberExpression") {
    const objectName = node.callee.object?.type === "Identifier" ? node.callee.object.name : null;
    if (
      objectName === "router" &&
      (isMemberProperty(node.callee, "push") || isMemberProperty(node.callee, "replace"))
    )
      return true;
  }

  if (node.type === "AssignmentExpression" && node.left?.type === "MemberExpression") {
    const objectName = node.left.object?.type === "Identifier" ? node.left.object.name : null;
    const propertyName = node.left.property?.type === "Identifier" ? node.left.property.name : null;
    if (objectName === "window" && propertyName === "location") return true;
    if (objectName === "location" && propertyName === "href") return true;
  }

  return false;
};

export const nextjsNoClientSideRedirect: Rule = {
  create: (context: RuleContext) => ({
    CallExpression(node: EsTreeNode) {
      if (!isHookCall(node, EFFECT_HOOK_NAMES)) return;
      const callback = getEffectCallback(node);
      if (!callback) return;

      walkAst(callback, (child: EsTreeNode) => {
        if (isClientSideRedirect(child)) {
          context.report({
            node: child,
            message:
              "Client-side redirect in useEffect — use redirect() from next/navigation or handle in middleware instead",
          });
        }
      });
    },
  }),
};

export const nextjsNoRedirectInTryCatch: Rule = {
  create: (context: RuleContext) => {
    let tryCatchDepth = 0;

    return {
      TryStatement() {
        tryCatchDepth++;
      },
      "TryStatement:exit"() {
        tryCatchDepth--;
      },
      CallExpression(node: EsTreeNode) {
        if (tryCatchDepth === 0) return;
        if (node.callee?.type !== "Identifier") return;
        if (!NEXTJS_NAVIGATION_FUNCTIONS.has(node.callee.name)) return;

        context.report({
          node,
          message: `${node.callee.name}() inside try-catch — this throws a special error Next.js handles internally. Move it outside the try block or use unstable_rethrow() in the catch`,
        });
      },
    };
  },
};

export const nextjsImageMissingSizes: Rule = {
  create: (context: RuleContext) => ({
    JSXOpeningElement(node: EsTreeNode) {
      if (node.name?.type !== "JSXIdentifier" || node.name.name !== "Image") return;
      const attributes = node.attributes ?? [];
      if (!hasJsxAttribute(attributes, "fill")) return;
      if (hasJsxAttribute(attributes, "sizes")) return;

      context.report({
        node,
        message:
          "next/image with fill but no sizes — the browser downloads the largest image. Add a sizes attribute for responsive behavior",
      });
    },
  }),
};

export const nextjsNoNativeScript: Rule = {
  create: (context: RuleContext) => ({
    JSXOpeningElement(node: EsTreeNode) {
      if (node.name?.type !== "JSXIdentifier" || node.name.name !== "script") return;

      const typeAttribute = findJsxAttribute(node.attributes ?? [], "type");
      const typeValue = typeAttribute?.value?.type === "Literal" ? typeAttribute.value.value : null;
      if (typeof typeValue === "string" && !EXECUTABLE_SCRIPT_TYPES.has(typeValue)) return;

      context.report({
        node,
        message:
          "Use next/script <Script> instead of <script> — provides loading strategy optimization and deferred loading",
      });
    },
  }),
};

export const nextjsInlineScriptMissingId: Rule = {
  create: (context: RuleContext) => ({
    JSXOpeningElement(node: EsTreeNode) {
      if (node.name?.type !== "JSXIdentifier" || node.name.name !== "Script") return;
      const attributes = node.attributes ?? [];

      if (hasJsxAttribute(attributes, "src")) return;
      if (hasJsxAttribute(attributes, "id")) return;

      context.report({
        node,
        message:
          "Inline <Script> without id — Next.js requires an id attribute to track inline scripts",
      });
    },
  }),
};

export const nextjsNoFontLink: Rule = {
  create: (context: RuleContext) => ({
    JSXOpeningElement(node: EsTreeNode) {
      if (node.name?.type !== "JSXIdentifier" || node.name.name !== "link") return;
      const attributes = node.attributes ?? [];

      const hrefAttribute = findJsxAttribute(attributes, "href");
      if (!hrefAttribute?.value) return;

      const hrefValue = hrefAttribute.value.type === "Literal" ? hrefAttribute.value.value : null;

      if (typeof hrefValue === "string" && GOOGLE_FONTS_PATTERN.test(hrefValue)) {
        context.report({
          node,
          message:
            "Loading Google Fonts via <link> — use next/font instead for self-hosting, zero layout shift, and no render-blocking requests",
        });
      }
    },
  }),
};

export const nextjsNoCssLink: Rule = {
  create: (context: RuleContext) => ({
    JSXOpeningElement(node: EsTreeNode) {
      if (node.name?.type !== "JSXIdentifier" || node.name.name !== "link") return;
      const attributes = node.attributes ?? [];

      const relAttribute = findJsxAttribute(attributes, "rel");
      if (!relAttribute?.value) return;
      const relValue = relAttribute.value.type === "Literal" ? relAttribute.value.value : null;
      if (relValue !== "stylesheet") return;

      const hrefAttribute = findJsxAttribute(attributes, "href");
      if (!hrefAttribute?.value) return;
      const hrefValue = hrefAttribute.value.type === "Literal" ? hrefAttribute.value.value : null;
      if (typeof hrefValue === "string" && GOOGLE_FONTS_PATTERN.test(hrefValue)) return;

      context.report({
        node,
        message: '<link rel="stylesheet"> tag — import CSS directly for bundling and optimization',
      });
    },
  }),
};

export const nextjsNoPolyfillScript: Rule = {
  create: (context: RuleContext) => ({
    JSXOpeningElement(node: EsTreeNode) {
      if (node.name?.type !== "JSXIdentifier") return;
      if (node.name.name !== "script" && node.name.name !== "Script") return;

      const srcAttribute = findJsxAttribute(node.attributes ?? [], "src");
      if (!srcAttribute?.value) return;

      const srcValue = srcAttribute.value.type === "Literal" ? srcAttribute.value.value : null;

      if (typeof srcValue === "string" && POLYFILL_SCRIPT_PATTERN.test(srcValue)) {
        context.report({
          node,
          message:
            "Polyfill CDN script — Next.js includes polyfills for fetch, Promise, Object.assign, and 50+ others automatically",
        });
      }
    },
  }),
};

export const nextjsNoHeadImport: Rule = {
  create: (context: RuleContext) => ({
    ImportDeclaration(node: EsTreeNode) {
      if (node.source?.value !== "next/head") return;

      const filename = context.getFilename?.() ?? "";
      if (!APP_DIRECTORY_PATTERN.test(filename)) return;

      context.report({
        node,
        message: "next/head is not supported in the App Router — use the Metadata API instead",
      });
    },
  }),
};

const extractMutatingRouteSegment = (filename: string): string | null => {
  const segments = filename.split("/");
  for (const segment of segments) {
    const cleaned = segment.replace(/^\[.*\]$/, "");
    if (MUTATING_ROUTE_SEGMENTS.has(cleaned)) return cleaned;
  }
  return null;
};

const getExportedGetHandlerBody = (node: EsTreeNode): EsTreeNode | null => {
  if (node.type !== "ExportNamedDeclaration") return null;
  const declaration = node.declaration;
  if (!declaration) return null;

  if (declaration.type === "FunctionDeclaration" && declaration.id?.name === "GET") {
    return declaration.body;
  }

  if (declaration.type === "VariableDeclaration") {
    const declarator = declaration.declarations?.[0];
    if (
      declarator?.id?.type === "Identifier" &&
      declarator.id.name === "GET" &&
      declarator.init &&
      (declarator.init.type === "ArrowFunctionExpression" ||
        declarator.init.type === "FunctionExpression")
    ) {
      return declarator.init.body;
    }
  }

  return null;
};

export const nextjsNoSideEffectInGetHandler: Rule = {
  create: (context: RuleContext) => ({
    ExportNamedDeclaration(node: EsTreeNode) {
      const filename = context.getFilename?.() ?? "";
      if (!ROUTE_HANDLER_FILE_PATTERN.test(filename)) return;

      const handlerBody = getExportedGetHandlerBody(node);
      if (!handlerBody) return;

      const mutatingSegment = extractMutatingRouteSegment(filename);
      if (mutatingSegment) {
        context.report({
          node,
          message: `GET handler on "/${mutatingSegment}" route — use POST to prevent CSRF and unintended prefetch triggers`,
        });
        return;
      }

      const sideEffect = findSideEffect(handlerBody);
      if (sideEffect) {
        context.report({
          node,
          message: `GET handler has side effects (${sideEffect}) — use POST to prevent CSRF and unintended prefetch triggers`,
        });
      }
    },
  }),
};
```

## File: `packages/react-doctor/src/plugin/rules/performance.ts`
```typescript
import {
  ANIMATION_CALLBACK_NAMES,
  BLUR_VALUE_PATTERN,
  EFFECT_HOOK_NAMES,
  LARGE_BLUR_THRESHOLD_PX,
  LAYOUT_PROPERTIES,
  LOADING_STATE_PATTERN,
  MOTION_ANIMATE_PROPS,
  SETTER_PATTERN,
} from "../constants.js";
import {
  getEffectCallback,
  isComponentAssignment,
  isHookCall,
  isMemberProperty,
  isSimpleExpression,
  isUppercaseName,
  walkAst,
} from "../helpers.js";
import type { EsTreeNode, Rule, RuleContext } from "../types.js";

const isMemoCall = (node: EsTreeNode): boolean => {
  if (node.type !== "CallExpression") return false;
  if (node.callee?.type === "Identifier" && node.callee.name === "memo") return true;
  if (
    node.callee?.type === "MemberExpression" &&
    node.callee.object?.type === "Identifier" &&
    node.callee.object.name === "React" &&
    node.callee.property?.type === "Identifier" &&
    node.callee.property.name === "memo"
  )
    return true;
  return false;
};

const isInlineReference = (node: EsTreeNode): string | null => {
  if (
    node.type === "ArrowFunctionExpression" ||
    node.type === "FunctionExpression" ||
    (node.type === "CallExpression" &&
      node.callee?.type === "MemberExpression" &&
      node.callee.property?.name === "bind")
  )
    return "functions";

  if (node.type === "ObjectExpression") return "objects";
  if (node.type === "ArrayExpression") return "Arrays";
  if (node.type === "JSXElement" || node.type === "JSXFragment") return "JSX";

  return null;
};

export const noInlinePropOnMemoComponent: Rule = {
  create: (context: RuleContext) => {
    const memoizedComponentNames = new Set<string>();

    return {
      VariableDeclarator(node: EsTreeNode) {
        if (node.id?.type !== "Identifier" || !node.init) return;
        if (isMemoCall(node.init)) {
          memoizedComponentNames.add(node.id.name);
        }
      },
      ExportDefaultDeclaration(node: EsTreeNode) {
        if (node.declaration && isMemoCall(node.declaration)) {
          const innerArgument = node.declaration.arguments?.[0];
          if (innerArgument?.type === "Identifier") {
            memoizedComponentNames.add(innerArgument.name);
          }
        }
      },
      JSXAttribute(node: EsTreeNode) {
        if (!node.value || node.value.type !== "JSXExpressionContainer") return;

        const openingElement = node.parent;
        if (!openingElement || openingElement.type !== "JSXOpeningElement") return;

        let elementName: string | null = null;
        if (openingElement.name?.type === "JSXIdentifier") {
          elementName = openingElement.name.name;
        }
        if (!elementName || !memoizedComponentNames.has(elementName)) return;

        const propType = isInlineReference(node.value.expression);
        if (propType) {
          context.report({
            node: node.value.expression,
            message: `JSX attribute values should not contain ${propType} created in the same scope — ${elementName} is wrapped in memo(), so new references cause unnecessary re-renders`,
          });
        }
      },
    };
  },
};

export const noUsememoSimpleExpression: Rule = {
  create: (context: RuleContext) => ({
    CallExpression(node: EsTreeNode) {
      if (!isHookCall(node, "useMemo")) return;

      const callback = node.arguments?.[0];
      if (!callback) return;
      if (callback.type !== "ArrowFunctionExpression" && callback.type !== "FunctionExpression")
        return;

      let returnExpression = null;
      if (callback.body?.type !== "BlockStatement") {
        returnExpression = callback.body;
      } else if (
        callback.body.body?.length === 1 &&
        callback.body.body[0].type === "ReturnStatement"
      ) {
        returnExpression = callback.body.body[0].argument;
      }

      if (returnExpression && isSimpleExpression(returnExpression)) {
        context.report({
          node,
          message:
            "useMemo wrapping a trivially cheap expression — memo overhead exceeds the computation",
        });
      }
    },
  }),
};

const isMotionElement = (attributeNode: EsTreeNode): boolean => {
  const openingElement = attributeNode.parent;
  if (!openingElement || openingElement.type !== "JSXOpeningElement") return false;

  const elementName = openingElement.name;
  if (
    elementName?.type === "JSXMemberExpression" &&
    elementName.object?.type === "JSXIdentifier" &&
    (elementName.object.name === "motion" || elementName.object.name === "m")
  )
    return true;

  if (elementName?.type === "JSXIdentifier" && elementName.name.startsWith("Motion")) return true;

  return false;
};

export const noLayoutPropertyAnimation: Rule = {
  create: (context: RuleContext) => ({
    JSXAttribute(node: EsTreeNode) {
      if (node.name?.type !== "JSXIdentifier" || !MOTION_ANIMATE_PROPS.has(node.name.name)) return;
      if (!node.value || node.value.type !== "JSXExpressionContainer") return;
      if (isMotionElement(node)) return;

      const expression = node.value.expression;
      if (expression?.type !== "ObjectExpression") return;

      for (const property of expression.properties ?? []) {
        if (property.type !== "Property") continue;
        let propertyName = null;
        if (property.key?.type === "Identifier") {
          propertyName = property.key.name;
        } else if (property.key?.type === "Literal") {
          propertyName = property.key.value;
        }

        if (propertyName && LAYOUT_PROPERTIES.has(propertyName)) {
          context.report({
            node: property,
            message: `Animating layout property "${propertyName}" triggers layout recalculation every frame — use transform/scale or the layout prop`,
          });
        }
      }
    },
  }),
};

export const noTransitionAll: Rule = {
  create: (context: RuleContext) => ({
    JSXAttribute(node: EsTreeNode) {
      if (node.name?.type !== "JSXIdentifier" || node.name.name !== "style") return;
      if (node.value?.type !== "JSXExpressionContainer") return;

      const expression = node.value.expression;
      if (expression?.type !== "ObjectExpression") return;

      for (const property of expression.properties ?? []) {
        if (property.type !== "Property") continue;
        const key = property.key?.type === "Identifier" ? property.key.name : null;
        if (key !== "transition") continue;

        if (
          property.value?.type === "Literal" &&
          typeof property.value.value === "string" &&
          property.value.value.startsWith("all")
        ) {
          context.report({
            node: property,
            message:
              'transition: "all" animates every property including layout — list only the properties you animate',
          });
        }
      }
    },
  }),
};

export const noGlobalCssVariableAnimation: Rule = {
  create: (context: RuleContext) => ({
    CallExpression(node: EsTreeNode) {
      if (node.callee?.type !== "Identifier") return;
      if (!ANIMATION_CALLBACK_NAMES.has(node.callee.name)) return;

      const callback = node.arguments?.[0];
      if (!callback) return;

      const calleeName = node.callee.name;
      walkAst(callback, (child: EsTreeNode) => {
        if (child.type !== "CallExpression") return;
        if (!isMemberProperty(child.callee, "setProperty")) return;
        if (child.arguments?.[0]?.type !== "Literal") return;

        const variableName = child.arguments[0].value;
        if (typeof variableName !== "string" || !variableName.startsWith("--")) return;

        context.report({
          node: child,
          message: `CSS variable "${variableName}" updated in ${calleeName} — forces style recalculation on all inheriting elements every frame`,
        });
      });
    },
  }),
};

export const noLargeAnimatedBlur: Rule = {
  create: (context: RuleContext) => ({
    JSXAttribute(node: EsTreeNode) {
      if (node.name?.type !== "JSXIdentifier") return;
      if (node.name.name !== "style" && !MOTION_ANIMATE_PROPS.has(node.name.name)) return;
      if (node.value?.type !== "JSXExpressionContainer") return;

      const expression = node.value.expression;
      if (expression?.type !== "ObjectExpression") return;

      for (const property of expression.properties ?? []) {
        if (property.type !== "Property") continue;
        const key = property.key?.type === "Identifier" ? property.key.name : null;
        if (key !== "filter" && key !== "backdropFilter" && key !== "WebkitBackdropFilter")
          continue;
        if (property.value?.type !== "Literal" || typeof property.value.value !== "string")
          continue;

        const match = BLUR_VALUE_PATTERN.exec(property.value.value);
        if (!match) continue;

        const blurRadius = Number.parseFloat(match[1]);
        if (blurRadius > LARGE_BLUR_THRESHOLD_PX) {
          context.report({
            node: property,
            message: `blur(${blurRadius}px) is expensive — cost escalates with radius and layer size, can exceed GPU memory on mobile`,
          });
        }
      }
    },
  }),
};

export const noScaleFromZero: Rule = {
  create: (context: RuleContext) => ({
    JSXAttribute(node: EsTreeNode) {
      if (node.name?.type !== "JSXIdentifier") return;
      if (node.name.name !== "initial" && node.name.name !== "exit") return;
      if (node.value?.type !== "JSXExpressionContainer") return;

      const expression = node.value.expression;
      if (expression?.type !== "ObjectExpression") return;

      for (const property of expression.properties ?? []) {
        if (property.type !== "Property") continue;
        const key = property.key?.type === "Identifier" ? property.key.name : null;
        if (key !== "scale") continue;

        if (property.value?.type === "Literal" && property.value.value === 0) {
          context.report({
            node: property,
            message:
              "scale: 0 makes elements appear from nowhere — use scale: 0.95 with opacity: 0 for natural entrance",
          });
        }
      }
    },
  }),
};

export const noPermanentWillChange: Rule = {
  create: (context: RuleContext) => ({
    JSXAttribute(node: EsTreeNode) {
      if (node.name?.type !== "JSXIdentifier" || node.name.name !== "style") return;
      if (node.value?.type !== "JSXExpressionContainer") return;

      const expression = node.value.expression;
      if (expression?.type !== "ObjectExpression") return;

      for (const property of expression.properties ?? []) {
        if (property.type !== "Property") continue;
        const key = property.key?.type === "Identifier" ? property.key.name : null;
        if (key !== "willChange") continue;

        context.report({
          node: property,
          message:
            "Permanent will-change wastes GPU memory — apply only during active animation and remove after",
        });
      }
    },
  }),
};

export const rerenderMemoWithDefaultValue: Rule = {
  create: (context: RuleContext) => {
    const checkDefaultProps = (params: EsTreeNode[]): void => {
      for (const param of params) {
        if (param.type !== "ObjectPattern") continue;
        for (const property of param.properties ?? []) {
          if (property.type !== "Property" || property.value?.type !== "AssignmentPattern")
            continue;
          const defaultValue = property.value.right;
          if (defaultValue?.type === "ObjectExpression" && defaultValue.properties?.length === 0) {
            context.report({
              node: defaultValue,
              message:
                "Default prop value {} creates a new object reference every render — extract to a module-level constant",
            });
          }
          if (defaultValue?.type === "ArrayExpression" && defaultValue.elements?.length === 0) {
            context.report({
              node: defaultValue,
              message:
                "Default prop value [] creates a new array reference every render — extract to a module-level constant",
            });
          }
        }
      }
    };

    return {
      FunctionDeclaration(node: EsTreeNode) {
        if (!node.id?.name || !isUppercaseName(node.id.name)) return;
        checkDefaultProps(node.params ?? []);
      },
      VariableDeclarator(node: EsTreeNode) {
        if (!isComponentAssignment(node)) return;
        checkDefaultProps(node.init.params ?? []);
      },
    };
  },
};

export const renderingAnimateSvgWrapper: Rule = {
  create: (context: RuleContext) => ({
    JSXOpeningElement(node: EsTreeNode) {
      if (node.name?.type !== "JSXIdentifier" || node.name.name !== "svg") return;

      const hasAnimationProp = node.attributes?.some(
        (attribute: EsTreeNode) =>
          attribute.type === "JSXAttribute" &&
          attribute.name?.type === "JSXIdentifier" &&
          MOTION_ANIMATE_PROPS.has(attribute.name.name),
      );

      if (hasAnimationProp) {
        context.report({
          node,
          message:
            "Animation props directly on <svg> — wrap in a <div> or <motion.div> for better rendering performance",
        });
      }
    },
  }),
};

export const renderingUsetransitionLoading: Rule = {
  create: (context: RuleContext) => ({
    VariableDeclarator(node: EsTreeNode) {
      if (node.id?.type !== "ArrayPattern" || !node.id.elements?.length) return;
      if (!node.init || !isHookCall(node.init, "useState")) return;
      if (!node.init.arguments?.length) return;

      const initializer = node.init.arguments[0];
      if (initializer.type !== "Literal" || initializer.value !== false) return;

      const stateVariableName = node.id.elements[0]?.name;
      if (!stateVariableName || !LOADING_STATE_PATTERN.test(stateVariableName)) return;

      context.report({
        node: node.init,
        message: `useState for "${stateVariableName}" — if this guards a state transition (not an async fetch), consider useTransition instead`,
      });
    },
  }),
};

export const renderingHydrationNoFlicker: Rule = {
  create: (context: RuleContext) => ({
    CallExpression(node: EsTreeNode) {
      if (!isHookCall(node, EFFECT_HOOK_NAMES) || node.arguments?.length < 2) return;

      const depsNode = node.arguments[1];
      if (depsNode.type !== "ArrayExpression" || depsNode.elements?.length !== 0) return;

      const callback = getEffectCallback(node);
      if (!callback) return;

      const bodyStatements =
        callback.body?.type === "BlockStatement" ? callback.body.body : [callback.body];
      if (!bodyStatements || bodyStatements.length !== 1) return;

      const soleStatement = bodyStatements[0];
      if (
        soleStatement?.type === "ExpressionStatement" &&
        soleStatement.expression?.type === "CallExpression" &&
        soleStatement.expression.callee?.type === "Identifier" &&
        SETTER_PATTERN.test(soleStatement.expression.callee.name)
      ) {
        context.report({
          node,
          message:
            "useEffect(setState, []) on mount causes a flash — consider useSyncExternalStore or suppressHydrationWarning",
        });
      }
    },
  }),
};
```

## File: `packages/react-doctor/src/plugin/rules/react-native.ts`
```typescript
import {
  DEPRECATED_RN_MODULE_REPLACEMENTS,
  LEGACY_EXPO_PACKAGE_REPLACEMENTS,
  LEGACY_SHADOW_STYLE_PROPERTIES,
  RAW_TEXT_PREVIEW_MAX_CHARS,
  REACT_NATIVE_LIST_COMPONENTS,
  REACT_NATIVE_TEXT_COMPONENTS,
} from "../constants.js";
import { hasDirective, isMemberProperty } from "../helpers.js";
import type { EsTreeNode, Rule, RuleContext } from "../types.js";

const resolveJsxElementName = (openingElement: EsTreeNode): string | null => {
  const elementName = openingElement?.name;
  if (!elementName) return null;
  if (elementName.type === "JSXIdentifier") return elementName.name;
  if (elementName.type === "JSXMemberExpression") return elementName.property?.name ?? null;
  return null;
};

const truncateText = (text: string): string =>
  text.length > RAW_TEXT_PREVIEW_MAX_CHARS
    ? `${text.slice(0, RAW_TEXT_PREVIEW_MAX_CHARS)}...`
    : text;

const isRawTextContent = (child: EsTreeNode): boolean => {
  if (child.type === "JSXText") return Boolean(child.value?.trim());
  if (child.type !== "JSXExpressionContainer" || !child.expression) return false;

  const expression = child.expression;
  return (
    (expression.type === "Literal" &&
      (typeof expression.value === "string" || typeof expression.value === "number")) ||
    expression.type === "TemplateLiteral"
  );
};

const getRawTextDescription = (child: EsTreeNode): string => {
  if (child.type === "JSXText") {
    return `"${truncateText(child.value.trim())}"`;
  }

  if (child.type === "JSXExpressionContainer" && child.expression) {
    const expression = child.expression;
    if (expression.type === "Literal" && typeof expression.value === "string") {
      return `"${truncateText(expression.value)}"`;
    }
    if (expression.type === "Literal" && typeof expression.value === "number") {
      return `{${expression.value}}`;
    }
    if (expression.type === "TemplateLiteral") return "template literal";
  }

  return "text content";
};

export const rnNoRawText: Rule = {
  create: (context: RuleContext) => {
    let isDomComponentFile = false;

    return {
      Program(programNode: EsTreeNode) {
        isDomComponentFile = hasDirective(programNode, "use dom");
      },
      JSXElement(node: EsTreeNode) {
        if (isDomComponentFile) return;

        const elementName = resolveJsxElementName(node.openingElement);
        if (
          elementName &&
          (REACT_NATIVE_TEXT_COMPONENTS.has(elementName) || elementName.endsWith("Text"))
        )
          return;

        for (const child of node.children ?? []) {
          if (!isRawTextContent(child)) continue;

          context.report({
            node: child,
            message: `Raw ${getRawTextDescription(child)} outside a <Text> component — this will crash on React Native`,
          });
        }
      },
    };
  },
};

export const rnNoDeprecatedModules: Rule = {
  create: (context: RuleContext) => ({
    ImportDeclaration(node: EsTreeNode) {
      if (node.source?.value !== "react-native") return;

      for (const specifier of node.specifiers ?? []) {
        if (specifier.type !== "ImportSpecifier") continue;
        const importedName = specifier.imported?.name;
        if (!importedName) continue;

        const replacement = DEPRECATED_RN_MODULE_REPLACEMENTS[importedName];
        if (!replacement) continue;

        context.report({
          node: specifier,
          message: `"${importedName}" was removed from react-native — use ${replacement} instead`,
        });
      }
    },
  }),
};

export const rnNoLegacyExpoPackages: Rule = {
  create: (context: RuleContext) => ({
    ImportDeclaration(node: EsTreeNode) {
      const source = node.source?.value;
      if (typeof source !== "string") return;

      for (const [packageName, replacement] of Object.entries(LEGACY_EXPO_PACKAGE_REPLACEMENTS)) {
        if (source === packageName || source.startsWith(`${packageName}/`)) {
          context.report({
            node,
            message: `"${packageName}" is deprecated — use ${replacement}`,
          });
          return;
        }
      }
    },
  }),
};

export const rnNoDimensionsGet: Rule = {
  create: (context: RuleContext) => ({
    CallExpression(node: EsTreeNode) {
      if (node.callee?.type !== "MemberExpression") return;
      if (node.callee.object?.type !== "Identifier" || node.callee.object.name !== "Dimensions")
        return;

      if (isMemberProperty(node.callee, "get")) {
        context.report({
          node,
          message:
            "Dimensions.get() does not update on screen rotation or resize — use useWindowDimensions() for reactive layout",
        });
      }

      if (isMemberProperty(node.callee, "addEventListener")) {
        context.report({
          node,
          message:
            "Dimensions.addEventListener() was removed in React Native 0.72 — use useWindowDimensions() instead",
        });
      }
    },
  }),
};

export const rnNoInlineFlatlistRenderitem: Rule = {
  create: (context: RuleContext) => ({
    JSXAttribute(node: EsTreeNode) {
      if (node.name?.type !== "JSXIdentifier" || node.name.name !== "renderItem") return;
      if (!node.value || node.value.type !== "JSXExpressionContainer") return;

      const openingElement = node.parent;
      if (!openingElement || openingElement.type !== "JSXOpeningElement") return;

      const listComponentName = resolveJsxElementName(openingElement);
      if (!listComponentName || !REACT_NATIVE_LIST_COMPONENTS.has(listComponentName)) return;

      const expression = node.value.expression;
      if (
        expression?.type !== "ArrowFunctionExpression" &&
        expression?.type !== "FunctionExpression"
      )
        return;

      context.report({
        node: expression,
        message: `Inline renderItem on <${listComponentName}> creates a new function reference every render — extract to a named function or wrap in useCallback`,
      });
    },
  }),
};

const reportLegacyShadowProperties = (objectExpression: EsTreeNode, context: RuleContext): void => {
  const legacyShadowPropertyNames: string[] = [];

  for (const property of objectExpression.properties ?? []) {
    if (property.type !== "Property") continue;
    const propertyName = property.key?.type === "Identifier" ? property.key.name : null;
    if (propertyName && LEGACY_SHADOW_STYLE_PROPERTIES.has(propertyName)) {
      legacyShadowPropertyNames.push(propertyName);
    }
  }

  if (legacyShadowPropertyNames.length === 0) return;

  const quotedPropertyNames = legacyShadowPropertyNames.map((name) => `"${name}"`).join(", ");
  context.report({
    node: objectExpression,
    message: `Legacy shadow style${legacyShadowPropertyNames.length > 1 ? "s" : ""} ${quotedPropertyNames} — use boxShadow for cross-platform shadows on the new architecture`,
  });
};

export const rnNoLegacyShadowStyles: Rule = {
  create: (context: RuleContext) => ({
    JSXAttribute(node: EsTreeNode) {
      if (node.name?.type !== "JSXIdentifier" || node.name.name !== "style") return;
      if (node.value?.type !== "JSXExpressionContainer") return;

      const expression = node.value.expression;

      if (expression?.type === "ObjectExpression") {
        reportLegacyShadowProperties(expression, context);
      } else if (expression?.type === "ArrayExpression") {
        for (const element of expression.elements ?? []) {
          if (element?.type === "ObjectExpression") {
            reportLegacyShadowProperties(element, context);
          }
        }
      }
    },
    CallExpression(node: EsTreeNode) {
      if (node.callee?.type !== "MemberExpression") return;
      if (node.callee.object?.type !== "Identifier" || node.callee.object.name !== "StyleSheet")
        return;
      if (!isMemberProperty(node.callee, "create")) return;

      const stylesArgument = node.arguments?.[0];
      if (stylesArgument?.type !== "ObjectExpression") return;

      for (const styleDefinition of stylesArgument.properties ?? []) {
        if (styleDefinition.type !== "Property") continue;
        if (styleDefinition.value?.type !== "ObjectExpression") continue;
        reportLegacyShadowProperties(styleDefinition.value, context);
      }
    },
  }),
};

export const rnPreferReanimated: Rule = {
  create: (context: RuleContext) => ({
    ImportDeclaration(node: EsTreeNode) {
      if (node.source?.value !== "react-native") return;

      for (const specifier of node.specifiers ?? []) {
        if (specifier.type !== "ImportSpecifier") continue;
        if (specifier.imported?.name !== "Animated") continue;

        context.report({
          node: specifier,
          message:
            "Animated from react-native runs animations on the JS thread — use react-native-reanimated for performant UI-thread animations",
        });
      }
    },
  }),
};

export const rnNoSingleElementStyleArray: Rule = {
  create: (context: RuleContext) => ({
    JSXAttribute(node: EsTreeNode) {
      const propName = node.name?.type === "JSXIdentifier" ? node.name.name : null;
      if (!propName) return;
      if (propName !== "style" && !propName.endsWith("Style")) return;
      if (node.value?.type !== "JSXExpressionContainer") return;

      const expression = node.value.expression;
      if (expression?.type !== "ArrayExpression") return;
      if (expression.elements?.length !== 1) return;

      context.report({
        node: expression,
        message: `Single-element style array on "${propName}" — use ${propName}={value} instead of ${propName}={[value]} to avoid unnecessary array allocation`,
      });
    },
  }),
};
```

## File: `packages/react-doctor/src/plugin/rules/security.ts`
```typescript
import {
  SECRET_FALSE_POSITIVE_SUFFIXES,
  SECRET_MIN_LENGTH_CHARS,
  SECRET_PATTERNS,
  SECRET_VARIABLE_PATTERN,
} from "../constants.js";
import type { EsTreeNode, Rule, RuleContext } from "../types.js";

export const noEval: Rule = {
  create: (context: RuleContext) => ({
    CallExpression(node: EsTreeNode) {
      if (node.callee?.type === "Identifier" && node.callee.name === "eval") {
        context.report({
          node,
          message: "eval() is a code injection risk — avoid dynamic code execution",
        });
        return;
      }

      if (
        node.callee?.type === "Identifier" &&
        (node.callee.name === "setTimeout" || node.callee.name === "setInterval") &&
        node.arguments?.[0]?.type === "Literal" &&
        typeof node.arguments[0].value === "string"
      ) {
        context.report({
          node,
          message: `${node.callee.name}() with string argument executes code dynamically — use a function instead`,
        });
      }
    },
    NewExpression(node: EsTreeNode) {
      if (node.callee?.type === "Identifier" && node.callee.name === "Function") {
        context.report({
          node,
          message: "new Function() is a code injection risk — avoid dynamic code execution",
        });
      }
    },
  }),
};

export const noSecretsInClientCode: Rule = {
  create: (context: RuleContext) => ({
    VariableDeclarator(node: EsTreeNode) {
      if (node.id?.type !== "Identifier") return;
      if (node.init?.type !== "Literal" || typeof node.init.value !== "string") return;

      const variableName = node.id.name;
      const literalValue = node.init.value;

      const trailingSuffix = variableName.split("_").pop()?.toLowerCase() ?? "";
      const isUiConstant = SECRET_FALSE_POSITIVE_SUFFIXES.has(trailingSuffix);

      if (
        SECRET_VARIABLE_PATTERN.test(variableName) &&
        !isUiConstant &&
        literalValue.length > SECRET_MIN_LENGTH_CHARS
      ) {
        context.report({
          node,
          message: `Possible hardcoded secret in "${variableName}" — use environment variables instead`,
        });
        return;
      }

      if (SECRET_PATTERNS.some((pattern) => pattern.test(literalValue))) {
        context.report({
          node,
          message: "Hardcoded secret detected — use environment variables instead",
        });
      }
    },
  }),
};
```

## File: `packages/react-doctor/src/plugin/rules/server.ts`
```typescript
import {
  AUTH_CHECK_LOOKAHEAD_STATEMENTS,
  AUTH_FUNCTION_NAMES,
  SERVER_ACTION_DIRECTORY_PATTERN,
  SERVER_ACTION_FILE_PATTERN,
} from "../constants.js";
import { hasDirective, hasUseServerDirective, walkAst } from "../helpers.js";
import type { EsTreeNode, Rule, RuleContext } from "../types.js";

const containsAuthCheck = (statements: EsTreeNode[]): boolean => {
  let foundAuthCall = false;
  for (const statement of statements) {
    walkAst(statement, (child: EsTreeNode) => {
      if (foundAuthCall) return;
      let callNode: EsTreeNode | null = null;
      if (child.type === "CallExpression") {
        callNode = child;
      } else if (child.type === "AwaitExpression" && child.argument?.type === "CallExpression") {
        callNode = child.argument;
      }

      if (
        callNode?.callee?.type === "Identifier" &&
        AUTH_FUNCTION_NAMES.has(callNode.callee.name)
      ) {
        foundAuthCall = true;
      }
    });
  }
  return foundAuthCall;
};

export const serverAuthActions: Rule = {
  create: (context: RuleContext) => {
    let fileHasUseServerDirective = false;

    return {
      Program(programNode: EsTreeNode) {
        fileHasUseServerDirective = hasDirective(programNode, "use server");
      },
      ExportNamedDeclaration(node: EsTreeNode) {
        const declaration = node.declaration;
        if (declaration?.type !== "FunctionDeclaration" || !declaration?.async) return;

        const isServerAction = fileHasUseServerDirective || hasUseServerDirective(declaration);
        if (!isServerAction) return;

        const firstStatements = (declaration.body?.body ?? []).slice(
          0,
          AUTH_CHECK_LOOKAHEAD_STATEMENTS,
        );
        if (!containsAuthCheck(firstStatements)) {
          const functionName = declaration.id?.name ?? "anonymous";
          context.report({
            node: declaration.id ?? node,
            message: `Server action "${functionName}" — add auth check (auth(), getSession(), etc.) at the top`,
          });
        }
      },
    };
  },
};

export const serverAfterNonblocking: Rule = {
  create: (context: RuleContext) => {
    let fileHasUseServerDirective = false;

    return {
      Program(programNode: EsTreeNode) {
        fileHasUseServerDirective = hasDirective(programNode, "use server");
      },
      CallExpression(node: EsTreeNode) {
        if (!fileHasUseServerDirective) return;
        if (node.callee?.type !== "MemberExpression") return;
        if (node.callee.property?.type !== "Identifier") return;

        const objectName =
          node.callee.object?.type === "Identifier" ? node.callee.object.name : null;
        if (!objectName) return;

        const methodName = node.callee.property.name;
        const isLoggingCall =
          (objectName === "console" &&
            (methodName === "log" || methodName === "info" || methodName === "warn")) ||
          (objectName === "analytics" &&
            (methodName === "track" || methodName === "identify" || methodName === "page"));
        if (!isLoggingCall) return;

        context.report({
          node,
          message: `${objectName}.${methodName}() in server action — use after() for non-blocking logging/analytics`,
        });
      },
    };
  },
};
```

## File: `packages/react-doctor/src/plugin/rules/state-and-effects.ts`
```typescript
import {
  CASCADING_SET_STATE_THRESHOLD,
  EFFECT_HOOK_NAMES,
  HOOKS_WITH_DEPS,
  RELATED_USE_STATE_THRESHOLD,
  TRIVIAL_INITIALIZER_NAMES,
} from "../constants.js";
import {
  containsFetchCall,
  countSetStateCalls,
  extractDestructuredPropNames,
  getCallbackStatements,
  getEffectCallback,
  isComponentAssignment,
  isHookCall,
  isSetterIdentifier,
  isUppercaseName,
  walkAst,
} from "../helpers.js";
import type { EsTreeNode, Rule, RuleContext } from "../types.js";

export const noDerivedStateEffect: Rule = {
  create: (context: RuleContext) => ({
    CallExpression(node: EsTreeNode) {
      if (!isHookCall(node, EFFECT_HOOK_NAMES) || node.arguments.length < 2) return;

      const callback = getEffectCallback(node);
      if (!callback) return;

      const depsNode = node.arguments[1];
      if (depsNode.type !== "ArrayExpression" || !depsNode.elements?.length) return;

      const dependencyNames = new Set(
        depsNode.elements
          .filter((element: EsTreeNode) => element?.type === "Identifier")
          .map((element: EsTreeNode) => element.name),
      );
      if (dependencyNames.size === 0) return;

      const statements = getCallbackStatements(callback);
      if (statements.length === 0) return;

      const containsOnlySetStateCalls = statements.every(
        (statement: EsTreeNode) =>
          statement.type === "ExpressionStatement" &&
          statement.expression?.type === "CallExpression" &&
          statement.expression.callee?.type === "Identifier" &&
          isSetterIdentifier(statement.expression.callee.name),
      );
      if (!containsOnlySetStateCalls) return;

      let allArgumentsDeriveFromDeps = true;
      let hasAnyDependencyReference = false;
      for (const statement of statements) {
        const setStateArguments = statement.expression.arguments;
        if (!setStateArguments?.length) continue;

        const referencedIdentifiers: string[] = [];
        walkAst(setStateArguments[0], (child: EsTreeNode) => {
          if (child.type === "Identifier") referencedIdentifiers.push(child.name);
        });

        const nonSetterIdentifiers = referencedIdentifiers.filter(
          (name) => !isSetterIdentifier(name),
        );

        if (nonSetterIdentifiers.some((name) => dependencyNames.has(name))) {
          hasAnyDependencyReference = true;
        }

        if (nonSetterIdentifiers.some((name) => !dependencyNames.has(name))) {
          allArgumentsDeriveFromDeps = false;
          break;
        }
      }

      if (allArgumentsDeriveFromDeps) {
        context.report({
          node,
          message: hasAnyDependencyReference
            ? "Derived state in useEffect — compute during render instead"
            : "State reset in useEffect — use a key prop to reset component state when props change",
        });
      }
    },
  }),
};

export const noFetchInEffect: Rule = {
  create: (context: RuleContext) => ({
    CallExpression(node: EsTreeNode) {
      if (!isHookCall(node, EFFECT_HOOK_NAMES)) return;
      const callback = getEffectCallback(node);
      if (!callback) return;

      if (containsFetchCall(callback)) {
        context.report({
          node,
          message:
            "fetch() inside useEffect — use a data fetching library (react-query, SWR) or server component",
        });
      }
    },
  }),
};

export const noCascadingSetState: Rule = {
  create: (context: RuleContext) => ({
    CallExpression(node: EsTreeNode) {
      if (!isHookCall(node, EFFECT_HOOK_NAMES)) return;
      const callback = getEffectCallback(node);
      if (!callback) return;

      const setStateCallCount = countSetStateCalls(callback);
      if (setStateCallCount >= CASCADING_SET_STATE_THRESHOLD) {
        context.report({
          node,
          message: `${setStateCallCount} setState calls in a single useEffect — consider using useReducer or deriving state`,
        });
      }
    },
  }),
};

export const noEffectEventHandler: Rule = {
  create: (context: RuleContext) => ({
    CallExpression(node: EsTreeNode) {
      if (!isHookCall(node, EFFECT_HOOK_NAMES) || node.arguments.length < 2) return;

      const callback = getEffectCallback(node);
      if (!callback) return;

      const depsNode = node.arguments[1];
      if (depsNode.type !== "ArrayExpression" || !depsNode.elements?.length) return;

      const dependencyNames = new Set(
        depsNode.elements
          .filter((element: EsTreeNode) => element?.type === "Identifier")
          .map((element: EsTreeNode) => element.name),
      );

      const statements = getCallbackStatements(callback);
      if (statements.length !== 1) return;

      const soleStatement = statements[0];
      if (
        soleStatement.type === "IfStatement" &&
        soleStatement.test?.type === "Identifier" &&
        dependencyNames.has(soleStatement.test.name)
      ) {
        context.report({
          node,
          message:
            "useEffect simulating an event handler — move logic to an actual event handler instead",
        });
      }
    },
  }),
};

export const noDerivedUseState: Rule = {
  create: (context: RuleContext) => {
    const componentPropNames = new Set<string>();

    return {
      FunctionDeclaration(node: EsTreeNode) {
        if (!node.id?.name || !isUppercaseName(node.id.name)) return;
        for (const name of extractDestructuredPropNames(node.params ?? [])) {
          componentPropNames.add(name);
        }
      },
      VariableDeclarator(node: EsTreeNode) {
        if (!isComponentAssignment(node)) return;
        for (const name of extractDestructuredPropNames(node.init?.params ?? [])) {
          componentPropNames.add(name);
        }
      },
      CallExpression(node: EsTreeNode) {
        if (!isHookCall(node, "useState") || !node.arguments?.length) return;
        const initializer = node.arguments[0];
        if (initializer.type !== "Identifier") return;

        if (componentPropNames.has(initializer.name)) {
          context.report({
            node,
            message: `useState initialized from prop "${initializer.name}" — if this value should stay in sync with the prop, derive it during render instead`,
          });
        }
      },
    };
  },
};

export const preferUseReducer: Rule = {
  create: (context: RuleContext) => {
    const reportExcessiveUseState = (body: EsTreeNode, componentName: string): void => {
      if (body.type !== "BlockStatement") return;
      let useStateCount = 0;
      for (const statement of body.body ?? []) {
        if (statement.type !== "VariableDeclaration") continue;
        for (const declarator of statement.declarations ?? []) {
          if (isHookCall(declarator.init, "useState")) useStateCount++;
        }
      }
      if (useStateCount >= RELATED_USE_STATE_THRESHOLD) {
        context.report({
          node: body,
          message: `Component "${componentName}" has ${useStateCount} useState calls — consider useReducer for related state`,
        });
      }
    };

    return {
      FunctionDeclaration(node: EsTreeNode) {
        if (!node.id?.name || !isUppercaseName(node.id.name)) return;
        reportExcessiveUseState(node.body, node.id.name);
      },
      VariableDeclarator(node: EsTreeNode) {
        if (!isComponentAssignment(node)) return;
        reportExcessiveUseState(node.init.body, node.id.name);
      },
    };
  },
};

export const rerenderLazyStateInit: Rule = {
  create: (context: RuleContext) => ({
    CallExpression(node: EsTreeNode) {
      if (!isHookCall(node, "useState") || !node.arguments?.length) return;
      const initializer = node.arguments[0];
      if (initializer.type !== "CallExpression") return;

      const calleeName =
        initializer.callee?.type === "Identifier"
          ? initializer.callee.name
          : (initializer.callee?.property?.name ?? "fn");

      if (TRIVIAL_INITIALIZER_NAMES.has(calleeName)) return;

      context.report({
        node: initializer,
        message: `useState(${calleeName}()) calls initializer on every render — use useState(() => ${calleeName}()) for lazy initialization`,
      });
    },
  }),
};

export const rerenderFunctionalSetstate: Rule = {
  create: (context: RuleContext) => ({
    CallExpression(node: EsTreeNode) {
      if (node.callee?.type !== "Identifier" || !isSetterIdentifier(node.callee.name)) return;
      if (!node.arguments?.length) return;

      const argument = node.arguments[0];
      if (
        argument.type === "BinaryExpression" &&
        (argument.operator === "+" || argument.operator === "-") &&
        argument.left?.type === "Identifier"
      ) {
        context.report({
          node,
          message: `${node.callee.name}(${argument.left.name} ${argument.operator} ...) — use functional update to avoid stale closures`,
        });
      }
    },
  }),
};

export const rerenderDependencies: Rule = {
  create: (context: RuleContext) => ({
    CallExpression(node: EsTreeNode) {
      if (!isHookCall(node, HOOKS_WITH_DEPS) || node.arguments.length < 2) return;
      const depsNode = node.arguments[1];
      if (depsNode.type !== "ArrayExpression") return;

      for (const element of depsNode.elements ?? []) {
        if (!element) continue;
        if (element.type === "ObjectExpression") {
          context.report({
            node: element,
            message:
              "Object literal in useEffect deps — creates new reference every render, causing infinite re-runs",
          });
        }
        if (element.type === "ArrayExpression") {
          context.report({
            node: element,
            message:
              "Array literal in useEffect deps — creates new reference every render, causing infinite re-runs",
          });
        }
      }
    },
  }),
};
```

## File: `packages/react-doctor/src/utils/calculate-score.ts`
```typescript
import {
  ERROR_ESTIMATED_FIX_RATE,
  ERROR_RULE_PENALTY,
  ESTIMATE_SCORE_API_URL,
  PERFECT_SCORE,
  SCORE_API_URL,
  SCORE_GOOD_THRESHOLD,
  SCORE_OK_THRESHOLD,
  WARNING_ESTIMATED_FIX_RATE,
  WARNING_RULE_PENALTY,
} from "../constants.js";
import type { Diagnostic, EstimatedScoreResult, ScoreResult } from "../types.js";
import { proxyFetch } from "./proxy-fetch.js";

const getScoreLabel = (score: number): string => {
  if (score >= SCORE_GOOD_THRESHOLD) return "Great";
  if (score >= SCORE_OK_THRESHOLD) return "Needs work";
  return "Critical";
};

const countUniqueRules = (
  diagnostics: Diagnostic[],
): { errorRuleCount: number; warningRuleCount: number } => {
  const errorRules = new Set<string>();
  const warningRules = new Set<string>();

  for (const diagnostic of diagnostics) {
    const ruleKey = `${diagnostic.plugin}/${diagnostic.rule}`;
    if (diagnostic.severity === "error") {
      errorRules.add(ruleKey);
    } else {
      warningRules.add(ruleKey);
    }
  }

  return { errorRuleCount: errorRules.size, warningRuleCount: warningRules.size };
};

const scoreFromRuleCounts = (errorRuleCount: number, warningRuleCount: number): number => {
  const penalty = errorRuleCount * ERROR_RULE_PENALTY + warningRuleCount * WARNING_RULE_PENALTY;
  return Math.max(0, Math.round(PERFECT_SCORE - penalty));
};

const estimateScoreLocally = (diagnostics: Diagnostic[]): EstimatedScoreResult => {
  const { errorRuleCount, warningRuleCount } = countUniqueRules(diagnostics);

  const currentScore = scoreFromRuleCounts(errorRuleCount, warningRuleCount);
  const estimatedUnfixedErrorRuleCount = Math.round(
    errorRuleCount * (1 - ERROR_ESTIMATED_FIX_RATE),
  );
  const estimatedUnfixedWarningRuleCount = Math.round(
    warningRuleCount * (1 - WARNING_ESTIMATED_FIX_RATE),
  );
  const estimatedScore = scoreFromRuleCounts(
    estimatedUnfixedErrorRuleCount,
    estimatedUnfixedWarningRuleCount,
  );

  return {
    currentScore,
    currentLabel: getScoreLabel(currentScore),
    estimatedScore,
    estimatedLabel: getScoreLabel(estimatedScore),
  };
};

export const calculateScoreLocally = (diagnostics: Diagnostic[]): ScoreResult => {
  const { currentScore, currentLabel } = estimateScoreLocally(diagnostics);
  return { score: currentScore, label: currentLabel };
};

export const calculateScore = async (diagnostics: Diagnostic[]): Promise<ScoreResult | null> => {
  try {
    const response = await proxyFetch(SCORE_API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ diagnostics }),
    });

    if (!response.ok) return calculateScoreLocally(diagnostics);

    return (await response.json()) as ScoreResult;
  } catch {
    return calculateScoreLocally(diagnostics);
  }
};

export const fetchEstimatedScore = async (
  diagnostics: Diagnostic[],
): Promise<EstimatedScoreResult | null> => {
  try {
    const response = await proxyFetch(ESTIMATE_SCORE_API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ diagnostics }),
    });

    if (!response.ok) return estimateScoreLocally(diagnostics);

    return (await response.json()) as EstimatedScoreResult;
  } catch {
    return estimateScoreLocally(diagnostics);
  }
};
```

## File: `packages/react-doctor/src/utils/check-reduced-motion.ts`
```typescript
import { execSync } from "node:child_process";
import path from "node:path";
import { MOTION_LIBRARY_PACKAGES } from "../plugin/constants.js";
import type { Diagnostic } from "../types.js";
import { isFile } from "./is-file.js";
import { readPackageJson } from "./read-package-json.js";

const REDUCED_MOTION_GREP_PATTERN =
  "prefers-reduced-motion|useReducedMotion|MotionConfig|reducedMotion";
const REDUCED_MOTION_FILE_GLOBS = '"*.ts" "*.tsx" "*.js" "*.jsx" "*.css" "*.scss"';

const MISSING_REDUCED_MOTION_DIAGNOSTIC: Diagnostic = {
  filePath: "package.json",
  plugin: "react-doctor",
  rule: "require-reduced-motion",
  severity: "error",
  message:
    "Project uses a motion library but has no prefers-reduced-motion handling — required for accessibility (WCAG 2.3.3)",
  help: "Add `useReducedMotion()` from your animation library, or a `@media (prefers-reduced-motion: reduce)` CSS query",
  line: 0,
  column: 0,
  category: "Accessibility",
  weight: 2,
};

export const checkReducedMotion = (rootDirectory: string): Diagnostic[] => {
  const packageJsonPath = path.join(rootDirectory, "package.json");
  if (!isFile(packageJsonPath)) return [];

  let hasMotionLibrary = false;
  try {
    const packageJson = readPackageJson(packageJsonPath);
    const allDependencies = { ...packageJson.dependencies, ...packageJson.devDependencies };
    hasMotionLibrary = Object.keys(allDependencies).some((packageName) =>
      MOTION_LIBRARY_PACKAGES.has(packageName),
    );
  } catch {
    return [];
  }
  if (!hasMotionLibrary) return [];

  try {
    execSync(`git grep -ql -E "${REDUCED_MOTION_GREP_PATTERN}" -- ${REDUCED_MOTION_FILE_GLOBS}`, {
      cwd: rootDirectory,
      stdio: "pipe",
    });
    return [];
  } catch {
    return [MISSING_REDUCED_MOTION_DIAGNOSTIC];
  }
};
```

## File: `packages/react-doctor/src/utils/colorize-by-score.ts`
```typescript
import { SCORE_GOOD_THRESHOLD, SCORE_OK_THRESHOLD } from "../constants.js";
import { highlighter } from "./highlighter.js";

export const colorizeByScore = (text: string, score: number): string => {
  if (score >= SCORE_GOOD_THRESHOLD) return highlighter.success(text);
  if (score >= SCORE_OK_THRESHOLD) return highlighter.warn(text);
  return highlighter.error(text);
};
```

## File: `packages/react-doctor/src/utils/combine-diagnostics.ts`
```typescript
import { JSX_FILE_PATTERN } from "../constants.js";
import type { Diagnostic, ReactDoctorConfig } from "../types.js";
import { checkReducedMotion } from "./check-reduced-motion.js";
import { filterIgnoredDiagnostics, filterInlineSuppressions } from "./filter-diagnostics.js";

export const computeJsxIncludePaths = (includePaths: string[]): string[] | undefined =>
  includePaths.length > 0
    ? includePaths.filter((filePath) => JSX_FILE_PATTERN.test(filePath))
    : undefined;

export const combineDiagnostics = (
  lintDiagnostics: Diagnostic[],
  deadCodeDiagnostics: Diagnostic[],
  directory: string,
  isDiffMode: boolean,
  userConfig: ReactDoctorConfig | null,
): Diagnostic[] => {
  const merged = [
    ...lintDiagnostics,
    ...deadCodeDiagnostics,
    ...(isDiffMode ? [] : checkReducedMotion(directory)),
  ];
  const filtered = userConfig ? filterIgnoredDiagnostics(merged, userConfig, directory) : merged;
  return filterInlineSuppressions(filtered, directory);
};
```

## File: `packages/react-doctor/src/utils/discover-project.ts`
```typescript
import fs from "node:fs";
import path from "node:path";
import { spawnSync } from "node:child_process";
import {
  GIT_LS_FILES_MAX_BUFFER_BYTES,
  IGNORED_DIRECTORIES,
  SOURCE_FILE_PATTERN,
} from "../constants.js";
import type {
  DependencyInfo,
  Framework,
  PackageJson,
  ProjectInfo,
  WorkspacePackage,
} from "../types.js";
import { findMonorepoRoot, isMonorepoRoot } from "./find-monorepo-root.js";
import { isFile } from "./is-file.js";
import { isPlainObject } from "./is-plain-object.js";
import { readPackageJson } from "./read-package-json.js";

const REACT_COMPILER_PACKAGES = new Set([
  "babel-plugin-react-compiler",
  "react-compiler-runtime",
  "eslint-plugin-react-compiler",
]);

const NEXT_CONFIG_FILENAMES = [
  "next.config.js",
  "next.config.mjs",
  "next.config.ts",
  "next.config.cjs",
];

const BABEL_CONFIG_FILENAMES = [
  ".babelrc",
  ".babelrc.json",
  "babel.config.js",
  "babel.config.json",
  "babel.config.cjs",
  "babel.config.mjs",
];

const VITE_CONFIG_FILENAMES = [
  "vite.config.js",
  "vite.config.ts",
  "vite.config.mjs",
  "vite.config.cjs",
];

const EXPO_APP_CONFIG_FILENAMES = ["app.json", "app.config.js", "app.config.ts"];

const REACT_COMPILER_CONFIG_PATTERN = /react-compiler|reactCompiler/;

const FRAMEWORK_PACKAGES: Record<string, Framework> = {
  next: "nextjs",
  vite: "vite",
  "react-scripts": "cra",
  "@remix-run/react": "remix",
  gatsby: "gatsby",
  expo: "expo",
  "react-native": "react-native",
};

const FRAMEWORK_DISPLAY_NAMES: Record<Framework, string> = {
  nextjs: "Next.js",
  vite: "Vite",
  cra: "Create React App",
  remix: "Remix",
  gatsby: "Gatsby",
  expo: "Expo",
  "react-native": "React Native",
  unknown: "React",
};

export const formatFrameworkName = (framework: Framework): string =>
  FRAMEWORK_DISPLAY_NAMES[framework];

const countSourceFilesViaFilesystem = (rootDirectory: string): number => {
  let count = 0;
  const stack = [rootDirectory];

  while (stack.length > 0) {
    const currentDirectory = stack.pop()!;
    const entries = fs.readdirSync(currentDirectory, { withFileTypes: true });

    for (const entry of entries) {
      if (entry.isDirectory()) {
        if (!entry.name.startsWith(".") && !IGNORED_DIRECTORIES.has(entry.name)) {
          stack.push(path.join(currentDirectory, entry.name));
        }
        continue;
      }
      if (entry.isFile() && SOURCE_FILE_PATTERN.test(entry.name)) {
        count++;
      }
    }
  }

  return count;
};

const countSourceFilesViaGit = (rootDirectory: string): number | null => {
  const result = spawnSync("git", ["ls-files", "--cached", "--others", "--exclude-standard"], {
    cwd: rootDirectory,
    encoding: "utf-8",
    maxBuffer: GIT_LS_FILES_MAX_BUFFER_BYTES,
  });

  if (result.error || result.status !== 0) {
    return null;
  }

  return result.stdout
    .split("\n")
    .filter((filePath) => filePath.length > 0 && SOURCE_FILE_PATTERN.test(filePath)).length;
};

const countSourceFiles = (rootDirectory: string): number =>
  countSourceFilesViaGit(rootDirectory) ?? countSourceFilesViaFilesystem(rootDirectory);

const collectAllDependencies = (packageJson: PackageJson): Record<string, string> => ({
  ...packageJson.peerDependencies,
  ...packageJson.dependencies,
  ...packageJson.devDependencies,
});

const detectFramework = (dependencies: Record<string, string>): Framework => {
  for (const [packageName, frameworkName] of Object.entries(FRAMEWORK_PACKAGES)) {
    if (dependencies[packageName]) {
      return frameworkName;
    }
  }
  return "unknown";
};

const isCatalogReference = (version: string): boolean => version.startsWith("catalog:");

const resolveVersionFromCatalog = (
  catalog: Record<string, unknown>,
  packageName: string,
): string | null => {
  const version = catalog[packageName];
  if (typeof version === "string" && !isCatalogReference(version)) return version;
  return null;
};

const resolveCatalogVersion = (packageJson: PackageJson, packageName: string): string | null => {
  const raw = packageJson as Record<string, unknown>;

  if (isPlainObject(raw.catalog)) {
    const version = resolveVersionFromCatalog(raw.catalog, packageName);
    if (version) return version;
  }

  if (isPlainObject(raw.catalogs)) {
    for (const catalogEntries of Object.values(raw.catalogs)) {
      if (isPlainObject(catalogEntries)) {
        const version = resolveVersionFromCatalog(catalogEntries, packageName);
        if (version) return version;
      }
    }
  }

  return null;
};

const extractDependencyInfo = (packageJson: PackageJson): DependencyInfo => {
  const allDependencies = collectAllDependencies(packageJson);
  const rawVersion = allDependencies.react ?? null;
  const reactVersion = rawVersion && !isCatalogReference(rawVersion) ? rawVersion : null;
  return {
    reactVersion,
    framework: detectFramework(allDependencies),
  };
};

const parsePnpmWorkspacePatterns = (rootDirectory: string): string[] => {
  const workspacePath = path.join(rootDirectory, "pnpm-workspace.yaml");
  if (!isFile(workspacePath)) return [];

  const content = fs.readFileSync(workspacePath, "utf-8");
  const patterns: string[] = [];
  let isInsidePackagesBlock = false;

  for (const line of content.split("\n")) {
    const trimmed = line.trim();
    if (trimmed === "packages:") {
      isInsidePackagesBlock = true;
      continue;
    }
    if (isInsidePackagesBlock && trimmed.startsWith("-")) {
      patterns.push(trimmed.replace(/^-\s*/, "").replace(/["']/g, ""));
    } else if (isInsidePackagesBlock && trimmed.length > 0 && !trimmed.startsWith("#")) {
      isInsidePackagesBlock = false;
    }
  }

  return patterns;
};

const getWorkspacePatterns = (rootDirectory: string, packageJson: PackageJson): string[] => {
  const pnpmPatterns = parsePnpmWorkspacePatterns(rootDirectory);
  if (pnpmPatterns.length > 0) return pnpmPatterns;

  if (Array.isArray(packageJson.workspaces)) {
    return packageJson.workspaces;
  }

  if (packageJson.workspaces?.packages) {
    return packageJson.workspaces.packages;
  }

  return [];
};

const resolveWorkspaceDirectories = (rootDirectory: string, pattern: string): string[] => {
  const cleanPattern = pattern.replace(/["']/g, "").replace(/\/\*\*$/, "/*");

  if (!cleanPattern.includes("*")) {
    const directoryPath = path.join(rootDirectory, cleanPattern);
    if (fs.existsSync(directoryPath) && isFile(path.join(directoryPath, "package.json"))) {
      return [directoryPath];
    }
    return [];
  }

  const wildcardIndex = cleanPattern.indexOf("*");
  const baseDirectory = path.join(rootDirectory, cleanPattern.slice(0, wildcardIndex));
  const suffixAfterWildcard = cleanPattern.slice(wildcardIndex + 1);

  if (!fs.existsSync(baseDirectory) || !fs.statSync(baseDirectory).isDirectory()) {
    return [];
  }

  return fs
    .readdirSync(baseDirectory)
    .map((entry) => path.join(baseDirectory, entry, suffixAfterWildcard))
    .filter(
      (entryPath) =>
        fs.existsSync(entryPath) &&
        fs.statSync(entryPath).isDirectory() &&
        isFile(path.join(entryPath, "package.json")),
    );
};

const findDependencyInfoFromMonorepoRoot = (directory: string): DependencyInfo => {
  const monorepoRoot = findMonorepoRoot(directory);
  if (!monorepoRoot) return { reactVersion: null, framework: "unknown" };

  const monorepoPackageJsonPath = path.join(monorepoRoot, "package.json");
  if (!isFile(monorepoPackageJsonPath)) return { reactVersion: null, framework: "unknown" };

  const rootPackageJson = readPackageJson(monorepoPackageJsonPath);
  const rootInfo = extractDependencyInfo(rootPackageJson);
  const catalogVersion = resolveCatalogVersion(rootPackageJson, "react");
  const workspaceInfo = findReactInWorkspaces(monorepoRoot, rootPackageJson);

  return {
    reactVersion: rootInfo.reactVersion ?? catalogVersion ?? workspaceInfo.reactVersion,
    framework: rootInfo.framework !== "unknown" ? rootInfo.framework : workspaceInfo.framework,
  };
};

const findReactInWorkspaces = (rootDirectory: string, packageJson: PackageJson): DependencyInfo => {
  const patterns = getWorkspacePatterns(rootDirectory, packageJson);
  const result: DependencyInfo = { reactVersion: null, framework: "unknown" };

  for (const pattern of patterns) {
    const directories = resolveWorkspaceDirectories(rootDirectory, pattern);

    for (const workspaceDirectory of directories) {
      const workspacePackageJson = readPackageJson(path.join(workspaceDirectory, "package.json"));
      const info = extractDependencyInfo(workspacePackageJson);

      if (info.reactVersion && !result.reactVersion) {
        result.reactVersion = info.reactVersion;
      }
      if (info.framework !== "unknown" && result.framework === "unknown") {
        result.framework = info.framework;
      }

      if (result.reactVersion && result.framework !== "unknown") {
        return result;
      }
    }
  }

  return result;
};

const REACT_DEPENDENCY_NAMES = new Set(["react", "react-native", "next"]);

const hasReactDependency = (packageJson: PackageJson): boolean => {
  const allDependencies = collectAllDependencies(packageJson);
  return Object.keys(allDependencies).some((packageName) =>
    REACT_DEPENDENCY_NAMES.has(packageName),
  );
};

export const discoverReactSubprojects = (rootDirectory: string): WorkspacePackage[] => {
  if (!fs.existsSync(rootDirectory) || !fs.statSync(rootDirectory).isDirectory()) return [];

  const packages: WorkspacePackage[] = [];

  const rootPackageJsonPath = path.join(rootDirectory, "package.json");
  if (isFile(rootPackageJsonPath)) {
    const rootPackageJson = readPackageJson(rootPackageJsonPath);
    if (hasReactDependency(rootPackageJson)) {
      const name = rootPackageJson.name ?? path.basename(rootDirectory);
      packages.push({ name, directory: rootDirectory });
    }
  }

  const entries = fs.readdirSync(rootDirectory, { withFileTypes: true });

  for (const entry of entries) {
    if (!entry.isDirectory() || entry.name.startsWith(".") || entry.name === "node_modules") {
      continue;
    }

    const subdirectory = path.join(rootDirectory, entry.name);
    const packageJsonPath = path.join(subdirectory, "package.json");
    if (!isFile(packageJsonPath)) continue;

    const packageJson = readPackageJson(packageJsonPath);
    if (!hasReactDependency(packageJson)) continue;

    const name = packageJson.name ?? entry.name;
    packages.push({ name, directory: subdirectory });
  }

  return packages;
};

export const listWorkspacePackages = (rootDirectory: string): WorkspacePackage[] => {
  const packageJsonPath = path.join(rootDirectory, "package.json");
  if (!isFile(packageJsonPath)) return [];

  const packageJson = readPackageJson(packageJsonPath);
  const patterns = getWorkspacePatterns(rootDirectory, packageJson);
  if (patterns.length === 0) return [];

  const packages: WorkspacePackage[] = [];

  for (const pattern of patterns) {
    const directories = resolveWorkspaceDirectories(rootDirectory, pattern);
    for (const workspaceDirectory of directories) {
      const workspacePackageJson = readPackageJson(path.join(workspaceDirectory, "package.json"));

      if (!hasReactDependency(workspacePackageJson)) continue;

      const name = workspacePackageJson.name ?? path.basename(workspaceDirectory);
      packages.push({ name, directory: workspaceDirectory });
    }
  }

  return packages;
};

const hasCompilerPackage = (packageJson: PackageJson): boolean => {
  const allDependencies = collectAllDependencies(packageJson);
  return Object.keys(allDependencies).some((packageName) =>
    REACT_COMPILER_PACKAGES.has(packageName),
  );
};

const fileContainsPattern = (filePath: string, pattern: RegExp): boolean => {
  if (!isFile(filePath)) return false;
  const content = fs.readFileSync(filePath, "utf-8");
  return pattern.test(content);
};

const hasCompilerInConfigFiles = (directory: string, filenames: string[]): boolean =>
  filenames.some((filename) =>
    fileContainsPattern(path.join(directory, filename), REACT_COMPILER_CONFIG_PATTERN),
  );

const detectReactCompiler = (directory: string, packageJson: PackageJson): boolean => {
  if (hasCompilerPackage(packageJson)) return true;

  if (hasCompilerInConfigFiles(directory, NEXT_CONFIG_FILENAMES)) return true;
  if (hasCompilerInConfigFiles(directory, BABEL_CONFIG_FILENAMES)) return true;
  if (hasCompilerInConfigFiles(directory, VITE_CONFIG_FILENAMES)) return true;
  if (hasCompilerInConfigFiles(directory, EXPO_APP_CONFIG_FILENAMES)) return true;

  let ancestorDirectory = path.dirname(directory);
  while (ancestorDirectory !== path.dirname(ancestorDirectory)) {
    const ancestorPackagePath = path.join(ancestorDirectory, "package.json");
    if (isFile(ancestorPackagePath)) {
      const ancestorPackageJson = readPackageJson(ancestorPackagePath);
      if (hasCompilerPackage(ancestorPackageJson)) return true;
    }
    ancestorDirectory = path.dirname(ancestorDirectory);
  }

  return false;
};

export const discoverProject = (directory: string): ProjectInfo => {
  const packageJsonPath = path.join(directory, "package.json");
  if (!isFile(packageJsonPath)) {
    throw new Error(`No package.json found in ${directory}`);
  }

  const packageJson = readPackageJson(packageJsonPath);
  let { reactVersion, framework } = extractDependencyInfo(packageJson);

  if (!reactVersion) {
    reactVersion = resolveCatalogVersion(packageJson, "react");
  }

  if (!reactVersion || framework === "unknown") {
    const workspaceInfo = findReactInWorkspaces(directory, packageJson);
    if (!reactVersion && workspaceInfo.reactVersion) {
      reactVersion = workspaceInfo.reactVersion;
    }
    if (framework === "unknown" && workspaceInfo.framework !== "unknown") {
      framework = workspaceInfo.framework;
    }
  }

  if ((!reactVersion || framework === "unknown") && !isMonorepoRoot(directory)) {
    const monorepoInfo = findDependencyInfoFromMonorepoRoot(directory);
    if (!reactVersion) {
      reactVersion = monorepoInfo.reactVersion;
    }
    if (framework === "unknown") {
      framework = monorepoInfo.framework;
    }
  }

  const projectName = packageJson.name ?? path.basename(directory);
  const hasTypeScript = fs.existsSync(path.join(directory, "tsconfig.json"));
  const sourceFileCount = countSourceFiles(directory);

  const hasReactCompiler = detectReactCompiler(directory, packageJson);

  return {
    rootDirectory: directory,
    projectName,
    reactVersion,
    framework,
    hasTypeScript,
    hasReactCompiler,
    sourceFileCount,
  };
};
```

## File: `packages/react-doctor/src/utils/filter-diagnostics.ts`
```typescript
import fs from "node:fs";
import path from "node:path";
import type { Diagnostic, ReactDoctorConfig } from "../types.js";
import { compileIgnoredFilePatterns, isFileIgnoredByPatterns } from "./is-ignored-file.js";

export const filterIgnoredDiagnostics = (
  diagnostics: Diagnostic[],
  config: ReactDoctorConfig,
  rootDirectory: string,
): Diagnostic[] => {
  const ignoredRules = new Set(Array.isArray(config.ignore?.rules) ? config.ignore.rules : []);
  const ignoredFilePatterns = compileIgnoredFilePatterns(config);

  if (ignoredRules.size === 0 && ignoredFilePatterns.length === 0) {
    return diagnostics;
  }

  return diagnostics.filter((diagnostic) => {
    const ruleIdentifier = `${diagnostic.plugin}/${diagnostic.rule}`;
    if (ignoredRules.has(ruleIdentifier)) {
      return false;
    }

    if (isFileIgnoredByPatterns(diagnostic.filePath, rootDirectory, ignoredFilePatterns)) {
      return false;
    }

    return true;
  });
};

const DISABLE_NEXT_LINE_PATTERN = /\/\/\s*react-doctor-disable-next-line\b(?:\s+(.+))?/;
const DISABLE_LINE_PATTERN = /\/\/\s*react-doctor-disable-line\b(?:\s+(.+))?/;

const isRuleSuppressed = (commentRules: string | undefined, ruleId: string): boolean => {
  if (!commentRules?.trim()) return true;
  return commentRules.split(/[,\s]+/).some((rule) => rule.trim() === ruleId);
};

export const filterInlineSuppressions = (
  diagnostics: Diagnostic[],
  rootDirectory: string,
): Diagnostic[] => {
  const fileLineCache = new Map<string, string[] | null>();

  const getFileLines = (filePath: string): string[] | null => {
    const cached = fileLineCache.get(filePath);
    if (cached !== undefined) return cached;
    const absolutePath = path.isAbsolute(filePath) ? filePath : path.join(rootDirectory, filePath);
    try {
      const lines = fs.readFileSync(absolutePath, "utf-8").split("\n");
      fileLineCache.set(filePath, lines);
      return lines;
    } catch {
      fileLineCache.set(filePath, null);
      return null;
    }
  };

  return diagnostics.filter((diagnostic) => {
    if (diagnostic.line <= 0) return true;

    const lines = getFileLines(diagnostic.filePath);
    if (!lines) return true;

    const ruleId = `${diagnostic.plugin}/${diagnostic.rule}`;

    const currentLine = lines[diagnostic.line - 1];
    if (currentLine) {
      const lineMatch = currentLine.match(DISABLE_LINE_PATTERN);
      if (lineMatch && isRuleSuppressed(lineMatch[1], ruleId)) return false;
    }

    if (diagnostic.line >= 2) {
      const prevLine = lines[diagnostic.line - 2];
      if (prevLine) {
        const nextLineMatch = prevLine.match(DISABLE_NEXT_LINE_PATTERN);
        if (nextLineMatch && isRuleSuppressed(nextLineMatch[1], ruleId)) return false;
      }
    }

    return true;
  });
};
```

## File: `packages/react-doctor/src/utils/find-monorepo-root.ts`
```typescript
import path from "node:path";
import { isFile } from "./is-file.js";
import { readPackageJson } from "./read-package-json.js";

export const isMonorepoRoot = (directory: string): boolean => {
  if (isFile(path.join(directory, "pnpm-workspace.yaml"))) return true;
  if (isFile(path.join(directory, "nx.json"))) return true;
  const packageJsonPath = path.join(directory, "package.json");
  if (!isFile(packageJsonPath)) return false;
  const packageJson = readPackageJson(packageJsonPath);
  return Array.isArray(packageJson.workspaces) || Boolean(packageJson.workspaces?.packages);
};

export const findMonorepoRoot = (startDirectory: string): string | null => {
  let currentDirectory = path.dirname(startDirectory);

  while (currentDirectory !== path.dirname(currentDirectory)) {
    if (isMonorepoRoot(currentDirectory)) return currentDirectory;
    currentDirectory = path.dirname(currentDirectory);
  }

  return null;
};
```

## File: `packages/react-doctor/src/utils/framed-box.ts`
```typescript
import {
  SUMMARY_BOX_HORIZONTAL_PADDING_CHARS,
  SUMMARY_BOX_OUTER_INDENT_CHARS,
} from "../constants.js";
import { highlighter } from "./highlighter.js";
import { logger } from "./logger.js";

export interface FramedLine {
  plainText: string;
  renderedText: string;
}

export const createFramedLine = (
  plainText: string,
  renderedText: string = plainText,
): FramedLine => ({
  plainText,
  renderedText,
});

export const renderFramedBoxString = (framedLines: FramedLine[]): string => {
  if (framedLines.length === 0) return "";

  const borderColorizer = highlighter.dim;
  const outerIndent = " ".repeat(SUMMARY_BOX_OUTER_INDENT_CHARS);
  const horizontalPadding = " ".repeat(SUMMARY_BOX_HORIZONTAL_PADDING_CHARS);
  const maximumLineLength = Math.max(
    ...framedLines.map((framedLine) => framedLine.plainText.length),
  );
  const borderLine = "─".repeat(maximumLineLength + SUMMARY_BOX_HORIZONTAL_PADDING_CHARS * 2);

  const lines: string[] = [];
  lines.push(`${outerIndent}${borderColorizer(`┌${borderLine}┐`)}`);

  for (const framedLine of framedLines) {
    const trailingSpaces = " ".repeat(maximumLineLength - framedLine.plainText.length);
    lines.push(
      `${outerIndent}${borderColorizer("│")}${horizontalPadding}${framedLine.renderedText}${trailingSpaces}${horizontalPadding}${borderColorizer("│")}`,
    );
  }

  lines.push(`${outerIndent}${borderColorizer(`└${borderLine}┘`)}`);
  return lines.join("\n");
};

export const printFramedBox = (framedLines: FramedLine[]): void => {
  const rendered = renderFramedBoxString(framedLines);
  if (rendered) {
    logger.log(rendered);
  }
};
```

## File: `packages/react-doctor/src/utils/get-diff-files.ts`
```typescript
import { execSync } from "node:child_process";
import { DEFAULT_BRANCH_CANDIDATES, SOURCE_FILE_PATTERN } from "../constants.js";
import type { DiffInfo } from "../types.js";

const getCurrentBranch = (directory: string): string | null => {
  try {
    const branch = execSync("git rev-parse --abbrev-ref HEAD", {
      cwd: directory,
      stdio: "pipe",
    })
      .toString()
      .trim();
    return branch === "HEAD" ? null : branch;
  } catch {
    return null;
  }
};

const detectDefaultBranch = (directory: string): string | null => {
  try {
    const reference = execSync("git symbolic-ref refs/remotes/origin/HEAD", {
      cwd: directory,
      stdio: "pipe",
    })
      .toString()
      .trim();
    return reference.replace("refs/remotes/origin/", "");
  } catch {
    for (const candidate of DEFAULT_BRANCH_CANDIDATES) {
      try {
        execSync(`git rev-parse --verify ${candidate}`, {
          cwd: directory,
          stdio: "pipe",
        });
        return candidate;
      } catch {}
    }
    return null;
  }
};

const getChangedFilesSinceBranch = (directory: string, baseBranch: string): string[] => {
  try {
    const mergeBase = execSync(`git merge-base ${baseBranch} HEAD`, {
      cwd: directory,
      stdio: "pipe",
    })
      .toString()
      .trim();

    const output = execSync(`git diff --name-only --diff-filter=ACMR --relative ${mergeBase}`, {
      cwd: directory,
      stdio: "pipe",
    })
      .toString()
      .trim();

    if (!output) return [];
    return output.split("\n").filter(Boolean);
  } catch {
    return [];
  }
};

const getUncommittedChangedFiles = (directory: string): string[] => {
  try {
    const output = execSync("git diff --name-only --diff-filter=ACMR --relative HEAD", {
      cwd: directory,
      stdio: "pipe",
    })
      .toString()
      .trim();
    if (!output) return [];
    return output.split("\n").filter(Boolean);
  } catch {
    return [];
  }
};

export const getDiffInfo = (directory: string, explicitBaseBranch?: string): DiffInfo | null => {
  const currentBranch = getCurrentBranch(directory);
  if (!currentBranch) return null;

  const baseBranch = explicitBaseBranch ?? detectDefaultBranch(directory);
  if (!baseBranch) return null;

  if (currentBranch === baseBranch) {
    const uncommittedFiles = getUncommittedChangedFiles(directory);
    if (uncommittedFiles.length === 0) return null;
    return { currentBranch, baseBranch, changedFiles: uncommittedFiles, isCurrentChanges: true };
  }

  const changedFiles = getChangedFilesSinceBranch(directory, baseBranch);
  return { currentBranch, baseBranch, changedFiles };
};

export const filterSourceFiles = (filePaths: string[]): string[] =>
  filePaths.filter((filePath) => SOURCE_FILE_PATTERN.test(filePath));
```

## File: `packages/react-doctor/src/utils/group-by.ts`
```typescript
export const groupBy = <T>(items: T[], keyFn: (item: T) => string): Map<string, T[]> => {
  const groups = new Map<string, T[]>();

  for (const item of items) {
    const key = keyFn(item);
    const existing = groups.get(key) ?? [];
    existing.push(item);
    groups.set(key, existing);
  }

  return groups;
};
```

## File: `packages/react-doctor/src/utils/handle-error.ts`
```typescript
import { logger } from "./logger.js";
import type { HandleErrorOptions } from "../types.js";

const DEFAULT_HANDLE_ERROR_OPTIONS: HandleErrorOptions = {
  shouldExit: true,
};

export const handleError = (
  error: unknown,
  options: HandleErrorOptions = DEFAULT_HANDLE_ERROR_OPTIONS,
): void => {
  logger.break();
  logger.error("Something went wrong. Please check the error below for more details.");
  logger.error("If the problem persists, please open an issue on GitHub.");
  logger.error("");
  if (error instanceof Error) {
    logger.error(error.message);
  }
  logger.break();
  if (options.shouldExit) {
    process.exit(1);
  }
  process.exitCode = 1;
};
```

## File: `packages/react-doctor/src/utils/highlighter.ts`
```typescript
import pc from "picocolors";

export const highlighter = {
  error: pc.red,
  warn: pc.yellow,
  info: pc.cyan,
  success: pc.green,
  dim: pc.dim,
};
```

## File: `packages/react-doctor/src/utils/indent-multiline-text.ts`
```typescript
export const indentMultilineText = (text: string, linePrefix: string): string =>
  text
    .split("\n")
    .map((lineText) => `${linePrefix}${lineText}`)
    .join("\n");
```

## File: `packages/react-doctor/src/utils/is-file.ts`
```typescript
import fs from "node:fs";

export const isFile = (filePath: string): boolean => {
  try {
    return fs.statSync(filePath).isFile();
  } catch {
    return false;
  }
};
```

## File: `packages/react-doctor/src/utils/is-ignored-file.ts`
```typescript
import type { ReactDoctorConfig } from "../types.js";
import { compileGlobPattern } from "./match-glob-pattern.js";

const toRelativePath = (filePath: string, rootDirectory: string): string => {
  const normalizedFilePath = filePath.replace(/\\/g, "/");
  const normalizedRoot = rootDirectory.replace(/\\/g, "/").replace(/\/$/, "") + "/";

  if (normalizedFilePath.startsWith(normalizedRoot)) {
    return normalizedFilePath.slice(normalizedRoot.length);
  }

  return normalizedFilePath.replace(/^\.\//, "");
};

export const compileIgnoredFilePatterns = (userConfig: ReactDoctorConfig | null): RegExp[] =>
  Array.isArray(userConfig?.ignore?.files) ? userConfig.ignore.files.map(compileGlobPattern) : [];

export const isFileIgnoredByPatterns = (
  filePath: string,
  rootDirectory: string,
  patterns: RegExp[],
): boolean => {
  if (patterns.length === 0) {
    return false;
  }

  const relativePath = toRelativePath(filePath, rootDirectory);
  return patterns.some((pattern) => pattern.test(relativePath));
};
```

## File: `packages/react-doctor/src/utils/is-plain-object.ts`
```typescript
export const isPlainObject = (value: unknown): value is Record<string, unknown> =>
  typeof value === "object" && value !== null && !Array.isArray(value);
```

## File: `packages/react-doctor/src/utils/load-config.ts`
```typescript
import fs from "node:fs";
import path from "node:path";
import type { ReactDoctorConfig } from "../types.js";
import { isFile } from "./is-file.js";
import { isPlainObject } from "./is-plain-object.js";

const CONFIG_FILENAME = "react-doctor.config.json";
const PACKAGE_JSON_CONFIG_KEY = "reactDoctor";

export const loadConfig = (rootDirectory: string): ReactDoctorConfig | null => {
  const configFilePath = path.join(rootDirectory, CONFIG_FILENAME);

  if (isFile(configFilePath)) {
    try {
      const fileContent = fs.readFileSync(configFilePath, "utf-8");
      const parsed: unknown = JSON.parse(fileContent);
      if (isPlainObject(parsed)) {
        return parsed as ReactDoctorConfig;
      }
      console.warn(`Warning: ${CONFIG_FILENAME} must be a JSON object, ignoring.`);
    } catch (error) {
      console.warn(
        `Warning: Failed to parse ${CONFIG_FILENAME}: ${error instanceof Error ? error.message : String(error)}`,
      );
    }
  }

  const packageJsonPath = path.join(rootDirectory, "package.json");
  if (isFile(packageJsonPath)) {
    try {
      const fileContent = fs.readFileSync(packageJsonPath, "utf-8");
      const packageJson = JSON.parse(fileContent);
      const embeddedConfig = packageJson[PACKAGE_JSON_CONFIG_KEY];
      if (isPlainObject(embeddedConfig)) {
        return embeddedConfig as ReactDoctorConfig;
      }
    } catch {
      return null;
    }
  }

  return null;
};
```

## File: `packages/react-doctor/src/utils/logger.ts`
```typescript
import { highlighter } from "./highlighter.js";

export const logger = {
  error(...args: unknown[]) {
    console.log(highlighter.error(args.join(" ")));
  },
  warn(...args: unknown[]) {
    console.log(highlighter.warn(args.join(" ")));
  },
  info(...args: unknown[]) {
    console.log(highlighter.info(args.join(" ")));
  },
  success(...args: unknown[]) {
    console.log(highlighter.success(args.join(" ")));
  },
  dim(...args: unknown[]) {
    console.log(highlighter.dim(args.join(" ")));
  },
  log(...args: unknown[]) {
    console.log(args.join(" "));
  },
  break() {
    console.log("");
  },
};
```

## File: `packages/react-doctor/src/utils/match-glob-pattern.ts`
```typescript
const REGEX_SPECIAL_CHARACTERS = /[.+^${}()|[\]\\]/g;

export const compileGlobPattern = (pattern: string): RegExp => {
  const normalizedPattern = pattern.replace(/\\/g, "/").replace(/^\//, "");

  let regexSource = "^";
  let characterIndex = 0;

  while (characterIndex < normalizedPattern.length) {
    if (
      normalizedPattern[characterIndex] === "*" &&
      normalizedPattern[characterIndex + 1] === "*"
    ) {
      if (normalizedPattern[characterIndex + 2] === "/") {
        regexSource += "(?:.+/)?";
        characterIndex += 3;
      } else {
        regexSource += ".*";
        characterIndex += 2;
      }
    } else if (normalizedPattern[characterIndex] === "*") {
      regexSource += "[^/]*";
      characterIndex++;
    } else if (normalizedPattern[characterIndex] === "?") {
      regexSource += "[^/]";
      characterIndex++;
    } else {
      regexSource += normalizedPattern[characterIndex].replace(REGEX_SPECIAL_CHARACTERS, "\\$&");
      characterIndex++;
    }
  }

  regexSource += "$";
  return new RegExp(regexSource);
};

export const matchGlobPattern = (filePath: string, pattern: string): boolean => {
  const normalizedPath = filePath.replace(/\\/g, "/");
  return compileGlobPattern(pattern).test(normalizedPath);
};
```

## File: `packages/react-doctor/src/utils/neutralize-disable-directives.ts`
```typescript
import { spawnSync } from "node:child_process";
import fs from "node:fs";
import path from "node:path";
import { GIT_LS_FILES_MAX_BUFFER_BYTES, SOURCE_FILE_PATTERN } from "../constants.js";

const findFilesWithDisableDirectives = (
  rootDirectory: string,
  includePaths?: string[],
): string[] => {
  const grepArgs = ["grep", "-l", "--untracked", "-E", "(eslint|oxlint)-disable"];
  if (includePaths && includePaths.length > 0) {
    grepArgs.push("--", ...includePaths);
  }

  const result = spawnSync("git", grepArgs, {
    cwd: rootDirectory,
    encoding: "utf-8",
    maxBuffer: GIT_LS_FILES_MAX_BUFFER_BYTES,
  });

  if (result.error || result.status === null) return [];
  if (result.status !== 0 && result.stdout.trim().length === 0) return [];

  return result.stdout
    .split("\n")
    .filter((filePath) => filePath.length > 0 && SOURCE_FILE_PATTERN.test(filePath));
};

const neutralizeContent = (content: string): string =>
  content
    .replaceAll("eslint-disable", "eslint_disable")
    .replaceAll("oxlint-disable", "oxlint_disable");

export const neutralizeDisableDirectives = (
  rootDirectory: string,
  includePaths?: string[],
): (() => void) => {
  const filePaths = findFilesWithDisableDirectives(rootDirectory, includePaths);
  const originalContents = new Map<string, string>();

  for (const relativePath of filePaths) {
    const absolutePath = path.join(rootDirectory, relativePath);

    let originalContent: string;
    try {
      originalContent = fs.readFileSync(absolutePath, "utf-8");
    } catch {
      continue;
    }

    const neutralizedContent = neutralizeContent(originalContent);
    if (neutralizedContent !== originalContent) {
      originalContents.set(absolutePath, originalContent);
      fs.writeFileSync(absolutePath, neutralizedContent);
    }
  }

  return () => {
    for (const [absolutePath, originalContent] of originalContents) {
      fs.writeFileSync(absolutePath, originalContent);
    }
  };
};
```

## File: `packages/react-doctor/src/utils/prompts.ts`
```typescript
import { createRequire } from "node:module";
import basePrompts, { type PromptObject, type Answers } from "prompts";
import type { PromptMultiselectContext } from "../types.js";
import { logger } from "./logger.js";
import { shouldAutoSelectCurrentChoice } from "./should-auto-select-current-choice.js";
import { shouldSelectAllChoices } from "./should-select-all-choices.js";

const require = createRequire(import.meta.url);
const PROMPTS_MULTISELECT_MODULE_PATH = "prompts/lib/elements/multiselect";
const PROMPTS_SELECT_MODULE_PATH = "prompts/lib/elements/select";
let didPatchMultiselectToggleAll = false;
let didPatchMultiselectSubmit = false;
let didPatchSelectBanner = false;

const selectBannerMap = new Map<number, string>();

export const setSelectBanner = (banner: string, targetIndex: number): void => {
  selectBannerMap.set(targetIndex, banner);
};

export const clearSelectBanner = (): void => {
  selectBannerMap.clear();
};

const onCancel = () => {
  logger.break();
  logger.log("Cancelled.");
  logger.dim("Run `npx react-doctor@latest --fix` to fix issues.");
  logger.break();
  process.exit(0);
};

const patchMultiselectToggleAll = (): void => {
  if (didPatchMultiselectToggleAll) return;
  didPatchMultiselectToggleAll = true;

  const multiselectPromptConstructor = require(PROMPTS_MULTISELECT_MODULE_PATH);

  multiselectPromptConstructor.prototype.toggleAll = function (
    this: PromptMultiselectContext,
  ): void {
    const isCurrentChoiceDisabled = Boolean(this.value[this.cursor]?.disabled);
    if (this.maxChoices !== undefined || isCurrentChoiceDisabled) {
      this.bell();
      return;
    }

    const shouldSelectAllEnabledChoices = shouldSelectAllChoices(this.value);

    for (const choiceState of this.value) {
      if (choiceState.disabled) continue;
      choiceState.selected = shouldSelectAllEnabledChoices;
    }

    this.render();
  };
};

const patchMultiselectSubmit = (): void => {
  if (didPatchMultiselectSubmit) return;
  didPatchMultiselectSubmit = true;

  const multiselectPromptConstructor = require(PROMPTS_MULTISELECT_MODULE_PATH);
  const originalSubmit = multiselectPromptConstructor.prototype.submit;

  multiselectPromptConstructor.prototype.submit = function (this: PromptMultiselectContext): void {
    if (shouldAutoSelectCurrentChoice(this.value, this.cursor)) {
      this.value[this.cursor].selected = true;
    }
    originalSubmit.call(this);
  };
};

interface SelectPromptInstance {
  closed: boolean;
  done: boolean;
  cursor: number;
  outputText: string;
  out: { write: (data: string) => boolean; columns: number };
  render: () => void;
}

const patchSelectBanner = (): void => {
  if (didPatchSelectBanner) return;
  didPatchSelectBanner = true;

  const selectConstructor = require(PROMPTS_SELECT_MODULE_PATH);
  const promptsClear = require("prompts/lib/util/clear");
  const originalRender = selectConstructor.prototype.render;

  selectConstructor.prototype.render = function (this: SelectPromptInstance): void {
    originalRender.call(this);

    const banner = selectBannerMap.get(this.cursor);
    if (!banner || this.closed || this.done) {
      return;
    }

    this.out.write(promptsClear(this.outputText, this.out.columns));
    this.outputText = `${banner}\n\n${this.outputText}`;
    this.out.write(this.outputText);
  };
};

export const prompts = <T extends string = string>(
  questions: PromptObject<T> | PromptObject<T>[],
): Promise<Answers<T>> => {
  patchMultiselectToggleAll();
  patchMultiselectSubmit();
  patchSelectBanner();
  return basePrompts(questions, { onCancel });
};
```

## File: `packages/react-doctor/src/utils/proxy-fetch.ts`
```typescript
import { execSync } from "node:child_process";
import { FETCH_TIMEOUT_MS } from "../constants.js";

const readNpmConfigValue = (key: string): string | undefined => {
  try {
    const value = execSync(`npm config get ${key}`, {
      encoding: "utf-8",
      stdio: ["pipe", "pipe", "ignore"],
    }).trim();
    if (value && value !== "null" && value !== "undefined") return value;
  } catch {}
  return undefined;
};

const resolveProxyUrl = (): string | undefined =>
  process.env.HTTPS_PROXY ??
  process.env.https_proxy ??
  process.env.HTTP_PROXY ??
  process.env.http_proxy ??
  readNpmConfigValue("https-proxy") ??
  readNpmConfigValue("proxy");

let isProxyUrlResolved = false;
let resolvedProxyUrl: string | undefined;

const getProxyUrl = (): string | undefined => {
  if (isProxyUrlResolved) return resolvedProxyUrl;
  isProxyUrlResolved = true;
  resolvedProxyUrl = resolveProxyUrl();
  return resolvedProxyUrl;
};

const createProxyDispatcher = async (proxyUrl: string): Promise<object | null> => {
  try {
    // @ts-expect-error undici is bundled with Node.js 18+ but lacks standalone type declarations
    const { ProxyAgent } = await import("undici");
    return new ProxyAgent(proxyUrl);
  } catch {
    return null;
  }
};

// HACK: Node.js's global fetch (undici) accepts `dispatcher` for proxy routing,
// which isn't part of the standard RequestInit type.
export const proxyFetch = async (url: string | URL, init?: RequestInit): Promise<Response> => {
  const controller = new AbortController();
  const timeoutId = setTimeout(() => controller.abort(), FETCH_TIMEOUT_MS);

  try {
    const proxyUrl = getProxyUrl();
    const dispatcher = proxyUrl ? await createProxyDispatcher(proxyUrl) : null;

    return await fetch(url, {
      ...init,
      signal: controller.signal,
      ...(dispatcher ? { dispatcher } : {}),
    } as RequestInit);
  } finally {
    clearTimeout(timeoutId);
  }
};
```

## File: `packages/react-doctor/src/utils/read-package-json.ts`
```typescript
import fs from "node:fs";
import type { PackageJson } from "../types.js";

export const readPackageJson = (packageJsonPath: string): PackageJson => {
  try {
    return JSON.parse(fs.readFileSync(packageJsonPath, "utf-8"));
  } catch (error) {
    if (error instanceof Error && "code" in error) {
      const { code } = error as { code: string };
      if (code === "EISDIR" || code === "EACCES") {
        return {};
      }
    }
    throw error;
  }
};
```

## File: `packages/react-doctor/src/utils/resolve-compatible-node.ts`
```typescript
import { execSync } from "node:child_process";
import { existsSync, readdirSync } from "node:fs";
import os from "node:os";
import path from "node:path";
import { OXLINT_RECOMMENDED_NODE_MAJOR } from "../constants.js";

interface NodeVersion {
  major: number;
  minor: number;
  patch: number;
}

interface NodeResolution {
  binaryPath: string;
  isCurrentNode: boolean;
  version: string;
}

const parseNodeVersion = (versionString: string): NodeVersion => {
  const cleaned = versionString.replace(/^v/, "").trim();
  const [major = 0, minor = 0, patch = 0] = cleaned.split(".").map(Number);
  return { major, minor, patch };
};

const isNodeVersionCompatibleWithOxlint = ({ major, minor }: NodeVersion): boolean => {
  if (major === 20 && minor >= 19) return true;
  if (major === 22 && minor >= 12) return true;
  if (major > 22) return true;
  return false;
};

const isCurrentNodeCompatibleWithOxlint = (): boolean =>
  isNodeVersionCompatibleWithOxlint(parseNodeVersion(process.version));

const getNvmDirectory = (): string | null => {
  const envNvmDirectory = process.env.NVM_DIR;
  if (envNvmDirectory && existsSync(envNvmDirectory)) return envNvmDirectory;

  const defaultNvmDirectory = path.join(os.homedir(), ".nvm");
  if (existsSync(defaultNvmDirectory)) return defaultNvmDirectory;

  return null;
};

export const isNvmInstalled = (): boolean => getNvmDirectory() !== null;

const findCompatibleNvmBinary = (): string | null => {
  const nvmDirectory = getNvmDirectory();
  if (!nvmDirectory) return null;

  const versionsDirectory = path.join(nvmDirectory, "versions", "node");
  if (!existsSync(versionsDirectory)) return null;

  const compatibleVersions = readdirSync(versionsDirectory)
    .filter((directoryName) => directoryName.startsWith("v"))
    .map((directoryName) => ({ directoryName, ...parseNodeVersion(directoryName) }))
    .filter((version) => isNodeVersionCompatibleWithOxlint(version))
    .sort(
      (versionA, versionB) =>
        versionB.major - versionA.major ||
        versionB.minor - versionA.minor ||
        versionB.patch - versionA.patch,
    );

  if (compatibleVersions.length === 0) return null;

  const bestVersion = compatibleVersions[0];
  const binaryPath = path.join(versionsDirectory, bestVersion.directoryName, "bin", "node");
  return existsSync(binaryPath) ? binaryPath : null;
};

const getNodeVersionFromBinary = (binaryPath: string): string | null => {
  try {
    return execSync(`"${binaryPath}" --version`, { encoding: "utf-8" }).trim();
  } catch {
    return null;
  }
};

export const installNodeViaNvm = (): boolean => {
  const nvmDirectory = getNvmDirectory();
  if (!nvmDirectory) return false;

  const nvmScript = path.join(nvmDirectory, "nvm.sh");
  if (!existsSync(nvmScript)) return false;

  try {
    execSync(`bash -c ". '${nvmScript}' && nvm install ${OXLINT_RECOMMENDED_NODE_MAJOR}"`, {
      stdio: "inherit",
    });
    return findCompatibleNvmBinary() !== null;
  } catch {
    return false;
  }
};

export const resolveNodeForOxlint = (): NodeResolution | null => {
  if (isCurrentNodeCompatibleWithOxlint()) {
    return {
      binaryPath: process.execPath,
      isCurrentNode: true,
      version: process.version,
    };
  }

  const nvmBinaryPath = findCompatibleNvmBinary();
  if (!nvmBinaryPath) return null;

  const version = getNodeVersionFromBinary(nvmBinaryPath);
  if (!version) return null;

  return { binaryPath: nvmBinaryPath, isCurrentNode: false, version };
};
```

## File: `packages/react-doctor/src/utils/resolve-lint-include-paths.ts`
```typescript
import { spawnSync } from "node:child_process";
import fs from "node:fs";
import path from "node:path";
import {
  GIT_LS_FILES_MAX_BUFFER_BYTES,
  IGNORED_DIRECTORIES,
  JSX_FILE_PATTERN,
  SOURCE_FILE_PATTERN,
} from "../constants.js";
import type { ReactDoctorConfig } from "../types.js";
import { compileIgnoredFilePatterns, isFileIgnoredByPatterns } from "./is-ignored-file.js";

const listSourceFilesViaGit = (rootDirectory: string): string[] | null => {
  const result = spawnSync("git", ["ls-files", "--cached", "--others", "--exclude-standard"], {
    cwd: rootDirectory,
    encoding: "utf-8",
    maxBuffer: GIT_LS_FILES_MAX_BUFFER_BYTES,
  });

  if (result.error || result.status !== 0) {
    return null;
  }

  return result.stdout
    .split("\n")
    .filter((filePath) => filePath.length > 0 && SOURCE_FILE_PATTERN.test(filePath));
};

const listSourceFilesViaFilesystem = (rootDirectory: string): string[] => {
  const filePaths: string[] = [];
  const stack = [rootDirectory];

  while (stack.length > 0) {
    const currentDirectory = stack.pop()!;
    const entries = fs.readdirSync(currentDirectory, { withFileTypes: true });

    for (const entry of entries) {
      const absolutePath = path.join(currentDirectory, entry.name);

      if (entry.isDirectory()) {
        if (!entry.name.startsWith(".") && !IGNORED_DIRECTORIES.has(entry.name)) {
          stack.push(absolutePath);
        }
        continue;
      }

      if (entry.isFile() && SOURCE_FILE_PATTERN.test(entry.name)) {
        filePaths.push(path.relative(rootDirectory, absolutePath).replace(/\\/g, "/"));
      }
    }
  }

  return filePaths;
};

const listSourceFiles = (rootDirectory: string): string[] =>
  listSourceFilesViaGit(rootDirectory) ?? listSourceFilesViaFilesystem(rootDirectory);

export const resolveLintIncludePaths = (
  rootDirectory: string,
  userConfig: ReactDoctorConfig | null,
): string[] | undefined => {
  if (!Array.isArray(userConfig?.ignore?.files) || userConfig.ignore.files.length === 0) {
    return undefined;
  }

  const ignoredPatterns = compileIgnoredFilePatterns(userConfig);

  const includedPaths = listSourceFiles(rootDirectory).filter((filePath) => {
    if (!JSX_FILE_PATTERN.test(filePath)) {
      return false;
    }

    return !isFileIgnoredByPatterns(filePath, rootDirectory, ignoredPatterns);
  });

  return includedPaths;
};
```

## File: `packages/react-doctor/src/utils/run-knip.ts`
```typescript
import fs from "node:fs";
import path from "node:path";
import { main } from "knip";
import { createOptions } from "knip/session";
import { MAX_KNIP_RETRIES } from "../constants.js";
import type { Diagnostic, KnipIssueRecords, KnipResults } from "../types.js";
import { findMonorepoRoot } from "./find-monorepo-root.js";
import { isFile } from "./is-file.js";

const KNIP_CATEGORY_MAP: Record<string, string> = {
  files: "Dead Code",
  exports: "Dead Code",
  types: "Dead Code",
  duplicates: "Dead Code",
};

const KNIP_MESSAGE_MAP: Record<string, string> = {
  files: "Unused file",
  exports: "Unused export",
  types: "Unused type",
  duplicates: "Duplicate export",
};

const KNIP_SEVERITY_MAP: Record<string, "error" | "warning"> = {
  files: "warning",
  exports: "warning",
  types: "warning",
  duplicates: "warning",
};

const collectIssueRecords = (
  records: KnipIssueRecords,
  issueType: string,
  rootDirectory: string,
): Diagnostic[] => {
  const diagnostics: Diagnostic[] = [];

  for (const issues of Object.values(records)) {
    for (const issue of Object.values(issues)) {
      diagnostics.push({
        filePath: path.relative(rootDirectory, issue.filePath),
        plugin: "knip",
        rule: issueType,
        severity: KNIP_SEVERITY_MAP[issueType] ?? "warning",
        message: `${KNIP_MESSAGE_MAP[issueType]}: ${issue.symbol}`,
        help: "",
        line: 0,
        column: 0,
        category: KNIP_CATEGORY_MAP[issueType] ?? "Dead Code",
        weight: 1,
      });
    }
  }

  return diagnostics;
};

// HACK: knip triggers dotenv which logs to stdout/stderr via console methods
const silenced = async <T>(fn: () => Promise<T>): Promise<T> => {
  const originalLog = console.log;
  const originalInfo = console.info;
  const originalWarn = console.warn;
  const originalError = console.error;
  console.log = () => {};
  console.info = () => {};
  console.warn = () => {};
  console.error = () => {};
  try {
    return await fn();
  } finally {
    console.log = originalLog;
    console.info = originalInfo;
    console.warn = originalWarn;
    console.error = originalError;
  }
};

const CONFIG_LOADING_ERROR_PATTERN = /Error loading .*\/([a-z-]+)\.config\./;

const extractFailedPluginName = (error: unknown): string | null => {
  const match = String(error).match(CONFIG_LOADING_ERROR_PATTERN);
  return match?.[1] ?? null;
};

const TSCONFIG_FILENAMES = ["tsconfig.base.json", "tsconfig.json"];

const resolveTsConfigFile = (directory: string): string | undefined =>
  TSCONFIG_FILENAMES.find((filename) => fs.existsSync(path.join(directory, filename)));

const runKnipWithOptions = async (
  knipCwd: string,
  workspaceName?: string,
): Promise<KnipResults> => {
  const tsConfigFile = resolveTsConfigFile(knipCwd);
  const options = await silenced(() =>
    createOptions({
      cwd: knipCwd,
      isShowProgress: false,
      ...(workspaceName ? { workspace: workspaceName } : {}),
      ...(tsConfigFile ? { tsConfigFile } : {}),
    }),
  );

  const parsedConfig = options.parsedConfig as Record<string, unknown>;

  for (let attempt = 0; attempt <= MAX_KNIP_RETRIES; attempt++) {
    try {
      return (await silenced(() => main(options))) as KnipResults;
    } catch (error) {
      const failedPlugin = extractFailedPluginName(error);
      if (!failedPlugin || attempt === MAX_KNIP_RETRIES) {
        throw error;
      }
      parsedConfig[failedPlugin] = false;
    }
  }

  throw new Error("Unreachable");
};

const hasNodeModules = (directory: string): boolean => {
  const nodeModulesPath = path.join(directory, "node_modules");
  return fs.existsSync(nodeModulesPath) && fs.statSync(nodeModulesPath).isDirectory();
};

export const runKnip = async (rootDirectory: string): Promise<Diagnostic[]> => {
  const monorepoRoot = findMonorepoRoot(rootDirectory);
  const hasInstalledDependencies =
    hasNodeModules(rootDirectory) || (monorepoRoot !== null && hasNodeModules(monorepoRoot));

  if (!hasInstalledDependencies) {
    return [];
  }

  let knipResult: KnipResults;

  if (monorepoRoot) {
    const packageJsonPath = path.join(rootDirectory, "package.json");
    const packageJson = isFile(packageJsonPath)
      ? JSON.parse(fs.readFileSync(packageJsonPath, "utf-8"))
      : {};
    const workspaceName = packageJson.name ?? path.basename(rootDirectory);

    try {
      knipResult = await runKnipWithOptions(monorepoRoot, workspaceName);
    } catch {
      knipResult = await runKnipWithOptions(rootDirectory);
    }
  } else {
    knipResult = await runKnipWithOptions(rootDirectory);
  }

  const { issues } = knipResult;
  const diagnostics: Diagnostic[] = [];

  for (const unusedFile of issues.files) {
    diagnostics.push({
      filePath: path.relative(rootDirectory, unusedFile),
      plugin: "knip",
      rule: "files",
      severity: KNIP_SEVERITY_MAP["files"],
      message: KNIP_MESSAGE_MAP["files"],
      help: "This file is not imported by any other file in the project.",
      line: 0,
      column: 0,
      category: KNIP_CATEGORY_MAP["files"],
      weight: 1,
    });
  }

  const recordTypes = ["exports", "types", "duplicates"] as const;

  for (const issueType of recordTypes) {
    diagnostics.push(...collectIssueRecords(issues[issueType], issueType, rootDirectory));
  }

  return diagnostics;
};
```

## File: `packages/react-doctor/src/utils/run-oxlint.ts`
```typescript
import { spawn } from "node:child_process";
import fs from "node:fs";
import { createRequire } from "node:module";
import os from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";
import {
  ERROR_PREVIEW_LENGTH_CHARS,
  JSX_FILE_PATTERN,
  SPAWN_ARGS_MAX_LENGTH_CHARS,
} from "../constants.js";
import { createOxlintConfig } from "../oxlint-config.js";
import type { CleanedDiagnostic, Diagnostic, Framework, OxlintOutput } from "../types.js";
import { neutralizeDisableDirectives } from "./neutralize-disable-directives.js";

const esmRequire = createRequire(import.meta.url);

const PLUGIN_CATEGORY_MAP: Record<string, string> = {
  react: "Correctness",
  "react-hooks": "Correctness",
  "react-hooks-js": "React Compiler",
  "react-perf": "Performance",
  "jsx-a11y": "Accessibility",
};

const RULE_CATEGORY_MAP: Record<string, string> = {
  "react-doctor/no-derived-state-effect": "State & Effects",
  "react-doctor/no-fetch-in-effect": "State & Effects",
  "react-doctor/no-cascading-set-state": "State & Effects",
  "react-doctor/no-effect-event-handler": "State & Effects",
  "react-doctor/no-derived-useState": "State & Effects",
  "react-doctor/prefer-useReducer": "State & Effects",
  "react-doctor/rerender-lazy-state-init": "Performance",
  "react-doctor/rerender-functional-setstate": "Performance",
  "react-doctor/rerender-dependencies": "State & Effects",

  "react-doctor/no-generic-handler-names": "Architecture",
  "react-doctor/no-giant-component": "Architecture",
  "react-doctor/no-render-in-render": "Architecture",
  "react-doctor/no-nested-component-definition": "Correctness",

  "react-doctor/no-usememo-simple-expression": "Performance",
  "react-doctor/no-layout-property-animation": "Performance",
  "react-doctor/rerender-memo-with-default-value": "Performance",
  "react-doctor/rendering-animate-svg-wrapper": "Performance",
  "react-doctor/rendering-usetransition-loading": "Performance",
  "react-doctor/rendering-hydration-no-flicker": "Performance",

  "react-doctor/no-transition-all": "Performance",
  "react-doctor/no-global-css-variable-animation": "Performance",
  "react-doctor/no-large-animated-blur": "Performance",
  "react-doctor/no-scale-from-zero": "Performance",
  "react-doctor/no-permanent-will-change": "Performance",

  "react-doctor/no-secrets-in-client-code": "Security",

  "react-doctor/no-barrel-import": "Bundle Size",
  "react-doctor/no-full-lodash-import": "Bundle Size",
  "react-doctor/no-moment": "Bundle Size",
  "react-doctor/prefer-dynamic-import": "Bundle Size",
  "react-doctor/use-lazy-motion": "Bundle Size",
  "react-doctor/no-undeferred-third-party": "Bundle Size",

  "react-doctor/no-array-index-as-key": "Correctness",
  "react-doctor/rendering-conditional-render": "Correctness",
  "react-doctor/no-prevent-default": "Correctness",
  "react-doctor/nextjs-no-img-element": "Next.js",
  "react-doctor/nextjs-async-client-component": "Next.js",
  "react-doctor/nextjs-no-a-element": "Next.js",
  "react-doctor/nextjs-no-use-search-params-without-suspense": "Next.js",
  "react-doctor/nextjs-no-client-fetch-for-server-data": "Next.js",
  "react-doctor/nextjs-missing-metadata": "Next.js",
  "react-doctor/nextjs-no-client-side-redirect": "Next.js",
  "react-doctor/nextjs-no-redirect-in-try-catch": "Next.js",
  "react-doctor/nextjs-image-missing-sizes": "Next.js",
  "react-doctor/nextjs-no-native-script": "Next.js",
  "react-doctor/nextjs-inline-script-missing-id": "Next.js",
  "react-doctor/nextjs-no-font-link": "Next.js",
  "react-doctor/nextjs-no-css-link": "Next.js",
  "react-doctor/nextjs-no-polyfill-script": "Next.js",
  "react-doctor/nextjs-no-head-import": "Next.js",
  "react-doctor/nextjs-no-side-effect-in-get-handler": "Security",

  "react-doctor/server-auth-actions": "Server",
  "react-doctor/server-after-nonblocking": "Server",

  "react-doctor/client-passive-event-listeners": "Performance",

  "react-doctor/async-parallel": "Performance",

  "react-doctor/rn-no-raw-text": "React Native",
  "react-doctor/rn-no-deprecated-modules": "React Native",
  "react-doctor/rn-no-legacy-expo-packages": "React Native",
  "react-doctor/rn-no-dimensions-get": "React Native",
  "react-doctor/rn-no-inline-flatlist-renderitem": "React Native",
  "react-doctor/rn-no-legacy-shadow-styles": "React Native",
  "react-doctor/rn-prefer-reanimated": "React Native",
  "react-doctor/rn-no-single-element-style-array": "React Native",
};

const RULE_HELP_MAP: Record<string, string> = {
  "no-derived-state-effect":
    "For derived state, compute inline: `const x = fn(dep)`. For state resets on prop change, use a key prop: `<Component key={prop} />`. See https://react.dev/learn/you-might-not-need-an-effect",
  "no-fetch-in-effect":
    "Use `useQuery()` from @tanstack/react-query, `useSWR()`, or fetch in a Server Component instead",
  "no-cascading-set-state":
    "Combine into useReducer: `const [state, dispatch] = useReducer(reducer, initialState)`",
  "no-effect-event-handler":
    "Move the conditional logic into onClick, onChange, or onSubmit handlers directly",
  "no-derived-useState":
    "Remove useState and compute the value inline: `const value = transform(propName)`",
  "prefer-useReducer":
    "Group related state: `const [state, dispatch] = useReducer(reducer, { field1, field2, ... })`",
  "rerender-lazy-state-init":
    "Wrap in an arrow function so it only runs once: `useState(() => expensiveComputation())`",
  "rerender-functional-setstate":
    "Use the callback form: `setState(prev => prev + 1)` to always read the latest value",
  "rerender-dependencies":
    "Extract to a useMemo, useRef, or module-level constant so the reference is stable",

  "no-generic-handler-names":
    "Rename to describe the action: e.g. `handleSubmit` → `saveUserProfile`, `handleClick` → `toggleSidebar`",
  "no-giant-component":
    "Extract logical sections into focused components: `<UserHeader />`, `<UserActions />`, etc.",
  "no-render-in-render":
    "Extract to a named component: `const ListItem = ({ item }) => <div>{item.name}</div>`",
  "no-nested-component-definition":
    "Move to a separate file or to module scope above the parent component",

  "no-usememo-simple-expression":
    "Remove useMemo — property access, math, and ternaries are already cheap without memoization",
  "no-layout-property-animation":
    "Use `transform: translateX()` or `scale()` instead — they run on the compositor and skip layout/paint",
  "rerender-memo-with-default-value":
    "Move to module scope: `const EMPTY_ITEMS: Item[] = []` then use as the default value",
  "rendering-animate-svg-wrapper":
    "Wrap the SVG: `<motion.div animate={...}><svg>...</svg></motion.div>`",
  "rendering-usetransition-loading":
    "Replace with `const [isPending, startTransition] = useTransition()` — avoids a re-render for the loading state",
  "rendering-hydration-no-flicker":
    "Use `useSyncExternalStore(subscribe, getSnapshot, getServerSnapshot)` or add `suppressHydrationWarning` to the element",

  "no-transition-all":
    'List specific properties: `transition: "opacity 200ms, transform 200ms"` — or in Tailwind use `transition-colors`, `transition-opacity`, or `transition-transform`',
  "no-global-css-variable-animation":
    "Set the variable on the nearest element instead of a parent, or use `@property` with `inherits: false` to prevent cascade. Better yet, use targeted `element.style.transform` updates",
  "no-large-animated-blur":
    "Keep blur radius under 10px, or apply blur to a smaller element. Large blurs multiply GPU memory usage with layer size",
  "no-scale-from-zero":
    "Use `initial={{ scale: 0.95, opacity: 0 }}` — elements should deflate like a balloon, not vanish into a point",
  "no-permanent-will-change":
    "Add will-change on animation start (`onMouseEnter`) and remove on end (`onAnimationEnd`). Permanent promotion wastes GPU memory and can degrade performance",

  "no-secrets-in-client-code":
    "Move to server-side `process.env.SECRET_NAME`. Only `NEXT_PUBLIC_*` vars are safe for the client (and should not contain secrets)",

  "no-barrel-import":
    "Import from the direct path: `import { Button } from './components/Button'` instead of `./components`",
  "no-full-lodash-import":
    "Import the specific function: `import debounce from 'lodash/debounce'` — saves ~70kb",
  "no-moment":
    "Replace with `import { format } from 'date-fns'` (tree-shakeable) or `import dayjs from 'dayjs'` (2kb)",
  "prefer-dynamic-import":
    "Use `const Component = dynamic(() => import('library'), { ssr: false })` from next/dynamic or React.lazy()",
  "use-lazy-motion":
    'Use `import { LazyMotion, m } from "framer-motion"` with `domAnimation` features — saves ~30kb',
  "no-undeferred-third-party":
    'Use `next/script` with `strategy="lazyOnload"` or add the `defer` attribute',

  "no-array-index-as-key":
    "Use a stable unique identifier: `key={item.id}` or `key={item.slug}` — index keys break on reorder/filter",
  "rendering-conditional-render":
    "Change to `{items.length > 0 && <List />}` or use a ternary: `{items.length ? <List /> : null}`",
  "no-prevent-default":
    "Use `<form action={serverAction}>` (works without JS) or `<button>` instead of `<a>` with preventDefault",

  "nextjs-no-img-element":
    "`import Image from 'next/image'` — provides automatic WebP/AVIF, lazy loading, and responsive srcset",
  "nextjs-async-client-component":
    "Fetch data in a parent Server Component and pass it as props, or use useQuery/useSWR in the client component",
  "nextjs-no-a-element":
    "`import Link from 'next/link'` — enables client-side navigation, prefetching, and preserves scroll position",
  "nextjs-no-use-search-params-without-suspense":
    "Wrap the component using useSearchParams: `<Suspense fallback={<Skeleton />}><SearchComponent /></Suspense>`",
  "nextjs-no-client-fetch-for-server-data":
    "Remove 'use client' and fetch directly in the Server Component — no API round-trip, secrets stay on server",
  "nextjs-missing-metadata":
    "Add `export const metadata = { title: '...', description: '...' }` or `export async function generateMetadata()`",
  "nextjs-no-client-side-redirect":
    "Use `redirect('/path')` from 'next/navigation' directly (works in both server and client components), or handle in middleware",
  "nextjs-no-redirect-in-try-catch":
    "Move the redirect/notFound call outside the try block, or add `unstable_rethrow(error)` in the catch",
  "nextjs-image-missing-sizes":
    'Add sizes for responsive behavior: `sizes="(max-width: 768px) 100vw, 50vw"` matching your layout breakpoints',
  "nextjs-no-native-script":
    '`import Script from "next/script"` — use `strategy="afterInteractive"` for analytics or `"lazyOnload"` for widgets',
  "nextjs-inline-script-missing-id":
    'Add `id="descriptive-name"` so Next.js can track, deduplicate, and re-execute the script correctly',
  "nextjs-no-font-link":
    '`import { Inter } from "next/font/google"` — self-hosted, zero layout shift, no render-blocking requests',
  "nextjs-no-css-link":
    "Import CSS directly: `import './styles.css'` or use CSS Modules: `import styles from './Button.module.css'`",
  "nextjs-no-polyfill-script":
    "Next.js includes polyfills for fetch, Promise, Object.assign, Array.from, and 50+ others automatically",
  "nextjs-no-head-import":
    "Use the Metadata API instead: `export const metadata = { title: '...' }` or `export async function generateMetadata()`",
  "nextjs-no-side-effect-in-get-handler":
    "Move the side effect to a POST handler and use a <form> or fetch with method POST — GET requests can be triggered by prefetching and are vulnerable to CSRF",

  "server-auth-actions":
    "Add `const session = await auth()` at the top and throw/redirect if unauthorized before any data access",
  "server-after-nonblocking":
    "`import { after } from 'next/server'` then wrap: `after(() => analytics.track(...))` — response isn't blocked",

  "client-passive-event-listeners":
    "Add `{ passive: true }` as the third argument: `addEventListener('scroll', handler, { passive: true })`",

  "async-parallel":
    "Use `const [a, b] = await Promise.all([fetchA(), fetchB()])` to run independent operations concurrently",

  "rn-no-raw-text":
    "Wrap text in a `<Text>` component: `<Text>{value}</Text>` — raw strings outside `<Text>` crash on React Native",
  "rn-no-deprecated-modules":
    "Import from the community package instead — deprecated modules were removed from the react-native core",
  "rn-no-legacy-expo-packages":
    "Migrate to the recommended replacement package — legacy Expo packages are no longer maintained",
  "rn-no-dimensions-get":
    "Use `const { width, height } = useWindowDimensions()` — it updates reactively on rotation and resize",
  "rn-no-inline-flatlist-renderitem":
    "Extract renderItem to a named function or wrap in useCallback to avoid re-creating on every render",
  "rn-no-legacy-shadow-styles":
    "Use `boxShadow` for cross-platform shadows on the new architecture instead of platform-specific shadow properties",
  "rn-prefer-reanimated":
    "Use `import Animated from 'react-native-reanimated'` — animations run on the UI thread instead of the JS thread",
  "rn-no-single-element-style-array":
    "Use `style={value}` instead of `style={[value]}` — single-element arrays add unnecessary allocation",
};

const FILEPATH_WITH_LOCATION_PATTERN = /\S+\.\w+:\d+:\d+[\s\S]*$/;

const REACT_COMPILER_MESSAGE = "React Compiler can't optimize this code";

const cleanDiagnosticMessage = (
  message: string,
  help: string,
  plugin: string,
  rule: string,
): CleanedDiagnostic => {
  if (plugin === "react-hooks-js") {
    const rawMessage = message.replace(FILEPATH_WITH_LOCATION_PATTERN, "").trim();
    return { message: REACT_COMPILER_MESSAGE, help: rawMessage || help };
  }
  const cleaned = message.replace(FILEPATH_WITH_LOCATION_PATTERN, "").trim();
  return { message: cleaned || message, help: help || RULE_HELP_MAP[rule] || "" };
};

const parseRuleCode = (code: string): { plugin: string; rule: string } => {
  const match = code.match(/^(.+)\((.+)\)$/);
  if (!match) return { plugin: "unknown", rule: code };
  return { plugin: match[1].replace(/^eslint-plugin-/, ""), rule: match[2] };
};

const resolveOxlintBinary = (): string => {
  const oxlintMainPath = esmRequire.resolve("oxlint");
  const oxlintPackageDirectory = path.resolve(path.dirname(oxlintMainPath), "..");
  return path.join(oxlintPackageDirectory, "bin", "oxlint");
};

const resolvePluginPath = (): string => {
  const currentDirectory = path.dirname(fileURLToPath(import.meta.url));
  const pluginPath = path.join(currentDirectory, "react-doctor-plugin.js");
  if (fs.existsSync(pluginPath)) return pluginPath;

  const distPluginPath = path.resolve(currentDirectory, "../../dist/react-doctor-plugin.js");
  if (fs.existsSync(distPluginPath)) return distPluginPath;

  return pluginPath;
};

const resolveDiagnosticCategory = (plugin: string, rule: string): string => {
  const ruleKey = `${plugin}/${rule}`;
  return RULE_CATEGORY_MAP[ruleKey] ?? PLUGIN_CATEGORY_MAP[plugin] ?? "Other";
};

const estimateArgsLength = (args: string[]): number =>
  args.reduce((total, argument) => total + argument.length + 1, 0);

const batchIncludePaths = (baseArgs: string[], includePaths: string[]): string[][] => {
  const baseArgsLength = estimateArgsLength(baseArgs);
  const batches: string[][] = [];
  let currentBatch: string[] = [];
  let currentBatchLength = baseArgsLength;

  for (const filePath of includePaths) {
    const entryLength = filePath.length + 1;
    if (currentBatch.length > 0 && currentBatchLength + entryLength > SPAWN_ARGS_MAX_LENGTH_CHARS) {
      batches.push(currentBatch);
      currentBatch = [];
      currentBatchLength = baseArgsLength;
    }
    currentBatch.push(filePath);
    currentBatchLength += entryLength;
  }

  if (currentBatch.length > 0) {
    batches.push(currentBatch);
  }

  return batches;
};

const spawnOxlint = (
  args: string[],
  rootDirectory: string,
  nodeBinaryPath: string,
): Promise<string> =>
  new Promise<string>((resolve, reject) => {
    const child = spawn(nodeBinaryPath, args, {
      cwd: rootDirectory,
    });

    const stdoutBuffers: Buffer[] = [];
    const stderrBuffers: Buffer[] = [];

    child.stdout.on("data", (buffer: Buffer) => stdoutBuffers.push(buffer));
    child.stderr.on("data", (buffer: Buffer) => stderrBuffers.push(buffer));

    child.on("error", (error) => reject(new Error(`Failed to run oxlint: ${error.message}`)));
    child.on("close", (code, signal) => {
      if (signal) {
        const stderrOutput = Buffer.concat(stderrBuffers).toString("utf-8").trim();
        const hint =
          signal === "SIGABRT" ? " (out of memory — try scanning fewer files with --diff)" : "";
        const detail = stderrOutput ? `: ${stderrOutput}` : "";
        reject(new Error(`oxlint was killed by ${signal}${hint}${detail}`));
        return;
      }
      const output = Buffer.concat(stdoutBuffers).toString("utf-8").trim();
      if (!output) {
        const stderrOutput = Buffer.concat(stderrBuffers).toString("utf-8").trim();
        if (stderrOutput) {
          reject(new Error(`Failed to run oxlint: ${stderrOutput}`));
          return;
        }
      }
      resolve(output);
    });
  });

const parseOxlintOutput = (stdout: string): Diagnostic[] => {
  if (!stdout) return [];

  let output: OxlintOutput;
  try {
    output = JSON.parse(stdout) as OxlintOutput;
  } catch {
    throw new Error(
      `Failed to parse oxlint output: ${stdout.slice(0, ERROR_PREVIEW_LENGTH_CHARS)}`,
    );
  }

  return output.diagnostics
    .filter((diagnostic) => diagnostic.code && JSX_FILE_PATTERN.test(diagnostic.filename))
    .map((diagnostic) => {
      const { plugin, rule } = parseRuleCode(diagnostic.code);
      const primaryLabel = diagnostic.labels[0];

      const cleaned = cleanDiagnosticMessage(diagnostic.message, diagnostic.help, plugin, rule);

      return {
        filePath: diagnostic.filename,
        plugin,
        rule,
        severity: diagnostic.severity,
        message: cleaned.message,
        help: cleaned.help,
        line: primaryLabel?.span.line ?? 0,
        column: primaryLabel?.span.column ?? 0,
        category: resolveDiagnosticCategory(plugin, rule),
      };
    });
};

export const runOxlint = async (
  rootDirectory: string,
  hasTypeScript: boolean,
  framework: Framework,
  hasReactCompiler: boolean,
  includePaths?: string[],
  nodeBinaryPath: string = process.execPath,
): Promise<Diagnostic[]> => {
  if (includePaths !== undefined && includePaths.length === 0) {
    return [];
  }

  const configPath = path.join(os.tmpdir(), `react-doctor-oxlintrc-${process.pid}.json`);
  const pluginPath = resolvePluginPath();
  const config = createOxlintConfig({ pluginPath, framework, hasReactCompiler });
  const restoreDisableDirectives = neutralizeDisableDirectives(rootDirectory, includePaths);

  try {
    fs.writeFileSync(configPath, JSON.stringify(config, null, 2));

    const oxlintBinary = resolveOxlintBinary();
    const baseArgs = [oxlintBinary, "-c", configPath, "--format", "json"];

    if (hasTypeScript) {
      baseArgs.push("--tsconfig", "./tsconfig.json");
    }

    const fileBatches =
      includePaths !== undefined ? batchIncludePaths(baseArgs, includePaths) : [["."]];

    const allDiagnostics: Diagnostic[] = [];
    for (const batch of fileBatches) {
      const batchArgs = [...baseArgs, ...batch];
      const stdout = await spawnOxlint(batchArgs, rootDirectory, nodeBinaryPath);
      allDiagnostics.push(...parseOxlintOutput(stdout));
    }

    return allDiagnostics;
  } finally {
    restoreDisableDirectives();
    if (fs.existsSync(configPath)) {
      fs.unlinkSync(configPath);
    }
  }
};
```

## File: `packages/react-doctor/src/utils/select-projects.ts`
```typescript
import path from "node:path";
import type { WorkspacePackage } from "../types.js";
import { discoverReactSubprojects, listWorkspacePackages } from "./discover-project.js";
import { highlighter } from "./highlighter.js";
import { logger } from "./logger.js";
import { prompts } from "./prompts.js";

export const selectProjects = async (
  rootDirectory: string,
  projectFlag: string | undefined,
  skipPrompts: boolean,
): Promise<string[]> => {
  let packages = listWorkspacePackages(rootDirectory);
  if (packages.length === 0) {
    packages = discoverReactSubprojects(rootDirectory);
  }

  if (packages.length === 0) return [rootDirectory];
  if (packages.length === 1) {
    logger.log(
      `${highlighter.success("✔")} Select projects to scan ${highlighter.dim("›")} ${packages[0].name}`,
    );
    return [packages[0].directory];
  }

  if (projectFlag) return resolveProjectFlag(projectFlag, packages);

  if (skipPrompts) {
    printDiscoveredProjects(packages);
    return packages.map((workspacePackage) => workspacePackage.directory);
  }

  return promptProjectSelection(packages, rootDirectory);
};

const resolveProjectFlag = (
  projectFlag: string,
  workspacePackages: WorkspacePackage[],
): string[] => {
  const requestedNames = projectFlag.split(",").map((name) => name.trim());
  const resolvedDirectories: string[] = [];

  for (const requestedName of requestedNames) {
    const matched = workspacePackages.find(
      (workspacePackage) =>
        workspacePackage.name === requestedName ||
        path.basename(workspacePackage.directory) === requestedName,
    );

    if (!matched) {
      const availableNames = workspacePackages
        .map((workspacePackage) => workspacePackage.name)
        .join(", ");
      throw new Error(`Project "${requestedName}" not found. Available: ${availableNames}`);
    }

    resolvedDirectories.push(matched.directory);
  }

  return resolvedDirectories;
};

const printDiscoveredProjects = (packages: WorkspacePackage[]): void => {
  logger.log(
    `${highlighter.success("✔")} Select projects to scan ${highlighter.dim("›")} ${packages.map((workspacePackage) => workspacePackage.name).join(", ")}`,
  );
};

const promptProjectSelection = async (
  workspacePackages: WorkspacePackage[],
  rootDirectory: string,
): Promise<string[]> => {
  const { selectedDirectories } = await prompts({
    type: "multiselect",
    name: "selectedDirectories",
    message: "Select projects to scan",
    choices: workspacePackages.map((workspacePackage) => ({
      title: workspacePackage.name,
      description: path.relative(rootDirectory, workspacePackage.directory),
      value: workspacePackage.directory,
    })),
    min: 1,
  });

  return selectedDirectories;
};
```

## File: `packages/react-doctor/src/utils/should-auto-select-current-choice.ts`
```typescript
import type { PromptMultiselectChoiceState } from "../types.js";

export const shouldAutoSelectCurrentChoice = (
  choiceStates: PromptMultiselectChoiceState[],
  cursor: number,
): boolean => {
  const hasSelection = choiceStates.some((choiceState) => choiceState.selected);
  if (hasSelection) return false;

  const currentChoice = choiceStates[cursor];
  return Boolean(currentChoice) && !currentChoice.disabled;
};
```

## File: `packages/react-doctor/src/utils/should-select-all-choices.ts`
```typescript
import type { PromptMultiselectChoiceState } from "../types.js";

export const shouldSelectAllChoices = (choiceStates: PromptMultiselectChoiceState[]): boolean => {
  const enabledChoiceStates = choiceStates.filter((choiceState) => !choiceState.disabled);
  return enabledChoiceStates.some((choiceState) => choiceState.selected !== true);
};
```

## File: `packages/react-doctor/src/utils/skill-prompt.ts`
```typescript
import { execSync } from "node:child_process";
import { appendFileSync, existsSync, mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { homedir } from "node:os";
import { join } from "node:path";
import { highlighter } from "./highlighter.js";
import { logger } from "./logger.js";
import { prompts } from "./prompts.js";

const HOME_DIRECTORY = homedir();
const CONFIG_DIRECTORY = join(HOME_DIRECTORY, ".react-doctor");
const CONFIG_FILE = join(CONFIG_DIRECTORY, "config.json");

const SKILL_NAME = "react-doctor";
const WINDSURF_MARKER = "# React Doctor";

const SKILL_DESCRIPTION =
  "Run after making React changes to catch issues early. Use when reviewing code, finishing a feature, or fixing bugs in a React project.";

const SKILL_BODY = `Scans your React codebase for security, performance, correctness, and architecture issues. Outputs a 0-100 score with actionable diagnostics.

## Usage

\`\`\`bash
npx -y react-doctor@latest . --verbose --diff
\`\`\`

## Workflow

Run after making changes to catch issues early. Fix errors first, then re-run to verify the score improved.`;

const SKILL_CONTENT = `---
name: ${SKILL_NAME}
description: ${SKILL_DESCRIPTION}
version: 1.0.0
---

# React Doctor

${SKILL_BODY}
`;

const AGENTS_CONTENT = `# React Doctor

${SKILL_DESCRIPTION}

${SKILL_BODY}
`;

const CODEX_AGENT_CONFIG = `interface:
  display_name: "${SKILL_NAME}"
  short_description: "Diagnose and fix React codebase health issues"
`;

interface SkillPromptConfig {
  skillPromptDismissed?: boolean;
}

interface SkillTarget {
  name: string;
  detect: () => boolean;
  install: () => void;
}

const readSkillPromptConfig = (): SkillPromptConfig => {
  try {
    if (!existsSync(CONFIG_FILE)) return {};
    return JSON.parse(readFileSync(CONFIG_FILE, "utf-8"));
  } catch {
    return {};
  }
};

const writeSkillPromptConfig = (config: SkillPromptConfig): void => {
  try {
    mkdirSync(CONFIG_DIRECTORY, { recursive: true });
    writeFileSync(CONFIG_FILE, JSON.stringify(config, null, 2));
  } catch {}
};

const writeSkillFiles = (directory: string): void => {
  mkdirSync(directory, { recursive: true });
  writeFileSync(join(directory, "SKILL.md"), SKILL_CONTENT);
  writeFileSync(join(directory, "AGENTS.md"), AGENTS_CONTENT);
};

const isCommandAvailable = (command: string): boolean => {
  try {
    const whichCommand = process.platform === "win32" ? "where" : "which";
    execSync(`${whichCommand} ${command}`, { stdio: "ignore" });
    return true;
  } catch {
    return false;
  }
};

const SKILL_TARGETS: SkillTarget[] = [
  {
    name: "Claude Code",
    detect: () => existsSync(join(HOME_DIRECTORY, ".claude")),
    install: () => writeSkillFiles(join(HOME_DIRECTORY, ".claude", "skills", SKILL_NAME)),
  },
  {
    name: "Amp Code",
    detect: () => existsSync(join(HOME_DIRECTORY, ".amp")),
    install: () => writeSkillFiles(join(HOME_DIRECTORY, ".config", "amp", "skills", SKILL_NAME)),
  },
  {
    name: "Cursor",
    detect: () => existsSync(join(HOME_DIRECTORY, ".cursor")),
    install: () => writeSkillFiles(join(HOME_DIRECTORY, ".cursor", "skills", SKILL_NAME)),
  },
  {
    name: "OpenCode",
    detect: () =>
      isCommandAvailable("opencode") || existsSync(join(HOME_DIRECTORY, ".config", "opencode")),
    install: () =>
      writeSkillFiles(join(HOME_DIRECTORY, ".config", "opencode", "skills", SKILL_NAME)),
  },
  {
    name: "Windsurf",
    detect: () =>
      existsSync(join(HOME_DIRECTORY, ".codeium")) ||
      existsSync(join(HOME_DIRECTORY, "Library", "Application Support", "Windsurf")),
    install: () => {
      const memoriesDirectory = join(HOME_DIRECTORY, ".codeium", "windsurf", "memories");
      mkdirSync(memoriesDirectory, { recursive: true });
      const rulesFile = join(memoriesDirectory, "global_rules.md");

      if (existsSync(rulesFile)) {
        const existingContent = readFileSync(rulesFile, "utf-8");
        if (existingContent.includes(WINDSURF_MARKER)) return;
        appendFileSync(rulesFile, `\n${WINDSURF_MARKER}\n\n${SKILL_CONTENT}`);
      } else {
        writeFileSync(rulesFile, `${WINDSURF_MARKER}\n\n${SKILL_CONTENT}`);
      }
    },
  },
  {
    name: "Antigravity",
    detect: () =>
      isCommandAvailable("agy") || existsSync(join(HOME_DIRECTORY, ".gemini", "antigravity")),
    install: () =>
      writeSkillFiles(join(HOME_DIRECTORY, ".gemini", "antigravity", "skills", SKILL_NAME)),
  },
  {
    name: "Gemini CLI",
    detect: () => isCommandAvailable("gemini") || existsSync(join(HOME_DIRECTORY, ".gemini")),
    install: () => writeSkillFiles(join(HOME_DIRECTORY, ".gemini", "skills", SKILL_NAME)),
  },
  {
    name: "Codex",
    detect: () => isCommandAvailable("codex") || existsSync(join(HOME_DIRECTORY, ".codex")),
    install: () => {
      const skillDirectory = join(HOME_DIRECTORY, ".codex", "skills", SKILL_NAME);
      writeSkillFiles(skillDirectory);
      const agentsDirectory = join(skillDirectory, "agents");
      mkdirSync(agentsDirectory, { recursive: true });
      writeFileSync(join(agentsDirectory, "openai.yaml"), CODEX_AGENT_CONFIG);
    },
  },
];

const installSkill = (): void => {
  let installedCount = 0;

  for (const target of SKILL_TARGETS) {
    if (!target.detect()) continue;
    try {
      target.install();
      logger.log(`  ${highlighter.success("✔")} ${target.name}`);
      installedCount++;
    } catch {
      logger.dim(`  ✗ ${target.name} (failed)`);
    }
  }

  try {
    const projectSkillDirectory = join(".agents", SKILL_NAME);
    writeSkillFiles(projectSkillDirectory);
    logger.log(`  ${highlighter.success("✔")} .agents/`);
    installedCount++;
  } catch {
    logger.dim("  ✗ .agents/ (failed)");
  }

  logger.break();
  if (installedCount === 0) {
    logger.dim("No supported tools detected.");
  } else {
    logger.success("Done! The skill will activate when working on React projects.");
  }
};

export const maybePromptSkillInstall = async (shouldSkipPrompts: boolean): Promise<void> => {
  const config = readSkillPromptConfig();
  if (config.skillPromptDismissed) return;
  if (shouldSkipPrompts) return;

  logger.break();
  logger.log(`${highlighter.info("💡")} Have your coding agent fix these issues automatically?`);
  logger.dim(
    `   Install the ${highlighter.info("react-doctor")} skill to teach Cursor, Claude Code,`,
  );
  logger.dim("   Ami, and other AI agents how to diagnose and fix React issues.");
  logger.break();

  const { shouldInstall } = await prompts({
    type: "confirm",
    name: "shouldInstall",
    message: "Install skill? (recommended)",
    initial: true,
  });

  if (shouldInstall) {
    logger.break();
    installSkill();
  }

  writeSkillPromptConfig({ ...config, skillPromptDismissed: true });
};
```

## File: `packages/react-doctor/src/utils/spinner.ts`
```typescript
import ora from "ora";

let sharedInstance: ReturnType<typeof ora> | null = null;
let activeCount = 0;
const pendingTexts = new Set<string>();

const finalize = (method: "succeed" | "fail", originalText: string, displayText: string) => {
  pendingTexts.delete(originalText);
  activeCount--;

  if (activeCount <= 0 || !sharedInstance) {
    sharedInstance?.[method](displayText);
    sharedInstance = null;
    activeCount = 0;
    return;
  }

  sharedInstance.stop();
  ora(displayText).start()[method](displayText);

  const [remainingText] = pendingTexts;
  if (remainingText) {
    sharedInstance.text = remainingText;
  }
  sharedInstance.start();
};

export const spinner = (text: string) => ({
  start() {
    activeCount++;
    pendingTexts.add(text);

    if (!sharedInstance) {
      sharedInstance = ora({ text }).start();
    } else {
      sharedInstance.text = text;
    }

    return {
      succeed: (displayText: string) => finalize("succeed", text, displayText),
      fail: (displayText: string) => finalize("fail", text, displayText),
    };
  },
});
```

## File: `packages/react-doctor/tests/colorize-by-score.test.ts`
```typescript
import { describe, expect, it } from "vitest";
import { colorizeByScore } from "../src/utils/colorize-by-score.js";

describe("colorizeByScore", () => {
  it("returns a string for high scores", () => {
    const result = colorizeByScore("Great", 90);
    expect(typeof result).toBe("string");
    expect(result).toContain("Great");
  });

  it("returns a string for medium scores", () => {
    const result = colorizeByScore("OK", 60);
    expect(typeof result).toBe("string");
    expect(result).toContain("OK");
  });

  it("returns a string for low scores", () => {
    const result = colorizeByScore("Critical", 30);
    expect(typeof result).toBe("string");
    expect(result).toContain("Critical");
  });

  it("does not throw at good threshold boundary (75)", () => {
    expect(() => colorizeByScore("text", 75)).not.toThrow();
    expect(() => colorizeByScore("text", 74)).not.toThrow();
    expect(colorizeByScore("text", 75)).toContain("text");
    expect(colorizeByScore("text", 74)).toContain("text");
  });

  it("does not throw at ok threshold boundary (50)", () => {
    expect(() => colorizeByScore("text", 50)).not.toThrow();
    expect(() => colorizeByScore("text", 49)).not.toThrow();
    expect(colorizeByScore("text", 50)).toContain("text");
    expect(colorizeByScore("text", 49)).toContain("text");
  });

  it("handles score of zero", () => {
    const result = colorizeByScore("zero", 0);
    expect(result).toContain("zero");
  });

  it("handles perfect score", () => {
    const result = colorizeByScore("perfect", 100);
    expect(result).toContain("perfect");
  });
});
```

## File: `packages/react-doctor/tests/combine-diagnostics.test.ts`
```typescript
import { describe, expect, it } from "vitest";
import type { Diagnostic, ReactDoctorConfig } from "../src/types.js";
import { combineDiagnostics, computeJsxIncludePaths } from "../src/utils/combine-diagnostics.js";

const createDiagnostic = (overrides: Partial<Diagnostic> = {}): Diagnostic => ({
  filePath: "src/app.tsx",
  plugin: "react-doctor",
  rule: "test-rule",
  severity: "warning",
  message: "test message",
  help: "test help",
  line: 1,
  column: 1,
  category: "Test",
  ...overrides,
});

describe("computeJsxIncludePaths", () => {
  it("returns undefined for empty include paths", () => {
    expect(computeJsxIncludePaths([])).toBeUndefined();
  });

  it("filters to only JSX/TSX files", () => {
    const paths = ["src/app.tsx", "src/utils.ts", "src/Button.jsx", "src/config.js"];
    const result = computeJsxIncludePaths(paths);
    expect(result).toEqual(["src/app.tsx", "src/Button.jsx"]);
  });

  it("returns empty array when no JSX/TSX files exist", () => {
    const paths = ["src/utils.ts", "src/config.js"];
    const result = computeJsxIncludePaths(paths);
    expect(result).toEqual([]);
  });
});

describe("combineDiagnostics", () => {
  it("merges lint and dead code diagnostics", () => {
    const lintDiagnostics = [createDiagnostic({ rule: "lint-rule" })];
    const deadCodeDiagnostics = [createDiagnostic({ rule: "dead-code-rule" })];

    const result = combineDiagnostics(lintDiagnostics, deadCodeDiagnostics, "/tmp", true, null);
    expect(result).toHaveLength(2);
    expect(result[0].rule).toBe("lint-rule");
    expect(result[1].rule).toBe("dead-code-rule");
  });

  it("returns empty array when both inputs are empty in diff mode", () => {
    const result = combineDiagnostics([], [], "/tmp", true, null);
    expect(result).toEqual([]);
  });

  it("applies config filtering when userConfig is provided", () => {
    const diagnostics = [
      createDiagnostic({ plugin: "react", rule: "no-danger" }),
      createDiagnostic({ plugin: "react-doctor", rule: "no-giant-component" }),
    ];
    const config: ReactDoctorConfig = {
      ignore: { rules: ["react/no-danger"] },
    };

    const result = combineDiagnostics(diagnostics, [], "/tmp", true, config);
    expect(result).toHaveLength(1);
    expect(result[0].rule).toBe("no-giant-component");
  });

  it("skips config filtering when userConfig is null", () => {
    const diagnostics = [createDiagnostic(), createDiagnostic()];
    const result = combineDiagnostics(diagnostics, [], "/tmp", true, null);
    expect(result).toHaveLength(2);
  });
});
```

## File: `packages/react-doctor/tests/discover-project.test.ts`
```typescript
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { afterAll, describe, expect, it } from "vitest";
import {
  discoverProject,
  discoverReactSubprojects,
  formatFrameworkName,
  listWorkspacePackages,
} from "../src/utils/discover-project.js";

const FIXTURES_DIRECTORY = path.resolve(import.meta.dirname, "fixtures");
const VALID_FRAMEWORKS = ["nextjs", "vite", "cra", "remix", "gatsby", "unknown"];

describe("discoverProject", () => {
  it("detects React version from package.json", () => {
    const projectInfo = discoverProject(path.join(FIXTURES_DIRECTORY, "basic-react"));
    expect(projectInfo.reactVersion).toBe("^19.0.0");
  });

  it("returns a valid framework", () => {
    const projectInfo = discoverProject(path.join(FIXTURES_DIRECTORY, "basic-react"));
    expect(VALID_FRAMEWORKS).toContain(projectInfo.framework);
  });

  it("detects TypeScript when tsconfig.json exists", () => {
    const projectInfo = discoverProject(path.join(FIXTURES_DIRECTORY, "basic-react"));
    expect(projectInfo.hasTypeScript).toBe(true);
  });

  it("detects React version from peerDependencies", () => {
    const projectInfo = discoverProject(path.join(FIXTURES_DIRECTORY, "component-library"));
    expect(projectInfo.reactVersion).toBe("^18.0.0 || ^19.0.0");
  });

  it("throws when package.json is missing", () => {
    expect(() => discoverProject("/nonexistent/path")).toThrow("No package.json found");
  });

  it("throws when package.json is a directory instead of a file", () => {
    const projectDirectory = path.join(tempDirectory, "eisdir-root");
    fs.mkdirSync(projectDirectory, { recursive: true });
    fs.mkdirSync(path.join(projectDirectory, "package.json"), { recursive: true });

    expect(() => discoverProject(projectDirectory)).toThrow("No package.json found");
  });
});

describe("listWorkspacePackages", () => {
  it("resolves nested workspace patterns like apps/*/ClientApp", () => {
    const packages = listWorkspacePackages(path.join(FIXTURES_DIRECTORY, "nested-workspaces"));
    const packageNames = packages.map((workspacePackage) => workspacePackage.name);

    expect(packageNames).toContain("my-app-client");
    expect(packageNames).toContain("ui");
    expect(packages).toHaveLength(2);
  });
});

const tempDirectory = fs.mkdtempSync(path.join(os.tmpdir(), "react-doctor-discover-test-"));

afterAll(() => {
  fs.rmSync(tempDirectory, { recursive: true, force: true });
});

describe("discoverReactSubprojects", () => {
  it("skips subdirectories where package.json is a directory (EISDIR)", () => {
    const rootDirectory = path.join(tempDirectory, "eisdir-package-json");
    const subdirectory = path.join(rootDirectory, "broken-sub");
    fs.mkdirSync(rootDirectory, { recursive: true });
    fs.writeFileSync(
      path.join(rootDirectory, "package.json"),
      JSON.stringify({ name: "my-app", dependencies: { react: "^19.0.0" } }),
    );
    fs.mkdirSync(subdirectory, { recursive: true });
    fs.mkdirSync(path.join(subdirectory, "package.json"), { recursive: true });

    const packages = discoverReactSubprojects(rootDirectory);
    expect(packages).toHaveLength(1);
    expect(packages[0].name).toBe("my-app");
  });

  it("includes root directory when it has a react dependency", () => {
    const rootDirectory = path.join(tempDirectory, "root-with-react");
    fs.mkdirSync(rootDirectory, { recursive: true });
    fs.writeFileSync(
      path.join(rootDirectory, "package.json"),
      JSON.stringify({ name: "my-app", dependencies: { react: "^19.0.0" } }),
    );

    const packages = discoverReactSubprojects(rootDirectory);
    expect(packages).toContainEqual({ name: "my-app", directory: rootDirectory });
  });

  it("includes both root and subdirectory when both have react", () => {
    const rootDirectory = path.join(tempDirectory, "root-and-sub");
    const subdirectory = path.join(rootDirectory, "extension");
    fs.mkdirSync(subdirectory, { recursive: true });
    fs.writeFileSync(
      path.join(rootDirectory, "package.json"),
      JSON.stringify({ name: "my-app", dependencies: { react: "^19.0.0" } }),
    );
    fs.writeFileSync(
      path.join(subdirectory, "package.json"),
      JSON.stringify({ name: "my-extension", dependencies: { react: "^18.0.0" } }),
    );

    const packages = discoverReactSubprojects(rootDirectory);
    expect(packages).toHaveLength(2);
    expect(packages[0]).toEqual({ name: "my-app", directory: rootDirectory });
    expect(packages[1]).toEqual({ name: "my-extension", directory: subdirectory });
  });

  it("does not match packages with only @types/react", () => {
    const rootDirectory = path.join(tempDirectory, "types-only");
    fs.mkdirSync(rootDirectory, { recursive: true });
    fs.writeFileSync(
      path.join(rootDirectory, "package.json"),
      JSON.stringify({ name: "types-only", devDependencies: { "@types/react": "^18.0.0" } }),
    );

    const packages = discoverReactSubprojects(rootDirectory);
    expect(packages).toHaveLength(0);
  });

  it("matches packages with react-native dependency", () => {
    const rootDirectory = path.join(tempDirectory, "rn-app");
    fs.mkdirSync(rootDirectory, { recursive: true });
    fs.writeFileSync(
      path.join(rootDirectory, "package.json"),
      JSON.stringify({ name: "rn-app", dependencies: { "react-native": "^0.74.0" } }),
    );

    const packages = discoverReactSubprojects(rootDirectory);
    expect(packages).toHaveLength(1);
  });
});

describe("formatFrameworkName", () => {
  it("formats known frameworks", () => {
    expect(formatFrameworkName("nextjs")).toBe("Next.js");
    expect(formatFrameworkName("vite")).toBe("Vite");
    expect(formatFrameworkName("cra")).toBe("Create React App");
    expect(formatFrameworkName("remix")).toBe("Remix");
    expect(formatFrameworkName("gatsby")).toBe("Gatsby");
  });

  it("formats unknown framework as React", () => {
    expect(formatFrameworkName("unknown")).toBe("React");
  });
});
```

## File: `packages/react-doctor/tests/filter-diagnostics.test.ts`
```typescript
import { describe, expect, it } from "vitest";
import type { Diagnostic, ReactDoctorConfig } from "../src/types.js";
import { filterIgnoredDiagnostics } from "../src/utils/filter-diagnostics.js";

const createDiagnostic = (overrides: Partial<Diagnostic> = {}): Diagnostic => ({
  filePath: "src/app.tsx",
  plugin: "react",
  rule: "no-danger",
  severity: "warning",
  message: "test message",
  help: "test help",
  line: 1,
  column: 1,
  category: "Correctness",
  ...overrides,
});

describe("filterIgnoredDiagnostics", () => {
  it("returns all diagnostics when config has no ignore rules", () => {
    const diagnostics = [createDiagnostic()];
    const config: ReactDoctorConfig = {};
    expect(filterIgnoredDiagnostics(diagnostics, config, "")).toEqual(diagnostics);
  });

  it("filters diagnostics matching ignored rules", () => {
    const diagnostics = [
      createDiagnostic({ plugin: "react", rule: "no-danger" }),
      createDiagnostic({ plugin: "jsx-a11y", rule: "no-autofocus" }),
      createDiagnostic({ plugin: "react-doctor", rule: "no-giant-component" }),
    ];
    const config: ReactDoctorConfig = {
      ignore: {
        rules: ["react/no-danger", "jsx-a11y/no-autofocus"],
      },
    };

    const filtered = filterIgnoredDiagnostics(diagnostics, config, "");
    expect(filtered).toHaveLength(1);
    expect(filtered[0].rule).toBe("no-giant-component");
  });

  it("filters diagnostics matching ignored file patterns", () => {
    const diagnostics = [
      createDiagnostic({ filePath: "src/generated/types.tsx" }),
      createDiagnostic({ filePath: "src/generated/api/client.tsx" }),
      createDiagnostic({ filePath: "src/components/Button.tsx" }),
    ];
    const config: ReactDoctorConfig = {
      ignore: {
        files: ["src/generated/**"],
      },
    };

    const filtered = filterIgnoredDiagnostics(diagnostics, config, "");
    expect(filtered).toHaveLength(1);
    expect(filtered[0].filePath).toBe("src/components/Button.tsx");
  });

  it("filters by both rules and files together", () => {
    const diagnostics = [
      createDiagnostic({ plugin: "react", rule: "no-danger", filePath: "src/app.tsx" }),
      createDiagnostic({ plugin: "knip", rule: "exports", filePath: "src/generated/api.tsx" }),
      createDiagnostic({
        plugin: "react-doctor",
        rule: "no-giant-component",
        filePath: "src/components/App.tsx",
      }),
    ];
    const config: ReactDoctorConfig = {
      ignore: {
        rules: ["react/no-danger"],
        files: ["src/generated/**"],
      },
    };

    const filtered = filterIgnoredDiagnostics(diagnostics, config, "");
    expect(filtered).toHaveLength(1);
    expect(filtered[0].rule).toBe("no-giant-component");
  });

  it("keeps all diagnostics when no rules or files match", () => {
    const diagnostics = [
      createDiagnostic({ plugin: "react", rule: "no-danger" }),
      createDiagnostic({ plugin: "knip", rule: "exports" }),
    ];
    const config: ReactDoctorConfig = {
      ignore: {
        rules: ["nonexistent/rule"],
        files: ["nonexistent/**"],
      },
    };

    const filtered = filterIgnoredDiagnostics(diagnostics, config, "");
    expect(filtered).toHaveLength(2);
  });

  it("filters file paths with ./ prefix against patterns without it", () => {
    const diagnostics = [
      createDiagnostic({ filePath: "./resources/js/components/ui/Button.tsx" }),
      createDiagnostic({ filePath: "./resources/js/marketing/Hero.tsx" }),
      createDiagnostic({ filePath: "./resources/js/pages/Home.tsx" }),
    ];
    const config: ReactDoctorConfig = {
      ignore: {
        files: ["resources/js/components/ui/**", "resources/js/marketing/**"],
      },
    };

    const filtered = filterIgnoredDiagnostics(diagnostics, config, "");
    expect(filtered).toHaveLength(1);
    expect(filtered[0].filePath).toBe("./resources/js/pages/Home.tsx");
  });

  it("handles knip rule identifiers", () => {
    const diagnostics = [
      createDiagnostic({ plugin: "knip", rule: "exports" }),
      createDiagnostic({ plugin: "knip", rule: "types" }),
      createDiagnostic({ plugin: "knip", rule: "files" }),
    ];
    const config: ReactDoctorConfig = {
      ignore: {
        rules: ["knip/exports", "knip/types"],
      },
    };

    const filtered = filterIgnoredDiagnostics(diagnostics, config, "");
    expect(filtered).toHaveLength(1);
    expect(filtered[0].rule).toBe("files");
  });
});
```

## File: `packages/react-doctor/tests/find-monorepo-root.test.ts`
```typescript
import path from "node:path";
import { describe, expect, it } from "vitest";
import { findMonorepoRoot, isMonorepoRoot } from "../src/utils/find-monorepo-root.js";

const FIXTURES_DIRECTORY = path.resolve(import.meta.dirname, "fixtures");

describe("isMonorepoRoot", () => {
  it("returns true for a directory with pnpm-workspace.yaml or workspaces", () => {
    const nestedWorkspaces = path.join(FIXTURES_DIRECTORY, "nested-workspaces");
    expect(isMonorepoRoot(nestedWorkspaces)).toBe(true);
  });

  it("returns false for a non-monorepo project", () => {
    const basicReact = path.join(FIXTURES_DIRECTORY, "basic-react");
    expect(isMonorepoRoot(basicReact)).toBe(false);
  });

  it("returns false for a nonexistent directory", () => {
    expect(isMonorepoRoot("/nonexistent/path")).toBe(false);
  });
});

describe("findMonorepoRoot", () => {
  it("returns null when no monorepo root exists above directory", () => {
    expect(findMonorepoRoot("/tmp")).toBeNull();
  });

  it("finds monorepo root from a nested workspace package", () => {
    const nestedPackage = path.join(FIXTURES_DIRECTORY, "nested-workspaces", "packages", "ui");
    const monorepoRoot = findMonorepoRoot(nestedPackage);
    expect(monorepoRoot).toBe(path.join(FIXTURES_DIRECTORY, "nested-workspaces"));
  });
});
```

## File: `packages/react-doctor/tests/indent-multiline-text.test.ts`
```typescript
import { describe, expect, it } from "vitest";
import { indentMultilineText } from "../src/utils/indent-multiline-text.js";

describe("indentMultilineText", () => {
  it("adds the prefix to a single line", () => {
    const indentedText = indentMultilineText("Error: Something happened", "    ");

    expect(indentedText).toBe("    Error: Something happened");
  });

  it("adds the prefix to every line in multiline text", () => {
    const explanation =
      "Error: Calling setState synchronously within an effect can trigger cascading renders\n\nEffects are intended to synchronize state between React and external systems.\n* Update external systems with the latest state from React.\n* Subscribe for updates from external systems and set state in a callback.";

    const indentedText = indentMultilineText(explanation, "    ");

    expect(indentedText).toBe(
      "    Error: Calling setState synchronously within an effect can trigger cascading renders\n    \n    Effects are intended to synchronize state between React and external systems.\n    * Update external systems with the latest state from React.\n    * Subscribe for updates from external systems and set state in a callback.",
    );
  });
});
```

## File: `packages/react-doctor/tests/load-config.test.ts`
```typescript
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { afterAll, beforeAll, describe, expect, it, vi } from "vitest";
import { loadConfig } from "../src/utils/load-config.js";

const tempRootDirectory = fs.mkdtempSync(path.join(os.tmpdir(), "react-doctor-config-test-"));

afterAll(() => {
  fs.rmSync(tempRootDirectory, { recursive: true, force: true });
});

describe("loadConfig", () => {
  describe("react-doctor.config.json", () => {
    let configDirectory: string;

    beforeAll(() => {
      configDirectory = path.join(tempRootDirectory, "with-config-file");
      fs.mkdirSync(configDirectory, { recursive: true });
      fs.writeFileSync(
        path.join(configDirectory, "react-doctor.config.json"),
        JSON.stringify({
          ignore: {
            rules: ["react/no-danger", "knip/exports"],
            files: ["src/generated/**"],
          },
        }),
      );
    });

    it("loads config from react-doctor.config.json", () => {
      const config = loadConfig(configDirectory);
      expect(config).toEqual({
        ignore: {
          rules: ["react/no-danger", "knip/exports"],
          files: ["src/generated/**"],
        },
      });
    });
  });

  describe("package.json reactDoctor key", () => {
    let packageJsonDirectory: string;

    beforeAll(() => {
      packageJsonDirectory = path.join(tempRootDirectory, "with-package-json-config");
      fs.mkdirSync(packageJsonDirectory, { recursive: true });
      fs.writeFileSync(
        path.join(packageJsonDirectory, "package.json"),
        JSON.stringify({
          name: "test-project",
          reactDoctor: {
            ignore: {
              rules: ["jsx-a11y/no-autofocus"],
            },
          },
        }),
      );
    });

    it("loads config from package.json reactDoctor key", () => {
      const config = loadConfig(packageJsonDirectory);
      expect(config).toEqual({
        ignore: {
          rules: ["jsx-a11y/no-autofocus"],
        },
      });
    });
  });

  describe("config file takes precedence", () => {
    let precedenceDirectory: string;

    beforeAll(() => {
      precedenceDirectory = path.join(tempRootDirectory, "precedence");
      fs.mkdirSync(precedenceDirectory, { recursive: true });
      fs.writeFileSync(
        path.join(precedenceDirectory, "react-doctor.config.json"),
        JSON.stringify({ ignore: { rules: ["from-config-file"] } }),
      );
      fs.writeFileSync(
        path.join(precedenceDirectory, "package.json"),
        JSON.stringify({
          name: "test",
          reactDoctor: { ignore: { rules: ["from-package-json"] } },
        }),
      );
    });

    it("prefers react-doctor.config.json over package.json", () => {
      const config = loadConfig(precedenceDirectory);
      expect(config?.ignore?.rules).toEqual(["from-config-file"]);
    });
  });

  describe("no config", () => {
    let emptyDirectory: string;

    beforeAll(() => {
      emptyDirectory = path.join(tempRootDirectory, "no-config");
      fs.mkdirSync(emptyDirectory, { recursive: true });
    });

    it("returns null when no config is found", () => {
      const config = loadConfig(emptyDirectory);
      expect(config).toBeNull();
    });

    it("returns null when config path is a directory instead of a file (EISDIR)", () => {
      const directoryConfigRoot = path.join(tempRootDirectory, "eisdir-config");
      fs.mkdirSync(directoryConfigRoot, { recursive: true });
      fs.mkdirSync(path.join(directoryConfigRoot, "react-doctor.config.json"), {
        recursive: true,
      });
      fs.mkdirSync(path.join(directoryConfigRoot, "package.json"), { recursive: true });

      const config = loadConfig(directoryConfigRoot);
      expect(config).toBeNull();
    });
  });

  describe("scan options in config", () => {
    let optionsDirectory: string;

    beforeAll(() => {
      optionsDirectory = path.join(tempRootDirectory, "with-scan-options");
      fs.mkdirSync(optionsDirectory, { recursive: true });
      fs.writeFileSync(
        path.join(optionsDirectory, "react-doctor.config.json"),
        JSON.stringify({
          ignore: { rules: ["react/no-danger"] },
          lint: true,
          deadCode: false,
          verbose: true,
          diff: "main",
        }),
      );
    });

    it("loads scan options alongside ignore config", () => {
      const config = loadConfig(optionsDirectory);
      expect(config).toEqual({
        ignore: { rules: ["react/no-danger"] },
        lint: true,
        deadCode: false,
        verbose: true,
        diff: "main",
      });
    });

    it("loads diff as boolean", () => {
      const boolDiffDirectory = path.join(tempRootDirectory, "with-bool-diff");
      fs.mkdirSync(boolDiffDirectory, { recursive: true });
      fs.writeFileSync(
        path.join(boolDiffDirectory, "react-doctor.config.json"),
        JSON.stringify({ diff: true }),
      );
      const config = loadConfig(boolDiffDirectory);
      expect(config?.diff).toBe(true);
    });
  });

  describe("invalid config", () => {
    let invalidJsonDirectory: string;
    let nonObjectDirectory: string;

    beforeAll(() => {
      invalidJsonDirectory = path.join(tempRootDirectory, "invalid-json");
      fs.mkdirSync(invalidJsonDirectory, { recursive: true });
      fs.writeFileSync(
        path.join(invalidJsonDirectory, "react-doctor.config.json"),
        "not valid json{{{",
      );

      nonObjectDirectory = path.join(tempRootDirectory, "non-object-config");
      fs.mkdirSync(nonObjectDirectory, { recursive: true });
      fs.writeFileSync(
        path.join(nonObjectDirectory, "react-doctor.config.json"),
        JSON.stringify([1, 2, 3]),
      );
    });

    it("returns null and warns for malformed JSON", () => {
      const warnSpy = vi.spyOn(console, "warn").mockImplementation(() => {});
      const config = loadConfig(invalidJsonDirectory);
      expect(config).toBeNull();
      expect(warnSpy).toHaveBeenCalledWith(expect.stringContaining("Failed to parse"));
      warnSpy.mockRestore();
    });

    it("returns null and warns when config is not an object", () => {
      const warnSpy = vi.spyOn(console, "warn").mockImplementation(() => {});
      const config = loadConfig(nonObjectDirectory);
      expect(config).toBeNull();
      expect(warnSpy).toHaveBeenCalledWith(expect.stringContaining("must be a JSON object"));
      warnSpy.mockRestore();
    });

    it("falls through to package.json when config file has malformed JSON", () => {
      const fallbackDirectory = path.join(tempRootDirectory, "malformed-with-fallback");
      fs.mkdirSync(fallbackDirectory, { recursive: true });
      fs.writeFileSync(
        path.join(fallbackDirectory, "react-doctor.config.json"),
        "not valid json{{{",
      );
      fs.writeFileSync(
        path.join(fallbackDirectory, "package.json"),
        JSON.stringify({
          name: "test",
          reactDoctor: { ignore: { rules: ["from-fallback"] } },
        }),
      );

      const warnSpy = vi.spyOn(console, "warn").mockImplementation(() => {});
      const config = loadConfig(fallbackDirectory);
      expect(config).toEqual({ ignore: { rules: ["from-fallback"] } });
      expect(warnSpy).toHaveBeenCalledOnce();
      warnSpy.mockRestore();
    });

    it("falls through to package.json when config file is not an object", () => {
      const nonObjectFallbackDirectory = path.join(tempRootDirectory, "non-object-with-fallback");
      fs.mkdirSync(nonObjectFallbackDirectory, { recursive: true });
      fs.writeFileSync(
        path.join(nonObjectFallbackDirectory, "react-doctor.config.json"),
        JSON.stringify([1, 2, 3]),
      );
      fs.writeFileSync(
        path.join(nonObjectFallbackDirectory, "package.json"),
        JSON.stringify({
          name: "test",
          reactDoctor: { ignore: { rules: ["from-non-object-fallback"] } },
        }),
      );

      const warnSpy = vi.spyOn(console, "warn").mockImplementation(() => {});
      const config = loadConfig(nonObjectFallbackDirectory);
      expect(config).toEqual({ ignore: { rules: ["from-non-object-fallback"] } });
      expect(warnSpy).toHaveBeenCalledOnce();
      warnSpy.mockRestore();
    });

    it("ignores non-object reactDoctor key in package.json", () => {
      const arrayConfigDirectory = path.join(tempRootDirectory, "array-pkg-config");
      fs.mkdirSync(arrayConfigDirectory, { recursive: true });
      fs.writeFileSync(
        path.join(arrayConfigDirectory, "package.json"),
        JSON.stringify({ name: "test", reactDoctor: "not-an-object" }),
      );
      const config = loadConfig(arrayConfigDirectory);
      expect(config).toBeNull();
    });
  });
});
```

## File: `packages/react-doctor/tests/match-glob-pattern.test.ts`
```typescript
import { describe, expect, it } from "vitest";
import { matchGlobPattern } from "../src/utils/match-glob-pattern.js";

describe("matchGlobPattern", () => {
  it("matches exact file paths", () => {
    expect(matchGlobPattern("src/app.tsx", "src/app.tsx")).toBe(true);
    expect(matchGlobPattern("src/app.tsx", "src/other.tsx")).toBe(false);
  });

  it("matches single wildcard for filenames", () => {
    expect(matchGlobPattern("src/app.tsx", "src/*.tsx")).toBe(true);
    expect(matchGlobPattern("src/utils.ts", "src/*.tsx")).toBe(false);
    expect(matchGlobPattern("src/nested/app.tsx", "src/*.tsx")).toBe(false);
  });

  it("matches double wildcard at the end", () => {
    expect(matchGlobPattern("src/generated/foo.tsx", "src/generated/**")).toBe(true);
    expect(matchGlobPattern("src/generated/bar/baz.tsx", "src/generated/**")).toBe(true);
    expect(matchGlobPattern("src/other/foo.tsx", "src/generated/**")).toBe(false);
  });

  it("matches double wildcard with trailing slash and filename", () => {
    expect(matchGlobPattern("src/foo/test.ts", "src/**/test.ts")).toBe(true);
    expect(matchGlobPattern("src/foo/bar/test.ts", "src/**/test.ts")).toBe(true);
    expect(matchGlobPattern("src/test.ts", "src/**/test.ts")).toBe(true);
  });

  it("matches double wildcard at the start", () => {
    expect(matchGlobPattern("src/components/Button.tsx", "**/*.tsx")).toBe(true);
    expect(matchGlobPattern("Button.tsx", "**/*.tsx")).toBe(true);
    expect(matchGlobPattern("deep/nested/path/file.tsx", "**/*.tsx")).toBe(true);
    expect(matchGlobPattern("file.ts", "**/*.tsx")).toBe(false);
  });

  it("matches question mark as single character", () => {
    expect(matchGlobPattern("src/a.tsx", "src/?.tsx")).toBe(true);
    expect(matchGlobPattern("src/ab.tsx", "src/?.tsx")).toBe(false);
  });

  it("escapes regex special characters in patterns", () => {
    expect(matchGlobPattern("src/file.test.tsx", "src/*.test.tsx")).toBe(true);
    expect(matchGlobPattern("src/filetesttsx", "src/*.test.tsx")).toBe(false);
  });

  it("normalizes backslashes to forward slashes", () => {
    expect(matchGlobPattern("src\\generated\\foo.tsx", "src/generated/**")).toBe(true);
  });
});
```

## File: `packages/react-doctor/tests/run-oxlint.test.ts`
```typescript
import path from "node:path";
import { describe, expect, it } from "vitest";
import type { Diagnostic } from "../src/types.js";
import { runOxlint } from "../src/utils/run-oxlint.js";

const FIXTURES_DIRECTORY = path.resolve(import.meta.dirname, "fixtures");
const BASIC_REACT_DIRECTORY = path.join(FIXTURES_DIRECTORY, "basic-react");
const NEXTJS_APP_DIRECTORY = path.join(FIXTURES_DIRECTORY, "nextjs-app");

const findDiagnosticsByRule = (diagnostics: Diagnostic[], rule: string): Diagnostic[] =>
  diagnostics.filter((diagnostic) => diagnostic.rule === rule);

interface RuleTestCase {
  fixture: string;
  ruleSource: string;
  severity?: "error" | "warning";
  category?: string;
}

const describeRules = (
  groupName: string,
  rules: Record<string, RuleTestCase>,
  getDiagnostics: () => Diagnostic[],
) => {
  describe(groupName, () => {
    for (const [ruleName, testCase] of Object.entries(rules)) {
      it(`${ruleName} (${testCase.fixture} → ${testCase.ruleSource})`, () => {
        const issues = findDiagnosticsByRule(getDiagnostics(), ruleName);
        expect(issues.length).toBeGreaterThan(0);
        if (testCase.severity) expect(issues[0].severity).toBe(testCase.severity);
        if (testCase.category) expect(issues[0].category).toBe(testCase.category);
      });
    }
  });
};

let basicReactDiagnostics: Diagnostic[];
let nextjsDiagnostics: Diagnostic[];

describe("runOxlint", () => {
  it("loads basic-react diagnostics", async () => {
    basicReactDiagnostics = await runOxlint(BASIC_REACT_DIRECTORY, true, "unknown", false);
    expect(basicReactDiagnostics.length).toBeGreaterThan(0);
  });

  it("loads nextjs diagnostics", async () => {
    nextjsDiagnostics = await runOxlint(NEXTJS_APP_DIRECTORY, true, "nextjs", false);
    expect(nextjsDiagnostics.length).toBeGreaterThan(0);
  });

  it("returns diagnostics with required fields", () => {
    for (const diagnostic of basicReactDiagnostics) {
      expect(diagnostic).toHaveProperty("filePath");
      expect(diagnostic).toHaveProperty("plugin");
      expect(diagnostic).toHaveProperty("rule");
      expect(diagnostic).toHaveProperty("severity");
      expect(diagnostic).toHaveProperty("message");
      expect(diagnostic).toHaveProperty("category");
      expect(["error", "warning"]).toContain(diagnostic.severity);
      expect(diagnostic.message.length).toBeGreaterThan(0);
    }
  });

  it("only reports diagnostics from JSX/TSX files", () => {
    for (const diagnostic of basicReactDiagnostics) {
      expect(diagnostic.filePath).toMatch(/\.(tsx|jsx)$/);
    }
  });

  describeRules(
    "state & effects rules",
    {
      "no-derived-state-effect": {
        fixture: "state-issues.tsx",
        ruleSource: "rules/state-and-effects.ts",
        severity: "error",
        category: "State & Effects",
      },
      "no-fetch-in-effect": {
        fixture: "state-issues.tsx",
        ruleSource: "rules/state-and-effects.ts",
        severity: "error",
      },
      "no-cascading-set-state": {
        fixture: "state-issues.tsx",
        ruleSource: "rules/state-and-effects.ts",
        severity: "warning",
      },
      "no-effect-event-handler": {
        fixture: "state-issues.tsx",
        ruleSource: "rules/state-and-effects.ts",
        severity: "warning",
      },
      "no-derived-useState": {
        fixture: "state-issues.tsx",
        ruleSource: "rules/state-and-effects.ts",
        severity: "warning",
      },
      "prefer-useReducer": {
        fixture: "state-issues.tsx",
        ruleSource: "rules/state-and-effects.ts",
        severity: "warning",
      },
      "rerender-lazy-state-init": {
        fixture: "state-issues.tsx",
        ruleSource: "rules/state-and-effects.ts",
        severity: "warning",
      },
      "rerender-functional-setstate": {
        fixture: "state-issues.tsx",
        ruleSource: "rules/state-and-effects.ts",
        severity: "warning",
      },
      "rerender-dependencies": {
        fixture: "state-issues.tsx",
        ruleSource: "rules/state-and-effects.ts",
        severity: "error",
      },
    },
    () => basicReactDiagnostics,
  );

  describeRules(
    "architecture rules",
    {
      "no-giant-component": {
        fixture: "giant-component.tsx",
        ruleSource: "rules/architecture.ts",
        category: "Architecture",
      },
      "no-render-in-render": {
        fixture: "architecture-issues.tsx",
        ruleSource: "rules/architecture.ts",
        category: "Architecture",
      },
      "no-nested-component-definition": {
        fixture: "architecture-issues.tsx",
        ruleSource: "rules/architecture.ts",
        severity: "error",
      },
    },
    () => basicReactDiagnostics,
  );

  describeRules(
    "performance rules",
    {
      "no-inline-prop-on-memo-component": {
        fixture: "performance-issues.tsx",
        ruleSource: "rules/performance.ts",
      },
      "no-usememo-simple-expression": {
        fixture: "performance-issues.tsx",
        ruleSource: "rules/performance.ts",
        category: "Performance",
      },
      "no-layout-property-animation": {
        fixture: "performance-issues.tsx",
        ruleSource: "rules/performance.ts",
        severity: "error",
      },
      "no-transition-all": {
        fixture: "performance-issues.tsx",
        ruleSource: "rules/performance.ts",
      },
      "no-large-animated-blur": {
        fixture: "performance-issues.tsx",
        ruleSource: "rules/performance.ts",
      },
      "no-scale-from-zero": {
        fixture: "performance-issues.tsx",
        ruleSource: "rules/performance.ts",
      },
      "no-permanent-will-change": {
        fixture: "performance-issues.tsx",
        ruleSource: "rules/performance.ts",
      },
      "rerender-memo-with-default-value": {
        fixture: "performance-issues.tsx",
        ruleSource: "rules/performance.ts",
      },
      "rendering-animate-svg-wrapper": {
        fixture: "performance-issues.tsx",
        ruleSource: "rules/performance.ts",
      },
      "rendering-hydration-no-flicker": {
        fixture: "performance-issues.tsx",
        ruleSource: "rules/performance.ts",
      },
      "no-global-css-variable-animation": {
        fixture: "performance-issues.tsx",
        ruleSource: "rules/performance.ts",
        severity: "error",
      },
      "client-passive-event-listeners": {
        fixture: "client-issues.tsx",
        ruleSource: "rules/client.ts",
      },
    },
    () => basicReactDiagnostics,
  );

  describeRules(
    "async performance rules",
    {
      "async-parallel": {
        fixture: "js-performance-issues.tsx",
        ruleSource: "rules/js-performance.ts",
      },
    },
    () => basicReactDiagnostics,
  );

  describeRules(
    "bundle size rules",
    {
      "no-full-lodash-import": {
        fixture: "bundle-issues.tsx",
        ruleSource: "rules/bundle-size.ts",
        category: "Bundle Size",
      },
      "no-moment": {
        fixture: "bundle-issues.tsx",
        ruleSource: "rules/bundle-size.ts",
      },
      "use-lazy-motion": {
        fixture: "bundle-issues.tsx",
        ruleSource: "rules/bundle-size.ts",
      },
      "prefer-dynamic-import": {
        fixture: "bundle-issues.tsx",
        ruleSource: "rules/bundle-size.ts",
      },
      "no-undeferred-third-party": {
        fixture: "bundle-issues.tsx",
        ruleSource: "rules/bundle-size.ts",
      },
    },
    () => basicReactDiagnostics,
  );

  describeRules(
    "correctness rules",
    {
      "no-array-index-as-key": {
        fixture: "correctness-issues.tsx",
        ruleSource: "rules/correctness.ts",
        category: "Correctness",
      },
      "rendering-conditional-render": {
        fixture: "correctness-issues.tsx",
        ruleSource: "rules/correctness.ts",
      },
      "no-prevent-default": {
        fixture: "correctness-issues.tsx",
        ruleSource: "rules/correctness.ts",
      },
    },
    () => basicReactDiagnostics,
  );

  describeRules(
    "security rules",
    {
      "no-secrets-in-client-code": {
        fixture: "security-issues.tsx",
        ruleSource: "rules/security.ts",
        severity: "error",
        category: "Security",
      },
    },
    () => basicReactDiagnostics,
  );

  describeRules(
    "nextjs rules",
    {
      "nextjs-no-img-element": {
        fixture: "app/page.tsx",
        ruleSource: "rules/nextjs.ts",
        category: "Next.js",
      },
      "nextjs-async-client-component": {
        fixture: "app/page.tsx",
        ruleSource: "rules/nextjs.ts",
        severity: "error",
      },
      "nextjs-no-a-element": {
        fixture: "app/page.tsx",
        ruleSource: "rules/nextjs.ts",
      },
      "nextjs-no-use-search-params-without-suspense": {
        fixture: "app/page.tsx",
        ruleSource: "rules/nextjs.ts",
      },
      "nextjs-no-client-fetch-for-server-data": {
        fixture: "app/layout.tsx",
        ruleSource: "rules/nextjs.ts",
      },
      "nextjs-missing-metadata": {
        fixture: "app/page.tsx",
        ruleSource: "rules/nextjs.ts",
      },
      "nextjs-no-client-side-redirect": {
        fixture: "app/page.tsx",
        ruleSource: "rules/nextjs.ts",
      },
      "nextjs-no-redirect-in-try-catch": {
        fixture: "app/page.tsx",
        ruleSource: "rules/nextjs.ts",
      },
      "nextjs-image-missing-sizes": {
        fixture: "app/page.tsx",
        ruleSource: "rules/nextjs.ts",
      },
      "nextjs-no-native-script": {
        fixture: "app/page.tsx",
        ruleSource: "rules/nextjs.ts",
      },
      "nextjs-inline-script-missing-id": {
        fixture: "app/page.tsx",
        ruleSource: "rules/nextjs.ts",
      },
      "nextjs-no-font-link": {
        fixture: "app/page.tsx",
        ruleSource: "rules/nextjs.ts",
      },
      "nextjs-no-css-link": {
        fixture: "app/page.tsx",
        ruleSource: "rules/nextjs.ts",
      },
      "nextjs-no-polyfill-script": {
        fixture: "app/page.tsx",
        ruleSource: "rules/nextjs.ts",
      },
      "nextjs-no-head-import": {
        fixture: "app/page.tsx",
        ruleSource: "rules/nextjs.ts",
        severity: "error",
      },
      "nextjs-no-side-effect-in-get-handler": {
        fixture: "app/logout/route.tsx",
        ruleSource: "rules/nextjs.ts",
        severity: "error",
      },
      "server-auth-actions": {
        fixture: "app/actions.tsx",
        ruleSource: "rules/server.ts",
        severity: "error",
        category: "Server",
      },
      "server-after-nonblocking": {
        fixture: "app/actions.tsx",
        ruleSource: "rules/server.ts",
      },
    },
    () => nextjsDiagnostics,
  );
});
```

## File: `packages/react-doctor/tests/scan.test.ts`
```typescript
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { afterAll, describe, expect, it, vi } from "vitest";
import { scan } from "../src/scan.js";

const FIXTURES_DIRECTORY = path.resolve(import.meta.dirname, "fixtures");

vi.mock("ora", () => ({
  default: () => ({
    text: "",
    start: function () {
      return this;
    },
    stop: function () {
      return this;
    },
    succeed: () => {},
    fail: () => {},
  }),
}));

const noReactTempDirectory = fs.mkdtempSync(path.join(os.tmpdir(), "react-doctor-test-"));
fs.writeFileSync(
  path.join(noReactTempDirectory, "package.json"),
  JSON.stringify({ name: "no-react", dependencies: {} }),
);

afterAll(() => {
  fs.rmSync(noReactTempDirectory, { recursive: true, force: true });
});

describe("scan", () => {
  it("completes without throwing on a valid React project", async () => {
    const consoleSpy = vi.spyOn(console, "log").mockImplementation(() => {});
    try {
      await scan(path.join(FIXTURES_DIRECTORY, "basic-react"), {
        lint: true,
        deadCode: false,
      });
    } finally {
      consoleSpy.mockRestore();
    }
  });

  it("throws when React dependency is missing", async () => {
    const consoleSpy = vi.spyOn(console, "log").mockImplementation(() => {});
    try {
      await expect(scan(noReactTempDirectory, { lint: true, deadCode: false })).rejects.toThrow(
        "No React dependency found",
      );
    } finally {
      consoleSpy.mockRestore();
    }
  });

  it("skips lint when option is disabled", async () => {
    const consoleSpy = vi.spyOn(console, "log").mockImplementation(() => {});
    try {
      await scan(path.join(FIXTURES_DIRECTORY, "basic-react"), {
        lint: false,
        deadCode: false,
      });
    } finally {
      consoleSpy.mockRestore();
    }
  });

  it("runs lint and dead code in parallel when both enabled", async () => {
    const consoleSpy = vi.spyOn(console, "log").mockImplementation(() => {});
    try {
      const startTime = performance.now();
      await scan(path.join(FIXTURES_DIRECTORY, "basic-react"), {
        lint: true,
        deadCode: true,
      });
      const elapsedMilliseconds = performance.now() - startTime;

      expect(elapsedMilliseconds).toBeLessThan(30_000);
    } finally {
      consoleSpy.mockRestore();
    }
  });
});
```

## File: `packages/react-doctor/tests/should-auto-select-current-choice.test.ts`
```typescript
import { describe, expect, it } from "vitest";
import { shouldAutoSelectCurrentChoice } from "../src/utils/should-auto-select-current-choice.js";

describe("shouldAutoSelectCurrentChoice", () => {
  it("returns true when nothing is selected and cursor is on an enabled choice", () => {
    const result = shouldAutoSelectCurrentChoice(
      [{ selected: false }, { selected: false }, { selected: false }],
      1,
    );

    expect(result).toBe(true);
  });

  it("returns false when a choice is already selected", () => {
    const result = shouldAutoSelectCurrentChoice(
      [{ selected: true }, { selected: false }, { selected: false }],
      1,
    );

    expect(result).toBe(false);
  });

  it("returns false when cursor is on a disabled choice", () => {
    const result = shouldAutoSelectCurrentChoice(
      [{ selected: false }, { selected: false, disabled: true }],
      1,
    );

    expect(result).toBe(false);
  });

  it("returns false when all choices are disabled and nothing is selected", () => {
    const result = shouldAutoSelectCurrentChoice([{ disabled: true }, { disabled: true }], 0);

    expect(result).toBe(false);
  });

  it("returns false when cursor is out of bounds", () => {
    const result = shouldAutoSelectCurrentChoice([{ selected: false }, { selected: false }], 5);

    expect(result).toBe(false);
  });

  it("returns false when choice states array is empty", () => {
    const result = shouldAutoSelectCurrentChoice([], 0);

    expect(result).toBe(false);
  });

  it("returns true when selected is undefined on all choices", () => {
    const result = shouldAutoSelectCurrentChoice([{}, {}, {}], 0);

    expect(result).toBe(true);
  });

  it("returns false when cursor is negative", () => {
    const result = shouldAutoSelectCurrentChoice([{ selected: false }, { selected: false }], -1);

    expect(result).toBe(false);
  });
});
```

## File: `packages/react-doctor/tests/should-select-all-choices.test.ts`
```typescript
import { describe, expect, it } from "vitest";
import { shouldSelectAllChoices } from "../src/utils/should-select-all-choices.js";

describe("shouldSelectAllChoices", () => {
  it("returns true when no enabled choice is selected", () => {
    const shouldSelectAllEnabledChoices = shouldSelectAllChoices([
      { selected: false },
      { selected: false },
    ]);

    expect(shouldSelectAllEnabledChoices).toBe(true);
  });

  it("returns true when some enabled choices are selected", () => {
    const shouldSelectAllEnabledChoices = shouldSelectAllChoices([
      { selected: true },
      { selected: false },
      { selected: false },
    ]);

    expect(shouldSelectAllEnabledChoices).toBe(true);
  });

  it("returns false when all enabled choices are selected", () => {
    const shouldSelectAllEnabledChoices = shouldSelectAllChoices([
      { selected: true },
      { selected: true },
      { selected: true },
    ]);

    expect(shouldSelectAllEnabledChoices).toBe(false);
  });

  it("ignores disabled choices when checking if all are selected", () => {
    const shouldSelectAllEnabledChoices = shouldSelectAllChoices([
      { selected: true },
      { selected: false, disabled: true },
      { selected: true },
    ]);

    expect(shouldSelectAllEnabledChoices).toBe(false);
  });
});
```

## File: `packages/react-doctor/tests/fixtures/basic-react/package.json`
```json
{
  "name": "test-basic-react",
  "private": true,
  "dependencies": {
    "react": "^19.0.0",
    "react-dom": "^19.0.0"
  }
}
```

## File: `packages/react-doctor/tests/fixtures/basic-react/tsconfig.json`
```json
{
  "compilerOptions": {
    "jsx": "react-jsx",
    "strict": true,
    "target": "ESNext",
    "module": "ESNext",
    "moduleResolution": "bundler"
  }
}
```

## File: `packages/react-doctor/tests/fixtures/basic-react/src/architecture-issues.tsx`
```tsx
import { useState } from "react";

const GenericHandlerComponent = () => {
  const handleClick = () => {};
  return <button onClick={handleClick}>Click</button>;
};

const RenderInRenderComponent = () => {
  const renderItem = (item: string) => <span>{item}</span>;
  return <div>{renderItem("hello")}</div>;
};

const ParentComponent = () => {
  const NestedChild = () => <span>nested</span>;
  return <NestedChild />;
};

export { GenericHandlerComponent, RenderInRenderComponent, ParentComponent };
```

## File: `packages/react-doctor/tests/fixtures/basic-react/src/bundle-issues.tsx`
```tsx
import { debounce } from "lodash";
import moment from "moment";
import { motion } from "framer-motion";
import MonacoEditor from "@monaco-editor/react";
import { Button } from "./components/index";

const DebouncedInput = () => {
  const handleChange = debounce(() => {}, 300);
  return <input onChange={handleChange} />;
};

const DateDisplay = () => <div>{moment().format("YYYY-MM-DD")}</div>;

const AnimatedBox = () => <motion.div animate={{ x: 100 }} />;

const EditorComponent = () => <MonacoEditor height="400px" />;

const ImportedButton = () => <Button />;

const ThirdPartyScript = () => <script src="https://cdn.example.com/widget.js" />;

export {
  DebouncedInput,
  DateDisplay,
  AnimatedBox,
  EditorComponent,
  ImportedButton,
  ThirdPartyScript,
};
```

## File: `packages/react-doctor/tests/fixtures/basic-react/src/clean.tsx`
```tsx
import { useState } from "react";

const Counter = () => {
  const [count, setCount] = useState(0);
  return <button onClick={() => setCount((previous) => previous + 1)}>{count}</button>;
};

export { Counter };
```

## File: `packages/react-doctor/tests/fixtures/basic-react/src/client-issues.tsx`
```tsx
import { useEffect, useRef } from "react";

const ScrollListenerComponent = () => {
  const ref = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const element = ref.current;
    if (!element) return;
    const handler = () => {};
    element.addEventListener("scroll", handler);
    return () => element.removeEventListener("scroll", handler);
  }, []);

  return <div ref={ref} />;
};

export { ScrollListenerComponent };
```

## File: `packages/react-doctor/tests/fixtures/basic-react/src/correctness-issues.tsx`
```tsx
const IndexKeyList = ({ items }: { items: string[] }) => (
  <ul>
    {items.map((item, index) => (
      <li key={index}>{item}</li>
    ))}
  </ul>
);

const ConditionalRenderBug = ({ items }: { items: string[] }) => (
  <div>
    {items.length && (
      <ul>
        {items.map((item) => (
          <li key={item}>{item}</li>
        ))}
      </ul>
    )}
  </div>
);

const PreventDefaultForm = () => (
  <form
    onSubmit={(event) => {
      event.preventDefault();
    }}
  >
    <button type="submit">Submit</button>
  </form>
);

export { IndexKeyList, ConditionalRenderBug, PreventDefaultForm };
```

## File: `packages/react-doctor/tests/fixtures/basic-react/src/giant-component.tsx`
```tsx
const GiantComponent = () => {
  const x0 = 0;
  const x1 = 1;
  const x2 = 2;
  const x3 = 3;
  const x4 = 4;
  const x5 = 5;
  const x6 = 6;
  const x7 = 7;
  const x8 = 8;
  const x9 = 9;
  const x10 = 10;
  const x11 = 11;
  const x12 = 12;
  const x13 = 13;
  const x14 = 14;
  const x15 = 15;
  const x16 = 16;
  const x17 = 17;
  const x18 = 18;
  const x19 = 19;
  const x20 = 20;
  const x21 = 21;
  const x22 = 22;
  const x23 = 23;
  const x24 = 24;
  const x25 = 25;
  const x26 = 26;
  const x27 = 27;
  const x28 = 28;
  const x29 = 29;
  const x30 = 30;
  const x31 = 31;
  const x32 = 32;
  const x33 = 33;
  const x34 = 34;
  const x35 = 35;
  const x36 = 36;
  const x37 = 37;
  const x38 = 38;
  const x39 = 39;
  const x40 = 40;
  const x41 = 41;
  const x42 = 42;
  const x43 = 43;
  const x44 = 44;
  const x45 = 45;
  const x46 = 46;
  const x47 = 47;
  const x48 = 48;
  const x49 = 49;
  const x50 = 50;
  const x51 = 51;
  const x52 = 52;
  const x53 = 53;
  const x54 = 54;
  const x55 = 55;
  const x56 = 56;
  const x57 = 57;
  const x58 = 58;
  const x59 = 59;
  const x60 = 60;
  const x61 = 61;
  const x62 = 62;
  const x63 = 63;
  const x64 = 64;
  const x65 = 65;
  const x66 = 66;
  const x67 = 67;
  const x68 = 68;
  const x69 = 69;
  const x70 = 70;
  const x71 = 71;
  const x72 = 72;
  const x73 = 73;
  const x74 = 74;
  const x75 = 75;
  const x76 = 76;
  const x77 = 77;
  const x78 = 78;
  const x79 = 79;
  const x80 = 80;
  const x81 = 81;
  const x82 = 82;
  const x83 = 83;
  const x84 = 84;
  const x85 = 85;
  const x86 = 86;
  const x87 = 87;
  const x88 = 88;
  const x89 = 89;
  const x90 = 90;
  const x91 = 91;
  const x92 = 92;
  const x93 = 93;
  const x94 = 94;
  const x95 = 95;
  const x96 = 96;
  const x97 = 97;
  const x98 = 98;
  const x99 = 99;
  const x100 = 100;
  const x101 = 101;
  const x102 = 102;
  const x103 = 103;
  const x104 = 104;
  const x105 = 105;
  const x106 = 106;
  const x107 = 107;
  const x108 = 108;
  const x109 = 109;
  const x110 = 110;
  const x111 = 111;
  const x112 = 112;
  const x113 = 113;
  const x114 = 114;
  const x115 = 115;
  const x116 = 116;
  const x117 = 117;
  const x118 = 118;
  const x119 = 119;
  const x120 = 120;
  const x121 = 121;
  const x122 = 122;
  const x123 = 123;
  const x124 = 124;
  const x125 = 125;
  const x126 = 126;
  const x127 = 127;
  const x128 = 128;
  const x129 = 129;
  const x130 = 130;
  const x131 = 131;
  const x132 = 132;
  const x133 = 133;
  const x134 = 134;
  const x135 = 135;
  const x136 = 136;
  const x137 = 137;
  const x138 = 138;
  const x139 = 139;
  const x140 = 140;
  const x141 = 141;
  const x142 = 142;
  const x143 = 143;
  const x144 = 144;
  const x145 = 145;
  const x146 = 146;
  const x147 = 147;
  const x148 = 148;
  const x149 = 149;
  const x150 = 150;
  const x151 = 151;
  const x152 = 152;
  const x153 = 153;
  const x154 = 154;
  const x155 = 155;
  const x156 = 156;
  const x157 = 157;
  const x158 = 158;
  const x159 = 159;
  const x160 = 160;
  const x161 = 161;
  const x162 = 162;
  const x163 = 163;
  const x164 = 164;
  const x165 = 165;
  const x166 = 166;
  const x167 = 167;
  const x168 = 168;
  const x169 = 169;
  const x170 = 170;
  const x171 = 171;
  const x172 = 172;
  const x173 = 173;
  const x174 = 174;
  const x175 = 175;
  const x176 = 176;
  const x177 = 177;
  const x178 = 178;
  const x179 = 179;
  const x180 = 180;
  const x181 = 181;
  const x182 = 182;
  const x183 = 183;
  const x184 = 184;
  const x185 = 185;
  const x186 = 186;
  const x187 = 187;
  const x188 = 188;
  const x189 = 189;
  const x190 = 190;
  const x191 = 191;
  const x192 = 192;
  const x193 = 193;
  const x194 = 194;
  const x195 = 195;
  const x196 = 196;
  const x197 = 197;
  const x198 = 198;
  const x199 = 199;
  const x200 = 200;
  const x201 = 201;
  const x202 = 202;
  const x203 = 203;
  const x204 = 204;
  const x205 = 205;
  const x206 = 206;
  const x207 = 207;
  const x208 = 208;
  const x209 = 209;
  const x210 = 210;
  const x211 = 211;
  const x212 = 212;
  const x213 = 213;
  const x214 = 214;
  const x215 = 215;
  const x216 = 216;
  const x217 = 217;
  const x218 = 218;
  const x219 = 219;
  const x220 = 220;
  const x221 = 221;
  const x222 = 222;
  const x223 = 223;
  const x224 = 224;
  const x225 = 225;
  const x226 = 226;
  const x227 = 227;
  const x228 = 228;
  const x229 = 229;
  const x230 = 230;
  const x231 = 231;
  const x232 = 232;
  const x233 = 233;
  const x234 = 234;
  const x235 = 235;
  const x236 = 236;
  const x237 = 237;
  const x238 = 238;
  const x239 = 239;
  const x240 = 240;
  const x241 = 241;
  const x242 = 242;
  const x243 = 243;
  const x244 = 244;
  const x245 = 245;
  const x246 = 246;
  const x247 = 247;
  const x248 = 248;
  const x249 = 249;
  const x250 = 250;
  const x251 = 251;
  const x252 = 252;
  const x253 = 253;
  const x254 = 254;
  const x255 = 255;
  const x256 = 256;
  const x257 = 257;
  const x258 = 258;
  const x259 = 259;
  const x260 = 260;
  const x261 = 261;
  const x262 = 262;
  const x263 = 263;
  const x264 = 264;
  const x265 = 265;
  const x266 = 266;
  const x267 = 267;
  const x268 = 268;
  const x269 = 269;
  const x270 = 270;
  const x271 = 271;
  const x272 = 272;
  const x273 = 273;
  const x274 = 274;
  const x275 = 275;
  const x276 = 276;
  const x277 = 277;
  const x278 = 278;
  const x279 = 279;
  const x280 = 280;
  const x281 = 281;
  const x282 = 282;
  const x283 = 283;
  const x284 = 284;
  const x285 = 285;
  const x286 = 286;
  const x287 = 287;
  const x288 = 288;
  const x289 = 289;
  const x290 = 290;
  const x291 = 291;
  const x292 = 292;
  const x293 = 293;
  const x294 = 294;
  const x295 = 295;
  const x296 = 296;
  const x297 = 297;
  const x298 = 298;
  const x299 = 299;
  const x300 = 300;
  return <div>{x0}</div>;
};

export { GiantComponent };
```

## File: `packages/react-doctor/tests/fixtures/basic-react/src/js-performance-issues.tsx`
```tsx
const CombineIterationsComponent = ({ items }: { items: number[] }) => {
  const result = items.filter((item) => item > 0).map((item) => item * 2);
  return <div>{result.join(",")}</div>;
};

const SpreadSortComponent = ({ items }: { items: number[] }) => {
  const sorted = [...items].sort((first, second) => first - second);
  return <div>{sorted.join(",")}</div>;
};

const MinViaSortComponent = ({ items }: { items: number[] }) => {
  const smallest = items.sort((first, second) => first - second)[0];
  return <div>{smallest}</div>;
};

const RegexpInLoopComponent = ({ items }: { items: string[] }) => {
  const matches: string[] = [];
  for (const item of items) {
    if (new RegExp("test").test(item)) {
      matches.push(item);
    }
  }
  return <div>{matches.join(",")}</div>;
};

const SetMapLookupsComponent = ({ items }: { items: string[] }) => {
  const allowed = ["a", "b", "c"];
  const filtered: string[] = [];
  for (const item of items) {
    if (allowed.includes(item)) {
      filtered.push(item);
    }
  }
  return <div>{filtered.join(",")}</div>;
};

const BatchDomCssComponent = () => {
  const applyStyles = (element: HTMLElement) => {
    element.style.color = "red";
    element.style.backgroundColor = "blue";
  };
  return <button onClick={(event) => applyStyles(event.currentTarget)}>Style</button>;
};

const IndexMapsComponent = ({ users }: { users: { id: string; name: string }[] }) => {
  const ids = ["1", "2", "3"];
  const found: string[] = [];
  for (const id of ids) {
    const user = users.find((innerUser) => innerUser.id === id);
    if (user) found.push(user.name);
  }
  return <div>{found.join(",")}</div>;
};

const CacheStorageComponent = () => {
  const theme = localStorage.getItem("theme");
  const themeAgain = localStorage.getItem("theme");
  return (
    <div>
      {theme}
      {themeAgain}
    </div>
  );
};

const EarlyExitComponent = ({ value }: { value: number }) => {
  if (value > 0) {
    if (value > 10) {
      if (value > 100) {
        if (value > 1000) {
          return <div>big</div>;
        }
      }
    }
  }
  return <div>small</div>;
};

const SequentialAwaitComponent = () => {
  const loadData = async () => {
    const users = await fetch("/api/users");
    const posts = await fetch("/api/posts");
    const comments = await fetch("/api/comments");
    return { users, posts, comments };
  };
  return <button onClick={loadData}>Load</button>;
};

export {
  CombineIterationsComponent,
  SpreadSortComponent,
  MinViaSortComponent,
  RegexpInLoopComponent,
  SetMapLookupsComponent,
  BatchDomCssComponent,
  IndexMapsComponent,
  CacheStorageComponent,
  EarlyExitComponent,
  SequentialAwaitComponent,
};
```

## File: `packages/react-doctor/tests/fixtures/basic-react/src/performance-issues.tsx`
```tsx
import { useState, useEffect, useMemo, memo } from "react";

const MemoChild = memo(({ onClick }: { onClick: () => void }) => (
  <button onClick={onClick}>click</button>
));

const ParentWithInlinePropOnMemo = () => <MemoChild onClick={() => console.log("inline")} />;

const SimpleMemoComponent = ({ count }: { count: number }) => {
  const doubled = useMemo(() => count * 2, [count]);
  return <div>{doubled}</div>;
};

const LayoutAnimationComponent = () => <div animate={{ width: 100, height: 200 }}>animated</div>;

const TransitionAllComponent = () => <div style={{ transition: "all 0.3s ease" }}>styled</div>;

const LargeBlurComponent = () => <div style={{ filter: "blur(20px)" }}>blurred</div>;

const ScaleFromZeroComponent = () => <div initial={{ scale: 0 }}>scale</div>;

const PermanentWillChangeComponent = () => <div style={{ willChange: "transform" }}>permanent</div>;

const DefaultPropComponent = ({ items = [] }: { items?: string[] }) => (
  <ul>
    {items.map((item) => (
      <li key={item}>{item}</li>
    ))}
  </ul>
);

const SvgAnimationComponent = () => (
  <svg animate={{ rotate: 45 }}>
    <circle r={10} />
  </svg>
);

const LoadingStateComponent = () => {
  const [isLoading, setIsLoading] = useState(false);
  return <div>{isLoading ? "Loading..." : "Done"}</div>;
};

const HydrationFlickerComponent = () => {
  const [mounted, setMounted] = useState(false);
  useEffect(() => {
    setMounted(true);
  }, []);
  return <div>{mounted ? "client" : "server"}</div>;
};

const GlobalCssVarComponent = () => {
  requestAnimationFrame(() => {
    document.documentElement.style.setProperty("--scroll-y", "100px");
  });
  return <div />;
};

export {
  MemoChild,
  ParentWithInlinePropOnMemo,
  SimpleMemoComponent,
  LayoutAnimationComponent,
  TransitionAllComponent,
  LargeBlurComponent,
  ScaleFromZeroComponent,
  PermanentWillChangeComponent,
  DefaultPropComponent,
  SvgAnimationComponent,
  LoadingStateComponent,
  HydrationFlickerComponent,
  GlobalCssVarComponent,
};
```

## File: `packages/react-doctor/tests/fixtures/basic-react/src/security-issues.tsx`
```tsx
const apiKey = "sk_live_1234567890abcdef";

const SecretDisplay = () => <div>{apiKey}</div>;

export { SecretDisplay };
```

## File: `packages/react-doctor/tests/fixtures/basic-react/src/state-issues.tsx`
```tsx
import { useState, useEffect, useMemo, useCallback } from "react";

const DerivedStateComponent = ({ items }: { items: string[] }) => {
  const [filteredItems, setFilteredItems] = useState<string[]>([]);

  useEffect(() => {
    setFilteredItems(items);
  }, [items]);

  return <div>{filteredItems.join(",")}</div>;
};

const StateResetComponent = ({ visible }: { visible: boolean }) => {
  const [inputValue, setInputValue] = useState("");
  useEffect(() => {
    setInputValue("");
  }, [visible]);
  return <input value={inputValue} onChange={(event) => setInputValue(event.target.value)} />;
};

const FetchInEffectComponent = () => {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch("/api/data")
      .then((response) => response.json())
      .then((json) => setData(json));
  }, []);

  return <div>{JSON.stringify(data)}</div>;
};

const LazyInitComponent = () => {
  const [value, setValue] = useState(JSON.parse("{}"));
  return <div>{JSON.stringify(value)}</div>;
};

const CascadingSetStateComponent = () => {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [age, setAge] = useState(0);

  useEffect(() => {
    setName("John");
    setEmail("john@example.com");
    setAge(30);
  }, []);

  return (
    <div>
      {name} {email} {age}
    </div>
  );
};

const EffectEventHandlerComponent = ({ isOpen }: { isOpen: boolean }) => {
  useEffect(() => {
    if (isOpen) {
      document.body.classList.add("modal-open");
    }
  }, [isOpen]);

  return <div />;
};

const DerivedUseStateComponent = ({ initialName }: { initialName: string }) => {
  const [name, setName] = useState(initialName);
  return <input value={name} onChange={(event) => setName(event.target.value)} />;
};

const PreferUseReducerComponent = () => {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [age, setAge] = useState(0);
  const [address, setAddress] = useState("");
  const [phone, setPhone] = useState("");

  return (
    <div>
      <input value={name} onChange={(event) => setName(event.target.value)} />
      <input value={email} onChange={(event) => setEmail(event.target.value)} />
      <input value={age} type="number" onChange={(event) => setAge(Number(event.target.value))} />
      <input value={address} onChange={(event) => setAddress(event.target.value)} />
      <input value={phone} onChange={(event) => setPhone(event.target.value)} />
    </div>
  );
};

const FunctionalSetStateComponent = () => {
  const [count, setCount] = useState(0);
  return <button onClick={() => setCount(count + 1)}>{count}</button>;
};

const DependencyLiteralComponent = () => {
  useEffect(() => {}, [{}]);
  useCallback(() => {}, [[]]);
  return <div />;
};

export {
  DerivedStateComponent,
  StateResetComponent,
  FetchInEffectComponent,
  LazyInitComponent,
  CascadingSetStateComponent,
  EffectEventHandlerComponent,
  DerivedUseStateComponent,
  PreferUseReducerComponent,
  FunctionalSetStateComponent,
  DependencyLiteralComponent,
};
```

## File: `packages/react-doctor/tests/fixtures/clean-react/package.json`
```json
{
  "name": "test-clean-react",
  "private": true,
  "dependencies": {
    "react": "^19.0.0",
    "react-dom": "^19.0.0"
  }
}
```

## File: `packages/react-doctor/tests/fixtures/clean-react/src/app.tsx`
```tsx
import { useState } from "react";

const App = () => {
  const [count, setCount] = useState(0);
  return <button onClick={() => setCount((previous) => previous + 1)}>{count}</button>;
};

export { App };
```

## File: `packages/react-doctor/tests/fixtures/component-library/package.json`
```json
{
  "name": "test-component-library",
  "private": true,
  "peerDependencies": {
    "react": "^18.0.0 || ^19.0.0",
    "react-dom": "^18.0.0 || ^19.0.0"
  }
}
```

## File: `packages/react-doctor/tests/fixtures/nested-workspaces/package.json`
```json
{
  "name": "nested-workspaces-fixture",
  "private": true,
  "workspaces": [
    "apps/*/ClientApp",
    "packages/*"
  ]
}
```

## File: `packages/react-doctor/tests/fixtures/nested-workspaces/apps/my-app/ClientApp/package.json`
```json
{
  "name": "my-app-client",
  "dependencies": {
    "react": "^19.0.0",
    "react-dom": "^19.0.0"
  }
}
```

## File: `packages/react-doctor/tests/fixtures/nested-workspaces/packages/ui/package.json`
```json
{
  "name": "ui",
  "dependencies": {
    "react": "^19.0.0"
  }
}
```

## File: `packages/react-doctor/tests/fixtures/nextjs-app/package.json`
```json
{
  "name": "test-nextjs-app",
  "private": true,
  "dependencies": {
    "next": "^15.0.0",
    "react": "^19.0.0",
    "react-dom": "^19.0.0"
  }
}
```

## File: `packages/react-doctor/tests/fixtures/nextjs-app/tsconfig.json`
```json
{
  "compilerOptions": {
    "jsx": "react-jsx",
    "strict": true,
    "target": "ESNext",
    "module": "ESNext",
    "moduleResolution": "bundler"
  }
}
```

## File: `packages/react-doctor/tests/fixtures/nextjs-app/src/app/actions.tsx`
```tsx
"use server";

export async function createUser(formData: FormData) {
  const name = formData.get("name");
  console.log("Creating user:", name);
  return { success: true };
}

export async function deleteUser(userId: string) {
  console.log("Deleting user:", userId);
  return { success: true };
}
```

## File: `packages/react-doctor/tests/fixtures/nextjs-app/src/app/layout.tsx`
```tsx
"use client";

import { useEffect, useState } from "react";

const Layout = ({ children }: { children: React.ReactNode }) => {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch("/api/layout-data")
      .then((response) => response.json())
      .then((json) => setData(json));
  }, []);

  return (
    <html>
      <body>{children}</body>
    </html>
  );
};

export default Layout;
```

## File: `packages/react-doctor/tests/fixtures/nextjs-app/src/app/page.tsx`
```tsx
"use client";

import { useEffect, useState } from "react";
import Head from "next/head";

const useSearchParams = () => new URLSearchParams();

const Page = () => {
  const params = useSearchParams();

  useEffect(() => {
    fetch("/api/data");
  }, []);

  useEffect(() => {
    router.push("/dashboard");
  }, []);

  return (
    <div>
      <img src="/photo.jpg" alt="photo" />
      <a href="/about">About</a>
      <Image fill src="/hero.jpg" alt="hero" />
      <script src="https://cdn.example.com/analytics.js" />
      <Script>{`console.log("inline")`}</Script>
      <Script src="https://cdn.polyfill.io/v3/polyfill.min.js" />
      <link href="https://fonts.googleapis.com/css2?family=Inter" rel="stylesheet" />
      <link rel="stylesheet" href="/styles/main.css" />
    </div>
  );
};

const AsyncClientComponent = async () => {
  const data = await fetch("/api/data");
  return <div>{JSON.stringify(data)}</div>;
};

const RedirectInTryCatchComponent = () => {
  try {
    redirect("/dashboard");
  } catch {
    return <div>error</div>;
  }
  return <div />;
};

const router = { push: (_path: string) => {} };
const redirect = (_path: string) => {};
const Image = (props: any) => <img {...props} />;
const Script = (props: any) => <script {...props} />;

export default Page;
export { AsyncClientComponent, RedirectInTryCatchComponent };
```

## File: `packages/react-doctor/tests/fixtures/nextjs-app/src/app/logout/route.tsx`
```tsx
import { cookies } from "next/headers";
import { redirect } from "next/navigation";
import { NextResponse } from "next/server";

export async function GET() {
  const cookieStore = await cookies();
  cookieStore.delete("session");
  redirect("/login");
  return NextResponse.json({ ok: true });
}
```

## File: `packages/website/.gitignore`
```
# See https://help.github.com/articles/ignoring-files/ for more about ignoring files.

# dependencies
/node_modules
/.pnp
.pnp.*
.yarn/*
!.yarn/patches
!.yarn/plugins
!.yarn/releases
!.yarn/versions

# testing
/coverage

# next.js
/.next/
/out/

# production
/build

# misc
.DS_Store
*.pem

# debug
npm-debug.log*
yarn-debug.log*
yarn-error.log*
.pnpm-debug.log*

# env files (can opt-in for committing if needed)
.env*

# vercel
.vercel

# typescript
*.tsbuildinfo
next-env.d.ts
```

## File: `packages/website/.oxlintrc.json`
```json
{
  "extends": ["../../.oxlintrc.json"],
  "plugins": ["typescript", "react", "import", "nextjs", "jsx-a11y"],
  "rules": {}
}
```

## File: `packages/website/next.config.ts`
```typescript
import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  rewrites: async () => {
    return {
      beforeFiles: [
        {
          source: "/",
          destination: "/llms.txt",
          has: [
            {
              type: "header",
              key: "accept",
              value: "(.*)text/markdown(.*)",
            },
          ],
        },
        {
          source: "/llm.txt",
          destination: "/llms.txt",
        },
      ],
    };
  },
};

export default nextConfig;
```

## File: `packages/website/package.json`
```json
{
  "name": "website",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start"
  },
  "dependencies": {
    "@vercel/analytics": "^1.6.1",
    "lucide-react": "^0.564.0",
    "next": "16.1.6",
    "react": "19.2.3",
    "react-dom": "19.2.3"
  },
  "devDependencies": {
    "@tailwindcss/postcss": "^4",
    "@types/node": "^20",
    "@types/react": "^19",
    "@types/react-dom": "^19",
    "tailwindcss": "^4",
    "typescript": "^5"
  }
}
```

## File: `packages/website/postcss.config.mjs`
```
const config = {
  plugins: {
    "@tailwindcss/postcss": {},
  },
};

export default config;
```

## File: `packages/website/tsconfig.json`
```json
{
  "compilerOptions": {
    "target": "ES2017",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "react-jsx",
    "incremental": true,
    "plugins": [
      {
        "name": "next"
      }
    ],
    "paths": {
      "@/*": ["./src/*"]
    }
  },
  "include": [
    "next-env.d.ts",
    "**/*.ts",
    "**/*.tsx",
    ".next/types/**/*.ts",
    ".next/dev/types/**/*.ts",
    "**/*.mts"
  ],
  "exclude": ["node_modules"]
}
```

## File: `packages/website/public/install-skill.sh`
```bash
#!/bin/bash
set -e

if [ -t 1 ]; then
  GREEN='\033[32m'
  DIM='\033[2m'
  RESET='\033[0m'
else
  GREEN=''
  DIM=''
  RESET=''
fi

SKILL_NAME="react-doctor"
INSTALLED=0

SKILL_CONTENT=$(cat << 'EOF'
---
name: react-doctor
description: Run after making React changes to catch issues early. Use when reviewing code, finishing a feature, or fixing bugs in a React project.
version: 1.0.0
---

# React Doctor

Scans your React codebase for security, performance, correctness, and architecture issues. Outputs a 0-100 score with actionable diagnostics.

## Usage

```bash
npx -y react-doctor@latest . --verbose --diff
```

## Workflow

Run after making changes to catch issues early. Fix errors first, then re-run to verify the score improved.
EOF
)

AGENTS_CONTENT=$(cat << 'EOF'
# React Doctor

Run after making React changes to catch issues early. Use when reviewing code, finishing a feature, or fixing bugs in a React project.

Scans your React codebase for security, performance, correctness, and architecture issues. Outputs a 0-100 score with actionable diagnostics.

## Usage

```bash
npx -y react-doctor@latest . --verbose --diff
```

## Workflow

Run after making changes to catch issues early. Fix errors first, then re-run to verify the score improved.
EOF
)

echo "Installing React Doctor skill..."
echo ""

# Claude Code
if [ -d "$HOME/.claude" ]; then
  SKILL_DIR="$HOME/.claude/skills/$SKILL_NAME"
  mkdir -p "$SKILL_DIR"
  printf '%s\n' "$SKILL_CONTENT" > "$SKILL_DIR/SKILL.md"
  printf '%s\n' "$AGENTS_CONTENT" > "$SKILL_DIR/AGENTS.md"
  printf "${GREEN}✔${RESET} Claude Code\n"
  INSTALLED=$((INSTALLED + 1))
fi

# Amp Code
if [ -d "$HOME/.amp" ]; then
  SKILL_DIR="$HOME/.config/amp/skills/$SKILL_NAME"
  mkdir -p "$SKILL_DIR"
  printf '%s\n' "$SKILL_CONTENT" > "$SKILL_DIR/SKILL.md"
  printf '%s\n' "$AGENTS_CONTENT" > "$SKILL_DIR/AGENTS.md"
  printf "${GREEN}✔${RESET} Amp Code\n"
  INSTALLED=$((INSTALLED + 1))
fi

# Cursor
if [ -d "$HOME/.cursor" ]; then
  SKILL_DIR="$HOME/.cursor/skills/$SKILL_NAME"
  mkdir -p "$SKILL_DIR"
  printf '%s\n' "$SKILL_CONTENT" > "$SKILL_DIR/SKILL.md"
  printf '%s\n' "$AGENTS_CONTENT" > "$SKILL_DIR/AGENTS.md"
  printf "${GREEN}✔${RESET} Cursor\n"
  INSTALLED=$((INSTALLED + 1))
fi

# OpenCode
if command -v opencode &> /dev/null || [ -d "$HOME/.config/opencode" ]; then
  SKILL_DIR="$HOME/.config/opencode/skills/$SKILL_NAME"
  mkdir -p "$SKILL_DIR"
  printf '%s\n' "$SKILL_CONTENT" > "$SKILL_DIR/SKILL.md"
  printf '%s\n' "$AGENTS_CONTENT" > "$SKILL_DIR/AGENTS.md"
  printf "${GREEN}✔${RESET} OpenCode\n"
  INSTALLED=$((INSTALLED + 1))
fi

# Windsurf
MARKER="# React Doctor"
if [ -d "$HOME/.codeium" ] || [ -d "$HOME/Library/Application Support/Windsurf" ]; then
  mkdir -p "$HOME/.codeium/windsurf/memories"
  RULES_FILE="$HOME/.codeium/windsurf/memories/global_rules.md"
  if [ -f "$RULES_FILE" ] && grep -q "$MARKER" "$RULES_FILE"; then
    printf "${GREEN}✔${RESET} Windsurf ${DIM}(already installed)${RESET}\n"
  else
    if [ -f "$RULES_FILE" ]; then
      echo "" >> "$RULES_FILE"
    fi
    echo "$MARKER" >> "$RULES_FILE"
    echo "" >> "$RULES_FILE"
    printf '%s\n' "$SKILL_CONTENT" >> "$RULES_FILE"
    printf "${GREEN}✔${RESET} Windsurf\n"
  fi
  INSTALLED=$((INSTALLED + 1))
fi

# Antigravity
if command -v agy &> /dev/null || [ -d "$HOME/.gemini/antigravity" ]; then
  SKILL_DIR="$HOME/.gemini/antigravity/skills/$SKILL_NAME"
  mkdir -p "$SKILL_DIR"
  printf '%s\n' "$SKILL_CONTENT" > "$SKILL_DIR/SKILL.md"
  printf '%s\n' "$AGENTS_CONTENT" > "$SKILL_DIR/AGENTS.md"
  printf "${GREEN}✔${RESET} Antigravity\n"
  INSTALLED=$((INSTALLED + 1))
fi

# Gemini CLI
if command -v gemini &> /dev/null || [ -d "$HOME/.gemini" ]; then
  mkdir -p "$HOME/.gemini/skills/$SKILL_NAME"
  printf '%s\n' "$SKILL_CONTENT" > "$HOME/.gemini/skills/$SKILL_NAME/SKILL.md"
  printf '%s\n' "$AGENTS_CONTENT" > "$HOME/.gemini/skills/$SKILL_NAME/AGENTS.md"
  printf "${GREEN}✔${RESET} Gemini CLI\n"
  INSTALLED=$((INSTALLED + 1))
fi

# Codex
if command -v codex &> /dev/null || [ -d "$HOME/.codex" ]; then
  SKILL_DIR="$HOME/.codex/skills/$SKILL_NAME"
  mkdir -p "$SKILL_DIR"
  mkdir -p "$SKILL_DIR/agents"
  printf '%s\n' "$SKILL_CONTENT" > "$SKILL_DIR/SKILL.md"
  printf '%s\n' "$AGENTS_CONTENT" > "$SKILL_DIR/AGENTS.md"
  cat > "$SKILL_DIR/agents/openai.yaml" << 'YAMLEOF'
interface:
  display_name: "react-doctor"
  short_description: "Diagnose and fix React codebase health issues"
YAMLEOF
  printf "${GREEN}✔${RESET} Codex\n"
  INSTALLED=$((INSTALLED + 1))
fi

# Project-level .agents/
AGENTS_DIR=".agents/$SKILL_NAME"
mkdir -p "$AGENTS_DIR"
printf '%s\n' "$SKILL_CONTENT" > "$AGENTS_DIR/SKILL.md"
printf '%s\n' "$AGENTS_CONTENT" > "$AGENTS_DIR/AGENTS.md"
printf "${GREEN}✔${RESET} .agents/\n"
INSTALLED=$((INSTALLED + 1))

echo ""
if [ $INSTALLED -eq 0 ]; then
  echo "No supported tools detected."
  echo ""
  echo "Install one of these first:"
  echo "  • Ami: https://ami.dev"
  echo "  • Amp Code: https://ampcode.com"
  echo "  • Antigravity: https://antigravity.google"
  echo "  • Claude Code: https://claude.ai/code"
  echo "  • Codex: https://codex.openai.com"
  echo "  • Cursor: https://cursor.com"
  echo "  • Gemini CLI: https://github.com/google-gemini/gemini-cli"
  echo "  • OpenCode: https://opencode.ai"
  echo "  • Windsurf: https://codeium.com/windsurf"
  exit 1
fi

echo "Done! The skill will activate when working on React projects."
```

## File: `packages/website/public/llms.txt`
```
# React Doctor

Diagnose React codebase health. Scans for security, performance, correctness, and architecture issues, then outputs a 0–100 score with actionable diagnostics.

## Usage

Run this at your project root:

```bash
npx -y react-doctor@latest .
```

Use `--verbose` to see affected files and line numbers:

```bash
npx -y react-doctor@latest . --verbose
```

Use `--diff` to scan only changed files (branch changes or uncommitted changes):

```bash
npx -y react-doctor@latest . --verbose --diff
```

Use `--score` to output only the numeric score:

```bash
npx -y react-doctor@latest . --score
```

Use `-y` to skip prompts (required for non-interactive environments like CI or coding agents):

```bash
npx -y react-doctor@latest . -y
```

## Options

```
Usage: react-doctor [directory] [options]

Options:
  -v, --version     display the version number
  --no-lint         skip linting
  --no-dead-code    skip dead code detection
  --verbose         show file details per rule
  --score           output only the score
  -y, --yes         skip prompts, scan all workspace projects
  --project <name>  select workspace project (comma-separated for multiple)
  --diff [base]     scan only files changed vs base branch or uncommitted changes
  --fix             open Ami to auto-fix all issues
  -h, --help        display help for command
```
```

## File: `packages/website/src/app/globals.css`
```css
@import "tailwindcss";

@theme {
  --font-mono: var(--font-mono), ui-monospace, monospace;
  --animate-fade-in: fade-in 200ms ease-out both;
}

@keyframes fade-in {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

html {
  background: #0a0a0a;
  height: 100%;
  scrollbar-width: thin;
  scrollbar-color: #333 transparent;
}

body {
  height: 100%;
}
```

## File: `packages/website/src/app/layout.tsx`
```tsx
import type { Metadata } from "next";
import { IBM_Plex_Mono } from "next/font/google";
import { Analytics } from "@vercel/analytics/next";
import "./globals.css";

const ibmPlexMono = IBM_Plex_Mono({
  variable: "--font-mono",
  subsets: ["latin"],
  weight: ["400", "500"],
});

const SITE_URL = "https://www.react.doctor";
const TWITTER_IMAGE_PATH = "/react-doctor-og-banner.svg";

export const metadata: Metadata = {
  metadataBase: new URL(SITE_URL),
  title: "React Doctor",
  description: "Let coding agents diagnose and fix your React code.",
  twitter: {
    card: "summary_large_image",
    images: [TWITTER_IMAGE_PATH],
  },
  icons: { icon: "/react-doctor-icon.svg" },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={`${ibmPlexMono.variable} antialiased`}>
        {children}
        <Analytics />
      </body>
    </html>
  );
}
```

## File: `packages/website/src/app/page.tsx`
```tsx
import Terminal from "@/components/terminal";

const Home = () => <Terminal />;

export default Home;
```

## File: `packages/website/src/app/api/estimate-score/route.ts`
```typescript
const PERFECT_SCORE = 100;
const ERROR_RULE_PENALTY = 1.5;
const WARNING_RULE_PENALTY = 0.75;
const SCORE_GOOD_THRESHOLD = 75;
const SCORE_OK_THRESHOLD = 50;

const ERROR_ESTIMATED_FIX_RATE = 0.85;
const WARNING_ESTIMATED_FIX_RATE = 0.8;

interface DiagnosticInput {
  filePath: string;
  plugin: string;
  rule: string;
  severity: "error" | "warning";
  message: string;
  help: string;
  line: number;
  column: number;
  category: string;
  weight?: number;
}

const getScoreLabel = (score: number): string => {
  if (score >= SCORE_GOOD_THRESHOLD) return "Great";
  if (score >= SCORE_OK_THRESHOLD) return "Needs work";
  return "Critical";
};

const scoreFromRuleCounts = (errorRuleCount: number, warningRuleCount: number): number => {
  const penalty = errorRuleCount * ERROR_RULE_PENALTY + warningRuleCount * WARNING_RULE_PENALTY;
  return Math.max(0, Math.round(PERFECT_SCORE - penalty));
};

const countUniqueRules = (
  diagnostics: DiagnosticInput[],
): { errorRuleCount: number; warningRuleCount: number } => {
  const errorRules = new Set<string>();
  const warningRules = new Set<string>();

  for (const diagnostic of diagnostics) {
    const ruleKey = `${diagnostic.plugin}/${diagnostic.rule}`;
    if (diagnostic.severity === "error") {
      errorRules.add(ruleKey);
    } else {
      warningRules.add(ruleKey);
    }
  }

  return { errorRuleCount: errorRules.size, warningRuleCount: warningRules.size };
};

const isValidDiagnostic = (value: unknown): value is DiagnosticInput => {
  if (typeof value !== "object" || value === null) return false;
  const record = value as Record<string, unknown>;
  return (
    typeof record.filePath === "string" &&
    typeof record.plugin === "string" &&
    typeof record.rule === "string" &&
    (record.severity === "error" || record.severity === "warning") &&
    typeof record.message === "string" &&
    typeof record.help === "string" &&
    typeof record.line === "number" &&
    typeof record.column === "number" &&
    typeof record.category === "string"
  );
};

const CORS_HEADERS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type",
};

export const OPTIONS = (): Response => new Response(null, { status: 204, headers: CORS_HEADERS });

export const POST = async (request: Request): Promise<Response> => {
  const body = await request.json().catch(() => null);
  console.log("[/api/estimate-score]", JSON.stringify(body));

  if (!body || !Array.isArray(body.diagnostics)) {
    return Response.json(
      { error: "Request body must contain a 'diagnostics' array" },
      { status: 400, headers: CORS_HEADERS },
    );
  }

  const isValidPayload = body.diagnostics.every((entry: unknown) => isValidDiagnostic(entry));

  if (!isValidPayload) {
    return Response.json(
      {
        error:
          "Each diagnostic must have 'filePath', 'plugin', 'rule', 'severity', 'message', 'help', 'line', 'column', and 'category'",
      },
      { status: 400, headers: CORS_HEADERS },
    );
  }

  const { errorRuleCount, warningRuleCount } = countUniqueRules(body.diagnostics);

  const currentScore = scoreFromRuleCounts(errorRuleCount, warningRuleCount);

  const estimatedUnfixedErrorRuleCount = Math.round(
    errorRuleCount * (1 - ERROR_ESTIMATED_FIX_RATE),
  );
  const estimatedUnfixedWarningRuleCount = Math.round(
    warningRuleCount * (1 - WARNING_ESTIMATED_FIX_RATE),
  );
  const estimatedScore = scoreFromRuleCounts(
    estimatedUnfixedErrorRuleCount,
    estimatedUnfixedWarningRuleCount,
  );

  return Response.json(
    {
      currentScore,
      currentLabel: getScoreLabel(currentScore),
      estimatedScore,
      estimatedLabel: getScoreLabel(estimatedScore),
    },
    { headers: CORS_HEADERS },
  );
};
```

## File: `packages/website/src/app/api/score/route.ts`
```typescript
const PERFECT_SCORE = 100;
const ERROR_RULE_PENALTY = 1.5;
const WARNING_RULE_PENALTY = 0.75;
const SCORE_GOOD_THRESHOLD = 75;
const SCORE_OK_THRESHOLD = 50;

interface DiagnosticInput {
  filePath: string;
  plugin: string;
  rule: string;
  severity: "error" | "warning";
  message: string;
  help: string;
  line: number;
  column: number;
  category: string;
  weight?: number;
}

const getScoreLabel = (score: number): string => {
  if (score >= SCORE_GOOD_THRESHOLD) return "Great";
  if (score >= SCORE_OK_THRESHOLD) return "Needs work";
  return "Critical";
};

const calculateScore = (diagnostics: DiagnosticInput[]): number => {
  if (diagnostics.length === 0) return PERFECT_SCORE;

  const errorRules = new Set<string>();
  const warningRules = new Set<string>();

  for (const diagnostic of diagnostics) {
    const ruleKey = `${diagnostic.plugin}/${diagnostic.rule}`;
    if (diagnostic.severity === "error") {
      errorRules.add(ruleKey);
    } else {
      warningRules.add(ruleKey);
    }
  }

  const penalty = errorRules.size * ERROR_RULE_PENALTY + warningRules.size * WARNING_RULE_PENALTY;

  return Math.max(0, Math.round(PERFECT_SCORE - penalty));
};

const isValidDiagnostic = (value: unknown): value is DiagnosticInput => {
  if (typeof value !== "object" || value === null) return false;
  const record = value as Record<string, unknown>;
  return (
    typeof record.filePath === "string" &&
    typeof record.plugin === "string" &&
    typeof record.rule === "string" &&
    (record.severity === "error" || record.severity === "warning") &&
    typeof record.message === "string" &&
    typeof record.help === "string" &&
    typeof record.line === "number" &&
    typeof record.column === "number" &&
    typeof record.category === "string"
  );
};

const CORS_HEADERS = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
  "Access-Control-Allow-Headers": "Content-Type",
};

export const OPTIONS = (): Response => new Response(null, { status: 204, headers: CORS_HEADERS });

export const POST = async (request: Request): Promise<Response> => {
  const body = await request.json().catch(() => null);
  console.log("[/api/score]", JSON.stringify(body));

  if (!body || !Array.isArray(body.diagnostics)) {
    return Response.json(
      { error: "Request body must contain a 'diagnostics' array" },
      { status: 400, headers: CORS_HEADERS },
    );
  }

  const isValidPayload = body.diagnostics.every((entry: unknown) => isValidDiagnostic(entry));

  if (!isValidPayload) {
    return Response.json(
      {
        error:
          "Each diagnostic must have 'filePath', 'plugin', 'rule', 'severity', 'message', 'help', 'line', 'column', and 'category'",
      },
      { status: 400, headers: CORS_HEADERS },
    );
  }

  const score = calculateScore(body.diagnostics);

  return Response.json({ score, label: getScoreLabel(score) }, { headers: CORS_HEADERS });
};
```

## File: `packages/website/src/app/install-skill/route.ts`
```typescript
const INSTALL_SCRIPT = `#!/bin/bash
set -e

if [ -t 1 ]; then
  GREEN='\\033[32m'
  DIM='\\033[2m'
  RESET='\\033[0m'
else
  GREEN=''
  DIM=''
  RESET=''
fi

SKILL_NAME="react-doctor"
INSTALLED=0

SKILL_CONTENT=$(cat << 'EOF'
---
name: react-doctor
description: Run after making React changes to catch issues early. Use when reviewing code, finishing a feature, or fixing bugs in a React project.
version: 1.0.0
---

# React Doctor

Scans your React codebase for security, performance, correctness, and architecture issues. Outputs a 0-100 score with actionable diagnostics.

## Usage

\\\`\\\`\\\`bash
npx -y react-doctor@latest . --verbose --diff
\\\`\\\`\\\`

## Workflow

Run after making changes to catch issues early. Fix errors first, then re-run to verify the score improved.
EOF
)

AGENTS_CONTENT=$(cat << 'EOF'
# React Doctor

Run after making React changes to catch issues early. Use when reviewing code, finishing a feature, or fixing bugs in a React project.

Scans your React codebase for security, performance, correctness, and architecture issues. Outputs a 0-100 score with actionable diagnostics.

## Usage

\\\`\\\`\\\`bash
npx -y react-doctor@latest . --verbose --diff
\\\`\\\`\\\`

## Workflow

Run after making changes to catch issues early. Fix errors first, then re-run to verify the score improved.
EOF
)

echo "Installing React Doctor skill..."
echo ""

# Claude Code
if [ -d "$HOME/.claude" ]; then
  SKILL_DIR="$HOME/.claude/skills/$SKILL_NAME"
  mkdir -p "$SKILL_DIR"
  printf '%s\\n' "$SKILL_CONTENT" > "$SKILL_DIR/SKILL.md"
  printf '%s\\n' "$AGENTS_CONTENT" > "$SKILL_DIR/AGENTS.md"
  printf "\${GREEN}✔\${RESET} Claude Code\\n"
  INSTALLED=$((INSTALLED + 1))
fi

# Amp Code
if [ -d "$HOME/.amp" ]; then
  SKILL_DIR="$HOME/.config/amp/skills/$SKILL_NAME"
  mkdir -p "$SKILL_DIR"
  printf '%s\\n' "$SKILL_CONTENT" > "$SKILL_DIR/SKILL.md"
  printf '%s\\n' "$AGENTS_CONTENT" > "$SKILL_DIR/AGENTS.md"
  printf "\${GREEN}✔\${RESET} Amp Code\\n"
  INSTALLED=$((INSTALLED + 1))
fi

# Cursor
if [ -d "$HOME/.cursor" ]; then
  SKILL_DIR="$HOME/.cursor/skills/$SKILL_NAME"
  mkdir -p "$SKILL_DIR"
  printf '%s\\n' "$SKILL_CONTENT" > "$SKILL_DIR/SKILL.md"
  printf '%s\\n' "$AGENTS_CONTENT" > "$SKILL_DIR/AGENTS.md"
  printf "\${GREEN}✔\${RESET} Cursor\\n"
  INSTALLED=$((INSTALLED + 1))
fi

# OpenCode
if command -v opencode &> /dev/null || [ -d "$HOME/.config/opencode" ]; then
  SKILL_DIR="$HOME/.config/opencode/skills/$SKILL_NAME"
  mkdir -p "$SKILL_DIR"
  printf '%s\\n' "$SKILL_CONTENT" > "$SKILL_DIR/SKILL.md"
  printf '%s\\n' "$AGENTS_CONTENT" > "$SKILL_DIR/AGENTS.md"
  printf "\${GREEN}✔\${RESET} OpenCode\\n"
  INSTALLED=$((INSTALLED + 1))
fi

# Windsurf
MARKER="# React Doctor"
if [ -d "$HOME/.codeium" ] || [ -d "$HOME/Library/Application Support/Windsurf" ]; then
  mkdir -p "$HOME/.codeium/windsurf/memories"
  RULES_FILE="$HOME/.codeium/windsurf/memories/global_rules.md"
  if [ -f "$RULES_FILE" ] && grep -q "$MARKER" "$RULES_FILE"; then
    printf "\${GREEN}✔\${RESET} Windsurf \${DIM}(already installed)\${RESET}\\n"
  else
    if [ -f "$RULES_FILE" ]; then
      echo "" >> "$RULES_FILE"
    fi
    echo "$MARKER" >> "$RULES_FILE"
    echo "" >> "$RULES_FILE"
    printf '%s\\n' "$SKILL_CONTENT" >> "$RULES_FILE"
    printf "\${GREEN}✔\${RESET} Windsurf\\n"
  fi
  INSTALLED=$((INSTALLED + 1))
fi

# Antigravity
if command -v agy &> /dev/null || [ -d "$HOME/.gemini/antigravity" ]; then
  SKILL_DIR="$HOME/.gemini/antigravity/skills/$SKILL_NAME"
  mkdir -p "$SKILL_DIR"
  printf '%s\\n' "$SKILL_CONTENT" > "$SKILL_DIR/SKILL.md"
  printf '%s\\n' "$AGENTS_CONTENT" > "$SKILL_DIR/AGENTS.md"
  printf "\${GREEN}✔\${RESET} Antigravity\\n"
  INSTALLED=$((INSTALLED + 1))
fi

# Gemini CLI
if command -v gemini &> /dev/null || [ -d "$HOME/.gemini" ]; then
  mkdir -p "$HOME/.gemini/skills/$SKILL_NAME"
  printf '%s\\n' "$SKILL_CONTENT" > "$HOME/.gemini/skills/$SKILL_NAME/SKILL.md"
  printf '%s\\n' "$AGENTS_CONTENT" > "$HOME/.gemini/skills/$SKILL_NAME/AGENTS.md"
  printf "\${GREEN}✔\${RESET} Gemini CLI\\n"
  INSTALLED=$((INSTALLED + 1))
fi

# Codex
if command -v codex &> /dev/null || [ -d "$HOME/.codex" ]; then
  SKILL_DIR="$HOME/.codex/skills/$SKILL_NAME"
  mkdir -p "$SKILL_DIR"
  mkdir -p "$SKILL_DIR/agents"
  printf '%s\\n' "$SKILL_CONTENT" > "$SKILL_DIR/SKILL.md"
  printf '%s\\n' "$AGENTS_CONTENT" > "$SKILL_DIR/AGENTS.md"
  cat > "$SKILL_DIR/agents/openai.yaml" << 'YAMLEOF'
interface:
  display_name: "react-doctor"
  short_description: "Diagnose and fix React codebase health issues"
YAMLEOF
  printf "\${GREEN}✔\${RESET} Codex\\n"
  INSTALLED=$((INSTALLED + 1))
fi

# Project-level .agents/
AGENTS_DIR=".agents/$SKILL_NAME"
mkdir -p "$AGENTS_DIR"
printf '%s\\n' "$SKILL_CONTENT" > "$AGENTS_DIR/SKILL.md"
printf '%s\\n' "$AGENTS_CONTENT" > "$AGENTS_DIR/AGENTS.md"
printf "\${GREEN}✔\${RESET} .agents/\\n"
INSTALLED=$((INSTALLED + 1))

echo ""
if [ $INSTALLED -eq 0 ]; then
  echo "No supported tools detected."
  echo ""
  echo "Install one of these first:"
  echo "  • Ami: https://ami.dev"
  echo "  • Amp Code: https://ampcode.com"
  echo "  • Antigravity: https://antigravity.google"
  echo "  • Claude Code: https://claude.ai/code"
  echo "  • Codex: https://codex.openai.com"
  echo "  • Cursor: https://cursor.com"
  echo "  • Gemini CLI: https://github.com/google-gemini/gemini-cli"
  echo "  • OpenCode: https://opencode.ai"
  echo "  • Windsurf: https://codeium.com/windsurf"
  exit 1
fi

echo "Done! The skill will activate when working on React projects."
`;

export const GET = (): Response =>
  new Response(INSTALL_SCRIPT, {
    headers: {
      "Content-Type": "text/plain; charset=utf-8",
      "Content-Disposition": 'attachment; filename="install.sh"',
    },
  });
```

## File: `packages/website/src/app/leaderboard/leaderboard-entries.ts`
```typescript
interface LeaderboardEntry {
  name: string;
  githubUrl: string;
  packageName: string;
  score: number;
  errorCount: number;
  warningCount: number;
  fileCount: number;
}

const buildShareUrl = (entry: LeaderboardEntry): string => {
  const searchParams = new URLSearchParams({
    p: entry.packageName,
    s: String(entry.score),
    e: String(entry.errorCount),
    w: String(entry.warningCount),
    f: String(entry.fileCount),
  });
  return `/share?${searchParams.toString()}`;
};

const RAW_ENTRIES: LeaderboardEntry[] = [
  {
    name: "tldraw",
    githubUrl: "https://github.com/tldraw/tldraw",
    packageName: "tldraw",
    score: 84,
    errorCount: 98,
    warningCount: 139,
    fileCount: 40,
  },
  {
    name: "excalidraw",
    githubUrl: "https://github.com/excalidraw/excalidraw",
    packageName: "@excalidraw/excalidraw",
    score: 84,
    errorCount: 2,
    warningCount: 196,
    fileCount: 80,
  },
  {
    name: "twenty",
    githubUrl: "https://github.com/twentyhq/twenty",
    packageName: "twenty-front",
    score: 78,
    errorCount: 99,
    warningCount: 293,
    fileCount: 268,
  },
  {
    name: "plane",
    githubUrl: "https://github.com/makeplane/plane",
    packageName: "web",
    score: 78,
    errorCount: 7,
    warningCount: 525,
    fileCount: 292,
  },
  {
    name: "formbricks",
    githubUrl: "https://github.com/formbricks/formbricks",
    packageName: "@formbricks/web",
    score: 75,
    errorCount: 15,
    warningCount: 389,
    fileCount: 242,
  },
  {
    name: "posthog",
    githubUrl: "https://github.com/PostHog/posthog",
    packageName: "@posthog/frontend",
    score: 72,
    errorCount: 82,
    warningCount: 1177,
    fileCount: 585,
  },
  {
    name: "supabase",
    githubUrl: "https://github.com/supabase/supabase",
    packageName: "studio",
    score: 69,
    errorCount: 74,
    warningCount: 1087,
    fileCount: 566,
  },
  {
    name: "onlook",
    githubUrl: "https://github.com/onlook-dev/onlook",
    packageName: "@onlook/web-client",
    score: 69,
    errorCount: 64,
    warningCount: 418,
    fileCount: 178,
  },
  {
    name: "payload",
    githubUrl: "https://github.com/payloadcms/payload",
    packageName: "@payloadcms/ui",
    score: 68,
    errorCount: 139,
    warningCount: 408,
    fileCount: 298,
  },
  {
    name: "sentry",
    githubUrl: "https://github.com/getsentry/sentry",
    packageName: "sentry",
    score: 64,
    errorCount: 94,
    warningCount: 1345,
    fileCount: 818,
  },
  {
    name: "cal.com",
    githubUrl: "https://github.com/calcom/cal.com",
    packageName: "@calcom/web",
    score: 63,
    errorCount: 31,
    warningCount: 558,
    fileCount: 311,
  },
  {
    name: "dub",
    githubUrl: "https://github.com/dubinc/dub",
    packageName: "web",
    score: 62,
    errorCount: 52,
    warningCount: 966,
    fileCount: 457,
  },
  {
    name: "nodejs.org",
    githubUrl: "https://github.com/nodejs/node",
    packageName: "@node-core/website",
    score: 88,
    errorCount: 9,
    warningCount: 169,
    fileCount: 169,
  },
];

export interface ResolvedLeaderboardEntry extends LeaderboardEntry {
  shareUrl: string;
}

export const LEADERBOARD_ENTRIES: ResolvedLeaderboardEntry[] = RAW_ENTRIES.sort(
  (entryA, entryB) => entryB.score - entryA.score,
).map((entry) => ({ ...entry, shareUrl: buildShareUrl(entry) }));
```

## File: `packages/website/src/app/leaderboard/page.tsx`
```tsx
import type { Metadata } from "next";
import Link from "next/link";
import { LEADERBOARD_ENTRIES, type ResolvedLeaderboardEntry } from "./leaderboard-entries";

const PERFECT_SCORE = 100;
const SCORE_GOOD_THRESHOLD = 75;
const SCORE_OK_THRESHOLD = 50;
const SCORE_BAR_WIDTH = 20;
const COMMAND = "npx -y react-doctor@latest .";
const CONTRIBUTE_URL =
  "https://github.com/millionco/react-doctor/edit/main/packages/website/src/app/leaderboard/leaderboard-entries.ts";

const getScoreColorClass = (score: number): string => {
  if (score >= SCORE_GOOD_THRESHOLD) return "text-green-400";
  if (score >= SCORE_OK_THRESHOLD) return "text-yellow-500";
  return "text-red-400";
};

const getDoctorFace = (score: number): [string, string] => {
  if (score >= SCORE_GOOD_THRESHOLD) return ["◠ ◠", " ▽ "];
  if (score >= SCORE_OK_THRESHOLD) return ["• •", " ─ "];
  return ["x x", " ▽ "];
};

const ScoreBar = ({ score }: { score: number }) => {
  const filledCount = Math.round((score / PERFECT_SCORE) * SCORE_BAR_WIDTH);
  const emptyCount = SCORE_BAR_WIDTH - filledCount;
  const colorClass = getScoreColorClass(score);

  return (
    <span className="text-xs sm:text-sm">
      <span className={colorClass}>{"█".repeat(filledCount)}</span>
      <span className="text-neutral-700">{"░".repeat(emptyCount)}</span>
    </span>
  );
};

const LeaderboardRow = ({ entry, rank }: { entry: ResolvedLeaderboardEntry; rank: number }) => {
  const colorClass = getScoreColorClass(entry.score);

  return (
    <div className="group grid items-center border-b border-white/5 py-2 transition-colors hover:bg-white/2 sm:py-2.5 grid-cols-[2rem_1fr_auto] sm:grid-cols-[2.5rem_7rem_1fr_auto]">
      <span className="text-right text-neutral-600">{rank}</span>

      <a
        href={entry.githubUrl}
        target="_blank"
        rel="noreferrer"
        className="ml-2 truncate text-white transition-colors hover:text-blue-400 sm:ml-4"
      >
        {entry.name}
      </a>

      <span className="hidden sm:inline">
        <ScoreBar score={entry.score} />
      </span>

      <Link href={entry.shareUrl} className="ml-4 text-right transition-colors hover:underline">
        <span className={`${colorClass} font-medium`}>{entry.score}</span>
        <span className="text-neutral-600">/{PERFECT_SCORE}</span>
      </Link>
    </div>
  );
};

export const metadata: Metadata = {
  title: "Leaderboard - React Doctor",
  description: "Scores for popular open-source React projects, diagnosed by React Doctor.",
};

const LeaderboardPage = () => {
  const topScore = LEADERBOARD_ENTRIES[0]?.score ?? 0;
  const [eyes, mouth] = getDoctorFace(topScore);
  const topScoreColor = getScoreColorClass(topScore);

  return (
    <div className="mx-auto min-h-screen w-full max-w-3xl bg-[#0a0a0a] p-6 pb-32 font-mono text-base leading-relaxed text-neutral-300 sm:p-8 sm:pb-40 sm:text-lg">
      <div className="mb-8">
        <Link
          href="/"
          className="inline-flex items-center gap-2 text-neutral-500 transition-colors hover:text-neutral-300"
        >
          <img src="/favicon.svg" alt="React Doctor" width={20} height={20} />
          <span>react-doctor</span>
        </Link>
      </div>

      <div className="mb-2">
        <pre className={`${topScoreColor} leading-tight`}>
          {`  ┌─────┐\n  │ ${eyes} │\n  │ ${mouth} │\n  └─────┘`}
        </pre>
      </div>

      <div className="mb-1 text-xl text-white">Leaderboard</div>
      <div className="mb-8 text-neutral-500">Scores for popular open-source React projects.</div>

      <div className="mb-8">
        {LEADERBOARD_ENTRIES.map((entry, index) => (
          <LeaderboardRow key={entry.name} entry={entry} rank={index + 1} />
        ))}
      </div>

      <div className="min-h-[1.4em]" />

      <div className="text-neutral-500">Run it on your codebase:</div>
      <div className="mt-2">
        <span className="border border-white/20 px-3 py-1.5 text-white">{COMMAND}</span>
      </div>

      <div className="min-h-[1.4em]" />
      <div className="min-h-[1.4em]" />

      <div className="text-neutral-500">
        {"+ "}
        <a
          href={CONTRIBUTE_URL}
          target="_blank"
          rel="noreferrer"
          className="text-green-400 transition-colors hover:text-green-300 hover:underline"
        >
          Add your project
        </a>
        <span className="text-neutral-600">{" — open a PR to leaderboard-entries.ts"}</span>
      </div>
    </div>
  );
};

export default LeaderboardPage;
```

## File: `packages/website/src/app/open/page.tsx`
```tsx
"use client";

import { useSearchParams } from "next/navigation";
import { Suspense, useEffect, useState } from "react";

const AMI_DEEPLINK_PREFIX = "ami://open-project";
const AMI_RELEASES_URL = "https://github.com/millionco/ami-releases/releases";
const REDIRECT_DELAY_MS = 500;

const OpenPageContent = () => {
  const searchParams = useSearchParams();
  const deeplink = `${AMI_DEEPLINK_PREFIX}?${searchParams.toString()}`;
  const [didAttemptOpen, setDidAttemptOpen] = useState(false);

  useEffect(() => {
    const timeout = setTimeout(() => {
      window.location.href = deeplink;
      setDidAttemptOpen(true);
    }, REDIRECT_DELAY_MS);

    return () => clearTimeout(timeout);
  }, [deeplink]);

  return (
    <div className="mx-auto flex min-h-screen w-full max-w-3xl flex-col items-center justify-center bg-[#0a0a0a] p-6 font-mono text-base leading-relaxed text-neutral-300 sm:p-8 sm:text-lg">
      <pre className="mb-6 text-green-400 leading-tight">
        {`  ┌─────┐\n  │ ◠ ◠ │\n  │  ▽  │\n  └─────┘`}
      </pre>

      <div className="mb-8 text-center">
        <h1 className="mb-2 text-xl text-white">Opening Ami...</h1>
        <p className="text-neutral-500">
          {didAttemptOpen
            ? "If Ami didn\u2019t open, it may not be installed."
            : "Redirecting to Ami to fix react-doctor issues."}
        </p>
      </div>

      {didAttemptOpen && (
        <div className="flex flex-col items-center gap-4">
          <a
            href={AMI_RELEASES_URL}
            target="_blank"
            rel="noreferrer"
            className="inline-flex items-center gap-2 border border-white/20 bg-white px-4 py-2 text-black transition-all hover:bg-white/90 active:scale-[0.98]"
          >
            Download Ami
          </a>

          <div className="mt-4 text-center">
            <p className="mb-2 text-sm text-neutral-500">Or open manually:</p>
            <a
              href={deeplink}
              className="break-all text-sm text-blue-400 underline underline-offset-2 hover:text-blue-300"
            >
              Open deeplink
            </a>
          </div>
        </div>
      )}
    </div>
  );
};

const OpenPage = () => (
  <Suspense
    fallback={
      <div className="flex min-h-screen items-center justify-center bg-[#0a0a0a] font-mono text-neutral-500">
        Loading...
      </div>
    }
  >
    <OpenPageContent />
  </Suspense>
);

export default OpenPage;
```

## File: `packages/website/src/app/share/animated-score.tsx`
```tsx
"use client";

import { useEffect, useState } from "react";

const PERFECT_SCORE = 100;
const SCORE_GOOD_THRESHOLD = 75;
const SCORE_OK_THRESHOLD = 50;
const SCORE_BAR_WIDTH = 30;
const SCORE_FRAME_COUNT = 20;
const SCORE_FRAME_DELAY_MS = 30;

const easeOutCubic = (progress: number) => 1 - Math.pow(1 - progress, 3);

const getScoreColorClass = (score: number): string => {
  if (score >= SCORE_GOOD_THRESHOLD) return "text-green-400";
  if (score >= SCORE_OK_THRESHOLD) return "text-yellow-500";
  return "text-red-400";
};

const getScoreLabel = (score: number): string => {
  if (score >= SCORE_GOOD_THRESHOLD) return "Great";
  if (score >= SCORE_OK_THRESHOLD) return "Needs work";
  return "Critical";
};

const ScoreBar = ({ score }: { score: number }) => {
  const filledCount = Math.round((score / PERFECT_SCORE) * SCORE_BAR_WIDTH);
  const emptyCount = SCORE_BAR_WIDTH - filledCount;
  const colorClass = getScoreColorClass(score);

  return (
    <>
      <span className={colorClass}>{"\u2588".repeat(filledCount)}</span>
      <span className="text-neutral-600">{"\u2591".repeat(emptyCount)}</span>
    </>
  );
};

const AnimatedScore = ({ targetScore }: { targetScore: number }) => {
  const [animatedScore, setAnimatedScore] = useState(0);

  useEffect(() => {
    let cancelled = false;
    let frame = 0;

    const animate = () => {
      if (cancelled || frame > SCORE_FRAME_COUNT) return;
      setAnimatedScore(Math.round(easeOutCubic(frame / SCORE_FRAME_COUNT) * targetScore));
      frame++;
      setTimeout(animate, SCORE_FRAME_DELAY_MS);
    };

    animate();
    return () => {
      cancelled = true;
    };
  }, [targetScore]);

  const colorClass = getScoreColorClass(animatedScore);

  return (
    <>
      <div className="mb-2 pl-2">
        <span className={colorClass}>{animatedScore}</span>
        {` / ${PERFECT_SCORE}  `}
        <span className={colorClass}>{getScoreLabel(animatedScore)}</span>
      </div>
      <div className="mb-6 pl-2">
        <ScoreBar score={animatedScore} />
      </div>
    </>
  );
};

export default AnimatedScore;
```

## File: `packages/website/src/app/share/badge-snippet.tsx`
```tsx
"use client";

import { useState } from "react";

const COPY_FEEDBACK_DURATION_MS = 2000;
const BADGE_BASE_URL = "https://www.react.doctor/share/badge";
const SHARE_BASE_URL = "https://www.react.doctor/share";

interface BadgeSnippetProps {
  searchParamsString: string;
}

const BadgeSnippet = ({ searchParamsString }: BadgeSnippetProps) => {
  const [didCopy, setDidCopy] = useState(false);

  const badgeFullUrl = `${BADGE_BASE_URL}?${searchParamsString}`;
  const shareFullUrl = `${SHARE_BASE_URL}?${searchParamsString}`;
  const badgePreviewPath = `/share/badge?${searchParamsString}`;
  const markdownSnippet = `[![React Doctor](${badgeFullUrl})](${shareFullUrl})`;

  const handleCopy = async () => {
    await navigator.clipboard.writeText(markdownSnippet);
    setDidCopy(true);
    setTimeout(() => setDidCopy(false), COPY_FEEDBACK_DURATION_MS);
  };

  return (
    <div className="mt-8">
      <div className="text-neutral-500">Add a badge to your README:</div>
      <div className="mt-3 flex flex-wrap items-center gap-3">
        <img src={badgePreviewPath} alt="React Doctor score badge" height={20} className="block" />
        <a
          href={badgePreviewPath}
          target="_blank"
          rel="noreferrer"
          className="text-xs text-neutral-500 underline underline-offset-2 transition-colors hover:text-neutral-300"
        >
          Open SVG
        </a>
      </div>

      <div className="mt-3 flex flex-wrap items-start gap-2">
        <code className="min-w-0 flex-1 break-all border border-white/20 px-3 py-1.5 text-xs text-neutral-300">
          {markdownSnippet}
        </code>
        <button
          type="button"
          onClick={handleCopy}
          className="shrink-0 border border-white/20 px-3 py-1.5 text-xs text-neutral-300 transition-all hover:bg-white/10 active:scale-[0.98]"
        >
          {didCopy ? "Copied" : "Copy"}
        </button>
      </div>
    </div>
  );
};

export default BadgeSnippet;
```

## File: `packages/website/src/app/share/page.tsx`
```tsx
import type { Metadata } from "next";
import AnimatedScore from "./animated-score";
import BadgeSnippet from "./badge-snippet";

const PERFECT_SCORE = 100;
const SCORE_GOOD_THRESHOLD = 75;
const SCORE_OK_THRESHOLD = 50;
const COMMAND = "npx -y react-doctor@latest .";
const FIX_COMMAND = "npx -y react-doctor@latest . --fix";
const SHARE_BASE_URL = "https://www.react.doctor/share";
const X_ICON_PATH =
  "M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z";
const LINKEDIN_ICON_PATH =
  "M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 112.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z";

interface ShareSearchParams {
  p?: string;
  s?: string;
  e?: string;
  w?: string;
  f?: string;
}

const clampScore = (value: number): number => Math.max(0, Math.min(PERFECT_SCORE, value));

const getScoreLabel = (score: number): string => {
  if (score >= SCORE_GOOD_THRESHOLD) return "Great";
  if (score >= SCORE_OK_THRESHOLD) return "Needs work";
  return "Critical";
};

const getScoreColorClass = (score: number): string => {
  if (score >= SCORE_GOOD_THRESHOLD) return "text-green-400";
  if (score >= SCORE_OK_THRESHOLD) return "text-yellow-500";
  return "text-red-400";
};

const getDoctorFace = (score: number): [string, string] => {
  if (score >= SCORE_GOOD_THRESHOLD) return ["\u25E0 \u25E0", " \u25BD "];
  if (score >= SCORE_OK_THRESHOLD) return ["\u2022 \u2022", " \u2500 "];
  return ["x x", " \u25BD "];
};

const DoctorFace = ({ score }: { score: number }) => {
  const [eyes, mouth] = getDoctorFace(score);
  const colorClass = getScoreColorClass(score);

  return (
    <pre className={`${colorClass} leading-tight`}>
      {`  \u250C\u2500\u2500\u2500\u2500\u2500\u2510\n  \u2502 ${eyes} \u2502\n  \u2502 ${mouth} \u2502\n  \u2514\u2500\u2500\u2500\u2500\u2500\u2518`}
    </pre>
  );
};

export const generateMetadata = async ({
  searchParams,
}: {
  searchParams: Promise<ShareSearchParams>;
}): Promise<Metadata> => {
  const resolvedParams = await searchParams;
  const projectName = resolvedParams.p ?? null;
  const score = clampScore(Number(resolvedParams.s) || 0);
  const errorCount = Math.max(0, Number(resolvedParams.e) || 0);
  const warningCount = Math.max(0, Number(resolvedParams.w) || 0);
  const label = getScoreLabel(score);

  const titlePrefix = projectName ? `${projectName} - ` : "";
  const title = `React Doctor - ${titlePrefix}Score: ${score}/100 (${label})`;
  const descriptionParts: string[] = [];
  if (errorCount > 0) descriptionParts.push(`${errorCount} error${errorCount === 1 ? "" : "s"}`);
  if (warningCount > 0)
    descriptionParts.push(`${warningCount} warning${warningCount === 1 ? "" : "s"}`);
  const description =
    descriptionParts.length > 0
      ? `${descriptionParts.join(", ")} found. Run react-doctor on your codebase to find React issues.`
      : "Run react-doctor on your codebase to find React issues.";

  const ogSearchParams = new URLSearchParams();
  if (resolvedParams.p) ogSearchParams.set("p", resolvedParams.p);
  if (resolvedParams.s) ogSearchParams.set("s", resolvedParams.s);
  if (resolvedParams.e) ogSearchParams.set("e", resolvedParams.e);
  if (resolvedParams.w) ogSearchParams.set("w", resolvedParams.w);
  if (resolvedParams.f) ogSearchParams.set("f", resolvedParams.f);
  const ogImageUrl = `/share/og?${ogSearchParams.toString()}`;

  return {
    title,
    description,
    openGraph: { title, description, images: [ogImageUrl] },
    twitter: { card: "summary_large_image", title, description, images: [ogImageUrl] },
  };
};

const SharePage = async ({ searchParams }: { searchParams: Promise<ShareSearchParams> }) => {
  const resolvedParams = await searchParams;
  const projectName = resolvedParams.p ?? null;
  const score = clampScore(Number(resolvedParams.s) || 0);
  const errorCount = Math.max(0, Number(resolvedParams.e) || 0);
  const warningCount = Math.max(0, Number(resolvedParams.w) || 0);
  const fileCount = Math.max(0, Number(resolvedParams.f) || 0);
  const label = getScoreLabel(score);

  const shareSearchParams = new URLSearchParams();
  if (resolvedParams.p) shareSearchParams.set("p", resolvedParams.p);
  if (resolvedParams.s) shareSearchParams.set("s", resolvedParams.s);
  if (resolvedParams.e) shareSearchParams.set("e", resolvedParams.e);
  if (resolvedParams.w) shareSearchParams.set("w", resolvedParams.w);
  if (resolvedParams.f) shareSearchParams.set("f", resolvedParams.f);
  const shareUrl = `${SHARE_BASE_URL}?${shareSearchParams.toString()}`;

  const projectLabel = projectName ? `${projectName} ` : "My React codebase ";
  const tweetText = `${projectLabel}scored ${score}/100 (${label}) on React Doctor. Run it on yours:`;
  const twitterShareUrl = `https://twitter.com/intent/tweet?text=${encodeURIComponent(tweetText)}&url=${encodeURIComponent(shareUrl)}`;
  const linkedinShareUrl = `https://www.linkedin.com/sharing/share-offsite/?url=${encodeURIComponent(shareUrl)}`;

  return (
    <div className="mx-auto min-h-screen w-full max-w-3xl bg-[#0a0a0a] p-6 pb-32 font-mono text-base leading-relaxed text-neutral-300 sm:p-8 sm:pb-40 sm:text-lg">
      <div className="mb-6">
        {projectName && <div className="mb-4 text-xl text-white">{projectName}</div>}
        <DoctorFace score={score} />
        <div className="mt-2 text-neutral-500">
          React Doctor <span className="text-neutral-600">(www.react.doctor)</span>
        </div>
      </div>

      <AnimatedScore targetScore={score} />

      {(errorCount > 0 || warningCount > 0 || fileCount > 0) && (
        <div className="mb-8 pl-2">
          {errorCount > 0 && (
            <span className="text-red-400">
              {errorCount} error{errorCount === 1 ? "" : "s"}
            </span>
          )}
          {warningCount > 0 && (
            <span className="text-yellow-500">
              {"  "}
              {warningCount} warning{warningCount === 1 ? "" : "s"}
            </span>
          )}
          {fileCount > 0 && (
            <span className="text-neutral-500">
              {"  "}across {fileCount} file{fileCount === 1 ? "" : "s"}
            </span>
          )}
        </div>
      )}

      <div className="text-neutral-500">Run it on your codebase:</div>
      <div className="mt-2">
        <span className="border border-white/20 px-3 py-1.5 text-white">{COMMAND}</span>
      </div>

      <div className="mt-6 text-neutral-500">Auto-fix with Ami:</div>
      <div className="mt-2">
        <span className="border border-white/20 px-3 py-1.5 text-white">{FIX_COMMAND}</span>
      </div>

      <div className="mt-8 flex flex-wrap items-center gap-3">
        <a
          href={twitterShareUrl}
          target="_blank"
          rel="noreferrer"
          className="inline-flex shrink-0 items-center gap-2 whitespace-nowrap border border-white/20 bg-white px-3 py-1.5 text-black transition-all hover:bg-white/90 active:scale-[0.98]"
        >
          <svg width="16" height="16" fill="currentColor" viewBox="0 0 24 24">
            <path d={X_ICON_PATH} />
          </svg>
          Share on X
        </a>
        <a
          href={linkedinShareUrl}
          target="_blank"
          rel="noreferrer"
          className="inline-flex shrink-0 items-center gap-2 whitespace-nowrap border border-white/20 bg-white px-3 py-1.5 text-black transition-all hover:bg-white/90 active:scale-[0.98]"
        >
          <svg width="16" height="16" fill="currentColor" viewBox="0 0 24 24">
            <path d={LINKEDIN_ICON_PATH} />
          </svg>
          Share on LinkedIn
        </a>
      </div>

      <BadgeSnippet searchParamsString={shareSearchParams.toString()} />
    </div>
  );
};

export default SharePage;
```

## File: `packages/website/src/app/share/badge/route.ts`
```typescript
const PERFECT_SCORE = 100;
const SCORE_GOOD_THRESHOLD = 75;
const SCORE_OK_THRESHOLD = 50;

const BADGE_HEIGHT_PX = 20;
const LABEL_TEXT = "react doctor";
const LABEL_RECT_WIDTH_PX = 97;
const LABEL_TEXT_CENTER_10X = 575;
const LABEL_TEXT_LENGTH_10X = 670;
const SECTION_PADDING_PX = 11;
const DIGIT_WIDTH_10X = 65;
const SLASH_WIDTH_10X = 38;
const FONT_SIZE_10X = 110;
const TEXT_Y_10X = 140;
const SHADOW_Y_10X = 150;
const CACHE_MAX_AGE_SECONDS = 86400;

const LOGO_SIZE_PX = 14;
const LOGO_X_PX = 6;
const LOGO_Y_PX = 3;

const WHITE_LOGO_SVG = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40"><mask id="a" style="mask-type:luminance" maskUnits="userSpaceOnUse" x="0" y="0" width="40" height="40"><path d="M39.2 0H0V39.2H39.2V0Z" fill="#fff"/></mask><g mask="url(#a)"><mask id="b" style="mask-type:luminance" maskUnits="userSpaceOnUse" x="0" y="0" width="40" height="40"><path d="M39.2 0H0V39.2H39.2V0Z" fill="#fff"/></mask><g mask="url(#b)"><mask id="c" style="mask-type:luminance" maskUnits="userSpaceOnUse" x="0" y="0" width="40" height="40"><path d="M39.2 0H0V39.2H39.2V0Z" fill="#fff"/><circle cx="26.9609" cy="23.9609" r="12.9658" fill="#000"/></mask><g mask="url(#c)"><path d="M19.2799 6.33229C22.6283 3.65276 25.9398 2.67017 28.2843 4.02393C30.3796 5.23404 31.3175 8.04321 30.9235 11.9354C30.8903 12.2676 30.8438 12.6056 30.792 12.9474L30.4702 14.6853C30.469 14.6848 30.4674 14.6842 30.466 14.6836C30.4648 14.6886 30.4639 14.6937 30.4624 14.6986L28.834 14.0988C28.8342 14.0981 28.8331 14.097 28.8331 14.0964C27.722 13.75 26.5895 13.4766 25.4427 13.2785L25.4262 13.2745L23.1368 12.9686L23.1348 12.9684C23.1323 12.9648 23.129 12.9623 23.1263 12.9587C21.8483 12.8275 20.5644 12.7622 19.2799 12.7629C17.9924 12.7621 16.706 12.8292 15.4258 12.9638C14.6767 14.0044 13.9812 15.0824 13.3418 16.1937C12.6991 17.3064 12.115 18.4521 11.5919 19.6257C12.115 20.7994 12.6991 21.945 13.3418 23.0577C13.9822 24.1736 14.6799 25.2556 15.4322 26.2993C15.4332 26.2993 15.4344 26.2994 15.4355 26.2996L15.4336 26.3026L15.4327 26.3044L15.4339 26.3061L16.8668 28.135L16.8766 28.1452C17.6182 29.0356 18.4168 29.8766 19.2676 30.6632L19.2812 30.6776L20.6096 31.7716C20.6052 31.7758 20.6008 31.78 20.5963 31.784C20.598 31.7856 20.5999 31.7869 20.6018 31.7882L19.1795 32.9976L19.177 32.9996C16.8747 34.817 14.5963 35.8326 12.6403 35.8326C11.8123 35.8449 10.9959 35.6362 10.2755 35.2277C8.17999 34.0176 7.24223 31.2082 7.63613 27.3161C7.67044 26.9742 7.71745 26.6258 7.77209 26.2738C3.77821 24.7102 1.26978 22.3346 1.26978 19.6257C1.26978 17.2056 3.23305 14.9861 6.79872 13.3833C7.11261 13.2421 7.43921 13.1074 7.77209 12.9803C7.71745 12.6269 7.67044 12.2773 7.63613 11.9354C7.24223 8.04321 8.17999 5.23404 10.2755 4.02393C12.62 2.67017 15.9315 3.65276 19.2799 6.33229ZM9.41901 26.842C9.38977 27.0606 9.36309 27.2754 9.34276 27.489C9.02252 30.6089 9.67308 32.8837 11.1149 33.7317L11.1357 33.7416C12.672 34.6289 15.202 33.9234 17.971 31.784C16.7064 30.5933 15.5459 29.2966 14.5019 27.9085C12.7803 27.6989 11.0797 27.3421 9.41901 26.842ZM10.7138 21.7917C10.312 22.8902 9.98225 24.0138 9.72649 25.1552C10.8239 25.4965 11.9421 25.7662 13.0743 25.9632L13.1283 25.975C12.6949 25.3153 12.2693 24.6213 11.8575 23.917C11.4458 23.2129 11.0671 22.5024 10.7138 21.7917ZM8.10124 14.6937C7.89791 14.7785 7.69841 14.8633 7.50271 14.948C4.63721 16.2408 2.98525 17.9454 2.98525 19.6257C2.98525 21.399 4.86213 23.2396 8.09996 24.568C8.49923 22.8774 9.04169 21.2242 9.72143 19.6257C9.04297 18.0306 8.50092 16.3806 8.10124 14.6937ZM13.1219 13.2854C11.9744 13.486 10.841 13.7608 9.72905 14.1078C9.98057 15.227 10.3033 16.329 10.6951 17.4072L10.7075 17.4585C11.0659 16.7466 11.4407 16.045 11.8512 15.3344C12.2616 14.6238 12.6873 13.9425 13.1219 13.2854ZM12.6568 5.13617C12.1245 5.12376 11.5983 5.25271 11.1319 5.50988C9.68392 6.34684 9.02637 8.61269 9.33903 11.7259L9.33892 11.7626C9.35924 11.9761 9.38592 12.191 9.41516 12.4083C11.0765 11.9115 12.7769 11.556 14.4982 11.3456C15.5427 9.95703 16.704 8.6604 17.9698 7.46996C15.9836 5.93447 14.1194 5.13617 12.6568 5.13617ZM27.4316 5.50861C26.9691 5.25304 26.4474 5.12408 25.9192 5.13463L25.9054 5.13491C24.4428 5.13491 22.5787 5.93319 20.5926 7.46868C21.8574 8.65829 23.0179 9.95407 24.0616 11.3418C25.7834 11.5512 27.4838 11.908 29.1446 12.4083C29.175 12.191 29.2004 11.9749 29.222 11.7613C29.5398 8.62796 28.8867 6.34883 27.4316 5.50861ZM19.2736 8.5746C18.4139 9.36816 17.6072 10.2174 16.8591 11.1168C17.652 11.066 18.4568 11.0406 19.2736 11.0406C20.097 11.0406 20.9038 11.0685 21.6943 11.1168C20.944 10.2172 20.1354 9.36792 19.2736 8.5746Z" fill="#fff"/></g></g></g><g clip-path="url(#d)"><path d="M26.9609 33.9219C32.459 33.9219 36.9219 29.459 36.9219 23.9609C36.9219 18.4629 32.459 14 26.9609 14C21.4629 14 17 18.4629 17 23.9609C17 29.459 21.4629 33.9219 26.9609 33.9219ZM26.9609 32.2617C22.3711 32.2617 18.6602 28.5508 18.6602 23.9609C18.6602 19.3711 22.3711 15.6602 26.9609 15.6602C31.5508 15.6602 35.2617 19.3711 35.2617 23.9609C35.2617 28.5508 31.5508 32.2617 26.9609 32.2617Z" fill="#fff"/><path d="M21.5605 24.9863C21.5605 25.582 21.9707 25.9824 22.5566 25.9824H24.9102V28.3262C24.9102 28.9414 25.3105 29.332 25.9062 29.332H27.9766C28.582 29.332 28.9727 28.9414 28.9727 28.3262V25.9824H31.3262C31.9316 25.9824 32.332 25.582 32.332 24.9863V22.9063C32.332 22.3203 31.9316 21.9102 31.3262 21.9102H28.9727V19.5762C28.9727 18.9707 28.582 18.5703 27.9766 18.5703H25.9062C25.3105 18.5703 24.9102 18.9707 24.9102 19.5762V21.9102H22.5566C21.9609 21.9102 21.5605 22.3203 21.5605 22.9063V24.9863Z" fill="#fff"/></g><defs><clipPath id="d"><rect x="17" y="14" width="20.2832" height="19.9316" rx="9.9658" fill="#fff"/></clipPath></defs></svg>`;

const LOGO_DATA_URI = `data:image/svg+xml,${encodeURIComponent(WHITE_LOGO_SVG)}`;

const getBadgeScoreColor = (score: number): string => {
  if (score >= SCORE_GOOD_THRESHOLD) return "#2ea043";
  if (score >= SCORE_OK_THRESHOLD) return "#d29922";
  return "#cf222e";
};

const computeScoreTextLength = (scoreText: string): number =>
  scoreText.split("").reduce((totalWidth, character) => {
    if (character === "/") return totalWidth + SLASH_WIDTH_10X;
    return totalWidth + DIGIT_WIDTH_10X;
  }, 0);

export const GET = (request: Request): Response => {
  const { searchParams } = new URL(request.url);
  const score = Math.max(0, Math.min(PERFECT_SCORE, Number(searchParams.get("s")) || 0));

  const scoreText = `${score}/${PERFECT_SCORE}`;
  const scoreColor = getBadgeScoreColor(score);
  const scoreTextLength = computeScoreTextLength(scoreText);
  const valueRectWidth = Math.round(scoreTextLength / 10) + SECTION_PADDING_PX * 2;
  const totalWidth = LABEL_RECT_WIDTH_PX + valueRectWidth;

  const valueCenterX = (LABEL_RECT_WIDTH_PX + valueRectWidth / 2) * 10;

  const svg = `<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="${totalWidth}" height="${BADGE_HEIGHT_PX}" role="img" aria-label="${LABEL_TEXT}: ${scoreText}">
  <title>${LABEL_TEXT}: ${scoreText}</title>
  <linearGradient id="s" x2="0" y2="100%">
    <stop offset="0" stop-color="#bbb" stop-opacity=".1"/>
    <stop offset="1" stop-opacity=".1"/>
  </linearGradient>
  <clipPath id="r">
    <rect width="${totalWidth}" height="${BADGE_HEIGHT_PX}" rx="3" fill="#fff"/>
  </clipPath>
  <g clip-path="url(#r)">
    <rect width="${LABEL_RECT_WIDTH_PX}" height="${BADGE_HEIGHT_PX}" fill="#555"/>
    <rect x="${LABEL_RECT_WIDTH_PX}" width="${valueRectWidth}" height="${BADGE_HEIGHT_PX}" fill="${scoreColor}"/>
    <rect width="${totalWidth}" height="${BADGE_HEIGHT_PX}" fill="url(#s)"/>
  </g>
  <image x="${LOGO_X_PX}" y="${LOGO_Y_PX}" width="${LOGO_SIZE_PX}" height="${LOGO_SIZE_PX}" href="${LOGO_DATA_URI}"/>
  <g fill="#fff" text-anchor="middle" font-family="Verdana,Geneva,DejaVu Sans,sans-serif" text-rendering="geometricPrecision" font-size="${FONT_SIZE_10X}">
    <text aria-hidden="true" x="${LABEL_TEXT_CENTER_10X}" y="${SHADOW_Y_10X}" fill="#010101" fill-opacity=".3" transform="scale(.1)" textLength="${LABEL_TEXT_LENGTH_10X}">${LABEL_TEXT}</text>
    <text x="${LABEL_TEXT_CENTER_10X}" y="${TEXT_Y_10X}" transform="scale(.1)" fill="#fff" textLength="${LABEL_TEXT_LENGTH_10X}">${LABEL_TEXT}</text>
    <text aria-hidden="true" x="${valueCenterX}" y="${SHADOW_Y_10X}" fill="#010101" fill-opacity=".3" transform="scale(.1)" textLength="${scoreTextLength}">${scoreText}</text>
    <text x="${valueCenterX}" y="${TEXT_Y_10X}" transform="scale(.1)" fill="#fff" textLength="${scoreTextLength}">${scoreText}</text>
  </g>
</svg>`;

  return new Response(svg, {
    headers: {
      "Content-Type": "image/svg+xml",
      "Cache-Control": `public, max-age=${CACHE_MAX_AGE_SECONDS}, s-maxage=${CACHE_MAX_AGE_SECONDS}`,
    },
  });
};
```

## File: `packages/website/src/app/share/og/route.tsx`
```tsx
import { ImageResponse } from "next/og";

const PERFECT_SCORE = 100;
const SCORE_GOOD_THRESHOLD = 75;
const SCORE_OK_THRESHOLD = 50;
const IMAGE_WIDTH_PX = 1200;
const IMAGE_HEIGHT_PX = 630;
const OG_BRAND_MARK_WIDTH_PX = 244;
const OG_BRAND_MARK_HEIGHT_PX = 82;
const OG_BRAND_MARK_PATH = "/react-doctor-og-banner.svg";

const getScoreLabel = (score: number): string => {
  if (score >= SCORE_GOOD_THRESHOLD) return "Great";
  if (score >= SCORE_OK_THRESHOLD) return "Needs work";
  return "Critical";
};

const getScoreColor = (score: number): string => {
  if (score >= SCORE_GOOD_THRESHOLD) return "#4ade80";
  if (score >= SCORE_OK_THRESHOLD) return "#eab308";
  return "#f87171";
};

export const GET = (request: Request): ImageResponse => {
  const { searchParams } = new URL(request.url);

  const projectName = searchParams.get("p") ?? null;
  const score = Math.max(0, Math.min(PERFECT_SCORE, Number(searchParams.get("s")) || 0));
  const errorCount = Math.max(0, Number(searchParams.get("e")) || 0);
  const warningCount = Math.max(0, Number(searchParams.get("w")) || 0);
  const fileCount = Math.max(0, Number(searchParams.get("f")) || 0);
  const scoreColor = getScoreColor(score);
  const brandMarkUrl = new URL(OG_BRAND_MARK_PATH, request.url).toString();
  const scoreBarPercent = (score / PERFECT_SCORE) * 100;

  return new ImageResponse(
    <div
      style={{
        width: "100%",
        height: "100%",
        display: "flex",
        flexDirection: "column",
        backgroundColor: "#0a0a0a",
        fontFamily: "monospace",
        padding: "60px 80px",
        justifyContent: "center",
      }}
    >
      <div style={{ display: "flex", alignItems: "center", gap: "24px" }}>
        <img src={brandMarkUrl} width={OG_BRAND_MARK_WIDTH_PX} height={OG_BRAND_MARK_HEIGHT_PX} />
        {projectName && (
          <div
            style={{
              display: "flex",
              marginLeft: "auto",
              fontSize: "24px",
              color: "#a3a3a3",
            }}
          >
            {projectName}
          </div>
        )}
      </div>

      <div style={{ display: "flex", alignItems: "baseline", gap: "16px", marginTop: "48px" }}>
        <span style={{ fontSize: "120px", color: scoreColor, fontWeight: 700, lineHeight: 1 }}>
          {score}
        </span>
        <span style={{ fontSize: "40px", color: "#525252", lineHeight: 1 }}>/ {PERFECT_SCORE}</span>
        <span style={{ fontSize: "40px", color: scoreColor, lineHeight: 1, marginLeft: "8px" }}>
          {getScoreLabel(score)}
        </span>
      </div>

      <div
        style={{
          display: "flex",
          width: "100%",
          height: "16px",
          backgroundColor: "#1a1a1a",
          borderRadius: "8px",
          marginTop: "32px",
          overflow: "hidden",
        }}
      >
        <div
          style={{
            width: `${scoreBarPercent}%`,
            height: "100%",
            backgroundColor: scoreColor,
            borderRadius: "8px",
          }}
        />
      </div>

      {(errorCount > 0 || warningCount > 0 || fileCount > 0) && (
        <div style={{ display: "flex", gap: "24px", marginTop: "36px", fontSize: "24px" }}>
          {errorCount > 0 && (
            <span style={{ color: "#f87171" }}>
              {errorCount} error{errorCount === 1 ? "" : "s"}
            </span>
          )}
          {warningCount > 0 && (
            <span style={{ color: "#eab308" }}>
              {warningCount} warning{warningCount === 1 ? "" : "s"}
            </span>
          )}
          {fileCount > 0 && (
            <span style={{ color: "#737373" }}>
              across {fileCount} file{fileCount === 1 ? "" : "s"}
            </span>
          )}
        </div>
      )}
    </div>,
    { width: IMAGE_WIDTH_PX, height: IMAGE_HEIGHT_PX },
  );
};
```

## File: `packages/website/src/components/react-doctor-icon.tsx`
```tsx
const DEFAULT_ICON_SIZE_PX = 40;

interface ReactDoctorIconProps {
  sizePx?: number;
  className?: string;
  alt?: string;
}

const ReactDoctorIcon = ({
  sizePx = DEFAULT_ICON_SIZE_PX,
  className,
  alt = "React Doctor icon",
}: ReactDoctorIconProps) => (
  <img
    src="/react-doctor-icon.svg"
    width={sizePx}
    height={sizePx}
    alt={alt}
    className={className}
  />
);

export default ReactDoctorIcon;
```

## File: `packages/website/src/components/terminal.tsx`
```tsx
"use client";

import { useEffect, useState, useCallback } from "react";
import { Copy, Check, ChevronRight, RotateCcw } from "lucide-react";

const COPIED_RESET_DELAY_MS = 2000;
const INITIAL_DELAY_MS = 500;
const TYPING_DELAY_MS = 50;
const PROJECT_SCAN_DELAY_MS = 800;
const POST_HEADER_DELAY_MS = 600;
const DIAGNOSTIC_MIN_DELAY_MS = 150;
const DIAGNOSTIC_MAX_DELAY_MS = 350;
const SCORE_REVEAL_DELAY_MS = 600;
const SCORE_FRAME_COUNT = 20;
const SCORE_FRAME_DELAY_MS = 30;
const POST_SCORE_DELAY_MS = 700;
const TARGET_SCORE = 42;
const PERFECT_SCORE = 100;
const SCORE_BAR_WIDTH_MOBILE = 15;
const SCORE_BAR_WIDTH_DESKTOP = 30;
const SCORE_GOOD_THRESHOLD = 75;
const SCORE_OK_THRESHOLD = 50;
const DIAGNOSTIC_COUNT_MOBILE = 3;
const TOTAL_ERROR_COUNT = 22;
const AFFECTED_FILE_COUNT = 18;
const ELAPSED_TIME = "2.1s";

const ANIMATION_COMPLETED_KEY = "react-doctor-animation-completed";
const COMMAND = "npx -y react-doctor@latest .";
const GITHUB_URL = "https://github.com/millionco/react-doctor";
const GITHUB_ICON_PATH =
  "M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.531 1.032 1.531 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z";

interface FileLocation {
  path: string;
  lines: number[];
}

interface Diagnostic {
  message: string;
  count: number;
  files: FileLocation[];
}

const DIAGNOSTICS: Diagnostic[] = [
  {
    message: "Derived state computed in useEffect, compute during render instead",
    count: 5,
    files: [
      { path: "src/components/Dashboard.tsx", lines: [42, 87] },
      { path: "src/hooks/useFilters.ts", lines: [15, 23, 31] },
    ],
  },
  {
    message: 'Server action "deleteUser" missing authentication check',
    count: 2,
    files: [
      { path: "src/app/actions/users.ts", lines: [18] },
      { path: "src/app/actions/admin.ts", lines: [45] },
    ],
  },
  {
    message: "Array index used as key, causes bugs when items are reordered",
    count: 12,
    files: [
      { path: "src/components/TodoList.tsx", lines: [24, 51] },
      { path: "src/components/CommentThread.tsx", lines: [33, 67, 89] },
      { path: "src/components/SearchResults.tsx", lines: [19, 42, 55, 78, 91, 103, 112] },
    ],
  },
  {
    message: 'Component "UserCard" inside "Dashboard", destroys state every render',
    count: 4,
    files: [
      { path: "src/components/Dashboard.tsx", lines: [56, 112] },
      { path: "src/components/Settings.tsx", lines: [34, 78] },
    ],
  },
  {
    message: "Data fetched in useEffect without cleanup, causes race conditions",
    count: 8,
    files: [
      { path: "src/components/Profile.tsx", lines: [22] },
      { path: "src/components/Feed.tsx", lines: [45, 89] },
      { path: "src/hooks/useUser.ts", lines: [12, 34] },
      { path: "src/hooks/usePosts.ts", lines: [8, 19, 27] },
    ],
  },
  {
    message: "useState initialized from prop, derive during render instead of syncing",
    count: 3,
    files: [
      { path: "src/components/EditForm.tsx", lines: [15, 16] },
      { path: "src/components/Modal.tsx", lines: [28] },
    ],
  },
  {
    message: "Missing prefers-reduced-motion check for animations",
    count: 2,
    files: [
      { path: "src/components/Hero.tsx", lines: [41] },
      { path: "src/components/Carousel.tsx", lines: [63] },
    ],
  },
];

const getScoreColor = (score: number) => {
  if (score >= SCORE_GOOD_THRESHOLD) return "text-green-400";
  if (score >= SCORE_OK_THRESHOLD) return "text-yellow-500";
  return "text-red-400";
};

const getScoreLabel = (score: number) => {
  if (score >= SCORE_GOOD_THRESHOLD) return "Great";
  if (score >= SCORE_OK_THRESHOLD) return "Needs work";
  return "Critical";
};

const easeOutCubic = (progress: number) => 1 - Math.pow(1 - progress, 3);

const sleep = (milliseconds: number) =>
  new Promise<void>((resolve) => setTimeout(resolve, milliseconds));

const Spacer = () => <div className="min-h-[1.4em]" />;

const FadeIn = ({ children }: { children: React.ReactNode }) => (
  <div className="animate-fade-in">{children}</div>
);

const getDoctorFace = (score: number): [string, string] => {
  if (score >= SCORE_GOOD_THRESHOLD) return ["◠ ◠", " ▽ "];
  if (score >= SCORE_OK_THRESHOLD) return ["• •", " ─ "];
  return ["x x", " ▽ "];
};

const BOX_TOP = "┌─────┐";
const BOX_BOTTOM = "└─────┘";

const DoctorBranding = ({ score }: { score: number }) => {
  const [eyes, mouth] = getDoctorFace(score);
  const colorClass = getScoreColor(score);

  return (
    <div>
      <pre className={`${colorClass} leading-tight`}>
        {`  ${BOX_TOP}\n  │ ${eyes} │\n  │ ${mouth} │\n  ${BOX_BOTTOM}`}
      </pre>
    </div>
  );
};

const ScoreBar = ({ score, barWidth }: { score: number; barWidth: number }) => {
  const filledCount = Math.round((score / PERFECT_SCORE) * barWidth);
  const emptyCount = barWidth - filledCount;
  const colorClass = getScoreColor(score);

  return (
    <>
      <span className={colorClass}>{"█".repeat(filledCount)}</span>
      <span className="text-neutral-600">{"░".repeat(emptyCount)}</span>
    </>
  );
};

const ScoreGauge = ({ score }: { score: number }) => {
  const colorClass = getScoreColor(score);

  return (
    <div className="pl-2">
      <div>
        <span className={colorClass}>{score}</span>
        {` / ${PERFECT_SCORE}  `}
        <span className={colorClass}>{getScoreLabel(score)}</span>
      </div>
      <div className="my-1 text-xs sm:text-sm">
        <span className="sm:hidden">
          <ScoreBar score={score} barWidth={SCORE_BAR_WIDTH_MOBILE} />
        </span>
        <span className="hidden sm:inline">
          <ScoreBar score={score} barWidth={SCORE_BAR_WIDTH_DESKTOP} />
        </span>
      </div>
    </div>
  );
};

const CopyCommand = () => {
  const [didCopy, setDidCopy] = useState(false);

  const handleCopy = useCallback(async () => {
    await navigator.clipboard.writeText(COMMAND);
    setDidCopy(true);
    setTimeout(() => setDidCopy(false), COPIED_RESET_DELAY_MS);
  }, []);

  const IconComponent = didCopy ? Check : Copy;
  const iconClass = didCopy
    ? "shrink-0 text-green-400"
    : "shrink-0 text-white/50 transition-colors group-hover:text-white";

  return (
    <div className="group flex items-center gap-4 border border-white/20 px-3 py-1.5 transition-colors hover:bg-white/5">
      <span className="select-all whitespace-nowrap text-white">{COMMAND}</span>
      <button onClick={handleCopy}>
        <IconComponent size={16} className={iconClass} />
      </button>
    </div>
  );
};

const DiagnosticItem = ({ diagnostic }: { diagnostic: Diagnostic }) => {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <div className="mb-1">
      <div className="sm:hidden">
        <span className="text-red-400"> ✗</span>
        {` ${diagnostic.message} `}
        <span className="text-neutral-500">({diagnostic.count})</span>
      </div>
      <div className="hidden sm:block">
        <button
          onClick={() => setIsOpen((previous) => !previous)}
          className="inline-flex items-start gap-1 text-left"
        >
          <ChevronRight
            size={16}
            className={`mt-[0.35em] shrink-0 text-neutral-500 transition-transform duration-150 ${isOpen ? "rotate-90" : ""}`}
          />
          <span>
            <span className="text-red-400">✗</span>
            {` ${diagnostic.message} `}
            <span className="text-neutral-500">({diagnostic.count})</span>
          </span>
        </button>
        <div
          className="ml-6 grid text-sm text-neutral-500 transition-[grid-template-rows,opacity] duration-200 ease-out sm:text-base"
          style={{
            gridTemplateRows: isOpen ? "1fr" : "0fr",
            opacity: isOpen ? 1 : 0,
          }}
        >
          <div className="overflow-hidden">
            <div className="mt-1">
              {diagnostic.files.map((file) => (
                <div key={file.path}>
                  {file.path}
                  {file.lines.length > 0 && `: ${file.lines.join(", ")}`}
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

interface AnimationState {
  typedCommand: string;
  isTyping: boolean;
  showHeader: boolean;
  visibleDiagnosticCount: number;
  showSeparator: boolean;
  score: number | null;
  showSummary: boolean;
}

const INITIAL_STATE: AnimationState = {
  typedCommand: "",
  isTyping: true,
  showHeader: false,
  visibleDiagnosticCount: 0,
  showSeparator: false,
  score: null,
  showSummary: false,
};

const COMPLETED_STATE: AnimationState = {
  typedCommand: COMMAND,
  isTyping: false,
  showHeader: true,
  visibleDiagnosticCount: DIAGNOSTICS.length,
  showSeparator: true,
  score: TARGET_SCORE,
  showSummary: true,
};

const didAnimationComplete = () => {
  try {
    return localStorage.getItem(ANIMATION_COMPLETED_KEY) === "true";
  } catch {
    return false;
  }
};

const markAnimationCompleted = () => {
  try {
    localStorage.setItem(ANIMATION_COMPLETED_KEY, "true");
  } catch {}
};

const Terminal = () => {
  const [state, setState] = useState<AnimationState>(
    didAnimationComplete() ? COMPLETED_STATE : INITIAL_STATE,
  );

  useEffect(() => {
    if (didAnimationComplete()) return;

    let cancelled = false;

    const update = (patch: Partial<AnimationState>) => {
      if (!cancelled) setState((previous) => ({ ...previous, ...patch }));
    };

    const run = async () => {
      await sleep(INITIAL_DELAY_MS);

      for (let index = 0; index <= COMMAND.length; index++) {
        if (cancelled) return;
        update({ typedCommand: COMMAND.slice(0, index) });
        await sleep(TYPING_DELAY_MS);
      }

      update({ isTyping: false });
      await sleep(PROJECT_SCAN_DELAY_MS);
      if (cancelled) return;

      update({ showHeader: true });
      await sleep(POST_HEADER_DELAY_MS);

      for (let index = 0; index < DIAGNOSTICS.length; index++) {
        if (cancelled) return;
        update({ visibleDiagnosticCount: index + 1 });
        const jitteredDelay =
          DIAGNOSTIC_MIN_DELAY_MS +
          Math.random() * (DIAGNOSTIC_MAX_DELAY_MS - DIAGNOSTIC_MIN_DELAY_MS);
        await sleep(jitteredDelay);
      }

      update({ showSeparator: true });
      await sleep(SCORE_REVEAL_DELAY_MS);

      for (let frame = 0; frame <= SCORE_FRAME_COUNT; frame++) {
        if (cancelled) return;
        update({ score: Math.round(easeOutCubic(frame / SCORE_FRAME_COUNT) * TARGET_SCORE) });
        await sleep(SCORE_FRAME_DELAY_MS);
      }

      await sleep(POST_SCORE_DELAY_MS);
      if (cancelled) return;
      update({ showSummary: true });
      markAnimationCompleted();
    };

    run();
    return () => {
      cancelled = true;
    };
  }, []);

  return (
    <div className="mx-auto min-h-screen w-full max-w-3xl bg-[#0a0a0a] p-6 pb-32 font-mono text-base leading-relaxed text-neutral-300 sm:p-8 sm:pb-40 sm:text-lg">
      <div>
        <span className="text-neutral-500">$ </span>
        <span>{state.typedCommand}</span>
        {state.isTyping && <span>▋</span>}
      </div>

      {state.showHeader && (
        <FadeIn>
          <Spacer />
          <div className="flex items-center gap-2">
            <img src="/favicon.svg" alt="React Doctor" width={24} height={24} />
            react-doctor
          </div>
          <div className="text-neutral-500">
            Let coding agents diagnose and fix your React code.
          </div>
          <Spacer />
        </FadeIn>
      )}

      <div className="sm:hidden">
        {DIAGNOSTICS.slice(0, Math.min(state.visibleDiagnosticCount, DIAGNOSTIC_COUNT_MOBILE)).map(
          (diagnostic) => (
            <FadeIn key={diagnostic.message}>
              <DiagnosticItem diagnostic={diagnostic} />
            </FadeIn>
          ),
        )}
      </div>
      <div className="hidden sm:block">
        {DIAGNOSTICS.slice(0, state.visibleDiagnosticCount).map((diagnostic) => (
          <FadeIn key={diagnostic.message}>
            <DiagnosticItem diagnostic={diagnostic} />
          </FadeIn>
        ))}
      </div>

      {state.showSeparator && <Spacer />}

      {state.score !== null && (
        <FadeIn>
          <DoctorBranding score={state.score} />
          <Spacer />
          <ScoreGauge score={state.score} />
        </FadeIn>
      )}

      {state.showSummary && (
        <FadeIn>
          <Spacer />
          <div>
            <span className="text-red-400">{TOTAL_ERROR_COUNT} errors</span>
            <span className="text-neutral-500">
              {`  across ${AFFECTED_FILE_COUNT} files  in ${ELAPSED_TIME}`}
            </span>
          </div>
          <Spacer />
          <div className="text-neutral-500">Run it on your codebase to find issues like these:</div>
          <Spacer />
          <div className="flex flex-wrap items-center gap-3">
            <CopyCommand />
            <a
              href={GITHUB_URL}
              target="_blank"
              rel="noreferrer"
              className="inline-flex shrink-0 items-center gap-2 whitespace-nowrap border border-white/20 bg-white px-3 py-1.5 text-black transition-all hover:bg-white/90 active:scale-[0.98]"
            >
              <svg width="18" height="18" fill="currentColor" viewBox="0 0 24 24">
                <path fillRule="evenodd" clipRule="evenodd" d={GITHUB_ICON_PATH} />
              </svg>
              Star on GitHub
            </a>
          </div>
        </FadeIn>
      )}

      {state.showSummary && (
        <div className="mt-8">
          <button
            onClick={() => {
              try {
                localStorage.removeItem(ANIMATION_COMPLETED_KEY);
              } catch {}
              location.reload();
            }}
            className="inline-flex items-center gap-1.5 text-xs text-neutral-600 transition-colors hover:text-neutral-400"
          >
            <RotateCcw size={12} />
            Restart demo
          </button>
        </div>
      )}
    </div>
  );
};

export default Terminal;
```

## File: `skills/react-doctor/SKILL.md`
```markdown
---
name: react-doctor
description: Run after making React changes to catch issues early. Use when reviewing code, finishing a feature, or fixing bugs in a React project.
version: 1.0.0
---

# React Doctor

Scans your React codebase for security, performance, correctness, and architecture issues. Outputs a 0-100 score with actionable diagnostics.

## Usage

```bash
npx -y react-doctor@latest . --verbose --diff
```

## Workflow

Run after making changes to catch issues early. Fix errors first, then re-run to verify the score improved.
```

