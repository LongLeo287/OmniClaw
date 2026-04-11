---
id: visual-excellence
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:32:41.300623
---

<!-- DEPRECATED — This workflow has been superseded by the current OmniClaw ecosystem.
     Kept for historical reference only. DO NOT USE in active flows.
     See ecosystem/workflows/ for current versions.
-->

# Thẩm Mỹ Tối Thượng (Visual Excellence) - Chuẩn Apple HIG

BẤT CỨ KHI NÀO a AGENT XY DỰNG GIAO DIỆN (UI/UX) for OMNICLAW HOẶC APP for SẾP, must TUN THỦ the LUẬT THÉP SAU ĐY:

1. **from Chối Đơn Sắc Cổ Điển (Reject Generic Colors):**
   - TUYỆT ĐỐI CẤM dùng màu thuần (như `red`, `blue`, `#FF0000`, `bg-blue-500` cơ bản).
   - must sử dụng HSL Variables successfully tinh chỉnh (Example: `hsl(210, 80%, 45%)` for Blue mượt).
   - must hỗ trợ Dark Mode and Light Mode with tỷ lệ tương phản chuẩn xác (WCAG AA). 

2. **Typography Tinh Tế (Premium Fonts):**
   - Cấm xài Font mặc định lởm khởm. must inject Google Fonts (`Inter`, `Outfit`, `SF Pro` style).
   - Phân cấp Heading mạch lạc: `<H1>` is King, chỉ has 1 `H1` duy nhất trên trang.
   - Khoảng trắng (Whitespace/Padding) is a thành phần thiết kế, not must chỗ trống! Hào phóng with `gap` and `padding`.

3. **Thiết Kế Động (Dynamic UI):**
   - Vạn vật đều must phản hồi khi Chuột lướt qua (Hover States).
   - the nút bấm must has Micro-interactions (Nảy nhẹ, đổi bóng, phát sáng).

Nếu bạn code ra a cái Form hoặc Bảng trông như đồ bài tập về nhà of sinh viên năm nhất, bạn ĐàTHẤT BẠI. must code for khách hàng "WOW" ngay ánh nhìn đầu.
