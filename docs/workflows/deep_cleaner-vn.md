# Quy trình Tẩy Rác Hệ Thống (Deep Sanitation Workflow)

## Lá Chắn Chống Rò Rỉ OS-Level (Dept 22 - Operations)

Đạo quân Tẩy rác (Deep Cleaner) là cỗ máy vệ sinh nhẫn tâm nhất trong lòng Hệ Điều Hành OmniClaw. Nó vận hành chặt chẽ dưới Bộ Luật Zero-Trust để đảm bảo không một giọt rò rỉ mã Secret, bộ nhớ đệm Cache, hay Data Base cũ nào được lởn vởn trong Đảo Sandbox khi mọi chuyện đã xong.

### Sức mạnh cốt lõi lõi

1. **Trảm Rác SQLite:** Nó đè bẹp mọi Database `.sqlite` không nằm trong danh sách đăng ký Vùng An Toàn `storage/vault/`, giết sạch Database chạy rỗng khi app đóng cửa.
2. **Quét Sạch Bước Chân Git:** Gột rửa các ổ `bare-clone`, lock files, lỗi Git dẫm đạp lên nhau do Agent đẻ ra.
3. **Ghost Cache Clearing:** Bốc hơi hàng ngàn tệp Cache do Python (pycache), Node (node_modules chạc rễ sai chỗ), LLMs hay Trình Duyệt sinh ra sau một đêm chạy Tool rầm rầm.
4. **Log Trimming:** Bỏ Log rỗng, bào mỏng ổ cứng do Nova / Strix sủa bậy quá trớn. Cắt đứt rò rỉ Key API kẹt trong file Logs TXT.

### Kích hoạt bằng lệnh Thủ công

Để gõ lệnh và lôi tên quét rác này ra ngoài dọn dẹp, từ Thư mục Gốc của Đảo bạn hãy chạy:

```ps1
python system/ops/scripts/omniclaw_deep_cleaner.py
```

### Chốt An Toàn (Safety Interlocks)

* **Vén Màng Vault:** Dù có xả xui kinh như bão, kịch bản gốc này vẫn không bao giờ chạm một móng tay vào `storage/vault/` hay `brain/`. Đó là lệnh.
* **Brain Sovereignty:** Các file như `MASTER_INDEX` giúp Màng Kháng Cự của Não Bộ OS nhận diện Deep Cleaner và từ chối Quét Nhầm vào Trí tuệ của Tập Đoàn.
