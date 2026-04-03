---
id: github.com-mikonos-zk-steward-companion-fe9a5eb4-k
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:27:59.136337
---

# KNOWLEDGE EXTRACT: github.com_mikonos_zk-steward-companion_fe9a5eb4
> **Extracted on:** 2026-04-01 08:31:48
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007519606/github.com_mikonos_zk-steward-companion_fe9a5eb4

---

## File: `README.md`
```markdown
# ZK Steward Companion Skills

Companion skills for **[ZK Steward](https://github.com/msitarzewski/agency-agents)** (from [The Agency](https://github.com/msitarzewski/agency-agents)). Use these with the ZK Steward agent to get the full Luhmann-style knowledge-base workflow.

## What’s in this repo

| Skill | Purpose |
|-------|---------|
| **link-proposer** | For new notes: suggest link candidates (3-way search), keyword/index entries, and one Gegenrede (counter-question). |
| **index-note** | Create or update index/MOC entries; daily sweep; network repair from health reports. |
| **strategic-advisor** | Default when intent is unclear: multi-perspective analysis, trade-offs, action options. |
| **workflow-audit** | Check multi-phase flows (e.g. deep-learning, meeting-note) against a checklist; Deming + Gawande style. |
| **structure-note** | Reading-order and logic trees for articles, project docs, or complex topics; Folgezettel-style argument chains. |
| **random-walk** | Random walk the knowledge network; tension/forgotten/island modes; script in `random-walk/scripts/get_random_notes.sh`. |
| **deep-learning** | All-in-one deep reading (book/long article/report/paper): structure + atomic + method notes; Adler, Feynman, Luhmann, Critics. |

Skills are in **Chinese** (original language). Paths in the docs (e.g. `05_每日记录/`, `03_索引/`, `memory/`) follow the original vault layout—**adapt them to your own folder names** when installing.

## Install (Cursor)

1. Copy the `skills/` folder into your project so that Cursor can see it as skills, e.g.:
   - **Option A**: Copy each skill under `.cursor/skills/` in your repo:
     ```bash
     cp -r skills/link-proposer .cursor/skills/
     cp -r skills/index-note   .cursor/skills/
     cp -r skills/strategic-advisor .cursor/skills/
     cp -r skills/workflow-audit .cursor/skills/
     cp -r skills/structure-note .cursor/skills/
     cp -r skills/random-walk .cursor/skills/
     cp -r skills/deep-learning .cursor/skills/
     ```
   - **Option B**: Clone this repo as a subfolder and add it to your Cursor rules/skills path if your setup supports it.

2. **Path customization**: If your vault uses different folders (e.g. `daily/`, `index/`), edit the paths inside each SKILL.md and, for link-proposer and random-walk, the script `get_random_notes.sh` in each (or set env vars `NOTES_DIR`, `INDEX_DIR` before running).

3. **Random-notes script** (link-proposer path C, random-walk): From your vault root, run so path defaults work:
   ```bash
   export NOTES_DIR="05_每日记录"   # or your daily-notes folder
   export INDEX_DIR="03_索引"      # or your index folder
   ./path/to/skills/link-proposer/scripts/get_random_notes.sh --mode tension --count 6
   ```

## Install (Claude Code / other tools)

Copy the contents of each `skills/<name>/SKILL.md` into your tool’s agent/skill format (e.g. Claude Code agents). Ensure paths and any script paths are adjusted for your environment.

## ZK Steward agent

Get the ZK Steward personality (Luhmann-style knowledge steward) from The Agency:

- **Upstream**: [agency-agents/specialized/zk-steward.md](https://github.com/msitarzewski/agency-agents/blob/main/specialized/zk-steward.md) (after merge) or from [the PR](https://github.com/msitarzewski/agency-agents/pull/84).
- Use ZK Steward + this companion repo for the full “ZK Steward 完全体” workflow.

## License

MIT. Same spirit as The Agency and the original AI-Zettelkasten rules.
```

## File: `skills/deep-learning/README.md`
```markdown
# deep-learning — Deep Reading for Zettelkasten

All-in-one deep reading skill: turn books, long articles, and reports into a connected knowledge network (structure notes, atomic notes, method notes, index). Uses Mortimer Adler for structure, Feynman for clarity, Luhmann for linking, plus Pragmatist and Critics. Enforces case fidelity and actionable extraction.

## When to Use

Use this skill when:

- You want to **deeply digest** a book, long article, research report, or paper and **build a knowledge network** (not just a summary).
- You need **structure notes** (reading order + argument tree), **atomic notes** (concepts), **method notes** (SOPs/checklists), and **index notes** (entry points).
- You say things like: “help me turn this book into a Zettelkasten,” “depth-first read this report,” “structure note + atomic notes for this article.”

## Quick Reference

| Phase   | Output                    | Key artifact                          |
|---------|---------------------------|----------------------------------------|
| 0       | Pre-game plan             | `YYYYMMDD_01_[title]_执行计划.md`     |
| 1       | Structure note            | `templates/structure_note_template.md`|
| 2       | Index note                | `templates/index_note_template.md`   |
| 2.5     | Index onboarding          | Mount to existing index; move to index dir |
| 3       | Atomic notes + Luhmann Scan | `references/luhmann_scan.md`       |
| 4       | Method notes              | `templates/method_note_template.md`   |
| 5       | Feynman review            | De-jargon, logic, topology            |
| 6       | Network review            | ≥2 links per note; multi-index mount  |
| 6.5     | Workflow audit (optional) | If `workflow-audit` skill is present  |

## Workflow at a Glance

1. **Phase 0**: Produce an execution plan (≥6 TODOs + context).
2. **Phase 1**: Create structure note (core thesis + logic chain). Uses `structure-note` if available.
3. **Phase 2**: Create index note (keywords + entry points). Uses `index-note` if available.
4. **Phase 2.5**: Mount the new index to an existing index; move index file into your index directory.
5. **Phase 3**: Create atomic notes from structure; run Luhmann Scan (dependencies, links, methods) per note.
6. **Phase 4**: Turn discovered methods into method notes (SOP/template/checklist).
7. **Phase 5**: Feynman review (clarity, metaphor, logic, surprise links).
8. **Phase 6**: Ensure ≥2 bidirectional links per note; complete index onboarding; multi-index mount check.
9. **Phase 6.5**: Optional workflow-audit pass if that skill is installed.

## Requirements

- **Paths**: The skill assumes an **index directory** (e.g. `03_索引/` or `Index/`) and a **daily/task directory** (e.g. `05_每日记录/YYYY/MM/DD` or `Daily/`). Adapt path names in the skill or your vault to match.
- **Optional companion skills**: For full automation, `structure-note`, `index-note`, `file-organize`, and `workflow-audit` can be used when available; the skill still works with manual steps if they are missing.
- **Language**: SKILL.md and templates are in Chinese; prompts and outputs follow your locale.

## Install (skills.sh)

If this skill is published to GitHub:

```bash
npx skills add <owner/repo>
```

Example (when repo is `your-username/deep-learning`):

```bash
npx skills add your-username/deep-learning
```

## Repo Layout

```
deep-learning/
├── README.md           # This file
├── SKILL.md            # Main skill instructions (required)
├── references/
│   ├── expert_personas.md
│   └── luhmann_scan.md
└── templates/
    ├── atomic_note_template.md
    ├── index_note_template.md
    ├── method_note_template.md
    └── structure_note_template.md
```

## Publishing This Skill to skills.sh

1. Create a **new GitHub repository** (e.g. `deep-learning` or `skill-deep-learning`).
2. Copy the **entire contents** of this folder (`SKILL.md`, `README.md`, `references/`, `templates/`) to the **root** of the repo (or into a single subfolder if you host multiple skills in one repo).
3. Add a short repo description and topics (e.g. `zettelkasten`, `deep-reading`, `cursor`, `skills`).
4. Push; then install via skills.sh:
   ```bash
   npx skills add <your-github-username>/<repo-name>
   ```
5. Optionally submit or list the skill on [skills.sh](https://skills.sh) so others can discover it.

No build step required. The platform renders `SKILL.md` from the repo.
```

## File: `skills/deep-learning/SKILL.md`
```markdown
---
name: deep-learning
description: 全能深度阅读工具（All-in-One Deep Reading）。适用于书/长文/研报/论文的深度消化。Use when 用户要深度消化一本书/长文/研报/论文并构建知识网络、产出结构笔记与原子笔记。融合 Mortimer Adler（结构）、Feynman（解释）、Luhmann（网络）、Pragmatist（工具化）、Critics（辩论）；强制 High Fidelity 案例保留与 Actionable 工具提取。关键词：深度阅读、结构笔记、deep learning、卢曼。
---

# 深度阅读 (Deep Reading)

> **核心理念**：不仅要理解世界（Understand），还要改变世界（Act）。
> **适用范围**：Book, Long-form Article, Research Report, Academic Paper.

## 专家座席 (The Council)

1.  **Mortimer Adler** (The Architect): 负责结构化，提取核心命题和逻辑树。
2.  **The Pragmatist** (The Engineer): 负责工具化，提取可执行的 SOP、模板和清单。
3.  **Richard Feynman** (The Teacher): 负责解释力，确保概念去魅，用人话讲清楚。
4.  **Niklas Luhmann** (The Librarian): 负责连接性，确保知识入网，有机生长。
5.  **The Critics** (The Stress Testers): Musk, Socrates, Munger 负责压力测试和辩论。

---

## 核心法则 (The Iron Rules)

1.  **Always Deep**: 无论输入长短，默认按最高规格处理（结构+工具+辩论）。
2.  **Case Fidelity (案例保真)**:
    *   **有原文/书在手**：禁止概括性改写；原子笔记中涉及案例、研究处须保留**具体数字、作者/机构、时间线、原话**（可标页码）。
    *   **无原文、仅摘要或记忆**：在笔记中标注 `来源: 本书/摘要，未核对原文`；保留能确定的专有名词与结论，**禁止编造细节**；Feynman 验收时标「案例保真：部分（无原文）」。
3.  **No Vague Verbs (模糊词禁令)**: 禁止使用 "优化"、"加强"、"适当" 等虚词。必须转化为**具体动作**或**量化指标**。
4.  **Metadata Mandatory (元数据强制)**: 所有笔记必须包含 YAML Frontmatter (type, tags, links, description)。**禁止省略**。`description` 回答两个问题：这张笔记最值得告诉别人的一个洞察是什么？费曼会怎么向别人介绍这张笔记。100字内，供 index-note 归网时快速定性使用。

---

## 归位与入网（与 file-organize 对齐）

本 skill 的产出**归位**与**入网**规则与 file-organize 一致：物理按天落 05_每日记录，MOC 在 03_索引 用链接拉取；入网步骤与 file-organize 共用同一套定义。

| 事项 | 规则 | 详见 |
|------|------|------|
| **归位** | 在 `05_每日记录/YYYY/MM/YYYYMMDD/` 下**新建本次任务文件夹**（若日期目录不存在则先创建），本次任务笔记默认落在该文件夹内。**索引笔记**例外：物理位置在 `03_索引/`，创建后从 05 任务目录**移动**到 03 下（与 file-organize 类型表一致） | Phase 2.5 步骤 2 |
| **入网** | **索引笔记**：在已存在索引中添加入口（挂载），本索引笔记底部链回父索引。**结构/原子/方法笔记**：在 `03_索引/` 的 MOC 里按关键词添加入口 + 笔记底部反链（与 file-organize 入网步骤一致） | 索引笔记入网见 Phase 2.5 步骤 1；结构/原子/方法入网见 **file-organize** `references/03索引实现MOC流程.md`，Phase 6 执行 |

**结构笔记命名**：`YYYYMMDD_00_[标题]_结构笔记.md`。日期文件夹不存在则创建。

---

## 工作流程 (The Workflow)

**执行顺序**：Phase 0 → 1 → 2 → 2.5 → 3 → 4 → 5 → 6 → **6.5（流程执行审查，强制）**，不可跳步；Phase 2.5 须在 Phase 2 完成后立即执行；Phase 6.5 须在 Phase 6 完成后立即执行。

### Phase 0: Pre-game Plan (准备)
在开始 Phase 1 前产出执行计划；落盘为 `YYYYMMDD_01_[书名]_执行计划.md`（与结构笔记同目录），并在 task.md 的 Preparation 下链接该文件。

确保包含：
1.  **TODO List** (≥6 项)：如全书论证骨架、关键概念、论证链、框架提取、方法提取、案例核实、批判性审查、入网连接。
2.  **Context**：读取意图（我要解决什么问题？）。

### Phase 1: Overview & Structure (概览与骨架)
**Agent**: Mortimer Adler

1.  **任务**: 创建结构笔记；产出须符合 `templates/structure_note_template.md`，含核心命题、逻辑支撑链与**阅读顺序 (Reading Sequence)**（每序列列出笔记顺序；该顺序将作为 Phase 3「阅读顺序链」的权威来源）。
2.  **说明**: 强制调用 `structure-note` skill

### Phase 2: Index Design (索引设计)
**Agent**: Niklas Luhmann
> "不要问它属于哪个分类，问它和谁对话。"

1.  **任务**: 为本书/本文创建索引笔记；产出须符合 `templates/index_note_template.md`，含关键词与多入口。
2.  **索引命名（强制）**：索引**文件名与标题**必须按**领域**命名，与 **file-organize** `references/03索引实现MOC流程.md` 的「索引层级与命名约定」一致：
    *   **必须**：从材料内容提炼**知识领域**（如「AI产品观与能力观」「多Agent与一人公司」），用领域名作为 `索引_<主题>_<领域>.md` 中的 `<领域>`。
    *   **禁止**：用材料名（书名/文章名/作者/来源/活动名/日期）作为索引名；这些信息只写在索引正文的「**来源说明**」或 frontmatter，不得进入文件名。
    *   **执行顺序**：先定领域名 → 再创建索引笔记 → 正文内写来源说明（例：「本索引内容主要来自 [书名/访谈名]，深度阅读产出见 [路径]」）。
3.  **说明**: 强制调用 `index-note` skill；调用前先完成「领域名」决策。

### Phase 2.5: 索引笔记入网（挂载）+ 归位
**Agent**: Niklas Luhmann

索引笔记创建完成后立即执行：**入网**（在已存在索引中挂载）→ **归位**（物理移动到 03_索引）。

1.  **入网（挂载）**：在 `03_索引/` 下选定一个（或多个）与本书主题相关的**已存在索引**，在其中添加入口指向本索引笔记（如子专题表追加 `- [[本索引笔记名]] — 领域简述，YYYYMMDD`；**说明用领域简述，不用书名/来源**）。本索引笔记底部链回该父索引。
2.  **归位**：将本索引笔记**文件**从当前任务目录（`05_每日记录/.../`）**移动**到 `03_索引/` 下合适位置（根目录或某主题子文件夹）。移动后父索引中的 `[[本索引笔记名]]` 仍有效（仅文件名，不依赖路径）。
3.  **多索引挂载检查**延后至 Phase 6：本索引内提到的笔记还可挂到哪些其他索引，届时统一检查并添加入口。

### Phase 3: Recursive Growth (递归生长)
**Agent**: Luhmann & Feynman
> 核心创新：边创建边发现 (Luhmann Scan)。

**流程**:
1.  **Round 1 (骨架)**: 从结构笔记出发，创建所有显式链接的 **Atomic Note (概念)**。
2.  **Luhmann Scan (每张必做)**：见 `references/luhmann_scan.md`。三项——前置依赖、潜在连接、**方法论发现**（若概念附带可执行 how → 记入 task，Phase 4 创建详细的 Method Note）。在 task.md 中每张卡记录格式：`前置 → Round 2: [[A]]. 连接 → Round 3: [[B]]. 方法论 → [[方法名]] (Phase 4).`
3.  **Round 2 (血肉)**: 创建发现的新笔记，继续 Luhmann Scan。
4.  **Round 3+ (边缘)**: 直到完成或超出范围。

**Atomic Note 规范**:
*   **模板**: `templates/atomic_note_template.md`
*   **聚焦**: 定义 (Definition)、机制 (Mechanism)、语境 (Context)。
*   **验收**: 费曼测试 (外行能听懂)。

**阅读顺序链 (Reading-Order Chain)**（强制）:
*   **卢曼策略**：阅读路径应长在**网络里**，而非只存在于结构笔记这一张「地图」。Folgezettel 思维——序列本身是一条链，每张卡带「上一张 / 下一张」，读者无需回到结构笔记即可顺次阅读。
*   **技能契约**：凡被列入结构笔记「阅读顺序」的笔记，**必须在笔记内**建立序列内前后链接（见 atomic 模板「阅读顺序导航」）。结构笔记是入口；一旦进入某 Sequence，由各笔记的「上一张 / 下一张」承担延续阅读。
*   **执行**：Round 1 创建完某 Sequence 中的笔记后，逐张检查并补全「阅读顺序导航」：首张无上一张、末张无下一张可标「—」或省略；中间张必须含 `← [[上一张]] | [[下一张]] →`。

### Phase 4: Methodology Consolidation (方法论整理)
**Agent**: The Pragmatist

将 Phase 3 发现的方法论创建为 Method Note。

**Method Note 规范** (*高优先级*):
1.  **模板**: `templates/method_note_template.md`
2.  **聚焦**: 可执行步骤 (SOP)、模板 (Template)、检查清单 (Checklist)。
3.  **约束**:
    *   **No Vague Verbs**: 无模糊动词。
    *   **Mechanism & Leverage**: 为什么有效？
    *   **MVE**: 下一步最小可行性实验。
4.  **实战化要求（"操作手册版"而不是学术交流）**:
    *   **步骤用表格**：若工具有多步骤，每步用 `| 步骤 | What（做什么） | How（怎么做） | Why（为什么） |` 表格，清晰区分动作要点、具体操作与目的机制；禁止只用纯段落描述步骤。
    *   **卡点随步走**：每步之后嵌入「常见问题 → 即时对策」，不要把所有避坑集中到最后；末尾的避坑指南保留作为全局性反模式总结。
    *   **使用者自评清单**：除了产出验收清单（结果是否达标），再加一份「我自己做得对不对」的执行行为自检（如过程质量、判断质量、协作质量等维度，按方法论领域调整）。
    *   **准备阶段独立**：前置条件之外，需有独立的「准备阶段清单 (Pre-flight)」——开始前需确认的环境、材料、心态等事项。

### Phase 5: Final Review (终极审视)
**Agent**: Richard Feynman

用 Feynman 标准审视整个知识网络：
1.  **去魅检验**: 术语是否已"翻译"为日常语言？
2.  **比喻检验**: 复杂概念是否有恰当比喻？
3.  **逻辑检验**: 论证链是否有断裂？
4.  **拓扑检验**: 是否形成了"意外的惊喜"连接？

### Phase 6: Network Review (入网审视)
**Agent**: Niklas Luhmann

1.  **检查**: 确认每张笔记（非结构父子）至少有 2 条双向链接。
2.  **入网**: 结构笔记与原子笔记（及方法笔记）在 `03_索引/` 相关 MOC 中完成接入。**按 file-organize 的入网步骤执行**（与 file-organize 共用同一套定义）：提取关键词 → 索引候选发现 → 在选中索引中添加入口（Inbox 或关键词条目）→ 笔记底部加反链。详见 **file-organize** 的 `references/03索引实现MOC流程.md`；无需调用其他 skill。
3.  **多索引挂载检查**: 针对本索引内提到的笔记，逐条评估是否还应挂到 `03_索引/` 下**其他**索引；若某笔记也是其他主题的优质入口，则在对应索引中添加入口。输出简要清单：`[[笔记A]] → 已入 索引_X；建议补充入 索引_Y（理由）`。

### Phase 6.5: 流程执行审查（强制）

**Phase 6 完成后必须执行**。调用 **workflow-audit** skill，以德明+葛文德视角对本流程执行完成度逐项核对与系统闭环检查：

1. **审查对象**：本 skill（deep-learning）；**产出**：本次任务目录（执行计划、结构笔记、索引、原子笔记、task.md 等）。
2. **产出**：落盘审查报告（`YYYYMMDD_[任务名]_流程审查报告_德明与葛文德视角.md`），含逐项清单、系统闭环、DoD 勾选、多索引挂载清单；对审查中标为 ❌ 的项**必须补执行**，直至 DoD 全部通过。
3. **workflow-audit 主文件**：`.cursor/skills/workflow-audit/SKILL.md`；报告模板：`workflow-audit/references/audit_report_template.md`。

> 不可跳过。未通过流程执行审查并补全漏项，则本流程视为未完成。

---

## 任务追踪 (Task Tracking)

在 `task.md` 中维护进度：

```markdown
# Preparation
- [ ] Pre-game Plan Created (≥6 项 TODO + Context；对话内区块或落盘文件)

