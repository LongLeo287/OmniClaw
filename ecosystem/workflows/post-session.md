# Department: operations
﻿# post-session.md — OmniClaw Session Close Hook
# Version: 1.0 | Updated: 2026-03-14
# Authority: Tier 2 (Operations)
# Executed by: Any agent at end of every session (before disconnect)

---

## AUTO-TRIGGER — Khi nào chạy?

Antigravity TỰ ĐỘNG chạy post-session khi nhận BẤT KỲ signal nào:

| Signal | Ví dụ | Trigger |
|--------|-------|--------|
| CEO nói kết thúc | "kết thúc phiên" / "end session" / "tạm biệt" / "xong rồi" | ✅ Chạy ngay |
| Task hoàn thành | CEO approve kết quả cuối, không hỏi thêm | ✅ Chạy ngay |
| Phiên mới bắt đầu | "bắt đầu phiên mới" / "khởi động lại" | ✅ Handoff session cũ trước |

**KHÔNG đợi CEO nói:** "handoff" / "cập nhật blackboard" / "viết brief" / "update HUD"

---
## Purpose

Ensure continuity between sessions by saving context, archiving evidence,
and leaving clear handoff notes for the next session.

---

## Execution Steps (Run in Order)

### Step 0.5: LTM Auto-Save (Long-Term Memory — NEW)
```
Before closing session — save key context to vector memory:
  python system/ops/scripts/save_session_memory.py --from-blackboard
  OR
  python system/ops/scripts/save_session_memory.py "[tóm tắt phiên ngắn gọn]"

This ensures OmniClaw remembers what happened across sessions (vectorized, not just text).
Silent fail if LTM offline — never block session close.
```

### Step 1: Context Snapshot
```
Write to smart_memory:
  {
    "session_end": "[ISO 8601]",
    "last_task": "[task_id or description]",
    "status": "[COMPLETE | IN_PROGRESS | BLOCKED]",
    "key_decisions": ["...", "..."],
    "open_items": ["...", "..."]
  }
```

### Step 2: Blackboard Handoff Note
```
If status = IN_PROGRESS (task not fully done):
  Update blackboard.json context field:
  {
    "session_interrupted": true,
    "last_completed_step": "[step N]",
    "next_step": "[step N+1 description]",
    "notes": "[anything next session needs to know]"
  }

If status = IDLE (nothing in progress):
  Set blackboard.json: handoff_trigger = null, status = "IDLE"
```

### Step 3: Knowledge Update
```
If any new knowledge was generated this session:
  → Update knowledge/knowledge_index.md with new entry
  → Save relevant notes to knowledge/[topic].md

If cognitive_reflector ran this session:
  → Ensure lessons are saved to cosmic_memory
```

### Step 3B: Autonomous Facility Sanitation (Dept 22)
```
TỰ ĐỘNG CHẠY Ở CUỐI PHIÊN LÀM VIỆC.
Trigger: Gọi kịch bản dọn dẹp hệ luỵ (omniclaw_deep_cleaner) để quét toàn cục.

Script: python system/ops/scripts/omniclaw_deep_cleaner.py --auto-delete --stale-days 14

Quy tắc dọn dẹp (RULE-CLEANUP-01):
1. Quét root directory ($OMNICLAW_ROOT) và đẩy mọi file tạo nháp lạc loài (.md, .py, .txt, .log) không thuộc hệ thống vào `storage/vault/DATA/stray_files/` để khoanh vùng rác.
2. Xóa sạch các repo mồ côi/rỗng trong `brain/knowledge/repos/*`.
3. Clear các report và log rác cũ (>14 ngày) khỏi `QUARANTINE/` và `storage/vault/DATA/`.

Silent fail nếu không có gì cần dọn — KHÔNG block session close.
```

### Step 4: Receipt Archive (if large)
```
Check: telemetry/receipts/ file count

If file count > 50:
  → Move receipts older than 7 days to telemetry/receipts/archive/
  → Log: "Archived [N] receipts"

Do NOT delete receipts — only archive.
```

### Step 5: Skill Registry Check
```
If any new SKILL.md was created or modified this session:
  → Reminder: "Run skill_loader.ps1 to update registry"

If skills/experimental/ has files not yet reviewed:
  → Reminder: "N skills in experimental/ awaiting review"
```

### Step 6: Session Close Announcement (Auto + Telegram notify)
```
Output (Vietnamese):

"📋 Phiên làm việc kết thúc.
- Đã lưu: context + decisions vào smart_memory
- Trạng thái: [COMPLETE | IN_PROGRESS | BLOCKED]
- Ghi chú cho phiên sau: [1-2 câu]
- Nhắc nhở: [skill registry / experimental skills nếu có]"
```

```powershell
# Báo Star Office UI: phiên đã đóng, chuyển sang idle
python "$OMNICLAW_ROOT\dashboard\set_state_aios.py" --state idle --detail "Phiên làm việc đã kết thúc - Tạm biệt!"
```

### Step 7: HUD Auto-Update (non-blocking)
```
Trigger: always run at session end — even if previous steps failed

powershell ops/scripts/update_hud.ps1 -Quiet
→ Port check (Ollama:11434, ClawTask:7474, LightRAG:9621)
→ Count open_items từ blackboard.json
→ Count pending proposals từ corp/proposals/
→ Update hud/STATUS.json (machine-readable)
→ Update hud/HUD.md services table (2-way write)
→ Create hud/snapshots/<date>_<time>.md (history)
→ Telegram: session summary (nếu có token)

On failure: skip silently — log warning only, NEVER block session close
```

---


## On Failure

If any step fails:
- Log warning, continue to next step
- Critical: Step 1 (context snapshot) — retry once if fails
- If Step 1 still fails: write manually to blackboard.json context field

