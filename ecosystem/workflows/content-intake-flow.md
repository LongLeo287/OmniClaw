# department: content_intake
# content intake & vetting — intake flow
# version: 1.4 | updated: 2026-03-27
# owner: content_intake dept (intake-chief-agent)
# change v1.4: +pending_repos.md role clarification | +rule-civ-02 pending gate | +step 6 cleanup
# change v1.2: +phase 0 local-first check | +step 3.5 gap detection | +step 3.6 gap proposal engine
# coordinate: security_grc (repo vetting) | asset_library (knowledge) | registry (code)

---

## full pipeline map

```
╔══════════════════════════════════════════════════════════════╗
║              content intake & vetting pipeline  v1.3         ║
╚══════════════════════════════════════════════════════════════╝

user / agent provides input
(thả tay bất cứ định dạng nào: link repo, url, document, pdf, post, hình ảnh)
            or
batch input from vault:
  storage/vault/data/pending_repos.md  ← hàng đợi chờ civ review (chưa được phép clone!)
  storage/vault/data/active_repos.md   ← đã qua civ + ceo approve → được phép clone & ingest
  storage/vault/data/github.txt        ← raw links chưa phân loại

⚠️ rule-civ-02 — pending gate:
  pending_repos.md = waiting room. repo ở đây chưa được phân tích.
  nghiêm cấm clone repo từ pending thẳng vào brain/quarantine mà không qua civ review.
  luồng bắt buộc: pending → civ analysis → ceo/intake-chief approve → active_repos.md → clone & ingest.

🚨 rule tối thượng: ngay khi nhận được mọi thể loại input, hệ thống phải tự động chạy, tự động nhận, tự động phân tích và cuối cùng tự động nhả báo cáo chuẩn "format 6 — dashboard analytics report" (xem presentation-protocol.md).
            │
            ▼
┌─────────────────────┐
│   phase 0 local     │  ← lightrag query + index.md check (new v1.2)
│   check (antigrav)  │  ← found? return ki. not found → continue
└─────────────────────┘
            │ not found
            ▼
┌─────────────────────┐
│    intake-agent     │  ← creates civ ticket, stages to /incoming/
│  [gate: ticket]     │
└─────────────────────┘
            │
            ▼
┌─────────────────────┐
│  classifier-agent   │  ← tags type: repo/web/doc/image/text/plugin
│  [gate: classify]   │
└─────────────────────┘
            │
    ┌───────┴──────────────────────────────┐
    │                                      │
    ▼                                      ▼
repo / plugin                     other content
(sec path)                        (content path)
    │                                      │
    ▼                                      │
┌──────────────────┐              ┌────────┴────────┐
│ repo-fetcher     │              │web_content       │
│ clone to         │              │ → web-crawler    │
│ /incoming/repos/ │              │                  │
└──────────────────┘              │document (pdf/doc)│
    │                             │ → doc-parser     │
    ▼                             │                  │
┌──────────────────────────────┐  │image             │
│ security grc (strix-agent)   │  │ → staging to     │
│ runs vet_repo.ps1            │  │   /incoming/imgs/│
│ 12-stage strix scan          │  │                  │
│                              │  │text/config       │
│ fail → rejected + blacklist  │  │ → staging to     │
│ warn → intake-chief review   │  │   /incoming/text/│
│ pass → /vetted/repos/        │  └────────┬────────┘
└──────────────────────────────┘           │
    │ pass                                  ▼
    │                             ┌──────────────────────┐
    ▼                             │ content-validator    │
┌──────────────────────────────┐  │ score 1-10           │
│ ★ step 3.5 — notebookllm    │  │ score 1-10           │
│   content analysis (v1.2)    │  │ < 4 → rejected       │
│                              │  │ ≥ 4 → /vetted/       │
│ tool: open-notebook          │  └──────────┬───────────┘
│ input: gitingest digest      │             │
│                              │             │
│ questions (6 total v1.2):    │             │
│ • "repo này làm gì?"         │             │
│ • "conflict với hệ thống?"   │             │
│ • "route về phòng nào?"      │             │
│ • "chất lượng / rủi ro?"     │             │
│ • "domain này omniclaw đã có    │             │
│    agent/dept nào không?"    │             │
│ • "đề xuất agent/dept mới    │             │
│    nếu chưa có?"             │             │
│                              │             │
│ output: civ analysis report  │             │
│   approved  → /vetted/       │             │
│   review    → intake-chief   │             │
│   rejected  → /rejected/     │             │
│   gap found → step 3.6 ★    │             │
└──────────────────────────────┘             │
            │ gap found
            ▼
┌──────────────────────────────┐
│ ★ step 3.6 — gap proposal    │
│   engine (antigravity)       │
│ domain mới, chưa có agent?   │
│ → gửi ceo proposal [a/b/c/d] │
│ a: kích hoạt agent-auto-create.md │
│ b: mở rộng dept hiện có      │
│ c: tạo dept/group mới        │
│ d: archive global            │
└──────────────┬───────────────┘
               │ (non-blocking: proposal is queued. intake continues!)
               ▼
        ┌─────────────────────┐
        │  ingest-router      │
        │  [gate: route]      │
        └─────────────────────┘
                   │
    ┌──────────────┼──────────────────────┐
    │              │                      │
    ▼              ▼                      ▼
registry &    asset & knowledge        assets/
capability    library                  (images)
(code/plugins) (knowledge/docs/web)   → asset-tracker

                   │
                   ▼
           ticket → ingested ✓
           receipt written to destination agent
```

