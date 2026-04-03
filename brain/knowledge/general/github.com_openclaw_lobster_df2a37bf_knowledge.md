---
id: github.com-openclaw-lobster-df2a37bf-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:09.119854
---

# KNOWLEDGE EXTRACT: github.com_openclaw_lobster_df2a37bf
> **Extracted on:** 2026-04-01 15:10:56
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007524336/github.com_openclaw_lobster_df2a37bf

---

## File: `.gitignore`
```
# Dependencies
node_modules/

# Build output
dist/

# Lobster state
.lobster/
.lobster-cache/
.pnpm-store/

# Private docs
clawdbot_enhancement.md

# OS files
.DS_Store

# Logs
*.log

# Environment
.env
.env.local
```

## File: `.oxlintrc.json`
```json
{
  "$schema": "https://raw.githubusercontent.com/oxc-project/oxlint/main/npm/oxlint/schema.json",
  "env": {
    "node": true,
    "es2022": true
  },
  "rules": {
    "eslint/no-unused-vars": ["error", { "argsIgnorePattern": "^_", "caughtErrorsIgnorePattern": "^_", "varsIgnorePattern": "^_" }],
    "eslint/no-undef": "error",
    "typescript/no-explicit-any": "off"
  }
}
```

## File: `AGENTS.md`
```markdown
# AGENTS.md

Guidance for coding assistants operating in this repository.

## When To Use Lobster

- Prefer `lobster` for multi-step or repeatable workflows.
- Use direct shell commands for simple one-off tasks.
- Prefer deterministic pipelines/workflows over ad-hoc LLM re-planning loops.

## Invocation Contract

- Use tool mode for machine-readable output:
  - `lobster run --mode tool '<pipeline>'`
  - `lobster run --mode tool --file <workflow.lobster> --args-json '<json>'`
- If `lobster` is not on `PATH`, use:
  - `node bin/lobster.js ...`

## Approval And Resume

- Treat `status: "needs_approval"` as a hard stop.
- Never auto-approve on behalf of a user.
- Resume only after explicit user decision:
  - `lobster resume --token <resumeToken> --approve yes|no`

## Output Handling

- Parse the tool envelope JSON fields: `ok`, `status`, `output`, `requiresApproval`, `error`.
- On `ok: false`, surface the error and stop.

## Safety And Shell Usage

- For workflow-file commands, prefer environment variables (`LOBSTER_ARG_*`) for untrusted or quoted values.
- Avoid embedding unsafe user strings directly into shell command text.

```

## File: `CHANGELOG.md`
```markdown
# Changelog

All notable changes to Lobster will be documented in this file.

## Unreleased

- Add workflow file runner for `.lobster`/YAML/JSON workflows with args, env, conditions, and approval gates.
- Add compact workflow resume tokens backed by Lobster state storage.
- Add `exec --stdin raw|json|jsonl` to pipe workflow output into subprocess stdin.
- Add `approve --preview-from-stdin --limit N` for approval previews without extra glue.
- Add `openclaw.invoke --each` to map pipeline input items into tool calls. (`clawd.invoke` remains supported as an alias.)
- Extend CLI to run workflow files with `lobster run <file>` or `--file` + `--args-json`.

## 2026.1.21-1

- Published release (pre-changelog).

## 2026.1.21

- Initial published release (pre-changelog).
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2026 Vignesh

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
# Lobster

An OpenClaw-native workflow shell: typed (JSON-first) pipelines, jobs, and approval gates.


## Example of Lobster at work
OpenClaw (or any other AI agent) can use `lobster` as a workflow engine and avoid re-planning every step — saving tokens while improving determinism and resumability.

### Watching a PR that hasn't had changes
```
node bin/lobster.js "workflows.run --name github.pr.monitor --args-json '{\"repo\":\"openclaw/openclaw\",\"pr\":1152}'"
[
  {
    "kind": "github.pr.monitor",
    "repo": "openclaw/openclaw",
    "prNumber": 1152,
    "key": "github.pr:openclaw/openclaw#1152",
    "changed": false,
    "summary": {
      "changedFields": [],
      "changes": {}
    },
    "prSnapshot": {
      "author": {
        "id": "MDQ6VXNlcjE0MzY4NTM=",
        "is_bot": false,
        "login": "vignesh07",
        "name": "Vignesh"
      },
      "baseRefName": "main",
      "headRefName": "feat/lobster-plugin",
      "isDraft": false,
      "mergeable": "MERGEABLE",
      "number": 1152,
      "reviewDecision": "",
      "state": "OPEN",
      "title": "feat: Add optional lobster plugin tool (typed workflows, approvals/resume)",
      "updatedAt": "2026-01-18T20:16:56Z",
      "url": "https://github.com/openclaw/openclaw/pull/1152"
    }
  }
]
```
### And a PR that has a state change (in this case an approved PR)

```
 node bin/lobster.js "workflows.run --name github.pr.monitor --args-json '{\"repo\":\"openclaw/openclaw\",\"pr\":1200}'"
[
  {
    "kind": "github.pr.monitor",
    "repo": "openclaw/openclaw",
    "prNumber": 1200,
    "key": "github.pr:openclaw/openclaw#1200",
    "changed": true,
    "summary": {
      "changedFields": [
        "number",
        "title",
        "url",
        "state",
        "isDraft",
        "mergeable",
        "reviewDecision",
        "updatedAt",
        "baseRefName",
        "headRefName"
      ],
      "changes": {
        "number": {
          "from": null,
          "to": 1200
        },
        "title": {
          "from": null,
          "to": "feat(tui): add syntax highlighting for code blocks"
        },
        "url": {
          "from": null,
          "to": "https://github.com/openclaw/openclaw/pull/1200"
        },
        "state": {
          "from": null,
          "to": "MERGED"
        },
        "isDraft": {
          "from": null,
          "to": false
        },
        "mergeable": {
          "from": null,
          "to": "UNKNOWN"
        },
        "reviewDecision": {
          "from": null,
          "to": ""
        },
        "updatedAt": {
          "from": null,
          "to": "2026-01-19T05:06:09Z"
        },
        "baseRefName": {
          "from": null,
          "to": "main"
        },
        "headRefName": {
          "from": null,
          "to": "feat/tui-syntax-highlighting"
        }
      }
    },
    "prSnapshot": {
      "author": {
        "id": "MDQ6VXNlcjE0MzY4NTM=",
        "is_bot": false,
        "login": "vignesh07",
        "name": "Vignesh"
      },
      "baseRefName": "main",
      "headRefName": "feat/tui-syntax-highlighting",
      "isDraft": false,
      "mergeable": "UNKNOWN",
      "number": 1200,
      "reviewDecision": "",
      "state": "MERGED",
      "title": "feat(tui): add syntax highlighting for code blocks",
      "updatedAt": "2026-01-19T05:06:09Z",
      "url": "https://github.com/openclaw/openclaw/pull/1200"
    }
  }
]
```

## Goals


- Typed pipelines (objects/arrays), not text pipes.
- Local-first execution.
- No new auth surface: Lobster must not own OAuth/tokens.
- Composable macros that OpenClaw (or any agent) can invoke in one step to save tokens.

## Quick start

From this folder:

- `pnpm install`
- `pnpm test`
- `pnpm lint`
- `node ./bin/lobster.js --help`
- `node ./bin/lobster.js doctor`
- `node ./bin/lobster.js "exec --json --shell 'echo [1,2,3]' | where '0>=0' | json"`

### Notes

- `pnpm test` runs `tsc` and then executes tests against `dist/`.
- `bin/lobster.js` prefers the compiled entrypoint in `dist/` when present.
## Commands

- `exec`: run OS commands
- `exec --stdin raw|json|jsonl`: feed pipeline input into subprocess stdin
- `where`, `pick`, `head`: data shaping
- `json`, `table`: renderers
- `approve`: approval gate (TTY prompt or `--emit` for OpenClaw integration)

## Next steps

- OpenClaw integration: ship as an optional OpenClaw plugin tool.

## Workflow files

Lobster workflow files are meant to read like small scripts:

- `run:` or `command:` for deterministic shell/CLI steps
- `pipeline:` for native Lobster stages like `llm.invoke`
- `approval:` for hard workflow gates between steps
- `stdin: $step.stdout` or `stdin: $step.json` to pass data forward

```
lobster run path/to/workflow.lobster
lobster run --file path/to/workflow.lobster --args-json '{"tag":"family"}'
```

Example file:

```yaml
name: jacket-advice
args:
  location:
    default: Phoenix
steps:
  - id: fetch
    run: weather --json ${location}

  - id: confirm
    approval: Want jacket advice from the LLM?
    stdin: $fetch.json

  - id: advice
    pipeline: >
      llm.invoke --prompt "Given this weather data, should I wear a jacket?
      Be concise and return JSON."
    stdin: $fetch.json
    when: $confirm.approved
```

Notes:

- `run:` and `command:` are equivalent; `run:` is the preferred spelling for new files.
- `pipeline:` shares the same args/env/results model as shell steps, so later steps can still reference `$step.stdout` or `$step.json`.
- If you need a human checkpoint before an LLM call, use a dedicated `approval:` step in the workflow file rather than `approve` inside the nested pipeline.
- `cwd`, `env`, `stdin`, `when`, and `condition` work for both shell and pipeline steps.

## Calling LLMs from workflows

Use `llm.invoke` from a native `pipeline:` step for model-backed work:

```bash
llm.invoke --prompt 'Summarize this diff'
llm.invoke --provider openclaw --prompt 'Summarize this diff'
llm.invoke --provider pi --prompt 'Summarize this diff'
```

Provider resolution order:

- `--provider`
- `LOBSTER_LLM_PROVIDER`
- auto-detect from environment

Built-in providers today:

- `openclaw` via `OPENCLAW_URL` / `OPENCLAW_TOKEN`
- `pi` via `LOBSTER_PI_LLM_ADAPTER_URL` (typically supplied by the Pi extension)
- `http` via `LOBSTER_LLM_ADAPTER_URL`

`llm_task.invoke` remains available as a backward-compatible alias for the OpenClaw provider.

## Calling OpenClaw tools from workflows

Shell `run:` steps execute in your system shell, so OpenClaw tool calls there must be real executables.

If you install Lobster via npm/pnpm, it installs a small shim executable named:

- `openclaw.invoke` (preferred)
- `clawd.invoke` (alias)

These shims forward to the Lobster pipeline command of the same name.

### Example: invoke llm-task

Prereqs:

- `OPENCLAW_URL` points at a running OpenClaw gateway
- optionally `OPENCLAW_TOKEN` if auth is enabled

```bash
export OPENCLAW_URL=http://127.0.0.1:18789
# export OPENCLAW_TOKEN=...
```

In a workflow:

```yaml
name: hello-world
steps:
  - id: greeting
    run: >
      openclaw.invoke --tool llm-task --action json --args-json '{"prompt":"Hello"}'
```

### Passing data between steps (no temp files)

Use `stdin: $stepId.stdout` to pipe output from one step into the next.

## Args and shell-safety

`${arg}` substitution is a raw string replace into the shell command text.

For anything that may contain quotes, `$`, backticks, or newlines, prefer env vars:

- every resolved workflow arg is exposed as `LOBSTER_ARG_<NAME>` (uppercased, non-alnum → `_`)
- the full args object is also available as `LOBSTER_ARGS_JSON`

Example:

```yaml
args:
  text:
    default: ""
steps:
  - id: safe
    env:
      TEXT: "$LOBSTER_ARG_TEXT"
    command: |
      jq -n --arg text "$TEXT" '{"result": $text}'
```
```

## File: `VISION.md`
```markdown
# Lobster: Vision & Value Proposition

## One-liner

**Lobster is safe automation for OpenClaw — workflows that ask before acting.**

---

## What is Lobster?

Lobster is a workflow runtime for OpenClaw. It lets you define multi-step automations that:

- Run deterministically (no LLM re-planning each step)
- Halt at checkpoints and ask for approval before side effects
- Resume exactly where they left off
- Remember what they've already processed

Think of it as **IFTTT/Zapier for OpenClaw, but with human checkpoints**.

---

## The Problem Lobster Solves

### Today's workflow in OpenClaw

```
User: "Check my email, draft replies to anything urgent, and send them"

What happens:
1. LLM plans: "I should search emails first"
2. Tool call: gmail.search
3. LLM interprets results, plans next step
4. Tool call: gmail.get (for each email)
5. LLM drafts replies
6. LLM decides to send
7. Tool call: gmail.send
... repeat for each email
```

**Problems:**
- Many tool calls = many tokens = expensive
- LLM decides when to send = risky (what if it misunderstands?)
- No memory = tomorrow it re-triages the same emails
- Not repeatable = you can't save this as an automation

### With Lobster

```
OpenClaw calls: lobster.run("email.triage")

What happens:
1. Lobster fetches emails (deterministic)
2. Lobster classifies them (rule-based)
3. Lobster drafts replies (optional LLM step)
4. Lobster HALTS: "Send 3 drafts? [approve/reject]"
5. User approves
6. Lobster sends

Tomorrow: Lobster remembers cursor, only processes new emails
```

**One call. Deterministic. Safe. Stateful.**

---

## Why Lobster Makes OpenClaw Better

| Without Lobster | With Lobster |
|-----------------|--------------|
| LLM orchestrates every step | Deterministic pipeline, LLM only for judgment |
| 10+ tool calls per workflow | 1 call to Lobster |
| "Don't send until I confirm" (hope it listens) | `approve` halts execution until explicit resume |
| Forgets what it did yesterday | Stateful — tracks cursors/checkpoints |
| Hard to share automations | Workflows are code — shareable, versionable |

### Token savings (real)
A 10-step workflow today might cost 10 tool calls × LLM planning overhead.
With Lobster: 1 tool call + compact structured output.

### Safety (the killer feature)
The `approve` primitive isn't a prompt hint — it's a **hard stop**. The workflow literally cannot continue until you resume it. No "oops, it sent 50 emails."

### Memory (underrated)
Workflows can persist state: "last processed email ID", "last PR SHA seen", etc. Tomorrow's run picks up where yesterday left off.

---

## How Lobster Fits with OpenClaw

```
┌─────────────────────────────────────────────────┐
│                   User                          │
│         "triage my email daily"                 │
└─────────────────────┬───────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────┐
│                 OpenClaw                       │
│   - Understands intent                          │
│   - Chooses appropriate tool/workflow           │
│   - Presents results and approval prompts       │
└─────────────────────┬───────────────────────────┘
                      │ lobster.run("email.triage")
                      ▼
┌─────────────────────────────────────────────────┐
│                  Lobster                        │
│   - Executes deterministic pipeline             │
│   - Calls OpenClaw tools (gmail, trello, etc)  │
│   - Halts at approval checkpoints               │
│   - Returns structured result + resume token    │
└─────────────────────────────────────────────────┘
```

**Key insight:** Lobster doesn't replace OpenClaw. It's the execution layer that makes OpenClaw's automations safe and efficient.

- **OpenClaw** = the brain (understands what you want)
- **Lobster** = the hands (executes workflows safely)
- **Tools/Skills** = the capabilities (gmail, trello, github, etc.)

---

## Who Should Use Lobster?

### Average OpenClaw users (invisible benefit)
They don't need to know Lobster exists. They just notice:
- "Set up daily email triage" works better
- Automations ask before sending/posting
- Things don't get re-processed every day

### Power users / tinkerers
They can:
- Customize workflows ("I want triage to also create Trello cards")
- Write new workflows for their specific needs
- Share workflows with the community

### The OpenClaw ecosystem
- Workflow recipes become a new category of shareable assets
- Skills stay simple (just expose APIs)
- Lobster handles the orchestration layer

---

## Analogies That Work

| If you know... | Lobster is like... |
|----------------|-------------------|
| IFTTT/Zapier | Multi-step version with approval checkpoints |
| GitHub Actions | But for personal automation, not CI/CD |
| AWS Step Functions | But local-first and human-in-the-loop |
| Unix pipes | But for JSON objects, not text bytes |
| Temporal | But 80/20 version for personal workflows |

**Best analogy for most people:**
> "Lobster is Zapier for OpenClaw, except it asks you before doing anything irreversible."

---

## Why Not Build This Into OpenClaw Core?

It could be. But the plugin architecture is intentional:

1. **Core stays small** — OpenClaw is already complex
2. **Faster iteration** — Lobster can evolve without core releases
3. **Opt-in** — Not everyone needs workflow automation
4. **Community** — Easier to contribute workflows than core changes
5. **Ecosystem proof** — If plugins work for Lobster, they work for other capabilities

OpenClaw explicitly provides a plugin boundary to enable this pattern. Lobster is the first proof that it works.

---

## Example Workflows

### Email triage (flagship)
```
gog.gmail.search --query "newer_than:1d" 
  | email.normalize 
  | email.classify 
  | where bucket==needs_reply 
  | draft.reply 
  | approve --prompt "Send N replies?" 
  | gog.gmail.send
```

### PR monitor
```
github.pr.get --repo org/repo --pr 123
  | diff.last
  | where changed==true
  | notify --channel telegram --message "PR updated: {summary}"
```

### Daily planning
```
calendar.today
  | join tasks.today
  | prioritize
  | format.plan
  | approve --prompt "Post to #daily?"
  | message.send --channel slack --to "#daily"
```

### Inbox → Trello
```
email.triage
  | where bucket==needs_action
  | to.trelloCard
  | approve --prompt "Create N cards?"
  | trello.card.create --list "Inbox"
```

---

## The USP (Unique Selling Proposition)

**"Automations that ask before acting."**

Other automation tools either:
- Run blindly (IFTTT, Zapier) — scary for important actions
- Require complex configuration for approvals
- Don't integrate with your AI assistant

Lobster is:
- Native to OpenClaw (uses the same tools you already have)
- Safe by default (approvals are a language primitive)
- Invisible when you want (OpenClaw uses it automatically)
- Customizable when you need (write your own workflows)

---

## What Lobster Is NOT

- **Not a terminal replacement** — You don't switch your shell to Lobster
- **Not a general programming language** — It's for workflows, not apps
- **Not trying to replace OpenClaw** — It makes OpenClaw better
- **Not managing your secrets** — OpenClaw handles auth, Lobster orchestrates

---

## Summary

| Question | Answer |
|----------|--------|
| What is it? | Workflow runtime for OpenClaw |
| One-liner? | Safe automation — workflows that ask before acting |
| Why use it? | Cheaper, safer, stateful automations |
| Who uses it? | Everyone (invisibly) or power users (directly) |
| Why not in core? | Plugin architecture — core stays small, capabilities are extensions |
| Best analogy? | Zapier for OpenClaw, but with approval checkpoints |
```

## File: `package.json`
```json
{
  "name": "@clawdbot/lobster",
  "version": "2026.1.21-1",
  "description": "Workflow runtime for AI agents - deterministic pipelines with approval gates",
  "type": "module",
  "bin": {
    "lobster": "bin/lobster.js",
    "openclaw.invoke": "bin/openclaw.invoke.js",
    "clawd.invoke": "bin/clawd.invoke.js"
  },
  "files": [
    "bin",
    "dist",
    "README.md",
    "LICENSE",
    "VISION.md"
  ],
  "exports": {
    ".": "./dist/src/sdk/index.js",
    "./sdk": "./dist/src/sdk/index.js",
    "./core": "./dist/src/core/index.js",
    "./recipes/github": "./dist/src/recipes/github/index.js"
  },
  "main": "./dist/src/sdk/index.js",
  "scripts": {
    "clean": "rm -rf dist",
    "build": "pnpm clean && tsc -p tsconfig.json",
    "prepack": "pnpm build",
    "typecheck": "tsc -p tsconfig.json --noEmit",
    "lint": "oxlint --tsconfig tsconfig.json src test",
    "fmt": "oxlint --tsconfig tsconfig.json --fix src test",
    "test": "pnpm build && node --test dist/test/*.test.js"
  },
  "devDependencies": {
    "@types/node": "^22.0.0",
    "oxlint": "^0.15.0",
    "typescript": "^5.7.0"
  },
  "engines": {
    "node": ">=20"
  },
  "keywords": [
    "workflow",
    "automation",
    "ai-agent",
    "approval",
    "pipeline",
    "lobster",
    "openclaw"
  ],
  "repository": {
    "type": "git",
    "url": "git+https://github.com/openclaw/lobster.git"
  },
  "bugs": {
    "url": "https://github.com/openclaw/lobster/issues"
  },
  "homepage": "https://github.com/openclaw/lobster#readme",
  "license": "MIT",
  "dependencies": {
    "ajv": "^8.17.1",
    "yaml": "^2.8.2"
  }
}
```

## File: `tsconfig.json`
```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "lib": ["ES2022"],
    "types": ["node"],
    "rootDir": ".",
    "outDir": "dist",
    "declaration": false,
    "sourceMap": true,
    "strict": false,
    "useUnknownInCatchVariables": false,
    "noImplicitAny": false,
    "skipLibCheck": true,
    "noEmitOnError": true
  },
  "include": ["src/**/*.ts", "test/**/*.ts"],
  "exclude": ["dist", "node_modules"]
}
```

## File: `src/cli.ts`
```typescript
import { parsePipeline } from './parser.js';
import { createDefaultRegistry } from './commands/registry.js';
import { runPipeline } from './runtime.js';
import { encodeToken } from './token.js';
import { decodeResumeToken, parseResumeArgs } from './resume.js';
import { runWorkflowFile } from './workflows/file.js';
import { randomUUID } from 'node:crypto';
import { deleteStateJson, readStateJson, writeStateJson } from './state/store.js';

type PipelineResumeState = {
  pipeline: Array<{ name: string; args: Record<string, unknown>; raw: string }>;
  resumeAtIndex: number;
  items: unknown[];
  prompt?: string;
  createdAt: string;
};

export async function runCli(argv) {
  const registry = createDefaultRegistry();

  if (argv.length === 0 || argv.includes('-h') || argv.includes('--help')) {
    process.stdout.write(helpText());
    return;
  }

  if (argv[0] === 'help') {
    const topic = argv[1];
    if (!topic) {
      process.stdout.write(helpText());
      return;
    }
    const cmd = registry.get(topic);
    if (!cmd) {
      process.stderr.write(`Unknown command: ${topic}\n`);
      process.exitCode = 2;
      return;
    }
    process.stdout.write(cmd.help());
    return;
  }

  if (argv[0] === 'version' || argv[0] === '--version' || argv[0] === '-v') {
    process.stdout.write(`${await readVersion()}\n`);
    return;
  }

  if (argv[0] === 'doctor') {
    await handleDoctor({ argv: argv.slice(1), registry });
    return;
  }

  if (argv[0] === 'run') {
    await handleRun({ argv: argv.slice(1), registry });
    return;
  }

  if (argv[0] === 'resume') {
    await handleResume({ argv: argv.slice(1), registry });
    return;
  }

  // Default: treat argv as a pipeline string.
  await handleRun({ argv, registry });
}

async function handleRun({ argv, registry }) {
  const { mode, rest, filePath, argsJson } = parseRunArgs(argv);
  const normalizedMode = normalizeMode(mode);

  const workflowFile = filePath
    ? await resolveWorkflowFile(filePath)
    : await detectWorkflowFile(rest);
  if (workflowFile) {
    let parsedArgs = {};
    if (argsJson) {
      try {
        parsedArgs = JSON.parse(argsJson);
      } catch {
        if (mode === 'tool') {
          writeToolEnvelope({ ok: false, error: { type: 'parse_error', message: 'run --args-json must be valid JSON' } });
          process.exitCode = 2;
          return;
        }
        process.stderr.write('run --args-json must be valid JSON\n');
        process.exitCode = 2;
        return;
      }
    }

    try {
      const output = await runWorkflowFile({
        filePath: workflowFile,
        args: parsedArgs,
        ctx: {
          stdin: process.stdin,
          stdout: process.stdout,
          stderr: process.stderr,
          env: process.env,
          mode: normalizedMode,
          registry,
        },
      });

      if (normalizedMode === 'tool') {
        if (output.status === 'needs_approval') {
          writeToolEnvelope({
            ok: true,
            status: 'needs_approval',
            output: [],
            requiresApproval: output.requiresApproval ?? null,
          });
          return;
        }

        writeToolEnvelope({
          ok: true,
          status: 'ok',
          output: output.output,
          requiresApproval: null,
        });
        return;
      }

      if (output.status === 'ok' && output.output.length) {
        process.stdout.write(JSON.stringify(output.output, null, 2));
        process.stdout.write('\n');
      }
      return;
    } catch (err) {
      if (normalizedMode === 'tool') {
        writeToolEnvelope({ ok: false, error: { type: 'runtime_error', message: err?.message ?? String(err) } });
        process.exitCode = 1;
        return;
      }
      process.stderr.write(`Error: ${err?.message ?? String(err)}\n`);
      process.exitCode = 1;
      return;
    }
  }

  const pipelineString = rest.join(' ');

  let pipeline;
  try {
    pipeline = parsePipeline(pipelineString);
  } catch (err) {
    if (mode === 'tool') {
      writeToolEnvelope({ ok: false, error: { type: 'parse_error', message: err?.message ?? String(err) } });
      process.exitCode = 2;
      return;
    }
    process.stderr.write(`Parse error: ${err?.message ?? String(err)}\n`);
    process.exitCode = 2;
    return;
  }

  try {
    const output = await runPipeline({
      pipeline,
      registry,
      input: [],
      stdin: process.stdin,
      stdout: process.stdout,
      stderr: process.stderr,
      env: process.env,
      mode: normalizedMode,
    });

    if (normalizedMode === 'tool') {
      const approval = output.halted && output.items.length === 1 && output.items[0]?.type === 'approval_request'
        ? output.items[0]
        : null;

      if (approval) {
        const stateKey = await savePipelineResumeState(process.env, {
          pipeline,
          resumeAtIndex: (output.haltedAt?.index ?? -1) + 1,
          items: approval.items,
          prompt: approval.prompt,
          createdAt: new Date().toISOString(),
        });

        const resumeToken = encodeToken({
          protocolVersion: 1,
          v: 1,
          kind: 'pipeline-resume',
          stateKey,
        });

        writeToolEnvelope({
          ok: true,
          status: 'needs_approval',
          output: [],
          requiresApproval: {
            ...approval,
            resumeToken,
          },
        });
        return;
      }

      writeToolEnvelope({
        ok: true,
        status: 'ok',
        output: output.items,
        requiresApproval: null,
      });
      return;
    }

    // Human mode: if the last command didn't render, print JSON.
    if (!output.rendered) {
      process.stdout.write(JSON.stringify(output.items, null, 2));
      process.stdout.write('\n');
    }
  } catch (err) {
    if (normalizedMode === 'tool') {
      writeToolEnvelope({ ok: false, error: { type: 'runtime_error', message: err?.message ?? String(err) } });
      process.exitCode = 1;
      return;
    }
    process.stderr.write(`Error: ${err?.message ?? String(err)}\n`);
    process.exitCode = 1;
  }
}

function parseRunArgs(argv) {
  const rest = [];
  let mode = 'human';
  let filePath = null;
  let argsJson = null;

  for (let i = 0; i < argv.length; i++) {
    const tok = argv[i];

    if (tok === '--mode') {
      const value = argv[i + 1];
      if (value) {
        mode = value;
        i++;
      }
      continue;
    }

    if (tok.startsWith('--mode=')) {
      mode = tok.slice('--mode='.length) || 'human';
      continue;
    }

    if (tok === '--file') {
      const value = argv[i + 1];
      if (value) {
        filePath = value;
        i++;
      }
      continue;
    }

    if (tok.startsWith('--file=')) {
      filePath = tok.slice('--file='.length);
      continue;
    }

    if (tok === '--args-json') {
      const value = argv[i + 1];
      if (value) {
        argsJson = value;
        i++;
      }
      continue;
    }

    if (tok.startsWith('--args-json=')) {
      argsJson = tok.slice('--args-json='.length);
      continue;
    }

    rest.push(tok);
  }

  return { mode, rest, filePath, argsJson };
}

function normalizeMode(mode) {
  return mode === 'tool' ? 'tool' : 'human';
}

async function detectWorkflowFile(rest) {
  if (rest.length !== 1) return null;
  const candidate = rest[0];
  if (!candidate || candidate.includes('|')) return null;
  try {
    return await resolveWorkflowFile(candidate);
  } catch {
    return null;
  }
}

async function resolveWorkflowFile(candidate) {
  const { promises: fsp } = await import('node:fs');
  const { resolve, extname, isAbsolute } = await import('node:path');
  const resolved = isAbsolute(candidate) ? candidate : resolve(process.cwd(), candidate);
  const stat = await fsp.stat(resolved);
  if (!stat.isFile()) throw new Error('Workflow path is not a file');

  const ext = extname(resolved).toLowerCase();
  if (!['.lobster', '.yaml', '.yml', '.json'].includes(ext)) {
    throw new Error('Workflow file must end in .lobster, .yaml, .yml, or .json');
  }

  return resolved;
}

async function handleResume({ argv, registry }) {
  const mode = 'tool';
  let approved: boolean;
  let payload: any;
  try {
    const parsed = parseResumeArgs(argv);
    approved = parsed.approved;
    payload = decodeResumeToken(parsed.token);
  } catch (err) {
    writeToolEnvelope({ ok: false, error: { type: 'parse_error', message: err?.message ?? String(err) } });
    process.exitCode = 2;
    return;
  }

  if (!approved) {
    if (payload.kind === 'workflow-file' && payload.stateKey) {
      await deleteStateJson({ env: process.env, key: payload.stateKey });
    }
    if (payload.kind === 'pipeline-resume' && payload.stateKey) {
      await deleteStateJson({ env: process.env, key: payload.stateKey });
    }
    writeToolEnvelope({ ok: true, status: 'cancelled', output: [], requiresApproval: null });
    return;
  }

  if (payload.kind === 'workflow-file') {
    try {
      const output = await runWorkflowFile({
        filePath: payload.filePath,
        ctx: {
          stdin: process.stdin,
          stdout: process.stdout,
          stderr: process.stderr,
          env: process.env,
          mode: 'tool',
          registry,
        },
        resume: payload,
        approved: true,
      });

      if (output.status === 'needs_approval') {
        writeToolEnvelope({
          ok: true,
          status: 'needs_approval',
          output: [],
          requiresApproval: output.requiresApproval ?? null,
        });
        return;
      }

      writeToolEnvelope({ ok: true, status: 'ok', output: output.output, requiresApproval: null });
      return;
    } catch (err) {
      writeToolEnvelope({ ok: false, error: { type: 'runtime_error', message: err?.message ?? String(err) } });
      process.exitCode = 1;
      return;
    }
  }
  const previousStateKey = payload.stateKey;
  let resumeState: PipelineResumeState;
  try {
    resumeState = await loadPipelineResumeState(process.env, previousStateKey);
  } catch (err) {
    writeToolEnvelope({ ok: false, error: { type: 'runtime_error', message: err?.message ?? String(err) } });
    process.exitCode = 1;
    return;
  }
  const remaining = resumeState.pipeline.slice(resumeState.resumeAtIndex);
  const input = streamFromItems(resumeState.items);

  try {
    const output = await runPipeline({
      pipeline: remaining,
      registry,
      stdin: process.stdin,
      stdout: process.stdout,
      stderr: process.stderr,
      env: process.env,
      mode,
      input,
    });

    const approval = output.halted && output.items.length === 1 && output.items[0]?.type === 'approval_request'
      ? output.items[0]
      : null;

    if (approval) {
      const nextStateKey = await savePipelineResumeState(process.env, {
        pipeline: remaining,
        resumeAtIndex: (output.haltedAt?.index ?? -1) + 1,
        items: approval.items,
        prompt: approval.prompt,
        createdAt: new Date().toISOString(),
      });
      await deleteStateJson({ env: process.env, key: previousStateKey });

      const resumeToken = encodeToken({
        protocolVersion: 1,
        v: 1,
        kind: 'pipeline-resume',
        stateKey: nextStateKey,
      });

      writeToolEnvelope({
        ok: true,
        status: 'needs_approval',
        output: [],
        requiresApproval: { ...approval, resumeToken },
      });
      return;
    }

    await deleteStateJson({ env: process.env, key: previousStateKey });
    writeToolEnvelope({ ok: true, status: 'ok', output: output.items, requiresApproval: null });
  } catch (err) {
    writeToolEnvelope({ ok: false, error: { type: 'runtime_error', message: err?.message ?? String(err) } });
    process.exitCode = 1;
  }
}

function streamFromItems(items: unknown[]) {
  return (async function* () {
    for (const item of items) yield item;
  })();
}

async function savePipelineResumeState(env: Record<string, string | undefined>, state: PipelineResumeState) {
  const stateKey = `pipeline_resume_${randomUUID()}`;
  await writeStateJson({ env, key: stateKey, value: state });
  return stateKey;
}

async function loadPipelineResumeState(env: Record<string, string | undefined>, stateKey: string) {
  const stored = await readStateJson({ env, key: stateKey });
  if (!stored || typeof stored !== 'object') {
    throw new Error('Pipeline resume state not found');
  }
  const data = stored as Partial<PipelineResumeState>;
  if (!Array.isArray(data.pipeline)) throw new Error('Invalid pipeline resume state');
  if (typeof data.resumeAtIndex !== 'number') throw new Error('Invalid pipeline resume state');
  if (!Array.isArray(data.items)) throw new Error('Invalid pipeline resume state');
  return data as PipelineResumeState;
}

async function readVersion() {
  const { readFile } = await import('node:fs/promises');
  const { fileURLToPath } = await import('node:url');
  const { dirname, join } = await import('node:path');

  const here = dirname(fileURLToPath(import.meta.url));
  const pkgPath = join(here, '..', '..', 'package.json');
  const pkg = JSON.parse(await readFile(pkgPath, 'utf8'));
  return pkg.version ?? '0.0.0';
}

async function handleDoctor({ argv, registry }) {
  const mode = 'tool';
  const pipeline = "exec --json --shell 'echo [1]'";
  const output: any = await (async () => {
    try {
      const parsed = parsePipeline(pipeline);
      return await runPipeline({
        pipeline: parsed,
        registry,
        input: [],
        stdin: process.stdin,
        stdout: process.stdout,
        stderr: process.stderr,
        env: process.env,
        mode,
      });
    } catch (err: any) {
      return { error: err };
    }
  })();

  if (output?.error) {
    writeToolEnvelope({
      ok: false,
      error: { type: 'doctor_error', message: output.error?.message ?? String(output.error) },
    });
    process.exitCode = 1;
    return;
  }

  writeToolEnvelope({
    ok: true,
    status: 'ok',
    output: [{
      toolMode: true,
      protocolVersion: 1,
      version: await readVersion(),
      notes: argv.length ? argv : undefined,
    }],
    requiresApproval: null,
  });
}

function writeToolEnvelope(payload) {
  const envelope = {
    protocolVersion: 1,
    ...payload,
  };
  process.stdout.write(JSON.stringify(envelope, null, 2));
  process.stdout.write('\n');
}

function helpText() {
  return `lobster — OpenClaw-native typed shell\n\n` +
    `Usage:\n` +
    `  lobster '<pipeline>'\n` +
    `  lobster run --mode tool '<pipeline>'\n` +
    `  lobster run path/to/workflow.lobster\n` +
    `  lobster run --file path/to/workflow.lobster --args-json '{...}'\n` +
    `  lobster resume --token <token> --approve yes|no\n` +
    `  lobster doctor\n` +
    `  lobster version\n` +
    `  lobster help <command>\n\n` +
    `Modes:\n` +
    `  - human (default): renderers can write to stdout\n` +
    `  - tool: prints a single JSON envelope for easy integration\n\n` +
    `Examples:\n` +
    `  lobster 'exec --json "echo [1,2,3]" | json'\n` +
    `  lobster run --mode tool 'exec --json "echo [1]" | approve --prompt "ok?"'\n\n` +
    `Commands:\n` +
    `  exec, head, json, pick, table, where, approve, openclaw.invoke, llm.invoke, llm_task.invoke, state.get, state.set, diff.last, commands.list, workflows.list, workflows.run\n`;
}
```

## File: `src/parser.ts`
```typescript
function isWhitespace(ch) {
  return ch === ' ' || ch === '\t' || ch === '\n' || ch === '\r';
}

function splitPipes(input) {
  const parts = [];
  let current = '';
  let quote = null;

  for (let i = 0; i < input.length; i++) {
    const ch = input[i];

    if (quote) {
      if (ch === '\\') {
        const next = input[i + 1];
        if (next) {
          current += ch + next;
          i++;
          continue;
        }
      }
      current += ch;
      if (ch === quote) {
        quote = null;
      }
      continue;
    }

    if (ch === '"' || ch === "'") {
      quote = ch;
      current += ch;
      continue;
    }

    if (ch === '|') {
      parts.push(current.trim());
      current = '';
      continue;
    }

    current += ch;
  }

  if (quote) throw new Error('Unclosed quote');
  if (current.trim().length > 0) parts.push(current.trim());
  return parts;
}

function tokenizeCommand(input) {
  const tokens = [];
  let current = '';
  let quote = null;

  const push = () => {
    if (current.length > 0) tokens.push(current);
    current = '';
  };

  for (let i = 0; i < input.length; i++) {
    const ch = input[i];

    if (quote) {
      if (ch === '\\') {
        const next = input[i + 1];
        if (next) {
          current += next;
          i++;
          continue;
        }
      }
      if (ch === quote) {
        quote = null;
        continue;
      }
      current += ch;
      continue;
    }

    if (ch === '"' || ch === "'") {
      quote = ch;
      continue;
    }

    if (isWhitespace(ch)) {
      push();
      continue;
    }

    current += ch;
  }

  if (quote) throw new Error('Unclosed quote');
  push();
  return tokens;
}

function parseArgs(tokens) {
  const args = { _: [] };

  for (let i = 0; i < tokens.length; i++) {
    const tok = tokens[i];

    if (tok.startsWith('--')) {
      const eq = tok.indexOf('=');
      if (eq !== -1) {
        const key = tok.slice(2, eq);
        const value = tok.slice(eq + 1);
        args[key] = value;
        continue;
      }

      const key = tok.slice(2);
      const next = tokens[i + 1];
      if (!next || next.startsWith('--')) {
        args[key] = true;
        continue;
      }
      args[key] = next;
      i++;
      continue;
    }

    args._.push(tok);
  }

  return args;
}

export function parsePipeline(input) {
  const stages = splitPipes(input);
  if (stages.length === 0) throw new Error('Empty pipeline');

  return stages.map((stage) => {
    const tokens = tokenizeCommand(stage);
    if (tokens.length === 0) throw new Error('Empty command stage');
    const name = tokens[0];
    const args = parseArgs(tokens.slice(1));
    return { name, args, raw: stage };
  });
}
```

