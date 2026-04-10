---
id: getting-started-vn
type: document
owner: SYSTEM
lang: vi
---

# 🚀 Bắt Đầu với OmniClaw

Chào mừng! Hướng dẫn này sẽ đưa bạn qua các bước cài đặt OmniClaw, khởi động AI orchestrator đầu tiên, và liên kết workspace nội bộ.

[**🇬🇧 View in English**](getting_started.md) | [**Quay về Mục Lục Docs**](../README-vn.md) | [**📚 Wiki**](https://github.com/LongLeo287/OmniClaw/wiki)

---

## 1. Yêu Cầu Trước Khi Cài

Trước khi kích hoạt khung AI 28 phòng ban, đảm bảo đã cài đặt:
- **Node.js (v18+)** cho hệ sinh thái MCP và các công cụ JavaScript.
- **Python (3.11+)** cho backend lý luận sâu và luồng pipeline.
- **Docker** (Tùy chọn nhưng khuyến nghị) để khởi động DB và API nội bộ cô lập.
- **API Keys**: Cung cấp `GEMINI_API_KEY` (hoặc Anthropic keys nếu dùng Claude Code).

## 2. Cài Đặt

1. Clone repository về máy: `git clone <repo-url>`
2. **[QUAN TRỌNG] Kéo về Vault Nặng:** Vì dữ liệu nặng (như Agent Memory và plugin code lớn) không được lưu trên GitHub do giới hạn 100MB, bạn PHẢI kéo các fragment delta từ HuggingFace/Drive:
   ```bash
   python system/ops/scripts/omniclaw_data_pull.py
   ```
3. Cài dependencies: `pip install -r requirements.txt`
4. Khởi động các router ban đầu qua `infra/llm/router.yaml`.

## 3. Khởi Động Lần Đầu

Hệ thống OmniClaw bắt đầu bằng cách boot file bộ nhớ orchestrator chính.
Để kích hoạt **Antigravity** — engine hub trung tâm — nạp file `GEMINI.md` qua giao diện agent trong IDE (hoặc Claude Code với `CLAUDE.md`).

Khi boot lần đầu, hệ thống sẽ:
1. Đọc `brain/memory/blackboard.json` để xem trạng thái tác vụ toàn cục hiện tại.
2. Đăng ký toàn bộ năng lực khả dụng từ `SKILL_REGISTRY.json`.
3. Chờ lệnh từ CEO (Con Người).

## 4. Bước Tiếp Theo

- Đọc [**Lệnh Agent**](agent_commands-vn.md) để hiểu cách tương tác.
- Gửi repository để xử lý qua giao thức [**CIV Intake**](../workflows/data_intake-vn.md).

