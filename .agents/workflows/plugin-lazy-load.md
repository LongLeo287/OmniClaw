---
description: "Safely isolate and load Tier 2 plugins dynamically during execution."
id: workflow-plugin-lazy-load
version: "1.0"
updated_at: "2026-04-03"
type: workflow
platform: antigravity
tier: 1
trigger: "agent needs a Tier 2 plugin (sandbox lifecycle)"
---

# Workflow: Plugin Lazy-Load (Tier 2 Sandbox)

> **Rule ref:** `GEMINI.md [rule-tier-01]` — Tier 2 plugins must NEVER be installed
> into the global environment. They run in isolated sandboxes only, then teardown.

---

## When to Use

Activate this workflow when:
- An agent requires a specialized tool that is **NOT** in Tier 1 core infra
  (mem0, firecrawl, lightrag, crewai, gitnexus)
- Examples: Excel manipulation, video processing, diagram rendering, OCR, etc.
- The task is **bounded** — has a clear start and end

DO NOT activate if:
- The plugin is on the **Global Blacklist** → `brain/rules/GLOBAL_BLACKLIST.md`
- The plugin conflicts with a Tier 1 service (Tier 3 = abort immediately)

---

## Steps

### Step 0 — Pre-flight: Blacklist Check

```
1. Read brain/rules/GLOBAL_BLACKLIST.md
2. Check if requested plugin name appears under [TIER_3_BLOCKED]
   → IF FOUND: ABORT. Escalate to CEO. Do not proceed.
3. Check brain/registry/SKILL_REGISTRY.json for existing capability
   → IF EXISTS (status: active): use existing — skip sandbox spin-up
```

### Step 1 — Sandbox Init

```
sandbox_path = ecosystem/plugins/<plugin_name>/sandbox/
1. Create sandbox dir if not exists
2. Install plugin into sandbox ONLY (not global):
   pip install --target=<sandbox_path>/vendor <package>==<version>
   (version MUST be pinned — no @latest)
3. Log spin-up to brain/registry/cli_run.log:
   [SANDBOX] <plugin_name> STARTED at <timestamp>
```

### Step 2 — Execute Task

```
1. Run task inside sandbox context
2. Timeout: 120 seconds (default) — configurable via .agents/config/antigravity.yaml
3. On timeout:
   → Kill sandbox process
   → Log TIMEOUT to cli_run.log
   → Retry once (Step 2 again)
   → If retry fails → Step 4 (Teardown) + escalate to OHD
```

### Step 3 — Capture Output

```
1. Collect output artifacts from sandbox
2. Move to designated output path (as specified by calling agent)
3. Validate output exists and is non-empty
   → IF empty: log WARN, report to calling agent
```

### Step 4 — Teardown (Always Runs)

```
1. Delete sandbox/vendor/ directory
2. Remove any temp files created during execution
3. Log teardown to cli_run.log:
   [SANDBOX] <plugin_name> TEARDOWN at <timestamp> | success=<bool>
4. Update brain/registry/SKILL_REGISTRY.json:
   → usage_count++ for this plugin entry
   → last_used: <timestamp>
```

### Step 5 — On Crash

```
IF any step caused unhandled exception:
1. Write crash report to vault/tmp/quarantine/FAILED_SANDBOX_<name>_<ts>.txt:
   content = plugin_name, error, timestamp, action_required
2. OHD daemon picks up quarantine file on next cycle
3. Calling agent receives: { status: "failed", reason: <error> }
4. Do NOT retry automatically — await CEO or OHD intervention
```

---

## Security Notes

- NEVER install Tier 2 plugin into system Python / global venv
- NEVER give sandbox network access unless explicitly required and CEO approved
- All sandbox installs must use pinned versions (ref: `rule-version-01`)
- Sandbox path is gitignored — never commit vendor dirs

---

## Quick Reference

| Action | Command pattern |
|--------|----------------|
| Install to sandbox | `pip install --target=ecosystem/plugins/<name>/sandbox/vendor <pkg>==<ver>` |
| Run in sandbox | `PYTHONPATH=sandbox/vendor python -c "import <pkg>; ..."` |
| Teardown | `Remove-Item -Recurse ecosystem/plugins/<name>/sandbox/vendor` |
| Log path | `brain/registry/cli_run.log` |
| Crash path | `vault/tmp/quarantine/FAILED_SANDBOX_<name>_<ts>.txt` |
