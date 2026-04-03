---
id: github.com-gokapso-agent-skills-be95778d-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:53.867068
---

# KNOWLEDGE EXTRACT: github.com_gokapso_agent-skills_be95778d
> **Extracted on:** 2026-04-01 07:28:42
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007518971/github.com_gokapso_agent-skills_be95778d

---

## File: `README.md`
```markdown
# Kapso Agent Skills

![Kapso Agent Skills](https://app.kapso.ai/rails/active_storage/blobs/redirect/eyJfcmFpbHMiOnsiZGF0YSI6ImI3YTg1NDE1LThjYzAtNGE2ZC04MGM3LWJhOGY2ODI0MTY3MSIsInB1ciI6ImJsb2JfaWQifX0=--1057c1ee33188e5afd42480e99937ae352e1a99b/kapso-agent-skills-image.png)

> **Alpha**: These skills are in active development and subject to rapid change.

Agent skills for [Kapso](https://kapso.ai), built on the open [Agent Skills](https://agentskills.io) format.

## Installation

```bash
npx skills add gokapso/kapso-agent-skills
```

## Environment Variables

Set these environment variables before using the skills:

```bash
export KAPSO_API_BASE_URL="https://api.kapso.ai"
export KAPSO_API_KEY="your-api-key"
```

| Variable | Description |
|----------|-------------|
| `KAPSO_API_BASE_URL` | Kapso API host. Use `https://api.kapso.ai` |
| `KAPSO_API_KEY` | API key from the Kapso web app at [app.kapso.ai](https://app.kapso.ai) |

## Path selection

- Prefer the Kapso CLI when it is installed and already authenticated. The skill docs now show CLI-first flows where the CLI already covers the task well.
- Keep the provided scripts and direct API references as the fallback path when the CLI is unavailable or when a task still needs script-only operations.
- If you use the CLI path, start with `kapso login` and `kapso status`.

## What are Agent Skills?

Agent Skills are folders of instructions, scripts, and resources that agents can discover and use to perform tasks more accurately. Each skill is a directory with a `SKILL.md` entrypoint and optional supporting files.

```
my-skill/
├── SKILL.md          # Required: instructions + metadata
├── scripts/          # Optional: executable code
├── references/       # Optional: documentation
└── assets/           # Optional: templates, resources
```

Skills use **progressive disclosure**: agents load only the name and description at startup, then read full instructions when a task matches. This keeps context usage efficient while giving agents access to detailed knowledge on demand.

## Available skills

- **integrate-whatsapp**: Connect WhatsApp, set up webhooks, send messages/templates, manage flows
- **automate-whatsapp**: Build WhatsApp automations with workflows, agents, functions, and databases
- **observe-whatsapp**: Debug delivery issues, inspect webhook deliveries, triage errors, run health checks

Each skill contains detailed documentation in its `SKILL.md` file.

## Maintenance

Shared references in this repo also exist under `kapso-brain/knowledge/docs_legacy/skills/skills`. Keep mirrored docs in sync when updating shared onboarding or API guidance.

## SKILL.md format

Each skill requires a `SKILL.md` file with YAML frontmatter:

```yaml
---
name: my-skill
description: What this skill does and when to use it.
---

# My Skill

Instructions for the agent...
```

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Lowercase identifier (letters, numbers, hyphens) |
| `description` | Yes | When to use this skill (max 1024 chars) |

## Learn more

- [Agent Skills specification](https://agentskills.io/specification)
- [Authoring best practices](https://platform.claude.com/brain/knowledge/docs_legacy/en/agents-and-tools/agent-skills/best-practices)
- [Example skills](https://github.com/anthropics/skills)
```

## File: `update-skill-filemap.mjs`
```
#!/usr/bin/env node

import { readFileSync, readdirSync, statSync, writeFileSync } from 'node:fs'
import path from 'node:path'
import { fileURLToPath } from 'node:url'

const MARKER_BEGIN = '<!-- FILEMAP:BEGIN -->'
const MARKER_END = '<!-- FILEMAP:END -->'

const IGNORED_DIRS = new Set(['node_modules', '.git', '.DS_Store'])
const IGNORED_FILES = new Set(['.DS_Store'])

function listSkillDirs(skillsRoot) {
  const entries = readdirSync(skillsRoot, { withFileTypes: true })
  return entries
    .filter((e) => e.isDirectory())
    .map((e) => path.join(skillsRoot, e.name))
    .filter((dir) => {
      try {
        return statSync(path.join(dir, 'SKILL.md')).isFile()
      } catch {
        return false
      }
    })
    .sort()
}

function walkDir(skillRoot, relDir = '.', out = new Map()) {
  const absDir = relDir === '.' ? skillRoot : path.join(skillRoot, relDir)
  let entries
  try {
    entries = readdirSync(absDir, { withFileTypes: true })
  } catch {
    return out
  }

  const files = []
  const dirs = []

  for (const entry of entries) {
    if (entry.name.startsWith('.') && entry.name !== '.well-known') continue
    if (entry.isDirectory()) {
      if (IGNORED_DIRS.has(entry.name)) continue
      dirs.push(entry.name)
      continue
    }
    if (entry.isFile()) {
      if (IGNORED_FILES.has(entry.name)) continue
      files.push(entry.name)
      continue
    }
  }

  files.sort((a, b) => a.localeCompare(b))
  dirs.sort((a, b) => a.localeCompare(b))

  if (files.length > 0) {
    out.set(relDir, files)
  }

  for (const d of dirs) {
    const nextRel = relDir === '.' ? d : path.join(relDir, d)
    walkDir(skillRoot, nextRel, out)
  }

  return out
}

function formatFileMap({ skillName, map }) {
  const lines = [`[${skillName} file map]|root: .`]
  const keys = [...map.keys()].sort((a, b) => a.localeCompare(b))

  for (const dir of keys) {
    const files = map.get(dir) || []
    const label = dir === '.' ? '.' : dir.replaceAll('\\', '/')
    lines.push(`|${label}:{${files.join(',')}}`)
  }

  return lines.join('\n')
}

function upsertFileMapSection(skillMd, fileMapText) {
  const block = `${MARKER_BEGIN}\n\`\`\`text\n${fileMapText}\n\`\`\`\n${MARKER_END}\n`

  const beginIndex = skillMd.indexOf(MARKER_BEGIN)
  const endIndex = skillMd.indexOf(MARKER_END)

  if (beginIndex >= 0 && endIndex >= 0 && endIndex > beginIndex) {
    const before = skillMd.slice(0, beginIndex).replace(/\s*$/, '\n\n')
    const after = skillMd.slice(endIndex + MARKER_END.length).replace(/^\s*/, '\n')
    return `${before}${block}${after}`.replace(/\n{4,}/g, '\n\n\n')
  }

  return `${skillMd.replace(/\s*$/, '\n\n')}${block}`
}

function main() {
  const scriptDir = path.dirname(fileURLToPath(import.meta.url))
  const skillsRoot = path.join(scriptDir, 'skills')

  const skillDirs = listSkillDirs(skillsRoot)
  if (skillDirs.length === 0) {
    console.error(`No skills found under: ${skillsRoot}`)
    process.exit(1)
  }

  for (const dir of skillDirs) {
    const skillMdPath = path.join(dir, 'SKILL.md')
    const skillName = path.basename(dir)

    const original = readFileSync(skillMdPath, 'utf8')
    const map = walkDir(dir)
    const fileMapText = formatFileMap({ skillName, map })
    const updated = upsertFileMapSection(original, fileMapText)

    if (updated !== original) {
      writeFileSync(skillMdPath, updated, 'utf8')
      console.log(`Updated: ${path.relative(scriptDir, skillMdPath)}`)
    } else {
      console.log(`Unchanged: ${path.relative(scriptDir, skillMdPath)}`)
    }
  }
}

main()

```

## File: `skills/automate-whatsapp/SKILL.md`
```markdown
---
name: automate-whatsapp
description: "Build WhatsApp automations with Kapso workflows: configure WhatsApp triggers, edit workflow graphs, manage executions, deploy functions, and use databases/integrations for state. Use when automating WhatsApp conversations and event handling."
---

# Automate WhatsApp

## When to use

Use this skill to build and run WhatsApp automations: workflow CRUD, graph edits, triggers, executions, function management, app integrations, and D1 database operations.

## Setup

Preferred path:
- Kapso CLI installed and authenticated (`kapso login`)
- Use the CLI for project/number discovery before wiring triggers or automations

Fallback path:
Env vars:
- `KAPSO_API_BASE_URL` (host only, no `/platform/v1`)
- `KAPSO_API_KEY`

## How to

### Discover phone numbers first

Preferred path:
1. Check project state: `kapso status`
2. List connected numbers: `kapso whatsapp numbers list --output json`
3. Resolve a display number when needed: `kapso whatsapp numbers resolve --phone-number "<display-number>" --output json`

Fallback path:
1. List number configs for triggers: `node scripts/list-whatsapp-phone-numbers.js`

### Edit a workflow graph

1. Fetch graph: `node scripts/get-graph.js <workflow_id>` (note the `lock_version`)
2. Edit the JSON (see graph rules below)
3. Validate: `node scripts/validate-graph.js --definition-file <path>`
4. Update: `node scripts/update-graph.js <workflow_id> --expected-lock-version <n> --definition-file <path>`
5. Re-fetch to confirm

For small edits, use `edit-graph.js` with `--old-file` and `--new-file` instead.

If you get a lock_version conflict: re-fetch, re-apply changes, retry with new lock_version.

### Manage triggers

1. List: `node scripts/list-triggers.js <workflow_id>`
2. Create: `node scripts/create-trigger.js <workflow_id> --trigger-type <type> --phone-number-id <id>`
3. Toggle: `node scripts/update-trigger.js --trigger-id <id> --active true|false`
4. Delete: `node scripts/delete-trigger.js --trigger-id <id>`

For inbound_message triggers, prefer `kapso whatsapp numbers resolve --phone-number "<display-number>" --output json` to get the exact `phone_number_id`. Fall back to `node scripts/list-whatsapp-phone-numbers.js` when the CLI is unavailable.

### Debug executions

1. List: `node scripts/list-executions.js <workflow_id>`
2. Inspect: `node scripts/get-execution.js <execution-id>`
3. Get value: `node scripts/get-context-value.js <execution-id> --variable-path vars.foo`
4. Events: `node scripts/list-execution-events.js <execution-id>`

### Create and deploy a function

1. Write code with handler signature (see function rules below)
2. Create: `node scripts/create-function.js --name <name> --code-file <path>`
3. Deploy: `node scripts/deploy-function.js --function-id <id>`
4. Verify: `node scripts/get-function.js --function-id <id>`

### Set up agent node with app integrations

1. Find model: `node scripts/list-provider-models.js`
2. Find account: `node scripts/list-accounts.js --app-slug <slug>` (use `pipedream_account_id`)
3. Find action: `node scripts/search-actions.js --query <word> --app-slug <slug>` (action_id = key)
4. Create integration: `node scripts/create-integration.js --action-id <id> --app-slug <slug> --account-id <id> --configured-props <json>`
5. Add tools to agent node via `flow_agent_app_integration_tools`

### Database CRUD

1. List tables: `node scripts/list-tables.js`
2. Query: `node scripts/query-rows.js --table <name> --filters <json>`
3. Create/update/delete with row scripts

## Graph rules

- Exactly one start node with `id` = `start`
- Never change existing node IDs
- Use `{node_type}_{timestamp_ms}` for new node IDs
- Non-decide nodes have 0 or 1 outgoing `next` edge
- Decide edge labels must match `conditions[].label`
- Edge keys are `source`/`target`/`label` (not `from`/`to`)

For full schema details, see `references/graph-contract.md`.

## Function rules

```js
async function handler(request, env) {
  // Parse input
  const body = await request.json();
  // Use env.KV and env.DB as needed
  return new Response(JSON.stringify({ result: "ok" }));
}
```

- Do NOT use `export`, `export default`, or arrow functions
- Return a `Response` object

## Execution context

Always use this structure:
- `vars` - user-defined variables
- `system` - system variables
- `context` - channel data
- `metadata` - request metadata

## Scripts

### Workflows

| Script | Purpose |
|--------|---------|
| `list-workflows.js` | List workflows (metadata only) |
| `get-workflow.js` | Get workflow metadata |
| `create-workflow.js` | Create a workflow |
| `update-workflow-settings.js` | Update workflow settings |

### Graph

| Script | Purpose |
|--------|---------|
| `get-graph.js` | Get workflow graph + lock_version |
| `edit-graph.js` | Patch graph via string replacement |
| `update-graph.js` | Replace entire graph |
| `validate-graph.js` | Validate graph structure locally |

### Triggers

| Script | Purpose |
|--------|---------|
| `list-triggers.js` | List triggers for a workflow |
| `create-trigger.js` | Create a trigger |
| `update-trigger.js` | Enable/disable a trigger |
| `delete-trigger.js` | Delete a trigger |
| `list-whatsapp-phone-numbers.js` | List phone numbers for trigger setup |

### Executions

| Script | Purpose |
|--------|---------|
| `list-executions.js` | List executions |
| `get-execution.js` | Get execution details |
| `get-context-value.js` | Read value from execution context |
| `update-execution-status.js` | Force execution state |
| `resume-execution.js` | Resume waiting execution |
| `list-execution-events.js` | List execution events |

### Functions

| Script | Purpose |
|--------|---------|
| `list-functions.js` | List project functions |
| `get-function.js` | Get function details + code |
| `create-function.js` | Create a function |
| `update-function.js` | Update function code |
| `deploy-function.js` | Deploy function to runtime |
| `invoke-function.js` | Invoke function with payload |
| `list-function-invocations.js` | List function invocations |

### App integrations

| Script | Purpose |
|--------|---------|
| `list-apps.js` | Search integration apps |
| `search-actions.js` | Search actions (action_id = key) |
| `get-action-schema.js` | Get action JSON schema |
| `list-accounts.js` | List connected accounts |
| `create-connect-token.js` | Create OAuth connect link |
| `configure-prop.js` | Resolve remote_options for a prop |
| `reload-props.js` | Reload dynamic props |
| `list-integrations.js` | List saved integrations |
| `create-integration.js` | Create an integration |
| `update-integration.js` | Update an integration |
| `delete-integration.js` | Delete an integration |

### Databases

| Script | Purpose |
|--------|---------|
| `list-tables.js` | List D1 tables |
| `get-table.js` | Get table schema + sample rows |
| `query-rows.js` | Query rows with filters |
| `create-row.js` | Create a row |
| `update-row.js` | Update rows |
| `upsert-row.js` | Upsert a row |
| `delete-row.js` | Delete rows |

### OpenAPI

| Script | Purpose |
|--------|---------|
| `openapi-explore.mjs` | Explore OpenAPI (search/op/schema/where) |

Install deps (once):
```bash
npm i
```

Examples:
```bash
node scripts/openapi-explore.mjs --spec workflows search "variables"
node scripts/openapi-explore.mjs --spec workflows op getWorkflowVariables
node scripts/openapi-explore.mjs --spec platform op queryDatabaseRows
```

## Notes

- Prefer file paths over inline JSON (`--definition-file`, `--code-file`)
- `action_id` is the same as `key` from `search-actions`
- `--account-id` uses `pipedream_account_id` from `list-accounts`
- Variable CRUD (`variables-set.js`, `variables-delete.js`) is blocked - Platform API doesn't support it
- Raw SQL execution is not supported via Platform API

## References

Read before editing:
- [references/graph-contract.md](references/graph-contract.md) - Graph schema, computed vs editable fields, lock_version
- [references/node-types.md](references/node-types.md) - Node types and config shapes
- [references/workflow-overview.md](references/workflow-overview.md) - Execution flow and states

Other references:
- [references/execution-context.md](references/execution-context.md) - Context structure and variable substitution
- [references/triggers.md](../../../core/security/QUARANTINE/incoming/repos/AutoGPT/docs/integrations/block_integrations/airtable/triggers.md) - Trigger types and setup
- [references/app-integrations.md](references/app-integrations.md) - App integration and variable_definitions
- [references/functions-reference.md](references/functions-reference.md) - Function management
- [references/functions-payloads.md](references/functions-payloads.md) - Payload shapes for functions
- [references/databases-reference.md](references/databases-reference.md) - Database operations

## Assets

| File | Description |
|------|-------------|
| `workflow-linear.json` | Minimal linear workflow |
| `workflow-decision.json` | Minimal branching workflow |
| `workflow-agent-simple.json` | Minimal agent workflow |
| `workflow-customer-support-intake-agent.json` | Customer support intake |
| `workflow-interactive-buttons-decide-function.json` | Interactive buttons + decide (function) |
| `workflow-interactive-buttons-decide-ai.json` | Interactive buttons + decide (AI) |
| `workflow-api-template-wait-agent.json` | API trigger + template + agent |
| `function-decide-route-interactive-buttons.json` | Function for button routing |
| `agent-app-integration-example.json` | Agent node with app integrations |

## Related skills

- `integrate-whatsapp` - Onboarding, webhooks, messaging, templates, flows
- `observe-whatsapp` - Debugging, logs, health checks

<!-- FILEMAP:BEGIN -->
```text
[automate-whatsapp file map]|root: .
|.:{package.json,SKILL.md}
|assets:{agent-app-integration-example.json,databases-example.json,function-decide-route-interactive-buttons.json,functions-example.json,workflow-agent-simple.json,workflow-api-template-wait-agent.json,workflow-customer-support-intake-agent.json,workflow-decision.json,workflow-interactive-buttons-decide-ai.json,workflow-interactive-buttons-decide-function.json,workflow-linear.json}
|references:{app-integrations.md,databases-reference.md,execution-context.md,function-contracts.md,functions-payloads.md,functions-reference.md,graph-contract.md,node-types.md,triggers.md,workflow-overview.md,workflow-reference.md}
|scripts:{configure-prop.js,create-connect-token.js,create-function.js,create-integration.js,create-row.js,create-trigger.js,create-workflow.js,delete-integration.js,delete-row.js,delete-trigger.js,deploy-function.js,edit-graph.js,get-action-schema.js,get-context-value.js,get-execution-event.js,get-execution.js,get-function.js,get-graph.js,get-table.js,get-workflow.js,invoke-function.js,list-accounts.js,list-apps.js,list-execution-events.js,list-executions.js,list-function-invocations.js,list-functions.js,list-integrations.js,list-provider-models.js,list-tables.js,list-triggers.js,list-whatsapp-phone-numbers.js,list-workflows.js,openapi-explore.mjs,query-rows.js,reload-props.js,resume-execution.js,search-actions.js,update-execution-status.js,update-function.js,update-graph.js,update-integration.js,update-row.js,update-trigger.js,update-workflow-settings.js,upsert-row.js,validate-graph.js,variables-delete.js,variables-list.js,variables-set.js}
|scripts/lib/databases:{args.js,filters.js,kapso-api.js}
|scripts/lib/functions:{args.js,kapso-api.js}
|scripts/lib/workflows:{args.js,kapso-api.js,result.js}
```
<!-- FILEMAP:END -->
```

## File: `skills/automate-whatsapp/package.json`
```json
{
  "private": true,
  "type": "module",
  "dependencies": {
    "yaml": "^2.6.0"
  },
  "scripts": {
    "openapi": "node scripts/openapi-explore.mjs"
  }
}
```

## File: `skills/automate-whatsapp/assets/agent-app-integration-example.json`
```json
{
  "integration_payload": {
    "action_id": "google_calendar-query-free-busy-calendars",
    "app_slug": "google_calendar",
    "account_id": "apn_example",
    "configured_props": {
      "calendarId": "{{calendar_id}}",
      "timeMin": "{{time_min}}",
      "timeMax": "{{time_max}}"
    },
    "variable_definitions": {
      "calendar_id": "string",
      "time_min": "string",
      "time_max": "string"
    }
  },
  "agent_node_config": {
    "node_type": "agent",
    "config": {
      "system_prompt": "Check calendar availability and book appointments.",
      "provider_model_id": "uuid",
      "max_iterations": 10,
      "temperature": 0.7,
      "flow_agent_app_integration_tools": [
        {
          "name": "check_calendar",
          "description": "Check availability in Google Calendar",
          "app_integration_id": "integration_uuid"
        }
      ],
      "flow_agent_webhooks": [],
      "flow_agent_mcp_servers": []
    }
  }
}
```

## File: `skills/automate-whatsapp/assets/databases-example.json`
```json
{
  "filters": {
    "status": "eq.active",
    "created_at": "gte.2025-01-01"
  },
  "data": {
    "phone": "+14155550123",
    "name": "Alicia",
    "status": "active"
  }
}
```

## File: `skills/automate-whatsapp/assets/function-decide-route-interactive-buttons.json`
```json
{
  "name": "decide-route-interactive-buttons",
  "description": "Decide node helper: route to the next edge based on vars.button_choice from an interactive button reply.",
  "code": "async function handler(request, env) {\n  const payload = await request.json();\n\n  const executionContext = payload && payload.execution_context ? payload.execution_context : {};\n  const vars = executionContext && executionContext.vars ? executionContext.vars : {};\n  const availableEdges = Array.isArray(payload && payload.available_edges) ? payload.available_edges : [];\n\n  const raw = vars.button_choice ?? vars.last_user_input;\n\n  function asString(value) {\n    if (typeof value === 'string') return value;\n    if (typeof value === 'number') return String(value);\n    if (value && typeof value === 'object') {\n      try {\n        return JSON.stringify(value);\n      } catch {\n        return null;\n      }\n    }\n    return null;\n  }\n\n  function extractChoice(value) {\n    if (!value) return null;\n\n    if (typeof value === 'string') {\n      const trimmed = value.trim();\n      if (trimmed.length === 0) return null;\n      return trimmed;\n    }\n\n    if (value && typeof value === 'object') {\n      const v = value;\n      const direct = v.button_id || v.buttonId || v.list_id || v.listId || v.id || v.choice || v.value;\n      if (typeof direct === 'string' && direct.trim().length > 0) return direct.trim();\n\n      // Common nested shapes.\n      const nested =\n        (v.interactive && (v.interactive.button_reply || v.interactive.list_reply)) ||\n        v.button_reply ||\n        v.list_reply;\n\n      if (nested && typeof nested === 'object') {\n        const nestedId = nested.id || nested.button_id || nested.list_id;\n        if (typeof nestedId === 'string' && nestedId.trim().length > 0) return nestedId.trim();\n      }\n    }\n\n    return null;\n  }\n\n  const extracted = extractChoice(raw);\n  const normalized = extracted ? extracted.toLowerCase().trim() : null;\n\n  // Map common variants to canonical edge labels.\n  const mapped = normalized === 'sale' ? 'sales' : normalized;\n\n  if (mapped && availableEdges.includes(mapped)) {\n    return new Response(JSON.stringify({ next_edge: mapped }), {\n      headers: { 'Content-Type': 'application/json' }\n    });\n  }\n\n  const fallback = availableEdges[0] || 'next';\n  const reason = {\n    extracted: extracted,\n    raw_preview: asString(raw),\n    available_edges: availableEdges\n  };\n\n  return new Response(JSON.stringify({ next_edge: fallback, vars: { decision_reason: reason } }), {\n    headers: { 'Content-Type': 'application/json' }\n  });\n}\n"
}

```

## File: `skills/automate-whatsapp/assets/functions-example.json`
```json
{
  "name": "webhook-handler",
  "description": "Store webhook payloads",
  "code": "async function handler(request, env) {\n  const payload = await request.json();\n  await env.DB.prepare(\"INSERT INTO webhook_logs (event, data) VALUES (?, ?)\").bind(payload.event, JSON.stringify(payload.data)).run();\n  return new Response(JSON.stringify({ success: true }), { headers: { 'Content-Type': 'application/json' } });\n}"
}
```

## File: `skills/automate-whatsapp/assets/workflow-agent-simple.json`
```json
{
  "nodes": [
    {
      "id": "start",
      "type": "flow-node",
      "position": { "x": 120, "y": 120 },
      "data": {
        "node_type": "start",
        "config": {}
      }
    },
    {
      "id": "agent_1710000100000",
      "type": "flow-node",
      "position": { "x": 120, "y": 320 },
      "data": {
        "node_type": "agent",
        "config": {
          "system_prompt": "You are a helpful assistant. Ask one clarifying question if needed, then call complete_task.",
          "provider_model_id": "PROVIDER_MODEL_ID_HERE",
          "max_iterations": 10,
          "temperature": 0.2
        }
      }
    }
  ],
  "edges": [
    { "source": "start", "target": "agent_1710000100000", "label": "next" }
  ]
}

```

## File: `skills/automate-whatsapp/assets/workflow-api-template-wait-agent.json`
```json
{
  "nodes": [
    {
      "id": "start",
      "type": "flow-node",
      "position": { "x": 120, "y": 120 },
      "data": {
        "node_type": "start",
        "config": {}
      }
    },
    {
      "id": "send_template_1710000500000",
      "type": "flow-node",
      "position": { "x": 120, "y": 320 },
      "data": {
        "node_type": "send_template",
        "config": {
          "template_id": "TEMPLATE_ID_HERE",
          "parameters": {
            "1": "{{vars.customer_name}}",
            "2": "{{vars.case_id}}"
          }
        }
      }
    },
    {
      "id": "wait_for_response_1710000504000",
      "type": "flow-node",
      "position": { "x": 120, "y": 520 },
      "data": {
        "node_type": "wait_for_response",
        "config": {
          "save_response_to": "user_reply"
        }
      }
    },
    {
      "id": "agent_1710000508000",
      "type": "flow-node",
      "position": { "x": 120, "y": 720 },
      "data": {
        "node_type": "agent",
        "config": {
          "system_prompt": "You are following up on a WhatsApp template message triggered by an API call. Use vars.case_id and vars.customer_name for context. The user's reply is in vars.user_reply. Resolve the request or gather the missing details. When complete, summarize and call complete_task.",
          "provider_model_id": "PROVIDER_MODEL_ID_HERE",
          "max_iterations": 20,
          "temperature": 0.2
        }
      }
    }
  ],
  "edges": [
    { "source": "start", "target": "send_template_1710000500000", "label": "next" },
    { "source": "send_template_1710000500000", "target": "wait_for_response_1710000504000", "label": "next" },
    { "source": "wait_for_response_1710000504000", "target": "agent_1710000508000", "label": "next" }
  ]
}

```

## File: `skills/automate-whatsapp/assets/workflow-customer-support-intake-agent.json`
```json
{
  "nodes": [
    {
      "id": "start",
      "type": "flow-node",
      "position": { "x": 120, "y": 120 },
      "data": {
        "node_type": "start",
        "config": {}
      }
    },
    {
      "id": "send_text_1710000200000",
      "type": "flow-node",
      "position": { "x": 120, "y": 320 },
      "data": {
        "node_type": "send_text",
        "config": {
          "message": "Thanks for reaching out. Please reply with your email and a short description of the issue.",
          "delay_seconds": 0
        }
      }
    },
    {
      "id": "wait_for_response_1710000204000",
      "type": "flow-node",
      "position": { "x": 120, "y": 520 },
      "data": {
        "node_type": "wait_for_response",
        "config": {
          "save_response_to": "support_intake"
        }
      }
    },
    {
      "id": "agent_1710000208000",
      "type": "flow-node",
      "position": { "x": 120, "y": 720 },
      "data": {
        "node_type": "agent",
        "config": {
          "system_prompt": "You are a customer support agent. The user's intake message is in vars.support_intake. Extract the email and issue summary. Ask concise follow-up questions if critical details are missing. When you have enough info, summarize the issue and call complete_task.",
          "provider_model_id": "PROVIDER_MODEL_ID_HERE",
          "max_iterations": 20,
          "temperature": 0.2
        }
      }
    }
  ],
  "edges": [
    { "source": "start", "target": "send_text_1710000200000", "label": "next" },
    { "source": "send_text_1710000200000", "target": "wait_for_response_1710000204000", "label": "next" },
    { "source": "wait_for_response_1710000204000", "target": "agent_1710000208000", "label": "next" }
  ]
}

```

## File: `skills/automate-whatsapp/assets/workflow-decision.json`
```json
{
  "nodes": [
    {
      "id": "start",
      "type": "flow-node",
      "position": { "x": 120, "y": 120 },
      "data": {
        "node_type": "start",
        "config": {}
      }
    },
    {
      "id": "send_text_1710000010000",
      "type": "flow-node",
      "position": { "x": 120, "y": 320 },
      "data": {
        "node_type": "send_text",
        "config": {
          "message": "Do you want to continue? Reply yes or no.",
          "delay_seconds": 0
        }
      }
    },
    {
      "id": "wait_for_response_1710000014000",
      "type": "flow-node",
      "position": { "x": 120, "y": 520 },
      "data": {
        "node_type": "wait_for_response",
        "config": {
          "save_response_to": "user_reply"
        }
      }
    },
    {
      "id": "decide_1710000018000",
      "type": "flow-node",
      "position": { "x": 120, "y": 720 },
      "data": {
        "node_type": "decide",
        "config": {
          "decision_type": "function",
          "function_id": "FUNCTION_ID_HERE",
          "conditions": [
            { "label": "yes", "description": "User agreed" },
            { "label": "no", "description": "User declined" }
          ]
        }
      }
    },
    {
      "id": "send_text_1710000022000",
      "type": "flow-node",
      "position": { "x": 0, "y": 920 },
      "data": {
        "node_type": "send_text",
        "config": {
          "message": "Great, let's continue!",
          "delay_seconds": 0
        }
      }
    },
    {
      "id": "send_text_1710000026000",
      "type": "flow-node",
      "position": { "x": 240, "y": 920 },
      "data": {
        "node_type": "send_text",
        "config": {
          "message": "No problem. Ending the workflow.",
          "delay_seconds": 0
        }
      }
    }
  ],
  "edges": [
    { "source": "start", "target": "send_text_1710000010000", "label": "next" },
    { "source": "send_text_1710000010000", "target": "wait_for_response_1710000014000", "label": "next" },
    { "source": "wait_for_response_1710000014000", "target": "decide_1710000018000", "label": "next" },
    { "source": "decide_1710000018000", "target": "send_text_1710000022000", "label": "yes" },
    { "source": "decide_1710000018000", "target": "send_text_1710000026000", "label": "no" }
  ]
}
```

## File: `skills/automate-whatsapp/assets/workflow-interactive-buttons-decide-ai.json`
```json
{
  "nodes": [
    {
      "id": "start",
      "type": "flow-node",
      "position": { "x": 120, "y": 120 },
      "data": {
        "node_type": "start",
        "config": {}
      }
    },
    {
      "id": "send_interactive_1710000400000",
      "type": "flow-node",
      "position": { "x": 120, "y": 320 },
      "data": {
        "node_type": "send_interactive",
        "config": {
          "interactive_type": "button",
          "body_text": "How can we help you today?",
          "buttons": [
            { "id": "sales", "title": "Sales" },
            { "id": "support", "title": "Support" }
          ]
        }
      }
    },
    {
      "id": "wait_for_response_1710000404000",
      "type": "flow-node",
      "position": { "x": 120, "y": 520 },
      "data": {
        "node_type": "wait_for_response",
        "config": {
          "save_response_to": "button_choice"
        }
      }
    },
    {
      "id": "decide_1710000408000",
      "type": "flow-node",
      "position": { "x": 120, "y": 720 },
      "data": {
        "node_type": "decide",
        "config": {
          "decision_type": "ai",
          "provider_model_id": "PROVIDER_MODEL_ID_HERE",
          "conditions": [
            { "label": "sales", "description": "User selected Sales (button id: sales)" },
            { "label": "support", "description": "User selected Support (button id: support)" }
          ],
          "llm_temperature": 0.0
        }
      }
    },
    {
      "id": "send_text_1710000412000",
      "type": "flow-node",
      "position": { "x": 0, "y": 920 },
      "data": {
        "node_type": "send_text",
        "config": {
          "message": "Got it - connecting you to Sales.",
          "delay_seconds": 0
        }
      }
    },
    {
      "id": "send_text_1710000416000",
      "type": "flow-node",
      "position": { "x": 240, "y": 920 },
      "data": {
        "node_type": "send_text",
        "config": {
          "message": "Got it - connecting you to Support.",
          "delay_seconds": 0
        }
      }
    }
  ],
  "edges": [
    { "source": "start", "target": "send_interactive_1710000400000", "label": "next" },
    { "source": "send_interactive_1710000400000", "target": "wait_for_response_1710000404000", "label": "next" },
    { "source": "wait_for_response_1710000404000", "target": "decide_1710000408000", "label": "next" },
    { "source": "decide_1710000408000", "target": "send_text_1710000412000", "label": "sales" },
    { "source": "decide_1710000408000", "target": "send_text_1710000416000", "label": "support" }
  ]
}

```

## File: `skills/automate-whatsapp/assets/workflow-interactive-buttons-decide-function.json`
```json
{
  "nodes": [
    {
      "id": "start",
      "type": "flow-node",
      "position": { "x": 120, "y": 120 },
      "data": {
        "node_type": "start",
        "config": {}
      }
    },
    {
      "id": "send_interactive_1710000300000",
      "type": "flow-node",
      "position": { "x": 120, "y": 320 },
      "data": {
        "node_type": "send_interactive",
        "config": {
          "interactive_type": "button",
          "body_text": "How can we help you today?",
          "buttons": [
            { "id": "sales", "title": "Sales" },
            { "id": "support", "title": "Support" }
          ]
        }
      }
    },
    {
      "id": "wait_for_response_1710000304000",
      "type": "flow-node",
      "position": { "x": 120, "y": 520 },
      "data": {
        "node_type": "wait_for_response",
        "config": {
          "save_response_to": "button_choice"
        }
      }
    },
    {
      "id": "decide_1710000308000",
      "type": "flow-node",
      "position": { "x": 120, "y": 720 },
      "data": {
        "node_type": "decide",
        "config": {
          "decision_type": "function",
          "function_id": "FUNCTION_ID_HERE",
          "conditions": [
            { "label": "sales", "description": "User selected Sales" },
            { "label": "support", "description": "User selected Support" }
          ]
        }
      }
    },
    {
      "id": "send_text_1710000312000",
      "type": "flow-node",
      "position": { "x": 0, "y": 920 },
      "data": {
        "node_type": "send_text",
        "config": {
          "message": "Got it - connecting you to Sales.",
          "delay_seconds": 0
        }
      }
    },
    {
      "id": "send_text_1710000316000",
      "type": "flow-node",
      "position": { "x": 240, "y": 920 },
      "data": {
        "node_type": "send_text",
        "config": {
          "message": "Got it - connecting you to Support.",
          "delay_seconds": 0
        }
      }
    }
  ],
  "edges": [
    { "source": "start", "target": "send_interactive_1710000300000", "label": "next" },
    { "source": "send_interactive_1710000300000", "target": "wait_for_response_1710000304000", "label": "next" },
    { "source": "wait_for_response_1710000304000", "target": "decide_1710000308000", "label": "next" },
    { "source": "decide_1710000308000", "target": "send_text_1710000312000", "label": "sales" },
    { "source": "decide_1710000308000", "target": "send_text_1710000316000", "label": "support" }
  ]
}

```

## File: `skills/automate-whatsapp/assets/workflow-linear.json`
```json
{
  "nodes": [
    {
      "id": "start",
      "type": "flow-node",
      "position": { "x": 120, "y": 120 },
      "data": {
        "node_type": "start",
        "config": {}
      }
    },
    {
      "id": "send_text_1710000000000",
      "type": "flow-node",
      "position": { "x": 120, "y": 320 },
      "data": {
        "node_type": "send_text",
        "config": {
          "message": "Hello! What's your name?",
          "delay_seconds": 0
        }
      }
    },
    {
      "id": "wait_for_response_1710000005000",
      "type": "flow-node",
      "position": { "x": 120, "y": 520 },
      "data": {
        "node_type": "wait_for_response",
        "config": {
          "save_response_to": "user_name"
        }
      }
    },
    {
      "id": "send_text_1710000009000",
      "type": "flow-node",
      "position": { "x": 120, "y": 720 },
      "data": {
        "node_type": "send_text",
        "config": {
          "message": "Nice to meet you, {{vars.user_name}}!",
          "delay_seconds": 0
        }
      }
    }
  ],
  "edges": [
    { "source": "start", "target": "send_text_1710000000000", "label": "next" },
    { "source": "send_text_1710000000000", "target": "wait_for_response_1710000005000", "label": "next" },
    { "source": "wait_for_response_1710000005000", "target": "send_text_1710000009000", "label": "next" }
  ]
}
```

## File: `skills/automate-whatsapp/references/app-integrations.md`
```markdown
# App Integrations (Workflow Nodes and Agent Tools)

Use these when you need to call external apps (Slack, HubSpot, Sheets, etc).

## Step 1: Accounts

1. List connected accounts:
   - `scripts/list-accounts.js --app-slug <slug>`
   - Use `accounts[].pipedream_account_id` for any `--account-id` flag.
2. If no account exists, generate a connect link:
   - `scripts/create-connect-token.js --app-slug <slug>`
3. Ask the user to open the connect URL and finish OAuth, then re-run list-accounts.

## Action discovery notes

- `action_id` is the same as the action `key` returned by `search-actions`.
- Prefer one-word queries (ex: `calendar`, `slack`, `hubspot`) and then filter by `app_slug`.
- If a multi-word query returns nothing, retry with a single token.

## Inputs and variable_definitions (required for agent tools)

App integration tools only accept inputs defined by `variable_definitions`. These inputs are mapped into
`configured_props` using `{{placeholders}}`.

Rules:
- Every placeholder in `configured_props` becomes a required tool input.
- If `variable_definitions` is omitted, Kapso infers variable names from `{{placeholders}}`
  and treats them as `string`.
- Agent tool calls must pass an `input` object with these variables.

Example configured props:
```json
{
  "calendarId": "{{calendar_id}}",
  "timeMin": "{{time_min}}",
  "timeMax": "{{time_max}}"
}
```

Example variable definitions:
```json
{
  "calendar_id": "string",
  "time_min": "string",
  "time_max": "string"
}
```

Create integration with explicit variable definitions:
```bash
node scripts/create-integration.js \
  --action-id "google_calendar-query-free-busy-calendars" \
  --app-slug "google_calendar" \
  --account-id "<pipedream_account_id>" \
  --configured-props '{"calendarId":"{{calendar_id}}","timeMin":"{{time_min}}","timeMax":"{{time_max}}"}' \
  --variable-definitions '{"calendar_id":"string","time_min":"string","time_max":"string"}'
```

Example asset: `assets/agent-app-integration-example.json`

## Step 2: Choose integration path

### Option A: Pipedream node (workflow graph)

1. Search actions: `scripts/search-actions.js --query "slack" --app-slug slack`
2. Get schema: `scripts/get-action-schema.js --action-id <id>`
3. For remote options: `scripts/configure-prop.js --action-id <id> --prop-name <name> --account-id <pipedream_account_id>`
4. For dynamic props: `scripts/reload-props.js --action-id <id> --account-id <pipedream_account_id>`
5. Add a `pipedream` node to the graph with action_id, app_slug, account_id, configured_props.

### Option B: Agent app integration tool (preferred for agent nodes)

1. List existing integrations: `scripts/list-integrations.js`
2. If none, create one:
   - `scripts/create-integration.js --action-id <id> --app-slug <slug> --account-id <pipedream_account_id> --configured-props <json>`
3. Use the integration id in `flow_agent_app_integration_tools` on the agent node.

### Option C: Integration via webhook

Use only when calling from a webhook node or agent webhook tool.

1. Create integration (same as Option B).
2. Call:
   - `https://app.kapso.ai/api/v1/integrations/{integration_id}/invoke`

Rules:
- Prefer Option B for agent nodes.
- Pipedream URLs do not work in webhook nodes or agent webhook tools.
- Always get action_id from search-actions; do not guess.
```

## File: `skills/automate-whatsapp/references/databases-reference.md`
```markdown
# Database Filters Reference

Use PostgREST-style filters as query parameters.

## Operators

- `eq`: equals (`status=eq.active`)
- `neq`: not equal (`status=neq.inactive`)
- `gt`: greater than (`age=gt.18`)
- `gte`: greater or equal (`age=gte.18`)
- `lt`: less than (`price=lt.100`)
- `lte`: less or equal (`price=lte.100`)
- `like`: pattern match (`name=like.%john%`)
- `in`: list match (`status=in.(active,pending)`)
- `is.null`: is null (`deleted_at=is.null`)

## Common patterns

- Select columns: `?select=id,name,email`
- Order: `?order=created_at.desc`
- Pagination: `?limit=20&offset=40`
```

## File: `skills/automate-whatsapp/references/execution-context.md`
```markdown
# Execution Context and Variables

Execution context shape:

```json
{
  "vars": { "user_name": "Alice" },
  "system": { "flow_id": "uuid", "flow_name": "...", "trigger_type": "inbound_message" },
  "context": { "channel": "whatsapp", "phone_number": "+1234567890", "contact": { "wa_id": "...", "profile_name": "..." } },
  "metadata": { "request": { "ip": "...", "timestamp": "..." } }
}
```

Always use this structure:
- `vars`: user-defined variables
- `system`: system variables (flow_id, trigger_type, etc)
- `context`: channel info (phone number, contact)
- `metadata`: request metadata

## Variable syntax

Environment variables (secrets):
- `${ENV:VARIABLE_NAME}`

Runtime variables:
- `{{vars.my_variable}}`
- `{{system.flow_name}}`
- `{{context.phone_number}}`

Substitution order:
1. Environment variables
2. Runtime variables

Important WhatsApp keys:
- `{{system.whatsapp_config.phone_number_id}}` (Meta phone_number_id)
- `{{system.trigger_whatsapp_config_id}}` (Kapso WhatsApp config id)
- `{{context.phone_number}}` (recipient phone)

Never guess variable paths. Use:
- `scripts/variables-list.js <workflow-id>`
- `scripts/get-execution.js <execution-id>`
- `scripts/get-context-value.js <execution-id> --variable-path <path>`
```

## File: `skills/automate-whatsapp/references/function-contracts.md`
```markdown
# Workflow Function Contracts

Use this when configuring function or decide nodes.

## Code rules (must follow)

- Code MUST start with: `async function handler(request, env) {`
- Do NOT use `export`, `export default`, or arrow functions.
- Output only JavaScript source code (no markdown fences).

## Payload (function/decide nodes)

```json
{
  "execution_context": { "vars": {}, "system": {}, "context": {}, "metadata": {} },
  "available_edges": ["edge_a", "edge_b"],
  "flow_events": [{ "event_type": "...", "payload": {} }]
}
```

## Function node response

Return variables to merge:

```json
{ "vars": { "processed": true } }
```

## Decide node response

Return `next_edge` matching an outgoing edge label:

```json
{ "next_edge": "qualified", "vars": { "decision_reason": "qualified" } }
```

Always fall back to the first available edge if unsure.

## Agent Function Tool

Agent node function tools receive:

```json
{
  "input": { "any": "shape" },
  "execution_context": { "vars": {}, "system": {}, "context": {}, "metadata": {} },
  "flow_events": [],
  "flow_info": { "id": "uuid", "name": "...", "step_id": "uuid" },
  "whatsapp_context": { "conversation": {}, "messages": [] }
}
```

For full runtime contract details, load:
- `functions-reference.md`
- `functions-payloads.md`
```

## File: `skills/automate-whatsapp/references/functions-payloads.md`
```markdown
# Payload Shapes (Quick Reference)

## Workflow function node (request)

Kapso sends:

```json
{
  "execution_context": {
    "vars": { "user_name": "John", "score": 42 },
    "system": { "flow_id": "uuid", "flow_name": "...", "trigger_type": "inbound_message" },
    "context": { "channel": "whatsapp", "phone_number": "+1234567890", "contact": { "wa_id": "...", "profile_name": "..." } },
    "metadata": { "request": { "ip": "...", "timestamp": "..." } }
  },
  "available_edges": ["edge_a", "edge_b"],
  "flow_events": [{ "event_type": "...", "payload": { "...": "..." } }]
}
```

### Function node response

Return vars to merge:

```json
{ "vars": { "processed": true, "result": "ok" } }
```

## Workflow decide node (request)

Same request shape as function nodes.

### Decide node response

Return `next_edge` that matches an outgoing edge label:

```json
{ "next_edge": "qualified", "vars": { "decision_reason": "qualified" } }
```

Always fall back to the first available edge if unsure.

## Agent function tool (request)

```json
{
  "input": { "any": "shape" },
  "execution_context": { "vars": {}, "system": {}, "context": {}, "metadata": {} },
  "flow_events": [{ "event_type": "...", "payload": { "...": "..." } }],
  "flow_info": { "id": "uuid", "name": "...", "step_id": "uuid" },
  "whatsapp_context": { "conversation": { "...": "..." }, "messages": [] }
}
```

## WhatsApp Flow data endpoint (request)

Kapso forwards:

```json
{
  "source": "whatsapp_flow",
  "flow": { "id": "<uuid>", "meta_flow_id": "<meta_id>" },
  "data_exchange": {
    "action": "INIT" | "data_exchange" | "BACK",
    "screen": "CURRENT_SCREEN_ID",
    "data": { "...": "..." },
    "flow_token": "opaque-token"
  },
  "signature_valid": true,
  "received_at": "2024-01-01T00:00:00Z"
}
```

### WhatsApp Flow response

```json
{
  "version": "3.0",
  "screen": "NEXT_SCREEN_ID",
  "data": {}
}
```

## Code rules

- Code MUST start with: `async function handler(request, env) {`
- Do NOT use `export`, `export default`, or arrow functions.
- Output only JavaScript source code (no markdown fences).
```

## File: `skills/automate-whatsapp/references/functions-reference.md`
```markdown
# Function Runtime Contract

## Handler signature

Functions must start with:

```
async function handler(request, env) {
```

Do not use `export` or arrow functions. Return a `Response` object.

## Runtime APIs

- `request`: Fetch API Request; use `await request.json()` for JSON.
- `env.DB`: D1 database access (if enabled for the project).
- `env.KV`: KV storage with `.get(key)`, `.put(key, value)`, `.delete(key)`.
- `env.SECRET_NAME`: Secrets configured in the function settings.

## Typical workflow

1. Create function with `code` that follows the contract.
2. Deploy the function (required before use).
3. Use the returned `function_url` for webhook destinations.

## Platform API payload envelope

When calling the Platform API directly (not via scripts), wrap attributes under `function`:

```json
{ "function": { "name": "...", "description": "...", "code": "..." } }
```

## Workflow node payload (Function / Decide)

When a workflow function node runs, Kapso sends:

```json
{
  "execution_context": {
    "vars": { "user_name": "John", "score": 42 },
    "system": { "flow_id": "uuid", "flow_name": "...", "trigger_type": "inbound_message" },
    "context": { "channel": "whatsapp", "phone_number": "+1234567890", "contact": { "wa_id": "...", "profile_name": "..." } },
    "metadata": { "request": { "ip": "...", "timestamp": "..." } }
  },
  "available_edges": ["edge_a", "edge_b"],
  "flow_events": [{ "event_type": "...", "payload": { "..." : "..." } }]
}
```

Execution context structure is always:
- `vars`: user-defined variables
- `system`: system variables (flow_id, trigger_type, etc)
- `context`: channel data (phone number, contact)
- `metadata`: request metadata

### Function node response

Return `vars` to update context:

```json
{
  "vars": { "processed": true, "result": "ok" }
}
```

### Decide node response

Return `next_edge` that matches an outgoing edge label:

```json
{
  "next_edge": "qualified",
  "vars": { "decision_reason": "qualified" }
}
```

Always fall back to the first available edge when unsure.

## Agent function tool payload

If an agent node uses a Function Tool, Kapso calls the function with:

```json
{
  "input": { "any": "shape" },
  "execution_context": { "vars": {}, "system": {}, "context": {}, "metadata": {} },
  "flow_events": [{ "event_type": "...", "payload": { "...": "..." } }],
  "flow_info": { "id": "uuid", "name": "...", "step_id": "uuid" },
  "whatsapp_context": { "conversation": { "...": "..." }, "messages": [] }
}
```

The tool expects a standard JSON response; you may return `vars` as above.

## WhatsApp Flow data endpoint payload

For WhatsApp Flow data endpoints, Kapso forwards:

```json
{
  "source": "whatsapp_flow",
  "flow": { "id": "<uuid>", "meta_flow_id": "<meta_id>" },
  "data_exchange": {
    "action": "INIT" | "data_exchange" | "BACK",
    "screen": "CURRENT_SCREEN_ID",
    "data": { "...": "..." },
    "flow_token": "opaque-token"
  },
  "signature_valid": true,
  "received_at": "2024-01-01T00:00:00Z"
}
```

Respond with:

```json
{
  "version": "3.0",
  "screen": "NEXT_SCREEN_ID",
  "data": {}
}
```

For full Flow JSON details and gotchas, load:
- `../integrate-whatsapp/references/whatsapp-flows-spec.md`

## Best practices

- Guard access: `const vars = body.execution_context?.vars || {};`
- Do not mutate `execution_context` in place; return new `vars`.
- Use try/catch for external API calls.
- Keep responses under the Meta timeout (10-15s).
```

## File: `skills/automate-whatsapp/references/graph-contract.md`
```markdown
# Workflow Graph Contract (Workflows / Definition)

This document is the source of truth for editing Kapso workflow graphs over the Platform API.

## Endpoints and envelopes

- Fetch graph (definition): `GET /platform/v1/workflows/:id/definition`
  - Returns a workflow record that includes `definition` (nodes + edges).
- Fetch metadata: `GET /platform/v1/workflows/:id`
  - Returns workflow metadata (including `lock_version`) but does NOT include `definition`.
- Update graph/settings: `PATCH /platform/v1/workflows/:id`
  - Send `workflow: { ... }` (what the scripts use). `flow: { ... }` is accepted as an alias.
  - To update the graph, send `workflow: { definition: <definition> }`.

## Two graph shapes: returned vs editable

### Shape returned by get-graph (ReactFlow-style)

`GET /workflows/:id/definition` returns a ReactFlow-style definition that includes extra/computed fields:

```json
{
  "nodes": [
    {
      "id": "start",
      "type": "flow-node",
      "position": { "x": 120, "y": 120 },
      "data": { "node_type": "start", "config": {}, "display_name": "Start" }
    }
  ],
  "edges": [
    {
      "id": "uuid",
      "source": "start",
      "target": "send_text_1710000000000",
      "label": "next",
      "type": "default",
      "flow_condition_id": null
    }
  ]
}
```

### Minimal editable shape accepted by the API

For `PATCH /workflows/:id`, the minimal shape you should edit and send is:

```json
{
  "nodes": [
    {
      "id": "start",
      "position": { "x": 120, "y": 120 },
      "data": { "node_type": "start", "config": {} }
    },
    {
      "id": "send_text_1710000000000",
      "position": { "x": 120, "y": 320 },
      "data": {
        "node_type": "send_text",
        "config": { "message": "Hello!", "delay_seconds": 0 }
      }
    }
  ],
  "edges": [
    { "source": "start", "target": "send_text_1710000000000", "label": "next" }
  ]
}
```

The API ignores/strips extra fields like `node.type`, `data.display_name`, `edge.id`, and `edge.type`. You can keep them unchanged when roundtripping, but do not rely on editing them.

## Nodes

Required:
- `node.id` (string)
- `node.position.x`, `node.position.y` (numbers)
- `node.data.node_type` (string)
- `node.data.config` (object; per node_type)

Rules:
- Exactly one start node with `id = "start"` and `data.node_type = "start"`.
- Never change existing node IDs.
- For new nodes: use `{node_type}_{timestamp_ms}` for the `id`.

Footgun (important):
- If `data.node_type` is missing, the backend defaults it to `"start"`.
- If you create a node with an unknown `data.node_type`, the backend will create it as a start-like step.
- Always validate before updating: `node scripts/validate-graph.js --definition-file <path>` and treat warnings as blockers.

## Edges

Required:
- `edge.source` (existing node id)
- `edge.target` (existing node id)
- `edge.label` (string)

Rules:
- Non-decide nodes: 0 or 1 outgoing edge; if present, its `label` must be `"next"`.
- Decide nodes: one outgoing edge per condition; each edge `label` must match `config.conditions[].label`.

Optional:
- `edge.flow_condition_id` (only meaningful for decide edges). If present, it must refer to a condition on that decide node.

## Decide node conditions (ids)

For `decide` nodes, `config.conditions[]` controls valid outgoing edge labels.

- When creating NEW conditions, do not include an `id` field (the backend generates it).
- When editing an EXISTING decide node fetched from the API, you may see `conditions[].id` and `edges[].flow_condition_id` in the returned graph. Keep them unchanged unless you have a specific reason to remove/rebuild the decide node.

## Computed vs editable fields

Do edit:
- `node.position`
- `node.data.node_type`
- `node.data.config`
- `edge.source`, `edge.target`, `edge.label`

Do NOT treat as editable (computed/ignored/unstable):
- `node.data.display_name`
- `edge.id`, `edge.type`
- any `*_name` fields (model names, function names, etc.)

## Terminal nodes and agent nodes

- Terminal nodes (leaf nodes) are allowed. A node with no outgoing edge ends the workflow after that step completes.
- Agent nodes can be terminal or can continue via a `"next"` edge, depending on what you want:
  - Terminal agent: the agent handles the conversation and finishes via its tools (ex: complete_task or handoff_to_human).
  - Continuing agent: add a `"next"` edge if you want deterministic post-agent steps (ex: send_text summary).

## lock_version conflicts (exact retry pattern)

The Platform API does not currently enforce `lock_version` for definition updates, so the scripts do a precheck.

Use this pattern:
1. Fetch graph and lock_version: `node scripts/get-graph.js <workflow_id>`
2. Apply change with lock precheck:
   - Small surgical edit: `node scripts/edit-graph.js <workflow_id> --expected-lock-version <n> ...`
   - Full update: `node scripts/update-graph.js <workflow_id> --expected-lock-version <n> --definition-file <path>`
     - `update-graph.js` can extract `definition` from wrapper JSON, but prefer sending just the `definition` object.
3. If you get a conflict error:
   - Re-fetch the latest graph to get the new lock_version.
   - Re-apply your change on top of the latest definition.
   - Retry with the new expected lock version.
```

## File: `skills/automate-whatsapp/references/node-types.md`
```markdown
# Workflow Node Types

## Supported node_type values

These are the `data.node_type` values supported by the Platform API and validated by `scripts/validate-graph.js`:

- `start`
- `send_text`
- `send_template`
- `send_interactive`
- `wait_for_response`
- `set_variable`
- `decide`
- `call`
- `webhook`
- `pipedream`
- `function`
- `agent`
- `handoff`

Messaging nodes are `send_text`, `send_template`, and `send_interactive`.

Node structure:

```json
{
  "id": "send_text_1710000000000",
  "type": "flow-node",
  "position": { "x": 300, "y": 100 },
  "data": {
    "node_type": "send_text",
    "config": {},
    "display_name": "Send Text"
  }
}
```

Notes:
- `display_name` is computed by the backend and is not reliably editable.
- New node IDs should use `{node_type}_{timestamp_ms}`.
- Nodes connect from bottom to top; organize the graph vertically (top-down) rather than left-to-right.

## start

```json
{ "node_type": "start", "config": {} }
```

Exactly one start node per workflow, id must be `start`.

## send_text

```json
{ "node_type": "send_text", "config": { "message": "Hello {{vars.name}}!", "delay_seconds": 0 } }
```

Optional: `whatsapp_config_id`, `to_phone_number`.

## send_template

```json
{
  "node_type": "send_template",
  "config": {
    "template_id": "uuid",
    "parameters": { "1": "{{vars.name}}" }
  }
}
```

Optional: `whatsapp_config_id`, `to_phone_number`.
Use the `integrate-whatsapp` skill to find template IDs and parameter formats.

## send_interactive (buttons)

```json
{
  "node_type": "send_interactive",
  "config": {
    "interactive_type": "button",
    "body_text": "Choose an option:",
    "buttons": [
      { "id": "yes", "title": "Yes" },
      { "id": "no", "title": "No" }
    ]
  }
}
```

Max 3 buttons; id + title required (title max 20 chars).

## send_interactive (list)

```json
{
  "node_type": "send_interactive",
  "config": {
    "interactive_type": "list",
    "body_text": "Select:",
    "list_button_text": "View options",
    "list_sections": [
      { "title": "Section", "rows": [{ "id": "opt1", "title": "Option 1" }] }
    ]
  }
}
```

## send_interactive (cta_url)

```json
{
  "node_type": "send_interactive",
  "config": {
    "interactive_type": "cta_url",
    "body_text": "Visit our site",
    "cta_display_text": "Open",
    "cta_url": "https://example.com"
  }
}
```

## send_interactive (flow)

```json
{
  "node_type": "send_interactive",
  "config": {
    "interactive_type": "flow",
    "body_text": "Open calendar",
    "flow_id": "<META_FLOW_ID>",
    "flow_cta": "Open",
    "flow_action": "navigate",
    "flow_action_payload": { "screen": "FIRST_SCREEN" }
  }
}
```

Notes:
- `flow_id` is the Meta Flow ID (string).
- `flow_action_payload.screen` must be a valid first screen.

## wait_for_response

```json
{ "node_type": "wait_for_response", "config": { "save_response_to": "user_reply" } }
```

Saves the next message into `vars.user_reply`.

## set_variable

```json
{
  "node_type": "set_variable",
  "config": {
    "variable_name": "customer_name",
    "variable_value": "{{vars.user_reply}}",
    "value_type": "string"
  }
}
```

Notes:
- Use `value_type: "string"` unless you have a specific reason to store a different type.

## decide (AI routing)

```json
{
  "node_type": "decide",
  "config": {
    "decision_type": "ai",
    "provider_model_id": "uuid",
    "conditions": [
      { "label": "interested", "description": "User shows interest" },
      { "label": "not_interested", "description": "User declines" }
    ]
  }
}
```

## decide (function routing)

```json
{
  "node_type": "decide",
  "config": {
    "decision_type": "function",
    "function_id": "uuid",
    "conditions": [
      { "label": "yes", "description": "Approved" },
      { "label": "no", "description": "Rejected" }
    ]
  }
}
```

Rules:
- Outgoing edge labels must match `conditions[].label`.
- When creating new conditions, do not include an `id` field.

## call (subworkflow)

```json
{ "node_type": "call", "config": { "workflow_id": "uuid", "save_error_to": "subflow_error" } }
```

## webhook

```json
{
  "node_type": "webhook",
  "config": {
    "url": "https://api.example.com/endpoint",
    "method": "POST",
    "headers": { "Authorization": "Bearer {{vars.token}}" },
    "body_template": { "phone": "{{context.phone_number}}" },
    "save_response_to": "api_result"
  }
}
```

`headers` and `body_template` must be valid JSON objects.

## pipedream (apps)

```json
{
  "node_type": "pipedream",
  "config": {
    "action_id": "slack-send_message_to_channel",
    "app_slug": "slack",
    "account_id": "apn_example",
    "configured_props": {
      "channel": "#general",
      "text": "Hello {{vars.user_name}}!"
    },
    "dynamic_props_id": "dp_optional",
    "save_response_to": "app_result"
  }
}
```

Notes:
- Use `references/app-integrations.md` for how to find `action_id`, `account_id`, and build `configured_props`.
- `configured_props` may include `{{vars.*}}`, `{{system.*}}`, `{{context.*}}` runtime variables.

## function

```json
{ "node_type": "function", "config": { "function_id": "uuid", "save_response_to": "fn_result" } }
```

Use `automate-whatsapp` function scripts to find function IDs and update code.

## agent

```json
{
  "node_type": "agent",
  "config": {
    "system_prompt": "You are a helpful assistant...",
    "provider_model_id": "uuid",
    "max_iterations": 10,
    "temperature": 0.7
  }
}
```

Notes:
- `provider_model_id` is required. Use `scripts/list-provider-models.js` to find it.
- Agent tool arrays live inside `data.config` (not at the `data` root).

Default tools (toggle on/off only):
- complete_task (required)
- handoff_to_human (required)
- send_notification_to_user
- send_media
- get_execution_metadata
- get_whatsapp_context
- get_current_datetime
- save_variable
- get_variable
- ask_about_file

Custom tools:
- `flow_agent_app_integration_tools[]` (app integrations)
- `flow_agent_webhooks[]` (webhook tools)
- `flow_agent_mcp_servers[]` (MCP tools)

### Agent tools: exact placement and structure

All tool arrays go under `data.config` of the agent node:

```json
{
  "id": "agent_1730000000000",
  "type": "flow-node",
  "position": { "x": 120, "y": 320 },
  "data": {
    "node_type": "agent",
    "config": {
      "system_prompt": "You can schedule appointments and use calendar tools.",
      "provider_model_id": "uuid",
      "max_iterations": 10,
      "temperature": 0.7,
      "flow_agent_app_integration_tools": [],
      "flow_agent_webhooks": [],
      "flow_agent_mcp_servers": []
    }
  }
}
```

Example asset: `assets/agent-app-integration-example.json`

#### App integration tools (preferred for agent nodes)

Use pre-configured integrations and attach them as tools:

```json
{
  "flow_agent_app_integration_tools": [
    {
      "name": "check_calendar",
      "description": "Check availability in Google Calendar",
      "app_integration_id": "integration_uuid"
    }
  ]
}
```

Rules:
- `app_integration_id` is the integration UUID from `scripts/list-integrations.js`.
- Do not include headers or URLs here; the integration handles auth.
- Inputs are defined by the integration's `variable_definitions` (or `{{placeholders}}`).

Tool input payload (runtime):
```json
{
  "input": {
    "calendar_id": "primary",
    "time_min": "2025-01-01T10:00:00Z",
    "time_max": "2025-01-01T12:00:00Z"
  }
}
```

#### Webhook tools (custom HTTP tools)

Use when the agent needs to call arbitrary HTTP endpoints:

```json
{
  "flow_agent_webhooks": [
    {
      "name": "lookup_customer",
      "description": "Fetch customer data from internal API",
      "url": "https://api.example.com/customers/lookup",
      "http_method": "POST",
      "headers": {
        "Authorization": "Bearer {{vars.api_token}}",
        "Content-Type": "application/json"
      },
      "body": {
        "phone_number": "{{context.phone_number}}"
      },
      "body_schema": {
        "type": "object",
        "properties": {
          "phone_number": { "type": "string" }
        },
        "required": ["phone_number"]
      },
      "jmespath_query": null
    }
  ]
}
```

Rules:
- `body_schema` must be valid JSON Schema.
- `headers` and `body` must be JSON objects (not strings).
- Tool inputs are defined by `body_schema` and are sent as the webhook JSON body.

#### MCP server tools

Use to attach MCP servers the agent can call:

```json
{
  "flow_agent_mcp_servers": [
    {
      "name": "files",
      "description": "Local file access",
      "url": "https://mcp.example.com",
      "headers": {
        "Authorization": "Bearer {{vars.mcp_token}}"
      }
    }
  ]
}
```

Rules:
- `url` is required.
- `headers` must be a JSON object.
- MCP tool inputs are defined by the MCP server's tool schemas (not configured here).

## handoff

```json
{ "node_type": "handoff", "config": {} }
```

Ends execution and flags for human takeover.

## AI Fields (dynamic content)

Set a field to `{"$ai":{}}` and add `ai_field_config`:

```json
{
  "message": { "$ai": {} },
  "provider_model_id": "uuid",
  "ai_field_config": {
    "message": { "mode": "prompt", "prompt": "Write a greeting for {{vars.name}}" }
  }
}
```
```

## File: `skills/automate-whatsapp/references/triggers.md`
```markdown
# Workflow Triggers

Triggers are separate from the workflow graph. Do not store triggers in `workflow_graph`.

Trigger types:
- `inbound_message`: fires on WhatsApp message (requires `phone_number_id`).
- `api_call`: fires via Platform API.
- `whatsapp_event`: fires on WhatsApp events (requires `event`, optional `phone_number_id`).

Use these scripts:
- `scripts/list-triggers.js <workflow-id>`
- `scripts/create-trigger.js <workflow-id> --trigger-type <inbound_message|api_call|whatsapp_event> ...`
- `scripts/update-trigger.js --trigger-id <id> --active true|false`
- `scripts/delete-trigger.js --trigger-id <id>`
- `scripts/list-whatsapp-phone-numbers.js` (to find `phone_number_id`)

Notes:
- For inbound message triggers, use `phone_number_id` (Meta ID).
- For whatsapp_event triggers, use `event` like `whatsapp.message.delivered`.
- For API triggers, no extra fields are required.
```

## File: `skills/automate-whatsapp/references/workflow-overview.md`
```markdown
# Workflow Overview

## Key behaviors

- Workflows are automation graphs; an execution moves node-to-node until it waits or ends.
- Trigger inbound_message: if a non-observer execution is running or waiting for that conversation, the message routes to it. If in handoff, workflow processing is skipped. Otherwise, a new execution starts.
- Trigger api_call: starts an execution from the API; context channel is api.
- Trigger whatsapp_event: starts an observer execution for each matching event; observer executions are read-only by default (allow_outbound: false).

## Execution states

- running: processing steps.
- waiting: paused waiting for user input (wait_for_response or agent nodes).
- handoff: halted for human takeover; automation does not process inbound messages.
- ended: terminal success.
- failed: terminal error; error_details recorded.

Valid transitions:
- running -> waiting | ended | failed | handoff
- waiting -> running | ended | failed | handoff
- handoff -> running | ended | failed
- ended/failed have no transitions
```

## File: `skills/automate-whatsapp/references/workflow-reference.md`
```markdown
# Reference

## Overview

This skill manages workflow graphs, triggers, executions, and app integrations over the Platform API and provides local graph validation. Variables CRUD is not supported and will return blocked responses.

## Environment

Required env vars:

- `KAPSO_API_BASE_URL` (host only, no `/platform/v1`, example: `https://api.kapso.ai`)
- `KAPSO_API_KEY`

## Scripts

Each script is a single operation. Run with `node` or `bun`.

- `scripts/get-graph.js`
- `scripts/list-workflows.js`
- `scripts/get-workflow.js`
- `scripts/create-workflow.js`
- `scripts/update-workflow-settings.js`
- `scripts/edit-graph.js`
- `scripts/update-graph.js`
- `scripts/validate-graph.js`
- `scripts/list-triggers.js`
- `scripts/create-trigger.js`
- `scripts/update-trigger.js`
- `scripts/delete-trigger.js`
- `scripts/list-executions.js`
- `scripts/get-execution.js`
- `scripts/get-context-value.js`
- `scripts/update-execution-status.js`
- `scripts/resume-execution.js`
- `scripts/variables-list.js`
- `scripts/variables-set.js` (blocked)
- `scripts/variables-delete.js` (blocked)
- `scripts/list-provider-models.js`
- `scripts/list-execution-events.js`
- `scripts/get-execution-event.js`
- `scripts/list-apps.js`
- `scripts/search-actions.js`
- `scripts/get-action-schema.js`
- `scripts/list-accounts.js`
- `scripts/create-connect-token.js`
- `scripts/configure-prop.js`
- `scripts/reload-props.js`
- `scripts/list-integrations.js`
- `scripts/create-integration.js`
- `scripts/update-integration.js`
- `scripts/delete-integration.js`
- `scripts/list-whatsapp-phone-numbers.js`

## Platform API endpoints

Implemented calls:

- `GET /platform/v1/workflows`
- `POST /platform/v1/workflows`
- `GET /platform/v1/workflows/:id`
- `GET /platform/v1/workflows/:id/definition` (fetch graph definition)
- `PATCH /platform/v1/workflows/:id` (update settings/definition)
- `GET /platform/v1/workflows/:id/variables` (workflow variable discovery)
- `GET /platform/v1/workflows/:workflow_id/triggers`
- `POST /platform/v1/workflows/:workflow_id/triggers`
- `PATCH /platform/v1/triggers/:id`
- `DELETE /platform/v1/triggers/:id`
- `GET /platform/v1/workflows/:workflow_id/executions`
- `GET /platform/v1/workflow_executions/:id`
- `PATCH /platform/v1/workflow_executions/:id`
- `POST /platform/v1/workflow_executions/:id/resume`
- `GET /platform/v1/workflow_executions/:id/events`
- `GET /platform/v1/workflow_events/:id`
- `GET /platform/v1/provider_models`
- `GET /platform/v1/integrations`
- `POST /platform/v1/integrations`
- `PATCH /platform/v1/integrations/:id`
- `DELETE /platform/v1/integrations/:id`
- `GET /platform/v1/integrations/apps`
- `GET /platform/v1/integrations/actions`
- `GET /platform/v1/integrations/accounts`
- `POST /platform/v1/integrations/connect_token`
- `GET /platform/v1/integrations/actions/:action_id/schema`
- `POST /platform/v1/integrations/actions/:action_id/configure_prop`
- `POST /platform/v1/integrations/actions/:action_id/reload_props`
- `GET /platform/v1/whatsapp/phone_numbers` (for inbound_message triggers)

Variables CRUD endpoints are not defined for Platform API. Scripts intentionally return blocked for create/update/delete operations.

## Workflow graphs: endpoints, shapes, and roundtrips

- `GET /platform/v1/workflows/:id` returns workflow metadata (including `lock_version`) but does NOT include `definition`.
- `GET /platform/v1/workflows/:id/definition` returns a workflow record that includes `definition` (nodes + edges).
- `PATCH /platform/v1/workflows/:id` accepts either `workflow: { ... }` or `flow: { ... }` envelopes.
  - To update the graph: send `workflow: { definition: <definition> }`.

Graph shapes:
- `get-graph.js` returns a ReactFlow-style definition that includes extra/computed fields (`node.type`, `data.display_name`, `edge.id`, `edge.type`).
- The API accepts a minimal editable definition (`nodes[].id/position/data.node_type/data.config` and `edges[].source/target/label`) and ignores/strips extra fields.

Source of truth: `references/graph-contract.md`.

## Phone number lookup for triggers

Use `scripts/list-whatsapp-phone-numbers.js` to find `phone_number_id` for inbound_message triggers.
Do not use `/whatsapp_configs` (not a Platform API endpoint).

## Graph validation rules (local)

The `scripts/validate-graph.js` script checks:

- Exactly one start node with `id` = `start` and `data.node_type` = `start`.
- Unique node IDs and valid edge source/target IDs.
- Non-empty edge labels.
- Only `decide` nodes may branch; other nodes may have 0 or 1 outgoing `next` edge.
- Decide node condition labels must match outgoing edge labels.

Warnings are emitted for unknown node types or extra decide edges. Treat warnings as blockers before you PATCH a graph.

## Assets

- `assets/workflow-linear.json` (simple linear example)
- `assets/workflow-decision.json` (wait + decide example)
```

## File: `skills/automate-whatsapp/scripts/configure-prop.js`
```javascript
#!/usr/bin/env node
import { loadConfig, requestJson } from './lib/workflows/kapso-api.js';
import { ok, err, printJson } from './lib/workflows/result.js';
import { parseArgs, getFlag, getBooleanFlag } from './lib/workflows/args.js';

function usage() {
  return ok({
    usage: 'node scripts/configure-prop.js --action-id <id> --prop-name <name> --account-id <id> [--configured-props <json>] [--dynamic-props-id <id>]',
    notes: [
      'Use accounts[].pipedream_account_id for --account-id.',
      'If you pass an internal account UUID, the script will try to resolve it.'
    ],
    env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
  });
}

function parseJson(value, label) {
  if (!value) return undefined;
  try {
    return JSON.parse(value);
  } catch (error) {
    throw new Error(`Invalid JSON for ${label}: ${String(error?.message || error)}`);
  }
}

function normalizeAccounts(payload) {
  if (Array.isArray(payload?.accounts)) return payload.accounts;
  if (Array.isArray(payload?.accounts?.accounts)) return payload.accounts.accounts;
  if (Array.isArray(payload)) return payload;
  return [];
}

async function resolveAccountId(config, accountId) {
  if (accountId.startsWith('apn_')) return accountId;

  const response = await requestJson(config, {
    method: 'GET',
    path: '/platform/v1/integrations/accounts'
  });

  if (!response.ok) {
    throw new Error('Unable to resolve account id. Use list-accounts and pass pipedream_account_id.');
  }

  const accounts = normalizeAccounts(response.data);
  const match = accounts.find((account) => account.id === accountId);
  if (match?.pipedream_account_id) return match.pipedream_account_id;

  throw new Error('account-id must be pipedream_account_id (use list-accounts output).');
}

async function main() {
  const parsed = parseArgs(process.argv.slice(2));
  if (getBooleanFlag(parsed.flags, 'help') || getBooleanFlag(parsed.flags, 'h')) {
    printJson(usage());
    return 0;
  }

  const actionId = getFlag(parsed.flags, 'action-id');
  const propName = getFlag(parsed.flags, 'prop-name');
  const accountId = getFlag(parsed.flags, 'account-id');

  if (!actionId || !propName || !accountId) {
    printJson(err('action-id, prop-name, and account-id are required'));
    return 2;
  }

  let configuredProps = {};
  try {
    const provided = parseJson(getFlag(parsed.flags, 'configured-props'), 'configured-props');
    configuredProps = provided || {};
  } catch (error) {
    printJson(err('Failed to parse configured-props', { message: error.message }));
    return 2;
  }

  const config = loadConfig();
  let resolvedAccountId = accountId;

  try {
    resolvedAccountId = await resolveAccountId(config, accountId);
  } catch (error) {
    printJson(err('Failed to resolve account-id', { message: error.message }));
    return 2;
  }

  if (!Object.keys(configuredProps).length) {
    configuredProps = { account_id: resolvedAccountId };
  }

  const response = await requestJson(config, {
    method: 'POST',
    path: `/platform/v1/integrations/actions/${actionId}/configure_prop`,
    body: {
      prop_name: propName,
      configured_props: configuredProps,
      dynamic_props_id: getFlag(parsed.flags, 'dynamic-props-id')
    }
  });

  if (!response.ok) {
    printJson(err('Failed to configure prop', response.raw, false, response.status));
    return 2;
  }

  printJson(ok({ result: response.data }));
  return 0;
}

main().catch((error) => {
  printJson(err('Unhandled error', { message: String(error?.message || error) }));
  process.exit(1);
});
```

## File: `skills/automate-whatsapp/scripts/create-connect-token.js`
```javascript
#!/usr/bin/env node
import { loadConfig, requestJson } from './lib/workflows/kapso-api.js';
import { ok, err, printJson } from './lib/workflows/result.js';
import { parseArgs, getBooleanFlag } from './lib/workflows/args.js';

function usage() {
  return ok({
    usage: 'node scripts/create-connect-token.js',
    env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
  });
}

async function main() {
  const parsed = parseArgs(process.argv.slice(2));
  if (getBooleanFlag(parsed.flags, 'help') || getBooleanFlag(parsed.flags, 'h')) {
    printJson(usage());
    return 0;
  }

  const config = loadConfig();
  const response = await requestJson(config, {
    method: 'POST',
    path: '/platform/v1/integrations/connect_token'
  });

  if (!response.ok) {
    printJson(err('Failed to create connect token', response.raw, false, response.status));
    return 2;
  }

  printJson(ok({ connect_token: response.data }));
  return 0;
}

main().catch((error) => {
  printJson(err('Unhandled error', { message: String(error?.message || error) }));
  process.exit(1);
});
```

## File: `skills/automate-whatsapp/scripts/create-function.js`
```javascript
import { readFileSync } from 'node:fs';
import { kapsoConfigFromEnv, kapsoRequest } from './lib/functions/kapso-api.js';
import { hasHelpFlag, parseFlags, requireFlag } from './lib/functions/args.js';

function ok(data) {
  return { ok: true, data };
}

function err(message, details) {
  return { ok: false, error: { message, details } };
}

function resolveCode(flags) {
  if (typeof flags.code === 'string' && flags.code.length > 0) {
    return flags.code;
  }
  if (typeof flags['code-file'] === 'string' && flags['code-file'].length > 0) {
    return readFileSync(flags['code-file'], 'utf8');
  }
  throw new Error('Provide --code or --code-file');
}

async function main() {
  const argv = process.argv.slice(2);
  if (hasHelpFlag(argv)) {
    console.log(
      JSON.stringify(
        {
          ok: true,
          usage:
            'node scripts/create-function.js --name <name> (--code <js> | --code-file <path>) [--description <text>]',
          env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
        },
        null,
        2
      )
    );
    return 0;
  }

  try {
    const flags = parseFlags(argv);
    const name = requireFlag(flags, 'name');
    const code = resolveCode(flags);
    const payload = { name, code };
    if (typeof flags.description === 'string' && flags.description.length > 0) {
      payload.description = flags.description;
    }
    const config = kapsoConfigFromEnv();
    const data = await kapsoRequest(config, '/platform/v1/functions', {
      method: 'POST',
      body: JSON.stringify({ function: payload })
    });

    console.log(JSON.stringify(ok(data), null, 2));
    return 0;
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    console.error(JSON.stringify(err('Command failed', { message }), null, 2));
    return 1;
  }
}

main().then((code) => process.exit(code));
```

## File: `skills/automate-whatsapp/scripts/create-integration.js`
```javascript
#!/usr/bin/env node
import { loadConfig, requestJson } from './lib/workflows/kapso-api.js';
import { ok, err, printJson } from './lib/workflows/result.js';
import { parseArgs, getFlag, getBooleanFlag } from './lib/workflows/args.js';

function usage() {
  return ok({
    usage: 'node scripts/create-integration.js --action-id <id> --app-slug <slug> --account-id <id> [--configured-props <json>] [--name <text>] [--app-name <text>] [--variable-definitions <json>] [--dynamic-props-id <id>]',
    notes: [
      'Use accounts[].pipedream_account_id for --account-id.',
      'If you pass an internal account UUID, the script will try to resolve it.',
      'Use --variable-definitions to define agent tool inputs (placeholders in configured_props become inputs).'
    ],
    env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
  });
}

function parseJson(value, label) {
  if (!value) return undefined;
  try {
    return JSON.parse(value);
  } catch (error) {
    throw new Error(`Invalid JSON for ${label}: ${String(error?.message || error)}`);
  }
}

function ensureAccountId(props, accountId) {
  if (!props || !Object.keys(props).length) {
    return { account_id: accountId };
  }
  if (!props.account_id && !props.accountId) {
    return { ...props, account_id: accountId };
  }
  return props;
}

function normalizeAccounts(payload) {
  if (Array.isArray(payload?.accounts)) return payload.accounts;
  if (Array.isArray(payload?.accounts?.accounts)) return payload.accounts.accounts;
  if (Array.isArray(payload)) return payload;
  return [];
}

async function resolveAccountId(config, appSlug, accountId) {
  if (accountId.startsWith('apn_')) return accountId;

  const response = await requestJson(config, {
    method: 'GET',
    path: '/platform/v1/integrations/accounts',
    query: { app_slug: appSlug }
  });

  if (!response.ok) {
    throw new Error('Unable to resolve account id. Use list-accounts and pass pipedream_account_id.');
  }

  const accounts = normalizeAccounts(response.data);
  const match = accounts.find((account) => account.id === accountId);
  if (match?.pipedream_account_id) return match.pipedream_account_id;

  throw new Error('account-id must be pipedream_account_id (use list-accounts output).');
}

async function main() {
  const parsed = parseArgs(process.argv.slice(2));
  if (getBooleanFlag(parsed.flags, 'help') || getBooleanFlag(parsed.flags, 'h')) {
    printJson(usage());
    return 0;
  }

  const actionId = getFlag(parsed.flags, 'action-id');
  const appSlug = getFlag(parsed.flags, 'app-slug');
  const accountId = getFlag(parsed.flags, 'account-id');

  if (!actionId || !appSlug || !accountId) {
    printJson(err('action-id, app-slug, and account-id are required'));
    return 2;
  }

  let configuredProps;
  let variableDefinitions;

  try {
    configuredProps = parseJson(getFlag(parsed.flags, 'configured-props'), 'configured-props');
    variableDefinitions = parseJson(getFlag(parsed.flags, 'variable-definitions'), 'variable-definitions');
  } catch (error) {
    printJson(err('Failed to parse JSON', { message: error.message }));
    return 2;
  }

  const config = loadConfig();
  let resolvedAccountId = accountId;

  try {
    resolvedAccountId = await resolveAccountId(config, appSlug, accountId);
  } catch (error) {
    printJson(err('Failed to resolve account-id', { message: error.message }));
    return 2;
  }

  configuredProps = ensureAccountId(configuredProps, resolvedAccountId);

  const payload = {
    action_id: actionId,
    app_slug: appSlug,
    account_id: resolvedAccountId,
    configured_props: configuredProps
  };

  const name = getFlag(parsed.flags, 'name');
  const appName = getFlag(parsed.flags, 'app-name');
  const dynamicPropsId = getFlag(parsed.flags, 'dynamic-props-id');

  if (name) payload.name = name;
  if (appName) payload.app_name = appName;
  if (dynamicPropsId) payload.dynamic_props_id = dynamicPropsId;
  if (variableDefinitions) payload.variable_definitions = variableDefinitions;

  const response = await requestJson(config, {
    method: 'POST',
    path: '/platform/v1/integrations',
    body: payload
  });

  if (!response.ok) {
    printJson(err('Failed to create integration', response.raw, false, response.status));
    return 2;
  }

  printJson(ok({ integration: response.data }));
  return 0;
}

main().catch((error) => {
  printJson(err('Unhandled error', { message: String(error?.message || error) }));
  process.exit(1);
});
```

## File: `skills/automate-whatsapp/scripts/create-row.js`
```javascript
import { kapsoConfigFromEnv, kapsoRequest } from './lib/databases/kapso-api.js';
import { hasHelpFlag, parseFlags, requireFlag, parseJsonObject } from './lib/databases/args.js';

function ok(data) {
  return { ok: true, data };
}

function err(message, details) {
  return { ok: false, error: { message, details } };
}

async function main() {
  const argv = process.argv.slice(2);
  if (hasHelpFlag(argv)) {
    console.log(
      JSON.stringify(
        {
          ok: true,
          usage: 'node scripts/create-row.js --table <name> --data <json>',
          env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
        },
        null,
        2
      )
    );
    return 0;
  }

  try {
    const flags = parseFlags(argv);
    const table = requireFlag(flags, 'table');
    const dataPayload = parseJsonObject(flags.data, 'data');
    const config = kapsoConfigFromEnv();
    const data = await kapsoRequest(config, `/platform/v1/db/${encodeURIComponent(table)}`, {
      method: 'POST',
      body: JSON.stringify(dataPayload)
    });
    console.log(JSON.stringify(ok(data), null, 2));
    return 0;
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    console.error(JSON.stringify(err('Command failed', { message }), null, 2));
    return 1;
  }
}

main().then((code) => process.exit(code));
```

## File: `skills/automate-whatsapp/scripts/create-trigger.js`
```javascript
#!/usr/bin/env node
import { loadConfig, requestJson } from './lib/workflows/kapso-api.js';
import { ok, err, printJson } from './lib/workflows/result.js';
import { parseArgs, getFlag, getBooleanFlag } from './lib/workflows/args.js';

function usage() {
  return ok({
    usage: 'node scripts/create-trigger.js <workflow-id> --trigger-type <inbound_message|api_call|whatsapp_event> [--phone-number-id <id>] [--event <whatsapp.event>] [--active true|false] [--triggerable-attributes <json>]',
    env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
  });
}

function parseBoolean(value) {
  if (value === undefined) return undefined;
  if (value === true) return true;
  const lowered = String(value).toLowerCase();
  if (lowered === 'true') return true;
  if (lowered === 'false') return false;
  return undefined;
}

function parseJson(value) {
  if (!value) return undefined;
  return JSON.parse(value);
}

async function main() {
  const parsed = parseArgs(process.argv.slice(2));
  if (getBooleanFlag(parsed.flags, 'help') || getBooleanFlag(parsed.flags, 'h')) {
    printJson(usage());
    return 0;
  }

  const workflowId = parsed.args[0] || getFlag(parsed.flags, 'workflow-id');
  if (!workflowId) {
    printJson(err('workflow_id is required'));
    return 2;
  }

  const triggerType = getFlag(parsed.flags, 'trigger-type');
  if (!triggerType) {
    printJson(err('trigger-type is required'));
    return 2;
  }

  const active = parseBoolean(getFlag(parsed.flags, 'active'));
  const phoneNumberId = getFlag(parsed.flags, 'phone-number-id');
  const whatsappConfigId = getFlag(parsed.flags, 'whatsapp-config-id');
  const event = getFlag(parsed.flags, 'event');

  let triggerableAttributes;
  try {
    triggerableAttributes = parseJson(getFlag(parsed.flags, 'triggerable-attributes'));
  } catch (error) {
    printJson(err('Invalid JSON for triggerable-attributes', { message: String(error?.message || error) }));
    return 2;
  }

  const triggerPayload = {
    trigger_type: triggerType
  };

  if (active !== undefined) triggerPayload.active = active;
  if (phoneNumberId) triggerPayload.phone_number_id = phoneNumberId;
  if (whatsappConfigId) triggerPayload.whatsapp_config_id = whatsappConfigId;
  if (event) triggerPayload.event = event;
  if (triggerableAttributes) triggerPayload.triggerable_attributes = triggerableAttributes;

  const config = loadConfig();
  const response = await requestJson(config, {
    method: 'POST',
    path: `/platform/v1/workflows/${workflowId}/triggers`,
    body: { trigger: triggerPayload }
  });

  if (!response.ok) {
    printJson(err('Failed to create trigger', response.raw, false, response.status));
    return 2;
  }

  printJson(ok({ trigger: response.data }));
  return 0;
}

main().catch((error) => {
  printJson(err('Unhandled error', { message: String(error?.message || error) }));
  process.exit(1);
});
```

## File: `skills/automate-whatsapp/scripts/create-workflow.js`
```javascript
#!/usr/bin/env node
import fs from 'fs';
import { loadConfig, requestJson } from './lib/workflows/kapso-api.js';
import { ok, err, printJson } from './lib/workflows/result.js';
import { parseArgs, getFlag, getBooleanFlag } from './lib/workflows/args.js';

function usage() {
  return ok({
    usage: 'node scripts/create-workflow.js --name <name> [--description <text>] [--definition-file <path> | --definition-json <json>]',
    env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
  });
}

function loadDefinition({ filePath, jsonText }) {
  if (filePath) {
    const raw = fs.readFileSync(filePath, 'utf8');
    return JSON.parse(raw);
  }
  if (jsonText) {
    return JSON.parse(jsonText);
  }
  return undefined;
}

async function main() {
  const parsed = parseArgs(process.argv.slice(2));
  if (getBooleanFlag(parsed.flags, 'help') || getBooleanFlag(parsed.flags, 'h')) {
    printJson(usage());
    return 0;
  }

  const name = getFlag(parsed.flags, 'name');
  if (!name) {
    printJson(err('name is required'));
    return 2;
  }

  const description = getFlag(parsed.flags, 'description');
  const definitionFile = getFlag(parsed.flags, 'definition-file');
  const definitionJson = getFlag(parsed.flags, 'definition-json');

  if (definitionFile && definitionJson) {
    printJson(err('Provide only one of --definition-file or --definition-json'));
    return 2;
  }

  let definition;
  try {
    definition = loadDefinition({ filePath: definitionFile, jsonText: definitionJson });
  } catch (error) {
    printJson(err('Failed to parse workflow definition JSON', { message: String(error?.message || error) }));
    return 2;
  }

  const payload = {
    workflow: {
      name,
      description
    }
  };

  if (definition) {
    payload.workflow.definition = definition;
  }

  const config = loadConfig();
  const response = await requestJson(config, {
    method: 'POST',
    path: '/platform/v1/workflows',
    body: payload
  });

  if (!response.ok) {
    printJson(err('Failed to create workflow', response.raw, false, response.status));
    return 2;
  }

  printJson(ok({ workflow: response.data }));
  return 0;
}

main().catch((error) => {
  printJson(err('Unhandled error', { message: String(error?.message || error) }));
  process.exit(1);
});
```

## File: `skills/automate-whatsapp/scripts/delete-integration.js`
```javascript
#!/usr/bin/env node
import { loadConfig, requestJson } from './lib/workflows/kapso-api.js';
import { ok, err, printJson } from './lib/workflows/result.js';
import { parseArgs, getFlag, getBooleanFlag } from './lib/workflows/args.js';

function usage() {
  return ok({
    usage: 'node scripts/delete-integration.js --integration-id <id>',
    env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
  });
}

async function main() {
  const parsed = parseArgs(process.argv.slice(2));
  if (getBooleanFlag(parsed.flags, 'help') || getBooleanFlag(parsed.flags, 'h')) {
    printJson(usage());
    return 0;
  }

  const integrationId = getFlag(parsed.flags, 'integration-id');
  if (!integrationId) {
    printJson(err('integration-id is required'));
    return 2;
  }

  const config = loadConfig();
  const response = await requestJson(config, {
    method: 'DELETE',
    path: `/platform/v1/integrations/${integrationId}`
  });

  if (!response.ok) {
    printJson(err('Failed to delete integration', response.raw, false, response.status));
    return 2;
  }

  printJson(ok({ deleted: true, status: response.status }));
  return 0;
}

main().catch((error) => {
  printJson(err('Unhandled error', { message: String(error?.message || error) }));
  process.exit(1);
});
```

## File: `skills/automate-whatsapp/scripts/delete-row.js`
```javascript
import { kapsoConfigFromEnv, kapsoRequest } from './lib/databases/kapso-api.js';
import { hasHelpFlag, parseFlags, requireFlag } from './lib/databases/args.js';
import { resolveFilters, filtersToQuery } from './lib/databases/filters.js';

function ok(data) {
  return { ok: true, data };
}

function err(message, details) {
  return { ok: false, error: { message, details } };
}

async function main() {
  const argv = process.argv.slice(2);
  if (hasHelpFlag(argv)) {
    console.log(
      JSON.stringify(
        {
          ok: true,
          usage:
            'node scripts/delete-row.js --table <name> (--id <row-id> | --filters <json>)',
          env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
        },
        null,
        2
      )
    );
    return 0;
  }

  try {
    const flags = parseFlags(argv);
    const table = requireFlag(flags, 'table');
    const filters = resolveFilters(flags);
    const query = filtersToQuery(filters);
    const config = kapsoConfigFromEnv();
    const data = await kapsoRequest(config, `/platform/v1/db/${encodeURIComponent(table)}${query}`, {
      method: 'DELETE'
    });
    console.log(JSON.stringify(ok(data), null, 2));
    return 0;
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    console.error(JSON.stringify(err('Command failed', { message }), null, 2));
    return 1;
  }
}

main().then((code) => process.exit(code));
```

## File: `skills/automate-whatsapp/scripts/delete-trigger.js`
```javascript
#!/usr/bin/env node
import { loadConfig, requestJson } from './lib/workflows/kapso-api.js';
import { ok, err, printJson } from './lib/workflows/result.js';
import { parseArgs, getFlag, getBooleanFlag } from './lib/workflows/args.js';

function usage() {
  return ok({
    usage: 'node scripts/delete-trigger.js --trigger-id <id>',
    env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
  });
}

async function main() {
  const parsed = parseArgs(process.argv.slice(2));
  if (getBooleanFlag(parsed.flags, 'help') || getBooleanFlag(parsed.flags, 'h')) {
    printJson(usage());
    return 0;
  }

  const triggerId = getFlag(parsed.flags, 'trigger-id');
  if (!triggerId) {
    printJson(err('trigger-id is required'));
    return 2;
  }

  const config = loadConfig();
  const response = await requestJson(config, {
    method: 'DELETE',
    path: `/platform/v1/triggers/${triggerId}`
  });

  if (!response.ok) {
    printJson(err('Failed to delete trigger', response.raw, false, response.status));
    return 2;
  }

  printJson(ok({ deleted: true, status: response.status }));
  return 0;
}

main().catch((error) => {
  printJson(err('Unhandled error', { message: String(error?.message || error) }));
  process.exit(1);
});
```

## File: `skills/automate-whatsapp/scripts/deploy-function.js`
```javascript
import { kapsoConfigFromEnv, kapsoRequest } from './lib/functions/kapso-api.js';
import { hasHelpFlag, parseFlags, requireFlag } from './lib/functions/args.js';

function ok(data) {
  return { ok: true, data };
}

function err(message, details) {
  return { ok: false, error: { message, details } };
}

async function main() {
  const argv = process.argv.slice(2);
  if (hasHelpFlag(argv)) {
    console.log(
      JSON.stringify(
        {
          ok: true,
          usage: 'node scripts/deploy-function.js --function-id <id>',
          env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
        },
        null,
        2
      )
    );
    return 0;
  }

  try {
    const flags = parseFlags(argv);
    const functionId = requireFlag(flags, 'function-id');
    const config = kapsoConfigFromEnv();
    const data = await kapsoRequest(config, `/platform/v1/functions/${encodeURIComponent(functionId)}/deploy`, {
      method: 'POST',
      body: JSON.stringify({})
    });

    console.log(JSON.stringify(ok(data), null, 2));
    return 0;
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    console.error(JSON.stringify(err('Command failed', { message }), null, 2));
    return 1;
  }
}

main().then((code) => process.exit(code));
```

## File: `skills/automate-whatsapp/scripts/edit-graph.js`
```javascript
#!/usr/bin/env node
import { createHash } from 'crypto';
import { readFileSync } from 'fs';
import { loadConfig, requestJson } from './lib/workflows/kapso-api.js';
import { ok, err, printJson } from './lib/workflows/result.js';
import { parseArgs, getFlag, getBooleanFlag, getNumberFlag } from './lib/workflows/args.js';

function sha256(text) {
  return createHash('sha256').update(text).digest('hex');
}

function normalizeLineEndings(text) {
  return text.replace(/\r\n/g, '\n').replace(/\r/g, '\n');
}

function stripCodeFences(text) {
  const trimmed = text.trim();
  if (trimmed.startsWith('```')) {
    const withoutFirst = trimmed.replace(/^```[a-zA-Z0-9_-]*\n?/, '');
    return withoutFirst.replace(/```$/, '').trim();
  }
  return text;
}

function stripLineNumbers(text) {
  return text
    .split('\n')
    .map((line) => line.replace(/^\s*\d+\s*\|\s?/, '').replace(/^\s*\d+:\s?/, ''))
    .join('\n');
}

function normalizeEditText(text) {
  return normalizeLineEndings(stripLineNumbers(stripCodeFences(text)));
}

function readFileText(path) {
  return readFileSync(path, 'utf8');
}

function loadTextInput(flags, valueFlag, fileFlag) {
  const filePath = getFlag(flags, fileFlag);
  if (filePath) {
    return readFileText(filePath);
  }
  return getFlag(flags, valueFlag);
}

function isEscaped(text, index) {
  let backslashes = 0;
  for (let i = index - 1; i >= 0 && text[i] === '\\'; i -= 1) {
    backslashes += 1;
  }
  return backslashes % 2 === 1;
}

function insideJsonString(text, index) {
  let inString = false;
  for (let i = 0; i < index; i += 1) {
    if (text[i] === '"' && !isEscaped(text, i)) {
      inString = !inString;
    }
  }
  return inString;
}

function unescapeCLike(text) {
  return text
    .replace(/\\n/g, '\n')
    .replace(/\\r/g, '\r')
    .replace(/\\t/g, '\t')
    .replace(/\\"/g, '"')
    .replace(/\\\\/g, '\\');
}

function jsonStringContent(text) {
  const json = JSON.stringify(text);
  return json.slice(1, -1);
}

function replaceAllOccurrences(content, search, newText) {
  let result = '';
  let index = 0;
  let replacementsInJson = 0;
  let replacementsOutsideJson = 0;

  while (true) {
    const matchIndex = content.indexOf(search, index);
    if (matchIndex === -1) {
      result += content.slice(index);
      break;
    }

    const insideString = insideJsonString(content, matchIndex);
    const replacement = insideString
      ? jsonStringContent(unescapeCLike(newText))
      : newText;

    result += content.slice(index, matchIndex) + replacement;
    index = matchIndex + search.length;

    if (insideString) {
      replacementsInJson += 1;
    } else {
      replacementsOutsideJson += 1;
    }
  }

  return {
    content: result,
    replacements: replacementsInJson + replacementsOutsideJson,
    replacements_in_json_strings: replacementsInJson,
    replacements_outside_json_strings: replacementsOutsideJson
  };
}

function applyReplacement(content, oldText, newText, replaceAll) {
  if (oldText === newText) {
    throw new Error('old and new text must be different');
  }

  const candidates = [
    { label: 'raw', value: oldText },
    { label: 'unescaped', value: oldText.replace(/\\n/g, '\n') },
    { label: 'escaped', value: oldText.replace(/\n/g, '\\n') }
  ];

  const seen = new Set();
  const uniqueCandidates = candidates.filter((candidate) => {
    if (seen.has(candidate.value)) return false;
    seen.add(candidate.value);
    return true;
  });

  for (const candidate of uniqueCandidates) {
    if (!candidate.value) continue;
    const firstIndex = content.indexOf(candidate.value);
    if (firstIndex === -1) continue;

    if (replaceAll) {
      const replaced = replaceAllOccurrences(content, candidate.value, newText);
      return { ...replaced, matchedVariant: candidate.label };
    }

    const lastIndex = content.lastIndexOf(candidate.value);
    if (firstIndex !== lastIndex) {
      throw new Error('old text matches multiple locations; use --replace-all or narrow the match');
    }

    const insideString = insideJsonString(content, firstIndex);
    const replacement = insideString
      ? jsonStringContent(unescapeCLike(newText))
      : newText;

    const updated = content.replace(candidate.value, replacement);
    return {
      content: updated,
      replacements: 1,
      replacements_in_json_strings: insideString ? 1 : 0,
      replacements_outside_json_strings: insideString ? 0 : 1,
      matchedVariant: candidate.label
    };
  }

  throw new Error('old text not found in workflow graph');
}

function usage() {
  return ok({
    usage: 'node scripts/edit-graph.js <workflow-id> --expected-lock-version <n> --old <text>|--old-file <path> --new <text>|--new-file <path> [--replace-all]',
    env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
  });
}

async function main() {
  const parsed = parseArgs(process.argv.slice(2));
  if (getBooleanFlag(parsed.flags, 'help') || getBooleanFlag(parsed.flags, 'h')) {
    printJson(usage());
    return 0;
  }

  const workflowId = parsed.args[0] || getFlag(parsed.flags, 'workflow-id');
  if (!workflowId) {
    printJson(err('workflow_id is required'));
    return 2;
  }

  const expectedLockVersion = getNumberFlag(parsed.flags, 'expected-lock-version')
    ?? getNumberFlag(parsed.flags, 'lock-version');
  if (expectedLockVersion === undefined) {
    printJson(err('expected-lock-version is required'));
    return 2;
  }

  const oldInput = loadTextInput(parsed.flags, 'old', 'old-file');
  const newInput = loadTextInput(parsed.flags, 'new', 'new-file');
  if (!oldInput || !newInput) {
    printJson(err('old/new text is required (use --old/--new or --old-file/--new-file)'));
    return 2;
  }

  const replaceAll = getBooleanFlag(parsed.flags, 'replace-all');

  const config = loadConfig();
  const response = await requestJson(config, {
    method: 'GET',
    path: `/platform/v1/workflows/${workflowId}/definition`
  });

  if (!response.ok) {
    printJson(err('Failed to fetch workflow definition', response.raw, false, response.status));
    return 2;
  }

  const workflow = response.data;
  const definition = workflow && typeof workflow === 'object' ? workflow.definition : null;
  if (!definition || typeof definition !== 'object') {
    printJson(err('Workflow definition missing in response', response.raw, false, response.status));
    return 2;
  }

  const currentLock = workflow.lock_version;
  if (currentLock !== expectedLockVersion) {
    printJson(err('Conflict: workflow was modified. Refetch and retry.', {
      expected_lock_version: expectedLockVersion,
      current_lock_version: currentLock
    }));
    return 2;
  }

  const pretty = JSON.stringify(definition, null, 2);
  const beforeHash = sha256(pretty);
  const oldText = normalizeEditText(oldInput);
  const newText = normalizeEditText(newInput);

  let editResult;
  try {
    editResult = applyReplacement(pretty, oldText, newText, replaceAll);
  } catch (error) {
    printJson(err(String(error?.message || error)));
    return 2;
  }

  let updatedDefinition;
  try {
    updatedDefinition = JSON.parse(editResult.content);
  } catch (error) {
    printJson(err('Invalid JSON after replacement', { message: String(error?.message || error) }));
    return 2;
  }

  const update = await requestJson(config, {
    method: 'PATCH',
    path: `/platform/v1/workflows/${workflowId}`,
    body: {
      workflow: {
        definition: updatedDefinition
      }
    }
  });

  if (!update.ok) {
    printJson(err('Failed to update workflow definition', update.raw, false, update.status));
    return 2;
  }

  printJson(ok({
    workflow_id: workflowId,
    replacements_count: editResult.replacements,
    replacements_in_json_strings: editResult.replacements_in_json_strings,
    replacements_outside_json_strings: editResult.replacements_outside_json_strings,
    matched_variant: editResult.matchedVariant,
    workflow_graph_sha256_before: beforeHash,
    workflow_graph_sha256_after: sha256(editResult.content),
    update: {
      id: update.data.id,
      name: update.data.name,
      status: update.data.status,
      lock_version: update.data.lock_version,
      updated_at: update.data.updated_at
    }
  }));

  return 0;
}

main().catch((error) => {
  printJson(err('Unhandled error', { message: String(error?.message || error) }));
  process.exit(1);
});
```

## File: `skills/automate-whatsapp/scripts/get-action-schema.js`
```javascript
#!/usr/bin/env node
import { loadConfig, requestJson } from './lib/workflows/kapso-api.js';
import { ok, err, printJson } from './lib/workflows/result.js';
import { parseArgs, getFlag, getBooleanFlag } from './lib/workflows/args.js';

function usage() {
  return ok({
    usage: 'node scripts/get-action-schema.js --action-id <id>',
    env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
  });
}

async function main() {
  const parsed = parseArgs(process.argv.slice(2));
  if (getBooleanFlag(parsed.flags, 'help') || getBooleanFlag(parsed.flags, 'h')) {
    printJson(usage());
    return 0;
  }

  const actionId = getFlag(parsed.flags, 'action-id');
  if (!actionId) {
    printJson(err('action-id is required'));
    return 2;
  }

  const config = loadConfig();
  const response = await requestJson(config, {
    method: 'GET',
    path: `/platform/v1/integrations/actions/${actionId}/schema`
  });

  if (!response.ok) {
    printJson(err('Failed to fetch action schema', response.raw, false, response.status));
    return 2;
  }

  printJson(ok({ schema: response.data }));
  return 0;
}

main().catch((error) => {
  printJson(err('Unhandled error', { message: String(error?.message || error) }));
  process.exit(1);
});
```

## File: `skills/automate-whatsapp/scripts/get-context-value.js`
```javascript
#!/usr/bin/env node
import { loadConfig, requestJson } from './lib/workflows/kapso-api.js';
import { ok, err, printJson } from './lib/workflows/result.js';
import { parseArgs, getFlag, getBooleanFlag } from './lib/workflows/args.js';

function usage() {
  return ok({
    usage: 'node scripts/get-context-value.js <execution-id> --variable-path <path>',
    env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY'],
    examples: ['node scripts/get-context-value.js exec_123 --variable-path vars.user_name']
  });
}

function getPathValue(obj, path) {
  if (!path) return undefined;
  const parts = path.split('.').filter(Boolean);
  let current = obj;
  for (const part of parts) {
    if (current && Object.prototype.hasOwnProperty.call(current, part)) {
      current = current[part];
    } else {
      return undefined;
    }
  }
  return current;
}

async function main() {
  const parsed = parseArgs(process.argv.slice(2));
  if (getBooleanFlag(parsed.flags, 'help') || getBooleanFlag(parsed.flags, 'h')) {
    printJson(usage());
    return 0;
  }

  const executionId = parsed.args[0] || getFlag(parsed.flags, 'execution-id');
  if (!executionId) {
    printJson(err('execution_id is required'));
    return 2;
  }

  const variablePath = getFlag(parsed.flags, 'variable-path');
  if (!variablePath) {
    printJson(err('variable-path is required'));
    return 2;
  }

  const config = loadConfig();
  const response = await requestJson(config, {
    method: 'GET',
    path: `/platform/v1/workflow_executions/${executionId}`
  });

  if (!response.ok) {
    printJson(err('Failed to fetch execution', response.raw, false, response.status));
    return 2;
  }

  const execution = response.data;
  const executionContext = execution && execution.execution_context ? execution.execution_context : {};
  let path = variablePath;

  if (path.startsWith('execution_context.')) {
    path = path.replace(/^execution_context\./, '');
  }

  const value = getPathValue(executionContext, path);

  if (value === undefined) {
    printJson(err('Path not found in execution_context', { variable_path: variablePath }));
    return 2;
  }

  printJson(ok({ value, variable_path: variablePath, execution_id: executionId }));
  return 0;
}

main().catch((error) => {
  printJson(err('Unhandled error', { message: String(error?.message || error) }));
  process.exit(1);
});
```

## File: `skills/automate-whatsapp/scripts/get-execution-event.js`
```javascript
#!/usr/bin/env node
import { loadConfig, requestJson } from './lib/workflows/kapso-api.js';
import { ok, err, printJson } from './lib/workflows/result.js';
import { parseArgs, getFlag, getBooleanFlag } from './lib/workflows/args.js';

function usage() {
  return ok({
    usage: 'node scripts/get-execution-event.js <event-id> [--event-id <id>]',
    env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
  });
}

async function main() {
  const parsed = parseArgs(process.argv.slice(2));
  if (getBooleanFlag(parsed.flags, 'help') || getBooleanFlag(parsed.flags, 'h')) {
    printJson(usage());
    return 0;
  }

  const eventId = parsed.args[0] || getFlag(parsed.flags, 'event-id');
  if (!eventId) {
    printJson(err('event_id is required'));
    return 2;
  }

  const config = loadConfig();
  const response = await requestJson(config, {
    method: 'GET',
    path: `/platform/v1/workflow_events/${eventId}`
  });

  if (!response.ok && response.status === 404) {
    printJson(err('Execution event detail endpoint is not available in the Platform API.', {
      endpoint: '/platform/v1/workflow_events/:id'
    }, true, response.status));
    return 2;
  }

  if (!response.ok) {
    printJson(err('Failed to fetch execution event detail', response.raw, false, response.status));
    return 2;
  }

  printJson(ok({
    event_id: eventId,
    event: response.data
  }));

  return 0;
}

main().catch((error) => {
  printJson(err('Unhandled error', { message: String(error?.message || error) }));
  process.exit(1);
});
```

## File: `skills/automate-whatsapp/scripts/get-execution.js`
```javascript
#!/usr/bin/env node
import { loadConfig, requestJson } from './lib/workflows/kapso-api.js';
import { ok, err, printJson } from './lib/workflows/result.js';
import { parseArgs, getFlag, getBooleanFlag } from './lib/workflows/args.js';

function usage() {
  return ok({
    usage: 'node scripts/get-execution.js <execution-id> [--execution-id <id>]',
    env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
  });
}

async function main() {
  const parsed = parseArgs(process.argv.slice(2));
  if (getBooleanFlag(parsed.flags, 'help') || getBooleanFlag(parsed.flags, 'h')) {
    printJson(usage());
    return 0;
  }

  const executionId = parsed.args[0] || getFlag(parsed.flags, 'execution-id');
  if (!executionId) {
    printJson(err('execution_id is required'));
    return 2;
  }

  const config = loadConfig();
  const response = await requestJson(config, {
    method: 'GET',
    path: `/platform/v1/workflow_executions/${executionId}`
  });

  if (!response.ok) {
    printJson(err('Failed to fetch execution', response.raw, false, response.status));
    return 2;
  }

  printJson(ok({ execution: response.data }));
  return 0;
}

main().catch((error) => {
  printJson(err('Unhandled error', { message: String(error?.message || error) }));
  process.exit(1);
});
```

## File: `skills/automate-whatsapp/scripts/get-function.js`
```javascript
import { kapsoConfigFromEnv, kapsoRequest } from './lib/functions/kapso-api.js';
import { hasHelpFlag, parseFlags, requireFlag } from './lib/functions/args.js';

function ok(data) {
  return { ok: true, data };
}

function err(message, details) {
  return { ok: false, error: { message, details } };
}

async function main() {
  const argv = process.argv.slice(2);
  if (hasHelpFlag(argv)) {
    console.log(
      JSON.stringify(
        {
          ok: true,
          usage: 'node scripts/get-function.js --function-id <id>',
          env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
        },
        null,
        2
      )
    );
    return 0;
  }

  try {
    const flags = parseFlags(argv);
    const functionId = requireFlag(flags, 'function-id');
    const config = kapsoConfigFromEnv();
    const data = await kapsoRequest(config, `/platform/v1/functions/${encodeURIComponent(functionId)}`);
    console.log(JSON.stringify(ok(data), null, 2));
    return 0;
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    console.error(JSON.stringify(err('Command failed', { message }), null, 2));
    return 1;
  }
}

main().then((code) => process.exit(code));
```

## File: `skills/automate-whatsapp/scripts/get-graph.js`
```javascript
#!/usr/bin/env node
import { createHash } from 'crypto';
import { loadConfig, requestJson } from './lib/workflows/kapso-api.js';
import { ok, err, printJson } from './lib/workflows/result.js';
import { parseArgs, getFlag, getBooleanFlag } from './lib/workflows/args.js';

function sha256(text) {
  return createHash('sha256').update(text).digest('hex');
}

function addLineNumbers(text) {
  return text
    .split('\n')
    .map((line, index) => `${String(index + 1).padStart(4, ' ')} | ${line}`)
    .join('\n');
}

function usage() {
  return ok({
    usage: 'node scripts/get-graph.js <workflow-id> [--workflow-id <id>]',
    env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
  });
}

async function main() {
  const parsed = parseArgs(process.argv.slice(2));
  if (getBooleanFlag(parsed.flags, 'help') || getBooleanFlag(parsed.flags, 'h')) {
    printJson(usage());
    return 0;
  }

  const workflowId = parsed.args[0] || getFlag(parsed.flags, 'workflow-id');
  if (!workflowId) {
    printJson(err('workflow_id is required'));
    return 2;
  }

  const config = loadConfig();
  const response = await requestJson(config, {
    method: 'GET',
    path: `/platform/v1/workflows/${workflowId}/definition`
  });

  if (!response.ok) {
    printJson(err('Failed to fetch workflow definition', response.raw, false, response.status));
    return 2;
  }

  const workflow = response.data;
  const definition = workflow && typeof workflow === 'object' ? workflow.definition : null;
  if (!definition || typeof definition !== 'object') {
    printJson(err('Workflow definition missing in response', response.raw, false, response.status));
    return 2;
  }

  const pretty = JSON.stringify(definition, null, 2);
  const hash = sha256(pretty);
  const withLines = addLineNumbers(pretty);

  const trimmedWorkflow = {
    id: workflow.id,
    name: workflow.name,
    description: workflow.description,
    status: workflow.status,
    lock_version: workflow.lock_version,
    message_debounce_seconds: workflow.message_debounce_seconds,
    project_id: workflow.project_id,
    updated_at: workflow.updated_at
  };

  printJson(ok({
    workflow: trimmedWorkflow,
    definition,
    workflow_graph_pretty: pretty,
    workflow_graph_with_lines: withLines,
    workflow_graph_sha256: hash
  }));

  return 0;
}

main().catch((error) => {
  printJson(err('Unhandled error', { message: String(error?.message || error) }));
  process.exit(1);
});
```

## File: `skills/automate-whatsapp/scripts/get-table.js`
```javascript
import { kapsoConfigFromEnv, kapsoRequest } from './lib/databases/kapso-api.js';
import { hasHelpFlag, parseFlags, requireFlag, parseNumber } from './lib/databases/args.js';

function ok(data) {
  return { ok: true, data };
}

function err(message, details) {
  return { ok: false, error: { message, details } };
}

async function main() {
  const argv = process.argv.slice(2);
  if (hasHelpFlag(argv)) {
    console.log(
      JSON.stringify(
        {
          ok: true,
          usage: 'node scripts/get-table.js --table <name> [--limit <n>]',
          env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
        },
        null,
        2
      )
    );
    return 0;
  }

  try {
    const flags = parseFlags(argv);
    const table = requireFlag(flags, 'table');
    const limit = parseNumber(flags.limit, 'limit');
    const query = limit !== undefined ? `?limit=${encodeURIComponent(String(limit))}` : '';
    const config = kapsoConfigFromEnv();
    const data = await kapsoRequest(config, `/platform/v1/database_tables/${encodeURIComponent(table)}${query}`);
    console.log(JSON.stringify(ok(data), null, 2));
    return 0;
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    console.error(JSON.stringify(err('Command failed', { message }), null, 2));
    return 1;
  }
}

main().then((code) => process.exit(code));
```

## File: `skills/automate-whatsapp/scripts/get-workflow.js`
```javascript
#!/usr/bin/env node
import { loadConfig, requestJson } from './lib/workflows/kapso-api.js';
import { ok, err, printJson } from './lib/workflows/result.js';
import { parseArgs, getFlag, getBooleanFlag } from './lib/workflows/args.js';

function usage() {
  return ok({
    usage: 'node scripts/get-workflow.js <workflow-id> [--workflow-id <id>]',
    env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
  });
}

async function main() {
  const parsed = parseArgs(process.argv.slice(2));
  if (getBooleanFlag(parsed.flags, 'help') || getBooleanFlag(parsed.flags, 'h')) {
    printJson(usage());
    return 0;
  }

  const workflowId = parsed.args[0] || getFlag(parsed.flags, 'workflow-id');
  if (!workflowId) {
    printJson(err('workflow_id is required'));
    return 2;
  }

  const config = loadConfig();
  const response = await requestJson(config, {
    method: 'GET',
    path: `/platform/v1/workflows/${workflowId}`
  });

  if (!response.ok) {
    printJson(err('Failed to fetch workflow', response.raw, false, response.status));
    return 2;
  }

  printJson(ok({ workflow: response.data }));
  return 0;
}

main().catch((error) => {
  printJson(err('Unhandled error', { message: String(error?.message || error) }));
  process.exit(1);
});
```

## File: `skills/automate-whatsapp/scripts/invoke-function.js`
```javascript
import { readFileSync } from 'node:fs';
import { kapsoConfigFromEnv, kapsoRequest } from './lib/functions/kapso-api.js';
import { hasHelpFlag, parseFlags, requireFlag, parseJsonValue } from './lib/functions/args.js';

function ok(data) {
  return { ok: true, data };
}

function err(message, details) {
  return { ok: false, error: { message, details } };
}

function resolvePayload(flags) {
  if (typeof flags.payload === 'string' && flags.payload.length > 0) {
    return parseJsonValue(flags.payload, 'payload');
  }
  if (typeof flags['payload-file'] === 'string' && flags['payload-file'].length > 0) {
    return JSON.parse(readFileSync(flags['payload-file'], 'utf8'));
  }
  throw new Error('Provide --payload or --payload-file');
}

async function main() {
  const argv = process.argv.slice(2);
  if (hasHelpFlag(argv)) {
    console.log(
      JSON.stringify(
        {
          ok: true,
          usage:
            'node scripts/invoke-function.js --function-id <id> (--payload <json> | --payload-file <path>)',
          env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
        },
        null,
        2
      )
    );
    return 0;
  }

  try {
    const flags = parseFlags(argv);
    const functionId = requireFlag(flags, 'function-id');
    const payload = resolvePayload(flags);
    const config = kapsoConfigFromEnv();
    const data = await kapsoRequest(config, `/platform/v1/functions/${encodeURIComponent(functionId)}/invoke`, {
      method: 'POST',
      body: JSON.stringify(payload)
    });

    console.log(JSON.stringify(ok(data), null, 2));
    return 0;
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    console.error(JSON.stringify(err('Command failed', { message }), null, 2));
    return 1;
  }
}

main().then((code) => process.exit(code));
```

## File: `skills/automate-whatsapp/scripts/list-accounts.js`
```javascript
#!/usr/bin/env node
import { loadConfig, requestJson } from './lib/workflows/kapso-api.js';
import { ok, err, printJson } from './lib/workflows/result.js';
import { parseArgs, getFlag, getBooleanFlag } from './lib/workflows/args.js';

function usage() {
  return ok({
    usage: 'node scripts/list-accounts.js [--app-slug <slug>]',
    notes: [
      'Use accounts[].pipedream_account_id for any --account-id flag.',
      'The internal accounts[].id will not work for integrations.'
    ],
    env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
  });
}

function normalizeAccounts(payload) {
  if (Array.isArray(payload?.accounts)) return payload.accounts;
  if (Array.isArray(payload?.accounts?.accounts)) return payload.accounts.accounts;
  if (Array.isArray(payload)) return payload;
  return [];
}

async function main() {
  const parsed = parseArgs(process.argv.slice(2));
  if (getBooleanFlag(parsed.flags, 'help') || getBooleanFlag(parsed.flags, 'h')) {
    printJson(usage());
    return 0;
  }

  const config = loadConfig();
  const response = await requestJson(config, {
    method: 'GET',
    path: '/platform/v1/integrations/accounts',
    query: {
      app_slug: getFlag(parsed.flags, 'app-slug')
    }
  });

  if (!response.ok) {
    printJson(err('Failed to list accounts', response.raw, false, response.status));
    return 2;
  }

  const raw = response.data;
  const accounts = normalizeAccounts(raw).map((account) => ({
    ...account,
    preferred_account_id: account.pipedream_account_id
  }));
  const payload = Array.isArray(raw) ? accounts : { ...raw, accounts };

  printJson(ok({
    accounts: payload,
    note: 'Use preferred_account_id (pipedream_account_id) for create-integration/configure-prop.'
  }));
  return 0;
}

main().catch((error) => {
  printJson(err('Unhandled error', { message: String(error?.message || error) }));
  process.exit(1);
});
```

## File: `skills/automate-whatsapp/scripts/list-apps.js`
```javascript
#!/usr/bin/env node
import { loadConfig, requestJson } from './lib/workflows/kapso-api.js';
import { ok, err, printJson } from './lib/workflows/result.js';
import { parseArgs, getFlag, getBooleanFlag, getNumberFlag } from './lib/workflows/args.js';

function usage() {
  return ok({
    usage: 'node scripts/list-apps.js [--query <text>] [--limit <n>]',
    env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
  });
}

async function main() {
  const parsed = parseArgs(process.argv.slice(2));
  if (getBooleanFlag(parsed.flags, 'help') || getBooleanFlag(parsed.flags, 'h')) {
    printJson(usage());
    return 0;
  }

  const config = loadConfig();
  const response = await requestJson(config, {
    method: 'GET',
    path: '/platform/v1/integrations/apps',
    query: {
      query: getFlag(parsed.flags, 'query'),
      limit: getNumberFlag(parsed.flags, 'limit')
    }
  });

  if (!response.ok) {
    printJson(err('Failed to list apps', response.raw, false, response.status));
    return 2;
  }

  printJson(ok({ apps: response.data }));
  return 0;
}

main().catch((error) => {
  printJson(err('Unhandled error', { message: String(error?.message || error) }));
  process.exit(1);
});
```

## File: `skills/automate-whatsapp/scripts/list-execution-events.js`
```javascript
#!/usr/bin/env node
import { loadConfig, requestJson } from './lib/workflows/kapso-api.js';
import { ok, err, printJson } from './lib/workflows/result.js';
import { parseArgs, getFlag, getBooleanFlag, getNumberFlag } from './lib/workflows/args.js';

function usage() {
  return ok({
    usage:
      'node scripts/list-execution-events.js <execution-id> [--event-type <type>] [--page <n>] [--per-page <n>]',
    env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
  });
}

async function main() {
  const parsed = parseArgs(process.argv.slice(2));
  if (getBooleanFlag(parsed.flags, 'help') || getBooleanFlag(parsed.flags, 'h')) {
    printJson(usage());
    return 0;
  }

  const executionId = parsed.args[0] || getFlag(parsed.flags, 'execution-id');
  if (!executionId) {
    printJson(err('execution_id is required'));
    return 2;
  }

  const config = loadConfig();
  const response = await requestJson(config, {
    method: 'GET',
    path: `/platform/v1/workflow_executions/${executionId}/events`,
    query: {
      event_type: getFlag(parsed.flags, 'event-type'),
      page: getNumberFlag(parsed.flags, 'page') ?? getNumberFlag(parsed.flags, 'offset'),
      per_page: getNumberFlag(parsed.flags, 'per-page') ?? getNumberFlag(parsed.flags, 'limit')
    }
  });

  if (!response.ok && response.status === 404) {
    printJson(err('Execution events endpoint is not available in the Platform API.', {
      endpoint: '/platform/v1/workflow_executions/:id/events'
    }, true, response.status));
    return 2;
  }

  if (!response.ok) {
    printJson(err('Failed to fetch execution events', response.raw, false, response.status));
    return 2;
  }

  printJson(ok({
    execution_id: executionId,
    events: response.data
  }));

  return 0;
}

main().catch((error) => {
  printJson(err('Unhandled error', { message: String(error?.message || error) }));
  process.exit(1);
});
```

## File: `skills/automate-whatsapp/scripts/list-executions.js`
```javascript
#!/usr/bin/env node
import { loadConfig, requestJson } from './lib/workflows/kapso-api.js';
import { ok, err, printJson } from './lib/workflows/result.js';
import { parseArgs, getFlag, getBooleanFlag, getNumberFlag } from './lib/workflows/args.js';

function usage() {
  return ok({
    usage: 'node scripts/list-executions.js <workflow-id> [--status <status>] [--waiting-reason <value>] [--whatsapp-conversation-id <id>] [--created-after <iso>] [--created-before <iso>] [--page <n>] [--per-page <n>]',
    env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
  });
}

async function main() {
  const parsed = parseArgs(process.argv.slice(2));
  if (getBooleanFlag(parsed.flags, 'help') || getBooleanFlag(parsed.flags, 'h')) {
    printJson(usage());
    return 0;
  }

  const workflowId = parsed.args[0] || getFlag(parsed.flags, 'workflow-id');
  if (!workflowId) {
    printJson(err('workflow_id is required'));
    return 2;
  }

  const config = loadConfig();
  const response = await requestJson(config, {
    method: 'GET',
    path: `/platform/v1/workflows/${workflowId}/executions`,
    query: {
      status: getFlag(parsed.flags, 'status'),
      waiting_reason: getFlag(parsed.flags, 'waiting-reason'),
      whatsapp_conversation_id: getFlag(parsed.flags, 'whatsapp-conversation-id'),
      created_after: getFlag(parsed.flags, 'created-after'),
      created_before: getFlag(parsed.flags, 'created-before'),
      page: getNumberFlag(parsed.flags, 'page'),
      per_page: getNumberFlag(parsed.flags, 'per-page')
    }
  });

  if (!response.ok) {
    printJson(err('Failed to list executions', response.raw, false, response.status));
    return 2;
  }

  printJson(ok({ executions: response.data }));
  return 0;
}

main().catch((error) => {
  printJson(err('Unhandled error', { message: String(error?.message || error) }));
  process.exit(1);
});
```

## File: `skills/automate-whatsapp/scripts/list-function-invocations.js`
```javascript
import { hasHelpFlag, parseFlags, requireFlag } from './lib/functions/args.js';
import { kapsoConfigFromEnv, kapsoRequest } from './lib/functions/kapso-api.js';

function ok(data) {
  return { ok: true, data };
}

function err(message, details) {
  return { ok: false, error: { message, details } };
}

async function main() {
  const argv = process.argv.slice(2);
  if (hasHelpFlag(argv)) {
    console.log(
      JSON.stringify(
        {
          ok: true,
          usage:
            'node scripts/list-function-invocations.js --function-id <id> [--status <success|failed>] [--limit <n>]',
          env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
        },
        null,
        2
      )
    );
    return 0;
  }

  try {
    const flags = parseFlags(argv);
    const functionId = requireFlag(flags, 'function-id');
    const params = new URLSearchParams();

    if (flags.status) params.set('status', flags.status);
    if (flags.limit) params.set('limit', flags.limit);

    const config = kapsoConfigFromEnv();
    const data = await kapsoRequest(
      config,
      `/platform/v1/functions/${encodeURIComponent(functionId)}/invocations${params.toString() ? `?${params.toString()}` : ''}`
    );

    console.log(JSON.stringify(ok(data), null, 2));
    return 0;
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    console.error(JSON.stringify(err('Command failed', { message }), null, 2));
    return 1;
  }
}

main().then((code) => process.exit(code));
```

## File: `skills/automate-whatsapp/scripts/list-functions.js`
```javascript
import { kapsoConfigFromEnv, kapsoRequest } from './lib/functions/kapso-api.js';
import { hasHelpFlag } from './lib/functions/args.js';

function ok(data) {
  return { ok: true, data };
}

function err(message, details) {
  return { ok: false, error: { message, details } };
}

async function main() {
  const argv = process.argv.slice(2);
  if (hasHelpFlag(argv)) {
    console.log(
      JSON.stringify(
        {
          ok: true,
          usage: 'node scripts/list-functions.js',
          env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
        },
        null,
        2
      )
    );
    return 0;
  }

  try {
    const config = kapsoConfigFromEnv();
    const data = await kapsoRequest(config, '/platform/v1/functions');
    console.log(JSON.stringify(ok(data), null, 2));
    return 0;
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    console.error(JSON.stringify(err('Command failed', { message }), null, 2));
    return 1;
  }
}

main().then((code) => process.exit(code));
```

## File: `skills/automate-whatsapp/scripts/list-integrations.js`
```javascript
#!/usr/bin/env node
import { loadConfig, requestJson } from './lib/workflows/kapso-api.js';
import { ok, err, printJson } from './lib/workflows/result.js';
import { parseArgs, getBooleanFlag } from './lib/workflows/args.js';

function usage() {
  return ok({
    usage: 'node scripts/list-integrations.js',
    notes: [
      'Check integrations[].variable_definitions to see required tool inputs.'
    ],
    env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
  });
}

async function main() {
  const parsed = parseArgs(process.argv.slice(2));
  if (getBooleanFlag(parsed.flags, 'help') || getBooleanFlag(parsed.flags, 'h')) {
    printJson(usage());
    return 0;
  }

  const config = loadConfig();
  const response = await requestJson(config, {
    method: 'GET',
    path: '/platform/v1/integrations'
  });

  if (!response.ok) {
    printJson(err('Failed to list integrations', response.raw, false, response.status));
    return 2;
  }

  printJson(ok({ integrations: response.data }));
  return 0;
}

main().catch((error) => {
  printJson(err('Unhandled error', { message: String(error?.message || error) }));
  process.exit(1);
});
```

## File: `skills/automate-whatsapp/scripts/list-provider-models.js`
```javascript
#!/usr/bin/env node
import { loadConfig, requestJson } from './lib/workflows/kapso-api.js';
import { ok, err, printJson } from './lib/workflows/result.js';
import { parseArgs, getBooleanFlag } from './lib/workflows/args.js';

function usage() {
  return ok({
    usage: 'node scripts/list-provider-models.js',
    env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
  });
}

async function main() {
  const parsed = parseArgs(process.argv.slice(2));
  if (getBooleanFlag(parsed.flags, 'help') || getBooleanFlag(parsed.flags, 'h')) {
    printJson(usage());
    return 0;
  }

  const config = loadConfig();
  const response = await requestJson(config, {
    method: 'GET',
    path: '/platform/v1/provider_models'
  });

  if (!response.ok && response.status === 404) {
    printJson(err('Provider models endpoint is not available in the Platform API.', {
      endpoint: '/platform/v1/provider_models'
    }, true, response.status));
    return 2;
  }

  if (!response.ok) {
    printJson(err('Failed to fetch provider models', response.raw, false, response.status));
    return 2;
  }

  printJson(ok({
    provider_models: response.data
  }));

  return 0;
}

main().catch((error) => {
  printJson(err('Unhandled error', { message: String(error?.message || error) }));
  process.exit(1);
});
```

## File: `skills/automate-whatsapp/scripts/list-tables.js`
```javascript
import { kapsoConfigFromEnv, kapsoRequest } from './lib/databases/kapso-api.js';
import { hasHelpFlag } from './lib/databases/args.js';

function ok(data) {
  return { ok: true, data };
}

function err(message, details) {
  return { ok: false, error: { message, details } };
}

async function main() {
  const argv = process.argv.slice(2);
  if (hasHelpFlag(argv)) {
    console.log(
      JSON.stringify(
        {
          ok: true,
          usage: 'node scripts/list-tables.js',
          env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
        },
        null,
        2
      )
    );
    return 0;
  }

  try {
    const config = kapsoConfigFromEnv();
    const data = await kapsoRequest(config, '/platform/v1/database_tables');
    console.log(JSON.stringify(ok(data), null, 2));
    return 0;
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    console.error(JSON.stringify(err('Command failed', { message }), null, 2));
    return 1;
  }
}

main().then((code) => process.exit(code));
```

## File: `skills/automate-whatsapp/scripts/list-triggers.js`
```javascript
#!/usr/bin/env node
import { loadConfig, requestJson } from './lib/workflows/kapso-api.js';
import { ok, err, printJson } from './lib/workflows/result.js';
import { parseArgs, getFlag, getBooleanFlag } from './lib/workflows/args.js';

function usage() {
  return ok({
    usage: 'node scripts/list-triggers.js <workflow-id> [--workflow-id <id>]',
    env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
  });
}

async function main() {
  const parsed = parseArgs(process.argv.slice(2));
  if (getBooleanFlag(parsed.flags, 'help') || getBooleanFlag(parsed.flags, 'h')) {
    printJson(usage());
    return 0;
  }

  const workflowId = parsed.args[0] || getFlag(parsed.flags, 'workflow-id');
  if (!workflowId) {
    printJson(err('workflow_id is required'));
    return 2;
  }

  const config = loadConfig();
  const response = await requestJson(config, {
    method: 'GET',
    path: `/platform/v1/workflows/${workflowId}/triggers`
  });

  if (!response.ok) {
    printJson(err('Failed to list triggers', response.raw, false, response.status));
    return 2;
  }

  printJson(ok({ triggers: response.data }));
  return 0;
}

main().catch((error) => {
  printJson(err('Unhandled error', { message: String(error?.message || error) }));
  process.exit(1);
});
```

## File: `skills/automate-whatsapp/scripts/list-whatsapp-phone-numbers.js`
```javascript
#!/usr/bin/env node
import { loadConfig, requestJson } from './lib/workflows/kapso-api.js';
import { ok, err, printJson } from './lib/workflows/result.js';
import { parseArgs, getBooleanFlag, getNumberFlag } from './lib/workflows/args.js';

function usage() {
  return ok({
    usage: 'node scripts/list-whatsapp-phone-numbers.js [--per-page <n>] [--page <n>]',
    env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
  });
}

function extractPhoneNumbers(payload) {
  if (Array.isArray(payload?.data)) return payload.data;
  if (Array.isArray(payload?.phone_numbers)) return payload.phone_numbers;
  if (Array.isArray(payload)) return payload;
  return [];
}

async function main() {
  const parsed = parseArgs(process.argv.slice(2));
  if (getBooleanFlag(parsed.flags, 'help') || getBooleanFlag(parsed.flags, 'h')) {
    printJson(usage());
    return 0;
  }

  const config = loadConfig();
  const response = await requestJson(config, {
    method: 'GET',
    path: '/platform/v1/whatsapp/phone_numbers',
    query: {
      per_page: getNumberFlag(parsed.flags, 'per-page'),
      page: getNumberFlag(parsed.flags, 'page')
    }
  });

  if (!response.ok) {
    printJson(err('Failed to list WhatsApp phone numbers', response.raw, false, response.status));
    return 2;
  }

  const payload = response.data;
  const phoneNumbers = extractPhoneNumbers(payload);

  printJson(ok({
    phone_numbers: phoneNumbers,
    raw: payload,
    note: 'Use phone_number_id for inbound_message triggers.'
  }));
  return 0;
}

main().catch((error) => {
  printJson(err('Unhandled error', { message: String(error?.message || error) }));
  process.exit(1);
});
```

## File: `skills/automate-whatsapp/scripts/list-workflows.js`
```javascript
#!/usr/bin/env node
import { loadConfig, requestJson } from './lib/workflows/kapso-api.js';
import { ok, err, printJson } from './lib/workflows/result.js';
import { parseArgs, getFlag, getBooleanFlag } from './lib/workflows/args.js';

function usage() {
  return ok({
    usage: 'node scripts/list-workflows.js [--status <status>] [--name-contains <text>] [--created-after <iso>] [--created-before <iso>]',
    env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
  });
}

async function main() {
  const parsed = parseArgs(process.argv.slice(2));
  if (getBooleanFlag(parsed.flags, 'help') || getBooleanFlag(parsed.flags, 'h')) {
    printJson(usage());
    return 0;
  }

  const config = loadConfig();
  const response = await requestJson(config, {
    method: 'GET',
    path: '/platform/v1/workflows',
    query: {
      status: getFlag(parsed.flags, 'status'),
      name_contains: getFlag(parsed.flags, 'name-contains'),
      created_after: getFlag(parsed.flags, 'created-after'),
      created_before: getFlag(parsed.flags, 'created-before')
    }
  });

  if (!response.ok) {
    printJson(err('Failed to list workflows', response.raw, false, response.status));
    return 2;
  }

  printJson(ok({ workflows: response.data }));
  return 0;
}

main().catch((error) => {
  printJson(err('Unhandled error', { message: String(error?.message || error) }));
  process.exit(1);
});
```

## File: `skills/automate-whatsapp/scripts/openapi-explore.mjs`
```
#!/usr/bin/env node

import { readFileSync, readdirSync, statSync } from 'fs'
import path from 'path'
import { fileURLToPath } from 'url'
import { parse as parseYaml } from 'yaml'

const HTTP_METHODS = ['get', 'post', 'put', 'patch', 'delete', 'options', 'head']
const DEFAULT_PUBLISHED_WHATSAPP_OPENAPI = 'https://docs.kapso.ai/api/meta/whatsapp/openapi-whatsapp.yaml'
const SCRIPT_DIR = path.dirname(fileURLToPath(import.meta.url))

function printHelp(exitCode = 0) {
  const msg = `
Explore OpenAPI specs (YAML)

Usage:
  node openapi-explore.mjs [openapi.yaml ...] <command> [args]
  node openapi-explore.mjs [--file <path> ...] <command> [args]
  node openapi-explore.mjs --all <command> [args]

Default (no files passed):
  Loads the published OpenAPI files from docs.kapso.ai:
  - ${DEFAULT_PUBLISHED_WHATSAPP_OPENAPI}
  - (plus platform + workflows, deduced from that URL)

Fallback:
  If it can't fetch the published specs (offline, etc.), it falls back to local repo files:
  api/**/openapi-*.yaml

Use --all to force local auto-discovery.

Commands:
  specs
  tags [--spec <id>]
  ops [--spec <id>] [--tag <tag>] [--q <query>]
  search <query> [--spec <id>]
  op <operationId | specId:operationId | "METHOD /path"> [--spec <id>]
  schema <SchemaName | specId:SchemaName> [--spec <id>]
  where <SchemaName | specId:SchemaName> [--spec <id>]

Flags:
  --file, -f <path>     Load a spec file (repeatable)
  --all                 Load all api/**/openapi-*.yaml files
  --spec <id>           Filter by spec id (platform, workflows, whatsapp, ...)
  --json                Output JSON (search/ops/where)
  --limit <n>           Limit results (default 30)
`
  console.log(msg.trim())
  process.exit(exitCode)
}

function die(msg, exitCode = 1) {
  console.error(msg)
  process.exit(exitCode)
}

function parseArgs(argv) {
  const args = [...argv]
  const opts = { files: [], all: false, spec: null, json: false, limit: 30, tag: null, q: null }
  let command = null
  const rest = []

  for (let i = 0; i < args.length; i++) {
    const a = args[i]
    if (a === '--help' || a === '-h') printHelp(0)

    if (a === '--all') {
      opts.all = true
      continue
    }
    if (a === '--json') {
      opts.json = true
      continue
    }
    if (a === '--file' || a === '-f') {
      const p = args[++i]
      if (!p) die('Missing value for --file')
      opts.files.push(p)
      continue
    }
    if (a === '--spec') {
      opts.spec = args[++i] || null
      if (!opts.spec) die('Missing value for --spec')
      continue
    }
    if (a === '--limit') {
      const raw = args[++i]
      const n = Number(raw)
      if (!Number.isFinite(n) || n <= 0) die(`Invalid --limit: ${raw}`)
      opts.limit = n
      continue
    }
    if (a === '--tag') {
      opts.tag = args[++i] || null
      if (!opts.tag) die('Missing value for --tag')
      continue
    }
    if (a === '--q') {
      opts.q = args[++i] || null
      if (!opts.q) die('Missing value for --q')
      continue
    }

    if (!command && (a.endsWith('.yaml') || a.endsWith('.yml'))) {
      opts.files.push(a)
      continue
    }

    if (!command) command = a
    else rest.push(a)
  }

  return { opts, command, rest }
}

function walk(dir, { filePattern, maxDepth = 10 } = {}, depth = 0, out = []) {
  if (depth > maxDepth) return out
  let entries
  try {
    entries = readdirSync(dir)
  } catch {
    return out
  }

  for (const entry of entries) {
    const full = path.join(dir, entry)
    let st
    try {
      st = statSync(full)
    } catch {
      continue
    }

    if (st.isDirectory()) {
      walk(full, { filePattern, maxDepth }, depth + 1, out)
    } else if (!filePattern || filePattern.test(entry)) {
      out.push(full)
    }
  }

  return out
}

function findUpDir(startDir, targetDirName, { maxDepth = 12 } = {}) {
  let current = path.resolve(startDir)
  for (let i = 0; i <= maxDepth; i++) {
    const candidate = path.join(current, targetDirName)
    try {
      const st = statSync(candidate)
      if (st.isDirectory()) return candidate
    } catch {
      // ignore
    }

    const parent = path.dirname(current)
    if (parent === current) break
    current = parent
  }
  return null
}

function findLocalApiDir() {
  return findUpDir(process.cwd(), 'api') || findUpDir(SCRIPT_DIR, 'api')
}

function isUrl(s) {
  return /^https?:\/\//i.test(String(s))
}

function deducePublishedOpenApiUrls(whatsappUrl = DEFAULT_PUBLISHED_WHATSAPP_OPENAPI) {
  const u = new URL(whatsappUrl)
  const origin = u.origin
  return [
    whatsappUrl,
    new URL('/api/platform/v1/openapi-platform.yaml', origin).toString(),
    new URL('/api/platform/v1/openapi-workflows.yaml', origin).toString(),
  ]
}

function inferSpecId(filePath, spec) {
  const base = (isUrl(filePath) ? path.basename(new URL(filePath).pathname) : path.basename(filePath)).toLowerCase()
  if (base.includes('whatsapp')) return 'whatsapp'
  if (base.includes('workflows')) return 'workflows'
  if (base.includes('platform')) return 'platform'

  const title = (spec?.info?.title || '').toLowerCase()
  if (title.includes('whatsapp')) return 'whatsapp'
  if (title.includes('workflow')) return 'workflows'
  if (title.includes('platform')) return 'platform'

  return base.replace(/^openapi-/, '').replace(/\.(ya?ml)$/, '') || 'spec'
}

function decodeJsonPointerToken(token) {
  return token.replaceAll('~1', '/').replaceAll('~0', '~')
}

function getByJsonPointer(doc, pointer) {
  if (!pointer || !pointer.startsWith('#/')) return null
  const parts = pointer.slice(2).split('/').map(decodeJsonPointerToken)
  let cur = doc
  for (const part of parts) {
    if (cur == null) return null
    cur = cur[part]
  }
  return cur ?? null
}

function refName(ref) {
  if (!ref) return null
  const parts = String(ref).split('/')
  return parts[parts.length - 1] || null
}

function derefObject(obj, doc, stack = new Set()) {
  if (!obj?.$ref) return obj
  const ref = String(obj.$ref)
  if (stack.has(ref)) return obj
  stack.add(ref)
  const resolved = getByJsonPointer(doc, ref)
  if (!resolved) return obj
  return derefObject(resolved, doc, stack)
}

function schemaTypeString(schema) {
  if (!schema) return 'any'
  if (schema.$ref) return refName(schema.$ref) || 'ref'
  if (schema.const !== undefined) return `const ${JSON.stringify(schema.const)}`
  if (schema.enum?.length) {
    const vals = schema.enum.slice(0, 6).map((v) => JSON.stringify(v)).join(' | ')
    return schema.enum.length > 6 ? `enum(${vals} | ...)` : `enum(${vals})`
  }
  if (schema.type) {
    if (Array.isArray(schema.type)) return schema.type.join('|')
    return schema.type
  }
  if (schema.oneOf) return 'oneOf'
  if (schema.anyOf) return 'anyOf'
  if (schema.allOf) return 'allOf'
  if (schema.properties) return 'object'
  if (schema.items) return 'array'
  return 'any'
}

function normalizeType(schema) {
  if (!schema) return null
  const t = schema.type
  if (!t) return null
  if (Array.isArray(t)) {
    const nonNull = t.find((x) => x !== 'null')
    return nonNull || t[0] || null
  }
  return t
}

function mergeAllOf(schema, doc, seen = new Set()) {
  if (!schema?.allOf?.length) return schema

  const out = { ...schema }
  delete out.allOf

  let merged = { type: 'object', properties: {}, required: [] }

  for (const part of schema.allOf) {
    let s = part
    if (s?.$ref) {
      const name = refName(s.$ref)
      if (name) {
        if (seen.has(name)) continue
        seen.add(name)
      }
      s = getByJsonPointer(doc, s.$ref) || s
    }
    if (s?.allOf) s = mergeAllOf(s, doc, seen)

    if (s?.type && normalizeType(s) !== 'object' && s.properties) {
      // some specs omit type: object but still have properties
    } else if (normalizeType(s) && normalizeType(s) !== 'object' && !s.properties) {
      return schema
    }

    if (s?.properties) Object.assign(merged.properties, s.properties)
    if (Array.isArray(s?.required)) merged.required.push(...s.required)
    if (s?.description && !merged.description) merged.description = s.description
  }

  merged.required = [...new Set(merged.required)]
  return { ...merged, ...out }
}

function formatSchemaPreview(schema, doc, { depth = 2, maxProps = 12 } = {}, indent = '', refStack = new Set()) {
  if (!schema) return [`${indent}any`]

  if (schema.$ref) {
    const name = refName(schema.$ref) || schema.$ref
    const resolved = getByJsonPointer(doc, schema.$ref)
    const lines = [`${indent}${name}`]
    const refKey = String(schema.$ref)
    if (refStack.has(refKey)) return lines
    refStack.add(refKey)
    if (resolved && depth > 0) {
      const next = resolved?.allOf ? mergeAllOf(resolved, doc) : resolved
      const childLines = formatSchemaPreview(next, doc, { depth, maxProps }, indent + '  ', refStack)
      // Avoid printing a single redundant "object" line for refs
      if (!(childLines.length === 1 && childLines[0].trim() === 'object')) lines.push(...childLines)
    }
    refStack.delete(refKey)
    return lines
  }

  const normalized = schema.allOf ? mergeAllOf(schema, doc) : schema

  const t = normalizeType(normalized) || schemaTypeString(normalized)
  if (t === 'object' || normalized.properties) {
    const props = normalized.properties || {}
    const required = new Set(normalized.required || [])
    const keys = Object.keys(props)
    if (!keys.length) return [`${indent}object`]

    const lines = []
    for (const key of keys.slice(0, maxProps)) {
      const s = props[key]
      const typeStr = schemaTypeString(s)
      const req = required.has(key) ? ' (required)' : ''
      const desc = s?.description ? ` - ${String(s.description).replaceAll('\n', ' ').slice(0, 80)}` : ''
      lines.push(`${indent}- ${key}: ${typeStr}${req}${desc}`)
      if (depth > 0) {
        const child = s?.$ref ? getByJsonPointer(doc, s.$ref) : s
        const childNorm = child?.allOf ? mergeAllOf(child, doc) : child
        const childType = normalizeType(childNorm)
        if (childType === 'object' || childNorm?.properties || childNorm?.items) {
          const nested = formatSchemaPreview(childNorm, doc, { depth: depth - 1, maxProps }, indent + '  ', refStack)
          // Only include nested if it adds something beyond "object"/"array"
          if (!(nested.length === 1 && ['object', 'array'].includes(nested[0].trim()))) lines.push(...nested)
        }
      }
    }
    if (keys.length > maxProps) lines.push(`${indent}- ... (${keys.length - maxProps} more)`)
    return lines
  }

  if (t === 'array' || normalized.items) {
    const itemType = schemaTypeString(normalized.items)
    const lines = [`${indent}array<${itemType}>`]
    if (normalized.items && depth > 0) {
      const next = normalized.items?.$ref ? getByJsonPointer(doc, normalized.items.$ref) : normalized.items
      const nextNorm = next?.allOf ? mergeAllOf(next, doc) : next
      const nested = formatSchemaPreview(nextNorm, doc, { depth: depth - 1, maxProps }, indent + '  ', refStack)
      const nestedTrim = nested.length === 1 ? nested[0].trim() : null
      const redundant =
        nestedTrim === null ? false : ['object', 'array'].includes(nestedTrim) || nestedTrim === itemType
      if (!redundant) lines.push(...nested)
    }
    return lines
  }

  if (normalized.oneOf?.length) {
    const opts = normalized.oneOf.slice(0, 5).map((s) => schemaTypeString(s)).join(' | ')
    return [`${indent}oneOf(${opts}${normalized.oneOf.length > 5 ? ' | ...' : ''})`]
  }
  if (normalized.anyOf?.length) {
    const opts = normalized.anyOf.slice(0, 5).map((s) => schemaTypeString(s)).join(' | ')
    return [`${indent}anyOf(${opts}${normalized.anyOf.length > 5 ? ' | ...' : ''})`]
  }

  return [`${indent}${schemaTypeString(normalized)}`]
}

function placeholderForString(schema) {
  if (schema?.enum?.length) return schema.enum[0]
  if (schema?.const !== undefined) return schema.const
  if (schema?.format === 'uuid') return '00000000-0000-0000-0000-000000000000'
  if (schema?.format === 'date-time') return '2025-01-01T00:00:00Z'
  if (schema?.format === 'date') return '2025-01-01'
  if (schema?.format === 'email') return 'user@example.com'
  if (schema?.format === 'uri' || schema?.format === 'url') return 'https://example.com'
  return 'string'
}

function exampleFromSchema(schema, doc, { depth = 3, includeOptional = false } = {}, stack = new Set()) {
  if (!schema) return null

  if (schema.$ref) {
    const name = refName(schema.$ref)
    if (name) {
      if (stack.has(name)) return `<circular:${name}>`
      stack.add(name)
    }
    const resolved = getByJsonPointer(doc, schema.$ref)
    const out = exampleFromSchema(resolved || {}, doc, { depth, includeOptional }, stack)
    if (name) stack.delete(name)
    return out
  }

  const normalized = schema.allOf ? mergeAllOf(schema, doc) : schema

  if (normalized.const !== undefined) return normalized.const
  if (normalized.enum?.length) return normalized.enum[0]

  const t = normalizeType(normalized)
  if (t === 'string') return placeholderForString(normalized)
  if (t === 'integer') return 0
  if (t === 'number') return 0
  if (t === 'boolean') return true
  if (t === 'null') return null

  if ((t === 'array' || normalized.items) && depth > 0) {
    return [exampleFromSchema(normalized.items || {}, doc, { depth: depth - 1, includeOptional }, stack)]
  }

  if ((t === 'object' || normalized.properties || normalized.additionalProperties) && depth > 0) {
    const props = normalized.properties || {}
    const required = new Set(normalized.required || [])
    const out = {}

    const keys = Object.keys(props)
    for (const key of keys) {
      if (!includeOptional && !required.has(key)) continue
      out[key] = exampleFromSchema(props[key], doc, { depth: depth - 1, includeOptional }, stack)
    }

    // If it is a free-form map, add a placeholder entry.
    if (!keys.length && normalized.additionalProperties) {
      out.key = exampleFromSchema(
        normalized.additionalProperties === true ? {} : normalized.additionalProperties,
        doc,
        { depth: depth - 1, includeOptional },
        stack,
      )
    }

    return out
  }

  if (normalized.oneOf?.length) return exampleFromSchema(normalized.oneOf[0], doc, { depth, includeOptional }, stack)
  if (normalized.anyOf?.length) return exampleFromSchema(normalized.anyOf[0], doc, { depth, includeOptional }, stack)

  return null
}

function collectSchemaRefs(schema, doc, out = new Set(), stack = new Set()) {
  if (!schema) return out

  if (schema.$ref) {
    const name = refName(schema.$ref)
    if (name) out.add(name)
    if (name) {
      if (stack.has(name)) return out
      stack.add(name)
    }
    const resolved = getByJsonPointer(doc, schema.$ref)
    if (resolved) collectSchemaRefs(resolved, doc, out, stack)
    if (name) stack.delete(name)
    return out
  }

  const normalized = schema.allOf ? mergeAllOf(schema, doc) : schema

  for (const key of ['oneOf', 'anyOf', 'allOf']) {
    if (Array.isArray(normalized[key])) {
      for (const s of normalized[key]) collectSchemaRefs(s, doc, out, stack)
    }
  }

  if (normalized.properties) {
    for (const s of Object.values(normalized.properties)) collectSchemaRefs(s, doc, out, stack)
  }
  if (normalized.items) collectSchemaRefs(normalized.items, doc, out, stack)
  if (normalized.additionalProperties && normalized.additionalProperties !== true) {
    collectSchemaRefs(normalized.additionalProperties, doc, out, stack)
  }

  return out
}

function collectSchemaFieldNames(schema, doc, out = new Set(), stack = new Set(), depth = 3) {
  if (!schema || depth < 0) return out

  if (schema.$ref) {
    const ref = String(schema.$ref)
    if (stack.has(ref)) return out
    stack.add(ref)
    const resolved = getByJsonPointer(doc, ref)
    if (resolved) collectSchemaFieldNames(resolved, doc, out, stack, depth)
    stack.delete(ref)
    return out
  }

  const normalized = schema.allOf ? mergeAllOf(schema, doc) : schema

  for (const key of ['oneOf', 'anyOf', 'allOf']) {
    if (Array.isArray(normalized[key])) {
      for (const s of normalized[key]) collectSchemaFieldNames(s, doc, out, stack, depth)
    }
  }

  if (normalized.properties) {
    for (const [k, s] of Object.entries(normalized.properties)) {
      out.add(k)
      collectSchemaFieldNames(s, doc, out, stack, depth - 1)
    }
  }

  if (normalized.items) collectSchemaFieldNames(normalized.items, doc, out, stack, depth - 1)
  if (normalized.additionalProperties && normalized.additionalProperties !== true) {
    collectSchemaFieldNames(normalized.additionalProperties, doc, out, stack, depth - 1)
  }

  return out
}

function normalizeOperationSecurity(op, spec) {
  if (Object.prototype.hasOwnProperty.call(op, 'security')) return op.security
  return spec.security
}

function securityLabel(opSecurity, spec) {
  if (!opSecurity) return null
  if (Array.isArray(opSecurity) && opSecurity.length === 0) return 'none'

  const schemes = spec?.components?.securitySchemes || {}

  function schemeLabel(name) {
    const s = schemes[name]
    if (!s) return name
    if (s.type === 'apiKey' && s.in === 'header' && s.name) return `${name} (${s.name} header)`
    if (s.type === 'apiKey' && s.in) return `${name} (apiKey in ${s.in})`
    if (s.type === 'http' && s.scheme === 'bearer') return `${name} (Authorization: Bearer ...)`
    if (s.type === 'http') return `${name} (http ${s.scheme || ''})`.trim()
    return `${name} (${s.type})`
  }

  const requirementSets = []
  for (const req of opSecurity || []) {
    const keys = Object.keys(req || {})
    if (!keys.length) continue
    requirementSets.push(keys.map(schemeLabel).join(' + '))
  }

  if (!requirementSets.length) return null
  return requirementSets.join(' OR ')
}

function toShortSpec(s) {
  return {
    id: s.id,
    title: s.title,
    version: s.version,
    file: s.filePath,
    servers: s.servers,
    operations: s.operations.length,
    schemas: Object.keys(s.schemas).length,
  }
}

async function readSpecSource(source) {
  if (isUrl(source)) {
    const res = await fetch(source, {
      // Some CDNs / WAFs behave better with a UA.
      headers: { 'User-Agent': 'kapso-openapi-explore/1.0 (+https://docs.kapso.ai)' },
    })
    if (!res.ok) throw new Error(`HTTP ${res.status} ${res.statusText}`)
    return await res.text()
  }
  return readFileSync(source, 'utf-8')
}

async function loadSpecsAsync({ sources, sourceMode, specFilter }) {
  if (!sources.length) die('No OpenAPI sources provided')

  const seenIds = new Map()
  const specs = []
  const errors = []

  for (const filePath of sources) {
    let raw = null
    try {
      raw = await readSpecSource(filePath)
    } catch (e) {
      errors.push({ source: filePath, error: e })
      if (sourceMode === 'explicit') console.error(`Skipping ${filePath}: ${e.message}`)
      continue
    }

    let doc
    try {
      doc = parseYaml(raw)
    } catch (e) {
      errors.push({ source: filePath, error: e })
      console.error(`Skipping ${filePath}: YAML parse error: ${e.message}`)
      continue
    }

    const idBase = inferSpecId(filePath, doc)
    const n = (seenIds.get(idBase) || 0) + 1
    seenIds.set(idBase, n)
    const id = n === 1 ? idBase : `${idBase}${n}`

    if (specFilter && id !== specFilter) continue

    const title = doc?.info?.title || id
    const version = doc?.info?.version || '?'
    const servers = (doc?.servers || []).map((s) => s?.url).filter(Boolean)
    const tags = doc?.tags || []
    const schemas = doc?.components?.schemas || {}
    const schemaFieldCache = new Map()

    const getSchemaFields = (schemaName) => {
      if (schemaFieldCache.has(schemaName)) return schemaFieldCache.get(schemaName)
      const schema = schemas?.[schemaName]
      const fields = schema ? [...collectSchemaFieldNames(schema, doc)] : []
      schemaFieldCache.set(schemaName, fields)
      return fields
    }

    const operations = []
    const paths = doc?.paths || {}
    for (const [p, pathItemRaw] of Object.entries(paths)) {
      const pathItem = pathItemRaw || {}
      const pathParams = Array.isArray(pathItem.parameters) ? pathItem.parameters.map((x) => derefObject(x, doc)) : []

      for (const method of HTTP_METHODS) {
        const op = pathItem[method]
        if (!op) continue

        const mergedParams = [...pathParams, ...((op.parameters || []).filter(Boolean))]
          .map((x) => derefObject(x, doc))
          .filter(Boolean)
        const opSecurity = normalizeOperationSecurity(op, doc)
        const opRequestBody = derefObject(op.requestBody || null, doc)

        const refs = new Set()
        // params
        for (const param of mergedParams) {
          if (param?.schema) collectSchemaRefs(param.schema, doc, refs)
          if (param?.content) {
            for (const media of Object.values(param.content)) {
              if (media?.schema) collectSchemaRefs(media.schema, doc, refs)
            }
          }
        }
        // body
        if (opRequestBody?.content) {
          for (const media of Object.values(opRequestBody.content)) {
            if (media?.schema) collectSchemaRefs(media.schema, doc, refs)
          }
        }
        // responses
        if (op?.responses) {
          for (const resp of Object.values(op.responses)) {
            const r = derefObject(resp, doc)
            if (r?.content) {
              for (const media of Object.values(r.content)) {
                if (media?.schema) collectSchemaRefs(media.schema, doc, refs)
              }
            }
          }
        }

        const fieldsUsed = new Set()
        for (const schemaName of refs) {
          for (const f of getSchemaFields(schemaName)) fieldsUsed.add(f)
        }

        operations.push({
          specId: id,
          specTitle: title,
          specFile: filePath,
          method,
          path: p,
          operationId: op.operationId || null,
          summary: op.summary || null,
          description: op.description || null,
          tags: op.tags || [],
          deprecated: Boolean(op.deprecated),
          security: opSecurity,
          securityLabel: securityLabel(opSecurity, doc),
          parameters: mergedParams,
          requestBody: opRequestBody,
          responses: op.responses || {},
          refsUsed: refs,
          fieldsUsed,
        })
      }
    }

    specs.push({
      id,
      filePath,
      title,
      version,
      servers,
      doc,
      tags,
      schemas,
      operations,
    })
  }

  if (!specs.length) {
    if (sourceMode === 'default_remote' && errors.length) {
      const apiDir = findLocalApiDir()
      const local = apiDir ? walk(apiDir, { filePattern: /^openapi-.*\.ya?ml$/ }) : []
      if (local.length) {
        console.error(`Could not fetch published OpenAPI specs. Falling back to local repo specs (api/**/openapi-*.yaml).`)
        return await loadSpecsAsync({ sources: local, sourceMode: 'explicit', specFilter })
      }
    }
    if (specFilter) die(`No specs matched --spec ${specFilter}`)
    die('No specs loaded')
  }

  if (sourceMode === 'default_remote' && errors.length) {
    console.error(`Some published OpenAPI specs could not be fetched:`)
    for (const e of errors) console.error(`- ${e.source}: ${e.error?.message || String(e.error)}`)
  }

  return specs
}

function findOperation(specs, query, { specHint } = {}) {
  const raw = query.trim()
  const direct = raw.includes(':') ? raw.split(':') : null
  const qSpec = direct?.[0] || specHint
  const qId = direct?.[1] || raw

  // METHOD /path
  const m = raw.match(/^(get|post|put|patch|delete|options|head)\\s+(.+)$/i)
  if (m) {
    const method = m[1].toLowerCase()
    const p = m[2].trim()
    const matches = []
    for (const s of specs) {
      if (qSpec && s.id !== qSpec) continue
      for (const op of s.operations) {
        if (op.method === method && op.path === p) matches.push(op)
      }
    }
    return matches
  }

  // operationId
  const matches = []
  for (const s of specs) {
    if (qSpec && s.id !== qSpec) continue
    for (const op of s.operations) {
      if (op.operationId === qId) matches.push(op)
    }
  }
  return matches
}

function findSchema(specs, query, { specHint } = {}) {
  const raw = query.trim()
  const direct = raw.includes(':') ? raw.split(':') : null
  const qSpec = direct?.[0] || specHint
  const qName = direct?.[1] || raw

  const matches = []
  for (const s of specs) {
    if (qSpec && s.id !== qSpec) continue
    if (Object.prototype.hasOwnProperty.call(s.schemas, qName)) {
      matches.push({ spec: s, name: qName, schema: s.schemas[qName] })
    }
  }
  return matches
}

function scoreText(hay, q) {
  if (!hay) return 0
  const h = hay.toLowerCase()
  if (h === q) return 100
  if (h.startsWith(q)) return 60
  if (h.includes(q)) return 30
  return 0
}

function search(specs, query, { specHint, limit = 30 } = {}) {
  const q = query.toLowerCase().trim()
  if (!q) return { ops: [], schemas: [] }

  const ops = []
  const schemas = []

  for (const s of specs) {
    if (specHint && s.id !== specHint) continue

    for (const op of s.operations) {
      let score = 0
      score += scoreText(op.operationId, q) * 3
      score += scoreText(`${op.method} ${op.path}`, q) * 2
      score += scoreText(op.summary, q) * 2
      score += scoreText(op.description, q)
      for (const t of op.tags || []) score += scoreText(t, q) * 2
      score += scoreText((op.parameters || []).map((p) => p?.name).filter(Boolean).join(' '), q) * 2
      score += scoreText([...op.refsUsed].join(' '), q) * 2
      score += scoreText([...op.fieldsUsed].join(' '), q)
      if (score > 0) ops.push({ score, op })
    }

    for (const [name, schema] of Object.entries(s.schemas)) {
      let score = 0
      score += scoreText(name, q) * 3
      score += scoreText(schema?.description, q)
      score += scoreText([...collectSchemaFieldNames(schema, s.doc)].join(' '), q) * 2
      if (score > 0) schemas.push({ score, spec: s, name, schema })
    }
  }

  ops.sort((a, b) => b.score - a.score)
  schemas.sort((a, b) => b.score - a.score)

  return {
    ops: ops.slice(0, limit).map((x) => x.op),
    schemas: schemas.slice(0, limit).map((x) => ({ specId: x.spec.id, name: x.name })),
  }
}

function printTable(rows, { sep = '  ' } = {}) {
  if (!rows.length) return
  const widths = []
  for (const row of rows) {
    row.forEach((cell, i) => {
      widths[i] = Math.max(widths[i] || 0, String(cell).length)
    })
  }
  for (const row of rows) {
    const line = row
      .map((cell, i) => String(cell).padEnd(widths[i], ' '))
      .join(sep)
      .trimEnd()
    console.log(line)
  }
}

function printSpecs(specs, { json } = {}) {
  if (json) {
    console.log(JSON.stringify(specs.map(toShortSpec), null, 2))
    return
  }

  const rows = [['id', 'version', 'operations', 'schemas', 'file']]
  for (const s of specs) rows.push([s.id, s.version, String(s.operations.length), String(Object.keys(s.schemas).length), s.filePath])
  printTable(rows)
}

function printTags(specs, { specHint } = {}) {
  const rows = [['spec', 'tag', 'description']]
  for (const s of specs) {
    if (specHint && s.id !== specHint) continue
    for (const t of s.tags || []) rows.push([s.id, t.name, (t.description || '').replaceAll('\n', ' ').slice(0, 80)])
  }
  if (rows.length === 1) die('No tags found')
  printTable(rows)
}

function printOps(specs, { specHint, tag, q, json, limit = 30 } = {}) {
  let ops = []
  for (const s of specs) {
    if (specHint && s.id !== specHint) continue
    ops.push(...s.operations)
  }

  if (tag) ops = ops.filter((o) => (o.tags || []).includes(tag))

  if (q) {
    const res = search(specs, q, { specHint, limit: Math.max(limit, 200) })
    const opSet = new Set(res.ops.map((o) => `${o.specId}:${o.operationId || o.method + ' ' + o.path}`))
    ops = ops.filter((o) => opSet.has(`${o.specId}:${o.operationId || o.method + ' ' + o.path}`))
  }

  ops = ops.slice(0, limit)

  if (json) {
    console.log(
      JSON.stringify(
        ops.map((o) => ({
          spec: o.specId,
          operationId: o.operationId,
          method: o.method,
          path: o.path,
          summary: o.summary,
        })),
        null,
        2,
      ),
    )
    return
  }

  const rows = [['spec', 'operationId', 'method', 'path', 'summary']]
  for (const o of ops) rows.push([o.specId, o.operationId || '-', o.method.toUpperCase(), o.path, (o.summary || '').slice(0, 80)])
  printTable(rows)
}

function splitParams(params) {
  const out = { path: [], query: [], header: [], cookie: [], other: [] }
  for (const p of params || []) {
    const loc = p?.in
    if (loc === 'path') out.path.push(p)
    else if (loc === 'query') out.query.push(p)
    else if (loc === 'header') out.header.push(p)
    else if (loc === 'cookie') out.cookie.push(p)
    else out.other.push(p)
  }
  return out
}

function paramType(param) {
  const s = param?.schema
  if (s) return schemaTypeString(s)
  if (param?.content) {
    const media = Object.values(param.content)[0]
    if (media?.schema) return schemaTypeString(media.schema)
  }
  return 'any'
}

function printParamsBlock(title, params) {
  if (!params.length) return
  console.log(`\n${title}`)
  const rows = [['name', 'in', 'required', 'type', 'description']]
  for (const p of params) {
    rows.push([
      p.name || '-',
      p.in || '-',
      p.required ? 'yes' : 'no',
      paramType(p),
      (p.description || '').replaceAll('\n', ' ').slice(0, 80),
    ])
  }
  printTable(rows)
}

function printOperation(op, spec) {
  const baseUrl = spec.servers?.[0] || ''
  const full = baseUrl ? `${baseUrl}${op.path}` : op.path

  const id = op.operationId ? `${op.specId}:${op.operationId}` : `${op.specId}:${op.method.toUpperCase()} ${op.path}`

  console.log(id)
  console.log(`${op.method.toUpperCase()} ${full}`)

  if (op.summary) console.log(`\n${op.summary}`)
  if (op.deprecated) console.log(`\nDeprecated: yes`)

  const auth = op.securityLabel
  if (auth) console.log(`\nAuth: ${auth}`)

  if (op.tags?.length) console.log(`Tags: ${op.tags.join(', ')}`)

  if (op.description) {
    const desc = String(op.description).trim().replace(/\n{3,}/g, '\n\n')
    const short = desc.length > 800 ? `${desc.slice(0, 800)}\n...` : desc
    console.log(`\n${short}`)
  }

  const params = splitParams(op.parameters || [])
  printParamsBlock('Path params', params.path)
  printParamsBlock('Query params', params.query)
  printParamsBlock('Header params', params.header)

  if (op.requestBody?.content) {
    console.log('\nBody')
    const required = op.requestBody.required ? 'required' : 'optional'
    console.log(`required: ${required}`)

    const contentTypes = Object.keys(op.requestBody.content)
    for (const ct of contentTypes) {
      const schema = op.requestBody.content?.[ct]?.schema
      if (!schema) continue
      console.log(`\n${ct}`)
      const lines = formatSchemaPreview(schema, spec.doc, { depth: 3, maxProps: 12 })
      for (const l of lines) console.log(l)

      if (ct === 'application/json') {
        const ex = exampleFromSchema(schema, spec.doc, { depth: 3, includeOptional: false })
        if (ex && typeof ex === 'object') {
          console.log('\nexample (required fields)')
          console.log(JSON.stringify(ex, null, 2))
        }
      }
    }
  }

  if (op.responses && Object.keys(op.responses).length) {
    console.log('\nResponses')
    const codes = Object.keys(op.responses).sort((a, b) => {
      const na = Number(a)
      const nb = Number(b)
      if (Number.isFinite(na) && Number.isFinite(nb)) return na - nb
      if (a === 'default') return 1
      if (b === 'default') return -1
      return a.localeCompare(b)
    })

    for (const code of codes) {
      const resp = derefObject(op.responses[code], spec.doc)
      const desc = resp?.description ? ` - ${String(resp.description).replaceAll('\n', ' ').slice(0, 80)}` : ''
      console.log(`\n${code}${desc}`)

      const content = resp?.content || {}
      for (const [ct, media] of Object.entries(content)) {
        if (!media?.schema) continue
        console.log(`${ct}`)
        const lines = formatSchemaPreview(media.schema, spec.doc, { depth: 3, maxProps: 12 })
        for (const l of lines) console.log(l)
      }
    }
  }

  console.log('\ncurl')
  console.log(formatCurl(op, spec))
}

function replacePathParams(p) {
  return p.replaceAll(/\{([^}]+)\}/g, '<$1>')
}

function formatCurl(op, spec) {
  const baseUrl = spec.servers?.[0] || ''
  let url = baseUrl ? `${baseUrl}${replacePathParams(op.path)}` : replacePathParams(op.path)

  const requiredQuery = (op.parameters || [])
    .filter((p) => p?.in === 'query' && p?.required && p?.name)
    .map((p) => `${encodeURIComponent(p.name)}=<${p.name}>`)
  if (requiredQuery.length) url += `?${requiredQuery.join('&')}`

  const lines = []
  lines.push(`curl -X ${op.method.toUpperCase()} '${url}' \\`)

  // auth header if we can infer it
  const schemes = spec?.doc?.components?.securitySchemes || {}
  const sec = Array.isArray(op.security) ? op.security : null
  const candidates = (sec || []).filter((x) => x && typeof x === 'object')
  const preferred =
    candidates.find((req) =>
      Object.keys(req).some((name) => schemes[name]?.type === 'apiKey' && schemes[name]?.in === 'header'),
    ) || candidates[0]

  for (const name of Object.keys(preferred || {})) {
    const s = schemes[name]
    if (s?.type === 'apiKey' && s.in === 'header' && s.name) {
      lines.push(`  -H '${s.name}: $KAPSO_API_KEY' \\`)
    } else if (s?.type === 'http' && s.scheme === 'bearer') {
      lines.push(`  -H 'Authorization: Bearer $ACCESS_TOKEN' \\`)
    }
  }

  // content-type + body for JSON
  const jsonSchema = op.requestBody?.content?.['application/json']?.schema
  if (jsonSchema) {
    const ex = exampleFromSchema(jsonSchema, spec.doc, { depth: 4, includeOptional: false })
    lines.push(`  -H 'Content-Type: application/json' \\`)
    lines.push(`  -d '${JSON.stringify(ex ?? {}, null, 0)}'`)
    return lines.join('\n')
  }

  // trim trailing backslash
  lines[lines.length - 1] = lines[lines.length - 1].replace(/ \\\\$/, '')
  return lines.join('\n')
}

function printSchemaDetails(match, specs, { includeUsedBy = true } = {}) {
  const { spec, name, schema } = match
  console.log(`${spec.id}:${name}`)

  const normalized = schema?.allOf ? mergeAllOf(schema, spec.doc) : schema
  const typeStr = schemaTypeString(normalized)
  console.log(typeStr)

  if (normalized?.description) console.log(`\n${String(normalized.description).trim()}`)

  const required = normalized?.required || []
  if (required.length) console.log(`\nrequired: ${required.join(', ')}`)

  if (normalized?.properties || normalized?.items) {
    console.log('\nshape')
    const lines = formatSchemaPreview(normalized, spec.doc, { depth: 3, maxProps: 25 })
    for (const l of lines) console.log(l)
  }

  const ex = exampleFromSchema(normalized, spec.doc, { depth: 4, includeOptional: false })
  if (ex && typeof ex === 'object') {
    console.log('\nexample (required fields)')
    console.log(JSON.stringify(ex, null, 2))
  }

  if (includeUsedBy) {
    const usedBy = []
    for (const s of specs) {
      for (const op of s.operations) {
        if (op.refsUsed?.has(name)) usedBy.push(op)
      }
    }

    if (usedBy.length) {
      console.log('\nused by')
      const rows = [['spec', 'operationId', 'method', 'path']]
      for (const op of usedBy.slice(0, 30)) rows.push([op.specId, op.operationId || '-', op.method.toUpperCase(), op.path])
      printTable(rows)
      if (usedBy.length > 30) console.log(`... (${usedBy.length - 30} more)`)
    }
  }
}

function printWhere(specs, schemaQuery, { specHint, json, limit = 30 } = {}) {
  const matches = findSchema(specs, schemaQuery, { specHint })
  if (!matches.length) die(`Schema not found: ${schemaQuery}`)
  if (matches.length > 1 && !schemaQuery.includes(':')) {
    die(`Schema exists in multiple specs. Use specId:SchemaName\n${matches.map((m) => `- ${m.spec.id}:${m.name}`).join('\n')}`)
  }

  const { name } = matches[0]
  const usedBy = []
  for (const s of specs) {
    if (specHint && s.id !== specHint) continue
    for (const op of s.operations) {
      if (op.refsUsed?.has(name)) usedBy.push(op)
    }
  }

  if (json) {
    console.log(
      JSON.stringify(
        usedBy.slice(0, limit).map((o) => ({
          spec: o.specId,
          operationId: o.operationId,
          method: o.method,
          path: o.path,
          summary: o.summary,
        })),
        null,
        2,
      ),
    )
    return
  }

  if (!usedBy.length) {
    console.log('No operations reference this schema (via $ref).')
    return
  }

  const rows = [['spec', 'operationId', 'method', 'path', 'summary']]
  for (const o of usedBy.slice(0, limit)) rows.push([o.specId, o.operationId || '-', o.method.toUpperCase(), o.path, (o.summary || '').slice(0, 80)])
  printTable(rows)
  if (usedBy.length > limit) console.log(`... (${usedBy.length - limit} more)`)
}

async function main() {
  const { opts, command, rest } = parseArgs(process.argv.slice(2))
  if (!command) printHelp(1)

  let sources = []
  let sourceMode = 'explicit'

  if (opts.files.length) {
    sources = opts.files
    sourceMode = 'explicit'
  } else if (opts.all) {
    const apiDir = findLocalApiDir()
    sources = apiDir ? walk(apiDir, { filePattern: /^openapi-.*\.ya?ml$/ }) : []
    sourceMode = 'explicit'
  } else {
    sources = deducePublishedOpenApiUrls(DEFAULT_PUBLISHED_WHATSAPP_OPENAPI)
    sourceMode = 'default_remote'
  }

  const specs = await loadSpecsAsync({ sources, sourceMode, specFilter: opts.spec })

  if (command === 'specs') return printSpecs(specs, { json: opts.json })
  if (command === 'tags') return printTags(specs, { specHint: opts.spec })
  if (command === 'ops') return printOps(specs, { specHint: opts.spec, tag: opts.tag, q: opts.q, json: opts.json, limit: opts.limit })
  if (command === 'search') {
    const q = rest.join(' ').trim()
    if (!q) die('Usage: search <query>')
    const res = search(specs, q, { specHint: opts.spec, limit: opts.limit })
    if (opts.json) {
      return console.log(
        JSON.stringify(
          {
            ops: res.ops.map((o) => ({
              spec: o.specId,
              operationId: o.operationId,
              method: o.method,
              path: o.path,
              summary: o.summary,
            })),
            schemas: res.schemas,
          },
          null,
          2,
        ),
      )
    }

    if (!res.ops.length && !res.schemas.length) {
      console.log('No matches.')
      return
    }

    if (res.ops.length) {
      console.log('ops')
      const rows = [['spec', 'operationId', 'method', 'path', 'summary']]
      for (const o of res.ops) rows.push([o.specId, o.operationId || '-', o.method.toUpperCase(), o.path, (o.summary || '').slice(0, 80)])
      printTable(rows)
    }
    if (res.schemas.length) {
      console.log('\nschemas')
      const rows = [['spec', 'name']]
      for (const s of res.schemas) rows.push([s.specId, s.name])
      printTable(rows)
    }
    return
  }
  if (command === 'op') {
    const q = rest.join(' ').trim()
    if (!q) die('Usage: op <operationId | specId:operationId | "METHOD /path">')
    const matches = findOperation(specs, q, { specHint: opts.spec })
    if (!matches.length) {
      const res = search(specs, q, { specHint: opts.spec, limit: 10 })
      if (res.ops.length) {
        console.log(`Operation not found: ${q}\n`)
        console.log('closest ops')
        const rows = [['spec', 'operationId', 'method', 'path', 'summary']]
        for (const o of res.ops) rows.push([o.specId, o.operationId || '-', o.method.toUpperCase(), o.path, (o.summary || '').slice(0, 80)])
        printTable(rows)
        process.exit(1)
      }
      die(`Operation not found: ${q}`)
    }
    if (matches.length > 1 && !q.includes(':') && !q.match(/^(get|post|put|patch|delete|options|head)\\s+/i)) {
      die(`OperationId exists in multiple specs. Use specId:operationId\n${matches.map((m) => `- ${m.specId}:${m.operationId}`).join('\n')}`)
    }
    const op = matches[0]
    const spec = specs.find((s) => s.id === op.specId)
    if (!spec) die(`Internal error: missing spec ${op.specId}`)
    printOperation(op, spec)
    return
  }
  if (command === 'schema') {
    const q = rest.join(' ').trim()
    if (!q) die('Usage: schema <SchemaName | specId:SchemaName>')
    const matches = findSchema(specs, q, { specHint: opts.spec })
    if (!matches.length) {
      const res = search(specs, q, { specHint: opts.spec, limit: 10 })
      if (res.schemas.length) {
        console.log(`Schema not found: ${q}\n`)
        console.log('closest schemas')
        const rows = [['spec', 'name']]
        for (const s of res.schemas) rows.push([s.specId, s.name])
        printTable(rows)
        process.exit(1)
      }
      die(`Schema not found: ${q}`)
    }
    if (matches.length > 1 && !q.includes(':')) {
      die(`Schema exists in multiple specs. Use specId:SchemaName\n${matches.map((m) => `- ${m.spec.id}:${m.name}`).join('\n')}`)
    }
    printSchemaDetails(matches[0], specs, { includeUsedBy: true })
    return
  }
  if (command === 'where') {
    const q = rest.join(' ').trim()
    if (!q) die('Usage: where <SchemaName | specId:SchemaName>')
    return printWhere(specs, q, { specHint: opts.spec, json: opts.json, limit: opts.limit })
  }

  die(`Unknown command: ${command}`)
}

main().catch((e) => die(e?.stack || e?.message || String(e)))
```

## File: `skills/automate-whatsapp/scripts/query-rows.js`
```javascript
import { kapsoConfigFromEnv, kapsoRequest } from './lib/databases/kapso-api.js';
import { hasHelpFlag, parseFlags, requireFlag, parseJsonObjectOptional, parseNumber } from './lib/databases/args.js';

function ok(data) {
  return { ok: true, data };
}

function err(message, details) {
  return { ok: false, error: { message, details } };
}

function buildQuery(flags) {
  const params = new URLSearchParams();
  const filters = parseJsonObjectOptional(flags.filters, 'filters');
  if (filters) {
    Object.entries(filters).forEach(([key, value]) => {
      params.set(key, String(value));
    });
  }
  if (typeof flags.select === 'string' && flags.select.length > 0) {
    params.set('select', flags.select);
  }
  if (typeof flags.order === 'string' && flags.order.length > 0) {
    params.set('order', flags.order);
  }
  const limit = parseNumber(flags.limit, 'limit');
  if (limit !== undefined) {
    params.set('limit', String(limit));
  }
  const offset = parseNumber(flags.offset, 'offset');
  if (offset !== undefined) {
    params.set('offset', String(offset));
  }
  const query = params.toString();
  return query ? `?${query}` : '';
}

async function main() {
  const argv = process.argv.slice(2);
  if (hasHelpFlag(argv)) {
    console.log(
      JSON.stringify(
        {
          ok: true,
          usage:
            'node scripts/query-rows.js --table <name> [--filters <json>] [--select <cols>] [--order <col.asc|desc>] [--limit <n>] [--offset <n>]',
          env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
        },
        null,
        2
      )
    );
    return 0;
  }

  try {
    const flags = parseFlags(argv);
    const table = requireFlag(flags, 'table');
    const query = buildQuery(flags);
    const config = kapsoConfigFromEnv();
    const data = await kapsoRequest(config, `/platform/v1/db/${encodeURIComponent(table)}${query}`);
    console.log(JSON.stringify(ok(data), null, 2));
    return 0;
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    console.error(JSON.stringify(err('Command failed', { message }), null, 2));
    return 1;
  }
}

main().then((code) => process.exit(code));
```

## File: `skills/automate-whatsapp/scripts/reload-props.js`
```javascript
#!/usr/bin/env node
import { loadConfig, requestJson } from './lib/workflows/kapso-api.js';
import { ok, err, printJson } from './lib/workflows/result.js';
import { parseArgs, getFlag, getBooleanFlag } from './lib/workflows/args.js';

function usage() {
  return ok({
    usage: 'node scripts/reload-props.js --action-id <id> --account-id <id> [--configured-props <json>] [--dynamic-props-id <id>]',
    notes: [
      'Use accounts[].pipedream_account_id for --account-id.',
      'If you pass an internal account UUID, the script will try to resolve it.'
    ],
    env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
  });
}

function parseJson(value, label) {
  if (!value) return undefined;
  try {
    return JSON.parse(value);
  } catch (error) {
    throw new Error(`Invalid JSON for ${label}: ${String(error?.message || error)}`);
  }
}

function normalizeAccounts(payload) {
  if (Array.isArray(payload?.accounts)) return payload.accounts;
  if (Array.isArray(payload?.accounts?.accounts)) return payload.accounts.accounts;
  if (Array.isArray(payload)) return payload;
  return [];
}

async function resolveAccountId(config, accountId) {
  if (accountId.startsWith('apn_')) return accountId;

  const response = await requestJson(config, {
    method: 'GET',
    path: '/platform/v1/integrations/accounts'
  });

  if (!response.ok) {
    throw new Error('Unable to resolve account id. Use list-accounts and pass pipedream_account_id.');
  }

  const accounts = normalizeAccounts(response.data);
  const match = accounts.find((account) => account.id === accountId);
  if (match?.pipedream_account_id) return match.pipedream_account_id;

  throw new Error('account-id must be pipedream_account_id (use list-accounts output).');
}

async function main() {
  const parsed = parseArgs(process.argv.slice(2));
  if (getBooleanFlag(parsed.flags, 'help') || getBooleanFlag(parsed.flags, 'h')) {
    printJson(usage());
    return 0;
  }

  const actionId = getFlag(parsed.flags, 'action-id');
  const accountId = getFlag(parsed.flags, 'account-id');
  if (!actionId || !accountId) {
    printJson(err('action-id and account-id are required'));
    return 2;
  }

  let configuredProps = {};
  try {
    const provided = parseJson(getFlag(parsed.flags, 'configured-props'), 'configured-props');
    configuredProps = provided || {};
  } catch (error) {
    printJson(err('Failed to parse configured-props', { message: error.message }));
    return 2;
  }

  const config = loadConfig();
  let resolvedAccountId = accountId;

  try {
    resolvedAccountId = await resolveAccountId(config, accountId);
  } catch (error) {
    printJson(err('Failed to resolve account-id', { message: error.message }));
    return 2;
  }

  if (!Object.keys(configuredProps).length) {
    configuredProps = { account_id: resolvedAccountId };
  }

  const response = await requestJson(config, {
    method: 'POST',
    path: `/platform/v1/integrations/actions/${actionId}/reload_props`,
    body: {
      configured_props: configuredProps,
      dynamic_props_id: getFlag(parsed.flags, 'dynamic-props-id')
    }
  });

  if (!response.ok) {
    printJson(err('Failed to reload props', response.raw, false, response.status));
    return 2;
  }

  printJson(ok({ result: response.data }));
  return 0;
}

main().catch((error) => {
  printJson(err('Unhandled error', { message: String(error?.message || error) }));
  process.exit(1);
});
```

## File: `skills/automate-whatsapp/scripts/resume-execution.js`
```javascript
#!/usr/bin/env node
import { loadConfig, requestJson } from './lib/workflows/kapso-api.js';
import { ok, err, printJson } from './lib/workflows/result.js';
import { parseArgs, getFlag, getBooleanFlag } from './lib/workflows/args.js';

function usage() {
  return ok({
    usage: 'node scripts/resume-execution.js <execution-id> --message <json> [--variables <json>]',
    env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY'],
    examples: [
      'node scripts/resume-execution.js exec_123 --message \'{"data":{"text":"hi"}}\''
    ]
  });
}

function parseJson(value, label) {
  if (!value) return undefined;
  try {
    return JSON.parse(value);
  } catch (error) {
    throw new Error(`Invalid JSON for ${label}: ${String(error?.message || error)}`);
  }
}

async function main() {
  const parsed = parseArgs(process.argv.slice(2));
  if (getBooleanFlag(parsed.flags, 'help') || getBooleanFlag(parsed.flags, 'h')) {
    printJson(usage());
    return 0;
  }

  const executionId = parsed.args[0] || getFlag(parsed.flags, 'execution-id');
  if (!executionId) {
    printJson(err('execution_id is required'));
    return 2;
  }

  let message;
  let variables;
  try {
    message = parseJson(getFlag(parsed.flags, 'message'), 'message');
    variables = parseJson(getFlag(parsed.flags, 'variables'), 'variables');
  } catch (error) {
    printJson(err('Failed to parse JSON', { message: error.message }));
    return 2;
  }

  if (!message || typeof message !== 'object') {
    printJson(err('message is required and must be a JSON object'));
    return 2;
  }

  const body = { message };
  if (variables) body.variables = variables;

  const config = loadConfig();
  const response = await requestJson(config, {
    method: 'POST',
    path: `/platform/v1/workflow_executions/${executionId}/resume`,
    body
  });

  if (!response.ok) {
    printJson(err('Failed to resume execution', response.raw, false, response.status));
    return 2;
  }

  printJson(ok({ execution: response.data }));
  return 0;
}

main().catch((error) => {
  printJson(err('Unhandled error', { message: String(error?.message || error) }));
  process.exit(1);
});
```

## File: `skills/automate-whatsapp/scripts/search-actions.js`
```javascript
#!/usr/bin/env node
import { loadConfig, requestJson } from './lib/workflows/kapso-api.js';
import { ok, err, printJson } from './lib/workflows/result.js';
import { parseArgs, getFlag, getBooleanFlag } from './lib/workflows/args.js';

function usage() {
  return ok({
    usage: 'node scripts/search-actions.js --query <text> [--app-slug <slug>]',
    notes: [
      'Prefer one-word queries (ex: "calendar", "slack", "hubspot").',
      'Use --app-slug to narrow results to a single app.',
      'action_id equals the action key returned in results.'
    ],
    env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
  });
}

async function main() {
  const parsed = parseArgs(process.argv.slice(2));
  if (getBooleanFlag(parsed.flags, 'help') || getBooleanFlag(parsed.flags, 'h')) {
    printJson(usage());
    return 0;
  }

  const query = getFlag(parsed.flags, 'query');
  if (!query) {
    printJson(err('query is required'));
    return 2;
  }

  const config = loadConfig();
  const response = await requestJson(config, {
    method: 'GET',
    path: '/platform/v1/integrations/actions',
    query: {
      query,
      app_slug: getFlag(parsed.flags, 'app-slug')
    }
  });

  if (!response.ok) {
    printJson(err('Failed to search actions', response.raw, false, response.status));
    return 2;
  }

  const raw = response.data;
  const actions = Array.isArray(raw?.actions) ? raw.actions : (Array.isArray(raw) ? raw : []);
  const mapped = actions.map((action) => ({
    ...action,
    action_id: action.action_id || action.key
  }));
  const payload = Array.isArray(raw) ? mapped : { ...raw, actions: mapped };

  printJson(ok({
    actions: payload,
    note: 'Use action_id (same as key) with get-action-schema/create-integration.'
  }));
  return 0;
}

main().catch((error) => {
  printJson(err('Unhandled error', { message: String(error?.message || error) }));
  process.exit(1);
});
```

## File: `skills/automate-whatsapp/scripts/update-execution-status.js`
```javascript
#!/usr/bin/env node
import { loadConfig, requestJson } from './lib/workflows/kapso-api.js';
import { ok, err, printJson } from './lib/workflows/result.js';
import { parseArgs, getFlag, getBooleanFlag } from './lib/workflows/args.js';

function usage() {
  return ok({
    usage: 'node scripts/update-execution-status.js <execution-id> --status <ended|handoff|waiting>',
    env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
  });
}

async function main() {
  const parsed = parseArgs(process.argv.slice(2));
  if (getBooleanFlag(parsed.flags, 'help') || getBooleanFlag(parsed.flags, 'h')) {
    printJson(usage());
    return 0;
  }

  const executionId = parsed.args[0] || getFlag(parsed.flags, 'execution-id');
  if (!executionId) {
    printJson(err('execution_id is required'));
    return 2;
  }

  const status = getFlag(parsed.flags, 'status');
  if (!status) {
    printJson(err('status is required'));
    return 2;
  }

  const config = loadConfig();
  const response = await requestJson(config, {
    method: 'PATCH',
    path: `/platform/v1/workflow_executions/${executionId}`,
    body: { workflow_execution: { status } }
  });

  if (!response.ok) {
    printJson(err('Failed to update execution status', response.raw, false, response.status));
    return 2;
  }

  printJson(ok({ execution: response.data }));
  return 0;
}

main().catch((error) => {
  printJson(err('Unhandled error', { message: String(error?.message || error) }));
  process.exit(1);
});
```

## File: `skills/automate-whatsapp/scripts/update-function.js`
```javascript
import { readFileSync } from 'node:fs';
import { kapsoConfigFromEnv, kapsoRequest } from './lib/functions/kapso-api.js';
import { hasHelpFlag, parseFlags, requireFlag } from './lib/functions/args.js';

function ok(data) {
  return { ok: true, data };
}

function err(message, details) {
  return { ok: false, error: { message, details } };
}

function resolveCode(flags) {
  if (typeof flags.code === 'string' && flags.code.length > 0) {
    return flags.code;
  }
  if (typeof flags['code-file'] === 'string' && flags['code-file'].length > 0) {
    return readFileSync(flags['code-file'], 'utf8');
  }
  throw new Error('Provide --code or --code-file');
}

async function main() {
  const argv = process.argv.slice(2);
  if (hasHelpFlag(argv)) {
    console.log(
      JSON.stringify(
        {
          ok: true,
          usage:
            'node scripts/update-function.js --function-id <id> --name <name> (--code <js> | --code-file <path>) [--description <text>]',
          env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
        },
        null,
        2
      )
    );
    return 0;
  }

  try {
    const flags = parseFlags(argv);
    const functionId = requireFlag(flags, 'function-id');
    const name = requireFlag(flags, 'name');
    const code = resolveCode(flags);
    const payload = { name, code };
    if (typeof flags.description === 'string' && flags.description.length > 0) {
      payload.description = flags.description;
    }
    const config = kapsoConfigFromEnv();
    const data = await kapsoRequest(config, `/platform/v1/functions/${encodeURIComponent(functionId)}`, {
      method: 'PATCH',
      body: JSON.stringify({ function: payload })
    });

    console.log(JSON.stringify(ok(data), null, 2));
    return 0;
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    console.error(JSON.stringify(err('Command failed', { message }), null, 2));
    return 1;
  }
}

main().then((code) => process.exit(code));
```

## File: `skills/automate-whatsapp/scripts/update-graph.js`
```javascript
#!/usr/bin/env node
import { createHash } from 'crypto';
import { readFileSync } from 'fs';
import { loadConfig, requestJson } from './lib/workflows/kapso-api.js';
import { ok, err, printJson } from './lib/workflows/result.js';
import { parseArgs, getFlag, getBooleanFlag, getNumberFlag } from './lib/workflows/args.js';

function sha256(text) {
  return createHash('sha256').update(text).digest('hex');
}

function readFileText(path) {
  return readFileSync(path, 'utf8');
}

function normalizeDefinition(input) {
  if (!input || typeof input !== 'object') return null;
  const record = input;

  if (record.ok === true && record.data && typeof record.data === 'object') {
    return normalizeDefinition(record.data);
  }

  if (record.definition && typeof record.definition === 'object') {
    return record.definition;
  }

  if (record.flow && typeof record.flow === 'object') {
    const flow = record.flow;
    if (flow.definition && typeof flow.definition === 'object') {
      return flow.definition;
    }
  }

  if (record.workflow && typeof record.workflow === 'object') {
    const workflow = record.workflow;
    if (workflow.definition && typeof workflow.definition === 'object') {
      return workflow.definition;
    }
  }

  if (record.nodes && record.edges) {
    return record;
  }

  return null;
}

function parseDefinitionInput(raw) {
  try {
    const parsed = JSON.parse(raw);
    return normalizeDefinition(parsed);
  } catch {
    return null;
  }
}

function usage() {
  return ok({
    usage: 'node scripts/update-graph.js <workflow-id> --expected-lock-version <n> --definition-file <path>|--definition-json <json>',
    env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
  });
}

async function main() {
  const parsed = parseArgs(process.argv.slice(2));
  if (getBooleanFlag(parsed.flags, 'help') || getBooleanFlag(parsed.flags, 'h')) {
    printJson(usage());
    return 0;
  }

  const workflowId = parsed.args[0] || getFlag(parsed.flags, 'workflow-id');
  if (!workflowId) {
    printJson(err('workflow_id is required'));
    return 2;
  }

  const expectedLockVersion = getNumberFlag(parsed.flags, 'expected-lock-version')
    ?? getNumberFlag(parsed.flags, 'lock-version');
  if (expectedLockVersion === undefined) {
    printJson(err('expected-lock-version is required'));
    return 2;
  }

  const definitionFile = getFlag(parsed.flags, 'definition-file');
  const definitionJson = getFlag(parsed.flags, 'definition-json');
  if (!definitionFile && !definitionJson) {
    printJson(err('definition-file or definition-json is required'));
    return 2;
  }

  const rawDefinition = definitionFile ? readFileText(definitionFile) : definitionJson || '';
  const definition = parseDefinitionInput(rawDefinition);
  if (!definition) {
    const source = definitionFile ? 'definition-file' : 'definition-json';
    printJson(err(`Unable to parse workflow definition from ${source}`));
    return 2;
  }

  const config = loadConfig();
  const current = await requestJson(config, {
    method: 'GET',
    path: `/platform/v1/workflows/${workflowId}`
  });

  if (!current.ok) {
    printJson(err('Failed to fetch workflow metadata for lock check', current.raw, false, current.status));
    return 2;
  }

  const currentLock = current.data.lock_version;
  if (currentLock !== expectedLockVersion) {
    printJson(err('Conflict: workflow was modified. Refetch and retry.', {
      expected_lock_version: expectedLockVersion,
      current_lock_version: currentLock
    }));
    return 2;
  }

  const update = await requestJson(config, {
    method: 'PATCH',
    path: `/platform/v1/workflows/${workflowId}`,
    body: {
      workflow: {
        definition
      }
    }
  });

  if (!update.ok) {
    printJson(err('Failed to update workflow definition', update.raw, false, update.status));
    return 2;
  }

  const pretty = JSON.stringify(definition, null, 2);

  printJson(ok({
    workflow: {
      id: update.data.id,
      name: update.data.name,
      status: update.data.status,
      lock_version: update.data.lock_version,
      updated_at: update.data.updated_at
    },
    workflow_graph_sha256: sha256(pretty)
  }));

  return 0;
}

main().catch((error) => {
  printJson(err('Unhandled error', { message: String(error?.message || error) }));
  process.exit(1);
});
```

## File: `skills/automate-whatsapp/scripts/update-integration.js`
```javascript
#!/usr/bin/env node
import { loadConfig, requestJson } from './lib/workflows/kapso-api.js';
import { ok, err, printJson } from './lib/workflows/result.js';
import { parseArgs, getFlag, getBooleanFlag } from './lib/workflows/args.js';

function usage() {
  return ok({
    usage: 'node scripts/update-integration.js --integration-id <id> [--configured-props <json>] [--name <text>] [--variable-definitions <json>] [--dynamic-props-id <id>]',
    notes: [
      'Use --variable-definitions to update required tool input fields.'
    ],
    env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
  });
}

function parseJson(value, label) {
  if (!value) return undefined;
  try {
    return JSON.parse(value);
  } catch (error) {
    throw new Error(`Invalid JSON for ${label}: ${String(error?.message || error)}`);
  }
}

async function main() {
  const parsed = parseArgs(process.argv.slice(2));
  if (getBooleanFlag(parsed.flags, 'help') || getBooleanFlag(parsed.flags, 'h')) {
    printJson(usage());
    return 0;
  }

  const integrationId = getFlag(parsed.flags, 'integration-id');
  if (!integrationId) {
    printJson(err('integration-id is required'));
    return 2;
  }

  let configuredProps;
  let variableDefinitions;

  try {
    configuredProps = parseJson(getFlag(parsed.flags, 'configured-props'), 'configured-props');
    variableDefinitions = parseJson(getFlag(parsed.flags, 'variable-definitions'), 'variable-definitions');
  } catch (error) {
    printJson(err('Failed to parse JSON', { message: error.message }));
    return 2;
  }

  const payload = {};
  const name = getFlag(parsed.flags, 'name');
  const dynamicPropsId = getFlag(parsed.flags, 'dynamic-props-id');

  if (name) payload.name = name;
  if (dynamicPropsId) payload.dynamic_props_id = dynamicPropsId;
  if (configuredProps) payload.configured_props = configuredProps;
  if (variableDefinitions) payload.variable_definitions = variableDefinitions;

  if (!Object.keys(payload).length) {
    printJson(err('No updates provided'));
    return 2;
  }

  const config = loadConfig();
  const response = await requestJson(config, {
    method: 'PATCH',
    path: `/platform/v1/integrations/${integrationId}`,
    body: payload
  });

  if (!response.ok) {
    printJson(err('Failed to update integration', response.raw, false, response.status));
    return 2;
  }

  printJson(ok({ integration: response.data }));
  return 0;
}

main().catch((error) => {
  printJson(err('Unhandled error', { message: String(error?.message || error) }));
  process.exit(1);
});
```

## File: `skills/automate-whatsapp/scripts/update-row.js`
```javascript
import { kapsoConfigFromEnv, kapsoRequest } from './lib/databases/kapso-api.js';
import { hasHelpFlag, parseFlags, requireFlag, parseJsonObject } from './lib/databases/args.js';
import { resolveFilters, filtersToQuery } from './lib/databases/filters.js';

function ok(data) {
  return { ok: true, data };
}

function err(message, details) {
  return { ok: false, error: { message, details } };
}

async function main() {
  const argv = process.argv.slice(2);
  if (hasHelpFlag(argv)) {
    console.log(
      JSON.stringify(
        {
          ok: true,
          usage:
            'node scripts/update-row.js --table <name> --data <json> (--id <row-id> | --filters <json>)',
          env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
        },
        null,
        2
      )
    );
    return 0;
  }

  try {
    const flags = parseFlags(argv);
    const table = requireFlag(flags, 'table');
    const dataPayload = parseJsonObject(flags.data, 'data');
    const filters = resolveFilters(flags);
    const query = filtersToQuery(filters);
    const config = kapsoConfigFromEnv();
    const data = await kapsoRequest(config, `/platform/v1/db/${encodeURIComponent(table)}${query}`, {
      method: 'PATCH',
      body: JSON.stringify(dataPayload)
    });
    console.log(JSON.stringify(ok(data), null, 2));
    return 0;
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    console.error(JSON.stringify(err('Command failed', { message }), null, 2));
    return 1;
  }
}

main().then((code) => process.exit(code));
```

## File: `skills/automate-whatsapp/scripts/update-trigger.js`
```javascript
#!/usr/bin/env node
import { loadConfig, requestJson } from './lib/workflows/kapso-api.js';
import { ok, err, printJson } from './lib/workflows/result.js';
import { parseArgs, getFlag, getBooleanFlag } from './lib/workflows/args.js';

function usage() {
  return ok({
    usage: 'node scripts/update-trigger.js --trigger-id <id> --active true|false',
    env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
  });
}

function parseBoolean(value) {
  if (value === undefined) return undefined;
  if (value === true) return true;
  const lowered = String(value).toLowerCase();
  if (lowered === 'true') return true;
  if (lowered === 'false') return false;
  return undefined;
}

async function main() {
  const parsed = parseArgs(process.argv.slice(2));
  if (getBooleanFlag(parsed.flags, 'help') || getBooleanFlag(parsed.flags, 'h')) {
    printJson(usage());
    return 0;
  }

  const triggerId = getFlag(parsed.flags, 'trigger-id');
  if (!triggerId) {
    printJson(err('trigger-id is required'));
    return 2;
  }

  const active = parseBoolean(getFlag(parsed.flags, 'active'));
  if (active === undefined) {
    printJson(err('active is required (true or false)'));
    return 2;
  }

  const config = loadConfig();
  const response = await requestJson(config, {
    method: 'PATCH',
    path: `/platform/v1/triggers/${triggerId}`,
    body: { trigger: { active } }
  });

  if (!response.ok) {
    printJson(err('Failed to update trigger', response.raw, false, response.status));
    return 2;
  }

  printJson(ok({ trigger: response.data }));
  return 0;
}

main().catch((error) => {
  printJson(err('Unhandled error', { message: String(error?.message || error) }));
  process.exit(1);
});
```

## File: `skills/automate-whatsapp/scripts/update-workflow-settings.js`
```javascript
#!/usr/bin/env node
import { loadConfig, requestJson } from './lib/workflows/kapso-api.js';
import { ok, err, printJson } from './lib/workflows/result.js';
import { parseArgs, getFlag, getBooleanFlag, getNumberFlag } from './lib/workflows/args.js';

function usage() {
  return ok({
    usage: 'node scripts/update-workflow-settings.js <workflow-id> --lock-version <n> [--name <name>] [--description <text>] [--status <draft|active|archived>] [--message-debounce-seconds <n>] [--inbound-message-read-mode <disabled|read_only|read_with_typing>]',
    env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
  });
}

async function main() {
  const parsed = parseArgs(process.argv.slice(2));
  if (getBooleanFlag(parsed.flags, 'help') || getBooleanFlag(parsed.flags, 'h')) {
    printJson(usage());
    return 0;
  }

  const workflowId = parsed.args[0] || getFlag(parsed.flags, 'workflow-id');
  if (!workflowId) {
    printJson(err('workflow_id is required'));
    return 2;
  }

  const lockVersion = getNumberFlag(parsed.flags, 'lock-version');
  if (lockVersion === undefined) {
    printJson(err('lock-version is required'));
    return 2;
  }

  const payload = {
    workflow: {
      lock_version: lockVersion
    }
  };

  const name = getFlag(parsed.flags, 'name');
  const description = getFlag(parsed.flags, 'description');
  const status = getFlag(parsed.flags, 'status');
  const messageDebounce = getNumberFlag(parsed.flags, 'message-debounce-seconds');
  const inboundMessageReadMode = getFlag(parsed.flags, 'inbound-message-read-mode');

  if (name) payload.workflow.name = name;
  if (description) payload.workflow.description = description;
  if (status) payload.workflow.status = status;
  if (messageDebounce !== undefined) payload.workflow.message_debounce_seconds = messageDebounce;
  if (inboundMessageReadMode) payload.workflow.inbound_message_read_mode = inboundMessageReadMode;

  const config = loadConfig();
  const response = await requestJson(config, {
    method: 'PATCH',
    path: `/platform/v1/workflows/${workflowId}`,
    body: payload
  });

  if (!response.ok) {
    printJson(err('Failed to update workflow', response.raw, false, response.status));
    return 2;
  }

  printJson(ok({ workflow: response.data }));
  return 0;
}

main().catch((error) => {
  printJson(err('Unhandled error', { message: String(error?.message || error) }));
  process.exit(1);
});
```

## File: `skills/automate-whatsapp/scripts/upsert-row.js`
```javascript
import { kapsoConfigFromEnv, kapsoRequest } from './lib/databases/kapso-api.js';
import { hasHelpFlag, parseFlags, requireFlag, parseJsonObject } from './lib/databases/args.js';
import { resolveFilters, filtersToQuery } from './lib/databases/filters.js';

function ok(data) {
  return { ok: true, data };
}

function err(message, details) {
  return { ok: false, error: { message, details } };
}

async function main() {
  const argv = process.argv.slice(2);
  if (hasHelpFlag(argv)) {
    console.log(
      JSON.stringify(
        {
          ok: true,
          usage:
            'node scripts/upsert-row.js --table <name> --data <json> [--upsert-key <column>] [--filters <json> | --id <row-id>]',
          env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
        },
        null,
        2
      )
    );
    return 0;
  }

  try {
    const flags = parseFlags(argv);
    const table = requireFlag(flags, 'table');
    const dataPayload = parseJsonObject(flags.data, 'data');

    let filters;
    if (typeof flags['upsert-key'] === 'string' && flags['upsert-key'].length > 0) {
      const key = flags['upsert-key'];
      const value = dataPayload[key];
      if (value === undefined) {
        throw new Error(`--data must include ${key} when using --upsert-key`);
      }
      filters = { [key]: `eq.${String(value)}` };
    } else {
      filters = resolveFilters(flags);
    }

    const query = filtersToQuery(filters);
    const config = kapsoConfigFromEnv();
    const data = await kapsoRequest(config, `/platform/v1/db/${encodeURIComponent(table)}${query}`, {
      method: 'PUT',
      body: JSON.stringify(dataPayload)
    });

    console.log(JSON.stringify(ok(data), null, 2));
    return 0;
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    console.error(JSON.stringify(err('Command failed', { message }), null, 2));
    return 1;
  }
}

main().then((code) => process.exit(code));
```

## File: `skills/automate-whatsapp/scripts/validate-graph.js`
```javascript
#!/usr/bin/env node
import { readFileSync } from 'fs';
import { loadConfig, requestJson } from './lib/workflows/kapso-api.js';
import { ok, err, printJson } from './lib/workflows/result.js';
import { parseArgs, getFlag, getBooleanFlag } from './lib/workflows/args.js';

const SUPPORTED_NODE_TYPES = new Set([
  'start',
  'send_text',
  'send_template',
  'set_variable',
  'send_interactive',
  'wait_for_response',
  'decide',
  'call',
  'webhook',
  'pipedream',
  'function',
  'agent',
  'handoff'
]);

function readFileText(path) {
  return readFileSync(path, 'utf8');
}

function normalizeDefinition(input) {
  if (!input || typeof input !== 'object') return null;
  const record = input;

  if (record.ok === true && record.data && typeof record.data === 'object') {
    return normalizeDefinition(record.data);
  }

  if (record.definition && typeof record.definition === 'object') {
    return record.definition;
  }

  if (record.flow && typeof record.flow === 'object') {
    const flow = record.flow;
    if (flow.definition && typeof flow.definition === 'object') {
      return flow.definition;
    }
  }

  if (record.workflow && typeof record.workflow === 'object') {
    const workflow = record.workflow;
    if (workflow.definition && typeof workflow.definition === 'object') {
      return workflow.definition;
    }
  }

  if (record.nodes && record.edges) {
    return record;
  }

  return null;
}

function parseDefinitionInput(raw) {
  try {
    const parsed = JSON.parse(raw);
    return normalizeDefinition(parsed);
  } catch {
    return null;
  }
}

function validateDefinition(definition) {
  const errors = [];
  const warnings = [];

  const nodes = Array.isArray(definition.nodes) ? definition.nodes : null;
  const edges = Array.isArray(definition.edges) ? definition.edges : null;

  if (!nodes) {
    errors.push('definition.nodes must be an array');
  }
  if (!edges) {
    errors.push('definition.edges must be an array');
  }

  if (!nodes || !edges) {
    return { errors, warnings, stats: { nodes: 0, edges: 0, decideNodes: 0 } };
  }

  const nodeIds = new Set();
  const nodeTypes = {};
  const outgoingEdges = {};

  nodes.forEach((node, index) => {
    if (!node || typeof node !== 'object') {
      errors.push(`node[${index}] must be an object`);
      return;
    }

    const nodeId = node.id;
    if (typeof nodeId !== 'string' || nodeId.trim() === '') {
      errors.push(`node[${index}].id must be a non-empty string`);
      return;
    }

    if (nodeIds.has(nodeId)) {
      errors.push(`duplicate node id: ${nodeId}`);
      return;
    }

    nodeIds.add(nodeId);

    const data = node.data || {};
    const nodeType = data.node_type;
    if (!nodeType) {
      errors.push(`node ${nodeId} is missing data.node_type`);
    } else {
      nodeTypes[nodeId] = nodeType;
      if (!SUPPORTED_NODE_TYPES.has(nodeType)) {
        warnings.push(`node ${nodeId} has unknown node_type: ${nodeType}`);
      }
    }
  });

  const startNodes = [...nodeIds].filter((id) => id === 'start');
  if (startNodes.length !== 1) {
    errors.push('graph must contain exactly one start node with id "start"');
  } else if (nodeTypes.start && nodeTypes.start !== 'start') {
    errors.push('start node must have data.node_type = "start"');
  }

  edges.forEach((edge, index) => {
    if (!edge || typeof edge !== 'object') {
      errors.push(`edge[${index}] must be an object`);
      return;
    }

    const source = edge.source;
    const target = edge.target;
    const label = edge.label;

    if (typeof source !== 'string' || !nodeIds.has(source)) {
      errors.push(`edge[${index}] has invalid source: ${String(source)}`);
    }
    if (typeof target !== 'string' || !nodeIds.has(target)) {
      errors.push(`edge[${index}] has invalid target: ${String(target)}`);
    }
    if (typeof label !== 'string' || label.trim() === '') {
      errors.push(`edge[${index}] must have a non-empty label`);
    }

    if (typeof source === 'string') {
      outgoingEdges[source] = outgoingEdges[source] || [];
      if (typeof label === 'string') {
        outgoingEdges[source].push(label);
      }
    }
  });

  let decideNodes = 0;
  nodes.forEach((node) => {
    if (!node || typeof node !== 'object') return;
    const nodeId = node.id;
    const nodeType = nodeTypes[nodeId];
    const outgoing = outgoingEdges[nodeId] || [];

    if (nodeType === 'decide') {
      decideNodes += 1;
      const config = (node.data || {}).config || {};
      const conditions = config.conditions;
      if (!Array.isArray(conditions) || conditions.length === 0) {
        errors.push(`decide node ${nodeId} must have config.conditions[]`);
        return;
      }

      const conditionLabels = conditions
        .map((condition) => condition.label)
        .filter((label) => typeof label === 'string' && label.trim() !== '');

      const uniqueLabels = new Set(conditionLabels);
      if (uniqueLabels.size !== conditionLabels.length) {
        errors.push(`decide node ${nodeId} has duplicate condition labels`);
      }

      conditionLabels.forEach((label) => {
        if (!outgoing.includes(label)) {
          errors.push(`decide node ${nodeId} missing outgoing edge for label "${label}"`);
        }
      });

      outgoing.forEach((label) => {
        if (!uniqueLabels.has(label)) {
          warnings.push(`decide node ${nodeId} has edge label "${label}" not in conditions`);
        }
      });

      return;
    }

    if (outgoing.length > 1) {
      errors.push(`node ${nodeId} has ${outgoing.length} outgoing edges; only decide nodes can branch`);
    }
    if (outgoing.length === 1 && outgoing[0] !== 'next') {
      errors.push(`node ${nodeId} outgoing edge label must be "next"`);
    }
  });

  return {
    errors,
    warnings,
    stats: {
      nodes: nodes.length,
      edges: edges.length,
      decideNodes
    }
  };
}

function usage() {
  return ok({
    usage: 'node scripts/validate-graph.js --workflow-id <id> | --definition-file <path> | --definition-json <json>',
    env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
  });
}

async function main() {
  const parsed = parseArgs(process.argv.slice(2));
  if (getBooleanFlag(parsed.flags, 'help') || getBooleanFlag(parsed.flags, 'h')) {
    printJson(usage());
    return 0;
  }

  const workflowId = getFlag(parsed.flags, 'workflow-id');
  const definitionFile = getFlag(parsed.flags, 'definition-file');
  const definitionJson = getFlag(parsed.flags, 'definition-json');

  let definition = null;
  let source = 'definition-input';

  if (workflowId) {
    const config = loadConfig();
    const response = await requestJson(config, {
      method: 'GET',
      path: `/platform/v1/workflows/${workflowId}/definition`
    });

    if (!response.ok) {
      printJson(err('Failed to fetch workflow definition', response.raw, false, response.status));
      return 2;
    }

    const workflow = response.data;
    definition = workflow && typeof workflow === 'object' ? workflow.definition : null;
    if (!definition || typeof definition !== 'object') {
      printJson(err('Workflow definition missing in response', response.raw, false, response.status));
      return 2;
    }

    source = `workflow:${workflowId}`;
  } else if (definitionFile) {
    definition = parseDefinitionInput(readFileText(definitionFile));
    if (!definition) {
      printJson(err('Unable to parse workflow definition from definition-file'));
      return 2;
    }
    source = definitionFile;
  } else if (definitionJson) {
    definition = parseDefinitionInput(definitionJson);
    if (!definition) {
      printJson(err('Unable to parse workflow definition from definition-json'));
      return 2;
    }
  }

  if (!definition) {
    printJson(err('Provide --workflow-id, --definition-file, or --definition-json'));
    return 2;
  }

  const validation = validateDefinition(definition);

  printJson(ok({
    source,
    valid: validation.errors.length === 0,
    errors: validation.errors,
    warnings: validation.warnings,
    stats: validation.stats
  }));

  return 0;
}

main().catch((error) => {
  printJson(err('Unhandled error', { message: String(error?.message || error) }));
  process.exit(1);
});
```

## File: `skills/automate-whatsapp/scripts/variables-delete.js`
```javascript
#!/usr/bin/env node
import { loadConfig } from './lib/workflows/kapso-api.js';
import { ok, err, printJson } from './lib/workflows/result.js';
import { parseArgs, getFlag, getBooleanFlag } from './lib/workflows/args.js';

function usage() {
  return ok({
    usage: 'node scripts/variables-delete.js <workflow-id> --name <name>',
    env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
  });
}

async function main() {
  const parsed = parseArgs(process.argv.slice(2));
  if (getBooleanFlag(parsed.flags, 'help') || getBooleanFlag(parsed.flags, 'h')) {
    printJson(usage());
    return 0;
  }

  const workflowId = parsed.args[0] || getFlag(parsed.flags, 'workflow-id');
  const name = getFlag(parsed.flags, 'name');

  const config = loadConfig();

  printJson(err('Workflow variables delete is not available in the Platform API.', {
    workflow_id: workflowId,
    name,
    note: 'Only variable discovery is proposed; CRUD endpoints are missing.'
  }, true));

  return 2;
}

main().catch((error) => {
  printJson(err('Unhandled error', { message: String(error?.message || error) }));
  process.exit(1);
});
```

## File: `skills/automate-whatsapp/scripts/variables-list.js`
```javascript
#!/usr/bin/env node
import { loadConfig, requestJson } from './lib/workflows/kapso-api.js';
import { ok, err, printJson } from './lib/workflows/result.js';
import { parseArgs, getFlag, getBooleanFlag } from './lib/workflows/args.js';

function usage() {
  return ok({
    usage: 'node scripts/variables-list.js <workflow-id> [--workflow-id <id>]',
    env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
  });
}

async function main() {
  const parsed = parseArgs(process.argv.slice(2));
  if (getBooleanFlag(parsed.flags, 'help') || getBooleanFlag(parsed.flags, 'h')) {
    printJson(usage());
    return 0;
  }

  const workflowId = parsed.args[0] || getFlag(parsed.flags, 'workflow-id');
  if (!workflowId) {
    printJson(err('workflow_id is required'));
    return 2;
  }

  const config = loadConfig();
  const response = await requestJson(config, {
    method: 'GET',
    path: `/platform/v1/workflows/${workflowId}/variables`
  });

  if (!response.ok && response.status === 404) {
    printJson(err('Workflow variables endpoint is not available in the Platform API.', {
      endpoint: '/platform/v1/workflows/:id/variables'
    }, true, response.status));
    return 2;
  }

  if (!response.ok) {
    printJson(err('Failed to fetch workflow variables', response.raw, false, response.status));
    return 2;
  }

  printJson(ok({
    workflow_id: workflowId,
    variables: response.data
  }));

  return 0;
}

main().catch((error) => {
  printJson(err('Unhandled error', { message: String(error?.message || error) }));
  process.exit(1);
});
```

## File: `skills/automate-whatsapp/scripts/variables-set.js`
```javascript
#!/usr/bin/env node
import { loadConfig } from './lib/workflows/kapso-api.js';
import { ok, err, printJson } from './lib/workflows/result.js';
import { parseArgs, getFlag, getBooleanFlag } from './lib/workflows/args.js';

function usage() {
  return ok({
    usage: 'node scripts/variables-set.js <workflow-id> --name <name> --value <value>',
    env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
  });
}

async function main() {
  const parsed = parseArgs(process.argv.slice(2));
  if (getBooleanFlag(parsed.flags, 'help') || getBooleanFlag(parsed.flags, 'h')) {
    printJson(usage());
    return 0;
  }

  const workflowId = parsed.args[0] || getFlag(parsed.flags, 'workflow-id');
  const name = getFlag(parsed.flags, 'name');
  const value = getFlag(parsed.flags, 'value');

  const config = loadConfig();

  printJson(err('Workflow variables create/update is not available in the Platform API.', {
    workflow_id: workflowId,
    name,
    value,
    note: 'Only variable discovery is proposed; CRUD endpoints are missing.'
  }, true));

  return 2;
}

main().catch((error) => {
  printJson(err('Unhandled error', { message: String(error?.message || error) }));
  process.exit(1);
});
```

## File: `skills/automate-whatsapp/scripts/lib/databases/args.js`
```javascript
function hasHelpFlag(argv) {
  return argv.includes('--help') || argv.includes('-h');
}

function parseFlags(argv) {
  const flags = {};
  for (let index = 0; index < argv.length; index += 1) {
    const arg = argv[index];
    if (!arg.startsWith('--')) {
      continue;
    }
    const trimmed = arg.slice(2);
    const eqIndex = trimmed.indexOf('=');
    if (eqIndex >= 0) {
      const key = trimmed.slice(0, eqIndex);
      const value = trimmed.slice(eqIndex + 1);
      flags[key] = value;
      continue;
    }
    const next = argv[index + 1];
    if (!next || next.startsWith('--')) {
      flags[trimmed] = true;
      continue;
    }
    flags[trimmed] = next;
    index += 1;
  }
  return flags;
}

function requireFlag(flags, name) {
  const value = flags[name];
  if (typeof value !== 'string' || value.length === 0) {
    throw new Error(`Missing required flag --${name}`);
  }
  return value;
}

function parseJsonObject(value, name) {
  if (value === undefined || value === true) {
    throw new Error(`Missing required JSON for --${name}`);
  }
  try {
    const parsed = JSON.parse(value);
    if (!parsed || typeof parsed !== 'object' || Array.isArray(parsed)) {
      throw new Error('Expected JSON object');
    }
    return parsed;
  } catch (error) {
    throw new Error(`Invalid JSON for --${name}: ${String(error)}`);
  }
}

function parseJsonObjectOptional(value, name) {
  if (value === undefined || value === true) {
    return undefined;
  }
  try {
    const parsed = JSON.parse(value);
    if (!parsed || typeof parsed !== 'object' || Array.isArray(parsed)) {
      throw new Error('Expected JSON object');
    }
    return parsed;
  } catch (error) {
    throw new Error(`Invalid JSON for --${name}: ${String(error)}`);
  }
}

function parseNumber(value, name) {
  if (value === undefined || value === true) {
    return undefined;
  }
  const parsed = Number(value);
  if (Number.isNaN(parsed)) {
    throw new Error(`Invalid number for --${name}: ${value}`);
  }
  return parsed;
}

export {
  hasHelpFlag,
  parseFlags,
  requireFlag,
  parseJsonObject,
  parseJsonObjectOptional,
  parseNumber
};
```

## File: `skills/automate-whatsapp/scripts/lib/databases/filters.js`
```javascript
import { parseJsonObjectOptional } from './args.js';

function resolveFilters(flags) {
  const filters = parseJsonObjectOptional(flags.filters, 'filters');
  if (filters) {
    const entries = {};
    Object.entries(filters).forEach(([key, value]) => {
      entries[key] = String(value);
    });
    return entries;
  }
  if (typeof flags.id === 'string' && flags.id.length > 0) {
    return { id: `eq.${flags.id}` };
  }
  throw new Error('Provide --filters (JSON) or --id');
}

function filtersToQuery(filters) {
  const params = new URLSearchParams();
  Object.entries(filters).forEach(([key, value]) => {
    params.set(key, value);
  });
  const query = params.toString();
  return query ? `?${query}` : '';
}

export {
  resolveFilters,
  filtersToQuery
};
```

## File: `skills/automate-whatsapp/scripts/lib/databases/kapso-api.js`
```javascript
function requireEnv(name) {
  const value = process.env[name];
  if (!value) {
    throw new Error(`Missing required env var: ${name}`);
  }
  return value;
}

function normalizeBaseUrl(raw) {
  return raw.replace(/\/+$/, '');
}

function isLocalhost(hostname) {
  return hostname === 'localhost' || hostname === '127.0.0.1';
}

function validateBaseUrl(baseUrl) {
  if (!baseUrl) return;
  let parsed;
  try {
    parsed = new URL(baseUrl);
  } catch (error) {
    throw new Error(`Invalid KAPSO_API_BASE_URL: ${baseUrl}`);
  }
  if (!process.env.KAPSO_API_ALLOW_LOCALHOST && isLocalhost(parsed.hostname)) {
    throw new Error(
      `KAPSO_API_BASE_URL points to localhost (${parsed.hostname}). ` +
      'Set KAPSO_API_ALLOW_LOCALHOST=true if this is intentional.'
    );
  }
}

function kapsoConfigFromEnv() {
  const baseUrl = normalizeBaseUrl(requireEnv('KAPSO_API_BASE_URL'));
  validateBaseUrl(baseUrl);
  return {
    baseUrl,
    apiKey: requireEnv('KAPSO_API_KEY')
  };
}

async function kapsoRequest(config, path, init = {}) {
  const url = `${config.baseUrl}${path}`;
  const headers = new Headers(init.headers || undefined);
  headers.set('X-API-Key', config.apiKey);
  if (!headers.has('Content-Type')) {
    headers.set('Content-Type', 'application/json');
  }

  let response;
  try {
    response = await fetch(url, { ...init, headers });
  } catch (error) {
    throw new Error(
      `Kapso API request failed (network error) url=${url} error=${String(error?.message || error)}`
    );
  }
  const text = await response.text();

  if (!response.ok) {
    throw new Error(`Kapso API request failed (status=${response.status}) body=${text}`);
  }

  return text ? JSON.parse(text) : {};
}

export {
  kapsoConfigFromEnv,
  kapsoRequest
};
```

## File: `skills/automate-whatsapp/scripts/lib/functions/args.js`
```javascript
function hasHelpFlag(argv) {
  return argv.includes('--help') || argv.includes('-h');
}

function parseFlags(argv) {
  const flags = {};
  for (let index = 0; index < argv.length; index += 1) {
    const arg = argv[index];
    if (!arg.startsWith('--')) {
      continue;
    }
    const trimmed = arg.slice(2);
    const eqIndex = trimmed.indexOf('=');
    if (eqIndex >= 0) {
      const key = trimmed.slice(0, eqIndex);
      const value = trimmed.slice(eqIndex + 1);
      flags[key] = value;
      continue;
    }
    const next = argv[index + 1];
    if (!next || next.startsWith('--')) {
      flags[trimmed] = true;
      continue;
    }
    flags[trimmed] = next;
    index += 1;
  }
  return flags;
}

function requireFlag(flags, name) {
  const value = flags[name];
  if (typeof value !== 'string' || value.length === 0) {
    throw new Error(`Missing required flag --${name}`);
  }
  return value;
}

function parseJsonValue(value, name) {
  if (value === undefined || value === true) {
    throw new Error(`Missing required JSON for --${name}`);
  }
  try {
    return JSON.parse(value);
  } catch (error) {
    throw new Error(`Invalid JSON for --${name}: ${String(error)}`);
  }
}

export {
  hasHelpFlag,
  parseFlags,
  requireFlag,
  parseJsonValue
};
```

## File: `skills/automate-whatsapp/scripts/lib/functions/kapso-api.js`
```javascript
function requireEnv(name) {
  const value = process.env[name];
  if (!value) {
    throw new Error(`Missing required env var: ${name}`);
  }
  return value;
}

function normalizeBaseUrl(raw) {
  return raw.replace(/\/+$/, '');
}

function isLocalhost(hostname) {
  return hostname === 'localhost' || hostname === '127.0.0.1';
}

function validateBaseUrl(baseUrl) {
  if (!baseUrl) return;
  let parsed;
  try {
    parsed = new URL(baseUrl);
  } catch (error) {
    throw new Error(`Invalid KAPSO_API_BASE_URL: ${baseUrl}`);
  }
  if (!process.env.KAPSO_API_ALLOW_LOCALHOST && isLocalhost(parsed.hostname)) {
    throw new Error(
      `KAPSO_API_BASE_URL points to localhost (${parsed.hostname}). ` +
      'Set KAPSO_API_ALLOW_LOCALHOST=true if this is intentional.'
    );
  }
}

function kapsoConfigFromEnv() {
  const baseUrl = normalizeBaseUrl(requireEnv('KAPSO_API_BASE_URL'));
  validateBaseUrl(baseUrl);
  return {
    baseUrl,
    apiKey: requireEnv('KAPSO_API_KEY')
  };
}

async function kapsoRequest(config, path, init = {}) {
  const url = `${config.baseUrl}${path}`;
  const headers = new Headers(init.headers || undefined);
  headers.set('X-API-Key', config.apiKey);
  if (!headers.has('Content-Type')) {
    headers.set('Content-Type', 'application/json');
  }

  let response;
  try {
    response = await fetch(url, { ...init, headers });
  } catch (error) {
    throw new Error(
      `Kapso API request failed (network error) url=${url} error=${String(error?.message || error)}`
    );
  }
  const text = await response.text();

  if (!response.ok) {
    throw new Error(`Kapso API request failed (status=${response.status}) body=${text}`);
  }

  return text ? JSON.parse(text) : {};
}

export {
  kapsoConfigFromEnv,
  kapsoRequest
};
```

## File: `skills/automate-whatsapp/scripts/lib/workflows/args.js`
```javascript
export function parseArgs(argv) {
  const flags = {};
  const args = [];

  let i = 0;
  while (i < argv.length) {
    const token = argv[i];
    if (token.startsWith('--')) {
      const trimmed = token.slice(2);
      const eqIndex = trimmed.indexOf('=');
      if (eqIndex !== -1) {
        const key = trimmed.slice(0, eqIndex);
        const value = trimmed.slice(eqIndex + 1);
        flags[key] = value;
        i += 1;
        continue;
      }

      const key = trimmed;
      const next = argv[i + 1];
      if (!next || next.startsWith('--')) {
        flags[key] = true;
        i += 1;
      } else {
        flags[key] = next;
        i += 2;
      }
      continue;
    }

    args.push(token);
    i += 1;
  }

  return { args, flags };
}

export function getFlag(flags, name) {
  const value = flags[name];
  if (typeof value === 'string') return value;
  return undefined;
}

export function getBooleanFlag(flags, name) {
  return Boolean(flags[name]);
}

export function getNumberFlag(flags, name) {
  const value = getFlag(flags, name);
  if (!value) return undefined;
  const parsed = Number(value);
  return Number.isFinite(parsed) ? parsed : undefined;
}
```

## File: `skills/automate-whatsapp/scripts/lib/workflows/kapso-api.js`
```javascript
function requireEnv(name) {
  const value = process.env[name];
  if (!value) {
    throw new Error(`Missing required env var: ${name}`);
  }
  return value;
}

function normalizeBaseUrl(raw) {
  return raw.replace(/\/+$/, '');
}

function isLocalhost(hostname) {
  return hostname === 'localhost' || hostname === '127.0.0.1';
}

function validateBaseUrl(baseUrl) {
  if (!baseUrl) return;
  let parsed;
  try {
    parsed = new URL(baseUrl);
  } catch (error) {
    throw new Error(`Invalid KAPSO_API_BASE_URL: ${baseUrl}`);
  }
  if (!process.env.KAPSO_API_ALLOW_LOCALHOST && isLocalhost(parsed.hostname)) {
    throw new Error(
      `KAPSO_API_BASE_URL points to localhost (${parsed.hostname}). ` +
      'Set KAPSO_API_ALLOW_LOCALHOST=true if this is intentional.'
    );
  }
}

export function loadConfig(options = {}) {
  const requireApi = options.requireApi !== false;

  const rawBaseUrl = requireApi ? requireEnv('KAPSO_API_BASE_URL') : (process.env.KAPSO_API_BASE_URL || '');
  const baseUrl = rawBaseUrl ? normalizeBaseUrl(rawBaseUrl) : '';
  validateBaseUrl(baseUrl);
  const apiKey = requireApi ? requireEnv('KAPSO_API_KEY') : (process.env.KAPSO_API_KEY || '');

  return { baseUrl, apiKey };
}

function buildUrl(baseUrl, path) {
  const trimmed = baseUrl.replace(/\/+$/, '');
  const safePath = path.startsWith('/') ? path.slice(1) : path;
  return `${trimmed}/${safePath}`;
}

export async function requestJson(config, options) {
  const url = new URL(buildUrl(config.baseUrl, options.path));

  if (options.query) {
    Object.entries(options.query).forEach(([key, value]) => {
      if (value === undefined || value === null || value === '') return;
      url.searchParams.set(key, String(value));
    });
  }

  const headers = {
    Accept: 'application/json'
  };

  if (config.apiKey) {
    headers['X-API-Key'] = config.apiKey;
  }

  let body;
  if (options.body !== undefined) {
    headers['Content-Type'] = 'application/json';
    body = JSON.stringify(options.body);
  }

  let response;
  try {
    response = await fetch(url.toString(), {
      method: options.method,
      headers,
      body
    });
  } catch (error) {
    return {
      ok: false,
      status: 0,
      error: 'Network error while calling Kapso API',
      raw: { message: String(error?.message || error), url: url.toString() }
    };
  }

  const text = await response.text();
  let parsed = text;
  if (text) {
    try {
      parsed = JSON.parse(text);
    } catch {
      parsed = text;
    }
  }

  if (response.ok) {
    const data = (parsed && typeof parsed === 'object' && 'data' in parsed)
      ? parsed.data
      : parsed;

    return {
      ok: true,
      status: response.status,
      data,
      raw: parsed
    };
  }

  const message = (parsed && typeof parsed === 'object' && 'error' in parsed)
    ? String(parsed.error)
    : `HTTP ${response.status}`;

  return {
    ok: false,
    status: response.status,
    error: message,
    raw: parsed
  };
}
```

## File: `skills/automate-whatsapp/scripts/lib/workflows/result.js`
```javascript
export function ok(data) {
  return { ok: true, data };
}

export function err(message, details, blocked, status) {
  const error = { message };
  if (details !== undefined) error.details = details;
  if (blocked !== undefined) error.blocked = blocked;
  if (status !== undefined) error.status = status;
  return { ok: false, error };
}

export function printJson(value) {
  // eslint-disable-next-line no-console
  console.log(JSON.stringify(value, null, 2));
}
```

## File: `skills/integrate-whatsapp/SKILL.md`
```markdown
---
name: integrate-whatsapp
description: "Connect WhatsApp to your product with Kapso: onboard customers with setup links, detect connections, receive events via webhooks, and send messages/templates/media. Also manage WhatsApp Flows (create/update/publish, data endpoints, encryption). Use when integrating WhatsApp end-to-end."
---

# Integrate WhatsApp

## Setup

Preferred path:
- Kapso CLI installed and authenticated (`kapso login`)
- Use `kapso status` to confirm project access before onboarding or messaging

Fallback path:
Env vars:
- `KAPSO_API_BASE_URL` (host only, no `/platform/v1`)
- `KAPSO_API_KEY`
- `META_GRAPH_VERSION` (optional, default `v24.0`)

Auth header (direct API calls):
```
X-API-Key: <api_key>
```

Install deps (once):
```bash
npm i
```

## Connect WhatsApp (setup links)

Preferred onboarding path (CLI):

1. Start onboarding: `kapso setup`
2. If setup is blocked, resolve context with:
   - `kapso projects list`
   - `kapso projects use <project-id>`
   - `kapso customers list`
   - `kapso customers new --name "<customer-name>" --external-id <external-id>`
   - `kapso setup --customer <customer-id>`
3. Complete the hosted onboarding URL
4. Confirm connected numbers: `kapso whatsapp numbers list --output json`
5. Resolve the exact number you want to operate: `kapso whatsapp numbers resolve --phone-number "<display-number>" --output json`

Fallback onboarding flow (direct API):

1. Create customer: `POST /platform/v1/customers`
2. Generate setup link: `POST /platform/v1/customers/:id/setup_links`
3. Customer completes embedded signup
4. Use `phone_number_id` to send messages and configure webhooks

Detect connection:
- Project webhook `whatsapp.phone_number.created` (recommended)
- Success redirect URL query params (use for frontend UX)

Recommended Kapso setup-link defaults:
```json
{
  "setup_link": {
    "allowed_connection_types": ["dedicated"],
    "provision_phone_number": true,
    "phone_number_country_isos": ["US"]
  }
}
```

Notes:
- `kapso setup` and `kapso whatsapp numbers new` use dedicated plus provisioning by default.
- Keep `phone_number_country_isos`, `phone_number_area_code`, `language`, and redirect URLs as optional overrides.

- Platform API base: `/platform/v1`
- Meta proxy base: `/meta/whatsapp/v24.0` (messaging, templates, media)
- Use `phone_number_id` as the primary WhatsApp identifier

## Receive events (webhooks)

Use webhooks to receive:
- Project events (connection lifecycle, workflow events)
- Phone-number events (messages, conversations, delivery status)

Scope rules:
- **Project webhooks**: only project-level events (connection lifecycle, workflow events)
- **Phone-number webhooks**: only WhatsApp message + conversation events for that `phone_number_id`
- WhatsApp message/conversation events (`whatsapp.message.*`, `whatsapp.conversation.*`) are **phone-number only**

Create a webhook:
- Project-level: `node scripts/create.js --scope project --url <https://...> --events <csv>`
- Phone-number: `node scripts/create.js --phone-number-id <id> --url <https://...> --events <csv>`

Common flags for create/update:
- `--url <https://...>` - webhook destination
- `--events <csv|json-array>` - event types (Kapso webhooks)
- `--kind <kapso|meta>` - Kapso (event-based) vs raw Meta forwarding
- `--payload-version <v1|v2>` - payload format (`v2` recommended)
- `--buffer-enabled <true|false>` - enable buffering for `whatsapp.message.received`
- `--buffer-window-seconds <n>` - 1-60 seconds
- `--max-buffer-size <n>` - 1-100
- `--active <true|false>` - enable/disable

Test delivery:
```bash
node scripts/test.js --webhook-id <id>
```

Always verify signatures. See:
- `references/webhooks-overview.md`
- `references/webhooks-reference.md`

## Send and read messages

### Discover IDs first

Two Meta IDs are needed for different operations:

| ID | Used for | How to discover |
|----|----------|-----------------|
| `business_account_id` (WABA) | Template CRUD | `kapso whatsapp numbers resolve --phone-number "<display-number>" --output json` or `node scripts/list-platform-phone-numbers.mjs` |
| `phone_number_id` | Sending messages, media upload | `kapso whatsapp numbers resolve --phone-number "<display-number>" --output json` or `node scripts/list-platform-phone-numbers.mjs` |

### Operate with the CLI first

Common commands:
```bash
kapso whatsapp numbers list --output json
kapso whatsapp numbers resolve --phone-number "<display-number>" --output json
kapso whatsapp messages send --phone-number-id <PHONE_NUMBER_ID> --to <wa-id> --text "Hello from Kapso"
kapso whatsapp messages list --phone-number-id <PHONE_NUMBER_ID> --limit 50 --output json
kapso whatsapp messages get <MESSAGE_ID> --phone-number-id <PHONE_NUMBER_ID> --output json
kapso whatsapp conversations list --phone-number-id <PHONE_NUMBER_ID> --output json
kapso whatsapp templates list --phone-number-id <PHONE_NUMBER_ID> --output json
kapso whatsapp templates get <TEMPLATE_ID> --phone-number-id <PHONE_NUMBER_ID> --output json
```

### SDK setup

Install:
```bash
npm install @kapso/whatsapp-cloud-api
```

Create client:
```ts
import { WhatsAppClient } from "@kapso/whatsapp-cloud-api";

const client = new WhatsAppClient({
  baseUrl: "https://api.kapso.ai/meta/whatsapp",
  kapsoApiKey: process.env.KAPSO_API_KEY!
});
```

### Send a text message

Via SDK:
```ts
await client.messages.sendText({
  phoneNumberId: "<PHONE_NUMBER_ID>",
  to: "+15551234567",
  body: "Hello from Kapso"
});
```

### Send a template message

1. Discover IDs: `node scripts/list-platform-phone-numbers.mjs`
2. Draft template payload from `assets/template-utility-order-status-update.json`
3. Create: `node scripts/create-template.mjs --business-account-id <WABA_ID> --file <payload.json>`
4. Check status: `node scripts/template-status.mjs --business-account-id <WABA_ID> --name <name>`
5. Send: `node scripts/send-template.mjs --phone-number-id <ID> --file <send-payload.json>`

### Send an interactive message

Interactive messages require an active 24-hour session window. For outbound notifications outside the window, use templates.

1. Discover `phone_number_id`
2. Pick payload from `assets/send-interactive-*.json`
3. Send: `node scripts/send-interactive.mjs --phone-number-id <ID> --file <payload.json>`

### Read inbox data

Preferred path:
- CLI: `kapso whatsapp messages ...`, `kapso whatsapp conversations ...`, `kapso whatsapp templates ...`

Fallback path:
- Proxy: `GET /{phone_number_id}/messages`, `GET /{phone_number_id}/conversations`
- SDK: `client.messages.query()`, `client.messages.get()`, `client.conversations.list()`, `client.conversations.get()`, `client.templates.get()`

### Template rules

Creation:
- Use `parameter_format: "NAMED"` with `{{param_name}}` (preferred over positional)
- Include examples when using variables in HEADER/BODY
- Use `language` (not `language_code`)
- Don't interleave QUICK_REPLY with URL/PHONE_NUMBER buttons
- URL button variables must be at the end of the URL and use positional `{{1}}`

Send-time:
- For NAMED templates, include `parameter_name` in header/body params
- URL buttons need a `button` component with `sub_type: "url"` and `index`
- Media headers use either `id` or `link` (never both)

## WhatsApp Flows

Use Flows to build native WhatsApp forms. Read `references/whatsapp-flows-spec.md` before editing Flow JSON.

### Create and publish a flow

1. Create flow: `node scripts/create-flow.js --phone-number-id <id> --name <name>`
2. Update JSON: `node scripts/update-flow-json.js --flow-id <id> --json-file <path>`
3. Publish: `node scripts/publish-flow.js --flow-id <id>`
4. Test: `node scripts/send-test-flow.js --phone-number-id <id> --flow-id <id> --to <phone>`

### Attach a data endpoint (dynamic flows)

1. Set up encryption: `node scripts/setup-encryption.js --flow-id <id>`
2. Create endpoint: `node scripts/set-data-endpoint.js --flow-id <id> --code-file <path>`
3. Deploy: `node scripts/deploy-data-endpoint.js --flow-id <id>`
4. Register: `node scripts/register-data-endpoint.js --flow-id <id>`

### Flow JSON rules

Static flows (no data endpoint):
- Use `version: "7.3"`
- `routing_model` and `data_api_version` are optional
- See `assets/sample-flow.json`

Dynamic flows (with data endpoint):
- Use `version: "7.3"` with `data_api_version: "3.0"`
- `routing_model` is required (defines valid screen transitions)
- See `assets/dynamic-flow.json`

### Data endpoint rules

Handler signature:
```js
async function handler(request, env) {
  const body = await request.json();
  // body.data_exchange.action: INIT | data_exchange | BACK
  // body.data_exchange.screen: current screen id
  // body.data_exchange.data: user inputs
  return Response.json({
    version: "3.0",
    screen: "NEXT_SCREEN_ID",
    data: { }
  });
}
```

- Do not use `export` or `module.exports`
- Completion uses `screen: "SUCCESS"` with `extension_message_response.params`
- Do not include `endpoint_uri` or `data_channel_uri` (Kapso injects these)

### Troubleshooting

- Preview shows `"flow_token is missing"`: flow is dynamic without a data endpoint. Attach one and refresh.
- Encryption setup errors: enable encryption in Settings for the phone number/WABA.
- OAuthException 139000 (Integrity): WABA must be verified in Meta security center.

## Scripts

### Webhooks

| Script | Purpose |
|--------|---------|
| `list.js` | List webhooks |
| `get.js` | Get webhook details |
| `create.js` | Create a webhook |
| `update.js` | Update a webhook |
| `delete.js` | Delete a webhook |
| `test.js` | Send a test event |

### Messaging and templates

| Script | Purpose | Required ID |
|--------|---------|-------------|
| `list-platform-phone-numbers.mjs` | Discover business_account_id + phone_number_id | — |
| `list-connected-numbers.mjs` | List WABA phone numbers | business_account_id |
| `list-templates.mjs` | List templates (with filters) | business_account_id |
| `template-status.mjs` | Check single template status | business_account_id |
| `create-template.mjs` | Create a template | business_account_id |
| `update-template.mjs` | Update existing template | business_account_id |
| `send-template.mjs` | Send template message | phone_number_id |
| `send-interactive.mjs` | Send interactive message | phone_number_id |
| `upload-media.mjs` | Upload media for send-time headers | phone_number_id |

### Flows

| Script | Purpose |
|--------|---------|
| `list-flows.js` | List all flows |
| `create-flow.js` | Create a new flow |
| `get-flow.js` | Get flow details |
| `read-flow-json.js` | Read flow JSON |
| `update-flow-json.js` | Update flow JSON (creates new version) |
| `publish-flow.js` | Publish a flow |
| `get-data-endpoint.js` | Get data endpoint config |
| `set-data-endpoint.js` | Create/update data endpoint code |
| `deploy-data-endpoint.js` | Deploy data endpoint |
| `register-data-endpoint.js` | Register data endpoint with Meta |
| `get-encryption-status.js` | Check encryption status |
| `setup-encryption.js` | Set up flow encryption |
| `send-test-flow.js` | Send a test flow message |
| `delete-flow.js` | Delete a flow |
| `list-flow-responses.js` | List stored flow responses |
| `list-function-logs.js` | List function logs |
| `list-function-invocations.js` | List function invocations |

### OpenAPI

| Script | Purpose |
|--------|---------|
| `openapi-explore.mjs` | Explore OpenAPI (search/op/schema/where) |

Examples:
```bash
node scripts/openapi-explore.mjs --spec whatsapp search "template"
node scripts/openapi-explore.mjs --spec whatsapp op sendMessage
node scripts/openapi-explore.mjs --spec whatsapp schema TemplateMessage
node scripts/openapi-explore.mjs --spec platform ops --tag "WhatsApp Flows"
node scripts/openapi-explore.mjs --spec platform op setupWhatsappFlowEncryption
node scripts/openapi-explore.mjs --spec platform search "setup link"
```

## Assets

| File | Description |
|------|-------------|
| `template-utility-order-status-update.json` | UTILITY template with named params + URL button |
| `send-template-order-status-update.json` | Send-time payload for order_status_update |
| `template-utility-named.json` | UTILITY template showing button ordering rules |
| `template-marketing-media-header.json` | MARKETING template with IMAGE header |
| `template-authentication-otp.json` | AUTHENTICATION OTP template (COPY_CODE) |
| `send-interactive-buttons.json` | Interactive button message |
| `send-interactive-list.json` | Interactive list message |
| `send-interactive-cta-url.json` | Interactive CTA URL message |
| `send-interactive-location-request.json` | Location request message |
| `send-interactive-catalog-message.json` | Catalog message |
| `sample-flow.json` | Static flow example (no endpoint) |
| `dynamic-flow.json` | Dynamic flow example (with endpoint) |
| `webhooks-example.json` | Webhook create/update payload example |

## References

- [references/getting-started.md](../bmad_repo/getting-started.md) - Platform onboarding
- [references/platform-api-reference.md](references/platform-api-reference.md) - Full endpoint reference
- [references/setup-links.md](references/setup-links.md) - Setup link configuration
- [references/detecting-whatsapp-connection.md](references/detecting-whatsapp-connection.md) - Connection detection methods
- [references/webhooks-overview.md](references/webhooks-overview.md) - Webhook types, signature verification, retries
- [references/webhooks-event-types.md](references/webhooks-event-types.md) - Available events
- [references/webhooks-reference.md](references/webhooks-reference.md) - Webhook API and payload notes
- [references/templates-reference.md](references/templates-reference.md) - Template creation rules, components cheat sheet, send-time components
- [references/whatsapp-api-reference.md](references/whatsapp-api-reference.md) - Meta proxy payloads for messages and conversations
- [references/whatsapp-cloud-api-js.md](references/whatsapp-cloud-api-js.md) - SDK usage for sending and reading messages
- [references/whatsapp-flows-spec.md](references/whatsapp-flows-spec.md) - Flow JSON spec

## Related skills

- `automate-whatsapp` - Workflows, agents, and automations
- `observe-whatsapp` - Debugging, logs, health checks

<!-- FILEMAP:BEGIN -->
```text
[integrate-whatsapp file map]|root: .
|.:{package.json,SKILL.md}
|assets:{dynamic-flow.json,sample-flow.json,send-interactive-buttons.json,send-interactive-catalog-message.json,send-interactive-cta-url.json,send-interactive-list.json,send-interactive-location-request.json,send-template-order-status-update.json,template-authentication-otp.json,template-marketing-media-header.json,template-utility-named.json,template-utility-order-status-update.json,webhooks-example.json}
|references:{detecting-whatsapp-connection.md,getting-started.md,platform-api-reference.md,setup-links.md,templates-reference.md,webhooks-event-types.md,webhooks-overview.md,webhooks-reference.md,whatsapp-api-reference.md,whatsapp-cloud-api-js.md,whatsapp-flows-spec.md}
|scripts:{create-flow.js,create-function.js,create-template.mjs,create.js,delete-flow.js,delete.js,deploy-data-endpoint.js,deploy-function.js,get-data-endpoint.js,get-encryption-status.js,get-flow.js,get-function.js,get.js,list-connected-numbers.mjs,list-flow-responses.js,list-flows.js,list-function-invocations.js,list-function-logs.js,list-platform-phone-numbers.mjs,list-templates.mjs,list.js,openapi-explore.mjs,publish-flow.js,read-flow-json.js,register-data-endpoint.js,send-interactive.mjs,send-template.mjs,send-test-flow.js,set-data-endpoint.js,setup-encryption.js,submit-template.mjs,template-status.mjs,test.js,update-flow-json.js,update-function.js,update-template.mjs,update.js,upload-media.mjs,upload-template-header-handle.mjs}
|scripts/lib:{args.mjs,cli.js,env.js,env.mjs,http.js,output.js,output.mjs,request.mjs,run.js,whatsapp-flow.js}
|scripts/lib/webhooks:{args.js,kapso-api.js,webhook.js}
```
<!-- FILEMAP:END -->
```

## File: `skills/integrate-whatsapp/package.json`
```json
{
  "private": true,
  "dependencies": {
    "yaml": "^2.6.0"
  },
  "scripts": {
    "openapi": "node scripts/openapi-explore.mjs"
  }
}

```

## File: `skills/integrate-whatsapp/assets/dynamic-flow.json`
```json
{
  "version": "7.3",
  "data_api_version": "3.0",
  "routing_model": {
    "SELECT_DATE": ["SELECT_SLOT", "SUCCESS"],
    "SELECT_SLOT": ["SUCCESS"]
  },
  "screens": [
    {
      "id": "SELECT_DATE",
      "title": "Book appointment",
      "data": {
        "error_message": {
          "type": "string",
          "__example__": ""
        }
      },
      "layout": {
        "type": "SingleColumnLayout",
        "children": [
          {
            "type": "TextBody",
            "text": "Select a date for your appointment."
          },
          {
            "type": "DatePicker",
            "name": "date",
            "label": "Date",
            "on-select-action": {
              "name": "data_exchange",
              "payload": {
                "date": "${form.date}"
              }
            }
          },
          {
            "type": "Footer",
            "label": "Continue",
            "on-click-action": {
              "name": "data_exchange",
              "payload": {
                "date": "${form.date}"
              }
            }
          }
        ]
      }
    },
    {
      "id": "SELECT_SLOT",
      "title": "Select time",
      "data": {
        "selected_date": {
          "type": "string",
          "__example__": "2025-01-15"
        },
        "available_slots": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "id": { "type": "string" },
              "title": { "type": "string" }
            }
          },
          "__example__": [
            { "id": "09:00", "title": "9:00 AM" },
            { "id": "10:00", "title": "10:00 AM" }
          ]
        },
        "error_message": {
          "type": "string",
          "__example__": ""
        }
      },
      "terminal": true,
      "layout": {
        "type": "SingleColumnLayout",
        "children": [
          {
            "type": "TextBody",
            "text": "Available times for ${data.selected_date}:"
          },
          {
            "type": "RadioButtonsGroup",
            "name": "slot",
            "label": "Time slot",
            "data-source": "${data.available_slots}",
            "required": true
          },
          {
            "type": "Footer",
            "label": "Book",
            "on-click-action": {
              "name": "data_exchange",
              "payload": {
                "date": "${data.selected_date}",
                "slot": "${form.slot}"
              }
            }
          }
        ]
      }
    }
  ]
}
```

## File: `skills/integrate-whatsapp/assets/sample-flow.json`
```json
{
  "version": "7.3",
  "screens": [
    {
      "id": "WELCOME",
      "terminal": true,
      "title": "Quick signup",
      "layout": {
        "type": "SingleColumnLayout",
        "children": [
          {
            "type": "TextBody",
            "text": "Tell us your name to get started."
          },
          {
            "type": "TextInput",
            "name": "full_name",
            "label": "Full name",
            "required": true
          },
          {
            "type": "Footer",
            "label": "Submit",
            "on-click-action": {
              "name": "complete",
              "payload": {}
            }
          }
        ]
      }
    }
  ]
}
```

## File: `skills/integrate-whatsapp/assets/send-interactive-buttons.json`
```json
{
  "messaging_product": "whatsapp",
  "to": "15551234567",
  "type": "interactive",
  "interactive": {
    "type": "button",
    "body": { "text": "Choose an option:" },
    "action": {
      "buttons": [
        { "type": "reply", "reply": { "id": "accept", "title": "Accept" } },
        { "type": "reply", "reply": { "id": "decline", "title": "Decline" } }
      ]
    }
  }
}

```

## File: `skills/integrate-whatsapp/assets/send-interactive-catalog-message.json`
```json
{
  "messaging_product": "whatsapp",
  "to": "15551234567",
  "type": "interactive",
  "interactive": {
    "type": "catalog_message",
    "body": { "text": "Browse our catalog on WhatsApp." },
    "action": {
      "name": "catalog_message",
      "parameters": { "thumbnail_product_retailer_id": "SKU_THUMBNAIL" }
    }
  }
}

```

## File: `skills/integrate-whatsapp/assets/send-interactive-cta-url.json`
```json
{
  "messaging_product": "whatsapp",
  "to": "15551234567",
  "type": "interactive",
  "interactive": {
    "type": "cta_url",
    "body": { "text": "Track your order:" },
    "action": {
      "name": "cta_url",
      "parameters": {
        "display_text": "Track order",
        "url": "https://example.com/orders/ORDER-123"
      }
    }
  }
}

```

## File: `skills/integrate-whatsapp/assets/send-interactive-list.json`
```json
{
  "messaging_product": "whatsapp",
  "to": "15551234567",
  "type": "interactive",
  "interactive": {
    "type": "list",
    "body": { "text": "Choose your preferred delivery option:" },
    "action": {
      "button": "View options",
      "sections": [
        {
          "title": "Delivery",
          "rows": [
            { "id": "standard", "title": "Standard", "description": "3-5 business days" },
            { "id": "express", "title": "Express", "description": "1-2 business days" }
          ]
        }
      ]
    }
  }
}

```

## File: `skills/integrate-whatsapp/assets/send-interactive-location-request.json`
```json
{
  "messaging_product": "whatsapp",
  "to": "15551234567",
  "type": "interactive",
  "interactive": {
    "type": "location_request_message",
    "body": { "text": "Please share your location." },
    "action": { "name": "send_location" }
  }
}

```

## File: `skills/integrate-whatsapp/assets/send-template-order-status-update.json`
```json
{
  "messaging_product": "whatsapp",
  "to": "15551234567",
  "type": "template",
  "template": {
    "name": "order_status_update",
    "language": { "code": "en_US" },
    "components": [
      {
        "type": "header",
        "parameters": [
          { "type": "text", "parameter_name": "order_id", "text": "ORDER-123" }
        ]
      },
      {
        "type": "body",
        "parameters": [
          { "type": "text", "parameter_name": "customer_name", "text": "Alex" },
          { "type": "text", "parameter_name": "status", "text": "shipped" },
          { "type": "text", "parameter_name": "details", "text": "Expected delivery: Jan 25" }
        ]
      },
      {
        "type": "button",
        "sub_type": "url",
        "index": "0",
        "parameters": [{ "type": "text", "text": "ORDER-123" }]
      }
    ]
  }
}

```

## File: `skills/integrate-whatsapp/assets/template-authentication-otp.json`
```json
{
  "name": "login_otp",
  "language": "en_US",
  "category": "AUTHENTICATION",
  "components": [
    {
      "type": "BODY",
      "add_security_recommendation": true,
      "code_expiration_minutes": 10
    },
    {
      "type": "BUTTONS",
      "buttons": [
        { "type": "OTP", "otp_type": "COPY_CODE", "text": "Copy code" }
      ]
    }
  ]
}
```

## File: `skills/integrate-whatsapp/assets/template-marketing-media-header.json`
```json
{
  "name": "product_launch_image",
  "language": "en_US",
  "category": "MARKETING",
  "parameter_format": "NAMED",
  "components": [
    {
      "type": "HEADER",
      "format": "IMAGE",
      "example": {
        "header_handle": ["HEADER_HANDLE_PLACEHOLDER"]
      }
    },
    {
      "type": "BODY",
      "text": "Hi {{first_name}}, meet the new release.",
      "example": {
        "body_text_named_params": [
          { "param_name": "first_name", "example": "Jordan" }
        ]
      }
    }
  ]
}

```

## File: `skills/integrate-whatsapp/assets/template-utility-named.json`
```json
{
  "name": "order_ready_named",
  "language": "en_US",
  "category": "UTILITY",
  "parameter_format": "NAMED",
  "components": [
    {
      "type": "HEADER",
      "format": "TEXT",
      "text": "Order {{order_id}} is ready",
      "example": {
        "header_text_named_params": [
          { "param_name": "order_id", "example": "ORDER-123" }
        ]
      }
    },
    {
      "type": "BODY",
      "text": "Hi {{customer_name}}, your total is {{amount}}.",
      "example": {
        "body_text_named_params": [
          { "param_name": "customer_name", "example": "Alex" },
          { "param_name": "amount", "example": "$42.00" }
        ]
      }
    },
    {
      "type": "FOOTER",
      "text": "Reply STOP to opt out"
    },
    {
      "type": "BUTTONS",
      "buttons": [
        { "type": "QUICK_REPLY", "text": "Need help" },
        {
          "type": "URL",
          "text": "Track order",
          "url": "https://example.com/track?id={{1}}",
          "example": ["https://example.com/track?id=ORDER-123"]
        }
      ]
    }
  ]
}

```

## File: `skills/integrate-whatsapp/assets/template-utility-order-status-update.json`
```json
{
  "name": "order_status_update",
  "language": "en_US",
  "category": "UTILITY",
  "parameter_format": "NAMED",
  "components": [
    {
      "type": "HEADER",
      "format": "TEXT",
      "text": "Order {{order_id}} update",
      "example": {
        "header_text_named_params": [
          { "param_name": "order_id", "example": "ORDER-123" }
        ]
      }
    },
    {
      "type": "BODY",
      "text": "Hi {{customer_name}}, your order is {{status}}. {{details}}",
      "example": {
        "body_text_named_params": [
          { "param_name": "customer_name", "example": "Alex" },
          { "param_name": "status", "example": "shipped" },
          { "param_name": "details", "example": "Expected delivery: Jan 25" }
        ]
      }
    },
    {
      "type": "FOOTER",
      "text": "Reply STOP to opt out"
    },
    {
      "type": "BUTTONS",
      "buttons": [
        {
          "type": "URL",
          "text": "Track order",
          "url": "https://example.com/orders/{{1}}",
          "example": ["https://example.com/orders/ORDER-123"]
        }
      ]
    }
  ]
}

```

## File: `skills/integrate-whatsapp/assets/webhooks-example.json`
```json
{
  "url": "https://example.com/webhooks/kapso",
  "events": ["whatsapp.message.received", "whatsapp.message.failed"],
  "payload_version": "v2",
  "active": true,
  "headers": {
    "X-Custom-Header": "my-value"
  },
  "buffer_enabled": true,
  "buffer_window_seconds": 5,
  "max_buffer_size": 10
}
```

## File: `skills/integrate-whatsapp/references/detecting-whatsapp-connection.md`
```markdown
---
title: Connection detection
description: Know when customers complete WhatsApp onboarding
---

You have two ways to detect when customers connect their WhatsApp account through setup links.

## 1. Project webhooks

Configure a project webhook to receive the `whatsapp.phone_number.created` event. This is the recommended approach for server-to-server notifications.

### Setup

1. Open the sidebar and click **Webhooks**
2. Go to the **Project webhooks** tab
3. Click **Add Webhook**
4. Enter your HTTPS endpoint URL
5. Copy the auto-generated secret key
6. Subscribe to `whatsapp.phone_number.created` event

### Webhook payload

```json
{
  "phone_number_id": "123456789012345",
  "project": {
    "id": "990e8400-e29b-41d4-a716-446655440004"
  },
  "customer": {
    "id": "880e8400-e29b-41d4-a716-446655440003"
  }
}
```

### Handle the webhook

```javascript
app.post('/webhooks/project', async (req, res) => {
  const { event, data } = req.body;

  if (event === 'whatsapp.phone_number.created') {
    const { phone_number_id, customer } = data;

    // Update your database
    await db.customers.update(customer.id, {
      phone_number_id,
      whatsapp_connected: true,
      connected_at: new Date()
    });

    // Trigger welcome flow
    await sendWelcomeMessage(phone_number_id, customer.id);
  }

  res.status(200).send('OK');
});
```

See [webhooks documentation](/brain/knowledge/docs_legacy/platform/webhooks) for signature verification and best practices.

## 2. Success redirect URL

When customers complete WhatsApp setup, they're redirected to your `success_redirect_url` with query parameters.

### Setup

When creating a setup link, provide redirect URLs:

```javascript
const KAPSO_API_BASE_URL = 'https://api.kapso.ai';
const setupLink = await fetch(`${KAPSO_API_BASE_URL}/platform/v1/customers/customer-123/setup_links`, {
  method: 'POST',
  headers: {
    'X-API-Key': 'YOUR_API_KEY',
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    setup_link: {
      success_redirect_url: 'https://your-app.com/whatsapp/success',
      failure_redirect_url: 'https://your-app.com/whatsapp/failed'
    }
  })
});
```

### Query parameters

After successful setup, customer is redirected to:

```
https://your-app.com/whatsapp/success?setup_link_id=...&status=completed&phone_number_id=123456789012345&business_account_id=...&provisioned_phone_number_id=...&display_phone_number=%2B15551234567
```

**Parameters**:
- `setup_link_id` - UUID of the setup link
- `status` - Always `completed` for success
- `phone_number_id` - WhatsApp phone number ID (primary identifier)
- `business_account_id` - Meta WABA ID (if available)
- `provisioned_phone_number_id` - Kapso phone number ID (if provisioning was used)
- `display_phone_number` - E.164 formatted phone number (URL encoded)

### Handle the redirect

```javascript
app.get('/whatsapp/success', async (req, res) => {
  const {
    setup_link_id,
    status,
    phone_number_id,
    business_account_id,
    provisioned_phone_number_id,
    display_phone_number
  } = req.query;

  // Update your database
  await db.customers.update({
    phone_number_id,
    business_account_id,
    display_phone_number: decodeURIComponent(display_phone_number),
    whatsapp_connected: true,
    connected_at: new Date()
  });

  // Show success page to customer
  res.render('whatsapp-connected', {
    phoneNumber: decodeURIComponent(display_phone_number)
  });
});
```

<Note>
These parameters are convenience identifiers to avoid extra API fetches. Use `phone_number_id` as the primary identifier.
</Note>

### Failure redirect

If setup fails, customer is redirected to your `failure_redirect_url`:

```
https://your-app.com/whatsapp/failed?setup_link_id=...&error_code=facebook_auth_failed
```

**Error codes**:
- `facebook_auth_failed` - Facebook login cancelled
- `phone_verification_failed` - Phone verification failed
- `waba_limit_reached` - Too many WhatsApp accounts
- `token_exchange_failed` - OAuth failed
- `link_expired` - Link expired (30 days)
- `already_used` - Link already used

```javascript
app.get('/whatsapp/failed', (req, res) => {
  const { setup_link_id, error_code } = req.query;

  // Log failure for monitoring
  await logSetupFailure(setup_link_id, error_code);

  // Show user-friendly error message
  res.render('whatsapp-setup-failed', {
    errorMessage: getErrorMessage(error_code)
  });
});
```

## Choosing the right method

**Use project webhooks when**:
- You need server-to-server notification
- Customer doesn't need immediate visual feedback
- You're building automated onboarding flows
- You need to process the connection before showing UI

**Use success redirect when**:
- Customer needs immediate confirmation in your app
- You want to show a custom success page
- You're building a wizard-style onboarding flow
- You need to collect additional information after connection

**Use both**:
- Webhook for backend processing (database updates, welcome messages)
- Redirect for frontend experience (success page, next steps)
```

## File: `skills/integrate-whatsapp/references/getting-started.md`
```markdown
---
title: Getting started
description: Enable WhatsApp for your customers
---

Kapso Platform lets your customers connect their own WhatsApp Business accounts without sharing credentials. Each customer uses their own number while you handle the automation.

## Quick example

```javascript
// 1. Create customer
const customer = await createCustomer({ name: 'Acme Corp' });

// 2. Setup link
const setupLink = await generateSetupLink(customer.id);
console.log(`Setup link: ${setupLink.url}`);

// 3. Send message
await sendWhatsAppMessage({
  customer_id: customer.id,
  phone_number: '+1234567890',
  content: 'Order confirmed!'
});
```

## Use cases

Perfect when you need your customers to use their own WhatsApp:

- **CRM platforms** - Let each client connect their WhatsApp for customer communication
- **Appointment booking** - Clinics and salons send reminders from their own number
- **E-commerce tools** - Stores send order updates using their WhatsApp Business
- **Marketing platforms** - Agencies manage multiple client WhatsApp accounts
- **Support software** - Each company provides support through their WhatsApp

## Step 1: Create a customer

```bash
curl -X POST https://api.kapso.ai/platform/v1/customers \
  -H "X-API-Key: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "customer": {
      "name": "Acme Corporation",
      "external_customer_id": "CUS-12345"
    }
  }'
```

Response:
```json
{
  "data": {
    "id": "customer-abc123",
    "name": "Acme Corporation",
    "external_customer_id": "CUS-12345"
  }
}
```

## Step 2: Generate setup link

```bash
curl -X POST https://api.kapso.ai/platform/v1/customers/customer-abc123/setup_links \
  -H "X-API-Key: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"setup_link":{}}'
```

Response:
```json
{
  "data": {
    "id": "link-xyz789",
    "url": "https://app.kapso.ai/whatsapp/setup/aBcD123...",
    "expires_at": "2024-03-15T10:00:00Z"
  }
}
```

Share the `url` with your customer. They'll click it, log in with Facebook, and connect their WhatsApp in ~5 minutes.

## Step 3: Send messages

After setup completes, use the customer's `phone_number_id` to send messages:

```bash
curl -X POST https://api.kapso.ai/meta/whatsapp/v24.0/110987654321/messages \
  -H "X-API-Key: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "messaging_product": "whatsapp",
    "to": "15551234567",
    "type": "text",
    "text": {
      "body": "Your order has been shipped!"
    }
  }'
```

## JavaScript example

```javascript
const KAPSO_API_KEY = 'YOUR_API_KEY';
const KAPSO_API_BASE_URL = 'https://api.kapso.ai';
const PLATFORM_API_URL = `${KAPSO_API_BASE_URL}/platform/v1`;
const WHATSAPP_API_URL = `${KAPSO_API_BASE_URL}/meta/whatsapp`;

async function onboardCustomer(customerData) {
  // 1. Create customer
  const customer = await fetch(`${PLATFORM_API_URL}/customers`, {
    method: 'POST',
    headers: {
      'X-API-Key': KAPSO_API_KEY,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ customer: customerData })
  }).then(r => r.json());

  // 2. Generate setup link
  const setupLink = await fetch(
    `${PLATFORM_API_URL}/customers/${customer.data.id}/setup_links`,
    {
      method: 'POST',
      headers: {
        'X-API-Key': KAPSO_API_KEY,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ setup_link: {} })
    }
  ).then(r => r.json());

  return setupLink.data.url;
}

async function sendMessage(phoneNumberId, recipientPhone, message) {
  return fetch(`${WHATSAPP_API_URL}/v24.0/${phoneNumberId}/messages`, {
    method: 'POST',
    headers: {
      'X-API-Key': KAPSO_API_KEY,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      messaging_product: 'whatsapp',
      to: recipientPhone,
      type: 'text',
      text: { body: message }
    })
  });
}
```

## What customers see

1. Click your setup link
2. Log in with Facebook
3. Connect their WhatsApp Business
4. Verify phone number
5. Done - you can now send messages

The entire process takes ~5 minutes.

## Next steps

- [Setup links](/brain/knowledge/docs_legacy/platform/setup-links) - Customize redirect URLs, branding, connection types
- [Connection detection](/brain/knowledge/docs_legacy/platform/detecting-whatsapp-connection) - Know when customers connect
- [Webhooks](/brain/knowledge/docs_legacy/platform/webhooks/overview) - Handle real-time message events
```

## File: `skills/integrate-whatsapp/references/platform-api-reference.md`
```markdown
# Kapso Platform API Overview

## Authentication

All Platform API requests require:

```
X-API-Key: <api_key>
```

Base host: `https://api.kapso.ai`
Platform API base path: `/platform/v1`

## Meta proxy (WhatsApp Cloud API)

Base URL: `https://api.kapso.ai/meta/whatsapp/v24.0`

Use Meta proxy for WhatsApp Cloud API calls (messages, templates, media, flows). Auth still uses `X-API-Key`.

## Multi-tenant WhatsApp (Customers)

Use Customers when your end-users connect their own WhatsApp numbers.

Flow:
1. Create customer
2. Create setup link
3. Customer completes embedded signup
4. Use their phone_number_id for sending

Endpoints:
- `POST /customers`
- `GET /customers`
- `GET /customers/:id`
- `POST /customers/:customer_id/setup_links`
- `POST /customers/:customer_id/whatsapp/phone_numbers`
- `GET /whatsapp/phone_numbers?customer_id=<uuid>` (filter phone numbers by customer)

If you are only sending from your own WhatsApp number, skip Customers.

## Core Platform API endpoints

Webhooks:
- Project-level: `GET/POST /whatsapp/webhooks`
- Config-level: `GET/POST /whatsapp/phone_numbers/:id/webhooks`
- Test delivery: `POST /whatsapp/webhooks/:id/test`

Messages and conversations:
- `GET /whatsapp/messages`
- `GET /whatsapp/messages/:id` (WAMID)
- `GET /whatsapp/conversations`
- `GET /whatsapp/conversations/:id`

Message list query params (use `GET /whatsapp/messages`):
- `phone_number_id`, `conversation_id`, `phone_number`
- `direction` (inbound|outbound), `status` (pending|sent|delivered|read|failed)
- `message_type` (text|image|audio|video|document), `has_media` (true|false)
- `page`, `per_page`

Example:
`GET /whatsapp/messages?conversation_id=<uuid>&phone_number_id=<id>&direction=inbound&per_page=50`

Conversation list query params (use `GET /whatsapp/conversations`):
- `phone_number_id`, `phone_number`
- `status` (active|ended)
- `page`, `per_page`

Example:
`GET /whatsapp/conversations?phone_number_id=<id>&status=active&per_page=50`

Workflows:
- `GET /workflows`
- `POST /workflows`
- `GET /workflows/:id`
- `GET /workflows/:id/definition`
- `PATCH /workflows/:id`
- `GET /workflows/:id/variables`
- `GET /workflows/:workflow_id/executions`
- `POST /workflows/:workflow_id/executions`
- `GET /workflow_executions/:id`
- `PATCH /workflow_executions/:id`
- `POST /workflow_executions/:id/resume`
- `GET /workflows/:workflow_id/triggers`
- `POST /workflows/:workflow_id/triggers`
- `PATCH /triggers/:id`
- `DELETE /triggers/:id`

Functions:
- `GET /functions`
- `POST /functions`
- `GET /functions/:id`
- `PATCH /functions/:id`
- `POST /functions/:id/deploy`
- `POST /functions/:id/invoke`
- `GET /functions/:id/invocations`

Integrations:
- `GET /integrations`
- `POST /integrations`
- `PATCH /integrations/:id`
- `DELETE /integrations/:id`
- `GET /integrations/apps`
- `GET /integrations/actions`
- `GET /integrations/accounts`
- `POST /integrations/connect_token`
- `GET /integrations/actions/:action_id/schema`
- `POST /integrations/actions/:action_id/configure_prop`
- `POST /integrations/actions/:action_id/reload_props`

Logs:
- `GET /api_logs`
- `GET /webhook_deliveries`

Provider models:
- `GET /provider_models`

## Guidance

- For template creation/sending, use the Meta proxy endpoints (see `integrate-whatsapp` skill).
- For WhatsApp Flows, use Platform API flow endpoints (see `integrate-whatsapp` skill).
- For workflow graph edits, use workflow definition endpoints (see `automate-whatsapp` skill).
```

## File: `skills/integrate-whatsapp/references/setup-links.md`
```markdown
---
title: Setup links
description: Customize the WhatsApp onboarding experience
---

Setup links let customers connect their WhatsApp Business accounts to your platform. Send a link, customer clicks, logs in with Facebook, and you're connected.

## Quick start

Create a basic setup link:

```bash
curl -X POST https://api.kapso.ai/platform/v1/customers/{customer_id}/setup_links \
  -H "X-API-Key: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "setup_link": {
      "success_redirect_url": "https://your-app.com/whatsapp/success",
      "failure_redirect_url": "https://your-app.com/whatsapp/failed"
    }
  }'
```

Response includes a `url` you send to your customer. Links expire after 30 days.

See [Connection detection](/brain/knowledge/docs_legacy/platform/detecting-whatsapp-connection) for handling successful connections.

## Connection types

Customers can connect their WhatsApp in two ways:

**Coexistence** - Keep using WhatsApp Business app alongside API
- 5 messages/second
- App stays active
- Good for small businesses

**Dedicated** - API-only access for automation
- Up to 1000 messages/second
- No app access
- Built for scale

## Redirect URLs

Configure where customers land after completing or failing setup:

```json
{
  "setup_link": {
    "success_redirect_url": "https://your-app.com/whatsapp/success",
    "failure_redirect_url": "https://your-app.com/whatsapp/failed"
  }
}
```

Both URLs receive query parameters with setup details. See [Connection detection](/brain/knowledge/docs_legacy/platform/detecting-whatsapp-connection) for handling redirects and available parameters.

## Language

Set the setup page language instead of auto-detecting from browser:

```json
{
  "setup_link": {
    "language": "es"
  }
}
```

Supported languages:
- `en` - English
- `es` - Spanish
- `pt` - Portuguese
- `hi` - Hindi
- `id` - Indonesian
- `ar` - Arabic

When omitted, language is auto-detected from the customer's browser.

## Recommended Kapso default

For Kapso-managed onboarding, prefer a dedicated connection plus phone provisioning:

```json
{
  "setup_link": {
    "allowed_connection_types": ["dedicated"],
    "provision_phone_number": true,
    "phone_number_country_isos": ["US"]
  }
}
```

`kapso setup` and `kapso whatsapp numbers new` follow this default path and let you override country, area code, language, and redirect URLs when needed.

## Connection type control

### Show both options (default)
```json
{
  "setup_link": {
    "allowed_connection_types": ["coexistence", "dedicated"]
  }
}
```

### Coexistence only
For customers using WhatsApp Business app:
```json
{
  "setup_link": {
    "allowed_connection_types": ["coexistence"]
  }
}
```

### Dedicated only
For API-only automation:
```json
{
  "setup_link": {
    "allowed_connection_types": ["dedicated"]
  }
}
```

When you provide one option, it auto-selects.

## Theme customization

Match your brand colors:

```json
{
  "setup_link": {
    "theme_config": {
      "primary_color": "#3b82f6",
      "background_color": "#ffffff",
      "text_color": "#1f2937",
      "muted_text_color": "#64748b",
      "card_color": "#f9fafb",
      "border_color": "#e5e7eb"
    }
  }
}
```

All colors use hex format (#RRGGBB).

## Phone number provisioning

Automatically provision a phone number for customers:

```json
{
  "setup_link": {
    "provision_phone_number": true,
    "phone_number_country_isos": ["US"]
  }
}
```

### Country support

- Default: `["US"]` - US phone numbers only
- Non-US countries require custom Twilio credentials (contact sales)

```json
{
  "setup_link": {
    "provision_phone_number": true,
    "phone_number_country_isos": ["US", "CL"]
  }
}
```

## Full example

```javascript
const KAPSO_API_BASE_URL = 'https://api.kapso.ai';
const setupLink = await fetch(
  `${KAPSO_API_BASE_URL}/platform/v1/customers/${customerId}/setup_links`,
  {
    method: 'POST',
    headers: {
      'X-API-Key': 'YOUR_API_KEY',
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      setup_link: {
        language: 'es',
        success_redirect_url: 'https://app.example.com/onboarding/complete',
        failure_redirect_url: 'https://app.example.com/onboarding/error',
        allowed_connection_types: ['dedicated'],
        provision_phone_number: true,
        phone_number_country_isos: ['US'],
        theme_config: {
          primary_color: '#10b981',
          background_color: '#ffffff',
          text_color: '#111827'
        }
      }
    })
  }
);

// Send link to customer
await sendEmail(customer.email, {
  subject: 'Connect your WhatsApp',
  body: `Click here to connect: ${setupLink.data.url}`
});
```

## Link management

### List all links
```bash
curl https://api.kapso.ai/platform/v1/customers/{customer_id}/setup_links \
  -H "X-API-Key: YOUR_API_KEY"
```

### Automatic revocation
Creating a new link revokes the previous one. Only one active link per customer.

### Expiration
Links expire after 30 days. Check the `expires_at` field.
```

## File: `skills/integrate-whatsapp/references/templates-reference.md`
```markdown
# WhatsApp Templates via Meta Proxy

## Environment

Required env vars:

- `KAPSO_API_BASE_URL` (host only, no `/platform/v1`, e.g. `https://api.kapso.ai`)
- `KAPSO_API_KEY`
- `META_GRAPH_VERSION` (optional, default: `v24.0`)
- `KAPSO_META_BASE_URL` (optional, defaults to `${KAPSO_API_BASE_URL}/meta/whatsapp`)

## Discover IDs (recommended)

Template CRUD requires `business_account_id` (WABA ID). Sending messages and uploading media require `phone_number_id` (Meta phone number id).

Use the Platform API to discover both:

- Script: `node scripts/list-platform-phone-numbers.mjs`
- Raw: `GET /platform/v1/whatsapp/phone_numbers` (header: `X-API-Key: $KAPSO_API_KEY`)

## Meta proxy endpoints used

- List WABA phone numbers:
  - `GET /{business_account_id}/phone_numbers`
- List templates:
  - `GET /{business_account_id}/message_templates`
- Create template:
  - `POST /{business_account_id}/message_templates`
- Update template:
  - `POST /{business_account_id}/message_templates?hsm_id=<template_id>`
- Delete template (not scripted):
  - `DELETE /{business_account_id}/message_templates?name=<template_name>`
- Send template message:
  - `POST /{phone_number_id}/messages`
- Upload media for send-time headers:
  - `POST /{phone_number_id}/media`

## Template concepts

Categories:
- MARKETING: promotional content.
- UTILITY: transactional updates.
- AUTHENTICATION: OTP/verification (special rules below).

AUTHENTICATION templates:
- Require Meta business verification.
- Body text is fixed by Meta (not customizable).
- Must include an OTP button (COPY_CODE or ONE_TAP).
- Send-time still requires the OTP value in body param {{1}} and URL button param.
- If user wants custom OTP text, use UTILITY instead.

Status flow:
- Kapso does not maintain a separate draft state; create/update calls go to Meta immediately.
- Use `status` from Meta (`APPROVED`, `PENDING`, `REJECTED`, etc) via list/status scripts.

Parameter types:
- POSITIONAL: `{{1}}`, `{{2}}` (sequential).
- NAMED: `{{customer_name}}` (lowercase + underscores). Prefer NAMED.

Component types:
- HEADER (optional)
- BODY (required)
- FOOTER (optional)
- BUTTONS (optional)

## Parameter format (creation time)

Set `parameter_format`:
- `POSITIONAL` (default): `{{1}}`, `{{2}}` with no gaps.
- `NAMED` (recommended): `{{order_id}}`.

## Example requirements (creation time)

If any variables appear in HEADER or BODY, you must include examples:
- POSITIONAL: `example.header_text` and 2D `example.body_text`.
- NAMED: `example.header_text_named_params` and `example.body_text_named_params`.

## Components cheat sheet (creation time)

### Header (TEXT, named)

```json
{
  "type": "HEADER",
  "format": "TEXT",
  "text": "Sale starts {{sale_date}}",
  "example": {
    "header_text_named_params": [
      { "param_name": "sale_date", "example": "December 1" }
    ]
  }
}
```

### Header (TEXT, positional)

```json
{
  "type": "HEADER",
  "format": "TEXT",
  "text": "Sale starts {{1}}",
  "example": {
    "header_text": ["December 1"]
  }
}
```

### Header (IMAGE/VIDEO/DOCUMENT)

```json
{
  "type": "HEADER",
  "format": "IMAGE",
  "example": {
    "header_handle": ["<header_handle>"]
  }
}
```

### Body (named)

```json
{
  "type": "BODY",
  "text": "Hi {{customer_name}}, order {{order_id}} is ready.",
  "example": {
    "body_text_named_params": [
      { "param_name": "customer_name", "example": "Alex" },
      { "param_name": "order_id", "example": "ORDER-123" }
    ]
  }
}
```

### Body (positional)

```json
{
  "type": "BODY",
  "text": "Order {{1}} is ready for {{2}}.",
  "example": {
    "body_text": [["ORDER-123", "Alex"]]
  }
}
```

### Footer (no variables)

```json
{
  "type": "FOOTER",
  "text": "Reply STOP to opt out"
}
```

### Buttons

```json
{
  "type": "BUTTONS",
  "buttons": [
    { "type": "QUICK_REPLY", "text": "Need help" },
    { "type": "URL", "text": "Track", "url": "https://example.com/track?id={{1}}", "example": ["https://example.com/track?id=ORDER-123"] }
  ]
}
```

Button ordering rules:
- Do not interleave QUICK_REPLY with URL/PHONE_NUMBER.
- Valid: QUICK_REPLY, QUICK_REPLY, URL, PHONE_NUMBER
- Invalid: QUICK_REPLY, URL, QUICK_REPLY
- Dynamic URL variables must be at the end of the URL.

URL button variables use positional placeholders in the URL (for example `{{1}}`). At send-time, include a `button` component with `sub_type: "url"` and the correct `index`.

Example (send-time URL button param):

```json
{
  "type": "button",
  "sub_type": "url",
  "index": "0",
  "parameters": [{ "type": "text", "text": "ORDER-123" }]
}
```

## AUTHENTICATION components

```json
{
  "type": "BODY",
  "add_security_recommendation": true,
  "code_expiration_minutes": 10
}
```

```json
{
  "type": "BUTTONS",
  "buttons": [
    { "type": "OTP", "otp_type": "COPY_CODE", "text": "Copy code" }
  ]
}
```

## Send-time components

Named parameters:

```json
{
  "type": "body",
  "parameters": [
    { "type": "text", "parameter_name": "order_id", "text": "ORDER-123" }
  ]
}
```

Positional parameters:

```json
{
  "type": "body",
  "parameters": [
    { "type": "text", "text": "ORDER-123" }
  ]
}
```

AUTHENTICATION send-time:

```json
[
  {
    "type": "body",
    "parameters": [{ "type": "text", "text": "123456" }]
  },
  {
    "type": "button",
    "sub_type": "url",
    "index": "0",
    "parameters": [{ "type": "text", "text": "123456" }]
  }
]
```

Media header send-time (use id or link, not both):

```json
{
  "type": "header",
  "parameters": [
    { "type": "image", "image": { "id": "4490709327384033" } }
  ]
}
```

## Header handle limitation

The Meta proxy does not expose resumable upload endpoints for `header_handle`. Use Platform media ingest (`/platform/v1/whatsapp/media` with `delivery: meta_resumable_asset`) if a header_handle is required.

```json
{
  "type": "header",
  "parameters": [
    { "type": "image", "image": { "link": "https://example.com/header.jpg" } }
  ]
}
```

Rules:

- Use either `id` or `link` (never both).
- Always include the header component when the template has a media header.
```

## File: `skills/integrate-whatsapp/references/webhooks-event-types.md`
```markdown
---
title: Event types
description: Available webhook events and their payloads
---

All webhook payloads use v2 format with `phone_number_id` at the top level.

## Payload structure

Webhook payloads separate message data from conversation data:

- **message.kapso** - Message-scoped only: direction, status, processing_status, statuses (raw status history), origin, has_media, content (text representation), transcript (for audio), media helpers (media_data, media_url, message_type_data)
- **conversation** - Top-level identifiers (id, phone_number, phone_number_id). Optional conversation.kapso contains summary metrics (counts, last-message metadata, timestamps)
- **phone_number_id** - Included at top level for routing

## Project webhook events

Use project webhooks for connection lifecycle and workflow events only.

### whatsapp.phone_number.created

Fires when a customer successfully connects their WhatsApp through a setup link.

See [Connection detection](/brain/knowledge/docs_legacy/platform/detecting-whatsapp-connection) for implementation guide.

**Payload**:

```json
{
  "phone_number_id": "123456789012345",
  "project": {
    "id": "990e8400-e29b-41d4-a716-446655440004"
  },
  "customer": {
    "id": "880e8400-e29b-41d4-a716-446655440003"
  }
}
```

### workflow.execution.handoff

Fires when a workflow execution is handed off to a human agent.

**Payload**:

```json
{
  "event": "workflow.execution.handoff",
  "occurred_at": "2025-12-08T12:00:00Z",
  "project_id": "990e8400-e29b-41d4-a716-446655440004",
  "workflow_id": "880e8400-e29b-41d4-a716-446655440001",
  "workflow_execution_id": "770e8400-e29b-41d4-a716-446655440002",
  "status": "handoff",
  "tracking_id": "track-abc123",
  "channel": "whatsapp",
  "whatsapp_conversation_id": "conv_789",
  "handoff": {
    "reason": "User requested human assistance",
    "source": "agent_tool"
  }
}
```

| Field | Description |
|-------|-------------|
| `handoff.reason` | Optional reason provided during handoff |
| `handoff.source` | `agent_tool` (from agent step) or `action_step` (from workflow action) |

### workflow.execution.failed

Fires when a workflow execution fails due to an error.

**Payload**:

```json
{
  "event": "workflow.execution.failed",
  "occurred_at": "2025-12-08T12:00:00Z",
  "project_id": "990e8400-e29b-41d4-a716-446655440004",
  "workflow_id": "880e8400-e29b-41d4-a716-446655440001",
  "workflow_execution_id": "770e8400-e29b-41d4-a716-446655440002",
  "status": "failed",
  "tracking_id": "track-abc123",
  "channel": "whatsapp",
  "whatsapp_conversation_id": "conv_789",
  "error": {
    "message": "Workflow execution timed out"
  }
}
```

## WhatsApp webhook events
Use phone-number webhooks for `whatsapp.message.*` and `whatsapp.conversation.*` events only.

<CardGroup cols={2}>
  <Card title="Message received" icon="message">
    `whatsapp.message.received`

    Fired when a new WhatsApp message is received from a customer. Supports message buffering for batch delivery.
  </Card>
  <Card title="Message sent" icon="paper-plane">
    `whatsapp.message.sent`

    Fired when a message is successfully sent to WhatsApp
  </Card>
  <Card title="Message delivered" icon="check">
    `whatsapp.message.delivered`

    Fired when a message is successfully delivered to the recipient's device
  </Card>
  <Card title="Message read" icon="eye">
    `whatsapp.message.read`

    Fired when the recipient reads your message
  </Card>
  <Card title="Message failed" icon="triangle-exclamation">
    `whatsapp.message.failed`

    Fired when a message fails to deliver
  </Card>
  <Card title="Conversation created" icon="comments">
    `whatsapp.conversation.created`

    Fired when a new WhatsApp conversation is initiated
  </Card>
  <Card title="Conversation ended" icon="clock">
    `whatsapp.conversation.ended`

    Fired when a WhatsApp conversation ends (agent action, manual closure, or 24-hour inactivity)
  </Card>
  <Card title="Conversation inactive" icon="timer">
    `whatsapp.conversation.inactive`

    Fired when no messages (inbound/outbound) for configured minutes (1-1440, default 60)
  </Card>
</CardGroup>

## Payload structures

### whatsapp.message.received

```json
{
  "message": {
    "id": "wamid.123",
    "timestamp": "1730092800",
    "type": "text",
    "text": { "body": "Hello" },
    "kapso": {
      "direction": "inbound",
      "status": "received",
      "processing_status": "pending",
      "origin": "cloud_api",
      "has_media": false,
      "content": "Hello"
    }
  },
  "conversation": {
    "id": "conv_123",
    "phone_number": "+15551234567",
    "status": "active",
    "last_active_at": "2025-10-28T14:25:01Z",
    "created_at": "2025-10-28T13:40:00Z",
    "updated_at": "2025-10-28T14:25:01Z",
    "metadata": {},
    "phone_number_id": "123456789012345",
    "kapso": {
      "contact_name": "John Doe",
      "messages_count": 1,
      "last_message_id": "wamid.123",
      "last_message_type": "text",
      "last_message_timestamp": "2025-10-28T14:25:01Z",
      "last_message_text": "Hello",
      "last_inbound_at": "2025-10-28T14:25:01Z",
      "last_outbound_at": null
    }
  },
  "is_new_conversation": true,
  "phone_number_id": "123456789012345"
}
```

### whatsapp.message.sent

```json
{
  "message": {
    "id": "wamid.456",
    "timestamp": "1730092860",
    "type": "text",
    "text": { "body": "On my way" },
    "kapso": {
      "direction": "outbound",
      "status": "sent",
      "processing_status": "completed",
      "origin": "cloud_api",
      "has_media": false,
      "statuses": [
        {
          "id": "wamid.456",
          "status": "sent",
          "timestamp": "1730092860",
          "recipient_id": "15551234567"
        }
      ]
    }
  },
  "conversation": {
    "id": "conv_123",
    "phone_number": "+15551234567",
    "status": "active",
    "last_active_at": "2025-10-28T14:31:00Z",
    "created_at": "2025-10-28T13:40:00Z",
    "updated_at": "2025-10-28T14:31:00Z",
    "metadata": {},
    "phone_number_id": "123456789012345",
    "kapso": {
      "contact_name": "John Doe",
      "messages_count": 2,
      "last_message_id": "wamid.456",
      "last_message_type": "text",
      "last_message_timestamp": "2025-10-28T14:31:00Z",
      "last_message_text": "On my way",
      "last_inbound_at": "2025-10-28T14:25:01Z",
      "last_outbound_at": "2025-10-28T14:31:00Z"
    }
  },
  "is_new_conversation": false,
  "phone_number_id": "123456789012345"
}
```

### whatsapp.message.delivered

```json
{
  "message": {
    "id": "wamid.456",
    "timestamp": "1730092888",
    "type": "text",
    "text": { "body": "On my way" },
    "kapso": {
      "direction": "outbound",
      "status": "delivered",
      "processing_status": "completed",
      "origin": "cloud_api",
      "has_media": false,
      "statuses": [
        {
          "id": "wamid.456",
          "status": "sent",
          "timestamp": "1730092860",
          "recipient_id": "15551234567"
        },
        {
          "id": "wamid.456",
          "status": "delivered",
          "timestamp": "1730092888",
          "recipient_id": "15551234567"
        }
      ]
    }
  },
  "conversation": {
    "id": "conv_123",
    "phone_number": "+15551234567",
    "status": "active",
    "last_active_at": "2025-10-28T14:31:28Z",
    "created_at": "2025-10-28T13:40:00Z",
    "updated_at": "2025-10-28T14:31:28Z",
    "metadata": {},
    "phone_number_id": "123456789012345"
  },
  "is_new_conversation": false,
  "phone_number_id": "123456789012345"
}
```

### whatsapp.message.failed

```json
{
  "message": {
    "id": "wamid.789",
    "timestamp": "1730093200",
    "type": "text",
    "text": { "body": "This message failed" },
    "kapso": {
      "direction": "outbound",
      "status": "failed",
      "processing_status": "completed",
      "origin": "cloud_api",
      "has_media": false,
      "statuses": [
        {
          "id": "wamid.789",
          "status": "sent",
          "timestamp": "1730093100",
          "recipient_id": "15551234567"
        },
        {
          "id": "wamid.789",
          "status": "failed",
          "timestamp": "1730093200",
          "recipient_id": "15551234567",
          "errors": [
            {
              "code": 131047,
              "title": "Re-engagement message",
              "message": "More than 24 hours have passed since the recipient last replied"
            }
          ]
        }
      ]
    }
  },
  "conversation": {
    "id": "conv_123",
    "phone_number": "+15551234567",
    "status": "active",
    "last_active_at": "2025-10-28T15:00:00Z",
    "created_at": "2025-10-28T13:40:00Z",
    "updated_at": "2025-10-28T15:00:00Z",
    "metadata": {},
    "phone_number_id": "123456789012345"
  },
  "is_new_conversation": false,
  "phone_number_id": "123456789012345"
}
```

### whatsapp.conversation.created

```json
{
  "conversation": {
    "id": "conv_789",
    "phone_number": "+15551234567",
    "status": "active",
    "last_active_at": "2025-10-28T14:00:00Z",
    "created_at": "2025-10-28T14:00:00Z",
    "updated_at": "2025-10-28T14:00:00Z",
    "metadata": {},
    "phone_number_id": "123456789012345",
    "kapso": {
      "contact_name": "John Doe",
      "messages_count": 0,
      "last_message_id": null,
      "last_message_type": null,
      "last_message_timestamp": null,
      "last_message_text": null,
      "last_inbound_at": null,
      "last_outbound_at": null
    }
  },
  "phone_number_id": "123456789012345"
}
```

### whatsapp.conversation.ended

```json
{
  "conversation": {
    "id": "conv_789",
    "phone_number": "+15551234567",
    "status": "ended",
    "last_active_at": "2025-10-28T15:10:45Z",
    "created_at": "2025-10-28T14:00:00Z",
    "updated_at": "2025-10-28T15:10:45Z",
    "metadata": {},
    "phone_number_id": "123456789012345",
    "kapso": {
      "contact_name": "John Doe",
      "messages_count": 15,
      "last_message_id": "wamid.999",
      "last_message_type": "text",
      "last_message_timestamp": "2025-10-28T15:10:45Z",
      "last_message_text": "Thanks!",
      "last_inbound_at": "2025-10-28T15:10:45Z",
      "last_outbound_at": "2025-10-28T15:10:30Z"
    }
  },
  "phone_number_id": "123456789012345"
}
```

### whatsapp.conversation.inactive

```json
{
  "conversation": {
    "id": "conv_789",
    "phone_number": "+15551234567",
    "status": "active",
    "last_active_at": "2025-10-28T13:00:00Z",
    "created_at": "2025-10-28T12:00:00Z",
    "updated_at": "2025-10-28T13:00:00Z",
    "metadata": {},
    "phone_number_id": "123456789012345"
  },
  "since_message": {
    "id": "msg_anchor",
    "whatsapp_message_id": "wamid.ANCHOR",
    "direction": "inbound",
    "created_at": "2025-10-28T13:00:00Z"
  },
  "inactivity": {
    "minutes": 60
  },
  "phone_number_id": "123456789012345"
}
```

### Multiple inactivity timeouts

Create separate webhooks for different timeout thresholds:

```json
// First webhook: 5 minute warning
{
  "events": ["whatsapp.conversation.inactive"],
  "inactive_after_minutes": 5
}

// Second webhook: 30 minute escalation
{
  "events": ["whatsapp.conversation.inactive"],
  "inactive_after_minutes": 30
}
```

Each webhook fires independently when its threshold is reached.

## Message origin

The `message.kapso.origin` field indicates how the message entered the system:

- **cloud_api** - Sent via Kapso API (outbound jobs, flow actions, API calls)
- **business_app** - Echoed from WhatsApp Business App (when using the Business App)
- **history_sync** - Backfilled during message history imports (only if project ran sync)

## Status history

The `message.kapso.statuses` array contains the complete history of raw Meta status events for a message, ordered chronologically. Each entry is the unmodified payload from Meta's webhook.

### Status object structure

Each status object in the array follows Meta's webhook format:

```json
{
  "id": "<WHATSAPP_MESSAGE_ID>",
  "status": "<STATUS>",
  "timestamp": "<UNIX_TIMESTAMP>",
  "recipient_id": "<PHONE_NUMBER>",
  "pricing": {
    "billable": true,
    "pricing_model": "<PRICING_MODEL>",
    "category": "<PRICING_CATEGORY>"
  },
  "errors": [
    {
      "code": 131031,
      "title": "<ERROR_TITLE>",
      "message": "<ERROR_MESSAGE>",
      "error_data": {
        "details": "<ERROR_DETAILS>"
      },
      "href": "<ERROR_CODES_URL>"
    }
  ],
  ...
}
```

| Field | Included when |
|-------|---------------|
| `pricing` | Sent status, plus delivered or read |
| `errors` | Failed to send or deliver |

See [Meta's status webhook reference](https://developers.facebook.com/brain/knowledge/docs_legacy/whatsapp/cloud-api/webhooks/components#statuses-object) for the complete schema.

Use this field to track the full lifecycle of outbound messages and understand failure causes. The array only appears when status events have been recorded.

## Message types

The `message.type` field can be one of:

- `text` - Plain text message
- `image` - Image attachment
- `video` - Video attachment
- `audio` - Audio/voice message
- `document` - Document attachment
- `location` - Location sharing
- `template` - WhatsApp template message
- `interactive` - Interactive message (buttons, lists)
- `reaction` - Message reaction
- `contacts` - Contact card sharing

## Message type-specific data

### Media messages (image/video/document)

```json
{
  "message": {
    "id": "wamid.789",
    "timestamp": "1730093000",
    "type": "image",
    "image": {
      "caption": "Photo description",
      "id": "media_id_123"
    },
    "kapso": {
      "direction": "inbound",
      "status": "received",
      "processing_status": "pending",
      "origin": "cloud_api",
      "has_media": true,
      "content": "Photo description Image attached (photo.jpg) [Size: 200 KB | Type: image/jpeg] URL: https://api.kapso.ai/media/...",
      "media_url": "https://api.kapso.ai/media/...",
      "media_data": {
        "url": "https://api.kapso.ai/media/...",
        "filename": "photo.jpg",
        "content_type": "image/jpeg",
        "byte_size": 204800
      },
      "message_type_data": {
        "caption": "Photo description"
      }
    }
  }
}
```

### Audio messages

```json
{
  "message": {
    "id": "wamid.790",
    "timestamp": "1730093100",
    "type": "audio",
    "audio": {
      "id": "media_id_456"
    },
    "kapso": {
      "direction": "inbound",
      "status": "received",
      "processing_status": "pending",
      "origin": "cloud_api",
      "has_media": true,
      "content": "[Audio attached] (voice.ogg) [Size: 50 KB | Type: audio/ogg] URL: https://api.kapso.ai/media/...\nTranscript: Hello, I need help with my order",
      "transcript": {
        "text": "Hello, I need help with my order"
      },
      "media_url": "https://api.kapso.ai/media/...",
      "media_data": {
        "url": "https://api.kapso.ai/media/...",
        "filename": "voice.ogg",
        "content_type": "audio/ogg",
        "byte_size": 51200
      }
    }
  }
}
```

### Location messages

```json
{
  "message": {
    "type": "location",
    "location": {
      "latitude": 37.7749,
      "longitude": -122.4194,
      "name": "San Francisco",
      "address": "San Francisco, CA, USA"
    }
  }
}
```

### Template messages

```json
{
  "message": {
    "type": "template",
    "template": {
      "name": "order_confirmation",
      "language": {
        "code": "en_US"
      },
      "components": [...]
    }
  }
}
```

### Interactive messages

```json
{
  "message": {
    "type": "interactive",
    "interactive": {
      "type": "button_reply",
      "button_reply": {
        "id": "btn_1",
        "title": "Confirm"
      }
    }
  }
}
```

### Reaction messages

```json
{
  "message": {
    "type": "reaction",
    "reaction": {
      "message_id": "wamid.HBgNNTU0MTIzNDU2Nzg5MA",
      "emoji": "👍"
    }
  }
}
```
```

## File: `skills/integrate-whatsapp/references/webhooks-overview.md`
```markdown
---
title: Webhooks Overview (Kapso)
---

# Webhooks Overview

## Webhook types

### Project webhooks
Project-wide events (for example, `whatsapp.phone_number.created`).
Use **project webhooks** for connection lifecycle and workflow events only.

### WhatsApp webhooks
Message and conversation events for a specific `phone_number_id`.
Use **phone-number webhooks** for `whatsapp.message.*` and `whatsapp.conversation.*` events only.
WhatsApp message events cannot be delivered via project webhooks.

Kinds:

- **Kapso webhooks** (default): event-based payloads, filtering, buffering.
- **Meta webhooks**: raw Meta payloads, no filtering or buffering. One meta webhook per phone number.

Meta webhooks include `X-Idempotency-Key` (SHA256 hash of payload) for deduplication.

## Response requirements

- Your endpoint must return `200 OK` within 10 seconds.
- Non-200 responses trigger retries.

Retry schedule (Kapso webhooks):
- 10 seconds
- 40 seconds
- 90 seconds

## Signature verification

Kapso signs webhook requests:

- Header: `X-Webhook-Signature`
- Value: `HMAC-SHA256(webhook_secret_key, raw_request_body)` as hex

Verify against raw request bytes before parsing JSON.

## Headers (Kapso webhooks)

- `X-Webhook-Event`
- `X-Webhook-Signature`
- `X-Idempotency-Key`
- `X-Webhook-Payload-Version`
- `Content-Type: application/json`

Batched payloads may include:

- `X-Webhook-Batch: true`
- `X-Batch-Size: <n>`
```

## File: `skills/integrate-whatsapp/references/webhooks-reference.md`
```markdown
# Webhook Reference

## Scopes

- Config-level: attach to a specific WhatsApp phone number (use `phone_number_id`).
- Project-level: receive lifecycle/workflow events across all numbers.
- Use config-level for any `whatsapp.message.*` and `whatsapp.conversation.*` events.
- WhatsApp message/conversation events are **not** delivered via project webhooks.

## Signature verification

Kapso signs outbound webhook requests:

- Header: `X-Webhook-Signature`
- Value: `HMAC-SHA256(webhook_secret_key, raw_request_body)` as hex

Verify against the raw request body bytes before JSON parsing.

## Event catalog

Message events (config-level):

- `whatsapp.message.received`
- `whatsapp.message.sent`
- `whatsapp.message.delivered`
- `whatsapp.message.read`
- `whatsapp.message.failed`

Conversation events:

- `whatsapp.conversation.created`
- `whatsapp.conversation.ended`
- `whatsapp.conversation.inactive`

Lifecycle events (project-level only):

- `whatsapp.config.created`
- `whatsapp.phone_number.created`
- `whatsapp.phone_number.deleted`

Workflow events:

- `workflow.execution.handoff`
- `workflow.execution.failed`

## Payload versions

- `v1`: legacy payloads with nested `whatsapp_config`.
- `v2`: modern payloads with `phone_number_id` at root (recommended).

## Buffering (message.received)

Use buffering to batch rapid inbound messages:

- `buffer_enabled`: true
- `buffer_window_seconds`: 1-60
- `max_buffer_size`: 1-100
```

## File: `skills/integrate-whatsapp/references/whatsapp-api-reference.md`
```markdown
---
title: WhatsApp Cloud API via Kapso Proxy
---

# WhatsApp Cloud API (Kapso Meta Proxy)

REST API reference for sending messages, managing templates, and querying history via Kapso's Meta proxy.

## Base URL and auth

```
Base URL: ${KAPSO_API_BASE_URL}/meta/whatsapp/v24.0
Auth header: X-API-Key: <api_key>
```

All payloads mirror the Meta Cloud API. Kapso adds storage and query features.

## Send messages

`POST /{phone_number_id}/messages`

All payloads require `messaging_product: "whatsapp"`.

### Text

```json
{
  "messaging_product": "whatsapp",
  "to": "15551234567",
  "type": "text",
  "text": { "body": "Hello!", "preview_url": true }
}
```

### Image

```json
{
  "messaging_product": "whatsapp",
  "to": "15551234567",
  "type": "image",
  "image": { "link": "https://example.com/photo.jpg", "caption": "Photo" }
}
```

Use `id` instead of `link` for uploaded media.

### Video

```json
{
  "messaging_product": "whatsapp",
  "to": "15551234567",
  "type": "video",
  "video": { "link": "https://example.com/clip.mp4", "caption": "Video" }
}
```

### Audio

```json
{
  "messaging_product": "whatsapp",
  "to": "15551234567",
  "type": "audio",
  "audio": { "link": "https://example.com/audio.mp3" }
}
```

### Voice message

Voice messages require `.ogg` files with OPUS codec. Set `voice: true`:

```json
{
  "messaging_product": "whatsapp",
  "to": "15551234567",
  "type": "audio",
  "audio": { "id": "<MEDIA_ID>", "voice": true }
}
```

### Document

```json
{
  "messaging_product": "whatsapp",
  "to": "15551234567",
  "type": "document",
  "document": { "link": "https://example.com/file.pdf", "filename": "report.pdf", "caption": "Report" }
}
```

### Sticker

```json
{
  "messaging_product": "whatsapp",
  "to": "15551234567",
  "type": "sticker",
  "sticker": { "id": "<MEDIA_ID>" }
}
```

### Location

```json
{
  "messaging_product": "whatsapp",
  "to": "15551234567",
  "type": "location",
  "location": { "latitude": 37.7749, "longitude": -122.4194, "name": "SF Office", "address": "123 Main St" }
}
```

### Contacts

```json
{
  "messaging_product": "whatsapp",
  "to": "15551234567",
  "type": "contacts",
  "contacts": [{
    "name": { "formatted_name": "John Doe", "first_name": "John", "last_name": "Doe" },
    "phones": [{ "phone": "+15551234567", "type": "MOBILE", "wa_id": "15551234567" }],
    "emails": [{ "email": "john@example.com", "type": "WORK" }]
  }]
}
```

### Reaction

```json
{
  "messaging_product": "whatsapp",
  "to": "15551234567",
  "type": "reaction",
  "reaction": { "message_id": "wamid......", "emoji": "👍" }
}
```

Note: Reactions only trigger `sent` status webhook (not delivered/read).

### Reply to a message

Add `context` to reply to a specific message:

```json
{
  "messaging_product": "whatsapp",
  "to": "15551234567",
  "type": "text",
  "context": { "message_id": "wamid......" },
  "text": { "body": "Thanks for your message!" }
}
```

## Interactive messages

Require an active 24-hour session window. Use templates for outbound notifications outside the window.

### Buttons

```json
{
  "messaging_product": "whatsapp",
  "to": "15551234567",
  "type": "interactive",
  "interactive": {
    "type": "button",
    "body": { "text": "Choose an option" },
    "action": {
      "buttons": [
        { "type": "reply", "reply": { "id": "yes", "title": "Yes" } },
        { "type": "reply", "reply": { "id": "no", "title": "No" } }
      ]
    }
  }
}
```

Max 3 buttons. Button titles max 20 chars.

### List

```json
{
  "messaging_product": "whatsapp",
  "to": "15551234567",
  "type": "interactive",
  "interactive": {
    "type": "list",
    "header": { "type": "text", "text": "Shipping Options" },
    "body": { "text": "Choose your preferred shipping" },
    "footer": { "text": "Estimates may vary" },
    "action": {
      "button": "View Options",
      "sections": [{
        "title": "Fast",
        "rows": [
          { "id": "express", "title": "Express", "description": "1-2 days" },
          { "id": "priority", "title": "Priority", "description": "2-3 days" }
        ]
      }]
    }
  }
}
```

Max 10 sections, 10 rows total. Button text max 20 chars.

### CTA URL

```json
{
  "messaging_product": "whatsapp",
  "to": "15551234567",
  "type": "interactive",
  "interactive": {
    "type": "cta_url",
    "body": { "text": "Track your order" },
    "action": {
      "name": "cta_url",
      "parameters": { "display_text": "Track Order", "url": "https://example.com/track/123" }
    }
  }
}
```

### Location request

```json
{
  "messaging_product": "whatsapp",
  "to": "15551234567",
  "type": "interactive",
  "interactive": {
    "type": "location_request_message",
    "body": { "text": "Please share your location for delivery." },
    "action": { "name": "send_location" }
  }
}
```

### Flow

```json
{
  "messaging_product": "whatsapp",
  "to": "15551234567",
  "type": "interactive",
  "interactive": {
    "type": "flow",
    "header": { "type": "text", "text": "Book Appointment" },
    "body": { "text": "Schedule your visit" },
    "action": {
      "name": "flow",
      "parameters": {
        "flow_message_version": "3",
        "flow_id": "123456789",
        "flow_cta": "Book Now",
        "mode": "published",
        "flow_token": "session_abc123",
        "flow_action": "navigate",
        "flow_action_payload": {
          "screen": "WELCOME_SCREEN",
          "data": { "customer_id": "cust_123" }
        }
      }
    }
  }
}
```

### Product

```json
{
  "messaging_product": "whatsapp",
  "to": "15551234567",
  "type": "interactive",
  "interactive": {
    "type": "product",
    "body": { "text": "Check out this item" },
    "action": {
      "catalog_id": "CATALOG_ID",
      "product_retailer_id": "SKU_1234"
    }
  }
}
```

### Product list

```json
{
  "messaging_product": "whatsapp",
  "to": "15551234567",
  "type": "interactive",
  "interactive": {
    "type": "product_list",
    "header": { "type": "text", "text": "Our Bestsellers" },
    "body": { "text": "Choose a product" },
    "action": {
      "catalog_id": "CATALOG_ID",
      "sections": [{
        "title": "Popular",
        "product_items": [
          { "product_retailer_id": "SKU_1234" },
          { "product_retailer_id": "SKU_2345" }
        ]
      }]
    }
  }
}
```

Max 10 sections, 30 products total.

### Catalog message

```json
{
  "messaging_product": "whatsapp",
  "to": "15551234567",
  "type": "interactive",
  "interactive": {
    "type": "catalog_message",
    "body": { "text": "Browse our catalog." },
    "action": {
      "name": "catalog_message",
      "parameters": { "thumbnail_product_retailer_id": "SKU_THUMBNAIL" }
    }
  }
}
```

## Template messages

### Send with named parameters

```json
{
  "messaging_product": "whatsapp",
  "to": "15551234567",
  "type": "template",
  "template": {
    "name": "order_confirmation",
    "language": { "code": "en_US" },
    "components": [{
      "type": "body",
      "parameters": [
        { "type": "text", "parameter_name": "customer_name", "text": "Jessica" },
        { "type": "text", "parameter_name": "order_number", "text": "ORD-12345" }
      ]
    }]
  }
}
```

### Send with positional parameters

```json
{
  "messaging_product": "whatsapp",
  "to": "15551234567",
  "type": "template",
  "template": {
    "name": "order_confirmation",
    "language": { "code": "en_US" },
    "components": [{
      "type": "body",
      "parameters": [
        { "type": "text", "text": "Jessica" },
        { "type": "text", "text": "ORD-12345" }
      ]
    }]
  }
}
```

### Send with media header

```json
{
  "messaging_product": "whatsapp",
  "to": "15551234567",
  "type": "template",
  "template": {
    "name": "seasonal_promotion",
    "language": { "code": "en_US" },
    "components": [
      {
        "type": "header",
        "parameters": [{ "type": "image", "image": { "link": "https://example.com/promo.jpg" } }]
      },
      {
        "type": "body",
        "parameters": [
          { "type": "text", "parameter_name": "sale_name", "text": "Summer Sale" },
          { "type": "text", "parameter_name": "discount", "text": "25%" }
        ]
      }
    ]
  }
}
```

### Send with URL button variable

```json
{
  "messaging_product": "whatsapp",
  "to": "15551234567",
  "type": "template",
  "template": {
    "name": "order_tracking",
    "language": { "code": "en_US" },
    "components": [
      {
        "type": "body",
        "parameters": [{ "type": "text", "parameter_name": "order_id", "text": "ORD-123" }]
      },
      {
        "type": "button",
        "sub_type": "url",
        "index": "0",
        "parameters": [{ "type": "text", "text": "ORD-123" }]
      }
    ]
  }
}
```

See [templates-reference.md](templates-reference.md) for full component rules.

## Template CRUD

### List templates

`GET /{business_account_id}/message_templates`

| Param | Description |
|-------|-------------|
| `name` | Filter by template name |
| `status` | `APPROVED`, `PENDING`, `REJECTED` |
| `category` | `AUTHENTICATION`, `MARKETING`, `UTILITY` |
| `language` | Language code (e.g., `en_US`) |
| `limit` | Max 100 |

### Create template

`POST /{business_account_id}/message_templates`

```json
{
  "name": "order_confirmation",
  "language": "en_US",
  "category": "UTILITY",
  "parameter_format": "NAMED",
  "components": [
    {
      "type": "BODY",
      "text": "Thank you, {{customer_name}}! Your order {{order_number}} is confirmed.",
      "example": {
        "body_text_named_params": [
          { "param_name": "customer_name", "example": "Pablo" },
          { "param_name": "order_number", "example": "ORD-12345" }
        ]
      }
    }
  ]
}
```

Response includes `id` and `status` (usually `PENDING`).

### Update template

`PUT /{business_account_id}/message_templates?hsm_id=<template_id>`

Same body structure as create.

### Delete template

`DELETE /{business_account_id}/message_templates?name=<name>` or `?hsm_id=<template_id>`

## Mark as read

`POST /{phone_number_id}/messages`

```json
{
  "messaging_product": "whatsapp",
  "status": "read",
  "message_id": "wamid......"
}
```

### With typing indicator

```json
{
  "messaging_product": "whatsapp",
  "status": "read",
  "message_id": "wamid......",
  "typing_indicator": { "type": "text" }
}
```

Typing indicator dismisses on send or after ~25s.

## Media

### Upload

`POST /{phone_number_id}/media` (multipart/form-data)

| Field | Value |
|-------|-------|
| `file` | Binary file |
| `messaging_product` | `whatsapp` |

Returns `{ "id": "<MEDIA_ID>" }` for use in send payloads.

### Get URL

`GET /{media_id}?phone_number_id=<phone_number_id>`

Returns temporary download URL (valid 5 minutes).

### Delete

`DELETE /{media_id}?phone_number_id=<phone_number_id>`

### Format limits

| Type | Formats | Max Size |
|------|---------|----------|
| Image | JPEG, PNG | 5 MB |
| Video | MP4, 3GP (H.264 + AAC) | 16 MB |
| Audio | AAC, AMR, MP3, M4A, OGG | 16 MB |
| Voice | OGG (OPUS codec only) | 16 MB |
| Document | PDF, DOC, DOCX, PPT, PPTX, XLS, XLSX, TXT | 100 MB |
| Sticker (static) | WEBP | 100 KB |
| Sticker (animated) | WEBP | 500 KB |

## Query history (Kapso)

These endpoints are Kapso-specific for stored conversation data.

### List messages

`GET /{phone_number_id}/messages`

| Param | Description |
|-------|-------------|
| `conversation_id` | Filter by conversation UUID |
| `direction` | `inbound` or `outbound` |
| `status` | `pending`, `sent`, `delivered`, `read`, `failed` |
| `since` / `until` | ISO 8601 timestamps |
| `limit` | Max 100 |
| `before` / `after` | Cursor pagination |
| `fields` | Use `kapso(...)` for extra fields |

### List conversations

`GET /{phone_number_id}/conversations`

| Param | Description |
|-------|-------------|
| `status` | `active` or `ended` |
| `last_active_since` / `last_active_until` | ISO 8601 timestamps |
| `phone_number` | Filter by customer phone (E.164) |
| `limit` | Max 100 |
| `before` / `after` | Cursor pagination |
| `fields` | Use `kapso(...)` for extra fields |

### Get conversation

`GET /{phone_number_id}/conversations/{conversation_id}`

### List contacts

`GET /{phone_number_id}/contacts`

| Param | Description |
|-------|-------------|
| `wa_id` | Filter by WhatsApp ID |
| `customer_id` | Filter by associated customer |
| `has_customer` | `true` or `false` |
| `limit` | Max 100 |
| `before` / `after` | Cursor pagination |

### Get contact

`GET /{phone_number_id}/contacts/{wa_id}`

## Response format

Successful send returns:

```json
{
  "messaging_product": "whatsapp",
  "contacts": [{ "input": "15551234567", "wa_id": "15551234567" }],
  "messages": [{ "id": "wamid.HBgN..." }]
}
```

## Errors

| Code | Description |
|------|-------------|
| 131047 | 24-hour window expired. Use template instead. |
| 1026 | Receiver incapable (e.g., address_message not supported) |
| 409 | Another message in-flight for this conversation. Retry shortly. |

## Kapso extensions

Add `fields=kapso(...)` to list endpoints:

- `kapso(default)` or `kapso(*)` - all default fields
- `kapso(direction,media_url,contact_name)` - specific fields
- `kapso()` - omit Kapso fields

Common fields: `direction`, `status`, `media_url`, `contact_name`, `flow_response`, `flow_token`, `content`, `message_type_data`.

## Notes

- Discover `phone_number_id` + `business_account_id` via `node scripts/list-platform-phone-numbers.mjs`
- All send payloads require `messaging_product: "whatsapp"`
- Graph version controlled by `META_GRAPH_VERSION` (default `v24.0`)
```

## File: `skills/integrate-whatsapp/references/whatsapp-cloud-api-js.md`
```markdown
---
title: whatsapp-cloud-api-js SDK
---

# whatsapp-cloud-api-js

Use the `@kapso/whatsapp-cloud-api` SDK for typed WhatsApp Cloud API calls.

## Install

```bash
npm install @kapso/whatsapp-cloud-api
```

## Create a client

Kapso proxy setup:

```ts
import { WhatsAppClient } from "@kapso/whatsapp-cloud-api";

const client = new WhatsAppClient({
  baseUrl: "https://api.kapso.ai/meta/whatsapp",
  kapsoApiKey: process.env.KAPSO_API_KEY!
});
```

Direct Meta setup:

```ts
const client = new WhatsAppClient({
  accessToken: process.env.WHATSAPP_TOKEN!
});
```

## Send a text message

```ts
await client.messages.sendText({
  phoneNumberId: "<PHONE_NUMBER_ID>",
  to: "+15551234567",
  body: "Hello from Kapso"
});
```

## Send a raw payload

```ts
await client.messages.sendRaw({
  phoneNumberId: "<PHONE_NUMBER_ID>",
  payload: {
    messaging_product: "whatsapp",
    recipient_type: "individual",
    to: "+15551234567",
    type: "text",
    text: { body: "Hello from a raw payload" }
  }
});
```

## Send a template message

```ts
await client.messages.sendTemplate({
  phoneNumberId: "<PHONE_NUMBER_ID>",
  to: "+15551234567",
  template: {
    name: "order_ready_named",
    language: { code: "en_US" },
    components: [
      {
        type: "body",
        parameters: [
          { type: "text", parameterName: "order_id", text: "ORDER-123" }
        ]
      }
    ]
  }
});
```

## Send an interactive button message

```ts
await client.messages.sendInteractiveButtons({
  phoneNumberId: "<PHONE_NUMBER_ID>",
  to: "+15551234567",
  bodyText: "Choose an option",
  buttons: [
    { id: "accept", title: "Accept" },
    { id: "decline", title: "Decline" }
  ]
});
```

## List conversations

```ts
const conversations = await client.conversations.list({
  phoneNumberId: "<PHONE_NUMBER_ID>",
  status: "active",
  limit: 20
});
```

## Get a conversation

```ts
const conversation = await client.conversations.get({
  conversationId: "123e4567-e89b-12d3-a456-426614174000"
});
```

## List messages

```ts
const messages = await client.messages.query({
  phoneNumberId: "<PHONE_NUMBER_ID>",
  conversationId: "123e4567-e89b-12d3-a456-426614174000",
  limit: 50
});
```

## Get a single message

```ts
const message = await client.messages.get({
  phoneNumberId: "<PHONE_NUMBER_ID>",
  messageId: "wamid.HBgL..."
});
```

## List messages for a conversation (shortcut)

```ts
const messages = await client.messages.listByConversation({
  phoneNumberId: "<PHONE_NUMBER_ID>",
  conversationId: "123e4567-e89b-12d3-a456-426614174000",
  limit: 50
});
```

## Get a template

```ts
const template = await client.templates.get({
  businessAccountId: "<BUSINESS_ACCOUNT_ID>",
  templateId: "564750795574598"
});
```

## Notes

- Use `phoneNumberId` from the connected WhatsApp number (discover via `kapso whatsapp numbers resolve --phone-number "<display-number>" --output json` or `node scripts/list-platform-phone-numbers.mjs`).
- With Kapso proxy, keep `baseUrl` and `kapsoApiKey` set.
- Template rules still apply (examples, button ordering, media headers).
- History endpoints (`messages.query`, `messages.get`, `messages.listByConversation`, `conversations.list/get`) require Kapso proxy; they are not available with a direct Meta access token.
- Requests use camelCase keys and the SDK converts to snake_case for the API; responses come back camelCase.
```

## File: `skills/integrate-whatsapp/references/whatsapp-flows-spec.md`
```markdown
# WhatsApp Business Platform: Flow JSON Reference

## IMPORTANT: Version Requirements

**Always use Flow JSON version 7.3** (the current recommended version). Earlier versions like 5.0 are no longer supported for publishing flows.

```json
{
  "version": "7.3",
  "data_api_version": "3.0",
  ...
}
```

---

Flow JSON enables businesses to create workflows in WhatsApp by accessing the features of WhatsApp Flows using a custom JSON object developed by Meta. These workflows are initiated, run, and managed entirely inside WhatsApp. They can include multiple screens, data flows, and response messages.

To visualize the complete user experience, use the **Builder** in the WhatsApp Manager (Account tools > Flows), which emulates the entire Flow experience.

## Structure of Flow JSON

Flow JSON consists of the following sections:

| Section               | Description                                                                                                                              |
| :-------------------- | :--------------------------------------------------------------------------------------------------------------------------------------- |
| **Screen Data Model** | Commands to define static types that power the screen.                                                                                   |
| **Screens**           | Used to compose layouts using standard UI library components.                                                                            |
| **Components**        | Individual building blocks that make up a screen (text fields, buttons, etc.).                                                           |
| **Routing Model**     | Defines the rules for screen transitions (e.g., Screen 1 can only go to Screen 2). Used for validation.                                  |
| **Actions**           | Syntax to invoke client-side logic. Allowed actions: `navigate`, `data_exchange`, `complete`, `open_url` (v6.0+), `update_data` (v6.0+). |

## Data Exchange quick spec (Kapso Functions)
- WhatsApp sends (POST): `action` (`INIT`/`data_exchange`/`BACK`), `screen`, `data` (fields), `flow_token`, optional `flow_token_signature` (JWT with Meta app secret). Expect response in ~10–15s.
- Kapso forwards to your Function as JSON: `{ source: "whatsapp_flow", flow: { id, meta_flow_id }, data_exchange: <original payload>, signature_valid: true|false, received_at: "<iso8601>" }`.
- Your Function must return JSON:
  - Next screen: `{ "screen": "NEXT_SCREEN", "data": { ... } }`
  - Validation on same screen: `{ "screen": "CURRENT", "data": { "error_message": "Try again" } }`
  - Completion: `{ "screen": "SUCCESS", "data": { "extension_message_response": { "params": { ... } } } }`
  - Optional: include `vars` to persist variables; `next_edge` is not required for WhatsApp flows.
- Do NOT include `endpoint_uri` / `data_channel_uri` (Kapso injects). Do NOT wrap JSON in markdown fences.
- Runtime tips: keep total work under ~12s, minimal external calls, respond with `Content-Type: application/json`.

### Common gotchas (read me first)
- **Dynamic property rule:** `${form.*}` and `${data.*}` must be the entire property value. `"Hello ${data.name}"` is invalid unless you use a backticked nested expression (v6.0+): ``"text": "`'Hello ' ${data.name}`"``.
- **Schema as whitelist:** On dynamic screens, declare **every** field your endpoint may return under `screen.data`. Undeclared fields may be dropped by Meta/Kapso even if your endpoint returns them.
- **Custom payload keys:** Extra keys in action payloads are forwarded as-is to `data_exchange.data`. Avoid reserved names like `action`, `screen`, `data`; prefer explicit names such as `user_action`, `step`, `intent`.
- **Version is mandatory:** Every endpoint response must include `"version": "3.0"` or the UI can appear to return empty data (silent failure).
- **Error responses need full data:** When you stay on the same screen with `error_message`, still include all data the screen expects (lists, init-values, etc.) or components can break.
- **Carry data forward:** Global references (`${screen.SCREEN.form.field}`) exist, but the safest pattern is to re-send needed values in each response: return them in `data` for the next screen and reference via `${data.field}`.
- **Routing pattern:** Route primarily on `data_exchange.action` then `data_exchange.screen`; see the example in “Action Routing Pattern” below for a multi-screen skeleton.

### Mini handler examples
Cloudflare Worker:
```javascript
async function handler(request) {
  const body = await request.json();
  const screen = body.data_exchange?.screen || "WELCOME";
  return new Response(JSON.stringify({
    screen: "SUCCESS",
    data: { message: `Thanks from ${screen}` }
  }), { headers: { "Content-Type": "application/json" } });
}
```

## Data Endpoint Quick Start (Kapso Functions)

This section is the **minimum you must do** to make a WhatsApp Flow endpoint work reliably with Kapso Functions.

### Enabling flows encryption
- Endpoint operations (create/update) require Flows encryption to be enabled.
- The Kapso Agent can enable this for you automatically when needed.
- If the agent can’t enable it (for example, no phone number selected) or asks you to do it manually:
  - In Kapso, click the **Settings** gear in the top-right toolbar.
  - Open the WhatsApp/Phone configuration section.
  - Toggle **Enable encryption** for the phone number / WhatsApp Business Account.

### 1. Response Contract (Critical)

Every response from your Function **must** include all three fields:

```json
{
  "version": "3.0",
  "screen": "NEXT_SCREEN_ID",
  "data": { }
}
```

- **CRITICAL:** if `version` is missing or incorrect, the flow can appear to
  succeed at the HTTP layer but behave as if no data was returned (silent
  failure / empty data in the UI).

- `version`
  - **Required** for all `data_exchange` responses.
  - Use `"3.0"` unless Meta changes the `data_api_version`.
  - If you omit or mis-set this, the flow may **fail silently** and appear to return empty data.
- `screen`
  - The screen to render next. Must exist in the Flow’s `routing_model`.
- `data`
  - Object with properties consumed by your Flow JSON (lists, error messages, etc.).

Examples:

```json
{
  "version": "3.0",
  "screen": "APPOINTMENT_SLOTS",
  "data": {
    "available_slots": [
      { "id": "slot-1", "title": "Today 10:00" },
      { "id": "slot-2", "title": "Today 11:00" }
    ]
  }
}
```

```json
{
  "version": "3.0",
  "screen": "APPOINTMENT_SLOTS",
  "data": {
    "error_message": "Please select a valid time",
    "available_slots": [
      { "id": "slot-1", "title": "Today 10:00" },
      { "id": "slot-2", "title": "Today 11:00" }
    ]
  }
}
```

```json
{
  "version": "3.0",
  "screen": "SUCCESS",
  "data": {
    "extension_message_response": {
      "params": {
        "flow_token": "<FLOW_TOKEN>",
        "summary": "Booked for 2025-01-10 at 10:00"
      }
    }
  }
}
```

### 2. Request Payload Map

Kapso decrypts Meta’s encrypted payload and forwards the following JSON to your Function:

```json
{
  "source": "whatsapp_flow",
  "flow": {
    "id": "<kapso_flow_id>",
    "meta_flow_id": "<meta_flow_id>"
  },
  "data_exchange": {
    "version": "3.0",
    "action": "INIT",
    "screen": "CURRENT_SCREEN_ID",
    "data": {},
    "flow_token": "<FLOW_TOKEN>",
    "flow_token_signature": "<JWT>"
  },
  "signature_valid": true,
  "received_at": "2025-01-01T12:34:56Z"
}
```

In your handler:

- User inputs: `body.data_exchange.data.<field_name>`
- Current screen: `body.data_exchange.screen`
- Flow action: `body.data_exchange.action` (`"INIT"`, `"data_exchange"`, `"BACK"`)
- Flow token: `body.data_exchange.flow_token`
- Signature: `body.data_exchange.flow_token_signature` + `body.signature_valid` if you want to enforce it.

You **do not** need to implement encryption/decryption yourself; Kapso already does that before calling your Function.

Note: in invocation logs we store a simplified shape with a top-level
`flow_id` for convenience. The JSON sent to your Function uses the `flow`
object as shown above.

### 3. Action Routing Pattern

A simple decision tree that works for most flows:

- **Best practice:** route primarily by `data_exchange.action` and
  `data_exchange.screen`. Use custom fields inside `data` only for secondary
  branching, not as your main router.

```ts
const de = body.data_exchange;
const action = de.action;
const screen = de.screen;
const data = de.data || {};

if (action === "INIT") {
  // First time the flow calls your endpoint
  return {
    version: "3.0",
    screen: "FIRST_SCREEN",
    data: {}
  };
}

if (action === "BACK") {
  // User pressed back; decide whether to re-load or reuse previous data
  return {
    version: "3.0",
    screen: screen || "FIRST_SCREEN",
    data: {}
  };
}

if (action === "data_exchange") {
  if (screen === "SCREEN_A") {
    // Process Screen A and send Screen B
    return {
      version: "3.0",
      screen: "SCREEN_B",
      data
    };
  }

  if (screen === "SCREEN_B") {
    // Maybe complete the flow
    return {
      version: "3.0",
      screen: "SUCCESS",
      data: {
        extension_message_response: {
          params: {
            flow_token: de.flow_token
          }
        }
      }
    };
  }
}
```

End-to-end multi-screen skeleton (INIT → SCREEN_A → SCREEN_B → SUCCESS):

```ts
if (action === "INIT") {
  return { version: "3.0", screen: "SCREEN_A", data: {} };
}

if (action === "data_exchange") {
  if (screen === "SCREEN_A") {
    // validate, fetch data
    return { version: "3.0", screen: "SCREEN_B", data: { slots, user_email: data.email } };
  }

  if (screen === "SCREEN_B") {
    // final submission
    return {
      version: "3.0",
      screen: "SUCCESS",
      data: {
        extension_message_response: {
          params: { flow_token: de.flow_token }
        }
      }
    };
  }
}
```

You can also use a custom field inside `data` (for example, `data.action`) to branch when multiple buttons on the same screen go to different places.

When in doubt, start with a minimal pattern:

- On `INIT`, return your first screen with any initial data.
- On `data_exchange` from that screen, validate inputs and either:
  - stay on the same screen with `error_message`, or
  - move to the next screen with derived data.
- On `data_exchange` from the final screen, return `SUCCESS` with an
  `extension_message_response` payload to complete the flow.

### 4. Error Handling Rules

Follow Meta’s rules, but in practice:

- Always return HTTP `200` from your Function (Kapso handles HTTP errors upstream).
- Never rely on 4xx/5xx to signal validation errors to the user.
- Use `data.error_message` with the same `screen` to show a snackbar and keep the user on the current screen.
- When returning an error, still include all data fields the screen expects (lists, init values, etc.) so components continue to render.
- Keep payloads small; avoid huge objects or unnecessary fields.

Example (validation failure):

```json
{
  "version": "3.0",
  "screen": "APPOINTMENT_SLOTS",
  "data": {
    "error_message": "That time is no longer available. Please pick another.",
    "available_slots": []
  }
}
```

### 5. Component Data Contract (Dynamic Options)

When a component uses a data source from the endpoint, the field name and shape must match exactly.

Example – dropdown with dynamic options:

```json
{
  "type": "Dropdown",
  "name": "slot_id",
  "data-source": "${data.available_slots}"
}
```

Your endpoint must return:

```json
{
  "version": "3.0",
  "screen": "APPOINTMENT_SLOTS",
  "data": {
    "available_slots": [
      { "id": "slot-1", "title": "Today 10:00" },
      { "id": "slot-2", "title": "Today 11:00" }
    ]
  }
}
```

- Field name in `data` → `available_slots`
- Each item → `{ "id": string, "title": string }`

### 6. Debugging & Logging Checklist

When debugging a Flow + Endpoint integration:

1. Log the raw forwarded body (from Kapso to your Function).
2. Log:
   - `data_exchange.action`
   - `data_exchange.screen`
   - `data_exchange.data`
3. Log the external API request/response (status, body shape).
4. Log the final response you return to Kapso (with `version`, `screen`, `data`).
5. If the UI shows an empty screen or no data:
   - Check `version` is `"3.0"` in responses.
   - Check `screen` exists in `routing_model`.
   - Check `data` field names match the Flow JSON.
   - Check array/object shape (especially for lists).

---

## Top-level Flow JSON Properties

### Required Properties
*   **`version`**: Represents the version of Flow JSON to use during compilation.
*   **`screens`**: An array representing the different pages (nodes) of the user experience.

### Optional Properties
*   **`routing_model`**: Represents the routing system. Generated automatically if the Flow does not use a Data Endpoint. Required if using an endpoint.
*   **`data_api_version`**: The version used for communication with the WhatsApp Flows Data Endpoint (currently `3.0`).
*   **`data_channel_uri`**: **Note:** Not supported as of Flow JSON 3.0. For v3.0+, configure the URL using the `endpoint_uri` field provided by the Flows API.

> **Version fields cheat sheet**
>
> - Flow JSON `version`: which Flow JSON schema version your flow uses (for example, `"3.1"`).
> - `data_api_version`: protocol version for the data endpoint (currently `"3.0"`).
> - Data-exchange payload `version`: the value Meta sends in `data_exchange.version` (should match `data_api_version`).
> - Endpoint response `version`: you must echo `"3.0"` in every response your Function returns. If you omit it, Meta may treat the payload as invalid and your flow can appear to return empty data.

**Example (Version 2.1 - Legacy)**
```json
{
 "version": "2.1",
 "data_api_version": "3.0",
 "routing_model": {"MY_FIRST_SCREEN": ["MY_SECOND_SCREEN"] },
 "screens": [...],
 "data_channel_uri": "https://example.com"
}
```

**Example (Version 3.1 - Current)**
```json
{
 "version": "3.1",
 "data_api_version": "3.0",
 "routing_model": {"MY_FIRST_SCREEN": ["MY_SECOND_SCREEN"] },
 "screens": [...]
}
```

---

## Screens

Screens are the main unit of a Flow. Each screen represents a single node in the state machine.

**Schema:**
```json
"screen" : {
  "id": "string",
  "terminal": boolean,
  "success": boolean,
  "title": "string",
  "refresh_on_back": boolean,
  "data": object,
  "layout": object,
  "sensitive": []
}
```

### Properties
*   **`id`** (Required): Unique identifier. `SUCCESS` is a reserved keyword and cannot be used.
*   **`layout`** (Required): The UI Layout. Can be predefined or a container with custom content using the WhatsApp Flows Library.
*   **`terminal`** (Optional): If `true`, this screen ends the flow. A Footer component is mandatory on terminal screens.
*   **`title`** (Optional): Attribute rendered in the top navigation bar.
*   **`success`** (Optional, terminal only): Defaults to `true`. Marks whether terminating on this screen is a successful business outcome.
*   **`data`** (Optional): Declaration of dynamic data that fills the components using JSON Schema.
    *   **Dynamic screens:** Declare **every field** your endpoint will return for this screen. Undeclared fields may be dropped and unavailable for binding even if the endpoint returns them.
    ```json
    {
      "data": {
        "first_name": {
          "type": "string",
          "__example__": "John"
        }
      }
    }
    ```
*   **`refresh_on_back`** (Optional, Data Endpoint only): Defaults to `false`. Defines whether to trigger a data exchange request when using the back button to return to this screen.
    *   **`false`**: Screen loads with previously provided data/input. Avoids roundtrip; snappier experience.
    *   **`true`**: Sends a request to the Endpoint (Action: `BACK`, Screen: Name of previous screen) to revalidate/update data.
*   **`sensitive`** (Optional, v5.1+): Defaults to `[]`. Array of field names containing sensitive data. When the Flow completes, the summary message will mask these fields based on the component type. Each field name must correspond to an input component (with matching `name` attribute) that exists on the same screen. Do not include fields from other screens. Review/summary screens that only display text (no input components) should not have a `sensitive` array.

### Sensitive Fields Masking Behavior
| Component           | Masking | Consumer Experience |
| :------------------ | :------ | :------------------ |
| Text Input          | ✅       | Masked (••••)       |
| Password / OTP      | ❌       | Hidden completely   |
| Text Area           | ✅       | Masked (••••)       |
| Date Picker         | ✅       | Masked (••••)       |
| Dropdown            | ✅       | Masked (••••)       |
| Checkbox Group      | ✅       | Masked (••••)       |
| Radio Buttons Group | ✅       | Masked (••••)       |
| Opt In              | ❌       | Display as-is       |
| Document Picker     | ✅       | Hidden completely   |
| Photo Picker        | ✅       | Hidden completely   |

---

## Layout

Layout represents screen UI Content.
*   **`type`**: Currently, only `"SingleColumnLayout"` (vertical flexbox container) is available.
*   **`children`**: An array of components from the WhatsApp Flows Library.

---

## Routing Model

Required only when using an Endpoint. It is a directed graph where screens are nodes and transitions are edges.

*   **Structure**: A map of screen IDs to an array of possible next screen IDs.
*   **Limits**: Maximum 10 "branches" or connections.
*   **Entry Screen**: A screen with no inbound edge.
*   **Terminal**: All routes must eventually end at a terminal screen.

**Example:**
```json
"routing_model": {
  "MY_FIRST_SCREEN": ["MY_SECOND_SCREEN"],
  "MY_SECOND_SCREEN": ["MY_THIRD_SCREEN"]
}
```

---

## Properties (Static vs. Dynamic)

### Static Properties
Set once and never change.
```json
"title": "Demo Screen"
```

### Dynamic Properties
Set content based on server or user data.
*   **Form properties**: `${form.field_name}` (Data entered by user).
*   **Screen properties**: `${data.field_name}` (Data provided by server or previous screen).

Supported types: `string`, `number`, `boolean`, `object`, `array`.

### Nested Expressions (v6.0+)
Allows conditionals and string concatenation. Must be wrapped in backticks (`` ` ``).
*   **Equality**: `==`, `!=`
*   **Math Comparisons**: `<`, `<=`, `>`, `>=`
*   **Logical**: `&&`, `||`
*   **Math Operations**: `+`, `-`, `/`, `%` (numbers only, not for strings)
*   **Escaping**: To use backticks inside a string, use double backslash: `\\` before it.

**Examples:**
*   **String Concatenation**: ``"text": "`'Hello ' ${form.first_name}`"`` (no `+` operator, just place strings next to each other)
*   **Multiple strings**: ``"text": "`${data.street} ', ' ${data.city} ', ' ${data.country}`"``
*   **Math**: ``"text": "`'Amount: ' ${data.total} / ${form.group_size}`"``
*   **Logic**: ``"visible": "`(${form.age} > 18) && ${form.accept}`"``
*   **Equality**: ``"visible": "`${form.first_name} == ${form.last_name}`"``

**Important:** Outside backticked nested expressions, a property cannot mix static text with `${...}`. Use either a pure dynamic value (e.g., `"text": "${data.name}"`) or the backtick form above for string concatenation.

---

## Forms and Data Handling

### Forms (Legacy vs v4.0+)
*   **Before v4.0**: Inputs had to be wrapped in a `"type": "Form"` component.
*   **v4.0+**: The `Form` component is optional. You can place interactive components directly in the layout.

### Form Configuration
*   **`init-values`**: Key-value object to pre-fill inputs. Types must match the component (e.g., Array of Strings for CheckboxGroup, String for TextInput).
*   **`error-messages`**: Key-value object to set custom errors.

**Example (v4.0+ No Form Component):**
```json
{
  "id": "DEMO_SCREEN",
  "data": {
     "init_values": { "first_name": "Jon" }
  },
  "layout": {
      "type": "SingleColumnLayout",
      "children": [
         {
             "type": "TextInput",
             "name": "first_name",
             "label": "First Name",
             "init-value": "${data.init_values.first_name}"
         }
      ]
  }
}
```

### Global Dynamic Referencing (v4.0+)
Allows accessing data from any screen globally.
**Syntax:** `${screen.<screen_name>.(form|data).<field-name>}`

*   **`screen`**: Global variable keyword.
*   **`screen_name`**: ID of the screen to reference.
*   **`(form|data)`**: Storage type.
*   **`field-name`**: Specific field.

**Use Case:** You no longer need to pass payloads explicitly in the `navigate` action to carry data forward.
**Practical tip:** For reliability, especially across different Flow JSON versions, also include needed values in the `data` you return for the next screen (e.g., echo `user_email` and `selected_date` forward) so components can bind via `${data.*}` even if global references are unavailable.

---

## Actions

Actions trigger asynchronous logic.

### 1. `navigate`
Transitions to the next screen.
*   **Payload**: Required, even if empty `{}`. Data passed here is available in the next screen via `${data.field}`.
*   **Note**: Do not use on the footer of a terminal screen.

```json
"on-click-action": {
  "name": "navigate",
  "next": { "type": "screen", "name": "NEXT_SCREEN" },
  "payload": {
    "name": "${form.first_name}"
  }
}
```

With no data to pass:
```json
"on-click-action": {
  "name": "navigate",
  "next": { "type": "screen", "name": "NEXT_SCREEN" },
  "payload": {}
}
```

### 2. `complete`
Terminates the flow and sends the payload to the chat thread via webhook.
*   **Recommendation**: Keep payload size minimum. Avoid base64 images.

```json
"on-click-action": {
  "name": "complete",
  "payload": {
    "selected_items": "${form.selected_items}"
  }
}
```

### 3. `data_exchange`
Sends data to the WhatsApp Flows Data Endpoint. The server response determines the next step.
*   Payload keys are forwarded as-is to your endpoint. Avoid generic names like `action` that may collide with Meta fields; prefer explicit keys such as `user_action`, `step`, `intent`.

```json
"on-click-action": {
  "name": "data_exchange",
  "payload": {
    "discount_code": "${data.discount_code}"
  }
}
```

### 4. `update_data` (v6.0+)
Triggers an immediate update to the screen's state based on user interaction (e.g., changing a dropdown list based on a previous selection) without a full screen refresh.

```json
"on-click-action": {
  "name": "update_data",
  "payload": {
    "state_list": "${data.countries[form.selected_country].states}"
  }
}
```

### 5. `open_url` (v6.0+)
Opens a URL in the device's default browser.
*   **Supported Components**: `EmbeddedLink` and `OptIn`.
*   **Payload**: Accepts only a `url` property.

```json
{
   "type": "EmbeddedLink",
   "text": "Terms and Conditions",
   "on-click-action": {
      "name": "open_url",
      "url": "https://www.whatsapp.com/"
   }
}
```

---

## Limitations

*   **File Size**: Flow JSON content string cannot exceed **10 MB**.
*   


# Flow JSON Components

Components are the building blocks of WhatsApp Flows. They allow you to build complex UIs and display business data using attribute models.

*   **Limit:** The maximum number of components per screen is **50**.

**Supported Components:**
*   **Text:** Heading, Subheading, Caption, Body, RichText
*   **Input:** TextEntry (TextInput, TextArea), DatePicker, CalendarPicker, Media upload
*   **Selection:** CheckboxGroup, RadioButtonsGroup, Dropdown, Chips Selector, Switch
*   **Display/Media:** Image, Image Carousel
*   **Navigation/Action:** Footer, OptIn, EmbeddedLink, NavigationList
*   **Logic:** If

---

## Text Components

### Heading
Top level title of a page.
| Parameter | Description                                 |
| :-------- | :------------------------------------------ |
| `type`    | (Required) `"TextHeading"`                  |
| `text`    | (Required) String or Dynamic `${data.text}` |
| `visible` | Boolean. Default: `true`.                   |

### Subheading
| Parameter | Description                                 |
| :-------- | :------------------------------------------ |
| `type`    | (Required) `"TextSubheading"`               |
| `text`    | (Required) String or Dynamic `${data.text}` |
| `visible` | Boolean. Default: `true`.                   |

### Body
| Parameter       | Description                                           |
| :-------------- | :---------------------------------------------------- |
| `type`          | (Required) `"TextBody"`                               |
| `text`          | (Required) String or Dynamic `${data.text}`           |
| `font-weight`   | Enum: `{'bold','italic','bold_italic','normal'}`      |
| `strikethrough` | Boolean                                               |
| `visible`       | Boolean. Default: `true`.                             |
| `markdown`      | Boolean. Default: `false`. (Requires Flow JSON V5.1+) |

### Caption
| Parameter       | Description                                           |
| :-------------- | :---------------------------------------------------- |
| `type`          | (Required) `"TextCaption"`                            |
| `text`          | (Required) String or Dynamic `${data.text}`           |
| `font-weight`   | Enum: `{'bold','italic','bold_italic','normal'}`      |
| `strikethrough` | Boolean                                               |
| `visible`       | Boolean. Default: `true`.                             |
| `markdown`      | Boolean. Default: `false`. (Requires Flow JSON V5.1+) |

### Markdown Support (v5.1+)
`TextBody` and `TextCaption` support limited markdown if `markdown: true` is set.
```json
{
   "type": "TextBody",
   "markdown": true,
   "text": [ "This text is ~~***really important***~~" ]
}
```

### Limits and Restrictions
| Component  | Property        | Limit / Restriction                  |
| :--------- | :-------------- | :----------------------------------- |
| Heading    | Character Limit | 80                                   |
| Subheading | Character Limit | 80                                   |
| Body       | Character Limit | 4096                                 |
| Caption    | Character Limit | 409                                  |
| All        | Text            | Empty or Blank value is not accepted |

---

## RichText (v5.1+)
Provides rich formatting capabilities and rendering for large texts (Terms, Policies, etc.).

| Parameter | Description                                               |
| :-------- | :-------------------------------------------------------- |
| `type`    | (Required) `"RichText"`                                   |
| `text`    | (Required) String or String Array. Dynamic `${data.text}` |
| `visible` | Boolean. Default: `true`.                                 |

**Note:**
*   **Until V6.2:** Must be a standalone component (cannot share screen with others).
*   **Starting V6.3:** Can be used with a `Footer` component.

### Supported Syntax
*   **Headings:** `# Heading 1`, `## Heading 2` (Others render as body text).
*   **Formatting:** `**bold**`, `*italic*`, `~~strikethrough~~`.
*   **Lists:** Ordered (`1. Item`) and Unordered (`- Item` or `+ Item`).
*   **Images:** Base64 inline only. `![Alt](data:image/png;base64,...)`.
    *   *Formats:* png, jpg/jpeg, webp (iOS 14.6+).
*   **Links:** `[Text](URL)`
*   **Tables:** Standard Markdown syntax. Columns widths based on header content size.

### Syntax Cheatsheet
| Syntax                               | RichText | TextBody | TextCaption |
| :----------------------------------- | :------- | :------- | :---------- |
| `# H1`, `## H2`                      | ✅        | ❌        | ❌           |
| `**bold**`, `*italic*`, `~~strike~~` | ✅        | ✅        | ✅           |
| Lists (`+`, `-`, `1.`)               | ✅        | ✅        | ✅           |
| `[Link](url)`                        | ✅        | ✅        | ✅           |
| `![Image](base64)`                   | ✅        | ❌        | ❌           |
| Tables                               | ✅        | ❌        | ❌           |

---

## Text Entry Components

### TextInput
| Parameter       | Description                                                        |
| :-------------- | :----------------------------------------------------------------- |
| `type`          | (Required) `"TextInput"`                                           |
| `name`          | (Required) String                                                  |
| `label`         | (Required) String.                                                 |
| `label-variant` | `large` (v7.0+) - Prominent style, multi-line support.             |
| `input-type`    | Enum: `{'text','number','email', 'password', 'passcode', 'phone'}` |
| `pattern`       | (v6.2+) Regex string. Requires `helper-text`.                      |
| `required`      | Boolean                                                            |
| `min-chars`     | Integer                                                            |
| `max-chars`     | Integer. Default: 80.                                              |
| `helper-text`   | String                                                             |
| `visible`       | Boolean. Default: `true`.                                          |
| `init-value`    | (v4.0+) String. Only outside `Form`.                               |
| `error-message` | (v4.0+) String. Only outside `Form`.                               |

### TextArea
| Parameter       | Description                          |
| :-------------- | :----------------------------------- |
| `type`          | (Required) `"TextArea"`              |
| `name`          | (Required) String                    |
| `label`         | (Required) String.                   |
| `label-variant` | `large` (v7.0+)                      |
| `max-length`    | Integer. Default: 600.               |
| `helper-text`   | String                               |
| `enabled`       | Boolean                              |
| `visible`       | Boolean. Default: `true`.            |
| `init-value`    | (v4.0+) String. Only outside `Form`. |
| `error-message` | (v4.0+) String. Only outside `Form`. |

### Limits
| Component | Property           | Limit              |
| :-------- | :----------------- | :----------------- |
| TextInput | Helper/Error/Label | 80 / 30 / 20 chars |
| TextArea  | Helper/Label       | 80 / 20 chars      |

---

## Selection Components

### CheckboxGroup & RadioButtonsGroup
**CheckboxGroup:** Pick multiple. **RadioButtonsGroup:** Pick one.

| Parameter            | Description                                         |
| :------------------- | :-------------------------------------------------- |
| `type`               | `"CheckboxGroup"` or `"RadioButtonsGroup"`          |
| `name`               | (Required) String                                   |
| `data-source`        | (Required) Array of objects (See structure below)   |
| `label`              | String (Required v4.0+)                             |
| `min-selected-items` | Integer (Checkbox only)                             |
| `max-selected-items` | Integer (Checkbox only)                             |
| `enabled`            | Boolean                                             |
| `required`           | Boolean                                             |
| `visible`            | Boolean                                             |
| `on-select-action`   | Action (`data_exchange`, `update_data` v6.0+)       |
| `on-unselect-action` | (v6.0+) Action (`update_data` only)                 |
| `init-value`         | Array<String> (Checkbox) or String (Radio). (v4.0+) |
| `media-size`         | (v5.0+) Enum: `{'regular', 'large'}`                |

**Data Source Structure:**
*   **< v5.0:** `id`, `title`, `description`, `metadata`, `enabled`.
*   **> v5.0:** Adds `image` (Base64), `alt-text`, `color` (hex).
*   **> v6.0:** Adds `on-select-action`, `on-unselect-action`.

**Limits:**
*   **Items:** Min 1, Max 20.
*   **Image Size:** 100KB (v6.0+), 300KB (<v6.0).
*   **Text:** Title (30), Desc (30), Meta (300).

### Dropdown
| Parameter            | Description                                         |
| :------------------- | :-------------------------------------------------- |
| `type`               | (Required) `"Dropdown"`                             |
| `label`              | (Required) String                                   |
| `data-source`        | (Required) Array (Same structure as Checkbox/Radio) |
| `required`           | Boolean                                             |
| `enabled`            | Boolean                                             |
| `visible`            | Boolean                                             |
| `on-select-action`   | Action (`data_exchange`, `update_data`)             |
| `on-unselect-action` | (v6.0+) Action (`update_data` only)                 |
| `init-value`         | String (v4.0+)                                      |

**Limits:**
*   **Items:** Max 200 (no images), Max 100 (with images).
*   **Text:** Label (20), Title (30), Desc (300).

### Chips Selector (v6.3+)
Allows picking multiple selections.

| Parameter                | Description                                                               |
| :----------------------- | :------------------------------------------------------------------------ |
| `type`                   | `"ChipsSelector"`                                                         |
| `name`                   | (Required) String                                                         |
| `data-source`            | Array: `id`, `title`, `enabled`, `on-select-action`, `on-unselect-action` |
| `label`                  | (Required) String                                                         |
| `min/max-selected-items` | Integer                                                                   |
| `on-select-action`       | Action (`data_exchange`, `update_data` v7.1+)                             |
| `on-unselect-action`     | (v7.1+) Action (`update_data` only)                                       |

**Limits:** Min 2 options, Max 20 options. Label 80 chars.

### Switch (v4.0+)
Renders components based on a value match.

| Parameter | Description                                                      |
| :-------- | :--------------------------------------------------------------- |
| `type`    | `"Switch"`                                                       |
| `value`   | (Required) String variable to evaluate (e.g., `${data.animal}`)  |
| `cases`   | (Required) Map. Key = string value. Value = Array of Components. |

---

## Action & Navigation Components

### Footer
| Parameter         | Description       |
| :---------------- | :---------------- |
| `type`            | `"Footer"`        |
| `label`           | (Required) String |
| `on-click-action` | (Required) Action |
| `left-caption`    | String            |
| `center-caption`  | String            |
| `right-caption`   | String            |

*   **Rule:** Can set Left+Right OR Center, but not all 3.
*   **Limits:** Label (35 chars), Captions (15 chars). 1 Footer per screen.

### OptIn
| Parameter                   | Description                                                 |
| :-------------------------- | :---------------------------------------------------------- |
| `type`                      | `"OptIn"`                                                   |
| `label`                     | (Required) String                                           |
| `name`                      | (Required) String                                           |
| `on-click-action`           | Action (Triggers "Read more"). Supports `open_url` (v6.0+). |
| `on-select/unselect-action` | (v6.0+) `update_data` only.                                 |

*   **Limits:** 120 chars, Max 5 per screen.

### EmbeddedLink
| Parameter         | Description                                                       |
| :---------------- | :---------------------------------------------------------------- |
| `type`            | `"EmbeddedLink"`                                                  |
| `text`            | (Required) String                                                 |
| `on-click-action` | (Required) Action (`navigate`, `data_exchange`, `open_url` v6.0+) |

*   **Limits:** 25 chars, Max 2 per screen.

### NavigationList (v6.2+)
List of options to navigate between screens.

| Parameter         | Description                                                       |
| :---------------- | :---------------------------------------------------------------- |
| `type`            | `"NavigationList"`                                                |
| `list-items`      | (Required) Array.                                                 |
| `on-click-action` | `data_exchange` or `navigate`. Can be on component or item level. |

**Item Structure:**
*   `main-content` (Req): `title` (30 chars), `description` (20), `metadata` (80).
*   `start`: `image` (Base64, 100KB), `alt-text`.
*   `end`: `title` (10 chars), `description` (10), `metadata` (10).
*   `badge`: String (15 chars). Max 1 item with badge per list.
*   `tags`: Array<string> (Max 3).

**Restrictions:** Max 2 per screen. Cannot be on terminal screen. Cannot be combined with other components.

---

## Date & Time Components

### DatePicker
**Important (v5.0+):** Uses formatted date string `"YYYY-MM-DD"`. This decouples values from time zones.

| Parameter               | Description                                       |
| :---------------------- | :------------------------------------------------ |
| `type`                  | `"DatePicker"`                                    |
| `name`                  | (Required) String                                 |
| `label`                 | (Required) String                                 |
| `min-date` / `max-date` | String (Timestamp in ms). See *Guidelines* below. |
| `unavailable-dates`     | Array <Timestamp in ms>.                          |
| `on-select-action`      | Only `data_exchange`.                             |

**Guidelines (< v5.0):**
If business and user are in different time zones, timezone offsets can cause incorrect dates.
*   *Recommendation:* Use v5.0+ logic ("YYYY-MM-DD") or calculate offsets carefully using the user's timezone (collected via Dropdown).

### CalendarPicker (v6.1+)
Full calendar interface.

| Parameter             | Description                                                  |
| :-------------------- | :----------------------------------------------------------- |
| `type`                | `"CalendarPicker"`                                           |
| `mode`                | `"single"` (Default) or `"range"`.                           |
| `label`               | String. If range: `{"start-date": "...", "end-date": "..."}` |
| `min-date`/`max-date` | String `"YYYY-MM-DD"`.                                       |
| `include-days`        | Array<Enum> (Mon, Tue, etc.). Default: All.                  |
| `min-days`/`max-days` | Integer (Range mode only).                                   |
| `on-select-action`    | `data_exchange`. Payload: String (Single) or Object (Range). |

---

## Media Components

### Image
| Parameter          | Description                     |
| :----------------- | :------------------------------ |
| `type`             | `"Image"`                       |
| `src`              | (Required) Base64 string.       |
| `scale-type`       | `cover` or `contain` (Default). |
| `aspect-ratio`     | Number. Default 1.              |
| `width` / `height` | Integer.                        |

*   **Limits:** Max 3 per screen, 300kb (Rec), 1MB Payload limit. Format: JPEG, PNG.

### Image Carousel (v7.1+)
Slide through multiple images.

| Parameter      | Description                           |
| :------------- | :------------------------------------ |
| `type`         | `"ImageCarousel"`                     |
| `images`       | (Required) Array `{ src, alt-text }`. |
| `aspect-ratio` | `"4:3"` (Default) or `"16:9"`.        |
| `scale-type`   | `cover` or `contain` (Default).       |

*   **Limits:** Min 1, Max 3 images. Max 2 carousels per screen.

### PhotoPicker (v4.0+)
Allows users to upload photos from camera or gallery.

| Parameter              | Description                                                                 |
| :--------------------- | :-------------------------------------------------------------------------- |
| `type`                 | (Required) `"PhotoPicker"`                                                  |
| `name`                 | (Required) String. Must be unique on the screen.                            |
| `label`                | (Required) String. Max 80 chars. Dynamic supported.                         |
| `description`          | String. Max 300 chars. Dynamic supported.                                   |
| `photo-source`         | Enum: `"camera_gallery"` (default), `"camera"`, `"gallery"`                 |
| `max-file-size-kb`     | Integer (kibibytes). Default: 25600 (25 MiB). Range: [1, 25600]             |
| `min-uploaded-photos`  | Integer. Default: 0. Range: [0, 30]. Use this instead of `required`.        |
| `max-uploaded-photos`  | Integer. Default: 30. Range: [1, 30]                                        |
| `enabled`              | Boolean. Default: true                                                      |
| `visible`              | Boolean. Default: true                                                      |
| `error-message`        | String or Object for image-specific errors                                  |

**Important:**
- `required` property is NOT supported. Use `min-uploaded-photos: 1` for required.
- Only 1 PhotoPicker allowed per screen.
- Cannot use PhotoPicker and DocumentPicker on the same screen.
- Cannot be used in `navigate` action payload. Use `data_exchange` or `complete`.
- Must be top-level in action payload: `"media": "${form.photo_picker}"` (not nested).

### DocumentPicker (v4.0+)
Allows users to upload documents.

| Parameter                 | Description                                                              |
| :------------------------ | :----------------------------------------------------------------------- |
| `type`                    | (Required) `"DocumentPicker"`                                            |
| `name`                    | (Required) String. Must be unique on the screen.                         |
| `label`                   | (Required) String. Max 80 chars. Dynamic supported.                      |
| `description`             | String. Max 300 chars. Dynamic supported.                                |
| `max-file-size-kb`        | Integer (kibibytes). Default: 25600 (25 MiB). Range: [1, 25600]          |
| `min-uploaded-documents`  | Integer. Default: 0. Range: [0, 30]. Use this instead of `required`.     |
| `max-uploaded-documents`  | Integer. Default: 30. Range: [1, 30]                                     |
| `allowed-mime-types`      | Array of strings. See supported list below.                              |
| `enabled`                 | Boolean. Default: true                                                   |
| `visible`                 | Boolean. Default: true                                                   |
| `error-message`           | String or Object for document-specific errors                            |

**Supported MIME types:** `application/pdf`, `application/msword`, `application/vnd.openxmlformats-officedocument.wordprocessingml.document`, `application/vnd.ms-excel`, `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`, `application/vnd.ms-powerpoint`, `application/vnd.openxmlformats-officedocument.presentationml.presentation`, `application/zip`, `application/gzip`, `application/x-7z-compressed`, `text/plain`, `image/jpeg`, `image/png`, `image/gif`, `image/webp`, `image/heic`, `image/heif`, `image/avif`, `image/tiff`, `video/mp4`, `video/mpeg`

**Important:**
- `required` property is NOT supported. Use `min-uploaded-documents: 1` for required.
- Only 1 DocumentPicker allowed per screen.
- Cannot use PhotoPicker and DocumentPicker on the same screen.
- Cannot be used in `navigate` action payload. Use `data_exchange` or `complete`.
- Must be top-level in action payload: `"media": "${form.document_picker}"` (not nested).

### Media Upload Limits
- Max 10 files can be sent in response message.
- Max aggregated size: 100 MiB for response message attachments.
- Files stored in WhatsApp CDN for up to 20 days (encrypted).

---

## Logic Components

### If (v4.0+)
Conditional rendering.

| Parameter   | Description                           |
| :---------- | :------------------------------------ |
| `type`      | `"If"`                                |
| `condition` | (Required) Boolean expression string. |
| `then`      | (Required) Array of Components.       |
| `else`      | Array of Components.                  |

**Operators:** `==`, `!=`, `&&`, `||`, `!`, `>`, `>=`, `<`, `<=`, `()`.
**Rules:**
*   Condition must resolve to boolean.
*   Max nesting: 3 levels.
*   **Footer Rule:** If used inside `If`, it must exist in *both* `then` and `else` branches (or neither), and no footer can exist outside the `If`.

---

## Dynamic Components (Tutorial)

This pattern allows updating the UI (e.g., refreshing time slots) when a user interacts with a component (e.g., selects a date).

**Prerequisites:** Requires a Data Endpoint and `data_api_version: "3.0"`.

### Step 1: Define the Screen
Create a screen with a `DatePicker` and a `Dropdown`.

```json
{
  "version": "7.2",
  "data_api_version": "3.0",
  "routing_model": { "BOOKING": [] },
  "screens": [
    {
      "id": "BOOKING",
      "terminal": true,
      "title": "Booking appointment",
      "data": {
        "is_dropdown_visible": { "type": "boolean", "__example__": false },
        "available_slots": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": { "id": {"type": "string"}, "title": {"type": "string"} }
            },
            "__example__": []
        }
      },
      "layout": {
        "type": "SingleColumnLayout",
        "children": [
          {
            "type": "DatePicker",
            "name": "date",
            "label": "Select date",
            "on-select-action": {
                "name": "data_exchange",
                "payload": {
                    "date": "${form.date}",
                    "component_action": "update_date"
                }
            }
          },
          {
             "type": "Dropdown",
             "label": "Pick a slot",
             "name": "slot",
             "required": "${data.is_dropdown_visible}",
             "visible": "${data.is_dropdown_visible}",
             "data-source": "${data.available_slots}"
          },
          {
             "type": "Footer",
             "label": "Book",
             "on-click-action": { "name": "complete", "payload": {} }
          }
        ]
      }
    }
  ]
}
```

### Step 2: Server Response
When the user selects a date, the `on-select-action` triggers `data_exchange`. Your server should respond with the new data to update the screen state.

**Expected Server Response Payload:**
```json
{
  "version": "3.0",
  "screen": "BOOKING",
  "data": {
    "is_dropdown_visible": true,
    "available_slots": [
      { "id": "1", "title": "08:00" },
      { "id": "2", "title": "09:00" }
    ]
  }
}
```

---

## Common Patterns & Gotchas

### Required + Visible for Inputs

Many input and selection components (`TextInput`, `Dropdown`, `CheckboxGroup`,
`RadioButtonsGroup`, etc.) support both `required` and `visible`.

- **Important:** WhatsApp Flows validation will fail if a component is
  effectively hidden but marked as required (for example,
  `required: true` and `visible: false`).
- When you hide a component until data is ready, either:
  - keep `required` omitted or `false` while it is hidden and only validate on a
    later screen, or
  - bind `required` to the same condition as visibility, for example:
    `required: "${data.is_dropdown_visible}"`.

The **Dynamic Components (Tutorial)** above uses this pattern for the `Dropdown`
that is only required once it is visible.

### Dynamic dropdowns (invisible → visible)

For patterns where:

- The user first picks a date or filter.
- The endpoint returns a set of options.
- A dropdown becomes visible once options are available.

Recommended pattern:

1. In `data`, declare:
   - a boolean flag like `is_dropdown_visible` (default `false`),
   - an array like `available_slots` with the `{ id, title }` structure.
2. In the layout:
   - bind `visible` to `${data.is_dropdown_visible}`,
   - bind `data-source` to `${data.available_slots}`,
   - optionally bind `required` to the same visibility flag.
3. In the endpoint response:
   - set `is_dropdown_visible: true` when you have options,
   - populate `available_slots` with the list of choices.

This keeps validation rules consistent and avoids hidden-but-required inputs.

### Routing by action + screen

For data endpoints, prefer routing using:

- `data_exchange.action`: `"INIT"`, `"data_exchange"`, `"BACK"`,
- `data_exchange.screen`: the current screen ID.

Custom fields inside `data` (for example, `data.action`) can still be used as
secondary hints, but they should not replace the canonical
`action + screen` decision tree described in the **Data Endpoint Quick Start**.

---

# Additional Technical Reference

## Logic Component Details (`If`)

### Supported Operators Reference
The `condition` property supports specific operators and data types.

| Operator          | Symbol | Types Allowed           | Rules & Return Type                                                                                      |
| :---------------- | :----- | :---------------------- | :------------------------------------------------------------------------------------------------------- |
| **Parentheses**   | `()`   | Boolean, Number, String | Used to define precedence. <br> *Example:* `${form.opt} \|\| (${data.num} > 5)`                          |
| **Equal**         | `==`   | Boolean, Number, String | Both sides must be the same type. <br> *Example:* `${form.city} == 'London'`                             |
| **Not Equal**     | `!=`   | Boolean, Number, String | Both sides must be the same type. <br> *Example:* `${data.val} != 5`                                     |
| **AND**           | `&&`   | Boolean                 | Evaluates true only if both sides are true. High priority. <br> *Example:* `${form.opt} && ${data.bool}` |
| **OR**            | `\|\|` | Boolean                 | Evaluates true if at least one side is true. <br> *Example:* `${form.opt} \|\| ${data.bool}`             |
| **NOT**           | `!`    | Boolean                 | Negates the statement. <br> *Example:* `!(${data.num} > 5)`                                              |
| **Greater Than**  | `>`    | Number                  | *Example:* `${data.num} > 5`                                                                             |
| **Greater/Equal** | `>=`   | Number                  | *Example:* `${data.num} >= 5`                                                                            |
| **Less Than**     | `<`    | Number                  | *Example:* `${data.num} < 5`                                                                             |
| **Less/Equal**    | `<=`   | Number                  | *Example:* `${data.num} <= 5`                                                                            |

### Validation Errors & Limitations (`If`)
These are the specific validation errors you will encounter during Flow compilation if rules are violated.

| Scenario                                        | Validation Error Message                                                                           |
| :---------------------------------------------- | :------------------------------------------------------------------------------------------------- |
| Footer exists in `then`, but `else` is missing. | *Missing Footer inside one of the if branches. Branch "else" should exist and contain one Footer.* |
| Footer exists in `then`, but not in `else`.     | *Missing Footer inside one of the if branches.*                                                    |
| Footer exists in `else`, but not in `then`.     | *Missing Footer inside one of the if branches.*                                                    |
| Footer exists inside `If` AND outside `If`.     | *You can only have 1 Footer component per screen.*                                                 |
| The `then` array is empty.                      | *Invalid value found at: ".../then" due to empty array. It should contain at least one component.* |

---

## Logic Component Details (`Switch`)

### Validation Errors (`Switch`)

| Scenario                       | Validation Error Message                        |
| :----------------------------- | :---------------------------------------------- |
| The `cases` property is empty. | *Invalid empty property found at: ".../cases".* |

---

## Rich Text Best Practices

### Working with Large Texts
While `RichText` allows static text arrays, it is recommended to use **dynamic data** for large documents (like Terms of Service).
*   **Why?** Improves JSON readability and allows you to update the text from your server without changing the Flow JSON.
*   **How?** Send the markdown string as a normal string property in your data payload (no need to convert it to an array of strings).

**Example:**
```json
{
   "type": "RichText",
   "text": "${data.terms_of_service_content}"
}
```

---

## Navigation List: Specific Restrictions

While the general limits were provided, note these specific behaviors for `NavigationList`:

1.  **Image Placeholder:** If an image in the `start` object exceeds **100KB**, it will not be displayed; it will be replaced by a generic placeholder.
2.  **Truncation:**
    *   `label` content (>80 chars) will truncate.
    *   `description` content (>300 chars) will truncate.
    *   `list-items` content (>20 items) will not render if the limit is reached.
3.  **Action definition:** You cannot define `on-click-action` on **both** the component level and the item level simultaneously. It must be one or the other.

---

# UX & Content Best Practices

These guidelines are distilled from Meta’s Flows docs and are intended to
produce flows that feel fast, clear, and trustworthy.

## Flow Length & Screen Design

- **Keep flows short.** Design flows so a typical user can complete the main
  task in **under ~5 minutes**.
- **One primary task per screen.** Avoid screens that try to collect many
  unrelated inputs at once. If you need multiple tasks, split them into
  separate screens.
- **Limit components per screen.**
  - Too many components make the layout noisy and slow to load.
  - Consider what happens if a user leaves mid-flow: fewer components per
    screen means less data lost when they re-enter.
- **Use the right screen for the right task.**
  - If a sub-flow is needed (for example, “Forgot password”), keep it
    **small (≤ 3 screens)** and return the user to the main task afterwards.

## Initiation & Navigation

- **Initiation message should match the first screen.**
  - The chat message + CTA that opens the flow must clearly describe the task.
  - The first screen should immediately reflect that task—no surprises.
- **Set expectations up front.**
  - In either the chat copy or the first screen, indicate roughly how long it
    will take (for example, “This will take about 2–3 minutes.”).
- **Use clear, action-oriented titles.**
  - Examples: “Book appointment”, “Confirm details”, “Update contact info”.
  - Use titles to show progress where it helps, for example “Step 1 of 3”.
- **Always end with a summary / confirmation screen.**
  - Show what the user is about to submit (or what was submitted).
  - Make the final CTA explicit, for example “Confirm booking”.

## CTAs, Copy & Style

- **CTAs should describe the outcome.**
  - Good: “Confirm booking”, “Submit application”.
  - Weak: “Continue”, “Next”.
- **Use sentence case consistently.**
  - Prefer “Book appointment” over “BOOK APPOINTMENT”.
- **Use emojis sparingly.**
  - Only when they add clarity or match brand tone.
  - Avoid them in critical or highly formal flows.
- **Avoid redundant copy.**
  - Don’t repeat the same phrase in title and body without adding information
    (for example, avoid “Complete registration” and then “Complete registration
    below”).

## Forms & Input Quality

- **Choose the appropriate component:**
  - Use `DatePicker` / `CalendarPicker` for dates (not free-text).
  - Use `TextArea` for long free-text answers.
  - Use `Dropdown` / `RadioButtonsGroup` / `CheckboxGroup` instead of free text
    when the set of options is known.
- **Order fields logically.**
  - For example: first name → last name → email → phone.
- **Make non-critical fields optional.**
  - Only mark fields as required if they are truly needed to complete the task.
- **Use helper text for tricky fields.**
  - Example: phone number formats, password rules, date formats.

## Options & Lists

- **Keep option lists small.**
  - Aim for **≤ 10 options per screen** when possible.
- **Pick the right selection component:**
  - Use **RadioButtons** when the user must pick exactly one option.
  - Use **CheckboxGroup** when multiple selections are allowed.
  - Use **Dropdown** when there are many options (Meta recommends using it
    when there are ~8 or more choices).
- **Use sensible defaults.**
  - Where appropriate, make the first option (or the most common one) the
    default selection.

## Error Handling & Validation UX

- **Errors should say what happened and how to fix it.**
  - For example: “This email looks invalid. Please check the format.” instead
    of just “Error”.
- **Show validation rules up front.**
  - Use helper text for passwords, date formats, numeric ranges, etc.
- **Prefer staying in-flow on errors.**
  - When endpoint data becomes invalid (for example, a slot becomes
    unavailable), send the user back to the previous relevant screen with a
    clear error message rather than ending the flow abruptly.

## Login & Trust

- **Use login screens only when necessary.**
  - Logging in can feel heavy inside a flow; only require it when the task
    truly needs authentication.
- **Place login later in the flow.**
  - Show value first (for example, show summary or available options), then
    prompt for login as one of the last steps before completion.
- **Maintain sense of place.**
  - Make it clear that login is still part of the same flow, not an external
    redirect.
- **Make support easy to reach.**
  - Provide a way (inside the flow or in follow-up messages) for users to
    contact support if something goes wrong.

## Termination & Follow-up

- **Clearly describe what happens after completion.**
  - The last screen should confirm the action and set expectations for what
    happens next (for example, “We’ll send a confirmation email shortly.”).
- **Keep completion payloads lean.**
  - Only send data that is needed downstream; avoid huge payloads or embedded
    images in completion responses.
- **Bookend with a chat message.**
  - After the Flow completes, send a human-readable message to the chat that
    summarizes the outcome and provides next steps or support information.
  - Combine this with the built-in summary behavior and `sensitive` fields when
    appropriate.

## Writing & Formatting

- **Use a clear content hierarchy.**
  - Use headings for the main point, body text for explanation, and captions
    for small hints or secondary information.
- **Format data appropriately.**
  - Use correct currency symbols, phone number formats, and localized date/time
    formats that match the user’s expectations.
- **Check grammar and spelling.**
  - Read flows end-to-end before publishing; keep terminology and
    capitalization consistent.
```

## File: `skills/integrate-whatsapp/scripts/create-flow.js`
```javascript
#!/usr/bin/env node
const { parseArgs, getStringFlag, getBooleanFlag, readFlagJson } = require('./lib/cli');
const { platformRequest } = require('./lib/http');
const { run } = require('./lib/run');

run(async () => {
  const { flags } = parseArgs(process.argv.slice(2));
  const phoneNumberId = getStringFlag(flags, 'phone-number-id') || getStringFlag(flags, 'phone_number_id');
  if (!phoneNumberId) {
    throw new Error('Missing required flag --phone-number-id');
  }

  const name = getStringFlag(flags, 'name');
  const publish = getBooleanFlag(flags, 'publish');
  const flowJson = await readFlagJson(flags, 'flow-json', 'flow-json-file');

  const body = {
    phone_number_id: phoneNumberId
  };

  if (name) body.name = name;
  if (flowJson) body.flow_json = flowJson;
  if (publish) body.publish = true;

  return platformRequest({
    method: 'POST',
    path: '/platform/v1/whatsapp/flows',
    body
  });
});
```

## File: `skills/integrate-whatsapp/scripts/create-function.js`
```javascript
#!/usr/bin/env node
const { parseArgs, requireStringFlag, getStringFlag, readFlagText, readFlagJson } = require('./lib/cli');
const { platformRequest } = require('./lib/http');
const { run } = require('./lib/run');

run(async () => {
  const { flags } = parseArgs(process.argv.slice(2));
  const name = requireStringFlag(flags, 'name');
  const code = await readFlagText(flags, 'code', 'code-file');

  if (!code) {
    throw new Error('Missing --code or --code-file');
  }

  const runtimeConfig = await readFlagJson(flags, 'runtime-config', 'runtime-config-file');

  const body = {
    function: {
      name,
      code,
      description: getStringFlag(flags, 'description'),
      runtime_config: runtimeConfig
    }
  };

  return platformRequest({
    method: 'POST',
    path: '/platform/v1/functions',
    body
  });
});
```

## File: `skills/integrate-whatsapp/scripts/create-template.mjs`
```
import { loadJsonPayload, parseArgs, requireFlag } from './lib/args.mjs';
import { metaProxyRequest } from './lib/request.mjs';
import { err, ok, printResult } from './lib/output.mjs';

function usage() {
  return {
    usage: 'node scripts/create-template.mjs --business-account-id <WABA_ID> --json <payload> | --file <path>',
    env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY', 'META_GRAPH_VERSION (optional)'],
    hints: [
      'To discover business_account_id (WABA), run: node scripts/list-platform-phone-numbers.mjs',
      'Start from an asset payload in assets/ (template definitions) and adjust name/text/examples.'
    ]
  };
}

async function main() {
  const { flags, errors } = parseArgs(process.argv.slice(2));
  if (flags.help) {
    return printResult(ok(usage()));
  }
  if (errors.length > 0) {
    return printResult(err('Invalid arguments', { errors, ...usage() }));
  }

  try {
    const businessAccountId = requireFlag(flags, ['business-account-id', 'business_account_id'], 'business-account-id');
    const payload = await loadJsonPayload(flags);

    const response = await metaProxyRequest({
      method: 'POST',
      path: `${businessAccountId}/message_templates`,
      body: JSON.stringify(payload)
    });

    if (!response.ok) {
      return printResult(err('Meta proxy request failed', { response }));
    }

    return printResult(ok({ response }));
  } catch (error) {
    return printResult(err('Failed to create template', { message: String(error?.message || error), ...usage() }));
  }
}

main().then((code) => process.exit(code));
```

## File: `skills/integrate-whatsapp/scripts/create.js`
```javascript
const { kapsoConfigFromEnv, kapsoRequest } = require('./lib/webhooks/kapso-api');
const { hasHelpFlag, parseFlags, requireFlag } = require('./lib/webhooks/args');
const { buildWebhookPayload } = require('./lib/webhooks/webhook');

function ok(data) {
  return { ok: true, data };
}

function err(message, details) {
  return { ok: false, error: { message, details } };
}

function resolveScope(flags) {
  const raw = flags.scope;
  if (!raw || raw === true) {
    return 'config';
  }
  const scope = String(raw);
  if (scope !== 'config' && scope !== 'project') {
    throw new Error(`Invalid --scope value: ${scope}`);
  }
  return scope;
}

async function main() {
  const argv = process.argv.slice(2);
  if (hasHelpFlag(argv)) {
    console.log(
      JSON.stringify(
        {
          ok: true,
          usage:
            'node scripts/create.js --url <https://...> --events <csv|json-array> [--phone-number-id <id>] [--scope config|project] [--kind <kapso|meta>] [--payload-version v1|v2] [--buffer-enabled true|false] [--buffer-window-seconds <n>] [--max-buffer-size <n>] [--inactivity-minutes <n>] [--headers <json>] [--active true|false]',
          env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
        },
        null,
        2
      )
    );
    return 0;
  }

  try {
    const flags = parseFlags(argv);
    const scope = resolveScope(flags);
    const payload = buildWebhookPayload(flags);
    if (!payload.url) {
      throw new Error('Missing required flag --url');
    }
    if (!payload.events) {
      throw new Error('Missing required flag --events');
    }

    const config = kapsoConfigFromEnv();
    let path = '';
    const body = { whatsapp_webhook: payload };

    if (scope === 'project') {
      const phoneNumberId = flags['phone-number-id'];
      if (phoneNumberId && phoneNumberId !== true) {
        body.whatsapp_webhook.phone_number_id = phoneNumberId;
      }
      path = '/platform/v1/whatsapp/webhooks';
    } else {
      const phoneNumberId = requireFlag(flags, 'phone-number-id');
      path = `/platform/v1/whatsapp/phone_numbers/${encodeURIComponent(phoneNumberId)}/webhooks`;
    }

    const data = await kapsoRequest(config, path, {
      method: 'POST',
      body: JSON.stringify(body)
    });

    console.log(JSON.stringify(ok(data), null, 2));
    return 0;
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    console.error(JSON.stringify(err('Command failed', { message }), null, 2));
    return 1;
  }
}

main().then((code) => process.exit(code));
```

## File: `skills/integrate-whatsapp/scripts/delete-flow.js`
```javascript
#!/usr/bin/env node
const { parseArgs } = require('./lib/cli');
const { metaRequest } = require('./lib/http');
const { run } = require('./lib/run');
const { requireFlowId, buildScopeQuery } = require('./lib/whatsapp-flow');

run(async () => {
  const { flags } = parseArgs(process.argv.slice(2));
  const flowId = requireFlowId(flags);
  const query = buildScopeQuery(flags);

  return metaRequest({
    method: 'DELETE',
    path: `/flows/${flowId}`,
    query
  });
});
```

## File: `skills/integrate-whatsapp/scripts/delete.js`
```javascript
const { kapsoConfigFromEnv, kapsoRequest } = require('./lib/webhooks/kapso-api');
const { hasHelpFlag, parseFlags, requireFlag } = require('./lib/webhooks/args');

function ok(data) {
  return { ok: true, data };
}

function err(message, details) {
  return { ok: false, error: { message, details } };
}

function resolveScope(flags) {
  const raw = flags.scope;
  if (!raw || raw === true) {
    return 'config';
  }
  const scope = String(raw);
  if (scope !== 'config' && scope !== 'project') {
    throw new Error(`Invalid --scope value: ${scope}`);
  }
  return scope;
}

async function main() {
  const argv = process.argv.slice(2);
  if (hasHelpFlag(argv)) {
    console.log(
      JSON.stringify(
        {
          ok: true,
          usage:
            'node scripts/delete.js --webhook-id <id> [--phone-number-id <id>] [--scope config|project]',
          env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
        },
        null,
        2
      )
    );
    return 0;
  }

  try {
    const flags = parseFlags(argv);
    const scope = resolveScope(flags);
    const webhookId = requireFlag(flags, 'webhook-id');
    const config = kapsoConfigFromEnv();
    let path = '';
    if (scope === 'project') {
      path = `/platform/v1/whatsapp/webhooks/${encodeURIComponent(webhookId)}`;
    } else {
      const phoneNumberId = requireFlag(flags, 'phone-number-id');
      path = `/platform/v1/whatsapp/phone_numbers/${encodeURIComponent(phoneNumberId)}/webhooks/${encodeURIComponent(webhookId)}`;
    }

    const data = await kapsoRequest(config, path, { method: 'DELETE' });

    console.log(JSON.stringify(ok(data), null, 2));
    return 0;
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    console.error(JSON.stringify(err('Command failed', { message }), null, 2));
    return 1;
  }
}

main().then((code) => process.exit(code));
```

## File: `skills/integrate-whatsapp/scripts/deploy-data-endpoint.js`
```javascript
#!/usr/bin/env node
const { parseArgs } = require('./lib/cli');
const { platformRequest } = require('./lib/http');
const { run } = require('./lib/run');
const { requireFlowId } = require('./lib/whatsapp-flow');

run(async () => {
  const { flags } = parseArgs(process.argv.slice(2));
  const flowId = requireFlowId(flags);

  return platformRequest({
    method: 'POST',
    path: `/platform/v1/whatsapp/flows/${flowId}/data_endpoint/deploy`
  });
});
```

## File: `skills/integrate-whatsapp/scripts/deploy-function.js`
```javascript
#!/usr/bin/env node
const { parseArgs, requireStringFlag } = require('./lib/cli');
const { platformRequest } = require('./lib/http');
const { run } = require('./lib/run');

run(async () => {
  const { flags } = parseArgs(process.argv.slice(2));
  const functionId = requireStringFlag(flags, 'function-id');

  return platformRequest({
    method: 'POST',
    path: `/platform/v1/functions/${functionId}/deploy`
  });
});
```

## File: `skills/integrate-whatsapp/scripts/get-data-endpoint.js`
```javascript
#!/usr/bin/env node
const { parseArgs } = require('./lib/cli');
const { platformRequest } = require('./lib/http');
const { run } = require('./lib/run');
const { requireFlowId } = require('./lib/whatsapp-flow');

run(async () => {
  const { flags } = parseArgs(process.argv.slice(2));
  const flowId = requireFlowId(flags);

  return platformRequest({
    method: 'GET',
    path: `/platform/v1/whatsapp/flows/${flowId}/data_endpoint`
  });
});
```

## File: `skills/integrate-whatsapp/scripts/get-encryption-status.js`
```javascript
#!/usr/bin/env node
const { parseArgs, requireStringFlag } = require('./lib/cli');
const { platformRequest } = require('./lib/http');
const { run } = require('./lib/run');

run(async () => {
  const { flags } = parseArgs(process.argv.slice(2));
  const phoneNumberId = requireStringFlag(flags, 'phone-number-id');

  return platformRequest({
    method: 'GET',
    path: `/platform/v1/whatsapp/phone_numbers/${phoneNumberId}`
  });
});
```

## File: `skills/integrate-whatsapp/scripts/get-flow.js`
```javascript
#!/usr/bin/env node
const { parseArgs } = require('./lib/cli');
const { platformRequest } = require('./lib/http');
const { run } = require('./lib/run');
const { requireFlowId } = require('./lib/whatsapp-flow');

run(async () => {
  const { flags } = parseArgs(process.argv.slice(2));
  const flowId = requireFlowId(flags);

  return platformRequest({
    method: 'GET',
    path: `/platform/v1/whatsapp/flows/${flowId}`
  });
});
```

## File: `skills/integrate-whatsapp/scripts/get-function.js`
```javascript
#!/usr/bin/env node
const { parseArgs, requireStringFlag } = require('./lib/cli');
const { platformRequest } = require('./lib/http');
const { run } = require('./lib/run');

run(async () => {
  const { flags } = parseArgs(process.argv.slice(2));
  const functionId = requireStringFlag(flags, 'function-id');

  return platformRequest({
    method: 'GET',
    path: `/platform/v1/functions/${functionId}`
  });
});
```

## File: `skills/integrate-whatsapp/scripts/get.js`
```javascript
const { kapsoConfigFromEnv, kapsoRequest } = require('./lib/webhooks/kapso-api');
const { hasHelpFlag, parseFlags, requireFlag } = require('./lib/webhooks/args');

function ok(data) {
  return { ok: true, data };
}

function err(message, details) {
  return { ok: false, error: { message, details } };
}

function resolveScope(flags) {
  const raw = flags.scope;
  if (!raw || raw === true) {
    return 'config';
  }
  const scope = String(raw);
  if (scope !== 'config' && scope !== 'project') {
    throw new Error(`Invalid --scope value: ${scope}`);
  }
  return scope;
}

async function main() {
  const argv = process.argv.slice(2);
  if (hasHelpFlag(argv)) {
    console.log(
      JSON.stringify(
        {
          ok: true,
          usage:
            'node scripts/get.js --webhook-id <id> [--phone-number-id <id>] [--scope config|project]',
          env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
        },
        null,
        2
      )
    );
    return 0;
  }

  try {
    const flags = parseFlags(argv);
    const scope = resolveScope(flags);
    const webhookId = requireFlag(flags, 'webhook-id');
    const config = kapsoConfigFromEnv();
    let path = '';
    if (scope === 'project') {
      path = `/platform/v1/whatsapp/webhooks/${encodeURIComponent(webhookId)}`;
    } else {
      const phoneNumberId = requireFlag(flags, 'phone-number-id');
      path = `/platform/v1/whatsapp/phone_numbers/${encodeURIComponent(phoneNumberId)}/webhooks/${encodeURIComponent(webhookId)}`;
    }

    const data = await kapsoRequest(config, path);

    console.log(JSON.stringify(ok(data), null, 2));
    return 0;
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    console.error(JSON.stringify(err('Command failed', { message }), null, 2));
    return 1;
  }
}

main().then((code) => process.exit(code));
```

## File: `skills/integrate-whatsapp/scripts/list-connected-numbers.mjs`
```
import { parseArgs, requireFlag } from './lib/args.mjs';
import { metaProxyRequest } from './lib/request.mjs';
import { err, ok, printResult } from './lib/output.mjs';

function usage() {
  return {
    usage: 'node scripts/list-connected-numbers.mjs --business-account-id <WABA_ID>',
    env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY', 'META_GRAPH_VERSION (optional)'],
    hints: [
      'To discover business_account_id (WABA) and phone_number_id, run: node scripts/list-platform-phone-numbers.mjs',
      'Platform API equivalent: GET /platform/v1/whatsapp/phone_numbers'
    ]
  };
}

async function main() {
  const { flags, errors } = parseArgs(process.argv.slice(2));
  if (flags.help) {
    return printResult(ok(usage()));
  }
  if (errors.length > 0) {
    return printResult(err('Invalid arguments', { errors, ...usage() }));
  }

  try {
    const businessAccountId = requireFlag(flags, ['business-account-id', 'business_account_id'], 'business-account-id');
    const response = await metaProxyRequest({
      method: 'GET',
      path: `${businessAccountId}/phone_numbers`
    });

    if (!response.ok) {
      return printResult(err('Meta proxy request failed', { response }));
    }

    return printResult(ok({ response }));
  } catch (error) {
    return printResult(err('Failed to list connected numbers', { message: String(error?.message || error), ...usage() }));
  }
}

main().then((code) => process.exit(code));
```

## File: `skills/integrate-whatsapp/scripts/list-flow-responses.js`
```javascript
#!/usr/bin/env node
const { parseArgs, getNumberFlag } = require('./lib/cli');
const { platformRequest } = require('./lib/http');
const { run } = require('./lib/run');
const { requireFlowId } = require('./lib/whatsapp-flow');

run(async () => {
  const { flags } = parseArgs(process.argv.slice(2));
  const flowId = requireFlowId(flags);

  const query = {
    page: getNumberFlag(flags, 'page'),
    per_page: getNumberFlag(flags, 'per-page')
  };

  return platformRequest({
    method: 'GET',
    path: `/platform/v1/whatsapp/flows/${flowId}/responses`,
    query
  });
});
```

## File: `skills/integrate-whatsapp/scripts/list-flows.js`
```javascript
#!/usr/bin/env node
const { parseArgs, getStringFlag, getNumberFlag } = require('./lib/cli');
const { platformRequest } = require('./lib/http');
const { run } = require('./lib/run');

run(async () => {
  const { flags } = parseArgs(process.argv.slice(2));
  const phoneNumberId = getStringFlag(flags, 'phone-number-id') || getStringFlag(flags, 'phone_number_id');

  const query = {
    status: getStringFlag(flags, 'status'),
    business_account_id: getStringFlag(flags, 'business-account-id'),
    phone_number_id: phoneNumberId,
    name_contains: getStringFlag(flags, 'name-contains'),
    created_after: getStringFlag(flags, 'created-after'),
    created_before: getStringFlag(flags, 'created-before'),
    page: getNumberFlag(flags, 'page'),
    per_page: getNumberFlag(flags, 'per-page')
  };

  return platformRequest({
    method: 'GET',
    path: '/platform/v1/whatsapp/flows',
    query
  });
});
```

## File: `skills/integrate-whatsapp/scripts/list-function-invocations.js`
```javascript
#!/usr/bin/env node
const { parseArgs, getStringFlag, getNumberFlag } = require('./lib/cli');
const { platformRequest } = require('./lib/http');
const { run } = require('./lib/run');

run(async () => {
  const { flags } = parseArgs(process.argv.slice(2));
  const functionId = getStringFlag(flags, 'function-id');
  const flowId = getStringFlag(flags, 'flow-id');

  if (!functionId && !flowId) {
    throw new Error('Provide --function-id or --flow-id');
  }

  if (functionId && flowId) {
    throw new Error('Provide only one of --function-id or --flow-id');
  }

  const query = {
    status: getStringFlag(flags, 'status'),
    limit: getNumberFlag(flags, 'limit')
  };

  return platformRequest({
    method: 'GET',
    path: functionId
      ? `/platform/v1/functions/${functionId}/invocations`
      : `/platform/v1/whatsapp/flows/${flowId}/function_invocations`,
    query
  });
});
```

## File: `skills/integrate-whatsapp/scripts/list-function-logs.js`
```javascript
#!/usr/bin/env node
const { parseArgs, getNumberFlag } = require('./lib/cli');
const { platformRequest } = require('./lib/http');
const { run } = require('./lib/run');
const { requireFlowId } = require('./lib/whatsapp-flow');

run(async () => {
  const { flags } = parseArgs(process.argv.slice(2));
  const flowId = requireFlowId(flags);

  const query = {
    limit: getNumberFlag(flags, 'limit')
  };

  return platformRequest({
    method: 'GET',
    path: `/platform/v1/whatsapp/flows/${flowId}/function_logs`,
    query
  });
});
```

## File: `skills/integrate-whatsapp/scripts/list-platform-phone-numbers.mjs`
```
import { getFlag, parseArgs } from './lib/args.mjs';
import { err, ok, printResult } from './lib/output.mjs';

function usage() {
  return {
    usage: 'node scripts/list-platform-phone-numbers.mjs [--page <n>] [--per-page <n>] [--phone-number-id <id>] [--business-account-id <id>]',
    env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY'],
    notes: [
      'This calls the Platform API: GET /platform/v1/whatsapp/phone_numbers.',
      'Use this to discover business_account_id (WABA) and phone_number_id (Meta phone number id).'
    ]
  };
}

function requireEnv(name) {
  const value = process.env[name];
  if (!value) {
    throw new Error(`Missing required env var: ${name}`);
  }
  return value;
}

function normalizePlatformBase(raw) {
  const trimmed = raw.replace(/\/+$/, '');
  if (trimmed.endsWith('/platform/v1')) {
    return trimmed.slice(0, -'/platform/v1'.length);
  }
  const metaIndex = trimmed.indexOf('/meta');
  if (metaIndex >= 0) {
    return trimmed.slice(0, metaIndex);
  }
  return trimmed;
}

function buildUrl(path, query) {
  const baseUrl = normalizePlatformBase(requireEnv('KAPSO_API_BASE_URL'));
  const cleanedPath = path.replace(/^\/+/, '');
  const url = new URL(`${baseUrl}/platform/v1/${cleanedPath}`);

  if (query) {
    Object.entries(query).forEach(([key, value]) => {
      if (value === undefined || value === null || value === '') return;
      url.searchParams.set(key, String(value));
    });
  }

  return url;
}

function shouldParseJson(contentType) {
  return contentType && contentType.toLowerCase().includes('application/json');
}

async function platformRequest({ method, path, query }) {
  const apiKey = requireEnv('KAPSO_API_KEY');
  const url = buildUrl(path, query);
  const headers = new Headers();

  headers.set('X-API-Key', apiKey);

  const response = await fetch(url, { method, headers });
  const contentType = response.headers.get('content-type') || '';
  const text = await response.text();
  let data = text;

  if (text && shouldParseJson(contentType)) {
    try {
      data = JSON.parse(text);
    } catch {
      data = text;
    }
  }

  return {
    ok: response.ok,
    status: response.status,
    url: url.toString(),
    data
  };
}

function summarizeIds(platformResponse) {
  const configs = platformResponse?.data?.data;
  if (!Array.isArray(configs)) return [];

  return configs.map((config) => ({
    name: config.name,
    display_phone_number: config.display_phone_number,
    phone_number_id: config.phone_number_id || config.id,
    business_account_id: config.business_account_id
  }));
}

async function main() {
  const { flags, errors } = parseArgs(process.argv.slice(2));
  if (flags.help) {
    return printResult(ok(usage()));
  }
  if (errors.length > 0) {
    return printResult(err('Invalid arguments', { errors, ...usage() }));
  }

  try {
    const query = {
      page: getFlag(flags, ['page']),
      per_page: getFlag(flags, ['per-page', 'per_page']),
      phone_number_id: getFlag(flags, ['phone-number-id', 'phone_number_id']),
      business_account_id: getFlag(flags, ['business-account-id', 'business_account_id'])
    };

    const response = await platformRequest({
      method: 'GET',
      path: 'whatsapp/phone_numbers',
      query
    });

    if (!response.ok) {
      return printResult(err('Platform API request failed', { response, ...usage() }));
    }

    return printResult(ok({ response, ids: summarizeIds(response) }));
  } catch (error) {
    return printResult(err('Failed to list platform WhatsApp phone numbers', { message: String(error?.message || error), ...usage() }));
  }
}

main().then((code) => process.exit(code));

```

## File: `skills/integrate-whatsapp/scripts/list-templates.mjs`
```
import { parseArgs, parseJsonFlag, requireFlag } from './lib/args.mjs';
import { metaProxyRequest } from './lib/request.mjs';
import { err, ok, printResult } from './lib/output.mjs';

function usage() {
  return {
    usage: 'node scripts/list-templates.mjs --business-account-id <WABA_ID> [--name <name>] [--status <status>] [--category <category>] [--language <lang>] [--fields <fields>] [--limit <n>] [--after <cursor>] [--before <cursor>] [--query <json>]',
    env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY', 'META_GRAPH_VERSION (optional)'],
    hints: [
      'To discover business_account_id (WABA) and phone_number_id, run: node scripts/list-platform-phone-numbers.mjs',
      'Platform API equivalent: GET /platform/v1/whatsapp/phone_numbers'
    ]
  };
}

async function main() {
  const { flags, errors } = parseArgs(process.argv.slice(2));
  if (flags.help) {
    return printResult(ok(usage()));
  }
  if (errors.length > 0) {
    return printResult(err('Invalid arguments', { errors, ...usage() }));
  }

  try {
    const businessAccountId = requireFlag(flags, ['business-account-id', 'business_account_id'], 'business-account-id');
    const query = {
      name: flags.name,
      status: flags.status,
      category: flags.category,
      language: flags.language,
      fields: flags.fields,
      limit: flags.limit,
      after: flags.after,
      before: flags.before
    };

    const extraQuery = parseJsonFlag(flags, 'query');
    const mergedQuery = extraQuery ? { ...query, ...extraQuery } : query;

    const response = await metaProxyRequest({
      method: 'GET',
      path: `${businessAccountId}/message_templates`,
      query: mergedQuery
    });

    if (!response.ok) {
      return printResult(err('Meta proxy request failed', { response }));
    }

    return printResult(ok({ response }));
  } catch (error) {
    return printResult(err('Failed to list templates', { message: String(error?.message || error), ...usage() }));
  }
}

main().then((code) => process.exit(code));
```

## File: `skills/integrate-whatsapp/scripts/list.js`
```javascript
const { kapsoConfigFromEnv, kapsoRequest } = require('./lib/webhooks/kapso-api');
const { hasHelpFlag, parseFlags, requireFlag } = require('./lib/webhooks/args');

function ok(data) {
  return { ok: true, data };
}

function err(message, details) {
  return { ok: false, error: { message, details } };
}

function resolveScope(flags) {
  const raw = flags.scope;
  if (!raw || raw === true) {
    return 'config';
  }
  const scope = String(raw);
  if (scope !== 'config' && scope !== 'project') {
    throw new Error(`Invalid --scope value: ${scope}`);
  }
  return scope;
}

async function main() {
  const argv = process.argv.slice(2);
  if (hasHelpFlag(argv)) {
    console.log(
      JSON.stringify(
        {
          ok: true,
          usage:
            'node scripts/list.js --phone-number-id <id> [--scope config|project] [--kind <kapso|meta>] [--page <n>] [--per-page <n>]',
          env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
        },
        null,
        2
      )
    );
    return 0;
  }

  try {
    const flags = parseFlags(argv);
    const scope = resolveScope(flags);
    const config = kapsoConfigFromEnv();
    let path = '';
    const params = new URLSearchParams();
    if (flags.kind) params.set('kind', flags.kind);
    if (flags.page) params.set('page', flags.page);
    if (flags['per-page']) params.set('per_page', flags['per-page']);
    if (scope === 'project') {
      path = '/platform/v1/whatsapp/webhooks';
    } else {
      const phoneNumberId = requireFlag(flags, 'phone-number-id');
      path = `/platform/v1/whatsapp/phone_numbers/${encodeURIComponent(phoneNumberId)}/webhooks`;
    }

    const suffix = params.toString();
    const data = await kapsoRequest(config, `${path}${suffix ? `?${suffix}` : ''}`);

    console.log(JSON.stringify(ok(data), null, 2));
    return 0;
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    console.error(JSON.stringify(err('Command failed', { message }), null, 2));
    return 1;
  }
}

main().then((code) => process.exit(code));
```

## File: `skills/integrate-whatsapp/scripts/openapi-explore.mjs`
```
#!/usr/bin/env node

import { readFileSync, readdirSync, statSync } from 'fs'
import path from 'path'
import { fileURLToPath } from 'url'
import { parse as parseYaml } from 'yaml'

const HTTP_METHODS = ['get', 'post', 'put', 'patch', 'delete', 'options', 'head']
const DEFAULT_PUBLISHED_WHATSAPP_OPENAPI = 'https://docs.kapso.ai/api/meta/whatsapp/openapi-whatsapp.yaml'
const SCRIPT_DIR = path.dirname(fileURLToPath(import.meta.url))

function printHelp(exitCode = 0) {
  const msg = `
Explore OpenAPI specs (YAML)

Usage:
  node openapi-explore.mjs [openapi.yaml ...] <command> [args]
  node openapi-explore.mjs [--file <path> ...] <command> [args]
  node openapi-explore.mjs --all <command> [args]

Default (no files passed):
  Loads the published OpenAPI files from docs.kapso.ai:
  - ${DEFAULT_PUBLISHED_WHATSAPP_OPENAPI}
  - (plus platform + workflows, deduced from that URL)

Fallback:
  If it can't fetch the published specs (offline, etc.), it falls back to local repo files:
  api/**/openapi-*.yaml

Use --all to force local auto-discovery.

Commands:
  specs
  tags [--spec <id>]
  ops [--spec <id>] [--tag <tag>] [--q <query>]
  search <query> [--spec <id>]
  op <operationId | specId:operationId | "METHOD /path"> [--spec <id>]
  schema <SchemaName | specId:SchemaName> [--spec <id>]
  where <SchemaName | specId:SchemaName> [--spec <id>]

Flags:
  --file, -f <path>     Load a spec file (repeatable)
  --all                 Load all api/**/openapi-*.yaml files
  --spec <id>           Filter by spec id (platform, workflows, whatsapp, ...)
  --json                Output JSON (search/ops/where)
  --limit <n>           Limit results (default 30)
`
  console.log(msg.trim())
  process.exit(exitCode)
}

function die(msg, exitCode = 1) {
  console.error(msg)
  process.exit(exitCode)
}

function parseArgs(argv) {
  const args = [...argv]
  const opts = { files: [], all: false, spec: null, json: false, limit: 30, tag: null, q: null }
  let command = null
  const rest = []

  for (let i = 0; i < args.length; i++) {
    const a = args[i]
    if (a === '--help' || a === '-h') printHelp(0)

    if (a === '--all') {
      opts.all = true
      continue
    }
    if (a === '--json') {
      opts.json = true
      continue
    }
    if (a === '--file' || a === '-f') {
      const p = args[++i]
      if (!p) die('Missing value for --file')
      opts.files.push(p)
      continue
    }
    if (a === '--spec') {
      opts.spec = args[++i] || null
      if (!opts.spec) die('Missing value for --spec')
      continue
    }
    if (a === '--limit') {
      const raw = args[++i]
      const n = Number(raw)
      if (!Number.isFinite(n) || n <= 0) die(`Invalid --limit: ${raw}`)
      opts.limit = n
      continue
    }
    if (a === '--tag') {
      opts.tag = args[++i] || null
      if (!opts.tag) die('Missing value for --tag')
      continue
    }
    if (a === '--q') {
      opts.q = args[++i] || null
      if (!opts.q) die('Missing value for --q')
      continue
    }

    if (!command && (a.endsWith('.yaml') || a.endsWith('.yml'))) {
      opts.files.push(a)
      continue
    }

    if (!command) command = a
    else rest.push(a)
  }

  return { opts, command, rest }
}

function walk(dir, { filePattern, maxDepth = 10 } = {}, depth = 0, out = []) {
  if (depth > maxDepth) return out
  let entries
  try {
    entries = readdirSync(dir)
  } catch {
    return out
  }

  for (const entry of entries) {
    const full = path.join(dir, entry)
    let st
    try {
      st = statSync(full)
    } catch {
      continue
    }

    if (st.isDirectory()) {
      walk(full, { filePattern, maxDepth }, depth + 1, out)
    } else if (!filePattern || filePattern.test(entry)) {
      out.push(full)
    }
  }

  return out
}

function findUpDir(startDir, targetDirName, { maxDepth = 12 } = {}) {
  let current = path.resolve(startDir)
  for (let i = 0; i <= maxDepth; i++) {
    const candidate = path.join(current, targetDirName)
    try {
      const st = statSync(candidate)
      if (st.isDirectory()) return candidate
    } catch {
      // ignore
    }

    const parent = path.dirname(current)
    if (parent === current) break
    current = parent
  }
  return null
}

function findLocalApiDir() {
  return findUpDir(process.cwd(), 'api') || findUpDir(SCRIPT_DIR, 'api')
}

function isUrl(s) {
  return /^https?:\/\//i.test(String(s))
}

function deducePublishedOpenApiUrls(whatsappUrl = DEFAULT_PUBLISHED_WHATSAPP_OPENAPI) {
  const u = new URL(whatsappUrl)
  const origin = u.origin
  return [
    whatsappUrl,
    new URL('/api/platform/v1/openapi-platform.yaml', origin).toString(),
    new URL('/api/platform/v1/openapi-workflows.yaml', origin).toString(),
  ]
}

function inferSpecId(filePath, spec) {
  const base = (isUrl(filePath) ? path.basename(new URL(filePath).pathname) : path.basename(filePath)).toLowerCase()
  if (base.includes('whatsapp')) return 'whatsapp'
  if (base.includes('workflows')) return 'workflows'
  if (base.includes('platform')) return 'platform'

  const title = (spec?.info?.title || '').toLowerCase()
  if (title.includes('whatsapp')) return 'whatsapp'
  if (title.includes('workflow')) return 'workflows'
  if (title.includes('platform')) return 'platform'

  return base.replace(/^openapi-/, '').replace(/\.(ya?ml)$/, '') || 'spec'
}

function decodeJsonPointerToken(token) {
  return token.replaceAll('~1', '/').replaceAll('~0', '~')
}

function getByJsonPointer(doc, pointer) {
  if (!pointer || !pointer.startsWith('#/')) return null
  const parts = pointer.slice(2).split('/').map(decodeJsonPointerToken)
  let cur = doc
  for (const part of parts) {
    if (cur == null) return null
    cur = cur[part]
  }
  return cur ?? null
}

function refName(ref) {
  if (!ref) return null
  const parts = String(ref).split('/')
  return parts[parts.length - 1] || null
}

function derefObject(obj, doc, stack = new Set()) {
  if (!obj?.$ref) return obj
  const ref = String(obj.$ref)
  if (stack.has(ref)) return obj
  stack.add(ref)
  const resolved = getByJsonPointer(doc, ref)
  if (!resolved) return obj
  return derefObject(resolved, doc, stack)
}

function schemaTypeString(schema) {
  if (!schema) return 'any'
  if (schema.$ref) return refName(schema.$ref) || 'ref'
  if (schema.const !== undefined) return `const ${JSON.stringify(schema.const)}`
  if (schema.enum?.length) {
    const vals = schema.enum.slice(0, 6).map((v) => JSON.stringify(v)).join(' | ')
    return schema.enum.length > 6 ? `enum(${vals} | ...)` : `enum(${vals})`
  }
  if (schema.type) {
    if (Array.isArray(schema.type)) return schema.type.join('|')
    return schema.type
  }
  if (schema.oneOf) return 'oneOf'
  if (schema.anyOf) return 'anyOf'
  if (schema.allOf) return 'allOf'
  if (schema.properties) return 'object'
  if (schema.items) return 'array'
  return 'any'
}

function normalizeType(schema) {
  if (!schema) return null
  const t = schema.type
  if (!t) return null
  if (Array.isArray(t)) {
    const nonNull = t.find((x) => x !== 'null')
    return nonNull || t[0] || null
  }
  return t
}

function mergeAllOf(schema, doc, seen = new Set()) {
  if (!schema?.allOf?.length) return schema

  const out = { ...schema }
  delete out.allOf

  let merged = { type: 'object', properties: {}, required: [] }

  for (const part of schema.allOf) {
    let s = part
    if (s?.$ref) {
      const name = refName(s.$ref)
      if (name) {
        if (seen.has(name)) continue
        seen.add(name)
      }
      s = getByJsonPointer(doc, s.$ref) || s
    }
    if (s?.allOf) s = mergeAllOf(s, doc, seen)

    if (s?.type && normalizeType(s) !== 'object' && s.properties) {
      // some specs omit type: object but still have properties
    } else if (normalizeType(s) && normalizeType(s) !== 'object' && !s.properties) {
      return schema
    }

    if (s?.properties) Object.assign(merged.properties, s.properties)
    if (Array.isArray(s?.required)) merged.required.push(...s.required)
    if (s?.description && !merged.description) merged.description = s.description
  }

  merged.required = [...new Set(merged.required)]
  return { ...merged, ...out }
}

function formatSchemaPreview(schema, doc, { depth = 2, maxProps = 12 } = {}, indent = '', refStack = new Set()) {
  if (!schema) return [`${indent}any`]

  if (schema.$ref) {
    const name = refName(schema.$ref) || schema.$ref
    const resolved = getByJsonPointer(doc, schema.$ref)
    const lines = [`${indent}${name}`]
    const refKey = String(schema.$ref)
    if (refStack.has(refKey)) return lines
    refStack.add(refKey)
    if (resolved && depth > 0) {
      const next = resolved?.allOf ? mergeAllOf(resolved, doc) : resolved
      const childLines = formatSchemaPreview(next, doc, { depth, maxProps }, indent + '  ', refStack)
      // Avoid printing a single redundant "object" line for refs
      if (!(childLines.length === 1 && childLines[0].trim() === 'object')) lines.push(...childLines)
    }
    refStack.delete(refKey)
    return lines
  }

  const normalized = schema.allOf ? mergeAllOf(schema, doc) : schema

  const t = normalizeType(normalized) || schemaTypeString(normalized)
  if (t === 'object' || normalized.properties) {
    const props = normalized.properties || {}
    const required = new Set(normalized.required || [])
    const keys = Object.keys(props)
    if (!keys.length) return [`${indent}object`]

    const lines = []
    for (const key of keys.slice(0, maxProps)) {
      const s = props[key]
      const typeStr = schemaTypeString(s)
      const req = required.has(key) ? ' (required)' : ''
      const desc = s?.description ? ` - ${String(s.description).replaceAll('\n', ' ').slice(0, 80)}` : ''
      lines.push(`${indent}- ${key}: ${typeStr}${req}${desc}`)
      if (depth > 0) {
        const child = s?.$ref ? getByJsonPointer(doc, s.$ref) : s
        const childNorm = child?.allOf ? mergeAllOf(child, doc) : child
        const childType = normalizeType(childNorm)
        if (childType === 'object' || childNorm?.properties || childNorm?.items) {
          const nested = formatSchemaPreview(childNorm, doc, { depth: depth - 1, maxProps }, indent + '  ', refStack)
          // Only include nested if it adds something beyond "object"/"array"
          if (!(nested.length === 1 && ['object', 'array'].includes(nested[0].trim()))) lines.push(...nested)
        }
      }
    }
    if (keys.length > maxProps) lines.push(`${indent}- ... (${keys.length - maxProps} more)`)
    return lines
  }

  if (t === 'array' || normalized.items) {
    const itemType = schemaTypeString(normalized.items)
    const lines = [`${indent}array<${itemType}>`]
    if (normalized.items && depth > 0) {
      const next = normalized.items?.$ref ? getByJsonPointer(doc, normalized.items.$ref) : normalized.items
      const nextNorm = next?.allOf ? mergeAllOf(next, doc) : next
      const nested = formatSchemaPreview(nextNorm, doc, { depth: depth - 1, maxProps }, indent + '  ', refStack)
      const nestedTrim = nested.length === 1 ? nested[0].trim() : null
      const redundant =
        nestedTrim === null ? false : ['object', 'array'].includes(nestedTrim) || nestedTrim === itemType
      if (!redundant) lines.push(...nested)
    }
    return lines
  }

  if (normalized.oneOf?.length) {
    const opts = normalized.oneOf.slice(0, 5).map((s) => schemaTypeString(s)).join(' | ')
    return [`${indent}oneOf(${opts}${normalized.oneOf.length > 5 ? ' | ...' : ''})`]
  }
  if (normalized.anyOf?.length) {
    const opts = normalized.anyOf.slice(0, 5).map((s) => schemaTypeString(s)).join(' | ')
    return [`${indent}anyOf(${opts}${normalized.anyOf.length > 5 ? ' | ...' : ''})`]
  }

  return [`${indent}${schemaTypeString(normalized)}`]
}

function placeholderForString(schema) {
  if (schema?.enum?.length) return schema.enum[0]
  if (schema?.const !== undefined) return schema.const
  if (schema?.format === 'uuid') return '00000000-0000-0000-0000-000000000000'
  if (schema?.format === 'date-time') return '2025-01-01T00:00:00Z'
  if (schema?.format === 'date') return '2025-01-01'
  if (schema?.format === 'email') return 'user@example.com'
  if (schema?.format === 'uri' || schema?.format === 'url') return 'https://example.com'
  return 'string'
}

function exampleFromSchema(schema, doc, { depth = 3, includeOptional = false } = {}, stack = new Set()) {
  if (!schema) return null

  if (schema.$ref) {
    const name = refName(schema.$ref)
    if (name) {
      if (stack.has(name)) return `<circular:${name}>`
      stack.add(name)
    }
    const resolved = getByJsonPointer(doc, schema.$ref)
    const out = exampleFromSchema(resolved || {}, doc, { depth, includeOptional }, stack)
    if (name) stack.delete(name)
    return out
  }

  const normalized = schema.allOf ? mergeAllOf(schema, doc) : schema

  if (normalized.const !== undefined) return normalized.const
  if (normalized.enum?.length) return normalized.enum[0]

  const t = normalizeType(normalized)
  if (t === 'string') return placeholderForString(normalized)
  if (t === 'integer') return 0
  if (t === 'number') return 0
  if (t === 'boolean') return true
  if (t === 'null') return null

  if ((t === 'array' || normalized.items) && depth > 0) {
    return [exampleFromSchema(normalized.items || {}, doc, { depth: depth - 1, includeOptional }, stack)]
  }

  if ((t === 'object' || normalized.properties || normalized.additionalProperties) && depth > 0) {
    const props = normalized.properties || {}
    const required = new Set(normalized.required || [])
    const out = {}

    const keys = Object.keys(props)
    for (const key of keys) {
      if (!includeOptional && !required.has(key)) continue
      out[key] = exampleFromSchema(props[key], doc, { depth: depth - 1, includeOptional }, stack)
    }

    // If it is a free-form map, add a placeholder entry.
    if (!keys.length && normalized.additionalProperties) {
      out.key = exampleFromSchema(
        normalized.additionalProperties === true ? {} : normalized.additionalProperties,
        doc,
        { depth: depth - 1, includeOptional },
        stack,
      )
    }

    return out
  }

  if (normalized.oneOf?.length) return exampleFromSchema(normalized.oneOf[0], doc, { depth, includeOptional }, stack)
  if (normalized.anyOf?.length) return exampleFromSchema(normalized.anyOf[0], doc, { depth, includeOptional }, stack)

  return null
}

function collectSchemaRefs(schema, doc, out = new Set(), stack = new Set()) {
  if (!schema) return out

  if (schema.$ref) {
    const name = refName(schema.$ref)
    if (name) out.add(name)
    if (name) {
      if (stack.has(name)) return out
      stack.add(name)
    }
    const resolved = getByJsonPointer(doc, schema.$ref)
    if (resolved) collectSchemaRefs(resolved, doc, out, stack)
    if (name) stack.delete(name)
    return out
  }

  const normalized = schema.allOf ? mergeAllOf(schema, doc) : schema

  for (const key of ['oneOf', 'anyOf', 'allOf']) {
    if (Array.isArray(normalized[key])) {
      for (const s of normalized[key]) collectSchemaRefs(s, doc, out, stack)
    }
  }

  if (normalized.properties) {
    for (const s of Object.values(normalized.properties)) collectSchemaRefs(s, doc, out, stack)
  }
  if (normalized.items) collectSchemaRefs(normalized.items, doc, out, stack)
  if (normalized.additionalProperties && normalized.additionalProperties !== true) {
    collectSchemaRefs(normalized.additionalProperties, doc, out, stack)
  }

  return out
}

function collectSchemaFieldNames(schema, doc, out = new Set(), stack = new Set(), depth = 3) {
  if (!schema || depth < 0) return out

  if (schema.$ref) {
    const ref = String(schema.$ref)
    if (stack.has(ref)) return out
    stack.add(ref)
    const resolved = getByJsonPointer(doc, ref)
    if (resolved) collectSchemaFieldNames(resolved, doc, out, stack, depth)
    stack.delete(ref)
    return out
  }

  const normalized = schema.allOf ? mergeAllOf(schema, doc) : schema

  for (const key of ['oneOf', 'anyOf', 'allOf']) {
    if (Array.isArray(normalized[key])) {
      for (const s of normalized[key]) collectSchemaFieldNames(s, doc, out, stack, depth)
    }
  }

  if (normalized.properties) {
    for (const [k, s] of Object.entries(normalized.properties)) {
      out.add(k)
      collectSchemaFieldNames(s, doc, out, stack, depth - 1)
    }
  }

  if (normalized.items) collectSchemaFieldNames(normalized.items, doc, out, stack, depth - 1)
  if (normalized.additionalProperties && normalized.additionalProperties !== true) {
    collectSchemaFieldNames(normalized.additionalProperties, doc, out, stack, depth - 1)
  }

  return out
}

function normalizeOperationSecurity(op, spec) {
  if (Object.prototype.hasOwnProperty.call(op, 'security')) return op.security
  return spec.security
}

function securityLabel(opSecurity, spec) {
  if (!opSecurity) return null
  if (Array.isArray(opSecurity) && opSecurity.length === 0) return 'none'

  const schemes = spec?.components?.securitySchemes || {}

  function schemeLabel(name) {
    const s = schemes[name]
    if (!s) return name
    if (s.type === 'apiKey' && s.in === 'header' && s.name) return `${name} (${s.name} header)`
    if (s.type === 'apiKey' && s.in) return `${name} (apiKey in ${s.in})`
    if (s.type === 'http' && s.scheme === 'bearer') return `${name} (Authorization: Bearer ...)`
    if (s.type === 'http') return `${name} (http ${s.scheme || ''})`.trim()
    return `${name} (${s.type})`
  }

  const requirementSets = []
  for (const req of opSecurity || []) {
    const keys = Object.keys(req || {})
    if (!keys.length) continue
    requirementSets.push(keys.map(schemeLabel).join(' + '))
  }

  if (!requirementSets.length) return null
  return requirementSets.join(' OR ')
}

function toShortSpec(s) {
  return {
    id: s.id,
    title: s.title,
    version: s.version,
    file: s.filePath,
    servers: s.servers,
    operations: s.operations.length,
    schemas: Object.keys(s.schemas).length,
  }
}

async function readSpecSource(source) {
  if (isUrl(source)) {
    const res = await fetch(source, {
      // Some CDNs / WAFs behave better with a UA.
      headers: { 'User-Agent': 'kapso-openapi-explore/1.0 (+https://docs.kapso.ai)' },
    })
    if (!res.ok) throw new Error(`HTTP ${res.status} ${res.statusText}`)
    return await res.text()
  }
  return readFileSync(source, 'utf-8')
}

async function loadSpecsAsync({ sources, sourceMode, specFilter }) {
  if (!sources.length) die('No OpenAPI sources provided')

  const seenIds = new Map()
  const specs = []
  const errors = []

  for (const filePath of sources) {
    let raw = null
    try {
      raw = await readSpecSource(filePath)
    } catch (e) {
      errors.push({ source: filePath, error: e })
      if (sourceMode === 'explicit') console.error(`Skipping ${filePath}: ${e.message}`)
      continue
    }

    let doc
    try {
      doc = parseYaml(raw)
    } catch (e) {
      errors.push({ source: filePath, error: e })
      console.error(`Skipping ${filePath}: YAML parse error: ${e.message}`)
      continue
    }

    const idBase = inferSpecId(filePath, doc)
    const n = (seenIds.get(idBase) || 0) + 1
    seenIds.set(idBase, n)
    const id = n === 1 ? idBase : `${idBase}${n}`

    if (specFilter && id !== specFilter) continue

    const title = doc?.info?.title || id
    const version = doc?.info?.version || '?'
    const servers = (doc?.servers || []).map((s) => s?.url).filter(Boolean)
    const tags = doc?.tags || []
    const schemas = doc?.components?.schemas || {}
    const schemaFieldCache = new Map()

    const getSchemaFields = (schemaName) => {
      if (schemaFieldCache.has(schemaName)) return schemaFieldCache.get(schemaName)
      const schema = schemas?.[schemaName]
      const fields = schema ? [...collectSchemaFieldNames(schema, doc)] : []
      schemaFieldCache.set(schemaName, fields)
      return fields
    }

    const operations = []
    const paths = doc?.paths || {}
    for (const [p, pathItemRaw] of Object.entries(paths)) {
      const pathItem = pathItemRaw || {}
      const pathParams = Array.isArray(pathItem.parameters) ? pathItem.parameters.map((x) => derefObject(x, doc)) : []

      for (const method of HTTP_METHODS) {
        const op = pathItem[method]
        if (!op) continue

        const mergedParams = [...pathParams, ...((op.parameters || []).filter(Boolean))]
          .map((x) => derefObject(x, doc))
          .filter(Boolean)
        const opSecurity = normalizeOperationSecurity(op, doc)
        const opRequestBody = derefObject(op.requestBody || null, doc)

        const refs = new Set()
        // params
        for (const param of mergedParams) {
          if (param?.schema) collectSchemaRefs(param.schema, doc, refs)
          if (param?.content) {
            for (const media of Object.values(param.content)) {
              if (media?.schema) collectSchemaRefs(media.schema, doc, refs)
            }
          }
        }
        // body
        if (opRequestBody?.content) {
          for (const media of Object.values(opRequestBody.content)) {
            if (media?.schema) collectSchemaRefs(media.schema, doc, refs)
          }
        }
        // responses
        if (op?.responses) {
          for (const resp of Object.values(op.responses)) {
            const r = derefObject(resp, doc)
            if (r?.content) {
              for (const media of Object.values(r.content)) {
                if (media?.schema) collectSchemaRefs(media.schema, doc, refs)
              }
            }
          }
        }

        const fieldsUsed = new Set()
        for (const schemaName of refs) {
          for (const f of getSchemaFields(schemaName)) fieldsUsed.add(f)
        }

        operations.push({
          specId: id,
          specTitle: title,
          specFile: filePath,
          method,
          path: p,
          operationId: op.operationId || null,
          summary: op.summary || null,
          description: op.description || null,
          tags: op.tags || [],
          deprecated: Boolean(op.deprecated),
          security: opSecurity,
          securityLabel: securityLabel(opSecurity, doc),
          parameters: mergedParams,
          requestBody: opRequestBody,
          responses: op.responses || {},
          refsUsed: refs,
          fieldsUsed,
        })
      }
    }

    specs.push({
      id,
      filePath,
      title,
      version,
      servers,
      doc,
      tags,
      schemas,
      operations,
    })
  }

  if (!specs.length) {
    if (sourceMode === 'default_remote' && errors.length) {
      const apiDir = findLocalApiDir()
      const local = apiDir ? walk(apiDir, { filePattern: /^openapi-.*\.ya?ml$/ }) : []
      if (local.length) {
        console.error(`Could not fetch published OpenAPI specs. Falling back to local repo specs (api/**/openapi-*.yaml).`)
        return await loadSpecsAsync({ sources: local, sourceMode: 'explicit', specFilter })
      }
    }
    if (specFilter) die(`No specs matched --spec ${specFilter}`)
    die('No specs loaded')
  }

  if (sourceMode === 'default_remote' && errors.length) {
    console.error(`Some published OpenAPI specs could not be fetched:`)
    for (const e of errors) console.error(`- ${e.source}: ${e.error?.message || String(e.error)}`)
  }

  return specs
}

function findOperation(specs, query, { specHint } = {}) {
  const raw = query.trim()
  const direct = raw.includes(':') ? raw.split(':') : null
  const qSpec = direct?.[0] || specHint
  const qId = direct?.[1] || raw

  // METHOD /path
  const m = raw.match(/^(get|post|put|patch|delete|options|head)\\s+(.+)$/i)
  if (m) {
    const method = m[1].toLowerCase()
    const p = m[2].trim()
    const matches = []
    for (const s of specs) {
      if (qSpec && s.id !== qSpec) continue
      for (const op of s.operations) {
        if (op.method === method && op.path === p) matches.push(op)
      }
    }
    return matches
  }

  // operationId
  const matches = []
  for (const s of specs) {
    if (qSpec && s.id !== qSpec) continue
    for (const op of s.operations) {
      if (op.operationId === qId) matches.push(op)
    }
  }
  return matches
}

function findSchema(specs, query, { specHint } = {}) {
  const raw = query.trim()
  const direct = raw.includes(':') ? raw.split(':') : null
  const qSpec = direct?.[0] || specHint
  const qName = direct?.[1] || raw

  const matches = []
  for (const s of specs) {
    if (qSpec && s.id !== qSpec) continue
    if (Object.prototype.hasOwnProperty.call(s.schemas, qName)) {
      matches.push({ spec: s, name: qName, schema: s.schemas[qName] })
    }
  }
  return matches
}

function scoreText(hay, q) {
  if (!hay) return 0
  const h = hay.toLowerCase()
  if (h === q) return 100
  if (h.startsWith(q)) return 60
  if (h.includes(q)) return 30
  return 0
}

function search(specs, query, { specHint, limit = 30 } = {}) {
  const q = query.toLowerCase().trim()
  if (!q) return { ops: [], schemas: [] }

  const ops = []
  const schemas = []

  for (const s of specs) {
    if (specHint && s.id !== specHint) continue

    for (const op of s.operations) {
      let score = 0
      score += scoreText(op.operationId, q) * 3
      score += scoreText(`${op.method} ${op.path}`, q) * 2
      score += scoreText(op.summary, q) * 2
      score += scoreText(op.description, q)
      for (const t of op.tags || []) score += scoreText(t, q) * 2
      score += scoreText((op.parameters || []).map((p) => p?.name).filter(Boolean).join(' '), q) * 2
      score += scoreText([...op.refsUsed].join(' '), q) * 2
      score += scoreText([...op.fieldsUsed].join(' '), q)
      if (score > 0) ops.push({ score, op })
    }

    for (const [name, schema] of Object.entries(s.schemas)) {
      let score = 0
      score += scoreText(name, q) * 3
      score += scoreText(schema?.description, q)
      score += scoreText([...collectSchemaFieldNames(schema, s.doc)].join(' '), q) * 2
      if (score > 0) schemas.push({ score, spec: s, name, schema })
    }
  }

  ops.sort((a, b) => b.score - a.score)
  schemas.sort((a, b) => b.score - a.score)

  return {
    ops: ops.slice(0, limit).map((x) => x.op),
    schemas: schemas.slice(0, limit).map((x) => ({ specId: x.spec.id, name: x.name })),
  }
}

function printTable(rows, { sep = '  ' } = {}) {
  if (!rows.length) return
  const widths = []
  for (const row of rows) {
    row.forEach((cell, i) => {
      widths[i] = Math.max(widths[i] || 0, String(cell).length)
    })
  }
  for (const row of rows) {
    const line = row
      .map((cell, i) => String(cell).padEnd(widths[i], ' '))
      .join(sep)
      .trimEnd()
    console.log(line)
  }
}

function printSpecs(specs, { json } = {}) {
  if (json) {
    console.log(JSON.stringify(specs.map(toShortSpec), null, 2))
    return
  }

  const rows = [['id', 'version', 'operations', 'schemas', 'file']]
  for (const s of specs) rows.push([s.id, s.version, String(s.operations.length), String(Object.keys(s.schemas).length), s.filePath])
  printTable(rows)
}

function printTags(specs, { specHint } = {}) {
  const rows = [['spec', 'tag', 'description']]
  for (const s of specs) {
    if (specHint && s.id !== specHint) continue
    for (const t of s.tags || []) rows.push([s.id, t.name, (t.description || '').replaceAll('\n', ' ').slice(0, 80)])
  }
  if (rows.length === 1) die('No tags found')
  printTable(rows)
}

function printOps(specs, { specHint, tag, q, json, limit = 30 } = {}) {
  let ops = []
  for (const s of specs) {
    if (specHint && s.id !== specHint) continue
    ops.push(...s.operations)
  }

  if (tag) ops = ops.filter((o) => (o.tags || []).includes(tag))

  if (q) {
    const res = search(specs, q, { specHint, limit: Math.max(limit, 200) })
    const opSet = new Set(res.ops.map((o) => `${o.specId}:${o.operationId || o.method + ' ' + o.path}`))
    ops = ops.filter((o) => opSet.has(`${o.specId}:${o.operationId || o.method + ' ' + o.path}`))
  }

  ops = ops.slice(0, limit)

  if (json) {
    console.log(
      JSON.stringify(
        ops.map((o) => ({
          spec: o.specId,
          operationId: o.operationId,
          method: o.method,
          path: o.path,
          summary: o.summary,
        })),
        null,
        2,
      ),
    )
    return
  }

  const rows = [['spec', 'operationId', 'method', 'path', 'summary']]
  for (const o of ops) rows.push([o.specId, o.operationId || '-', o.method.toUpperCase(), o.path, (o.summary || '').slice(0, 80)])
  printTable(rows)
}

function splitParams(params) {
  const out = { path: [], query: [], header: [], cookie: [], other: [] }
  for (const p of params || []) {
    const loc = p?.in
    if (loc === 'path') out.path.push(p)
    else if (loc === 'query') out.query.push(p)
    else if (loc === 'header') out.header.push(p)
    else if (loc === 'cookie') out.cookie.push(p)
    else out.other.push(p)
  }
  return out
}

function paramType(param) {
  const s = param?.schema
  if (s) return schemaTypeString(s)
  if (param?.content) {
    const media = Object.values(param.content)[0]
    if (media?.schema) return schemaTypeString(media.schema)
  }
  return 'any'
}

function printParamsBlock(title, params) {
  if (!params.length) return
  console.log(`\n${title}`)
  const rows = [['name', 'in', 'required', 'type', 'description']]
  for (const p of params) {
    rows.push([
      p.name || '-',
      p.in || '-',
      p.required ? 'yes' : 'no',
      paramType(p),
      (p.description || '').replaceAll('\n', ' ').slice(0, 80),
    ])
  }
  printTable(rows)
}

function printOperation(op, spec) {
  const baseUrl = spec.servers?.[0] || ''
  const full = baseUrl ? `${baseUrl}${op.path}` : op.path

  const id = op.operationId ? `${op.specId}:${op.operationId}` : `${op.specId}:${op.method.toUpperCase()} ${op.path}`

  console.log(id)
  console.log(`${op.method.toUpperCase()} ${full}`)

  if (op.summary) console.log(`\n${op.summary}`)
  if (op.deprecated) console.log(`\nDeprecated: yes`)

  const auth = op.securityLabel
  if (auth) console.log(`\nAuth: ${auth}`)

  if (op.tags?.length) console.log(`Tags: ${op.tags.join(', ')}`)

  if (op.description) {
    const desc = String(op.description).trim().replace(/\n{3,}/g, '\n\n')
    const short = desc.length > 800 ? `${desc.slice(0, 800)}\n...` : desc
    console.log(`\n${short}`)
  }

  const params = splitParams(op.parameters || [])
  printParamsBlock('Path params', params.path)
  printParamsBlock('Query params', params.query)
  printParamsBlock('Header params', params.header)

  if (op.requestBody?.content) {
    console.log('\nBody')
    const required = op.requestBody.required ? 'required' : 'optional'
    console.log(`required: ${required}`)

    const contentTypes = Object.keys(op.requestBody.content)
    for (const ct of contentTypes) {
      const schema = op.requestBody.content?.[ct]?.schema
      if (!schema) continue
      console.log(`\n${ct}`)
      const lines = formatSchemaPreview(schema, spec.doc, { depth: 3, maxProps: 12 })
      for (const l of lines) console.log(l)

      if (ct === 'application/json') {
        const ex = exampleFromSchema(schema, spec.doc, { depth: 3, includeOptional: false })
        if (ex && typeof ex === 'object') {
          console.log('\nexample (required fields)')
          console.log(JSON.stringify(ex, null, 2))
        }
      }
    }
  }

  if (op.responses && Object.keys(op.responses).length) {
    console.log('\nResponses')
    const codes = Object.keys(op.responses).sort((a, b) => {
      const na = Number(a)
      const nb = Number(b)
      if (Number.isFinite(na) && Number.isFinite(nb)) return na - nb
      if (a === 'default') return 1
      if (b === 'default') return -1
      return a.localeCompare(b)
    })

    for (const code of codes) {
      const resp = derefObject(op.responses[code], spec.doc)
      const desc = resp?.description ? ` - ${String(resp.description).replaceAll('\n', ' ').slice(0, 80)}` : ''
      console.log(`\n${code}${desc}`)

      const content = resp?.content || {}
      for (const [ct, media] of Object.entries(content)) {
        if (!media?.schema) continue
        console.log(`${ct}`)
        const lines = formatSchemaPreview(media.schema, spec.doc, { depth: 3, maxProps: 12 })
        for (const l of lines) console.log(l)
      }
    }
  }

  console.log('\ncurl')
  console.log(formatCurl(op, spec))
}

function replacePathParams(p) {
  return p.replaceAll(/\{([^}]+)\}/g, '<$1>')
}

function formatCurl(op, spec) {
  const baseUrl = spec.servers?.[0] || ''
  let url = baseUrl ? `${baseUrl}${replacePathParams(op.path)}` : replacePathParams(op.path)

  const requiredQuery = (op.parameters || [])
    .filter((p) => p?.in === 'query' && p?.required && p?.name)
    .map((p) => `${encodeURIComponent(p.name)}=<${p.name}>`)
  if (requiredQuery.length) url += `?${requiredQuery.join('&')}`

  const lines = []
  lines.push(`curl -X ${op.method.toUpperCase()} '${url}' \\`)

  // auth header if we can infer it
  const schemes = spec?.doc?.components?.securitySchemes || {}
  const sec = Array.isArray(op.security) ? op.security : null
  const candidates = (sec || []).filter((x) => x && typeof x === 'object')
  const preferred =
    candidates.find((req) =>
      Object.keys(req).some((name) => schemes[name]?.type === 'apiKey' && schemes[name]?.in === 'header'),
    ) || candidates[0]

  for (const name of Object.keys(preferred || {})) {
    const s = schemes[name]
    if (s?.type === 'apiKey' && s.in === 'header' && s.name) {
      lines.push(`  -H '${s.name}: $KAPSO_API_KEY' \\`)
    } else if (s?.type === 'http' && s.scheme === 'bearer') {
      lines.push(`  -H 'Authorization: Bearer $ACCESS_TOKEN' \\`)
    }
  }

  // content-type + body for JSON
  const jsonSchema = op.requestBody?.content?.['application/json']?.schema
  if (jsonSchema) {
    const ex = exampleFromSchema(jsonSchema, spec.doc, { depth: 4, includeOptional: false })
    lines.push(`  -H 'Content-Type: application/json' \\`)
    lines.push(`  -d '${JSON.stringify(ex ?? {}, null, 0)}'`)
    return lines.join('\n')
  }

  // trim trailing backslash
  lines[lines.length - 1] = lines[lines.length - 1].replace(/ \\\\$/, '')
  return lines.join('\n')
}

function printSchemaDetails(match, specs, { includeUsedBy = true } = {}) {
  const { spec, name, schema } = match
  console.log(`${spec.id}:${name}`)

  const normalized = schema?.allOf ? mergeAllOf(schema, spec.doc) : schema
  const typeStr = schemaTypeString(normalized)
  console.log(typeStr)

  if (normalized?.description) console.log(`\n${String(normalized.description).trim()}`)

  const required = normalized?.required || []
  if (required.length) console.log(`\nrequired: ${required.join(', ')}`)

  if (normalized?.properties || normalized?.items) {
    console.log('\nshape')
    const lines = formatSchemaPreview(normalized, spec.doc, { depth: 3, maxProps: 25 })
    for (const l of lines) console.log(l)
  }

  const ex = exampleFromSchema(normalized, spec.doc, { depth: 4, includeOptional: false })
  if (ex && typeof ex === 'object') {
    console.log('\nexample (required fields)')
    console.log(JSON.stringify(ex, null, 2))
  }

  if (includeUsedBy) {
    const usedBy = []
    for (const s of specs) {
      for (const op of s.operations) {
        if (op.refsUsed?.has(name)) usedBy.push(op)
      }
    }

    if (usedBy.length) {
      console.log('\nused by')
      const rows = [['spec', 'operationId', 'method', 'path']]
      for (const op of usedBy.slice(0, 30)) rows.push([op.specId, op.operationId || '-', op.method.toUpperCase(), op.path])
      printTable(rows)
      if (usedBy.length > 30) console.log(`... (${usedBy.length - 30} more)`)
    }
  }
}

function printWhere(specs, schemaQuery, { specHint, json, limit = 30 } = {}) {
  const matches = findSchema(specs, schemaQuery, { specHint })
  if (!matches.length) die(`Schema not found: ${schemaQuery}`)
  if (matches.length > 1 && !schemaQuery.includes(':')) {
    die(`Schema exists in multiple specs. Use specId:SchemaName\n${matches.map((m) => `- ${m.spec.id}:${m.name}`).join('\n')}`)
  }

  const { name } = matches[0]
  const usedBy = []
  for (const s of specs) {
    if (specHint && s.id !== specHint) continue
    for (const op of s.operations) {
      if (op.refsUsed?.has(name)) usedBy.push(op)
    }
  }

  if (json) {
    console.log(
      JSON.stringify(
        usedBy.slice(0, limit).map((o) => ({
          spec: o.specId,
          operationId: o.operationId,
          method: o.method,
          path: o.path,
          summary: o.summary,
        })),
        null,
        2,
      ),
    )
    return
  }

  if (!usedBy.length) {
    console.log('No operations reference this schema (via $ref).')
    return
  }

  const rows = [['spec', 'operationId', 'method', 'path', 'summary']]
  for (const o of usedBy.slice(0, limit)) rows.push([o.specId, o.operationId || '-', o.method.toUpperCase(), o.path, (o.summary || '').slice(0, 80)])
  printTable(rows)
  if (usedBy.length > limit) console.log(`... (${usedBy.length - limit} more)`)
}

async function main() {
  const { opts, command, rest } = parseArgs(process.argv.slice(2))
  if (!command) printHelp(1)

  let sources = []
  let sourceMode = 'explicit'

  if (opts.files.length) {
    sources = opts.files
    sourceMode = 'explicit'
  } else if (opts.all) {
    const apiDir = findLocalApiDir()
    sources = apiDir ? walk(apiDir, { filePattern: /^openapi-.*\.ya?ml$/ }) : []
    sourceMode = 'explicit'
  } else {
    sources = deducePublishedOpenApiUrls(DEFAULT_PUBLISHED_WHATSAPP_OPENAPI)
    sourceMode = 'default_remote'
  }

  const specs = await loadSpecsAsync({ sources, sourceMode, specFilter: opts.spec })

  if (command === 'specs') return printSpecs(specs, { json: opts.json })
  if (command === 'tags') return printTags(specs, { specHint: opts.spec })
  if (command === 'ops') return printOps(specs, { specHint: opts.spec, tag: opts.tag, q: opts.q, json: opts.json, limit: opts.limit })
  if (command === 'search') {
    const q = rest.join(' ').trim()
    if (!q) die('Usage: search <query>')
    const res = search(specs, q, { specHint: opts.spec, limit: opts.limit })
    if (opts.json) {
      return console.log(
        JSON.stringify(
          {
            ops: res.ops.map((o) => ({
              spec: o.specId,
              operationId: o.operationId,
              method: o.method,
              path: o.path,
              summary: o.summary,
            })),
            schemas: res.schemas,
          },
          null,
          2,
        ),
      )
    }

    if (!res.ops.length && !res.schemas.length) {
      console.log('No matches.')
      return
    }

    if (res.ops.length) {
      console.log('ops')
      const rows = [['spec', 'operationId', 'method', 'path', 'summary']]
      for (const o of res.ops) rows.push([o.specId, o.operationId || '-', o.method.toUpperCase(), o.path, (o.summary || '').slice(0, 80)])
      printTable(rows)
    }
    if (res.schemas.length) {
      console.log('\nschemas')
      const rows = [['spec', 'name']]
      for (const s of res.schemas) rows.push([s.specId, s.name])
      printTable(rows)
    }
    return
  }
  if (command === 'op') {
    const q = rest.join(' ').trim()
    if (!q) die('Usage: op <operationId | specId:operationId | "METHOD /path">')
    const matches = findOperation(specs, q, { specHint: opts.spec })
    if (!matches.length) {
      const res = search(specs, q, { specHint: opts.spec, limit: 10 })
      if (res.ops.length) {
        console.log(`Operation not found: ${q}\n`)
        console.log('closest ops')
        const rows = [['spec', 'operationId', 'method', 'path', 'summary']]
        for (const o of res.ops) rows.push([o.specId, o.operationId || '-', o.method.toUpperCase(), o.path, (o.summary || '').slice(0, 80)])
        printTable(rows)
        process.exit(1)
      }
      die(`Operation not found: ${q}`)
    }
    if (matches.length > 1 && !q.includes(':') && !q.match(/^(get|post|put|patch|delete|options|head)\\s+/i)) {
      die(`OperationId exists in multiple specs. Use specId:operationId\n${matches.map((m) => `- ${m.specId}:${m.operationId}`).join('\n')}`)
    }
    const op = matches[0]
    const spec = specs.find((s) => s.id === op.specId)
    if (!spec) die(`Internal error: missing spec ${op.specId}`)
    printOperation(op, spec)
    return
  }
  if (command === 'schema') {
    const q = rest.join(' ').trim()
    if (!q) die('Usage: schema <SchemaName | specId:SchemaName>')
    const matches = findSchema(specs, q, { specHint: opts.spec })
    if (!matches.length) {
      const res = search(specs, q, { specHint: opts.spec, limit: 10 })
      if (res.schemas.length) {
        console.log(`Schema not found: ${q}\n`)
        console.log('closest schemas')
        const rows = [['spec', 'name']]
        for (const s of res.schemas) rows.push([s.specId, s.name])
        printTable(rows)
        process.exit(1)
      }
      die(`Schema not found: ${q}`)
    }
    if (matches.length > 1 && !q.includes(':')) {
      die(`Schema exists in multiple specs. Use specId:SchemaName\n${matches.map((m) => `- ${m.spec.id}:${m.name}`).join('\n')}`)
    }
    printSchemaDetails(matches[0], specs, { includeUsedBy: true })
    return
  }
  if (command === 'where') {
    const q = rest.join(' ').trim()
    if (!q) die('Usage: where <SchemaName | specId:SchemaName>')
    return printWhere(specs, q, { specHint: opts.spec, json: opts.json, limit: opts.limit })
  }

  die(`Unknown command: ${command}`)
}

main().catch((e) => die(e?.stack || e?.message || String(e)))
```

## File: `skills/integrate-whatsapp/scripts/publish-flow.js`
```javascript
#!/usr/bin/env node
const { parseArgs, getStringFlag } = require('./lib/cli');
const { platformRequest } = require('./lib/http');
const { run } = require('./lib/run');
const { requireFlowId } = require('./lib/whatsapp-flow');

run(async () => {
  const { flags } = parseArgs(process.argv.slice(2));
  const flowId = requireFlowId(flags);
  const phoneNumberId = getStringFlag(flags, 'phone-number-id') || getStringFlag(flags, 'phone_number_id');
  const body = {};

  if (phoneNumberId) {
    body.phone_number_id = phoneNumberId;
  }

  return platformRequest({
    method: 'POST',
    path: `/platform/v1/whatsapp/flows/${flowId}/publish`,
    body: Object.keys(body).length > 0 ? body : undefined
  });
});
```

## File: `skills/integrate-whatsapp/scripts/read-flow-json.js`
```javascript
#!/usr/bin/env node
const { parseArgs, getStringFlag, getNumberFlag } = require('./lib/cli');
const { platformRequest } = require('./lib/http');
const { run } = require('./lib/run');
const { requireFlowId } = require('./lib/whatsapp-flow');

run(async () => {
  const { flags } = parseArgs(process.argv.slice(2));
  const flowId = requireFlowId(flags);
  const versionId = getStringFlag(flags, 'version-id');

  if (versionId) {
    return platformRequest({
      method: 'GET',
      path: `/platform/v1/whatsapp/flows/${flowId}/versions/${versionId}`
    });
  }

  const list = await platformRequest({
    method: 'GET',
    path: `/platform/v1/whatsapp/flows/${flowId}/versions`,
    query: {
      page: getNumberFlag(flags, 'page') || 1,
      per_page: getNumberFlag(flags, 'per-page') || 1
    }
  });

  const versions = Array.isArray(list?.data) ? list.data : [];
  const latest = versions[0];
  if (!latest) {
    return { data: { flow_id: flowId, versions: [] }, meta: list?.meta };
  }

  const detail = await platformRequest({
    method: 'GET',
    path: `/platform/v1/whatsapp/flows/${flowId}/versions/${latest.id}`
  });

  return {
    data: {
      flow_id: flowId,
      version: detail?.data || detail,
      versions
    },
    meta: list?.meta
  };
});
```

## File: `skills/integrate-whatsapp/scripts/register-data-endpoint.js`
```javascript
#!/usr/bin/env node
const { parseArgs, getStringFlag } = require('./lib/cli');
const { platformRequest } = require('./lib/http');
const { run } = require('./lib/run');
const { requireFlowId } = require('./lib/whatsapp-flow');

run(async () => {
  const { flags } = parseArgs(process.argv.slice(2));
  const flowId = requireFlowId(flags);
  const phoneNumberId = getStringFlag(flags, 'phone-number-id') || getStringFlag(flags, 'phone_number_id');

  const body = {};
  if (phoneNumberId) {
    body.phone_number_id = phoneNumberId;
  }

  return platformRequest({
    method: 'POST',
    path: `/platform/v1/whatsapp/flows/${flowId}/data_endpoint/register`,
    body: Object.keys(body).length > 0 ? body : undefined
  });
});
```

## File: `skills/integrate-whatsapp/scripts/send-interactive.mjs`
```
import { loadJsonPayload, parseArgs, requireFlag } from './lib/args.mjs';
import { metaProxyRequest } from './lib/request.mjs';
import { err, ok, printResult } from './lib/output.mjs';

function usage() {
  return {
    usage: 'node scripts/send-interactive.mjs --phone-number-id <PHONE_NUMBER_ID> --json <payload> | --file <path>',
    env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY', 'META_GRAPH_VERSION (optional)'],
    notes: ['Payload must include messaging_product: "whatsapp" and type: "interactive".'],
    hints: [
      'To discover phone_number_id (Meta phone number id), run: node scripts/list-platform-phone-numbers.mjs',
      'Start from an asset payload in assets/ (send-interactive-*.json) and adjust to/interactive fields.'
    ]
  };
}

function normalizePayload(payload) {
  if (!payload || typeof payload !== 'object') {
    throw new Error('Payload must be a JSON object');
  }

  if (!payload.messaging_product) {
    payload.messaging_product = 'whatsapp';
  }

  if (payload.messaging_product !== 'whatsapp') {
    throw new Error('messaging_product must be whatsapp');
  }

  if (payload.type !== 'interactive') {
    throw new Error('type must be interactive');
  }

  if (!payload.to) {
    throw new Error('to is required');
  }

  if (!payload.interactive || typeof payload.interactive !== 'object') {
    throw new Error('interactive is required and must be an object');
  }

  if (!payload.interactive.type) {
    throw new Error('interactive.type is required');
  }

  return payload;
}

async function main() {
  const { flags, errors } = parseArgs(process.argv.slice(2));
  if (flags.help) {
    return printResult(ok(usage()));
  }
  if (errors.length > 0) {
    return printResult(err('Invalid arguments', { errors, ...usage() }));
  }

  try {
    const phoneNumberId = requireFlag(flags, ['phone-number-id', 'phone_number_id'], 'phone-number-id');
    const payload = normalizePayload(await loadJsonPayload(flags));

    const response = await metaProxyRequest({
      method: 'POST',
      path: `${phoneNumberId}/messages`,
      body: JSON.stringify(payload)
    });

    if (!response.ok) {
      return printResult(err('Meta proxy request failed', { response }));
    }

    return printResult(ok({ response }));
  } catch (error) {
    return printResult(err('Failed to send interactive message', { message: String(error?.message || error), ...usage() }));
  }
}

main().then((code) => process.exit(code));

```

## File: `skills/integrate-whatsapp/scripts/send-template.mjs`
```
import { loadJsonPayload, parseArgs, requireFlag } from './lib/args.mjs';
import { metaProxyRequest } from './lib/request.mjs';
import { err, ok, printResult } from './lib/output.mjs';

function usage() {
  return {
    usage: 'node scripts/send-template.mjs --phone-number-id <PHONE_NUMBER_ID> --json <payload> | --file <path>',
    env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY', 'META_GRAPH_VERSION (optional)'],
    notes: ['Payload must include messaging_product: "whatsapp" and type: "template".'],
    hints: [
      'To discover phone_number_id (Meta phone number id), run: node scripts/list-platform-phone-numbers.mjs',
      'Start from an asset payload in assets/ (send-time examples) and adjust the template name/to/components.'
    ]
  };
}

function normalizePayload(payload) {
  if (!payload || typeof payload !== 'object') {
    throw new Error('Payload must be a JSON object');
  }

  if (!payload.messaging_product) {
    payload.messaging_product = 'whatsapp';
  }

  if (payload.messaging_product !== 'whatsapp') {
    throw new Error('messaging_product must be whatsapp');
  }

  if (payload.type !== 'template') {
    throw new Error('type must be template');
  }

  if (!payload.to) {
    throw new Error('to is required');
  }

  return payload;
}

async function main() {
  const { flags, errors } = parseArgs(process.argv.slice(2));
  if (flags.help) {
    return printResult(ok(usage()));
  }
  if (errors.length > 0) {
    return printResult(err('Invalid arguments', { errors, ...usage() }));
  }

  try {
    const phoneNumberId = requireFlag(flags, ['phone-number-id', 'phone_number_id'], 'phone-number-id');
    const payload = normalizePayload(await loadJsonPayload(flags));

    const response = await metaProxyRequest({
      method: 'POST',
      path: `${phoneNumberId}/messages`,
      body: JSON.stringify(payload)
    });

    if (!response.ok) {
      return printResult(err('Meta proxy request failed', { response }));
    }

    return printResult(ok({ response }));
  } catch (error) {
    return printResult(err('Failed to send template message', { message: String(error?.message || error), ...usage() }));
  }
}

main().then((code) => process.exit(code));
```

## File: `skills/integrate-whatsapp/scripts/send-test-flow.js`
```javascript
#!/usr/bin/env node
const { parseArgs, requireStringFlag, getStringFlag, getBooleanFlag, readFlagJson } = require('./lib/cli');
const { metaRequest } = require('./lib/http');
const { run } = require('./lib/run');

run(async () => {
  const { flags } = parseArgs(process.argv.slice(2));
  const phoneNumberId = requireStringFlag(flags, 'phone-number-id');
  const to = requireStringFlag(flags, 'to');
  const flowId = requireStringFlag(flags, 'flow-id');
  const bodyText = requireStringFlag(flags, 'body-text');
  const flowCta = getStringFlag(flags, 'flow-cta') || 'Open';
  const headerText = getStringFlag(flags, 'header-text');
  const footerText = getStringFlag(flags, 'footer-text');
  const flowToken = getStringFlag(flags, 'flow-token') || flowId;
  const flowAction = getStringFlag(flags, 'flow-action');
  const flowActionPayload = await readFlagJson(flags, 'flow-action-payload', 'flow-action-payload-file');
  const mode = getStringFlag(flags, 'mode');
  const draft = getBooleanFlag(flags, 'draft');

  const payload = {
    messaging_product: 'whatsapp',
    recipient_type: 'individual',
    to,
    type: 'interactive',
    interactive: {
      type: 'flow',
      body: { text: bodyText },
      action: {
        name: 'flow',
        parameters: {
          flow_message_version: '3',
          flow_id: flowId,
          flow_cta: flowCta,
          flow_token: flowToken
        }
      }
    }
  };

  if (headerText) {
    payload.interactive.header = { type: 'text', text: headerText };
  }

  if (footerText) {
    payload.interactive.footer = { text: footerText };
  }

  if (flowAction) {
    payload.interactive.action.parameters.flow_action = flowAction;
  }

  if (flowActionPayload) {
    payload.interactive.action.parameters.flow_action_payload = flowActionPayload;
  }

  if (mode) {
    payload.interactive.action.parameters.mode = mode;
  } else if (draft) {
    payload.interactive.action.parameters.mode = 'draft';
  }

  return metaRequest({
    method: 'POST',
    path: `/${phoneNumberId}/messages`,
    body: payload
  });
});
```

## File: `skills/integrate-whatsapp/scripts/set-data-endpoint.js`
```javascript
#!/usr/bin/env node
const { parseArgs, readFlagText } = require('./lib/cli');
const { platformRequest } = require('./lib/http');
const { run } = require('./lib/run');
const { requireFlowId } = require('./lib/whatsapp-flow');

run(async () => {
  const { flags } = parseArgs(process.argv.slice(2));
  const flowId = requireFlowId(flags);
  const code = await readFlagText(flags, 'code', 'code-file');
  if (!code) {
    throw new Error('Missing --code or --code-file');
  }

  return platformRequest({
    method: 'POST',
    path: `/platform/v1/whatsapp/flows/${flowId}/data_endpoint`,
    body: { code }
  });
});
```

## File: `skills/integrate-whatsapp/scripts/setup-encryption.js`
```javascript
#!/usr/bin/env node
const { parseArgs, getStringFlag } = require('./lib/cli');
const { platformRequest } = require('./lib/http');
const { run } = require('./lib/run');
const { requireFlowId } = require('./lib/whatsapp-flow');

run(async () => {
  const { flags } = parseArgs(process.argv.slice(2));
  const flowId = requireFlowId(flags);
  const phoneNumberId = getStringFlag(flags, 'phone-number-id') || getStringFlag(flags, 'phone_number_id');

  const body = {};
  if (phoneNumberId) {
    body.phone_number_id = phoneNumberId;
  }

  return platformRequest({
    method: 'POST',
    path: `/platform/v1/whatsapp/flows/${flowId}/setup_encryption`,
    body: Object.keys(body).length > 0 ? body : undefined
  });
});
```

## File: `skills/integrate-whatsapp/scripts/submit-template.mjs`
```
import { loadJsonPayload, parseArgs, requireFlag } from './lib/args.mjs';
import { metaProxyRequest } from './lib/request.mjs';
import { err, ok, printResult } from './lib/output.mjs';

function usage() {
  return {
    usage: 'node scripts/submit-template.mjs --business-account-id <WABA_ID> --json <payload> | --file <path>',
    env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY', 'META_GRAPH_VERSION (optional)'],
    hints: [
      'To discover business_account_id (WABA), run: node scripts/list-platform-phone-numbers.mjs',
      'This uses the same Meta endpoint as create-template; use whichever command name matches the task.'
    ]
  };
}

async function main() {
  const { flags, errors } = parseArgs(process.argv.slice(2));
  if (flags.help) {
    return printResult(ok(usage()));
  }
  if (errors.length > 0) {
    return printResult(err('Invalid arguments', { errors, ...usage() }));
  }

  try {
    const businessAccountId = requireFlag(flags, ['business-account-id', 'business_account_id'], 'business-account-id');
    const payload = await loadJsonPayload(flags);

    const response = await metaProxyRequest({
      method: 'POST',
      path: `${businessAccountId}/message_templates`,
      body: JSON.stringify(payload)
    });

    if (!response.ok) {
      return printResult(err('Meta proxy request failed', { response }));
    }

    return printResult(
      ok({
        response,
        note: 'Meta proxy template creation immediately submits to Meta; there is no Kapso draft state.'
      })
    );
  } catch (error) {
    return printResult(err('Failed to submit template', { message: String(error?.message || error), ...usage() }));
  }
}

main().then((code) => process.exit(code));
```

## File: `skills/integrate-whatsapp/scripts/template-status.mjs`
```
import { parseArgs, requireFlag } from './lib/args.mjs';
import { metaProxyRequest } from './lib/request.mjs';
import { err, ok, printResult } from './lib/output.mjs';

function usage() {
  return {
    usage: 'node scripts/template-status.mjs --business-account-id <WABA_ID> --name <template_name> [--fields <fields>]',
    env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY', 'META_GRAPH_VERSION (optional)'],
    hints: [
      'To discover business_account_id (WABA), run: node scripts/list-platform-phone-numbers.mjs',
      'To list all templates (and get ids/status), use scripts/list-templates.mjs.'
    ]
  };
}

async function main() {
  const { flags, errors } = parseArgs(process.argv.slice(2));
  if (flags.help) {
    return printResult(ok(usage()));
  }
  if (errors.length > 0) {
    return printResult(err('Invalid arguments', { errors, ...usage() }));
  }

  try {
    const businessAccountId = requireFlag(flags, ['business-account-id', 'business_account_id'], 'business-account-id');
    const name = requireFlag(flags, ['name', 'template-name', 'template_name'], 'name');
    const fields = flags.fields || 'name,status,category,language,components';

    const response = await metaProxyRequest({
      method: 'GET',
      path: `${businessAccountId}/message_templates`,
      query: { name, fields }
    });

    if (!response.ok) {
      return printResult(err('Meta proxy request failed', { response }));
    }

    return printResult(ok({ response }));
  } catch (error) {
    return printResult(err('Failed to fetch template status', { message: String(error?.message || error), ...usage() }));
  }
}

main().then((code) => process.exit(code));
```

## File: `skills/integrate-whatsapp/scripts/test.js`
```javascript
const { hasHelpFlag, parseFlags, requireFlag } = require('./lib/webhooks/args');
const { kapsoConfigFromEnv, kapsoRequest } = require('./lib/webhooks/kapso-api');

function ok(data) {
  return { ok: true, data };
}

function err(message, details) {
  return { ok: false, error: { message, details } };
}

async function main() {
  const argv = process.argv.slice(2);
  if (hasHelpFlag(argv)) {
    console.log(
      JSON.stringify(
        {
          ok: true,
          usage: 'node scripts/test.js --webhook-id <id> [--event-type <value>]',
          env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
        },
        null,
        2
      )
    );
    return 0;
  }

  try {
    const flags = parseFlags(argv);
    const webhookId = requireFlag(flags, 'webhook-id');
    const eventType = flags['event-type'];

    const params = new URLSearchParams();
    if (eventType && eventType !== true) {
      params.set('event_type', eventType);
    }

    const config = kapsoConfigFromEnv();
    const data = await kapsoRequest(
      config,
      `/platform/v1/whatsapp/webhooks/${encodeURIComponent(webhookId)}/test${params.toString() ? `?${params.toString()}` : ''}`,
      { method: 'POST' }
    );

    console.log(JSON.stringify(ok(data), null, 2));
    return 0;
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    console.error(JSON.stringify(err('Command failed', { message }), null, 2));
    return 1;
  }
}

main().then((code) => process.exit(code));
```

## File: `skills/integrate-whatsapp/scripts/update-flow-json.js`
```javascript
#!/usr/bin/env node
const { parseArgs, readFlagJson } = require('./lib/cli');
const { platformRequest } = require('./lib/http');
const { run } = require('./lib/run');
const { requireFlowId } = require('./lib/whatsapp-flow');

run(async () => {
  const { flags } = parseArgs(process.argv.slice(2));
  const flowId = requireFlowId(flags);
  const flowJson = await readFlagJson(flags, 'json', 'json-file');

  if (!flowJson) {
    throw new Error('Missing --json or --json-file');
  }

  return platformRequest({
    method: 'POST',
    path: `/platform/v1/whatsapp/flows/${flowId}/versions`,
    body: {
      flow_json: flowJson
    }
  });
});
```

## File: `skills/integrate-whatsapp/scripts/update-function.js`
```javascript
#!/usr/bin/env node
const { parseArgs, requireStringFlag, getStringFlag, readFlagText, readFlagJson } = require('./lib/cli');
const { platformRequest } = require('./lib/http');
const { run } = require('./lib/run');

run(async () => {
  const { flags } = parseArgs(process.argv.slice(2));
  const functionId = requireStringFlag(flags, 'function-id');
  const code = await readFlagText(flags, 'code', 'code-file');

  if (!code) {
    throw new Error('Missing --code or --code-file');
  }

  const runtimeConfig = await readFlagJson(flags, 'runtime-config', 'runtime-config-file');

  const body = {
    function: {
      name: getStringFlag(flags, 'name'),
      code,
      description: getStringFlag(flags, 'description'),
      runtime_config: runtimeConfig
    }
  };

  return platformRequest({
    method: 'PATCH',
    path: `/platform/v1/functions/${functionId}`,
    body
  });
});
```

## File: `skills/integrate-whatsapp/scripts/update-template.mjs`
```
import { loadJsonPayload, parseArgs, requireFlag } from './lib/args.mjs';
import { metaProxyRequest } from './lib/request.mjs';
import { err, ok, printResult } from './lib/output.mjs';

function usage() {
  return {
    usage: 'node scripts/update-template.mjs --business-account-id <WABA_ID> --hsm-id <template_id> --json <payload> | --file <path>',
    env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY', 'META_GRAPH_VERSION (optional)'],
    hints: [
      'To discover business_account_id (WABA), run: node scripts/list-platform-phone-numbers.mjs',
      'Find template id (hsm_id) via list-templates or template-status.'
    ]
  };
}

async function main() {
  const { flags, errors } = parseArgs(process.argv.slice(2));
  if (flags.help) {
    return printResult(ok(usage()));
  }
  if (errors.length > 0) {
    return printResult(err('Invalid arguments', { errors, ...usage() }));
  }

  try {
    const businessAccountId = requireFlag(flags, ['business-account-id', 'business_account_id'], 'business-account-id');
    const hsmId = requireFlag(flags, ['hsm-id', 'hsm_id'], 'hsm-id');
    const payload = await loadJsonPayload(flags);

    const response = await metaProxyRequest({
      method: 'POST',
      path: `${businessAccountId}/message_templates`,
      query: { hsm_id: hsmId },
      body: JSON.stringify(payload)
    });

    if (!response.ok) {
      return printResult(err('Meta proxy request failed', { response }));
    }

    return printResult(ok({ response }));
  } catch (error) {
    return printResult(err('Failed to update template', { message: String(error?.message || error), ...usage() }));
  }
}

main().then((code) => process.exit(code));
```

## File: `skills/integrate-whatsapp/scripts/update.js`
```javascript
const { kapsoConfigFromEnv, kapsoRequest } = require('./lib/webhooks/kapso-api');
const { hasHelpFlag, parseFlags, requireFlag } = require('./lib/webhooks/args');
const { buildWebhookPayload } = require('./lib/webhooks/webhook');

function ok(data) {
  return { ok: true, data };
}

function err(message, details) {
  return { ok: false, error: { message, details } };
}

function resolveScope(flags) {
  const raw = flags.scope;
  if (!raw || raw === true) {
    return 'config';
  }
  const scope = String(raw);
  if (scope !== 'config' && scope !== 'project') {
    throw new Error(`Invalid --scope value: ${scope}`);
  }
  return scope;
}

async function main() {
  const argv = process.argv.slice(2);
  if (hasHelpFlag(argv)) {
    console.log(
      JSON.stringify(
        {
          ok: true,
          usage:
            'node scripts/update.js --webhook-id <id> [--phone-number-id <id>] [--scope config|project] [--url ...] [--events ...] [--kind <kapso|meta>] [--payload-version v1|v2] [--buffer-enabled true|false] [--buffer-window-seconds <n>] [--max-buffer-size <n>] [--inactivity-minutes <n>] [--headers <json>] [--active true|false]',
          env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
        },
        null,
        2
      )
    );
    return 0;
  }

  try {
    const flags = parseFlags(argv);
    const scope = resolveScope(flags);
    const webhookId = requireFlag(flags, 'webhook-id');
    const payload = buildWebhookPayload(flags);
    if (Object.keys(payload).length === 0) {
      throw new Error('Provide at least one update field (e.g. --url, --events).');
    }

    const config = kapsoConfigFromEnv();
    let path = '';
    if (scope === 'project') {
      path = `/platform/v1/whatsapp/webhooks/${encodeURIComponent(webhookId)}`;
    } else {
      const phoneNumberId = requireFlag(flags, 'phone-number-id');
      path = `/platform/v1/whatsapp/phone_numbers/${encodeURIComponent(phoneNumberId)}/webhooks/${encodeURIComponent(webhookId)}`;
    }

    const data = await kapsoRequest(config, path, {
      method: 'PATCH',
      body: JSON.stringify({ whatsapp_webhook: payload })
    });

    console.log(JSON.stringify(ok(data), null, 2));
    return 0;
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    console.error(JSON.stringify(err('Command failed', { message }), null, 2));
    return 1;
  }
}

main().then((code) => process.exit(code));
```

## File: `skills/integrate-whatsapp/scripts/upload-media.mjs`
```
import { readFile } from 'node:fs/promises';
import path from 'node:path';

import { parseArgs, requireFlag } from './lib/args.mjs';
import { metaProxyRequest } from './lib/request.mjs';
import { err, ok, printResult } from './lib/output.mjs';

function usage() {
  return {
    usage: 'node scripts/upload-media.mjs --phone-number-id <PHONE_NUMBER_ID> --file <path> --mime-type <mime> [--filename <name>]',
    env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY', 'META_GRAPH_VERSION (optional)'],
    notes: ['This returns a media id for send-time headers, not a template header_handle.'],
    hints: ['To discover phone_number_id (Meta phone number id), run: node scripts/list-platform-phone-numbers.mjs']
  };
}

async function main() {
  const { flags, errors } = parseArgs(process.argv.slice(2));
  if (flags.help) {
    return printResult(ok(usage()));
  }
  if (errors.length > 0) {
    return printResult(err('Invalid arguments', { errors, ...usage() }));
  }

  try {
    const phoneNumberId = requireFlag(flags, ['phone-number-id', 'phone_number_id'], 'phone-number-id');
    const filePath = requireFlag(flags, ['file'], 'file');
    const mimeType = requireFlag(flags, ['mime-type', 'mime_type'], 'mime-type');
    const filename = flags.filename || path.basename(filePath);

    const fileBuffer = await readFile(filePath);
    const blob = new Blob([fileBuffer], { type: mimeType });
    const formData = new FormData();

    formData.append('messaging_product', 'whatsapp');
    formData.append('type', mimeType);
    formData.append('file', blob, filename);

    const response = await metaProxyRequest({
      method: 'POST',
      path: `${phoneNumberId}/media`,
      body: formData
    });

    if (!response.ok) {
      return printResult(err('Meta proxy request failed', { response }));
    }

    return printResult(ok({ response }));
  } catch (error) {
    return printResult(err('Failed to upload media', { message: String(error?.message || error), ...usage() }));
  }
}

main().then((code) => process.exit(code));
```

## File: `skills/integrate-whatsapp/scripts/upload-template-header-handle.mjs`
```
import { err, blocked, printResult } from './lib/output.mjs';

function usage() {
  return {
    usage: 'node scripts/upload-template-header-handle.mjs --file <path> --mime-type <mime> --resumable-app-id <app_id>',
    env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY', 'META_GRAPH_VERSION (optional)']
  };
}

function main() {
  try {
    return printResult(
      blocked('Meta proxy does not expose the resumable upload endpoints required for header_handle.', {
        missing_endpoints: [
          'POST /api/meta/vXX.X/{app_id}/uploads',
          'POST /api/meta/vXX.X/{upload_session_id}'
        ],
        notes: [
          'Use the Platform media ingest endpoint with delivery: meta_resumable_asset to obtain header_handle.',
          'Current proxy registry only supports POST /{phone_number_id}/media, which returns media_id (send-time only).'
        ],
        usage: usage()
      })
    );
  } catch (error) {
    return printResult(err('Failed to explain header handle limitations', { message: String(error?.message || error) }));
  }
}

main();
```

## File: `skills/integrate-whatsapp/scripts/lib/args.mjs`
```
import { readFile } from 'node:fs/promises';

export function parseArgs(argv) {
  const flags = {};
  const positionals = [];
  const errors = [];

  for (let index = 0; index < argv.length; index += 1) {
    const value = argv[index];

    if (!value.startsWith('--')) {
      positionals.push(value);
      continue;
    }

    const key = value.slice(2);
    if (!key) {
      errors.push('Invalid flag');
      continue;
    }

    if (key === 'help' || key === 'h') {
      flags.help = 'true';
      continue;
    }

    if (key.includes('=')) {
      const [flag, ...rest] = key.split('=');
      flags[flag] = rest.join('=');
      continue;
    }

    const nextValue = argv[index + 1];
    if (!nextValue || nextValue.startsWith('--')) {
      errors.push(`Missing value for --${key}`);
      continue;
    }

    flags[key] = nextValue;
    index += 1;
  }

  return { flags, positionals, errors };
}

export function getFlag(flags, names) {
  for (const name of names) {
    if (flags[name]) return flags[name];
  }
  return undefined;
}

export function requireFlag(flags, names, label) {
  const value = getFlag(flags, names);
  if (!value) {
    throw new Error(`Missing required flag: ${label}`);
  }
  return value;
}

export async function loadJsonPayload(flags) {
  const jsonValue = getFlag(flags, ['json', 'payload']);
  const fileValue = getFlag(flags, ['file']);

  if (jsonValue && fileValue) {
    throw new Error('Provide either --json or --file, not both');
  }

  if (jsonValue) {
    return JSON.parse(jsonValue);
  }

  if (fileValue) {
    const contents = await readFile(fileValue, 'utf8');
    return JSON.parse(contents);
  }

  throw new Error('Missing required JSON payload: use --json or --file');
}

export function parseJsonFlag(flags, name) {
  const value = flags[name];
  if (!value) return undefined;
  return JSON.parse(value);
}
```

## File: `skills/integrate-whatsapp/scripts/lib/cli.js`
```javascript
const { readFile } = require('fs/promises');

function parseArgs(argv) {
  const flags = {};
  const positionals = [];

  for (let index = 0; index < argv.length; index += 1) {
    const token = argv[index];

    if (!token.startsWith('--')) {
      positionals.push(token);
      continue;
    }

    const [rawKey, rawValue] = token.slice(2).split('=');
    if (rawValue !== undefined) {
      flags[rawKey] = rawValue;
      continue;
    }

    const next = argv[index + 1];
    if (next && !next.startsWith('--')) {
      flags[rawKey] = next;
      index += 1;
    } else {
      flags[rawKey] = true;
    }
  }

  return { flags, positionals };
}

function getFlag(flags, name) {
  return flags[name];
}

function getStringFlag(flags, name) {
  const value = getFlag(flags, name);
  if (value === undefined) return undefined;
  if (value === true) return 'true';
  return String(value);
}

function requireStringFlag(flags, name) {
  const value = getStringFlag(flags, name);
  if (!value) throw new Error(`Missing required flag --${name}`);
  return value;
}

function getBooleanFlag(flags, name) {
  const raw = getFlag(flags, name);
  if (raw === undefined) return undefined;
  if (raw === true) return true;
  const value = String(raw).toLowerCase();
  if (['true', '1', 'yes'].includes(value)) return true;
  if (['false', '0', 'no'].includes(value)) return false;
  throw new Error(`Invalid boolean for --${name}: ${raw}`);
}

function getNumberFlag(flags, name) {
  const raw = getStringFlag(flags, name);
  if (raw === undefined) return undefined;
  const value = Number(raw);
  if (Number.isNaN(value)) throw new Error(`Invalid number for --${name}: ${raw}`);
  return value;
}

async function readFlagText(flags, name, fileName) {
  const inlineValue = getStringFlag(flags, name);
  const fileValue = getStringFlag(flags, fileName);

  if (inlineValue && fileValue) {
    throw new Error(`Provide only one of --${name} or --${fileName}`);
  }

  if (fileValue) {
    return (await readFile(fileValue, 'utf8')).toString();
  }

  return inlineValue;
}

async function readFlagJson(flags, name, fileName) {
  const text = await readFlagText(flags, name, fileName);
  if (!text) return undefined;
  return JSON.parse(text);
}

module.exports = {
  parseArgs,
  getStringFlag,
  requireStringFlag,
  getBooleanFlag,
  getNumberFlag,
  readFlagText,
  readFlagJson
};
```

## File: `skills/integrate-whatsapp/scripts/lib/env.js`
```javascript
const DEFAULT_GRAPH_VERSION = 'v24.0';

function requireEnv(name) {
  const value = process.env[name];
  if (!value) throw new Error(`Missing required env var: ${name}`);
  return value;
}

function normalizeBaseUrl(raw) {
  const trimmed = raw.replace(/\/+$/, '');
  const metaMatch = trimmed.match(/^(.*)\/meta(?:\/whatsapp)?\/v\d+\.\d+$/);
  if (metaMatch) return metaMatch[1];
  if (trimmed.endsWith('/platform/v1')) return trimmed.slice(0, -'/platform/v1'.length);
  return trimmed;
}

function normalizeGraphVersion(version) {
  if (!version) return DEFAULT_GRAPH_VERSION;
  return version.startsWith('v') ? version : `v${version}`;
}

function getConfig() {
  const baseUrl = normalizeBaseUrl(requireEnv('KAPSO_API_BASE_URL'));
  return {
    baseUrl,
    apiKey: requireEnv('KAPSO_API_KEY'),
    graphVersion: normalizeGraphVersion(process.env.META_GRAPH_VERSION)
  };
}

module.exports = {
  getConfig
};
```

## File: `skills/integrate-whatsapp/scripts/lib/env.mjs`
```
function requireEnv(name) {
  const value = process.env[name];
  if (!value) {
    throw new Error(`Missing required env var: ${name}`);
  }
  return value;
}

function normalizeMetaBase(raw) {
  const trimmed = raw.replace(/\/+$/, '');
  if (trimmed.endsWith('/platform/v1')) {
    return `${trimmed.slice(0, -'/platform/v1'.length)}/meta/whatsapp`;
  }
  const metaMatch = trimmed.match(/^(.*)\/meta\/whatsapp(?:\/v\d+\.\d+)?$/);
  if (metaMatch) {
    return `${metaMatch[1]}/meta/whatsapp`;
  }
  const rawMetaMatch = trimmed.match(/^(.*)\/meta$/);
  if (rawMetaMatch) {
    return `${rawMetaMatch[1]}/meta/whatsapp`;
  }
  return `${trimmed}/meta/whatsapp`;
}

function normalizeGraphVersion(value) {
  if (!value) return 'v24.0';
  return value.startsWith('v') ? value : `v${value}`;
}

export function metaProxyConfig() {
  const rawBase = process.env.KAPSO_META_BASE_URL || requireEnv('KAPSO_API_BASE_URL');
  const baseUrl = normalizeMetaBase(rawBase);
  const apiKey = requireEnv('KAPSO_API_KEY');
  const graphVersion = normalizeGraphVersion(process.env.META_GRAPH_VERSION || 'v24.0');

  return {
    baseUrl,
    apiKey,
    graphVersion
  };
}
```

## File: `skills/integrate-whatsapp/scripts/lib/http.js`
```javascript
const { getConfig } = require('./env');

class RequestError extends Error {
  constructor(message, status, body) {
    super(message);
    this.status = status;
    this.body = body;
  }
}

function buildUrl(baseUrl, path, query) {
  const trimmed = baseUrl.replace(/\/+$/, '');
  const safePath = path.startsWith('/') ? path : `/${path}`;
  const url = new URL(`${trimmed}${safePath}`);

  if (query) {
    Object.entries(query).forEach(([key, value]) => {
      if (value === undefined || value === null) return;
      url.searchParams.set(key, String(value));
    });
  }

  return url.toString();
}

function isFormData(body) {
  return typeof FormData !== 'undefined' && body instanceof FormData;
}

function isBlob(body) {
  return typeof Blob !== 'undefined' && body instanceof Blob;
}

function isPlainObject(value) {
  return value !== null && typeof value === 'object' && value.constructor === Object;
}

async function request({ baseUrl, path, method, query, body, headers }) {
  const config = getConfig();
  const url = buildUrl(baseUrl, path, query);
  const finalHeaders = new Headers(headers || {});
  finalHeaders.set('X-API-Key', config.apiKey);

  let finalBody = body;

  if (body !== undefined && body !== null) {
    if (isPlainObject(body)) {
      finalBody = JSON.stringify(body);
      if (!finalHeaders.has('Content-Type')) {
        finalHeaders.set('Content-Type', 'application/json');
      }
    } else if (typeof body === 'string') {
      finalBody = body;
    } else if (isFormData(body) || isBlob(body)) {
      finalBody = body;
    }
  }

  const response = await fetch(url, {
    method,
    headers: finalHeaders,
    body: finalBody
  });

  const contentType = response.headers.get('content-type') || '';
  const text = await response.text();
  const parsed = contentType.includes('application/json') ? safeJson(text) : text;

  if (!response.ok) {
    throw new RequestError(`Request failed (${response.status})`, response.status, parsed);
  }

  return parsed;
}

function safeJson(text) {
  try {
    return JSON.parse(text);
  } catch {
    return text;
  }
}

function metaBaseUrl() {
  const config = getConfig();
  return `${config.baseUrl}/meta/whatsapp/${config.graphVersion}`;
}

function platformBaseUrl() {
  const config = getConfig();
  return config.baseUrl;
}

async function metaRequest(options) {
  return request({ baseUrl: metaBaseUrl(), ...options });
}

async function platformRequest(options) {
  return request({ baseUrl: platformBaseUrl(), ...options });
}

module.exports = {
  RequestError,
  metaRequest,
  platformRequest
};
```

## File: `skills/integrate-whatsapp/scripts/lib/output.js`
```javascript
function printOk(data) {
  // eslint-disable-next-line no-console
  console.log(JSON.stringify({ ok: true, data }, null, 2));
}

function printError(message, details) {
  // eslint-disable-next-line no-console
  console.error(JSON.stringify({ ok: false, error: { message, details } }, null, 2));
}

module.exports = {
  printOk,
  printError
};
```

## File: `skills/integrate-whatsapp/scripts/lib/output.mjs`
```
export function ok(data) {
  return { ok: true, data };
}

export function blocked(reason, details) {
  return { ok: true, blocked: true, ...details, reason };
}

export function err(message, details) {
  return { ok: false, error: { message, details } };
}

export function printResult(result) {
  const json = JSON.stringify(result, null, 2);

  // Skill runners sometimes only surface stdout. Print errors there too so
  // agents don't see only "exit status 2" with no details.
  // eslint-disable-next-line no-console
  console.log(json);

  return result.ok ? 0 : 2;
}
```

## File: `skills/integrate-whatsapp/scripts/lib/request.mjs`
```
import { metaProxyConfig } from './env.mjs';

function buildUrl(path, query) {
  const { baseUrl, graphVersion } = metaProxyConfig();
  const cleanedPath = path.replace(/^\/+/, '');
  const url = new URL(`${baseUrl}/${graphVersion}/${cleanedPath}`);

  if (query) {
    Object.entries(query).forEach(([key, value]) => {
      if (value === undefined || value === null || value === '') return;
      url.searchParams.set(key, String(value));
    });
  }

  return url;
}

function shouldParseJson(contentType) {
  return contentType && contentType.toLowerCase().includes('application/json');
}

export async function metaProxyRequest({ method, path, query, headers, body }) {
  const { apiKey } = metaProxyConfig();
  const url = buildUrl(path, query);
  const finalHeaders = new Headers(headers || {});

  finalHeaders.set('X-API-Key', apiKey);

  if (body && !(body instanceof FormData) && !finalHeaders.has('Content-Type')) {
    finalHeaders.set('Content-Type', 'application/json');
  }

  const response = await fetch(url, {
    method,
    headers: finalHeaders,
    body
  });

  const contentType = response.headers.get('content-type') || '';
  const text = await response.text();
  let data = text;

  if (text && shouldParseJson(contentType)) {
    try {
      data = JSON.parse(text);
    } catch {
      data = text;
    }
  }

  return {
    ok: response.ok,
    status: response.status,
    url: url.toString(),
    data
  };
}
```

## File: `skills/integrate-whatsapp/scripts/lib/run.js`
```javascript
const { printOk, printError } = require('./output');
const { RequestError } = require('./http');

async function run(action) {
  try {
    const data = await action();
    printOk(data);
    return 0;
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);

    if (error instanceof RequestError) {
      const blocked = error.status === 404;
      const details = {
        status: error.status,
        body: error.body,
        blocked
      };
      if (blocked) {
        details.hint = 'Endpoint not available in Meta proxy or Platform API yet.';
      }
      printError(message, details);
      return blocked ? 3 : 1;
    }

    printError(message, { blocked: false });
    return 1;
  }
}

module.exports = {
  run
};
```

## File: `skills/integrate-whatsapp/scripts/lib/whatsapp-flow.js`
```javascript
const { getStringFlag, requireStringFlag } = require('./cli');

function requireScope(flags) {
  const phoneNumberId = getStringFlag(flags, 'phone-number-id');
  const businessAccountId = getStringFlag(flags, 'business-account-id');

  if (!phoneNumberId && !businessAccountId) {
    throw new Error('Provide --phone-number-id or --business-account-id');
  }

  if (phoneNumberId && businessAccountId) {
    throw new Error('Provide only one of --phone-number-id or --business-account-id');
  }

  return { phoneNumberId, businessAccountId };
}

function requireScopeId(flags) {
  const scope = requireScope(flags);
  return scope.phoneNumberId || scope.businessAccountId;
}

function buildScopeQuery(flags) {
  const scope = requireScope(flags);
  return {
    phone_number_id: scope.phoneNumberId,
    business_account_id: scope.businessAccountId
  };
}

function requireFlowId(flags) {
  return requireStringFlag(flags, 'flow-id');
}

module.exports = {
  requireScope,
  requireScopeId,
  buildScopeQuery,
  requireFlowId
};
```

## File: `skills/integrate-whatsapp/scripts/lib/webhooks/args.js`
```javascript
function hasHelpFlag(argv) {
  return argv.includes('--help') || argv.includes('-h');
}

function parseFlags(argv) {
  const flags = {};
  for (let index = 0; index < argv.length; index += 1) {
    const arg = argv[index];
    if (!arg.startsWith('--')) {
      continue;
    }
    const trimmed = arg.slice(2);
    const eqIndex = trimmed.indexOf('=');
    if (eqIndex >= 0) {
      const key = trimmed.slice(0, eqIndex);
      const value = trimmed.slice(eqIndex + 1);
      flags[key] = value;
      continue;
    }
    const next = argv[index + 1];
    if (!next || next.startsWith('--')) {
      flags[trimmed] = true;
      continue;
    }
    flags[trimmed] = next;
    index += 1;
  }
  return flags;
}

function requireFlag(flags, name) {
  const value = flags[name];
  if (typeof value !== 'string' || value.length === 0) {
    throw new Error(`Missing required flag --${name}`);
  }
  return value;
}

function parseBoolean(value, name) {
  if (value === undefined) {
    return undefined;
  }
  if (value === true) {
    return true;
  }
  const normalized = String(value).toLowerCase();
  if (['true', '1', 'yes'].includes(normalized)) {
    return true;
  }
  if (['false', '0', 'no'].includes(normalized)) {
    return false;
  }
  throw new Error(`Invalid boolean for --${name}: ${value}`);
}

function parseNumber(value, name) {
  if (value === undefined || value === true) {
    return undefined;
  }
  const parsed = Number(value);
  if (Number.isNaN(parsed)) {
    throw new Error(`Invalid number for --${name}: ${value}`);
  }
  return parsed;
}

function parseJsonObject(value, name) {
  if (value === undefined || value === true) {
    return undefined;
  }
  try {
    const parsed = JSON.parse(value);
    if (!parsed || typeof parsed !== 'object' || Array.isArray(parsed)) {
      throw new Error('Expected JSON object');
    }
    return parsed;
  } catch (error) {
    throw new Error(`Invalid JSON for --${name}: ${String(error)}`);
  }
}

function parseStringArray(value, name) {
  if (value === undefined || value === true) {
    return undefined;
  }
  const trimmed = String(value).trim();
  if (trimmed.startsWith('[')) {
    try {
      const parsed = JSON.parse(trimmed);
      if (!Array.isArray(parsed)) {
        throw new Error('Expected JSON array');
      }
      return parsed.map((entry) => String(entry));
    } catch (error) {
      throw new Error(`Invalid JSON array for --${name}: ${String(error)}`);
    }
  }
  return trimmed.split(',').map((entry) => entry.trim()).filter(Boolean);
}

module.exports = {
  hasHelpFlag,
  parseFlags,
  requireFlag,
  parseBoolean,
  parseNumber,
  parseJsonObject,
  parseStringArray
};
```

## File: `skills/integrate-whatsapp/scripts/lib/webhooks/kapso-api.js`
```javascript
function requireEnv(name) {
  const value = process.env[name];
  if (!value) {
    throw new Error(`Missing required env var: ${name}`);
  }
  return value;
}

function normalizeBaseUrl(raw) {
  return raw.replace(/\/+$/, '');
}

function kapsoConfigFromEnv() {
  return {
    baseUrl: normalizeBaseUrl(requireEnv('KAPSO_API_BASE_URL')),
    apiKey: requireEnv('KAPSO_API_KEY')
  };
}

async function kapsoRequest(config, path, init = {}) {
  const url = `${config.baseUrl}${path}`;
  const headers = new Headers(init.headers || undefined);
  headers.set('X-API-Key', config.apiKey);
  if (!headers.has('Content-Type')) {
    headers.set('Content-Type', 'application/json');
  }

  const response = await fetch(url, { ...init, headers });
  const text = await response.text();

  if (!response.ok) {
    throw new Error(`Kapso API request failed (status=${response.status}) body=${text}`);
  }

  return text ? JSON.parse(text) : {};
}

module.exports = {
  kapsoConfigFromEnv,
  kapsoRequest
};
```

## File: `skills/integrate-whatsapp/scripts/lib/webhooks/webhook.js`
```javascript
const { parseBoolean, parseNumber, parseJsonObject, parseStringArray } = require('./args');

function buildWebhookPayload(flags) {
  const payload = {};
  if (typeof flags.url === 'string' && flags.url.length > 0) {
    payload.url = flags.url;
  }
  const events = parseStringArray(flags.events, 'events');
  if (events) {
    payload.events = events;
  }
  const active = parseBoolean(flags.active, 'active');
  if (active !== undefined) {
    payload.active = active;
  }
  if (typeof flags.kind === 'string' && flags.kind.length > 0) {
    payload.kind = flags.kind;
  }
  if (typeof flags['payload-version'] === 'string' && flags['payload-version'].length > 0) {
    payload.payload_version = flags['payload-version'];
  }
  const bufferEnabled = parseBoolean(flags['buffer-enabled'], 'buffer-enabled');
  if (bufferEnabled !== undefined) {
    payload.buffer_enabled = bufferEnabled;
  }
  const bufferWindowSeconds = parseNumber(flags['buffer-window-seconds'], 'buffer-window-seconds');
  if (bufferWindowSeconds !== undefined) {
    payload.buffer_window_seconds = bufferWindowSeconds;
  }
  const maxBufferSize = parseNumber(flags['max-buffer-size'], 'max-buffer-size');
  if (maxBufferSize !== undefined) {
    payload.max_buffer_size = maxBufferSize;
  }
  const inactivityMinutes = parseNumber(flags['inactivity-minutes'], 'inactivity-minutes');
  if (inactivityMinutes !== undefined) {
    payload.inactivity_minutes = inactivityMinutes;
  }
  const headers = parseJsonObject(flags.headers, 'headers');
  if (headers) {
    payload.headers = headers;
  }
  return payload;
}

module.exports = {
  buildWebhookPayload
};
```

## File: `skills/observe-whatsapp/SKILL.md`
```markdown
---
name: observe-whatsapp
description: "Observe and troubleshoot WhatsApp in Kapso: debug message delivery, inspect webhook deliveries/retries, triage API errors, and run health checks. Use when investigating production issues, message failures, or webhook delivery problems."
---

# Observe WhatsApp

## When to use

Use this skill for operational diagnostics: message delivery investigation, webhook delivery debugging, error triage, and WhatsApp health checks.

## Setup

Preferred path:
- Kapso CLI installed and authenticated (`kapso login`)
- Start with `kapso status` to confirm project access and available WhatsApp numbers

Fallback path:
Env vars:
- `KAPSO_API_BASE_URL` (host only, no `/platform/v1`)
- `KAPSO_API_KEY`

## How to

### Investigate message delivery

Preferred path:
1. Resolve the number: `kapso whatsapp numbers resolve --phone-number "<display-number>" --output json`
2. List recent messages: `kapso whatsapp messages list --phone-number "<display-number>" --limit 50 --output json`
3. Inspect a specific message: `kapso whatsapp messages get <message-id> --phone-number-id <id> --output json`
4. Inspect the conversation: `kapso whatsapp conversations list --phone-number "<display-number>" --output json`

Fallback path:
1. List messages: `node scripts/messages.js --phone-number-id <id>`
2. Inspect message: `node scripts/message-details.js --message-id <id>`
3. Find conversation: `node scripts/lookup-conversation.js --phone-number <e164>`

### Triage errors

Preferred path:
1. Confirm project and number state: `kapso status`
2. Run number health: `kapso whatsapp numbers health --phone-number "<display-number>" --output human`
3. Inspect related templates when relevant: `kapso whatsapp templates list --phone-number "<display-number>" --output json`

Fallback path:
1. Message errors: `node scripts/errors.js`
2. API logs: `node scripts/api-logs.js`
3. Webhook deliveries: `node scripts/webhook-deliveries.js`

### Run health checks

Preferred path:
1. Project overview: `kapso status`
2. Phone number health: `kapso whatsapp numbers health --phone-number "<display-number>" --output human`

Fallback path:
1. Project overview: `node scripts/overview.js`
2. Phone number health: `node scripts/whatsapp-health.js --phone-number-id <id>`

## Scripts

### Messages

| Script | Purpose |
|--------|---------|
| `messages.js` | List messages |
| `message-details.js` | Get message details |
| `lookup-conversation.js` | Find conversation by phone or ID |

### Errors and logs

| Script | Purpose |
|--------|---------|
| `errors.js` | List message errors |
| `api-logs.js` | List external API logs |
| `webhook-deliveries.js` | List webhook delivery attempts |

### Health

| Script | Purpose |
|--------|---------|
| `overview.js` | Project overview |
| `whatsapp-health.js` | Phone number health check |

### OpenAPI

| Script | Purpose |
|--------|---------|
| `openapi-explore.mjs` | Explore OpenAPI (search/op/schema/where) |

Install deps (once):
```bash
npm i
```

Examples:
```bash
node scripts/openapi-explore.mjs --spec platform search "webhook deliveries"
node scripts/openapi-explore.mjs --spec platform op listWebhookDeliveries
node scripts/openapi-explore.mjs --spec platform schema WebhookDelivery
```

## Notes

- For webhook setup (create/update/delete, signature verification, event types), use `integrate-whatsapp`.
- Prefer resolving a display phone number to the canonical `phone_number_id` before deep debugging.
- Keep the scripts as the fallback path when the CLI is unavailable or when you need API-log or webhook-delivery inspection.

## References

- [references/message-debugging-reference.md](references/message-debugging-reference.md) - Message debugging guide
- [references/triage-reference.md](references/triage-reference.md) - Error triage guide
- [references/health-reference.md](references/health-reference.md) - Health check guide

## Related skills

- `integrate-whatsapp` - Onboarding, webhooks, messaging, templates, flows
- `automate-whatsapp` - Workflows, agents, and automations

<!-- FILEMAP:BEGIN -->
```text
[observe-whatsapp file map]|root: .
|.:{package.json,SKILL.md}
|assets:{health-example.json,message-debugging-example.json,triage-example.json}
|references:{health-reference.md,message-debugging-reference.md,triage-reference.md}
|scripts:{api-logs.js,errors.js,lookup-conversation.js,message-details.js,messages.js,openapi-explore.mjs,overview.js,webhook-deliveries.js,whatsapp-health.js}
|scripts/lib/messages:{args.js,kapso-api.js}
|scripts/lib/status:{args.js,kapso-api.js}
|scripts/lib/triage:{args.js,kapso-api.js}
```
<!-- FILEMAP:END -->
```

## File: `skills/observe-whatsapp/package.json`
```json
{
  "private": true,
  "dependencies": {
    "yaml": "^2.6.0"
  },
  "scripts": {
    "openapi": "node scripts/openapi-explore.mjs"
  }
}

```

## File: `skills/observe-whatsapp/assets/health-example.json`
```json
{
  "status": "degraded",
  "checked_at": "2025-07-16T10:15:00Z",
  "checks": {
    "phone_number_access": { "passed": true },
    "token_validity": { "passed": true },
    "messaging_health": { "overall_status": "LIMITED" },
    "webhook_verified": { "passed": false },
    "webhook_subscription": { "passed": true }
  }
}
```

## File: `skills/observe-whatsapp/assets/message-debugging-example.json`
```json
{
  "message_id": "wamid.HBgMMTIzNDU2Nzg5",
  "timeline": [
    { "status": "sent", "at": "2025-07-16T09:40:00Z" },
    { "status": "delivered", "at": "2025-07-16T09:40:05Z" },
    { "status": "read", "at": "2025-07-16T09:41:12Z" }
  ]
}
```

## File: `skills/observe-whatsapp/assets/triage-example.json`
```json
{
  "errors": [
    {
      "source": "webhook_delivery",
      "event": "whatsapp.message.received",
      "status": "failed",
      "error": "Connection refused",
      "last_attempt_at": "2025-07-16T10:05:00Z"
    }
  ]
}
```

## File: `skills/observe-whatsapp/references/health-reference.md`
```markdown
# Health Check Interpretation

## 1) 60-second triage order

1. Confirm the health check ran (status + timestamp).
2. Identify the blocking check in this order:
   - `checks.phone_number_access.passed`
   - `checks.token_validity.passed` (only present on some configs)
   - `checks.messaging_health.overall_status` (BLOCKED = critical, LIMITED = degraded)
   - `checks.webhook_verified.passed`
   - `checks.webhook_subscription.passed`
   - `checks.test_message.passed` (only if a test was requested)
3. Lead with overall status (healthy/degraded/unhealthy), then name failing checks.

## 2) If status is "error"

Explain that the health check itself failed to run. Surface the error message and timestamp, then ask them to retry. If it repeats, collect JSON + config id for escalation.

## 3) Overall status (status)

This is the UI headline only. Always explain the underlying checks too.

- `healthy`: all required checks passed.
- `degraded`: core access works, but something needs attention (webhook, messaging limited, test failed).
- `unhealthy`: a critical requirement failed or messaging is blocked.
- `error`: health check failed to run.

## 4) Access token check (checks.token_validity)

Only present on some configs.

- passed: true -> token is valid.
- passed: false -> critical blocker.

Tell the user: token is invalid/expired or missing permissions. They cannot fix this directly; escalate to support.

## 5) Phone number access (checks.phone_number_access)

- passed: false -> critical blocker (Meta access is failing).
- passed: true -> show details if present.

Details:
- `details.verified_name`, `details.display_phone_number`, `details.quality_rating` (GREEN/YELLOW/RED).
- If `details.status` is "PENDING" (case-insensitive), treat as account under review.

Account under review guidance:
- "Meta is reviewing your account; this is normal and can take a few hours."
- Tell them to check Meta account status in WhatsApp Manager.

## 6) Messaging health (checks.messaging_health)

Use `checks.messaging_health.overall_status`:
- `AVAILABLE`: can send normally.
- `LIMITED`: partially restricted.
- `BLOCKED`: sending blocked.

If `checks.messaging_health.error` exists, say Meta status couldn't be retrieved.

### Entity-level diagnosis
If overall status is LIMITED or BLOCKED, inspect `checks.messaging_health.details.entities[]`.
Pick the most actionable entity:
1. Any BLOCKED entity with errors
2. Else any LIMITED entity with additional_info
3. Else any LIMITED/BLOCKED entity not BUSINESS
4. Else BUSINESS (only if it's the only limited one)

Entity name mapping:
- PHONE_NUMBER -> Phone Number
- WABA -> WhatsApp Business Account
- BUSINESS -> Business Portfolio
- APP -> Application
- MESSAGE_TEMPLATE -> Message Template

Description sources:
- additional_info joined if present
- else first error's error_description plus possible_solution
- else "Check Meta Business Suite for details"

Special case (payment method issue):
- If LIMITED with payment issue, explain templates are blocked but 24-hour window messages still work.

## 7) Webhook verification (checks.webhook_verified)

- passed: false -> inbound events won't work until verified.
- Message to user: "Meta hasn't verified the webhook yet; it will verify after a message is sent."

Steps:
1. Send a WhatsApp message to the business number.
2. Re-run health check.
3. Confirm `webhook_verified.passed` is true.

## 8) Webhook subscription (checks.webhook_subscription)

- passed: false -> app not subscribed to webhook events.
- If they used their own Meta app, this may still work; confirm actual inbound events.

## 9) Test message (checks.test_message)

- passed: false -> use error as primary explanation.
- Confirm the number used from `details.phone_number`.

Reminder: recipient must message first to open the 24-hour window.

## 10) What to collect when escalating

- timestamp, status
- any `checks.*.error` strings
- for limitations: entity_type, id, can_send_message, errors, additional_info
- phone number details: id, display_phone_number, status

## 11) Display name note

If display name is not approved, it affects cold message limits but is not usually the error source.

## 12) Special error

If you see error `141000`, tell the user to contact support.
```

## File: `skills/observe-whatsapp/references/message-debugging-reference.md`
```markdown
# Message Debugging Playbook

## Message delivery failed

1. Identify the message ID (`wamid.*`).
2. Review the status timeline in order: sent -> delivered -> read.
3. Surface error codes in status events and map to remediation.

## Common issues to confirm

- Recipient phone number formatting and registration.
- Template approval status (for business-initiated messages).
- Messaging health status (LIMITED/BLOCKED).
- Webhook subscription and inbound event receipt.
```

## File: `skills/observe-whatsapp/references/triage-reference.md`
```markdown
# Debugging Workflow

## Message delivery failed

1. Collect message ID (`wamid.*`).
2. Inspect message lifecycle timeline.
3. Translate error codes into user-facing guidance.

## WhatsApp config issues

1. Run a health check on the phone number config.
2. Review token validity, messaging health, and webhook subscription.
3. Explain whether the issue is critical or degraded.

## Webhook delivery failures

1. Review recent delivery attempts.
2. Check response status codes and error messages.
3. Verify webhook URL availability and signature verification logic.

## API errors

1. Review external API call logs.
2. Filter by status code or endpoint.
3. Identify auth errors, rate limits, or upstream failures.
```

## File: `skills/observe-whatsapp/scripts/api-logs.js`
```javascript
const { hasHelpFlag, parseFlags } = require('./lib/triage/args');
const { kapsoConfigFromEnv, kapsoRequest } = require('./lib/triage/kapso-api');

function err(message, details) {
  return { ok: false, error: { message, details } };
}

async function main() {
  const argv = process.argv.slice(2);
  if (hasHelpFlag(argv)) {
    console.log(
      JSON.stringify(
        {
          ok: true,
          usage:
            'node scripts/api-logs.js [--period <24h|7d|30d>] [--endpoint <value>] [--status-code <code>] [--errors-only true|false] [--page <n>] [--per-page <n>]',
          env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
        },
        null,
        2
      )
    );
    return 0;
  }

  try {
    const flags = parseFlags(argv);
    const params = new URLSearchParams();

    if (flags.period) params.set('period', flags.period);
    if (flags.endpoint) params.set('endpoint', flags.endpoint);
    if (flags['status-code']) params.set('status_code', flags['status-code']);
    if (flags['errors-only'] !== undefined) params.set('errors_only', flags['errors-only']);
    if (flags.page) params.set('page', flags.page);
    if (flags['per-page']) params.set('per_page', flags['per-page']);

    const suffix = params.toString();
    const config = kapsoConfigFromEnv();
    const data = await kapsoRequest(
      config,
      `/platform/v1/api_logs${suffix ? `?${suffix}` : ''}`
    );

    console.log(JSON.stringify({ ok: true, data }, null, 2));
    return 0;
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    console.error(JSON.stringify(err('Command failed', { message }), null, 2));
    return 1;
  }
}

main().then((code) => process.exit(code));
```

## File: `skills/observe-whatsapp/scripts/errors.js`
```javascript
const { hasHelpFlag, parseFlags } = require('./lib/triage/args');
const { kapsoConfigFromEnv, kapsoRequest } = require('./lib/triage/kapso-api');

function err(message, details) {
  return { ok: false, error: { message, details } };
}

async function main() {
  const argv = process.argv.slice(2);
  if (hasHelpFlag(argv)) {
    console.log(
      JSON.stringify(
        {
          ok: true,
          usage:
            'node scripts/errors.js [--period <24h|7d|30d>] [--source <message_delivery|api_call|webhook_delivery>] [--limit <n>] [--page <n>] [--phone-number <e164>]',
          env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
        },
        null,
        2
      )
    );
    return 0;
  }

  try {
    const flags = parseFlags(argv);
    const source = normalizeSource(flags.source);
    const limit = parseNumber(flags.limit, 20, 'limit');
    const page = parseNumber(flags.page, 1, 'page');
    const period = flags.period || '24h';
    const phoneNumber = flags['phone-number'];

    const config = kapsoConfigFromEnv();
    const result = { ok: true, period, sources: {}, notes: [] };

    if (!source || source === 'message_delivery') {
      const params = new URLSearchParams();
      params.set('status', 'failed');
      params.set('direction', 'outbound');
      params.set('per_page', String(limit));
      params.set('page', String(page));
      if (phoneNumber) params.set('phone_number', phoneNumber);

      const path = `/platform/v1/whatsapp/messages?${params.toString()}`;
      result.sources.message_delivery = await kapsoRequest(config, path);
      result.notes.push('Message failures use outbound status=failed and do not support period filtering.');
    }

    if (!source || source === 'api_call') {
      const params = new URLSearchParams();
      params.set('period', period);
      params.set('errors_only', 'true');
      params.set('per_page', String(limit));
      params.set('page', String(page));

      const path = `/platform/v1/api_logs?${params.toString()}`;
      result.sources.api_call = await kapsoRequest(config, path);
    }

    if (!source || source === 'webhook_delivery') {
      const params = new URLSearchParams();
      params.set('period', period);
      params.set('errors_only', 'true');
      params.set('per_page', String(limit));
      params.set('page', String(page));

      const path = `/platform/v1/webhook_deliveries?${params.toString()}`;
      result.sources.webhook_delivery = await kapsoRequest(config, path);
    }

    console.log(JSON.stringify(result, null, 2));
    return 0;
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    console.error(JSON.stringify(err('Command failed', { message }), null, 2));
    return 1;
  }
}

function normalizeSource(source) {
  if (!source || source === true) return null;
  const value = String(source).toLowerCase();
  const allowed = ['message_delivery', 'api_call', 'webhook_delivery'];
  if (!allowed.includes(value)) {
    throw new Error(`Invalid --source value: ${source}`);
  }
  return value;
}

function parseNumber(value, fallback, name) {
  if (value === undefined || value === true) return fallback;
  const parsed = Number(value);
  if (!Number.isFinite(parsed) || parsed <= 0) {
    throw new Error(`Invalid --${name} value: ${value}`);
  }
  return parsed;
}

main().then((code) => process.exit(code));
```

## File: `skills/observe-whatsapp/scripts/lookup-conversation.js`
```javascript
const { hasHelpFlag, parseFlags } = require('./lib/messages/args');
const { kapsoConfigFromEnv, kapsoRequest } = require('./lib/messages/kapso-api');

function ok(data) {
  return { ok: true, data };
}

function err(message, details) {
  return { ok: false, error: { message, details } };
}

async function main() {
  const argv = process.argv.slice(2);
  if (hasHelpFlag(argv)) {
    console.log(
      JSON.stringify(
        {
          ok: true,
          usage:
            'node scripts/lookup-conversation.js [--phone-number <e164>] [--phone-number-id <id>] [--conversation-id <uuid>] [--status <active|ended>] [--page <n>] [--per-page <n>]',
          env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
        },
        null,
        2
      )
    );
    return 0;
  }

  try {
    const flags = parseFlags(argv);
    const conversationId = flags['conversation-id'];
    const phoneNumber = flags['phone-number'];
    const phoneNumberId = flags['phone-number-id'] || flags.phone_number_id;

    const config = kapsoConfigFromEnv();

    if (conversationId && conversationId !== true) {
      const data = await kapsoRequest(
        config,
        `/platform/v1/whatsapp/conversations/${encodeURIComponent(conversationId)}`
      );
      console.log(JSON.stringify(ok(data), null, 2));
      return 0;
    }

    if ((!phoneNumber || phoneNumber === true) && !phoneNumberId) {
      throw new Error('Provide --conversation-id, --phone-number, or --phone-number-id');
    }

    const params = new URLSearchParams();
    if (phoneNumber && phoneNumber !== true) {
      params.set('phone_number', phoneNumber);
    }
    if (phoneNumberId) params.set('phone_number_id', phoneNumberId);
    if (flags.status) params.set('status', flags.status);
    if (flags.page) params.set('page', flags.page);
    if (flags['per-page']) params.set('per_page', flags['per-page']);

    const data = await kapsoRequest(
      config,
      `/platform/v1/whatsapp/conversations?${params.toString()}`
    );

    console.log(JSON.stringify(ok(data), null, 2));
    return 0;
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    console.error(JSON.stringify(err('Command failed', { message }), null, 2));
    return 1;
  }
}

main().then((code) => process.exit(code));
```

## File: `skills/observe-whatsapp/scripts/message-details.js`
```javascript
const { hasHelpFlag, parseFlags } = require('./lib/messages/args');
const { kapsoConfigFromEnv, kapsoRequest } = require('./lib/messages/kapso-api');

function ok(data) {
  return { ok: true, data };
}

function err(message, details) {
  return { ok: false, error: { message, details } };
}

async function main() {
  const argv = process.argv.slice(2);
  if (hasHelpFlag(argv)) {
    console.log(
      JSON.stringify(
        {
          ok: true,
          usage: 'node scripts/message-details.js --message-id <wamid>',
          env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
        },
        null,
        2
      )
    );
    return 0;
  }

  try {
    const flags = parseFlags(argv);
    const messageId = flags['message-id'];
    if (!messageId || messageId === true) {
      throw new Error('Missing required flag --message-id');
    }

    const config = kapsoConfigFromEnv();
    const data = await kapsoRequest(
      config,
      `/platform/v1/whatsapp/messages/${encodeURIComponent(messageId)}`
    );

    console.log(JSON.stringify(ok(data), null, 2));
    return 0;
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    console.error(JSON.stringify(err('Command failed', { message }), null, 2));
    return 1;
  }
}

main().then((code) => process.exit(code));
```

## File: `skills/observe-whatsapp/scripts/messages.js`
```javascript
const { hasHelpFlag, parseFlags } = require('./lib/messages/args');
const { kapsoConfigFromEnv, kapsoRequest } = require('./lib/messages/kapso-api');

function ok(data) {
  return { ok: true, data };
}

function err(message, details) {
  return { ok: false, error: { message, details } };
}

async function main() {
  const argv = process.argv.slice(2);
  if (hasHelpFlag(argv)) {
    console.log(
      JSON.stringify(
        {
          ok: true,
          usage:
            'node scripts/messages.js [--direction <inbound|outbound>] [--status <pending|sent|delivered|read|failed>] [--phone-number <e164>] [--conversation-id <uuid>] [--message-type <text|image|audio|video|document>] [--phone-number-id <id>] [--has-media true|false] [--page <n>] [--per-page <n>]',
          env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
        },
        null,
        2
      )
    );
    return 0;
  }

  try {
    const flags = parseFlags(argv);
    const params = new URLSearchParams();

    if (flags.direction) params.set('direction', flags.direction);
    if (flags.status) params.set('status', flags.status);
    if (flags['phone-number']) params.set('phone_number', flags['phone-number']);
    if (flags['conversation-id']) params.set('conversation_id', flags['conversation-id']);
    if (flags['message-type']) params.set('message_type', flags['message-type']);
    if (flags['phone-number-id']) params.set('phone_number_id', flags['phone-number-id']);
    if (flags.phone_number_id) params.set('phone_number_id', flags.phone_number_id);

    const hasMedia = parseBoolean(flags['has-media']);
    if (hasMedia !== undefined) params.set('has_media', String(hasMedia));

    if (flags.page) params.set('page', flags.page);
    if (flags['per-page']) params.set('per_page', flags['per-page']);

    const config = kapsoConfigFromEnv();
    const data = await kapsoRequest(
      config,
      `/platform/v1/whatsapp/messages${params.toString() ? `?${params.toString()}` : ''}`
    );

    console.log(JSON.stringify(ok(data), null, 2));
    return 0;
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    console.error(JSON.stringify(err('Command failed', { message }), null, 2));
    return 1;
  }
}

function parseBoolean(value) {
  if (value === undefined) return undefined;
  if (value === true) return true;
  const normalized = String(value).toLowerCase();
  if (['true', '1', 'yes'].includes(normalized)) return true;
  if (['false', '0', 'no'].includes(normalized)) return false;
  throw new Error(`Invalid boolean for --has-media: ${value}`);
}

main().then((code) => process.exit(code));
```

## File: `skills/observe-whatsapp/scripts/openapi-explore.mjs`
```
#!/usr/bin/env node

import { readFileSync, readdirSync, statSync } from 'fs'
import path from 'path'
import { fileURLToPath } from 'url'
import { parse as parseYaml } from 'yaml'

const HTTP_METHODS = ['get', 'post', 'put', 'patch', 'delete', 'options', 'head']
const DEFAULT_PUBLISHED_WHATSAPP_OPENAPI = 'https://docs.kapso.ai/api/meta/whatsapp/openapi-whatsapp.yaml'
const SCRIPT_DIR = path.dirname(fileURLToPath(import.meta.url))

function printHelp(exitCode = 0) {
  const msg = `
Explore OpenAPI specs (YAML)

Usage:
  node openapi-explore.mjs [openapi.yaml ...] <command> [args]
  node openapi-explore.mjs [--file <path> ...] <command> [args]
  node openapi-explore.mjs --all <command> [args]

Default (no files passed):
  Loads the published OpenAPI files from docs.kapso.ai:
  - ${DEFAULT_PUBLISHED_WHATSAPP_OPENAPI}
  - (plus platform + workflows, deduced from that URL)

Fallback:
  If it can't fetch the published specs (offline, etc.), it falls back to local repo files:
  api/**/openapi-*.yaml

Use --all to force local auto-discovery.

Commands:
  specs
  tags [--spec <id>]
  ops [--spec <id>] [--tag <tag>] [--q <query>]
  search <query> [--spec <id>]
  op <operationId | specId:operationId | "METHOD /path"> [--spec <id>]
  schema <SchemaName | specId:SchemaName> [--spec <id>]
  where <SchemaName | specId:SchemaName> [--spec <id>]

Flags:
  --file, -f <path>     Load a spec file (repeatable)
  --all                 Load all api/**/openapi-*.yaml files
  --spec <id>           Filter by spec id (platform, workflows, whatsapp, ...)
  --json                Output JSON (search/ops/where)
  --limit <n>           Limit results (default 30)
`
  console.log(msg.trim())
  process.exit(exitCode)
}

function die(msg, exitCode = 1) {
  console.error(msg)
  process.exit(exitCode)
}

function parseArgs(argv) {
  const args = [...argv]
  const opts = { files: [], all: false, spec: null, json: false, limit: 30, tag: null, q: null }
  let command = null
  const rest = []

  for (let i = 0; i < args.length; i++) {
    const a = args[i]
    if (a === '--help' || a === '-h') printHelp(0)

    if (a === '--all') {
      opts.all = true
      continue
    }
    if (a === '--json') {
      opts.json = true
      continue
    }
    if (a === '--file' || a === '-f') {
      const p = args[++i]
      if (!p) die('Missing value for --file')
      opts.files.push(p)
      continue
    }
    if (a === '--spec') {
      opts.spec = args[++i] || null
      if (!opts.spec) die('Missing value for --spec')
      continue
    }
    if (a === '--limit') {
      const raw = args[++i]
      const n = Number(raw)
      if (!Number.isFinite(n) || n <= 0) die(`Invalid --limit: ${raw}`)
      opts.limit = n
      continue
    }
    if (a === '--tag') {
      opts.tag = args[++i] || null
      if (!opts.tag) die('Missing value for --tag')
      continue
    }
    if (a === '--q') {
      opts.q = args[++i] || null
      if (!opts.q) die('Missing value for --q')
      continue
    }

    if (!command && (a.endsWith('.yaml') || a.endsWith('.yml'))) {
      opts.files.push(a)
      continue
    }

    if (!command) command = a
    else rest.push(a)
  }

  return { opts, command, rest }
}

function walk(dir, { filePattern, maxDepth = 10 } = {}, depth = 0, out = []) {
  if (depth > maxDepth) return out
  let entries
  try {
    entries = readdirSync(dir)
  } catch {
    return out
  }

  for (const entry of entries) {
    const full = path.join(dir, entry)
    let st
    try {
      st = statSync(full)
    } catch {
      continue
    }

    if (st.isDirectory()) {
      walk(full, { filePattern, maxDepth }, depth + 1, out)
    } else if (!filePattern || filePattern.test(entry)) {
      out.push(full)
    }
  }

  return out
}

function findUpDir(startDir, targetDirName, { maxDepth = 12 } = {}) {
  let current = path.resolve(startDir)
  for (let i = 0; i <= maxDepth; i++) {
    const candidate = path.join(current, targetDirName)
    try {
      const st = statSync(candidate)
      if (st.isDirectory()) return candidate
    } catch {
      // ignore
    }

    const parent = path.dirname(current)
    if (parent === current) break
    current = parent
  }
  return null
}

function findLocalApiDir() {
  return findUpDir(process.cwd(), 'api') || findUpDir(SCRIPT_DIR, 'api')
}

function isUrl(s) {
  return /^https?:\/\//i.test(String(s))
}

function deducePublishedOpenApiUrls(whatsappUrl = DEFAULT_PUBLISHED_WHATSAPP_OPENAPI) {
  const u = new URL(whatsappUrl)
  const origin = u.origin
  return [
    whatsappUrl,
    new URL('/api/platform/v1/openapi-platform.yaml', origin).toString(),
    new URL('/api/platform/v1/openapi-workflows.yaml', origin).toString(),
  ]
}

function inferSpecId(filePath, spec) {
  const base = (isUrl(filePath) ? path.basename(new URL(filePath).pathname) : path.basename(filePath)).toLowerCase()
  if (base.includes('whatsapp')) return 'whatsapp'
  if (base.includes('workflows')) return 'workflows'
  if (base.includes('platform')) return 'platform'

  const title = (spec?.info?.title || '').toLowerCase()
  if (title.includes('whatsapp')) return 'whatsapp'
  if (title.includes('workflow')) return 'workflows'
  if (title.includes('platform')) return 'platform'

  return base.replace(/^openapi-/, '').replace(/\.(ya?ml)$/, '') || 'spec'
}

function decodeJsonPointerToken(token) {
  return token.replaceAll('~1', '/').replaceAll('~0', '~')
}

function getByJsonPointer(doc, pointer) {
  if (!pointer || !pointer.startsWith('#/')) return null
  const parts = pointer.slice(2).split('/').map(decodeJsonPointerToken)
  let cur = doc
  for (const part of parts) {
    if (cur == null) return null
    cur = cur[part]
  }
  return cur ?? null
}

function refName(ref) {
  if (!ref) return null
  const parts = String(ref).split('/')
  return parts[parts.length - 1] || null
}

function derefObject(obj, doc, stack = new Set()) {
  if (!obj?.$ref) return obj
  const ref = String(obj.$ref)
  if (stack.has(ref)) return obj
  stack.add(ref)
  const resolved = getByJsonPointer(doc, ref)
  if (!resolved) return obj
  return derefObject(resolved, doc, stack)
}

function schemaTypeString(schema) {
  if (!schema) return 'any'
  if (schema.$ref) return refName(schema.$ref) || 'ref'
  if (schema.const !== undefined) return `const ${JSON.stringify(schema.const)}`
  if (schema.enum?.length) {
    const vals = schema.enum.slice(0, 6).map((v) => JSON.stringify(v)).join(' | ')
    return schema.enum.length > 6 ? `enum(${vals} | ...)` : `enum(${vals})`
  }
  if (schema.type) {
    if (Array.isArray(schema.type)) return schema.type.join('|')
    return schema.type
  }
  if (schema.oneOf) return 'oneOf'
  if (schema.anyOf) return 'anyOf'
  if (schema.allOf) return 'allOf'
  if (schema.properties) return 'object'
  if (schema.items) return 'array'
  return 'any'
}

function normalizeType(schema) {
  if (!schema) return null
  const t = schema.type
  if (!t) return null
  if (Array.isArray(t)) {
    const nonNull = t.find((x) => x !== 'null')
    return nonNull || t[0] || null
  }
  return t
}

function mergeAllOf(schema, doc, seen = new Set()) {
  if (!schema?.allOf?.length) return schema

  const out = { ...schema }
  delete out.allOf

  let merged = { type: 'object', properties: {}, required: [] }

  for (const part of schema.allOf) {
    let s = part
    if (s?.$ref) {
      const name = refName(s.$ref)
      if (name) {
        if (seen.has(name)) continue
        seen.add(name)
      }
      s = getByJsonPointer(doc, s.$ref) || s
    }
    if (s?.allOf) s = mergeAllOf(s, doc, seen)

    if (s?.type && normalizeType(s) !== 'object' && s.properties) {
      // some specs omit type: object but still have properties
    } else if (normalizeType(s) && normalizeType(s) !== 'object' && !s.properties) {
      return schema
    }

    if (s?.properties) Object.assign(merged.properties, s.properties)
    if (Array.isArray(s?.required)) merged.required.push(...s.required)
    if (s?.description && !merged.description) merged.description = s.description
  }

  merged.required = [...new Set(merged.required)]
  return { ...merged, ...out }
}

function formatSchemaPreview(schema, doc, { depth = 2, maxProps = 12 } = {}, indent = '', refStack = new Set()) {
  if (!schema) return [`${indent}any`]

  if (schema.$ref) {
    const name = refName(schema.$ref) || schema.$ref
    const resolved = getByJsonPointer(doc, schema.$ref)
    const lines = [`${indent}${name}`]
    const refKey = String(schema.$ref)
    if (refStack.has(refKey)) return lines
    refStack.add(refKey)
    if (resolved && depth > 0) {
      const next = resolved?.allOf ? mergeAllOf(resolved, doc) : resolved
      const childLines = formatSchemaPreview(next, doc, { depth, maxProps }, indent + '  ', refStack)
      // Avoid printing a single redundant "object" line for refs
      if (!(childLines.length === 1 && childLines[0].trim() === 'object')) lines.push(...childLines)
    }
    refStack.delete(refKey)
    return lines
  }

  const normalized = schema.allOf ? mergeAllOf(schema, doc) : schema

  const t = normalizeType(normalized) || schemaTypeString(normalized)
  if (t === 'object' || normalized.properties) {
    const props = normalized.properties || {}
    const required = new Set(normalized.required || [])
    const keys = Object.keys(props)
    if (!keys.length) return [`${indent}object`]

    const lines = []
    for (const key of keys.slice(0, maxProps)) {
      const s = props[key]
      const typeStr = schemaTypeString(s)
      const req = required.has(key) ? ' (required)' : ''
      const desc = s?.description ? ` - ${String(s.description).replaceAll('\n', ' ').slice(0, 80)}` : ''
      lines.push(`${indent}- ${key}: ${typeStr}${req}${desc}`)
      if (depth > 0) {
        const child = s?.$ref ? getByJsonPointer(doc, s.$ref) : s
        const childNorm = child?.allOf ? mergeAllOf(child, doc) : child
        const childType = normalizeType(childNorm)
        if (childType === 'object' || childNorm?.properties || childNorm?.items) {
          const nested = formatSchemaPreview(childNorm, doc, { depth: depth - 1, maxProps }, indent + '  ', refStack)
          // Only include nested if it adds something beyond "object"/"array"
          if (!(nested.length === 1 && ['object', 'array'].includes(nested[0].trim()))) lines.push(...nested)
        }
      }
    }
    if (keys.length > maxProps) lines.push(`${indent}- ... (${keys.length - maxProps} more)`)
    return lines
  }

  if (t === 'array' || normalized.items) {
    const itemType = schemaTypeString(normalized.items)
    const lines = [`${indent}array<${itemType}>`]
    if (normalized.items && depth > 0) {
      const next = normalized.items?.$ref ? getByJsonPointer(doc, normalized.items.$ref) : normalized.items
      const nextNorm = next?.allOf ? mergeAllOf(next, doc) : next
      const nested = formatSchemaPreview(nextNorm, doc, { depth: depth - 1, maxProps }, indent + '  ', refStack)
      const nestedTrim = nested.length === 1 ? nested[0].trim() : null
      const redundant =
        nestedTrim === null ? false : ['object', 'array'].includes(nestedTrim) || nestedTrim === itemType
      if (!redundant) lines.push(...nested)
    }
    return lines
  }

  if (normalized.oneOf?.length) {
    const opts = normalized.oneOf.slice(0, 5).map((s) => schemaTypeString(s)).join(' | ')
    return [`${indent}oneOf(${opts}${normalized.oneOf.length > 5 ? ' | ...' : ''})`]
  }
  if (normalized.anyOf?.length) {
    const opts = normalized.anyOf.slice(0, 5).map((s) => schemaTypeString(s)).join(' | ')
    return [`${indent}anyOf(${opts}${normalized.anyOf.length > 5 ? ' | ...' : ''})`]
  }

  return [`${indent}${schemaTypeString(normalized)}`]
}

function placeholderForString(schema) {
  if (schema?.enum?.length) return schema.enum[0]
  if (schema?.const !== undefined) return schema.const
  if (schema?.format === 'uuid') return '00000000-0000-0000-0000-000000000000'
  if (schema?.format === 'date-time') return '2025-01-01T00:00:00Z'
  if (schema?.format === 'date') return '2025-01-01'
  if (schema?.format === 'email') return 'user@example.com'
  if (schema?.format === 'uri' || schema?.format === 'url') return 'https://example.com'
  return 'string'
}

function exampleFromSchema(schema, doc, { depth = 3, includeOptional = false } = {}, stack = new Set()) {
  if (!schema) return null

  if (schema.$ref) {
    const name = refName(schema.$ref)
    if (name) {
      if (stack.has(name)) return `<circular:${name}>`
      stack.add(name)
    }
    const resolved = getByJsonPointer(doc, schema.$ref)
    const out = exampleFromSchema(resolved || {}, doc, { depth, includeOptional }, stack)
    if (name) stack.delete(name)
    return out
  }

  const normalized = schema.allOf ? mergeAllOf(schema, doc) : schema

  if (normalized.const !== undefined) return normalized.const
  if (normalized.enum?.length) return normalized.enum[0]

  const t = normalizeType(normalized)
  if (t === 'string') return placeholderForString(normalized)
  if (t === 'integer') return 0
  if (t === 'number') return 0
  if (t === 'boolean') return true
  if (t === 'null') return null

  if ((t === 'array' || normalized.items) && depth > 0) {
    return [exampleFromSchema(normalized.items || {}, doc, { depth: depth - 1, includeOptional }, stack)]
  }

  if ((t === 'object' || normalized.properties || normalized.additionalProperties) && depth > 0) {
    const props = normalized.properties || {}
    const required = new Set(normalized.required || [])
    const out = {}

    const keys = Object.keys(props)
    for (const key of keys) {
      if (!includeOptional && !required.has(key)) continue
      out[key] = exampleFromSchema(props[key], doc, { depth: depth - 1, includeOptional }, stack)
    }

    // If it is a free-form map, add a placeholder entry.
    if (!keys.length && normalized.additionalProperties) {
      out.key = exampleFromSchema(
        normalized.additionalProperties === true ? {} : normalized.additionalProperties,
        doc,
        { depth: depth - 1, includeOptional },
        stack,
      )
    }

    return out
  }

  if (normalized.oneOf?.length) return exampleFromSchema(normalized.oneOf[0], doc, { depth, includeOptional }, stack)
  if (normalized.anyOf?.length) return exampleFromSchema(normalized.anyOf[0], doc, { depth, includeOptional }, stack)

  return null
}

function collectSchemaRefs(schema, doc, out = new Set(), stack = new Set()) {
  if (!schema) return out

  if (schema.$ref) {
    const name = refName(schema.$ref)
    if (name) out.add(name)
    if (name) {
      if (stack.has(name)) return out
      stack.add(name)
    }
    const resolved = getByJsonPointer(doc, schema.$ref)
    if (resolved) collectSchemaRefs(resolved, doc, out, stack)
    if (name) stack.delete(name)
    return out
  }

  const normalized = schema.allOf ? mergeAllOf(schema, doc) : schema

  for (const key of ['oneOf', 'anyOf', 'allOf']) {
    if (Array.isArray(normalized[key])) {
      for (const s of normalized[key]) collectSchemaRefs(s, doc, out, stack)
    }
  }

  if (normalized.properties) {
    for (const s of Object.values(normalized.properties)) collectSchemaRefs(s, doc, out, stack)
  }
  if (normalized.items) collectSchemaRefs(normalized.items, doc, out, stack)
  if (normalized.additionalProperties && normalized.additionalProperties !== true) {
    collectSchemaRefs(normalized.additionalProperties, doc, out, stack)
  }

  return out
}

function collectSchemaFieldNames(schema, doc, out = new Set(), stack = new Set(), depth = 3) {
  if (!schema || depth < 0) return out

  if (schema.$ref) {
    const ref = String(schema.$ref)
    if (stack.has(ref)) return out
    stack.add(ref)
    const resolved = getByJsonPointer(doc, ref)
    if (resolved) collectSchemaFieldNames(resolved, doc, out, stack, depth)
    stack.delete(ref)
    return out
  }

  const normalized = schema.allOf ? mergeAllOf(schema, doc) : schema

  for (const key of ['oneOf', 'anyOf', 'allOf']) {
    if (Array.isArray(normalized[key])) {
      for (const s of normalized[key]) collectSchemaFieldNames(s, doc, out, stack, depth)
    }
  }

  if (normalized.properties) {
    for (const [k, s] of Object.entries(normalized.properties)) {
      out.add(k)
      collectSchemaFieldNames(s, doc, out, stack, depth - 1)
    }
  }

  if (normalized.items) collectSchemaFieldNames(normalized.items, doc, out, stack, depth - 1)
  if (normalized.additionalProperties && normalized.additionalProperties !== true) {
    collectSchemaFieldNames(normalized.additionalProperties, doc, out, stack, depth - 1)
  }

  return out
}

function normalizeOperationSecurity(op, spec) {
  if (Object.prototype.hasOwnProperty.call(op, 'security')) return op.security
  return spec.security
}

function securityLabel(opSecurity, spec) {
  if (!opSecurity) return null
  if (Array.isArray(opSecurity) && opSecurity.length === 0) return 'none'

  const schemes = spec?.components?.securitySchemes || {}

  function schemeLabel(name) {
    const s = schemes[name]
    if (!s) return name
    if (s.type === 'apiKey' && s.in === 'header' && s.name) return `${name} (${s.name} header)`
    if (s.type === 'apiKey' && s.in) return `${name} (apiKey in ${s.in})`
    if (s.type === 'http' && s.scheme === 'bearer') return `${name} (Authorization: Bearer ...)`
    if (s.type === 'http') return `${name} (http ${s.scheme || ''})`.trim()
    return `${name} (${s.type})`
  }

  const requirementSets = []
  for (const req of opSecurity || []) {
    const keys = Object.keys(req || {})
    if (!keys.length) continue
    requirementSets.push(keys.map(schemeLabel).join(' + '))
  }

  if (!requirementSets.length) return null
  return requirementSets.join(' OR ')
}

function toShortSpec(s) {
  return {
    id: s.id,
    title: s.title,
    version: s.version,
    file: s.filePath,
    servers: s.servers,
    operations: s.operations.length,
    schemas: Object.keys(s.schemas).length,
  }
}

async function readSpecSource(source) {
  if (isUrl(source)) {
    const res = await fetch(source, {
      // Some CDNs / WAFs behave better with a UA.
      headers: { 'User-Agent': 'kapso-openapi-explore/1.0 (+https://docs.kapso.ai)' },
    })
    if (!res.ok) throw new Error(`HTTP ${res.status} ${res.statusText}`)
    return await res.text()
  }
  return readFileSync(source, 'utf-8')
}

async function loadSpecsAsync({ sources, sourceMode, specFilter }) {
  if (!sources.length) die('No OpenAPI sources provided')

  const seenIds = new Map()
  const specs = []
  const errors = []

  for (const filePath of sources) {
    let raw = null
    try {
      raw = await readSpecSource(filePath)
    } catch (e) {
      errors.push({ source: filePath, error: e })
      if (sourceMode === 'explicit') console.error(`Skipping ${filePath}: ${e.message}`)
      continue
    }

    let doc
    try {
      doc = parseYaml(raw)
    } catch (e) {
      errors.push({ source: filePath, error: e })
      console.error(`Skipping ${filePath}: YAML parse error: ${e.message}`)
      continue
    }

    const idBase = inferSpecId(filePath, doc)
    const n = (seenIds.get(idBase) || 0) + 1
    seenIds.set(idBase, n)
    const id = n === 1 ? idBase : `${idBase}${n}`

    if (specFilter && id !== specFilter) continue

    const title = doc?.info?.title || id
    const version = doc?.info?.version || '?'
    const servers = (doc?.servers || []).map((s) => s?.url).filter(Boolean)
    const tags = doc?.tags || []
    const schemas = doc?.components?.schemas || {}
    const schemaFieldCache = new Map()

    const getSchemaFields = (schemaName) => {
      if (schemaFieldCache.has(schemaName)) return schemaFieldCache.get(schemaName)
      const schema = schemas?.[schemaName]
      const fields = schema ? [...collectSchemaFieldNames(schema, doc)] : []
      schemaFieldCache.set(schemaName, fields)
      return fields
    }

    const operations = []
    const paths = doc?.paths || {}
    for (const [p, pathItemRaw] of Object.entries(paths)) {
      const pathItem = pathItemRaw || {}
      const pathParams = Array.isArray(pathItem.parameters) ? pathItem.parameters.map((x) => derefObject(x, doc)) : []

      for (const method of HTTP_METHODS) {
        const op = pathItem[method]
        if (!op) continue

        const mergedParams = [...pathParams, ...((op.parameters || []).filter(Boolean))]
          .map((x) => derefObject(x, doc))
          .filter(Boolean)
        const opSecurity = normalizeOperationSecurity(op, doc)
        const opRequestBody = derefObject(op.requestBody || null, doc)

        const refs = new Set()
        // params
        for (const param of mergedParams) {
          if (param?.schema) collectSchemaRefs(param.schema, doc, refs)
          if (param?.content) {
            for (const media of Object.values(param.content)) {
              if (media?.schema) collectSchemaRefs(media.schema, doc, refs)
            }
          }
        }
        // body
        if (opRequestBody?.content) {
          for (const media of Object.values(opRequestBody.content)) {
            if (media?.schema) collectSchemaRefs(media.schema, doc, refs)
          }
        }
        // responses
        if (op?.responses) {
          for (const resp of Object.values(op.responses)) {
            const r = derefObject(resp, doc)
            if (r?.content) {
              for (const media of Object.values(r.content)) {
                if (media?.schema) collectSchemaRefs(media.schema, doc, refs)
              }
            }
          }
        }

        const fieldsUsed = new Set()
        for (const schemaName of refs) {
          for (const f of getSchemaFields(schemaName)) fieldsUsed.add(f)
        }

        operations.push({
          specId: id,
          specTitle: title,
          specFile: filePath,
          method,
          path: p,
          operationId: op.operationId || null,
          summary: op.summary || null,
          description: op.description || null,
          tags: op.tags || [],
          deprecated: Boolean(op.deprecated),
          security: opSecurity,
          securityLabel: securityLabel(opSecurity, doc),
          parameters: mergedParams,
          requestBody: opRequestBody,
          responses: op.responses || {},
          refsUsed: refs,
          fieldsUsed,
        })
      }
    }

    specs.push({
      id,
      filePath,
      title,
      version,
      servers,
      doc,
      tags,
      schemas,
      operations,
    })
  }

  if (!specs.length) {
    if (sourceMode === 'default_remote' && errors.length) {
      const apiDir = findLocalApiDir()
      const local = apiDir ? walk(apiDir, { filePattern: /^openapi-.*\.ya?ml$/ }) : []
      if (local.length) {
        console.error(`Could not fetch published OpenAPI specs. Falling back to local repo specs (api/**/openapi-*.yaml).`)
        return await loadSpecsAsync({ sources: local, sourceMode: 'explicit', specFilter })
      }
    }
    if (specFilter) die(`No specs matched --spec ${specFilter}`)
    die('No specs loaded')
  }

  if (sourceMode === 'default_remote' && errors.length) {
    console.error(`Some published OpenAPI specs could not be fetched:`)
    for (const e of errors) console.error(`- ${e.source}: ${e.error?.message || String(e.error)}`)
  }

  return specs
}

function findOperation(specs, query, { specHint } = {}) {
  const raw = query.trim()
  const direct = raw.includes(':') ? raw.split(':') : null
  const qSpec = direct?.[0] || specHint
  const qId = direct?.[1] || raw

  // METHOD /path
  const m = raw.match(/^(get|post|put|patch|delete|options|head)\\s+(.+)$/i)
  if (m) {
    const method = m[1].toLowerCase()
    const p = m[2].trim()
    const matches = []
    for (const s of specs) {
      if (qSpec && s.id !== qSpec) continue
      for (const op of s.operations) {
        if (op.method === method && op.path === p) matches.push(op)
      }
    }
    return matches
  }

  // operationId
  const matches = []
  for (const s of specs) {
    if (qSpec && s.id !== qSpec) continue
    for (const op of s.operations) {
      if (op.operationId === qId) matches.push(op)
    }
  }
  return matches
}

function findSchema(specs, query, { specHint } = {}) {
  const raw = query.trim()
  const direct = raw.includes(':') ? raw.split(':') : null
  const qSpec = direct?.[0] || specHint
  const qName = direct?.[1] || raw

  const matches = []
  for (const s of specs) {
    if (qSpec && s.id !== qSpec) continue
    if (Object.prototype.hasOwnProperty.call(s.schemas, qName)) {
      matches.push({ spec: s, name: qName, schema: s.schemas[qName] })
    }
  }
  return matches
}

function scoreText(hay, q) {
  if (!hay) return 0
  const h = hay.toLowerCase()
  if (h === q) return 100
  if (h.startsWith(q)) return 60
  if (h.includes(q)) return 30
  return 0
}

function search(specs, query, { specHint, limit = 30 } = {}) {
  const q = query.toLowerCase().trim()
  if (!q) return { ops: [], schemas: [] }

  const ops = []
  const schemas = []

  for (const s of specs) {
    if (specHint && s.id !== specHint) continue

    for (const op of s.operations) {
      let score = 0
      score += scoreText(op.operationId, q) * 3
      score += scoreText(`${op.method} ${op.path}`, q) * 2
      score += scoreText(op.summary, q) * 2
      score += scoreText(op.description, q)
      for (const t of op.tags || []) score += scoreText(t, q) * 2
      score += scoreText((op.parameters || []).map((p) => p?.name).filter(Boolean).join(' '), q) * 2
      score += scoreText([...op.refsUsed].join(' '), q) * 2
      score += scoreText([...op.fieldsUsed].join(' '), q)
      if (score > 0) ops.push({ score, op })
    }

    for (const [name, schema] of Object.entries(s.schemas)) {
      let score = 0
      score += scoreText(name, q) * 3
      score += scoreText(schema?.description, q)
      score += scoreText([...collectSchemaFieldNames(schema, s.doc)].join(' '), q) * 2
      if (score > 0) schemas.push({ score, spec: s, name, schema })
    }
  }

  ops.sort((a, b) => b.score - a.score)
  schemas.sort((a, b) => b.score - a.score)

  return {
    ops: ops.slice(0, limit).map((x) => x.op),
    schemas: schemas.slice(0, limit).map((x) => ({ specId: x.spec.id, name: x.name })),
  }
}

function printTable(rows, { sep = '  ' } = {}) {
  if (!rows.length) return
  const widths = []
  for (const row of rows) {
    row.forEach((cell, i) => {
      widths[i] = Math.max(widths[i] || 0, String(cell).length)
    })
  }
  for (const row of rows) {
    const line = row
      .map((cell, i) => String(cell).padEnd(widths[i], ' '))
      .join(sep)
      .trimEnd()
    console.log(line)
  }
}

function printSpecs(specs, { json } = {}) {
  if (json) {
    console.log(JSON.stringify(specs.map(toShortSpec), null, 2))
    return
  }

  const rows = [['id', 'version', 'operations', 'schemas', 'file']]
  for (const s of specs) rows.push([s.id, s.version, String(s.operations.length), String(Object.keys(s.schemas).length), s.filePath])
  printTable(rows)
}

function printTags(specs, { specHint } = {}) {
  const rows = [['spec', 'tag', 'description']]
  for (const s of specs) {
    if (specHint && s.id !== specHint) continue
    for (const t of s.tags || []) rows.push([s.id, t.name, (t.description || '').replaceAll('\n', ' ').slice(0, 80)])
  }
  if (rows.length === 1) die('No tags found')
  printTable(rows)
}

function printOps(specs, { specHint, tag, q, json, limit = 30 } = {}) {
  let ops = []
  for (const s of specs) {
    if (specHint && s.id !== specHint) continue
    ops.push(...s.operations)
  }

  if (tag) ops = ops.filter((o) => (o.tags || []).includes(tag))

  if (q) {
    const res = search(specs, q, { specHint, limit: Math.max(limit, 200) })
    const opSet = new Set(res.ops.map((o) => `${o.specId}:${o.operationId || o.method + ' ' + o.path}`))
    ops = ops.filter((o) => opSet.has(`${o.specId}:${o.operationId || o.method + ' ' + o.path}`))
  }

  ops = ops.slice(0, limit)

  if (json) {
    console.log(
      JSON.stringify(
        ops.map((o) => ({
          spec: o.specId,
          operationId: o.operationId,
          method: o.method,
          path: o.path,
          summary: o.summary,
        })),
        null,
        2,
      ),
    )
    return
  }

  const rows = [['spec', 'operationId', 'method', 'path', 'summary']]
  for (const o of ops) rows.push([o.specId, o.operationId || '-', o.method.toUpperCase(), o.path, (o.summary || '').slice(0, 80)])
  printTable(rows)
}

function splitParams(params) {
  const out = { path: [], query: [], header: [], cookie: [], other: [] }
  for (const p of params || []) {
    const loc = p?.in
    if (loc === 'path') out.path.push(p)
    else if (loc === 'query') out.query.push(p)
    else if (loc === 'header') out.header.push(p)
    else if (loc === 'cookie') out.cookie.push(p)
    else out.other.push(p)
  }
  return out
}

function paramType(param) {
  const s = param?.schema
  if (s) return schemaTypeString(s)
  if (param?.content) {
    const media = Object.values(param.content)[0]
    if (media?.schema) return schemaTypeString(media.schema)
  }
  return 'any'
}

function printParamsBlock(title, params) {
  if (!params.length) return
  console.log(`\n${title}`)
  const rows = [['name', 'in', 'required', 'type', 'description']]
  for (const p of params) {
    rows.push([
      p.name || '-',
      p.in || '-',
      p.required ? 'yes' : 'no',
      paramType(p),
      (p.description || '').replaceAll('\n', ' ').slice(0, 80),
    ])
  }
  printTable(rows)
}

function printOperation(op, spec) {
  const baseUrl = spec.servers?.[0] || ''
  const full = baseUrl ? `${baseUrl}${op.path}` : op.path

  const id = op.operationId ? `${op.specId}:${op.operationId}` : `${op.specId}:${op.method.toUpperCase()} ${op.path}`

  console.log(id)
  console.log(`${op.method.toUpperCase()} ${full}`)

  if (op.summary) console.log(`\n${op.summary}`)
  if (op.deprecated) console.log(`\nDeprecated: yes`)

  const auth = op.securityLabel
  if (auth) console.log(`\nAuth: ${auth}`)

  if (op.tags?.length) console.log(`Tags: ${op.tags.join(', ')}`)

  if (op.description) {
    const desc = String(op.description).trim().replace(/\n{3,}/g, '\n\n')
    const short = desc.length > 800 ? `${desc.slice(0, 800)}\n...` : desc
    console.log(`\n${short}`)
  }

  const params = splitParams(op.parameters || [])
  printParamsBlock('Path params', params.path)
  printParamsBlock('Query params', params.query)
  printParamsBlock('Header params', params.header)

  if (op.requestBody?.content) {
    console.log('\nBody')
    const required = op.requestBody.required ? 'required' : 'optional'
    console.log(`required: ${required}`)

    const contentTypes = Object.keys(op.requestBody.content)
    for (const ct of contentTypes) {
      const schema = op.requestBody.content?.[ct]?.schema
      if (!schema) continue
      console.log(`\n${ct}`)
      const lines = formatSchemaPreview(schema, spec.doc, { depth: 3, maxProps: 12 })
      for (const l of lines) console.log(l)

      if (ct === 'application/json') {
        const ex = exampleFromSchema(schema, spec.doc, { depth: 3, includeOptional: false })
        if (ex && typeof ex === 'object') {
          console.log('\nexample (required fields)')
          console.log(JSON.stringify(ex, null, 2))
        }
      }
    }
  }

  if (op.responses && Object.keys(op.responses).length) {
    console.log('\nResponses')
    const codes = Object.keys(op.responses).sort((a, b) => {
      const na = Number(a)
      const nb = Number(b)
      if (Number.isFinite(na) && Number.isFinite(nb)) return na - nb
      if (a === 'default') return 1
      if (b === 'default') return -1
      return a.localeCompare(b)
    })

    for (const code of codes) {
      const resp = derefObject(op.responses[code], spec.doc)
      const desc = resp?.description ? ` - ${String(resp.description).replaceAll('\n', ' ').slice(0, 80)}` : ''
      console.log(`\n${code}${desc}`)

      const content = resp?.content || {}
      for (const [ct, media] of Object.entries(content)) {
        if (!media?.schema) continue
        console.log(`${ct}`)
        const lines = formatSchemaPreview(media.schema, spec.doc, { depth: 3, maxProps: 12 })
        for (const l of lines) console.log(l)
      }
    }
  }

  console.log('\ncurl')
  console.log(formatCurl(op, spec))
}

function replacePathParams(p) {
  return p.replaceAll(/\{([^}]+)\}/g, '<$1>')
}

function formatCurl(op, spec) {
  const baseUrl = spec.servers?.[0] || ''
  let url = baseUrl ? `${baseUrl}${replacePathParams(op.path)}` : replacePathParams(op.path)

  const requiredQuery = (op.parameters || [])
    .filter((p) => p?.in === 'query' && p?.required && p?.name)
    .map((p) => `${encodeURIComponent(p.name)}=<${p.name}>`)
  if (requiredQuery.length) url += `?${requiredQuery.join('&')}`

  const lines = []
  lines.push(`curl -X ${op.method.toUpperCase()} '${url}' \\`)

  // auth header if we can infer it
  const schemes = spec?.doc?.components?.securitySchemes || {}
  const sec = Array.isArray(op.security) ? op.security : null
  const candidates = (sec || []).filter((x) => x && typeof x === 'object')
  const preferred =
    candidates.find((req) =>
      Object.keys(req).some((name) => schemes[name]?.type === 'apiKey' && schemes[name]?.in === 'header'),
    ) || candidates[0]

  for (const name of Object.keys(preferred || {})) {
    const s = schemes[name]
    if (s?.type === 'apiKey' && s.in === 'header' && s.name) {
      lines.push(`  -H '${s.name}: $KAPSO_API_KEY' \\`)
    } else if (s?.type === 'http' && s.scheme === 'bearer') {
      lines.push(`  -H 'Authorization: Bearer $ACCESS_TOKEN' \\`)
    }
  }

  // content-type + body for JSON
  const jsonSchema = op.requestBody?.content?.['application/json']?.schema
  if (jsonSchema) {
    const ex = exampleFromSchema(jsonSchema, spec.doc, { depth: 4, includeOptional: false })
    lines.push(`  -H 'Content-Type: application/json' \\`)
    lines.push(`  -d '${JSON.stringify(ex ?? {}, null, 0)}'`)
    return lines.join('\n')
  }

  // trim trailing backslash
  lines[lines.length - 1] = lines[lines.length - 1].replace(/ \\\\$/, '')
  return lines.join('\n')
}

function printSchemaDetails(match, specs, { includeUsedBy = true } = {}) {
  const { spec, name, schema } = match
  console.log(`${spec.id}:${name}`)

  const normalized = schema?.allOf ? mergeAllOf(schema, spec.doc) : schema
  const typeStr = schemaTypeString(normalized)
  console.log(typeStr)

  if (normalized?.description) console.log(`\n${String(normalized.description).trim()}`)

  const required = normalized?.required || []
  if (required.length) console.log(`\nrequired: ${required.join(', ')}`)

  if (normalized?.properties || normalized?.items) {
    console.log('\nshape')
    const lines = formatSchemaPreview(normalized, spec.doc, { depth: 3, maxProps: 25 })
    for (const l of lines) console.log(l)
  }

  const ex = exampleFromSchema(normalized, spec.doc, { depth: 4, includeOptional: false })
  if (ex && typeof ex === 'object') {
    console.log('\nexample (required fields)')
    console.log(JSON.stringify(ex, null, 2))
  }

  if (includeUsedBy) {
    const usedBy = []
    for (const s of specs) {
      for (const op of s.operations) {
        if (op.refsUsed?.has(name)) usedBy.push(op)
      }
    }

    if (usedBy.length) {
      console.log('\nused by')
      const rows = [['spec', 'operationId', 'method', 'path']]
      for (const op of usedBy.slice(0, 30)) rows.push([op.specId, op.operationId || '-', op.method.toUpperCase(), op.path])
      printTable(rows)
      if (usedBy.length > 30) console.log(`... (${usedBy.length - 30} more)`)
    }
  }
}

function printWhere(specs, schemaQuery, { specHint, json, limit = 30 } = {}) {
  const matches = findSchema(specs, schemaQuery, { specHint })
  if (!matches.length) die(`Schema not found: ${schemaQuery}`)
  if (matches.length > 1 && !schemaQuery.includes(':')) {
    die(`Schema exists in multiple specs. Use specId:SchemaName\n${matches.map((m) => `- ${m.spec.id}:${m.name}`).join('\n')}`)
  }

  const { name } = matches[0]
  const usedBy = []
  for (const s of specs) {
    if (specHint && s.id !== specHint) continue
    for (const op of s.operations) {
      if (op.refsUsed?.has(name)) usedBy.push(op)
    }
  }

  if (json) {
    console.log(
      JSON.stringify(
        usedBy.slice(0, limit).map((o) => ({
          spec: o.specId,
          operationId: o.operationId,
          method: o.method,
          path: o.path,
          summary: o.summary,
        })),
        null,
        2,
      ),
    )
    return
  }

  if (!usedBy.length) {
    console.log('No operations reference this schema (via $ref).')
    return
  }

  const rows = [['spec', 'operationId', 'method', 'path', 'summary']]
  for (const o of usedBy.slice(0, limit)) rows.push([o.specId, o.operationId || '-', o.method.toUpperCase(), o.path, (o.summary || '').slice(0, 80)])
  printTable(rows)
  if (usedBy.length > limit) console.log(`... (${usedBy.length - limit} more)`)
}

async function main() {
  const { opts, command, rest } = parseArgs(process.argv.slice(2))
  if (!command) printHelp(1)

  let sources = []
  let sourceMode = 'explicit'

  if (opts.files.length) {
    sources = opts.files
    sourceMode = 'explicit'
  } else if (opts.all) {
    const apiDir = findLocalApiDir()
    sources = apiDir ? walk(apiDir, { filePattern: /^openapi-.*\.ya?ml$/ }) : []
    sourceMode = 'explicit'
  } else {
    sources = deducePublishedOpenApiUrls(DEFAULT_PUBLISHED_WHATSAPP_OPENAPI)
    sourceMode = 'default_remote'
  }

  const specs = await loadSpecsAsync({ sources, sourceMode, specFilter: opts.spec })

  if (command === 'specs') return printSpecs(specs, { json: opts.json })
  if (command === 'tags') return printTags(specs, { specHint: opts.spec })
  if (command === 'ops') return printOps(specs, { specHint: opts.spec, tag: opts.tag, q: opts.q, json: opts.json, limit: opts.limit })
  if (command === 'search') {
    const q = rest.join(' ').trim()
    if (!q) die('Usage: search <query>')
    const res = search(specs, q, { specHint: opts.spec, limit: opts.limit })
    if (opts.json) {
      return console.log(
        JSON.stringify(
          {
            ops: res.ops.map((o) => ({
              spec: o.specId,
              operationId: o.operationId,
              method: o.method,
              path: o.path,
              summary: o.summary,
            })),
            schemas: res.schemas,
          },
          null,
          2,
        ),
      )
    }

    if (!res.ops.length && !res.schemas.length) {
      console.log('No matches.')
      return
    }

    if (res.ops.length) {
      console.log('ops')
      const rows = [['spec', 'operationId', 'method', 'path', 'summary']]
      for (const o of res.ops) rows.push([o.specId, o.operationId || '-', o.method.toUpperCase(), o.path, (o.summary || '').slice(0, 80)])
      printTable(rows)
    }
    if (res.schemas.length) {
      console.log('\nschemas')
      const rows = [['spec', 'name']]
      for (const s of res.schemas) rows.push([s.specId, s.name])
      printTable(rows)
    }
    return
  }
  if (command === 'op') {
    const q = rest.join(' ').trim()
    if (!q) die('Usage: op <operationId | specId:operationId | "METHOD /path">')
    const matches = findOperation(specs, q, { specHint: opts.spec })
    if (!matches.length) {
      const res = search(specs, q, { specHint: opts.spec, limit: 10 })
      if (res.ops.length) {
        console.log(`Operation not found: ${q}\n`)
        console.log('closest ops')
        const rows = [['spec', 'operationId', 'method', 'path', 'summary']]
        for (const o of res.ops) rows.push([o.specId, o.operationId || '-', o.method.toUpperCase(), o.path, (o.summary || '').slice(0, 80)])
        printTable(rows)
        process.exit(1)
      }
      die(`Operation not found: ${q}`)
    }
    if (matches.length > 1 && !q.includes(':') && !q.match(/^(get|post|put|patch|delete|options|head)\\s+/i)) {
      die(`OperationId exists in multiple specs. Use specId:operationId\n${matches.map((m) => `- ${m.specId}:${m.operationId}`).join('\n')}`)
    }
    const op = matches[0]
    const spec = specs.find((s) => s.id === op.specId)
    if (!spec) die(`Internal error: missing spec ${op.specId}`)
    printOperation(op, spec)
    return
  }
  if (command === 'schema') {
    const q = rest.join(' ').trim()
    if (!q) die('Usage: schema <SchemaName | specId:SchemaName>')
    const matches = findSchema(specs, q, { specHint: opts.spec })
    if (!matches.length) {
      const res = search(specs, q, { specHint: opts.spec, limit: 10 })
      if (res.schemas.length) {
        console.log(`Schema not found: ${q}\n`)
        console.log('closest schemas')
        const rows = [['spec', 'name']]
        for (const s of res.schemas) rows.push([s.specId, s.name])
        printTable(rows)
        process.exit(1)
      }
      die(`Schema not found: ${q}`)
    }
    if (matches.length > 1 && !q.includes(':')) {
      die(`Schema exists in multiple specs. Use specId:SchemaName\n${matches.map((m) => `- ${m.spec.id}:${m.name}`).join('\n')}`)
    }
    printSchemaDetails(matches[0], specs, { includeUsedBy: true })
    return
  }
  if (command === 'where') {
    const q = rest.join(' ').trim()
    if (!q) die('Usage: where <SchemaName | specId:SchemaName>')
    return printWhere(specs, q, { specHint: opts.spec, json: opts.json, limit: opts.limit })
  }

  die(`Unknown command: ${command}`)
}

main().catch((e) => die(e?.stack || e?.message || String(e)))
```

## File: `skills/observe-whatsapp/scripts/overview.js`
```javascript
const { hasHelpFlag, parseFlags } = require('./lib/status/args');
const { kapsoConfigFromEnv, kapsoRequest } = require('./lib/status/kapso-api');

function err(message, details) {
  return { ok: false, error: { message, details } };
}

async function main() {
  const argv = process.argv.slice(2);
  if (hasHelpFlag(argv)) {
    console.log(
      JSON.stringify(
        {
          ok: true,
          usage:
            'node scripts/overview.js [--period <24h|7d|30d>] [--per-page <n>]',
          env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
        },
        null,
        2
      )
    );
    return 0;
  }

  try {
    const flags = parseFlags(argv);
    const period = flags.period || '24h';
    const perPage = parseNumber(flags['per-page'], 50, 'per-page');
    const config = kapsoConfigFromEnv();

    const phoneNumbers = await kapsoRequest(
      config,
      `/platform/v1/whatsapp/phone_numbers?per_page=${perPage}`
    );

    const apiTotals = await kapsoRequest(
      config,
      `/platform/v1/api_logs?period=${encodeURIComponent(period)}&per_page=1`
    );
    const apiErrors = await kapsoRequest(
      config,
      `/platform/v1/api_logs?period=${encodeURIComponent(period)}&errors_only=true&per_page=1`
    );

    const webhookTotals = await kapsoRequest(
      config,
      `/platform/v1/webhook_deliveries?period=${encodeURIComponent(period)}&per_page=1`
    );
    const webhookErrors = await kapsoRequest(
      config,
      `/platform/v1/webhook_deliveries?period=${encodeURIComponent(period)}&errors_only=true&per_page=1`
    );

    const payload = {
      ok: true,
      period,
      phone_numbers: phoneNumbers.data || [],
      api_calls: {
        total: extractCount(apiTotals),
        failed: extractCount(apiErrors)
      },
      webhook_deliveries: {
        total: extractCount(webhookTotals),
        failed: extractCount(webhookErrors)
      },
      notes: [
        'Plan and subscription details are not exposed via the Platform API.',
        'Use whatsapp-health.js per phone number for detailed WhatsApp checks.'
      ]
    };

    console.log(JSON.stringify(payload, null, 2));
    return 0;
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    console.error(JSON.stringify(err('Command failed', { message }), null, 2));
    return 1;
  }
}

function parseNumber(value, fallback, name) {
  if (value === undefined || value === true) return fallback;
  const parsed = Number(value);
  if (!Number.isFinite(parsed) || parsed <= 0) {
    throw new Error(`Invalid --${name} value: ${value}`);
  }
  return parsed;
}

function extractCount(response) {
  if (!response || typeof response !== 'object') return null;
  return response.meta && typeof response.meta.total_count === 'number'
    ? response.meta.total_count
    : null;
}

main().then((code) => process.exit(code));
```

## File: `skills/observe-whatsapp/scripts/webhook-deliveries.js`
```javascript
const { hasHelpFlag, parseFlags } = require('./lib/triage/args');
const { kapsoConfigFromEnv, kapsoRequest } = require('./lib/triage/kapso-api');

function err(message, details) {
  return { ok: false, error: { message, details } };
}

async function main() {
  const argv = process.argv.slice(2);
  if (hasHelpFlag(argv)) {
    console.log(
      JSON.stringify(
        {
          ok: true,
          usage:
            'node scripts/webhook-deliveries.js [--period <24h|7d|30d>] [--status <value>] [--event <value>] [--webhook-id <id>] [--errors-only true|false] [--page <n>] [--per-page <n>]',
          env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
        },
        null,
        2
      )
    );
    return 0;
  }

  try {
    const flags = parseFlags(argv);
    const params = new URLSearchParams();

    if (flags.period) params.set('period', flags.period);
    if (flags.status) params.set('status', flags.status);
    if (flags.event) params.set('event', flags.event);
    if (flags['webhook-id']) params.set('webhook_id', flags['webhook-id']);
    if (flags['errors-only'] !== undefined) params.set('errors_only', flags['errors-only']);
    if (flags.page) params.set('page', flags.page);
    if (flags['per-page']) params.set('per_page', flags['per-page']);

    const suffix = params.toString();
    const config = kapsoConfigFromEnv();
    const data = await kapsoRequest(
      config,
      `/platform/v1/webhook_deliveries${suffix ? `?${suffix}` : ''}`
    );

    console.log(JSON.stringify({ ok: true, data }, null, 2));
    return 0;
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    console.error(JSON.stringify(err('Command failed', { message }), null, 2));
    return 1;
  }
}

main().then((code) => process.exit(code));
```

## File: `skills/observe-whatsapp/scripts/whatsapp-health.js`
```javascript
const { kapsoConfigFromEnv, kapsoRequest } = require('./lib/status/kapso-api');
const { hasHelpFlag, parseFlags, requireFlag } = require('./lib/status/args');

function ok(data) {
  return { ok: true, data };
}

function err(message, details) {
  return { ok: false, error: { message, details } };
}

async function main() {
  const argv = process.argv.slice(2);
  if (hasHelpFlag(argv)) {
    console.log(
      JSON.stringify(
        {
          ok: true,
          usage:
            'node scripts/whatsapp-health.js --phone-number-id <id>',
          env: ['KAPSO_API_BASE_URL', 'KAPSO_API_KEY']
        },
        null,
        2
      )
    );
    return 0;
  }

  try {
    const flags = parseFlags(argv);
    const phoneNumberId = requireFlag(flags, 'phone-number-id');
    const config = kapsoConfigFromEnv();
    const data = await kapsoRequest(
      config,
      `/platform/v1/whatsapp/phone_numbers/${encodeURIComponent(phoneNumberId)}/health`
    );

    console.log(JSON.stringify(ok(data), null, 2));
    return 0;
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    console.error(JSON.stringify(err('Command failed', { message }), null, 2));
    return 1;
  }
}

main().then((code) => process.exit(code));
```

## File: `skills/observe-whatsapp/scripts/lib/messages/args.js`
```javascript
function hasHelpFlag(argv) {
  return argv.includes('--help') || argv.includes('-h');
}

function parseFlags(argv) {
  const flags = {};
  for (let index = 0; index < argv.length; index += 1) {
    const arg = argv[index];
    if (!arg.startsWith('--')) {
      continue;
    }
    const trimmed = arg.slice(2);
    const eqIndex = trimmed.indexOf('=');
    if (eqIndex >= 0) {
      const key = trimmed.slice(0, eqIndex);
      const value = trimmed.slice(eqIndex + 1);
      flags[key] = value;
      continue;
    }
    const next = argv[index + 1];
    if (!next || next.startsWith('--')) {
      flags[trimmed] = true;
      continue;
    }
    flags[trimmed] = next;
    index += 1;
  }
  return flags;
}

module.exports = {
  hasHelpFlag,
  parseFlags
};
```

## File: `skills/observe-whatsapp/scripts/lib/messages/kapso-api.js`
```javascript
function requireEnv(name) {
  const value = process.env[name];
  if (!value) {
    throw new Error(`Missing required env var: ${name}`);
  }
  return value;
}

function normalizeBaseUrl(raw) {
  return raw.replace(/\/+$/, '');
}

function kapsoConfigFromEnv() {
  return {
    baseUrl: normalizeBaseUrl(requireEnv('KAPSO_API_BASE_URL')),
    apiKey: requireEnv('KAPSO_API_KEY')
  };
}

async function kapsoRequest(config, path, init = {}) {
  const url = `${config.baseUrl}${path}`;
  const headers = new Headers(init.headers || undefined);
  headers.set('X-API-Key', config.apiKey);
  if (!headers.has('Content-Type')) {
    headers.set('Content-Type', 'application/json');
  }

  const response = await fetch(url, { ...init, headers });
  const text = await response.text();

  if (!response.ok) {
    throw new Error(`Kapso API request failed (status=${response.status}) body=${text}`);
  }

  return text ? JSON.parse(text) : {};
}

module.exports = {
  kapsoConfigFromEnv,
  kapsoRequest
};
```

## File: `skills/observe-whatsapp/scripts/lib/status/args.js`
```javascript
function hasHelpFlag(argv) {
  return argv.includes('--help') || argv.includes('-h');
}

function parseFlags(argv) {
  const flags = {};
  for (let index = 0; index < argv.length; index += 1) {
    const arg = argv[index];
    if (!arg.startsWith('--')) {
      continue;
    }
    const trimmed = arg.slice(2);
    const eqIndex = trimmed.indexOf('=');
    if (eqIndex >= 0) {
      const key = trimmed.slice(0, eqIndex);
      const value = trimmed.slice(eqIndex + 1);
      flags[key] = value;
      continue;
    }
    const next = argv[index + 1];
    if (!next || next.startsWith('--')) {
      flags[trimmed] = true;
      continue;
    }
    flags[trimmed] = next;
    index += 1;
  }
  return flags;
}

function requireFlag(flags, name) {
  const value = flags[name];
  if (typeof value !== 'string' || value.length === 0) {
    throw new Error(`Missing required flag --${name}`);
  }
  return value;
}

module.exports = {
  hasHelpFlag,
  parseFlags,
  requireFlag
};
```

## File: `skills/observe-whatsapp/scripts/lib/status/kapso-api.js`
```javascript
function requireEnv(name) {
  const value = process.env[name];
  if (!value) {
    throw new Error(`Missing required env var: ${name}`);
  }
  return value;
}

function normalizeBaseUrl(raw) {
  return raw.replace(/\/+$/, '');
}

function kapsoConfigFromEnv() {
  return {
    baseUrl: normalizeBaseUrl(requireEnv('KAPSO_API_BASE_URL')),
    apiKey: requireEnv('KAPSO_API_KEY')
  };
}

async function kapsoRequest(config, path, init = {}) {
  const url = `${config.baseUrl}${path}`;
  if (process.env.KAPSO_DEBUG_URLS === 'true') {
    console.error(`[kapso-debug] ${init.method || 'GET'} ${url}`);
  }
  const headers = new Headers(init.headers || undefined);
  headers.set('X-API-Key', config.apiKey);
  if (!headers.has('Content-Type')) {
    headers.set('Content-Type', 'application/json');
  }

  const response = await fetch(url, { ...init, headers });
  const text = await response.text();

  if (!response.ok) {
    throw new Error(`Kapso API request failed (status=${response.status}) body=${text}`);
  }

  return text ? JSON.parse(text) : {};
}

module.exports = {
  kapsoConfigFromEnv,
  kapsoRequest
};
```

## File: `skills/observe-whatsapp/scripts/lib/triage/args.js`
```javascript
function hasHelpFlag(argv) {
  return argv.includes('--help') || argv.includes('-h');
}

function parseFlags(argv) {
  const flags = {};
  for (let index = 0; index < argv.length; index += 1) {
    const arg = argv[index];
    if (!arg.startsWith('--')) {
      continue;
    }
    const trimmed = arg.slice(2);
    const eqIndex = trimmed.indexOf('=');
    if (eqIndex >= 0) {
      const key = trimmed.slice(0, eqIndex);
      const value = trimmed.slice(eqIndex + 1);
      flags[key] = value;
      continue;
    }
    const next = argv[index + 1];
    if (!next || next.startsWith('--')) {
      flags[trimmed] = true;
      continue;
    }
    flags[trimmed] = next;
    index += 1;
  }
  return flags;
}

module.exports = {
  hasHelpFlag,
  parseFlags
};
```

## File: `skills/observe-whatsapp/scripts/lib/triage/kapso-api.js`
```javascript
function requireEnv(name) {
  const value = process.env[name];
  if (!value) {
    throw new Error(`Missing required env var: ${name}`);
  }
  return value;
}

function normalizeBaseUrl(raw) {
  return raw.replace(/\/+$/, '');
}

function kapsoConfigFromEnv() {
  return {
    baseUrl: normalizeBaseUrl(requireEnv('KAPSO_API_BASE_URL')),
    apiKey: requireEnv('KAPSO_API_KEY')
  };
}

async function kapsoRequest(config, path, init = {}) {
  const url = `${config.baseUrl}${path}`;
  const headers = new Headers(init.headers || undefined);
  headers.set('X-API-Key', config.apiKey);
  if (!headers.has('Content-Type')) {
    headers.set('Content-Type', 'application/json');
  }

  const response = await fetch(url, { ...init, headers });
  const text = await response.text();

  if (!response.ok) {
    throw new Error(`Kapso API request failed (status=${response.status}) body=${text}`);
  }

  return text ? JSON.parse(text) : {};
}

module.exports = {
  kapsoConfigFromEnv,
  kapsoRequest
};
```

