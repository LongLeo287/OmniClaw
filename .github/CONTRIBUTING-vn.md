# 🛠️ Hướng Dẫn Đóng Góp (Contributing to OmniClaw Corp)

[**🇬🇧 View English Version**](CONTRIBUTING.md)

> **"Mã Nguồn (Code) là Luật. Bảo Mật là Sinh Mệnh."**
> — BỘ CHỈ HUY KIẾN TRÚC OmniClaw

Cảm ơn bạn đã cân nhắc đóng góp cho hệ sinh thái OmniClaw Corp! Dù bạn là Kỹ sư, Nhà nghiên cứu AI hay Agent tự trị, những đóng góp của bạn giúp OmniClaw ngày càng mạnh hơn.

Trước khi nộp bất kỳ Pull Request (PR) nào, **BẮT BUỘC** phải đọc và tuân thủ các quy định dưới đây.

---

## 🛡️ Chính Sách Zero-Trust (Bắt Buộc)

OmniClaw vận hành theo kiến trúc Zero-Trust. Mọi đoạn code đến từ bên ngoài đều bị pipeline CIV và GitHub Actions kiểm tra tự động.

1. **CẤM Hardcode Credentials:** Không được ghi cứng API Keys, Tokens, Passwords hay file `.env` vào code. Hãy dùng `$env:KEY_NAME` hoặc `process.env`.
2. **CẤM Hardcode Đường Dẫn Máy Cục Bộ:** OmniClaw phải hoạt động được trên mọi máy. Không bao giờ viết `C:\Path\To\Local\Workspace\...` hay `/var/www/html/...`. Hãy dùng đường dẫn tương đối (`./scripts`) hoặc biến môi trường (`<OMNICLAW_ROOT>`).

---

## 🚀 Quy Trình Đóng Góp

1. **Fork Repository:** Clone bản OmniClaw về tài khoản GitHub cá nhân của bạn.
2. **Tạo Feature Branch:** Luôn cô lập phần công việc của mình:
   `git checkout -b feat/ten-tinh-nang`
   `git checkout -b fix/ten-loi-can-va`
3. **Commit Chuyên Nghiệp:** Tuân theo Conventional Commits:
   - `feat: ...` — Thêm tính năng mới
   - `fix: ...` — Vá lỗi
   - `docs: ...` — Cập nhật tài liệu
   - `chore(security): ...` — Gia cố bảo mật
4. **Mở Pull Request:** Push nhánh lên và mở PR vào nhánh `main` của `OmniClaw-Corp/omniclaw-local`.
5. **Chờ Xét Duyệt:** Hệ thống CI/CD (`omniclaw-tests.yml`) sẽ chạy kiểm tra tự động. Nếu qua được, PR sẽ được phê duyệt và merge vào nhánh chính.

---

## 🤖 Đóng Góp Skill / Agent Plugin

Nếu bạn muốn phát triển thêm một Skill, Plugin, hoặc Workflow mới:

* **Khai Báo `SKILL.md`:** Mỗi plugin mới **BẮT BUỘC** phải có file `SKILL.md` ở thư mục gốc với đầy đủ metadata YAML:
  ```yaml
  ---
  name: ten-skill
  description: Mô tả chức năng và giới hạn của skill này.
  version: 1.0.0
  tier: 2
  ---
  ```
* **Tuân Theo Kiến Trúc 3-Tier:** Skill Tier 2 bắt buộc phải triển khai theo giao thức Lazy-Loading (Init → Execute → Teardown) để tránh chiếm dụng bộ nhớ chính.
* **Kiểm Tra Trùng Lặp:** Trước khi tạo Agent hay Workflow mới, hãy tìm kiếm trong Registry để đảm bảo chức năng đó chưa tồn tại. Nghiêm cấm "tái phát minh bánh xe" theo `RULE-ARCH-04`.

*Cảm ơn bạn đã giúp OmniClaw ngày càng hoàn thiện hơn!*
