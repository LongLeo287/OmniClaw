# Department: engineering
---
description: Antigravity → Claude Code CLI handoff — quy trình duy nhất, đầy đủ
---
# Claude Code Handoff Protocol
# Version: 3.0 | Updated: 2026-03-26 | SINGLE SOURCE OF TRUTH
# Merges: claude-code-handoff.md v2.0 + automated_cli_handoff.md v2.1

// turbo-all

---

## Khi Nào Antigravity Handoff Sang Claude Code?

| Task Type | Lý do dùng Claude Code |
|---|---|
| Viết code phức tạp (>200 dòng) | Long-context code generation |
| Multi-file refactoring | DEVELOPER role + bash execution |
| Chạy shell/PS1 commands hàng loạt | Native execution, không cần confirm |
| Tạo/debug test suite | QA role + sub-agent isolation |
| Reverse engineering repo cũ | RESEARCHER role + file traversal |
| CIV: phân tích repo phức tạp | gitingest + code analysis |
| Dọn dẹp/di dời file hàng loạt | Auto-mode, CEO đã approve trước |

---

## Luồng Hoàn Chỉnh (Antigravity → Claude Code → Antigravity)

```
[ANTIGRAVITY]
    │  1. Chuẩn bị task (CEO approve hoặc Phase 4 daily cycle)
    │  2. Viết task detail → subagents/mq/claude_code_tasks.md
    │  3. Ghi blackboard.json: handoff_trigger = "READY"
    │  4. Gọi launcher: ops/scripts/handoff_to_claude_code.ps1
    ▼
[LAUNCHER SCRIPT — 5 Safety Checks]
    │  ✓ .clauderules tồn tại?
    │  ✓ .claudeignore tồn tại?
    │  ✓ blackboard.json có handoff_trigger = "READY"?
    │  ✓ Gatekeeper GRANT workspace?
    │  ✓ Git snapshot tạo thành công?
    │  → Chọn mode: SUPERVISED (1) hoặc AUTONOMOUS (2)
    ▼
[CLAUDE CODE CLI]
    │  Boot: đọc CLAUDE.md → blackboard.json → task file
    │  Thực thi task theo role (DEVELOPER/QA/RESEARCHER)
    │  Viết receipt → telemetry/receipts/
    │  Cập nhật blackboard: handoff_trigger = "COMPLETE" | "BLOCKED"
    ▼
[ANTIGRAVITY]
       Monitor blackboard
       COMPLETE → đọc receipt → báo CEO (tiếng Việt)
       BLOCKED  → đọc failure notes → retry hoặc escalate
       Reset: handoff_trigger = null
```

---

## Step 1: Antigravity Chuẩn Bị Task

### 1a. Viết task vào queue
File: `subagents/mq/claude_code_tasks.md`
```markdown
# Claude Code Task — CC-YYYYMMDD-XXX
Priority: HIGH | MEDIUM | LOW
Roles: DEVELOPER | QA | RESEARCHER

## Context
<ngữ cảnh ngắn gọn>

## Task Steps
- [ ] Step 1: ...
- [ ] Step 2: ...

## Acceptance Criteria
- [ ] Tiêu chí 1
- [ ] Tiêu chí 2

## RECEIPT (REQUIRED)
Write: telemetry/receipts/<task-id>.md
```

### 1b. Cập nhật blackboard
File: `brain/shared-context/blackboard.json`
```json
{
  "handoff_trigger": "READY",
  "source_agent": "Antigravity",
  "target_agent": "Claude Code",
  "task_payload": {
    "task_id": "CC-YYYYMMDD-XXX",
    "description": "<mô tả ngắn>",
    "task_file": "subagents/mq/claude_code_tasks.md",
    "workspace_id": "<PRJ-XXX>",
    "workspace_path": "$OMNICLAW_ROOT",
    "priority": "HIGH"
  },
  "blackboard_updated_at": "<ISO 8601>"
}
```

### 1c. Gọi launcher
```powershell
& "$OMNICLAW_ROOT\ops\scripts\handoff_to_claude_code.ps1"
```

---

## Step 2: Chọn Execution Mode

Launcher hiện 2 lựa chọn (auto-select SUPERVISED sau 15s):

| Mode | Flag | Khi nào dùng |
|---|---|---|
| **SUPERVISED** (default) | `claude` | Task có rủi ro, cần review |
| **AUTONOMOUS** | `claude --enable-auto-mode` | CEO đã approve, task rõ ràng |

> ⚠️ `--dangerously-skip-permissions` đã DEPRECATED — dùng `--enable-auto-mode`

---

## Step 3: Claude Code Boot Khi Nhận Handoff

Claude Code tự động đọc theo thứ tự:
1. `CLAUDE.md` (boot protocol)
2. `brain/shared-context/blackboard.json` → tìm `handoff_trigger: "READY"`
3. `subagents/mq/claude_code_tasks.md` → task steps
4. Thực thi theo role → viết receipt → cập nhật blackboard

---

## Step 4: Antigravity Nhận Kết Quả

```
Monitor: brain/shared-context/blackboard.json
  → "COMPLETE" : đọc receipt → báo CEO bằng tiếng Việt → reset blackboard
  → "BLOCKED"  : đọc blocked_task → retry hoặc escalate CEO
  → Reset: { "handoff_trigger": null, "blocked_task": null }
```

---

## Capabilities Của Claude Code Trong OmniClaw

```
1. Auto-execute (--enable-auto-mode)     → Hàng loạt file ops không cần confirm
2. Sub-agent spawning (isolated context) → Parallel testing, parallel writes
3. Long-context code gen (200K tokens)   → Viết module lớn không bị truncation
4. DEVELOPER → QA → RESEARCHER roles    → Self-review code vừa viết
5. Native git integration               → Snapshot trước task, reset --hard nếu fail
6. .claude/commands/ slash commands     → /project:omniclaw-intake, /project:vet-repo
```

---

## CIV Integration

Khi Claude Code nhận task intake repo:
1. Đọc `corp/departments/content_intake/WORKER_PROMPT.md` (v1.2)
2. Chạy STEP 0: LightRAG check
3. Fill `_CIV_ANALYSIS.md` 6 câu → trigger STEP 3.6 via blackboard

---

*v3.0 | 2026-03-26 | Merged from: claude-code-handoff.md v2.0 + automated_cli_handoff.md v2.1*
*"Antigravity thinks. Claude Code acts. One handoff, one truth."*

