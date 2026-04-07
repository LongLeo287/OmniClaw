---
id: easy-vibe
type: knowledge
owner: OA_Triage
---
# easy-vibe
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "easy-vibe",
  "version": "1.0.0",
  "description": "Easy-Vibe 中文实战课 - 零基础学会用 AI 编程",
  "type": "module",
  "scripts": {
    "dev": "vitepress dev docs",
    "build": "npm run sitemap && vitepress build docs",
    "build:force": "npm run sitemap && vitepress build docs --force",
    "preview": "vitepress preview docs",
    "format": "prettier --write .",
    "verify": "bash scripts/verify.sh",
    "lint": "eslint docs/.vitepress/theme",
    "lint:fix": "eslint docs/.vitepress/theme --fix",
    "prepare": "husky",
    "sitemap": "node scripts/generate-sitemap.mjs"
  },
  "keywords": [
    "easy-vibe",
    "ai",
    "tutorial",
    "vitepress"
  ],
  "engines": {
    "node": ">=18.0.0"
  },
  "license": "CC-BY-NC-SA-4.0",
  "devDependencies": {
    "@eslint/js": "^9.0.0",
    "eslint": "^9.0.0",
    "eslint-plugin-vue": "^9.30.0",
    "husky": "^9.1.7",
    "markdown-it-katex": "^2.0.3",
    "prettier": "^3.7.4",
    "vue-eslint-parser": "^9.4.3"
  },
  "dependencies": {
    "@element-plus/icons-vue": "^2.3.2",
    "claude": "^0.1.1",
    "element-plus": "^2.13.1",
    "mermaid": "^11.13.0",
    "typeit": "^8.8.7",
    "viewerjs": "^1.11.7",
    "vitepress": "^2.0.0-alpha.16",
    "vue": "^3.5.0"
  }
}

```

### File: README.md
```md
<!-- trigger vercel build -->
<div align="center">

<img src="assets/easy-vibe-logo-hd.svg" alt="Easy-Vibe Logo" width="300">

<p align="center" style="font-size: 1.2em; color: #666; margin: 20px 0;">
  Jump right in and vibe together — if you can talk, you can build apps.<br>
  <span style="font-size: 0.9em; color: #888;">直接上手，一起 vibe！会说话就会做应用。</span>
</p>

<a href="https://trendshift.io/repositories/22079" target="_blank"><img src="https://trendshift.io/api/badge/repositories/22079" alt="datawhalechina/easy-vibe | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

<p align="center">
  🚀 <a href="https://datawhalechina.github.io/easy-vibe/welcome.html">Start Exploring</a> · ✨ <a href="https://datawhalechina.github.io/easy-vibe/en/appendix/">Interactive Tutorial</a> · 🦞 <a href="https://github.com/datawhalechina/hello-claw">Learn OpenClaw</a><br>
  <span style="font-size: 0.85em; color: #888;">🚀 <a href="https://datawhalechina.github.io/easy-vibe/welcome.html">开始体验</a> · ✨ <a href="https://datawhalechina.github.io/easy-vibe/zh-cn/appendix/">交互式教程</a> · 🦞 <a href="https://github.com/datawhalechina/hello-claw">学习 OpenClaw</a></span>
</p>

<p align="center">
  <a href="https://datawhalechina.github.io/easy-vibe/welcome.html">Read Online</a> ·
  <a href="#-content-navigation">Learning Map</a> ·
  <a href="#contact">Community</a><br>
  <span style="font-size: 0.85em; color: #888;">
    <a href="https://datawhalechina.github.io/easy-vibe/welcome.html">开始阅读</a> ·
    <a href="#-content-navigation">学习地图</a> ·
    <a href="#contact">社区</a>
  </span>
</p>

<p align="center">
    <a href="https://github.com/datawhalechina/easy-vibe/stargazers" target="_blank">
        <img src="https://img.shields.io/github/stars/datawhalechina/easy-vibe?color=660874&style=for-the-badge&logo=star&logoColor=white&labelColor=1a1a2e" alt="Stars"></a>
    <a href="https://github.com/datawhalechina/easy-vibe/network/members" target="_blank">
        <img src="https://img.shields.io/github/forks/datawhalechina/easy-vibe?color=660874&style=for-the-badge&logo=git-fork&logoColor=white&labelColor=1a1a2e" alt="Forks"></a>
    <a href="LICENSE" target="_blank">
        <img src="https://img.shields.io/badge/License-CC_BY_NC_SA_4.0-4ecdc4?style=for-the-badge&logo=creative-commons&logoColor=white&labelColor=1a1a2e" alt="License"></a>
</p>

<p align="center">
  <a href="README.md"><img alt="English" src="https://img.shields.io/badge/English-d9d9d9"></a>
  <a href="docs-readme/zh-CN/README.md"><img alt="简体中文" src="https://img.shields.io/badge/简体中文-d9d9d9"></a>
  <a href="docs-readme/zh-TW/README.md"><img alt="繁體中文" src="https://img.shields.io/badge/繁體中文-d9d9d9"></a>
  <a href="docs-readme/ja-JP/README.md"><img alt="日本語" src="https://img.shields.io/badge/日本語-d9d9d9"></a>
  <a href="docs-readme/es-ES/README.md"><img alt="Español" src="https://img.shields.io/badge/Español-d9d9d9"></a>
  <a href="docs-readme/fr-FR/README.md"><img alt="Français" src="https://img.shields.io/badge/Français-d9d9d9"></a>
  <a href="docs-readme/ko-KR/README.md"><img alt="한국어" src="https://img.shields.io/badge/한국어-d9d9d9"></a>
  <a href="docs-readme/ar-SA/README.md"><img alt="العربية" src="https://img.shields.io/badge/العربية-d9d9d9"></a>
  <a href="docs-readme/vi-VN/README.md"><img alt="Tiếng_Việt" src="https://img.shields.io/badge/Tiếng_Việt-d9d9d9"></a>
  <a href="docs-readme/de-DE/README.md"><img alt="Deutsch" src="https://img.shields.io/badge/Deutsch-d9d9d9"></a>
</p>

