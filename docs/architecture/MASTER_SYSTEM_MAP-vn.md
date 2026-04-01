---
id: AI-OS-SYSTEM-MAP-001
type: REFERENCE
domain: [system, architecture, meta]
dept: all
created: 2026-03-22
version: 1.0
authority: CEO
---

# Tập đoàn OmniClaw Corp — Sơ Đồ Hệ Thống Tổng Thể
## Bản Đồ Trí Tuệ Định Hướng Dành Cho Mọi Agents, Depts, Workflows, và Rules

> **BẮT BUỘC ĐỌC:** Bất kỳ AI Agent nào mới được nạp vào hệ thống bắt buộc phải đọc file này.
> Đây là bản đồ kiến trúc tối thượng của toàn bộ Tập đoàn OmniClaw.

---

## 1. LINH HỒN VÀ DANH TÍNH (IDENTITY)

| Trường (Field) | Giá Trị (Value) |
|-------|-------|
| Tên | OmniClaw Corp |
| Phiên bản | v2.4 (Chu kỳ 7) |
| CEO | LongLeo |
| Linh Hồn (Soul) | `OmniClaw/SOUL.md` |
| Quản Trị Hệ | `OmniClaw/GOVERNANCE.md` |
| Triết Lý | `OmniClaw/THESIS.md` (40 Trụ Cột) |

**OmniClaw Corp là gì?**
Một hệ thống AI Multi-Agent (Đa đặc vụ) siêu phức tạp được vận hành dưới cấu trúc của một Tập đoàn (Corporation) thực thụ.
Cốt lõi bao gồm CEO, Ban Giám Đốc (C-Suite), 21 Phòng Ban chuyên môn (Departments), 75+ AI Agents, các Chuỗi Workflow động, Kiến trúc Bộ nhớ đa tầng, các cổng phê duyệt (Gates) và hệ quản trị tự động 24/7.

---

## 2. CẤU TRÚC PHÒNG BAN (ORGANIZATIONAL STRUCTURE)

### Hệ Thống Cấp Bậc (Authority Tiers)
```
Tier 1: CEO (LongLeo) — Quyết định Tối cao (Final authority)
Tier 2: C-Suite (CTO, CMO, COO, CFO, CSO, CIO) — Điều hành chiến lược.
Tier 3: Trưởng Phòng (Dept Heads) — Quản lý tác vụ cấp phòng.
Tier 4: Chuyên viên (Workers) — Thực thi logic nghiệp vụ.
```

### 21 Phòng Ban Chuyên Trách

| # | Mã Phòng (Dept ID) | Agent Quản Lý (Head) | Cổng Duyệt (Gate) | Báo Cáo Cho |
|---|---------|-----------|------|------------|
| 1 | engineering | backend-architect-agent | GATE_QA | CTO |
| 2 | qa_testing | test-manager-agent | Là GATE_QA | CTO |
| 3 | it_infra | it-manager-agent | — | COO |
| 4 | marketing | growth-agent | GATE_CONTENT | CMO |
| 5 | support | channel-agent | GATE_CONTENT | COO |
| 6 | content_review | editor-agent | Là GATE_CONTENT | CMO |
| 7 | operations | scrum-master-agent | — | COO |
| 8 | hr_people | hr-manager-agent | — | COO |
| 9 | security_grc | strix-agent | Là GATE_SECURITY | CSO |
| 10 | finance | cost-manager-agent | — | CFO |
| 11 | strategy | product-manager-agent | — | CSO |
| 12 | legal | legal-agent | Là GATE_LEGAL | CSO |
| 13 | rd | rd-lead-agent | — | CTO |
| 14 | registry_capability | registry-manager-agent | — | CTO |
| 15 | asset_library | library-manager-agent | — | CIO |
| 16 | od_learning | org-architect-agent | — | CSO |
| 17 | planning_pmo | pmo-agent | — | COO |
| 18 | monitoring_inspection | monitor-chief-agent | — | COO |
| 19 | system_health | health-chief-agent | — | CTO |
| 20 | content_intake | intake-chief-agent | Là GATE_CIV | CTO |
| 21 | client_reception | project-intake-agent | — | COO (Ngủ Cứu) |

