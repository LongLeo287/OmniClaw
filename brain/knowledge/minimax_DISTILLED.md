---
id: minimax
type: knowledge
owner: OA_Triage
---
# minimax
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: main.py
```py
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoConfig, QuantoConfig, GenerationConfig
import torch
import argparse

"""
 usage:
    export SAFETENSORS_FAST_GPU=1
    python main.py --quant_type int8 --world_size 8 --model_id <model_path>
"""

def generate_quanto_config(hf_config: AutoConfig, quant_type: str):
    QUANT_TYPE_MAP = {
        "default": None,
        "int8": QuantoConfig(
            weights="int8",
            modules_to_not_convert=[
                "lm_head",
                "embed_tokens",
            ] + [f"model.layers.{i}.coefficient" for i in range(hf_config.num_hidden_layers)]
            + [f"model.layers.{i}.block_sparse_moe.gate" for i in range(hf_config.num_hidden_layers)]
        ),
    }
    return QUANT_TYPE_MAP[quant_type]


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--quant_type", type=str, default="default", choices=["default", "int8"])
    parser.add_argument("--model_id", type=str, required=True)
    parser.add_argument("--world_size", type=int, required=True)
    return parser.parse_args()


def check_params(args, hf_config: AutoConfig):
    if args.quant_type == "int8":
        assert args.world_size >= 8, "int8 weight-only quantization requires at least 8 GPUs"

    assert hf_config.num_hidden_layers % args.world_size == 0, f"num_hidden_layers({hf_config.num_hidden_layers}) must be divisible by world_size({args.world_size})"


@torch.no_grad()
def main():
    args = parse_args()
    print("\n=============== Argument ===============")
    for key in vars(args):
        print(f"{key}: {vars(args)[key]}")
    print("========================================")

    model_id = args.model_id

    hf_config = AutoConfig.from_pretrained(model_id, trust_remote_code=True)
    check_params(args, hf_config)
    quantization_config = generate_quanto_config(hf_config, args.quant_type)
 
    device_map = {
        'model.embed_tokens': 'cuda:0',
        'model.norm': f'cuda:{args.world_size - 1}',
        'lm_head': f'cuda:{args.world_size - 1}'
    }
    layers_per_device = hf_config.num_hidden_layers // args.world_size
    for i in range(args.world_size):
        for j in range(layers_per_device):
            device_map[f'model.layers.{i * layers_per_device + j}'] = f'cuda:{i}'

    tokenizer = AutoTokenizer.from_pretrained(model_id)
    message = [
        {"role": "system", "content": [{"type": "text", "text": "You are a helpful assistant."}]},
        {"role": "user", "content": [{"type": "text", "text": "Hello, what is the weather today?"}]}
    ]
    tools = [
        {"name": "get_location", "description": "Get the location of the user.", "parameters": {"type": "object", "properties": {}}},
        {"name": "get_weather", "description": "Get the weather of a city.", "parameters": {"type": "object", "properties": {"city": {"type": "string", "description": "The name of the city"}}}},
        {"name": "get_news", "description": "Get the news.", "parameters": {"type": "object", "properties": {"domain": {"type": "string", "description": "The domain of the news"}}}}
    ]
    text = tokenizer.apply_chat_template(
        message,
        tools,
        tokenize=False,
        add_generation_prompt=True
    )
    model_inputs = tokenizer(text, return_tensors="pt").to("cuda")
    quantized_model = AutoModelForCausalLM.from_pretrained(
        model_id,
        torch_dtype="bfloat16",
        device_map=device_map,
        quantization_config=quantization_config,
        trust_remote_code=True,
        offload_buffers=True,
    )
    generation_config = GenerationConfig(
        max_new_tokens=20,
        eos_token_id=200020,
        use_cache=True,
    )
    generated_ids = quantized_model.generate(**model_inputs, generation_config=generation_config)
    print(f"generated_ids: {generated_ids}")
    generated_ids = [
        output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
    ]
    response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
    print(response)

if __name__ == "__main__":
    main()



```

### File: package.json
```json
{
  "name": "minimax-mcp-js",
  "version": "0.0.17", 
  "description": "Official MiniMax Model Context Protocol (MCP) JavaScript implementation that provides seamless integration with MiniMax's powerful AI capabilities including image generation, video generation, text-to-speech, and voice cloning APIs.",
  "main": "build/index.js",
  "type": "module",
  "bin": {
    "minimax-mcp-js": "./build/index.js"
  },
  "scripts": {
    "build": "tsc && chmod 755 build/index.js",
    "start": "node build/index.js",
    "dev": "tsc -w",
    "format": "prettier --write \"src/**/*.ts\"",
    "lint": "prettier --check \"src/**/*.ts\"",
    "prepare": "pnpm run build",
    "pretest": "pnpm run build",
    "inspector": "npx @modelcontextprotocol/inspector build/index.js"
  },
  "keywords": [
    "mcp",
    "minimax",
    "ai",
    "image-generation",
    "video-generation",
    "music-generation",
    "text-to-speech",
    "tts"
  ],
  "author": "Mark Yang <https://github.com/MaxYangyu>",
  "license": "MIT",
  "repository": {
    "type": "git",
    "url": "git+https://github.com/MiniMax-AI/MiniMax-MCP-JS.git"
  },
  "bugs": {
    "url": "https://github.com/MiniMax-AI/MiniMax-MCP-JS/issues"
  },
  "homepage": "https://github.com/MiniMax-AI/MiniMax-MCP-JS#readme",
  "dependencies": {
    "@chatmcp/sdk": "^1.0.5",
    "@modelcontextprotocol/sdk": "^1.7.0",
    "axios": "^1.8.4",
    "cors": "^2.8.5",
    "dotenv": "^16.5.0",
    "express": "^4.18.2",
    "yargs": "18.0.0-candidate.4",
    "zod": "^3.24.2"
  },
  "devDependencies": {
    "@types/cors": "^2.8.17",
    "@types/express": "^5.0.1",
    "@types/node": "^22.14.1",
    "@types/yargs": "^17.0.33",
    "prettier": "^3.2.1",
    "typescript": "^5.8.3"
  },
  "engines": {
    "node": ">=20.0.0",
    "pnpm": ">=8.0.0"
  },
  "files": [
    "build",
    "README.md",
    "README.zh-CN.md"
  ],
  "publishConfig": {
    "access": "public"
  }
}
```

