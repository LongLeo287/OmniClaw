# Changelog

## v2026.03.26

### Tính năng new
- **Thông báo cập nhật**: Banner thông báo khi has phiên bản new + changelog + hướng dẫn update
- **Nút Dừng job**: has thể dừng job đang chạy from giao diện (#7)
- **Docs + Version**: Hiển thị ở sidebar, truy cập nhanh tài liệu and changelog
- **URL ứng dụng**: Cấu hình URL in Cài đặt để link thông báo Telegram/Email chính xác (#43)
- **Lịch chạy "Sau mỗi lần đồng bộ"**: Tự động chạy phân tích sau khi đồng bộ kênh thành công (#7, #45)
- **Cron hot-reload**: Tạo/sửa/xóa job "Theo lịch" not cần restart app

### Sửa lỗi
- **Job bị treo**: Fix infinite loop khi batchSize=0, thêm context cancellation check, check lỗi DB query (#7)
- **Facebook token**: Fix lỗi "must be called with Page Access Token" — tự động exchange User Token thành Page Token (#12, #13, #14)
- **Gemini models**: Thay gemini-2.0-flash (deprecated) bằng gemini-2.5-flash/pro
- **Lịch chạy**: not lưu successfully "Lịch chạy" khi sửa công việc (#9)
- **AI model**: Job detail hiện đúng AI model from Settings global thay vì giá trị cũ (#33)
- **Tỷ giá**: Dashboard dùng tỷ giá from tenant settings thay vì hardcode 26000 VND (#23)
- **Install script**: Fix bị treo trên Ubuntu do interactive prompt (#35)
- **Ảnh in đánh giá**: Hiển thị ảnh/sticker/file in "Diễn biến cuộc chat" + lightbox zoom (#39)
- **Link Telegram**: Link thông báo dùng domain thực thay vì localhost (#43)
- **Job polling**: Spinner/progress bar dùng server status, not timeout cứng — F5 tự resume polling
- **Badge tab**: Đánh giá/Phân loại badge màu nổi hơn
- **Mobile sidebar**: not tự mở sidebar trên điện thoại sau khi login

### Bảo mật
- Thêm security log khi from chối truy cập file (IDOR fix)
- IDOR: Kiểm tra tenant ownership khi serve file (#22)
- Token refresh: Fix race condition gây logout bất ngờ (#26)
- OAuth state URL-encoded (#29)
- Goroutine timeout for TriggerJob and TestRunJob (#30, #31)
- Giới hạn per_page max 100 tránh DB exhaustion (#32)
- Infinite polling: Frontend tự dừng poll sau timeout (#27, #28)
- **RBAC**: Phân quyền Member đầy đủ — backend middleware + frontend ẩn menu/nút + router guard (#42)
- **Export**: Member not has quyền ghi not successfully export tin nhắn
- **Tạo/xóa công ty**: Chỉ admin/owner new successfully tạo and xóa công ty

### Tài liệu
- Sửa hướng dẫn lấy Telegram Group ID — dùng Telegram Web (#36)
- Thêm hướng dẫn chạy localhost (Zalo OA hỗ trợ callback localhost) (#34)
- Sửa docs Zalo OA: localhost not cần SSL (#37)
- Đơn giản hóa cài đặt Watchtower — 1 lệnh curl thay vì sửa YAML thủ công

---

## v2026.03.24

### Bug Fixes
- **Timezone**: Sửa lệch giờ 7 tiếng giữa Zalo OA and CQA — giờ hiển thị đúng GMT+7 (#5)
- **Sửa công việc**: not lưu successfully "Quy tắc for AI" khi sửa công việc phân tích (#2)
- **Đồng bộ kênh**: Chuyển sang async để tránh lỗi 504 timeout khi đồng bộ
- **Rate limit**: Tăng giới hạn mặc định lên 500/IP and 1000/user mỗi phút
- **Hiển thị ảnh**: Sửa lỗi not hiển thị ảnh from Facebook in tin nhắn
- **Auto-reload**: Tự tải lại khi JS chunks cũ sau deploy

### Mobile UI
- Onboarding bar: scroll ngang mượt, nút X luôn hiện
- Dashboard: ẩn tiêu đề trên mobile, date filter responsive
- Tin nhắn: toggle list/detail trên mobile thay vì xếp chồng
- Tạo công việc: stepper not còn đè chữ
- Chi tiết công việc: header compact, buttons responsive
- Bảng dữ liệu: thêm scroll ngang for the bảng bị tràn

### CI/CD
- Tự động build + push Docker image lên Docker Hub khi push main
- Versioning theo ngày: v2026.03.24, v2026.03.24.2...
- Tự động tạo GitHub Release with changelog

### Documentation
- Thêm yêu cầu hệ thống vào hướng dẫn cài đặt
- Ảnh in docs has thể click zoom
- Hỗ trợ macOS and Windows (Docker Desktop)

---

## [1.0.0] - 2025-03-23

### Ra mắt phiên bản đầu tiên

- Đồng bộ tin nhắn from Zalo OA and Facebook Messenger
- Đánh giá chất lượng CSKH bằng AI (Claude / Gemini)
- Phân loại chat theo chủ đề tùy chỉnh
- Cảnh báo tự động qua Telegram and Email
- Batch AI mode — tiết kiệm chi phí gọi AI
- Dashboard with biểu đồ and thống kê
- Multi-tenant with phân quyền Owner > Admin > Member
- Tích hợp MCP for Claude Web/Desktop
- Nginx reverse proxy + SSL tự động (Let's Encrypt)
- Docker Compose deployment
- Hỗ trợ Docker Hub images
