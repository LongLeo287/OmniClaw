# 📚 OmniClaw Corp - Tài Liệu Chính Thức

Chào mừng bạn đến với **Tài liệu chính thức của hệ thống OmniClaw**. Thư mục này chứa các cẩm nang hướng dẫn sử dụng, tổng quan kiến trúc, và quy trình do con người đọc được để hiểu cách thức vận hành hệ điều hành AI 21 phòng ban.

[**🇬🇧 Read in English**](README.md)

> 🔗 **OmniClaw Wiki:** Để xem thêm tài nguyên cộng đồng, hỏi đáp và thảo luận mở rộng, vui lòng truy cập [**OmniClaw Official Wiki**](https://github.com/LongLeo287/OmniClaw/wiki).

---

## 🏛️ Kiến Trúc Hệ Thống (Architecture)
Tìm hiểu các đặc vụ AI phối hợp, mở rộng đa luồng, và cơ chế bảo mật chéo.

- [**Tổng Quan Hệ Thống (System Overview)**](architecture/system_overview-vn.md) — Cấu trúc 21 phòng ban và phân cấp ra lệnh.
- [**Cấu Trúc Plugin (Plugin Architecture)**](architecture/plugin_architecture-vn.md) — Cách hệ sinh thái 3 tầng Plugin Zero-Trust hoạt động.

## 🚀 Cẩm Nang Sử Dụng (Usage Guides)
Hướng dẫn cấp tốc và các tập lệnh dành cho nhà lập trình (Developer) & nhà quản trị hệ thống (System Operator).

- [**Getting Started**](usage_guides/getting_started-vn.md): Cài đặt và thiết lập.
- [**Agent Commands & Invocations**](usage_guides/agent_commands-vn.md): Lệnh điều khiển hệ thống.
- [**Data Packaging & Sync Process**](workflows/data_packaging_sync-vn.md): Quy trình đóng gói, sao lưu phiên làm việc, và đồng bộ dữ liệu Github, HuggingFace an toàn.

## 🔄 Quy Trình & SOPs
Các tiêu chuẩn và kịch bản dùng để duy trì tính toàn vẹn của OmniClaw.

- [**Kiểm Duyệt Nạp Dữ Liệu (CIV Gate)**](workflows/data_intake-vn.md) — Cách dữ liệu RAG, repos từ bên ngoài bị rà quét trước khi đi vào Local Memory.
- [**Dọn Dẹp Triệt Để (Deep Cleaner)**](workflows/deep_cleaner-vn.md) — Đường ống tự động làm sạch và vệ sinh hệ thống định kỳ.

---
*Ghi chú cho AI: Nếu bạn là thực thể AI đang truy cập thư mục này, lưu ý rằng `docs/` được viết để Người thao tác (Human) đọc. Để trích xuất các quy tắc gốc, hãy tải bộ nhớ từ `brain/rules/` và `brain/shared-context/` thay thế.*
