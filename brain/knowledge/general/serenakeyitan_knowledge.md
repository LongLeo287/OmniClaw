---
id: serenakeyitan-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:12.153816
---

# KNOWLEDGE EXTRACT: serenakeyitan
> **Extracted on:** 2026-03-30 17:53:11
> **Source:** serenakeyitan

---

## File: `awesome-notebookLM-prompts.md`
```markdown
# 📦 serenakeyitan/awesome-notebookLM-prompts [🔖 PENDING/APPROVE]
🔗 https://github.com/serenakeyitan/awesome-notebookLM-prompts


## Meta
- **Stars:** ⭐ 1663 | **Forks:** 🍴 202
- **Language:** N/A | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A curated collection of the strongest NotebookLM slide prompts sourced from the real creative underground . Your go-to resource for AI powerpoint :P

## README (trích đầu)
```
# Awesome NotebookLM Templates
### TRY [Kael.im](https://kael.im/home)(NotebookLM slides alternative) and register at this link for 100 pages free daily quota (nbp)!
![repo_banner](https://hackmd.io/_uploads/HJdglgwrZe.png)
![Awesome](https://awesome.re/badge.svg)
![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)


NotebookLM Slide Prompt⚡️
> A curated collection of the strongest NotebookLM & Kael.im slide prompts sourced from the real creative underground — Note, WeChat, blogs, RED creators, and Twitter/X power users.

These prompts are field-tested by people who ship fast: **researchers, founders, designers**. Use them to turn papers, notes, transcripts, or random brain dumps into **clean, structured, presentation-ready decks** that actually look intentional.

If you want NotebookLM to consistently generate slides that hit, **this is the repo!**

I also built a [citation checker skill](https://github.com/serenakeyitan/citation-check-skill) that detecting hallucinated missing citations in ur slides. Feel free to add it to ur workflow.

## Table of Contents

### A. Editorial & Business Styles
- [Modern Newspaper](#modern-newspaper)
- [Sharp-edged Minimalism](#sharp-edged-minimalism)
- [Yellow × Black Editorial](#yellow--black-editorial)
- [Black × Orange Creative Agency](#black--orange-creative-agency)
- [For Seminar Use (Minimal Text)](#for-seminar-use-minimal-text)

### B. Pop, Youth, and Street Styles
- [Manga Style](#manga-style)
- [Magazine Style](#magazine-style)
- [Pink Street-style](#pink-street-style)
- [Digital / Neo / Pop](#digital--neo--pop)

### C. Typography / Font-driven Styles
- [Mincho × Handwritten Mix](#mincho-font--handwritten-mix)

### D. Artistic & Avant-Garde Styles
- [Deformed Flat Persona](#deformed-flat-persona)
- [Royal Blue × Red Watercolor](#royal-blue-and-red)
- [Classic / Pop (Sculpture × Vaporwave)](#classic--pop)
- [Tech / Art / Neon](#tech--art--neon)

### E. Professional / Product / Premium
- [Studio / Mockup / Premium](#studio--mockup--premium)

### F. Sports & High-energy Styles
- [Sports / Athletic / Energy](#sports--athletic--energy)



## **modern newspaper:**

![image](https://hackmd.io/_uploads/SkkpwiPM-g.png)
![image](https://hackmd.io/_uploads/rJZ0pyKGbg.png)
![image](https://hackmd.io/_uploads/Hya0p1FzZx.png)



```
You are a top art director leading Japan's "new economy business media." But the language should be what users said in the prompt. so not nessecery in (the language what users requested in the prompt).
Based on the following "design definition," generate a visually focused, high-sensibility presentation slide that sparks intellectual excitement in business professionals of the smartphone generation.

[Important: Absolutely Prohibited Output Format Rules]
* **Complete Exclusion of Markdown Symbols**: Do not include symbols like "#" for headings or "*" and "**" for emphasis in the slide text **under any circumstances**.
* **Plain Text Only**: Text display
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `citation-check-skill.md`
```markdown
# 📦 serenakeyitan/citation-check-skill [🔖 PENDING/APPROVE]
🔗 https://github.com/serenakeyitan/citation-check-skill


## Meta
- **Stars:** ⭐ 53 | **Forks:** 🍴 7
- **Language:** N/A | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Citation Check Skill is a lightweight, opinionated citation validation layer designed to detect, verify, and enforce citations in LLM outputs.

## README (trích đầu)
```
# Citation Check v2

> No citation → no output.

Citation Check is a small, opinionated module for **detecting and blocking hallucinated or missing citations** in LLM outputs.

Built for research, slides, and agent pipelines where correctness matters.

---
## Demo - Identified Issues

### TRY [Kael.im](https://kael.im/home)(NotebookLM slides alternative) and register at this link for 100 pages free daily quota (nbp)!
https://github.com/user-attachments/assets/99d427cf-992f-455c-897b-a8f8a132271c


<img width="1219" height="713" alt="Screenshot 2026-01-25 at 13 56 07" src="https://github.com/user-attachments/assets/660592cd-ca53-46ae-8064-28fad9e90b44" />

### Check out [Awesome Notebooklm Slides Prompts List](https://github.com/serenakeyitan/awesome-notebookLM-prompts/tree/main) with all viral templates on X!
## How to Use?
1. Download `citation-check-skill.zip` from [Releases](https://github.com/serenakeyitan/citation-check-skill/releases/latest)
2. Upload it to Claude Code (Profile → Settings → Capabilities → Skills → Add)
3. Use it by telling Claude: "use citation checker" or "use skills"

**Note:** Don't use the "Code → Download ZIP" button - it adds `-main` to the folder name. Always download from Releases!
## What it does

- ✅ Checks that every factual claim has a citation  
- ✅ Verifies that cited sources actually exist  
- ✅ Validates claim–citation consistency (exact numbers, not rounded)
- ✅ Supports vision: reads slides, PDFs, charts, tables
- ✅ Two modes: web search verification OR doc-only verification

If a check fails, the output should be blocked or regenerated.

---

## Why

Most tools add citations *after* generation.  
This enforces citations as a **generation constraint**.

If your agent can't cite a claim, it shouldn't make it.

---

## v2.0 — Consistency Update

Same input → Same output. Key changes:

| Feature                        | What it does                                                 |
| ------------------------------ | ------------------------------------------------------------ |
| **Two-Pass Architecture**      | Extract all claims first, then verify. No more inconsistent results. |
| **Claim Extraction Rules**     | Explicit taxonomy — statistics, comparatives, attributions, etc. |
| **Status Decision Tree**       | Deterministic classification: Verified → Numerical Error → Hallucination |
| **Academic Precision Mode**    | 96.555% ≠ 97%. Exact numbers only.                           |
| **Mandatory Search Templates** | Runs ALL query patterns, not ad-hoc searches                 |
| **Tie-Breaker Rules**          | No judgment calls on edge cases                              |

---

## Typical flow

```text
LLM output (slides / report / PDF)
↓
Pass 1: Extract all claims
↓
Pass 2: Verify each claim
↓
pass → ship
fail → regenerate / fix
```

---

## Two Modes

### Mode 1: Search Verification (default)

- Searches web for authoritative sources
- Validates citations actually exist
- Checks if cited sources say w
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

