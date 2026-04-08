| :--- | :--- | :--- |
| **OIW** | Intake Watchdog | Trấn giữ biên giới ngoại vi (Internet/Web), cào và thu gom tin tức, dữ liệu thô nạp từ ngoài vào. |
| **OSF** | Sandbox Firewall | Bức tường lửa thực thi việc quét mã độc (Heuristic Deep Scans) để chặn đứng việc lộ lọt API keys, Mật khẩu trước khi dữ liệu xâm nhập vào Core. |
| **OBD** | Bridge Daemon | Kẻ giữ bến cảng. Điểu khiển việc khởi chạy các tiến trình phụ rẽ nhánh, đo nhịp tim liên tục và truy sát các tiến trình zombie (Docker/Python). |
| **OHD** | Health Daemon | Giám sát nhịp tim hệ thống, mức độ ngốn CPU/RAM và đảm bảo các vòng lặp tác vụ không bị tràn bộ nhớ. |
| **OMA** | Master Architect | Chuyên gia định tuyến Bản đồ Cấu trúc. Gìn giữ thiết kế 4-Pillar của hệ thống và bắt giam bất cứ file nào nằm sai vị trí. |
| **OA** | Học Viện Đào Tạo | Cỗ máy tự tiến hóa. Đọc log hệ thống, tự động chắp vá quy trình hỏng, tuyển dụng Agent bù đắp chỗ trống. |
| **OER** | Ecosystem Registrar | Lễ tân tối cao. Đóng dấu duyệt thẻ Căn Cước (\_DIR_IDENTITY.md\) và nhập tịch các Node/Agent mới vào bản đồ hệ thống \FAST_INDEX.json\. | ID | Phòng Ban | Chức Năng | Agent Phụ Trách |
| :--- | :--- | :--- | :--- |
| **Dept 01** | **Kỹ Thuật** | Phát triển Backend, giao diện UI/UX và tích hợp AI. | `backend-architect` |
| **Dept 05** | **Chiến Lược** | Điều phối lộ trình, phân tích KPI và phát triển hệ thống. | `product-manager` |
| **Dept 09** | **Kiểm Duyệt** | Chốt chặn kiểm duyệt chất lượng nội dung và văn phong. | `editor-agent` |
| **Dept 10** | **An Ninh Strix** | Kiểm duyệt mã nguồn và thẩm định an ninh các thành phần bên ngoài. | `strix-agent` |
| **Dept 13** | **Nghiên Cứu Nova** | Nghiên cứu Deep Web và phát triển các thiết kế kiến trúc nền tảng. | `rd-lead` |
| **Dept 18** | **Thư Viện Tài Sản** | Quản lý vòng lặp bộ nhớ và Đồ thị Tri thức (Knowledge Graph). | `library-manager` |
| **Dept 20** | **Tiếp Nhận CIV** | Thu thập, phân tích và thẩm định các tài liệu/mã nguồn khẩn cấp. | `intake-chief` |
| **Dept 22** | **Vận Hành** | Vệ sinh phần cứng, dọn dẹp thư mục gốc và bảo vệ Git. | `scrum-master` |
| **Dept 23** | **Lễ Tân** | Tiếp nhận dự án tự động, thu thập brief và soạn thảo đề xuất. | `project-intake` |

> [!TIP]
> **Tìm hiểu sâu**: Để xem chi tiết 21 phòng ban, sơ đồ báo cáo và cách các agent tương tác, hãy xem bản [**Sơ đồ Tổng thể Hệ thống**](brain/knowledge/corp/MASTER_INDEX-vn.md).

> [!NOTE]
> Để xem danh sách đầy đủ 21 phòng ban và danh sách agent, vui lòng tham khảo file đăng ký `brain/corp/org_chart.yaml`.

---

---

## 🛡️ OAP Pipeline (Luồng Zero-Trust)

OmniClaw OS áp đặt một kỷ luật cực kỳ khắt khe: **Luồng Tự Trị OmniClaw (OAP)** nhằm kiểm soát toàn bộ vòng đời của dữ liệu và hệ thống quân lực. OAP hủy diệt mọi nguy cơ từ các file rác.

- **Cổng Báo Danh Duy Nhất (`OER_INBOX`)**: Bất cứ xưởng đúc nào tạo ra Agent mới hay Kỹ năng (Skill) đều không được phép vứt bừa vào bộ máy. Chúng buộc phải bị cách ly tại hàng đợi INBOX.
- **Định Danh Dưới Dạng Căn Cước (`_DIR_IDENTITY.md`)**: Mọi Phòng ban hay Agent đều phải sở hữu Căn Cước chính quy. Bất kỳ thực thể ma nào thiếu Căn Cước sẽ bị chặn đứng quyền biểu quyết bởi cổng Orchestrator.
- **Đồng Bộ Bản Đồ Cốt Lõi**: Những thực thể đã vượt qua đợt kiểm tra sẽ được nạp thông tin vào `FAST_INDEX.json`, chính thức "Hòa Mạng" vào hệ sinh thái.