---

## intake ticket lifecycle

```
local_hit (return existing ki, no ticket needed)
     or
received → classifying → vetting → validating → routing → ingested → cleaned
                                              ↘
                                           rejected (any stage) → cleaned_rejected
                         ↘
                      gap_proposed (parallel, non-blocking)
```

---

## workflow steps

### step 0 — local-first check ★ new v1.2
trigger: bất kỳ input nào — trước khi tạo civ ticket
agent: `antigravity` (tier 1)
skill: `smart_memory`, `lightrag` (localhost:9621)
actions:
- query lightrag: `rag.hybrid_query("<source url or topic>", mode="mix")`
- kiểm tra `brain/knowledge/index.md` có source url / domain không
- chạy `system/ops/scripts/staleness_check.py <url>` để tự động quyết định lấy dữ liệu:

kết quả:
  unchanged (no update / known url):
    → trả về ki đã có cho user/agent
    → stop (không tạo ticket, tiết kiệm băng thông)
  changed (new or updated content):
    → tiếp tục step 1 (tạo civ ticket bình thường)

sla: < 30 giây (local query)

---

### step 1 — receive input
trigger: user/agent provides url, file path, or content body
agent: `intake-agent`
actions:
- create civ-[date]-[seq] ticket in quarantine/logs/intake_log.md
- stage to quarantine/incoming/ (temp folder by type)
- set ticket status: received
- call classifier-agent

sla: immediate (synchronous)

---

### step 2 — classify
trigger: intake-agent hands off ticket
agent: `classifier-agent`
actions:
- inspect content type (url pattern, file extension, content body)
- assign tag: repo | web_content | document | image | text | config | plugin
- update ticket with classification
- route to correct pipeline branch
- unknown → /incoming/unclassified/ + alert intake-chief-agent

sla: < 5 minutes

---

### step 3a — repo/plugin path
trigger: classifier tag = repo or plugin
agent: `repo-fetcher-agent` then `security-scanner` (security grc)
actions:
- repo-fetcher: git clone (depth=1) into quarantine/incoming/repos/<name>/
  - ⚠️ timeout rule (v1.3): giới hạn clone tối đa 120s. nếu vượt quá, tự động skip repo, ghi log vào `skipped` list, và xóa (rmtree) thư mục clone dở dang để chống bloat rác ổ cứng.
