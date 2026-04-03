---
id: github.com-op7418-nanobanana-ppt-skills-bc7d9326-k
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:07.736650
---

# KNOWLEDGE EXTRACT: github.com_op7418_NanoBanana-PPT-Skills_bc7d9326
> **Extracted on:** 2026-04-01 15:51:27
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007524805/github.com_op7418_NanoBanana-PPT-Skills_bc7d9326

---

## File: `.env.example`
```
##############################################################################
# PPT Generator Pro - 环境变量配置文件
##############################################################################
#
# 📋 使用说明：
#
# 1. 复制此文件为 .env
#    cp .env.example .env
#
# 2. 将 your-api-key-here 替换为您的实际 API 密钥
#
# 3. .env 文件不会被提交到 Git（已在 .gitignore 中配置）
#
##############################################################################

##############################################################################
# 📂 .env 文件位置说明
##############################################################################
#
# 本项目支持智能查找 .env 文件，按以下优先级搜索：
#
# 1️⃣ 脚本所在目录（最高优先级）
#    - 独立模式: ./ppt-generator/.env
#    - Skill 模式: ~/.claude/skills/ppt-generator/.env
#
# 2️⃣ 向上查找项目根目录
#    - 自动向上搜索，直到找到包含 .git 或 .env 的目录
#    - 适合项目嵌套在子目录的场景
#
# 3️⃣ 系统环境变量（最低优先级）
#    - 如果以上都未找到，从系统环境变量读取
#    - 不推荐，建议使用 .env 文件管理
#
# 🎯 推荐配置方式：
#
#   独立使用：
#     将 .env 文件放在项目根目录（与 generate_ppt.py 同级）
#
#   作为 Skill 使用：
#     将 .env 文件放在 ~/.claude/skills/ppt-generator/ 目录下
#
##############################################################################

##############################################################################
# 🔑 必需的 API 密钥
##############################################################################

# Google AI API 密钥（必需）
# 用于：使用 Nano Banana Pro (Gemini 3 Pro Image Preview) 生成 PPT 图片
# 获取地址：https://aistudio.google.com/apikey
# 免费额度：每天 15 次请求
GEMINI_API_KEY=your-gemini-api-key-here

##############################################################################
# 🎬 可选的 API 密钥（视频功能）
##############################################################################

# 可灵 AI Access Key（可选）
# 用于：生成页面间的转场视频
# 获取地址：https://klingai.com
# 说明：如果不配置，仍可使用图片生成功能，只是无法生成转场视频
KLING_ACCESS_KEY=your-kling-access-key-here

# 可灵 AI Secret Key（可选）
# 用于：配合 Access Key 使用
# 获取地址：https://klingai.com
KLING_SECRET_KEY=your-kling-secret-key-here

##############################################################################
# 📝 配置示例
##############################################################################
#
# 仅使用图片生成功能（推荐新手）：
#   GEMINI_API_KEY=AIzaSy...（填入你的真实密钥）
#   KLING_ACCESS_KEY=（留空或删除）
#   KLING_SECRET_KEY=（留空或删除）
#
# 使用完整功能（图片 + 转场视频）：
#   GEMINI_API_KEY=AIzaSy...
#   KLING_ACCESS_KEY=ak-...
#   KLING_SECRET_KEY=sk-...
#
##############################################################################

##############################################################################
# 🛡️ 安全提醒
##############################################################################
#
# ⚠️  永远不要将 .env 文件提交到 Git 仓库！
# ⚠️  永远不要在代码中硬编码 API 密钥！
# ⚠️  永远不要在公开场合分享你的 API 密钥！
#
# ✅ .env 文件已在 .gitignore 中配置，不会被 Git 跟踪
# ✅ 使用 .env.example 作为模板，保护真实密钥
# ✅ 定期检查密钥是否泄露: grep -r "AIzaSy\|ak-" .
#
##############################################################################

##############################################################################
# 📚 更多信息
##############################################################################
#
# - API 管理完整指南: API_MANAGEMENT.md
# - 环境变量配置指南: ENV_SETUP.md
# - 安全最佳实践: SECURITY.md
# - 项目完整文档: README.md
# - Skill 使用指南: SKILL.md
#
##############################################################################
```

## File: `.gitignore`
```
# Python
venv/
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
*.so
*.egg
*.egg-info/
dist/
build/

# 环境变量和密钥
.env
*.key
*.pem

# 输出文件
outputs/
*.png
*.jpg
*.jpeg

# 临时文件
*.tmp
*.log
.DS_Store
.vscode/
.idea/

# 测试文件
test_*.json
test_*.py
*_test.py
test_outputs/

# 临时工具和示例
fix_json.py
verify_new_key.py
*_plan.json

# 下载的参考文档
可灵*.md
```

## File: `ANTIGRAVITY_WORKFLOW.md`
```markdown
# PPT Generator Workflow 提示词模板

## 🎯 这是什么？

这是为内置 Nano Banana Pro 的 AI 编程软件（如 Antigravity）设计的 Global Workflow 模板。
将以下内容填写到软件的 Description 和 Content 字段中，即可实现 PPT 自动生成功能。

---

## 📝 填写说明

### Description 字段（0-250字符）

```
基于文档内容自动生成专业PPT图片。支持2种风格（渐变毛玻璃/矢量插画），16:9比例，2K/4K分辨率。智能分析文档，规划页面结构，调用Nano Banana Pro生成高质量演示文稿。适用于商务演示、教育培训、创意提案等场景。
```

**字符数**: 132/250 ✅

---

### Content 字段（0-12000字符）

```markdown
# PPT Generator Workflow

你是一个专业的PPT生成助手，负责基于用户提供的文档内容，自动生成高质量的PPT图片。

## 核心能力

- 智能文档分析和内容规划
- 调用 Nano Banana Pro 生成 16:9 高清图片
- 支持多种专业视觉风格
- 自动规划页面类型（封面/内容/数据）
- 生成2K或4K分辨率图片

## 工作流程

### 步骤1: 接收用户输入

询问用户以下信息：

1. **文档内容**
   - 询问："请提供您的文档内容，可以是文本、Markdown或文件路径"
   - 如果是文件路径，读取文件内容

2. **页数范围**
   - 询问："您希望生成多少页PPT？"
   - 选项：
     - 5页（快速演示，5分钟）
     - 5-10页（标准演示，15分钟）
     - 10-15页（深入讲解，30分钟）
     - 20-25页（完整培训，60分钟）
     - 自定义页数

3. **视觉风格**
   - 询问："请选择视觉风格："
   - 选项：
     - **渐变毛玻璃卡片风格**: 科技感，未来感，3D玻璃，霓虹渐变
     - **矢量插画风格**: 温暖可爱，扁平化，黑色轮廓线，复古配色
   - 提示适用场景帮助用户选择

4. **分辨率**
   - 询问："选择图片分辨率："
   - 选项：
     - 2K (2752x1536) - 推荐，日常使用
     - 4K (5504x3072) - 高质量，打印/大屏

### 步骤2: 文档分析与内容规划

基于文档内容和页数，规划PPT结构：

#### 规划原则

**5页结构**：
- 第1页：封面（标题+副标题）
- 第2-4页：核心内容（每页1-2个要点）
- 第5页：总结或行动建议

**5-10页结构**：
- 第1页：封面
- 第2页：目录或引言
- 第3-8页：详细内容（分章节展开）
- 第9-10页：总结+下一步

**10-15页结构**：
- 第1页：封面
- 第2-3页：引言/背景
- 第4-12页：核心内容（分3-4个章节）
- 第13-14页：案例/数据
- 第15页：总结

**20-25页结构**：
- 第1页：封面
- 第2页：目录
- 第3-5页：引言
- 第6-20页：详细内容（多个章节）
- 第21-23页：案例研究
- 第24页：关键发现
- 第25页：总结

#### 页面类型识别

为每一页分配类型：
- **cover**: 第1页封面
- **content**: 中间内容页
- **data**: 包含数据、统计、对比的页面（通常是最后1-2页）

#### 输出规划

为用户展示完整的页面规划：

```
📋 PPT内容规划（共X页）

第1页 [封面]
标题：[文档主题]
副标题：[简短描述]

第2页 [内容]
主题：[第一个核心观点]
要点：
- [要点1]
- [要点2]
- [要点3]

第3页 [内容]
...

第X页 [总结]
总结：[核心结论]
行动项：[下一步建议]
```

询问用户："这个规划是否满意？需要调整吗？"

### 步骤3: 生成提示词

为每一页生成专业的图像生成提示词。

#### 风格1: 渐变毛玻璃卡片风格

**基础提示词模板**：

```
你是一位专家级UI UX演示设计师，请生成高保真、未来科技感的16比9演示文稿幻灯片。请根据视觉平衡美学，自动在封面、网格布局或数据可视化中选择一种最完美的构图。

全局视觉语言方面，风格要无缝融合Apple Keynote的极简主义、现代SaaS产品设计和玻璃拟态风格。整体氛围需要高端、沉浸、洁净且有呼吸感。光照采用电影级体积光、柔和的光线追踪反射和环境光遮蔽。配色方案选择深邃的虚空黑或纯净的陶瓷白作为基底，并以流动的极光渐变色即霓虹紫、电光蓝、柔和珊瑚橙、青色作为背景和UI高光点缀。

关于画面内容模块，请智能整合以下元素：

1. 排版引擎采用Bento便当盒网格系统，将内容组织在模块化的圆角矩形容器中。容器材质必须是带有模糊效果的磨砂玻璃，具有精致的白色边缘和柔和的投影，并强制保留巨大的内部留白，避免拥挤。

2. 插入礼物质感的3D物体，渲染独特的高端抽象3D制品作为视觉锚点。它们的外观应像实体的昂贵礼物或收藏品，材质为抛光金属、幻彩亚克力、透明玻璃或软硅胶，形状可是悬浮胶囊、球体、盾牌、莫比乌斯环或流体波浪。

3. 字体与数据方面，使用干净的无衬线字体，建立高对比度。如果有图表，请使用发光的3D甜甜圈图、胶囊状进度条或悬浮数字，图表应看起来像发光的霓虹灯玩具。

渲染质量要求：虚幻引擎5渲染，8k分辨率，超细节纹理，UI设计感，UX界面，Dribbble热门趋势，设计奖获奖作品。
```

**封面页提示词**：

```
[基础提示词模板]

请根据视觉平衡美学，生成封面页。在中心放置一个巨大的复杂3D玻璃物体，并覆盖粗体大字：

[页面标题内容]

背景有延伸的极光波浪。
```

**内容页提示词**：

```
[基础提示词模板]

请生成内容页。使用Bento网格布局，将以下内容组织在模块化的圆角矩形容器中，容器材质必须是带有模糊效果的磨砂玻璃：

[页面内容]
```

**数据页提示词**：

```
[基础提示词模板]

请生成数据页或总结页。使用分屏设计，左侧排版以下文字，右侧悬浮巨大的发光3D数据可视化图表：

[页面内容]
```

#### 风格2: 矢量插画风格

**基础提示词模板**：

```
你是一位专家级插画设计师，请生成16比9的矢量插画风格演示文稿幻灯片。

插画风格：扁平化矢量插画（Flat Vector Illustration）。必须包含清晰、统一粗细的黑色轮廓线（Monoline/Stroke）。色彩填涂需简洁，仅使用少量阴影，严禁使用渐变色或3D渲染效果。

构图形式：横向全景式构图（Panoramic），占据版面顶部 1/3 的空间。

线条风格（Line Work）：必须使用统一粗细的黑色单线描边（Monoline/Uniform Stroke）。所有物体（建筑、植物、云朵）都必须有封闭的黑色轮廓，类似填色书的线稿风格。线条末端圆润，避免尖锐的棱角。

几何化处理（Geometric Simplification）：将复杂的物体简化为基本几何形状。例如，树木简化为棒棒糖形状或三角形，建筑物简化为简单的矩形块面，窗户简化为整齐的小方格网格。不要追求写实细节，要追求"玩具模型"般的可爱感。

空间与透视：采用平视或稍微俯视的 2.5D 视角（类似等轴测，但更自由）。通过图层的前后遮挡来表现纵深，不要使用大气透视（即远景不要变模糊或变淡），所有图层清晰度一致。

装饰元素：在空白处添加装饰性的几何元素，如放射状的线条（代表阳光或能量）、药丸形状的云朵、或者是简单的小圆点和星星，以平衡画面的视觉密度。

配色方案：复古且柔和的色调。背景使用米色/奶油色（Cream/Off-white）纸张纹理感底色。强调色使用珊瑚红、薄荷绿、芥末黄、赭石色（Burnt Orange）和岩石蓝。

字体排版：主标题使用巨大的、加粗的复古衬线体（Retro Serif），体现权威感与优雅感。副标题位于矩形色块内的全大写无衬线体。正文使用清晰易读的几何感无衬线体。
```

**封面页提示词**：

```
[基础提示词模板]

请生成封面页。在顶部1/3区域绘制横向全景式的矢量插画场景，包含几何化简化的建筑、棒棒糖树木和装饰元素。

主标题使用巨大的复古衬线体，内容为：

[页面标题内容]

背景使用米色/奶油色纸张纹理。
```

**内容页提示词**：

```
[基础提示词模板]

请生成内容页。顶部绘制横向插画装饰带。

内容区域展示以下要点，每个要点配合简洁的矢量图标，所有元素都有统一的黑色轮廓线：

[页面内容]

使用彩色矩形块（珊瑚红、薄荷绿、芥末黄）分隔不同要点。
```

**数据页提示词**：

```
[基础提示词模板]

请生成数据页。使用几何化的矢量图表形式展示以下数据，所有图表元素都有清晰的黑色轮廓：

[页面内容]

配色使用复古柔和色调，添加装饰性的几何元素（小圆点、星星、放射线）平衡画面。
```

### 步骤4: 调用 Nano Banana Pro 生成图片

对于每一页，执行以下操作：

1. **显示进度**
   ```
   🎨 正在生成第 X/总页数 页...
   页面类型：[封面/内容/数据]
   内容主题：[简短描述]
   ```

2. **调用 Nano Banana Pro**
   - 使用生成的提示词
   - 配置参数：
     ```
     model: "gemini-3-pro-image-preview"
     aspect_ratio: "16:9"
     image_size: "2K" 或 "4K"（根据用户选择）
     ```

3. **保存图片**
   - 文件名格式：`slide-{页码:02d}.png`
   - 例如：`slide-01.png`, `slide-02.png`, ...

4. **错误处理**
   - 如果某页生成失败，记录失败信息
   - 继续生成下一页
   - 最后汇总失败的页面，询问是否重新生成

### 步骤5: 生成结果汇总

生成完成后，向用户展示：

```
✅ PPT生成完成！

📊 生成统计：
- 总页数：X 页
- 成功：X 页
- 失败：X 页
- 总用时：约 X 分钟

📁 生成的文件：
slide-01.png - 封面：[标题]
slide-02.png - 内容：[主题]
...
slide-XX.png - 总结：[主题]

💡 使用建议：
1. 所有图片已按顺序命名（slide-01 到 slide-XX）
2. 可以直接导入到演示软件（Keynote、PowerPoint等）
3. 也可以在网页中按顺序展示

🔄 后续操作：
- 重新生成失败的页面
- 调整特定页面的内容
- 生成不同风格的版本
```

### 步骤6: 提供后续支持

询问用户是否需要：

1. **重新生成特定页面**
   - "需要重新生成哪些页面？"
   - 提供页码选择

2. **调整内容**
   - "需要修改哪页的内容？"
   - 接收新内容并重新生成

3. **生成其他风格**
   - "想尝试另一种风格吗？"
   - 使用相同的内容规划，切换风格重新生成

4. **生成HTML播放器**（可选）
   - 如果系统支持，生成简单的HTML文件用于预览

## 关键注意事项

### 提示词优化

1. **保持一致性**
   - 所有页面使用同一风格的基础模板
   - 确保视觉语言统一

2. **内容适配**
   - 根据内容长度调整布局
   - 避免单页信息过载（最多3-5个要点）

3. **中英文处理**
   - 提示词可以包含中文内容
   - Nano Banana Pro 支持多语言

### 图片质量控制

1. **分辨率选择**
   - 2K：日常演示，快速生成（推荐）
   - 4K：打印输出，大屏展示

2. **纵横比固定**
   - 始终使用 16:9 比例
   - 这是标准PPT比例

3. **文件大小**
   - 2K 约 2-3MB/页
   - 4K 约 8-10MB/页

### 用户体验优化

1. **进度反馈**
   - 实时显示生成进度
   - 预估剩余时间

2. **错误提示**
   - 清晰说明失败原因
   - 提供解决方案

3. **灵活调整**
   - 允许用户中途修改规划
   - 支持迭代优化

## 示例对话流程

**用户**：我想生成一个关于"AI产品设计原则"的PPT

**助手**：好的！我来帮您生成。首先需要了解一些信息：

1. 请提供您的文档内容或要点
2. 您希望生成多少页PPT？（5页/5-10页/10-15页/20-25页）
3. 选择视觉风格：
   - 渐变毛玻璃卡片风格（科技感，适合商务演示）
   - 矢量插画风格（温暖可爱，适合教育培训）
4. 图片分辨率：2K（推荐）或 4K？

**用户**：5页，渐变毛玻璃卡片风格，2K

内容：
- 什么是好的AI产品
- 用户需求优先
- 简单胜过复杂
- 数据驱动决策
- 持续迭代优化

**助手**：明白了！让我为您规划内容：

📋 PPT内容规划（共5页）

第1页 [封面]
标题：AI产品设计原则
副标题：打造用户喜爱的智能产品

第2页 [内容]
什么是好的AI产品
- 解决真实问题
- 易于使用
- 持续进化

第3页 [内容]
用户需求优先 + 简单胜过复杂
- 深入理解用户痛点
- 避免过度设计
- 清晰的信息架构

第4页 [内容]
数据驱动决策
- A/B测试
- 用户行为分析
- 指标监控

第5页 [数据]
持续迭代优化
- 快速试错
- 用户反馈循环
- 版本演进路线图

这个规划是否满意？

**用户**：很好，开始生成吧

**助手**：
🎨 开始生成，请稍候...

🎨 正在生成第 1/5 页...
页面类型：封面
✓ 第1页生成完成：slide-01.png

🎨 正在生成第 2/5 页...
页面类型：内容
✓ 第2页生成完成：slide-02.png

...

✅ PPT生成完成！

📊 生成统计：
- 总页数：5 页
- 成功：5 页
- 失败：0 页
- 总用时：约 2.5 分钟

## 总结

此 Workflow 将：

1. ✅ 智能分析文档内容
2. ✅ 根据页数规划结构
3. ✅ 选择合适的视觉风格
4. ✅ 生成专业的图像提示词
5. ✅ 调用 Nano Banana Pro 生成图片
6. ✅ 提供完整的结果汇总
7. ✅ 支持迭代优化

用户只需提供文档内容和基本偏好，即可获得完整的专业PPT图片！
```

**字符数**: 约11,500/12,000 ✅

---

## 🎯 填写步骤总结

1. **打开软件中的 Global Workflows 编辑器**
   - 路径：`.gemini > antigravity > global_workflows`
   - 创建新文件：`ppt-generator.md`

2. **填写 Description 字段**
   - 复制上面的 Description 内容（132字符）
   - 粘贴到软件的 Description 输入框

3. **填写 Content 字段**
   - 复制上面完整的 Content Markdown 内容（约11,500字符）
   - 粘贴到软件的 Content 输入框

4. **保存并测试**
   - 保存 Workflow
   - 测试调用，确保功能正常

---

## 💡 与 Claude Code Skill 的对比

| 特性 | Claude Code Skill | Antigravity Workflow |
|------|------------------|---------------------|
| 安装方式 | 需要手动安装Python环境 | 内置，无需安装 |
| API调用 | 自己配置API密钥 | 内置Nano Banana Pro |
| 文件管理 | 生成文件到本地 | 自动管理 |
| 播放器 | 自带HTML5播放器 | 需自行实现 |
| 灵活性 | 可自定义脚本 | 基于Workflow规则 |
| 适用场景 | 开发者，需要完全控制 | 普通用户，快速使用 |

两种方案各有优势，可根据实际需求选择！

---

## 📚 参考资源

- **风格定义**: 参考 `styles/gradient-glass.md` 和 `styles/vector-illustration.md`
- **GitHub仓库**: https://github.com/op7418/NanoBanana-PPT-Skills
- **创作者**: 歸藏 [@op7418](https://github.com/op7418)
```

## File: `API_MANAGEMENT.md`
```markdown
# API 密钥管理规范

## 📋 当前配置

### API 存储位置

所有 API 密钥现在统一存储在：

```
📁 ppt-generator/.env
```

### ✅ 安全验证

- ✅ `.env` 文件已创建
- ✅ 已被 `.gitignore` 保护（第15行规则）
- ✅ 不会被提交到 Git
- ✅ `run.sh` 可以正确加载

### 🎯 使用方法

**无需任何额外配置！** 直接使用即可：

```bash
./run.sh --plan slides_plan.json --style styles/gradient-glass.md --resolution 2K
```

输出显示：
```
📌 从 .env 文件加载API密钥
```

---

## 🔐 API 管理规范

### 1️⃣ 添加新的 API 密钥

编辑 `.env` 文件：

```bash
# 使用编辑器打开
nano .env

# 或使用 VS Code
code .env
```

按照以下格式添加：

```bash
# API 名称说明
# 用途：描述这个 API 的用途
# 获取地址：https://...
API_NAME=your-api-key-here
```

**示例**：

```bash
# OpenAI API
# 用途：未来可能用于文档分析
# 获取地址：https://platform.openai.com/api-keys
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxx
```

### 2️⃣ 在代码中使用 API 密钥

**❌ 错误做法**（硬编码）：

```python
# 绝对不要这样做！
api_key = "AIzaSyAfHE4vctPhMF2mVn96aEZZp8WuURlaGpM"
```

**✅ 正确做法**（从环境变量读取）：

```python
import os

# 从环境变量读取
api_key = os.environ.get("GEMINI_API_KEY")

# 或带默认值
api_key = os.getenv("GEMINI_API_KEY", "")

# 检查是否存在
if not api_key:
    raise ValueError("未找到 GEMINI_API_KEY 环境变量")
```

### 3️⃣ 环境变量加载优先级

`run.sh` 的加载逻辑：

```
1. 系统环境变量（~/.zshrc 等）
   ↓ 如果没有
2. .env 文件
   ↓ 如果都没有
3. 报错提示用户配置
```

这意味着：
- ✅ CI/CD 环境可以使用系统环境变量
- ✅ 本地开发使用 .env 文件
- ✅ 灵活切换不同环境的密钥

### 4️⃣ 多环境管理

如果需要管理多个环境（开发/测试/生产）：

```bash
# 开发环境
.env.development

# 测试环境
.env.test

# 生产环境
.env.production
```

使用时指定：

```bash
# 复制对应环境的配置
cp .env.development .env

# 或使用符号链接
ln -sf .env.development .env
```

---

## 📝 .env 文件结构

### 当前结构

```bash
.env
├─ [注释区域]
│  ├─ 安全提醒
│  ├─ 使用说明
│  └─ 加载优先级说明
│
├─ [主要 API 密钥]
│  └─ GEMINI_API_KEY (已配置)
│
├─ [备用 API 密钥]
│  ├─ OPENAI_API_KEY (注释状态)
│  ├─ ANTHROPIC_API_KEY (注释状态)
│  └─ STABILITY_API_KEY (注释状态)
│
└─ [项目配置]
   ├─ DEFAULT_RESOLUTION (注释状态)
   ├─ DEFAULT_STYLE (注释状态)
   └─ OUTPUT_DIR (注释状态)
```

### 字段说明

| 变量名 | 状态 | 用途 | 获取地址 |
|--------|------|------|----------|
| `GEMINI_API_KEY` | ✅ 已配置 | Nano Banana Pro 图像生成 | [Google AI Studio](https://makersuite.google.com/app/apikey) |
| `OPENAI_API_KEY` | 💤 预留 | 未来可能用于文档分析 | [OpenAI Platform](https://platform.openai.com/api-keys) |
| `ANTHROPIC_API_KEY` | 💤 预留 | 未来可能用于Claude API | [Anthropic Console](https://console.anthropic.com/) |
| `STABILITY_API_KEY` | 💤 预留 | 未来可能用于其他图像模型 | [Stability AI](https://platform.stability.ai/) |

---

## 🚨 安全检查清单

### 开发时

- [ ] 从不在代码中硬编码 API 密钥
- [ ] 使用 `os.environ.get()` 或 `os.getenv()` 读取
- [ ] 添加密钥缺失时的错误提示
- [ ] 在函数/类初始化时读取，不要每次请求都读

### 提交前

- [ ] 运行 `git status` 确认 .env 不在列表中
- [ ] 运行 `grep -r "AIzaSy" --exclude-dir=.git .` 无输出
- [ ] 检查 `.gitignore` 包含 `.env`
- [ ] 代码中无任何硬编码的密钥

### 分享项目时

- [ ] 提供 `.env.example` 作为模板
- [ ] 在 README 中说明如何配置
- [ ] 不要通过聊天/邮件发送 .env 文件
- [ ] 建议用户使用自己的 API 密钥

---

## 💡 最佳实践

### 1. 密钥轮换

定期更新 API 密钥（建议 3-6 个月）：

```bash
# 1. 在 API 平台生成新密钥
# 2. 更新 .env 文件
# 3. 测试功能正常
# 4. 撤销旧密钥
```

### 2. 密钥权限

为不同用途创建不同的 API 密钥：

```bash
# 开发用（限制配额）
GEMINI_API_KEY_DEV=...

# 生产用（完整权限）
GEMINI_API_KEY_PROD=...
```

### 3. 错误处理

代码中添加友好的错误提示：

```python
import os
import sys

def get_api_key(key_name):
    """安全获取 API 密钥"""
    api_key = os.getenv(key_name)

    if not api_key:
        print(f"❌ 错误: 未找到 {key_name} 环境变量")
        print("")
        print("请配置 API 密钥：")
        print("1. 编辑 .env 文件")
        print("2. 添加：{key_name}=your-key")
        print("3. 保存并重新运行")
        sys.exit(1)

    return api_key

# 使用
gemini_key = get_api_key("GEMINI_API_KEY")
```

### 4. 日志安全

不要在日志中输出完整密钥：

```python
# ❌ 危险
print(f"Using API key: {api_key}")

# ✅ 安全
print(f"Using API key: {api_key[:8]}...{api_key[-4:]}")
# 输出: Using API key: AIzaSyAf...GpM
```

---

## 🔄 迁移指南

### 从系统环境变量迁移到 .env

如果您之前在 `~/.zshrc` 中配置了密钥：

**步骤1**: 从 .zshrc 删除

```bash
# 编辑配置文件
nano ~/.zshrc

# 删除这一行
export GEMINI_API_KEY="..."

# 重新加载
source ~/.zshrc
```

**步骤2**: 添加到 .env

```bash
# .env 文件已包含密钥，无需额外操作
```

**步骤3**: 测试

```bash
./run.sh --help
# 应该显示：📌 从 .env 文件加载API密钥
```

### 从 .env 迁移到系统环境变量

如果您想使用系统环境变量（跨项目共享）：

```bash
# 1. 复制 .env 中的密钥
cat .env | grep GEMINI_API_KEY

# 2. 添加到 .zshrc
echo 'export GEMINI_API_KEY="..."' >> ~/.zshrc

# 3. 重新加载
source ~/.zshrc

# 4. 测试
./run.sh --help
# 应该显示：✅ 使用系统环境变量中的API密钥
```

---

## 📚 相关文档

- **SECURITY.md** - 完整的安全指南
- **ENV_SETUP.md** - 环境变量配置详解
- **.env.example** - 配置模板
- **README.md** - 项目使用说明

---

## 🆘 常见问题

### Q: .env 文件在哪里？

A: 在项目根目录 `ppt-generator/.env`

### Q: 如何查看我的 API 密钥？

A:
```bash
cat .env | grep GEMINI_API_KEY
```

### Q: 可以提交 .env 文件吗？

A: **绝对不可以！** .env 文件包含敏感信息，已被 .gitignore 保护。

### Q: 团队协作时如何共享配置？

A:
1. 提交 `.env.example` 模板
2. 团队成员复制为 `.env`
3. 各自填入自己的 API 密钥

### Q: 如何知道密钥是从哪里加载的？

A: 运行任何命令时查看输出：
- `✅ 使用系统环境变量中的API密钥` - 从系统加载
- `📌 从 .env 文件加载API密钥` - 从 .env 加载

---

## ✅ 总结

### 当前配置

✅ **API 密钥统一管理**
- 存储位置：`ppt-generator/.env`
- 安全保护：`.gitignore` 规则
- 自动加载：`run.sh` 脚本

✅ **开发规范**
- 不在代码中硬编码
- 使用 `os.getenv()` 读取
- 添加错误处理
- 日志中不输出完整密钥

✅ **安全保证**
- .env 不会提交到 Git
- .env.example 作为模板
- 定期轮换密钥
- 不同环境使用不同密钥

### 立即可用

现在您可以直接开始迭代功能，所有 API 配置都已就绪！

```bash
# 直接使用
./run.sh --plan your_plan.json --style styles/gradient-glass.md
```

---

**创建日期**: 2026-01-11
**最后更新**: 2026-01-11
**创作者**: 歸藏
```

