# ☘️ llm-lean-log

<p align="center">
  <img src="docs/imgs/logo.webp" alt="llm-lean-log logo" width="200">
</p>

使用 LLM 及其代理来读写日志：

- Antigravity
- Cursor
- Windsurf
- Claude Code
- Opencode
- 或您选择的任何 LLM 客户端

从我日常编码需求出发，我想要一个记录与AI代理聊天会话的工具，以便将其用作个人参考资料或项目文档。在浏览开发者群组时，我还注意到对跨多台机器同步聊天日志和保存长期历史记录的需求日益增长。

这就是 `llm-lean-log-cli` 的由来：一个用于读写聊天历史记录的工具，针对最小化token使用进行了优化——这意味着更少的tokens，因此成本更低。

> 📝 为大语言模型（LLM）设计的日志记录工具，但去除了冗余部分。

`llm-lean-log` 是一种为大语言模型token使用量优化的日志格式，基于CSV数据的因果关系。

## 🍓 让AI代理（LLM）写日志

在让AI代理（LLM）写日志之前，请确保全局安装 `llm-lean-log-cli` 命令行工具。

```bash
bun add -g llm-lean-log-cli
```

通过提示词让LLM写日志：

> 使用 `l-log add ./logs/chat.csv "修复错误" --tags=bug,fix --problem="问题描述" --files="file1.ts,src/file2.ts" --tech-stack="elysia,drizzle,sqlite" --causeIds="uuid1,uuid2" --created-by-agent="agent-name"` 命令行工具保存上面的聊天记录

或者对用户来说更简单但对LLM效率较低的方式：

> 使用 l-log CLI 保存上面的聊天记录

或者：

> 使用 l-log 保存

## 🍓 让AI代理（LLM）读取日志

只通过提示词让LLM读取最后一条日志（对LLM高效）：

> 运行 `l-log view ./logs/example.csv --last` 命令并读取输出

通过提示词让LLM读取所有日志（对LLM效率较低）：

> 从"./logs/example.csv"读取最近的聊天记录，并告诉我接下来应该做什么

这是LLM读取日志的有效方式。节省时间、token和能源。因为LLM不需要先读取长CSV文件才能在日志末尾写入新日志。

## 📚 为代理添加写日志规则

例如，您可以将此规则添加到您的LLM代理配置文件中（例如 `.agent/rules/common.md`）：

```bash
# 创建文件
touch .agent/rules/common.md
```

复制 [.agent/rules/common.md](.agent/rules/common.md) 的内容。

更改规则中的 `logs/chat.csv` 文件路径。

如果LLMs忘记写日志或者不知道应该写日志时，可以提示LLMs写日志：

> use l-log

## 🌵 MCP Memory

对于 MCP 内存，请使用 `l-log-mcp-server` 软件包。更多信息请参见 [packages/mcp/README.md](packages/mcp/README.md) 和 [packages/mcp-server/README.md](packages/mcp-server/README.md)。

## ❌ 问题

- 🐥 `markdown` 没有为LLM的token使用量优化，仅适用于人类阅读。
- 🐥 `json` 没有为LLM的token使用量优化，仅适用于机器阅读。
- 🐥 LLM token使用量的最佳性能。这是纯表格数据，所以对于平面表，CSV比`TOON`更小。参考 <https://github.com/toon-format/toon?tab=readme-ov-file#when-not-to-use-toon>。
- 🐥 有许多系统日志的最佳实践，但它们没有为LLM的token使用量优化，缺少理解日志聊天上下文的数据结构。
  - 例如，系统日志器使用日志级别WARNING，但LLM需要知道什么？
- 🐥 清晰、可预测且简单的格式，供LLM读取过去的日志。
- 🐥 当LLM写日志时，应使用命令行工具保存日志，这样LLM无需自己编辑CSV文件，节省时间、token和能源。
  - 🌳 我们需要一种LLM保存日志的高效方式。
- 🐥 当人类读取CSV日志时，我希望有一个工具以更人性化的方式查看长CSV日志。
  - 🌳 我们需要一种人类读取日志的高效方式。
- 🌳 本地优先、完全控制的日志和项目文档存储，不依赖于Cursor、Windsurf、TUI客户端等外部服务。
- 🐥 非常长的对话历史，但LLM可以用几句话总结并仅保存重要信息。
  - 🌳 不要保存所有对话历史，只保存重要信息。
- 🌳 我们需要基于推理、类似人类的长文档检索（如 <https://github.com/VectifyAI/PageIndex>）。
  - 数据可以是有向无环图（<https://zh.wikipedia.org/wiki/%E6%9C%89%E5%90%91%E6%97%A0%E7%8E%AF%E5%9B%BE>）或有向循环图（<https://zh.wikipedia.org/wiki/%E6%9C%89%E5%90%91%E5%9B%BE>）。因果关系是节点之间的链接 - 聊天。