# Structure & Index
- [ ] Structure Note Created (Adler)
- [ ] Index Note Created (Luhmann)
- [ ] Index Note Onboarding (Phase 2.5): 挂载到已存在索引 + 归位到 03_索引

# Extraction Loop (Phase 3)
- [ ] [[笔记A (Concept)]] + Luhmann Scan
- [ ] [[笔记B (Concept)]] + Luhmann Scan

# Methodology (Phase 4)
- [ ] [[工具A (Method)]] (SOP/Checklist/MVE)

# Review (Phase 5 & 6)
- [ ] Feynman Check (De-jargon check)
- [ ] Network Check (2+ Links per note；入网按 file-organize 的 03索引实现MOC流程；多索引挂载检查)

# Workflow Audit (Phase 6.5，强制)
- [ ] 调用 **workflow-audit** 做流程执行审查（德明+葛文德视角），产出审查报告并对 ❌ 项补执行，直至 DoD 全部通过
```

---

## 质量验收清单 (Definition of Done)

- [ ] **Phase 0**: 执行计划已产出（≥6 项 TODO + Context）。
- [ ] **Overview**: 5个问题回答清晰，费曼测试通过。
- [ ] **Fidelity**: 有原文时案例含数字/专有名词/原话；无原文时已标注来源限制且未编造细节。
- [ ] **Actionability**: Method Note 包含无模糊词的步骤 + 可复制模板 + 实战化检查（步骤有 What/How/Why 表格、每步有卡点、有使用者自评清单、有准备阶段清单）。
- [ ] **Network**: 所有笔记双向可达 (≥2 links)；已按 file-organize 入网步骤在 03_索引 相关 MOC 中接入；本索引已挂载并位于 03_索引 下；多索引挂载检查已完成。
- [ ] **阅读顺序链**：凡出现在结构笔记「阅读顺序」中的笔记，已含「阅读顺序导航」（上一张 / 下一张），读者可不回结构笔记顺次阅读。
- [ ] **Insight**: 产生了新的连接或意外发现。
- [ ] **流程执行审查**：Phase 6.5 已执行，workflow-audit 已产出审查报告，且所有 ❌ 项已补执行、DoD 全部通过。
```

## File: `skills/deep-learning/references/expert_personas.md`
```markdown
# 专家座席方法论

> 核心原则：当有个具体的工作要做时，让 AI 模拟这个工作做得最好的人，按这个人的方法来工作。

---

## Mortimer Adler — 结构分析专家

**代表作**：《如何阅读一本书 (How to Read a Book)》

### 核心方法论
1. **分析阅读 (Analytical Reading)**：识别作者意图、论证结构、核心命题
2. **主题阅读 (Syntopical Reading)**：跨书籍比较同一主题
3. **X光透视法**：快速把握全书骨架

### 应用场景
- Phase 1：创建结构笔记时激活
- 任务：识别核心命题、论证链、阅读顺序

### 典型问题
- "作者想证明什么？"
- "他用什么证据支撑？"
- "概念之间的逻辑依赖是什么？"

---

## Richard Feynman — 解释力检验专家

**代表作**：《费曼物理讲义》、"费曼学习法"

### 核心方法论
1. **费曼技巧 (Feynman Technique)**：用外行人能听懂的话解释概念
2. **比喻优先**：复杂概念需要恰当比喻
3. **诚实面对无知**：承认不懂的地方

### 应用场景
- Phase 3：创建原子笔记时的解释标准
- Phase 4：终极审视时激活

### 典型问题
- "能不能不用术语解释这个概念？"
- "有没有一个日常生活的比喻？"
- "如果给一个 10 岁的孩子讲，他能听懂吗？"

### 费曼判决标准
- ✅ 术语被"翻译"成日常语言
- ✅ 复杂概念有恰当比喻
- ⚠️ 使用了"系统级现象"等模糊词汇 → 需要举例

---

## Niklas Luhmann — 知识连接专家

**代表作**：卡片盒方法 (Zettelkasten)、9万张卡片、50多本学术著作

### 核心方法论
1. **原子化 (Atomicity)**：一张卡片只讲一个概念
2. **连接优先 (Connection First)**：不问"属于哪类"，问"和谁对话"
3. **有机生长 (Organic Growth)**：避免过度结构化，让网络自然生长
4. **Folgezettel**：前驱 → 本位 → 后继的链式思维

### 应用场景
- Phase 2：创建索引笔记时激活
- Phase 3：执行 Luhmann Scan 时激活

### Luhmann Scan（每张笔记必做）
创建完一张笔记后，问：
1. **前置依赖**：要完全理解这张卡片，还需要哪些笔记？
2. **潜在连接**：这张卡片暗示了哪些相关概念？

发现的笔记 → 加入下一轮创建队列

### 验收标准
- 每张笔记 ≥ 2 条有意义的链接
- 所有笔记通过索引/结构笔记可达
- 网络中存在"意外的惊喜连接"

---

## 专家协作模式

| Phase | 主导专家 | 辅助专家 | 输出 |
|-------|---------|---------|------|
| 1. 结构分析 | Adler | - | 结构笔记 |
| 2. 索引设计 | Luhmann | - | 索引笔记 |
| 3. 递归生长 | Luhmann | Feynman | 原子笔记 × N |
| 4. 终极审视 | Feynman | Adler, Luhmann | 判决书 |
```

## File: `skills/deep-learning/references/luhmann_scan.md`
```markdown
# Luhmann Scan 工作流

> 这是本 skill 的核心创新：**边创建边发现**。

---

## 什么是 Luhmann Scan？

每次创建完一张原子笔记后，执行的一套标准化问答：

### 问题 1：前置依赖
> "要完全理解这张卡片，还需要哪些笔记？"

**思考方向**：
- 这张卡片引用了哪些未定义的术语？
- 这张卡片的论证基于哪些更基础的概念？
- 如果读者没读过 X，能看懂这张卡片吗？

### 问题 2：潜在连接
> "这张卡片暗示了哪些相关概念？"

**思考方向**：
- 这个概念在其他领域有没有对应物？
- 有没有"对立面"或"替代方案"？
- 这个概念的应用场景是什么？

### 问题 3：方法论发现
> "这个概念（what）被提及时，是否也交代了可执行的方法论（how）？"

**思考方向**：
- 书中是否给出了步骤、清单、模板或练习方式？
- 若有，创建立即建卡。

---

## Scan 结果处理

发现的潜在笔记按**轮次**分类：

| 轮次 | 定义 | 来源 |
|------|------|------|
| **Round 1** | 显式链接 | 结构笔记/索引笔记中直接提到的 |
| **Round 2** | 隐式依赖 | Round 1 笔记的 Scan 中发现的 |
| **Round 3** | 外围扩展 | Round 2 笔记的 Scan 中发现的 |

---

## 示例

### 输入笔记：[[快乐跑步机效应]]
创建完这张笔记后，执行 Scan：

**问题 1：前置依赖**
- 要理解"快乐跑步机"，需要知道**多巴胺**是什么 → [[多巴胺预测误差]]
- 这个效应是进化产物 → [[自然选择的错觉机制]] (已在 Round 1)

**问题 2：潜在连接**
- 这和经济学的"享乐适应"是同一回事吗？→ [[享乐适应]]
- 有没有打破跑步机的方法？→ [[多巴胺断食]]
- 佛学怎么看这件事？→ [[贪爱]]

**问题 3：方法论发现**
- 书中若给出「打破快乐跑步机」的具体练习（如多巴胺断食步骤）→ [[多巴胺断食_SOP]] (Phase 4 创建)；本例假设无，故无。

**Scan 结果**：
- Round 2: [[多巴胺预测误差]]
- Round 3: [[享乐适应]], [[多巴胺断食]], [[贪爱]]
- 方法论: 无（若有则写 `[[方法名]] (Phase 4)`）

---

## 在 task.md 中记录

每张卡一行 Scan 汇总，格式：

```markdown
- [x] **[[快乐跑步机效应]]** (Mechanism)
    - *Luhmann Scan*: 前置 → Round 2: [[多巴胺预测误差]]. 连接 → Round 3: [[享乐适应]], [[多巴胺断食]], [[贪爱]]. 方法论 → (无；若有则写 [[方法名]] Phase 4)
```

---

## 何时停止？

1. **用户明确停止**
2. **新发现的笔记已超出本书范围**（如关联到完全不同的学科）
3. **边际收益递减**：Round 3+ 的笔记对理解本书帮助有限

> 记住：目标是**理解这本书**，不是建一个百科全书。
```