- hand off to security-scanner: run vet_repo.ps1 (12-stage scan)
- strix-agent review _vet_report.md
- pass → move to quarantine/vetted/repos/ → step 3.5
- warn → hold, notify intake-chief-agent for manual review
- fail → move to quarantine/rejected/ + log to rejected_log.md → closed

sla: < 1 corp cycle

---

### step 3.5 — notebookllm content analysis ★ upgraded v1.2
trigger: security scan pass (repo/plugin path)
agent: `content-analyst-agent` using `open-notebook` (port 5055, local)
actions:
- run gitingest on repo → convert to text digest
- load digest into open-notebook
- query **6 standard civ questions** (v1.2 — thêm 2 câu gap detection):
  1. "repo/plugin này làm gì? Description chính xác purpose."
  2. "có conflict hoặc overlap với tools đã có trong omniclaw không?"
  3. "phòng ban nào nên sử dụng repo này?"
  4. "rủi ro nội dung: có sensitive data, suspicious logic, hoặc quality issues nào không?"
  5. ★ new: "domain này (kỹ năng/lĩnh vực) omniclaw đã có agent hoặc dept phụ trách chưa?" ← gap detection
  6. ★ new: "nếu chưa có, đề xuất tên agent hoặc dept mới phù hợp nhất?"
- generate civ analysis report → save to quarantine/vetted/repos/<name>/_civ_analysis.md
  - **mandatory format:** report phải xuất theo định dạng c-suite (no markdown headings, dùng in hoa + emoji, thuần ascii) đúng chuẩn `presentation-protocol.md`.
- decision:
  - approved + no gap (score ≥ 7/10) → step 5
  - approved + gap found (score ≥ 7/10) → step 3.6 (gap proposal) → step 5
  - review (score 4-6) → intake-chief-agent manual review
  - rejected (score < 4) → move to /rejected/ → closed

output fields:
  purpose, conflicts[], recommended_dept, quality_score, risk_notes, verdict,
  gap_detected (bool), gap_domain, proposed_agent, proposed_dept

sla: < 15 minutes per repo

---

### step 3.6 — gap proposal engine ★ new v1.2
trigger: step 3.5 output có `gap_detected = true`
agent: `antigravity` (tier 1 — escalate ceo decision)
skill: `proposal_engine` + `reasoning_engine`

actions:
1. đọc `gap_domain` và `proposed_agent` từ _civ_analysis.md
2. cross-check với `corp/org_chart.yaml` + `brain/knowledge/capability_map.md`
3. xác nhận gap thực sự chưa có agent/dept cover
4. tạo gap proposal gửi ceo qua `notification_bridge` (telegram):

```markdown
## 🔭 gap detected — civ-<id> — <date>

**source:** <repo_url>
**gap domain:** <domain>
**lý do:** không có agent/dept nào cover domain "<domain>" này

**omniclaw hiện có gần nhất:**
- dept x (match ~60%) — scope: <Description>

**đề xuất:**
[a] tạo agent: `<domain>-agent` → ops/workflows/agent-auto-create.md
[b] mở rộng dept x thêm sub-domain "<domain>"
[c] tạo dept/group mới (nếu domain đủ lớn ≥ 3 ki)
[d] archive global — không assign dept cụ thể

**ceo chọn a/b/c/d → tiếp tục intake:**
```

5. sau khi ceo chọn:
   - a → khởi động `agent-auto-create.md` (async — không block intake)
   - b/c → update `corp/org_chart.yaml` + `agents.md` (async)
   - d → ghi vào `brain/knowledge/global/`
   - mọi option → tiếp tục step 5 (intake không bị block)

output: gap_report ghi vào `corp/gaps/gap-<date>-<domain>.md`
sla: proposal gửi ceo < 5 phút | ceo response không bắt buộc để tiếp tục intake

