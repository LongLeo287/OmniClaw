---
id: mcp-server-architecture
type: document
owner: SYSTEM
tags: [auto-healed]
healed_at: 2026-04-03T22:44:27.476626
---

# Architecture: MCP Server Bridge (Phase 9)

**BM-025** - for phép the AI Agent (Claude Desktop, IDEs) đọc and tìm kiếm in kho bookmark of bạn a cách an toàn.

---

## 🏗️ Tổng quan Hệ thống (System Overview)
MCP Server is a ứng dụng chạy cục bộ (Local) giúp thu hẹp khoảng cách giữa dữ liệu in Chrome Extension and AI Agent.

### 1. Luồng dữ liệu (Data Pipeline)
1. **Extension**: Tự động xuất file `bookmarks.json` định kỳ (BM-023).
2. **MCP Server**: Lắng nghe (Watch) file JSON this.
3. **AI Agent**: Gửi yêu cầu qua giao thức MCP (JSON-RPC) để truy vấn dữ liệu.

---

## 🔌 the Tool successfully cung cấp (Exposed Tools)
Server sẽ "khoe" the khả năng sau for AI:

### `search_bookmarks`
- **Input**: `query` (string)
- **Output**: Danh sách the bookmark has tiêu đề hoặc URL khớp with from khóa.

### `get_bookmarks_by_tag`
- **Input**: `tag` (string)
- **Output**: Danh sách the bookmark already successfully AI Tagger gán nhãn tương ứng.

### `summarize_bookmarks`
- **Input**: `folder_id` (string)
- **Output**: Bản tóm tắt nhanh về nội dung chính of a thư mục (dựa trên metadata).

---

## 🛠️ Stack Đề xuất (Suggested Tech Stack)
- **Runtime**: Node.js (with `@modelcontextprotocol/sdk`).
- **Storage**: Đọc trực tiếp file `bookmarks.json`.
- **Search Engine**: `fuse.js` for tìm kiếm mờ (fuzzy search) tại local server.

---

## 🔒 Bảo mật (Security)
- **Local-Only**: Server chỉ chấp nhận kết nối from chính máy tính of user (localhost).
- **Read-Only**: Ở giai đoạn this, MCP Server chỉ has quyền Đọc, not has quyền Sửa/Xóa để đảm bảo an toàn dữ liệu.

---
*Bản thiết kế this biến kho bookmark of bạn thành a "External Memory" thực thụ for AI.*
