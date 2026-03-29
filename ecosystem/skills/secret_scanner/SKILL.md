---
name: secret_scanner
description: Máy quét lộ Token/Password của phòng ban Strix Security
---
# Vũ Khí Cứu Sinh: Secret Scanner

Dựa trên siêu kiến trúc của **Trufflehog**, đây là kỹ năng chuyên dụng CHỈ DÀNH cho `strix-agent` (Dept 10) hoặc `security-auditor`. Bất cứ Agent nào khác cấm lén lút quét nếu không có lệnh C-Suite.

## Định Nghĩa Nhiệm Vụ (The Core Directives)
- Quét TÀN BẠO: Lục lọi từng dòng `.env`, `.yml`, `.json`, `*.py` của mọi mục tiêu truyền tới.
- Tìm kiếm Pattern nhạy cảm cao: `sk-...` (Stripe/OpenAI), `ghp_...` (Github PAT), `xoxb-...` (Slack), `AKIA...` (AWS), JSON rác chứa Regex của Private Keys (`-----BEGIN PRIVATE KEY-----`).

## Luồng Bão Tố (Storm Workflow)
1. Kích hoạt `secret_scanner` báo tọa độ thư mục đích.
2. Nó sẽ Regex Matching toàn bộ các file trong Target (Bao gồm cả các Commit History nếu cần).
3. Báo động ĐỎ: Lập tức ghi log vào `QUARANTINE_REJECTED` nếu tìm thấy DÙ CHỈ LÀ TRONG COMMENT. Điểm nổ cách ly repo đó ngay lập tức, không khoan nhượng.
4. KHÔNG bao giờ in cái key/token đó ra màn hình Chat của Lãnh tụ Sếp. Chỉ được phép ghi LOG RẰNG: `Đã cắt tiết Repo abc vì phát hiện OpenAI key bị lọt ở file script.py`.

## Tool Usage
Mặc định hệ thống Python Core đã cài các hàm Regex chặn. Agents mang Skill này có quyền khước từ sáp nhập Tri thức và block Workflow của Kỹ sư (Dept 01) lập tức.