### File: README.md
```md
![export](https://github.com/MiniMax-AI/MiniMax-01/raw/main/figures/MiniMaxLogo-Light.png)

<div align="center">

# MiniMax MCP JS

JavaScript/TypeScript implementation of MiniMax MCP, providing image generation, video generation, text-to-speech, and more.

<div style="line-height: 1.5;">
  <a href="https://www.minimax.io" target="_blank" style="margin: 2px; color: var(--fgColor-default);">
    <img alt="Homepage" src="https://img.shields.io/badge/_Homepage-MiniMax-FF4040?style=flat-square&labelColor=2C3E50&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB2aWV3Qm94PSIwIDAgNDkwLjE2IDQxMS43Ij48ZGVmcz48c3R5bGU+LmNscy0xe2ZpbGw6I2ZmZjt9PC9zdHlsZT48L2RlZnM+PHBhdGggY2xhc3M9ImNscy0xIiBkPSJNMjMzLjQ1LDQwLjgxYTE3LjU1LDE3LjU1LDAsMSwwLTM1LjEsMFYzMzEuNTZhNDAuODIsNDAuODIsMCwwLDEtODEuNjMsMFYxNDVhMTcuNTUsMTcuNTUsMCwxLDAtMzUuMDksMHY3OS4wNmE0MC44Miw0MC44MiwwLDAsMS04MS42MywwVjE5NS40MmExMS42MywxMS42MywwLDAsMSwyMy4yNiwwdjI4LjY2YTE3LjU1LDE3LjU1LDAsMCwwLDM1LjEsMFYxNDVBNDAuODIsNDAuODIsMCwwLDEsMTQwLDE0NVYzMzEuNTZhMTcuNTUsMTcuNTUsMCwwLDAsMzUuMSwwVjIxNy41aDBWNDAuODFhNDAuODEsNDAuODEsMCwxLDEsODEuNjIsMFYyODEuNTZhMTEuNjMsMTEuNjMsMCwxLDEtMjMuMjYsMFptMjE1LjksNjMuNEE0MC44Niw0MC44NiwwLDAsMCw0MDguNTMsMTQ1VjMwMC44NWExNy41NSwxNy41NSwwLDAsMS0zNS4wOSwwdi0yNjBhNDAuODIsNDAuODIsMCwwLDAtODEuNjMsMFYzNzAuODlhMTcuNTUsMTcuNTUsMCwwLDEtMzUuMSwwVjMzMGExMS42MywxMS42MywwLDEsMC0yMy4yNiwwdjQwLjg2YTQwLjgxLDQwLjgxLDAsMCwwLDgxLjYyLDBWNDAuODFhMTcuNTUsMTcuNTUsMCwwLDEsMzUuMSwwdjI2MGE0MC44Miw0MC44MiwwLDAsMCw4MS42MywwVjE0NWExNy41NSwxNy41NSwwLDEsMSwzNS4xLDBWMjgxLjU2YTExLjYzLDExLjYzLDAsMCwwLDIzLjI2LDBWMTQ1QTQwLjg1LDQwLjg1LDAsMCwwLDQ0OS4zNSwxMDQuMjFaIi8+PC9zdmc+&logoWidth=20" style="display: inline-block; vertical-align: middle;"/>
  </a>
  <a href="https://arxiv.org/abs/2501.08313" target="_blank" style="margin: 2px;">
    <img alt="Paper" src="https://img.shields.io/badge/📖_Paper-MiniMax--01-FF4040?style=flat-square&labelColor=2C3E50" style="display: inline-block; vertical-align: middle;"/>
  </a>
  <a href="https://chat.minimax.io/" target="_blank" style="margin: 2px;">
    <img alt="Chat" src="https://img.shields.io/badge/_MiniMax_Chat-FF4040?style=flat-square&labelColor=2C3E50&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB2aWV3Qm94PSIwIDAgNDkwLjE2IDQxMS43Ij48ZGVmcz48c3R5bGU+LmNscy0xe2ZpbGw6I2ZmZjt9PC9zdHlsZT48L2RlZnM+PHBhdGggY2xhc3M9ImNscy0xIiBkPSJNMjMzLjQ1LDQwLjgxYTE3LjU1LDE3LjU1LDAsMSwwLTM1LjEsMFYzMzEuNTZhNDAuODIsNDAuODIsMCwwLDEtODEuNjMsMFYxNDVhMTcuNTUsMTcuNTUsMCwxLDAtMzUuMDksMHY3OS4wNmE0MC44Miw0MC44MiwwLDAsMS04MS42MywwVjE5NS40MmExMS42MywxMS42MywwLDAsMSwyMy4yNiwwdjI4LjY2YTE3LjU1LDE3LjU1LDAsMCwwLDM1LjEsMFYxNDVBNDAuODIsNDAuODIsMCwwLDEsMTQwLDE0NVYzMzEuNTZhMTcuNTUsMTcuNTUsMCwwLDAsMzUuMSwwVjIxNy41aDBWNDAuODFhNDAuODEsNDAuODEsMCwxLDEsODEuNjIsMFYyODEuNTZhMTEuNjMsMTEuNjMsMCwxLDEtMjMuMjYsMFptMjE1LjksNjMuNEE0MC44Niw0MC44NiwwLDAsMCw0MDguNTMsMTQ1VjMwMC44NWExNy41NSwxNy41NSwwLDAsMS0zNS4wOSwwdi0yNjBhNDAuODIsNDAuODIsMCwwLDAtODEuNjMsMFYzNzAuODlhMTcuNTUsMTcuNTUsMCwwLDEtMzUuMSwwVjMzMGExMS42MywxMS42MywwLDEsMC0yMy4yNiwwdjQwLjg2YTQwLjgxLDQwLjgxLDAsMCwwLDgxLjYyLDBWNDAuODFhMTcuNTUsMTcuNTUsMCwwLDEsMzUuMSwwdjI2MGE0MC44Miw0MC44MiwwLDAsMCw4MS42MywwVjE0NWExNy41NSwxNy41NSwwLDEsMSwzNS4xLDBWMjgxLjU2YTExLjYzLDExLjYzLDAsMCwwLDIzLjI2LDBWMTQ1QTQwLjg1LDQwLjg1LDAsMCwwLDQ0OS4zNSwxMDQuMjFaIi8+PC9zdmc+&logoWidth=20" style="display: inline-block; vertical-align: middle;"/>
  </a>
  <a href="https://www.minimax.io/platform" style="margin: 2px;">
    <img alt="API" src="https://img.shields.io/badge/⚡_API-Platform-FF4040?style=flat-square&labelColor=2C3E50" style="display: inline-block; vertical-align: middle;"/>
  </a>
</div>

<div style="line-height: 1.5;">
  <a href="https://huggingface.co/MiniMaxAI" target="_blank" style="margin: 2px;">
    <img alt="Hugging Face" src="https://img.shields.io/badge/🤗_Hugging_Face-MiniMax-FF4040?style=flat-square&labelColor=2C3E50" style="display: inline-block; vertical-align: middle;"/>
  </a>
  <a href="https://github.com/MiniMax-AI/MiniMax-AI.github.io/blob/main/images/wechat-qrcode.jpeg" target="_blank" style="margin: 2px;">
    <img alt="WeChat" src="https://img.shields.io/badge/_WeChat-MiniMax-FF4040?style=flat-square&labelColor=2C3E50" style="display: inline-block; vertical-align: middle;"/>
  </a>
  <a href="https://www.modelscope.cn/organization/MiniMax" target="_blank" style="margin: 2px;">
    <img alt="ModelScope" src="https://img.shields.io/badge/_ModelScope-MiniMax-FF4040?style=flat-square&labelColor=2C3E50" style="display: inline-block; vertical-align: middle;"/>
  </a>
</div>

<div style="line-height: 1.5;">
  <a href="https://github.com/MiniMax-AI/MiniMax-MCP-JS/blob/main/LICENSE" style="margin: 2px;">
    <img alt="Code License" src="https://img.shields.io/badge/_Code_License-MIT-FF4040?style=flat-square&labelColor=2C3E50" style="display: inline-block; vertical-align: middle;"/>
  </a>
  <a href="https://smithery.ai/server/@MiniMax-AI/MiniMax-MCP-JS"><img alt="Smithery Badge" src="https://smithery.ai/badge/@MiniMax-AI/MiniMax-MCP-JS"></a>
</div>

</div>

## Documentation

- [中文文档](README.zh-CN.md)
- [Python Version](https://github.com/MiniMax-AI/MiniMax-MCP) - Official Python implementation of MiniMax MCP

## Release Notes

### July 22, 2025

#### 🔧 Fixes & Improvements
- **TTS Tool Fixes**: Fixed parameter handling for `languageBoost` and `subtitleEnable` in the `text_to_audio` tool
- **API Response Enhancement**: TTS API can return both audio file and subtitle file, providing a more complete speech-to-text experience

### July 7, 2025

#### 🆕 What's New
- **Voice Design**: New `voice_design` tool - create custom voices from descriptive prompts with preview audio
- **Video Enhancement**: Added `MiniMax-Hailuo-02` model with ultra-clear quality and duration/resolution controls  
- **Music Generation**: Enhanced `music_generation` tool powered by `music-1.5` model

#### 📈 Enhanced Tools
- `voice_design` - Generate personalized voices from text descriptions
- `generate_video` - Now supports MiniMax-Hailuo-02 with 6s/10s duration and 768P/1080P resolution options
- `music_generation` - High-quality music creation with music-1.5 model

## Features

- Text-to-Speech (TTS)
- Image Generation
- Video Generation
- Voice Cloning
- Music Generation
- Voice Design
- Dynamic configuration (supports both environment variables and request parameters)
- Compatible with MCP platform hosting (ModelScope and other MCP platforms)

## Installation

### Installing via Smithery

To install MiniMax MCP JS for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@MiniMax-AI/MiniMax-MCP-JS):

```bash
npx -y @smithery/cli install @MiniMax-AI/MiniMax-MCP-JS --client claude
```

### Installing manually
```bash
# Install with pnpm (recommended)
pnpm add minimax-mcp-js
```

## Quick Start

MiniMax MCP JS implements the [Model Context Protocol (MCP)](https://github.com/anthropics/model-context-protocol) specification and can be used as a server to interact with MCP-compatible clients (such as Claude AI).

### Quickstart with MCP Client

1. Get your API key from [MiniMax International Platform](https://www.minimax.io/platform/user-center/basic-information/interface-key).
2. Make sure that you already installed [Node.js and npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)
3. **Important: API HOST&KEY are different in different region**, they must match, otherwise you will receive an `Invalid API key` error.

|Region| Global  | Mainland  |
|:--|:-----|:-----|
|MINIMAX_API_KEY| go get from [MiniMax Global](https://www.minimax.io/platform/user-center/basic-information/interface-key) | go get from [MiniMax](https://platform.minimaxi.com/user-center/basic-information/interface-key) |
|MINIMAX_API_HOST| ​https://api.minimaxi.chat (note the extra **"i"**) | ​https://api.minimax.chat |


### Using with MCP Clients (Recommended)

Configure your MCP client:

#### Claude Desktop

Go to `Claude > Settings > Developer > Edit Config > claude_desktop_config.json` to include:

```json
{
  "mcpServers": {
    "minimax-mcp-js": {
      "command": "npx",
      "args": [
        "-y",
        "minimax-mcp-js"
      ],
      "env": {
        "MINIMAX_API_HOST": "<https://api.minimaxi.chat|https://api.minimax.chat>",
        "MINIMAX_API_KEY": "<your-api-key-here>",
        "MINIMAX_MCP_BASE_PATH": "<local-output-dir-path, such as /User/xxx/Desktop>",
        "MINIMAX_RESOURCE_MODE": "<optional, [url|local], url is default, audio/image/video are downloaded locally or provided in URL format>"
      }
    }
  }
}
```

#### Cursor

Go to `Cursor → Preferences → Cursor Settings → MCP → Add new global MCP Server` to add the above config.

⚠️ **Note**: If you encounter a "No tools found" error when using MiniMax MCP JS with Cursor, please update your Cursor to the latest version. For more information, see this [discussion thread](https://forum.cursor.com/t/mcp-servers-no-tools-found/49094/23).

That's it. Your MCP client can now interact with MiniMax through these tools.

**For local development**: 
When developing locally, you can use `npm link` to test your changes:
```bash
# In your project directory
npm link
```

Then configure Claude Desktop or Cursor to use npx as shown above. This will automatically use your linked version.

⚠️ **Note**: The API key needs to match the host address. Different hosts are used for global and mainland China versions:
- Global Host: `https://api.minimaxi.chat` (note the extra "i")
- Mainland China Host: `https://api.minimaxi.chat`

