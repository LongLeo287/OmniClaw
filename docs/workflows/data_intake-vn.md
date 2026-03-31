# Quy trình Nạp Dữ liệu OmniClaw (Data Intake Workflow)

## Chuỗi Chắt Lọc & Nạp Tri Thức (CIV Pipeline)

Hệ sinh thái OmniClaw vận hành dựa trên Kiến trúc Zero-Trust ngặt nghèo. Mọi mã nguồn từ bên ngoài, thư viện hay code do AI tự kéo về BẮT BUỘC phải đi qua trạm kiểm dịch và bị nhốt vào vùng `system/security/QUARANTINE_INCOMING` để dò quét. Hành vi `git clone` thẳng vào bán cầu não `/brain` hoặc `/ecosystem/plugins/` bị cấm hoàn toàn.

Để nạp kho tri thức mới một cách an toàn, bạn PHẢI tuân thủ chuỗi thao tác của Tổ Quản Lý Phân Loại Nội Dung (Dept 20 - CIV) và Tổ An Ninh Mạng (Dept 10 - Strix).

### Các bước Nạp Dữ liệu

1. **Nhắm Mục Tiêu:** Lựa chọn Link Github hoặc Repository cần ăn cắp, cào dữ liệu về máy.
2. **Khai Báo Trạm Chờ:** Paste link URL đó và alias đích đến nội bộ vào sổ Nam Tào điện tử nằm tại `storage/vault/DATA/Github.txt`.
3. **Thẩm Định Sâu (Deep Evaluation):** Mồi chài thuật toán chạy một vòng đánh giá xem kho dữ liệu kia cấu trúc như nào, có đáng để Nạp không.
   ```ps1
   python system/ops/scripts/omniclaw_deep_evaluator.py
   ```
4. **Nạp & Phân Tích (Active Pipeline Extraction):** Bấm nút chạy Mạch Nạp Chính. Script này tự bay ra Cloud cào toàn bộ Repo trên Github nhét thẳng vào khu Cách ly `QUARANTINE_INCOMING`. Tại đây nó trảm sạch file mã độc, quét API lộ lọt, strip mã nhị phân, vắt kiệt tri thức thành Dạng Đọc Rõ Rồi xếp gọn gàng vào bộ óc `/brain/corp` và `/brain/registry`.
   ```ps1
   python system/ops/scripts/active_repos_pipeline.py
   ```

### Giao Thức Bảo Mật Khi Nạp

* **Chặn Rò Rỉ Chìa Khóa:** Máy quét sẽ truy đuổi các tokens, mật khẩu, và biến `.env` bị hardcode lọt qua. Nếu bắt được cặn bã, tiến trình sẽ Đỏ lửa Báo Lỗi.
* **Bảo Tồn Hình Đọc:** Nó có khả năng biến tấu và tái sắp xếp File Markdown/Code thuần thành RAG Data Vector để bón cho Não LLM tiêu hóa dễ nhất.

### Băng chuyền Xử lý Kho Dữ liệu mã nguồn (Repo Analysis)

Để dọn dẹp và lấy tri thức từ mã nguồn thô của hàng trăm kho được kéo về, hãy chạy:

```ps1
python system/ops/scripts/omniclaw_repo_analyzer.py
```

* **Trích xuất:** Tạo ra báo cáo kiến thức siêu tốc gọn nhẹ `.md` lưu vào `brain/knowledge/processed_repos/`.
* **Dọn Dẹp (ARCHIVE):** Sau đó nó tự điều chu chuyển khuân vác toàn bộ mã nguồn nặng sang vùng lưu trữ Vĩnh Viễn `storage/vault/ARCHIVE/` để cách ly với Github, chống phình to Git.
* **Phân Loại (Knowledge Cleanup):** Cuối cùng, chạy `python system/ops/scripts/clean_knowledge.py` để phân loại các báo cáo AI/ML, kiến trúc và UI vào đúng chuyên mục trong `brain/knowledge/`.
