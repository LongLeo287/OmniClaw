---
id: stitchskill
type: knowledge
owner: OA_Triage
---
# stitchskill
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# 🧩 Stitch Wireframe Generator — Antigravity Skill

> AI đọc tài liệu mô tả phần mềm → lên kế hoạch toàn bộ màn hình → xây dựng prompt có context đầy đủ → tự động vẽ wireframe qua Google Stitch.

Một skill cho [Antigravity](https://code.google.com/assist/) giúp tự động hóa quy trình vẽ wireframe qua Google Stitch MCP. Thay vì ngồi tạo từng screen thủ công, để AI agent xử lý toàn bộ pipeline — từ phân tích tài liệu đến vẽ hệ thống hoàn chỉnh.

---

## 🤔 Vấn đề

Có hai cách vẽ wireframe với Google Stitch, và cả hai đều có hạn chế:

**Cách 1 — Upload tài liệu trực tiếp lên Stitch:**
Stitch đọc toàn bộ file, hiểu hệ thống, rồi tạo ra các screens có navigation nhất quán, data liên kết, flow rõ ràng. Kết quả tốt. Nhưng phải ngồi click tay tạo từng screen.

**Cách 2 — AI agent gọi Stitch MCP:**
AI đọc tài liệu, tự lên danh sách screens, gọi Stitch MCP để vẽ tự động. Không cần click gì. Nhưng mỗi lần gọi MCP là một session riêng — Stitch không biết screen trước đã vẽ gì. Kết quả: mỗi screen tự chọn sidebar, navigation, màu sắc riêng.

**Nhìn vào bảng dưới sẽ thấy rõ:**

| Màn hình | Sidebar | Top Navigation | Vấn đề |
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

> Từng screen trông rất xịn. Nhưng để ý sidebar, top navigation, thậm chí ngôn ngữ thay đổi giữa các screens. Đó là vấn đề context.

---

## 💡 Giải pháp

Skill này kết hợp cả hai cách: **giữ lại "hiểu tổng thể" của Cách 1, cộng "tự động hoàn toàn" của Cách 2.**

Ý tưởng cốt lõi: trước khi vẽ bất kỳ screen nào, tạo ra một **Design System Spec** chung và inject vào mọi prompt. Mỗi prompt không chỉ mô tả "vẽ gì" mà còn chứa toàn bộ thông tin hệ thống: navigation structure, color palette, danh sách tất cả screens và vị trí screen hiện tại trong flow.

### Ảnh minh họa (sau khi dùng skill)

<p align="center">
  <img src="examples/createdScreens/image copy 2.png" width="45%" alt="Dashboard Overview — navigation nhất quán" />
  <img src="examples/createdScreens/image copy 5.png" width="45%" alt="Comparison View — cùng navigation, data liên kết" />
</p>
<p align="center">
  <img src="examples/createdScreens/image copy 3.png" width="45%" alt="Dashboard Detail — sidebar đồng nhất" />
</p>

> Cùng sidebar, cùng top navigation, cùng hệ màu, data liên kết chéo — xuyên suốt 16 screens được auto-feed.

### Quá trình chạy auto-feed

Khi chạy skill ở chế độ auto-feed, AI tự động gọi Stitch MCP lần lượt cho từng screen. Đây là quá trình thực tế khi vẽ 16 screens cho TaskLens v2:

<p align="center">
  <img src="examples/createdScreens/image copy.png" width="45%" alt="Bắt đầu auto-feed — S01 đến S05" />
  <img src="examples/createdScreens/image copy 4.png" width="45%" alt="Tiếp tục — S05 đến S08" />
</p>
<p align="center">
  <img src="examples/createdScreens/image.png" width="45%" alt="Chi tiết prompt đang được feed vào Stitch" />
  <img src="examples/createdScreens/image copy 6.png" width="45%" alt="Hoàn tất 16/16 screens — tất cả thành công" />
</p>

> AI tự đọc prompt từ thư mục `prompts/`, gọi `generate_screen_from_text` cho từng screen, log kết quả, rồi tự chuyển sang screen tiếp theo. Cả 16 screens hoàn thành mà không cần can thiệp.

---

## ✨ Skill làm được gì

- 📖 **Đọc tài liệu mô tả phần mềm** (markdown, docx, txt) và trích xuất system context
- 🎨 **Thu thập style preferences** (screenshots, brand guide, URL tham khảo, hoặc đơn giản "dark theme, minimal")
- 👥 **Đề xuất actors và journeys** cho người dùng duyệt — chỉ vẽ khi được approve
- 🎯 **Tạo Design System thống nhất** (colors, fonts, navigation) inject vào mọi screen prompt
- 📝 **Xây prompt 3 phần chi tiết** cho từng screen (Design System + Screen Map Context + Screen Content)
- 🖼️ **Tự động vẽ wireframe** qua Stitch MCP — 16 screens liền, không cần click
- 📊 **Log toàn bộ** vào thư mục project để truy vết

---

## 📦 Cài đặt

### Yêu cầu

- [Antigravity](https://code.google.com/assist/) (AI coding assistant của Google)
- [Google Stitch MCP](https://developers.google.com/stitch) đã bật trong Antigravity settings
- [Google Cloud SDK](https://cloud.google.com/sdk) (`gcloud` CLI) — chỉ cần cho chế độ script

### Các bước

1. **Clone hoặc copy skill** vào thư mục skills của Antigravity:

```
# Thư mục skills của Antigravity — thường là:
#   <workspace>/.agent/skills/
#   hoặc đường dẫn skills tùy chỉnh

git clone <repo-url> stitchSkill
```

2. **Kiểm tra skill được nhận diện:** Mở Antigravity trong workspace. Skill sẽ tự kích hoạt khi bạn hỏi về wireframe hoặc Stitch.

3. **(Tùy chọn) Cài authentication cho chế độ script:**

```powershell
# Vào thư mục skill
cd .agent/skills/stitchSkill

# Chạy setup auth (chỉ 1 lần)
powershell -File scripts/setup_auth.ps1
```

Xong. Skill sẵn sàng sử dụng.

---

## 🔐 Authentication (cho chế độ script)

> **Lưu ý:** Nếu chỉ dùng Mode A (Stitch MCP), authentication được Antigravity xử lý tự động. Phần này chỉ dành cho Mode B (script batch).

<!-- TODO: Hoàn thiện tự động hóa gcloud ADC setup -->
<!-- Script setup_auth.ps1 hiện hướng dẫn qua:
1. Kiểm tra gcloud CLI đã cài chưa
2. Chạy `gcloud auth application-default login`
3. Verify file credential được tạo
4. Test kết nối tới stitch.googleapis.com

Tạo file ~/.config/gcloud/application_default_credentials.json
chứa OAuth2 refresh_token, tự refresh vĩnh viễn. -->

```powershell
# Chạy 1 lần — mở browser để login Google
gcloud auth application-default login

# Kiểm tra
gcloud auth application-default print-access-token
```

**Trạng thái:** 🚧 Script `setup_auth.ps1` và batch generation đang trong quá trình hoàn thiện. Phương án gcloud ADC hoạt động ổn nhưng automation wrapper đang được cải thiện. Đóng góp luôn được chào đón!

---

## 🚀 Cách sử dụng

### Bắt đầu nhanh

Chỉ cần nói với AI agent:

> "Đọc file mô tả phần mềm ở `docs/product-spec.md` và vẽ wireframe cho toàn bộ hệ thống bằng stitch wireframe skill."

Agent sẽ tự động:
1. Đọc SKILL.md và thực hiện pipeline 8 bước
2. Hỏi bạn ở đúng thời điểm (không hỏi tất cả cùng lúc)
3. Vẽ toàn bộ screens vào Stitch project

### Pipeline 8 bước

```
📖 Bước 1: Đọc tài liệu & thu thập style references
     ↓
👥 Bước 2: Đề xuất actors → journeys → screens (bạn duyệt từng lớp)
     ↓
🎨 Bước 3: Xây Design System (màu → nav → layout, bạn duyệt từng phần)
     ↓
📝 Bước 4: Tạo prompt 3 phần cho mọi screen
     ↓
🔧 Bước 5: Chọn Stitch project & chế độ vẽ
     ↓
🖼️ Bước 6: Auto-feed screens theo thứ tự journey
     ↓
✏️ Bước 7: Review & chỉnh sửa
     ↓
📊 Bước 8: Xuất báo cáo
```

### Hai chế độ vẽ

| Chế độ | Cách hoạt động | Phù hợp khi |
|--------|---------------|-------------|
| **Interactive (MCP)** | AI vẽ từng screen → trình bày → chờ feedback → sửa → tiếp | < 10 screens, muốn review từng cái |
| **Auto-feed (MCP)** | AI vẽ toàn bộ liền, bạn review cuối | ≥ 10 screens, vẽ hàng loạt |

Agent sẽ gợi ý chế độ dựa trên số lượng screen, nhưng bạn luôn có thể chọn.

### Ví dụ tương tác

```
Bạn:    "Vẽ wireframe cho TaskLens v2 bằng stitch wireframe skill.
         Đây là spec: docs/tasklens-v2-spec.md"

Agent:  "Đã đọc spec và trích xuất system context.
         Anh/chị có tài liệu tham chiếu nào không — screenshots,
         brand guidelines, hoặc website nào thích phong cách?"

Bạn:    "Dark theme, minimal, giống Linear.app"

Agent:  "Ghi nhận. Từ spec, tôi nhận diện 3 actors:
         1. Analyst — sử dụng hàng ngày
         2. Unit Manager — hàng tuần
         3. Executive — hàng tháng
         
         Anh/chị đồng ý không?"

Bạn:    "Thêm System Admin"

Agent:  "Đã cập nhật. Với Analyst, tôi đề xuất các journeys sau:
         1. Dashboard Analytics → Drill-down → Export
         2. Task Management → Task Detail → Annotations
         ..."

[... hỏi từng lớp tiếp tục ...]

Agent:  "Cả 16 screens đã được duyệt. Với 16 screens,
         tôi đề xuất chế độ Auto-feed. Tiến hành?"

Bạn:    "OK"

Agent:  "Auto-feeding S01 Login Page (1/16)...
         Auto-feeding S02 Dashboard Overview (2/16)...
         ...
         Cả 16/16 screens đã tạo thành công! ✅"
```

---

## 📁 Cấu trúc dự án

```
stitchSkill/
├── SKILL.md                          # Hướng dẫn chính (pipeline 8 bước)
├── README.md                         # Bạn đang đọc file này
├── README_vi.md                      # File này (bản tiếng Việt)
├── implementation_plan.md            # Kế hoạch chi tiết (tiếng Việt)
├── implementation_plan_en.md         # Kế hoạch chi tiết (tiếng Anh)
│
├── templates/                        # Template mẫu cho từng bước
│   ├── system_context_template.md    # Bước 1 — Trích xuất system context
│   ├── screen_map_template.md        # Bước 2 — Cấu trúc screen map
│   ├── design_system_template.md     # Bước 3 — Design system spec
│   ├── screen_prompt_template.md     # Bước 4 — Prompt 3 phần cho mỗi screen
│   └── generation_log_template.md    # Bước 6 — Log quá trình vẽ
│
├── scripts/                          # Script tự động hóa (Mode B)
│   ├── setup_auth.ps1                # 🚧 Cài đặt Google ADC (1 lần)
│   ├── setup_project.js              # 🚧 Tạo/liệt kê Stitch projects qua API
│   └── batch_generate.js             # 🚧 Vẽ hàng loạt qua API
│
├── examples/                         # Ví dụ tham khảo
│   ├── tasklens_design_system.md     # Ví dụ design system (TaskLens v2)
│   ├── tasklens_screen_prompts.md    # Ví dụ screen prompts (TaskLens v2)
│   ├── createdScreens/              # Kết quả auto-feed (16 screens)
│   └── tmpScreens/                  # Screenshots so sánh
│       ├── createdByStitch/         # Kết quả upload trực tiếp
│       └── createdByAIPrompt/       # Kết quả AI prompt đơn lẻ
│
└── projects/                         # [RUNTIME] Output mỗi dự án
    └── <tên-dự-án>/
        ├── system_context.md
        ├── style_references.md
        ├── screen_map.md
        ├── design_system.md
        ├── prompts/
        │   ├── S01_login.md
        │   ├── S02_dashboard.md
        │   └── ...
        ├── generation_log.md
        └── wireframe_report.md
```

---

## 🔬 Context injection hoạt động thế nào

"Bí quyết" nằm ở cấu trúc prompt 3 phần. Mọi screen prompt đều chứa:

```
┌─────────────────────────────────────────────┐
│  PHẦN 1: DESIGN SYSTEM                     │
│  Cùng colors, fonts, nav cho TẤT CẢ screens│
│  → Sidebar: đúng các mục này, đúng thứ tự  │
│  → Top bar: layout này, elements này        │
│  → Colors: #1A1B2E bg, #6366F1 accent, ...  │
├─────────────────────────────────────────────┤
│  PHẦN 2: SCREEN MAP CONTEXT                │
│  "Đây là screen 7 trên 16."                │
│  "Thuộc Journey: Dashboard Analytics"       │
│  "Sidebar highlight: Dashboard > Detail"    │
│  "Screen trước: Dashboard Overview"         │
│  "Screen tiếp: Export Modal"                │
├─────────────────────────────────────────────┤
│  PHẦN 3: NỘI DUNG SCREEN CỤ THỂ           │
│  Layout grid, sections, components          │
│  Data mẫu — nhất quán với screens khác     │
│  Interactions, states, edge cases           │
└─────────────────────────────────────────────┘
```

Cách này đảm bảo Stitch luôn có "bức tranh toàn cảnh" cho mọi screen — giống hệt khi bạn upload tất cả tài liệu cùng lúc.

---

## 🗺️ Thư viện journey tham khảo

Skill bao gồm 12 nhóm journey để AI đề xuất flow phù hợp:

| Nhóm | Ví dụ |
|------|-------|
| Core Navigation | Login, Register, 2FA, Onboarding, Dashboard |
| Data Browsing | Master List, Detail View, Edit Form, Search, Import/Export |
| Analytics | KPI Dashboard, Drill-down, Report Builder, So sánh giữa các kỳ |
| Workflow | Kanban Board, Approval Flow, Multi-step Wizard, Alerts |
| Communication | Inbox, Thread, File Sharing, Activity Feed |
| User Management | Profile, Org Management, User Admin, Roles & Permissions |
| System Admin | Settings, Feature Toggles, Audit Logs |
| E-commerce | Product Catalog, Cart, Checkout, Order Management |
| Content | WYSIWYG Editor, Publishing Flow, Template Management |
| Map & Location | Interactive Map, Asset Tracking |
| Monitoring | System Status, Incident Management |
| Edge Cases | Empty States, Error Pages, Help Center |

AI chọn các nhóm phù hợp dựa trên tài liệu mô tả — không phải project nào cũng cần đủ 12 nhóm.

---

## 🛠️ Trạng thái & lộ trình

| Thành phần | Trạng thái | Ghi chú |
|-----------|-----------|---------|
| SKILL.md (pipeline 8 bước) | ✅ Hoàn thành | Pipeline đầy đủ với interaction rules |
| Templates (5 files) | ✅ Hoàn thành | Bao phủ tất cả bước |
| Examples (TaskLens v2) | ✅ Hoàn thành | Design system + screen prompts |
| Auto-feed qua MCP | ✅ Hoạt động | Đã test với 16 screens |
| `setup_auth.ps1` | 🚧 Đang phát triển | Flow cơ bản hoạt động, đang cải thiện automation |
| `batch_generate.js` | 🚧 Đang phát triển | API calls hoạt động, retry logic đang phát triển |
| `setup_project.js` | 🚧 Đang phát triển | CRUD project qua REST API |

---

## 🤝 Đóng góp

Skill đang được phát triển tích cực. Mọi đóng góp đều được chào đón!

**Các mảng cần đóng góp:**
- Script tự động hóa (thư mục `scripts/`) — gcloud auth wrapper, batch generation, retry logic
- Thêm ví dụ cho các loại phần mềm khác (e-commerce, SaaS, mobile app)
- Cải thiện templates dựa trên trải nghiệm thực tế
- Hỗ trợ hệ điều hành khác (hiện tại tập trung Windows/PowerShell)

**Cách đóng góp:**
1. Fork repo này
2. Tạo branch mới
3. Thực hiện thay đổi
4. Gửi pull request

---

## 📄 Giấy phép

MIT

---

## 🙏 Lời cảm ơn

- [Google Stitch](https://stitch.google.com/) — công cụ vẽ wireframe bằng AI
- [Antigravity](https://code.google.com/assist/) — AI coding assistant với hệ thống skill
- Xây dựng từ nhận thức rằng **context là tất cả** — cho AI thấy bức tranh toàn cảnh, nó sẽ vẽ ra hệ thống, không phải những màn hình rời rạc.

```

### File: projects\README.md
```md
# Projects Directory
This directory is created at runtime for per-project output.
Each project gets its own subdirectory with all generated artifacts.

See SKILL.md for the full file structure.

```

### File: stitchSkill\README.md
```md
# 🧩 Stitch Wireframe Generator — Antigravity Skill

> AI đọc tài liệu mô tả phần mềm → lên kế hoạch toàn bộ màn hình → xây dựng prompt có context đầy đủ → tự động vẽ wireframe qua Google Stitch.

Một skill cho [Antigravity](https://code.google.com/assist/) giúp tự động hóa quy trình vẽ wireframe qua Google Stitch MCP. Thay vì ngồi tạo từng screen thủ công, để AI agent xử lý toàn bộ pipeline — từ phân tích tài liệu đến vẽ hệ thống hoàn chỉnh.

---

## 🤔 Vấn đề

Có hai cách vẽ wireframe với Google Stitch, và cả hai đều có hạn chế:

**Cách 1 — Upload tài liệu trực tiếp lên Stitch:**
Stitch đọc toàn bộ file, hiểu hệ thống, rồi tạo ra các screens có navigation nhất quán, data liên kết, flow rõ ràng. Kết quả tốt. Nhưng phải ngồi click tay tạo từng screen.

**Cách 2 — AI agent gọi Stitch MCP:**
AI đọc tài liệu, tự lên danh sách screens, gọi Stitch MCP để vẽ tự động. Không cần click gì. Nhưng mỗi lần gọi MCP là một session riêng — Stitch không biết screen trước đã vẽ gì. Kết quả: mỗi screen tự chọn sidebar, navigation, màu sắc riêng.

**Nhìn vào bảng dưới sẽ thấy rõ:**

| Màn hình | Sidebar | Top Navigation | Vấn đề |
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

> Từng screen trông rất xịn. Nhưng để ý sidebar, top navigation, thậm chí ngôn ngữ thay đổi giữa các screens. Đó là vấn đề context.

---

## 💡 Giải pháp

Skill này kết hợp cả hai cách: **giữ lại "hiểu tổng thể" của Cách 1, cộng "tự động hoàn toàn" của Cách 2.**

Ý tưởng cốt lõi: trước khi vẽ bất kỳ screen nào, tạo ra một **Design System Spec** chung và inject vào mọi prompt. Mỗi prompt không chỉ mô tả "vẽ gì" mà còn chứa toàn bộ thông tin hệ thống: navigation structure, color palette, danh sách tất cả screens và vị trí screen hiện tại trong flow.

### Ảnh minh họa (sau khi dùng skill)

<p align="center">
  <img src="examples/createdScreens/image copy 2.png" width="45%" alt="Dashboard Overview — navigation nhất quán" />
  <img src="examples/createdScreens/image copy 5.png" width="45%" alt="Comparison View — cùng navigation, data liên kết" />
</p>
<p align="center">
  <img src="examples/createdScreens/image copy 3.png" width="45%" alt="Dashboard Detail — sidebar đồng nhất" />
</p>

> Cùng sidebar, cùng top navigation, cùng hệ màu, data liên kết chéo — xuyên suốt 16 screens được auto-feed.

### Quá trình chạy auto-feed

Khi chạy skill ở chế độ auto-feed, AI tự động gọi Stitch MCP lần lượt cho từng screen. Đây là quá trình thực tế khi vẽ 16 screens cho TaskLens v2:

<p align="center">
  <img src="examples/createdScreens/image copy.png" width="45%" alt="Bắt đầu auto-feed — S01 đến S05" />
  <img src="examples/createdScreens/image copy 4.png" width="45%" alt="Tiếp tục — S05 đến S08" />
</p>
<p align="center">
  <img src="examples/createdScreens/image.png" width="45%" alt="Chi tiết prompt đang được feed vào Stitch" />
  <img src="examples/createdScreens/image copy 6.png" width="45%" alt="Hoàn tất 16/16 screens — tất cả thành công" />
</p>

> AI tự đọc prompt từ thư mục `prompts/`, gọi `generate_screen_from_text` cho từng screen, log kết quả, rồi tự chuyển sang screen tiếp theo. Cả 16 screens hoàn thành mà không cần can thiệp.

---

## ✨ Skill làm được gì

- 📖 **Đọc tài liệu mô tả phần mềm** (markdown, docx, txt) và trích xuất system context
- 🎨 **Thu thập style preferences** (screenshots, brand guide, URL tham khảo, hoặc đơn giản "dark theme, minimal")
- 👥 **Đề xuất actors và journeys** cho người dùng duyệt — chỉ vẽ khi được approve
- 🎯 **Tạo Design System thống nhất** (colors, fonts, navigation) inject vào mọi screen prompt
- 📝 **Xây prompt 3 phần chi tiết** cho từng screen (Design System + Screen Map Context + Screen Content)
- 🖼️ **Tự động vẽ wireframe** qua Stitch MCP — 16 screens liền, không cần click
- 📊 **Log toàn bộ** vào thư mục project để truy vết

---

## 📦 Cài đặt

### Yêu cầu

- [Antigravity](https://code.google.com/assist/) (AI coding assistant của Google)
- [Google Stitch MCP](https://developers.google.com/stitch) đã bật trong Antigravity settings
- [Google Cloud SDK](https://cloud.google.com/sdk) (`gcloud` CLI) — chỉ cần cho chế độ script

### Các bước

1. **Clone hoặc copy skill** vào thư mục skills của Antigravity:

```
# Thư mục skills của Antigravity — thường là:
#   <workspace>/.agent/skills/
#   hoặc đường dẫn skills tùy chỉnh

git clone <repo-url> stitchSkill
```

2. **Kiểm tra skill được nhận diện:** Mở Antigravity trong workspace. Skill sẽ tự kích hoạt khi bạn hỏi về wireframe hoặc Stitch.

3. **(Tùy chọn) Cài authentication cho chế độ script:**

```powershell
# Vào thư mục skill
cd .agent/skills/stitchSkill

# Chạy setup auth (chỉ 1 lần)
powershell -File scripts/setup_auth.ps1
```

Xong. Skill sẵn sàng sử dụng.

---

## 🔐 Authentication (cho chế độ script)

> **Lưu ý:** Nếu chỉ dùng Mode A (Stitch MCP), authentication được Antigravity xử lý tự động. Phần này chỉ dành cho Mode B (script batch).

<!-- TODO: Hoàn thiện tự động hóa gcloud ADC setup -->
<!-- Script setup_auth.ps1 hiện hướng dẫn qua:
1. Kiểm tra gcloud CLI đã cài chưa
2. Chạy `gcloud auth application-default login`
3. Verify file credential được tạo
4. Test kết nối tới stitch.googleapis.com

Tạo file ~/.config/gcloud/application_default_credentials.json
chứa OAuth2 refresh_token, tự refresh vĩnh viễn. -->

```powershell
# Chạy 1 lần — mở browser để login Google
gcloud auth application-default login

# Kiểm tra
gcloud auth application-default print-access-token
```

**Trạng thái:** 🚧 Script `setup_auth.ps1` và batch generation đang trong quá trình hoàn thiện. Phương án gcloud ADC hoạt động ổn nhưng automation wrapper đang được cải thiện. Đóng góp luôn được chào đón!

---

## 🚀 Cách sử dụng

### Bắt đầu nhanh

Chỉ cần nói với AI agent:

> "Đọc file mô tả phần mềm ở `docs/product-spec.md` và vẽ wireframe cho toàn bộ hệ thống bằng stitch wireframe skill."

Agent sẽ tự động:
1. Đọc SKILL.md và thực hiện pipeline 8 bước
2. Hỏi bạn ở đúng thời điểm (không hỏi tất cả cùng lúc)
3. Vẽ toàn bộ screens vào Stitch project

### Pipeline 8 bước

```
📖 Bước 1: Đọc tài liệu & thu thập style references
     ↓
👥 Bước 2: Đề xuất actors → journeys → screens (bạn duyệt từng lớp)
     ↓
🎨 Bước 3: Xây Design System (màu → nav → layout, bạn duyệt từng phần)
     ↓
📝 Bước 4: Tạo prompt 3 phần cho mọi screen
     ↓
🔧 Bước 5: Chọn Stitch project & chế độ vẽ
     ↓
🖼️ Bước 6: Auto-feed screens theo thứ tự journey
     ↓
✏️ Bước 7: Review & chỉnh sửa
     ↓
📊 Bước 8: Xuất báo cáo
```

### Hai chế độ vẽ

| Chế độ | Cách hoạt động | Phù hợp khi |
|--------|---------------|-------------|
| **Interactive (MCP)** | AI vẽ từng screen → trình bày → chờ feedback → sửa → tiếp | < 10 screens, muốn review từng cái |
| **Auto-feed (MCP)** | AI vẽ toàn bộ liền, bạn review cuối | ≥ 10 screens, vẽ hàng loạt |

Agent sẽ gợi ý chế độ dựa trên số lượng screen, nhưng bạn luôn có thể chọn.

### Ví dụ tương tác

```
Bạn:    "Vẽ wireframe cho TaskLens v2 bằng stitch wireframe skill.
         Đây là spec: docs/tasklens-v2-spec.md"

Agent:  "Đã đọc spec và trích xuất system context.
         Anh/chị có tài liệu tham chiếu nào không — screenshots,
         brand guidelines, hoặc website nào thích phong cách?"

Bạn:    "Dark theme, minimal, giống Linear.app"

Agent:  "Ghi nhận. Từ spec, tôi nhận diện 3 actors:
         1. Analyst — sử dụng hàng ngày
         2. Unit Manager — hàng tuần
         3. Executive — hàng tháng
         
         Anh/chị đồng ý không?"

Bạn:    "Thêm System Admin"

Agent:  "Đã cập nhật. Với Analyst, tôi đề xuất các journeys sau:
         1. Dashboard Analytics → Drill-down → Export
         2. Task Management → Task Detail → Annotations
         ..."

[... hỏi từng lớp tiếp tục ...]

Agent:  "Cả 16 screens đã được duyệt. Với 16 screens,
         tôi đề xuất chế độ Auto-feed. Tiến hành?"

Bạn:    "OK"

Agent:  "Auto-feeding S01 Login Page (1/16)...
         Auto-feeding S02 Dashboard Overview (2/16)...
         ...
         Cả 16/16 screens đã tạo thành công! ✅"
```

---

## 📁 Cấu trúc dự án

```
stitchSkill/
├── SKILL.md                          # Hướng dẫn chính (pipeline 8 bước)
├── README.md                         # Bạn đang đọc file này
├── README_vi.md                      # File này (bản tiếng Việt)
├── implementation_plan.md            # Kế hoạch chi tiết (tiếng Việt)
├── implementation_plan_en.md         # Kế hoạch chi tiết (tiếng Anh)
│
├── templates/                        # Template mẫu cho từng bước
│   ├── system_context_template.md    # Bước 1 — Trích xuất system context
│   ├── screen_map_template.md        # Bước 2 — Cấu trúc screen map
│   ├── design_system_template.md     # Bước 3 — Design system spec
│   ├── screen_prompt_template.md     # Bước 4 — Prompt 3 phần cho mỗi screen
│   └── generation_log_template.md    # Bước 6 — Log quá trình vẽ
│
├── scripts/                          # Script tự động hóa (Mode B)
│   ├── setup_auth.ps1                # 🚧 Cài đặt Google ADC (1 lần)
│   ├── setup_project.js              # 🚧 Tạo/liệt kê Stitch projects qua API
│   └── batch_generate.js             # 🚧 Vẽ hàng loạt qua API
│
├── examples/                         # Ví dụ tham khảo
│   ├── tasklens_design_system.md     # Ví dụ design system (TaskLens v2)
│   ├── tasklens_screen_prompts.md    # Ví dụ screen prompts (TaskLens v2)
│   ├── createdScreens/              # Kết quả auto-feed (16 screens)
│   └── tmpScreens/                  # Screenshots so sánh
│       ├── createdByStitch/         # Kết quả upload trực tiếp
│       └── createdByAIPrompt/       # Kết quả AI prompt đơn lẻ
│
└── projects/                         # [RUNTIME] Output mỗi dự án
    └── <tên-dự-án>/
        ├── system_context.md
        ├── style_references.md
        ├── screen_map.md
        ├── design_system.md
        ├── prompts/
        │   ├── S01_login.md
        │   ├── S02_dashboard.md
        │   └── ...
        ├── generation_log.md
        └── wireframe_report.md
```

---

## 🔬 Context injection hoạt động thế nào

"Bí quyết" nằm ở cấu trúc prompt 3 phần. Mọi screen prompt đều chứa:

```
┌─────────────────────────────────────────────┐
│  PHẦN 1: DESIGN SYSTEM                     │
│  Cùng colors, fonts, nav cho TẤT CẢ screens│
│  → Sidebar: đúng các mục này, đúng thứ tự  │
│  → Top bar: layout này, elements này        │
│  → Colors: #1A1B2E bg, #6366F1 accent, ...  │
├─────────────────────────────────────────────┤
│  PHẦN 2: SCREEN MAP CONTEXT                │
│  "Đây là screen 7 trên 16."                │
│  "Thuộc Journey: Dashboard Analytics"       │
│  "Sidebar highlight: Dashboard > Detail"    │
│  "Screen trước: Dashboard Overview"         │
│  "Screen tiếp: Export Modal"                │
├─────────────────────────────────────────────┤
│  PHẦN 3: NỘI DUNG SCREEN CỤ THỂ           │
│  Layout grid, sections, components          │
│  Data mẫu — nhất quán với screens khác     │
│  Interactions, states, edge cases           │
└─────────────────────────────────────────────┘
```

Cách này đảm bảo Stitch luôn có "bức tranh toàn cảnh" cho mọi screen — giống hệt khi bạn upload tất cả tài liệu cùng lúc.

---

## 🗺️ Thư viện journey tham khảo

Skill bao gồm 12 nhóm journey để AI đề xuất flow phù hợp:

| Nhóm | Ví dụ |
|------|-------|
| Core Navigation | Login, Register, 2FA, Onboarding, Dashboard |
| Data Browsing | Master List, Detail View, Edit Form, Search, Import/Export |
| Analytics | KPI Dashboard, Drill-down, Report Builder, So sánh giữa các kỳ |
| Workflow | Kanban Board, Approval Flow, Multi-step Wizard, Alerts |
| Communication | Inbox, Thread, File Sharing, Activity Feed |
| User Management | Profile, Org Management, User Admin, Roles & Permissions |
| System Admin | Settings, Feature Toggles, Audit Logs |
| E-commerce | Product Catalog, Cart, Checkout, Order Management |
| Content | WYSIWYG Editor, Publishing Flow, Template Management |
| Map & Location | Interactive Map, Asset Tracking |
| Monitoring | System Status, Incident Management |
| Edge Cases | Empty States, Error Pages, Help Center |

AI chọn các nhóm phù hợp dựa trên tài liệu mô tả — không phải project nào cũng cần đủ 12 nhóm.

---

## 🛠️ Trạng thái & lộ trình

| Thành phần | Trạng thái | Ghi chú |
|-----------|-----------|---------|
| SKILL.md (pipeline 8 bước) | ✅ Hoàn thành | Pipeline đầy đủ với interaction rules |
| Templates (5 files) | ✅ Hoàn thành | Bao phủ tất cả bước |
| Examples (TaskLens v2) | ✅ Hoàn thành | Design system + screen prompts |
| Auto-feed qua MCP | ✅ Hoạt động | Đã test với 16 screens |
| `setup_auth.ps1` | 🚧 Đang phát triển | Flow cơ bản hoạt động, đang cải thiện automation |
| `batch_generate.js` | 🚧 Đang phát triển | API calls hoạt động, retry logic đang phát triển |
| `setup_project.js` | 🚧 Đang phát triển | CRUD project qua REST API |

---

## 🤝 Đóng góp

Skill đang được phát triển tích cực. Mọi đóng góp đều được chào đón!

**Các mảng cần đóng góp:**
- Script tự động hóa (thư mục `scripts/`) — gcloud auth wrapper, batch generation, retry logic
- Thêm ví dụ cho các loại phần mềm khác (e-commerce, SaaS, mobile app)
- Cải thiện templates dựa trên trải nghiệm thực tế
- Hỗ trợ hệ điều hành khác (hiện tại tập trung Windows/PowerShell)

**Cách đóng góp:**
1. Fork repo này
2. Tạo branch mới
3. Thực hiện thay đổi
4. Gửi pull request

---

## 📄 Giấy phép

MIT

---

## 🙏 Lời cảm ơn

- [Google Stitch](https://stitch.google.com/) — công cụ vẽ wireframe bằng AI
- [Antigravity](https://code.google.com/assist/) — AI coding assistant với hệ thống skill
- Xây dựng từ nhận thức rằng **context là tất cả** — cho AI thấy bức tranh toàn cảnh, nó sẽ vẽ ra hệ thống, không phải những màn hình rời rạc.

```

### File: stitchSkill\projects\README.md
```md
# Projects Directory
This directory is created at runtime for per-project output.
Each project gets its own subdirectory with all generated artifacts.

See SKILL.md for the full file structure.

```

### File: implementation_plan.md
```md
# Phương Án Tự Động: AI-Powered Wireframe Generation via Stitch

## Mục tiêu

Xây dựng **Skill** hoàn chỉnh (`stitchSkill`) giúp AI tự động: đọc tài liệu mô tả → lên kế hoạch toàn bộ màn hình → xây dựng prompt chất lượng cao → **vẽ wireframe qua Stitch MCP hoặc script trực tiếp**.

---

## Hai Chế Độ Thực Thi

| | Mode A — Stitch MCP | Mode B — Direct API Script |
|---|---|---|
| **Cơ chế** | AI gọi MCP tools | Node.js gọi `stitch.googleapis.com` REST API |
| **Auth** | Google ADC | ✅ Tái sử dụng cùng ADC |
| **Ưu điểm** | AI review từng screen, linh hoạt sửa | Batch, retry, parallel, logging tự động |
| **Khi nào dùng** | < 10 screens, cần review | ≥ 10 screens, batch |

---

## Authentication

File `application_default_credentials.json` chứa: `client_id`, `client_secret`, `refresh_token`, `type: authorized_user`. Không thể tái sử dụng login Antigravity (scope khác). Skill bao gồm `setup_auth.ps1` chạy **1 lần duy nhất** — mở browser login Google → token tự refresh vĩnh viễn.

---

## Pipeline 8 Bước

> **Lưu ý:** Toàn bộ output nằm tại `stitchSkill/projects/<tên-project>/`

### Bước 1 — Đọc Tài Liệu & Thu Thập Tham Chiếu

**1a. Đọc & phân tích tài liệu mô tả:**
- AI đọc toàn bộ file mô tả (markdown, docx, txt…)
- Trích xuất: mục tiêu, user roles, features, data entities, business rules, thuật ngữ
- → Output: `projects/<name>/system_context.md`

**1b. Hỏi người dùng về reference materials:**

AI chủ động hỏi:

> *"Anh/chị có tài liệu tham chiếu nào không? Ví dụ:"*
> 1. 🖼️ **Screenshot / mockup** của ứng dụng tương tự muốn tham khảo
> 2. 🎨 **Style guide / brand guidelines** (logo, màu sắc, font chữ)
> 3. 🌐 **URL website/app** mà anh/chị thích phong cách
> 4. 📝 **Ghi chú về style** (ví dụ: "dark theme, corporate, minimal")
> 5. 📄 **Bất kỳ tài liệu nào khác** (wireframe cũ, Figma link, PDF…)

Nếu người dùng cung cấp:
- Screenshot → AI phân tích color palette, layout pattern, component style → inject vào design system
- URL → AI (hoặc browser tool) capture & phân tích visual style
- Brand guide → Extract colors, fonts, logo rules
- Text → Ghi nhận preferences

→ Output: `projects/<name>/style_references.md` (tổng hợp mọi reference)

### Bước 2 — Xác Định TOÀN BỘ Màn Hình (Screen Map)

**2a. AI đề xuất Users/Actors & Journeys:**

Dựa trên `system_context.md` + `style_references.md`, AI tư vấn:

```markdown
## Đề xuất Users/Actors

Từ tài liệu mô tả, tôi nhận diện các nhóm user sau:

| # | Actor | Mô tả | Tần suất sử dụng |
|---|---|---|---|
| 1 | Analyst | Người phân tích dữ liệu chính | Hàng ngày |
| 2 | Unit Manager | Quản lý cấp đơn vị | Hàng tuần |
| 3 | Executive | Lãnh đạo cấp cao | Hàng tháng |
| 4 | System Admin | Quản trị hệ thống | Khi cần |

## Đề xuất Journeys cho từng Actor

### Actor 1: Analyst
- ✅ Dashboard Analytics → Drill-down → Export
- ✅ Task Management → Task Detail → Annotations
- ✅ Report Comparison → Cross-period Analysis

### Actor 2: Unit Manager
- ✅ Team Overview → Member Performance → Alerts
- ...

> 💬 Anh/chị đồng ý với đề xuất trên không?
> Có thể: bổ sung actor, bỏ bớt journey, thêm screen cụ thể,
> hoặc comment bất kỳ điều chỉnh nào.
```

**2b. Người dùng review & điều chỉnh:**
- Đồng ý → AI tiến hành
- Comment → AI cập nhật theo feedback, đề xuất lại
- Bổ sung → AI thêm vào
- Bỏ bớt → AI loại ra

**2c. Sau khi được duyệt, AI tạo screen map hoàn chỉnh:**

→ Output: `projects/<name>/screen_map.md` bao gồm:
- Danh sách tất cả screens (đánh số SXX)
- Phân nhóm theo journey đã duyệt
- Flow diagram (mermaid)
- Navigation mapping (screen nào link đến screen nào)

#### Thư viện Journey Tham Khảo cho AI

##### 1. Core Navigation & Entry
| Journey | Screens ví dụ |
|---|---|
| Authentication | Login, Register, Forgot Password, 2FA, SSO Redirect |
| Onboarding | Welcome, Setup Wizard, Profile Completion, Tour |
| Home / Landing | Dashboard Overview, News Feed, Activity Stream |

##### 2. Data Browsing & Management
| Journey | Screens ví dụ |
|---|---|
| List → Detail → Edit | Master List, Detail View, Edit Form, Delete Confirm |
| Search & Filter | Advanced Search, Saved Filters, Search Results |
| Data Import/Export | Upload Wizard, Column Mapping, Preview, Export |
| Bulk Operations | Multi-select, Bulk Edit, Bulk Delete, Progress |

##### 3. Analytics & Reporting
| Journey | Screens ví dụ |
|---|---|
| Dashboard Analytics | KPI Overview, Trends, Comparisons, Period Selector |
| Drill-down | Summary → Category → Individual Item |
| Report Builder | Template, Parameters, Preview, Schedule, Export |
| Data Visualization | Chart Builder, Map View, Heatmap, Pivot Table |
| Cross-period Analysis | Period Comparison, Delta, Trend Projection |

##### 4. Workflow & Process
| Journey | Screens ví dụ |
|---|---|
| Task Management | Kanban Board, Task Detail, Assignment, Tracking |
| Approval Workflow | Submit, Pending, Approve/Reject, History |
| Multi-step Process | Wizard, Progress Bar, Validation, Confirm |
| Alerts & Notifications | Alert Center, Detail, Severity, Acknowledge |
| Calendar & Scheduling | Calendar, Event Detail, Create, Recurring |

##### 5. Communication & Collaboration
| Journey | Screens ví dụ |
|---|---|
| Messaging | Inbox, Thread, Compose, Attachments |
| Comments | Thread, @Mention, Reply, Reactions |
| File Sharing | Browser, Upload, Preview, Version History |

##### 6. User & Account Management
| Journey | Screens ví dụ |
|---|---|
| Profile | View, Edit, Avatar, Preferences |
| Organization | Org List, Detail, Departments, Members |
| User Admin | User List, Detail, Role Assignment, Invite |
| Roles & Permissions | Role List, Permission Matrix, Custom Roles |

##### 7. System Administration
| Journey | Screens ví dụ |
|---|---|
| Settings | General, Theme, Integrations, API Keys |
| Configuration | Feature Toggles, Parameters, Email Templates |
| Audit & Logs | Audit Trail, System Logs, Filters |

##### 8. E-commerce & Transactions
| Journey | Screens ví dụ |
|---|---|
| Product Catalog | Browse, Grid/List, Detail, Compare |
| Cart & Checkout | Cart, Payment, Review, Confirmation |
| Order Management | Orders, Detail, Tracking, Returns |

##### 9. Content Management
| Journey | Screens ví dụ |
|---|---|
| Editing | WYSIWYG, Media Library, Version Control |
| Publishing | Draft → Review → Publish, Schedule |
| Templates | List, Editor, Variable Binding |

##### 10. Map & Location
| Journey | Screens ví dụ |
|---|---|
| Map View | Interactive Map, Markers, Detail Popup |
| Asset Tracking | Real-time Map, Detail, Route History |

##### 11. Monitoring & Operations
| Journey | Screens ví dụ |
|---|---|
| System Monitoring | Status, Health, Uptime, Performance |
| Incidents | List, Triage, Escalation, Post-mortem |

##### 12. Edge Cases & System States
| Journey | Screens ví dụ |
|---|---|
| Empty States | First-time, No Results, No Access |
| Error States | 404, 500, Offline, Session Expired |
| Help & Support | Help Center, FAQ, Contact, Feedback |

### Bước 3 — Xây Dựng Design System Spec

→ Output: `projects/<name>/design_system.md`

Kết hợp `system_context.md` + `style_references.md` (từ Bước 1b) để tạo:
- App Identity, Color Palette, Typography
- **Navigation Structure** (FIXED cho mọi screen)
- Layout Grid, Component Patterns

### Bước 4 — Xây Dựng Prompt Chi Tiết Cho Từng Screen

→ Output: `projects/<name>/prompts/SXX_screen_name.md`

Mỗi prompt gồm **3 phần bắt buộc**:

```
┌─────────────────────────────────────────────┐
│  PART 1: DESIGN SYSTEM (copy từ bước 3)     │
│  → Đảm bảo color, font, nav nhất quán      │
├─────────────────────────────────────────────┤
│  PART 2: SCREEN MAP CONTEXT                 │
│  → Tóm tắt tất cả screens + vị trí hiện tại│
│  → "Đây là screen 3/12: Alerts Console"     │
│  → Sidebar phải highlight đúng menu item    │
├─────────────────────────────────────────────┤
│  PART 3: SCREEN CONTENT                     │
│  → Layout chi tiết cho screen này           │
│  → Data mẫu (nhất quán cross-screen)        │
│  → Sections, interactions, states           │
└─────────────────────────────────────────────┘
```

### Bước 5 — Chọn Project Stitch & Chế Độ Vẽ

**5a.** Gọi `list_projects` → hiển thị danh sách → **hỏi user chọn** project hoặc tạo mới.

**5b.** Hỏi user chọn **chế độ vẽ**:
- **Interactive**: AI vẽ → trình bày → chờ feedback → sửa → tiếp
- **Auto-feed**: AI tự vẽ toàn bộ → user review cuối

### Bước 6 — Vẽ Screens Theo Thứ Tự Journey

Thực thi theo mode đã chọn (Interactive / Auto-feed / Script batch).

### Bước 7 — Review & Chỉnh Sửa

Review tổng thể → sửa (`edit_screens`) → tạo variant nếu cần.

### Bước 8 — Export & Báo Cáo

→ Output: `projects/<name>/wireframe_report.md`

---

## File Structure

```
stitchSkill/
├── SKILL.md                          # Hướng dẫn chính (8 bước)
├── implementation_plan.md            # Plan này
├── templates/
│   ├── system_context_template.md
│   ├── screen_map_template.md
│   ├── design_system_template.md
│   ├── screen_prompt_template.md
│   └── generation_log_template.md
├── scripts/
│   ├── setup_auth.ps1                # One-time ADC login
│   ├── setup_project.js              # Create/list projects
│   └── batch_generate.js             # Batch generation
├── examples/
│   ├── tasklens_design_system.md
│   └── tasklens_screen_prompts.md
└── projects/                         # [RUNTIME] Per-project output
    └── <project-name>/
        ├── system_context.md         # From Step 1a
        ├── style_references.md       # From Step 1b
        ├── screen_map.md             # From Step 2
        ├── design_system.md          # From Step 3
        ├── prompts/                  # From Step 4
        │   ├── S01_dashboard.md
        │   ├── S02_task_list.md
        │   └── ...
        ├── generation_log.md         # From Step 6
        └── wireframe_report.md       # From Step 8
```

---

## Verification Plan

### Automated
1. `setup_auth.ps1` → verify ADC credentials
2. `node scripts/setup_project.js --dry-run` → verify API
3. `node scripts/batch_generate.js --dry-run` → verify prompts

### Manual
1. Full pipeline dry-run
2. So sánh output với Stitch results
3. Đánh giá consistency, data linkage, visual coherence

```

### File: implementation_plan_en.md
```md
# Automated Plan: AI-Powered Wireframe Generation via Stitch

## Goal

Build a complete **Skill** (`stitchSkill`) that enables AI to automatically: read software description docs → plan all screens → craft high-quality prompts → **generate wireframes via Stitch MCP or direct API script**.

---

## Dual Execution Modes

| | Mode A — Stitch MCP | Mode B — Direct API Script |
|---|---|---|
| **Mechanism** | AI calls MCP tools | Node.js calls `stitch.googleapis.com` REST API |
| **Auth** | Google ADC | ✅ Reuses same ADC credentials |
| **Strengths** | AI reviews each screen, flexible edits | Batch processing, retry, parallel, auto-logging |
| **When to use** | < 10 screens, needs review | ≥ 10 screens, batch generation |

---

## Authentication

The `application_default_credentials.json` file contains: `client_id`, `client_secret`, `refresh_token`, `type: authorized_user`. Cannot reuse Antigravity's login (different OAuth scope). The skill includes `setup_auth.ps1` — a **one-time setup** that opens a browser for Google login → token auto-refreshes indefinitely.

---

## 8-Step Pipeline

> **Note:** All output is stored at `stitchSkill/projects/<project-name>/`

### Step 1 — Read Documentation & Collect References

**1a. Read & analyze description documents:**
- AI reads all description files (markdown, docx, txt…)
- Extracts: objectives, user roles, features, data entities, business rules, domain terminology
- → Output: `projects/<name>/system_context.md`

**1b. Ask user for reference materials:**

AI proactively asks:

> *"Do you have any reference materials? For example:"*
> 1. 🖼️ **Screenshots / mockups** of similar apps for inspiration
> 2. 🎨 **Style guide / brand guidelines** (logo, colors, fonts)
> 3. 🌐 **Website/app URLs** whose style you like
> 4. 📝 **Style notes** (e.g., "dark theme, corporate, minimal")
> 5. 📄 **Any other documents** (old wireframes, Figma links, PDFs…)

If the user provides:
- Screenshots → AI analyzes color palette, layout patterns, component styles → injects into design system
- URLs → AI (or browser tool) captures & analyzes visual style
- Brand guide → Extracts colors, fonts, logo rules
- Text → Records preferences

→ Output: `projects/<name>/style_references.md` (consolidated references)

### Step 2 — Identify ALL Screens (Screen Map)

**2a. AI recommends Users/Actors & Journeys:**

Based on `system_context.md` + `style_references.md`, AI proposes:

```markdown
## Proposed Users/Actors

From the description documents, I identified the following user groups:

| # | Actor | Description | Usage Frequency |
|---|---|---|---|
| 1 | Analyst | Primary data analyst | Daily |
| 2 | Unit Manager | Unit-level manager | Weekly |
| 3 | Executive | C-level leadership | Monthly |
| 4 | System Admin | System administrator | As needed |

## Proposed Journeys per Actor

### Actor 1: Analyst
- ✅ Dashboard Analytics → Drill-down → Export
- ✅ Task Management → Task Detail → Annotations
- ✅ Report Comparison → Cross-period Analysis

### Actor 2: Unit Manager
- ✅ Team Overview → Member Performance → Alerts
- ...

> 💬 Do you agree with these proposals?
> You can: add actors, remove journeys, add specific screens,
> or comment with any adjustments.
```

**2b. User reviews & adjusts:**
- Agree → AI proceeds
- Comment → AI updates per feedback, re-proposes
- Add → AI incorporates
- Remove → AI excludes

**2c. After approval, AI creates the complete screen map:**

→ Output: `projects/<name>/screen_map.md` including:
- Full list of all screens (numbered SXX)
- Grouped by approved journeys
- Flow diagram (mermaid)
- Navigation mapping (which screen links to which)

#### Journey Reference Library for AI

##### 1. Core Navigation & Entry
| Journey | Example Screens |
|---|---|
| Authentication | Login, Register, Forgot Password, 2FA, SSO Redirect |
| Onboarding | Welcome, Setup Wizard, Profile Completion, Tour |
| Home / Landing | Dashboard Overview, News Feed, Activity Stream |

##### 2. Data Browsing & Management
| Journey | Example Screens |
|---|---|
| List → Detail → Edit | Master List, Detail View, Edit Form, Delete Confirm |
| Search & Filter | Advanced Search, Saved Filters, Search Results |
| Data Import/Export | Upload Wizard, Column Mapping, Preview, Export |
| Bulk Operations | Multi-select, Bulk Edit, Bulk Delete, Progress |

##### 3. Analytics & Reporting
| Journey | Example Screens |
|---|---|
| Dashboard Analytics | KPI Overview, Trends, Comparisons, Period Selector |
| Drill-down | Summary → Category → Individual Item |
| Report Builder | Template, Parameters, Preview, Schedule, Export |
| Data Visualization | Chart Builder, Map View, Heatmap, Pivot Table |
| Cross-period Analysis | Period Comparison, Delta, Trend Projection |

##### 4. Workflow & Process
| Journey | Example Screens |
|---|---|
| Task Management | Kanban Board, Task Detail, Assignment, Tracking |
| Approval Workflow | Submit, Pending, Approve/Reject, History |
| Multi-step Process | Wizard, Progress Bar, Validation, Confirm |
| Alerts & Notifications | Alert Center, Detail, Severity, Acknowledge |
| Calendar & Scheduling | Calendar, Event Detail, Create, Recurring |

##### 5. Communication & Collaboration
| Journey | Example Screens |
|---|---|
| Messaging | Inbox, Thread, Compose, Attachments |
| Comments | Thread, @Mention, Reply, Reactions |
| File Sharing | Browser, Upload, Preview, Version History |

##### 6. User & Account Management
| Journey | Example Screens |
|---|---|
| Profile | View, Edit, Avatar, Preferences |
| Organization | Org List, Detail, Departments, Members |
| User Admin | User List, Detail, Role Assignment, Invite |
| Roles & Permissions | Role List, Permission Matrix, Custom Roles |

##### 7. System Administration
| Journey | Example Screens |
|---|---|
| Settings | General, Theme, Integrations, API Keys |
| Configuration | Feature Toggles, Parameters, Email Templates |
| Audit & Logs | Audit Trail, System Logs, Filters |

##### 8. E-commerce & Transactions
| Journey | Example Screens |
|---|---|
| Product Catalog | Browse, Grid/List, Detail, Compare |
| Cart & Checkout | Cart, Payment, Review, Confirmation |
| Order Management | Orders, Detail, Tracking, Returns |

##### 9. Content Management
| Journey | Example Screens |
|---|---|
| Editing | WYSIWYG, Media Library, Version Control |
| Publishing | Draft → Review → Publish, Schedule |
| Templates | List, Editor, Variable Binding |

##### 10. Map & Location
| Journey | Example Screens |
|---|---|
| Map View | Interactive Map, Markers, Detail Popup |
| Asset Tracking | Real-time Map, Detail, Route History |

##### 11. Monitoring & Operations
| Journey | Example Screens |
|---|---|
| System Monitoring | Status, Health, Uptime, Performance |
| Incidents | List, Triage, Escalation, Post-mortem |

##### 12. Edge Cases & System States
| Journey | Example Screens |
|---|---|
| Empty States | First-time, No Results, No Access |
| Error States | 404, 500, Offline, Session Expired |
| Help & Support | Help Center, FAQ, Contact, Feedback |

### Step 3 — Build Design System Spec

→ Output: `projects/<name>/design_system.md`

Combines `system_context.md` + `style_references.md` (from Step 1b) to create:
- App Identity, Color Palette, Typography
- **Navigation Structure** (FIXED across all screens)
- Layout Grid, Component Patterns

### Step 4 — Build Detailed Prompts for Each Screen

→ Output: `projects/<name>/prompts/SXX_screen_name.md`

Each prompt contains **3 mandatory parts**:

```
┌─────────────────────────────────────────────┐
│  PART 1: DESIGN SYSTEM (copied from Step 3) │
│  → Ensures color, font, nav consistency     │
├─────────────────────────────────────────────┤
│  PART 2: SCREEN MAP CONTEXT                 │
│  → Summarizes all screens + current position│
│  → "This is screen 3/12: Alerts Console"    │
│  → Sidebar must highlight correct menu item │
├─────────────────────────────────────────────┤
│  PART 3: SCREEN CONTENT                     │
│  → Detailed layout for this screen          │
│  → Sample data (consistent cross-screen)    │
│  → Sections, interactions, states           │
└─────────────────────────────────────────────┘
```

### Step 5 — Select Stitch Project & Drawing Mode

**5a.** Call `list_projects` → display list → **ask user to choose** a project or create new.

**5b.** Ask user to choose **drawing mode**:
- **Interactive**: AI draws → presents → waits for feedback → edits → continues
- **Auto-feed**: AI draws all screens automatically → user reviews at the end

### Step 6 — Draw Screens in Journey Order

Execute per selected mode (Interactive / Auto-feed / Script batch).

### Step 7 — Review & Edit

Overall review → edit (`edit_screens`) → generate variants if needed.

### Step 8 — Export & Report

→ Output: `projects/<name>/wireframe_report.md`

---

## File Structure

```
stitchSkill/
├── SKILL.md                          # Main instructions (8 steps)
├── implementation_plan.md            # This plan (Vietnamese)
├── implementation_plan_en.md         # This plan (English)
├── templates/
│   ├── system_context_template.md
│   ├── screen_map_template.md
│   ├── design_system_template.md
│   ├── screen_prompt_template.md
│   └── generation_log_template.md
├── scripts/
│   ├── setup_auth.ps1                # One-time ADC login
│   ├── setup_project.js              # Create/list projects
│   └── batch_generate.js             # Batch generation
├── examples/
│   ├── tasklens_design_system.md
│   └── tasklens_screen_prompts.md
└── projects/                         # [RUNTIME] Per-project output
    └── <project-name>/
        ├── system_context.md         # From Step 1a
        ├── style_references.md       # From Step 1b
        ├── screen_map.md             # From Step 2
        ├── design_system.md          # From Step 3
        ├── prompts/                  # From Step 4
        │   ├── S01_dashboard.md
        │   ├── S02_task_list.md
        │   └── ...
        ├── generation_log.md         # From Step 6
        └── wireframe_report.md       # From Step 8
```

---

## Verification Plan

### Automated
1. `setup_auth.ps1` → verify ADC credentials exist
2. `node scripts/setup_project.js --dry-run` → verify API connectivity
3. `node scripts/batch_generate.js --dry-run` → verify prompt loading

### Manual
1. Full pipeline dry-run
2. Compare output with Stitch results
3. Evaluate: navigation consistency, data linkage, visual coherence

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
