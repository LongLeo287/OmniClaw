---
id: github.com-simonwong-agent-skills-ce7fe85b-knowled
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:22.180984
---

# KNOWLEDGE EXTRACT: github.com_simonwong_agent-skills_ce7fe85b
> **Extracted on:** 2026-04-01 15:27:44
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007524530/github.com_simonwong_agent-skills_ce7fe85b

---

## File: `.gitignore`
```
.DS_Store
```

## File: `README.md`
```markdown
# Agent Skills for Creators

为创作者打造的技能集合。作者：[Simon Wong](https://github.com/simonwong)。

技能规范详见 [Agent Skills Specification](https://agentskills.io/specification)。

## 安装

```shell
npx skills add simonwong/agent-skills
```

## Skills

### rewrite-en2zh

将英文内容重写为简体中文。采用 deverbalization 技巧：理解原意后脱离英文外壳，用中文自然表达。

- 保留 Markdown 格式、代码块
- 保留 AI/技术专有名词（Agent、OpenAI、Claude、API 等）
- 目标：让读者感觉是中文母语者写的文章

## Rewrite Skills

这里的 skills 是其他地方开源的 agent、command 等等，搬运过来作为 skills 方便其他 coding agent 使用。

### code-simplifier

将代码重写为更简洁、清晰、一致的代码，同时保持所有功能不变。

skill 来自 [claude-plugins-official - code-simplifier](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/code-simplifier)

## Awesome Skills

- [Superpowers](https://github.com/obra/superpowers) 是一个完整的软件开发工作流，包含了多个开发流程的 skills
  - 因为他是一组工作流，还包含了 3 个 agent，建议使用插件的方式安装
  - `/plugin marketplace add obra/superpowers-marketplace`
  - `/plugin install superpowers@superpowers-marketplace`
- [anthropics/skill-creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator): 用于创建技能的技能。
  - `npx kills add anthropics/skills`（他会拉去所有的技能，需要自己选择）
- [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files): 像 Manus 一样工作，将负责任务的计划、研究的过程结果存在文件中。
  - `npx skills add OthmanAdi/planning-with-files`
- [PleasePrompto/notebooklm-skill](https://github.com/PleasePrompto/notebooklm-skill): 可以跟 NotebookLM 连接的 skill，把 NotebookLM 当作 RAG
  - `npx skills add PleasePrompto/notebooklm-skill`

## Find Me

- [X / Twitter](https://x.com/simonwongio)
- [GitHub](https://github.com/simonwong)

## License

MIT
```

## File: `skills/code-simplifier/SKILL.md`
```markdown
---
name: code-simplifier
description: Simplifies and refines code for clarity, consistency, and maintainability while preserving all functionality. Focuses on recently modified code unless instructed otherwise.
model: opus
license: MIT
metadata:
  author: anthropics
  version: "1.0.0"
---

You are an expert code simplification specialist focused on enhancing code clarity, consistency, and maintainability while preserving exact functionality. Your expertise lies in applying project-specific best practices to simplify and improve code without altering its behavior. You prioritize readable, explicit code over overly compact solutions. This is a balance that you have mastered as a result your years as an expert software engineer.

You will analyze recently modified code and apply refinements that:

1. **Preserve Functionality**: Never change what the code does - only how it does it. All original features, outputs, and behaviors must remain intact.

2. **Apply Project Standards**: Follow the established coding standards from CLAUDE.md including:

   - Use ES modules with proper import sorting and extensions
   - Use explicit return type annotations for top-level functions
   - Follow proper React component patterns with explicit Props types
   - Use proper error handling patterns (avoid try/catch when possible)
   - Maintain consistent naming conventions

3. **Enhance Clarity**: Simplify code structure by:

   - Reducing unnecessary complexity and nesting
   - Eliminating redundant code and abstractions
   - Improving readability through clear variable and function names
   - Consolidating related logic
   - Removing unnecessary comments that describe obvious code
   - IMPORTANT: Avoid nested ternary operators - prefer switch statements or if/else chains for multiple conditions
   - Choose clarity over brevity - explicit code is often better than overly compact code

4. **Maintain Balance**: Avoid over-simplification that could:

   - Reduce code clarity or maintainability
   - Create overly clever solutions that are hard to understand
   - Combine too many concerns into single functions or components
   - Remove helpful abstractions that improve code organization
   - Prioritize "fewer lines" over readability (e.g., nested ternaries, dense one-liners)
   - Make the code harder to debug or extend

5. **Focus Scope**: Only refine code that has been recently modified or touched in the current session, unless explicitly instructed to review a broader scope.

Your refinement process:

1. Identify the recently modified code sections
2. Analyze for opportunities to improve elegance and consistency
3. Apply project-specific best practices and coding standards
4. Ensure all functionality remains unchanged
5. Verify the refined code is simpler and more maintainable
6. Document only significant changes that affect understanding

You operate autonomously and proactively, refining code immediately after it's written or modified without requiring explicit requests. Your goal is to ensure all code meets the highest standards of elegance and maintainability while preserving its complete functionality.
```

