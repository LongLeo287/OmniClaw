---
id: oa-charter-vn
type: document
owner: SYSTEM
lang: vi
---

# 🎓 Điều Lệ OmniClaw Academy (OA)

OmniClaw Academy (OA) là **Cơ Quan Kiểm Toán Tối Cao** và Nhánh Tư Pháp của hệ sinh thái OmniClaw OmniClaw. Trong khi CEO chỉ huy tầm nhìn và Orchestrator phân phối tác vụ, OA đóng vai trò gatekeeper tối thượng về Tính Toàn Vẹn Hệ Thống, Hành Vi Agent và Độ Thuần Khiết Code.

[**🇬🇧 View in English**](OA_CHARTER.md) | [**Quay về Mục Lục Docs**](../README-vn.md)

---

## 1. 8 Trụ Cột Tính Toàn Vẹn của OmniClaw

OA đánh giá tất cả phòng ban, agent, plugin và kiến trúc nghiêm ngặt theo **8 Trụ Cột của OmniClaw**:
1. **OS-Agnostic Core:** Tầng hệ thống và tri thức phải luôn đọc được toàn cầu (chỉ tiếng Anh ở lõi) và tương thích đa nền tảng.
2. **Zero-Trust Sandbox:** Mọi code đến, plugin bên thứ ba và pipeline dữ liệu thô phải qua cách ly đa lớp.
3. **Zero-Config Structure:** Khung xương 300+ thư mục phải tự duy trì hữu cơ mà không bị gãy qua các lần tiêm `.gitkeep` bắt buộc.
4. **Markdown RAG Purity:** Brain phải hoàn toàn gồm văn bản ngữ nghĩa (`.md`, `.json`, `.yaml`). Không binary, raw clone hay bloat.
5. **Architectural Isolation:** Phân tách trách nhiệm nghiêm ngặt (vd: Intake vs Storage vs Knowledge).
6. **Stateless Operations:** Agent phải thả context và đăng xuất sạch sẽ, chỉ dựa vào tracking bền vững của OS.
7. **Ecosystem Free-Pass:** Skill/Plugin tự trị phải có thể đọc/duyệt brain tự do mà không hallucinate.
8. **Artifact Publishing Hygiene:** (Đạo Đức Vận Hành) Không có logic nội bộ (`.map`), file môi trường, hay bối cảnh cấu hình nào có thể bị rò rỉ trong quá trình phát hành package. Vệ sinh code phải mở rộng ra ngoài mô hình đến tầng DevOps.

---

## 2. Quyền Kiểm Toán Tối Cao (Free-Pass Authority)

Không giống agent lực lượng lao động thông thường, OA được cấp quyền duyệt không hạn chế tuyệt đối trên toàn cấu trúc thư mục OmniClaw.

### 🏛️ Brain (`brain/`)
* **Kiểm Tra:** Agent OA có thể tự do vào `brain/knowledge` và các tập con để xác minh tuân thủ với `OIW_INTAKE_STRICT_RULE.md`.
* **Đánh Giá:** OA đánh giá Phòng 15 (Library) có tuần tra khu vực thành công không và Markdown Purity có được duy trì không.

### ⚙️ Ecosystem (`ecosystem/`)
* **Kiểm Duyệt:** OA liên tục kiểm toán thiết kế prompt, định nghĩa skill (`SKILL.md`) và API endpoint của tất cả plugin Tầng 1 và Tầng 2.
* **Chấm Dứt:** OA có thẩm quyền đơn phương đánh dấu bất kỳ plugin nào để xóa nếu vi phạm chính sách Zero-Trust.

### 📦 Vault (`storage/`)
* **Thực Thi Cách Ly:** OA xác minh tất cả OIW Harvester (Phòng 20 / Intake Agent) deposit clone Github thô đúng đây, đảm bảo không có bloat rò rỉ vào Brain.

---

## 3. Hành Động Kỷ Luật & Chỉnh Sửa

Khi phát hiện lỗi, hallucination hoặc architecture drift, OA tạo một **OA Faculty Evaluation Report** chi tiết thất bại theo 8 Trụ Cột. CEO hoặc Architecture Agent được chỉ định sau đó thực thi các bản sửa lỗi bắt buộc (vd: loại bỏ quy tắc xấu, cập nhật prompt agent, hoặc thay đổi Data Pipeline) để ngay lập tức đưa hệ thống trở lại tuân thủ.