</div>
<table align="center">
  <tr>
    <td width="50%" valign="top" align="center">
      <img src="assets/gif-header.png" width="100%">
      <br>
      <strong>A beginner-friendly learning map</strong>
      <br>
      <sub>Clear guidance from zero, so you can stop "learning and forgetting"</sub>
    </td>
    <td width="50%" valign="top" align="center">
      <img src="assets/gif-tutorial.png" width="100%">
      <br>
      <strong>Step-by-step visual tutorials</strong>
      <br>
      <sub>Detailed walkthroughs that feel like learning with a private tutor</sub>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top" align="center">
      <img src="assets/gif-ide.gif" width="100%">
      <br>
      <strong>Immersive simulated coding</strong>
      <br>
      <sub>Virtual mouse guidance helps you quickly learn the core IDE workflow</sub>
    </td>
    <td width="50%" valign="top" align="center">
      <img src="assets/gif-diffusion.gif" width="100%">
      <br>
      <strong>Visible AI principles</strong>
      <br>
      <sub>Animated explanations make it easy to see how AI generates images</sub>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top" align="center">
      <img src="assets/gif-rag.gif" width="100%">
      <br>
      <strong>Learn RAG like a game</strong>
      <br>
      <sub>Interactive components let you click through the full RAG data flow</sub>
    </td>
    <td width="50%" valign="top" align="center">
      <img src="assets/git-terminal.gif" width="100%">
      <br>
      <strong>Visual terminal concepts</strong>
      <br>
      <sub>Command-line behavior becomes intuitive when the underlying logic is visualized</sub>
    </td>
  </tr>
</table>
<div align="center">
  <h3>⭐ <a href="https://github.com/datawhalechina/easy-vibe" style="color: #d0cd16ff;">Star the repo here</a> to help accelerate updates ❤️</h3>
</div>

<div align="center" style="margin: 30px 0;">
  <a href="https://github.com/datawhalechina/easy-vibe/issues/new?template=story_submission.md">
    <img src="https://raw.githubusercontent.com/datawhalechina/easy-vibe/main/assets/stories_image.png" alt="Share Your Vibe Story" width="80%" style="border-radius: 10px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);">
  </a>
  <p style="margin-top: 15px; font-size: 1.1em; color: #666;">
    📝 <strong>Have your own vibe coding story?</strong> 
    Submit it here and inspire others!
  </p>
</div>

## Why Easy-Vibe

Want an expense tracker? Say it.

Need a booking system with WeChat login? Say it.

Want a blog with comments? Say it.

In the AI era, programming starts by describing what you want.

Easy-Vibe teaches you how to turn that into a real product.


## 🔥 News

