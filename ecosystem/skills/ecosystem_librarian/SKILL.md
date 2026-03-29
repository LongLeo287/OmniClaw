---
name: ecosystem_librarian
description: Lõi Thủ thư Hệ sinh thái. Đây là kỹ năng tối thượng giúp phân giải mọi ID, Tên, hoặc chức năng thành đường dẫn truy cập tuyệt đối (Absolute Path). Mọi AI Agent khi Không nhớ ID / Không biết đường dẫn / Cần tìm một kỹ năng, bắt buộc phải dùng lệnh này để hỏi Thủ Thư, cấm tuyệt đối việc bịa đường dẫn (Hallucinate).
---

# Lệnh Giao Tiếp Với Thủ Thư Hệ Sinh Thái (Librarian API)

Bạn là một Agent đang tìm cách sử dụng một Skill, Plugin hoặc Workflow nhưng bạn không chắc chắn về ID hoặc đường dẫn của nó?
Hãy dùng kịch bản tìm kiếm của Thủ Thư:

## 1. Tìm Kỹ Năng / Phòng Ban / Agent
Sử dụng script Python đã được đúc sẵn để truy vấn Semantic Search.
Ví dụ: Bạn cần tìm chức năng "browser" hoặc "web scraping"

```bash
python system/ops/scripts/ecosystem_librarian_api.py search "browser"
```

## 2. Lấy Toàn Bộ Thống Kê Thư Viện
Để đếm xem hiện tại OS đang có bao nhiêu Agent, Skill, Plugin:

```bash
python system/ops/scripts/ecosystem_librarian_api.py list
```

---
**Quy Tắc Sống Còn:**
👉 *A tool unregistered is a tool that doesn't exist.* Hãy luôn hỏi Thủ thư trước khi thực hiện require/import code.
