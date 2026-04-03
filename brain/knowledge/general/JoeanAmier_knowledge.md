---
id: joeanamier-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:56.174060
---

# KNOWLEDGE EXTRACT: JoeanAmier
> **Extracted on:** 2026-03-30 17:38:12
> **Source:** JoeanAmier

---

## File: `TikTokDownloader.md`
```markdown
# 📦 JoeanAmier/TikTokDownloader [🔖 PENDING/APPROVE]
🔗 https://github.com/JoeanAmier/TikTokDownloader
🌐 https://discord.com/invite/ZYtmgKud9Y

## Meta
- **Stars:** ⭐ 13761 | **Forks:** 🍴 2371
- **Language:** Python | **License:** GPL-3.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
TikTok 发布/喜欢/合辑/直播/视频/图集/音乐；抖音发布/喜欢/收藏/收藏夹/视频/图集/实况/直播/音乐/合集/评论/账号/搜索/热榜数据采集工具/下载工具

## README (trích đầu)
```
<div align="center">
<img src="./static/images/DouK-Downloader.png" alt="DouK-Downloader" height="256" width="256"><br>
<h1>DouK-Downloader</h1>
<p>简体中文 | <a href="README_EN.md">English</a></p>
<a href="https://trendshift.io/repositories/6222" target="_blank"><img src="https://trendshift.io/api/badge/repositories/6222" alt="" style="width: 250px; height: 55px;" width="250" height="55"/></a>
<br>
<img alt="GitHub" src="https://img.shields.io/github/license/JoeanAmier/TikTokDownloader?style=flat-square">
<img alt="GitHub forks" src="https://img.shields.io/github/forks/JoeanAmier/TikTokDownloader?style=flat-square&color=55efc4">
<img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/JoeanAmier/TikTokDownloader?style=flat-square&color=fda7df">
<img alt="GitHub code size in bytes" src="https://img.shields.io/github/languages/code-size/JoeanAmier/TikTokDownloader?style=flat-square&color=a29bfe">
<br>
<img alt="Static Badge" src="https://img.shields.io/badge/Python-3.12-b8e994?style=flat-square&logo=python&labelColor=3dc1d3">
<img alt="GitHub release (with filter)" src="https://img.shields.io/github/v/release/JoeanAmier/TikTokDownloader?style=flat-square&color=48dbfb">
<img src="https://img.shields.io/badge/Sourcery-enabled-884898?style=flat-square&color=1890ff" alt="">
<img alt="Static Badge" src="https://img.shields.io/badge/Docker-badc58?style=flat-square&logo=docker">
<img alt="GitHub all releases" src="https://img.shields.io/github/downloads/JoeanAmier/TikTokDownloader/total?style=flat-square&color=ffdd59">
</div>
<br>
<p>🔥 <b>TikTok 发布/喜欢/合辑/直播/视频/图集/音乐；抖音发布/喜欢/收藏/收藏夹/视频/图集/实况/直播/音乐/合集/评论/账号/搜索/热榜数据采集工具：</b>完全开源，基于 HTTPX 模块实现的免费数据采集和文件下载工具；批量下载抖音账号发布、喜欢、收藏、收藏夹作品；批量下载 TikTok 账号发布、喜欢作品；下载抖音链接或 TikTok 链接作品；获取抖音直播拉流地址；下载抖音直播视频；获取 TikTok 直播拉流地址；下载 TikTok 直播视频；采集抖音作品评论数据；批量下载抖音合集作品；批量下载 TikTok 合辑作品；采集抖音账号详细数据；采集抖音用户 / 作品 / 直播搜索结果；采集抖音热榜数据。</p>
<p>⭐ 本项目历史名称：<code>TikTokDownloader</code></p>
<p>📣 本项目将于未来进行代码结构重构，目标是让代码更加稳健，并具备更好的可维护性与扩展性；如果你对项目设计、实现方式或优化思路有想法，欢迎提出建议或参与讨论！</p>
<hr>

# 📝 项目功能

<details>
<summary>功能列表（点击展开）</summary>
<ul>
<li>✅ 下载抖音视频/图集</li>
<li>✅ 下载抖音实况/动图</li>
<li>✅ 下载最高画质视频文件</li>
<li>✅ 下载 TikTok 视频原画</li>
<li>✅ 下载 TikTok 视频/图集</li>
<li>✅ 下载抖音账号发布/喜欢/收藏/收藏夹作品</li>
<li>✅ 下载 TikTok 账号发布/喜欢作品</li>
<li>✅ 采集抖音 / TikTok 详细数据</li>
<li>✅ 批量下载链接作品</li>
<li>✅ 多账号批量下载作品</li>
<li>✅ 自动跳过已下载的文件</li>
<li>✅ 持久化保存采集数据</li>
<li>✅ 支持 CSV/XLSX/SQLite 格式保存数据</li>
<li>✅ 下载动态/静态封面图</li>
<li>✅ 获取抖音直播拉流地址</li>
<li>✅ 获取 TikTok 直播拉流地址</li>
<li>✅ 调用 ffmpeg 下载直播</li>
<li>✅ Web UI 交互界面</li>
<li>✅ 采集抖音作品评论数据</li>
<li>✅ 下载抖音合集作品</li>
<li>✅ 下载 TikTok 合辑作品</li>
<li>✅ 记录点赞收藏等统计数据</li>
<li>✅ 筛选作品发布时间</li>
<li>✅ 支持账号作品增量下载</li>
<li>✅ 支持使用代理采集数据</li>
<li>✅ 支持局域网远程访问</li>
<li>✅ 采集抖音账号详细数据</li>
<li>✅ 作品统计数据更新</li>
<li>✅ 支持自定义账号/合集标识</li>
<li>✅ 自动更新账号昵称/标识</li>
<li>✅ 部署至私有服务器</li>
<li>✅ 部署至公开服务器</li>
<li>✅ 采集抖音搜索数据</li>
<li>✅ 采集抖音热榜数据</li>
<li>✅ 记录已下载作品 ID</li>
<li>☑️ <del>扫码登陆获取 Cookie</del></li>
<li>✅ 从浏览器读取 Cookie</li>
<li>✅ 支持 Web API 调用</li>
<li>✅ 支持多线程下载作品<
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