## File: `skills/deep-learning/templates/atomic_note_template.md`
```markdown
---
type: Atomic_Note
tags:
  - [领域1]
  - [领域2]
links:
  - [[相关笔记A]]
  - [[相关笔记B]]
  - [[潜在笔记C]]
description: [这张笔记最值得告诉别人的一个洞察是什么？费曼会怎么向别人介绍这张笔记。100字内]
---

# [概念名称]

<!-- 仅当本笔记属于结构笔记的某「阅读顺序」时保留本节；首张无上一张、末张无下一张可写 — 或省略。不属于任何顺序则删除本节。这里的写法是固定语法，必须保留:: -->
## 阅读顺序导航
prev::[[上一张笔记]] ← 
next::[[下一张笔记]] →

## 核心概念
**[概念名称]** 是 [一句话定义]。
*   比如：[具体例子]

## 机制解析
*   **[要点1]**：[解释]
*   **[要点2]**：[解释]
*   **[要点3]**：[解释]

## 卢曼视角 (Zettelkasten Note)
这是 [[相关笔记A]] 的 [上游前提/下游应用/平行对照]。
[解释为什么它与其他笔记相连、在知识网络中的位置]

> [!NOTE] 延伸思考
> [可选：未来可探索的方向]
```

## File: `skills/deep-learning/templates/index_note_template.md`
```markdown
# 索引_[主题名]

<!-- 主题名 = 领域名（如「AI产品观与能力观」「多Agent与一人公司」），勿用书名/文章名/作者/来源/活动名；来源写在正文「来源说明」。见 file-organize/references/03索引实现MOC流程.md -->

> **类型**：Hub 索引 或 子专题索引（属 [[父索引]]）  
> **更新**：YYYY-MM-DD  
> **来源说明**：（若内容来自某书/某文，在此写来源，不放入文件名）

---

## 关键词入口 (Keywords)

### [关键词1]
- [[笔记A]] — 核心定义
- [[笔记B]] — 应用案例

### [关键词2]
- [[笔记C]] — 机制解析

### [关键词3]
...

---

## 主题结构 (Theme Structure)

> 按书籍的核心论证结构组织

### 论证一：[命题名]
→ 入口：[[结构笔记]] Sequence A

### 论证二：[命题名]
→ 入口：[[结构笔记]] Sequence B

---

## 相关结构笔记

- [[书名_结构笔记]]
```

## File: `skills/deep-learning/templates/method_note_template.md`
```markdown
---
type: Method_Note
tags:
  - [领域1]
  - [领域2]
links:
  - [[相关结构笔记]]
  - [[相关概念笔记]]
description: [这张笔记最值得告诉别人的一个洞察是什么？费曼会怎么向别人介绍这张笔记。100字内]
---

# [方法/工具名称]

## 🆔 唯一标识符
ID: [[YYYYMMDD_HH_方法名称]]
Status: SEED / DRAFT / EVERGREEN

## 🎯 目的与价值 (Purpose)
> 为什么需要这个工具？解决什么具体问题？

*   **解决痛点**：[描述]
*   **适用场景**：[描述]
*   **预期产出**：[描述]

## ⚙️ 前置条件 (Prerequisites)
> 在开始之前，必须具备什么？

*   [ ] **输入信息**：[比如：用户画像、原始数据...]
*   [ ] **资源/工具**：[比如：Excel、会议室...]
*   [ ] **人员/权限**：[比如：决策人参与...]

## 🎬 准备阶段 (Pre-flight)
> 开始执行前需确认的事项

*   [ ] **环境**：[如：安静的空间/预留足够时间/利益相关方已通知]
*   [ ] **材料**：[如：所需数据已就绪/模板已准备/工具已配置]
*   [ ] **心态/角色**：[如：明确自己在本流程中的角色与边界]

## 📝 可执行步骤 (Actionable Steps)
> ❌ 禁止模糊动词；✅ 每步用表格列出 What（做什么）/ How（怎么做）/ Why（为什么）

### Step 1: [步骤名称]

| 步骤 | What（做什么） | How（怎么做） | Why（为什么） |
|------|--------------|--------------|--------------|
| 1    | [动作要点]    | [具体操作/话术/指令] | [目的/机制] |
| 2    | [动作要点]    | [具体操作/话术/指令] | [目的/机制] |

**常见卡点**：
*   [问题描述] → [即时对策]
*   [问题描述] → [即时对策]

### Step 2: [步骤名称]

| 步骤 | What（做什么） | How（怎么做） | Why（为什么） |
|------|--------------|--------------|--------------|
| 1    | [动作要点]    | [具体操作/话术/指令] | [目的/机制] |
| 2    | [动作要点]    | [具体操作/话术/指令] | [目的/机制] |

**常见卡点**：
*   [问题描述] → [即时对策]

### Step 3: [步骤名称]

| 步骤 | What（做什么） | How（怎么做） | Why（为什么） |
|------|--------------|--------------|--------------|
| 1    | [动作要点]    | [具体操作/话术/指令] | [目的/机制] |

**常见卡点**：
*   [问题描述] → [即时对策]

## 🛠️ 交付模板 (Template)
> [在此处提供可直接复制使用的 表格 / 清单 / 提示词 / 代码块]

```markdown
(在此处粘贴模板内容)
```

## ✅ 验收清单 (Checklist)
> 如何判断做好了？(Definition of Done)

*   [ ] [检查项1]
*   [ ] [检查项2]
*   [ ] [检查项3]

## 🪞 使用者自评清单 (Self-Assessment)
> 执行后反思：我自己的执行行为是否到位？

*   [ ] **过程质量**：[如：是否按步骤执行而非跳步？每步产出是否达到预期？]
*   [ ] **判断质量**：[如：关键决策点是否有依据？是否避免了主观臆断？]
*   [ ] **协作质量**：[如：若涉及他人，沟通是否充分？是否获得了必要的输入？]

## ⚠️ 避坑指南 (Pitfalls & Anti-patterns)
> 全局性反模式总结（逐步卡点已嵌入各 Step 中）

*   **常见错误**：[描述] → **对策**：[描述]
*   **常见错误**：[描述] → **对策**：[描述]

## 🧠 机制与杠杆 (Mechanism & Leverage)
> 第一性原理视角：为什么这个方法有效？

*   **隐含假设**：[比如：假设用户是理性的...]
*   **核心机制**：[比如：利用了心理学上的互惠原理...]
*   **20/80 杠杆**：哪 20% 的动作决定了 80% 的效果？

## 🧪 下一步实验 (Next Step Experiment)
> 本周内可以执行的最小可行性实验 (MVE)

*   **实验目标**：验证 [某一步骤/效果]
*   **行动**：[具体动作]
*   **预期结果**：[数据/现象]

## 🧠 Critical Review (压力测试)
> 死对头/小白/第一性原理视角的攻击

*   **Critic**: [质疑]
*   **Response**: [回应/修正]
```

## File: `skills/deep-learning/templates/structure_note_template.md`
```markdown
---
type: Structure_Note
tags:
  - [领域1]
  - [领域2]
links:
  - [[相关索引]]
description: [这张笔记最值得告诉别人的一个洞察是什么？费曼会怎么向别人介绍这张笔记。100字内]
---

# [书名/文章名]结构笔记

> **所属索引**：[[索引_XXX]]  
> **更新**：YYYY-MM-DD
>
> **当时语境**：YYYY年M月，因 [目标] 需要，整理《[标题]》的核心论证结构。
> **默认读者**：半年后的昀峤——本结构自包含，不依赖记忆。

---

## 📋 Overview (5 Questions)
> 建立全局认知地图，防止陷入细节。

1.  **它解决什么问题？** (痛点/场景): 
2.  **核心机制是什么？** (第一性原理): 
3.  **关键概念 (3-5个)**: 
4.  **与已知方法的对比**: 
5.  **一句话总结 (费曼测试)**: 

---

## 核心命题 (Core Propositions)

> Mortimer Adler: "一本好书应该能被浓缩为几个核心命题。"

1.  **命题一**：[概括]
2.  **命题二**：[概括]
3.  **命题三**：[概括]

---

## 逻辑树 (Logic Tree)

<!--
> **Luhmann Scan 指引**：
> *   理论/概念 → 创建 **Atomic Note** ([[概念名]])
> *   工具/SOP → 创建 **Method Note** ([[方法名]])
-->

命题一（前提）
├─ [[概念笔记A]] — 证据/机制
└─ [[方法笔记B]] — 落地工具/SOP

命题二（核心论证）
├─ [[概念笔记C]] — 核心模型
└─ [[概念笔记D]] — 反驳/限定

命题三（结论/应用）
├─ [[方法笔记E]] — 解决方案
└─ [[方法笔记F]] — 实践指南

---

## 阅读顺序 (Reading Sequence)

> 每个顺序都有「理由」：半年后读到这里，仍能理解为什么下一步是它。  
> **链式导航**：本顺序中的每张笔记内须含「上一张 / 下一张」链接（见 atomic 模板「阅读顺序导航」），读者无需回到本结构笔记即可顺次阅读。

### Sequence A: [主题名]
1.  **[[笔记A]]** (Premise)
    > 理由：建立基础概念...
2.  **[[笔记B]]** (Argument)
    > 理由：核心机制解析...

### Sequence B: [主题名]
...

---

## 缺口分析 (Gap Analysis)

> 论证链中是否有跳跃？

-   [ ] Sequence A → B 之间缺少 [[潜在笔记X]]
-   [ ] [其他发现]

---

## 🏛️ 专家圆桌 (Expert Debate)
> **L3 深度辩论**：模拟 Musk (物理视角), Socrates (诘问), Munger (逆向), Feynman (解释) 对本书核心观点的辩论。

*   **Musk**: [从第一性原理/物理约束角度质疑]
*   **Socrates**: [对核心概念定义的诘问]
*   **Munger**: [反过来想，有什么潜在风险/反效应？]
*   **Feynman**: [能否用更简单的比喻解释 X？]
*   **Author (Proxy)**: [回应]

> **结论/重构**：[辩论后的共识或存疑点]

---

相关索引：[[索引_XXX]]
```

## File: `skills/index-note/SKILL.md`
```markdown
---
name: index-note
description: 索引网络与入口维护工具。Use when 建新索引、网络大修体检处方开具、单篇/批量笔记寻找网状结构归属、执行每日 05/ 每日记录笔记挂载 MOC 时。负责落实卢曼网络连接架构（包含生成修复处方与写入操作）。
---

# 索引与网络维护 (index-note)

## 定位
知识网络入口系统与结构健康专家。
**核心理念**：索引是「入口」而非「分类」——克制、精选、可达。不问“属于哪”，只问“从哪找”。
（03_索引 = MOC，用链接指向 05_每日记录里的原子笔记）

## 导航与契约（何时读什么）

| 操作模式 | 触发场景 / 核心动作 | 执行前必须 Load 的依据文档 |
| --- | --- | --- |
| **模式一：创建索引** | 为全新主题建立枢纽点 | 读 `references/index-design-concept.md` 判断边界<br>读 `references/output-templates.md` 取对应结构 |
| **模式二：网络修复** | 分析体检报告，开具网络缺陷补救处方 | 读 `references/output-templates.md` 取处方模板 |
| **模式三：内容入网** | 被动或手动为零散笔记建立网络连接 | 读 `references/入网流程.md` 执行操作判断 |
| **模式四：每日归网** | 每日一键收尾 `05_每日记录` 最新笔记集散 | 读 `references/output-templates.md` 取聚合清单方案 |

---

## 模式一：创建索引
> **强制要求**：索引用领域名命名（如 `索引_营销`），不能出现书名/文章名/作者/日期。

1. **先读概念字典**：加载 `references/index-design-concept.md` 以确定当前需求应建立的是「**概念知识索引**」还是含时间线的「**项目事件索引**」。清晰分辨出索引的主题边界。
2. **聚类与筛选入口**：搜索全库与该领域相关的卡片。梳理其内在的**关键词簇**。挑选出能真正作为入口的节点解答搜寻意图，不需要大水漫灌全部罗列。
3. **加载模板建档**：读取 `references/output-templates.md`，使用对应的索引骨架输出全新内容节点。
4. **加设回溯跳点**：确保关联到的底层卡片底部都植入了指向新索引的返回链接（双向可达）。

## 模式二：网络修复
> **输入输出**：以 `network-health` 报告为输入分析，出具体检修复可执行处方。本技能不负责重新计算总数和网络层厚数据。

1. **读取数据源**：从 `memory/network-health/` 抽取最近报告，提取：孤岛列表、高频死链、枢纽桥接笔记。
2. **甄别深水区隐患（index 层专属判断）**：
   - **检查主题真空**：搜索是否有聚成丛的笔记（近3月超5篇同概念）但在 MOC 层没有对应 `03_索引`，提议「主题缺索引」。
   - **扫除沉睡锚**：抽验底部存在 `SEED` 标签且过久未动的节点——提议激活，牵桥搭线，或让其参与下次随机漫游验证。
   - **孤岛抢救分析**：对抛出的孤岛只负责找到可归属索引或挂钩至相近节点，生搬硬套不进行。
3. **提报处方**：读取 `references/output-templates.md` 的【模式二模板】向用户列出详细的修复对策。由用户确认后进行逐一挂载打通。注：因死链通常是移动文件改变的路径，故不直接替用户操作死链。

## 模式三：内容入网（单篇/批量）
> **目标要求**：用点对点的方式将新游离知识锁在图谱里（≥2路径原则）。执行该模式的核心是将 03_文件夹当做 MOC 系统集散池用。

1. **圈定范围**：明确当次是被指派一篇文件还是一组文件，作为待入网体待办列表。
2. **研读判定规则**：加载并读一遍 `references/入网流程.md` 中对于提取主张/分类 IF-ELSE 的处理手段。
3. **落实与宣告**：实施对既有索引词条的增添，或者独立生成新的图谱双链交击。完成后，读取 `references/output-templates.md` 【模式三】区段提供的语法发送《批量入网报告》。

## 模式四：每日归网 (清理 Inbox)
> **目标要求**：日清日结的兜底动作。让今天未落点的新卡挂接回网络大动脉，防止随风遗落而“脱网”。 

1. **锁定增量**：过滤出当日创建在 `05_每日记录/YYYY/MM/YYYYMMDD` 以下所有尚未被记下 `归网：✅` 的独立文章。
2. **快速预读定性**：按优先级读取 **YAML frontmatter → 标题 → 首段**。先抽取 `tags`（候选索引主信号）和 `links`（已有连接，归网时跳过重复入网）；tags 存在时通常无需读正文即可完成判断；tags 缺失或指向不明时再读首段补充。判定：该卡属于项目范畴？知识范畴？两者兼收并蓄？还是悬而未决不强判归属？
3. **加载模板写方案**：读取 `references/output-templates.md` 并严格按【模式四今日归网方案】。将分属**同一个索引的文件合并显示**，拒绝散沙般的流水列表展示。展示修改后的挂接草图与时间线动作描述。
4. **等待确认执行**：接受用户指令后，在各卡的尾部统一注入：`← 已归网至 [[索引_XXX]]` 伴随 `归网：✅ YYYY-MM-DD` 的确认字样并在 `memory/入网/YYYYMMDD.md` 写入处理日志。
5. **Open Loops 收尾**：归网完成后，回看今日 `memory/YYYY-MM-DD.md` 日志中的所有 Open loops，逐条判断：已闭环 → 划掉；未闭环但下次自然会遇到 → 留在日志；未闭环且「如果不特地去找就会忘」→ 提升到 `memory/open loops.md`（附来源笔记链接）。闭环后从 `open loops.md` 删除，不存档。

---

## 质量与审查 CheckList（必做）

- [ ] **执行前置判断**：明确执行当前流程前，是否已经且**必须要先读取**了上方表格内规定的 `references` 外挂辅助文档？（防出现大模型的幻觉式模板操作）
- [ ] **克制精简审查**：输出与构建的索引页是否超出一屏？每一处加入的入口节点（尤其是模式四）是否都提供了该节点「一句话核心价值提要」？
- [ ] **闭环完整性**：不管任何模式执行下来，凡是被挂入索引的下方原子笔记是否不仅添加了指向关系，还加上了清晰的标签识别？
- [ ] **模式四聚合度**：每日归网方案中的同归属内容是否已经聚拢展示？无法定夺的内容是否单独设立了「待判断」，阻止了不负责的粗暴合并？

---

## 附录：批量归网自动化扩展 (资产化实现)

对于通过确认后累积的大规模未闭环归网笔记队列，可直接使用底盘提供的脚手架完成幂等闭环操作，无需模型自己逐字复写：
- **执行方法**：确保确认清单架构完好后，在终端执行：
  `python3 ".agents/skills/index-note/scripts/batch_network_integration.py"`
- 脚本会主动找到已在清单中的映射目标，自动穿透完成逆向链接填充以及结尾印章加注，已被识别过的节点将会无害略过。
```

