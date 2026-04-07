---
id: tiktokdownloader
type: knowledge
owner: OA_Triage
---
# tiktokdownloader
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: main.py
```py
from asyncio import CancelledError
from asyncio import run

from src.application import TikTokDownloader


async def main():
    async with TikTokDownloader() as downloader:
        try:
            await downloader.run()
        except (
                KeyboardInterrupt,
                CancelledError,
        ):
            return


if __name__ == "__main__":
    run(main())

```

### File: README.md
```md
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
<li>✅ 支持多线程下载作品</li>
<li>✅ 文件完整性处理机制</li>
<li>✅ 自定义规则筛选作品</li>
<li>✅ 按文件夹归档保存作品文件</li>
<li>✅ 自定义设置文件大小上限</li>
<li>✅ 支持文件断点续传下载</li>
<li>✅ 监听剪贴板链接下载作品</li>
</ul>
</details>

# 💻 程序截图

<p><a href="https://www.bilibili.com/video/BV1d7eAzTEFs/">前往 bilibili 观看演示</a>；<a href="https://youtu.be/yMU-RWl55hg">前往 YouTube 观看演示</a></p>

## 终端交互模式

<p>建议通过配置文件管理账号，更多介绍请查阅 <a href="https://github.com/JoeanAmier/TikTokDownloader/wiki/Documentation">文档</a></p>

![终端模式截图](docs/screenshot/终端交互模式截图CN1.png)
*****
![终端模式截图](docs/screenshot/终端交互模式截图CN2.png)
*****
![终端模式截图](docs/screenshot/终端交互模式截图CN3.png)

## Web UI 交互模式

> **项目代码已重构，该模式代码尚未更新，未来开发完成重新开放！**

## Web API 接口模式

![WebAPI模式截图](docs/screenshot/WebAPI模式截图CN1.png)
*****
![WebAPI模式截图](docs/screenshot/WebAPI模式截图CN2.png)

> **启动该模式后，访问 `http://127.0.0.1:5555/docs` 或者 `http://127.0.0.1:5555/redoc` 可以查阅自动生成的文档！**

### API 调用示例代码

```python
from httpx import post
from rich import print


def demo():
    headers = {"token": ""}
    data = {
        "detail_id": "0123456789",
        "pages": 2,
    }
    api = "http://127.0.0.1:5555/douyin/comment"
    response = post(api, json=data, headers=headers)
    print(response.json())


demo()
```

# 📋 项目说明

## 快速入门

<p>⭐ Mac OS、Windows 10 及以上用户可前往 <a href="https://github.com/JoeanAmier/TikTokDownloader/releases/latest">Releases</a> 或者 <a href="https://github.com/JoeanAmier/TikTokDownloader/actions">Actions</a> 下载已编译的程序，开箱即用！</p>
<p>⭐ 本项目包含自动构建可执行文件的 GitHub Actions，使用者可以随时使用 GitHub Actions 将最新源码构建为可执行文件！</p>
<p>⭐ 自动构建可执行文件教程请查阅本文档的 <code>构建可执行文件指南</code> 部分；如果需要更加详细的图文教程，请 <a href="https://mp.weixin.qq.com/s/TorfoZKkf4-x8IBNLImNuw">查阅文章</a>！</p>
<p><strong>注意：由于 Mac OS 平台的可执行文件 <code>main</code> 未经过代码签名，首次运行时会受到系统安全限制。请先在终端执行 <code>xattr -cr 项目文件夹路径</code> 命令移除安全标记，执行一次后即可正常运行。</strong></p>
<hr>
<ol>
<li><b>运行可执行文件</b> 或者 <b>配置环境运行</b>（二选一）
<ol><b>运行可执行文件</b>
<li>下载 <a href="https://github.com/JoeanAmier/TikTokDownloader/releases/latest">Releases</a> 或者 Actions 构建的可执行文件压缩包</li>
<li>解压后打开程序文件夹，双击运行 <code>main</code></li>
</ol>
<ol><b>配置环境运行</b>

