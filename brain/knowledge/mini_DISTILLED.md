---
id: mini
type: knowledge
owner: OA_Triage
---
# mini
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# Mini Agent

English | [中文](./README_CN.md)

**Mini Agent** is a minimal yet professional demo project that showcases the best practices for building agents with the MiniMax M2.5 model. Leveraging an Anthropic-compatible API, it fully supports interleaved thinking to unlock M2's powerful reasoning capabilities for long, complex tasks.

This project comes packed with features designed for a robust and intelligent agent development experience:

*   ✅ **Full Agent Execution Loop**: A complete and reliable foundation with a basic toolset for file system and shell operations.
*   ✅ **Persistent Memory**: An active **Session Note Tool** ensures the agent retains key information across multiple sessions.
*   ✅ **Intelligent Context Management**: Automatically summarizes conversation history to handle contexts up to a configurable token limit, enabling infinitely long tasks.
*   ✅ **Claude Skills Integration**: Comes with 15 professional skills for documents, design, testing, and development.
*   ✅ **MCP Tool Integration**: Natively supports MCP for tools like knowledge graph access and web search.
*   ✅ **Comprehensive Logging**: Detailed logs for every request, response, and tool execution for easy debugging.
*   ✅ **Clean & Simple Design**: A beautiful CLI and a codebase that is easy to understand, making it the perfect starting point for building advanced agents.

## Table of Contents

