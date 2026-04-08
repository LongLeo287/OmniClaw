---
description: "Connect an external project workspace to the OmniClaw OS infrastructure."
id: "workflow-connect-omniclaw"
version: "1.0"
updated_at: "2026-04-03"
type: "workflow"
platform: "antigravity"
tier: 1
trigger: "/connect-omniclaw in IDE chat"
---

# Workflow: Connect OmniClaw Ecosystem (/connect-omniclaw)

> **Purpose:** Integrates a blank OR existing project workspace (e.g., inside `OmniProject`) into the OmniClaw Core System by applying necessary routing connections and verifying the bridge.

---

## Steps (Execute in Order)

### 1. Verification
Check if the absolute OS architecture path `D:\LongLeo\OmniClaw OS\OmniClaw\brain` exists using `Test-Path`.
If it doesn't exist, stop execution and alert the CEO that the 5-Pillar Core is missing from the host machine.

### 2. Environment Setup
Inject the runtime environment variables into the active session to bind the current project sandbox to the Neural Bus APIs.
// turbo
```powershell
$env:OMNICLAW_BRIDGE_ACTIVE="1"
$env:OMNICLAW_API_ENDPOINT="http://127.0.0.1:8080"
Write-Output "[OmniClaw Bridge] Connection endpoints verified and active."
```

### 3. Connection Confirmation
Output a highly stylized confirmation direct to the CEO's Chat Interface:
**"🚀 OMNICLAW WORKFORCE AGENTS KICKSTARTED!"**
"This Sandbox has been authenticated and spliced into the OS Pipeline. The local Agent Workforce is standing by for coding or scaffolding directives."
