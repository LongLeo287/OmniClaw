---
id: plugin-integration
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:00.674103
---

# Department: operations
---
description: Plugin Integration Process — OmniClaw Corp
---

# Plugin Integration Workflow
# Version: 1.0 | 2026-03-23 | Owner: Antigravity (Dept 4 — Registry)

Mandatory process when integrating any new repo/plugin/tool into OmniClaw Corp.
Trigger: `omniclaw integrate <plugin_id>` or when CEO requests.

> ⚠️ **PRE-GATE:** This workflow runs ONLY AFTER `ops/workflows/repo-evaluation.md` gives **APPROVE** verdict.
> If repo-evaluation not run → STOP, return to evaluation step.

---

## PHASE 0 — Catalog & Conflict Check

### 0.1 — Mark repo in plugin-catalog.md

Open `plugins/plugin-catalog.md` and update Status:

| Symbol | Meaning |
|---------|---------|
| `👁️` | Read/surveyed README |
| `🔖` | Retained, may use later |
| `✅` | In use (track version) |
| `⚡` | In integration process |
| `❌` | Removed (duplicate features / not suitable) |

**Rule:** Every repo in `plugins/` must have a Status in catalog before reading code.

### 0.2 — Conflict check

Check if new features overlap with existing plugins:

```
1. List core features of new plugin
2. Compare with plugins/registry.json (status: active)
3. Compare with blackboard.json infrastructure section
4. If overlap: evaluate "supplement" vs "replace"
   - Supplement → OK, clearly state differentiating use case
   - Replace → must deprecate old plugin first
```

### 0.3 — Update catalog: ⚡ (in progress)

---

## PHASE 1 — Security Scan (RULE-PROCESS-01 Mandatory)

**Owner: Dept 10 — Security/GRC (Strix)**

```bash
# Run nemoclaw-strix-scan on repo
# See: ops/workflows/nemoclaw-strix-scan.md
```

Minimum check:
- [ ] License compatible (MIT/Apache/BSD preferred; AGPL flag for CEO review)
- [ ] No hardcoded credentials, API keys
- [ ] No cryptominer, obfuscated code
- [ ] Source repo is public/verified
- [ ] `pip show <package>` or `npm info <package>` — verify publisher

Result: **CLEAR** or **FLAG** (CEO decides if FLAG)

---

## PHASE 2 — Create Plugin Structure (PLUGIN_SPEC.md)

```
plugins/<plugin_id>/
├── manifest.json     [REQUIRED]
├── PLUGIN.md         [REQUIRED] — agent guidance
├── README.md         [REQUIRED] — overview
├── <adapter>.py      [if wrapper needed]
└── tests/            [REQUIRED]
    └── test_<id>.py  — smoke tests
```

### manifest.json checklist
- [ ] `id`, `name`, `version`, `type`, `status` filled completely
- [ ] `agent_hooks` declares hooks used correctly
- [ ] `auto_load: false` (default — do not auto-load on boot)
- [ ] `can_crash_os: false` — mandatory
- [ ] `conflict_check` section: record Phase 0 result
- [ ] `upstream_check`: frequency to check for new versions

---

## PHASE 3 — Version Tracking Setup

Add to **Version Tracking table** in `plugin-catalog.md`:

```markdown
| <plugin_id> | <current_version> | <frequency> | <update_command> |
```

**Frequency by importance:**
- Core agent tools → Weekly
- Data/bridge tools → Monthly
- Security tools → Weekly
- Reference/UI → Quarterly

---

## PHASE 4 — Register Registry

Update `plugins/registry.json`:

```json
{
  "id": "<plugin_id>",
  "type": "<cognitive|data|bridge|ui>",
  "status": "active",
  "auto_load": false,
  "path": "plugins/<plugin_id>/",
  "manifest": "plugins/<plugin_id>/manifest.json",
  "notes": "<Short description, integration date>",
  "registered_at": "YYYY-MM-DD",
  "upstream_check": "<frequency> — <command>"
}
```

Update `total_registered` and `active_count`.

---

