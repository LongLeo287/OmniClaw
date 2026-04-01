# [HANDOFF] Job Assignment Campaign: Building Skills for GCP Architect

**From:** Antigravity (Chief Architect)
**To:** Claude Code CLI (Implementation Engineer)
**Goal:** Build the entire Profile and Skills Code for Agent `gcp_architect` based on OmniClaw V3.1 `Open Standard` documents and intelligence from Google Developer MCP.

---

## 🛠️ Foundation knowledge (Claude Code is required to read before coding)
Open and devour the following 3 documents to understand the rules of the Boss Code (OmniClaw):
1. `$OMNICLAW_ROOT\brain\knowledge\agent_skills_open_standard.md` (CODE SKILL LAW)
2. `$OMNICLAW_ROOT\brain\knowledge\spawn_agent_skill.md` (SKILL CREATION INSTRUCTIONS)
3. Look up `google-developer-knowledge` MCP to find the latest documentation on: *gcloud CLI, Cloud Run, Cloud Build.*

## 📋 Task Queue
- [ ] **Initialize the Skill system:** In the `ecosystem/skills/` directory, create a new Skill set named `gcp_deploy_skill`. This set of code must be 100% Open Standard (such as `schema.json`, `index.py`, `README.md`).
- [ ] **Coding logic:** Write Python code inside this Skill to execute the commands `gcloud builds submit` and `gcloud run deploy`. Do not make up orders! Must use MCP Google Dev to look up gcloud API first.
- [ ] **Attach Skill to Implant (Bind):** Modify the files `ecosystem/workforce/agents/gcp_architect/agent.yaml` and `prompts/system_prompt.md` to connect this Subagent directly to the Skill `gcp_deploy_skill` just created.
- [ ] **Cross-check:** Make sure the code runs smoothly on the Local (simulated) environment or at least does not have Google Command Syntax errors.
- [ ] **Report:** Write the result "Satisfactorily Completed" to `brain/shared-context/blackboard.json` (change `handoff_trigger` to `DONE`).

> ⚠ **CLAUDE CODE CLI ATTENTION:** Absolutely do not delete any System files. After completing the code, remember to report back to the Master.

---

## TASK-CC-0326-BOOT-FIX: Sync CLAUDE.md Cycle Number
**Status:** DONE
**Priority:** P1
**Assigned:** Claude Code CLI
**Created:** 2026-03-26T19:16:00+07:00

### Tasks
Fix CLAUDE.md header: Cycle 8 (2026-03-23) -> Cycle 11 (2026-03-26)

### Steps
1. Doc file CLAUDE.md at root: $OMNICLAW_ROOT\CLAUDE.md
2. Tim: # OmniClaw Corp | Cycle 8 | Last synced: 2026-03-23
3. Replace bar: # OmniClaw Corp | Cycle 11 | Last synced: 2026-03-26
4. Save UTF-8 files
5. Verify: git diff CLAUDE.md

### Receipt
system/telemetry/receipts/RECEIPT_CC0326_claude_md_sync.md