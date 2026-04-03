---
id: github.com-dream-num-univer-mcp-de844373-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:45.263809
---

# KNOWLEDGE EXTRACT: github.com_dream-num_univer-mcp_de844373
> **Extracted on:** 2026-04-01 09:39:54
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007520359/github.com_dream-num_univer-mcp_de844373

---

## File: `LICENSE`
```
MIT License

Copyright (c) 2025 DreamNum

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
# Univer MCP

> 🚀 AI-powered spreadsheet automation through Model Context Protocol (MCP)

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-dream--num%2Funiver--mcp-blue)](https://github.com/dream-num/univer-mcp)

## Overview

Univer MCP is a Model Context Protocol (MCP) server that enables AI applications to interact with and automate spreadsheet operations using the powerful [Univer](https://github.com/dream-num/univer) framework. It bridges the gap between AI language models and spreadsheet functionality, allowing for intelligent spreadsheets processing and automation.

> ⚠️ **Early Stage**: Univer MCP is currently in early development. We welcome feedback, suggestions, and collaboration from the community to help shape its future direction.

## Key Features

- **📊 Spreadsheet Operations**: Full support for creating, editing, and manipulating spreadsheets
- **🔧 Extensible Architecture**: Built on Univer's plugin system for custom functionality
- **⚡ High Performance**: Leverages Univer's optimized rendering and calculation engines
- **📦 Advanced Features**: Formulas, conditional formatting, data validation, and more
- **🤖 AI Integration**: Seamless integration with MCP-compatible AI applications
- **📈 Chart Support[WIP]**: Creating and updating charts in spreadsheets
- **🔗 Pivot Table[WIP]**: Creating and updating pivot tables in spreadsheets
- **🌐 Cross-Platform[WIP]**: Works across web browsers and Node.js environments
- **🔄 Real-time Collaboration[WIP]**: Support for collaborative editing and real-time updates


https://github.com/user-attachments/assets/c77c7927-335e-47fd-9cf7-852d4880d4b9



## Requirements

**Multi-modal Model required**: Some Univer mcp tools support returning images for better understanding, so the model you choose should ideally support multimodality.

> Plain text mode is currently experimental(NOT supported yet); it may be supported in the future. Any suggestions in this regard are very welcome.


## How It Works

<img width="600" height="400" alt="image" src="https://github.com/user-attachments/assets/58626cac-831d-4aa0-9c44-b3d2ff5262d9" />


- MCP host: such as cursor, claude code, or the agents you built.  
- Univer MCP Server: provides the endpoint for univer mcp, which proxies tool calls to the univer instance for execution.
- mcp-bridge: this is a [univer plugin](https://docs.univer.ai/guides/recipes/architecture/univer#plugins) used to handle various spreadsheet commands in mcp.
- univer instance: the runtime environment of univer (spreadsheet).


## Quick Start

### Get API Key
First, you need to get an API key from the [API Keys page](https://console.univer.ai/apikeys). This key will be used to authenticate your MCP server connection.

### Start Univer Instance

Before you talk to LLM, you need to launch a univer instance, which is a spreadsheet runtime where you will see the contents of the spreadsheet and how it is being operated.

There are two ways to start a univer instance quickly:
1. Use the [Univer MCP Playground](https://console.univer.ai/playground) to start a univer instance.
2. Use the [Univer MCP Start-kit](https://github.com/dream-num/univer-mcp-start-kit) to start a univer instance.

### Configure MCP Server

Add the following configuration to your MCP client settings:

```json
{
  "mcpServers": {
    "univer": {
      "url": "https://mcp.univer.ai/mcp/?univer_session_id=default",
      "type": "http",
      "headers": {
        "Authorization": "Bearer <API_KEY>"
      }
    }
  }
}
```
> [!TIP]
> `univer_session_id` is the session id of your Univer MCP session. Optional, `default` by default. Keep in mind that the session id MUST be consistent with the session id of your Univer instance.

<details>
<summary>Cursor</summary>

Click the button to install:

[![Install MCP Server](https://cursor.com/deeplink/mcp-install-dark.svg)](https://cursor.com/en/install-mcp?name=univer-mcp&config=eyJ1cmwiOiJodHRwczovL21jcC51bml2ZXIuYWkvbWNwLyIsImhlYWRlcnMiOnsiQXV0aG9yaXphdGlvbiI6IkJlYXJlciB7WU9VUl9VTklWRVJfQVBJX0tFWX0ifX0%3D)


</details>

<details>

<summary>Claude Code</summary>

```bash
claude mcp add --transport http univer-mcp https://mcp.univer.ai/mcp/ -H 'Authorization: Bearer {Your UNIVER_API_KEY}'
```
</details>

<details>
<summary>Gemini CLI</summary>

```bash
gemini mcp add --transport http univer-mcp https://mcp.univer.ai/mcp/ --header "Authorization: Bearer {Your UNIVER_API_KEY}"
```
</details>



## References

- **[Univer MCP Console](https://console.univer.ai/apikeys)** - Get your API keys and manage your account
- **[Documentation Guide](https://console.univer.ai/mcpguide)** - Comprehensive usage guide
- **[Playground](https://console.univer.ai/playground)** - Playground for spreadsheet operations
- **[Start Kit](https://github.com/dream-num/univer-mcp-start-kit)** - Ready-to-use templates and examples

## Resources & Support

- **Main Project**: [Univer Framework](https://github.com/dream-num/univer)
- **Community**: Join our [Discord](https://discord.gg/kB2wpYyM) for discussions and support
- **Issues**: Report bugs and request features on [GitHub Issues](https://github.com/dream-num/univer-mcp/issues)
- **Stack Overflow**: Tag your questions with `univer-mcp`

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Made with ❤️ by the [DreamNum](https://github.com/dream-num) team
```