- **[2026-03-29]** ✨ **Vibe Stories launched and upgraded with real user journeys**: Added a new homepage Vibe Stories section with an interactive carousel and dedicated story pages, then replaced placeholder content with four real user stories featuring a rural primary school teacher, a college student, a high school IT teacher, and a truck driver who built real products with AI. [👉 View the stories](https://datawhalechina.github.io/easy-vibe/zh-cn/vibe-stories/story-1.html)
- **[2026-03-26]** 🚀 **Major Stage 2 practice update**: Completed the SaaS capstone project "[Your First SaaS Full-Stack App: Copywriting Generator Website](https://datawhalechina.github.io/easy-vibe/en/stage-2/assignments/fullstack-app/)" and substantially expanded the "[How to integrate Stripe and payment systems](https://datawhalechina.github.io/easy-vibe/en/stage-2/backend/stripe-payment/)" section, plus key content around multi-product UI and WeChat Mini Program backend workflows.
- **[2026-03-25]** 📚 **New appendix: User Research and Requirement Validation**: Added four new articles covering idea sourcing, the Double Diamond model, Jobs to Be Done, and The Mom Test to help beginners discover and validate product ideas. [👉 Read the appendix](https://datawhalechina.github.io/easy-vibe/en/appendix/)
- **[2026-03-25]** 📚 **English documentation fully updated**: Stage 2 (Full-stack Development) and Stage 3 (Advanced Development) are now fully available in English. [👉 Start learning](https://datawhalechina.github.io/easy-vibe/en/stage-2/)
<details>
<summary>Past News</summary>

- **[2026-03-02]** 🦞 **OpenClaw and AI Agent friendly support**: Added `llms.txt` so OpenClaw, Claude, Cursor, Trae, and other AI agents can quickly understand the repository structure and find the right tutorial content.
- **[2026-03-01]** The [Advanced Development section](https://datawhalechina.github.io/easy-vibe/en/stage-3/) has been comprehensively upgraded with deep guides for Claude Code, including MCP, Skills, Agent Teams, and more, along with eight cross-platform project tutorials.
- **[2026-02-25]** Updated the [Appendix Knowledge Base](https://datawhalechina.github.io/easy-vibe/en/appendix/), now covering 9 knowledge areas and 80+ interactive topics.
- **[2026-01-27]** Added Android and iOS app development tutorials.
- **[2026-01-19]** Released interactive demos for Prompt Engineering, AI history, authentication design, Git principles, and more.
- **[2026-01-16]** Reorganized the project structure and formally established a beginner entry path.
- **[2026-01-14]** Completed a large update to the Stage 1 product prototyping docs.
- **[2026-01-13]** Refactored the documentation architecture and fully enabled multi-language support.
- **[2026-01-01]** Released the core learning map for the project.
</details>

## Who This Is For

- **Complete beginners**: Build your first project first, then understand how it works
- **Product managers / founders**: Validate ideas fast and build MVPs at low cost
- **Students**: Develop practical skills for the AI era
- **Junior developers**: Learn the full path from idea to launch
- **Mid-level and senior developers**: Upgrade your AI collaboration workflow for complex projects



## Your Learning Paths

### 🎮 I want to try it first (5-minute experience)
**Best for**: Everyone
**What you will learn**: Your first AI coding experience with a Snake mini-game
**What you will get**: Your first AI-built app in 5 minutes

[Start here](https://datawhalechina.github.io/easy-vibe/en/stage-1/)

### 💡 I have an idea I want to build
**Best for**: Beginners / product managers / founders
**What you will learn**: AI IDE tools, requirement breakdown, page design, feature planning, prompting, prototype iteration
**What you will get**: A demoable product prototype

[Start learning](https://datawhalechina.github.io/easy-vibe/en/stage-1/)

### 🚀 I want a structured learning path
**Best for**: Developers / advanced learners
**What you will learn**: Frontend, backend, databases, AI integration, deployment, Claude Code workflow
**What you will get**: The ability to ship a full-stack AI app independently

[Start learning](https://datawhalechina.github.io/easy-vibe/en/stage-2/)

### 🦞 I want to build an AI Agent
**Best for**: Developers interested in AI agents
**What you will learn**: OpenClaw assistant workflows, the Skills system, and automation
**What you will get**: Your own command-line AI assistant

[Learn OpenClaw](https://github.com/datawhalechina/hello-claw)

### 📚 I want to browse reference material
**Best for**: Everyone
**What you will learn**: Computer fundamentals, AI principles, and 9 major knowledge areas
**What you will get**: 80+ interactive reference topics

[Browse the knowledge base](https://datawhalechina.github.io/easy-vibe/en/appendix/)

## Study Suggestions

- If you are a beginner, product manager, or founder, start with [Stage 0 / Stage 1](https://datawhalechina.github.io/easy-vibe/en/stage-1/)
- If you already have development experience, start with [Stage 2](https://datawhalechina.github.io/easy-vibe/en/stage-2/)
- If you want to jump directly into complex projects, go to [Stage 3](https://datawhalechina.github.io/easy-vibe/en/stage-3/)
- If you want to learn AI agents, check out [Hello Claw](https://github.com/datawhalechina/hello-claw)

### 📖 Content Navigation

<div align="center">
  <img src="assets/readme-image1.png" alt="Learning Map" width="70%" style="border-radius: 10px; box-shadow: 0 8px 20px rgba(45,55,72,0.3); margin: 15px 0;"/>
</div>

### I. Beginner Entry

| Section | Key Content |
| :------ | :---------- |
| [Learning Map](https://datawhalechina.github.io/easy-vibe/en/stage-1/learning-map/) | A guided overview of the full learning journey |
| [In the AI era, if you can talk, you can code](https://datawhalechina.github.io/easy-vibe/en/stage-1/ai-capabilities-through-games/) | Get your first feel for AI coding through examples like Snake |
| [Finding great ideas](https://datawhalechina.github.io/easy-vibe/en/stage-1/finding-great-idea/) | Learn how to discover and validate product ideas worth building |
| [Introduction to AI IDE tools](https://datawhalechina.github.io/easy-vibe/en/stage-1/introduction-to-ai-ide/) | Learn to use an IDE and build simple local projects |
| [Build your prototype](https://datawhalechina.github.io/easy-vibe/en/stage-1/building-prototype/) | Move from requirements to single-page and multi-page product prototypes |
| [Add AI capabilities to your prototype](https://datawhalechina.github.io/easy-vibe/en/stage-1/integrating-ai-capabilities/) | Integrate text, image, and video AI features |
| [Complete project practice](https://datawhalechina.github.io/easy-vibe/en/stage-1/complete-project-practice/) | Simulate real scenarios, collect user feedback, and iterate on a full project |

#### Appendix: Product and Business Thinking

| Section | Key Content |
| :------ | :---------- |
| [Product thinking and solution design](https://datawhalechina.github.io/easy-vibe/en/stage-1/appendix-a-product-thinking/) | Core frameworks for going from zero to one with a product |
| [AI industry application scenarios (B2B)](https://datawhalechina.github.io/easy-vibe/en/stage-1/appendix-industry-scenarios/) | Understand how AI is applied across industries |
| [AI consumer product inspiration (B2C)](https://datawhalechina.github.io/easy-vibe/en/stage-1/appendix-c-consumer-scenarios/) | Explore product opportunities in consumer AI |

#### Appendix: Technical Solutions

| Section | Key Content |
| :------ | :---------- |
| [What to do when coding errors happen](https://datawhalechina.github.io/easy-vibe/en/stage-1/appendix-b-common-errors/) | Common vibe coding issues and how to troubleshoot them |
| [Comparison of seven AI coding tools](https://datawhalechina.github.io/easy-vibe/en/stage-1/appendix-articles/example0-1/vibe-coding-tools-snake-game-tutorial) | Compare major AI coding platforms through hands-on testing |
| [Design a website with design and coding agents](https://datawhalechina.github.io/easy-vibe/en/stage-1/appendix-articles/example0-2/vibe-coding-tools-build-website-with-ai-coding-and-design-agents) | Learn multi-agent collaboration in practice |

### II. Junior and Mid-Level Developers

#### Frontend

| Section | Key Content |
| :------ | :---------- |
| [Build your own asset-generation agent starting from Lovart](https://datawhalechina.github.io/easy-vibe/en/stage-2/frontend/lovart-assets/) | Use Nanobanana and Lovart to generate high-quality visual assets and build a drawing agent that understands intent |
| [Getting started with Figma and MasterGo](https://datawhalechina.github.io/easy-vibe/en/stage-2/frontend/figma-mastergo/) | Organize information architecture and page structure with design tools |
| [Build your first mo
... [TRUNCATED]
```

### File: docs\.vitepress\theme\index.js
```js
import DefaultTheme from 'vitepress/theme'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import Viewer from 'viewerjs'
import 'viewerjs/dist/viewer.css'
import TypeIt from 'typeit'
import { onMounted, onBeforeUnmount, watch, nextTick } from 'vue'
import { useRoute, useData } from 'vitepress'
import './style.css'
import Layout from './Layout.vue'
import HomeFeatures from './components/HomeFeatures.vue'
import WelcomeScreen from './components/WelcomeScreen.vue'
import NavGrid from './components/NavGrid.vue'
import NavCard from './components/NavCard.vue'
import CategoryIndex from './components/CategoryIndex.vue'
import ArticleGrid from './components/ArticleGrid.vue'
import RelatedArticlesSection from './components/RelatedArticlesSection.vue'
import StepBar from './components/StepBar.vue'
import ChapterIntroduction from './components/ChapterIntroduction.vue'
import ReadingProgress from './components/ReadingProgress.vue'
import SummaryCard from './components/SummaryCard.vue'
import WebTerminal from './components/appendix/terminal-intro/WebTerminal.vue'
import TerminalGrid from './components/appendix/terminal-intro/TerminalGrid.vue'
import CellInspector from './components/appendix/terminal-intro/CellInspector.vue'
import EscapeSequences from './components/appendix/terminal-intro/EscapeSequences.vue'
import InputVisualizer from './components/appendix/terminal-intro/InputVisualizer.vue'
import SignalsDemo from './components/appendix/terminal-intro/SignalsDemo.vue'
import FlowDiagram from './components/appendix/terminal-intro/FlowDiagram.vue'
import BufferSwitchDemo from './components/appendix/terminal-intro/BufferSwitchDemo.vue'
import AdvancedTUIDemo from './components/appendix/terminal-intro/AdvancedTUIDemo.vue'
import ArchitectureDemo from './components/appendix/terminal-intro/ArchitectureDemo.vue'
import TerminalDefinition from './components/appendix/terminal-intro/TerminalDefinition.vue'
import TerminalOSDemo from './components/appendix/terminal-intro/TerminalOSDemo.vue'
import TerminalHandsOn from './components/appendix/terminal-intro/TerminalHandsOn.vue'

import EscapeParserDemo from './components/appendix/terminal-intro/EscapeParserDemo.vue'
import CookedRawDemo from './components/appendix/terminal-intro/CookedRawDemo.vue'

// API Intro Components
import ApiQuickStartDemo from './components/appendix/api-intro/ApiQuickStartDemo.vue'
import ApiConceptDemo from './components/appendix/api-intro/ApiConceptDemo.vue'
import RequestResponseFlow from './components/appendix/api-intro/RequestResponseFlow.vue'
import ApiMethodDemo from './components/appendix/api-intro/ApiMethodDemo.vue'
import ApiDocumentDemo from './components/appendix/api-intro/ApiDocumentDemo.vue'
import ApiPlayground from './components/appendix/api-intro/ApiPlayground.vue'
import RealWorldApiDemo from './components/appendix/api-intro/RealWorldApiDemo.vue'
import FunctionApiDemo from './components/appendix/api-intro/FunctionApiDemo.vue'
import ApiTypesComparison from './components/appendix/api-intro/ApiTypesComparison.vue'
import ApiFunctionVsHttp from './components/appendix/api-intro/ApiFunctionVsHttp.vue'
import DocumentTypesComparison from './components/appendix/api-intro/DocumentTypesComparison.vue'
import HttpMethodsDemo from './components/appendix/api-intro/HttpMethodsDemo.vue'
import StatusCodeCategories from './components/appendix/api-intro/StatusCodeCategories.vue'

// LLM Intro Components
import EmbeddingDemo from './components/appendix/llm-intro/EmbeddingDemo.vue'
import LinearAttentionDemo from './components/appendix/llm-intro/LinearAttentionDemo.vue'
import LlmQuickStartDemo from './components/appendix/llm-intro/LlmQuickStartDemo.vue'
import MoEDemo from './components/appendix/llm-intro/MoEDemo.vue'
import NextTokenPrediction from './components/appendix/llm-intro/NextTokenPrediction.vue'
import RNNvsTransformer from './components/appendix/llm-intro/RNNvsTransformer.vue'
import ThinkingModelDemo from './components/appendix/llm-intro/ThinkingModelDemo.vue'
import TokenizationDemo from './components/appendix/llm-intro/TokenizationDemo.vue'
import TokenizerToMatrix from './components/appendix/llm-intro/TokenizerToMatrix.vue'
import TrainingInferenceDemo from './components/appendix/llm-intro/TrainingInferenceDemo.vue'

// VLM Intro Components
import AttentionDemo from './components/appendix/vlm-intro/AttentionDemo.vue'
import FeatureAlignmentDemo from './components/appendix/vlm-intro/FeatureAlignmentDemo.vue'
import LinearProjectionDemo from './components/appendix/vlm-intro/LinearProjectionDemo.vue'
import ModelArchitectureComparisonDemo from './components/appendix/vlm-intro/ModelArchitectureComparisonDemo.vue'
import PatchifyDemo from './components/appendix/vlm-intro/PatchifyDemo.vue'
import PositionalEmbeddingDemo from './components/appendix/vlm-intro/PositionalEmbeddingDemo.vue'
import ProjectorDemo from './components/appendix/vlm-intro/ProjectorDemo.vue'
import TrainingPipelineDemo from './components/appendix/vlm-intro/TrainingPipelineDemo.vue'
import VLMInferenceDemo from './components/appendix/vlm-intro/VLMInferenceDemo.vue'
import ViTOutputDemo from './components/appendix/vlm-intro/ViTOutputDemo.vue'
import VlmQuickStartDemo from './components/appendix/vlm-intro/VlmQuickStartDemo.vue'

// Image Gen Intro Components
import ImageGenArchitecture from './components/appendix/image-gen-intro/ImageGenArchitecture.vue'
import LatentSpaceViz from './components/appendix/image-gen-intro/LatentSpaceViz.vue'
import DiffusionProcessDemo from './components/appendix/image-gen-intro/DiffusionProcessDemo.vue'
import FlowMatchingDemo from './components/appendix/image-gen-intro/FlowMatchingDemo.vue'
import PromptVisualizer from './components/appendix/image-gen-intro/PromptVisualizer.vue'
import ImageGenQuickStartDemo from './components/appendix/image-gen-intro/ImageGenQuickStartDemo.vue'

// Audio Intro Components
import AudioWaveformDemo from './components/appendix/audio-intro/AudioWaveformDemo.vue'
import AudioTokenizationDemo from './components/appendix/audio-intro/AudioTokenizationDemo.vue'
import SpectrogramViz from './components/appendix/audio-intro/SpectrogramViz.vue'
import AutoregressiveAudioDemo from './components/appendix/audio-intro/AutoregressiveAudioDemo.vue'
import AudioQuickStartDemo from './components/appendix/audio-intro/AudioQuickStartDemo.vue'
import MelSpectrogramDemo from './components/appendix/audio-intro/MelSpectrogramDemo.vue'
import TTSPipelineDemo from './components/appendix/audio-intro/TTSPipelineDemo.vue'
import VoiceCloningDemo from './components/appendix/audio-intro/VoiceCloningDemo.vue'
import ASRvsTTSDemo from './components/appendix/audio-intro/ASRvsTTSDemo.vue'
import EmotionControlDemo from './components/appendix/audio-intro/EmotionControlDemo.vue'

// Web Basics Components
import WebTechTriad from './components/appendix/web-basics/WebTechTriad.vue'
import UrlToBrowserDemo from './components/appendix/web-basics/UrlToBrowserDemo.vue'
// Git Intro Components
import GitCommitFlow from './components/appendix/git-intro/GitCommitFlow.vue'
import GitBranchVisual from './components/appendix/git-intro/GitBranchVisual.vue'
import GitSyncDemo from './components/appendix/git-intro/GitSyncDemo.vue'
import GitCommandCheatsheet from './components/appendix/git-intro/GitCommandCheatsheet.vue'

// （保留网络相关，未修改）
import NetworkLayers from './components/appendix/web-basics/NetworkLayers.vue'
import TcpUdpComparison from './components/appendix/web-basics/TcpUdpComparison.vue'
import SubnetCalculator from './components/appendix/web-basics/SubnetCalculator.vue'
import NetworkTroubleshooting from './components/appendix/web-basics/NetworkTroubleshooting.vue'

// Computer Fundamentals Components
import TransistorDemo from './components/appendix/computer-fundamentals/TransistorDemo.vue'
import LogicGateDemo from './components/appendix/computer-fundamentals/LogicGateDemo.vue'
import BinaryAdditionRulesDemo from './components/appendix/computer-fundamentals/BinaryAdditionRulesDemo.vue'
import HalfAdderDemo from './components/appendix/computer-fundamentals/HalfAdderDemo.vue'
import FullAdderDemo from './components/appendix/computer-fundamentals/FullAdderDemo.vue'
import AdderDemo from './components/appendix/computer-fundamentals/AdderDemo.vue'
import AdderChainDemo from './components/appendix/computer-fundamentals/AdderChainDemo.vue'
import CompleteAdderDemo from './components/appendix/computer-fundamentals/CompleteAdderDemo.vue'
import FunctionalUnitDemo from './components/appendix/computer-fundamentals/FunctionalUnitDemo.vue'
import CpuArchitectureDemo from './components/appendix/computer-fundamentals/CpuArchitectureDemo.vue'
import MinCpuDemo from './components/appendix/computer-fundamentals/MinCpuDemo.vue'
import RegisterDemo from './components/appendix/computer-fundamentals/RegisterDemo.vue'
import PipelineDemo from './components/appendix/computer-fundamentals/PipelineDemo.vue'
import ControllerDemo from './components/appendix/computer-fundamentals/ControllerDemo.vue'
import BusSystemDemo from './components/appendix/computer-fundamentals/BusSystemDemo.vue'
import InstructionFormatDemo from './components/appendix/computer-fundamentals/InstructionFormatDemo.vue'
import AddressingModeDemo from './components/appendix/computer-fundamentals/AddressingModeDemo.vue'
import CacheDemo from './components/appendix/computer-fundamentals/CacheDemo.vue'
import IOMethodDemo from './components/appendix/computer-fundamentals/IOMethodDemo.vue'
import PSWFlagDemo from './components/appendix/computer-fundamentals/PSWFlagDemo.vue'
import FlipFlopDemo from './components/appendix/computer-fundamentals/FlipFlopDemo.vue'
// import EvolutionFlowDemo from './components/appendix/computer-fundamentals/EvolutionFlowDemo.vue'
import ProcessDemo from './components/appendix/computer-fundamentals/ProcessDemo.vue'
import MemoryDemo from './components/appendix/computer-fundamentals/MemoryDemo.vue'
import FilesystemDemo from './components/appendix/computer-fundamentals/FilesystemDemo.vue'
import EncodingDemo from './components/appendix/computer-fundamentals/EncodingDemo.vue'
import StorageDemo from './components/appendix/computer-fundamentals/StorageDemo.vue'
import TransmissionDemo from './components/appendix/computer-fundamentals/TransmissionDemo.vue'
import DataStructureDemo from './components/appendix/computer-fundamentals/DataStructureDemo.vue'
import AlgorithmDemo from './components/appendix/computer-fundamentals/AlgorithmDemo.vue'
import LanguageMapDemo from './components/appendix/computer-fundamentals/LanguageMapDemo.vue'
import TypeSystemDemo from './components/appendix/computer-fundamentals/TypeSystemDemo.vue'
import CompilerDemo from './components/appendix/computer-fundamentals/CompilerDemo.vue'
import StaticVsDynamicDemo from './components/appendix/computer-fundamentals/StaticVsDynamicDemo.vue'
import StrongVsWeakDemo from './components/appendix/computer-fundamentals/StrongVsWeakDemo.vue'
import TypeInferenceFlowDemo from './components/appendix/computer-fundamentals/TypeInferenceFlowDemo.vue'
import LexerTokenDemo from './components/appendix/computer-fundamentals/LexerTokenDemo.vue'
import CompileVsInterpretDemo from './components/appendix/computer-fundamentals/CompileVsInterpretDemo.vue'
import CodeToInstructionDemo from './components/appendix/computer-fundamentals/CodeToInstructionDemo.vue'
import CISCvsRISCDemo from './components/appendix/computer-fundamentals/CISCvsRISCDemo.vue'
import TypeSafetyPracticeDemo from './components/appendix/computer-fundamentals/TypeSafetyPracticeDemo.vue'
import GenericTypeDemo from './components/appendix/computer-fundamentals/GenericTypeDemo.vue'
import ASTVisualizerDemo from './components/appendix/computer-fundamentals/ASTVisualizerDemo.vue'
import CodeOptimizationDemo from './components/appendix/computer-fundamentals/CodeOptimizationDemo.vue'
import CFNetworkLayers from './components/appendix/computer-fundamentals/NetworkLayers.vue'
import CFSubnetCalculator from './components/appendix/computer-fundamentals/SubnetCalculator.vue'
import CFTcpUdpComparison from './components/appendix/computer-fundamentals/TcpUdpComparison.vue'

// Computer Fundamentals Additional Components
import OSArchitectureDemo from './components/appendix/computer-fundamentals/OSArchitectureDemo.vue'
import ProgramLaunchDemo from './components/appendix/computer-fundamentals/ProgramLaunchDemo.vue'
import DataLifecycleDemo from './components/appendix/computer-fundamentals/DataLifecycleDemo.vue'
import EncodingStorageTransmissionDemo from './components/appendix/computer-fundamentals/EncodingStorageTransmissionDemo.vue'
import NetworkOverviewDemo from './components/appendix/computer-fundamentals/NetworkOverviewDemo.vue'
import PhysicalLayerDemo from './components/appendix/computer-fundamentals/PhysicalLayerDemo.vue'
import DataLinkLayerDemo from './components/appendix/computer-fundamentals/DataLinkLayerDemo.vue'
import TransportLayerDemo from './components/appendix/computer-fundamentals/TransportLayerDemo.vue'
import ApplicationLayerDemo from './components/appendix/computer-fundamentals/ApplicationLayerDemo.vue'
import DataStructureOverviewDemo from './components/appendix/computer-fundamentals/DataStructureOverviewDemo.vue'
import LinearStructuresDemo from './components/appendix/computer-fundamentals/LinearStructuresDemo.vue'
import HashTableDemo from './components/appendix/computer-fundamentals/HashTableDemo.vue'
import TreeStructureDemo from './components/appendix/computer-fundamentals/TreeStructureDemo.vue'
import DataStructureSelectorDemo from './components/appendix/computer-fundamentals/DataStructureSelectorDemo.vue'
import AlgorithmOverviewDemo from './components/appendix/computer-fundamentals/AlgorithmOverviewDemo.vue'
import RecursiveThinkingDemo from './components/appendix/computer-fundamentals/RecursiveThinkingDemo.vue'
import GreedyThinkingDemo from './components/appendix/computer-fundamentals/GreedyThinkingDemo.vue'
import AlgorithmParadigmDemo from './components/appendix/computer-fundamentals/AlgorithmParadigmDemo.vue'
import LanguageEvolutionDemo from './components/appendix/computer-fundamentals/LanguageEvolutionDemo.vue'
import ProgrammingParadigmDemo from './components/appendix/computer-fundamentals/ProgrammingParadigmDemo.vue'
import LanguageScenarioDemo from './components/appendix/computer-fundamentals/LanguageScenarioDemo.vue'
import ProgrammingLanguageComparisonDemo from './components/appendix/computer-fundamentals/ProgrammingLanguageComparisonDemo.vue'
import CompilerAnalogyDemo from './components/appendix/computer-fundamentals/CompilerAnalogyDemo.vue'
import SearchAlgorithmDemo from './components/appendix/computer-fundamentals/SearchAlgorithmDemo.vue'
import SortingAlgorithmDemo from './components/appendix/computer-fundamentals/SortingAlgorithmDemo.vue'
import NetworkPrincipleDemo from './components/appendix/computer-fundamentals/NetworkPrincipleDemo.vue'
import DataEncodingBasicsDemo from './components/appendix/computer-fu
... [TRUNCATED]
```

### File: docs\.vitepress\theme\locales\ai-history\index.js
```js
import zhCn from './zh-cn.js'
import en from './en.js'

export const aiHistoryLocale = {
  'zh-cn': zhCn,
  en
}

```

### File: docs\.vitepress\theme\locales\chapter-introduction\index.js
```js
export default {
  'zh-cn': {
    title: '本章学习目标',
    duration: '预计耗时',
    output: '预期产出',
    assignment: '课后任务'
  },
  en: {
    title: 'Learning Objectives',
    duration: 'Estimated Time',
    output: 'Expected Output',
    assignment: 'Assignment'
  }
}

```

### File: docs\.vitepress\theme\components\appendix\frontend-routing\index.js
```js
// Frontend Routing Components
export { default as RoutingModesDemo } from './RoutingModesDemo.vue'
export { default as HashVsHistoryDemo } from './HashVsHistoryDemo.vue'
export { default as RouteMatchingDemo } from './RouteMatchingDemo.vue'
export { default as NestedRoutesDemo } from './NestedRoutesDemo.vue'
export { default as DynamicRoutesDemo } from './DynamicRoutesDemo.vue'
export { default as RouteGuardsDemo } from './RouteGuardsDemo.vue'
export { default as SpaNavigationDemo } from './SpaNavigationDemo.vue'
export { default as MpaRoutingDemo } from './MpaRoutingDemo.vue'
export { default as RouterArchitectureDemo } from './RouterArchitectureDemo.vue'

```

### File: docs\.vitepress\theme\components\appendix\terminal-intro\README.md
```md
# Terminal Intro Components

此目录包含 `docs/zh-cn/appendix/terminal-intro.md`（终端原理附录）页面使用的所有交互式 Vue 组件。

这些组件旨在通过可视化和互动的方式，帮助读者理解终端的工作原理、ANSI 转义序列、Shell 交互等概念。

## 组件列表

| 组件名                     | 描述                                                                                  | 对应文档章节     |
| :------------------------- | :------------------------------------------------------------------------------------ | :--------------- |
| **TerminalDefinition.vue** | 可视化终端作为“字符流输入/输出环境”的定义。展示键盘输入 -> 字符流 -> 屏幕输出的过程。 | 1. 概念界定      |
| **ArchitectureDemo.vue**   | 演示终端（前端）与 Shell（后端）的分离架构。模拟点餐流程类比。                        | 2. 核心架构      |
| **TerminalGrid.vue**       | 展示终端的字符网格系统，演示行、列和单元格的概念。                                    | 3. 视觉模型      |
| **CellInspector.vue**      | 单元格检查器，展示每个字符单元格背后的属性（字符、前景色、背景色等）。                | 3.2 样式检查     |
| **EscapeSequences.vue**    | 演示 ANSI 转义序列如何控制颜色、样式、光标移动和清屏。                                | 4. 通信协议      |
| **InputVisualizer.vue**    | 可视化键盘按键如何转换为字节序列发送给 Shell。                                        | 5. 输入机制      |
| **WebTerminal.vue**        | 一个功能较完整的模拟终端，支持 `ls`, `cd`, `cat`, `apt` 等命令，包含虚拟文件系统。    | 附录/综合演示    |
| **SignalsDemo.vue**        | 演示终端信号（如 Ctrl+C SIGINT）的工作机制。                                          | (文档中可能引用) |
| **FlowDiagram.vue**        | 展示标准输入/输出/错误流 (stdin/stdout/stderr) 的流向图。                             | (文档中可能引用) |
| **AdvancedTUIDemo.vue**    | 展示基于文本的用户界面 (TUI) 的高级布局能力（如面板、进度条）。                       | (文档中可能引用) |

## 开发指南

### 技术栈

- **Vue 3**: 使用 `<script setup>` 语法。
- **Styling**: Scoped CSS，主要使用 Flexbox 和 Grid 布局。
- **Theme**: 统一使用黑色系背景 (`#09090b`, `#18181b`) 和 JetBrains Mono 字体，保持类似终端的视觉风格。

### 维护注意事项

1.  **双语支持**: 组件内部文本尽量支持中英双语，或通过 Props 传入文本。目前部分组件已硬编码双语标签。
2.  **自包含**: 组件应尽量自包含，不依赖外部复杂的 Store 或 Context，以便于在 Markdown 中直接使用。
3.  **响应式**: 考虑移动端适配，通常使用 `@media (max-width: 768px)` 进行布局调整。

### 常用颜色变量 (参考)

- 背景: `#09090b` (Main), `#18181b` (Panel)
- 边框: `#27272a`
- 文本: `#e4e4e7` (Primary), `#a1a1aa` (Secondary)
- 强调色: `#22c55e` (Green/Success), `#facc15` (Yellow/Warning), `#22d3ee` (Cyan/Info)

## 目录结构

所有组件均位于 `docs/.vitepress/theme/components/appendix/terminal-intro/` 下。
注册逻辑位于 `docs/.vitepress/theme/index.js`。

```

### File: AGENTS.md
```md
# Repository Guidelines

## Project Structure & Module Organization

- `docs/`: VitePress site source (Markdown content, sidebar/nav, assets referenced by docs).
- `docs/.vitepress/theme/`: custom theme, global component registration in `index.js`, shared styles in `style.css`, layout in `Layout.vue`.
- `docs/.vitepress/theme/components/appendix/*/`: interactive Vue demos used inside appendix pages (e.g. `web-basics/`, `deployment/`).
- `assets/`: repo-level images/media (if referenced, prefer linking/copying into `docs/public/` or a doc-local folder when appropriate).
- `scripts/`, `tools/`, `update_readmes.cjs`: utility scripts for maintaining docs.

## Build, Test, and Development Commands

This repo is a VitePress (Vue 3) documentation project. Requires Node.js **>= 18**.

```bash
npm install
npm run dev      # start local docs server (hot reload)
npm run build    # production build (use as CI-style check)
npm run preview  # preview the built site locally
npm run format   # run Prettier on the whole repo
```

## Coding Style & Naming Conventions

- Formatting: Prettier (`npm run format`). Keep diffs small and avoid reformatting unrelated files.
- Vue components: Vue 3 SFCs with `<script setup>`, PascalCase filenames (e.g. `SemanticTagsDemo.vue`).
- CSS: prefer VitePress theme variables (`var(--vp-c-*)`) and keep components responsive (`@media (max-width: 720px)` when needed).
- Docs: use clear headings and short paragraphs; components are referenced in Markdown as `<ComponentName />`.

## Testing Guidelines

There is no dedicated test framework in this repo. Use `npm run build` as the primary correctness check, and manually verify interactive components in `npm run dev`.

## Commit & Pull Request Guidelines

- Commits follow a Conventional Commits style seen in history: `feat: ...`, `fix: ...`, `docs: ...` (optionally scoped like `feat(docs): ...`).
- PRs should include: a short description, screenshots/GIFs for UI or component changes, and any relevant paths touched (e.g. `docs/zh-cn/appendix/...`, `docs/.vitepress/theme/...`).

## Configuration & Deployment Notes

- `vercel.json` is present; keep builds reproducible and avoid relying on local-only assets.

```

### File: CLAUDE.md
```md
# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Easy-Vibe** is an educational curriculum for learning AI Vibe Coding from zero to advanced levels. It's a documentation-based project using **VitePress** to serve educational content about AI-assisted software development.

The curriculum follows a progressive four-stage structure:

- **Stage 0 (幼儿园)**: Introduction to AI programming through games
- **Stage 1 (AI 产品经理)**: Building AI-powered web application prototypes
- **Stage 2 (初中级开发工程师)**: Full-stack development with databases and deployment
- **Stage 3 (高级开发工程师)**: Cross-platform development (WeChat mini-programs, Android apps, MCP)

## Development Commands

### Start Local Documentation Server

```bash
npm install      # Install dependencies (first time only)
npm run dev      # Start VitePress dev server
```

The documentation will be available at `http://localhost:5173` (VitePress default port)

### Build/Run Commands

- `npm run dev` - Start VitePress development server with hot reload
- `npm run build` - Build static site for production (outputs to `docs/.vitepress/dist`)
- `npm run preview` - Preview production build locally
- `npm run format` - Format code using Prettier

### Node Version Requirement

- Node.js >= 18.0.0 required (specified in package.json `engines`)

## Project Architecture

### VitePress Base Path Configuration

The site automatically configures its base path based on the deployment environment:

- **Vercel**: Uses `/` as base (detected via `VERCEL` environment variable)
- **GitHub Pages / Local**: Uses `/easy-vibe/` as base

This logic is in `docs/.vitepress/config.mjs:3-5`. When linking assets or configuring paths, the `${base}` variable is used to ensure compatibility across environments.

### Directory Structure

```
easy-vibe/
├── docs/                        # Main documentation content (served by VitePress)
│   ├── .vitepress/             # VitePress configuration and theme
│   │   ├── config.mjs          # Site configuration (nav, sidebar, plugins)
│   │   ├── theme/              # Custom theme extensions
│   │   │   ├── Layout.vue      # Override default layout with typewriter effect
│   │   │   ├── index.js        # Theme setup (Viewer.js, TypeIt, image optimization)
│   │   │   └── style.css       # Custom CSS overrides
│   │   ├── dist/               # Production build output (generated)
│   │   └── cache/              # VitePress cache (generated)
│   ├── index.md                # Homepage
│   ├── public/                 # Static assets (logo.png, etc.)
│   ├── assets/                 # Symlink to ../assets
│   ├── stage-1/                # Stage 1 content (AI 产品经理)
│   ├── stage-2/                # Stage 2 content (初中级开发工程师)
│   ├── stage-3/                # Stage 3 content (高级开发工程师)
│   ├── appendix/               # Reference materials (AI capability dictionary)
│   ├── examples/               # Practical examples and tutorials (legacy)
│   ├── extra/                  # Additional knowledge (Git, API, RAG, etc.)
│   ├── guide/                  # Course guide
│   └── project/                # Legacy project documentation
├── assets/                     # Images and static assets
├── package.json                # Project dependencies and scripts
├── vercel.json                 # Vercel deployment configuration
└── README.md                   # Project overview and contribution guide
```

### Content Organization

Each stage follows a numbered chapter structure:

```
stage-{N}/
└── {category or chapter-dir}/
    └── index.md          # Main content file (or .md file directly)
```

Examples:

- `stage-1/introduction-to-ai-ide/index.md`
- `stage-2/backend/what-is-api/extra2/extra2-what-is-api.md`

**Note**: Content files may use either `index.md` or direct `.md` files depending on the chapter structure.

### Documentation System (VitePress)

The project uses **VitePress 2.0.0-alpha.15** with these key features:

**Configuration** (`docs/.vitepress/config.mjs`):

- **Single Sidebar**: Route-based sidebars configured per path prefix (`/stage-1/`, etc.)
- **Navigation**: Top nav with links to each stage and appendix
- **Search**: Local search via `minisearch` (no external API required)
- **Dark Mode**: Built-in VitePress theme with toggle

**Custom Theme** (`docs/.vitepress/theme/`):

- **Image Viewer**: Viewer.js integration for zoom/rotate/flip on all images
- **Typewriter Effect**: TypeIt.js for homepage hero tagline animation
- **Image Optimization**: Automatic image height classes based on aspect ratio
- **Custom Layout**: Extends default theme with `Layout.vue` override
- **Reading Settings**: Element Plus popover panel for adjusting font size (12-18px) and line height (1.25-1.8) with localStorage persistence

**Key Theme Behaviors**:

- Images with aspect ratio > 1.2 get height-limited classes (tall/very-tall/ultra-tall)
- Viewer.js initialized on `.vp-doc` container on each route change
- Typewriter effect only activates on homepage when `frontmatter.hero.tagline` is an array
- Font size/line height adjustments use CSS custom properties `--ev-doc-font-size` and `--ev-doc-line-height`
- Reading settings panel appears in nav bar after the search/home buttons (gear icon)

### Sidebar Management

The sidebar is defined in `docs/.vitepress/config.mjs`. When adding new chapters:

1. Locate the appropriate route prefix section (`/stage-1/`, etc.)
2. Add a new object with `text` (display name) and `link` (relative path)
3. For nested items, use `items` array with `collapsed: true|false`
4. **Links should not include `.md` extension** - VitePress handles this
5. Links should not include `index` - use directory path with trailing slash

Example pattern:

```javascript
{
  text: 'Chapter Title',
  link: '/stage-1/chapter-directory/'  // Note: trailing slash, no .md
}
```

### Asset Management

- Root-level static assets are in `/assets/` at project root
- Public files (favicon, logo) go in `docs/public/`
- Images are referenced with relative paths from markdown file location
- VitePress serves `docs/assets` as symlink to `../assets`
- Image optimization is automatic via theme (height-limited classes based on aspect ratio)

### Deployment

**Vercel** (vercel.json):

- Build command: `npm run build`
- Output directory: `docs/.vitepress/dist`
- Framework: vitepress

**Preview Production Build**:

```bash
npm run build
npm run preview  # Preview built site locally
```

### Legacy Content Structure

The project maintains three legacy sections for backward compatibility:

1. **Project 文档** (`project/`): Older chapter-based tutorials (migrated to Stage 2)
2. **Extra 扩展知识** (`extra/`): Supplementary topics - Git, APIs, RAG, deployment (migrated to Stage 2/3)
3. **Examples 实战案例** (`examples/`): Practical tutorials (migrated to Stage 0/3)

When updating content, prefer integrating into the stage structure over adding to legacy sections.

## Content Guidelines

### Writing New Chapters

1. Create directory: `docs/stage-{N}/{chapter-directory}/`
2. Create `index.md` or direct `.md` file with chapter content
3. Update `docs/.vitepress/config.mjs` sidebar with the new entry
4. Follow Chinese language conventions (this is a Chinese curriculum)

### Content Status Markers

In README.md, use these status indicators:

- ✅ Completed
- 🚧 In progress/Under construction

### File Naming Conventions

- Use kebab-case for directories: `1.1-introduction-to-ai-ide`, `frontend`, `backend`
- Content can be either `index.md` in a directory or a direct `.md` file
- Images use descriptive names; can be in chapter subdirectories or root `/assets/`

### Code Formatting

Prettier configuration (`.prettierrc`):

- No semicolons (`semi: false`)
- Single quotes (`singleQuote: true`)
- No trailing commas (`trailingComma: "none"`)

Run `npm run format` before committing code changes.

## Interactive Vue Components

### Component Registration

All interactive Vue components for the documentation are registered in `docs/.vitepress/theme/index.js`. To add a new component:

1. Create the `.vue` file in the appropriate subdirectory of `docs/.vitepress/theme/components/`
2. Import the component in `docs/.vitepress/theme/index.js`
3. Register the component using `app.component('ComponentName', ComponentName)` in the `enhanceApp` function

### Component Categories

Components are organized by topic:

- `appendix/llm-intro/` - Large Language Model interactive demos
- `appendix/vlm-intro/` - Vision Language Model interactive demos
- `appendix/git-intro/` - Git workflow visualizations
- `appendix/terminal-intro/` - Terminal/CLI interactive demos
- `appendix/web-basics/` - HTML/CSS/JavaScript fundamentals
- `appendix/auth-design/` - Authentication/authorization demos
- `appendix/cache-design/` - Caching strategy visualizations
- `appendix/database-intro/` - Database fundamentals
- `appendix/queue-design/` - Message queue demos
- `appendix/operations/` - DevOps/monitoring demos
- `appendix/deployment/` - Deployment architecture demos
- `appendix/frontend-performance/` - Frontend performance demos
- `appendix/frontend-evolution/` - Frontend history/evolution demos
- `appendix/backend-evolution/` - Backend architecture evolution
- `appendix/backend-languages/` - Backend language comparisons

### Using Components in Markdown

Components can be used directly in markdown files:

```markdown
## LLM Basics

<LLMQuickStartDemo />

### Tokenization

<TokenizationDemo />
```

### Component Development Best Practices

1. **Props**: Use props for configurable demo parameters
2. **Styling**: Use scoped CSS or Tailwind-like utility classes
3. **Responsiveness**: Ensure components work on mobile and desktop
4. **Accessibility**: Include aria labels where appropriate
5. **i18n**: Keep text content minimal or use props for text

## Multi-language Support

### Supported Locales

The project supports 13 languages:

- `zh-cn` - Simplified Chinese (primary)
- `zh-tw` - Traditional Chinese
- `en-us` - English (US)
- `ja-jp` - Japanese
- `ko-kr` - Korean
- `es-es` - Spanish
- `fr-fr` - French
- `de-de` - German
- `ar-sa` - Arabic
- `vi-vn` - Vietnamese

### Adding Multi-language Content

1. Create content in `docs/{locale}/` following the same structure as `docs/zh-cn/`
2. Add locale configuration in `docs/.vitepress/config.mjs` under `locales`
3. Copy the sidebar structure from `zh-cn` and translate the text values

### Content Translation Priority

1. **Primary**: `zh-cn` (Simplified Chinese) - always complete this first
2. **Secondary**: `en-us` (English) - for international reach
3. **Tertiary**: Other languages based on contributor availability

## Permissions

The project has configured bash permissions in `.claude/settings.local.json`:

- File operations: `which`, `find`, `mv`, `tree`, `cat`, `curl`, `lsof`, `mkdir`, `cp`, `ls`
- Process management: `xargs ps`, `kill`
- Development: `npm run dev`, `npm run build`, `npm run preview`, `npm run format`

## Key Context for Development

- **Educational Focus**: This is curriculum content, not application code
- **Target Audience**: Beginners to advanced developers learning AI-assisted programming
- **Language**: Primary content is in Chinese
- **Build Pipeline**: VitePress requires build step for production (`npm run build`)
- **Git Workflow**: Content changes should preserve formatting and structure
- **Asset Paths**: Always use relative paths from markdown file location

When making changes:

- Preserve the VitePress configuration in `docs/.vitepress/config.mjs`
- Maintain sidebar structure consistency in config.mjs
- Test locally with `npm run dev` before committing
- Check that image links work correctly
- Ensure theme customizations in `.vitepress/theme/` are not broken
- Run `npm run format` before committing code changes (uses Prettier: no semicolons, single quotes)

```

### File: eslint.config.js
```js
import js from '@eslint/js'
import pluginVue from 'eslint-plugin-vue'
import vueParser from 'vue-eslint-parser'

export default [
  {
    ignores: [
      'node_modules/**',
      'docs/.vitepress/dist/**',
      'docs/.vitepress/cache/**'
    ]
  },
  js.configs.recommended,
  ...pluginVue.configs['flat/recommended'],
  {
    files: ['**/*.vue', '**/*.js', '**/*.ts'],
    languageOptions: {
      parser: vueParser,
      parserOptions: {
        ecmaVersion: 'latest',
        sourceType: 'module',
        ecmaFeatures: {
          jsx: false
        }
      }
    },
    rules: {
      // Important Vue rules - keep as errors
      'vue/no-ref-as-operand': 'error',
      'vue/no-template-shadow': 'error',
      'vue/require-v-for-key': 'error',
      'vue/no-use-v-if-with-v-for': 'error',
      'vue/no-mutating-props': 'error',
      'vue/return-in-computed-property': 'error',
      'vue/no-side-effects-in-computed-properties': 'error',
      'vue/no-async-in-computed-properties': 'error',
      'no-undef': 'error',

      // Relaxed rules - warnings or off
      'vue/no-setup-props-destructure': 'warn',
      'vue/require-valid-default-prop': 'off',
      'no-unused-vars': 'warn',

      // Disable formatting rules (handled by Prettier)
      'vue/max-attributes-per-line': 'off',
      'vue/singleline-html-element-content-newline': 'off',
      'vue/html-self-closing': 'off',
      'vue/html-indent': 'off',
      'vue/multiline-html-element-content-newline': 'off',
      'vue/first-attribute-linebreak': 'off',

      // Other Vue rules
      'vue/multi-word-component-names': 'off',
      'vue/no-v-html': 'off', // v-html is common in docs
      'no-case-declarations': 'off', // Too strict for demo code
      'no-control-regex': 'off', // Terminal codes need this
      'no-useless-escape': 'warn', // Sometimes needed for clarity
      'no-dupe-keys': 'error', // Real issue
      'no-prototype-builtins': 'warn', // Common in demo code
      'no-dupe-else-if': 'warn', // Sometimes intentional
      'no-async-promise-executor': 'warn' // Common pattern in demo code
    }
  }
]

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
