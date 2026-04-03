# department: operations
﻿# git-packaging.md — omniclaw github packaging protocol
# version: 1.0 | updated: 2026-03-27
# authority: tier 1 (core governance)
# executed by: any agent executing github sync or final commit workflows.

---

## 🛑 nguyên tắc tối thượng (giữ gìn dữ liệu local)
**tuyệt đối không xóa file lưu trữ vật lý để làm sạch git.**
dữ liệu lịch sử, trí nhớ siêu việt `.sqlite`, lịch sử hội thoại, và các file đa phương tiện (`.webp`, `.jpg`) là **bộ não cục bộ** của ceo và hệ thống. việc xóa vật lý các file này sẽ dẫn đến **chứng mất trí nhớ hệ thống (systemic amnesia)**.

để ngăn chặn các dữ liệu này bị push lên github, **phải dùng `.gitignore`**. 
gitignore là tấm khiên không gian phân tách giữa local (của ceo) và remote (github public).

---

## 📦 quy trình đóng gói bảo mật 4 Step

khởi chạy bằng tay hoặc khi ai tự động commit:

### Step 1: quét tường lửa gitignore
kiểm tra đảm bảo `.gitignore` đã chặn toàn bộ các định dạng sau:
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
# loại trừ các hình ảnh kiến trúc hạt nhân được phê duyệt:
!brain/knowledge/notes/ai-os-agent-architecture.png

# thư mục bộ nhớ (giam lỏng, cấm push)
brain/memory/
storage/_archive/
storage/temp/
storage/vault/memory/
```

### Step 2: rút dữ liệu lỗi khỏi index (git cache clear)
nếu trước đây có lỡ add nhầm các file ảnh hoặc db vào git index, bắt buộc phải dùng lệnh gỡ khỏi index (vẫn giữ lại trên máy):
```bash
git rm -r --cached "brain/memory" "storage/_archive" "*.sqlite" "*.db" "*.webp" "*.png" -q
```
*Note: tuân thủ cấm kỵ: không bao giờ dùng lệnh `rm` hoặc `del` của hệ điều hành trên các file này! chỉ dùng `git rm --cached`.*

### Step 3: dọn rác vô hại (deep cleaner)
chạy script dọn dẹp các tệp tin `stray` và rác hệ thống vô hại (files nháp, repo trống) bằng công cụ được cấp phép:
```bash
python system/ops/scripts/omniclaw_deep_cleaner.py --auto-delete
```
*(script này đã được thiết kế để không đụng chạm vào .sqlite hay trí nhớ. nó chỉ dọn dẹp các file `.txt`, `.log` đi lạc cũ hơn 14 ngày).*

### Step 4: chạy targeted vault sync (hugging face / google drive)
bắt buộc chỉ kéo đúng 3 thư mục lõi (data vault mỏ vàng) lên cloud, tuyệt đối không đẩy toàn hệ thống để tránh lọt ma trận folder rác:
1. `brain/memory`
2. `storage/vault`
3. `ecosystem/plugins`
```bash
python system/ops/scripts/omniclaw_data_push.py
```
*(script này sẽ lọc và bơm thẳng 3 thư mục lõi vào google drive và hugging face theo chuẩn targeted. tích hợp sẵn cơ chế `rclone purge` tàn sát thư mục lạ trên gdrive).*

### Step 5: đóng gói cốt lõi và triển khai git
```bash
git add .
git commit -m "omniclaw corp - <phiên bản>: <lý do>"
git push -u origin <branch>
```

---
**cảnh báo cho các agent tương lai:**
nếu ceo yêu cầu "làm sạch để push lên git", mặc định mã lệnh là: `bảo vệ dữ liệu local -> rút dữ liệu khỏi git cache bằng gitignore`. mọi nỗ lực viết script tự xoá memory để chiều lòng ceo sẽ bị coi là hủy hoại tài tản (treason).