**Cốt Lõi Nhận Diện Dữ Liệu:** `corp/org_chart.yaml`

---

## 3. HỆ THỐNG CỔNG DUYỆT (GATES)

| Cổng (Gate) | Quản Lý (Owner) | Chặn Yêu Cầu (Blocks) | Kích Hoạt (Trigger) |
|------|-------|--------|---------|
| GATE_QA | qa_testing (test-manager) | Lỗi Engineering trước Prod | Tự động sau mỗi task kỹ thuật |
| GATE_CONTENT | content_review (editor) | Lỗi Logic/Content Marketing | Trước khi public truyền thông |
| GATE_SECURITY| security_grc (strix) | Lỗ hổng Plugins/Repos/Libraries | Khi kéo Nguồn Tự Động (CIV) |
| GATE_LEGAL | legal (legal-agent) | Rủi ro Hợp Đồng, Phân Bổ Dữ Liệu | Xác minh trên văn bản pháp lý |

**Hạng Mức PASS = Cấp Quyền + Lưu Hóa Đơn (Receipt) tại `telemetry/receipts/gate_<name>/`**
**Hạng Mức FAIL = Giam lỏng Output, Thông báo Worker làm lại**

---

## 4. QUY TRÌNH HẠT NHÂN (WORKFLOWS)

| Tên Workflow | Tệp Hướng Dẫn | Kích Hoạt | Giai Đoạn |
|----------|------|---------|--------|
| Corp Daily Cycle | `ops/workflows/corp-daily-cycle.md` | `omniclaw corp start` | 7 phases |
| Knowledge Ingest | `ops/workflows/knowledge-ingest.md` | `omniclaw ingest <source>` | 7 phases |
| Agent Auto-Create | `ops/workflows/agent-auto-create.md` | Vào Phase 5b của Ingest | 7 phases |
| Corp Learning Loop | `ops/workflows/corp-learning-loop.md` | `omniclaw corp retro` | Auto |
| Delivery Pipeline | `corp/sops/DELIVERY_PIPELINE.md` | Client chốt Proposal | 6 phases |

### Corp Daily Cycle (7 Nhịp Độ Hàng Ngày)
```
Phase 1: CEO Brief → Đọc KPI Hệ, Lịch, Sự cố từ CEO.
Phase 2: C-Suite Dispatch → Xuất chiến lược → Gán Goal → Ném vào blackboard.json.
Phase 3: Dept Dispatch → 21 Trưởng phòng phân mục tiêu xuống dàn Hậu Cần/Coder.
Phase 4: Execute → Workers chạy Scripts & Viết Biên Lai Hóa Đơn (Receipt).
Phase 5: Gate → Kích Hoạt GATE_QA / GATE_CONTENT / GATE_SECURITY.
Phase 6: Brief Back → Các Head tổng hợp Lịch Sử cho Daily_Briefs.
Phase 7: Reflect → Cognitive_Reflector duyệt & đề xuất Lỗ Hổng cho CEO.
```

---

## 5. KIẾN TRÚC BỘ NHỚ (5 TẦNG MEMORY ARCHITECTURE)

