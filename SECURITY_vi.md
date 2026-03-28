# 🔒 Chính Sách Bảo Mật (Security Policy) của AI OS CORP

*This page is available in [English](SECURITY.md).*

> **"Mã Nguồn là Luật. Bảo Mật là Sinh Mệnh."**
> — THE AI OS ZERO-TRUST DIRECTIVE

Hệ sinh thái AI OS CORP vận hành dựa trên **Kiến Trúc ZERO-TRUST (Cấm Tin Tưởng Tuyệt Đối) Nghiêm Ngặt**. Chúng tôi coi vấn đề an ninh của hệ thống là ưu tiên số một và luôn trân trọng các báo cáo lỗ hổng có trách nhiệm.

---

## 🟢 Các Phiên Bản Được Hỗ Trợ (Supported Versions)

Hiện tại, chúng tôi chỉ cung cấp các bản Vá bảo mật độc quyền cho Lõi chính (Leading edge):

| Version (Phiên bản) | Supported (Hỗ trợ) |
| --- | --- |
| `main` | ✅ |
| `<= 11.x.x` | ❌ |

*(Lưu ý: Chúng tôi chỉ tiến hành vá lỗi trên nhánh `main`. Các bản clone nguyên khối cũ hơn đã bị phế truất và buộc phải cập nhật lên commit mới nhất).*

---

## 🚨 Báo Cáo Lỗ Hổng (Reporting a Vulnerability)

**CẤM TUYỆT ĐỐI MỞ BÁO CÁO CÔNG KHAI KHI PHÁT HIỆN LỖ HỔNG (EXPLOIT)!**

Nếu Sếp/Kỹ sư phát hiện thấy một lỗ hổng trọng yếu, sự cố rò rỉ mã API Key, hay một Agent nào đó bị hack (Lỗi thực thi mã tùy ý - RCE), lộ lọt qua cổng kiểm duyệt CIV, xin hãy báo cáo bí mật ngay lập tức:

1. **Email/Kênh riêng:** [Gửi thông báo khẩn cấp trực tiếp cho CEO hoặc Quản Lý Trọng Yếu qua Kênh Mật]
2. **GitHub Security Advisories:** Click thẳng vào nút "Report a vulnerability" (Báo cáo Lỗ hổng) ngay trên tab Security của Github dự án.

Chúng tôi sẽ có cảnh báo xác nhận trong vòng 48h và cùng phối hợp để mô phỏng, Vá Lỗi (Patch), sau đó tung Bản Cập Nhật Nóng (Hotfix) trước khi lỗi đó bị tiết lộ ra công chúng.

---

## 🛡️ Cách Báo Cáo Chuẩn Chuyên Nghiệp (Best Practices)

Trong Đơn khiếu nại bảo mật, vui lòng mang theo:

* Mô tả cụ thể Lỗ hổng là gì và mức độ Càn quét (Impact) của nó.
* Khai rõ Thực Thể Agent (ví dụ: Nova, Strix, Antigravity), Tool, Workflow, hay Skill nào là thủ phạm gây rò rỉ.
* Các bước chi tiết từ A-Z hoặc Bản Diễn Tập Chứng Minh (Proof of Concept - PoC) để các kỹ sư có thể giả lập lại lỗi trong môi trường Cách ly ảo (Sandbox).

Tập đoàn AI OS xin cảm tạ nhữg nỗ lực của bạn trong việc rào chắn cho Hệ Điều Hành bất khả xâm phạm!