- [Mini Agent](#mini-agent)
  - [Table of Contents](#table-of-contents)
  - [Quick Start](#quick-start)
    - [1. Get API Key](#1-get-api-key)
    - [2. Choose Your Usage Mode](#2-choose-your-usage-mode)
      - [🚀 Quick Start Mode (Recommended for Beginners)](#-quick-start-mode-recommended-for-beginners)
      - [🔧 Development Mode](#-development-mode)
  - [ACP \& Zed Editor Integration(optional)](#acp--zed-editor-integrationoptional)
  - [Usage Examples](#usage-examples)
    - [Task Execution](#task-execution)
    - [Using a Claude Skill (e.g., PDF Generation)](#using-a-claude-skill-eg-pdf-generation)
    - [Web Search \& Summarization (MCP Tool)](#web-search--summarization-mcp-tool)
  - [Testing](#testing)
    - [Quick Run](#quick-run)
    - [Test Coverage](#test-coverage)
  - [Troubleshooting](#troubleshooting)
    - [SSL Certificate Error](#ssl-certificate-error)
    - [Module Not Found Error](#module-not-found-error)
  - [Related Documentation](#related-documentation)
  - [Community](#community)
  - [Contributing](#contributing)
  - [License](#license)
  - [References](#references)

## Quick Start

### 1. Get API Key

MiniMax provides both global and China platforms. Choose based on your network environment:

| Version    | Platform                                                       | API Base                   |
| ---------- | -------------------------------------------------------------- | -------------------------- |
| **Global** | [https://platform.minimax.io](https://platform.minimax.io)     | `https://api.minimax.io`   |
| **China**  | [https://platform.minimaxi.com](https://platform.minimaxi.com) | `https://api.minimaxi.com` |

**Steps to get API Key:**
1. Visit the corresponding platform to register and login
2. Go to **Account Management > API Keys**
3. Click **"Create New Key"**
4. Copy and save it securely (key is only shown once)

> 💡 **Tip**: Remember the API Base address corresponding to your chosen platform, you'll need it for configuration

### 2. Choose Your Usage Mode

**Prerequisites: Install uv**

Both usage modes require uv. If you don't have it installed:

```bash
# macOS/Linux/WSL
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
python -m pip install --user pipx
python -m pipx ensurepath
# Restart PowerShell after installation

# After installation, restart your terminal or run:
source ~/.bashrc  # or ~/.zshrc (macOS/Linux)
```

We offer two usage modes - choose based on your needs:

#### 🚀 Quick Start Mode (Recommended for Beginners)

Perfect for users who want to quickly try Mini Agent without cloning the repository or modifying code.

**Installation:**

```bash
# 1. Install directly from GitHub
uv tool install git+https://github.com/MiniMax-AI/Mini-Agent.git

# 2. Run setup script (automatically creates config files)
# macOS/Linux:
curl -fsSL https://raw.githubusercontent.com/MiniMax-AI/Mini-Agent/main/scripts/setup-config.sh | bash

# Windows (PowerShell):
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/MiniMax-AI/Mini-Agent/main/scripts/setup-config.ps1" -OutFile "$env:TEMP\setup-config.ps1"
powershell -ExecutionPolicy Bypass -File "$env:TEMP\setup-config.ps1"
```

> 💡 **Tip**: If you want to develop locally or modify code, use "Development Mode" below

**Configuration:**

The setup script creates config files in `~/.mini-agent/config/`. Edit the config file:

```bash
# Edit config file
nano ~/.mini-agent/config/config.yaml
```

Fill in your API Key and corresponding API Base:

```yaml
api_key: "YOUR_API_KEY_HERE"          # API Key from step 1
api_base: "https://api.minimax.io"  # Global
# api_base: "https://api.minimaxi.com"  # China
model: "MiniMax-M2.5"
```

**Start Using:**

```bash
mini-agent                                    # Use current directory as workspace
mini-agent --workspace /path/to/your/project  # Specify workspace directory
mini-agent --version                          # Check version

# Management commands
uv tool upgrade mini-agent                    # Upgrade to latest version
uv tool uninstall mini-agent                  # Uninstall if needed
uv tool list                                  # View all installed tools
```

#### 🔧 Development Mode

For developers who need to modify code, add features, or debug.

**Installation & Configuration:**

```bash
# 1. Clone the repository
git clone https://github.com/MiniMax-AI/Mini-Agent.git
cd Mini-Agent

# 2. Install uv (if you haven't)
# macOS/Linux:
curl -LsSf https://astral.sh/uv/install.sh | sh
# Windows (PowerShell):
irm https://astral.sh/uv/install.ps1 | iex
# Restart terminal after installation

# 3. Sync dependencies
uv sync

# Alternative: Install dependencies manually (if not using uv)
# pip install -r requirements.txt
# Or install required packages:
# pip install tiktoken pyyaml httpx pydantic requests prompt-toolkit mcp

# 4. Initialize Claude Skills (Optional)
git submodule update --init --recursive

# 5. Copy config template
```

**macOS/Linux:**
```bash
cp mini_agent/config/config-example.yaml mini_agent/config/config.yaml
```

**Windows:**
```powershell
Copy-Item mini_agent\config\config-example.yaml mini_agent\config\config.yaml

# 6. Edit config file
vim mini_agent/config/config.yaml  # Or use your preferred editor
```

Fill in your API Key and corresponding API Base:

```yaml
api_key: "YOUR_API_KEY_HERE"          # API Key from step 1
api_base: "https://api.minimax.io"  # Global
# api_base: "https://api.minimaxi.com"  # China
model: "MiniMax-M2.5"
max_steps: 100
workspace_dir: "./workspace"
```

> 📖 Full configuration guide: See [config-example.yaml](mini_agent/config/config-example.yaml)

**Run Methods:**

Choose your preferred run method:

```bash
# Method 1: Run as module directly (good for debugging)
uv run python -m mini_agent.cli

# Method 2: Install in editable mode (recommended)
uv tool install -e .
# After installation, run from anywhere and code changes take effect immediately
mini-agent
mini-agent --workspace /path/to/your/project
```

> 📖 For more development guidance, see [Development Guide](docs/DEVELOPMENT_GUIDE.md)

> 📖 For more production deployment guidance, see [Production Guide](docs/PRODUCTION_GUIDE.md)

## ACP & Zed Editor Integration(optional)

Mini Agent supports the [Agent Communication Protocol (ACP)](https://github.com/modelcontextprotocol/protocol) for integration with code editors like Zed.

**Setup in Zed Editor:**

1. Install Mini Agent in development mode or as a tool
2. Add to your Zed `settings.json`:

```json
{
  "agent_servers": {
    "mini-agent": {
      "command": "/path/to/mini-agent-acp"
    }
  }
}
```

The command path should be:
- If installed via `uv tool install`: Use the output of `which mini-agent-acp`
- If in development mode: `./mini_agent/acp/server.py`

**Usage:**
- Open Zed's agent panel with `Ctrl+Shift+P` → "Agent: Toggle Panel"
- Select "mini-agent" from the agent dropdown
- Start conversations with Mini Agent directly in your editor

## Usage Examples

Here are a few examples of what Mini Agent can do.

### Task Execution

*In this demo, the agent is asked to create a simple, beautiful webpage and display it in the browser, showcasing the basic tool-use loop.*

![Demo GIF 1: Basic Task Execution](docs/assets/demo1-task-execution.gif "Basic Task Execution Demo")

### Using a Claude Skill (e.g., PDF Generation)

*Here, the agent leverages a Claude Skill to create a professional document (like a PDF or DOCX) based on the user's request, demonstrating its advanced capabilities.*

![Demo GIF 2: Claude Skill Usage](docs/assets/demo2-claude-skill.gif "Claude Skill Usage Demo")

### Web Search & Summarization (MCP Tool)

*This demo shows the agent using its web search tool to find up-to-date information online and summarize it for the user.*

![Demo GIF 3: Web Search](docs/assets/demo3-web-search.gif "Web Search Demo")

## Testing

The project includes comprehensive test cases covering unit tests, functional tests, and integration tests.

### Quick Run

```bash
# Run all tests
pytest tests/ -v

# Run core functionality tests
pytest tests/test_agent.py tests/test_note_tool.py -v
```

### Test Coverage

- ✅ **Unit Tests** - Tool classes, LLM client
- ✅ **Functional Tests** - Session Note Tool, MCP loading
- ✅ **Integration Tests** - Agent end-to-end execution
- ✅ **External Services** - Git MCP Server loading


## Troubleshooting

### SSL Certificate Error

If you encounter `[SSL: CERTIFICATE_VERIFY_FAILED]` error:

**Quick fix for testing** (modify `mini_agent/llm.py`):
```python
# Line 50: Add verify=False to AsyncClient
async with httpx.AsyncClient(timeout=120.0, verify=False) as client:
```

**Production solution**:
```bash
# Update certificates
pip install --upgrade certifi

# Or configure system proxy/certificates
```

### Module Not Found Error

Make sure you're running from the project directory:
```bash
cd Mini-Agent
python -m mini_agent.cli
```

## Related Documentation

- [Development Guide](docs/DEVELOPMENT_GUIDE.md) - Detailed development and configuration guidance
- [Production Guide](docs/PRODUCTION_GUIDE.md) - Best practices for production deployment

## Community

Join the MiniMax official community to get help, share ideas, and stay updated:

- **WeChat Group**: Scan the QR code on [Contact Us](https://platform.minimaxi.com/docs/faq/contact-us) page to join

## Contributing

Issues and Pull Requests are welcome!

- [Contributing Guide](CONTRIBUTING.md) - How to contribute
- [Code of Conduct](CODE_OF_CONDUCT.md) - Community guidelines

## License

This project is licensed under the [MIT License](LICENSE).

## References

- MiniMax API: https://platform.minimax.io/docs
- MiniMax-M2: https://github.com/MiniMax-AI/MiniMax-M2
- Anthropic API: https://docs.anthropic.com/claude/reference
- Claude Skills: https://github.com/anthropics/skills
- MCP Servers: https://github.com/modelcontextprotocol/servers

---

**⭐ If this project helps you, please give it a Star!**

```

### File: examples\README.md
```md
# Mini Agent Examples

This directory contains a series of progressive examples to help you understand how to use the Mini Agent framework.

## 📚 Example List

### 01_basic_tools.py - Basic Tool Usage

**Difficulty**: ⭐ Beginner

**Content**:
- How to directly use ReadTool, WriteTool, EditTool, BashTool
- No Agent or LLM involved, pure tool call demonstrations
- Perfect for understanding each tool's basic functionality

**Run**:
```bash
python examples/01_basic_tools.py
```

**Key Learnings**:
- Tool input parameter formats
- ToolResult return structure
- Error handling approaches

---

### 02_simple_agent.py - Simple Agent Usage

**Difficulty**: ⭐⭐ Beginner-Intermediate

**Content**:
- Create the simplest Agent
- Have Agent perform file creation tasks
- Have Agent execute bash command tasks
- Understand Agent execution flow

**Run**:
```bash
# Requires API key configuration first
python examples/02_simple_agent.py
```

**Key Learnings**:
- Agent initialization process
- How to give tasks to Agent
- How Agent autonomously selects tools
- Task completion criteria

**Prerequisites**:
- API key configured in `mini_agent/config/config.yaml`

---

### 03_session_notes.py - Session Note Tool

**Difficulty**: ⭐⭐⭐ Intermediate

**Content**:
- Direct usage of Session Note tools (record_note, recall_notes)
- Agent using Session Notes to maintain cross-session memory
- Demonstrate how two Agent instances share memory

**Run**:
```bash
python examples/03_session_notes.py
```

**Key Learnings**:
- How Session Notes work
- Note categorization management (category)
- How to guide Agent to use notes in system prompt
- Cross-session memory implementation

**Highlight**:
This is one of the core features of this project! Shows a lightweight but effective session memory management solution.

---

### 04_full_agent.py - Full-Featured Agent

**Difficulty**: ⭐⭐⭐⭐ Advanced

**Content**:
- Complete Agent setup with all features
- Integration of basic tools + Session Notes + MCP tools
- Full execution flow for complex tasks
- Multi-turn conversation examples

**Run**:
```bash
python examples/04_full_agent.py
```

**Key Learnings**:
- How to combine multiple tools
- MCP tool loading and usage
- Complex task decomposition and execution
- Production environment Agent configuration

**Prerequisites**:
- API key configured
- (Optional) MCP tools configured

---

## 🚀 Quick Start

### 1. Configure API Key

```bash
# Copy configuration template
cp mini_agent/config/config-example.yaml mini_agent/config/config.yaml

# Edit config file and fill in your MiniMax API Key
vim mini_agent/config/config.yaml
```

### 2. Run Your First Example

```bash
# Example that doesn't need API key
python examples/01_basic_tools.py

# Example that needs API key
python examples/02_simple_agent.py
```

### 3. Progressive Learning

Recommended to learn in numerical order:
1. **01_basic_tools.py** - Understand tools
2. **02_simple_agent.py** - Understand Agent
3. **03_session_notes.py** - Understand memory management
4. **04_full_agent.py** - Understand complete system

---

## 📖 Relationship with Test Cases

These examples are all refined from test cases in the `tests/` directory:

| Example             | Based on Test                                        | Description                     |
| ------------------- | ---------------------------------------------------- | ------------------------------- |
| 01_basic_tools.py   | tests/test_tools.py                                  | Basic tool unit tests           |
| 02_simple_agent.py  | tests/test_agent.py                                  | Agent basic functionality tests |
| 03_session_notes.py | tests/test_note_tool.py<br>tests/test_integration.py | Session Note tool tests         |
| 04_full_agent.py    | tests/test_integration.py                            | Complete integration tests      |

---

## 💡 Recommended Learning Paths

### Path 1: Quick Start
1. Run `01_basic_tools.py` - Learn about tools
2. Run `02_simple_agent.py` - Run your first Agent
3. Go directly to interactive mode with `mini-agent`

### Path 2: Deep Understanding
1. Read and run all examples (01 → 04)
2. Read corresponding test cases (`tests/`)
3. Read core implementation code (`mini_agent/`)
4. Try modifying examples to implement your own features

### Path 3: Production Application
1. Understand all examples
2. Read [Production Deployment Guide](../docs/PRODUCTION_GUIDE.md)
3. Configure MCP tools and Skills
4. Extend tool set based on needs

---

## 🔧 Troubleshooting

### API Key Error
```
❌ API key not configured in config.yaml
```
**Solution**: Ensure you've configured a valid MiniMax API Key in `mini_agent/config/config.yaml`

### config.yaml Not Found
```
❌ config.yaml not found
```
**Solution**:
```bash
cp mini_agent/config/config-example.yaml mini_agent/config/config.yaml
```

### MCP Tools Loading Failed
```
⚠️ MCP tools not loaded: [error message]
```
**Solution**: MCP tools are optional and don't affect basic functionality. If you need them, refer to the MCP configuration section in the main README.

---

## 📚 More Resources

- [Main Project README](../README.md) - Complete project documentation
- [Test Cases](../tests/) - More usage examples
- [Core Implementation](../mini_agent/) - Source code
- [Production Guide](../docs/PRODUCTION_GUIDE.md) - Deployment guide

---

## 🤝 Contributing Examples

If you have good usage examples, PRs are welcome!

Suggested new example directions:
- Web search integration examples (using MiniMax Search MCP)
- Skills usage examples (document processing, design, etc.)
- Custom tool development examples
- Error handling and retry mechanism examples

---

**⭐ If these examples help you, please give the project a Star!**

```

### File: CODE_OF_CONDUCT.md
```md
# Code of Conduct

## Our Pledge

In the interest of fostering an open and welcoming environment, we as contributors and maintainers pledge to making participation in our project and our community a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, education, socio-economic status, nationality, personal appearance, race, religion, or sexual identity and orientation.

## Our Standards

Examples of behavior that contributes to creating a positive environment include:

- Using welcoming and inclusive language
- Being respectful of differing viewpoints and experiences
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

- The use of sexualized language or imagery and unwelcome sexual attention or advances
- Trolling, insulting/derogatory comments, and personal or political attacks
- Public or private harassment
- Publishing others' private information, such as a physical or electronic address, without explicit permission
- Other conduct which could reasonably be considered inappropriate in a professional setting

## Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable behavior and are expected to take appropriate and fair corrective action in response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or reject comments, commits, code, wiki edits, issues, and other contributions that are not aligned to this Code of Conduct, or to ban temporarily or permanently any contributor for other behaviors that they deem inappropriate, threatening, offensive, or harmful.

## Scope

This Code of Conduct applies within all project spaces, and it also applies when an individual is representing the project or its community in public spaces. Examples of representing a project or community include using an official project e-mail address, posting via an official social media account, or acting as an appointed representative at an online or offline event. Representation of a project may be further defined and clarified by project maintainers.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be reported by contacting the project team. All complaints will be reviewed and investigated and will result in a response that is deemed necessary and appropriate to the circumstances. The project team is obligated to maintain confidentiality with regard to the reporter of an incident. Further details of specific enforcement policies may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good faith may face temporary or permanent repercussions as determined by other members of the project's leadership.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant](https://www.contributor-covenant.org), version 2.0, available at https://www.contributor-covenant.org/version/2/0/code_of_conduct.html.

For answers to common questions about this code of conduct, see https://www.contributor-covenant.org/faq. Translations are available at https://www.contributor-covenant.org/translations.

```

### File: CODE_OF_CONDUCT_CN.md
```md
# 行为准则

## 我们的承诺

为了营造开放和友好的环境，我们作为贡献者和维护者承诺：无论年龄、体型、残疾、种族、性别认同和表达、经验水平、教育程度、社会经济地位、国籍、外貌、种族、宗教或性取向如何，参与我们的项目和社区的每个人都不会受到骚扰。

## 我们的标准

有助于创建积极环境的行为包括：

- 使用友好和包容的语言
- 尊重不同的观点和经验
- 优雅地接受建设性批评
- 专注于对社区最有利的事情
- 对其他社区成员表示同理心

不可接受的行为包括：

- 使用性暗示的语言或图像，以及不受欢迎的性关注或挑逗
- 发表侮辱性/贬损性评论，进行人身攻击或政治攻击
- 公开或私下骚扰
- 未经明确许可，发布他人的私人信息（如地址、电子邮件地址）
- 在专业环境中可被合理认为不适当的其他行为

## 我们的责任

项目维护者有责任澄清可接受行为的标准，并应对任何不可接受的行为采取适当和公平的纠正措施。

项目维护者有权利和责任删除、编辑或拒绝不符合本行为准则的评论、提交、代码、wiki 编辑、问题和其他贡献，或暂时或永久禁止任何他们认为有不适当、威胁、冒犯或有害行为的贡献者。

## 范围

本行为准则适用于项目空间和公共空间，当个人代表项目或其社区时。代表项目或社区的示例包括：使用官方项目电子邮件地址、通过官方社交媒体账户发帖，或在在线或离线活动中担任指定代表。项目维护者可以进一步定义和阐明项目的代表性。

## 执行

可以通过联系项目团队来报告滥用、骚扰或其他不可接受的行为。所有投诉都将被审查和调查，并将做出被认为必要和适当的回应。项目团队有义务对事件报告者保密。具体执行政策的更多细节可能会单独发布。

不善意遵守或执行行为准则的项目维护者可能会面临项目领导层其他成员决定的临时或永久性后果。

## 归属

本行为准则改编自 [Contributor Covenant](https://www.contributor-covenant.org/) 2.0 版本，可在 https://www.contributor-covenant.org/version/2/0/code_of_conduct.html 获取。

社区影响指南受到 [Mozilla 的行为准则执行阶梯](https://github.com/mozilla/diversity)的启发。

有关本行为准则的常见问题的答案，请参阅 https://www.contributor-covenant.org/faq。翻译版本可在 https://www.contributor-covenant.org/translations 获取。


```

### File: CONTRIBUTING.md
```md
# Contributing Guide

Thank you for your interest in the Mini Agent project! We welcome contributions of all forms.

## How to Contribute

### Reporting Bugs

If you find a bug, please create an Issue and include the following information:

- **Problem Description**: A clear description of the problem.
- **Steps to Reproduce**: Detailed steps to reproduce the issue.
- **Expected Behavior**: What you expected to happen.
- **Actual Behavior**: What actually happened.
- **Environment Information**:
  - Python version
  - Operating system
  - Versions of relevant dependencies

### Suggesting New Features

If you have an idea for a new feature, please create an Issue first to discuss it:

- Describe the purpose and value of the feature.
- Explain the intended use case.
- Provide a design proposal if possible.

### Submitting Code

#### Getting Started

1. Fork this repository.
2. Clone your fork:
   ```bash
   git clone https://github.com/MiniMax-AI/Mini-Agent mini-agent
   cd mini-agent
   ```

3. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/your-bug-fix
   ```

4. Install development dependencies:
   ```bash
   uv sync
   ```

#### Development Process

1. **Write Code**
   - Follow the project's code style (see the [Development Guide](docs/DEVELOPMENT.md#code-style-guide)).
   - Add necessary comments and docstrings.
   - Keep your code clean and concise.

2. **Add Tests**
   - Add test cases for new features.
   - Ensure all tests pass:
     ```bash
     pytest tests/ -v
     ```

3. **Update Documentation**
   - If you add a new feature, update the README or relevant documentation.
   - Keep documentation in sync with your code.

4. **Commit Changes**
   - Use clear commit messages:
     ```bash
     git commit -m "feat(tools): Add new file search tool"
     # or
     git commit -m "fix(agent): Fix error handling for tool calls"
     ```
   
   - Commit message format:
     - `feat`: A new feature
     - `fix`: A bug fix
     - `docs`: Documentation updates
     - `style`: Code style adjustments
     - `refactor`: Code refactoring
     - `test`: Test-related changes
     - `chore`: Build or auxiliary tools

5. **Push to Your Fork**
   ```bash
   git push origin feature/your-feature-name
   ```

6. **Create a Pull Request**
   - Create a Pull Request on GitHub.
   - Clearly describe your changes.
   - Reference any related Issues if applicable.

#### Pull Request Checklist

Before submitting a PR, please ensure:

- [ ] The code follows the project's style guide.
- [ ] All tests pass.
- [ ] Necessary tests have been added.
- [ ] Relevant documentation has been updated.
- [ ] The commit message is clear and concise.
- [ ] There are no unrelated changes.

### Code Review

All Pull Requests will be reviewed:

- We will review your code as soon as possible.
- We may request some changes.
- Please be patient and responsive to feedback.
- Once approved, your PR will be merged into the main branch.

## Code Style Guide

### Python Code Style

Follow PEP 8 and the Google Python Style Guide:

```python
# Good example ✅
class MyClass:
    """A brief description of the class.
    
    A more detailed description...
    """
    
    def my_method(self, param1: str, param2: int = 10) -> str:
        """A brief description of the method.
        
        Args:
            param1: Description of parameter 1.
            param2: Description of parameter 2.
        
        Returns:
            Description of the return value.
        """
        pass

# Bad example ❌
class myclass:  # Class names should be PascalCase
    def MyMethod(self,param1,param2=10):  # Method names should be snake_case
        pass  # Missing docstring
```

### Type Hinting

Use Python type hints:

```python
from typing import List, Dict, Optional, Any

async def process_messages(
    messages: List[Dict[str, Any]],
    max_tokens: Optional[int] = None
) -> str:
    """Process a list of messages."""
    pass
```

### Testing

- Write tests for new features.
- Keep tests simple and clear.
- Ensure tests cover critical paths.

```python
import pytest
from mini_agent.tools.my_tool import MyTool

@pytest.mark.asyncio
async def test_my_tool():
    """Test the custom tool."""
    tool = MyTool()
    result = await tool.execute(param="test")
    assert result.success
    assert "expected" in result.content
```

## Community Guidelines

Please follow our [Code of Conduct](CODE_OF_CONDUCT.md) and be friendly and respectful.

## Questions and Help

If you have any questions:

- Check the [README](README.md) and [documentation](docs/).
- Search existing Issues.
- Create a new Issue to ask a question.

## License

By contributing, you agree that your contributions will be licensed under the [MIT License](LICENSE).

---

Thank you again for your contribution! 🎉

```

### File: CONTRIBUTING_CN.md
```md
# 贡献指南

感谢你对 Mini Agent 项目的兴趣！我们欢迎各种形式的贡献。

## 如何贡献

### 报告 Bug

如果你发现了 bug，请创建一个 Issue 并包含以下信息：

- **问题描述**：清晰描述问题
- **复现步骤**：详细的复现步骤
- **预期行为**：你期望发生什么
- **实际行为**：实际发生了什么
- **环境信息**：
  - Python 版本
  - 操作系统
  - 相关依赖版本

### 提出新功能

如果你有新功能的想法，请先创建一个 Issue 讨论：

- 描述功能的用途和价值
- 说明预期的使用场景
- 如果可能，提供设计思路

### 提交代码

#### 准备工作

1. Fork 本仓库
2. 克隆你的 fork：
   ```bash
   git clone https://github.com/MiniMax-AI/Mini-Agent mini-agent
   cd mini-agent
   ```

3. 创建新分支：
   ```bash
   git checkout -b feature/your-feature-name
   # 或
   git checkout -b fix/your-bug-fix
   ```

4. 安装开发依赖：
   ```bash
   uv sync
   ```

#### 开发流程

1. **编写代码**
   - 遵循项目的代码风格（参考 [开发指南](docs/DEVELOPMENT.md#代码规范)）
   - 添加必要的注释和文档字符串
   - 保持代码简洁清晰

2. **添加测试**
   - 为新功能添加测试用例
   - 确保所有测试通过：
     ```bash
     pytest tests/ -v
     ```

3. **更新文档**
   - 如果添加了新功能，更新 README 或相关文档
   - 保持文档与代码同步

4. **提交更改**
   - 使用清晰的提交消息：
     ```bash
     git commit -m "feat(tools): 添加新的文件搜索工具"
     # 或
     git commit -m "fix(agent): 修复工具调用错误处理"
     ```
   
   - 提交消息格式：
     - `feat`: 新功能
     - `fix`: Bug 修复
     - `docs`: 文档更新
     - `style`: 代码格式调整
     - `refactor`: 代码重构
     - `test`: 测试相关
     - `chore`: 构建或辅助工具

5. **推送到你的 fork**
   ```bash
   git push origin feature/your-feature-name
   ```

6. **创建 Pull Request**
   - 在 GitHub 上创建 Pull Request
   - 清楚描述你的更改
   - 引用相关的 Issue（如果有）

#### Pull Request 检查清单

在提交 PR 之前，请确保：

- [ ] 代码遵循项目规范
- [ ] 所有测试通过
- [ ] 添加了必要的测试
- [ ] 更新了相关文档
- [ ] 提交消息清晰明确
- [ ] 没有不相关的更改

### 代码审查

所有 Pull Request 需要经过代码审查：

- 我们会尽快审查你的代码
- 可能会要求一些修改
- 请保持耐心并及时响应反馈
- 审查通过后会被合并到主分支

## 代码规范

### Python 代码风格

遵循 PEP 8 和 Google Python Style Guide：

```python
# 好的示例 ✅
class MyClass:
    """类的简短描述。
    
    详细描述...
    """
    
    def my_method(self, param1: str, param2: int = 10) -> str:
        """方法的简短描述。
        
        Args:
            param1: 参数1的描述
            param2: 参数2的描述
        
        Returns:
            返回值的描述
        """
        pass

# 不好的示例 ❌
class myclass:  # 类名应该用 PascalCase
    def MyMethod(self,param1,param2=10):  # 方法名应该用 snake_case
        pass  # 缺少 docstring
```

### 类型注解

使用 Python 类型注解：

```python
from typing import List, Dict, Optional

async def process_messages(
    messages: List[Dict[str, Any]],
    max_tokens: Optional[int] = None
) -> str:
    """处理消息列表"""
    pass
```

### 测试

- 为新功能编写测试
- 保持测试简单清晰
- 测试覆盖关键路径

```python
import pytest
from mini_agent.tools.my_tool import MyTool

@pytest.mark.asyncio
async def test_my_tool():
    """测试自定义工具"""
    tool = MyTool()
    result = await tool.execute(param="test")
    assert result.success
    assert "expected" in result.content
```

## 社区准则

请遵守我们的[行为准则](CODE_OF_CONDUCT.md)，保持友好和尊重。

## 问题和帮助

如果有任何问题：

- 查看 [README](README.md) 和 [文档](docs/)
- 搜索现有的 Issues
- 创建新的 Issue 提问

## 许可证

提交代码即表示你同意将代码以 [MIT License](LICENSE) 发布。

---

再次感谢你的贡献！ 🎉


```

### File: README_CN.md
```md
# Mini Agent

[English](./README.md) | 中文

**Mini Agent** 是一个极简但专业的演示项目，旨在展示使用 MiniMax M2.5 模型构建 Agent 的最佳实践。项目通过兼容 Anthropic 的 API，完全支持交错思维（interleaved thinking），从而解锁 M2 模型在处理长而复杂的任务时强大的推理能力。

该项目具备一系列为稳健、智能的 Agent 开发而设计的特性：

*   ✅ **完整的 Agent 执行循环**：一个完整可靠的执行框架，配备了文件系统和 Shell 操作的基础工具集。
*   ✅ **持久化记忆**：通过内置的 **Session Note Tool**，Agent 能够在多个会话中保留关键信息。
*   ✅ **智能上下文管理**：自动对会话历史进行摘要，可处理长达可配置 Token 上限的上下文，从而支持无限长的任务。
*   ✅ **集成 Claude Skills**：内置 15 种专业技能，涵盖文档处理、设计、测试和开发等领域。
*   ✅ **集成 MCP 工具**：原生支持 MCP 协议，可轻松接入知识图谱、网页搜索等工具。
*   ✅ **全面的日志记录**：为每个请求、响应和工具执行提供详细日志，便于调试。
*   ✅ **简洁明了的设计**：美观的命令行界面和易于理解的代码库，使其成为构建高级 Agent 的理想起点。

## 目录

- [Mini Agent](#mini-agent)
  - [目录](#目录)
  - [快速开始](#快速开始)
    - [1. 获取 API Key](#1-获取-api-key)
    - [2. 选择使用模式](#2-选择使用模式)
      - [🚀 快速上手模式（推荐新手）](#-快速上手模式推荐新手)
      - [🔧 开发模式](#-开发模式)
  - [ACP \& Zed Editor 集成（可选）](#acp--zed-editor-集成可选)
  - [使用示例](#使用示例)
    - [任务执行](#任务执行)
    - [使用 Claude Skill（例如：PDF 生成）](#使用-claude-skill例如pdf-生成)
    - [网页搜索与摘要（MCP 工具）](#网页搜索与摘要mcp-工具)
  - [测试](#测试)
    - [快速运行](#快速运行)
    - [测试覆盖范围](#测试覆盖范围)
  - [常见问题](#常见问题)
    - [SSL 证书错误](#ssl-证书错误)
    - [模块未找到错误](#模块未找到错误)
  - [相关文档](#相关文档)
  - [社区](#社区)
  - [贡献](#贡献)
  - [许可证](#许可证)
  - [参考资源](#参考资源)

## 快速开始

### 1. 获取 API Key

MiniMax 提供国内和海外两个平台，请根据您的网络环境选择：

| 版本       | 平台地址                                                       | API Base                   |
| ---------- | -------------------------------------------------------------- | -------------------------- |
| **国内版** | [https://platform.minimaxi.com](https://platform.minimaxi.com) | `https://api.minimaxi.com` |
| **海外版** | [https://platform.minimax.io](https://platform.minimax.io)     | `https://api.minimax.io`   |

**获取步骤：**
1. 访问相应平台注册并登录
2. 进入 **账户管理 > API 密钥**
3. 点击 **"创建新密钥"**
4. 复制并妥善保存（密钥仅显示一次）

> 💡 **提示**：请记住您所选平台对应的 API Base 地址，后续配置时会用到。

### 2. 选择使用模式

**前置要求：安装 uv**

两种使用模式都需要 uv。如果您尚未安装：

```bash
# macOS/Linux/WSL
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
python -m pip install --user pipx
python -m pipx ensurepath
# 安装后需要重启 PowerShell

# 安装完成后，重启终端或运行：
source ~/.bashrc  # 或 ~/.zshrc (macOS/Linux)
```

我们提供两种使用模式，请根据您的需求选择：

#### 🚀 快速上手模式（推荐新手）

此模式适合希望快速体验 Mini Agent，而无需克隆代码仓库或修改代码的用户。

**安装步骤：**

```bash
# 1. 直接从 GitHub 安装
uv tool install git+https://github.com/MiniMax-AI/Mini-Agent.git

# 2. 运行配置脚本（自动创建配置文件）
# macOS/Linux:
curl -fsSL https://raw.githubusercontent.com/MiniMax-AI/Mini-Agent/main/scripts/setup-config.sh | bash

# Windows (PowerShell):
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/MiniMax-AI/Mini-Agent/main/scripts/setup-config.ps1" -OutFile "$env:TEMP\setup-config.ps1"
powershell -ExecutionPolicy Bypass -File "$env:TEMP\setup-config.ps1"
```

> 💡 **提示**：如果您希望在本地进行开发或修改代码，请使用下方的"开发模式"。

**配置步骤：**

配置脚本会在 `~/.mini-agent/config/` 目录下创建配置文件，请编辑该文件：

```bash
# 编辑配置文件
nano ~/.mini-agent/config/config.yaml
```

填入您的 API Key 和对应的 API Base：

```yaml
api_key: "YOUR_API_KEY_HERE"          # 填入第 1 步获取的 API Key
api_base: "https://api.minimaxi.com"  # 国内版
# api_base: "https://api.minimax.io"  # 海外版（如使用海外平台，请取消本行注释）
model: "MiniMax-M2.5"
```

**开始使用：**

```bash
mini-agent                                    # 使用当前目录作为工作空间
mini-agent --workspace /path/to/your/project  # 指定工作空间目录
mini-agent --version                          # 查看版本信息

# 管理命令
uv tool upgrade mini-agent                    # 升级到最新版本
uv tool uninstall mini-agent                  # 卸载工具（如需要）
uv tool list                                  # 查看所有已安装的工具
```

#### 🔧 开发模式

此模式适合需要修改代码、添加功能或进行调试的开发者。

**安装与配置步骤：**

```bash
# 1. 克隆仓库
git clone https://github.com/MiniMax-AI/Mini-Agent.git
cd Mini-Agent

# 2. 安装 uv（如果尚未安装）
# macOS/Linux:
curl -LsSf https://astral.sh/uv/install.sh | sh
# Windows (PowerShell):
irm https://astral.sh/uv/install.ps1 | iex
# 安装后需要重启终端

# 3. 同步依赖
uv sync

# 替代方案: 手动安装依赖（如果不使用 uv）
# pip install -r requirements.txt
# 或者安装必需的包:
# pip install tiktoken pyyaml httpx pydantic requests prompt-toolkit mcp

# 4. 初始化 Claude Skills（可选）
git submodule update --init --recursive

# 5. 复制配置模板
```

**macOS/Linux:**
```bash
cp mini_agent/config/config-example.yaml mini_agent/config/config.yaml
```

**Windows:**
```powershell
Copy-Item mini_agent\config\config-example.yaml mini_agent\config\config.yaml

# 6. 编辑配置文件
vim mini_agent/config/config.yaml  # 或使用您偏好的编辑器
```

填入您的 API Key 和对应的 API Base：

```yaml
api_key: "YOUR_API_KEY_HERE"          # 填入第 1 步获取的 API Key
api_base: "https://api.minimaxi.com"  # 国内版
# api_base: "https://api.minimax.io"  # 海外版（如使用海外平台，请修改此行）
model: "MiniMax-M2.5"
max_steps: 100
workspace_dir: "./workspace"
```

> 📖 完整的配置指南，请参阅 [config-example.yaml](mini_agent/config/config-example.yaml)

**运行方式：**

选择您偏好的方式运行：

```bash
# 方式 1：作为模块直接运行（适合调试）
uv run python -m mini_agent.cli

# 方式 2：以可编辑模式安装（推荐）
uv tool install -e .
# 安装后，您可以在任何路径下运行，且代码更改会立即生效
mini-agent
mini-agent --workspace /path/to/your/project
```

> 📖 更多开发指引，请参阅 [开发指南](docs/DEVELOPMENT_GUIDE_CN.md)

> 📖 更多生产部署指引，请参阅 [生产指南](docs/PRODUCTION_GUIDE_CN.md)

## ACP & Zed Editor 集成（可选）

Mini Agent 支持 [Agent Communication Protocol (ACP)](https://github.com/modelcontextprotocol/protocol)，可与 Zed 等代码编辑器集成。

**在 Zed Editor 中设置：**

1. 以开发模式或工具模式安装 Mini Agent
2. 在您的 Zed `settings.json` 中添加：

```json
{
  "agent_servers": {
    "mini-agent": {
      "command": "/path/to/mini-agent-acp"
    }
  }
}
```

命令路径应为：
- 通过 `uv tool install` 安装：使用 `which mini-agent-acp` 的输出结果
- 开发模式：`./mini_agent/acp/server.py`

**使用方法：**
- 使用 `Ctrl+Shift+P` → "Agent: Toggle Panel" 打开 Zed 的 Agent 面板
- 从 Agent 下拉列表中选择 "mini-agent"
- 直接在编辑器中开始与 Mini Agent 对话

## 使用示例

这里有几个 Mini Agent 能力的演示。

### 任务执行

*在这个演示中，我们要求 Agent 创建一个简洁美观的网页并在浏览器中显示它，以此展示基础的工具使用循环。*

![演示动图 1: 基础任务执行](docs/assets/demo1-task-execution.gif "基础任务执行演示")

### 使用 Claude Skill（例如：PDF 生成）

*这里，Agent 利用 Claude Skill 根据用户请求创建专业文档（如 PDF 或 DOCX），展示了其强大的高级能力。*

![演示动图 2: Claude Skill 使用](docs/assets/demo2-claude-skill.gif "Claude Skill 使用演示")

### 网页搜索与摘要（MCP 工具）

*此演示展示了 Agent 如何使用其网页搜索工具在线查找最新信息，并为用户进行总结。*

![演示动图 3: 网页搜索](docs/assets/demo3-web-search.gif "网页搜索演示")


## 测试

项目包含了覆盖单元测试、功能测试和集成测试的全面测试用例。

### 快速运行

```bash
# 运行所有测试
pytest tests/ -v

# 仅运行核心功能测试
pytest tests/test_agent.py tests/test_note_tool.py -v
```

### 测试覆盖范围

- ✅ **单元测试** - 工具类、LLM 客户端
- ✅ **功能测试** - Session Note Tool、MCP 加载
- ✅ **集成测试** - Agent 端到端执行
- ✅ **外部服务** - Git MCP 服务器加载


## 常见问题

### SSL 证书错误

如果遇到 `[SSL: CERTIFICATE_VERIFY_FAILED]` 错误:

**测试环境快速修复** (修改 `mini_agent/llm.py`):
```python
# 第 50 行: 给 AsyncClient 添加 verify=False
async with httpx.AsyncClient(timeout=120.0, verify=False) as client:
```

**生产环境解决方案**:
```bash
# 更新证书
pip install --upgrade certifi

# 或配置系统代理/证书
```

### 模块未找到错误

确保从项目目录运行:
```bash
cd Mini-Agent
python -m mini_agent.cli
```

## 相关文档

- [开发指南](docs/DEVELOPMENT_GUIDE_CN.md) - 详细的开发和配置指引
- [生产环境指南](docs/PRODUCTION_GUIDE_CN.md) - 生产部署最佳实践

## 社区

加入 MiniMax 官方社区，获取帮助、分享想法、了解最新动态：

- **微信交流群**：扫描 [联系我们](https://platform.minimaxi.com/docs/faq/contact-us) 页面的二维码加入官方交流群

## 贡献

我们欢迎并鼓励您提交 Issue 和 Pull Request！

- [贡献指南](CONTRIBUTING.md) - 如何为项目做贡献
- [行为准则](CODE_OF_CONDUCT.md) - 社区行为准则

## 许可证

本项目采用 [MIT 许可证](LICENSE) 授权。

## 参考资源

- MiniMax API: https://platform.minimaxi.com/docs
- MiniMax-M2: https://github.com/MiniMax-AI/MiniMax-M2
- Anthropic API: https://docs.anthropic.com/claude/reference
- Claude Skills: https://github.com/anthropics/skills
- MCP Servers: https://github.com/modelcontextprotocol/servers

---

**⭐ 如果这个项目对您有帮助，请给它一个 Star！**

```

### File: docs\DEVELOPMENT_GUIDE.md
```md
# Development Guide

## Table of Contents

- [Development Guide](#development-guide)
  - [Table of Contents](#table-of-contents)
  - [1. Project Architecture](#1-project-architecture)
  - [2. Basic Usage](#2-basic-usage)
    - [2.1 Interactive Commands](#21-interactive-commands)
    - [2.2 Integrated MCP Tools](#22-integrated-mcp-tools)
      - [Memory - Knowledge Graph Memory System](#memory---knowledge-graph-memory-system)
      - [MiniMax Search - Web Search and Browse](#minimax-search---web-search-and-browse)
  - [3. Extended Abilities](#3-extended-abilities)
    - [3.1 Adding Custom Tools](#31-adding-custom-tools)
      - [Steps](#steps)
      - [Example](#example)
    - [3.2 Adding MCP Tools](#32-adding-mcp-tools)
    - [3.3 Customizing Note Storage](#33-customizing-note-storage)
    - [3.4 Initialize Claude Skills (Recommended)](#34-initialize-claude-skills-recommended)
    - [3.5 Adding a New Skill](#35-adding-a-new-skill)
    - [3.6 Customizing System Prompt](#36-customizing-system-prompt)
      - [What You Can Customize](#what-you-can-customize)
  - [4. Troubleshooting](#4-troubleshooting)
    - [4.1 Common Issues](#41-common-issues)
      - [API Key Configuration Error](#api-key-configuration-error)
      - [Dependency Installation Failure](#dependency-installation-failure)
      - [MCP Tool Loading Failure](#mcp-tool-loading-failure)
    - [4.2 Debugging Tips](#42-debugging-tips)
      - [Enable Verbose Logging](#enable-verbose-logging)
      - [Using the Python Debugger](#using-the-python-debugger)
      - [Inspecting Tool Calls](#inspecting-tool-calls)

---

## 1. Project Architecture

```
mini-agent/
├── mini_agent/              # Core source code
│   ├── agent.py             # Main agent loop
│   ├── llm.py               # LLM client
│   ├── cli.py               # Command-line interface
│   ├── config.py            # Configuration loading
│   ├── tools/               # Tool implementations (file, bash, MCP, skills, etc.)
│   └── skills/              # Claude Skills (submodule)
├── tests/                   # Test code
├── docs/                    # Documentation
├── workspace/               # Working directory
└── pyproject.toml           # Project configuration
```

## 2. Basic Usage

### 2.1 Interactive Commands

When running the agent in interactive mode (`mini-agent`), the following commands are available:

| Command                | Description                                                 |
| ---------------------- | ----------------------------------------------------------- |
| `/exit`, `/quit`, `/q` | Exit the agent and display session statistics               |
| `/help`                | Display help information and available commands             |
| `/clear`               | Clear message history and start a new session               |
| `/history`             | Show the current session message count                      |
| `/stats`               | Display session statistics (steps, tool calls, tokens used) |

### 2.2 Integrated MCP Tools

This project comes with pre-configured MCP (Model Context Protocol) tools that extend the agent's capabilities:

#### Memory - Knowledge Graph Memory System

**Function**: Provides long-term memory storage and retrieval based on graph database

**Status**: Enabled by default (`disabled: false`)

**Configuration**: No API Key required, works out of the box

**Capabilities**:
- Store and retrieve information across sessions
- Build knowledge graphs from conversations
- Semantic search through stored memories

---

#### MiniMax Search - Web Search and Browse

**Function**: Provides three powerful tools:
- `search` - Web search capability
- `parallel_search` - Execute multiple searches simultaneously
- `browse` - Intelligent web browsing and content extraction

**Status**: Disabled by default, needs configuration to enable

**Configuration Example**

```json
{
  "mcpServers": {
    "minimax_search": {
      "disabled": false,
      "env": {
        "JINA_API_KEY": "your-jina-api-key",
        "SERPER_API_KEY": "your-serper-api-key",
        "MINIMAX_TOKEN": "your-minimax-token"
      }
    }
  }
}
```

## 3. Extended Abilities

### 3.1 Adding Custom Tools

#### Steps

1.  Create a new tool file under `mini_agent/tools/`.
2.  Inherit from the `Tool` base class.
3.  Implement the required properties and methods.
4.  Register the tool during Agent initialization.

#### Example

```python
# mini_agent/tools/my_tool.py
from mini_agent.tools.base import Tool, ToolResult
from typing import Dict, Any

class MyTool(Tool):
    @property
    def name(self) -> str:
        """A unique name for the tool."""
        return "my_tool"
    
    @property
    def description(self) -> str:
        """A description for the LLM to understand the tool's purpose."""
        return "My custom tool for doing something useful"
    
    @property
    def parameters(self) -> Dict[str, Any]:
        """Parameter schema in JSON Schema format."""
        return {
            "type": "object",
            "properties": {
                "param1": {
                    "type": "string",
                    "description": "First parameter"
                },
                "param2": {
                    "type": "integer",
                    "description": "Second parameter",
                    "default": 10
                }
            },
            "required": ["param1"]
        }
    
    async def execute(self, param1: str, param2: int = 10) -> ToolResult:
        """
        The main logic of the tool.
        
        Args:
            param1: The first parameter.
            param2: The second parameter, with a default value.
        
        Returns:
            A ToolResult object.
        """
        try:
            # Implement your logic here
            result = f"Processed {param1} with param2={param2}"
            
            return ToolResult(
                success=True,
                content=result
            )
        except Exception as e:
            return ToolResult(
                success=False,
                content=f"Error: {str(e)}"
            )

# In cli.py or agent initialization code
from mini_agent.tools.my_tool import MyTool

# Add the new tool when creating the Agent
tools = [
    ReadTool(workspace_dir),
    WriteTool(workspace_dir),
    MyTool(),  # Add your custom tool
]

agent = Agent(
    llm=llm,
    tools=tools,
    max_steps=50
)
```

### 3.2 Adding MCP Tools

Edit `mcp.json` to add a new MCP Server:

```json
{
  "mcpServers": {
    "my_custom_mcp": {
      "description": "My custom MCP server",
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@my-org/my-mcp-server"],
      "env": {
        "API_KEY": "your-api-key"
      },
      "disabled": false,
      "notes": {
        "description": "This is a custom MCP server.",
        "api_key_url": "https://example.com/api-keys"
      }
    }
  }
}
```

### 3.3 Customizing Note Storage

To replace the storage backend for the `SessionNoteTool`:

```python
# Current implementation: JSON file
class SessionNoteTool:
    def __init__(self, memory_file: str = "./workspace/.agent_memory.json"):
        self.memory_file = Path(memory_file)
    
    async def _save_notes(self, notes: List[Dict]):
        with open(self.memory_file, 'w') as f:
            json.dump(notes, f, indent=2, ensure_ascii=False)

# Example extension: PostgreSQL
class PostgresNoteTool(Tool):
    def __init__(self, db_url: str):
        self.db = PostgresDB(db_url)
    
    async def _save_notes(self, notes: List[Dict]):
        await self.db.execute(
            "INSERT INTO notes (content, category, timestamp) VALUES ($1, $2, $3)",
            notes
        )

# Example extension: Vector Database
class MilvusNoteTool(Tool):
    def __init__(self, milvus_host: str):
        self.vector_db = MilvusClient(host=milvus_host)
    
    async def _save_notes(self, notes: List[Dict]):
        # Generate embeddings
        embeddings = await self.get_embeddings([n["content"] for n in notes])
        
        # Store in the vector database
        await self.vector_db.insert(
            collection="agent_notes",
            data=notes,
            embeddings=embeddings
        )
```

### 3.4 Initialize Claude Skills (Recommended) 

This project integrates Claude's official skills repository via git submodule. Initialize it after first clone:

```bash
# Initialize submodule
git submodule update --init --recursive
```

Skills provide 20+ professional capabilities, making the Agent work like a professional:

- 📄 **Document Processing**: Create and edit PDF, DOCX, XLSX, PPTX
- 🎨 **Design Creation**: Generate artwork, posters, GIF animations
- 🧪 **Development & Testing**: Web automation testing (Playwright), MCP server development
- 🏢 **Enterprise Applications**: Internal communication, brand guidelines, theme customization

✨ **This is one of the core highlights of this project.** For details, see the "Configure Skills" section below.

**More information:**

- [Claude Skills Official Documentation](https://docs.claude.com/zh-CN/docs/agents-and-tools/agent-skills)
- [Anthropic Blog: Equipping agents for the real world](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)

### 3.5 Adding a New Skill

Create a custom Skill:

```bash
# Create a new skill directory under skills/
mkdir skills/my-custom-skill
cd skills/my-custom-skill

# Create the SKILL.md file
cat > SKILL.md << 'EOF'
---
name: my-custom-skill
description: My custom skill for handling specific tasks.
---

# Overview

This skill provides the following capabilities:
- Capability 1
- Capability 2

# Usage

1. Step one...
2. Step two...

# Best Practices

- Practice 1
- Practice 2

# FAQ

Q: Question 1
A: Answer 1
```

The new Skill will be automatically loaded and recognized by the Agent.

### 3.6 Customizing System Prompt

The system prompt (`system_prompt.md`) defines the Agent's behavior, capabilities, and working guidelines. You can customize it to tailor the Agent for specific use cases.

#### What You Can Customize

1. **Core Capabilities**: Add or modify tool descriptions
2. **Working Guidelines**: Define custom workflows and best practices
3. **Domain-Specific Knowledge**: Add expertise in specific areas
4. **Communication Style**: Adjust how the Agent interacts with users
5. **Task Priorities**: Set preferences for how tasks should be approached

After modifying `system_prompt.md`, be sure to restart the Agent to apply changes

## 4. Troubleshooting

### 4.1 Common Issues

#### API Key Configuration Error

```bash
# Error message
Error: Invalid API key

# Solution
1. Check that the API key in `config.yaml` is correct.
2. Ensure there are no extra spaces or quotes.
3. Verify that the API key has not expired.
```

#### Dependency Installation Failure

```bash
# Error message
uv sync failed

# Solution
1. Update uv to the latest version: `uv self update`
2. Clear the cache: `uv cache clean`
3. Try syncing again: `uv sync`
```

#### MCP Tool Loading Failure

```bash
# Error message
Failed to load MCP server

# Solution
1. Check the configuration in `mcp.json` is correct.
2. Ensure Node.js is installed (required for most MCP tools).
3. Verify that any required API keys are configured.
4. View detailed logs: `pytest tests/test_mcp.py -v -s`
```

### 4.2 Debugging Tips

#### Enable Verbose Logging

```python
# At the beginning of cli.py or a test file
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
```

#### Using the Python Debugger

```python
# Set a breakpoint in your code
import pdb; pdb.set_trace()

# Or use ipdb for a better experience
import ipdb; ipdb.set_trace()
```

#### Inspecting Tool Calls

```python
# Add logging in the Agent to see tool interactions
logger.debug(f"Tool call: {tool_call.name}")
logger.debug(f"Tool arguments: {tool_call.arguments}")
logger.debug(f"Tool result: {result.content[:200]}")
```

```

### File: docs\DEVELOPMENT_GUIDE_CN.md
```md
# 开发指南


## 目录

- [开发指南](#开发指南)
  - [目录](#目录)
  - [1. 项目架构](#1-项目架构)
  - [2. 基础使用](#2-基础使用)
    - [2.1 交互式命令](#21-交互式命令)
    - [2.2 已集成的 MCP 工具](#22-已集成的-mcp-工具)
      - [Memory - 知识图谱记忆系统](#memory---知识图谱记忆系统)
      - [MiniMax Search - 网页搜索与浏览](#minimax-search---网页搜索与浏览)
  - [3. 扩展能力](#3-扩展能力)
    - [3.1 添加自定义工具](#31-添加自定义工具)
      - [步骤](#步骤)
      - [示例](#示例)
    - [3.2 添加 MCP 工具](#32-添加-mcp-工具)
    - [3.3 自定义存储](#33-自定义存储)
    - [3.4 初始化 Claude Skills（推荐）](#34-初始化-claude-skills推荐)
    - [3.5 添加新的Skill](#35-添加新的skill)
    - [3.6 自定义系统提示词](#36-自定义系统提示词)
      - [可定制内容包括：](#可定制内容包括)
  - [4. 故障排查](#4-故障排查)
    - [4.1 常见问题](#41-常见问题)
      - [API 密钥配置错误](#api-密钥配置错误)
      - [依赖安装失败](#依赖安装失败)
      - [MCP 工具加载失败](#mcp-工具加载失败)
    - [4.2 调试技巧](#42-调试技巧)
      - [启用 Debug 日志](#启用-debug-日志)
      - [使用 Python 调试器](#使用-python-调试器)
      - [监控工具调用](#监控工具调用)

---

## 1. 项目架构

```
mini-agent/
├── mini_agent/              # 核心源代码
│   ├── agent.py             # 主 Agent 循环
│   ├── llm.py               # LLM 客户端
│   ├── cli.py               # 命令行接口
│   ├── config.py            # 配置加载
│   ├── tools/               # 工具实现（文件、Bash、MCP、技能等）
│   └── skills/              # Claude 技能集（子模块）
├── tests/                   # 测试代码
├── docs/                    # 文档
├── workspace/               # 工作目录
└── pyproject.toml           # 项目配置
```

## 2. 基础使用

### 2.1 交互式命令

在交互模式 (通过 `mini-agent` 启动) 下运行 Agent 时，您可以使用以下命令：

| 命令                   | 说明                                             |
| ---------------------- | ------------------------------------------------ |
| `/exit`, `/quit`, `/q` | 退出 Agent 并显示会话统计信息                    |
| `/help`                | 显示帮助信息和可用命令                           |
| `/clear`               | 清除消息历史并开始新会话                         |
| `/history`             | 显示当前会话的消息数量                           |
| `/stats`               | 显示会话统计信息（步数、工具调用、使用的 Token） |

### 2.2 已集成的 MCP 工具

本项目预先集成了以下 MCP (模型上下文协议) 工具，用以扩展 Agent 的能力：

#### Memory - 知识图谱记忆系统

**功能**：基于图数据库，为 Agent 提供长期记忆的存储与检索能力。

**状态**：默认启用

**配置**：无需 API Key，开箱即用

**能力**：
- 跨会话存储并检索信息
- 根据对话内容构建知识图谱
- 对已存储的记忆进行语义搜索

---

#### MiniMax Search - 网页搜索与浏览

**功能**：提供三大强大工具：
- `search` - 网页搜索
- `parallel_search` - 并行执行多个搜索任务
- `browse` - 智能网页浏览与内容提取

**状态**：默认禁用，需要配置 API Key 后方可启用。

**配置示例**：

```json
{
  "mcpServers": {
    "minimax_search": {
      "disabled": false,
      "env": {
        "JINA_API_KEY": "your-jina-api-key",
        "SERPER_API_KEY": "your-serper-api-key",
        "MINIMAX_API_KEY": "your-minimax-token"
      }
    }
  }
}
```

## 3. 扩展能力

### 3.1 添加自定义工具

#### 步骤

1.  在 `mini_agent/tools/` 目录下创建一个新的 Python 文件。
2.  在文件中定义一个新类，并继承 `Tool` 基类。
3.  在类中实现所需的属性和方法。
4.  在 Agent 初始化时注册你的新工具。

#### 示例

```python
# mini_agent/tools/my_tool.py
from mini_agent.tools.base import Tool, ToolResult
from typing import Dict, Any

class MyTool(Tool):
    @property
    def name(self) -> str:
        """工具的唯一名称，需保持独一无二。"""
        return "my_tool"
    
    @property
    def description(self) -> str:
        """工具用途的详细描述，帮助 LLM 理解其功能。"""
        return "我的自定义工具，用于完成特定任务"
    
    @property
    def parameters(self) -> Dict[str, Any]:
        """参数模式（JSON Schema 格式）。"""
        return {
            "type": "object",
            "properties": {
                "param1": {
                    "type": "string",
                    "description": "第一个参数"
                },
                "param2": {
                    "type": "integer",
                    "description": "第二个参数",
                    "default": 10
                }
            },
            "required": ["param1"]
        }
    
    async def execute(self, param1: str, param2: int = 10) -> ToolResult:
        """
        工具执行的核心逻辑。
        
        Args:
            param1: 参数一。
            param2: 参数二，包含默认值。
        
        Returns:
            返回一个 ToolResult 对象。
        """
        try:
            # 在此实现你的逻辑
            result = f"处理了 {param1}，param2={param2}"
            
            return ToolResult(
                success=True,
                content=result
            )
        except Exception as e:
            return ToolResult(
                success=False,
                content=f"错误: {str(e)}"
            )

# 在 cli.py 或 Agent 的初始化代码中
from mini_agent.tools.my_tool import MyTool

# 创建 Agent 实例时，将新工具加入列表
tools = [
    ReadTool(workspace_dir),
    WriteTool(workspace_dir),
    MyTool(),  # 添加您的自定义工具
]

agent = Agent(
    llm=llm,
    tools=tools,
    max_steps=50
)
```

### 3.2 添加 MCP 工具

编辑 `mcp.json` 文件，即可添加新的 MCP 服务器：

```json
{
  "mcpServers": {
    "my_custom_mcp": {
      "description": "我的自定义 MCP 服务器",
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@my-org/my-mcp-server"],
      "env": {
        "API_KEY": "your-api-key"
      },
      "disabled": false,
      "notes": {
        "description": "这是一个自定义 MCP 服务器。",
        "api_key_url": "https://example.com/api-keys"
      }
    }
  }
}
```

### 3.3 自定义存储

您可以替换 `SessionNoteTool` 的默认存储实现，以对接不同的数据后端：

```python
# 默认实现：JSON 文件
class SessionNoteTool:
    def __init__(self, memory_file: str = "./workspace/.agent_memory.json"):
        self.memory_file = Path(memory_file)
    
    async def _save_notes(self, notes: List[Dict]):
        with open(self.memory_file, 'w') as f:
            json.dump(notes, f, indent=2, ensure_ascii=False)

# 扩展示例：使用 PostgreSQL 存储
class PostgresNoteTool(Tool):
    def __init__(self, db_url: str):
        self.db = PostgresDB(db_url)
    
    async def _save_notes(self, notes: List[Dict]):
        await self.db.execute(
            "INSERT INTO notes (content, category, timestamp) VALUES ($1, $2, $3)",
            notes
        )

# 扩展示例：使用向量数据库存储
class MilvusNoteTool(Tool):
    def __init__(self, milvus_host: str):
        self.vector_db = MilvusClient(host=milvus_host)
    
    async def _save_notes(self, notes: List[Dict]):
        # 生成内容的嵌入向量
        embeddings = await self.get_embeddings([n["content"] for n in notes])
        
        # 将笔记和向量存入向量数据库
        await self.vector_db.insert(
            collection="agent_notes",
            data=notes,
            embeddings=embeddings
        )
```

### 3.4 初始化 Claude Skills（推荐）

本项目通过 Git Submodule 的方式集成了 Claude 官方技能库。首次克隆项目后，请执行以下命令来初始化技能库：

```bash
# 初始化并拉取技能库子模块
git submodule update --init --recursive
```

Skills 库提供了超过20种专业能力，能让 Agent 如同行业专家般处理复杂任务：

- 📄 **文档处理**：轻松创建和编辑 PDF、DOCX、XLSX、PPTX 等格式的文档。
- 🎨 **设计创作**：生成富有创意的艺术作品、海报和 GIF 动画。
- 🧪 **开发与测试**：支持 Web 自动化测试 (Playwright) 和 MCP 服务器开发。
- 🏢 **企业应用**：高效处理内部沟通、品牌指南应用和主题定制等任务。

✨ **这是本项目的核心亮点之一。**

**更多信息：**

- [Claude Skills 官方文档](https://docs.claude.com/zh-CN/docs/agents-and-tools/agent-skills)
- [Anthropic 博客：为真实世界装备智能体](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)

### 3.5 添加新的Skill

您可以按照以下步骤创建自定义 Skill：

```bash
# 在 skills/ 目录下为您的新技能创建一个目录
mkdir skills/my-custom-skill
cd skills/my-custom-skill

# 创建技能描述文件 SKILL.md
cat > SKILL.md << 'EOF'
---
name: my-custom-skill
description: 这是一个自定义技能，用于处理特定任务。
---

# 概述

该技能主要提供以下功能：
- 功能 1
- 功能 2

# 使用方法

1. 第一步...
2. 第二步...

# 最佳实践

- 实践 1
- 实践 2

# 常见问题

问：问题 1
答：答案 1
EOF
```

完成以上步骤后，Agent 将在下次启动时自动加载并识别这项新技能。

### 3.6 自定义系统提示词

系统提示词文件 (`system_prompt.md`) 定义了 Agent 的核心行为、能力边界和工作指南。您可以根据具体应用场景，对其进行深度定制。

#### 可定制内容包括：

1.  **核心能力**：添加或修改工具的描述，以影响 Agent 的工具选择。
2.  **工作指南**：定义特定的工作流程或决策偏好。
3.  **领域专业知识**：注入特定领域的知识，提升 Agent 的专业性。
4.  **沟通风格**：调整 Agent 与用户交互时的语气和风格。
5.  **任务优先级**：设定处理任务时的优先级和策略。

完成修改后，请重启 Agent 以使新配置生效。

## 4. 故障排查

### 4.1 常见问题

#### API 密钥配置错误

```bash
# 错误消息
Error: Invalid API key

# 解决方法
1. 检查 `config.yaml` 文件中的 API 密钥是否填写正确。
2. 确保密钥前后没有多余的空格或引号。
3. 确认该 API 密钥是否仍在有效期内。
```

#### 依赖安装失败

```bash
# 错误消息
uv sync failed

# 解决方法
1. 升级 uv 至最新版本：`uv self update`
2. 清理 uv 缓存：`uv cache clean`
3. 再次尝试同步依赖：`uv sync`
```

#### MCP 工具加载失败

```bash
# 错误消息
Failed to load MCP server

# 解决方法
1. 检查 `mcp.json` 文件中的服务器配置是否正确。
2. 确保您的开发环境已安装 Node.js (大部分 MCP 工具的运行需要)。
3. 确认所需服务的 API 密钥已正确配置。
4. 运行 MCP 测试并查看详细日志：`pytest tests/test_mcp.py -v -s`
```

### 4.2 调试技巧

#### 启用 Debug 日志

```python
# 在 cli.py 或相关测试文件的开头添加以下代码：
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
```

#### 使用 Python 调试器

```python
# 在需要暂停执行的代码行处插入断点：
import pdb; pdb.set_trace()

# 或者使用 ipdb 以获得更佳的调试体验：
import ipdb; ipdb.set_trace()
```

#### 监控工具调用

```python
# 在 Agent 代码中添加日志，以便实时查看工具的调用详情：
logger.debug(f"工具调用: {tool_call.name}")
logger.debug(f"工具参数: {tool_call.arguments}")
logger.debug(f"工具结果: {result.content[:200]}")
```


```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
