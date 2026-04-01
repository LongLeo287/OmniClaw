# 🏛️ Tứ Trụ Daemon & OER — Quản Trị Hệ Sinh Thái OmniClaw

> **Thẩm Quyền:** CEO (LongLeo) | **Phiên bản:** 1.0 | **Ngày:** 2026-04-02
> **Trạng thái:** HIỆU LỰC — Tài liệu này thay thế mọi định nghĩa quyền hạn hệ sinh thái trước đây.

[**🇬🇧 English Version**](CORE_DAEMONS_AND_OER.md) | [**Quay lại Mục Lục**](../README-vn.md)

Tài liệu này định nghĩa **4 Core Daemon** của OmniClaw OS và **Pipeline 5-Gate Tự Động** — quy định cách thức mọi Skill, Plugin, Agent và Workflow được nhập vào hệ sinh thái.

---

## Tại Sao Tài Liệu Này Ra Đời?

Trước khi OER được thành lập, quyền hạn hệ sinh thái bị phân mảnh ở 4 nơi:

| Vấn Đề | Thực Thể | Lỗi |
|---|---|---|
| OIW hút data nhưng cũng tự ý đăng ký Agent mới | OIW | **Vượt quyền** |
| Dept 14 nắm Registry nhưng không có danh xưng chuẩn | Dept 14 | **Vô hình trong Prompt** |
| OA xét xử kiến trúc nhưng OEA (đề xuất, sau loại bỏ) cũng xét xử | OEA | **Trùng lặp quyền hạn** |
| Orchestrator/CTO tự ghi file vào `ecosystem/` | C-Suite | **Phá vỡ Zero-Trust** |

**Giải pháp:** Khai sinh **OER (OmniClaw Ecosystem Registry)** làm Core Daemon thứ 4, phân chia toàn bộ trách nhiệm theo Ma Trận Phân Quyền Tứ Trụ — không chồng chéo.

---

## 4 Core Daemon

| Daemon | Tên Đầy Đủ | Phòng Ban Vận Hành | Vai Trò Chính |
|---|---|---|---|
| **OIW** | OmniClaw Intake Workflow | Dept 20 (`intake-chief-agent`) | Thợ Săn — hút & ép khô dữ liệu ngoài |
| **OHD** | OmniClaw Health Daemon | Dept 19 (`health-chief-agent`) | Bác Sĩ — khử khuẩn & duy trì sức khỏe hệ thống |
| **OA** | OmniClaw Academy | OA Faculty + Dept 9/12 | Quan Tòa — thực thi 8 Trụ Cột, kiểm toán tuân thủ |
| **OER** | OmniClaw Ecosystem Registry | Dept 14 (`registry-manager-agent`) | Cục Đăng Kiểm — thẩm quyền duy nhất về nhập kho hệ sinh thái |

---

## Ma Trận Phân Quyền (Ai Làm Gì)

| Chức Năng | OIW | OHD | OA | OER |
|---|---|---|---|---|
| Hút Repo, Gitingest | ✅ | ❌ | ❌ | ❌ |
| Đặt Repo vào Quarantine | ✅ | ❌ | ❌ | ❌ |
| **Đăng ký Agent/Dept mới** | ❌ 🔁 | ❌ | ❌ | ✅ |
| Quét Virus, IOC Supply Chain | ❌ | ✅ | ❌ | ❌ |
| Dọn rác npm, cache, `__pycache__` | ❌ | ✅ | ❌ | ❌ |
| Báo cáo sức khỏe định kỳ | ❌ | ✅ | ❌ | ❌ |
| Xét xử vi phạm Kiến trúc | ❌ | ❌ | ✅ | ❌ |
| Kiểm toán Ecosystem plugins | ❌ | ❌ | ✅ | ❌ |
| **Ghi file vào `ecosystem/`** | ❌ | ❌ | ❌ | ✅ |
| **Cập nhật `SKILL_REGISTRY.json`** | ❌ | ❌ | ❌ | ✅ |
| **Cấp ID, Biển số Tool/Plugin** | ❌ | ❌ | ❌ | ✅ |
| **Free-Pass vào `brain/knowledge`** | ❌ | ❌ | ❌ | ✅ |
| Viết luật, 8 Trụ Cột OA | ❌ | ❌ | ✅ | ❌ |

> [!IMPORTANT]
> **🔁 Thay đổi cốt lõi:** OIW mất toàn bộ quyền Đăng ký. Toàn bộ quyền Đăng kiểm (Agent, Dept, Skill, Plugin, Workflow) chuyển sang OER. Không thực thể nào khác được phép ghi vào `ecosystem/` hay sửa `SKILL_REGISTRY.json`.

---

## Pipeline 5-Gate Tự Động

