---
id: arinnem-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:18:50.554893
---

# KNOWLEDGE EXTRACT: arinnem
> **Extracted on:** 2026-03-30 17:29:10
> **Source:** arinnem

---

## File: `stitchSkill.md`
```markdown
# 📦 arinnem/stitchSkill [🔖 PENDING/APPROVE]
🔗 https://github.com/arinnem/stitchSkill


## Meta
- **Stars:** ⭐ 17 | **Forks:** 🍴 1
- **Language:** JavaScript | **License:** Unknown
- **Last updated:** 2026-03-23
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
(No description)

## README (trích đầu)
```
# 🧩 Stitch Wireframe Generator — Antigravity Skill

> AI đọc tài liệu Description: phần mềm → lên kế hoạch toàn bộ màn hình → xây dựng prompt có context đầy đủ → tự động vẽ wireframe qua Google Stitch.

Một skill cho [Antigravity](https://code.google.com/assist/) giúp tự động hóa quy trình vẽ wireframe qua Google Stitch MCP. Thay vì ngồi tạo từng screen thủ công, để AI agent xử lý toàn bộ pipeline — từ phân tích tài liệu đến vẽ hệ thống hoàn chỉnh.

---

## 🤔 Problem:

Có hai cách vẽ wireframe với Google Stitch, và cả hai đều có hạn chế:

**Cách 1 — Upload tài liệu trực tiếp lên Stitch:**
Stitch đọc toàn bộ file, hiểu hệ thống, rồi tạo ra các screens có navigation nhất quán, data liên kết, flow rõ ràng. Result: tốt. Nhưng phải ngồi click tay tạo từng screen.

**Cách 2 — AI agent gọi Stitch MCP:**
AI đọc tài liệu, tự lên danh sách screens, gọi Stitch MCP để vẽ tự động. Không cần click gì. Nhưng mỗi lần gọi MCP là một session riêng — Stitch không biết screen trước đã vẽ gì. Result: mỗi screen tự chọn sidebar, navigation, màu sắc riêng.

**Nhìn vào bảng dưới sẽ thấy rõ:**

| Màn hình | Sidebar | Top Navigation | Problem: |
|----------|---------|----------------|--------|
| App Shell Header (S01) | Không có | `Nhà phân tích · BaoCaoT3_2026.xlsx` | Header bar riêng |
| Tab Navigation (S02) | `Dashboard, Reports, History, Cảnh báo` | `Dashboard, Reports, History` | Khác hoàn toàn S01 |
| KPI Row (S05) | `Analytics, Team, Projects, Tasks, Archive` | `Dashboard, Reports, History` | Sidebar khác S02 |
| State Distribution (S06) | `Analytics, Team, Projects, Tasks, Archive` | `Dashboard, Reports, History` | Giống S05 nhưng khác S02 |
| Health Distribution (S07) | `PHÂN TÍCH, NHÓM, DỰ ÁN, CÔNG VIỆC, LƯU TRỮ` | `Phân tích, Nhóm, Dự án` | Bỗng chuyển sang chữ in hoa (!) |

Năm screens, năm hệ thống navigation khác nhau. Từng screen đứng riêng thì đẹp — nhưng ghép lại không phải một hệ thống.

### Ảnh minh họa (trước khi dùng skill)

<p align="center">
  <img src="examples/tmpScreens/createdByAIPrompt/image.png" width="45%" alt="App Shell Header — navigation riêng" />
  <img src="examples/tmpScreens/createdByAIPrompt/image copy.png" width="45%" alt="Tab Navigation — sidebar khác" />
</p>
<p align="center">
  <img src="examples/tmpScreens/createdByAIPrompt/image copy 2.png" width="45%" alt="KPI Dashboard — lại sidebar khác" />
  <img src="examples/tmpScreens/createdByAIPrompt/image copy 3.png" width="45%" alt="State Distribution — không nhất quán" />
</p>
<p align="center">
  <img src="examples/tmpScreens/createdByAIPrompt/image copy 4.png" width="45%" alt="Health Distribution — sidebar chữ in hoa" />
</p>

> Từng screen trông rất xịn. Nhưng để ý sidebar, top navigation, thậm chí ngôn ngữ Changes: giữa các screens. Đó là Problem: context.

---

## 💡 Solution:

Skill này kết hợp cả hai cách: **giữ lại "hiểu tổng thể" của Cách 1, cộng "tự động hoàn toàn" của Cách 2.**

Ý tưởng cốt lõi: trước khi vẽ bất kỳ screen nào, tạo ra một **Design System Spec** chung và inject vào mọi 
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

