---
id: hello-agents
type: knowledge
owner: OA_Triage
---
# hello-agents
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<div align="right">
  <a href="./README_EN.md">English</a> | 中文
</div>

<div align='center'>
  <img src="./docs/images/hello-agents.png" alt="alt text" width="100%">
  <h1>Hello-Agents</h1>
  <h3>🤖 《从零开始构建智能体》</h3>
  <div align="center">
  <a href="https://trendshift.io/repositories/15520" target="_blank">
    <img src="https://trendshift.io/api/badge/repositories/15520" alt="datawhalechina%2Fhello-agents | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/>
  </a>
  </div>
  <p><em>从基础理论到实际应用，全面掌握智能体系统的设计与实现</em></p>
  <img src="https://img.shields.io/github/stars/datawhalechina/Hello-Agents?style=flat&logo=github" alt="GitHub stars"/>
  <img src="https://img.shields.io/github/forks/datawhalechina/Hello-Agents?style=flat&logo=github" alt="GitHub forks"/>
  <img src="https://img.shields.io/badge/language-Chinese-brightgreen?style=flat" alt="Language"/>
  <a href="https://github.com/datawhalechina/Hello-Agents"><img src="https://img.shields.io/badge/GitHub-Project-blue?style=flat&logo=github" alt="GitHub Project"></a>
  <a href="https://datawhalechina.github.io/hello-agents/"><img src="https://img.shields.io/badge/在线阅读-Online%20Reading-green?style=flat&logo=gitbook" alt="Online Reading"></a>
</div>

---

## 🎯 项目介绍

&emsp;&emsp;如果说 2024 年是"百模大战"的元年，那么 2025 年无疑开启了"Agent 元年"。技术的焦点正从训练更大的基础模型，转向构建更聪明的智能体应用。然而，当前系统性、重实践的教程却极度匮乏。为此，我们发起了 Hello-Agents 项目，希望能为社区提供一本从零开始、理论与实战并重的智能体系统构建指南。

&emsp;&emsp;Hello-Agents 是 Datawhale 社区的<strong>系统性智能体学习教程</strong>。如今 Agent 构建主要分为两派，一派是 Dify，Coze，n8n 这类软件工程类 Agent，其本质是流程驱动的软件开发，LLM 作为数据处理的后端；另一派则是 AI 原生的 Agent，即真正以 AI 驱动的 Agent。本教程旨在带领大家深入理解并构建后者——真正的 AI Native Agent。教程将带领你穿透框架表象，从智能体的核心原理出发，深入其核心架构，理解其经典范式，并最终亲手构建起属于自己的多智能体应用。我们相信，最好的学习方式就是动手实践。希望这本教程能成为你探索智能体世界的起点，能够从一名大语言模型的"使用者"，蜕变为一名智能体系统的"构建者"。

## 📚 快速开始

