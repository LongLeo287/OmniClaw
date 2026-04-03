# department: operations
---
description: omniclaw corp v3.1 — quy trình khởi động toàn hệ thống, từ boot ai agent đến corp daily cycle
---

# 🚀 omniclaw startup — quy trình khởi động hệ thống
**version:** 1.0 | **date:** 2026-03-26 | **authority:** tier 0  
**trigger:** đầu mỗi ngày làm việc hoặc khi mở session mới  
**script tự động:** `python system/ops/omniclaw_startup.py`

---

## tổng quan — 3 giai đoạn khởi động

```
giai đoạn 1: system boot        (30 giây)
  → kiểm tra services, files, ports
  → tự động khởi động services thiếu

giai đoạn 2: agent boot         (1-2 phút)  
  → load context 9-step sequence (gemini.md)
  → register session vào blackboard
  → kiểm tra escalations, kpi, proposals

giai đoạn 3: corp activation    (theo yêu cầu)
  → ceo quyết định: corp cycle hay direct task
  → trigger: "omniclaw corp start" hoặc task trực tiếp
```

---

## giai đoạn 1 — system boot

### Step 1.1: khởi động tự động (chạy script)

```powershell
# lệnh duy nhất cần nhớ:
python system/ops/omniclaw_startup.py

# hoặc full verbose:
python system/ops/omniclaw_startup.py --verbose

# chỉ kiểm tra không khởi động:
python system/ops/omniclaw_startup.py --check-only
```

### Step 1.2: script kiểm tra (tự động)

script sẽ tự động kiểm tra và báo cáo:

| service | port | auto-start? |
|---------|------|-------------|
| ollama (local llm) | 11434 | ❌ thủ công |
| clawtask api | 7474 | ✅ tự động |
| gitnexus | 4747 | ✅ tự động |
| ag-auto-accept | 7476 | ✅ tự động |
| lightrag (rag) | 9621 | ✅ tự động |
| telegram bot | — | ✅ verify token |

### Step 1.3: file integrity check

script kiểm tra 6 file quan trọng (stop nếu thiếu):

```
✅ brain/shared-context/blackboard.json
✅ brain/shared-context/skill_registry.json
✅ brain/shared-context/corp/kpi_scoreboard.json
✅ brain/shared-context/corp/escalations.md
✅ brain/corp/org_chart.yaml (relative corp/)
✅ gemini.md
```

---

## giai đoạn 2 — agent boot (gemini.md 9-step sequence)

> **áp dụng cho:** antigravity (gemini) | bắt buộc mỗi session

```
step 1  → read gemini.md               ← entry point (file này)
step 2  → load soul.md                 ← identity & core values
step 3  → load governance.md           ← rules & authority
step 4  → load agents.md               ← 99 agent roster
step 5  → load thesis.md               ← strategy & 40 pillars
step 6  → load report_formats.md       ← output format guide
step 7  → check blackboard.json        ← active tasks & state
step 8  → load skill_registry.json     ← 20 skills available
step 9  → begin work                   ← sẵn sàng nhận lệnh
```

**rules bắt buộc:**
- skip bất kỳ step → vi phạm governance. log warning + report ceo.
- file missing → skip step, continue, báo ceo.
- hard rule: không đọc sai boot file (gemini ≠ claude code).

### Step 2.1: đọc blackboard state

```json
// đọc brain/shared-context/blackboard.json
{
  "open_items": [...],          // ← việc còn tồn đọng
  "active_campaign": "...",     // ← campaign đang chạy
  "handoff_trigger": "idle",    // ← idle = sẵn sàng
  "corp_cycle_status": "idle"   // ← idle = ok start cycle
}
```

**stop nếu:** `corp_cycle_status = "running"` → cycle trước chưa xong!

### Step 2.2: register session

```json
// update blackboard.json:
{
  "target_agent": "antigravity",
  "status": "active",
  "session_start": "<iso timestamp>",
  "handoff_trigger": "active"
}
```

### Step 2.3: ceo briefing (auto-generated)

```
📊 omniclaw corp status — <date>
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🏢 system:   <overall_status from kpi_scoreboard>
🔋 services: <n> live | <m> down
📋 blackboard: <summary từ last session>
⚠️  open items: <n> pending tasks
📌 escalations: <l2/l3 nếu có>
🎯 campaign: <active_campaign>
🧠 skills: <n> available
🔌 mcps: 8 configured

→ sẵn sàng nhận lệnh. corp cycle hay direct task?
```

---

## giai đoạn 3 — corp activation

### option a: corp daily cycle (khuyến nghị buổi sáng)

```powershell
omniclaw corp start   # full 8-phase cycle
# or
python ops/omniclaw.py corp start
```

flow: phase 0 → 1 → 2 → 3 → 4 → 5 → 6 → 7  
xem chi tiết: `ecosystem/workflows/corp-daily-cycle.md`

### option b: status check nhanh

