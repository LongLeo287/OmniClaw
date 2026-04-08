---
id: data-intake-vn
type: document
owner: SYSTEM
lang: vi
---

# Quy Trình Tiếp Nhận Dữ Liệu OmniClaw

## Pipeline Tiếp Nhận & Kiểm Duyệt Nội Dung (CIV)

Hệ sinh thái OmniClaw vận hành theo Kiến Trúc Zero-Trust nghiêm ngặt. Mọi code bên thứ ba, repository, hoặc plugin bên ngoài PHẢI được sandbox hoàn toàn trong `system/security/QUARANTINE_INCOMING` và trải qua quét tỉ mỉ trước khi thực thi. Việc `git clone` thô vào `/brain` hoặc `/ecosystem/plugins/` bị cấm về mặt kiến trúc và bị chặn tự nhiên. Thay vào đó, bạn PHẢI dùng `gitingest` hoặc `gitnexus` để trích xuất codebase repository thành một file `.md` hoặc `.txt` nhẹ, trước khi commit vào cơ sở tri thức.

Để tiếp nhận dữ liệu mới một cách an toàn, bạn PHẢI dùng pipeline CIV do Phòng 20 (CIV) và Phòng 10 (Strix) quản lý.

[**🇬🇧 View in English**](data_intake.md) | [**Quay về Mục Lục Docs**](../README-vn.md)

### Các Bước Thực Thi Pipeline

1. **Xác Định Mục Tiêu:** Xác định URL mục tiêu hoặc repository bạn muốn đưa vào corpus OmniClaw.
2. **Đăng Ký:** Thêm URL mục tiêu và bí danh thư mục nội bộ vào danh sách theo dõi `storage/vault/DATA/Github.txt`.
3. **Đánh Giá Sâu:** Chạy bộ đánh giá thông minh để phân tích và đánh giá mức độ liên quan cấu trúc của repository.
   ```ps1
   python system/ops/scripts/omniclaw_deep_evaluator.py
   ```
4. **Trích Xuất Pipeline Chủ Động:** Thực thi pipeline tiếp nhận chính. Script này sẽ kéo repository vào không gian `/system/security/QUARANTINE_INCOMING`, quét malware và secret, loại bỏ file không cần thiết, và cuối cùng di chuyển dữ liệu đã được vệ sinh vào `/brain/corp` hoặc `/brain/registry`.
   ```ps1
   python system/ops/scripts/active_repos_pipeline.py
   ```

### Thực Thi Kiến Trúc

* **Không API Keys Cứng Coded:** Pipeline quét chủ động tìm key, token, hoặc file `.env` đã commit. Nếu phát hiện, payload bị loại bỏ ngay lập tức.
* **Bảo Tồn Định Dạng:** Pipeline sẽ chuyển đổi tài liệu Markdown và code sang định dạng dễ phân tích cho LLM và RAG engine.

### Pipeline Xử Lý Repository (Phân Tích Repo)

Để dọn dẹp và chắt lọc kiến thức từ source code thô của hàng trăm repository được clone, chạy:

```ps1
python system/ops/scripts/omniclaw_repo_analyzer.py
```

* **Trích Xuất:** Tạo báo cáo tri thức `.md` nhẹ lưu tại `brain/knowledge/processed_repos/`.
* **Dọn Dẹp (ARCHIVE):** Tự động chuyển source code nặng sang vault lưu trữ vĩnh viễn `storage/vault/ARCHIVE/` để cô lập khỏi Github và ngăn repository phình to.
* **Phân Loại (Knowledge Cleanup):** Cuối cùng, chạy `python system/ops/scripts/clean_knowledge.py` để sắp xếp các báo cáo AI/ML, kiến trúc và UI vào các danh mục tương ứng trong `brain/knowledge/`.