### 在线阅读
**[🌐 国外访问](https://datawhalechina.github.io/hello-agents/)** | **[🚀 国内加速](https://hello-agents.datawhale.cc)** - 无需下载，随时随地学习

### 本地阅读
如果您希望在本地阅读或贡献内容，请参考下方的学习指南。

### ✨ 你将收获什么？

- 📖 <strong>Datawhale 开源免费</strong> 完全免费学习本项目所有内容，与社区共同成长
- 🔍 <strong>理解核心原理</strong> 深入理解智能体的概念、历史与经典范式
- 🏗️ <strong>亲手实现</strong> 掌握热门低代码平台和智能体代码框架的使用
- 🛠️ <strong>自研框架[HelloAgents](https://github.com/jjyaoao/helloagents)</strong> 基于 Openai 原生 API 从零构建一个自己的智能体框架
- ⚙️ <strong>掌握高级技能</strong> 一步步实现上下文工程、Memory、协议、评估等系统性技术
- 🤝 <strong>模型训练</strong> 掌握 Agentic RL，从 SFT 到 GRPO 的全流程实战训练 LLM
- 🚀 <strong>驱动真实案例</strong> 实战开发智能旅行助手、赛博小镇等综合项目
- 📖 <strong>求职面试</strong> 学习智能体求职相关面试问题

## 📖 内容导航

| 章节                                                                                        | 关键内容                                      | 状态 |
| ------------------------------------------------------------------------------------------- | --------------------------------------------- | ---- |
| [前言](./docs/前言.md)                                                                      | 项目的缘起、背景及读者建议                    | ✅    |
| <strong>第一部分：智能体与语言模型基础</strong>                                             |                                               |      |
| [第一章 初识智能体](./docs/chapter1/第一章%20初识智能体.md)                                 | 智能体定义、类型、范式与应用                  | ✅    |
| [第二章 智能体发展史](./docs/chapter2/第二章%20智能体发展史.md)                             | 从符号主义到 LLM 驱动的智能体演进             | ✅    |
| [第三章 大语言模型基础](./docs/chapter3/第三章%20大语言模型基础.md)                         | Transformer、提示、主流 LLM 及其局限          | ✅    |
| <strong>第二部分：构建你的大语言模型智能体</strong>                                         |                                               |      |
| [第四章 智能体经典范式构建](./docs/chapter4/第四章%20智能体经典范式构建.md)                 | 手把手实现 ReAct、Plan-and-Solve、Reflection  | ✅    |
| [第五章 基于低代码平台的智能体搭建](./docs/chapter5/第五章%20基于低代码平台的智能体搭建.md) | 了解 Coze、Dify、n8n 等低代码智能体平台使用   | ✅    |
| [第六章 框架开发实践](./docs/chapter6/第六章%20框架开发实践.md)                             | AutoGen、AgentScope、LangGraph 等主流框架应用 | ✅    |
| [第七章 构建你的Agent框架](./docs/chapter7/第七章%20构建你的Agent框架.md)                   | 从 0 开始构建智能体框架                       | ✅    |
| <strong>第三部分：高级知识扩展</strong>                                                     |                                               |      |
| [第八章 记忆与检索](./docs/chapter8/第八章%20记忆与检索.md)                                 | 记忆系统，RAG，存储                           | ✅    |
| [第九章 上下文工程](./docs/chapter9/第九章%20上下文工程.md)                                 | 持续交互的"情境理解"                          | ✅    |
| [第十章 智能体通信协议](./docs/chapter10/第十章%20智能体通信协议.md)                        | MCP、A2A、ANP 等协议解析                      | ✅    |
| [第十一章 Agentic-RL](./docs/chapter11/第十一章%20Agentic-RL.md)                            | 从 SFT 到 GRPO 的 LLM 训练实战                | ✅    |
| [第十二章 智能体性能评估](./docs/chapter12/第十二章%20智能体性能评估.md)                    | 核心指标、基准测试与评估框架                  | ✅    |
| <strong>第四部分：综合案例进阶</strong>                                                     |                                               |      |
| [第十三章 智能旅行助手](./docs/chapter13/第十三章%20智能旅行助手.md)                        | MCP 与多智能体协作的真实世界应用              | ✅    |
| [第十四章 自动化深度研究智能体](./docs/chapter14/第十四章%20自动化深度研究智能体.md)        | DeepResearch Agent 复现与解析                 | ✅    |
| [第十五章 构建赛博小镇](./docs/chapter15/第十五章%20构建赛博小镇.md)                        | Agent 与游戏的结合，模拟社会动态              | ✅    |
| <strong>第五部分：毕业设计及未来展望</strong>                                               |                                               |      |
| [第十六章 毕业设计](./docs/chapter16/第十六章%20毕业设计.md)                                | 构建属于你的完整多智能体应用                  | ✅    |

### 社区贡献精选 (Community Blog)

&emsp;&emsp;欢迎大家将在学习 Hello-Agents 或 Agent 相关技术中的独到见解、实践总结，以 PR 的形式贡献到社区精选。如果是独立于正文的内容，也可以投稿至 Extra-Chapter！<strong>期待你的第一次贡献！</strong>

| 社区精选                                                                                                                                      | 内容总结                  |
| --------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- |
| [00-共创毕业设计](https://github.com/datawhalechina/hello-agents/blob/main/Co-creation-projects)                                             | 社区共创毕业设计项目      |
| [01-Agent面试题总结](https://github.com/datawhalechina/hello-agents/blob/main/Extra-Chapter/Extra01-面试问题总结.md)                          | Agent 岗位相关面试问题    |
| [01-Agent面试题答案](https://github.com/datawhalechina/hello-agents/blob/main/Extra-Chapter/Extra01-参考答案.md)                              | 相关面试问题答案          |
| [02-上下文工程内容补充](https://github.com/datawhalechina/hello-agents/blob/main/Extra-Chapter/Extra02-上下文工程补充知识.md)                 | 上下文工程内容扩展        |
| [03-Dify智能体创建保姆级教程](https://github.com/datawhalechina/hello-agents/blob/main/Extra-Chapter/Extra03-Dify智能体创建保姆级操作流程.md) | Dify智能体创建保姆级教程  |
| [04-Hello-agents课程常见问题](https://github.com/datawhalechina/hello-agents/blob/main/Extra-Chapter/Extra04-DatawhaleFAQ.md)                 | Datawhale课程常见问题     |
| [05-Agent Skills与MCP对比解读](https://github.com/datawhalechina/hello-agents/blob/main/Extra-Chapter/Extra05-AgentSkills解读.md)             | Agent Skills与MCP技术对比 |
| [06-GUI Agent科普与实战](https://github.com/datawhalechina/hello-agents/blob/main/Extra-Chapter/Extra06-GUIAgent科普与实战.md)                | GUI Agent科普与多场景实战 |
| [07-环境配置](https://github.com/datawhalechina/hello-agents/blob/main/Extra-Chapter/Extra07-环境配置.md)                | 环境配置 |
| [08-如何写出好的Skill](https://github.com/datawhalechina/hello-agents/blob/main/Extra-Chapter/Extra08-如何写出好的Skill.md) | Skill 写作最佳实践 |
| [09-Agent应用开发实践踩坑与经验分享](https://github.com/datawhalechina/hello-agents/blob/main/Extra-Chapter/Extra09-Agent应用开发实践踩坑与经验分享.md) | Code Agent 应用开发踩坑与经验总结 |

### PDF 版本下载

&emsp;&emsp;*<strong>本 Hello-Agents PDF 教程完全开源免费。为防止各类营销号加水印后贩卖给多智能体系统初学者，我们特地在 PDF 文件中预先添加了不影响阅读的 Datawhale 开源标志水印，敬请谅解～</strong>*

> *Hello-Agents PDF : https://github.com/datawhalechina/hello-agents/releases/tag/V1.0.0*  
> *Hello-Agents PDF 国内下载地址 : https://www.datawhale.cn/learn/summary/239* 

## 💡 如何学习

&emsp;&emsp;欢迎你，未来的智能系统构建者！在开启这段激动人心的旅程之前，请允许我们给你一些清晰的指引。

&emsp;&emsp;本项目内容兼顾理论与实战，旨在帮助你系统性地掌握从单个智能体到多智能体系统的设计与开发全流程。因此，尤其适合有一定编程基础的 <strong>AI 开发者、软件工程师、在校学生</strong> 以及对前沿 AI 技术抱有浓厚兴趣的 <strong>自学者</strong>。在学习本项目之前，我们希望你具备基础的 Python 编程能力，并对大语言模型有基本的概念性了解（例如，知道如何通过 API 调用一个 LLM）。项目的重点是应用与构建，因此你无需具备深厚的算法或模型训练背景。

&emsp;&emsp;项目分为五大部分，每一部分都是通往下一阶段的坚实阶梯：

- <strong>第一部分：智能体与语言模型基础</strong>（第一章～第三章），我们将从智能体的定义、类型与发展历史讲起，为你梳理"智能体"这一概念的来龙去脉。随后，我们会快速巩固大语言模型的核心知识，为你的实践之旅打下坚实的理论地基。

- <strong>第二部分：构建你的大语言模型智能体</strong>（第四章～第七章），这是你动手实践的起点。你将亲手实现 ReAct 等经典范式，体验 Coze 等低代码平台的便捷，并掌握 Langgraph 等主流框架的应用。最终，我们还会带你从零开始构建一个属于自己的智能体框架，让你兼具“用轮子”与“造轮子”的能力。

- <strong>第三部分：高级知识扩展</strong>（第八章～第十二章），在这一部分，你的智能体将“学会”思考与协作。我们将使用第二部分的自研框架，深入探索记忆与检索、上下文工程、Agent 训练等核心技术，并学习多智能体间的通信协议。最终，你将掌握评估智能体系统性能的专业方法。

- <strong>第四部分：综合案例进阶</strong>（第十三章～第十五章），这里是理论与实践的交汇点。你将把所学融会贯通，亲手打造智能旅行助手、自动化深度研究智能体，乃至一个模拟社会动态的赛博小镇，在真实有趣的项目中淬炼你的构建能力。

- <strong>第五部分：毕业设计及未来展望</strong>（第十六章），在旅程的终点，你将迎来一个毕业设计，构建一个完整的、属于你自己的多智能体应用，全面检验你的学习成果。我们还将与你一同展望智能体的未来，探索激动人心的前沿方向。


&emsp;&emsp;智能体是一个飞速发展且极度依赖实践的领域。为了获得最佳的学习效果，我们在项目的`code`文件夹内提供了配套的全部代码，强烈建议你<strong>将理论与实践相结合</strong>。请务必亲手运行、调试甚至修改项目里提供的每一份代码。欢迎你随时关注 Datawhale 以及其他 Agent 相关社区，当遇到问题时，你可以随时在本项目的 issue 区提问。

&emsp;&emsp;现在，准备好进入智能体的奇妙世界了吗？让我们即刻启程！

## 下一步规划

- 视频课程陆续放出（将会更加细致，实践课带领大家从设计思路到实施，授人以鱼也授人以渔）
- HelloAgents框架已经更新V1.0.0版本，将会继续完善，增加更多好用，轻量化的工具和特性，兼容学习版本。
- 感谢大家助力3W Star! 之后将会提供调查问卷，供大家填写自己需要学习的智能体训练内容。后续作品《从零开始训练智能体》，帮助每一个学习者掌握从零到一训练自定义场景智能体模型的能力。

## 🤝 如何贡献

我们是一个开放的开源社区，欢迎任何形式的贡献！

- 🐛 <strong>报告 Bug</strong> - 发现内容或代码问题，请提交 Issue
- 💡 <strong>提出建议</strong> - 对项目有好想法，欢迎发起讨论
- 📝 <strong>完善内容</strong> - 帮助改进教程，提交你的 Pull Request
- ✍️ <strong>分享实践</strong> - 在"社区贡献精选"中分享你的学习笔记和项目

## 🙏 致谢

### 核心贡献者
- [陈思州-项目负责人](https://github.com/jjyaoao) (Datawhale 成员, 全文写作和校对)
- [孙韬-联合发起者](https://github.com/fengju0213) (Datawhale 成员、CAMEL-AI, 第九章内容和校对)  
- [姜舒凡-联合发起者](https://github.com/Tsumugii24)（Datawhale 成员, 章节习题设计和校对）
- [黄佩林-Datawhale意向成员](https://github.com/HeteroCat) (Agent 开发工程师, 第五章内容贡献者)
- [曾鑫民-Agent工程师](https://github.com/fancyboi999) (牛客科技, 第十四章案例开发)
- [朱信忠-指导专家](https://xinzhongzhu.github.io/) (Datawhale首席科学家-浙江师范大学杭州人工智能研究院教授)
### Extra-Chapter 贡献者
- [WH](https://github.com/WHQAQ11) (内容贡献者)
- [周奥杰-DW贡献者团队](https://github.com/thunderbolt-fire) (西安交通大学, Extra02 内容贡献)
- [张宸旭-个人开发者](https://github.com/Tasselszcx)(帝国理工学院, Extra03 内容贡献)
- [黄宏晗-DW贡献者团队](https://github.com/XiaoMa-PM) (深圳大学, Extra04 内容贡献)
- [王大鹏-Datawhale成员](https://github.com/ditingdapeng) (高级研发工程师, Extra08 内容贡献)
- [尤逸晖-个人开发者](https://github.com/YYHDBL) (南京信息工程大学, Extra09 内容贡献)

### 特别感谢
- 感谢 [@Sm1les](https://github.com/Sm1les) 对本项目的帮助与支持
- 感谢所有为本项目做出贡献的开发者们 ❤️

<div align=center style="margin-top: 30px;">
  <a href="https://github.com/datawhalechina/Hello-Agents/graphs/contributors">
    <img src="https://contrib.rocks/image?repo=datawhalechina/Hello-Agents" />
  </a>
</div>

## Star History

<div align='center'>
    <img src="./docs/images/star-history-2026324.png" alt="Datawhale" width="90%">
</div>

<div align="center">
  <p>⭐ 如果这个项目对你有帮助，请给我们一个 Star！</p>
</div>

## 读者交流群

<div align='center'>
    <img src="./读者群二维码.png" alt="读者群二维码" width="30%">
    <p>扫描二维码加入读者交流群，与更多学习者交流讨论</p>
</div>

## 关于 Datawhale

<div align='center'>
    <img src="./docs/images/datawhale.png" alt="Datawhale" width="30%">
    <p>扫描二维码关注 Datawhale 公众号，获取更多优质开源内容</p>
</div>

---

## 📜 开源协议

本作品采用[知识共享署名-非商业性使用-相同方式共享 4.0 国际许可协议](http://creativecommons.org/licenses/by-nc-sa/4.0/)进行许可。

```

### File: docs\README.md
```md
<div align="right">
  <a href="./README_EN.md">English</a> | 中文
</div>
<div align='center'>
  <img src="./images/hello-agents.png" alt="alt text" width="100%">
  <h1>Hello-Agents</h1>
  <h3>🤖 《从零开始构建智能体》</h3>
  <div align="center">
  <a href="https://trendshift.io/repositories/15520" target="_blank">
    <img src="https://trendshift.io/api/badge/repositories/15520" alt="datawhalechina%2Fhello-agents | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/>
  </a>
  </div>
  <p><em>从基础理论到实际应用，全面掌握智能体系统的设计与实现</em></p>
  <img src="https://img.shields.io/github/stars/datawhalechina/Hello-Agents?style=flat&logo=github" alt="GitHub stars"/>
  <img src="https://img.shields.io/github/forks/datawhalechina/Hello-Agents?style=flat&logo=github" alt="GitHub forks"/>
  <img src="https://img.shields.io/badge/language-Chinese-brightgreen?style=flat" alt="Language"/>
  <a href="https://github.com/datawhalechina/Hello-Agents"><img src="https://img.shields.io/badge/GitHub-Project-blue?style=flat&logo=github" alt="GitHub Project"></a>
  <a href="https://datawhalechina.github.io/hello-agents/"><img src="https://img.shields.io/badge/在线阅读-Online%20Reading-green?style=flat&logo=gitbook" alt="Online Reading"></a>
</div>


---

## 🎯 项目介绍

&emsp;&emsp;如果说 2024 年是"百模大战"的元年，那么 2025 年无疑开启了"Agent 元年"。技术的焦点正从训练更大的基础模型，转向构建更聪明的智能体应用。然而，当前系统性、重实践的教程却极度匮乏。为此，我们发起了 Hello-Agents 项目，希望能为社区提供一本从零开始、理论与实战并重的智能体系统构建指南。

&emsp;&emsp;Hello-Agents 是 Datawhale 社区的<strong>系统性智能体学习教程</strong>。如今 Agent 构建主要分为两派，一派是 Dify，Coze，n8n 这类软件工程类 Agent，其本质是流程驱动的软件开发，LLM 作为数据处理的后端；另一派则是 AI 原生的 Agent，即真正以 AI 驱动的 Agent。本教程旨在带领大家深入理解并构建后者——真正的 AI Native Agent。教程将带领你穿透框架表象，从智能体的核心原理出发，深入其核心架构，理解其经典范式，并最终亲手构建起属于自己的多智能体应用。我们相信，最好的学习方式就是动手实践。希望这本教程能成为你探索智能体世界的起点，能够从一名大语言模型的"使用者"，蜕变为一名智能体系统的"构建者"。

## 🌐 在线阅读

**[🌐 国外访问](https://datawhalechina.github.io/hello-agents/)** | **[🚀 国内加速](https://hello-agents.datawhale.cc)**

### ✨ 你将收获什么？

- 📖 <strong>Datawhale 开源免费</strong> 完全免费学习本项目所有内容，与社区共同成长
- 🔍 <strong>理解核心原理</strong> 深入理解智能体的概念、历史与经典范式
- 🏗️ <strong>亲手实现</strong> 掌握热门低代码平台和智能体代码框架的使用
- 🛠️ <strong>自研框架[HelloAgents](https://github.com/jjyaoao/helloagents)</strong> 基于 Openai 原生 API 从零构建一个自己的智能体框架
- ⚙️ <strong>掌握高级技能</strong> 一步步实现上下文工程、Memory、协议、评估等系统性技术
- 🤝 <strong>模型训练</strong> 掌握 Agentic RL，从 SFT 到 GRPO 的全流程实战训练 LLM
- 🚀 <strong>驱动真实案例</strong> 实战开发智能旅行助手、赛博小镇等综合项目
- 📖 <strong>求职面试</strong> 学习智能体求职相关面试问题

## 📖 内容导航

| 章节                                                                                   | 关键内容                                      | 状态 |
| -------------------------------------------------------------------------------------- | --------------------------------------------- | ---- |
| [前言](./前言.md)                                                                      | 项目的缘起、背景及读者建议                    | ✅    |
| <strong>第一部分：智能体与语言模型基础</strong>                                        |                                               |      |
| [第一章 初识智能体](./chapter1/第一章%20初识智能体.md)                                 | 智能体定义、类型、范式与应用                  | ✅    |
| [第二章 智能体发展史](./chapter2/第二章%20智能体发展史.md)                             | 从符号主义到 LLM 驱动的智能体演进             | ✅    |
| [第三章 大语言模型基础](./chapter3/第三章%20大语言模型基础.md)                         | Transformer、提示、主流 LLM 及其局限          | ✅    |
| <strong>第二部分：构建你的大语言模型智能体</strong>                                    |                                               |      |
| [第四章 智能体经典范式构建](./chapter4/第四章%20智能体经典范式构建.md)                 | 手把手实现 ReAct、Plan-and-Solve、Reflection  | ✅    |
| [第五章 基于低代码平台的智能体搭建](./chapter5/第五章%20基于低代码平台的智能体搭建.md) | 了解 Coze、Dify、n8n 等低代码智能体平台使用   | ✅    |
| [第六章 框架开发实践](./chapter6/第六章%20框架开发实践.md)                             | AutoGen、AgentScope、LangGraph 等主流框架应用 | ✅    |
| [第七章 构建你的Agent框架](./chapter7/第七章%20构建你的Agent框架.md)                   | 从 0 开始构建智能体框架                       | ✅    |
| <strong>第三部分：高级知识扩展</strong>                                                |                                               |      |
| [第八章 记忆与检索](./chapter8/第八章%20记忆与检索.md)                                 | 记忆系统，RAG，存储                           | ✅    |
| [第九章 上下文工程](./chapter9/第九章%20上下文工程.md)                                 | 持续交互的"情境理解"                          | ✅    |
| [第十章 智能体通信协议](./chapter10/第十章%20智能体通信协议.md)                        | MCP、A2A、ANP 等协议解析                      | ✅    |
| [第十一章 Agentic-RL](./chapter11/第十一章%20Agentic-RL.md)                            | 从 SFT 到 GRPO 的 LLM 训练实战                | ✅    |
| [第十二章 智能体性能评估](./chapter12/第十二章%20智能体性能评估.md)                    | 核心指标、基准测试与评估框架                  | ✅    |
| <strong>第四部分：综合案例进阶</strong>                                                |                                               |      |
| [第十三章 智能旅行助手](./chapter13/第十三章%20智能旅行助手.md)                        | MCP 与多智能体协作的真实世界应用              | ✅    |
| [第十四章 自动化深度研究智能体](./chapter14/第十四章%20自动化深度研究智能体.md)        | DeepResearch Agent 复现与解析                 | ✅    |
| [第十五章 构建赛博小镇](./chapter15/第十五章%20构建赛博小镇.md)                        | Agent 与游戏的结合，模拟社会动态              | ✅    |
| <strong>第五部分：毕业设计及未来展望</strong>                                          |                                               |      |
| [第十六章 毕业设计](./chapter16/第十六章%20毕业设计.md)                                | 构建属于你的完整多智能体应用                  | ✅    |

### 社区贡献精选 (Community Blog)

&emsp;&emsp;欢迎大家将在学习 Hello-Agents 或 Agent 相关技术中的独到见解、实践总结，以 PR 的形式贡献到社区精选。如果是独立于正文的内容，也可以投稿至 Extra-Chapter！<strong>期待你的第一次贡献！</strong>

| 社区精选                                                                                                                                      | 内容总结                  |
| --------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- |
| [00-共创毕业设计](https://github.com/datawhalechina/hello-agents/blob/main/Co-creation-projects)                                             | 社区共创毕业设计项目      |
| [01-Agent面试题总结](https://github.com/datawhalechina/hello-agents/blob/main/Extra-Chapter/Extra01-面试问题总结.md)                          | Agent 岗位相关面试问题    |
| [01-Agent面试题答案](https://github.com/datawhalechina/hello-agents/blob/main/Extra-Chapter/Extra01-参考答案.md)                              | 相关面试问题答案          |
| [02-上下文工程内容补充](https://github.com/datawhalechina/hello-agents/blob/main/Extra-Chapter/Extra02-上下文工程补充知识.md)                 | 上下文工程内容扩展        |
| [03-Dify智能体创建保姆级教程](https://github.com/datawhalechina/hello-agents/blob/main/Extra-Chapter/Extra03-Dify智能体创建保姆级操作流程.md) | Dify智能体创建保姆级教程  |
| [04-Hello-agents课程常见问题](https://github.com/datawhalechina/hello-agents/blob/main/Extra-Chapter/Extra04-DatawhaleFAQ.md)                 | Datawhale课程常见问题     |
| [05-Agent Skills与MCP对比解读](https://github.com/datawhalechina/hello-agents/blob/main/Extra-Chapter/Extra05-AgentSkills解读.md)             | Agent Skills与MCP技术对比 |
| [06-GUI Agent科普与实战](https://github.com/datawhalechina/hello-agents/blob/main/Extra-Chapter/Extra06-GUIAgent科普与实战.md)                | GUI Agent科普与多场景实战 |
| [07-环境配置](https://github.com/datawhalechina/hello-agents/blob/main/Extra-Chapter/Extra07-环境配置.md)                | 环境配置 |
| [08-如何写出好的Skill](https://github.com/datawhalechina/hello-agents/blob/main/Extra-Chapter/Extra08-如何写出好的Skill.md) | Skill 写作最佳实践 |
| [09-Agent应用开发实践踩坑与经验分享](https://github.com/datawhalechina/hello-agents/blob/main/Extra-Chapter/Extra09-Agent应用开发实践踩坑与经验分享.md) | Code Agent 应用开发踩坑与经验总结 |

### PDF 版本下载

&emsp;&emsp; *<strong>本 Hello-Agents PDF 教程完全开源免费。为防止各类营销号加水印后贩卖给多智能体系统初学者，我们特地在 PDF 文件中预先添加了不影响阅读的 Datawhale 开源标志水印，敬请谅解～</strong>*

> *Hello-Agents PDF : https://github.com/datawhalechina/hello-agents/releases/tag/V1.0.0*  
> *Hello-Agents PDF 国内下载地址 : https://www.datawhale.cn/learn/summary/239* 

## 💡 如何学习

&emsp;&emsp;欢迎你，未来的智能系统构建者！在开启这段激动人心的旅程之前，请允许我们给你一些清晰的指引。

&emsp;&emsp;本项目内容兼顾理论与实战，旨在帮助你系统性地掌握从单个智能体到多智能体系统的设计与开发全流程。因此，尤其适合有一定编程基础的 <strong>AI 开发者、软件工程师、在校学生</strong> 以及对前沿 AI 技术抱有浓厚兴趣的 <strong>自学者</strong>。在学习本项目之前，我们希望你具备基础的 Python 编程能力，并对大语言模型有基本的概念性了解（例如，知道如何通过 API 调用一个 LLM）。项目的重点是应用与构建，因此你无需具备深厚的算法或模型训练背景。

&emsp;&emsp;项目分为五大部分，每一部分都是通往下一阶段的坚实阶梯：

- <strong>第一部分：智能体与语言模型基础</strong>（第一章～第三章），我们将从智能体的定义、类型与发展历史讲起，为你梳理"智能体"这一概念的来龙去脉。随后，我们会快速巩固大语言模型的核心知识，为你的实践之旅打下坚实的理论地基。

- <strong>第二部分：构建你的大语言模型智能体</strong>（第四章～第七章），这是你动手实践的起点。你将亲手实现 ReAct 等经典范式，体验 Coze 等低代码平台的便捷，并掌握 Langgraph 等主流框架的应用。最终，我们还会带你从零开始构建一个属于自己的智能体框架，让你兼具“用轮子”与“造轮子”的能力。

- <strong>第三部分：高级知识扩展</strong>（第八章～第十二章），在这一部分，你的智能体将“学会”思考与协作。我们将使用第二部分的自研框架，深入探索记忆与检索、上下文工程、Agent 训练等核心技术，并学习多智能体间的通信协议。最终，你将掌握评估智能体系统性能的专业方法。

- <strong>第四部分：综合案例进阶</strong>（第十三章～第十五章），这里是理论与实践的交汇点。你将把所学融会贯通，亲手打造智能旅行助手、自动化深度研究智能体，乃至一个模拟社会动态的赛博小镇，在真实有趣的项目中淬炼你的构建能力。

- <strong>第五部分：毕业设计及未来展望</strong>（第十六章），在旅程的终点，你将迎来一个毕业设计，构建一个完整的、属于你自己的多智能体应用，全面检验你的学习成果。我们还将与你一同展望智能体的未来，探索激动人心的前沿方向。


&emsp;&emsp;智能体是一个飞速发展且极度依赖实践的领域。为了获得最佳的学习效果，我们在项目的`code`文件夹内提供了配套的全部代码，强烈建议你<strong>将理论与实践相结合</strong>。请务必亲手运行、调试甚至修改项目里提供的每一份代码。欢迎你随时关注 Datawhale 以及其他 Agent 相关社区，当遇到问题时，你可以随时在本项目的 issue 区提问。

&emsp;&emsp;现在，准备好进入智能体的奇妙世界了吗？让我们即刻启程！

## 🤝 如何贡献

我们是一个开放的开源社区，欢迎任何形式的贡献！

- 🐛 <strong>报告 Bug</strong> - 发现内容或代码问题，请提交 Issue
- 💡 <strong>提出建议</strong> - 对项目有好想法，欢迎发起讨论
- 📝 <strong>完善内容</strong> - 帮助改进教程，提交你的 Pull Request
- ✍️ <strong>分享实践</strong> - 在"社区贡献精选"中分享你的学习笔记和项目

## 🙏 致谢

### 核心贡献者
- [陈思州-项目负责人](https://github.com/jjyaoao) (Datawhale 成员, 全文写作和校对)
- [孙韬-联合发起者](https://github.com/fengju0213) (Datawhale 成员、CAMEL-AI, 第九章内容和校对)
- [姜舒凡-联合发起者](https://github.com/Tsumugii24)（Datawhale 成员, 章节习题设计和校对）
- [黄佩林-Datawhale意向成员](https://github.com/HeteroCat) (Agent 开发工程师, 第五章内容贡献者)
- [曾鑫民-Agent工程师](https://github.com/fancyboi999) (牛客科技, 第十四章案例开发)
- [朱信忠-指导专家](https://xinzhongzhu.github.io/) (Datawhale首席科学家-浙江师范大学杭州人工智能研究院教授)

### Extra-Chapter 贡献者
- [WH](https://github.com/WHQAQ11) (内容贡献者)
- [周奥杰-DW贡献者团队](https://github.com/thunderbolt-fire) (西安交通大学, Extra02 内容贡献)
- [张宸旭-个人开发者](https://github.com/Tasselszcx)(帝国理工学院, Extra03 内容贡献)
- [黄宏晗-DW贡献者团队](https://github.com/XiaoMa-PM) (深圳大学, Extra04 内容贡献)
- [王大鹏-Datawhale成员](https://github.com/ditingdapeng) (高级研发工程师, Extra08 内容贡献)
- [尤逸晖-个人开发者](https://github.com/YYHDBL) (南京信息工程大学, Extra09 内容贡献)

### 特别感谢
- 感谢 [@Sm1les](https://github.com/Sm1les) 对本项目的帮助与支持
- 感谢所有为本项目做出贡献的开发者们 ❤️

<div align=center style="margin-top: 30px;">
  <a href="https://github.com/datawhalechina/Hello-Agents/graphs/contributors">
    <img src="https://contrib.rocks/image?repo=datawhalechina/Hello-Agents" />
  </a>
</div>

## Star History

<div align='center'>
    <img src="./images/star-history-2026324.png" alt="Datawhale" width="90%">
</div>

<div align="center">
  <p>⭐ 如果这个项目对你有帮助，请给我们一个 Star！</p>
</div>

## 读者交流群

<div align='center'>
    <img src="./读者群二维码.png" alt="读者群二维码" width="30%">
    <p>扫描二维码加入读者交流群，与更多学习者交流讨论</p>
</div>

## 关于 Datawhale

<div align='center'>
    <img src="./images/datawhale.png" alt="Datawhale" width="30%">
    <p>扫描二维码关注 Datawhale 公众号，获取更多优质开源内容</p>
</div>

---

## 📜 开源协议

本作品采用[知识共享署名-非商业性使用-相同方式共享 4.0 国际许可协议](http://creativecommons.org/licenses/by-nc-sa/4.0/)进行许可。

```

### File: fix_bold_format.py
```py
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批量修复Markdown文件中的加粗格式
将 **文本** 替换为 <strong>文本</strong>
"""

import re
import os
import glob

def fix_bold_format_in_file(file_path):
    """修复单个文件中的加粗格式"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 先找出所有代码块的位置
        code_blocks = []
        code_pattern = r'```[\s\S]*?```'
        for match in re.finditer(code_pattern, content):
            code_blocks.append((match.start(), match.end()))
        
        # 使用正则表达式匹配 **文本** 并替换为 <strong>文本</strong>
        # 确保不匹配已经是HTML标签的情况和代码块内的情况
        pattern = r'\*\*([^*]+?)\*\*'
        
        def replacement_func(match):
            # 检查匹配位置是否在代码块内
            match_start = match.start()
            for block_start, block_end in code_blocks:
                if block_start <= match_start < block_end:
                    return match.group(0)  # 在代码块内，不替换
            return f'<strong>{match.group(1)}</strong>'  # 不在代码块内，进行替换
        
        # 执行替换
        new_content = re.sub(pattern, replacement_func, content)
        
        # 如果内容有变化，写回文件
        if new_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✅ 已修复: {file_path}")
            return True
        else:
            print(f"ℹ️  无需修改: {file_path}")
            return False
            
    except Exception as e:
        print(f"❌ 处理文件出错 {file_path}: {e}")
        return False

def main():
    """主函数"""
    # 查找所有Markdown文件
    docs_dir = "xxx/xxx"
    
    # 递归查找所有.md文件
    md_files = []
    for root, dirs, files in os.walk(docs_dir):
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))
    
    print(f"找到 {len(md_files)} 个Markdown文件")
    print("=" * 50)
    
    modified_count = 0
    for file_path in md_files:
        if fix_bold_format_in_file(file_path):
            modified_count += 1
    
    print("=" * 50)
    print(f"处理完成！共修改了 {modified_count} 个文件")

if __name__ == "__main__":
    main()

```

### File: LICENSE.txt
```txt
Attribution-NonCommercial-ShareAlike 4.0 International

=======================================================================

Creative Commons Corporation ("Creative Commons") is not a law firm and
does not provide legal services or legal advice. Distribution of
Creative Commons public licenses does not create a lawyer-client or
other relationship. Creative Commons makes its licenses and related
information available on an "as-is" basis. Creative Commons gives no
warranties regarding its licenses, any material licensed under their
terms and conditions, or any related information. Creative Commons
disclaims all liability for damages resulting from their use to the
fullest extent possible.

Using Creative Commons Public Licenses

Creative Commons public licenses provide a standard set of terms and
conditions that creators and other rights holders may use to share
original works of authorship and other material subject to copyright
and certain other rights specified in the public license below. The
following considerations are for informational purposes only, are not
exhaustive, and do not form part of our licenses.

     Considerations for licensors: Our public licenses are
     intended for use by those authorized to give the public
     permission to use material in ways otherwise restricted by
     copyright and certain other rights. Our licenses are
     irrevocable. Licensors should read and understand the terms
     and conditions of the license they choose before applying it.
     Licensors should also secure all rights necessary before
     applying our licenses so that the public can reuse the
     material as expected. Licensors should clearly mark any
     material not subject to the license. This includes other CC-
     licensed material, or material used under an exception or
     limitation to copyright. More considerations for licensors:
    wiki.creativecommons.org/Considerations_for_licensors

     Considerations for the public: By using one of our public
     licenses, a licensor grants the public permission to use the
     licensed material under specified terms and conditions. If
     the licensor's permission is not necessary for any reason--for
     example, because of any applicable exception or limitation to
     copyright--then that use is not regulated by the license. Our
     licenses grant only permissions under copyright and certain
     other rights that a licensor has authority to grant. Use of
     the licensed material may still be restricted for other
     reasons, including because others have copyright or other
     rights in the material. A licensor may make special requests,
     such as asking that all changes be marked or described.
     Although not required by our licenses, you are encouraged to
     respect those requests where reasonable. More considerations
     for the public:
    wiki.creativecommons.org/Considerations_for_licensees

=======================================================================

Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International
Public License

By exercising the Licensed Rights (defined below), You accept and agree
to be bound by the terms and conditions of this Creative Commons
Attribution-NonCommercial-ShareAlike 4.0 International Public License
("Public License"). To the extent this Public License may be
interpreted as a contract, You are granted the Licensed Rights in
consideration of Your acceptance of these terms and conditions, and the
Licensor grants You such rights in consideration of benefits the
Licensor receives from making the Licensed Material available under
these terms and conditions.


Section 1 -- Definitions.

  a. Adapted Material means material subject to Copyright and Similar
     Rights that is derived from or based upon the Licensed Material
     and in which the Licensed Material is translated, altered,
     arranged, transformed, or otherwise modified in a manner requiring
     permission under the Copyright and Similar Rights held by the
     Licensor. For purposes of this Public License, where the Licensed
     Material is a musical work, performance, or sound recording,
     Adapted Material is always produced where the Licensed Material is
     synched in timed relation with a moving image.

  b. Adapter's License means the license You apply to Your Copyright
     and Similar Rights in Your contributions to Adapted Material in
     accordance with the terms and conditions of this Public License.

  c. BY-NC-SA Compatible License means a license listed at
     creativecommons.org/compatiblelicenses, approved by Creative
     Commons as essentially the equivalent of this Public License.

  d. Copyright and Similar Rights means copyright and/or similar rights
     closely related to copyright including, without limitation,
     performance, broadcast, sound recording, and Sui Generis Database
     Rights, without regard to how the rights are labeled or
     categorized. For purposes of this Public License, the rights
     specified in Section 2(b)(1)-(2) are not Copyright and Similar
     Rights.

  e. Effective Technological Measures means those measures that, in the
     absence of proper authority, may not be circumvented under laws
     fulfilling obligations under Article 11 of the WIPO Copyright
     Treaty adopted on December 20, 1996, and/or similar international
     agreements.

  f. Exceptions and Limitations means fair use, fair dealing, and/or
     any other exception or limitation to Copyright and Similar Rights
     that applies to Your use of the Licensed Material.

  g. License Elements means the license attributes listed in the name
     of a Creative Commons Public License. The License Elements of this
     Public License are Attribution, NonCommercial, and ShareAlike.

  h. Licensed Material means the artistic or literary work, database,
     or other material to which the Licensor applied this Public
     License.

  i. Licensed Rights means the rights granted to You subject to the
     terms and conditions of this Public License, which are limited to
     all Copyright and Similar Rights that apply to Your use of the
     Licensed Material and that the Licensor has authority to license.

  j. Licensor means the individual(s) or entity(ies) granting rights
     under this Public License.

  k. NonCommercial means not primarily intended for or directed towards
     commercial advantage or monetary compensation. For purposes of
     this Public License, the exchange of the Licensed Material for
     other material subject to Copyright and Similar Rights by digital
     file-sharing or similar means is NonCommercial provided there is
     no payment of monetary compensation in connection with the
     exchange.

  l. Share means to provide material to the public by any means or
     process that requires permission under the Licensed Rights, such
     as reproduction, public display, public performance, distribution,
     dissemination, communication, or importation, and to make material
     available to the public including in ways that members of the
     public may access the material from a place and at a time
     individually chosen by them.

  m. Sui Generis Database Rights means rights other than copyright
     resulting from Directive 96/9/EC of the European Parliament and of
     the Council of 11 March 1996 on the legal protection of databases,
     as amended and/or succeeded, as well as other essentially
     equivalent rights anywhere in the world.

  n. You means the individual or entity exercising the Licensed Rights
     under this Public License. Your has a corresponding meaning.


Section 2 -- Scope.

  a. License grant.

       1. Subject to the terms and conditions of this Public License,
          the Licensor hereby grants You a worldwide, royalty-free,
          non-sublicensable, non-exclusive, irrevocable license to
          exercise the Licensed Rights in the Licensed Material to:

            a. reproduce and Share the Licensed Material, in whole or
               in part, for NonCommercial purposes only; and

            b. produce, reproduce, and Share Adapted Material for
               NonCommercial purposes only.

       2. Exceptions and Limitations. For the avoidance of doubt, where
          Exceptions and Limitations apply to Your use, this Public
          License does not apply, and You do not need to comply with
          its terms and conditions.

       3. Term. The term of this Public License is specified in Section
          6(a).

       4. Media and formats; technical modifications allowed. The
          Licensor authorizes You to exercise the Licensed Rights in
          all media and formats whether now known or hereafter created,
          and to make technical modifications necessary to do so. The
          Licensor waives and/or agrees not to assert any right or
          authority to forbid You from making technical modifications
          necessary to exercise the Licensed Rights, including
          technical modifications necessary to circumvent Effective
          Technological Measures. For purposes of this Public License,
          simply making modifications authorized by this Section 2(a)
          (4) never produces Adapted Material.

       5. Downstream recipients.

            a. Offer from the Licensor -- Licensed Material. Every
               recipient of the Licensed Material automatically
               receives an offer from the Licensor to exercise the
               Licensed Rights under the terms and conditions of this
               Public License.

            b. Additional offer from the Licensor -- Adapted Material.
               Every recipient of Adapted Material from You
               automatically receives an offer from the Licensor to
               exercise the Licensed Rights in the Adapted Material
               under the conditions of the Adapter's License You apply.

            c. No downstream restrictions. You may not offer or impose
               any additional or different terms or conditions on, or
               apply any Effective Technological Measures to, the
               Licensed Material if doing so restricts exercise of the
               Licensed Rights by any recipient of the Licensed
               Material.

       6. No endorsement. Nothing in this Public License constitutes or
          may be construed as permission to assert or imply that You
          are, or that Your use of the Licensed Material is, connected
          with, or sponsored, endorsed, or granted official status by,
          the Licensor or others designated to receive attribution as
          provided in Section 3(a)(1)(A)(i).

  b. Other rights.

       1. Moral rights, such as the right of integrity, are not
          licensed under this Public License, nor are publicity,
          privacy, and/or other similar personality rights; however, to
          the extent possible, the Licensor waives and/or agrees not to
          assert any such rights held by the Licensor to the limited
          extent necessary to allow You to exercise the Licensed
          Rights, but not otherwise.

       2. Patent and trademark rights are not licensed under this
          Public License.

       3. To the extent possible, the Licensor waives any right to
          collect royalties from You for the exercise of the Licensed
          Rights, whether directly or through a collecting society
          under any voluntary or waivable statutory or compulsory
          licensing scheme. In all other cases the Licensor expressly
          reserves any right to collect such royalties, including when
          the Licensed Material is used other than for NonCommercial
          purposes.


Section 3 -- License Conditions.

Your exercise of the Licensed Rights is expressly made subject to the
following conditions.

  a. Attribution.

       1. If You Share the Licensed Material (including in modified
          form), You must:

            a. retain the following if it is supplied by the Licensor
               with the Licensed Material:

                 i. identification of the creator(s) of the Licensed
                    Material and any others designated to receive
                    attribution, in any reasonable manner requested by
                    the Licensor (including by pseudonym if
                    designated);

                ii. a copyright notice;

               iii. a notice that refers to this Public License;

                iv. a notice that refers to the disclaimer of
                    warranties;

                 v. a URI or hyperlink to the Licensed Material to the
                    extent reasonably practicable;

            b. indicate if You modified the Licensed Material and
               retain an indication of any previous modifications; and

            c. indicate the Licensed Material is licensed under this
               Public License, and include the text of, or the URI or
               hyperlink to, this Public License.

       2. You may satisfy the conditions in Section 3(a)(1) in any
          reasonable manner based on the medium, means, and context in
          which You Share the Licensed Material. For example, it may be
          reasonable to satisfy the conditions by providing a URI or
          hyperlink to a resource that includes the required
          information.
       3. If requested by the Licensor, You must remove any of the
          information required by Section 3(a)(1)(A) to the extent
          reasonably practicable.

  b. ShareAlike.

     In addition to the conditions in Section 3(a), if You Share
     Adapted Material You produce, the following conditions also apply.

       1. The Adapter's License You apply must be a Creative Commons
          license with the same License Elements, this version or
          later, or a BY-NC-SA Compatible License.

       2. You must include the text of, or the URI or hyperlink to, the
          Adapter's License You apply. You may satisfy this condition
          in any reasonable manner based on the medium, means, and
          context in which You Share Adapted Material.

       3. You may not offer or impose any additional or different terms
          or conditions on, or apply any Effective Technological
          Measures to, Adapted Material that restrict exercise of the
          rights granted under the Adapter's License You apply.


Section 4 -- Sui Generis Database Rights.

Where the Licensed Rights include Sui Generis Database Rights that
apply to Your use of the Licensed Material:

  a. for the avoidance of doubt, Section 2(a)(1) grants You the right
     to extract, reuse, reproduce, and Share all or a substantial
     portion of the contents of the database for NonCommercial purposes
     only;

  b. if You include all or a substantial portion of the database
     contents in a datab
... [TRUNCATED]
```

### File: README_EN.md
```md
<div align="right">
  English | <a href="./README.md">中文</a>
</div>

<div align='center'>
  <img src="./docs/images/hello-agents.png" alt="alt text" width="100%">
  <h1>Hello-Agents</h1>
  <h3>🤖 "Building Agent Systems from Scratch"</h3>
  <div align="center">
  <a href="https://trendshift.io/repositories/15520" target="_blank">
    <img src="https://trendshift.io/api/badge/repositories/15520" alt="datawhalechina%2Fhello-agents | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/>
  </a>
  </div>
  <p><em>From foundational theory to practical applications, master the design and implementation of agent systems</em></p>
  <img src="https://img.shields.io/github/stars/datawhalechina/Hello-Agents?style=flat&logo=github" alt="GitHub stars"/>
  <img src="https://img.shields.io/github/forks/datawhalechina/Hello-Agents?style=flat&logo=github" alt="GitHub forks"/>
  <img src="https://img.shields.io/badge/language-English-brightgreen?style=flat" alt="Language"/>
  <a href="https://github.com/datawhalechina/Hello-Agents"><img src="https://img.shields.io/badge/GitHub-Project-blue?style=flat&logo=github" alt="GitHub Project"></a>
  <a href="https://datawhalechina.github.io/hello-agents/"><img src="https://img.shields.io/badge/Online%20Reading-green?style=flat&logo=gitbook" alt="Online Reading"></a>
</div>

---

## 🎯 Project Introduction

&emsp;&emsp;If 2024 was the year of the "Battle of a Hundred Models," then 2025 has undoubtedly ushered in the "Year of Agents." The focus of technology is shifting from training larger foundation models to building smarter agent applications. However, systematic, practice-oriented tutorials are extremely scarce. For this reason, we launched the Hello-Agents project, hoping to provide the community with a comprehensive guide to building agent systems from scratch, balancing theory and practice.

&emsp;&emsp;Hello-Agents is a **systematic agent learning tutorial** from the Datawhale community. Today, agent development is mainly divided into two schools: one is software engineering-oriented agents like Dify, Coze, and n8n, which are essentially process-driven software development with LLMs serving as data processing backends; the other is AI-native agents, truly AI-driven agents. This tutorial aims to lead you to deeply understand and build the latter—truly AI Native Agents. The tutorial will guide you through the surface of frameworks, starting from the core principles of agents, delving into their core architecture, understanding their classic paradigms, and ultimately building your own multi-agent applications. We believe that the best way to learn is through hands-on practice. We hope this tutorial can be your starting point for exploring the world of agents, transforming you from a "user" of large language models to a "builder" of agent systems.

## 📚 Quick Start

### Online Reading
**[🌐 International Access](https://datawhalechina.github.io/hello-agents/)** | **[🚀 Domestic Acceleration](https://hello-agents.datawhale.cc)** - No download required, learn anytime, anywhere

### Local Reading
If you wish to read locally or contribute content, please refer to the learning guide below.

### ✨ What Will You Gain?

- 📖 **Datawhale Open Source & Free** - Learn all project content completely free, grow with the community
- 🔍 **Understand Core Principles** - Deeply understand agent concepts, history, and classic paradigms
- 🏗️ **Hands-on Implementation** - Master popular low-code platforms and agent code frameworks
- 🛠️ **Self-developed Framework [HelloAgents](https://github.com/jjyaoao/helloagents)** - Build your own agent framework from scratch based on OpenAI native API
- ⚙️ **Master Advanced Skills** - Step-by-step implementation of context engineering, Memory, protocols, evaluation, and other systematic technologies
- 🤝 **Model Training** - Master Agentic RL, from SFT to GRPO full-process practical LLM training
- 🚀 **Drive Real Cases** - Practical development of intelligent travel assistants, cyber towns, and other comprehensive projects
- 📖 **Job Interviews** - Learn agent-related interview questions for job hunting

## 📖 Content Navigation

| Chapter                                                                                                               | Key Content                                                                | Status |
| --------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- | ------ |
| [Preface](./docs/Preface.md)                                                                                          | Project origin, background, and reader suggestions                         | ✅      |
| **Part 1: Agent and Language Model Fundamentals**                                                                     |                                                                            |        |
| [Chapter 1: Introduction to Agents](./docs/chapter1/Chapter1-Introduction-to-Agents.md)                               | Agent definition, types, paradigms, and applications                       | ✅      |
| [Chapter 2: History of Agents](./docs/chapter2/Chapter2-History-of-Agents.md)                                         | Evolution from symbolism to LLM-driven agents                              | ✅      |
| [Chapter 3: Large Language Model Fundamentals](./docs/chapter3/Chapter3-Fundamentals-of-Large-Language-Models.md)     | Transformer, prompts, mainstream LLMs and their limitations                | ✅      |
| **Part 2: Building Your LLM Agent**                                                                                   |                                                                            |        |
| [Chapter 4: Classic Agent Paradigm Construction](./docs/chapter4/Chapter4-Building-Classic-Agent-Paradigms.md)        | Hands-on implementation of ReAct, Plan-and-Solve, Reflection               | ✅      |
| [Chapter 5: Low-Code Platform Agent Development](./docs/chapter5/Chapter5-Building-Agents-with-Low-Code-Platforms.md) | Understanding Coze, Dify, n8n and other low-code agent platforms           | ✅      |
| [Chapter 6: Framework Development Practice](./docs/chapter6/Chapter6-Framework-Development-Practice.md)               | AutoGen, AgentScope, LangGraph and other mainstream framework applications | ✅      |
| [Chapter 7: Building Your Agent Framework](./docs/chapter7/Chapter7-Building-Your-Agent-Framework.md)                 | Building an agent framework from scratch                                   | ✅      |
| **Part 3: Advanced Knowledge Extension**                                                                              |                                                                            |        |
| [Chapter 8: Memory and Retrieval](./docs/chapter8/Chapter8-Memory-and-Retrieval.md)                                   | Memory systems, RAG, storage                                               | ✅      |
| [Chapter 9: Context Engineering](./docs/chapter9/Chapter9-Context-Engineering.md)                                     | "Contextual understanding" for continuous interaction                      | ✅      |
| [Chapter 10: Agent Communication Protocols](./docs/chapter10/Chapter10-Agent-Communication-Protocols.md)              | MCP, A2A, ANP and other protocol analysis                                  | ✅      |
| [Chapter 11: Agentic-RL](./docs/chapter11/Chapter11-Agentic-RL.md)                                                    | Practical LLM training from SFT to GRPO                                    | ✅      |
| [Chapter 12: Agent Performance Evaluation](./docs/chapter12/Chapter12-Agent-Performance-Evaluation.md)                | Core metrics, benchmarks, and evaluation frameworks                        | ✅      |
| **Part 4: Comprehensive Case Studies**                                                                                |                                                                            |        |
| [Chapter 13: Intelligent Travel Assistant](./docs/chapter13/Chapter13-Intelligent-Travel-Assistant.md)                | Real-world applications of MCP and multi-agent collaboration               | ✅      |
| [Chapter 14: Automated Deep Research Agent](./docs/chapter14/Chapter14-Automated-Deep-Research-Agent.md)              | DeepResearch Agent reproduction and analysis                               | ✅      |
| [Chapter 15: Building a Cyber Town](./docs/chapter15/Chapter15-Building-Cyber-Town.md)                                | Combining agents with games, simulating social dynamics                    | ✅      |
| **Part 5: Capstone Project and Future Outlook**                                                                       |                                                                            |        |
| [Chapter 16: Capstone Project](./docs/chapter16/Chapter16-Graduation-Project.md)                                      | Build your own complete multi-agent application                            | ✅      |

### Community Contributions

&emsp;&emsp;We welcome everyone to contribute their unique insights and practical summaries from learning Hello-Agents or Agent-related technologies to the community selection in the form of PRs. If the content is independent of the main text, you can also submit it to Extra-Chapter! **Looking forward to your first contribution!**

| Community Selection                                                                                                                                            | Content Summary                            |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| [00-Co-creation Capstone Projects](https://github.com/datawhalechina/hello-agents/blob/main/Co-creation-projects)                                             | Community co-creation capstone projects    |
| [01-Agent Interview Questions Summary](https://github.com/datawhalechina/hello-agents/blob/main/Extra-Chapter/Extra01-面试问题总结.md)                         | Agent position-related interview questions |
| [01-Agent Interview Answers](https://github.com/datawhalechina/hello-agents/blob/main/Extra-Chapter/Extra01-参考答案.md)                                       | Answers to related interview questions     |
| [02-Context Engineering Content Supplement](https://github.com/datawhalechina/hello-agents/blob/main/Extra-Chapter/Extra02-上下文工程补充知识.md)              | Context engineering content extension      |
| [03-Dify Agent Creation Step-by-Step Tutorial](https://github.com/datawhalechina/hello-agents/blob/main/Extra-Chapter/Extra03-Dify智能体创建保姆级操作流程.md) | Dify Agent Creation Step-by-Step Tutorial  |
| [04-Hello-agents Course Common Questions](https://github.com/datawhalechina/hello-agents/blob/main/Extra-Chapter/Extra04-DatawhaleFAQ.md)                      | Datawhale Course Common Questions          |
| [05-Agent Skills vs MCP Comparison](https://github.com/datawhalechina/hello-agents/blob/main/Extra-Chapter/Extra05-AgentSkills解读.md)                         | Agent Skills vs MCP Technical Comparison   |
| [06-GUI Agent Overview and Hands-on Practice](https://github.com/datawhalechina/hello-agents/blob/main/Extra-Chapter/Extra06-GUIAgent科普与实战.md)            | GUI Agent concepts and practical tutorials |
| [07-Environment Configuration](https://github.com/datawhalechina/hello-agents/blob/main/Extra-Chapter/Extra07-环境配置.md)            | Environment Configuration |
| [08-How to Write Good Skills](https://github.com/datawhalechina/hello-agents/blob/main/Extra-Chapter/Extra08-如何写出好的Skill.md) | Skill writing best practices |
| [09-Agent Development Pitfalls and Practical Lessons](https://github.com/datawhalechina/hello-agents/blob/main/Extra-Chapter/Extra09-Agent应用开发实践踩坑与经验分享.md) | Practical lessons and pitfalls from building a Code Agent |

### PDF Version Download

&emsp;&emsp;*<strong>This Hello-Agents PDF tutorial is completely open source and free. To prevent various marketing accounts from adding watermarks and selling it to multi-agent system beginners, we have pre-added a Datawhale open source logo watermark that does not affect reading in the PDF file. Please understand~</strong>*

> *Hello-Agents PDF: https://github.com/datawhalechina/hello-agents/releases/tag/V1.0.0*  
> *Hello-Agents PDF Domestic Download: https://www.datawhale.cn/learn/summary/239* 

## 💡 How to Learn

&emsp;&emsp;Welcome, future builder of intelligent systems! Before embarking on this exciting journey, please allow us to give you some clear guidance.

&emsp;&emsp;This project balances theory and practice, aiming to help you systematically master the entire process of designing and developing from single agents to multi-agent systems. Therefore, it is especially suitable for **AI developers, software engineers, students** with some programming foundation, as well as **self-learners** with a strong interest in cutting-edge AI technology. Before learning this project, we hope you have basic Python programming skills and a basic conceptual understanding of large language models (for example, knowing how to call an LLM through an API). The focus of the project is on application and construction, so you do not need a deep background in algorithms or model training.

&emsp;&emsp;The project is divided into five major parts, each being a solid step towards the next stage:

- **Part 1: Agent and Language Model Fundamentals** (Chapters 1-3), we will start from the definition, types, and development history of agents, sorting out the ins and outs of the concept of "agents." Then, we will quickly consolidate the core knowledge of large language models, laying a solid theoretical foundation for your practical journey.

- **Part 2: Building Your LLM Agent** (Chapters 4-7), this is the starting point of your hands-on practice. You will personally implement classic paradigms such as ReAct, experience the convenience of low-code platforms like Coze, and master the application of mainstream frameworks like Langgraph. Finally, we will also guide you to build your own agent framework from scratch, giving you the ability to both "use wheels" and "build wheels."

- **Part 3: Advanced Knowledge Extension** (Chapters 8-12), in this part, your agent will "learn" to think and collaborate. We will use the self-developed framework from Part 2 to deeply explore core technologies such as memory and retrieval, context engineering, and Agent training, and learn communication protocols between multi-agents. Finally, you will master professional methods for evaluating agent system performance.

- **Part 4: Comprehensive Case Studies** (Chapters 13-15), this is the intersection of theory and practice. You will integrate what you have learn
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