---

## ⚙️ Core System Daemons (Tiến trình ngầm)

Để duy trì trạng thái luôn thức giấc, OmniClaw vắt sức của 7 Tiến trình Daemons bất tử hoạt động ngầm 24/7 dưới màn hình đen:

| Daemon | Tên Thể Hiện | Nhiệm vụ Tối Cáo |
| :--- | :--- | :--- |
| **OIW** | Intake Watchdog | Trấn giữ biên giới ngoại vi (Internet/Web), cào và thu gom tin tức, dữ liệu thô nạp từ ngoài vào. |
| **OHD** | Health Daemon | Giám sát nhịp tim hệ thống, mức độ ngốn CPU/RAM và đảm bảo các vòng lặp tác vụ không bị tràn bộ nhớ. |
| **OA** | Học Viện Đào Tạo | Cỗ máy tự tiến hóa. Đọc log hệ thống, tự động chắp vá quy trình hỏng, tuyển dụng Agent bù đắp chỗ trống. |
| **OER** | Ecosystem Registrar | Lễ tân tối cao. Đóng dấu duyệt thẻ Căn Cước (`_DIR_IDENTITY.md`) và nhập tịch các Node/Agent mới vào bản đồ hệ thống `FAST_INDEX.json`. |

---

## 🗺️ Master Map & Cấu Trúc Đồ Thị Tri Thức (Knowledge Tracking)

Để triệt tiêu tình trạng dữ liệu mồ côi hoặc lạc mất trên đường truyền, OmniClaw cấm tuyệt đối việc tạo ra các bản đồ rác rải rác (`MAP.md`). Thay vào đó, toàn bộ mạng lưới cấu trúc được định vị tập trung tại 2 Bảng Đồ Chí Tôn (Master Maps):

- **Bản đồ Truy Tốc (`FAST_INDEX.json`)**: Là cuốn sổ sinh tử của Hệ điều hành. Mọi Agent, Phòng Ban hay Kỹ năng đều phải được nạp thẻ Căn Cước vào đây. Bất cứ thực thể nào không có tên trong Fast Index sẽ tự động bị hệ thống từ chối quyền truy cập.
- **Cấu trúc Đồ Thị (`LIBRARY_GRAPH.json`)**: Định tuyến các sợi dây liên kết vô hình giữa hệ thống Quân Lực (Agents) và Siêu Khối Trí Tuệ (Knowledge). Đồ thị này giúp hệ thống nhận diện sâu sự phụ thuộc của Agent vào kiến trúc hạ tầng.
- **Tàng Kinh Các (`brain/knowledge`)**: Khu vực đóng băng lưu trữ trí nhớ dài hạn (Memory), các Bảng Cận Cảnh Chỉ Tiêu (KPI Scoreboard). Toàn bộ Quân lực chỉ được kết nối với Vùng Não này thông qua đường truyền Mapped Links bảo mật, đảm bảo không một bit dữ liệu nào bị xâm phạm trái phép.

---

## 🔒 Phân lập Quyền lực Tuyệt đối (OSF vs OA)

Nguyên tắc bất di bất dịch của kiến trúc Zero-Trust trong OmniClaw đó là sự phân tách giữa Năng lực Học tập và Quyền hạn Trừng phạt:
- **OSF (Sandbox Firewall)** sở hữu uy quyền độc tôn (Supreme Override) trên toàn bộ Vùng Cách ly (`QUARANTINE`). Chỉ những đặc vụ chuyên trách của OSD (`osf_warden`, `osf_auditor`, `osf_quarantine_guard`) mới được phép thao túng, cách ly và tiêu hủy mã độc thông qua Thiết Quân Luật.
- **OA (Academy)**, dù sở hữu năng lực định đoạt và thiết kế của một Đại trưởng lão, vẫn bị chặn đứng Quyền Lực khi chạm đến Sandbox phòng vệ. OA tuyệt đối không được tự ý tiếp cận các file nhiễm độc nếu chưa có con dấu làm sạch của OSF.

---

## 💽 Cài đặt

OmniClaw được xây dựng theo kiến trúc "Clone & Chạy" đơn giản.

```bash
# 1. Clone repository về máy cục bộ
git clone https://github.com/LongLeo287/omniclaw-local.git "OmniClaw"
cd "OmniClaw"

# 2. Liên kết hệ thống toàn cầu qua NPM
npm install -g .

# 3. Khởi chạy Monolithic OS Terminal (Có thể chạy từ bất cứ đâu)
omniclaw
```

*Mẹo cho Windows: Chúng tôi đã cung cấp khả năng truy cập GUI bản địa. Chỉ cần nhấp đúp vào script `omniclaw.bat` nằm trong thư mục gốc để mở ngay Bảng Điều khiển (Dashboard).*

---

## 📚 Hướng dẫn sử dụng & Quy trình vận hành