## File: `skills/index-note/references/20260203_索引体系设计规范.md`
```markdown
# 索引体系设计规范

> 以卢曼（Niklas Luhmann）的 Zettelkasten 方法论为基础，结合现代知识管理实践的索引设计规范

---

## 核心洞察

> **索引不是分类，是入口。**

卢曼的原始系统中，Register（索引）只是「关键词 → 卡片位置」的简单映射表。他不会问「这个索引是项目类还是方法论类？」，他只问**「我想找某个东西，从哪张卡开始？」**

---

## 索引与结构笔记

> [!NOTE]
> 索引回答「从哪进」，结构笔记回答「怎么看」。本规范只涉及索引，结构笔记按需自然产生。

| 类型 | 回答的问题 | 隐喻 | 核心元素 |
|------|-----------|------|----------|
| **索引** | 我想找 X，从哪进？ | 图书馆检索卡片柜 | 关键词 → 入口 |
| **结构笔记** | 我想搞懂 X，怎么看？ | 策划好的阅读清单 | 1、2、3… 的阅读顺序 |

**结构笔记何时产生**：当你准备写文章、需要串联论证链、或向他人解释复杂话题时。

**结构笔记如何被发现**：在相关索引的「关键词」板块加一个入口。索引不区分「原子笔记」还是「结构笔记」——它只指向「最能帮你找到想要内容的那张卡」。

---

## 设计决策：多索引

卢曼物理上只有一个索引文件，但里面有成百上千个词条。现代数字系统中，我们选择**按主题领域拆分成多个索引文件**，每个索引内部仍是「词→入口」结构。

**约束**：
- 索引数量克制（不超过 10-15 个）
- 每个索引对应一个「查找意图」
- 索引之间通过底部链接互联

---

## 设计原则

### 原则一：索引按「稳定性」区分

| 稳定性 | 俗称 | 特征 | 增长方式 | 例子 |
|--------|------|------|----------|------|
| **高（Hub）** | 方法论索引 | 领域持续积累 | 长期迭代，入口相对固定 | 产品方法论、AI时代观察 |
| **中（Structure）** | 项目索引 | 项目生命周期 | 项目周期内活跃，结束后归档 | 601项目、家庭机器人研究 |

> [!NOTE]
> Hub ≈ 方法论索引，Structure ≈ 项目索引。这两套术语可以互换使用，本质是「稳定性」的区别。

---

### 索引生命周期

| 状态 | 条件 | 处理方式 |
|------|------|----------|
| **活跃** | 近 30 天有更新 | 正常维护 |
| **休眠** | 超过 90 天无更新 | 检查是否合并到 Hub |
| **归档** | 项目结束 | 结构笔记标记归档，保留只读 |

---

### 原则二：自下而上演化（核心！）

> **索引不是预先规划的，是有机生长出来的。**

**两条入口路径**：

```
┌─────────────┐                      ┌─────────────┐
│ 项目资料    │                      │ 文献笔记    │
│（工作产出） │                      │（外部输入） │
└──────┬──────┘                      └──────┬──────┘
       ▼                                    │
┌─────────────────┐                         │
│ 项目索引        │ ← 路径A：先入项目索引    │
│（Structure）    │                         │
└────────┬────────┘                         │
         │ 关键词重复出现时向上抽象          │
         ▼                                  ▼
┌─────────────────────────────────────────────┐
│              方法论索引（Hub）               │ ← 路径B：直接入方法论索引
│         汇总各项目应用 + 方法论本身          │
└─────────────────────────────────────────────┘
```

| 输入类型 | 路径 | 说明 |
|---------|------|------|
| **项目资料**（工作产出、会议纪要、项目分析） | 项目索引 → 方法论索引 | 先入项目，关键词重复时向上抽象 |
| **文献笔记**（书、文章、论文、播客） | 直接入方法论索引 | 本身就是方法论/知识的载体 |

> [!CAUTION]
> **禁止预设空索引**。不要先规划「应该有哪些方法论索引」，让它从输入中自然涌现。

---

### 原则三：同一关键词可出现在多个索引

以 **JTBD** 为例：

| 索引 | 关键词指向 | 服务的查找意图 |
|------|-----------|---------------|
| `索引_601项目.md` | 601 项目的 JTBD 应用笔记 | 「我在做601项目，用户JTBD是什么？」 |
| `索引_家庭机器人用户研究.md` | Aether 的 JTBD 分析笔记 | 「我在做机器人，用户JTBD是什么？」 |
| `索引_产品方法论.md` | JTBD 方法论本身 + 各项目应用汇总 | 「JTBD是什么方法？有哪些实战案例？」 |

> [!TIP]
> 这不是冗余——这是「**多入口可达**」，卢曼系统的核心设计！

---

### 原则四：方法论索引增加「跨项目应用」板块

当一个方法在多个项目中被使用时，方法论索引应该汇总各项目的应用实例：

```markdown
## 方法论应用案例（跨项目）

| 项目 | 应用笔记 | 核心洞察 |
|-----|---------|---------|
| 家庭机器人 | [[xxx_JTBD分析]] | P0=远程安心 |
| 601项目 | [[xxx_JTBD分析]] | [待填] |
```

这样，从方法论索引进入时，可以看到该方法在不同项目中的应用对比，形成**跨项目的知识复用**。

---

### 原则五：索引之间的关系

```
          ┌─────────────────┐
          │ 索引_产品方法论  │ ← Hub（方法论入口）
          │  (JTBD, 定价...)│
          └────────┬────────┘
                   │ "应用案例"指向
         ┌─────────┴─────────┐
         ▼                   ▼
┌────────────────┐  ┌────────────────────┐
│ 索引_601项目   │  │ 索引_家庭机器人研究 │ ← Structure（项目入口）
│  (JTBD_601...)│  │  (JTBD_机器人...)   │
└────────────────┘  └────────────────────┘
         │                   │
         └─────────┬─────────┘
                   │ "相关索引"互指
                   ▼
          ┌─────────────────┐
          │ 索引_AI时代观察  │ ← Hub（趋势入口）
          └─────────────────┘
```

**核心逻辑**：
- **索引笔记**（产品方法论、AI时代）= 领域顶层入口，持续积累
- **结构笔记**（601、机器人研究）= 项目入口，生命周期有限
- **索引笔记的「应用案例」板块** 指向各结构笔记的具体笔记

---

### 原则六：命名规范

统一格式：`索引_[主题名].md`（子专题为 `索引_<主题>_<领域>.md`）。具体格式、禁止项与示例见 **index-note** `references/索引笔记命名速查.md`。

---

## 索引模板

```markdown
# 索引_[主题名]

> **类型**：索引笔记 / 结构笔记  
> **创建**：YYYY-MM-DD | **更新**：YYYY-MM-DD

---

## 关键词

**[词1]** → [[笔记A]]
**[词2]** → [[笔记B]]

---

## 主题结构（可选阅读）

### [子主题1]
- [[笔记C]] — 简短说明
- [[笔记D]] — 简短说明

### [子主题2]
- [[笔记E]] — 简短说明

---

## 方法论应用案例（仅 Hub 类索引需要）

| 项目 | 应用笔记 | 核心洞察 |
|-----|---------|---------|
| [项目1] | [[笔记F]] | [洞察] |
| [项目2] | [[笔记G]] | [洞察] |

---

相关索引：[[索引_xxx]] · [[索引_yyy]]
```

---

## 连接

- [[索引笔记vs结构笔记的区别]] — 概念澄清
- [[DDC杜威十进制分类在Zettelkasten中的应用]] — 目录结构规范

---

创建：2026-02-03 | 作者：昀峤 + AI分身
```

## File: `skills/index-note/references/index-design-concept.md`
```markdown
# 索引系统设计规范字典

> **用 03_索引 实现 MOC 的流程**（笔记在 05、何时入网到 03）见 **file-organize** 的 `references/03索引实现MOC流程.md`。

## 索引 vs 结构笔记

| 类型 | 回答的问题 | 隐喻 | 核心元素 |
|------|-----------|------|----------|
| **索引** | 我想找 X，从哪进？ | 图书馆检索卡片柜 | 关键词 → 入口 |
| **结构笔记** | 我想搞懂 X，怎么看？ | 策划好的阅读清单 | 1、2、3… 的阅读顺序 |

**结构笔记何时产生**：准备写文章、串联论证链、或向他人解释复杂话题时 → 请用 `structure-note` skill。
**结构笔记如何被发现**：在相关索引的「关键词」板块加一个入口。

## 多索引设计约束

- 索引数量克制（**不超过 10-15 个**）
- 每个索引对应一个「查找意图」
- 索引之间通过底部链接互联
- **命名规范**：`索引_[主题名].md` 或子专题 `索引_<主题>_<领域>.md`；**主题/领域 = 知识领域**，不是书名/文章名/作者/来源/活动名。格式与禁止项速查见 `references/索引笔记命名速查.md`。

### 激进设计：不强调「索引入口」层

- **默认只有一层索引（Hub）**，内含「查找词 → 最佳入口」表。
- **词多时**：在表内按词簇**分块/分节**（例如「## 合规与履约」），而不新增「索引入口」这类文档。
- **克制原则**：索引保持一屏能看完；每个查找词链接的笔记数量由内容决定——能真正回答这个意图的都可列入，但避免堆砌。

### 层级用链接表达，不用文件夹嵌套

父索引通过链接指向子域索引，子域索引再指向具体笔记——层级活在链接里，不活在文件夹里。

**为什么不用文件夹**：一张笔记可以同时被多个子域索引指向。文件夹只用于**命名空间隔离**。
**子域索引何时新建**：当某个领域的查找词超出 10-15 个、父索引一屏放不下时，才拆出独立子域索引，并在父项加入口。

## 概念索引 vs 项目索引

| | 概念索引 | 项目索引 |
|---|---|---|
| 例子 | 索引_产品方法论 | 索引_Lockin、索引_OpenClaw |
| 核心问题 | 这个概念/方法论是什么？ | 这个对象怎么演变的？ |
| 时效性 | 无，知识常青 | 有，记录决策历史 |
| 核心区块 | 关键词 + 主题结构 | 关键词 + 主题结构 + **📅 时间线** |
| frontmatter | `类型：概念索引` | `类型：项目索引` |

**时间线区块的讨论类型标签**（项目索引专用）：
`决策` / `方向调整` / `问题暴露` / `执行`

### 如何判断是项目还是知识索引

1. **有没有明确的对象？**（具体的产品、项目、人物序列等）→ 有则是候选项目索引。
2. **"时间顺序"重要吗？**（会想知道不同季度的对比吗？）→ 会则是项目索引。
3. **能被多个不同项目复用吗？**（概念边界）→ 能同时应用于多项目则是知识索引，否则项目索引。

> 同一张笔记可以同时挂两种索引——既在项目时间轴，也作为方法论实战。这不是冗余，而是「**多入口可达**」。

## 索引生命周期

| 状态 | 条件 | 处理方式 |
|------|------|----------|
| **活跃** | 近 30 天有更新 | 正常维护 |
| **休眠** | 超过 90 天无更新 | 检查是否合并到 Hub |
| **归档** | 项目结束 | 结构笔记标记归档，保留只读 |

## 两条入口路径演化

1. **项目资料**（工作产出、纪要）→ 先入项目索引；当该抽象解决重复问题时，提炼归入知识索引。
2. **文献笔记**（阅读、文章）→ 直接入知识索引，因为它本身就是方法论/领域知识载体。

## 索引间关系

- **索引笔记** = 领域顶层入口，持续积累
- **结构笔记** = 项目入口，生命周期有限
- **索引笔记的「应用案例」板块** 指向结构笔记内的具体卡片
- **结构笔记之间** 通过「相关索引」互指
```

## File: `skills/index-note/references/output-templates.md`
```markdown
# 索引网络与输出模板集

## 【模式一：骨架参考】概念知识索引模板

```markdown
# 索引_产品方法论

> **类型**：概念索引
> **创建**：2025-09-01 | **更新**：{{YYYY-MM-DD}}

---

## 关键词

### 用户洞察
**[如何定义用户真实需求]** → [[20250726_JTBD2.0学习总结与实践指南]] — Jobs-to-be-Done，需求不是功能而是进展
**[如何做用户分层]** → [[20250623_横向端到端表价格段分析_知识卡片]] — 价格段 × 用户心智矩阵

### 竞争与市场
**[如何判断市场机会]** → [[20251223_海外新市场操盘方法论]] — 市场扫描 → 机会域 → 组织匹配

---

## 主题结构

### 原理层（方法论本体）
- [[20250726_JTBD2.0学习总结与实践指南]] — JTBD 完整理论框架

### 应用案例层（实战）
- [[20251223_海外新市场操盘方法论]] — Lockin 北美新市场落地过程

### 批评与边界（什么时候不适用）
- [[20251221_用户心智与技术信仰的平衡_产品创新的哲学选择]] — 何时顺从用户、何时坚持技术判断

