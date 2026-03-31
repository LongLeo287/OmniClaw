<!-- DEPRECATED — This workflow has been superseded by the current OmniClaw ecosystem.
     Kept for historical reference only. DO NOT USE in active flows.
     See ecosystem/workflows/ for current versions.
-->

# Thẩm Mỹ Tối Thượng (Visual Excellence) - Chuẩn Apple HIG

BẤT CỨ KHI NÀO MỘT AGENT XÂY DỰNG GIAO DIỆN (UI/UX) CHO OMNICLAW HOẶC APP CHO SẾP, PHẢI TUÂN THỦ CÁC LUẬT THÉP SAU ĐÂY:

1. **Từ Chối Đơn Sắc Cổ Điển (Reject Generic Colors):**
   - TUYỆT ĐỐI CẤM dùng màu thuần (như `red`, `blue`, `#FF0000`, `bg-blue-500` cơ bản).
   - PHẢI sử dụng HSL Variables được tinh chỉnh (Ví dụ: `hsl(210, 80%, 45%)` cho Blue mượt).
   - PHẢI hỗ trợ Dark Mode và Light Mode với tỷ lệ tương phản chuẩn xác (WCAG AA). 

2. **Typography Tinh Tế (Premium Fonts):**
   - Cấm xài Font mặc định lởm khởm. Phải inject Google Fonts (`Inter`, `Outfit`, `SF Pro` style).
   - Phân cấp Heading mạch lạc: `<H1>` là King, chỉ có 1 `H1` duy nhất trên trang.
   - Khoảng trắng (Whitespace/Padding) là một thành phần thiết kế, Không phải chỗ trống! Hào phóng với `gap` và `padding`.

3. **Thiết Kế Động (Dynamic UI):**
   - Vạn vật đều phải phản hồi khi Chuột lướt qua (Hover States).
   - Các nút bấm phải có Micro-interactions (Nảy nhẹ, đổi bóng, phát sáng).

Nếu bạn code ra một cái Form hoặc Bảng trông như đồ bài tập về nhà của sinh viên năm nhất, bạn ĐÃ THẤT BẠI. Phải code cho khách hàng "WOW" ngay ánh nhìn đầu.
