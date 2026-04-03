---
id: github.com-wshuyi-x-article-publisher-skill-e41c21
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:44.823322
---

# KNOWLEDGE EXTRACT: github.com_wshuyi_x-article-publisher-skill_e41c2192
> **Extracted on:** 2026-04-01 07:35:23
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007519057/github.com_wshuyi_x-article-publisher-skill_e41c2192

---

## File: `.gitignore`
```
# Python
__pycache__/
*.py[cod]
*.egg-info/
.venv/
venv/

# macOS
.DS_Store
.AppleDouble
.LSOverride

# Temp files
*.tmp
*.temp
/tmp/
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2024 wshuyi

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
# X Article Publisher Skill

[English](README.md) | [中文](README_CN.md)

> Publish Markdown articles to X (Twitter) Articles with one command. Say goodbye to tedious rich text editing.

**v1.2.0** — Now with divider support, table-to-image, Mermaid support, and cross-platform clipboard

---

## The Problem

If you're used to writing in Markdown, publishing to X Articles is a **painful process**:

| Pain Point | Description |
|------------|-------------|
| **Format Loss** | Copy from Markdown editor → Paste to X → All formatting gone |
| **Manual Formatting** | Set each H2, bold, link manually — 15-20 min per article |
| **Tedious Image Upload** | 5 clicks per image: Add media → Media → Add photo → Select → Wait |
| **Position Errors** | Hard to remember where each image should go |

### Time Comparison

| Task | Manual | With This Skill |
|------|--------|-----------------|
| Format conversion | 15-20 min | 0 (automatic) |
| Cover image | 1-2 min | 10 sec |
| 5 content images | 5-10 min | 1 min |
| **Total** | **20-30 min** | **2-3 min** |

**10x efficiency improvement**

---

## The Solution

This skill automates the entire publishing workflow:

```
Markdown File
     ↓ Python parsing
Structured Data (title, images with block_index, HTML)
     ↓ Playwright MCP
X Articles Editor (browser automation)
     ↓
Draft Saved (never auto-publishes)
```

### Key Features

- **Rich Text Paste**: Convert Markdown to HTML, paste via clipboard — all formatting preserved
- **Block-Index Positioning** (v1.1): Precise image placement using element indices, not text matching
- **Reverse Insertion**: Insert images from highest to lowest index to avoid position shifts
- **Smart Wait Strategy**: Conditions return immediately when met, no wasted wait time
- **Safe by Design**: Only saves as draft, never publishes automatically

---

## What's New in v1.1.0

| Feature | Before | After |
|---------|--------|-------|
| Image positioning | Text matching (fragile) | Block index (precise) |
| Insertion order | Sequential | Reverse (high→low) |
| Wait behavior | Fixed delay | Immediate return on condition |

### Why Block-Index?

Previously, images were positioned by matching surrounding text — this failed when:
- Multiple paragraphs had similar content
- Text was too short to be unique

Now, each image has a `block_index` indicating exactly which block element it follows. This is deterministic and reliable.

---

## Requirements

| Requirement | Details |
|-------------|---------|
| Claude Code | [claude.ai/code](https://claude.ai/code) |
| Playwright MCP | Browser automation |
| X Premium Plus | Required for Articles feature |
| Python 3.9+ | With dependencies below |
| OS | macOS or Windows |

```bash
# macOS
pip install Pillow pyobjc-framework-Cocoa

# Windows
pip install Pillow pywin32 clip-util

# For Mermaid diagrams (optional)
npm install -g @mermaid-js/mermaid-cli
```

---

## Installation

### Method 1: Git Clone (Recommended)

```bash
git clone https://github.com/wshuyi/x-article-publisher-skill.git
cp -r x-article-publisher-skill/skills/x-article-publisher ~/.claude/skills/
```

### Method 2: Plugin Marketplace

```
/plugin marketplace add wshuyi/x-article-publisher-skill
/plugin install x-article-publisher@wshuyi/x-article-publisher-skill
```

---

## Usage

### Natural Language

```
Publish /path/to/article.md to X
```

```
Help me post this article to X Articles: ~/Documents/my-post.md
```

### Skill Command

```
/x-article-publisher /path/to/article.md
```

---

## Workflow Steps

```
[1/7] Parse Markdown...
      → Extract title, cover image, content images with block_index
      → Convert to HTML, count total blocks

[2/7] Open X Articles editor...
      → Navigate to x.com/compose/articles

[3/7] Upload cover image...
      → First image becomes cover

[4/7] Fill title...
      → H1 used as title (not included in body)

[5/7] Paste article content...
      → Rich text via clipboard
      → All formatting preserved

[6/7] Insert content images (reverse order)...
      → Sort by block_index descending
      → Click block element at index → Paste image
      → Wait for upload (returns immediately when done)

[7/7] Save draft...
      → ✅ Review and publish manually
```

---

## Supported Markdown

| Syntax | Result | Notes |
|--------|--------|-------|
| `# H1` | Article title | Extracted, not in body |
| `## H2` | Section headers | Native support |
| `**bold**` | **Bold text** | Native support |
| `*italic*` | *Italic text* | Native support |
| `[text](url)` | Hyperlinks | Native support |
| `> quote` | Blockquotes | Native support |
| `- item` | Unordered lists | Native support |
| `1. item` | Ordered lists | Native support |
| `![](img.jpg)` | Images | First = cover |
| `---` | Dividers | Via Insert menu (v1.2) |
| Tables | PNG images | Via table_to_image.py (v1.2) |
| Mermaid | PNG images | Via mmdc CLI (v1.2) |

---

## Example

### Input: `article.md`

```markdown
# 5 AI Tools Worth Watching in 2024

![cover](./images/cover.jpg)

AI tools exploded in 2024. Here are 5 worth your attention.

## 1. Claude: Best Conversational AI

**Claude** by Anthropic excels at long-context understanding.

> Claude's context window reaches 200K tokens.

![claude-demo](./images/claude-demo.png)

## 2. Midjourney: AI Art Leader

[Midjourney](https://midjourney.com) is the most popular AI art tool.

![midjourney](./images/midjourney.jpg)
```

### Parsed Output (JSON)

```json
{
  "title": "5 AI Tools Worth Watching in 2024",
  "cover_image": "./images/cover.jpg",
  "content_images": [
    {"path": "./images/claude-demo.png", "block_index": 4},
    {"path": "./images/midjourney.jpg", "block_index": 6}
  ],
  "total_blocks": 7
}
```

### Insertion Order

Images inserted in reverse: `block_index=6` first, then `block_index=4`.

### Result

- Cover: `cover.jpg` uploaded
- Title: "5 AI Tools Worth Watching in 2024"
- Content: Rich text with H2, bold, quotes, links
- Images: Inserted at precise positions via block index
- Status: **Draft saved** (ready for manual review)

---

## Project Structure

```
x-article-publisher-skill/
├── .claude-plugin/
│   └── plugin.json              # Plugin config
├── skills/
│   └── x-article-publisher/
│       ├── SKILL.md             # Skill instructions
│       └── scripts/
│           ├── parse_markdown.py    # Extracts block_index + dividers
│           ├── copy_to_clipboard.py # Cross-platform clipboard
│           └── table_to_image.py    # Markdown table → PNG (v1.2)
├── docs/
│   └── GUIDE.md                 # Detailed guide
├── README.md                    # This file
├── README_CN.md                 # Chinese version
└── LICENSE
```

---

## FAQ

**Q: Why Premium Plus?**
A: X Articles is exclusive to Premium Plus subscribers.

**Q: Windows/Linux support?**
A: Windows is now supported (v1.2). Linux support is still in progress — PRs welcome!

**Q: Image upload failed?**
A: Check: valid path, supported format (jpg/png/gif/webp), stable network.

**Q: Can I publish to multiple accounts?**
A: Not automatically. Switch accounts in browser manually before running.

**Q: Why insert images in reverse order?**
A: Each inserted image shifts subsequent block indices. Inserting from highest to lowest ensures earlier indices remain valid.

**Q: What if text matching was used before?**
A: v1.1 replaces text matching with `block_index`. The `after_text` field is kept for debugging but not used for positioning.

**Q: Why does wait return immediately sometimes?**
A: `browser_wait_for textGone="..."` returns as soon as the text disappears. The `time` parameter is just a maximum, not a fixed delay.

---

## Documentation

- [Detailed Usage Guide](../../../core/security/QUARANTINE/vetted/repos/litellm/cookbook/ai_coding_tool_guides/claude_code_quickstart/guide.md) — Complete documentation with examples

---

## Changelog

### v1.2.0 (2025-01)
- **Divider support**: Detect `---` in Markdown, insert via X Articles menu
- **Table to image**: New `table_to_image.py` script converts Markdown tables to PNG
- **Mermaid support**: Documentation for using `mmdc` to convert diagrams
- **YAML frontmatter**: Automatically skip frontmatter in Markdown files
- **Windows support**: Cross-platform clipboard operations (pywin32 + clip-util)

### v1.1.0 (2025-12)
- **Block-index positioning**: Replace text matching with precise element indices
- **Reverse insertion order**: Prevent index shifts when inserting multiple images
- **Optimized wait strategy**: Return immediately when upload completes
- **H1 title handling**: H1 extracted as title, not included in body HTML

### v1.0.0 (2025-12)
- Initial release
- Rich text paste via clipboard
- Cover + content image support
- Draft-only publishing

---

## License

MIT License - see [LICENSE](LICENSE)

## Author