---

## 跨项目应用汇总

| 项目 | 应用笔记 | 核心洞察 |
|-----|---------|---------|
| Lockin 北美 | [[20251008_Lockin北美战略屋]] | 五看三定落地于门锁品类 |

---

相关索引：[[索引_营销]] · [[索引_第二曲线]] · [[索引_Lockin]]
\```

## 【模式一：骨架参考】项目追踪索引模板（包含时间线）

```markdown
# 索引_V7Max

> **类型**：项目索引
> **创建**：2026-01-10 | **更新**：{{YYYY-MM-DD}}

---

## 📅 时间线

### 2025-Q4
- [[20251010_Lockin四大核心技术战略价值与GTM全案]] · 决策 — 确定掌静脉为差异化技术核心
- [[20251119_Lockin产品价值分析]] · 问题暴露 — 功能层讲述过重，情感牵引不足

### 2026-Q1
- [[20260309_V7Max产品评审]] · 问题暴露 — 掌静脉模组功耗超标，需重新选型
- [[20260309_V7Max选型决策会]] · 决策 — 锁定新供应商，Q2 重新打样

---

## 关键词

**[掌静脉技术]** → [[20251010_Lockin四大核心技术战略价值与GTM全案]]
**[功耗选型]** → [[20260309_V7Max产品评审]]

---

## 主题结构

### 产品定义
- [[20251010_Lockin四大核心技术战略价值与GTM全案]] — 技术选型与差异化叙事

### 营销与 GTM
- [[20251105_Lockin掌脉锁AIPL广告素材规划]] — AIPL 漏斗素材规划

---

相关索引：[[索引_Lockin]] · [[索引_产品方法论]]
\```

---

## 【模式二】网络修复体检处方模板

```markdown
## 🔧 网络修复处方 [YYYY-MM-DD]
> 数据来源：memory/network-health/YYYY-MM-DD.md

### ① 主题缺索引（需新建）
- 「掌静脉技术」：相关笔记 7 篇（[[笔记A]]、[[笔记B]]…），建议新建 `索引_掌静脉技术`（项目索引）

### ② SEED 笔记激活
- [[20260220_小红书_永不失忆记忆系统]]（沉睡 17 天）→ 建议挂入 [[索引_记忆与记忆系统]]

### ③ 孤岛归属
- [[面部识别展示墙]] → 归入 [[索引_Lockin]]（产品展示物料）
- [[龙虾生态观察V3]] → 无法归属，标记「待判断」
\```

---

## 【模式三】内容入网模板（单篇与批量追加入口格式）

写入到目标笔记末点与对应的索引区：

```markdown
- **新增关键词**：
  `**[New_Concept]** → [[New_Note]] — [一句话核心价值]`

- **追加视角到现有词**：
  `**[Existing_Concept]** → [[Old_Note]], [[New_Note]] (补充视角)`
\```

针对批量入网后的综合汇报模板：

```markdown
## 批量入网报告

**处理范围**：[目录/文件列表]
**处理数量**：X 个文档

### 入网结果
| 文档 | 入网方式 | 关联索引/笔记 |
|------|---------|--------------|
| [[文档A]] | 追加入口 | 索引_xxx |
| [[文档B]] | 双向链接 | [[笔记C]] |
| [[文档C]] | 新建索引 | 索引_新领域 |

### 新建索引
- [[索引_xxx]] — 理由

### 需人工确认
- [[文档D]] — 无法判断归属，建议 [选项]
\```

---

## 【模式四】今日归网聚合方案模板
注意：同一索引内归结在一起，杜绝零散的流水账罗列：

```markdown
## 📋 今日归网方案 [YYYY-MM-DD]
共扫描 X 篇笔记，提议归网 Y 篇，待判断 Z 篇。

---

### 写入 [[索引_Lockin]]（项目索引）

**时间线追加**（YYYY-MM 或 YYYY-QN）：
- [[20260309_V7Max产品评审]] · 问题暴露 — 掌静脉模组功耗超标，需重新选型

**关键词追加**：
- `[掌静脉功耗]` → [[20260309_V7Max产品评审]]

---

### 写入 [[索引_产品方法论]]（知识索引）

**关键词追加**：
- `[硬件选型决策]` → [[20260309_V7Max产品评审]] — 功耗 vs 体验的取舍框架

**应用案例追加**：
- [[20260309_V7Max产品评审]] — Lockin V7Max 项目中功耗平衡案例

---

### ⚠️ 待判断（无法归属，需人工决定）
- [[20260309_随想_AI与组织]] — 建议：归入 [[索引_AI时代观察]]？或新建知识索引？

---
请确认后我执行写入，并在对应笔记底部追加反向链接。
\```
```

## File: `skills/index-note/references/入网流程.md`
```markdown
# 知识网络入网流程

> 本文件定义从「一篇笔记」到「入网完成」的通用处理逻辑。
> 被 SKILL.md 的模式一、模式三引用。

---

## 流程总览

```
笔记 → 提取关键词 → 索引候选发现 → 判断入网方式 → 确保双向可达 → 递归发现
```

---

## Step 1: 提取关键词

阅读文档内容，结合文档的 **What / How / Why**，提取 3-5 个核心关键词。

**思维方式**：用第一性原理分析——
- 这篇笔记的核心概念是什么？
- 未来我会用什么词来找它？
- 它和哪些已有概念在对话？

---

## Step 1.5: 索引候选发现（语义共振搜索）

> **核心原则**：不问"它属于哪个分类"，问"它和哪些索引在对话"。

对每个关键词执行以下流程：

### 1. 全索引扫描
- 遍历 `03_索引/` 下的所有索引文件
- 读取每个索引的"关键词"区域

### 2. 语义相关度判断
对每个索引，判断关键词是否与该索引**语义相关**：

| 判断维度 | 示例 |
|---------|------|
| **直接匹配** | 关键词"JTBD"在索引中已出现 |
| **概念从属** | 关键词"决策疲劳"属于"认知偏差"领域 |
| **应用场景** | 关键词"JTBD"在"产品方法论"中是工具 |
| **跨域关联** | 关键词"决策疲劳"影响"用户体验"设计 |

### 3. 生成候选列表（可能是多个）

**输出格式**：
```
关键词"[X]"的候选索引：
□ 索引_A.md（因为：[一句话说明相关性]）
□ 索引_B.md（因为：[一句话说明相关性]）
□ 索引_C.md（因为：[一句话说明相关性]）
```

### 4. 多索引入口设计（卢曼核心）

> **重要**：同一关键词可以进入**多个索引**，这不是冗余，而是"多入口可达"。

**示例**：关键词"JTBD"
- `索引_产品方法论.md` → JTBD方法论本身
- `索引_601项目.md` → 601项目的JTBD应用
- `索引_家庭机器人研究.md` → Aether的JTBD分析

每个索引中的**描述可以不同**（体现该索引的视角）。

---

## Step 2: 判断入网方式（基于候选列表）

**前置条件**：已通过 Step 1.5 生成候选索引列表。

### 执行逻辑（半自动）

```
FOR 每个关键词:
  IF Step 1.5 生成的候选列表为空:
    → 这是新领域，调用 index-note skill 创建新索引
  
  ELSE IF 候选列表有1个索引:
    → 自动执行插入（见"插入规则"）
  
  ELSE（候选列表有多个索引）:
    → 展示候选列表，等待用户确认选择
    → 对每个用户选中的索引，执行插入（见"插入规则"）
```

### 插入规则

对每个目标索引：

```
IF 关键词已在该索引中:
  IF 新笔记能独立回答这个关键词（提供不同视角或独立价值）:
    → 在索引中该关键词后追加新笔记作为入口
    格式: **[关键词]** → [[旧笔记]], [[新笔记]] (补充视角)
  
  ELSE（新笔记是已有笔记的补充/扩展/案例）:
    → 在新笔记与该关键词原指向笔记之间建立双向链接
    → 不修改索引（避免索引臃肿）

ELSE（关键词不在该索引中）:
  → 在索引中添加新关键词 + 新笔记
  格式: **[新关键词]** → [[新笔记]] — [一句话核心价值]
  → 定位：找到索引中最相关的"分节"（如果有分节的话）
```

### 批量写入示例

**场景**：关键词"决策疲劳"被用户选择插入3个索引

**执行**：
1. 在 `索引_认知偏差.md` 中添加：
   ```markdown
   **决策疲劳** → [[20260210_决策疲劳]] — 长时间决策导致的认知资源耗竭
   ```

2. 在 `索引_用户体验.md` 中添加：
   ```markdown
   **决策疲劳** → [[20260210_决策疲劳]] — 过多选择导致的用户流失
   ```

3. 在 `索引_管理工具.md` 中添加：
   ```markdown
   **决策疲劳** → [[20260210_决策疲劳]] — SOP设计减少团队决策负荷
   ```

4. 在 `20260210_决策疲劳.md` 底部添加反向链接：
   ```markdown
   相关索引：[[索引_认知偏差]] · [[索引_用户体验]] · [[索引_管理工具]]
   ```

---

## Step 3: 确保双向可达

**验收标准**：新笔记至少有 ≥2 条双向可达路径

**操作清单**：
1. **笔记 → 索引/相关笔记**：在笔记底部添加反向链接
2. **索引/相关笔记 → 笔记**：在索引或相关笔记中添加入口

---

## Step 3.5: 递归发现（Luhmann Scan）

> **核心理念**：入网不是终点，而是新一轮发现的起点。

对刚入网的笔记执行**两个核心问题**（借鉴 `book-reading` skill 的 Luhmann Scan）：

### 1. 前置依赖检查

**问题**：要完全理解这张笔记，读者还需要哪些笔记？

**执行**：
- 扫描笔记中提到但未链接的概念
- 判断这些概念是否已有笔记
- 如缺失，加入"待创建笔记清单"（Round 2 队列）

**示例**：
```
笔记：[[决策疲劳与用户流失]]
前置依赖检查：
- 提到"认知资源耗竭" → 检查是否有 [[认知资源理论]]
- 提到"选择悖论" → 检查是否有 [[选择过载效应]]
→ 如缺失，加入待创建清单
```

### 2. 潜在连接发现

**问题**：这张笔记暗示了哪些跨域概念？

**执行**：
- **跨域扫描**：扫描非直接相关的索引，寻找"意外关联"
- **类比思维**：问"这个模式在其他领域是否也存在？"
- **记录候选**：即使暂不建立链接，也记录在笔记中（未来可能激活）

**示例**：
```
笔记：[[决策疲劳与用户流失]]（在 索引_用户体验 中）
潜在连接发现：
- 跨域到 [[索引_系统设计]]：容错机制是否也在"减少决策负荷"？
- 跨域到 [[索引_管理工具]]：SOP设计是否是"决策疲劳"的组织层面解法？
→ 记录在笔记的"意外发现区"
```

### 输出格式

在笔记底部增加：

```markdown
## 🔄 递归发现（Luhmann Scan）

### 前置依赖（Round 2 队列）
- [ ] [[概念A]] — 需要补充的前置知识
- [ ] [[概念B]] — 读者可能不理解的术语

### 潜在连接（意外关联候选）
- **跨域到 [[索引_X]]**：[一句话说明为什么可能相关]
- **类比思维**：[这个模式在哪些领域也存在？]
```

---

## 质量检查

- [ ] 提取了 3-5 个核心关键词
- [ ] **索引候选发现**：每个关键词都执行了全索引扫描
- [ ] **语义相关性**：候选列表中的索引都给出了相关性理由
- [ ] **多索引入口**：如有多个候选，已展示给用户确认
- [ ] **批量写入**：所有选中的索引都已更新
- [ ] 新笔记至少有 2 条双向可达路径
- [ ] 反向链接已添加（笔记底部链接到所有相关索引）
- [ ] **递归发现（Luhmann Scan）**：已执行前置依赖检查和潜在连接发现
- [ ] **意外连接**：至少尝试发现 1 个跨域连接候选
- [ ] **扩展队列**：记录了"暂未入网但未来可能相关"的概念（Round 2 队列）
```

## File: `skills/index-note/references/索引笔记命名速查.md`
```markdown
# 索引笔记命名速查

> 索引文件名 = **知识领域**，不是来源/日期/文章名。来源写在正文「来源说明」。

## 正确格式

| 类型 | 格式 | 示例 |
|------|------|------|
| 顶级索引 | `索引_<主题>.md` | `索引_OpenClaw.md`、`索引_个人发展.md` |
| 子专题索引 | `索引_<主题>_<领域>.md` | `索引_OpenClaw_人格与配置.md`、`索引_AI时代观察_组织变革与AI提效.md` |

**主题/领域** = 从内容提炼的**知识领域**（如「CTO角色与董事会沟通」「DMN与认知架构」），不是某本书/某篇文章/某次活动的名字。

## 禁止出现在索引文件名中

- ❌ 日期/批次：`20260222`、`20260223`
- ❌ 文章/来源名：`CTO七问`、`笔记侠`、`TechVision`
- ❌ 活动/书名：`XXX访谈`、`YYY书`
- ❌ 后缀「索引笔记」：用 `索引_领域名.md` 即可，不必写「_索引笔记」

## 创建索引时的自检

1. **先定领域名**：这张索引将来别人会用什么**查找意图**找到？→ 用那个意图对应的领域命名。
2. **来源放正文**：在索引正文顶部写「> 来源：公众号/书/方案名 | 日期」。
3. **结构笔记可带原文**：结构笔记可以用原文标题（如 `20260222_00_CTO七问_结构笔记`），但**索引**必须按领域命名。

## 本次修正示例

| 原文件名（错误） | 新文件名（正确） |
|------------------|------------------|
| `20260222_02_CTO七问_索引笔记.md` | `索引_CTO角色与董事会沟通.md` |
| `20260223_02_DMN_索引笔记.md` | `索引_DMN与认知架构.md` |

**在体系中的位置**：本文件是《20260203_索引体系设计规范》原则六（命名规范）的操作展开。完整层级与入网见 `03索引实现MOC流程.md`（file-organize 内）、index-note SKILL.md 模式一 Step 1。
```