## File: `src/read_line.ts`
```typescript
export function readLineFromStream(
  stream: NodeJS.ReadableStream,
  opts?: { timeoutMs?: number },
) {
  const timeoutMs = Number(opts?.timeoutMs ?? 0);

  return new Promise<string>((resolve, reject) => {
    let settled = false;
    let buf = '';
    let timer: NodeJS.Timeout | null = null;

    const cleanup = () => {
      stream.off('data', onData);
      stream.off('end', onEnd);
      stream.off('close', onClose);
      stream.off('error', onError);
      if (timer) clearTimeout(timer);
    };

    const finish = (value: string) => {
      if (settled) return;
      settled = true;
      cleanup();
      resolve(value);
    };

    const fail = (err: Error) => {
      if (settled) return;
      settled = true;
      cleanup();
      reject(err);
    };

    const onData = (chunk: Buffer | string) => {
      buf += Buffer.isBuffer(chunk) ? chunk.toString('utf8') : String(chunk);
      const idx = buf.indexOf('\n');
      if (idx !== -1) {
        finish(buf.slice(0, idx));
      }
    };

    const onEnd = () => finish(buf);
    const onClose = () => finish(buf);
    const onError = (err: Error) => fail(err);

    if (timeoutMs > 0) {
      timer = setTimeout(() => {
        fail(new Error(`Timed out waiting for input (${timeoutMs}ms)`));
      }, timeoutMs);
    }

    stream.on('data', onData);
    stream.on('end', onEnd);
    stream.on('close', onClose);
    stream.on('error', onError);
  });
}
```

## File: `src/resume.ts`
```typescript
import { decodeToken } from './token.js';
import { decodeWorkflowResumePayload } from './workflows/file.js';

export type PipelineResumePayload = {
  protocolVersion: 1;
  v: 1;
  kind: 'pipeline-resume';
  stateKey: string;
};

export function parseResumeArgs(argv) {
  const args = { decision: null, token: null };

  for (let i = 0; i < argv.length; i++) {
    const tok = argv[i];
    if (tok === '--token') {
      args.token = argv[i + 1];
      i++;
      continue;
    }
    if (tok.startsWith('--token=')) {
      args.token = tok.slice('--token='.length);
      continue;
    }
    if (tok === '--approve' || tok === '--decision') {
      args.decision = argv[i + 1];
      i++;
      continue;
    }
    if (tok.startsWith('--approve=')) {
      args.decision = tok.slice('--approve='.length);
      continue;
    }
    if (tok.startsWith('--decision=')) {
      args.decision = tok.slice('--decision='.length);
      continue;
    }
  }

  if (!args.token) throw new Error('resume requires --token');
  if (!args.decision) throw new Error('resume requires --approve yes|no');

  const decision = String(args.decision).toLowerCase();
  if (!['yes', 'y', 'no', 'n'].includes(decision)) throw new Error('resume --approve must be yes or no');

  return { token: String(args.token), approved: decision === 'yes' || decision === 'y' };
}

export function decodeResumeToken(token) {
  const payload = decodeToken(token);
  if (!payload || typeof payload !== 'object') throw new Error('Invalid token');
  if (payload.protocolVersion !== 1) throw new Error('Unsupported protocol version');
  if (payload.v !== 1) throw new Error('Unsupported token version');
  const workflowPayload = decodeWorkflowResumePayload(payload);
  if (workflowPayload) return workflowPayload;
  const pipelinePayload = decodePipelineResumePayload(payload);
  if (pipelinePayload) return pipelinePayload;
  throw new Error('Invalid token');
}

function decodePipelineResumePayload(payload: unknown): PipelineResumePayload | null {
  if (!payload || typeof payload !== 'object') return null;
  const data = payload as Partial<PipelineResumePayload>;
  if (data.kind !== 'pipeline-resume') return null;
  if (data.protocolVersion !== 1 || data.v !== 1) throw new Error('Unsupported token version');
  if (!data.stateKey || typeof data.stateKey !== 'string') throw new Error('Invalid token');
  return {
    protocolVersion: 1,
    v: 1,
    kind: 'pipeline-resume',
    stateKey: data.stateKey,
  };
}
```

## File: `src/runtime.ts`
```typescript
import { createJsonRenderer } from './renderers/json.js';

export async function runPipeline({
  pipeline,
  registry,
  stdin,
  stdout,
  stderr,
  env,
  mode = 'human',
  input,
  cwd = undefined,
  llmAdapters = undefined,
  signal = undefined,
}: {
  pipeline: any[];
  registry: any;
  stdin: any;
  stdout: any;
  stderr: any;
  env: any;
  mode?: string;
  input?: any;
  cwd?: string | undefined;
  llmAdapters?: Record<string, any> | undefined;
  signal?: AbortSignal | undefined;
}) {
  let stream = input ?? emptyStream();
  let rendered = false;
  let halted = false;
  let haltedAt = null;

  const ctx = {
    stdin,
    stdout,
    stderr,
    env,
    registry,
    mode,
    cwd,
    llmAdapters,
    signal,
    render: createJsonRenderer(stdout),
  };

  for (let idx = 0; idx < pipeline.length; idx++) {
    const stage = pipeline[idx];
    const command = registry.get(stage.name);
    if (!command) {
      throw new Error(`Unknown command: ${stage.name}`);
    }

    const result = await command.run({ input: stream, args: stage.args, ctx });

    if (result?.rendered) {
      rendered = true;
    }

    if (result?.halt) {
      halted = true;
      haltedAt = { index: idx, stage };
      stream = result.output ?? emptyStream();
      break;
    }

    stream = result?.output ?? emptyStream();
  }

  const items = [];
  for await (const item of stream) items.push(item);

  return { items, rendered, halted, haltedAt };
}

async function* emptyStream() {}
```

## File: `src/shell.ts`
```typescript
export function resolveInlineShellCommand({
  command,
  env,
  platform = process.platform,
}: {
  command: string;
  env: Record<string, string | undefined>;
  platform?: string;
}) {
  const shellOverride = String(env?.LOBSTER_SHELL ?? '').trim();
  const isWindows = platform === 'win32';

  if (shellOverride) {
    return {
      command: shellOverride,
      argv: buildShellArgs({ shellCommand: shellOverride, command, isWindows }),
    };
  }

  if (isWindows) {
    const comspec = String(env?.ComSpec ?? env?.COMSPEC ?? 'cmd.exe').trim() || 'cmd.exe';
    return {
      command: comspec,
      argv: ['/d', '/s', '/c', command],
    };
  }

  // Keep default behavior deterministic and POSIX-compatible across environments.
  const shell = '/bin/sh';
  return {
    command: shell,
    argv: ['-lc', command],
  };
}

function buildShellArgs({
  shellCommand,
  command,
  isWindows,
}: {
  shellCommand: string;
  command: string;
  isWindows: boolean;
}) {
  const lowered = shellCommand.toLowerCase();
  const looksLikeCmd = lowered.endsWith('cmd') || lowered.endsWith('cmd.exe');
  const looksLikePowerShell =
    lowered.endsWith('powershell') ||
    lowered.endsWith('powershell.exe') ||
    lowered.endsWith('pwsh') ||
    lowered.endsWith('pwsh.exe');

  if (looksLikePowerShell) {
    return ['-NoProfile', '-Command', command];
  }
  if (looksLikeCmd || isWindows) {
    return ['/d', '/s', '/c', command];
  }
  return ['-lc', command];
}
```

## File: `src/token.ts`
```typescript
import { Buffer } from 'node:buffer';

export function encodeToken(obj) {
  const json = JSON.stringify(obj);
  return Buffer.from(json, 'utf8').toString('base64url');
}

export function decodeToken(token) {
  try {
    const json = Buffer.from(String(token), 'base64url').toString('utf8');
    return JSON.parse(json);
  } catch (_err) {
    throw new Error('Invalid token');
  }
}
```

## File: `src/commands/commands_list.ts`
```typescript
import type { CommandMeta, LobsterCommand } from './types.js';

function parseDescriptionFromHelp(helpText: string): string {
  const firstLine = helpText.split('\n').find((l) => l.trim().length > 0) ?? '';
  // Expected pattern: "name — description" but fall back to the line as-is.
  return firstLine.includes('—') ? firstLine.split('—').slice(1).join('—').trim() : firstLine.trim();
}

export const commandsListCommand: LobsterCommand = {
  name: 'commands.list',
  help() {
    return (
      `commands.list — list available Lobster pipeline commands\n\n` +
      `Usage:\n` +
      `  commands.list\n\n` +
      `Notes:\n` +
      `  - Intended for agents (e.g. OpenClaw) to discover available pipeline stages dynamically.\n` +
      `  - Output includes name/description plus optional metadata (argsSchema/examples/sideEffects) when provided by commands.\n`
    );
  },
  meta: {
    description: 'List available Lobster pipeline commands',
    argsSchema: { type: 'object', properties: {}, required: [] },
    sideEffects: [],
  } satisfies CommandMeta,
  async run({ input, ctx }) {
    // Drain input
    for await (const _ of input) {
      // no-op
    }

    const names = ctx.registry.list();
    const output = names.map((name) => {
      const cmd = ctx.registry.get(name) as LobsterCommand | undefined;
      const help = typeof cmd?.help === 'function' ? String(cmd.help()) : '';
      const description = cmd?.meta?.description ?? parseDescriptionFromHelp(help);

      return {
        name,
        description,
        argsSchema: cmd?.meta?.argsSchema ?? null,
        examples: cmd?.meta?.examples ?? null,
        sideEffects: cmd?.meta?.sideEffects ?? null,
      };
    });

    return {
      output: (async function* () {
        for (const item of output) yield item;
      })(),
    };
  },
};
```

## File: `src/commands/registry.ts`
```typescript
import { execCommand } from "./stdlib/exec.js";
import { headCommand } from "./stdlib/head.js";
import { jsonCommand } from "./stdlib/json.js";
import { pickCommand } from "./stdlib/pick.js";
import { tableCommand } from "./stdlib/table.js";
import { whereCommand } from "./stdlib/where.js";
import { sortCommand } from "./stdlib/sort.js";
import { dedupeCommand } from "./stdlib/dedupe.js";
import { templateCommand } from "./stdlib/template.js";
import { mapCommand } from "./stdlib/map.js";
import { groupByCommand } from "./stdlib/group_by.js";
import { approveCommand } from "./stdlib/approve.js";
import { clawdInvokeCommand, openclawInvokeCommand } from "./stdlib/openclaw_invoke.js";
import { llmInvokeCommand } from "./stdlib/llm_invoke.js";
import { llmTaskInvokeCommand } from "./stdlib/llm_task_invoke.js";
import { stateGetCommand, stateSetCommand } from "./stdlib/state.js";
import { diffLastCommand } from "./stdlib/diff_last.js";
import { workflowsListCommand } from "./workflows/workflows_list.js";
import { workflowsRunCommand } from "./workflows/workflows_run.js";
import { commandsListCommand } from "./commands_list.js";
import { gogGmailSearchCommand } from "./stdlib/gog_gmail_search.js";
import { gogGmailSendCommand } from "./stdlib/gog_gmail_send.js";
import { emailTriageCommand } from "./stdlib/email_triage.js";

export function createDefaultRegistry() {
  const commands = new Map();

  for (const cmd of [
    execCommand,
    headCommand,
    jsonCommand,
    pickCommand,
    tableCommand,
    whereCommand,
    sortCommand,
    dedupeCommand,
    templateCommand,
    mapCommand,
    groupByCommand,
    approveCommand,
    openclawInvokeCommand,
    clawdInvokeCommand,
    llmInvokeCommand,
    llmTaskInvokeCommand,
    stateGetCommand,
    stateSetCommand,
    diffLastCommand,
    workflowsListCommand,
    workflowsRunCommand,
    commandsListCommand,
    gogGmailSearchCommand,
    gogGmailSendCommand,
    emailTriageCommand,
  ]) {
    commands.set(cmd.name, cmd);
  }

  return {
    get(name) {
      return commands.get(name);
    },
    list() {
      return [...commands.keys()].sort();
    },
  };
}
```

## File: `src/commands/types.ts`
```typescript
export type CommandMeta = {
  description?: string;
  argsSchema?: unknown;
  examples?: Array<{ args: Record<string, unknown>; description?: string }>;
  sideEffects?: string[];
};

export type LobsterCommand = {
  name: string;
  help: () => string;
  run: (params: any) => Promise<any>;
  meta?: CommandMeta;
};
```

## File: `src/commands/stdlib/approve.ts`
```typescript
import { readLineFromStream } from '../../read_line.js';

function isInteractive(stdin) {
  return Boolean(stdin.isTTY);
}

export const approveCommand = {
  name: 'approve',
  meta: {
    description: 'Require confirmation to continue',
    argsSchema: {
      type: 'object',
      properties: {
        prompt: { type: 'string', description: 'Approval prompt text', default: 'Approve?' },
        emit: { type: 'boolean', description: 'Force emit approval request + halt' },
        _: { type: 'array', items: { type: 'string' } },
      },
      required: [],
    },
    sideEffects: [],
  },
  help() {
    return `approve — require confirmation to continue\n\nUsage:\n  ... | approve --prompt "Send these emails?"\n  ... | approve --emit --prompt "Send these emails?"\n  ... | approve --emit --preview-from-stdin --limit 5 --prompt "Proceed?"\n\nModes:\n  - Interactive (default): prompts on TTY and passes items through if approved.\n  - Emit (--emit): returns an approval request object and stops the pipeline.\n\nNotes:\n  - In tool mode (or non-interactive), this emits an approval request and halts.\n`;
  },
  async run({ input, args, ctx }) {
    const prompt = args.prompt ?? 'Approve?';
    const previewFromStdin = Boolean(args.previewFromStdin ?? args['preview-from-stdin']);
    const previewLimitRaw = args.limit ?? args.previewLimit ?? args['preview-limit'];
    const previewLimit = Number.isFinite(Number(previewLimitRaw)) ? Number(previewLimitRaw) : 5;

    const items = [];
    for await (const item of input) items.push(item);

    const emit = Boolean(args.emit) || ctx.mode === 'tool' || !isInteractive(ctx.stdin);

    if (emit) {
      const preview = previewFromStdin
        ? buildPreview(items.slice(0, Math.max(0, previewLimit)))
        : undefined;
      return {
        halt: true,
        output: (async function* () {
          yield {
            type: 'approval_request',
            prompt,
            items,
            ...(preview ? { preview } : null),
          };
        })(),
      };
    }

    ctx.stdout.write(`${prompt} [y/N] `);
    const answer = await readLineFromStream(ctx.stdin, {
      timeoutMs: parseApprovalTimeoutMs(ctx.env),
    });

    if (!/^y(es)?$/i.test(String(answer).trim())) {
      throw new Error('Not approved');
    }

    return { output: asStream(items) };
  },
};

function buildPreview(items) {
  if (!items.length) return '';
  if (items.every((item) => typeof item === 'string')) {
    return items.join('\n');
  }
  return JSON.stringify(items, null, 2);
}

function parseApprovalTimeoutMs(env) {
  const raw = env?.LOBSTER_APPROVAL_INPUT_TIMEOUT_MS;
  const value = Number(raw);
  if (!Number.isFinite(value) || value <= 0) return 0;
  return Math.floor(value);
}

async function* asStream(items) {
  for (const item of items) yield item;
}
```

## File: `src/commands/stdlib/dedupe.ts`
```typescript
function getByPath(obj: any, path: string): any {
  if (!path) return obj;
  const parts = path.split('.').filter(Boolean);
  let cur: any = obj;
  for (const p of parts) {
    if (cur == null) return undefined;
    cur = cur[p];
  }
  return cur;
}

export const dedupeCommand = {
  name: 'dedupe',
  meta: {
    description: 'Remove duplicate items, keeping first occurrence (stable)',
    argsSchema: {
      type: 'object',
      properties: {
        key: { type: 'string', description: 'Dot-path key used for identity (defaults to whole item)' },
        _: { type: 'array', items: { type: 'string' } },
      },
      required: [],
    },
    sideEffects: [],
  },
  help() {
    return (
      `dedupe — remove duplicate items (stable)\n\n` +
      `Usage:\n` +
      `  ... | dedupe\n` +
      `  ... | dedupe --key id\n\n` +
      `Notes:\n` +
      `  - Keeps the first occurrence.\n`
    );
  },
  async run({ input, args }: any) {
    const key = typeof args.key === 'string' ? args.key : undefined;
    const seen = new Set<string>();

    return {
      output: (async function* () {
        for await (const item of input) {
          const id = key ? getByPath(item, key) : item;
          const k = JSON.stringify(id);
          if (seen.has(k)) continue;
          seen.add(k);
          yield item;
        }
      })(),
    };
  },
};
```

## File: `src/commands/stdlib/diff_last.ts`
```typescript
import { diffAndStore } from '../../state/store.js';

export const diffLastCommand = {
  name: 'diff.last',
  meta: {
    description: 'Compare current items to last stored snapshot',
    argsSchema: {
      type: 'object',
      properties: {
        key: { type: 'string', description: 'State key to diff against' },
        _: { type: 'array', items: { type: 'string' } },
      },
      required: ['key'],
    },
    sideEffects: ['writes_state'],
  },
  help() {
    return `diff.last — compare current items to last stored snapshot\n\nUsage:\n  <items> | diff.last --key <stateKey>\n\nOutput:\n  { changed, key, before, after }\n`;
  },
  async run({ input, args, ctx }) {
    const key = args.key ?? args._[0];
    if (!key) throw new Error('diff.last requires --key');

    const afterItems = [];
    for await (const item of input) afterItems.push(item);

    const after = afterItems.length === 1 ? afterItems[0] : afterItems;
    const { before, changed } = await diffAndStore({ env: ctx.env, key, value: after });

    return {
      output: (async function* () {
        yield { kind: 'diff.last', key, changed, before, after };
      })(),
    };
  },
};
```

## File: `src/commands/stdlib/email_triage.ts`
```typescript
type EmailLike = {
  id?: string;
  threadId?: string;
  from?: string;
  subject?: string;
  date?: string;
  snippet?: string;
  labels?: string[];
};

type NormalizedEmail = Required<Pick<EmailLike, 'id' | 'threadId' | 'from' | 'subject' | 'date' | 'snippet'>> & {
  labels: string[];
};

function normalizeEmail(raw: any): NormalizedEmail {
  const id = String(raw?.id ?? raw?.messageId ?? '').trim();
  const threadId = String(raw?.threadId ?? raw?.thread_id ?? id).trim();
  const from = String(raw?.from ?? raw?.sender ?? '').trim();
  const subject = String(raw?.subject ?? '').trim();
  const date = String(raw?.date ?? raw?.internalDate ?? raw?.timestamp ?? '').trim();
  const snippet = String(raw?.snippet ?? raw?.bodyPreview ?? '').trim();
  const labels = Array.isArray(raw?.labels) ? raw.labels.map((x: any) => String(x)) : [];

  return {
    id,
    threadId: threadId || id,
    from,
    subject,
    date,
    snippet,
    labels,
  };
}

function isLikelyNoReply(from: string) {
  const f = from.toLowerCase();
  return (
    f.includes('no-reply') ||
    f.includes('noreply') ||
    f.includes('do-not-reply') ||
    f.includes('donotreply')
  );
}

function extractEmailAddress(from: string): string {
  const m = String(from).match(/<([^>]+)>/);
  if (m?.[1]) return m[1].trim();
  // fallback: find first email-ish token
  const m2 = String(from).match(/[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}/i);
  return (m2?.[0] ?? '').trim();
}

function ensureRe(subject: string) {
  const s = String(subject ?? '').trim();
  if (!s) return 'Re:';
  return /^re:\s*/i.test(s) ? s : `Re: ${s}`;
}

type TriageCategory = 'needs_reply' | 'needs_action' | 'fyi';

type TriageDecision = {
  id: string;
  category: TriageCategory;
  rationale?: string;
  reply?: {
    subject?: string;
    body: string;
  };
};

type EmailTriageReport = {
  summary: string;
  buckets: {
    needsReply: string[];
    needsAction: string[];
    fyi: string[];
  };
  emails: NormalizedEmail[];
  decisions?: TriageDecision[];
  drafts?: { to: string; subject: string; body: string; emailId: string }[];
  mode: 'deterministic' | 'llm';
};

function buildDeterministicReport(emails: NormalizedEmail[]): EmailTriageReport {
  const buckets = {
    needsReply: [] as NormalizedEmail[],
    needsAction: [] as NormalizedEmail[],
    fyi: [] as NormalizedEmail[],
  };

  for (const e of emails) {
    const subjLower = e.subject.toLowerCase();
    const unread = e.labels.some((l) => l.toUpperCase() === 'UNREAD');

    if (subjLower.includes('action required') || subjLower.includes('urgent')) {
      buckets.needsAction.push(e);
      continue;
    }

    if (unread && !isLikelyNoReply(e.from)) {
      buckets.needsReply.push(e);
      continue;
    }

    buckets.fyi.push(e);
  }

  const summary = `${buckets.needsReply.length} need replies, ${buckets.needsAction.length} need action, ${buckets.fyi.length} FYI`;

  return {
    summary,
    buckets: {
      needsReply: buckets.needsReply.map((x) => x.id),
      needsAction: buckets.needsAction.map((x) => x.id),
      fyi: buckets.fyi.map((x) => x.id),
    },
    emails,
    mode: 'deterministic',
  };
}

function triagePrompt(emails: NormalizedEmail[]) {
  return (
    `You are an email triage assistant.\n` +
    `Given the following emails, return JSON that categorizes each email and (when category is needs_reply) drafts a short reply.\n` +
    `Guidelines:\n` +
    `- Keep replies concise, friendly, and professional.\n` +
    `- If sender appears to be automated (no-reply), do not draft a reply; categorize as fyi unless it is clearly urgent/actionable.\n` +
    `- Use one of categories: needs_reply, needs_action, fyi.\n` +
    `- The reply body should be plain text, no markdown.\n\n` +
    `Emails (JSON):\n` +
    JSON.stringify(
      emails.map((e) => ({
        id: e.id,
        from: e.from,
        subject: e.subject,
        date: e.date,
        snippet: e.snippet,
        labels: e.labels,
      })),
      null,
      2,
    )
  );
}

const TRIAGE_OUTPUT_SCHEMA = {
  type: 'object',
  properties: {
    decisions: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          id: { type: 'string' },
          category: { type: 'string', enum: ['needs_reply', 'needs_action', 'fyi'] },
          rationale: { type: 'string' },
          reply: {
            type: 'object',
            properties: {
              subject: { type: 'string' },
              body: { type: 'string' },
            },
            required: ['body'],
            additionalProperties: false,
          },
        },
        required: ['id', 'category'],
        additionalProperties: false,
      },
    },
  },
  required: ['decisions'],
  additionalProperties: false,
};

export const emailTriageCommand = {
  name: 'email.triage',
  meta: {
    description: 'Email triage (deterministic by default, optionally LLM-assisted via llm.invoke)',
    argsSchema: {
      type: 'object',
      properties: {
        limit: { type: 'number', description: 'Maximum items to consume from input stream', default: 20 },
        llm: { type: 'boolean', description: 'Use llm.invoke for categorization + draft replies' },
        model: { type: 'string', description: 'Model for llm.invoke (optional; adapter defaults may apply)' },
        url: { type: 'string', description: 'Reserved for compatibility (ignored in OpenClaw mode)' },
        token: { type: 'string', description: 'Bearer token (or OPENCLAW_TOKEN/CLAWD_TOKEN)' },
        temperature: { type: 'number', description: 'LLM temperature' },
        'max-output-tokens': { type: 'number', description: 'Max completion tokens' },
        emit: { type: 'string', description: "Output mode: 'report' (default) or 'drafts'", default: 'report' },
        'state-key': { type: 'string', description: 'Run-state key forwarded to llm.invoke' },
        _: { type: 'array', items: { type: 'string' } },
      },
      required: [],
    },
    sideEffects: [],
  },
  help() {
    return (
      `email.triage — categorize emails and draft replies (optional LLM)\n\n` +
      `Usage (deterministic):\n` +
      `  gog.gmail.search --query 'newer_than:1d' --max 20 | email.triage\n\n` +
      `Usage (LLM-assisted drafts):\n` +
      `  gog.gmail.search --query 'newer_than:1d' --max 20 | email.triage --llm --model <model>\n\n` +
      `Send drafts (requires approval):\n` +
      `  ... | email.triage --llm --model <model> --emit drafts | approve --prompt 'Send replies?' | gog.gmail.send\n\n` +
      `Notes:\n` +
      `  - Read-only by default: does not send anything.\n` +
      `  - LLM mode uses llm.invoke (and its cache/resume semantics).\n`
    );
  },
  async run({ input, args, ctx }) {
    const limit = Number(args.limit ?? 20);
    const emit = String(args.emit ?? 'report').trim() || 'report';

    const emails: NormalizedEmail[] = [];
    for await (const item of input) {
      emails.push(normalizeEmail(item));
      if (emails.length >= limit) break;
    }

    const wantLlm = Boolean(args.llm ?? false);
    const env = ctx?.env ?? process.env;
    const hasLlmProvider = Boolean(
      String(env.LOBSTER_LLM_PROVIDER ?? '').trim() ||
      String(env.LOBSTER_PI_LLM_ADAPTER_URL ?? '').trim() ||
      String(env.LOBSTER_LLM_ADAPTER_URL ?? '').trim() ||
      String(env.OPENCLAW_URL ?? env.CLAWD_URL ?? '').trim(),
    );

    if (!wantLlm || !hasLlmProvider) {
      const report = buildDeterministicReport(emails);
      if (emit === 'drafts') {
        return { output: streamOf([]) };
      }
      return { output: streamOf([report]) };
    }

    const model = String(args.model ?? '').trim();

    if (!ctx?.registry) throw new Error('email.triage (LLM mode) requires ctx.registry');
    const llmCmd = ctx.registry.get('llm.invoke') ?? ctx.registry.get('llm_task.invoke');
    if (!llmCmd) throw new Error('email.triage requires llm.invoke to be registered');

    const llmRes = await llmCmd.run({
      input: streamOf(emails),
      args: {
        _: [],
        url: args.url,
        token: args.token,
        ...(model ? { model } : null),
        prompt: triagePrompt(emails),
        'output-schema': JSON.stringify(TRIAGE_OUTPUT_SCHEMA),
        'schema-version': 'email_triage.v1',
        temperature: args.temperature,
        'max-output-tokens': args['max-output-tokens'],
        'state-key': args['state-key'] ?? env.LOBSTER_RUN_STATE_KEY,
      },
      ctx,
    } as any);

    const llmItems: any[] = [];
    for await (const it of llmRes.output) llmItems.push(it);
    const first = llmItems[0];
    const data = first?.output?.data;
    const decisionsRaw = Array.isArray(data?.decisions) ? data.decisions : [];
    const decisions: TriageDecision[] = decisionsRaw.map((d: any) => ({
      id: String(d?.id ?? '').trim(),
      category: String(d?.category ?? 'fyi') as TriageCategory,
      rationale: d?.rationale ? String(d.rationale) : undefined,
      reply: d?.reply && typeof d.reply === 'object' ? { subject: d.reply.subject, body: String(d.reply.body ?? '') } : undefined,
    })).filter((d: any) => d.id);

    const byId = new Map(emails.map((e) => [e.id, e] as const));
    const buckets = {
      needsReply: [] as string[],
      needsAction: [] as string[],
      fyi: [] as string[],
    };

    const drafts: { to: string; subject: string; body: string; emailId: string }[] = [];

    for (const d of decisions) {
      if (d.category === 'needs_reply') buckets.needsReply.push(d.id);
      else if (d.category === 'needs_action') buckets.needsAction.push(d.id);
      else buckets.fyi.push(d.id);

      if (d.category === 'needs_reply' && d.reply?.body) {
        const email = byId.get(d.id);
        const to = email ? extractEmailAddress(email.from) : '';
        if (to && !isLikelyNoReply(email?.from ?? '')) {
          drafts.push({
            emailId: d.id,
            to,
            subject: d.reply.subject ? String(d.reply.subject) : ensureRe(email?.subject ?? ''),
            body: String(d.reply.body),
          });
        }
      }
    }

    const summary = `${buckets.needsReply.length} need replies, ${buckets.needsAction.length} need action, ${buckets.fyi.length} FYI`;

    if (emit === 'drafts') {
      return {
        output: (async function* () {
          for (const d of drafts) {
            // gog.gmail.send expects: {to, subject, body}
            yield { to: d.to, subject: d.subject, body: d.body, emailId: d.emailId };
          }
        })(),
      };
    }

    const report: EmailTriageReport = {
      summary,
      buckets,
      emails,
      decisions,
      drafts,
      mode: 'llm',
    };

    return { output: streamOf([report]) };
  },
};

async function* streamOf(items: any[]) {
  for (const item of items) yield item;
}
```

## File: `src/commands/stdlib/exec.ts`
```typescript
import { spawn } from 'node:child_process';
import { resolveInlineShellCommand } from '../../shell.js';

export const execCommand = {
  name: 'exec',
  meta: {
    description: 'Run an OS command',
    argsSchema: {
      type: 'object',
      properties: {
        json: { type: 'boolean', description: 'Parse stdout as JSON (single value).' },
        shell: { type: 'string', description: 'Run via the system shell with this command line.' },
        _: { type: 'array', items: { type: 'string' }, description: 'Command + args.' },
      },
      required: ['_'],
    },
    sideEffects: ['local_exec'],
  },
  help() {
    return `exec — run an OS command\n\n` +
      `Usage:\n` +
      `  exec <command...>\n` +
      `  exec --stdin raw|json|jsonl <command...>\n` +
      `  exec --json <command...>\n` +
      `  exec --shell "<command line>"\n\n` +
      `Notes:\n` +
      `  - With --json, parses stdout as JSON (single value).\n` +
      `  - With --stdin, writes pipeline input to stdin.\n` +
      `  - With --shell (or a single arg containing spaces), runs via the system shell.\n`;
  },
  async run({ input, args, ctx }) {
    const cmd = args._;
    const cwd = ctx?.cwd ?? process.cwd();

    const shellLine = typeof args.shell === 'string' ? args.shell : null;
    const useShell = Boolean(args.shell) || (cmd.length === 1 && /\s/.test(cmd[0]));
    const stdinMode = typeof args.stdin === 'string' ? String(args.stdin).toLowerCase() : null;

    if (!cmd.length && !shellLine) throw new Error('exec requires a command');

    let stdinPayload = null;
    if (stdinMode) {
      const items = [];
      for await (const item of input) items.push(item);
      stdinPayload = encodeStdin(items, stdinMode);
    } else {
      // Drain input to avoid dangling streams.
      for await (const _item of input) {
        // no-op
      }
    }

    const result = useShell
      ? await runShellLine(shellLine ?? cmd[0] ?? '', { env: ctx.env, cwd, stdin: stdinPayload, signal: ctx.signal })
      : await runProcess(cmd[0], cmd.slice(1), { env: ctx.env, cwd, stdin: stdinPayload, signal: ctx.signal });

    if (args.json) {
      let parsed;
      try {
        parsed = JSON.parse(result.stdout.trim() || 'null');
      } catch (err) {
        throw new Error(`exec --json could not parse stdout as JSON: ${err?.message ?? String(err)}`);
      }

      return {
        output: asStream(Array.isArray(parsed) ? parsed : [parsed]),
      };
    }

    const lines = result.stdout.split(/\r?\n/).filter(Boolean);
    return { output: asStream(lines) };
  },
};

function runProcess(command, argv, { env, cwd, stdin, signal }) {
  return new Promise<any>((resolve, reject) => {
    const child = spawn(command, argv, {
      env,
      cwd,
      signal,
      stdio: ['pipe', 'pipe', 'pipe'],
    });

    let stdout = '';
    let stderr = '';

    child.stdout.setEncoding('utf8');
    child.stderr.setEncoding('utf8');

    child.stdout.on('data', (d) => { stdout += d; });
    child.stderr.on('data', (d) => { stderr += d; });

    if (typeof stdin === 'string') {
      child.stdin.setDefaultEncoding('utf8');
      child.stdin.write(stdin);
    }
    child.stdin.end();

    child.on('error', reject);
    child.on('close', (code) => {
      if (code === 0) return resolve({ stdout, stderr });
      reject(new Error(`exec failed (${code}): ${stderr.trim() || stdout.trim() || command}`));
    });
  });
}

function runShellLine(commandLine, { env, cwd, stdin, signal }) {
  const shell = resolveInlineShellCommand({ command: commandLine, env });
  return runProcess(shell.command, shell.argv, { env, cwd, stdin, signal });
}

function encodeStdin(items, mode) {
  if (mode === 'json') return JSON.stringify(items);
  if (mode === 'jsonl') {
    return items.map((item) => JSON.stringify(item)).join('\n') + (items.length ? '\n' : '');
  }
  if (mode === 'raw') {
    return items.map((item) => (typeof item === 'string' ? item : JSON.stringify(item))).join('\n');
  }
  throw new Error(`exec --stdin must be raw, json, or jsonl (got ${mode})`);
}

async function* asStream(items) {
  for (const item of items) yield item;
}
```

## File: `src/commands/stdlib/gog_gmail_search.ts`
```typescript
import { spawn } from "node:child_process";

function run(cmd: string, argv: string[], env: Record<string, string | undefined>, cwd?: string) {
  return new Promise<{ stdout: string; stderr: string; code: number | null }>((resolve, reject) => {
    const child = spawn(cmd, argv, {
      env: { ...process.env, ...env },
      cwd,
      stdio: ["ignore", "pipe", "pipe"],
    });

    let stdout = "";
    let stderr = "";
    child.stdout?.on("data", (d) => (stdout += String(d)));
    child.stderr?.on("data", (d) => (stderr += String(d)));

    child.on("error", (err: any) => {
      if (err?.code === "ENOENT") {
        reject(new Error("gog not found on PATH (install: https://github.com/steipete/gogcli)"));
        return;
      }
      reject(err);
    });

    child.on("close", (code) => {
      resolve({ stdout, stderr, code });
    });
  });
}

export const gogGmailSearchCommand = {
  name: "gog.gmail.search",
  meta: {
    description: "Fetch Gmail threads via gog (JSON)",
    argsSchema: {
      type: "object",
      properties: {
        query: { type: "string", description: "Gmail search query", default: "newer_than:1d" },
        max: { type: "number", description: "Max results", default: 20 },
        limit: { type: "number", description: "Alias for max" },
        _: { type: "array", items: { type: "string" } },
      },
      required: [],
    },
    sideEffects: ['reads_email'],
  },
  help() {
    return (
      `gog.gmail.search — fetch Gmail messages via gog (JSON)\n\n` +
      `Usage:\n` +
      `  gog.gmail.search --query 'newer_than:1d' --max 20\n\n` +
      `Notes:\n` +
      `  - Requires the gog CLI: https://github.com/steipete/gogcli\n` +
      `  - Set GOG_BIN to override the executable used (default: gog).\n` +
      `  - This command outputs an array of message objects (as a stream).\n`
    );
  },
  async run({ input, args, ctx }) {
    // Drain input
    for await (const _item of input) {
      // no-op
    }

    const query = String(args.query ?? "newer_than:1d");
    const max = Number(args.max ?? args.limit ?? 20);

    const gogBinRaw = String(ctx.env.GOG_BIN ?? "gog");

    // gog CLI (v0.9.x) expects the query as a positional argument:
    //   gog gmail search <query> ... --json
    // Earlier draft versions used --query; keep Lobster's --query flag but translate it.
    const argvBase = ["gmail", "search", query, "--json", "--max", String(max)];

    // Test-friendly: allow pointing GOG_BIN at a node script.
    const isScript = /\.(mjs|cjs|js|ts)$/i.test(gogBinRaw);
    const gogBin = isScript ? process.execPath : gogBinRaw;
    const argv = isScript ? [gogBinRaw, ...argvBase] : argvBase;

    const res = await run(gogBin, argv, ctx.env, process.cwd());
    if (res.code !== 0) {
      throw new Error(`gog.gmail.search failed (${res.code ?? "?"}): ${res.stderr.slice(0, 400)}`);
    }

    let parsed: any;
    try {
      parsed = JSON.parse(res.stdout);
    } catch (_err) {
      throw new Error("gog.gmail.search expected JSON output");
    }

    // gog gmail search --json returns either:
    // - an array of message/thread objects (older versions / some commands), or
    // - an object like { nextPageToken, threads: [...] } (gog v0.9.x).
    const items = Array.isArray(parsed)
      ? // Some gog versions return: [ { nextPageToken, threads: [...] } ]
        (parsed as any[]).flatMap((x) => (Array.isArray(x?.threads) ? x.threads : [x]))
      : Array.isArray((parsed as any)?.threads)
        ? (parsed as any).threads
        : [parsed];

    return {
      output: (async function* () {
        for (const item of items) yield item;
      })(),
    };
  },
};
```

## File: `src/commands/stdlib/gog_gmail_send.ts`
```typescript
import { spawn } from "node:child_process";

