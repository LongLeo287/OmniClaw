---
description: "Terminate all running background Core Daemons to clean up system memory and ensure safe shutdown."
id: "workflow-stop-core"
version: "1.0"
updated_at: "2026-04-03"
type: "workflow"
platform: "antigravity"
tier: 1
trigger: "/stop-core in IDE chat"
---

# Workflow: Stop OmniClaw Core Daemons (/stop-core)

> **Purpose:** Execute Order 66. Safely shut down all executing background daemons by tracing their PIDs defined in `daemon_manager.py` to prevent memory leaks and duplicate pipelines.

---

## Steps (Execute in Order)

### 1. Execute Stealth Teardown (Order 66)
Run the python Daemon Manager with the `stop` argument. We must natively invoke this through the Powershell CLI.
// turbo
```powershell
python "core\ops\scripts\daemon_manager.py" stop
```

### 2. Status Delivery
Inform the CEO in the chat natively that the operations have ceased safely.
**"🔴 OMNICLAW CORE STANDBY MODE ACTIVATED."**
"All active Core Daemons (OIW, OMA, OA, etc.) have been pulled from memory and neutralized cleanly using exact PID tracing."