## File: `skills/link-proposer/SKILL.md`
```markdown
---
name: link-proposer
description: 为新笔记提议链接候选（三路搜索）、关键词建议与 Gegenrede 反问。适用于写完新笔记后需要建立连接，或用户说「帮我找连接/链接提议/建议关键词/反问/Gegenrede」时调用。关键词：link-proposer、链接提议、关键词建议、反问、连接候选、Verweise、Gegenrede。
---

# Link Proposer（Verweise-Agent）

> 以卢曼的视角：重要的是在工作中捕捉放射状的连接——同时也立即在被链接的卡片上记录反向链接。

**输入**：新笔记的路径
**输出**：链接候选 + 关键词建议 + Gegenrede 反问
**铁律**：Agent 只建议，人确认后才写入

---

## 工作流

### Step 1：读笔记，提炼核心

读取目标笔记，识别：
- **核心概念**（1-3 个）
- **主要主张**（1 句话）
- **学科领域**（用于 Step 4 的跨域反问）

### Step 1.5：提取已有链接（预过滤）

读取目标笔记正文中所有 `[[...]]` 形式的链接，记为**已有链接集合 E**。
三路搜索完成后，凡命中笔记已在 E 中的：
- **过滤掉**，不计入 3-5 条候选限额
- 若该笔记确实重要，可单独列为「建议强化描述」（不占候选名额）：说明当前链接的关系描述是否需要更新

### Step 2：三路搜索（并行执行）

#### 路径 A · 语义相近
1. 从笔记提取 3-5 个关键词/短语（选最具辨识度的，避免通用词）
2. 用这些关键词 grep `05_每日记录/`（`-r -l`，返回文件路径）
3. 读命中文件的标题行或首段，挑出 **2-3 条最相关**的

#### 路径 B · 时间邻近
1. 从笔记路径提取日期（`YYYY/MM/YYYYMMDD`）
2. 列出同一周（±3 天）内的其他笔记文件
3. 排除当前笔记；排除已在路径 A 命中的笔记；挑 **1-2 条**（有同一思考线索的优先）
4. **去重原则**：若某笔记同时命中 A 路和 B 路，合并到 A 路（备注"时间亦邻近"），B 路候选必须是 A 路未收录的笔记

#### 路径 C · 反相关 ⚡（惊讶的来源 · 真偶遇）

**铁律**：先随机抽样，再判断张力——不能先想「哪张可能有张力」再挑，否则不是偶遇。

1. **执行随机抽取脚本**：执行本技能自带的脚本 `scripts/get_random_notes.sh --mode tension --count 6`，直接获取 6 张随机抽样的笔记路径。
2. **判断张力**：逐一读取这几张笔记的标题或首段，并与当前笔记对比，问：「这张和当前笔记之间有没有张力、对立、或意外的桥梁？」
3. 找到张力 → 纳入候选；若 6 张都无发现 → 记录「无发现」并说明，可再次运行脚本重新抽取。

**总候选数**：3-5 条，其中**至少 1 条来自路径 C**。如果路径 C 无发现，扩大采样范围重试一次。

### Step 3：关键词建议

思考：「昀峤将来会从哪个问题想到这张笔记？」
建议 1-3 个关键词，标注应添加到 `03_索引/00_索引_关键词总表.md` 的哪个词条下（新词条或已有词条）。

### Step 4：Gegenrede（反问）

1. 确认笔记的核心主张
2. 选择一个**完全不同**的学科视角：
   - 笔记讲商业策略 → 用生物进化论视角
   - 笔记讲技术架构 → 用组织理论视角
   - 笔记讲心理学 → 用经济学/博弈论视角
   - 笔记讲产品设计 → 用人类学视角
3. 从该视角提出一个质疑或反问（简短，1-2 句）

**反问不写入笔记正文**，只出现在回复中。昀峤觉得有启发时，可另起一张回应笔记。

---

## 输出格式

```markdown
## 🔗 链接候选

**A · 语义相近**
1. [[笔记名]] — 理由：[具体说明]
2. [[笔记名]] — 理由：[具体说明]

**B · 时间邻近**
3. [[笔记名]] — 理由：[同一思考线索]

**⚡ C · 反相关**
4. [[笔记名]] — 张力：[你在这里说X，那里说Y，可能有对话空间]

---
请确认接受哪些链接，我再写入双向链接。

## 🏷️ 关键词建议
- `词条A` → 建议添加到 [[00_索引_关键词总表]] 的「X」词条下，指向此笔记
- `词条B` → 建议新建词条「Y」

## 💬 Gegenrede
你说 [X]，但从 [Y 视角] 来看，[Z 质疑]？
```

---

## 质量检查

- [ ] 三路都已执行（A/B/C），总候选 3-5 条
- [ ] 至少 1 条 ⚡ 反相关（路径 C）
- [ ] 每条候选都有具体理由（不能只写"可能相关"）
- [ ] 关键词建议标注了总表词条位置（新增或已有）
- [ ] 反问使用了与笔记**不同学科**的视角
- [ ] **未替人写入任何链接**（铁律：人确认后才执行）
```

## File: `skills/link-proposer/scripts/get_random_notes.sh`
```bash
#!/bin/bash
# get_random_notes.sh — ZK Steward companion (link-proposer path C).
# Usage: ./get_random_notes.sh --mode <mode> [--count <count>]
# Optional env: NOTES_DIR (default 05_每日记录), INDEX_DIR (default 03_索引), EXTRA_DIR (default longlongago).

NOTES_DIR="${NOTES_DIR:-05_每日记录}"
INDEX_DIR="${INDEX_DIR:-03_索引}"
EXTRA_DIR="${EXTRA_DIR:-longlongago}"

MODE=""
COUNT=1

while [[ "$#" -gt 0 ]]; do
    case $1 in
        --mode) MODE="$2"; shift ;;
        --count) COUNT="$2"; shift ;;
        *) echo "Unknown parameter passed: $1"; exit 1 ;;
    esac
    shift
done

if [[ -z "$MODE" ]]; then
    echo "Error: --mode is required."
    exit 1
fi

case "$MODE" in
    tension)
        SEED=$(date +%s)
        find "$NOTES_DIR" "$EXTRA_DIR" -name "*.md" -type f 2>/dev/null | \
            awk -v seed=$SEED 'BEGIN{srand(seed)} {print rand() "\t" $0}' | \
            sort -n | cut -f2- | head -n "$COUNT"
        ;;
    forgotten)
        find "$NOTES_DIR" "$EXTRA_DIR" -type f -name "*.md" -mtime +90 2>/dev/null | while read -r file; do
            basename=$(basename "$file" .md)
            link_count=$(grep -rc "\[\[$basename\]\]" "$NOTES_DIR" "$INDEX_DIR" 2>/dev/null | awk -F: '{sum+=$2} END{print sum+0}')
            if [ "$link_count" -le 1 ]; then
                echo "$file"
            fi
        done | head -n 50 | sort -R | head -n "$COUNT"
        ;;
    recent)
        find "$NOTES_DIR" -type f -name "*.md" -mtime -7 2>/dev/null | sort -R | head -n "$COUNT"
        ;;
    *)
        echo "Error: Unknown mode '$MODE'. Supported modes: tension, forgotten, recent."
        exit 1
        ;;
esac
```

## File: `skills/random-walk/SKILL.md`
```markdown
---
name: random-walk
description: 随机漫游知识网络并制造偶遇。Use when 用户说“随机漫游/随便逛逛/给我点意外连接/打破惯性”。
---

# 随机漫游

> **Persona（防讨好约束）**: 你是一个苛刻的知识拓扑学家与勘探者。你的任务不是像普通的 “Helpful Assistant” 那样去讨好用户、强行把毫不相干的主题凑在一起；相反，你应该敏锐地指出概念深处的断层。当两张卡片像水和油一样完全无法融合时，必须直接大声报告【无张力，强行连接会破坏系统】。拒绝生搬硬套是你的天职。真正的惊讶源于断裂处，而非强行拟合。

> 卢曼每天随机抽取卡片，与过去的自己对话——不是目的性搜索，而是制造偶遇。

## 快速开始
- 明确本次漫游的 **mode**（random/theme/time/cross）与 **count**（建议 3-5）。
- 抽取后对每张笔记回答“连接三问”，输出 **可执行的双向链接修改建议**。

---

## 输入参数

| 参数 | 默认值 | 说明 |
|------|--------|------|
| `mode` | random | `random` 随机（含孤岛混入）/ `theme` 主题过滤 / `time` 时间过滤 / `cross` 跨域 / **`tension`** 张力对撞 / **`forgotten`** 遗忘打捞 / **`island`** 孤岛专注 |
| `count` | 5 | random 默认 5（3 日常 + 2 孤岛）；`tension`/`forgotten`/`island` 建议 2-3 |
| `filter` | - | 主题关键词或时间范围（如 `202401`）|

---

## 工作流

### Step 1: 智能抽取
使用文件名/路径匹配从以下目录获取笔记列表（优先用项目内文件搜索能力）：
- `05_每日记录/`（主笔记目录）
- `CEO思考/`（历史 DMN 产出，仍有漫游价值）
- `longlongago/01_永久笔记/`（历史归档）
- `longlongago/02_文献笔记/`（历史归档）

**常规抽取策略（random/theme/time/cross）**：
- **random**: 从 `05_每日记录/` 随机抽 3 张（对旧笔记略微加权）+ 从最新 network-health 报告的 🏝️ 孤岛列表随机抽 2 张，共 5 张混合漫游。若 `memory/network-health/` 无报告或孤岛列表为空，则全部从 `05_每日记录/` 抽取。
- **theme**: 按关键词过滤后随机选择
- **time**: 按文件名日期前缀过滤
- **cross**: 强制从不同杜威分类各抽1张

**高攻击性抽取策略（tension/forgotten/island）**：
- **tension**: 执行 `scripts/get_random_notes.sh --mode tension --count 6`，两两配对（3对），读标题/首段，选出**语义距离最大**的那一对作为"张力对"，尝试寻找它们之间意外的相互作用或对立。
- **forgotten**: 执行 `scripts/get_random_notes.sh --mode forgotten --count 2`，提取旧笔记。然后与**最近 7 天内写的笔记**（可结合当前思路，或执行 `scripts/get_random_notes.sh --mode recent --count 5`）进行对比强制碰撞，寻找可能被忽略的价值。
- **island**: 专注模式——只从孤岛列表抽取，不混入其他笔记。适合集中清理孤岛时使用。与 index-note 模式二的区别：模式二判断「该挂哪个索引」，island 模式找「内容层面真正共鸣的笔记」。

### Step 2: 深度阅读

**常规模式（random/theme/time/cross）**完成连接三问：
1. 和我**当前项目/问题**有什么联系？
2. 和我**最近学的东西**有什么呼应？
3. 让我想到了**什么新问题**？

**Tension 模式**回答：
在最终输出前，必须先生成 `<thinking>` 内部流转过程：分析 A 的第一性原理 → 分析 B 的第一性原理 → 尝试映射维度 → 发现深层断裂带或桥梁。
最后得出结论：「A 说 [X]，B 说 [Y]。它们之间存在 [具体张力/桥梁]，或者【完全无张力，强扯会破坏系统】。」
> **💡 必须阅读**：参见 [references/tension-example.md](references/tension-example.md) 了解合格的 `<thinking>` 深度与断层推演标准。

**Forgotten 模式**回答：
同样需要 `<thinking>` 逻辑流转：分析旧笔记核心价值 → 对比当前项目。
得出结论：「这张沉没的旧笔记，和你最近正在想的 [某问题] 有关联，补充了 [X] 视角。若完全无共振，标注为【自然沉没】。」

**Island 模式**回答：
对每张孤岛笔记，完成连接三问，找到 ≥2 条有意义的候选连接。输出：
- 连接理由（为什么这两张笔记应该对话）
- 可执行的双向链接文案（两端各写什么）
- 若真的找不到有意义连接：标注【建议保持孤岛，自然沉没】，不强行拼凑。

### Step 3: 行动输出

| 发现类型 | 行动 |
|---------|------|
| 新连接 | 更新双向链接（两张笔记都更新）|
| 新想法 | 创建闪念笔记或永久笔记 |
| 需更新 | 补充新理解、修正过时内容 |
| 无发现 | 记录漫游日志即可 |

---

## 输出模板

```markdown
## 随机漫游记录 [日期]

### 抽取的笔记
1. [[笔记1]] - [一句话核心观点]
2. [[笔记2]] - [一句话核心观点]
...

### 偶遇洞察（常规/Forgotten）
<thinking>
1. 沉没笔记B的价值实质是...
2. 当前项目核心矛盾是...
3. 映射发现...
</thinking>
- **[笔记A] × [当前思考/项目]**：[发现的连接]
- **[沉没笔记B]**：[打捞价值，或标记为“自然沉没”]

### 张力碰撞（Tension 专用）
<thinking>
1. 笔记A的第一性原理是...
2. 笔记B的第一性原理是...
3. 试图在这个维度上发生碰撞... 发现断层/桥梁...
</thinking>
- **[笔记A] ⚡ [笔记B]**：[它们之间的张力与桥梁发现，或报告无张力]

### 行动项
- [ ] [具体行动，如：更新两张笔记的双向链接]
```

**自动保存**：将上述内容保存到 `memory/random-walk/YYYY-MM-DD.md`

---

## 质量检查
- [ ] 至少提出 2 条“能落到文件里的”双向建议（含 Tension 的桥梁或 Forgotten 的打捞）
- [ ] Tension 模式：必须至少尝试 3 对配对，找到 ≥1 个桥梁洞察
- [ ] Forgotten 模式：明确区分"有价值的打捞"与"自然沉没"，无须强行连接
- [ ] Island 模式：已读取最新 network-health 报告并提取孤岛列表；每张孤岛给出 ≥2 条有意义连接，或明确标注【建议保持孤岛】
- [ ] 如全无发现：说明为什么，并给出下一次参数建议（mode/filter）
- [ ] 输出已保存到 `memory/random-walk/YYYY-MM-DD.md`
```

## File: `skills/random-walk/references/tension-example.md`
```markdown
# 随机漫游 Tension 模式优秀样例

当执行 `tension` 模式时，哪怕抽离出的笔记看似风马牛不相及，也应努力按**第一性原理**进行深度降维映射，而一旦完全无法融合时，则果断报告“无张力”；若能融合，则应产出极其意外的桥梁新知。

以下是一次合格的、具备 `<thinking>` 链与断层发现的高质量示例（它没有生搬硬套，而是揭示了内在的方法论冲突）：

***

## 随机漫游记录 2026-03-08 (Tension)

### 抽取的笔记
1. [[20260306_老年AI伴侣设计原则_ElliQ启示]] - 老年AI伴侣（如ElliQ）需定位Wellness、不直连911以保持边界清晰，且必须有极高的可预测性。
2. [[20260203_洞察_抖音5A与AIPL模型映射关系]] - 抖音的5A模型核心在于强调A3（Ask主动问询）是决定种草成功和未来转化的金标准。

### 张力碰撞（Tension 专用）
<thinking>
1. 笔记A的第一性原理是：对待脆弱信任人群（老年人），产品功能不能失控、需要边界、甚至为了安全感要主动放弃一些过度服务。其核心是**控制预期、消除意外，让用户始终处于舒适被动区**。
2. 笔记B的第一性原理是：在内容营销与电商转化中，最高价值的用户动作是突破被动接受（A1/A2），产生主动的探究、搜索和问询（A3）。其核心是**激发意外兴趣、促成主动行为突变**。
3. 试图在这个维度上发生碰撞... 发现断层/桥梁：
   - 表面断层：老年AI设计追求“老人家别乱动，机器也别乱动”（去A3化）；而电商营销却在“不计代价地引诱用户乱动”（A3化）。二者有天然水火不容的张力。
   - 桥梁深挖：如果用 A3 的思维去审核 ElliQ？如果在不破坏“可预测性”安全感的前提下，让 ElliQ 能够自然诱发老人的“A3（主动诉求/询问）”，这是否意味着从“监护仪”真正进化成了“伴侣”？比如：AI 偶发性地提一个留白话题（A2），引发老人主动追问（A3）——这其实才是老年AI从「被动服从」向「主动信任与依赖」跨越的转化金标准。
</thinking>
- **[[20260306_老年AI伴侣设计原则_ElliQ启示]] ⚡ [[20260203_洞察_抖音5A与AIPL模型映射关系]]**：由水火不容产生的新知——老年AI设计的“可预测性安全感”与营销漏斗的“A3主动问询”形成巨大张力。可以把营销领域的 A3 转化率概念引入老年 AI 评估中：一个成功的 AI 伴侣，不仅是稳妥的被动响应者，更应能通过克制的留白，安全地引发老人的“主动反问（Ask）”。
```

