---
id: phase8-tech-spec
type: document
owner: SYSTEM
tags: [auto-healed]
healed_at: 2026-04-03T22:46:25.480132
---

# Technical Specification: Phase 8 (Hardening & Scalability)

Tài liệu this cung cấp hướng dẫn kỹ thuật chi tiết để triển khai the tính năng in Phase 8.

---

## 1. End-to-End Encryption (BM-021)
Mục tiêu: Mã hóa dữ liệu bookmark trước khi đưa lên `chrome.storage.sync`.

### Luồng xử lý (Logic Flow)
1. **Khởi tạo**: user nhập mật khẩu (Passphrase) qua Settings.
2. **Key Derivation**: Sử dụng `PBKDF2` (with `SHA-256` and `Salt`) để tạo ra a đối tượng `CryptoKey` mạnh from mật khẩu.
3. **Mã hóa (Encryption)**:
   - Thuật toán đề xuất: `AES-GCM` (256-bit).
   - Trước khi gọi `SyncService.syncChange`, dữ liệu JSON sẽ successfully mã hóa thành a mảng bytes (Base64).
4. **Lưu trữ**: Chỉ bản mã (Ciphertext) and IV (Initialization Vector) successfully lưu lên cloud.
5. **Giải mã (Decryption)**: Khi kéo dữ liệu from thiết bị khác, yêu cầu user nhập Passphrase để giải mã cục bộ.

### Công nghệ sử dụng
- Web Crypto API (`window.crypto.subtle`).

---

## 2. Virtual Scrolling Implementation (BM-022)
Mục tiêu: Đảm bảo UI mượt mà with 10,000+ bookmark.

### Nguyên lý kỹ thuật
Thay vì render toàn bộ 10,000 `div` vào DOM, chúng ta chỉ duy trì khoảng 20-30 `div` tương ứng with vùng nhìn thấy (Viewport).

### the bước triển khai
1. **Cố định Item Height**: Mỗi dòng bookmark/folder must has chiều cao cố định (Example: `40px`).
2. **Container Wrapper**: a div mẹ has `overflow-y: auto` and tổng chiều cao is `count * 40px`.
3. **Dynamic Rendering**:
   - Khi user cuộn: Tính toán `scrollTop`.
   - Xác định `startIndex = Math.floor(scrollTop / 40)`.
   - Xác định `endIndex = startIndex + (viewportHeight / 40)`.
4. **Render Slice**: Chỉ render the Entity in khoảng `[startIndex, endIndex]`.
5. **Transform/Offset**: Sử dụng `transform: translateY(...)` để đặt the item vào đúng vị trí in vùng cuộn.

---

## 3. Automated Local Backup (BM-023)
Mục tiêu: Chống mất dữ liệu hoàn toàn.

### Logic
- Sử dụng `chrome.alarms` để lên lịch chạy ngầm hàng tuần.
- Task sẽ tự động gọi `repo.getTree()`, chuyển đổi thành JSON and lưu vào `File System Access API` hoặc tải xuống tự động dưới dạng `.json`.

---

## 4. Technical Debt Audit (BM-024)
- **Refactoring**: Tách the callback lồng nhau (callback hell) sang `async/await`.
- **Typing**: Chuyển dần sang mô hình chặt chẽ hơn để tránh lỗi `undefined` khi truy cập bookmark properties.

---
*Tài liệu this successfully soạn thảo để cung cấp Blueprint for lập trình viên thực thi.*