function run(cmd: string, argv: string[], env: Record<string, string | undefined>, cwd?: string) {
  return new Promise<{ stdout: string; stderr: string; code: number | null }>((resolve, reject) => {
    const child = spawn(cmd, argv, {
      env: { ...process.env, ...env },
      cwd,
      stdio: ["ignore", "pipe", "pipe"],
    });

    let stdout = "";
    let stderr = "";
    child.stdout?.on("data", (d) => (stdout += String(d)));
    child.stderr?.on("data", (d) => (stderr += String(d)));

    child.on("error", (err: any) => {
      if (err?.code === "ENOENT") {
        reject(new Error("gog not found on PATH (install: https://github.com/steipete/gogcli)"));
        return;
      }
      reject(err);
    });

    child.on("close", (code) => {
      resolve({ stdout, stderr, code });
    });
  });
}

type Draft = {
  to: string;
  subject: string;
  body: string;
};

function parseDraft(item: any): Draft {
  if (!item || typeof item !== "object") {
    throw new Error("gog.gmail.send expects draft objects");
  }
  const to = String((item as any).to ?? "").trim();
  const subject = String((item as any).subject ?? "").trim();
  const body = String((item as any).body ?? "").trim();
  if (!to) throw new Error("gog.gmail.send draft missing to");
  return { to, subject, body };
}

export const gogGmailSendCommand = {
  name: "gog.gmail.send",
  meta: {
    description: "Send Gmail messages via gog",
    argsSchema: {
      type: "object",
      properties: {
        dryRun: { type: "boolean", description: "If true, do not send; echo drafts" },
        "dry-run": { type: "boolean", description: "Alias for dryRun" },
        _: { type: "array", items: { type: "string" } },
      },
      required: [],
    },
    sideEffects: ['sends_email'],
  },
  help() {
    return (
      `gog.gmail.send — send Gmail messages via gog\n\n` +
      `Usage:\n` +
      `  ... | approve --prompt 'Send replies?' | gog.gmail.send\n\n` +
      `Input:\n` +
      `  Stream of draft objects: { to, subject, body }\n\n` +
      `Notes:\n` +
      `  - Requires the gog CLI: https://github.com/steipete/gogcli\n` +
      `  - Set GOG_BIN to override the executable used (default: gog).\n`
    );
  },
  async run({ input, args, ctx }) {
    const dryRun = Boolean(args.dryRun ?? args["dry-run"] ?? false);
    const gogBinRaw = String(ctx.env.GOG_BIN ?? "gog");
    const isScript = /\.(mjs|cjs|js|ts)$/i.test(gogBinRaw);
    const gogBin = isScript ? process.execPath : gogBinRaw;

    const results: any[] = [];

    for await (const item of input) {
      const draft = parseDraft(item);

      if (dryRun) {
        results.push({ ok: true, dryRun: true, ...draft });
        continue;
      }

      const argvBase = [
        "gmail",
        "send",
        "--to",
        draft.to,
        ...(draft.subject ? ["--subject", draft.subject] : []),
        ...(draft.body ? ["--body", draft.body] : []),
        "--json",
      ];

      const argv = isScript ? [gogBinRaw, ...argvBase] : argvBase;
      const res = await run(gogBin, argv, ctx.env, process.cwd());
      if (res.code !== 0) {
        throw new Error(`gog.gmail.send failed (${res.code ?? "?"}): ${res.stderr.slice(0, 400)}`);
      }

      let parsed: any;
      try {
        parsed = res.stdout ? JSON.parse(res.stdout) : { ok: true };
      } catch (_err) {
        parsed = { ok: true, raw: res.stdout };
      }

      results.push(parsed);
    }

    return {
      output: (async function* () {
        for (const r of results) yield r;
      })(),
    };
  },
};
```

## File: `src/commands/stdlib/group_by.ts`
```typescript
function getByPath(obj: any, path: string): any {
  const parts = path.split('.').filter(Boolean);
  let cur: any = obj;
  for (const p of parts) {
    if (cur == null) return undefined;
    cur = cur[p];
  }
  return cur;
}

export const groupByCommand = {
  name: 'groupBy',
  meta: {
    description: 'Group items by a key (stable group order)',
    argsSchema: {
      type: 'object',
      properties: {
        key: { type: 'string', description: 'Dot-path key to group by (required)' },
        _: { type: 'array', items: { type: 'string' } },
      },
      required: ['key'],
    },
    sideEffects: [],
  },
  help() {
    return (
      `groupBy — group items by a key\n\n` +
      `Usage:\n` +
      `  ... | groupBy --key from\n\n` +
      `Output:\n` +
      `  Stream of { key, items, count } objects\n\n` +
      `Notes:\n` +
      `  - Group order is stable (order of first appearance).\n`
    );
  },
  async run({ input, args }: any) {
    const keyPath = String(args.key ?? '').trim();
    if (!keyPath) throw new Error('groupBy requires --key');

    const groups = new Map<string, { key: any; items: any[] }>();
    const order: string[] = [];

    for await (const item of input) {
      const keyVal = getByPath(item, keyPath);
      const k = JSON.stringify(keyVal);
      if (!groups.has(k)) {
        groups.set(k, { key: keyVal, items: [] });
        order.push(k);
      }
      groups.get(k)!.items.push(item);
    }

    return {
      output: (async function* () {
        for (const k of order) {
          const g = groups.get(k)!;
          yield { key: g.key, items: g.items, count: g.items.length };
        }
      })(),
    };
  },
};
```

## File: `src/commands/stdlib/head.ts`
```typescript
export const headCommand = {
  name: 'head',
  meta: {
    description: 'Take first N items',
    argsSchema: {
      type: 'object',
      properties: {
        n: { type: 'number', description: 'Number of items to take', default: 10 },
        _: { type: 'array', items: { type: 'string' } },
      },
      required: [],
    },
    sideEffects: [],
  },
  help() {
    return `head — take first N items\n\nUsage:\n  head --n 10\n`;
  },
  async run({ input, args }) {
    const n = args.n === undefined ? 10 : Number(args.n);
    if (!Number.isFinite(n) || n < 0) throw new Error('head --n must be a non-negative number');

    return {
      output: (async function* () {
        let i = 0;
        for await (const item of input) {
          if (i++ >= n) break;
          yield item;
        }
      })(),
    };
  },
};
```

## File: `src/commands/stdlib/json.ts`
```typescript
export const jsonCommand = {
  name: 'json',
  meta: {
    description: 'Render pipeline output as JSON',
    argsSchema: { type: 'object', properties: {}, required: [] },
    sideEffects: [],
  },
  help() {
    return `json — render pipeline output as JSON\n\nUsage:\n  ... | json\n`;
  },
  async run({ input, ctx }) {
    const items = [];
    for await (const item of input) items.push(item);
    ctx.render.json(items);
    return { output: emptyStream(), rendered: true };
  },
};

async function* emptyStream() {}
```

## File: `src/commands/stdlib/llm_invoke.ts`
```typescript
import path from 'node:path';
import { promises as fsp } from 'node:fs';
import { createHash } from 'node:crypto';
import { Ajv } from 'ajv';
import type { ErrorObject } from 'ajv';

import { readStateJson, writeStateJson, stableStringify } from '../../state/store.js';
import type { LobsterCommand } from '../types.js';

const ajv = new Ajv({ allErrors: true, strict: false });

const artifactSchema = {
  type: 'object',
  properties: {
    kind: { type: 'string' },
    role: { type: 'string' },
    name: { type: 'string' },
    mimeType: { type: 'string' },
    text: { type: 'string' },
    data: {},
    uri: { type: 'string' },
  },
  additionalProperties: true,
};

const payloadSchema = {
  type: 'object',
  properties: {
    prompt: { type: 'string', minLength: 1 },
    model: { type: 'string', minLength: 1 },
    artifacts: { type: 'array', items: artifactSchema },
    artifactHashes: { type: 'array', items: { type: 'string', minLength: 10 } },
    schemaVersion: { type: 'string' },
    metadata: { type: 'object', additionalProperties: true },
    outputSchema: { type: 'object', additionalProperties: true },
    temperature: { type: 'number' },
    maxOutputTokens: { type: 'number' },
    retryContext: {
      type: 'object',
      properties: {
        attempt: { type: 'number' },
        validationErrors: { type: 'array', items: { type: 'string' } },
      },
      additionalProperties: false,
    },
  },
  required: ['prompt', 'artifacts', 'artifactHashes'],
  additionalProperties: false,
};

const responseSchema = {
  type: 'object',
  properties: {
    ok: { type: 'boolean' },
    result: {
      type: 'object',
      properties: {
        runId: { type: 'string' },
        model: { type: 'string' },
        prompt: { type: 'string' },
        status: { type: 'string' },
        output: {
          type: 'object',
          properties: {
            text: { type: 'string' },
            data: {},
            format: { type: 'string' },
          },
          required: [],
          additionalProperties: true,
        },
        usage: {
          type: 'object',
          properties: {
            inputTokens: { type: 'number' },
            outputTokens: { type: 'number' },
            totalTokens: { type: 'number' },
          },
          additionalProperties: true,
        },
        warnings: { type: 'array', items: { type: 'string' } },
        metadata: { type: 'object', additionalProperties: true },
        diagnostics: { type: 'object', additionalProperties: true },
      },
      required: ['output'],
      additionalProperties: true,
    },
    error: { type: 'object', additionalProperties: true },
  },
  required: ['ok'],
  additionalProperties: true,
};

const validatePayload = ajv.compile(payloadSchema);
const validateResponseEnvelope = ajv.compile(responseSchema);

const DEFAULT_MAX_VALIDATION_RETRIES = 1;
const STATE_VERSION = 1;

type BuiltInProvider = 'openclaw' | 'pi' | 'http';
type SupportedProvider = BuiltInProvider | string;

type LlmResponseEnvelope = {
  ok: boolean;
  result?: LlmResponse | null;
  error?: { message?: string } | null;
};

type LlmResponse = {
  runId?: string | null;
  model?: string | null;
  prompt?: string | null;
  status?: string | null;
  output?: {
    text?: string | null;
    data?: any;
    format?: string | null;
  } | null;
  usage?: Record<string, unknown> | null;
  warnings?: string[] | null;
  metadata?: Record<string, unknown> | null;
  diagnostics?: Record<string, unknown> | null;
};

type NormalizedInvocationItem = {
  kind: string;
  runId: string | null;
  prompt: string | null;
  model: string | null;
  schemaVersion: string | null;
  status: string;
  cacheKey: string;
  artifactHashes: string[];
  output: { format: string | null; text: string | null; data: any };
  usage: Record<string, unknown> | null;
  metadata: Record<string, unknown> | null;
  warnings: string[] | null;
  diagnostics: Record<string, unknown> | null;
  createdAt: string;
  source: string;
  cached: boolean;
  attemptCount: number;
};

type CacheEntry = {
  items: NormalizedInvocationItem[];
  cacheKey: string;
  storedAt: string;
};

type CommandConfig = {
  name: string;
  itemKind: string;
  stateType: string;
  cacheNamespace: string;
  defaultProvider?: SupportedProvider | null;
  description: string;
  helpTitle: string;
  helpConfig: string[];
  helpExamples: string[];
  sourceForProvider?: (provider: SupportedProvider) => string;
  legacyEnvCompat?: boolean;
};

type Adapter = {
  provider: SupportedProvider;
  source: string;
  invoke: (params: { env: any; args: any; payload: Record<string, any> }) => Promise<LlmResponseEnvelope>;
};

type DirectAdapter =
  | ((params: { env: any; args: any; payload: Record<string, any>; ctx: any }) => Promise<LlmResponseEnvelope>)
  | {
    source?: string;
    invoke: (params: { env: any; args: any; payload: Record<string, any>; ctx: any }) => Promise<LlmResponseEnvelope>;
  };

export const llmInvokeCommand = createLlmInvokeCommand({
  name: 'llm.invoke',
  itemKind: 'llm.invoke',
  stateType: 'llm.invoke',
  cacheNamespace: 'llm.invoke',
  defaultProvider: null,
  description: 'Call a configured LLM adapter with typed payloads and caching',
  helpTitle: 'llm.invoke — call a configured LLM adapter with caching and schema validation',
  helpConfig: [
    'Provider resolution order: --provider, LOBSTER_LLM_PROVIDER, then environment auto-detect.',
    'Built-in providers: openclaw, pi, http.',
    'OpenClaw provider uses OPENCLAW_URL (CLAWD_URL also supported) and OPENCLAW_TOKEN.',
    'Pi provider uses LOBSTER_PI_LLM_ADAPTER_URL and is intended to be supplied by a Pi extension.',
    'Generic http provider uses LOBSTER_LLM_ADAPTER_URL and optional LOBSTER_LLM_ADAPTER_TOKEN.',
  ],
  helpExamples: [
    "llm.invoke --prompt 'Write summary'",
    "llm.invoke --provider openclaw --model claude-3-sonnet --prompt 'Write summary'",
    "cat artifacts.json | llm.invoke --provider pi --prompt 'Score each item'",
    "... | llm.invoke --prompt 'Plan next steps' --output-schema '{\"type\":\"object\"}'",
  ],
  sourceForProvider(provider) {
    return provider;
  },
  legacyEnvCompat: true,
});

export const llmTaskInvokeCommand = createLlmInvokeCommand({
  name: 'llm_task.invoke',
  itemKind: 'llm_task.invoke',
  stateType: 'llm_task.invoke',
  cacheNamespace: 'llm_task.invoke',
  defaultProvider: 'openclaw',
  description: 'Backward-compatible alias for llm.invoke using the OpenClaw adapter',
  helpTitle: 'llm_task.invoke — backward-compatible alias for llm.invoke using OpenClaw',
  helpConfig: [
    'Requires OPENCLAW_URL (or CLAWD_URL) and optionally OPENCLAW_TOKEN.',
    'Use llm.invoke for new workflows and non-OpenClaw adapters.',
  ],
  helpExamples: [
    "llm_task.invoke --prompt 'Write summary'",
    "llm_task.invoke --model claude-3-sonnet --prompt 'Write summary'",
    "cat artifacts.json | llm_task.invoke --prompt 'Score each item'",
  ],
  sourceForProvider() {
    return 'clawd';
  },
  legacyEnvCompat: true,
});

export function createLlmInvokeCommand(config: CommandConfig): LobsterCommand {
  return {
    name: config.name,
    meta: {
      description: config.description,
      argsSchema: {
        type: 'object',
        properties: {
          provider: {
            type: 'string',
            description: 'LLM adapter provider (openclaw, pi, http). Optional if auto-detected.',
          },
          token: {
            type: 'string',
            description: 'Optional bearer token for providers that support it.',
          },
          prompt: { type: 'string', description: 'Primary prompt / instructions' },
          model: {
            type: 'string',
            description: 'Model identifier. Optional; adapter defaults may apply if omitted.',
          },
          'artifacts-json': { type: 'string', description: 'JSON array of artifacts to send' },
          'metadata-json': { type: 'string', description: 'JSON object of metadata to include' },
          'output-schema': { type: 'string', description: 'JSON schema LLM output must satisfy' },
          'schema-version': { type: 'string', description: 'Logical schema version for caching' },
          'max-validation-retries': { type: 'number', description: 'Retries when schema validation fails' },
          temperature: { type: 'number', description: 'Sampling temperature' },
          'max-output-tokens': { type: 'number', description: 'Max completion tokens' },
          'state-key': { type: 'string', description: 'Run-state key override (else LOBSTER_RUN_STATE_KEY)' },
          refresh: { type: 'boolean', description: 'Bypass run-state + cache' },
          'disable-cache': { type: 'boolean', description: 'Skip persistent cache' },
          _: { type: 'array', items: { type: 'string' } },
        },
        required: [],
      },
      sideEffects: ['calls_llm'],
    },
    help() {
      const lines = [
        config.helpTitle,
        '',
        'Usage:',
        ...config.helpExamples.map((example) => `  ${example}`),
        '',
        'Features:',
        '  - Typed payload validation before invoking the adapter.',
        '  - Run-state + file cache so resumes do not re-call the LLM.',
        '  - Optional JSON-schema enforcement with bounded retries.',
        '',
        'Config:',
        ...config.helpConfig.map((line) => `  - ${line}`),
      ];
      return `${lines.join('\n')}\n`;
    },
    async run({ input, args, ctx }) {
      return runLlmInvoke({ input, args, ctx, config });
    },
  } satisfies LobsterCommand;
}

async function runLlmInvoke({ input, args, ctx, config }: { input: AsyncIterable<any>; args: any; ctx: any; config: CommandConfig }) {
  const env = ctx.env ?? process.env;
  const provider = resolveProvider(args, env, config.defaultProvider, ctx);
  const adapter = resolveAdapter({ provider, env, args, config, ctx });
  const prompt = extractPrompt(args);
  if (!prompt) throw new Error(`${config.name} requires --prompt or positional text`);

  const model = resolveModel(args, env, config.legacyEnvCompat);
  const schemaVersion = resolveEnvString(
    args['schema-version'],
    ['LOBSTER_LLM_SCHEMA_VERSION', ...(config.legacyEnvCompat ? ['LLM_TASK_SCHEMA_VERSION'] : [])],
    env,
    'v1',
  );
  const maxOutputTokens = parseOptionalNumber(args['max-output-tokens']);
  const temperature = parseOptionalNumber(args.temperature);
  const providedArtifacts = parseJsonArray(args['artifacts-json'], `${config.name} --artifacts-json`);
  const metadataObject = parseJsonObject(args['metadata-json'], `${config.name} --metadata-json`);
  const userOutputSchema = parseJsonObject(args['output-schema'], `${config.name} --output-schema`);
  const maxValidationRetriesRaw =
    args['max-validation-retries'] ??
    getFirstEnv(env, ['LOBSTER_LLM_VALIDATION_RETRIES', ...(config.legacyEnvCompat ? ['LLM_TASK_VALIDATION_RETRIES'] : [])]);
  const maxValidationRetries = userOutputSchema
    ? Math.max(
        0,
        Number.isFinite(Number(maxValidationRetriesRaw)) ? Number(maxValidationRetriesRaw) : DEFAULT_MAX_VALIDATION_RETRIES,
      )
    : 0;
  const disableCache = flag(args['disable-cache']);
  const forceRefresh = flag(
    args.refresh ??
      getFirstEnv(env, ['LOBSTER_LLM_FORCE_REFRESH', ...(config.legacyEnvCompat ? ['LLM_TASK_FORCE_REFRESH'] : [])]),
  );
  const stateKey = String(args['state-key'] ?? env.LOBSTER_RUN_STATE_KEY ?? '').trim() || null;

  const inputArtifacts: any[] = [];
  for await (const item of input) inputArtifacts.push(item);

  const normalizedArtifacts = [...inputArtifacts, ...providedArtifacts].map(normalizeArtifact);
  const artifactHashes = normalizedArtifacts.map(hashArtifact);
  const cacheKey = computeCacheKey({
    provider,
    prompt,
    model,
    schemaVersion,
    artifactHashes,
    outputSchema: userOutputSchema,
  });

  if (stateKey && !forceRefresh) {
    const stored = await readStateJson({ env, key: stateKey }).catch(() => null);
    const reused = pickReusableState(stored, cacheKey, config.stateType);
    if (reused) {
      return {
        output: streamOf(reused.items.map((item) => ({ ...item, source: 'run_state', cached: true }))),
      };
    }
  }

  if (!disableCache && !forceRefresh) {
    const cache = await readCacheEntry(env, cacheKey, config.cacheNamespace);
    if (cache) {
      return {
        output: streamOf(cache.items.map((item) => ({ ...item, source: 'cache', cached: true }))),
      };
    }
  }

  const payload: Record<string, any> = {
    prompt,
    ...(model ? { model } : null),
    artifacts: normalizedArtifacts,
    artifactHashes,
  };
  if (metadataObject) payload.metadata = metadataObject;
  if (userOutputSchema) payload.outputSchema = userOutputSchema;
  if (schemaVersion) payload.schemaVersion = schemaVersion;
  if (Number.isFinite(maxOutputTokens ?? NaN)) payload.maxOutputTokens = Number(maxOutputTokens);
  if (Number.isFinite(temperature ?? NaN)) payload.temperature = Number(temperature);

  if (!validatePayload(payload)) {
    throw new Error(`${config.name} payload invalid: ${ajv.errorsText(validatePayload.errors)}`);
  }

  const validator = userOutputSchema ? ajv.compile(userOutputSchema) : null;
  let attempt = 0;
  let lastValidationErrors: string[] = [];

  while (true) {
    attempt += 1;
    if (attempt > 1) {
      payload.retryContext = {
        attempt,
        ...(lastValidationErrors.length ? { validationErrors: lastValidationErrors } : null),
      };
    } else {
      delete payload.retryContext;
    }

    let responseEnvelope: LlmResponseEnvelope;
    try {
      responseEnvelope = await adapter.invoke({ env, args, payload });
    } catch (err: any) {
      throw new Error(`${config.name} request failed: ${err?.message ?? String(err)}`);
    }

    if (!validateResponseEnvelope(responseEnvelope)) {
      throw new Error(`${config.name} received invalid response envelope`);
    }

    if (responseEnvelope.ok !== true) {
      const message = responseEnvelope.error?.message ?? 'llm adapter returned an error';
      throw new Error(`${config.name} remote error: ${message}`);
    }

    const normalized = normalizeResult({
      envelope: responseEnvelope,
      cacheKey,
      schemaVersion,
      artifactHashes,
      source: adapter.source,
      attempt,
      itemKind: config.itemKind,
    });

    if (!validator) {
      await persistOutputs({ env, stateKey, cacheKey, items: normalized, stateType: config.stateType });
      if (!disableCache) await writeCacheEntry(env, cacheKey, normalized, config.cacheNamespace);
      return { output: streamOf(normalized) };
    }

    const structured = normalized[0]?.output?.data ?? null;
    if (validator(structured)) {
      await persistOutputs({ env, stateKey, cacheKey, items: normalized, stateType: config.stateType });
      if (!disableCache) await writeCacheEntry(env, cacheKey, normalized, config.cacheNamespace);
      return { output: streamOf(normalized) };
    }

    lastValidationErrors = collectAjvErrors(validator.errors);
    if (attempt > maxValidationRetries + 1) {
      throw new Error(`${config.name} output failed schema validation: ${lastValidationErrors.join('; ')}`);
    }
  }
}

function resolveProvider(args: any, env: any, defaultProvider?: SupportedProvider | null, ctx?: any): SupportedProvider {
  const explicit = String(args.provider ?? env.LOBSTER_LLM_PROVIDER ?? '').trim().toLowerCase();
  if (explicit) {
    if (explicit === 'openclaw' || explicit === 'pi' || explicit === 'http') {
      return explicit;
    }
    if (getDirectAdapter(ctx, explicit)) {
      return explicit;
    }
    throw new Error(`Unsupported llm provider: ${explicit}`);
  }
  if (defaultProvider) return defaultProvider;
  const directAdapters = ctx?.llmAdapters && typeof ctx.llmAdapters === 'object'
    ? Object.keys(ctx.llmAdapters).filter((key) => getDirectAdapter(ctx, key))
    : [];
  if (directAdapters.length === 1) return directAdapters[0];
  if (String(env.LOBSTER_PI_LLM_ADAPTER_URL ?? '').trim()) return 'pi';
  if (String(env.OPENCLAW_URL ?? env.CLAWD_URL ?? '').trim()) return 'openclaw';
  if (String(env.LOBSTER_LLM_ADAPTER_URL ?? '').trim()) return 'http';
  throw new Error('llm.invoke could not resolve a provider. Set --provider or LOBSTER_LLM_PROVIDER');
}

function resolveAdapter({
  provider,
  env,
  args,
  config,
  ctx,
}: {
  provider: SupportedProvider;
  env: any;
  args: any;
  config: CommandConfig;
  ctx: any;
}): Adapter {
  const direct = getDirectAdapter(ctx, provider);
  if (direct) {
    const invoke = typeof direct === 'function' ? direct : direct.invoke;
    return {
      provider,
      source: typeof direct === 'function' ? provider : direct.source ?? provider,
      async invoke({ payload }) {
        return invoke({ env, args, payload, ctx });
      },
    };
  }

  if (provider === 'openclaw') {
    const openclawUrl = String(env.OPENCLAW_URL ?? env.CLAWD_URL ?? '').trim();
    if (!openclawUrl) {
      throw new Error(`${config.name} requires OPENCLAW_URL (or CLAWD_URL) for provider=openclaw`);
    }
    const endpoint = new URL('/tools/invoke', openclawUrl);
    const token = String(args.token ?? env.OPENCLAW_TOKEN ?? env.CLAWD_TOKEN ?? '').trim();
    return {
      provider,
      source: config.sourceForProvider?.(provider) ?? 'openclaw',
      async invoke({ payload }) {
        return invokeOpenClawAdapter({ endpoint, token, payload });
      },
    };
  }

  if (provider === 'pi') {
    const adapterUrl = String(env.LOBSTER_PI_LLM_ADAPTER_URL ?? '').trim();
    if (!adapterUrl) {
      throw new Error(`${config.name} requires LOBSTER_PI_LLM_ADAPTER_URL for provider=pi`);
    }
    const token = String(args.token ?? env.LOBSTER_PI_LLM_ADAPTER_TOKEN ?? '').trim();
    return {
      provider,
      source: config.sourceForProvider?.(provider) ?? 'pi',
      async invoke({ payload }) {
        return invokeHttpAdapter({ endpoint: buildAdapterEndpoint(adapterUrl), token, payload });
      },
    };
  }

  const adapterUrl = String(env.LOBSTER_LLM_ADAPTER_URL ?? '').trim();
  if (!adapterUrl) {
    throw new Error(`${config.name} requires LOBSTER_LLM_ADAPTER_URL for provider=http`);
  }
  const token = String(args.token ?? env.LOBSTER_LLM_ADAPTER_TOKEN ?? '').trim();
  return {
    provider,
    source: config.sourceForProvider?.(provider) ?? 'http',
    async invoke({ payload }) {
      return invokeHttpAdapter({ endpoint: buildAdapterEndpoint(adapterUrl), token, payload });
    },
  };
}

function getDirectAdapter(ctx: any, provider: string): DirectAdapter | null {
  const adapters = ctx?.llmAdapters;
  if (!adapters || typeof adapters !== 'object') return null;
  const adapter = adapters[provider];
  if (typeof adapter === 'function') return adapter as DirectAdapter;
  if (adapter && typeof adapter === 'object' && typeof adapter.invoke === 'function') {
    return adapter as DirectAdapter;
  }
  return null;
}

function buildAdapterEndpoint(rawUrl: string) {
  const endpoint = new URL(rawUrl);
  if (endpoint.pathname === '/' || endpoint.pathname === '') {
    endpoint.pathname = '/invoke';
  }
  return endpoint;
}

async function invokeOpenClawAdapter({ endpoint, token, payload }: { endpoint: URL; token: string; payload: any }) {
  const res = await fetch(endpoint, {
    method: 'POST',
    headers: {
      'content-type': 'application/json',
      ...(token ? { authorization: `Bearer ${token}` } : null),
    },
    body: JSON.stringify({
      tool: 'llm-task',
      action: 'invoke',
      args: payload,
    }),
  });

  const text = await res.text();
  if (!res.ok) {
    throw new Error(`${res.status} ${res.statusText}: ${text.slice(0, 400)}`);
  }

  let parsed: any;
  try {
    parsed = text ? JSON.parse(text) : null;
  } catch {
    throw new Error('Response was not JSON');
  }

  if (parsed && typeof parsed === 'object' && !Array.isArray(parsed) && 'ok' in parsed) {
    if (parsed.ok !== true) {
      const msg = parsed?.error?.message ?? 'Unknown error';
      throw new Error(`openclaw adapter error: ${msg}`);
    }
    const inner = parsed.result;
    if (inner && typeof inner === 'object' && !Array.isArray(inner) && 'ok' in inner) {
      return inner as LlmResponseEnvelope;
    }
    return { ok: true, result: inner } as LlmResponseEnvelope;
  }

  return { ok: true, result: parsed } as LlmResponseEnvelope;
}

async function invokeHttpAdapter({ endpoint, token, payload }: { endpoint: URL; token: string; payload: any }) {
  const res = await fetch(endpoint, {
    method: 'POST',
    headers: {
      'content-type': 'application/json',
      ...(token ? { authorization: `Bearer ${token}` } : null),
    },
    body: JSON.stringify(payload),
  });

  const text = await res.text();
  if (!res.ok) {
    throw new Error(`${res.status} ${res.statusText}: ${text.slice(0, 400)}`);
  }

  let parsed: any;
  try {
    parsed = text ? JSON.parse(text) : null;
  } catch {
    throw new Error('Response was not JSON');
  }

  if (parsed && typeof parsed === 'object' && !Array.isArray(parsed) && 'ok' in parsed) {
    return parsed as LlmResponseEnvelope;
  }
  return { ok: true, result: parsed } as LlmResponseEnvelope;
}

function resolveModel(args: any, env: any, legacyEnvCompat: boolean | undefined) {
  return resolveEnvString(
    args.model,
    ['LOBSTER_LLM_MODEL', ...(legacyEnvCompat ? ['LLM_TASK_MODEL'] : [])],
    env,
    '',
  );
}

function resolveEnvString(raw: any, envKeys: string[], env: any, fallback: string) {
  if (raw !== undefined && raw !== null && String(raw).trim()) return String(raw).trim();
  const fromEnv = getFirstEnv(env, envKeys);
  if (fromEnv && String(fromEnv).trim()) return String(fromEnv).trim();
  return fallback;
}

function getFirstEnv(env: any, keys: string[]) {
  for (const key of keys) {
    if (env?.[key] !== undefined && env?.[key] !== null && String(env[key]).trim()) {
      return env[key];
    }
  }
  return undefined;
}

function extractPrompt(args: any) {
  if (args.prompt) return String(args.prompt);
  if (Array.isArray(args._) && args._.length) {
    return args._.join(' ');
  }
  return '';
}

function parseJsonArray(raw: any, label: string) {
  if (!raw) return [];
  try {
    const parsed = JSON.parse(String(raw));
    if (!Array.isArray(parsed)) throw new Error('must be array');
    return parsed;
  } catch {
    throw new Error(`${label} must be a JSON array`);
  }
}

function parseJsonObject(raw: any, label: string) {
  if (!raw) return null;
  try {
    const parsed = JSON.parse(String(raw));
    if (!parsed || typeof parsed !== 'object' || Array.isArray(parsed)) {
      throw new Error('must be an object');
    }
    return parsed;
  } catch {
    throw new Error(`${label} must be a JSON object`);
  }
}

function parseOptionalNumber(value: any) {
  if (value === undefined || value === null) return null;
  const num = Number(value);
  return Number.isFinite(num) ? num : null;
}

function flag(value: any) {
  if (value === undefined || value === null) return false;
  if (typeof value === 'boolean') return value;
  if (typeof value === 'string') {
    const normalized = value.trim().toLowerCase();
    if (['false', '0', 'no'].includes(normalized)) return false;
    if (['true', '1', 'yes'].includes(normalized)) return true;
  }
  return Boolean(value);
}

function normalizeArtifact(raw: any) {
  if (raw && typeof raw === 'object' && !Array.isArray(raw)) {
    return raw;
  }
  if (typeof raw === 'string') {
    return { kind: 'text', text: raw };
  }
  if (typeof raw === 'number' || typeof raw === 'boolean') {
    return { kind: 'text', text: String(raw) };
  }
  return { kind: 'json', data: raw };
}

function hashArtifact(artifact: any) {
  const stable = stableStringify(artifact);
  return createHash('sha256').update(stable).digest('hex');
}

function computeCacheKey({
  provider,
  prompt,
  model,
  schemaVersion,
  artifactHashes,
  outputSchema,
}: {
  provider: SupportedProvider;
  prompt: string;
  model: string;
  schemaVersion: string;
  artifactHashes: string[];
  outputSchema: any;
}) {
  const payload = {
    provider,
    prompt,
    model: model || `${provider}-default`,
    schemaVersion,
    artifactHashes,
    outputSchema: outputSchema ?? null,
  };
  return createHash('sha256').update(stableStringify(payload)).digest('hex');
}

function normalizeResult({
  envelope,
  cacheKey,
  schemaVersion,
  artifactHashes,
  source,
  attempt,
  itemKind,
}: {
  envelope: LlmResponseEnvelope;
  cacheKey: string;
  schemaVersion: string;
  artifactHashes: string[];
  source: string;
  attempt: number;
  itemKind: string;
}): NormalizedInvocationItem[] {
  const result = envelope.result ?? {};
  const output = result.output ?? {};
  const item: NormalizedInvocationItem = {
    kind: itemKind,
    runId: (result.runId ?? null) as any,
    prompt: (result.prompt ?? null) as any,
    model: (result.model ?? null) as any,
    schemaVersion,
    status: String(result.status ?? 'completed'),
    cacheKey,
    artifactHashes,
    output: {
      format: (output.format ?? (output.data ? 'json' : 'text')) as any,
      text: (output.text ?? null) as any,
      data: (output.data ?? null) as any,
    },
    usage: (result.usage ?? null) as any,
    metadata: (result.metadata ?? null) as any,
    warnings: (result.warnings ?? null) as any,
    diagnostics: (result.diagnostics ?? null) as any,
    createdAt: new Date().toISOString(),
    source,
    cached: source !== 'remote' && source !== 'openclaw' && source !== 'clawd' && source !== 'pi' && source !== 'http',
    attemptCount: attempt,
  };
  return [item];
}

async function persistOutputs({
  env,
  stateKey,
  cacheKey,
  items,
  stateType,
}: {
  env: any;
  stateKey: string | null;
  cacheKey: string;
  items: NormalizedInvocationItem[];
  stateType: string;
}) {
  if (!stateKey) return;
  const record = {
    type: stateType,
    version: STATE_VERSION,
    cacheKey,
    items,
    storedAt: new Date().toISOString(),
  };
  await writeStateJson({ env, key: stateKey, value: record });
}

function pickReusableState(stored: any, cacheKey: string, stateType: string) {
  if (!stored || typeof stored !== 'object') return null;
  if (stored.type !== stateType) return null;
  if (stored.cacheKey !== cacheKey) return null;
  if (!Array.isArray(stored.items)) return null;
  return { items: stored.items as NormalizedInvocationItem[] };
}

function collectAjvErrors(errors: ErrorObject[] | null | undefined) {
  if (!errors?.length) return [];
  return errors.map((err) => `${err.instancePath || '/'} ${err.message ?? ''}`.trim());
}

async function readCacheEntry(env: any, key: string, cacheNamespace: string): Promise<CacheEntry | null> {
  const filePath = path.join(getCacheDir(env), cacheNamespace, `${key}.json`);
  try {
    const text = await fsp.readFile(filePath, 'utf8');
    return JSON.parse(text) as CacheEntry;
  } catch (err: any) {
    if (err?.code === 'ENOENT') return null;
    throw err;
  }
}

async function writeCacheEntry(env: any, key: string, items: NormalizedInvocationItem[], cacheNamespace: string) {
  const dir = path.join(getCacheDir(env), cacheNamespace);
  await fsp.mkdir(dir, { recursive: true });
  const filePath = path.join(dir, `${key}.json`);
  await fsp.writeFile(
    filePath,
    JSON.stringify({ items, cacheKey: key, storedAt: new Date().toISOString() }, null, 2),
  );
}

function getCacheDir(env: any) {
  if (env?.LOBSTER_CACHE_DIR) return String(env.LOBSTER_CACHE_DIR);
  return path.join(process.cwd(), '.lobster-cache');
}

async function* streamOf(items: any[]) {
  for (const item of items) yield item;
}
```

## File: `src/commands/stdlib/llm_task_invoke.ts`
```typescript
export { llmTaskInvokeCommand } from './llm_invoke.js';
```

## File: `src/commands/stdlib/map.ts`
```typescript
function getByPath(obj: any, path: string): any {
  if (path === '.' || path === 'this') return obj;
  const parts = path.split('.').filter(Boolean);
  let cur: any = obj;
  for (const p of parts) {
    if (cur == null) return undefined;
    cur = cur[p];
  }
  return cur;
}

function renderTemplate(tpl: string, ctx: any): string {
  return tpl.replace(/\{\{\s*([^}]+?)\s*\}\}/g, (_m, expr) => {
    const key = String(expr ?? '').trim();
    const val = getByPath(ctx, key);
    if (val === undefined || val === null) return '';
    if (typeof val === 'string') return val;
    return JSON.stringify(val);
  });
}

function parseAssignments(tokens: any[]): Array<{ key: string; value: string }> {
  const out: Array<{ key: string; value: string }> = [];
  for (const tok of tokens ?? []) {
    const s = String(tok);
    const idx = s.indexOf('=');
    if (idx === -1) continue;
    const key = s.slice(0, idx).trim();
    const value = s.slice(idx + 1);
    if (!key) continue;
    out.push({ key, value });
  }
  return out;
}