## File: `skills/random-walk/scripts/get_random_notes.sh`
```bash
#!/bin/bash
# get_random_notes.sh — ZK Steward companion (link-proposer path C).
# Usage: ./get_random_notes.sh --mode <mode> [--count <count>]
# Optional env: NOTES_DIR (default 05_每日记录), INDEX_DIR (default 03_索引), EXTRA_DIR (default longlongago).

NOTES_DIR="${NOTES_DIR:-05_每日记录}"
INDEX_DIR="${INDEX_DIR:-03_索引}"
EXTRA_DIR="${EXTRA_DIR:-longlongago}"

MODE=""
COUNT=1

while [[ "$#" -gt 0 ]]; do
    case $1 in
        --mode) MODE="$2"; shift ;;
        --count) COUNT="$2"; shift ;;
        *) echo "Unknown parameter passed: $1"; exit 1 ;;
    esac
    shift
done

if [[ -z "$MODE" ]]; then
    echo "Error: --mode is required."
    exit 1
fi

case "$MODE" in
    tension)
        SEED=$(date +%s)
        find "$NOTES_DIR" "$EXTRA_DIR" -name "*.md" -type f 2>/dev/null | \
            awk -v seed=$SEED 'BEGIN{srand(seed)} {print rand() "\t" $0}' | \
            sort -n | cut -f2- | head -n "$COUNT"
        ;;
    forgotten)
        find "$NOTES_DIR" "$EXTRA_DIR" -type f -name "*.md" -mtime +90 2>/dev/null | while read -r file; do
            basename=$(basename "$file" .md)
            link_count=$(grep -rc "\[\[$basename\]\]" "$NOTES_DIR" "$INDEX_DIR" 2>/dev/null | awk -F: '{sum+=$2} END{print sum+0}')
            if [ "$link_count" -le 1 ]; then
                echo "$file"
            fi
        done | head -n 50 | sort -R | head -n "$COUNT"
        ;;
    recent)
        find "$NOTES_DIR" -type f -name "*.md" -mtime -7 2>/dev/null | sort -R | head -n "$COUNT"
        ;;
    *)
        echo "Error: Unknown mode '$MODE'. Supported modes: tension, forgotten, recent."
        exit 1
        ;;
esac
```

## File: `skills/strategic-advisor/SKILL.md`
```markdown
---
name: strategic-advisor
description: 决策建议与权衡取舍（多视角分析）。适用于用户问“怎么办/该不该/怎么选/如何决策”，需要给出取舍理由、行动方案与风险对策。
---

# 出谋划策

## 角色
战略咨询与决策支持领域的最强大脑。

## 思维模型工具箱

| 模型 | 核心问题 | 适用场景 |
|------|---------|---------|
| **第一性原理** | 最根本的假设是什么？ | 打破惯性思维，回归本质 |
| **80/20法则** | 哪20%因素决定80%结果？ | 识别关键杠杆点 |
| **系统思维** | 各要素如何相互影响？ | 分析复杂关联和反馈循环 |
| **JTBD** | 用户真正想完成什么任务？ | 从目标出发重构问题 |

---

## 执行原则

根据问题复杂度选择深度：
- **快速咨询**（一句话答疑）：仅执行 Step 1-2
- **深度决策**（需要归档）：执行全部 Step 1-4

## 快速开始
- 先把问题改写成“可决策句”（A vs B / 做 or 不做 / 先后顺序）。
- 选 1-2 个思维模型推进（不要全用），并输出：建议 + 行动计划 + 风险与对策。

---

## 工作流

### Step 0: 识别领域 → 选择专家
在回答开头声明："以 [专家名] 的视角来分析..."

### Step 1: 理解用户背景
- **强制读取个性化**：`.cursor/context/personalization.md`（真源，用户直接编辑）
- 按「优势放大」「劣势补强」策略适配沟通与输出风格（结论先行、结构可导航、可执行）

### Step 2: 同理心分析
- 搜索历史对话记录
- 深度分析：历史关注点、反复出现的问题模式
- 提供有同理心的回应

### Step 3: 知识连接与框架分析
- 从思维模型工具箱选择 1-2 个模型
- 建立连接：概念连接、方法论连接、跨领域连接

### Step 4: 战略建议与归档
- 对齐长期目标
- 提供资源配置建议、风险识别
- 归档到「对话记录」文件夹

---

## 输出模板

```markdown
# YYYYMMDD_HH_主题

## 问题概述
[核心问题]

## 分析框架
使用 [思维模型] 分析：
- ...

## 决策建议
[一句话核心建议]

## 行动计划
| 阶段 | 动作 | 衡量指标 |
|------|------|---------|
| 1 | ... | ... |

## 知识连接
- [[相关文档1]] - 连接理由
```

## 质量检查
- [ ] 展现同理心
- [ ] 使用 ≥1 个思维模型
- [ ] 建立 ≥2 个知识连接
```

## File: `skills/structure-note/SKILL.md`
```markdown
---
name: structure-note
description: 结构笔记工具。适用于"写文章/整理项目文档/整理项目资料/整理文件夹里的文档/大纲整理/串联论证/解释复杂话题"时需要阅读顺序和逻辑树。以半年后读者仍能看懂为目的，采用卢曼 Folgezettel 思维设计论证链。
---

# 结构笔记

> 设计规范见 `../index-note/references/20260203_索引体系设计规范.md`
> 结构化流程详见 `references/结构化流程.md`

## 定位
知识网络的阅读导航系统。
**核心理念**：结构笔记是「阅读清单」而非「分类」——串联、论证、引导。

---

## 创建目的（必读）

> **默认读者**：未来的自己——假设已忘记当时情境、项目背景、为什么做这个结构。

**写作原则**：结构笔记必须**自包含**，让未来读者无需依赖记忆即可理解：
1. **当时语境**：顶部写明「何时、为何、在什么项目下」创建
2. **为什么这个顺序**：每个阅读项都要有理由，回答「半年后读到这里，为什么下一步是它？」
3. **论证链可见**：用 Folgezettel 思维（前驱→本位→后继）让思想轨迹可追溯

**卢曼方法论**（策略层）：
- **不问「属于哪类」**，问「**和谁对话、接在谁后面**」
- **结构 = 链接链**：卢曼的「结构」来自纸条间的引用链，不是分类树
- **桌面固化**：结构笔记 = 卢曼桌面上「这一摊怎么排」的数字化固化
- **论证依赖优先**：先识别概念依赖、论证依赖、应用依赖，再排阅读顺序

---

## 快速开始
- **模式一（创建结构笔记）**：识别依赖 → 设计逻辑树 → 定义阅读顺序 → 确保可发现。
- **模式二（批量整理）**：指定目录/文件 → 逐个分析依赖 → 生成结构笔记。

> 不要问"它属于哪个分类"，问"怎么读才能搞懂它"。
> 如需「查找入口」而非「阅读顺序」，请用 `index-note` skill。

---

## 本项目约定（重要）

### 索引 vs 结构笔记

| 类型 | 回答的问题 | 隐喻 | 核心元素 |
|------|-----------|------|----------|
| **索引** | 我想找 X，从哪进？ | 图书馆检索卡片柜 | 关键词 → 入口 |
| **结构笔记** | 我想搞懂 X，怎么看？ | 策划好的阅读清单 | 1、2、3… 的阅读顺序 |

### 结构笔记触发场景

- 准备写文章
- 需要串联论证链
- 向他人解释复杂话题
- 项目大纲整理
- 整理某个文件夹里的文档

### 结构笔记设计约束

- **命名规范**：清晰标识主题+笔记类型（推荐格式：`[主题]_结构笔记.md` 或 `[主题]结构笔记.md`）
- **逻辑树必须有**：阅读顺序 + 依赖关系
- **必须可发现**：在相关索引中添加入口

### 结构笔记生命周期

| 状态 | 条件 | 处理方式 |
|------|------|----------|
| **活跃** | 正在使用 | 正常维护 |
| **归档** | 项目结束/文章完成 | 标记归档，保留只读 |

---

## 模式一：创建结构笔记

> 结构化流程详见 `references/结构化流程.md`

### Step 1: 明确目标
1. **串联内容**：这个结构笔记要串联哪些内容？
2. **目标读者**：默认是「未来的自己」——需自包含，不依赖当前记忆
3. **预期收获**：阅读后能得到什么？（写进结构笔记顶部，供未来读者锚定）
4. **当时语境**：何时、为何、在什么项目下创建？（必须写进结构笔记，供未来回溯）

### Step 2: 全库搜集与聚合
1. **全库搜索**：搜索与该主题相关的现有笔记
2. **聚类筛选**：识别核心笔记（骨架）和支撑笔记（血肉）

### Step 3: 执行结构化流程
按 `references/结构化流程.md` 的 Step 1-5 执行：
1. 识别笔记间依赖关系（前置知识/核心概念/延伸应用）
2. 设计逻辑树（核心→深化→应用）
3. 定义阅读顺序（从简单到复杂/先理论后实践）
4. 确保可发现（被索引指向）
5. **半年后可读检查**：当时语境 + 自包含理由

---

## 模式二：内容整理（单篇/批量）

> 结构化流程详见 `references/结构化流程.md`

将散落的笔记整理进有序的阅读路径（Bottom-up）。

### 适用场景
- **单篇**：刚写完一篇笔记，寻找它在现有结构中的位置
- **批量**：整理项目文档 / 归档散乱笔记

### Step 1: 确定输入
- **单篇**：直接指定笔记路径
- **批量**：指定目录路径或文件列表

### Step 2: 逐个寻找逻辑位置
对每篇笔记，思考它在序列中的角色（Folgezettel）：
1. **前驱 (Premise)**：它基于什么？（接在谁后面）
2. **本位 (Argument)**：它讲了什么？（核心贡献）
3. **后继 (Function)**：它导向什么？（开启什么新话题）

### Step 3: 生成序列建议

1. **单篇**：找到它在逻辑树中的最佳插入点（Insert After X）。
2. **批量**：根据依赖关系整理出有向无环图（DAG），转化为线性阅读顺序。

### Step 4: 汇总报告

见下文「输出模板」。

---

## 输出模板

### 模式二（单篇）：结构插入建议

```markdown
**文档**：[[笔记名]]

**1. 逻辑定位 (Logic Role)**：
> "它在论证链中扮演什么角色？"
- [ ] **前驱 (Premise)**：基于 [[笔记A]] (铺垫/原理)
- [ ] **本位 (Argument)**：提出核心观点...
- [ ] **后继 (Function)**：为 [[笔记B]] 提供支撑/反例

**2. 序列插入 (Sequence Insertion)**：
> "把它插在阅读清单的哪里？"
- [ ] **插入位置**：在 [[结构笔记_X]] 的 [[笔记A]] 之后
- [ ] **阅读引导**：先读 A，再读本篇（因为...）

**3. 结构补完 (Gap Analysis)**：
- [ ] (可选) 是否缺了中间环节？→ 建议补写 [[笔记C]]
```

### 模式二（批量）：内容整理报告

| 文档 | 逻辑角色 (Role) | 序列位置 (Sequence) | 补完建议 (Gap) |
|------|----------------|--------------------|---------------|
| [[笔记A]] | 核心论点 | 1.作为开篇 | - |
| [[笔记B]] | A 的具体案例 | 2.紧接 A 之后 | 建议补一个反例 |

### 模式一：结构笔记格式

```markdown
# [主题]结构笔记

> **所属索引**：[[索引名称]]  
> **更新**：YYYY-MM-DD
>
> **当时语境**（半年后仍能看懂的关键）：YYYY年M月，因 [项目/写文章/解释X] 需要，整理 [主题] 的阅读路径。预期阅读后能 [一句话概括收获]。
>
> **默认读者**：未来的自己——本结构自包含，不依赖记忆。

---

## 逻辑树 (Logic Tree)

① [[核心笔记]] — 框架概述
  └─ [[深化笔记]] — 具体应用
      └─ [[案例笔记]] — 实践例证

---

## 阅读顺序 (Sequence)

> 每个顺序都有「理由」：半年后读到这里，仍能理解为什么下一步是它。

1. **[[笔记A]]** (Premise)
   > 理由：建立基础概念...（接在谁后面？为什么先读它？）
2. **[[笔记B]]** (Argument)
   > 理由：核心机制解析...（依赖 A 的什么？）
3. **[[笔记C]]** (Conclusion)
   > 理由：实战应用与总结...（导向什么？）

---

## 意外发现区（Serendipity）

> 卢曼强调：知识网络的价值在于「意外连接」。虽然不在主阅读路径，但可能带来启发的笔记：

- **[[笔记X]]** — 不同领域但类似模式（跨域类比）
- **[[笔记Y]]** — 反例/对比视角（批判性思考）
- **[[笔记Z]]** — 意外相关的主题（网络漫游）

---

相关索引：[[索引_xxx]]
```

---

## 常见错误与失败案例

### 常见错误速查表

| 错误 | 解决 |
|------|------|
| 结构笔记没有阅读顺序（只有列表）| 必须有 1、2、3 的顺序 + 理由 |
| 结构笔记没有被索引指向 | 在相关索引添加入口 |
| 逻辑树过于扁平（无层级）| 区分核心/深化/案例层次 |
| 结构笔记太长（变成文章）| 保持导航性质，不要写内容 |
| 没有说明为什么这个顺序 | 每个阅读项都要有理由 |
| **缺少当时语境** | 顶部必须写「何时、为何、在什么项目下」——半年后看不懂 |
| **理由太简略** | 理由要回答「半年后读到这里，为什么下一步是它？」 |

### 失败案例：过度线性化的结构笔记

❌ **Before（问题版本）**：
```markdown
# 项目X结构笔记

