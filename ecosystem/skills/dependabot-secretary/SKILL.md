---
name: dependabot-secretary
description: Quản lý và hướng dẫn các Agent khác nhường quyền Merging cho Bot tự động của GitHub.
version: 1.0.0
tier: 1
---

# 🤖 Dependabot Secretary (Auto-Merge Handler)

## 📌 Khái quát về Đặc vụ này (Skill Overview)
Đây là một "Đặc vụ Bóng đêm" (Background Agent). Nó thực chất là một GitHub Action nằm ở tầng Cloud (`.github/workflows/ai-os-dependabot-merger.yml`). Chức năng duy nhất của nó là Duyệt Đơn (Auto-Approve) và Sát nhập (Auto-Merge) các Pull Requests tạo bởi Thằng `dependabot[bot]`.

## ⚙️ Cơ Chế Làm Việc Theo Chuẩn Zero-Trust
Thay vì phó mặc 100%, Thư ký này bị giới hạn quyền bằng Luật `RULE-VERSION-02`:

1.  **Duyệt Lỗ Hổng Bảo Mật Ngắn Hạn (Minor/Patch Security):** Nếu Thư Viện X nhảy từ bản `v1.2.0` lên bản `v1.2.1` để vá lỗ hổng (Ví dụ: Lỗi Picomatch) -> Kích Hoạt Quyền Merging tự động.
2.  **Duyệt Lỗ Hổng Từ Các Nền Tảng Chạy Độc Lập Bên Ngoài:** Các Thư viện nằm trong mục `dependencies` hoặc `deps-dev` (Test) không làm sập Lõi Chính.
3.  **Khóa Quyền Trước Mặt The Core Major Bumps:** Nếu Dependabot đòi đẩy bản `v1.2` thẳng lên bản lớn `v2.0.0` (Gây đứt gãy tương thích API) -> Từ chối chạy! Để CEO duyệt thủ công tay đôi.

## 🤝 Giao Ước Khi Làm Việc Cùng (Collaborator Agent Instructions)
Nếu bạn là một con AI Agent (Ví dụ: `Nova`, `Antigravity`, `Claude Code`), và bạn nhìn thấy các thư viện trên repo Local đang khác Version với trên Cloud:

1.  BẠN TUYỆT ĐỐI **KHÔNG ĐƯỢC PHÉP CHẠY LỆNH NÂNG CẤP THỦ CÔNG** CÁC LỖ HỔNG (Vulnerable Components) BẰNG `pip upgrade` hay `npm update` TRONG CONVERSATION.
2.  Thay vào đó, hãy yên tâm để Dependabot quét, và **Dependabot Secretary sẽ tự động xử lý nó trên Cloud**. Bạn chỉ tập trung vào Logic Code của chức năng được CEO giao.
3.  Trường hợp CEO ra lệnh cụ thể: "Mày hãy nâng cấp riêng thằng X lên bản Y cho tao". Lúc này bạn mới được phép Code vào Version.

***Lưu ý: Skill này là dạng Căn cước định danh giới hạn trách nhiệm.***
