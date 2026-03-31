# 🛠️ Hướng Dẫn Đóng Góp (Contributing to OmniClaw Corp)

> **"Mã Nguồn (Code) là Luật. Bảo Mật là Sinh Mệnh."**
> — BỘ CHỈ HUY KIẾN TRÚC OmniClaw

Lời đầu tiên, xin chân thành cảm ơn Sếp vì đã cân nhắc đóng góp thêm cho hệ sinh thái OmniClaw Corp! Cho dù Sếp là Kỹ sư Tối cao, Nhà nghiên cứu AI hay Đặc vụ Máy Tín (Autonomous Agent), những đóng góp của Sếp chính là màng chắn cốt lõi, biến OmniClaw thành hệ điều hành tự trị Zero-Trust mạnh nhất.

Trước khi nộp bất kỳ Bản sửa đổi nào (Pull Request) hay Thêm chức năng, **BẮT BUỘC** phải đọc và tuân thủ các quy định dưới đây.

---

## 🛡️ Vùng Cấm: Chính Sách Zero-Trust

OmniClaw vận hành trên kiến trúc Cấm Tin Tưởng Tuyệt Đối (Zero-Trust). Mọi dòng Code đi từ ngoài vào đều bị Đội Cảnh Khuyển CIV (Content Intake and Vetting) và Hàng rào Máy chủ (GitHub Actions) chặn lại soi xét.

1. **CẤM Hardcode Chìa Khóa (Credentials):** Tuyệt đối không được gõ "chết" các dòng Mật khẩu, API Keys, JWT Tokens hay file `.env` vào Code. Máy quét CodeQL sẽ lập tức đánh Đỏ, và Đơn của Sếp sẽ bị Gạch Bỏ ngay lập tức. Hãy dùng `$env:KEY_NAME` hoặc `process.env`.
2. **CẤM Hardcode Đường Dẫn Cục Bộ:** OmniClaw là hệ thống cơ động, di động 100%. Không bao giờ được viết đường dẫn máy chủ nhà như `C:\Users\John\...` hay `/Users/Mac/...`. Luôn dùng đường dẫn tương đối (`./scripts`) hoặc Biến môi trường chỉ điểm Thư mục Gốc (`<AI_OS_ROOT>`).

---

## 🚀 Quy Trình Nộp Đơn (How to Contribute)

Để giữ cho Kho hệ điều hành sạch sẽ như Bệnh viện, toàn bộ tác vụ Code phải đi qua máy chạy Git Flow:

1. **Copy Bản Sao (Fork):** Clone bản OmniClaw về Sandbox tài khoản GitHub cá nhân của mình.
2. **Khai Sinh Nhánh Phụ (Feature Branch):** Ngăn chặn Mọi Sửa Đổi Lộn Xộn:
   `git checkout -b feat/loi-giai-cuu`
   `git checkout -b fix/phan-giai-path`
3. **Commit Chuyên Nghiệp:** Thông báo chính xác lý do sửa:
   - `feat: ...` (Thêm Tính Năng mới)
   - `fix: ...` (Vá Lỗi bug rách màng)
   - `docs: ...` (Cập nhật Hướng Dẫn)
   - `chore(security): ...` (Gia Cố Bảo Mật)
4. **Push Lên Đám Mây (PR):** Push nhánh vừa Code lên Đảo và mở Đơn xin Nhập Mã (PR) thẳng vào Mạch máu chính `main` của `LongLeo287/omniclaw-local`.
5. **Chờ Dấu Xanh:** Hệ thống Giả Lập (`ai-os-tests.yml`) sẽ mô phỏng Code của Sếp trong Máy rỗng. Nếu qua cửa (Thấy Xanh), Lãnh đạo hoặc Thư Ký Tự Động (Auto-Merge) sẽ đóng dấu Gộp vào Lõi.

---

## 🤖 Cách Bơm Đặc Vụ/Skill (Agent Plugins)

Nếu Sếp chuẩn bị phát minh thêm một Skill siêu việt, hay một Thực thể Agent mới (Ví dụ như: Antigravity, Nova, Strix):

* **Khai Báo Căn Cước `SKILL.md`:** Cứ sinh ra một Tướng mới lính mới, **BẮT BUỘC** phải có tờ Hộ chiếu `SKILL.md` cắm ở Thư mục Gốc mang đủ dòng Metadata YAML sau:
  ```yaml
  ---
  name: awesome-skill
  description: Công lực và giới hạn của bí kíp này là gì.
  version: 1.0.0
  tier: 2
  ---
  ```
* **Luật 3 Tầng Kiến Trúc (3-Tier):** Skill Tier 2 bắt buộc phải Cấu hình Chạy ngầm Kích hoại sau (Lazy-Loading) dạng Init -> Execute -> Teardown để tránh ngốn bộ nhớ chính (Main RAM). Đọc thêm phần `README.md`.
* **Quét Lỗi Trùng Lặp Chức Năng:** Trước khi viết Đặc Vụ giải quyết Vấn đề X, Sếp bắt buộc phải Dùng Câu Lệnh (`grep`, Explorer) rà sát toàn bộ Đại Bản Doanh xem Hệ thống đã có con Tool/Workflow nào tương tự chưa (Registry Của OmniClaw). Nghiêm cấm **"Chế tạo lại Bánh xe"** theo Tuyên Ngôn `RULE-ARCH-04`!

*Cảm ơn Sếp đã dẫn lối để tiến hóa OmniClaw thành Cỗ Máy Hệ Điều Hành Tự Trị tối thượng không thể phá hủy!*