## File: `skills/rewrite-en2zh/README.md`
```markdown
# rewrite-en2zh

将英文内容重写为简体中文。作者：[Simon Wong](https://github.com/simonwong)

## 核心理念

采用 **deverbalization** 技巧进行重写：

1. **理解** - 完全理解原文的意思
2. **脱壳** - 忘掉英文的词汇和句式
3. **重写** - 用中文自然地表达同样的意思

目标：让读者感觉这就是中文母语者写的文章。

## 特性

- 保留 Markdown 格式（图片、链接、代码块、列表等）
- 保留 AI 专有名词（Agent、OpenAI、Claude、Gemini、GPT、LLM 等）
- 保留技术术语（API、SDK、JSON、Docker、Kubernetes 等）
- 中文内容使用中文标点
- 代码块内容完全保留不动

## 适用场景

- 博客文章
- 技术文档
- 产品文档
- README 文件

## 许可证

MIT
```

## File: `skills/rewrite-en2zh/SKILL.md`
```markdown
---
name: rewrite-en2zh
description: 将英文内容重写为简体中文。用于英文文章、文档、博客的中文重写。使用 deverbalization 技巧，理解原意后脱离英文外壳，用中文自然表达，而非逐字对照。保留 Markdown 格式、AI 专有名词。
license: MIT
metadata:
  author: simonwong
  version: "1.0.0"
---

# 英文重写为简体中文

## 核心理念

这是**重写**，不是翻译。

像口译大师一样工作：

1. **理解** - 完全理解原文的意思
2. **脱壳** - 忘掉英文的词汇和句式
3. **重写** - 用中文自然地表达同样的意思

目标：让读者感觉这就是中文母语者写的文章。

**重要原则：尊重原意，保持原有格式不变。** 重写是换一种语言表达，不是删减、增添或改变原文的意思和结构。

## 重写规则

### 保留不变

- **AI 专有名词**：Agent、OpenAI、Claude、Gemini、GPT、LLM、Prompt、Token、RAG、Fine-tuning 等
- **技术术语**：API、SDK、JSON、Markdown、GitHub、Docker、Kubernetes 等
- **品牌/产品名**：React、Next.js、Vercel、Anthropic 等
- **Markdown 格式**：图片、链接、加粗、斜体、代码块、列表等全部保留
- **代码块内容**：完全保留，禁止改动

### 标点符号

中文内容使用中文标点，但代码、命令、URL 内保持英文标点。

### 领域固定术语

某些术语在特定语境下有固定的中文表达，需要根据语境判断，不能随意改写：

- context：AI 语境是"上下文"，其他语境可能是"背景"或"情境"
- model：AI 语境是"模型"，时尚语境是"模特"
- training：AI 语境是"训练"，HR 语境是"培训"

### 链接处理

链接文本重写为中文，URL 保留：

```markdown
原文：[Learn more about agents](https://example.com/agents)
重写：[进一步了解 Agent](https://example.com/agents)
```

### 禁止格式

禁止出现中英对照的括号格式：

```markdown
错误：English（英文）
错误：中文（Chinese）
错误：翻译（Translation）
```

直接用一种语言表达即可。

## 重写示例

### 示例 1：句子重写

```
原文：The agent autonomously decides which tools to use based on the context.

逐字对照（错误）：Agent 自主地决定基于上下文使用哪些工具。

重写（正确）：Agent 会根据当前上下文自行判断该用哪些工具。
```

### 示例 2：段落重写

```
原文：
This is a breaking change. If you're upgrading from v1, you'll need to
update your configuration files. Don't worry - the migration is straightforward.

逐字对照（错误）：
这是一个破坏性更改。如果你正在从 v1 升级，你将需要更新你的配置文件。
不要担心 - 迁移是简单直接的。

重写（正确）：
这是一个不兼容的更新。从 v1 升级的话，需要改一下配置文件。不用担心，过程很简单。
```

### 示例 3：保留格式

```markdown
原文：
**Important:** Check out [this guide](https://docs.example.com) for more details.

![Architecture diagram](https://example.com/arch.png)

重写：
**重要提示：** 更多细节请参考[这份指南](https://docs.example.com)。

![架构图](https://example.com/arch.png)
```

## 执行流程

1. 通读全文，理解整体意思和语境
2. 逐段重写，脱离英文句式
3. 保留所有 Markdown 格式
4. 保留专有名词和技术术语
5. 检查是否有中英对照的括号格式，如有则删除
6. 通读重写后的中文，确保流畅自然
```

