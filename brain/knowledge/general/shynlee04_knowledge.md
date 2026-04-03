---
id: shynlee04-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:13.639119
---

# KNOWLEDGE EXTRACT: shynlee04
> **Extracted on:** 2026-03-30 17:53:20
> **Source:** shynlee04

---

## File: `hivemind-plugin.md`
```markdown
# 📦 shynlee04/hivemind-plugin [🔖 PENDING/APPROVE]
🔗 https://github.com/shynlee04/hivemind-plugin


## Meta
- **Stars:** ⭐ 53 | **Forks:** 🍴 18
- **Language:** TypeScript | **License:** MIT
- **Last updated:** 2026-03-01
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
(No description)

## README (trích đầu)
```
# HiveMind Context Governance

> **The operating system for AI coding sessions.**

## 🇻🇳 Bản phát hành v2.8 ưu tiên thị trường Việt Nam

HiveMind là plugin [OpenCode](https://opencode.ai) giúp AI agent không bị trôi ngữ cảnh, không quên quyết định Architecture, và không mất Status: khi session kéo dài. Trọng tâm v2.8: onboarding rõ ràng, governance chặt, và triển khai thực chiến cho team Việt Nam trước.

### 10 kịch bản demo ấn tượng để ra mắt
1. `SaaS 0→1 cho người không biết code`: menu hỏi đáp + auto-lane để ra PRD có thể triển khai.
2. `Giải cứu prompt hỗn loạn của team enterprise`: bóc tách yêu cầu, ambiguity map, risk register.
3. `War-room production incident`: ép agent đi theo checklist bằng chứng trước khi kết luận fix.
4. `TDD autopilot`: agent chuyển tự động từ `spec -> build -> validate` với gate kiểm thử.
5. `MCP-first research sprint`: phối hợp Context7/DeepWiki/Tavily/Exa/Repomix và chấm điểm confidence.
6. `Brownfield modernization`: quét codebase cũ, lập workflow refactor theo từng lane và checkpoint.
7. `Cross-domain planning`: cùng một khung cho dev + marketing + finance + office-ops.
8. `Subagent swarm governance`: giao việc song song nhưng vẫn giữ được trace, export, và hồi cứu.
9. `Bilingual coaching mode`: đầu ra EN/VI cùng cấu trúc, hỗ trợ onboarding team đa vai trò.
10. `No-command recovery`: người dùng nói tự nhiên, hệ thống tự realign sang lệnh phù hợp và xin quyền bước tiếp theo.

# 🇻🇳 Hướng Dẫn Tiếng Việt (Chi Tiết)

> *Phần này không phải bản dịch — mà được viết riêng cho người dùng Việt Nam, với giải thích kỹ hơn về cách hoạt động và lý do tại sao.*

**Cảm thấy hữu ích?** [![Mời cà phê](https://img.shields.io/badge/Mời%20cà%20phê-ủng%20hộ-orange?logo=buy-me-a-coffee&logoColor=white)](https://buymeacoffee.com/shynlee04l)

## HiveMind Là Gì?

Hãy tưởng tượng bạn thuê một lập trình viên AI rất giỏi, nhưng anh ta có một Problem: **mỗi 30 phút anh ta quên hết mọi thứ đang làm**.

Đó chính xác là điều xảy ra với các AI coding agent hiện tại:
- Đang làm feature A, tự nhiên nhảy sang feature B mà không checkpoint
- Sau context compaction (khi hết bộ nhớ), quên hết lý do tại sao đã quyết định Architecture X
- Giao việc cho subagent, nhận Result: nhưng không tổng hợp lại
- Session mới bắt đầu từ con số 0 — không biết gì về session trước

**HiveMind giải quyết tất cả** bằng một hệ thống quản trị context đơn giản nhưng hiệu quả.

## Cách Hoạt Động (Giải Thích Dễ Hiểu)

Mỗi session làm việc với AI đều tuân theo một quy trình:

```
declare_intent → map_context → [làm việc] → compact_session
   (khai báo)     (cập nhật)     (code)      (lưu trữ)
```

### Step 1: Khai Báo Ý Định — `declare_intent`

Trước khi bắt đầu bất kỳ công việc nào, agent phải nói rõ:
- **Đang làm gì**: "Xây dựng hệ thống xác thực"
- **Làm theo cách nào**: `plan_driven` (có kế hoạch), `quick_fix` (sửa nhanh), hoặc `exploration` (tìm hiểu)

Nếu không khai báo, ở chế độ `strict` agent sẽ bị khóa — không thể ghi file cho đến khi khai báo. Điều này đảm bảo mọi công vi
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