```
   ┌─────────────────────────────────────────────────────────────────────────┐
   │                 PIPELINE NHẬP KHO HỆ SINH THÁI OMNICLAW                │
   └─────────────────────────────────────────────────────────────────────────┘

[KHỞI ĐỘNG]
CEO / Orchestrator / Trưởng Phòng yêu cầu:
  "Cần 1 Skill mới / Plugin / Agent"
         │
         ▼
  ┌─────────────┐
  │ GATE 0      │  Kiểm tra: Đã có trong SKILL_REGISTRY.json chưa?
  │ OER Kiểm   │  → Có rồi: Từ chối, trả về ID đã tồn tại
  └──────┬──────┘  → Chưa có: Tiếp tục
         │
         ▼
  ┌─────────────┐
  │ PHASE 1     │  OIW (Dept 20) hút source code về
  │ THU HOẠCH  │  gitingest → ép thành .md / .txt
  │             │  Đặt vào: storage/vault/quarantine/
  └──────┬──────┘
         │
         ▼
  ┌─────────────┐
  │ PHASE 2     │  OHD (Dept 19) chạy supply_chain_scan.ps1
  │ KHỬ TRÙNG  │  Kiểm tra IOC, virus, .map leak, C2 connection
  │             │  → THẤT BẠI: Gửi bản án OA, ném vào BLACKLIST
  └──────┬──────┘  → THÀNH CÔNG: Đóng dấu "OHD_CLEAN" + timestamp
         │
         ▼
  ┌─────────────┐
  │ PHASE 3     │  OA (Viện Hàn Lâm) xét xử 8 Trụ Cột
  │ KIỂM TOÁN  │  Dept 9 (Strix): Điểm bảo mật >= 70
  │             │  Dept 12 (Legal): Kiểm tra bản quyền
  │             │  → THẤT BẠI: Block + Bản Án OA Faculty Report
  └──────┬──────┘  → THÀNH CÔNG: Đóng dấu "OA_APPROVED" + điểm
         │
         ▼
  ┌─────────────┐
  │ PHASE 4     │  Dept 1 (Engineering): Build & Integration test
  │ RÈN LUYỆN  │  Viết SKILL.md đúng chuẩn Schema
  │             │  Viết unit test cơ bản
  └──────┬──────┘  → THẤT BẠI: Trả về Dept 1 để sửa
         │
         ▼
  ┌─────────────┐
  │ PHASE 5     │  OER (Dept 14 - registry-manager-agent) tiếp nhận
  │ ĐĂNG KÝ    │  Cấp ID duy nhất (SKILL-xxxx / PLG-xxxx / AGT-xxxx)
  │             │  Ghi vào SKILL_REGISTRY.json
  │             │  Cất vào ecosystem/ đúng tầng
  └──────┬──────┘  Báo cáo lại Orchestrator/CEO: "ĐÃ ĐĂNG KÝ ✅"
         │
         ▼
  ┌─────────────┐
  │ TELEMETRY   │  Ghi Biên Lai tại telemetry/qa_receipts/gate_oer/
  │ LOG         │  + Cập nhật brain/knowledge/repos/ (nếu là repo mới)
  └─────────────┘
```

---

## Các Phòng Ban & Agent Tham Gia Pipeline OER

| Daemon / Dept | Đóng Góp Vào OER | Agent Chủ Chốt |
|---|---|---|
| **OIW** | Cung cấp nguồn nguyên liệu thô đã cách ly | `intake-chief-agent` (Dept 20) |
| **OHD** | Phát chứng chỉ "Sạch Khuẩn" | `health-chief-agent` (Dept 19) |
| **OA** | Phát dấu "Hợp Hiến" 8 Trụ Cột | `strix-agent` + `legal-agent` (Dept 9, 12) |
| **Dept 1** | Rèn code thành SKILL.md chuẩn Schema | `backend-architect-agent` |
| **Dept 13** | R&D đề xuất các skill cần thiết | `rd-lead-agent` |
| **Dept 15** | Mở cửa `brain/knowledge` khi OER cần đọc | `library-manager-agent` |
| **OER (Dept 14)** | **Đầu não cuối cùng** — cấp ID, nhập kho | `registry-manager-agent` |

---

## Các File Liên Quan

| File | Mục Đích |
|---|---|
| [`OER_CHARTER.md`](OER_CHARTER.md) | Hiến Chương OER đầy đủ (Tiếng Anh) |
| [`OER_CHARTER-vn.md`](OER_CHARTER-vn.md) | Hiến Chương OER đầy đủ (Tiếng Việt) |
| [`MASTER_SYSTEM_MAP-vn.md`](MASTER_SYSTEM_MAP-vn.md) | Sơ đồ hệ thống tổng thể với Ma Trận Tứ Trụ |
| [`OA_CHARTER-vn.md`](OA_CHARTER-vn.md) | 8 Trụ Cột Quân Luật của OA |
| [`../brain/rules/OIW_INTAKE_STRICT_RULE.md`](../brain/rules/OIW_INTAKE_STRICT_RULE.md) | Luật OIW (gồm Rule 20.4: ZERO Registration Rights) |
| [`../brain/rules/GLOBAL_BLACKLIST.md`](../brain/rules/GLOBAL_BLACKLIST.md) | Danh sách đen IOC hiện hành (OHD thực thi) |
| [`../system/ops/scripts/oer_register.py`](../system/ops/scripts/oer_register.py) | Script tự động hoá Phase 5 |
| [`../system/security/supply_chain_scan.ps1`](../system/security/supply_chain_scan.ps1) | Script quét OHD Phase 2 |
| [`../system/security/strix_policy.yaml`](../system/security/strix_policy.yaml) | Chính sách chấm điểm OA Phase 3 (v2.0) |

---

*Tứ Trụ Daemon OmniClaw & OER — v1.0 — 2026-04-02*