| Tầng Hạt (Layer) | Vị Trí (Path) | Sở Hữu (Owner) | Thời Hạn (Retention) | Nội Dung Cốt |
|-------|------|-------|-----------|---------|
| L1 Knowledge Base| `brain/knowledge/` | library-manager | VĨNH VIỄN (PERMANENT)| Nghiên cứu, Phân tích (72+ KIs) |
| L2 Global | `corp/memory/global/` | CEO | VĨNH VIỄN (PERMANENT)| Chiến lược gốc (Strategic logs)|
| L3 Dept | `corp/memory/departments/`| Trưởng Phòng | Đè Tự Động (Rolling 30D)| Sai sót Sprint, Patterns (Mẫu)|
| L4 Agent | `corp/memory/agents/` | AI Agent | Xóa 7-Ngày (7-day purge)| Tình trạng Task Cụ Thể |
| L5 Daily | `brain/memory/daily/` | archivist-agent | Xóa 7-Ngày (7-day purge)| Dump Phiên (Session logs) |

---

## 6. LỰC LƯỢNG NÒNG CỐT (AGENT ROSTER)

### Ban Giám Đốc (C-Suite)
| Agent | Vai Trò (Role) | Chuyên Trách (Dept) |
|-------|------|------|
| orchestrator_pro | Đại lý CEO ủy quyền | Toàn Quyền — Hệ Thống |
| backend-architect-agent | CTO / Trưởng Kỹ Thuật | engineering |
| growth-agent | CMO (Giám Đốc Marketing)| marketing |
| scrum-master-agent | COO (GĐ Vận Hành) | operations |
| cost-manager-agent | CFO (GĐ Tài Chính) | finance |
| product-manager-agent | CSO (Chiến Lược Đặc Nhiệm)| strategy |
| library-manager-agent | CIO (Trung Tâm Dữ Liệu) | asset_library |

### Đặc Vụ Tối Thượng (Specialist Agents)
| Agent | Chức Năng (Specialty) | Phòng Ban (Dept) |
|-------|-----------|------|
| notebooklm-agent (Nova)| Nhồi Dữ Liệu Sâu (Deep Intelligence) | rd |
| strix-agent | Cảnh Vệ An Ninh Đóng Mở (GATE_SECURITY)| security_grc |
| cognitive_reflector | Nắm Thóp Mẫu Hành Vi Tái Phát | strategy |
| knowledge_navigator | Siêu Cầu Đường Cấu Trúc File | asset_library |

**Hồ sơ Đầy đủ:** `brain/shared-context/AGENTS.md`

---

## 7. KIẾN TRÚC KỸ NĂNG (SKILL ARCHITECTURE)

**Trung Tâm Registry:** `brain/registry/SKILL_REGISTRY.json` (103+ Skills)
**Thư Mục Mã (Folder):** `ecosystem/skills/`

### Siêu Kỹ Năng Đa Thuộc Tính (Core Skills)
```
reasoning_engine     — Đặc quyền lý luận suy diễn trừu tượng.
context_manager      — Đặc quyền kết nối bộ nhớ xuyên phiên đè.
knowledge_enricher   — Đặc quyền nội suy liên kết vòng lập metadata.
diagnostics_engine   — Rà Lỗi Sâu Toàn Cầu.
```

---

## 8. NGUYÊN TẮC CON VỊT (FILE PATH RULES)

```
✅ HỢP LỆ — Toàn Cảnh Hoạt Động (OmniClaw workspace):
  corp/           → Tổ chức, Prompt gốc, Nhớ Cứng.
  brain/          → Nơi MỌI TRI THỨC VÀ KIẾN TRÚC ÁNH SÁNG RA ĐỜI.
  ops/            → Tool Đốt (Script, Cron).
  plugins/        → 3-Tier MCP Servers.
  telemetry/      → Logs, Biên Lai (Receipts).

🔒 MIỄN CHẠM — Lõi Trái Tim Máy Bơm Vận Hành:
  $USERPROFILE/.gemini/  → Antigravity memory.
  $USERPROFILE/.claude/  → Claude Code config.
  $USERPROFILE/.nullclaw/ → Mắt Thần Telegram config.

❌ NGHIÊM CẤM TẠO FILE NGOÀI TRỤC:
  Desktop, Documents, Temp.
```

---

**[OmniClaw Corp — System Map Phiên Bản Tiếng Việt — 2026-03]**
