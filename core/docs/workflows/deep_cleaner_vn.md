---
id: deep-cleaner-vn
type: document
owner: SYSTEM
lang: vi
---

# Quy Trình Vệ Sinh Sâu OmniClaw

## Daemon OS-Level (Phòng 22 - Operations)

Deep Cleaner là bộ vệ sinh phần mềm cưỡng chế mạnh mẽ, tích hợp vào hệ điều hành OmniClaw. Nó hoạt động theo Kiến Trúc Zero-Trust để đảm bảo không có secret tạm thời, file cache treo, hoặc database mồ côi nào bị phơi lộ trong workspace.

[**🇬🇧 View in English**](deep_cleaner.md) | [**Quay về Mục Lục Docs**](../README-vn.md)

### Các Chức Năng Cốt Lõi

1. **Xóa SQLite & DB:** Hủy các cache `.sqlite` và database cache bị bỏ lại, trừ khi chúng được bảo vệ rõ ràng trong kiến trúc `/storage/vault/`.
2. **Xóa Dấu Vết Git:** Quét các Git repository bị lỗi, lock file, và bare-clone tình cờ.
3. **Xóa Cache Ảo:** Xóa các file `.cache` tạm thời trên toàn cây thư mục OS được tạo bởi Python, Node, LLM, hoặc browser MCP.
4. **Cắt Tỉa Log:** Lưu trữ hoặc xóa output log quá mức từ các agent (vd: Nova, Strix) để ngăn log phình to và vô tình ghi API key.

### Thực Thi

Để chạy thủ công Deep Cleaner daemon, thực thi script sau từ thư mục workspace gốc:

```ps1
python system/ops/scripts/omniclaw_deep_cleaner.py
```

### Khóa An Toàn

* **Bảo Vệ Vault:** Bộ dọn dẹp mặc nhiên bỏ qua đường dẫn `/storage/vault/`, tạo khóa bảo vệ tuyệt đối cho dữ liệu người dùng và file trạng thái bền vững.
* **Chủ Quyền Brain:** Dữ liệu lưu trữ trong `/brain/corp/` và `/brain/registry/` được xác minh so với `MASTER_INDEX.md` và không thể bị script này xóa, giữ cho OmniClaw thông minh và an toàn.