## Transport Modes

MiniMax MCP JS supports three transport modes:

| Feature | stdio (default) | REST | SSE |
|:-----|:-----|:-----|:-----|
| Environment | Local only | Local or cloud deployment | Local or cloud deployment |
| Communication | Via `standard I/O` | Via `HTTP requests` | Via `server-sent events` |
| Use Cases | Local MCP client integration | API services, cross-language calls | Applications requiring server push |
| Input Restrictions | Supports `local files` or `URL` resources | When deployed in cloud, `URL` input recommended | When deployed in cloud, `URL` input recommended |

## Configuration

MiniMax-MCP-JS provides multiple flexible configuration methods to adapt to different use cases. The configuration priority from highest to lowest is as follows:

### 1. Request Parameter Configuration (Highest Priority)

In platform hosting environments (like ModelScope or other MCP platforms), you can provide an independent configuration for each request via the `meta.auth` object in the request parameters:

```json
{
  "params": {
    "meta": {
      "auth": {
        "api_key": "your_api_key_here",
        "api_host": "<https://api.minimaxi.chat|https://api.minimaxi.chat>",
        "base_path": "/path/to/output",
        "resource_mode": "url"
      }
    }
  }
}
```

This method enables multi-tenant usage, where each request can use different API keys and configurations.

### 2. API Configuration

When used as a module in other projects, you can pass configuration through the `startMiniMaxMCP` function:

```javascript
import { startMiniMaxMCP } from 'minimax-mcp-js';

await startMiniMaxMCP({
  apiKey: 'your_api_key_here',
  apiHost: 'https://api.minimaxi.chat', // Global Host - https://api.minimaxi.chat, Mainland Host - https://api.minimax.chat
  basePath: '/path/to/output',
  resourceMode: 'url'
});
```

### 3. Command Line Arguments

1. Install the CLI tool globally:
```bash
# Install globally
pnpm install -g minimax-mcp-js
```

2. When used as a CLI tool, you can provide configuration via command line arguments:

```bash
minimax-mcp-js --api-key your_api_key_here --api-host https://api.minimaxi.chat --base-path /path/to/output --resource-mode url
```

### 4. Environment Variables (Lowest Priority)

The most basic configuration method is through environment variables:

```bash
# MiniMax API Key (required)
MINIMAX_API_KEY=your_api_key_here

# Base path for output files (optional, defaults to user's desktop)
MINIMAX_MCP_BASE_PATH=~/Desktop

# MiniMax API Host (optional, defaults to https://api.minimaxi.chat, Global Host - https://api.minimaxi.chat, Mainland Host - https://api.minimax.chat)
MINIMAX_API_HOST=https://api.minimaxi.chat

# Resource mode (optional, defaults to 'url')
# Options: 'url' (return URLs), 'local' (save files locally)
MINIMAX_RESOURCE_MODE=url
```

### Configuration Priority

When multiple configuration methods are used, the following priority order applies (from highest to lowest):

1. **Request-level configuration** (via `meta.auth` in each API request)
2. **Command line arguments**
3. **Environment variables**
4. **Configuration file**
5. **Default values**

This prioritization ensures flexibility across different deployment scenarios while maintaining per-request configuration capabilities for multi-tenant environments.

### Configuration Parameters

| Parameter | Description | Default Value |
|-----------|-------------|---------------|
| apiKey | MiniMax API Key | None (Required) |
| apiHost | MiniMax API Host | Global Host - https://api.minimaxi.chat, Mainland Host - https://api.minimax.chat |
| basePath | Base path for output files | User's desktop |
| resourceMode | Resource handling mode, 'url' or 'local' | url |

⚠️ **Note**: The API key needs to match the host address. Different hosts are used for global and mainland China versions:
- Global Host: `https://api.minimaxi.chat` (note the extra "i")
- Mainland China Host: `https://api.minimax.chat`

## Example usage

⚠️ Warning: Using these tools may incur costs.

### 1. broadcast a segment of the evening news
<img src="https://public-cdn-video-data-algeng.oss-cn-wulanchabu.aliyuncs.com/Snipaste_2025-04-09_20-07-53.png?x-oss-process=image/resize,p_50/format,webp" style="display: inline-block; vertical-align: middle;"/>

### 2. clone a voice
<img src="https://public-cdn-video-data-algeng.oss-cn-wulanchabu.aliyuncs.com/Snipaste_2025-04-09_19-45-13.png?x-oss-process=image/resize,p_50/format,webp" style="display: inline-block; vertical-align: middle;"/>

### 3. generate a video
<img src="https://public-cdn-video-data-algeng.oss-cn-wulanchabu.aliyuncs.com/Snipaste_2025-04-09_19-58-52.png?x-oss-process=image/resize,p_50/format,webp" style="display: inline-block; vertical-align: middle;"/>
<img src="https://public-cdn-video-data-algeng.oss-cn-wulanchabu.aliyuncs.com/Snipaste_2025-04-09_19-59-43.png?x-oss-process=image/resize,p_50/format,webp" style="display: inline-block; vertical-align: middle; "/>

### 4. generate images
<img src="https://public-cdn-video-data-algeng.oss-cn-wulanchabu.aliyuncs.com/gen_image.png?x-oss-process=image/resize,p_50/format,webp" style="display: inline-block; vertical-align: middle;"/>
<img src="https://public-cdn-video-data-algeng.oss-cn-wulanchabu.aliyuncs.com/gen_image1.png?x-oss-process=image/resize,p_50/format,webp" styl
... [TRUNCATED]
```

### File: setup.py
```py
from setuptools import setup, find_packages

setup(
    packages=find_packages(),
    include_package_data=True,
)

```

### File: config.json
```json
{
  "architectures": [
    "MiniMaxM1ForCausalLM"
  ],
  "attention_dropout": 0.0,
  "attn_type_list": [
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    1
  ],
  "auto_map": {
    "AutoConfig": "configuration_minimax_m1.MiniMaxM1Config",
    "AutoModelForCausalLM": "modeling_minimax_m1.MiniMaxM1ForCausalLM"
  },
  "bos_token_id": null,
  "eos_token_id": null,
  "head_dim": 128,
  "hidden_act": "silu",
  "hidden_size": 6144,
  "initializer_range": 0.02,
  "intermediate_size": 9216,
  "layernorm_full_attention_alpha": 3.5565588200778455,
  "layernorm_full_attention_beta": 1.0,
  "layernorm_linear_attention_alpha": 3.5565588200778455,
  "layernorm_linear_attention_beta": 1.0,
  "layernorm_mlp_alpha": 3.5565588200778455,
  "layernorm_mlp_beta": 1.0,
  "max_position_embeddings": 10240000,
  "model_type": "minimax_m1",
  "num_attention_heads": 64,
  "num_experts_per_tok": 2,
  "num_hidden_layers": 80,
  "num_key_value_heads": 8,
  "num_local_experts": 32,
  "output_router_logits": false,
  "postnorm": true,
  "rms_norm_eps": 1e-05,
  "rope_theta": 10000000,
  "rotary_dim": 64,
  "router_aux_loss_coef": 0.001,
  "router_jitter_noise": 0.0,
  "shared_intermediate_size": 0,
  "shared_moe_mode": "sigmoid",
  "sliding_window": null,
  "tie_word_embeddings": false,
  "transformers_version": "4.45.2",
  "use_cache": true,
  "vocab_size": 200064
}


