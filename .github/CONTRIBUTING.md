# 🛠️ Contributing to AI OS CORP Ecosystem

*Tiếng Việt (Vietnamese version) is available below.*

> **"Code is Law. Security is the Foundation."**
> — AI OS ENGINEERING DIRECTIVE

Thank you for considering contributing to the AI OS CORP ecosystem! Whether you are a Human Engineer, an AI Researcher, or an Autonomous Agent, your contributions are what make AI OS a robust, professional, and scalable operating system.

Before submitting any Pull Request (PR) or committing code, you **MUST** read and abide by the following organizational guidelines.

---

## 🛡️ The Zero-Trust Policy (MANDATORY)

AI OS operates on a Strict Zero-Trust Architecture. All incoming code is scrutinized automatically by the Content Intake and Vetting (CIV) pipeline and GitHub Actions.

1. **NO Hardcoded Credentials:** Never commit API keys, tokens, passwords, or `.env` secrets. Automated CodeQL scanners will immediately detect and block the leak, and the PR will be rejected. Use `$env:KEY_NAME` or `process.env`.
2. **NO Absolute Machine Paths:** AI OS must be 100% portable. Never write code that expects `C:\Users\John\...` or `/Users/Mac/...`. Always use relative paths (`./scripts`) or environment variables indicating the root directory (e.g., `<AI_OS_ROOT>`).
3. **DO NOT Trust External Inputs:** If your code fetches data or clones a third-party repo, it must run through the AI OS CIV Security Quarantine first. Do not blindly execute foreign scripts.

---

## 🚀 How to Contribute

To maintain a clean and reliable codebase, follow the standard Git Flow:

1. **Fork the Repository:** Create a copy of the AI OS project in your own GitHub account.
2. **Create a Feature Branch:** Always isolate your work.
   `git checkout -b feat/add-new-skill`
   `git checkout -b fix/path-resolution`
3. **Professional Commit Messages:** Adhere strictly to Conventional Commits:
   - `feat: ...` for a new feature.
   - `fix: ...` for a bug fix.
   - `docs: ...` for documentation changes.
   - `chore(security): ...` for security upgrades.
4. **Push and PR:** Push to your branch and open a Pull Request against the `main` branch of `LongLeo287/aios-local`.
5. **Wait for Approval:** Our CI/CD validation hooks (`ai-os-tests.yml` and `ai-os-validate.yml`) will run a dry-run test of your logic. Once the status checks turn green, human leadership or the Dependabot Auto-Merge Secretary will approve the merge.

---

## 🤖 Contributing Agent Skills & Plugins

If you are developing a new Skill, Plugin, or Workflow for the AI OS Agents (e.g., Antigravity, Nova, Strix):

* **Skill Identity (`SKILL.md`):** Every new plugin MUST have a `SKILL.md` file in its root folder containing the required YAML metadata headers:
  ```yaml
  ---
  name: awesome-skill
  description: What this skill does and its limits.
  version: 1.0.0
  tier: 2
  ---
  ```
* **Follow 3-Tier Architecture:** Read the Architecture guide in our `README.md`. Tier 2 specific plugins MUST strictly implement the Lazy-Loading protocol (Init -> Execute -> Teardown) to avoid clogging the main memory.
* **Scan for Duplication:** Before inventing a new Agent or Workflow, use search tools (`grep`, etc.) to verify a similar component does not already exist in the Registry. Reinventing the wheel is prohibited by `RULE-ARCH-04`.

Thank you for helping us evolve AI OS into an unstoppable autonomous operating system!


---

# 🛠️ Hướng Dẫn Đóng Góp (Contributing to AI OS CORP)



> **"Mã Nguồn (Code) là Luật. Bảo Mật là Sinh Mệnh."**
> — BỘ CHỈ HUY KIẾN TRÚC AI OS