export const mapCommand = {
  name: 'map',
  meta: {
    description: 'Transform items (wrap/unwrap/add fields)',
    argsSchema: {
      type: 'object',
      properties: {
        wrap: { type: 'string', description: 'Wrap each item as {wrap: item}' },
        unwrap: { type: 'string', description: 'Unwrap a field (yield item[unwrap])' },
        _: { type: 'array', items: { type: 'string' }, description: 'Optional assignments like key=value (value supports {{path}})' },
      },
      required: [],
    },
    sideEffects: [],
  },
  help() {
    return (
      `map — transform items\n\n` +
      `Usage:\n` +
      `  ... | map --wrap item\n` +
      `  ... | map --unwrap item\n` +
      `  ... | map foo=bar id={{id}}\n\n` +
      `Notes:\n` +
      `  - Assignments are added to an object item (preserves existing fields).\n` +
      `  - Assignment values support template placeholders like {{id}} and {{nested.field}}.\n`
    );
  },
  async run({ input, args }: any) {
    const wrap = typeof args.wrap === 'string' ? args.wrap : undefined;
    const unwrap = typeof args.unwrap === 'string' ? args.unwrap : undefined;
    const assignments = parseAssignments(Array.isArray(args._) ? args._ : []);

    if (wrap && unwrap) throw new Error('map cannot use both --wrap and --unwrap');

    return {
      output: (async function* () {
        for await (const item of input) {
          let cur: any = item;

          if (unwrap) {
            if (cur && typeof cur === 'object') cur = cur[unwrap];
            else cur = undefined;
            yield cur;
            continue;
          }

          if (wrap) {
            cur = { [wrap]: cur };
          }

          if (assignments.length > 0) {
            if (cur === null || typeof cur !== 'object' || Array.isArray(cur)) {
              // If current is not an object, turn it into one so we can attach fields.
              cur = { value: cur };
            }
            for (const { key, value } of assignments) {
              cur[key] = renderTemplate(String(value), item);
            }
          }

          yield cur;
        }
      })(),
    };
  },
};
```

## File: `src/commands/stdlib/openclaw_invoke.ts`
```typescript
function createInvokeCommand(commandName: string) {
  return {
    name: commandName,
    meta: {
      description: 'Call a local OpenClaw tool endpoint',
      argsSchema: {
        type: 'object',
        properties: {
          url: {
            type: 'string',
            description: 'OpenClaw control URL (or OPENCLAW_URL / CLAWD_URL)',
          },
          token: { type: 'string', description: 'Bearer token (or OPENCLAW_TOKEN / CLAWD_TOKEN)' },
          tool: { type: 'string', description: 'Tool name (e.g. message, cron, github, etc.)' },
          action: { type: 'string', description: 'Tool action' },
          'args-json': { type: 'string', description: 'JSON string of tool args' },
          sessionKey: { type: 'string', description: 'Optional session key attribution' },
          'session-key': { type: 'string', description: 'Alias for sessionKey' },
          dryRun: { type: 'boolean', description: 'Dry run' },
          'dry-run': { type: 'boolean', description: 'Alias for dryRun' },
          each: { type: 'boolean', description: 'Map each pipeline item into tool args' },
          itemKey: { type: 'string', description: 'Key to set from the pipeline item (default: item)' },
          'item-key': { type: 'string', description: 'Alias for itemKey' },
          _: { type: 'array', items: { type: 'string' } },
        },
        required: ['tool', 'action'],
      },
      sideEffects: ['calls_clawd_tool'],
    },
    help() {
      return (
        `${commandName} — call a local OpenClaw tool endpoint\n\n` +
        `Usage:\n` +
        `  ${commandName} --tool message --action send --args-json '{"provider":"telegram","to":"...","message":"..."}'\n` +
        `  ${commandName} --tool message --action send --args-json '{...}' --dry-run\n` +
        `  ... | ${commandName} --tool message --action send --each --item-key message --args-json '{"provider":"telegram","to":"..."}'\n\n` +
        `Config:\n` +
        `  - Uses OPENCLAW_URL env var by default (or pass --url).\n` +
        `  - Backward compatible: CLAWD_URL is also supported.\n` +
        `  - Optional Bearer token via OPENCLAW_TOKEN env var (or pass --token).\n` +
        `  - Backward compatible: CLAWD_TOKEN is also supported.\n` +
        `  - Optional attribution via --session-key <sessionKey>.\n\n` +
        `Notes:\n` +
        `  - This is a thin transport bridge. Lobster should not own OAuth/secrets.\n`
      );
    },
    async run({ input, args, ctx }) {
      const each = Boolean(args.each);
      const itemKey = String(args.itemKey ?? args['item-key'] ?? 'item');

      const url = String(args.url ?? ctx.env.OPENCLAW_URL ?? ctx.env.CLAWD_URL ?? '').trim();
      if (!url) throw new Error(`${commandName} requires --url or OPENCLAW_URL`);

      const tool = args.tool;
      const action = args.action;
      if (!tool || !action) throw new Error(`${commandName} requires --tool and --action`);

      const token = String(args.token ?? ctx.env.OPENCLAW_TOKEN ?? ctx.env.CLAWD_TOKEN ?? '').trim();

      let toolArgs: any = {};
      if (args['args-json']) {
        try {
          toolArgs = JSON.parse(String(args['args-json']));
        } catch (_err) {
          throw new Error(`${commandName} --args-json must be valid JSON`);
        }
      }

      if (each && (toolArgs === null || typeof toolArgs !== 'object' || Array.isArray(toolArgs))) {
        throw new Error(`${commandName} --each requires --args-json to be an object`);
      }

      const endpoint = new URL('/tools/invoke', url);
      const sessionKey = args.sessionKey ?? args['session-key'] ?? null;
      const dryRun = args.dryRun ?? args['dry-run'] ?? null;

      const invokeOnce = async (argsValue: unknown) => {
        const res = await fetch(endpoint, {
          method: 'POST',
          headers: {
            'content-type': 'application/json',
            ...(token ? { authorization: `Bearer ${token}` } : null),
          },
          body: JSON.stringify({
            tool: String(tool),
            action: String(action),
            args: argsValue,
            ...(sessionKey ? { sessionKey: String(sessionKey) } : null),
            ...(dryRun !== null ? { dryRun: Boolean(dryRun) } : null),
          }),
        });

        const text = await res.text();
        if (!res.ok) {
          throw new Error(`${commandName} failed (${res.status}): ${text.slice(0, 400)}`);
        }

        let parsed: any;
        try {
          parsed = text ? JSON.parse(text) : null;
        } catch (_err) {
          throw new Error(`${commandName} expected JSON response`);
        }

        // Preferred: { ok: true, result: ... }
        if (parsed && typeof parsed === 'object' && !Array.isArray(parsed) && 'ok' in parsed) {
          if (parsed.ok !== true) {
            const msg = parsed?.error?.message ?? 'Unknown error';
            throw new Error(`${commandName} tool error: ${msg}`);
          }
          const result = parsed.result;
          return Array.isArray(result) ? result : [result];
        }

        // Compatibility: raw JSON result
        return Array.isArray(parsed) ? parsed : [parsed];
      };

      if (!each) {
        // Drain input: for now we don't stream input into clawd calls.
        for await (const _item of input) {
          // no-op
        }
        const items = await invokeOnce(toolArgs);
        return { output: asStream(items) };
      }

      const out: any[] = [];
      for await (const item of input) {
        const argsValue = { ...(toolArgs as any), [itemKey]: item };
        const items = await invokeOnce(argsValue);
        out.push(...items);
      }

      return { output: asStream(out) };
    },
  };
}

async function* asStream(items: any[]) {
  for (const item of items) yield item;
}

export const openclawInvokeCommand = createInvokeCommand('openclaw.invoke');
export const clawdInvokeCommand = createInvokeCommand('clawd.invoke');
```

## File: `src/commands/stdlib/pick.ts`
```typescript
export const pickCommand = {
  name: 'pick',
  meta: {
    description: 'Project fields from objects',
    argsSchema: {
      type: 'object',
      properties: {
        _: {
          type: 'array',
          items: { type: 'string' },
          description: 'First positional arg is a comma-separated list of fields',
        },
      },
      required: ['_'],
    },
    sideEffects: [],
  },
  help() {
    return `pick — project fields from objects\n\nUsage:\n  ... | pick id,subject,from\n`;
  },
  async run({ input, args }) {
    const spec = args._[0];
    if (!spec) throw new Error('pick requires a comma-separated field list');
    const fields = spec.split(',').map((s) => s.trim()).filter(Boolean);

    return {
      output: (async function* () {
        for await (const item of input) {
          if (item === null || typeof item !== 'object') {
            yield item;
            continue;
          }
          const out = {};
          for (const f of fields) out[f] = item[f];
          yield out;
        }
      })(),
    };
  },
};
```

## File: `src/commands/stdlib/sort.ts`
```typescript
function getByPath(obj: any, path: string): any {
  if (!path) return undefined;
  const parts = path.split('.').filter(Boolean);
  let cur: any = obj;
  for (const p of parts) {
    if (cur == null) return undefined;
    cur = cur[p];
  }
  return cur;
}

function defaultCompare(a: any, b: any): number {
  // Treat undefined/null as last
  const aU = a === undefined || a === null;
  const bU = b === undefined || b === null;
  if (aU && bU) return 0;
  if (aU) return 1;
  if (bU) return -1;

  // number compare if both numbers
  if (typeof a === 'number' && typeof b === 'number') return a - b;

  // Deterministic lexical compare independent of process locale.
  const aStr = String(a);
  const bStr = String(b);
  if (aStr < bStr) return -1;
  if (aStr > bStr) return 1;
  return 0;
}

export const sortCommand = {
  name: 'sort',
  meta: {
    description: 'Sort items (stable) by a key or by stringified value',
    argsSchema: {
      type: 'object',
      properties: {
        key: { type: 'string', description: 'Dot-path key to sort by (e.g. updatedAt, pr.number)' },
        desc: { type: 'boolean', description: 'Sort descending' },
        _: { type: 'array', items: { type: 'string' } },
      },
      required: [],
    },
    sideEffects: [],
  },
  help() {
    return (
      `sort — sort items (stable) by a key\n\n` +
      `Usage:\n` +
      `  ... | sort\n` +
      `  ... | sort --key updatedAt\n` +
      `  ... | sort --key prNumber --desc\n\n` +
      `Notes:\n` +
      `  - Sorting is stable (preserves order for equal keys).\n` +
      `  - undefined/null keys sort last.\n`
    );
  },
  async run({ input, args }: any) {
    const key = typeof args.key === 'string' ? args.key : undefined;
    const desc = Boolean(args.desc);

    const items: any[] = [];
    let idx = 0;
    for await (const item of input) {
      items.push({ item, idx });
      idx++;
    }

    items.sort((a, b) => {
      const av = key ? getByPath(a.item, key) : a.item;
      const bv = key ? getByPath(b.item, key) : b.item;
      const c = defaultCompare(av, bv);
      if (c !== 0) return desc ? -c : c;
      // stable tie-break
      return a.idx - b.idx;
    });

    return {
      output: (async function* () {
        for (const x of items) yield x.item;
      })(),
    };
  },
};
```

## File: `src/commands/stdlib/state.ts`
```typescript
import { promises as fsp } from 'node:fs';

import { defaultStateDir, keyToPath } from '../../state/store.js';

export const stateGetCommand = {
  name: 'state.get',
  meta: {
    description: 'Read a JSON value from Lobster state',
    argsSchema: {
      type: 'object',
      properties: {
        _: { type: 'array', items: { type: 'string' }, description: 'Key' },
      },
      required: ['_'],
    },
    sideEffects: ['reads_state'],
  },
  help() {
    return `state.get — read a JSON value from Lobster state\n\nUsage:\n  state.get <key>\n\nEnv:\n  LOBSTER_STATE_DIR overrides storage directory\n`;
  },
  async run({ args, ctx }) {
    const key = args._[0];
    if (!key) throw new Error('state.get requires a key');

    const stateDir = defaultStateDir(ctx.env);
    const filePath = keyToPath(stateDir, key);

    let value = null;
    try {
      const text = await fsp.readFile(filePath, 'utf8');
      value = JSON.parse(text);
    } catch (err) {
      if (err?.code === 'ENOENT') {
        value = null;
      } else {
        throw err;
      }
    }

    return { output: asStream([value]) };
  },
};

export const stateSetCommand = {
  name: 'state.set',
  meta: {
    description: 'Write a JSON value to Lobster state',
    argsSchema: {
      type: 'object',
      properties: {
        _: { type: 'array', items: { type: 'string' }, description: 'Key' },
      },
      required: ['_'],
    },
    sideEffects: ['writes_state'],
  },
  help() {
    return `state.set — write a JSON value to Lobster state\n\nUsage:\n  <value> | state.set <key>\n\nNotes:\n  - Consumes the entire input stream; stores a single JSON value.\n`;
  },
  async run({ input, args, ctx }) {
    const key = args._[0];
    if (!key) throw new Error('state.set requires a key');

    const items = [];
    for await (const item of input) items.push(item);

    const value = items.length === 1 ? items[0] : items;

    const stateDir = defaultStateDir(ctx.env);
    const filePath = keyToPath(stateDir, key);

    await fsp.mkdir(stateDir, { recursive: true });
    await fsp.writeFile(filePath, JSON.stringify(value, null, 2) + '\n', 'utf8');

    return { output: asStream([value]) };
  },
};

async function* asStream(items) {
  for (const item of items) yield item;
}
```

## File: `src/commands/stdlib/table.ts`
```typescript
function stringifyCell(v) {
  if (v === null || v === undefined) return '';
  if (typeof v === 'string') return v;
  if (typeof v === 'number' || typeof v === 'boolean') return String(v);
  return JSON.stringify(v);
}

export const tableCommand = {
  name: 'table',
  meta: {
    description: 'Render items as a simple table',
    argsSchema: { type: 'object', properties: {}, required: [] },
    sideEffects: [],
  },
  help() {
    return `table — render items as a simple table\n\nUsage:\n  ... | table\n\nNotes:\n  - If items are objects, columns are union of keys (first 20 items).\n`;
  },
  async run({ input, ctx }) {
    const items = [];
    for await (const item of input) items.push(item);

    if (items.length === 0) {
      ctx.stdout.write('(no results)\n');
      return { output: emptyStream(), rendered: true };
    }

    const sample = items.slice(0, 20);
    const objectItems = sample.filter((x) => x && typeof x === 'object' && !Array.isArray(x));

    if (objectItems.length === sample.length) {
      const cols = [];
      const seen = new Set();
      for (const obj of objectItems) {
        for (const k of Object.keys(obj)) {
          if (!seen.has(k)) {
            seen.add(k);
            cols.push(k);
          }
        }
      }

      const rows = [cols, ...items.map((it) => cols.map((c) => stringifyCell(it?.[c])))]
        .map((row) => row.map((cell) => cell.replace(/\n/g, ' ')));

      const widths = cols.map((_, i) => Math.max(...rows.map((r) => r[i].length), 3));

      const renderRow = (row) => row.map((cell, i) => cell.padEnd(widths[i])).join('  ');
      ctx.stdout.write(renderRow(rows[0]) + '\n');
      ctx.stdout.write(widths.map((w) => '-'.repeat(w)).join('  ') + '\n');
      for (const row of rows.slice(1)) ctx.stdout.write(renderRow(row) + '\n');

      return { output: emptyStream(), rendered: true };
    }

    // Fallback: render each item on a line.
    for (const item of items) ctx.stdout.write(stringifyCell(item) + '\n');
    return { output: emptyStream(), rendered: true };
  },
};

async function* emptyStream() {}
```

## File: `src/commands/stdlib/template.ts`
```typescript
import fs from 'node:fs/promises';

function getByPath(obj: any, path: string): any {
  if (path === '.' || path === 'this') return obj;
  const parts = path.split('.').filter(Boolean);
  let cur: any = obj;
  for (const p of parts) {
    if (cur == null) return undefined;
    cur = cur[p];
  }
  return cur;
}

function renderTemplate(tpl: string, ctx: any): string {
  return tpl.replace(/\{\{\s*([^}]+?)\s*\}\}/g, (_m, expr) => {
    const key = String(expr ?? '').trim();
    const val = getByPath(ctx, key);
    if (val === undefined || val === null) return '';
    if (typeof val === 'string') return val;
    return JSON.stringify(val);
  });
}

export const templateCommand = {
  name: 'template',
  meta: {
    description: 'Render a simple {{path}} template against each input item',
    argsSchema: {
      type: 'object',
      properties: {
        text: { type: 'string', description: 'Template text (supports {{path}}; {{.}} for the whole item)' },
        file: { type: 'string', description: 'Template file path' },
        _: { type: 'array', items: { type: 'string' } },
      },
      required: [],
    },
    sideEffects: [],
  },
  help() {
    return (
      `template — render a simple template against each item\n\n` +
      `Usage:\n` +
      `  ... | template --text 'PR {{number}}: {{title}}'\n` +
      `  ... | template --file ./draft.txt\n\n` +
      `Template syntax:\n` +
      `  - {{field}} or {{nested.field}}\n` +
      `  - {{.}} for the whole item\n` +
      `  - Missing values render as empty string\n`
    );
  },
  async run({ input, args }: any) {
    let tpl = typeof args.text === 'string' ? args.text : undefined;
    const file = typeof args.file === 'string' ? args.file : undefined;

    if (!tpl && file) {
      tpl = await fs.readFile(file, 'utf8');
    }

    if (!tpl) {
      const positional = Array.isArray(args._) ? args._ : [];
      if (positional.length) tpl = positional.join(' ');
    }

    if (!tpl) throw new Error('template requires --text or --file (or positional text)');

    return {
      output: (async function* () {
        for await (const item of input) {
          yield renderTemplate(String(tpl), item);
        }
      })(),
    };
  },
};
```

## File: `src/commands/stdlib/where.ts`
```typescript
function parsePredicate(expr) {
  const m = expr.match(/^([a-zA-Z0-9_.]+)\s*(==|=|!=|<=|>=|<|>)\s*(.+)$/);
  if (!m) throw new Error(`Invalid where expression: ${expr}`);
  const [, path, op, rawValue] = m;

  let value = rawValue;
  if (rawValue === 'true') value = true;
  else if (rawValue === 'false') value = false;
  else if (rawValue === 'null') value = null;
  else if (!Number.isNaN(Number(rawValue)) && rawValue.trim() !== '') value = Number(rawValue);

  return { path, op: op === '=' ? '==' : op, value };
}

function getPath(obj, path) {
  const parts = path.split('.');
  let cur = obj;
  for (const p of parts) {
    if (cur === null || typeof cur !== 'object') return undefined;
    cur = cur[p];
  }
  return cur;
}

function compare(left, op, right) {
  switch (op) {
    case '==': return left == right; // intentional loose equality for convenience
    case '!=': return left != right;
    case '<': return left < right;
    case '<=': return left <= right;
    case '>': return left > right;
    case '>=': return left >= right;
    default: throw new Error(`Unsupported operator: ${op}`);
  }
}

export const whereCommand = {
  name: 'where',
  meta: {
    description: 'Filter objects by a simple predicate',
    argsSchema: {
      type: 'object',
      properties: {
        _: {
          type: 'array',
          items: { type: 'string' },
          description: 'First positional arg is an expression like field=value or minutes>=30',
        },
      },
      required: ['_'],
    },
    sideEffects: [],
  },
  help() {
    return `where — filter objects by a simple predicate\n\nUsage:\n  ... | where unread=true\n  ... | where minutes>=30\n  ... | where sender.domain==example.com\n`;
  },
  async run({ input, args }) {
    const expr = args._[0];
    if (!expr) throw new Error('where requires an expression (e.g. field=value)');
    const pred = parsePredicate(expr);

    return {
      output: (async function* () {
        for await (const item of input) {
          const left = getPath(item, pred.path);
          if (compare(left, pred.op, pred.value)) yield item;
        }
      })(),
    };
  },
};
```

## File: `src/commands/workflows/workflows_list.ts`
```typescript
import { listWorkflows } from '../../workflows/registry.js';

export const workflowsListCommand = {
  name: 'workflows.list',
  meta: {
    description: 'List available Lobster workflows',
    argsSchema: { type: 'object', properties: {}, required: [] },
    sideEffects: [],
  },
  help() {
    return `workflows.list — list available Lobster workflows\n\nUsage:\n  workflows.list\n\nNotes:\n  - Intended for OpenClaw to discover workflows dynamically.\n`;
  },
  async run({ input }) {
    // Drain input.
    for await (const _item of input) {
      // no-op
    }

    return { output: asStream(listWorkflows()) };
  },
};

async function* asStream(items) {
  for (const item of items) yield item;
}
```

## File: `src/commands/workflows/workflows_run.ts`
```typescript
import { workflowRegistry } from '../../workflows/registry.js';
import { runGithubPrMonitorWorkflow, runGithubPrMonitorNotifyWorkflow } from '../../workflows/github_pr_monitor.js';

const runners = {
  'github.pr.monitor': runGithubPrMonitorWorkflow,
  'github.pr.monitor.notify': runGithubPrMonitorNotifyWorkflow,
};

// Recipe runners - adapt SDK recipes to workflow runner interface
const recipeRunners = {};


export const workflowsRunCommand = {
  name: 'workflows.run',
  meta: {
    description: 'Run a named Lobster workflow',
    argsSchema: {
      type: 'object',
      properties: {
        name: { type: 'string', description: 'Workflow name' },
        'args-json': { type: 'string', description: 'JSON string of workflow args' },
        _: { type: 'array', items: { type: 'string' } },
      },
      required: ['name'],
    },
    sideEffects: [],
  },
  help() {
    return `workflows.run — run a named Lobster workflow\n\nUsage:\n  workflows.run --name <workflow> [--args-json '{...}']\n\nExample:\n  workflows.run --name github.pr.monitor.notify --args-json '{"repo":"openclaw/openclaw","pr":1152}'\n`;
  },
  async run({ input, args, ctx }) {
    // Drain input.
    for await (const _item of input) {
      // no-op
    }

    const name = args.name ?? args._[0];
    if (!name) throw new Error('workflows.run requires --name');

    // Check for recipe-based workflow first
    const recipeRunner = recipeRunners[name];
    if (recipeRunner) {
      let workflowArgs = {};
      if (args['args-json']) {
        try {
          workflowArgs = JSON.parse(String(args['args-json']));
        } catch {
          throw new Error('workflows.run --args-json must be valid JSON');
        }
      }
      const result = await recipeRunner({ args: workflowArgs, ctx });
      return { output: asStream([result]) };
    }

    // Fall back to legacy workflow registry
    const meta = workflowRegistry[name];
    if (!meta) throw new Error(`Unknown workflow: ${name}`);

    const runner = runners[name];
    if (!runner) throw new Error(`Workflow runner not implemented: ${name}`);

    let workflowArgs = {};
    if (args['args-json']) {
      try {
        workflowArgs = JSON.parse(String(args['args-json']));
      } catch {
        throw new Error('workflows.run --args-json must be valid JSON');
      }
    }

    const result = await runner({ args: workflowArgs, ctx });
    return { output: asStream([result]) };
  },
};

async function* asStream(items) {
  for (const item of items) yield item;
}
```

## File: `src/core/index.ts`
```typescript
export { createDefaultRegistry } from '../commands/registry.js';
export { parsePipeline } from '../parser.js';
export { runPipeline } from '../runtime.js';
export { runWorkflowFile } from '../workflows/file.js';
export { decodeResumeToken } from '../resume.js';
export { runToolRequest, resumeToolRequest, createToolContext } from './tool_runtime.js';
```

## File: `src/core/tool_runtime.ts`
```typescript
import { randomUUID } from 'node:crypto';
import { Writable } from 'node:stream';
import path from 'node:path';

import { createDefaultRegistry } from '../commands/registry.js';
import { parsePipeline } from '../parser.js';
import { decodeResumeToken } from '../resume.js';
import { runPipeline } from '../runtime.js';
import { encodeToken } from '../token.js';
import { readStateJson, writeStateJson, deleteStateJson } from '../state/store.js';
import { runWorkflowFile } from '../workflows/file.js';

type PipelineResumeState = {
  pipeline: Array<{ name: string; args: Record<string, unknown>; raw: string }>;
  resumeAtIndex: number;
  items: unknown[];
  prompt?: string;
  createdAt: string;
};

type ToolRunContext = {
  cwd?: string;
  env?: Record<string, string | undefined>;
  mode?: 'tool' | 'human' | 'sdk';
  stdin?: NodeJS.ReadableStream;
  stdout?: NodeJS.WritableStream;
  stderr?: NodeJS.WritableStream;
  signal?: AbortSignal;
  registry?: any;
  llmAdapters?: Record<string, any>;
};

type ToolEnvelope = {
  protocolVersion: 1;
  ok: boolean;
  status?: 'ok' | 'needs_approval' | 'cancelled';
  output?: unknown[];
  requiresApproval?: {
    type?: 'approval_request';
    prompt: string;
    items: unknown[];
    preview?: string;
    resumeToken?: string;
  } | null;
  error?: {
    type: string;
    message: string;
  };
};

export async function runToolRequest({
  pipeline,
  filePath,
  args,
  ctx = {},
}: {
  pipeline?: string;
  filePath?: string;
  args?: Record<string, unknown>;
  ctx?: ToolRunContext;
}): Promise<ToolEnvelope> {
  const runtime = createToolContext(ctx);
  const hasPipeline = typeof pipeline === 'string' && pipeline.trim().length > 0;
  const hasFile = typeof filePath === 'string' && filePath.trim().length > 0;

  if (!hasPipeline && !hasFile) {
    return errorEnvelope('parse_error', 'run requires either pipeline or filePath');
  }
  if (hasPipeline && hasFile) {
    return errorEnvelope('parse_error', 'run accepts either pipeline or filePath, not both');
  }

  if (hasFile) {
    let resolvedFilePath: string;
    try {
      resolvedFilePath = await resolveWorkflowFile(filePath!, runtime.cwd);
    } catch (err: any) {
      return errorEnvelope('parse_error', err?.message ?? String(err));
    }

    try {
      const output = await runWorkflowFile({
        filePath: resolvedFilePath,
        args,
        ctx: runtime,
      });

      if (output.status === 'needs_approval') {
        return okEnvelope('needs_approval', [], output.requiresApproval ?? null);
      }
      if (output.status === 'cancelled') {
        return okEnvelope('cancelled', [], null);
      }
      return okEnvelope('ok', output.output, null);
    } catch (err: any) {
      return errorEnvelope('runtime_error', err?.message ?? String(err));
    }
  }

  let parsed;
  try {
    parsed = parsePipeline(String(pipeline));
  } catch (err: any) {
    return errorEnvelope('parse_error', err?.message ?? String(err));
  }

  try {
    const output = await runPipeline({
      pipeline: parsed,
      registry: runtime.registry,
      input: [],
      stdin: runtime.stdin,
      stdout: runtime.stdout,
      stderr: runtime.stderr,
      env: runtime.env,
      mode: 'tool',
      cwd: runtime.cwd,
      llmAdapters: runtime.llmAdapters,
      signal: runtime.signal,
    });

    const approval = output.halted && output.items.length === 1 && output.items[0]?.type === 'approval_request'
      ? output.items[0]
      : null;

    if (approval) {
      const stateKey = await savePipelineResumeState(runtime.env, {
        pipeline: parsed,
        resumeAtIndex: (output.haltedAt?.index ?? -1) + 1,
        items: approval.items,
        prompt: approval.prompt,
        createdAt: new Date().toISOString(),
      });

      const resumeToken = encodeToken({
        protocolVersion: 1,
        v: 1,
        kind: 'pipeline-resume',
        stateKey,
      });

      return okEnvelope('needs_approval', [], {
        ...approval,
        resumeToken,
      });
    }

    return okEnvelope('ok', output.items, null);
  } catch (err: any) {
    return errorEnvelope('runtime_error', err?.message ?? String(err));
  }
}

export async function resumeToolRequest({
  token,
  approved,
  ctx = {},
}: {
  token: string;
  approved: boolean;
  ctx?: ToolRunContext;
}): Promise<ToolEnvelope> {
  const runtime = createToolContext(ctx);
  let payload: any;

  try {
    payload = decodeResumeToken(token);
  } catch (err: any) {
    return errorEnvelope('parse_error', err?.message ?? String(err));
  }

  if (!approved) {
    if (payload.kind === 'workflow-file' && payload.stateKey) {
      await deleteStateJson({ env: runtime.env, key: payload.stateKey });
    }
    if (payload.kind === 'pipeline-resume' && payload.stateKey) {
      await deleteStateJson({ env: runtime.env, key: payload.stateKey });
    }
    return okEnvelope('cancelled', [], null);
  }

  if (payload.kind === 'workflow-file') {
    try {
      const output = await runWorkflowFile({
        filePath: payload.filePath,
        ctx: runtime,
        resume: payload,
        approved: true,
      });

      if (output.status === 'needs_approval') {
        return okEnvelope('needs_approval', [], output.requiresApproval ?? null);
      }
      if (output.status === 'cancelled') {
        return okEnvelope('cancelled', [], null);
      }
      return okEnvelope('ok', output.output, null);
    } catch (err: any) {
      return errorEnvelope('runtime_error', err?.message ?? String(err));
    }
  }

  let resumeState: PipelineResumeState;
  try {
    resumeState = await loadPipelineResumeState(runtime.env, payload.stateKey);
  } catch (err: any) {
    return errorEnvelope('runtime_error', err?.message ?? String(err));
  }

  const remaining = resumeState.pipeline.slice(resumeState.resumeAtIndex);
  const input = streamFromItems(resumeState.items);

  try {
    const output = await runPipeline({
      pipeline: remaining,
      registry: runtime.registry,
      stdin: runtime.stdin,
      stdout: runtime.stdout,
      stderr: runtime.stderr,
      env: runtime.env,
      mode: 'tool',
      cwd: runtime.cwd,
      llmAdapters: runtime.llmAdapters,
      signal: runtime.signal,
      input,
    });

    const approval = output.halted && output.items.length === 1 && output.items[0]?.type === 'approval_request'
      ? output.items[0]
      : null;

    if (approval) {
      const nextStateKey = await savePipelineResumeState(runtime.env, {
        pipeline: remaining,
        resumeAtIndex: (output.haltedAt?.index ?? -1) + 1,
        items: approval.items,
        prompt: approval.prompt,
        createdAt: new Date().toISOString(),
      });
      await deleteStateJson({ env: runtime.env, key: payload.stateKey });

      const resumeToken = encodeToken({
        protocolVersion: 1,
        v: 1,
        kind: 'pipeline-resume',
        stateKey: nextStateKey,
      });

      return okEnvelope('needs_approval', [], {
        ...approval,
        resumeToken,
      });
    }

    await deleteStateJson({ env: runtime.env, key: payload.stateKey });
    return okEnvelope('ok', output.items, null);
  } catch (err: any) {
    return errorEnvelope('runtime_error', err?.message ?? String(err));
  }
}

export function createToolContext(ctx: ToolRunContext = {}) {
  return {
    cwd: ctx.cwd ?? process.cwd(),
    env: { ...process.env, ...ctx.env },
    mode: 'tool' as const,
    stdin: ctx.stdin ?? process.stdin,
    stdout: ctx.stdout ?? createCaptureStream(),
    stderr: ctx.stderr ?? createCaptureStream(),
    signal: ctx.signal,
    registry: ctx.registry ?? createDefaultRegistry(),
    llmAdapters: ctx.llmAdapters,
  };
}

export function createCaptureStream() {
  return new Writable({
    write(_chunk, _encoding, callback) {
      callback();
    },
  });
}

function okEnvelope(status: 'ok' | 'needs_approval' | 'cancelled', output: unknown[], requiresApproval: ToolEnvelope['requiresApproval']) {
  return {
    protocolVersion: 1 as const,
    ok: true,
    status,
    output,
    requiresApproval,
  };
}

function errorEnvelope(type: string, message: string): ToolEnvelope {
  return {
    protocolVersion: 1,
    ok: false,
    error: { type, message },
  };
}

function streamFromItems(items: unknown[]) {
  return (async function* () {
    for (const item of items) {
      yield item;
    }
  })();
}

async function savePipelineResumeState(env: Record<string, string | undefined>, state: PipelineResumeState) {
  const stateKey = `pipeline_resume_${randomUUID()}`;
  await writeStateJson({ env, key: stateKey, value: state });
  return stateKey;
}

async function loadPipelineResumeState(env: Record<string, string | undefined>, stateKey: string) {
  const stored = await readStateJson({ env, key: stateKey });
  if (!stored || typeof stored !== 'object') {
    throw new Error('Pipeline resume state not found');
  }
  const data = stored as Partial<PipelineResumeState>;
  if (!Array.isArray(data.pipeline)) throw new Error('Invalid pipeline resume state');
  if (typeof data.resumeAtIndex !== 'number') throw new Error('Invalid pipeline resume state');
  if (!Array.isArray(data.items)) throw new Error('Invalid pipeline resume state');
  return data as PipelineResumeState;
}

async function resolveWorkflowFile(candidate: string, cwd: string) {
  const { stat } = await import('node:fs/promises');
  const resolved = path.isAbsolute(candidate) ? candidate : path.resolve(cwd, candidate);
  const fileStat = await stat(resolved);
  if (!fileStat.isFile()) throw new Error('Workflow path is not a file');
  const ext = path.extname(resolved).toLowerCase();
  if (!['.lobster', '.yaml', '.yml', '.json'].includes(ext)) {
    throw new Error('Workflow file must end in .lobster, .yaml, .yml, or .json');
  }
  return resolved;
}
```

## File: `src/recipes/index.ts`
```typescript
/**
 * Recipe entrypoints.
 *
 * Core Lobster intentionally keeps only OpenClaw-first recipes here.
 */

export * from "./github/index.js";
```

## File: `src/recipes/registry.ts`
```typescript
/**
 * Recipe registry for discovery.
 */

import { prMonitor, prMonitorNotify } from "./github/pr-monitor.js";

const recipes: Record<string, any> = {
  "github.pr.monitor": prMonitor,
  "github.pr.monitor.notify": prMonitorNotify,
};

export function registerRecipe(fn) {
  const meta = fn?.meta ?? {};
  const name = meta.name;
  if (!name) throw new Error("Recipe is missing meta.name");
  recipes[name] = fn;
}

export function listRecipes() {
  return Object.entries(recipes).map(([name, fn]) => {
    const meta: any = (fn as any).meta ?? {};
    return {
      name,
      description: meta.description ?? "",
      requires: meta.requires ?? [],
      args: meta.args ?? {},
    };
  });
}

export function getRecipe(name) {
  return recipes[name];
}
```

## File: `src/recipes/github/index.ts`
```typescript
/**
 * GitHub Recipes
 *
 * @example
 * import { prMonitor, prMonitorNotify } from 'lobster/recipes/github';
 *
 * const result = await prMonitor({ repo: 'owner/repo', pr: 123 }).run();
 */

export { prMonitor, prMonitorNotify } from './pr-monitor.js';
export { ghPrView } from './stages/pr-view.js';

// Register recipes
import { registerRecipe } from '../registry.js';
import { prMonitor, prMonitorNotify } from './pr-monitor.js';

registerRecipe(prMonitor);
registerRecipe(prMonitorNotify);
```

## File: `src/recipes/github/pr-monitor.ts`
```typescript
/**
 * GitHub PR Monitor Recipe - Track PR changes over time
 *
 * @example
 * import { prMonitor, prMonitorNotify } from 'lobster/recipes/github';
 *
 * // Full PR state with diff
 * const result = await prMonitor({ repo: 'owner/repo', pr: 123 }).run();
 *
 * // Compact notification when changed
 * const notify = await prMonitorNotify({ repo: 'owner/repo', pr: 123 }).run();
 */

import { Lobster } from '../../sdk/index.js';
import { diffLast } from '../../sdk/primitives/diff.js';
import { ghPrView } from './stages/pr-view.js';

/**
 * Pick a subset of PR fields for comparison
 * @param {Object} snapshot
 * @returns {Object|null}
 */
function pickSubset(snapshot) {
  if (!snapshot || typeof snapshot !== 'object') return null;
  return {
    number: snapshot.number,
    title: snapshot.title,
    url: snapshot.url,
    state: snapshot.state,
    isDraft: snapshot.isDraft,
    mergeable: snapshot.mergeable,
    reviewDecision: snapshot.reviewDecision,
    updatedAt: snapshot.updatedAt,
    baseRefName: snapshot.baseRefName,
    headRefName: snapshot.headRefName,
  };
}

/**
 * Build a summary of what changed between two snapshots
 * @param {Object|null} before
 * @param {Object} after
 * @returns {{ changedFields: string[], changes: Object }}
 */
function buildChangeSummary(before, after) {
  const a = pickSubset(after);
  const b = pickSubset(before);

  if (!a) return { changedFields: [], changes: {} };
  if (!b) {
    return {
      changedFields: Object.keys(a),
      changes: Object.fromEntries(Object.keys(a).map((k) => [k, { from: null, to: a[k] }])),
    };
  }

  const changes = {};
  for (const key of Object.keys(a)) {
    if (JSON.stringify(a[key]) !== JSON.stringify(b[key])) {
      changes[key] = { from: b[key], to: a[key] };
    }
  }

  return {
    changedFields: Object.keys(changes),
    changes,
  };
}

/**
 * Format a human-readable change message
 * @param {Object} options
 * @returns {string}
 */
function formatChangeMessage({ repo, pr, changedFields, prInfo }) {
  const fields = changedFields.length ? ` (${changedFields.join(', ')})` : '';
  const title = prInfo?.title ? `: ${prInfo.title}` : '';
  const url = prInfo?.url ? ` ${prInfo.url}` : '';
  return `PR updated: ${repo}#${pr}${title}${fields}.${url}`.replace(/\s+/g, ' ').trim();
}

