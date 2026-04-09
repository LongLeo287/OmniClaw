---
id: agent-commands-vn
type: document
owner: SYSTEM
lang: vi
---

# 💻 Lệnh Agent (Sử Dụng CLI)

Giao thức này quy định cách người vận hành (CEO) hoặc Orchestrator gọi các agent và công cụ cụ thể trong khung OmniClaw.

[**🇬🇧 View in English**](agent_commands.md) | [**Quay về Mục Lục Docs**](../README-vn.md) | [**📚 Wiki**](https://github.com/LongLeo287/OmniClaw/wiki)

---

## Gọi Trực Tiếp qua Terminal

Nếu muốn bỏ qua Orchestrator và nói chuyện trực tiếp với một agent, nạp file `_rules.md` cụ thể của họ trong `brain/rules` và cung cấp tác vụ ban đầu.

**Ví dụ: Kích Hoạt Strix Security (Phòng 10)**

Khi bạn đang đánh giá một repo clone hoặc plugin cộng đồng:

```bash
> Hey Assistant, load brain/rules/10_strix_security_rules.md and review this payload.
```

## Lệnh & Kỹ Năng Tích Hợp Sẵn

Các Agent hiểu các kỹ năng được cung cấp bởi registry. Thay vì viết shell script, chỉ cần bảo agent gọi công cụ:

- **`search_web`**: Bảo Research Agent (Phòng 13) tra cứu một chủ đề trên Google/Perplexity.
- **`run_tests`**: Bảo QA Agent (Phòng 02) xác minh một PR branch mới bằng pytest nội bộ.
- **`civ_intake`**: Kích hoạt Content Intake Pipeline để tiếp nhận PDF hoặc GitHub Repository.

### Luồng Công Việc Tùy Chỉnh
Nếu một agent không hoàn thành được tác vụ đa bước, hãy tạo luồng công việc cho họ trong `system/ops/workflows/` và bảo họ đọc trước khi thực thi.
