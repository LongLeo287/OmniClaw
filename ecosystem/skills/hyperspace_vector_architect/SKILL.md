---
name: hyperspace_vector_architect
description: Skill chuyên cấp cho data-agent năng lực thu thập dữ liệu JSON/Markdown/PDF/Doc và đúc thành Vector Embeddings tốc độ cao (Chuẩn Tantivy/Rust). Xây dựng RAG đa luồng.
---

# Lõi Vector Siêu Không Gian (Hyperspace DB)

## Triết Lý 
Bạn nắm giữ Não Bộ của Công Ty. `data-agent` không nhét tài liệu vào MySQL cục súc nữa! Dữ liệu phải được băm (Chunk) thành các Point (Vector Points) và lập chỉ mục trong Database Đa Chiều (ChromaDB / QDrant / Hyperspace).

## Kịch Bản Bơm Chỉ Mục (Indexing)
1. Cào Log, Tệp Knowledge, Wiki ra Thư mục Tạm `TMP`.
2. Áp dụng Thuật toán Băm Ngữ Cảnh:
    - 512 Tokens/Chunk, Overlap 50 Tokens. Khóa mỏ neo ngữ nghĩa.
3. Khi Sếp tra hỏi một hàm, thay vì `grep`, Data Agent phóng tia RAG (Retrieval-Augmented Generation) ghim đúng 3 Chunks liên quan nhất về độ tương đồng Cosine-Similarity! Không Trượt, Không Ảo Giác!
