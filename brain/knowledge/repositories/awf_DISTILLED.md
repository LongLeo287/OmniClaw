---
id: repo-fetched-awf-093333
type: knowledge
owner: OA
registered_at: 2026-04-05T03:45:51.694899
tags: ["auto-cloned", "oa-assimilated"]
---

# FETCHED_awf_093333

## Assimilation Report
Auto-cloned repository: FETCHED_awf_093333

## Application for OmniClaw
No structural integration blueprint provided.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
🇻🇳 **Tiếng Việt** | [🇬🇧 English](README.en.md)

# ⚡ AWF v4.0 - Antigravity Workflow Framework

> **Framework mở rộng cho Antigravity Agent.**
> Biến AI của bạn thành một đội ngũ chuyên nghiệp (PM, Designer, Coder) với quy trình làm việc chuẩn.

[![Version](https://img.shields.io/badge/version-4.1.0-blue.svg)](https://github.com/TUAN130294/awf)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Website](https://img.shields.io/badge/Website-awfweb.pages.dev-8b5cf6.svg)](https://awfweb.pages.dev/)

🌐 **Website:** [https://awfweb.pages.dev/](https://awfweb.pages.dev/)

---

## ✨ Tính Năng Chính

- 🤖 **Multi-Persona AI**: Đội ngũ AI chuyên biệt (PM Hà, Dev Tuấn, Designer Mai, QA Long)
- 🧠 **Context Vĩnh Cửu**: Tự động lưu và khôi phục session làm việc
- 📦 **All-in-One**: Không cần cài thêm bất kỳ skill/agent nào khác
- 🔄 **Auto-Update**: Tự động kiểm tra và cập nhật phiên bản mới

---

## 🚀 Cài Đặt (Chỉ 1 Lệnh)

### Windows (PowerShell)
Mở Terminal (**Ctrl + `**) và dán:

```powershell
irm https://raw.githubusercontent.com/TUAN130294/awf/main/install.ps1 | iex
```

### macOS / Linux
```bash
curl -fsSL https://raw.githubusercontent.com/TUAN130294/awf/main/install.sh | sh
```

**Xong!** ✅ AWF sẽ tự động tải và cấu hình vào Antigravity.

> ⚠️ **Windows: Gặp lỗi ExecutionPolicy?** Chạy lệnh này trước:
> ```powershell
> Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

---

## 🎮 Cách Sử Dụng

Sau khi cài xong, gõ lệnh này vào khung Chat của Antigravity:

```
/init
```

AI sẽ hỏi bạn muốn làm dự án gì và tự động hướng dẫn từng bước.

---

## 🗺️ Các Lệnh Chính

| Lệnh | Chức năng | Mô tả |
|------|-----------|-------|
| `/init` | 🏁 Khởi động | Bắt đầu dự án mới |
| `/plan` | 📝 Kế hoạch | AI đóng vai PM, phỏng vấn yêu cầu |
| `/visualize` | 🎨 Thiết kế | Tạo UI/UX trước khi code |
| `/code` | 💻 Viết code | AI tự động lập trình theo spec |
| `/run` | ▶️ Chạy | Khởi động ứng dụng |
| `/debug` | 🐛 Sửa lỗi | Phân tích và fix bug tự động |
| `/test` | ✅ Kiểm thử | Chạy test cases |
| `/deploy` | 🚀 Deploy | Đẩy lên production |
| `/recap` | 🧠 Nhớ lại | Khôi phục context từ session cũ |
| `/awf-update` | 🔄 Cập nhật | Kiểm tra và update AWF |

---

## 📂 Cấu Trúc Thư Mục (Sau Cài Đặt)

```
~/.gemini/antigravity/
├── global_workflows/    # Các workflow chính (/init, /plan, /code...)
├── skills/              # AWF Skills (auto-activate)
├── schemas/             # JSON Schemas
└── templates/           # Mẫu cấu hình
```

---

## 🔄 Cập Nhật

Để kiểm tra và cập nhật lên phiên bản mới nhất, gõ:
```
/awf-update
```

---

## 📚 Tài Liệu Chi Tiết
Mở file `docs/index.html` để xem hướng dẫn đầy đủ với giao diện đẹp.

---

## 📜 Changelog

### v4.1.0 (Latest)
- 🆕 **Eternal Context System** - Auto-save để không bao giờ mất context
- 🆕 Skill `awf-auto-save` với trigger thông minh
- 🆕 3-Tier lazy loading cho session restore
- ✅ Session schema v2.0 với summary & checkpoints

### v4.0.1
- ✅ Fix lỗi install script trên Windows
- ✅ Cải thiện Session Restore skill
- ✅ Thêm `/awf-update` workflow

### v4.0.0
- 🆕 Skill System (awf-session-restore, awf-error-translator...)
- 🆕 Schemas & Templates
- 🆕 Multi-language support

---

**Happy Vibe Coding!** 🚀
*Authored by Antigravity Team*

```

### File: CODE_OF_CONDUCT.md
```md
# Quy Tắc Ứng Xử

## Cam Kết

Chúng tôi cam kết tạo một môi trường mở, thân thiện cho tất cả mọi người, bất kể kinh nghiệm, giới tính, bản dạng, dân tộc, tôn giáo, hay quốc tịch.

## Tiêu Chuẩn

**Hành vi được khuyến khích:**
- Sử dụng ngôn ngữ thân thiện
- Tôn trọng quan điểm khác biệt
- Chấp nhận phê bình mang tính xây dựng
- Tập trung vào lợi ích cộng đồng

**Hành vi không được chấp nhận:**
- Ngôn ngữ xúc phạm, quấy rối
- Troll, bình luận mang tính công kích
- Công khai thông tin cá nhân người khác
- Các hành vi không phù hợp khác

## Thực Thi

Các trường hợp vi phạm có thể được báo cáo qua [Issues](https://github.com/TUAN130294/awf/issues). Đội ngũ duy trì sẽ xem xét và xử lý phù hợp.

## Phạm Vi

Quy tắc này áp dụng trong tất cả không gian của dự án, bao gồm Issues, Pull Requests, Discussions, và các kênh liên lạc khác.

---

Quy tắc này được lấy cảm hứng từ [Contributor Covenant](https://www.contributor-covenant.org/).

```

### File: CONTRIBUTING.md
```md
# Đóng Góp cho AWF

Cảm ơn bạn muốn đóng góp cho AWF! 🎉

## 🚀 Cách Đóng Góp

### Báo Lỗi (Bug Report)
1. Kiểm tra [Issues](https://github.com/TUAN130294/awf/issues) xem lỗi đã được báo chưa
2. Tạo Issue mới với template **Bug Report**
3. Mô tả chi tiết: bước tái hiện, kết quả mong đợi, kết quả thực tế

### Đề Xuất Tính Năng
1. Tạo Issue mới với template **Feature Request**
2. Giải thích vấn đề bạn gặp và cách tính năng mới sẽ giải quyết

### Gửi Code (Pull Request)
1. **Fork** repo này
2. Tạo branch mới: `git checkout -b feature/ten-tinh-nang`
3. Code và test
4. Commit với message rõ ràng: `feat: thêm tính năng XYZ`
5. Push và tạo **Pull Request**

## 📋 Quy Tắc

- Giữ code đơn giản, dễ đọc
- Viết commit message theo [Conventional Commits](https://www.conventionalcommits.org/)
- Test trên cả Windows (PowerShell) và macOS/Linux (Bash)
- Cập nhật README nếu thêm tính năng mới
- Tôn trọng mọi người trong cộng đồng

## 🗂️ Cấu Trúc Thư Mục

```
awf/
├── workflows/       # Các workflow chính (/init, /plan, /code...)
├── awf_skills/      # AWF Skills
├── schemas/         # JSON Schemas
├── templates/       # Mẫu cấu hình
├── docs/            # Tài liệu
├── install.ps1      # Script cài đặt Windows
└── install.sh       # Script cài đặt macOS/Linux
```

## 💬 Cần Hỗ Trợ?

- Mở [Discussion](https://github.com/TUAN130294/awf/discussions) để hỏi
- Đọc [Tài liệu](https://awfweb.pages.dev/) trước khi hỏi

Mọi đóng góp đều được trân trọng! ❤️

```

### File: README.en.md
```md
[🇻🇳 Tiếng Việt](README.md) | 🇬🇧 **English**

# AWF v4.0 - Antigravity Workflow Framework

> **Extension framework for Antigravity Agent.**
> Transform your AI into a professional team (PM, Designer, Coder) with standardized workflows.

[![Version](https://img.shields.io/badge/version-4.0.1-blue.svg)](https://github.com/TUAN130294/awf)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

---

## Why AWF?

**Traditional AI coding:**
```
You: "Build me a todo app"
AI: *dumps 500 lines of code*
You: "Wait, what? Where do I put this?"
```

**With AWF:**
```
You: /init
AI: "What kind of app do you want to build? Tell me in plain language..."
    *guides you step by step*
    *explains everything in simple terms*
    *remembers context across sessions*
```

---

## Key Features

- **Multi-Persona AI**: Specialized AI team (PM Ha, Dev Tuan, Designer Mai, QA Long)
- **Eternal Context**: Auto-save and restore your working session
- **All-in-One**: No need to install additional skills/agents
- **Non-Tech Friendly**: Technical jargon automatically translated to plain language
- **Auto-Update**: Check and update to latest version anytime

---

## Quick Install (One Command)

### Windows (PowerShell)
Open Terminal (**Ctrl + `**) and paste:

```powershell
irm https://raw.githubusercontent.com/TUAN130294/awf/main/install.ps1 | iex
```

### macOS / Linux
```bash
curl -fsSL https://raw.githubusercontent.com/TUAN130294/awf/main/install.sh | sh
```

**Done!** AWF will automatically download and configure into Antigravity.

> **Windows: ExecutionPolicy error?** Run this first:
> ```powershell
> Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

---

## Getting Started

After installation, type this in Antigravity Chat:

```
/init
```

AI will ask what project you want to build and guide you step by step.

---

## Command Reference

### Project Lifecycle

| Command | Function | Description |
|---------|----------|-------------|
| `/init` | Bootstrap | Start a new project from scratch |
| `/brainstorm` | Ideation | Explore and refine your idea |
| `/plan` | Planning | AI acts as PM, interviews requirements |
| `/visualize` | Design | Create UI/UX before coding |
| `/code` | Development | AI codes according to spec |
| `/run` | Execute | Launch your application |
| `/debug` | Fix Bugs | Analyze and fix errors automatically |
| `/test` | Testing | Run test cases |
| `/deploy` | Ship | Push to production |

### Context & Memory

| Command | Function | Description |
|---------|----------|-------------|
| `/recap` | Remember | Restore context from previous session |
| `/save-brain` | Save | Store project knowledge for later |
| `/next` | Navigate | Get suggestions for next steps |

### Customization

| Command | Function | Description |
|---------|----------|-------------|
| `/customize` | Personalize | Set AI communication style |
| `/awf-update` | Update | Check and update AWF |

---

## For Non-Technical Users

AWF automatically adjusts its language based on your technical level:

### Technical Level: Newbie
```
Database     → "Storage for your app's information"
API          → "Bridge between different software"
Deploy       → "Put your app online for others to use"
Debug        → "Find and fix problems"
```

### Error Translation
When errors happen, AWF translates them:
```
ECONNREFUSED     → "Database not running - start your database app"
Cannot find module → "Missing library - run npm install"
CORS error       → "Server blocking request - needs server config"
```

---

## AI Personas

AWF includes specialized AI personalities:

| Persona | Role | Style |
|---------|------|-------|
| **Ha** | Product Manager | Friendly, asks clarifying questions, prioritizes user needs |
| **Tuan** | Senior Developer | Patient, explains the "why", never judges |
| **Mai** | UX Designer | Visual thinker, uses real-world examples |
| **Long** | QA Detective | Calm, thorough, always has a hypothesis |

---

## Folder Structure (After Install)

```
~/.gemini/antigravity/
├── global_workflows/    # Main workflows (/init, /plan, /code...)
├── skills/              # AWF Skills (auto-activate)
├── schemas/             # JSON Schemas
└── templates/           # Configuration templates
```

---

## AWF Skills (Auto-Activate)

These skills work silently in the background:

| Skill | Trigger | Function |
|-------|---------|----------|
| `awf-session-restore` | Session start | Auto-restore previous context |
| `awf-adaptive-language` | Session start | Adjust language to user level |
| `awf-error-translator` | On error | Translate technical errors to plain language |
| `awf-context-help` | `/help` or `?` | Smart help based on current context |

---

## Update

To check and update to the latest version:
```
/awf-update
```

---

## Workflow Chain

```
/brainstorm → /plan → /visualize → /code → /test → /deploy
      ↓                              ↓
   BRIEF.md                      /debug (if errors)
                                     ↓
                                /save-brain (end of session)
```

---

## Configuration

### Personality Modes (via /customize)

**Mentor Mode:**
- Explains WHY, not just HOW
- Asks questions back to make you think
- "Do you understand why we use try-catch here?"

**Strict Coach Mode:**
- High standards for code quality
- Points out best practices
- "This approach isn't optimal because..."

### Technical Levels

| Level | Behavior |
|-------|----------|
| `newbie` | Hide all technical details, explain everything |
| `basic` | Mix of simple and technical terms |
| `technical` | Full technical terminology, no explanations |

---

## Changelog

### v4.0.1 (Latest)
- Fix Windows install script issues
- Improved Session Restore skill
- Added `/awf-update` workflow

### v4.0.0
- New Skill System (awf-session-restore, awf-error-translator...)
- Schemas & Templates
- Multi-language support
- Non-Tech Mode for all workflows

### v3.2.4
- Flexible `/customize` options
- Response length settings
- Global + Local preferences

---

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## Support

- Issues: [GitHub Issues](https://github.com/TUAN130294/awf/issues)
- Discussions: [GitHub Discussions](https://github.com/TUAN130294/awf/discussions)

---

## License

MIT License - feel free to use in personal and commercial projects.

---

**Happy Vibe Coding!**

*Authored by Antigravity Team*

```

### File: SECURITY.md
```md
# 🔒 Security Policy

## Phiên Bản Được Hỗ Trợ

| Version | Supported          |
| ------- | ------------------ |
| 4.1.x   | ✅ Đang hỗ trợ    |
| < 4.0   | ❌ Không hỗ trợ   |

## Báo Cáo Lỗ Hổng Bảo Mật

Nếu bạn phát hiện lỗ hổng bảo mật, **KHÔNG tạo Issue công khai**.

Thay vào đó, vui lòng:
1. Gửi email đến: **tuan130294@gmail.com**
2. Mô tả chi tiết lỗ hổng
3. Chờ phản hồi trong vòng 48 giờ

Chúng tôi sẽ xử lý và phát hành bản vá trong thời gian sớm nhất.

```

### File: VETTING_REPORT.md
```md
---
title: Auto Vetting Report for awf
date: 2026-04-05
analyst: civ_vetting_pipeline
status: AUTO_VETTED
---

# Auto-Vetted Repository
This repository was automatically swept and vetted by the batch processor. Only documentation remains.

```

### File: .github\PULL_REQUEST_TEMPLATE.md
```md
## Mô Tả Thay Đổi
<!-- Mô tả ngắn gọn thay đổi trong PR này -->

## Loại Thay Đổi
- [ ] 🐛 Sửa lỗi (Bug fix)
- [ ] ✨ Tính năng mới (New feature)
- [ ] 📝 Cập nhật tài liệu (Documentation)
- [ ] ♻️ Refactor code
- [ ] 🎨 Style/UI

## Đã Test Chưa?
- [ ] Windows (PowerShell)
- [ ] macOS / Linux (Bash)

## Checklist
- [ ] Code đã được test
- [ ] README đã được cập nhật (nếu cần)
- [ ] Không có breaking changes

## Ảnh Chụp (nếu có)
<!-- Thêm ảnh chụp nếu liên quan đến UI -->

```

### File: docs\ETERNAL_CONTEXT_DESIGN.md
```md
# Eternal Context System - AWF 4.1

> Auto-save context thong minh, khong bao gio mat du lieu.

---

## 1. Van De

- Context window gioi han (128K tokens)
- Khi day, AI "quen" thong tin cu (auto compact)
- User phai nho go `/save-brain` thu cong
- Load lai toan bo brain = ton token

---

## 2. Giai Phap: 3-Tier System

### Tier 1: CRITICAL (Khong bao gio xoa)
```yaml
# ~200-500 tokens
project:
  name: "MyApp"
  tech_stack: ["Next.js", "Prisma"]

key_decisions:
  - decision: "Use NextAuth"
    reason: "Simple, team familiar"
```

### Tier 2: IMPORTANT (Giu trong session)
```yaml
# ~300-800 tokens
working_on:
  feature: "Authentication"
  task: "Login form"
  progress: 65%

errors_history:
  - error: "CORS"
    fixed: true
```

### Tier 3: CONTEXT (Tam thoi)
```yaml
# ~500-2000 tokens
conversation_summary:
  - "Discussed auth options, picked NextAuth"

recent_files:
  - "src/app/login/page.tsx"
```

---

## 3. Auto-Save Triggers

| Trigger | Hanh dong |
|---------|-----------|
| Workflow hoan thanh | Save Tier 1+2 |
| Quyet dinh duoc dua ra | Append vao decisions |
| Loi duoc fix | Log vao errors_history |
| Moi 15 tin nhan | Background checkpoint |
| User roi di ("bye", "tam nghi") | Full save + summary |
| Context > 80% (uoc tinh) | Emergency save |

### Pattern Detection
```yaml
user_leaving:
  - "toi di", "tam nghi", "bye", "het gio"

decision_made:
  - "chon", "dung cai nay", "ok lam vay", "dong y"

milestone:
  - "xong", "done", "hoan thanh", "pass test"
```

### Token Estimation (Heuristic)
```
tokens = messages * 150 + code_lines * 5 + errors * 300

if tokens > 100000:  # 80% of 128K
    emergency_save()
    warn("Context sap day, da save. Go /recap de tiep tuc.")
```

---

## 4. File Structure

```
.brain/
├── brain.json              # Tier 1: Static knowledge
├── session.json            # Tier 2: Current state
├── session_log.txt         # Append-only log
│
├── snapshots/              # Historical
│   └── 2024-01-15_1430.json
│
├── summaries/
│   ├── project_summary.md  # Human-readable
│   └── context_digest.json # Quick reload
│
└── cache/                  # Temporary
    └── last_conversation.json
```

---

## 5. Lazy Loading

### Level 1: Instant (<500 tokens) - LUON LOAD
- Project name, tech stack
- Current task/feature
- Active errors

### Level 2: On-Demand (~1000 tokens) - KHI CAN
- Key decisions lien quan
- Recent files
- Pending tasks

### Level 3: Deep Dive (~2000+ tokens) - KHI YEU CAU
- Full decision history
- All summaries
- Error history

### /recap Redesign
```
/recap         → Level 1 only (nhanh)
/recap full    → Level 1 + 2
/recap [topic] → Smart search ("recap auth")
```

---

## 6. Token Optimization

### Summarization (10:1 compression)
```
Before: "User asked about auth options. I explained JWT vs Session..."
After:  "Decision: Use NextAuth (simple > flexible)"
```

### Delta Updates
```json
{
  "deltas": [
    { "time": "09:30", "action": "started_task", "data": "login" },
    { "time": "09:45", "action": "error_fixed", "data": "CORS" }
  ]
}
```

### Reference Pattern
```yaml
# Khong lap lai
task_1:
  uses: "$project.tech_stack"  # Reference
```

### Token Budget
```
128K total
├── System: 10K (fixed)
├── Conversation: 100K
├── Brain Load: 8K max
│   ├── L1: 500
│   ├── L2: 2000
│   └── L3: 5500
└── Buffer: 10K
```

---

## 7. Edge Cases

| Case | Xu ly |
|------|-------|
| File corrupted | Load snapshot → Ask user rebuild |
| Conflicting info | Show conflict → User chon |
| Project qua dai | Archive old snapshots (>7 ngay) |
| Context day | Warn user → User quyet dinh |

### Emergency Protocol (Warn Only)
```
1. Detect context > 80% (estimate)
2. Auto-save current state
3. Show warning: "⚠️ Context sap day. Go /save-brain roi bat dau session moi."
4. User tu quyet dinh khi nao reset
```

---

## 8. Auto-Inject (Session Start)

```markdown
# System prompt addition

## Project Context
- Project: MyApp (E-commerce)
- Stack: Next.js, Prisma
- Current: Authentication
- Task: Login validation (65%)
- Errors: None

[User message continues...]
```

---

## 9. Implementation Phases

### Phase 1: Core (P0)
- [ ] 3-Tier brain.json structure
- [ ] Auto-save on workflow end
- [ ] Basic /recap levels

### Phase 2: Smart Triggers (P1)
- [ ] Pattern detection
- [ ] Token estimation
- [ ] Decision extraction

### Phase 3: Optimization (P2)
- [ ] Summarization
- [ ] Delta updates
- [ ] Snapshot management

### Phase 4: Polish (P3)
- [ ] Edge cases
- [ ] User-friendly messages
- [ ] Testing

---

## 10. Commands

| Command | Chuc nang |
|---------|-----------|
| `/recap` | Load Level 1, tom tat nhanh |
| `/recap full` | Load Level 1+2, chi tiet |
| `/recap [topic]` | Tim theo chu de |
| `/save-brain` | Manual save (existing) |

---

## 11. User Messages (Co thong bao)

```
[Auto-save - workflow end]
"💾 Da luu tien do. Ban co the dong app an toan."

[Auto-save - user leaving detected]
"💾 Thay ban chuan bi di, da auto-save session."

[Context warning - 80%]
"⚠️ Context sap day. Da save backup. Nen go /save-brain roi bat dau session moi."

[Session restore]
"👋 Chao mung tro lai! Ban dang lam [feature], task: [task]."
```

## 12. Config

```yaml
# Quyet dinh da duoc dua ra:
notifications: true          # Hien thong bao khi auto-save
snapshot_retention: 7        # Giu snapshots 7 ngay
emergency_protocol: "warn"   # Chi warn, khong auto reset
```

---

## Summary

| Aspect | Solution |
|--------|----------|
| What | 3-tier (Critical/Important/Context) |
| When | Pattern + Workflow + Heuristic triggers |
| Where | brain.json + session.json + snapshots (7 ngay) |
| Load | Lazy (Level 1/2/3) |
| Optimize | Summarize + Delta + Reference |
| Edge | Warn only, user quyet dinh |
| Notification | Co thong bao khi save |

**Token overhead: <5% cua conversation binh thuong**

---

*Version: 1.0 - AWF 4.1 Design*
*Decisions: notifications=true, retention=7d, emergency=warn*

```

### File: .github\ISSUE_TEMPLATE\bug_report.md
```md
---
name: 🐛 Báo Lỗi (Bug Report)
about: Báo cáo lỗi để giúp AWF tốt hơn
title: '[BUG] '
labels: bug
assignees: TUAN130294
---

## Mô Tả Lỗi
<!-- Mô tả rõ ràng lỗi gặp phải -->

## Các Bước Tái Hiện
1. Gõ lệnh `...`
2. Chọn `...`
3. Xem lỗi xuất hiện

## Kết Quả Mong Đợi
<!-- Bạn mong đợi điều gì xảy ra? -->

## Kết Quả Thực Tế
<!-- Thực tế điều gì xảy ra? -->

## Ảnh Chụp Màn Hình
<!-- Nếu có, thêm ảnh chụp để mô tả rõ hơn -->

## Môi Trường
- **OS:** [VD: Windows 11 / macOS 14 / Ubuntu 22.04]
- **AWF Version:** [VD: v4.1.0]
- **Antigravity Version:** [VD: latest]

## Thông Tin Thêm
<!-- Bất kỳ thông tin nào khác có thể hữu ích -->

```

### File: .github\ISSUE_TEMPLATE\feature_request.md
```md
---
name: 💡 Đề Xuất Tính Năng (Feature Request)
about: Đề xuất ý tưởng mới cho AWF
title: '[FEATURE] '
labels: enhancement
assignees: TUAN130294
---

## Vấn Đề
<!-- Bạn đang gặp vấn đề gì? VD: "Tôi thấy khó chịu khi..." -->

## Giải Pháp Đề Xuất
<!-- Mô tả tính năng bạn muốn thêm -->

## Lợi Ích
<!-- Tính năng này giúp ích gì cho người dùng? -->

## Phương Án Thay Thế
<!-- Bạn đã thử cách nào khác chưa? -->

## Thông Tin Thêm
<!-- Ảnh chụp, link tham khảo, etc. -->

```

### File: .github\ISSUE_TEMPLATE\question.md
```md
---
name: ❓ Hỏi Đáp (Question)
about: Hỏi về cách sử dụng AWF
title: '[Q&A] '
labels: question
assignees: ''
---

## Câu Hỏi
<!-- Mô tả câu hỏi của bạn -->

## Bạn Đã Thử Gì?
<!-- Bạn đã đọc docs / thử lệnh gì rồi? -->

## Môi Trường
- **OS:** [VD: Windows 11]
- **AWF Version:** [VD: v4.1.0]

```