/**
 * Create a PR monitor workflow
 *
 * @param {Object} options
 * @param {string} options.repo - Repository in owner/repo format
 * @param {number} options.pr - PR number
 * @param {string} [options.key] - State key override
 * @param {boolean} [options.changesOnly=false] - Only output when changed
 * @param {boolean} [options.summaryOnly=false] - Return compact summary
 * @returns {Lobster}
 */
export function prMonitor(options) {
  const { repo, pr, changesOnly = false, summaryOnly = false } = options;
  const key = options.key ?? `github.pr:${repo}#${pr}`;

  if (!repo) throw new Error('prMonitor requires repo');
  if (!pr) throw new Error('prMonitor requires pr');

  const workflow = new Lobster()
    .pipe(ghPrView({ repo, pr }))
    .pipe(diffLast(key))
    .pipe((results) => {
      const diffResult = results[0];
      const current = diffResult.after;
      const before = diffResult.before;
      const changed = diffResult.changed;

      // If changesOnly and no change, suppress output
      if (changesOnly && !changed) {
        return [{
          kind: 'github.pr.monitor',
          repo,
          pr: Number(pr),
          key,
          changed: false,
          suppressed: true,
        }];
      }

      const summary = buildChangeSummary(before, current);

      if (summaryOnly) {
        return [{
          kind: 'github.pr.monitor',
          repo,
          pr: Number(pr),
          key,
          changed,
          summary,
          prInfo: {
            number: current.number,
            title: current.title,
            url: current.url,
            state: current.state,
            updatedAt: current.updatedAt,
          },
        }];
      }

      return [{
        kind: 'github.pr.monitor',
        repo,
        pr: Number(pr),
        key,
        changed,
        summary,
        prSnapshot: current,
      }];
    })
    .meta({
      name: 'github.pr.monitor',
      description: 'Monitor PR state and detect changes',
      requires: ['gh'],
      args: {
        repo: { type: 'string', required: true, description: 'Repository (owner/repo)' },
        pr: { type: 'number', required: true, description: 'PR number' },
        key: { type: 'string', description: 'State key override' },
        changesOnly: { type: 'boolean', default: false, description: 'Only output when changed' },
        summaryOnly: { type: 'boolean', default: false, description: 'Return compact summary' },
      },
    });

  return workflow;
}

// Attach metadata
prMonitor.meta = {
  name: 'github.pr.monitor',
  description: 'Monitor PR state and detect changes',
  requires: ['gh'],
  args: {
    repo: { type: 'string', required: true },
    pr: { type: 'number', required: true },
    key: { type: 'string' },
    changesOnly: { type: 'boolean', default: false },
    summaryOnly: { type: 'boolean', default: false },
  },
};

/**
 * Create a PR monitor notify workflow
 * Returns a compact message only when PR changes
 *
 * @param {Object} options
 * @param {string} options.repo - Repository in owner/repo format
 * @param {number} options.pr - PR number
 * @param {string} [options.key] - State key override
 * @returns {Lobster}
 */
export function prMonitorNotify(options) {
  const { repo, pr } = options;
  const key = options.key ?? `github.pr:${repo}#${pr}`;

  if (!repo) throw new Error('prMonitorNotify requires repo');
  if (!pr) throw new Error('prMonitorNotify requires pr');

  const workflow = new Lobster()
    .pipe(ghPrView({ repo, pr }))
    .pipe(diffLast(key, { changesOnly: true }))
    .pipe((results) => {
      const diffResult = results[0];

      if (diffResult.suppressed) {
        return [{ kind: 'github.pr.monitor.notify', suppressed: true }];
      }

      const current = diffResult.after;
      const before = diffResult.before;
      const summary = buildChangeSummary(before, current);

      const message = formatChangeMessage({
        repo,
        pr: Number(pr),
        changedFields: summary.changedFields,
        prInfo: current,
      });

      return [{
        kind: 'github.pr.monitor.notify',
        changed: true,
        repo,
        pr: Number(pr),
        message,
        prInfo: {
          number: current.number,
          title: current.title,
          url: current.url,
          state: current.state,
        },
        summary,
      }];
    })
    .meta({
      name: 'github.pr.monitor.notify',
      description: 'Emit a notification message when PR changes',
      requires: ['gh'],
      args: {
        repo: { type: 'string', required: true },
        pr: { type: 'number', required: true },
        key: { type: 'string' },
      },
    });

  return workflow;
}

// Attach metadata
prMonitorNotify.meta = {
  name: 'github.pr.monitor.notify',
  description: 'Emit a notification message when PR changes',
  requires: ['gh'],
  args: {
    repo: { type: 'string', required: true },
    pr: { type: 'number', required: true },
    key: { type: 'string' },
  },
};
```

## File: `src/recipes/github/stages/pr-view.ts`
```typescript
/**
 * GitHub PR View Stage - Fetch PR details via gh CLI
 *
 * @example
 * import { Lobster } from 'lobster-sdk';
 * import { ghPrView } from 'lobster/recipes/github';
 *
 * new Lobster()
 *   .pipe(ghPrView({ repo: 'owner/repo', pr: 123 }))
 *   .pipe(pr => console.log(pr.state));
 */

import { spawn } from 'node:child_process';

/**
 * Run gh command
 * @param {string[]} argv
 * @param {Object} options
 * @returns {Promise<{stdout: string, stderr: string}>}
 */
function runGh(argv, { env, cwd }) {
  return new Promise<any>((resolve, reject) => {
    const child = spawn('gh', argv, {
      env,
      cwd,
      stdio: ['ignore', 'pipe', 'pipe'],
    });

    let stdout = '';
    let stderr = '';

    child.stdout.setEncoding('utf8');
    child.stderr.setEncoding('utf8');

    child.stdout.on('data', (d) => { stdout += d; });
    child.stderr.on('data', (d) => { stderr += d; });

    child.on('error', (err: any) => {
      if (err?.code === 'ENOENT') {
        reject(new Error('gh not found on PATH (install GitHub CLI)'));
        return;
      }
      reject(err);
    });

    child.on('close', (code) => {
      if (code === 0) {
        resolve({ stdout, stderr });
      } else {
        reject(new Error(`gh failed (${code}): ${stderr.trim() || stdout.trim()}`));
      }
    });
  });
}

/**
 * Create a GitHub PR view stage
 *
 * @param {Object} options
 * @param {string} options.repo - Repository in owner/repo format
 * @param {number} options.pr - PR number
 * @param {string[]} [options.fields] - Fields to fetch
 * @returns {Object} Stage object with run method
 */
export function ghPrView(options) {
  const { repo, pr } = options;
  const fields = options.fields ?? [
    'number', 'title', 'url', 'state', 'isDraft',
    'mergeable', 'reviewDecision', 'author',
    'baseRefName', 'headRefName', 'updatedAt',
  ];

  if (!repo) throw new Error('ghPrView requires repo');
  if (!pr) throw new Error('ghPrView requires pr');

  return {
    type: 'github.pr.view',
    repo,
    pr,

    async run({ input, ctx }) {
      // Drain input
      for await (const _item of input) {
        // no-op
      }

      const argv = [
        'pr', 'view',
        String(pr),
        '--repo', String(repo),
        '--json', fields.join(','),
      ];

      const { stdout } = (await runGh(argv, { env: ctx.env, cwd: process.cwd() })) as any;

      let parsed;
      try {
        parsed = JSON.parse(stdout.trim());
      } catch {
        throw new Error('gh returned non-JSON output');
      }

      return {
        output: (async function* () {
          yield parsed;
        })(),
      };
    },
  };
}
```

## File: `src/renderers/json.ts`
```typescript
export function createJsonRenderer(stdout) {
  return {
    json(items) {
      stdout.write(JSON.stringify(items, null, 2));
      stdout.write('\n');
    },
    lines(lines) {
      for (const line of lines) stdout.write(String(line) + '\n');
    },
  };
}
```

## File: `src/sdk/Lobster.ts`
```typescript
import { runPipelineInternal } from './runtime.js';
import { encodeToken, decodeToken } from './token.js';

/**
 * @typedef {Object} LobsterResult
 * @property {boolean} ok - Whether the workflow completed successfully
 * @property {'ok' | 'needs_approval' | 'cancelled' | 'error'} status - Workflow status
 * @property {any[]} output - Output items from the workflow
 * @property {Object|null} requiresApproval - Approval request if halted
 * @property {string} [requiresApproval.prompt] - Approval prompt
 * @property {any[]} [requiresApproval.items] - Items pending approval
 * @property {string} [requiresApproval.resumeToken] - Token to resume workflow
 * @property {Object} [error] - Error details if failed
 */

/**
 * @typedef {Object} LobsterOptions
 * @property {Object} [env] - Environment variables
 * @property {string} [stateDir] - State directory override
 */

/**
 * Lobster - Fluent workflow builder for AI agents
 *
 * @example
 * const workflow = new Lobster()
 *   .pipe(exec('gh pr view 123 --repo owner/repo --json title,url'))
 *   .pipe(approve({ prompt: 'Continue?' }))
 *   .run();
 */
export class Lobster {
  /** @type {Array<Function|Object>} */
  #stages = [];

  /** @type {any} */
  #options: any = {} as any;

  /** @type {Object|null} */
  #meta = null;

  /**
   * Create a new Lobster workflow builder
   * @param {LobsterOptions} [options]
   */
  constructor(options: any = {}) { 
    this.#options = {
      env: options.env ?? process.env,
      stateDir: options.stateDir,
    };
  }

  /**
   * Add a stage to the pipeline
   *
   * Stages can be:
   * - A function: (items: any[]) => any[] | AsyncIterable
   * - An async generator function: async function* (input) { ... }
   * - A stage object with { run: Function }
   * - A primitive from lobster-sdk (approve, exec, etc.)
   *
   * @param {Function|Object} stage - Stage to add
   * @returns {Lobster} - Returns this for chaining
   *
   * @example
   * new Lobster()
   *   .pipe(exec('gh pr view 123 --repo owner/repo --json title,url'))
   *   .pipe(items => items)
   *   .pipe(approve({ prompt: 'Proceed?' }))
   */
  pipe(stage) {
    if (typeof stage !== 'function' && typeof stage?.run !== 'function') {
      throw new Error('Stage must be a function or have a run() method');
    }
    this.#stages.push(stage);
    return this;
  }

  /**
   * Set metadata for this workflow (for recipe discovery)
   * @param {Object} meta
   * @param {string} meta.name - Workflow name
   * @param {string} meta.description - Description
   * @param {string[]} [meta.requires] - Required CLI tools
   * @param {Object} [meta.args] - Argument schema
   * @returns {Lobster}
   */
  meta(meta) {
    this.#meta = meta;
    return this;
  }

  /**
   * Get workflow metadata
   * @returns {Object|null}
   */
  getMeta() {
    return this.#meta;
  }

  /**
   * Execute the workflow
   * @param {any[]} [initialInput] - Optional initial input items
   * @returns {Promise<LobsterResult>}
   */
  async run(initialInput = []) {
    const ctx = {
      env: this.#options.env,
      stateDir: this.#options.stateDir,
      mode: 'sdk',
    };

    try {
      const result = await runPipelineInternal({
        stages: this.#stages,
        ctx,
        input: initialInput,
      });

      // Check for approval halt
      if (result.halted && result.items.length === 1 && result.items[0]?.type === 'approval_request') {
        const approval = result.items[0];
        const resumeToken = encodeToken({
          protocolVersion: 1,
          v: 1,
          stageIndex: result.haltedAt?.index ?? -1,
          resumeAtIndex: (result.haltedAt?.index ?? -1) + 1,
          items: approval.items,
          prompt: approval.prompt,
          // Note: We can't serialize the stages themselves, so resume requires
          // the caller to maintain the workflow reference
        });

        return {
          ok: true,
          status: 'needs_approval',
          output: [],
          requiresApproval: {
            prompt: approval.prompt,
            items: approval.items,
            resumeToken,
          },
        };
      }

      return {
        ok: true,
        status: 'ok',
        output: result.items,
        requiresApproval: null,
      };
    } catch (err) {
      return {
        ok: false,
        status: 'error',
        output: [],
        requiresApproval: null,
        error: {
          type: 'runtime_error',
          message: err?.message ?? String(err),
        },
      };
    }
  }

  /**
   * Resume a halted workflow after approval
   * @param {string} token - Resume token from previous run
   * @param {Object} options
   * @param {boolean} options.approved - Whether the approval was granted
   * @returns {Promise<LobsterResult>}
   */
  async resume(token, { approved }) {
    if (!approved) {
      return {
        ok: true,
        status: 'cancelled',
        output: [],
        requiresApproval: null,
      };
    }

    const payload = decodeToken(token);
    const resumeIndex = payload.resumeAtIndex ?? 0;
    const resumeItems = payload.items ?? [];

    // Get remaining stages
    const remainingStages = this.#stages.slice(resumeIndex);

    const ctx = {
      env: this.#options.env,
      stateDir: this.#options.stateDir,
      mode: 'sdk',
    };

    try {
      const result = await runPipelineInternal({
        stages: remainingStages,
        ctx,
        input: resumeItems,
      });

      // Check for another approval halt
      if (result.halted && result.items.length === 1 && result.items[0]?.type === 'approval_request') {
        const approval = result.items[0];
        const resumeToken = encodeToken({
          protocolVersion: 1,
          v: 1,
          stageIndex: resumeIndex + (result.haltedAt?.index ?? 0),
          resumeAtIndex: resumeIndex + (result.haltedAt?.index ?? 0) + 1,
          items: approval.items,
          prompt: approval.prompt,
        });

        return {
          ok: true,
          status: 'needs_approval',
          output: [],
          requiresApproval: {
            prompt: approval.prompt,
            items: approval.items,
            resumeToken,
          },
        };
      }

      return {
        ok: true,
        status: 'ok',
        output: result.items,
        requiresApproval: null,
      };
    } catch (err) {
      return {
        ok: false,
        status: 'error',
        output: [],
        requiresApproval: null,
        error: {
          type: 'runtime_error',
          message: err?.message ?? String(err),
        },
      };
    }
  }

  /**
   * Clone this workflow (for creating variants)
   * @returns {Lobster}
   */
  clone() {
    const cloned = new Lobster(this.#options);
    cloned.#stages = [...this.#stages];
    cloned.#meta = this.#meta ? { ...this.#meta } : null;
    return cloned;
  }
}
```

## File: `src/sdk/index.ts`
```typescript
/**
 * Lobster SDK - Workflow runtime for AI agents
 *
 * @example
 * import { Lobster, approve, exec } from 'lobster-sdk';
 *
 * const workflow = new Lobster()
 *   .pipe(exec('gh pr view 123 --repo owner/repo --json title,url'))
 *   .pipe(items => items.filter(e => e.unread))
 *   .pipe(approve({ prompt: 'Process these emails?' }))
 *   .pipe(async function* (items) {
 *     for (const item of items) {
 *       yield { ...item, processed: true };
 *     }
 *   });
 *
 * const result = await workflow.run();
 */

export { Lobster } from './Lobster.js';
export { approve } from './primitives/approve.js';
export { exec } from './primitives/exec.js';
export { stateGet, stateSet, state } from './primitives/state.js';
export { diffLast } from './primitives/diff.js';
export { runPipeline } from './runtime.js';
```

## File: `src/sdk/runtime.ts`
```typescript
/**
 * SDK Runtime - Executes Lobster pipelines
 *
 * This is adapted from the CLI runtime but designed for SDK use.
 */

/**
 * @typedef {Object} StageResult
 * @property {AsyncIterable|any[]} [output] - Output items
 * @property {boolean} [halt] - Whether to halt the pipeline
 * @property {boolean} [rendered] - Whether output was rendered
 */

/**
 * @typedef {Object} PipelineResult
 * @property {any[]} items - Collected output items
 * @property {boolean} halted - Whether pipeline halted
 * @property {Object|null} haltedAt - Stage where halt occurred
 */

/**
 * Convert various inputs to an async iterable
 * @param {any} input
 * @returns {AsyncIterable}
 */
async function* toAsyncIterable(input) {
  if (input === null || input === undefined) {
    return;
  }

  if (Array.isArray(input)) {
    for (const item of input) {
      yield item;
    }
    return;
  }

  if (typeof input[Symbol.asyncIterator] === 'function') {
    yield* input;
    return;
  }

  if (typeof input[Symbol.iterator] === 'function') {
    for (const item of input) {
      yield item;
    }
    return;
  }

  // Single item
  yield input;
}

/**
 * Collect async iterable to array
 * @param {AsyncIterable} iterable
 * @returns {Promise<any[]>}
 */
async function collectItems(iterable) {
  const items = [];
  for await (const item of iterable) {
    items.push(item);
  }
  return items;
}

/**
 * Run a pipeline of stages
 *
 * @param {Object} options
 * @param {Array<Function|Object>} options.stages - Pipeline stages
 * @param {Object} options.ctx - Execution context
 * @param {any[]} [options.input] - Initial input items
 * @returns {Promise<PipelineResult>}
 */
export async function runPipelineInternal({ stages, ctx, input = [] }) {
  let stream = toAsyncIterable(input);
  let halted = false;
  let haltedAt = null;

  for (let idx = 0; idx < stages.length; idx++) {
    const stage = stages[idx];

    let result;

    if (typeof stage === 'function') {
      // Check if it's a generator function
      const isGenerator = stage.constructor?.name === 'AsyncGeneratorFunction' ||
                          stage.constructor?.name === 'GeneratorFunction';

      if (isGenerator) {
        // Generator function - pass the stream directly
        result = { output: stage(stream, ctx) };
      } else {
        // Regular function - collect items first, then call
        const items = await collectItems(stream);
        const output = await stage(items, ctx);
        result = { output: toAsyncIterable(output) };
      }
    } else if (typeof stage?.run === 'function') {
      // Stage object with run method (primitives)
      result = await stage.run({ input: stream, ctx });
    } else {
      throw new Error(`Invalid stage at index ${idx}: must be a function or have run() method`);
    }

    // Handle halt
    if (result?.halt) {
      halted = true;
      haltedAt = { index: idx, stage };
      stream = result.output ?? toAsyncIterable([]);
      break;
    }

    stream = result?.output ?? toAsyncIterable([]);
  }

  // Collect final output
  const items = await collectItems(stream);

  return { items, halted, haltedAt };
}

/**
 * Re-export for compatibility with CLI runtime
 */
export async function runPipeline({ pipeline, registry, stdin, stdout, stderr, env, mode = 'human', input }) {
  // This wraps the CLI-style pipeline execution
  // Convert pipeline stages to functions using registry

  const stages = pipeline.map((stage) => {
    const command = registry.get(stage.name);
    if (!command) {
      throw new Error(`Unknown command: ${stage.name}`);
    }

    return {
      run: async ({ input, ctx }) => {
        return command.run({ input, args: stage.args, ctx });
      },
    };
  });

  const ctx = {
    stdin,
    stdout,
    stderr,
    env,
    mode,
  };

  return runPipelineInternal({
    stages,
    ctx,
    input: input ? await collectItems(input) : [],
  });
}
```

## File: `src/sdk/token.ts`
```typescript
/**
 * Token encoding/decoding for SDK resume functionality
 *
 * Re-exports from the main token module for consistency
 */

import { encodeToken as mainEncode, decodeToken as mainDecode } from '../token.js';

export const encodeToken = mainEncode;
export const decodeToken = mainDecode;
```

## File: `src/sdk/primitives/approve.ts`
```typescript
/**
 * Approve primitive - Creates a hard halt point requiring human approval
 *
 * @example
 * import { Lobster, approve } from 'lobster-sdk';
 *
 * new Lobster()
 *   .pipe(fetchEmails())
 *   .pipe(approve({ prompt: 'Send these replies?' }))
 *   .pipe(sendReplies())
 */

/**
 * Create an approval stage
 *
 * @param {Object} [options]
 * @param {string} [options.prompt='Approve?'] - Prompt to show user
 * @param {boolean} [options.preview=true] - Include items in approval request
 * @returns {Object} Stage object with run method
 */
export function approve(options: any = {}) {
  const prompt = options.prompt ?? 'Approve?';
  const preview = options.preview !== false;

  return {
    type: 'approve',
    prompt,

    async run({ input, ctx: _ctx }) {
      // Collect all items
      const items = [];
      for await (const item of input) {
        items.push(item);
      }

      // In SDK mode, always emit approval request and halt
      return {
        halt: true,
        output: (async function* () {
          yield {
            type: 'approval_request',
            prompt,
            items: preview ? items : [],
            itemCount: items.length,
          };
        })(),
      };
    },
  };
}
```

## File: `src/sdk/primitives/diff.ts`
```typescript
/**
 * Diff primitive - Compare current value against last stored value
 *
 * @example
 * import { Lobster, diffLast } from 'lobster-sdk';
 *
 * new Lobster()
 *   .pipe(fetchPRStatus())
 *   .pipe(diffLast('pr-123'))
 *   .pipe(result => {
 *     if (result.changed) {
 *       console.log('PR changed!', result.changes);
 *     }
 *   });
 */

import { promises as fsp } from 'node:fs';
import os from 'node:os';
import path from 'node:path';

/**
 * Get the state directory
 * @param {Object} ctx
 * @returns {string}
 */
function getStateDir(ctx) {
  return (
    ctx?.stateDir ||
    (ctx?.env?.LOBSTER_STATE_DIR && String(ctx.env.LOBSTER_STATE_DIR).trim()) ||
    path.join(os.homedir(), '.lobster', 'state')
  );
}

/**
 * Convert a key to a safe file path
 * @param {string} stateDir
 * @param {string} key
 * @returns {string}
 */
function keyToPath(stateDir, key) {
  const safe = String(key)
    .toLowerCase()
    .replace(/[^a-z0-9._-]+/g, '_')
    .replace(/_+/g, '_')
    .replace(/^_+|_+$/g, '');
  if (!safe) throw new Error('state key is empty/invalid');
  return path.join(stateDir, `${safe}.json`);
}

/**
 * Stable JSON stringify for comparison
 * @param {any} value
 * @returns {string}
 */
function stableStringify(value) {
  return JSON.stringify(value, (_k, v) => {
    if (v && typeof v === 'object' && !Array.isArray(v)) {
      return Object.fromEntries(Object.keys(v).sort().map((k) => [k, v[k]]));
    }
    return v;
  });
}

/**
 * Create a diff.last stage
 *
 * Compares the input against the last stored value for the given key,
 * stores the new value, and outputs a diff result.
 *
 * @param {string} key - State key to compare against
 * @param {Object} [options]
 * @param {boolean} [options.changesOnly=false] - If true, suppress output when unchanged
 * @returns {Object} Stage object with run method
 */
export function diffLast(key, options: any = {}) {
  if (!key) throw new Error('diffLast requires a key');

  const changesOnly = options.changesOnly === true;

  return {
    type: 'diff.last',
    key,

    async run({ input, ctx }) {
      // Collect all input items
      const items = [];
      for await (const item of input) {
        items.push(item);
      }

      const value = items.length === 1 ? items[0] : items;

      const stateDir = getStateDir(ctx);
      const filePath = keyToPath(stateDir, key);

      // Read previous value
      let before = null;
      try {
        const text = await fsp.readFile(filePath, 'utf8');
        before = JSON.parse(text);
      } catch (err) {
        if (err?.code !== 'ENOENT') {
          throw err;
        }
      }

      // Compare
      const changed = stableStringify(before) !== stableStringify(value);

      // Store new value
      await fsp.mkdir(stateDir, { recursive: true });
      await fsp.writeFile(filePath, JSON.stringify(value, null, 2) + '\n', 'utf8');

      // Build result
      const result = {
        kind: 'diff.last',
        key,
        changed,
        before,
        after: value,
      };

      // If changesOnly and no change, output suppressed marker
      if (changesOnly && !changed) {
        return {
          output: (async function* () {
            yield { kind: 'diff.last', key, changed: false, suppressed: true };
          })(),
        };
      }

      return {
        output: (async function* () {
          yield result;
        })(),
      };
    },
  };
}

/**
 * Diff and store directly (not as a pipeline stage)
 * @param {string} key
 * @param {any} value
 * @param {Object} [ctx]
 * @returns {Promise<{before: any, after: any, changed: boolean}>}
 */
export async function diffAndStoreValue(key, value, ctx = {}) {
  const stateDir = getStateDir(ctx);
  const filePath = keyToPath(stateDir, key);

  // Read previous value
  let before = null;
  try {
    const text = await fsp.readFile(filePath, 'utf8');
    before = JSON.parse(text);
  } catch (err) {
    if (err?.code !== 'ENOENT') {
      throw err;
    }
  }

  // Compare
  const changed = stableStringify(before) !== stableStringify(value);

  // Store new value
  await fsp.mkdir(stateDir, { recursive: true });
  await fsp.writeFile(filePath, JSON.stringify(value, null, 2) + '\n', 'utf8');

  return { before, after: value, changed };
}
```

## File: `src/sdk/primitives/exec.ts`
```typescript
/**
 * Exec primitive - Execute shell commands and return JSON output
 *
 * @example
 * import { Lobster, exec } from 'lobster-sdk';
 *
 * new Lobster()
 *   .pipe(exec('gh pr view 123 --repo owner/repo --json title,url'))
 *   .pipe(items => items.filter(e => e.unread))
 */

import { spawn } from 'node:child_process';
import { resolveInlineShellCommand } from '../../shell.js';

/**
 * Run a process and capture output
 * @param {string} command
 * @param {string[]} argv
 * @param {Object} options
 * @returns {Promise<{stdout: string, stderr: string}>}
 */
function runProcess(command, argv, { env, cwd }) {
  return new Promise<any>((resolve, reject) => {
    const child = spawn(command, argv, {
      env,
      cwd,
      stdio: ['ignore', 'pipe', 'pipe'],
      shell: false,
    });

    let stdout = '';
    let stderr = '';

    child.stdout.setEncoding('utf8');
    child.stderr.setEncoding('utf8');

    child.stdout.on('data', (d) => { stdout += d; });
    child.stderr.on('data', (d) => { stderr += d; });

    child.on('error', (err) => {
      reject(new Error(`Failed to execute ${command}: ${err.message}`));
    });

    child.on('close', (code) => {
      if (code === 0) {
        resolve({ stdout, stderr });
      } else {
        reject(new Error(`${command} exited with code ${code}: ${stderr.trim() || stdout.trim()}`));
      }
    });
  });
}

/**
 * Parse a shell command string into command and arguments
 * Simple parsing - for complex cases, use options.shell
 * @param {string} cmdString
 * @returns {{command: string, args: string[]}}
 */
function parseCommand(cmdString) {
  const tokens = [];
  let current = '';
  let quote = null;

  for (let i = 0; i < cmdString.length; i++) {
    const ch = cmdString[i];

    if (quote) {
      if (ch === '\\' && cmdString[i + 1]) {
        current += cmdString[i + 1];
        i++;
        continue;
      }
      if (ch === quote) {
        quote = null;
        continue;
      }
      current += ch;
      continue;
    }

    if (ch === '"' || ch === "'") {
      quote = ch;
      continue;
    }

    if (ch === ' ' || ch === '\t') {
      if (current.length > 0) {
        tokens.push(current);
        current = '';
      }
      continue;
    }

    current += ch;
  }

  if (current.length > 0) {
    tokens.push(current);
  }

  const [command, ...args] = tokens;
  return { command, args };
}

/**
 * Create an exec stage
 *
 * @param {string} cmdString - Command to execute
 * @param {Object} [options]
 * @param {boolean} [options.json=true] - Parse output as JSON
 * @param {boolean} [options.shell=false] - Use shell execution
 * @param {string} [options.cwd] - Working directory
 * @returns {Object} Stage object with run method
 */
export function exec(cmdString, options: any = {}) {
  const parseJson = options.json !== false;
  const useShell = options.shell === true;
  const cwd = options.cwd ?? process.cwd();

  return {
    type: 'exec',
    command: cmdString,

    async run({ input, ctx }) {
      // Drain input (exec doesn't use input stream)
      for await (const _item of input) {
        // no-op
      }

      const env = ctx.env ?? process.env;

      let stdout;

      if (useShell) {
        // Shell execution
        const shell = resolveInlineShellCommand({ command: cmdString, env });
        const result = await runProcess(shell.command, shell.argv, { env, cwd });
        stdout = result.stdout;
      } else {
        // Direct execution
        const { command, args } = parseCommand(cmdString);
        const result = await runProcess(command, args, { env, cwd });
        stdout = result.stdout;
      }

      // Parse output
      let output;
      if (parseJson) {
        try {
          output = JSON.parse(stdout.trim() || '[]');
        } catch {
          throw new Error(`exec output is not valid JSON: ${stdout.slice(0, 100)}`);
        }
      } else {
        output = stdout;
      }

      // Normalize to array
      const items = Array.isArray(output) ? output : [output];

      return {
        output: (async function* () {
          for (const item of items) {
            yield item;
          }
        })(),
      };
    },
  };
}

/**
 * Create an exec stage that runs in shell mode
 * Convenience wrapper for exec(cmd, { shell: true })
 *
 * @param {string} cmdString
 * @param {Object} [options]
 * @returns {Object}
 */
export function shell(cmdString, options = {}) {
  return exec(cmdString, { ...options, shell: true });
}
```

## File: `src/sdk/primitives/state.ts`
```typescript
/**
 * State primitives - Persistent state management
 *
 * @example
 * import { Lobster, stateGet, stateSet } from 'lobster-sdk';
 *
 * // Read state
 * new Lobster()
 *   .pipe(stateGet('my-key'))
 *   .pipe(value => console.log(value));
 *
 * // Write state
 * new Lobster()
 *   .pipe(() => ({ count: 42 }))
 *   .pipe(stateSet('my-key'));
 */

import { promises as fsp } from 'node:fs';
import os from 'node:os';
import path from 'node:path';

/**
 * Get the state directory
 * @param {Object} ctx
 * @returns {string}
 */
function getStateDir(ctx) {
  return (
    ctx?.stateDir ||
    (ctx?.env?.LOBSTER_STATE_DIR && String(ctx.env.LOBSTER_STATE_DIR).trim()) ||
    path.join(os.homedir(), '.lobster', 'state')
  );
}

/**
 * Convert a key to a safe file path
 * @param {string} stateDir
 * @param {string} key
 * @returns {string}
 */
function keyToPath(stateDir, key) {
  const safe = String(key)
    .toLowerCase()
    .replace(/[^a-z0-9._-]+/g, '_')
    .replace(/_+/g, '_')
    .replace(/^_+|_+$/g, '');
  if (!safe) throw new Error('state key is empty/invalid');
  return path.join(stateDir, `${safe}.json`);
}

/**
 * Create a state.get stage
 *
 * @param {string} key - State key to read
 * @returns {Object} Stage object with run method
 */
export function stateGet(key) {
  if (!key) throw new Error('stateGet requires a key');

  return {
    type: 'state.get',
    key,

    async run({ input, ctx }) {
      // Drain input
      for await (const _item of input) {
        // no-op
      }

      const stateDir = getStateDir(ctx);
      const filePath = keyToPath(stateDir, key);

      let value = null;
      try {
        const text = await fsp.readFile(filePath, 'utf8');
        value = JSON.parse(text);
      } catch (err) {
        if (err?.code !== 'ENOENT') {
          throw err;
        }
        // File doesn't exist, return null
      }

      return {
        output: (async function* () {
          yield value;
        })(),
      };
    },
  };
}

/**
 * Create a state.set stage
 *
 * @param {string} key - State key to write
 * @returns {Object} Stage object with run method
 */
export function stateSet(key) {
  if (!key) throw new Error('stateSet requires a key');

  return {
    type: 'state.set',
    key,

    async run({ input, ctx }) {
      // Collect all input items
      const items = [];
      for await (const item of input) {
        items.push(item);
      }

      const value = items.length === 1 ? items[0] : items;

      const stateDir = getStateDir(ctx);
      const filePath = keyToPath(stateDir, key);

      await fsp.mkdir(stateDir, { recursive: true });
      await fsp.writeFile(filePath, JSON.stringify(value, null, 2) + '\n', 'utf8');

      // Pass through the value
      return {
        output: (async function* () {
          yield value;
        })(),
      };
    },
  };
}

/**
 * State namespace - provides get/set methods
 *
 * @example
 * import { state } from 'lobster-sdk';
 *
 * new Lobster()
 *   .pipe(state.get('my-key'))
 *   .pipe(state.set('my-key'));
 */
export const state = {
  get: stateGet,
  set: stateSet,
};

/**
 * Read state directly (not as a pipeline stage)
 * @param {string} key
 * @param {Object} [ctx]
 * @returns {Promise<any>}
 */
export async function readState(key, ctx = {}) {
  const stateDir = getStateDir(ctx);
  const filePath = keyToPath(stateDir, key);

  try {
    const text = await fsp.readFile(filePath, 'utf8');
    return JSON.parse(text);
  } catch (err) {
    if (err?.code === 'ENOENT') return null;
    throw err;
  }
}

/**
 * Write state directly (not as a pipeline stage)
 * @param {string} key
 * @param {any} value
 * @param {Object} [ctx]
 * @returns {Promise<void>}
 */
export async function writeState(key, value, ctx = {}) {
  const stateDir = getStateDir(ctx);
  const filePath = keyToPath(stateDir, key);

  await fsp.mkdir(stateDir, { recursive: true });
  await fsp.writeFile(filePath, JSON.stringify(value, null, 2) + '\n', 'utf8');
}
```

## File: `src/state/store.ts`
```typescript
import os from 'node:os';
import path from 'node:path';
import { promises as fsp } from 'node:fs';

export function defaultStateDir(env) {
  return (
    (env?.LOBSTER_STATE_DIR && String(env.LOBSTER_STATE_DIR).trim()) ||
    path.join(os.homedir(), '.lobster', 'state')
  );
}

export function keyToPath(stateDir, key) {
  const safe = String(key)
    .toLowerCase()
    .replace(/[^a-z0-9._-]+/g, '_')
    .replace(/_+/g, '_')
    .replace(/^_+|_+$/g, '');
  if (!safe) throw new Error('state key is empty/invalid');
  return path.join(stateDir, `${safe}.json`);
}

export function stableStringify(value) {
  return JSON.stringify(value, (_k, v) => {
    if (v && typeof v === 'object' && !Array.isArray(v)) {
      return Object.fromEntries(Object.keys(v).sort().map((k) => [k, v[k]]));
    }
    return v;
  });
}

export async function readStateJson({ env, key }) {
  const stateDir = defaultStateDir(env);
  const filePath = keyToPath(stateDir, key);

  try {
    const text = await fsp.readFile(filePath, 'utf8');
    return JSON.parse(text);
  } catch (err) {
    if (err?.code === 'ENOENT') return null;
    throw err;
  }
}

export async function writeStateJson({ env, key, value }) {
  const stateDir = defaultStateDir(env);
  const filePath = keyToPath(stateDir, key);

  await fsp.mkdir(stateDir, { recursive: true });
  await fsp.writeFile(filePath, JSON.stringify(value, null, 2) + '\n', 'utf8');
}

export async function deleteStateJson({ env, key }) {
  const stateDir = defaultStateDir(env);
  const filePath = keyToPath(stateDir, key);
  try {
    await fsp.unlink(filePath);
  } catch (err) {
    if (err?.code === 'ENOENT') return;
    throw err;
  }
}

export async function diffAndStore({ env, key, value }) {
  const before = await readStateJson({ env, key });
  const changed = stableStringify(before) !== stableStringify(value);
  await writeStateJson({ env, key, value });
  return { before, after: value, changed };
}
```

## File: `src/workflows/file.ts`
```typescript
import { promises as fsp } from 'node:fs';
import path from 'node:path';
import { parse as parseYaml } from 'yaml';

import { randomUUID } from 'node:crypto';
import { PassThrough } from 'node:stream';

import { parsePipeline } from '../parser.js';
import { runPipeline } from '../runtime.js';
import { encodeToken } from '../token.js';
import { deleteStateJson, readStateJson, writeStateJson } from '../state/store.js';
import { readLineFromStream } from '../read_line.js';
import { resolveInlineShellCommand } from '../shell.js';

export type WorkflowFile = {
  name?: string;
  description?: string;
  args?: Record<string, { default?: unknown; description?: string }>;
  env?: Record<string, string>;
  cwd?: string;
  steps: WorkflowStep[];
};

export type WorkflowStep = {
  id: string;
  command?: string;
  run?: string;
  pipeline?: string;
  env?: Record<string, string>;
  cwd?: string;
  stdin?: unknown;
  approval?: WorkflowApproval;
  condition?: unknown;
  when?: unknown;
};

export type WorkflowApproval =
  | boolean
  | 'required'
  | string
  | {
    prompt?: string;
    items?: unknown[];
    preview?: string;
  };

export type WorkflowStepResult = {
  id: string;
  stdout?: string;
  json?: unknown;
  approved?: boolean;
  skipped?: boolean;
};

export type WorkflowRunResult = {
  status: 'ok' | 'needs_approval' | 'cancelled';
  output: unknown[];
  requiresApproval?: {
    type: 'approval_request';
    prompt: string;
    items: unknown[];
    preview?: string;
    resumeToken?: string;
  };
};

type RunContext = {
  stdin: NodeJS.ReadableStream;
  stdout: NodeJS.WritableStream;
  stderr: NodeJS.WritableStream;
  env: Record<string, string | undefined>;
  mode: 'human' | 'tool' | 'sdk';
  cwd?: string;
  signal?: AbortSignal;
  registry?: {
    get: (name: string) => any;
  };
  llmAdapters?: Record<string, any>;
};

