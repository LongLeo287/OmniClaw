---
description: Xóa rác và file nhị phân sau khi Vetting Repo, thu gọn thành Markdown Framework.
trigger: "Vetting Complete Event from OA"
daemon: "OHD / OA"
script: "core/ops/scripts/ghost_sweep.py"
---

# Repo Cleanup Protocol (Ghost Sweep)

Quy định xử lý (Data Retention) bắt buộc cho tất cả các Repo sau khi hoàn tất quy trình Vetting. Việc dọn rác giúp chống vi phạm RAM memory, chống token bloat cho LLM, và tối ưu kiến trúc OMA Map.

## 1. Trách nhiệm (Responsibilities)
- **OA (OmniAgent Academy) / Tác nhân phân tích:** Sau khi đọc xong mã nguồn và viết bài rút trích `VETTING_REPORT.md` thành công, bắt buộc gọi script dọn dẹp.
- **OHD (Omni Health Daemon):** Có trách nhiệm check logs. Nếu phát hiện Repo nào trong `CIV/` hoặc `frameworks/` đã có `VETTING_REPORT.md` nhưng dung lượng vẫn còn to (>10MB), có quyền cưỡng chế gọi lại Script Ghost Sweep để dọn rác.

## 2. Tiêu chuẩn dọn dẹp (Retention Rules)
- Hành động: **"Lấy Não Bỏ Xác"**
- Xóa bỏ **TẤT CẢ** các files ngoại trừ whitelist: `.md`, `.txt`
- Xóa bỏ **vĩnh viễn** các thư mục mang tính Build/Source code: `.git`, `node_modules`, `__pycache__`, `assets`, `images`, `build`, v.v.

## 3. Cách thực thi
// turbo
Chạy script chuyên dụng trên target path:
```bash
python core/ops/scripts/ghost_sweep.py --target "path/to/repo"
```
