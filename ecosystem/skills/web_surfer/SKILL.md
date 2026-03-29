---
name: web_surfer
description: Kỹ năng Duyệt web sâu (Deep Web Surfing) cho Agent.
---

# Web Surfer Skill
**Nguồn Gốc:** Trích xuất từ kho chứa Awesome-Agent-Skills.

## Mô tả (Description)
Cấp quyền cho Sub-Agent gọi công cụ trình duyệt (như Puppeteer, Playwright hoặc MCP Browser) để tra cứu web mở thay vì chỉ dựa vào dữ liệu huấn luyện.

## Hướng dẫn sử dụng (Usage)
- Khi prompt yêu cầu "Tìm hiểu...", Agent tự động parse Keyword và gọi `Browser_Tool`.
- Khả năng đọc DOM HTML và biến đổi thành cấu trúc Markdown sạch.

## Quy tắc (Rules)
1. **Lọc Quảng cáo:** Sẽ bị chặn ở các URL chứa spam hoặc cờ cờ bạc, chỉ truy cập Wikipedia, Docs chính thống, Github, StackOverflow.
2. **Không Click Sâu (Max Depth 2):** Chỉ ấn sang Link trang trong, không ấn tiếp tầng thứ 3 để tránh vòng lặp chết (Infinite Loop).
