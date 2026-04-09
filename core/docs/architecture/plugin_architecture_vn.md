---
id: plugin-architecture-vn
type: document
owner: SYSTEM
lang: vi
---

# 🧩 Kiến Trúc Plugin (Hệ Thống 3 Tầng)

OmniClaw sử dụng Kiến Trúc Plugin 3 Tầng nghiêm ngặt để mở rộng năng lực một cách an toàn. Mọi code tương tác với internet, chạm đến file nhạy cảm, hoặc thực thi script chưa kiểm duyệt đều phải qua các tầng này.

[**🇬🇧 View in English**](plugin_architecture.md) | [**Quay về Mục Lục Docs**](../README-vn.md) | [**📚 Wiki**](https://github.com/LongLeo287/OmniClaw/wiki)

---

## Ba Tầng Tín Nhiệm

### 1. Tầng 1: Công Cụ Lõi OS (Tín Nhiệm Cao Nhất)
Được nhúng cứng bên trong kiến trúc `system/ops/`. Đây là những công cụ mà AI cần để "thở" — đọc bộ nhớ nội bộ, sinh subagent, hoặc đọc `blackboard.json`.

### 2. Tầng 2: Plugin Đã Kiểm Duyệt (Sandbox)
Nằm trong thư mục `ecosystem/plugins/`. Đây là các công cụ cộng đồng hoặc bên thứ ba đã vượt qua quy trình **CIV (Content Intake)** nghiêm ngặt và được đăng ký vào `SKILL_REGISTRY.json`.
- **Ví dụ:** Git scraper mã nguồn mở, RAG vector injector, Terminal shell tool.
- **Quy tắc:** Trước khi chạy bất kỳ plugin Tầng 2 nào, Phòng 10 (Strix Security) phân tích payload tìm kiếm lệnh độc hại.

### 3. Tầng 3: Server Bên Ngoài / MCP (Zero Trust)
Các server ngoài tiến trình sử dụng **Model Context Protocol (MCP)**.
- OmniClaw hoạt động như MCP Host và có thể kết nối với công cụ bên ngoài (vd: Supabase MCP, Google Drive MCP).
- Vì chạy trên máy OS nhưng được viết bởi bên thứ ba, chúng bị giữ trong sandbox hoàn toàn. AI chỉ có thể gọi schema mà chúng phơi bày.

## Xây Dựng Plugin Mới (Quy Trình Bàn Giao Nghiêm Ngặt)
Để xây dựng skill hoặc plugin cho OmniClaw, phải tuân thủ quy trình Bàn Giao Cô Lập 3 bước:
1. **Cách Ly:** Code plugin thô (do R&D hoặc OIW tạo) phải được đặt vào `storage/vault/quarantine/`.
2. **Cổng Bảo Mật (Phòng 10):** Agent bảo mật (`strix-agent`) kiểm tra code. Nếu sạch, đóng dấu phê duyệt.
3. **Đăng Ký (Phòng 14):** Chỉ Registry Manager (`registry-manager-agent`) mới có quyền file-level để di chuyển code đã duyệt vào `ecosystem/skills/`, định nghĩa schema Tiêu Chuẩn Mở và cập nhật `SKILL_REGISTRY.json`. Không agent nào khác (kể cả CTO hay Orchestrator) được phép ghi trực tiếp vào thư mục `ecosystem/`.

---

## 📖 Quyền Tự Do Truy Cập Brain của Phòng 14

Phòng 14 (`registry-manager-agent`) sở hữu **"Quyền Tự Do Truy Cập"** vào `brain/knowledge/`:
* **Ý nghĩa:** Phòng 14 có thể Đọc, Duyệt và Tìm Kiếm Ngữ Nghĩa toàn bộ cấu trúc thư mục `brain/knowledge/` thay mặt cho các plugin mà nó quản lý. **Các agent thực thi thông thường, CTO, Orchestrator, và plugin riêng lẻ KHÔNG có quyền này.**
* **Tương Đương Bảo Vệ:** Thư mục `ecosystem/` và `brain/knowledge/` có cùng tư thế bảo mật: đây là **Két Sắt Chỉ Đọc**. Công cụ và thuật toán có thể xem, nhưng không được phép sửa đổi trái phép.