export type WorkflowResumePayload = {
  protocolVersion: 1;
  v: 1;
  kind: 'workflow-file';
  stateKey?: string;
  filePath?: string;
  resumeAtIndex?: number;
  steps?: Record<string, WorkflowStepResult>;
  args?: Record<string, unknown>;
  approvalStepId?: string;
};

type WorkflowResumeState = {
  filePath: string;
  resumeAtIndex: number;
  steps: Record<string, WorkflowStepResult>;
  args: Record<string, unknown>;
  approvalStepId?: string;
  createdAt: string;
};

export async function loadWorkflowFile(filePath: string): Promise<WorkflowFile> {
  const text = await fsp.readFile(filePath, 'utf8');
  const ext = path.extname(filePath).toLowerCase();
  const parsed = ext === '.json' ? JSON.parse(text) : parseYaml(text);

  if (!parsed || typeof parsed !== 'object') {
    throw new Error('Workflow file must be a JSON/YAML object');
  }

  const steps = (parsed as WorkflowFile).steps;
  if (!Array.isArray(steps) || steps.length === 0) {
    throw new Error('Workflow file requires a non-empty steps array');
  }

  const seen = new Set<string>();
  for (const step of steps) {
    if (!step || typeof step !== 'object') {
      throw new Error('Workflow step must be an object');
    }
    if (!step.id || typeof step.id !== 'string') {
      throw new Error('Workflow step requires an id');
    }
    const shellCommand = typeof step.run === 'string' ? step.run : step.command;
    const pipeline = typeof step.pipeline === 'string' ? step.pipeline : undefined;
    const executionCount = Number(Boolean(shellCommand)) + Number(Boolean(pipeline));
    if (executionCount === 0 && !isApprovalStep(step.approval)) {
      throw new Error(`Workflow step ${step.id} requires run, command, pipeline, or approval`);
    }
    if (executionCount > 1) {
      throw new Error(`Workflow step ${step.id} can only define one of run, command, or pipeline`);
    }
    if (step.run !== undefined && typeof step.run !== 'string') {
      throw new Error(`Workflow step ${step.id} run must be a string`);
    }
    if (step.command !== undefined && typeof step.command !== 'string') {
      throw new Error(`Workflow step ${step.id} command must be a string`);
    }
    if (step.pipeline !== undefined && typeof step.pipeline !== 'string') {
      throw new Error(`Workflow step ${step.id} pipeline must be a string`);
    }
    if (seen.has(step.id)) {
      throw new Error(`Duplicate workflow step id: ${step.id}`);
    }
    seen.add(step.id);
  }

  return parsed as WorkflowFile;
}

export function resolveWorkflowArgs(
  argDefs: WorkflowFile['args'],
  provided: Record<string, unknown> | undefined,
) {
  const resolved: Record<string, unknown> = {};
  if (argDefs) {
    for (const [key, def] of Object.entries(argDefs)) {
      if (def && typeof def === 'object' && 'default' in def) {
        resolved[key] = def.default;
      }
    }
  }
  if (provided) {
    for (const [key, value] of Object.entries(provided)) {
      resolved[key] = value;
    }
  }
  return resolved;
}

export async function runWorkflowFile({
  filePath,
  args,
  ctx,
  resume,
  approved,
}: {
  filePath?: string;
  args?: Record<string, unknown>;
  ctx: RunContext;
  resume?: WorkflowResumePayload;
  approved?: boolean;
}): Promise<WorkflowRunResult> {
  const consumedResumeStateKey = resume?.stateKey && typeof resume.stateKey === 'string'
    ? resume.stateKey
    : null;
  const resumeState = resume?.stateKey
    ? await loadWorkflowResumeState(ctx.env, resume.stateKey)
    : resume ?? null;
  const resolvedFilePath = filePath ?? resumeState?.filePath;
  if (!resolvedFilePath) {
    throw new Error('Workflow file path required');
  }
  const workflow = await loadWorkflowFile(resolvedFilePath);
  const resolvedArgs = resolveWorkflowArgs(workflow.args, args ?? resumeState?.args);
  const steps = workflow.steps;
  const results: Record<string, WorkflowStepResult> = resumeState?.steps
    ? cloneResults(resumeState.steps)
    : {};
  const startIndex = resumeState?.resumeAtIndex ?? 0;

  if (resumeState?.approvalStepId && approved === false) {
    if (consumedResumeStateKey) {
      await deleteStateJson({ env: ctx.env, key: consumedResumeStateKey });
    }
    return { status: 'cancelled', output: [] };
  }

  if (resumeState?.approvalStepId && typeof approved === 'boolean') {
    const previous = results[resumeState.approvalStepId] ?? { id: resumeState.approvalStepId };
    previous.approved = approved;
    results[resumeState.approvalStepId] = previous;
  }

  let lastStepId: string | null = findLastCompletedStepId(steps, results);

  for (let idx = startIndex; idx < steps.length; idx++) {
    const step = steps[idx];

    if (!evaluateCondition(step.when ?? step.condition, results)) {
      results[step.id] = { id: step.id, skipped: true };
      continue;
    }

    const env = mergeEnv(ctx.env, workflow.env, step.env, resolvedArgs, results);
    const cwd = resolveCwd(step.cwd ?? workflow.cwd, resolvedArgs) ?? ctx.cwd;
    const execution = getStepExecution(step);

    let result: WorkflowStepResult;
    if (execution.kind === 'shell') {
      const command = resolveTemplate(execution.value, resolvedArgs, results);
      const stdinValue = resolveShellStdin(step.stdin, resolvedArgs, results);
      const { stdout } = await runShellCommand({ command, stdin: stdinValue, env, cwd, signal: ctx.signal });
      result = { id: step.id, stdout, json: parseJson(stdout) };
    } else if (execution.kind === 'pipeline') {
      if (!ctx.registry) {
        throw new Error(`Workflow step ${step.id} requires a command registry for pipeline execution`);
      }
      const pipelineText = resolveTemplate(execution.value, resolvedArgs, results);
      const inputValue = resolveInputValue(step.stdin, resolvedArgs, results);
      result = await runPipelineStep({
        stepId: step.id,
        pipelineText,
        inputValue,
        ctx,
        env,
        cwd,
      });
    } else {
      const inputValue = resolveInputValue(step.stdin, resolvedArgs, results);
      result = createSyntheticStepResult(step.id, inputValue);
    }

    results[step.id] = result;
    lastStepId = step.id;

    if (isApprovalStep(step.approval)) {
      const approval = extractApprovalRequest(step, results[step.id]);

      if (ctx.mode === 'tool' || !isInteractive(ctx.stdin)) {
        const stateKey = await saveWorkflowResumeState(ctx.env, {
          filePath: resolvedFilePath,
          resumeAtIndex: idx + 1,
          steps: results,
          args: resolvedArgs,
          approvalStepId: step.id,
          createdAt: new Date().toISOString(),
        });

        if (consumedResumeStateKey && consumedResumeStateKey !== stateKey) {
          await deleteStateJson({ env: ctx.env, key: consumedResumeStateKey });
        }

        const resumeToken = encodeToken({
          protocolVersion: 1,
          v: 1,
          kind: 'workflow-file',
          stateKey,
        } satisfies WorkflowResumePayload);

        return {
          status: 'needs_approval',
          output: [],
          requiresApproval: {
            ...approval,
            resumeToken,
          },
        };
      }

      ctx.stdout.write(`${approval.prompt} [y/N] `);
      const answer = await readLineFromStream(ctx.stdin, {
        timeoutMs: parseApprovalTimeoutMs(ctx.env),
      });
      if (!/^y(es)?$/i.test(String(answer).trim())) {
        throw new Error('Not approved');
      }
      results[step.id].approved = true;
    }
  }

  const output = lastStepId ? toOutputItems(results[lastStepId]) : [];
  if (consumedResumeStateKey) {
    await deleteStateJson({ env: ctx.env, key: consumedResumeStateKey });
  }
  return { status: 'ok', output };
}

export function decodeWorkflowResumePayload(payload: unknown): WorkflowResumePayload | null {
  if (!payload || typeof payload !== 'object') return null;
  const data = payload as Partial<WorkflowResumePayload>;
  if (data.kind !== 'workflow-file') return null;
  if (data.protocolVersion !== 1 || data.v !== 1) throw new Error('Unsupported token version');
  if (data.stateKey && typeof data.stateKey === 'string') {
    return data as WorkflowResumePayload;
  }
  if (!data.filePath || typeof data.filePath !== 'string') throw new Error('Invalid workflow token');
  if (typeof data.resumeAtIndex !== 'number') throw new Error('Invalid workflow token');
  if (!data.steps || typeof data.steps !== 'object') throw new Error('Invalid workflow token');
  if (!data.args || typeof data.args !== 'object') throw new Error('Invalid workflow token');
  return data as WorkflowResumePayload;
}

async function saveWorkflowResumeState(env: Record<string, string | undefined>, state: WorkflowResumeState) {
  const stateKey = `workflow_resume_${randomUUID()}`;
  await writeStateJson({ env, key: stateKey, value: state });
  return stateKey;
}

async function loadWorkflowResumeState(env: Record<string, string | undefined>, stateKey: string) {
  const stored = await readStateJson({ env, key: stateKey });
  if (!stored || typeof stored !== 'object') {
    throw new Error('Workflow resume state not found');
  }
  const data = stored as Partial<WorkflowResumeState>;
  if (!data.filePath || typeof data.filePath !== 'string') throw new Error('Invalid workflow resume state');
  if (typeof data.resumeAtIndex !== 'number') throw new Error('Invalid workflow resume state');
  if (!data.steps || typeof data.steps !== 'object') throw new Error('Invalid workflow resume state');
  if (!data.args || typeof data.args !== 'object') throw new Error('Invalid workflow resume state');
  return data as WorkflowResumeState;
}

function mergeEnv(
  base: Record<string, string | undefined>,
  workflowEnv: WorkflowFile['env'],
  stepEnv: WorkflowStep['env'],
  args: Record<string, unknown>,
  results: Record<string, WorkflowStepResult>,
) {
  const env = { ...base } as Record<string, string | undefined>;

  // Expose resolved args as env vars so shell commands can safely reference them
  // without embedding raw values into the command string.
  // Example: $LOBSTER_ARG_TEXT
  env.LOBSTER_ARGS_JSON = JSON.stringify(args ?? {});
  for (const [key, value] of Object.entries(args ?? {})) {
    const normalized = normalizeArgEnvKey(key);
    if (!normalized) continue;
    env[`LOBSTER_ARG_${normalized}`] = String(value);
  }

  const apply = (source?: Record<string, string>) => {
    if (!source) return;
    for (const [key, value] of Object.entries(source)) {
      if (typeof value === 'string') {
        env[key] = resolveTemplate(value, args, results);
      }
    }
  };

  // Allow explicit env blocks to override injected defaults.
  apply(workflowEnv);
  apply(stepEnv);
  return env;
}

function normalizeArgEnvKey(key: string): string | null {
  const trimmed = String(key ?? '').trim();
  if (!trimmed) return null;
  // Keep it predictable for shells: uppercase and [A-Z0-9_]
  const up = trimmed.toUpperCase();
  const normalized = up.replace(/[^A-Z0-9]+/g, '_').replace(/^_+|_+$/g, '');
  return normalized || null;
}

function resolveCwd(cwd: string | undefined, args: Record<string, unknown>) {
  if (!cwd) return undefined;
  return resolveArgsTemplate(cwd, args);
}

function resolveInputValue(
  stdin: unknown,
  args: Record<string, unknown>,
  results: Record<string, WorkflowStepResult>,
) {
  if (stdin === null || stdin === undefined) return null;
  if (typeof stdin === 'string') {
    const ref = parseStepRef(stdin.trim());
    if (ref) return getStepRefValue(ref, results, true);
    return resolveTemplate(stdin, args, results);
  }
  return stdin;
}

function resolveShellStdin(
  stdin: unknown,
  args: Record<string, unknown>,
  results: Record<string, WorkflowStepResult>,
) {
  const value = resolveInputValue(stdin, args, results);
  return encodeShellInput(value);
}

function resolveTemplate(
  input: string,
  args: Record<string, unknown>,
  results: Record<string, WorkflowStepResult>,
) {
  const withArgs = resolveArgsTemplate(input, args);
  return resolveStepRefs(withArgs, results);
}

function resolveArgsTemplate(input: string, args: Record<string, unknown>) {
  return input.replace(/\$\{([A-Za-z0-9_-]+)\}/g, (match, key) => {
    if (key in args) return String(args[key]);
    return match;
  });
}

function resolveStepRefs(input: string, results: Record<string, WorkflowStepResult>) {
  return input.replace(/\$([A-Za-z0-9_-]+)\.(stdout|json|approved)/g, (match, id, field) => {
    const step = results[id];
    if (!step) return match;
    if (field === 'stdout') return step.stdout ?? '';
    if (field === 'json') return step.json !== undefined ? JSON.stringify(step.json) : '';
    if (field === 'approved') return step.approved === true ? 'true' : 'false';
    return match;
  });
}

function parseStepRef(value: string) {
  const match = value.match(/^\$([A-Za-z0-9_-]+)\.(stdout|json)$/);
  if (!match) return null;
  return { id: match[1], field: match[2] as 'stdout' | 'json' };
}

function getStepRefValue(
  ref: { id: string; field: 'stdout' | 'json' },
  results: Record<string, WorkflowStepResult>,
  strict: boolean,
) {
  const step = results[ref.id];
  if (!step) {
    if (strict) throw new Error(`Unknown step reference: ${ref.id}.${ref.field}`);
    return '';
  }
  if (ref.field === 'stdout') return step.stdout ?? '';
  return step.json;
}

function evaluateCondition(
  condition: unknown,
  results: Record<string, WorkflowStepResult>,
) {
  if (condition === undefined || condition === null) return true;
  if (typeof condition === 'boolean') return condition;
  if (typeof condition !== 'string') throw new Error('Unsupported condition type');

  const trimmed = condition.trim();
  if (trimmed === 'true') return true;
  if (trimmed === 'false') return false;

  const match = trimmed.match(/^\$([A-Za-z0-9_-]+)\.(approved|skipped)$/);
  if (!match) throw new Error(`Unsupported condition: ${condition}`);

  const step = results[match[1]];
  if (!step) return false;

  return match[2] === 'approved' ? step.approved === true : step.skipped === true;
}

function isApprovalStep(approval: WorkflowStep['approval']) {
  if (approval === true) return true;
  if (typeof approval === 'string' && approval.trim().length > 0) return true;
  if (approval && typeof approval === 'object' && !Array.isArray(approval)) return true;
  return false;
}

function extractApprovalRequest(step: WorkflowStep, result: WorkflowStepResult) {
  const approvalConfig = normalizeApprovalConfig(step.approval);
  const fallbackPrompt = approvalConfig.prompt ?? `Approve ${step.id}?`;
  const json = result.json;

  if (json && typeof json === 'object' && !Array.isArray(json)) {
    const candidate = json as {
      requiresApproval?: { prompt?: string; items?: unknown[]; preview?: string };
      prompt?: string;
      items?: unknown[];
      preview?: string;
    };
    if (candidate.requiresApproval?.prompt) {
      return {
        type: 'approval_request' as const,
        prompt: candidate.requiresApproval.prompt,
        items: candidate.requiresApproval.items ?? [],
        ...(candidate.requiresApproval.preview ? { preview: candidate.requiresApproval.preview } : null),
      };
    }
    if (candidate.prompt) {
      return {
        type: 'approval_request' as const,
        prompt: candidate.prompt,
        items: candidate.items ?? [],
        ...(candidate.preview ? { preview: candidate.preview } : null),
      };
    }
  }

  const items = approvalConfig.items ?? normalizeApprovalItems(result.json);
  const preview = approvalConfig.preview ?? buildResultPreview(result);

  return {
    type: 'approval_request' as const,
    prompt: fallbackPrompt,
    items,
    ...(preview ? { preview } : null),
  };
}

function parseJson(stdout: string) {
  const trimmed = stdout.trim();
  if (!trimmed) return undefined;
  try {
    return JSON.parse(trimmed);
  } catch {
    return undefined;
  }
}

function toOutputItems(result: WorkflowStepResult | undefined) {
  if (!result) return [];
  if (result.json !== undefined) {
    return Array.isArray(result.json) ? result.json : [result.json];
  }
  if (result.stdout !== undefined) {
    return result.stdout === '' ? [] : [result.stdout];
  }
  return [];
}

function cloneResults(results: Record<string, WorkflowStepResult>) {
  const out: Record<string, WorkflowStepResult> = {};
  for (const [key, value] of Object.entries(results)) {
    out[key] = { ...value };
  }
  return out;
}

function findLastCompletedStepId(steps: WorkflowStep[], results: Record<string, WorkflowStepResult>) {
  for (let idx = steps.length - 1; idx >= 0; idx--) {
    if (results[steps[idx].id]) return steps[idx].id;
  }
  return null;
}

function isInteractive(stdin: NodeJS.ReadableStream) {
  return Boolean((stdin as NodeJS.ReadStream).isTTY);
}

function parseApprovalTimeoutMs(env: Record<string, string | undefined>) {
  const raw = env?.LOBSTER_APPROVAL_INPUT_TIMEOUT_MS;
  const value = Number(raw);
  if (!Number.isFinite(value) || value <= 0) return 0;
  return Math.floor(value);
}

async function runShellCommand({
  command,
  stdin,
  env,
  cwd,
  signal,
}: {
  command: string;
  stdin: string | null;
  env: Record<string, string | undefined>;
  cwd?: string;
  signal?: AbortSignal;
}) {
  const { spawn } = await import('node:child_process');

  return await new Promise<{ stdout: string; stderr: string }>((resolve, reject) => {
    const shell = resolveInlineShellCommand({ command, env });
    const child = spawn(shell.command, shell.argv, {
      env,
      cwd,
      signal,
      stdio: ['pipe', 'pipe', 'pipe'],
    });

    let stdout = '';
    let stderr = '';

    child.stdout.setEncoding('utf8');
    child.stderr.setEncoding('utf8');

    child.stdout.on('data', (d) => { stdout += d; });
    child.stderr.on('data', (d) => { stderr += d; });

    if (typeof stdin === 'string') {
      child.stdin.setDefaultEncoding('utf8');
      child.stdin.write(stdin);
    }
    child.stdin.end();

    child.on('error', reject);
    child.on('close', (code) => {
      if (code === 0) return resolve({ stdout, stderr });
      reject(new Error(`workflow command failed (${code}): ${stderr.trim() || stdout.trim() || command}`));
    });
  });
}

function getStepExecution(step: WorkflowStep) {
  if (typeof step.pipeline === 'string' && step.pipeline.trim()) {
    return { kind: 'pipeline' as const, value: step.pipeline };
  }

  const shellCommand = typeof step.run === 'string' ? step.run : step.command;
  if (typeof shellCommand === 'string' && shellCommand.trim()) {
    return { kind: 'shell' as const, value: shellCommand };
  }

  return { kind: 'none' as const };
}

async function runPipelineStep({
  stepId,
  pipelineText,
  inputValue,
  ctx,
  env,
  cwd,
}: {
  stepId: string;
  pipelineText: string;
  inputValue: unknown;
  ctx: RunContext;
  env: Record<string, string | undefined>;
  cwd?: string;
}) {
  let pipeline;
  try {
    pipeline = parsePipeline(pipelineText);
  } catch (err: any) {
    throw new Error(`Workflow step ${stepId} pipeline parse failed: ${err?.message ?? String(err)}`);
  }

  const stdout = new PassThrough();
  let renderedStdout = '';
  stdout.setEncoding('utf8');
  stdout.on('data', (chunk) => {
    renderedStdout += String(chunk);
  });

  const result = await runPipeline({
    pipeline,
    registry: ctx.registry,
    stdin: ctx.stdin,
    stdout,
    stderr: ctx.stderr,
    env,
    mode: ctx.mode,
    cwd,
    signal: ctx.signal,
    llmAdapters: ctx.llmAdapters,
    input: inputValueToStream(inputValue),
  });
  stdout.end();

  if (result.halted) {
    const haltedName = result.haltedAt?.stage?.name ?? 'unknown';
    if (result.items.length === 1 && result.items[0]?.type === 'approval_request') {
      throw new Error(
        `Workflow step ${stepId} halted for approval inside pipeline stage ${haltedName}. Use a separate approval step in the workflow file.`,
      );
    }
    throw new Error(`Workflow step ${stepId} halted before completion at pipeline stage ${haltedName}`);
  }

  const normalizedStdout = renderedStdout || serializePipelineItemsToStdout(result.items);
  const json = result.items.length
    ? (result.items.length === 1 ? result.items[0] : result.items)
    : parseJson(renderedStdout);

  return {
    id: stepId,
    stdout: normalizedStdout,
    json,
  } satisfies WorkflowStepResult;
}

function createSyntheticStepResult(stepId: string, value: unknown): WorkflowStepResult {
  if (value === null || value === undefined) {
    return { id: stepId };
  }
  if (typeof value === 'string') {
    return {
      id: stepId,
      stdout: value,
      json: parseJson(value),
    };
  }
  return {
    id: stepId,
    stdout: serializeValueForStdout(value),
    json: value,
  };
}

function encodeShellInput(value: unknown) {
  if (value === null || value === undefined) return null;
  if (typeof value === 'string') return value;
  return JSON.stringify(value);
}

function* inputValueToItems(value: unknown) {
  if (value === null || value === undefined) return;
  if (Array.isArray(value)) {
    for (const item of value) yield item;
    return;
  }
  yield value;
}

function inputValueToStream(value: unknown) {
  return (async function* () {
    for (const item of inputValueToItems(value)) {
      yield item;
    }
  })();
}

function serializePipelineItemsToStdout(items: unknown[]) {
  if (!items.length) return '';
  if (items.every((item) => typeof item === 'string')) {
    return items.map((item) => String(item)).join('\n');
  }
  if (items.length === 1) {
    return serializeValueForStdout(items[0]);
  }
  return JSON.stringify(items);
}

function serializeValueForStdout(value: unknown) {
  if (value === null || value === undefined) return '';
  if (typeof value === 'string') return value;
  return JSON.stringify(value);
}

function normalizeApprovalConfig(approval: WorkflowStep['approval']) {
  if (approval === true || approval === 'required' || approval === undefined || approval === false) {
    return {} as { prompt?: string; items?: unknown[]; preview?: string };
  }
  if (typeof approval === 'string') {
    return { prompt: approval };
  }
  if (approval && typeof approval === 'object' && !Array.isArray(approval)) {
    return approval;
  }
  return {} as { prompt?: string; items?: unknown[]; preview?: string };
}

function normalizeApprovalItems(value: unknown) {
  if (value === undefined) return [];
  return Array.isArray(value) ? value : [value];
}

function buildResultPreview(result: WorkflowStepResult) {
  if (result.stdout) return result.stdout.trim().slice(0, 2000);
  if (result.json !== undefined) return serializeValueForStdout(result.json).trim().slice(0, 2000);
  return undefined;
}
```

## File: `src/workflows/github_pr_monitor.ts`
```typescript
import { spawn } from 'node:child_process';

function runProcess(command, argv, { env, cwd }) {
  return new Promise((resolve, reject) => {
    const child = spawn(command, argv, { env, cwd, stdio: ['ignore', 'pipe', 'pipe'] });

    let stdout = '';
    let stderr = '';

    child.stdout.setEncoding('utf8');
    child.stderr.setEncoding('utf8');

    child.stdout.on('data', (d) => { stdout += d; });
    child.stderr.on('data', (d) => { stderr += d; });

    child.on('error', (err: any) => {
      if (err?.code === 'ENOENT') {
        reject(new Error('gh not found on PATH (install GitHub CLI)'));
        return;
      }
      reject(err);
    });

    child.on('close', (code) => {
      if (code === 0) return resolve({ stdout, stderr });
      reject(new Error(`gh failed (${code}): ${stderr.trim() || stdout.trim()}`));
    });
  });
}

import { diffAndStore } from '../state/store.js';

function pickSubset(snapshot) {
  if (!snapshot || typeof snapshot !== 'object') return null;
  return {
    number: snapshot.number,
    title: snapshot.title,
    url: snapshot.url,
    state: snapshot.state,
    isDraft: snapshot.isDraft,
    mergeable: snapshot.mergeable,
    reviewDecision: snapshot.reviewDecision,
    updatedAt: snapshot.updatedAt,
    baseRefName: snapshot.baseRefName,
    headRefName: snapshot.headRefName,
  };
}

export function buildPrChangeSummary(before, after) {
  const a = pickSubset(after);
  const b = pickSubset(before);

  if (!a) return { changedFields: [], changes: {} };
  if (!b) {
    return {
      changedFields: Object.keys(a),
      changes: Object.fromEntries(Object.keys(a).map((k) => [k, { from: null, to: a[k] }])),
    };
  }

  const changes = {};
  for (const key of Object.keys(a)) {
    if (JSON.stringify(a[key]) !== JSON.stringify(b[key])) {
      changes[key] = { from: b[key], to: a[key] };
    }
  }

  return {
    changedFields: Object.keys(changes),
    changes,
  };
}

function formatPrChangeMessage({ repo, pr, changedFields, prInfo }) {
  const fields = changedFields.length ? ` (${changedFields.join(', ')})` : '';
  const title = prInfo?.title ? `: ${prInfo.title}` : '';
  const url = prInfo?.url ? ` ${prInfo.url}` : '';
  return `PR updated: ${repo}#${pr}${title}${fields}.${url}`.replace(/\s+/g, ' ').trim();
}

export async function runGithubPrMonitorWorkflow({ args, ctx }) {
  const repo = args.repo;
  const pr = args.pr;
  if (!repo || !pr) throw new Error('github.pr.monitor requires args.repo and args.pr');

  const key = args.key ?? `github.pr:${repo}#${pr}`;
  const changesOnly = Boolean(args.changesOnly);
  const summaryOnly = Boolean(args.summaryOnly);

  const argv = [
    'pr',
    'view',
    String(pr),
    '--repo',
    String(repo),
    '--json',
    'number,title,url,state,isDraft,mergeable,reviewDecision,author,baseRefName,headRefName,updatedAt',
  ];

  const { stdout } = (await runProcess('gh', argv, { env: ctx.env, cwd: process.cwd() })) as any;

  let current;
  try {
    current = JSON.parse(stdout.trim());
  } catch {
    throw new Error('gh returned non-JSON output');
  }

  const { changed, before } = await diffAndStore({ env: ctx.env, key, value: current });

  if (changesOnly && !changed) {
    return {
      kind: 'github.pr.monitor',
      repo,
      prNumber: Number(pr),
      key,
      changed: false,
      suppressed: true,
    };
  }

  const summary = buildPrChangeSummary(before, current);

  if (summaryOnly) {
    return {
      kind: 'github.pr.monitor',
      repo,
      prNumber: Number(pr),
      key,
      changed,
      summary,
      pr: {
        number: current.number,
        title: current.title,
        url: current.url,
        state: current.state,
        updatedAt: current.updatedAt,
      },
    };
  }

  return {
    kind: 'github.pr.monitor',
    repo,
    prNumber: Number(pr),
    key,
    changed,
    summary,
    prSnapshot: current,
  };
}

export async function runGithubPrMonitorNotifyWorkflow({ args, ctx }) {
  const base = await runGithubPrMonitorWorkflow({
    args: {
      ...args,
      changesOnly: true,
      summaryOnly: true,
    },
    ctx,
  });

  if (base.suppressed) {
    return { kind: 'github.pr.monitor.notify', suppressed: true };
  }

  const changedFields = base.summary?.changedFields ?? [];
  const prInfo = base.pr ?? {};

  return {
    kind: 'github.pr.monitor.notify',
    changed: Boolean(base.changed),
    repo: args.repo,
    prNumber: Number(args.pr),
    message: formatPrChangeMessage({
      repo: args.repo,
      pr: Number(args.pr),
      changedFields,
      prInfo,
    }),
    pr: prInfo,
    summary: base.summary,
  };
}
```

## File: `src/workflows/registry.ts`
```typescript
export const workflowRegistry = {
  'github.pr.monitor': {
    name: 'github.pr.monitor',
    description: 'Fetch PR state via gh, diff against last run, emit only on change.',
    argsSchema: {
      type: 'object',
      properties: {
        repo: { type: 'string', description: 'owner/repo (e.g. openclaw/openclaw)' },
        pr: { type: 'number', description: 'Pull request number' },
        key: { type: 'string', description: 'Optional state key override.' },
        changesOnly: { type: 'boolean', description: 'If true, suppress output when unchanged.' },
        summaryOnly: { type: 'boolean', description: 'If true, return only a compact change summary (smaller output).' },
      },
      required: ['repo', 'pr'],
    },
    examples: [
      {
        args: { repo: 'openclaw/openclaw', pr: 1152 },
        description: 'Monitor a PR and report when it changes.',
      },
    ],
    sideEffects: [],
  },
  'github.pr.monitor.notify': {
    name: 'github.pr.monitor.notify',
    description: 'Monitor a PR and emit a single human-friendly message when it changes.',
    argsSchema: {
      type: 'object',
      properties: {
        repo: { type: 'string', description: 'owner/repo (e.g. openclaw/openclaw)' },
        pr: { type: 'number', description: 'Pull request number' },
        key: { type: 'string', description: 'Optional state key override.' },
      },
      required: ['repo', 'pr'],
    },
    examples: [
      {
        args: { repo: 'openclaw/openclaw', pr: 1152 },
        description: 'Emit "PR updated" message only when changed.',
      },
    ],
    sideEffects: [],
  },
};

export function listWorkflows() {
  return Object.values(workflowRegistry).map((w) => ({
    name: w.name,
    description: w.description,
    argsSchema: w.argsSchema,
    examples: w.examples,
    sideEffects: w.sideEffects,
  }));
}
```

## File: `test/approve_preview.test.ts`
```typescript
import test from 'node:test';
import assert from 'node:assert/strict';
import { createDefaultRegistry } from '../src/commands/registry.js';

function streamOf(items) {
  return (async function* () {
    for (const item of items) yield item;
  })();
}

test('approve preview includes stdin sample when requested', async () => {
  const registry = createDefaultRegistry();
  const cmd = registry.get('approve');

  const result = await cmd.run({
    input: streamOf([{ a: 1 }, { a: 2 }]),
    args: {
      _: [],
      emit: true,
      prompt: 'ok?',
      'preview-from-stdin': true,
      limit: 1,
    },
    ctx: {
      stdin: process.stdin,
      stdout: process.stdout,
      stderr: process.stderr,
      env: process.env,
      registry,
      mode: 'tool',
      render: { json() {}, lines() {} },
    },
  });

  const items = [];
  for await (const item of result.output) items.push(item);
  assert.equal(items[0].type, 'approval_request');
  assert.ok(String(items[0].preview).includes('"a": 1'));
});
```

## File: `test/clawd_invoke.test.ts`
```typescript
import test from 'node:test';
import assert from 'node:assert/strict';
import http from 'node:http';
import { createDefaultRegistry } from '../src/commands/registry.js';

function streamOf(items) {
  return (async function* () {
    for (const item of items) yield item;
  })();
}

test('openclaw.invoke posts to /tools/invoke and returns JSON', async () => {
  const server = http.createServer((req, res) => {
    if (req.method !== 'POST' || req.url !== '/tools/invoke') {
      res.writeHead(404);
      res.end('not found');
      return;
    }

    let body = '';
    req.setEncoding('utf8');
    req.on('data', (d) => (body += d));
    req.on('end', () => {
      const parsed = JSON.parse(body);
      assert.equal(parsed.tool, 'demo');
      assert.equal(parsed.action, 'ping');
      res.writeHead(200, { 'content-type': 'application/json' });
      res.end(JSON.stringify({ ok: true, result: [{ ok: true, echo: parsed.args }] }));
    });
  });

  await new Promise<void>((resolve) => server.listen(0, () => resolve()));
  const addr = server.address();
  const port = typeof addr === "string" || addr == null ? 0 : addr.port;

  try {
    const registry = createDefaultRegistry();
    const cmd = registry.get('openclaw.invoke');

    const result = await cmd.run({
      input: streamOf([]),
      args: {
        _: [],
        url: `http://127.0.0.1:${port}`,
        tool: 'demo',
        action: 'ping',
        'args-json': '{"hello":"world"}',
      },
      ctx: {
        stdin: process.stdin,
        stdout: process.stdout,
        stderr: process.stderr,
        env: process.env,
        registry,
        mode: 'tool',
        render: { json() {}, lines() {} },
      },
    });

    const items = [];
    for await (const it of result.output) items.push(it);
    assert.deepEqual(items, [{ ok: true, echo: { hello: 'world' } }]);
  } finally {
    server.close();
  }
});

test('openclaw.invoke --each maps input items into tool args', async () => {
  const seen: Array<{ call: number; args: unknown }> = [];
  const server = http.createServer((req, res) => {
    if (req.method !== 'POST' || req.url !== '/tools/invoke') {
      res.writeHead(404);
      res.end('not found');
      return;
    }

    let body = '';
    req.setEncoding('utf8');
    req.on('data', (d) => (body += d));
    req.on('end', () => {
      const parsed = JSON.parse(body);
      seen.push({ call: seen.length + 1, args: parsed.args });
      res.writeHead(200, { 'content-type': 'application/json' });
      res.end(JSON.stringify({ ok: true, result: [{ ok: true, call: seen.length }] }));
    });
  });

  await new Promise<void>((resolve) => server.listen(0, () => resolve()));
  const addr = server.address();
  const port = typeof addr === "string" || addr == null ? 0 : addr.port;

  try {
    const registry = createDefaultRegistry();
    const cmd = registry.get('openclaw.invoke');

    const result = await cmd.run({
      input: streamOf(['a', 'b']),
      args: {
        _: [],
        url: `http://127.0.0.1:${port}`,
        tool: 'demo',
        action: 'ping',
        each: true,
        'item-key': 'message',
        'args-json': '{"channel":"test"}',
      },
      ctx: {
        stdin: process.stdin,
        stdout: process.stdout,
        stderr: process.stderr,
        env: process.env,
        registry,
        mode: 'tool',
        render: { json() {}, lines() {} },
      },
    });

    const items = [];
    for await (const it of result.output) items.push(it);
    assert.deepEqual(items, [{ ok: true, call: 1 }, { ok: true, call: 2 }]);
    assert.deepEqual(seen, [
      { call: 1, args: { channel: 'test', message: 'a' } },
      { call: 2, args: { channel: 'test', message: 'b' } },
    ]);
  } finally {
    server.close();
  }
});
```

## File: `test/clawd_invoke_legacy.test.ts`
```typescript
import test from 'node:test';
import assert from 'node:assert/strict';
import http from 'node:http';
import { createDefaultRegistry } from '../src/commands/registry.js';

function streamOf(items) {
  return (async function* () {
    for (const item of items) yield item;
  })();
}

test('openclaw.invoke accepts legacy raw JSON response', async () => {
  const server = http.createServer((req, res) => {
    if (req.method !== 'POST' || req.url !== '/tools/invoke') {
      res.writeHead(404);
      res.end('not found');
      return;
    }

    let body = '';
    req.setEncoding('utf8');
    req.on('data', (d) => (body += d));
    req.on('end', () => {
      const parsed = JSON.parse(body);
      assert.equal(parsed.tool, 'demo');
      assert.equal(parsed.action, 'ping');
      res.writeHead(200, { 'content-type': 'application/json' });
      res.end(JSON.stringify([{ ok: true, legacy: true, echo: parsed.args }]));
    });
  });

  await new Promise<void>((resolve) => server.listen(0, () => resolve()));
  const addr = server.address();
  const port = typeof addr === "string" || addr == null ? 0 : addr.port;

  try {
    const registry = createDefaultRegistry();
    const cmd = registry.get('openclaw.invoke');

    const result = await cmd.run({
      input: streamOf([]),
      args: {
        _: [],
        url: `http://127.0.0.1:${port}`,
        tool: 'demo',
        action: 'ping',
        'args-json': '{"hello":"world"}',
      },
      ctx: {
        stdin: process.stdin,
        stdout: process.stdout,
        stderr: process.stderr,
        env: process.env,
        registry,
        mode: 'tool',
        render: { json() {}, lines() {} },
      },
    });

    const items = [];
    for await (const it of result.output) items.push(it);
    assert.deepEqual(items, [{ ok: true, legacy: true, echo: { hello: 'world' } }]);
  } finally {
    server.close();
  }
});
```

## File: `test/cli_run_file_args_json.test.ts`
```typescript
import test from 'node:test';
import assert from 'node:assert/strict';
import { promises as fsp } from 'node:fs';
import path from 'node:path';
import os from 'node:os';
import { spawnSync } from 'node:child_process';

function runLobster(args: string[], opts?: { env?: Record<string, string | undefined> }) {
  const res = spawnSync(process.execPath, [path.join('bin', 'lobster.js'), ...args], {
    cwd: path.resolve('.'),
    env: { ...process.env, ...(opts?.env ?? undefined) },
    encoding: 'utf8',
  });
  return res;
}