```

### File: configuration_minimax_m1.py
```py
""" MiniMaxM1 model configuration"""

from transformers.configuration_utils import PretrainedConfig
from transformers.utils import logging


logger = logging.get_logger(__name__)


class MiniMaxM1Config(PretrainedConfig):
    r"""
    This is the configuration class to store the configuration of a [`MiniMaxM1Model`]. It is used to instantiate an
    MiniMaxM1 model according to the specified arguments, defining the model architecture. Instantiating a configuration
    with the defaults will yield a similar configuration to that of the MiniMaxM1.

    Configuration objects inherit from [`PretrainedConfig`] and can be used to control the model outputs. Read the
    documentation from [`PretrainedConfig`] for more information.


    Args:
        vocab_size (`int`, *optional*, defaults to 32000):
            Vocabulary size of the MiniMaxM1 model. Defines the number of different tokens that can be represented by the
            `inputs_ids` passed when calling [`MiniMaxM1Model`]
        hidden_size (`int`, *optional*, defaults to 4096):
            Dimension of the hidden representations.
        intermediate_size (`int`, *optional*, defaults to 14336):
            Dimension of the MLP representations.
        num_hidden_layers (`int`, *optional*, defaults to 32):
            Number of hidden layers in the Transformer encoder.
        num_attention_heads (`int`, *optional*, defaults to 32):
            Number of attention heads for each attention layer in the Transformer encoder.
        num_key_value_heads (`int`, *optional*, defaults to 8):
            This is the number of key_value heads that should be used to implement Grouped Query Attention. If
            `num_key_value_heads=num_attention_heads`, the model will use Multi Head Attention (MHA), if
            `num_key_value_heads=1 the model will use Multi Query Attention (MQA) otherwise GQA is used. When
            converting a multi-head checkpoint to a GQA checkpoint, each group key and value head should be constructed
            by meanpooling all the original heads within that group. For more details checkout [this
            paper](https://arxiv.org/pdf/2305.13245.pdf). If it is not specified, will default to `8`.
        hidden_act (`str` or `function`, *optional*, defaults to `"silu"`):
            The non-linear activation function (function or string) in the decoder.
        max_position_embeddings (`int`, *optional*, defaults to `4096*32`):
            The maximum sequence length that this model might ever be used with. MiniMaxM1's sliding window attention
            allows sequence of up to 4096*32 tokens.
        initializer_range (`float`, *optional*, defaults to 0.02):
            The standard deviation of the truncated_normal_initializer for initializing all weight matrices.
        rms_norm_eps (`float`, *optional*, defaults to 1e-05):
            The epsilon used by the rms normalization layers.
        use_cache (`bool`, *optional*, defaults to `True`):
            Whether or not the model should return the last key/values attentions (not used by all models). Only
            relevant if `config.is_decoder=True`.
        pad_token_id (`int`, *optional*):
            The id of the padding token.
        bos_token_id (`int`, *optional*, defaults to 1):
            The id of the "beginning-of-sequence" token.
        eos_token_id (`int`, *optional*, defaults to 2):
            The id of the "end-of-sequence" token.
        tie_word_embeddings (`bool`, *optional*, defaults to `False`):
            Whether the model's input and output word embeddings should be tied.
        rope_theta (`float`, *optional*, defaults to 1000000.0):
            The base period of the RoPE embeddings.
        sliding_window (`int`, *optional*):
            Sliding window attention window size. If not specified, will default to `4096`.
        attention_dropout (`float`, *optional*, defaults to 0.0):
            The dropout ratio for the attention probabilities.
        num_experts_per_tok (`int`, *optional*, defaults to 2):
            The number of experts to route per-token, can be also interpreted as the `top-k` routing
            parameter
        num_local_experts (`int`, *optional*, defaults to 8):
            Number of experts per Sparse MLP layer.
        output_router_logits (`bool`, *optional*, defaults to `False`):
            Whether or not the router logits should be returned by the model. Enabeling this will also
            allow the model to output the auxiliary loss. See [here]() for more details
        router_aux_loss_coef (`float`, *optional*, defaults to 0.001):
            The aux loss factor for the total loss.
        router_jitter_noise (`float`, *optional*, defaults to 0.0):
            Amount of noise to add to the router.

    ```python
    >>> from transformers import MiniMaxM1Model, MiniMaxM1Config

    >>> # Initializing a MiniMaxM1 style configuration
    >>> configuration = MiniMaxM1Config()

    >>> # Initializing a model from the MiniMaxM1 style configuration
    >>> model = MiniMaxM1Model(configuration)

    >>> # Accessing the model configuration
    >>> configuration = model.config
    ```"""

    model_type = "MiniMaxM1"
    keys_to_ignore_at_inference = ["past_key_values"]

    def __init__(
        self,
        vocab_size=32000,
        hidden_size=4096,
        intermediate_size=14336,
        num_hidden_layers=32,
        num_attention_heads=32,
        num_key_value_heads=8,
        hidden_act="silu",
        max_position_embeddings=4096 * 32,
        initializer_range=0.02,
        rms_norm_eps=1e-5,
        use_cache=True,
        pad_token_id=None,
        bos_token_id=None,
        eos_token_id=None,
        tie_word_embeddings=False,
        rope_theta=1e6,
        sliding_window=None,
        attention_dropout=0.0,
        num_experts_per_tok=2,
        num_local_experts=8,
        output_router_logits=False,
        router_aux_loss_coef=0.001,
        router_jitter_noise=0.0,
        **kwargs,
    ):
        self.vocab_size = vocab_size
        self.max_position_embeddings = max_position_embeddings
        self.hidden_size = hidden_size
        self.intermediate_size = intermediate_size
        self.num_hidden_layers = num_hidden_layers
        self.num_attention_heads = num_attention_heads
        self.sliding_window = sliding_window

        # for backward compatibility
        if num_key_value_heads is None:
            num_key_value_heads = num_attention_heads

        self.num_key_value_heads = num_key_value_heads
        self.hidden_act = hidden_act
        self.initializer_range = initializer_range
        self.rms_norm_eps = rms_norm_eps
        self.use_cache = use_cache
        self.rope_theta = rope_theta
        self.attention_dropout = attention_dropout

        self.num_experts_per_tok = num_experts_per_tok
        self.num_local_experts = num_local_experts
        self.output_router_logits = output_router_logits
        self.router_aux_loss_coef = router_aux_loss_coef
        self.router_jitter_noise = router_jitter_noise
        super().__init__(
            pad_token_id=pad_token_id,
            bos_token_id=bos_token_id,
            eos_token_id=eos_token_id,
            tie_word_embeddings=tie_word_embeddings,
            **kwargs,
        )

```

### File: example.minimax-config.json
```json
{
  "apiKey": "your_api_key_here",
  "apiHost": "https://api.minimax.chat",
  "basePath": "~/Desktop",
  "resourceMode": "url",
  "server": {
    "mode": "stdio",
    "port": 9593,
    "endpoint": "/rest"
  }
} 
```

### File: mcp_server_config_demo.json
```json
{
    "mcpServers": {
      "MiniMax": {
        "command": "uvx",
        "args": [
          "minimax-mcp"
        ],
        "env": {
          "MINIMAX_API_KEY": "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWUsImlhdCI6MTc0NTM3NjU1N30.nrmwo6orXJfyf63IqJCK4LiUXrq9r9ZELCY530Mu6sLyx_qNAVsJ3Q828Rqy6pwoQl6VFMMFaJG3kc6aIMEfVLo7xlB-4NbwMxYKhwtxyQL8g_agYqw-1aY4zr3uvgTZxafXt1dEjcuS5i9O9SuOXXofeqb0jAnb_dssaLfgHNKlKthJpjsg8G76ZULS7KCpm6GvPWR4mwIdH-i0IhBU6CVSWpBAYKVNHJ-FVN_HzN5UgGvHkDbOOggg6Ib1illYbx6zkb7_JYZ7Tek1erjvJi7IG8Keh4NHq5kcyROWBetO9W8_2if_nfO6XBhlJRECpEmYBONwroGw0nH6xNblQw",
          "MINIMAX_MCP_BASE_PATH": "~/Desktop",
          "MINIMAX_API_HOST": "https://api.minimax.chat",
          "MINIMAX_API_RESOURCE_MODE": "url"
        }
      }
    }
  }
```

### File: MiniMax-Text-01-Model-Card.md
```md
<div align="center">
  <picture>
    <source srcset="figures/MiniMaxLogo-Dark.png" media="(prefers-color-scheme: dark)">
      <img src="figures/MiniMaxLogo-Light.png" width="60%" alt="MiniMax-Text-01">
    </source>
  </picture>
</div>
<hr>

