---
id: core-daemons-oer-vn
type: document
owner: SYSTEM
lang: vi
---

# 🏛️ Core Daemons — Quản Trị Hệ Sinh Thái OmniClaw

> **Thẩm Quyền:** CEO (LongLeo) | **Phiên Bản:** 5.0 | **Ngày:** 2026-04-11
> **Trạng Thái:** ĐANG HOẠT ĐỘNG — Tài liệu này thay thế tất cả định nghĩa thẩm quyền hệ sinh thái trước đây.

[**🇻🇳 View in English**](core_daemons_and_oer.md) | [**Quay về Docs**](../README-vn.md)

Tài liệu này định nghĩa **8 Core Daemons** của OmniClaw OS và **Pipeline Tự Động Zero-Trust** quản trị cách mà mọi Skill, Plugin, Agent và Workflow gia nhập hệ sinh thái.

---

## 1. 8 Trụ Cột Quản Trị (Master Hierarchy)

Để ngăn lạm quyền và vi phạm Zero-Trust, thẩm quyền hệ sinh thái được phân phối nghiêm ngặt qua 8 Agent chuyên biệt (Daemon) nằm trong 3 phòng ban kiến trúc riêng biệt (`system_daemons`, `system_health`, `system_security`):

| Node ID | Designation | Vai Trò Chung | Phòng Ban |
| :--- | :--- | :--- | :--- |
| **`oma_architect`**| OmniClaw Map Architect | Cấu Hình Hạ Tầng | `system_daemons` |
| **`oap_pipeline`** | Omnibus Assimilation | Điều Phối Pipeline | `system_daemons` |
| **`oer_registry`**| OmniClaw Ecosystem Registry | Quản Lý Đăng Ký | `system_daemons` |
| **`oiw_intake`** | OmniClaw Intake Worker | Thu Hoạch Viên | `system_daemons` |
| **`osf_warden`** | OmniClaw Sandbox Firewall | Tường Lửa Biên Giới | `system_security` |
| **`ohd_healer`** | OmniClaw Health Daemon | Bác Sĩ Hệ Thống | `system_health` |
| **`oa_academy`** | OmniClaw Academy | Kiểm Toán Thực Thi | `system_daemons` |
| **`obd_harbor`** | OmniClaw Bridge Daemon | Harbor Master / Quản Lý Cổng | `system_security` |

---

## 2. Ma Trận Thẩm Quyền (Ai Làm Gì)

| Chức Năng | OMA | OAP | OER | OIW | OSF | OHD | OA | OBD |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Lập Bản đồ Thiết bị & Định danh | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Phân Tuyến Triage | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Cập Nhật `REGISTRY.json` | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Clone Mã nguồn / Thu Hoạch | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ |
| Kiểm Duyệt Cách Ly (Biên giới) | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ | ❌ |
| Sửa File (Lint/Auto-Heal) | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ | ❌ |
| Phân tich logic & Tuyển dụng | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ❌ |
| Mở Cổng Localhost / Bridges | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |

> [!CAUTION]
> **Phân Vùng Zero-Trust**: Toàn bộ 8 Daemons đều là các điệp viên độc lập bị giới hạn bộ kỹ năng. Nếu một daemon cố tình chạy lệnh ngoài phân quyền của mình, Orchestrator sẽ kết liễu tiến trình ngay lập tức.

---

## 3. OBD Harbor – Thiết Quân Luật Vòng Ngoài

Kể từ Phiên bản 5.0, **OBD (OmniClaw Bridge Daemon)** được thăng cấp để xử lý tuyệt đối Vành đai cổng kết nối:
* **Không Tự Động:** Mọi server hay skill từ bên thứ 3 KHÔNG được phép tự ý chiếm cổng TCP/UDP nếu không được OBD quản lý.
* **Ép buộc `127.0.0.1`:** Việc mở toang `0.0.0.0` là hành động bất hợp pháp trừ khi sếp có lệnh mở API Gateway cho người ngoài truy cập.
* **Tích Hợp MCP:** Các module chạy ngầm qua `stdio` của Claude/Cursor cũng bị đưa vào danh sách kiểm soát mặt chữ trên Bảng Điều Khiển để sếp dễ dàng thống kê.

Chi tiết về thiết kế Trạm Gác (Bridge), tham khảo `ecosystem/bridges/README-vn.md`.

---

*Core Daemons v5.0 — OmniClaw Corp — 2026-04-11*
