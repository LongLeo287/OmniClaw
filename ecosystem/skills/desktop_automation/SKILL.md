---
name: desktop_automation
description: Điều khiển Giao diện Máy Tính Cục bộ (Computer Use).
---

# Desktop Automation Skill
**Nguồn Gốc:** Trích xuất từ kho chứa Awesome-Agent-Skills (PyAutoGUI / Computer-Use API).

## Mô tả (Description)
Thay vì làm việc thông qua API hay Terminal tĩnh, Agent có thể "nhìn thấy" Màn hình của Hệ điều hành, định vị Icon (Pixel Match), Di chuột (Mouse Move) và Gõ Phím (Keystrokes) như con người.

## Hướng dẫn sử dụng (Usage)
- Các Agent thuộc nhóm `ui-ux-agent` hoặc `qa-tester` gọi Kỹ năng này bật ứng dụng, bấm nút X, Y, Z để Verify Luồng đồ họa (VD: Test App Unity, Unreal, Android Emulator).
- Sử dụng Module `pyautogui` hoặc `playwright`.

## Luật cấm (Restrictions)
1. **Kiểm duyệt Sếp:** Mọi thao tác click chuột / phím tự động bắt buộc phải bật Mode "Xác nhận từng bước" nếu vượt quá 10 cú Click.
2. Không mở Thư mục Cấp cao (Windows Boot / System32).