<div align="center" style="line-height: 1;">
  <a href="https://www.minimax.io" target="_blank" style="margin: 2px; color: var(--fgColor-default);">
    <img alt="Homepage" src="https://img.shields.io/badge/_Homepage-MiniMax-FF4040?style=flat-square&labelColor=2C3E50&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB2aWV3Qm94PSIwIDAgNDkwLjE2IDQxMS43Ij48ZGVmcz48c3R5bGU+LmNscy0xe2ZpbGw6I2ZmZjt9PC9zdHlsZT48L2RlZnM+PHBhdGggY2xhc3M9ImNscy0xIiBkPSJNMjMzLjQ1LDQwLjgxYTE3LjU1LDE3LjU1LDAsMSwwLTM1LjEsMFYzMzEuNTZhNDAuODIsNDAuODIsMCwwLDEtODEuNjMsMFYxNDVhMTcuNTUsMTcuNTUsMCwxLDAtMzUuMDksMHY3OS4wNmE0MC44Miw0MC44MiwwLDAsMS04MS42MywwVjE5NS40MmExMS42MywxMS42MywwLDAsMSwyMy4yNiwwdjI4LjY2YTE3LjU1LDE3LjU1LDAsMCwwLDM1LjEsMFYxNDVBNDAuODIsNDAuODIsMCwwLDEsMTQwLDE0NVYzMzEuNTZhMTcuNTUsMTcuNTUsMCwwLDAsMzUuMSwwVjIxNy41aDBWNDAuODFhNDAuODEsNDAuODEsMCwxLDEsODEuNjIsMFYyODEuNTZhMTEuNjMsMTEuNjMsMCwxLDEtMjMuMjYsMFptMjE1LjksNjMuNEE0MC44Niw0MC44NiwwLDAsMCw0MDguNTMsMTQ1VjMwMC44NWExNy41NSwxNy41NSwwLDAsMS0zNS4wOSwwdi0yNjBhNDAuODIsNDAuODIsMCwwLDAtODEuNjMsMFYzNzAuODlhMTcuNTUsMTcuNTUsMCwwLDEtMzUuMSwwVjMzMGExMS42MywxMS42MywwLDEsMC0yMy4yNiwwdjQwLjg2YTQwLjgxLDQwLjgxLDAsMCwwLDgxLjYyLDBWNDAuODFhMTcuNTUsMTcuNTUsMCwwLDEsMzUuMSwwdjI2MGE0MC44Miw0MC44MiwwLDAsMCw4MS42MywwVjE0NWExNy41NSwxNy41NSwwLDEsMSwzNS4xLDBWMjgxLjU2YTExLjYzLDExLjYzLDAsMCwwLDIzLjI2LDBWMTQ1QTQwLjg1LDQwLjg1LDAsMCwwLDQ0OS4zNSwxMDQuMjFaIi8+PC9zdmc+&logoWidth=20" style="display: inline-block; vertical-align: middle;"/>
  </a>
  <a href="https://arxiv.org/abs/2501.08313" target="_blank" style="margin: 2px;">
    <img alt="Paper" src="https://img.shields.io/badge/📖_Paper-MiniMax--01-FF4040?style=flat-square&labelColor=2C3E50" style="display: inline-block; vertical-align: middle;"/>
  </a>
   <a href="https://chat.minimax.io/" target="_blank" style="margin: 2px;">
    <img alt="Chat" src="https://img.shields.io/badge/_MiniMax_Chat-FF4040?style=flat-square&labelColor=2C3E50&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB2aWV3Qm94PSIwIDAgNDkwLjE2IDQxMS43Ij48ZGVmcz48c3R5bGU+LmNscy0xe2ZpbGw6I2ZmZjt9PC9zdHlsZT48L2RlZnM+PHBhdGggY2xhc3M9ImNscy0xIiBkPSJNMjMzLjQ1LDQwLjgxYTE3LjU1LDE3LjU1LDAsMSwwLTM1LjEsMFYzMzEuNTZhNDAuODIsNDAuODIsMCwwLDEtODEuNjMsMFYxNDVhMTcuNTUsMTcuNTUsMCwxLDAtMzUuMDksMHY3OS4wNmE0MC44Miw0MC44MiwwLDAsMS04MS42MywwVjE5NS40MmExMS42MywxMS42MywwLDAsMSwyMy4yNiwwdjI4LjY2YTE3LjU1LDE3LjU1LDAsMCwwLDM1LjEsMFYxNDVBNDAuODIsNDAuODIsMCwwLDEsMTQwLDE0NVYzMzEuNTZhMTcuNTUsMTcuNTUsMCwwLDAsMzUuMSwwVjIxNy41aDBWNDAuODFhNDAuODEsNDAuODEsMCwxLDEsODEuNjIsMFYyODEuNTZhMTEuNjMsMTEuNjMsMCwxLDEtMjMuMjYsMFptMjE1LjksNjMuNEE0MC44Niw0MC44NiwwLDAsMCw0MDguNTMsMTQ1VjMwMC44NWExNy41NSwxNy41NSwwLDAsMS0zNS4wOSwwdi0yNjBhNDAuODIsNDAuODIsMCwwLDAtODEuNjMsMFYzNzAuODlhMTcuNTUsMTcuNTUsMCwwLDEtMzUuMSwwVjMzMGExMS42MywxMS42MywwLDEsMC0yMy4yNiwwdjQwLjg2YTQwLjgxLDQwLjgxLDAsMCwwLDgxLjYyLDBWNDAuODFhMTcuNTUsMTcuNTUsMCwwLDEsMzUuMSwwdjI2MGE0MC44Miw0MC44MiwwLDAsMCw4MS42MywwVjE0NWExNy41NSwxNy41NSwwLDEsMSwzNS4xLDBWMjgxLjU2YTExLjYzLDExLjYzLDAsMCwwLDIzLjI2LDBWMTQ1QTQwLjg1LDQwLjg1LDAsMCwwLDQ0OS4zNSwxMDQuMjFaIi8+PC9zdmc+&logoWidth=20" style="display: inline-block; vertical-align: middle;"/>
  </a>
  <a href="https://www.minimax.io/platform" style="margin: 2px;">
    <img alt="API" src="https://img.shields.io/badge/⚡_API-Platform-FF4040?style=flat-square&labelColor=2C3E50" style="display: inline-block; vertical-align: middle;"/>
  </a>  
</div>
<div align="center" style="line-height: 1;">
  <a href="https://huggingface.co/MiniMaxAI" target="_blank" style="margin: 2px;">
    <img alt="Hugging Face" src="https://img.shields.io/badge/🤗_Hugging_Face-MiniMax-FF4040?style=flat-square&labelColor=2C3E50" style="display: inline-block; vertical-align: middle;"/>
  </a>
  <a href="https://github.com/MiniMax-AI/MiniMax-AI.github.io/blob/main/images/wechat-qrcode.jpegg" target="_blank" style="margin: 2px;">
    <img alt="WeChat" src="https://img.shields.io/badge/_WeChat-MiniMax-FF4040?style=flat-square&labelColor=2C3E50" style="display: inline-block; vertical-align: middle;"/>
  </a>
</div>
<div align="center" style="line-height: 1;">
  <a href="https://github.com/MiniMax-AI/MiniMax-01/blob/main/LICENSE-MODEL" style="margin: 2px;">
    <img alt="Model License" src="https://img.shields.io/badge/_Model_License-Model_Agreement-FF4040?style=flat-square&labelColor=2C3E50" style="display: inline-block; vertical-align: middle;"/>
  </a>
   <a href="https://github.com/MiniMax-AI/MiniMax-01/blob/main/LICENSE-CODE" style="margin: 2px;">
    <img alt="Code License" src="https://img.shields.io/badge/_Code_License-MIT-FF4040?style=flat-square&labelColor=2C3E50" style="display: inline-block; vertical-align: middle;"/>
  </a>
</div>


# MiniMax-Text-01

## 1. Introduction

MiniMax-Text-01 is a powerful language model with 456 billion total parameters, of which 45.9 billion are activated per token. To better unlock the long context capabilities of the model, MiniMax-Text-01 adopts a hybrid architecture that combines Lightning Attention, Softmax Attention and Mixture-of-Experts (MoE). Leveraging advanced parallel strategies and innovative compute-communication overlap methods—such as Linear Attention Sequence Parallelism Plus (LASP+), varlen ring attention, Expert Tensor Parallel (ETP), etc., MiniMax-Text-01's training context length is extended to 1 million tokens, and it can handle a context of up to 4 million tokens during the inference. On various academic benchmarks, MiniMax-Text-01 also demonstrates the performance of a top-tier model.

<p align="center">
  <img width="100%" src="figures/TextBench.png">
</p>

## 2. Model Architecture