## PHASE 5 — Activation Commands (RULE-ACTIVATION-01)

**If plugin requires cmd/powershell to activate:**

### 5a — Add to Dashboard (dashboard.ps1)

Open `$OMNICLAW_ROOT\launcher\dashboard.ps1` and add to **PLUGIN MANAGER** section:

```powershell
# In menu [P] Plugin Manager → sub-menu
"<plugin_id>" = @{
    Name = "<Display Name>"
    Check = { <check if installed/running> }
    Install = "<install command>"
    Start = "<start command, if any>"
    Port = <port if service, $null if not>
}
```

### 5b — Add to ClawTask (Port 7474)

If plugin is a **service with a port** → add to `$SERVICES` in `dashboard.ps1`.

If plugin is a **library/tool** (no port) → only add to Plugin Manager section.

### 5c — Update MASTER.env (if API key needed)

```
$OMNICLAW_ROOT\ops\secrets\MASTER.env
```

---

## PHASE 6 — Test & Verify

```bash
# 1. Run smoke tests
python plugins/<plugin_id>/tests/test_<id>.py

# 2. Verify registry
python -c "import json; r=json.load(open('plugins/registry.json')); print([p for p in r['plugins'] if p['id']=='<id>'])"

# 3. Test activation from dashboard (if applicable)
# Open OmniClaw Corp.cmd → [P] Plugin Manager → select plugin
```

---

## PHASE 7 — Update Blackboard & Catalog

```
1. blackboard.json: update open_items if this is an OPEN task
2. plugin-catalog.md: status ⚡ → ✅, add version tracking
3. telemetry/receipts/<plugin_id>/: log first activation
```

---

## PHASE 7b — Register Rules, Skills & Workflow Hooks (MANDATORY)

> This step is often overlooked. Must be done IMMEDIATELY after Phase 7.

### 7b.1 — Add RULE to GEMINI.md

If plugin changes how agents work, MUST add clear rule:

```
Open: $OMNICLAW_ROOT\GEMINI.md
Add to SECTION 3 — ANTIGRAVITY SPECIFIC RULES:

**[RULE-<XYZ>-01]** <Rule name>:
  1. When to use this plugin
  2. How to call (import, function)
  3. Scope: which department / agent

Full docs: plugins/<plugin_id>/PLUGIN.md
```

### 7b.2 — Register SKILL_REGISTRY.json

```
Open: brain/shared-context/SKILL_REGISTRY.json
Add entry to "entries" array:
{
  "id": "<plugin_id>",
  "name": "<Display Name>",
  "tier": 2,
  "status": "active",
  "source": "plugin",
  "path": "plugins/<plugin_id>/SKILL.md",
  "adapter": "plugins/<plugin_id>/<adapter>.py",
  "description": "<Short description of when to use>",
  "domain": "<data|core|bridge|ui>",
  "accessible_by": ["<agent_ids>"],
  "exposed_functions": ["<function_names>"],
  "listens_to": { "<hook>": "<function_call>" },
  "rule": "<RULE-ID>",
  "noop_safe": true
}
Increment "count".
Validate: python -c "import json; json.load(open('brain/shared-context/SKILL_REGISTRY.json'))"
```

### 7b.3 — Hook into Related Workflows

Check and update workflows using this plugin:

```
- ops/workflows/knowledge-ingest.md  → step "fetch URL/search"
- ops/workflows/corp-daily-cycle.md  → if plugin runs daily
- ops/workflows/agent-workflow.md    → if agent needs plugin
```

Specifically: find steps currently using manual fallback → replace with adapter call.

---

## VERSION TRACKING — Weekly/Monthly Checks

```powershell
# Run from dashboard: [V] Version Check (newly added)
# Or run manually:
pip show mem0ai
pip show firecrawl-py
pip show crewai
# → Compare with version in plugin-catalog.md
# → If newer version: pip install --upgrade <package>
```

---

*Workflow Owner: Antigravity | Dept 4 Registry | Last updated: 2026-03-23*
*"Catalog first. Security second. Register third. Never skip."*