test('cli: run --file passes --args-json into workflow args', async () => {
  const tmpDir = await fsp.mkdtemp(path.join(os.tmpdir(), 'lobster-cli-'));
  const filePath = path.join(tmpDir, 'workflow.lobster');

  // Print both template-substituted arg and env-injected arg (LOBSTER_ARG_TASK)
  // so we catch regressions in either path.
  const workflow = `name: test\nargs:\n  task:\n    default: ""\nsteps:\n  - id: s\n    command: >\n      node -e "process.stdout.write(JSON.stringify({task: '\${task}', env: process.env.LOBSTER_ARG_TASK}))"\n`;

  await fsp.writeFile(filePath, workflow, 'utf8');

  const res = runLobster([
    'run',
    '--file',
    filePath,
    '--args-json',
    '{"task":"test"}',
  ]);

  assert.equal(res.status, 0, `expected exit 0, got ${res.status}\nstdout=${res.stdout}\nstderr=${res.stderr}`);

  const parsed = JSON.parse(String(res.stdout).trim());
  assert.deepEqual(parsed, [{ task: 'test', env: 'test' }]);
});
```

## File: `test/commands_list.test.ts`
```typescript
import test from 'node:test';
import assert from 'node:assert/strict';
import { createDefaultRegistry } from '../src/commands/registry.js';

function streamOf(items) {
  return (async function* () {
    for (const item of items) yield item;
  })();
}

test('commands.list returns command inventory including stdlib + workflows', async () => {
  const registry = createDefaultRegistry();
  const cmd = registry.get('commands.list');
  assert.ok(cmd, 'commands.list should be registered');

  const res = await cmd.run({
    input: streamOf([]),
    args: { _: [] },
    ctx: {
      stdin: process.stdin,
      stdout: process.stdout,
      stderr: process.stderr,
      env: process.env,
      registry,
      mode: 'tool',
      render: { json() {}, lines() {} },
    },
  });

  const items = [];
  for await (const it of res.output) items.push(it);

  const names = items.map((x) => x.name).sort();

  // A couple representative commands we always expect.
  assert.ok(names.includes('exec'));
  assert.ok(names.includes('json'));
  assert.ok(names.includes('llm.invoke'));
  assert.ok(names.includes('workflows.list'));
  assert.ok(names.includes('commands.list'));

  const self = items.find((x) => x.name === 'commands.list');
  assert.ok(self);
  assert.equal(typeof self.description, 'string');
  assert.ok(self.description.length > 0);
  // Schema should be present for commands that declare it.
  assert.ok(self.argsSchema);
});
```

## File: `test/core_tool_runtime.test.ts`
```typescript
import test from 'node:test';
import assert from 'node:assert/strict';
import { promises as fsp } from 'node:fs';
import path from 'node:path';
import os from 'node:os';

import { resumeToolRequest, runToolRequest } from '../src/core/index.js';

function createDirectAdapter(resultText: string) {
  const calls: Array<Record<string, unknown>> = [];
  return {
    calls,
    adapter: {
      source: 'test',
      async invoke({ payload }: { payload: Record<string, unknown> }) {
        calls.push(payload);
        return {
          ok: true,
          result: {
            runId: 'adapter_1',
            model: 'test/model',
            prompt: payload.prompt,
            status: 'completed',
            output: {
              format: 'json',
              text: resultText,
              data: JSON.parse(resultText),
            },
          },
        };
      },
    },
  };
}

test('runToolRequest executes pipeline with injected llm adapter', async () => {
  const { adapter, calls } = createDirectAdapter('{"recommendation":"no jacket"}');
  const envelope = await runToolRequest({
    pipeline:
      'exec --json=true node -e "process.stdout.write(JSON.stringify({location:\'Phoenix\',temp_f:73.8}))" | llm.invoke --provider pi --prompt "Should I wear a jacket?" --disable-cache',
    ctx: {
      env: {
        ...process.env,
        LOBSTER_LLM_PROVIDER: 'pi',
        LOBSTER_LLM_MODEL: 'test/model',
      },
      llmAdapters: {
        pi: adapter,
      },
    },
  });

  assert.equal(envelope.ok, true);
  assert.equal(envelope.status, 'ok');
  assert.equal(envelope.output?.length, 1);
  assert.equal((envelope.output![0] as any).output.data.recommendation, 'no jacket');
  assert.equal(calls.length, 1);
  assert.equal((calls[0] as any).model, 'test/model');
});

test('resumeToolRequest completes approval-gated workflow with injected llm adapter', async () => {
  const { adapter, calls } = createDirectAdapter('{"recommendation":"no","reason":"warm"}');
  const tmpDir = await fsp.mkdtemp(path.join(os.tmpdir(), 'lobster-core-tool-runtime-'));
  const filePath = path.join(tmpDir, 'workflow.lobster');

  await fsp.writeFile(
    filePath,
    JSON.stringify(
      {
        steps: [
          {
            id: 'fetch',
            run: 'node -e "process.stdout.write(JSON.stringify({location:\'Phoenix\',temp_f:73.8}))"',
          },
          {
            id: 'confirm',
            approval: 'Want jacket advice?',
            stdin: '$fetch.json',
          },
          {
            id: 'advice',
            pipeline: 'llm.invoke --provider pi --prompt "Return JSON." --disable-cache',
            stdin: '$fetch.json',
            when: '$confirm.approved',
          },
        ],
      },
      null,
      2,
    ),
    'utf8',
  );

  const env = {
    ...process.env,
    LOBSTER_STATE_DIR: path.join(tmpDir, 'state'),
    LOBSTER_LLM_PROVIDER: 'pi',
    LOBSTER_LLM_MODEL: 'test/model',
  };

  const first = await runToolRequest({
    filePath,
    ctx: {
      cwd: tmpDir,
      env,
      llmAdapters: { pi: adapter },
    },
  });

  assert.equal(first.ok, true);
  assert.equal(first.status, 'needs_approval');
  assert.ok(first.requiresApproval?.resumeToken);

  const resumed = await resumeToolRequest({
    token: first.requiresApproval?.resumeToken ?? '',
    approved: true,
    ctx: {
      cwd: tmpDir,
      env,
      llmAdapters: { pi: adapter },
    },
  });

  assert.equal(resumed.ok, true);
  assert.equal(resumed.status, 'ok');
  assert.equal((resumed.output![0] as any).output.data.reason, 'warm');
  assert.equal(calls.length, 1);
});
```

## File: `test/dedupe.test.ts`
```typescript
import test from 'node:test';
import assert from 'node:assert/strict';

import { runPipeline } from '../src/runtime.js';
import { createDefaultRegistry } from '../src/commands/registry.js';
import { parsePipeline } from '../src/parser.js';

async function run(pipelineText: string, input: any[]) {
  const pipeline = parsePipeline(pipelineText);
  const registry = createDefaultRegistry();
  const res = await runPipeline({
    pipeline,
    registry,
    stdin: process.stdin,
    stdout: process.stdout,
    stderr: process.stderr,
    env: process.env,
    mode: 'tool',
    input: (async function* () { for (const x of input) yield x; })(),
  });
  return res.items;
}

test('dedupe removes duplicate primitives (stable)', async () => {
  const out = await run('dedupe', [1, 2, 1, 3, 2]);
  assert.deepEqual(out, [1, 2, 3]);
});

test('dedupe supports --key', async () => {
  const input = [
    { id: 'a', v: 1 },
    { id: 'b', v: 2 },
    { id: 'a', v: 3 },
  ];
  const out = await run('dedupe --key id', input);
  assert.deepEqual(out, [input[0], input[1]]);
});

test('dedupe treats undefined keys as a key value', async () => {
  const input = [
    { id: undefined, v: 1 },
    { id: undefined, v: 2 },
    { id: 'x', v: 3 },
  ];
  const out = await run('dedupe --key id', input);
  assert.equal(out.length, 2);
  assert.equal(out[0].v, 1);
  assert.equal(out[1].v, 3);
});
```

## File: `test/diff_last.test.ts`
```typescript
import test from 'node:test';
import assert from 'node:assert/strict';
import os from 'node:os';
import path from 'node:path';
import { mkdtempSync } from 'node:fs';
import { createDefaultRegistry } from '../src/commands/registry.js';

function streamOf(items) {
  return (async function* () {
    for (const item of items) yield item;
  })();
}

test('diff.last reports changed on first run and not changed on same input', async () => {
  const tmp = mkdtempSync(path.join(os.tmpdir(), 'lobster-diff-'));
  const env = { ...process.env, LOBSTER_STATE_DIR: tmp };
  const registry = createDefaultRegistry();
  const cmd = registry.get('diff.last');

  const first = await cmd.run({
    input: streamOf([{ a: 1 }]),
    args: { _: [], key: 'k' },
    ctx: { stdin: process.stdin, stdout: process.stdout, stderr: process.stderr, env, registry, mode: 'tool', render: { json() {}, lines() {} } },
  });
  const out1 = [];
  for await (const it of first.output) out1.push(it);
  assert.equal(out1[0].changed, true);

  const second = await cmd.run({
    input: streamOf([{ a: 1 }]),
    args: { _: [], key: 'k' },
    ctx: { stdin: process.stdin, stdout: process.stdout, stderr: process.stderr, env, registry, mode: 'tool', render: { json() {}, lines() {} } },
  });
  const out2 = [];
  for await (const it of second.output) out2.push(it);
  assert.equal(out2[0].changed, false);

  const third = await cmd.run({
    input: streamOf([{ a: 2 }]),
    args: { _: [], key: 'k' },
    ctx: { stdin: process.stdin, stdout: process.stdout, stderr: process.stderr, env, registry, mode: 'tool', render: { json() {}, lines() {} } },
  });
  const out3 = [];
  for await (const it of third.output) out3.push(it);
  assert.equal(out3[0].changed, true);
});
```

## File: `test/doctor.test.ts`
```typescript
import test from 'node:test';
import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import path from 'node:path';

