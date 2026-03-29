# ⚖️ RULES (Dept 18: Asset & Knowledge Library)

> Bộ luật nội bộ dành cho Thư viện Tài Sản.

1. **RULE 01: NO BULK READ** 🚫
   Các Agent (bao gồm Tier 1) tuyệt đối KHÔNG ĐƯỢC tự đọc toàn bộ file `PROCESSED_LIBRARY.md` hoặc các file dữ liệu thô lớn hơn 500 lines. Mọi truy vấn phải thông qua `retrieval-master`.

2. **RULE 02: HIGH-SPEED RAG MANDATE** ⚡
   `retrieval-master` bắt buộc phải sử dụng biểu thức Vector/Keyword song song theo nguyên lý FlashRAG. Không quét tuyến tính. Đầu ra phải giới hạn trong 200 - 300 words có tinh suất cao nhất.

3. **RULE 03: INDEX FIRST, RETRIEVE LATER** 🗃️
   Toàn bộ mã nguồn mới đẩy vào nhánh ARCHIVE phải được `knowledge-curator-agent` và `asset-tracker-agent` gán chunk tagging ngay lập tức trước khi phân quyền truy cập.
