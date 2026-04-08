---
description: "Start the Core Daemons HUD and diagnostic background systems."
id: "workflow-start-core"
version: "1.0"
updated_at: "2026-04-03"
type: "workflow"
platform: "antigravity"
tier: 1
trigger: "/start-core in IDE chat"
---

# Workflow: Start OmniClaw Core Daemons (/start-core)

> **Purpose:** Initiate the OmniClaw master pipeline (OHD, OIW, OA) and output the Core Diagnostics HUD natively to the CEO's terminal. 
> Replaces legacy `.bat` execution with native Agent execution.

---

## Steps (Execute in Order)

### 1. Workspace Validation
Verify that the `core\ops\scripts\omniclaw_start.py` file exists in the current working directory hierarchy. If not, inform the CEO that they are in the wrong workspace.

### 2. Launch Stealth Daemons & Diagnostic HUD
Execute the Python Daemon Manager payload natively using the terminal, pushing all engines to the background safely. Then trigger the visual HUD.
// turbo-all
```powershell
python "core\ops\scripts\daemon_manager.py" start
python "core\ops\scripts\omniclaw_start.py"
```

### 3. Chat Output Delivery
Display the output metrics back to the CEO. Highlight the critical components:
- System Environment (Python/Git config)
- Knowledge Pulse (Selected / Pending arrays)
- Neural Bus MQ (Pending tasks)
- Core Daemons Availability

State explicitly: "Core Daemons have been successfully awakened."
