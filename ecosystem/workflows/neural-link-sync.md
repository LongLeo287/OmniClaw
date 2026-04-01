# neural-link-sync.md — Knowledge Graph & Registry Synchronization
# Version: 1.1 | Updated: 2026-03-26
# Department: [DEPT-07] KNOWLEDGE & REGISTRY CAPABILITY (Archivist Agent)
# Mode: EVENT-DRIVEN (Chỉ quét khi có dữ liệu mới, tối ưu Quota/Context)
# Trigger: Cuối STEP 5 của `content-intake-flow.md` hoặc lệnh thủ công `omniclaw neural sync`

---

## 1. Mục Đích (Purpose)
Bản đồ Kiến trúc Toàn cầu của OmniClaw (Neural Link) không thể là một tệp chết. Bất cứ khi nào có Repo mới được nạp vào qua quá trình Intake, hoặc bị xóa đi, hệ thống phải cập nhật sơ đồ ngay lập tức để các Trợ lý AI (Antigravity, Claude Code) không bị mất phương hướng.

Quy trình này hướng dẫn `Archivist Agent` cập nhật Mạng Lưới Nhận Thức 3D thông qua Sổ Đăng Ký Tổng (Master Registry) và Não bộ Cốt lõi (LightRAG).

## 2. Quy Trình Cập Nhật (Sync Routine)

**BƯỚC 1: Xây Dựng Sổ Đăng Ký (Index Build)**
- Lệnh thực thi: `python "$OMNICLAW_ROOT\system\ops\scripts\registry_indexer.py"`
- Hành động: Quét toàn cục tất cả Repo, Plugin, Tool ở cả 2 Bán Cầu (Local Core & Remote Ecosystem). Cập nhật danh sách 300+ Entities vào `$OMNICLAW_ROOT\system\registry\SYSTEM_INDEX.yaml`.

**BƯỚC 2: Cấp Dữ Liệu Ngữ Nghĩa (Narrative Feed)**
- Lệnh thực thi: `python "$OMNICLAW_ROOT\system\ops\scripts\graph_feeder.py"`
- Hành động: Dịch tệp cấu hình tĩnh (YAML) thành văn bản ngữ nghĩa học (Narrative Text) để máy học RAG có thể lập bản đồ. Xuất ra tệp `SYSTEM_INDEX_NARRATIVE.txt`.

**BƯỚC 3: Dệt Mạng Lưới (Graph Injection)**
- Lệnh thực thi: Kích hoạt `LightRAG.insert` thông qua Script hoặc Adapter với đầu vào là tệp Narrative vừa sinh ra.
- Kết quả: Không gian 3D của hệ thống được dệt lại thành công. AI có thể truy vấn `Ai thuộc nhánh nào, Ai kết nối với Repo nào`.

## 3. Quy Tắc Truy Xuất Của Agent (Retrieval Rules)
Tất cả các Agent khi nhận Task từ CEO (Ví dụ: "Hãy mở tool X", "Kiểm tra repo Y"):
1. ĐỌC `SYSTEM_INDEX.yaml`: Để lấy tọa độ tuyệt đối mà không cần scan đĩa.
2. DÙNG `GitNexus MCP`: Nếu cần đào sâu xuống cây cấu trúc AST của repo đó.
3. CẤM: Lệnh `find` hoặc `ls -R` mù mờ gây rác bộ nhớ.

---
> "Biết mình biết ta, trăm trận trăm thắng. AI không biết mình đang ở đâu trong hệ thống thì chỉ là cỗ máy vô dụng." - Kiến trúc sư OmniClaw.

