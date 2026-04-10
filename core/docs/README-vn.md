---
id: docs_readme_vn
type: document
owner: SYSTEM
tags: [human-readable, index]
lang: vi
---

# 📚 OmniClaw - Trung Tâm Tài Liệu Hệ Thống

Chào mừng đến với **Tài Liệu Cốt Lõi OmniClaw**. Thư mục này đóng vai trò là thư viện trung tâm lưu trữ toàn bộ các hướng dẫn, tổng quan kiến trúc và giáo trình dành riêng cho Con Người để thấu hiểu **Hệ điều hành 8-Daemon V5.0**.

[**🇺🇸 View in English**](README.md)

> [!WARNING]
> Thư mục này được bảo trì đễ phục vụ độc quyền cho **Kỹ sư & Người dùng thật**. Nếu bạn là một Trí Tuệ Nhân Tạo (AI MLLM) đang cố gắng đọc các quy tắc chạy hệ thống, bạn sẽ không thu được thông tin kỹ thuật nào ở đây. Vui lòng di chuyển sang thư mục lệnh `brain/rules/`.

---

## 🏛️ Kiến Trúc Hệ Thống (Architecture)

Khám phá các bản thiết kế tổng thể và giới luật cấu trúc định hình nên hành vi tự trị tự động của OmniClaw.

- [**Tổng Quan Hệ Thống**](architecture/system_overview_vn.md) — Sự tiến hóa lên cấu trúc 8-Daemon V5.0.
- [**Nguyên Tắc Cốt Lõi**](architecture/core_principles_vn.md) — Bộ khung Zero-Config Memory và Chính sách Ngôn ngữ Toàn cầu.
- [**Bản Đồ Kế Thừa Hệ Thống**](architecture/master_system_map.md) — Luồng lưu chuyển dữ liệu gốc truyền thống.
- [**Kiến Trúc Băng Chuyền OAP**](architecture/oap_architecture_vn.md) — Cơ chế phân phối dữ liệu chi tiết của OAP.
- [**Sức mạnh 4 Daemons & OER**](architecture/core_daemons_and_oer_vn.md) — Quyền lực của hệ thống OIW, OHD, OA và OER.
- [**Hiến Chương Viện Hàn Lâm OA**](architecture/oa_charter_vn.md) — Tiêu chuẩn phân loại tự động Code Repositories.
- [**Quy Tắc Đăng ký OER**](architecture/oer_charter_vn.md) — Bộ tiêu chí khắc nghiệt để cấp phép các Kỹ năng mới.
- [**Kiến Trúc Plugins**](architecture/plugin_architecture_vn.md) — Cơ chế Sandbox 3 Lớp cách ly.
- [**Bản Đồ Kỹ Năng**](architecture/skills_map_vn.md) — Cuốn từ điển lưu danh 1,970+ Kỹ năng (Skils) gốc của Hệ điều hành.

## 🧭 Hướng Dẫn Sử Dụng (Usage Guides)

Sổ tay khởi động nhanh và thao tác công cụ thực chiến.

- [**Bắt Đầu Sử Dụng**](usage_guides/getting_started_vn.md) — Cài đặt và thiết lập môi trường lần đầu.
- [**Hướng Dẫn Kích Hoạt**](usage_guides/activation_guide.md) — Khai báo các Cổng Mạng (Port) cho các Modules ngoại sinh (LightRAG, Ollama).
- [**Lệnh Điều Khiển Agent**](usage_guides/agent_commands_vn.md) — Các cú pháp (Syntax) để điều phối Agents.
- [**Hướng Dẫn Figma MCP**](usage_guides/figma_mcp_usage.md) — Cách dùng Cầu nối giao thức MCP cho việc bóc tách thiết kế Figma.
- [**Thư Viện Khoa Học Dữ Liệu**](usage_guides/data_science_library.md) — Tích hợp hệ sinh thái phân tích Python.

## ⚙️ Quy Trình & SOP (Workflows)

Các Quy trình Chuẩn (Standard Operating Procedures) quy định cách máy móc xử lý dữ liệu thô và bảo vệ Vault.

- [**Máy Hút Bụi Sâu (Deep Cleaner)**](workflows/deep_cleaner_vn.md) — Cơ chế diệt virus, làm sạch các đoạn log Github tự động chống rò rỉ API.
- [**Tiếp Nhận Dữ Liệu (CIV Gate)**](workflows/data_intake_vn.md) — Các phương thức bảo mật để rà quét kho mã nguồn bên thứ 3.
- [**Đóng Gói & Đồng Bộ Dữ Liệu**](workflows/data_packaging_sync_vn.md) — Cách sao lưu bộ nhớ lên mây (HuggingFace/GDrive) cực an toàn.
- [**Quy trình Hoạt động OIW**](workflows/oiw_daemon_vn.md) — Bộ quét thông tin độc tài Harvester.

---
*Để cấu hình định tuyến cho Daemons nội tại của máy móc, vui lòng tham chiếu tuyệt đối tới Bản Tuyên ngôn Máy tại `brain/rules/_DIR_IDENTITY.md`.*