## ✅ 解决方案

<img src="docs/imgs/graph.png" alt="图" width="256">

🪴 创建一个简单、单一、平面的CSV数据格式文件作为日志：

- 🌟 表头是日志记录的重要字段：
  - `id`: 日志ID（必需），UUID作为唯一标识符，用于有向图，因果关系。
  - `name`: 日志的主要内容（简短）。（必需）
  - `tags`: 用于分类日志的标签，逗号分隔。示例：`error,api,auth`。（可选）
  - `problem`: 问题描述，日志上下文。（必需）
  - `solution`: 解决方案描述，解决问题的方法。（可选）
  - `action`: 运行命令，采取的行动（网络搜索等）来解决问题。（可选）
    - 运行命令格式：`text {language}`\`code-block\``
      - 行值示例：

        ```text
        运行 bash`bun i`; 然后启动开发服务器 bash`bun dev`; 更新 "src/constants.ts" 中的常量：ts`const MY_CONSTANT = 'new value';`
        ```

      - 语言是可选的，但推荐使用以获得更好的解析。
      - 为什么？
        - 更好的代码解析和理解。
        - 学习Markdown代码块格式，这样人类可以阅读和理解代码。
    - 格式：`text {language}`\`code-block\`` 或者 markdown code block 或者 text。
  - `files`: 修改、创建、删除或必须阅读的文件列表（可选）。
    - 示例：`src/index.ts,src/constants.ts`
    - 为什么？
      - 更好地理解代码，日志上下文。
    - 格式：逗号分隔的文件列表。
  - `tech-stack`: 使用的技术列表（可选）。
    - 示例：`elysia,drizzle,sqlite,turso`
    - 为什么？
      - 更好地理解代码，日志上下文。
    - 格式：逗号分隔的技术列表。
  - `cause`: 问题的原因（可选）。
    - 示例：`you choose to use X instead of Y, to do Z`
    - 为什么？
      - 更好地理解日誌。
    - 格式：文本。

  - `causeIds`: 日志的原因ID（可选）。
    - 示例：`UUID,UUID`
    - 为什么？
      - 更好地理解日志。
    - 格式：逗号分隔的其他日志ID列表。

  - `effectIds`: 日志的影响ID（可选）。
    - 示例：`UUID,UUID`
    - 为什么？
      - 更好地理解日志。
    - 格式：逗号分隔的其他日志ID列表。

  - `last-commit-short-sha`: 日志的最后一次git提交短SHA（可选）。
    - 示例：`a1b2c3d`
    - 为什么不更新git提交？
      - git提交通常在LLM写日志之前就已更新。
    - 格式：最后一次提交的短SHA。

  - `created-at`: 日志创建时间。（必需）。
    - 格式：`YYYY-MM-DDTHH:mm:ssZ`（ISO 8601）
      - 示例：`2025-10-15T12:34:56Z`
      - 人类、机器和LLM都可读。
  - `updated-at`: 日志更新时间（可选）。
    - 格式：`YYYY-MM-DDTHH:mm:ssZ`（ISO 8601）
      - 示例：`2025-10-15T12:34:56Z`
      - 人类、机器和LLM都可读。
  - `model`: 使用的模型（可选）。
    - 示例：`gpt-4o-mini`
  - `created-by-agent`: 用于创建日志的模型（可选）。
    - 示例：`gpt-4o-mini`
- 行：
  - 每一行是一个日志条目。
  - 没有换行符，或使用`\n`，只需使用逗号 - `,`，句号 - `.`，分号 - `;` 来分隔信息。

## 其他问题

CSV格式有时难以阅读，因为它对人类不够友好，行太长，不支持代码块。

### 解决方案

使用 `llm-lean-log-cli` 命令行工具以更人性化的方式查看日志。

```bash
bun add -g llm-lean-log-cli
```

## 💻 使用方法

`llm-lean-log-cli` 的二进制名称是 `l-log`。

对于LLM查看日志（不需要 `--human` 选项，输出是CSV格式（+ 如果元数据列为空则自动隐藏））：

```bash
# 列出所有日志条目，输出是CSV格式
l-log list ./logs/example.csv
```

LLM的预期输出是CSV格式：

```text
id,name,tags,problem,solution,action,files,tech-stack,causeIds,created-at,model
auth-error-001,API身份验证错误,"error,api,auth",由于JWT令牌过期未正确处理，用户无法登录,添加了带指数退避重试机制的令牌刷新逻辑,更新了auth.ts中间件并添加了刷新端点,"src/middleware/auth.ts, src/routes/auth.routes.ts","typescript, express, jwt",,2026-01-13T14:52:58.681Z,claude-3.5-sonnet
db-investigation-002,数据库连接池耗尽,"error,database,performance",高流量期间应用程序崩溃，由于数据库连接池耗尽,将池大小从10增加到50并添加了连接超时处理,"修改database.config.ts: ts`pool.max = 50, pool.idleTimeoutMillis = 30_000`",src/config/database.config.ts,"typescript, postgresql, node.js",auth-error-001,2026-01-13T14:52:58.681Z,gpt-4-turbo
...
```

