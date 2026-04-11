---
id: architect-handbook
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:18:50.047720
---

# Architect's Handbook: Smart Bookmark Manager

Chào mừng bạn to with tài liệu hướng dẫn kỹ thuật dành for lập trình viên. Tài liệu this giải thích the nguyên tắc thiết kế cốt lõi đứng sau Extension this.

## 🏗 Architecture: Domain-Driven Design (DDD)
Chúng ta tách biệt logic thành 4 lớp rõ rệt:
1. **Entities (`src/core/entities`)**: Chứa logic nghiệp vụ thuần túy (Example: `BookmarkEntity` xác định a bookmark hợp lệ).
2. **Repositories (`src/services/BookmarkRepository.js`)**: Lớp truy xuất dữ liệu (Abstraction layer). not quan tâm dữ liệu to from Chrome hay IndexedDB.
3. **Services (`src/services`)**: Xử lý the nghiệp vụ phức tạp liên quan to bên thứ 3 (Sync, AI, HTML Parsing).
4. **UI Components (`src/ui/components`)**: Hoàn toàn not chứa logic lưu trữ. Chỉ nhận dữ liệu and render.

## 🔌 Hệ thống Plugin
Extension sử dụng mô hình **Event-driven Hooks**. Bạn has thể đăng ký plugin new tại `PluginManager`:
- `onBeforeCreate`: Tiền xử lý dữ liệu.
- `onCreated`: Gán nhãn AI (Async).
- `onImportComplete`: Xử lý hàng loạt sau khi nạp dữ liệu.

## 💾 Luồng Dữ liệu (Data Flow)
`UI Event` -> `AppController` -> `BookmarkRepository` -> `Storage API` -> `SyncService` -> `Cloud`.

## 🎨 Design System
Hệ thống sử dụng **CSS Variable Tokens**. Mọi Changes: về màu sắc in Settings thực chất is Changes: giá trị of `--accent-primary` in `:root`.

## 🚀 Định hướng Scalability
Để hỗ trợ tree bookmark cực lớn:
- **Lazy Loading**: Chỉ nạp metadata khi cần thiết.
- **Virtual DOM**: (Sắp triển khai ở Phase 8) Để nâng cao hiệu năng cuộn.

---
*Tài liệu this successfully biên soạn bởi Senior Architect để làm kim chỉ nam for quá trình phát triển.*