The architecture of MiniMax-Text-01 is briefly described as follows:
- Total Parameters: 456B
- Activated Parameters per Token: 45.9B
- Number Layers: 80
- Hybrid Attention: a softmax attention is positioned after every 7 lightning attention.
  - Number of attention heads: 64
  - Attention head dimension: 128
- Mixture of Experts:
  - Number of experts: 32
  - Expert hidden dimension: 9216
  - Top-2 routing strategy
- Positional Encoding: Rotary Position Embedding (RoPE) applied to half of the attention head dimension with a base frequency of 10,000,000
- Hidden Size: 6144
- Vocab Size: 200,064

## 3. Evaluation

### Core Academic Benchmarks

| **Tasks**                     | **GPT-4o (11-20)** | **Claude-3.5-Sonnet (10-22)** | **Gemini-1.5-Pro (002)** | **Gemini-2.0-Flash (exp)** | **Qwen2.5-72B-Inst.** | **DeepSeek-V3** | **Llama-3.1-405B-Inst.** | **MiniMax-Text-01** |
|-------------------------------|--------------------|-------------------------------|--------------------------|----------------------------|-----------------------|-----------------|--------------------------|---------------------|
| **General**                   |                    |                               |                          |                            |                       |                 |                          |                     |
| MMLU<sup>*</sup>                      | 85.7               | 88.3                          | 86.8                     | 86.5                       | 86.1                  | 88.5        | **88.6**                 | 88.5                |
| MMLU-Pro<sup>*</sup>                  | 74.4               | **78.0**                      | 75.8                     | 76.4                       | 71.1                  | 75.9            | 73.3                     | 75.7                |
| SimpleQA                      | **39.0**           | 28.1                          | 23.4                     | 26.6                       | 10.3                  | 24.9            | 23.2                     | 23.7                |
| C-SimpleQA                    | 64.6               | 56.8                          | 59.4                     | 63.3                       | 52.2                  | 64.8            | 54.7                     | **67.4**            |
| IFEval _(avg)_                | 84.1               | **90.1**                      | 89.4                     | 88.4                       | 87.2                  | 87.3            | 86.4                     | 89.1                |
| Arena-Hard                    | **92.4**           | 87.6                          | 85.3                     | 72.7                       | 81.2                  | 91.4            | 63.5                     | 89.1                |
| **Reasoning**                 |                    |                               |                          |                            |                       |                 |                          |                     |
| GPQA<sup>*</sup> _(diamond)_          | 46.0               | **65.0**                      | 59.1                     | 62.1                       | 49.0                  | 59.1            | 50.7                     | 54.4                |
| DROP<sup>*</sup> _(F1)_               | 89.2               | 88.8                          | 89.2                     | 89.3                       | 85.0                  | 91.0        | **92.5**                 | 87.8                |
| **Mathematics**               |                    |                               |                          |                            |                       |                 |                          |                     |
| GSM8k<sup>*</sup>                     | 95.6               | **96.9**                      | 95.2                     | 95.4                       | 95.8                  | 96.7            | 96.7                     | 94.8                |
| MATH<sup>*</sup>                      | 76.6               | 74.1                          | **84.6**                 | 83.9                       | 81.8                  | **84.6**        | 73.8                     | 77.4                |
| **Coding**                    |                    |                               |                          |                            |                       |                 |                          |                     |
| MBPP +                        | 76.2               | 75.1                          | 75.4                     | 75.9                       | 77.0              | **78.8**        | 73.0                     | 71.7                |
| HumanEval                     | 90.2               | **93.7**                      | 86.6                     | 89.6                       | 86.6                  | 92.1            | 89.0                     | 86.9                |

<sup>*</sup> Evaluated following a _0-shot CoT_ setting.

### Long Benchmarks
#### 4M Needle In A Haystack Test
<p align="center">
  <img width="90%" src="figures/niah.png">
</p>

#### Ruler
| Model | 4k | 8k | 16k | 32k | 64k | 128k | 256k | 512k | 1M |
|-------|----|----|-----|-----|-----|------|------|------|----|
| **GPT-4o (11-20)** | **0.970** | 0.921 | 0.890 | 0.888 | 0.884 | - | - | - | - |
| **Claude-3.5-Sonnet (10-22)** | 0.965 | 0.960 | 0.957 | 0.950 | **0.952** | 0.938 | - | - | - |
| **Gemini-1.5-Pro (002)** | 0.962 | 0.960 | **0.960** | **0.958** | 0.938 | 0.917 | 0.916 | 0.861 | 0.850 |
| **Gemini-2.0-Flash (exp)** | 0.960 | 0.960 | 0.951 | 0.957 | 0.937 | 0.860 | 0.797 | 0.709 | - |
| **MiniMax-Text-01** | 0.963 | **0.961** | 0.953 | 0.954 | 0.943 | **0.947** | **0.945** | **0.928** | **0.910** |

#### LongBench v2
| **Model**                  | **overall** | **easy** | **hard** | **short** | **medium** | **long** |
|----------------------------|-------------|----------|----------|------------|------------|----------|
| Human                      | 53.7        | 100.0    | 25.1     | 47.2       | 59.1       | 53.7     |
| **w/ CoT**                 |             |          |          |            |            |          |
| GPT-4o (11-20)             | 51.4        | 54.2     | 49.7     | 59.6       | 48.6       | 43.5     |
| Claude-3.5-Sonnet (10-22)  | 46.7        | 55.2     | 41.5     | 53.9       | 41.9       | 44.4     |
| Deepseek-V3                | -           | -        | -        | -          | -          | -        |
| Qwen2.5-72B-Inst.          | 43.5        | 47.9     | 40.8     | 48.9       | 40.9       | 39.8     |
| **MiniMax-Text-01**        | **56.5**    | **66.1** | **50.5** | **61.7**   | **56.7**   | **47.2** |
| **w/o CoT**                |             |          |          |            |            |          |
| GPT-4o (11-20)             | 50.1        | 57.4     | 45.6     | 53.3       | 52.4       | 40.2     |
| Claude-3.5-Sonnet (10-22)  | 41.0        | 46.9     | 37.3     | 46.1       | 38.6       | 37.0     |
| Deepseek-V3                | 48.7        | -        | -        | -          | -          | -        |
| Qwen2.5-72B-Inst.          | 42.1        | 42.7     | 41.8     | 45.6       | 38.1       | **44.4** |
| **MiniMax-Text-01**        | **52.9**    | **60.9** | **47.9** | **58.9**   | **52.6**   | 43.5     |

#### MTOB
| **Context Type** | **no context** | **half book** | **full book** | **Δ half book** | **Δ full book** |
|------------------|----------------|---------------|---------------|------------------|-----------------|
| **eng → kalam (ChrF)** | | | | | |
| GPT-4o (11-20) | 9.90 | **54.30** | - | 44.40 | - |
| Claude-3.5-Sonnet (10-22) | 20.22 | 53.62 | 55.65 | 33.39 | 35.42 |
| Gemini-1.5-Pro (002) | 16.79 | 53.68 | **57.90** | 36.89 | 41.11 |
| Gemini-2.0-Flash (exp) | 12.20 | 49.50 | 53.30 | 37.30 | 41.10 |
| Qwen-Long | 16.55 | 48.48 | 45.94 | 31.92 | 29.39 |
| **MiniMax-Text-01** | 6.0 | 51.74 | 51.60 | **45.7** | **45.6** |
| **kalam → eng (BLEURT)** | | | | | |
| GPT-4o (11-20) | 33.20 | 58.30 | - | 25.10 | - |
| Claude-3.5-Sonnet (10-22) | 31.42 | 59.70 | 62.30 | 28.28 | 30.88 |
| Gemini-1.5-Pro (002) | 32.02 | **61.52** | **63.09** | **29.50** | **31.07** |
| Gemini-2.0-Flash (exp) | 33.80 | 57.50 | 57.00 | 23.70 | 23.20 |
| Qwen-Long | 30.13 | 53.14 | 32.15 | 23.01 | 2.02 |
| **MiniMax-Text-01** | 33.65 | 57.10 | 58.00 | 23.45 | 24.35 |


## 4. Quickstart
Here we provide a simple example of loading the tokenizer and model to generate content.
```python
from transformers import AutoModelForCausalLM, AutoTokenizer, AutoConfig, QuantoConfig, GenerationConfig

# load hf config
hf_config = AutoConfig.from_pretrained("MiniMaxAI/MiniMax-Text-01", trust_remote_code=True)

# quantization config, int8 is recommended
quantization_config =  QuantoConfig(
            weights="int8",
            modules_to_not_convert=[
                "lm_head",
                "embed_tokens",
            ] + [f"model.layers.{i}.coefficient" for i in range(hf_config.num_hidden_layers)]
         
... [TRUNCATED]
```

