# department: operations
---
description: pipeline for continually monitoring and pulling new releases (knowledge + code diffs) from actively integrated plugins
---
# omniclaw update sync pipeline
# version: 1.0 | 2026-03-24 | owner: antigravity + dept 20 civ

> **mục tiêu**: khi một repository (plugin) đã lọt vào mắt của omniclaw (verditct = approve) và chính thức được cài đặt (integrate), hệ thống phải **liên tục nhận được các bản sinh trưởng / cập nhật** từ source gốc (trên github).
> việc này tránh cho các công cụ lõi của ai os bị lỗi thời so với thế giới.

---

## kiến trúc theo dõi (tracking architecture)

hệ thống hoạt động theo mô hình **khắc dấu & cảnh báo (mark & alert)**, nói 'không' với việc overwrite source code thẳng tay để bảo vệ tính toàn vẹn (safety) của omniclaw.

### 1. bắt đầu vòng đời giám sát (marking)
khi lệnh `omniclaw integrate owner/repo` được chạy:
- script `omniclaw_integrate.py` tự động nhúng khóa `github_url: ...` vào file `manifest.json`.
- nó cũng khởi tạo khóa `tracking: true` (bảo vệ bằng cờ) và `last_synced_release: "initial_intake"`.

### 2. vòng lặp tuần tra (polling daemon)
file lõi: `system/ops/scripts/omniclaw_update_daemon.py`

#### cách thức:
```bash
python system/ops/scripts/omniclaw_update_daemon.py
```
*(có thể đưa vào cronjob chạy 24 tiếng / 1 lần, hoặc chạy thủ công bởi civ)*.

- lôi toàn bộ danh mục plugin từ `registry.json` ra điểm danh.
- chọc vào github api: `get /repos/{owner}/{repo}/releases/latest`.
- đo lường phiên bản: nếu `tag_name` > `manifest["last_synced_release"]`, kích hoạt tình trạng cập nhật.

### 3. tải tri thức & cảnh báo (knowledge extractor)
khi bot nhận diện có phiên bản mới:
1. nó tải toàn bộ Description Changes (release notes / changelog) về máy.
2. ép thành định dạng `.md` lưu vào `brain/knowledge/updates/`.
3. thông qua cơ chế đọc file, các agent khác của omniclaw có thể lập tức "biết" plugin này vừa ra tính năng gì mới.
4. nó tự động update dòng `manifest["last_synced_release"]` để không tải lại hai lần.
5. cuối cùng, nó **tự động git clone** nhánh cập nhật mới đó vào vùng cách ly (`quarantine_dir/incoming/update/{repo}`).
6. chạy tiếp kịch bản `knowledge_extractor.py` để ép toàn bộ mã nguồn phiên bản mới thành 1 khối tri thức ném thẳng vào `brain/knowledge/processed_repos/`. như vậy rag agent luôn học được bản code mới nhất.

---

## ứng xử khi có updates

hệ thống omniclaw là một con tàu lõi, mọi bản cập nhật đều mang rủi ro breaking changes (làm vỡ hệ thống). vì vậy, quy trình cài đặt bản thân mã code mới (update source code) vẫn **yêu cầu bàn tay con người hoặc agent được cấp quyền khẩn cấp**.

1. **nhận được knowledge alert**: người quản trị vào `brain/knowledge/updates/` đọc release notes.
2. **kiểm duyệt**: các Changes có ảnh hưởng api, làm sửa path hay xung đột thư viện không?
3. **thực thi update**: vào thư mục `ecosystem/plugins/{repo}/` và dùng `git pull` hoặc tải file zip đè lên.

---
*pipeline owner: antigravity | synchronization flow | created: 2026-03-24*
*"track endlessly, alert quickly, overwrite cautiously."*
