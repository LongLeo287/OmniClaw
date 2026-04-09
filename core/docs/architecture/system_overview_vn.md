---
id: system-overview-vn
type: document
owner: SYSTEM
lang: vi
---

# 🏛️ Tổng Quan Hệ Thống (Kiến Trúc 28 Phòng Ban)

OmniClaw vận hành giống hệt một tập đoàn kỹ thuật số, bao gồm **28 "Phòng Ban" cấu trúc riêng biệt** được quản lý bởi các AI Agent hoạt động phối hợp thông qua các luồng đa tác nhân.

[**🇬🇧 View in English**](system_overview.md) | [**Quay về Mục Lục Docs**](../README-vn.md) | [**📚 Wiki**](https://github.com/LongLeo287/OmniClaw/wiki)

---

## 1. Phân Cấp Thực Thi

Kiến trúc của chúng ta dựa trên luồng truyền tải từ trên xuống dưới nghiêm ngặt, đảm bảo các quyết định và ranh giới an toàn được kế thừa hoàn hảo.

1. **CEO (Tầng 0)**: Người vận hành (Bạn). Cung cấp lệnh chiến lược cấp cao.
2. **Orchestrator / C-Suite (Tầng 1)**: Các mô hình Agent chủ (vd: Antigravity). Tiếp nhận lệnh phức tạp, định tuyến luồng công việc, xử lý phân tích sâu.
3. **Trưởng Phòng Ban (Tầng 2)**: Các LLM Agent chuyên biệt bị ràng buộc bởi `rules/` riêng (vd: QA Manager, Frontend Engineer, CIV Chief).
4. **Subagent Tác Vụ (Tầng 3)**: Các Agent chuyên biệt tạm thời sinh ra để thực thi logic mục tiêu (vd: git-protector, doc-parser) và hủy sau khi hoàn thành.

## 2. Tứ Đại Trụ Cột Lực Lượng Lao Động

Cấu trúc file trong `ecosystem/workforce/` phân chia tổ chức AI thành bốn ranh giới tuyệt đối:
- **`agents/`**: Chứa 116 Đặc vụ tự trị độc lập.
- **`subagents/`**: Chứa 37 Chuyên viên tác vụ tạm thời.
- **`departments/`**: Phân nhóm 28 Phòng ban theo chuỗi chỉ huy.
- **`system/`**: Vùng Cấu Hình Tĩnh — nghiêm cấm code thực thi. Chứa khuôn mẫu prompt toàn cục (`corp_prompts/`) và sổ đăng ký Daemon (`daemons/`).

## 3. Trạng Thái AI Chia Sẻ

Tất cả các thành phần tự trị được liên kết qua Bộ Nhớ Nội Bộ (`brain/`):

- **`blackboard.json`**: Trạng thái tác vụ đồng bộ đang hoạt động. Nếu Agent A hoàn thành một tính năng, nó cập nhật blackboard để Agent B (QA Testing) tự động biết đã đến lúc chạy kiểm thử.
- **RAG & Cơ Sở Tri Thức**: Thư mục lưu trữ dựa trên graph-DB (`brain/knowledge`) chứa các kiến thức được kiểm duyệt và tham chiếu thư viện bên ngoài.

## 4. Các Phòng Ban Cốt Lõi Hàng Đầu

Trong số 28 Phòng Ban, một số nút quan trọng nổi bật:
- **Phòng 01 (Engineering)**: Xây dựng tính năng, sửa code, viết kiểm thử.
- **Phòng 10 (Strix Security)**: Kiểm duyệt plugin, xem xét payload, chặn các chỉnh sửa trái phép (Zero Trust).
- **Phòng 20 (CIV - Content Intake)**: Tiếp nhận GitHub repo, PDF, tài liệu web và tóm tắt cho Graph Local Memory.
- **Phòng 22 (Operations)**: Tự động hóa đường dẫn git sync, hook sao lưu và quy trình deep cleaner.

> *Để biết ánh xạ JSON dành cho máy đọc, AI tham chiếu `brain/corp/org_chart.yaml` và `AGENTS.md`.*
