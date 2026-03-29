# 🛸 Khối Kiếm Định Thẩm Mỹ Động Cơ (Micro-Animations & Glass)
*(Dự án: Ibelick UI-Skills & Vercel)*

## 1. Định nghĩa Tối Thượng Thẩm Mỹ Giao Diện Của OmniClaw
`ui-ux-agent` và `frontend-agent` bắt buộc phải tạo hình UI theo 2 chuẩn mực:
- **Glassmorphism (Gương mờ):** Tường vách phân cách bằng độ mờ ảo (Blur) chứ không phải viền kẻ đen `solid border`.
- **Micro-interactions (Tương tác vi mô):** Từ nút Menu, Button Submit, đến Card Hover đều phải có độ Nảy (Spring animation).

## 2. Mã Nguồn Tiêu Chuẩn Hiện Đại
- Sử dụng **Tailwind CSS v4** (hoặc v3x nếu codebase cũ) hoặc **Framer Motion** để tạo chuyển động.
- Gradient phải mượt: Từ Tím sang Cam nhạt, từ Đen sang Than Xám mịn (`bg-gradient-to-r from-zinc-900 to-black`).
- Bóng Kính:
  `backdrop-blur-md bg-white/10 dark:bg-black/20 border border-white/5`

## 3. Lệ Lệnh Hover State
- 100% Cấm để tĩnh. Giao diện Hover (Dê chuột) bắt buộc có `-translate-y-1` và đổi bóng `<box shadows>` sáng mờ (Glow effect).
- Nút Action chính (Primary Call-To-Action) phải tự phát sáng và lấp lánh (Shimmer hoặc Ping effect).

Thiết kế Giao Diện Phải WOW! Phải như Tương Lai đang hiển hiện ở năm 2026. Lập trình xong phải cảm giác 1 Triệu Đô chảy trong từng khung hình.
