---
description: How retrieval-master executes High-Speed RAG queries
---
# Workflow Bão Táp: FlashRAG Retrieval (Dept 18)

## Khởi đầu (The Prompt)
- Bất kỳ Agent nào cần tra cứu dữ liệu từ `PROCESSED_LIBRARY.md` hoặc các docs dài đều phải gửi Input vào `retrieval-master`.
- Ví dụ: `[Context_Request]: Cấu hình Redis trong file KI gốc ở đâu?`

## Giai đoạn 1: Lập Chỉ Mục Kép
- `retrieval-master` phân giải Prompt thành 2 mảnh: Semantics (Ngữ nghĩa) và Keywords (Từ vựng).
- Kích hoạt thuật toán Vectorizing. Nếu Database chưa nhúng (Embed), kích hoạt Semantic Search bằng `grep_search` kết hợp Pattern Recognition.

## Giai đoạn 2: Quét Song Song (Parallel Sweep)
- **Path A (Dành cho Logic / Tư duy):** Chạy lệnh Regex để túm lấy các file có `##` hoặc `---` liên quan đến "Redis".
- **Path B (Dành cho Trực diện):** Đọc nắp các dòng Context liền kề. Không load file trên 500 lines.

## Giai đoạn 3: Phản hồi Nén (Truncated Answer)
- Trích xuất ra duy nhất 1 đoạn Text (khoảng 300 từ) chứa trực tiếp Lệnh hoặc Logic gốc.
- Gửi ngược lại cho Node gọi: "Tôi không gửi file. Tôi gửi viên nén thông tin!".

> [!NOTE] FlashRAG Concept
> Tối ưu hóa API Call bằng cách giảm độ dày của Prompt. Mọi cục Text thừa thãi bị chặt xén hết trước khi gửi sang Reasoner.
