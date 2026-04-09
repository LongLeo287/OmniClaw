---
id: data-packaging-sync-vn
type: document
owner: SYSTEM
lang: vi
---

# Quy Trình Đóng Gói & Đồng Bộ (Cloud Push)

[**🇬🇧 View in English**](data_packaging_sync.md) | [**Wiki**](https://github.com/LongLeo287/OmniClaw/wiki)

---

Đây là luồng end-to-end để sao lưu và đóng gói toàn bộ Brain, State và Memory của OmniClaw, đồng thời đồng bộ lên ba hub cloud: **HuggingFace**, **Google Drive**, và **GitHub**. Tuân thủ nghiêm ngặt quy trình này đảm bảo không có đường dẫn gãy hay lỗi giới hạn file lớn (Git LFS).

---

## 1. Đẩy Dữ Liệu Mục Tiêu (Cloud Sniper)
Để tránh làm phình Git repository hoặc gửi lên các thư mục rác không cần thiết, hệ thống ưu tiên "Đồng Bộ Dữ Liệu Mục Tiêu" thay vì sao chép toàn bộ root.

Script cốt lõi xử lý thao tác vault dữ liệu này là:
**`system/ops/scripts/omniclaw_data_push.py`**

Nó thông minh trích xuất và đẩy ba thư mục hệ thống nặng nhất:
1. `brain/memory/` (Long-term Agent Experience Memory)
2. `storage/vault/` (Library of Raw Extracted Data and Media Assets)
3. `ecosystem/plugins/` (Third-Party Repositories and Agent Source Code)

Các asset lớn này được truyền an toàn vào **HuggingFace Dataset** và **Google Drive** Vault chính.

> **⚠️ Cảnh Báo:** Không bao giờ force push file database thô (`.db`, `.sqlite`, `.webp`) hoặc repository lưu trữ khổng lồ (>100MB) trực tiếp lên nhánh GitHub chính (`main`). Làm vậy vi phạm giới hạn LFS của GitHub và sẽ gây lỗi "pre-receive hook declined".

---

## 2. Kéo Dữ Liệu Mục Tiêu (Rehydrate Vault)
Khi nhà phát triển fork hoặc clone OmniClaw từ Github, `storage/vault` và `brain/memory` của họ có thể trống.
Để tải lại liền mạch các file nặng còn thiếu vào đúng đường dẫn nội bộ, chạy:
**`python system/ops/scripts/omniclaw_data_pull.py`**

Script này sử dụng `snapshot_download` của HuggingFace và RClone `copy` để **khớp chính xác và rehydrate** các cấu trúc thư mục gốc. Links sẽ không gãy và tất cả Agent sẽ nhận ra cấu trúc bộ nhớ ngay lập tức.

---

## 3. Quy Trình Sao Lưu Soul (Đóng Gói Phiên)
Trước bất kỳ commit code GitHub nào, quy tắc hệ thống bắt buộc sao lưu "active session soul" của phiên chat hiện tại của Operator.

**Script Thực Thi:**
```bash
powershell -ExecutionPolicy Bypass -File system\ops\scripts\memory\backup_soul.ps1
```

**Luồng Công Việc:**
1. Sao chép file `.pb` chính xác phản ánh phiên hội thoại Agent gần nhất.
2. Thu gom toàn bộ logic nội bộ lưu trong thư mục `brain/` gắn với UUID đó.
3. Payload khổng lồ này được nén chặt thành file Zip kín: `soul_backup.zip`.
4. Sau khi niêm phong xong, file được dock an toàn vào vùng buffer nội bộ được bảo vệ. Chỉ sau đó Operator mới được phép push Git Commit cuối cùng.

---

## 4. Cổng CI/CD Tự Động (GitHub Actions)
Ngay khi Operator chạy lệnh **Git Push** đồng bộ code lên nhánh `main`, hai Guardian GitHub Actions CI được kích hoạt:

- **`.github/workflows/ai-os-tests.yml`:** Liên tục kiểm tra vi phạm cú pháp Python (`.py`, `.js`), đảm bảo các thay đổi module `docs/` mới tích hợp không gây crash engine.
- **`.github/workflows/ai-os-validate.yml`:** Quét qua metadata kiến trúc quan trọng như `SKILL_REGISTRY.json` và cấu hình YAML agent. Đảm bảo mọi Skill mới được AI code độc lập đều đáp ứng cú pháp cấu hình hoàn hảo, không có ID trùng hoặc JSON mapping bị hỏng.

---

Mọi thủ tục Đóng Gói Dữ Liệu và Git Push phải tuân theo kiến trúc nghiêm ngặt này. Tính toàn vẹn Hệ thống OmniClaw là bất khả xâm phạm.