test('doctor returns tool-mode ok with version', () => {
  const bin = path.join(process.cwd(), 'bin', 'lobster.js');
  const res = spawnSync('node', [bin, 'doctor'], {
    encoding: 'utf8',
    env: { ...process.env, LOBSTER_STATE_DIR: path.join(process.cwd(), '.tmp-test-state') },
  });
  assert.equal(res.status, 0);
  const out = JSON.parse(res.stdout);
  assert.equal(out.ok, true);
  assert.equal(out.protocolVersion, 1);
  assert.equal(out.status, 'ok');
  assert.equal(out.output[0].toolMode, true);
  assert.ok(typeof out.output[0].version === 'string');
});
```

## File: `test/email_triage.test.ts`
```typescript
import test from "node:test";
import assert from "node:assert/strict";
import http from "node:http";
import { mkdtemp, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

import { createDefaultRegistry } from "../src/commands/registry.js";
import { runPipeline } from "../src/runtime.js";

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

async function closeServer(server: http.Server) {
  await new Promise<void>((resolve) => server.close(() => resolve()));
}

test("gog.gmail.search | email.triage works end-to-end (mock gog)", async () => {
  const registry = createDefaultRegistry();

  // Tests run from dist/, but fixtures live in source tree.
  const repoRoot = join(__dirname, "..", "..");
  const mockGog = join(repoRoot, "test", "fixtures", "mock-gog.mjs");

  const result = await runPipeline({
    pipeline: [
      { name: "gog.gmail.search", args: { query: "newer_than:1d", max: 20 }, raw: "" },
      { name: "email.triage", args: { limit: 20 }, raw: "" },
    ],
    registry,
    input: [],
    stdin: process.stdin,
    stdout: process.stdout,
    stderr: process.stderr,
    env: { ...process.env, GOG_BIN: mockGog },
    mode: "tool",
  } as any);

  assert.equal(result.items.length, 1);
  assert.equal(result.items[0].summary, "1 need replies, 1 need action, 1 FYI");
});

test("email.triage buckets based on subject/from/labels", async () => {
  const registry = createDefaultRegistry();

  const emails = [
    {
      id: "m1",
      threadId: "t1",
      from: "Alice <alice@example.com>",
      subject: "Quick question",
      date: "2026-01-22T07:00:00Z",
      snippet: "Hey, can you take a look?",
      labels: ["INBOX", "UNREAD"],
    },
    {
      id: "m2",
      threadId: "t2",
      from: "no-reply@service.com",
      subject: "Your receipt",
      date: "2026-01-22T06:00:00Z",
      snippet: "Thanks",
      labels: ["INBOX", "UNREAD"],
    },
    {
      id: "m3",
      threadId: "t3",
      from: "Bob <bob@example.com>",
      subject: "Action required: NDA",
      date: "2026-01-21T23:00:00Z",
      snippet: "Please sign",
      labels: ["INBOX"],
    },
  ];

  const input = (async function* () {
    for (const e of emails) yield e;
  })();

  const result = await runPipeline({
    pipeline: [{ name: "email.triage", args: { limit: 20 }, raw: "" }],
    registry,
    input,
    stdin: process.stdin,
    stdout: process.stdout,
    stderr: process.stderr,
    env: process.env,
    mode: "tool",
  } as any);

  assert.equal(result.items.length, 1);
  const out = result.items[0];
  assert.equal(out.summary, "1 need replies, 1 need action, 1 FYI");
  assert.deepEqual(out.buckets.needsReply, ["m1"]);
  assert.deepEqual(out.buckets.needsAction, ["m3"]);
  assert.deepEqual(out.buckets.fyi, ["m2"]);
});

test("email.triage --llm uses llm_task.invoke to draft replies (and can emit drafts)", async () => {
  const registry = createDefaultRegistry();

  const emails = [
    {
      id: "m1",
      threadId: "t1",
      from: "Alice <alice@example.com>",
      subject: "Quick question",
      date: "2026-01-22T07:00:00Z",
      snippet: "Hey, can you take a look?",
      labels: ["INBOX", "UNREAD"],
    },
    {
      id: "m2",
      threadId: "t2",
      from: "Bob <bob@example.com>",
      subject: "Action required: NDA",
      date: "2026-01-21T23:00:00Z",
      snippet: "Please sign",
      labels: ["INBOX"],
    },
  ];

  const cacheDir = await mkdtemp(join(tmpdir(), "lobster-cache-"));

  const bodyLog: any[] = [];
  const server = http.createServer((req, res) => {
    if (req.method !== "POST" || req.url !== "/tools/invoke") {
      res.writeHead(404);
      res.end("not found");
      return;
    }

    let buf = "";
    req.setEncoding("utf8");
    req.on("data", (d) => (buf += d));
    req.on("end", () => {
      const parsed = JSON.parse(buf || "{}");
      bodyLog.push(parsed);

      res.writeHead(200, { "content-type": "application/json" });
      // OpenClaw tool router envelope -> llm-task tool envelope
      res.end(
        JSON.stringify({
          ok: true,
          result: {
            ok: true,
            result: {
              runId: "triage_1",
              output: {
                data: {
                  decisions: [
                    {
                      id: "m1",
                      category: "needs_reply",
                      rationale: "Unclear question",
                      reply: { body: "Sure — what’s the deadline?" },
                    },
                    { id: "m2", category: "needs_action", rationale: "NDA" },
                  ],
                },
              },
            },
          },
        }),
      );
    });
  });

  await new Promise<void>((resolve) => server.listen(0, resolve));
  const addr = server.address();
  const port = typeof addr === "object" && addr ? addr.port : 0;

  try {
    // Report mode
    const input1 = (async function* () {
      for (const e of emails) yield e;
    })();

    const res1 = await runPipeline({
      pipeline: [{ name: "email.triage", args: { llm: true, model: "claude-test", limit: 20 }, raw: "" }],
      registry,
      input: input1,
      stdin: process.stdin,
      stdout: process.stdout,
      stderr: process.stderr,
      env: {
        ...process.env,
        CLAWD_URL: `http://127.0.0.1:${port}`,
        LOBSTER_CACHE_DIR: cacheDir,
        LLM_TASK_FORCE_REFRESH: "1",
      },
      mode: "tool",
    } as any);

    assert.equal(res1.items.length, 1);
    assert.equal(res1.items[0].mode, "llm");
    assert.equal(res1.items[0].buckets.needsReply.length, 1);
    assert.equal(res1.items[0].drafts.length, 1);
    assert.equal(res1.items[0].drafts[0].to, "alice@example.com");

    // Draft emit mode
    const input2 = (async function* () {
      for (const e of emails) yield e;
    })();

    const res2 = await runPipeline({
      pipeline: [
        {
          name: "email.triage",
          args: { llm: true, model: "claude-test", limit: 20, emit: "drafts" },
          raw: "",
        },
      ],
      registry,
      input: input2,
      stdin: process.stdin,
      stdout: process.stdout,
      stderr: process.stderr,
      env: {
        ...process.env,
        CLAWD_URL: `http://127.0.0.1:${port}`,
        LOBSTER_CACHE_DIR: cacheDir,
        LLM_TASK_FORCE_REFRESH: "1",
      },
      mode: "tool",
    } as any);

    assert.equal(res2.items.length, 1);
    assert.equal(res2.items[0].to, "alice@example.com");
    assert.ok(res2.items[0].subject.toLowerCase().startsWith("re:"));
    assert.equal(bodyLog.length >= 1, true);
    assert.equal(bodyLog[0].args?.model ?? bodyLog[0].model, "claude-test");
    assert.ok(bodyLog[0].prompt || bodyLog[0].args?.prompt);
  } finally {
    await rm(cacheDir, { recursive: true, force: true });
    await closeServer(server);
  }
});

test("email.triage --llm honors OPENCLAW_URL (not just CLAWD_URL)", async () => {
  const registry = createDefaultRegistry();
  const cacheDir = await mkdtemp(join(tmpdir(), "lobster-cache-"));

  const emails = [
    {
      id: "m1",
      threadId: "t1",
      from: "Alice <alice@example.com>",
      subject: "Quick question",
      date: "2026-01-22T07:00:00Z",
      snippet: "Hey, can you take a look?",
      labels: ["INBOX", "UNREAD"],
    },
  ];

  let callCount = 0;
  const server = http.createServer((req, res) => {
    if (req.method !== "POST" || req.url !== "/tools/invoke") {
      res.writeHead(404);
      res.end("not found");
      return;
    }

    callCount++;
    res.writeHead(200, { "content-type": "application/json" });
    res.end(
      JSON.stringify({
        ok: true,
        result: {
          ok: true,
          result: {
            runId: "triage_openclaw_url",
            output: {
              data: {
                decisions: [
                  {
                    id: "m1",
                    category: "needs_reply",
                    reply: { body: "Absolutely — I can help." },
                  },
                ],
              },
            },
          },
        },
      }),
    );
  });

  await new Promise<void>((resolve) => server.listen(0, resolve));
  const addr = server.address();
  const port = typeof addr === "object" && addr ? addr.port : 0;

  try {
    const input = (async function* () {
      for (const e of emails) yield e;
    })();

    const result = await runPipeline({
      pipeline: [{ name: "email.triage", args: { llm: true, limit: 20 }, raw: "" }],
      registry,
      input,
      stdin: process.stdin,
      stdout: process.stdout,
      stderr: process.stderr,
      env: {
        ...process.env,
        OPENCLAW_URL: `http://127.0.0.1:${port}`,
        LOBSTER_CACHE_DIR: cacheDir,
        LLM_TASK_FORCE_REFRESH: "1",
      },
      mode: "tool",
    } as any);

    assert.equal(callCount, 1);
    assert.equal(result.items.length, 1);
    assert.equal(result.items[0].mode, "llm");
    assert.equal(result.items[0].drafts.length, 1);
  } finally {
    await rm(cacheDir, { recursive: true, force: true });
    await closeServer(server);
  }
});
```

## File: `test/exec_stdin.test.ts`
```typescript
import test from 'node:test';
import assert from 'node:assert/strict';
import { createDefaultRegistry } from '../src/commands/registry.js';

function streamOf(items) {
  return (async function* () {
    for (const item of items) yield item;
  })();
}

test('exec --stdin jsonl feeds pipeline input to subprocess', async () => {
  const registry = createDefaultRegistry();
  const cmd = registry.get('exec');

  const nodeScript = [
    "let d='';",
    "process.stdin.on('data',c=>d+=c);",
    "process.stdin.on('end',()=>{",
    "  const lines=d.trim().split('\\n').filter(Boolean);",
    "  console.log(JSON.stringify(lines));",
    "});",
  ].join('');

  const result = await cmd.run({
    input: streamOf([{ a: 1 }, { a: 2 }]),
    args: {
      _: ['node', '-e', nodeScript],
      stdin: 'jsonl',
      json: true,
    },
    ctx: {
      stdin: process.stdin,
      stdout: process.stdout,
      stderr: process.stderr,
      env: process.env,
      registry,
      mode: 'human',
      render: { json() {}, lines() {} },
    },
  });

  const items = [];
  for await (const item of result.output) items.push(item);
  assert.deepEqual(items, ['{"a":1}', '{"a":2}']);
});
```

## File: `test/github_pr_notify_format.test.ts`
```typescript
import test from 'node:test';
import assert from 'node:assert/strict';
import { buildPrChangeSummary } from '../src/workflows/github_pr_monitor.js';

function formatLikeWorkflow({ repo, pr, after, before }) {
  const summary = buildPrChangeSummary(before, after);
  const fields = summary.changedFields.length ? ` (${summary.changedFields.join(', ')})` : '';
  const title = after?.title ? `: ${after.title}` : '';
  const url = after?.url ? ` ${after.url}` : '';
  return `PR updated: ${repo}#${pr}${title}${fields}.${url}`.replace(/\s+/g, ' ').trim();
}

test('notify message includes repo/pr and changed fields', () => {
  const before = { number: 1, title: 'A', url: 'u', state: 'OPEN', updatedAt: 't1' };
  const after = { ...before, title: 'B', updatedAt: 't2' };

  const msg = formatLikeWorkflow({ repo: 'o/r', pr: 1, before, after });
  assert.ok(msg.includes('o/r#1'));
  assert.ok(msg.includes('title'));
  assert.ok(msg.includes('updatedAt'));
});
```

## File: `test/github_pr_summary.test.ts`
```typescript
import test from 'node:test';
import assert from 'node:assert/strict';
import { buildPrChangeSummary } from '../src/workflows/github_pr_monitor.js';

const build = buildPrChangeSummary as any;

test('buildPrChangeSummary reports all fields on first snapshot', () => {
  const after = {
    number: 1,
    title: 'A',
    url: 'u',
    state: 'OPEN',
    isDraft: false,
    mergeable: 'MERGEABLE',
    reviewDecision: 'REVIEW_REQUIRED',
    updatedAt: 't1',
    baseRefName: 'main',
    headRefName: 'feat',
  };

  const res = build(null, after);
  assert.ok(res.changedFields.length > 0);
  assert.equal(res.changes.title.to, 'A');
});

test('buildPrChangeSummary only includes changed fields', () => {
  const before = {
    number: 1,
    title: 'A',
    url: 'u',
    state: 'OPEN',
    isDraft: false,
    mergeable: 'MERGEABLE',
    reviewDecision: null,
    updatedAt: 't1',
    baseRefName: 'main',
    headRefName: 'feat',
  };
  const after = { ...before, title: 'B', updatedAt: 't2' };

  const res = build(before, after);
  assert.deepEqual(res.changedFields.sort(), ['title', 'updatedAt'].sort());
  assert.equal(res.changes.title.from, 'A');
  assert.equal(res.changes.title.to, 'B');
});
```

## File: `test/group_by.test.ts`
```typescript
import test from 'node:test';
import assert from 'node:assert/strict';

import { runPipeline } from '../src/runtime.js';
import { createDefaultRegistry } from '../src/commands/registry.js';
import { parsePipeline } from '../src/parser.js';

async function run(pipelineText: string, input: any[]) {
  const pipeline = parsePipeline(pipelineText);
  const registry = createDefaultRegistry();
  const res = await runPipeline({
    pipeline,
    registry,
    stdin: process.stdin,
    stdout: process.stdout,
    stderr: process.stderr,
    env: process.env,
    mode: 'tool',
    input: (async function* () { for (const x of input) yield x; })(),
  });
  return res.items;
}

test('groupBy groups items by key and preserves group order', async () => {
  const input = [
    { from: 'a', id: 1 },
    { from: 'b', id: 2 },
    { from: 'a', id: 3 },
  ];
  const out = await run('groupBy --key from', input);
  assert.equal(out.length, 2);
  assert.deepEqual(out[0].key, 'a');
  assert.deepEqual(out[0].items.map((x: any) => x.id), [1, 3]);
  assert.equal(out[0].count, 2);
  assert.deepEqual(out[1].key, 'b');
});

test('groupBy supports nested key paths', async () => {
  const input = [
    { user: { id: 'u1' } },
    { user: { id: 'u2' } },
    { user: { id: 'u1' } },
  ];
  const out = await run('groupBy --key user.id', input);
  assert.deepEqual(out.map((g: any) => g.key), ['u1', 'u2']);
  assert.equal(out[0].count, 2);
});
```

## File: `test/llm_invoke.test.ts`
```typescript
import test from 'node:test';
import assert from 'node:assert/strict';
import http from 'node:http';
import { mkdtemp, rm } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import path from 'node:path';

import { createDefaultRegistry } from '../src/commands/registry.js';

function streamOf(items: any[]) {
  return (async function* () {
    for (const item of items) yield item;
  })();
}

async function collect(iterable: AsyncIterable<any>) {
  const items = [];
  for await (const item of iterable) items.push(item);
  return items;
}

test('llm.invoke auto-detects OpenClaw provider and normalizes output', async () => {
  const registry = createDefaultRegistry();
  const cmd = registry.get('llm.invoke');
  assert.ok(cmd, 'llm.invoke should be registered');
  const cacheDir = await mkdtemp(path.join(tmpdir(), 'lobster-cache-'));

  const bodyLog: any[] = [];
  const server = http.createServer((req, res) => {
    if (req.method !== 'POST' || req.url !== '/tools/invoke') {
      res.writeHead(404);
      res.end('nope');
      return;
    }
    let buf = '';
    req.setEncoding('utf8');
    req.on('data', (d) => (buf += d));
    req.on('end', () => {
      const parsed = JSON.parse(buf || '{}');
      bodyLog.push(parsed);
      res.writeHead(200, { 'content-type': 'application/json' });
      res.end(
        JSON.stringify({
          ok: true,
          result: {
            ok: true,
            result: {
              runId: 'invoke_1',
              model: parsed.args?.model,
              prompt: parsed.args?.prompt,
              output: { data: { summary: 'hello' } },
            },
          },
        }),
      );
    });
  });

  await new Promise<void>((resolve) => server.listen(0, resolve));
  const addr = server.address();
  const port = typeof addr === 'object' && addr ? addr.port : 0;

  try {
    const result = await cmd.run({
      input: streamOf([{ kind: 'text', text: 'doc' }]),
      args: {
        _: [],
        model: 'claude-3-sonnet',
        prompt: 'Summarize',
      },
      ctx: baseCtx({ OPENCLAW_URL: `http://localhost:${port}`, LOBSTER_CACHE_DIR: cacheDir }, registry),
    } as any);

    const items = await collect(result.output!);
    assert.equal(items.length, 1);
    assert.equal(items[0].kind, 'llm.invoke');
    assert.equal(items[0].source, 'openclaw');
    assert.equal(items[0].runId, 'invoke_1');
    assert.equal(items[0].output.data.summary, 'hello');
    assert.equal(bodyLog.length, 1);
    assert.equal(bodyLog[0].tool, 'llm-task');
    assert.equal(bodyLog[0].args.prompt, 'Summarize');
  } finally {
    await rm(cacheDir, { recursive: true, force: true });
    await closeServer(server);
  }
});

test('llm.invoke uses Pi adapter over local HTTP bridge', async () => {
  const registry = createDefaultRegistry();
  const cmd = registry.get('llm.invoke');
  assert.ok(cmd);
  const cacheDir = await mkdtemp(path.join(tmpdir(), 'lobster-cache-'));

  const requestLog: any[] = [];
  const server = http.createServer((req, res) => {
    if (req.method !== 'POST' || req.url !== '/invoke') {
      res.writeHead(404);
      res.end('nope');
      return;
    }
    let buf = '';
    req.setEncoding('utf8');
    req.on('data', (d) => (buf += d));
    req.on('end', () => {
      const parsed = JSON.parse(buf || '{}');
      requestLog.push(parsed);
      res.writeHead(200, { 'content-type': 'application/json' });
      res.end(
        JSON.stringify({
          ok: true,
          result: {
            runId: 'pi_1',
            model: parsed.model,
            prompt: parsed.prompt,
            output: {
              format: 'json',
              text: '{"decision":"reply"}',
              data: { decision: 'reply' },
            },
            diagnostics: { adapter: 'pi' },
          },
        }),
      );
    });
  });

  await new Promise<void>((resolve) => server.listen(0, '127.0.0.1', resolve));
  const addr = server.address();
  const port = typeof addr === 'object' && addr ? addr.port : 0;

  try {
    const result = await cmd.run({
      input: streamOf([{ kind: 'text', text: 'draft this' }]),
      args: {
        _: [],
        provider: 'pi',
        prompt: 'Decide',
        'output-schema': '{"type":"object","required":["decision"]}',
      },
      ctx: baseCtx(
        {
          LOBSTER_PI_LLM_ADAPTER_URL: `http://127.0.0.1:${port}`,
          LOBSTER_LLM_MODEL: 'anthropic/claude-sonnet-4-5',
          LOBSTER_CACHE_DIR: cacheDir,
        },
        registry,
      ),
    } as any);

    const items = await collect(result.output!);
    assert.equal(items.length, 1);
    assert.equal(items[0].kind, 'llm.invoke');
    assert.equal(items[0].source, 'pi');
    assert.equal(items[0].model, 'anthropic/claude-sonnet-4-5');
    assert.equal(items[0].output.data.decision, 'reply');
    assert.equal(requestLog.length, 1);
    assert.equal(requestLog[0].prompt, 'Decide');
    assert.equal(requestLog[0].model, 'anthropic/claude-sonnet-4-5');
    assert.equal(requestLog[0].artifacts.length, 1);
  } finally {
    await rm(cacheDir, { recursive: true, force: true });
    await closeServer(server);
  }
});

function baseCtx(envOverrides: Record<string, string>, registry?: any) {
  return {
    stdin: process.stdin,
    stdout: process.stdout,
    stderr: process.stderr,
    env: { ...process.env, ...envOverrides },
    registry: registry ?? null,
    mode: 'tool',
    render: { json() {}, lines() {} },
  };
}

async function closeServer(server: http.Server) {
  if (!server.listening) return;
  await new Promise<void>((resolve) => server.close(() => resolve()));
}
```

## File: `test/llm_task_invoke.test.ts`
```typescript
import test from 'node:test';
import assert from 'node:assert/strict';
import http from 'node:http';
import { mkdtemp, rm } from 'node:fs/promises';
import { tmpdir } from 'node:os';
import path from 'node:path';

import { createDefaultRegistry } from '../src/commands/registry.js';

function streamOf(items: any[]) {
  return (async function* () {
    for (const item of items) yield item;
  })();
}

async function collect(iterable: AsyncIterable<any>) {
  const items = [];
  for await (const item of iterable) items.push(item);
  return items;
}

test('llm_task.invoke posts to /tools/invoke (clawd) and normalizes result', async () => {
  const registry = createDefaultRegistry();
  const cmd = registry.get('llm_task.invoke');
  assert.ok(cmd, 'llm_task.invoke should be registered');
  const cacheDir = await mkdtemp(path.join(tmpdir(), 'lobster-cache-'));

  const bodyLog: any[] = [];
  const server = http.createServer((req, res) => {
    if (req.method !== 'POST' || req.url !== '/tools/invoke') {
      res.writeHead(404);
      res.end('nope');
      return;
    }
    let buf = '';
    req.setEncoding('utf8');
    req.on('data', (d) => (buf += d));
    req.on('end', () => {
      const parsed = JSON.parse(buf || '{}');
      bodyLog.push(parsed);
      res.writeHead(200, { 'content-type': 'application/json' });
      res.end(
        JSON.stringify({
          ok: true,
          result: {
            ok: true,
            result: {
              runId: 'task_1',
              model: parsed.args?.model,
              prompt: parsed.args?.prompt,
              output: {
                text: 'done',
                data: { summary: 'hello world' },
              },
              usage: { inputTokens: 12, outputTokens: 2, totalTokens: 14 },
            },
          },
        }),
      );
    });
  });

  await new Promise<void>((resolve) => server.listen(0, resolve));
  const addr = server.address();
  const port = typeof addr === 'object' && addr ? addr.port : 0;

  try {
    const result = await cmd.run({
      input: streamOf([{ kind: 'text', text: 'doc' }]),
      args: {
        _: [],
        token: 'test-token',
        model: 'claude-3-sonnet',
        prompt: 'Summarize',
      },
      ctx: baseCtx({ LOBSTER_CACHE_DIR: cacheDir, CLAWD_URL: `http://localhost:${port}` }, registry),
    } as any);

    const items = await collect(result.output!);
    assert.equal(items.length, 1);
    const payload = items[0];
    assert.equal(payload.kind, 'llm_task.invoke');
    assert.equal(payload.runId, 'task_1');
    assert.equal(payload.output.data.summary, 'hello world');
    assert.equal(payload.model, 'claude-3-sonnet');
    assert.equal(payload.source, 'clawd');
    assert.equal(payload.cached, false);
    assert.ok(payload.cacheKey);

    assert.equal(bodyLog.length, 1);
    assert.equal(bodyLog[0].tool, 'llm-task');
    assert.equal(bodyLog[0].action, 'invoke');
    assert.equal(bodyLog[0].args.prompt, 'Summarize');
    assert.equal(bodyLog[0].args.model, 'claude-3-sonnet');
    assert.equal(bodyLog[0].args.artifacts.length, 1);
    assert.equal(bodyLog[0].args.artifactHashes.length, 1);
  } finally {
    await rm(cacheDir, { recursive: true, force: true });
    await closeServer(server);
  }
});

test('llm_task.invoke retries when schema validation fails', async () => {
  const registry = createDefaultRegistry();
  const cmd = registry.get('llm_task.invoke');
  assert.ok(cmd);
  const cacheDir = await mkdtemp(path.join(tmpdir(), 'lobster-cache-'));

  let calls = 0;
  const server = http.createServer((req, res) => {
    if (req.method !== 'POST' || req.url !== '/tools/invoke') {
      res.writeHead(404);
      res.end();
      return;
    }
    calls += 1;
    const valid = calls >= 2;
    const payload = {
      ok: true,
      result: {
        ok: true,
        result: {
          runId: `attempt_${calls}`,
          output: valid ? { data: { decision: 'send' } } : { data: { foo: 'bar' } },
        },
      },
    };
    res.writeHead(200, { 'content-type': 'application/json' });
    res.end(JSON.stringify(payload));
  });

  await new Promise<void>((resolve) => server.listen(0, resolve));
  const addr = server.address();
  const port = typeof addr === 'object' && addr ? addr.port : 0;

  try {
    const result = await cmd.run({
      input: streamOf([]),
      args: {
        _: [],
        model: 'claude-3-opus',
        prompt: 'Decide',
        'output-schema': '{"type":"object","required":["decision"]}',
        'max-validation-retries': 2,
      },
      ctx: baseCtx({ LOBSTER_CACHE_DIR: cacheDir, CLAWD_URL: `http://localhost:${port}` }, registry),
    } as any);

    const items = await collect(result.output!);
    assert.equal(items.length, 1);
    assert.equal(items[0].runId, 'attempt_2');
    assert.equal(items[0].output.data.decision, 'send');
    assert.equal(calls, 2);
  } finally {
    await rm(cacheDir, { recursive: true, force: true });
    await closeServer(server);
  }
});

test('llm_task.invoke persists to run state so resume skips remote call', async () => {
  const stateDir = await mkdtemp(path.join(tmpdir(), 'lobster-state-'));
  const registry = createDefaultRegistry();
  const cmd = registry.get('llm_task.invoke');
  assert.ok(cmd);

  const server = http.createServer((req, res) => {
    if (req.method !== 'POST' || req.url !== '/tools/invoke') {
      res.writeHead(404);
      res.end('not found');
      return;
    }
    let buf = '';
    req.setEncoding('utf8');
    req.on('data', (d) => (buf += d));
    req.on('end', () => {
      void buf;
      res.writeHead(200, { 'content-type': 'application/json' });
      res.end(
        JSON.stringify({ ok: true, result: { ok: true, result: { runId: 'state_run', output: { data: { ok: true } } } } }),
      );
    });
  });
  await new Promise<void>((resolve) => server.listen(0, resolve));
  const addr = server.address();
  const port = typeof addr === 'object' && addr ? addr.port : 0;

  const cacheDir = await mkdtemp(path.join(tmpdir(), 'lobster-cache-'));
  const ctxEnv = { LOBSTER_STATE_DIR: stateDir, LOBSTER_CACHE_DIR: cacheDir };

  try {
    const first = await cmd.run({
      input: streamOf([{ foo: 'bar' }]),
      args: {
        _: [],
        model: 'claude',
        prompt: 'Do thing',
        'state-key': 'run123',
      },
      ctx: baseCtx({ ...ctxEnv, CLAWD_URL: `http://localhost:${port}` }, registry),
    } as any);
    const firstItems = await collect(first.output!);
    assert.equal(firstItems[0].source, 'clawd');

    await closeServer(server);

    const second = await cmd.run({
      input: streamOf([{ foo: 'bar' }]),
      args: {
        _: [],
        model: 'claude',
        prompt: 'Do thing',
        'state-key': 'run123',
      },
      ctx: baseCtx({ ...ctxEnv, CLAWD_URL: `http://localhost:${port}` }, registry),
    } as any);
    const secondItems = await collect(second.output!);
    assert.equal(secondItems.length, 1);
    assert.equal(secondItems[0].source, 'run_state');
  } finally {
    await rm(stateDir, { recursive: true, force: true });
    await rm(cacheDir, { recursive: true, force: true });
    await closeServer(server);
  }
});

test('llm_task.invoke reuses file cache when URL unavailable', async () => {
  const cacheDir = await mkdtemp(path.join(tmpdir(), 'lobster-cache-'));
  const registry = createDefaultRegistry();
  const cmd = registry.get('llm_task.invoke');
  assert.ok(cmd);

  const server = http.createServer((req, res) => {
    if (req.method !== 'POST' || req.url !== '/tools/invoke') {
      res.writeHead(404);
      res.end('not found');
      return;
    }
    let buf = '';
    req.setEncoding('utf8');
    req.on('data', (d) => (buf += d));
    req.on('end', () => {
      void buf;
      res.writeHead(200, { 'content-type': 'application/json' });
      res.end(
        JSON.stringify({ ok: true, result: { ok: true, result: { runId: 'cache_run', output: { text: 'cached' } } } }),
      );
    });
  });
  await new Promise<void>((resolve) => server.listen(0, resolve));
  const addr = server.address();
  const port = typeof addr === 'object' && addr ? addr.port : 0;

  const ctxEnv = { LOBSTER_CACHE_DIR: cacheDir, CLAWD_URL: `http://localhost:${port}` };

  try {
    const first = await cmd.run({
      input: streamOf([]),
      args: {
        _: [],
        model: 'claude',
        prompt: 'Cache me',
      },
      ctx: baseCtx({ ...ctxEnv, CLAWD_URL: `http://localhost:${port}` }, registry),
    } as any);
    const firstItems = await collect(first.output!);
    assert.equal(firstItems[0].source, 'clawd');

    await closeServer(server);

    const second = await cmd.run({
      input: streamOf([]),
      args: {
        _: [],
        model: 'claude',
        prompt: 'Cache me',
      },
      ctx: baseCtx({ ...ctxEnv, CLAWD_URL: `http://localhost:${port}` }, registry),
    } as any);
    const secondItems = await collect(second.output!);
    assert.equal(secondItems.length, 1);
    assert.equal(secondItems[0].source, 'cache');
    assert.equal(secondItems[0].cached, true);
  } finally {
    await rm(cacheDir, { recursive: true, force: true });
    await closeServer(server);
  }
});

test('llm_task.invoke uses CLAWD_URL (/tools/invoke) without requiring --url/--model', async () => {
  const registry = createDefaultRegistry();
  const cmd = registry.get('llm_task.invoke');
  assert.ok(cmd);

  const cacheDir = await mkdtemp(path.join(tmpdir(), 'lobster-cache-'));

  const bodyLog: any[] = [];
  const server = http.createServer((req, res) => {
    if (req.method !== 'POST' || req.url !== '/tools/invoke') {
      res.writeHead(404);
      res.end('not found');
      return;
    }

    let buf = '';
    req.setEncoding('utf8');
    req.on('data', (d) => (buf += d));
    req.on('end', () => {
      const parsed = JSON.parse(buf || '{}');
      bodyLog.push(parsed);

      // This is the OpenClaw tool router envelope.
      res.writeHead(200, { 'content-type': 'application/json' });
      res.end(
        JSON.stringify({
          ok: true,
          result: {
            ok: true,
            result: {
              runId: 'task_clawd_1',
              output: { data: { hello: 'world' } },
            },
          },
        }),
      );
    });
  });

  await new Promise<void>((resolve) => server.listen(0, resolve));
  const addr = server.address();
  const port = typeof addr === 'object' && addr ? addr.port : 0;

  try {
    const result = await cmd.run({
      input: streamOf([{ kind: 'text', text: 'doc' }]),
      args: {
        _: [],
        // no url, no model
        prompt: 'Summarize',
        refresh: true,
      },
      ctx: baseCtx({ CLAWD_URL: `http://localhost:${port}`, LOBSTER_CACHE_DIR: cacheDir }, registry),
    } as any);

    const items = await collect(result.output!);
    assert.equal(items.length, 1);
    assert.equal(items[0].source, 'clawd');
    assert.equal(items[0].cached, false);
    assert.equal(items[0].runId, 'task_clawd_1');
    assert.equal(items[0].output.data.hello, 'world');

    assert.equal(bodyLog.length, 1);
    assert.equal(bodyLog[0].tool, 'llm-task');
    assert.equal(bodyLog[0].action, 'invoke');
    assert.equal(bodyLog[0].args.prompt, 'Summarize');
    assert.ok(Array.isArray(bodyLog[0].args.artifactHashes));
  } finally {
    await rm(cacheDir, { recursive: true, force: true });
    await closeServer(server);
  }
});

function baseCtx(envOverrides: Record<string, string>, registry?) {
  return {
    stdin: process.stdin,
    stdout: process.stdout,
    stderr: process.stderr,
    env: { ...process.env, ...envOverrides },
    registry: registry ?? null,
    mode: 'tool',
    render: { json() {}, lines() {} },
  };
}

async function closeServer(server: http.Server) {
  if (!server.listening) return;
  await new Promise<void>((resolve) => server.close(() => resolve()));
}
```

## File: `test/map.test.ts`
```typescript
import test from 'node:test';
import assert from 'node:assert/strict';

import { runPipeline } from '../src/runtime.js';
import { createDefaultRegistry } from '../src/commands/registry.js';
import { parsePipeline } from '../src/parser.js';

async function run(pipelineText: string, input: any[]) {
  const pipeline = parsePipeline(pipelineText);
  const registry = createDefaultRegistry();
  const res = await runPipeline({
    pipeline,
    registry,
    stdin: process.stdin,
    stdout: process.stdout,
    stderr: process.stderr,
    env: process.env,
    mode: 'tool',
    input: (async function* () { for (const x of input) yield x; })(),
  });
  return res.items;
}

test('map --wrap wraps items', async () => {
  const out = await run('map --wrap item', [1, 2]);
  assert.deepEqual(out, [{ item: 1 }, { item: 2 }]);
});

test('map --unwrap unwraps fields', async () => {
  const out = await run('map --unwrap x', [{ x: 1 }, { x: 2 }]);
  assert.deepEqual(out, [1, 2]);
});

test('map adds fields via assignments with template values', async () => {
  const out = await run('map kind=pr id={{id}}', [{ id: 123, title: 't' }]);
  // assignment overwrites existing id with rendered string
  assert.deepEqual(out, [{ id: '123', title: 't', kind: 'pr' }]);
});

test('map converts non-object items to {value: item} when adding fields', async () => {
  const out = await run('map kind=num', [5]);
  assert.deepEqual(out, [{ value: 5, kind: 'num' }]);
});
```

## File: `test/multi_approval_resume.test.ts`
```typescript
import test from 'node:test';
import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import path from 'node:path';
import os from 'node:os';
import { promises as fsp } from 'node:fs';

function runTool(pipeline, env) {
  const bin = path.join(process.cwd(), 'bin', 'lobster.js');
  const res = spawnSync('node', [bin, 'run', '--mode', 'tool', pipeline], {
    encoding: 'utf8',
    env: { ...process.env, ...env },
  });
  assert.equal(res.status, 0);
  return JSON.parse(res.stdout);
}

function resume(token, approve, env) {
  const bin = path.join(process.cwd(), 'bin', 'lobster.js');
  const res = spawnSync('node', [bin, 'resume', '--token', token, '--approve', approve ? 'yes' : 'no'], {
    encoding: 'utf8',
    env: { ...process.env, ...env },
  });
  assert.equal(res.status, 0);
  return JSON.parse(res.stdout);
}

test('two approve gates can be resumed sequentially', async () => {
  const tmpDir = await fsp.mkdtemp(path.join(os.tmpdir(), 'lobster-multi-approval-'));
  const stateDir = path.join(tmpDir, 'state');
  const env = { LOBSTER_STATE_DIR: stateDir };

  const pipeline = [
    "exec --json --shell \"printf '%s' '[{\\\"x\\\":1}]'\"",
    "approve --prompt 'first?'",
    "approve --prompt 'second?'",
    'pick x',
  ].join(' | ');

  const first = runTool(pipeline, env);
  assert.equal(first.status, 'needs_approval');
  assert.equal(first.requiresApproval.prompt, 'first?');

  const second = resume(first.requiresApproval.resumeToken, true, env);
  assert.equal(second.status, 'needs_approval');
  assert.equal(second.requiresApproval.prompt, 'second?');

  const done = resume(second.requiresApproval.resumeToken, true, env);
  assert.equal(done.status, 'ok');
  assert.deepEqual(done.output, [{ x: 1 }]);

  const files = await fsp.readdir(stateDir);
  const pipelineResumeFiles = files.filter((name) => name.startsWith('pipeline_resume_'));
  assert.deepEqual(pipelineResumeFiles, []);
});
```

## File: `test/openclaw_invoke_alias.test.ts`
```typescript
import test from 'node:test';
import assert from 'node:assert/strict';
import { createDefaultRegistry } from '../src/commands/registry.js';

test('clawd.invoke remains available as an alias', async () => {
  const registry = createDefaultRegistry();
  const a = registry.get('openclaw.invoke');
  const b = registry.get('clawd.invoke');
  assert.ok(a, 'expected openclaw.invoke to exist');
  assert.ok(b, 'expected clawd.invoke to exist');
  assert.equal(typeof a.run, 'function');
  assert.equal(typeof b.run, 'function');
});
```

## File: `test/parser.test.ts`
```typescript
import test from 'node:test';
import assert from 'node:assert/strict';
import { parsePipeline } from '../src/parser.js';

test('parsePipeline splits stages and args', () => {
  const p = parsePipeline("exec echo hi | where a=1 | pick id,subject");
  assert.equal(p.length, 3);
  assert.equal(p[0].name, 'exec');
  assert.deepEqual(p[0].args._, ['echo', 'hi']);
  assert.equal(p[1].name, 'where');
  assert.equal(p[1].args._[0], 'a=1');
  assert.equal(p[2].name, 'pick');
  assert.equal(p[2].args._[0], 'id,subject');
});

test('parsePipeline keeps quoted pipes', () => {
  const p = parsePipeline("exec echo 'a|b' | json");
  assert.equal(p.length, 2);
  assert.deepEqual(p[0].args._, ['echo', 'a|b']);
});
```

## File: `test/read_line.test.ts`
```typescript
import test from 'node:test';
import assert from 'node:assert/strict';
import { PassThrough } from 'node:stream';

import { readLineFromStream } from '../src/read_line.js';

test('readLineFromStream resolves on newline', async () => {
  const input = new PassThrough();
  const promise = readLineFromStream(input);
  input.write('yes\n');
  input.end();

  const value = await promise;
  assert.equal(value, 'yes');
});

test('readLineFromStream resolves on end without newline', async () => {
  const input = new PassThrough();
  const promise = readLineFromStream(input);
  input.write('partial');
  input.end();

  const value = await promise;
  assert.equal(value, 'partial');
});

test('readLineFromStream times out when no input arrives', async () => {
  const input = new PassThrough();
  await assert.rejects(() => readLineFromStream(input, { timeoutMs: 5 }), /Timed out waiting for input/);
});
```

## File: `test/resume.test.ts`
```typescript
import test from 'node:test';
import assert from 'node:assert/strict';
import { promises as fsp } from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { spawnSync } from 'node:child_process';

import { decodeResumeToken } from '../src/resume.js';
import { encodeToken } from '../src/token.js';

function runCli(args: string[], env: Record<string, string | undefined>) {
  const bin = path.join(process.cwd(), 'bin', 'lobster.js');
  return spawnSync('node', [bin, ...args], {
    encoding: 'utf8',
    env: { ...process.env, ...env },
  });
}

test('state-backed resume token roundtrip and resume pipeline continues', async () => {
  const tmpDir = await fsp.mkdtemp(path.join(os.tmpdir(), 'lobster-resume-'));
  const stateDir = path.join(tmpDir, 'state');

  const pipeline =
    "exec --json --shell \"node -e 'process.stdout.write(JSON.stringify([{a:1}]))'\" | approve --prompt 'ok?' | pick a";

  const first = runCli(['run', '--mode', 'tool', pipeline], { LOBSTER_STATE_DIR: stateDir });
  assert.equal(first.status, 0);
  const firstJson = JSON.parse(first.stdout);
  assert.equal(firstJson.status, 'needs_approval');
  assert.ok(firstJson.requiresApproval?.resumeToken);

  const payload = decodeResumeToken(firstJson.requiresApproval.resumeToken);
  assert.equal(payload.kind, 'pipeline-resume');
  assert.equal(typeof payload.stateKey, 'string');

  const resumed = runCli(
    ['resume', '--token', firstJson.requiresApproval.resumeToken, '--approve', 'yes'],
    { LOBSTER_STATE_DIR: stateDir },
  );
  assert.equal(resumed.status, 0);
  const resumedJson = JSON.parse(resumed.stdout);
  assert.equal(resumedJson.status, 'ok');
  assert.deepEqual(resumedJson.output, [{ a: 1 }]);
});

test('decodeResumeToken rejects inline executable pipeline tokens', () => {
  const forgedToken = encodeToken({
    protocolVersion: 1,
    v: 1,
    pipeline: [{ name: 'exec', args: { shell: 'echo FORGED' }, raw: "exec --shell 'echo FORGED'" }],
    resumeAtIndex: 0,
    items: [],
    prompt: 'ignored',
  });

  assert.throws(() => decodeResumeToken(forgedToken), /Invalid token/);
});

test('resume cancellation cleans up pipeline resume state', async () => {
  const tmpDir = await fsp.mkdtemp(path.join(os.tmpdir(), 'lobster-resume-cancel-'));
  const stateDir = path.join(tmpDir, 'state');

  const pipeline =
    "exec --json --shell \"node -e 'process.stdout.write(JSON.stringify([{a:1}]))'\" | approve --prompt 'ok?' | pick a";

  const first = runCli(['run', '--mode', 'tool', pipeline], { LOBSTER_STATE_DIR: stateDir });
  assert.equal(first.status, 0);
  const firstJson = JSON.parse(first.stdout);
  assert.equal(firstJson.status, 'needs_approval');

  const cancelled = runCli(
    ['resume', '--token', firstJson.requiresApproval.resumeToken, '--approve', 'no'],
    { LOBSTER_STATE_DIR: stateDir },
  );
  assert.equal(cancelled.status, 0);
  const cancelledJson = JSON.parse(cancelled.stdout);
  assert.equal(cancelledJson.status, 'cancelled');

  const files = await fsp.readdir(stateDir);
  const pipelineResumeFiles = files.filter((name) => name.startsWith('pipeline_resume_'));
  assert.deepEqual(pipelineResumeFiles, []);
});
```

## File: `test/shell.test.ts`
```typescript
import test from 'node:test';
import assert from 'node:assert/strict';

import { resolveInlineShellCommand } from '../src/shell.js';

test('resolveInlineShellCommand uses POSIX shell by default', () => {
  const resolved = resolveInlineShellCommand({
    command: 'echo hello',
    env: { SHELL: '/bin/zsh' },
    platform: 'darwin',
  });

  assert.equal(resolved.command, '/bin/sh');
  assert.deepEqual(resolved.argv, ['-lc', 'echo hello']);
});

test('resolveInlineShellCommand uses cmd on Windows', () => {
  const resolved = resolveInlineShellCommand({
    command: 'echo hello',
    env: { ComSpec: 'C:\\Windows\\System32\\cmd.exe' },
    platform: 'win32',
  });

  assert.equal(resolved.command, 'C:\\Windows\\System32\\cmd.exe');
  assert.deepEqual(resolved.argv, ['/d', '/s', '/c', 'echo hello']);
});

test('resolveInlineShellCommand respects powershell override', () => {
  const resolved = resolveInlineShellCommand({
    command: 'Write-Host hello',
    env: { LOBSTER_SHELL: 'pwsh' },
    platform: 'linux',
  });

  assert.equal(resolved.command, 'pwsh');
  assert.deepEqual(resolved.argv, ['-NoProfile', '-Command', 'Write-Host hello']);
});
```

## File: `test/sort.test.ts`
```typescript
import test from 'node:test';
import assert from 'node:assert/strict';

import { runPipeline } from '../src/runtime.js';
import { createDefaultRegistry } from '../src/commands/registry.js';
import { parsePipeline } from '../src/parser.js';

async function run(pipelineText: string, input: any[]) {
  const pipeline = parsePipeline(pipelineText);
  const registry = createDefaultRegistry();
  const res = await runPipeline({
    pipeline,
    registry,
    stdin: process.stdin,
    stdout: process.stdout,
    stderr: process.stderr,
    env: process.env,
    mode: 'tool',
    input: (async function* () { for (const x of input) yield x; })(),
  });
  return res.items;
}

test('sort sorts primitives ascending by default', async () => {
  const out = await run('sort', [3, 1, 2]);
  assert.deepEqual(out, [1, 2, 3]);
});

test('sort supports --desc', async () => {
  const out = await run('sort --desc', ["b", "a", "c"]);
  assert.deepEqual(out, ["c", "b", "a"]);
});

test('sort sorts objects by --key and is stable', async () => {
  const input = [
    { id: 'a', k: 2 },
    { id: 'b', k: 1 },
    { id: 'c', k: 2 },
  ];
  const out = await run('sort --key k', input);
  assert.deepEqual(out.map((x: any) => x.id), ['b', 'a', 'c']);
});

test('sort places undefined/null last', async () => {
  const input = [
    { id: 'a', k: undefined },
    { id: 'b', k: 2 },
    { id: 'c', k: null },
    { id: 'd', k: 1 },
  ];
  const out = await run('sort --key k', input);
  assert.deepEqual(out.map((x: any) => x.id), ['d', 'b', 'a', 'c']);
});
```

## File: `test/state.test.ts`
```typescript
import test from 'node:test';
import assert from 'node:assert/strict';
import os from 'node:os';
import path from 'node:path';
import { mkdtempSync } from 'node:fs';
import { createDefaultRegistry } from '../src/commands/registry.js';
import { runPipeline } from '../src/runtime.js';

function streamOf(items) {
  return (async function* () {
    for (const item of items) yield item;
  })();
}

test('state.set writes and state.get reads', async () => {
  const tmp = mkdtempSync(path.join(os.tmpdir(), 'lobster-state-'));
  const registry = createDefaultRegistry();

  const env = { ...process.env, LOBSTER_STATE_DIR: tmp };

  // write
  const setCmd = registry.get('state.set');
  await setCmd.run({
    input: streamOf([{ a: 1 }]),
    args: { _: ['demo-key'] },
    ctx: { stdin: process.stdin, stdout: process.stdout, stderr: process.stderr, env, registry, mode: 'tool', render: { json() {}, lines() {} } },
  });

  // read
  const getCmd = registry.get('state.get');
  const res = await getCmd.run({
    input: streamOf([]),
    args: { _: ['demo-key'] },
    ctx: { stdin: process.stdin, stdout: process.stdout, stderr: process.stderr, env, registry, mode: 'tool', render: { json() {}, lines() {} } },
  });

  const items = [];
  for await (const it of res.output) items.push(it);
  assert.deepEqual(items, [{ a: 1 }]);
});

test('state.get returns null for missing key', async () => {
  const tmp = mkdtempSync(path.join(os.tmpdir(), 'lobster-state-'));
  const registry = createDefaultRegistry();
  const env = { ...process.env, LOBSTER_STATE_DIR: tmp };

  const output = await runPipeline({
    pipeline: [{ name: 'state.get', args: { _: ['missing'] }, raw: 'state.get missing' }],
    registry,
    input: [],
    stdin: process.stdin,
    stdout: process.stdout,
    stderr: process.stderr,
    env,
    mode: 'tool',
  });

  assert.deepEqual(output.items, [null]);
});
```

## File: `test/template.test.ts`
```typescript
import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';

import { runPipeline } from '../src/runtime.js';
import { createDefaultRegistry } from '../src/commands/registry.js';
import { parsePipeline } from '../src/parser.js';

async function run(pipelineText: string, input: any[]) {
  const pipeline = parsePipeline(pipelineText);
  const registry = createDefaultRegistry();
  const res = await runPipeline({
    pipeline,
    registry,
    stdin: process.stdin,
    stdout: process.stdout,
    stderr: process.stderr,
    env: process.env,
    mode: 'tool',
    input: (async function* () { for (const x of input) yield x; })(),
  });
  return res.items;
}

test('template renders fields and nested fields', async () => {
  const out = await run("template --text 'hi {{user.name}}'", [{ user: { name: 'v' } }]);
  assert.deepEqual(out, ['hi v']);
});

test('template renders missing fields as empty', async () => {
  const out = await run("template --text 'x={{nope}}'", [{ a: 1 }]);
  assert.deepEqual(out, ['x=']);
});

test('template supports {{.}} for whole item', async () => {
  const out = await run("template --text '{{.}}'", [{ a: 1 }]);
  assert.deepEqual(out, [JSON.stringify({ a: 1 })]);
});

test('template supports --file', async () => {
  const dir = await fs.mkdtemp(path.join(os.tmpdir(), 'lobster-template-'));
  const file = path.join(dir, 'tpl.txt');
  await fs.writeFile(file, 'hey {{x}}', 'utf8');
  const out = await run(`template --file ${file}`, [{ x: 'ok' }]);
  assert.deepEqual(out, ['hey ok']);
});
```

## File: `test/tool_envelope_version.test.ts`
```typescript
import test from 'node:test';
import assert from 'node:assert/strict';
import { spawnSync } from 'node:child_process';
import path from 'node:path';

test('tool mode outputs protocolVersion', () => {
  const bin = path.join(process.cwd(), 'bin', 'lobster.js');
  const res = spawnSync('node', [bin, 'run', '--mode', 'tool', "exec --json --shell 'echo [1]'"], {
    encoding: 'utf8',
  });

  assert.equal(res.status, 0);
  const out = JSON.parse(res.stdout);
  assert.equal(out.protocolVersion, 1);
  assert.equal(out.ok, true);
});
```

## File: `test/tool_mode.test.ts`
```typescript
import test from 'node:test';
import assert from 'node:assert/strict';
import { parsePipeline } from '../src/parser.js';
import { createDefaultRegistry } from '../src/commands/registry.js';
import { runPipeline } from '../src/runtime.js';

function streamOf(items) {
  return (async function* () {
    for (const item of items) yield item;
  })();
}

test('approve halts pipeline in tool mode', async () => {
  const registry = createDefaultRegistry();
  const pipeline = parsePipeline(
    "exec --json --shell \"node -e 'process.stdout.write(JSON.stringify([{a:1}]))'\" | approve --prompt 'send?' | exec --shell 'exit 1'"
  );

  const output = await runPipeline({
    pipeline,
    registry,
    input: [],
    stdin: process.stdin,
    stdout: process.stdout,
    stderr: process.stderr,
    env: process.env,
    mode: 'tool',
  });

  assert.equal(output.halted, true);
  assert.equal(output.items.length, 1);
  assert.equal(output.items[0].type, 'approval_request');
  assert.equal(output.items[0].items.length, 1);
  assert.deepEqual(output.items[0].items[0], { a: 1 });
});

test('approve passes through in human interactive mode only (emit required otherwise)', async () => {
  const registry = createDefaultRegistry();
  const cmd = registry.get('approve');

  const result = await cmd.run({
    input: streamOf([{ x: 1 }]),
    args: { _: [], emit: true, prompt: 'ok?' },
    ctx: {
      stdin: process.stdin,
      stdout: process.stdout,
      stderr: process.stderr,
      env: process.env,
      registry,
      mode: 'human',
      render: { json() {}, lines() {} },
    },
  });

  const items = [];
  for await (const it of result.output) items.push(it);
  assert.equal(result.halt, true);
  assert.equal(items[0].type, 'approval_request');
});
```

## File: `test/workflow_args_env.test.ts`
```typescript
import test from 'node:test';
import assert from 'node:assert/strict';
import { promises as fsp } from 'node:fs';
import path from 'node:path';
import os from 'node:os';

import { runWorkflowFile } from '../src/workflows/file.js';

test('workflow file exposes args as LOBSTER_ARG_* env vars (safe for quotes)', async () => {
  const workflow = {
    name: 'args-env',
    args: {
      text: { default: '' },
    },
    steps: [
      {
        id: 'echo',
        // Avoid embedding the arg into the shell command; read from env instead.
        command:
          "node -e \"process.stdout.write(JSON.stringify({text: process.env.LOBSTER_ARG_TEXT}))\"",
      },
    ],
  };

  const tmpDir = await fsp.mkdtemp(path.join(os.tmpdir(), 'lobster-workflow-args-env-'));
  const stateDir = path.join(tmpDir, 'state');
  const filePath = path.join(tmpDir, 'workflow.lobster');
  await fsp.writeFile(filePath, JSON.stringify(workflow, null, 2), 'utf8');

  const env = { ...process.env, LOBSTER_STATE_DIR: stateDir };
  const text = 'hello "world" $HOME `backticks` $(whoami)';

  const result = await runWorkflowFile({
    filePath,
    args: { text },
    ctx: {
      stdin: process.stdin,
      stdout: process.stdout,
      stderr: process.stderr,
      env,
      mode: 'tool',
    },
  });

  assert.equal(result.status, 'ok');
  assert.deepEqual(result.output, [{ text }]);
});
```

## File: `test/workflow_file.test.ts`
```typescript
import test from 'node:test';
import assert from 'node:assert/strict';
import { promises as fsp } from 'node:fs';
import http from 'node:http';
import path from 'node:path';
import os from 'node:os';

import { createDefaultRegistry } from '../src/commands/registry.js';
import { runWorkflowFile } from '../src/workflows/file.js';
import { decodeResumeToken } from '../src/resume.js';

test('workflow file runs with approval and resume', async () => {
  const workflow = {
    name: 'sample',
    steps: [
      {
        id: 'collect',
        command: "node -e \"process.stdout.write(JSON.stringify([{value:1}]))\"",
      },
      {
        id: 'mutate',
        command: "node -e \"let d='';process.stdin.on('data',c=>d+=c);process.stdin.on('end',()=>{const items=JSON.parse(d);items[0].value=2;process.stdout.write(JSON.stringify(items));});\"",
        stdin: '$collect.stdout',
      },
      {
        id: 'approve_step',
        command: "node -e \"process.stdout.write(JSON.stringify({requiresApproval:{prompt:'Proceed?', items:[{id:1}]}}))\"",
        approval: 'required',
      },
      {
        id: 'finish',
        command: "node -e \"let d='';process.stdin.on('data',c=>d+=c);process.stdin.on('end',()=>{const items=JSON.parse(d);process.stdout.write(JSON.stringify({done:true,value:items[0].value}));});\"",
        stdin: '$mutate.stdout',
        condition: '$approve_step.approved',
      },
    ],
  };

  const tmpDir = await fsp.mkdtemp(path.join(os.tmpdir(), 'lobster-workflow-'));
  const stateDir = path.join(tmpDir, 'state');
  const filePath = path.join(tmpDir, 'workflow.lobster');
  await fsp.writeFile(filePath, JSON.stringify(workflow, null, 2), 'utf8');

  const env = { ...process.env, LOBSTER_STATE_DIR: stateDir };

  const first = await runWorkflowFile({
    filePath,
    ctx: {
      stdin: process.stdin,
      stdout: process.stdout,
      stderr: process.stderr,
      env,
      mode: 'tool',
    },
  });

  assert.equal(first.status, 'needs_approval');
  assert.equal(first.requiresApproval?.prompt, 'Proceed?');
  assert.ok(first.requiresApproval?.resumeToken);

  const payload = decodeResumeToken(first.requiresApproval?.resumeToken ?? '');
  assert.equal(payload.kind, 'workflow-file');

  const resumed = await runWorkflowFile({
    filePath,
    ctx: {
      stdin: process.stdin,
      stdout: process.stdout,
      stderr: process.stderr,
      env,
      mode: 'tool',
    },
    resume: payload,
    approved: true,
  });

  assert.equal(resumed.status, 'ok');
  assert.deepEqual(resumed.output, [{ done: true, value: 2 }]);

  const stateFiles = await fsp.readdir(stateDir);
  const resumeStateFiles = stateFiles.filter((name) => name.startsWith('workflow_resume_'));
  assert.deepEqual(resumeStateFiles, []);
});

test('workflow resume cancellation cleans up resume state', async () => {
  const workflow = {
    steps: [
      {
        id: 'approve_step',
        command: "node -e \"process.stdout.write(JSON.stringify({requiresApproval:{prompt:'Proceed?', items:[{id:1}]}}))\"",
        approval: 'required',
      },
      {
        id: 'finish',
        command: "node -e \"process.stdout.write(JSON.stringify({done:true}))\"",
        condition: '$approve_step.approved',
      },
    ],
  };

  const tmpDir = await fsp.mkdtemp(path.join(os.tmpdir(), 'lobster-workflow-cancel-'));
  const stateDir = path.join(tmpDir, 'state');
  const filePath = path.join(tmpDir, 'workflow.lobster');
  await fsp.writeFile(filePath, JSON.stringify(workflow, null, 2), 'utf8');

  const env = { ...process.env, LOBSTER_STATE_DIR: stateDir };

  const first = await runWorkflowFile({
    filePath,
    ctx: {
      stdin: process.stdin,
      stdout: process.stdout,
      stderr: process.stderr,
      env,
      mode: 'tool',
    },
  });
  assert.equal(first.status, 'needs_approval');

  const payload = decodeResumeToken(first.requiresApproval?.resumeToken ?? '');
  assert.equal(payload.kind, 'workflow-file');
  assert.ok(payload.stateKey);

  await fsp.access(path.join(stateDir, `${payload.stateKey}.json`));

  const cancelled = await runWorkflowFile({
    filePath,
    ctx: {
      stdin: process.stdin,
      stdout: process.stdout,
      stderr: process.stderr,
      env,
      mode: 'tool',
    },
    resume: payload,
    approved: false,
  });

  assert.equal(cancelled.status, 'cancelled');
  assert.deepEqual(cancelled.output, []);
  const files = await fsp.readdir(stateDir);
  const resumeStateFiles = files.filter((name) => name.startsWith('workflow_resume_'));
  assert.deepEqual(resumeStateFiles, []);
});

test('workflow files can mix shell steps, approval-only steps, and pipeline llm steps', async () => {
  const registry = createDefaultRegistry();
  const requests: any[] = [];
  const server = http.createServer((req, res) => {
    if (req.method !== 'POST' || req.url !== '/invoke') {
      res.writeHead(404);
      res.end('nope');
      return;
    }

    let body = '';
    req.setEncoding('utf8');
    req.on('data', (chunk) => {
      body += chunk;
    });
    req.on('end', () => {
      const parsed = JSON.parse(body || '{}');
      requests.push(parsed);
      res.writeHead(200, { 'content-type': 'application/json' });
      res.end(
        JSON.stringify({
          ok: true,
          result: {
            runId: 'http_1',
            model: parsed.model || 'test-model',
            prompt: parsed.prompt,
            output: {
              format: 'json',
              text: '{"recommendation":"no","reason":"warm"}',
              data: { recommendation: 'no', reason: 'warm' },
            },
          },
        }),
      );
    });
  });

  await new Promise<void>((resolve) => server.listen(0, '127.0.0.1', resolve));
  const addr = server.address();
  const port = typeof addr === 'object' && addr ? addr.port : 0;

  const workflow = {
    name: 'mixed-workflow',
    steps: [
      {
        id: 'fetch',
        run: "node -e \"process.stdout.write(JSON.stringify({location:'Phoenix',temp_f:73.8,humidity_pct:13,wind_mph:3.4}))\"",
      },
      {
        id: 'confirm',
        approval: 'Want jacket advice from the LLM?',
        stdin: '$fetch.json',
      },
      {
        id: 'advice',
        pipeline: 'llm.invoke --provider http --prompt "Given this weather data, should I wear a jacket? Return JSON." --disable-cache',
        stdin: '$fetch.json',
        when: '$confirm.approved',
      },
    ],
  };

  const tmpDir = await fsp.mkdtemp(path.join(os.tmpdir(), 'lobster-workflow-mixed-'));
  const stateDir = path.join(tmpDir, 'state');
  const cacheDir = path.join(tmpDir, 'cache');
  const filePath = path.join(tmpDir, 'workflow.lobster');
  await fsp.writeFile(filePath, JSON.stringify(workflow, null, 2), 'utf8');

  const env = {
    ...process.env,
    LOBSTER_STATE_DIR: stateDir,
    LOBSTER_CACHE_DIR: cacheDir,
    LOBSTER_LLM_ADAPTER_URL: `http://127.0.0.1:${port}`,
  };

  try {
    const first = await runWorkflowFile({
      filePath,
      ctx: {
        stdin: process.stdin,
        stdout: process.stdout,
        stderr: process.stderr,
        env,
        mode: 'tool',
        registry,
      },
    });

    assert.equal(first.status, 'needs_approval');
    assert.equal(first.requiresApproval?.prompt, 'Want jacket advice from the LLM?');
    assert.match(first.requiresApproval?.preview ?? '', /Phoenix/);
    assert.ok(first.requiresApproval?.resumeToken);

    const payload = decodeResumeToken(first.requiresApproval?.resumeToken ?? '');
    assert.equal(payload.kind, 'workflow-file');

    const resumed = await runWorkflowFile({
      filePath,
      ctx: {
        stdin: process.stdin,
        stdout: process.stdout,
        stderr: process.stderr,
        env,
        mode: 'tool',
        registry,
      },
      resume: payload,
      approved: true,
    });

    assert.equal(resumed.status, 'ok');
    assert.equal(resumed.output.length, 1);
    assert.equal((resumed.output[0] as any).kind, 'llm.invoke');
    assert.equal((resumed.output[0] as any).output.data.recommendation, 'no');
    assert.equal(requests.length, 1);
    assert.equal(requests[0].artifacts[0].location, 'Phoenix');
  } finally {
    await closeServer(server);
  }
});

test('workflow pipeline steps respect cwd and feed later shell steps via stdout refs', async () => {
  const registry = createDefaultRegistry();
  const workflow = {
    cwd: '${TARGET_DIR}',
    steps: [
      {
        id: 'pwd',
        pipeline: 'exec pwd',
      },
      {
        id: 'capture',
        run: "node -e \"let d='';process.stdin.on('data',c=>d+=c);process.stdin.on('end',()=>{process.stdout.write(JSON.stringify({pwd:d.trim()}));});\"",
        stdin: '$pwd.stdout',
      },
    ],
  };

  const tmpDir = await fsp.mkdtemp(path.join(os.tmpdir(), 'lobster-workflow-pipeline-cwd-'));
  const targetDir = path.join(tmpDir, 'nested');
  const filePath = path.join(tmpDir, 'workflow.lobster');
  await fsp.mkdir(targetDir, { recursive: true });
  await fsp.writeFile(filePath, JSON.stringify(workflow, null, 2), 'utf8');

  const result = await runWorkflowFile({
    filePath,
    args: { TARGET_DIR: targetDir },
    ctx: {
      stdin: process.stdin,
      stdout: process.stdout,
      stderr: process.stderr,
      env: { ...process.env, LOBSTER_STATE_DIR: path.join(tmpDir, 'state') },
      mode: 'tool',
      registry,
    },
  });

  assert.equal(result.status, 'ok');
  const resolvedTargetDir = await fsp.realpath(targetDir);
  assert.deepEqual(result.output, [{ pwd: resolvedTargetDir }]);
});

async function closeServer(server: http.Server) {
  if (!server.listening) return;
  await new Promise<void>((resolve) => server.close(() => resolve()));
}
```

## File: `test/workflows.test.ts`
```typescript
import test from 'node:test';
import assert from 'node:assert/strict';
import { createDefaultRegistry } from '../src/commands/registry.js';

function streamOf(items) {
  return (async function* () {
    for (const item of items) yield item;
  })();
}

test('workflows.list returns known workflows', async () => {
  const registry = createDefaultRegistry();
  const cmd = registry.get('workflows.list');

  const res = await cmd.run({
    input: streamOf([]),
    args: { _: [] },
    ctx: { stdin: process.stdin, stdout: process.stdout, stderr: process.stderr, env: process.env, registry, mode: 'tool', render: { json() {}, lines() {} } },
  });

  const items = [];
  for await (const it of res.output) items.push(it);

  const names = items.map((x) => x.name).sort();
  assert.deepEqual(names, ['github.pr.monitor', 'github.pr.monitor.notify']);
});
```

## File: `test/fixtures/gog_gmail_search.json`
```json
[
  {
    "id": "m1",
    "threadId": "t1",
    "from": "Alice <alice@example.com>",
    "subject": "Quick question",
    "date": "2026-01-22T07:00:00Z",
    "snippet": "Hey, can you take a look?",
    "labels": ["INBOX", "UNREAD"]
  },
  {
    "id": "m2",
    "threadId": "t2",
    "from": "no-reply@service.com",
    "subject": "Your receipt",
    "date": "2026-01-22T06:00:00Z",
    "snippet": "Thanks for your purchase",
    "labels": ["INBOX", "UNREAD"]
  },
  {
    "id": "m3",
    "threadId": "t3",
    "from": "Bob <bob@example.com>",
    "subject": "Action required: NDA",
    "date": "2026-01-21T23:00:00Z",
    "snippet": "Please sign",
    "labels": ["INBOX"]
  }
]
```

## File: `test/fixtures/mock-gog.mjs`
```
#!/usr/bin/env node
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

const argv = process.argv.slice(2);

// Minimal mock for `gog gmail search` and `gog gmail send`.
if (argv[0] === 'gmail' && argv[1] === 'search') {
  const data = readFileSync(join(__dirname, 'gog_gmail_search.json'), 'utf8');
  process.stdout.write(data);
  process.exit(0);
}

if (argv[0] === 'gmail' && argv[1] === 'send') {
  // Echo a json success object.
  process.stdout.write(JSON.stringify({ ok: true }));
  process.exit(0);
}

process.stderr.write('mock-gog: unsupported args: ' + argv.join(' ') + '\n');
process.exit(2);
```

