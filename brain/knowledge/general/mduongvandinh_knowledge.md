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
- **Status in AI OS:** 🔖 PENDING/APPROVE

## Description:
springboot-best-practices

## README (excerpt)
```
# Spring Boot Best Practices Skill



**174 best practices | 19 domains | Scoring 0-100 | Vietnamese**



An automated tool that scans Spring Boot source code, evaluates compliance with **174 best practices** across **19 domains**, scores 0-100 per domain with weights. Supports both **Claude Code** and **Google Antigravity**.



> Complements the [Engineering Failures Audit Skill](https://github.com/mduongvandinh/engineering-failures/) — this skill **proposes standards** (proactive), while Engineering Failures **detects errors** (reactive).



---



## Table of Contents



- [Installation:](#installation)

  - [Claude Code](#claude-code)

  - [Google Antigravity](#google-antigravity)

- [Usage](#usage)

  - [Claude Code](#usage-in-claude-code)

  - [Google Antigravity](#usage-in-google-antigravity)

- [19 Domains](#19-domains)

- [Levels & Scoring](#levels--scoring)

- [Project Structure](#project-structure)

- [Format of Each Best Practice](#format-of-each-best-practice)

- [License](#license)



---



## Installation:



### Claude Code



**Method 1: Direct Clone**



```bash

git clone https://github.com/mduongvandinh/springboot-best-practices.git \

  ~/.claude/skills/springboot-best-practices

```



**Method 2: Manual Copy**



```bash

cp -r springboot-best-practices/ ~/.claude/skills/springboot-best-practices/

```



**Verify Installation:**



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



**Step 2: Convert Structure**



```bash

cd ~/.gemini/antigravity/skills/springboot-best-practices



# Rename skill file → SKILL.md

mv springboot-best-practices.skill SKILL.md



# Rename knowledge/ → references/

mv knowledge references

```



**Step 3: Add Metadata to Top of SKILL.md**



Open `SKILL.md` and add header:



```markdown

---

name: Spring Boot Best Practices

description: Scan and score Spring Boot projects against 174 best practices, 19 domains. Automatically detect violations and propose improvements.

---



(... keep rest of content below ...)

```



**Step 4 (optional): Create Workflow Trigger `/sbp`**



Create file `~/.gemini/antigravity/global_workflows/sbp.md`:



```markdown

---

name: Spring Boot Best Practices Audit

description: Scan and score Spring Boot project

---



Read all references in springboot-best-practices skill,

then scan source code in current workspace and score

against 174 practices, 19 domains. Output detailed report.

```



**Verify Installation:**



```bash

ls ~/.gemini/antigravity/skills/springboot-best-practices/

# SKILL.md  references/  README.md

```



> **Note:** Antigravity supports Claude Sonnet 4.5 — you can choose Claude model instead of Gemini when running audits.



---



## Usage



### Usage in Claude Code



```bash

# Scan entire project

/springboot-best-prac
```