[//]: # (<li>安装不低于 <code>3.12</code> 版本的 <a href="https://www.python.org/">Python</a> 解释器</li>)
<li>安装 <code>3.12</code> 版本的 <a href="https://www.python.org/">Python</a> 解释器</li>
<li>下载最新的源码或 <a href="https://github.com/JoeanAmier/TikTokDownloader/releases/latest">Releases</a> 发布的源码至本地</li>
<ol><b>使用 pip 安装项目依赖</b>
<li>运行 <code>python -m venv venv</code> 命令创建虚拟环境（可选）</li>
<li>运行 <code>.\venv\Scripts\activate.ps1</code> 或者 <code>venv\Scripts\activate</code> 命令激活虚拟环境（可选）</li>
<li>运行 <code>pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt</code> 命令安装程序所需模块</li>
<li>运行 <code>python .\main.py</code> 或者 <code>python main.py</code> 命令启动 DouK-Downloader</li>
</ol>
<ol><b>使用 uv 安装项目依赖（推荐）</b>
<li>运行 <code>uv sync --no-dev</code> 命令同步环境依赖</li>
<li>运行 <code>uv run main.py</code> 命令启动 DouK-Downloader</li>
</ol>
</ol>
</li>
<li>阅读 DouK-Downloader 的免责声明，根据提示输入内容</li>
<li>将 Cookie 信息写入配置文件
<ol><b>从剪贴板读取 Cookie（推荐）</b>
<li>参考 <a href="https://github.com/JoeanAmier/TikTokDownloader/blob/master/docs/Cookie%E8%8E%B7%E5%8F%96%E6%95%99%E7%A8%8B.md">Cookie 提取教程</a>，复制所需 Cookie 至剪贴板</li>
<li>选择 <code>从剪贴板读取 Cookie</code> 选项，程序会自动读取剪贴板的 Cookie 并写入配置文件</li>
</ol>
<ol><b>从浏览器读取 Cookie</b>
<li>选择 <code>从浏览器读取 Cookie</code> 选项，按照提示输入浏览器类型或序号</li>
</ol>
<ol><b><del>扫码登录获取 Cookie</del>（失效）</b>
<li><del>选择 <code>扫码登录获取 Cookie</code> 选项，程序会显示登录二维码图片，并使用默认应用打开图片</del></li>
<li><del>使用抖音 APP 扫描二维码并登录账号</del></li>
<li><del>按照提示操作，程序会自动将 Cookie 写入配置文件</del></li>
</ol>
</li>
<li>返回程序界面，依次选择 <code>终端交互模式</code> -> <code>批量下载链接作品(通用)</code> -> <code>手动输入待采集的作品链接</code></li>
<li>输入抖音作品链接即可下载作品文件（TikTok 平台需要更多初始设置，详见文档）</li>
<li>更多详细说明请查看 <b><a href="https://github.com/JoeanAmier/TikTokDownloader/wiki/Documentation">项目文档</a></b></li>
</ol>
<p>⭐ 推荐使用 <a href="https://learn.microsoft.com/zh-cn/windows/terminal/install">Windows 终端</a>（Windows 11 自带默认终端）</p>

### Docker 容器

<ol>
<li>获取镜像</li>
<ul>
<li>方式一：使用 <code>Dockerfile</code> 文件构建镜像</li>
<li>方式二：使用 <code>docker pull joeanamier/tiktok-downloader</code> 命令拉取镜像</li>
<li>方式三：使用 <code>docker pull ghcr.io/joeanamier/tiktok-downloader</code> 命令拉取镜像</li>
</ul>
<li>创建容器：<code>docker run --name 容器名称(可选) -p 主机端口号:5555 -v tiktok_downloader_volume:/app/Volume -it &lt;镜像名称&gt;</code>
</li>
<br><b>注意：</b>此处的 <code>&lt;镜像名称&gt;</code> 需与您在第一步中使用的镜像名称保持一致（例如 <code>joeanamier/tiktok-downloader</code> 或 <code>ghcr.io/joeanamier/tiktok-downloader</code>）
<li>运行容器
<ul>
<li>启动容器：<code>docker start -i 容器名称/容器 ID</code></li>
<li>重启容器：<code>docker restart -i 容器名称/容器 ID</code></li>
</ul>
</li>
</ol>
<p>Docker 容器无法直接访问宿主机的文件系统，部分功能不可用，例如：<code>从浏览器读取 Cookie</code>；其他功能如有异常请反馈！</p>
<hr>

## 关于 Cookie

[点击查看 Cookie 获取教程](https://github.com/JoeanAmier/TikTokDownloader/blob/master/docs/Cookie%E8%8E%B7%E5%8F%96%E6%95%99%E7%A8%8B.md)

> * Cookie 仅需在失效后重新写入配置文件，并非每次运行程序都要写入配置文件！
>
> * Cookie 会影响下载的视频文件分辨率，如果无法下载最高分辨率的视频文件，请尝试更新 Cookie！
>
> * 程序获取数据失败时，可以尝试更新 Cookie 或者使用已登录的 Cookie！

<hr>

## 其他说明

<ul>
<li>程序提示用户输入时，直接回车代表返回上级菜单，输入 <code>Q</code> 或 <code>q</code> 代表结束运行</li>
<li>由于获取账号喜欢作品和收藏作品数据仅返回喜欢 / 收藏作品的发布日期，不返回操作日期，因此程序需要获取全部喜欢 / 收藏作品数据再进行日期筛选；如果作品数量较多，可能会花费较长的时间；可通过 <code>max_pages</code> 参数控制请求次数</li>
<li>获取私密账号的发布作品数据需要登录后的 Cookie，且登录的账号需要关注该私密账号</li>
<li>批量下载账号作品或合集作品时，如果对应的昵称或标识发生变化，程序会自动更新已下载作品文件名称中的昵称和标识</li>
<li>程序下载文件时会先将文件下载至临时文件夹，下载完成后再移动至储存文件夹；程序运行结束时会清空临时文件夹</li>
<li><code>批量下载收藏作品模式</code> 目前仅支持下载当前已登录 Cookie 对应账号的收藏作品，暂不支持多账号</li>
<li>如果想要程序使用代理请求数据，必须在 <code>settings.json</code> 设置 <code>proxy</code> 参数，否则程序不会使用代理</li>
<li>如果您的计算机没有合适的程序编辑 JSON 文件，建议使用 <a href="https://www.toolhelper.cn/JSON/JSONFormat">在线工具</a> 编辑配置文件内容，修改后需要重启软件才能生效。</li>
<li>当程序请求用户输入内容或链接时，请注意避免输入的内容或链接包含换行符，这可能会导致预期之外的问题</li>
<li>本项目不会支持付费作品下载，请勿反馈任何关于付费作品下载的问题</li>
<li>Windows 系统需要以管理员身份运行程序才能读取 Chromium、Chrome、Edge 浏览器 Cookie</li>
<li>本项目并未针对程序多开的情况进行优化，如需程序多开，请复制整个项目的文件夹，避免出现预期之外的问题</li>
<li>程序运行过程中，如需终止程序或 <code>ffmpeg</code>，请按下 <code>Ctrl + C</code> 终止运行，不要直接点击终端窗口的关闭按钮</li>
</ul>
<h2>构建可执行文件指南</h2>
<details>
<summary><b>构建可执行文件指南（点击展开）</b></summary>

本指南将引导您通过 Fork 本仓库并执行 GitHub Actions 自动完成基于最新源码的程序构建和打包！

---

### 使用步骤

#### 1. Fork 本仓库

1. 点击项目仓库右上角的 **Fork** 按钮，将本仓库 Fork 到您的个人 GitHub 账户中
2. 您的 Fork 仓库地址将类似于：`https://github.com/your-username/this-repo`

---

#### 2. 启用 GitHub Actions

1. 前往您 Fork 的仓库页面
2. 点击顶部的 **Settings** 选项卡
3. 点击右侧的 **Actions** 选项卡
4. 点击 **General** 选项
5. 在 **Actions permissions** 下，选择 **Allow all actions and reusable workflows** 选项，点击 **Save** 按钮

---

#### 3. 手动触发打包流程

1. 在您 Fork 的仓库中，点击顶部的 **Actions** 选项卡
2. 找到名为 **构建可执行文件** 的工作流
3. 点击右侧的 **Run workflow** 按钮：
    - 选择 **master** 或者 **develop** 分支
    - 点击 **Run workflow**

---

#### 4. 查看打包进度

1. 在 **Actions** 页面中，您可以看到触发的工作流运行记录
2. 点击运行记录，查看详细的日志以了解打包进度和状态

---

#### 5. 下载打包结果

1. 打包完成后，进入对应的运行记录页面
2. 在页面底部的 **Artifacts** 部分，您将看到打包的结果文件
3. 点击下载并保存到本地，即可获得打包好的程序

---

### 注意事项

1. **资源使用**：
    - Actions 的运行环境由 GitHub 免费提供，普通用户每月有一定的免费使用额度（2000 分钟）

2. **代码修改**：
    - 您可以自由修改 Fork 仓库中的代码以定制程序打包流程
    - 修改后重新触发打包流程，您将得到自定义的构建版本

3. **与主仓库保持同步**：
    - 如果主仓库更新了代码或工作流，建议您定期同步 Fork 仓库以获取最新功能和修复

---

### Actions 常见问题

#### Q1: 为什么我无法触发工作流？

A: 请确认您已按照步骤 **启用 Actions**，否则 GitHub 会禁止运行工作流

#### Q2: 打包流程失败怎么办？

A:

- 检查运行日志，了解失败原因
- 确保代码没有语法错误或依赖问题
- 如果问题仍未解决，可以在本仓库的 [Issues 页面](https://github.com/JoeanAmier/TikTokDownloader/issues) 提出问题

#### Q3: 我可以直接使用主仓库的 Actions 吗？

A: 由于权限限制，您无法直接触发主仓库的 Actions。请通过 Fork 仓库的方式执行打包流程

</details>

## 程序更新

<p><strong>方案一：</strong>下载并解压文件，将旧版本的 <code>_internal\Volume</code> 文件夹复制到新版本的 <code>_internal</code> 文件夹。</p>
<p><strong>方案二：</strong>下载并解压文件（不要运行程序），复制全部文件，直接覆盖旧版本文件。</p>

# ⚠️ 免责声明

<ol>
<li>使用者对本项目的使用由使用者自行决定，并自行承担风险。作者对使用者使用本项目所产生的任何损失、责任、或风险概不负责。</li>
<li>本项目的作者提供的代码和功能是基于现有知识和技术的开发成果。作者按现有技术水平努力确保代码的正确性和安全性，但不保证代码完全没有错误或缺陷。</li>
<li>本项目依赖的所有第三方库、插件或服务各自遵循其原始开源或商业许可，使用者需自行查阅并遵守相应协议，作者不对第三方组件的稳定性、安全性及合规性承担任何责任。</li>
<li>使用者在使用本项目时必须严格遵守 <a href="https://github.com/JoeanAmier/TikTokDownloader/blob/master/LICENSE">GNU
    General Public License v3.0</a> 的要求，并在适当的地方注明使用了 <a
        href="https://github.com/JoeanAmier/TikTokDownloader/blob/master/LICENSE">GNU General Public License
    v3.0</a> 的代码。
</li>
<li>使用者在使用本项目的代码和功能时，必须自行研究相关法律法规，并确保其使用行为合法合规。任何因违反法律法规而导致的法律责任和风险，均由使用者自行承担。</li>
<li>使用者不得使用本工具从事任何侵犯知识产权的行为，包括但不限于未经授权下载、传播受版权保护的内容，开发者不参与、不支持、不认可任何非法内容的获取或分发。</li>
<li>本项目不对使用者涉及的数据收集、存储、传输等处理活动的合规性承担责任。使用者应自行遵守相关法律法规，确保处理行为合法正当；因违规操作导致的法律责任由使用者自行承担。</li>
<li>使用者在任何情况下均不得将本项目的作者、贡献者或其他相关方与使用者的使用行为联系起来，或要求其对使用者使用本项目所产生的任何损失或损害负责。</li>
<li>本项目的作者不会提供 DouK-Downloader 项目的付费版本，也不会提供与 DouK-Downloader 项目相关的任何商业服务。</li>
<li>基于本项目进行的任何二次开发、修改或编译的程序与原创作者无关，原创作者不承担与二次开发行为或其结果相关的任何责任，使用者应自行对因二次开发可能带来的各种情况负全部责任。</li>
<li>本项目不授予使用者任何专利许可；若使用本项目导致专利纠纷或侵权，使用者自行承担全部风险和责任。未经作者或权利人书面授权，不得使用本项目进行任何商业宣传、推广或再授权。</li>
<li>作者保留随时终止向任何违反本声明的使用者提供服务的权利，并可能要求其销毁已获取的代码及衍生作品。</li>
<li>作者保留在不另行通知的情况下更新本声明的权利，使用者持续使用即视为接受修订后的条款。</li>
</ol>
<b>在使用本项目的代码和功能之前，请您认真考虑并接受以上免责声明。如果您对上述声明有任何疑问或不同意，请不要使用本项目的代码和功能。如果您使用了本项目的代码和功能，则视为您已完全理解并接受上述免责声明，并自愿承担使用本项目的一切风险和后果。</b>
<h1>🌟 贡献指南</h1>
<p><strong>欢迎对本项目做出贡献！为了保持代码库的整洁、高效和易于维护，请仔细阅读以下指南，以确保您的贡献能够顺利被接受和整合。</strong></p>
<ul>
<li>在开始开发前，请从 <code>develop</code> 分支拉取最新的代码，以此为基础进行修改；这有助于避免合并冲突并保证您的改动基于最新的项目状态。</li>
<li>如果您的更改涉及多个不相关的功能或问题，请将它们分成多个独立的提交或拉取请求。</li>
<li>每个拉取请求应尽可能专注于单一功能或修复，以便于代码审查和测试。</li>
<li>遵循现有的代码风格；请确保您的代码与项目中已有的代码风格保持一致；建议使用 Ruff 工具保持代码格式规范。</li>
<li>编写可读性强的代码；添加适当的注释帮助他人理解您的意图。</li>
<li>每个提交都应该包含一个清晰、简洁的提交信息，以描述所做的更改。提交信息应遵循以下格式：<code>&lt;类型&gt;: &lt;简短描述&gt;</code></li>
<li>当您准备提交拉取请求时，请优先将它们提交到 <code>develop</code> 分支；这是为了给维护者一个缓冲区，在最终合并到 <code>master</code>
分支之前进行额外的测试和审查。</li>
<li>建议在开发前或遇到疑问时与作者沟通，确保开发方向一致，避免重复劳动或无效提交。</li>
</ul>
<p><strong>参考资料：</strong></p>
<ul>
<li><a href="https://www.contributor-covenant.org/zh-cn/version/2/1/code_of_conduct/">贡献者公约</a></li>
<li><a href="https://opensource.guide/zh-hans/how-to-contribute/">如何为开源做贡献</a></li>
</ul>

# ♥️ 支持项目

<p>如果 <b>DouK-Downloader</b> 对您有帮助，请考虑为它点个 <b>Star</b> ⭐，感谢您的支持！</p>
<table>
<thead>
<tr>
<th align="center">微信(WeChat)</th>
<th align="center">支付宝(Alipay)</th>
</tr>
</thead>
<tbody><tr>
<td align="center"><img src="./docs/微信赞助二维码.png" alt="微信赞助二维码" height="200" width="200"></td>
<td align="center"><img src="./docs/支付宝赞助二维码.png" alt="支付宝赞助二维码" height="200" width="200"></td>
</tr>
</tbody>
</table>
<p>如果您愿意，可以考虑提供资助为 <b>DouK-Downloader</b> 提供额外的支持！</p>

# 💰 项目赞助

## DartNode

[![Powered by DartNode](docs/AD/DartNode_AD.png)](https://dartnode.com "Powered by DartNode - Free VPS for Open Source")

***

## ZMTO

<p><a href="https://www.zmto.com/"><img src="https://console.zmto.com/templates/2019/dist/images/logo_dark.svg" alt="ZMTO"></a></p>
<p><a href="https://www.zmto.com/">ZMTO</a>：一家专业的云基础设施提供商，以可靠的尖端技术与专业支持，提供高效的解决方案，并为符合条件的开源项目提供企业级VPS基础设施，支持开源生态系统的可持续发展与创新。</p>

***

## TikHub

<p><a href="https://tikhub.io/?utm_source=github&utm_medium=readme&utm_campaign=tiktok_downloader&ref=github_joeanamier_tiktokdownloader"><img src="docs/AD/TIKHUB_AD.jpg" alt="TIKHUB" width="458" height="319"></a></p>
<p><a href="https://tikhub.io/?utm_source=github&utm_medium=readme&utm_campaign=tiktok_downloader&ref=github_joeanamier_tiktokdownloader">TikHub API</a> 提供超过 700 个端点，可用于从 14+ 个社交媒体平台获取与分析数据 —— 包括视频、用户、评论、商店、商品与趋势等，一站式完成所有数据访问与分析。</p>
<p>使用 <strong>邀请码</strong>：<code>ZrdH8McC</code> 注册并充值即可获得 <code>$2</code> 额度。</p>

# ✉️ 联系作者

<ul>
<li>作者邮箱：yonglelolu@foxmail.com</li>
<li>作者微信: Downloader_Tools</li>
<li>微信公众号: Downloader Tools</li>
<li><b>Discord 社区</b>: <a href="https://discord.com/invite/ZYtmgKud9Y">点击加入社区</a></li>
<li>QQ 群聊(用于项目交流与摸鱼闲聊): <a href="https://github.com/JoeanAmier/TikTokDownloader/blob/master/docs/QQ%E7%BE%A4%E8%81%8A%E4%BA%8C%E7%BB%B4%E7%A0%81.png">扫码加入群聊</a></li>
</ul>
<p>✨ <b>作者的其他开源项目：</b></p>
<ul>
<li><b>XHS-Downloader（小红书、XiaoHongShu、RedNote）</b>：<a href="https://github.com/JoeanAmier/XHS-Downloader">https://github.com/JoeanAmier/XHS-Downloader</a></li>
<li><b>KS-Downloader（快手、KuaiShou）</b>：<a href="https://github.com/JoeanAmier/KS-Downloader">https://
... [TRUNCATED]
```

### File: requirements.txt
```txt
# This file was autogenerated by uv via the following command:
#    uv pip compile pyproject.toml --no-deps --no-strip-extras -o requirements.txt
aiofiles==25.1.0
    # via douk-downloader (pyproject.toml)
aiosqlite==0.22.1
    # via douk-downloader (pyproject.toml)
emoji==2.15.0
    # via douk-downloader (pyproject.toml)
fastapi==0.135.2
    # via douk-downloader (pyproject.toml)
gmssl==3.2.2
    # via douk-downloader (pyproject.toml)
httpx[socks]==0.28.1
    # via douk-downloader (pyproject.toml)
lxml==6.0.2
    # via douk-downloader (pyproject.toml)
openpyxl==3.1.5
    # via douk-downloader (pyproject.toml)
pydantic==2.12.5
    # via douk-downloader (pyproject.toml)
pyperclip==1.11.0
    # via douk-downloader (pyproject.toml)
qrcode==8.2
    # via douk-downloader (pyproject.toml)
rich==14.3.3
    # via douk-downloader (pyproject.toml)
rookiepy==0.5.6
    # via douk-downloader (pyproject.toml)
uvicorn==0.42.0
    # via douk-downloader (pyproject.toml)

```

### File: locale\README.md
```md
# 命令参考

**运行命令前，确保已经安装了 `gettext` 软件包，并配置好环境变量。**

**Before running the command, ensure that the `gettext` package is installed and the environment variables are properly
configured.**

* `xgettext --files-from=py_files.txt -d tk -o tk.pot`
* `mkdir zh_CN\LC_MESSAGES`
* `msginit -l zh_CN -o zh_CN/LC_MESSAGES/tk.po -i tk.pot`
* `mkdir en_US\LC_MESSAGES`
* `msginit -l en_US -o en_US/LC_MESSAGES/tk.po -i tk.pot`
* `msgmerge -U zh_CN/LC_MESSAGES/tk.po tk.pot`
* `msgmerge -U en_US/LC_MESSAGES/tk.po tk.pot`

# 翻译贡献指南

* 如果想要贡献支持更多语言，请在终端切换至 `locale` 文件夹，运行命令 `msginit -l 语言代码 -o 语言代码/LC_MESSAGES/tk.po -i tk.pot`
  生成 po 文件并编辑翻译。
* 如果想要贡献改进翻译结果，请直接编辑 `tk.po` 文件内容。
* 仅需提交 `tk.po` 文件，作者会转换格式并合并。

# Translation Contribution Guide

* If you want to contribute support for more languages, please switch to the `locale` folder in the terminal and run the
  command `msginit -l language_code -o language_code/LC_MESSAGES/tk.po -i tk.pot` to generate the po file and edit the
  translation.
* If you want to contribute to improving the translation, please directly edit the content of the `tk.po` file.
* Only the `tk.po` file needs to be submitted, and the author will convert the format and merge it.

```

### File: README_EN.md
```md
<div align="center">
<img src="./static/images/DouK-Downloader.png" alt="DouK-Downloader" height="256" width="256"><br>
<h1>DouK-Downloader</h1>
<p><a href="README.md">简体中文</a> | English</p>
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
<p>🔥 <b>TikTok Posts/Liked/Mix/Live/Video/Image/Music; DouYin Posts/Liked/Favorites/Collections/Video/Image/LivePhoto/Live/Music/Mix/Comments/Account/Search/Hot Board Data Acquisition Tools:</b> Fully open-source, free data collection and file download tool based on HTTPX module implementation; batch download of DouYin account posts works, liked works, favorites works and collections works; batch download of TikTok account posts works and liked works; download of DouYin linked or TikTok linked works; obtain DouYin live stream push addresses; download DouYin live stream video; obtain TikTok live stream push addresses; download TikTok live stream video; collect DouYin works comments data; batch download of DouYin Mix works; batch download of TikTok Mix works; collect detailed data of DouYin accounts; collect DouYin user/works/live search results; collect DouYin Hot Board data.</p>
<p>⭐ Previous project names: <code>TikTokDownloader</code></p>
<p>📣 This project will undergo code structure refactoring in the future, with the goal of making the code more robust and providing better maintainability and extensibility. If you have any thoughts on project design, implementation methods, or optimization ideas, you are welcome to make suggestions or participate in discussions!</p>
<p>⭐ Due to the author's limited energy, I was unable to update the English document in a timely manner, and the content may have become outdated, partial translation is machine translation, the translation result may be incorrect, Suggest referring to Chinese documentation. If you want to contribute to translation, we warmly welcome you.</p>
<hr>

# 📝 Project Features

<details>
<summary>Function List (Click to Expand)</summary>
<ul>
<li>✅ Download DouYin video/image</li>
<li>✅ Download DouYin live photo</li>
<li>✅ Download the highest quality video file</li>
<li>✅ Download TikTok video source files</li>
<li>✅ Download TikTok video/image</li>
<li>✅ Download of DouYin account posts/liked/favorites works</li>
<li>✅ Download of TikTok account posts/liked works</li>
<li>✅ Collect detailed data from DouYin/TikTok</li>
<li>✅ Batch download of linked works</li>
<li>✅ Batch download of works from multiple accounts</li>
<li>✅ Automatically skip already downloaded files</li>
<li>✅ Persistently save collected data</li>
<li>✅ Support CSV/XLSX/SQLite format for saving data</li>
<li>✅ Download dynamic/static cover images</li>
<li>✅ Obtain DouYin live stream push addresses</li>
<li>✅ Obtain TikTok live stream push addresses</li>
<li>✅ Use ffmpeg to download live video</li>
<li>✅ Web UI interaction interface</li>
<li>✅ Collect comments data from DouYin works</li>
<li>✅ Batch download of DouYin Mix works</li>
<li>✅ Batch download of TikTok Mix works</li>
<li>✅ Record statistics such as likes and favorites</li>
<li>✅ Filter works based on publication time</li>
<li>✅ Support incremental downloading of account works</li>
<li>✅ Support data Collections using proxies</li>
<li>✅ Support remote access via LAN</li>
<li>✅ Collect detailed data from DouYin accounts</li>
<li>✅ Update statistics of works</li>
<li>✅ Support custom account/mix mark</li>
<li>✅ Automatically update account nickname/mark</li>
<li>✅ Deploy to private servers</li>
<li>✅ Deploy to public servers</li>
<li>✅ Collect DouYin search data</li>
<li>✅ Collect DouYin hot board data</li>
<li>✅ Record IDs of already downloaded works</li>
<li>☑️ <del>Scan QR code to log in and obtain Cookies</del></li>
<li>✅ Obtain Cookies from browsers</li>
<li>✅ Support Web API calls</li>
<li>✅ Support multithreaded downloading of works</li>
<li>✅ File integrity processing mechanism</li>
<li>✅ Custom rules for filtering works</li>
<li>✅ Archive and save works files by folder</li>
<li>✅ Customize file size limit</li>
<li>✅ Support resume downloading of files from breakpoints</li>
<li>✅ Monitor clipboard links to download works</li>
</ul>
</details>

# 💻 Program Screenshot

<p><a href="https://www.bilibili.com/video/BV1d7eAzTEFs/">Watch Demo on Bilibili</a>; <a href="https://youtu.be/yMU-RWl55hg">Watch Demo on YouTube</a></p>

## Terminal interaction mode

<p>It is recommended to manage accounts through configuration files. For more information, please refer to the <a href="https://github.com/JoeanAmier/TikTokDownloader/wiki/Documentation">documentation</a></p>

![终端模式截图](docs/screenshot/终端交互模式截图EN1.png)
*****
![终端模式截图](docs/screenshot/终端交互模式截图EN2.png)
*****
![终端模式截图](docs/screenshot/终端交互模式截图EN3.png)

## Web UI interaction mode

> **The project code has been refactored; the code for this mode has not yet been updated. It will be reopened after
future development is completed!**

## Web API mode

![WebAPI模式截图](docs/screenshot/WebAPI模式截图EN1.png)
*****
![WebAPI模式截图](docs/screenshot/WebAPI模式截图EN2.png)

> **After starting this mode, Open http://127.0.0.1:5555/docs or http://127.0.0.1:5555/redoc to access the automatically
generated documentation!**

### API call example code

```python
from httpx import post
from rich import print


def demo():
    headers = {"token": ""}
    data = {
        "detail_id": "0123456789",
        "pages": 2,
    }
    api = "http://127.0.0.1:5555/douyin/comment"
    response = post(api, json=data, headers=headers)
    print(response.json())


demo()
```

# 📋 Project Instructions

## Quick Start

<p>⭐ Mac OS and Windows 10 and above users can go to <a href="https://github.com/JoeanAmier/TikTokDownloader/releases/latest">Releases</a> or <a href="https://github.com/JoeanAmier/TikTokDownloader/actions">Actions</a> to download the compiled program, ready to use!</p>
<p>⭐ This project includes GitHub Actions for automatic building executable files. Users can use GitHub Actions to build the latest source code into executable files at any time!</p>
<p>⭐ For the automatic building executable files tutorial, please refer to the <code>Build of Executable File Guide</code> section of this document. If you need a more detailed step-by-step tutorial with illustrations, please <a href="https://mp.weixin.qq.com/s/TorfoZKkf4-x8IBNLImNuw">check out this article</a>!</p>
<p><strong>Note: Due to the macOS platform's executable file <code>main</code> not being code-signed, it will be restricted by system security measures on first run. Please execute the command <code>xattr -cr project_folder_path</code> in the terminal to remove the security flag, after which it can run normally.</strong></p>
<hr>
<ol>
<li><b>Run the executable file</b> or <b>configure the environment to run</b> (choose one of the two)
<ol><b>Run the executable file</b>
<li>Download the executable file compressed file built by <a href="https://github.com/JoeanAmier/TikTokDownloader/releases/latest">Releases</a> or Actions.</li>
<li>After extracting, open the program folder and double-click to run <code>main</code>.</li>
</ol>
<ol><b>Configure the environment to run</b>

[//]: # (<li>Install Python interpreter version not lower than <code>3.12</code></li>)
<li>Install the <a href="https://www.python.org/">Python</a> interpreter version <code>3.12</code></li>
<li>Download the latest source code or the source code released in <a href="https://github.com/JoeanAmier/TikTokDownloader/releases/latest">Releases</a> to your local machine</li>
<ol><b>Install project dependencies using pip</b>
<li>Run the command <code>python -m venv venv</code> to create a virtual environment (optional)</li>
<li>Run the command <code>.\venv\Scripts\activate.ps1</code> or <code>venv\Scripts\activate</code> to activate the virtual environment (optional)</li>
<li>Run the command <code>pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt</code> to install the required modules for the program</li>
<li>Run the command <code>python .\main.py</code> or <code>python main.py</code> to start DouK-Downloader</li>
</ol>
<ol><b>Install project dependencies using uv (recommended)</b>
<li>Run the command <code>uv sync --no-dev</code> to synchronize environment dependencies</li>
<li>Run the command <code>uv run main.py</code> to start DouK-Downloader</li>
</ol>
</ol>
</li>
<li>Read the disclaimer of DouK-Downloader and enter content according to the prompt.</li>
<li>Write Cookie Information into Configuration File 
<ol><b>Read Cookie from Clipboard(Recommended)</b>
<li>Refer to the <a href="https://github.com/JoeanAmier/TikTokDownloader/blob/master/docs/Cookie%E8%8E%B7%E5%8F%96%E6%95%99%E7%A8%8B.md">Cookie Extraction Tutorial</a>, copy the required Cookie to the clipboard</li>
<li>Select the <code>Read Cookie from Clipboard</code> option, the program will automatically read the Cookie from the clipboard and write it into the configuration file</li>
</ol>
<ol><b>Read Cookie from Browser</b>
<li>Select the <code>Read Cookie from Browser</code> option, then follow the prompts to input the browser type or its corresponding number</li>
</ol>
<ol><b><del>Obtain Cookie via QR Code Login</del> (No longer valid)</b>
<li><del>Select the <code>Obtain Cookie via QR Code Login</code> option, the program will display a login QR code image and open it with the default application</del></li>
<li><del>Use the TikTok app to scan the QR code and log in</del></li>
<li><del>Follow the prompts, the program will automatically write the Cookie into the configuration file</del></li>
</ol>
</li>
<li>Return to the program interface, sequentially select <code>Terminal interactive mode</code> -> <code>Batch download link works (general)</code> -> <code>Manually enter the link of the works to be collected</code>.</li>
<li>Input the DouYin works link to download the works file (the TikTok platform requires more initial setup, please refer to the documentation for details).</li>
<li>For more detailed instructions, please see <b><a href="https://github.com/JoeanAmier/TikTokDownloader/wiki/Documentation">Project Documentation</a></b>.</li>
</ol>
<p>⭐ It is recommended to use <a href="https://learn.microsoft.com/zh-cn/windows/terminal/install">Windows Terminal</a> (the default terminal that comes with Windows 11).</p>

### Docker Container

<ol>
<li>Get the image</li>
<ul>
<li>Method 1: Build the image using the <code>Dockerfile</code>.</li>
<li>Method 2: Pull the image using the command <code>docker pull joeanamier/tiktok-downloader</code>.</li>
<li>Method 3: Pull the image using the command <code>docker pull ghcr.io/joeanamier/tiktok-downloader</code>.</li>
</ul>
<li>Create the container: <code>docker run --name ContainerName(optional) -p HostPort:5555 -v tiktok_downloader_volume:/app/Volume -it &lt;image name&gt;</code>.</li>
<br><b>Note:</b> The <code>&lt;image name&gt;</code> here must be consistent with the image name you used in the first step (<code>joeanamier/tiktok-downloader</code> or <code>ghcr.io/joeanamier/tiktok-downloader</code>)
<li>Run the container
<ul>
<li>Start the container: <code>docker start -i container name/container ID</code>.</li>
<li>Restart the container: <code>docker restart -i container name/container ID</code>.</li>
</ul>
</li>
</ol>
<p>Docker containers cannot directly access the host machine's file system, and some features may be unavailable, for example: <code>Get Cookie from Browser</code>; if there are any other issues, please report!</p>
<hr>

## About Cookie

[Click to view Cookie tutorial](https://github.com/JoeanAmier/TikTokDownloader/blob/master/docs/Cookie%E8%8E%B7%E5%8F%96%E6%95%99%E7%A8%8B.md)

> * Cookie only needs to be re-written to the configuration file after it expires, and not every time the program is
    run.
>
> * The Cookie can affect the resolution of the video files downloaded from the DouYin platform. If you are unable to
    download high-resolution video files, please try updating the Cookie!
>
> * When the program fails to obtain data, you can try updating the Cookie or using a Cookie that is already logged in!

<hr>

## Other Instructions

<ul>
<li>When the program prompts the user for input, pressing Enter directly will return to the previous menu, and inputting <code>Q</code> or <code>q</code> will end the program's execution.</li>
<li>Since fetching data for liked and favorites works of an account only returns the publication dates of those works, not the dates of the actions (liking or favouring), the program needs to retrieve all liked and favorites works data before performing date filtering. If there are a large number of works, this may take a considerable amount of time. The number of requests can be controlled via the <code>max_pages</code> parameter.</li>
<li>To obtain data for posts made by a private account, a logged-in Cookie is required, and the logged-in account must follow the private account.</li>
<li>When batch downloading account posts works or mix works, if the corresponding nickname or mark parameter changes, the program will automatically update the nickname and mark parameter in the file names of the downloaded works.</li>
<li>When downloading files, the program first downloads them to a temporary folder and then moves them to the storage folder upon completion. The temporary folder will be emptied when the program ends.</li>
<li>The <code>Batch Download Favorites Works Mode</code> currently only supports downloading Favorites works for the account corresponding to the currently logged-in Cookie and does not support multiple accounts.</li>
<li>If you want the program to use a proxy to request data, you must set the <code>proxy</code> parameter in <code>settings.json</code>; otherwise, the program
... [TRUNCATED]
```

### File: docs\Cookie获取教程.md
```md
# Cookie 获取教程

本教程仅演示部分能够获取所需 `Cookie` 的方法，仍有其他方法能够获取所需 `Cookie`；本教程使用的浏览器为 `Microsoft Edge`
，部分浏览器的开发人员工具可能不支持中文语言。

**方法一\(推荐\)：**

1. 打开浏览器\(可选无痕模式启动\)，访问`https://www.douyin.com/`
2. 登录抖音账号\(可跳过\)
3. 按 `F12` 打开开发人员工具
4. 选择 `网络` 选项卡
5. 勾选 `保留日志`
6. 在 `筛选器` 输入框输入 `cookie-name:odin_tt`
7. 点击加载任意一个作品的评论区
8. 在开发人员工具窗口选择任意一个数据包\(如果无数据包，重复步骤7\)
9. 全选并复制 `Cookie` 的值
10. 运行 `main.py` ，根据提示写入 `Cookie`

**截图示例：**

<img src="screenshot/Cookie获取教程1.png" alt="开发人员工具">

**方法二\(不适用本项目\)：**

1. 打开浏览器\(可选无痕模式启动\)，访问`https://www.douyin.com/`
2. 登录抖音账号\(可跳过\)
3. 按 `F12` 打开开发人员工具
4. 选择 `控制台` 选项卡
5. 输入 `document.cookie` 后回车确认
6. 检查 `Cookie` 是否包含 `passport_csrf_token` 和 `odin_tt` 字段
7. 如果未包含所需字段，尝试刷新网页或者点击加载任意一个作品的评论区，回到步骤5
8. 全选并复制 `Cookie` 的值
9. 运行 `main.py` ，根据提示写入 `Cookie`

**截图示例：**

<img src="screenshot/Cookie获取教程2.png" alt="开发人员工具">

# device_id 参数

`device_id` 参数获取方法与 Cookie 类似。

<img src="screenshot/device_id获取示例图.png" alt="开发人员工具">

```

### File: docs\DouK-Downloader文档.md
```md
<div align="center">
<img src="https://github.com/JoeanAmier/TikTokDownloader/blob/master/static/images/DouK-Downloader.png" alt="DouK-Downloader" height="256" width="256"><br>
<h1>DouK-Downloader 项目文档</h1>
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
<p>⭐ <b>项目版本：<code>5.8 Beta</code>；文档更新日期：<code>2026/2/28</code></b></p>
<p>⭐ <b>项目文档正在完善，如果发现任何错误或描述模糊之处，请告知作者以便改进！本项目历史名称：<code>TikTokDownloader</code></b></p>
<p>⭐ Due to the author’s limited time and energy, the complete English documentation for this project is not yet available. If you wish to read the full documentation, we recommend using AI translation tools to assist your understanding. If you would like to contribute to the translation, your help is warmly welcomed.</p>
<hr>
<h1>快速入门</h1>
<p>⭐ 本项目包含手动构建可执行文件的 GitHub Actions，使用者可以随时使用 GitHub Actions 将最新源码构建为可执行文件！</p>
<p>⭐ 自动构建可执行文件教程请查阅本文档的 <code>构建可执行文件指南</code> 部分；如果需要更加详细的图文教程，请 <a href="https://mp.weixin.qq.com/s/TorfoZKkf4-x8IBNLImNuw">查阅文章</a>！</p>
<p><strong>注意：由于 Mac OS 平台的可执行文件 <code>main</code> 未经过代码签名，首次运行时会受到系统安全限制。请先在终端执行 <code>xattr -cr main.app</code> 命令移除安全标记，执行一次后即可正常运行。</strong></p>
<ol>
<li><b>运行可执行文件</b> 或者 <b>配置环境运行</b>
<ol><b>运行可执行文件</b>
<li>下载 <a href="https://github.com/JoeanAmier/TikTokDownloader/releases/latest">Releases</a> 或者 Actions 构建的可执行文件压缩包</li>
<li>解压后打开程序文件夹，双击运行 <code>main</code></li>
</ol>
<ol><b>配置环境运行</b>

[//]: # (<li>安装不低于 <code>3.12</code> 版本的 <a href="https://www.python.org/">Python</a> 解释器</li>)
<li>安装 <code>3.12</code> 版本的 <a href="https://www.python.org/">Python</a> 解释器</li>
<li>下载最新的源码或 <a href="https://github.com/JoeanAmier/TikTokDownloader/releases/latest">Releases</a> 发布的源码至本地</li>
<li>运行 <code>python -m venv venv</code> 命令创建虚拟环境（可选）</li>
<li>运行 <code>.\venv\Scripts\activate.ps1</code> 或者 <code>venv\Scripts\activate</code> 命令激活虚拟环境（可选）</li>
<li>运行 <code>pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt</code> 命令安装程序所需模块</li>
<li>运行 <code>python .\main.py</code> 或者 <code>python main.py</code> 命令启动 DouK-Downloader</li>
</ol>
</li>
<li>阅读 DouK-Downloader 的免责声明，根据提示输入内容</li>
<li>将 Cookie 信息写入配置文件
<ol><b>从剪贴板读取 Cookie（推荐）</b>
<li>参考 <a href="https://github.com/JoeanAmier/TikTokDownloader/blob/master/docs/Cookie%E8%8E%B7%E5%8F%96%E6%95%99%E7%A8%8B.md">Cookie 提取教程</a>，复制所需 Cookie 至剪贴板</li>
<li>选择 <code>从剪贴板读取 Cookie</code> 选项，程序会自动读取剪贴板的 Cookie 并写入配置文件</li>
</ol>
<ol><b>从浏览器读取 Cookie</b>
<li>选择 <code>从浏览器读取 Cookie</code> 选项，按照提示输入浏览器类型或序号</li>
</ol>
<ol><b><del>扫码登录获取 Cookie</del>（失效）</b>
<li><del>选择 <code>扫码登录获取 Cookie</code> 选项，程序会显示登录二维码图片，并使用默认应用打开图片</del></li>
<li><del>使用抖音 APP 扫描二维码并登录账号</del></li>
<li><del>按照提示操作，程序会自动将 Cookie 写入配置文件</del></li>
</ol>
</li>
<li>返回程序界面，依次选择 <code>终端交互模式</code> -> <code>批量下载链接作品(抖音)</code> -> <code>手动输入待采集的作品链接</code></li>
<li>输入抖音作品链接即可下载作品文件</li>
</ol>
<p><b>TikTok 平台功能需要额外设置配置文件 <code>browser_info_tiktok</code> 的 <code>device_id</code> 参数，否则 TikTok 平台功能可能无法正常使用！参数获取方式与 Cookie 类似，详见 <a href="https://github.com/JoeanAmier/TikTokDownloader/blob/master/docs/Cookie%E8%8E%B7%E5%8F%96%E6%95%99%E7%A8%8B.md">Cookie 获取教程</a></b></p>
<h2>Docker 容器</h2>
<ol>
<li>获取镜像</li>
<ul>
<li>方式一：使用 <code>Dockerfile</code> 文件构建镜像</li>
<li>方式二：使用 <code>docker pull joeanamier/tiktok-downloader</code> 命令拉取镜像</li>
<li>方式三：使用 <code>docker pull ghcr.io/joeanamier/tiktok-downloader</code> 命令拉取镜像</li>
</ul>
<li>创建容器：<code>docker run --name 容器名称(可选) -p 主机端口号:5555 -v tiktok_downloader_volume:/app/Volume -it &lt;镜像名称&gt;</code>
</li>
<br><b>注意：</b>此处的 <code>&lt;镜像名称&gt;</code> 需与您在第一步中使用的镜像名称保持一致（例如 <code>joeanamier/tiktok-downloader</code> 或 <code>ghcr.io/joeanamier/tiktok-downloader</code>）
<li>运行容器
<ul>
<li>启动容器：<code>docker start -i 容器名称/容器 ID</code></li>
<li>重启容器：<code>docker restart -i 容器名称/容器 ID</code></li>
</ul>
</li>
</ol>
<p>Docker 容器无法直接访问宿主机的文件系统，部分功能不可用，例如：<code>从浏览器读取 Cookie</code>；其他功能如有异常请反馈！</p>
<h1>Cookie 说明</h1>
<p><a href="https://github.com/JoeanAmier/TikTokDownloader/blob/master/docs/Cookie%E8%8E%B7%E5%8F%96%E6%95%99%E7%A8%8B.md">点击查看 Cookie 获取教程</a>；无效或失效的 Cookie 会导致程序获取数据失败！</p>
<ul>
<li>Cookie 仅需在失效后重新写入配置文件，并非每次运行程序都要写入配置文件！</li>
<li><p>Cookie 会影响下载的视频文件分辨率，如果无法下载最高分辨率的视频文件，请尝试更新 Cookie！</li>
<li>程序获取数据失败时，可以尝试更新 Cookie 或者使用已登录的 Cookie！</li>
</ul>
<h1>入门说明</h1>
<h2>关于终端</h2>
<p>⭐ 推荐使用 <a href="https://learn.microsoft.com/zh-cn/windows/terminal/install">Windows 终端</a>（Windows 11 自带默认终端）运行程序以便获得最佳彩色交互显示效果！</p>
<h2>链接类型</h2>
<ul>
<li>完整链接：使用浏览器打开抖音或 TikTok 链接时，地址栏所显示的 URL 地址。</li>
<li>分享链接：点击 APP 或网页版的分享按钮得到的 URL 地址，抖音平台以 <code>https://v.</code> 开头，掺杂中文和其他字符；TikTok
平台以 <code>https://vm.</code> 或 <code>https://vt.</code> 开头，不掺杂其他字符；使用时<b>不需要</b>手动去除中文和其他字符，程序会自动提取 URL 链接。</li>
</ul>
<h2>数据储存</h2>
<ul>
<li>项目支持使用 <code>CSV</code>、<code>XLSX</code>、<code>SQLite</code> 格式文件储存采集数据。</li>
<li>配置文件 <code>settings.json</code> 的 <code>storage_format</code> 参数可设置数据储存格式类型，如果不设置该参数，程序不会储存任何数据至文件。</li>
<li><code>采集作品评论数据</code>、<code>采集账号详细数据</code>、<code>采集搜索结果数据</code>、<code>采集抖音热榜数据</code> 模式必须设置 <code>storage_format</code> 参数才能正常使用。</li>
<li>程序所有数据均储存至配置文件 <code>root</code> 参数路径下的 <code>Data</code> 文件夹。</li>
</ul>
<h2>文本文档</h2>
<p>项目部分功能支持从文本文档（TXT）读取链接，如需使用，请在计算机任意路径创建一个空白文本文档，然后编辑文件内容，每行输入单个链接，编辑完成后保存文件。</p>
<p>文本文档编码：UTF-8</p>
<h3>文本文档内容示例</h3>

```text
https://www.douyin.com/user/abcd?vid=123456789
https://www.douyin.com/search/key?modal_id=123456789
https://www.douyin.com/video/123456789
https://www.douyin.com/note/123456789
```

<h2>直播下载</h2>
<p><code>获取直播拉流地址</code> 功能需要调用 <code>ffmpeg</code> 下载直播文件；程序会优先调用系统环境的 <code>ffmpeg</code>，其次调用 <code>ffmpeg</code> 参数指定的 <code>ffmpeg</code>，如果 <code>ffmpeg</code> 不可用，程序将不支持直播下载！</p>
<p>建议前往 <a href="https://ffmpeg.org/download.html">官方网站</a> 或者 <a href="https://github.com/BtbN/FFmpeg-Builds">FFmpeg-Builds</a> 获取 <code>ffmpeg</code> 程序！</p>
<p>项目开发时所用的 FFmpeg 版本信息如下，不同版本的 FFmpeg 可能会有差异；若功能异常，请向作者反馈！</p>
<pre>
ffmpeg version n7.1.1-6-g48c0f071d4-20250405 Copyright (c) 2000-2025 the FFmpeg developers
built with gcc 14.2.0 (crosstool-NG 1.27.0.18_7458341)
</pre>
<h2>功能汇总</h2>
<table>
<thead>
<tr>
<th align="center">程序功能</th>
<th align="center">功能类型</th>
</tr>
</thead>
<tbody><tr>
<td align="center">批量下载账号作品（发布、喜欢）</td>
<td align="center">文件下载, 数据采集</td>
</tr>
<tr>
<td align="center">批量下载链接作品</td>
<td align="center">文件下载, 数据采集</td>
</tr>
<tr>
<td align="center">获取直播拉流地址</td>
<td align="center">文件下载, 数据采集</td>
</tr>
<tr>
<td align="center">采集作品评论数据</td>
<td align="center">数据采集</td>
</tr>
<tr>
<td align="center">批量下载合集作品</td>
<td align="center">文件下载, 数据采集</td>
</tr>
<tr>
<td align="center">采集账号详细数据</td>
<td align="center">数据采集</td>
</tr>
<tr>
<td align="center">采集搜索结果数据</td>
<td align="center">数据采集</td>
</tr>
<tr>
<td align="center">采集抖音热榜数据</td>
<td align="center">数据采集</td>
</tr>
<tr>
<td align="center">批量下载收藏作品</td>
<td align="center">文件下载，数据采集</td>
</tr>
<tr>
<td align="center">批量下载收藏夹作品</td>
<td align="center">文件下载，数据采集</td>
</tr>
<tr>
<td align="center">批量下载收藏音乐作品</td>
<td align="center">文件下载，数据采集</td>
</tr>
</tbody></table>
<h2>关闭平台功能</h2>
<p>本项目支持抖音平台和 TikTok 平台的数据采集和文件下载功能，平台功能默认开启，如果不需要使用平台的任何功能，可以编辑配置文件关闭平台功能。</p>
<p>本项目内置参数更新机制，程序会周期性更新抖音与 TikTok 请求的部分参数，以保持参数的有效性（或许没有效果？），该功能无法防止参数失效，参数失效后需要重新写入 Cookie；关闭平台功能后，对应平台的参数更新功能将会禁用！</p>
<h1>配置文件</h1>
<p>配置文件：项目根目录下的 <code>./Volume/settings.json</code> 文件，可以自定义设置程序部分运行参数。</p>
<p>若无特殊需求，大部分配置参数无需修改，直接使用默认值即可。</p>
<p><b><code>cookie</code>、<code>cookie_tiktok</code> 与 <code>device_id</code>参数为必需参数，必须设置该参数才能正常使用程序</b>；其余参数可以根据实际需求进行修改！</p>
<p>如果您的计算机没有合适的程序编辑 JSON 文件，建议使用 <a href="https://www.toolhelper.cn/JSON/JSONFormat">在线工具</a> 编辑配置文件内容，修改后需要重启软件才能生效。</p>
<p>注意: 手动修改 <code>settings.json</code> 后需要重新运行程序才会生效！</p>
<h2>参数说明</h2>
<table>
<thead>
<tr>
<th align="center">参数</th>
<th align="center">类型</th>
<th align="center">说明</th>
<th align="center">默认</th>
</tr>
</thead>
<tbody>
<tr>
<td align="center"><i>mark</i></td>
<td align="center">str</td>
<td align="center"><a href="#mark"><sup>1</sup></a>账号/合集标识，用于区分账号/合集；<strong>属于 accounts_urls、mix_urls 和 owner_url 子参数</strong></td>
<td align="center">账号昵称/合集标题</td>
</tr>
<tr>
<td align="center"><i>url</i></td>
<td align="center">str</td>
<td align="center">账号主页/合集作品链接；<strong>属于 accounts_urls、mix_urls 和 owner_url 子参数</strong></td>
<td align="center">无</td>
</tr>
<tr>
<td align="center"><i>tab</i></td>
<td align="center">str</td>
<td align="center"><a href="#supplement"><sup>2</sup></a>主页标签，<code>post</code> 代表发布作品、<code>favorite</code> 代表喜欢作品；<strong>属于 accounts_urls 子参数</strong></td>
<td align="center">发布作品</td>
</tr>
<tr>
<td align="center"><i>earliest</i></td>
<td align="center">str | float | int</td>
<td align="center">作品最早发布日期，格式：<code>2023/1/1</code>、<code>整数</code>、<code>浮点数</code>；设置为数值代表基于 <code>latest</code>参数的前 XX 天，<strong>属于 accounts_urls 子参数</strong></td>
<td align="center">不限制</td>
</tr>
<tr>
<td align="center"><i>latest</i></td>
<td align="center">str | float | int</td>
<td align="center">作品最晚发布日期，格式：<code>2023/1/1</code>、<code>整数</code>、<code>浮点数</code>；设置为数值代表基于当天的前 XX 天，<strong>属于 accounts_urls 子参数</strong></td>
<td align="center">不限制</td>
</tr>
<tr>
<td align="center"><i>enable</i></td>
<td align="center">bool</td>
<td align="center">参数对象是否启用，设置为 <code>false</code> 时程序会跳过处理；<strong>属于 accounts_urls 和 mix_urls 子参数</strong></td>
<td align="center">启用</td>
</tr>
<tr>
<td align="center">accounts_urls[mark, url, tab, earliest, latest, enable]</td>
<td align="center">list[dict[str, str, str, Any, str, bool]]</td>
<td align="center"><a href="#supplement"><sup>3</sup></a>抖音平台：账号标识，账号链接，主页标签，最早发布日期，最晚发布日期，是否启用；作为 <code>批量下载账号作品</code> 模式选项，支持多账号，以字典格式包含六个参数</td>
<td align="center">无</td>
<tr>
<td align="center">mix_urls[mark, url, enable]</td>
<td align="center">list[dict[str, str, bool]]</td>
<td align="center"><a href="#supplement"><sup>3</sup></a>抖音平台：合集标识，合集链接或作品链接，是否启用；作为 <code>批量下载合集作品</code> 模式选项，支持多合集，以字典格式包含三个参数</td>
<td align="center">无</td>
</tr>
<tr>
<td align="center">owner_url[mark, url]</td>
<td align="center">dict[str, str]</td>
<td align="center"><a href="#supplement"><sup>3</sup></a>抖音平台：当前登录 Cookie 的账号标识，账号主页链接；<code>批量下载收藏作品</code> 模式下用于获取账号信息，以字典格式包含两个参数</td>
<td align="center">无</td>
</tr>
<tr>
<td align="center">accounts_urls_tiktok[mark, url, tab, earliest, latest, enable]</td>
<td align="center">list[dict[str, str, str, Any, str, bool]]</td>
<td align="center"><a href="#supplement"><sup>3</sup></a>TikTok 平台；参数规则与 <code>accounts_urls</code> 一致</td>
<td align="center">无</td>
</tr>
<tr>
<td align="center">mix_urls_tiktok[mark, url, enable]</td>
<td align="center">list[dict[str, str, bool]]</td>
<td align="center"><a href="#supplement"><sup>3</sup></a>TikTok 平台；参数规则与 <code>mix_urls</code> 一致</td>
<td align="center">无</td>
</tr>
<tr>
<td align="center">owner_url_tiktok[mark, url](未生效)</td>
<td align="center">dict[str, str]</td>
<td align="center"><a href="#supplement"><sup>3</sup></a>TikTok 平台；参数规则与 <code>owner_url</code> 一致</td>
<td align="center">无</td>
</tr>
<tr>
<td align="center">root</td>
<td align="center">str</td>
<td align="center">作品文件和数据记录保存路径；建议使用绝对路径</td>
<td align="center">项目根路径/Volume</td>
</tr>
<tr>
<td align="center">folder_name</td>
<td align="center">str</td>
<td align="center">批量下载链接作品时，保存文件夹的名称</td>
<td align="center">Download</td>
</tr>
<tr>
<td align="center">name_format</td>
<td align="center">str</td>
<td align="center">文件保存时的命名规则，值之间使用空格分隔，支持：<code>id</code>：作品 ID；<code>desc</code>：作品描述；<code>create_time</code>：发布时间；<code>nickname</code>：账号昵称；<code>mark</code>：账号标识；<code>uid</code>：账号 ID；<code>type</code>：作品类型</td>
<td align="center">发布时间-作品类型-账号昵称-描述</td>
</tr>
<tr>
<td align="center">desc_length</td>
<td align="center">int</td>
<td align="center">作品文件名中描述字段的最大字符数；超过限制的描述字段将折叠处理</td>
<td align="center">64</td>
</tr>
<tr>
<td align="center">name_length</td>
<td align="center">int</td>
<td align="center">作品文件名称的最大字符数；超过限制的文件名称将折叠处理</td>
<td align="center">128</td>
</tr>
<tr>
<td align="center">date_format</td>
<td align="center">str</td>
<td align="center">日期时间格式；<a href="https://docs.python.org/zh-cn/3/library/time.html?highlight=strftime#time.strftime">点击查看设置规则</a></td>
<td align="center">年-月-日 时:分:秒</td>
</tr>
<tr>
<td align="center">split</td>
<td align="center">str</td>
<td align="center">文件命名的分隔符</td>
<td align="center">-</td>
</tr>
<tr>
<td align="center">folder_mode</td>
<td align="center">bool</td>
<td align="center">是否将每个作品的文件储存至单独的文件夹，文件夹名称格式与 <code>name_format</code> 参数一致</td>
<td align="center">false</td>
</tr>
<tr>
<td align="center">music</td>
<td align="center">bool</td>
<td align="center">是否下载作品音乐</td>
<td align="center">false</td>
</tr>
<tr>
<td align="center">truncate</td>
<td align="center">int</td>
<td align="center">文件下载进度条中描述字符串的最大长度，该参数用于调整显示效果</td>
<td align="center">64</td>
</tr>
<tr>
<td align="center">storage_format</td>
<td align="center">str</td>
<td align="center"><a href="#supplement"><sup>3</sup></a>采集数据持久化储存格式，支持：<code>csv</code>、<code>xlsx</code>、<code>sql</code>(SQLite)</td>
<td align="center">不保存</td>
</tr>
<tr>
<td align="center">cookie</td>
<td align="center">dict | str</td>
<td align="center"><a href="#supplement"><sup>4</sup></a>抖音网页版 Cookie, 必需参数; 建议通过程序写入配置文件，亦可手动编辑</td>
<td align="center">无</td>
</tr>
<tr>
<td align="center">cookie_tiktok</td>
<td align="center">dict | str</td>
<td align="center"><a href="#supplement"><sup>4</sup></a>TikTok 网页版 Cookie, 必需参数; 建议通过程序写入配
... [TRUNCATED]
```

### File: docs\Release_Notes.md
```md
**更新内容：**

1. API 模式搜索接口增加 `offset` 和 `count` 参数
2. 修复部分 TikTok 账号提取 sec_user_id 失败的问题
3. 修复 API 模式账号作品接口部分参数不生效的问题
4. 修复 API 模式搜索接口多页数据报错的问题
5. 修复 API 模式搜索接口结果为空报错的问题
6. 修复 TikTok 平台批量下载账号作品功能
7. 修复 TikTok 平台批量下载合集作品功能
8. 修复报错时可能损坏 XLSX 文件的问题
9. TikTok 平台新增 X-Gnarly 请求参数
10. 优化提取 secUid 的正则表达式
11. 服务器模式默认启用局域网访问
12. 修复请求参数编码错误的问题
13. 修复提取作品 ID 失败的问题
14. 更新数据接口请求参数
15. 更新项目英语翻译
16. 修正项目功能描述
17. 修复其他已知问题

```

### File: locale\generate_path.py
```py
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def find_python_files(dir_, file):
    with open(file, "w", encoding="utf-8") as f:
        for py_file in dir_.rglob("*.py"):  # 递归查找所有 .py 文件
            f.write(str(py_file) + "\n")  # 写入文件路径


# 设置源目录和输出文件
source_directory = ROOT.joinpath("src")  # 源目录
output_file = "py_files.txt"  # 输出文件名

find_python_files(source_directory, output_file)
print(f"所有 .py 文件路径已保存到 {output_file}")

```

### File: locale\po_to_mo.py
```py
from pathlib import Path
from subprocess import run

ROOT = Path(__file__).resolve().parent


def scan_directory():
    return [
        item.joinpath("LC_MESSAGES/tk.po") for item in ROOT.iterdir() if item.is_dir()
    ]


def generate_map(files: list[Path]):
    return [(i, i.with_suffix(".mo")) for i in files]


def generate_mo(maps: list[tuple[Path, Path]]):
    for i, j in maps:
        command = f'msgfmt --check -o "{j}" "{i}"'
        print(run(command, shell=True, text=True))


if __name__ == "__main__":
    generate_mo(generate_map(scan_directory()))

```

### File: .github\ISSUE_TEMPLATE\bug_report.md
```md
---
name: Bug report
about: 报告项目问题
title: '[功能异常] '
labels: ''
assignees: JoeanAmier

---

**问题描述**

清晰简洁地描述该错误是什么。

A clear and concise description of what the bug is.

**重现步骤**

重现该问题的步骤：

Steps to reproduce the behavior:

1. ...
2. ...
3. ...

**预期结果**

清晰简洁地描述您预期会发生的情况。

A clear and concise description of what you expected to happen.

**补充信息**

在此添加有关该问题的任何其他上下文信息，例如：操作系统、运行方式、配置文件、错误截图、运行日志等。

请注意：提供配置文件时，请删除 Cookie 内容，避免敏感数据泄露！

Add any other contextual information about the issue here, such as operating system, runtime mode, configuration files,
error screenshots, runtime logs, etc.

Please note: When providing configuration files, please delete cookie content to avoid sensitive data leakage!

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