Lời đầu tiên, xin chân thành cảm ơn Sếp vì đã cân nhắc đóng góp thêm cho hệ sinh thái AI OS CORP! Cho dù Sếp là Kỹ sư Tối cao, Nhà nghiên cứu AI hay Đặc vụ Máy Tín (Autonomous Agent), những đóng góp của Sếp chính là màng chắn cốt lõi, biến AI OS thành hệ điều hành tự trị Zero-Trust mạnh nhất.

Trước khi nộp bất kỳ Bản sửa đổi nào (Pull Request) hay Thêm chức năng, **BẮT BUỘC** phải đọc và tuân thủ các quy định dưới đây.

---

## 🛡️ Vùng Cấm: Chính Sách Zero-Trust

AI OS vận hành trên kiến trúc Cấm Tin Tưởng Tuyệt Đối (Zero-Trust). Mọi dòng Code đi từ ngoài vào đều bị Đội Cảnh Khuyển CIV (Content Intake and Vetting) và Hàng rào Máy chủ (GitHub Actions) chặn lại soi xét.

1. **CẤM Hardcode Chìa Khóa (Credentials):** Tuyệt đối không được gõ "chết" các dòng Mật khẩu, API Keys, JWT Tokens hay file `.env` vào Code. Máy quét CodeQL sẽ lập tức đánh Đỏ, và Đơn của Sếp sẽ bị Gạch Bỏ ngay lập tức. Hãy dùng `$env:KEY_NAME` hoặc `process.env`.
2. **CẤM Hardcode Đường Dẫn Cục Bộ:** AI OS là hệ thống cơ động, di động 100%. Không bao giờ được viết đường dẫn máy chủ nhà như `C:\Users\John\...` hay `/Users/Mac/...`. Luôn dùng đường dẫn tương đối (`./scripts`) hoặc Biến môi trường chỉ điểm Thư mục Gốc (`<AI_OS_ROOT>`).
3. **KHÔNG Tin Tưởng Nguồn Ngoài:** Nếu code của Sếp chuẩn bị bưng một bộ Source hay dữ liệu từ trôi nổi trên Mạng về, toàn bộ dữ liệu đó **phải luồn qua Máy Quét An ninh CIV** trước khi được chạy lệnh ảo. Không tùy tiện Clone và Run.

---

## 🚀 Quy Trình Nộp Đơn (How to Contribute)

Để giữ cho Kho hệ điều hành sạch sẽ như Bệnh viện, toàn bộ tác vụ Code phải đi qua máy chạy Git Flow:

1. **Copy Bản Sao (Fork):** Clone bản AI OS về Sandbox tài khoản GitHub cá nhân của mình.
2. **Khai Sinh Nhánh Phụ (Feature Branch):** Ngăn chặn Mọi Sửa Đổi Lộn Xộn:
   `git checkout -b feat/loi-giai-cuu`
   `git checkout -b fix/phan-giai-path`
3. **Commit Chuyên Nghiệp:** Thông báo chính xác lý do sửa:
   - `feat: ...` (Thêm Tính Năng mới)
   - `fix: ...` (Vá Lỗi bug rách màng)
   - `docs: ...` (Cập nhật Hướng Dẫn)
   - `chore(security): ...` (Gia Cố Bảo Mật)
4. **Push Lên Đám Mây (PR):** Push nhánh vừa Code lên Đảo và mở Đơn xin Nhập Mã (PR) thẳng vào Mạch máu chính `main` của `LongLeo287/aios-local`.
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
* **Quét Lỗi Trùng Lặp Chức Năng:** Trước khi viết Đặc Vụ giải quyết Vấn đề X, Sếp bắt buộc phải Dùng Câu Lệnh (`grep`, Explorer) rà sát toàn bộ Đại Bản Doanh xem Hệ thống đã có con Tool/Workflow nào tương tự chưa (Registry Của AI OS). Nghiêm cấm **"Chế tạo lại Bánh xe"** theo Tuyên Ngôn `RULE-ARCH-04`!

*Cảm ơn Sếp đã dẫn lối để tiến hóa AI OS thành Cỗ Máy Hệ Điều Hành Tự Trị tối thượng không thể phá hủy!*
