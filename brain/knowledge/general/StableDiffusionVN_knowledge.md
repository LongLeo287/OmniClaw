---
id: stablediffusionvn-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:16.855583
---

# KNOWLEDGE EXTRACT: StableDiffusionVN
> **Extracted on:** 2026-03-30 17:54:06
> **Source:** StableDiffusionVN

---

## File: `sdvn_apix_python.md`
```markdown
# 📦 StableDiffusionVN/sdvn_apix_python [🔖 PENDING/APPROVE]
🔗 https://github.com/StableDiffusionVN/sdvn_apix_python


## Meta
- **Stars:** ⭐ 32 | **Forks:** 🍴 22
- **Language:** JavaScript | **License:** Unknown
- **Last updated:** 2026-02-27
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
apix - SDVN Banana Pro

## README (trích đầu)
```
# aPix Image Workspace

## Tiếng Việt
### Giới thiệu
aPix Image Workspace là một giao diện Flask nhẹ giúp bạn tạo hình ảnh bằng API Model Gemini Image 3 Pro (Nano Banana Pro). Bạn có thể gửi prompt, upload tài liệu tham khảo và điều chỉnh tỷ lệ khung hình/độ phân giải.

![Preview](./preview.jpeg)

### Người tạo
- Người tạo: [Phạm Hưng](https://www.facebook.com/phamhungd/)
- Group: [SDVN - Cộng đồng AI Art](https://www.facebook.com/groups/stablediffusion.vn/)
- Website: [sdvn.vn](https://www.sdvn.vn)
- Donate: [sdvn.vn/donate](https://stablediffusion.vn/donate/)

### Khởi chạy nhanh bằng `run_app`
1. Nháy đúp vào `run_app.command` trên macOS, `run_app.sh` trên Linux, hoặc `run_app.bat` trên Windows để tự động tìm Python, tạo `.venv`, cài `requirements.txt` và khởi động `app.py`.
2. Mở `http://127.0.0.1:8888`, nhập prompt/tùy chọn rồi nhấn Generate.
3. Hình ảnh mới nằm trong `static/generated/`; `/gallery` thể hiện lịch sử.

### Sử dụng
1. Đặt biến môi trường `GOOGLE_API_KEY` với API key của Google GenAI hoặc nhập trực tiếp trong giao diện.
2. Mở trình duyệt tới `http://127.0.0.1:8888`, nhập prompt, chọn tùy chọn và nhấn Generate.  
3. Hình ảnh: `static/generated` lưu nội dung mới nhất, còn `/gallery` trả về URL cho phần lịch sử.

### Cú pháp đặc biệt
Ứng dụng hỗ trợ cú pháp placeholder để tạo nhiều biến thể ảnh hoặc thay thế nội dung linh hoạt:

*   **Placeholder:** Sử dụng `{text}` hoặc `[text]` trong prompt. Example: `A photo of a {animal} in the style of {style}`.
*   **Trường Note:** Nội dung trong trường Note sẽ thay thế cho placeholder:
    *   **Thay thế đơn:** Nếu Note là `cat`, prompt sẽ thành `A photo of a cat...`.
    *   **Hàng đợi (Queue):** Nếu Note chứa ký tự `|` (Example: `cat|dog|bird`), ứng dụng sẽ tự động tạo 3 ảnh lần lượt với `cat`, `dog`, và `bird`.
    *   **Nhiều dòng:** Nếu Note có nhiều dòng, mỗi dòng sẽ ứng với một lần tạo ảnh.
    *   **Mặc định:** Nếu Note để trống, placeholder sẽ giữ nguyên hoặc dùng giá trị mặc định nếu có (Example: `{cat|dog}` sẽ tạo 2 ảnh nếu Note trống).

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