### File: MiniMax-VL-01-Model-Card.md
```md
<div align="center">
  <picture>
    <source srcset="figures/MiniMaxLogo-Dark.png" media="(prefers-color-scheme: dark)">
      <img src="figures/MiniMaxLogo-Light.png" width="60%" alt="MiniMax-VL-01">
    </source>
  </picture>
</div>
<hr>

<div align="center" style="line-height: 1;">
  <a href="https://www.minimax.io" target="_blank" style="margin: 2px; color: var(--fgColor-default);">
    <img alt="Homepage" src="https://img.shields.io/badge/_Homepage-MiniMax-FF4040?style=flat-square&labelColor=2C3E50&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB2aWV3Qm94PSIwIDAgNDkwLjE2IDQxMS43Ij48ZGVmcz48c3R5bGU+LmNscy0xe2ZpbGw6I2ZmZjt9PC9zdHlsZT48L2RlZnM+PHBhdGggY2xhc3M9ImNscy0xIiBkPSJNMjMzLjQ1LDQwLjgxYTE3LjU1LDE3LjU1LDAsMSwwLTM1LjEsMFYzMzEuNTZhNDAuODIsNDAuODIsMCwwLDEtODEuNjMsMFYxNDVhMTcuNTUsMTcuNTUsMCwxLDAtMzUuMDksMHY3OS4wNmE0MC44Miw0MC44MiwwLDAsMS04MS42MywwVjE5NS40MmExMS42MywxMS42MywwLDAsMSwyMy4yNiwwdjI4LjY2YTE3LjU1LDE3LjU1LDAsMCwwLDM1LjEsMFYxNDVBNDAuODIsNDAuODIsMCwwLDEsMTQwLDE0NVYzMzEuNTZhMTcuNTUsMTcuNTUsMCwwLDAsMzUuMSwwVjIxNy41aDBWNDAuODFhNDAuODEsNDAuODEsMCwxLDEsODEuNjIsMFYyODEuNTZhMTEuNjMsMTEuNjMsMCwxLDEtMjMuMjYsMFptMjE1LjksNjMuNEE0MC44Niw0MC44NiwwLDAsMCw0MDguNTMsMTQ1VjMwMC44NWExNy41NSwxNy41NSwwLDAsMS0zNS4wOSwwdi0yNjBhNDAuODIsNDAuODIsMCwwLDAtODEuNjMsMFYzNzAuODlhMTcuNTUsMTcuNTUsMCwwLDEtMzUuMSwwVjMzMGExMS42MywxMS42MywwLDEsMC0yMy4yNiwwdjQwLjg2YTQwLjgxLDQwLjgxLDAsMCwwLDgxLjYyLDBWNDAuODFhMTcuNTUsMTcuNTUsMCwwLDEsMzUuMSwwdjI2MGE0MC44Miw0MC44MiwwLDAsMCw4MS42MywwVjE0NWExNy41NSwxNy41NSwwLDEsMSwzNS4xLDBWMjgxLjU2YTExLjYzLDExLjYzLDAsMCwwLDIzLjI2LDBWMTQ1QTQwLjg1LDQwLjg1LDAsMCwwLDQ0OS4zNSwxMDQuMjFaIi8+PC9zdmc+&logoWidth=20" style="display: inline-block; vertical-align: middle;"/>
  </a>
  <a href="https://arxiv.org/abs/2501.08313" target="_blank" style="margin: 2px;">
    <img alt="Paper" src="https://img.shields.io/badge/📖_Paper-MiniMax--01-FF4040?style=flat-square&labelColor=2C3E50" style="display: inline-block; vertical-align: middle;"/>
  </a>
   <a href="https://chat.minimax.io/" target="_blank" style="margin: 2px;">
    <img alt="Chat" src="https://img.shields.io/badge/_MiniMax_Chat-FF4040?style=flat-square&labelColor=2C3E50&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB2aWV3Qm94PSIwIDAgNDkwLjE2IDQxMS43Ij48ZGVmcz48c3R5bGU+LmNscy0xe2ZpbGw6I2ZmZjt9PC9zdHlsZT48L2RlZnM+PHBhdGggY2xhc3M9ImNscy0xIiBkPSJNMjMzLjQ1LDQwLjgxYTE3LjU1LDE3LjU1LDAsMSwwLTM1LjEsMFYzMzEuNTZhNDAuODIsNDAuODIsMCwwLDEtODEuNjMsMFYxNDVhMTcuNTUsMTcuNTUsMCwxLDAtMzUuMDksMHY3OS4wNmE0MC44Miw0MC44MiwwLDAsMS04MS42MywwVjE5NS40MmExMS42MywxMS42MywwLDAsMSwyMy4yNiwwdjI4LjY2YTE3LjU1LDE3LjU1LDAsMCwwLDM1LjEsMFYxNDVBNDAuODIsNDAuODIsMCwwLDEsMTQwLDE0NVYzMzEuNTZhMTcuNTUsMTcuNTUsMCwwLDAsMzUuMSwwVjIxNy41aDBWNDAuODFhNDAuODEsNDAuODEsMCwxLDEsODEuNjIsMFYyODEuNTZhMTEuNjMsMTEuNjMsMCwxLDEtMjMuMjYsMFptMjE1LjksNjMuNEE0MC44Niw0MC44NiwwLDAsMCw0MDguNTMsMTQ1VjMwMC44NWExNy41NSwxNy41NSwwLDAsMS0zNS4wOSwwdi0yNjBhNDAuODIsNDAuODIsMCwwLDAtODEuNjMsMFYzNzAuODlhMTcuNTUsMTcuNTUsMCwwLDEtMzUuMSwwVjMzMGExMS42MywxMS42MywwLDEsMC0yMy4yNiwwdjQwLjg2YTQwLjgxLDQwLjgxLDAsMCwwLDgxLjYyLDBWNDAuODFhMTcuNTUsMTcuNTUsMCwwLDEsMzUuMSwwdjI2MGE0MC44Miw0MC44MiwwLDAsMCw4MS42MywwVjE0NWExNy41NSwxNy41NSwwLDEsMSwzNS4xLDBWMjgxLjU2YTExLjYzLDExLjYzLDAsMCwwLDIzLjI2LDBWMTQ1QTQwLjg1LDQwLjg1LDAsMCwwLDQ0OS4zNSwxMDQuMjFaIi8+PC9zdmc+&logoWidth=20" style="display: inline-block; vertical-align: middle;"/>
  </a>
  <a href="https://www.minimax.io/platform" style="margin: 2px;">
    <img alt="API" src="https://img.shields.io/badge/⚡_API-Platform-FF4040?style=flat-square&labelColor=2C3E50" style="display: inline-block; vertical-align: middle;"/>
  </a>  
</div>
<div align="center" style="line-height: 1;">
  <a href="https://huggingface.co/MiniMaxAI" target="_blank" style="margin: 2px;">
    <img alt="Hugging Face" src="https://img.shields.io/badge/🤗_Hugging_Face-MiniMax-FF4040?style=flat-square&labelColor=2C3E50" style="display: inline-block; vertical-align: middle;"/>
  </a>
  <a href="https://github.com/MiniMax-AI/MiniMax-AI.github.io/blob/main/images/wechat-qrcode.jpeg" target="_blank" style="margin: 2px;">
    <img alt="WeChat" src="https://img.shields.io/badge/_WeChat-MiniMax-FF4040?style=flat-square&labelColor=2C3E50" style="display: inline-block; vertical-align: middle;"/>
  </a>
</div>
<div align="center" style="line-height: 1;">
  <a href="https://github.com/MiniMax-AI/MiniMax-01/blob/main/LICENSE-MODEL" style="margin: 2px;">
    <img alt="Model License" src="https://img.shields.io/badge/_Model_License-Model_Agreement-FF4040?style=flat-square&labelColor=2C3E50" style="display: inline-block; vertical-align: middle;"/>
  </a>
   <a href="https://github.com/MiniMax-AI/MiniMax-01/blob/main/LICENSE-CODE" style="margin: 2px;">
    <img alt="Code License" src="https://img.shields.io/badge/_Code_License-MIT-FF4040?style=flat-square&labelColor=2C3E50" style="display: inline-block; vertical-align: middle;"/>
  </a>
</div>

# MiniMax-VL-01

## 1. Introduction
We are delighted to introduce our **MiniMax-VL-01** model. It adopts the “ViT-MLP-LLM” framework, which is a commonly used technique in the field of multimodal large language models. The model is initialized and trained with three key parts: a 303-million-parameter Vision Transformer (ViT) for visual encoding, a randomly initialized two-layer MLP projector for image adaptation, and the MiniMax-Text-01 as the base LLM.
MiniMax-VL-01 has a notable dynamic resolution feature. Input images are resized per a pre-set grid, with resolutions from 336×336 to 2016×2016, keeping a 336×336 thumbnail. The resized images are split into non-overlapping patches of the same size. These patches and the thumbnail are encoded separately and then combined for a full image representation.
The training data for MiniMax-VL-01 consists of caption, description, and instruction data. The Vision Transformer (ViT) is trained on 694 million image-caption pairs from scratch. Across four distinct stages of the training pipeline, a total of 512 billion tokens are processed, leveraging this vast amount of data to endow the model with strong capabilities.
Finally, MiniMax-VL-01 has reached top-level performance on multimodal leaderboards, demonstrating its edge and dependability in complex multimodal tasks.


<p align="center">
  <img width="100%" src="figures/VisionBench.png">
</p>


## 2. Evaluation

| Tasks | GPT-4o<br>(11-20) | Claude-3.5-Sonnet (10-22) | Gemini-1.5-Pro (002) | Gemini-2.0-Flash (exp) | Qwen2-VL-72B-Inst. | InternVL2.5-78B | LLama-3.2-90B | MiniMax-VL-01 |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| **Knowledge** |  |  |  |  |  |  |  |  |
| MMMU<sup>*</sup> | 63.5 | **72.0** | 68.4  | 70.6  | 64.5 | 66.5 | 62.1 | 68.5 |
| MMMU-Pro<sup>*</sup>  |  54.5 | 54.7 | 50.9 | **57.0**  | 43.2 | 47.3 | 36.0 | 52.7 |
| **Visual Q&A** |  |  |  |  |  |  |  |  |
| ChartQA<sup>*</sup><sub>relaxed</sub> | 88.1 | 90.8 | 88.7 | 88.3 | 91.2 | 91.5 | 85.5 | **91.7** |
| DocVQA<sup>*</sup>  | 91.1 | 94.2 | 91.5 | 92.9 | **97.1** | 96.1 | 90.1 | 96.4 |
| OCRBench | 806 | 790 | 800 | 846  | 856 | 847 | 805 | **865** |
| **Mathematics & Sciences** ||  |  |  |  |  |  |  |
| AI2D<sup>*</sup> | 83.1 | 82.0 | 80.9 | 85.1 | 84.4 | **86.8** | 78.9 | 83.3 |
| MathVista<sup>*</sup>  | 62.1 | 65.4 | 70.6 | **73.1** | 69.6 | 68.4 | 57.3 | 68.6 |
| OlympiadBench<sub>full</sub> | 25.2 | 28.4 | 32.1 | **46.1** | 21.9 | 25.1 | 19.3 | 24.2 |
|**Long Context**|||||
|M-LongDoc<sub>acc</sub>| **41.4** | 31.4 | 26.2 | 31.4 | 11.6 | 19.7 | 13.9 | 32.5 |
|**Comprehensive**|||||
|MEGA-Bench<sub>macro</sub> | 49.4 | 51.4 | 45.9 | **53.9** | 46.8 | 45.3 | 19.9 | 47.4 |
|**User Experience**|||||
|In-house Benchmark | 62.3 | 47.0 | 49.2 | **72.1** | 40.6 | 34.8 | 13.6 | 56.6 |

<sup>*</sup> Evaluated following a _0-shot CoT_ setting.


## 3. Quickstart
Here we provide a simple example of loading the tokenizer and model to generate content.
```python
from transformers import AutoModelForCausalLM, AutoProcessor, AutoConfig, QuantoConfig, GenerationConfig
import torch
import json
import os
from PIL import Image

