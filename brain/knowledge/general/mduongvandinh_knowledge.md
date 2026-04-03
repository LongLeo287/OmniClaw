---
id: mduongvandinh-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:07.329407
---

# KNOWLEDGE EXTRACT: mduongvandinh
> **Extracted on:** 2026-03-30 17:42:29
> **Source:** mduongvandinh

---

## File: `springboot-best-practices.md`
```markdown
# 📦 mduongvandinh/springboot-best-practices [🔖 PENDING/APPROVE]
🔗 https://github.com/mduongvandinh/springboot-best-practices


## Meta
- **Stars:** ⭐ 36 | **Forks:** 🍴 11
- **Language:** N/A | **License:** Unknown
- **Last updated:** 2026-03-07
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
springboot-best-practices

## README (trích đầu)
```
# Spring Boot Best Practices Skill



**174 best practices | 19 domains | Scoring 0-100 | Vietnamese**



Bộ công cụ tự động quét mã nguồn Spring Boot, đánh giá mức tuân thủ **174 best practices** trong **19 lĩnh vực**, chấm điểm 0-100 mỗi domain với trọng số. Hỗ trợ cả **Claude Code** và **Google Antigravity**.



> Bổ sung cho [Engineering Failures Audit Skill](https://github.com/mduongvandinh/engineering-failures/) — skill này **đề xuất chuẩn mực** (proactive), còn Engineering Failures **phát hiện lỗi** (reactive).



---



## Mục lục



- [Installation:](#cài-đặt)

  - [Claude Code](#claude-code)

  - [Google Antigravity](#google-antigravity)

- [Sử dụng](#sử-dụng)

  - [Claude Code](#sử-dụng-trong-claude-code)

  - [Google Antigravity](#sử-dụng-trong-google-antigravity)

- [19 Lĩnh vực](#19-lĩnh-vực)

- [Mức độ & Chấm điểm](#mức-độ--chấm-điểm)

- [Cấu trúc dự án](#cấu-trúc-dự-án)

- [Format mỗi best practice](#format-mỗi-best-practice)

- [Giấy phép](#giấy-phép)



---



## Installation:



### Claude Code



**Cách 1: Clone trực tiếp**



```bash

git clone https://github.com/mduongvandinh/springboot-best-practices.git \

  ~/.claude/skills/springboot-best-practices

```



**Cách 2: Copy thủ công**



```bash

cp -r springboot-best-practices/ ~/.claude/skills/springboot-best-practices/

```



**Xác nhận Installation:**



```bash

ls ~/.claude/skills/springboot-best-practices/

# springboot-best-practices.skill  knowledge/  README.md

```



### Google Antigravity



**Step 1: Clone**



```bash

git clone https://github.com/mduongvandinh/springboot-best-practices.git \

  ~/.gemini/antigravity/skills/springboot-best-practices

```



**Step 2: Chuyển đổi cấu trúc**



```bash

cd ~/.gemini/antigravity/skills/springboot-best-practices



# Đổi skill file → SKILL.md

mv springboot-best-practices.skill SKILL.md



# Đổi knowledge/ → references/

mv knowledge references

```



**Step 3: Thêm metadata vào đầu SKILL.md**



Mở `SKILL.md` và thêm header:



```markdown

---

name: Spring Boot Best Practices

description: Quét và chấm điểm dự án Spring Boot theo 174 best practices, 19 domains. Tự động phát hiện vi phạm và đề xuất cải thiện.

---



(... giữ nguyên nội dung phía dưới ...)

```



**Bước 4 (tuỳ chọn): Tạo workflow trigger `/sbp`**



Tạo file `~/.gemini/antigravity/global_workflows/sbp.md`:



```markdown

---

name: Spring Boot Best Practices Audit

description: Quét và chấm điểm Spring Boot project

---



Đọc tất cả references trong skill springboot-best-practices,

sau đó quét source code trong workspace hiện tại và chấm điểm

theo 174 practices, 19 domains. Xuất báo cáo chi tiết.

```



**Xác nhận Installation:**



```bash

ls ~/.gemini/antigravity/skills/springboot-best-practices/

# SKILL.md  references/  README.md

```



> **Note:** Antigravity hỗ trợ Claude Sonnet 4.5 — bạn có thể chọn model Claude thay vì Gemini khi chạy audit.



---



## Sử dụng



### Sử dụng trong Claude Code



```bash

# Quét toàn bộ dự án

/springboot-best-prac
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

