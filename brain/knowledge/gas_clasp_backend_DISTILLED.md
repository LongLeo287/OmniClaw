---
title: "No-DB Serverless Backend with Google Apps Script (GAS) & Clasp"
description: "Kiến trúc sử dụng Google Sheets làm Master Database cho ứng dụng React, kết hợp với công cụ Clasp để tự động cấu hình và CI/CD tự động."
tags: ["architecture", "google-apps-script", "backend", "clasp", "no-db", "serverless"]
related_projects: ["Tiem_Nuoc_Nho_v5"]
---

# Kiến trúc No-DB Serverless: React + GAS + Clasp

Mô hình kiến trúc độc đáo bứt phá khỏi Database truyền thống (PostgreSQL/Supabase) để tận dụng **Google Sheets** như một Database Relational Realtime miễn phí. Rất phù hợp cho các dự án SME, POS, hoặc internal tools nơi khách hàng đã quen với giao diện Google Sheets.

## 1. Thành phần Cốt lõi

- **Google Sheets:** Đóng vai trò là Master Database. Mỗi Sheet là một table (VD: `Danh sách món`, `Đơn hàng`, `Sổ tay`).
- **Google Apps Script (GAS):** Đóng vai trò HTTP API Backend. Hàm `doGet(e)` và `doPost(e)` xử lý routing, parse data và tương tác với Sheets thông qua `SpreadsheetApp`.
- **Clasp (`@google/clasp`):** Công cụ CLI của Google, lưu trữ code của GAS dưới local (Tập tin `.js`/`.ts` lưu trong thư mục `/gas`). Cung cấp khả năng CI/CD:
  - `clasp push`: Cập nhật code lên Cloud.
  - `clasp deploy`: Tạo trực tiếp các bản phát hành (Deployment) sinh ra URL Web App.
- **Vite/React Client:** Ứng dụng Frontend fetch dữ liệu thẳng đến `EXEC_URL` sinh ra từ bản deploy của biểu mẫu web.

## 2. Ưu điểm & Thách thức

### Ưu điểm:
- **Zero Cost:** Miễn phí Server, CSDL, không giới hạn dung lượng truy vấn cơ bản.
- **Khả năng quan sát (Observability):** Admin/Chủ cửa hàng có thể xem/chỉnh sửa DB ngay trên giao diện Spreadsheet cực kỳ trực quan và quen thuộc.
- **Code cục bộ:** Sử dụng `clasp` cho phép code backend trên VSCode/Cursor với autocomplete, chia nhỏ file thay vì gõ trên IDE web của Google.

### Thách thức (Những Lỗi Thường Gặp):
> [!WARNING]
> **Tử huyệt CORS (Net::ERR_FAILED / Failed to fetch)**
> Google Apps Script bắt buộc phải được `Deploy as Web App` với cài đặt:
> - **Execute as:** `USER_DEPLOYING` (bản thân người lập trình/chủ DB)
> - **Who has access:** `ANYONE_ANONYMOUS` (Bất kỳ ai).
> 
> Nếu vô tình khóa quyền truy cập xuống "Only Me", trình duyệt sẽ bị yêu cầu redirect về trang Login Google. Vercel/Localhost gọi API bằng AJAX `fetch` sẽ bị dội lại bằng lỗi **CORS No Access-Control-Allow-Origin**.

## 3. Workflow Vận Hành Tự Động (Auto-Deploy)

Các Agent (như OmniClaw) có thể cập nhật Backend Google Script cho người dùng hoàn toàn bằng Terminal:
```bash
cd gas
# Push code mới lên
npx @google/clasp push
# Bấm nút kích hoạt version mới sinh ra URL
npx @google/clasp deploy
```
*Lưu ý:* Cập nhật URL được sinh ra (bắt đầu bằng `AKfy...`) vào `<App.tsx>` hoặc `.env` để Frontend fetch đúng API.

## 4. Cơ chế Front-end Fetching

Dưới front-end (VD: `DataContext.tsx`), bắt buộc phải xử lý cấu trúc JSON và Retry:
```javascript
// GET (Đọc dữ liệu) -> Thường được redirect sang domain googleusercontent.com
fetch(`${appsScriptUrl}?action=getMenu`)
  .then(res => res.json())
  
// POST (Ghi dữ liệu) -> Phải truyền body dạng JSON text.
const GAS_POST_HEADERS = { 'Content-Type': 'text/plain;charset=utf-8' };
fetch(appsScriptUrl, {
  method: 'POST',
  headers: GAS_POST_HEADERS, // Lưu ý: 'text/plain' thay vì 'application/json' để tránh Preflight CORS lỗi
  body: JSON.stringify({ action: 'createOrder', order: data }),
  redirect: 'follow'
})
```
Sử dụng `text/plain` cho POST request là kỹ thuật quan trọng để né cấu hình CORS khắt khe của Google Apps Script đối với `application/json`. Dưới GAS (`doPost(e)`), code sẽ gọi `JSON.parse(e.postData.contents)` để lấy object.
