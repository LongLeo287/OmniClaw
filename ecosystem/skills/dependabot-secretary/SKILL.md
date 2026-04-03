---
name: dependabot-secretary
description: quản lý và hướng dẫn các agent khác nhường quyền merging cho bot tự động của github.
version: 1.0.0
tier: 1
---

# 🤖 dependabot secretary (auto-merge handler)

## 📌 khái quát về đặc vụ này (skill overview)
đây là một "đặc vụ bóng đêm" (background agent). nó thực chất là một github action nằm ở tầng cloud (`.github/workflows/ai-os-dependabot-merger.yml`). chức năng duy nhất của nó là duyệt đơn (auto-approve) và sát nhập (auto-merge) các pull requests tạo bởi thằng `dependabot[bot]`.

## ⚙️ cơ chế làm việc theo chuẩn zero-trust
thay vì phó mặc 100%, thư ký này bị giới hạn quyền bằng luật `rule-version-02`:

1.  **duyệt lỗ hổng bảo mật ngắn hạn (minor/patch security):** nếu thư viện x nhảy từ bản `v1.2.0` lên bản `v1.2.1` để vá lỗ hổng (ví dụ: lỗi picomatch) -> kích hoạt quyền merging tự động.
2.  **duyệt lỗ hổng từ các nền tảng chạy độc lập bên ngoài:** các thư viện nằm trong mục `dependencies` hoặc `deps-dev` (test) không làm sập lõi chính.
3.  **khóa quyền trước mặt the core major bumps:** nếu dependabot đòi đẩy bản `v1.2` thẳng lên bản lớn `v2.0.0` (gây đứt gãy tương thích api) -> từ chối chạy! để ceo duyệt thủ công tay đôi.

## 🤝 giao ước khi làm việc cùng (collaborator agent instructions)
nếu bạn là một con ai agent (ví dụ: `nova`, `antigravity`, `claude code`), và bạn nhìn thấy các thư viện trên repo local đang khác version với trên cloud:

1.  bạn tuyệt đối **không được phép chạy lệnh nâng cấp thủ công** các lỗ hổng (vulnerable components) bằng `pip upgrade` hay `npm update` trong conversation.
2.  thay vào đó, hãy yên tâm để dependabot quét, và **dependabot secretary sẽ tự động xử lý nó trên cloud**. bạn chỉ tập trung vào logic code của chức năng được ceo giao.
3.  trường hợp ceo ra lệnh cụ thể: "mày hãy nâng cấp riêng thằng x lên bản y cho tao". lúc này bạn mới được phép code vào version.

***Note: skill này là dạng căn cước định danh giới hạn trách nhiệm.***
