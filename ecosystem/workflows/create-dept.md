# department: operations
---
description: tạo phòng ban mới và/hoặc agent mới trong omniclaw corp
---

# omniclaw corp — quy trình tạo phòng ban & agent mới

## nguyên tắc bất biến

> **không bao giờ tự ý tạo phòng ban/agent mà không có ceo duyệt.**
> flow bắt buộc: **phân tích → đề xuất → ceo duyệt → execute**

---

## khi nào mở quy trình này?

| trigger | ai khởi động |
|---------|-------------|
| phát hiện gap khi phân tích repo/url/tài liệu | antigravity tự đề xuất |
| ceo hỏi/brainstorm về dept/agent mới | antigravity phân tích + đề xuất |
| ceo ra lệnh trực tiếp | bỏ Step propose, thực thi ngay |

---

## phase 1 — phân tích & đề xuất (antigravity)

### Step 1: kiểm tra agent có sẵn trước
```bash
python system/ops/scripts/create_agent.py --list
python system/ops/scripts/create_agent.py --check <agent-id>
```
- nếu agent phù hợp **đã tồn tại** → chỉ cần assign vào dept mới (phase 2b)
- nếu **chưa có** → cần tạo agent mới (phase 2a)

### Step 2: kiểm tra dept có sẵn
```bash
python system/ops/scripts/propose_dept.py --scan
```

### Step 3: tạo proposal và báo ceo
```bash
python system/ops/scripts/propose_dept.py --propose
```
- proposal được lưu vào: `brain/shared-context/corp/proposals/`
- antigravity báo ceo: "tôi đề xuất tạo phòng ban x vì lý do y, cần ceo duyệt."

---

## phase 2a — tạo agent mới (khi chưa có agent phù hợp)

### Step 4: ceo duyệt proposal

### Step 5: scaffold agent
```bash
python system/ops/scripts/create_agent.py \
  --id <agent-id> \
  --dept <dept-name> \
  --tier <2|3> \
  --title "<agent title>"
  [--head]   # nếu là department head
```

**files tự động tạo:**
- `ecosystem/workforce/agents/<agent-id>/agent.md` — từ template
- `brain/corp/memory/agents/<agent-id>.md`
- `system/telemetry/receipts/agent_onboard/<agent-id>.json`
- `ecosystem/workforce/agents/<agent-id>/skill.md`
- *(nếu --head)* `ecosystem/workforce/departments/<dept>/manager_prompt.md`, `worker_prompt.md`, `rules.md`

---

## phase 2b — assign agent có sẵn vào dept

nếu agent đã có agent.md, script tự động:
1. update trường `department:` trong agent.md
2. kiểm tra `org_chart.yaml` — báo nếu chưa đăng ký
3. ghi assignment receipt: `telemetry/receipts/agent_assign/`

---

## phase 3 — tạo & kích hoạt phòng ban

### Step 6: ceo approve → auto-execute toàn bộ
```bash
# approve 1 phòng ban
python system/ops/scripts/propose_dept.py --approve <dept-name>

# approve tất cả
python system/ops/scripts/propose_dept.py --approve-all
```

**script tự động chạy 3 Step:**

**step 1 — dept files:**
```
ecosystem/workforce/departments/<dept>/manager_prompt.md
ecosystem/workforce/departments/<dept>/worker_prompt.md
ecosystem/workforce/departments/<dept>/rules.md
brain/corp/memory/departments/<dept>.md
brain/shared-context/corp/daily_briefs/<dept>.md
```

**step 2 — smart agent routing:**
- agent đã có agent.md → assign (2a path)
- chưa có → gọi `create_agent.py` scaffold (2b path)

**step 3 — system registration:**
- `agents.md` → append agent entry (boot step 4 nhận ra agent)
- `kpi_scoreboard.json` → add dept kpi slot (corp_cycle tracking)
- `blackboard.json` → update `corp_state.total_depts`
- `org_chart.yaml` → **tự động update** bằng ruamel.yaml
- `library_graph.json` → **tự động đăng ký nodes & edges** cho agent/dept mới vào thư viện.

---

## phase 4 — manual verification (luôn làm)

sau khi script chạy xong, kiểm tra:

```bash
# check agent profile đủ chưa
python system/ops/scripts/create_agent.py --check <agent-id>

# check dept files đủ chưa
python system/ops/scripts/propose_dept.py --scan
```

checklist thủ công:
- [ ] `brain/corp/org_chart.yaml` — agent xuất hiện đúng dept section
- [ ] `brain/shared-context/agents.md` — entry được thêm đúng format
- [ ] `skill_registry.json` — assign skills cho agent mới nếu cần
- [ ] `library_graph.json` — agent và dept mới đã xuất hiện như node
- [ ] chạy `boot_check.py` để xác nhận hệ thống nhận ra dept mới

---

## notes

- **llm tier mặc định:** `economy` cho mọi agent mới (upgrade cần cfo+ceo)
- **autonomy mặc định:** `supervised` — mọi output phải được head agent review
- **strix gate:** agent mới phải qua security scan trước khi trao tool permissions
- **2-strike rule:** fail 2 lần cùng task → set blocked → report antigravity
