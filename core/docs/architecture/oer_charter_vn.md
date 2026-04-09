---
id: oer-charter-vn
type: document
owner: SYSTEM
lang: vi
---

# OER_CHARTER.md - OmniClaw Ecosystem Registry

**Thẩm Quyền:** CEO (LongLeo) | **Daemon Class:** Core Daemon #4
**Vận Hành Bởi:** Phòng 14 (`registry-manager-agent`)
**Hiệu Lực:** 2026-04-02

[**🇬🇧 View in English**](OER_CHARTER.md) | [**Quay về Docs**](../README-vn.md)

---

## OER là gì?

OER (OmniClaw Ecosystem Registry) là **Core Daemon Thứ Tư** của OmniClaw OS.
Trong khi OIW thu hoạch, OHD chữa lành và OA phán xét — **OER là Người Đăng Ký**.

OER là thực thể duy nhất được ủy quyền để:
- Cấp ID duy nhất cho tất cả Skill, Plugin, Agent và Workflow.
- Viết và duy trì `SKILL_REGISTRY.json` (bản kê khai hệ sinh thái).
- Di chuyển artifact đã duyệt vào thư mục `ecosystem/`.
- Giữ khóa duyệt Free-Pass tới `brain/knowledge/` để điều phối năng lực.

Không agent, daemon hay cán bộ nào khác có thể thực hiện các hành động này. Đây không phải khuyến nghị.

---

## Trách Nhiệm Cốt Lõi

### 1. Registry (Sổ Cái Sinh Thái)
OER sở hữu và vận hành nguồn sự thật duy nhất: `brain/registry/SKILL_REGISTRY.json`.
Mọi Skill, Plugin, Agent, Workflow đăng ký trong OmniClaw phải có ID do OER cấp trước khi Orchestrator có thể sử dụng.

**Định Dạng ID:**
| Loại Asset | Định Dạng ID | Ví Dụ |
|---|---|---|
| Skill | `SKILL-xxxx` | `SKILL-0104` |
| Plugin | `PLG-xxxx` | `PLG-0021` |
| Agent | `AGT-xxxx` | `AGT-0015` |
| Workflow | `WRK-xxxx` | `WRK-0008` |
| Department | `DEPT-xx` | `DEPT-22` |

### 2. Gate 0 — Kiểm Tra Trùng Lặp
Trước khi pipeline bất kỳ bắt đầu, OER phải xác nhận asset chưa tồn tại trong `SKILL_REGISTRY.json`. Nếu phát hiện trùng lặp, OER từ chối yêu cầu và trả lại ID asset hiện có cho người yêu cầu.

### 3. Intake Cuối — GIAI ĐOẠN 5
OER chỉ hành động **sau khi** TẤT CẢ điều kiện sau được đáp ứng:
- Có dấu `OHD_CLEAN` (chuỗi cung ứng đã xác minh, zero IOC)
- Có dấu `OA_APPROVED` (điểm >= 70, tất cả 8 Trụ Cột đã xem xét)
- `SKILL.md` hoặc manifest tương đương được Phòng 1 (Engineering) viết
- Nguồn trong `storage/vault/quarantine/` chờ chuyển giao cuối cùng

OER sau đó:
1. Tạo ID duy nhất cho asset.
2. Sao chép artifact từ `quarantine/` vào đúng tầng `ecosystem/`.
3. Cập nhật `SKILL_REGISTRY.json` với metadata đầy đủ.
4. Ghi receipt tới `telemetry/qa_receipts/gate_oer/`.
5. Thông báo Orchestrator với bản tóm tắt có cấu trúc.

---

## Pipeline Tự Động 5 Cổng

```
[TRIGGER: CEO / Orchestrator / Dept Lead]
        |
 [GATE 0: OER Kiểm Tra Trùng Lặp]  -----> TỪ CHỐI nếu đã tồn tại
        |
 [GIAI ĐOẠN 1: OIW — Thu Hoạch & Gitingest]
   - Clone repo vào storage/vault/quarantine/
   - Nén thành .md qua gitingest
        |
 [GIAI ĐOẠN 2: OHD — Vệ Sinh & Quét Chuỗi Cung Ứng]
   - Chạy: system/security/supply_chain_scan.ps1
   - Chạy: npm audit (JS), pip-audit (Python)
   - Đóng Dấu: OHD_CLEAN | Timestamp
        |        \___FAIL_-> OA Blacklist + Cảnh Báo
 [GIAI ĐOẠN 3: OA — Kiểm Toán & Tuân Thủ]
   - Phòng 9 (Strix): Điểm bảo mật >= 70
   - Phòng 12 (Legal): Kiểm tra License
   - Xem xét 8 Trụ Cột
   - Đóng Dấu: OA_APPROVED | Score
        |        \___FAIL_-> OA Faculty Report + Chặn
 [GIAI ĐOẠN 4: Phòng 1 (Engineering) — Chế Tạo]
   - Viết: SKILL.md / plugin manifest
   - Viết: unit tests
   - Dàn dựng trong: quarantine/ (hoàn thiện, sẵn sàng)
        |
 [GIAI ĐOẠN 5: OER — Đăng Ký]
   - Cấp ID duy nhất
   - Chuyển đến ecosystem/[tier]/
   - Cập nhật: SKILL_REGISTRY.json
   - Ghi: telemetry receipt
   - Thông báo: Orchestrator "REGISTERED"
```

---

## Kiểm Soát Truy Cập

| Thực Thể | Đọc `ecosystem/` | Ghi `ecosystem/` | Cập Nhật Registry |
|---|---|---|---|
| **OER (Phòng 14)** | CÓ | **CÓ (DUY NHẤT)** | **CÓ (DUY NHẤT)** |
| OA | CÓ (kiểm toán) | KHÔNG | KHÔNG |
| OHD | KHÔNG | KHÔNG | KHÔNG |
| OIW | KHÔNG | KHÔNG | KHÔNG |
| Orchestrator | CÓ | KHÔNG | KHÔNG |
| CTO / C-Suite | CÓ | KHÔNG | KHÔNG |
| Tất cả agent khác | KHÔNG | KHÔNG | KHÔNG |

---

## Mối Quan Hệ với Các Core Daemon Khác

| Daemon | Vai Trò | Giao cho OER | Nhận từ OER |
|---|---|---|---|
| OIW | Thu Hoạch Viên | Nguồn thô đã cách ly | Xác nhận slot mở |
| OHD | Bác Sĩ | Dấu `OHD_CLEAN` | Yêu cầu quét theo lịch |
| OA | Thẩm Phán | Dấu `OA_APPROVED` | Cập nhật Blacklist để thực thi |

---

*OER Charter v1.0 — OmniClaw Corp — 2026-04-02*