Khác với một kho lưu trữ code thông thường, OmniClaw là một hệ điều hành thực thụ. Hãy xem các tài liệu dưới đây để biết cách vận hành các quy trình tự động.

*   [**Quy trình nạp nguồn dữ liệu Github an toàn (CIV Intake)**](brain/knowledge/corp/docs/workflows/data_intake-vn.md)
*   [**Dọn rác hệ thống & Bảo vệ thư mục Vault**](brain/knowledge/corp/docs/workflows/deep_cleaner-vn.md)

---

## 📖 Sơ Đồ Hệ Thống & Hướng Dẫn Chi Tiết

Để hiểu sâu hơn về kiến trúc hệ thống, các luồng dịch vụ và kỹ năng của Agent, vui lòng tham khảo các bản đồ tổng quan:

* 🏛️ [**Các Nguyên Tắc Lõi Kiến Trúc**](brain/knowledge/corp/docs/architecture/CORE_PRINCIPLES-vn.md) — Phân tích chi tiết tại sao Lõi Hệ thống phải là Tiếng Anh và Cơ chế Bộ nhớ rỗng (Zero-Config Memory).
* 🧭 [**Sơ Đồ Hệ Thống Tổng Thể**](brain/knowledge/corp/docs/architecture/MASTER_SYSTEM_MAP-vn.md) — Sơ đồ toàn diện: Tổ chức 21 phòng ban, Boot Sequence, Bộ nhớ, và quy trình Gate.
* 🚦 [**Bảng Điều Khiển Khởi Động**](brain/knowledge/corp/docs/usage_guides/ACTIVATION_GUIDE-vn.md) — Danh sách Port và lệnh khởi động cho toàn bộ dịch vụ Local (LobsterBoard, LightRAG, v.v.).
* 🧩 [**Bản Đồ Plugins & Kỹ Năng**](brain/knowledge/corp/docs/architecture/SKILLS_AND_PLUGINS_MAP-vn.md) — Mục lục tham chiếu 100+ kỹ năng và Plugins dành cho AI Agent.
* 📊 [**Kho Dữ Liệu Khoa Học**](brain/knowledge/corp/docs/usage_guides/DATA_SCIENCE_LIBRARY-vn.md) — Danh sách các Repositories mẫu về Machine Learning & RAG hiện hành.
* 🏛️ [**Tứ Trụ Daemon & OER — Quản Trị Hệ Sinh Thái**](brain/knowledge/corp/docs/architecture/CORE_DAEMONS_AND_OER-vn.md) — 4 Core Daemon (OIW/OHD/OA/OER), Ma Trận Phân Quyền và Pipeline 5-Gate tự động toàn diện.

---

## 🌐 Cộng đồng & Hỗ trợ

Bạn có ý tưởng, câu hỏi hoặc muốn giới thiệu các quy trình Agent tùy chỉnh của mình? Chúng tôi đã xây dựng một không gian riêng để đội ngũ OmniClaw cùng nhau thảo luận.

**[🚀 Tham gia không gian Thảo luận của OmniClaw](https://github.com/LongLeo287/omniclaw-local/discussions)**

---

## 🙏 Lời cảm ơn & Tri ân

OmniClaw được xây dựng dựa trên nền tảng của các kiến trúc mã nguồn mở vĩ đại. Chúng tôi chân thành cảm ơn các tổ chức và dự án sau:

*   **[Anthropic](https://anthropic.com)**: Cho Claude Code CLI và cấu trúc REPL tuyệt vời.
*   **[Google Deepmind](https://deepmind.google.com/technologies/gemini/)**: Cho các mô hình Gemini và khả năng phân tích cấu trúc ngữ cảnh sâu sắc chưa từng có.
*   **[affaan-m / everything-claude-code](https://github.com/affaan-m/everything-claude-code)**: Cho các quy trình bảo vệ Agent đa nền tảng và các mẫu chỉ dẫn dựa trên vai trò.
*   **[LightRAG](https://github.com/HKUDS/LightRAG)**: Cung cấp hệ thống truy xuất tri thức dựa trên đồ thị chính xác và mạnh mẽ.
*   **[Firecrawl](https://firecrawl.dev)**: Vận hành quy trình trích xuất markdown hoàn hảo.
*   **[Mem0](https://github.com/mem0ai/mem0)**: Cách mạng hóa việc lưu giữ bộ nhớ dài hạn cho các AI agent.
*   **[CrewAI](https://crewai.com)**: Cảm hứng cho mạng lưới worker-thread và sub-agent cục bộ.
*   **[Cursor](https://cursor.sh)** / **OpenCode**: Các môi trường IDE được lựa chọn, tạo điều kiện cho liên kết thần kinh giữa OS và CEO.

<br>
<div align="center">
  <i>"Hệ Điều Hành Của Tương Lai, Đang Chạy Trên Bàn Làm Việc Của Bạn Hôm Nay."</i>
</div>
