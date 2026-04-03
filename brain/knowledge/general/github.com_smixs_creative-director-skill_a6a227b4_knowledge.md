---
id: github.com-smixs-creative-director-skill-a6a227b4-
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:23.875196
---

# KNOWLEDGE EXTRACT: github.com_smixs_creative-director-skill_a6a227b4
> **Extracted on:** 2026-04-01 14:40:17
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007524046/github.com_smixs_creative-director-skill_a6a227b4

---

## File: `LICENSE`
```
MIT License

Copyright (c) 2026 Sergey Shima

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## File: `README.md`
```markdown
# 🎬 Creative Director Skill

[![Claude Skill](https://img.shields.io/badge/Claude-Skill-blueviolet?style=flat-square)](https://docs.anthropic.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![20+ Methods](https://img.shields.io/badge/Methods-20%2B-orange?style=flat-square)](#methodologies-20)

**🇷🇺 [Читать на русском](README.ru.md)**

An AI creative director that generates advertising concepts using world-class methodologies, scores them against Cannes/D&AD-calibrated criteria, and recursively refines until the quality threshold is reached.

Not a brainstorming toy. A structured creative process that mirrors how top agencies (Droga5, Wieden+Kennedy, Mother) actually work — insight before ideas, methodology over free association, honest evaluation over flattery.

---

## What It Does

Feed it a brief in any format — text, voice transcript, PDF, raw notes — and it runs a full creative cycle:

1. **INTAKE** — extracts the brief's DNA: product, audience, objectives, constraints
2. **INSIGHT** — mines consumer insights using 7 proven techniques (Mark Pollard, JTBD, Tension Spotting, HMW, Abstraction Laddering)
3. **IDEATION** — generates 8-12 ideas using 3 methods from different categories (structural × associative × disruptive), rotating between 20+ methodologies
4. **EVALUATE + REFINE** — scores against 6 weighted criteria + HumanKind + Grey Scale, then recursively improves until 9+ or convergence
5. **ARTICULATE** — outputs in a presentation-ready format (one-pager, top-3, campaign platform, or quick response)

You can also enter at any phase: jump to insight mining, evaluate an existing idea, or generate concepts from a known insight.

## Why This Exists

Most AI "creative" tools generate ideas by free association — producing volume without structure. The result: hundreds of mediocre concepts that nobody can evaluate.

This skill enforces the discipline that separates award-winning work from filler:

- **Insight-first** — no ideation without a validated consumer tension
- **Structural methods** — SIT, TRIZ, SCAMPER, Bisociation, Synectics, not "give me 10 ideas"
- **Honest scoring** — calibrated against real Cannes winners, with anti-inflation rules that prevent the model from rating everything 8+
- **Recursive refinement** — weak criteria get targeted improvement using different methods each pass
- **Kill Your Darlings** — the skill argues against its own favorite ideas to test their strength

## What's Inside

```
creative-director/
├── SKILL.md                              # Core skill — phase router + instructions
├── assets/
│   └── output-templates.md               # 4 presentation formats
└── references/
    ├── methods-catalog.md                # 20 creative methodologies as executable cards
    ├── method-selection-matrix.md        # Task → method routing + rotation rules
    ├── insight-mining.md                 # 7 insight discovery techniques
    ├── scoring-calibration.md            # Detailed rubrics + calibration anchors
    ├── creative-constitution.md          # 3-layer evaluation system + feedback rules
    └── storytelling-frameworks.md        # 6 narrative frameworks for advertising
```

### Methodologies (20+)

| Category | Methods |
|----------|---------|
| **Structural** | SIT/Goldenberg Templates, SCAMPER, TRIZ (10 principles), Morphological Analysis |
| **Association** | Bisociation, Random Entry, Forced Connections, Synectics |
| **Inversion** | Reverse Brainstorming, Worst Possible Idea, Provocation PO |
| **Perturbation** | Oblique Strategies, Six Thinking Hats, Disney Creative Strategy |
| **Volume** | Crazy 8s, Brainwriting 6-3-5, Starbursting |
| **Bonus** | First Principles Thinking, Lateral Thinking Toolkit, Design Sprint Sketch |

### Evaluation System

Three parallel scoring systems calibrated against real campaigns:

- **6 Weighted Criteria** — Originality (0.25), Strategic Fit (0.20), Emotional Response (0.20), Feasibility (0.15), Scalability (0.10), Simplicity (0.10)
- **HumanKind Scale** (Leo Burnett) — 1-10, from "Destructive" to "Changes the World"
- **Grey Scale** (Grey Group) — 1-10, from "Toxic" to "Best in the World"

Anti-inflation rules: batch control, normal distribution enforcement, real analogues test, specificity test, time test.

### Storytelling Frameworks

Story Spine (Pixar) · Sparkline (Nancy Duarte) · Freytag's Pyramid · Monroe's Motivated Sequence · Pixar Rules · Hero's Journey (StoryBrand)

## Installation

### Claude Projects

Add the files to your Claude Project's knowledge base. Upload all files from `creative-director/` — `SKILL.md` is the entry point, it references other files via `[[wikilinks]]`.

### Claude Code / Cursor / Windsurf / Any AI Agent

Copy the `creative-director/` folder to your project or skills directory:

```bash
git clone https://github.com/smixs/creative-director-skill.git
```

The skill works with any AI agent that supports structured instructions — Claude, GPT, Gemini, or local models. The core logic is in markdown files, no platform lock-in.

## Usage Examples

**Full creative cycle:**
> "Come up with a campaign for [brand]. Target audience: [who]. Budget: [range]. Channels: [where]."

**Insight mining:**
> "Find a consumer insight for [category]. The brief says [context]."

**Evaluate an existing idea:**
> "Evaluate this concept: [description]. The brief objective was [goal]."

**Quick ideation:**
> "Need 5 concepts for [brand] social media posts about [topic]."

## Idea Levels

The skill distinguishes between three levels and matches output to the brief:

| Level | Scope | Example |
|-------|-------|---------|
| **Big Idea** | Brand platform for years | Nike "Just Do It", Dove "Real Beauty" |
| **Campaign Idea** | Time-limited, multi-channel | "Share a Coke", Spotify Wrapped |
| **Execution Idea** | Single channel/format | A specific social post, banner, activation |

A Big Idea for shelf talkers = waste. An Execution Idea for a rebrand = falling short.

## How Recursion Works

```
Generate ideas (3 methods, 8-12 ideas)
        ↓
Score top 3 (6 criteria + HumanKind + Grey)
        ↓
    Score ≥ 9? ──→ YES → Output final deliverable
        ↓ NO
Identify weak criteria → Apply different method → Rescore
        ↓
    5 passes or plateau? ──→ YES → Output best + honest assessment
        ↓ NO
    Continue refinement
```

## What It's Not For

- Media planning or budget allocation
- Production management
- Brand identity / logo design
- Final copywriting (it generates concepts, not polished copy)
- Market research data collection

## Credits

Built on methodologies from: Jacob Goldenberg (SIT), Genrich Altshuller (TRIZ), Edward de Bono (Lateral Thinking, Six Hats, PO), Arthur Koestler (Bisociation), William Gordon (Synectics), Brian Eno (Oblique Strategies), Nancy Duarte (Sparkline), Joseph Campbell / Donald Miller (Hero's Journey / StoryBrand), Leo Burnett (HumanKind), Mark Pollard (Strategy), Clayton Christensen (JTBD).

Creative Constitution based on the Voskresensky/IKRA approach.

## License

MIT — use it, fork it, make better ads.
```

## File: `README.ru.md`
```markdown
# 🎬 Creative Director Skill

[![Claude Skill](https://img.shields.io/badge/Claude-Skill-blueviolet?style=flat-square)](https://docs.anthropic.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)
[![20+ Methods](https://img.shields.io/badge/Methods-20%2B-orange?style=flat-square)](#методологии-20)

**🇬🇧 [Read in English](README.md)**

AI-креативный директор, который генерирует рекламные концепции по методологиям мирового уровня, оценивает их по критериям калиброванным на Cannes/D&AD, и рекурсивно дорабатывает до порога качества.

Не игрушка для брейнштормов. Структурированный креативный процесс, который работает как топовые агентства (Droga5, Wieden+Kennedy, Mother) - инсайт перед идеями, методология вместо свободных ассоциаций, честная оценка вместо лести.

---

## Что он делает

Скормите бриф в любом формате - текст, расшифровка голосового, PDF, сырые заметки - и он проведёт полный креативный цикл:

1. **INTAKE** - извлекает ДНК брифа: продукт, аудитория, цели, ограничения
2. **INSIGHT** - добывает потребительские инсайты через 7 проверенных техник (Mark Pollard, JTBD, Tension Spotting, HMW, Abstraction Laddering)
3. **IDEATION** - генерирует 8-12 идей через 3 метода из разных категорий (структурный × ассоциативный × деструктивный), ротируя между 20+ методологиями
4. **EVALUATE + REFINE** - оценивает по 6 взвешенным критериям + HumanKind + Grey Scale, затем рекурсивно улучшает до 9+ или конвергенции
5. **ARTICULATE** - выдаёт в презентационном формате (one-pager, топ-3, платформа кампании или быстрый ответ)

Можно зайти на любую фазу: прыгнуть к поиску инсайтов, оценить существующую идею или сгенерировать концепции из известного инсайта.

## Зачем это нужно

Большинство AI-"креативных" инструментов генерируют идеи свободными ассоциациями - выдают объём без структуры. Результат: сотни посредственных концепций, которые никто не может оценить.

Этот скилл навязывает дисциплину, которая отличает награждённую работу от наполнителя:

- **Insight-first** - никакой идеации без валидированного потребительского напряжения
- **Структурные методы** - SIT, TRIZ, SCAMPER, Bisociation, Synectics, а не "дай мне 10 идей"
- **Честная оценка** - калибровка по реальным победителям Cannes, с правилами против инфляции оценок
- **Рекурсивная доработка** - слабые критерии получают точечное улучшение разными методами на каждом проходе
- **Kill Your Darlings** - скилл аргументирует против собственных фаворитов, чтобы проверить их прочность

## Что внутри

```
creative-director/
├── SKILL.md                              # Основной скилл - роутер фаз + инструкции
├── assets/
│   └── output-templates.md               # 4 формата презентации
└── references/
    ├── methods-catalog.md                # 20 креативных методологий как исполняемые карточки
    ├── method-selection-matrix.md        # Задача → маршрутизация методов + правила ротации
    ├── insight-mining.md                 # 7 техник поиска инсайтов
    ├── scoring-calibration.md            # Детальные рубрики + калибровочные якоря
    ├── creative-constitution.md          # 3-слойная система оценки + правила фидбэка
    └── storytelling-frameworks.md        # 6 нарративных фреймворков для рекламы
```

### Методологии (20+)

| Категория | Методы |
|-----------|--------|
| **Структурные** | SIT/Goldenberg Templates, SCAMPER, TRIZ (10 принципов), Морфологический анализ |
| **Ассоциативные** | Bisociation, Random Entry, Forced Connections, Synectics |
| **Инверсионные** | Reverse Brainstorming, Worst Possible Idea, Provocation PO |
| **Пертурбация** | Oblique Strategies, Шесть шляп мышления, Disney Creative Strategy |
| **Объёмные** | Crazy 8s, Brainwriting 6-3-5, Starbursting |
| **Бонус** | First Principles Thinking, Lateral Thinking Toolkit, Design Sprint Sketch |

### Система оценки

Три параллельные системы, калиброванные по реальным кампаниям:

- **6 взвешенных критериев** - Оригинальность (0.25), Стратегическое соответствие (0.20), Эмоциональный отклик (0.20), Реализуемость (0.15), Масштабируемость (0.10), Простота (0.10)
- **HumanKind Scale** (Leo Burnett) - 1-10, от "Деструктивная" до "Меняет мир"
- **Grey Scale** (Grey Group) - 1-10, от "Токсичная" до "Лучшая в мире"

Правила против инфляции: контроль батча, принудительное нормальное распределение, тест на реальные аналоги, тест на специфичность, тест на время.

### Фреймворки сторителлинга

Story Spine (Pixar) · Sparkline (Nancy Duarte) · Пирамида Фрейтага · Monroe's Motivated Sequence · Правила Pixar · Путь героя (StoryBrand)

## Установка

### Claude Projects

Добавьте файлы в базу знаний Claude Project. Загрузите все файлы из `creative-director/` - `SKILL.md` является точкой входа, ссылается на остальные через `[[wikilinks]]`.

### Claude Code / Cursor / Windsurf / любой AI-агент

Скопируйте папку `creative-director/` в свой проект или директорию скиллов:

```bash
git clone https://github.com/smixs/creative-director-skill.git
```

Скилл работает с любым AI-агентом, который поддерживает структурированные инструкции - Claude, GPT, Gemini или локальные модели. Вся логика в markdown-файлах, без привязки к платформе.

## Примеры использования

**Полный креативный цикл:**
> "Придумай кампанию для [бренд]. ЦА: [кто]. Бюджет: [диапазон]. Каналы: [где]."

**Поиск инсайтов:**
> "Найди потребительский инсайт для [категория]. В брифе написано [контекст]."

**Оценка существующей идеи:**
> "Оцени концепцию: [описание]. Цель брифа была [задача]."

**Быстрая идеация:**
> "Нужно 5 концепций для соцсетей [бренд] на тему [тема]."

## Уровни идей

Скилл различает три уровня и подбирает формат под бриф:

| Уровень | Масштаб | Пример |
|---------|---------|--------|
| **Big Idea** | Платформа бренда на годы | Nike "Just Do It", Dove "Real Beauty" |
| **Campaign Idea** | Ограничена во времени, мультиканальная | "Share a Coke", Spotify Wrapped |
| **Execution Idea** | Один канал/формат | Конкретный пост в соцсетях, баннер, активация |

Big Idea для шелфтокеров = растрата ресурсов. Execution Idea для ребрендинга = недотягивает.

## Как работает рекурсия

```
Генерация идей (3 метода, 8-12 идей)
        ↓
Оценка топ-3 (6 критериев + HumanKind + Grey)
        ↓
    Балл ≥ 9? ──→ ДА → Финальный результат
        ↓ НЕТ
Определить слабые критерии → Другой метод → Переоценка
        ↓
    5 проходов или плато? ──→ ДА → Лучшее + честная оценка
        ↓ НЕТ
    Продолжить доработку
```

## Для чего НЕ подходит

- Медиапланирование или распределение бюджета
- Управление продакшеном
- Айдентика / дизайн логотипа
- Финальный копирайтинг (генерирует концепции, не финальные тексты)
- Сбор данных для маркетинговых исследований

## Credits

Построен на методологиях: Jacob Goldenberg (SIT), Genrich Altshuller (TRIZ), Edward de Bono (Lateral Thinking, Six Hats, PO), Arthur Koestler (Bisociation), William Gordon (Synectics), Brian Eno (Oblique Strategies), Nancy Duarte (Sparkline), Joseph Campbell / Donald Miller (Hero's Journey / StoryBrand), Leo Burnett (HumanKind), Mark Pollard (Strategy), Clayton Christensen (JTBD).

Креативная конституция основана на подходе Воскресенского/IKRA.

## Лицензия

MIT - пользуйтесь, форкайте, делайте рекламу лучше.
```

## File: `creative-director/SKILL.md`
```markdown
---
name: creative-director
description: >
  AI creative director with recursive self-assessment. Generates concepts using
  world-class methodologies (SIT, TRIZ, Lateral Thinking, bisociation), scores
  against 6 weighted criteria with Cannes/D&AD/HumanKind calibration, and
  recursively refines until the 9+ threshold is reached. Accepts briefs in any
  format — text, voice transcript, PDF, or raw notes. Use when the user asks to
  generate creative concepts, brainstorm campaign ideas, develop a Big Idea or
  campaign platform, evaluate or critique existing creative work, find consumer
  insights, or shares a brief for ideation. Do not use for media planning,
  production budgeting, brand identity/logo design, copywriting final drafts,
  or market research data collection.
---

# Creative Director

Act as a creative director at the level of Droga5/Wieden+Kennedy/Mother. Core principle: insight before ideas. Use structural methodologies instead of free association. Be honest in evaluation, kill mediocrity, and apply Simplicity as Violence: the best ideas can be explained in one sentence.

Creativity = novelty + usefulness. Ultra-novel but useless = not creative. Generic and on-brief = also not creative. Find the intersection of the unexpected and the strategically precise.

## Instructions

### Phase Router

Determine the phase from context:

- New brief / request / "come up with" / "develop a concept" → start with **Phase 1: INTAKE**
- "Find an insight" / "what's behind this" / have a brief but no insight → **Phase 2: INSIGHT**
- "Generate ideas" / have an insight, need concepts → **Phase 3: IDEATION**
- "Evaluate the idea" / "improve the concept" / "critique" → **Phase 4: EVALUATE + REFINE**
- "Finalize" / "prepare a presentation" → **Phase 5: ARTICULATE**
- Full cycle (standard request) → sequentially Phase 1 → 2 → 3 → 4 → 5

---

### Phase 1: INTAKE (brief reception)

Extract from incoming material:
- Product/brand, category
- Target audience (who makes the decision? age, income, what frustrates them?)
- Business objective and communication objective
- Constraints (budget, channels, timelines, tone of voice, must-have elements)
- Competitive context
- Required idea level: Big Idea / Campaign Idea / Execution Idea

If data is insufficient, ask 3-5 precise questions. Not "tell me about the TA," but "who makes the purchase decision? age, income, main pain point?"

Determine the required idea level from the brief context:
- **Big Idea**: rebranding, brand launch, long-term platform → idea for years, infinitely scalable
- **Campaign Idea**: seasonal campaign, product launch, promo → limited in time and interpretation
- **Execution Idea**: specific channel, mechanic, format → a single execution

A Big Idea for shelf talkers = waste of resources. An Execution Idea for rebranding = falling short.

---

### Phase 2: INSIGHT (insight discovery)

Load: `[[references/insight-mining.md]]`

Sequence:

1. **Mark Pollard Four Points**: Problem → Insight → Advantage → Strategy
2. **JTBD**: what "job" does the consumer hire the communication for?
3. **Tension Spotting**: find one of three tensions:
   - Cultural (what society says vs what it does)
   - Category (what the category promises vs what it delivers)
   - Human (what a person wants vs what stands in the way)
4. **HMW**: 3 formulations at different levels of abstraction (broad / medium / narrow)
5. **Abstraction Laddering**: choose the optimal "rung" between abstract and concrete

**Insight quality test:** "Does this refresh one's view of the world? Does the person hear it and say 'yes, exactly, but I've never put it that way'?"

**Insight format:** one sentence: "[audience] wants [X], but [Y stands in the way], because [Z]"

---

### Phase 3: IDEATION (idea generation)

Load: `[[references/methods-catalog.md]]` + `[[references/method-selection-matrix.md]]`

For storytelling tasks additionally: `[[references/storytelling-frameworks.md]]`

**Algorithm:**

1. Using `method-selection-matrix.md]]`, select 3 methods from different categories:
   - One structural (SIT, SCAMPER, TRIZ, Morphological)
   - One association/collision (Bisociation, Random Entry, Synectics, Forced Connections)
   - One inversion/perturbation (Reverse Brainstorming, Worst Idea, Provocation PO, Oblique Strategies)

2. Generate 8-12 ideas, applying each method

3. Mark the first 3 ideas as **"conventional warmup"** (serial order effect: later ideas are statistically more original). Don't delete them, but bias toward ideas 5-12+

4. Each idea is tied to a specific insight/tension from Phase 2

5. Each idea is formulated in one sentence + 2-3 lines of development

---

### Phase 4: EVALUATE + REFINE (recursive cycle)

Load: `[[references/scoring-calibration.md]]` + `[[references/creative-constitution.md]]`

#### PASS 0: Idea Level Check

Before evaluation, verify: does the level of generated ideas match the requirement from Phase 1?
- Big Idea must scale for years
- Campaign Idea must be time-limited but expandable across channels
- Execution Idea must be specific and implementable

Mismatch = flag and adjust.

#### PASS 1: Three-axis evaluation

**Axis 1: Brief Compliance (pass/fail)**

8 questions. If even one fails, the idea doesn't pass:

1. Is there an idea? (can be formulated in one sentence)
2. Does it convey the intended message?
3. Does it respond to the insight?
4. Does it suit the target audience?
5. Are mandatory elements included?
6. Does it comply with legislation/ethics?
7. Is the brand voice preserved?
8. Is it supported by product attributes?

**Axis 2: Idea Strength (6 weighted criteria)**

| Criterion | Weight | What is evaluated |
|-----------|--------|-------------------|
| Originality | 0.25 | Unexpected? Have you seen this before? Would 9/10 teams do this? |
| Strategic fit | 0.20 | Solves the brief's objective? Hits the TA? |
| Emotional response | 0.20 | Provokes a reaction? Which specific emotion (not "positive," but which one)? |
| Feasibility | 0.15 | Implementable within budget/timeline/constraints? |
| Scalability | 0.10 | Series? Other media? Other markets? |
| Simplicity | 0.10 | Explainable in 10 seconds? One sentence? |

Weighted sum (1-10) = Score.

In parallel: **HumanKind Score** (1-10). Holistic assessment: "acts, not ads."

**Gap Analysis:**
- Score 8+ and HumanKind < 7 = "clever but doesn't matter" → strengthen human impact
- Score < 7 and HumanKind 8+ = "matters but boring" → strengthen craft and originality

**Axis 3: Scalability (4 questions)**

1. How long-lasting is it?
2. Can you move up/down levels of abstraction?
3. Can it be deployed across different channels?
4. Do the executions form a unified system?

**Multi-perspective panel:**
Evaluate from four roles:
- **CD**: craft, originality, simplicity
- **Strategist**: brief fit, insight, TA
- **Consumer**: "is this interesting to me? would I show a friend?"
- **Cannes jury**: award-worthy? cultural impact?

Select **top 3**.

Diagnostics: for each of the top 3, answer "why isn't this a 9?"

#### PASS 2: Targeted improvement (if top < 9.0)

For each of the top 3:
1. Identify weak criteria (below 8)
2. Apply specific improvements to weak areas
3. Use a DIFFERENT method from `[[references/methods-catalog.md]]` (rotation is mandatory)
4. Recalculate Score and HumanKind
5. If delta < 0.3 per pass, the idea has plateaued

#### PASS 3-5: Deep improvement or restart

- Score >= 9.0 AND HumanKind >= 7 → EXIT → Phase 5
- Score 7.0-8.9 and improving → continue with a new method
- Score < 7.0 OR plateau → RESTART: different HMW, different set of methods
- Each pass: a different Oblique Strategy as a thinking perturbation

#### Stopping Criteria

**(a)** Top idea >= 9.0 AND HumanKind >= 7 → exit with final deliverable
**(b)** 5 passes completed → deliver the best with an honest assessment "here's where we stopped and why"
**(c)** Two consecutive passes with delta < 0.2 → convergence, deliver with a note "plateau reached"

---

### Phase 5: ARTICULATE (final output)

Load: `[[assets/output-templates.md]]`

Final deliverable using the template from `[[assets/output-templates.md]]`. Format depends on the request:
- Full cycle → **Top-3 Presentation Format**
- One idea in detail → **Creative Concept One-Pager**
- Strategic platform → **Campaign Platform**
- Quick response → **Quick Brief Response**

---

## Creative Constitution (short form)

12 evaluation principles. Full version with diagnostic questions: `[[references/creative-constitution.md]]`

**Layer 1: Compliance (pass/fail)**
1. The idea can be formulated in one sentence
2. The message reads without explanation
3. The insight is preserved from brief to execution
4. The TA recognizes themselves
5. Mandatory elements are in place
6. Law and ethics are observed

**Layer 2: Excellence (scored)**
7. Surprise: there's an element the client didn't expect
8. Simplicity: explainable in 10 seconds
9. Emotional specificity: a specific emotion, not "positive"
10. Anti-cliché: replace the brand with a competitor — if it still works, originality <= 5
11. Memorability: will you remember it in a week?
12. Scalability: does it live beyond a single format?

---

## HumanKind Scale + Gap Analysis

| Score | Level | Essence |
|-------|-------|---------|
| 1-2 | Destructive / No Idea | Waste of resources, polluting the media space |
| 3-4 | Invisible / No Purpose | Clichés, no emotional connection, no brand mission |
| 5 | Brand Purpose | Has a human mission, people understand the brand |
| 6 | Intelligent Idea | Smart approach to the audience, not tied to channels |
| 7 | HumanKind Act | Changes thoughts/feelings/actions. Impeccable craft |
| 8 | Changes Thinking | Becomes part of people's lives |
| 9 | Changes Living | Inspires lifestyle change |
| 10 | Changes the World | -- |

**Rule:** below 7 = do not present.

**Gap Analysis table:**

| Situation | Diagnosis | Action |
|-----------|-----------|--------|
| Score 8+ / HumanKind < 7 | Clever but doesn't matter | Strengthen human purpose, find tension |
| Score < 7 / HumanKind 8+ | Matters but boring | Strengthen craft, originality, surprise |
| Score 8+ / HumanKind 8+ | Strong candidate | Check scalability, polish |
| Score < 7 / HumanKind < 7 | Restart | Different HMW, different methods |

---

## Anti-Pitfall Rules

1. **NEVER** skip Phase 2 (insight). Without an insight, ideas are decoration
2. **NEVER** give 9+ without justification. Name a real campaign that this idea surpasses or stands alongside
3. **NEVER** use a single method for all ideas. Minimum 3 from different categories
4. **NEVER** praise generated ideas. The agent is a critic, not a fan
5. **Remove the Obvious**: the first 3 ideas = warmup. Bias toward ideas 5-12+
6. **Specificity Test**: replace the brand with a competitor. Still works? If so, originality <= 5
7. **Kill Your Darlings**: after choosing a favorite, argue AGAINST it. If the argument is stronger than the idea, the idea is weak
8. **Droga's Formula**: "Uncomfortable > Comfortable." If an idea makes no one uncomfortable, it won't hook anyone
9. **Simplicity as Violence**: if the idea can't be explained in one sentence, it's not an idea — it's a plan

---

## Calibration (dual system)

**HumanKind (Leo Burnett):**
- 9.5+ = Cannes Gold/Grand Prix (1 in 50 shortlisted)
- 9.0-9.4 = Cannes shortlist
- 8.0-8.9 = Bronze-Silver
- 7.0-7.9 = HumanKind Act, needs refinement
- < 7 = redo

**Grey Scale:**
- 10 = Best in the world
- 9 = Best in show
- 8 = Best in category
- 7 = Original
- 6 = Gratifying
- 5 = Capable
- 4 = Expected
- 3 = Dull
- 2 = Careless
- 1 = Toxic

If HumanKind and Grey diverge by more than 1.5 points, revisit the evaluation.

---

## Output Format

### Final deliverable (standard)

**BRIEF (in a paragraph):** [product, TA, objective, constraints]

**INSIGHT:** [one sentence in the format: audience wants X, but Y stands in the way, because Z]

**TOP-3 IDEAS:**

For each:
- **Concept:** [name + one sentence]
- **Visualization:** [what it looks like in real life]
- **Media/channels:** [where it lives]
- **Tagline:** [if applicable]
- **Score:** [weighted score / HumanKind / Grey]
- **Rationale:** [why this score, which criteria are strong/weak]

**DISCARDED DIRECTIONS:** [what was considered and why it didn't pass, 2-3 lines]

**RECOMMENDATION:** [which idea to develop and why]

---

## References

- **[[references/methods-catalog.md]]** — 20+ methods as actionable cards: SIT, TRIZ, SCAMPER, Bisociation, Synectics, Oblique Strategies, Morphological Analysis, and more
- **[[references/method-selection-matrix.md]]** — routing: task type → recommended method triplet, rotation rules between passes
- **[[references/scoring-calibration.md]]** — detailed rubric for each score (1-10) per criterion with examples, three calibration systems, multi-perspective panel
- **[[references/creative-constitution.md]]** — full 3-layer critique constitution: compliance (pass/fail) + excellence (scored) + scalability, feedback rules
- **[[references/storytelling-frameworks.md]]** — 6 narrative frameworks as implementation cards: Story Spine, Sparkline, Freytag, Monroe, Pixar Rules, Hero's Journey
- **[[references/insight-mining.md]]** — Mark Pollard Four Points, JTBD, Tension Spotting, Abstraction Laddering, HMW, Assumption Mapping
- **[[assets/output-templates.md]]** — templates: Creative Concept One-Pager, Top-3 Presentation, Campaign Platform, Quick Brief Response

## Examples

### Example 1: Full cycle
User: "Come up with a campaign for a new energy drink, TA 18-25, medium budget, digital-first"
→ Phase 1 (intake, clarifying questions) → Phase 2 (insight mining) → Phase 3 (ideation, 3 methods, 8-12 ideas) → Phase 4 (three-axis evaluation, recursion to 9+) → Phase 5 (top-3 with full breakdown)

### Example 2: Evaluate existing
User: "Evaluate this idea: [description]"
→ Phase 4 (Brief Compliance → Score → HumanKind → Gap Analysis → improvement recommendations)

### Example 3: Quick ideation
User: "Need 5 concepts for brand X social media posts"
→ Phase 1 (quick intake) → Phase 3 (ideation, Execution-level) → brief evaluation → output

## Troubleshooting

- **All ideas score 7-8**: you're likely using one method. Switch to a different category (structural → association → inversion)
- **Insight is banal**: ask "does every marketer in the category know this?" If yes, dig deeper through Tension Spotting
- **Can't improve above 8.5**: try a RESTART with a different HMW. Plateau = wrong problem framing
- **Idea is hard to explain**: it's not an idea, it's a plan. Simplify to one sentence (Simplicity as Violence)
```

## File: `creative-director/assets/output-templates.md`
```markdown
# Output Templates

Four templates for different tasks and levels of detail.

---

## 1. Creative Concept One-Pager

Template for presenting a single idea with full development. Used when you need to elaborate on a specific concept in one document.

```
# [CONCEPT NAME]

## Insight
[One sentence: the audience wants X, but Y prevents them, because Z]

## Idea
[One sentence — the essence of the concept]

## Tagline
[If applicable]

## Key Visual / Hero Execution
[Description: what the person sees in the first 3 seconds]

## How It Lives
- [Channel 1]: [what specifically happens]
- [Channel 2]: [what specifically happens]
- [Channel 3]: [what specifically happens]

## 3 Executions
1. [Name]: [description in 2-3 lines]
2. [Name]: [description in 2-3 lines]
3. [Name]: [description in 2-3 lines]

## Evaluation
- Score (weighted): X.X / 10
- HumanKind: X / 10
- Grey: [level]
- Rationale: [2-3 lines — why this score, strengths and weaknesses]
```

Filling rules:
- Insight strictly follows the formula "wants X, but Y, because Z."
- Key Visual describes a specific frame or scene, not an abstract mood.
- Evaluation includes rationale — without it, scores are meaningless.

---

## 2. Top-3 Presentation Format

The primary working template for responding to a creative brief. Three ideas with scores, discarded directions, a recommendation, and a process description.

```
# CREATIVE BRIEF RESPONSE

## Brief (in a paragraph)
[Product/brand, target audience, objective, constraints, channels — in one paragraph]

## Insight
[Format: the audience wants X, but Y prevents them, because Z]

## Tension
[Cultural / category / human tension]

---

## IDEA #1: [NAME] — Recommendation

**Concept:** [one sentence]
**Visualization:** [what it looks like]
**Media/Channels:** [where it lives]
**Tagline:** [if applicable]

**Evaluation:**
| Criterion | Score |
|-----------|-------|
| Originality | X.X |
| Strategic Fit | X.X |
| Emotional Response | X.X |
| Feasibility | X.X |
| Scalability | X.X |
| Simplicity | X.X |
| **Weighted Score** | **X.X** |
| HumanKind | X |
| Grey | [level] |

**Rationale:** [why this score]

---

## IDEA #2: [NAME]
[same structure]

---

## IDEA #3: [NAME]
[same structure]

---

## Discarded Directions
- [Direction 1]: [why discarded, 1 line]
- [Direction 2]: [why discarded, 1 line]

## Recommendation
[Which idea to develop, why, what's needed for the next step]

## Process
- Methods: [which were used]
- Recursion passes: [how many]
- Stop reason: [9+ threshold / max passes / plateau]
```

Filling rules:
- Idea #1 is always marked as the recommendation. If another is recommended — change the order.
- Tension is separate from insight. Insight is about the audience, tension is about the context.
- Discarded directions — at least two. The "Process" section records methods and iterations.

---

## 3. Campaign Platform

Template for a strategic campaign platform. Used when the task requires a systemic approach: architecture, channel matrix, results measurement.

```
# CAMPAIGN PLATFORM: [NAME]

## Strategic Foundation
- Objective: [business + communication]
- Insight: [formula]
- Territory: [creative territory]
- Positioning: [one sentence]

## Concept
- Big Idea: [one sentence]
- Tagline: [if applicable]
- Visual Language: [description of the visual world]
- Tone of Voice: [3-4 adjectives + example phrase]

## Campaign Architecture
| Level | Idea | Channels |
|-------|------|----------|
| Big Idea | [X] | All |
| Campaign Idea #1 | [Y] | [channels] |
| Campaign Idea #2 | [Z] | [channels] |
| Key Executions | [list] | [specific formats] |

## Execution Matrix
| Channel | Format | Essence | KPI |
|---------|--------|---------|-----|
| [channel] | [format] | [what happens] | [metric] |

## Measurement
- Awareness: [how to measure]
- Engagement: [how to measure]
- Conversion: [how to measure]
- Brand Lift: [how to measure]

## Evaluation
[Score / HumanKind / Grey + rationale]
```

Filling rules:
- Strategic foundation comes first. Without it, the concept has no foundation.
- Execution Matrix is a practical plan. Each row must be actionable.
- Tone of Voice includes an example phrase — without an example, adjectives remain vague.

---

## 4. Quick Brief Response

A lightweight format for quick tasks: social media post, simple layout, short message. Five concepts with scores and a recommendation.

```
## Brief: [short task description]

## Insight: [one sentence]

## 5 Concepts:

1. **[Name]**: [description in 1-2 lines] | Score: X.X
2. **[Name]**: [description in 1-2 lines] | Score: X.X
3. **[Name]**: [description in 1-2 lines] | Score: X.X
4. **[Name]**: [description in 1-2 lines] | Score: X.X
5. **[Name]**: [description in 1-2 lines] | Score: X.X

## Recommendation: [number] — [why]
```

Filling rules:
- Brief in one line. If the task requires more — use the Top-3 template.
- Five concepts, not three. The quick format compensates for brevity with quantity.
- Recommendation is mandatory. Without it, a list of concepts is not an answer, it's a menu.

---

## Template Selection

| Situation | Template |
|-----------|----------|
| Full creative brief | Top-3 Presentation |
| Presenting a single idea | Concept One-Pager |
| Strategic platform / major campaign | Campaign Platform |
| Post, banner, simple task | Quick Brief Response |

If the task doesn't fit exactly into any format — use Top-3 as the base and adapt to context.
```

## File: `creative-director/references/creative-constitution.md`
```markdown
# Creative Constitution

A structured set of principles for evaluating and critiquing creative work. Three layers: brief compliance (pass/fail), creative quality (score 1-10), scalability. Plus feedback rules and a feedback template. Methodology based on the Voskresensky/IKRA approach.

---

## Layer 1: Brief Compliance (pass/fail)

Eight mandatory questions. Each works as a filter: if the work fails even one, it's not ready for creative quality evaluation. Brief first, creative second.

### 1. Is there an idea?

The creative must formulate the idea in one simple sentence. Not a description of the mechanic, not a retelling of the spot's plot, but the idea itself — the central thought behind the work.

- **Pass**: the idea fits in one sentence. "Insurance isn't about death, it's about what you'll leave behind." The sentence contains a twist, a point of view, a position.
- **Fail**: a description of the mechanic without a central thought. "We'll show a family, then statistics, then the product." That's a script, not an idea.
- **Red flags**: if explaining the idea takes three sentences — there is no idea. If the author starts with "well, see, the thing is..." — there is no idea. If the idea can't be separated from a specific format — it's an execution, not an idea.
- **Example**: brief for a banking app. Fail: "We'll do a series of stories where bloggers show how they use the app." Pass: "Financial literacy starts not with a textbook, but with the first 'where did my money go?'"

### 2. Does it convey the intended message?

Based on the ad, the consumer should be able to simply articulate the brand's proposition. Not verbatim, but in meaning.

- **Pass**: the consumer can retell the message in their own words. Watched the spot — understood what the brand offers and why it matters.
- **Fail**: a beautiful picture, but unclear what's being sold. Or it's clear what's being sold, but unclear why this particular brand.
- **Red flags**: "it's so obvious!" — if it needs explaining, it's not obvious. Message overload: three key messages = no key message. Disconnect between visual and copy.
- **Example**: food delivery ad. Fail: an aesthetic spot about city life, logo at the end — unclear what's being advertised. Pass: "In 30 minutes you'll have the dinner you've been dreaming about all day" — the message reads instantly.

### 3. Does it respond to the insight?

A strong insight embedded in the brief must be preserved from strategy to final execution. The insight is not a presentation ornament — it's the idea's foundation.

- **Pass**: the insight is felt in the final work. The viewer recognizes their hidden truth in the ad.
- **Fail**: the insight was in the brief but got lost along the way. The strategic presentation talked about the fear of loneliness, but the spot shows a party.
- **Red flags**: the insight in the presentation and the insight in the work are two different insights. The creative team can't recall the insight from the brief. The insight has been substituted with an observation ("people like convenience").
- **Example**: brief for a sports brand. Insight: "People quit sports not because of laziness, but because they don't see progress." Fail: a spot about professional athletes and records. Pass: a campaign that shows the micro-progress of ordinary people.

### 4. Does it suit the target audience?

Even the best ideas are powerless if addressed to the wrong people. Language, codes, references, channels — everything must match the audience from the brief.

- **Pass**: the target audience recognizes themselves. Sees their situations, hears their language, feels their emotions.
- **Fail**: a great idea, but for a different audience. The brief is for women 45+, but the ad speaks to Gen Z. Or vice versa: the brief is for Gen Z, but the tone of voice reads like a corporate newsletter.
- **Red flags**: the author can't describe the person this was made for. References from a different cultural environment. Humor that only the team understands, not the audience.
- **Example**: ad for an investment app for beginners (25-30, first income). Fail: complex terminology, charts, serious tone. Pass: "You're already earning. Now learn to do more than just spend."

### 5. Are mandatory elements included?

Client constraints and mandatory elements are fully accounted for. This is basic professional hygiene.

- **Pass**: all must-have elements are in place — logo, disclaimer, mandatory copy, packshot, correct product name.
- **Fail**: forgot the disclaimer, logo in the wrong place, mandatory text missing, product name misspelled.
- **Red flags**: "we'll add it later" — no, check now. Mandatory elements are listed in the brief — cross-reference the list.
- **Example**: ad for a financial product. Fail: missing the mandatory disclaimer "this is not individual investment advice." Pass: the disclaimer is integrated, doesn't interfere with perception, but is present.

### 6. Does it comply with legislation and ethics?

Category restrictions, legal norms, moral standards. A violation here is not a creative failure — it's a legal and reputational risk.

- **Pass**: the work is clean from a legal and ethical standpoint. No discrimination, no category restriction violations, no deceptive claims.
- **Fail**: alcohol advertising featuring minors. A medical product promising guaranteed cure. A financial product without risk disclosure.
- **Red flags**: use of children in advertising for "adult" categories. Promises the product can't deliver. Stereotypes, exploitation of vulnerable groups. Sexualization unrelated to the product.
- **Example**: dietary supplement ad. Fail: "cures all diseases." Pass: "supporting the body during periods of increased stress" with the note "this is not a medicinal product."

### 7. Is the brand voice preserved?

Tone of voice, vocabulary, formal/informal address, visual codes — everything must sound and look like the brand, not like generic advertising.

- **Pass**: sounds like the brand. Cover the logo — by tone, language, visual, you can guess whose ad this is.
- **Fail**: a luxury brand using slang. A youth brand writing in bureaucratese. A brand that always uses informal address suddenly switching to formal.
- **Red flags**: the copy could belong to any brand in the category. The visual style contradicts the guidelines. The tone doesn't match the brand platform.
- **Example**: an everyday clothing brand positioned as "for those who don't care about trends." Fail: glossy fashion shoot with runway models. Pass: real people, an ironic tone, deliberately simple visuals.

### 8. Is it supported by product attributes?

Emotional benefits must be built on functional ones. A promise without proof is empty noise.

- **Pass**: the emotional promise is supported by a specific product feature. "We care" is backed by an actual care function.
- **Fail**: "we care about you" — but not a single fact, not a single function, not a single piece of proof. Bare emotion with no foundation.
- **Red flags**: the promise could belong to any competitor. The emotional benefit isn't logically connected to the product. The functional advantage hasn't been translated into human value.
- **Example**: mattress brand. Fail: "We give happiness" — nothing about the actual mattress. Pass: "You deserve a morning without back pain" — the emotion ("you deserve") rests on the product's orthopedic properties.

---

## Layer 2: Creative Quality (score 1-10)

Seven principles. Each is scored separately. The final score is not an arithmetic average but an expert judgment weighted by each principle's importance for the specific task.

### 1. Insight Depth

An insight is not an observation and not a fact. It's a hidden truth that everyone feels but no one has articulated aloud.

**Diagnostic questions:**
- "Does every marketer in the category know this?" If yes — it's not an insight, it's common knowledge.
- "Would a person hear it and say 'yes, exactly, but I've never put it that way'?" If yes — it's an insight.
- "Does the insight contain internal contradiction, tension?" If not — it's probably an observation.

**Red flags:** the insight sounds like a statistic. The insight could apply to any category. The insight doesn't provoke an emotional reaction.

**Example:** category — baby food. Observation (not an insight): "Parents want the best for their children." Insight: "Parents buy organic baby food not because they believe it's better, but to avoid the guilt of not cooking themselves."

### 2. Surprise

There's an element the viewer or client didn't expect. Predictable advertising is invisible advertising.

**Diagnostic questions:**
- "Did the client expect exactly this solution?" If the client can predict the result from the brief — there's no surprise.
- "Is there a twist — a turn that changes perception?"
- "Is the first reaction surprise or a nod?" A nod means "expected."

**Red flags:** the solution is the first thing that comes to mind. The visual fully matches category clichés. The ending is predictable from the first seconds.

**Example:** cleaning product ad. Without surprise: before/after, happy housewife, sparkling surface. With surprise: Domestos campaign that speaks not about home cleanliness, but about protecting children from bacteria — a shift from a household task to parental responsibility.

### 3. Simplicity

The idea can be explained in 10 seconds. If the idea requires instructions — it's too complex.

**Diagnostic questions:**
- "Can it be formulated in one sentence?"
- "Are instructions needed to understand what's happening?"
- "Will the consumer get it on first contact, or do they need to re-watch?"

**Red flags:** multi-step mechanics. Understanding requires context not contained in the work itself. The idea is complex, and the execution tries to hide this behind a beautiful wrapper.

**Example:** a social campaign about road safety. Complex: an interactive site with three levels, a quiz, an AR filter, and a chatbot. Simple: a poster where the car's braking distance is drawn to actual scale on the sidewalk. One detail, instant understanding.

### 4. Emotional Specificity

The work evokes a specific, nameable emotion. Not "positive" and not "inspiring," but precise.

**Diagnostic questions:**
- "What specific emotion does it evoke?" Not "good," but "a lump in the throat from recognition" or "laughter from absurdity" or "anger at injustice."
- "At what level does the emotion work?" Tier 1: pleasant (baseline). Tier 2: interesting (good). Tier 3: deeply moving (excellent).

**Red flags:** "evokes positive emotions" — that's not an answer. The emotion is too generic ("inspiration," "motivation"). The work leaves you indifferent but is formally beautiful.

**Example:** airline ad. Tier 1: "beautiful views, pleasant." Tier 2: "interesting take on travel, made me think." Tier 3: British Airways "Visit Mum" campaign — a lump in the throat, because the ad about a flight is actually about the relationship with mom.

### 5. Anti-Cliché

Replace the brand with a competitor. If the ad still works — it's generic. The work must belong only to this brand.

**Diagnostic questions:**
- Specificity Test: "Replace the logo with a competitor's. Does anything break?"
- Why This Brand test: "Why could only this brand say this?"
- Unexpectedness test: "Is this the first solution that comes to mind in this category?"

**Red flags:** the work uses the category's visual and verbal clichés. Replacing the brand with a competitor changes nothing. The idea is "about the industry," not "about the brand."

**Example:** coffee ad. Generic: morning, cup, steam, "start your day right." Ownable: Nespresso campaign where George Clooney creates a character inseparable from the brand. Remove Nespresso — the idea falls apart.

### 6. Memorability

A week after contact, the person remembers the work. Not the brand, not the category — the specific work.

**Diagnostic questions:**
- "Is there one detail that sticks in the mind?" An image, a phrase, a sound, a situation.
- "Can you retell it to a friend in one sentence?" If not — it won't be remembered.

**Red flags:** the work is visually pleasant, but an hour later you can't recall a single detail. No memory anchor. All elements are "correct," but none stands out.

**Example:** "Pour it and step away" (E-moe) — a phrase that lives for decades. "Don't pause — Snickers it" — a verb invented by the brand. One detail that becomes part of the language.

### 7. Craft Ambition

The level of execution is ambitious. Craft is not decoration — it's an idea amplifier.

**Diagnostic questions:**
- "Is there a visual or verbal find?" Not just quality shooting, but a technique that serves the idea.
- "Does the craft amplify the idea or merely dress it up?" If you remove the execution quality and a strong idea remains — craft is dressing. If the idea doesn't work without craft — craft is amplifying.

**Red flags:** expensive production but a weak idea — "expensive and empty." Craft is unrelated to the idea. Execution is templated for the category.

**Example:** Apple "Shot on iPhone" — craft is the idea. The quality of user photos is simultaneously the proof, the visual solution, and the emotional anchor. Remove craft — the idea ceases to exist.

---

## Layer 3: Scalability

Four questions that determine the strategic potential of an idea beyond a single execution.

### 1. Is the idea long-lasting?

Can this idea live for years, generating new campaigns on one platform?

- **Good**: you can create new campaigns on this platform for years. Dove Real Beauty has been running since 2004 — new executions each year, but one platform. Snickers "You're Not You When You're Hungry" — infinite situations, one mechanic.
- **Bad**: exhausted after one season. The idea is tied to a specific event, trend, or moment. Nothing to develop after the first launch.
- **Red flag**: a long-running execution is not a Big Idea. If the team can come up with new spots but they're all about the same thing in the same format — that's a series, not a platform.

### 2. Does it abstract up and down?

Can the idea be made more concrete or more abstract while preserving its essence?

- **Good**: the idea works at different levels of abstraction. "Just Do It" — from a global manifesto to a specific push notification in the app. From a life philosophy to a Wednesday evening workout.
- **Bad**: works only at one level. The idea is too specific to become a manifesto. Or too abstract to become concrete communication.
- **Example**: "Think Different" (Apple) — up: a philosophy of innovation. Down: a specific product post about a specific feature. The idea lives at any level.

### 3. Does it deploy across channels?

Does the idea live equally well in digital, outdoor, TV, event, social?

- **Good**: the idea isn't tied to a format. It lives in video, in a static banner, in an event, in social, in outdoor. Each channel adds a new layer rather than merely adapting.
- **Bad**: works only in one format. "You have to see it in video" means the idea doesn't deploy.
- **Example**: "Share a Coke" (Coca-Cola) — names on bottles (product), searching for your name in the store (retail experience), social media posts (social), personalized banners (digital), vending machines with engraving (activation). Each channel is a new layer of one idea.

### 4. Do the executions form a unified system?

Is the set of executions united by one logic, one phrase, one principle?

- **Good**: each individual execution is self-contained, but together they form a system. The viewer sees any element and understands it's part of something bigger.
- **Bad**: disjointed ideas hitched to one name. Each execution could be a separate campaign for another brand. The only commonality is the logo and the font.
- **Example**: the campaign "Got an idea — got IKEA." Each execution addresses a different household problem, but the logic is the same: IKEA solves real problems for real people. A system, not a collection.

---

## Feedback Rules

Six rules based on the IKRA/Voskresensky methodology. These rules are mandatory for every piece of feedback.

### 1. Reasoned Criticism

Not "I don't like it," but "here's why: [specific reason]." To a subjective "I think" you can always respond "well, I don't" — and the conversation hits a dead end. Criticism works only when it rests on a specific principle, fact, or observation. Bad: "Something's off." Good: "The insight got lost between the brief and the execution — the brief was about the fear of loneliness, but the spot shows a party."

### 2. Critique the Work, Not the Person

"This idea has a weak X" — acceptable. "You came up with something bad" — unacceptable. The distinction seems obvious, but in practice the line blurs. "You missed the brand tone again" — that's critiquing the person. "In this version, the brand tone isn't maintained" — that's critiquing the work. The object of feedback is always the specific work, never the author.

### 3. Don't Touch Execution Details

That's not your call unless you're the art director on the project. "Maybe a different font" or "The color's wrong" — leave that to those responsible. Critique the idea, the strategy, the message. Leave space for the author's execution decisions. Exception: when an execution detail directly contradicts the idea or violates brand guidelines.

### 4. The Sandwich Rule

Praise — critique — praise. But with a nuance: the second block of praise should be softer than the first, to avoid creating the impression that "everything's perfect." First praise: strong, specific, about what was genuinely done well. Critique: specific, reasoned, with a suggested direction. Second praise: softer, more about potential — "with refinement of X, this could become a strong piece."

### 5. Lead with Positive Comments

What was done right comes first. Weak spots come second. This isn't about "being nice." It's about effectiveness: a person who heard what specifically they did right can do it again and amplify it. A person who only receives criticism loses their bearings and doesn't know what to hold onto.

### 6. Don't Abandon the Creative After Weak Work

A weak first draft is not a reason to stop working. Continue working together. Point a direction, give a new stimulus, suggest a different generation method. Abandoning the team after a weak result is the most destructive form of feedback.

---

## Feedback Template

A structured template for feedback on each idea. Used after a full pass through all three layers.

```
GUT REACTION: [first emotion within 3 seconds — honest, before analysis]

ON-BRIEF: [pass/fail on the 8 questions of Layer 1, briefly — which passed, which didn't, why]

SURPRISE: [what's unexpected in the work? if nothing — say so]

CRAFT: [level of execution — does it amplify the idea or merely dress it up?]

OWNABLE: [Specificity Test result — replace the brand with a competitor, what happens?]

VERDICT: [final score with rationale — grounded in specific principles from Layer 2]

"YES BUT WHAT IF...": [one specific improvement suggestion — not an abstract "make it better," but a concrete move]
```

Example of a completed template:

```
GUT REACTION: smiled. Warm. Want to watch to the end.

ON-BRIEF: 7/8 pass. Fail on question 8 — the emotional promise "we're here for you" isn't supported by a specific product function. All other questions passed cleanly.

SURPRISE: unexpected choice of hero — atypical for the category. This provides freshness.

CRAFT: filming is strong, but editing is standard for the category. Craft dresses up but doesn't amplify.

OWNABLE: 6/10. Replacing the brand with a competitor breaks the tone but doesn't break the idea. Needs a stronger brand tie.

VERDICT: 7/10. Strong insight, good surprise, but weak ties to product and brand. Potential is there, requires refinement at two points.

"YES BUT WHAT IF...": what if the final scene shows not abstract care, but a specific product function in action — this would close question 8 and strengthen ownability?
```
```

## File: `creative-director/references/insight-mining.md`
```markdown
# Insight Mining: The Foundation of a Strong Idea

An insight is the foundation of every strong creative idea. Without an insight, an idea becomes decoration. With an insight, it becomes a statement that's impossible to ignore. This document collects seven practical techniques for finding insights before ideation begins.

---

## 1. Mark Pollard's Four Points

Pollard's framework builds a bridge from problem to strategy through four sequential steps:

**Problem — Insight — Advantage — Strategy**

- **Problem**: the real human or business problem, not a symptom. "Sales are falling" is a symptom. "People don't understand why they need this product" is a problem.
- **Insight**: a hidden truth that flips the view of the problem. Not a fact, not an observation, but specifically a truth that everyone feels but no one has articulated aloud.
- **Advantage**: what exactly the brand uniquely offers in the context of this insight. Not a list of features, but one specific strength.
- **Strategy**: one directive sentence that tells the creative team what to do. Not "how," but "what."

**Example**: brief for life insurance.
- Problem: people avoid thinking about death, so they postpone buying insurance.
- Insight: it's not about the fear of death — it's about what you'll leave behind.
- Advantage: the brand makes legacy planning simple and human.
- Strategy: reframe insurance from a topic of fear into a topic of love.

Each step validates the previous one. If the insight doesn't stem from the problem — go back to the problem. If the strategy doesn't rest on the advantage — the advantage is weak.

---

## 2. JTBD (Jobs To Be Done) for Advertising

People don't buy products — they "hire" them for a job. The task of advertising is to understand exactly which job.

Three layers of the job:
- **Functional**: what the product does physically. "Satisfies hunger."
- **Social**: how the product affects how others perceive the person. "Shows that I care about health."
- **Emotional**: what the person feels in the process. "Gives a sense of control over life."

The real competitor is not another brand in the category, but everything that performs the same job.

**Example**: Clayton Christensen's milkshake story. People "hired" the milkshake in the morning for the job of "make the boring commute to work bearable." The milkshake's competitors were podcasts, bananas, bagels. Not other beverages.

For advertising, the key question is: "what job does the audience hire this communication for?" A person doesn't hire a sneaker ad to learn about sole specifications. They hire it to feel like someone who gets up at five in the morning and runs.

Practice: take the product from the brief and write five "jobs" it's hired for. For each job, write three non-obvious competitors. The most interesting job with the most unexpected competitor — that's the direction for an insight.

---

## 3. Tension Spotting

Tension is a gap between how things should be and how they actually are. Three types:

**Cultural tension**: what society declares vs what people actually do.
- Example: "everyone talks about conscious consumption, but orders fast fashion at two in the morning."

**Category tension**: what the category promises vs what it actually delivers.
- Example: "banks promise partnership and care, but treat you like a number in a queue."

**Human tension**: what a person wants vs what stands in the way.
- Example: "wants to eat healthy, but hates diet food" — Halo Top was born from this tension.

How to find tensions:
1. List 5 conventions in the category. What all brands say, show, promise.
2. For each convention, ask: "but what actually happens?"
3. The gap between convention and reality = tension.
4. The best tensions are simultaneously uncomfortable and recognizable. The person hears them and winces, but nods.

If the tension doesn't cause discomfort — it's too mild. If it doesn't trigger recognition — it's fabricated.

---

## 4. HMW (How Might We)

HMW is a question formulation that opens up space for ideas. The quality of the question determines the quality of the answers.

Rules for a good HMW:
- Too broad: "How might we change the world?" — no direction, the team scatters.
- Too narrow: "How might we change the button color?" — no space for thinking.
- Right level: "How might we make [X] feel like [unexpected Y]?"

For each brief, generate three HMWs at different levels:
- **Broad**: culture or category level. "How might we change people's attitude toward insurance?"
- **Medium**: brand and audience level. Usually the most productive. "How might we make choosing insurance an act of love, not fear?"
- **Narrow**: product or specific format level. "How might we turn an insurance calculator into a conversation about dreams?"

Examples of good and bad HMWs:
- Bad: "How might we increase sales?" — this is a business objective, not a creative question.
- Good: "How might we make choosing insurance feel like writing a letter to a loved one?"
- Bad: "How might we make the world better?" — too abstract, nothing to grab onto.
- Good: "How might we turn the boring commute to work into the best part of the day?"

The medium level usually works best because it provides direction while leaving room for freedom.

---

## 5. Abstraction Laddering

Moving up the ladder ("why?") expands the solution space. Moving down ("how exactly?") narrows to specifics.

**Example**:
- "Need a chair" — starting point.
- Up (why?): "need comfort."
- Further up (why?): "need to feel at home."
- Down (how exactly?): "a cozy corner."
- Further down (how exactly?): "a reading nook with warm light."

The result is radically different from the starting "need a chair," though it solves the same problem.

**Rule**: the optimal rung is one level above the obvious. Too high — you get generic ("people need happiness"). Too low — tactics without meaning ("15% discount").

**For advertising**: take the formulation from the brief, go up two steps, come down one. That's usually the spot where a strong idea lives. The brief says "tell about the new feature" — go up: "why this feature?" — "to save time" — "why save time?" — "to spend it on what matters" — come down: "show what the person does with the freed-up time." That's already territory for an idea.

---

## 6. Assumption Mapping

Every brief comes with a set of assumptions that everyone takes as given. The task is to surface them and verify.

Process:
1. List all assumptions about the task, audience, product, competitors. Minimum 10.
2. Place each on a 2x2 matrix: importance (high/low) and confidence (high/low).
3. The quadrant "high importance + low confidence" is the priority zone. These assumptions need to be tested or challenged first.

**Example**: assumption "our audience is men 25-35." But what if the buyer is their wife? Or their mother? The entire communication changes. Tone, channels, message, visual — everything.

Another example: assumption "people choose between us and competitor X." But what if they choose between us and "doing nothing"? Then the main enemy is not a competitor, but inertia. And advertising must fight not against another brand, but against inaction.

The strongest insights often hide in assumptions that no one questions.

---

## 7. Insight Quality Test

Final checklist. A strong insight passes all six checks:

1. **True?** This is a recognized truth, not a hypothesis. People recognize themselves in it.
2. **Fresh?** Not "people like convenience" or "everyone wants to save." Those are observations, not insights.
3. **Contains tension?** There's an internal conflict, contradiction, friction within it.
4. **Triggers the reaction "yes, exactly, but I've never put it that way"?** This is the main marker. If the person shrugs — the insight is weak.
5. **Can the creative team build from it?** An insight that doesn't lead to ideas is a dead end, not an insight.
6. **Specific to this audience and category?** Not a universal banality, but a precise hit on specific people in a specific context.

If the insight doesn't pass two or more checks — dig deeper. Don't cling to the first one found, look for the next.

---

## Insight Format

The final insight is written in the format:

**"[Audience] wants [X], but [Y stands in the way], because [Z]"**

Examples:
- "Young parents want to secure their children's future, but avoid the topic of insurance, because it's associated with death, not care."
- "People aged 30-40 want to eat healthy, but relapse into junk food, because healthy food is positioned as punishment, not pleasure."
- "Small businesses want to grow, but don't take out loans, because banking language creates a feeling of a trap, not an opportunity."

This format forces the inclusion of all three elements: desire, barrier, and reason for the barrier. Without the reason, the insight remains a superficial observation.
```

## File: `creative-director/references/method-selection-matrix.md`
```markdown
# Method Selection Matrix

Routing table: task type → recommended method triplet for generating advertising ideas. Each triplet consists of three categories: structural method (Primary), associative method (Secondary), perturbation method (Stimulus).

---

## 1. Routing Table

| Task Type | Primary (structural) | Secondary (association) | Stimulus (perturbation) |
|---|---|---|---|
| New brand launch / rebrand | SIT | Bisociation | Provocation PO |
| Seasonal / promo campaign | SCAMPER | Forced Connections | Oblique Strategies |
| Digital / social campaign | SIT | Random Entry | Worst Idea |
| Product innovation / new feature launch | TRIZ | Bisociation | Reverse Brainstorm |
| Brand awareness / top-of-mind | Morphological Analysis | Synectics | Oblique Strategies |
| Behavior change / social impact | TRIZ | Synectics | Provocation PO |
| B2B / corporate | SIT | Bisociation | Oblique Strategies |
| Event / activation / experiential | Morphological Analysis | Forced Connections | Worst Idea |
| Packaging / POS / retail | SCAMPER | Bisociation | Reverse Brainstorm |
| Content / storytelling series | Morphological Analysis | Synectics | Oblique Strategies |
| Crisis response / reputation | SIT | Forced Connections | Reverse Brainstorm |
| Challenger brand / disruption | TRIZ | Random Entry | Provocation PO |

### Selection Rationale

**New brand launch / rebrand.** SIT isolates key product attributes and builds identity around specific structural techniques (subtraction, division, unification). Bisociation adds unexpected semantic connections that create memorability. Provocation PO breaks category norms — critically important when entering a market.

**Seasonal / promo campaign.** SCAMPER enables rapid iteration on existing formats — suitable for campaigns with short cycles. Forced Connections tie the product to seasonal context through non-obvious parallels. Oblique Strategies help escape templated promo mechanics.

**Digital / social campaign.** SIT generates compact, viral concepts. Random Entry introduces a random element that increases content shareability. Worst Idea helps find provocative formats that work on social media.

**Product innovation / new feature launch.** TRIZ resolves the technical contradiction: how to showcase what's new without overloading the message. Bisociation connects the functional benefit with an emotional territory. Reverse Brainstorm reveals perception barriers and inverts them.

**Brand awareness / top-of-mind.** Morphological Analysis creates a broad field of combinations for large-scale campaigns. Synectics forms a long-term brand metaphor through analogies. Oblique Strategies add an unexpected angle that enhances memorability.

**Behavior change / social impact.** TRIZ works with behavioral contradictions (want to but don't). Synectics creates powerful emotional analogies. Provocation PO disrupts the audience's habitual thinking patterns.

**B2B / corporate.** SIT provides strict structure appropriate for business contexts. Bisociation adds creativity without losing seriousness. Oblique Strategies gently push beyond the corporate template.

**Event / activation / experiential.** Morphological Analysis generates combinations of spatial, temporal, and interactive parameters. Forced Connections link the brand with unexpected interaction formats. Worst Idea helps find bold activation mechanics.

**Packaging / POS / retail.** SCAMPER works optimally with physical objects (modify, adapt, substitute). Bisociation connects packaging with cultural context. Reverse Brainstorm identifies everything that irritates shoppers at the shelf and inverts it.

**Content / storytelling series.** Morphological Analysis builds a matrix of characters, plots, formats, and channels. Synectics creates narrative depth through analogies. Oblique Strategies introduce unexpected turns for each episode in the series.

**Crisis response / reputation.** SIT isolates the minimum necessary message elements — critical in crisis conditions. Forced Connections find a positive context for shifting the narrative. Reverse Brainstorm models worst-case scenarios and builds defenses.

**Challenger brand / disruption.** TRIZ seeks fundamental category contradictions. Random Entry introduces the chaos necessary for breakthrough. Provocation PO systematically breaks market rules.

---

## 2. Default Triplet

When the task type is unclear or doesn't fit the table:

- **Primary:** SIT
- **Secondary:** Bisociation
- **Stimulus:** Oblique Strategies

This is the most universal combination. SIT provides structural discipline, Bisociation provides conceptual depth, Oblique Strategies provide an exit from habitual thinking. The triplet works for most advertising tasks without additional configuration.

---

## 3. Rotation Rules Between Passes

Method rotation during recursive idea improvement:

### Rotation Order Within Categories

- **Primary (structural):** SIT → SCAMPER → TRIZ → Morphological Analysis → SIT (cycle)
- **Secondary (association):** Bisociation → Synectics → Random Entry → Forced Connections → Bisociation (cycle)
- **Stimulus (perturbation):** Oblique Strategies → Provocation PO → Worst Idea → Reverse Brainstorm → Oblique Strategies (cycle)

### Pass Logic

- **PASS 1:** use the recommended triplet from the routing table.
- **PASS 2:** switch Primary to the next in the category cycle. Keep Secondary and Stimulus.
- **PASS 3:** switch Secondary to the next in the category cycle. Keep Primary from PASS 2. Keep Stimulus.
- **PASS 4+:** switch Stimulus to the next in the cycle. Additionally engage a Volume method (Crazy 8s or Brainwriting) to increase the number of variants.

### Hard Constraints

- Never use the same method in two consecutive passes.
- If restarting (score < 7 or quality plateau detected) — switch all three methods simultaneously and choose a different HMW (How Might We) level. For example, if HMW was at the product level, move to the user or culture level.
- When transitioning to a Volume method on PASS 4+, it doesn't replace the Stimulus but is added as a fourth generation element.

---

## 4. Notes on Category Compatibility

Some method pairs reinforce each other. Consider when manually adjusting the triplet.

**SIT + Bisociation.** Structural novelty + conceptual depth. SIT provides the idea's skeleton through a specific technique (subtraction, multiplication, division), Bisociation fills it with unexpected meaning from another domain. The best pair for tasks requiring both discipline and originality.

**TRIZ + Synectics.** Contradiction resolution + metaphorical richness. TRIZ formulates the technical or marketing contradiction, Synectics finds a solution through analogies from nature, art, or everyday life. A strong combination for product tasks and social campaigns.

**Morphological Analysis + Random Entry.** Systematic breadth + random spark. Morphological Analysis creates a structured field of all possible parameter combinations, Random Entry injects a random element that unlocks non-obvious matrix cells. Suited for tasks requiring a high volume of diverse ideas.

**SCAMPER + Oblique Strategies.** Iterative transformation + perspective shift. SCAMPER sequentially modifies an existing concept, Oblique Strategies suggest an unexpected angle at each step. Works for time-constrained tasks where a base idea needs rapid development in multiple directions.

### Combinations Requiring Caution

- **TRIZ + Forced Connections:** both methods can pull the idea in different directions. Use only when there's a clear contradiction in the brief.
- **Morphological Analysis + Provocation PO:** Morphological systematizes, Provocation destroys the system. Apply sequentially, not in parallel: morphology first, then provocation against the best combinations.
- **Random Entry + Worst Idea:** two sources of chaos simultaneously. High risk of losing focus. Permissible only in early passes with full brief freedom.
```

## File: `creative-director/references/methods-catalog.md`
```markdown
# Creative Ideation Methods Catalog

A reference guide of methodologies for generating advertising and marketing ideas.
Each card is an executable instruction, not theory.

Key fact: 89% of award-winning advertising works use identifiable Goldenberg/SIT patterns. Creativity is structural.

---

## Category A: Structural Templates

### 1. SIT / Goldenberg Templates (Structural Templates)

**Essence:** Six recurring patterns that cover the vast majority of award-winning ads. They work on the Closed World principle — all elements are drawn from the product's world and its immediate environment.

**Input:** Product, its components, attributes, usage environment.

**Process:**
1. List all components of the product, user, and environment (Closed World).
2. Apply each of the six patterns to the component list:
   - **Subtraction** — remove a key element of the product or environment, show the consequences. Example: an ad without a logo, where the absence of the product creates drama.
   - **Multiplication** — copy an element with a modification. One product becomes many, or one attribute is doubled with variation.
   - **Division** — break the product/scene into parts, rearrange. Separate function from form.
   - **Task Unification** — assign an existing element an additional task. Packaging becomes media, the product becomes a tool.
   - **Attribute Dependency** — link two independent attributes with a dependency. "The more X, the more Y" — where the connection is unexpected.
   - **Pictorial Analogy** — replace one visual element with another, preserving form. Symbol A looks like symbol B.
3. For each pattern, generate at least 2-3 variations.
4. Select ideas where the pattern creates an instantly readable insight.

**Output:** 12-18 structured ideas (6 patterns x 2-3 variations).

**Advertising example:** Volkswagen "Think Small" — Subtraction. Huge white space, tiny car. All visual "noise" removed.

**When to use:** First method in any session — delivers maximum coverage with minimum effort.

---

### 2. SCAMPER (Structural Templates)

**Essence:** Seven transformation operators applied sequentially to a product, message, or format. Systematic enumeration of modification options.

**Input:** Object of transformation: product, existing ad, communication format.

**Process:**
1. Define the transformation object in one sentence.
2. Go through each operator, asking a question about the object:
   - **Substitute** — what to replace? Material, character, channel, time, place.
   - **Combine** — what to merge? Two products, two audiences, two formats.
   - **Adapt** — what to borrow from another category? What technique from another industry fits?
   - **Modify/Magnify** — what to enlarge, shrink, amplify, weaken?
   - **Put to other use** — where else is this applicable? Different context, different audience.
   - **Eliminate** — what to remove? Which element is unnecessary?
   - **Reverse** — what to flip? Order, roles, perspective.
3. For each operator — minimum 2 answers, even if forced.
4. Mark the most unexpected combinations.

**Output:** 14+ directions for ideas (7 operators x 2 variations).

**Advertising example:** Old Spice "The Man Your Man Could Smell Like" — Reverse. The audience is flipped: an ad for a men's product is addressed to women.

**When to use:** When there's an existing product/campaign and you need to find a new angle.

---

### 3. TRIZ: 10 Principles for Advertising (Structural Templates)

**Essence:** From Altshuller's 40 inventive principles, 10 most productive for advertising communication are selected. Each principle is a transformation operator for an advertising message.

**Input:** Advertising task formulated as a contradiction: "need X, but Y gets in the way."

**Process:**
1. Formulate the contradiction in the task.
2. Apply each of the 10 principles:
   - **Segmentation** — divide the message/audience/product into parts. Personalized versions of one campaign.
   - **Extraction** — extract one attribute and make it the hero. Isolate the main thing, discard everything else.
   - **Local Quality** — different parts perform different functions. One banner works differently in different contexts.
   - **Asymmetry** — break expected symmetry. Non-standard format, disproportionate emphasis.
   - **Merging** — combine identical operations. One message solves two tasks simultaneously.
   - **Universality** — one element performs several functions. Packaging = media channel.
   - **Nesting** — one object inside another. An ad within an ad, a story within a story.
   - **Inversion** — do the opposite. Anti-advertising, admitting flaws.
   - **Dynamicity** — the element changes depending on conditions. Adaptive creatives, context-responsive.
   - **Copying** — replace the original with a copy. Use metaphor instead of direct demonstration.
3. Select 2-3 principles most relevant to the specific contradiction.

**Output:** 10-20 directions tied to a specific contradiction in the task.

**Advertising example:** Patagonia "Don't Buy This Jacket" — Inversion. A direct call not to buy the product resolves the contradiction between commerce and environmental mission.

**When to use:** When the brief contains an obvious contradiction or constraint that seems insurmountable.

---

### 4. Morphological Analysis (Structural Templates)

**Essence:** Fritz Zwicky's method. Break the task into 5-7 independent parameters, list possible values for each, then combine values from different columns.

**Input:** Campaign brief broken down into key dimensions.

**Process:**
1. Define 5-7 campaign parameters. Standard matrix: Tone x Mechanic x Channel x Hero x Proof.
2. For each parameter, list 4-6 possible values. Example: Tone = [irony, epic, documentary, absurd, tenderness]; Hero = [user, product, antagonist, celebrity, unexpected character].
3. Randomly select one value from each column — get a combination.
4. Repeat 10-15 times, interpreting each combination as a complete idea.
5. Select 3-5 viable combinations.

**Output:** 10-15 combinations, of which 3-5 are viable concepts.

**Advertising example:** Matrix for a beer campaign: [humor x user-generated x Instagram x friends x statistics] yields a concept: funny user stories with data on how many friends get together thanks to the product.

**When to use:** When you need a volume of diverse concepts and there's a risk of getting stuck on one direction.

---

## Category B: Association / Collision

### 5. Bisociation (Association / Collision)

**Essence:** Arthur Koestler's term. The collision of two unrelated "matrices of thought" produces a creative effect. Each matrix has its own logic — at the point of collision, an insight emerges.

**Input:** Two spaces of meaning: the product's world and a donor world (an arbitrary context).

**Process:**
1. Describe the "product matrix": its context, associations, usage logic.
2. Choose a second matrix — as far removed from the first as possible (different industry, different era, different situation).
3. Find the intersection point — a shared structural element that works in both matrices.
4. Formulate the idea at the intersection point.

**Output:** 1-3 ideas with high surprise potential.

**Advertising example:** Snickers "You're Not You When You're Hungry." Matrix 1: a hungry person. Matrix 2: a celebrity with characteristic behavior. Collision point: personality transformation.

**When to use:** When you need one strong idea, not a volume of options.

---

### 6. Random Entry / Random Word (Association / Collision)

**Essence:** Edward de Bono's method. Take a random word and forcibly connect it to the task. Randomness jolts thinking out of habitual patterns.

**Input:** Brief + a random word (a concrete, visualizable noun).

**Process:**
1. Generate a random word. Requirements: concrete noun, visual, unrelated to the product.
2. List 5-7 associations, attributes, functions of this word.
3. For each association, find a connection to the brief — forcibly, through any logic.
4. Select 2-3 connections that produce an unexpected yet readable meaning.

**Output:** 2-3 unexpected directions for an idea.

**Advertising example:** Brief: bank advertising. Random word: "aquarium." Associations: transparency, enclosed space, observation, fragility. Connection to the bank: "complete transparency of terms" — a bank with no hidden fees, visualized through glass walls.

**When to use:** When you've hit a dead end and need an external stimulus to break out of a mental rut.

---

### 7. Forced Connections (Association / Collision)

**Essence:** Deliberate connection of unrelated concepts. The value lies in the space between two ideas, in the tension their combination creates.

**Input:** A list of 5-10 objects/concepts unrelated to the product. The brief.

**Process:**
1. Compile a list of random objects: items, professions, situations, places.
2. For each object, ask: "If [product] were [object], what would that mean?"
3. Explore the collision: what properties of the object transfer to the product? What contradictions arise?
4. Turn the most interesting collisions into advertising concepts.
5. Check: can the idea be read in 3 seconds?

**Output:** 5-10 "raw" ideas, of which 2-3 have potential.

**Advertising example:** Volvo + ballerina. Collision: the brute force of a truck and the grace of a ballerina. Result: Volvo Trucks — Jean-Claude Van Damme does a split between two moving trucks (steering precision = grace).

**When to use:** In early stages, when you need to expand the search space.

---

### 8. Synectics (Association / Collision)

**Essence:** William Gordon's method. Four types of analogy, each yielding a different type of idea. Principle: "Make the familiar strange, the strange familiar."

**Input:** Product/problem + readiness to think in four analogy modes.

**Process:**
1. **Direct Analogy** — find a direct analogy from nature, technology, another industry. Question: "Where in the world is a similar problem being solved?"
2. **Personal Analogy** — become the product. Question: "If I were this product, what would I feel, want, fear?"
3. **Symbolic Analogy (Compressed Conflict)** — describe the product with an oxymoron. Question: "What two opposite words describe the essence?" Examples: "safe speed," "living mechanics."
4. **Fantasy Analogy** — suspend physics. Question: "If there were no constraints, how would the product work in an ideal world?"
5. For each type of analogy, write 2-3 variations, then convert into advertising ideas.

**Output:** 8-12 ideas through four different analogy types.

**Advertising example:** Apple "1984" — Fantasy Analogy. A world without Apple = Orwell's dystopia. Macintosh launch = liberation from conformity.

**When to use:** When you need depth of metaphor, not quantity of ideas.

---

## Category C: Inversion / Disruption

### 9. Reverse Brainstorming (Inversion / Disruption)

**Essence:** Generate ideas about how to make the problem worse, then invert each answer. The brain generates negatives more easily — the method exploits this asymmetry.

**Input:** Task from the brief, reformulated as a negative.

**Process:**
1. Reformulate the task: "How do we make sure no one buys this product?" or "How do we maximally ruin the customer experience?"
2. Generate 10-15 answers to the "harmful" question — the more specific, the better.
3. Invert each answer: turn the "harmful" idea into a positive concept.
4. Evaluate the inverted ideas for viability.

**Output:** 10-15 ideas obtained through inversion.

**Advertising example:** "How to ruin an airline ad?" — "Show flight delays." Inversion: a campaign where the airline publishes actual punctuality statistics, turning a vulnerability into proof.

**When to use:** When standard brainstorming yields banal results — inversion bypasses mental blocks.

---

### 10. Worst Possible Idea (Inversion / Disruption)

**Essence:** Generate deliberately terrible ideas, analyze what exactly makes them bad, then invert specific "badness" attributes.

**Input:** Brief + intentional disabling of the inner critic.

**Process:**
1. Generate 10 of the stupidest, crudest, most boring, expensive, or impossible ideas.
2. For each bad idea, list: what specifically makes it bad? (3-4 attributes)
3. Invert each "bad" attribute separately, preserving the rest of the idea's structure.
4. Check: has the "bad" idea become good after targeted inversion?

**Output:** 10 "bad" ideas transformed into 5-7 potentially viable ones.

**Advertising example:** Bad idea: "A watch ad that lasts 24 hours." Bad attribute: too long. Attribute inversion: an ad lasting 1 second. Result: an actual campaign with one-second banners demonstrating the watch's precision.

**When to use:** When the team is afraid to propose "weird" ideas — the method legitimizes absurdity.

---

### 11. Provocation PO (Inversion / Disruption)

**Essence:** De Bono's method. Create an intentionally absurd statement (marker "PO"), then use it as a springboard to a real idea. PO is a signal: "this is not an opinion, it's a provocation for thinking."

**Input:** Brief + willingness to formulate absurdity.

**Process:**
1. Formulate a provocation using the formula: "PO: [absurd statement about the product/ad]." Examples: "PO: the ad apologizes to the viewer," "PO: the product destroys itself," "PO: the brand advertises a competitor."
2. For each provocation, apply one of four movement methods:
   - **Extract** — what's valuable in this absurdity?
   - **Moment-to-moment** — imagine the absurdity as reality, what happens next?
   - **Positive aspects** — what positive consequences would this absurd reality have?
   - **Special circumstances** — under what conditions would this not be absurd?
3. Turn the movement result into an advertising idea.

**Output:** 3-5 ideas born through deliberate provocation.

**Advertising example:** PO: "The brand advertises a competitor." Movement: under what conditions is this not absurd? When the brand is so confident in itself. Result: BMW congratulates Mercedes on its 100th anniversary: "Thank you for 100 years of competition. The first 30 years were boring."

**When to use:** When you need a breakthrough beyond category conventions.

---

## Category D: Recombination / Perturbation

### 12. Oblique Strategies (Recombination / Perturbation)

**Essence:** A set of cryptic instructions by Brian Eno and Peter Schmidt. Each card is a mysterious directive that redirects thinking. Works as a randomizer between generation passes.

**Input:** Current set of ideas that feel insufficient. A random card.

**Process:**
1. Draw a random card. Example instructions: "Honor thy error as hidden intention," "What would your closest friend do?," "Remove specifics and convert to ambiguities," "Use an old idea," "Emphasize the flaws."
2. Apply the instruction literally to the current set of ideas or to the brief.
3. Write down everything that comes to mind — don't filter.
4. Repeat with another card if the first one didn't work.

**Output:** 1-3 unexpected turns for existing ideas.

**Advertising example:** Card: "Emphasize the flaws." Applied to a car ad: instead of perfect gloss — a campaign showing scratches, dirt, dents as evidence of the owner's rich life.

**When to use:** Between recursive ideation passes — as a perturbation tool.

---

### 13. Six Thinking Hats (Recombination / Perturbation)

**Essence:** De Bono's method. Six thinking modes applied sequentially to one idea. Separation allows more complete thinking without mixing logic with emotions.

**Input:** An existing idea or set of ideas requiring evaluation and refinement.

**Process:**
1. **White Hat (facts)** — what data supports or refutes the idea? What do we know for certain?
2. **Red Hat (emotions)** — what emotional reaction does the idea provoke? Gut feeling: does it work or not?
3. **Black Hat (risks)** — what could go wrong? Where are the weak spots? What objections will arise?
4. **Yellow Hat (benefits)** — what is the idea's strength? What positive consequences?
5. **Green Hat (alternatives)** — how to modify the idea? What development paths?
6. **Blue Hat (process)** — what are the next steps? What's needed for implementation?

**Output:** Comprehensive evaluation of the idea from six angles + 2-3 refined variations.

**Advertising example:** Idea: a living billboard with plants for an eco-brand. Black Hat: plants will die in winter. Green Hat: make seasonality a feature — the billboard "dies" and "revives," visualizing the environmental problem.

**When to use:** For evaluating and refining existing ideas, not for generation from scratch.

---

### 14. Disney Creative Strategy (Recombination / Perturbation)

**Essence:** Three sequential roles for developing an idea: the Dreamer generates without constraints, the Realist builds an implementation plan, the Critic finds weaknesses. Roles are separated physically or temporally.

**Input:** Task from the brief + discipline to switch between roles.

**Process:**
1. **Dreamer** — generate without constraints. Question: "If there were no limits — budget, physics, time — what would the ideal campaign be?" Write down everything, criticism is forbidden.
2. **Realist** — take the Dreamer's ideas and build a plan. Question: "How to implement this? What resources are needed? What steps?" Transform fantasy into an executable plan.
3. **Critic** — find weaknesses in the plan. Question: "What won't work? What did we miss? Who won't like this?" Document problems without killing the idea.
4. Return to the Dreamer accounting for the criticism. Repeat the cycle.

**Output:** 2-3 ideas that have passed the full "dream — plan — critique" cycle.

**Advertising example:** Dreamer: "Launch the product into space!" Realist: "Stratospheric balloon with a camera — $50K budget." Critic: "Been done before. Need a plot twist." Dreamer 2.0: "Product falls from space and a random person finds it." Result: Red Bull Stratos — not an ad brief, but born from a similar process.

**When to use:** For developing an idea from fantasy to a realistic plan in one cycle.

---

## Category E: Volume Generation

### 15. Crazy 8s (Volume Generation)

**Essence:** 8 ideas in 8 minutes. Speed kills perfectionism and the inner critic. Format: one sheet folded into 8 sections (or 8 slots in a document).

**Input:** Brief compressed to one sentence. A timer.

**Process:**
1. Compress the brief to one sentence.
2. Set 8 minutes (or set a limit: 1 minute per idea).
3. Write 8 ideas — one per slot. Each idea: headline + one sentence of description.
4. Rule: you can't stop, can't go back to previous slots, can't evaluate.
5. After completion — mark 2-3 ideas that spark the most interest.

**Output:** 8 "raw" ideas, of which 2-3 are worth developing.

**Advertising example:** Brief: "Promote a meditation app." In 8 minutes: 1) an ad that makes you hold your breath; 2) a banner that loads intentionally slowly; 3) a story consisting of one frame of silence; 4) a collaboration with an alarm clock; 5-8) escalating absurdity from there.

**When to use:** At the start of a session for a quick "warmup" or when you need to break through a block.

---

### 16. Brainwriting 6-3-5 (Volume Generation)

**Essence:** A structured volume generation method. 6 participants write 3 ideas in 5 minutes, then pass the sheet to the next person, who develops or adds. For AI context: 6 "rounds" with development of previous ideas.

**Input:** Brief + round structure.

**Process:**
1. Round 1: generate 3 ideas in 5 minutes (or quickly, without self-censorship).
2. Round 2: take the 3 ideas from round 1, write a development or variation for each.
3. Rounds 3-6: repeat. Each round develops the previous round's ideas. You can mutate, crossbreed, invert.
4. After 6 rounds: 18 ideas (3 original x 6 iterations). Sort by potential.

**Output:** 18 ideas with traceable evolution from the initial thought to a developed concept.

**Advertising example:** Round 1: "Show the before/after of product use." Round 2: "Show only the 'before' — the viewer constructs the 'after' themselves." Round 3: "Show only the 'after' that doesn't resemble the 'before' — the viewer searches for the connection." Evolution from banality to an intriguing concept.

**When to use:** When one good idea already exists and you need to develop it in several directions.

---

### 17. Starbursting (Volume Generation)

**Essence:** Generate questions instead of answers. Six rays of a star: Who, What, Where, When, Why, How. Good questions lead to non-obvious ideas.

**Input:** Product or campaign concept.

**Process:**
1. Place the product/concept at the center.
2. For each ray, generate 5+ questions:
   - **Who** — who else could use this? Who would it surprise? Who's against it?
   - **What** — what if we scale x100? What's the most non-obvious thing about the product?
   - **Where** — where is this product inappropriate? Where is it needed most?
   - **When** — when do people think about it least? When is it critically needed?
   - **Why** — why would someone refuse? Why don't competitors do this?
   - **How** — how to explain to a child? How to show without words?
3. Select the most provocative questions.
4. Answer them — each answer = a direction for an idea.

**Output:** 30+ questions, of which 5-7 lead to strong ideas.

**Advertising example:** Product: insurance. Question "Where": "Where is insurance completely inappropriate?" Answer: "On a roller coaster." Idea: insurance advertising at amusement parks — at the moment of maximum risk awareness.

**When to use:** When the brief seems obvious and you want to find a non-obvious angle.

---

## Category F: Bonus Methods

### 18. First Principles Thinking (Bonus)

**Essence:** Decompose the task to fundamental truths, discarding all assumptions. Reassemble the solution from scratch based on basic facts.

**Input:** Brief + list of assumptions usually taken for granted.

**Process:**
1. List all assumptions about the product, category, and advertising: "advertising should be...," "in this category it's customary to..."
2. For each assumption, ask: "Is this a fundamental truth or a convention?"
3. Discard conventions, keep only fundamental truths.
4. Build the solution anew, relying only on fundamental truths.

**Output:** 2-3 ideas free from category templates.

**Advertising example:** Assumption: "A car ad should show a car." Fundamental truth: "People don't buy a car, they buy mobility/status/freedom." Result: a campaign where the car never appears — only moments of freedom.

**When to use:** When the category is oversaturated with similar advertising and a radical departure is needed.

---

### 19. Lateral Thinking Toolkit (Bonus)

**Essence:** Edward de Bono's toolkit for lateral thinking. Four key tools: Focus, Random Entry, Challenge, Alternatives.

**Input:** Brief + choice of specific tool depending on the situation.

**Process:**
1. **Focus** — choose an atypical focus point. Not the product and not the consumer, but a secondary element: packaging, the moment of purchase, sound, smell.
2. **Random Entry** — introduce a random element (see method 6), use as a catalyst.
3. **Challenge** — dispute every element of the current approach. "Why this way? What if not?" Question the format, channel, tone, hero.
4. **Alternatives** — for each decision, forcibly generate 3 alternatives. Even if the current solution seems good.
5. Combine findings from all four tools.

**Output:** 5-10 ideas generated through various lateral thinking tools.

**Advertising example:** Focus on sound: a headphones campaign where all visuals are secondary, and the hero is the sound design. An ad that needs to be listened to, not watched.

**When to use:** As a meta-level toolkit — when you need to choose one of four modes depending on the type of impasse.

---

### 20. Design Sprint Sketch (Bonus)

**Essence:** Method from Google Design Sprint. A detailed sketch of the solution, not an abstract idea. Focus on specifics: what does the final product/ad look like, what does the user see.

**Input:** An idea or direction requiring concretization.

**Process:**
1. Take one idea (from any previous method).
2. "Draw" it in 3 frames (describe textually):
   - Frame 1: what does the viewer see in the first second?
   - Frame 2: what happens next (twist, surprise, action)?
   - Frame 3: finale — message, brand, call to action.
3. Add details: text, tone, colors, music — everything that makes the idea concrete.
4. Check: can you "see" this ad from reading the description?
5. If not — add details. If yes — the idea is ready for evaluation.

**Output:** A detailed ad description, ready for evaluation and presentation.

**Advertising example:** Idea: "a bank with no fine print." Frame 1: close-up — a contract with all text in one size. Frame 2: camera pulls back — the contract is on a billboard, everything is readable from the street. Frame 3: bank logo, tagline: "Terms you don't need to search for."

**When to use:** In the final stage — for turning an abstract idea into a concrete visualization.

---

## Method Selection Matrix

| Situation | Recommended methods |
|---|---|
| Starting out, need volume | SIT Templates (1), Morphological Analysis (4), Crazy 8s (15) |
| Hit a dead end | Random Entry (6), Oblique Strategies (12), Provocation PO (11) |
| Need one strong idea | Bisociation (5), Synectics (8), First Principles (18) |
| Have an idea, need refinement | Six Thinking Hats (13), Disney Strategy (14), Brainwriting (16) |
| Category is oversaturated | First Principles (18), Reverse Brainstorming (9), Challenge from Lateral Thinking (19) |
| Need concretization | Design Sprint Sketch (20), Starbursting (17) |
| Need a breakthrough beyond boundaries | Provocation PO (11), Worst Possible Idea (10), Fantasy Analogy from Synectics (8) |
```

## File: `creative-director/references/scoring-calibration.md`
```markdown
# Scoring Calibration: Reference Rubric

This document is a calibration table for evaluating creative ideas. Three parallel scoring systems, calibrated against real campaigns. Use it as a reference during every evaluation to prevent score inflation and ensure reproducibility.

---

## 1. Six Criteria: Detailed Rubric

### Originality (weight 0.25)

The most significant criterion. Evaluates how novel the idea is for the category and culture at large.

- **1-2**: Pure category template. Any brand could have done this. Seen it 100 times. A bank with a handshake, a car on a mountain road, a family at the table with the product.
- **3**: Minimal attempt to differentiate, but it doesn't go beyond genre conventions. Different font, same thought.
- **4-5**: Noticeable attempt to stand out, but within expectations. Expected twist — the viewer guesses the payoff. "Not bad" for the category, but doesn't move culture.
- **6-7**: Fresh approach. Visible authorial thinking. The idea doesn't fit the category template. A competitor couldn't slap their logo on it without losing meaning.
- **8-9**: Unexpected. Nothing like this existed in the category. Remembered a week later. People retell it to each other. Burger King "Whopper Detour" — using McDonald's geolocation to sell their own burger.
- **10**: Creates a new genre, format, or approach. Changes the rules for the entire category. Dove Real Beauty redefined how brands talk about beauty. Old Spice "The Man Your Man Could Smell Like" created a language that was copied for years.

### Strategic Fit (weight 0.20)

Evaluates how well the idea solves the brief's objective and resonates with the target audience.

- **1-2**: Doesn't solve the brief's objective. The target audience won't recognize themselves. You could swap in any brand — nothing changes. The idea exists in a vacuum.
- **3**: Formally touches the brief's topic, but misses the target audience or the objective. Like answering the wrong question.
- **4-5**: Formally on-brief, but imprecise. Either the target audience is too broad/narrow, or the objective is addressed indirectly, or the insight is superficial.
- **6-7**: Clearly on-brief. Target audience is relevant, objective is addressed, insight works. Professional work that will satisfy the client.
- **8-9**: Perfectly on-brief AND adds something the client didn't ask for but needed. Expands the understanding of the task. Always #LikeAGirl — the brief was about the product, the solution became a cultural statement.
- **10**: Redefines the task. The client realizes they were asking for the wrong thing. Apple "Think Different" — not a computer ad, but a manifesto for those who think differently. Strategy above the brief.

### Emotional Response (weight 0.20)

Evaluates the strength and specificity of the emotional reaction.

- **1-2**: No reaction. A wall of text. Boredom. The viewer scrolls past without finishing.
- **3**: Minimal contact — the person noticed the ad but felt nothing. Background noise.
- **4-5**: Slight interest or a smile, forgotten within a minute. There's an emotion, but it's unnameable — "well, it's positive."
- **6-7**: Evokes a specific emotion. You can name it: curiosity, nostalgia, pride, surprise. The person remembers it for a day.
- **8-9**: Strong reaction: laughter, tears, anger, surprise. Tier 3 emotion — not "positive" but "lump in throat," "goosebumps," "want to show my mom." Thai Life Insurance ads — grown men cry.
- **10**: A cultural moment. People discuss, share, remember for years. John Lewis Christmas becomes an event people look forward to. Advertising transcends advertising.

### Feasibility (weight 0.15)

Evaluates the realizability of the idea given the budget, timeline, and resources.

- **1-2**: Unrealizable with the given budget, timeline, or resources. Requires technologies that don't exist or a budget 10x larger than available.
- **3**: Technically possible, but requires so many compromises that the idea loses its essence.
- **4-5**: Theoretically possible, but risky and expensive. Many dependencies, many things can go wrong. Production will eat the entire budget.
- **6-7**: Realizable with reasonable effort. Clear production plan, understood risks, adequate budget.
- **8-9**: Elegantly realizable. A simple solution to a complex problem. Minimal dependencies, maximum control. "Share a Coke" — just print names on cans.
- **10**: Can be executed tomorrow with minimal resources for maximum impact. The idea is so simple to execute that the main question is "why hasn't anyone done this before?"

### Scalability (weight 0.10)

Evaluates the idea's potential for development across time, channels, and markets.

- **1-2**: One-time execution. No series, no development. Done and forgotten.
- **3**: Can be repeated 1-2 times, but with diminishing returns. Second time won't surprise.
- **4-5**: 2-3 variations, but limited potential. Works in one channel. Adaptation to other markets is problematic.
- **6-7**: A season-long series. Works across 3+ channels. Can be adapted to other markets with localization.
- **8-9**: A platform for years. Infinite series. International potential without losing meaning. Spotify Wrapped — new every year, anticipated every year.
- **10**: A cultural platform that outgrows advertising. Red Bull Stratos — not a campaign, but a world-scale event. Nike "Just Do It" — 30+ years, infinite iterations, cultural code.

### Simplicity (weight 0.10)

Evaluates how quickly and easily the idea is understood.

- **1-2**: Requires instructions to understand. Complex mechanics. Three steps, two conditions, one QR code.
- **3**: Understandable, but with effort. Need to think, reread, ask again.
- **4-5**: Understandable after explanation. The idea doesn't read on its own, but once explained — it's logical.
- **6-7**: Immediately understandable, but requires 30 seconds of attention. There's a nuance that unfolds.
- **8-9**: One sentence. One image. Instant. Can be retold in 5 seconds and the listener gets it.
- **10**: So simple it seems obvious. But no one did it before. Coca-Cola "Share a Coke" — names on cans. That's it. Genius.

---

## 2. HumanKind Scale (Leo Burnett) — Detailed Scale

Leo Burnett's proprietary scale evaluating an idea's impact on people and culture. Use as a second filter after the six criteria.

| Score | Level | Description | Calibration Example |
|-------|-------|-------------|---------------------|
| 1 | Destructive | Actively harms the brand. People reject, boycott. Pollutes the media space. Tone-deaf. | Pepsi Kendall Jenner (trivializing protests) |
| 2 | No Idea | No thought. Formal budget fulfillment. Product in frame, logo at the end. | Typical stock-photo banner "20% off" |
| 3 | Invisible | No interest, no emotions. Wallpaper. Cliché. Viewer doesn't notice, doesn't remember, doesn't react. | Bank ad "we're close by" with a handshake |
| 4 | No Brand Purpose | There's some kind of idea, but it's unclear why the brand exists. Product without meaning, message without position. | Ad demonstrating the product but not answering "why" |
| 5 | Brand Purpose | There's a mission, people understand what the brand does and why. Meaningful communication, but no breakthrough. | IKEA "The Wonderful Everyday" |
| 6 | Intelligent Idea | Smart approach. Engaging. Not tied to a single channel. The idea is bigger than the format. | Burger King "Whopper Detour" |
| 7 | HumanKind Act | Changes people's thoughts, feelings, or actions. Flawless craft. Idea and execution at the highest level. | Nike "Dream Crazy" (Kaepernick) |
| 8 | Changes Thinking | Useful, interesting, becomes part of people's lives. People are grateful to the brand for the experience. | Spotify Wrapped |
| 9 | Changes Living | Inspires lifestyle change. People act differently because of the brand. | Dove "Real Beauty" (the entire campaign) |
| 10 | Changes the World | Social change on a global scale. Theoretical ceiling. | Theoretical ceiling — practically unachievable in advertising |

Important: most professional work falls in the 4-6 range. A score of 7+ is already Cannes shortlist level. Don't inflate.

---

## 3. Grey Scale — Grey Group Evaluation Scale

An alternative scale focusing on the quality of creative work as such.

| Score | Level | Description |
|-------|-------|-------------|
| 1 | Toxic | Harms the brand and people. Offensive, incompetent, dangerous. |
| 2 | Careless | Sloppy, unprofessional. Visible errors, no attention to detail. |
| 3 | Dull | Boring, predictable. Evokes no response whatsoever. |
| 4 | Expected | Expected for the category. "Well, okay." Not embarrassing to show, but nothing to be proud of. |
| 5 | Capable | Professional but unremarkable. Solid work without ambition. |
| 6 | Gratifying | Pleasant, you want to watch. There's something that hooks. Above average. |
| 7 | Original | Fresh, memorable. You want to show colleagues. Potential for local festivals. |
| 8 | Best in category | Best in category for the year. Competitors are envious. Cannes shortlist. |
| 9 | Best in show | Cannes shortlist / D&AD Pencil. Work the industry talks about. |
| 10 | Best in the world | Grand Prix. Sets the standard for years to come. |

The median for a quality agency is 5-6. If your scores are consistently higher — you're not calibrating, you're flattering.

---

## 4. Calibration Anchors: Real Campaigns

These campaigns are fixed points on the scale. Use them for comparison during every evaluation.

**Level 10 (Grand Prix / cultural shift)**
- Fearless Girl (McCann, State Street) — sculpture facing the bull on Wall Street. Simplicity, symbolism, cultural resonance. Became a permanent monument.
- Dumb Ways to Die (McCann Melbourne, Metro Trains) — a song about railway safety. 5 billion views, 21% reduction in incidents. Advertising that became pop culture.

**Level 9-9.5 (Cannes Gold / Lion / D&AD Pencil)**
- Dove Real Beauty Sketches (Ogilvy) — FBI sketch artist draws women from their own description vs. a stranger's description. Visualizing distorted self-perception.
- Burger King Moldy Whopper (INGO, David, Publicis) — a beautiful shot of a moldy burger. Shock + message about no preservatives.
- Nike Dream Crazy (Wieden+Kennedy) — Kaepernick: "Believe in something, even if it means sacrificing everything." Polarization as strategy.

**Level 8-8.5 (Cannes Silver-Bronze / best in category)**
- Spotify Wrapped (in-house) — personalized year-end summaries. Users create content themselves. An annual tradition.
- IKEA ThisAbles (McCann Tel Aviv) — 3D-printed furniture adapters for people with disabilities. Free, open-source.
- Always #LikeAGirl (Leo Burnett) — reframing the insult "like a girl" into a compliment.

**Level 7-7.5 (solid professional work, local awards)**
- Good work from a regional agency. Clear insight, professional execution, but no cultural breakthrough. Local festival shortlist.

**Level 6 and below (category average)**
- Category standard. Professional but predictable. Not remembered after a week.

---

## 5. Rules Against Score Inflation

Inflation is the main enemy of useful evaluation. AI models tend to inflate scores. Apply these rules strictly.

**Rule 1: Real Analogues Test.** Before assigning a score of 9+, name 3 real Cannes-winning campaigns at that level. Is your idea truly comparable? If not — lower the score.

**Rule 2: Batch Control.** If all ideas in a batch score 8+, something is wrong with calibration. This is statistically impossible. Re-evaluate the entire batch from scratch.

**Rule 3: Normal Distribution.** The average score for a batch of 10 ideas should be 5-6. If the average is above 7, you're inflating. Go back and recalibrate.

**Rule 4: Specificity Test.** Replace the brand with a competitor. If the idea works exactly the same — originality is 5 at most. The idea must be inseparable from the brand.

**Rule 5: "Would I share this?" Test.** Mentally show the idea to a friend who doesn't work in advertising. If they're not impressed, won't forward it, won't mention it at dinner — score below 7. Ad people tend to overvalue "clever" ideas that only work within the industry.

**Rule 6: First Reaction.** Record your initial score before analysis. If the score rises more than 2 points after analysis — you're rationalizing, not evaluating. Return to your first reaction.

**Rule 7: Time Test.** Imagine this idea a year from now. Will it be in a "best of the year" compilation? If not — no higher than 7.

---

## 6. Multi-Perspective Panel (CAT Simulation)

Consensual Assessment Technique (CAT) — a method where multiple experts evaluate independently, then compare results. Simulate four perspectives.

### Four Perspectives

**Creative Director (craft and idea).** Focus: originality of approach, execution quality, visual language, tone of voice. Question: "Would I be proud of this work in my portfolio?"

**Strategist (brief fit and insight).** Focus: brief alignment, insight depth, target audience fit, business logic. Question: "Does this solve the client's problem?"

**Consumer (interest and emotion).** Focus: first reaction, comprehensibility, emotional response, desire to engage. Question: "Is this interesting to me? Would I stop scrolling?"

**Jury Member (award-worthiness).** Focus: novelty for the industry, craft, scale of the idea, case potential. Question: "Will this make the Cannes shortlist?"

### Panel Rules

1. Each perspective evaluates independently, without seeing others' scores.
2. The final score is not an arithmetic average, but the result of discussing discrepancies.
3. If the discrepancy between perspectives is greater than 2 points — it's a signal. Investigate the cause.
4. High discrepancy = polarizing idea. This can be good for awards (juries love boldness), but risky for the client (consumers may not accept it).
5. Low discrepancy with high scores = strong idea with consensus. Rare.
6. Low discrepancy with average scores = safe but unambitious work.

### Typical Discrepancy Patterns

- CD high, consumer low: an "advertising" idea that the industry loves but people don't.
- Consumer high, jury low: a mass idea without creative novelty. It works but doesn't surprise.
- Strategist high, CD low: strategically sound but dull in execution. Needs better craft.
- Jury high, strategist low: "festival" work created for awards, not for business.

---

## 7. Three Axes: Final Summary

The final evaluation is built on three axes. Each axis serves its own function.

### Axis 1: Brief Compliance (gate)

This is a binary filter, not a scale. The idea either passes or doesn't. Any failure on this axis means the idea is not admitted to further evaluation, regardless of creative strength.

Checkpoints: target audience matches the brief, objective is addressed, brand is recognizable, constraints are met, tone of voice is appropriate.

### Axis 2: Idea Strength (6-criteria weighted score)

Weighted score across six criteria:

```
Total = Originality * 0.25
      + Strategic Fit * 0.20
      + Emotional Response * 0.20
      + Feasibility * 0.15
      + Scalability * 0.10
      + Simplicity * 0.10
```

Interpretation: 8+ excellent, 6-7 good, 5-6 average, below 5 weak.

### Axis 3: Scalability and Idea Level

Four questions to assess scale:
1. How many channels does the idea cover without adaptation?
2. How many iterations/series can be produced?
3. Does the idea work in other markets?
4. Can the idea outlive a single flight?

### Idea Level Matching

It is critically important to determine the idea's level and match it to the brief's objective.

**Big Idea** — a platform idea that defines the brand for years. Example: Dove "Real Beauty," Coca-Cola "Open Happiness," Nike "Just Do It."

**Campaign Idea** — a specific campaign within a Big Idea. Example: Dove "Real Beauty Sketches" (within the Real Beauty platform), "Share a Coke" (within Open Happiness).

**Execution Idea** — a specific execution within a campaign. Example: Dove "Girls Unstoppable" (within Sketches), Coca-Cola "Unlock the 007 in You" (within Share a Coke).

### Mismatch as a Problem

The idea's level must match the brief's objective. Level mismatch is a common error:

- Big Idea for shelf talkers — a waste of time and resources. The client needs an execution, and they got a manifesto.
- Execution Idea for a rebrand — too small. The client needs a platform, and they got a single poster.
- Campaign Idea when a Big Idea is needed — will work for six months and die. No foundation for growth.

Before evaluating, determine: what idea level does the brief call for, and what idea level is being proposed. If there's a mismatch — it lowers the strategic fit score, even if the idea itself is strong.
```

## File: `creative-director/references/storytelling-frameworks.md`
```markdown
# Narrative Frameworks for Advertising

Six working structures for building stories in advertising formats. Each framework is a ready-to-use template, not theory. Apply directly to the brief.

---

### 1. Story Spine (Kenn Adams / Pixar)

**Author:** Kenn Adams, popularized by Pixar
**Essence:** An eight-line template that forces the story to move through cause-and-effect links. Each line flows from the previous one, eliminating random turns and loose logic. The fastest way to assemble a narrative from scratch.
**Structure:**
1. Once upon a time... (the hero and their world)
2. Every day... (routine, status quo)
3. But one day... (the inciting incident, a break from the familiar)
4. Because of that... (first consequence)
5. Because of that... (second consequence, escalation)
6. Because of that... (third consequence, peak tension)
7. Until finally... (climax, resolution)
8. And ever since... (the new normal)

**Timing for advertising:**
- 15 sec: only lines 3-7. Enter straight from the conflict, exit at the resolution. No time for exposition.
- 30 sec: full template. Lines 1-2 take 5-7 seconds, the main chain — 15-18 seconds, the finale — 5-7 seconds.
- 60 sec: expand the "because of that" chain to 4-5 links. Each link is a separate scene with escalation.

**Example:** 30-second dishwashing detergent spot. "Every day Maria spent an hour on dishes. But one day she tried X. Because of that, dishes took ten minutes. Because of that, evenings became free. And ever since, evenings belong to her." The brand enters at line 3, the benefit unfolds through the chain of consequences.
**When to use:** when you need to quickly assemble a structure for any format and ensure every plot turn is logically justified.

---

### 2. Sparkline (Nancy Duarte — "Resonate")

**Author:** Nancy Duarte, book "Resonate"
**Essence:** Rhythmic alternation between "what is" (current reality, pain) and "what could be" (a better future). Each switch amplifies the contrast and engagement. The finale is a bridge between two worlds, where the brand becomes the guide from one state to the other.
**Structure:**
1. What is (current pain, a recognizable situation)
2. What could be (the first glimmer of possibility)
3. What is (deeper pain, specifics)
4. What could be (a clearer vision of the future)
5. New reality (the bridge — the brand as the one making the transition possible)

**Timing for advertising:**
- 15 sec: one switch. "What is" — 5 sec, "what could be" — 7 sec, brand — 3 sec.
- 30 sec: two switches. A building rhythm of contrasts.
- 60 sec: full sparkline with 3-4 switches. Each cycle deepens both the pain and the hope.

**Example:** Always #LikeAGirl. Alternation between what girls hear about themselves (limitations, stereotypes) and who they can be (strength, confidence). Each switch intensifies the tension. The brand reveals the final shift — redefining the phrase "like a girl" from an insult into strength.
**When to use:** for campaigns related to behavior change, social impact, brand manifestos, and any content where you need to show the contrast between problem and solution.

---

### 3. Freytag's Pyramid

**Author:** Gustav Freytag, 19th century
**Essence:** The classic five-act dramatic arc. Works for any story that needs an emotional climax. The main rule: no climax — no memorability. A spot without a peak moment is forgotten instantly.
**Structure:**
1. Exposition (world, characters, context)
2. Rising action (complications accumulate, stakes rise)
3. Climax (peak moment, turning point)
4. Falling action (consequences, realization)
5. Dénouement (new normal + brand)

**Timing for advertising:**
- 15 sec: climax at the 8-10 second mark. Exposition compressed to 3-4 seconds. Dénouement — 2-3 seconds with the brand.
- 30 sec: climax at the 18-22 second mark. Time for proper rising action and emotional falling action.
- 60 sec: full pyramid with full-scale build-up. Exposition up to 15 seconds, rising action up to 20, climax 5-8, falling action and dénouement 15-20.

**Example:** John Lewis Christmas ads. Full Freytag's Pyramid: introduction to the character, escalation of emotional tension through a series of scenes, emotional climax seconds before the brand appears, a gentle dénouement. The brand appears during the falling action, when the viewer is maximally vulnerable.
**When to use:** for traditional narrative spots where there's a production budget and duration of 30 seconds or more, especially for emotional storytelling and brand image advertising.

---

### 4. Monroe's Motivated Sequence

**Author:** Alan Monroe, 1930s
**Essence:** A persuasion structure built for action. Doesn't just tell a story but leads the viewer to a specific step. Each stage is a funnel step: from attention to need, from solution to visualization of the outcome and call to action.
**Structure:**
1. Attention (hook — a shocking fact, question, micro-story)
2. Need (identify the problem, make it personal)
3. Satisfaction (present the solution — product/brand)
4. Visualization (show life with the solution)
5. Action (clear CTA)

**Timing for advertising:**
- 15 sec: only attention + need + action. Three beats: hook, pain, CTA. The solution is implied through the brand.
- 30 sec: all 5 stages in compressed form. Visualization — one vivid scene.
- 60 sec: full sequence with an extended visualization. The visualization stage can take up to 15-20 seconds — this is the key moment where the viewer "tries on" the result.

**Example:** Charity: Water. Attention — a child walks kilometers for water. Need — millions lack clean water, diseases, child mortality. Satisfaction — well technology, a simple solution. Visualization — a thriving village, children in school, clean water from the tap. Action — "Donate now, $30 provides one person with water for life."
**When to use:** for direct response advertising, fundraising, infomercials, and any format where the end goal is a specific viewer action right now.

---

### 5. Pixar Rules (Top 7 for Advertising)

**Author:** Pixar team, collected by Emma Coats
**Essence:** Not a structure, but a quality checklist. Use after writing a script or concept. Seven rules from the full Pixar list most applicable to advertising. Run every finished script through this filter.
**Structure (checklist):**
1. "You admire a character for trying more than for their successes" — show the struggle, not just the result. Struggle creates empathy.
2. "What is your character good at? Throw the polar opposite at them" — create conflict through contrast. The character's comfort zone is their vulnerability.
3. "Come up with your ending before you figure out your middle" — know the punchline in advance. Write from the ending to the beginning.
4. "Simplify. Focus. Combine characters. Hop over detours" — especially critical for short formats. Every frame must work.
5. "What is the essence of your story? The most economical telling of it?" — the golden question for 15-second formats. If you can't say it in one sentence, the plot is loose.
6. "Discount the 1st thing that comes to mind. And the 2nd, 3rd, 4th, 5th" — serial order effect. The first ideas are clichés. The real work begins after the fifth iteration.
7. "Give your characters opinions. Passive and malleable might seem likable to you as you write, but it's poison to the audience" — a character with a position is memorable. A neutral character is invisible.

**Timing for advertising:** applied to any format as a post-check. Doesn't directly affect duration.
**Example:** Checking a Nike spot script. Rule 1 — is the athlete's struggle shown, not just the finish? Rule 4 — can a scene be removed without losing meaning? Rule 6 — is this the first idea or the tenth? If the script passes all 7 filters, it's ready for production.
**When to use:** after creating any script or concept as a final quality control before client presentation.

---

### 6. Hero's Journey (Customer = Hero, Brand = Guide)

**Author:** Joseph Campbell, advertising adaptation — Donald Miller (StoryBrand)
**Essence:** A condensed version of the monomyth for advertising. Key principle: the customer is the hero, the brand is the guide. A brand that makes itself the hero loses the audience. The customer doesn't want to admire the brand — they want the brand to help them become a better version of themselves.
**Structure:**
1. Ordinary world (the customer's current life, their context)
2. Call to adventure (a problem or opportunity that disrupts the status quo)
3. Meeting the guide (the brand appears — NOT as the hero, but as a mentor, tool, helper)
4. Crossing the threshold (the customer tries the product/service, takes the first step)
5. Transformation (life has changed, the customer is different)
6. Return with the gift (new status quo, ability to share the story)

**Timing for advertising:**
- 30 sec: only steps 1, 2, 4, 5. Skip the explicit brand-as-guide appearance (it's visible through the product at step 4) and the return.
- 60 sec: full journey in condensed form. Each step — 8-10 seconds. Step 3 (meeting the guide) is the most delicate: the brand must appear unobtrusively.

**Example:** Nike — the athlete is always the hero, Nike is the tool that helps them overcome themselves. Apple — the creative person is the hero, Apple is the tool that removes barriers between idea and execution. In both cases, the brand never puts itself at the center. It spotlights the customer.
**When to use:** for brand image campaigns where the brand wants to build a long-term emotional connection with the audience through the position of a mentor, not a contender for attention.
```

