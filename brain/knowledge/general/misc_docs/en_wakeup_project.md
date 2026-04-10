---
id: wakeup-project
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:32:45.396157
---

# Department: operations
---
description: Fetches brain data from .ai-memory/ within a project to restore into a new session.
---

# Wake Up Project

When the user gives a clear command: "Wake up project [project name]" (an independent command only for projects, Note: the system will mostly self-wakeup on startup using `pre-session`):

1.  Confirm: "I will restore brain data from .ai-memory/ in the project. Please confirm."

1.  Confirm: "I will restore brain data from .ai-memory/ in the [Name] project. Please confirm."

2.  If the user does not provide a specific project path, FIND the project name in the user's CHAT COMMAND (Example: "Wake up project Tiem_Nuoc_Nho_v5") to infer and append it to `$ProjectsRoot`.

// turbo
3.  Run the script:
    ```powershell
    & "$OMNICLAW_ROOT\scripts\wakeup.ps1" -ProjectPath "PATH_TO_PROJECT_NAME_IN_CHAT_COMMAND"
    ```

    The script will:
    -   Read `.ai-memory/` from within the project
    -   Restore brain sessions to `~\.gemini\antigravity\brain\`
    -   Restore knowledge items
    -   Auto-seed the current session with key artifacts (task.md, walkthrough...)
    -   Ask the user if it cannot auto-detect the session ID

4.  Notify: "✅ Restore complete — you can continue working normally!"