---

### step 3b — web content path
trigger: classifier tag = web_content
agent: `web-crawler-agent`
actions:
- fetch url content (text + metadata)
- check: no malicious redirects, no injected scripts
- convert to markdown: quarantine/incoming/web/<slug>.md
- pass to content-validator-agent → step 4

sla: < 10 minutes per url

---

### step 3c — document path
trigger: classifier tag = document (pdf, docx, md)
agent: security grc (strix-agent) + `doc-parser-agent`
actions:
- strix-agent runs `system/security/vet_media_docs.py` (mandatory)
- fail → move to quarantine/rejected/ + blacklist
- pass → doc-parser-agent extract: title, date, author, full text
- structure as markdown: quarantine/incoming/documents/<name>.md
- pass to content-validator-agent → step 4

sla: < 15 minutes per document

---

### step 3d — image path
trigger: classifier tag = image
agent: security grc (strix-agent) + `content-validator-agent`
actions:
- strix-agent runs `system/security/vet_media_docs.py` (check magic bytes for steganography/polyglots)
- fail → move to quarantine/rejected/ + blacklist
- pass → stage to quarantine/incoming/images/<name>
- content-validator checks: verify safe imagery
- pass → quarantine/vetted/assets/ → step 5

sla: < 5 minutes

---

### step 4 — content validation (non-repo)
trigger: web-crawler, doc-parser, or direct text staging completes
agent: `content-validator-agent`
actions:
- score content quality (1-10): relevance, accuracy, safety, soul.md alignment
- score < 4 → rejected + log reason
- score ≥ 4 → pass → move to quarantine/vetted/ → step 5
- score ≥ 8 → flag for cosmic_memory (permanent retention candidate)

sla: < 10 minutes

---

### step 5 — route to destination
trigger: content in /vetted/ with pass status
agent: `ingest-router-agent`
actions:
- match classification tag to destination (see classification table in rules.md)
- move file from vetted/ to destination
- write receipt to destination agent
- update civ ticket to ingested
- confirm file exists at destination (verify)

destinations (paths relative to $omniclaw_root):
  repo/plugin        → plugins/  or  ecosystem/skills/
  web_content        → brain/knowledge/web/
  document           → brain/knowledge/documents/
  image              → assets/images/
  text               → brain/knowledge/text/
  config/rules doc   → corp/departments/<dept>/ or corp/rules/

post-routing handoff:
  → after file lands at destination, ingest-router must trigger
    knowledge-distribution-flow.md step d1 by writing a receipt to:
    subagents/mq/asset_library_ingest.md (for web/document/text)
    subagents/mq/registry_ingest.md     (for repo/plugin)
  → this receipt contains: { civ_ticket, content_type, destination_path, quality_score }

★ new v1.2 — post-route: skill-discovery-auto trigger
  if content_type = repo or plugin:
    → registry-manager-agent runs skill-discovery-auto.md:
       kiểm tra destination folder có skill.md chưa
       → nếu không: auto-create skill.md (skill creator ultra)
       → rebuild fast_index.json
    ref: ops/workflows/skill-discovery-auto.md

★ new v1.3 — post-route: neural link graph sync trigger
  tất cả content nạp vào thành công (repo, plugin, document):
    → archivist agent chạy `neural-link-sync.md`.
    → update `system_index.yaml` + `system_index_narrative.txt`.
    → đảm bảo omniclaw luôn biết vị trí của file/repo mới.

sla: < 5 minutes after content reaches /vetted/

---