# load hf config
hf_config = AutoConfig.from_pretrained("MiniMaxAI/MiniMax-VL-01", trust_remote_code=True)

# quantization config, int8 is recommended
quantization_config =  QuantoConfig(
            weights="int8",
            modules_to_not_convert=[
                "vision_tower",
                "image_newline",
                "multi_modal_projector",
                "lm_head",
                "embed_tokens",
            ] + [f"model.layers.{i}.coefficient" for i in range(hf_config.text_config.num_hidden_layers)]
            + [f"model.layers.{i}.block_sparse_moe.gate" for i in range(hf_config.text_config.num_hidden_layers)]
        )

# set device map
model_safetensors_index_path = os.path.join("MiniMax-VL-01", "model.safetensors.index.json")
with open(model_safetensors_index_path, "r") as f:
    model_safetensors_index = json.load(f)
weight_map = model_safetensors_index['weight_map']
vision_map = {}
for key, value in weight_map.items():
    if 'vision_tower' in key or 'image_newline' in key or 'multi_modal_projector' in key:
        new_key = key.replace('.weight','').replace('.bias','')
        if new_key not in vision_map:
            vision_map[new_key] = value
# assume 8 GPUs
world_size = 8
device_map = {
    'language_model.model.embed_tokens': 'cuda:0',
    'language_model.model.norm': f'cuda:{world_size - 1}',
    'language_model.lm_head': f'cuda:{world_size - 1}'
}
for key, value in vision_map.items():
    device_map[key] = f'cuda:0'
device_map['vision_tower.vision_model.post_layernorm'] = f'cuda:0'
layers_per_device = hf_config.text_config.num_hidden_layers // world_size
for i in range(world_size):
    for j in range(layers_per_device):
        device_map[f'language_model.model.layers.{i * layers_per_device + j}'] = f'cuda:{i}'

# load processor
processor = AutoProcessor.from_pretrained("MiniMaxAI/MiniMax-VL-01", trust_remote_code=True)
messages = [
    {"role": "system", "content": [{"type": "text", "text": "You are a helpful assistant created by MiniMax based on MiniMax-VL-01 model."}]},
    {"role": "user", "content": [{"type": "image", "image": "placeholder"},{"type": "text", "text": "Describe this image."}]},
]
prompt = processor.tokenizer.apply_chat_template(
    messages, tokenize=False, add_generation_prompt=True
)
raw_image = Image.open("figures/image.jpg")
# tokenize and move to device
model_inputs = processor(images=[raw_image], text=prompt, return_tensors='pt').to('cuda').to(torch.bfloat16)

# load bfloat16 model, move to device, and apply quantization
quantized_model = AutoModelForCausalLM.from_pretrained(
    "MiniMaxAI/MiniMax-VL-01",
    torch_dtype="bfloat16",
    device_map=device_map,
    quantization_config=quantization_config,
    trust_remote_code=True,
    offload_buffers=True,
)
generation_config = GenerationConfig(
    max_new_tokens=100,
    eos_token_id=200020,
    use_cache=True,
)

# generate response
generated_ids = quantized_model.generate(**model_inputs, generation_config=generation_config)
print(f"generated_ids: {generated_ids}")
generated_ids = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
]
response = processor.tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
```

# 4. Citation

```
@misc{minimax2025minimax01scalingfoundationmodels,
      title={MiniMax-01: Scaling Foundation Models with Lightning Attention}, 
      author={MiniMax and Aonian Li and Bangwei Gong and Bo Yang and Boji Shan and Chang Liu and Cheng Zhu and Chunhao Zhang and Congchao Guo and Da Chen and Dong Li and Enwei Jiao and Gengxin Li and Guojun Zhang and Haohai Sun and Houze Dong and Jiadai Zhu and Jiaqi Zhuang and Jiayuan Song and Jin Zhu and Jingtao Han and Jingyang Li and Junbin Xie and Junhao Xu and Junjie Yan and Kaishun Zhang and Kecheng Xiao and Kexi Kang and Le Han and Leyang Wang and Lianfei Yu and Liheng Feng and Lin Zheng and Linbo Chai and Long Xing and Meizhi Ju and Mingyuan Chi and Mozhi Zhang and Peikai Huang and Pengcheng Niu and Pengfei Li and Pengyu Zhao and Qi Yang and Qidi Xu and Qiexiang Wang and Qin Wang and Qiuhui Li and Ruitao Leng and Shengmin Shi and Shuqi Yu and Sichen Li and Songquan Zhu and Tao Huang and Tianrun Liang and Weigao Sun and Weixuan Sun and Weiyu Cheng and Wenkai Li and Xiangjun Song and Xiao Su and Xiaodong Han and Xinjie Zhang and Xinzhu Hou and Xu Min and Xun Zou and Xuyang Shen and Yan Gong and Yingjie Zhu and Yipeng Zhou and Yiran Zhong and Yongyi Hu and Yuanxiang Fan and Yue Yu and Yufeng Yang and Yuhao Li and Yunan Huang and Yunji Li and Yunpeng Huang and Yunzhi Xu and Yuxin Mao and Zehan Li and Zekang Li and Zewei Tao and Zewen Ying and Zhaoyang Cong and Zhen Qin and Zhenhua Fan and Zhihang Yu and Zhuo Jiang and Zijia Wu},
      year={2025},
      eprint={2501.08313},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2501.08313}, 
}
```

## 5. Chatbot & API
For general use and evaluation, we provide a [Chatbot](https://chat.minimax.io/) with online search capabilities and the [online API](https://www.minimax.io/platform) for developers.

Contact us at [model@minimaxi.com](mailto:model@minimaxi.com).

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