[wshuyi](https://github.com/wshuyi)

---

## Acknowledgments

v1.2.0 features were inspired by and adapted from:

- **[sugarforever/01coder-agent-skills](https://github.com/sugarforever/01coder-agent-skills)** — The `publish-x-article` skill contributed ideas for:
  - Divider detection and menu-based insertion
  - Table-to-image conversion script
  - Mermaid diagram support documentation
  - YAML frontmatter handling
  - Windows clipboard implementation

Thank you to the community for building upon and improving this skill!

---

## Contributing

- **Issues**: Report bugs or request features
- **PRs**: Welcome! Especially for Windows/Linux support
```

## File: `README_CN.md`
```markdown
# X Article Publisher Skill

[English](README.md) | [中文](README_CN.md)

> 一键将 Markdown 文章发布到 X (Twitter) Articles，告别繁琐的富文本编辑。

**v1.2.0** — 新增分割线支持、表格转图片、Mermaid 支持、跨平台剪贴板

---

## 痛点分析

如果你习惯用 Markdown 写作，将内容发布到 X Articles 是一个**极其痛苦**的过程：

| 痛点 | 描述 |
|------|------|
| **格式丢失** | 从 Markdown 编辑器复制 → 粘贴到 X → 格式全部丢失 |
| **手动格式化** | 逐个设置 H2、粗体、链接 — 每篇文章 15-20 分钟 |
| **图片上传繁琐** | 每张图片 5 次点击：添加媒体 → 媒体 → 添加照片 → 选择 → 等待 |
| **位置容易出错** | 很难记住每张图片应该插入的位置 |

### 时间对比

| 操作 | 手动方式 | 使用本 Skill |
|------|----------|--------------|
| 格式转换 | 15-20 分钟 | 0（自动） |
| 封面图上传 | 1-2 分钟 | 10 秒 |
| 5 张内容图插入 | 5-10 分钟 | 1 分钟 |
| **总计** | **20-30 分钟** | **2-3 分钟** |

**效率提升 10 倍以上**

---

## 解决方案

本 Skill 自动化整个发布流程：

```
Markdown 文件
     ↓ Python 解析
结构化数据（标题、带 block_index 的图片、HTML）
     ↓ Playwright MCP
X Articles 编辑器（浏览器自动化）
     ↓
保存草稿（绝不自动发布）
```

### 核心特性

- **富文本粘贴**：将 Markdown 转换为 HTML，通过剪贴板粘贴 — 所有格式完整保留
- **Block-Index 定位**（v1.1）：使用元素索引精确定位，不依赖文字匹配
- **反向插入**：从高到低索引插入图片，避免位置偏移
- **智能等待策略**：条件满足立即返回，不浪费等待时间
- **安全设计**：仅保存草稿，绝不自动发布

---

## v1.1.0 更新内容

| 功能 | 之前 | 现在 |
|------|------|------|
| 图片定位 | 文字匹配（不稳定） | Block 索引（精确） |
| 插入顺序 | 顺序插入 | 反向插入（从大到小） |
| 等待行为 | 固定延时 | 条件满足立即返回 |

### 为什么使用 Block-Index？

之前的版本通过匹配周围文字来定位图片位置，但遇到以下情况会失败：
- 多个段落内容相似
- 文字太短不够唯一

现在，每张图片都有一个 `block_index` 表示它应该跟在第几个块元素后面。这是确定性的，不会出错。

---

## 环境要求

| 要求 | 说明 |
|------|------|
| Claude Code | [claude.ai/code](https://claude.ai/code) |
| Playwright MCP | 浏览器自动化 |
| X Premium Plus | Articles 功能需要此订阅 |
| Python 3.9+ | 需安装以下依赖 |
| 操作系统 | macOS 或 Windows |

```bash
# macOS
pip install Pillow pyobjc-framework-Cocoa

# Windows
pip install Pillow pywin32 clip-util

# Mermaid 图表支持（可选）
npm install -g @mermaid-js/mermaid-cli
```

---

## 安装方式

### 方式一：Git Clone（推荐）

```bash
git clone https://github.com/wshuyi/x-article-publisher-skill.git
cp -r x-article-publisher-skill/skills/x-article-publisher ~/.claude/skills/
```

### 方式二：插件市场

```
/plugin marketplace add wshuyi/x-article-publisher-skill
/plugin install x-article-publisher@wshuyi/x-article-publisher-skill
```

---

## 使用方法

### 自然语言

```
把 /path/to/article.md 发布到 X
```

```
帮我把这篇文章发到 X Articles：~/Documents/my-post.md
```

### Skill 命令

```
/x-article-publisher /path/to/article.md
```

---

## 工作流程

```
[1/7] 解析 Markdown...
      → 提取标题、封面图、带 block_index 的内容图片
      → 转换为 HTML，统计块元素总数

[2/7] 打开 X Articles 编辑器...
      → 导航到 x.com/compose/articles

[3/7] 上传封面图...
      → 第一张图片作为封面

[4/7] 填写标题...
      → H1 作为标题（不包含在正文中）

[5/7] 粘贴文章内容...
      → 通过剪贴板粘贴富文本
      → 所有格式完整保留

[6/7] 插入内容图片（反向顺序）...
      → 按 block_index 从大到小排序
      → 点击对应块元素 → 粘贴图片
      → 等待上传（完成后立即返回）

[7/7] 保存草稿...
      → ✅ 请手动预览并发布
```

---

## 支持的 Markdown 格式

| 语法 | 效果 | 说明 |
|------|------|------|
| `# H1` | 文章标题 | 提取后不含在正文中 |
| `## H2` | 二级标题 | 原生支持 |
| `**粗体**` | **粗体文字** | 原生支持 |
| `*斜体*` | *斜体文字* | 原生支持 |
| `[文字](url)` | 超链接 | 原生支持 |
| `> 引用` | 引用块 | 原生支持 |
| `- 列表` | 无序列表 | 原生支持 |
| `1. 列表` | 有序列表 | 原生支持 |
| `![](img.jpg)` | 图片 | 第一张为封面 |
| `---` | 分割线 | 通过菜单插入 (v1.2) |
| 表格 | PNG 图片 | 使用 table_to_image.py (v1.2) |
| Mermaid | PNG 图片 | 使用 mmdc CLI (v1.2) |

---

## 完整示例

### 输入：`article.md`

```markdown
# 2024 年最值得关注的 5 个 AI 工具

![封面](./images/cover.jpg)

人工智能工具在 2024 年迎来了爆发式增长。本文将介绍 5 个最值得关注的工具。

## 1. Claude：最强对话 AI

**Claude** 由 Anthropic 开发，在长文本理解方面表现出色。

> Claude 的上下文窗口高达 200K tokens。

![claude-demo](./images/claude-demo.png)

## 2. Midjourney：AI 绘画领导者

[Midjourney](https://midjourney.com) 是目前最受欢迎的 AI 绘画工具。

![midjourney](./images/midjourney.jpg)
```

### 解析输出（JSON）

```json
{
  "title": "2024 年最值得关注的 5 个 AI 工具",
  "cover_image": "./images/cover.jpg",
  "content_images": [
    {"path": "./images/claude-demo.png", "block_index": 4},
    {"path": "./images/midjourney.jpg", "block_index": 6}
  ],
  "total_blocks": 7
}
```

### 插入顺序

图片按反向顺序插入：先 `block_index=6`，再 `block_index=4`。

### 执行结果

- 封面：`cover.jpg` 已上传
- 标题：「2024 年最值得关注的 5 个 AI 工具」
- 内容：富文本格式完整保留（H2、粗体、引用、链接）
- 图片：通过 block index 精确定位插入
- 状态：**草稿已保存**（等待手动预览发布）

---

## 项目结构

```
x-article-publisher-skill/
├── .claude-plugin/
│   └── plugin.json              # 插件配置
├── skills/
│   └── x-article-publisher/
│       ├── SKILL.md             # Skill 核心指令
│       └── scripts/
│           ├── parse_markdown.py    # 提取 block_index + 分割线
│           ├── copy_to_clipboard.py # 跨平台剪贴板
│           └── table_to_image.py    # 表格转 PNG (v1.2)
├── docs/
│   └── GUIDE.md                 # 详细使用指南
├── README.md                    # 英文说明
├── README_CN.md                 # 中文说明（本文件）
└── LICENSE
```

---

## 常见问题

**Q: 为什么需要 Premium Plus？**
A: X Articles 是 Premium Plus 订阅专属功能，普通用户无法使用。

**Q: 支持 Windows/Linux 吗？**
A: Windows 已支持 (v1.2)。Linux 支持仍在开发中，欢迎贡献 PR！

**Q: 图片上传失败怎么办？**
A: 检查：路径是否正确、格式是否支持（jpg/png/gif/webp）、网络是否稳定。

**Q: 可以发布到多个账号吗？**
A: 不支持自动切换。请在浏览器中手动切换账号后再执行。

**Q: 为什么要反向插入图片？**
A: 每插入一张图片，后续块元素的索引会偏移。从大到小插入可以确保前面的索引不受影响。

**Q: 之前的文字匹配方式还能用吗？**
A: v1.1 已用 `block_index` 替代文字匹配。`after_text` 字段保留用于调试，但不再用于定位。

**Q: 为什么等待有时候立即返回？**
A: `browser_wait_for textGone="..."` 会在文字消失时立即返回。`time` 参数只是最大等待时间，不是固定延时。

---

## 详细文档

- [完整使用指南](../../../core/security/QUARANTINE/vetted/repos/litellm/cookbook/ai_coding_tool_guides/claude_code_quickstart/guide.md) — 包含详细说明和更多示例

---

## 更新日志

### v1.2.0 (2025-01)
- **分割线支持**：识别 Markdown 中的 `---`，通过 X Articles 菜单插入
- **表格转图片**：新增 `table_to_image.py` 脚本，将表格转为 PNG
- **Mermaid 支持**：文档说明如何使用 `mmdc` 转换图表
- **YAML 头部跳过**：自动跳过 Markdown 文件开头的 frontmatter
- **Windows 支持**：跨平台剪贴板操作（pywin32 + clip-util）

### v1.1.0 (2025-12)
- **Block-index 定位**：用精确的元素索引替代文字匹配
- **反向插入顺序**：防止多图插入时的索引偏移
- **优化等待策略**：上传完成后立即返回
- **H1 标题处理**：H1 提取为标题，不包含在正文 HTML 中

### v1.0.0 (2025-12)
- 首次发布
- 剪贴板富文本粘贴
- 封面图 + 内容图支持
- 仅保存草稿

---

## 许可证

MIT License - 见 [LICENSE](LICENSE)

## 作者

[wshuyi](https://github.com/wshuyi)

---

## 致谢

v1.2.0 的新功能参考并借鉴自：

- **[sugarforever/01coder-agent-skills](https://github.com/sugarforever/01coder-agent-skills)** — 其中的 `publish-x-article` 技能贡献了以下功能思路：
  - 分割线检测与菜单插入
  - 表格转图片脚本
  - Mermaid 图表支持文档
  - YAML frontmatter 处理
  - Windows 剪贴板实现

感谢社区成员在本项目基础上的改进和贡献！

---

## 贡献

- **Issues**：报告 Bug 或提出功能建议
- **PR**：欢迎贡献代码，特别是 Linux 支持
```

## File: `docs/GUIDE.md`
```markdown
# X Article Publisher Skill 使用指南

> 一键将 Markdown 文章发布到 X (Twitter) Articles，告别繁琐的富文本编辑。

**v1.1.0** — 新增 block-index 精确定位，图片位置更准确

---

## v1.1.0 更新亮点

| 功能 | v1.0 | v1.1 |
|------|------|------|
| 图片定位 | 文字匹配（不稳定） | Block 索引（精确） |
| 插入顺序 | 顺序插入 | 反向插入（高→低） |
| 等待策略 | 固定延时 | 条件满足立即返回 |

---

## 目录

1. [解决的痛点](#1-解决的痛点)
2. [解决方案](#2-解决方案)
3. [执行方式](#3-执行方式)
4. [完整示例](#4-完整示例)
5. [常见问题](#5-常见问题)
6. [更新日志](#6-更新日志)

---

## 1. 解决的痛点

### 1.1 X Articles 是什么？

X (原 Twitter) 为 Premium Plus 订阅用户提供了 **Articles** 功能，允许用户发布长文章（类似博客），突破 280 字符限制。文章支持：

- 富文本格式（标题、粗体、引用等）
- 多张图片嵌入
- 超链接

访问入口：https://x.com/compose/articles

### 1.2 手动发布的痛点

如果你习惯用 Markdown 写作，将内容发布到 X Articles 是一个**极其繁琐**的过程：

#### 痛点一：格式无法直接粘贴

```
❌ 从 Markdown 编辑器复制内容 → 粘贴到 X Articles → 格式全部丢失
```

X Articles 编辑器不支持 Markdown，你需要**逐一手动设置**每个格式：
- 选中文字 → 点击 H2 按钮
- 选中文字 → 点击粗体按钮
- 选中文字 → 点击链接按钮 → 粘贴 URL

一篇包含 5 个小节、10 处加粗、8 个链接的文章，格式设置可能需要 **15-20 分钟**。

#### 痛点二：图片插入效率低下

X Articles 的图片插入流程：

```
点击段落 → 点击"添加媒体内容" → 点击"媒体" → 点击"添加照片或视频" → 选择文件 → 等待上传
```

每张图片需要 **5 次点击 + 文件选择 + 等待上传**。一篇包含 5 张图片的文章，仅图片插入就需要 **5-10 分钟**。

#### 痛点三：图片位置难以精确控制

Markdown 中图片位置是精确的：

```markdown
这是第一段内容。

![图1](image1.jpg)

这是第二段内容。

![图2](image2.jpg)
```

但在 X Articles 中，你需要：
1. 记住每张图片应该插入的位置
2. 滚动找到正确的段落
3. 手动插入

图片越多，出错概率越高。

#### 痛点四：重复劳动

如果你经常发布长文章，这些操作需要**每次重复**：
- 每篇文章都要手动转换格式
- 每张图片都要重复 5 次点击
- 每次都要检查格式是否正确

### 1.3 时间成本对比

| 操作 | 手动方式 | 使用本 Skill |
|------|----------|--------------|
| 格式转换 | 15-20 分钟 | 0（自动） |
| 封面图上传 | 1-2 分钟 | 10 秒 |
| 5 张内容图插入 | 5-10 分钟 | 1 分钟 |
| 总计 | **20-30 分钟** | **2-3 分钟** |

**效率提升：10 倍以上**

---

## 2. 解决方案

### 2.1 技术架构

本 Skill 通过以下技术栈实现自动化：

```
┌─────────────────┐
│   Markdown 文件  │
└────────┬────────┘
         │ Python 解析
         ▼
┌─────────────────┐
│  结构化数据 (JSON) │
│  - title        │
│  - cover_image  │
│  - content_images│
│  - html         │
└────────┬────────┘
         │ Playwright MCP
         ▼
┌─────────────────┐
│  X Articles 编辑器 │
│  (浏览器自动化)   │
└─────────────────┘
```

#### 核心组件

| 组件 | 作用 |
|------|------|
| `parse_markdown.py` | 解析 Markdown，提取标题、图片、转换 HTML |
| `copy_to_clipboard.py` | 将 HTML/图片复制到系统剪贴板 |
| Playwright MCP | 控制浏览器，模拟用户操作 |
| Claude Code | 协调整个流程 |

### 2.2 工作流程："先文后图"策略

本 Skill 采用**先文后图**（Text First, Images Later）策略，确保内容完整且图片位置准确：

```
Step 1: 解析 Markdown
        ↓
Step 2: 打开 X Articles 编辑器
        ↓
Step 3: 上传封面图（第一张图片）
        ↓
Step 4: 填写标题
        ↓
Step 5: 粘贴 HTML 富文本内容（通过剪贴板）
        ↓
Step 6: 在正确位置插入内容图片（通过剪贴板粘贴）
        ↓
Step 7: 保存草稿（绝不自动发布）
```

### 2.3 关键技术优化

#### 优化一：剪贴板富文本粘贴

传统方式需要逐个设置格式，本 Skill 通过：

1. Python 将 Markdown 转换为 HTML
2. 将 HTML 复制到系统剪贴板（保留富文本格式）
3. 在编辑器中 `Cmd+V` 粘贴

```python
# copy_to_clipboard.py 核心逻辑
from AppKit import NSPasteboard, NSPasteboardTypeHTML

pasteboard = NSPasteboard.generalPasteboard()
pasteboard.setData_forType_(html_data, NSPasteboardTypeHTML)
```

结果：**所有格式一次性粘贴完成**，包括 H2、粗体、链接、列表等。

#### 优化二：图片剪贴板粘贴

传统方式每张图片需要 5 次点击，本 Skill 通过：

1. Python 将图片复制到系统剪贴板
2. 点击目标段落
3. `Cmd+V` 粘贴图片

```python
# copy_to_clipboard.py 图片处理
from AppKit import NSPasteboard, NSPasteboardTypeTIFF

# 可选：上传前压缩图片
img.thumbnail((2000, 2000))
img.save(buffer, format='JPEG', quality=85)
```

对比：

| 方式 | 浏览器操作次数 |
|------|--------------|
| 传统 | 5 次点击 + 文件选择 |
| 本 Skill | 1 次点击 + 1 次粘贴 |

#### 优化三：图片位置精确定位

`parse_markdown.py` 提取每张图片的**块索引信息**（v1.1 新特性）：

```json
{
  "content_images": [
    {
      "path": "/path/to/img1.jpg",
      "block_index": 5,
      "after_text": "上下文文字（仅用于调试）..."
    }
  ],
  "total_blocks": 12
}
```

**block_index 定位原理**：
- 每张图片的 `block_index` 表示它应该插入在第 N 个块元素之后（0 索引）
- 不依赖文字匹配，精确可靠
- `after_text` 保留用于人工核验，不参与定位

**反向插入策略**：
- 按 `block_index` 从大到小的顺序插入图片
- 先插入索引大的，不会影响索引小的位置
- 例如：先插入 block_index=12，再插入 block_index=5

### 2.4 支持的 Markdown 格式

| Markdown 语法 | 效果 |
|--------------|------|
| `# H1` | 文章标题（自动提取） |
| `## H2` | 二级标题 |
| `**粗体**` | **粗体文字** |
| `*斜体*` | *斜体文字* |
| `[链接](url)` | 超链接 |
| `> 引用` | 引用块 |
| `- 列表` | 无序列表 |
| `1. 列表` | 有序列表 |
| `![](img.jpg)` | 图片（第一张为封面） |

### 2.5 安全设计

**绝不自动发布**：本 Skill 仅将内容保存为草稿，最终发布需要用户手动确认。

```
✅ 自动完成：上传、格式化、排版
❌ 不会执行：点击"发布"按钮
```

这确保用户可以在发布前：
- 预览最终效果
- 检查格式是否正确
- 修改任何需要调整的内容

---

## 3. 执行方式

### 3.1 前置条件

#### 条件一：X Premium Plus 订阅

Articles 功能仅对 Premium Plus 用户开放。验证方式：
1. 访问 https://x.com/compose/articles
2. 如果能看到编辑器，说明你有权限

#### 条件二：安装 Playwright MCP

本 Skill 依赖 Playwright MCP 进行浏览器自动化。

检查是否已安装：
```bash
cat ~/.claude/settings.json | grep playwright
```

如未安装，在 Claude Code 中执行：
```
帮我安装 Playwright MCP
```

#### 条件三：安装 Python 依赖

```bash
pip install Pillow pyobjc-framework-Cocoa
```

验证安装：
```bash
python -c "from AppKit import NSPasteboard; print('OK')"
```

#### 条件四：安装本 Skill

**方式 A：Git Clone（推荐）**

```bash
git clone https://github.com/wshuyi/x-article-publisher-skill.git
cp -r x-article-publisher-skill/skills/x-article-publisher ~/.claude/skills/
```

**方式 B：插件市场**

```
/plugin marketplace add wshuyi/x-article-publisher-skill
/plugin install x-article-publisher@wshuyi/x-article-publisher-skill
```

### 3.2 触发指令

安装完成后，在 Claude Code 中使用以下方式触发：

#### 方式一：自然语言

```
把 /path/to/article.md 发布到 X
```

```
帮我把这篇文章发到 X Articles：~/Documents/my-article.md
```

```
Publish ~/blog/post.md to X
```

#### 方式二：Skill 命令

```
/x-article-publisher /path/to/article.md
```

### 3.3 操作流程

触发后，Claude 会自动执行以下步骤：

```
[1/7] 解析 Markdown 文件...
      → 提取标题：「你的文章标题」
      → 发现封面图：cover.jpg
      → 发现 3 张内容图片
      → HTML 转换完成

[2/7] 打开 X Articles 编辑器...
      → 导航到 https://x.com/compose/articles
      → 等待编辑器加载

[3/7] 上传封面图...
      → 点击"添加照片或视频"
      → 上传 cover.jpg
      → 等待上传完成

[4/7] 填写标题...
      → 输入：「你的文章标题」

[5/7] 粘贴文章内容...
      → HTML 已复制到剪贴板
      → 粘贴富文本内容
      → 格式保留：5 个 H2，8 处粗体，12 个链接

[6/7] 插入内容图片...
      → 图片 1/3：定位到「这是第一段内容...」后
      → 图片 2/3：定位到「这是第二段内容...」后
      → 图片 3/3：定位到「这是第三段内容...」后

[7/7] 保存草稿...
      → 草稿已自动保存
      → 请在 X 中预览并手动发布
```

### 3.4 注意事项

1. **保持浏览器可见**：Playwright 需要控制浏览器窗口，请不要最小化
2. **已登录 X**：确保浏览器中已登录你的 X 账号
3. **图片路径**：Markdown 中的图片路径需要是有效的本地路径
4. **网络稳定**：图片上传需要稳定的网络连接

---

## 4. 完整示例

### 4.1 示例 Markdown 文件

文件路径：`~/Documents/ai-tools-review.md`

```markdown
# 2024 年最值得关注的 5 个 AI 工具

![cover](./images/cover.jpg)

人工智能工具在 2024 年迎来了爆发式增长。本文将介绍 5 个最值得关注的 AI 工具。

## 1. Claude：最强对话 AI

**Claude** 由 Anthropic 开发，在长文本理解和代码生成方面表现出色。

> Claude 的上下文窗口高达 200K tokens，可以处理整本书的内容。

主要特点：
- 超长上下文理解
- 出色的推理能力
- 安全可靠

![claude-demo](./images/claude-demo.png)

## 2. Midjourney：AI 绘画领导者

[Midjourney](https://midjourney.com) 是目前最受欢迎的 AI 绘画工具。

![midjourney-example](./images/midjourney.jpg)

## 总结

这些工具正在改变我们的工作方式。选择适合自己的工具，提升效率。
```

### 4.2 执行命令

```
把 ~/Documents/ai-tools-review.md 发布到 X
```

### 4.3 执行结果

Claude 会：

1. **解析文件**，输出：
   ```json
   {
     "title": "2024 年最值得关注的 5 个 AI 工具",
     "cover_image": "~/Documents/images/cover.jpg",
     "content_images": [
       {"path": "~/Documents/images/claude-demo.png", "after_text": "安全可靠"},
       {"path": "~/Documents/images/midjourney.jpg", "after_text": "是目前最受欢迎的 AI 绘画工具"}
     ]
   }
   ```

2. **自动操作浏览器**：
   - 上传 cover.jpg 作为封面
   - 填写标题「2024 年最值得关注的 5 个 AI 工具」
   - 粘贴富文本内容（H2、粗体、引用、链接、列表全部保留）
   - 在「安全可靠」段落后插入 claude-demo.png
   - 在「是目前最受欢迎的 AI 绘画工具」段落后插入 midjourney.jpg

3. **完成提示**：
   ```
   ✅ 草稿已保存！

   请在 X 中预览文章效果，确认无误后手动点击发布。
   预览地址：当前浏览器窗口
   ```

---

## 5. 常见问题

### Q1: 为什么需要 Premium Plus？

A: X Articles 是 Premium Plus 订阅专属功能。普通用户无法访问 `/compose/articles` 页面。

### Q2: 支持 Windows 吗？

A: 目前仅支持 macOS，因为剪贴板操作使用了 `pyobjc-framework-Cocoa`。Windows 支持需要替换为 `pywin32`，欢迎贡献 PR。

### Q3: 图片上传失败怎么办？

A: 检查以下几点：
- 图片路径是否正确
- 图片格式是否支持（jpg, png, gif, webp）
- 网络连接是否稳定
- 图片大小是否超过 X 限制

### Q4: 格式粘贴后显示不正确？

A: 确保：
- Python 依赖已正确安装
- 使用 `Cmd+V` 粘贴而非右键粘贴
- 编辑器已完全加载

### Q5: 可以发布到多个账号吗？

A: 目前不支持自动切换账号。如需发布到不同账号，请手动在浏览器中切换后再执行。

### Q6: 如何自定义图片压缩质量？

A: 在 SKILL.md 中，图片粘贴使用 `--quality 85` 参数。你可以修改这个值（1-100），数值越低压缩越多。

---

## 附录：项目结构

```
x-article-publisher-skill/
├── .claude-plugin/
│   └── plugin.json           # 插件配置
├── skills/
│   └── x-article-publisher/
│       ├── SKILL.md          # Skill 核心指令
│       └── scripts/
│           ├── parse_markdown.py    # Markdown 解析
│           └── copy_to_clipboard.py # 剪贴板操作
├── docs/
│   └── GUIDE.md              # 本文档
├── README.md
└── LICENSE
```

---

## 反馈与贡献

- **GitHub**: https://github.com/wshuyi/x-article-publisher-skill
- **Issues**: 遇到问题请提交 Issue
- **PR**: 欢迎贡献代码，特别是 Windows/Linux 支持

---

*本文档由 Claude Code 生成，最后更新：2024-12*
```

## File: `skills/x-article-publisher/SKILL.md`
```markdown
---
name: x-article-publisher
description: |
  Publish Markdown articles to X (Twitter) Articles editor with proper formatting. Use when user wants to publish a Markdown file/URL to X Articles, or mentions "publish to X", "post article to Twitter", "X article", or wants help with X Premium article publishing. Handles cover image upload and converts Markdown to rich text automatically.
---

# X Article Publisher

Publish Markdown content to X (Twitter) Articles editor, preserving formatting with rich text conversion.

## Prerequisites

- Playwright MCP for browser automation
- User logged into X with Premium Plus subscription
- Python 3.9+ with dependencies:
  - macOS: `pip install Pillow pyobjc-framework-Cocoa`
  - Windows: `pip install Pillow pywin32 clip-util`
- For Mermaid diagrams: `npm install -g @mermaid-js/mermaid-cli`

## Scripts

Located in `~/.claude/skills/x-article-publisher/scripts/`:

### parse_markdown.py
Parse Markdown and extract structured data:
```bash
python parse_markdown.py <markdown_file> [--output json|html] [--html-only]
```
Returns JSON with: title, cover_image, content_images, **dividers** (with block_index for positioning), html, total_blocks

### copy_to_clipboard.py
Copy image or HTML to system clipboard (cross-platform):
```bash
# Copy image (with optional compression)
python copy_to_clipboard.py image /path/to/image.jpg [--quality 80]

# Copy HTML for rich text paste
python copy_to_clipboard.py html --file /path/to/content.html
```

### table_to_image.py
Convert Markdown table to PNG image:
```bash
python table_to_image.py <input.md> <output.png> [--scale 2]
```
Use when X Articles doesn't support native table rendering or for consistent styling.

## Pre-Processing (Optional)

Before publishing, scan the Markdown for elements that need conversion:

### Tables → PNG
```bash
# Extract table to temp file, then convert
python ~/.claude/skills/x-article-publisher/scripts/table_to_image.py /tmp/table.md /tmp/table.png
# Replace table in markdown with: ![Table](/tmp/table.png)
```

### Mermaid Diagrams → PNG
```bash
# Extract mermaid block to .mmd file, then convert
mmdc -i /tmp/diagram.mmd -o /tmp/diagram.png -b white -s 2
# Replace mermaid block with: ![Diagram](/tmp/diagram.png)
```

### Dividers (---)
Dividers are automatically detected by `parse_markdown.py` and output in the `dividers` array. They must be inserted via X Articles' **Insert > Divider** menu (HTML `<hr>` tags are ignored by X).

## Workflow

**Strategy: "先文后图后分割线" (Text First, Images Second, Dividers Last)**

For articles with images and dividers, paste ALL text content first, then insert images and dividers at correct positions using block index.

1. **(Optional)** Pre-process: Convert tables/mermaid to images
2. Parse Markdown with Python script → get title, images, **dividers** with block_index, HTML
3. Navigate to X Articles editor
4. Upload cover image (first image)
5. Fill title
6. Copy HTML to clipboard (Python) → Paste with Cmd+V
7. Insert content images at positions specified by block_index
8. **Insert dividers at positions specified by block_index** (via Insert > Divider menu)
9. Save as draft (NEVER auto-publish)

## 高效执行原则 (Efficiency Guidelines)

**目标**: 最小化操作之间的等待时间，实现流畅的自动化体验。

### 1. 避免不必要的 browser_snapshot

大多数浏览器操作（click, type, press_key 等）都会在返回结果中包含页面状态。**不要**在每次操作后单独调用 `browser_snapshot`，直接使用操作返回的页面状态即可。

```
❌ 错误做法：
browser_click → browser_snapshot → 分析 → browser_click → browser_snapshot → ...

✅ 正确做法：
browser_click → 从返回结果中获取页面状态 → browser_click → ...
```

### 2. 避免不必要的 browser_wait_for

只在以下情况使用 `browser_wait_for`：
- 等待图片上传完成（`textGone="正在上传媒体"`）
- 等待页面初始加载（极少数情况）

**不要**使用 `browser_wait_for` 来等待按钮或输入框出现 - 它们在页面加载完成后立即可用。

### 3. 并行执行独立操作

当两个操作没有依赖关系时，可以在同一个消息中并行调用多个工具：

```
✅ 可以并行：
- 填写标题 (browser_type) + 复制HTML到剪贴板 (Bash)
- 解析Markdown生成JSON + 生成HTML文件

❌ 不能并行（有依赖）：
- 必须先点击create才能上传封面图
- 必须先粘贴内容才能插入图片
```

### 4. 连续执行浏览器操作

每个浏览器操作返回的页面状态包含所有需要的元素引用。直接使用这些引用进行下一步操作：

```
# 理想流程（每步直接执行，不额外等待）：
browser_navigate → 从返回状态找create按钮 → browser_click(create)
→ 从返回状态找上传按钮 → browser_click(上传) → browser_file_upload
→ 从返回状态找应用按钮 → browser_click(应用)
→ 从返回状态找标题框 → browser_type(标题)
→ 点击编辑器 → browser_press_key(Meta+v)
→ ...
```

### 5. 准备工作前置

在开始浏览器操作之前，先完成所有准备工作：
1. 解析 Markdown 获取 JSON 数据
2. 生成 HTML 文件到 /tmp/
3. 记录 title、cover_image、content_images 等信息

这样浏览器操作阶段可以连续执行，不需要中途停下来处理数据。

## Step 1: Parse Markdown (Python)

Use `parse_markdown.py` to extract all structured data:

```bash
python ~/.claude/skills/x-article-publisher/scripts/parse_markdown.py /path/to/article.md
```

Output JSON:
```json
{
  "title": "Article Title",
  "cover_image": "/path/to/first-image.jpg",
  "cover_exists": true,
  "content_images": [
    {"path": "/path/to/img2.jpg", "original_path": "/md/dir/assets/img2.jpg", "exists": true, "block_index": 5, "after_text": "context..."},
    {"path": "/path/to/img3.jpg", "original_path": "/md/dir/assets/img3.jpg", "exists": true, "block_index": 12, "after_text": "another..."}
  ],
  "html": "<p>Content...</p><h2>Section</h2>...",
  "total_blocks": 45,
  "missing_images": 0
}
```

**Key fields:**
- `block_index`: The image should be inserted AFTER block element at this index (0-indexed)
- `total_blocks`: Total number of block elements in the HTML
- `after_text`: Kept for reference/debugging only, NOT for positioning
- `exists`: Whether the image file was found (if false, upload will fail)
- `original_path`: The path resolved from Markdown (before auto-search)
- `path`: The actual path to use (may differ from original_path if auto-searched)
- `missing_images`: Count of images not found anywhere

Save HTML to temp file for clipboard:
```bash
python parse_markdown.py article.md --html-only > /tmp/article_html.html
```

## Step 2: Open X Articles Editor

### 浏览器错误处理

如果遇到 `Error: Browser is already in use` 错误：

```
# 方案1：先关闭浏览器再重新打开
browser_close
browser_navigate: https://x.com/compose/articles

# 方案2：如果 browser_close 无效（锁定），提示用户手动关闭 Chrome

# 方案3：使用已有标签页，直接导航
browser_tabs action=list  # 查看现有标签
browser_navigate: https://x.com/compose/articles  # 在当前标签导航
```

**最佳实践**：每次开始前先用 `browser_tabs action=list` 检查状态，避免创建多余空白标签。

### 导航到编辑器

```
browser_navigate: https://x.com/compose/articles
```

**重要**: 页面加载后会显示草稿列表，不是编辑器。需要：

1. **等待页面加载完成**: 使用 `browser_snapshot` 检查页面状态
2. **立即点击 "create" 按钮**: 不要等待 "添加标题" 等编辑器元素，它们只有点击 create 后才出现
3. **等待编辑器加载**: 点击 create 后，等待编辑器元素出现

```
# 1. 导航到页面
browser_navigate: https://x.com/compose/articles

# 2. 获取页面快照，找到 create 按钮
browser_snapshot

# 3. 点击 create 按钮（通常 ref 类似 "create" 或带有 create 标签）
browser_click: element="create button", ref=<create_button_ref>

# 4. 现在编辑器应该打开了，可以继续上传封面图等操作
```

**注意**: 不要使用 `browser_wait_for text="添加标题"` 来等待页面加载，因为这个文本只有在点击 create 后才出现，会导致超时。

If login needed, prompt user to log in manually.

## Step 3: Upload Cover Image

1. Click "添加照片或视频" button
2. Use browser_file_upload with the cover image path (from JSON output)
3. Verify image uploaded

## Step 4: Fill Title

- Find textbox with "添加标题" placeholder
- Use browser_type to input title (from JSON output)

## Step 5: Paste Text Content (Python Clipboard)

Copy HTML to system clipboard using Python, then paste:

```bash
# Copy HTML to clipboard
python ~/.claude/skills/x-article-publisher/scripts/copy_to_clipboard.py html --file /tmp/article_html.html
```

Then in browser:
```
browser_click on editor textbox
browser_press_key: Meta+v
```

This preserves all rich text formatting (H2, bold, links, lists).

## Step 6: Insert Content Images (Text Search Positioning)

**推荐方法**: 使用 `after_text` 文字搜索定位，比 `block_index` 更直观可靠。

### 定位原理

每张图片的 `after_text` 字段记录了它前一个段落的末尾文字（最多80字符）。在编辑器中搜索包含该文字的段落，点击后插入图片。

### 操作步骤

For each content image (from `content_images` array), **按 block_index 从大到小的顺序**：

```bash
# 1. Copy image to clipboard (with compression)
python ~/.claude/skills/x-article-publisher/scripts/copy_to_clipboard.py image /path/to/img.jpg --quality 85
```

```
# 2. 在 browser_snapshot 中搜索包含 after_text 的段落
#    找到该段落的 ref

# 3. Click the paragraph containing after_text
browser_click: element="paragraph with target text", ref=<paragraph_ref>

# 4. **关键步骤**: 按 End 键移动光标到行尾
#    这一步非常重要！避免点击到段落中的链接导致位置偏移
browser_press_key: End

# 5. Paste image
browser_press_key: Meta+v

# 6. Wait for upload (only use textGone, no time parameter)
browser_wait_for textGone="正在上传媒体"
```

### 为什么需要按 End 键？

**问题**: 当段落包含链接时（如 `[链接文字](url)`），点击段落可能会：
- 触发链接编辑弹窗
- 将光标定位在链接内部而非段落末尾

**解决方案**: 点击段落后立即按 `End` 键：
- 确保光标移动到段落末尾
- 避免链接干扰
- 图片将正确插入在该段落之后

### 定位策略

在 browser_snapshot 返回的结构中，搜索 `after_text` 的关键词：

```yaml
textbox [ref=editor]:
  generic [ref=p1]:
    - StaticText: "元旦假期我在家里翻手机相册..."  # 如果 after_text 包含这段文字，点击 p1
  heading [ref=h1]:
    - StaticText: "演示"
  generic [ref=p2]:
    - StaticText: "这东西到底有多省事儿？"
    - link [ref=link1]: "Claude Code"  # 注意：段落可能包含链接
  ...
```

### 反向插入示例

如果有3张图片，block_index 分别为 5, 12, 27：
1. 先插入 block_index=27 的图片（after_text 搜索 + End + 粘贴）
2. 再插入 block_index=12 的图片
3. 最后插入 block_index=5 的图片

**从大到小插入**可以避免位置偏移问题。

## Step 6.5: Insert Dividers (Via Menu)

**重要**: Markdown 中的 `---` 分割线不能通过 HTML `<hr>` 标签粘贴（X Articles 会忽略它）。必须通过 X Articles 的 Insert 菜单插入。

### 操作步骤

For each divider (from `dividers` array), in **reverse order of block_index**:

```
# 1. Click the block element at block_index position
browser_click on the element at position block_index in the editor

# 2. Open Insert menu (Add Media button)
browser_click on "Insert" or "添加媒体" button

# 3. Click Divider menu item
browser_click on "Divider" or "分割线" menuitem

# Divider is inserted at cursor position
```

### 与图片的插入顺序

建议先插入所有图片，再插入所有分割线。两者都按 block_index **从大到小**的顺序：

1. 插入所有图片（从最大 block_index 开始）
2. 插入所有分割线（从最大 block_index 开始）

## Step 7: Save Draft

1. Verify content pasted (check word count indicator)
2. Draft auto-saves, or click Save button if needed
3. Click "预览" to verify formatting
4. Report: "Draft saved. Review and publish manually."

## Critical Rules

1. **NEVER publish** - Only save draft
2. **First image = cover** - Upload first image as cover image
3. **Rich text conversion** - Always convert Markdown to HTML before pasting
4. **Use clipboard API** - Paste via clipboard for proper formatting
5. **Block index positioning** - Use block_index for precise image/divider placement
6. **Reverse order insertion** - Insert images and dividers from highest to lowest block_index
7. **H1 title handling** - H1 is used as title only, not included in body
8. **Dividers via menu** - Markdown `---` must be inserted via Insert > Divider menu (HTML `<hr>` is ignored)

## Supported Formatting

| Element | Support | Notes |
|---------|---------|-------|
| H2 (`##`) | Native | Section headers |
| Bold (`**`) | Native | Strong emphasis |
| Italic (`*`) | Native | Emphasis |
| Links (`[](url)`) | Native | Hyperlinks |
| Ordered lists | Native | 1. 2. 3. |
| Unordered lists | Native | - bullets |
| Blockquotes (`>`) | Native | Quoted text |
| Code blocks | Converted | → Blockquotes |
| Tables | Converted | → PNG images (use table_to_image.py) |
| Mermaid | Converted | → PNG images (use mmdc) |
| Dividers (`---`) | Menu insert | → Insert > Divider |

## Example Flow

User: "Publish /path/to/article.md to X"

```bash
# Step 1: Parse Markdown
python ~/.claude/skills/x-article-publisher/scripts/parse_markdown.py /path/to/article.md > /tmp/article.json
python ~/.claude/skills/x-article-publisher/scripts/parse_markdown.py /path/to/article.md --html-only > /tmp/article_html.html
```

2. Navigate to https://x.com/compose/articles
3. Upload cover image (browser_file_upload for cover only)
4. Fill title (from JSON: `title`)
5. Copy & paste HTML:
   ```bash
   python ~/.claude/skills/x-article-publisher/scripts/copy_to_clipboard.py html --file /tmp/article_html.html
   ```
   Then: browser_press_key Meta+v
6. For each content image, **in reverse order of block_index**:
   ```bash
   python copy_to_clipboard.py image /path/to/img.jpg --quality 85
   ```
   - Click block element at `block_index` position
   - browser_press_key Meta+v
   - Wait until upload complete
7. Verify in preview
8. "Draft saved. Please review and publish manually."

## Best Practices

### 为什么用 block_index 而非文字匹配？

1. **精确定位**: 不依赖文字内容，即使多处文字相似也能正确定位
2. **可靠性**: 索引是确定性的，不会因为文字相似而混淆
3. **调试方便**: `after_text` 仍保留用于人工核验

### 为什么用 Python 而非浏览器内 JavaScript？

1. **本地处理更可靠**: Python 直接操作系统剪贴板，不受浏览器沙盒限制
2. **图片压缩**: 上传前压缩图片 (--quality 85)，减少上传时间
3. **代码复用**: 脚本固定不变，无需每次重新编写转换逻辑
4. **调试方便**: 脚本可单独测试，问题易定位

### 等待策略

**重要发现**: Playwright MCP 的 `browser_wait_for` 实际行为是 **先等待 time 秒，再检查条件**，而非轮询！

```javascript
// 实际执行的代码：
await new Promise(f => setTimeout(f, time * 1000));  // 先固定等待
await page.getByText("xxx").waitFor({ state: 'hidden' });  // 再检查
```

**正确用法**:
- ✅ 只用 `textGone`，不设 `time`：让 Playwright 自己轮询等待
- ✅ 只用 `time`：固定等待指定秒数
- ❌ 同时用 `textGone` + `time`：会先等 time 秒再检查，浪费时间

```
# 推荐：只用 textGone，让它自动等待条件满足
browser_wait_for textGone="正在上传媒体"

# 或者：用 browser_snapshot 轮询检查状态
# 每次操作后检查返回的页面状态，无需额外等待
```

### 图片插入效率

每张图片的浏览器操作从5步减少到2步：
- 旧: 点击 → 添加媒体 → 媒体 → 添加照片 → file_upload
- 新: 点击段落 → Meta+v

### 封面图 vs 内容图

- **封面图**: 使用 browser_file_upload（因为有专门的上传按钮）
- **内容图**: 使用 Python 剪贴板 + 粘贴（更高效）

## 故障排除

### MCP 连接问题

如果 Playwright MCP 工具不可用（报错 `No such tool available` 或 `Not connected`）：

**方案1：重新连接 MCP（推荐）**
```
执行 /mcp 命令，选择 playwright，选择 Restart
```

**方案2：清理残留进程后重连**
```bash
# 杀掉所有残留的 playwright 进程
pkill -f "mcp-server-playwright"
pkill -f "@playwright/mcp"

# 然后执行 /mcp 重新连接
```

**配置文件位置**: `~/.claude/mcp_servers.json`

### 浏览器错误处理

如果遇到 `Error: Browser is already in use` 错误：

```bash
# 方案1：先关闭浏览器再重新打开
browser_close
browser_navigate: https://x.com/compose/articles

# 方案2：杀掉 Chrome 进程
pkill -f "Chrome.*--remote-debugging"
# 然后重新 navigate
```

### 图片位置偏移

如果图片插入位置不正确（特别是点击含链接的段落时）：

**原因**: 点击段落时可能误触链接，导致光标位置错误

**解决方案**: 点击后**必须按 End 键**移动光标到行尾

```
# 正确流程
1. browser_click 点击目标段落
2. browser_press_key: End        # 关键步骤！
3. browser_press_key: Meta+v     # 粘贴图片
4. browser_wait_for textGone="正在上传媒体"
```

### 图片路径找不到

如果 Markdown 中的相对路径图片找不到（如 `./assets/image.png` 实际在其他位置）：

**自动搜索**: `parse_markdown.py` 会自动在以下目录搜索同名文件：
- `~/Downloads`
- `~/Desktop`
- `~/Pictures`

**stderr 输出示例**:
```
[parse_markdown] Image not found at '/path/to/assets/img.png', using '/Users/xxx/Downloads/img.png' instead
```

**JSON 字段说明**:
- `original_path`: Markdown 中指定的路径（解析后的绝对路径）
- `path`: 实际使用的路径（如果自动搜索成功，会不同于 original_path）
- `exists`: `true` 表示找到文件，`false` 表示未找到（上传会失败）

**如果仍然找不到**:
1. 检查 JSON 输出中的 `missing_images` 字段
2. 手动将图片复制到 Markdown 文件同目录的 `assets/` 子目录
3. 或修改 Markdown 中的图片路径为绝对路径
```

## File: `skills/x-article-publisher/scripts/copy_to_clipboard.py`
```python
#!/usr/bin/env python3
"""
Copy image or HTML to system clipboard for X Articles publishing.

Supports:
- Image files (jpg, png, gif, webp) - copies as image data
- HTML content - copies as rich text for paste
- Optional image compression before copying

Usage:
    # Copy image to clipboard
    python copy_to_clipboard.py image /path/to/image.jpg

    # Copy image with compression (quality 0-100)
    python copy_to_clipboard.py image /path/to/image.jpg --quality 80

    # Copy HTML to clipboard
    python copy_to_clipboard.py html "<p>Hello</p>"

    # Copy HTML from file
    python copy_to_clipboard.py html --file /path/to/content.html

Requirements:
    macOS: pip install Pillow pyobjc-framework-Cocoa
    Windows: pip install Pillow pywin32 clip-util
"""

import argparse
import io
import os
import sys
from pathlib import Path


def compress_image(image_path: str, quality: int = 85, max_size: tuple = (2000, 2000)) -> bytes:
    """Compress image and return as bytes."""
    from PIL import Image

    img = Image.open(image_path)

    # Convert to RGB if necessary (for JPEG)
    if img.mode in ('RGBA', 'P'):
        img = img.convert('RGB')

    # Resize if too large
    img.thumbnail(max_size, Image.Resampling.LANCZOS)

    # Save to bytes
    buffer = io.BytesIO()
    img.save(buffer, format='JPEG', quality=quality, optimize=True)
    return buffer.getvalue()


def copy_image_to_clipboard_macos(image_path: str, quality: int = None) -> bool:
    """Copy image to macOS clipboard using AppKit."""
    try:
        from AppKit import NSPasteboard, NSPasteboardTypePNG, NSPasteboardTypeTIFF
        from Foundation import NSData

        # Compress if quality specified, otherwise use original
        if quality:
            image_data = compress_image(image_path, quality)
        else:
            with open(image_path, 'rb') as f:
                image_data = f.read()

        # Create NSData from image bytes
        ns_data = NSData.dataWithBytes_length_(image_data, len(image_data))

        # Get pasteboard and clear it
        pasteboard = NSPasteboard.generalPasteboard()
        pasteboard.clearContents()

        # Determine type based on file extension
        ext = Path(image_path).suffix.lower()
        if ext in ('.png',):
            pasteboard.setData_forType_(ns_data, NSPasteboardTypePNG)
        else:
            # For JPEG and others, use TIFF (more compatible)
            from PIL import Image
            img = Image.open(io.BytesIO(image_data))
            tiff_buffer = io.BytesIO()
            img.save(tiff_buffer, format='TIFF')
            tiff_data = NSData.dataWithBytes_length_(tiff_buffer.getvalue(), len(tiff_buffer.getvalue()))
            pasteboard.setData_forType_(tiff_data, NSPasteboardTypeTIFF)

        return True

    except ImportError as e:
        print(f"Error: Missing dependency: {e}", file=sys.stderr)
        print("Install with: pip install Pillow pyobjc-framework-Cocoa", file=sys.stderr)
        return False
    except Exception as e:
        print(f"Error copying image: {e}", file=sys.stderr)
        return False


def copy_html_to_clipboard_macos(html: str) -> bool:
    """Copy HTML to macOS clipboard as rich text."""
    try:
        from AppKit import NSPasteboard, NSPasteboardTypeHTML, NSPasteboardTypeString
        from Foundation import NSData

        # Get pasteboard and clear it
        pasteboard = NSPasteboard.generalPasteboard()
        pasteboard.clearContents()

        # Set HTML content
        html_data = html.encode('utf-8')
        ns_data = NSData.dataWithBytes_length_(html_data, len(html_data))
        pasteboard.setData_forType_(ns_data, NSPasteboardTypeHTML)

        # Also set plain text version
        pasteboard.setString_forType_(html, NSPasteboardTypeString)

        return True

    except ImportError as e:
        print(f"Error: Missing dependency: {e}", file=sys.stderr)
        print("Install with: pip install pyobjc-framework-Cocoa", file=sys.stderr)
        return False
    except Exception as e:
        print(f"Error copying HTML: {e}", file=sys.stderr)
        return False


# ============================================================================
# Windows Implementation
# ============================================================================

def copy_image_to_clipboard_windows(image_path: str, quality: int = None) -> bool:
    """Copy image to Windows clipboard using CF_DIB format."""
    try:
        import win32clipboard
        from PIL import Image

        # Load and optionally compress image
        if quality:
            image_data = compress_image(image_path, quality)
            img = Image.open(io.BytesIO(image_data))
        else:
            img = Image.open(image_path)

        # Convert to RGB (required for BMP format)
        if img.mode in ('RGBA', 'P', 'LA'):
            img = img.convert('RGB')

        # Save as BMP to BytesIO, skip 14-byte BITMAPFILEHEADER
        output = io.BytesIO()
        img.save(output, format='BMP')
        data = output.getvalue()[14:]  # Skip BITMAPFILEHEADER
        output.close()

        # Copy to clipboard
        win32clipboard.OpenClipboard()
        try:
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
        finally:
            win32clipboard.CloseClipboard()

        return True

    except ImportError as e:
        print(f"Error: Missing dependency: {e}", file=sys.stderr)
        print("Install with: pip install Pillow pywin32", file=sys.stderr)
        return False
    except Exception as e:
        print(f"Error copying image: {e}", file=sys.stderr)
        return False


def copy_html_to_clipboard_windows(html: str) -> bool:
    """Copy HTML to Windows clipboard using clip-util library."""
    try:
        from clipboard import Clipboard

        with Clipboard() as clipboard:
            clipboard["html"] = html

        return True

    except ImportError as e:
        print(f"Error: Missing dependency: {e}", file=sys.stderr)
        print("Install with: pip install clip-util", file=sys.stderr)
        return False
    except Exception as e:
        print(f"Error copying HTML: {e}", file=sys.stderr)
        return False


# ============================================================================
# Platform Detection
# ============================================================================

def copy_image_to_clipboard(image_path: str, quality: int = None) -> bool:
    """Copy image to clipboard (cross-platform)."""
    if sys.platform == 'darwin':
        return copy_image_to_clipboard_macos(image_path, quality)
    elif sys.platform == 'win32':
        return copy_image_to_clipboard_windows(image_path, quality)
    else:
        print(f"Error: Unsupported platform: {sys.platform}", file=sys.stderr)
        return False


def copy_html_to_clipboard(html: str) -> bool:
    """Copy HTML to clipboard (cross-platform)."""
    if sys.platform == 'darwin':
        return copy_html_to_clipboard_macos(html)
    elif sys.platform == 'win32':
        return copy_html_to_clipboard_windows(html)
    else:
        print(f"Error: Unsupported platform: {sys.platform}", file=sys.stderr)
        return False


def main():
    parser = argparse.ArgumentParser(description='Copy to clipboard for X Articles')
    subparsers = parser.add_subparsers(dest='type', required=True)

    # Image subcommand
    img_parser = subparsers.add_parser('image', help='Copy image to clipboard')
    img_parser.add_argument('path', help='Path to image file')
    img_parser.add_argument('--quality', type=int, default=None,
                           help='JPEG quality (1-100), enables compression')
    img_parser.add_argument('--max-width', type=int, default=2000,
                           help='Max width for resize')
    img_parser.add_argument('--max-height', type=int, default=2000,
                           help='Max height for resize')

    # HTML subcommand
    html_parser = subparsers.add_parser('html', help='Copy HTML to clipboard')
    html_parser.add_argument('content', nargs='?', help='HTML content')
    html_parser.add_argument('--file', '-f', help='Read HTML from file')

    args = parser.parse_args()

    if args.type == 'image':
        if not os.path.exists(args.path):
            print(f"Error: Image not found: {args.path}", file=sys.stderr)
            sys.exit(1)

        success = copy_image_to_clipboard(args.path, args.quality)
        if success:
            print(f"Image copied to clipboard: {args.path}")
            if args.quality:
                print(f"  (compressed with quality={args.quality})")
        sys.exit(0 if success else 1)

    elif args.type == 'html':
        if args.file:
            if not os.path.exists(args.file):
                print(f"Error: File not found: {args.file}", file=sys.stderr)
                sys.exit(1)
            with open(args.file, 'r', encoding='utf-8') as f:
                html = f.read()
        elif args.content:
            html = args.content
        else:
            # Read from stdin
            html = sys.stdin.read()

        success = copy_html_to_clipboard(html)
        if success:
            print(f"HTML copied to clipboard ({len(html)} chars)")
        sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
```

## File: `skills/x-article-publisher/scripts/parse_markdown.py`
```python
#!/usr/bin/env python3
"""
Parse Markdown for X Articles publishing.

Extracts:
- Title (from first H1/H2 or first line)
- Cover image (first image)
- Content images with block index for precise positioning
- Dividers (---) with block index for menu insertion
- HTML content (images and dividers stripped)

Usage:
    python parse_markdown.py <markdown_file> [--output json|html]

Output (JSON):
{
    "title": "Article Title",
    "cover_image": "/path/to/cover.jpg",
    "content_images": [
        {"path": "/path/to/img.jpg", "block_index": 3, "after_text": "context..."},
        ...
    ],
    "dividers": [
        {"block_index": 7, "after_text": "context..."},
        ...
    ],
    "html": "<p>Content...</p><h2>Section</h2>...",
    "total_blocks": 25
}

The block_index indicates which block element (0-indexed) the image/divider should follow.
This allows precise positioning without relying on text matching.

Note: Dividers must be inserted via X Articles' Insert > Divider menu, not HTML <hr> tags.
"""

import argparse
import json
import os
import re
import sys
import urllib.parse
from pathlib import Path


# Common search directories for missing images
SEARCH_DIRS = [
    Path.home() / "Downloads",
    Path.home() / "Desktop",
    Path.home() / "Pictures",
]


def find_image_file(original_path: str, filename: str) -> tuple[str, bool]:
    """Find an image file, searching common directories if not found at original path.
    
    Args:
        original_path: The resolved absolute path from markdown
        filename: Just the filename to search for
    
    Returns:
        (found_path, exists): The path to use and whether file exists
    """
    if os.path.isfile(original_path):
        return original_path, True
    
    for search_dir in SEARCH_DIRS:
        candidate = search_dir / filename
        if candidate.is_file():
            print(f"[parse_markdown] Image not found at '{original_path}', using '{candidate}' instead", file=sys.stderr)
            return str(candidate), True
    
    print(f"[parse_markdown] WARNING: Image not found: '{original_path}' (also searched {[str(d) for d in SEARCH_DIRS]})", file=sys.stderr)
    return original_path, False


def split_into_blocks(markdown: str) -> list[str]:
    """Split markdown into logical blocks (paragraphs, headers, quotes, code blocks, etc.)."""
    blocks = []
    current_block = []
    in_code_block = False
    code_block_lines = []

    lines = markdown.split('\n')

    for line in lines:
        stripped = line.strip()

        # Handle code block boundaries
        if stripped.startswith('```'):
            if in_code_block:
                # End of code block
                in_code_block = False
                if code_block_lines:
                    # Mark as code block with special prefix for later processing
                    # Use ___CODE_BLOCK_START___ and ___CODE_BLOCK_END___ to preserve content
                    blocks.append('___CODE_BLOCK_START___' + '\n'.join(code_block_lines) + '___CODE_BLOCK_END___')
                code_block_lines = []
            else:
                # Start of code block
                if current_block:
                    blocks.append('\n'.join(current_block))
                    current_block = []
                in_code_block = True
            continue

        # If inside code block, collect ALL lines (including empty lines)
        if in_code_block:
            code_block_lines.append(line)
            continue

        # Empty line signals end of block
        if not stripped:
            if current_block:
                blocks.append('\n'.join(current_block))
                current_block = []
            continue

        # Horizontal rule (divider) is its own block
        if re.match(r'^---+$', stripped):
            if current_block:
                blocks.append('\n'.join(current_block))
                current_block = []
            blocks.append('___DIVIDER___')
            continue

        # Headers, blockquotes are their own blocks
        if stripped.startswith(('#', '>')):
            if current_block:
                blocks.append('\n'.join(current_block))
                current_block = []
            blocks.append(stripped)
            continue

        # Image on its own line is its own block
        if re.match(r'^!\[.*\]\(.*\)$', stripped):
            if current_block:
                blocks.append('\n'.join(current_block))
                current_block = []
            blocks.append(stripped)
            continue

        current_block.append(line)

    if current_block:
        blocks.append('\n'.join(current_block))

    # Handle unclosed code block
    if code_block_lines:
        blocks.append('___CODE_BLOCK_START___' + '\n'.join(code_block_lines) + '___CODE_BLOCK_END___')

    return blocks


def extract_images_and_dividers(markdown: str, base_path: Path) -> tuple[list[dict], list[dict], str, int]:
    """Extract images and dividers with their block index positions.

    Returns:
        (image_list, divider_list, markdown_without_images_and_dividers, total_blocks)
    """
    blocks = split_into_blocks(markdown)
    images = []
    dividers = []
    clean_blocks = []

    img_pattern = re.compile(r'^!\[([^\]]*)\]\(([^)]+)\)$')

    for i, block in enumerate(blocks):
        block_stripped = block.strip()

        # Check for divider
        if block_stripped == '___DIVIDER___':
            block_index = len(clean_blocks)
            after_text = ""
            if clean_blocks:
                prev_block = clean_blocks[-1].strip()
                lines = [l for l in prev_block.split('\n') if l.strip()]
                after_text = lines[-1][:80] if lines else ""
            dividers.append({
                "block_index": block_index,
                "after_text": after_text
            })
            continue

        match = img_pattern.match(block_stripped)
        if match:
            alt_text = match.group(1)
            img_path = match.group(2)

            if not os.path.isabs(img_path):
                resolved_path = str(base_path / img_path)
            else:
                resolved_path = img_path

            filename = os.path.basename(urllib.parse.unquote(img_path))
            full_path, exists = find_image_file(resolved_path, filename)

            block_index = len(clean_blocks)

            after_text = ""
            if clean_blocks:
                prev_block = clean_blocks[-1].strip()
                lines = [l for l in prev_block.split('\n') if l.strip()]
                after_text = lines[-1][:80] if lines else ""

            images.append({
                "path": full_path,
                "original_path": resolved_path,
                "exists": exists,
                "alt": alt_text,
                "block_index": block_index,
                "after_text": after_text
            })
        else:
            clean_blocks.append(block)

    clean_markdown = '\n\n'.join(clean_blocks)
    return images, dividers, clean_markdown, len(clean_blocks)


def extract_title(markdown: str) -> tuple[str, str]:
    """Extract title from first H1, H2, or first non-empty line.

    Returns:
        (title, markdown_without_title): Title string and markdown with H1 title removed.
        If title is from H1, it's removed from markdown to avoid duplication.
    """
    lines = markdown.strip().split('\n')
    title = "Untitled"
    title_line_idx = None

    for idx, line in enumerate(lines):
        stripped = line.strip()
        if not stripped:
            continue
        # H1 - use as title and mark for removal
        if stripped.startswith('# '):
            title = stripped[2:].strip()
            title_line_idx = idx
            break
        # H2 - use as title but don't remove (it's a section header)
        if stripped.startswith('## '):
            title = stripped[3:].strip()
            break
        # First non-empty, non-image line
        if not stripped.startswith('!['):
            title = stripped[:100]
            break

    # Remove H1 title line from markdown to avoid duplication
    if title_line_idx is not None:
        lines.pop(title_line_idx)
        markdown = '\n'.join(lines)

    return title, markdown


def markdown_to_html(markdown: str) -> str:
    """Convert markdown to HTML for X Articles rich text paste."""
    html = markdown

    # Process code blocks first (marked with ___CODE_BLOCK_START___ and ___CODE_BLOCK_END___)
    # Convert to blockquote format since X Articles doesn't support <pre><code>
    def convert_code_block(match):
        code_content = match.group(1)
        lines = code_content.strip().split('\n')
        # Join non-empty lines with <br> for display
        formatted = '<br>'.join(line for line in lines if line.strip())
        return f'<blockquote>{formatted}</blockquote>'

    html = re.sub(r'___CODE_BLOCK_START___(.*?)___CODE_BLOCK_END___', convert_code_block, html, flags=re.DOTALL)

    # Headers (H2 only, H1 is title)
    html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)

    # Bold
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)

    # Italic
    html = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', html)

    # Links
    html = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', html)

    # Blockquotes (regular markdown blockquotes, not code blocks)
    html = re.sub(r'^> (.+)$', r'<blockquote>\1</blockquote>', html, flags=re.MULTILINE)

    # Unordered lists
    html = re.sub(r'^- (.+)$', r'<li>\1</li>', html, flags=re.MULTILINE)

    # Ordered lists
    html = re.sub(r'^\d+\. (.+)$', r'<li>\1</li>', html, flags=re.MULTILINE)

    # Wrap consecutive <li> in <ul>
    html = re.sub(r'((?:<li>.*?</li>\n?)+)', r'<ul>\1</ul>', html)

    # Paragraphs - split by double newlines
    parts = html.split('\n\n')
    processed_parts = []

    for part in parts:
        part = part.strip()
        if not part:
            continue
        # Skip if already a block element
        if part.startswith(('<h2>', '<h3>', '<blockquote>', '<ul>', '<ol>')):
            processed_parts.append(part)
        else:
            # Wrap in paragraph, convert single newlines to <br>
            part = part.replace('\n', '<br>')
            processed_parts.append(f'<p>{part}</p>')

    return ''.join(processed_parts)


def parse_markdown_file(filepath: str) -> dict:
    """Parse a markdown file and return structured data."""
    path = Path(filepath)
    base_path = path.parent

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip YAML frontmatter if present
    if content.startswith('---'):
        end_marker = content.find('---', 3)
        if end_marker != -1:
            content = content[end_marker + 3:].strip()

    # Extract title first (and remove H1 from markdown)
    title, content = extract_title(content)

    # Extract images and dividers with block indices
    images, dividers, clean_markdown, total_blocks = extract_images_and_dividers(content, base_path)

    # Convert to HTML
    html = markdown_to_html(clean_markdown)

    cover_image = images[0]["path"] if images else None
    cover_exists = images[0]["exists"] if images else True
    content_images = images[1:] if len(images) > 1 else []

    missing = [img for img in images if not img["exists"]]
    if missing:
        print(f"[parse_markdown] WARNING: {len(missing)} image(s) not found", file=sys.stderr)

    return {
        "title": title,
        "cover_image": cover_image,
        "cover_exists": cover_exists,
        "content_images": content_images,
        "dividers": dividers,
        "html": html,
        "total_blocks": total_blocks,
        "source_file": str(path.absolute()),
        "missing_images": len(missing)
    }


def main():
    parser = argparse.ArgumentParser(description='Parse Markdown for X Articles')
    parser.add_argument('file', help='Markdown file to parse')
    parser.add_argument('--output', choices=['json', 'html'], default='json',
                       help='Output format (default: json)')
    parser.add_argument('--html-only', action='store_true',
                       help='Output only HTML content')

    args = parser.parse_args()

    if not os.path.exists(args.file):
        print(f"Error: File not found: {args.file}", file=sys.stderr)
        sys.exit(1)

    result = parse_markdown_file(args.file)

    if args.html_only:
        print(result['html'])
    elif args.output == 'json':
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(result['html'])


if __name__ == '__main__':
    main()
```

## File: `skills/x-article-publisher/scripts/table_to_image.py`
```python
#!/usr/bin/env python3
"""
Convert Markdown table to PNG image.

For X Articles publishing when native table rendering is not supported
(X Premium tier) or when you want consistent visual styling.

Usage:
    python3 table_to_image.py <input.md> <output.png> [--scale 2]

Arguments:
    input.md    - Markdown file containing a table
    output.png  - Output PNG file path
    --scale N   - Scale factor for high-DPI displays (default: 2)

Requirements:
    pip install pillow
"""

import sys
import re
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("Error: Pillow not installed. Run: pip install pillow")
    sys.exit(1)


def parse_markdown_table(content: str) -> tuple[list[str], list[list[str]], list[str]]:
    """Parse markdown table into headers, rows, and alignments."""
    lines = [line.strip() for line in content.strip().split('\n') if line.strip()]

    if len(lines) < 2:
        raise ValueError("Table must have at least 2 rows")

    def parse_cells(line: str) -> list[str]:
        line = line.strip()
        if line.startswith('|'):
            line = line[1:]
        if line.endswith('|'):
            line = line[:-1]
        return [cell.strip() for cell in line.split('|')]

    # Find separator line
    separator_idx = -1
    for i, line in enumerate(lines):
        if re.match(r'^\|?[\s]*:?-{2,}:?[\s]*(\|[\s]*:?-{2,}:?[\s]*)*\|?$', line):
            separator_idx = i
            break

    if separator_idx > 0:
        # Has headers
        headers = parse_cells(lines[separator_idx - 1])
        sep_cells = parse_cells(lines[separator_idx])
        alignments = []
        for cell in sep_cells:
            cell = cell.strip()
            if cell.startswith(':') and cell.endswith(':'):
                alignments.append('center')
            elif cell.endswith(':'):
                alignments.append('right')
            else:
                alignments.append('left')
        rows = [parse_cells(line) for line in lines[separator_idx + 1:]]
    else:
        # No headers - all data rows
        headers = []
        rows = [parse_cells(line) for line in lines]
        alignments = ['left'] * (len(rows[0]) if rows else 0)

    return headers, rows, alignments


def get_font(size: int, bold: bool = False):
    """Get a font, falling back to default if system fonts unavailable."""
    font_paths = [
        # macOS
        "/System/Library/Fonts/SFNSMono.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
        "/Library/Fonts/Arial.ttf",
        # macOS Chinese fonts
        "/System/Library/Fonts/PingFang.ttc",
        "/System/Library/Fonts/STHeiti Light.ttc",
        # Linux
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/TTF/DejaVuSans.ttf",
        # Windows
        "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/msyh.ttc",  # Microsoft YaHei
    ]

    for path in font_paths:
        try:
            return ImageFont.truetype(path, size)
        except (OSError, IOError):
            continue

    # Fallback to default
    return ImageFont.load_default()


def render_table_to_image(
    headers: list[str],
    rows: list[list[str]],
    alignments: list[str],
    scale: int = 2
) -> Image.Image:
    """Render table data to a PIL Image."""

    # Configuration
    base_font_size = 14
    font_size = base_font_size * scale
    padding_x = 16 * scale
    padding_y = 12 * scale
    border_radius = 8 * scale
    margin = 20 * scale

    # Colors
    bg_color = (255, 255, 255)
    header_bg = (249, 250, 251)
    text_color = (55, 65, 81)
    header_text_color = (17, 24, 39)
    border_color = (229, 231, 235)

    # Fonts
    regular_font = get_font(font_size)
    bold_font = get_font(font_size, bold=True)

    # Calculate column widths
    col_count = len(headers) if headers else (len(rows[0]) if rows else 0)
    col_widths = [0] * col_count

    # Create temp image for text measurement
    temp_img = Image.new('RGB', (1, 1))
    temp_draw = ImageDraw.Draw(temp_img)

    # Measure headers
    for i, header in enumerate(headers):
        bbox = temp_draw.textbbox((0, 0), header, font=bold_font)
        col_widths[i] = max(col_widths[i], bbox[2] - bbox[0])

    # Measure data cells
    for row in rows:
        for i, cell in enumerate(row):
            if i < col_count:
                bbox = temp_draw.textbbox((0, 0), cell, font=regular_font)
                col_widths[i] = max(col_widths[i], bbox[2] - bbox[0])

    # Add padding to widths
    col_widths = [w + padding_x * 2 for w in col_widths]

    # Calculate dimensions
    row_height = font_size + padding_y * 2
    header_height = row_height if headers else 0
    table_width = sum(col_widths)
    table_height = header_height + len(rows) * row_height

    img_width = table_width + margin * 2
    img_height = table_height + margin * 2

    # Create image
    img = Image.new('RGB', (img_width, img_height), bg_color)
    draw = ImageDraw.Draw(img)

    # Draw table border (rounded rectangle)
    x0, y0 = margin, margin
    x1, y1 = margin + table_width, margin + table_height
    draw.rounded_rectangle([x0, y0, x1, y1], radius=border_radius, outline=border_color, width=scale)

    y = margin

    # Draw header
    if headers:
        # Header background
        draw.rounded_rectangle(
            [x0, y0, x1, y0 + row_height],
            radius=border_radius,
            fill=header_bg
        )
        # Cover bottom corners of header (they should be square)
        draw.rectangle([x0, y0 + row_height - border_radius, x1, y0 + row_height], fill=header_bg)

        # Header border
        draw.line([(x0, y + row_height), (x1, y + row_height)], fill=border_color, width=scale)

        # Header text
        x = margin
        for i, header in enumerate(headers):
            bbox = draw.textbbox((0, 0), header, font=bold_font)
            text_width = bbox[2] - bbox[0]

            if alignments[i] == 'center':
                text_x = x + (col_widths[i] - text_width) // 2
            elif alignments[i] == 'right':
                text_x = x + col_widths[i] - text_width - padding_x
            else:
                text_x = x + padding_x

            text_y = y + padding_y
            draw.text((text_x, text_y), header, fill=header_text_color, font=bold_font)
            x += col_widths[i]

        y += row_height

    # Draw data rows
    for row_idx, row in enumerate(rows):
        # Row border (except last row)
        if row_idx < len(rows) - 1:
            draw.line([(x0, y + row_height), (x1, y + row_height)], fill=border_color, width=scale)

        # Cell text
        x = margin
        for i, cell in enumerate(row):
            if i >= col_count:
                break

            bbox = draw.textbbox((0, 0), cell, font=regular_font)
            text_width = bbox[2] - bbox[0]

            if i < len(alignments):
                if alignments[i] == 'center':
                    text_x = x + (col_widths[i] - text_width) // 2
                elif alignments[i] == 'right':
                    text_x = x + col_widths[i] - text_width - padding_x
                else:
                    text_x = x + padding_x
            else:
                text_x = x + padding_x

            text_y = y + padding_y
            draw.text((text_x, text_y), cell, fill=text_color, font=regular_font)
            x += col_widths[i]

        y += row_height

    return img


def main():
    if len(sys.argv) < 3:
        print("Usage: python3 table_to_image.py <input.md> <output.png> [--scale N]")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    # Parse optional scale argument
    scale = 2
    if '--scale' in sys.argv:
        scale_idx = sys.argv.index('--scale')
        if scale_idx + 1 < len(sys.argv):
            try:
                scale = int(sys.argv[scale_idx + 1])
            except ValueError:
                pass

    # Read input
    content = Path(input_path).read_text()

    # Parse table
    try:
        headers, rows, alignments = parse_markdown_table(content)
    except Exception as e:
        print(f"Error parsing table: {e}")
        sys.exit(1)

    if not rows:
        print("Error: No data rows found in table")
        sys.exit(1)

    # Render image
    img = render_table_to_image(headers, rows, alignments, scale)

    # Save
    output = Path(output_path)
    img.save(output, 'PNG')
    print(f"Saved: {output} ({img.width}x{img.height})")


if __name__ == '__main__':
    main()
```