```powershell
python system/ops/omniclaw_orchestrator.py once   # update hud + telegram
python ops/scripts/system_pulse.py            # health check 5-min
python ops/scripts/dept_health.py             # 21 dept health
```

### option c: nhiệm vụ trực tiếp (direct task)

ceo giao task trực tiếp → antigravity plan → handoff claude code

```
1. antigravity: plan + write implementation_plan.md
2. ceo: approve (lgtm)
3. antigravity: write blackboard.json handoff_trigger=active
4. claude code: execute + write receipts
5. antigravity: review + report vietnamese
```

---

## quick reference — lệnh khởi động

```powershell
# === khởi động nhanh (1 lệnh) ===
python system/ops/omniclaw_startup.py

# === data vault (sync dữ liệu) ===
powershell "d:\longleo\omniclaw corp\omniclaw remote\scripts\setup.ps1" # (kéo data: chạy setup)
python system/ops/scripts/omniclaw_data_push.py                  # (đẩy data: sync lên mây)

# === orchestrator ===
python system/ops/omniclaw_orchestrator.py once      # update hud + dispatch
python system/ops/omniclaw_orchestrator.py routes    # xem 77 routing rules

# === telegram ===
python system/ops/telegram_dispatch.py status    # gửi system status
python system/ops/telegram_dispatch.py test      # test kết nối

# === corp cycle ===
python ops/omniclaw.py corp start    # full cycle
python ops/omniclaw.py corp brief    # ceo brief only
python ops/omniclaw.py status        # current status

# === services thủ công ===
python system/ops/scripts/lightrag_server.py          # lightrag :9621
docker compose up -d infra/observability/             # langfuse :3100
```

---

## sơ đồ khởi động

```
ceo mở máy
    │
    ▼
[terminal] python system/ops/omniclaw_startup.py
    │
    ├─ [1.1] check blackboard.json       ✅ pass / ❌ stop
    ├─ [1.2] check 6 critical files      ✅ pass / ⚠️ warn
    ├─ [1.3] check ports                 ✅ live  / 🔴 down
    ├─ [1.4] check skill_registry        ✅ fresh / ⚠️ old
    ├─ [1.5] update hud status.json      ✅ done
    └─ [1.6] send telegram boot report   ✅ sent
    │
    ▼
[ai agent] antigravity đọc gemini.md
    │
    ├─ step 2: soul.md          ← identity
    ├─ step 3: governance.md    ← rules
    ├─ step 4: agents.md        ← roster
    ├─ step 5: thesis.md        ← strategy
    ├─ step 6: report_formats   ← output format
    ├─ step 7: blackboard.json  ← state check
    ├─ step 8: skill_registry   ← load skills
    └─ step 9: begin work
    │
    ▼
[ceo] nhận briefing từ antigravity:
    │
    ├─ corp cycle? → "omniclaw corp start"
    ├─ direct task? → Description task
    └─ status check? → "omniclaw status" hoặc hud
```

---

## các trường hợp đặc biệt

### trường hợp 1: blackboard `corp_cycle_status = "running"`
```
→ cycle trước chưa xong. không start cycle mới.
→ đọc escalations.md để hiểu tình trạng.
→ ceo quyết định: reset hay tiếp tục?
→ reset: set blackboard corp_cycle_status = "idle"
```

### trường hợp 2: có l3 escalation mở
```
→ không start corp cycle.
→ báo cáo ceo ngay lập tức.
→ ceo resolve l3 trước khi start.
```

### trường hợp 3: service quan trọng down
```
ollama down → không dùng local llm được. dùng api thay thế.
clawtask down → mất task tracking. chạy: npm start --prefix ecosystem/tools/clawtask
lightrag down → civ pipeline bị ảnh hưởng. fallback: claude code researcher
telegram down → mất notification. check .env bot_token.
```

### trường hợp 4: skill_registry > 7 ngày chưa cập nhật
```
→ warning. không stop.
→ chạy: python system/ops/omniclaw_orchestrator.py once (tự update)
→ hoặc: powershell ops/scripts/skill_loader.ps1
```

---

## security checklist (mỗi boot)

```
☐ skillsentry 9-layer scanner: active (passive monitoring)
☐ không có credentials trong project files
☐ .env không được commit vào git
☐ strix-agent sẵn sàng scan tool mới
☐ gemini.md có "hard rule" còn hiệu lực
```

---

## session close protocol

khi kết thúc session (đọc `post-session.md` để chi tiết):

```
1. update blackboard.json:
   - status: "idle"
   - handoff_trigger: "complete" hoặc "blocked"
   - summary: <tóm tắt session>

2. mark tasks trong clawtask: done/blocked

3. l2/l3 issues → write to corp/escalations.md

4. auto: powershell ops/scripts/update_hud.ps1 (hud snapshot)
```

---

*v1.0 | 2026-03-26 | omniclaw corp v3.1 | owner: antigravity*  
*xem thêm: gemini.md, antigravity-boot.md, pre-session.md, corp-daily-cycle.md*
