---
description: How pipeline-architect orchestrates event-driven automated chains
---
# Workflow Đỉnh Cao: Dây Chuyền Tự Động Hóa (Dept 22 - Operations)

## Nền tảng (The Core concept)
Được trích xuất từ `claude-workflow-v2`, thay vì CEO ném Issue thủ công, hệ thống OmniClaw dựa vào tín hiệu từ Cảm biến (Webhooks, File Watchers, hoặc Git Hooks). `pipeline-architect` đóng vai trò "Kỹ sư Nhà Máy".

## Giai đoạn 1: Mắc Xích Kích Hoạt (Triggers)
- Các sự kiện có thể kích hoạt Pipeline: 
  - Đóng 1 cái Pull Request (Code sáp nhập).
  - Agent Đội Engineering Vừa gõ xong chữ `END_SCRIPT`.
  - Có 1 File rác mới rớt vào thư mục `/tmp`.
- Kỹ sư sẽ gài Lắng nghe (Listen Event). Khi 1 Trigger nổ, `pipeline-architect` được đánh thức.

## Giai đoạn 2: Lắp Đạn Tự Động (Event Chain)
- Gọi 1 loạt lệnh (bash) hoặc skill liên hoàn không ngắt quãng.
- **Ví dụ chuỗi Phát Hành Code (Deploy Chain):**
  1. Gọi `Strix_Protocol` (Dept 06) Quét an ninh tĩnh (Trivy).
  2. Bắn sang `QA-tester` (Dept 02) Chạy Jest hoặc Playwright tự động nghiệm thu giao diện.
  3. Gọi Lệnh rsync lên Server Product.
  
## Giai đoạn 3: Rớt Xích & Vá Lỗi (Fallbacks)
- Nếu mắc xích B chết (Ví dụ: Lỗi UnitTest).
- Kỹ sư tự động gửi ngược Cảnh báo cho Dept 01 (Kỹ sư code), bắt họ đẻ ra Bản Vá. Vòng lặp tự đóng kín cho đến khi Node qua được.

## Giai đoạn 4: Telegram Bridge
- Hoàn thành Toàn chuỗi -> Bắn ping lên Sếp qua OmniClaw Bot: `"🚀 [DEPLOY HOÀN TẤT] Bản vá #42 đã online"`. CEO tốn đúng 0 cú Click.