## 阅读顺序

1. [[笔记A]] — 建立基础
2. [[笔记B]] — 深入理解
3. [[笔记C]] — 实践应用
```

**问题诊断**：
- 缺少当时语境（不知道为什么创建这个结构）
- 理由模糊（"建立基础"太抽象，半年后看不懂为什么先读A）
- 缺少依赖说明（B依赖A的什么？）
- 没有意外发现区（过度线性化）

---

✅ **After（修正版本）**：
```markdown
# 项目X结构笔记

> **当时语境**：2026年1月，因需要向新团队成员解释项目X的设计逻辑，整理阅读路径。预期阅读后能理解：为什么选择架构A而非B、如何落地执行。
> **默认读者**：未来的自己——本结构自包含，不依赖记忆。

## 阅读顺序

1. **[[笔记A：用户需求分析]]** (Premise)
   > **理由**：需先理解用户的3大核心痛点（来自笔记A第2节），才能理解下一篇的架构设计为什么选择"分布式"而非"单体"。
   > **接下来**：理解了需求后 → [[笔记B]]理解架构选择

2. **[[笔记B：架构设计决策]]** (Argument)
   > **理由**：基于A的痛点2（高并发），本篇解释为什么选择分布式架构。依赖A的"用户规模预测"（10万+）作为决策依据。
   > **前置依赖**：需先读[[笔记A]]，否则看不懂"为什么不用单体架构"
   > **接下来**：理解了架构后 → [[笔记C]]看实践案例

3. **[[笔记C：实践案例]]** (Conclusion)
   > **理由**：B是理论，C是实战——展示架构在真实场景的应用与踩坑经验。

## 意外发现区

- **[[笔记D：反例_单体架构的失败]]** — 对比视角，理解为什么不选单体
```

**改进要点**：
✅ 增加当时语境
✅ 理由具体化（说明依赖什么、为什么这个顺序）
✅ 增加意外发现区（反例）
✅ 标注前置依赖和接下来的阅读路径

---

## 质量检查

### 模式一（创建结构笔记）
- [ ] 所有笔记的依赖关系已识别
- [ ] 逻辑树层级清晰（核心→深化→应用）
- [ ] 阅读顺序有理由说明 (Premise/Argument/Conclusion)
- [ ] 链式双向链接完整 (笔记间已添加 Next/Previous)
- [ ] **半年后可读**：顶部有「当时语境」；每个阅读项的理由能让半年后的读者理解「为什么下一步是它」

### 模式二（内容整理）
- [ ] **单篇**：明确指定了插入位置（接在谁后面）并建立链接
- [ ] **批量**：生成的阅读顺序无逻辑断层且笔记间已互链
- [ ] **完整性**：所有输入文档都被分配了逻辑角色

---

## 设计说明（本 skill 的编写方法论）

> 本 skill 的「创建目的」「卢曼方法论」「半年后可读」等设计，遵循以下编写策略：

- **卢曼思考策略**：不问分类问对话；结构=链接链；Folgezettel（前驱/本位/后继）思维
- **提示词工程**（Karpathy/Context Engineering）：具体约束、示例驱动、结构清晰、减少模糊
- **Skill 最佳实践**（skill-creator）：契约明确、渐进披露、适度自由度、质量检查清单
```

## File: `skills/structure-note/references/结构化流程.md`
```markdown
# 结构化流程

> 本文件定义从「一组相关笔记」到「结构笔记完成」的通用处理逻辑。
> 被 SKILL.md 的模式一、模式二引用。

---

## 卢曼方法论（策略层）

> **不问「属于哪类」**，问「**和谁对话、接在谁后面**」。

- **结构 = 链接链**：卢曼的「结构」来自纸条间的引用链，不是分类树
- **Folgezettel 思维**：每张笔记有前驱（基于什么）、本位（讲什么）、后继（导向什么）
- **默认读者**：半年后的昀峤——结构笔记必须自包含，不依赖当前记忆

---

## 流程总览

```
相关笔记 → 识别依赖 → 设计逻辑树 → 定义阅读顺序 → 确保可发现 → 半年后可读检查
```

---

## Step 1: 识别笔记间依赖关系

对每篇笔记问三个问题：
1. **前置知识**：读这篇前需要先理解什么？
2. **核心概念**：这篇的核心是什么？
3. **延伸应用**：读完这篇后可以继续读什么？

**依赖类型**：
- **概念依赖**：A 是 B 的前置概念
- **论证依赖**：A 是 B 的论据/证据
- **应用依赖**：A 是理论，B 是实践

---

## Step 2: 设计逻辑树

根据依赖关系，构建层级结构：

```
核心框架笔记
├── 深化笔记 A（概念细化）
│   └── 案例笔记 A1
├── 深化笔记 B（另一分支）
└── 应用笔记 C（实践层）
```

**层级原则**：
- **第 1 层**：核心框架（先读这个才能理解其他）
- **第 2 层**：概念深化（拆解核心的各个方面）
- **第 3 层**：工具/方法/实践步骤（具体实践）
- **第 4 层**：案例/应用（具体实践）

---

## Step 3: 定义阅读顺序

把逻辑树转化为**线性阅读序列**：

**排序原则**（Learning Path 设计）：
1. **从简单到复杂**：先基础概念，再进阶内容
2. **先理论后实践**：先框架，再案例
3. **先全局后细节**：先鸟瞰，再深入

**关键动作：建立双向链接（Chain Linking）**
> 仅仅在结构笔记里列出来是不够的，笔记之间必须**互相看见**。
- **前一篇笔记底部**：添加 `Next: [[后一篇笔记]]`
- **后一篇笔记顶部**：添加 `Previous: [[前一篇笔记]]`

**理由写作原则（半年后可读）**：
> 每个阅读项的理由要能回答：「半年后读到这里，为什么下一步是它？」——避免「建立基础」这类模糊表述，要写清「接在谁后面、依赖什么、导向什么」。

**输出格式**：
```markdown
## 阅读顺序建议

1. 先读 [[笔记A]]：建立基础概念
   > (已添加 Next: [[笔记B]])
2. 再读 [[笔记B]]：理解核心机制
   > (已添加 Previous: [[笔记A]], Next: [[笔记C]])
3. 然后 [[笔记C]]：看具体方法
4. 最后 [[笔记D]]：看实战应用
```

---

## Step 4: 确保可发现

**验收标准**：结构笔记必须被至少 1 个索引指向

**操作清单**：
1. **结构笔记 → 索引**：在结构笔记底部添加「相关索引」链接
2. **索引 → 结构笔记**：在相关索引的关键词区添加入口

---

## Step 5: 半年后可读检查（未来昀峤能看懂）

**验收问题**：半年后的昀峤打开这份结构笔记，能否不依赖记忆就理解？

- [ ] **当时语境**：顶部有「何时、为何、在什么项目下」创建
- [ ] **预期收获**：顶部有一句话概括「阅读后能得到什么」
- [ ] **理由自包含**：每个阅读项的理由能回答「半年后读到这里，为什么下一步是它？」

---

## 质量检查

- [ ] 所有笔记的依赖关系已识别
- [ ] 逻辑树层级清晰（核心→深化→应用）
- [ ] 阅读顺序有理由说明（为什么这个顺序）
- [ ] 结构笔记已被索引指向
- [ ] **半年后可读**：当时语境 + 自包含理由
```

## File: `skills/workflow-audit/SKILL.md`
```markdown
---
name: workflow-audit
description: 用审查领域最强大脑（德明+葛文德）对多阶段流程的执行完成度做逐项核对与系统闭环检查，产出审查报告并可选补执行。适用于 book-reading、meeting-note、deep-learning 等有明确 Phase/步骤与 Definition of Done（或质量验收清单）的 skill。关键词：流程审查、执行完成度、是否执行完、用最强大脑检查、workflow audit。
---

# 流程执行审查（Workflow Audit）

## 适用边界

- **本 skill 适用**：某次按某 skill（如 book-reading、meeting-note）执行后，需**核对是否全部按该 skill 要求做完**；或用户明确说「检查一遍」「审查」「是否执行完」「用最强大脑检查」。
- **不适用**：对「计划/方案内容」做评审（用 plan-reviewer）；对「单篇文档质量」做润色或校对。

## 角色定位（审查领域最强大脑）

- **W. Edwards Deming（系统视角）**：流程是否闭环？哪里有断点？输入→输出是否可测量？
- **Atul Gawande（清单视角）**：逐项打勾，漏一步即风险；不跳过、不假设「应该做了」。

**核心理念**：审查的价值在于**显式化遗漏**并可选**补执行**，而不是给「大概做完了」背书。

## 工作流

### Step 1：确定审查对象

- 明确**被审查的 skill**（如 book-reading、meeting-note）及**本次产出所在位置**（目录/文件列表）。
- 若用户未指定 skill，从上下文推断（如刚做完 Book-Reading 版会议整理 → 审查 book-reading）。

### Step 2：提取标准

- **读取**该 skill 的 `SKILL.md`（必要时含 `references/` 中与流程、验收相关的文件）。
- **提取**：① 工作流阶段（Phase 0→1→2… 或等效步骤）；② 每阶段强制要求（交付物、检查项）；③ Definition of Done 或质量验收清单；④ 若有 task 追踪（如 task.md），其要求的勾选项。

### Step 3：逐项核对（葛文德式清单）

- 按阶段/检查项制表：**要求 | 状态(✅/❌/⚠️) | 说明**。
- 对每条要求，对照**本次实际产出**（文件是否存在、内容是否满足）给出状态；❌ 与 ⚠️ 须写清缺什么或与标准的差异。
- 若 skill 要求「在 task.md 中记录」，检查 task.md 是否存在、是否包含对应链接或勾选。

### Step 4：系统闭环（德明视角）

- **输入→输出**：本次任务的输入（如会议纪要、一本书）与预期输出（如结构笔记、原子笔记、索引）是否完整？
- **断点**：哪些阶段未执行或未达标，导致下游无法成立？（例如未做 Phase 2.5 → 索引未入网，即断点。）
- **可测量**：Definition of Done 中与「网络/入网/链接」等可验证项，是否已满足？

### Step 5：产出审查报告

- 落盘为 **`YYYYMMDD_[任务名]_流程审查报告_德明与葛文德视角.md`**，与本次产出同目录或用户指定位置。
- 结构必须包含：
  1. **逐项清单表**（Step 3 结果）
  2. **系统闭环**（Step 4 结论）
  3. **Definition of Done 最终勾选**（逐条 ✅/❌）
  4. 若该 skill 有「多索引挂载/入网」类要求：**多索引挂载清单**（哪些笔记已入哪一索引、建议补充入哪一索引及理由）
- 模板见 `references/audit_report_template.md`。

### Step 6：可选补执行

- 若用户同意或上下文合理（如「全部执行完了吗」隐含希望补全），对审查中标为 ❌ 的项执行补救：
  - 缺文件则创建（如 task.md、缺失的索引入口）；
  - 缺挂载则写入父索引、移动文件到规定目录等。
- 补执行后在审查报告中更新状态（❌→✅）并注明「已补执行」。

## 输出规范

- **审查报告**：必出；含上述四块（清单、闭环、DoD、多索引若有）。
- **补执行**：按需；若执行，须在报告末尾简短列出「本次补执行项」。

## 质量自检

- [ ] 清单中每一项都对应 skill 原文中的可验证要求，无主观新增或遗漏。
- [ ] 状态 ❌/⚠️ 均有「说明」列，可追溯。
- [ ] 德明断点与 DoD 勾选一致（断点即 DoD 未满足项）。
- [ ] 若补执行，报告与实际文件状态一致。

---

**参考**：`references/audit_report_template.md`（报告结构模板）；首次实践见 `05_每日记录/2026/02/20260212/安防与老人看护会议_BookReading版/20260212_BookReading流程审查报告_德明与葛文德视角.md`。
```

## File: `skills/workflow-audit/references/audit_report_template.md`
```markdown
# [任务名] 流程审查报告（德明 × 葛文德视角）

> **审查标准**：以 **W. Edwards Deming**（系统闭环、未执行即缺陷）与 **Atul Gawande**（清单逐项、漏一步即风险）为审查领域最强大脑，对照 `[目标 skill 名]/SKILL.md` 工作流程与 Definition of Done 逐项核对。  
> **审查对象**：[任务/产出名称]  
> **审查时间**：YYYY-MM-DD

---

## 一、逐项清单（葛文德式 Checklist）

| Phase/步骤 | 要求 | 状态 | 说明 |
|------------|------|------|------|
| ... | ... | ✅/❌/⚠️ | ... |

---

## 二、系统闭环（德明视角）

- **输入→输出**：[是否完整]
- **断点**：[哪些未做导致下游不成立]
- **可测量**：[DoD 中可验证项是否满足]

---

## 三、Definition of Done 最终勾选

- [ ] / [x] **项一**：…
- [ ] / [x] **项二**：…

---

## 四、多索引挂载清单（若适用）

| 笔记 | 已入索引 | 建议补充入 | 理由 |
|------|----------|------------|------|
| ... | ... | ... | ... |

---

## 五、结论

**[未] 全部执行完毕**的项为：…  
[若已补执行] 以上已在本次审查中**补执行**；补做后流程可视为**全部执行完毕**，符合 Definition of Done。
```

## File: `skills/workflow-audit/references/expert_personas.md`
```markdown
# 审查领域专家视角（Expert Personas）

> 本 skill 强制使用两位「审查领域最强大脑」的思维，避免审查流于形式。

## W. Edwards Deming（系统与质量）

- **关注点**：系统闭环、变异与断点、可测量。
- **审查时问**：流程的输入→输出是否完整？哪一环节未执行会导致下游失效（断点）？Definition of Done 中可验证的项是否真的可被检查？
- **输出要求**：审查报告必须含「系统闭环」一节，明确写出断点与可测量结论。

## Atul Gawande（清单与漏步）

- **关注点**：逐项打勾、不假设、漏一步即风险。
- **审查时问**：Skill 中写的每一步、每一项验收，是否都有一条对应的核对结果？是否有「我们以为做了」但未在清单中体现的项？
- **输出要求**：审查报告必须含「逐项清单表」，每行对应 skill 中的可验证要求，状态为 ✅/❌/⚠️ 且带说明。

## 组合使用

- **先清单（葛文德）**：把 skill 的 Phase/DoD 拆成一行行，逐项对照产出打勾。
- **再系统（德明）**：看哪些 ❌ 构成断点、DoD 整体是否从「可测量」上通过。
- **后补执行（可选）**：对 ❌ 项按 skill 要求补做，再更新报告。
```