## File: `ARCHITECTURE.md`
```markdown
# PPT Generator Pro 架构文档

## 📐 系统架构图

```mermaid
graph TB
    %% 用户输入
    User[👤 用户] -->|文档内容| Input[📝 输入处理]
    
    %% 输入处理
    Input --> Plan[📋 内容规划<br/>slides_plan.json]
    
    %% 核心模块
    Plan --> PPTGen[🎨 PPT 图片生成模块<br/>generate_ppt.py]
    Plan --> VideoGen[🎬 视频生成模块<br/>generate_ppt_video.py]
    
    %% PPT 图片生成流程
    PPTGen --> StyleLoader[🎨 风格加载器<br/>styles/*.md]
    StyleLoader --> PromptEngine[✍️ 提示词引擎]
    PromptEngine --> NanoBanana[🤖 Nano Banana Pro API<br/>Google Gemini]
    NanoBanana --> Images[🖼️ PPT 图片<br/>slide-01.png ~ slide-N.png]
    
    %% 视频生成流程
    VideoGen --> TransPrompt[📝 转场提示词生成器<br/>transition_prompt_generator.py]
    TransPrompt --> KlingAPI[🎬 可灵 AI API<br/>kling_api.py]
    KlingAPI --> PreviewVideo[🔄 预览视频<br/>preview.mp4]
    KlingAPI --> TransVideos[🎞️ 转场视频<br/>transition_01_to_02.mp4]
    
    %% 视频合成
    Images --> VideoMat[📦 视频素材管理<br/>video_materials.py]
    PreviewVideo --> VideoMat
    TransVideos --> VideoMat
    
    VideoMat --> Composer[🎬 FFmpeg 视频合成器<br/>video_composer.py]
    Composer --> FullVideo[🎥 完整视频<br/>full_ppt_video.mp4]
    
    %% 播放器生成
    Images --> ImgPlayer[🎮 图片播放器<br/>templates/viewer.html]
    VideoMat --> VidPlayer[🎮 视频播放器<br/>templates/video_viewer.html]
    
    %% 输出
    ImgPlayer --> Output1[📤 输出 1: 图片版<br/>index.html + images/]
    VidPlayer --> Output2[📤 输出 2: 视频版<br/>video_index.html + videos/]
    FullVideo --> Output3[📤 输出 3: 完整视频<br/>full_ppt_video.mp4]
    
    Output1 --> User
    Output2 --> User
    Output3 --> User
    
    %% 样式定义
    classDef userNode fill:#e1f5ff,stroke:#0288d1,stroke-width:2px
    classDef inputNode fill:#fff9c4,stroke:#f9a825,stroke-width:2px
    classDef coreNode fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px
    classDef apiNode fill:#ffebee,stroke:#c62828,stroke-width:2px
    classDef outputNode fill:#e8f5e9,stroke:#388e3c,stroke-width:2px
    
    class User userNode
    class Input,Plan inputNode
    class PPTGen,VideoGen,StyleLoader,PromptEngine,TransPrompt,VideoMat,Composer coreNode
    class NanoBanana,KlingAPI apiNode
    class Images,PreviewVideo,TransVideos,FullVideo,ImgPlayer,VidPlayer,Output1,Output2,Output3 outputNode
```

## 🏗️ 模块架构

### 1️⃣ 核心生成模块

```
┌─────────────────────────────────────────────────────────────┐
│                    PPT Generator Pro                         │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌────────────────────┐        ┌──────────────────────┐    │
│  │  图片生成模块      │        │   视频生成模块       │    │
│  │  generate_ppt.py   │        │ generate_ppt_video.py│    │
│  └────────────────────┘        └──────────────────────┘    │
│           │                              │                  │
│           ▼                              ▼                  │
│  ┌────────────────────┐        ┌──────────────────────┐    │
│  │  风格系统          │        │  转场提示词生成      │    │
│  │  styles/*.md       │        │ transition_prompt_   │    │
│  │                    │        │   generator.py       │    │
│  └────────────────────┘        └──────────────────────┘    │
│           │                              │                  │
│           ▼                              ▼                  │
│  ┌────────────────────┐        ┌──────────────────────┐    │
│  │ Nano Banana Pro    │        │   可灵 AI API        │    │
│  │ (Gemini 3 Pro)     │        │   kling_api.py       │    │
│  └────────────────────┘        └──────────────────────┘    │
│           │                              │                  │
│           ▼                              ▼                  │
│    🖼️ PPT 图片                    🎬 转场视频               │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 2️⃣ 视频合成模块

```
┌─────────────────────────────────────────────────────────────┐
│               FFmpeg 视频合成流程                            │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  输入素材:                                                   │
│  ├── 📷 PPT 图片 (slide-01.png ~ slide-N.png)              │
│  ├── 🔄 预览视频 (preview.mp4)                              │
│  └── 🎞️ 转场视频 (transition_XX_to_YY.mp4)                 │
│                                                              │
│  ┌────────────────────────────────────────────────┐         │
│  │     video_materials.py - 素材管理             │         │
│  │  • 收集所有素材                                │         │
│  │  • 验证文件完整性                              │         │
│  │  • 组织素材顺序                                │         │
│  └────────────────────────────────────────────────┘         │
│                       │                                      │
│                       ▼                                      │
│  ┌────────────────────────────────────────────────┐         │
│  │     video_composer.py - FFmpeg 合成器         │         │
│  │                                                │         │
│  │  步骤 1: 图片转静态视频                        │         │
│  │    • 转换为 2 秒静态视频                       │         │
│  │    • 统一分辨率 1920x1080                      │         │
│  │    • 统一帧率 24fps                            │         │
│  │                                                │         │
│  │  步骤 2: 标准化所有视频                        │         │
│  │    • 缩放到统一分辨率                          │         │
│  │    • 添加黑边保持宽高比                        │         │
│  │    • 统一帧率                                  │         │
│  │                                                │         │
│  │  步骤 3: 拼接视频序列                          │         │
│  │    预览 → 转场01-02 → 静态02 → 转场02-03...   │         │
│  │                                                │         │
│  │  步骤 4: H.264 编码输出                        │         │
│  └────────────────────────────────────────────────┘         │
│                       │                                      │
│                       ▼                                      │
│              🎥 full_ppt_video.mp4                          │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

### 3️⃣ 播放器系统

```
┌─────────────────────────────────────────────────────────────┐
│                   播放器架构                                 │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌───────────────────────┐    ┌────────────────────────┐   │
│  │  图片播放器           │    │   视频播放器           │   │
│  │  viewer.html          │    │   video_viewer.html    │   │
│  ├───────────────────────┤    ├────────────────────────┤   │
│  │                       │    │                        │   │
│  │  • 图片轮播           │    │  • 视频+图片混合       │   │
│  │  • 键盘导航           │    │  • 智能转场            │   │
│  │  • 全屏支持           │    │  • 预览模式            │   │
│  │  • 触摸滑动           │    │  • 状态管理            │   │
│  │  • 自动播放           │    │  • 键盘控制            │   │
│  │                       │    │                        │   │
│  └───────────────────────┘    └────────────────────────┘   │
│           │                              │                  │
│           ▼                              ▼                  │
│   📁 outputs/TIMESTAMP/        📁 outputs/TIMESTAMP_video/  │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## 🔄 数据流图

```
┌──────────────────────────────────────────────────────────────────┐
│                         完整工作流                                │
└──────────────────────────────────────────────────────────────────┘

1️⃣ 内容输入阶段
   用户文档 → Claude 分析 → slides_plan.json
   
2️⃣ 图片生成阶段
   slides_plan.json → 风格提示词 → Nano Banana Pro → PPT 图片
   
3️⃣ 视频生成阶段 (可选)
   PPT 图片 → 转场提示词 → 可灵 AI → 转场视频
   
4️⃣ 播放器生成阶段
   素材集合 → HTML 模板 → 交互式播放器
   
5️⃣ 完整视频合成阶段 (可选)
   所有素材 → FFmpeg → 完整视频文件
```

## 📦 文件组织结构

```
ppt-generator-pro/
│
├── 🎯 核心脚本
│   ├── generate_ppt.py              # PPT 图片生成主程序
│   ├── generate_ppt_video.py        # 视频生成主程序
│   ├── kling_api.py                 # 可灵 AI API 封装
│   ├── video_composer.py            # FFmpeg 视频合成
│   ├── video_materials.py           # 素材管理
│   └── transition_prompt_generator.py # 转场提示词生成
│
├── 🎨 风格系统
│   └── styles/
│       ├── gradient-glass.md        # 渐变毛玻璃风格
│       └── vector-illustration.md   # 矢量插画风格
│
├── 🎮 播放器模板
│   └── templates/
│       ├── viewer.html              # 图片播放器
│       └── video_viewer.html        # 视频播放器
│
├── 📝 提示词模板
│   └── prompts/
│       └── transition_base.md       # 转场提示词基础
│
├── ⚙️ 配置文件
│   ├── .env                         # API 密钥配置
│   └── .env.example                 # 配置模板
│
└── 📤 输出目录
    └── outputs/
        ├── TIMESTAMP/               # 图片版本
        │   ├── images/             # PPT 图片
        │   ├── index.html          # 图片播放器
        │   └── prompts.json        # 提示词记录
        └── TIMESTAMP_video/         # 视频版本
            ├── videos/             # 转场视频
            ├── video_index.html    # 视频播放器
            └── full_ppt_video.mp4  # 完整视频
```

## 🔌 API 集成架构

```
┌─────────────────────────────────────────────────────────────┐
│                      API 集成层                              │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌──────────────────────┐      ┌───────────────────────┐   │
│  │  Google Gemini API   │      │    可灵 AI API        │   │
│  ├──────────────────────┤      ├───────────────────────┤   │
│  │                      │      │                       │   │
│  │  • Nano Banana Pro   │      │  • 图生视频 (i2v)    │   │
│  │  • 图像生成          │      │  • 视频生成           │   │
│  │  • 提示词工程        │      │  • 数字人生成         │   │
│  │  • 风格控制          │      │  • 主体库             │   │
│  │  • 分辨率控制        │      │  • 专业/创意模式      │   │
│  │                      │      │                       │   │
│  └──────────────────────┘      └───────────────────────┘   │
│           ▲                              ▲                  │
│           │                              │                  │
│  ┌────────┴───────────┐      ┌──────────┴────────────┐    │
│  │  GEMINI_API_KEY    │      │  KLING_ACCESS_KEY     │    │
│  │  (必需)            │      │  KLING_SECRET_KEY     │    │
│  │                    │      │  (可选)               │    │
│  └────────────────────┘      └───────────────────────┘    │
│           ▲                              ▲                  │
│           └──────────────┬───────────────┘                 │
│                          │                                  │
│                    ┌─────┴──────┐                          │
│                    │  .env 文件  │                          │
│                    └────────────┘                          │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## 🎬 视频播放器交互流程

```
┌─────────────────────────────────────────────────────────────┐
│            视频播放器 (VideoPPTPlayer) 状态机               │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│      ┌──────────────────────────────────┐                  │
│      │      初始状态: 预览模式          │                  │
│      │   🔄 播放 preview.mp4 (循环)    │                  │
│      └──────────────────────────────────┘                  │
│                     │                                        │
│                     │ 用户按右键 →                          │
│                     ▼                                        │
│      ┌──────────────────────────────────┐                  │
│      │      转场状态 (01→02)            │                  │
│      │   🎞️ 播放 transition_01_to_02   │                  │
│      │      isTransitioning = true      │                  │
│      └──────────────────────────────────┘                  │
│                     │                                        │
│                     │ 视频结束 →                            │
│                     ▼                                        │
│      ┌──────────────────────────────────┐                  │
│      │      静态页面状态 (页面2)        │                  │
│      │   🖼️ 显示 slide-02.png          │                  │
│      │      currentSlide = 1            │                  │
│      │      isPreviewMode = false       │                  │
│      └──────────────────────────────────┘                  │
│                     │                                        │
│                     │ 用户按右键 →                          │
│                     ▼                                        │
│      ┌──────────────────────────────────┐                  │
│      │      转场状态 (02→03)            │                  │
│      │   🎞️ 播放 transition_02_to_03   │                  │
│      └──────────────────────────────────┘                  │
│                     │                                        │
│                     │ 视频结束 →                            │
│                     ▼                                        │
│      ┌──────────────────────────────────┐                  │
│      │      静态页面状态 (页面3)        │                  │
│      │   🖼️ 显示 slide-03.png          │                  │
│      └──────────────────────────────────┘                  │
│                     │                                        │
│                     │ 循环继续...                           │
│                     ▼                                        │
│                                                              │
└─────────────────────────────────────────────────────────────┘

关键状态变量:
• isPreviewMode: 是否在预览模式
• isTransitioning: 是否在播放转场视频
• currentSlide: 当前幻灯片索引
```

## 🛠️ 技术栈

```
┌─────────────────────────────────────────────────────────────┐
│                        技术栈                                │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  后端 (Python 3.8+)                                         │
│  ├── google-genai       # Google Gemini API 客户端         │
│  ├── pillow            # 图像处理                           │
│  └── requests          # HTTP 请求                          │
│                                                              │
│  视频处理                                                    │
│  └── FFmpeg            # 视频编码、转换、合成               │
│                                                              │
│  前端 (HTML5 + JavaScript)                                  │
│  ├── 原生 JavaScript    # 播放器逻辑                        │
│  ├── HTML5 Video       # 视频播放                           │
│  └── CSS3              # 样式和动画                         │
│                                                              │
│  AI 服务                                                     │
│  ├── Google Nano Banana Pro (Gemini 3 Pro Image Preview)   │
│  └── 可灵 AI (Kling AI)                                    │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## 📊 性能指标

```
生成速度:
├── PPT 图片: ~30秒/页 (2K) | ~60秒/页 (4K)
├── 转场视频: ~30-60秒/段 (可灵 AI)
└── 视频合成: ~5-10秒 (FFmpeg, 取决于页数)

文件大小:
├── PPT 图片: ~2.5MB/页 (2K) | ~8MB/页 (4K)
├── 转场视频: ~3-5MB/段 (1080p, 5秒)
└── 完整视频: ~12-20MB (5页 PPT + 转场)

质量参数:
├── 图片: 2752x1536 (2K) | 5504x3072 (4K)
├── 视频: 1920x1080, 24fps, H.264
└── 编码: CRF 23 (高质量)
```

---

## 🎯 使用流程总结

### 基础流程（仅图片）
```
用户文档 → 内容规划 → 生成图片 → 图片播放器 → ✅
```

### 完整流程（图片 + 视频）
```
用户文档 → 内容规划 → 生成图片 → 生成转场视频 
         → 视频播放器 + 完整视频 → ✅
```

### 快速流程（使用完整视频）
```
用户文档 → 内容规划 → 生成图片 → 生成视频 
         → 导出 MP4 → 直接分享 → ✅
```

---

<div align="center">

**🏗️ 架构设计原则**

模块化 • 可扩展 • 高内聚低耦合 • API 驱动

Made with ❤️ by 歸藏

</div>
```

## File: `ENV_SETUP.md`
```markdown
# 系统环境变量配置指南

## ✅ 当前配置状态

您的项目现在使用**系统环境变量**来管理API密钥，这是最安全的方案！

### 🎯 优势对比

| 方案 | 安全性 | 便利性 | Git安全 |
|------|--------|--------|---------|
| 硬编码 | ❌ 极低 | ✓ 方便 | ❌ 会泄露 |
| .env文件 | ⚠️ 中等 | ✓ 方便 | ⚠️ 需配置.gitignore |
| **系统环境变量** | ✅ **高** | ✅ **最方便** | ✅ **完全安全** |

## 📋 已完成的配置

### 1. 系统环境变量 ✅

API密钥已添加到您的 `~/.zshrc` 文件中：

```bash
# Google AI API Key for PPT Generator
export GEMINI_API_KEY="your-api-key-here"
```

**验证方法**：
```bash
echo $GEMINI_API_KEY
# 应显示您的API密钥
```

### 2. run.sh 智能识别 ✅

启动脚本已更新，优先级顺序：
1. **系统环境变量**（最高优先级）✅
2. .env 文件（备用方案）

当您运行 `./run.sh` 时，会显示：
```
✅ 使用系统环境变量中的API密钥
```

### 3. 项目文件清理 ✅

- ✅ `.env` 文件已删除
- ✅ `.env.example` 保留（作为模板）
- ✅ `run.sh` 不包含硬编码密钥
- ✅ 所有文档使用占位符

## 🔐 Git提交安全性

### 现在提交到GitHub，绝对安全！

**不会被提交的内容**：
- ❌ API密钥（存储在系统环境变量中）
- ❌ `.env` 文件（已删除且在.gitignore中）
- ❌ 虚拟环境（venv/）
- ❌ 输出文件（outputs/）

**会被提交的内容（全部安全）**：
- ✅ `.env.example` - 仅包含模板
- ✅ `.gitignore` - Git忽略规则
- ✅ `run.sh` - 从环境变量读取密钥
- ✅ `generate_ppt.py` - Python脚本
- ✅ 所有文档和风格文件

### 验证命令

```bash
# 搜索项目中的API密钥
grep -r "AIzaSy" --exclude-dir=.git --exclude-dir=venv .

# 应该没有任何输出！✅
```

## 🚀 使用方法

### 在当前项目中使用

直接运行即可，会自动使用系统环境变量：

```bash
./run.sh --plan ../test_slides_plan.json --style styles/gradient-glass.md --resolution 2K
```

输出显示：
```
✅ 使用系统环境变量中的API密钥
```

### 在其他机器上使用

当您在新机器上克隆项目时：

**步骤1**: 克隆仓库
```bash
git clone https://github.com/你的用户名/ppt-generator.git
cd ppt-generator
```

**步骤2**: 配置环境变量（根据Shell选择）

**zsh用户**（推荐）：
```bash
echo 'export GEMINI_API_KEY="your-api-key"' >> ~/.zshrc
source ~/.zshrc
```

**bash用户**：
```bash
echo 'export GEMINI_API_KEY="your-api-key"' >> ~/.bashrc
source ~/.bashrc
```

**fish用户**：
```bash
set -Ux GEMINI_API_KEY "your-api-key"
```

**步骤3**: 安装依赖并运行
```bash
python3 -m venv venv
source venv/bin/activate
pip install google-genai pillow
./run.sh --help
```

## 🔄 管理API密钥

### 查看当前密钥

```bash
echo $GEMINI_API_KEY
```

### 临时修改密钥（当前会话）

```bash
export GEMINI_API_KEY="new-key-here"
```

### 永久修改密钥

编辑配置文件：
```bash
nano ~/.zshrc  # 或使用你喜欢的编辑器
```

找到这一行并修改：
```bash
export GEMINI_API_KEY="新的密钥"
```

重新加载配置：
```bash
source ~/.zshrc
```

### 删除密钥

编辑 `~/.zshrc`，删除包含 `GEMINI_API_KEY` 的行，然后：
```bash
source ~/.zshrc
unset GEMINI_API_KEY
```

## 💡 最佳实践

### ✓ 推荐做法

1. **使用系统环境变量存储所有密钥**
   ```bash
   # 示例：添加多个API密钥
   export GEMINI_API_KEY="..."
   export OPENAI_API_KEY="..."
   export AWS_ACCESS_KEY="..."
   ```

2. **定期轮换API密钥**
   - 每3-6个月更新一次
   - 发现异常使用立即更新

3. **不同项目使用不同密钥**（可选）
   - 便于追踪使用情况
   - 限制单个密钥的影响范围

4. **备份环境变量配置**
   ```bash
   # 导出配置（注意安全存储）
   grep "export.*_KEY" ~/.zshrc > ~/my-env-backup.txt
   ```

### ✗ 避免做法

- ❌ 在代码中硬编码密钥
- ❌ 将 `.zshrc` 提交到Git
- ❌ 通过邮件发送密钥
- ❌ 在截图中暴露密钥
- ❌ 使用同一密钥在多个公共项目

## 🛡️ 安全检查清单

在提交到GitHub前，确认：

- [ ] 运行 `grep -r "AIzaSy" .` 无输出
- [ ] `.env` 文件不存在或已在 .gitignore
- [ ] `run.sh` 不包含硬编码密钥
- [ ] 所有文档使用 `your-api-key-here` 占位符
- [ ] `git status` 不显示敏感文件
- [ ] `.zshrc` 不在Git仓库中

全部✅后，可以安全提交！

## 📊 安全等级对比

```
┌─────────────────────────────────────────────┐
│ 安全等级：系统环境变量方案                    │
├─────────────────────────────────────────────┤
│                                             │
│  Git泄露风险         ████████████ 0%       │
│  代码泄露风险         ████████████ 0%       │
│  文档泄露风险         ████████████ 0%       │
│  便利性             ████████████ 100%      │
│  多项目共享          ████████████ 100%      │
│                                             │
└─────────────────────────────────────────────┘
```

## 🎉 总结

您现在拥有最安全的API密钥管理方案：

✅ **API密钥存储在系统环境变量中**
✅ **项目代码完全不含密钥**
✅ **可以放心提交到GitHub**
✅ **跨项目共享同一密钥**
✅ **新机器配置简单快速**

---

**需要帮助？**
- 系统环境变量配置问题：查看本文档"管理API密钥"部分
- Git提交问题：查看 SECURITY.md
- 项目使用问题：查看 README.md 和 QUICKSTART.md
```

## File: `QUICKSTART.md`
```markdown
# 快速使用指南

## 🚀 5分钟快速上手

### 步骤1: 设置API密钥

```bash
export GEMINI_API_KEY='your-google-ai-api-key'
```

**获取API密钥**: 访问 [Google AI Studio](https://makersuite.google.com/app/apikey)

### 步骤2: 安装依赖

```bash
pip install google-genai pillow
```

### 步骤3: 准备文档

创建或准备一个markdown文档，例如 `my-document.md`：

```markdown
# 我的演示主题

## 第一部分：背景
这里是背景介绍...

## 第二部分：核心观点
- 观点1：...
- 观点2：...
- 观点3：...

## 第三部分：总结
关键发现和行动建议...
```

### 步骤4: 在Claude Code中使用

打开Claude Code，执行：

```
我想基于 my-document.md 生成一个5页的PPT，使用渐变毛玻璃卡片风格，2K分辨率。
```

Claude会自动：
1. 分析文档内容
2. 规划5页PPT的内容
3. 生成高质量图片
4. 创建HTML播放网页

### 步骤5: 查看结果

```bash
open outputs/TIMESTAMP/index.html
```

使用键盘操作：
- ← → : 切换页面
- ESC : 全屏模式
- 空格 : 自动播放

## 💡 使用技巧

### 技巧1: 选择合适的页数

- **5页**: 电梯演讲（5分钟）
- **5-10页**: 标准演示（10-15分钟）
- **10-15页**: 深入讲解（20-30分钟）
- **20-25页**: 完整培训（45-60分钟）

### 技巧2: 优化文档结构

**好的文档结构**:
```markdown
# 主标题

## 核心观点1
- 要点
- 要点
- 要点

## 核心观点2
[详细说明...]

## 总结
[关键结论...]
```

**不理想的结构**:
```markdown
# 标题
一大段没有分段的文字...
```

### 技巧3: 分辨率选择建议

| 用途 | 推荐分辨率 | 生成时间 | 文件大小 |
|------|------------|----------|----------|
| 日常演示 | 2K | ~30秒/页 | ~2MB/页 |
| 正式场合 | 2K | ~30秒/页 | ~2MB/页 |
| 打印输出 | 4K | ~60秒/页 | ~8MB/页 |
| 大屏展示 | 4K | ~60秒/页 | ~8MB/页 |

### 技巧4: 批量生成

如果需要生成多个版本：

```bash
# 5页精简版
python generate_ppt.py --plan plan_5.json --style styles/gradient-glass.md --resolution 2K --output outputs/v1-brief

# 15页详细版
python generate_ppt.py --plan plan_15.json --style styles/gradient-glass.md --resolution 2K --output outputs/v2-detailed
```

## 🎨 自定义风格

### 创建新风格

1. 复制现有风格文件：
```bash
cp styles/gradient-glass.md styles/my-style.md
```

2. 编辑风格定义：
```markdown
# 我的自定义风格

## 风格ID
my-custom-style

## 基础提示词模板
[修改为你的风格描述...]
```

3. 使用新风格：
```bash
python generate_ppt.py --plan plan.json --style styles/my-style.md
```

## 🔧 高级用法

### 手动调整提示词

1. 查看生成的提示词：
```bash
cat outputs/TIMESTAMP/prompts.json
```

2. 复制并修改想要调整的提示词

3. 创建新的规划文件并重新生成

### 混合页面类型

在JSON规划文件中自定义页面类型：

```json
{
  "slides": [
    {"page_type": "cover", "content": "..."},
    {"page_type": "content", "content": "..."},
    {"page_type": "data", "content": "..."},
    {"page_type": "content", "content": "..."}
  ]
}
```

### 并行生成

同时生成多个版本：

```bash
python generate_ppt.py --plan plan1.json --style styles/gradient-glass.md --output outputs/v1 &
python generate_ppt.py --plan plan2.json --style styles/gradient-glass.md --output outputs/v2 &
wait
echo "所有版本生成完成！"
```

## 📋 常见问题

### Q: 生成失败怎么办？

A: 检查以下几点：
1. API密钥是否正确设置
2. 网络连接是否正常
3. Python依赖是否完整安装
4. 查看详细错误信息

### Q: 可以生成中文内容吗？

A: 可以！Nano Banana Pro支持多语言，包括中文。

### Q: 生成需要多长时间？

A:
- 2K: 约30秒/页
- 4K: 约60秒/页
- 5页PPT大约需要2.5-5分钟

### Q: 如何导出为PDF？

A: 在浏览器中打开HTML播放器，使用"打印"功能：
1. 打开播放器
2. 按 Cmd+P (Mac) 或 Ctrl+P (Windows)
3. 选择"另存为PDF"

### Q: 可以修改已生成的PPT吗？

A: 可以通过以下方式：
1. 编辑JSON规划文件
2. 修改提示词
3. 重新运行生成脚本

### Q: 支持哪些文档格式？

A: 目前最佳支持Markdown格式，也可以使用纯文本。

## 📞 获取帮助

遇到问题？
1. 查看README.md
2. 查看ppt-generator.md详细文档
3. 在Claude Code中使用 `/help`

## 🎯 最佳实践清单

✅ 使用清晰的标题和分段
✅ 每页内容不超过3-5个要点
✅ 选择合适的页数范围
✅ 日常使用2K分辨率
✅ 保存原始JSON规划文件
✅ 定期检查API配额使用情况
✅ 测试播放器在不同浏览器的表现

---

**开始创作吧！** 🚀
```

## File: `README.md`
```markdown
# NanoBanana PPT Skills

> 基于 AI 自动生成高质量 PPT 图片和视频的强大工具，支持智能转场和交互式播放

<div align="center">

![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Python](https://img.shields.io/badge/python-3.8+-green.svg)

**创作者**: [歸藏](https://github.com/op7418)

[效果演示](#-效果演示) • [功能特性](#-功能特性) • [一键安装](#-一键安装) • [作为 Skill 使用](#-作为-claude-code-skill-使用) • [使用指南](#-使用指南) • [视频功能](#-视频功能) • [架构文档](ARCHITECTURE.md) • [常见问题](#-常见问题)

</div>

---

## 🎬 效果演示

<div align="center">

https://github.com/user-attachments/assets/b394de21-2848-489a-8d33-a8e262e60f60

*AI 自动生成 PPT 并添加流畅转场动画 - 从文档分析到视频合成一键完成*

</div>

---

## 📖 简介

NanoBanana PPT Skills 是一个强大的 AI 驱动的 PPT 生成工具，能够：

- 📄 **智能分析文档**，自动提取核心要点并规划 PPT 结构
- 🎨 **生成高质量图片**，使用 Google Nano Banana Pro（Gemini 3 Pro Image Preview）
- 🎬 **自动生成转场视频**，使用可灵 AI 创建流畅的页面过渡动画
- 🎮 **交互式视频播放器**，支持键盘控制、循环预览、智能转场
- 🎥 **完整视频导出**，一键合成包含所有转场的完整 PPT 视频

### 🎨 视觉风格

**渐变毛玻璃卡片风格**
- 高端科技感，Apple Keynote 极简主义
- 3D 玻璃物体 + 霓虹渐变
- 电影级光照效果
- 适合：科技产品、商务演示、数据报告

**矢量插画风格**
- 温暖扁平化设计，复古配色
- 黑色轮廓线 + 几何化处理
- 玩具模型般的可爱感
- 适合：教育培训、创意提案、品牌故事

---

## ✨ 功能特性

### 🎯 核心能力

- 🤖 **智能文档分析** - 自动提取核心要点，规划 PPT 内容结构
- 🎨 **多风格支持** - 内置 2 种专业风格，可无限扩展
- 🖼️ **高质量图片** - 16:9 比例，2K/4K 分辨率可选
- 🎬 **AI 转场视频** - 可灵 AI 生成流畅的页面过渡动画
- 🎮 **交互式播放器** - 视频+图片混合播放，支持键盘导航
- 🎥 **完整视频导出** - FFmpeg 合成包含转场的完整 PPT 视频
- 📊 **智能布局** - 封面页、内容页、数据页自动识别
- ⚡ **快速生成** - 2K 约 30 秒/页

### 🆕 视频功能（v2.0）

- 🎬 **首页循环预览** - 自动生成吸引眼球的循环动画
- 🎞️ **智能转场** - 自动生成页面间的过渡视频
- 🎮 **交互式播放** - 按键翻页时播放转场视频，结束后显示静态图片
- 🎥 **完整视频导出** - 合成包含所有转场和静态页的完整视频
- 🔧 **参数统一** - 自动统一所有视频分辨率和帧率，确保流畅播放

### 🛠️ 技术亮点

- ✅ Google Nano Banana Pro（Gemini 3 Pro Image Preview）图像生成
- ✅ 可灵 AI API 集成（视频生成、数字人、主体库）
- ✅ FFmpeg 视频合成与参数统一
- ✅ 完整的提示词工程和风格管理系统
- ✅ 安全的 .env 环境变量管理
- ✅ 模块化设计，易于扩展

---

## 🚀 一键安装

### 方法一：Claude Code 自动安装（推荐）

**只需复制以下提示词，发送给 Claude Code，它会自动完成全部安装！**

```
请帮我安装 NanoBanana PPT Skills：

1. 克隆项目并进入目录：
   git clone https://github.com/op7418/NanoBanana-PPT-Skills.git
   cd NanoBanana-PPT-Skills

2. 创建 Python 虚拟环境：
   python3 -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate

3. 安装依赖：
   pip install google-genai pillow python-dotenv

4. 配置 API 密钥 - 创建 .env 文件：
   cp .env.example .env

5. 编辑 .env 文件，填入我的 API 密钥：

   GEMINI_API_KEY=YOUR_GEMINI_API_KEY
   KLING_ACCESS_KEY=YOUR_KLING_ACCESS_KEY
   KLING_SECRET_KEY=YOUR_KLING_SECRET_KEY

   注意：
   - GEMINI_API_KEY: Google AI API 密钥（必需，用于生成 PPT 图片）
   - KLING_ACCESS_KEY 和 KLING_SECRET_KEY: 可灵 AI 密钥（可选，用于生成转场视频）

6. 验证安装：
   python3 generate_ppt.py --help

完成后，告诉我安装结果和如何使用。

我的 API 密钥：
- GEMINI_API_KEY: YOUR_GEMINI_API_KEY_HERE
- KLING_ACCESS_KEY: YOUR_KLING_ACCESS_KEY_HERE (可选)
- KLING_SECRET_KEY: YOUR_KLING_SECRET_KEY_HERE (可选)
```

**使用说明**：
1. 先获取 API 密钥：
   - **必需**: [Google AI API 密钥](https://aistudio.google.com/apikey)
   - **可选**: [可灵 AI API 密钥](https://klingai.com)（用于视频转场功能）
2. 复制上面的提示词
3. 将 `YOUR_GEMINI_API_KEY_HERE` 等替换为你的真实 API 密钥
4. 发送给 Claude Code
5. Claude Code 会自动执行所有安装步骤并告知结果

### 方法二：手动安装

如果你想手动安装，按照以下步骤操作：

#### 1. 克隆项目

```bash
git clone https://github.com/op7418/NanoBanana-PPT-Skills.git
cd NanoBanana-PPT-Skills
```

#### 2. 创建虚拟环境

```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

#### 3. 安装依赖

```bash
pip install google-genai pillow
```

如果需要视频功能，还需要安装 FFmpeg：

```bash
# macOS
brew install ffmpeg

# Ubuntu/Debian
sudo apt-get install ffmpeg

# Windows
# 下载 FFmpeg 并添加到系统 PATH
```

#### 4. 配置 API 密钥

**推荐方式：.env 文件（已内置支持）**

```bash
# 复制示例文件
cp .env.example .env

# 编辑 .env 文件
nano .env  # 或使用你喜欢的编辑器
```

在 `.env` 文件中填入你的 API 密钥：

```bash
# Google AI API 密钥（必需）
GEMINI_API_KEY=your_gemini_api_key_here

# 可灵 AI API 密钥（可选，用于视频转场功能）
KLING_ACCESS_KEY=your_kling_access_key_here
KLING_SECRET_KEY=your_kling_secret_key_here
```

**替代方式：系统环境变量**

```bash
# zsh 用户 (macOS 默认)
echo 'export GEMINI_API_KEY="your-api-key-here"' >> ~/.zshrc
source ~/.zshrc

# bash 用户
echo 'export GEMINI_API_KEY="your-api-key-here"' >> ~/.bashrc
source ~/.bashrc
```

#### 5. 验证安装

```bash
python3 generate_ppt.py --help
```

应该显示帮助信息，表示安装成功。

---

## 🎯 作为 Claude Code Skill 使用

NanoBanana PPT Skills 完全支持 Claude Code Skill 标准，可以直接通过 Claude Code 调用。

### 快速安装为 Skill

**方法一：Claude Code 自动安装为 Skill（最简单）**

**只需复制以下提示词，发送给 Claude Code，它会自动完成 Skill 安装！**

```
请帮我将 NanoBanana PPT Skills 安装为 Claude Code Skill：

1. 创建 Skill 目录：
   mkdir -p ~/.claude/skills/ppt-generator

2. 克隆项目到 Skill 目录：
   git clone https://github.com/op7418/NanoBanana-PPT-Skills.git ~/.claude/skills/ppt-generator

3. 进入目录并安装依赖：
   cd ~/.claude/skills/ppt-generator
   python3 -m venv venv
   source venv/bin/activate
   pip install google-genai pillow python-dotenv

4. 配置 API 密钥：
   cp .env.example .env

   然后编辑 .env 文件，填入我的 API 密钥：
   GEMINI_API_KEY=YOUR_GEMINI_API_KEY
   KLING_ACCESS_KEY=YOUR_KLING_ACCESS_KEY
   KLING_SECRET_KEY=YOUR_KLING_SECRET_KEY

5. 验证安装：
   python3 generate_ppt.py --help

完成后，告诉我如何在 Claude Code 中使用这个 Skill。

我的 API 密钥：
- GEMINI_API_KEY: YOUR_GEMINI_API_KEY_HERE
- KLING_ACCESS_KEY: YOUR_KLING_ACCESS_KEY_HERE (可选)
- KLING_SECRET_KEY: YOUR_KLING_SECRET_KEY_HERE (可选)
```

**方法二：使用安装脚本**

```bash
# 克隆项目
git clone https://github.com/op7418/NanoBanana-PPT-Skills.git
cd NanoBanana-PPT-Skills

# 运行安装脚本
bash install_as_skill.sh
```

安装脚本会自动：
1. 创建 `~/.claude/skills/ppt-generator/` 目录
2. 复制所有必要文件
3. 安装 Python 依赖
4. 引导配置 API 密钥

**方法三：手动安装**

```bash
# 1. 创建 Skill 目录
mkdir -p ~/.claude/skills/ppt-generator

# 2. 克隆项目到 Skill 目录
git clone https://github.com/op7418/NanoBanana-PPT-Skills.git ~/.claude/skills/ppt-generator

# 3. 安装依赖
cd ~/.claude/skills/ppt-generator
pip install google-genai pillow python-dotenv

# 4. 配置 API 密钥
cp .env.example .env
nano .env  # 填入你的 API 密钥
```

### 环境变量配置

Skill 会智能查找 `.env` 文件，按以下优先级：

1. **脚本所在目录** - `~/.claude/skills/ppt-generator/.env`
2. **向上查找项目根目录** - 直到找到包含 `.git` 或 `.env` 的目录
3. **用户主目录** - `~/.env`
4. **系统环境变量** - 作为最后的备选方案

**推荐配置方式：**

```bash
# 在 Skill 目录下创建 .env 文件
cat > ~/.claude/skills/ppt-generator/.env << EOF
# Google AI API 密钥（必需）
GEMINI_API_KEY=your_gemini_api_key_here

# 可灵 AI API 密钥（可选，用于视频功能）
KLING_ACCESS_KEY=your_kling_access_key_here
KLING_SECRET_KEY=your_kling_secret_key_here
EOF
```

### 在 Claude Code 中使用

安装完成后，直接在 Claude Code 中调用：

```bash
/ppt-generator-pro
```

或者告诉 Claude：

```
我想基于以下文档生成一个 5 页的 PPT，使用渐变毛玻璃风格。

[文档内容...]
```

Claude 会自动：
1. 分析文档内容
2. 询问风格、页数、分辨率等选项
3. 生成 slides_plan.json
4. 调用 generate_ppt.py 生成图片
5. （可选）生成转场视频
6. 返回结果路径

### Skill 模式 vs 独立模式

| 特性 | Skill 模式 | 独立模式 |
|------|-----------|---------|
| 安装位置 | `~/.claude/skills/ppt-generator/` | 任意目录 |
| 调用方式 | `/ppt-generator-pro` 或自然语言 | 手动执行 Python 脚本 |
| 文档分析 | Claude 自动分析 | 需手动准备 JSON |
| 交互体验 | 对话式，自动询问选项 | 命令行参数 |
| .env 位置 | Skill 目录或项目根目录 | 脚本所在目录 |
| 适用场景 | 日常使用，快速生成 | 批量生成，自动化脚本 |

### 详细使用文档

完整的 Skill 使用文档请参考 [SKILL.md](../bmad_repo/SKILL.md)，包含：
- 完整的执行流程
- 用户输入收集策略
- 内容规划方法
- 错误处理指南
- 最佳实践建议

---

## 💡 使用指南

### 基础使用：生成 PPT 图片

#### 1. 准备内容规划文件

创建 `my_slides_plan.json`：

```json
{
  "title": "AI 产品设计指南",
  "total_slides": 5,
  "slides": [
    {
      "slide_number": 1,
      "page_type": "cover",
      "content": "标题：AI 产品设计指南\n副标题：构建以用户为中心的智能体验"
    },
    {
      "slide_number": 2,
      "page_type": "content",
      "content": "核心原则\n- 简单直观\n- 快速响应\n- 透明可控"
    },
    {
      "slide_number": 3,
      "page_type": "content",
      "content": "设计流程\n1. 用户研究\n2. 原型设计\n3. 测试迭代"
    },
    {
      "slide_number": 4,
      "page_type": "data",
      "content": "用户满意度\n使用前：65%\n使用后：92%\n提升：+27%"
    },
    {
      "slide_number": 5,
      "page_type": "content",
      "content": "总结\n- 以用户为中心\n- 持续优化迭代\n- 数据驱动决策"
    }
  ]
}
```

#### 2. 生成 PPT 图片

```bash
python3 generate_ppt.py \
  --plan my_slides_plan.json \
  --style styles/gradient-glass.md \
  --resolution 2K
```

#### 3. 查看结果

```bash
# 在浏览器中打开图片播放器
open outputs/TIMESTAMP/index.html
```

### 高级使用：生成带转场视频的 PPT

#### 1. 生成 PPT 图片

```bash
python3 generate_ppt.py \
  --plan my_slides_plan.json \
  --style styles/gradient-glass.md \
  --resolution 2K
```

#### 2. 使用 Claude Code 生成转场提示词（必需）

在 Claude Code 中执行：

```
我刚生成了 5 页 PPT 图片在 outputs/TIMESTAMP/images 目录下。
请帮我分析这些图片，为每个页面转场生成视频提示词，
保存为 outputs/TIMESTAMP/transition_prompts.json
```

Claude Code 会：
1. 读取所有 PPT 图片
2. 分析每两页之间的视觉差异
3. 生成精准的转场描述
4. 保存为 JSON 文件

#### 3. 生成转场视频

```bash
python3 generate_ppt_video.py \
  --slides-dir outputs/TIMESTAMP/images \
  --output-dir outputs/TIMESTAMP_video \
  --prompts-file outputs/TIMESTAMP/transition_prompts.json
```

这会生成：
- 首页循环预览视频
- 每个页面间的转场视频
- 交互式视频播放器 HTML
- 完整视频 (full_ppt_video.mp4)

#### 4. 播放交互式视频 PPT

```bash
open outputs/TIMESTAMP_video/video_index.html
```

**播放逻辑**：
1. 首页：播放循环预览视频
2. 按右键：播放转场视频 → 显示目标页图片（停留 2 秒）
3. 再按右键：播放下一个转场视频 → 显示下一页图片
4. 依此类推...

#### 4. 导出完整视频（可选）

交互式播放器会自动生成完整视频：

```bash
# 视频文件
outputs/TIMESTAMP_video/full_ppt_video.mp4
```

完整视频包含：
- 首页预览（如果有）
- 转场视频 01→02
- 第 2 页静态（2 秒）
- 转场视频 02→03
- 第 3 页静态（2 秒）
- ...

---

## 🎬 视频功能

### 转场视频生成

使用可灵 AI 自动生成页面间的转场视频：

```bash
python3 generate_ppt_video.py \
  --slides-dir outputs/20260111_160221/images \
  --output-dir outputs/20260111_video \
  --mode professional \
  --duration 5
```

**参数说明**：
- `--slides-dir`: PPT 图片目录
- `--output-dir`: 输出目录
- `--mode`: 转场模式（`professional` 或 `creative`）
- `--duration`: 转场视频时长（秒，默认 5）

### 交互式播放器

生成的 `video_index.html` 支持：

| 功能 | 快捷键 | 说明 |
|------|--------|------|
| 下一页 | `→` `↓` | 播放转场视频，然后显示下一页 |
| 上一页 | `←` `↑` | 返回上一页（直接显示） |
| 首页 | `Home` | 返回首页预览 |
| 末页 | `End` | 跳到最后一页 |
| 播放/暂停 | `空格` | 暂停/继续当前视频 |
| 全屏 | `ESC` | 切换全屏模式 |
| 隐藏控件 | `H` | 隐藏/显示控制提示 |

### 完整视频合成

使用 FFmpeg 自动合成完整视频：

```python
from video_composer import VideoComposer

composer = VideoComposer()
composer.compose_full_ppt_video(
    slides_paths=[...],
    transitions_dict={...},
    output_path='output.mp4',
    slide_duration=2,  # 每页停留 2 秒
    include_preview=True,
    preview_video_path='preview.mp4',
    resolution='1920x1080',
    fps=24
)
```

**特性**：
- 自动统一所有视频的分辨率和帧率
- 保持宽高比，添加黑边
- 支持预览视频循环
- 高质量 H.264 编码

---

## 🎨 风格库

### 已内置风格

#### 1. 渐变毛玻璃卡片风格 (`gradient-glass.md`)

**视觉特点**：
- Apple Keynote 极简主义
- 玻璃拟态效果
- 霓虹紫/电光蓝/珊瑚橙渐变
- 3D 玻璃物体 + 电影级光照

**适用场景**：
- 🚀 科技产品发布
- 💼 商务演示
- 📊 数据报告
- 🏢 企业品牌展示

#### 2. 矢量插画风格 (`vector-illustration.md`)

**视觉特点**：
- 扁平化矢量设计
- 统一黑色轮廓线
- 复古柔和配色
- 几何化简化

**适用场景**：
- 📚 教育培训
- 🎨 创意提案
- 👶 儿童相关
- 💖 温暖品牌故事

### 添加自定义风格

1. 在 `styles/` 目录创建新的 `.md` 文件
2. 按照模板编写风格定义（参考现有风格）
3. 直接使用新风格生成 PPT

---

## 📚 项目结构

```
ppt-generator/
├── README.md                      # 本文件
├── API_MANAGEMENT.md              # API 密钥管理指南
├── ENV_SETUP.md                   # 环境变量配置指南
├── SECURITY.md                    # 安全最佳实践
├── .env.example                   # 环境变量模板
├── .env                          # 实际环境变量（不提交到 Git）
├── .gitignore                    # Git 忽略规则
│
├── generate_ppt.py               # PPT 图片生成脚本
├── generate_ppt_video.py         # 视频生成主脚本
├── kling_api.py                  # 可灵 AI API 封装
├── video_composer.py             # FFmpeg 视频合成
├── video_materials.py            # 视频素材管理
├── transition_prompt_generator.py # 转场提示词生成器
│
├── styles/                       # 风格库
│   ├── gradient-glass.md         # 渐变毛玻璃卡片风格
│   └── vector-illustration.md    # 矢量插画风格
│
├── templates/                    # HTML 模板
│   ├── viewer.html              # 图片播放器
│   └── video_viewer.html        # 视频播放器
│
├── prompts/                      # 提示词模板
│   └── transition_base.md       # 转场提示词基础模板
│
└── outputs/                      # 生成结果（自动创建）
    ├── TIMESTAMP/               # 图片版本
    │   ├── images/             # PPT 图片
    │   ├── index.html          # 图片播放器
    │   └── prompts.json        # 生成提示词记录
    └── TIMESTAMP_video/         # 视频版本
        ├── videos/             # 转场视频
        ├── video_index.html    # 视频播放器
        └── full_ppt_video.mp4  # 完整视频
```

---

## 🔧 配置选项

### 分辨率选择

| 分辨率 | 尺寸 | 文件大小 | 生成速度 | 推荐场景 |
|--------|------|----------|----------|----------|
| 2K | 2752x1536 | ~2.5MB/页 | ~30秒/页 | 日常演示、在线分享 ✅ |
| 4K | 5504x3072 | ~8MB/页 | ~60秒/页 | 打印输出、大屏展示 |

### 视频参数

| 参数 | 默认值 | 说明 |
|------|--------|------|
| 分辨率 | 1920x1080 | 统一为 1080p，兼容可灵视频 |
| 帧率 | 24fps | 统一帧率，确保流畅拼接 |
| 静态图片时长 | 2秒 | 每页停留时间 |
| 转场视频时长 | 5秒 | 可灵生成的转场时长 |

### 页数建议

| 页数范围 | 演讲时长 | 适用场景 |
|----------|----------|----------|
| 5 页 | 5 分钟 | 电梯演讲、快速介绍 |
| 5-10 页 | 10-15 分钟 | 标准演示、产品介绍 |
| 10-15 页 | 20-30 分钟 | 深入讲解、培训课程 |
| 20-25 页 | 45-60 分钟 | 完整培训、研讨会 |

---

## ❓ 常见问题

### Q: 如何获取 API 密钥？

**A**:
- **Google AI API**: 访问 [Google AI Studio](https://aistudio.google.com/apikey)，登录后即可创建
- **可灵 AI API**: 访问 [可灵 AI 开放平台](https://klingai.com)，注册并创建应用获取密钥

### Q: 是否必须配置可灵 AI 密钥？

**A**: 不是必须的。
- **只生成 PPT 图片**：只需要 GEMINI_API_KEY
- **生成转场视频**：需要 KLING_ACCESS_KEY 和 KLING_SECRET_KEY

### Q: 视频合成失败怎么办？

**A**: 检查以下几点：
1. FFmpeg 是否已安装（`ffmpeg -version`）
2. 视频文件是否存在且完整
3. 磁盘空间是否充足
4. 查看详细错误信息

### Q: 如何修改静态图片展示时间？

**A**: 在 `video_composer.py` 中修改 `slide_duration` 参数（默认 2 秒）

### Q: 转场视频生成很慢怎么办？

**A**: 可灵 AI 生成视频需要一定时间（通常 30-60 秒/段）。可以：
- 减少转场数量
- 使用较短的转场时长
- 分批生成

### Q: 可以导出为 PDF 吗？

**A**: 可以。
1. 在浏览器中打开 `index.html`
2. 按 `Cmd+P` (Mac) 或 `Ctrl+P` (Windows)
3. 选择"另存为 PDF"

### Q: 生成的内容可以商用吗？

**A**: 请查阅相关服务条款：
- [Google AI 使用条款](https://ai.google.dev/terms)
- [可灵 AI 使用条款](https://klingai.com/terms)

一般情况下，你拥有生成内容的使用权。

---

## 🛡️ 安全说明

### API 密钥安全

本项目采用 `.env` 文件管理 API 密钥，确保安全：

- ✅ `.env` 文件已在 `.gitignore` 中，不会提交到 Git
- ✅ 代码中无硬编码密钥
- ✅ 支持系统环境变量作为备用方案
- ✅ `.env.example` 提供配置模板

**最佳实践**：

```bash
# ✅ 正确：使用 .env 文件
cp .env.example .env
# 编辑 .env 填入真实密钥

# ❌ 错误：直接在代码中写密钥
GEMINI_API_KEY = "AIzaSy..." # 永远不要这样做！
```

### 提交前检查

```bash
# 验证没有密钥泄露
grep -r "AIzaSy\|ak-" --exclude-dir=.git --exclude-dir=venv .
# 应该无输出

# 检查 .env 文件是否被排除
git status
# 确认 .env 不在待提交列表中
```

详细说明请查看：
- **API_MANAGEMENT.md** - API 密钥管理完整指南
- **ENV_SETUP.md** - 环境变量配置指南
- **SECURITY.md** - 安全最佳实践

---

## 📝 更新日志

### v2.0.0 (2026-01-11)

- 🎬 **新增视频功能**
  - 可灵 AI 转场视频生成
  - 交互式视频播放器（视频+图片混合）
  - FFmpeg 完整视频合成
  - 首页循环预览视频
- 🔧 **优化视频合成**
  - 自动统一分辨率和帧率
  - 修复视频拼接兼容性问题
  - 静态图片展示时间改为 2 秒
- 🐛 **Bug 修复**
  - 修复预览模式状态管理问题
  - 修复 FFmpeg 滤镜参数格式错误
- 📚 **文档更新**
  - 全面改写 README
  - 新增视频功能使用指南
  - 更新 API 密钥配置说明

### v1.0.0 (2026-01-09)

- ✨ 首次发布
- 🎨 内置 2 种专业风格
- 🖼️ 支持 2K/4K 分辨率
- 🎬 HTML5 图片播放器
- 📊 智能文档分析
- 🔐 安全的环境变量管理

---

## 🤝 贡献指南

欢迎贡献！你可以：

### 添加新风格

1. Fork 本项目
2. 在 `styles/` 创建新风格文件
3. 参考现有风格编写提示词
4. 测试生成效果
5. 提交 Pull Request

### 报告问题

在 [GitHub Issues](https://github.com/op7418/NanoBanana-PPT-Skills/issues) 提交问题，请包含：
- 错误信息
- 操作步骤
- 系统环境
- 日志文件（如有）

---

## 📄 许可证

MIT License

Copyright (c) 2026 歸藏

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

---

## 🙏 致谢

- **Google Gemini Team** - 提供强大的 Nano Banana Pro 图像生成模型
- **可灵 AI 团队** - 提供高质量的视频生成服务
- **FFmpeg 项目** - 提供强大的视频处理工具
- **开源社区** - 提供的各种工具和灵感

---

## 📞 联系方式

- **创作者**: 歸藏
- **GitHub**: [@op7418](https://github.com/op7418)
- **Issues**: [GitHub Issues](https://github.com/op7418/NanoBanana-PPT-Skills/issues)

---

<div align="center">

**⭐ 如果这个项目对你有帮助，请给一个 Star！**

Made with ❤️ by 歸藏 | Powered by Google Gemini & 可灵 AI & FFmpeg

</div>
```

## File: `README_VIDEO_EXAMPLES.md`
```markdown
# README 视频演示添加方案

## 方案选择建议

### 🎯 推荐方案对比

| 方案 | 文件大小限制 | 国内访问 | 国外访问 | 自动播放 | 维护成本 |
|------|------------|----------|----------|----------|---------|
| **GIF 动图** | 建议 < 10MB | ✅ 快 | ✅ 快 | ✅ 是 | ⭐ 低 |
| **GitHub 仓库视频** | < 100MB | ⚠️ 慢 | ✅ 快 | ❌ 否 | ⭐ 低 |
| **Bilibili** | 无限制 | ✅ 快 | ⚠️ 慢 | ❌ 否 | ⭐⭐ 中 |
| **GitHub + Bilibili** | - | ✅ 快 | ✅ 快 | ❌ 否 | ⭐⭐ 中 |
| **Cloudinary** | 25GB 免费 | ✅ 快 | ✅ 快 | ❌ 否 | ⭐⭐⭐ 高 |

### 💡 具体建议

**对于你的项目（NanoBanana PPT Skills）**，我推荐：

1. **首选：GIF 动图** - 如果能压缩到 5-10MB 以内
   - 最佳用户体验，自动播放
   - 适合展示 10-20 秒核心功能演示

2. **备选：GitHub 仓库 + Bilibili 双链接**
   - GitHub 放短视频（< 50MB）展示核心功能
   - Bilibili 放完整演示（带讲解）
   - 照顾国内外用户

---

## Markdown 代码示例

### 方案 1: GIF 动图（推荐）

在 README.md 第 15 行（`</div>` 之后）添加：

```markdown
</div>

---

## 🎬 效果演示

<div align="center">

![NanoBanana PPT Skills Demo](demo.gif)

*AI 自动生成 PPT 并添加流畅转场动画*

</div>

---
```

**或者使用 HTML 标签控制大小：**

```markdown
<div align="center">
  <img src="demo.gif" alt="NanoBanana PPT Skills Demo" width="800">
  <p><em>AI 自动生成 PPT 并添加流畅转场动画</em></p>
</div>
```

---

### 方案 2: GitHub 仓库视频（< 100MB）

```markdown
## 🎬 效果演示

<div align="center">

https://github.com/op7418/NanoBanana-PPT-Skills/assets/YOUR_USER_ID/demo.mp4

*点击播放查看完整演示*

</div>
```

**或使用 HTML5 video 标签（更多控制）：**

```markdown
<div align="center">
  <video src="https://github.com/op7418/NanoBanana-PPT-Skills/assets/YOUR_USER_ID/demo.mp4"
         width="800"
         controls
         loop
         muted>
    您的浏览器不支持视频播放
  </video>
  <p><em>AI 自动生成 PPT 并添加流畅转场动画</em></p>
</div>
```

---

### 方案 3: Bilibili 嵌入

```markdown
## 🎬 效果演示

<div align="center">

[![Watch Demo on Bilibili](https://i0.hdslb.com/bfs/archive/VIDEO_COVER.jpg)](https://www.bilibili.com/video/BVXXXXXXX)

**🎥 [点击观看完整演示视频（Bilibili）](https://www.bilibili.com/video/BVXXXXXXX)**

*包含详细功能讲解和使用教程*

</div>
```

---

### 方案 4: GitHub + Bilibili 双托管（推荐给你的最佳方案）

```markdown
## 🎬 效果演示

<div align="center">

### 快速预览（30秒）

https://github.com/op7418/NanoBanana-PPT-Skills/assets/YOUR_USER_ID/demo-short.mp4

### 完整教程

**🎥 [观看完整演示视频（Bilibili 5分钟）](https://www.bilibili.com/video/BVXXXXXXX)** - 包含详细功能讲解

**🌍 [Watch Full Demo (YouTube 5min)](https://youtube.com/watch?v=XXXXXXXXX)** - English subtitles available

</div>

---
```

---

### 方案 5: Cloudinary 托管

```markdown
## 🎬 效果演示

<div align="center">

<video
  src="https://res.cloudinary.com/YOUR_CLOUD_NAME/video/upload/v1234567890/demo.mp4"
  width="800"
  controls
  loop
  muted
  poster="https://res.cloudinary.com/YOUR_CLOUD_NAME/image/upload/v1234567890/demo-poster.jpg">
</video>

*AI 自动生成 PPT 并添加流畅转场动画*

</div>
```

---

### 方案 6: 多种演示方式组合（完整版）

```markdown
## 🎬 效果演示

<div align="center">

### 🎨 渐变毛玻璃风格演示

![Gradient Glass Style Demo](demos/gradient-glass-demo.gif)

### 🎞️ 完整 PPT 生成流程

https://github.com/op7418/NanoBanana-PPT-Skills/assets/YOUR_USER_ID/full-demo.mp4

### 📺 详细教程视频

| 平台 | 链接 | 时长 | 说明 |
|------|------|------|------|
| 🎬 **Bilibili** | [观看教程](https://bilibili.com/video/BVXXXX) | 5:30 | 中文讲解，包含安装和使用 |
| 🌏 **YouTube** | [Watch Tutorial](https://youtube.com/watch?v=XXXX) | 5:30 | English subtitles |

</div>

---
```

---

## 具体操作步骤

### 如果选择 GIF 方案：

1. **生成 GIF**（推荐 10-20 秒精华片段）：

```bash
cd /Users/guohao/Documents/code/ppt/ppt-generator

# 方法1：完整视频转 GIF（会很大）
ffmpeg -i outputs/20260112_135018_video/full_ppt_video.mp4 \
  -vf "fps=10,scale=800:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" \
  -loop 0 \
  demo.gif

# 方法2：截取前 20 秒（推荐）
ffmpeg -i outputs/20260112_135018_video/full_ppt_video.mp4 \
  -t 20 \
  -vf "fps=10,scale=800:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" \
  -loop 0 \
  demo.gif

# 方法3：超压缩版（如果文件太大）
ffmpeg -i outputs/20260112_135018_video/full_ppt_video.mp4 \
  -t 15 \
  -vf "fps=8,scale=600:-1:flags=lanczos,split[s0][s1];[s0]palettegen=max_colors=128[p];[s1][p]paletteuse=dither=bayer" \
  -loop 0 \
  demo-compressed.gif
```

2. **检查文件大小**：
```bash
ls -lh demo.gif
# 建议控制在 5-10MB 以内
```

3. **放到仓库根目录**：
```bash
# 将 GIF 移动到仓库根目录
mv demo.gif /Users/guohao/Documents/code/ppt/ppt-generator/

# 添加到 git
git add demo.gif
```

### 如果选择 GitHub 视频方案：

1. **压缩视频**（必须 < 100MB）：

```bash
# 压缩到 1080p, 5Mbps 码率
ffmpeg -i outputs/20260112_135018_video/full_ppt_video.mp4 \
  -vf "scale=1920:1080:force_original_aspect_ratio=decrease" \
  -c:v libx264 -b:v 5M -maxrate 5M -bufsize 10M \
  -c:a aac -b:a 128k \
  demo-compressed.mp4

# 检查大小
ls -lh demo-compressed.mp4
```

2. **上传到 GitHub**：
   - 直接在 GitHub 仓库的 Issue 或 Pull Request 中拖拽视频上传
   - 复制生成的 URL（类似 `https://github.com/user/repo/assets/12345/video.mp4`）
   - 在 README 中使用这个 URL

### 如果选择 Bilibili 方案：

1. 录制完整演示（带讲解）
2. 上传到 Bilibili，设置封面
3. 复制视频链接（BV号）
4. 在 README 中使用

---

## 推荐的完整布局

```markdown
# NanoBanana PPT Skills

> 基于 AI 自动生成高质量 PPT 图片和视频的强大工具，支持智能转场和交互式播放

<div align="center">

![Version](https://img.shields.io/badge/version-2.0.0-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Python](https://img.shields.io/badge/python-3.8+-green.svg)

**创作者**: [歸藏](https://github.com/op7418)

[功能特性](#-功能特性) • [效果演示](#-效果演示) • [一键安装](#-一键安装) • [使用指南](#-使用指南)

</div>

---

## 🎬 效果演示

<div align="center">

### 🎨 自动生成渐变毛玻璃风格 PPT

![Demo](demo.gif)

*从文档分析到转场视频，一键完成*

### 📺 完整教程

**🎥 [观看详细教程（Bilibili 5分钟）](https://bilibili.com/video/BVXXXX)** - 包含安装和使用说明

</div>

---

## 📖 简介

...
```

---

## 我的最终建议

**对于你的项目，推荐这样做：**

1. **立即行动**：
   - 生成一个 15-20 秒的 GIF 动图（展示核心功能）
   - 放在 README 开头，给用户第一印象

2. **后续增强**：
   - 录制一个 3-5 分钟的完整演示视频
   - 上传到 Bilibili（中文讲解）
   - 在 README 中提供链接

3. **README 结构**：
```
标题 + Badges
    ↓
导航链接（添加"效果演示"）
    ↓
🎬 效果演示（GIF 自动播放）
    ↓
完整教程链接（Bilibili/YouTube）
    ↓
简介
    ↓
其他内容...
```

需要我帮你执行具体操作吗？比如：
1. 生成优化的 GIF
2. 压缩视频到 < 100MB
3. 修改 README 添加演示区域
```

## File: `SECURITY.md`
```markdown
# Git提交安全检查清单

## ✅ 已配置的安全措施

### 1. .gitignore 配置 ✓

以下敏感文件和目录已被正确忽略，**不会被提交到GitHub**：

```
✓ .env                  # API密钥配置文件
✓ venv/                 # Python虚拟环境
✓ outputs/              # 生成的PPT图片
✓ *.key, *.pem          # 其他密钥文件
✓ .DS_Store             # macOS系统文件
✓ __pycache__/          # Python缓存
✓ test_*.json           # 测试文件
```

### 2. 安全的环境变量管理 ✓

**之前的问题（已修复）**：
- ❌ `run.sh` 中硬编码了API密钥

**当前方案**：
- ✅ API密钥存储在 `.env` 文件中
- ✅ `.env` 已添加到 `.gitignore`
- ✅ `run.sh` 从 `.env` 文件读取密钥
- ✅ 提供 `.env.example` 作为配置模板

### 3. 会被提交的文件清单 ✓

以下文件是安全的，**可以提交**到GitHub：

```
✓ .env.example          # 环境变量模板（不含真实密钥）
✓ .gitignore            # Git忽略规则
✓ README.md             # 项目说明
✓ QUICKSTART.md         # 快速开始指南
✓ SETUP_COMPLETE.md     # 配置完成说明
✓ generate_ppt.py       # Python生成脚本
✓ ppt-generator.md      # Skill定义
✓ run.sh                # 启动脚本（已修复，不含密钥）
✓ styles/*.md           # 风格定义文件
✓ templates/*.html      # HTML模板
```

## 🔒 提交前安全检查步骤

### 步骤1: 验证敏感文件被忽略

```bash
# 检查 .env 是否被忽略
git check-ignore -v .env
# 应输出: .gitignore:15:.env	.env

# 检查哪些文件会被提交（模拟）
git add -n .
# 确认列表中没有 .env 文件
```

### 步骤2: 搜索代码中的密钥

```bash
# 搜索可能的API密钥
grep -r "AIzaSy" --exclude-dir=.git --exclude-dir=venv --exclude-dir=outputs .

# 如果只在 .env 中找到，说明安全 ✓
# 如果在其他文件中找到，需要删除 ✗
```

### 步骤3: 检查Git历史

```bash
# 如果您之前有提交，检查历史中是否包含密钥
git log --all --full-history --source -- .env

# 如果有输出，说明 .env 曾被提交，需要清理历史
```

## 📋 安全的Git工作流

### 首次提交

```bash
# 1. 初始化Git仓库（如果还没有）
git init

# 2. 验证 .gitignore 正常工作
git status
# 确认 .env、venv/、outputs/ 不在列表中

# 3. 添加所有安全文件
git add .

# 4. 再次检查暂存区
git status
# 确认没有敏感文件

# 5. 提交
git commit -m "Initial commit: PPT Generator"

# 6. 关联远程仓库
git remote add origin https://github.com/你的用户名/ppt-generator.git

# 7. 推送
git push -u origin main
```

### 日常提交

```bash
# 1. 查看改动
git status

# 2. 添加文件
git add .

# 3. 提交
git commit -m "描述您的改动"

# 4. 推送
git push
```

## 🚨 如果密钥已经被提交

### 紧急处理步骤

如果您不小心提交了包含密钥的文件，请立即：

**1. 立即撤销密钥**
```bash
# 访问 https://makersuite.google.com/app/apikey
# 删除或重新生成API密钥
```

**2. 从Git历史中删除敏感信息**
```bash
# 使用 git filter-branch 或 BFG Repo-Cleaner
# 删除历史记录中的敏感文件

# 简单方法（会重写所有历史）
git filter-branch --force --index-filter \
  "git rm --cached --ignore-unmatch .env" \
  --prune-empty --tag-name-filter cat -- --all

# 强制推送（慎用！）
git push origin --force --all
```

**3. 通知GitHub**
```bash
# 如果仓库是公开的，考虑删除整个仓库重新创建
# 或者使用GitHub的密钥扫描功能检测
```

## ✅ 安全检查清单总结

提交到GitHub前，确认以下所有项目：

- [ ] `.env` 文件在 `.gitignore` 中
- [ ] `run.sh` 不包含硬编码的密钥
- [ ] 运行 `git status` 确认没有敏感文件
- [ ] 运行 `grep -r "AIzaSy" .` 确认密钥只在 `.env` 中
- [ ] `.env.example` 只包含模板，不包含真实密钥
- [ ] `outputs/` 目录被忽略（避免提交大量图片）
- [ ] `venv/` 目录被忽略（避免提交依赖包）

## 📝 .env.example 使用说明

**给其他协作者的说明**：

1. 克隆仓库后，复制 `.env.example` 为 `.env`：
   ```bash
   cp .env.example .env
   ```

2. 编辑 `.env`，填入自己的API密钥：
   ```bash
   GEMINI_API_KEY=你的实际密钥
   ```

3. `.env` 文件会被Git忽略，不用担心提交

## 🔐 最佳实践

### DO ✓

- ✓ 使用 `.env` 文件存储密钥
- ✓ 将 `.env` 添加到 `.gitignore`
- ✓ 提供 `.env.example` 作为模板
- ✓ 定期轮换API密钥
- ✓ 使用环境变量而非硬编码
- ✓ 提交前运行 `git status` 检查

### DON'T ✗

- ✗ 在代码中硬编码密钥
- ✗ 将 `.env` 提交到Git
- ✗ 在公共仓库中存储密钥
- ✗ 在 README 中包含真实密钥
- ✗ 通过邮件或聊天发送密钥
- ✗ 使用同一密钥在多个项目

## 🛡️ 额外安全建议

1. **使用GitHub Secrets**（如果使用GitHub Actions）
   - 在仓库设置中添加密钥
   - 在工作流中通过 `${{ secrets.GEMINI_API_KEY }}` 使用

2. **限制API密钥权限**
   - 只授予必要的API权限
   - 设置API配额限制

3. **监控API使用**
   - 定期检查API使用情况
   - 发现异常立即撤销密钥

4. **使用密钥管理服务**（生产环境）
   - AWS Secrets Manager
   - HashiCorp Vault
   - Azure Key Vault

---

**当前状态**: ✅ 您的项目已正确配置，可以安全提交到GitHub！
```

## File: `SETUP_COMPLETE.md`
```markdown
# 环境配置完成！

## ✅ 已完成的配置

### 1. Python依赖安装 ✓
- google-genai (1.57.0)
- pillow (12.1.0)
- 所有依赖项已安装在虚拟环境中

### 2. API密钥配置 ✓
- GEMINI_API_KEY 已设置
- 密钥存储在 .env 文件中
- .gitignore 已配置，防止密钥泄露

### 3. 便捷脚本创建 ✓
- run.sh: 自动激活虚拟环境和设置API密钥的启动脚本

## 🚀 现在可以使用了！

### 方式1: 使用便捷脚本（推荐）

```bash
# 直接运行，自动处理环境
./run.sh --plan ../test_slides_plan.json --style styles/gradient-glass.md --resolution 2K
```

### 方式2: 手动激活环境

```bash
# 激活虚拟环境
source venv/bin/activate

# 设置API密钥（如果需要）
export GEMINI_API_KEY="your-api-key-here"

# 运行脚本
python generate_ppt.py --plan ../test_slides_plan.json --style styles/gradient-glass.md --resolution 2K
```

### 方式3: 在Claude Code中使用（最简单）

只需要在Claude Code中说：

```
我想基于"莫伊兰箭.md"文档生成一个5页的PPT
```

Claude会自动处理所有步骤。

## 🧪 快速测试

我已经为您创建了一个测试规划文件 `test_slides_plan.json`，包含5页关于"莫伊兰箭"的PPT内容。

### 运行测试：

```bash
cd /Users/guohao/Documents/code/ppt/ppt-generator
./run.sh --plan ../test_slides_plan.json --style styles/gradient-glass.md --resolution 2K
```

### 生成说明：
- 每页大约需要30秒
- 5页总共约2.5分钟
- 生成完成后会显示输出路径

### 查看结果：

```bash
# 打开播放器（生成完成后会显示具体路径）
open outputs/TIMESTAMP/index.html
```

## 📁 项目文件说明

```
ppt-generator/
├── run.sh                    # 便捷启动脚本（推荐使用）
├── .env                      # API密钥配置文件
├── .gitignore               # Git忽略文件（保护密钥）
├── venv/                    # Python虚拟环境
├── generate_ppt.py          # 核心生成脚本
├── ppt-generator.md         # Skill定义
├── README.md                # 项目说明
├── QUICKSTART.md            # 快速开始指南
├── styles/                  # 风格库
│   └── gradient-glass.md    # 渐变毛玻璃卡片风格
├── templates/               # HTML模板
│   └── viewer.html          # PPT播放器
└── outputs/                 # 生成结果（自动创建）
```

## ⚙️ 环境变量

API密钥已配置在：
1. **run.sh** - 启动脚本中自动加载
2. **.env** - 环境变量文件

**重要提醒**：
- ⚠️ 不要将 .env 文件提交到公共代码仓库
- ⚠️ API密钥已包含在 .gitignore 中
- ⚠️ 如需分享项目，删除 .env 文件中的密钥

## 🎯 下一步

### 选项1: 立即测试
```bash
./run.sh --plan ../test_slides_plan.json --style styles/gradient-glass.md --resolution 2K
```

### 选项2: 生成自己的PPT
1. 准备您的文档（Markdown或文本）
2. 在Claude Code中说明您的需求
3. Claude会自动分析文档并生成PPT

### 选项3: 查看文档
- `README.md` - 完整项目说明
- `QUICKSTART.md` - 快速上手指南
- `ppt-generator.md` - 详细技术文档

## 💡 使用技巧

### 分辨率选择：
- **2K (2752x1536)**: 日常使用，快速生成
- **4K (5504x3072)**: 重要场合，高质量输出

### 页数建议：
- **5页**: 5分钟快速演讲
- **5-10页**: 15分钟标准演示
- **10-15页**: 30分钟深入讲解
- **20-25页**: 60分钟完整展示

### 播放器快捷键：
- `←` `→`: 切换页面
- `↑` `Home`: 首页
- `↓` `End`: 末页
- `空格`: 自动播放/暂停
- `ESC`: 全屏切换
- `H`: 隐藏/显示控件

## 🆘 遇到问题？

### 环境问题
```bash
# 重新激活虚拟环境
source venv/bin/activate

# 检查依赖
pip list | grep genai
```

### API问题
```bash
# 检查API密钥
echo $GEMINI_API_KEY

# 手动设置（如果需要）
export GEMINI_API_KEY="your-key"
```

### 生成失败
1. 检查网络连接
2. 确认API密钥有效
3. 降低分辨率重试
4. 查看详细错误信息

## 🎉 准备就绪！

您的PPT生成器已经完全配置好了，可以开始使用了！

**推荐第一步**：运行测试命令，体验完整流程。

```bash
./run.sh --plan ../test_slides_plan.json --style styles/gradient-glass.md --resolution 2K
```

祝您使用愉快！🚀
```

## File: `SKILL.md`
```markdown
# PPT Generator Pro - Claude Code Skill

## 📋 元数据

- **Skill 名称**: ppt-generator-pro
- **版本**: 2.0.0
- **描述**: 基于 AI 自动生成高质量 PPT 图片和视频，支持智能转场和交互式播放
- **作者**: 歸藏
- **标签**: ppt, presentation, video, ai, nano-banana, kling-ai, image-generation

## ✨ 功能特性

### 核心功能
- 🤖 **智能文档分析** - 自动提取核心要点，规划 PPT 内容结构
- 🎨 **多风格支持** - 内置渐变毛玻璃、矢量插画两种专业风格
- 🖼️ **高质量图片** - 使用 Nano Banana Pro 生成 16:9 高清 PPT
- 🎬 **AI 转场视频** - 可灵 AI 生成流畅的页面过渡动画
- 🎮 **交互式播放器** - 视频+图片混合播放，支持键盘导航
- 🎥 **完整视频导出** - FFmpeg 合成包含所有转场的完整 PPT 视频

### 新功能 (v2.0)
- 🔄 **首页循环预览** - 自动生成吸引眼球的循环动画
- 🎞️ **智能转场** - 自动生成页面间的过渡视频
- 🔧 **参数统一** - 自动统一所有视频分辨率和帧率

## 📦 系统要求

### 环境变量

**必需：**
- `GEMINI_API_KEY`: Google AI API 密钥（用于生成 PPT 图片）

**可选（用于视频功能）：**
- `KLING_ACCESS_KEY`: 可灵 AI Access Key
- `KLING_SECRET_KEY`: 可灵 AI Secret Key

### Python 依赖

```bash
pip install google-genai pillow python-dotenv
```

### 视频功能依赖

```bash
# macOS
brew install ffmpeg

# Ubuntu/Debian
sudo apt-get install ffmpeg
```

## 🚀 使用方法

### 在 Claude Code 中调用

```bash
/ppt-generator-pro
```

或直接告诉 Claude：

```
我想基于以下文档生成一个 5 页的 PPT，使用渐变毛玻璃风格。

[文档内容...]
```

## 📝 Skill 执行流程

### 阶段 1: 收集用户输入

#### 1.1 获取文档内容

**选项 A: 文档路径**
```
用户: 基于 my-document.md 生成 PPT
→ 使用 Read 工具读取文件内容
```

**选项 B: 直接文本**
```
用户: 我想生成一个关于 AI 产品设计的 PPT
主要内容：
1. 现状分析
2. 设计原则
3. 案例研究
```

**选项 C: 主动询问**
```
如果用户未提供内容，询问：
"请提供文档路径或直接粘贴文档内容"
```

#### 1.2 选择风格

扫描 `styles/` 目录，列出可用风格：

```python
# 自动检测风格文件
styles = ['gradient-glass.md', 'vector-illustration.md']
```

**如果有多个风格，使用 AskUserQuestion：**

```markdown
问题: 请选择 PPT 风格
选项:
- 渐变毛玻璃卡片风格（科技感、商务演示）
- 矢量插画风格（温暖、教育培训）
```

#### 1.3 选择页数范围

使用 AskUserQuestion 询问：

```markdown
问题: 希望生成多少页 PPT？
选项:
- 5 页（5 分钟演讲）
- 5-10 页（10-15 分钟演讲）
- 10-15 页（20-30 分钟演讲）
- 20-25 页（45-60 分钟演讲）
```

#### 1.4 选择分辨率

```markdown
问题: 选择图片分辨率
选项:
- 2K (2752x1536) - 推荐，快速生成
- 4K (5504x3072) - 高质量，适合打印
```

#### 1.5 是否生成视频（可选）

如果配置了可灵 AI 密钥，询问：

```markdown
问题: 是否生成转场视频？
选项:
- 仅图片（快速）
- 图片 + 转场视频（完整体验）
```

### 阶段 2: 文档分析与内容规划

#### 2.1 内容规划策略

根据页数范围，智能规划每一页内容：

**5 页版本：**
1. 封面：标题 + 核心主题
2. 要点 1：第一个核心观点
3. 要点 2：第二个核心观点
4. 要点 3：第三个核心观点
5. 总结：核心结论或行动建议

**5-10 页版本：**
1. 封面
2-3. 引言/背景
4-7. 核心内容（3-4 个关键观点）
8-9. 案例或数据支持
10. 总结与行动建议

**10-15 页版本：**
1. 封面
2-3. 引言/目录
4-6. 第一章节（3 页）
7-9. 第二章节（3 页）
10-12. 第三章节/案例研究
13-14. 数据可视化
15. 总结与下一步

**20-25 页版本：**
1. 封面
2. 目录
3-4. 引言和背景
5-8. 第一部分（4 页）
9-12. 第二部分（4 页）
13-16. 第三部分（4 页）
17-19. 案例研究
20-22. 数据分析和洞察
23-24. 关键发现和建议
25. 总结与致谢

#### 2.2 生成 slides_plan.json

创建 JSON 文件：

```json
{
  "title": "文档标题",
  "total_slides": 5,
  "slides": [
    {
      "slide_number": 1,
      "page_type": "cover",
      "content": "标题：AI 产品设计指南\n副标题：构建以用户为中心的智能体验"
    },
    {
      "slide_number": 2,
      "page_type": "content",
      "content": "核心原则\n- 简单直观\n- 快速响应\n- 透明可控"
    },
    {
      "slide_number": 3,
      "page_type": "content",
      "content": "设计流程\n1. 用户研究\n2. 原型设计\n3. 测试迭代"
    },
    {
      "slide_number": 4,
      "page_type": "data",
      "content": "用户满意度\n使用前：65%\n使用后：92%\n提升：+27%"
    },
    {
      "slide_number": 5,
      "page_type": "content",
      "content": "总结\n- 以用户为中心\n- 持续优化迭代\n- 数据驱动决策"
    }
  ]
}
```

**重要：** 将此文件保存到：
- 独立使用：`./slides_plan.json`
- Skill 模式：`.claude/skills/ppt-generator/slides_plan.json`

### 阶段 3: 生成 PPT 图片

#### 3.1 确定工作目录

**独立模式：**
```bash
cd /path/to/ppt-generator
```

**Skill 模式：**
```bash
cd ~/.claude/skills/ppt-generator
```

#### 3.2 执行生成命令

```bash
python generate_ppt.py \
  --plan slides_plan.json \
  --style styles/gradient-glass.md \
  --resolution 2K
```

**或使用 uv run（推荐）：**
```bash
uv run python generate_ppt.py \
  --plan slides_plan.json \
  --style styles/gradient-glass.md \
  --resolution 2K
```

**参数说明：**
- `--plan`: slides 规划 JSON 文件路径
- `--style`: 风格文件路径
- `--resolution`: 分辨率（2K 或 4K）
- `--template`: HTML 模板路径（可选）

#### 3.3 监控生成进度

脚本会输出进度信息：

```
✅ 已加载环境变量: /path/to/.env
📊 开始生成 PPT 图片...
   总页数: 5
   分辨率: 2K (2752x1536)
   风格: 渐变毛玻璃卡片风格

🎨 生成第 1 页 (封面页)...
   提示词已生成
   调用 Nano Banana Pro API...
   ✅ 第 1 页生成成功 (32.5 秒)

🎨 生成第 2 页 (内容页)...
   ✅ 第 2 页生成成功 (28.3 秒)

...

✅ 所有页面生成完成！
📁 输出目录: outputs/20260112_143022/
```

### 阶段 4: 生成转场提示词（视频模式需要）

**这是 Skill 的核心优势**：我（Claude Code）会分析生成的 PPT 图片，为每个转场生成精准的视频提示词。

#### 4.1 读取并分析 PPT 图片

我会读取所有生成的图片：

```python
# 自动读取输出目录中的所有图片
slides = ['slide-01.png', 'slide-02.png', ...]
```

#### 4.2 分析图片差异并生成提示词

对于每对相邻图片，我会：
1. **视觉分析**：理解两张图片的布局、元素、色彩差异
2. **生成预览提示词**：为首页创建可循环的微动效描述
3. **生成转场提示词**：详细描述如何从起始帧过渡到结束帧

**示例输出：**
```json
{
  "preview": {
    "slide_path": "outputs/.../slide-01.png",
    "prompt": "画面保持封面的静态构图，中心的3D玻璃环缓慢旋转..."
  },
  "transitions": [
    {
      "from_slide": 1,
      "to_slide": 2,
      "prompt": "镜头从封面开始，玻璃环逐渐解构，分裂成透明碎片..."
    }
  ]
}
```

#### 4.3 保存提示词文件

我会将生成的提示词保存到：
```
outputs/TIMESTAMP/transition_prompts.json
```

**关键优势：**
- ✅ 不需要单独的 Claude API 密钥
- ✅ 提示词针对实际图片内容定制
- ✅ 考虑文字稳定性，避免视频模型弄模糊文字
- ✅ 符合渐变毛玻璃风格的视觉语言

### 阶段 5: 生成转场视频（可选）

如果用户选择生成视频，使用阶段 4 生成的提示词文件：

```bash
python generate_ppt_video.py \
  --slides-dir outputs/20260112_143022/images \
  --output-dir outputs/20260112_143022_video \
  --prompts-file outputs/20260112_143022/transition_prompts.json
```

**生成内容：**
- 首页循环预览视频（`preview.mp4`）
- 页面间转场视频（`transition_01_to_02.mp4` 等）
- 交互式视频播放器（`video_index.html`）
- 完整视频（`full_ppt_video.mp4`）

### 阶段 6: 返回结果

#### 6.1 仅图片模式

```
✅ PPT 生成成功！

📁 输出目录: outputs/20260112_143022/
🖼️ PPT 图片: outputs/20260112_143022/images/
🎬 播放网页: outputs/20260112_143022/index.html

打开播放网页:
open outputs/20260112_143022/index.html

播放器快捷键:
- ← → 键: 切换页面
- ↑ Home: 回到首页
- ↓ End: 跳到末页
- 空格: 暂停/继续自动播放
- ESC: 全屏切换
- H: 隐藏/显示控件
```

#### 5.2 视频模式

```
✅ PPT 视频生成成功！

📁 输出目录: outputs/20260112_143022_video/
🖼️ PPT 图片: outputs/20260112_143022/images/
🎬 转场视频: outputs/20260112_143022_video/videos/
🎮 交互式播放器: outputs/20260112_143022_video/video_index.html
🎥 完整视频: outputs/20260112_143022_video/full_ppt_video.mp4

打开交互式播放器:
open outputs/20260112_143022_video/video_index.html

播放逻辑:
1. 首页: 播放循环预览视频
2. 按右键 → 播放转场视频 → 显示目标页图片（2 秒）
3. 再按右键 → 播放下一个转场 → 显示下一页图片
4. 依此类推...

视频播放器快捷键:
- ← → 键: 上一页/下一页（含转场）
- 空格: 播放/暂停当前视频
- ESC: 全屏切换
- H: 隐藏/显示控件
```

## 🔧 环境变量配置

### .env 文件位置

Skill 会按以下顺序查找 `.env` 文件：

1. **脚本所在目录** - `./ppt-generator/.env`
2. **向上查找项目根目录** - 直到找到包含 `.git` 或 `.env` 的目录
3. **Claude Skill 标准位置** - `~/.claude/skills/ppt-generator/.env`
4. **系统环境变量** - 如果以上都未找到

### .env 文件示例

```bash
# Google AI API 密钥（必需）
GEMINI_API_KEY=your_gemini_api_key_here

# 可灵 AI API 密钥（可选，用于视频功能）
KLING_ACCESS_KEY=your_kling_access_key_here
KLING_SECRET_KEY=your_kling_secret_key_here
```

## ⚠️ 错误处理

### 常见错误及解决方案

**1. API 密钥未设置**
```
错误: ⚠️ 未找到 .env 文件，尝试使用系统环境变量
      未设置 GEMINI_API_KEY 环境变量

解决:
1. 创建 .env 文件
2. 添加 GEMINI_API_KEY=your_key_here
```

**2. Python 依赖缺失**
```
错误: ModuleNotFoundError: No module named 'google.genai'

解决: pip install google-genai pillow python-dotenv
```

**3. FFmpeg 未安装**
```
错误: ❌ FFmpeg 不可用！

解决: brew install ffmpeg  # macOS
      sudo apt-get install ffmpeg  # Ubuntu
```

**4. API 调用失败**
```
错误: API 调用超时或失败

解决:
1. 检查网络连接
2. 确认 API 密钥有效
3. 稍后重试
```

**5. 视频生成失败**
```
错误: 可灵 AI 密钥未配置

解决:
1. 如果只需要图片，跳过视频生成步骤
2. 如果需要视频，配置 KLING_ACCESS_KEY 和 KLING_SECRET_KEY
```

## 🎨 风格系统

### 已内置风格

#### 1. 渐变毛玻璃卡片风格 (`gradient-glass.md`)

**视觉特点：**
- Apple Keynote 极简主义
- 玻璃拟态效果
- 霓虹紫/电光蓝/珊瑚橙渐变
- 3D 玻璃物体 + 电影级光照

**适用场景：**
- 科技产品发布
- 商务演示
- 数据报告
- 企业品牌展示

#### 2. 矢量插画风格 (`vector-illustration.md`)

**视觉特点：**
- 扁平化矢量设计
- 统一黑色轮廓线
- 复古柔和配色
- 几何化简化

**适用场景：**
- 教育培训
- 创意提案
- 儿童相关
- 温暖品牌故事

### 添加自定义风格

1. 在 `styles/` 目录创建新的 `.md` 文件
2. 按照现有风格格式编写
3. Skill 会自动识别并提供选择

## 📊 技术细节

### API 配置

**Nano Banana Pro（图片生成）：**
- 模型：`gemini-3-pro-image-preview`
- 比例：`16:9`
- 响应模式：`IMAGE`
- 分辨率：2K (2752x1536) 或 4K (5504x3072)

**可灵 AI（视频生成）：**
- 模式：专业模式（professional）
- 时长：5 秒
- 分辨率：1920x1080
- 帧率：24fps

**FFmpeg（视频合成）：**
- 编码：H.264
- 质量：CRF 23
- 帧率：24fps（统一）
- 分辨率：1920x1080（统一）

### 性能指标

**生成速度：**
- PPT 图片：~30 秒/页（2K）| ~60 秒/页（4K）
- 转场视频：~30-60 秒/段
- 视频合成：~5-10 秒

**文件大小：**
- PPT 图片：~2.5MB/页（2K）| ~8MB/页（4K）
- 转场视频：~3-5MB/段（1080p，5 秒）
- 完整视频：~12-20MB（5 页 PPT + 转场）

## 📁 文件组织

### 输出目录结构

**仅图片模式：**
```
outputs/20260112_143022/
├── images/
│   ├── slide-01.png
│   ├── slide-02.png
│   └── ...
├── index.html          # 图片播放器
└── prompts.json        # 提示词记录
```

**视频模式：**
```
outputs/20260112_143022_video/
├── videos/
│   ├── preview.mp4              # 首页循环预览
│   ├── transition_01_to_02.mp4
│   ├── transition_02_to_03.mp4
│   └── ...
├── video_index.html             # 交互式播放器
└── full_ppt_video.mp4           # 完整视频
```

## 🎯 最佳实践

1. **文档质量**：输入文档内容越清晰结构化，生成的 PPT 质量越高
2. **页数选择**：根据文档长度和演示场景合理选择页数
3. **分辨率选择**：日常使用推荐 2K，重要展示场合可选 4K
4. **视频功能**：首次使用建议先尝试仅图片模式，熟悉后再使用视频功能
5. **提示词调整**：查看 `prompts.json` 了解生成逻辑，可手动调整后重新生成

## 📝 使用示例

### 示例 1: 快速生成

**用户输入：**
```
我需要基于这份会议纪要生成一个 5 页的 PPT，使用矢量插画风格。

会议主题：Q1 产品路线图规划
参与人：产品团队

讨论内容：
1. 用户反馈汇总
2. 新功能优先级
3. 技术可行性评估
4. Q1 里程碑
5. 下一步行动项
```

**Skill 执行：**
1. 收集输入（已提供内容）
2. 确认风格（矢量插画）
3. 确认页数（5 页）
4. 确认分辨率（询问用户）
5. 生成 slides_plan.json
6. 执行生成命令
7. 返回结果

### 示例 2: 完整流程

**用户输入：**
```
基于 AI-Product-Design.md 文档，生成一个 15 页的 PPT，使用渐变毛玻璃风格，需要转场视频。
```

**Skill 执行：**
1. 读取文档内容
2. 确认风格（渐变毛玻璃）
3. 确认页数（15 页）
4. 确认分辨率（询问用户）
5. 确认生成视频（是）
6. 分析文档，规划 15 页内容
7. 生成 slides_plan.json
8. 生成 PPT 图片
9. 生成转场视频
10. 合成完整视频
11. 返回所有结果

## 🔄 更新日志

### v2.0.0 (2026-01-12)

- 🎬 **新增视频功能**
  - 可灵 AI 转场视频生成
  - 交互式视频播放器
  - FFmpeg 完整视频合成
  - 首页循环预览视频
- 🔧 **优化视频合成**
  - 自动统一分辨率和帧率
  - 修复视频拼接兼容性问题
  - 静态图片展示时间改为 2 秒
- 🔑 **改进环境变量**
  - 智能查找 .env 文件
  - 支持多种部署模式
  - 自动向上查找项目根目录
- 📚 **文档完善**
  - 重命名为 SKILL.md（符合官方规范）
  - 更新所有路径和命令
  - 添加视频功能使用指南

### v1.0.0 (2026-01-09)

- ✨ 首次发布
- 🎨 内置 2 种专业风格
- 🖼️ 支持 2K/4K 分辨率
- 🎬 HTML5 图片播放器
- 📊 智能文档分析

## 📄 许可证

MIT License

## 📞 技术支持

- 项目架构：参见 `ARCHITECTURE.md`
- API 管理：参见 `API_MANAGEMENT.md`
- 环境配置：参见 `ENV_SETUP.md`
- 安全说明：参见 `SECURITY.md`
- 完整文档：参见 `README.md`
```

## File: `generate_ppt.py`
```python
#!/usr/bin/env python3
"""
PPT Generator - Generate PPT slide images using Google Gemini API.

This script generates PPT slide images based on a slide plan and style template,
then creates an HTML viewer for playback.
"""

import argparse
import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

from dotenv import load_dotenv


# =============================================================================
# Constants
# =============================================================================

DEFAULT_RESOLUTION = "2K"
DEFAULT_TEMPLATE_PATH = "templates/viewer.html"
OUTPUT_BASE_DIR = "outputs"

# Style template markers
TEMPLATE_START_MARKER = "## "
TEMPLATE_END_MARKER = "## "


# =============================================================================
# Environment Configuration
# =============================================================================

def find_and_load_env() -> bool:
    """
    Find and load .env file from multiple locations.

    Search priority:
    1. Current script directory
    2. Parent directories up to project root (containing .git or .env)
    3. Claude Code skill standard location (~/.claude/skills/ppt-generator/)

    Returns:
        True if .env file was found and loaded, False otherwise.
    """
    current_dir = Path(__file__).parent
    env_locations = [
        current_dir / ".env",
        *[parent / ".env" for parent in current_dir.parents],
        Path.home() / ".claude" / "skills" / "ppt-generator" / ".env",
    ]

    for env_path in env_locations:
        if env_path.exists():
            load_dotenv(env_path, override=True)
            print(f"Loaded environment from: {env_path}")
            return True

        # Stop at project root if .git exists
        if env_path.parent != current_dir and (env_path.parent / ".git").exists():
            break

    # Fallback: try default loading from system environment
    load_dotenv(override=True)
    print("Warning: No .env file found, using system environment variables")
    return False


# =============================================================================
# Style Template
# =============================================================================

def load_style_template(style_path: str) -> str:
    """
    Load and parse style template file.

    Args:
        style_path: Path to the style template markdown file.

    Returns:
        Extracted base prompt template string.
    """
    with open(style_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract base prompt template section
    start_marker = "## "
    end_marker = "## "

    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker, start_idx + len(start_marker))

    if start_idx == -1 or end_idx == -1:
        print("Warning: Could not parse style template, using full content")
        return content

    return content[start_idx + len(start_marker):end_idx].strip()


# =============================================================================
# Prompt Generation
# =============================================================================

def generate_prompt(
    style_template: str,
    page_type: str,
    content_text: str,
    slide_number: int,
    total_slides: int,
) -> str:
    """
    Generate a prompt for a single slide.

    Args:
        style_template: Base style template text.
        page_type: Type of page (cover, data, content).
        content_text: Text content for the slide.
        slide_number: Current slide number (1-indexed).
        total_slides: Total number of slides.

    Returns:
        Complete prompt string for image generation.
    """
    prompt_parts = [style_template, "\n\n"]

    # Determine page type based on slide position or explicit type
    is_cover = page_type == "cover" or slide_number == 1
    is_data = page_type == "data" or slide_number == total_slides

    if is_cover:
        prompt_parts.append(
            f"""Please generate a cover page based on visual balance aesthetics.
Place a large complex 3D glass object in the center, overlaid with bold text:

{content_text}

Background with extended aurora waves."""
        )
    elif is_data:
        prompt_parts.append(
            f"""Please generate a data/summary page using split-screen design.
Left side: typeset the following text.
Right side: floating large glowing 3D data visualization:

{content_text}"""
        )
    else:
        prompt_parts.append(
            f"""Please generate a content page using Bento grid layout.
Organize the following content in modular rounded rectangle containers.
Container material must be frosted glass with blur effect:

{content_text}"""
        )

    return "".join(prompt_parts)


# =============================================================================
# Image Generation
# =============================================================================

def get_gemini_client():
    """
    Initialize and return Gemini API client.

    Returns:
        Configured genai.Client instance.

    Raises:
        SystemExit: If google-genai is not installed or API key is missing.
    """
    try:
        from google import genai
    except ImportError:
        print("Error: google-genai library not installed")
        print("Please run: pip install google-genai")
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable not set")
        print("Please set: export GEMINI_API_KEY='your-api-key'")
        sys.exit(1)

    return genai.Client(api_key=api_key)


def generate_slide(
    prompt: str,
    slide_number: int,
    output_dir: str,
    resolution: str = DEFAULT_RESOLUTION,
) -> Optional[str]:
    """
    Generate a single PPT slide image using Gemini API.

    Args:
        prompt: The generation prompt.
        slide_number: Slide number for filename.
        output_dir: Output directory path.
        resolution: Image resolution (2K or 4K).

    Returns:
        Path to saved image, or None if generation failed.
    """
    from google.genai import types

    print(f"Generating slide {slide_number}...")

    try:
        client = get_gemini_client()
        response = client.models.generate_content(
            model="gemini-3-pro-image-preview",
            contents=prompt,
            config=types.GenerateContentConfig(
                response_modalities=["IMAGE"],
                image_config=types.ImageConfig(
                    aspect_ratio="16:9",
                    image_size=resolution,
                ),
            ),
        )

        for part in response.parts:
            if part.inline_data is not None:
                image = part.as_image()
                image_path = os.path.join(
                    output_dir, "images", f"slide-{slide_number:02d}.png"
                )
                image.save(image_path)
                print(f"  Slide {slide_number} saved: {image_path}")
                return image_path

        print(f"  Slide {slide_number} failed: No image data received")
        return None

    except Exception as e:
        print(f"  Slide {slide_number} failed: {e}")
        return None


# =============================================================================
# Output Generation
# =============================================================================

def generate_viewer_html(
    output_dir: str,
    slide_count: int,
    template_path: str,
) -> str:
    """
    Generate HTML viewer for slides playback.

    Args:
        output_dir: Output directory path.
        slide_count: Total number of slides.
        template_path: Path to HTML template.

    Returns:
        Path to generated HTML file.
    """
    with open(template_path, "r", encoding="utf-8") as f:
        html_template = f.read()

    # Generate image list
    slides_list = [f"'images/slide-{i:02d}.png'" for i in range(1, slide_count + 1)]

    # Replace placeholder
    html_content = html_template.replace(
        "/* IMAGE_LIST_PLACEHOLDER */",
        ",\n            ".join(slides_list),
    )

    html_path = os.path.join(output_dir, "index.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"  Viewer HTML generated: {html_path}")
    return html_path


def save_prompts(output_dir: str, prompts_data: Dict[str, Any]) -> str:
    """
    Save all prompts to JSON file.

    Args:
        output_dir: Output directory path.
        prompts_data: Dictionary containing all prompts and metadata.

    Returns:
        Path to saved JSON file.
    """
    prompts_path = os.path.join(output_dir, "prompts.json")
    with open(prompts_path, "w", encoding="utf-8") as f:
        json.dump(prompts_data, f, ensure_ascii=False, indent=2)
    print(f"  Prompts saved: {prompts_path}")
    return prompts_path


# =============================================================================
# Main Entry Point
# =============================================================================

def create_argument_parser() -> argparse.ArgumentParser:
    """Create and configure argument parser."""
    parser = argparse.ArgumentParser(
        description="PPT Generator - Generate PPT images using Gemini API",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Example usage:
  python generate_ppt.py --plan slides_plan.json --style styles/gradient-glass.md --resolution 2K

Environment variables:
  GEMINI_API_KEY: Google AI API key (required)
""",
    )

    parser.add_argument(
        "--plan",
        required=True,
        help="Path to slides plan JSON file (generated by Skill)",
    )
    parser.add_argument(
        "--style",
        required=True,
        help="Path to style template file",
    )
    parser.add_argument(
        "--resolution",
        choices=["2K", "4K"],
        default=DEFAULT_RESOLUTION,
        help=f"Image resolution (default: {DEFAULT_RESOLUTION})",
    )
    parser.add_argument(
        "--output",
        help="Output directory path (default: outputs/TIMESTAMP)",
    )
    parser.add_argument(
        "--template",
        default=DEFAULT_TEMPLATE_PATH,
        help=f"HTML template path (default: {DEFAULT_TEMPLATE_PATH})",
    )

    return parser


def main() -> None:
    """Main entry point for PPT generation."""
    # Load environment variables
    find_and_load_env()

    # Parse arguments
    parser = create_argument_parser()
    args = parser.parse_args()

    # Load slides plan
    with open(args.plan, "r", encoding="utf-8") as f:
        slides_plan = json.load(f)

    # Load style template
    style_template = load_style_template(args.style)

    # Create output directory
    if args.output:
        output_dir = args.output
    else:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_dir = f"{OUTPUT_BASE_DIR}/{timestamp}"

    os.makedirs(os.path.join(output_dir, "images"), exist_ok=True)

    # Print configuration
    slides = slides_plan["slides"]
    total_slides = len(slides)

    print("=" * 60)
    print("PPT Generator Started")
    print("=" * 60)
    print(f"Style: {args.style}")
    print(f"Resolution: {args.resolution}")
    print(f"Slides: {total_slides}")
    print(f"Output: {output_dir}")
    print("=" * 60)
    print()

    # Initialize prompts data
    prompts_data: Dict[str, Any] = {
        "metadata": {
            "title": slides_plan.get("title", "Untitled Presentation"),
            "total_slides": total_slides,
            "resolution": args.resolution,
            "style": args.style,
            "generated_at": datetime.now().isoformat(),
        },
        "slides": [],
    }

    # Generate each slide
    for slide_info in slides:
        slide_number = slide_info["slide_number"]
        page_type = slide_info.get("page_type", "content")
        content_text = slide_info["content"]

        # Generate prompt
        prompt = generate_prompt(
            style_template,
            page_type,
            content_text,
            slide_number,
            total_slides,
        )

        # Generate image
        image_path = generate_slide(prompt, slide_number, output_dir, args.resolution)

        # Record prompt data
        prompts_data["slides"].append({
            "slide_number": slide_number,
            "page_type": page_type,
            "content": content_text,
            "prompt": prompt,
            "image_path": image_path,
        })

        print()

    # Save prompts
    save_prompts(output_dir, prompts_data)

    # Generate viewer HTML
    generate_viewer_html(output_dir, total_slides, args.template)

    # Print completion summary
    print()
    print("=" * 60)
    print("Generation Complete!")
    print("=" * 60)
    print(f"Output directory: {output_dir}")
    print(f"Viewer HTML: {os.path.join(output_dir, 'index.html')}")
    print()
    print("Open viewer in browser:")
    print(f"  open {os.path.join(output_dir, 'index.html')}")
    print()


if __name__ == "__main__":
    main()
```

## File: `generate_ppt_video.py`
```python
#!/usr/bin/env python3
"""
PPT Video Generator - Generate videos with transitions from PPT slide images.

This script integrates image processing, video material generation, and video
composition to create complete PPT presentation videos.
"""

import argparse
import json
import os
import sys
import traceback
from pathlib import Path
from typing import Any, Dict, List, Optional

from dotenv import load_dotenv

from video_composer import VideoComposer
from video_materials import VideoMaterialsGenerator


# =============================================================================
# Constants
# =============================================================================

DEFAULT_VIDEO_MODE = "both"
DEFAULT_VIDEO_DURATION = "5"
DEFAULT_SLIDE_DURATION = 5
DEFAULT_VIDEO_QUALITY = "pro"
DEFAULT_MAX_CONCURRENT = 3


# =============================================================================
# Video Generation
# =============================================================================

def scan_slide_images(slides_dir: str) -> List[str]:
    """
    Scan directory for PPT slide images.

    Args:
        slides_dir: Directory containing slide images.

    Returns:
        Sorted list of slide image paths.

    Raises:
        FileNotFoundError: If no slide images are found.
    """
    slides_paths = sorted(Path(slides_dir).glob("slide-*.png"))

    if not slides_paths:
        raise FileNotFoundError(
            f"No PPT images found in {slides_dir} (expected format: slide-*.png)"
        )

    return [str(p) for p in slides_paths]


def create_output_directories(output_dir: str) -> str:
    """
    Create output directory structure.

    Args:
        output_dir: Base output directory.

    Returns:
        Path to videos subdirectory.
    """
    os.makedirs(output_dir, exist_ok=True)
    videos_dir = os.path.join(output_dir, "videos")
    os.makedirs(videos_dir, exist_ok=True)
    return videos_dir


def generate_ppt_video_from_images(
    slides_dir: str,
    output_dir: str,
    video_mode: str = DEFAULT_VIDEO_MODE,
    video_duration: str = DEFAULT_VIDEO_DURATION,
    slide_duration: int = DEFAULT_SLIDE_DURATION,
    video_quality: str = DEFAULT_VIDEO_QUALITY,
    max_concurrent: int = DEFAULT_MAX_CONCURRENT,
    skip_preview: bool = False,
    prompts_file: Optional[str] = None,
) -> Optional[Dict[str, Any]]:
    """
    Generate video from existing PPT images.

    Args:
        slides_dir: Directory containing PPT slide images.
        output_dir: Output directory for generated videos.
        video_mode: Output mode - both/local/web.
        video_duration: Transition video duration (5 or 10 seconds).
        slide_duration: Duration for each slide (seconds).
        video_quality: Video quality (std/pro).
        max_concurrent: Maximum concurrent video generation tasks.
        skip_preview: Whether to skip preview video generation.
        prompts_file: Path to transition prompts JSON file.

    Returns:
        Result dictionary with generation statistics, or None on failure.
    """
    print("\n" + "=" * 80)
    print("PPT Video Generation - Full Pipeline")
    print("=" * 80)

    # Phase 1: Scan slide images
    print(f"\nScanning slides directory: {slides_dir}")
    try:
        slides_paths = scan_slide_images(slides_dir)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None

    num_slides = len(slides_paths)
    print(f"Found {num_slides} slides:")
    for i, path in enumerate(slides_paths, 1):
        print(f"  {i}. {Path(path).name}")

    # Phase 2: Create output directories
    videos_dir = create_output_directories(output_dir)
    print(f"\nOutput directory: {output_dir}")
    print(f"  Videos: {videos_dir}/")

    # Phase 3: Generate video materials
    print("\n" + "=" * 80)
    print("Phase 1: Generate Video Materials (Preview + Transitions)")
    print("=" * 80)

    materials_generator = VideoMaterialsGenerator(
        max_concurrent=max_concurrent,
        prompts_file=prompts_file,
    )

    # Prepare content contexts
    content_contexts = [
        f"Transition from slide {i+1} to slide {i+2}"
        for i in range(num_slides - 1)
    ]

    materials_result = materials_generator.generate_all_materials(
        slides_paths=slides_paths,
        output_dir=videos_dir,
        content_contexts=content_contexts,
        duration=video_duration,
        mode=video_quality,
        skip_preview=skip_preview,
    )

    if materials_result["failed_count"] > 0:
        print(f"\nWarning: {materials_result['failed_count']} video(s) failed")
        print("Continuing with composition, final video may be incomplete...")

    # Phase 4: Compose full video (if needed)
    if video_mode in ("both", "local"):
        print("\n" + "=" * 80)
        print("Phase 2: Compose Full PPT Video")
        print("=" * 80)

        composer = VideoComposer()

        # Build transitions dictionary
        transitions_dict = {
            key: result["video_path"]
            for key, result in materials_result["transitions"].items()
            if result["success"]
        }

        full_video_path = os.path.join(output_dir, "full_ppt_video.mp4")

        preview_video = None
        if materials_result["preview"] and not skip_preview:
            preview_video = materials_result["preview"]["video_path"]

        compose_success = composer.compose_full_ppt_video(
            slides_paths=slides_paths,
            transitions_dict=transitions_dict,
            output_path=full_video_path,
            slide_duration=slide_duration,
            include_preview=False,
            preview_video_path=preview_video,
        )

        if compose_success:
            print(f"Full video generated: {full_video_path}")
        else:
            print("Full video composition failed")

    # Phase 5: Generate web viewer (if needed)
    if video_mode in ("both", "web"):
        print("\n" + "=" * 80)
        print("Phase 3: Generate Web Viewer")
        print("=" * 80)

        generate_video_viewer(
            slides_paths=slides_paths,
            transitions_result=materials_result["transitions"],
            preview_result=materials_result.get("preview"),
            output_dir=output_dir,
        )

    # Phase 6: Print summary
    print("\n" + "=" * 80)
    print("PPT Video Generation Complete!")
    print("=" * 80)

    print(f"\nStatistics:")
    print(f"  Slides: {num_slides}")
    print(f"  Videos: {materials_result['success_count']} success, "
          f"{materials_result['failed_count']} failed")
    total_minutes = materials_result["total_duration"] / 60
    print(f"  Duration: {materials_result['total_duration']}s ({total_minutes:.1f}m)")

    print(f"\nOutput files:")
    if video_mode in ("both", "local"):
        print(f"  Full video: {output_dir}/full_ppt_video.mp4")
    if video_mode in ("both", "web"):
        print(f"  Web viewer: {output_dir}/video_index.html")
    print(f"  Video materials: {videos_dir}/")
    print(f"  Metadata: {videos_dir}/video_metadata.json")

    print("\n" + "=" * 80 + "\n")

    return {
        "output_dir": output_dir,
        "num_slides": num_slides,
        "materials_result": materials_result,
        "video_mode": video_mode,
    }


# =============================================================================
# Web Viewer Generation
# =============================================================================

def generate_video_viewer(
    slides_paths: List[str],
    transitions_result: Dict[str, Any],
    preview_result: Optional[Dict[str, Any]],
    output_dir: str,
) -> Optional[str]:
    """
    Generate HTML video viewer.

    Args:
        slides_paths: List of slide image paths.
        transitions_result: Transition video generation results.
        preview_result: Preview video generation result.
        output_dir: Output directory.

    Returns:
        Path to generated HTML file, or None if template not found.
    """
    print("Generating web viewer...")

    template_path = "templates/video_viewer.html"
    output_html = os.path.join(output_dir, "video_index.html")

    if not os.path.exists(template_path):
        print(f"Warning: Template not found: {template_path}, skipping web viewer")
        return None

    # Build slides data (relative paths)
    slides_data = [os.path.relpath(path, output_dir) for path in slides_paths]

    # Build transitions data
    transitions_data = {
        key: os.path.relpath(result["video_path"], output_dir)
        for key, result in transitions_result.items()
        if result["success"]
    }

    # Build preview data
    preview_data = None
    if preview_result:
        preview_data = os.path.relpath(preview_result["video_path"], output_dir)

    # Read template and replace placeholders
    with open(template_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    replacements = [
        ("/* SLIDES_DATA_PLACEHOLDER */", json.dumps(slides_data, ensure_ascii=False)),
        ("/* TRANSITIONS_DATA_PLACEHOLDER */", json.dumps(transitions_data, ensure_ascii=False)),
        ("/* PREVIEW_DATA_PLACEHOLDER */", json.dumps(preview_data, ensure_ascii=False) if preview_data else "null"),
    ]

    for placeholder, value in replacements:
        html_content = html_content.replace(placeholder, value)

    with open(output_html, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"Web viewer generated: {output_html}")
    return output_html


# =============================================================================
# Command Line Interface
# =============================================================================

def create_argument_parser() -> argparse.ArgumentParser:
    """Create and configure argument parser."""
    parser = argparse.ArgumentParser(
        description="PPT Video Generator - Create videos with transitions from PPT images",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic usage with prompts file
  python generate_ppt_video.py \\
    --slides-dir outputs/xxx/images \\
    --output-dir outputs/xxx_video \\
    --prompts-file outputs/xxx/transition_prompts.json

  # Full parameters
  python generate_ppt_video.py \\
    --slides-dir outputs/xxx/images \\
    --output-dir outputs/xxx_video \\
    --prompts-file outputs/xxx/transition_prompts.json \\
    --video-mode both \\
    --video-duration 5 \\
    --slide-duration 5 \\
    --video-quality pro \\
    --max-concurrent 3

Workflow:
  1. Generate PPT images: python generate_ppt.py ...
  2. Have Claude Code analyze images and generate prompts:
     Run in Claude Code: "Analyze images in outputs/xxx/images, generate transition prompts"
  3. Generate videos: python generate_ppt_video.py --prompts-file ...

Notes:
  - Ensure KLING_ACCESS_KEY and KLING_SECRET_KEY are configured in .env
  - Claude Code must analyze images to create transition_prompts.json
  - First-last frame videos require pro mode (high quality)
  - Kling API has concurrent limit of 3, generation takes time
""",
    )

    parser.add_argument(
        "--slides-dir",
        required=True,
        help="PPT images directory (containing slide-01.png, slide-02.png, etc.)",
    )
    parser.add_argument(
        "--output-dir",
        required=True,
        help="Output directory",
    )
    parser.add_argument(
        "--video-mode",
        choices=["both", "local", "web"],
        default=DEFAULT_VIDEO_MODE,
        help=f"Output mode: both/local/web (default: {DEFAULT_VIDEO_MODE})",
    )
    parser.add_argument(
        "--video-duration",
        choices=["5", "10"],
        default=DEFAULT_VIDEO_DURATION,
        help=f"Transition video duration in seconds (default: {DEFAULT_VIDEO_DURATION})",
    )
    parser.add_argument(
        "--slide-duration",
        type=int,
        default=DEFAULT_SLIDE_DURATION,
        help=f"Duration per slide in seconds (default: {DEFAULT_SLIDE_DURATION})",
    )
    parser.add_argument(
        "--video-quality",
        choices=["std", "pro"],
        default=DEFAULT_VIDEO_QUALITY,
        help=f"Video quality: std/pro (default: {DEFAULT_VIDEO_QUALITY})",
    )
    parser.add_argument(
        "--max-concurrent",
        type=int,
        default=DEFAULT_MAX_CONCURRENT,
        help=f"Maximum concurrent tasks (default: {DEFAULT_MAX_CONCURRENT})",
    )
    parser.add_argument(
        "--skip-preview",
        action="store_true",
        help="Skip preview video generation",
    )
    parser.add_argument(
        "--prompts-file",
        required=True,
        help="Path to transition prompts JSON file (generated by Claude Code)",
    )

    return parser


def validate_inputs(args: argparse.Namespace) -> bool:
    """
    Validate command line inputs.

    Args:
        args: Parsed command line arguments.

    Returns:
        True if all inputs are valid, False otherwise.
    """
    if not os.path.exists(args.slides_dir):
        print(f"Error: Slides directory not found: {args.slides_dir}")
        return False

    if not os.path.exists(args.prompts_file):
        print(f"Error: Prompts file not found: {args.prompts_file}")
        print(f"\nHow to generate prompts file:")
        print(f"  1. Run in Claude Code:")
        print(f"     'Analyze images in {args.slides_dir}, generate transition prompts,")
        print(f"      save to transition_prompts.json'")
        print(f"  2. Use --prompts-file to specify the generated file path")
        return False

    return True


def main() -> None:
    """Main entry point."""
    # Load environment variables
    load_dotenv()

    # Parse arguments
    parser = create_argument_parser()
    args = parser.parse_args()

    # Validate inputs
    if not validate_inputs(args):
        sys.exit(1)

    # Execute generation
    try:
        result = generate_ppt_video_from_images(
            slides_dir=args.slides_dir,
            output_dir=args.output_dir,
            video_mode=args.video_mode,
            video_duration=args.video_duration,
            slide_duration=args.slide_duration,
            video_quality=args.video_quality,
            max_concurrent=args.max_concurrent,
            skip_preview=args.skip_preview,
            prompts_file=args.prompts_file,
        )

        sys.exit(0 if result else 1)

    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user")
        sys.exit(130)
    except Exception as e:
        print(f"\nError: {e}")
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
```

## File: `install_as_skill.sh`
```bash
#!/bin/bash

##############################################################################
# PPT Generator Pro - Claude Code Skill 安装脚本
#
# 功能：
# 1. 自动创建 Skill 目录
# 2. 复制所有必要文件
# 3. 安装 Python 依赖
# 4. 引导配置 API 密钥
#
# 使用方法：
#   bash install_as_skill.sh
##############################################################################

set -e  # 遇到错误立即退出

# 颜色输出
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 打印函数
print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_header() {
    echo ""
    echo "========================================"
    echo "$1"
    echo "========================================"
    echo ""
}

# 检查命令是否存在
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# 主函数
main() {
    print_header "PPT Generator Pro - Claude Code Skill 安装"

    # 1. 确定 Skill 目录
    SKILL_DIR="$HOME/.claude/skills/ppt-generator"
    print_info "目标目录: $SKILL_DIR"

    # 2. 检查是否已存在
    if [ -d "$SKILL_DIR" ]; then
        print_warning "Skill 目录已存在: $SKILL_DIR"
        read -p "是否覆盖安装？(y/N) " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            print_info "安装已取消"
            exit 0
        fi
        print_info "删除旧版本..."
        rm -rf "$SKILL_DIR"
    fi

    # 3. 创建目录
    print_info "创建 Skill 目录..."
    mkdir -p "$SKILL_DIR"
    print_success "目录已创建"

    # 4. 复制文件
    print_info "复制项目文件..."

    # 获取当前脚本所在目录（即项目根目录）
    SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

    # 复制所有必要文件
    cp -r "$SCRIPT_DIR"/* "$SKILL_DIR/"

    # 排除不需要的文件
    if [ -d "$SKILL_DIR/.git" ]; then
        rm -rf "$SKILL_DIR/.git"
    fi
    if [ -d "$SKILL_DIR/venv" ]; then
        rm -rf "$SKILL_DIR/venv"
    fi
    if [ -d "$SKILL_DIR/outputs" ]; then
        rm -rf "$SKILL_DIR/outputs"
    fi
    if [ -f "$SKILL_DIR/.env" ]; then
        rm "$SKILL_DIR/.env"
    fi

    print_success "文件复制完成"

    # 5. 检查 Python
    print_info "检查 Python 环境..."
    if ! command_exists python3; then
        print_error "未找到 Python 3，请先安装 Python 3.8+"
        exit 1
    fi

    PYTHON_VERSION=$(python3 --version)
    print_success "Python 已安装: $PYTHON_VERSION"

    # 6. 检查 pip
    if ! command_exists pip3 && ! command_exists pip; then
        print_error "未找到 pip，请先安装 pip"
        exit 1
    fi
    print_success "pip 已安装"

    # 7. 安装 Python 依赖
    print_info "安装 Python 依赖..."
    cd "$SKILL_DIR"

    # 尝试使用 pip3，如果不存在则使用 pip
    if command_exists pip3; then
        pip3 install -q google-genai pillow python-dotenv
    else
        pip install -q google-genai pillow python-dotenv
    fi

    print_success "Python 依赖安装完成"

    # 8. 检查 FFmpeg（可选）
    print_info "检查 FFmpeg（视频功能需要）..."
    if command_exists ffmpeg; then
        FFMPEG_VERSION=$(ffmpeg -version | head -n 1)
        print_success "FFmpeg 已安装: $FFMPEG_VERSION"
    else
        print_warning "FFmpeg 未安装，视频功能将不可用"
        print_info "安装方法:"
        print_info "  macOS:  brew install ffmpeg"
        print_info "  Ubuntu: sudo apt-get install ffmpeg"
    fi

    # 9. 配置 API 密钥
    print_header "配置 API 密钥"

    print_info "PPT Generator Pro 需要以下 API 密钥："
    print_info "  1. GEMINI_API_KEY (必需) - Google AI API"
    print_info "  2. KLING_ACCESS_KEY (可选) - 可灵 AI Access Key"
    print_info "  3. KLING_SECRET_KEY (可选) - 可灵 AI Secret Key"
    echo ""

    # 检查是否有 .env.example
    if [ -f "$SKILL_DIR/.env.example" ]; then
        print_info "创建 .env 文件..."
        cp "$SKILL_DIR/.env.example" "$SKILL_DIR/.env"
        print_success ".env 文件已创建"
        echo ""
        print_warning "请编辑 .env 文件，填入你的 API 密钥："
        print_info "  nano $SKILL_DIR/.env"
        print_info "  或"
        print_info "  code $SKILL_DIR/.env"
    else
        print_warning "未找到 .env.example 文件"
        print_info "请手动创建 $SKILL_DIR/.env 文件"
    fi

    # 10. 完成
    print_header "安装完成！"

    print_success "PPT Generator Pro 已成功安装为 Claude Code Skill"
    echo ""
    print_info "安装位置: $SKILL_DIR"
    echo ""
    print_info "下一步："
    print_info "  1. 配置 API 密钥（编辑 .env 文件）"
    print_info "     nano $SKILL_DIR/.env"
    echo ""
    print_info "  2. 在 Claude Code 中使用："
    print_info "     /ppt-generator-pro"
    echo ""
    print_info "  3. 或直接告诉 Claude："
    print_info "     \"我想基于以下文档生成一个 5 页的 PPT\""
    echo ""
    print_info "详细文档："
    print_info "  - Skill 使用指南: $SKILL_DIR/SKILL.md"
    print_info "  - 项目文档: $SKILL_DIR/README.md"
    print_info "  - 架构说明: $SKILL_DIR/ARCHITECTURE.md"
    echo ""
    print_success "祝使用愉快！ 🎉"
    echo ""
}

# 错误处理
trap 'print_error "安装过程中发生错误"; exit 1' ERR

# 运行主函数
main
```

## File: `kling_api.py`
```python
#!/usr/bin/env python3
"""
Kling Video Generation API Client.

Provides a wrapper for the Kling AI video generation API, supporting
image-to-video generation with first-last frame control.
"""

import base64
import os
import time
from pathlib import Path
from typing import Any, Dict, List, Optional

import jwt
import requests


# =============================================================================
# Constants
# =============================================================================

API_BASE_URL = "https://api-beijing.klingai.com"
API_CREATE_TASK = "/v1/videos/image2video"
API_QUERY_TASK = "/v1/videos/image2video/{task_id}"

DEFAULT_MODEL = "kling-v2-6"
DEFAULT_DURATION = "5"
DEFAULT_MODE = "std"
DEFAULT_CFG_SCALE = 0.5
DEFAULT_TIMEOUT = 300
DEFAULT_POLL_INTERVAL = 5
DEFAULT_TOKEN_EXPIRE = 1800


# =============================================================================
# Exceptions
# =============================================================================

class KlingAPIError(Exception):
    """Base exception for Kling API errors."""
    pass


class KlingTaskError(KlingAPIError):
    """Exception for task-related errors."""
    pass


class KlingConfigError(KlingAPIError):
    """Exception for configuration errors."""
    pass


# =============================================================================
# Kling Video Generator
# =============================================================================

class KlingVideoGenerator:
    """Client for Kling video generation API."""

    def __init__(
        self,
        access_key: Optional[str] = None,
        secret_key: Optional[str] = None,
    ) -> None:
        """
        Initialize Kling API client.

        Args:
            access_key: API access key. If not provided, reads from KLING_ACCESS_KEY env var.
            secret_key: API secret key. If not provided, reads from KLING_SECRET_KEY env var.

        Raises:
            KlingConfigError: If API keys are not configured.
        """
        self.access_key = access_key or os.environ.get("KLING_ACCESS_KEY")
        self.secret_key = secret_key or os.environ.get("KLING_SECRET_KEY")

        if not self.access_key or not self.secret_key:
            raise KlingConfigError(
                "Kling API keys not configured.\n"
                "Please set in .env file:\n"
                "  KLING_ACCESS_KEY=your-access-key\n"
                "  KLING_SECRET_KEY=your-secret-key"
            )

        print("Kling API client initialized")
        print(f"  Access Key: {self.access_key[:8]}...{self.access_key[-4:]}")

    # -------------------------------------------------------------------------
    # Authentication
    # -------------------------------------------------------------------------

    def generate_jwt_token(self, expire_seconds: int = DEFAULT_TOKEN_EXPIRE) -> str:
        """
        Generate JWT token for API authentication.

        Args:
            expire_seconds: Token validity period in seconds.

        Returns:
            JWT token string.
        """
        current_time = int(time.time())

        headers = {"alg": "HS256", "typ": "JWT"}
        payload = {
            "iss": self.access_key,
            "exp": current_time + expire_seconds,
            "nbf": current_time - 5,
        }

        return jwt.encode(payload, self.secret_key, headers=headers)

    def _get_auth_headers(self) -> Dict[str, str]:
        """Get authentication headers for API requests."""
        return {
            "Authorization": f"Bearer {self.generate_jwt_token()}",
            "Content-Type": "application/json",
        }

    # -------------------------------------------------------------------------
    # Image Processing
    # -------------------------------------------------------------------------

    @staticmethod
    def _image_to_base64(image_path: str) -> str:
        """
        Convert image file to base64 string.

        Args:
            image_path: Path to image file.

        Returns:
            Base64-encoded string (without data: prefix).
        """
        with open(image_path, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")

    def _prepare_image(self, image: str) -> str:
        """
        Prepare image for API request.

        Args:
            image: Image path or base64 string.

        Returns:
            Base64-encoded image string.
        """
        if os.path.exists(image):
            print(f"  Converting image: {Path(image).name}")
            return self._image_to_base64(image)
        return image

    # -------------------------------------------------------------------------
    # Task Management
    # -------------------------------------------------------------------------

    def create_video_task(
        self,
        image_start: str,
        image_end: Optional[str] = None,
        prompt: str = "",
        model_name: str = DEFAULT_MODEL,
        duration: str = DEFAULT_DURATION,
        mode: str = DEFAULT_MODE,
        cfg_scale: float = DEFAULT_CFG_SCALE,
        negative_prompt: str = "",
        callback_url: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Create image-to-video generation task.

        Args:
            image_start: Start frame image path or base64 string.
            image_end: End frame image path or base64 string (optional).
            prompt: Positive prompt describing the transition.
            model_name: Model name (default: kling-v2-6).
            duration: Video duration in seconds (5 or 10).
            mode: Generation mode (std or pro).
            cfg_scale: Prompt adherence (0-1), only for V1.x models.
            negative_prompt: Negative prompt.
            callback_url: Callback URL for task completion.

        Returns:
            Task data dictionary with task_id and status.

        Raises:
            KlingAPIError: If task creation fails.
        """
        # Prepare images
        request_body = {
            "model_name": model_name,
            "image": self._prepare_image(image_start),
            "duration": duration,
            "mode": mode,
        }

        if image_end:
            request_body["image_tail"] = self._prepare_image(image_end)

        # Add optional parameters
        if prompt:
            request_body["prompt"] = prompt
        if negative_prompt:
            request_body["negative_prompt"] = negative_prompt
        if callback_url:
            request_body["callback_url"] = callback_url

        # cfg_scale only supported in V1.x models
        if not model_name.startswith("kling-v2"):
            request_body["cfg_scale"] = cfg_scale

        # Log task info
        video_type = "first-last frame" if image_end else "single frame animation"
        print(f"Creating video task...")
        print(f"  Model: {model_name}")
        print(f"  Mode: {mode}")
        print(f"  Duration: {duration}s")
        print(f"  Type: {video_type}")

        # Send request
        url = f"{API_BASE_URL}{API_CREATE_TASK}"
        response = requests.post(url, json=request_body, headers=self._get_auth_headers())

        self._check_response(response, "create task")

        result = response.json()
        task_data = result["data"]

        print(f"Task created successfully!")
        print(f"  Task ID: {task_data['task_id']}")
        print(f"  Status: {task_data['task_status']}")

        return task_data

    def query_task_status(self, task_id: str) -> Dict[str, Any]:
        """
        Query task status.

        Args:
            task_id: Task ID to query.

        Returns:
            Task data dictionary.

        Raises:
            KlingAPIError: If query fails.
        """
        url = f"{API_BASE_URL}{API_QUERY_TASK.format(task_id=task_id)}"
        response = requests.get(url, headers=self._get_auth_headers())

        self._check_response(response, "query task")
        return response.json()["data"]

    def wait_for_completion(
        self,
        task_id: str,
        timeout: int = DEFAULT_TIMEOUT,
        poll_interval: int = DEFAULT_POLL_INTERVAL,
    ) -> Dict[str, Any]:
        """
        Wait for task completion by polling.

        Args:
            task_id: Task ID to wait for.
            timeout: Maximum wait time in seconds.
            poll_interval: Polling interval in seconds.

        Returns:
            Completed task data.

        Raises:
            TimeoutError: If task doesn't complete within timeout.
            KlingTaskError: If task fails.
        """
        print(f"Waiting for task completion (ID: {task_id})...")
        start_time = time.time()

        while True:
            elapsed = int(time.time() - start_time)

            if elapsed > timeout:
                raise TimeoutError(f"Task timeout after {elapsed}s (ID: {task_id})")

            task_data = self.query_task_status(task_id)
            status = task_data["task_status"]

            if status == "succeed":
                print(f"Task completed! Duration: {elapsed}s")
                return task_data

            if status == "failed":
                error_msg = task_data.get("task_status_msg", "Unknown error")
                raise KlingTaskError(f"Task failed (ID: {task_id}): {error_msg}")

            if status in ("submitted", "processing"):
                print(f"  [{elapsed}s] Status: {status}, waiting...")
                time.sleep(poll_interval)
            else:
                raise KlingTaskError(f"Unknown task status: {status}")

    # -------------------------------------------------------------------------
    # Video Download
    # -------------------------------------------------------------------------

    def download_video(self, video_url: str, save_path: str) -> str:
        """
        Download generated video.

        Args:
            video_url: URL of the video to download.
            save_path: Path to save the video.

        Returns:
            Path to saved video file.

        Raises:
            KlingAPIError: If download fails.
        """
        print(f"Downloading video...")
        print(f"  URL: {video_url}")
        print(f"  Save to: {save_path}")

        # Create directory if needed
        Path(save_path).parent.mkdir(parents=True, exist_ok=True)

        # Download with streaming
        response = requests.get(video_url, stream=True)
        if response.status_code != 200:
            raise KlingAPIError(f"Download failed with status {response.status_code}")

        with open(save_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)

        file_size_mb = os.path.getsize(save_path) / (1024 * 1024)
        print(f"Download complete! Size: {file_size_mb:.2f} MB")

        return save_path

    # -------------------------------------------------------------------------
    # High-Level API
    # -------------------------------------------------------------------------

    def generate_and_download(
        self,
        image_start: str,
        image_end: Optional[str],
        prompt: str,
        output_path: str,
        **kwargs: Any,
    ) -> str:
        """
        Generate video and download in one call.

        Args:
            image_start: Start frame image path.
            image_end: End frame image path (optional).
            prompt: Generation prompt.
            output_path: Path to save the video.
            **kwargs: Additional arguments for create_video_task().

        Returns:
            Path to downloaded video.

        Raises:
            KlingAPIError: If any step fails.
        """
        # Create task
        task_data = self.create_video_task(
            image_start=image_start,
            image_end=image_end,
            prompt=prompt,
            **kwargs,
        )

        # Wait for completion
        result_data = self.wait_for_completion(task_data["task_id"])

        # Get video URL
        videos = result_data.get("task_result", {}).get("videos", [])
        if not videos:
            raise KlingAPIError("Task completed but no video returned")

        # Download video
        return self.download_video(videos[0]["url"], output_path)

    # -------------------------------------------------------------------------
    # Helpers
    # -------------------------------------------------------------------------

    def _check_response(self, response: requests.Response, action: str) -> None:
        """
        Check API response for errors.

        Args:
            response: HTTP response object.
            action: Description of the action for error messages.

        Raises:
            KlingAPIError: If response indicates an error.
        """
        if response.status_code != 200:
            raise KlingAPIError(
                f"Failed to {action}:\n"
                f"  Status: {response.status_code}\n"
                f"  Response: {response.text}"
            )

        result = response.json()
        if result.get("code") != 0:
            raise KlingAPIError(
                f"Failed to {action}:\n"
                f"  Error code: {result.get('code')}\n"
                f"  Message: {result.get('message')}"
            )


# =============================================================================
# Main (for testing)
# =============================================================================

if __name__ == "__main__":
    # Test JWT token generation
    generator = KlingVideoGenerator()
    token = generator.generate_jwt_token()
    print(f"\nGenerated JWT Token: {token[:50]}...")
```

## File: `prompt_file_reader.py`
```python
#!/usr/bin/env python3
"""
Prompt File Reader Module.

Reads transition prompts from JSON files generated by Claude Code.
"""

import json
from pathlib import Path
from typing import Optional


class PromptFileReader:
    """Reader for transition prompts from JSON file."""

    def __init__(self, prompts_file: str) -> None:
        """
        Initialize prompt file reader.

        Args:
            prompts_file: Path to prompts JSON file.

        Raises:
            FileNotFoundError: If prompts file not found.
            json.JSONDecodeError: If file is not valid JSON.
        """
        self.prompts_file = prompts_file

        with open(prompts_file, "r", encoding="utf-8") as f:
            self.data = json.load(f)

        transitions_count = len(self.data.get("transitions", []))
        has_preview = "preview" in self.data and self.data["preview"]

        print(f"Prompts file loaded: {prompts_file}")
        print(f"  Preview prompt: {'Yes' if has_preview else 'No'}")
        print(f"  Transition prompts: {transitions_count}")

    def generate_prompt(
        self,
        frame_start_path: str,
        frame_end_path: str,
        content_context: Optional[str] = None,
    ) -> str:
        """
        Get transition prompt for specified frames.

        Args:
            frame_start_path: Path to start frame image.
            frame_end_path: Path to end frame image.
            content_context: Ignored (for interface compatibility).

        Returns:
            Transition prompt text.

        Raises:
            ValueError: If no prompt found for the transition.
        """
        # Extract slide numbers from filenames
        start_num = int(Path(frame_start_path).stem.split("-")[-1])
        end_num = int(Path(frame_end_path).stem.split("-")[-1])

        print(f"\nReading transition prompt...")
        print(f"  Start: {Path(frame_start_path).name} (slide {start_num})")
        print(f"  End: {Path(frame_end_path).name} (slide {end_num})")

        # Find matching transition
        for transition in self.data.get("transitions", []):
            if transition["from_slide"] == start_num and transition["to_slide"] == end_num:
                prompt = transition["prompt"]
                print(f"  Found transition prompt!")
                print(f"\n{'=' * 60}")
                print(prompt)
                print(f"{'=' * 60}\n")
                return prompt

        raise ValueError(
            f"No transition prompt found: {start_num} -> {end_num}\n"
            "Please ensure the prompts file contains this transition."
        )

    def generate_preview_prompt(self, first_slide_path: str) -> str:
        """
        Get preview prompt for first slide.

        Args:
            first_slide_path: Path to first slide image.

        Returns:
            Preview prompt text.

        Raises:
            ValueError: If no preview prompt in file.
        """
        print(f"\nReading preview prompt...")
        print(f"  Slide: {Path(first_slide_path).name}")

        preview_data = self.data.get("preview")
        if not preview_data:
            raise ValueError("No preview prompt found in prompts file.")

        prompt = preview_data["prompt"]
        print("  Found preview prompt!")

        return prompt


if __name__ == "__main__":
    import os

    test_file = "outputs/20260112_012753/transition_prompts.json"

    if os.path.exists(test_file):
        reader = PromptFileReader(test_file)
        print(f"\nPrompts file loaded successfully.")
    else:
        print(f"Test file not found: {test_file}")
```

## File: `run.sh`
```bash
#!/bin/bash

# PPT生成器启动脚本
# 自动激活虚拟环境并设置API密钥

# 设置项目根目录
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# 激活虚拟环境
source "$SCRIPT_DIR/venv/bin/activate"

# API密钥配置（优先级顺序）
# 1. 系统环境变量（最高优先级）
# 2. .env 文件（备用方案）

if [ -z "$GEMINI_API_KEY" ]; then
    # 系统环境变量未设置，尝试从 .env 文件加载
    if [ -f "$SCRIPT_DIR/.env" ]; then
        echo "📌 从 .env 文件加载API密钥"
        export $(cat "$SCRIPT_DIR/.env" | grep -v '^#' | xargs)
    else
        echo "❌ 错误: API密钥未配置"
        echo ""
        echo "请选择以下任一方式配置API密钥："
        echo ""
        echo "方式1（推荐）: 系统环境变量"
        echo "  echo 'export GEMINI_API_KEY=\"your-key\"' >> ~/.zshrc"
        echo "  source ~/.zshrc"
        echo ""
        echo "方式2: .env 文件"
        echo "  cp .env.example .env"
        echo "  编辑 .env 文件并填入您的API密钥"
        echo ""
        exit 1
    fi
else
    echo "✅ 使用系统环境变量中的API密钥"
fi

# 最终检查
if [ -z "$GEMINI_API_KEY" ]; then
    echo "❌ 错误: GEMINI_API_KEY 仍未设置"
    exit 1
fi

# 运行Python脚本，传递所有参数
python "$SCRIPT_DIR/generate_ppt.py" "$@"
```

## File: `simple_transition_prompt_generator.py`
```python
#!/usr/bin/env python3
"""
Simple Transition Prompt Generator.

Provides generic transition prompts without requiring Claude API.
Useful for testing or when Claude API is not available.
"""

from pathlib import Path
from typing import Optional


# =============================================================================
# Default Prompts
# =============================================================================

DEFAULT_TRANSITION_PROMPT = """The camera starts from the initial page, with background aurora waves flowing slowly from left to right. Neon purple, electric blue, and coral orange gradients shift gently against the dark background. The 3D glass object in the center begins to deconstruct, splitting into multiple transparent glass fragments that elegantly rotate and float in the air, reflecting the surrounding neon lights.

During deconstruction, the main elements of the starting page gradually disappear through fade-out, while new elements of the target page slowly emerge from transparency. If there are frosted glass rounded rectangle cards, they slide in from the edge or expand from the center, with subtle blur effects and reflections on their surfaces.

On the right side or other areas, glass fragments reassemble and weave into new 3D glass structures or data visualization graphics. These new elements are progressively assembled, each part maintaining the glass-morphic texture. If there are data labels or text information, they appear through simple fade-in, with text content remaining absolutely clear and stable throughout, without any distortion, blur, or shaking.

The aurora waves continue flowing throughout the transition, colors smoothly transitioning from the starting page's main tones to the target page's color scheme. Deep blue, purple, and coral gradients remain soft and coherent, creating a smooth, premium, tech-forward visual atmosphere. At the end, all elements stabilize in their final state, text is clear and readable, and glass objects are fully rendered."""

DEFAULT_PREVIEW_PROMPT = """The PPT cover composition remains static, with background aurora waves flowing extremely slowly from left to right. Neon purple, electric blue, and coral orange gradients breathe with subtle changes, completing a gentle brightness cycle over 5 seconds.

The central 3D glass object maintains its main form, but its surface reflections flow slowly, with glass material highlights shimmering like water waves, creating a subtle breathing sensation. If there are frosted glass cards, their edge glow intensity fluctuates subtly between 0.8 and 1.0.

Deep in the background, a few small light points may slowly drift in the darkness, like cosmic stardust. The overall brightness varies extremely subtly between 95% and 105% of normal value. All text content remains absolutely clear and stable, without any movement, distortion, or blur, always clearly readable.

This is a seamlessly looping subtle animation, where the last frame and first frame connect perfectly. The flow of light effects and color changes form a natural loop, giving a sense of serenity, premium quality, and waiting for interaction."""


# =============================================================================
# Simple Transition Prompt Generator
# =============================================================================

class SimpleTransitionPromptGenerator:
    """Simple prompt generator using generic templates."""

    def __init__(self) -> None:
        """Initialize simple prompt generator."""
        print("Simple prompt generator initialized")

    def generate_prompt(
        self,
        frame_start_path: str,
        frame_end_path: str,
        content_context: Optional[str] = None,
    ) -> str:
        """
        Generate generic transition prompt.

        Args:
            frame_start_path: Path to start frame image.
            frame_end_path: Path to end frame image.
            content_context: Ignored (for interface compatibility).

        Returns:
            Generic transition prompt text.
        """
        print(f"\nGenerating transition prompt...")
        print(f"  Start: {Path(frame_start_path).name}")
        print(f"  End: {Path(frame_end_path).name}")

        print("  Using generic transition template")
        print(f"\n{'=' * 60}")
        print(DEFAULT_TRANSITION_PROMPT)
        print(f"{'=' * 60}\n")

        return DEFAULT_TRANSITION_PROMPT

    def generate_preview_prompt(self, first_slide_path: str) -> str:
        """
        Generate generic preview prompt.

        Args:
            first_slide_path: Path to first slide image.

        Returns:
            Generic preview prompt text.
        """
        print(f"\nGenerating preview prompt...")
        print(f"  Slide: {Path(first_slide_path).name}")

        print("  Using generic preview template")

        return DEFAULT_PREVIEW_PROMPT


if __name__ == "__main__":
    import os

    generator = SimpleTransitionPromptGenerator()

    test_start = "outputs/20260112_012753/images/slide-01.png"
    test_end = "outputs/20260112_012753/images/slide-02.png"

    if os.path.exists(test_start) and os.path.exists(test_end):
        prompt = generator.generate_prompt(test_start, test_end)
        print(f"\nGenerated prompt length: {len(prompt)} characters")

    if os.path.exists(test_start):
        preview_prompt = generator.generate_preview_prompt(test_start)
        print(f"\nGenerated preview prompt length: {len(preview_prompt)} characters")
```

## File: `transition_prompt_generator.py`
```python
#!/usr/bin/env python3
"""
Transition Prompt Generator Module.

Uses Claude AI to analyze slide images and generate transition descriptions
for video generation.
"""

import base64
import os
from pathlib import Path
from typing import Optional, Tuple

from anthropic import Anthropic


# =============================================================================
# Constants
# =============================================================================

DEFAULT_TEMPLATE_PATH = "prompts/transition_template.md"
DEFAULT_MODEL = "claude-sonnet-4-5-20250929"
DEFAULT_MAX_TOKENS = 2000
DEFAULT_TEMPERATURE = 0.7

# Media type mapping
MEDIA_TYPE_MAP = {
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".gif": "image/gif",
    ".webp": "image/webp",
}


# =============================================================================
# Exceptions
# =============================================================================

class PromptGeneratorError(Exception):
    """Exception for prompt generation errors."""
    pass


# =============================================================================
# Transition Prompt Generator
# =============================================================================

class TransitionPromptGenerator:
    """Generator for transition prompts using Claude AI."""

    def __init__(self, template_path: str = DEFAULT_TEMPLATE_PATH) -> None:
        """
        Initialize transition prompt generator.

        Args:
            template_path: Path to transition template markdown file.

        Raises:
            FileNotFoundError: If template file not found.
            PromptGeneratorError: If Claude API initialization fails.
        """
        self.template_path = template_path

        # Load template
        if not os.path.exists(template_path):
            raise FileNotFoundError(
                f"Transition template not found: {template_path}\n"
                "Please ensure the file exists."
            )

        with open(template_path, "r", encoding="utf-8") as f:
            self.template = f.read()

        print(f"Transition template loaded: {template_path}")

        # Initialize Claude client
        self.client = self._init_claude_client()
        print("Claude API client initialized")

    def _init_claude_client(self) -> Anthropic:
        """
        Initialize Claude API client.

        Returns:
            Configured Anthropic client.

        Raises:
            PromptGeneratorError: If initialization fails.
        """
        api_key = os.environ.get("ANTHROPIC_API_KEY")

        if api_key:
            return Anthropic(api_key=api_key)

        # Try default config (Claude Code environment)
        try:
            return Anthropic()
        except Exception as e:
            raise PromptGeneratorError(
                f"Claude API initialization failed.\n"
                f"Please set ANTHROPIC_API_KEY in .env file,\n"
                f"or run in Claude Code environment.\n"
                f"Error: {e}"
            )

    # -------------------------------------------------------------------------
    # Image Processing
    # -------------------------------------------------------------------------

    @staticmethod
    def _encode_image(image_path: str) -> Tuple[str, str]:
        """
        Encode image to base64 with media type.

        Args:
            image_path: Path to image file.

        Returns:
            Tuple of (base64_string, media_type).
        """
        with open(image_path, "rb") as f:
            image_data = f.read()

        base64_str = base64.standard_b64encode(image_data).decode("utf-8")

        ext = Path(image_path).suffix.lower()
        media_type = MEDIA_TYPE_MAP.get(ext, "image/jpeg")

        return base64_str, media_type

    # -------------------------------------------------------------------------
    # Prompt Generation
    # -------------------------------------------------------------------------

    def generate_prompt(
        self,
        frame_start_path: str,
        frame_end_path: str,
        content_context: Optional[str] = None,
    ) -> str:
        """
        Generate transition prompt by analyzing two frames.

        Args:
            frame_start_path: Path to start frame image.
            frame_end_path: Path to end frame image.
            content_context: Optional context about the content transition.

        Returns:
            Generated transition description.

        Raises:
            PromptGeneratorError: If API call fails.
        """
        print(f"\nAnalyzing transition scene...")
        print(f"  Start: {Path(frame_start_path).name}")
        print(f"  End: {Path(frame_end_path).name}")

        # Encode images
        start_b64, start_media = self._encode_image(frame_start_path)
        end_b64, end_media = self._encode_image(frame_end_path)

        # Build system message with text handling rules
        system_message = self.template + """

**Important - Text Handling Rules**:
1. Video models have issues with text (blur, distortion, garbled). Avoid text changes.
2. If there is text in the frame, explicitly state "text content remains clear and stable"
3. Prioritize transitions through background, decorations, lighting, and color changes
4. If text areas are involved, use fade in/out instead of transformation or movement
5. Avoid descriptions like "text gradually changes", "text moves", "text rotates"
6. Recommended: "text transitions via fade in/out", "text remains clear and stable"

Now, based on the provided [Start Frame] (Image A) and [End Frame] (Image B), generate your transition description.
"""

        if content_context:
            system_message += f"\n**Content Context**: {content_context}\n"

        system_message += "\nPlease generate the transition description."

        # Build multimodal message
        message_content = [
            {
                "type": "image",
                "source": {
                    "type": "base64",
                    "media_type": start_media,
                    "data": start_b64,
                },
            },
            {"type": "text", "text": "This is the [Start Frame] (Image A)"},
            {
                "type": "image",
                "source": {
                    "type": "base64",
                    "media_type": end_media,
                    "data": end_b64,
                },
            },
            {"type": "text", "text": "This is the [End Frame] (Image B)"},
            {"type": "text", "text": system_message},
        ]

        print("Calling Claude API for transition analysis...")

        try:
            response = self.client.messages.create(
                model=DEFAULT_MODEL,
                max_tokens=DEFAULT_MAX_TOKENS,
                temperature=DEFAULT_TEMPERATURE,
                messages=[{"role": "user", "content": message_content}],
            )

            transition_prompt = response.content[0].text.strip()

            print("Transition prompt generated!")
            print(f"\n{'=' * 60}")
            print(transition_prompt)
            print(f"{'=' * 60}\n")

            return transition_prompt

        except Exception as e:
            raise PromptGeneratorError(f"Claude API call failed: {e}")

    def generate_preview_prompt(self, first_slide_path: str) -> str:
        """
        Generate preview video prompt for first slide (looping animation).

        Args:
            first_slide_path: Path to first slide image.

        Returns:
            Generated preview animation description.

        Raises:
            PromptGeneratorError: If API call fails.
        """
        print(f"\nGenerating preview prompt...")
        print(f"  Slide: {Path(first_slide_path).name}")

        # Encode image
        image_b64, media_type = self._encode_image(first_slide_path)

        # Build message
        message_content = [
            {
                "type": "image",
                "source": {
                    "type": "base64",
                    "media_type": media_type,
                    "data": image_b64,
                },
            },
            {
                "type": "text",
                "text": """Please generate a subtle animation prompt for this PPT cover image, for a looping preview video.

Requirements:
1. First and last frames are the same image, video should loop seamlessly
2. Animation should be subtle and elegant, not exaggerated
3. Suggested animation types:
   - Light flow (aurora-like light slowly moving)
   - Glass surface breathing effect (subtle reflection changes)
   - Subtle background gradient color changes
   - Slow rotation of 3D objects (if present)
   - Particle effects (floating light dots)
4. **Important**: Text content must remain clear and stable, no changes, distortion or blur
5. Overall atmosphere should be serene, breathing, waiting to be clicked

Please describe this subtle animation in one paragraph (150-250 words).""",
            },
        ]

        print("Calling Claude API for preview prompt...")

        try:
            response = self.client.messages.create(
                model=DEFAULT_MODEL,
                max_tokens=1000,
                temperature=DEFAULT_TEMPERATURE,
                messages=[{"role": "user", "content": message_content}],
            )

            preview_prompt = response.content[0].text.strip()

            print("Preview prompt generated!")
            print(f"\n{'=' * 60}")
            print(preview_prompt)
            print(f"{'=' * 60}\n")

            return preview_prompt

        except Exception as e:
            raise PromptGeneratorError(f"Claude API call failed: {e}")


# =============================================================================
# Main (for testing)
# =============================================================================

if __name__ == "__main__":
    print("TransitionPromptGenerator Test")
    print("=" * 60)

    try:
        generator = TransitionPromptGenerator()
        print("\nGenerator initialized successfully.")
        print("To test, provide slide image paths.")
    except Exception as e:
        print(f"Initialization failed: {e}")
```

## File: `video_composer.py`
```python
#!/usr/bin/env python3
"""
FFmpeg Video Composer Module.

Responsible for converting static images to videos, concatenating video clips,
and composing complete PPT videos.
"""

import os
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Dict, List, Optional


# =============================================================================
# Constants
# =============================================================================

DEFAULT_RESOLUTION = "1920x1080"
DEFAULT_FPS = 24
DEFAULT_SLIDE_DURATION = 2
FFMPEG_TIMEOUT = 300  # 5 minutes


# =============================================================================
# Exceptions
# =============================================================================

class FFmpegError(Exception):
    """Exception for FFmpeg-related errors."""
    pass


# =============================================================================
# Video Composer
# =============================================================================

class VideoComposer:
    """FFmpeg-based video composer for PPT video generation."""

    def __init__(self, ffmpeg_path: str = "ffmpeg") -> None:
        """
        Initialize video composer.

        Args:
            ffmpeg_path: Path to FFmpeg executable.

        Raises:
            FFmpegError: If FFmpeg is not available.
        """
        self.ffmpeg_path = ffmpeg_path
        self._verify_ffmpeg()

    def _verify_ffmpeg(self) -> None:
        """Verify FFmpeg is available and working."""
        try:
            result = subprocess.run(
                [self.ffmpeg_path, "-version"],
                capture_output=True,
                text=True,
                timeout=5,
            )
            if result.returncode == 0:
                version = result.stdout.split("\n")[0]
                print(f"FFmpeg ready: {version}")
            else:
                raise FFmpegError("FFmpeg version check failed")
        except FileNotFoundError:
            raise FFmpegError(
                "FFmpeg not found.\n"
                "Please install FFmpeg: brew install ffmpeg"
            )
        except subprocess.TimeoutExpired:
            raise FFmpegError("FFmpeg version check timed out")

    # -------------------------------------------------------------------------
    # FFmpeg Execution
    # -------------------------------------------------------------------------

    def _run_ffmpeg(
        self,
        cmd: List[str],
        description: str = "",
    ) -> bool:
        """
        Execute FFmpeg command.

        Args:
            cmd: FFmpeg command as list of arguments.
            description: Operation description for logging.

        Returns:
            True if successful, False otherwise.
        """
        if description:
            print(f"  {description}...")

        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=FFMPEG_TIMEOUT,
            )

            if result.returncode != 0:
                print(f"  FFmpeg failed: {result.stderr[:200]}")
                return False

            if description:
                print(f"  {description} complete")
            return True

        except subprocess.TimeoutExpired:
            print("  FFmpeg timed out")
            return False
        except Exception as e:
            print(f"  FFmpeg error: {e}")
            return False

    # -------------------------------------------------------------------------
    # Static Video Creation
    # -------------------------------------------------------------------------

    def create_static_video(
        self,
        image_path: str,
        duration: int = DEFAULT_SLIDE_DURATION,
        output_path: Optional[str] = None,
        resolution: str = DEFAULT_RESOLUTION,
        fps: int = DEFAULT_FPS,
    ) -> Optional[str]:
        """
        Convert static image to video.

        Args:
            image_path: Path to source image.
            duration: Video duration in seconds.
            output_path: Output video path (auto-generated if not provided).
            resolution: Target resolution (WxH format).
            fps: Target frame rate.

        Returns:
            Path to output video, or None if failed.
        """
        if not os.path.exists(image_path):
            print(f"  Image not found: {image_path}")
            return None

        # Auto-generate output path
        if not output_path:
            stem = Path(image_path).stem
            output_path = str(Path(image_path).parent / f"{stem}_static.mp4")

        width, height = resolution.split("x")

        # Build FFmpeg command
        cmd = [
            self.ffmpeg_path,
            "-y",  # Overwrite output
            "-loop", "1",  # Loop input image
            "-i", image_path,
            "-c:v", "libx264",  # H.264 codec
            "-t", str(duration),
            "-pix_fmt", "yuv420p",
            "-vf", (
                f"scale={width}:{height}:force_original_aspect_ratio=decrease,"
                f"pad={width}:{height}:(ow-iw)/2:(oh-ih)/2,setsar=1"
            ),
            "-r", str(fps),
            output_path,
        ]

        description = f"Image to video ({Path(image_path).name}, {duration}s)"
        success = self._run_ffmpeg(cmd, description)

        return output_path if success else None

    # -------------------------------------------------------------------------
    # Video Concatenation
    # -------------------------------------------------------------------------

    def concat_videos(
        self,
        video_list: List[str],
        output_path: str,
        normalize_params: bool = True,
        target_resolution: str = DEFAULT_RESOLUTION,
        target_fps: int = DEFAULT_FPS,
    ) -> bool:
        """
        Concatenate multiple videos into one.

        Args:
            video_list: List of video paths in order.
            output_path: Output video path.
            normalize_params: Whether to normalize video parameters.
            target_resolution: Target resolution for normalization.
            target_fps: Target FPS for normalization.

        Returns:
            True if successful, False otherwise.
        """
        if not video_list:
            print("  Empty video list")
            return False

        # Verify all videos exist
        for video_path in video_list:
            if not os.path.exists(video_path):
                print(f"  Video not found: {video_path}")
                return False

        if normalize_params:
            return self._concat_with_filter(
                video_list, output_path, target_resolution, target_fps
            )
        else:
            return self._concat_with_demuxer(video_list, output_path)

    def _concat_with_demuxer(
        self,
        video_list: List[str],
        output_path: str,
    ) -> bool:
        """
        Concatenate videos using concat demuxer (fast, no re-encoding).

        Args:
            video_list: List of video paths.
            output_path: Output video path.

        Returns:
            True if successful, False otherwise.
        """
        # Create temporary file list
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".txt", delete=False
        ) as f:
            concat_file = f.name
            for video_path in video_list:
                f.write(f"file '{os.path.abspath(video_path)}'\n")

        try:
            cmd = [
                self.ffmpeg_path,
                "-y",
                "-f", "concat",
                "-safe", "0",
                "-i", concat_file,
                "-c", "copy",
                output_path,
            ]

            description = f"Concatenating {len(video_list)} videos (fast mode)"
            return self._run_ffmpeg(cmd, description)
        finally:
            if os.path.exists(concat_file):
                os.remove(concat_file)

    def _concat_with_filter(
        self,
        video_list: List[str],
        output_path: str,
        resolution: str,
        fps: int,
    ) -> bool:
        """
        Concatenate videos using filter_complex (re-encodes, normalizes parameters).

        Args:
            video_list: List of video paths.
            output_path: Output video path.
            resolution: Target resolution.
            fps: Target FPS.

        Returns:
            True if successful, False otherwise.
        """
        width, height = resolution.split("x")

        # Build input arguments
        inputs = []
        for video_path in video_list:
            inputs.extend(["-i", video_path])

        # Build filter for each input
        filter_parts = []
        for i in range(len(video_list)):
            filter_parts.append(
                f"[{i}:v]scale={width}:{height}:force_original_aspect_ratio=decrease,"
                f"pad={width}:{height}:(ow-iw)/2:(oh-ih)/2,setsar=1,"
                f"fps={fps}[v{i}]"
            )

        # Build concat filter
        concat_inputs = "".join(f"[v{i}]" for i in range(len(video_list)))
        filter_complex = (
            ";".join(filter_parts) + ";"
            f"{concat_inputs}concat=n={len(video_list)}:v=1:a=0[outv]"
        )

        cmd = [
            self.ffmpeg_path,
            "-y",
            *inputs,
            "-filter_complex", filter_complex,
            "-map", "[outv]",
            "-c:v", "libx264",
            "-preset", "medium",
            "-crf", "23",
            "-pix_fmt", "yuv420p",
            output_path,
        ]

        description = f"Concatenating {len(video_list)} videos (normalized)"
        return self._run_ffmpeg(cmd, description)

    # -------------------------------------------------------------------------
    # Full PPT Video Composition
    # -------------------------------------------------------------------------

    def compose_full_ppt_video(
        self,
        slides_paths: List[str],
        transitions_dict: Dict[str, str],
        output_path: str,
        slide_duration: int = DEFAULT_SLIDE_DURATION,
        include_preview: bool = False,
        preview_video_path: Optional[str] = None,
        resolution: str = DEFAULT_RESOLUTION,
        fps: int = DEFAULT_FPS,
    ) -> bool:
        """
        Compose complete PPT video from slides and transitions.

        Video structure:
        1. [Optional] Preview video
        2. Transition 1-2
        3. Slide 2 static (N seconds)
        4. Transition 2-3
        5. Slide 3 static (N seconds)
        ...

        Args:
            slides_paths: List of slide image paths.
            transitions_dict: Dict mapping 'from-to' keys to transition video paths.
            output_path: Output video path.
            slide_duration: Duration for each static slide.
            include_preview: Whether to include preview video.
            preview_video_path: Path to preview video.
            resolution: Target resolution.
            fps: Target FPS.

        Returns:
            True if successful, False otherwise.
        """
        print("\n" + "=" * 80)
        print("Composing Full PPT Video")
        print("=" * 80)

        num_slides = len(slides_paths)
        print(f"\nParameters:")
        print(f"  Slides: {num_slides}")
        print(f"  Duration per slide: {slide_duration}s")
        print(f"  Include preview: {'Yes' if include_preview else 'No'}")
        print(f"  Resolution: {resolution}")
        print(f"  FPS: {fps}\n")

        # Create temporary directory
        temp_dir = tempfile.mkdtemp(prefix="ppt_video_")
        print(f"Temp directory: {temp_dir}\n")

        try:
            # Generate static videos (skip first slide)
            print("Generating static video clips...")
            static_videos = {}

            for i in range(1, num_slides):
                slide_path = slides_paths[i]
                slide_num = Path(slide_path).stem.split("-")[-1]

                static_path = os.path.join(temp_dir, f"slide-{slide_num}-static.mp4")
                result = self.create_static_video(
                    image_path=slide_path,
                    duration=slide_duration,
                    output_path=static_path,
                    resolution=resolution,
                    fps=fps,
                )

                if not result:
                    print(f"  Failed to create static video for slide {slide_num}")
                    return False

                static_videos[slide_num] = static_path

            print(f"  Generated {len(static_videos)} static videos\n")

            # Build video sequence
            print("Building video sequence...")
            video_sequence = []

            # Optional preview
            if include_preview and preview_video_path and os.path.exists(preview_video_path):
                video_sequence.append(preview_video_path)
                print("  + Preview video")

            # Add transitions and static videos
            for i in range(num_slides - 1):
                from_num = Path(slides_paths[i]).stem.split("-")[-1]
                to_num = Path(slides_paths[i + 1]).stem.split("-")[-1]
                transition_key = f"{from_num}-{to_num}"

                # Add transition video
                if transition_key in transitions_dict:
                    transition_path = transitions_dict[transition_key]
                    if os.path.exists(transition_path):
                        video_sequence.append(transition_path)
                        print(f"  + Transition {transition_key}")
                    else:
                        print(f"  ! Transition missing: {transition_key}")
                else:
                    print(f"  ! Transition not defined: {transition_key}")

                # Add target slide static video
                if to_num in static_videos:
                    video_sequence.append(static_videos[to_num])
                    print(f"  + Static slide-{to_num} ({slide_duration}s)")

            print(f"\n  Total clips: {len(video_sequence)}\n")

            if not video_sequence:
                print("  No video clips to concatenate")
                return False

            # Concatenate all videos
            print("Concatenating videos...")
            success = self.concat_videos(
                video_list=video_sequence,
                output_path=output_path,
                normalize_params=True,
                target_resolution=resolution,
                target_fps=fps,
            )

            if success:
                file_size_mb = os.path.getsize(output_path) / (1024 * 1024)
                print("\n" + "=" * 80)
                print("Full PPT Video Complete!")
                print("=" * 80)
                print(f"  Output: {output_path}")
                print(f"  Size: {file_size_mb:.2f} MB")
                print(f"  Clips: {len(video_sequence)}")
                print("=" * 80 + "\n")
            else:
                print("\n  Video concatenation failed")

            return success

        finally:
            # Cleanup
            print("Cleaning up temp files...")
            if os.path.exists(temp_dir):
                shutil.rmtree(temp_dir)
                print(f"  Removed: {temp_dir}\n")


# =============================================================================
# Main (for testing)
# =============================================================================

if __name__ == "__main__":
    composer = VideoComposer()

    # Test: Image to video
    test_image = "outputs/20260109_121822/images/slide-02.png"
    if os.path.exists(test_image):
        print("\nTest: Image to static video")
        result = composer.create_static_video(
            image_path=test_image,
            duration=3,
            output_path="test_outputs/test_static.mp4",
        )
        if result:
            print(f"  Test passed: {result}")
        else:
            print("  Test failed")
    else:
        print(f"Skipping test: Image not found {test_image}")
```

## File: `video_materials.py`
```python
#!/usr/bin/env python3
"""
Video Materials Generator Module.

Responsible for generating preview videos and transition videos for PPT slides.
Supports concurrent generation with configurable limits.
"""

import json
import os
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any, Dict, List, Optional

from kling_api import KlingVideoGenerator
from prompt_file_reader import PromptFileReader


# =============================================================================
# Constants
# =============================================================================

DEFAULT_MAX_CONCURRENT = 3
DEFAULT_DURATION = "5"
DEFAULT_MODE = "pro"


# =============================================================================
# Video Materials Generator
# =============================================================================

class VideoMaterialsGenerator:
    """Generator for PPT video materials (preview and transition videos)."""

    def __init__(
        self,
        kling_client: Optional[KlingVideoGenerator] = None,
        prompt_generator: Optional[Any] = None,
        max_concurrent: int = DEFAULT_MAX_CONCURRENT,
        prompts_file: Optional[str] = None,
    ) -> None:
        """
        Initialize video materials generator.

        Args:
            kling_client: Kling API client instance (created if not provided).
            prompt_generator: Custom prompt generator (prompts_file takes priority).
            max_concurrent: Maximum concurrent video generation tasks.
            prompts_file: Path to prompts JSON file (required if no prompt_generator).

        Raises:
            ValueError: If neither prompts_file nor prompt_generator is provided.
        """
        self.kling_client = kling_client or KlingVideoGenerator()
        self.max_concurrent = max_concurrent

        # Initialize prompt generator
        if prompts_file:
            self.prompt_generator = PromptFileReader(prompts_file)
            print(f"Using prompts file: {prompts_file}")
        elif prompt_generator:
            self.prompt_generator = prompt_generator
            print("Using custom prompt generator")
        else:
            raise ValueError(
                "Missing transition prompts.\n\n"
                "To generate video transitions, you need a prompts file.\n"
                "Follow these steps:\n"
                "1. In Claude Code, run:\n"
                "   'Analyze images in outputs/xxx/images, generate transition prompts,\n"
                "    save to outputs/xxx/transition_prompts.json'\n"
                "2. Use --prompts-file to specify the generated file path\n\n"
                "Example:\n"
                "  python generate_ppt_video.py \\\n"
                "    --slides-dir outputs/xxx/images \\\n"
                "    --output-dir outputs/xxx_video \\\n"
                "    --prompts-file outputs/xxx/transition_prompts.json"
            )

        print(f"Video materials generator initialized")
        print(f"  Max concurrent: {max_concurrent}")

    # -------------------------------------------------------------------------
    # Preview Video Generation
    # -------------------------------------------------------------------------

    def generate_preview_video(
        self,
        first_slide_path: str,
        output_dir: str,
        duration: str = DEFAULT_DURATION,
        mode: str = DEFAULT_MODE,
    ) -> Dict[str, Any]:
        """
        Generate preview video for the first slide (same first and last frame).

        Args:
            first_slide_path: Path to first slide image.
            output_dir: Output directory.
            duration: Video duration (5 or 10 seconds).
            mode: Generation mode (std/pro).

        Returns:
            Result dict with video_path, prompt, and duration.

        Raises:
            Exception: If video generation fails.
        """
        print("\n" + "=" * 80)
        print("Generating Preview Video")
        print("=" * 80)

        preview_prompt = self.prompt_generator.generate_preview_prompt(first_slide_path)

        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, "preview.mp4")

        print(f"\nGenerating preview video...")
        start_time = time.time()

        try:
            self.kling_client.generate_and_download(
                image_start=first_slide_path,
                image_end=first_slide_path,  # Same as start for looping
                prompt=preview_prompt,
                output_path=output_path,
                model_name="kling-v2-6",
                duration=duration,
                mode=mode,
            )

            elapsed = int(time.time() - start_time)

            print(f"\nPreview video generated!")
            print(f"  Duration: {elapsed}s")
            print(f"  Path: {output_path}\n")

            return {
                "video_path": output_path,
                "prompt": preview_prompt,
                "duration": elapsed,
            }

        except Exception as e:
            print(f"\nPreview video generation failed: {e}\n")
            raise

    # -------------------------------------------------------------------------
    # Transition Video Generation
    # -------------------------------------------------------------------------

    def _generate_single_transition(
        self,
        slide_from: str,
        slide_to: str,
        output_path: str,
        content_context: Optional[str] = None,
        duration: str = DEFAULT_DURATION,
        mode: str = DEFAULT_MODE,
    ) -> Dict[str, Any]:
        """
        Generate a single transition video.

        Args:
            slide_from: Source slide path.
            slide_to: Target slide path.
            output_path: Output video path.
            content_context: Content context for prompt generation.
            duration: Video duration.
            mode: Generation mode.

        Returns:
            Result dict with success status and details.
        """
        from_num = Path(slide_from).stem.split("-")[-1]
        to_num = Path(slide_to).stem.split("-")[-1]
        transition_key = f"{from_num}-{to_num}"

        print(f"\nGenerating transition [{transition_key}]")
        print(f"  {Path(slide_from).name} -> {Path(slide_to).name}")

        try:
            transition_prompt = self.prompt_generator.generate_prompt(
                frame_start_path=slide_from,
                frame_end_path=slide_to,
                content_context=content_context,
            )

            start_time = time.time()

            self.kling_client.generate_and_download(
                image_start=slide_from,
                image_end=slide_to,
                prompt=transition_prompt,
                output_path=output_path,
                model_name="kling-v2-6",
                duration=duration,
                mode=mode,
            )

            elapsed = int(time.time() - start_time)

            return {
                "from_to": transition_key,
                "video_path": output_path,
                "prompt": transition_prompt,
                "duration": elapsed,
                "success": True,
            }

        except Exception as e:
            return {
                "from_to": transition_key,
                "video_path": output_path,
                "prompt": "",
                "duration": 0,
                "success": False,
                "error": str(e),
            }

    def generate_transition_videos(
        self,
        slides_paths: List[str],
        output_dir: str,
        content_contexts: Optional[List[str]] = None,
        duration: str = DEFAULT_DURATION,
        mode: str = DEFAULT_MODE,
    ) -> Dict[str, Dict[str, Any]]:
        """
        Generate all transition videos with concurrent execution.

        Args:
            slides_paths: List of slide image paths in order.
            output_dir: Output directory.
            content_contexts: Optional list of content contexts for each transition.
            duration: Video duration.
            mode: Generation mode.

        Returns:
            Dict mapping transition keys to result dicts.
        """
        print("\n" + "=" * 80)
        print("Generating Transition Videos")
        print("=" * 80)

        num_slides = len(slides_paths)
        num_transitions = num_slides - 1

        estimated_time_min = num_transitions * 100 / self.max_concurrent
        estimated_time_max = num_transitions * 120 / self.max_concurrent

        print(f"\nTask summary:")
        print(f"  Slides: {num_slides}")
        print(f"  Transitions: {num_transitions}")
        print(f"  Max concurrent: {self.max_concurrent}")
        print(f"  Estimated time: {estimated_time_min:.0f}-{estimated_time_max:.0f}s\n")

        os.makedirs(output_dir, exist_ok=True)

        # Prepare tasks
        tasks = []
        for i in range(num_transitions):
            from_num = Path(slides_paths[i]).stem.split("-")[-1]
            to_num = Path(slides_paths[i + 1]).stem.split("-")[-1]

            tasks.append({
                "slide_from": slides_paths[i],
                "slide_to": slides_paths[i + 1],
                "output_path": os.path.join(output_dir, f"transition_{from_num}_to_{to_num}.mp4"),
                "content_context": content_contexts[i] if content_contexts and i < len(content_contexts) else None,
            })

        # Execute with thread pool
        results: Dict[str, Dict[str, Any]] = {}
        completed_count = 0
        failed_count = 0

        print(f"Starting generation (concurrent: {self.max_concurrent})...\n")
        start_time = time.time()

        with ThreadPoolExecutor(max_workers=self.max_concurrent) as executor:
            future_to_task = {
                executor.submit(
                    self._generate_single_transition,
                    task["slide_from"],
                    task["slide_to"],
                    task["output_path"],
                    task["content_context"],
                    duration,
                    mode,
                ): task
                for task in tasks
            }

            for future in as_completed(future_to_task):
                result = future.result()
                transition_key = result["from_to"]
                results[transition_key] = result

                completed_count += 1

                if result["success"]:
                    print(f"  [{completed_count}/{num_transitions}] "
                          f"Transition {transition_key} complete ({result['duration']}s)")
                else:
                    failed_count += 1
                    print(f"  [{completed_count}/{num_transitions}] "
                          f"Transition {transition_key} failed: {result['error']}")

        total_elapsed = int(time.time() - start_time)

        # Summary
        print("\n" + "=" * 80)
        print("Transition Generation Complete")
        print("=" * 80)
        print(f"  Total time: {total_elapsed}s ({total_elapsed/60:.1f}m)")
        print(f"  Success: {num_transitions - failed_count}/{num_transitions}")
        print(f"  Failed: {failed_count}/{num_transitions}")

        if failed_count > 0:
            print(f"\n  Failed transitions:")
            for key, result in results.items():
                if not result["success"]:
                    print(f"    - {key}: {result['error']}")

        print("=" * 80 + "\n")

        return results

    # -------------------------------------------------------------------------
    # Metadata
    # -------------------------------------------------------------------------

    def save_metadata(self, output_dir: str, metadata: Dict[str, Any]) -> str:
        """
        Save generation metadata to JSON file.

        Args:
            output_dir: Output directory.
            metadata: Metadata dictionary.

        Returns:
            Path to saved metadata file.
        """
        metadata_path = os.path.join(output_dir, "video_metadata.json")

        with open(metadata_path, "w", encoding="utf-8") as f:
            json.dump(metadata, f, ensure_ascii=False, indent=2)

        print(f"Metadata saved: {metadata_path}")
        return metadata_path

    # -------------------------------------------------------------------------
    # High-Level API
    # -------------------------------------------------------------------------

    def generate_all_materials(
        self,
        slides_paths: List[str],
        output_dir: str,
        content_contexts: Optional[List[str]] = None,
        duration: str = DEFAULT_DURATION,
        mode: str = DEFAULT_MODE,
        skip_preview: bool = False,
    ) -> Dict[str, Any]:
        """
        Generate all video materials (preview + transitions) in one call.

        Args:
            slides_paths: List of slide image paths.
            output_dir: Output directory.
            content_contexts: Optional content contexts for transitions.
            duration: Video duration.
            mode: Generation mode.
            skip_preview: Whether to skip preview video generation.

        Returns:
            Complete results dict with preview, transitions, and statistics.
        """
        print("\n" + "=" * 80)
        print("Generating All Video Materials")
        print("=" * 80)

        total_start = time.time()

        all_results: Dict[str, Any] = {
            "preview": None,
            "transitions": {},
            "total_duration": 0,
            "success_count": 0,
            "failed_count": 0,
        }

        # Generate preview video
        if not skip_preview:
            try:
                preview_result = self.generate_preview_video(
                    first_slide_path=slides_paths[0],
                    output_dir=output_dir,
                    duration=duration,
                    mode=mode,
                )
                all_results["preview"] = preview_result
                all_results["success_count"] += 1
            except Exception as e:
                print(f"Warning: Preview generation failed, continuing: {e}")
                all_results["failed_count"] += 1
        else:
            print("Skipping preview video generation")

        # Generate transition videos
        transition_results = self.generate_transition_videos(
            slides_paths=slides_paths,
            output_dir=output_dir,
            content_contexts=content_contexts,
            duration=duration,
            mode=mode,
        )

        all_results["transitions"] = transition_results

        # Count successes/failures
        for result in transition_results.values():
            if result["success"]:
                all_results["success_count"] += 1
            else:
                all_results["failed_count"] += 1

        all_results["total_duration"] = int(time.time() - total_start)

        # Save metadata
        self.save_metadata(output_dir, all_results)

        # Final summary
        total_minutes = all_results["total_duration"] / 60
        print("\n" + "=" * 80)
        print("All Video Materials Generated!")
        print("=" * 80)
        print(f"  Total time: {all_results['total_duration']}s ({total_minutes:.1f}m)")
        print(f"  Success: {all_results['success_count']}")
        print(f"  Failed: {all_results['failed_count']}")
        print(f"  Output: {output_dir}")
        print("=" * 80 + "\n")

        return all_results


# =============================================================================
# Main (for testing)
# =============================================================================

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()

    print("VideoMaterialsGenerator requires a prompts file to run.")
    print("Use generate_ppt_video.py for complete workflow.")
```

## File: `prompts/transition_template.md`
```markdown
## 首尾帧视频生成提示词
适用模型：Kling、Veo、Seedance
使用方式：将首帧和尾帧图片以及提示词，发送给任意支持多模态的大语言模型

### 提示词
你是一位顶尖的创意视频导演和VFX（视觉特效）概念艺术家。你的任务是为AI视频生成模型设计一个从【起始帧】到【结束帧】的转场过程。

你的核心目标是：构思并用一段话清晰、具体地描述这个动态视觉变化。

在构思时，请遵循以下创作框架：

第一步：分析差异 快速判断【起始帧】和【结束帧】的差异程度。

A类 - 关联性强： 主体或场景基本一致，只是状态、风格或环境发生改变（例如，同一个人换了衣服，同一个场景从白天到黑夜）。

B类 - 差异巨大： 主体和场景完全不同（例如，一只猫在客厅 → 一艘飞船在太空）。

第二步：选择转场策略

如果属于 A类，优先采用**“原地演变”的策略。让变化直接发生在主体和环境上，尽量不使用或只使用微弱的摄像机移动。

如果属于 B类，采用“运镜驱动转场”**的策略。必须使用一种明确的摄像机移动（如推、拉、摇、移、旋转）来引导过渡，让镜头运动成为连接两个不相干画面的桥梁。

第三步：构思具体变化（从以下工具箱中选择组合）

主体变化： 主体如何改变？（形态变化、材质替换、服装更替、分解重组、消失或出现）。

环境变化： 背景如何改变？（时间流逝、季节更替、空间切换、从现实变为幻想）。

风格/特效变化： 用什么视觉风格或特效来包装这个过程？（例如，画面逐渐像素化后重组、被火焰/水流吞噬后显现、转变为水彩/油画风格、出现光效粒子）。

输出规则：

将你的最终构思整合为一个连贯的段落。

描述要具体、直接，充满画面感。专注于“我们看到了什么”，而不是“我们感觉到了什么”。

严格遵守你在第二步中选择的摄像机移动策略。

避免使用模糊的比喻和过于文学化的修辞。

现在，请根据我提供的【起始帧】（图片A）和【结束帧】（图片B），生成你的转场描述。
```

## File: `styles/gradient-glass.md`
```markdown
# 渐变拟物玻璃卡片风格

## 风格ID
gradient-glass

## 风格名称
渐变拟物玻璃卡片风格

## 适配模型
- Nano Banana Pro (gemini-3-pro-image-preview)
- Seedream

## 风格描述
一套非常漂亮的渐变拟物玻璃卡片风格 PPT，融合了Apple Keynote的极简主义、现代SaaS产品设计和玻璃拟态风格。整体氛围高端、沉浸、洁净且有呼吸感。

## 基础提示词模板

你是一位专家级UI UX演示设计师，请生成高保真、未来科技感的16比9演示文稿幻灯片。请根据视觉平衡美学，自动在封面、网格布局或数据可视化中选择一种最完美的构图。

全局视觉语言方面，风格要无缝融合Apple Keynote的极简主义、现代SaaS产品设计和玻璃拟态风格。整体氛围需要高端、沉浸、洁净且有呼吸感。光照采用电影级体积光、柔和的光线追踪反射和环境光遮蔽。配色方案选择深邃的虚空黑或纯净的陶瓷白作为基底，并以流动的极光渐变色即霓虹紫、电光蓝、柔和珊瑚橙、青色作为背景和UI高光点缀。

关于画面内容模块，请智能整合以下元素：

1. 排版引擎采用Bento便当盒网格系统，将内容组织在模块化的圆角矩形容器中。容器材质必须是带有模糊效果的磨砂玻璃，具有精致的白色边缘和柔和的投影,并强制保留巨大的内部留白，避免拥挤。

2. 插入礼物质感的3D物体，渲染独特的高端抽象3D制品作为视觉锚点。它们的外观应像实体的昂贵礼物或收藏品，材质为抛光金属、幻彩亚克力、透明玻璃或软硅胶，形状可是悬浮胶囊、球体、盾牌、莫比乌斯环或流体波浪。

3. 字体与数据方面，使用干净的无衬线字体，建立高对比度。如果有图表，请使用发光的3D甜甜圈图、胶囊状进度条或悬浮数字，图表应看起来像发光的霓虹灯玩具。

渲染质量要求：虚幻引擎5渲染，8k分辨率，超细节纹理，UI设计感，UX界面，Dribbble热门趋势，设计奖获奖作品。

## 页面类型模板

### 封面页模板
构图逻辑：在中心放置一个巨大的复杂3D玻璃物体，并覆盖粗体大字，背景有延伸的极光波浪。

使用场景：PPT的第一页，展示标题和主题。

### 内容页模板
构图逻辑：使用Bento网格布局，将3D图标放在小卡片中，文本放在大卡片中。容器材质必须是带有模糊效果的磨砂玻璃，具有精致的白色边缘和柔和的投影，并强制保留巨大的内部留白，避免拥挤。

使用场景：展示核心观点、要点、内容章节等。

### 数据页模板
构图逻辑：使用分屏设计，左侧排版文字，右侧悬浮巨大的发光3D数据可视化图表。图表应使用发光的3D甜甜圈图、胶囊状进度条或悬浮数字，看起来像发光的霓虹灯玩具。

使用场景：展示数据、统计信息、对比分析、总结等。

## 使用示例

### 生成封面页
```
{基础提示词模板}

请根据视觉平衡美学，生成封面页。在中心放置一个巨大的复杂3D玻璃物体，并覆盖粗体大字：

[标题文本]

背景有延伸的极光波浪。
```

### 生成内容页
```
{基础提示词模板}

请生成内容页。使用Bento网格布局，将以下内容组织在模块化的圆角矩形容器中，容器材质必须是带有模糊效果的磨砂玻璃：

[内容文本]
```

### 生成数据页
```
{基础提示词模板}

请生成数据页或总结页。使用分屏设计，左侧排版以下文字，右侧悬浮巨大的发光3D数据可视化图表：

[内容文本]
```

## 技术参数

### Nano Banana Pro配置
- 模型：gemini-3-pro-image-preview
- 比例：16:9
- 分辨率：2K (2752x1536) 或 4K (5504x3072)
- 响应模式：IMAGE

### 建议设置
- 推荐分辨率：2K（平衡质量和生成速度）
- 适用于：产品演示、技术分享、创意提案、数据报告等场景
```

## File: `styles/vector-illustration.md`
```markdown
# 矢量插画风格

## 风格ID
vector-illustration

## 风格名称
矢量插画风格PPT

## 适配模型
- Nano Banana Pro (gemini-3-pro-image-preview)
- Notebookml
- Youmind
- Listenhub
- Lovart

## 风格描述
扁平化矢量插画风格，具有清晰的黑色轮廓线和复古柔和的配色方案。强调几何化简化和玩具模型般的可爱感。

## 基础提示词模板

你是一位专家级插画设计师，请生成16比9的矢量插画风格演示文稿幻灯片。

**视觉风格与美术指导**

插画风格：扁平化矢量插画（Flat Vector Illustration）。必须包含清晰、统一粗细的黑色轮廓线（Monoline/Stroke）。色彩填涂需简洁，仅使用少量阴影，严禁使用渐变色或3D渲染效果。

构图形式：横向全景式构图（Panoramic），占据版面顶部 1/3 的空间。

线条风格（Line Work）：必须使用统一粗细的黑色单线描边（Monoline/Uniform Stroke）。所有物体（建筑、植物、云朵）都必须有封闭的黑色轮廓，类似填色书的线稿风格。线条末端圆润，避免尖锐的棱角。

几何化处理（Geometric Simplification）：将复杂的物体简化为基本几何形状。例如，树木简化为棒棒糖形状或三角形，建筑物简化为简单的矩形块面，窗户简化为整齐的小方格网格。不要追求写实细节，要追求"玩具模型"般的可爱感。

空间与透视：采用平视或稍微俯视的 2.5D 视角（类似等轴测，但更自由）。通过图层的前后遮挡来表现纵深，不要使用大气透视（即远景不要变模糊或变淡），所有图层清晰度一致。

装饰元素：在空白处添加装饰性的几何元素，如放射状的线条（代表阳光或能量）、药丸形状的云朵、或者是简单的小圆点和星星，以平衡画面的视觉密度。

**配色方案**

背景：米色/奶油色（Cream/Off-white）纸张纹理感底色。

强调色：珊瑚红、薄荷绿、芥末黄、赭石色（Burnt Orange）和岩石蓝。复古且柔和的色调。

**字体排版**

主标题：巨大的、加粗的复古衬线体（Retro Serif），体现权威感与优雅感。

副标题：位于矩形色块内的全大写无衬线体。

正文：清晰易读的几何感无衬线体。

## 页面类型模板

### 封面页模板
构图逻辑：主标题使用巨大的复古衬线体，占据画面中央。顶部1/3区域绘制横向全景式的矢量插画场景，包含简化的几何化建筑、玩具般的树木和装饰元素。背景使用米色/奶油色纸张纹理。

使用场景：PPT的第一页，展示标题和主题。

### 内容页模板
构图逻辑：顶部保留横向插画装饰带。内容区域使用几何化的图标和矢量小插画配合文字，所有元素都带有统一粗细的黑色轮廓线。使用彩色矩形块分隔不同的要点。

使用场景：展示核心观点、要点、内容章节等。

### 数据页模板
构图逻辑：使用几何化的图表和信息图形式，如简化的饼图、条形图等，所有图表元素都有清晰的黑色轮廓。配色使用复古柔和色调。添加装饰性几何元素平衡画面。

使用场景：展示数据、统计信息、对比分析、总结等。

## 使用示例

### 生成封面页
```
{基础提示词模板}

请生成封面页。在顶部1/3区域绘制横向全景式的矢量插画场景，包含以下元素的几何化简化表现：[根据主题选择场景元素]。

主标题使用巨大的复古衬线体，内容为：
[标题文本]

副标题使用矩形色块背景的全大写无衬线体：
[副标题文本]

背景使用米色/奶油色纸张纹理。
```

### 生成内容页
```
{基础提示词模板}

请生成内容页。顶部绘制横向插画装饰带。

内容区域展示以下要点，每个要点配合简洁的矢量图标，所有元素都有统一的黑色轮廓线：

[内容文本]

使用彩色矩形块（珊瑚红、薄荷绿、芥末黄）分隔不同要点。
```

### 生成数据页
```
{基础提示词模板}

请生成数据页。使用几何化的矢量图表形式展示以下数据，所有图表元素都有清晰的黑色轮廓：

[内容文本]

配色使用复古柔和色调，添加装饰性的几何元素（小圆点、星星、放射线）平衡画面。
```

## 技术参数

### Nano Banana Pro配置
- 模型：gemini-3-pro-image-preview
- 比例：16:9
- 分辨率：2K (2752x1536) 或 4K (5504x3072)
- 响应模式：IMAGE

### 建议设置
- 推荐分辨率：2K（平衡质量和生成速度）
- 适用于：教育演示、创意提案、儿童内容、品牌展示等场景
- 风格特点：温暖可爱、易于理解、复古怀旧

## 风格关键词

- 扁平化矢量插画
- 黑色轮廓线
- 几何化简化
- 复古配色
- 玩具模型感
- 横向全景构图
- 米色纸张纹理
- 装饰性几何元素
```

## File: `templates/video_viewer.html`
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PPT视频播放器</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            overflow: hidden;
            background: #000;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        }

        .container {
            width: 100vw;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            position: relative;
        }

        /* 静态图片显示 */
        .slide-image {
            width: 100%;
            height: 100%;
            object-fit: contain;
            display: none;
        }

        .slide-image.active {
            display: block;
        }

        /* 视频播放器 */
        .video-player {
            width: 100%;
            height: 100%;
            object-fit: contain;
            display: none;
        }

        .video-player.active {
            display: block;
        }

        /* 页码指示器 */
        .indicator {
            position: fixed;
            top: 20px;
            right: 20px;
            background: rgba(0, 0, 0, 0.7);
            padding: 10px 20px;
            border-radius: 20px;
            color: white;
            font-size: 14px;
            z-index: 100;
            backdrop-filter: blur(10px);
        }

        /* 控制提示 */
        .controls {
            position: fixed;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(0, 0, 0, 0.7);
            padding: 10px 20px;
            border-radius: 25px;
            color: white;
            font-size: 14px;
            z-index: 100;
            backdrop-filter: blur(10px);
            opacity: 1;
            transition: opacity 0.3s;
        }

        .controls.hidden {
            opacity: 0;
        }

        /* 加载指示器 */
        .loading {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: rgba(0, 0, 0, 0.8);
            padding: 20px 40px;
            border-radius: 10px;
            color: white;
            font-size: 16px;
            z-index: 200;
            display: none;
        }

        .loading.active {
            display: block;
        }

        /* 加载动画 */
        .loading::after {
            content: '';
            display: inline-block;
            width: 16px;
            height: 16px;
            margin-left: 10px;
            border: 2px solid #fff;
            border-radius: 50%;
            border-top-color: transparent;
            animation: spin 1s linear infinite;
        }

        @keyframes spin {
            to { transform: rotate(360deg); }
        }
    </style>
</head>
<body>
    <div class="container" id="container">
        <!-- 内容将通过JS动态插入 -->
    </div>

    <div class="indicator">
        <span id="current">1</span> / <span id="total">0</span>
    </div>

    <div class="controls" id="controls">
        ← → 切换页面 | Space 播放/暂停 | H 隐藏控制 | ESC 全屏
    </div>

    <div class="loading" id="loading">
        正在加载视频
    </div>

    <script>
        // 数据注入（由Python脚本替换）
        const slidesData = /* SLIDES_DATA_PLACEHOLDER */;
        const transitionsData = /* TRANSITIONS_DATA_PLACEHOLDER */;
        const previewData = /* PREVIEW_DATA_PLACEHOLDER */;

        class VideoPPTPlayer {
            constructor() {
                this.slides = slidesData;
                this.transitions = transitionsData;
                this.preview = previewData;
                this.currentSlide = 0;
                this.isTransitioning = false;
                this.isPreviewMode = true;

                this.container = document.getElementById('container');
                this.currentIndicator = document.getElementById('current');
                this.totalIndicator = document.getElementById('total');
                this.controlsEl = document.getElementById('controls');
                this.loadingEl = document.getElementById('loading');

                this.videoElement = null;
                this.imageElements = [];

                this.init();
            }

            init() {
                // 创建图片元素
                this.slides.forEach((slidePath, index) => {
                    const img = document.createElement('img');
                    img.src = slidePath;
                    img.className = 'slide-image';
                    img.alt = `幻灯片 ${index + 1}`;
                    this.container.appendChild(img);
                    this.imageElements.push(img);
                });

                // 创建视频元素
                this.videoElement = document.createElement('video');
                this.videoElement.className = 'video-player';
                this.videoElement.preload = 'auto';
                this.container.appendChild(this.videoElement);

                // 更新总页数
                this.totalIndicator.textContent = this.slides.length;

                // 绑定事件
                this.bindEvents();

                // 显示预览或第一页
                if (this.preview) {
                    this.playPreview();
                } else {
                    this.showSlide(0);
                }

                // 自动隐藏控制提示
                setTimeout(() => {
                    this.controlsEl.classList.add('hidden');
                }, 3000);
            }

            bindEvents() {
                // 键盘控制
                document.addEventListener('keydown', (e) => {
                    switch(e.key) {
                        case 'ArrowLeft':
                        case 'ArrowUp':
                            this.previousSlide();
                            break;
                        case 'ArrowRight':
                        case 'ArrowDown':
                            this.nextSlide();
                            break;
                        case ' ':
                            e.preventDefault();
                            this.togglePlayPause();
                            break;
                        case 'Home':
                            this.goToSlide(0);
                            break;
                        case 'End':
                            this.goToSlide(this.slides.length - 1);
                            break;
                        case 'Escape':
                            this.toggleFullscreen();
                            break;
                        case 'h':
                        case 'H':
                            this.toggleControls();
                            break;
                    }
                });

                // 视频播放结束事件
                this.videoElement.addEventListener('ended', () => {
                    this.onVideoEnded();
                });

                // 鼠标移动显示控制
                let hideControlsTimeout;
                document.addEventListener('mousemove', () => {
                    this.controlsEl.classList.remove('hidden');
                    clearTimeout(hideControlsTimeout);
                    hideControlsTimeout = setTimeout(() => {
                        this.controlsEl.classList.add('hidden');
                    }, 3000);
                });
            }

            playPreview() {
                if (!this.preview) return;

                console.log('播放预览视频');
                this.isPreviewMode = true;
                this.hideAllSlides();
                this.videoElement.src = this.preview;
                this.videoElement.loop = true;
                this.videoElement.classList.add('active');
                this.videoElement.play();
            }

            showSlide(index) {
                if (index < 0 || index >= this.slides.length) return;

                console.log(`显示第 ${index + 1} 页`);
                this.currentSlide = index;
                this.isPreviewMode = false;
                this.isTransitioning = false;

                // 隐藏所有元素
                this.hideAllSlides();

                // 显示当前页图片
                this.imageElements[index].classList.add('active');

                // 更新页码
                this.updateIndicator();
            }

            hideAllSlides() {
                // 隐藏所有图片
                this.imageElements.forEach(img => {
                    img.classList.remove('active');
                });

                // 隐藏视频
                this.videoElement.classList.remove('active');
                this.videoElement.pause();
                this.videoElement.loop = false;
            }

            playTransition(fromIndex, toIndex) {
                const fromNum = (fromIndex + 1).toString().padStart(2, '0');
                const toNum = (toIndex + 1).toString().padStart(2, '0');
                const transitionKey = `${fromNum}-${toNum}`;

                console.log(`播放过渡视频: ${transitionKey}`);

                if (!this.transitions[transitionKey]) {
                    console.warn(`过渡视频不存在: ${transitionKey}，直接显示目标页`);
                    this.showSlide(toIndex);
                    return;
                }

                this.isTransitioning = true;
                this.loadingEl.classList.add('active');

                // 隐藏所有元素
                this.hideAllSlides();

                // 播放过渡视频
                this.videoElement.src = this.transitions[transitionKey];
                this.videoElement.loop = false;
                this.videoElement.classList.add('active');

                // 等待视频加载
                this.videoElement.onloadeddata = () => {
                    this.loadingEl.classList.remove('active');
                    this.videoElement.play();
                };

                // 设置目标页
                this.currentSlide = toIndex;
                this.isPreviewMode = false; // 退出预览模式
            }

            onVideoEnded() {
                console.log('视频播放结束');

                if (this.isPreviewMode) {
                    // 预览视频循环播放（已设置loop）
                    return;
                }

                if (this.isTransitioning) {
                    // 过渡视频结束，显示目标页
                    this.showSlide(this.currentSlide);
                }
            }

            nextSlide() {
                if (this.isTransitioning) {
                    console.log('正在过渡中，请等待');
                    return;
                }

                const nextIndex = this.currentSlide + 1;
                if (nextIndex >= this.slides.length) {
                    console.log('已经是最后一页');
                    return;
                }

                if (this.isPreviewMode) {
                    // 从预览进入第二页
                    this.playTransition(0, 1);
                } else {
                    // 正常翻页
                    this.playTransition(this.currentSlide, nextIndex);
                }
            }

            previousSlide() {
                if (this.isTransitioning) {
                    console.log('正在过渡中，请等待');
                    return;
                }

                const prevIndex = this.currentSlide - 1;

                if (this.isPreviewMode) {
                    console.log('已经在首页预览');
                    return;
                }

                if (prevIndex < 0) {
                    // 返回首页预览
                    if (this.preview) {
                        this.playPreview();
                    } else {
                        console.log('已经是第一页');
                    }
                    return;
                }

                // 反向过渡（如果有）
                // 注意：目前过渡视频是单向的，反向翻页直接显示
                this.showSlide(prevIndex);
            }

            goToSlide(index) {
                if (this.isTransitioning) return;
                if (index === this.currentSlide && !this.isPreviewMode) return;

                if (index === 0 && this.preview) {
                    this.playPreview();
                } else {
                    this.showSlide(index);
                }
            }

            togglePlayPause() {
                if (this.videoElement.classList.contains('active')) {
                    if (this.videoElement.paused) {
                        this.videoElement.play();
                    } else {
                        this.videoElement.pause();
                    }
                }
            }

            toggleFullscreen() {
                if (!document.fullscreenElement) {
                    document.documentElement.requestFullscreen();
                } else {
                    document.exitFullscreen();
                }
            }

            toggleControls() {
                this.controlsEl.classList.toggle('hidden');
            }

            updateIndicator() {
                this.currentIndicator.textContent = this.currentSlide + 1;
            }
        }

        // 初始化播放器
        window.addEventListener('DOMContentLoaded', () => {
            new VideoPPTPlayer();
        });
    </script>
</body>
</html>
```

## File: `templates/viewer.html`
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PPT播放器</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            overflow: hidden;
            background: #000;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
        }

        .container {
            width: 100vw;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            position: relative;
        }

        .slide {
            width: 100%;
            height: 100%;
            object-fit: contain;
            display: none;
        }

        .slide.active {
            display: block;
        }

        .controls {
            position: fixed;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(0, 0, 0, 0.7);
            backdrop-filter: blur(10px);
            padding: 12px 24px;
            border-radius: 25px;
            color: white;
            font-size: 14px;
            z-index: 100;
            transition: opacity 0.3s ease;
        }

        .controls.hidden {
            opacity: 0;
        }

        .indicator {
            position: fixed;
            top: 20px;
            right: 20px;
            background: rgba(0, 0, 0, 0.7);
            backdrop-filter: blur(10px);
            padding: 12px 24px;
            border-radius: 20px;
            color: white;
            font-size: 14px;
            z-index: 100;
            transition: opacity 0.3s ease;
        }

        .indicator.hidden {
            opacity: 0;
        }

        .loading {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            color: white;
            font-size: 18px;
            z-index: 200;
        }
    </style>
</head>
<body>
    <div class="container" id="slideContainer">
        <!-- 图片将通过JS动态插入 -->
    </div>

    <div class="indicator" id="indicator">
        <span id="current">1</span> / <span id="total">0</span>
    </div>

    <div class="controls" id="controls">
        ← → 切换页面 | ↑ 首页 | ↓ 末页 | ESC 全屏 | 空格 暂停/继续 | H 隐藏控件
    </div>

    <div class="loading" id="loading">加载中...</div>

    <script>
        // 图片列表将通过替换占位符注入
        const slides = [/* IMAGE_LIST_PLACEHOLDER */];
        let currentSlide = 0;
        let autoPlayInterval = null;
        let isAutoPlaying = false;
        let controlsVisible = true;

        function init() {
            const container = document.getElementById('slideContainer');
            const loading = document.getElementById('loading');

            if (slides.length === 0) {
                loading.textContent = '未找到幻灯片图片';
                return;
            }

            slides.forEach((src, index) => {
                const img = document.createElement('img');
                img.src = src;
                img.className = 'slide' + (index === 0 ? ' active' : '');
                img.alt = `幻灯片 ${index + 1}`;
                img.onerror = function() {
                    console.error(`Failed to load image: ${src}`);
                };
                container.appendChild(img);
            });

            document.getElementById('total').textContent = slides.length;
            updateIndicator();

            // 隐藏加载提示
            loading.style.display = 'none';

            // 3秒后自动隐藏控件
            setTimeout(() => {
                hideControls();
            }, 3000);
        }

        function showSlide(index) {
            const allSlides = document.querySelectorAll('.slide');

            if (index < 0 || index >= slides.length) {
                return;
            }

            allSlides.forEach(s => s.classList.remove('active'));
            allSlides[index].classList.add('active');
            currentSlide = index;
            updateIndicator();

            // 显示控件
            showControls();

            // 3秒后再次隐藏
            setTimeout(() => {
                hideControls();
            }, 3000);
        }

        function updateIndicator() {
            document.getElementById('current').textContent = currentSlide + 1;
        }

        function nextSlide() {
            if (currentSlide < slides.length - 1) {
                showSlide(currentSlide + 1);
            } else if (isAutoPlaying) {
                // 自动播放模式下循环
                showSlide(0);
            }
        }

        function prevSlide() {
            if (currentSlide > 0) {
                showSlide(currentSlide - 1);
            } else if (isAutoPlaying) {
                // 自动播放模式下循环
                showSlide(slides.length - 1);
            }
        }

        function toggleFullscreen() {
            if (document.fullscreenElement) {
                document.exitFullscreen();
            } else {
                document.documentElement.requestFullscreen();
            }
        }

        function toggleAutoPlay() {
            if (isAutoPlaying) {
                stopAutoPlay();
            } else {
                startAutoPlay();
            }
        }

        function startAutoPlay() {
            if (autoPlayInterval) {
                clearInterval(autoPlayInterval);
            }
            autoPlayInterval = setInterval(() => {
                nextSlide();
            }, 3000); // 每3秒切换一次
            isAutoPlaying = true;
            updateControlsText();
        }

        function stopAutoPlay() {
            if (autoPlayInterval) {
                clearInterval(autoPlayInterval);
                autoPlayInterval = null;
            }
            isAutoPlaying = false;
            updateControlsText();
        }

        function updateControlsText() {
            const controls = document.getElementById('controls');
            const playText = isAutoPlaying ? '暂停' : '继续';
            controls.textContent = `← → 切换页面 | ↑ 首页 | ↓ 末页 | ESC 全屏 | 空格 ${playText} | H 隐藏控件`;
        }

        function hideControls() {
            if (controlsVisible) {
                document.getElementById('indicator').classList.add('hidden');
                document.getElementById('controls').classList.add('hidden');
                controlsVisible = false;
            }
        }

        function showControls() {
            if (!controlsVisible) {
                document.getElementById('indicator').classList.remove('hidden');
                document.getElementById('controls').classList.remove('hidden');
                controlsVisible = true;
            }
        }

        function toggleControls() {
            if (controlsVisible) {
                hideControls();
            } else {
                showControls();
            }
        }

        // 键盘事件监听
        document.addEventListener('keydown', (e) => {
            switch(e.key) {
                case 'ArrowLeft':
                    prevSlide();
                    stopAutoPlay(); // 手动操作时停止自动播放
                    break;
                case 'ArrowRight':
                    nextSlide();
                    stopAutoPlay();
                    break;
                case 'ArrowUp':
                case 'Home':
                    showSlide(0);
                    stopAutoPlay();
                    break;
                case 'ArrowDown':
                case 'End':
                    showSlide(slides.length - 1);
                    stopAutoPlay();
                    break;
                case 'Escape':
                    toggleFullscreen();
                    break;
                case ' ': // 空格键
                    e.preventDefault(); // 防止页面滚动
                    toggleAutoPlay();
                    break;
                case 'h':
                case 'H':
                    toggleControls();
                    break;
            }
        });

        // 鼠标移动时显示控件
        let mouseTimer = null;
        document.addEventListener('mousemove', () => {
            showControls();

            // 清除之前的定时器
            if (mouseTimer) {
                clearTimeout(mouseTimer);
            }

            // 3秒后隐藏控件
            mouseTimer = setTimeout(() => {
                hideControls();
            }, 3000);
        });

        // 触摸滑动支持（移动设备）
        let touchStartX = 0;
        let touchEndX = 0;

        document.addEventListener('touchstart', (e) => {
            touchStartX = e.changedTouches[0].screenX;
        });

        document.addEventListener('touchend', (e) => {
            touchEndX = e.changedTouches[0].screenX;
            handleSwipe();
        });

        function handleSwipe() {
            const swipeThreshold = 50; // 最小滑动距离

            if (touchEndX < touchStartX - swipeThreshold) {
                // 向左滑动，显示下一页
                nextSlide();
                stopAutoPlay();
            }

            if (touchEndX > touchStartX + swipeThreshold) {
                // 向右滑动，显示上一页
                prevSlide();
                stopAutoPlay();
            }
        }

        // 初始化
        init();
    </script>
</body>
</html>
```

