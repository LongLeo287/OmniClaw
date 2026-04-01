---
name: Pull Request (VN)
about: Nộp bản vá, công cụ, hoặc cập nhật đặc vụ AI
---

[**🇺🇸 Read English Version**](omniclaw_pr_template.md)

## 🛠 Khu Vực Cập Nhật
- [ ] Lõi Hạ Tầng (Tier 1) / Bootstrapper
- [ ] Plugin / Công Cụ (Tier 2/3)
- [ ] Danh Sách Đặc Vụ / Vai Trò / Prompt
- [ ] Luật Hệ Thống / Quản Trị (`SOUL.md`, `GEMINI.md`, v.v.)
- [ ] Bơm Kiến Thức / Bộ Nhớ RAG

## 📖 Mô Tả
Vui lòng giải thích ngắn gọn cập nhật này làm gì và tại sao nó cần thiết.

## ✅ Danh Sách Kiểm Tra (Bắt buộc)
- [ ] Code đã được quét bảo mật (Không nhúng API keys / Mật khẩu cá nhân / `.env`).
- [ ] Tính năng mới KHÔNG thực thi lệnh hệ điều hành Root trực tiếp trừ khi được cấp quyền rõ ràng (chính sách `SafeToAutoRun` nghiêm ngặt).
- [ ] (Nếu là Plugin Mới) Tuân thủ nghiêm ngặt Kiến trúc Tải Chậm 3 Tầng (Lazy-Load 3-Tier).
- [ ] Đã cập nhật `SKILL_REGISTRY.json` hoặc `AGENTS.md` (nếu có).

## 🧠 Tác Động Giao Tiếp (Liên quan đến CEO)
Cập nhật này có làm thay đổi cách CEO ra lệnh cho hệ thống không?
(Nếu có, giải thích ngắn gọn về lệnh mới / luồng thông tin mới).