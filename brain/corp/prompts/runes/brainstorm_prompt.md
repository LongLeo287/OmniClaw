## MANDATORY DELIVERY RULES

1. NEVER paste brainstorm or report content inline in chat.
2. Always write to an artifact `.md` file.
3. Call `notify_user` with `PathsToReview` pointing to the file.
4. Language: **<!--LANG-->Vietnamese<!--/LANG-->** (all user-facing content).

## APPROVED FORMAT STRUCTURE (FINAL — CEO Approved 2026-03-19)

Combine the following elements based on content type. DO NOT use only one element.

---
### ELEMENT 1: Mermaid Diagram (REQUIRED — Always Fixed at the Top)

- Placed OUTSIDE of any Carousel block.
- Visualizes the architecture, flow, or system being discussed.
- **CRITICAL BUG PREVENTION — Mermaid Parse Errors:**
  - NO `\n` inside node labels.
  - NO `===` (triple equal) for arrows — use `==>` instead.
  - NO parentheses `()` inside node labels — use `-` or space.
  - NO colons `:` inside node labels.
  - Node label format: `["Label - Sublabel"]` using dash separator.
- Example clean node: `Paperclip{"📋 PAPERCLIP - Operational Core"}`

---
### ELEMENT 2: Carousel (USE FOR — Comparison, Feature Lists, Options)

- Use `carousel` fenced block with ` ``` ` four-backtick wrapper.
- Separate slides with `<!-- slide -->` HTML comment.
- Content that fits in a Carousel: comparison tables, feature breakdowns, multi-option analysis.
- Do NOT use Carousel for timelines, risk alerts, or single-topic blocks.

---
### ELEMENT 3: Alert Blocks (USE FOR — Risks, Critical Decisions, Budget)

```
> [!NOTE]    — Background context, executive summary
> [!WARNING] — Risks, dangers, financial loss scenarios
> [!IMPORTANT] — Critical decisions that require CEO confirmation
> [!TIP]     — Observations or optimization suggestions
```

- Place Alert blocks in vertical layout (not inside Carousel).
- Use sparingly — maximum 2-3 alert blocks per report.

---
### ELEMENT 4: ASCII Timeline (USE FOR — Roadmaps, Phases, Step-by-step Delivery)

- Use for sequential phase or day-by-day rollout plans.
- Format:
```
Day 1  ──►  [Action]
   │
Day 2  ──►  [Action]
   │
Day N  ──►  [Final outcome]
```

---
### ELEMENT 5: Markdown Tables + Dividers (USE FOR — Data, Specs, KPIs)

- Use `---` horizontal rules to separate major sections visually.
- Use emoji headers for each section (🗺️ 📊 ⚠️ 🚀).
- Keep table columns narrow — max 4-5 columns.

---
## STANDARD REPORT SKELETON

```
# [EMOJI] TITLE IN CAPS

> [!NOTE]
> One-line executive summary.

---
## 🗺️ Diagram [Fixed Mermaid]

---
## 📊 [Topic] (Carousel — if comparison needed)

---
## ⚠️ Risks & Decisions (Alert blocks)

---
## 🚀 Roadmap (ASCII Timeline)

*Wait for CEO confirmation before execution.*
```

---
*This format was approved by CEO on 2026-03-19. Do not alter the structure.*
