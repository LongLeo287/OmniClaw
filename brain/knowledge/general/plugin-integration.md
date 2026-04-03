---
id: plugin-integration
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:00.674103
---

# Department: operations
---
description: Plugin Integration Process — OmniClaw Corp (Quy trình tích hợp Plugin)
---

# Plugin Integration Workflow
# Version: 1.0 | 2026-03-23 | Owner: Antigravity (Dept 4 — Registry)

Quy trình bắt buộc khi tích hợp bất kỳ repo/plugin/tool mới vào OmniClaw Corp.
Trigger: `omniclaw integrate <plugin_id>` hoặc khi CEO request.

> ⚠️ **PRE-GATE:** Workflow này chỉ chạy SAU KHI `ops/workflows/repo-evaluation.md` cho phán quyết **APPROVE**.
> Nếu chưa chạy repo-evaluation → STOP, quay lại bước đánh giá trước.


---

## PHASE 0 — Catalog & Conflict Check

### 0.1 — Đánh dấu repo trong plugin-catalog.md

Mở `plugins/plugin-catalog.md` và cập nhật Status:

| Ký hiệu | Ý nghĩa |
|---------|---------|
| `👁️` | Đã đọc/khảo sát README |
| `🔖` | Giữ lại, có thể dùng sau |
| `✅` | Đang sử dụng (theo dõi version) |
| `⚡` | Đang trong quá trình tích hợp |
| `❌` | Loại bỏ (trùng Features: / không phù hợp) |

**Rule:** Mọi repo trong `plugins/` phải có Status: trong catalog trước khi đọc code.

### 0.2 — Conflict check

Kiểm tra Features: mới có trùng với plugin hiện có không:

```
1. Liệt kê Core Features: của plugin mới
2. So sánh với plugins/registry.json (status: active)
3. So sánh với blackboard.json infrastructure section
4. Nếu trùng: đánh giá "bổ sung" hay "thay thế"
   - Bổ sung → OK, ghi rõ use case phân biệt
   - Thay thế → phải deprecate plugin cũ trước
```

### 0.3 — Update catalog: ⚡ (in progress)

---

## PHASE 1 — Security Scan (RULE-PROCESS-01 Bắt buộc)

**Owner: Dept 10 — Security/GRC (Strix)**

```bash
# Chạy nemoclaw-strix-scan trên repo
# See: ops/workflows/nemoclaw-strix-scan.md
```

Minimum check:
- [ ] License compatible (MIT/Apache/BSD preferred; AGPL flag for CEO review)
- [ ] No hardcoded credentials, API keys
- [ ] No cryptominer, obfuscated code
- [ ] Source repo is public/verified
- [ ] `pip show <package>` hoặc `npm info <package>` — verify publisher

Result: **CLEAR** hoặc **FLAG** (CEO quyết định nếu FLAG)

---

## PHASE 2 — Tạo Plugin Structure (PLUGIN_SPEC.md)

```
plugins/<plugin_id>/
├── manifest.json     [REQUIRED]
├── PLUGIN.md         [REQUIRED] — hướng dẫn cho agents
├── README.md         [REQUIRED] — tổng quan
├── <adapter>.py      [nếu cần wrapper]
└── tests/            [REQUIRED]
    └── test_<id>.py  — smoke tests
```

### manifest.json checklist
- [ ] `id`, `name`, `version`, `type`, `status` điền đầy đủ
- [ ] `agent_hooks` khai báo đúng hooks dùng
- [ ] `auto_load: false` (mặc định — không tự load khi boot)
- [ ] `can_crash_os: false` — bắt buộc
- [ ] `conflict_check` section: ghi Result: phase 0
- [ ] `upstream_check`: tần suất check version mới

---

## PHASE 3 — Version Tracking Setup

Thêm vào **Version Tracking table** trong `plugin-catalog.md`:

```markdown
| <plugin_id> | <current_version> | <frequency> | <update_command> |
```

**Tần suất theo mức độ quan trọng:**
- Core agent tools → Weekly
- Data/bridge tools → Monthly
- Security tools → Weekly
- Reference/UI → Quarterly

---

## PHASE 4 — Đăng ký Registry

Cập nhật `plugins/registry.json`:

```json
{
  "id": "<plugin_id>",
  "type": "<cognitive|data|bridge|ui>",
  "status": "active",
  "auto_load": false,
  "path": "plugins/<plugin_id>/",
  "manifest": "plugins/<plugin_id>/manifest.json",
  "notes": "<Description: ngắn, ngày tích hợp>",
  "registered_at": "YYYY-MM-DD",
  "upstream_check": "<frequency> — <command>"
}
```