### step 6 — quarantine cleanup ⚡ (mandatory — rule-quarantine-01)
trigger: step 5 hoàn tất (ticket status = ingested) hoặc ticket status = rejected
agent: `ingest-router-agent` (ngay sau khi ghi receipt xong)
actions:
- **ingested path:**
  - xóa toàn bộ: `quarantine/incoming/<type>/<civ_ticket>/`
  - xóa toàn bộ: `quarantine/vetted/<type>/<civ_ticket>/`
  - ⚠️ giữ lại: `quarantine/logs/intake_log.md` (chỉ log text, không phải repo)
  - ⚠️ giữ lại: `quarantine/vetted/<name>/_civ_analysis.md` (report nhỏ, không cần xóa)
- **rejected path:**
  - xóa toàn bộ: `quarantine/incoming/<type>/<civ_ticket>/`
  - chuyển `quarantine/vetted/<civ_ticket>/` → `quarantine/rejected/` (log nhỏ)
- **stale files (quá 7 ngày, không có ticket active):**
  - xóa toàn bộ file/folder trong `quarantine/incoming/` và `quarantine/vetted/`
- update ticket status: ingested → cleaned | rejected → cleaned_rejected

> ⚡ **rule-quarantine-01:** không được để repo nguyên trong quarantine sau khi đã ingested.
> quarantine chỉ là phòng tạm (staging area), không phải nơi lưu trữ lâu dài.
> vi phạm gây tích lũy hàng gb rác mỗi tuần, ảnh hưởng hiệu suất hệ thống.

sla: xóa ngay sau khi step 5 xác nhận file tồn tại tại destination

| dept | coordination |
|------|-------------|
| security grc | co-authority on all repo/plugin vetting (vet_repo.ps1) |
| registry & capability | destination for all repo/plugin after pass |
| asset & knowledge library | destination for web/document/text |
| operations | escalate civ backlog issues to scrum-master |
| monitoring & inspection | monitor civ ticket queue for sla breaches |

---

## escalation path

| issue | escalation |
|-------|-----------|
| unknown content type | intake-chief-agent manual review |
| warn repo (borderline) | intake-chief → strix-agent joint review |
| fail repo (critical threat) | strix-agent → l3 (ceo) if sophisticated attack |
| civ backlog > 5 tickets | intake-chief → coo |
| destination agent not acknowledging | ingest-router → monitoring dept |

---

### 🛡️ rule-civ-02: pending gate strict enforcement
trạng thái `pending` trong `pending_repos.md` là trạng thái chờ. 
**nghiêm cấm:**
1. clone thẳng repo đang ở trạng thái `pending` vào bất kỳ thư mục nào trên đĩa cứng (kể cả `quarantine`).
2. tự động chuyển trạng thái từ `pending` sang `active` mà không qua civ review.
3. ghi dữ liệu/metadata (như nội dung readme) của repo `pending` thẳng vào thư mục `brain/knowledge/repos` (hành vi này bypass hoàn toàn quá trình intaking).

**quy trình chuẩn cho rule-civ-02**:
1. ai/agent dùng `system/ops/scripts/pending_civ_classifier.py` để phân tích tĩnh (url, description) các repo `pending`. script tạo report `civ_pending_report_*.md` với 3 danh sách: approve, review, reject.
2. sếp (ceo / dept 20 intake chief) đọc report và quyết định.
3. nếu đồng ý với list approve, duyệt bằng script: `python system/ops/scripts/pending_civ_approve.py --auto-approve`. lệnh này chuyển repo từ `pending` sang `active`.
4. chỉ khi repo nằm trong `active_repos.md`, mới được phép kích hoạt `active_repos_pipeline.py` để thực hiện clone thật sự qua quy trình: `github → quarantine/incoming/repos → strix scan → brain/knowledge`.

> **Note enforcement (2026-03-27)**: `batch_repo_intake.py` mode `pending` và `all` đã bị block trên code (sẽ báo lỗi và sys.exit(1)). các chức năng tự động lấy nội dung từ github bắt buộc chỉ được dùng trên repo đã approved hoặc active. mọi script cũ bypass pipeline phải bị dừng chạy.

*(phiên bản tài liệu 1.5 - cập nhật ngày 2026-03-27)*
