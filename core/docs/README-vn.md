---
id: readme-vn
type: document
owner: SYSTEM
language: vi
---

# 📚 OmniClaw — Tài Liệu Chính Thức

Chào mừng đến với **Tài Liệu Chính Thức của OmniClaw**. Thư mục này chứa các hướng dẫn dành cho con người, tổng quan kiến trúc hệ thống và hướng dẫn tương tác với hệ điều hành AI 21 phòng ban.

[**🇺🇸 View English Version**](README.md)

> 🔗 **OmniClaw Wiki:** Để xem thêm tài nguyên cộng đồng, hướng dẫn xử lý lỗi và thảo luận, hãy truy cập [**OmniClaw Official Wiki**](https://github.com/LongLeo287/OmniClaw/wiki).

---

## 🏛️ Kiến Trúc Hệ Thống
Tìm hiểu cách hệ thống đa tác nhân hoạt động, mở rộng và tự bảo vệ.

- [**Tổng Quan Hệ Thống**](architecture/system_overview.md) — Cấu trúc 21 phòng ban và thứ bậc thực thi.
- [**Kiến Trúc Plugin**](architecture/plugin_architecture.md) — Cách hệ sinh thái Plugin Zero-Trust 3 tầng được tích hợp.
- [**Các Nguyên Tắc Lõi**](architecture/CORE_PRINCIPLES.md) — Các nguyên tắc thiết kế bất biến của OmniClaw.
- [**OAP Architecture**](architecture/OAP_ARCHITECTURE-vn.md) — Kiến trúc Hệ thống Đa Tác Nhân (bản tiếng Việt).

## 🚀 Hướng Dẫn Sử Dụng
Khởi động nhanh và các lệnh dành cho nhà phát triển và vận hành hệ thống.

- [**Bắt Đầu**](usage_guides/getting_started.md) — Cài đặt và thiết lập ban đầu.
- [**Lệnh Agent & Kích Hoạt**](usage_guides/agent_commands.md) — Cách kích hoạt các tính năng OmniClaw.
- [**Hướng Dẫn Kích Hoạt**](usage_guides/ACTIVATION_GUIDE.md) — Bật/tắt các dịch vụ và plugin.
- [**Đóng Gói & Đồng Bộ Dữ Liệu**](workflows/data_packaging_sync.md) — Cách đóng gói, backup phiên làm việc và đẩy lên GitHub, HuggingFace, Google Drive an toàn.

## 🔄 Quy Trình & SOP
Các quy tắc và kịch bản chuẩn để duy trì tính toàn vẹn hệ thống.

- [**Tiếp Nhận Nội Dung (CIV Gate)**](workflows/data_intake.md) — Cách dữ liệu từ bên ngoài được kiểm duyệt trước khi vào bộ nhớ nội bộ.
- [**Quy Trình Dọn Dẹp Sâu**](workflows/deep_cleaner.md) — Quy trình vệ sinh tự động để đảm bảo tính toàn vẹn của hệ điều hành.
- [**OIW Daemon**](workflows/oiw_daemon.md) — Quy trình hoạt động của Daemon Tiếp Nhận.

## 📊 Kiểm Kê & Báo Cáo
- [**Kiểm Kê Hệ Thống**](OMNICLAW_SYSTEM_INVENTORY_2026-03-31.md) — Toàn bộ tài sản và cấu trúc hệ thống tính đến 31/03/2026.
- [**Báo Cáo Kiểm Toán Bảo Mật**](security-audit-report-March2026.md) — Kết quả kiểm toán bảo mật tháng 3/2026.

---
*Nếu bạn là AI đang truy cập thư mục này, hãy lưu ý rằng `docs/` dành cho nhà phát triển con người. Để xem các quy tắc thực thi nghiêm ngặt, hãy tham chiếu `brain/rules/` và `brain/shared-context/`.*