```bash
# 显示统计信息
l-log stats ./logs/example.csv

# 查看索引处的详细条目
l-log view ./logs/example.csv 0

# 查看最后一条日志
l-log view ./logs/example.csv --last
```

LLM的预期输出是CSV格式：

```text
id,name,tags,problem,solution,action,files,tech-stack,causeIds,created-at,model
typescript-migration-006,TypeScript迁移完成,"refactor,typescript,milestone",代码库是JavaScript，很难捕获类型错误,将整个代码库迁移到TypeScript并启用严格模式,"将所有.js文件转换为.ts，添加类型定义，配置tsconfig.json","tsconfig.json, package.json, src/**/*","typescript, node.js","auth-error-001,memory-leak-004,image-optimization-005",2026-01-13T14:52:58.681Z,gpt-4-turbo
```

```bash
# 搜索日志，输出是CSV格式
l-log search ./logs/example.csv "Database"

# 按标签过滤，输出是CSV格式
l-log tags ./logs/example.csv error api

# 添加新的日志条目
l-log add ./logs/chat.csv "修复错误" --tags=bug,fix --problem="问题描述"
```

对于人类用户使用 `--human` 选项查看日志：

```bash
# 列出所有日志条目
l-log list ./logs/example.csv --human
# 输出: [带有颜色和标题的完整漂亮表格]

# 显示统计信息
l-log stats ./logs/example.csv --human

# 查看索引处的详细条目
l-log view ./logs/example.csv 0 --human

# 搜索日志
l-log search ./logs/example.csv "query" --human

# 按标签过滤
l-log tags ./logs/example.csv tag1 tag2 --human

# 添加新的日志条目，如果不指定日志文件，则使用 `./logs/example.csv` 日志文件
l-log add ./logs/example.csv "修复错误" --tags=bug,fix --problem="问题描述"
```

## 🐳 人类的可视化工具

全局安装 `l-log-vis` (llm-lean-log-visualizer` 包)：

```bash
bun add -g l-log-vis
```

运行可视化工具：

```bash
l-log-vis ./logs/example.csv
# 或者
l-log-vis
```

## 🛠️ 开发

- 添加了用于管理日志的命令行工具
- 添加了搜索和过滤功能
- 添加了基于React的精美Web可视化工具，具有代码高亮功能，更多信息请参见 [Web可视化工具](./packages/visualizer/README.md)。

安装依赖项：

```bash
bun i
```

### 🌈 运行应用程序

🌱 创建示例日志并运行可视化工具：

```bash
bun example
```

💻 命令行使用：

```bash
# 列出所有日志条目
bun cli list

# 列出所有日志条目（紧凑视图）
bun cli ls -c
```

```bash
# 显示统计信息
bun cli stats
```

截图：

![CLI Stats](docs/imgs/bun-cli-stats.png)

```bash
# 查看索引处的详细条目
bun cli view 0

# 查看最后一条日志
bun cli view --last
```

截图：

![CLI View](docs/imgs/bun-cli-view.png)

```bash
# 按名称、问题或解决方案搜索日志
bun cli search "memory"
```

截图：

![CLI Search](docs/imgs/bun-cli-search.png)

```bash
# 按标签过滤日志
bun cli tags error api
```

```bash
# 添加新的日志条目
bun cli add "修复错误" --tags=bug,fix --problem="错误描述" --solution="修复了问题"
# 预期: 日志条目添加成功

# 显示帮助
bun cli help
```

此项目使用 `bun init` 在 bun v1.3.5 中创建。[Bun](https://bun.com) 是一个快速的一体化JavaScript运行时。

## 📖 附加信息

- 发布文档：`./docs/publish.sh`
- 发布文档：`./docs/release.sh`

更多信息请参见 `./docs` 文件夹。

### 💻 与VS Code基础编辑器一起使用

- 从 `.vscode/extensions.json` 安装推荐的扩展，包括：
  - `DavidAnson.vscode-markdownlint` - Markdown linting
  - `biomejs.biome` - 代码格式化和linting
  - `oven-sh.bun` - Bun运行时支持
  - `jeff-hykin.better-csv-syntax` - CSV语法高亮（带颜色编码）
  - `YoavBls.pretty-ts-errors` - 美观的TypeScript错误
  - `ReprEng.csv` - CSV支持
  
![CSV Preview](./docs/imgs/screenshot-csv-preview.png)

## 📚 覆盖状态

`./coverage.txt`

## 待办事项

- 改进有向图的Web可视化应用（显示因果关系）。

## 📄 许可证

MIT
