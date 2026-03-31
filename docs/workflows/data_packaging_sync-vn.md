# Quy Trình Đóng Gói Lại & Đồng Bộ Dữ Liệu Lên Đám Mây (Packaging & Sync Workflow)

[**🇺🇸 Read English Version**](data_packaging_sync.md) | [**Wiki Reference**](https://github.com/LongLeo287/OmniClaw/wiki)

---

Đây là quy trình khép kín giúp sao lưu, đóng gói toàn bộ Bộ Nhớ, Trạng Thái Hoạt Động của OmniClaw và đẩy (Push) đồng thời lên 3 cao điểm đám mây: **HuggingFace**, **Google Drive** và **GitHub**. Tuân thủ quy trình này đảm bảo không làm gãy đường dẫn (Path errors) hoặc tải lên các tệp vượt quá kích thước (Git LFS limit).

---

## 1. Cơ Chế Bắn Tỉa (Targeted Data Push)
Để tránh nhồi nhét thư mục gốc vào Git hoặc làm cồng kềnh kho dữ liệu, hệ thống ưu tiên "Bắn Tỉa" các vùng trọng yếu thay vì sao chép toàn bộ.

Lõi sao lưu chịu trách nhiệm chính là Kịch bản Python:
**`system/ops/scripts/omniclaw_data_push.py`** 

Nó sẽ chỉ trích xuất và đẩy 3 tụ điểm dữ liệu lớn nhất của hệ thống:
1. `brain/memory/` (Ký ức dài hạn)
2. `storage/vault/` (Thư viện kho lưu trữ tài sản, dữ liệu thô)
3. `ecosystem/plugins/` (Mã nguồn Plugin & Agent bên thứ ba)

Hai tụ điểm tiếp nhận dữ liệu ngoại cỡ này là lõi **HuggingFace** Dataset và **Google Drive**.

> **⚠️ Cảnh Báo:** Tuyệt đối không đẩy (Push) các tệp tin lưu trữ thô (`.db`, `.sqlite`, `.webp`) hoặc các Thư viện Đại Khối của Storage (nhỏ hơn > 100MB) thẳng lên Github Repo chính (`main`) để tránh gặp lỗi "Git push pre-receive hook declined" do vi phạm giới hạn kích cỡ.

---

## 2. Quy Trình Bơm Lại Lõi (Targeted Data Pull)
Vì Github không chứa dữ liệu nặng, khi một Nhân sự mới tiến hành Clone (Kéo) source code về máy, các thư mục `storage/vault/` và `brain/memory/` của họ sẽ bị trống rỗng.
Để bơm lại toàn bộ số dữ liệu tịnh tiến này thẳng vào hệ thống, Sếp chỉ cần chạy lệnh:
**`python system/ops/scripts/omniclaw_data_pull.py`**

Script này sẽ sử dụng `snapshot_download` của HuggingFace và RClone của Google Drive để **hồi sinh nguyên trạng gốc** tải xuống và nén thẳng vào `d:/LongLeo/AI OS CORP/AI OS/...`. Nhờ vậy, cấu trúc liên kết nội bộ luôn liền mạch và không bao giờ bị đứt gãy.

---

## 3. Quy Trình Nén "Linh Hồn" (Backup Soul)
Trước khi commit mã nguồn lên GitHub, hệ thống quy định quản trị viên phải sao lưu "Tâm trí phiên làm việc" hiện tại.

**Script chạy:**
```bash
powershell -ExecutionPolicy Bypass -File system\ops\scripts\memory\backup_soul.ps1
```

**Hoạt động:**
1. Nó trích xuất tệp `.pb` phiên mã chat gần nhất của Người Vận Hành.
2. Nó hút toàn bộ tri thức trong thư mục `brain/` của ID hiện tại.
3. Toàn bộ tập dữ liệu não này được nén chặt thành file Zip tên: `soul_backup.zip`.
4. Sau khi nén thành công, tệp này nằm ngoan ngoãn trong môi trường an toàn. Lúc này Người Vận Hành mới được quyền đẩy lệnh Commit cuối cùng.

---

## 3. CI/CD: Xác Thực Tự Động (GitHub Actions)
Ngay khi Người Vận Hành thực hiện thao tác **Git Push** cuối cùng để tải cập nhật lên nhánh `main`, 2 Đội Cận Vệ (CI/CD Workflows) sẽ tự động được đánh thức bởi đám mây GitHub:

- **`.github/workflows/ai-os-tests.yml`:** Liên tục kiểm tra lỗi cú pháp (Lint) của mã nguồn Code (`.py`, `.js`), đồng thời xác thực xem sự bành trướng của hệ thống và việc thêm `docs/` mới có làm sập hệ thống (Crash Engine) hay không.
- **`.github/workflows/ai-os-validate.yml`:** Rà soát lại tất cả các siêu dữ liệu cấu hình như `SKILL_REGISTRY.json` và thuộc tính Agent YAML. Đảm bảo mọi Skill mới do AI Tự Viết đều đạt chuẩn định dạng mà không có dấu vân tay hay ID rác bị trùng lắp.

---

Mọi quy trình Đóng Gói Dữ Liệu và Push Code này cần được tuân theo nghiêm ngặt. Hệ sinh thái OmniClaw coi sự **Tính Toàn Vẹn** (System Integrity) là luật bất khả xâm phạm.
