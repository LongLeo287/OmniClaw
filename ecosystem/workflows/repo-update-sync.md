# Department: operations
---
description: Pipeline for continually monitoring and pulling new releases (knowledge + code diffs) from actively integrated plugins
---
# OmniClaw Update Sync Pipeline
# Version: 1.0 | 2026-03-24 | Owner: Antigravity + Dept 20 CIV

> **Mục tiêu**: Khi một repository (plugin) đã lọt vào Mắt của OmniClaw (Verditct = APPROVE) và chính thức được cài đặt (Integrate), hệ thống phải **liên tục nhận được các bản sinh trưởng / cập nhật** từ Source gốc (Trên Github).
> Việc này tránh cho các công cụ lõi của AI OS bị lỗi thời so với thế giới.

---

## KIẾN TRÚC THEO DÕI (TRACKING ARCHITECTURE)

Hệ thống hoạt động theo mô hình **Khắc dấu & Cảnh báo (Mark & Alert)**, nói 'Không' với việc Overwrite Source Code thẳng tay để bảo vệ tính toàn vẹn (Safety) của OmniClaw.

### 1. Bắt đầu Vòng đời Giám sát (Marking)
Khi lệnh `omniclaw integrate owner/repo` được chạy:
- Script `omniclaw_integrate.py` tự động nhúng khóa `github_url: ...` vào file `manifest.json`.
- Nó cũng khởi tạo khóa `tracking: true` (bảo vệ bằng cờ) và `last_synced_release: "initial_intake"`.

### 2. Vòng Lặp Tuần tra (Polling Daemon)
File lõi: `system/ops/scripts/omniclaw_update_daemon.py`

#### Cách thức:
```bash
python system/ops/scripts/omniclaw_update_daemon.py
```
*(Có thể đưa vào Cronjob chạy 24 tiếng / 1 lần, hoặc chạy thủ công bởi CIV)*.

- Lôi toàn bộ danh mục Plugin từ `registry.json` ra điểm danh.
- Chọc vào GitHub API: `GET /repos/{owner}/{repo}/releases/latest`.
- Đo lường phiên bản: Nếu `tag_name` > `manifest["last_synced_release"]`, kích hoạt Tình trạng Cập nhật.

### 3. Tải Tri thức & Cảnh Báo (Knowledge Extractor)
Khi Bot nhận diện có phiên bản mới:
1. Nó tải toàn bộ mô tả thay đổi (Release Notes / Changelog) về máy.
2. Ép thành định dạng `.md` lưu vào `brain/knowledge/updates/`.
3. Thông qua cơ chế đọc file, các Agent khác của OmniClaw có thể lập tức "biết" Plugin này vừa ra tính năng gì mới.
4. Nó tự động Update dòng `manifest["last_synced_release"]` để không tải lại hai lần.
5. Cuối cùng, nó **tự động Git Clone** nhánh cập nhật mới đó vào vùng cách ly (`QUARANTINE_DIR/incoming/UPDATE/{repo}`).
6. Chạy tiếp kịch bản `knowledge_extractor.py` để ép toàn bộ mã nguồn phiên bản mới thành 1 khối tri thức ném thẳng vào `brain/knowledge/processed_repos/`. Như vậy RAG Agent luôn học được bản Code mới nhất.

---

## ỨNG XỬ KHI CÓ UPDATES

Hệ thống OmniClaw là một con tàu lõi, MỌI bản cập nhật đều mang rủi ro Breaking Changes (Làm vỡ hệ thống). Vì vậy, quy trình cài đặt bản thân mã code mới (Update Source Code) vẫn **yêu cầu bàn tay con người hoặc Agent được Cấp quyền Khẩn cấp**.

1. **Nhận được Knowledge Alert**: Người quản trị vào `brain/knowledge/updates/` đọc Release notes.
2. **Kiểm duyệt**: Các thay đổi có ảnh hưởng API, làm sửa Path hay xung đột thư viện không?
3. **Thực thi update**: Vào thư mục `ecosystem/plugins/{repo}/` và dùng `git pull` hoặc tải file zip đè lên.

---
*Pipeline Owner: Antigravity | Synchronization Flow | Created: 2026-03-24*
*"Track endlessly, Alert quickly, Overwrite cautiously."*