Cập nhật `total_registered` và `active_count`.

---

## PHASE 5 — Activation Commands (RULE-ACTIVATION-01)

**Nếu plugin cần cmd/powershell để kích hoạt:**

### 5a — Thêm vào Dashboard (dashboard.ps1)

Mở `$OMNICLAW_ROOT\launcher\dashboard.ps1` và thêm vào section **PLUGIN MANAGER**:

```powershell
# Trong menu [P] Plugin Manager → sub-menu
"<plugin_id>" = @{
    Name = "<Display Name>"
    Check = { <check if installed/running> }
    Install = "<install command>"
    Start = "<start command, nếu có>"
    Port = <port nếu có service, $null nếu không>
}
```

### 5b — Thêm vào ClawTask (Port 7474)

Nếu plugin là một **service có port** → thêm vào `$SERVICES` trong `dashboard.ps1`.

Nếu plugin là **library/tool** (không có port) → chỉ thêm vào Plugin Manager section.

### 5c — Update MASTER.env (nếu cần API key)

```
$OMNICLAW_ROOT\ops\secrets\MASTER.env
```

---

## PHASE 6 — Test & Verify

```bash
# 1. Chạy smoke tests
python plugins/<plugin_id>/tests/test_<id>.py

# 2. Verify registry
python -c "import json; r=json.load(open('plugins/registry.json')); print([p for p in r['plugins'] if p['id']=='<id>'])"

# 3. Test activation từ dashboard (nếu có)
# Mở OmniClaw Corp.cmd → [P] Plugin Manager → chọn plugin
```

---

## PHASE 7 — Update Blackboard & Catalog

```
1. blackboard.json: cập nhật open_items nếu đây là OPEN task
2. plugin-catalog.md: status ⚡ → ✅, thêm version tracking
3. telemetry/receipts/<plugin_id>/: log activation đầu tiên
```

---

## PHASE 7b — Register Rules, Skills & Workflow Hooks (BẮT BUỘC)

> Đây là bước thường bị bỏ qua. Phải làm NGAY SAU Phase 7.

### 7b.1 — Thêm RULE vào GEMINI.md

Nếu plugin Changes: cách agent làm việc, PHẢI thêm rule rõ ràng:

```
Mở: $OMNICLAW_ROOT\GEMINI.md
Thêm vào SECTION 3 — ANTIGRAVITY SPECIFIC RULES:

**[RULE-<XYZ>-01]** <Tên rule>:
  1. Khi nào dùng plugin này
  2. Cách gọi (import, function)
  3. Scope: phòng ban nào / agent nào
  
Full docs: plugins/<plugin_id>/PLUGIN.md
```

### 7b.2 — Đăng ký SKILL_REGISTRY.json

```
Mở: brain/shared-context/SKILL_REGISTRY.json
Thêm entry vào "entries" array:
{
  "id": "<plugin_id>",
  "name": "<Display Name>",
  "tier": 2,
  "status": "active",
  "source": "plugin",
  "path": "plugins/<plugin_id>/SKILL.md",
  "adapter": "plugins/<plugin_id>/<adapter>.py",
  "description": "<Description: ngắn khi nào dùng>",
  "domain": "<data|core|bridge|ui>",
  "accessible_by": ["<agent_ids>"],
  "exposed_functions": ["<function_names>"],
  "listens_to": { "<hook>": "<function_call>" },
  "rule": "<RULE-ID>",
  "noop_safe": true
}
Tăng "count" lên.
Validate: python -c "import json; json.load(open('brain/shared-context/SKILL_REGISTRY.json'))"
```

### 7b.3 — Hook vào Workflows liên quan

Kiểm tra và cập nhật các workflow sử dụng plugin này:

```
- ops/workflows/knowledge-ingest.md  → step "fetch URL/search"
- ops/workflows/corp-daily-cycle.md  → nếu plugin chạy daily
- ops/workflows/agent-workflow.md    → nếu agent cần dùng plugin
```

Cụ thể: tìm các bước hiện dùng fallback thủ công → thay bằng adapter call.

---

## VERSION TRACKING — Weekly/Monthly Checks

```powershell
# Chạy từ dashboard: [V] Version Check (mới thêm)
# Hoặc chạy thủ công:
pip show mem0ai
pip show firecrawl-py
pip show crewai
# → So sánh với version trong plugin-catalog.md
# → Nếu có version mới: pip install --upgrade <package>
```

---

*Workflow Owner: Antigravity | Dept 4 Registry | Last updated: 2026-03-23*
*"Catalog first. Security second. Register third. Never skip."*

