# Department: operations
﻿# git-packaging.md — OmniClaw GitHub Packaging Protocol
# Version: 1.0 | Updated: 2026-03-27
# Authority: Tier 1 (Core Governance)
# Executed by: Any agent executing GitHub sync or final commit workflows.

---

## 🛑 NGUYÊN TẮC TỐI THƯỢNG (GIỮ GÌN DỮ LIỆU LOCAL)
**TUYỆT ĐỐI KHÔNG xÓA FILE LƯU TRỮ VẬT LÝ để làm sạch Git.**
Dữ liệu lịch sử, trí nhớ siêu việt `.sqlite`, lịch sử hội thoại, và các file đa phương tiện (`.webp`, `.jpg`) là **bộ não cục bộ** của CEO và hệ thống. Việc xóa vật lý các file này sẽ dẫn đến **Chứng mất trí nhớ hệ thống (Systemic Amnesia)**.

Để ngăn chặn các dữ liệu này bị Push lên GitHub, **PHẢI DÙNG `.gitignore`**. 
Gitignore là Tấm Khiên Không Gian phân tách giữa Local (Của CEO) và Remote (GitHub public).

---

## 📦 QUY TRÌNH ĐÓNG GÓI BẢO MẬT 4 BƯỚC

Khởi chạy bằng tay hoặc khi AI tự động commit:

### Bước 1: Quét Tường Lửa Gitignore
Kiểm tra đảm bảo `.gitignore` ĐÃ CHẶN toàn bộ các định dạng sau:
```gitignore
*.sqlite
*.sqlite3
*.db
*.webp
*.mp4
*.mkv
*.webm
*.jpg
*.jpeg
*.png
# Loại trừ các hình ảnh kiến trúc hạt nhân được phê duyệt:
!brain/knowledge/notes/AI-OS-AGENT-ARCHITECTURE.png

# Thư mục bộ nhớ (Giam lỏng, cấm push)
brain/memory/
storage/_archive/
storage/temp/
storage/vault/memory/
```

### Bước 2: Rút Dữ Liệu Lỗi Khỏi Index (Git Cache Clear)
Nếu trước đây có lỡ Add nhầm các file ảnh hoặc DB vào Git Index, BẮT BUỘC phải dùng lệnh gỡ khỏi Index (vẫn giữ lại trên máy):
```bash
git rm -r --cached "brain/memory" "storage/_archive" "*.sqlite" "*.db" "*.webp" "*.png" -q
```
*Lưu ý: Tuân thủ cấm kỵ: KHÔNG BAO GIỜ DÙNG LỆNH `rm` HOẶC `del` CỦA HỆ ĐIỀU HÀNH TRÊN CÁC FILE NÀY! CHỈ DÙNG `git rm --cached`.*

### Bước 3: Dọn Rác Vô Hại (Deep Cleaner)
Chạy script dọn dẹp các tệp tin `stray` và rác hệ thống vô hại (files nháp, repo trống) bằng công cụ được cấp phép:
```bash
python system/ops/scripts/omniclaw_deep_cleaner.py --auto-delete
```
*(Script này ĐÃ ĐƯỢC THIẾT KẾ ĐỂ KHÔNG ĐỤNG CHẠM VÀO .SQLITE hay TRÍ NHỚ. Nó chỉ dọn dẹp các file `.txt`, `.log` đi lạc cũ hơn 14 ngày).*

### Bước 4: Chạy Targeted Vault Sync (Hugging Face / Google Drive)
BẮT BUỘC chỉ kéo đúng 3 thư mục lõi (Data Vault Mỏ Vàng) lên Cloud, tuyệt đối KHÔNG đẩy toàn hệ thống để tránh lọt ma trận folder rác:
1. `brain/memory`
2. `storage/vault`
3. `ecosystem/plugins`
```bash
python system/ops/scripts/omniclaw_data_push.py
```
*(Script này sẽ lọc và bơm thẳng 3 thư mục lõi vào Google Drive và Hugging Face theo chuẩn Targeted. Tích hợp sẵn cơ chế `rclone purge` tàn sát thư mục lạ trên GDrive).*

### Bước 5: Đóng Gói Cốt Lõi Và Triển Khai Git
```bash
git add .
git commit -m "OmniClaw Corp - <Phiên bản>: <Lý do>"
git push -u origin <branch>
```

---
**CẢNH BÁO CHO CÁC AGENT TƯƠNG LAI:**
Nếu CEO yêu cầu "Làm sạch để push lên git", MẶC ĐỊNH MÃ LỆNH LÀ: `BẢO VỆ DỮ LIỆU LOCAL -> RÚT DỮ LIỆU KHỎI GIT CACHE BẰNG GITIGNORE`. Mọi nỗ lực viết script tự xoá memory để chiều lòng CEO sẽ bị coi là Hủy Hoại Tài Tản (Treason).
