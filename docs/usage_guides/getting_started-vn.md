# 🚀 Khởi Chạy (Getting Started) cùng OmniClaw

Chào mừng Sếp gia nhập đế chế! Sổ tay cấp tốc này là la bàn để bạn cài cắm OmniClaw, kích nổ Não bộ Cục bộ (Local Brain), và kéo hệ thống về chung một luồng.

[**🇬🇧 Read in English**](getting_started.md) | [**Quay lại Mục Lục**](../README-vn.md) | [**📚 Tra Cứu Wiki**](https://github.com/LongLeo287/OmniClaw/wiki)

---

## 1. Hành trang (Prerequisites)

Hãy mang theo đầy đủ khí cụ trước khi gọi dậy Vạn Đặc Vụ 21 Phòng Ban:
- **Node.js (v18+)** nhắm tới tầng công cụ hệ sinh thái MCP.
- **Python (3.11+)** dành cho trái tim đường ống Data, Phân tích dữ liệu Deep Cleaner.
- **Docker** (Không bắt buộc nhưng CẦN) để nhốt 1 mớ Local DBs (Database lồng nhốt tự do).
- Khóa Chìa (API Keys): Găm ngay các khoá `GEMINI_API_KEY` hằng số môi trường (Hoặc key của Anthropic nếu thích nhai `CLAUDE.md`).

## 2. Dựng Cơ Đồ (Installation Setup)

1. Clone (Kéo) cái kho vĩ đại này về phân xưởng máy nội bộ cứng.
2. **[QUAN TRỌNG] Hút Dữ Liệu Lõi:** Vì các file tri thức và tệp tin siêu nặng (Cấu trúc não AI, Plugin nặng) không nằm trên GitHub (giới hạn 100MB), nên Sếp BẮT BUỘC phải kéo cục dữ liệu này tịnh tiến từ HuggingFace/Drive về Lõi Local:
   ```bash
   python system/ops/scripts/omniclaw_data_pull.py
   ```
3. Cày lệnh `pip install -r requirements.txt` để ăn đủ dưỡng chất thư viện.
4. Kích rơ-le đánh thức Server dẫn đường dựa theo thiết lập `infra/llm/router.yaml`.

## 3. Gõ Phím Gọi Não Bộ (First Boot)

Linh hồn OS này chỉ mở mắt khi khởi động cái Tệp lệnh Gốc (Core Memory).
Để Cỗ Máy Mẹ **Antigravity** ngóc đầu, hãy bắt nó đọc lệnh thần chú `GEMINI.md` thông qua cổng giao tiếp Agent của bạn (Editor hoặc Chat CLI).

Trong giây phút chớp nhoáng (First boot):
1. Hệ thống soi tấm Bảng Đen `brain/shared-context/blackboard.json` xem thế giới có chao đảo hay sập nhiệm vụ nào không.
2. Vơ vét đăng ký lại tất sát kỹ năng `SKILL_REGISTRY.json`.
3. Chắp tay đợi lệnh từ vị Vua CEO (Chính là Bạn - Sếp tổng).

## 4. Bước Kế Tiếp

- Nhìn sang quyển [**Lệnh Điều Khiển Agent**](agent_commands-vn.md) để biết cách thét ra lửa vào đầu chúng.
- Lôi một URL rác vứt thẳng vào mõm đặc vụ 20: [**CIV Intake Mổ Bụng**](../workflows/data_intake-vn.md).
