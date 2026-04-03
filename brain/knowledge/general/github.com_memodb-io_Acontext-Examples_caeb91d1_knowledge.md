---
id: github.com-memodb-io-acontext-examples-caeb91d1-kn
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:20:24.114571
---

# KNOWLEDGE EXTRACT: github.com_memodb-io_Acontext-Examples_caeb91d1
> **Extracted on:** 2026-04-01 08:38:57
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007519682/github.com_memodb-io_Acontext-Examples_caeb91d1

---

## File: `.gitignore`
```
.DS_Store
.env
__pycache__/
```

## File: `readme.md`
```markdown
## `acontext-cli` examples

[![Made with Acontext](https://assets.memodb.io/Acontext/badge-made-with-acontext-dark.svg)](https://acontext.io)

Supported Examples:

### Python Examples

- `python/acontext-basic`: Core Acontext SDK examples demonstrating session management, task extraction, and artifact handling.
- `python/openai-basic`: Direct OpenAI Python SDK integration with Acontext for multi-turn conversations and manual tool calling.
- `python/openai-agent-basic`: OpenAI Agents SDK with Acontext for persistent sessions, automatic tool execution, and conversation resumption.
- `python/openai-agent-artifacts`: Async ReAct-style agent using OpenAI SDK with Acontext Disk APIs for file operations (write, read, download).
- `python/claude-agent-sdk`: Claude Agent SDK with `ClaudeAgentStorage` for automatic message persistence and session-id discovery.
- `python/agno-basic`: Agno multi-agent framework integration with Acontext for session persistence and task extraction.
- `python/smolagents-basic`: Smolagents (HuggingFace) tool-calling agent with Acontext for session persistence, task extraction, and conversation resumption.
- `python/interactive-agent-skill`: Interactive sandbox demo that uploads Acontext Skills (zip) and runs an OpenAI agentic loop with bash, Python, and file export tools.
- `python/wait-for-user-confirmation`: User confirmation workflow allowing users to review and approve AI-learned patterns before saving to the knowledge base.

### TypeScript Examples

- `typescript/openai-basic`: OpenAI SDK with Acontext integration for session management, task extraction, and conversation history retrieval.
- `typescript/vercel-ai-basic`: Vercel AI SDK with Acontext integration for session management and task extraction.
- `typescript/claude-agent-sdk`: Claude Agent SDK with `ClaudeAgentStorage` for automatic message persistence and session-id discovery.
- `typescript/interactive-agent-skill`: Interactive sandbox demo (TypeScript) that uploads Acontext Skills and runs an OpenAI agentic loop with bash, Python, and file export tools.



### Install/Update cli

```bash
curl -fsSL https://install.acontext.io | sh
```



### Download templates

```bash
acontext create my-project --template-path "python/openai_basic"
```



### Conventions

- We use `uv` as pkg manager for Python Examples
- We use `npm` as pkg manager for Typescript Examples
```

## File: `python/acontext-basic/.env.example`
```
# Acontext API Configuration
ACONTEXT_API_KEY=sk-ac-your-root-api-bearer-token
ACONTEXT_BASE_URL=http://localhost:8029/api/v1
```

## File: `python/acontext-basic/.gitignore`
```
# Environment variables
.env
.env.local

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environments
venv/
env/
ENV/
.venv

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db
```

## File: `python/acontext-basic/.python-version`
```
3.13
```

## File: `python/acontext-basic/README.md`
```markdown
[![Made with Acontext](https://assets.memodb.io/Acontext/badge-made-with-acontext-dark.svg)](https://acontext.io)

# Acontext Examples

This example demonstrates how to use the Acontext Python SDK for session management, task extraction, and artifact handling.

## Overview

This example shows:
- Creating sessions
- Sending messages to sessions
- Retrieving tasks from sessions
- Creating and retrieving artifacts (files)

## Prerequisites

- Python 3.13 or newer
- [uv](https://github.com/astral-sh/uv) package manager
- Acontext API key

## Installation

1. Install dependencies using uv:

```bash
uv sync
```

2. Set up environment variables:

Create a `.env` file in this directory:

```bash
ACONTEXT_API_KEY=your-acontext-api-key
ACONTEXT_BASE_URL=http://localhost:8029/api/v1
```

## Running the Examples

Activate the virtual environment:

```bash
source .venv/bin/activate
```

### Session Example

Run the session example to see how to create sessions, send messages, and retrieve tasks:

```bash
python session.py
```

This example demonstrates:
- Creating a session
- Sending multiple messages (user and assistant messages, including tool calls)
- Flushing the session
- Retrieving and displaying tasks with their status and progress

### Artifacts Example

Run the artifacts example to see how to create and retrieve artifacts:

```bash
python artifacts.py
```

This example demonstrates:
- Creating a disk
- Uploading markdown and PNG files as artifacts
- Retrieving artifacts by file path and filename

```

## File: `python/acontext-basic/artifacts.py`
```python
"""
Main entry point demonstrating Acontext.

This script shows how to:
1. create and get artifacts
"""

import os
from dotenv import load_dotenv
from acontext import AcontextClient
from pathlib import Path


def main():
    # Load environment variables
    load_dotenv()

    # Initialize clients
    acontext_api_key = os.getenv("ACONTEXT_API_KEY")
    acontext_base_url = os.getenv("ACONTEXT_BASE_URL", "http://localhost:8029/api/v1")

    if not acontext_api_key:
        raise ValueError("ACONTEXT_API_KEY environment variable is required")
    
    with AcontextClient(api_key=acontext_api_key, base_url=acontext_base_url) as acontext_client:
        
        # Create a sample markdown file
        markdown_path = Path(__file__).parent / "retro.md"
        if not markdown_path.exists():
            raise FileNotFoundError(f"Markdown file not found: {markdown_path}")
        print(f"Using markdown file: {markdown_path}")

        # Use existing PNG file
        png_path = Path(__file__).parent / "rounded_white.png"
        if not png_path.exists():
            raise FileNotFoundError(f"PNG file not found: {png_path}")
        print(f"Using PNG file: {png_path}")
        
        # Create markdown artifact
        disk = acontext_client.disks.create()
        print("\nCreating markdown artifact...")
        with open(markdown_path, "rb") as f:
            markdown_artifact = acontext_client.artifacts.upsert(
                disk_id=disk.id,
                file=(markdown_path.name, f, "text/markdown"),
                file_path="/notes/",
                meta={"source": "example markdown"},
            )
        print(f"✓ Created markdown artifact: {markdown_artifact.filename}")
        
        # Create PNG artifact
        print("\nCreating PNG artifact...")
        with open(png_path, "rb") as f:
            png_artifact = acontext_client.artifacts.upsert(
                disk_id=disk.id,
                file=(png_path.name, f, "image/png"),
                file_path="/images/",
                meta={"source": "example png"},
            )
        print(f"✓ Created PNG artifact: {png_artifact.filename}")
        
        # Get artifacts
        print("\nRetrieving artifacts...")
        markdown_artifact_retrieved = acontext_client.artifacts.get(
            disk_id=disk.id,
            file_path="/notes/",
            filename="retro.md",
        )
        print(f"✓ Retrieved markdown artifact: {markdown_artifact_retrieved.artifact.filename}")
        
        png_artifact_retrieved = acontext_client.artifacts.get(
            disk_id=disk.id,
            file_path="/images/",
            filename="rounded_white.png",
        )
        print(f"✓ Retrieved PNG artifact: {png_artifact_retrieved.artifact.filename}")
        

if __name__ == "__main__":
    main()
```

## File: `python/acontext-basic/pyproject.toml`
```
[project]
name = "acontext-examples"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.13"
dependencies = [
    "asyncio",
    "acontext>=0.1.18",
    "python-dotenv",
]
```

## File: `python/acontext-basic/retro.md`
```markdown
# Retro Notes

We shipped file uploads successfully!
```

## File: `python/acontext-basic/session.py`
```python
"""
Main entry point demonstrating Acontext.

This script shows how to:
1. create and get sessions, create messages
2. Learn from sessions and retrieve skills
"""

import os
import shutil
from dotenv import load_dotenv
from acontext import AcontextClient


def main():
    # Load environment variables
    load_dotenv()

    # Initialize clients
    acontext_api_key = os.getenv("ACONTEXT_API_KEY")
    acontext_base_url = os.getenv("ACONTEXT_BASE_URL", "http://localhost:8029/api/v1")

    if not acontext_api_key:
        raise ValueError("ACONTEXT_API_KEY environment variable is required")

    with AcontextClient(
        api_key=acontext_api_key, base_url=acontext_base_url
    ) as acontext_client:
        # Create a session
        session = acontext_client.sessions.create()

        messages = [
            {
                "role": "user",
                "parts": [
                    {
                        "type": "text",
                        "text": "I need to write a landing page of iPhone 15 pro max",
                    }
                ],
            },
            {
                "role": "assistant",
                "parts": [
                    {
                        "type": "text",
                        "text": "Sure, my plan is below:\n1. Search for the latest news about iPhone 15 pro max\n2. Init Next.js project for the landing page\n3. Deploy the landing page to the website",
                    }
                ],
            },
            {
                "role": "user",
                "parts": [
                    {
                        "type": "text",
                        "text": "That sounds good. Let's first collect the message and report to me before any landing page coding.",
                    }
                ],
            },
            {
                "role": "assistant",
                "parts": [
                    {
                        "type": "text",
                        "text": "Sure, I will first collect the message then report to you before any landing page coding.",
                    }
                ],
            },
            {
                "role": "assistant",
                "parts": [
                    {
                        "type": "text",
                        "text": "I need to search the latest news about iPhone 15 pro max first",
                    }
                ],
            },
            {
                "role": "assistant",
                "parts": [
                    {
                        "type": "tool-call",
                        "text": "search_news",
                        "meta": {
                            "name": "search_news",
                            "arguments": {"query": "iPhone 15 pro max launching"},
                        },
                    }
                ],
            },
            {
                "role": "assistant",
                "parts": [
                    {
                        "type": "tool-call",
                        "text": "search_news",
                        "meta": {
                            "name": "search_news",
                            "arguments": {"query": "iPhone 15 pro max price"},
                        },
                    }
                ],
            },
            {
                "role": "assistant",
                "parts": [
                    {
                        "type": "tool-call",
                        "text": "search_news",
                        "meta": {
                            "name": "search_news",
                            "arguments": {
                                "query": "iPhone 15 pro max features specifications"
                            },
                        },
                    }
                ],
            },
            {
                "role": "assistant",
                "parts": [
                    {
                        "type": "text",
                        "text": "Based on my search results, here's what I found about the iPhone 15 Pro Max:",
                    }
                ],
            },
            {
                "role": "assistant",
                "parts": [
                    {
                        "type": "text",
                        "text": "## iPhone 15 Pro Max Key Information\n\n**Launch Details:**\n- Released in September 2023\n- Available in Natural Titanium, Blue Titanium, White Titanium, and Black Titanium\n\n**Key Features:**\n- 6.7-inch Super Retina XDR display\n- A17 Pro chip with 6-core GPU\n- Pro camera system with 48MP main camera\n- Action Button replacing the mute switch\n- USB-C connectivity\n- Titanium design\n\n**Pricing:**\n- Starting at $1,199 for 256GB\n- 512GB model at $1,399\n- 1TB model at $1,599\n\nThis information should be perfect for creating an engaging landing page. Should I proceed with initializing the Next.js project?",
                    }
                ],
            },
            {
                "role": "user",
                "parts": [
                    {
                        "type": "text",
                        "text": "Great research! Yes, please proceed with the Next.js project setup.",
                    }
                ],
            },
            {
                "role": "assistant",
                "parts": [
                    {
                        "type": "text",
                        "text": "I'll now create the Next.js project for the iPhone 15 Pro Max landing page.",
                    }
                ],
            },
        ]

        for message in messages:
            acontext_client.sessions.store_message(
                session_id=session.id, blob=message, format="acontext"
            )

        # Create a learning space and trigger learning
        space = acontext_client.learning_spaces.create()
        acontext_client.learning_spaces.learn(space.id, session_id=session.id)
        print(f"\nCreated learning space: {space.id}")

        # Wait for learning to complete
        print("Waiting for learning to complete...")
        result = acontext_client.learning_spaces.wait_for_learning(space.id, session_id=session.id)
        print(f"Learning status: {result.status}")

        # List learned skills
        skills = acontext_client.learning_spaces.list_skills(space.id)
        print(f"\n=== Learned Skills ({len(skills)}) ===")
        for skill in skills:
            print(f"\n  - {skill.name}: {skill.description}")
            print(f"    files: {[f.path for f in skill.file_index]}")

        # Download all skill files
        download_dir = "./skills_output"
        if os.path.exists(download_dir):
            shutil.rmtree(download_dir)

        print(f"\nDownloading skills to {download_dir}/")
        for skill in skills:
            resp = acontext_client.skills.download(skill_id=skill.id, path=f"{download_dir}/{skill.name}")
            print(f"  {resp.name} -> {resp.dir_path}")
            for f in resp.files:
                print(f"    {f}")


if __name__ == "__main__":
    main()
```

## File: `python/acontext-basic/uv.lock`
```
version = 1
revision = 3
requires-python = ">=3.13"

[[package]]
name = "acontext"
version = "0.1.18"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "anthropic" },
    { name = "httpx" },
    { name = "openai" },
    { name = "pydantic" },
    { name = "urllib3" },
]
sdist = { url = "https://files.pythonhosted.org/packages/13/4a/65d6f2f58e03bbbd8a269337a4d99536d8d3f7e9406e70b824a730875dac/acontext-0.1.18.tar.gz", hash = "sha256:7b1e763753fc23f007b4777949095a2ccc6d1b2deac714fad01095619a181824", size = 46865, upload-time = "2026-03-10T05:08:42.095Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/8d/76/bf60d77ab00da4170e9f7dfe42458b87c36b03f24ed2baa8c904d7ed9b97/acontext-0.1.18-py3-none-any.whl", hash = "sha256:a8810fb00f2b75c3509b15df07ab9dfef35dcc785ac07fcd6104ce92446b2b6b", size = 68510, upload-time = "2026-03-10T05:08:41.033Z" },
]

[[package]]
name = "acontext-examples"
version = "0.1.0"
source = { virtual = "." }
dependencies = [
    { name = "acontext" },
    { name = "asyncio" },
    { name = "python-dotenv" },
]

[package.metadata]
requires-dist = [
    { name = "acontext", specifier = ">=0.1.18" },
    { name = "asyncio" },
    { name = "python-dotenv" },
]

[[package]]
name = "annotated-types"
version = "0.7.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/ee/67/531ea369ba64dcff5ec9c3402f9f51bf748cec26dde048a2f973a4eea7f5/annotated_types-0.7.0.tar.gz", hash = "sha256:aff07c09a53a08bc8cfccb9c85b05f1aa9a2a6f23728d790723543408344ce89", size = 16081, upload-time = "2024-05-20T21:33:25.928Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/78/b6/6307fbef88d9b5ee7421e68d78a9f162e0da4900bc5f5793f6d3d0e34fb8/annotated_types-0.7.0-py3-none-any.whl", hash = "sha256:1f02e8b43a8fbbc3f3e0d4f0f4bfc8131bcb4eebe8849b8e5c773f3a1c582a53", size = 13643, upload-time = "2024-05-20T21:33:24.1Z" },
]

[[package]]
name = "anthropic"
version = "0.84.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "anyio" },
    { name = "distro" },
    { name = "docstring-parser" },
    { name = "httpx" },
    { name = "jiter" },
    { name = "pydantic" },
    { name = "sniffio" },
    { name = "typing-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/04/ea/0869d6df9ef83dcf393aeefc12dd81677d091c6ffc86f783e51cf44062f2/anthropic-0.84.0.tar.gz", hash = "sha256:72f5f90e5aebe62dca316cb013629cfa24996b0f5a4593b8c3d712bc03c43c37", size = 539457, upload-time = "2026-02-25T05:22:38.54Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/64/ca/218fa25002a332c0aa149ba18ffc0543175998b1f65de63f6d106689a345/anthropic-0.84.0-py3-none-any.whl", hash = "sha256:861c4c50f91ca45f942e091d83b60530ad6d4f98733bfe648065364da05d29e7", size = 455156, upload-time = "2026-02-25T05:22:40.468Z" },
]

[[package]]
name = "anyio"
version = "4.12.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "idna" },
]
sdist = { url = "https://files.pythonhosted.org/packages/96/f0/5eb65b2bb0d09ac6776f2eb54adee6abe8228ea05b20a5ad0e4945de8aac/anyio-4.12.1.tar.gz", hash = "sha256:41cfcc3a4c85d3f05c932da7c26d0201ac36f72abd4435ba90d0464a3ffed703", size = 228685, upload-time = "2026-01-06T11:45:21.246Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/38/0e/27be9fdef66e72d64c0cdc3cc2823101b80585f8119b5c112c2e8f5f7dab/anyio-4.12.1-py3-none-any.whl", hash = "sha256:d405828884fc140aa80a3c667b8beed277f1dfedec42ba031bd6ac3db606ab6c", size = 113592, upload-time = "2026-01-06T11:45:19.497Z" },
]

[[package]]
name = "asyncio"
version = "4.0.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/71/ea/26c489a11f7ca862d5705db67683a7361ce11c23a7b98fc6c2deaeccede2/asyncio-4.0.0.tar.gz", hash = "sha256:570cd9e50db83bc1629152d4d0b7558d6451bb1bfd5dfc2e935d96fc2f40329b", size = 5371, upload-time = "2025-08-05T02:51:46.605Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/57/64/eff2564783bd650ca25e15938d1c5b459cda997574a510f7de69688cb0b4/asyncio-4.0.0-py3-none-any.whl", hash = "sha256:c1eddb0659231837046809e68103969b2bef8b0400d59cfa6363f6b5ed8cc88b", size = 5555, upload-time = "2025-08-05T02:51:45.767Z" },
]

[[package]]
name = "certifi"
version = "2026.2.25"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/af/2d/7bf41579a8986e348fa033a31cdd0e4121114f6bce2457e8876010b092dd/certifi-2026.2.25.tar.gz", hash = "sha256:e887ab5cee78ea814d3472169153c2d12cd43b14bd03329a39a9c6e2e80bfba7", size = 155029, upload-time = "2026-02-25T02:54:17.342Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/9a/3c/c17fb3ca2d9c3acff52e30b309f538586f9f5b9c9cf454f3845fc9af4881/certifi-2026.2.25-py3-none-any.whl", hash = "sha256:027692e4402ad994f1c42e52a4997a9763c646b73e4096e4d5d6db8af1d6f0fa", size = 153684, upload-time = "2026-02-25T02:54:15.766Z" },
]

[[package]]
name = "colorama"
version = "0.4.6"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/d8/53/6f443c9a4a8358a93a6792e2acffb9d9d5cb0a5cfd8802644b7b1c9a02e4/colorama-0.4.6.tar.gz", hash = "sha256:08695f5cb7ed6e0531a20572697297273c47b8cae5a63ffc6d6ed5c201be6e44", size = 27697, upload-time = "2022-10-25T02:36:22.414Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/d1/d6/3965ed04c63042e047cb6a3e6ed1a63a35087b6a609aa3a15ed8ac56c221/colorama-0.4.6-py2.py3-none-any.whl", hash = "sha256:4f1d9991f5acc0ca119f9d443620b77f9d6b33703e51011c16baf57afb285fc6", size = 25335, upload-time = "2022-10-25T02:36:20.889Z" },
]

[[package]]
name = "distro"
version = "1.9.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/fc/f8/98eea607f65de6527f8a2e8885fc8015d3e6f5775df186e443e0964a11c3/distro-1.9.0.tar.gz", hash = "sha256:2fa77c6fd8940f116ee1d6b94a2f90b13b5ea8d019b98bc8bafdcabcdd9bdbed", size = 60722, upload-time = "2023-12-24T09:54:32.31Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/12/b3/231ffd4ab1fc9d679809f356cebee130ac7daa00d6d6f3206dd4fd137e9e/distro-1.9.0-py3-none-any.whl", hash = "sha256:7bffd925d65168f85027d8da9af6bddab658135b840670a223589bc0c8ef02b2", size = 20277, upload-time = "2023-12-24T09:54:30.421Z" },
]

[[package]]
name = "docstring-parser"
version = "0.17.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/b2/9d/c3b43da9515bd270df0f80548d9944e389870713cc1fe2b8fb35fe2bcefd/docstring_parser-0.17.0.tar.gz", hash = "sha256:583de4a309722b3315439bb31d64ba3eebada841f2e2cee23b99df001434c912", size = 27442, upload-time = "2025-07-21T07:35:01.868Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/55/e2/2537ebcff11c1ee1ff17d8d0b6f4db75873e3b0fb32c2d4a2ee31ecb310a/docstring_parser-0.17.0-py3-none-any.whl", hash = "sha256:cf2569abd23dce8099b300f9b4fa8191e9582dda731fd533daf54c4551658708", size = 36896, upload-time = "2025-07-21T07:35:00.684Z" },
]

[[package]]
name = "h11"
version = "0.16.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/01/ee/02a2c011bdab74c6fb3c75474d40b3052059d95df7e73351460c8588d963/h11-0.16.0.tar.gz", hash = "sha256:4e35b956cf45792e4caa5885e69fba00bdbc6ffafbfa020300e549b208ee5ff1", size = 101250, upload-time = "2025-04-24T03:35:25.427Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/04/4b/29cac41a4d98d144bf5f6d33995617b185d14b22401f75ca86f384e87ff1/h11-0.16.0-py3-none-any.whl", hash = "sha256:63cf8bbe7522de3bf65932fda1d9c2772064ffb3dae62d55932da54b31cb6c86", size = 37515, upload-time = "2025-04-24T03:35:24.344Z" },
]

[[package]]
name = "httpcore"
version = "1.0.9"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "certifi" },
    { name = "h11" },
]
sdist = { url = "https://files.pythonhosted.org/packages/06/94/82699a10bca87a5556c9c59b5963f2d039dbd239f25bc2a63907a05a14cb/httpcore-1.0.9.tar.gz", hash = "sha256:6e34463af53fd2ab5d807f399a9b45ea31c3dfa2276f15a2c3f00afff6e176e8", size = 85484, upload-time = "2025-04-24T22:06:22.219Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/7e/f5/f66802a942d491edb555dd61e3a9961140fd64c90bce1eafd741609d334d/httpcore-1.0.9-py3-none-any.whl", hash = "sha256:2d400746a40668fc9dec9810239072b40b4484b640a8c38fd654a024c7a1bf55", size = 78784, upload-time = "2025-04-24T22:06:20.566Z" },
]

[[package]]
name = "httpx"
version = "0.28.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "anyio" },
    { name = "certifi" },
    { name = "httpcore" },
    { name = "idna" },
]
sdist = { url = "https://files.pythonhosted.org/packages/b1/df/48c586a5fe32a0f01324ee087459e112ebb7224f646c0b5023f5e79e9956/httpx-0.28.1.tar.gz", hash = "sha256:75e98c5f16b0f35b567856f597f06ff2270a374470a5c2392242528e3e3e42fc", size = 141406, upload-time = "2024-12-06T15:37:23.222Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/2a/39/e50c7c3a983047577ee07d2a9e53faf5a69493943ec3f6a384bdc792deb2/httpx-0.28.1-py3-none-any.whl", hash = "sha256:d909fcccc110f8c7faf814ca82a9a4d816bc5a6dbfea25d6591d6985b8ba59ad", size = 73517, upload-time = "2024-12-06T15:37:21.509Z" },
]

[[package]]
name = "idna"
version = "3.11"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/6f/6d/0703ccc57f3a7233505399edb88de3cbd678da106337b9fcde432b65ed60/idna-3.11.tar.gz", hash = "sha256:795dafcc9c04ed0c1fb032c2aa73654d8e8c5023a7df64a53f39190ada629902", size = 194582, upload-time = "2025-10-12T14:55:20.501Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/0e/61/66938bbb5fc52dbdf84594873d5b51fb1f7c7794e9c0f5bd885f30bc507b/idna-3.11-py3-none-any.whl", hash = "sha256:771a87f49d9defaf64091e6e6fe9c18d4833f140bd19464795bc32d966ca37ea", size = 71008, upload-time = "2025-10-12T14:55:18.883Z" },
]

[[package]]
name = "jiter"
version = "0.13.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/0d/5e/4ec91646aee381d01cdb9974e30882c9cd3b8c5d1079d6b5ff4af522439a/jiter-0.13.0.tar.gz", hash = "sha256:f2839f9c2c7e2dffc1bc5929a510e14ce0a946be9365fd1219e7ef342dae14f4", size = 164847, upload-time = "2026-02-02T12:37:56.441Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/91/9c/7ee5a6ff4b9991e1a45263bfc46731634c4a2bde27dfda6c8251df2d958c/jiter-0.13.0-cp313-cp313-macosx_10_12_x86_64.whl", hash = "sha256:1f8a55b848cbabf97d861495cd65f1e5c590246fabca8b48e1747c4dfc8f85bf", size = 306897, upload-time = "2026-02-02T12:36:16.748Z" },
    { url = "https://files.pythonhosted.org/packages/7c/02/be5b870d1d2be5dd6a91bdfb90f248fbb7dcbd21338f092c6b89817c3dbf/jiter-0.13.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:f556aa591c00f2c45eb1b89f68f52441a016034d18b65da60e2d2875bbbf344a", size = 317507, upload-time = "2026-02-02T12:36:18.351Z" },
    { url = "https://files.pythonhosted.org/packages/da/92/b25d2ec333615f5f284f3a4024f7ce68cfa0604c322c6808b2344c7f5d2b/jiter-0.13.0-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:f7e1d61da332ec412350463891923f960c3073cf1aae93b538f0bb4c8cd46efb", size = 350560, upload-time = "2026-02-02T12:36:19.746Z" },
    { url = "https://files.pythonhosted.org/packages/be/ec/74dcb99fef0aca9fbe56b303bf79f6bd839010cb18ad41000bf6cc71eec0/jiter-0.13.0-cp313-cp313-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:3097d665a27bc96fd9bbf7f86178037db139f319f785e4757ce7ccbf390db6c2", size = 363232, upload-time = "2026-02-02T12:36:21.243Z" },
    { url = "https://files.pythonhosted.org/packages/1b/37/f17375e0bb2f6a812d4dd92d7616e41917f740f3e71343627da9db2824ce/jiter-0.13.0-cp313-cp313-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:9d01ecc3a8cbdb6f25a37bd500510550b64ddf9f7d64a107d92f3ccb25035d0f", size = 483727, upload-time = "2026-02-02T12:36:22.688Z" },
    { url = "https://files.pythonhosted.org/packages/77/d2/a71160a5ae1a1e66c1395b37ef77da67513b0adba73b993a27fbe47eb048/jiter-0.13.0-cp313-cp313-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:ed9bbc30f5d60a3bdf63ae76beb3f9db280d7f195dfcfa61af792d6ce912d159", size = 370799, upload-time = "2026-02-02T12:36:24.106Z" },
    { url = "https://files.pythonhosted.org/packages/01/99/ed5e478ff0eb4e8aa5fd998f9d69603c9fd3f32de3bd16c2b1194f68361c/jiter-0.13.0-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:98fbafb6e88256f4454de33c1f40203d09fc33ed19162a68b3b257b29ca7f663", size = 359120, upload-time = "2026-02-02T12:36:25.519Z" },
    { url = "https://files.pythonhosted.org/packages/16/be/7ffd08203277a813f732ba897352797fa9493faf8dc7995b31f3d9cb9488/jiter-0.13.0-cp313-cp313-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:5467696f6b827f1116556cb0db620440380434591e93ecee7fd14d1a491b6daa", size = 390664, upload-time = "2026-02-02T12:36:26.866Z" },
    { url = "https://files.pythonhosted.org/packages/d1/84/e0787856196d6d346264d6dcccb01f741e5f0bd014c1d9a2ebe149caf4f3/jiter-0.13.0-cp313-cp313-musllinux_1_1_aarch64.whl", hash = "sha256:2d08c9475d48b92892583df9da592a0e2ac49bcd41fae1fec4f39ba6cf107820", size = 513543, upload-time = "2026-02-02T12:36:28.217Z" },
    { url = "https://files.pythonhosted.org/packages/65/50/ecbd258181c4313cf79bca6c88fb63207d04d5bf5e4f65174114d072aa55/jiter-0.13.0-cp313-cp313-musllinux_1_1_x86_64.whl", hash = "sha256:aed40e099404721d7fcaf5b89bd3b4568a4666358bcac7b6b15c09fb6252ab68", size = 547262, upload-time = "2026-02-02T12:36:29.678Z" },
    { url = "https://files.pythonhosted.org/packages/27/da/68f38d12e7111d2016cd198161b36e1f042bd115c169255bcb7ec823a3bf/jiter-0.13.0-cp313-cp313-win32.whl", hash = "sha256:36ebfbcffafb146d0e6ffb3e74d51e03d9c35ce7c625c8066cdbfc7b953bdc72", size = 200630, upload-time = "2026-02-02T12:36:31.808Z" },
    { url = "https://files.pythonhosted.org/packages/25/65/3bd1a972c9a08ecd22eb3b08a95d1941ebe6938aea620c246cf426ae09c2/jiter-0.13.0-cp313-cp313-win_amd64.whl", hash = "sha256:8d76029f077379374cf0dbc78dbe45b38dec4a2eb78b08b5194ce836b2517afc", size = 202602, upload-time = "2026-02-02T12:36:33.679Z" },
    { url = "https://files.pythonhosted.org/packages/15/fe/13bd3678a311aa67686bb303654792c48206a112068f8b0b21426eb6851e/jiter-0.13.0-cp313-cp313-win_arm64.whl", hash = "sha256:bb7613e1a427cfcb6ea4544f9ac566b93d5bf67e0d48c787eca673ff9c9dff2b", size = 185939, upload-time = "2026-02-02T12:36:35.065Z" },
    { url = "https://files.pythonhosted.org/packages/49/19/a929ec002ad3228bc97ca01dbb14f7632fffdc84a95ec92ceaf4145688ae/jiter-0.13.0-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:fa476ab5dd49f3bf3a168e05f89358c75a17608dbabb080ef65f96b27c19ab10", size = 316616, upload-time = "2026-02-02T12:36:36.579Z" },
    { url = "https://files.pythonhosted.org/packages/52/56/d19a9a194afa37c1728831e5fb81b7722c3de18a3109e8f282bfc23e587a/jiter-0.13.0-cp313-cp313t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:ade8cb6ff5632a62b7dbd4757d8c5573f7a2e9ae285d6b5b841707d8363205ef", size = 346850, upload-time = "2026-02-02T12:36:38.058Z" },
    { url = "https://files.pythonhosted.org/packages/36/4a/94e831c6bf287754a8a019cb966ed39ff8be6ab78cadecf08df3bb02d505/jiter-0.13.0-cp313-cp313t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:9950290340acc1adaded363edd94baebcee7dabdfa8bee4790794cd5cfad2af6", size = 358551, upload-time = "2026-02-02T12:36:39.417Z" },
    { url = "https://files.pythonhosted.org/packages/a2/ec/a4c72c822695fa80e55d2b4142b73f0012035d9fcf90eccc56bc060db37c/jiter-0.13.0-cp313-cp313t-win_amd64.whl", hash = "sha256:2b4972c6df33731aac0742b64fd0d18e0a69bc7d6e03108ce7d40c85fd9e3e6d", size = 201950, upload-time = "2026-02-02T12:36:40.791Z" },
    { url = "https://files.pythonhosted.org/packages/b6/00/393553ec27b824fbc29047e9c7cd4a3951d7fbe4a76743f17e44034fa4e4/jiter-0.13.0-cp313-cp313t-win_arm64.whl", hash = "sha256:701a1e77d1e593c1b435315ff625fd071f0998c5f02792038a5ca98899261b7d", size = 185852, upload-time = "2026-02-02T12:36:42.077Z" },
    { url = "https://files.pythonhosted.org/packages/6e/f5/f1997e987211f6f9bd71b8083047b316208b4aca0b529bb5f8c96c89ef3e/jiter-0.13.0-cp314-cp314-macosx_10_12_x86_64.whl", hash = "sha256:cc5223ab19fe25e2f0bf2643204ad7318896fe3729bf12fde41b77bfc4fafff0", size = 308804, upload-time = "2026-02-02T12:36:43.496Z" },
    { url = "https://files.pythonhosted.org/packages/cd/8f/5482a7677731fd44881f0204981ce2d7175db271f82cba2085dd2212e095/jiter-0.13.0-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:9776ebe51713acf438fd9b4405fcd86893ae5d03487546dae7f34993217f8a91", size = 318787, upload-time = "2026-02-02T12:36:45.071Z" },
    { url = "https://files.pythonhosted.org/packages/f3/b9/7257ac59778f1cd025b26a23c5520a36a424f7f1b068f2442a5b499b7464/jiter-0.13.0-cp314-cp314-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:879e768938e7b49b5e90b7e3fecc0dbec01b8cb89595861fb39a8967c5220d09", size = 353880, upload-time = "2026-02-02T12:36:47.365Z" },
    { url = "https://files.pythonhosted.org/packages/c3/87/719eec4a3f0841dad99e3d3604ee4cba36af4419a76f3cb0b8e2e691ad67/jiter-0.13.0-cp314-cp314-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:682161a67adea11e3aae9038c06c8b4a9a71023228767477d683f69903ebc607", size = 366702, upload-time = "2026-02-02T12:36:48.871Z" },
    { url = "https://files.pythonhosted.org/packages/d2/65/415f0a75cf6921e43365a1bc227c565cb949caca8b7532776e430cbaa530/jiter-0.13.0-cp314-cp314-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:a13b68cd1cd8cc9de8f244ebae18ccb3e4067ad205220ef324c39181e23bbf66", size = 486319, upload-time = "2026-02-02T12:36:53.006Z" },
    { url = "https://files.pythonhosted.org/packages/54/a2/9e12b48e82c6bbc6081fd81abf915e1443add1b13d8fc586e1d90bb02bb8/jiter-0.13.0-cp314-cp314-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:87ce0f14c6c08892b610686ae8be350bf368467b6acd5085a5b65441e2bf36d2", size = 372289, upload-time = "2026-02-02T12:36:54.593Z" },
    { url = "https://files.pythonhosted.org/packages/4e/c1/e4693f107a1789a239c759a432e9afc592366f04e901470c2af89cfd28e1/jiter-0.13.0-cp314-cp314-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:0c365005b05505a90d1c47856420980d0237adf82f70c4aff7aebd3c1cc143ad", size = 360165, upload-time = "2026-02-02T12:36:56.112Z" },
    { url = "https://files.pythonhosted.org/packages/17/08/91b9ea976c1c758240614bd88442681a87672eebc3d9a6dde476874e706b/jiter-0.13.0-cp314-cp314-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:1317fdffd16f5873e46ce27d0e0f7f4f90f0cdf1d86bf6abeaea9f63ca2c401d", size = 389634, upload-time = "2026-02-02T12:36:57.495Z" },
    { url = "https://files.pythonhosted.org/packages/18/23/58325ef99390d6d40427ed6005bf1ad54f2577866594bcf13ce55675f87d/jiter-0.13.0-cp314-cp314-musllinux_1_1_aarch64.whl", hash = "sha256:c05b450d37ba0c9e21c77fef1f205f56bcee2330bddca68d344baebfc55ae0df", size = 514933, upload-time = "2026-02-02T12:36:58.909Z" },
    { url = "https://files.pythonhosted.org/packages/5b/25/69f1120c7c395fd276c3996bb8adefa9c6b84c12bb7111e5c6ccdcd8526d/jiter-0.13.0-cp314-cp314-musllinux_1_1_x86_64.whl", hash = "sha256:775e10de3849d0631a97c603f996f518159272db00fdda0a780f81752255ee9d", size = 548842, upload-time = "2026-02-02T12:37:00.433Z" },
    { url = "https://files.pythonhosted.org/packages/18/05/981c9669d86850c5fbb0d9e62bba144787f9fba84546ba43d624ee27ef29/jiter-0.13.0-cp314-cp314-win32.whl", hash = "sha256:632bf7c1d28421c00dd8bbb8a3bac5663e1f57d5cd5ed962bce3c73bf62608e6", size = 202108, upload-time = "2026-02-02T12:37:01.718Z" },
    { url = "https://files.pythonhosted.org/packages/8d/96/cdcf54dd0b0341db7d25413229888a346c7130bd20820530905fdb65727b/jiter-0.13.0-cp314-cp314-win_amd64.whl", hash = "sha256:f22ef501c3f87ede88f23f9b11e608581c14f04db59b6a801f354397ae13739f", size = 204027, upload-time = "2026-02-02T12:37:03.075Z" },
    { url = "https://files.pythonhosted.org/packages/fb/f9/724bcaaab7a3cd727031fe4f6995cb86c4bd344909177c186699c8dec51a/jiter-0.13.0-cp314-cp314-win_arm64.whl", hash = "sha256:07b75fe09a4ee8e0c606200622e571e44943f47254f95e2436c8bdcaceb36d7d", size = 187199, upload-time = "2026-02-02T12:37:04.414Z" },
    { url = "https://files.pythonhosted.org/packages/62/92/1661d8b9fd6a3d7a2d89831db26fe3c1509a287d83ad7838831c7b7a5c7e/jiter-0.13.0-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:964538479359059a35fb400e769295d4b315ae61e4105396d355a12f7fef09f0", size = 318423, upload-time = "2026-02-02T12:37:05.806Z" },
    { url = "https://files.pythonhosted.org/packages/4f/3b/f77d342a54d4ebcd128e520fc58ec2f5b30a423b0fd26acdfc0c6fef8e26/jiter-0.13.0-cp314-cp314t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:e104da1db1c0991b3eaed391ccd650ae8d947eab1480c733e5a3fb28d4313e40", size = 351438, upload-time = "2026-02-02T12:37:07.189Z" },
    { url = "https://files.pythonhosted.org/packages/76/b3/ba9a69f0e4209bd3331470c723c2f5509e6f0482e416b612431a5061ed71/jiter-0.13.0-cp314-cp314t-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:0e3a5f0cde8ff433b8e88e41aa40131455420fb3649a3c7abdda6145f8cb7202", size = 364774, upload-time = "2026-02-02T12:37:08.579Z" },
    { url = "https://files.pythonhosted.org/packages/b3/16/6cdb31fa342932602458dbb631bfbd47f601e03d2e4950740e0b2100b570/jiter-0.13.0-cp314-cp314t-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:57aab48f40be1db920a582b30b116fe2435d184f77f0e4226f546794cedd9cf0", size = 487238, upload-time = "2026-02-02T12:37:10.066Z" },
    { url = "https://files.pythonhosted.org/packages/ed/b1/956cc7abaca8d95c13aa8d6c9b3f3797241c246cd6e792934cc4c8b250d2/jiter-0.13.0-cp314-cp314t-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:7772115877c53f62beeb8fd853cab692dbc04374ef623b30f997959a4c0e7e95", size = 372892, upload-time = "2026-02-02T12:37:11.656Z" },
    { url = "https://files.pythonhosted.org/packages/26/c4/97ecde8b1e74f67b8598c57c6fccf6df86ea7861ed29da84629cdbba76c4/jiter-0.13.0-cp314-cp314t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:1211427574b17b633cfceba5040de8081e5abf114f7a7602f73d2e16f9fdaa59", size = 360309, upload-time = "2026-02-02T12:37:13.244Z" },
    { url = "https://files.pythonhosted.org/packages/4b/d7/eabe3cf46715854ccc80be2cd78dd4c36aedeb30751dbf85a1d08c14373c/jiter-0.13.0-cp314-cp314t-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:7beae3a3d3b5212d3a55d2961db3c292e02e302feb43fce6a3f7a31b90ea6dfe", size = 389607, upload-time = "2026-02-02T12:37:14.881Z" },
    { url = "https://files.pythonhosted.org/packages/df/2d/03963fc0804e6109b82decfb9974eb92df3797fe7222428cae12f8ccaa0c/jiter-0.13.0-cp314-cp314t-musllinux_1_1_aarch64.whl", hash = "sha256:e5562a0f0e90a6223b704163ea28e831bd3a9faa3512a711f031611e6b06c939", size = 514986, upload-time = "2026-02-02T12:37:16.326Z" },
    { url = "https://files.pythonhosted.org/packages/f6/6c/8c83b45eb3eb1c1e18d841fe30b4b5bc5619d781267ca9bc03e005d8fd0a/jiter-0.13.0-cp314-cp314t-musllinux_1_1_x86_64.whl", hash = "sha256:6c26a424569a59140fb51160a56df13f438a2b0967365e987889186d5fc2f6f9", size = 548756, upload-time = "2026-02-02T12:37:17.736Z" },
    { url = "https://files.pythonhosted.org/packages/47/66/eea81dfff765ed66c68fd2ed8c96245109e13c896c2a5015c7839c92367e/jiter-0.13.0-cp314-cp314t-win32.whl", hash = "sha256:24dc96eca9f84da4131cdf87a95e6ce36765c3b156fc9ae33280873b1c32d5f6", size = 201196, upload-time = "2026-02-02T12:37:19.101Z" },
    { url = "https://files.pythonhosted.org/packages/ff/32/4ac9c7a76402f8f00d00842a7f6b83b284d0cf7c1e9d4227bc95aa6d17fa/jiter-0.13.0-cp314-cp314t-win_amd64.whl", hash = "sha256:0a8d76c7524087272c8ae913f5d9d608bd839154b62c4322ef65723d2e5bb0b8", size = 204215, upload-time = "2026-02-02T12:37:20.495Z" },
    { url = "https://files.pythonhosted.org/packages/f9/8e/7def204fea9f9be8b3c21a6f2dd6c020cf56c7d5ff753e0e23ed7f9ea57e/jiter-0.13.0-cp314-cp314t-win_arm64.whl", hash = "sha256:2c26cf47e2cad140fa23b6d58d435a7c0161f5c514284802f25e87fddfe11024", size = 187152, upload-time = "2026-02-02T12:37:22.124Z" },
]

[[package]]
name = "openai"
version = "2.26.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "anyio" },
    { name = "distro" },
    { name = "httpx" },
    { name = "jiter" },
    { name = "pydantic" },
    { name = "sniffio" },
    { name = "tqdm" },
    { name = "typing-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/d7/91/2a06c4e9597c338cac1e5e5a8dd6f29e1836fc229c4c523529dca387fda8/openai-2.26.0.tar.gz", hash = "sha256:b41f37c140ae0034a6e92b0c509376d907f3a66109935fba2c1b471a7c05a8fb", size = 666702, upload-time = "2026-03-05T23:17:35.874Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/c6/2e/3f73e8ca53718952222cacd0cf7eecc9db439d020f0c1fe7ae717e4e199a/openai-2.26.0-py3-none-any.whl", hash = "sha256:6151bf8f83802f036117f06cc8a57b3a4da60da9926826cc96747888b57f394f", size = 1136409, upload-time = "2026-03-05T23:17:34.072Z" },
]

[[package]]
name = "pydantic"
version = "2.12.5"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "annotated-types" },
    { name = "pydantic-core" },
    { name = "typing-extensions" },
    { name = "typing-inspection" },
]
sdist = { url = "https://files.pythonhosted.org/packages/69/44/36f1a6e523abc58ae5f928898e4aca2e0ea509b5aa6f6f392a5d882be928/pydantic-2.12.5.tar.gz", hash = "sha256:4d351024c75c0f085a9febbb665ce8c0c6ec5d30e903bdb6394b7ede26aebb49", size = 821591, upload-time = "2025-11-26T15:11:46.471Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/5a/87/b70ad306ebb6f9b585f114d0ac2137d792b48be34d732d60e597c2f8465a/pydantic-2.12.5-py3-none-any.whl", hash = "sha256:e561593fccf61e8a20fc46dfc2dfe075b8be7d0188df33f221ad1f0139180f9d", size = 463580, upload-time = "2025-11-26T15:11:44.605Z" },
]

[[package]]
name = "pydantic-core"
version = "2.41.5"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "typing-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/71/70/23b021c950c2addd24ec408e9ab05d59b035b39d97cdc1130e1bce647bb6/pydantic_core-2.41.5.tar.gz", hash = "sha256:08daa51ea16ad373ffd5e7606252cc32f07bc72b28284b6bc9c6df804816476e", size = 460952, upload-time = "2025-11-04T13:43:49.098Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/87/06/8806241ff1f70d9939f9af039c6c35f2360cf16e93c2ca76f184e76b1564/pydantic_core-2.41.5-cp313-cp313-macosx_10_12_x86_64.whl", hash = "sha256:941103c9be18ac8daf7b7adca8228f8ed6bb7a1849020f643b3a14d15b1924d9", size = 2120403, upload-time = "2025-11-04T13:40:25.248Z" },
    { url = "https://files.pythonhosted.org/packages/94/02/abfa0e0bda67faa65fef1c84971c7e45928e108fe24333c81f3bfe35d5f5/pydantic_core-2.41.5-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:112e305c3314f40c93998e567879e887a3160bb8689ef3d2c04b6cc62c33ac34", size = 1896206, upload-time = "2025-11-04T13:40:27.099Z" },
    { url = "https://files.pythonhosted.org/packages/15/df/a4c740c0943e93e6500f9eb23f4ca7ec9bf71b19e608ae5b579678c8d02f/pydantic_core-2.41.5-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:0cbaad15cb0c90aa221d43c00e77bb33c93e8d36e0bf74760cd00e732d10a6a0", size = 1919307, upload-time = "2025-11-04T13:40:29.806Z" },
    { url = "https://files.pythonhosted.org/packages/9a/e3/6324802931ae1d123528988e0e86587c2072ac2e5394b4bc2bc34b61ff6e/pydantic_core-2.41.5-cp313-cp313-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:03ca43e12fab6023fc79d28ca6b39b05f794ad08ec2feccc59a339b02f2b3d33", size = 2063258, upload-time = "2025-11-04T13:40:33.544Z" },
    { url = "https://files.pythonhosted.org/packages/c9/d4/2230d7151d4957dd79c3044ea26346c148c98fbf0ee6ebd41056f2d62ab5/pydantic_core-2.41.5-cp313-cp313-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:dc799088c08fa04e43144b164feb0c13f9a0bc40503f8df3e9fde58a3c0c101e", size = 2214917, upload-time = "2025-11-04T13:40:35.479Z" },
    { url = "https://files.pythonhosted.org/packages/e6/9f/eaac5df17a3672fef0081b6c1bb0b82b33ee89aa5cec0d7b05f52fd4a1fa/pydantic_core-2.41.5-cp313-cp313-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:97aeba56665b4c3235a0e52b2c2f5ae9cd071b8a8310ad27bddb3f7fb30e9aa2", size = 2332186, upload-time = "2025-11-04T13:40:37.436Z" },
    { url = "https://files.pythonhosted.org/packages/cf/4e/35a80cae583a37cf15604b44240e45c05e04e86f9cfd766623149297e971/pydantic_core-2.41.5-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:406bf18d345822d6c21366031003612b9c77b3e29ffdb0f612367352aab7d586", size = 2073164, upload-time = "2025-11-04T13:40:40.289Z" },
    { url = "https://files.pythonhosted.org/packages/bf/e3/f6e262673c6140dd3305d144d032f7bd5f7497d3871c1428521f19f9efa2/pydantic_core-2.41.5-cp313-cp313-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:b93590ae81f7010dbe380cdeab6f515902ebcbefe0b9327cc4804d74e93ae69d", size = 2179146, upload-time = "2025-11-04T13:40:42.809Z" },
    { url = "https://files.pythonhosted.org/packages/75/c7/20bd7fc05f0c6ea2056a4565c6f36f8968c0924f19b7d97bbfea55780e73/pydantic_core-2.41.5-cp313-cp313-musllinux_1_1_aarch64.whl", hash = "sha256:01a3d0ab748ee531f4ea6c3e48ad9dac84ddba4b0d82291f87248f2f9de8d740", size = 2137788, upload-time = "2025-11-04T13:40:44.752Z" },
    { url = "https://files.pythonhosted.org/packages/3a/8d/34318ef985c45196e004bc46c6eab2eda437e744c124ef0dbe1ff2c9d06b/pydantic_core-2.41.5-cp313-cp313-musllinux_1_1_armv7l.whl", hash = "sha256:6561e94ba9dacc9c61bce40e2d6bdc3bfaa0259d3ff36ace3b1e6901936d2e3e", size = 2340133, upload-time = "2025-11-04T13:40:46.66Z" },
    { url = "https://files.pythonhosted.org/packages/9c/59/013626bf8c78a5a5d9350d12e7697d3d4de951a75565496abd40ccd46bee/pydantic_core-2.41.5-cp313-cp313-musllinux_1_1_x86_64.whl", hash = "sha256:915c3d10f81bec3a74fbd4faebe8391013ba61e5a1a8d48c4455b923bdda7858", size = 2324852, upload-time = "2025-11-04T13:40:48.575Z" },
    { url = "https://files.pythonhosted.org/packages/1a/d9/c248c103856f807ef70c18a4f986693a46a8ffe1602e5d361485da502d20/pydantic_core-2.41.5-cp313-cp313-win32.whl", hash = "sha256:650ae77860b45cfa6e2cdafc42618ceafab3a2d9a3811fcfbd3bbf8ac3c40d36", size = 1994679, upload-time = "2025-11-04T13:40:50.619Z" },
    { url = "https://files.pythonhosted.org/packages/9e/8b/341991b158ddab181cff136acd2552c9f35bd30380422a639c0671e99a91/pydantic_core-2.41.5-cp313-cp313-win_amd64.whl", hash = "sha256:79ec52ec461e99e13791ec6508c722742ad745571f234ea6255bed38c6480f11", size = 2019766, upload-time = "2025-11-04T13:40:52.631Z" },
    { url = "https://files.pythonhosted.org/packages/73/7d/f2f9db34af103bea3e09735bb40b021788a5e834c81eedb541991badf8f5/pydantic_core-2.41.5-cp313-cp313-win_arm64.whl", hash = "sha256:3f84d5c1b4ab906093bdc1ff10484838aca54ef08de4afa9de0f5f14d69639cd", size = 1981005, upload-time = "2025-11-04T13:40:54.734Z" },
    { url = "https://files.pythonhosted.org/packages/ea/28/46b7c5c9635ae96ea0fbb779e271a38129df2550f763937659ee6c5dbc65/pydantic_core-2.41.5-cp314-cp314-macosx_10_12_x86_64.whl", hash = "sha256:3f37a19d7ebcdd20b96485056ba9e8b304e27d9904d233d7b1015db320e51f0a", size = 2119622, upload-time = "2025-11-04T13:40:56.68Z" },
    { url = "https://files.pythonhosted.org/packages/74/1a/145646e5687e8d9a1e8d09acb278c8535ebe9e972e1f162ed338a622f193/pydantic_core-2.41.5-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:1d1d9764366c73f996edd17abb6d9d7649a7eb690006ab6adbda117717099b14", size = 1891725, upload-time = "2025-11-04T13:40:58.807Z" },
    { url = "https://files.pythonhosted.org/packages/23/04/e89c29e267b8060b40dca97bfc64a19b2a3cf99018167ea1677d96368273/pydantic_core-2.41.5-cp314-cp314-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:25e1c2af0fce638d5f1988b686f3b3ea8cd7de5f244ca147c777769e798a9cd1", size = 1915040, upload-time = "2025-11-04T13:41:00.853Z" },
    { url = "https://files.pythonhosted.org/packages/84/a3/15a82ac7bd97992a82257f777b3583d3e84bdb06ba6858f745daa2ec8a85/pydantic_core-2.41.5-cp314-cp314-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:506d766a8727beef16b7adaeb8ee6217c64fc813646b424d0804d67c16eddb66", size = 2063691, upload-time = "2025-11-04T13:41:03.504Z" },
    { url = "https://files.pythonhosted.org/packages/74/9b/0046701313c6ef08c0c1cf0e028c67c770a4e1275ca73131563c5f2a310a/pydantic_core-2.41.5-cp314-cp314-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:4819fa52133c9aa3c387b3328f25c1facc356491e6135b459f1de698ff64d869", size = 2213897, upload-time = "2025-11-04T13:41:05.804Z" },
    { url = "https://files.pythonhosted.org/packages/8a/cd/6bac76ecd1b27e75a95ca3a9a559c643b3afcd2dd62086d4b7a32a18b169/pydantic_core-2.41.5-cp314-cp314-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:2b761d210c9ea91feda40d25b4efe82a1707da2ef62901466a42492c028553a2", size = 2333302, upload-time = "2025-11-04T13:41:07.809Z" },
    { url = "https://files.pythonhosted.org/packages/4c/d2/ef2074dc020dd6e109611a8be4449b98cd25e1b9b8a303c2f0fca2f2bcf7/pydantic_core-2.41.5-cp314-cp314-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:22f0fb8c1c583a3b6f24df2470833b40207e907b90c928cc8d3594b76f874375", size = 2064877, upload-time = "2025-11-04T13:41:09.827Z" },
    { url = "https://files.pythonhosted.org/packages/18/66/e9db17a9a763d72f03de903883c057b2592c09509ccfe468187f2a2eef29/pydantic_core-2.41.5-cp314-cp314-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:2782c870e99878c634505236d81e5443092fba820f0373997ff75f90f68cd553", size = 2180680, upload-time = "2025-11-04T13:41:12.379Z" },
    { url = "https://files.pythonhosted.org/packages/d3/9e/3ce66cebb929f3ced22be85d4c2399b8e85b622db77dad36b73c5387f8f8/pydantic_core-2.41.5-cp314-cp314-musllinux_1_1_aarch64.whl", hash = "sha256:0177272f88ab8312479336e1d777f6b124537d47f2123f89cb37e0accea97f90", size = 2138960, upload-time = "2025-11-04T13:41:14.627Z" },
    { url = "https://files.pythonhosted.org/packages/a6/62/205a998f4327d2079326b01abee48e502ea739d174f0a89295c481a2272e/pydantic_core-2.41.5-cp314-cp314-musllinux_1_1_armv7l.whl", hash = "sha256:63510af5e38f8955b8ee5687740d6ebf7c2a0886d15a6d65c32814613681bc07", size = 2339102, upload-time = "2025-11-04T13:41:16.868Z" },
    { url = "https://files.pythonhosted.org/packages/3c/0d/f05e79471e889d74d3d88f5bd20d0ed189ad94c2423d81ff8d0000aab4ff/pydantic_core-2.41.5-cp314-cp314-musllinux_1_1_x86_64.whl", hash = "sha256:e56ba91f47764cc14f1daacd723e3e82d1a89d783f0f5afe9c364b8bb491ccdb", size = 2326039, upload-time = "2025-11-04T13:41:18.934Z" },
    { url = "https://files.pythonhosted.org/packages/ec/e1/e08a6208bb100da7e0c4b288eed624a703f4d129bde2da475721a80cab32/pydantic_core-2.41.5-cp314-cp314-win32.whl", hash = "sha256:aec5cf2fd867b4ff45b9959f8b20ea3993fc93e63c7363fe6851424c8a7e7c23", size = 1995126, upload-time = "2025-11-04T13:41:21.418Z" },
    { url = "https://files.pythonhosted.org/packages/48/5d/56ba7b24e9557f99c9237e29f5c09913c81eeb2f3217e40e922353668092/pydantic_core-2.41.5-cp314-cp314-win_amd64.whl", hash = "sha256:8e7c86f27c585ef37c35e56a96363ab8de4e549a95512445b85c96d3e2f7c1bf", size = 2015489, upload-time = "2025-11-04T13:41:24.076Z" },
    { url = "https://files.pythonhosted.org/packages/4e/bb/f7a190991ec9e3e0ba22e4993d8755bbc4a32925c0b5b42775c03e8148f9/pydantic_core-2.41.5-cp314-cp314-win_arm64.whl", hash = "sha256:e672ba74fbc2dc8eea59fb6d4aed6845e6905fc2a8afe93175d94a83ba2a01a0", size = 1977288, upload-time = "2025-11-04T13:41:26.33Z" },
    { url = "https://files.pythonhosted.org/packages/92/ed/77542d0c51538e32e15afe7899d79efce4b81eee631d99850edc2f5e9349/pydantic_core-2.41.5-cp314-cp314t-macosx_10_12_x86_64.whl", hash = "sha256:8566def80554c3faa0e65ac30ab0932b9e3a5cd7f8323764303d468e5c37595a", size = 2120255, upload-time = "2025-11-04T13:41:28.569Z" },
    { url = "https://files.pythonhosted.org/packages/bb/3d/6913dde84d5be21e284439676168b28d8bbba5600d838b9dca99de0fad71/pydantic_core-2.41.5-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:b80aa5095cd3109962a298ce14110ae16b8c1aece8b72f9dafe81cf597ad80b3", size = 1863760, upload-time = "2025-11-04T13:41:31.055Z" },
    { url = "https://files.pythonhosted.org/packages/5a/f0/e5e6b99d4191da102f2b0eb9687aaa7f5bea5d9964071a84effc3e40f997/pydantic_core-2.41.5-cp314-cp314t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:3006c3dd9ba34b0c094c544c6006cc79e87d8612999f1a5d43b769b89181f23c", size = 1878092, upload-time = "2025-11-04T13:41:33.21Z" },
    { url = "https://files.pythonhosted.org/packages/71/48/36fb760642d568925953bcc8116455513d6e34c4beaa37544118c36aba6d/pydantic_core-2.41.5-cp314-cp314t-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:72f6c8b11857a856bcfa48c86f5368439f74453563f951e473514579d44aa612", size = 2053385, upload-time = "2025-11-04T13:41:35.508Z" },
    { url = "https://files.pythonhosted.org/packages/20/25/92dc684dd8eb75a234bc1c764b4210cf2646479d54b47bf46061657292a8/pydantic_core-2.41.5-cp314-cp314t-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:5cb1b2f9742240e4bb26b652a5aeb840aa4b417c7748b6f8387927bc6e45e40d", size = 2218832, upload-time = "2025-11-04T13:41:37.732Z" },
    { url = "https://files.pythonhosted.org/packages/e2/09/f53e0b05023d3e30357d82eb35835d0f6340ca344720a4599cd663dca599/pydantic_core-2.41.5-cp314-cp314t-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:bd3d54f38609ff308209bd43acea66061494157703364ae40c951f83ba99a1a9", size = 2327585, upload-time = "2025-11-04T13:41:40Z" },
    { url = "https://files.pythonhosted.org/packages/aa/4e/2ae1aa85d6af35a39b236b1b1641de73f5a6ac4d5a7509f77b814885760c/pydantic_core-2.41.5-cp314-cp314t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:2ff4321e56e879ee8d2a879501c8e469414d948f4aba74a2d4593184eb326660", size = 2041078, upload-time = "2025-11-04T13:41:42.323Z" },
    { url = "https://files.pythonhosted.org/packages/cd/13/2e215f17f0ef326fc72afe94776edb77525142c693767fc347ed6288728d/pydantic_core-2.41.5-cp314-cp314t-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:d0d2568a8c11bf8225044aa94409e21da0cb09dcdafe9ecd10250b2baad531a9", size = 2173914, upload-time = "2025-11-04T13:41:45.221Z" },
    { url = "https://files.pythonhosted.org/packages/02/7a/f999a6dcbcd0e5660bc348a3991c8915ce6599f4f2c6ac22f01d7a10816c/pydantic_core-2.41.5-cp314-cp314t-musllinux_1_1_aarch64.whl", hash = "sha256:a39455728aabd58ceabb03c90e12f71fd30fa69615760a075b9fec596456ccc3", size = 2129560, upload-time = "2025-11-04T13:41:47.474Z" },
    { url = "https://files.pythonhosted.org/packages/3a/b1/6c990ac65e3b4c079a4fb9f5b05f5b013afa0f4ed6780a3dd236d2cbdc64/pydantic_core-2.41.5-cp314-cp314t-musllinux_1_1_armv7l.whl", hash = "sha256:239edca560d05757817c13dc17c50766136d21f7cd0fac50295499ae24f90fdf", size = 2329244, upload-time = "2025-11-04T13:41:49.992Z" },
    { url = "https://files.pythonhosted.org/packages/d9/02/3c562f3a51afd4d88fff8dffb1771b30cfdfd79befd9883ee094f5b6c0d8/pydantic_core-2.41.5-cp314-cp314t-musllinux_1_1_x86_64.whl", hash = "sha256:2a5e06546e19f24c6a96a129142a75cee553cc018ffee48a460059b1185f4470", size = 2331955, upload-time = "2025-11-04T13:41:54.079Z" },
    { url = "https://files.pythonhosted.org/packages/5c/96/5fb7d8c3c17bc8c62fdb031c47d77a1af698f1d7a406b0f79aaa1338f9ad/pydantic_core-2.41.5-cp314-cp314t-win32.whl", hash = "sha256:b4ececa40ac28afa90871c2cc2b9ffd2ff0bf749380fbdf57d165fd23da353aa", size = 1988906, upload-time = "2025-11-04T13:41:56.606Z" },
    { url = "https://files.pythonhosted.org/packages/22/ed/182129d83032702912c2e2d8bbe33c036f342cc735737064668585dac28f/pydantic_core-2.41.5-cp314-cp314t-win_amd64.whl", hash = "sha256:80aa89cad80b32a912a65332f64a4450ed00966111b6615ca6816153d3585a8c", size = 1981607, upload-time = "2025-11-04T13:41:58.889Z" },
    { url = "https://files.pythonhosted.org/packages/9f/ed/068e41660b832bb0b1aa5b58011dea2a3fe0ba7861ff38c4d4904c1c1a99/pydantic_core-2.41.5-cp314-cp314t-win_arm64.whl", hash = "sha256:35b44f37a3199f771c3eaa53051bc8a70cd7b54f333531c59e29fd4db5d15008", size = 1974769, upload-time = "2025-11-04T13:42:01.186Z" },
]

[[package]]
name = "python-dotenv"
version = "1.2.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/82/ed/0301aeeac3e5353ef3d94b6ec08bbcabd04a72018415dcb29e588514bba8/python_dotenv-1.2.2.tar.gz", hash = "sha256:2c371a91fbd7ba082c2c1dc1f8bf89ca22564a087c2c287cd9b662adde799cf3", size = 50135, upload-time = "2026-03-01T16:00:26.196Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/0b/d7/1959b9648791274998a9c3526f6d0ec8fd2233e4d4acce81bbae76b44b2a/python_dotenv-1.2.2-py3-none-any.whl", hash = "sha256:1d8214789a24de455a8b8bd8ae6fe3c6b69a5e3d64aa8a8e5d68e694bbcb285a", size = 22101, upload-time = "2026-03-01T16:00:25.09Z" },
]

[[package]]
name = "sniffio"
version = "1.3.1"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/a2/87/a6771e1546d97e7e041b6ae58d80074f81b7d5121207425c964ddf5cfdbd/sniffio-1.3.1.tar.gz", hash = "sha256:f4324edc670a0f49750a81b895f35c3adb843cca46f0530f79fc1babb23789dc", size = 20372, upload-time = "2024-02-25T23:20:04.057Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/e9/44/75a9c9421471a6c4805dbf2356f7c181a29c1879239abab1ea2cc8f38b40/sniffio-1.3.1-py3-none-any.whl", hash = "sha256:2f6da418d1f1e0fddd844478f41680e794e6051915791a034ff65e5f100525a2", size = 10235, upload-time = "2024-02-25T23:20:01.196Z" },
]

[[package]]
name = "tqdm"
version = "4.67.3"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "colorama", marker = "sys_platform == 'win32'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/09/a9/6ba95a270c6f1fbcd8dac228323f2777d886cb206987444e4bce66338dd4/tqdm-4.67.3.tar.gz", hash = "sha256:7d825f03f89244ef73f1d4ce193cb1774a8179fd96f31d7e1dcde62092b960bb", size = 169598, upload-time = "2026-02-03T17:35:53.048Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/16/e1/3079a9ff9b8e11b846c6ac5c8b5bfb7ff225eee721825310c91b3b50304f/tqdm-4.67.3-py3-none-any.whl", hash = "sha256:ee1e4c0e59148062281c49d80b25b67771a127c85fc9676d3be5f243206826bf", size = 78374, upload-time = "2026-02-03T17:35:50.982Z" },
]

[[package]]
name = "typing-extensions"
version = "4.15.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/72/94/1a15dd82efb362ac84269196e94cf00f187f7ed21c242792a923cdb1c61f/typing_extensions-4.15.0.tar.gz", hash = "sha256:0cea48d173cc12fa28ecabc3b837ea3cf6f38c6d1136f85cbaaf598984861466", size = 109391, upload-time = "2025-08-25T13:49:26.313Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/18/67/36e9267722cc04a6b9f15c7f3441c2363321a3ea07da7ae0c0707beb2a9c/typing_extensions-4.15.0-py3-none-any.whl", hash = "sha256:f0fa19c6845758ab08074a0cfa8b7aecb71c999ca73d62883bc25cc018c4e548", size = 44614, upload-time = "2025-08-25T13:49:24.86Z" },
]

[[package]]
name = "typing-inspection"
version = "0.4.2"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "typing-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/55/e3/70399cb7dd41c10ac53367ae42139cf4b1ca5f36bb3dc6c9d33acdb43655/typing_inspection-0.4.2.tar.gz", hash = "sha256:ba561c48a67c5958007083d386c3295464928b01faa735ab8547c5692e87f464", size = 75949, upload-time = "2025-10-01T02:14:41.687Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/dc/9b/47798a6c91d8bdb567fe2698fe81e0c6b7cb7ef4d13da4114b41d239f65d/typing_inspection-0.4.2-py3-none-any.whl", hash = "sha256:4ed1cacbdc298c220f1bd249ed5287caa16f34d44ef4e9c3d0cbad5b521545e7", size = 14611, upload-time = "2025-10-01T02:14:40.154Z" },
]

[[package]]
name = "urllib3"
version = "2.6.3"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/c7/24/5f1b3bdffd70275f6661c76461e25f024d5a38a46f04aaca912426a2b1d3/urllib3-2.6.3.tar.gz", hash = "sha256:1b62b6884944a57dbe321509ab94fd4d3b307075e0c2eae991ac71ee15ad38ed", size = 435556, upload-time = "2026-01-07T16:24:43.925Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/39/08/aaaad47bc4e9dc8c725e68f9d04865dbcb2052843ff09c97b08904852d84/urllib3-2.6.3-py3-none-any.whl", hash = "sha256:bf272323e553dfb2e87d9bfd225ca7b0f467b919d7bbd355436d3fd37cb0acd4", size = 131584, upload-time = "2026-01-07T16:24:42.685Z" },
]
```

## File: `python/agno-basic/.env.example`
```
# OpenAI API Key
# Get your API key from: https://platform.openai.com/api-keys
OPENAI_API_KEY=your-openai-api-key

# Acontext API Key
# Get your API key from your Acontext dashboard
ACONTEXT_API_KEY=sk-ac-your-root-api-bearer-token

# Acontext Base URL
# Use the default local URL or your deployed Acontext server URL
ACONTEXT_BASE_URL=http://localhost:8029/api/v1
```

## File: `python/agno-basic/.gitignore`
```
# Created by https://www.toptal.com/developers/gitignore/api/python
# Edit at https://www.toptal.com/developers/gitignore?templates=python

### Python ###
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# poetry
#   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
#poetry.lock

# pdm
#   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
#pdm.lock
#   pdm stores project-wide configurations in .pdm.toml, but it is recommended to not include it
#   in version control.
#   https://pdm.fming.dev/#use-with-ide
.pdm.toml

# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# PyCharm
#  JetBrains specific template is maintained in a separate JetBrains.gitignore that can
#  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
#  and can be added to the global gitignore or merged into this file.  For a more nuclear
#  option (not recommended) you can uncomment the following to ignore the entire idea folder.
#.idea/

### Python Patch ###
# Poetry local configuration file - https://python-poetry.org/docs/configuration/#local-configuration
poetry.toml

# ruff
.ruff_cache/

# LSP config files
pyrightconfig.json

# End of https://www.toptal.com/developers/gitignore/api/python

```

## File: `python/agno-basic/.python-version`
```
3.12
```

## File: `python/agno-basic/README.md`
```markdown
[![Made with Acontext](https://assets.memodb.io/Acontext/badge-made-with-acontext-dark.svg)](https://acontext.io)

# Agno with Acontext Example

This example demonstrates how to use [Agno](https://github.com/agno-agi/agno) - a Python framework for building multi-agent systems - with Acontext for session persistence and task extraction.

## Features

- **Multi-turn conversations**: Maintains conversation history across multiple interactions
- **Tool usage**: Demonstrates function calling with `get_weather` and `book_flight` tools
- **Message list input**: Shows how to pass conversation history using Agno's `Message` objects
- **Acontext integration**: Sends conversation messages to Acontext for task extraction and analysis

## How It Works

The example creates an agent that helps plan a trip:

1. **First interaction**: User asks for a 3-day trip plan in Finland
2. **Second interaction**: User requests weather check for Finland
3. **Third interaction**: User books a flight from Shanghai to Finland

After the conversation, all messages are sent to Acontext which:
- Extracts tasks from the conversation
- Tracks progress updates
- Identifies user preferences

## Setup

1. Install dependencies:
```bash
uv sync
```

2. Create a `.env` file with your API keys:
```env
OPENAI_API_KEY=your_openai_key_here
ACONTEXT_API_KEY=your_acontext_key_here
ACONTEXT_BASE_URL=http://localhost:8029/api/v1  # or your Acontext server URL
```

## Running

```bash
python basic_persistent_agent.py
```



## Acontext Integration
Messages in OpenAI format can be sent directly to Acontext without any conversion:

```python
def append_message(message: dict, conversation: list[dict], session_id: str):
    conversation.append(message)
    acontext_client.sessions.store_message(session_id=session_id, blob=message)
    return conversation
```

## Output

The script will:
1. Show the conversation between user and agent
2. Display tool calls (weather checks, flight bookings)
3. Print extracted tasks with their status and metadata
4. Show any progress updates and user preferences identified by Acontext

```

## File: `python/agno-basic/basic_persistent_agent.py`
```python
import asyncio
import os
import shutil
from dotenv import load_dotenv
from rich import print
from agno.agent import Agent, RunOutput
from agno.models.openai import OpenAIChat
from agno.tools import tool
from acontext import AcontextClient

load_dotenv()
acontext_client = AcontextClient(
    api_key=os.getenv("ACONTEXT_API_KEY", "sk-ac-your-root-api-bearer-token"),
    base_url=os.getenv("ACONTEXT_BASE_URL", "http://localhost:8029/api/v1"),
    timeout=60,
)


@tool
def get_weather(city: str) -> str:
    """Returns weather info for the specified city."""
    return f"The weather in {city} is sunny"


@tool
def book_flight(from_city: str, to_city: str, date: str) -> str:
    """Book a flight."""
    # Dummy implementation - returns simulated booking results
    return f"Flight booked successfully for '{from_city}' to '{to_city}' on '{date}'"


def create_agno_agent() -> Agent:
    """Create an agno agent with tools."""
    return Agent(
        name="Assistant",
        model=OpenAIChat(id="gpt-4.1", base_url=os.getenv("OPENAI_BASE_URL", None)),
        instructions="You are a helpful assistant",
        tools=[get_weather, book_flight],
        markdown=True,
        # debug_mode=True,  # Enable debug mode to see tool calls and execution details
    )


def append_messages(
    messages: list[dict], conversation: list[dict], session_id: str
) -> list[dict]:
    messages = messages[1:]  # exclude sys prompt
    new_messages = messages[len(conversation) :]  # exclude already messages
    for m in new_messages:
        conversation = append_message(m, conversation, session_id)
    return conversation


def append_message(message: dict, conversation: list[dict], session_id: str):
    conversation.append(message)
    acontext_client.sessions.store_message(session_id=session_id, blob=message)
    return conversation


async def session_1(session_id: str):

    agent = create_agno_agent()

    # Build conversation history using OpenAI message format
    # This format works with both agno and acontext
    conversation: list[dict] = []

    # First interaction - ask for trip plan
    print("\n=== First interaction: Planning trip ===")
    user_msg_1 = {
        "role": "user",
        "content": "I'd like to have a 3-day trip in Finland. I like to see the nature. Give me the plan",
    }
    conversation = append_message(user_msg_1, conversation, session_id)

    response1: RunOutput = agent.run(conversation)
    print(f"\nAssistant: {response1.content}")
    new_messages = [m.to_dict() for m in response1.messages]

    conversation = append_messages(
        new_messages,
        conversation,
        session_id,
    )

    # Second interaction - check weather
    print("\n\n=== Second interaction: Checking weather ===")
    conversation = append_message(
        {"role": "user", "content": "The plan sounds good, check the weather there"},
        conversation,
        session_id,
    )

    response2: RunOutput = agent.run(conversation)
    print(f"\nAssistant: {response2.content}")

    new_messages = [m.to_dict() for m in response2.messages]

    conversation = append_messages(
        new_messages,
        conversation,
        session_id,
    )

    # Third interaction - book flight
    print("\n\n=== Third interaction: Booking flight ===")
    conversation = append_message(
        {
            "role": "user",
            "content": "The weather is good, I am in Shanghai now, let's book the flight, you should just call the tool and don't ask me for more information. Remember, I only want the cheapest flight.",
        },
        conversation,
        session_id,
    )

    response3: RunOutput = agent.run(conversation)
    print(f"\nAssistant: {response3.content}")

    new_messages = [m.to_dict() for m in response3.messages]

    conversation = append_messages(
        new_messages,
        conversation,
        session_id,
    )

    append_message(
        {
            "role": "user",
            "content": "cool, everything is done, thank you!",
        },
        conversation,
        session_id,
    )

    print(
        f"Saved {len(conversation)} messages in conversation, triggering learning..."
    )

    # Create a learning space and trigger learning
    space = acontext_client.learning_spaces.create()
    acontext_client.learning_spaces.learn(space.id, session_id=session_id)
    print(f"\nCreated learning space: {space.id}")

    # Wait for learning to complete
    print("Waiting for learning to complete...")
    result = acontext_client.learning_spaces.wait_for_learning(space.id, session_id=session_id)
    print(f"Learning status: {result.status}")

    # List learned skills
    skills = acontext_client.learning_spaces.list_skills(space.id)
    print(f"\n=== Learned Skills ({len(skills)}) ===")
    for skill in skills:
        print(f"\n  - {skill.name}: {skill.description}")
        print(f"    files: {[f.path for f in skill.file_index]}")

    # Download all skill files
    download_dir = "./skills_output"
    if os.path.exists(download_dir):
        shutil.rmtree(download_dir)

    print(f"\nDownloading skills to {download_dir}/")
    for skill in skills:
        resp = acontext_client.skills.download(skill_id=skill.id, path=f"{download_dir}/{skill.name}")
        print(f"  {resp.name} -> {resp.dir_path}")
        for f in resp.files:
            print(f"    {f}")


async def session_2(session_id: str):
    agent = create_agno_agent()

    messages = acontext_client.sessions.get_messages(session_id)
    conversation: list[dict] = messages.items
    conversation.append(
        {"role": "user", "content": "Summarize the conversation so far"}
    )
    response: RunOutput = agent.run(conversation)
    print(f"\nAssistant: {response.content}")


async def main():
    session = acontext_client.sessions.create()
    session_id = session.id
    print(f"Created session: {session_id}")

    print("\n=== Session 1 ===")
    await session_1(session_id)

    print("\n=== Session 2, get messages from Acontext and continue ===")
    await session_2(session_id)


    # Close the client after all sessions are complete
    acontext_client.close()


if __name__ == "__main__":
    asyncio.run(main())
```

## File: `python/agno-basic/pyproject.toml`
```
[project]
name = "agno-basic"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.12"
dependencies = [
    "acontext>=0.1.18",
    "agno>=2.2.13",
    "openai>=2.8.0",
    "python-dotenv>=1.0.0",
]
```

## File: `python/agno-basic/uv.lock`
```
version = 1
revision = 3
requires-python = ">=3.12"

[[package]]
name = "acontext"
version = "0.1.18"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "anthropic" },
    { name = "httpx" },
    { name = "openai" },
    { name = "pydantic" },
    { name = "urllib3" },
]
sdist = { url = "https://files.pythonhosted.org/packages/13/4a/65d6f2f58e03bbbd8a269337a4d99536d8d3f7e9406e70b824a730875dac/acontext-0.1.18.tar.gz", hash = "sha256:7b1e763753fc23f007b4777949095a2ccc6d1b2deac714fad01095619a181824", size = 46865, upload-time = "2026-03-10T05:08:42.095Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/8d/76/bf60d77ab00da4170e9f7dfe42458b87c36b03f24ed2baa8c904d7ed9b97/acontext-0.1.18-py3-none-any.whl", hash = "sha256:a8810fb00f2b75c3509b15df07ab9dfef35dcc785ac07fcd6104ce92446b2b6b", size = 68510, upload-time = "2026-03-10T05:08:41.033Z" },
]

[[package]]
name = "agno"
version = "2.5.9"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "docstring-parser" },
    { name = "gitpython" },
    { name = "h11" },
    { name = "httpx", extra = ["http2"] },
    { name = "packaging" },
    { name = "pydantic" },
    { name = "pydantic-settings" },
    { name = "python-dotenv" },
    { name = "python-multipart" },
    { name = "pyyaml" },
    { name = "rich" },
    { name = "typer" },
    { name = "typing-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/4a/ad/accb1cf3063fe1efffe9b41a37cccfa3b81c35486022d5b932668613df68/agno-2.5.9.tar.gz", hash = "sha256:e7a8b713bb49b79fd3b69ae70b3228321f753fd8c28fe0fcf72bcf435db14554", size = 1768973, upload-time = "2026-03-10T15:33:48.854Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/58/c2/ce5a1f02b2def0b50b37a5477bc9e979438b1aceef1d1d8ed3a6a2ab12f6/agno-2.5.9-py3-none-any.whl", hash = "sha256:78161e918a8e0a762da1b5d3e4ee82edb148cd454d710bf52442e5e15e8e6233", size = 2108165, upload-time = "2026-03-10T15:33:46.88Z" },
]

[[package]]
name = "agno-basic"
version = "0.1.0"
source = { virtual = "." }
dependencies = [
    { name = "acontext" },
    { name = "agno" },
    { name = "openai" },
    { name = "python-dotenv" },
]

[package.metadata]
requires-dist = [
    { name = "acontext", specifier = ">=0.1.18" },
    { name = "agno", specifier = ">=2.2.13" },
    { name = "openai", specifier = ">=2.8.0" },
    { name = "python-dotenv", specifier = ">=1.0.0" },
]

[[package]]
name = "annotated-doc"
version = "0.0.4"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/57/ba/046ceea27344560984e26a590f90bc7f4a75b06701f653222458922b558c/annotated_doc-0.0.4.tar.gz", hash = "sha256:fbcda96e87e9c92ad167c2e53839e57503ecfda18804ea28102353485033faa4", size = 7288, upload-time = "2025-11-10T22:07:42.062Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/1e/d3/26bf1008eb3d2daa8ef4cacc7f3bfdc11818d111f7e2d0201bc6e3b49d45/annotated_doc-0.0.4-py3-none-any.whl", hash = "sha256:571ac1dc6991c450b25a9c2d84a3705e2ae7a53467b5d111c24fa8baabbed320", size = 5303, upload-time = "2025-11-10T22:07:40.673Z" },
]

[[package]]
name = "annotated-types"
version = "0.7.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/ee/67/531ea369ba64dcff5ec9c3402f9f51bf748cec26dde048a2f973a4eea7f5/annotated_types-0.7.0.tar.gz", hash = "sha256:aff07c09a53a08bc8cfccb9c85b05f1aa9a2a6f23728d790723543408344ce89", size = 16081, upload-time = "2024-05-20T21:33:25.928Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/78/b6/6307fbef88d9b5ee7421e68d78a9f162e0da4900bc5f5793f6d3d0e34fb8/annotated_types-0.7.0-py3-none-any.whl", hash = "sha256:1f02e8b43a8fbbc3f3e0d4f0f4bfc8131bcb4eebe8849b8e5c773f3a1c582a53", size = 13643, upload-time = "2024-05-20T21:33:24.1Z" },
]

[[package]]
name = "anthropic"
version = "0.84.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "anyio" },
    { name = "distro" },
    { name = "docstring-parser" },
    { name = "httpx" },
    { name = "jiter" },
    { name = "pydantic" },
    { name = "sniffio" },
    { name = "typing-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/04/ea/0869d6df9ef83dcf393aeefc12dd81677d091c6ffc86f783e51cf44062f2/anthropic-0.84.0.tar.gz", hash = "sha256:72f5f90e5aebe62dca316cb013629cfa24996b0f5a4593b8c3d712bc03c43c37", size = 539457, upload-time = "2026-02-25T05:22:38.54Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/64/ca/218fa25002a332c0aa149ba18ffc0543175998b1f65de63f6d106689a345/anthropic-0.84.0-py3-none-any.whl", hash = "sha256:861c4c50f91ca45f942e091d83b60530ad6d4f98733bfe648065364da05d29e7", size = 455156, upload-time = "2026-02-25T05:22:40.468Z" },
]

[[package]]
name = "anyio"
version = "4.12.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "idna" },
    { name = "typing-extensions", marker = "python_full_version < '3.13'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/96/f0/5eb65b2bb0d09ac6776f2eb54adee6abe8228ea05b20a5ad0e4945de8aac/anyio-4.12.1.tar.gz", hash = "sha256:41cfcc3a4c85d3f05c932da7c26d0201ac36f72abd4435ba90d0464a3ffed703", size = 228685, upload-time = "2026-01-06T11:45:21.246Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/38/0e/27be9fdef66e72d64c0cdc3cc2823101b80585f8119b5c112c2e8f5f7dab/anyio-4.12.1-py3-none-any.whl", hash = "sha256:d405828884fc140aa80a3c667b8beed277f1dfedec42ba031bd6ac3db606ab6c", size = 113592, upload-time = "2026-01-06T11:45:19.497Z" },
]

[[package]]
name = "certifi"
version = "2026.2.25"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/af/2d/7bf41579a8986e348fa033a31cdd0e4121114f6bce2457e8876010b092dd/certifi-2026.2.25.tar.gz", hash = "sha256:e887ab5cee78ea814d3472169153c2d12cd43b14bd03329a39a9c6e2e80bfba7", size = 155029, upload-time = "2026-02-25T02:54:17.342Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/9a/3c/c17fb3ca2d9c3acff52e30b309f538586f9f5b9c9cf454f3845fc9af4881/certifi-2026.2.25-py3-none-any.whl", hash = "sha256:027692e4402ad994f1c42e52a4997a9763c646b73e4096e4d5d6db8af1d6f0fa", size = 153684, upload-time = "2026-02-25T02:54:15.766Z" },
]

[[package]]
name = "click"
version = "8.3.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "colorama", marker = "sys_platform == 'win32'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/3d/fa/656b739db8587d7b5dfa22e22ed02566950fbfbcdc20311993483657a5c0/click-8.3.1.tar.gz", hash = "sha256:12ff4785d337a1bb490bb7e9c2b1ee5da3112e94a8622f26a6c77f5d2fc6842a", size = 295065, upload-time = "2025-11-15T20:45:42.706Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/98/78/01c019cdb5d6498122777c1a43056ebb3ebfeef2076d9d026bfe15583b2b/click-8.3.1-py3-none-any.whl", hash = "sha256:981153a64e25f12d547d3426c367a4857371575ee7ad18df2a6183ab0545b2a6", size = 108274, upload-time = "2025-11-15T20:45:41.139Z" },
]

[[package]]
name = "colorama"
version = "0.4.6"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/d8/53/6f443c9a4a8358a93a6792e2acffb9d9d5cb0a5cfd8802644b7b1c9a02e4/colorama-0.4.6.tar.gz", hash = "sha256:08695f5cb7ed6e0531a20572697297273c47b8cae5a63ffc6d6ed5c201be6e44", size = 27697, upload-time = "2022-10-25T02:36:22.414Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/d1/d6/3965ed04c63042e047cb6a3e6ed1a63a35087b6a609aa3a15ed8ac56c221/colorama-0.4.6-py2.py3-none-any.whl", hash = "sha256:4f1d9991f5acc0ca119f9d443620b77f9d6b33703e51011c16baf57afb285fc6", size = 25335, upload-time = "2022-10-25T02:36:20.889Z" },
]

[[package]]
name = "distro"
version = "1.9.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/fc/f8/98eea607f65de6527f8a2e8885fc8015d3e6f5775df186e443e0964a11c3/distro-1.9.0.tar.gz", hash = "sha256:2fa77c6fd8940f116ee1d6b94a2f90b13b5ea8d019b98bc8bafdcabcdd9bdbed", size = 60722, upload-time = "2023-12-24T09:54:32.31Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/12/b3/231ffd4ab1fc9d679809f356cebee130ac7daa00d6d6f3206dd4fd137e9e/distro-1.9.0-py3-none-any.whl", hash = "sha256:7bffd925d65168f85027d8da9af6bddab658135b840670a223589bc0c8ef02b2", size = 20277, upload-time = "2023-12-24T09:54:30.421Z" },
]

[[package]]
name = "docstring-parser"
version = "0.17.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/b2/9d/c3b43da9515bd270df0f80548d9944e389870713cc1fe2b8fb35fe2bcefd/docstring_parser-0.17.0.tar.gz", hash = "sha256:583de4a309722b3315439bb31d64ba3eebada841f2e2cee23b99df001434c912", size = 27442, upload-time = "2025-07-21T07:35:01.868Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/55/e2/2537ebcff11c1ee1ff17d8d0b6f4db75873e3b0fb32c2d4a2ee31ecb310a/docstring_parser-0.17.0-py3-none-any.whl", hash = "sha256:cf2569abd23dce8099b300f9b4fa8191e9582dda731fd533daf54c4551658708", size = 36896, upload-time = "2025-07-21T07:35:00.684Z" },
]

[[package]]
name = "gitdb"
version = "4.0.12"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "smmap" },
]
sdist = { url = "https://files.pythonhosted.org/packages/72/94/63b0fc47eb32792c7ba1fe1b694daec9a63620db1e313033d18140c2320a/gitdb-4.0.12.tar.gz", hash = "sha256:5ef71f855d191a3326fcfbc0d5da835f26b13fbcba60c32c21091c349ffdb571", size = 394684, upload-time = "2025-01-02T07:20:46.413Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/a0/61/5c78b91c3143ed5c14207f463aecfc8f9dbb5092fb2869baf37c273b2705/gitdb-4.0.12-py3-none-any.whl", hash = "sha256:67073e15955400952c6565cc3e707c554a4eea2e428946f7a4c162fab9bd9bcf", size = 62794, upload-time = "2025-01-02T07:20:43.624Z" },
]

[[package]]
name = "gitpython"
version = "3.1.46"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "gitdb" },
]
sdist = { url = "https://files.pythonhosted.org/packages/df/b5/59d16470a1f0dfe8c793f9ef56fd3826093fc52b3bd96d6b9d6c26c7e27b/gitpython-3.1.46.tar.gz", hash = "sha256:400124c7d0ef4ea03f7310ac2fbf7151e09ff97f2a3288d64a440c584a29c37f", size = 215371, upload-time = "2026-01-01T15:37:32.073Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/6a/09/e21df6aef1e1ffc0c816f0522ddc3f6dcded766c3261813131c78a704470/gitpython-3.1.46-py3-none-any.whl", hash = "sha256:79812ed143d9d25b6d176a10bb511de0f9c67b1fa641d82097b0ab90398a2058", size = 208620, upload-time = "2026-01-01T15:37:30.574Z" },
]

[[package]]
name = "h11"
version = "0.16.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/01/ee/02a2c011bdab74c6fb3c75474d40b3052059d95df7e73351460c8588d963/h11-0.16.0.tar.gz", hash = "sha256:4e35b956cf45792e4caa5885e69fba00bdbc6ffafbfa020300e549b208ee5ff1", size = 101250, upload-time = "2025-04-24T03:35:25.427Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/04/4b/29cac41a4d98d144bf5f6d33995617b185d14b22401f75ca86f384e87ff1/h11-0.16.0-py3-none-any.whl", hash = "sha256:63cf8bbe7522de3bf65932fda1d9c2772064ffb3dae62d55932da54b31cb6c86", size = 37515, upload-time = "2025-04-24T03:35:24.344Z" },
]

[[package]]
name = "h2"
version = "4.3.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "hpack" },
    { name = "hyperframe" },
]
sdist = { url = "https://files.pythonhosted.org/packages/1d/17/afa56379f94ad0fe8defd37d6eb3f89a25404ffc71d4d848893d270325fc/h2-4.3.0.tar.gz", hash = "sha256:6c59efe4323fa18b47a632221a1888bd7fde6249819beda254aeca909f221bf1", size = 2152026, upload-time = "2025-08-23T18:12:19.778Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/69/b2/119f6e6dcbd96f9069ce9a2665e0146588dc9f88f29549711853645e736a/h2-4.3.0-py3-none-any.whl", hash = "sha256:c438f029a25f7945c69e0ccf0fb951dc3f73a5f6412981daee861431b70e2bdd", size = 61779, upload-time = "2025-08-23T18:12:17.779Z" },
]

[[package]]
name = "hpack"
version = "4.1.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/2c/48/71de9ed269fdae9c8057e5a4c0aa7402e8bb16f2c6e90b3aa53327b113f8/hpack-4.1.0.tar.gz", hash = "sha256:ec5eca154f7056aa06f196a557655c5b009b382873ac8d1e66e79e87535f1dca", size = 51276, upload-time = "2025-01-22T21:44:58.347Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/07/c6/80c95b1b2b94682a72cbdbfb85b81ae2daffa4291fbfa1b1464502ede10d/hpack-4.1.0-py3-none-any.whl", hash = "sha256:157ac792668d995c657d93111f46b4535ed114f0c9c8d672271bbec7eae1b496", size = 34357, upload-time = "2025-01-22T21:44:56.92Z" },
]

[[package]]
name = "httpcore"
version = "1.0.9"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "certifi" },
    { name = "h11" },
]
sdist = { url = "https://files.pythonhosted.org/packages/06/94/82699a10bca87a5556c9c59b5963f2d039dbd239f25bc2a63907a05a14cb/httpcore-1.0.9.tar.gz", hash = "sha256:6e34463af53fd2ab5d807f399a9b45ea31c3dfa2276f15a2c3f00afff6e176e8", size = 85484, upload-time = "2025-04-24T22:06:22.219Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/7e/f5/f66802a942d491edb555dd61e3a9961140fd64c90bce1eafd741609d334d/httpcore-1.0.9-py3-none-any.whl", hash = "sha256:2d400746a40668fc9dec9810239072b40b4484b640a8c38fd654a024c7a1bf55", size = 78784, upload-time = "2025-04-24T22:06:20.566Z" },
]

[[package]]
name = "httpx"
version = "0.28.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "anyio" },
    { name = "certifi" },
    { name = "httpcore" },
    { name = "idna" },
]
sdist = { url = "https://files.pythonhosted.org/packages/b1/df/48c586a5fe32a0f01324ee087459e112ebb7224f646c0b5023f5e79e9956/httpx-0.28.1.tar.gz", hash = "sha256:75e98c5f16b0f35b567856f597f06ff2270a374470a5c2392242528e3e3e42fc", size = 141406, upload-time = "2024-12-06T15:37:23.222Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/2a/39/e50c7c3a983047577ee07d2a9e53faf5a69493943ec3f6a384bdc792deb2/httpx-0.28.1-py3-none-any.whl", hash = "sha256:d909fcccc110f8c7faf814ca82a9a4d816bc5a6dbfea25d6591d6985b8ba59ad", size = 73517, upload-time = "2024-12-06T15:37:21.509Z" },
]

[package.optional-dependencies]
http2 = [
    { name = "h2" },
]

[[package]]
name = "hyperframe"
version = "6.1.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/02/e7/94f8232d4a74cc99514c13a9f995811485a6903d48e5d952771ef6322e30/hyperframe-6.1.0.tar.gz", hash = "sha256:f630908a00854a7adeabd6382b43923a4c4cd4b821fcb527e6ab9e15382a3b08", size = 26566, upload-time = "2025-01-22T21:41:49.302Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/48/30/47d0bf6072f7252e6521f3447ccfa40b421b6824517f82854703d0f5a98b/hyperframe-6.1.0-py3-none-any.whl", hash = "sha256:b03380493a519fce58ea5af42e4a42317bf9bd425596f7a0835ffce80f1a42e5", size = 13007, upload-time = "2025-01-22T21:41:47.295Z" },
]

[[package]]
name = "idna"
version = "3.11"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/6f/6d/0703ccc57f3a7233505399edb88de3cbd678da106337b9fcde432b65ed60/idna-3.11.tar.gz", hash = "sha256:795dafcc9c04ed0c1fb032c2aa73654d8e8c5023a7df64a53f39190ada629902", size = 194582, upload-time = "2025-10-12T14:55:20.501Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/0e/61/66938bbb5fc52dbdf84594873d5b51fb1f7c7794e9c0f5bd885f30bc507b/idna-3.11-py3-none-any.whl", hash = "sha256:771a87f49d9defaf64091e6e6fe9c18d4833f140bd19464795bc32d966ca37ea", size = 71008, upload-time = "2025-10-12T14:55:18.883Z" },
]

[[package]]
name = "jiter"
version = "0.13.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/0d/5e/4ec91646aee381d01cdb9974e30882c9cd3b8c5d1079d6b5ff4af522439a/jiter-0.13.0.tar.gz", hash = "sha256:f2839f9c2c7e2dffc1bc5929a510e14ce0a946be9365fd1219e7ef342dae14f4", size = 164847, upload-time = "2026-02-02T12:37:56.441Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/2e/30/7687e4f87086829955013ca12a9233523349767f69653ebc27036313def9/jiter-0.13.0-cp312-cp312-macosx_10_12_x86_64.whl", hash = "sha256:0a2bd69fc1d902e89925fc34d1da51b2128019423d7b339a45d9e99c894e0663", size = 307958, upload-time = "2026-02-02T12:35:57.165Z" },
    { url = "https://files.pythonhosted.org/packages/c3/27/e57f9a783246ed95481e6749cc5002a8a767a73177a83c63ea71f0528b90/jiter-0.13.0-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:f917a04240ef31898182f76a332f508f2cc4b57d2b4d7ad2dbfebbfe167eb505", size = 318597, upload-time = "2026-02-02T12:35:58.591Z" },
    { url = "https://files.pythonhosted.org/packages/cf/52/e5719a60ac5d4d7c5995461a94ad5ef962a37c8bf5b088390e6fad59b2ff/jiter-0.13.0-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:c1e2b199f446d3e82246b4fd9236d7cb502dc2222b18698ba0d986d2fecc6152", size = 348821, upload-time = "2026-02-02T12:36:00.093Z" },
    { url = "https://files.pythonhosted.org/packages/61/db/c1efc32b8ba4c740ab3fc2d037d8753f67685f475e26b9d6536a4322bcdd/jiter-0.13.0-cp312-cp312-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:04670992b576fa65bd056dbac0c39fe8bd67681c380cb2b48efa885711d9d726", size = 364163, upload-time = "2026-02-02T12:36:01.937Z" },
    { url = "https://files.pythonhosted.org/packages/55/8a/fb75556236047c8806995671a18e4a0ad646ed255276f51a20f32dceaeec/jiter-0.13.0-cp312-cp312-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:5a1aff1fbdb803a376d4d22a8f63f8e7ccbce0b4890c26cc7af9e501ab339ef0", size = 483709, upload-time = "2026-02-02T12:36:03.41Z" },
    { url = "https://files.pythonhosted.org/packages/7e/16/43512e6ee863875693a8e6f6d532e19d650779d6ba9a81593ae40a9088ff/jiter-0.13.0-cp312-cp312-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:3b3fb8c2053acaef8580809ac1d1f7481a0a0bdc012fd7f5d8b18fb696a5a089", size = 370480, upload-time = "2026-02-02T12:36:04.791Z" },
    { url = "https://files.pythonhosted.org/packages/f8/4c/09b93e30e984a187bc8aaa3510e1ec8dcbdcd71ca05d2f56aac0492453aa/jiter-0.13.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:bdaba7d87e66f26a2c45d8cbadcbfc4bf7884182317907baf39cfe9775bb4d93", size = 360735, upload-time = "2026-02-02T12:36:06.994Z" },
    { url = "https://files.pythonhosted.org/packages/1a/1b/46c5e349019874ec5dfa508c14c37e29864ea108d376ae26d90bee238cd7/jiter-0.13.0-cp312-cp312-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:7b88d649135aca526da172e48083da915ec086b54e8e73a425ba50999468cc08", size = 391814, upload-time = "2026-02-02T12:36:08.368Z" },
    { url = "https://files.pythonhosted.org/packages/15/9e/26184760e85baee7162ad37b7912797d2077718476bf91517641c92b3639/jiter-0.13.0-cp312-cp312-musllinux_1_1_aarch64.whl", hash = "sha256:e404ea551d35438013c64b4f357b0474c7abf9f781c06d44fcaf7a14c69ff9e2", size = 513990, upload-time = "2026-02-02T12:36:09.993Z" },
    { url = "https://files.pythonhosted.org/packages/e9/34/2c9355247d6debad57a0a15e76ab1566ab799388042743656e566b3b7de1/jiter-0.13.0-cp312-cp312-musllinux_1_1_x86_64.whl", hash = "sha256:1f4748aad1b4a93c8bdd70f604d0f748cdc0e8744c5547798acfa52f10e79228", size = 548021, upload-time = "2026-02-02T12:36:11.376Z" },
    { url = "https://files.pythonhosted.org/packages/ac/4a/9f2c23255d04a834398b9c2e0e665382116911dc4d06b795710503cdad25/jiter-0.13.0-cp312-cp312-win32.whl", hash = "sha256:0bf670e3b1445fc4d31612199f1744f67f889ee1bbae703c4b54dc097e5dd394", size = 203024, upload-time = "2026-02-02T12:36:12.682Z" },
    { url = "https://files.pythonhosted.org/packages/09/ee/f0ae675a957ae5a8f160be3e87acea6b11dc7b89f6b7ab057e77b2d2b13a/jiter-0.13.0-cp312-cp312-win_amd64.whl", hash = "sha256:15db60e121e11fe186c0b15236bd5d18381b9ddacdcf4e659feb96fc6c969c92", size = 205424, upload-time = "2026-02-02T12:36:13.93Z" },
    { url = "https://files.pythonhosted.org/packages/1b/02/ae611edf913d3cbf02c97cdb90374af2082c48d7190d74c1111dde08bcdd/jiter-0.13.0-cp312-cp312-win_arm64.whl", hash = "sha256:41f92313d17989102f3cb5dd533a02787cdb99454d494344b0361355da52fcb9", size = 186818, upload-time = "2026-02-02T12:36:15.308Z" },
    { url = "https://files.pythonhosted.org/packages/91/9c/7ee5a6ff4b9991e1a45263bfc46731634c4a2bde27dfda6c8251df2d958c/jiter-0.13.0-cp313-cp313-macosx_10_12_x86_64.whl", hash = "sha256:1f8a55b848cbabf97d861495cd65f1e5c590246fabca8b48e1747c4dfc8f85bf", size = 306897, upload-time = "2026-02-02T12:36:16.748Z" },
    { url = "https://files.pythonhosted.org/packages/7c/02/be5b870d1d2be5dd6a91bdfb90f248fbb7dcbd21338f092c6b89817c3dbf/jiter-0.13.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:f556aa591c00f2c45eb1b89f68f52441a016034d18b65da60e2d2875bbbf344a", size = 317507, upload-time = "2026-02-02T12:36:18.351Z" },
    { url = "https://files.pythonhosted.org/packages/da/92/b25d2ec333615f5f284f3a4024f7ce68cfa0604c322c6808b2344c7f5d2b/jiter-0.13.0-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:f7e1d61da332ec412350463891923f960c3073cf1aae93b538f0bb4c8cd46efb", size = 350560, upload-time = "2026-02-02T12:36:19.746Z" },
    { url = "https://files.pythonhosted.org/packages/be/ec/74dcb99fef0aca9fbe56b303bf79f6bd839010cb18ad41000bf6cc71eec0/jiter-0.13.0-cp313-cp313-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:3097d665a27bc96fd9bbf7f86178037db139f319f785e4757ce7ccbf390db6c2", size = 363232, upload-time = "2026-02-02T12:36:21.243Z" },
    { url = "https://files.pythonhosted.org/packages/1b/37/f17375e0bb2f6a812d4dd92d7616e41917f740f3e71343627da9db2824ce/jiter-0.13.0-cp313-cp313-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:9d01ecc3a8cbdb6f25a37bd500510550b64ddf9f7d64a107d92f3ccb25035d0f", size = 483727, upload-time = "2026-02-02T12:36:22.688Z" },
    { url = "https://files.pythonhosted.org/packages/77/d2/a71160a5ae1a1e66c1395b37ef77da67513b0adba73b993a27fbe47eb048/jiter-0.13.0-cp313-cp313-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:ed9bbc30f5d60a3bdf63ae76beb3f9db280d7f195dfcfa61af792d6ce912d159", size = 370799, upload-time = "2026-02-02T12:36:24.106Z" },
    { url = "https://files.pythonhosted.org/packages/01/99/ed5e478ff0eb4e8aa5fd998f9d69603c9fd3f32de3bd16c2b1194f68361c/jiter-0.13.0-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:98fbafb6e88256f4454de33c1f40203d09fc33ed19162a68b3b257b29ca7f663", size = 359120, upload-time = "2026-02-02T12:36:25.519Z" },
    { url = "https://files.pythonhosted.org/packages/16/be/7ffd08203277a813f732ba897352797fa9493faf8dc7995b31f3d9cb9488/jiter-0.13.0-cp313-cp313-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:5467696f6b827f1116556cb0db620440380434591e93ecee7fd14d1a491b6daa", size = 390664, upload-time = "2026-02-02T12:36:26.866Z" },
    { url = "https://files.pythonhosted.org/packages/d1/84/e0787856196d6d346264d6dcccb01f741e5f0bd014c1d9a2ebe149caf4f3/jiter-0.13.0-cp313-cp313-musllinux_1_1_aarch64.whl", hash = "sha256:2d08c9475d48b92892583df9da592a0e2ac49bcd41fae1fec4f39ba6cf107820", size = 513543, upload-time = "2026-02-02T12:36:28.217Z" },
    { url = "https://files.pythonhosted.org/packages/65/50/ecbd258181c4313cf79bca6c88fb63207d04d5bf5e4f65174114d072aa55/jiter-0.13.0-cp313-cp313-musllinux_1_1_x86_64.whl", hash = "sha256:aed40e099404721d7fcaf5b89bd3b4568a4666358bcac7b6b15c09fb6252ab68", size = 547262, upload-time = "2026-02-02T12:36:29.678Z" },
    { url = "https://files.pythonhosted.org/packages/27/da/68f38d12e7111d2016cd198161b36e1f042bd115c169255bcb7ec823a3bf/jiter-0.13.0-cp313-cp313-win32.whl", hash = "sha256:36ebfbcffafb146d0e6ffb3e74d51e03d9c35ce7c625c8066cdbfc7b953bdc72", size = 200630, upload-time = "2026-02-02T12:36:31.808Z" },
    { url = "https://files.pythonhosted.org/packages/25/65/3bd1a972c9a08ecd22eb3b08a95d1941ebe6938aea620c246cf426ae09c2/jiter-0.13.0-cp313-cp313-win_amd64.whl", hash = "sha256:8d76029f077379374cf0dbc78dbe45b38dec4a2eb78b08b5194ce836b2517afc", size = 202602, upload-time = "2026-02-02T12:36:33.679Z" },
    { url = "https://files.pythonhosted.org/packages/15/fe/13bd3678a311aa67686bb303654792c48206a112068f8b0b21426eb6851e/jiter-0.13.0-cp313-cp313-win_arm64.whl", hash = "sha256:bb7613e1a427cfcb6ea4544f9ac566b93d5bf67e0d48c787eca673ff9c9dff2b", size = 185939, upload-time = "2026-02-02T12:36:35.065Z" },
    { url = "https://files.pythonhosted.org/packages/49/19/a929ec002ad3228bc97ca01dbb14f7632fffdc84a95ec92ceaf4145688ae/jiter-0.13.0-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:fa476ab5dd49f3bf3a168e05f89358c75a17608dbabb080ef65f96b27c19ab10", size = 316616, upload-time = "2026-02-02T12:36:36.579Z" },
    { url = "https://files.pythonhosted.org/packages/52/56/d19a9a194afa37c1728831e5fb81b7722c3de18a3109e8f282bfc23e587a/jiter-0.13.0-cp313-cp313t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:ade8cb6ff5632a62b7dbd4757d8c5573f7a2e9ae285d6b5b841707d8363205ef", size = 346850, upload-time = "2026-02-02T12:36:38.058Z" },
    { url = "https://files.pythonhosted.org/packages/36/4a/94e831c6bf287754a8a019cb966ed39ff8be6ab78cadecf08df3bb02d505/jiter-0.13.0-cp313-cp313t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:9950290340acc1adaded363edd94baebcee7dabdfa8bee4790794cd5cfad2af6", size = 358551, upload-time = "2026-02-02T12:36:39.417Z" },
    { url = "https://files.pythonhosted.org/packages/a2/ec/a4c72c822695fa80e55d2b4142b73f0012035d9fcf90eccc56bc060db37c/jiter-0.13.0-cp313-cp313t-win_amd64.whl", hash = "sha256:2b4972c6df33731aac0742b64fd0d18e0a69bc7d6e03108ce7d40c85fd9e3e6d", size = 201950, upload-time = "2026-02-02T12:36:40.791Z" },
    { url = "https://files.pythonhosted.org/packages/b6/00/393553ec27b824fbc29047e9c7cd4a3951d7fbe4a76743f17e44034fa4e4/jiter-0.13.0-cp313-cp313t-win_arm64.whl", hash = "sha256:701a1e77d1e593c1b435315ff625fd071f0998c5f02792038a5ca98899261b7d", size = 185852, upload-time = "2026-02-02T12:36:42.077Z" },
    { url = "https://files.pythonhosted.org/packages/6e/f5/f1997e987211f6f9bd71b8083047b316208b4aca0b529bb5f8c96c89ef3e/jiter-0.13.0-cp314-cp314-macosx_10_12_x86_64.whl", hash = "sha256:cc5223ab19fe25e2f0bf2643204ad7318896fe3729bf12fde41b77bfc4fafff0", size = 308804, upload-time = "2026-02-02T12:36:43.496Z" },
    { url = "https://files.pythonhosted.org/packages/cd/8f/5482a7677731fd44881f0204981ce2d7175db271f82cba2085dd2212e095/jiter-0.13.0-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:9776ebe51713acf438fd9b4405fcd86893ae5d03487546dae7f34993217f8a91", size = 318787, upload-time = "2026-02-02T12:36:45.071Z" },
    { url = "https://files.pythonhosted.org/packages/f3/b9/7257ac59778f1cd025b26a23c5520a36a424f7f1b068f2442a5b499b7464/jiter-0.13.0-cp314-cp314-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:879e768938e7b49b5e90b7e3fecc0dbec01b8cb89595861fb39a8967c5220d09", size = 353880, upload-time = "2026-02-02T12:36:47.365Z" },
    { url = "https://files.pythonhosted.org/packages/c3/87/719eec4a3f0841dad99e3d3604ee4cba36af4419a76f3cb0b8e2e691ad67/jiter-0.13.0-cp314-cp314-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:682161a67adea11e3aae9038c06c8b4a9a71023228767477d683f69903ebc607", size = 366702, upload-time = "2026-02-02T12:36:48.871Z" },
    { url = "https://files.pythonhosted.org/packages/d2/65/415f0a75cf6921e43365a1bc227c565cb949caca8b7532776e430cbaa530/jiter-0.13.0-cp314-cp314-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:a13b68cd1cd8cc9de8f244ebae18ccb3e4067ad205220ef324c39181e23bbf66", size = 486319, upload-time = "2026-02-02T12:36:53.006Z" },
    { url = "https://files.pythonhosted.org/packages/54/a2/9e12b48e82c6bbc6081fd81abf915e1443add1b13d8fc586e1d90bb02bb8/jiter-0.13.0-cp314-cp314-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:87ce0f14c6c08892b610686ae8be350bf368467b6acd5085a5b65441e2bf36d2", size = 372289, upload-time = "2026-02-02T12:36:54.593Z" },
    { url = "https://files.pythonhosted.org/packages/4e/c1/e4693f107a1789a239c759a432e9afc592366f04e901470c2af89cfd28e1/jiter-0.13.0-cp314-cp314-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:0c365005b05505a90d1c47856420980d0237adf82f70c4aff7aebd3c1cc143ad", size = 360165, upload-time = "2026-02-02T12:36:56.112Z" },
    { url = "https://files.pythonhosted.org/packages/17/08/91b9ea976c1c758240614bd88442681a87672eebc3d9a6dde476874e706b/jiter-0.13.0-cp314-cp314-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:1317fdffd16f5873e46ce27d0e0f7f4f90f0cdf1d86bf6abeaea9f63ca2c401d", size = 389634, upload-time = "2026-02-02T12:36:57.495Z" },
    { url = "https://files.pythonhosted.org/packages/18/23/58325ef99390d6d40427ed6005bf1ad54f2577866594bcf13ce55675f87d/jiter-0.13.0-cp314-cp314-musllinux_1_1_aarch64.whl", hash = "sha256:c05b450d37ba0c9e21c77fef1f205f56bcee2330bddca68d344baebfc55ae0df", size = 514933, upload-time = "2026-02-02T12:36:58.909Z" },
    { url = "https://files.pythonhosted.org/packages/5b/25/69f1120c7c395fd276c3996bb8adefa9c6b84c12bb7111e5c6ccdcd8526d/jiter-0.13.0-cp314-cp314-musllinux_1_1_x86_64.whl", hash = "sha256:775e10de3849d0631a97c603f996f518159272db00fdda0a780f81752255ee9d", size = 548842, upload-time = "2026-02-02T12:37:00.433Z" },
    { url = "https://files.pythonhosted.org/packages/18/05/981c9669d86850c5fbb0d9e62bba144787f9fba84546ba43d624ee27ef29/jiter-0.13.0-cp314-cp314-win32.whl", hash = "sha256:632bf7c1d28421c00dd8bbb8a3bac5663e1f57d5cd5ed962bce3c73bf62608e6", size = 202108, upload-time = "2026-02-02T12:37:01.718Z" },
    { url = "https://files.pythonhosted.org/packages/8d/96/cdcf54dd0b0341db7d25413229888a346c7130bd20820530905fdb65727b/jiter-0.13.0-cp314-cp314-win_amd64.whl", hash = "sha256:f22ef501c3f87ede88f23f9b11e608581c14f04db59b6a801f354397ae13739f", size = 204027, upload-time = "2026-02-02T12:37:03.075Z" },
    { url = "https://files.pythonhosted.org/packages/fb/f9/724bcaaab7a3cd727031fe4f6995cb86c4bd344909177c186699c8dec51a/jiter-0.13.0-cp314-cp314-win_arm64.whl", hash = "sha256:07b75fe09a4ee8e0c606200622e571e44943f47254f95e2436c8bdcaceb36d7d", size = 187199, upload-time = "2026-02-02T12:37:04.414Z" },
    { url = "https://files.pythonhosted.org/packages/62/92/1661d8b9fd6a3d7a2d89831db26fe3c1509a287d83ad7838831c7b7a5c7e/jiter-0.13.0-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:964538479359059a35fb400e769295d4b315ae61e4105396d355a12f7fef09f0", size = 318423, upload-time = "2026-02-02T12:37:05.806Z" },
    { url = "https://files.pythonhosted.org/packages/4f/3b/f77d342a54d4ebcd128e520fc58ec2f5b30a423b0fd26acdfc0c6fef8e26/jiter-0.13.0-cp314-cp314t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:e104da1db1c0991b3eaed391ccd650ae8d947eab1480c733e5a3fb28d4313e40", size = 351438, upload-time = "2026-02-02T12:37:07.189Z" },
    { url = "https://files.pythonhosted.org/packages/76/b3/ba9a69f0e4209bd3331470c723c2f5509e6f0482e416b612431a5061ed71/jiter-0.13.0-cp314-cp314t-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:0e3a5f0cde8ff433b8e88e41aa40131455420fb3649a3c7abdda6145f8cb7202", size = 364774, upload-time = "2026-02-02T12:37:08.579Z" },
    { url = "https://files.pythonhosted.org/packages/b3/16/6cdb31fa342932602458dbb631bfbd47f601e03d2e4950740e0b2100b570/jiter-0.13.0-cp314-cp314t-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:57aab48f40be1db920a582b30b116fe2435d184f77f0e4226f546794cedd9cf0", size = 487238, upload-time = "2026-02-02T12:37:10.066Z" },
    { url = "https://files.pythonhosted.org/packages/ed/b1/956cc7abaca8d95c13aa8d6c9b3f3797241c246cd6e792934cc4c8b250d2/jiter-0.13.0-cp314-cp314t-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:7772115877c53f62beeb8fd853cab692dbc04374ef623b30f997959a4c0e7e95", size = 372892, upload-time = "2026-02-02T12:37:11.656Z" },
    { url = "https://files.pythonhosted.org/packages/26/c4/97ecde8b1e74f67b8598c57c6fccf6df86ea7861ed29da84629cdbba76c4/jiter-0.13.0-cp314-cp314t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:1211427574b17b633cfceba5040de8081e5abf114f7a7602f73d2e16f9fdaa59", size = 360309, upload-time = "2026-02-02T12:37:13.244Z" },
    { url = "https://files.pythonhosted.org/packages/4b/d7/eabe3cf46715854ccc80be2cd78dd4c36aedeb30751dbf85a1d08c14373c/jiter-0.13.0-cp314-cp314t-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:7beae3a3d3b5212d3a55d2961db3c292e02e302feb43fce6a3f7a31b90ea6dfe", size = 389607, upload-time = "2026-02-02T12:37:14.881Z" },
    { url = "https://files.pythonhosted.org/packages/df/2d/03963fc0804e6109b82decfb9974eb92df3797fe7222428cae12f8ccaa0c/jiter-0.13.0-cp314-cp314t-musllinux_1_1_aarch64.whl", hash = "sha256:e5562a0f0e90a6223b704163ea28e831bd3a9faa3512a711f031611e6b06c939", size = 514986, upload-time = "2026-02-02T12:37:16.326Z" },
    { url = "https://files.pythonhosted.org/packages/f6/6c/8c83b45eb3eb1c1e18d841fe30b4b5bc5619d781267ca9bc03e005d8fd0a/jiter-0.13.0-cp314-cp314t-musllinux_1_1_x86_64.whl", hash = "sha256:6c26a424569a59140fb51160a56df13f438a2b0967365e987889186d5fc2f6f9", size = 548756, upload-time = "2026-02-02T12:37:17.736Z" },
    { url = "https://files.pythonhosted.org/packages/47/66/eea81dfff765ed66c68fd2ed8c96245109e13c896c2a5015c7839c92367e/jiter-0.13.0-cp314-cp314t-win32.whl", hash = "sha256:24dc96eca9f84da4131cdf87a95e6ce36765c3b156fc9ae33280873b1c32d5f6", size = 201196, upload-time = "2026-02-02T12:37:19.101Z" },
    { url = "https://files.pythonhosted.org/packages/ff/32/4ac9c7a76402f8f00d00842a7f6b83b284d0cf7c1e9d4227bc95aa6d17fa/jiter-0.13.0-cp314-cp314t-win_amd64.whl", hash = "sha256:0a8d76c7524087272c8ae913f5d9d608bd839154b62c4322ef65723d2e5bb0b8", size = 204215, upload-time = "2026-02-02T12:37:20.495Z" },
    { url = "https://files.pythonhosted.org/packages/f9/8e/7def204fea9f9be8b3c21a6f2dd6c020cf56c7d5ff753e0e23ed7f9ea57e/jiter-0.13.0-cp314-cp314t-win_arm64.whl", hash = "sha256:2c26cf47e2cad140fa23b6d58d435a7c0161f5c514284802f25e87fddfe11024", size = 187152, upload-time = "2026-02-02T12:37:22.124Z" },
    { url = "https://files.pythonhosted.org/packages/80/60/e50fa45dd7e2eae049f0ce964663849e897300433921198aef94b6ffa23a/jiter-0.13.0-graalpy312-graalpy250_312_native-macosx_10_12_x86_64.whl", hash = "sha256:3d744a6061afba08dd7ae375dcde870cffb14429b7477e10f67e9e6d68772a0a", size = 305169, upload-time = "2026-02-02T12:37:50.376Z" },
    { url = "https://files.pythonhosted.org/packages/d2/73/a009f41c5eed71c49bec53036c4b33555afcdee70682a18c6f66e396c039/jiter-0.13.0-graalpy312-graalpy250_312_native-macosx_11_0_arm64.whl", hash = "sha256:ff732bd0a0e778f43d5009840f20b935e79087b4dc65bd36f1cd0f9b04b8ff7f", size = 303808, upload-time = "2026-02-02T12:37:52.092Z" },
    { url = "https://files.pythonhosted.org/packages/c4/10/528b439290763bff3d939268085d03382471b442f212dca4ff5f12802d43/jiter-0.13.0-graalpy312-graalpy250_312_native-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:ab44b178f7981fcaea7e0a5df20e773c663d06ffda0198f1a524e91b2fde7e59", size = 337384, upload-time = "2026-02-02T12:37:53.582Z" },
    { url = "https://files.pythonhosted.org/packages/67/8a/a342b2f0251f3dac4ca17618265d93bf244a2a4d089126e81e4c1056ac50/jiter-0.13.0-graalpy312-graalpy250_312_native-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:7bb00b6d26db67a05fe3e12c76edc75f32077fb51deed13822dc648fa373bc19", size = 343768, upload-time = "2026-02-02T12:37:55.055Z" },
]

[[package]]
name = "markdown-it-py"
version = "4.0.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "mdurl" },
]
sdist = { url = "https://files.pythonhosted.org/packages/5b/f5/4ec618ed16cc4f8fb3b701563655a69816155e79e24a17b651541804721d/markdown_it_py-4.0.0.tar.gz", hash = "sha256:cb0a2b4aa34f932c007117b194e945bd74e0ec24133ceb5bac59009cda1cb9f3", size = 73070, upload-time = "2025-08-11T12:57:52.854Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/94/54/e7d793b573f298e1c9013b8c4dade17d481164aa517d1d7148619c2cedbf/markdown_it_py-4.0.0-py3-none-any.whl", hash = "sha256:87327c59b172c5011896038353a81343b6754500a08cd7a4973bb48c6d578147", size = 87321, upload-time = "2025-08-11T12:57:51.923Z" },
]

[[package]]
name = "mdurl"
version = "0.1.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/d6/54/cfe61301667036ec958cb99bd3efefba235e65cdeb9c84d24a8293ba1d90/mdurl-0.1.2.tar.gz", hash = "sha256:bb413d29f5eea38f31dd4754dd7377d4465116fb207585f97bf925588687c1ba", size = 8729, upload-time = "2022-08-14T12:40:10.846Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/b3/38/89ba8ad64ae25be8de66a6d463314cf1eb366222074cfda9ee839c56a4b4/mdurl-0.1.2-py3-none-any.whl", hash = "sha256:84008a41e51615a49fc9966191ff91509e3c40b939176e643fd50a5c2196b8f8", size = 9979, upload-time = "2022-08-14T12:40:09.779Z" },
]

[[package]]
name = "openai"
version = "2.26.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "anyio" },
    { name = "distro" },
    { name = "httpx" },
    { name = "jiter" },
    { name = "pydantic" },
    { name = "sniffio" },
    { name = "tqdm" },
    { name = "typing-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/d7/91/2a06c4e9597c338cac1e5e5a8dd6f29e1836fc229c4c523529dca387fda8/openai-2.26.0.tar.gz", hash = "sha256:b41f37c140ae0034a6e92b0c509376d907f3a66109935fba2c1b471a7c05a8fb", size = 666702, upload-time = "2026-03-05T23:17:35.874Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/c6/2e/3f73e8ca53718952222cacd0cf7eecc9db439d020f0c1fe7ae717e4e199a/openai-2.26.0-py3-none-any.whl", hash = "sha256:6151bf8f83802f036117f06cc8a57b3a4da60da9926826cc96747888b57f394f", size = 1136409, upload-time = "2026-03-05T23:17:34.072Z" },
]

[[package]]
name = "packaging"
version = "26.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/65/ee/299d360cdc32edc7d2cf530f3accf79c4fca01e96ffc950d8a52213bd8e4/packaging-26.0.tar.gz", hash = "sha256:00243ae351a257117b6a241061796684b084ed1c516a08c48a3f7e147a9d80b4", size = 143416, upload-time = "2026-01-21T20:50:39.064Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/b7/b9/c538f279a4e237a006a2c98387d081e9eb060d203d8ed34467cc0f0b9b53/packaging-26.0-py3-none-any.whl", hash = "sha256:b36f1fef9334a5588b4166f8bcd26a14e521f2b55e6b9de3aaa80d3ff7a37529", size = 74366, upload-time = "2026-01-21T20:50:37.788Z" },
]

[[package]]
name = "pydantic"
version = "2.12.5"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "annotated-types" },
    { name = "pydantic-core" },
    { name = "typing-extensions" },
    { name = "typing-inspection" },
]
sdist = { url = "https://files.pythonhosted.org/packages/69/44/36f1a6e523abc58ae5f928898e4aca2e0ea509b5aa6f6f392a5d882be928/pydantic-2.12.5.tar.gz", hash = "sha256:4d351024c75c0f085a9febbb665ce8c0c6ec5d30e903bdb6394b7ede26aebb49", size = 821591, upload-time = "2025-11-26T15:11:46.471Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/5a/87/b70ad306ebb6f9b585f114d0ac2137d792b48be34d732d60e597c2f8465a/pydantic-2.12.5-py3-none-any.whl", hash = "sha256:e561593fccf61e8a20fc46dfc2dfe075b8be7d0188df33f221ad1f0139180f9d", size = 463580, upload-time = "2025-11-26T15:11:44.605Z" },
]

[[package]]
name = "pydantic-core"
version = "2.41.5"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "typing-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/71/70/23b021c950c2addd24ec408e9ab05d59b035b39d97cdc1130e1bce647bb6/pydantic_core-2.41.5.tar.gz", hash = "sha256:08daa51ea16ad373ffd5e7606252cc32f07bc72b28284b6bc9c6df804816476e", size = 460952, upload-time = "2025-11-04T13:43:49.098Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/5f/5d/5f6c63eebb5afee93bcaae4ce9a898f3373ca23df3ccaef086d0233a35a7/pydantic_core-2.41.5-cp312-cp312-macosx_10_12_x86_64.whl", hash = "sha256:f41a7489d32336dbf2199c8c0a215390a751c5b014c2c1c5366e817202e9cdf7", size = 2110990, upload-time = "2025-11-04T13:39:58.079Z" },
    { url = "https://files.pythonhosted.org/packages/aa/32/9c2e8ccb57c01111e0fd091f236c7b371c1bccea0fa85247ac55b1e2b6b6/pydantic_core-2.41.5-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:070259a8818988b9a84a449a2a7337c7f430a22acc0859c6b110aa7212a6d9c0", size = 1896003, upload-time = "2025-11-04T13:39:59.956Z" },
    { url = "https://files.pythonhosted.org/packages/68/b8/a01b53cb0e59139fbc9e4fda3e9724ede8de279097179be4ff31f1abb65a/pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:e96cea19e34778f8d59fe40775a7a574d95816eb150850a85a7a4c8f4b94ac69", size = 1919200, upload-time = "2025-11-04T13:40:02.241Z" },
    { url = "https://files.pythonhosted.org/packages/38/de/8c36b5198a29bdaade07b5985e80a233a5ac27137846f3bc2d3b40a47360/pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:ed2e99c456e3fadd05c991f8f437ef902e00eedf34320ba2b0842bd1c3ca3a75", size = 2052578, upload-time = "2025-11-04T13:40:04.401Z" },
    { url = "https://files.pythonhosted.org/packages/00/b5/0e8e4b5b081eac6cb3dbb7e60a65907549a1ce035a724368c330112adfdd/pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:65840751b72fbfd82c3c640cff9284545342a4f1eb1586ad0636955b261b0b05", size = 2208504, upload-time = "2025-11-04T13:40:06.072Z" },
    { url = "https://files.pythonhosted.org/packages/77/56/87a61aad59c7c5b9dc8caad5a41a5545cba3810c3e828708b3d7404f6cef/pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:e536c98a7626a98feb2d3eaf75944ef6f3dbee447e1f841eae16f2f0a72d8ddc", size = 2335816, upload-time = "2025-11-04T13:40:07.835Z" },
    { url = "https://files.pythonhosted.org/packages/0d/76/941cc9f73529988688a665a5c0ecff1112b3d95ab48f81db5f7606f522d3/pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:eceb81a8d74f9267ef4081e246ffd6d129da5d87e37a77c9bde550cb04870c1c", size = 2075366, upload-time = "2025-11-04T13:40:09.804Z" },
    { url = "https://files.pythonhosted.org/packages/d3/43/ebef01f69baa07a482844faaa0a591bad1ef129253ffd0cdaa9d8a7f72d3/pydantic_core-2.41.5-cp312-cp312-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:d38548150c39b74aeeb0ce8ee1d8e82696f4a4e16ddc6de7b1d8823f7de4b9b5", size = 2171698, upload-time = "2025-11-04T13:40:12.004Z" },
    { url = "https://files.pythonhosted.org/packages/b1/87/41f3202e4193e3bacfc2c065fab7706ebe81af46a83d3e27605029c1f5a6/pydantic_core-2.41.5-cp312-cp312-musllinux_1_1_aarch64.whl", hash = "sha256:c23e27686783f60290e36827f9c626e63154b82b116d7fe9adba1fda36da706c", size = 2132603, upload-time = "2025-11-04T13:40:13.868Z" },
    { url = "https://files.pythonhosted.org/packages/49/7d/4c00df99cb12070b6bccdef4a195255e6020a550d572768d92cc54dba91a/pydantic_core-2.41.5-cp312-cp312-musllinux_1_1_armv7l.whl", hash = "sha256:482c982f814460eabe1d3bb0adfdc583387bd4691ef00b90575ca0d2b6fe2294", size = 2329591, upload-time = "2025-11-04T13:40:15.672Z" },
    { url = "https://files.pythonhosted.org/packages/cc/6a/ebf4b1d65d458f3cda6a7335d141305dfa19bdc61140a884d165a8a1bbc7/pydantic_core-2.41.5-cp312-cp312-musllinux_1_1_x86_64.whl", hash = "sha256:bfea2a5f0b4d8d43adf9d7b8bf019fb46fdd10a2e5cde477fbcb9d1fa08c68e1", size = 2319068, upload-time = "2025-11-04T13:40:17.532Z" },
    { url = "https://files.pythonhosted.org/packages/49/3b/774f2b5cd4192d5ab75870ce4381fd89cf218af999515baf07e7206753f0/pydantic_core-2.41.5-cp312-cp312-win32.whl", hash = "sha256:b74557b16e390ec12dca509bce9264c3bbd128f8a2c376eaa68003d7f327276d", size = 1985908, upload-time = "2025-11-04T13:40:19.309Z" },
    { url = "https://files.pythonhosted.org/packages/86/45/00173a033c801cacf67c190fef088789394feaf88a98a7035b0e40d53dc9/pydantic_core-2.41.5-cp312-cp312-win_amd64.whl", hash = "sha256:1962293292865bca8e54702b08a4f26da73adc83dd1fcf26fbc875b35d81c815", size = 2020145, upload-time = "2025-11-04T13:40:21.548Z" },
    { url = "https://files.pythonhosted.org/packages/f9/22/91fbc821fa6d261b376a3f73809f907cec5ca6025642c463d3488aad22fb/pydantic_core-2.41.5-cp312-cp312-win_arm64.whl", hash = "sha256:1746d4a3d9a794cacae06a5eaaccb4b8643a131d45fbc9af23e353dc0a5ba5c3", size = 1976179, upload-time = "2025-11-04T13:40:23.393Z" },
    { url = "https://files.pythonhosted.org/packages/87/06/8806241ff1f70d9939f9af039c6c35f2360cf16e93c2ca76f184e76b1564/pydantic_core-2.41.5-cp313-cp313-macosx_10_12_x86_64.whl", hash = "sha256:941103c9be18ac8daf7b7adca8228f8ed6bb7a1849020f643b3a14d15b1924d9", size = 2120403, upload-time = "2025-11-04T13:40:25.248Z" },
    { url = "https://files.pythonhosted.org/packages/94/02/abfa0e0bda67faa65fef1c84971c7e45928e108fe24333c81f3bfe35d5f5/pydantic_core-2.41.5-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:112e305c3314f40c93998e567879e887a3160bb8689ef3d2c04b6cc62c33ac34", size = 1896206, upload-time = "2025-11-04T13:40:27.099Z" },
    { url = "https://files.pythonhosted.org/packages/15/df/a4c740c0943e93e6500f9eb23f4ca7ec9bf71b19e608ae5b579678c8d02f/pydantic_core-2.41.5-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:0cbaad15cb0c90aa221d43c00e77bb33c93e8d36e0bf74760cd00e732d10a6a0", size = 1919307, upload-time = "2025-11-04T13:40:29.806Z" },
    { url = "https://files.pythonhosted.org/packages/9a/e3/6324802931ae1d123528988e0e86587c2072ac2e5394b4bc2bc34b61ff6e/pydantic_core-2.41.5-cp313-cp313-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:03ca43e12fab6023fc79d28ca6b39b05f794ad08ec2feccc59a339b02f2b3d33", size = 2063258, upload-time = "2025-11-04T13:40:33.544Z" },
    { url = "https://files.pythonhosted.org/packages/c9/d4/2230d7151d4957dd79c3044ea26346c148c98fbf0ee6ebd41056f2d62ab5/pydantic_core-2.41.5-cp313-cp313-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:dc799088c08fa04e43144b164feb0c13f9a0bc40503f8df3e9fde58a3c0c101e", size = 2214917, upload-time = "2025-11-04T13:40:35.479Z" },
    { url = "https://files.pythonhosted.org/packages/e6/9f/eaac5df17a3672fef0081b6c1bb0b82b33ee89aa5cec0d7b05f52fd4a1fa/pydantic_core-2.41.5-cp313-cp313-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:97aeba56665b4c3235a0e52b2c2f5ae9cd071b8a8310ad27bddb3f7fb30e9aa2", size = 2332186, upload-time = "2025-11-04T13:40:37.436Z" },
    { url = "https://files.pythonhosted.org/packages/cf/4e/35a80cae583a37cf15604b44240e45c05e04e86f9cfd766623149297e971/pydantic_core-2.41.5-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:406bf18d345822d6c21366031003612b9c77b3e29ffdb0f612367352aab7d586", size = 2073164, upload-time = "2025-11-04T13:40:40.289Z" },
    { url = "https://files.pythonhosted.org/packages/bf/e3/f6e262673c6140dd3305d144d032f7bd5f7497d3871c1428521f19f9efa2/pydantic_core-2.41.5-cp313-cp313-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:b93590ae81f7010dbe380cdeab6f515902ebcbefe0b9327cc4804d74e93ae69d", size = 2179146, upload-time = "2025-11-04T13:40:42.809Z" },
    { url = "https://files.pythonhosted.org/packages/75/c7/20bd7fc05f0c6ea2056a4565c6f36f8968c0924f19b7d97bbfea55780e73/pydantic_core-2.41.5-cp313-cp313-musllinux_1_1_aarch64.whl", hash = "sha256:01a3d0ab748ee531f4ea6c3e48ad9dac84ddba4b0d82291f87248f2f9de8d740", size = 2137788, upload-time = "2025-11-04T13:40:44.752Z" },
    { url = "https://files.pythonhosted.org/packages/3a/8d/34318ef985c45196e004bc46c6eab2eda437e744c124ef0dbe1ff2c9d06b/pydantic_core-2.41.5-cp313-cp313-musllinux_1_1_armv7l.whl", hash = "sha256:6561e94ba9dacc9c61bce40e2d6bdc3bfaa0259d3ff36ace3b1e6901936d2e3e", size = 2340133, upload-time = "2025-11-04T13:40:46.66Z" },
    { url = "https://files.pythonhosted.org/packages/9c/59/013626bf8c78a5a5d9350d12e7697d3d4de951a75565496abd40ccd46bee/pydantic_core-2.41.5-cp313-cp313-musllinux_1_1_x86_64.whl", hash = "sha256:915c3d10f81bec3a74fbd4faebe8391013ba61e5a1a8d48c4455b923bdda7858", size = 2324852, upload-time = "2025-11-04T13:40:48.575Z" },
    { url = "https://files.pythonhosted.org/packages/1a/d9/c248c103856f807ef70c18a4f986693a46a8ffe1602e5d361485da502d20/pydantic_core-2.41.5-cp313-cp313-win32.whl", hash = "sha256:650ae77860b45cfa6e2cdafc42618ceafab3a2d9a3811fcfbd3bbf8ac3c40d36", size = 1994679, upload-time = "2025-11-04T13:40:50.619Z" },
    { url = "https://files.pythonhosted.org/packages/9e/8b/341991b158ddab181cff136acd2552c9f35bd30380422a639c0671e99a91/pydantic_core-2.41.5-cp313-cp313-win_amd64.whl", hash = "sha256:79ec52ec461e99e13791ec6508c722742ad745571f234ea6255bed38c6480f11", size = 2019766, upload-time = "2025-11-04T13:40:52.631Z" },
    { url = "https://files.pythonhosted.org/packages/73/7d/f2f9db34af103bea3e09735bb40b021788a5e834c81eedb541991badf8f5/pydantic_core-2.41.5-cp313-cp313-win_arm64.whl", hash = "sha256:3f84d5c1b4ab906093bdc1ff10484838aca54ef08de4afa9de0f5f14d69639cd", size = 1981005, upload-time = "2025-11-04T13:40:54.734Z" },
    { url = "https://files.pythonhosted.org/packages/ea/28/46b7c5c9635ae96ea0fbb779e271a38129df2550f763937659ee6c5dbc65/pydantic_core-2.41.5-cp314-cp314-macosx_10_12_x86_64.whl", hash = "sha256:3f37a19d7ebcdd20b96485056ba9e8b304e27d9904d233d7b1015db320e51f0a", size = 2119622, upload-time = "2025-11-04T13:40:56.68Z" },
    { url = "https://files.pythonhosted.org/packages/74/1a/145646e5687e8d9a1e8d09acb278c8535ebe9e972e1f162ed338a622f193/pydantic_core-2.41.5-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:1d1d9764366c73f996edd17abb6d9d7649a7eb690006ab6adbda117717099b14", size = 1891725, upload-time = "2025-11-04T13:40:58.807Z" },
    { url = "https://files.pythonhosted.org/packages/23/04/e89c29e267b8060b40dca97bfc64a19b2a3cf99018167ea1677d96368273/pydantic_core-2.41.5-cp314-cp314-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:25e1c2af0fce638d5f1988b686f3b3ea8cd7de5f244ca147c777769e798a9cd1", size = 1915040, upload-time = "2025-11-04T13:41:00.853Z" },
    { url = "https://files.pythonhosted.org/packages/84/a3/15a82ac7bd97992a82257f777b3583d3e84bdb06ba6858f745daa2ec8a85/pydantic_core-2.41.5-cp314-cp314-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:506d766a8727beef16b7adaeb8ee6217c64fc813646b424d0804d67c16eddb66", size = 2063691, upload-time = "2025-11-04T13:41:03.504Z" },
    { url = "https://files.pythonhosted.org/packages/74/9b/0046701313c6ef08c0c1cf0e028c67c770a4e1275ca73131563c5f2a310a/pydantic_core-2.41.5-cp314-cp314-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:4819fa52133c9aa3c387b3328f25c1facc356491e6135b459f1de698ff64d869", size = 2213897, upload-time = "2025-11-04T13:41:05.804Z" },
    { url = "https://files.pythonhosted.org/packages/8a/cd/6bac76ecd1b27e75a95ca3a9a559c643b3afcd2dd62086d4b7a32a18b169/pydantic_core-2.41.5-cp314-cp314-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:2b761d210c9ea91feda40d25b4efe82a1707da2ef62901466a42492c028553a2", size = 2333302, upload-time = "2025-11-04T13:41:07.809Z" },
    { url = "https://files.pythonhosted.org/packages/4c/d2/ef2074dc020dd6e109611a8be4449b98cd25e1b9b8a303c2f0fca2f2bcf7/pydantic_core-2.41.5-cp314-cp314-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:22f0fb8c1c583a3b6f24df2470833b40207e907b90c928cc8d3594b76f874375", size = 2064877, upload-time = "2025-11-04T13:41:09.827Z" },
    { url = "https://files.pythonhosted.org/packages/18/66/e9db17a9a763d72f03de903883c057b2592c09509ccfe468187f2a2eef29/pydantic_core-2.41.5-cp314-cp314-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:2782c870e99878c634505236d81e5443092fba820f0373997ff75f90f68cd553", size = 2180680, upload-time = "2025-11-04T13:41:12.379Z" },
    { url = "https://files.pythonhosted.org/packages/d3/9e/3ce66cebb929f3ced22be85d4c2399b8e85b622db77dad36b73c5387f8f8/pydantic_core-2.41.5-cp314-cp314-musllinux_1_1_aarch64.whl", hash = "sha256:0177272f88ab8312479336e1d777f6b124537d47f2123f89cb37e0accea97f90", size = 2138960, upload-time = "2025-11-04T13:41:14.627Z" },
    { url = "https://files.pythonhosted.org/packages/a6/62/205a998f4327d2079326b01abee48e502ea739d174f0a89295c481a2272e/pydantic_core-2.41.5-cp314-cp314-musllinux_1_1_armv7l.whl", hash = "sha256:63510af5e38f8955b8ee5687740d6ebf7c2a0886d15a6d65c32814613681bc07", size = 2339102, upload-time = "2025-11-04T13:41:16.868Z" },
    { url = "https://files.pythonhosted.org/packages/3c/0d/f05e79471e889d74d3d88f5bd20d0ed189ad94c2423d81ff8d0000aab4ff/pydantic_core-2.41.5-cp314-cp314-musllinux_1_1_x86_64.whl", hash = "sha256:e56ba91f47764cc14f1daacd723e3e82d1a89d783f0f5afe9c364b8bb491ccdb", size = 2326039, upload-time = "2025-11-04T13:41:18.934Z" },
    { url = "https://files.pythonhosted.org/packages/ec/e1/e08a6208bb100da7e0c4b288eed624a703f4d129bde2da475721a80cab32/pydantic_core-2.41.5-cp314-cp314-win32.whl", hash = "sha256:aec5cf2fd867b4ff45b9959f8b20ea3993fc93e63c7363fe6851424c8a7e7c23", size = 1995126, upload-time = "2025-11-04T13:41:21.418Z" },
    { url = "https://files.pythonhosted.org/packages/48/5d/56ba7b24e9557f99c9237e29f5c09913c81eeb2f3217e40e922353668092/pydantic_core-2.41.5-cp314-cp314-win_amd64.whl", hash = "sha256:8e7c86f27c585ef37c35e56a96363ab8de4e549a95512445b85c96d3e2f7c1bf", size = 2015489, upload-time = "2025-11-04T13:41:24.076Z" },
    { url = "https://files.pythonhosted.org/packages/4e/bb/f7a190991ec9e3e0ba22e4993d8755bbc4a32925c0b5b42775c03e8148f9/pydantic_core-2.41.5-cp314-cp314-win_arm64.whl", hash = "sha256:e672ba74fbc2dc8eea59fb6d4aed6845e6905fc2a8afe93175d94a83ba2a01a0", size = 1977288, upload-time = "2025-11-04T13:41:26.33Z" },
    { url = "https://files.pythonhosted.org/packages/92/ed/77542d0c51538e32e15afe7899d79efce4b81eee631d99850edc2f5e9349/pydantic_core-2.41.5-cp314-cp314t-macosx_10_12_x86_64.whl", hash = "sha256:8566def80554c3faa0e65ac30ab0932b9e3a5cd7f8323764303d468e5c37595a", size = 2120255, upload-time = "2025-11-04T13:41:28.569Z" },
    { url = "https://files.pythonhosted.org/packages/bb/3d/6913dde84d5be21e284439676168b28d8bbba5600d838b9dca99de0fad71/pydantic_core-2.41.5-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:b80aa5095cd3109962a298ce14110ae16b8c1aece8b72f9dafe81cf597ad80b3", size = 1863760, upload-time = "2025-11-04T13:41:31.055Z" },
    { url = "https://files.pythonhosted.org/packages/5a/f0/e5e6b99d4191da102f2b0eb9687aaa7f5bea5d9964071a84effc3e40f997/pydantic_core-2.41.5-cp314-cp314t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:3006c3dd9ba34b0c094c544c6006cc79e87d8612999f1a5d43b769b89181f23c", size = 1878092, upload-time = "2025-11-04T13:41:33.21Z" },
    { url = "https://files.pythonhosted.org/packages/71/48/36fb760642d568925953bcc8116455513d6e34c4beaa37544118c36aba6d/pydantic_core-2.41.5-cp314-cp314t-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:72f6c8b11857a856bcfa48c86f5368439f74453563f951e473514579d44aa612", size = 2053385, upload-time = "2025-11-04T13:41:35.508Z" },
    { url = "https://files.pythonhosted.org/packages/20/25/92dc684dd8eb75a234bc1c764b4210cf2646479d54b47bf46061657292a8/pydantic_core-2.41.5-cp314-cp314t-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:5cb1b2f9742240e4bb26b652a5aeb840aa4b417c7748b6f8387927bc6e45e40d", size = 2218832, upload-time = "2025-11-04T13:41:37.732Z" },
    { url = "https://files.pythonhosted.org/packages/e2/09/f53e0b05023d3e30357d82eb35835d0f6340ca344720a4599cd663dca599/pydantic_core-2.41.5-cp314-cp314t-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:bd3d54f38609ff308209bd43acea66061494157703364ae40c951f83ba99a1a9", size = 2327585, upload-time = "2025-11-04T13:41:40Z" },
    { url = "https://files.pythonhosted.org/packages/aa/4e/2ae1aa85d6af35a39b236b1b1641de73f5a6ac4d5a7509f77b814885760c/pydantic_core-2.41.5-cp314-cp314t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:2ff4321e56e879ee8d2a879501c8e469414d948f4aba74a2d4593184eb326660", size = 2041078, upload-time = "2025-11-04T13:41:42.323Z" },
    { url = "https://files.pythonhosted.org/packages/cd/13/2e215f17f0ef326fc72afe94776edb77525142c693767fc347ed6288728d/pydantic_core-2.41.5-cp314-cp314t-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:d0d2568a8c11bf8225044aa94409e21da0cb09dcdafe9ecd10250b2baad531a9", size = 2173914, upload-time = "2025-11-04T13:41:45.221Z" },
    { url = "https://files.pythonhosted.org/packages/02/7a/f999a6dcbcd0e5660bc348a3991c8915ce6599f4f2c6ac22f01d7a10816c/pydantic_core-2.41.5-cp314-cp314t-musllinux_1_1_aarch64.whl", hash = "sha256:a39455728aabd58ceabb03c90e12f71fd30fa69615760a075b9fec596456ccc3", size = 2129560, upload-time = "2025-11-04T13:41:47.474Z" },
    { url = "https://files.pythonhosted.org/packages/3a/b1/6c990ac65e3b4c079a4fb9f5b05f5b013afa0f4ed6780a3dd236d2cbdc64/pydantic_core-2.41.5-cp314-cp314t-musllinux_1_1_armv7l.whl", hash = "sha256:239edca560d05757817c13dc17c50766136d21f7cd0fac50295499ae24f90fdf", size = 2329244, upload-time = "2025-11-04T13:41:49.992Z" },
    { url = "https://files.pythonhosted.org/packages/d9/02/3c562f3a51afd4d88fff8dffb1771b30cfdfd79befd9883ee094f5b6c0d8/pydantic_core-2.41.5-cp314-cp314t-musllinux_1_1_x86_64.whl", hash = "sha256:2a5e06546e19f24c6a96a129142a75cee553cc018ffee48a460059b1185f4470", size = 2331955, upload-time = "2025-11-04T13:41:54.079Z" },
    { url = "https://files.pythonhosted.org/packages/5c/96/5fb7d8c3c17bc8c62fdb031c47d77a1af698f1d7a406b0f79aaa1338f9ad/pydantic_core-2.41.5-cp314-cp314t-win32.whl", hash = "sha256:b4ececa40ac28afa90871c2cc2b9ffd2ff0bf749380fbdf57d165fd23da353aa", size = 1988906, upload-time = "2025-11-04T13:41:56.606Z" },
    { url = "https://files.pythonhosted.org/packages/22/ed/182129d83032702912c2e2d8bbe33c036f342cc735737064668585dac28f/pydantic_core-2.41.5-cp314-cp314t-win_amd64.whl", hash = "sha256:80aa89cad80b32a912a65332f64a4450ed00966111b6615ca6816153d3585a8c", size = 1981607, upload-time = "2025-11-04T13:41:58.889Z" },
    { url = "https://files.pythonhosted.org/packages/9f/ed/068e41660b832bb0b1aa5b58011dea2a3fe0ba7861ff38c4d4904c1c1a99/pydantic_core-2.41.5-cp314-cp314t-win_arm64.whl", hash = "sha256:35b44f37a3199f771c3eaa53051bc8a70cd7b54f333531c59e29fd4db5d15008", size = 1974769, upload-time = "2025-11-04T13:42:01.186Z" },
    { url = "https://files.pythonhosted.org/packages/09/32/59b0c7e63e277fa7911c2fc70ccfb45ce4b98991e7ef37110663437005af/pydantic_core-2.41.5-graalpy312-graalpy250_312_native-macosx_10_12_x86_64.whl", hash = "sha256:7da7087d756b19037bc2c06edc6c170eeef3c3bafcb8f532ff17d64dc427adfd", size = 2110495, upload-time = "2025-11-04T13:42:49.689Z" },
    { url = "https://files.pythonhosted.org/packages/aa/81/05e400037eaf55ad400bcd318c05bb345b57e708887f07ddb2d20e3f0e98/pydantic_core-2.41.5-graalpy312-graalpy250_312_native-macosx_11_0_arm64.whl", hash = "sha256:aabf5777b5c8ca26f7824cb4a120a740c9588ed58df9b2d196ce92fba42ff8dc", size = 1915388, upload-time = "2025-11-04T13:42:52.215Z" },
    { url = "https://files.pythonhosted.org/packages/6e/0d/e3549b2399f71d56476b77dbf3cf8937cec5cd70536bdc0e374a421d0599/pydantic_core-2.41.5-graalpy312-graalpy250_312_native-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:c007fe8a43d43b3969e8469004e9845944f1a80e6acd47c150856bb87f230c56", size = 1942879, upload-time = "2025-11-04T13:42:56.483Z" },
    { url = "https://files.pythonhosted.org/packages/f7/07/34573da085946b6a313d7c42f82f16e8920bfd730665de2d11c0c37a74b5/pydantic_core-2.41.5-graalpy312-graalpy250_312_native-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:76d0819de158cd855d1cbb8fcafdf6f5cf1eb8e470abe056d5d161106e38062b", size = 2139017, upload-time = "2025-11-04T13:42:59.471Z" },
]

[[package]]
name = "pydantic-settings"
version = "2.13.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "pydantic" },
    { name = "python-dotenv" },
    { name = "typing-inspection" },
]
sdist = { url = "https://files.pythonhosted.org/packages/52/6d/fffca34caecc4a3f97bda81b2098da5e8ab7efc9a66e819074a11955d87e/pydantic_settings-2.13.1.tar.gz", hash = "sha256:b4c11847b15237fb0171e1462bf540e294affb9b86db4d9aa5c01730bdbe4025", size = 223826, upload-time = "2026-02-19T13:45:08.055Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/00/4b/ccc026168948fec4f7555b9164c724cf4125eac006e176541483d2c959be/pydantic_settings-2.13.1-py3-none-any.whl", hash = "sha256:d56fd801823dbeae7f0975e1f8c8e25c258eb75d278ea7abb5d9cebb01b56237", size = 58929, upload-time = "2026-02-19T13:45:06.034Z" },
]

[[package]]
name = "pygments"
version = "2.19.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/b0/77/a5b8c569bf593b0140bde72ea885a803b82086995367bf2037de0159d924/pygments-2.19.2.tar.gz", hash = "sha256:636cb2477cec7f8952536970bc533bc43743542f70392ae026374600add5b887", size = 4968631, upload-time = "2025-06-21T13:39:12.283Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/c7/21/705964c7812476f378728bdf590ca4b771ec72385c533964653c68e86bdc/pygments-2.19.2-py3-none-any.whl", hash = "sha256:86540386c03d588bb81d44bc3928634ff26449851e99741617ecb9037ee5ec0b", size = 1225217, upload-time = "2025-06-21T13:39:07.939Z" },
]

[[package]]
name = "python-dotenv"
version = "1.2.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/82/ed/0301aeeac3e5353ef3d94b6ec08bbcabd04a72018415dcb29e588514bba8/python_dotenv-1.2.2.tar.gz", hash = "sha256:2c371a91fbd7ba082c2c1dc1f8bf89ca22564a087c2c287cd9b662adde799cf3", size = 50135, upload-time = "2026-03-01T16:00:26.196Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/0b/d7/1959b9648791274998a9c3526f6d0ec8fd2233e4d4acce81bbae76b44b2a/python_dotenv-1.2.2-py3-none-any.whl", hash = "sha256:1d8214789a24de455a8b8bd8ae6fe3c6b69a5e3d64aa8a8e5d68e694bbcb285a", size = 22101, upload-time = "2026-03-01T16:00:25.09Z" },
]

[[package]]
name = "python-multipart"
version = "0.0.22"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/94/01/979e98d542a70714b0cb2b6728ed0b7c46792b695e3eaec3e20711271ca3/python_multipart-0.0.22.tar.gz", hash = "sha256:7340bef99a7e0032613f56dc36027b959fd3b30a787ed62d310e951f7c3a3a58", size = 37612, upload-time = "2026-01-25T10:15:56.219Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/1b/d0/397f9626e711ff749a95d96b7af99b9c566a9bb5129b8e4c10fc4d100304/python_multipart-0.0.22-py3-none-any.whl", hash = "sha256:2b2cd894c83d21bf49d702499531c7bafd057d730c201782048f7945d82de155", size = 24579, upload-time = "2026-01-25T10:15:54.811Z" },
]

[[package]]
name = "pyyaml"
version = "6.0.3"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/05/8e/961c0007c59b8dd7729d542c61a4d537767a59645b82a0b521206e1e25c2/pyyaml-6.0.3.tar.gz", hash = "sha256:d76623373421df22fb4cf8817020cbb7ef15c725b9d5e45f17e189bfc384190f", size = 130960, upload-time = "2025-09-25T21:33:16.546Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/d1/33/422b98d2195232ca1826284a76852ad5a86fe23e31b009c9886b2d0fb8b2/pyyaml-6.0.3-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:7f047e29dcae44602496db43be01ad42fc6f1cc0d8cd6c83d342306c32270196", size = 182063, upload-time = "2025-09-25T21:32:11.445Z" },
    { url = "https://files.pythonhosted.org/packages/89/a0/6cf41a19a1f2f3feab0e9c0b74134aa2ce6849093d5517a0c550fe37a648/pyyaml-6.0.3-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:fc09d0aa354569bc501d4e787133afc08552722d3ab34836a80547331bb5d4a0", size = 173973, upload-time = "2025-09-25T21:32:12.492Z" },
    { url = "https://files.pythonhosted.org/packages/ed/23/7a778b6bd0b9a8039df8b1b1d80e2e2ad78aa04171592c8a5c43a56a6af4/pyyaml-6.0.3-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:9149cad251584d5fb4981be1ecde53a1ca46c891a79788c0df828d2f166bda28", size = 775116, upload-time = "2025-09-25T21:32:13.652Z" },
    { url = "https://files.pythonhosted.org/packages/65/30/d7353c338e12baef4ecc1b09e877c1970bd3382789c159b4f89d6a70dc09/pyyaml-6.0.3-cp312-cp312-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:5fdec68f91a0c6739b380c83b951e2c72ac0197ace422360e6d5a959d8d97b2c", size = 844011, upload-time = "2025-09-25T21:32:15.21Z" },
    { url = "https://files.pythonhosted.org/packages/8b/9d/b3589d3877982d4f2329302ef98a8026e7f4443c765c46cfecc8858c6b4b/pyyaml-6.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:ba1cc08a7ccde2d2ec775841541641e4548226580ab850948cbfda66a1befcdc", size = 807870, upload-time = "2025-09-25T21:32:16.431Z" },
    { url = "https://files.pythonhosted.org/packages/05/c0/b3be26a015601b822b97d9149ff8cb5ead58c66f981e04fedf4e762f4bd4/pyyaml-6.0.3-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:8dc52c23056b9ddd46818a57b78404882310fb473d63f17b07d5c40421e47f8e", size = 761089, upload-time = "2025-09-25T21:32:17.56Z" },
    { url = "https://files.pythonhosted.org/packages/be/8e/98435a21d1d4b46590d5459a22d88128103f8da4c2d4cb8f14f2a96504e1/pyyaml-6.0.3-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:41715c910c881bc081f1e8872880d3c650acf13dfa8214bad49ed4cede7c34ea", size = 790181, upload-time = "2025-09-25T21:32:18.834Z" },
    { url = "https://files.pythonhosted.org/packages/74/93/7baea19427dcfbe1e5a372d81473250b379f04b1bd3c4c5ff825e2327202/pyyaml-6.0.3-cp312-cp312-win32.whl", hash = "sha256:96b533f0e99f6579b3d4d4995707cf36df9100d67e0c8303a0c55b27b5f99bc5", size = 137658, upload-time = "2025-09-25T21:32:20.209Z" },
    { url = "https://files.pythonhosted.org/packages/86/bf/899e81e4cce32febab4fb42bb97dcdf66bc135272882d1987881a4b519e9/pyyaml-6.0.3-cp312-cp312-win_amd64.whl", hash = "sha256:5fcd34e47f6e0b794d17de1b4ff496c00986e1c83f7ab2fb8fcfe9616ff7477b", size = 154003, upload-time = "2025-09-25T21:32:21.167Z" },
    { url = "https://files.pythonhosted.org/packages/1a/08/67bd04656199bbb51dbed1439b7f27601dfb576fb864099c7ef0c3e55531/pyyaml-6.0.3-cp312-cp312-win_arm64.whl", hash = "sha256:64386e5e707d03a7e172c0701abfb7e10f0fb753ee1d773128192742712a98fd", size = 140344, upload-time = "2025-09-25T21:32:22.617Z" },
    { url = "https://files.pythonhosted.org/packages/d1/11/0fd08f8192109f7169db964b5707a2f1e8b745d4e239b784a5a1dd80d1db/pyyaml-6.0.3-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:8da9669d359f02c0b91ccc01cac4a67f16afec0dac22c2ad09f46bee0697eba8", size = 181669, upload-time = "2025-09-25T21:32:23.673Z" },
    { url = "https://files.pythonhosted.org/packages/b1/16/95309993f1d3748cd644e02e38b75d50cbc0d9561d21f390a76242ce073f/pyyaml-6.0.3-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:2283a07e2c21a2aa78d9c4442724ec1eb15f5e42a723b99cb3d822d48f5f7ad1", size = 173252, upload-time = "2025-09-25T21:32:25.149Z" },
    { url = "https://files.pythonhosted.org/packages/50/31/b20f376d3f810b9b2371e72ef5adb33879b25edb7a6d072cb7ca0c486398/pyyaml-6.0.3-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:ee2922902c45ae8ccada2c5b501ab86c36525b883eff4255313a253a3160861c", size = 767081, upload-time = "2025-09-25T21:32:26.575Z" },
    { url = "https://files.pythonhosted.org/packages/49/1e/a55ca81e949270d5d4432fbbd19dfea5321eda7c41a849d443dc92fd1ff7/pyyaml-6.0.3-cp313-cp313-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:a33284e20b78bd4a18c8c2282d549d10bc8408a2a7ff57653c0cf0b9be0afce5", size = 841159, upload-time = "2025-09-25T21:32:27.727Z" },
    { url = "https://files.pythonhosted.org/packages/74/27/e5b8f34d02d9995b80abcef563ea1f8b56d20134d8f4e5e81733b1feceb2/pyyaml-6.0.3-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:0f29edc409a6392443abf94b9cf89ce99889a1dd5376d94316ae5145dfedd5d6", size = 801626, upload-time = "2025-09-25T21:32:28.878Z" },
    { url = "https://files.pythonhosted.org/packages/f9/11/ba845c23988798f40e52ba45f34849aa8a1f2d4af4b798588010792ebad6/pyyaml-6.0.3-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:f7057c9a337546edc7973c0d3ba84ddcdf0daa14533c2065749c9075001090e6", size = 753613, upload-time = "2025-09-25T21:32:30.178Z" },
    { url = "https://files.pythonhosted.org/packages/3d/e0/7966e1a7bfc0a45bf0a7fb6b98ea03fc9b8d84fa7f2229e9659680b69ee3/pyyaml-6.0.3-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:eda16858a3cab07b80edaf74336ece1f986ba330fdb8ee0d6c0d68fe82bc96be", size = 794115, upload-time = "2025-09-25T21:32:31.353Z" },
    { url = "https://files.pythonhosted.org/packages/de/94/980b50a6531b3019e45ddeada0626d45fa85cbe22300844a7983285bed3b/pyyaml-6.0.3-cp313-cp313-win32.whl", hash = "sha256:d0eae10f8159e8fdad514efdc92d74fd8d682c933a6dd088030f3834bc8e6b26", size = 137427, upload-time = "2025-09-25T21:32:32.58Z" },
    { url = "https://files.pythonhosted.org/packages/97/c9/39d5b874e8b28845e4ec2202b5da735d0199dbe5b8fb85f91398814a9a46/pyyaml-6.0.3-cp313-cp313-win_amd64.whl", hash = "sha256:79005a0d97d5ddabfeeea4cf676af11e647e41d81c9a7722a193022accdb6b7c", size = 154090, upload-time = "2025-09-25T21:32:33.659Z" },
    { url = "https://files.pythonhosted.org/packages/73/e8/2bdf3ca2090f68bb3d75b44da7bbc71843b19c9f2b9cb9b0f4ab7a5a4329/pyyaml-6.0.3-cp313-cp313-win_arm64.whl", hash = "sha256:5498cd1645aa724a7c71c8f378eb29ebe23da2fc0d7a08071d89469bf1d2defb", size = 140246, upload-time = "2025-09-25T21:32:34.663Z" },
    { url = "https://files.pythonhosted.org/packages/9d/8c/f4bd7f6465179953d3ac9bc44ac1a8a3e6122cf8ada906b4f96c60172d43/pyyaml-6.0.3-cp314-cp314-macosx_10_13_x86_64.whl", hash = "sha256:8d1fab6bb153a416f9aeb4b8763bc0f22a5586065f86f7664fc23339fc1c1fac", size = 181814, upload-time = "2025-09-25T21:32:35.712Z" },
    { url = "https://files.pythonhosted.org/packages/bd/9c/4d95bb87eb2063d20db7b60faa3840c1b18025517ae857371c4dd55a6b3a/pyyaml-6.0.3-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:34d5fcd24b8445fadc33f9cf348c1047101756fd760b4dacb5c3e99755703310", size = 173809, upload-time = "2025-09-25T21:32:36.789Z" },
    { url = "https://files.pythonhosted.org/packages/92/b5/47e807c2623074914e29dabd16cbbdd4bf5e9b2db9f8090fa64411fc5382/pyyaml-6.0.3-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:501a031947e3a9025ed4405a168e6ef5ae3126c59f90ce0cd6f2bfc477be31b7", size = 766454, upload-time = "2025-09-25T21:32:37.966Z" },
    { url = "https://files.pythonhosted.org/packages/02/9e/e5e9b168be58564121efb3de6859c452fccde0ab093d8438905899a3a483/pyyaml-6.0.3-cp314-cp314-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:b3bc83488de33889877a0f2543ade9f70c67d66d9ebb4ac959502e12de895788", size = 836355, upload-time = "2025-09-25T21:32:39.178Z" },
    { url = "https://files.pythonhosted.org/packages/88/f9/16491d7ed2a919954993e48aa941b200f38040928474c9e85ea9e64222c3/pyyaml-6.0.3-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:c458b6d084f9b935061bc36216e8a69a7e293a2f1e68bf956dcd9e6cbcd143f5", size = 794175, upload-time = "2025-09-25T21:32:40.865Z" },
    { url = "https://files.pythonhosted.org/packages/dd/3f/5989debef34dc6397317802b527dbbafb2b4760878a53d4166579111411e/pyyaml-6.0.3-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:7c6610def4f163542a622a73fb39f534f8c101d690126992300bf3207eab9764", size = 755228, upload-time = "2025-09-25T21:32:42.084Z" },
    { url = "https://files.pythonhosted.org/packages/d7/ce/af88a49043cd2e265be63d083fc75b27b6ed062f5f9fd6cdc223ad62f03e/pyyaml-6.0.3-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:5190d403f121660ce8d1d2c1bb2ef1bd05b5f68533fc5c2ea899bd15f4399b35", size = 789194, upload-time = "2025-09-25T21:32:43.362Z" },
    { url = "https://files.pythonhosted.org/packages/23/20/bb6982b26a40bb43951265ba29d4c246ef0ff59c9fdcdf0ed04e0687de4d/pyyaml-6.0.3-cp314-cp314-win_amd64.whl", hash = "sha256:4a2e8cebe2ff6ab7d1050ecd59c25d4c8bd7e6f400f5f82b96557ac0abafd0ac", size = 156429, upload-time = "2025-09-25T21:32:57.844Z" },
    { url = "https://files.pythonhosted.org/packages/f4/f4/a4541072bb9422c8a883ab55255f918fa378ecf083f5b85e87fc2b4eda1b/pyyaml-6.0.3-cp314-cp314-win_arm64.whl", hash = "sha256:93dda82c9c22deb0a405ea4dc5f2d0cda384168e466364dec6255b293923b2f3", size = 143912, upload-time = "2025-09-25T21:32:59.247Z" },
    { url = "https://files.pythonhosted.org/packages/7c/f9/07dd09ae774e4616edf6cda684ee78f97777bdd15847253637a6f052a62f/pyyaml-6.0.3-cp314-cp314t-macosx_10_13_x86_64.whl", hash = "sha256:02893d100e99e03eda1c8fd5c441d8c60103fd175728e23e431db1b589cf5ab3", size = 189108, upload-time = "2025-09-25T21:32:44.377Z" },
    { url = "https://files.pythonhosted.org/packages/4e/78/8d08c9fb7ce09ad8c38ad533c1191cf27f7ae1effe5bb9400a46d9437fcf/pyyaml-6.0.3-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:c1ff362665ae507275af2853520967820d9124984e0f7466736aea23d8611fba", size = 183641, upload-time = "2025-09-25T21:32:45.407Z" },
    { url = "https://files.pythonhosted.org/packages/7b/5b/3babb19104a46945cf816d047db2788bcaf8c94527a805610b0289a01c6b/pyyaml-6.0.3-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:6adc77889b628398debc7b65c073bcb99c4a0237b248cacaf3fe8a557563ef6c", size = 831901, upload-time = "2025-09-25T21:32:48.83Z" },
    { url = "https://files.pythonhosted.org/packages/8b/cc/dff0684d8dc44da4d22a13f35f073d558c268780ce3c6ba1b87055bb0b87/pyyaml-6.0.3-cp314-cp314t-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:a80cb027f6b349846a3bf6d73b5e95e782175e52f22108cfa17876aaeff93702", size = 861132, upload-time = "2025-09-25T21:32:50.149Z" },
    { url = "https://files.pythonhosted.org/packages/b1/5e/f77dc6b9036943e285ba76b49e118d9ea929885becb0a29ba8a7c75e29fe/pyyaml-6.0.3-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:00c4bdeba853cc34e7dd471f16b4114f4162dc03e6b7afcc2128711f0eca823c", size = 839261, upload-time = "2025-09-25T21:32:51.808Z" },
    { url = "https://files.pythonhosted.org/packages/ce/88/a9db1376aa2a228197c58b37302f284b5617f56a5d959fd1763fb1675ce6/pyyaml-6.0.3-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:66e1674c3ef6f541c35191caae2d429b967b99e02040f5ba928632d9a7f0f065", size = 805272, upload-time = "2025-09-25T21:32:52.941Z" },
    { url = "https://files.pythonhosted.org/packages/da/92/1446574745d74df0c92e6aa4a7b0b3130706a4142b2d1a5869f2eaa423c6/pyyaml-6.0.3-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:16249ee61e95f858e83976573de0f5b2893b3677ba71c9dd36b9cf8be9ac6d65", size = 829923, upload-time = "2025-09-25T21:32:54.537Z" },
    { url = "https://files.pythonhosted.org/packages/f0/7a/1c7270340330e575b92f397352af856a8c06f230aa3e76f86b39d01b416a/pyyaml-6.0.3-cp314-cp314t-win_amd64.whl", hash = "sha256:4ad1906908f2f5ae4e5a8ddfce73c320c2a1429ec52eafd27138b7f1cbe341c9", size = 174062, upload-time = "2025-09-25T21:32:55.767Z" },
    { url = "https://files.pythonhosted.org/packages/f1/12/de94a39c2ef588c7e6455cfbe7343d3b2dc9d6b6b2f40c4c6565744c873d/pyyaml-6.0.3-cp314-cp314t-win_arm64.whl", hash = "sha256:ebc55a14a21cb14062aa4162f906cd962b28e2e9ea38f9b4391244cd8de4ae0b", size = 149341, upload-time = "2025-09-25T21:32:56.828Z" },
]

[[package]]
name = "rich"
version = "14.3.3"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "markdown-it-py" },
    { name = "pygments" },
]
sdist = { url = "https://files.pythonhosted.org/packages/b3/c6/f3b320c27991c46f43ee9d856302c70dc2d0fb2dba4842ff739d5f46b393/rich-14.3.3.tar.gz", hash = "sha256:b8daa0b9e4eef54dd8cf7c86c03713f53241884e814f4e2f5fb342fe520f639b", size = 230582, upload-time = "2026-02-19T17:23:12.474Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/14/25/b208c5683343959b670dc001595f2f3737e051da617f66c31f7c4fa93abc/rich-14.3.3-py3-none-any.whl", hash = "sha256:793431c1f8619afa7d3b52b2cdec859562b950ea0d4b6b505397612db8d5362d", size = 310458, upload-time = "2026-02-19T17:23:13.732Z" },
]

[[package]]
name = "shellingham"
version = "1.5.4"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/58/15/8b3609fd3830ef7b27b655beb4b4e9c62313a4e8da8c676e142cc210d58e/shellingham-1.5.4.tar.gz", hash = "sha256:8dbca0739d487e5bd35ab3ca4b36e11c4078f3a234bfce294b0a0291363404de", size = 10310, upload-time = "2023-10-24T04:13:40.426Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/e0/f9/0595336914c5619e5f28a1fb793285925a8cd4b432c9da0a987836c7f822/shellingham-1.5.4-py2.py3-none-any.whl", hash = "sha256:7ecfff8f2fd72616f7481040475a65b2bf8af90a56c89140852d1120324e8686", size = 9755, upload-time = "2023-10-24T04:13:38.866Z" },
]

[[package]]
name = "smmap"
version = "5.0.3"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/1f/ea/49c993d6dfdd7338c9b1000a0f36817ed7ec84577ae2e52f890d1a4ff909/smmap-5.0.3.tar.gz", hash = "sha256:4d9debb8b99007ae47165abc08670bd74cb74b5227dda7f643eccc4e9eb5642c", size = 22506, upload-time = "2026-03-09T03:43:26.1Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/c1/d4/59e74daffcb57a07668852eeeb6035af9f32cbfd7a1d2511f17d2fe6a738/smmap-5.0.3-py3-none-any.whl", hash = "sha256:c106e05d5a61449cf6ba9a1e650227ecfb141590d2a98412103ff35d89fc7b2f", size = 24390, upload-time = "2026-03-09T03:43:24.361Z" },
]

[[package]]
name = "sniffio"
version = "1.3.1"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/a2/87/a6771e1546d97e7e041b6ae58d80074f81b7d5121207425c964ddf5cfdbd/sniffio-1.3.1.tar.gz", hash = "sha256:f4324edc670a0f49750a81b895f35c3adb843cca46f0530f79fc1babb23789dc", size = 20372, upload-time = "2024-02-25T23:20:04.057Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/e9/44/75a9c9421471a6c4805dbf2356f7c181a29c1879239abab1ea2cc8f38b40/sniffio-1.3.1-py3-none-any.whl", hash = "sha256:2f6da418d1f1e0fddd844478f41680e794e6051915791a034ff65e5f100525a2", size = 10235, upload-time = "2024-02-25T23:20:01.196Z" },
]

[[package]]
name = "tqdm"
version = "4.67.3"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "colorama", marker = "sys_platform == 'win32'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/09/a9/6ba95a270c6f1fbcd8dac228323f2777d886cb206987444e4bce66338dd4/tqdm-4.67.3.tar.gz", hash = "sha256:7d825f03f89244ef73f1d4ce193cb1774a8179fd96f31d7e1dcde62092b960bb", size = 169598, upload-time = "2026-02-03T17:35:53.048Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/16/e1/3079a9ff9b8e11b846c6ac5c8b5bfb7ff225eee721825310c91b3b50304f/tqdm-4.67.3-py3-none-any.whl", hash = "sha256:ee1e4c0e59148062281c49d80b25b67771a127c85fc9676d3be5f243206826bf", size = 78374, upload-time = "2026-02-03T17:35:50.982Z" },
]

[[package]]
name = "typer"
version = "0.24.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "annotated-doc" },
    { name = "click" },
    { name = "rich" },
    { name = "shellingham" },
]
sdist = { url = "https://files.pythonhosted.org/packages/f5/24/cb09efec5cc954f7f9b930bf8279447d24618bb6758d4f6adf2574c41780/typer-0.24.1.tar.gz", hash = "sha256:e39b4732d65fbdcde189ae76cf7cd48aeae72919dea1fdfc16593be016256b45", size = 118613, upload-time = "2026-02-21T16:54:40.609Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/4a/91/48db081e7a63bb37284f9fbcefda7c44c277b18b0e13fbc36ea2335b71e6/typer-0.24.1-py3-none-any.whl", hash = "sha256:112c1f0ce578bfb4cab9ffdabc68f031416ebcc216536611ba21f04e9aa84c9e", size = 56085, upload-time = "2026-02-21T16:54:41.616Z" },
]

[[package]]
name = "typing-extensions"
version = "4.15.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/72/94/1a15dd82efb362ac84269196e94cf00f187f7ed21c242792a923cdb1c61f/typing_extensions-4.15.0.tar.gz", hash = "sha256:0cea48d173cc12fa28ecabc3b837ea3cf6f38c6d1136f85cbaaf598984861466", size = 109391, upload-time = "2025-08-25T13:49:26.313Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/18/67/36e9267722cc04a6b9f15c7f3441c2363321a3ea07da7ae0c0707beb2a9c/typing_extensions-4.15.0-py3-none-any.whl", hash = "sha256:f0fa19c6845758ab08074a0cfa8b7aecb71c999ca73d62883bc25cc018c4e548", size = 44614, upload-time = "2025-08-25T13:49:24.86Z" },
]

[[package]]
name = "typing-inspection"
version = "0.4.2"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "typing-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/55/e3/70399cb7dd41c10ac53367ae42139cf4b1ca5f36bb3dc6c9d33acdb43655/typing_inspection-0.4.2.tar.gz", hash = "sha256:ba561c48a67c5958007083d386c3295464928b01faa735ab8547c5692e87f464", size = 75949, upload-time = "2025-10-01T02:14:41.687Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/dc/9b/47798a6c91d8bdb567fe2698fe81e0c6b7cb7ef4d13da4114b41d239f65d/typing_inspection-0.4.2-py3-none-any.whl", hash = "sha256:4ed1cacbdc298c220f1bd249ed5287caa16f34d44ef4e9c3d0cbad5b521545e7", size = 14611, upload-time = "2025-10-01T02:14:40.154Z" },
]

[[package]]
name = "urllib3"
version = "2.6.3"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/c7/24/5f1b3bdffd70275f6661c76461e25f024d5a38a46f04aaca912426a2b1d3/urllib3-2.6.3.tar.gz", hash = "sha256:1b62b6884944a57dbe321509ab94fd4d3b307075e0c2eae991ac71ee15ad38ed", size = 435556, upload-time = "2026-01-07T16:24:43.925Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/39/08/aaaad47bc4e9dc8c725e68f9d04865dbcb2052843ff09c97b08904852d84/urllib3-2.6.3-py3-none-any.whl", hash = "sha256:bf272323e553dfb2e87d9bfd225ca7b0f467b919d7bbd355436d3fd37cb0acd4", size = 131584, upload-time = "2026-01-07T16:24:42.685Z" },
]
```

## File: `python/claude-agent-sdk/.env.example`
```
# Anthropic API Configuration
# For direct Anthropic usage:
#   ANTHROPIC_API_KEY=your-anthropic-key
#   ANTHROPIC_BASE_URL=https://api.anthropic.com
# For OpenRouter usage:
ANTHROPIC_API_KEY=
ANTHROPIC_AUTH_TOKEN=your-openrouter-key
ANTHROPIC_BASE_URL=https://openrouter.ai/api
# Acontext API Configuration
ACONTEXT_API_KEY=sk-ac-your-root-api-bearer-token
ACONTEXT_BASE_URL=http://localhost:8029/api/v1
```

## File: `python/claude-agent-sdk/.gitignore`
```
# Environments
.venv/
venv/
.env

# Python cache/artifacts
__pycache__/
*.py[cod]
*.pyo
*.pyd
*.egg-info/
dist/
build/

# Tooling
.coverage
.pytest_cache/
.mypy_cache/
.ruff_cache/

# IDE/editor
.idea/
.vscode/
.DS_Store
Thumbs.db
```

## File: `python/claude-agent-sdk/.python-version`
```
3.13
```

## File: `python/claude-agent-sdk/README.md`
```markdown
[![Made with Acontext](https://assets.memodb.io/Acontext/badge-made-with-acontext-dark.svg)](https://acontext.io)

# Claude Agent SDK + Acontext (`ClaudeAgentStorage`) Example

This example shows how to use the [`ClaudeAgentStorage`](https://docs.acontext.io/integrations/claude-agent) integration to automatically persist Claude Agent SDK messages to Acontext.

## Overview

The script demonstrates:
- Connecting to the Claude Agent SDK via `ClaudeSDKClient`
- Using `ClaudeAgentStorage` from the Acontext SDK to stream messages directly into Acontext
- Automatic session-id discovery from the Claude Agent SDK stream
- The `replay-user-messages` flag to capture both user and assistant messages

Unlike the `claude-agent-basic` example that manually serializes messages, this approach uses the built-in `ClaudeAgentStorage` helper which handles message formatting, session management, and error handling automatically.

## Prerequisites

- Python 3.13 or newer
- [uv](https://github.com/astral-sh/uv) for dependency management
- `ANTHROPIC_API_KEY` for the Claude Agent SDK
- `ACONTEXT_API_KEY` for the Acontext SDK

## Installation

Install dependencies with uv:

```bash
uv sync
```

## Environment Variables

Create a `.env` file in this directory (see `.env.example`):

```bash
ANTHROPIC_API_KEY=your-anthropic-key
ACONTEXT_API_KEY=sk-ac-your-acontext-key
ACONTEXT_BASE_URL=http://localhost:8029/api/v1  # optional, defaults to this value
```

## Running the Example

```bash
# Option 1: traditional venv
source .venv/bin/activate
python main.py

# Option 2: no activation needed
uv run python main.py
```

## How it works

1. Creates an `AcontextAsyncClient` and wraps it with `ClaudeAgentStorage`
2. Sends a query to Claude via `ClaudeSDKClient`
3. Iterates over `receive_response()` and passes each message to `storage.save_message()`
4. `ClaudeAgentStorage` automatically discovers the session id, formats messages in Anthropic format, and stores them in Acontext

> **Tip:** The `replay-user-messages` flag ensures `UserMessage` is included in the stream so both sides of the conversation are persisted. Without it, only `AssistantMessage` appears and user messages won't be stored.

## Learn More

- [ClaudeAgentStorage docs](https://docs.acontext.io/integrations/claude-agent)
- [Acontext Python SDK](https://docs.acontext.io/chore/async_python)
```

## File: `python/claude-agent-sdk/main.py`
```python
import asyncio
import os
import shutil

from dotenv import load_dotenv

load_dotenv()

from acontext import AcontextAsyncClient, ClaudeAgentStorage
from claude_agent_sdk import ClaudeAgentOptions, ClaudeSDKClient


async def main():
    acontext_client = AcontextAsyncClient(api_key=os.environ["ACONTEXT_API_KEY"])
    storage = ClaudeAgentStorage(client=acontext_client)

    options = ClaudeAgentOptions(
        extra_args={"replay-user-messages": None},
    )
    async with ClaudeSDKClient(options=options) as claude_client:
        await claude_client.query("What is the capital of France?")
        async for message in claude_client.receive_response():
            await storage.save_message(message)

    # Get the session ID from storage
    session_id = storage.session_id
    print(f"Session ID: {session_id}")

    # Create a learning space and trigger learning
    space = await acontext_client.learning_spaces.create()
    await acontext_client.learning_spaces.learn(space.id, session_id=session_id)
    print(f"Created learning space: {space.id}")

    # Wait for learning to complete
    print("Waiting for learning to complete...")
    result = await acontext_client.learning_spaces.wait_for_learning(space.id, session_id=session_id)
    print(f"Learning status: {result.status}")

    # List learned skills
    skills = await acontext_client.learning_spaces.list_skills(space.id)
    print(f"\n=== Learned Skills ({len(skills)}) ===")
    for skill in skills:
        print(f"  - {skill.name}: {skill.description}")
        print(f"    files: {[f.path for f in skill.file_index]}")

    # Download all skill files
    download_dir = "./skills_output"
    if os.path.exists(download_dir):
        shutil.rmtree(download_dir)

    print(f"\nDownloading skills to {download_dir}/")
    for skill in skills:
        resp = await acontext_client.skills.download(skill_id=skill.id, path=f"{download_dir}/{skill.name}")
        print(f"  {resp.name} -> {resp.dir_path}")
        for f in resp.files:
            print(f"    {f}")

    await acontext_client.close()


asyncio.run(main())
```

## File: `python/claude-agent-sdk/pyproject.toml`
```
[project]
name = "claude-agent-sdk-example"
version = "0.1.0"
description = "Example: Claude Agent SDK + Acontext ClaudeAgentStorage integration"
readme = "README.md"
requires-python = ">=3.13"
dependencies = [
    "acontext>=0.1.18",
    "claude-agent-sdk",
    "python-dotenv",
]
```

## File: `python/claude-agent-sdk/uv.lock`
```
version = 1
revision = 3
requires-python = ">=3.13"

[[package]]
name = "acontext"
version = "0.1.18"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "anthropic" },
    { name = "httpx" },
    { name = "openai" },
    { name = "pydantic" },
    { name = "urllib3" },
]
sdist = { url = "https://files.pythonhosted.org/packages/13/4a/65d6f2f58e03bbbd8a269337a4d99536d8d3f7e9406e70b824a730875dac/acontext-0.1.18.tar.gz", hash = "sha256:7b1e763753fc23f007b4777949095a2ccc6d1b2deac714fad01095619a181824", size = 46865, upload-time = "2026-03-10T05:08:42.095Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/8d/76/bf60d77ab00da4170e9f7dfe42458b87c36b03f24ed2baa8c904d7ed9b97/acontext-0.1.18-py3-none-any.whl", hash = "sha256:a8810fb00f2b75c3509b15df07ab9dfef35dcc785ac07fcd6104ce92446b2b6b", size = 68510, upload-time = "2026-03-10T05:08:41.033Z" },
]

[[package]]
name = "annotated-types"
version = "0.7.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/ee/67/531ea369ba64dcff5ec9c3402f9f51bf748cec26dde048a2f973a4eea7f5/annotated_types-0.7.0.tar.gz", hash = "sha256:aff07c09a53a08bc8cfccb9c85b05f1aa9a2a6f23728d790723543408344ce89", size = 16081, upload-time = "2024-05-20T21:33:25.928Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/78/b6/6307fbef88d9b5ee7421e68d78a9f162e0da4900bc5f5793f6d3d0e34fb8/annotated_types-0.7.0-py3-none-any.whl", hash = "sha256:1f02e8b43a8fbbc3f3e0d4f0f4bfc8131bcb4eebe8849b8e5c773f3a1c582a53", size = 13643, upload-time = "2024-05-20T21:33:24.1Z" },
]

[[package]]
name = "anthropic"
version = "0.84.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "anyio" },
    { name = "distro" },
    { name = "docstring-parser" },
    { name = "httpx" },
    { name = "jiter" },
    { name = "pydantic" },
    { name = "sniffio" },
    { name = "typing-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/04/ea/0869d6df9ef83dcf393aeefc12dd81677d091c6ffc86f783e51cf44062f2/anthropic-0.84.0.tar.gz", hash = "sha256:72f5f90e5aebe62dca316cb013629cfa24996b0f5a4593b8c3d712bc03c43c37", size = 539457, upload-time = "2026-02-25T05:22:38.54Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/64/ca/218fa25002a332c0aa149ba18ffc0543175998b1f65de63f6d106689a345/anthropic-0.84.0-py3-none-any.whl", hash = "sha256:861c4c50f91ca45f942e091d83b60530ad6d4f98733bfe648065364da05d29e7", size = 455156, upload-time = "2026-02-25T05:22:40.468Z" },
]

[[package]]
name = "anyio"
version = "4.12.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "idna" },
]
sdist = { url = "https://files.pythonhosted.org/packages/96/f0/5eb65b2bb0d09ac6776f2eb54adee6abe8228ea05b20a5ad0e4945de8aac/anyio-4.12.1.tar.gz", hash = "sha256:41cfcc3a4c85d3f05c932da7c26d0201ac36f72abd4435ba90d0464a3ffed703", size = 228685, upload-time = "2026-01-06T11:45:21.246Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/38/0e/27be9fdef66e72d64c0cdc3cc2823101b80585f8119b5c112c2e8f5f7dab/anyio-4.12.1-py3-none-any.whl", hash = "sha256:d405828884fc140aa80a3c667b8beed277f1dfedec42ba031bd6ac3db606ab6c", size = 113592, upload-time = "2026-01-06T11:45:19.497Z" },
]

[[package]]
name = "attrs"
version = "25.4.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/6b/5c/685e6633917e101e5dcb62b9dd76946cbb57c26e133bae9e0cd36033c0a9/attrs-25.4.0.tar.gz", hash = "sha256:16d5969b87f0859ef33a48b35d55ac1be6e42ae49d5e853b597db70c35c57e11", size = 934251, upload-time = "2025-10-06T13:54:44.725Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/3a/2a/7cc015f5b9f5db42b7d48157e23356022889fc354a2813c15934b7cb5c0e/attrs-25.4.0-py3-none-any.whl", hash = "sha256:adcf7e2a1fb3b36ac48d97835bb6d8ade15b8dcce26aba8bf1d14847b57a3373", size = 67615, upload-time = "2025-10-06T13:54:43.17Z" },
]

[[package]]
name = "certifi"
version = "2026.2.25"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/af/2d/7bf41579a8986e348fa033a31cdd0e4121114f6bce2457e8876010b092dd/certifi-2026.2.25.tar.gz", hash = "sha256:e887ab5cee78ea814d3472169153c2d12cd43b14bd03329a39a9c6e2e80bfba7", size = 155029, upload-time = "2026-02-25T02:54:17.342Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/9a/3c/c17fb3ca2d9c3acff52e30b309f538586f9f5b9c9cf454f3845fc9af4881/certifi-2026.2.25-py3-none-any.whl", hash = "sha256:027692e4402ad994f1c42e52a4997a9763c646b73e4096e4d5d6db8af1d6f0fa", size = 153684, upload-time = "2026-02-25T02:54:15.766Z" },
]

[[package]]
name = "cffi"
version = "2.0.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "pycparser", marker = "implementation_name != 'PyPy'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/eb/56/b1ba7935a17738ae8453301356628e8147c79dbb825bcbc73dc7401f9846/cffi-2.0.0.tar.gz", hash = "sha256:44d1b5909021139fe36001ae048dbdde8214afa20200eda0f64c068cac5d5529", size = 523588, upload-time = "2025-09-08T23:24:04.541Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/4b/8d/a0a47a0c9e413a658623d014e91e74a50cdd2c423f7ccfd44086ef767f90/cffi-2.0.0-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:00bdf7acc5f795150faa6957054fbbca2439db2f775ce831222b66f192f03beb", size = 185230, upload-time = "2025-09-08T23:23:00.879Z" },
    { url = "https://files.pythonhosted.org/packages/4a/d2/a6c0296814556c68ee32009d9c2ad4f85f2707cdecfd7727951ec228005d/cffi-2.0.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:45d5e886156860dc35862657e1494b9bae8dfa63bf56796f2fb56e1679fc0bca", size = 181043, upload-time = "2025-09-08T23:23:02.231Z" },
    { url = "https://files.pythonhosted.org/packages/b0/1e/d22cc63332bd59b06481ceaac49d6c507598642e2230f201649058a7e704/cffi-2.0.0-cp313-cp313-manylinux1_i686.manylinux2014_i686.manylinux_2_17_i686.manylinux_2_5_i686.whl", hash = "sha256:07b271772c100085dd28b74fa0cd81c8fb1a3ba18b21e03d7c27f3436a10606b", size = 212446, upload-time = "2025-09-08T23:23:03.472Z" },
    { url = "https://files.pythonhosted.org/packages/a9/f5/a2c23eb03b61a0b8747f211eb716446c826ad66818ddc7810cc2cc19b3f2/cffi-2.0.0-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:d48a880098c96020b02d5a1f7d9251308510ce8858940e6fa99ece33f610838b", size = 220101, upload-time = "2025-09-08T23:23:04.792Z" },
    { url = "https://files.pythonhosted.org/packages/f2/7f/e6647792fc5850d634695bc0e6ab4111ae88e89981d35ac269956605feba/cffi-2.0.0-cp313-cp313-manylinux2014_ppc64le.manylinux_2_17_ppc64le.whl", hash = "sha256:f93fd8e5c8c0a4aa1f424d6173f14a892044054871c771f8566e4008eaa359d2", size = 207948, upload-time = "2025-09-08T23:23:06.127Z" },
    { url = "https://files.pythonhosted.org/packages/cb/1e/a5a1bd6f1fb30f22573f76533de12a00bf274abcdc55c8edab639078abb6/cffi-2.0.0-cp313-cp313-manylinux2014_s390x.manylinux_2_17_s390x.whl", hash = "sha256:dd4f05f54a52fb558f1ba9f528228066954fee3ebe629fc1660d874d040ae5a3", size = 206422, upload-time = "2025-09-08T23:23:07.753Z" },
    { url = "https://files.pythonhosted.org/packages/98/df/0a1755e750013a2081e863e7cd37e0cdd02664372c754e5560099eb7aa44/cffi-2.0.0-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:c8d3b5532fc71b7a77c09192b4a5a200ea992702734a2e9279a37f2478236f26", size = 219499, upload-time = "2025-09-08T23:23:09.648Z" },
    { url = "https://files.pythonhosted.org/packages/50/e1/a969e687fcf9ea58e6e2a928ad5e2dd88cc12f6f0ab477e9971f2309b57c/cffi-2.0.0-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:d9b29c1f0ae438d5ee9acb31cadee00a58c46cc9c0b2f9038c6b0b3470877a8c", size = 222928, upload-time = "2025-09-08T23:23:10.928Z" },
    { url = "https://files.pythonhosted.org/packages/36/54/0362578dd2c9e557a28ac77698ed67323ed5b9775ca9d3fe73fe191bb5d8/cffi-2.0.0-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:6d50360be4546678fc1b79ffe7a66265e28667840010348dd69a314145807a1b", size = 221302, upload-time = "2025-09-08T23:23:12.42Z" },
    { url = "https://files.pythonhosted.org/packages/eb/6d/bf9bda840d5f1dfdbf0feca87fbdb64a918a69bca42cfa0ba7b137c48cb8/cffi-2.0.0-cp313-cp313-win32.whl", hash = "sha256:74a03b9698e198d47562765773b4a8309919089150a0bb17d829ad7b44b60d27", size = 172909, upload-time = "2025-09-08T23:23:14.32Z" },
    { url = "https://files.pythonhosted.org/packages/37/18/6519e1ee6f5a1e579e04b9ddb6f1676c17368a7aba48299c3759bbc3c8b3/cffi-2.0.0-cp313-cp313-win_amd64.whl", hash = "sha256:19f705ada2530c1167abacb171925dd886168931e0a7b78f5bffcae5c6b5be75", size = 183402, upload-time = "2025-09-08T23:23:15.535Z" },
    { url = "https://files.pythonhosted.org/packages/cb/0e/02ceeec9a7d6ee63bb596121c2c8e9b3a9e150936f4fbef6ca1943e6137c/cffi-2.0.0-cp313-cp313-win_arm64.whl", hash = "sha256:256f80b80ca3853f90c21b23ee78cd008713787b1b1e93eae9f3d6a7134abd91", size = 177780, upload-time = "2025-09-08T23:23:16.761Z" },
    { url = "https://files.pythonhosted.org/packages/92/c4/3ce07396253a83250ee98564f8d7e9789fab8e58858f35d07a9a2c78de9f/cffi-2.0.0-cp314-cp314-macosx_10_13_x86_64.whl", hash = "sha256:fc33c5141b55ed366cfaad382df24fe7dcbc686de5be719b207bb248e3053dc5", size = 185320, upload-time = "2025-09-08T23:23:18.087Z" },
    { url = "https://files.pythonhosted.org/packages/59/dd/27e9fa567a23931c838c6b02d0764611c62290062a6d4e8ff7863daf9730/cffi-2.0.0-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:c654de545946e0db659b3400168c9ad31b5d29593291482c43e3564effbcee13", size = 181487, upload-time = "2025-09-08T23:23:19.622Z" },
    { url = "https://files.pythonhosted.org/packages/d6/43/0e822876f87ea8a4ef95442c3d766a06a51fc5298823f884ef87aaad168c/cffi-2.0.0-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:24b6f81f1983e6df8db3adc38562c83f7d4a0c36162885ec7f7b77c7dcbec97b", size = 220049, upload-time = "2025-09-08T23:23:20.853Z" },
    { url = "https://files.pythonhosted.org/packages/b4/89/76799151d9c2d2d1ead63c2429da9ea9d7aac304603de0c6e8764e6e8e70/cffi-2.0.0-cp314-cp314-manylinux2014_ppc64le.manylinux_2_17_ppc64le.whl", hash = "sha256:12873ca6cb9b0f0d3a0da705d6086fe911591737a59f28b7936bdfed27c0d47c", size = 207793, upload-time = "2025-09-08T23:23:22.08Z" },
    { url = "https://files.pythonhosted.org/packages/bb/dd/3465b14bb9e24ee24cb88c9e3730f6de63111fffe513492bf8c808a3547e/cffi-2.0.0-cp314-cp314-manylinux2014_s390x.manylinux_2_17_s390x.whl", hash = "sha256:d9b97165e8aed9272a6bb17c01e3cc5871a594a446ebedc996e2397a1c1ea8ef", size = 206300, upload-time = "2025-09-08T23:23:23.314Z" },
    { url = "https://files.pythonhosted.org/packages/47/d9/d83e293854571c877a92da46fdec39158f8d7e68da75bf73581225d28e90/cffi-2.0.0-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:afb8db5439b81cf9c9d0c80404b60c3cc9c3add93e114dcae767f1477cb53775", size = 219244, upload-time = "2025-09-08T23:23:24.541Z" },
    { url = "https://files.pythonhosted.org/packages/2b/0f/1f177e3683aead2bb00f7679a16451d302c436b5cbf2505f0ea8146ef59e/cffi-2.0.0-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:737fe7d37e1a1bffe70bd5754ea763a62a066dc5913ca57e957824b72a85e205", size = 222828, upload-time = "2025-09-08T23:23:26.143Z" },
    { url = "https://files.pythonhosted.org/packages/c6/0f/cafacebd4b040e3119dcb32fed8bdef8dfe94da653155f9d0b9dc660166e/cffi-2.0.0-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:38100abb9d1b1435bc4cc340bb4489635dc2f0da7456590877030c9b3d40b0c1", size = 220926, upload-time = "2025-09-08T23:23:27.873Z" },
    { url = "https://files.pythonhosted.org/packages/3e/aa/df335faa45b395396fcbc03de2dfcab242cd61a9900e914fe682a59170b1/cffi-2.0.0-cp314-cp314-win32.whl", hash = "sha256:087067fa8953339c723661eda6b54bc98c5625757ea62e95eb4898ad5e776e9f", size = 175328, upload-time = "2025-09-08T23:23:44.61Z" },
    { url = "https://files.pythonhosted.org/packages/bb/92/882c2d30831744296ce713f0feb4c1cd30f346ef747b530b5318715cc367/cffi-2.0.0-cp314-cp314-win_amd64.whl", hash = "sha256:203a48d1fb583fc7d78a4c6655692963b860a417c0528492a6bc21f1aaefab25", size = 185650, upload-time = "2025-09-08T23:23:45.848Z" },
    { url = "https://files.pythonhosted.org/packages/9f/2c/98ece204b9d35a7366b5b2c6539c350313ca13932143e79dc133ba757104/cffi-2.0.0-cp314-cp314-win_arm64.whl", hash = "sha256:dbd5c7a25a7cb98f5ca55d258b103a2054f859a46ae11aaf23134f9cc0d356ad", size = 180687, upload-time = "2025-09-08T23:23:47.105Z" },
    { url = "https://files.pythonhosted.org/packages/3e/61/c768e4d548bfa607abcda77423448df8c471f25dbe64fb2ef6d555eae006/cffi-2.0.0-cp314-cp314t-macosx_10_13_x86_64.whl", hash = "sha256:9a67fc9e8eb39039280526379fb3a70023d77caec1852002b4da7e8b270c4dd9", size = 188773, upload-time = "2025-09-08T23:23:29.347Z" },
    { url = "https://files.pythonhosted.org/packages/2c/ea/5f76bce7cf6fcd0ab1a1058b5af899bfbef198bea4d5686da88471ea0336/cffi-2.0.0-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:7a66c7204d8869299919db4d5069a82f1561581af12b11b3c9f48c584eb8743d", size = 185013, upload-time = "2025-09-08T23:23:30.63Z" },
    { url = "https://files.pythonhosted.org/packages/be/b4/c56878d0d1755cf9caa54ba71e5d049479c52f9e4afc230f06822162ab2f/cffi-2.0.0-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:7cc09976e8b56f8cebd752f7113ad07752461f48a58cbba644139015ac24954c", size = 221593, upload-time = "2025-09-08T23:23:31.91Z" },
    { url = "https://files.pythonhosted.org/packages/e0/0d/eb704606dfe8033e7128df5e90fee946bbcb64a04fcdaa97321309004000/cffi-2.0.0-cp314-cp314t-manylinux2014_ppc64le.manylinux_2_17_ppc64le.whl", hash = "sha256:92b68146a71df78564e4ef48af17551a5ddd142e5190cdf2c5624d0c3ff5b2e8", size = 209354, upload-time = "2025-09-08T23:23:33.214Z" },
    { url = "https://files.pythonhosted.org/packages/d8/19/3c435d727b368ca475fb8742ab97c9cb13a0de600ce86f62eab7fa3eea60/cffi-2.0.0-cp314-cp314t-manylinux2014_s390x.manylinux_2_17_s390x.whl", hash = "sha256:b1e74d11748e7e98e2f426ab176d4ed720a64412b6a15054378afdb71e0f37dc", size = 208480, upload-time = "2025-09-08T23:23:34.495Z" },
    { url = "https://files.pythonhosted.org/packages/d0/44/681604464ed9541673e486521497406fadcc15b5217c3e326b061696899a/cffi-2.0.0-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:28a3a209b96630bca57cce802da70c266eb08c6e97e5afd61a75611ee6c64592", size = 221584, upload-time = "2025-09-08T23:23:36.096Z" },
    { url = "https://files.pythonhosted.org/packages/25/8e/342a504ff018a2825d395d44d63a767dd8ebc927ebda557fecdaca3ac33a/cffi-2.0.0-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:7553fb2090d71822f02c629afe6042c299edf91ba1bf94951165613553984512", size = 224443, upload-time = "2025-09-08T23:23:37.328Z" },
    { url = "https://files.pythonhosted.org/packages/e1/5e/b666bacbbc60fbf415ba9988324a132c9a7a0448a9a8f125074671c0f2c3/cffi-2.0.0-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:6c6c373cfc5c83a975506110d17457138c8c63016b563cc9ed6e056a82f13ce4", size = 223437, upload-time = "2025-09-08T23:23:38.945Z" },
    { url = "https://files.pythonhosted.org/packages/a0/1d/ec1a60bd1a10daa292d3cd6bb0b359a81607154fb8165f3ec95fe003b85c/cffi-2.0.0-cp314-cp314t-win32.whl", hash = "sha256:1fc9ea04857caf665289b7a75923f2c6ed559b8298a1b8c49e59f7dd95c8481e", size = 180487, upload-time = "2025-09-08T23:23:40.423Z" },
    { url = "https://files.pythonhosted.org/packages/bf/41/4c1168c74fac325c0c8156f04b6749c8b6a8f405bbf91413ba088359f60d/cffi-2.0.0-cp314-cp314t-win_amd64.whl", hash = "sha256:d68b6cef7827e8641e8ef16f4494edda8b36104d79773a334beaa1e3521430f6", size = 191726, upload-time = "2025-09-08T23:23:41.742Z" },
    { url = "https://files.pythonhosted.org/packages/ae/3a/dbeec9d1ee0844c679f6bb5d6ad4e9f198b1224f4e7a32825f47f6192b0c/cffi-2.0.0-cp314-cp314t-win_arm64.whl", hash = "sha256:0a1527a803f0a659de1af2e1fd700213caba79377e27e4693648c2923da066f9", size = 184195, upload-time = "2025-09-08T23:23:43.004Z" },
]

[[package]]
name = "claude-agent-sdk"
version = "0.1.48"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "anyio" },
    { name = "mcp" },
]
sdist = { url = "https://files.pythonhosted.org/packages/6c/dd/2818538efd18ed4ef72d4775efa75bb36cbea0fa418eda51df85ee9c2424/claude_agent_sdk-0.1.48.tar.gz", hash = "sha256:ee294d3f02936c0b826119ffbefcf88c67731cf8c2d2cb7111ccc97f76344272", size = 87375, upload-time = "2026-03-07T00:21:37.087Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/c3/cf/bbbdee52ee0c63c8709b0ac03ce3c1da5bdc37def5da0eca63363448744f/claude_agent_sdk-0.1.48-py3-none-macosx_11_0_arm64.whl", hash = "sha256:5761ff1d362e0f17c2b1bfd890d1c897f0aa81091e37bbd15b7d06f05ced552d", size = 57559306, upload-time = "2026-03-07T00:21:20.011Z" },
    { url = "https://files.pythonhosted.org/packages/57/d1/2179154b88d4cf6ba1cf6a15066ee8e96257aaeb1330e625e809ba2f28eb/claude_agent_sdk-0.1.48-py3-none-manylinux_2_17_aarch64.whl", hash = "sha256:39c1307daa17e42fa8a71180bb20af8a789d72d3891fc93519ff15540badcb83", size = 73980309, upload-time = "2026-03-07T00:21:24.592Z" },
    { url = "https://files.pythonhosted.org/packages/dc/99/55b0cd3bf54a7449e744d23cf50be104e9445cf623e1ed75722112aa6264/claude_agent_sdk-0.1.48-py3-none-manylinux_2_17_x86_64.whl", hash = "sha256:543d70acba468eccfff836965a14b8ac88cf90809aeeb88431dfcea3ee9a2fa9", size = 74583686, upload-time = "2026-03-07T00:21:28.969Z" },
    { url = "https://files.pythonhosted.org/packages/c8/f6/4851bd9a238b7aadba7639eb906aca7da32a51f01563fa4488469c608b3a/claude_agent_sdk-0.1.48-py3-none-win_amd64.whl", hash = "sha256:0d37e60bd2b17efc3f927dccef080f14897ab62cd1d0d67a4abc8a0e2d4f1006", size = 74956045, upload-time = "2026-03-07T00:21:33.475Z" },
]

[[package]]
name = "claude-agent-sdk-example"
version = "0.1.0"
source = { virtual = "." }
dependencies = [
    { name = "acontext" },
    { name = "claude-agent-sdk" },
    { name = "python-dotenv" },
]

[package.metadata]
requires-dist = [
    { name = "acontext", specifier = ">=0.1.18" },
    { name = "claude-agent-sdk" },
    { name = "python-dotenv" },
]

[[package]]
name = "click"
version = "8.3.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "colorama", marker = "sys_platform == 'win32'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/3d/fa/656b739db8587d7b5dfa22e22ed02566950fbfbcdc20311993483657a5c0/click-8.3.1.tar.gz", hash = "sha256:12ff4785d337a1bb490bb7e9c2b1ee5da3112e94a8622f26a6c77f5d2fc6842a", size = 295065, upload-time = "2025-11-15T20:45:42.706Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/98/78/01c019cdb5d6498122777c1a43056ebb3ebfeef2076d9d026bfe15583b2b/click-8.3.1-py3-none-any.whl", hash = "sha256:981153a64e25f12d547d3426c367a4857371575ee7ad18df2a6183ab0545b2a6", size = 108274, upload-time = "2025-11-15T20:45:41.139Z" },
]

[[package]]
name = "colorama"
version = "0.4.6"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/d8/53/6f443c9a4a8358a93a6792e2acffb9d9d5cb0a5cfd8802644b7b1c9a02e4/colorama-0.4.6.tar.gz", hash = "sha256:08695f5cb7ed6e0531a20572697297273c47b8cae5a63ffc6d6ed5c201be6e44", size = 27697, upload-time = "2022-10-25T02:36:22.414Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/d1/d6/3965ed04c63042e047cb6a3e6ed1a63a35087b6a609aa3a15ed8ac56c221/colorama-0.4.6-py2.py3-none-any.whl", hash = "sha256:4f1d9991f5acc0ca119f9d443620b77f9d6b33703e51011c16baf57afb285fc6", size = 25335, upload-time = "2022-10-25T02:36:20.889Z" },
]

[[package]]
name = "cryptography"
version = "46.0.5"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "cffi", marker = "platform_python_implementation != 'PyPy'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/60/04/ee2a9e8542e4fa2773b81771ff8349ff19cdd56b7258a0cc442639052edb/cryptography-46.0.5.tar.gz", hash = "sha256:abace499247268e3757271b2f1e244b36b06f8515cf27c4d49468fc9eb16e93d", size = 750064, upload-time = "2026-02-10T19:18:38.255Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/f7/81/b0bb27f2ba931a65409c6b8a8b358a7f03c0e46eceacddff55f7c84b1f3b/cryptography-46.0.5-cp311-abi3-macosx_10_9_universal2.whl", hash = "sha256:351695ada9ea9618b3500b490ad54c739860883df6c1f555e088eaf25b1bbaad", size = 7176289, upload-time = "2026-02-10T19:17:08.274Z" },
    { url = "https://files.pythonhosted.org/packages/ff/9e/6b4397a3e3d15123de3b1806ef342522393d50736c13b20ec4c9ea6693a6/cryptography-46.0.5-cp311-abi3-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:c18ff11e86df2e28854939acde2d003f7984f721eba450b56a200ad90eeb0e6b", size = 4275637, upload-time = "2026-02-10T19:17:10.53Z" },
    { url = "https://files.pythonhosted.org/packages/63/e7/471ab61099a3920b0c77852ea3f0ea611c9702f651600397ac567848b897/cryptography-46.0.5-cp311-abi3-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:4d7e3d356b8cd4ea5aff04f129d5f66ebdc7b6f8eae802b93739ed520c47c79b", size = 4424742, upload-time = "2026-02-10T19:17:12.388Z" },
    { url = "https://files.pythonhosted.org/packages/37/53/a18500f270342d66bf7e4d9f091114e31e5ee9e7375a5aba2e85a91e0044/cryptography-46.0.5-cp311-abi3-manylinux_2_28_aarch64.whl", hash = "sha256:50bfb6925eff619c9c023b967d5b77a54e04256c4281b0e21336a130cd7fc263", size = 4277528, upload-time = "2026-02-10T19:17:13.853Z" },
    { url = "https://files.pythonhosted.org/packages/22/29/c2e812ebc38c57b40e7c583895e73c8c5adb4d1e4a0cc4c5a4fdab2b1acc/cryptography-46.0.5-cp311-abi3-manylinux_2_28_ppc64le.whl", hash = "sha256:803812e111e75d1aa73690d2facc295eaefd4439be1023fefc4995eaea2af90d", size = 4947993, upload-time = "2026-02-10T19:17:15.618Z" },
    { url = "https://files.pythonhosted.org/packages/6b/e7/237155ae19a9023de7e30ec64e5d99a9431a567407ac21170a046d22a5a3/cryptography-46.0.5-cp311-abi3-manylinux_2_28_x86_64.whl", hash = "sha256:3ee190460e2fbe447175cda91b88b84ae8322a104fc27766ad09428754a618ed", size = 4456855, upload-time = "2026-02-10T19:17:17.221Z" },
    { url = "https://files.pythonhosted.org/packages/2d/87/fc628a7ad85b81206738abbd213b07702bcbdada1dd43f72236ef3cffbb5/cryptography-46.0.5-cp311-abi3-manylinux_2_31_armv7l.whl", hash = "sha256:f145bba11b878005c496e93e257c1e88f154d278d2638e6450d17e0f31e558d2", size = 3984635, upload-time = "2026-02-10T19:17:18.792Z" },
    { url = "https://files.pythonhosted.org/packages/84/29/65b55622bde135aedf4565dc509d99b560ee4095e56989e815f8fd2aa910/cryptography-46.0.5-cp311-abi3-manylinux_2_34_aarch64.whl", hash = "sha256:e9251e3be159d1020c4030bd2e5f84d6a43fe54b6c19c12f51cde9542a2817b2", size = 4277038, upload-time = "2026-02-10T19:17:20.256Z" },
    { url = "https://files.pythonhosted.org/packages/bc/36/45e76c68d7311432741faf1fbf7fac8a196a0a735ca21f504c75d37e2558/cryptography-46.0.5-cp311-abi3-manylinux_2_34_ppc64le.whl", hash = "sha256:47fb8a66058b80e509c47118ef8a75d14c455e81ac369050f20ba0d23e77fee0", size = 4912181, upload-time = "2026-02-10T19:17:21.825Z" },
    { url = "https://files.pythonhosted.org/packages/6d/1a/c1ba8fead184d6e3d5afcf03d569acac5ad063f3ac9fb7258af158f7e378/cryptography-46.0.5-cp311-abi3-manylinux_2_34_x86_64.whl", hash = "sha256:4c3341037c136030cb46e4b1e17b7418ea4cbd9dd207e4a6f3b2b24e0d4ac731", size = 4456482, upload-time = "2026-02-10T19:17:25.133Z" },
    { url = "https://files.pythonhosted.org/packages/f9/e5/3fb22e37f66827ced3b902cf895e6a6bc1d095b5b26be26bd13c441fdf19/cryptography-46.0.5-cp311-abi3-musllinux_1_2_aarch64.whl", hash = "sha256:890bcb4abd5a2d3f852196437129eb3667d62630333aacc13dfd470fad3aaa82", size = 4405497, upload-time = "2026-02-10T19:17:26.66Z" },
    { url = "https://files.pythonhosted.org/packages/1a/df/9d58bb32b1121a8a2f27383fabae4d63080c7ca60b9b5c88be742be04ee7/cryptography-46.0.5-cp311-abi3-musllinux_1_2_x86_64.whl", hash = "sha256:80a8d7bfdf38f87ca30a5391c0c9ce4ed2926918e017c29ddf643d0ed2778ea1", size = 4667819, upload-time = "2026-02-10T19:17:28.569Z" },
    { url = "https://files.pythonhosted.org/packages/ea/ed/325d2a490c5e94038cdb0117da9397ece1f11201f425c4e9c57fe5b9f08b/cryptography-46.0.5-cp311-abi3-win32.whl", hash = "sha256:60ee7e19e95104d4c03871d7d7dfb3d22ef8a9b9c6778c94e1c8fcc8365afd48", size = 3028230, upload-time = "2026-02-10T19:17:30.518Z" },
    { url = "https://files.pythonhosted.org/packages/e9/5a/ac0f49e48063ab4255d9e3b79f5def51697fce1a95ea1370f03dc9db76f6/cryptography-46.0.5-cp311-abi3-win_amd64.whl", hash = "sha256:38946c54b16c885c72c4f59846be9743d699eee2b69b6988e0a00a01f46a61a4", size = 3480909, upload-time = "2026-02-10T19:17:32.083Z" },
    { url = "https://files.pythonhosted.org/packages/00/13/3d278bfa7a15a96b9dc22db5a12ad1e48a9eb3d40e1827ef66a5df75d0d0/cryptography-46.0.5-cp314-cp314t-macosx_10_9_universal2.whl", hash = "sha256:94a76daa32eb78d61339aff7952ea819b1734b46f73646a07decb40e5b3448e2", size = 7119287, upload-time = "2026-02-10T19:17:33.801Z" },
    { url = "https://files.pythonhosted.org/packages/67/c8/581a6702e14f0898a0848105cbefd20c058099e2c2d22ef4e476dfec75d7/cryptography-46.0.5-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:5be7bf2fb40769e05739dd0046e7b26f9d4670badc7b032d6ce4db64dddc0678", size = 4265728, upload-time = "2026-02-10T19:17:35.569Z" },
    { url = "https://files.pythonhosted.org/packages/dd/4a/ba1a65ce8fc65435e5a849558379896c957870dd64fecea97b1ad5f46a37/cryptography-46.0.5-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:fe346b143ff9685e40192a4960938545c699054ba11d4f9029f94751e3f71d87", size = 4408287, upload-time = "2026-02-10T19:17:36.938Z" },
    { url = "https://files.pythonhosted.org/packages/f8/67/8ffdbf7b65ed1ac224d1c2df3943553766914a8ca718747ee3871da6107e/cryptography-46.0.5-cp314-cp314t-manylinux_2_28_aarch64.whl", hash = "sha256:c69fd885df7d089548a42d5ec05be26050ebcd2283d89b3d30676eb32ff87dee", size = 4270291, upload-time = "2026-02-10T19:17:38.748Z" },
    { url = "https://files.pythonhosted.org/packages/f8/e5/f52377ee93bc2f2bba55a41a886fd208c15276ffbd2569f2ddc89d50e2c5/cryptography-46.0.5-cp314-cp314t-manylinux_2_28_ppc64le.whl", hash = "sha256:8293f3dea7fc929ef7240796ba231413afa7b68ce38fd21da2995549f5961981", size = 4927539, upload-time = "2026-02-10T19:17:40.241Z" },
    { url = "https://files.pythonhosted.org/packages/3b/02/cfe39181b02419bbbbcf3abdd16c1c5c8541f03ca8bda240debc467d5a12/cryptography-46.0.5-cp314-cp314t-manylinux_2_28_x86_64.whl", hash = "sha256:1abfdb89b41c3be0365328a410baa9df3ff8a9110fb75e7b52e66803ddabc9a9", size = 4442199, upload-time = "2026-02-10T19:17:41.789Z" },
    { url = "https://files.pythonhosted.org/packages/c0/96/2fcaeb4873e536cf71421a388a6c11b5bc846e986b2b069c79363dc1648e/cryptography-46.0.5-cp314-cp314t-manylinux_2_31_armv7l.whl", hash = "sha256:d66e421495fdb797610a08f43b05269e0a5ea7f5e652a89bfd5a7d3c1dee3648", size = 3960131, upload-time = "2026-02-10T19:17:43.379Z" },
    { url = "https://files.pythonhosted.org/packages/d8/d2/b27631f401ddd644e94c5cf33c9a4069f72011821cf3dc7309546b0642a0/cryptography-46.0.5-cp314-cp314t-manylinux_2_34_aarch64.whl", hash = "sha256:4e817a8920bfbcff8940ecfd60f23d01836408242b30f1a708d93198393a80b4", size = 4270072, upload-time = "2026-02-10T19:17:45.481Z" },
    { url = "https://files.pythonhosted.org/packages/f4/a7/60d32b0370dae0b4ebe55ffa10e8599a2a59935b5ece1b9f06edb73abdeb/cryptography-46.0.5-cp314-cp314t-manylinux_2_34_ppc64le.whl", hash = "sha256:68f68d13f2e1cb95163fa3b4db4bf9a159a418f5f6e7242564fc75fcae667fd0", size = 4892170, upload-time = "2026-02-10T19:17:46.997Z" },
    { url = "https://files.pythonhosted.org/packages/d2/b9/cf73ddf8ef1164330eb0b199a589103c363afa0cf794218c24d524a58eab/cryptography-46.0.5-cp314-cp314t-manylinux_2_34_x86_64.whl", hash = "sha256:a3d1fae9863299076f05cb8a778c467578262fae09f9dc0ee9b12eb4268ce663", size = 4441741, upload-time = "2026-02-10T19:17:48.661Z" },
    { url = "https://files.pythonhosted.org/packages/5f/eb/eee00b28c84c726fe8fa0158c65afe312d9c3b78d9d01daf700f1f6e37ff/cryptography-46.0.5-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:c4143987a42a2397f2fc3b4d7e3a7d313fbe684f67ff443999e803dd75a76826", size = 4396728, upload-time = "2026-02-10T19:17:50.058Z" },
    { url = "https://files.pythonhosted.org/packages/65/f4/6bc1a9ed5aef7145045114b75b77c2a8261b4d38717bd8dea111a63c3442/cryptography-46.0.5-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:7d731d4b107030987fd61a7f8ab512b25b53cef8f233a97379ede116f30eb67d", size = 4652001, upload-time = "2026-02-10T19:17:51.54Z" },
    { url = "https://files.pythonhosted.org/packages/86/ef/5d00ef966ddd71ac2e6951d278884a84a40ffbd88948ef0e294b214ae9e4/cryptography-46.0.5-cp314-cp314t-win32.whl", hash = "sha256:c3bcce8521d785d510b2aad26ae2c966092b7daa8f45dd8f44734a104dc0bc1a", size = 3003637, upload-time = "2026-02-10T19:17:52.997Z" },
    { url = "https://files.pythonhosted.org/packages/b7/57/f3f4160123da6d098db78350fdfd9705057aad21de7388eacb2401dceab9/cryptography-46.0.5-cp314-cp314t-win_amd64.whl", hash = "sha256:4d8ae8659ab18c65ced284993c2265910f6c9e650189d4e3f68445ef82a810e4", size = 3469487, upload-time = "2026-02-10T19:17:54.549Z" },
    { url = "https://files.pythonhosted.org/packages/e2/fa/a66aa722105ad6a458bebd64086ca2b72cdd361fed31763d20390f6f1389/cryptography-46.0.5-cp38-abi3-macosx_10_9_universal2.whl", hash = "sha256:4108d4c09fbbf2789d0c926eb4152ae1760d5a2d97612b92d508d96c861e4d31", size = 7170514, upload-time = "2026-02-10T19:17:56.267Z" },
    { url = "https://files.pythonhosted.org/packages/0f/04/c85bdeab78c8bc77b701bf0d9bdcf514c044e18a46dcff330df5448631b0/cryptography-46.0.5-cp38-abi3-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:7d1f30a86d2757199cb2d56e48cce14deddf1f9c95f1ef1b64ee91ea43fe2e18", size = 4275349, upload-time = "2026-02-10T19:17:58.419Z" },
    { url = "https://files.pythonhosted.org/packages/5c/32/9b87132a2f91ee7f5223b091dc963055503e9b442c98fc0b8a5ca765fab0/cryptography-46.0.5-cp38-abi3-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:039917b0dc418bb9f6edce8a906572d69e74bd330b0b3fea4f79dab7f8ddd235", size = 4420667, upload-time = "2026-02-10T19:18:00.619Z" },
    { url = "https://files.pythonhosted.org/packages/a1/a6/a7cb7010bec4b7c5692ca6f024150371b295ee1c108bdc1c400e4c44562b/cryptography-46.0.5-cp38-abi3-manylinux_2_28_aarch64.whl", hash = "sha256:ba2a27ff02f48193fc4daeadf8ad2590516fa3d0adeeb34336b96f7fa64c1e3a", size = 4276980, upload-time = "2026-02-10T19:18:02.379Z" },
    { url = "https://files.pythonhosted.org/packages/8e/7c/c4f45e0eeff9b91e3f12dbd0e165fcf2a38847288fcfd889deea99fb7b6d/cryptography-46.0.5-cp38-abi3-manylinux_2_28_ppc64le.whl", hash = "sha256:61aa400dce22cb001a98014f647dc21cda08f7915ceb95df0c9eaf84b4b6af76", size = 4939143, upload-time = "2026-02-10T19:18:03.964Z" },
    { url = "https://files.pythonhosted.org/packages/37/19/e1b8f964a834eddb44fa1b9a9976f4e414cbb7aa62809b6760c8803d22d1/cryptography-46.0.5-cp38-abi3-manylinux_2_28_x86_64.whl", hash = "sha256:3ce58ba46e1bc2aac4f7d9290223cead56743fa6ab94a5d53292ffaac6a91614", size = 4453674, upload-time = "2026-02-10T19:18:05.588Z" },
    { url = "https://files.pythonhosted.org/packages/db/ed/db15d3956f65264ca204625597c410d420e26530c4e2943e05a0d2f24d51/cryptography-46.0.5-cp38-abi3-manylinux_2_31_armv7l.whl", hash = "sha256:420d0e909050490d04359e7fdb5ed7e667ca5c3c402b809ae2563d7e66a92229", size = 3978801, upload-time = "2026-02-10T19:18:07.167Z" },
    { url = "https://files.pythonhosted.org/packages/41/e2/df40a31d82df0a70a0daf69791f91dbb70e47644c58581d654879b382d11/cryptography-46.0.5-cp38-abi3-manylinux_2_34_aarch64.whl", hash = "sha256:582f5fcd2afa31622f317f80426a027f30dc792e9c80ffee87b993200ea115f1", size = 4276755, upload-time = "2026-02-10T19:18:09.813Z" },
    { url = "https://files.pythonhosted.org/packages/33/45/726809d1176959f4a896b86907b98ff4391a8aa29c0aaaf9450a8a10630e/cryptography-46.0.5-cp38-abi3-manylinux_2_34_ppc64le.whl", hash = "sha256:bfd56bb4b37ed4f330b82402f6f435845a5f5648edf1ad497da51a8452d5d62d", size = 4901539, upload-time = "2026-02-10T19:18:11.263Z" },
    { url = "https://files.pythonhosted.org/packages/99/0f/a3076874e9c88ecb2ecc31382f6e7c21b428ede6f55aafa1aa272613e3cd/cryptography-46.0.5-cp38-abi3-manylinux_2_34_x86_64.whl", hash = "sha256:a3d507bb6a513ca96ba84443226af944b0f7f47dcc9a399d110cd6146481d24c", size = 4452794, upload-time = "2026-02-10T19:18:12.914Z" },
    { url = "https://files.pythonhosted.org/packages/02/ef/ffeb542d3683d24194a38f66ca17c0a4b8bf10631feef44a7ef64e631b1a/cryptography-46.0.5-cp38-abi3-musllinux_1_2_aarch64.whl", hash = "sha256:9f16fbdf4da055efb21c22d81b89f155f02ba420558db21288b3d0035bafd5f4", size = 4404160, upload-time = "2026-02-10T19:18:14.375Z" },
    { url = "https://files.pythonhosted.org/packages/96/93/682d2b43c1d5f1406ed048f377c0fc9fc8f7b0447a478d5c65ab3d3a66eb/cryptography-46.0.5-cp38-abi3-musllinux_1_2_x86_64.whl", hash = "sha256:ced80795227d70549a411a4ab66e8ce307899fad2220ce5ab2f296e687eacde9", size = 4667123, upload-time = "2026-02-10T19:18:15.886Z" },
    { url = "https://files.pythonhosted.org/packages/45/2d/9c5f2926cb5300a8eefc3f4f0b3f3df39db7f7ce40c8365444c49363cbda/cryptography-46.0.5-cp38-abi3-win32.whl", hash = "sha256:02f547fce831f5096c9a567fd41bc12ca8f11df260959ecc7c3202555cc47a72", size = 3010220, upload-time = "2026-02-10T19:18:17.361Z" },
    { url = "https://files.pythonhosted.org/packages/48/ef/0c2f4a8e31018a986949d34a01115dd057bf536905dca38897bacd21fac3/cryptography-46.0.5-cp38-abi3-win_amd64.whl", hash = "sha256:556e106ee01aa13484ce9b0239bca667be5004efb0aabbed28d353df86445595", size = 3467050, upload-time = "2026-02-10T19:18:18.899Z" },
]

[[package]]
name = "distro"
version = "1.9.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/fc/f8/98eea607f65de6527f8a2e8885fc8015d3e6f5775df186e443e0964a11c3/distro-1.9.0.tar.gz", hash = "sha256:2fa77c6fd8940f116ee1d6b94a2f90b13b5ea8d019b98bc8bafdcabcdd9bdbed", size = 60722, upload-time = "2023-12-24T09:54:32.31Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/12/b3/231ffd4ab1fc9d679809f356cebee130ac7daa00d6d6f3206dd4fd137e9e/distro-1.9.0-py3-none-any.whl", hash = "sha256:7bffd925d65168f85027d8da9af6bddab658135b840670a223589bc0c8ef02b2", size = 20277, upload-time = "2023-12-24T09:54:30.421Z" },
]

[[package]]
name = "docstring-parser"
version = "0.17.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/b2/9d/c3b43da9515bd270df0f80548d9944e389870713cc1fe2b8fb35fe2bcefd/docstring_parser-0.17.0.tar.gz", hash = "sha256:583de4a309722b3315439bb31d64ba3eebada841f2e2cee23b99df001434c912", size = 27442, upload-time = "2025-07-21T07:35:01.868Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/55/e2/2537ebcff11c1ee1ff17d8d0b6f4db75873e3b0fb32c2d4a2ee31ecb310a/docstring_parser-0.17.0-py3-none-any.whl", hash = "sha256:cf2569abd23dce8099b300f9b4fa8191e9582dda731fd533daf54c4551658708", size = 36896, upload-time = "2025-07-21T07:35:00.684Z" },
]

[[package]]
name = "h11"
version = "0.16.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/01/ee/02a2c011bdab74c6fb3c75474d40b3052059d95df7e73351460c8588d963/h11-0.16.0.tar.gz", hash = "sha256:4e35b956cf45792e4caa5885e69fba00bdbc6ffafbfa020300e549b208ee5ff1", size = 101250, upload-time = "2025-04-24T03:35:25.427Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/04/4b/29cac41a4d98d144bf5f6d33995617b185d14b22401f75ca86f384e87ff1/h11-0.16.0-py3-none-any.whl", hash = "sha256:63cf8bbe7522de3bf65932fda1d9c2772064ffb3dae62d55932da54b31cb6c86", size = 37515, upload-time = "2025-04-24T03:35:24.344Z" },
]

[[package]]
name = "httpcore"
version = "1.0.9"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "certifi" },
    { name = "h11" },
]
sdist = { url = "https://files.pythonhosted.org/packages/06/94/82699a10bca87a5556c9c59b5963f2d039dbd239f25bc2a63907a05a14cb/httpcore-1.0.9.tar.gz", hash = "sha256:6e34463af53fd2ab5d807f399a9b45ea31c3dfa2276f15a2c3f00afff6e176e8", size = 85484, upload-time = "2025-04-24T22:06:22.219Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/7e/f5/f66802a942d491edb555dd61e3a9961140fd64c90bce1eafd741609d334d/httpcore-1.0.9-py3-none-any.whl", hash = "sha256:2d400746a40668fc9dec9810239072b40b4484b640a8c38fd654a024c7a1bf55", size = 78784, upload-time = "2025-04-24T22:06:20.566Z" },
]

[[package]]
name = "httpx"
version = "0.28.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "anyio" },
    { name = "certifi" },
    { name = "httpcore" },
    { name = "idna" },
]
sdist = { url = "https://files.pythonhosted.org/packages/b1/df/48c586a5fe32a0f01324ee087459e112ebb7224f646c0b5023f5e79e9956/httpx-0.28.1.tar.gz", hash = "sha256:75e98c5f16b0f35b567856f597f06ff2270a374470a5c2392242528e3e3e42fc", size = 141406, upload-time = "2024-12-06T15:37:23.222Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/2a/39/e50c7c3a983047577ee07d2a9e53faf5a69493943ec3f6a384bdc792deb2/httpx-0.28.1-py3-none-any.whl", hash = "sha256:d909fcccc110f8c7faf814ca82a9a4d816bc5a6dbfea25d6591d6985b8ba59ad", size = 73517, upload-time = "2024-12-06T15:37:21.509Z" },
]

[[package]]
name = "httpx-sse"
version = "0.4.3"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/0f/4c/751061ffa58615a32c31b2d82e8482be8dd4a89154f003147acee90f2be9/httpx_sse-0.4.3.tar.gz", hash = "sha256:9b1ed0127459a66014aec3c56bebd93da3c1bc8bb6618c8082039a44889a755d", size = 15943, upload-time = "2025-10-10T21:48:22.271Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/d2/fd/6668e5aec43ab844de6fc74927e155a3b37bf40d7c3790e49fc0406b6578/httpx_sse-0.4.3-py3-none-any.whl", hash = "sha256:0ac1c9fe3c0afad2e0ebb25a934a59f4c7823b60792691f779fad2c5568830fc", size = 8960, upload-time = "2025-10-10T21:48:21.158Z" },
]

[[package]]
name = "idna"
version = "3.11"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/6f/6d/0703ccc57f3a7233505399edb88de3cbd678da106337b9fcde432b65ed60/idna-3.11.tar.gz", hash = "sha256:795dafcc9c04ed0c1fb032c2aa73654d8e8c5023a7df64a53f39190ada629902", size = 194582, upload-time = "2025-10-12T14:55:20.501Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/0e/61/66938bbb5fc52dbdf84594873d5b51fb1f7c7794e9c0f5bd885f30bc507b/idna-3.11-py3-none-any.whl", hash = "sha256:771a87f49d9defaf64091e6e6fe9c18d4833f140bd19464795bc32d966ca37ea", size = 71008, upload-time = "2025-10-12T14:55:18.883Z" },
]

[[package]]
name = "jiter"
version = "0.13.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/0d/5e/4ec91646aee381d01cdb9974e30882c9cd3b8c5d1079d6b5ff4af522439a/jiter-0.13.0.tar.gz", hash = "sha256:f2839f9c2c7e2dffc1bc5929a510e14ce0a946be9365fd1219e7ef342dae14f4", size = 164847, upload-time = "2026-02-02T12:37:56.441Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/91/9c/7ee5a6ff4b9991e1a45263bfc46731634c4a2bde27dfda6c8251df2d958c/jiter-0.13.0-cp313-cp313-macosx_10_12_x86_64.whl", hash = "sha256:1f8a55b848cbabf97d861495cd65f1e5c590246fabca8b48e1747c4dfc8f85bf", size = 306897, upload-time = "2026-02-02T12:36:16.748Z" },
    { url = "https://files.pythonhosted.org/packages/7c/02/be5b870d1d2be5dd6a91bdfb90f248fbb7dcbd21338f092c6b89817c3dbf/jiter-0.13.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:f556aa591c00f2c45eb1b89f68f52441a016034d18b65da60e2d2875bbbf344a", size = 317507, upload-time = "2026-02-02T12:36:18.351Z" },
    { url = "https://files.pythonhosted.org/packages/da/92/b25d2ec333615f5f284f3a4024f7ce68cfa0604c322c6808b2344c7f5d2b/jiter-0.13.0-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:f7e1d61da332ec412350463891923f960c3073cf1aae93b538f0bb4c8cd46efb", size = 350560, upload-time = "2026-02-02T12:36:19.746Z" },
    { url = "https://files.pythonhosted.org/packages/be/ec/74dcb99fef0aca9fbe56b303bf79f6bd839010cb18ad41000bf6cc71eec0/jiter-0.13.0-cp313-cp313-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:3097d665a27bc96fd9bbf7f86178037db139f319f785e4757ce7ccbf390db6c2", size = 363232, upload-time = "2026-02-02T12:36:21.243Z" },
    { url = "https://files.pythonhosted.org/packages/1b/37/f17375e0bb2f6a812d4dd92d7616e41917f740f3e71343627da9db2824ce/jiter-0.13.0-cp313-cp313-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:9d01ecc3a8cbdb6f25a37bd500510550b64ddf9f7d64a107d92f3ccb25035d0f", size = 483727, upload-time = "2026-02-02T12:36:22.688Z" },
    { url = "https://files.pythonhosted.org/packages/77/d2/a71160a5ae1a1e66c1395b37ef77da67513b0adba73b993a27fbe47eb048/jiter-0.13.0-cp313-cp313-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:ed9bbc30f5d60a3bdf63ae76beb3f9db280d7f195dfcfa61af792d6ce912d159", size = 370799, upload-time = "2026-02-02T12:36:24.106Z" },
    { url = "https://files.pythonhosted.org/packages/01/99/ed5e478ff0eb4e8aa5fd998f9d69603c9fd3f32de3bd16c2b1194f68361c/jiter-0.13.0-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:98fbafb6e88256f4454de33c1f40203d09fc33ed19162a68b3b257b29ca7f663", size = 359120, upload-time = "2026-02-02T12:36:25.519Z" },
    { url = "https://files.pythonhosted.org/packages/16/be/7ffd08203277a813f732ba897352797fa9493faf8dc7995b31f3d9cb9488/jiter-0.13.0-cp313-cp313-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:5467696f6b827f1116556cb0db620440380434591e93ecee7fd14d1a491b6daa", size = 390664, upload-time = "2026-02-02T12:36:26.866Z" },
    { url = "https://files.pythonhosted.org/packages/d1/84/e0787856196d6d346264d6dcccb01f741e5f0bd014c1d9a2ebe149caf4f3/jiter-0.13.0-cp313-cp313-musllinux_1_1_aarch64.whl", hash = "sha256:2d08c9475d48b92892583df9da592a0e2ac49bcd41fae1fec4f39ba6cf107820", size = 513543, upload-time = "2026-02-02T12:36:28.217Z" },
    { url = "https://files.pythonhosted.org/packages/65/50/ecbd258181c4313cf79bca6c88fb63207d04d5bf5e4f65174114d072aa55/jiter-0.13.0-cp313-cp313-musllinux_1_1_x86_64.whl", hash = "sha256:aed40e099404721d7fcaf5b89bd3b4568a4666358bcac7b6b15c09fb6252ab68", size = 547262, upload-time = "2026-02-02T12:36:29.678Z" },
    { url = "https://files.pythonhosted.org/packages/27/da/68f38d12e7111d2016cd198161b36e1f042bd115c169255bcb7ec823a3bf/jiter-0.13.0-cp313-cp313-win32.whl", hash = "sha256:36ebfbcffafb146d0e6ffb3e74d51e03d9c35ce7c625c8066cdbfc7b953bdc72", size = 200630, upload-time = "2026-02-02T12:36:31.808Z" },
    { url = "https://files.pythonhosted.org/packages/25/65/3bd1a972c9a08ecd22eb3b08a95d1941ebe6938aea620c246cf426ae09c2/jiter-0.13.0-cp313-cp313-win_amd64.whl", hash = "sha256:8d76029f077379374cf0dbc78dbe45b38dec4a2eb78b08b5194ce836b2517afc", size = 202602, upload-time = "2026-02-02T12:36:33.679Z" },
    { url = "https://files.pythonhosted.org/packages/15/fe/13bd3678a311aa67686bb303654792c48206a112068f8b0b21426eb6851e/jiter-0.13.0-cp313-cp313-win_arm64.whl", hash = "sha256:bb7613e1a427cfcb6ea4544f9ac566b93d5bf67e0d48c787eca673ff9c9dff2b", size = 185939, upload-time = "2026-02-02T12:36:35.065Z" },
    { url = "https://files.pythonhosted.org/packages/49/19/a929ec002ad3228bc97ca01dbb14f7632fffdc84a95ec92ceaf4145688ae/jiter-0.13.0-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:fa476ab5dd49f3bf3a168e05f89358c75a17608dbabb080ef65f96b27c19ab10", size = 316616, upload-time = "2026-02-02T12:36:36.579Z" },
    { url = "https://files.pythonhosted.org/packages/52/56/d19a9a194afa37c1728831e5fb81b7722c3de18a3109e8f282bfc23e587a/jiter-0.13.0-cp313-cp313t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:ade8cb6ff5632a62b7dbd4757d8c5573f7a2e9ae285d6b5b841707d8363205ef", size = 346850, upload-time = "2026-02-02T12:36:38.058Z" },
    { url = "https://files.pythonhosted.org/packages/36/4a/94e831c6bf287754a8a019cb966ed39ff8be6ab78cadecf08df3bb02d505/jiter-0.13.0-cp313-cp313t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:9950290340acc1adaded363edd94baebcee7dabdfa8bee4790794cd5cfad2af6", size = 358551, upload-time = "2026-02-02T12:36:39.417Z" },
    { url = "https://files.pythonhosted.org/packages/a2/ec/a4c72c822695fa80e55d2b4142b73f0012035d9fcf90eccc56bc060db37c/jiter-0.13.0-cp313-cp313t-win_amd64.whl", hash = "sha256:2b4972c6df33731aac0742b64fd0d18e0a69bc7d6e03108ce7d40c85fd9e3e6d", size = 201950, upload-time = "2026-02-02T12:36:40.791Z" },
    { url = "https://files.pythonhosted.org/packages/b6/00/393553ec27b824fbc29047e9c7cd4a3951d7fbe4a76743f17e44034fa4e4/jiter-0.13.0-cp313-cp313t-win_arm64.whl", hash = "sha256:701a1e77d1e593c1b435315ff625fd071f0998c5f02792038a5ca98899261b7d", size = 185852, upload-time = "2026-02-02T12:36:42.077Z" },
    { url = "https://files.pythonhosted.org/packages/6e/f5/f1997e987211f6f9bd71b8083047b316208b4aca0b529bb5f8c96c89ef3e/jiter-0.13.0-cp314-cp314-macosx_10_12_x86_64.whl", hash = "sha256:cc5223ab19fe25e2f0bf2643204ad7318896fe3729bf12fde41b77bfc4fafff0", size = 308804, upload-time = "2026-02-02T12:36:43.496Z" },
    { url = "https://files.pythonhosted.org/packages/cd/8f/5482a7677731fd44881f0204981ce2d7175db271f82cba2085dd2212e095/jiter-0.13.0-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:9776ebe51713acf438fd9b4405fcd86893ae5d03487546dae7f34993217f8a91", size = 318787, upload-time = "2026-02-02T12:36:45.071Z" },
    { url = "https://files.pythonhosted.org/packages/f3/b9/7257ac59778f1cd025b26a23c5520a36a424f7f1b068f2442a5b499b7464/jiter-0.13.0-cp314-cp314-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:879e768938e7b49b5e90b7e3fecc0dbec01b8cb89595861fb39a8967c5220d09", size = 353880, upload-time = "2026-02-02T12:36:47.365Z" },
    { url = "https://files.pythonhosted.org/packages/c3/87/719eec4a3f0841dad99e3d3604ee4cba36af4419a76f3cb0b8e2e691ad67/jiter-0.13.0-cp314-cp314-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:682161a67adea11e3aae9038c06c8b4a9a71023228767477d683f69903ebc607", size = 366702, upload-time = "2026-02-02T12:36:48.871Z" },
    { url = "https://files.pythonhosted.org/packages/d2/65/415f0a75cf6921e43365a1bc227c565cb949caca8b7532776e430cbaa530/jiter-0.13.0-cp314-cp314-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:a13b68cd1cd8cc9de8f244ebae18ccb3e4067ad205220ef324c39181e23bbf66", size = 486319, upload-time = "2026-02-02T12:36:53.006Z" },
    { url = "https://files.pythonhosted.org/packages/54/a2/9e12b48e82c6bbc6081fd81abf915e1443add1b13d8fc586e1d90bb02bb8/jiter-0.13.0-cp314-cp314-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:87ce0f14c6c08892b610686ae8be350bf368467b6acd5085a5b65441e2bf36d2", size = 372289, upload-time = "2026-02-02T12:36:54.593Z" },
    { url = "https://files.pythonhosted.org/packages/4e/c1/e4693f107a1789a239c759a432e9afc592366f04e901470c2af89cfd28e1/jiter-0.13.0-cp314-cp314-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:0c365005b05505a90d1c47856420980d0237adf82f70c4aff7aebd3c1cc143ad", size = 360165, upload-time = "2026-02-02T12:36:56.112Z" },
    { url = "https://files.pythonhosted.org/packages/17/08/91b9ea976c1c758240614bd88442681a87672eebc3d9a6dde476874e706b/jiter-0.13.0-cp314-cp314-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:1317fdffd16f5873e46ce27d0e0f7f4f90f0cdf1d86bf6abeaea9f63ca2c401d", size = 389634, upload-time = "2026-02-02T12:36:57.495Z" },
    { url = "https://files.pythonhosted.org/packages/18/23/58325ef99390d6d40427ed6005bf1ad54f2577866594bcf13ce55675f87d/jiter-0.13.0-cp314-cp314-musllinux_1_1_aarch64.whl", hash = "sha256:c05b450d37ba0c9e21c77fef1f205f56bcee2330bddca68d344baebfc55ae0df", size = 514933, upload-time = "2026-02-02T12:36:58.909Z" },
    { url = "https://files.pythonhosted.org/packages/5b/25/69f1120c7c395fd276c3996bb8adefa9c6b84c12bb7111e5c6ccdcd8526d/jiter-0.13.0-cp314-cp314-musllinux_1_1_x86_64.whl", hash = "sha256:775e10de3849d0631a97c603f996f518159272db00fdda0a780f81752255ee9d", size = 548842, upload-time = "2026-02-02T12:37:00.433Z" },
    { url = "https://files.pythonhosted.org/packages/18/05/981c9669d86850c5fbb0d9e62bba144787f9fba84546ba43d624ee27ef29/jiter-0.13.0-cp314-cp314-win32.whl", hash = "sha256:632bf7c1d28421c00dd8bbb8a3bac5663e1f57d5cd5ed962bce3c73bf62608e6", size = 202108, upload-time = "2026-02-02T12:37:01.718Z" },
    { url = "https://files.pythonhosted.org/packages/8d/96/cdcf54dd0b0341db7d25413229888a346c7130bd20820530905fdb65727b/jiter-0.13.0-cp314-cp314-win_amd64.whl", hash = "sha256:f22ef501c3f87ede88f23f9b11e608581c14f04db59b6a801f354397ae13739f", size = 204027, upload-time = "2026-02-02T12:37:03.075Z" },
    { url = "https://files.pythonhosted.org/packages/fb/f9/724bcaaab7a3cd727031fe4f6995cb86c4bd344909177c186699c8dec51a/jiter-0.13.0-cp314-cp314-win_arm64.whl", hash = "sha256:07b75fe09a4ee8e0c606200622e571e44943f47254f95e2436c8bdcaceb36d7d", size = 187199, upload-time = "2026-02-02T12:37:04.414Z" },
    { url = "https://files.pythonhosted.org/packages/62/92/1661d8b9fd6a3d7a2d89831db26fe3c1509a287d83ad7838831c7b7a5c7e/jiter-0.13.0-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:964538479359059a35fb400e769295d4b315ae61e4105396d355a12f7fef09f0", size = 318423, upload-time = "2026-02-02T12:37:05.806Z" },
    { url = "https://files.pythonhosted.org/packages/4f/3b/f77d342a54d4ebcd128e520fc58ec2f5b30a423b0fd26acdfc0c6fef8e26/jiter-0.13.0-cp314-cp314t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:e104da1db1c0991b3eaed391ccd650ae8d947eab1480c733e5a3fb28d4313e40", size = 351438, upload-time = "2026-02-02T12:37:07.189Z" },
    { url = "https://files.pythonhosted.org/packages/76/b3/ba9a69f0e4209bd3331470c723c2f5509e6f0482e416b612431a5061ed71/jiter-0.13.0-cp314-cp314t-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:0e3a5f0cde8ff433b8e88e41aa40131455420fb3649a3c7abdda6145f8cb7202", size = 364774, upload-time = "2026-02-02T12:37:08.579Z" },
    { url = "https://files.pythonhosted.org/packages/b3/16/6cdb31fa342932602458dbb631bfbd47f601e03d2e4950740e0b2100b570/jiter-0.13.0-cp314-cp314t-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:57aab48f40be1db920a582b30b116fe2435d184f77f0e4226f546794cedd9cf0", size = 487238, upload-time = "2026-02-02T12:37:10.066Z" },
    { url = "https://files.pythonhosted.org/packages/ed/b1/956cc7abaca8d95c13aa8d6c9b3f3797241c246cd6e792934cc4c8b250d2/jiter-0.13.0-cp314-cp314t-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:7772115877c53f62beeb8fd853cab692dbc04374ef623b30f997959a4c0e7e95", size = 372892, upload-time = "2026-02-02T12:37:11.656Z" },
    { url = "https://files.pythonhosted.org/packages/26/c4/97ecde8b1e74f67b8598c57c6fccf6df86ea7861ed29da84629cdbba76c4/jiter-0.13.0-cp314-cp314t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:1211427574b17b633cfceba5040de8081e5abf114f7a7602f73d2e16f9fdaa59", size = 360309, upload-time = "2026-02-02T12:37:13.244Z" },
    { url = "https://files.pythonhosted.org/packages/4b/d7/eabe3cf46715854ccc80be2cd78dd4c36aedeb30751dbf85a1d08c14373c/jiter-0.13.0-cp314-cp314t-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:7beae3a3d3b5212d3a55d2961db3c292e02e302feb43fce6a3f7a31b90ea6dfe", size = 389607, upload-time = "2026-02-02T12:37:14.881Z" },
    { url = "https://files.pythonhosted.org/packages/df/2d/03963fc0804e6109b82decfb9974eb92df3797fe7222428cae12f8ccaa0c/jiter-0.13.0-cp314-cp314t-musllinux_1_1_aarch64.whl", hash = "sha256:e5562a0f0e90a6223b704163ea28e831bd3a9faa3512a711f031611e6b06c939", size = 514986, upload-time = "2026-02-02T12:37:16.326Z" },
    { url = "https://files.pythonhosted.org/packages/f6/6c/8c83b45eb3eb1c1e18d841fe30b4b5bc5619d781267ca9bc03e005d8fd0a/jiter-0.13.0-cp314-cp314t-musllinux_1_1_x86_64.whl", hash = "sha256:6c26a424569a59140fb51160a56df13f438a2b0967365e987889186d5fc2f6f9", size = 548756, upload-time = "2026-02-02T12:37:17.736Z" },
    { url = "https://files.pythonhosted.org/packages/47/66/eea81dfff765ed66c68fd2ed8c96245109e13c896c2a5015c7839c92367e/jiter-0.13.0-cp314-cp314t-win32.whl", hash = "sha256:24dc96eca9f84da4131cdf87a95e6ce36765c3b156fc9ae33280873b1c32d5f6", size = 201196, upload-time = "2026-02-02T12:37:19.101Z" },
    { url = "https://files.pythonhosted.org/packages/ff/32/4ac9c7a76402f8f00d00842a7f6b83b284d0cf7c1e9d4227bc95aa6d17fa/jiter-0.13.0-cp314-cp314t-win_amd64.whl", hash = "sha256:0a8d76c7524087272c8ae913f5d9d608bd839154b62c4322ef65723d2e5bb0b8", size = 204215, upload-time = "2026-02-02T12:37:20.495Z" },
    { url = "https://files.pythonhosted.org/packages/f9/8e/7def204fea9f9be8b3c21a6f2dd6c020cf56c7d5ff753e0e23ed7f9ea57e/jiter-0.13.0-cp314-cp314t-win_arm64.whl", hash = "sha256:2c26cf47e2cad140fa23b6d58d435a7c0161f5c514284802f25e87fddfe11024", size = 187152, upload-time = "2026-02-02T12:37:22.124Z" },
]

[[package]]
name = "jsonschema"
version = "4.26.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "attrs" },
    { name = "jsonschema-specifications" },
    { name = "referencing" },
    { name = "rpds-py" },
]
sdist = { url = "https://files.pythonhosted.org/packages/b3/fc/e067678238fa451312d4c62bf6e6cf5ec56375422aee02f9cb5f909b3047/jsonschema-4.26.0.tar.gz", hash = "sha256:0c26707e2efad8aa1bfc5b7ce170f3fccc2e4918ff85989ba9ffa9facb2be326", size = 366583, upload-time = "2026-01-07T13:41:07.246Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/69/90/f63fb5873511e014207a475e2bb4e8b2e570d655b00ac19a9a0ca0a385ee/jsonschema-4.26.0-py3-none-any.whl", hash = "sha256:d489f15263b8d200f8387e64b4c3a75f06629559fb73deb8fdfb525f2dab50ce", size = 90630, upload-time = "2026-01-07T13:41:05.306Z" },
]

[[package]]
name = "jsonschema-specifications"
version = "2025.9.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "referencing" },
]
sdist = { url = "https://files.pythonhosted.org/packages/19/74/a633ee74eb36c44aa6d1095e7cc5569bebf04342ee146178e2d36600708b/jsonschema_specifications-2025.9.1.tar.gz", hash = "sha256:b540987f239e745613c7a9176f3edb72b832a4ac465cf02712288397832b5e8d", size = 32855, upload-time = "2025-09-08T01:34:59.186Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/41/45/1a4ed80516f02155c51f51e8cedb3c1902296743db0bbc66608a0db2814f/jsonschema_specifications-2025.9.1-py3-none-any.whl", hash = "sha256:98802fee3a11ee76ecaca44429fda8a41bff98b00a0f2838151b113f210cc6fe", size = 18437, upload-time = "2025-09-08T01:34:57.871Z" },
]

[[package]]
name = "mcp"
version = "1.26.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "anyio" },
    { name = "httpx" },
    { name = "httpx-sse" },
    { name = "jsonschema" },
    { name = "pydantic" },
    { name = "pydantic-settings" },
    { name = "pyjwt", extra = ["crypto"] },
    { name = "python-multipart" },
    { name = "pywin32", marker = "sys_platform == 'win32'" },
    { name = "sse-starlette" },
    { name = "starlette" },
    { name = "typing-extensions" },
    { name = "typing-inspection" },
    { name = "uvicorn", marker = "sys_platform != 'emscripten'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/fc/6d/62e76bbb8144d6ed86e202b5edd8a4cb631e7c8130f3f4893c3f90262b10/mcp-1.26.0.tar.gz", hash = "sha256:db6e2ef491eecc1a0d93711a76f28dec2e05999f93afd48795da1c1137142c66", size = 608005, upload-time = "2026-01-24T19:40:32.468Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/fd/d9/eaa1f80170d2b7c5ba23f3b59f766f3a0bb41155fbc32a69adfa1adaaef9/mcp-1.26.0-py3-none-any.whl", hash = "sha256:904a21c33c25aa98ddbeb47273033c435e595bbacfdb177f4bd87f6dceebe1ca", size = 233615, upload-time = "2026-01-24T19:40:30.652Z" },
]

[[package]]
name = "openai"
version = "2.26.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "anyio" },
    { name = "distro" },
    { name = "httpx" },
    { name = "jiter" },
    { name = "pydantic" },
    { name = "sniffio" },
    { name = "tqdm" },
    { name = "typing-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/d7/91/2a06c4e9597c338cac1e5e5a8dd6f29e1836fc229c4c523529dca387fda8/openai-2.26.0.tar.gz", hash = "sha256:b41f37c140ae0034a6e92b0c509376d907f3a66109935fba2c1b471a7c05a8fb", size = 666702, upload-time = "2026-03-05T23:17:35.874Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/c6/2e/3f73e8ca53718952222cacd0cf7eecc9db439d020f0c1fe7ae717e4e199a/openai-2.26.0-py3-none-any.whl", hash = "sha256:6151bf8f83802f036117f06cc8a57b3a4da60da9926826cc96747888b57f394f", size = 1136409, upload-time = "2026-03-05T23:17:34.072Z" },
]

[[package]]
name = "pycparser"
version = "3.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/1b/7d/92392ff7815c21062bea51aa7b87d45576f649f16458d78b7cf94b9ab2e6/pycparser-3.0.tar.gz", hash = "sha256:600f49d217304a5902ac3c37e1281c9fe94e4d0489de643a9504c5cdfdfc6b29", size = 103492, upload-time = "2026-01-21T14:26:51.89Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/0c/c3/44f3fbbfa403ea2a7c779186dc20772604442dde72947e7d01069cbe98e3/pycparser-3.0-py3-none-any.whl", hash = "sha256:b727414169a36b7d524c1c3e31839a521725078d7b2ff038656844266160a992", size = 48172, upload-time = "2026-01-21T14:26:50.693Z" },
]

[[package]]
name = "pydantic"
version = "2.12.5"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "annotated-types" },
    { name = "pydantic-core" },
    { name = "typing-extensions" },
    { name = "typing-inspection" },
]
sdist = { url = "https://files.pythonhosted.org/packages/69/44/36f1a6e523abc58ae5f928898e4aca2e0ea509b5aa6f6f392a5d882be928/pydantic-2.12.5.tar.gz", hash = "sha256:4d351024c75c0f085a9febbb665ce8c0c6ec5d30e903bdb6394b7ede26aebb49", size = 821591, upload-time = "2025-11-26T15:11:46.471Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/5a/87/b70ad306ebb6f9b585f114d0ac2137d792b48be34d732d60e597c2f8465a/pydantic-2.12.5-py3-none-any.whl", hash = "sha256:e561593fccf61e8a20fc46dfc2dfe075b8be7d0188df33f221ad1f0139180f9d", size = 463580, upload-time = "2025-11-26T15:11:44.605Z" },
]

[[package]]
name = "pydantic-core"
version = "2.41.5"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "typing-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/71/70/23b021c950c2addd24ec408e9ab05d59b035b39d97cdc1130e1bce647bb6/pydantic_core-2.41.5.tar.gz", hash = "sha256:08daa51ea16ad373ffd5e7606252cc32f07bc72b28284b6bc9c6df804816476e", size = 460952, upload-time = "2025-11-04T13:43:49.098Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/87/06/8806241ff1f70d9939f9af039c6c35f2360cf16e93c2ca76f184e76b1564/pydantic_core-2.41.5-cp313-cp313-macosx_10_12_x86_64.whl", hash = "sha256:941103c9be18ac8daf7b7adca8228f8ed6bb7a1849020f643b3a14d15b1924d9", size = 2120403, upload-time = "2025-11-04T13:40:25.248Z" },
    { url = "https://files.pythonhosted.org/packages/94/02/abfa0e0bda67faa65fef1c84971c7e45928e108fe24333c81f3bfe35d5f5/pydantic_core-2.41.5-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:112e305c3314f40c93998e567879e887a3160bb8689ef3d2c04b6cc62c33ac34", size = 1896206, upload-time = "2025-11-04T13:40:27.099Z" },
    { url = "https://files.pythonhosted.org/packages/15/df/a4c740c0943e93e6500f9eb23f4ca7ec9bf71b19e608ae5b579678c8d02f/pydantic_core-2.41.5-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:0cbaad15cb0c90aa221d43c00e77bb33c93e8d36e0bf74760cd00e732d10a6a0", size = 1919307, upload-time = "2025-11-04T13:40:29.806Z" },
    { url = "https://files.pythonhosted.org/packages/9a/e3/6324802931ae1d123528988e0e86587c2072ac2e5394b4bc2bc34b61ff6e/pydantic_core-2.41.5-cp313-cp313-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:03ca43e12fab6023fc79d28ca6b39b05f794ad08ec2feccc59a339b02f2b3d33", size = 2063258, upload-time = "2025-11-04T13:40:33.544Z" },
    { url = "https://files.pythonhosted.org/packages/c9/d4/2230d7151d4957dd79c3044ea26346c148c98fbf0ee6ebd41056f2d62ab5/pydantic_core-2.41.5-cp313-cp313-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:dc799088c08fa04e43144b164feb0c13f9a0bc40503f8df3e9fde58a3c0c101e", size = 2214917, upload-time = "2025-11-04T13:40:35.479Z" },
    { url = "https://files.pythonhosted.org/packages/e6/9f/eaac5df17a3672fef0081b6c1bb0b82b33ee89aa5cec0d7b05f52fd4a1fa/pydantic_core-2.41.5-cp313-cp313-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:97aeba56665b4c3235a0e52b2c2f5ae9cd071b8a8310ad27bddb3f7fb30e9aa2", size = 2332186, upload-time = "2025-11-04T13:40:37.436Z" },
    { url = "https://files.pythonhosted.org/packages/cf/4e/35a80cae583a37cf15604b44240e45c05e04e86f9cfd766623149297e971/pydantic_core-2.41.5-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:406bf18d345822d6c21366031003612b9c77b3e29ffdb0f612367352aab7d586", size = 2073164, upload-time = "2025-11-04T13:40:40.289Z" },
    { url = "https://files.pythonhosted.org/packages/bf/e3/f6e262673c6140dd3305d144d032f7bd5f7497d3871c1428521f19f9efa2/pydantic_core-2.41.5-cp313-cp313-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:b93590ae81f7010dbe380cdeab6f515902ebcbefe0b9327cc4804d74e93ae69d", size = 2179146, upload-time = "2025-11-04T13:40:42.809Z" },
    { url = "https://files.pythonhosted.org/packages/75/c7/20bd7fc05f0c6ea2056a4565c6f36f8968c0924f19b7d97bbfea55780e73/pydantic_core-2.41.5-cp313-cp313-musllinux_1_1_aarch64.whl", hash = "sha256:01a3d0ab748ee531f4ea6c3e48ad9dac84ddba4b0d82291f87248f2f9de8d740", size = 2137788, upload-time = "2025-11-04T13:40:44.752Z" },
    { url = "https://files.pythonhosted.org/packages/3a/8d/34318ef985c45196e004bc46c6eab2eda437e744c124ef0dbe1ff2c9d06b/pydantic_core-2.41.5-cp313-cp313-musllinux_1_1_armv7l.whl", hash = "sha256:6561e94ba9dacc9c61bce40e2d6bdc3bfaa0259d3ff36ace3b1e6901936d2e3e", size = 2340133, upload-time = "2025-11-04T13:40:46.66Z" },
    { url = "https://files.pythonhosted.org/packages/9c/59/013626bf8c78a5a5d9350d12e7697d3d4de951a75565496abd40ccd46bee/pydantic_core-2.41.5-cp313-cp313-musllinux_1_1_x86_64.whl", hash = "sha256:915c3d10f81bec3a74fbd4faebe8391013ba61e5a1a8d48c4455b923bdda7858", size = 2324852, upload-time = "2025-11-04T13:40:48.575Z" },
    { url = "https://files.pythonhosted.org/packages/1a/d9/c248c103856f807ef70c18a4f986693a46a8ffe1602e5d361485da502d20/pydantic_core-2.41.5-cp313-cp313-win32.whl", hash = "sha256:650ae77860b45cfa6e2cdafc42618ceafab3a2d9a3811fcfbd3bbf8ac3c40d36", size = 1994679, upload-time = "2025-11-04T13:40:50.619Z" },
    { url = "https://files.pythonhosted.org/packages/9e/8b/341991b158ddab181cff136acd2552c9f35bd30380422a639c0671e99a91/pydantic_core-2.41.5-cp313-cp313-win_amd64.whl", hash = "sha256:79ec52ec461e99e13791ec6508c722742ad745571f234ea6255bed38c6480f11", size = 2019766, upload-time = "2025-11-04T13:40:52.631Z" },
    { url = "https://files.pythonhosted.org/packages/73/7d/f2f9db34af103bea3e09735bb40b021788a5e834c81eedb541991badf8f5/pydantic_core-2.41.5-cp313-cp313-win_arm64.whl", hash = "sha256:3f84d5c1b4ab906093bdc1ff10484838aca54ef08de4afa9de0f5f14d69639cd", size = 1981005, upload-time = "2025-11-04T13:40:54.734Z" },
    { url = "https://files.pythonhosted.org/packages/ea/28/46b7c5c9635ae96ea0fbb779e271a38129df2550f763937659ee6c5dbc65/pydantic_core-2.41.5-cp314-cp314-macosx_10_12_x86_64.whl", hash = "sha256:3f37a19d7ebcdd20b96485056ba9e8b304e27d9904d233d7b1015db320e51f0a", size = 2119622, upload-time = "2025-11-04T13:40:56.68Z" },
    { url = "https://files.pythonhosted.org/packages/74/1a/145646e5687e8d9a1e8d09acb278c8535ebe9e972e1f162ed338a622f193/pydantic_core-2.41.5-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:1d1d9764366c73f996edd17abb6d9d7649a7eb690006ab6adbda117717099b14", size = 1891725, upload-time = "2025-11-04T13:40:58.807Z" },
    { url = "https://files.pythonhosted.org/packages/23/04/e89c29e267b8060b40dca97bfc64a19b2a3cf99018167ea1677d96368273/pydantic_core-2.41.5-cp314-cp314-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:25e1c2af0fce638d5f1988b686f3b3ea8cd7de5f244ca147c777769e798a9cd1", size = 1915040, upload-time = "2025-11-04T13:41:00.853Z" },
    { url = "https://files.pythonhosted.org/packages/84/a3/15a82ac7bd97992a82257f777b3583d3e84bdb06ba6858f745daa2ec8a85/pydantic_core-2.41.5-cp314-cp314-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:506d766a8727beef16b7adaeb8ee6217c64fc813646b424d0804d67c16eddb66", size = 2063691, upload-time = "2025-11-04T13:41:03.504Z" },
    { url = "https://files.pythonhosted.org/packages/74/9b/0046701313c6ef08c0c1cf0e028c67c770a4e1275ca73131563c5f2a310a/pydantic_core-2.41.5-cp314-cp314-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:4819fa52133c9aa3c387b3328f25c1facc356491e6135b459f1de698ff64d869", size = 2213897, upload-time = "2025-11-04T13:41:05.804Z" },
    { url = "https://files.pythonhosted.org/packages/8a/cd/6bac76ecd1b27e75a95ca3a9a559c643b3afcd2dd62086d4b7a32a18b169/pydantic_core-2.41.5-cp314-cp314-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:2b761d210c9ea91feda40d25b4efe82a1707da2ef62901466a42492c028553a2", size = 2333302, upload-time = "2025-11-04T13:41:07.809Z" },
    { url = "https://files.pythonhosted.org/packages/4c/d2/ef2074dc020dd6e109611a8be4449b98cd25e1b9b8a303c2f0fca2f2bcf7/pydantic_core-2.41.5-cp314-cp314-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:22f0fb8c1c583a3b6f24df2470833b40207e907b90c928cc8d3594b76f874375", size = 2064877, upload-time = "2025-11-04T13:41:09.827Z" },
    { url = "https://files.pythonhosted.org/packages/18/66/e9db17a9a763d72f03de903883c057b2592c09509ccfe468187f2a2eef29/pydantic_core-2.41.5-cp314-cp314-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:2782c870e99878c634505236d81e5443092fba820f0373997ff75f90f68cd553", size = 2180680, upload-time = "2025-11-04T13:41:12.379Z" },
    { url = "https://files.pythonhosted.org/packages/d3/9e/3ce66cebb929f3ced22be85d4c2399b8e85b622db77dad36b73c5387f8f8/pydantic_core-2.41.5-cp314-cp314-musllinux_1_1_aarch64.whl", hash = "sha256:0177272f88ab8312479336e1d777f6b124537d47f2123f89cb37e0accea97f90", size = 2138960, upload-time = "2025-11-04T13:41:14.627Z" },
    { url = "https://files.pythonhosted.org/packages/a6/62/205a998f4327d2079326b01abee48e502ea739d174f0a89295c481a2272e/pydantic_core-2.41.5-cp314-cp314-musllinux_1_1_armv7l.whl", hash = "sha256:63510af5e38f8955b8ee5687740d6ebf7c2a0886d15a6d65c32814613681bc07", size = 2339102, upload-time = "2025-11-04T13:41:16.868Z" },
    { url = "https://files.pythonhosted.org/packages/3c/0d/f05e79471e889d74d3d88f5bd20d0ed189ad94c2423d81ff8d0000aab4ff/pydantic_core-2.41.5-cp314-cp314-musllinux_1_1_x86_64.whl", hash = "sha256:e56ba91f47764cc14f1daacd723e3e82d1a89d783f0f5afe9c364b8bb491ccdb", size = 2326039, upload-time = "2025-11-04T13:41:18.934Z" },
    { url = "https://files.pythonhosted.org/packages/ec/e1/e08a6208bb100da7e0c4b288eed624a703f4d129bde2da475721a80cab32/pydantic_core-2.41.5-cp314-cp314-win32.whl", hash = "sha256:aec5cf2fd867b4ff45b9959f8b20ea3993fc93e63c7363fe6851424c8a7e7c23", size = 1995126, upload-time = "2025-11-04T13:41:21.418Z" },
    { url = "https://files.pythonhosted.org/packages/48/5d/56ba7b24e9557f99c9237e29f5c09913c81eeb2f3217e40e922353668092/pydantic_core-2.41.5-cp314-cp314-win_amd64.whl", hash = "sha256:8e7c86f27c585ef37c35e56a96363ab8de4e549a95512445b85c96d3e2f7c1bf", size = 2015489, upload-time = "2025-11-04T13:41:24.076Z" },
    { url = "https://files.pythonhosted.org/packages/4e/bb/f7a190991ec9e3e0ba22e4993d8755bbc4a32925c0b5b42775c03e8148f9/pydantic_core-2.41.5-cp314-cp314-win_arm64.whl", hash = "sha256:e672ba74fbc2dc8eea59fb6d4aed6845e6905fc2a8afe93175d94a83ba2a01a0", size = 1977288, upload-time = "2025-11-04T13:41:26.33Z" },
    { url = "https://files.pythonhosted.org/packages/92/ed/77542d0c51538e32e15afe7899d79efce4b81eee631d99850edc2f5e9349/pydantic_core-2.41.5-cp314-cp314t-macosx_10_12_x86_64.whl", hash = "sha256:8566def80554c3faa0e65ac30ab0932b9e3a5cd7f8323764303d468e5c37595a", size = 2120255, upload-time = "2025-11-04T13:41:28.569Z" },
    { url = "https://files.pythonhosted.org/packages/bb/3d/6913dde84d5be21e284439676168b28d8bbba5600d838b9dca99de0fad71/pydantic_core-2.41.5-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:b80aa5095cd3109962a298ce14110ae16b8c1aece8b72f9dafe81cf597ad80b3", size = 1863760, upload-time = "2025-11-04T13:41:31.055Z" },
    { url = "https://files.pythonhosted.org/packages/5a/f0/e5e6b99d4191da102f2b0eb9687aaa7f5bea5d9964071a84effc3e40f997/pydantic_core-2.41.5-cp314-cp314t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:3006c3dd9ba34b0c094c544c6006cc79e87d8612999f1a5d43b769b89181f23c", size = 1878092, upload-time = "2025-11-04T13:41:33.21Z" },
    { url = "https://files.pythonhosted.org/packages/71/48/36fb760642d568925953bcc8116455513d6e34c4beaa37544118c36aba6d/pydantic_core-2.41.5-cp314-cp314t-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:72f6c8b11857a856bcfa48c86f5368439f74453563f951e473514579d44aa612", size = 2053385, upload-time = "2025-11-04T13:41:35.508Z" },
    { url = "https://files.pythonhosted.org/packages/20/25/92dc684dd8eb75a234bc1c764b4210cf2646479d54b47bf46061657292a8/pydantic_core-2.41.5-cp314-cp314t-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:5cb1b2f9742240e4bb26b652a5aeb840aa4b417c7748b6f8387927bc6e45e40d", size = 2218832, upload-time = "2025-11-04T13:41:37.732Z" },
    { url = "https://files.pythonhosted.org/packages/e2/09/f53e0b05023d3e30357d82eb35835d0f6340ca344720a4599cd663dca599/pydantic_core-2.41.5-cp314-cp314t-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:bd3d54f38609ff308209bd43acea66061494157703364ae40c951f83ba99a1a9", size = 2327585, upload-time = "2025-11-04T13:41:40Z" },
    { url = "https://files.pythonhosted.org/packages/aa/4e/2ae1aa85d6af35a39b236b1b1641de73f5a6ac4d5a7509f77b814885760c/pydantic_core-2.41.5-cp314-cp314t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:2ff4321e56e879ee8d2a879501c8e469414d948f4aba74a2d4593184eb326660", size = 2041078, upload-time = "2025-11-04T13:41:42.323Z" },
    { url = "https://files.pythonhosted.org/packages/cd/13/2e215f17f0ef326fc72afe94776edb77525142c693767fc347ed6288728d/pydantic_core-2.41.5-cp314-cp314t-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:d0d2568a8c11bf8225044aa94409e21da0cb09dcdafe9ecd10250b2baad531a9", size = 2173914, upload-time = "2025-11-04T13:41:45.221Z" },
    { url = "https://files.pythonhosted.org/packages/02/7a/f999a6dcbcd0e5660bc348a3991c8915ce6599f4f2c6ac22f01d7a10816c/pydantic_core-2.41.5-cp314-cp314t-musllinux_1_1_aarch64.whl", hash = "sha256:a39455728aabd58ceabb03c90e12f71fd30fa69615760a075b9fec596456ccc3", size = 2129560, upload-time = "2025-11-04T13:41:47.474Z" },
    { url = "https://files.pythonhosted.org/packages/3a/b1/6c990ac65e3b4c079a4fb9f5b05f5b013afa0f4ed6780a3dd236d2cbdc64/pydantic_core-2.41.5-cp314-cp314t-musllinux_1_1_armv7l.whl", hash = "sha256:239edca560d05757817c13dc17c50766136d21f7cd0fac50295499ae24f90fdf", size = 2329244, upload-time = "2025-11-04T13:41:49.992Z" },
    { url = "https://files.pythonhosted.org/packages/d9/02/3c562f3a51afd4d88fff8dffb1771b30cfdfd79befd9883ee094f5b6c0d8/pydantic_core-2.41.5-cp314-cp314t-musllinux_1_1_x86_64.whl", hash = "sha256:2a5e06546e19f24c6a96a129142a75cee553cc018ffee48a460059b1185f4470", size = 2331955, upload-time = "2025-11-04T13:41:54.079Z" },
    { url = "https://files.pythonhosted.org/packages/5c/96/5fb7d8c3c17bc8c62fdb031c47d77a1af698f1d7a406b0f79aaa1338f9ad/pydantic_core-2.41.5-cp314-cp314t-win32.whl", hash = "sha256:b4ececa40ac28afa90871c2cc2b9ffd2ff0bf749380fbdf57d165fd23da353aa", size = 1988906, upload-time = "2025-11-04T13:41:56.606Z" },
    { url = "https://files.pythonhosted.org/packages/22/ed/182129d83032702912c2e2d8bbe33c036f342cc735737064668585dac28f/pydantic_core-2.41.5-cp314-cp314t-win_amd64.whl", hash = "sha256:80aa89cad80b32a912a65332f64a4450ed00966111b6615ca6816153d3585a8c", size = 1981607, upload-time = "2025-11-04T13:41:58.889Z" },
    { url = "https://files.pythonhosted.org/packages/9f/ed/068e41660b832bb0b1aa5b58011dea2a3fe0ba7861ff38c4d4904c1c1a99/pydantic_core-2.41.5-cp314-cp314t-win_arm64.whl", hash = "sha256:35b44f37a3199f771c3eaa53051bc8a70cd7b54f333531c59e29fd4db5d15008", size = 1974769, upload-time = "2025-11-04T13:42:01.186Z" },
]

[[package]]
name = "pydantic-settings"
version = "2.13.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "pydantic" },
    { name = "python-dotenv" },
    { name = "typing-inspection" },
]
sdist = { url = "https://files.pythonhosted.org/packages/52/6d/fffca34caecc4a3f97bda81b2098da5e8ab7efc9a66e819074a11955d87e/pydantic_settings-2.13.1.tar.gz", hash = "sha256:b4c11847b15237fb0171e1462bf540e294affb9b86db4d9aa5c01730bdbe4025", size = 223826, upload-time = "2026-02-19T13:45:08.055Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/00/4b/ccc026168948fec4f7555b9164c724cf4125eac006e176541483d2c959be/pydantic_settings-2.13.1-py3-none-any.whl", hash = "sha256:d56fd801823dbeae7f0975e1f8c8e25c258eb75d278ea7abb5d9cebb01b56237", size = 58929, upload-time = "2026-02-19T13:45:06.034Z" },
]

[[package]]
name = "pyjwt"
version = "2.11.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/5c/5a/b46fa56bf322901eee5b0454a34343cdbdae202cd421775a8ee4e42fd519/pyjwt-2.11.0.tar.gz", hash = "sha256:35f95c1f0fbe5d5ba6e43f00271c275f7a1a4db1dab27bf708073b75318ea623", size = 98019, upload-time = "2026-01-30T19:59:55.694Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/6f/01/c26ce75ba460d5cd503da9e13b21a33804d38c2165dec7b716d06b13010c/pyjwt-2.11.0-py3-none-any.whl", hash = "sha256:94a6bde30eb5c8e04fee991062b534071fd1439ef58d2adc9ccb823e7bcd0469", size = 28224, upload-time = "2026-01-30T19:59:54.539Z" },
]

[package.optional-dependencies]
crypto = [
    { name = "cryptography" },
]

[[package]]
name = "python-dotenv"
version = "1.2.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/82/ed/0301aeeac3e5353ef3d94b6ec08bbcabd04a72018415dcb29e588514bba8/python_dotenv-1.2.2.tar.gz", hash = "sha256:2c371a91fbd7ba082c2c1dc1f8bf89ca22564a087c2c287cd9b662adde799cf3", size = 50135, upload-time = "2026-03-01T16:00:26.196Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/0b/d7/1959b9648791274998a9c3526f6d0ec8fd2233e4d4acce81bbae76b44b2a/python_dotenv-1.2.2-py3-none-any.whl", hash = "sha256:1d8214789a24de455a8b8bd8ae6fe3c6b69a5e3d64aa8a8e5d68e694bbcb285a", size = 22101, upload-time = "2026-03-01T16:00:25.09Z" },
]

[[package]]
name = "python-multipart"
version = "0.0.22"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/94/01/979e98d542a70714b0cb2b6728ed0b7c46792b695e3eaec3e20711271ca3/python_multipart-0.0.22.tar.gz", hash = "sha256:7340bef99a7e0032613f56dc36027b959fd3b30a787ed62d310e951f7c3a3a58", size = 37612, upload-time = "2026-01-25T10:15:56.219Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/1b/d0/397f9626e711ff749a95d96b7af99b9c566a9bb5129b8e4c10fc4d100304/python_multipart-0.0.22-py3-none-any.whl", hash = "sha256:2b2cd894c83d21bf49d702499531c7bafd057d730c201782048f7945d82de155", size = 24579, upload-time = "2026-01-25T10:15:54.811Z" },
]

[[package]]
name = "pywin32"
version = "311"
source = { registry = "https://pypi.org/simple" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/a5/be/3fd5de0979fcb3994bfee0d65ed8ca9506a8a1260651b86174f6a86f52b3/pywin32-311-cp313-cp313-win32.whl", hash = "sha256:f95ba5a847cba10dd8c4d8fefa9f2a6cf283b8b88ed6178fa8a6c1ab16054d0d", size = 8705700, upload-time = "2025-07-14T20:13:26.471Z" },
    { url = "https://files.pythonhosted.org/packages/e3/28/e0a1909523c6890208295a29e05c2adb2126364e289826c0a8bc7297bd5c/pywin32-311-cp313-cp313-win_amd64.whl", hash = "sha256:718a38f7e5b058e76aee1c56ddd06908116d35147e133427e59a3983f703a20d", size = 9494700, upload-time = "2025-07-14T20:13:28.243Z" },
    { url = "https://files.pythonhosted.org/packages/04/bf/90339ac0f55726dce7d794e6d79a18a91265bdf3aa70b6b9ca52f35e022a/pywin32-311-cp313-cp313-win_arm64.whl", hash = "sha256:7b4075d959648406202d92a2310cb990fea19b535c7f4a78d3f5e10b926eeb8a", size = 8709318, upload-time = "2025-07-14T20:13:30.348Z" },
    { url = "https://files.pythonhosted.org/packages/c9/31/097f2e132c4f16d99a22bfb777e0fd88bd8e1c634304e102f313af69ace5/pywin32-311-cp314-cp314-win32.whl", hash = "sha256:b7a2c10b93f8986666d0c803ee19b5990885872a7de910fc460f9b0c2fbf92ee", size = 8840714, upload-time = "2025-07-14T20:13:32.449Z" },
    { url = "https://files.pythonhosted.org/packages/90/4b/07c77d8ba0e01349358082713400435347df8426208171ce297da32c313d/pywin32-311-cp314-cp314-win_amd64.whl", hash = "sha256:3aca44c046bd2ed8c90de9cb8427f581c479e594e99b5c0bb19b29c10fd6cb87", size = 9656800, upload-time = "2025-07-14T20:13:34.312Z" },
    { url = "https://files.pythonhosted.org/packages/c0/d2/21af5c535501a7233e734b8af901574572da66fcc254cb35d0609c9080dd/pywin32-311-cp314-cp314-win_arm64.whl", hash = "sha256:a508e2d9025764a8270f93111a970e1d0fbfc33f4153b388bb649b7eec4f9b42", size = 8932540, upload-time = "2025-07-14T20:13:36.379Z" },
]

[[package]]
name = "referencing"
version = "0.37.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "attrs" },
    { name = "rpds-py" },
]
sdist = { url = "https://files.pythonhosted.org/packages/22/f5/df4e9027acead3ecc63e50fe1e36aca1523e1719559c499951bb4b53188f/referencing-0.37.0.tar.gz", hash = "sha256:44aefc3142c5b842538163acb373e24cce6632bd54bdb01b21ad5863489f50d8", size = 78036, upload-time = "2025-10-13T15:30:48.871Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/2c/58/ca301544e1fa93ed4f80d724bf5b194f6e4b945841c5bfd555878eea9fcb/referencing-0.37.0-py3-none-any.whl", hash = "sha256:381329a9f99628c9069361716891d34ad94af76e461dcb0335825aecc7692231", size = 26766, upload-time = "2025-10-13T15:30:47.625Z" },
]

[[package]]
name = "rpds-py"
version = "0.30.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/20/af/3f2f423103f1113b36230496629986e0ef7e199d2aa8392452b484b38ced/rpds_py-0.30.0.tar.gz", hash = "sha256:dd8ff7cf90014af0c0f787eea34794ebf6415242ee1d6fa91eaba725cc441e84", size = 69469, upload-time = "2025-11-30T20:24:38.837Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/ed/dc/d61221eb88ff410de3c49143407f6f3147acf2538c86f2ab7ce65ae7d5f9/rpds_py-0.30.0-cp313-cp313-macosx_10_12_x86_64.whl", hash = "sha256:f83424d738204d9770830d35290ff3273fbb02b41f919870479fab14b9d303b2", size = 374887, upload-time = "2025-11-30T20:22:41.812Z" },
    { url = "https://files.pythonhosted.org/packages/fd/32/55fb50ae104061dbc564ef15cc43c013dc4a9f4527a1f4d99baddf56fe5f/rpds_py-0.30.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:e7536cd91353c5273434b4e003cbda89034d67e7710eab8761fd918ec6c69cf8", size = 358904, upload-time = "2025-11-30T20:22:43.479Z" },
    { url = "https://files.pythonhosted.org/packages/58/70/faed8186300e3b9bdd138d0273109784eea2396c68458ed580f885dfe7ad/rpds_py-0.30.0-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:2771c6c15973347f50fece41fc447c054b7ac2ae0502388ce3b6738cd366e3d4", size = 389945, upload-time = "2025-11-30T20:22:44.819Z" },
    { url = "https://files.pythonhosted.org/packages/bd/a8/073cac3ed2c6387df38f71296d002ab43496a96b92c823e76f46b8af0543/rpds_py-0.30.0-cp313-cp313-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:0a59119fc6e3f460315fe9d08149f8102aa322299deaa5cab5b40092345c2136", size = 407783, upload-time = "2025-11-30T20:22:46.103Z" },
    { url = "https://files.pythonhosted.org/packages/77/57/5999eb8c58671f1c11eba084115e77a8899d6e694d2a18f69f0ba471ec8b/rpds_py-0.30.0-cp313-cp313-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:76fec018282b4ead0364022e3c54b60bf368b9d926877957a8624b58419169b7", size = 515021, upload-time = "2025-11-30T20:22:47.458Z" },
    { url = "https://files.pythonhosted.org/packages/e0/af/5ab4833eadc36c0a8ed2bc5c0de0493c04f6c06de223170bd0798ff98ced/rpds_py-0.30.0-cp313-cp313-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:692bef75a5525db97318e8cd061542b5a79812d711ea03dbc1f6f8dbb0c5f0d2", size = 414589, upload-time = "2025-11-30T20:22:48.872Z" },
    { url = "https://files.pythonhosted.org/packages/b7/de/f7192e12b21b9e9a68a6d0f249b4af3fdcdff8418be0767a627564afa1f1/rpds_py-0.30.0-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:9027da1ce107104c50c81383cae773ef5c24d296dd11c99e2629dbd7967a20c6", size = 394025, upload-time = "2025-11-30T20:22:50.196Z" },
    { url = "https://files.pythonhosted.org/packages/91/c4/fc70cd0249496493500e7cc2de87504f5aa6509de1e88623431fec76d4b6/rpds_py-0.30.0-cp313-cp313-manylinux_2_31_riscv64.whl", hash = "sha256:9cf69cdda1f5968a30a359aba2f7f9aa648a9ce4b580d6826437f2b291cfc86e", size = 408895, upload-time = "2025-11-30T20:22:51.87Z" },
    { url = "https://files.pythonhosted.org/packages/58/95/d9275b05ab96556fefff73a385813eb66032e4c99f411d0795372d9abcea/rpds_py-0.30.0-cp313-cp313-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:a4796a717bf12b9da9d3ad002519a86063dcac8988b030e405704ef7d74d2d9d", size = 422799, upload-time = "2025-11-30T20:22:53.341Z" },
    { url = "https://files.pythonhosted.org/packages/06/c1/3088fc04b6624eb12a57eb814f0d4997a44b0d208d6cace713033ff1a6ba/rpds_py-0.30.0-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:5d4c2aa7c50ad4728a094ebd5eb46c452e9cb7edbfdb18f9e1221f597a73e1e7", size = 572731, upload-time = "2025-11-30T20:22:54.778Z" },
    { url = "https://files.pythonhosted.org/packages/d8/42/c612a833183b39774e8ac8fecae81263a68b9583ee343db33ab571a7ce55/rpds_py-0.30.0-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:ba81a9203d07805435eb06f536d95a266c21e5b2dfbf6517748ca40c98d19e31", size = 599027, upload-time = "2025-11-30T20:22:56.212Z" },
    { url = "https://files.pythonhosted.org/packages/5f/60/525a50f45b01d70005403ae0e25f43c0384369ad24ffe46e8d9068b50086/rpds_py-0.30.0-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:945dccface01af02675628334f7cf49c2af4c1c904748efc5cf7bbdf0b579f95", size = 563020, upload-time = "2025-11-30T20:22:58.2Z" },
    { url = "https://files.pythonhosted.org/packages/0b/5d/47c4655e9bcd5ca907148535c10e7d489044243cc9941c16ed7cd53be91d/rpds_py-0.30.0-cp313-cp313-win32.whl", hash = "sha256:b40fb160a2db369a194cb27943582b38f79fc4887291417685f3ad693c5a1d5d", size = 223139, upload-time = "2025-11-30T20:23:00.209Z" },
    { url = "https://files.pythonhosted.org/packages/f2/e1/485132437d20aa4d3e1d8b3fb5a5e65aa8139f1e097080c2a8443201742c/rpds_py-0.30.0-cp313-cp313-win_amd64.whl", hash = "sha256:806f36b1b605e2d6a72716f321f20036b9489d29c51c91f4dd29a3e3afb73b15", size = 240224, upload-time = "2025-11-30T20:23:02.008Z" },
    { url = "https://files.pythonhosted.org/packages/24/95/ffd128ed1146a153d928617b0ef673960130be0009c77d8fbf0abe306713/rpds_py-0.30.0-cp313-cp313-win_arm64.whl", hash = "sha256:d96c2086587c7c30d44f31f42eae4eac89b60dabbac18c7669be3700f13c3ce1", size = 230645, upload-time = "2025-11-30T20:23:03.43Z" },
    { url = "https://files.pythonhosted.org/packages/ff/1b/b10de890a0def2a319a2626334a7f0ae388215eb60914dbac8a3bae54435/rpds_py-0.30.0-cp313-cp313t-macosx_10_12_x86_64.whl", hash = "sha256:eb0b93f2e5c2189ee831ee43f156ed34e2a89a78a66b98cadad955972548be5a", size = 364443, upload-time = "2025-11-30T20:23:04.878Z" },
    { url = "https://files.pythonhosted.org/packages/0d/bf/27e39f5971dc4f305a4fb9c672ca06f290f7c4e261c568f3dea16a410d47/rpds_py-0.30.0-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:922e10f31f303c7c920da8981051ff6d8c1a56207dbdf330d9047f6d30b70e5e", size = 353375, upload-time = "2025-11-30T20:23:06.342Z" },
    { url = "https://files.pythonhosted.org/packages/40/58/442ada3bba6e8e6615fc00483135c14a7538d2ffac30e2d933ccf6852232/rpds_py-0.30.0-cp313-cp313t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:cdc62c8286ba9bf7f47befdcea13ea0e26bf294bda99758fd90535cbaf408000", size = 383850, upload-time = "2025-11-30T20:23:07.825Z" },
    { url = "https://files.pythonhosted.org/packages/14/14/f59b0127409a33c6ef6f5c1ebd5ad8e32d7861c9c7adfa9a624fc3889f6c/rpds_py-0.30.0-cp313-cp313t-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:47f9a91efc418b54fb8190a6b4aa7813a23fb79c51f4bb84e418f5476c38b8db", size = 392812, upload-time = "2025-11-30T20:23:09.228Z" },
    { url = "https://files.pythonhosted.org/packages/b3/66/e0be3e162ac299b3a22527e8913767d869e6cc75c46bd844aa43fb81ab62/rpds_py-0.30.0-cp313-cp313t-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:1f3587eb9b17f3789ad50824084fa6f81921bbf9a795826570bda82cb3ed91f2", size = 517841, upload-time = "2025-11-30T20:23:11.186Z" },
    { url = "https://files.pythonhosted.org/packages/3d/55/fa3b9cf31d0c963ecf1ba777f7cf4b2a2c976795ac430d24a1f43d25a6ba/rpds_py-0.30.0-cp313-cp313t-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:39c02563fc592411c2c61d26b6c5fe1e51eaa44a75aa2c8735ca88b0d9599daa", size = 408149, upload-time = "2025-11-30T20:23:12.864Z" },
    { url = "https://files.pythonhosted.org/packages/60/ca/780cf3b1a32b18c0f05c441958d3758f02544f1d613abf9488cd78876378/rpds_py-0.30.0-cp313-cp313t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:51a1234d8febafdfd33a42d97da7a43f5dcb120c1060e352a3fbc0c6d36e2083", size = 383843, upload-time = "2025-11-30T20:23:14.638Z" },
    { url = "https://files.pythonhosted.org/packages/82/86/d5f2e04f2aa6247c613da0c1dd87fcd08fa17107e858193566048a1e2f0a/rpds_py-0.30.0-cp313-cp313t-manylinux_2_31_riscv64.whl", hash = "sha256:eb2c4071ab598733724c08221091e8d80e89064cd472819285a9ab0f24bcedb9", size = 396507, upload-time = "2025-11-30T20:23:16.105Z" },
    { url = "https://files.pythonhosted.org/packages/4b/9a/453255d2f769fe44e07ea9785c8347edaf867f7026872e76c1ad9f7bed92/rpds_py-0.30.0-cp313-cp313t-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:6bdfdb946967d816e6adf9a3d8201bfad269c67efe6cefd7093ef959683c8de0", size = 414949, upload-time = "2025-11-30T20:23:17.539Z" },
    { url = "https://files.pythonhosted.org/packages/a3/31/622a86cdc0c45d6df0e9ccb6becdba5074735e7033c20e401a6d9d0e2ca0/rpds_py-0.30.0-cp313-cp313t-musllinux_1_2_aarch64.whl", hash = "sha256:c77afbd5f5250bf27bf516c7c4a016813eb2d3e116139aed0096940c5982da94", size = 565790, upload-time = "2025-11-30T20:23:19.029Z" },
    { url = "https://files.pythonhosted.org/packages/1c/5d/15bbf0fb4a3f58a3b1c67855ec1efcc4ceaef4e86644665fff03e1b66d8d/rpds_py-0.30.0-cp313-cp313t-musllinux_1_2_i686.whl", hash = "sha256:61046904275472a76c8c90c9ccee9013d70a6d0f73eecefd38c1ae7c39045a08", size = 590217, upload-time = "2025-11-30T20:23:20.885Z" },
    { url = "https://files.pythonhosted.org/packages/6d/61/21b8c41f68e60c8cc3b2e25644f0e3681926020f11d06ab0b78e3c6bbff1/rpds_py-0.30.0-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:4c5f36a861bc4b7da6516dbdf302c55313afa09b81931e8280361a4f6c9a2d27", size = 555806, upload-time = "2025-11-30T20:23:22.488Z" },
    { url = "https://files.pythonhosted.org/packages/f9/39/7e067bb06c31de48de3eb200f9fc7c58982a4d3db44b07e73963e10d3be9/rpds_py-0.30.0-cp313-cp313t-win32.whl", hash = "sha256:3d4a69de7a3e50ffc214ae16d79d8fbb0922972da0356dcf4d0fdca2878559c6", size = 211341, upload-time = "2025-11-30T20:23:24.449Z" },
    { url = "https://files.pythonhosted.org/packages/0a/4d/222ef0b46443cf4cf46764d9c630f3fe4abaa7245be9417e56e9f52b8f65/rpds_py-0.30.0-cp313-cp313t-win_amd64.whl", hash = "sha256:f14fc5df50a716f7ece6a80b6c78bb35ea2ca47c499e422aa4463455dd96d56d", size = 225768, upload-time = "2025-11-30T20:23:25.908Z" },
    { url = "https://files.pythonhosted.org/packages/86/81/dad16382ebbd3d0e0328776d8fd7ca94220e4fa0798d1dc5e7da48cb3201/rpds_py-0.30.0-cp314-cp314-macosx_10_12_x86_64.whl", hash = "sha256:68f19c879420aa08f61203801423f6cd5ac5f0ac4ac82a2368a9fcd6a9a075e0", size = 362099, upload-time = "2025-11-30T20:23:27.316Z" },
    { url = "https://files.pythonhosted.org/packages/2b/60/19f7884db5d5603edf3c6bce35408f45ad3e97e10007df0e17dd57af18f8/rpds_py-0.30.0-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:ec7c4490c672c1a0389d319b3a9cfcd098dcdc4783991553c332a15acf7249be", size = 353192, upload-time = "2025-11-30T20:23:29.151Z" },
    { url = "https://files.pythonhosted.org/packages/bf/c4/76eb0e1e72d1a9c4703c69607cec123c29028bff28ce41588792417098ac/rpds_py-0.30.0-cp314-cp314-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:f251c812357a3fed308d684a5079ddfb9d933860fc6de89f2b7ab00da481e65f", size = 384080, upload-time = "2025-11-30T20:23:30.785Z" },
    { url = "https://files.pythonhosted.org/packages/72/87/87ea665e92f3298d1b26d78814721dc39ed8d2c74b86e83348d6b48a6f31/rpds_py-0.30.0-cp314-cp314-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:ac98b175585ecf4c0348fd7b29c3864bda53b805c773cbf7bfdaffc8070c976f", size = 394841, upload-time = "2025-11-30T20:23:32.209Z" },
    { url = "https://files.pythonhosted.org/packages/77/ad/7783a89ca0587c15dcbf139b4a8364a872a25f861bdb88ed99f9b0dec985/rpds_py-0.30.0-cp314-cp314-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:3e62880792319dbeb7eb866547f2e35973289e7d5696c6e295476448f5b63c87", size = 516670, upload-time = "2025-11-30T20:23:33.742Z" },
    { url = "https://files.pythonhosted.org/packages/5b/3c/2882bdac942bd2172f3da574eab16f309ae10a3925644e969536553cb4ee/rpds_py-0.30.0-cp314-cp314-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:4e7fc54e0900ab35d041b0601431b0a0eb495f0851a0639b6ef90f7741b39a18", size = 408005, upload-time = "2025-11-30T20:23:35.253Z" },
    { url = "https://files.pythonhosted.org/packages/ce/81/9a91c0111ce1758c92516a3e44776920b579d9a7c09b2b06b642d4de3f0f/rpds_py-0.30.0-cp314-cp314-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:47e77dc9822d3ad616c3d5759ea5631a75e5809d5a28707744ef79d7a1bcfcad", size = 382112, upload-time = "2025-11-30T20:23:36.842Z" },
    { url = "https://files.pythonhosted.org/packages/cf/8e/1da49d4a107027e5fbc64daeab96a0706361a2918da10cb41769244b805d/rpds_py-0.30.0-cp314-cp314-manylinux_2_31_riscv64.whl", hash = "sha256:b4dc1a6ff022ff85ecafef7979a2c6eb423430e05f1165d6688234e62ba99a07", size = 399049, upload-time = "2025-11-30T20:23:38.343Z" },
    { url = "https://files.pythonhosted.org/packages/df/5a/7ee239b1aa48a127570ec03becbb29c9d5a9eb092febbd1699d567cae859/rpds_py-0.30.0-cp314-cp314-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:4559c972db3a360808309e06a74628b95eaccbf961c335c8fe0d590cf587456f", size = 415661, upload-time = "2025-11-30T20:23:40.263Z" },
    { url = "https://files.pythonhosted.org/packages/70/ea/caa143cf6b772f823bc7929a45da1fa83569ee49b11d18d0ada7f5ee6fd6/rpds_py-0.30.0-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:0ed177ed9bded28f8deb6ab40c183cd1192aa0de40c12f38be4d59cd33cb5c65", size = 565606, upload-time = "2025-11-30T20:23:42.186Z" },
    { url = "https://files.pythonhosted.org/packages/64/91/ac20ba2d69303f961ad8cf55bf7dbdb4763f627291ba3d0d7d67333cced9/rpds_py-0.30.0-cp314-cp314-musllinux_1_2_i686.whl", hash = "sha256:ad1fa8db769b76ea911cb4e10f049d80bf518c104f15b3edb2371cc65375c46f", size = 591126, upload-time = "2025-11-30T20:23:44.086Z" },
    { url = "https://files.pythonhosted.org/packages/21/20/7ff5f3c8b00c8a95f75985128c26ba44503fb35b8e0259d812766ea966c7/rpds_py-0.30.0-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:46e83c697b1f1c72b50e5ee5adb4353eef7406fb3f2043d64c33f20ad1c2fc53", size = 553371, upload-time = "2025-11-30T20:23:46.004Z" },
    { url = "https://files.pythonhosted.org/packages/72/c7/81dadd7b27c8ee391c132a6b192111ca58d866577ce2d9b0ca157552cce0/rpds_py-0.30.0-cp314-cp314-win32.whl", hash = "sha256:ee454b2a007d57363c2dfd5b6ca4a5d7e2c518938f8ed3b706e37e5d470801ed", size = 215298, upload-time = "2025-11-30T20:23:47.696Z" },
    { url = "https://files.pythonhosted.org/packages/3e/d2/1aaac33287e8cfb07aab2e6b8ac1deca62f6f65411344f1433c55e6f3eb8/rpds_py-0.30.0-cp314-cp314-win_amd64.whl", hash = "sha256:95f0802447ac2d10bcc69f6dc28fe95fdf17940367b21d34e34c737870758950", size = 228604, upload-time = "2025-11-30T20:23:49.501Z" },
    { url = "https://files.pythonhosted.org/packages/e8/95/ab005315818cc519ad074cb7784dae60d939163108bd2b394e60dc7b5461/rpds_py-0.30.0-cp314-cp314-win_arm64.whl", hash = "sha256:613aa4771c99f03346e54c3f038e4cc574ac09a3ddfb0e8878487335e96dead6", size = 222391, upload-time = "2025-11-30T20:23:50.96Z" },
    { url = "https://files.pythonhosted.org/packages/9e/68/154fe0194d83b973cdedcdcc88947a2752411165930182ae41d983dcefa6/rpds_py-0.30.0-cp314-cp314t-macosx_10_12_x86_64.whl", hash = "sha256:7e6ecfcb62edfd632e56983964e6884851786443739dbfe3582947e87274f7cb", size = 364868, upload-time = "2025-11-30T20:23:52.494Z" },
    { url = "https://files.pythonhosted.org/packages/83/69/8bbc8b07ec854d92a8b75668c24d2abcb1719ebf890f5604c61c9369a16f/rpds_py-0.30.0-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:a1d0bc22a7cdc173fedebb73ef81e07faef93692b8c1ad3733b67e31e1b6e1b8", size = 353747, upload-time = "2025-11-30T20:23:54.036Z" },
    { url = "https://files.pythonhosted.org/packages/ab/00/ba2e50183dbd9abcce9497fa5149c62b4ff3e22d338a30d690f9af970561/rpds_py-0.30.0-cp314-cp314t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:0d08f00679177226c4cb8c5265012eea897c8ca3b93f429e546600c971bcbae7", size = 383795, upload-time = "2025-11-30T20:23:55.556Z" },
    { url = "https://files.pythonhosted.org/packages/05/6f/86f0272b84926bcb0e4c972262f54223e8ecc556b3224d281e6598fc9268/rpds_py-0.30.0-cp314-cp314t-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:5965af57d5848192c13534f90f9dd16464f3c37aaf166cc1da1cae1fd5a34898", size = 393330, upload-time = "2025-11-30T20:23:57.033Z" },
    { url = "https://files.pythonhosted.org/packages/cb/e9/0e02bb2e6dc63d212641da45df2b0bf29699d01715913e0d0f017ee29438/rpds_py-0.30.0-cp314-cp314t-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:9a4e86e34e9ab6b667c27f3211ca48f73dba7cd3d90f8d5b11be56e5dbc3fb4e", size = 518194, upload-time = "2025-11-30T20:23:58.637Z" },
    { url = "https://files.pythonhosted.org/packages/ee/ca/be7bca14cf21513bdf9c0606aba17d1f389ea2b6987035eb4f62bd923f25/rpds_py-0.30.0-cp314-cp314t-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:e5d3e6b26f2c785d65cc25ef1e5267ccbe1b069c5c21b8cc724efee290554419", size = 408340, upload-time = "2025-11-30T20:24:00.2Z" },
    { url = "https://files.pythonhosted.org/packages/c2/c7/736e00ebf39ed81d75544c0da6ef7b0998f8201b369acf842f9a90dc8fce/rpds_py-0.30.0-cp314-cp314t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:626a7433c34566535b6e56a1b39a7b17ba961e97ce3b80ec62e6f1312c025551", size = 383765, upload-time = "2025-11-30T20:24:01.759Z" },
    { url = "https://files.pythonhosted.org/packages/4a/3f/da50dfde9956aaf365c4adc9533b100008ed31aea635f2b8d7b627e25b49/rpds_py-0.30.0-cp314-cp314t-manylinux_2_31_riscv64.whl", hash = "sha256:acd7eb3f4471577b9b5a41baf02a978e8bdeb08b4b355273994f8b87032000a8", size = 396834, upload-time = "2025-11-30T20:24:03.687Z" },
    { url = "https://files.pythonhosted.org/packages/4e/00/34bcc2565b6020eab2623349efbdec810676ad571995911f1abdae62a3a0/rpds_py-0.30.0-cp314-cp314t-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:fe5fa731a1fa8a0a56b0977413f8cacac1768dad38d16b3a296712709476fbd5", size = 415470, upload-time = "2025-11-30T20:24:05.232Z" },
    { url = "https://files.pythonhosted.org/packages/8c/28/882e72b5b3e6f718d5453bd4d0d9cf8df36fddeb4ddbbab17869d5868616/rpds_py-0.30.0-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:74a3243a411126362712ee1524dfc90c650a503502f135d54d1b352bd01f2404", size = 565630, upload-time = "2025-11-30T20:24:06.878Z" },
    { url = "https://files.pythonhosted.org/packages/3b/97/04a65539c17692de5b85c6e293520fd01317fd878ea1995f0367d4532fb1/rpds_py-0.30.0-cp314-cp314t-musllinux_1_2_i686.whl", hash = "sha256:3e8eeb0544f2eb0d2581774be4c3410356eba189529a6b3e36bbbf9696175856", size = 591148, upload-time = "2025-11-30T20:24:08.445Z" },
    { url = "https://files.pythonhosted.org/packages/85/70/92482ccffb96f5441aab93e26c4d66489eb599efdcf96fad90c14bbfb976/rpds_py-0.30.0-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:dbd936cde57abfee19ab3213cf9c26be06d60750e60a8e4dd85d1ab12c8b1f40", size = 556030, upload-time = "2025-11-30T20:24:10.956Z" },
    { url = "https://files.pythonhosted.org/packages/20/53/7c7e784abfa500a2b6b583b147ee4bb5a2b3747a9166bab52fec4b5b5e7d/rpds_py-0.30.0-cp314-cp314t-win32.whl", hash = "sha256:dc824125c72246d924f7f796b4f63c1e9dc810c7d9e2355864b3c3a73d59ade0", size = 211570, upload-time = "2025-11-30T20:24:12.735Z" },
    { url = "https://files.pythonhosted.org/packages/d0/02/fa464cdfbe6b26e0600b62c528b72d8608f5cc49f96b8d6e38c95d60c676/rpds_py-0.30.0-cp314-cp314t-win_amd64.whl", hash = "sha256:27f4b0e92de5bfbc6f86e43959e6edd1425c33b5e69aab0984a72047f2bcf1e3", size = 226532, upload-time = "2025-11-30T20:24:14.634Z" },
]

[[package]]
name = "sniffio"
version = "1.3.1"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/a2/87/a6771e1546d97e7e041b6ae58d80074f81b7d5121207425c964ddf5cfdbd/sniffio-1.3.1.tar.gz", hash = "sha256:f4324edc670a0f49750a81b895f35c3adb843cca46f0530f79fc1babb23789dc", size = 20372, upload-time = "2024-02-25T23:20:04.057Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/e9/44/75a9c9421471a6c4805dbf2356f7c181a29c1879239abab1ea2cc8f38b40/sniffio-1.3.1-py3-none-any.whl", hash = "sha256:2f6da418d1f1e0fddd844478f41680e794e6051915791a034ff65e5f100525a2", size = 10235, upload-time = "2024-02-25T23:20:01.196Z" },
]

[[package]]
name = "sse-starlette"
version = "3.3.2"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "anyio" },
    { name = "starlette" },
]
sdist = { url = "https://files.pythonhosted.org/packages/5a/9f/c3695c2d2d4ef70072c3a06992850498b01c6bc9be531950813716b426fa/sse_starlette-3.3.2.tar.gz", hash = "sha256:678fca55a1945c734d8472a6cad186a55ab02840b4f6786f5ee8770970579dcd", size = 32326, upload-time = "2026-02-28T11:24:34.36Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/61/28/8cb142d3fe80c4a2d8af54ca0b003f47ce0ba920974e7990fa6e016402d1/sse_starlette-3.3.2-py3-none-any.whl", hash = "sha256:5c3ea3dad425c601236726af2f27689b74494643f57017cafcb6f8c9acfbb862", size = 14270, upload-time = "2026-02-28T11:24:32.984Z" },
]

[[package]]
name = "starlette"
version = "0.52.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "anyio" },
]
sdist = { url = "https://files.pythonhosted.org/packages/c4/68/79977123bb7be889ad680d79a40f339082c1978b5cfcf62c2d8d196873ac/starlette-0.52.1.tar.gz", hash = "sha256:834edd1b0a23167694292e94f597773bc3f89f362be6effee198165a35d62933", size = 2653702, upload-time = "2026-01-18T13:34:11.062Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/81/0d/13d1d239a25cbfb19e740db83143e95c772a1fe10202dda4b76792b114dd/starlette-0.52.1-py3-none-any.whl", hash = "sha256:0029d43eb3d273bc4f83a08720b4912ea4b071087a3b48db01b7c839f7954d74", size = 74272, upload-time = "2026-01-18T13:34:09.188Z" },
]

[[package]]
name = "tqdm"
version = "4.67.3"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "colorama", marker = "sys_platform == 'win32'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/09/a9/6ba95a270c6f1fbcd8dac228323f2777d886cb206987444e4bce66338dd4/tqdm-4.67.3.tar.gz", hash = "sha256:7d825f03f89244ef73f1d4ce193cb1774a8179fd96f31d7e1dcde62092b960bb", size = 169598, upload-time = "2026-02-03T17:35:53.048Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/16/e1/3079a9ff9b8e11b846c6ac5c8b5bfb7ff225eee721825310c91b3b50304f/tqdm-4.67.3-py3-none-any.whl", hash = "sha256:ee1e4c0e59148062281c49d80b25b67771a127c85fc9676d3be5f243206826bf", size = 78374, upload-time = "2026-02-03T17:35:50.982Z" },
]

[[package]]
name = "typing-extensions"
version = "4.15.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/72/94/1a15dd82efb362ac84269196e94cf00f187f7ed21c242792a923cdb1c61f/typing_extensions-4.15.0.tar.gz", hash = "sha256:0cea48d173cc12fa28ecabc3b837ea3cf6f38c6d1136f85cbaaf598984861466", size = 109391, upload-time = "2025-08-25T13:49:26.313Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/18/67/36e9267722cc04a6b9f15c7f3441c2363321a3ea07da7ae0c0707beb2a9c/typing_extensions-4.15.0-py3-none-any.whl", hash = "sha256:f0fa19c6845758ab08074a0cfa8b7aecb71c999ca73d62883bc25cc018c4e548", size = 44614, upload-time = "2025-08-25T13:49:24.86Z" },
]

[[package]]
name = "typing-inspection"
version = "0.4.2"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "typing-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/55/e3/70399cb7dd41c10ac53367ae42139cf4b1ca5f36bb3dc6c9d33acdb43655/typing_inspection-0.4.2.tar.gz", hash = "sha256:ba561c48a67c5958007083d386c3295464928b01faa735ab8547c5692e87f464", size = 75949, upload-time = "2025-10-01T02:14:41.687Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/dc/9b/47798a6c91d8bdb567fe2698fe81e0c6b7cb7ef4d13da4114b41d239f65d/typing_inspection-0.4.2-py3-none-any.whl", hash = "sha256:4ed1cacbdc298c220f1bd249ed5287caa16f34d44ef4e9c3d0cbad5b521545e7", size = 14611, upload-time = "2025-10-01T02:14:40.154Z" },
]

[[package]]
name = "urllib3"
version = "2.6.3"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/c7/24/5f1b3bdffd70275f6661c76461e25f024d5a38a46f04aaca912426a2b1d3/urllib3-2.6.3.tar.gz", hash = "sha256:1b62b6884944a57dbe321509ab94fd4d3b307075e0c2eae991ac71ee15ad38ed", size = 435556, upload-time = "2026-01-07T16:24:43.925Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/39/08/aaaad47bc4e9dc8c725e68f9d04865dbcb2052843ff09c97b08904852d84/urllib3-2.6.3-py3-none-any.whl", hash = "sha256:bf272323e553dfb2e87d9bfd225ca7b0f467b919d7bbd355436d3fd37cb0acd4", size = 131584, upload-time = "2026-01-07T16:24:42.685Z" },
]

[[package]]
name = "uvicorn"
version = "0.41.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "click" },
    { name = "h11" },
]
sdist = { url = "https://files.pythonhosted.org/packages/32/ce/eeb58ae4ac36fe09e3842eb02e0eb676bf2c53ae062b98f1b2531673efdd/uvicorn-0.41.0.tar.gz", hash = "sha256:09d11cf7008da33113824ee5a1c6422d89fbc2ff476540d69a34c87fab8b571a", size = 82633, upload-time = "2026-02-16T23:07:24.1Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/83/e4/d04a086285c20886c0daad0e026f250869201013d18f81d9ff5eada73a88/uvicorn-0.41.0-py3-none-any.whl", hash = "sha256:29e35b1d2c36a04b9e180d4007ede3bcb32a85fbdfd6c6aeb3f26839de088187", size = 68783, upload-time = "2026-02-16T23:07:22.357Z" },
]
```

## File: `python/interactive-agent-skill/.env.example`
```
OPENAI_API_KEY="your-openai-api-key"
ACONTEXT_API_KEY="your-acontext-api-key"

# Optional: custom OpenAI base URL
# OPENAI_BASE_URL="https://api.openai.com/v1"
```

## File: `python/interactive-agent-skill/README.md`
```markdown
# Agent Skill Demo

A demo showing how to create and use Acontext Skills within a sandbox environment, powered by an OpenAI agentic loop.

## What it does

1. Uploads a skill (from a zip file) to Acontext
2. Creates a sandbox with a persistent disk
3. Mounts the skill into the sandbox
4. Runs an interactive chat loop where an AI agent can execute bash commands, run Python scripts, and export files

## Prerequisites

- Python 3.10+
- [uv](https://docs.astral.sh/uv/) (recommended) or pip
- API keys for OpenAI and Acontext
- An Acontext instance (local or cloud)

## Setup

1. **Install dependencies:**

```bash
uv sync
```

2. **Configure environment variables:**

Copy the `.env.example` file to `.env`:

```bash
cp .env.example .env
```

Then edit the `.env` file with your actual values:

```env
# OpenAI Configuration
OPENAI_API_KEY=your-openai-api-key

# Acontext Configuration
ACONTEXT_API_KEY=sk-ac-your-root-api-bearer-token

# Optional: Custom OpenAI base URL (uncomment if using a different endpoint)
# OPENAI_BASE_URL=https://api.openai.com/v1
```

**Required variables:**
- `OPENAI_API_KEY` - Your OpenAI API key
- `ACONTEXT_API_KEY` - Your Acontext API key

**Optional variables:**
- `OPENAI_BASE_URL` - Custom OpenAI endpoint (only needed if using a proxy or alternative service)

## Usage

```bash
# Run with a skill zip file
python create_skill_sandbox.py <path_to_zip_file> [model_name]

# Examples
python create_skill_sandbox.py pptx.zip
python create_skill_sandbox.py xlsx.zip gpt-4.1
```

### Interactive Commands

Once the sandbox is ready, you can:
- Type requests for the agent to execute
- Type `reset` to clear conversation history
- Type `quit` to exit

## Example Skills

The folder includes example skill zip files:
- `pptx.zip` - PowerPoint generation skill
- `xlsx.zip` - Excel file generation skill
- `web-artifacts-builder.zip` - Web artifacts builder skill
```

## File: `python/interactive-agent-skill/create_skill_sandbox.py`
```python
import os
import sys
import json
from dotenv import load_dotenv
from openai import OpenAI
from acontext import AcontextClient, FileUpload
from acontext.agent import SANDBOX_TOOLS

load_dotenv()

oai_client = OpenAI(
    base_url=os.getenv("OPENAI_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY"),
)

if len(sys.argv) < 2:
    print(
        "Usage: python create_skill_sandbox.py <path_to_zip_file> <model_name optional>"
    )
    exit()
ZIP_PATH = sys.argv[1]
MODEL_NAME = sys.argv[2] if len(sys.argv) > 2 else "gpt-4.1"

client = AcontextClient(
    # base_url="http://localhost:8029/api/v1",
    # api_key="sk-ac-your-root-api-bearer-token",
    api_key=os.getenv("ACONTEXT_API_KEY")
)

with open(ZIP_PATH, "rb") as f:
    skill_bin = f.read()
name = os.path.basename(ZIP_PATH)

r = client.skills.create(
    file=FileUpload(filename=name, content=skill_bin),
)
SN = r.name
sid = r.id


sandbox = client.sandboxes.create()
disk = client.disks.create()
try:
    # Create tool context with mounted skills
    ctx = SANDBOX_TOOLS.format_context(
        client=client,
        sandbox_id=sandbox.sandbox_id,
        disk_id=disk.id,
        mount_skills=[sid],
    )

    tools = SANDBOX_TOOLS.to_openai_tool_schema()
    system_prompt = f"""You are a helpful assistant with access to a secure sandbox environment.
You can execute bash commands, run Python scripts, and export files for the user.

{ctx.get_context_prompt()}"""

    messages = []
    max_iterations = 20

    print("\n--- Sandbox Ready ---")
    print("Type your requests (or 'quit' to exit, 'reset' to clear history)")
    print("-" * 50)

    while True:
        try:
            user_input = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nExiting...")
            break

        if not user_input:
            continue

        if user_input.lower() == "quit":
            break

        if user_input.lower() == "reset":
            messages = []
            print("Conversation history cleared.")
            continue

        # Add user message
        messages.append({"role": "user", "content": user_input})
        print("\nAgent working...")

        # Agentic loop
        for iteration in range(max_iterations):
            print(f"\n[Iteration {iteration + 1}]")

            response = oai_client.chat.completions.create(
                model=MODEL_NAME,
                messages=[{"role": "system", "content": system_prompt}] + messages,
                tools=tools if tools else None,
                tool_choice="auto",
            )

            assistant_message = response.choices[0].message

            # Check if we're done (no tool calls)
            if not assistant_message.tool_calls:
                final_response = assistant_message.content or ""
                messages.append({"role": "assistant", "content": final_response})
                print(f"\nAgent: {final_response}")
                break

            # Process tool calls
            messages.append(assistant_message.model_dump())

            for tool_call in assistant_message.tool_calls:
                tool_name = tool_call.function.name
                tool_args = json.loads(tool_call.function.arguments)

                print(f"  Tool: {tool_name}")
                print(f"  Args: {json.dumps(tool_args, indent=2)}")

                # Execute the tool
                try:
                    result = SANDBOX_TOOLS.execute_tool(
                        ctx=ctx,
                        tool_name=tool_name,
                        llm_arguments=tool_args,
                    )
                except Exception as e:
                    result = json.dumps({"error": str(e)})

                print(
                    f"  Result: {result[:200]}..."
                    if len(result) > 200
                    else f"  Result: {result}"
                )

                # Add tool result to messages
                messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": result,
                    }
                )
        else:
            print("Max iterations reached. Task may be incomplete.")

finally:
    client.sandboxes.kill(sandbox.sandbox_id)
```

## File: `python/interactive-agent-skill/pyproject.toml`
```
[project]
name = "agent_skill_demo"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.10"
dependencies = [
    "acontext>=0.1.18",
    "openai>=2.15.0",
    "python-dotenv>=1.2.1",
]
```

## File: `python/interactive-agent-skill/uv.lock`
```
version = 1
revision = 3
requires-python = ">=3.10"

[[package]]
name = "acontext"
version = "0.1.18"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "anthropic" },
    { name = "httpx" },
    { name = "openai" },
    { name = "pydantic" },
    { name = "urllib3" },
]
sdist = { url = "https://files.pythonhosted.org/packages/13/4a/65d6f2f58e03bbbd8a269337a4d99536d8d3f7e9406e70b824a730875dac/acontext-0.1.18.tar.gz", hash = "sha256:7b1e763753fc23f007b4777949095a2ccc6d1b2deac714fad01095619a181824", size = 46865, upload-time = "2026-03-10T05:08:42.095Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/8d/76/bf60d77ab00da4170e9f7dfe42458b87c36b03f24ed2baa8c904d7ed9b97/acontext-0.1.18-py3-none-any.whl", hash = "sha256:a8810fb00f2b75c3509b15df07ab9dfef35dcc785ac07fcd6104ce92446b2b6b", size = 68510, upload-time = "2026-03-10T05:08:41.033Z" },
]

[[package]]
name = "agent-skill-demo"
version = "0.1.0"
source = { virtual = "." }
dependencies = [
    { name = "acontext" },
    { name = "openai" },
    { name = "python-dotenv" },
]

[package.metadata]
requires-dist = [
    { name = "acontext", specifier = ">=0.1.18" },
    { name = "openai", specifier = ">=2.15.0" },
    { name = "python-dotenv", specifier = ">=1.2.1" },
]

[[package]]
name = "annotated-types"
version = "0.7.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/ee/67/531ea369ba64dcff5ec9c3402f9f51bf748cec26dde048a2f973a4eea7f5/annotated_types-0.7.0.tar.gz", hash = "sha256:aff07c09a53a08bc8cfccb9c85b05f1aa9a2a6f23728d790723543408344ce89", size = 16081, upload-time = "2024-05-20T21:33:25.928Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/78/b6/6307fbef88d9b5ee7421e68d78a9f162e0da4900bc5f5793f6d3d0e34fb8/annotated_types-0.7.0-py3-none-any.whl", hash = "sha256:1f02e8b43a8fbbc3f3e0d4f0f4bfc8131bcb4eebe8849b8e5c773f3a1c582a53", size = 13643, upload-time = "2024-05-20T21:33:24.1Z" },
]

[[package]]
name = "anthropic"
version = "0.84.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "anyio" },
    { name = "distro" },
    { name = "docstring-parser" },
    { name = "httpx" },
    { name = "jiter" },
    { name = "pydantic" },
    { name = "sniffio" },
    { name = "typing-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/04/ea/0869d6df9ef83dcf393aeefc12dd81677d091c6ffc86f783e51cf44062f2/anthropic-0.84.0.tar.gz", hash = "sha256:72f5f90e5aebe62dca316cb013629cfa24996b0f5a4593b8c3d712bc03c43c37", size = 539457, upload-time = "2026-02-25T05:22:38.54Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/64/ca/218fa25002a332c0aa149ba18ffc0543175998b1f65de63f6d106689a345/anthropic-0.84.0-py3-none-any.whl", hash = "sha256:861c4c50f91ca45f942e091d83b60530ad6d4f98733bfe648065364da05d29e7", size = 455156, upload-time = "2026-02-25T05:22:40.468Z" },
]

[[package]]
name = "anyio"
version = "4.12.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "exceptiongroup", marker = "python_full_version < '3.11'" },
    { name = "idna" },
    { name = "typing-extensions", marker = "python_full_version < '3.13'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/96/f0/5eb65b2bb0d09ac6776f2eb54adee6abe8228ea05b20a5ad0e4945de8aac/anyio-4.12.1.tar.gz", hash = "sha256:41cfcc3a4c85d3f05c932da7c26d0201ac36f72abd4435ba90d0464a3ffed703", size = 228685, upload-time = "2026-01-06T11:45:21.246Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/38/0e/27be9fdef66e72d64c0cdc3cc2823101b80585f8119b5c112c2e8f5f7dab/anyio-4.12.1-py3-none-any.whl", hash = "sha256:d405828884fc140aa80a3c667b8beed277f1dfedec42ba031bd6ac3db606ab6c", size = 113592, upload-time = "2026-01-06T11:45:19.497Z" },
]

[[package]]
name = "certifi"
version = "2026.2.25"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/af/2d/7bf41579a8986e348fa033a31cdd0e4121114f6bce2457e8876010b092dd/certifi-2026.2.25.tar.gz", hash = "sha256:e887ab5cee78ea814d3472169153c2d12cd43b14bd03329a39a9c6e2e80bfba7", size = 155029, upload-time = "2026-02-25T02:54:17.342Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/9a/3c/c17fb3ca2d9c3acff52e30b309f538586f9f5b9c9cf454f3845fc9af4881/certifi-2026.2.25-py3-none-any.whl", hash = "sha256:027692e4402ad994f1c42e52a4997a9763c646b73e4096e4d5d6db8af1d6f0fa", size = 153684, upload-time = "2026-02-25T02:54:15.766Z" },
]

[[package]]
name = "colorama"
version = "0.4.6"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/d8/53/6f443c9a4a8358a93a6792e2acffb9d9d5cb0a5cfd8802644b7b1c9a02e4/colorama-0.4.6.tar.gz", hash = "sha256:08695f5cb7ed6e0531a20572697297273c47b8cae5a63ffc6d6ed5c201be6e44", size = 27697, upload-time = "2022-10-25T02:36:22.414Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/d1/d6/3965ed04c63042e047cb6a3e6ed1a63a35087b6a609aa3a15ed8ac56c221/colorama-0.4.6-py2.py3-none-any.whl", hash = "sha256:4f1d9991f5acc0ca119f9d443620b77f9d6b33703e51011c16baf57afb285fc6", size = 25335, upload-time = "2022-10-25T02:36:20.889Z" },
]

[[package]]
name = "distro"
version = "1.9.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/fc/f8/98eea607f65de6527f8a2e8885fc8015d3e6f5775df186e443e0964a11c3/distro-1.9.0.tar.gz", hash = "sha256:2fa77c6fd8940f116ee1d6b94a2f90b13b5ea8d019b98bc8bafdcabcdd9bdbed", size = 60722, upload-time = "2023-12-24T09:54:32.31Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/12/b3/231ffd4ab1fc9d679809f356cebee130ac7daa00d6d6f3206dd4fd137e9e/distro-1.9.0-py3-none-any.whl", hash = "sha256:7bffd925d65168f85027d8da9af6bddab658135b840670a223589bc0c8ef02b2", size = 20277, upload-time = "2023-12-24T09:54:30.421Z" },
]

[[package]]
name = "docstring-parser"
version = "0.17.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/b2/9d/c3b43da9515bd270df0f80548d9944e389870713cc1fe2b8fb35fe2bcefd/docstring_parser-0.17.0.tar.gz", hash = "sha256:583de4a309722b3315439bb31d64ba3eebada841f2e2cee23b99df001434c912", size = 27442, upload-time = "2025-07-21T07:35:01.868Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/55/e2/2537ebcff11c1ee1ff17d8d0b6f4db75873e3b0fb32c2d4a2ee31ecb310a/docstring_parser-0.17.0-py3-none-any.whl", hash = "sha256:cf2569abd23dce8099b300f9b4fa8191e9582dda731fd533daf54c4551658708", size = 36896, upload-time = "2025-07-21T07:35:00.684Z" },
]

[[package]]
name = "exceptiongroup"
version = "1.3.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "typing-extensions", marker = "python_full_version < '3.13'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/50/79/66800aadf48771f6b62f7eb014e352e5d06856655206165d775e675a02c9/exceptiongroup-1.3.1.tar.gz", hash = "sha256:8b412432c6055b0b7d14c310000ae93352ed6754f70fa8f7c34141f91c4e3219", size = 30371, upload-time = "2025-11-21T23:01:54.787Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/8a/0e/97c33bf5009bdbac74fd2beace167cab3f978feb69cc36f1ef79360d6c4e/exceptiongroup-1.3.1-py3-none-any.whl", hash = "sha256:a7a39a3bd276781e98394987d3a5701d0c4edffb633bb7a5144577f82c773598", size = 16740, upload-time = "2025-11-21T23:01:53.443Z" },
]

[[package]]
name = "h11"
version = "0.16.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/01/ee/02a2c011bdab74c6fb3c75474d40b3052059d95df7e73351460c8588d963/h11-0.16.0.tar.gz", hash = "sha256:4e35b956cf45792e4caa5885e69fba00bdbc6ffafbfa020300e549b208ee5ff1", size = 101250, upload-time = "2025-04-24T03:35:25.427Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/04/4b/29cac41a4d98d144bf5f6d33995617b185d14b22401f75ca86f384e87ff1/h11-0.16.0-py3-none-any.whl", hash = "sha256:63cf8bbe7522de3bf65932fda1d9c2772064ffb3dae62d55932da54b31cb6c86", size = 37515, upload-time = "2025-04-24T03:35:24.344Z" },
]

[[package]]
name = "httpcore"
version = "1.0.9"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "certifi" },
    { name = "h11" },
]
sdist = { url = "https://files.pythonhosted.org/packages/06/94/82699a10bca87a5556c9c59b5963f2d039dbd239f25bc2a63907a05a14cb/httpcore-1.0.9.tar.gz", hash = "sha256:6e34463af53fd2ab5d807f399a9b45ea31c3dfa2276f15a2c3f00afff6e176e8", size = 85484, upload-time = "2025-04-24T22:06:22.219Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/7e/f5/f66802a942d491edb555dd61e3a9961140fd64c90bce1eafd741609d334d/httpcore-1.0.9-py3-none-any.whl", hash = "sha256:2d400746a40668fc9dec9810239072b40b4484b640a8c38fd654a024c7a1bf55", size = 78784, upload-time = "2025-04-24T22:06:20.566Z" },
]

[[package]]
name = "httpx"
version = "0.28.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "anyio" },
    { name = "certifi" },
    { name = "httpcore" },
    { name = "idna" },
]
sdist = { url = "https://files.pythonhosted.org/packages/b1/df/48c586a5fe32a0f01324ee087459e112ebb7224f646c0b5023f5e79e9956/httpx-0.28.1.tar.gz", hash = "sha256:75e98c5f16b0f35b567856f597f06ff2270a374470a5c2392242528e3e3e42fc", size = 141406, upload-time = "2024-12-06T15:37:23.222Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/2a/39/e50c7c3a983047577ee07d2a9e53faf5a69493943ec3f6a384bdc792deb2/httpx-0.28.1-py3-none-any.whl", hash = "sha256:d909fcccc110f8c7faf814ca82a9a4d816bc5a6dbfea25d6591d6985b8ba59ad", size = 73517, upload-time = "2024-12-06T15:37:21.509Z" },
]

[[package]]
name = "idna"
version = "3.11"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/6f/6d/0703ccc57f3a7233505399edb88de3cbd678da106337b9fcde432b65ed60/idna-3.11.tar.gz", hash = "sha256:795dafcc9c04ed0c1fb032c2aa73654d8e8c5023a7df64a53f39190ada629902", size = 194582, upload-time = "2025-10-12T14:55:20.501Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/0e/61/66938bbb5fc52dbdf84594873d5b51fb1f7c7794e9c0f5bd885f30bc507b/idna-3.11-py3-none-any.whl", hash = "sha256:771a87f49d9defaf64091e6e6fe9c18d4833f140bd19464795bc32d966ca37ea", size = 71008, upload-time = "2025-10-12T14:55:18.883Z" },
]

[[package]]
name = "jiter"
version = "0.13.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/0d/5e/4ec91646aee381d01cdb9974e30882c9cd3b8c5d1079d6b5ff4af522439a/jiter-0.13.0.tar.gz", hash = "sha256:f2839f9c2c7e2dffc1bc5929a510e14ce0a946be9365fd1219e7ef342dae14f4", size = 164847, upload-time = "2026-02-02T12:37:56.441Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/d0/5a/41da76c5ea07bec1b0472b6b2fdb1b651074d504b19374d7e130e0cdfb25/jiter-0.13.0-cp310-cp310-macosx_10_12_x86_64.whl", hash = "sha256:2ffc63785fd6c7977defe49b9824ae6ce2b2e2b77ce539bdaf006c26da06342e", size = 311164, upload-time = "2026-02-02T12:35:17.688Z" },
    { url = "https://files.pythonhosted.org/packages/40/cb/4a1bf994a3e869f0d39d10e11efb471b76d0ad70ecbfb591427a46c880c2/jiter-0.13.0-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:4a638816427006c1e3f0013eb66d391d7a3acda99a7b0cf091eff4497ccea33a", size = 320296, upload-time = "2026-02-02T12:35:19.828Z" },
    { url = "https://files.pythonhosted.org/packages/09/82/acd71ca9b50ecebadc3979c541cd717cce2fe2bc86236f4fa597565d8f1a/jiter-0.13.0-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:19928b5d1ce0ff8c1ee1b9bdef3b5bfc19e8304f1b904e436caf30bc15dc6cf5", size = 352742, upload-time = "2026-02-02T12:35:21.258Z" },
    { url = "https://files.pythonhosted.org/packages/71/03/d1fc996f3aecfd42eb70922edecfb6dd26421c874503e241153ad41df94f/jiter-0.13.0-cp310-cp310-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:309549b778b949d731a2f0e1594a3f805716be704a73bf3ad9a807eed5eb5721", size = 363145, upload-time = "2026-02-02T12:35:24.653Z" },
    { url = "https://files.pythonhosted.org/packages/f1/61/a30492366378cc7a93088858f8991acd7d959759fe6138c12a4644e58e81/jiter-0.13.0-cp310-cp310-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:bcdabaea26cb04e25df3103ce47f97466627999260290349a88c8136ecae0060", size = 487683, upload-time = "2026-02-02T12:35:26.162Z" },
    { url = "https://files.pythonhosted.org/packages/20/4e/4223cffa9dbbbc96ed821c5aeb6bca510848c72c02086d1ed3f1da3d58a7/jiter-0.13.0-cp310-cp310-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:a3a377af27b236abbf665a69b2bdd680e3b5a0bd2af825cd3b81245279a7606c", size = 373579, upload-time = "2026-02-02T12:35:27.582Z" },
    { url = "https://files.pythonhosted.org/packages/fe/c9/b0489a01329ab07a83812d9ebcffe7820a38163c6d9e7da644f926ff877c/jiter-0.13.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:fe49d3ff6db74321f144dff9addd4a5874d3105ac5ba7c5b77fac099cfae31ae", size = 362904, upload-time = "2026-02-02T12:35:28.925Z" },
    { url = "https://files.pythonhosted.org/packages/05/af/53e561352a44afcba9a9bc67ee1d320b05a370aed8df54eafe714c4e454d/jiter-0.13.0-cp310-cp310-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:2113c17c9a67071b0f820733c0893ed1d467b5fcf4414068169e5c2cabddb1e2", size = 392380, upload-time = "2026-02-02T12:35:30.385Z" },
    { url = "https://files.pythonhosted.org/packages/76/2a/dd805c3afb8ed5b326c5ae49e725d1b1255b9754b1b77dbecdc621b20773/jiter-0.13.0-cp310-cp310-musllinux_1_1_aarch64.whl", hash = "sha256:ab1185ca5c8b9491b55ebf6c1e8866b8f68258612899693e24a92c5fdb9455d5", size = 517939, upload-time = "2026-02-02T12:35:31.865Z" },
    { url = "https://files.pythonhosted.org/packages/20/2a/7b67d76f55b8fe14c937e7640389612f05f9a4145fc28ae128aaa5e62257/jiter-0.13.0-cp310-cp310-musllinux_1_1_x86_64.whl", hash = "sha256:9621ca242547edc16400981ca3231e0c91c0c4c1ab8573a596cd9bb3575d5c2b", size = 551696, upload-time = "2026-02-02T12:35:33.306Z" },
    { url = "https://files.pythonhosted.org/packages/85/9c/57cdd64dac8f4c6ab8f994fe0eb04dc9fd1db102856a4458fcf8a99dfa62/jiter-0.13.0-cp310-cp310-win32.whl", hash = "sha256:a7637d92b1c9d7a771e8c56f445c7f84396d48f2e756e5978840ecba2fac0894", size = 204592, upload-time = "2026-02-02T12:35:34.58Z" },
    { url = "https://files.pythonhosted.org/packages/a7/38/f4f3ea5788b8a5bae7510a678cdc747eda0c45ffe534f9878ff37e7cf3b3/jiter-0.13.0-cp310-cp310-win_amd64.whl", hash = "sha256:c1b609e5cbd2f52bb74fb721515745b407df26d7b800458bd97cb3b972c29e7d", size = 206016, upload-time = "2026-02-02T12:35:36.435Z" },
    { url = "https://files.pythonhosted.org/packages/71/29/499f8c9eaa8a16751b1c0e45e6f5f1761d180da873d417996cc7bddc8eef/jiter-0.13.0-cp311-cp311-macosx_10_12_x86_64.whl", hash = "sha256:ea026e70a9a28ebbdddcbcf0f1323128a8db66898a06eaad3a4e62d2f554d096", size = 311157, upload-time = "2026-02-02T12:35:37.758Z" },
    { url = "https://files.pythonhosted.org/packages/50/f6/566364c777d2ab450b92100bea11333c64c38d32caf8dc378b48e5b20c46/jiter-0.13.0-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:66aa3e663840152d18cc8ff1e4faad3dd181373491b9cfdc6004b92198d67911", size = 319729, upload-time = "2026-02-02T12:35:39.246Z" },
    { url = "https://files.pythonhosted.org/packages/73/dd/560f13ec5e4f116d8ad2658781646cca91b617ae3b8758d4a5076b278f70/jiter-0.13.0-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:c3524798e70655ff19aec58c7d05adb1f074fecff62da857ea9be2b908b6d701", size = 354766, upload-time = "2026-02-02T12:35:40.662Z" },
    { url = "https://files.pythonhosted.org/packages/7c/0d/061faffcfe94608cbc28a0d42a77a74222bdf5055ccdbe5fd2292b94f510/jiter-0.13.0-cp311-cp311-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:ec7e287d7fbd02cb6e22f9a00dd9c9cd504c40a61f2c61e7e1f9690a82726b4c", size = 362587, upload-time = "2026-02-02T12:35:42.025Z" },
    { url = "https://files.pythonhosted.org/packages/92/c9/c66a7864982fd38a9773ec6e932e0398d1262677b8c60faecd02ffb67bf3/jiter-0.13.0-cp311-cp311-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:47455245307e4debf2ce6c6e65a717550a0244231240dcf3b8f7d64e4c2f22f4", size = 487537, upload-time = "2026-02-02T12:35:43.459Z" },
    { url = "https://files.pythonhosted.org/packages/6c/86/84eb4352cd3668f16d1a88929b5888a3fe0418ea8c1dfc2ad4e7bf6e069a/jiter-0.13.0-cp311-cp311-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:ee9da221dca6e0429c2704c1b3655fe7b025204a71d4d9b73390c759d776d165", size = 373717, upload-time = "2026-02-02T12:35:44.928Z" },
    { url = "https://files.pythonhosted.org/packages/6e/09/9fe4c159358176f82d4390407a03f506a8659ed13ca3ac93a843402acecf/jiter-0.13.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:24ab43126d5e05f3d53a36a8e11eb2f23304c6c1117844aaaf9a0aa5e40b5018", size = 362683, upload-time = "2026-02-02T12:35:46.636Z" },
    { url = "https://files.pythonhosted.org/packages/c9/5e/85f3ab9caca0c1d0897937d378b4a515cae9e119730563572361ea0c48ae/jiter-0.13.0-cp311-cp311-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:9da38b4fedde4fb528c740c2564628fbab737166a0e73d6d46cb4bb5463ff411", size = 392345, upload-time = "2026-02-02T12:35:48.088Z" },
    { url = "https://files.pythonhosted.org/packages/12/4c/05b8629ad546191939e6f0c2f17e29f542a398f4a52fb987bc70b6d1eb8b/jiter-0.13.0-cp311-cp311-musllinux_1_1_aarch64.whl", hash = "sha256:0b34c519e17658ed88d5047999a93547f8889f3c1824120c26ad6be5f27b6cf5", size = 517775, upload-time = "2026-02-02T12:35:49.482Z" },
    { url = "https://files.pythonhosted.org/packages/4d/88/367ea2eb6bc582c7052e4baf5ddf57ebe5ab924a88e0e09830dfb585c02d/jiter-0.13.0-cp311-cp311-musllinux_1_1_x86_64.whl", hash = "sha256:d2a6394e6af690d462310a86b53c47ad75ac8c21dc79f120714ea449979cb1d3", size = 551325, upload-time = "2026-02-02T12:35:51.104Z" },
    { url = "https://files.pythonhosted.org/packages/f3/12/fa377ffb94a2f28c41afaed093e0d70cfe512035d5ecb0cad0ae4792d35e/jiter-0.13.0-cp311-cp311-win32.whl", hash = "sha256:0f0c065695f616a27c920a56ad0d4fc46415ef8b806bf8fc1cacf25002bd24e1", size = 204709, upload-time = "2026-02-02T12:35:52.467Z" },
    { url = "https://files.pythonhosted.org/packages/cb/16/8e8203ce92f844dfcd3d9d6a5a7322c77077248dbb12da52d23193a839cd/jiter-0.13.0-cp311-cp311-win_amd64.whl", hash = "sha256:0733312953b909688ae3c2d58d043aa040f9f1a6a75693defed7bc2cc4bf2654", size = 204560, upload-time = "2026-02-02T12:35:53.925Z" },
    { url = "https://files.pythonhosted.org/packages/44/26/97cc40663deb17b9e13c3a5cf29251788c271b18ee4d262c8f94798b8336/jiter-0.13.0-cp311-cp311-win_arm64.whl", hash = "sha256:5d9b34ad56761b3bf0fbe8f7e55468704107608512350962d3317ffd7a4382d5", size = 189608, upload-time = "2026-02-02T12:35:55.304Z" },
    { url = "https://files.pythonhosted.org/packages/2e/30/7687e4f87086829955013ca12a9233523349767f69653ebc27036313def9/jiter-0.13.0-cp312-cp312-macosx_10_12_x86_64.whl", hash = "sha256:0a2bd69fc1d902e89925fc34d1da51b2128019423d7b339a45d9e99c894e0663", size = 307958, upload-time = "2026-02-02T12:35:57.165Z" },
    { url = "https://files.pythonhosted.org/packages/c3/27/e57f9a783246ed95481e6749cc5002a8a767a73177a83c63ea71f0528b90/jiter-0.13.0-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:f917a04240ef31898182f76a332f508f2cc4b57d2b4d7ad2dbfebbfe167eb505", size = 318597, upload-time = "2026-02-02T12:35:58.591Z" },
    { url = "https://files.pythonhosted.org/packages/cf/52/e5719a60ac5d4d7c5995461a94ad5ef962a37c8bf5b088390e6fad59b2ff/jiter-0.13.0-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:c1e2b199f446d3e82246b4fd9236d7cb502dc2222b18698ba0d986d2fecc6152", size = 348821, upload-time = "2026-02-02T12:36:00.093Z" },
    { url = "https://files.pythonhosted.org/packages/61/db/c1efc32b8ba4c740ab3fc2d037d8753f67685f475e26b9d6536a4322bcdd/jiter-0.13.0-cp312-cp312-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:04670992b576fa65bd056dbac0c39fe8bd67681c380cb2b48efa885711d9d726", size = 364163, upload-time = "2026-02-02T12:36:01.937Z" },
    { url = "https://files.pythonhosted.org/packages/55/8a/fb75556236047c8806995671a18e4a0ad646ed255276f51a20f32dceaeec/jiter-0.13.0-cp312-cp312-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:5a1aff1fbdb803a376d4d22a8f63f8e7ccbce0b4890c26cc7af9e501ab339ef0", size = 483709, upload-time = "2026-02-02T12:36:03.41Z" },
    { url = "https://files.pythonhosted.org/packages/7e/16/43512e6ee863875693a8e6f6d532e19d650779d6ba9a81593ae40a9088ff/jiter-0.13.0-cp312-cp312-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:3b3fb8c2053acaef8580809ac1d1f7481a0a0bdc012fd7f5d8b18fb696a5a089", size = 370480, upload-time = "2026-02-02T12:36:04.791Z" },
    { url = "https://files.pythonhosted.org/packages/f8/4c/09b93e30e984a187bc8aaa3510e1ec8dcbdcd71ca05d2f56aac0492453aa/jiter-0.13.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:bdaba7d87e66f26a2c45d8cbadcbfc4bf7884182317907baf39cfe9775bb4d93", size = 360735, upload-time = "2026-02-02T12:36:06.994Z" },
    { url = "https://files.pythonhosted.org/packages/1a/1b/46c5e349019874ec5dfa508c14c37e29864ea108d376ae26d90bee238cd7/jiter-0.13.0-cp312-cp312-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:7b88d649135aca526da172e48083da915ec086b54e8e73a425ba50999468cc08", size = 391814, upload-time = "2026-02-02T12:36:08.368Z" },
    { url = "https://files.pythonhosted.org/packages/15/9e/26184760e85baee7162ad37b7912797d2077718476bf91517641c92b3639/jiter-0.13.0-cp312-cp312-musllinux_1_1_aarch64.whl", hash = "sha256:e404ea551d35438013c64b4f357b0474c7abf9f781c06d44fcaf7a14c69ff9e2", size = 513990, upload-time = "2026-02-02T12:36:09.993Z" },
    { url = "https://files.pythonhosted.org/packages/e9/34/2c9355247d6debad57a0a15e76ab1566ab799388042743656e566b3b7de1/jiter-0.13.0-cp312-cp312-musllinux_1_1_x86_64.whl", hash = "sha256:1f4748aad1b4a93c8bdd70f604d0f748cdc0e8744c5547798acfa52f10e79228", size = 548021, upload-time = "2026-02-02T12:36:11.376Z" },
    { url = "https://files.pythonhosted.org/packages/ac/4a/9f2c23255d04a834398b9c2e0e665382116911dc4d06b795710503cdad25/jiter-0.13.0-cp312-cp312-win32.whl", hash = "sha256:0bf670e3b1445fc4d31612199f1744f67f889ee1bbae703c4b54dc097e5dd394", size = 203024, upload-time = "2026-02-02T12:36:12.682Z" },
    { url = "https://files.pythonhosted.org/packages/09/ee/f0ae675a957ae5a8f160be3e87acea6b11dc7b89f6b7ab057e77b2d2b13a/jiter-0.13.0-cp312-cp312-win_amd64.whl", hash = "sha256:15db60e121e11fe186c0b15236bd5d18381b9ddacdcf4e659feb96fc6c969c92", size = 205424, upload-time = "2026-02-02T12:36:13.93Z" },
    { url = "https://files.pythonhosted.org/packages/1b/02/ae611edf913d3cbf02c97cdb90374af2082c48d7190d74c1111dde08bcdd/jiter-0.13.0-cp312-cp312-win_arm64.whl", hash = "sha256:41f92313d17989102f3cb5dd533a02787cdb99454d494344b0361355da52fcb9", size = 186818, upload-time = "2026-02-02T12:36:15.308Z" },
    { url = "https://files.pythonhosted.org/packages/91/9c/7ee5a6ff4b9991e1a45263bfc46731634c4a2bde27dfda6c8251df2d958c/jiter-0.13.0-cp313-cp313-macosx_10_12_x86_64.whl", hash = "sha256:1f8a55b848cbabf97d861495cd65f1e5c590246fabca8b48e1747c4dfc8f85bf", size = 306897, upload-time = "2026-02-02T12:36:16.748Z" },
    { url = "https://files.pythonhosted.org/packages/7c/02/be5b870d1d2be5dd6a91bdfb90f248fbb7dcbd21338f092c6b89817c3dbf/jiter-0.13.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:f556aa591c00f2c45eb1b89f68f52441a016034d18b65da60e2d2875bbbf344a", size = 317507, upload-time = "2026-02-02T12:36:18.351Z" },
    { url = "https://files.pythonhosted.org/packages/da/92/b25d2ec333615f5f284f3a4024f7ce68cfa0604c322c6808b2344c7f5d2b/jiter-0.13.0-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:f7e1d61da332ec412350463891923f960c3073cf1aae93b538f0bb4c8cd46efb", size = 350560, upload-time = "2026-02-02T12:36:19.746Z" },
    { url = "https://files.pythonhosted.org/packages/be/ec/74dcb99fef0aca9fbe56b303bf79f6bd839010cb18ad41000bf6cc71eec0/jiter-0.13.0-cp313-cp313-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:3097d665a27bc96fd9bbf7f86178037db139f319f785e4757ce7ccbf390db6c2", size = 363232, upload-time = "2026-02-02T12:36:21.243Z" },
    { url = "https://files.pythonhosted.org/packages/1b/37/f17375e0bb2f6a812d4dd92d7616e41917f740f3e71343627da9db2824ce/jiter-0.13.0-cp313-cp313-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:9d01ecc3a8cbdb6f25a37bd500510550b64ddf9f7d64a107d92f3ccb25035d0f", size = 483727, upload-time = "2026-02-02T12:36:22.688Z" },
    { url = "https://files.pythonhosted.org/packages/77/d2/a71160a5ae1a1e66c1395b37ef77da67513b0adba73b993a27fbe47eb048/jiter-0.13.0-cp313-cp313-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:ed9bbc30f5d60a3bdf63ae76beb3f9db280d7f195dfcfa61af792d6ce912d159", size = 370799, upload-time = "2026-02-02T12:36:24.106Z" },
    { url = "https://files.pythonhosted.org/packages/01/99/ed5e478ff0eb4e8aa5fd998f9d69603c9fd3f32de3bd16c2b1194f68361c/jiter-0.13.0-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:98fbafb6e88256f4454de33c1f40203d09fc33ed19162a68b3b257b29ca7f663", size = 359120, upload-time = "2026-02-02T12:36:25.519Z" },
    { url = "https://files.pythonhosted.org/packages/16/be/7ffd08203277a813f732ba897352797fa9493faf8dc7995b31f3d9cb9488/jiter-0.13.0-cp313-cp313-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:5467696f6b827f1116556cb0db620440380434591e93ecee7fd14d1a491b6daa", size = 390664, upload-time = "2026-02-02T12:36:26.866Z" },
    { url = "https://files.pythonhosted.org/packages/d1/84/e0787856196d6d346264d6dcccb01f741e5f0bd014c1d9a2ebe149caf4f3/jiter-0.13.0-cp313-cp313-musllinux_1_1_aarch64.whl", hash = "sha256:2d08c9475d48b92892583df9da592a0e2ac49bcd41fae1fec4f39ba6cf107820", size = 513543, upload-time = "2026-02-02T12:36:28.217Z" },
    { url = "https://files.pythonhosted.org/packages/65/50/ecbd258181c4313cf79bca6c88fb63207d04d5bf5e4f65174114d072aa55/jiter-0.13.0-cp313-cp313-musllinux_1_1_x86_64.whl", hash = "sha256:aed40e099404721d7fcaf5b89bd3b4568a4666358bcac7b6b15c09fb6252ab68", size = 547262, upload-time = "2026-02-02T12:36:29.678Z" },
    { url = "https://files.pythonhosted.org/packages/27/da/68f38d12e7111d2016cd198161b36e1f042bd115c169255bcb7ec823a3bf/jiter-0.13.0-cp313-cp313-win32.whl", hash = "sha256:36ebfbcffafb146d0e6ffb3e74d51e03d9c35ce7c625c8066cdbfc7b953bdc72", size = 200630, upload-time = "2026-02-02T12:36:31.808Z" },
    { url = "https://files.pythonhosted.org/packages/25/65/3bd1a972c9a08ecd22eb3b08a95d1941ebe6938aea620c246cf426ae09c2/jiter-0.13.0-cp313-cp313-win_amd64.whl", hash = "sha256:8d76029f077379374cf0dbc78dbe45b38dec4a2eb78b08b5194ce836b2517afc", size = 202602, upload-time = "2026-02-02T12:36:33.679Z" },
    { url = "https://files.pythonhosted.org/packages/15/fe/13bd3678a311aa67686bb303654792c48206a112068f8b0b21426eb6851e/jiter-0.13.0-cp313-cp313-win_arm64.whl", hash = "sha256:bb7613e1a427cfcb6ea4544f9ac566b93d5bf67e0d48c787eca673ff9c9dff2b", size = 185939, upload-time = "2026-02-02T12:36:35.065Z" },
    { url = "https://files.pythonhosted.org/packages/49/19/a929ec002ad3228bc97ca01dbb14f7632fffdc84a95ec92ceaf4145688ae/jiter-0.13.0-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:fa476ab5dd49f3bf3a168e05f89358c75a17608dbabb080ef65f96b27c19ab10", size = 316616, upload-time = "2026-02-02T12:36:36.579Z" },
    { url = "https://files.pythonhosted.org/packages/52/56/d19a9a194afa37c1728831e5fb81b7722c3de18a3109e8f282bfc23e587a/jiter-0.13.0-cp313-cp313t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:ade8cb6ff5632a62b7dbd4757d8c5573f7a2e9ae285d6b5b841707d8363205ef", size = 346850, upload-time = "2026-02-02T12:36:38.058Z" },
    { url = "https://files.pythonhosted.org/packages/36/4a/94e831c6bf287754a8a019cb966ed39ff8be6ab78cadecf08df3bb02d505/jiter-0.13.0-cp313-cp313t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:9950290340acc1adaded363edd94baebcee7dabdfa8bee4790794cd5cfad2af6", size = 358551, upload-time = "2026-02-02T12:36:39.417Z" },
    { url = "https://files.pythonhosted.org/packages/a2/ec/a4c72c822695fa80e55d2b4142b73f0012035d9fcf90eccc56bc060db37c/jiter-0.13.0-cp313-cp313t-win_amd64.whl", hash = "sha256:2b4972c6df33731aac0742b64fd0d18e0a69bc7d6e03108ce7d40c85fd9e3e6d", size = 201950, upload-time = "2026-02-02T12:36:40.791Z" },
    { url = "https://files.pythonhosted.org/packages/b6/00/393553ec27b824fbc29047e9c7cd4a3951d7fbe4a76743f17e44034fa4e4/jiter-0.13.0-cp313-cp313t-win_arm64.whl", hash = "sha256:701a1e77d1e593c1b435315ff625fd071f0998c5f02792038a5ca98899261b7d", size = 185852, upload-time = "2026-02-02T12:36:42.077Z" },
    { url = "https://files.pythonhosted.org/packages/6e/f5/f1997e987211f6f9bd71b8083047b316208b4aca0b529bb5f8c96c89ef3e/jiter-0.13.0-cp314-cp314-macosx_10_12_x86_64.whl", hash = "sha256:cc5223ab19fe25e2f0bf2643204ad7318896fe3729bf12fde41b77bfc4fafff0", size = 308804, upload-time = "2026-02-02T12:36:43.496Z" },
    { url = "https://files.pythonhosted.org/packages/cd/8f/5482a7677731fd44881f0204981ce2d7175db271f82cba2085dd2212e095/jiter-0.13.0-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:9776ebe51713acf438fd9b4405fcd86893ae5d03487546dae7f34993217f8a91", size = 318787, upload-time = "2026-02-02T12:36:45.071Z" },
    { url = "https://files.pythonhosted.org/packages/f3/b9/7257ac59778f1cd025b26a23c5520a36a424f7f1b068f2442a5b499b7464/jiter-0.13.0-cp314-cp314-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:879e768938e7b49b5e90b7e3fecc0dbec01b8cb89595861fb39a8967c5220d09", size = 353880, upload-time = "2026-02-02T12:36:47.365Z" },
    { url = "https://files.pythonhosted.org/packages/c3/87/719eec4a3f0841dad99e3d3604ee4cba36af4419a76f3cb0b8e2e691ad67/jiter-0.13.0-cp314-cp314-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:682161a67adea11e3aae9038c06c8b4a9a71023228767477d683f69903ebc607", size = 366702, upload-time = "2026-02-02T12:36:48.871Z" },
    { url = "https://files.pythonhosted.org/packages/d2/65/415f0a75cf6921e43365a1bc227c565cb949caca8b7532776e430cbaa530/jiter-0.13.0-cp314-cp314-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:a13b68cd1cd8cc9de8f244ebae18ccb3e4067ad205220ef324c39181e23bbf66", size = 486319, upload-time = "2026-02-02T12:36:53.006Z" },
    { url = "https://files.pythonhosted.org/packages/54/a2/9e12b48e82c6bbc6081fd81abf915e1443add1b13d8fc586e1d90bb02bb8/jiter-0.13.0-cp314-cp314-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:87ce0f14c6c08892b610686ae8be350bf368467b6acd5085a5b65441e2bf36d2", size = 372289, upload-time = "2026-02-02T12:36:54.593Z" },
    { url = "https://files.pythonhosted.org/packages/4e/c1/e4693f107a1789a239c759a432e9afc592366f04e901470c2af89cfd28e1/jiter-0.13.0-cp314-cp314-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:0c365005b05505a90d1c47856420980d0237adf82f70c4aff7aebd3c1cc143ad", size = 360165, upload-time = "2026-02-02T12:36:56.112Z" },
    { url = "https://files.pythonhosted.org/packages/17/08/91b9ea976c1c758240614bd88442681a87672eebc3d9a6dde476874e706b/jiter-0.13.0-cp314-cp314-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:1317fdffd16f5873e46ce27d0e0f7f4f90f0cdf1d86bf6abeaea9f63ca2c401d", size = 389634, upload-time = "2026-02-02T12:36:57.495Z" },
    { url = "https://files.pythonhosted.org/packages/18/23/58325ef99390d6d40427ed6005bf1ad54f2577866594bcf13ce55675f87d/jiter-0.13.0-cp314-cp314-musllinux_1_1_aarch64.whl", hash = "sha256:c05b450d37ba0c9e21c77fef1f205f56bcee2330bddca68d344baebfc55ae0df", size = 514933, upload-time = "2026-02-02T12:36:58.909Z" },
    { url = "https://files.pythonhosted.org/packages/5b/25/69f1120c7c395fd276c3996bb8adefa9c6b84c12bb7111e5c6ccdcd8526d/jiter-0.13.0-cp314-cp314-musllinux_1_1_x86_64.whl", hash = "sha256:775e10de3849d0631a97c603f996f518159272db00fdda0a780f81752255ee9d", size = 548842, upload-time = "2026-02-02T12:37:00.433Z" },
    { url = "https://files.pythonhosted.org/packages/18/05/981c9669d86850c5fbb0d9e62bba144787f9fba84546ba43d624ee27ef29/jiter-0.13.0-cp314-cp314-win32.whl", hash = "sha256:632bf7c1d28421c00dd8bbb8a3bac5663e1f57d5cd5ed962bce3c73bf62608e6", size = 202108, upload-time = "2026-02-02T12:37:01.718Z" },
    { url = "https://files.pythonhosted.org/packages/8d/96/cdcf54dd0b0341db7d25413229888a346c7130bd20820530905fdb65727b/jiter-0.13.0-cp314-cp314-win_amd64.whl", hash = "sha256:f22ef501c3f87ede88f23f9b11e608581c14f04db59b6a801f354397ae13739f", size = 204027, upload-time = "2026-02-02T12:37:03.075Z" },
    { url = "https://files.pythonhosted.org/packages/fb/f9/724bcaaab7a3cd727031fe4f6995cb86c4bd344909177c186699c8dec51a/jiter-0.13.0-cp314-cp314-win_arm64.whl", hash = "sha256:07b75fe09a4ee8e0c606200622e571e44943f47254f95e2436c8bdcaceb36d7d", size = 187199, upload-time = "2026-02-02T12:37:04.414Z" },
    { url = "https://files.pythonhosted.org/packages/62/92/1661d8b9fd6a3d7a2d89831db26fe3c1509a287d83ad7838831c7b7a5c7e/jiter-0.13.0-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:964538479359059a35fb400e769295d4b315ae61e4105396d355a12f7fef09f0", size = 318423, upload-time = "2026-02-02T12:37:05.806Z" },
    { url = "https://files.pythonhosted.org/packages/4f/3b/f77d342a54d4ebcd128e520fc58ec2f5b30a423b0fd26acdfc0c6fef8e26/jiter-0.13.0-cp314-cp314t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:e104da1db1c0991b3eaed391ccd650ae8d947eab1480c733e5a3fb28d4313e40", size = 351438, upload-time = "2026-02-02T12:37:07.189Z" },
    { url = "https://files.pythonhosted.org/packages/76/b3/ba9a69f0e4209bd3331470c723c2f5509e6f0482e416b612431a5061ed71/jiter-0.13.0-cp314-cp314t-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:0e3a5f0cde8ff433b8e88e41aa40131455420fb3649a3c7abdda6145f8cb7202", size = 364774, upload-time = "2026-02-02T12:37:08.579Z" },
    { url = "https://files.pythonhosted.org/packages/b3/16/6cdb31fa342932602458dbb631bfbd47f601e03d2e4950740e0b2100b570/jiter-0.13.0-cp314-cp314t-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:57aab48f40be1db920a582b30b116fe2435d184f77f0e4226f546794cedd9cf0", size = 487238, upload-time = "2026-02-02T12:37:10.066Z" },
    { url = "https://files.pythonhosted.org/packages/ed/b1/956cc7abaca8d95c13aa8d6c9b3f3797241c246cd6e792934cc4c8b250d2/jiter-0.13.0-cp314-cp314t-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:7772115877c53f62beeb8fd853cab692dbc04374ef623b30f997959a4c0e7e95", size = 372892, upload-time = "2026-02-02T12:37:11.656Z" },
    { url = "https://files.pythonhosted.org/packages/26/c4/97ecde8b1e74f67b8598c57c6fccf6df86ea7861ed29da84629cdbba76c4/jiter-0.13.0-cp314-cp314t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:1211427574b17b633cfceba5040de8081e5abf114f7a7602f73d2e16f9fdaa59", size = 360309, upload-time = "2026-02-02T12:37:13.244Z" },
    { url = "https://files.pythonhosted.org/packages/4b/d7/eabe3cf46715854ccc80be2cd78dd4c36aedeb30751dbf85a1d08c14373c/jiter-0.13.0-cp314-cp314t-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:7beae3a3d3b5212d3a55d2961db3c292e02e302feb43fce6a3f7a31b90ea6dfe", size = 389607, upload-time = "2026-02-02T12:37:14.881Z" },
    { url = "https://files.pythonhosted.org/packages/df/2d/03963fc0804e6109b82decfb9974eb92df3797fe7222428cae12f8ccaa0c/jiter-0.13.0-cp314-cp314t-musllinux_1_1_aarch64.whl", hash = "sha256:e5562a0f0e90a6223b704163ea28e831bd3a9faa3512a711f031611e6b06c939", size = 514986, upload-time = "2026-02-02T12:37:16.326Z" },
    { url = "https://files.pythonhosted.org/packages/f6/6c/8c83b45eb3eb1c1e18d841fe30b4b5bc5619d781267ca9bc03e005d8fd0a/jiter-0.13.0-cp314-cp314t-musllinux_1_1_x86_64.whl", hash = "sha256:6c26a424569a59140fb51160a56df13f438a2b0967365e987889186d5fc2f6f9", size = 548756, upload-time = "2026-02-02T12:37:17.736Z" },
    { url = "https://files.pythonhosted.org/packages/47/66/eea81dfff765ed66c68fd2ed8c96245109e13c896c2a5015c7839c92367e/jiter-0.13.0-cp314-cp314t-win32.whl", hash = "sha256:24dc96eca9f84da4131cdf87a95e6ce36765c3b156fc9ae33280873b1c32d5f6", size = 201196, upload-time = "2026-02-02T12:37:19.101Z" },
    { url = "https://files.pythonhosted.org/packages/ff/32/4ac9c7a76402f8f00d00842a7f6b83b284d0cf7c1e9d4227bc95aa6d17fa/jiter-0.13.0-cp314-cp314t-win_amd64.whl", hash = "sha256:0a8d76c7524087272c8ae913f5d9d608bd839154b62c4322ef65723d2e5bb0b8", size = 204215, upload-time = "2026-02-02T12:37:20.495Z" },
    { url = "https://files.pythonhosted.org/packages/f9/8e/7def204fea9f9be8b3c21a6f2dd6c020cf56c7d5ff753e0e23ed7f9ea57e/jiter-0.13.0-cp314-cp314t-win_arm64.whl", hash = "sha256:2c26cf47e2cad140fa23b6d58d435a7c0161f5c514284802f25e87fddfe11024", size = 187152, upload-time = "2026-02-02T12:37:22.124Z" },
    { url = "https://files.pythonhosted.org/packages/79/b3/3c29819a27178d0e461a8571fb63c6ae38be6dc36b78b3ec2876bbd6a910/jiter-0.13.0-graalpy311-graalpy242_311_native-macosx_10_12_x86_64.whl", hash = "sha256:b1cbfa133241d0e6bdab48dcdc2604e8ba81512f6bbd68ec3e8e1357dd3c316c", size = 307016, upload-time = "2026-02-02T12:37:42.755Z" },
    { url = "https://files.pythonhosted.org/packages/eb/ae/60993e4b07b1ac5ebe46da7aa99fdbb802eb986c38d26e3883ac0125c4e0/jiter-0.13.0-graalpy311-graalpy242_311_native-macosx_11_0_arm64.whl", hash = "sha256:db367d8be9fad6e8ebbac4a7578b7af562e506211036cba2c06c3b998603c3d2", size = 305024, upload-time = "2026-02-02T12:37:44.774Z" },
    { url = "https://files.pythonhosted.org/packages/77/fa/2227e590e9cf98803db2811f172b2d6460a21539ab73006f251c66f44b14/jiter-0.13.0-graalpy311-graalpy242_311_native-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:45f6f8efb2f3b0603092401dc2df79fa89ccbc027aaba4174d2d4133ed661434", size = 339337, upload-time = "2026-02-02T12:37:46.668Z" },
    { url = "https://files.pythonhosted.org/packages/2d/92/015173281f7eb96c0ef580c997da8ef50870d4f7f4c9e03c845a1d62ae04/jiter-0.13.0-graalpy311-graalpy242_311_native-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:597245258e6ad085d064780abfb23a284d418d3e61c57362d9449c6c7317ee2d", size = 346395, upload-time = "2026-02-02T12:37:48.09Z" },
    { url = "https://files.pythonhosted.org/packages/80/60/e50fa45dd7e2eae049f0ce964663849e897300433921198aef94b6ffa23a/jiter-0.13.0-graalpy312-graalpy250_312_native-macosx_10_12_x86_64.whl", hash = "sha256:3d744a6061afba08dd7ae375dcde870cffb14429b7477e10f67e9e6d68772a0a", size = 305169, upload-time = "2026-02-02T12:37:50.376Z" },
    { url = "https://files.pythonhosted.org/packages/d2/73/a009f41c5eed71c49bec53036c4b33555afcdee70682a18c6f66e396c039/jiter-0.13.0-graalpy312-graalpy250_312_native-macosx_11_0_arm64.whl", hash = "sha256:ff732bd0a0e778f43d5009840f20b935e79087b4dc65bd36f1cd0f9b04b8ff7f", size = 303808, upload-time = "2026-02-02T12:37:52.092Z" },
    { url = "https://files.pythonhosted.org/packages/c4/10/528b439290763bff3d939268085d03382471b442f212dca4ff5f12802d43/jiter-0.13.0-graalpy312-graalpy250_312_native-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:ab44b178f7981fcaea7e0a5df20e773c663d06ffda0198f1a524e91b2fde7e59", size = 337384, upload-time = "2026-02-02T12:37:53.582Z" },
    { url = "https://files.pythonhosted.org/packages/67/8a/a342b2f0251f3dac4ca17618265d93bf244a2a4d089126e81e4c1056ac50/jiter-0.13.0-graalpy312-graalpy250_312_native-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:7bb00b6d26db67a05fe3e12c76edc75f32077fb51deed13822dc648fa373bc19", size = 343768, upload-time = "2026-02-02T12:37:55.055Z" },
]

[[package]]
name = "openai"
version = "2.26.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "anyio" },
    { name = "distro" },
    { name = "httpx" },
    { name = "jiter" },
    { name = "pydantic" },
    { name = "sniffio" },
    { name = "tqdm" },
    { name = "typing-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/d7/91/2a06c4e9597c338cac1e5e5a8dd6f29e1836fc229c4c523529dca387fda8/openai-2.26.0.tar.gz", hash = "sha256:b41f37c140ae0034a6e92b0c509376d907f3a66109935fba2c1b471a7c05a8fb", size = 666702, upload-time = "2026-03-05T23:17:35.874Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/c6/2e/3f73e8ca53718952222cacd0cf7eecc9db439d020f0c1fe7ae717e4e199a/openai-2.26.0-py3-none-any.whl", hash = "sha256:6151bf8f83802f036117f06cc8a57b3a4da60da9926826cc96747888b57f394f", size = 1136409, upload-time = "2026-03-05T23:17:34.072Z" },
]

[[package]]
name = "pydantic"
version = "2.12.5"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "annotated-types" },
    { name = "pydantic-core" },
    { name = "typing-extensions" },
    { name = "typing-inspection" },
]
sdist = { url = "https://files.pythonhosted.org/packages/69/44/36f1a6e523abc58ae5f928898e4aca2e0ea509b5aa6f6f392a5d882be928/pydantic-2.12.5.tar.gz", hash = "sha256:4d351024c75c0f085a9febbb665ce8c0c6ec5d30e903bdb6394b7ede26aebb49", size = 821591, upload-time = "2025-11-26T15:11:46.471Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/5a/87/b70ad306ebb6f9b585f114d0ac2137d792b48be34d732d60e597c2f8465a/pydantic-2.12.5-py3-none-any.whl", hash = "sha256:e561593fccf61e8a20fc46dfc2dfe075b8be7d0188df33f221ad1f0139180f9d", size = 463580, upload-time = "2025-11-26T15:11:44.605Z" },
]

[[package]]
name = "pydantic-core"
version = "2.41.5"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "typing-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/71/70/23b021c950c2addd24ec408e9ab05d59b035b39d97cdc1130e1bce647bb6/pydantic_core-2.41.5.tar.gz", hash = "sha256:08daa51ea16ad373ffd5e7606252cc32f07bc72b28284b6bc9c6df804816476e", size = 460952, upload-time = "2025-11-04T13:43:49.098Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/c6/90/32c9941e728d564b411d574d8ee0cf09b12ec978cb22b294995bae5549a5/pydantic_core-2.41.5-cp310-cp310-macosx_10_12_x86_64.whl", hash = "sha256:77b63866ca88d804225eaa4af3e664c5faf3568cea95360d21f4725ab6e07146", size = 2107298, upload-time = "2025-11-04T13:39:04.116Z" },
    { url = "https://files.pythonhosted.org/packages/fb/a8/61c96a77fe28993d9a6fb0f4127e05430a267b235a124545d79fea46dd65/pydantic_core-2.41.5-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:dfa8a0c812ac681395907e71e1274819dec685fec28273a28905df579ef137e2", size = 1901475, upload-time = "2025-11-04T13:39:06.055Z" },
    { url = "https://files.pythonhosted.org/packages/5d/b6/338abf60225acc18cdc08b4faef592d0310923d19a87fba1faf05af5346e/pydantic_core-2.41.5-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:5921a4d3ca3aee735d9fd163808f5e8dd6c6972101e4adbda9a4667908849b97", size = 1918815, upload-time = "2025-11-04T13:39:10.41Z" },
    { url = "https://files.pythonhosted.org/packages/d1/1c/2ed0433e682983d8e8cba9c8d8ef274d4791ec6a6f24c58935b90e780e0a/pydantic_core-2.41.5-cp310-cp310-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:e25c479382d26a2a41b7ebea1043564a937db462816ea07afa8a44c0866d52f9", size = 2065567, upload-time = "2025-11-04T13:39:12.244Z" },
    { url = "https://files.pythonhosted.org/packages/b3/24/cf84974ee7d6eae06b9e63289b7b8f6549d416b5c199ca2d7ce13bbcf619/pydantic_core-2.41.5-cp310-cp310-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:f547144f2966e1e16ae626d8ce72b4cfa0caedc7fa28052001c94fb2fcaa1c52", size = 2230442, upload-time = "2025-11-04T13:39:13.962Z" },
    { url = "https://files.pythonhosted.org/packages/fd/21/4e287865504b3edc0136c89c9c09431be326168b1eb7841911cbc877a995/pydantic_core-2.41.5-cp310-cp310-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:6f52298fbd394f9ed112d56f3d11aabd0d5bd27beb3084cc3d8ad069483b8941", size = 2350956, upload-time = "2025-11-04T13:39:15.889Z" },
    { url = "https://files.pythonhosted.org/packages/a8/76/7727ef2ffa4b62fcab916686a68a0426b9b790139720e1934e8ba797e238/pydantic_core-2.41.5-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:100baa204bb412b74fe285fb0f3a385256dad1d1879f0a5cb1499ed2e83d132a", size = 2068253, upload-time = "2025-11-04T13:39:17.403Z" },
    { url = "https://files.pythonhosted.org/packages/d5/8c/a4abfc79604bcb4c748e18975c44f94f756f08fb04218d5cb87eb0d3a63e/pydantic_core-2.41.5-cp310-cp310-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:05a2c8852530ad2812cb7914dc61a1125dc4e06252ee98e5638a12da6cc6fb6c", size = 2177050, upload-time = "2025-11-04T13:39:19.351Z" },
    { url = "https://files.pythonhosted.org/packages/67/b1/de2e9a9a79b480f9cb0b6e8b6ba4c50b18d4e89852426364c66aa82bb7b3/pydantic_core-2.41.5-cp310-cp310-musllinux_1_1_aarch64.whl", hash = "sha256:29452c56df2ed968d18d7e21f4ab0ac55e71dc59524872f6fc57dcf4a3249ed2", size = 2147178, upload-time = "2025-11-04T13:39:21Z" },
    { url = "https://files.pythonhosted.org/packages/16/c1/dfb33f837a47b20417500efaa0378adc6635b3c79e8369ff7a03c494b4ac/pydantic_core-2.41.5-cp310-cp310-musllinux_1_1_armv7l.whl", hash = "sha256:d5160812ea7a8a2ffbe233d8da666880cad0cbaf5d4de74ae15c313213d62556", size = 2341833, upload-time = "2025-11-04T13:39:22.606Z" },
    { url = "https://files.pythonhosted.org/packages/47/36/00f398642a0f4b815a9a558c4f1dca1b4020a7d49562807d7bc9ff279a6c/pydantic_core-2.41.5-cp310-cp310-musllinux_1_1_x86_64.whl", hash = "sha256:df3959765b553b9440adfd3c795617c352154e497a4eaf3752555cfb5da8fc49", size = 2321156, upload-time = "2025-11-04T13:39:25.843Z" },
    { url = "https://files.pythonhosted.org/packages/7e/70/cad3acd89fde2010807354d978725ae111ddf6d0ea46d1ea1775b5c1bd0c/pydantic_core-2.41.5-cp310-cp310-win32.whl", hash = "sha256:1f8d33a7f4d5a7889e60dc39856d76d09333d8a6ed0f5f1190635cbec70ec4ba", size = 1989378, upload-time = "2025-11-04T13:39:27.92Z" },
    { url = "https://files.pythonhosted.org/packages/76/92/d338652464c6c367e5608e4488201702cd1cbb0f33f7b6a85a60fe5f3720/pydantic_core-2.41.5-cp310-cp310-win_amd64.whl", hash = "sha256:62de39db01b8d593e45871af2af9e497295db8d73b085f6bfd0b18c83c70a8f9", size = 2013622, upload-time = "2025-11-04T13:39:29.848Z" },
    { url = "https://files.pythonhosted.org/packages/e8/72/74a989dd9f2084b3d9530b0915fdda64ac48831c30dbf7c72a41a5232db8/pydantic_core-2.41.5-cp311-cp311-macosx_10_12_x86_64.whl", hash = "sha256:a3a52f6156e73e7ccb0f8cced536adccb7042be67cb45f9562e12b319c119da6", size = 2105873, upload-time = "2025-11-04T13:39:31.373Z" },
    { url = "https://files.pythonhosted.org/packages/12/44/37e403fd9455708b3b942949e1d7febc02167662bf1a7da5b78ee1ea2842/pydantic_core-2.41.5-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:7f3bf998340c6d4b0c9a2f02d6a400e51f123b59565d74dc60d252ce888c260b", size = 1899826, upload-time = "2025-11-04T13:39:32.897Z" },
    { url = "https://files.pythonhosted.org/packages/33/7f/1d5cab3ccf44c1935a359d51a8a2a9e1a654b744b5e7f80d41b88d501eec/pydantic_core-2.41.5-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:378bec5c66998815d224c9ca994f1e14c0c21cb95d2f52b6021cc0b2a58f2a5a", size = 1917869, upload-time = "2025-11-04T13:39:34.469Z" },
    { url = "https://files.pythonhosted.org/packages/6e/6a/30d94a9674a7fe4f4744052ed6c5e083424510be1e93da5bc47569d11810/pydantic_core-2.41.5-cp311-cp311-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:e7b576130c69225432866fe2f4a469a85a54ade141d96fd396dffcf607b558f8", size = 2063890, upload-time = "2025-11-04T13:39:36.053Z" },
    { url = "https://files.pythonhosted.org/packages/50/be/76e5d46203fcb2750e542f32e6c371ffa9b8ad17364cf94bb0818dbfb50c/pydantic_core-2.41.5-cp311-cp311-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:6cb58b9c66f7e4179a2d5e0f849c48eff5c1fca560994d6eb6543abf955a149e", size = 2229740, upload-time = "2025-11-04T13:39:37.753Z" },
    { url = "https://files.pythonhosted.org/packages/d3/ee/fed784df0144793489f87db310a6bbf8118d7b630ed07aa180d6067e653a/pydantic_core-2.41.5-cp311-cp311-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:88942d3a3dff3afc8288c21e565e476fc278902ae4d6d134f1eeda118cc830b1", size = 2350021, upload-time = "2025-11-04T13:39:40.94Z" },
    { url = "https://files.pythonhosted.org/packages/c8/be/8fed28dd0a180dca19e72c233cbf58efa36df055e5b9d90d64fd1740b828/pydantic_core-2.41.5-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:f31d95a179f8d64d90f6831d71fa93290893a33148d890ba15de25642c5d075b", size = 2066378, upload-time = "2025-11-04T13:39:42.523Z" },
    { url = "https://files.pythonhosted.org/packages/b0/3b/698cf8ae1d536a010e05121b4958b1257f0b5522085e335360e53a6b1c8b/pydantic_core-2.41.5-cp311-cp311-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:c1df3d34aced70add6f867a8cf413e299177e0c22660cc767218373d0779487b", size = 2175761, upload-time = "2025-11-04T13:39:44.553Z" },
    { url = "https://files.pythonhosted.org/packages/b8/ba/15d537423939553116dea94ce02f9c31be0fa9d0b806d427e0308ec17145/pydantic_core-2.41.5-cp311-cp311-musllinux_1_1_aarch64.whl", hash = "sha256:4009935984bd36bd2c774e13f9a09563ce8de4abaa7226f5108262fa3e637284", size = 2146303, upload-time = "2025-11-04T13:39:46.238Z" },
    { url = "https://files.pythonhosted.org/packages/58/7f/0de669bf37d206723795f9c90c82966726a2ab06c336deba4735b55af431/pydantic_core-2.41.5-cp311-cp311-musllinux_1_1_armv7l.whl", hash = "sha256:34a64bc3441dc1213096a20fe27e8e128bd3ff89921706e83c0b1ac971276594", size = 2340355, upload-time = "2025-11-04T13:39:48.002Z" },
    { url = "https://files.pythonhosted.org/packages/e5/de/e7482c435b83d7e3c3ee5ee4451f6e8973cff0eb6007d2872ce6383f6398/pydantic_core-2.41.5-cp311-cp311-musllinux_1_1_x86_64.whl", hash = "sha256:c9e19dd6e28fdcaa5a1de679aec4141f691023916427ef9bae8584f9c2fb3b0e", size = 2319875, upload-time = "2025-11-04T13:39:49.705Z" },
    { url = "https://files.pythonhosted.org/packages/fe/e6/8c9e81bb6dd7560e33b9053351c29f30c8194b72f2d6932888581f503482/pydantic_core-2.41.5-cp311-cp311-win32.whl", hash = "sha256:2c010c6ded393148374c0f6f0bf89d206bf3217f201faa0635dcd56bd1520f6b", size = 1987549, upload-time = "2025-11-04T13:39:51.842Z" },
    { url = "https://files.pythonhosted.org/packages/11/66/f14d1d978ea94d1bc21fc98fcf570f9542fe55bfcc40269d4e1a21c19bf7/pydantic_core-2.41.5-cp311-cp311-win_amd64.whl", hash = "sha256:76ee27c6e9c7f16f47db7a94157112a2f3a00e958bc626e2f4ee8bec5c328fbe", size = 2011305, upload-time = "2025-11-04T13:39:53.485Z" },
    { url = "https://files.pythonhosted.org/packages/56/d8/0e271434e8efd03186c5386671328154ee349ff0354d83c74f5caaf096ed/pydantic_core-2.41.5-cp311-cp311-win_arm64.whl", hash = "sha256:4bc36bbc0b7584de96561184ad7f012478987882ebf9f9c389b23f432ea3d90f", size = 1972902, upload-time = "2025-11-04T13:39:56.488Z" },
    { url = "https://files.pythonhosted.org/packages/5f/5d/5f6c63eebb5afee93bcaae4ce9a898f3373ca23df3ccaef086d0233a35a7/pydantic_core-2.41.5-cp312-cp312-macosx_10_12_x86_64.whl", hash = "sha256:f41a7489d32336dbf2199c8c0a215390a751c5b014c2c1c5366e817202e9cdf7", size = 2110990, upload-time = "2025-11-04T13:39:58.079Z" },
    { url = "https://files.pythonhosted.org/packages/aa/32/9c2e8ccb57c01111e0fd091f236c7b371c1bccea0fa85247ac55b1e2b6b6/pydantic_core-2.41.5-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:070259a8818988b9a84a449a2a7337c7f430a22acc0859c6b110aa7212a6d9c0", size = 1896003, upload-time = "2025-11-04T13:39:59.956Z" },
    { url = "https://files.pythonhosted.org/packages/68/b8/a01b53cb0e59139fbc9e4fda3e9724ede8de279097179be4ff31f1abb65a/pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:e96cea19e34778f8d59fe40775a7a574d95816eb150850a85a7a4c8f4b94ac69", size = 1919200, upload-time = "2025-11-04T13:40:02.241Z" },
    { url = "https://files.pythonhosted.org/packages/38/de/8c36b5198a29bdaade07b5985e80a233a5ac27137846f3bc2d3b40a47360/pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:ed2e99c456e3fadd05c991f8f437ef902e00eedf34320ba2b0842bd1c3ca3a75", size = 2052578, upload-time = "2025-11-04T13:40:04.401Z" },
    { url = "https://files.pythonhosted.org/packages/00/b5/0e8e4b5b081eac6cb3dbb7e60a65907549a1ce035a724368c330112adfdd/pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:65840751b72fbfd82c3c640cff9284545342a4f1eb1586ad0636955b261b0b05", size = 2208504, upload-time = "2025-11-04T13:40:06.072Z" },
    { url = "https://files.pythonhosted.org/packages/77/56/87a61aad59c7c5b9dc8caad5a41a5545cba3810c3e828708b3d7404f6cef/pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:e536c98a7626a98feb2d3eaf75944ef6f3dbee447e1f841eae16f2f0a72d8ddc", size = 2335816, upload-time = "2025-11-04T13:40:07.835Z" },
    { url = "https://files.pythonhosted.org/packages/0d/76/941cc9f73529988688a665a5c0ecff1112b3d95ab48f81db5f7606f522d3/pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:eceb81a8d74f9267ef4081e246ffd6d129da5d87e37a77c9bde550cb04870c1c", size = 2075366, upload-time = "2025-11-04T13:40:09.804Z" },
    { url = "https://files.pythonhosted.org/packages/d3/43/ebef01f69baa07a482844faaa0a591bad1ef129253ffd0cdaa9d8a7f72d3/pydantic_core-2.41.5-cp312-cp312-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:d38548150c39b74aeeb0ce8ee1d8e82696f4a4e16ddc6de7b1d8823f7de4b9b5", size = 2171698, upload-time = "2025-11-04T13:40:12.004Z" },
    { url = "https://files.pythonhosted.org/packages/b1/87/41f3202e4193e3bacfc2c065fab7706ebe81af46a83d3e27605029c1f5a6/pydantic_core-2.41.5-cp312-cp312-musllinux_1_1_aarch64.whl", hash = "sha256:c23e27686783f60290e36827f9c626e63154b82b116d7fe9adba1fda36da706c", size = 2132603, upload-time = "2025-11-04T13:40:13.868Z" },
    { url = "https://files.pythonhosted.org/packages/49/7d/4c00df99cb12070b6bccdef4a195255e6020a550d572768d92cc54dba91a/pydantic_core-2.41.5-cp312-cp312-musllinux_1_1_armv7l.whl", hash = "sha256:482c982f814460eabe1d3bb0adfdc583387bd4691ef00b90575ca0d2b6fe2294", size = 2329591, upload-time = "2025-11-04T13:40:15.672Z" },
    { url = "https://files.pythonhosted.org/packages/cc/6a/ebf4b1d65d458f3cda6a7335d141305dfa19bdc61140a884d165a8a1bbc7/pydantic_core-2.41.5-cp312-cp312-musllinux_1_1_x86_64.whl", hash = "sha256:bfea2a5f0b4d8d43adf9d7b8bf019fb46fdd10a2e5cde477fbcb9d1fa08c68e1", size = 2319068, upload-time = "2025-11-04T13:40:17.532Z" },
    { url = "https://files.pythonhosted.org/packages/49/3b/774f2b5cd4192d5ab75870ce4381fd89cf218af999515baf07e7206753f0/pydantic_core-2.41.5-cp312-cp312-win32.whl", hash = "sha256:b74557b16e390ec12dca509bce9264c3bbd128f8a2c376eaa68003d7f327276d", size = 1985908, upload-time = "2025-11-04T13:40:19.309Z" },
    { url = "https://files.pythonhosted.org/packages/86/45/00173a033c801cacf67c190fef088789394feaf88a98a7035b0e40d53dc9/pydantic_core-2.41.5-cp312-cp312-win_amd64.whl", hash = "sha256:1962293292865bca8e54702b08a4f26da73adc83dd1fcf26fbc875b35d81c815", size = 2020145, upload-time = "2025-11-04T13:40:21.548Z" },
    { url = "https://files.pythonhosted.org/packages/f9/22/91fbc821fa6d261b376a3f73809f907cec5ca6025642c463d3488aad22fb/pydantic_core-2.41.5-cp312-cp312-win_arm64.whl", hash = "sha256:1746d4a3d9a794cacae06a5eaaccb4b8643a131d45fbc9af23e353dc0a5ba5c3", size = 1976179, upload-time = "2025-11-04T13:40:23.393Z" },
    { url = "https://files.pythonhosted.org/packages/87/06/8806241ff1f70d9939f9af039c6c35f2360cf16e93c2ca76f184e76b1564/pydantic_core-2.41.5-cp313-cp313-macosx_10_12_x86_64.whl", hash = "sha256:941103c9be18ac8daf7b7adca8228f8ed6bb7a1849020f643b3a14d15b1924d9", size = 2120403, upload-time = "2025-11-04T13:40:25.248Z" },
    { url = "https://files.pythonhosted.org/packages/94/02/abfa0e0bda67faa65fef1c84971c7e45928e108fe24333c81f3bfe35d5f5/pydantic_core-2.41.5-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:112e305c3314f40c93998e567879e887a3160bb8689ef3d2c04b6cc62c33ac34", size = 1896206, upload-time = "2025-11-04T13:40:27.099Z" },
    { url = "https://files.pythonhosted.org/packages/15/df/a4c740c0943e93e6500f9eb23f4ca7ec9bf71b19e608ae5b579678c8d02f/pydantic_core-2.41.5-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:0cbaad15cb0c90aa221d43c00e77bb33c93e8d36e0bf74760cd00e732d10a6a0", size = 1919307, upload-time = "2025-11-04T13:40:29.806Z" },
    { url = "https://files.pythonhosted.org/packages/9a/e3/6324802931ae1d123528988e0e86587c2072ac2e5394b4bc2bc34b61ff6e/pydantic_core-2.41.5-cp313-cp313-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:03ca43e12fab6023fc79d28ca6b39b05f794ad08ec2feccc59a339b02f2b3d33", size = 2063258, upload-time = "2025-11-04T13:40:33.544Z" },
    { url = "https://files.pythonhosted.org/packages/c9/d4/2230d7151d4957dd79c3044ea26346c148c98fbf0ee6ebd41056f2d62ab5/pydantic_core-2.41.5-cp313-cp313-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:dc799088c08fa04e43144b164feb0c13f9a0bc40503f8df3e9fde58a3c0c101e", size = 2214917, upload-time = "2025-11-04T13:40:35.479Z" },
    { url = "https://files.pythonhosted.org/packages/e6/9f/eaac5df17a3672fef0081b6c1bb0b82b33ee89aa5cec0d7b05f52fd4a1fa/pydantic_core-2.41.5-cp313-cp313-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:97aeba56665b4c3235a0e52b2c2f5ae9cd071b8a8310ad27bddb3f7fb30e9aa2", size = 2332186, upload-time = "2025-11-04T13:40:37.436Z" },
    { url = "https://files.pythonhosted.org/packages/cf/4e/35a80cae583a37cf15604b44240e45c05e04e86f9cfd766623149297e971/pydantic_core-2.41.5-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:406bf18d345822d6c21366031003612b9c77b3e29ffdb0f612367352aab7d586", size = 2073164, upload-time = "2025-11-04T13:40:40.289Z" },
    { url = "https://files.pythonhosted.org/packages/bf/e3/f6e262673c6140dd3305d144d032f7bd5f7497d3871c1428521f19f9efa2/pydantic_core-2.41.5-cp313-cp313-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:b93590ae81f7010dbe380cdeab6f515902ebcbefe0b9327cc4804d74e93ae69d", size = 2179146, upload-time = "2025-11-04T13:40:42.809Z" },
    { url = "https://files.pythonhosted.org/packages/75/c7/20bd7fc05f0c6ea2056a4565c6f36f8968c0924f19b7d97bbfea55780e73/pydantic_core-2.41.5-cp313-cp313-musllinux_1_1_aarch64.whl", hash = "sha256:01a3d0ab748ee531f4ea6c3e48ad9dac84ddba4b0d82291f87248f2f9de8d740", size = 2137788, upload-time = "2025-11-04T13:40:44.752Z" },
    { url = "https://files.pythonhosted.org/packages/3a/8d/34318ef985c45196e004bc46c6eab2eda437e744c124ef0dbe1ff2c9d06b/pydantic_core-2.41.5-cp313-cp313-musllinux_1_1_armv7l.whl", hash = "sha256:6561e94ba9dacc9c61bce40e2d6bdc3bfaa0259d3ff36ace3b1e6901936d2e3e", size = 2340133, upload-time = "2025-11-04T13:40:46.66Z" },
    { url = "https://files.pythonhosted.org/packages/9c/59/013626bf8c78a5a5d9350d12e7697d3d4de951a75565496abd40ccd46bee/pydantic_core-2.41.5-cp313-cp313-musllinux_1_1_x86_64.whl", hash = "sha256:915c3d10f81bec3a74fbd4faebe8391013ba61e5a1a8d48c4455b923bdda7858", size = 2324852, upload-time = "2025-11-04T13:40:48.575Z" },
    { url = "https://files.pythonhosted.org/packages/1a/d9/c248c103856f807ef70c18a4f986693a46a8ffe1602e5d361485da502d20/pydantic_core-2.41.5-cp313-cp313-win32.whl", hash = "sha256:650ae77860b45cfa6e2cdafc42618ceafab3a2d9a3811fcfbd3bbf8ac3c40d36", size = 1994679, upload-time = "2025-11-04T13:40:50.619Z" },
    { url = "https://files.pythonhosted.org/packages/9e/8b/341991b158ddab181cff136acd2552c9f35bd30380422a639c0671e99a91/pydantic_core-2.41.5-cp313-cp313-win_amd64.whl", hash = "sha256:79ec52ec461e99e13791ec6508c722742ad745571f234ea6255bed38c6480f11", size = 2019766, upload-time = "2025-11-04T13:40:52.631Z" },
    { url = "https://files.pythonhosted.org/packages/73/7d/f2f9db34af103bea3e09735bb40b021788a5e834c81eedb541991badf8f5/pydantic_core-2.41.5-cp313-cp313-win_arm64.whl", hash = "sha256:3f84d5c1b4ab906093bdc1ff10484838aca54ef08de4afa9de0f5f14d69639cd", size = 1981005, upload-time = "2025-11-04T13:40:54.734Z" },
    { url = "https://files.pythonhosted.org/packages/ea/28/46b7c5c9635ae96ea0fbb779e271a38129df2550f763937659ee6c5dbc65/pydantic_core-2.41.5-cp314-cp314-macosx_10_12_x86_64.whl", hash = "sha256:3f37a19d7ebcdd20b96485056ba9e8b304e27d9904d233d7b1015db320e51f0a", size = 2119622, upload-time = "2025-11-04T13:40:56.68Z" },
    { url = "https://files.pythonhosted.org/packages/74/1a/145646e5687e8d9a1e8d09acb278c8535ebe9e972e1f162ed338a622f193/pydantic_core-2.41.5-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:1d1d9764366c73f996edd17abb6d9d7649a7eb690006ab6adbda117717099b14", size = 1891725, upload-time = "2025-11-04T13:40:58.807Z" },
    { url = "https://files.pythonhosted.org/packages/23/04/e89c29e267b8060b40dca97bfc64a19b2a3cf99018167ea1677d96368273/pydantic_core-2.41.5-cp314-cp314-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:25e1c2af0fce638d5f1988b686f3b3ea8cd7de5f244ca147c777769e798a9cd1", size = 1915040, upload-time = "2025-11-04T13:41:00.853Z" },
    { url = "https://files.pythonhosted.org/packages/84/a3/15a82ac7bd97992a82257f777b3583d3e84bdb06ba6858f745daa2ec8a85/pydantic_core-2.41.5-cp314-cp314-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:506d766a8727beef16b7adaeb8ee6217c64fc813646b424d0804d67c16eddb66", size = 2063691, upload-time = "2025-11-04T13:41:03.504Z" },
    { url = "https://files.pythonhosted.org/packages/74/9b/0046701313c6ef08c0c1cf0e028c67c770a4e1275ca73131563c5f2a310a/pydantic_core-2.41.5-cp314-cp314-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:4819fa52133c9aa3c387b3328f25c1facc356491e6135b459f1de698ff64d869", size = 2213897, upload-time = "2025-11-04T13:41:05.804Z" },
    { url = "https://files.pythonhosted.org/packages/8a/cd/6bac76ecd1b27e75a95ca3a9a559c643b3afcd2dd62086d4b7a32a18b169/pydantic_core-2.41.5-cp314-cp314-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:2b761d210c9ea91feda40d25b4efe82a1707da2ef62901466a42492c028553a2", size = 2333302, upload-time = "2025-11-04T13:41:07.809Z" },
    { url = "https://files.pythonhosted.org/packages/4c/d2/ef2074dc020dd6e109611a8be4449b98cd25e1b9b8a303c2f0fca2f2bcf7/pydantic_core-2.41.5-cp314-cp314-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:22f0fb8c1c583a3b6f24df2470833b40207e907b90c928cc8d3594b76f874375", size = 2064877, upload-time = "2025-11-04T13:41:09.827Z" },
    { url = "https://files.pythonhosted.org/packages/18/66/e9db17a9a763d72f03de903883c057b2592c09509ccfe468187f2a2eef29/pydantic_core-2.41.5-cp314-cp314-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:2782c870e99878c634505236d81e5443092fba820f0373997ff75f90f68cd553", size = 2180680, upload-time = "2025-11-04T13:41:12.379Z" },
    { url = "https://files.pythonhosted.org/packages/d3/9e/3ce66cebb929f3ced22be85d4c2399b8e85b622db77dad36b73c5387f8f8/pydantic_core-2.41.5-cp314-cp314-musllinux_1_1_aarch64.whl", hash = "sha256:0177272f88ab8312479336e1d777f6b124537d47f2123f89cb37e0accea97f90", size = 2138960, upload-time = "2025-11-04T13:41:14.627Z" },
    { url = "https://files.pythonhosted.org/packages/a6/62/205a998f4327d2079326b01abee48e502ea739d174f0a89295c481a2272e/pydantic_core-2.41.5-cp314-cp314-musllinux_1_1_armv7l.whl", hash = "sha256:63510af5e38f8955b8ee5687740d6ebf7c2a0886d15a6d65c32814613681bc07", size = 2339102, upload-time = "2025-11-04T13:41:16.868Z" },
    { url = "https://files.pythonhosted.org/packages/3c/0d/f05e79471e889d74d3d88f5bd20d0ed189ad94c2423d81ff8d0000aab4ff/pydantic_core-2.41.5-cp314-cp314-musllinux_1_1_x86_64.whl", hash = "sha256:e56ba91f47764cc14f1daacd723e3e82d1a89d783f0f5afe9c364b8bb491ccdb", size = 2326039, upload-time = "2025-11-04T13:41:18.934Z" },
    { url = "https://files.pythonhosted.org/packages/ec/e1/e08a6208bb100da7e0c4b288eed624a703f4d129bde2da475721a80cab32/pydantic_core-2.41.5-cp314-cp314-win32.whl", hash = "sha256:aec5cf2fd867b4ff45b9959f8b20ea3993fc93e63c7363fe6851424c8a7e7c23", size = 1995126, upload-time = "2025-11-04T13:41:21.418Z" },
    { url = "https://files.pythonhosted.org/packages/48/5d/56ba7b24e9557f99c9237e29f5c09913c81eeb2f3217e40e922353668092/pydantic_core-2.41.5-cp314-cp314-win_amd64.whl", hash = "sha256:8e7c86f27c585ef37c35e56a96363ab8de4e549a95512445b85c96d3e2f7c1bf", size = 2015489, upload-time = "2025-11-04T13:41:24.076Z" },
    { url = "https://files.pythonhosted.org/packages/4e/bb/f7a190991ec9e3e0ba22e4993d8755bbc4a32925c0b5b42775c03e8148f9/pydantic_core-2.41.5-cp314-cp314-win_arm64.whl", hash = "sha256:e672ba74fbc2dc8eea59fb6d4aed6845e6905fc2a8afe93175d94a83ba2a01a0", size = 1977288, upload-time = "2025-11-04T13:41:26.33Z" },
    { url = "https://files.pythonhosted.org/packages/92/ed/77542d0c51538e32e15afe7899d79efce4b81eee631d99850edc2f5e9349/pydantic_core-2.41.5-cp314-cp314t-macosx_10_12_x86_64.whl", hash = "sha256:8566def80554c3faa0e65ac30ab0932b9e3a5cd7f8323764303d468e5c37595a", size = 2120255, upload-time = "2025-11-04T13:41:28.569Z" },
    { url = "https://files.pythonhosted.org/packages/bb/3d/6913dde84d5be21e284439676168b28d8bbba5600d838b9dca99de0fad71/pydantic_core-2.41.5-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:b80aa5095cd3109962a298ce14110ae16b8c1aece8b72f9dafe81cf597ad80b3", size = 1863760, upload-time = "2025-11-04T13:41:31.055Z" },
    { url = "https://files.pythonhosted.org/packages/5a/f0/e5e6b99d4191da102f2b0eb9687aaa7f5bea5d9964071a84effc3e40f997/pydantic_core-2.41.5-cp314-cp314t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:3006c3dd9ba34b0c094c544c6006cc79e87d8612999f1a5d43b769b89181f23c", size = 1878092, upload-time = "2025-11-04T13:41:33.21Z" },
    { url = "https://files.pythonhosted.org/packages/71/48/36fb760642d568925953bcc8116455513d6e34c4beaa37544118c36aba6d/pydantic_core-2.41.5-cp314-cp314t-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:72f6c8b11857a856bcfa48c86f5368439f74453563f951e473514579d44aa612", size = 2053385, upload-time = "2025-11-04T13:41:35.508Z" },
    { url = "https://files.pythonhosted.org/packages/20/25/92dc684dd8eb75a234bc1c764b4210cf2646479d54b47bf46061657292a8/pydantic_core-2.41.5-cp314-cp314t-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:5cb1b2f9742240e4bb26b652a5aeb840aa4b417c7748b6f8387927bc6e45e40d", size = 2218832, upload-time = "2025-11-04T13:41:37.732Z" },
    { url = "https://files.pythonhosted.org/packages/e2/09/f53e0b05023d3e30357d82eb35835d0f6340ca344720a4599cd663dca599/pydantic_core-2.41.5-cp314-cp314t-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:bd3d54f38609ff308209bd43acea66061494157703364ae40c951f83ba99a1a9", size = 2327585, upload-time = "2025-11-04T13:41:40Z" },
    { url = "https://files.pythonhosted.org/packages/aa/4e/2ae1aa85d6af35a39b236b1b1641de73f5a6ac4d5a7509f77b814885760c/pydantic_core-2.41.5-cp314-cp314t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:2ff4321e56e879ee8d2a879501c8e469414d948f4aba74a2d4593184eb326660", size = 2041078, upload-time = "2025-11-04T13:41:42.323Z" },
    { url = "https://files.pythonhosted.org/packages/cd/13/2e215f17f0ef326fc72afe94776edb77525142c693767fc347ed6288728d/pydantic_core-2.41.5-cp314-cp314t-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:d0d2568a8c11bf8225044aa94409e21da0cb09dcdafe9ecd10250b2baad531a9", size = 2173914, upload-time = "2025-11-04T13:41:45.221Z" },
    { url = "https://files.pythonhosted.org/packages/02/7a/f999a6dcbcd0e5660bc348a3991c8915ce6599f4f2c6ac22f01d7a10816c/pydantic_core-2.41.5-cp314-cp314t-musllinux_1_1_aarch64.whl", hash = "sha256:a39455728aabd58ceabb03c90e12f71fd30fa69615760a075b9fec596456ccc3", size = 2129560, upload-time = "2025-11-04T13:41:47.474Z" },
    { url = "https://files.pythonhosted.org/packages/3a/b1/6c990ac65e3b4c079a4fb9f5b05f5b013afa0f4ed6780a3dd236d2cbdc64/pydantic_core-2.41.5-cp314-cp314t-musllinux_1_1_armv7l.whl", hash = "sha256:239edca560d05757817c13dc17c50766136d21f7cd0fac50295499ae24f90fdf", size = 2329244, upload-time = "2025-11-04T13:41:49.992Z" },
    { url = "https://files.pythonhosted.org/packages/d9/02/3c562f3a51afd4d88fff8dffb1771b30cfdfd79befd9883ee094f5b6c0d8/pydantic_core-2.41.5-cp314-cp314t-musllinux_1_1_x86_64.whl", hash = "sha256:2a5e06546e19f24c6a96a129142a75cee553cc018ffee48a460059b1185f4470", size = 2331955, upload-time = "2025-11-04T13:41:54.079Z" },
    { url = "https://files.pythonhosted.org/packages/5c/96/5fb7d8c3c17bc8c62fdb031c47d77a1af698f1d7a406b0f79aaa1338f9ad/pydantic_core-2.41.5-cp314-cp314t-win32.whl", hash = "sha256:b4ececa40ac28afa90871c2cc2b9ffd2ff0bf749380fbdf57d165fd23da353aa", size = 1988906, upload-time = "2025-11-04T13:41:56.606Z" },
    { url = "https://files.pythonhosted.org/packages/22/ed/182129d83032702912c2e2d8bbe33c036f342cc735737064668585dac28f/pydantic_core-2.41.5-cp314-cp314t-win_amd64.whl", hash = "sha256:80aa89cad80b32a912a65332f64a4450ed00966111b6615ca6816153d3585a8c", size = 1981607, upload-time = "2025-11-04T13:41:58.889Z" },
    { url = "https://files.pythonhosted.org/packages/9f/ed/068e41660b832bb0b1aa5b58011dea2a3fe0ba7861ff38c4d4904c1c1a99/pydantic_core-2.41.5-cp314-cp314t-win_arm64.whl", hash = "sha256:35b44f37a3199f771c3eaa53051bc8a70cd7b54f333531c59e29fd4db5d15008", size = 1974769, upload-time = "2025-11-04T13:42:01.186Z" },
    { url = "https://files.pythonhosted.org/packages/11/72/90fda5ee3b97e51c494938a4a44c3a35a9c96c19bba12372fb9c634d6f57/pydantic_core-2.41.5-graalpy311-graalpy242_311_native-macosx_10_12_x86_64.whl", hash = "sha256:b96d5f26b05d03cc60f11a7761a5ded1741da411e7fe0909e27a5e6a0cb7b034", size = 2115441, upload-time = "2025-11-04T13:42:39.557Z" },
    { url = "https://files.pythonhosted.org/packages/1f/53/8942f884fa33f50794f119012dc6a1a02ac43a56407adaac20463df8e98f/pydantic_core-2.41.5-graalpy311-graalpy242_311_native-macosx_11_0_arm64.whl", hash = "sha256:634e8609e89ceecea15e2d61bc9ac3718caaaa71963717bf3c8f38bfde64242c", size = 1930291, upload-time = "2025-11-04T13:42:42.169Z" },
    { url = "https://files.pythonhosted.org/packages/79/c8/ecb9ed9cd942bce09fc888ee960b52654fbdbede4ba6c2d6e0d3b1d8b49c/pydantic_core-2.41.5-graalpy311-graalpy242_311_native-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:93e8740d7503eb008aa2df04d3b9735f845d43ae845e6dcd2be0b55a2da43cd2", size = 1948632, upload-time = "2025-11-04T13:42:44.564Z" },
    { url = "https://files.pythonhosted.org/packages/2e/1b/687711069de7efa6af934e74f601e2a4307365e8fdc404703afc453eab26/pydantic_core-2.41.5-graalpy311-graalpy242_311_native-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:f15489ba13d61f670dcc96772e733aad1a6f9c429cc27574c6cdaed82d0146ad", size = 2138905, upload-time = "2025-11-04T13:42:47.156Z" },
    { url = "https://files.pythonhosted.org/packages/09/32/59b0c7e63e277fa7911c2fc70ccfb45ce4b98991e7ef37110663437005af/pydantic_core-2.41.5-graalpy312-graalpy250_312_native-macosx_10_12_x86_64.whl", hash = "sha256:7da7087d756b19037bc2c06edc6c170eeef3c3bafcb8f532ff17d64dc427adfd", size = 2110495, upload-time = "2025-11-04T13:42:49.689Z" },
    { url = "https://files.pythonhosted.org/packages/aa/81/05e400037eaf55ad400bcd318c05bb345b57e708887f07ddb2d20e3f0e98/pydantic_core-2.41.5-graalpy312-graalpy250_312_native-macosx_11_0_arm64.whl", hash = "sha256:aabf5777b5c8ca26f7824cb4a120a740c9588ed58df9b2d196ce92fba42ff8dc", size = 1915388, upload-time = "2025-11-04T13:42:52.215Z" },
    { url = "https://files.pythonhosted.org/packages/6e/0d/e3549b2399f71d56476b77dbf3cf8937cec5cd70536bdc0e374a421d0599/pydantic_core-2.41.5-graalpy312-graalpy250_312_native-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:c007fe8a43d43b3969e8469004e9845944f1a80e6acd47c150856bb87f230c56", size = 1942879, upload-time = "2025-11-04T13:42:56.483Z" },
    { url = "https://files.pythonhosted.org/packages/f7/07/34573da085946b6a313d7c42f82f16e8920bfd730665de2d11c0c37a74b5/pydantic_core-2.41.5-graalpy312-graalpy250_312_native-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:76d0819de158cd855d1cbb8fcafdf6f5cf1eb8e470abe056d5d161106e38062b", size = 2139017, upload-time = "2025-11-04T13:42:59.471Z" },
    { url = "https://files.pythonhosted.org/packages/e6/b0/1a2aa41e3b5a4ba11420aba2d091b2d17959c8d1519ece3627c371951e73/pydantic_core-2.41.5-pp310-pypy310_pp73-macosx_10_12_x86_64.whl", hash = "sha256:b5819cd790dbf0c5eb9f82c73c16b39a65dd6dd4d1439dcdea7816ec9adddab8", size = 2103351, upload-time = "2025-11-04T13:43:02.058Z" },
    { url = "https://files.pythonhosted.org/packages/a4/ee/31b1f0020baaf6d091c87900ae05c6aeae101fa4e188e1613c80e4f1ea31/pydantic_core-2.41.5-pp310-pypy310_pp73-macosx_11_0_arm64.whl", hash = "sha256:5a4e67afbc95fa5c34cf27d9089bca7fcab4e51e57278d710320a70b956d1b9a", size = 1925363, upload-time = "2025-11-04T13:43:05.159Z" },
    { url = "https://files.pythonhosted.org/packages/e1/89/ab8e86208467e467a80deaca4e434adac37b10a9d134cd2f99b28a01e483/pydantic_core-2.41.5-pp310-pypy310_pp73-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:ece5c59f0ce7d001e017643d8d24da587ea1f74f6993467d85ae8a5ef9d4f42b", size = 2135615, upload-time = "2025-11-04T13:43:08.116Z" },
    { url = "https://files.pythonhosted.org/packages/99/0a/99a53d06dd0348b2008f2f30884b34719c323f16c3be4e6cc1203b74a91d/pydantic_core-2.41.5-pp310-pypy310_pp73-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:16f80f7abe3351f8ea6858914ddc8c77e02578544a0ebc15b4c2e1a0e813b0b2", size = 2175369, upload-time = "2025-11-04T13:43:12.49Z" },
    { url = "https://files.pythonhosted.org/packages/6d/94/30ca3b73c6d485b9bb0bc66e611cff4a7138ff9736b7e66bcf0852151636/pydantic_core-2.41.5-pp310-pypy310_pp73-musllinux_1_1_aarch64.whl", hash = "sha256:33cb885e759a705b426baada1fe68cbb0a2e68e34c5d0d0289a364cf01709093", size = 2144218, upload-time = "2025-11-04T13:43:15.431Z" },
    { url = "https://files.pythonhosted.org/packages/87/57/31b4f8e12680b739a91f472b5671294236b82586889ef764b5fbc6669238/pydantic_core-2.41.5-pp310-pypy310_pp73-musllinux_1_1_armv7l.whl", hash = "sha256:c8d8b4eb992936023be7dee581270af5c6e0697a8559895f527f5b7105ecd36a", size = 2329951, upload-time = "2025-11-04T13:43:18.062Z" },
    { url = "https://files.pythonhosted.org/packages/7d/73/3c2c8edef77b8f7310e6fb012dbc4b8551386ed575b9eb6fb2506e28a7eb/pydantic_core-2.41.5-pp310-pypy310_pp73-musllinux_1_1_x86_64.whl", hash = "sha256:242a206cd0318f95cd21bdacff3fcc3aab23e79bba5cac3db5a841c9ef9c6963", size = 2318428, upload-time = "2025-11-04T13:43:20.679Z" },
    { url = "https://files.pythonhosted.org/packages/2f/02/8559b1f26ee0d502c74f9cca5c0d2fd97e967e083e006bbbb4e97f3a043a/pydantic_core-2.41.5-pp310-pypy310_pp73-win_amd64.whl", hash = "sha256:d3a978c4f57a597908b7e697229d996d77a6d3c94901e9edee593adada95ce1a", size = 2147009, upload-time = "2025-11-04T13:43:23.286Z" },
    { url = "https://files.pythonhosted.org/packages/5f/9b/1b3f0e9f9305839d7e84912f9e8bfbd191ed1b1ef48083609f0dabde978c/pydantic_core-2.41.5-pp311-pypy311_pp73-macosx_10_12_x86_64.whl", hash = "sha256:b2379fa7ed44ddecb5bfe4e48577d752db9fc10be00a6b7446e9663ba143de26", size = 2101980, upload-time = "2025-11-04T13:43:25.97Z" },
    { url = "https://files.pythonhosted.org/packages/a4/ed/d71fefcb4263df0da6a85b5d8a7508360f2f2e9b3bf5814be9c8bccdccc1/pydantic_core-2.41.5-pp311-pypy311_pp73-macosx_11_0_arm64.whl", hash = "sha256:266fb4cbf5e3cbd0b53669a6d1b039c45e3ce651fd5442eff4d07c2cc8d66808", size = 1923865, upload-time = "2025-11-04T13:43:28.763Z" },
    { url = "https://files.pythonhosted.org/packages/ce/3a/626b38db460d675f873e4444b4bb030453bbe7b4ba55df821d026a0493c4/pydantic_core-2.41.5-pp311-pypy311_pp73-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:58133647260ea01e4d0500089a8c4f07bd7aa6ce109682b1426394988d8aaacc", size = 2134256, upload-time = "2025-11-04T13:43:31.71Z" },
    { url = "https://files.pythonhosted.org/packages/83/d9/8412d7f06f616bbc053d30cb4e5f76786af3221462ad5eee1f202021eb4e/pydantic_core-2.41.5-pp311-pypy311_pp73-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:287dad91cfb551c363dc62899a80e9e14da1f0e2b6ebde82c806612ca2a13ef1", size = 2174762, upload-time = "2025-11-04T13:43:34.744Z" },
    { url = "https://files.pythonhosted.org/packages/55/4c/162d906b8e3ba3a99354e20faa1b49a85206c47de97a639510a0e673f5da/pydantic_core-2.41.5-pp311-pypy311_pp73-musllinux_1_1_aarch64.whl", hash = "sha256:03b77d184b9eb40240ae9fd676ca364ce1085f203e1b1256f8ab9984dca80a84", size = 2143141, upload-time = "2025-11-04T13:43:37.701Z" },
    { url = "https://files.pythonhosted.org/packages/1f/f2/f11dd73284122713f5f89fc940f370d035fa8e1e078d446b3313955157fe/pydantic_core-2.41.5-pp311-pypy311_pp73-musllinux_1_1_armv7l.whl", hash = "sha256:a668ce24de96165bb239160b3d854943128f4334822900534f2fe947930e5770", size = 2330317, upload-time = "2025-11-04T13:43:40.406Z" },
    { url = "https://files.pythonhosted.org/packages/88/9d/b06ca6acfe4abb296110fb1273a4d848a0bfb2ff65f3ee92127b3244e16b/pydantic_core-2.41.5-pp311-pypy311_pp73-musllinux_1_1_x86_64.whl", hash = "sha256:f14f8f046c14563f8eb3f45f499cc658ab8d10072961e07225e507adb700e93f", size = 2316992, upload-time = "2025-11-04T13:43:43.602Z" },
    { url = "https://files.pythonhosted.org/packages/36/c7/cfc8e811f061c841d7990b0201912c3556bfeb99cdcb7ed24adc8d6f8704/pydantic_core-2.41.5-pp311-pypy311_pp73-win_amd64.whl", hash = "sha256:56121965f7a4dc965bff783d70b907ddf3d57f6eba29b6d2e5dabfaf07799c51", size = 2145302, upload-time = "2025-11-04T13:43:46.64Z" },
]

[[package]]
name = "python-dotenv"
version = "1.2.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/82/ed/0301aeeac3e5353ef3d94b6ec08bbcabd04a72018415dcb29e588514bba8/python_dotenv-1.2.2.tar.gz", hash = "sha256:2c371a91fbd7ba082c2c1dc1f8bf89ca22564a087c2c287cd9b662adde799cf3", size = 50135, upload-time = "2026-03-01T16:00:26.196Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/0b/d7/1959b9648791274998a9c3526f6d0ec8fd2233e4d4acce81bbae76b44b2a/python_dotenv-1.2.2-py3-none-any.whl", hash = "sha256:1d8214789a24de455a8b8bd8ae6fe3c6b69a5e3d64aa8a8e5d68e694bbcb285a", size = 22101, upload-time = "2026-03-01T16:00:25.09Z" },
]

[[package]]
name = "sniffio"
version = "1.3.1"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/a2/87/a6771e1546d97e7e041b6ae58d80074f81b7d5121207425c964ddf5cfdbd/sniffio-1.3.1.tar.gz", hash = "sha256:f4324edc670a0f49750a81b895f35c3adb843cca46f0530f79fc1babb23789dc", size = 20372, upload-time = "2024-02-25T23:20:04.057Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/e9/44/75a9c9421471a6c4805dbf2356f7c181a29c1879239abab1ea2cc8f38b40/sniffio-1.3.1-py3-none-any.whl", hash = "sha256:2f6da418d1f1e0fddd844478f41680e794e6051915791a034ff65e5f100525a2", size = 10235, upload-time = "2024-02-25T23:20:01.196Z" },
]

[[package]]
name = "tqdm"
version = "4.67.3"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "colorama", marker = "sys_platform == 'win32'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/09/a9/6ba95a270c6f1fbcd8dac228323f2777d886cb206987444e4bce66338dd4/tqdm-4.67.3.tar.gz", hash = "sha256:7d825f03f89244ef73f1d4ce193cb1774a8179fd96f31d7e1dcde62092b960bb", size = 169598, upload-time = "2026-02-03T17:35:53.048Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/16/e1/3079a9ff9b8e11b846c6ac5c8b5bfb7ff225eee721825310c91b3b50304f/tqdm-4.67.3-py3-none-any.whl", hash = "sha256:ee1e4c0e59148062281c49d80b25b67771a127c85fc9676d3be5f243206826bf", size = 78374, upload-time = "2026-02-03T17:35:50.982Z" },
]

[[package]]
name = "typing-extensions"
version = "4.15.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/72/94/1a15dd82efb362ac84269196e94cf00f187f7ed21c242792a923cdb1c61f/typing_extensions-4.15.0.tar.gz", hash = "sha256:0cea48d173cc12fa28ecabc3b837ea3cf6f38c6d1136f85cbaaf598984861466", size = 109391, upload-time = "2025-08-25T13:49:26.313Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/18/67/36e9267722cc04a6b9f15c7f3441c2363321a3ea07da7ae0c0707beb2a9c/typing_extensions-4.15.0-py3-none-any.whl", hash = "sha256:f0fa19c6845758ab08074a0cfa8b7aecb71c999ca73d62883bc25cc018c4e548", size = 44614, upload-time = "2025-08-25T13:49:24.86Z" },
]

[[package]]
name = "typing-inspection"
version = "0.4.2"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "typing-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/55/e3/70399cb7dd41c10ac53367ae42139cf4b1ca5f36bb3dc6c9d33acdb43655/typing_inspection-0.4.2.tar.gz", hash = "sha256:ba561c48a67c5958007083d386c3295464928b01faa735ab8547c5692e87f464", size = 75949, upload-time = "2025-10-01T02:14:41.687Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/dc/9b/47798a6c91d8bdb567fe2698fe81e0c6b7cb7ef4d13da4114b41d239f65d/typing_inspection-0.4.2-py3-none-any.whl", hash = "sha256:4ed1cacbdc298c220f1bd249ed5287caa16f34d44ef4e9c3d0cbad5b521545e7", size = 14611, upload-time = "2025-10-01T02:14:40.154Z" },
]

[[package]]
name = "urllib3"
version = "2.6.3"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/c7/24/5f1b3bdffd70275f6661c76461e25f024d5a38a46f04aaca912426a2b1d3/urllib3-2.6.3.tar.gz", hash = "sha256:1b62b6884944a57dbe321509ab94fd4d3b307075e0c2eae991ac71ee15ad38ed", size = 435556, upload-time = "2026-01-07T16:24:43.925Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/39/08/aaaad47bc4e9dc8c725e68f9d04865dbcb2052843ff09c97b08904852d84/urllib3-2.6.3-py3-none-any.whl", hash = "sha256:bf272323e553dfb2e87d9bfd225ca7b0f467b919d7bbd355436d3fd37cb0acd4", size = 131584, upload-time = "2026-01-07T16:24:42.685Z" },
]
```

## File: `python/openai-agent-artifacts/.env.example`
```
OPENAI_API_KEY=
OPENAI_BASE_URL=
OPENAI_MODEL=

# Acontext API Configuration
ACONTEXT_API_KEY=sk-ac-your-root-api-bearer-token
ACONTEXT_BASE_URL=http://localhost:8029/api/v1
```

## File: `python/openai-agent-artifacts/.gitignore`
```
# Environment variables
.env
.env.local
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environments
venv/
env/
ENV/
.venv

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db
```

## File: `python/openai-agent-artifacts/README.md`
```markdown
# OpenAI ReAct Agent Demo

Minimal async ReAct-style agent that uses the OpenAI Python SDK plus the Acontext
Disk Tools to demonstrate tool-calling (write, read, replace, list).

## Prerequisites
- Python 3.11+ (project uses `uv` but regular `pip` also works)
- OpenAI API key with access to the specified model
- Acontext API key (and optional base URL for self-hosted setups)

## Setup
1. `cd Acontext-Examples/python/openai_artifacts_agent`
2. Copy `.env.example` to `.env` and fill in:
   ```
   OPENAI_API_KEY=...
   OPENAI_MODEL=gpt-4o-mini
   OPENAI_BASE_URL=https://api.openai.com/v1
   ACONTEXT_API_KEY=...
   ACONTEXT_BASE_URL=http://localhost:8029/api/v1
   ```
3. Install dependencies:
   - With uv: `uv sync` (recommended)
   - With pip: `python -m venv .venv && .venv\Scripts\activate && pip install -e .`
   
   **Note**: This project requires `acontext>=0.1.0` for `DISK_TOOLS` support.

## Run the Demo
```
uv run python main.py
```
The agent will:
1. Create an Acontext disk automatically
2. Write `/notes/demo.txt` on the Acontext disk with a short tools summary
3. List the artifacts in `/notes/` directory
4. Read the file back to verify content
5. Use `replace_string` to modify content in the file

Console logs show each tool invocation and the final response.

## Repo Layout
```
agent/
  __init__.py        # exports AcontextArtifactAgent
  react.py           # AcontextArtifactAgent class with chat loop + tool call handling
  tools.py           # deprecated (now using DISK_TOOLS from SDK)
  disk.py            # deprecated (now using DISK_TOOLS from SDK)
  pretty_print.py    # console output formatting utilities
main.py              # demo entry point: creates disk and runs agent
```
## Troubleshooting
- Missing `.env` values → runtime `RuntimeError` when loading API keys.
- Disk errors → confirm `ACONTEXT_API_KEY` and the API server URL.

---

# OpenAI React Agent (Python)

This companion section explains how the demo is structured and how you can reuse the components in your own projects.

## Feature Highlights
- **Async execution**: `AsyncOpenAI` plus `asyncio` keep tool calls and model responses concurrent.
- **ReAct loop safeguards**: `max_turn` prevents infinite cycles during experimentation.
- **SDK-integrated tools**: Uses `DISK_TOOLS` from `acontext.agent.disk` for pre-built filesystem operations.
- **Artifact listing**: `list_artifacts` allows the agent to explore directory contents on the Acontext disk.
- **File manipulation**: `write_file`, `read_file`, and `replace_string` provide comprehensive file operations.
- **Custom OpenAI endpoint**: point `base_url` at proxies or private deployments when needed.
- **Explicit disk management**: Disk is created in `main.py` and tool context is passed to `AcontextArtifactAgent`.

## Quick Start

1. Install dependencies:
   ```bash
   uv sync
   ```
2. Create `.env` and supply keys:
   ```env
   OPENAI_API_KEY=sk-your-key
   OPENAI_BASE_URL=https://api.openai.com/v1  # optional
   ACONTEXT_API_KEY=sk-ac-your-root-api-bearer-token
   ACONTEXT_BASE_URL=http://localhost:8029/api/v1  # optional
   ```
3. Run the demo:
   ```bash
   uv run python main.py
   ```

> To reuse elsewhere, import `AcontextArtifactAgent` and use it as an async context manager:
> ```python
> from acontext import AcontextClient
> from acontext.agent.disk import DISK_TOOLS
> 
> client = AcontextClient(api_key=..., base_url=...)
> disk = client.disks.create()
> ctx = DISK_TOOLS.format_context(client, disk.id)
> 
> async with AcontextArtifactAgent(api_key=..., tool_context=ctx) as agent:
>     result = await agent.run(user_query)
> ```

## Code Structure

```text
agent/
  __init__.py         # exposes AcontextArtifactAgent
  react.py            # AcontextArtifactAgent class with ReAct loop orchestration
  tools.py            # deprecated (now using DISK_TOOLS from SDK)
  disk.py             # deprecated (now using DISK_TOOLS from SDK)
  pretty_print.py     # console output formatting utilities
main.py               # demo entry point: creates disk and runs agent
pyproject.toml        # dependency manifest (openai + python-dotenv)
README.md             # this guide
```

## Execution Flow

1. **Initialization** (`main.py`):
   - Load environment variables from `.env`
   - Create `AcontextClient` and create a new disk
   - Create tool context using `DISK_TOOLS.format_context(client, disk.id)`
   - Pass `tool_context` to `AcontextArtifactAgent` when initializing the agent

2. **Agent Setup** (`react.py`):
   - `AcontextArtifactAgent` is initialized as an async context manager
   - On context entry: Initialize `AsyncOpenAI` client
   - Get tool schemas using `DISK_TOOLS.to_openai_tool_schema()`
   - Initialize conversation with user query

3. **ReAct Loop**:
   - Send messages to OpenAI API with available tools from `DISK_TOOLS`
   - If model returns tool calls:
     - Execute each tool using `DISK_TOOLS.execute_tool()` wrapped in `asyncio.to_thread()`
     - Append tool results to conversation history
     - Print formatted tool call information using `pretty_print` utilities
   - Continue until model returns final answer or `max_turn` reached

4. **Tool Execution** (via `DISK_TOOLS`):
   - Tools automatically use the provided tool context (contains `disk_id`)
   - `write_file`: Creates/updates text files on Acontext disk
   - `read_file`: Reads file content with optional `line_offset` and `line_limit` parameters
   - `replace_string`: Finds and replaces text in files
   - `list_artifacts`: Lists files and directories in a specified path (requires `file_path` parameter)

This pattern demonstrates how to use the SDK's pre-built `DISK_TOOLS` with async OpenAI clients.

### How the Disk Tools Work
- All disk operations go through `DISK_TOOLS` from `acontext.agent.disk`, which provides pre-configured tools.
- Tool context is created using `DISK_TOOLS.format_context(client, disk.id)` and contains the client and disk ID.
- Tool schemas are generated via `DISK_TOOLS.to_openai_tool_schema()` which returns OpenAI-compatible tool definitions.
- `write_file` accepts `filename`, `content`, and optional `file_path` parameters for organizing files into directories.
- `read_file` accepts `filename`, optional `file_path`, `line_offset` (default 0), and `line_limit` (default 100) parameters.
- `replace_string` accepts `filename`, `old_string`, `new_string`, and optional `file_path` parameters.
- `list_artifacts` requires `file_path` parameter (e.g., `"/notes/"` or `"/"`).
- Tool execution is synchronous, so `asyncio.to_thread()` is used to run `DISK_TOOLS.execute_tool()` in a thread pool.


```

## File: `python/openai-agent-artifacts/main.py`
```python
"""Minimal async Acontext Artifact Agent using the OpenAI Python SDK."""
import asyncio
import os
import shutil
from pathlib import Path
from acontext import AcontextClient
from acontext.agent.disk import DISK_TOOLS
from dotenv import load_dotenv
from agent import AcontextArtifactAgent


async def main() -> None:
    env_path = Path(__file__).with_name(".env")
    load_dotenv(dotenv_path=env_path, override=True)
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("Please set OPENAI_API_KEY in the environment or .env file.")

    base_url = os.getenv("OPENAI_BASE_URL")
    print(base_url)
    print(api_key)

    # Create Acontext client and disk
    acontext_api_key = os.getenv("ACONTEXT_API_KEY")
    if not acontext_api_key:
        raise RuntimeError("Please set ACONTEXT_API_KEY in the environment or .env file.")
    acontext_base_url = os.getenv("ACONTEXT_BASE_URL", "http://localhost:8029/api/v1")
    client = AcontextClient(api_key=acontext_api_key, base_url=acontext_base_url)
    disk = client.disks.create()

    # Create tool context using DISK_TOOLS
    ctx = DISK_TOOLS.format_context(client, disk.id)

    print(f"Created disk with ID: {disk.id}")

    # Create a session to store the conversation
    session = client.sessions.create()
    print(f"Created session: {session.id}")

    user_query = (
        "Please create /notes/demo.txt with a short summary about your tools, "
        "then list the artifacts in /notes/ directory, "
        "read the file back to confirm it was written, "
        "and finally use replace_string to replace a word in the file."
    )

    # Store user message
    client.sessions.store_message(session_id=session.id, blob={"role": "user", "content": user_query})

    print("Starting agent execution...")
    print(f"Disk ID: {disk.id}")
    print(f"Model: {os.getenv('OPENAI_MODEL', 'gpt-4o-mini')}")
    print(f"Max Turns: 5")

    async with AcontextArtifactAgent(
        api_key=api_key,
        base_url=base_url,
        tool_context=ctx,
        model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"),
        max_turn=5,
    ) as agent:
        result = await agent.run(user_query)
        print("Agent completed successfully!")

    # Store assistant response
    client.sessions.store_message(session_id=session.id, blob={"role": "assistant", "content": "Agent completed the disk operations successfully."})

    # Create a learning space and trigger learning
    space = client.learning_spaces.create()
    client.learning_spaces.learn(space.id, session_id=session.id)
    print(f"\nCreated learning space: {space.id}")

    # Wait for learning to complete
    print("Waiting for learning to complete...")
    learn_result = client.learning_spaces.wait_for_learning(space.id, session_id=session.id)
    print(f"Learning status: {learn_result.status}")

    # List learned skills
    skills = client.learning_spaces.list_skills(space.id)
    print(f"\n=== Learned Skills ({len(skills)}) ===")
    for skill in skills:
        print(f"  - {skill.name}: {skill.description}")
        print(f"    files: {[f.path for f in skill.file_index]}")

    # Download all skill files
    download_dir = "./skills_output"
    if os.path.exists(download_dir):
        shutil.rmtree(download_dir)

    print(f"\nDownloading skills to {download_dir}/")
    for skill in skills:
        resp = client.skills.download(skill_id=skill.id, path=f"{download_dir}/{skill.name}")
        print(f"  {resp.name} -> {resp.dir_path}")
        for f in resp.files:
            print(f"    {f}")


if __name__ == "__main__":
    asyncio.run(main())

```

## File: `python/openai-agent-artifacts/pyproject.toml`
```
[project]
name = "openai-artifacts-agent"
version = "0.1.0"
description = "Async OpenAI React Agent example"
readme = "README.md"
requires-python = ">=3.10"
dependencies = [
    "acontext>=0.1.18",
    "openai>=1.51.0",
    "python-dotenv>=1.0.0",
]


```

## File: `python/openai-agent-artifacts/uv.lock`
```
version = 1
revision = 3
requires-python = ">=3.10"

[[package]]
name = "acontext"
version = "0.1.18"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "anthropic" },
    { name = "httpx" },
    { name = "openai" },
    { name = "pydantic" },
    { name = "urllib3" },
]
sdist = { url = "https://files.pythonhosted.org/packages/13/4a/65d6f2f58e03bbbd8a269337a4d99536d8d3f7e9406e70b824a730875dac/acontext-0.1.18.tar.gz", hash = "sha256:7b1e763753fc23f007b4777949095a2ccc6d1b2deac714fad01095619a181824", size = 46865, upload-time = "2026-03-10T05:08:42.095Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/8d/76/bf60d77ab00da4170e9f7dfe42458b87c36b03f24ed2baa8c904d7ed9b97/acontext-0.1.18-py3-none-any.whl", hash = "sha256:a8810fb00f2b75c3509b15df07ab9dfef35dcc785ac07fcd6104ce92446b2b6b", size = 68510, upload-time = "2026-03-10T05:08:41.033Z" },
]

[[package]]
name = "annotated-types"
version = "0.7.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/ee/67/531ea369ba64dcff5ec9c3402f9f51bf748cec26dde048a2f973a4eea7f5/annotated_types-0.7.0.tar.gz", hash = "sha256:aff07c09a53a08bc8cfccb9c85b05f1aa9a2a6f23728d790723543408344ce89", size = 16081, upload-time = "2024-05-20T21:33:25.928Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/78/b6/6307fbef88d9b5ee7421e68d78a9f162e0da4900bc5f5793f6d3d0e34fb8/annotated_types-0.7.0-py3-none-any.whl", hash = "sha256:1f02e8b43a8fbbc3f3e0d4f0f4bfc8131bcb4eebe8849b8e5c773f3a1c582a53", size = 13643, upload-time = "2024-05-20T21:33:24.1Z" },
]

[[package]]
name = "anthropic"
version = "0.84.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "anyio" },
    { name = "distro" },
    { name = "docstring-parser" },
    { name = "httpx" },
    { name = "jiter" },
    { name = "pydantic" },
    { name = "sniffio" },
    { name = "typing-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/04/ea/0869d6df9ef83dcf393aeefc12dd81677d091c6ffc86f783e51cf44062f2/anthropic-0.84.0.tar.gz", hash = "sha256:72f5f90e5aebe62dca316cb013629cfa24996b0f5a4593b8c3d712bc03c43c37", size = 539457, upload-time = "2026-02-25T05:22:38.54Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/64/ca/218fa25002a332c0aa149ba18ffc0543175998b1f65de63f6d106689a345/anthropic-0.84.0-py3-none-any.whl", hash = "sha256:861c4c50f91ca45f942e091d83b60530ad6d4f98733bfe648065364da05d29e7", size = 455156, upload-time = "2026-02-25T05:22:40.468Z" },
]

[[package]]
name = "anyio"
version = "4.12.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "exceptiongroup", marker = "python_full_version < '3.11'" },
    { name = "idna" },
    { name = "typing-extensions", marker = "python_full_version < '3.13'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/96/f0/5eb65b2bb0d09ac6776f2eb54adee6abe8228ea05b20a5ad0e4945de8aac/anyio-4.12.1.tar.gz", hash = "sha256:41cfcc3a4c85d3f05c932da7c26d0201ac36f72abd4435ba90d0464a3ffed703", size = 228685, upload-time = "2026-01-06T11:45:21.246Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/38/0e/27be9fdef66e72d64c0cdc3cc2823101b80585f8119b5c112c2e8f5f7dab/anyio-4.12.1-py3-none-any.whl", hash = "sha256:d405828884fc140aa80a3c667b8beed277f1dfedec42ba031bd6ac3db606ab6c", size = 113592, upload-time = "2026-01-06T11:45:19.497Z" },
]

[[package]]
name = "certifi"
version = "2026.2.25"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/af/2d/7bf41579a8986e348fa033a31cdd0e4121114f6bce2457e8876010b092dd/certifi-2026.2.25.tar.gz", hash = "sha256:e887ab5cee78ea814d3472169153c2d12cd43b14bd03329a39a9c6e2e80bfba7", size = 155029, upload-time = "2026-02-25T02:54:17.342Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/9a/3c/c17fb3ca2d9c3acff52e30b309f538586f9f5b9c9cf454f3845fc9af4881/certifi-2026.2.25-py3-none-any.whl", hash = "sha256:027692e4402ad994f1c42e52a4997a9763c646b73e4096e4d5d6db8af1d6f0fa", size = 153684, upload-time = "2026-02-25T02:54:15.766Z" },
]

[[package]]
name = "colorama"
version = "0.4.6"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/d8/53/6f443c9a4a8358a93a6792e2acffb9d9d5cb0a5cfd8802644b7b1c9a02e4/colorama-0.4.6.tar.gz", hash = "sha256:08695f5cb7ed6e0531a20572697297273c47b8cae5a63ffc6d6ed5c201be6e44", size = 27697, upload-time = "2022-10-25T02:36:22.414Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/d1/d6/3965ed04c63042e047cb6a3e6ed1a63a35087b6a609aa3a15ed8ac56c221/colorama-0.4.6-py2.py3-none-any.whl", hash = "sha256:4f1d9991f5acc0ca119f9d443620b77f9d6b33703e51011c16baf57afb285fc6", size = 25335, upload-time = "2022-10-25T02:36:20.889Z" },
]

[[package]]
name = "distro"
version = "1.9.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/fc/f8/98eea607f65de6527f8a2e8885fc8015d3e6f5775df186e443e0964a11c3/distro-1.9.0.tar.gz", hash = "sha256:2fa77c6fd8940f116ee1d6b94a2f90b13b5ea8d019b98bc8bafdcabcdd9bdbed", size = 60722, upload-time = "2023-12-24T09:54:32.31Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/12/b3/231ffd4ab1fc9d679809f356cebee130ac7daa00d6d6f3206dd4fd137e9e/distro-1.9.0-py3-none-any.whl", hash = "sha256:7bffd925d65168f85027d8da9af6bddab658135b840670a223589bc0c8ef02b2", size = 20277, upload-time = "2023-12-24T09:54:30.421Z" },
]

[[package]]
name = "docstring-parser"
version = "0.17.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/b2/9d/c3b43da9515bd270df0f80548d9944e389870713cc1fe2b8fb35fe2bcefd/docstring_parser-0.17.0.tar.gz", hash = "sha256:583de4a309722b3315439bb31d64ba3eebada841f2e2cee23b99df001434c912", size = 27442, upload-time = "2025-07-21T07:35:01.868Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/55/e2/2537ebcff11c1ee1ff17d8d0b6f4db75873e3b0fb32c2d4a2ee31ecb310a/docstring_parser-0.17.0-py3-none-any.whl", hash = "sha256:cf2569abd23dce8099b300f9b4fa8191e9582dda731fd533daf54c4551658708", size = 36896, upload-time = "2025-07-21T07:35:00.684Z" },
]

[[package]]
name = "exceptiongroup"
version = "1.3.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "typing-extensions", marker = "python_full_version < '3.13'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/50/79/66800aadf48771f6b62f7eb014e352e5d06856655206165d775e675a02c9/exceptiongroup-1.3.1.tar.gz", hash = "sha256:8b412432c6055b0b7d14c310000ae93352ed6754f70fa8f7c34141f91c4e3219", size = 30371, upload-time = "2025-11-21T23:01:54.787Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/8a/0e/97c33bf5009bdbac74fd2beace167cab3f978feb69cc36f1ef79360d6c4e/exceptiongroup-1.3.1-py3-none-any.whl", hash = "sha256:a7a39a3bd276781e98394987d3a5701d0c4edffb633bb7a5144577f82c773598", size = 16740, upload-time = "2025-11-21T23:01:53.443Z" },
]

[[package]]
name = "h11"
version = "0.16.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/01/ee/02a2c011bdab74c6fb3c75474d40b3052059d95df7e73351460c8588d963/h11-0.16.0.tar.gz", hash = "sha256:4e35b956cf45792e4caa5885e69fba00bdbc6ffafbfa020300e549b208ee5ff1", size = 101250, upload-time = "2025-04-24T03:35:25.427Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/04/4b/29cac41a4d98d144bf5f6d33995617b185d14b22401f75ca86f384e87ff1/h11-0.16.0-py3-none-any.whl", hash = "sha256:63cf8bbe7522de3bf65932fda1d9c2772064ffb3dae62d55932da54b31cb6c86", size = 37515, upload-time = "2025-04-24T03:35:24.344Z" },
]

[[package]]
name = "httpcore"
version = "1.0.9"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "certifi" },
    { name = "h11" },
]
sdist = { url = "https://files.pythonhosted.org/packages/06/94/82699a10bca87a5556c9c59b5963f2d039dbd239f25bc2a63907a05a14cb/httpcore-1.0.9.tar.gz", hash = "sha256:6e34463af53fd2ab5d807f399a9b45ea31c3dfa2276f15a2c3f00afff6e176e8", size = 85484, upload-time = "2025-04-24T22:06:22.219Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/7e/f5/f66802a942d491edb555dd61e3a9961140fd64c90bce1eafd741609d334d/httpcore-1.0.9-py3-none-any.whl", hash = "sha256:2d400746a40668fc9dec9810239072b40b4484b640a8c38fd654a024c7a1bf55", size = 78784, upload-time = "2025-04-24T22:06:20.566Z" },
]

[[package]]
name = "httpx"
version = "0.28.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "anyio" },
    { name = "certifi" },
    { name = "httpcore" },
    { name = "idna" },
]
sdist = { url = "https://files.pythonhosted.org/packages/b1/df/48c586a5fe32a0f01324ee087459e112ebb7224f646c0b5023f5e79e9956/httpx-0.28.1.tar.gz", hash = "sha256:75e98c5f16b0f35b567856f597f06ff2270a374470a5c2392242528e3e3e42fc", size = 141406, upload-time = "2024-12-06T15:37:23.222Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/2a/39/e50c7c3a983047577ee07d2a9e53faf5a69493943ec3f6a384bdc792deb2/httpx-0.28.1-py3-none-any.whl", hash = "sha256:d909fcccc110f8c7faf814ca82a9a4d816bc5a6dbfea25d6591d6985b8ba59ad", size = 73517, upload-time = "2024-12-06T15:37:21.509Z" },
]

[[package]]
name = "idna"
version = "3.11"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/6f/6d/0703ccc57f3a7233505399edb88de3cbd678da106337b9fcde432b65ed60/idna-3.11.tar.gz", hash = "sha256:795dafcc9c04ed0c1fb032c2aa73654d8e8c5023a7df64a53f39190ada629902", size = 194582, upload-time = "2025-10-12T14:55:20.501Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/0e/61/66938bbb5fc52dbdf84594873d5b51fb1f7c7794e9c0f5bd885f30bc507b/idna-3.11-py3-none-any.whl", hash = "sha256:771a87f49d9defaf64091e6e6fe9c18d4833f140bd19464795bc32d966ca37ea", size = 71008, upload-time = "2025-10-12T14:55:18.883Z" },
]

[[package]]
name = "jiter"
version = "0.13.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/0d/5e/4ec91646aee381d01cdb9974e30882c9cd3b8c5d1079d6b5ff4af522439a/jiter-0.13.0.tar.gz", hash = "sha256:f2839f9c2c7e2dffc1bc5929a510e14ce0a946be9365fd1219e7ef342dae14f4", size = 164847, upload-time = "2026-02-02T12:37:56.441Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/d0/5a/41da76c5ea07bec1b0472b6b2fdb1b651074d504b19374d7e130e0cdfb25/jiter-0.13.0-cp310-cp310-macosx_10_12_x86_64.whl", hash = "sha256:2ffc63785fd6c7977defe49b9824ae6ce2b2e2b77ce539bdaf006c26da06342e", size = 311164, upload-time = "2026-02-02T12:35:17.688Z" },
    { url = "https://files.pythonhosted.org/packages/40/cb/4a1bf994a3e869f0d39d10e11efb471b76d0ad70ecbfb591427a46c880c2/jiter-0.13.0-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:4a638816427006c1e3f0013eb66d391d7a3acda99a7b0cf091eff4497ccea33a", size = 320296, upload-time = "2026-02-02T12:35:19.828Z" },
    { url = "https://files.pythonhosted.org/packages/09/82/acd71ca9b50ecebadc3979c541cd717cce2fe2bc86236f4fa597565d8f1a/jiter-0.13.0-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:19928b5d1ce0ff8c1ee1b9bdef3b5bfc19e8304f1b904e436caf30bc15dc6cf5", size = 352742, upload-time = "2026-02-02T12:35:21.258Z" },
    { url = "https://files.pythonhosted.org/packages/71/03/d1fc996f3aecfd42eb70922edecfb6dd26421c874503e241153ad41df94f/jiter-0.13.0-cp310-cp310-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:309549b778b949d731a2f0e1594a3f805716be704a73bf3ad9a807eed5eb5721", size = 363145, upload-time = "2026-02-02T12:35:24.653Z" },
    { url = "https://files.pythonhosted.org/packages/f1/61/a30492366378cc7a93088858f8991acd7d959759fe6138c12a4644e58e81/jiter-0.13.0-cp310-cp310-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:bcdabaea26cb04e25df3103ce47f97466627999260290349a88c8136ecae0060", size = 487683, upload-time = "2026-02-02T12:35:26.162Z" },
    { url = "https://files.pythonhosted.org/packages/20/4e/4223cffa9dbbbc96ed821c5aeb6bca510848c72c02086d1ed3f1da3d58a7/jiter-0.13.0-cp310-cp310-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:a3a377af27b236abbf665a69b2bdd680e3b5a0bd2af825cd3b81245279a7606c", size = 373579, upload-time = "2026-02-02T12:35:27.582Z" },
    { url = "https://files.pythonhosted.org/packages/fe/c9/b0489a01329ab07a83812d9ebcffe7820a38163c6d9e7da644f926ff877c/jiter-0.13.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:fe49d3ff6db74321f144dff9addd4a5874d3105ac5ba7c5b77fac099cfae31ae", size = 362904, upload-time = "2026-02-02T12:35:28.925Z" },
    { url = "https://files.pythonhosted.org/packages/05/af/53e561352a44afcba9a9bc67ee1d320b05a370aed8df54eafe714c4e454d/jiter-0.13.0-cp310-cp310-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:2113c17c9a67071b0f820733c0893ed1d467b5fcf4414068169e5c2cabddb1e2", size = 392380, upload-time = "2026-02-02T12:35:30.385Z" },
    { url = "https://files.pythonhosted.org/packages/76/2a/dd805c3afb8ed5b326c5ae49e725d1b1255b9754b1b77dbecdc621b20773/jiter-0.13.0-cp310-cp310-musllinux_1_1_aarch64.whl", hash = "sha256:ab1185ca5c8b9491b55ebf6c1e8866b8f68258612899693e24a92c5fdb9455d5", size = 517939, upload-time = "2026-02-02T12:35:31.865Z" },
    { url = "https://files.pythonhosted.org/packages/20/2a/7b67d76f55b8fe14c937e7640389612f05f9a4145fc28ae128aaa5e62257/jiter-0.13.0-cp310-cp310-musllinux_1_1_x86_64.whl", hash = "sha256:9621ca242547edc16400981ca3231e0c91c0c4c1ab8573a596cd9bb3575d5c2b", size = 551696, upload-time = "2026-02-02T12:35:33.306Z" },
    { url = "https://files.pythonhosted.org/packages/85/9c/57cdd64dac8f4c6ab8f994fe0eb04dc9fd1db102856a4458fcf8a99dfa62/jiter-0.13.0-cp310-cp310-win32.whl", hash = "sha256:a7637d92b1c9d7a771e8c56f445c7f84396d48f2e756e5978840ecba2fac0894", size = 204592, upload-time = "2026-02-02T12:35:34.58Z" },
    { url = "https://files.pythonhosted.org/packages/a7/38/f4f3ea5788b8a5bae7510a678cdc747eda0c45ffe534f9878ff37e7cf3b3/jiter-0.13.0-cp310-cp310-win_amd64.whl", hash = "sha256:c1b609e5cbd2f52bb74fb721515745b407df26d7b800458bd97cb3b972c29e7d", size = 206016, upload-time = "2026-02-02T12:35:36.435Z" },
    { url = "https://files.pythonhosted.org/packages/71/29/499f8c9eaa8a16751b1c0e45e6f5f1761d180da873d417996cc7bddc8eef/jiter-0.13.0-cp311-cp311-macosx_10_12_x86_64.whl", hash = "sha256:ea026e70a9a28ebbdddcbcf0f1323128a8db66898a06eaad3a4e62d2f554d096", size = 311157, upload-time = "2026-02-02T12:35:37.758Z" },
    { url = "https://files.pythonhosted.org/packages/50/f6/566364c777d2ab450b92100bea11333c64c38d32caf8dc378b48e5b20c46/jiter-0.13.0-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:66aa3e663840152d18cc8ff1e4faad3dd181373491b9cfdc6004b92198d67911", size = 319729, upload-time = "2026-02-02T12:35:39.246Z" },
    { url = "https://files.pythonhosted.org/packages/73/dd/560f13ec5e4f116d8ad2658781646cca91b617ae3b8758d4a5076b278f70/jiter-0.13.0-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:c3524798e70655ff19aec58c7d05adb1f074fecff62da857ea9be2b908b6d701", size = 354766, upload-time = "2026-02-02T12:35:40.662Z" },
    { url = "https://files.pythonhosted.org/packages/7c/0d/061faffcfe94608cbc28a0d42a77a74222bdf5055ccdbe5fd2292b94f510/jiter-0.13.0-cp311-cp311-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:ec7e287d7fbd02cb6e22f9a00dd9c9cd504c40a61f2c61e7e1f9690a82726b4c", size = 362587, upload-time = "2026-02-02T12:35:42.025Z" },
    { url = "https://files.pythonhosted.org/packages/92/c9/c66a7864982fd38a9773ec6e932e0398d1262677b8c60faecd02ffb67bf3/jiter-0.13.0-cp311-cp311-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:47455245307e4debf2ce6c6e65a717550a0244231240dcf3b8f7d64e4c2f22f4", size = 487537, upload-time = "2026-02-02T12:35:43.459Z" },
    { url = "https://files.pythonhosted.org/packages/6c/86/84eb4352cd3668f16d1a88929b5888a3fe0418ea8c1dfc2ad4e7bf6e069a/jiter-0.13.0-cp311-cp311-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:ee9da221dca6e0429c2704c1b3655fe7b025204a71d4d9b73390c759d776d165", size = 373717, upload-time = "2026-02-02T12:35:44.928Z" },
    { url = "https://files.pythonhosted.org/packages/6e/09/9fe4c159358176f82d4390407a03f506a8659ed13ca3ac93a843402acecf/jiter-0.13.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:24ab43126d5e05f3d53a36a8e11eb2f23304c6c1117844aaaf9a0aa5e40b5018", size = 362683, upload-time = "2026-02-02T12:35:46.636Z" },
    { url = "https://files.pythonhosted.org/packages/c9/5e/85f3ab9caca0c1d0897937d378b4a515cae9e119730563572361ea0c48ae/jiter-0.13.0-cp311-cp311-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:9da38b4fedde4fb528c740c2564628fbab737166a0e73d6d46cb4bb5463ff411", size = 392345, upload-time = "2026-02-02T12:35:48.088Z" },
    { url = "https://files.pythonhosted.org/packages/12/4c/05b8629ad546191939e6f0c2f17e29f542a398f4a52fb987bc70b6d1eb8b/jiter-0.13.0-cp311-cp311-musllinux_1_1_aarch64.whl", hash = "sha256:0b34c519e17658ed88d5047999a93547f8889f3c1824120c26ad6be5f27b6cf5", size = 517775, upload-time = "2026-02-02T12:35:49.482Z" },
    { url = "https://files.pythonhosted.org/packages/4d/88/367ea2eb6bc582c7052e4baf5ddf57ebe5ab924a88e0e09830dfb585c02d/jiter-0.13.0-cp311-cp311-musllinux_1_1_x86_64.whl", hash = "sha256:d2a6394e6af690d462310a86b53c47ad75ac8c21dc79f120714ea449979cb1d3", size = 551325, upload-time = "2026-02-02T12:35:51.104Z" },
    { url = "https://files.pythonhosted.org/packages/f3/12/fa377ffb94a2f28c41afaed093e0d70cfe512035d5ecb0cad0ae4792d35e/jiter-0.13.0-cp311-cp311-win32.whl", hash = "sha256:0f0c065695f616a27c920a56ad0d4fc46415ef8b806bf8fc1cacf25002bd24e1", size = 204709, upload-time = "2026-02-02T12:35:52.467Z" },
    { url = "https://files.pythonhosted.org/packages/cb/16/8e8203ce92f844dfcd3d9d6a5a7322c77077248dbb12da52d23193a839cd/jiter-0.13.0-cp311-cp311-win_amd64.whl", hash = "sha256:0733312953b909688ae3c2d58d043aa040f9f1a6a75693defed7bc2cc4bf2654", size = 204560, upload-time = "2026-02-02T12:35:53.925Z" },
    { url = "https://files.pythonhosted.org/packages/44/26/97cc40663deb17b9e13c3a5cf29251788c271b18ee4d262c8f94798b8336/jiter-0.13.0-cp311-cp311-win_arm64.whl", hash = "sha256:5d9b34ad56761b3bf0fbe8f7e55468704107608512350962d3317ffd7a4382d5", size = 189608, upload-time = "2026-02-02T12:35:55.304Z" },
    { url = "https://files.pythonhosted.org/packages/2e/30/7687e4f87086829955013ca12a9233523349767f69653ebc27036313def9/jiter-0.13.0-cp312-cp312-macosx_10_12_x86_64.whl", hash = "sha256:0a2bd69fc1d902e89925fc34d1da51b2128019423d7b339a45d9e99c894e0663", size = 307958, upload-time = "2026-02-02T12:35:57.165Z" },
    { url = "https://files.pythonhosted.org/packages/c3/27/e57f9a783246ed95481e6749cc5002a8a767a73177a83c63ea71f0528b90/jiter-0.13.0-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:f917a04240ef31898182f76a332f508f2cc4b57d2b4d7ad2dbfebbfe167eb505", size = 318597, upload-time = "2026-02-02T12:35:58.591Z" },
    { url = "https://files.pythonhosted.org/packages/cf/52/e5719a60ac5d4d7c5995461a94ad5ef962a37c8bf5b088390e6fad59b2ff/jiter-0.13.0-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:c1e2b199f446d3e82246b4fd9236d7cb502dc2222b18698ba0d986d2fecc6152", size = 348821, upload-time = "2026-02-02T12:36:00.093Z" },
    { url = "https://files.pythonhosted.org/packages/61/db/c1efc32b8ba4c740ab3fc2d037d8753f67685f475e26b9d6536a4322bcdd/jiter-0.13.0-cp312-cp312-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:04670992b576fa65bd056dbac0c39fe8bd67681c380cb2b48efa885711d9d726", size = 364163, upload-time = "2026-02-02T12:36:01.937Z" },
    { url = "https://files.pythonhosted.org/packages/55/8a/fb75556236047c8806995671a18e4a0ad646ed255276f51a20f32dceaeec/jiter-0.13.0-cp312-cp312-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:5a1aff1fbdb803a376d4d22a8f63f8e7ccbce0b4890c26cc7af9e501ab339ef0", size = 483709, upload-time = "2026-02-02T12:36:03.41Z" },
    { url = "https://files.pythonhosted.org/packages/7e/16/43512e6ee863875693a8e6f6d532e19d650779d6ba9a81593ae40a9088ff/jiter-0.13.0-cp312-cp312-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:3b3fb8c2053acaef8580809ac1d1f7481a0a0bdc012fd7f5d8b18fb696a5a089", size = 370480, upload-time = "2026-02-02T12:36:04.791Z" },
    { url = "https://files.pythonhosted.org/packages/f8/4c/09b93e30e984a187bc8aaa3510e1ec8dcbdcd71ca05d2f56aac0492453aa/jiter-0.13.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:bdaba7d87e66f26a2c45d8cbadcbfc4bf7884182317907baf39cfe9775bb4d93", size = 360735, upload-time = "2026-02-02T12:36:06.994Z" },
    { url = "https://files.pythonhosted.org/packages/1a/1b/46c5e349019874ec5dfa508c14c37e29864ea108d376ae26d90bee238cd7/jiter-0.13.0-cp312-cp312-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:7b88d649135aca526da172e48083da915ec086b54e8e73a425ba50999468cc08", size = 391814, upload-time = "2026-02-02T12:36:08.368Z" },
    { url = "https://files.pythonhosted.org/packages/15/9e/26184760e85baee7162ad37b7912797d2077718476bf91517641c92b3639/jiter-0.13.0-cp312-cp312-musllinux_1_1_aarch64.whl", hash = "sha256:e404ea551d35438013c64b4f357b0474c7abf9f781c06d44fcaf7a14c69ff9e2", size = 513990, upload-time = "2026-02-02T12:36:09.993Z" },
    { url = "https://files.pythonhosted.org/packages/e9/34/2c9355247d6debad57a0a15e76ab1566ab799388042743656e566b3b7de1/jiter-0.13.0-cp312-cp312-musllinux_1_1_x86_64.whl", hash = "sha256:1f4748aad1b4a93c8bdd70f604d0f748cdc0e8744c5547798acfa52f10e79228", size = 548021, upload-time = "2026-02-02T12:36:11.376Z" },
    { url = "https://files.pythonhosted.org/packages/ac/4a/9f2c23255d04a834398b9c2e0e665382116911dc4d06b795710503cdad25/jiter-0.13.0-cp312-cp312-win32.whl", hash = "sha256:0bf670e3b1445fc4d31612199f1744f67f889ee1bbae703c4b54dc097e5dd394", size = 203024, upload-time = "2026-02-02T12:36:12.682Z" },
    { url = "https://files.pythonhosted.org/packages/09/ee/f0ae675a957ae5a8f160be3e87acea6b11dc7b89f6b7ab057e77b2d2b13a/jiter-0.13.0-cp312-cp312-win_amd64.whl", hash = "sha256:15db60e121e11fe186c0b15236bd5d18381b9ddacdcf4e659feb96fc6c969c92", size = 205424, upload-time = "2026-02-02T12:36:13.93Z" },
    { url = "https://files.pythonhosted.org/packages/1b/02/ae611edf913d3cbf02c97cdb90374af2082c48d7190d74c1111dde08bcdd/jiter-0.13.0-cp312-cp312-win_arm64.whl", hash = "sha256:41f92313d17989102f3cb5dd533a02787cdb99454d494344b0361355da52fcb9", size = 186818, upload-time = "2026-02-02T12:36:15.308Z" },
    { url = "https://files.pythonhosted.org/packages/91/9c/7ee5a6ff4b9991e1a45263bfc46731634c4a2bde27dfda6c8251df2d958c/jiter-0.13.0-cp313-cp313-macosx_10_12_x86_64.whl", hash = "sha256:1f8a55b848cbabf97d861495cd65f1e5c590246fabca8b48e1747c4dfc8f85bf", size = 306897, upload-time = "2026-02-02T12:36:16.748Z" },
    { url = "https://files.pythonhosted.org/packages/7c/02/be5b870d1d2be5dd6a91bdfb90f248fbb7dcbd21338f092c6b89817c3dbf/jiter-0.13.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:f556aa591c00f2c45eb1b89f68f52441a016034d18b65da60e2d2875bbbf344a", size = 317507, upload-time = "2026-02-02T12:36:18.351Z" },
    { url = "https://files.pythonhosted.org/packages/da/92/b25d2ec333615f5f284f3a4024f7ce68cfa0604c322c6808b2344c7f5d2b/jiter-0.13.0-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:f7e1d61da332ec412350463891923f960c3073cf1aae93b538f0bb4c8cd46efb", size = 350560, upload-time = "2026-02-02T12:36:19.746Z" },
    { url = "https://files.pythonhosted.org/packages/be/ec/74dcb99fef0aca9fbe56b303bf79f6bd839010cb18ad41000bf6cc71eec0/jiter-0.13.0-cp313-cp313-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:3097d665a27bc96fd9bbf7f86178037db139f319f785e4757ce7ccbf390db6c2", size = 363232, upload-time = "2026-02-02T12:36:21.243Z" },
    { url = "https://files.pythonhosted.org/packages/1b/37/f17375e0bb2f6a812d4dd92d7616e41917f740f3e71343627da9db2824ce/jiter-0.13.0-cp313-cp313-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:9d01ecc3a8cbdb6f25a37bd500510550b64ddf9f7d64a107d92f3ccb25035d0f", size = 483727, upload-time = "2026-02-02T12:36:22.688Z" },
    { url = "https://files.pythonhosted.org/packages/77/d2/a71160a5ae1a1e66c1395b37ef77da67513b0adba73b993a27fbe47eb048/jiter-0.13.0-cp313-cp313-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:ed9bbc30f5d60a3bdf63ae76beb3f9db280d7f195dfcfa61af792d6ce912d159", size = 370799, upload-time = "2026-02-02T12:36:24.106Z" },
    { url = "https://files.pythonhosted.org/packages/01/99/ed5e478ff0eb4e8aa5fd998f9d69603c9fd3f32de3bd16c2b1194f68361c/jiter-0.13.0-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:98fbafb6e88256f4454de33c1f40203d09fc33ed19162a68b3b257b29ca7f663", size = 359120, upload-time = "2026-02-02T12:36:25.519Z" },
    { url = "https://files.pythonhosted.org/packages/16/be/7ffd08203277a813f732ba897352797fa9493faf8dc7995b31f3d9cb9488/jiter-0.13.0-cp313-cp313-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:5467696f6b827f1116556cb0db620440380434591e93ecee7fd14d1a491b6daa", size = 390664, upload-time = "2026-02-02T12:36:26.866Z" },
    { url = "https://files.pythonhosted.org/packages/d1/84/e0787856196d6d346264d6dcccb01f741e5f0bd014c1d9a2ebe149caf4f3/jiter-0.13.0-cp313-cp313-musllinux_1_1_aarch64.whl", hash = "sha256:2d08c9475d48b92892583df9da592a0e2ac49bcd41fae1fec4f39ba6cf107820", size = 513543, upload-time = "2026-02-02T12:36:28.217Z" },
    { url = "https://files.pythonhosted.org/packages/65/50/ecbd258181c4313cf79bca6c88fb63207d04d5bf5e4f65174114d072aa55/jiter-0.13.0-cp313-cp313-musllinux_1_1_x86_64.whl", hash = "sha256:aed40e099404721d7fcaf5b89bd3b4568a4666358bcac7b6b15c09fb6252ab68", size = 547262, upload-time = "2026-02-02T12:36:29.678Z" },
    { url = "https://files.pythonhosted.org/packages/27/da/68f38d12e7111d2016cd198161b36e1f042bd115c169255bcb7ec823a3bf/jiter-0.13.0-cp313-cp313-win32.whl", hash = "sha256:36ebfbcffafb146d0e6ffb3e74d51e03d9c35ce7c625c8066cdbfc7b953bdc72", size = 200630, upload-time = "2026-02-02T12:36:31.808Z" },
    { url = "https://files.pythonhosted.org/packages/25/65/3bd1a972c9a08ecd22eb3b08a95d1941ebe6938aea620c246cf426ae09c2/jiter-0.13.0-cp313-cp313-win_amd64.whl", hash = "sha256:8d76029f077379374cf0dbc78dbe45b38dec4a2eb78b08b5194ce836b2517afc", size = 202602, upload-time = "2026-02-02T12:36:33.679Z" },
    { url = "https://files.pythonhosted.org/packages/15/fe/13bd3678a311aa67686bb303654792c48206a112068f8b0b21426eb6851e/jiter-0.13.0-cp313-cp313-win_arm64.whl", hash = "sha256:bb7613e1a427cfcb6ea4544f9ac566b93d5bf67e0d48c787eca673ff9c9dff2b", size = 185939, upload-time = "2026-02-02T12:36:35.065Z" },
    { url = "https://files.pythonhosted.org/packages/49/19/a929ec002ad3228bc97ca01dbb14f7632fffdc84a95ec92ceaf4145688ae/jiter-0.13.0-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:fa476ab5dd49f3bf3a168e05f89358c75a17608dbabb080ef65f96b27c19ab10", size = 316616, upload-time = "2026-02-02T12:36:36.579Z" },
    { url = "https://files.pythonhosted.org/packages/52/56/d19a9a194afa37c1728831e5fb81b7722c3de18a3109e8f282bfc23e587a/jiter-0.13.0-cp313-cp313t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:ade8cb6ff5632a62b7dbd4757d8c5573f7a2e9ae285d6b5b841707d8363205ef", size = 346850, upload-time = "2026-02-02T12:36:38.058Z" },
    { url = "https://files.pythonhosted.org/packages/36/4a/94e831c6bf287754a8a019cb966ed39ff8be6ab78cadecf08df3bb02d505/jiter-0.13.0-cp313-cp313t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:9950290340acc1adaded363edd94baebcee7dabdfa8bee4790794cd5cfad2af6", size = 358551, upload-time = "2026-02-02T12:36:39.417Z" },
    { url = "https://files.pythonhosted.org/packages/a2/ec/a4c72c822695fa80e55d2b4142b73f0012035d9fcf90eccc56bc060db37c/jiter-0.13.0-cp313-cp313t-win_amd64.whl", hash = "sha256:2b4972c6df33731aac0742b64fd0d18e0a69bc7d6e03108ce7d40c85fd9e3e6d", size = 201950, upload-time = "2026-02-02T12:36:40.791Z" },
    { url = "https://files.pythonhosted.org/packages/b6/00/393553ec27b824fbc29047e9c7cd4a3951d7fbe4a76743f17e44034fa4e4/jiter-0.13.0-cp313-cp313t-win_arm64.whl", hash = "sha256:701a1e77d1e593c1b435315ff625fd071f0998c5f02792038a5ca98899261b7d", size = 185852, upload-time = "2026-02-02T12:36:42.077Z" },
    { url = "https://files.pythonhosted.org/packages/6e/f5/f1997e987211f6f9bd71b8083047b316208b4aca0b529bb5f8c96c89ef3e/jiter-0.13.0-cp314-cp314-macosx_10_12_x86_64.whl", hash = "sha256:cc5223ab19fe25e2f0bf2643204ad7318896fe3729bf12fde41b77bfc4fafff0", size = 308804, upload-time = "2026-02-02T12:36:43.496Z" },
    { url = "https://files.pythonhosted.org/packages/cd/8f/5482a7677731fd44881f0204981ce2d7175db271f82cba2085dd2212e095/jiter-0.13.0-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:9776ebe51713acf438fd9b4405fcd86893ae5d03487546dae7f34993217f8a91", size = 318787, upload-time = "2026-02-02T12:36:45.071Z" },
    { url = "https://files.pythonhosted.org/packages/f3/b9/7257ac59778f1cd025b26a23c5520a36a424f7f1b068f2442a5b499b7464/jiter-0.13.0-cp314-cp314-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:879e768938e7b49b5e90b7e3fecc0dbec01b8cb89595861fb39a8967c5220d09", size = 353880, upload-time = "2026-02-02T12:36:47.365Z" },
    { url = "https://files.pythonhosted.org/packages/c3/87/719eec4a3f0841dad99e3d3604ee4cba36af4419a76f3cb0b8e2e691ad67/jiter-0.13.0-cp314-cp314-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:682161a67adea11e3aae9038c06c8b4a9a71023228767477d683f69903ebc607", size = 366702, upload-time = "2026-02-02T12:36:48.871Z" },
    { url = "https://files.pythonhosted.org/packages/d2/65/415f0a75cf6921e43365a1bc227c565cb949caca8b7532776e430cbaa530/jiter-0.13.0-cp314-cp314-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:a13b68cd1cd8cc9de8f244ebae18ccb3e4067ad205220ef324c39181e23bbf66", size = 486319, upload-time = "2026-02-02T12:36:53.006Z" },
    { url = "https://files.pythonhosted.org/packages/54/a2/9e12b48e82c6bbc6081fd81abf915e1443add1b13d8fc586e1d90bb02bb8/jiter-0.13.0-cp314-cp314-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:87ce0f14c6c08892b610686ae8be350bf368467b6acd5085a5b65441e2bf36d2", size = 372289, upload-time = "2026-02-02T12:36:54.593Z" },
    { url = "https://files.pythonhosted.org/packages/4e/c1/e4693f107a1789a239c759a432e9afc592366f04e901470c2af89cfd28e1/jiter-0.13.0-cp314-cp314-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:0c365005b05505a90d1c47856420980d0237adf82f70c4aff7aebd3c1cc143ad", size = 360165, upload-time = "2026-02-02T12:36:56.112Z" },
    { url = "https://files.pythonhosted.org/packages/17/08/91b9ea976c1c758240614bd88442681a87672eebc3d9a6dde476874e706b/jiter-0.13.0-cp314-cp314-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:1317fdffd16f5873e46ce27d0e0f7f4f90f0cdf1d86bf6abeaea9f63ca2c401d", size = 389634, upload-time = "2026-02-02T12:36:57.495Z" },
    { url = "https://files.pythonhosted.org/packages/18/23/58325ef99390d6d40427ed6005bf1ad54f2577866594bcf13ce55675f87d/jiter-0.13.0-cp314-cp314-musllinux_1_1_aarch64.whl", hash = "sha256:c05b450d37ba0c9e21c77fef1f205f56bcee2330bddca68d344baebfc55ae0df", size = 514933, upload-time = "2026-02-02T12:36:58.909Z" },
    { url = "https://files.pythonhosted.org/packages/5b/25/69f1120c7c395fd276c3996bb8adefa9c6b84c12bb7111e5c6ccdcd8526d/jiter-0.13.0-cp314-cp314-musllinux_1_1_x86_64.whl", hash = "sha256:775e10de3849d0631a97c603f996f518159272db00fdda0a780f81752255ee9d", size = 548842, upload-time = "2026-02-02T12:37:00.433Z" },
    { url = "https://files.pythonhosted.org/packages/18/05/981c9669d86850c5fbb0d9e62bba144787f9fba84546ba43d624ee27ef29/jiter-0.13.0-cp314-cp314-win32.whl", hash = "sha256:632bf7c1d28421c00dd8bbb8a3bac5663e1f57d5cd5ed962bce3c73bf62608e6", size = 202108, upload-time = "2026-02-02T12:37:01.718Z" },
    { url = "https://files.pythonhosted.org/packages/8d/96/cdcf54dd0b0341db7d25413229888a346c7130bd20820530905fdb65727b/jiter-0.13.0-cp314-cp314-win_amd64.whl", hash = "sha256:f22ef501c3f87ede88f23f9b11e608581c14f04db59b6a801f354397ae13739f", size = 204027, upload-time = "2026-02-02T12:37:03.075Z" },
    { url = "https://files.pythonhosted.org/packages/fb/f9/724bcaaab7a3cd727031fe4f6995cb86c4bd344909177c186699c8dec51a/jiter-0.13.0-cp314-cp314-win_arm64.whl", hash = "sha256:07b75fe09a4ee8e0c606200622e571e44943f47254f95e2436c8bdcaceb36d7d", size = 187199, upload-time = "2026-02-02T12:37:04.414Z" },
    { url = "https://files.pythonhosted.org/packages/62/92/1661d8b9fd6a3d7a2d89831db26fe3c1509a287d83ad7838831c7b7a5c7e/jiter-0.13.0-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:964538479359059a35fb400e769295d4b315ae61e4105396d355a12f7fef09f0", size = 318423, upload-time = "2026-02-02T12:37:05.806Z" },
    { url = "https://files.pythonhosted.org/packages/4f/3b/f77d342a54d4ebcd128e520fc58ec2f5b30a423b0fd26acdfc0c6fef8e26/jiter-0.13.0-cp314-cp314t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:e104da1db1c0991b3eaed391ccd650ae8d947eab1480c733e5a3fb28d4313e40", size = 351438, upload-time = "2026-02-02T12:37:07.189Z" },
    { url = "https://files.pythonhosted.org/packages/76/b3/ba9a69f0e4209bd3331470c723c2f5509e6f0482e416b612431a5061ed71/jiter-0.13.0-cp314-cp314t-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:0e3a5f0cde8ff433b8e88e41aa40131455420fb3649a3c7abdda6145f8cb7202", size = 364774, upload-time = "2026-02-02T12:37:08.579Z" },
    { url = "https://files.pythonhosted.org/packages/b3/16/6cdb31fa342932602458dbb631bfbd47f601e03d2e4950740e0b2100b570/jiter-0.13.0-cp314-cp314t-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:57aab48f40be1db920a582b30b116fe2435d184f77f0e4226f546794cedd9cf0", size = 487238, upload-time = "2026-02-02T12:37:10.066Z" },
    { url = "https://files.pythonhosted.org/packages/ed/b1/956cc7abaca8d95c13aa8d6c9b3f3797241c246cd6e792934cc4c8b250d2/jiter-0.13.0-cp314-cp314t-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:7772115877c53f62beeb8fd853cab692dbc04374ef623b30f997959a4c0e7e95", size = 372892, upload-time = "2026-02-02T12:37:11.656Z" },
    { url = "https://files.pythonhosted.org/packages/26/c4/97ecde8b1e74f67b8598c57c6fccf6df86ea7861ed29da84629cdbba76c4/jiter-0.13.0-cp314-cp314t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:1211427574b17b633cfceba5040de8081e5abf114f7a7602f73d2e16f9fdaa59", size = 360309, upload-time = "2026-02-02T12:37:13.244Z" },
    { url = "https://files.pythonhosted.org/packages/4b/d7/eabe3cf46715854ccc80be2cd78dd4c36aedeb30751dbf85a1d08c14373c/jiter-0.13.0-cp314-cp314t-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:7beae3a3d3b5212d3a55d2961db3c292e02e302feb43fce6a3f7a31b90ea6dfe", size = 389607, upload-time = "2026-02-02T12:37:14.881Z" },
    { url = "https://files.pythonhosted.org/packages/df/2d/03963fc0804e6109b82decfb9974eb92df3797fe7222428cae12f8ccaa0c/jiter-0.13.0-cp314-cp314t-musllinux_1_1_aarch64.whl", hash = "sha256:e5562a0f0e90a6223b704163ea28e831bd3a9faa3512a711f031611e6b06c939", size = 514986, upload-time = "2026-02-02T12:37:16.326Z" },
    { url = "https://files.pythonhosted.org/packages/f6/6c/8c83b45eb3eb1c1e18d841fe30b4b5bc5619d781267ca9bc03e005d8fd0a/jiter-0.13.0-cp314-cp314t-musllinux_1_1_x86_64.whl", hash = "sha256:6c26a424569a59140fb51160a56df13f438a2b0967365e987889186d5fc2f6f9", size = 548756, upload-time = "2026-02-02T12:37:17.736Z" },
    { url = "https://files.pythonhosted.org/packages/47/66/eea81dfff765ed66c68fd2ed8c96245109e13c896c2a5015c7839c92367e/jiter-0.13.0-cp314-cp314t-win32.whl", hash = "sha256:24dc96eca9f84da4131cdf87a95e6ce36765c3b156fc9ae33280873b1c32d5f6", size = 201196, upload-time = "2026-02-02T12:37:19.101Z" },
    { url = "https://files.pythonhosted.org/packages/ff/32/4ac9c7a76402f8f00d00842a7f6b83b284d0cf7c1e9d4227bc95aa6d17fa/jiter-0.13.0-cp314-cp314t-win_amd64.whl", hash = "sha256:0a8d76c7524087272c8ae913f5d9d608bd839154b62c4322ef65723d2e5bb0b8", size = 204215, upload-time = "2026-02-02T12:37:20.495Z" },
    { url = "https://files.pythonhosted.org/packages/f9/8e/7def204fea9f9be8b3c21a6f2dd6c020cf56c7d5ff753e0e23ed7f9ea57e/jiter-0.13.0-cp314-cp314t-win_arm64.whl", hash = "sha256:2c26cf47e2cad140fa23b6d58d435a7c0161f5c514284802f25e87fddfe11024", size = 187152, upload-time = "2026-02-02T12:37:22.124Z" },
    { url = "https://files.pythonhosted.org/packages/79/b3/3c29819a27178d0e461a8571fb63c6ae38be6dc36b78b3ec2876bbd6a910/jiter-0.13.0-graalpy311-graalpy242_311_native-macosx_10_12_x86_64.whl", hash = "sha256:b1cbfa133241d0e6bdab48dcdc2604e8ba81512f6bbd68ec3e8e1357dd3c316c", size = 307016, upload-time = "2026-02-02T12:37:42.755Z" },
    { url = "https://files.pythonhosted.org/packages/eb/ae/60993e4b07b1ac5ebe46da7aa99fdbb802eb986c38d26e3883ac0125c4e0/jiter-0.13.0-graalpy311-graalpy242_311_native-macosx_11_0_arm64.whl", hash = "sha256:db367d8be9fad6e8ebbac4a7578b7af562e506211036cba2c06c3b998603c3d2", size = 305024, upload-time = "2026-02-02T12:37:44.774Z" },
    { url = "https://files.pythonhosted.org/packages/77/fa/2227e590e9cf98803db2811f172b2d6460a21539ab73006f251c66f44b14/jiter-0.13.0-graalpy311-graalpy242_311_native-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:45f6f8efb2f3b0603092401dc2df79fa89ccbc027aaba4174d2d4133ed661434", size = 339337, upload-time = "2026-02-02T12:37:46.668Z" },
    { url = "https://files.pythonhosted.org/packages/2d/92/015173281f7eb96c0ef580c997da8ef50870d4f7f4c9e03c845a1d62ae04/jiter-0.13.0-graalpy311-graalpy242_311_native-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:597245258e6ad085d064780abfb23a284d418d3e61c57362d9449c6c7317ee2d", size = 346395, upload-time = "2026-02-02T12:37:48.09Z" },
    { url = "https://files.pythonhosted.org/packages/80/60/e50fa45dd7e2eae049f0ce964663849e897300433921198aef94b6ffa23a/jiter-0.13.0-graalpy312-graalpy250_312_native-macosx_10_12_x86_64.whl", hash = "sha256:3d744a6061afba08dd7ae375dcde870cffb14429b7477e10f67e9e6d68772a0a", size = 305169, upload-time = "2026-02-02T12:37:50.376Z" },
    { url = "https://files.pythonhosted.org/packages/d2/73/a009f41c5eed71c49bec53036c4b33555afcdee70682a18c6f66e396c039/jiter-0.13.0-graalpy312-graalpy250_312_native-macosx_11_0_arm64.whl", hash = "sha256:ff732bd0a0e778f43d5009840f20b935e79087b4dc65bd36f1cd0f9b04b8ff7f", size = 303808, upload-time = "2026-02-02T12:37:52.092Z" },
    { url = "https://files.pythonhosted.org/packages/c4/10/528b439290763bff3d939268085d03382471b442f212dca4ff5f12802d43/jiter-0.13.0-graalpy312-graalpy250_312_native-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:ab44b178f7981fcaea7e0a5df20e773c663d06ffda0198f1a524e91b2fde7e59", size = 337384, upload-time = "2026-02-02T12:37:53.582Z" },
    { url = "https://files.pythonhosted.org/packages/67/8a/a342b2f0251f3dac4ca17618265d93bf244a2a4d089126e81e4c1056ac50/jiter-0.13.0-graalpy312-graalpy250_312_native-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:7bb00b6d26db67a05fe3e12c76edc75f32077fb51deed13822dc648fa373bc19", size = 343768, upload-time = "2026-02-02T12:37:55.055Z" },
]

[[package]]
name = "openai"
version = "2.26.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "anyio" },
    { name = "distro" },
    { name = "httpx" },
    { name = "jiter" },
    { name = "pydantic" },
    { name = "sniffio" },
    { name = "tqdm" },
    { name = "typing-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/d7/91/2a06c4e9597c338cac1e5e5a8dd6f29e1836fc229c4c523529dca387fda8/openai-2.26.0.tar.gz", hash = "sha256:b41f37c140ae0034a6e92b0c509376d907f3a66109935fba2c1b471a7c05a8fb", size = 666702, upload-time = "2026-03-05T23:17:35.874Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/c6/2e/3f73e8ca53718952222cacd0cf7eecc9db439d020f0c1fe7ae717e4e199a/openai-2.26.0-py3-none-any.whl", hash = "sha256:6151bf8f83802f036117f06cc8a57b3a4da60da9926826cc96747888b57f394f", size = 1136409, upload-time = "2026-03-05T23:17:34.072Z" },
]

[[package]]
name = "openai-artifacts-agent"
version = "0.1.0"
source = { virtual = "." }
dependencies = [
    { name = "acontext" },
    { name = "openai" },
    { name = "python-dotenv" },
]

[package.metadata]
requires-dist = [
    { name = "acontext", specifier = ">=0.1.18" },
    { name = "openai", specifier = ">=1.51.0" },
    { name = "python-dotenv", specifier = ">=1.0.0" },
]

[[package]]
name = "pydantic"
version = "2.12.5"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "annotated-types" },
    { name = "pydantic-core" },
    { name = "typing-extensions" },
    { name = "typing-inspection" },
]
sdist = { url = "https://files.pythonhosted.org/packages/69/44/36f1a6e523abc58ae5f928898e4aca2e0ea509b5aa6f6f392a5d882be928/pydantic-2.12.5.tar.gz", hash = "sha256:4d351024c75c0f085a9febbb665ce8c0c6ec5d30e903bdb6394b7ede26aebb49", size = 821591, upload-time = "2025-11-26T15:11:46.471Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/5a/87/b70ad306ebb6f9b585f114d0ac2137d792b48be34d732d60e597c2f8465a/pydantic-2.12.5-py3-none-any.whl", hash = "sha256:e561593fccf61e8a20fc46dfc2dfe075b8be7d0188df33f221ad1f0139180f9d", size = 463580, upload-time = "2025-11-26T15:11:44.605Z" },
]

[[package]]
name = "pydantic-core"
version = "2.41.5"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "typing-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/71/70/23b021c950c2addd24ec408e9ab05d59b035b39d97cdc1130e1bce647bb6/pydantic_core-2.41.5.tar.gz", hash = "sha256:08daa51ea16ad373ffd5e7606252cc32f07bc72b28284b6bc9c6df804816476e", size = 460952, upload-time = "2025-11-04T13:43:49.098Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/c6/90/32c9941e728d564b411d574d8ee0cf09b12ec978cb22b294995bae5549a5/pydantic_core-2.41.5-cp310-cp310-macosx_10_12_x86_64.whl", hash = "sha256:77b63866ca88d804225eaa4af3e664c5faf3568cea95360d21f4725ab6e07146", size = 2107298, upload-time = "2025-11-04T13:39:04.116Z" },
    { url = "https://files.pythonhosted.org/packages/fb/a8/61c96a77fe28993d9a6fb0f4127e05430a267b235a124545d79fea46dd65/pydantic_core-2.41.5-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:dfa8a0c812ac681395907e71e1274819dec685fec28273a28905df579ef137e2", size = 1901475, upload-time = "2025-11-04T13:39:06.055Z" },
    { url = "https://files.pythonhosted.org/packages/5d/b6/338abf60225acc18cdc08b4faef592d0310923d19a87fba1faf05af5346e/pydantic_core-2.41.5-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:5921a4d3ca3aee735d9fd163808f5e8dd6c6972101e4adbda9a4667908849b97", size = 1918815, upload-time = "2025-11-04T13:39:10.41Z" },
    { url = "https://files.pythonhosted.org/packages/d1/1c/2ed0433e682983d8e8cba9c8d8ef274d4791ec6a6f24c58935b90e780e0a/pydantic_core-2.41.5-cp310-cp310-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:e25c479382d26a2a41b7ebea1043564a937db462816ea07afa8a44c0866d52f9", size = 2065567, upload-time = "2025-11-04T13:39:12.244Z" },
    { url = "https://files.pythonhosted.org/packages/b3/24/cf84974ee7d6eae06b9e63289b7b8f6549d416b5c199ca2d7ce13bbcf619/pydantic_core-2.41.5-cp310-cp310-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:f547144f2966e1e16ae626d8ce72b4cfa0caedc7fa28052001c94fb2fcaa1c52", size = 2230442, upload-time = "2025-11-04T13:39:13.962Z" },
    { url = "https://files.pythonhosted.org/packages/fd/21/4e287865504b3edc0136c89c9c09431be326168b1eb7841911cbc877a995/pydantic_core-2.41.5-cp310-cp310-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:6f52298fbd394f9ed112d56f3d11aabd0d5bd27beb3084cc3d8ad069483b8941", size = 2350956, upload-time = "2025-11-04T13:39:15.889Z" },
    { url = "https://files.pythonhosted.org/packages/a8/76/7727ef2ffa4b62fcab916686a68a0426b9b790139720e1934e8ba797e238/pydantic_core-2.41.5-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:100baa204bb412b74fe285fb0f3a385256dad1d1879f0a5cb1499ed2e83d132a", size = 2068253, upload-time = "2025-11-04T13:39:17.403Z" },
    { url = "https://files.pythonhosted.org/packages/d5/8c/a4abfc79604bcb4c748e18975c44f94f756f08fb04218d5cb87eb0d3a63e/pydantic_core-2.41.5-cp310-cp310-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:05a2c8852530ad2812cb7914dc61a1125dc4e06252ee98e5638a12da6cc6fb6c", size = 2177050, upload-time = "2025-11-04T13:39:19.351Z" },
    { url = "https://files.pythonhosted.org/packages/67/b1/de2e9a9a79b480f9cb0b6e8b6ba4c50b18d4e89852426364c66aa82bb7b3/pydantic_core-2.41.5-cp310-cp310-musllinux_1_1_aarch64.whl", hash = "sha256:29452c56df2ed968d18d7e21f4ab0ac55e71dc59524872f6fc57dcf4a3249ed2", size = 2147178, upload-time = "2025-11-04T13:39:21Z" },
    { url = "https://files.pythonhosted.org/packages/16/c1/dfb33f837a47b20417500efaa0378adc6635b3c79e8369ff7a03c494b4ac/pydantic_core-2.41.5-cp310-cp310-musllinux_1_1_armv7l.whl", hash = "sha256:d5160812ea7a8a2ffbe233d8da666880cad0cbaf5d4de74ae15c313213d62556", size = 2341833, upload-time = "2025-11-04T13:39:22.606Z" },
    { url = "https://files.pythonhosted.org/packages/47/36/00f398642a0f4b815a9a558c4f1dca1b4020a7d49562807d7bc9ff279a6c/pydantic_core-2.41.5-cp310-cp310-musllinux_1_1_x86_64.whl", hash = "sha256:df3959765b553b9440adfd3c795617c352154e497a4eaf3752555cfb5da8fc49", size = 2321156, upload-time = "2025-11-04T13:39:25.843Z" },
    { url = "https://files.pythonhosted.org/packages/7e/70/cad3acd89fde2010807354d978725ae111ddf6d0ea46d1ea1775b5c1bd0c/pydantic_core-2.41.5-cp310-cp310-win32.whl", hash = "sha256:1f8d33a7f4d5a7889e60dc39856d76d09333d8a6ed0f5f1190635cbec70ec4ba", size = 1989378, upload-time = "2025-11-04T13:39:27.92Z" },
    { url = "https://files.pythonhosted.org/packages/76/92/d338652464c6c367e5608e4488201702cd1cbb0f33f7b6a85a60fe5f3720/pydantic_core-2.41.5-cp310-cp310-win_amd64.whl", hash = "sha256:62de39db01b8d593e45871af2af9e497295db8d73b085f6bfd0b18c83c70a8f9", size = 2013622, upload-time = "2025-11-04T13:39:29.848Z" },
    { url = "https://files.pythonhosted.org/packages/e8/72/74a989dd9f2084b3d9530b0915fdda64ac48831c30dbf7c72a41a5232db8/pydantic_core-2.41.5-cp311-cp311-macosx_10_12_x86_64.whl", hash = "sha256:a3a52f6156e73e7ccb0f8cced536adccb7042be67cb45f9562e12b319c119da6", size = 2105873, upload-time = "2025-11-04T13:39:31.373Z" },
    { url = "https://files.pythonhosted.org/packages/12/44/37e403fd9455708b3b942949e1d7febc02167662bf1a7da5b78ee1ea2842/pydantic_core-2.41.5-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:7f3bf998340c6d4b0c9a2f02d6a400e51f123b59565d74dc60d252ce888c260b", size = 1899826, upload-time = "2025-11-04T13:39:32.897Z" },
    { url = "https://files.pythonhosted.org/packages/33/7f/1d5cab3ccf44c1935a359d51a8a2a9e1a654b744b5e7f80d41b88d501eec/pydantic_core-2.41.5-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:378bec5c66998815d224c9ca994f1e14c0c21cb95d2f52b6021cc0b2a58f2a5a", size = 1917869, upload-time = "2025-11-04T13:39:34.469Z" },
    { url = "https://files.pythonhosted.org/packages/6e/6a/30d94a9674a7fe4f4744052ed6c5e083424510be1e93da5bc47569d11810/pydantic_core-2.41.5-cp311-cp311-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:e7b576130c69225432866fe2f4a469a85a54ade141d96fd396dffcf607b558f8", size = 2063890, upload-time = "2025-11-04T13:39:36.053Z" },
    { url = "https://files.pythonhosted.org/packages/50/be/76e5d46203fcb2750e542f32e6c371ffa9b8ad17364cf94bb0818dbfb50c/pydantic_core-2.41.5-cp311-cp311-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:6cb58b9c66f7e4179a2d5e0f849c48eff5c1fca560994d6eb6543abf955a149e", size = 2229740, upload-time = "2025-11-04T13:39:37.753Z" },
    { url = "https://files.pythonhosted.org/packages/d3/ee/fed784df0144793489f87db310a6bbf8118d7b630ed07aa180d6067e653a/pydantic_core-2.41.5-cp311-cp311-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:88942d3a3dff3afc8288c21e565e476fc278902ae4d6d134f1eeda118cc830b1", size = 2350021, upload-time = "2025-11-04T13:39:40.94Z" },
    { url = "https://files.pythonhosted.org/packages/c8/be/8fed28dd0a180dca19e72c233cbf58efa36df055e5b9d90d64fd1740b828/pydantic_core-2.41.5-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:f31d95a179f8d64d90f6831d71fa93290893a33148d890ba15de25642c5d075b", size = 2066378, upload-time = "2025-11-04T13:39:42.523Z" },
    { url = "https://files.pythonhosted.org/packages/b0/3b/698cf8ae1d536a010e05121b4958b1257f0b5522085e335360e53a6b1c8b/pydantic_core-2.41.5-cp311-cp311-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:c1df3d34aced70add6f867a8cf413e299177e0c22660cc767218373d0779487b", size = 2175761, upload-time = "2025-11-04T13:39:44.553Z" },
    { url = "https://files.pythonhosted.org/packages/b8/ba/15d537423939553116dea94ce02f9c31be0fa9d0b806d427e0308ec17145/pydantic_core-2.41.5-cp311-cp311-musllinux_1_1_aarch64.whl", hash = "sha256:4009935984bd36bd2c774e13f9a09563ce8de4abaa7226f5108262fa3e637284", size = 2146303, upload-time = "2025-11-04T13:39:46.238Z" },
    { url = "https://files.pythonhosted.org/packages/58/7f/0de669bf37d206723795f9c90c82966726a2ab06c336deba4735b55af431/pydantic_core-2.41.5-cp311-cp311-musllinux_1_1_armv7l.whl", hash = "sha256:34a64bc3441dc1213096a20fe27e8e128bd3ff89921706e83c0b1ac971276594", size = 2340355, upload-time = "2025-11-04T13:39:48.002Z" },
    { url = "https://files.pythonhosted.org/packages/e5/de/e7482c435b83d7e3c3ee5ee4451f6e8973cff0eb6007d2872ce6383f6398/pydantic_core-2.41.5-cp311-cp311-musllinux_1_1_x86_64.whl", hash = "sha256:c9e19dd6e28fdcaa5a1de679aec4141f691023916427ef9bae8584f9c2fb3b0e", size = 2319875, upload-time = "2025-11-04T13:39:49.705Z" },
    { url = "https://files.pythonhosted.org/packages/fe/e6/8c9e81bb6dd7560e33b9053351c29f30c8194b72f2d6932888581f503482/pydantic_core-2.41.5-cp311-cp311-win32.whl", hash = "sha256:2c010c6ded393148374c0f6f0bf89d206bf3217f201faa0635dcd56bd1520f6b", size = 1987549, upload-time = "2025-11-04T13:39:51.842Z" },
    { url = "https://files.pythonhosted.org/packages/11/66/f14d1d978ea94d1bc21fc98fcf570f9542fe55bfcc40269d4e1a21c19bf7/pydantic_core-2.41.5-cp311-cp311-win_amd64.whl", hash = "sha256:76ee27c6e9c7f16f47db7a94157112a2f3a00e958bc626e2f4ee8bec5c328fbe", size = 2011305, upload-time = "2025-11-04T13:39:53.485Z" },
    { url = "https://files.pythonhosted.org/packages/56/d8/0e271434e8efd03186c5386671328154ee349ff0354d83c74f5caaf096ed/pydantic_core-2.41.5-cp311-cp311-win_arm64.whl", hash = "sha256:4bc36bbc0b7584de96561184ad7f012478987882ebf9f9c389b23f432ea3d90f", size = 1972902, upload-time = "2025-11-04T13:39:56.488Z" },
    { url = "https://files.pythonhosted.org/packages/5f/5d/5f6c63eebb5afee93bcaae4ce9a898f3373ca23df3ccaef086d0233a35a7/pydantic_core-2.41.5-cp312-cp312-macosx_10_12_x86_64.whl", hash = "sha256:f41a7489d32336dbf2199c8c0a215390a751c5b014c2c1c5366e817202e9cdf7", size = 2110990, upload-time = "2025-11-04T13:39:58.079Z" },
    { url = "https://files.pythonhosted.org/packages/aa/32/9c2e8ccb57c01111e0fd091f236c7b371c1bccea0fa85247ac55b1e2b6b6/pydantic_core-2.41.5-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:070259a8818988b9a84a449a2a7337c7f430a22acc0859c6b110aa7212a6d9c0", size = 1896003, upload-time = "2025-11-04T13:39:59.956Z" },
    { url = "https://files.pythonhosted.org/packages/68/b8/a01b53cb0e59139fbc9e4fda3e9724ede8de279097179be4ff31f1abb65a/pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:e96cea19e34778f8d59fe40775a7a574d95816eb150850a85a7a4c8f4b94ac69", size = 1919200, upload-time = "2025-11-04T13:40:02.241Z" },
    { url = "https://files.pythonhosted.org/packages/38/de/8c36b5198a29bdaade07b5985e80a233a5ac27137846f3bc2d3b40a47360/pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:ed2e99c456e3fadd05c991f8f437ef902e00eedf34320ba2b0842bd1c3ca3a75", size = 2052578, upload-time = "2025-11-04T13:40:04.401Z" },
    { url = "https://files.pythonhosted.org/packages/00/b5/0e8e4b5b081eac6cb3dbb7e60a65907549a1ce035a724368c330112adfdd/pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:65840751b72fbfd82c3c640cff9284545342a4f1eb1586ad0636955b261b0b05", size = 2208504, upload-time = "2025-11-04T13:40:06.072Z" },
    { url = "https://files.pythonhosted.org/packages/77/56/87a61aad59c7c5b9dc8caad5a41a5545cba3810c3e828708b3d7404f6cef/pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:e536c98a7626a98feb2d3eaf75944ef6f3dbee447e1f841eae16f2f0a72d8ddc", size = 2335816, upload-time = "2025-11-04T13:40:07.835Z" },
    { url = "https://files.pythonhosted.org/packages/0d/76/941cc9f73529988688a665a5c0ecff1112b3d95ab48f81db5f7606f522d3/pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:eceb81a8d74f9267ef4081e246ffd6d129da5d87e37a77c9bde550cb04870c1c", size = 2075366, upload-time = "2025-11-04T13:40:09.804Z" },
    { url = "https://files.pythonhosted.org/packages/d3/43/ebef01f69baa07a482844faaa0a591bad1ef129253ffd0cdaa9d8a7f72d3/pydantic_core-2.41.5-cp312-cp312-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:d38548150c39b74aeeb0ce8ee1d8e82696f4a4e16ddc6de7b1d8823f7de4b9b5", size = 2171698, upload-time = "2025-11-04T13:40:12.004Z" },
    { url = "https://files.pythonhosted.org/packages/b1/87/41f3202e4193e3bacfc2c065fab7706ebe81af46a83d3e27605029c1f5a6/pydantic_core-2.41.5-cp312-cp312-musllinux_1_1_aarch64.whl", hash = "sha256:c23e27686783f60290e36827f9c626e63154b82b116d7fe9adba1fda36da706c", size = 2132603, upload-time = "2025-11-04T13:40:13.868Z" },
    { url = "https://files.pythonhosted.org/packages/49/7d/4c00df99cb12070b6bccdef4a195255e6020a550d572768d92cc54dba91a/pydantic_core-2.41.5-cp312-cp312-musllinux_1_1_armv7l.whl", hash = "sha256:482c982f814460eabe1d3bb0adfdc583387bd4691ef00b90575ca0d2b6fe2294", size = 2329591, upload-time = "2025-11-04T13:40:15.672Z" },
    { url = "https://files.pythonhosted.org/packages/cc/6a/ebf4b1d65d458f3cda6a7335d141305dfa19bdc61140a884d165a8a1bbc7/pydantic_core-2.41.5-cp312-cp312-musllinux_1_1_x86_64.whl", hash = "sha256:bfea2a5f0b4d8d43adf9d7b8bf019fb46fdd10a2e5cde477fbcb9d1fa08c68e1", size = 2319068, upload-time = "2025-11-04T13:40:17.532Z" },
    { url = "https://files.pythonhosted.org/packages/49/3b/774f2b5cd4192d5ab75870ce4381fd89cf218af999515baf07e7206753f0/pydantic_core-2.41.5-cp312-cp312-win32.whl", hash = "sha256:b74557b16e390ec12dca509bce9264c3bbd128f8a2c376eaa68003d7f327276d", size = 1985908, upload-time = "2025-11-04T13:40:19.309Z" },
    { url = "https://files.pythonhosted.org/packages/86/45/00173a033c801cacf67c190fef088789394feaf88a98a7035b0e40d53dc9/pydantic_core-2.41.5-cp312-cp312-win_amd64.whl", hash = "sha256:1962293292865bca8e54702b08a4f26da73adc83dd1fcf26fbc875b35d81c815", size = 2020145, upload-time = "2025-11-04T13:40:21.548Z" },
    { url = "https://files.pythonhosted.org/packages/f9/22/91fbc821fa6d261b376a3f73809f907cec5ca6025642c463d3488aad22fb/pydantic_core-2.41.5-cp312-cp312-win_arm64.whl", hash = "sha256:1746d4a3d9a794cacae06a5eaaccb4b8643a131d45fbc9af23e353dc0a5ba5c3", size = 1976179, upload-time = "2025-11-04T13:40:23.393Z" },
    { url = "https://files.pythonhosted.org/packages/87/06/8806241ff1f70d9939f9af039c6c35f2360cf16e93c2ca76f184e76b1564/pydantic_core-2.41.5-cp313-cp313-macosx_10_12_x86_64.whl", hash = "sha256:941103c9be18ac8daf7b7adca8228f8ed6bb7a1849020f643b3a14d15b1924d9", size = 2120403, upload-time = "2025-11-04T13:40:25.248Z" },
    { url = "https://files.pythonhosted.org/packages/94/02/abfa0e0bda67faa65fef1c84971c7e45928e108fe24333c81f3bfe35d5f5/pydantic_core-2.41.5-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:112e305c3314f40c93998e567879e887a3160bb8689ef3d2c04b6cc62c33ac34", size = 1896206, upload-time = "2025-11-04T13:40:27.099Z" },
    { url = "https://files.pythonhosted.org/packages/15/df/a4c740c0943e93e6500f9eb23f4ca7ec9bf71b19e608ae5b579678c8d02f/pydantic_core-2.41.5-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:0cbaad15cb0c90aa221d43c00e77bb33c93e8d36e0bf74760cd00e732d10a6a0", size = 1919307, upload-time = "2025-11-04T13:40:29.806Z" },
    { url = "https://files.pythonhosted.org/packages/9a/e3/6324802931ae1d123528988e0e86587c2072ac2e5394b4bc2bc34b61ff6e/pydantic_core-2.41.5-cp313-cp313-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:03ca43e12fab6023fc79d28ca6b39b05f794ad08ec2feccc59a339b02f2b3d33", size = 2063258, upload-time = "2025-11-04T13:40:33.544Z" },
    { url = "https://files.pythonhosted.org/packages/c9/d4/2230d7151d4957dd79c3044ea26346c148c98fbf0ee6ebd41056f2d62ab5/pydantic_core-2.41.5-cp313-cp313-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:dc799088c08fa04e43144b164feb0c13f9a0bc40503f8df3e9fde58a3c0c101e", size = 2214917, upload-time = "2025-11-04T13:40:35.479Z" },
    { url = "https://files.pythonhosted.org/packages/e6/9f/eaac5df17a3672fef0081b6c1bb0b82b33ee89aa5cec0d7b05f52fd4a1fa/pydantic_core-2.41.5-cp313-cp313-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:97aeba56665b4c3235a0e52b2c2f5ae9cd071b8a8310ad27bddb3f7fb30e9aa2", size = 2332186, upload-time = "2025-11-04T13:40:37.436Z" },
    { url = "https://files.pythonhosted.org/packages/cf/4e/35a80cae583a37cf15604b44240e45c05e04e86f9cfd766623149297e971/pydantic_core-2.41.5-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:406bf18d345822d6c21366031003612b9c77b3e29ffdb0f612367352aab7d586", size = 2073164, upload-time = "2025-11-04T13:40:40.289Z" },
    { url = "https://files.pythonhosted.org/packages/bf/e3/f6e262673c6140dd3305d144d032f7bd5f7497d3871c1428521f19f9efa2/pydantic_core-2.41.5-cp313-cp313-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:b93590ae81f7010dbe380cdeab6f515902ebcbefe0b9327cc4804d74e93ae69d", size = 2179146, upload-time = "2025-11-04T13:40:42.809Z" },
    { url = "https://files.pythonhosted.org/packages/75/c7/20bd7fc05f0c6ea2056a4565c6f36f8968c0924f19b7d97bbfea55780e73/pydantic_core-2.41.5-cp313-cp313-musllinux_1_1_aarch64.whl", hash = "sha256:01a3d0ab748ee531f4ea6c3e48ad9dac84ddba4b0d82291f87248f2f9de8d740", size = 2137788, upload-time = "2025-11-04T13:40:44.752Z" },
    { url = "https://files.pythonhosted.org/packages/3a/8d/34318ef985c45196e004bc46c6eab2eda437e744c124ef0dbe1ff2c9d06b/pydantic_core-2.41.5-cp313-cp313-musllinux_1_1_armv7l.whl", hash = "sha256:6561e94ba9dacc9c61bce40e2d6bdc3bfaa0259d3ff36ace3b1e6901936d2e3e", size = 2340133, upload-time = "2025-11-04T13:40:46.66Z" },
    { url = "https://files.pythonhosted.org/packages/9c/59/013626bf8c78a5a5d9350d12e7697d3d4de951a75565496abd40ccd46bee/pydantic_core-2.41.5-cp313-cp313-musllinux_1_1_x86_64.whl", hash = "sha256:915c3d10f81bec3a74fbd4faebe8391013ba61e5a1a8d48c4455b923bdda7858", size = 2324852, upload-time = "2025-11-04T13:40:48.575Z" },
    { url = "https://files.pythonhosted.org/packages/1a/d9/c248c103856f807ef70c18a4f986693a46a8ffe1602e5d361485da502d20/pydantic_core-2.41.5-cp313-cp313-win32.whl", hash = "sha256:650ae77860b45cfa6e2cdafc42618ceafab3a2d9a3811fcfbd3bbf8ac3c40d36", size = 1994679, upload-time = "2025-11-04T13:40:50.619Z" },
    { url = "https://files.pythonhosted.org/packages/9e/8b/341991b158ddab181cff136acd2552c9f35bd30380422a639c0671e99a91/pydantic_core-2.41.5-cp313-cp313-win_amd64.whl", hash = "sha256:79ec52ec461e99e13791ec6508c722742ad745571f234ea6255bed38c6480f11", size = 2019766, upload-time = "2025-11-04T13:40:52.631Z" },
    { url = "https://files.pythonhosted.org/packages/73/7d/f2f9db34af103bea3e09735bb40b021788a5e834c81eedb541991badf8f5/pydantic_core-2.41.5-cp313-cp313-win_arm64.whl", hash = "sha256:3f84d5c1b4ab906093bdc1ff10484838aca54ef08de4afa9de0f5f14d69639cd", size = 1981005, upload-time = "2025-11-04T13:40:54.734Z" },
    { url = "https://files.pythonhosted.org/packages/ea/28/46b7c5c9635ae96ea0fbb779e271a38129df2550f763937659ee6c5dbc65/pydantic_core-2.41.5-cp314-cp314-macosx_10_12_x86_64.whl", hash = "sha256:3f37a19d7ebcdd20b96485056ba9e8b304e27d9904d233d7b1015db320e51f0a", size = 2119622, upload-time = "2025-11-04T13:40:56.68Z" },
    { url = "https://files.pythonhosted.org/packages/74/1a/145646e5687e8d9a1e8d09acb278c8535ebe9e972e1f162ed338a622f193/pydantic_core-2.41.5-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:1d1d9764366c73f996edd17abb6d9d7649a7eb690006ab6adbda117717099b14", size = 1891725, upload-time = "2025-11-04T13:40:58.807Z" },
    { url = "https://files.pythonhosted.org/packages/23/04/e89c29e267b8060b40dca97bfc64a19b2a3cf99018167ea1677d96368273/pydantic_core-2.41.5-cp314-cp314-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:25e1c2af0fce638d5f1988b686f3b3ea8cd7de5f244ca147c777769e798a9cd1", size = 1915040, upload-time = "2025-11-04T13:41:00.853Z" },
    { url = "https://files.pythonhosted.org/packages/84/a3/15a82ac7bd97992a82257f777b3583d3e84bdb06ba6858f745daa2ec8a85/pydantic_core-2.41.5-cp314-cp314-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:506d766a8727beef16b7adaeb8ee6217c64fc813646b424d0804d67c16eddb66", size = 2063691, upload-time = "2025-11-04T13:41:03.504Z" },
    { url = "https://files.pythonhosted.org/packages/74/9b/0046701313c6ef08c0c1cf0e028c67c770a4e1275ca73131563c5f2a310a/pydantic_core-2.41.5-cp314-cp314-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:4819fa52133c9aa3c387b3328f25c1facc356491e6135b459f1de698ff64d869", size = 2213897, upload-time = "2025-11-04T13:41:05.804Z" },
    { url = "https://files.pythonhosted.org/packages/8a/cd/6bac76ecd1b27e75a95ca3a9a559c643b3afcd2dd62086d4b7a32a18b169/pydantic_core-2.41.5-cp314-cp314-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:2b761d210c9ea91feda40d25b4efe82a1707da2ef62901466a42492c028553a2", size = 2333302, upload-time = "2025-11-04T13:41:07.809Z" },
    { url = "https://files.pythonhosted.org/packages/4c/d2/ef2074dc020dd6e109611a8be4449b98cd25e1b9b8a303c2f0fca2f2bcf7/pydantic_core-2.41.5-cp314-cp314-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:22f0fb8c1c583a3b6f24df2470833b40207e907b90c928cc8d3594b76f874375", size = 2064877, upload-time = "2025-11-04T13:41:09.827Z" },
    { url = "https://files.pythonhosted.org/packages/18/66/e9db17a9a763d72f03de903883c057b2592c09509ccfe468187f2a2eef29/pydantic_core-2.41.5-cp314-cp314-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:2782c870e99878c634505236d81e5443092fba820f0373997ff75f90f68cd553", size = 2180680, upload-time = "2025-11-04T13:41:12.379Z" },
    { url = "https://files.pythonhosted.org/packages/d3/9e/3ce66cebb929f3ced22be85d4c2399b8e85b622db77dad36b73c5387f8f8/pydantic_core-2.41.5-cp314-cp314-musllinux_1_1_aarch64.whl", hash = "sha256:0177272f88ab8312479336e1d777f6b124537d47f2123f89cb37e0accea97f90", size = 2138960, upload-time = "2025-11-04T13:41:14.627Z" },
    { url = "https://files.pythonhosted.org/packages/a6/62/205a998f4327d2079326b01abee48e502ea739d174f0a89295c481a2272e/pydantic_core-2.41.5-cp314-cp314-musllinux_1_1_armv7l.whl", hash = "sha256:63510af5e38f8955b8ee5687740d6ebf7c2a0886d15a6d65c32814613681bc07", size = 2339102, upload-time = "2025-11-04T13:41:16.868Z" },
    { url = "https://files.pythonhosted.org/packages/3c/0d/f05e79471e889d74d3d88f5bd20d0ed189ad94c2423d81ff8d0000aab4ff/pydantic_core-2.41.5-cp314-cp314-musllinux_1_1_x86_64.whl", hash = "sha256:e56ba91f47764cc14f1daacd723e3e82d1a89d783f0f5afe9c364b8bb491ccdb", size = 2326039, upload-time = "2025-11-04T13:41:18.934Z" },
    { url = "https://files.pythonhosted.org/packages/ec/e1/e08a6208bb100da7e0c4b288eed624a703f4d129bde2da475721a80cab32/pydantic_core-2.41.5-cp314-cp314-win32.whl", hash = "sha256:aec5cf2fd867b4ff45b9959f8b20ea3993fc93e63c7363fe6851424c8a7e7c23", size = 1995126, upload-time = "2025-11-04T13:41:21.418Z" },
    { url = "https://files.pythonhosted.org/packages/48/5d/56ba7b24e9557f99c9237e29f5c09913c81eeb2f3217e40e922353668092/pydantic_core-2.41.5-cp314-cp314-win_amd64.whl", hash = "sha256:8e7c86f27c585ef37c35e56a96363ab8de4e549a95512445b85c96d3e2f7c1bf", size = 2015489, upload-time = "2025-11-04T13:41:24.076Z" },
    { url = "https://files.pythonhosted.org/packages/4e/bb/f7a190991ec9e3e0ba22e4993d8755bbc4a32925c0b5b42775c03e8148f9/pydantic_core-2.41.5-cp314-cp314-win_arm64.whl", hash = "sha256:e672ba74fbc2dc8eea59fb6d4aed6845e6905fc2a8afe93175d94a83ba2a01a0", size = 1977288, upload-time = "2025-11-04T13:41:26.33Z" },
    { url = "https://files.pythonhosted.org/packages/92/ed/77542d0c51538e32e15afe7899d79efce4b81eee631d99850edc2f5e9349/pydantic_core-2.41.5-cp314-cp314t-macosx_10_12_x86_64.whl", hash = "sha256:8566def80554c3faa0e65ac30ab0932b9e3a5cd7f8323764303d468e5c37595a", size = 2120255, upload-time = "2025-11-04T13:41:28.569Z" },
    { url = "https://files.pythonhosted.org/packages/bb/3d/6913dde84d5be21e284439676168b28d8bbba5600d838b9dca99de0fad71/pydantic_core-2.41.5-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:b80aa5095cd3109962a298ce14110ae16b8c1aece8b72f9dafe81cf597ad80b3", size = 1863760, upload-time = "2025-11-04T13:41:31.055Z" },
    { url = "https://files.pythonhosted.org/packages/5a/f0/e5e6b99d4191da102f2b0eb9687aaa7f5bea5d9964071a84effc3e40f997/pydantic_core-2.41.5-cp314-cp314t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:3006c3dd9ba34b0c094c544c6006cc79e87d8612999f1a5d43b769b89181f23c", size = 1878092, upload-time = "2025-11-04T13:41:33.21Z" },
    { url = "https://files.pythonhosted.org/packages/71/48/36fb760642d568925953bcc8116455513d6e34c4beaa37544118c36aba6d/pydantic_core-2.41.5-cp314-cp314t-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:72f6c8b11857a856bcfa48c86f5368439f74453563f951e473514579d44aa612", size = 2053385, upload-time = "2025-11-04T13:41:35.508Z" },
    { url = "https://files.pythonhosted.org/packages/20/25/92dc684dd8eb75a234bc1c764b4210cf2646479d54b47bf46061657292a8/pydantic_core-2.41.5-cp314-cp314t-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:5cb1b2f9742240e4bb26b652a5aeb840aa4b417c7748b6f8387927bc6e45e40d", size = 2218832, upload-time = "2025-11-04T13:41:37.732Z" },
    { url = "https://files.pythonhosted.org/packages/e2/09/f53e0b05023d3e30357d82eb35835d0f6340ca344720a4599cd663dca599/pydantic_core-2.41.5-cp314-cp314t-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:bd3d54f38609ff308209bd43acea66061494157703364ae40c951f83ba99a1a9", size = 2327585, upload-time = "2025-11-04T13:41:40Z" },
    { url = "https://files.pythonhosted.org/packages/aa/4e/2ae1aa85d6af35a39b236b1b1641de73f5a6ac4d5a7509f77b814885760c/pydantic_core-2.41.5-cp314-cp314t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:2ff4321e56e879ee8d2a879501c8e469414d948f4aba74a2d4593184eb326660", size = 2041078, upload-time = "2025-11-04T13:41:42.323Z" },
    { url = "https://files.pythonhosted.org/packages/cd/13/2e215f17f0ef326fc72afe94776edb77525142c693767fc347ed6288728d/pydantic_core-2.41.5-cp314-cp314t-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:d0d2568a8c11bf8225044aa94409e21da0cb09dcdafe9ecd10250b2baad531a9", size = 2173914, upload-time = "2025-11-04T13:41:45.221Z" },
    { url = "https://files.pythonhosted.org/packages/02/7a/f999a6dcbcd0e5660bc348a3991c8915ce6599f4f2c6ac22f01d7a10816c/pydantic_core-2.41.5-cp314-cp314t-musllinux_1_1_aarch64.whl", hash = "sha256:a39455728aabd58ceabb03c90e12f71fd30fa69615760a075b9fec596456ccc3", size = 2129560, upload-time = "2025-11-04T13:41:47.474Z" },
    { url = "https://files.pythonhosted.org/packages/3a/b1/6c990ac65e3b4c079a4fb9f5b05f5b013afa0f4ed6780a3dd236d2cbdc64/pydantic_core-2.41.5-cp314-cp314t-musllinux_1_1_armv7l.whl", hash = "sha256:239edca560d05757817c13dc17c50766136d21f7cd0fac50295499ae24f90fdf", size = 2329244, upload-time = "2025-11-04T13:41:49.992Z" },
    { url = "https://files.pythonhosted.org/packages/d9/02/3c562f3a51afd4d88fff8dffb1771b30cfdfd79befd9883ee094f5b6c0d8/pydantic_core-2.41.5-cp314-cp314t-musllinux_1_1_x86_64.whl", hash = "sha256:2a5e06546e19f24c6a96a129142a75cee553cc018ffee48a460059b1185f4470", size = 2331955, upload-time = "2025-11-04T13:41:54.079Z" },
    { url = "https://files.pythonhosted.org/packages/5c/96/5fb7d8c3c17bc8c62fdb031c47d77a1af698f1d7a406b0f79aaa1338f9ad/pydantic_core-2.41.5-cp314-cp314t-win32.whl", hash = "sha256:b4ececa40ac28afa90871c2cc2b9ffd2ff0bf749380fbdf57d165fd23da353aa", size = 1988906, upload-time = "2025-11-04T13:41:56.606Z" },
    { url = "https://files.pythonhosted.org/packages/22/ed/182129d83032702912c2e2d8bbe33c036f342cc735737064668585dac28f/pydantic_core-2.41.5-cp314-cp314t-win_amd64.whl", hash = "sha256:80aa89cad80b32a912a65332f64a4450ed00966111b6615ca6816153d3585a8c", size = 1981607, upload-time = "2025-11-04T13:41:58.889Z" },
    { url = "https://files.pythonhosted.org/packages/9f/ed/068e41660b832bb0b1aa5b58011dea2a3fe0ba7861ff38c4d4904c1c1a99/pydantic_core-2.41.5-cp314-cp314t-win_arm64.whl", hash = "sha256:35b44f37a3199f771c3eaa53051bc8a70cd7b54f333531c59e29fd4db5d15008", size = 1974769, upload-time = "2025-11-04T13:42:01.186Z" },
    { url = "https://files.pythonhosted.org/packages/11/72/90fda5ee3b97e51c494938a4a44c3a35a9c96c19bba12372fb9c634d6f57/pydantic_core-2.41.5-graalpy311-graalpy242_311_native-macosx_10_12_x86_64.whl", hash = "sha256:b96d5f26b05d03cc60f11a7761a5ded1741da411e7fe0909e27a5e6a0cb7b034", size = 2115441, upload-time = "2025-11-04T13:42:39.557Z" },
    { url = "https://files.pythonhosted.org/packages/1f/53/8942f884fa33f50794f119012dc6a1a02ac43a56407adaac20463df8e98f/pydantic_core-2.41.5-graalpy311-graalpy242_311_native-macosx_11_0_arm64.whl", hash = "sha256:634e8609e89ceecea15e2d61bc9ac3718caaaa71963717bf3c8f38bfde64242c", size = 1930291, upload-time = "2025-11-04T13:42:42.169Z" },
    { url = "https://files.pythonhosted.org/packages/79/c8/ecb9ed9cd942bce09fc888ee960b52654fbdbede4ba6c2d6e0d3b1d8b49c/pydantic_core-2.41.5-graalpy311-graalpy242_311_native-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:93e8740d7503eb008aa2df04d3b9735f845d43ae845e6dcd2be0b55a2da43cd2", size = 1948632, upload-time = "2025-11-04T13:42:44.564Z" },
    { url = "https://files.pythonhosted.org/packages/2e/1b/687711069de7efa6af934e74f601e2a4307365e8fdc404703afc453eab26/pydantic_core-2.41.5-graalpy311-graalpy242_311_native-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:f15489ba13d61f670dcc96772e733aad1a6f9c429cc27574c6cdaed82d0146ad", size = 2138905, upload-time = "2025-11-04T13:42:47.156Z" },
    { url = "https://files.pythonhosted.org/packages/09/32/59b0c7e63e277fa7911c2fc70ccfb45ce4b98991e7ef37110663437005af/pydantic_core-2.41.5-graalpy312-graalpy250_312_native-macosx_10_12_x86_64.whl", hash = "sha256:7da7087d756b19037bc2c06edc6c170eeef3c3bafcb8f532ff17d64dc427adfd", size = 2110495, upload-time = "2025-11-04T13:42:49.689Z" },
    { url = "https://files.pythonhosted.org/packages/aa/81/05e400037eaf55ad400bcd318c05bb345b57e708887f07ddb2d20e3f0e98/pydantic_core-2.41.5-graalpy312-graalpy250_312_native-macosx_11_0_arm64.whl", hash = "sha256:aabf5777b5c8ca26f7824cb4a120a740c9588ed58df9b2d196ce92fba42ff8dc", size = 1915388, upload-time = "2025-11-04T13:42:52.215Z" },
    { url = "https://files.pythonhosted.org/packages/6e/0d/e3549b2399f71d56476b77dbf3cf8937cec5cd70536bdc0e374a421d0599/pydantic_core-2.41.5-graalpy312-graalpy250_312_native-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:c007fe8a43d43b3969e8469004e9845944f1a80e6acd47c150856bb87f230c56", size = 1942879, upload-time = "2025-11-04T13:42:56.483Z" },
    { url = "https://files.pythonhosted.org/packages/f7/07/34573da085946b6a313d7c42f82f16e8920bfd730665de2d11c0c37a74b5/pydantic_core-2.41.5-graalpy312-graalpy250_312_native-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:76d0819de158cd855d1cbb8fcafdf6f5cf1eb8e470abe056d5d161106e38062b", size = 2139017, upload-time = "2025-11-04T13:42:59.471Z" },
    { url = "https://files.pythonhosted.org/packages/e6/b0/1a2aa41e3b5a4ba11420aba2d091b2d17959c8d1519ece3627c371951e73/pydantic_core-2.41.5-pp310-pypy310_pp73-macosx_10_12_x86_64.whl", hash = "sha256:b5819cd790dbf0c5eb9f82c73c16b39a65dd6dd4d1439dcdea7816ec9adddab8", size = 2103351, upload-time = "2025-11-04T13:43:02.058Z" },
    { url = "https://files.pythonhosted.org/packages/a4/ee/31b1f0020baaf6d091c87900ae05c6aeae101fa4e188e1613c80e4f1ea31/pydantic_core-2.41.5-pp310-pypy310_pp73-macosx_11_0_arm64.whl", hash = "sha256:5a4e67afbc95fa5c34cf27d9089bca7fcab4e51e57278d710320a70b956d1b9a", size = 1925363, upload-time = "2025-11-04T13:43:05.159Z" },
    { url = "https://files.pythonhosted.org/packages/e1/89/ab8e86208467e467a80deaca4e434adac37b10a9d134cd2f99b28a01e483/pydantic_core-2.41.5-pp310-pypy310_pp73-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:ece5c59f0ce7d001e017643d8d24da587ea1f74f6993467d85ae8a5ef9d4f42b", size = 2135615, upload-time = "2025-11-04T13:43:08.116Z" },
    { url = "https://files.pythonhosted.org/packages/99/0a/99a53d06dd0348b2008f2f30884b34719c323f16c3be4e6cc1203b74a91d/pydantic_core-2.41.5-pp310-pypy310_pp73-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:16f80f7abe3351f8ea6858914ddc8c77e02578544a0ebc15b4c2e1a0e813b0b2", size = 2175369, upload-time = "2025-11-04T13:43:12.49Z" },
    { url = "https://files.pythonhosted.org/packages/6d/94/30ca3b73c6d485b9bb0bc66e611cff4a7138ff9736b7e66bcf0852151636/pydantic_core-2.41.5-pp310-pypy310_pp73-musllinux_1_1_aarch64.whl", hash = "sha256:33cb885e759a705b426baada1fe68cbb0a2e68e34c5d0d0289a364cf01709093", size = 2144218, upload-time = "2025-11-04T13:43:15.431Z" },
    { url = "https://files.pythonhosted.org/packages/87/57/31b4f8e12680b739a91f472b5671294236b82586889ef764b5fbc6669238/pydantic_core-2.41.5-pp310-pypy310_pp73-musllinux_1_1_armv7l.whl", hash = "sha256:c8d8b4eb992936023be7dee581270af5c6e0697a8559895f527f5b7105ecd36a", size = 2329951, upload-time = "2025-11-04T13:43:18.062Z" },
    { url = "https://files.pythonhosted.org/packages/7d/73/3c2c8edef77b8f7310e6fb012dbc4b8551386ed575b9eb6fb2506e28a7eb/pydantic_core-2.41.5-pp310-pypy310_pp73-musllinux_1_1_x86_64.whl", hash = "sha256:242a206cd0318f95cd21bdacff3fcc3aab23e79bba5cac3db5a841c9ef9c6963", size = 2318428, upload-time = "2025-11-04T13:43:20.679Z" },
    { url = "https://files.pythonhosted.org/packages/2f/02/8559b1f26ee0d502c74f9cca5c0d2fd97e967e083e006bbbb4e97f3a043a/pydantic_core-2.41.5-pp310-pypy310_pp73-win_amd64.whl", hash = "sha256:d3a978c4f57a597908b7e697229d996d77a6d3c94901e9edee593adada95ce1a", size = 2147009, upload-time = "2025-11-04T13:43:23.286Z" },
    { url = "https://files.pythonhosted.org/packages/5f/9b/1b3f0e9f9305839d7e84912f9e8bfbd191ed1b1ef48083609f0dabde978c/pydantic_core-2.41.5-pp311-pypy311_pp73-macosx_10_12_x86_64.whl", hash = "sha256:b2379fa7ed44ddecb5bfe4e48577d752db9fc10be00a6b7446e9663ba143de26", size = 2101980, upload-time = "2025-11-04T13:43:25.97Z" },
    { url = "https://files.pythonhosted.org/packages/a4/ed/d71fefcb4263df0da6a85b5d8a7508360f2f2e9b3bf5814be9c8bccdccc1/pydantic_core-2.41.5-pp311-pypy311_pp73-macosx_11_0_arm64.whl", hash = "sha256:266fb4cbf5e3cbd0b53669a6d1b039c45e3ce651fd5442eff4d07c2cc8d66808", size = 1923865, upload-time = "2025-11-04T13:43:28.763Z" },
    { url = "https://files.pythonhosted.org/packages/ce/3a/626b38db460d675f873e4444b4bb030453bbe7b4ba55df821d026a0493c4/pydantic_core-2.41.5-pp311-pypy311_pp73-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:58133647260ea01e4d0500089a8c4f07bd7aa6ce109682b1426394988d8aaacc", size = 2134256, upload-time = "2025-11-04T13:43:31.71Z" },
    { url = "https://files.pythonhosted.org/packages/83/d9/8412d7f06f616bbc053d30cb4e5f76786af3221462ad5eee1f202021eb4e/pydantic_core-2.41.5-pp311-pypy311_pp73-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:287dad91cfb551c363dc62899a80e9e14da1f0e2b6ebde82c806612ca2a13ef1", size = 2174762, upload-time = "2025-11-04T13:43:34.744Z" },
    { url = "https://files.pythonhosted.org/packages/55/4c/162d906b8e3ba3a99354e20faa1b49a85206c47de97a639510a0e673f5da/pydantic_core-2.41.5-pp311-pypy311_pp73-musllinux_1_1_aarch64.whl", hash = "sha256:03b77d184b9eb40240ae9fd676ca364ce1085f203e1b1256f8ab9984dca80a84", size = 2143141, upload-time = "2025-11-04T13:43:37.701Z" },
    { url = "https://files.pythonhosted.org/packages/1f/f2/f11dd73284122713f5f89fc940f370d035fa8e1e078d446b3313955157fe/pydantic_core-2.41.5-pp311-pypy311_pp73-musllinux_1_1_armv7l.whl", hash = "sha256:a668ce24de96165bb239160b3d854943128f4334822900534f2fe947930e5770", size = 2330317, upload-time = "2025-11-04T13:43:40.406Z" },
    { url = "https://files.pythonhosted.org/packages/88/9d/b06ca6acfe4abb296110fb1273a4d848a0bfb2ff65f3ee92127b3244e16b/pydantic_core-2.41.5-pp311-pypy311_pp73-musllinux_1_1_x86_64.whl", hash = "sha256:f14f8f046c14563f8eb3f45f499cc658ab8d10072961e07225e507adb700e93f", size = 2316992, upload-time = "2025-11-04T13:43:43.602Z" },
    { url = "https://files.pythonhosted.org/packages/36/c7/cfc8e811f061c841d7990b0201912c3556bfeb99cdcb7ed24adc8d6f8704/pydantic_core-2.41.5-pp311-pypy311_pp73-win_amd64.whl", hash = "sha256:56121965f7a4dc965bff783d70b907ddf3d57f6eba29b6d2e5dabfaf07799c51", size = 2145302, upload-time = "2025-11-04T13:43:46.64Z" },
]

[[package]]
name = "python-dotenv"
version = "1.2.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/82/ed/0301aeeac3e5353ef3d94b6ec08bbcabd04a72018415dcb29e588514bba8/python_dotenv-1.2.2.tar.gz", hash = "sha256:2c371a91fbd7ba082c2c1dc1f8bf89ca22564a087c2c287cd9b662adde799cf3", size = 50135, upload-time = "2026-03-01T16:00:26.196Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/0b/d7/1959b9648791274998a9c3526f6d0ec8fd2233e4d4acce81bbae76b44b2a/python_dotenv-1.2.2-py3-none-any.whl", hash = "sha256:1d8214789a24de455a8b8bd8ae6fe3c6b69a5e3d64aa8a8e5d68e694bbcb285a", size = 22101, upload-time = "2026-03-01T16:00:25.09Z" },
]

[[package]]
name = "sniffio"
version = "1.3.1"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/a2/87/a6771e1546d97e7e041b6ae58d80074f81b7d5121207425c964ddf5cfdbd/sniffio-1.3.1.tar.gz", hash = "sha256:f4324edc670a0f49750a81b895f35c3adb843cca46f0530f79fc1babb23789dc", size = 20372, upload-time = "2024-02-25T23:20:04.057Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/e9/44/75a9c9421471a6c4805dbf2356f7c181a29c1879239abab1ea2cc8f38b40/sniffio-1.3.1-py3-none-any.whl", hash = "sha256:2f6da418d1f1e0fddd844478f41680e794e6051915791a034ff65e5f100525a2", size = 10235, upload-time = "2024-02-25T23:20:01.196Z" },
]

[[package]]
name = "tqdm"
version = "4.67.3"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "colorama", marker = "sys_platform == 'win32'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/09/a9/6ba95a270c6f1fbcd8dac228323f2777d886cb206987444e4bce66338dd4/tqdm-4.67.3.tar.gz", hash = "sha256:7d825f03f89244ef73f1d4ce193cb1774a8179fd96f31d7e1dcde62092b960bb", size = 169598, upload-time = "2026-02-03T17:35:53.048Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/16/e1/3079a9ff9b8e11b846c6ac5c8b5bfb7ff225eee721825310c91b3b50304f/tqdm-4.67.3-py3-none-any.whl", hash = "sha256:ee1e4c0e59148062281c49d80b25b67771a127c85fc9676d3be5f243206826bf", size = 78374, upload-time = "2026-02-03T17:35:50.982Z" },
]

[[package]]
name = "typing-extensions"
version = "4.15.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/72/94/1a15dd82efb362ac84269196e94cf00f187f7ed21c242792a923cdb1c61f/typing_extensions-4.15.0.tar.gz", hash = "sha256:0cea48d173cc12fa28ecabc3b837ea3cf6f38c6d1136f85cbaaf598984861466", size = 109391, upload-time = "2025-08-25T13:49:26.313Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/18/67/36e9267722cc04a6b9f15c7f3441c2363321a3ea07da7ae0c0707beb2a9c/typing_extensions-4.15.0-py3-none-any.whl", hash = "sha256:f0fa19c6845758ab08074a0cfa8b7aecb71c999ca73d62883bc25cc018c4e548", size = 44614, upload-time = "2025-08-25T13:49:24.86Z" },
]

[[package]]
name = "typing-inspection"
version = "0.4.2"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "typing-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/55/e3/70399cb7dd41c10ac53367ae42139cf4b1ca5f36bb3dc6c9d33acdb43655/typing_inspection-0.4.2.tar.gz", hash = "sha256:ba561c48a67c5958007083d386c3295464928b01faa735ab8547c5692e87f464", size = 75949, upload-time = "2025-10-01T02:14:41.687Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/dc/9b/47798a6c91d8bdb567fe2698fe81e0c6b7cb7ef4d13da4114b41d239f65d/typing_inspection-0.4.2-py3-none-any.whl", hash = "sha256:4ed1cacbdc298c220f1bd249ed5287caa16f34d44ef4e9c3d0cbad5b521545e7", size = 14611, upload-time = "2025-10-01T02:14:40.154Z" },
]

[[package]]
name = "urllib3"
version = "2.6.3"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/c7/24/5f1b3bdffd70275f6661c76461e25f024d5a38a46f04aaca912426a2b1d3/urllib3-2.6.3.tar.gz", hash = "sha256:1b62b6884944a57dbe321509ab94fd4d3b307075e0c2eae991ac71ee15ad38ed", size = 435556, upload-time = "2026-01-07T16:24:43.925Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/39/08/aaaad47bc4e9dc8c725e68f9d04865dbcb2052843ff09c97b08904852d84/urllib3-2.6.3-py3-none-any.whl", hash = "sha256:bf272323e553dfb2e87d9bfd225ca7b0f467b919d7bbd355436d3fd37cb0acd4", size = 131584, upload-time = "2026-01-07T16:24:42.685Z" },
]
```

## File: `python/openai-agent-artifacts/agent/__init__.py`
```python
from .react import AcontextArtifactAgent

__all__ = ["AcontextArtifactAgent"]

```

## File: `python/openai-agent-artifacts/agent/disk.py`
```python
"""
This module is deprecated. Disk operations are now handled by DISK_TOOLS from acontext.agent.disk.

The agent now uses DISK_TOOLS directly, which provides all disk operations through
the SDK's pre-built tool pool. See agent/react.py for the updated implementation.
"""

```

## File: `python/openai-agent-artifacts/agent/pretty_print.py`
```python
"""Pretty printing utilities for better console output."""
from typing import Any


class Colors:
    """ANSI color codes for terminal output."""
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    
    # Colors
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    
    # Bright colors
    BRIGHT_BLACK = "\033[90m"
    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_CYAN = "\033[96m"
    BRIGHT_WHITE = "\033[97m"


def print_header(text: str, char: str = "=", color: str = Colors.CYAN) -> None:
    """Print a formatted header."""
    width = 60
    print(f"\n{color}{char * width}{Colors.RESET}")
    print(f"{color}{Colors.BOLD}{text.center(width)}{Colors.RESET}")
    print(f"{color}{char * width}{Colors.RESET}\n")


def print_success(text: str) -> None:
    """Print a success message."""
    print(f"{Colors.BRIGHT_GREEN}✓{Colors.RESET} {Colors.GREEN}{text}{Colors.RESET}")


def print_info(text: str) -> None:
    """Print an info message."""
    print(f"{Colors.BRIGHT_BLUE}ℹ{Colors.RESET} {Colors.BLUE}{text}{Colors.RESET}")


def print_warning(text: str) -> None:
    """Print a warning message."""
    print(f"{Colors.BRIGHT_YELLOW}⚠{Colors.RESET} {Colors.YELLOW}{text}{Colors.RESET}")


def print_error(text: str) -> None:
    """Print an error message."""
    print(f"{Colors.BRIGHT_RED}✗{Colors.RESET} {Colors.RED}{text}{Colors.RESET}")


def print_box(title: str, content: str, color: str = Colors.CYAN) -> None:
    """Print content in a box with title."""
    width = 60
    border = f"{color}{'─' * (width - 2)}{Colors.RESET}"
    
    print(f"\n{color}┌{border}┐{Colors.RESET}")
    print(f"{color}│{Colors.RESET} {Colors.BOLD}{title:<{width-4}}{Colors.RESET}{color}│{Colors.RESET}")
    print(f"{color}├{border}┤{Colors.RESET}")
    
    # Wrap content if needed
    lines = content.split("\n")
    for line in lines:
        if len(line) <= width - 4:
            print(f"{color}│{Colors.RESET} {line:<{width-4}}{color}│{Colors.RESET}")
        else:
            # Word wrap
            words = line.split()
            current_line = ""
            for word in words:
                if len(current_line + word) + 1 <= width - 4:
                    current_line += word + " "
                else:
                    if current_line:
                        print(f"{color}│{Colors.RESET} {current_line:<{width-4}}{color}│{Colors.RESET}")
                    current_line = word + " "
            if current_line:
                print(f"{color}│{Colors.RESET} {current_line:<{width-4}}{color}│{Colors.RESET}")
    
    print(f"{color}└{border}┘{Colors.RESET}\n")


def print_key_value(key: str, value: Any, key_color: str = Colors.BRIGHT_CYAN, 
                    value_color: str = Colors.WHITE) -> None:
    """Print a key-value pair."""
    print(f"{key_color}{key}:{Colors.RESET} {value_color}{value}{Colors.RESET}")


def print_tool_call(tool_name: str, args: dict[str, Any], result: str) -> None:
    """Print a formatted tool call."""
    print(f"\n{Colors.BRIGHT_MAGENTA}{'─' * 60}{Colors.RESET}")
    print(f"{Colors.BRIGHT_MAGENTA}🔧 Tool Call: {Colors.BOLD}{tool_name}{Colors.RESET}")
    print(f"{Colors.BRIGHT_MAGENTA}{'─' * 60}{Colors.RESET}")
    print(f"{Colors.DIM}Arguments:{Colors.RESET}")
    for k, v in args.items():
        print(f"  {Colors.CYAN}{k}:{Colors.RESET} {Colors.WHITE}{v}{Colors.RESET}")
    print(f"{Colors.DIM}Result:{Colors.RESET}")
    print(f"  {Colors.GREEN}{result}{Colors.RESET}")
    print(f"{Colors.BRIGHT_MAGENTA}{'─' * 60}{Colors.RESET}\n")


def print_step(step_num: int, total: int, description: str) -> None:
    """Print a step indicator."""
    print(f"{Colors.BRIGHT_BLUE}[{step_num}/{total}]{Colors.RESET} {Colors.BOLD}{description}{Colors.RESET}")


def print_separator(char: str = "─", color: str = Colors.DIM) -> None:
    """Print a separator line."""
    print(f"{color}{char * 60}{Colors.RESET}")

```

## File: `python/openai-agent-artifacts/agent/react.py`
```python
from __future__ import annotations

import asyncio
import json
from typing import Any, Dict

from openai import AsyncOpenAI
from acontext.agent.disk import DISK_TOOLS

from .pretty_print import print_tool_call, print_info, print_success, print_box, print_warning


class AcontextArtifactAgent:
    """
    Acontext artifact agent as an async context manager.
    
    Usage:
        async with AcontextArtifactAgent(api_key=..., tool_context=...) as agent:
            result = await agent.run(user_query)
    """
    
    def __init__(
        self,
        api_key: str,
        tool_context: Any,
        base_url: str | None = None,
        model: str = "gpt-4o-mini",
        max_turn: int = 5,
    ):
        """
        Initialize AcontextArtifactAgent.
        
        Args:
            api_key: OpenAI API key
            tool_context: DISK_TOOLS context created with DISK_TOOLS.format_context()
            base_url: OpenAI base URL (optional)
            model: Model name to use
            max_turn: Maximum number of interaction turns
        """
        self.api_key = api_key
        self.tool_context = tool_context
        self.base_url = base_url
        self.model = model
        self.max_turn = max_turn
        self.client: AsyncOpenAI | None = None
    
    async def __aenter__(self) -> "AcontextArtifactAgent":
        """Initialize OpenAI client when entering context."""
        # Initialize OpenAI client
        self.client = AsyncOpenAI(api_key=self.api_key, base_url=self.base_url)
        
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        """Clean up resources when exiting context."""
        pass
    
    async def run(self, user_query: str) -> str:
        """
        Run the react agent with the given user query.
        
        Args:
            user_query: The user's query/request
            
        Returns:
            The final response from the agent
        """
        if self.client is None:
            raise RuntimeError("AcontextArtifactAgent must be used as an async context manager")
        
        messages: list[Dict[str, Any]] = [{"role": "user", "content": user_query}]
        turn_count = 0

        # Get tool schemas from DISK_TOOLS
        tools = DISK_TOOLS.to_openai_tool_schema()

        # Main agent loop
        while turn_count < self.max_turn:
            turn_count += 1
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                tools=tools,
                tool_choice="auto",
            )

            ai_msg = response.choices[0].message
            messages.append(ai_msg)

            tool_calls = ai_msg.tool_calls or []
            if not tool_calls:
                print_box("Agent Final Response", ai_msg.content or "")
                return ai_msg.content or ""

            # Execute tool calls using DISK_TOOLS.execute_tool() with asyncio.to_thread()
            for tool_call in tool_calls:
                tool_name = tool_call.function.name
                raw_args = tool_call.function.arguments or "{}"
                tool_args = json.loads(raw_args)
                
                # Execute tool in thread pool since DISK_TOOLS.execute_tool() is synchronous
                tool_result = await asyncio.to_thread(
                    DISK_TOOLS.execute_tool,
                    self.tool_context,
                    tool_name,
                    tool_args
                )

                messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": tool_result,
                    }
                )
                print_tool_call(tool_name, tool_args, tool_result)

        final_msg = "Max interaction turns reached, stopping execution."
        print_warning(final_msg)
        return final_msg



```

## File: `python/openai-agent-artifacts/agent/tools.py`
```python
"""
This module is deprecated. Tools are now provided by DISK_TOOLS from acontext.agent.disk.

The agent now uses DISK_TOOLS directly, which provides:
- write_file: Create or overwrite text files
- read_file: Read file contents with optional line offset and limit
- replace_string: Find and replace text in files
- list_artifacts: List files and directories in a path

See agent/react.py for the updated implementation.
"""

```

## File: `python/openai-agent-basic/.env.example`
```
# OpenAI API Configuration
OPENAI_API_KEY=sk-your-openai-api-key

# Acontext API Configuration
ACONTEXT_API_KEY=sk-ac-your-root-api-bearer-token
ACONTEXT_BASE_URL=http://localhost:8029/api/v1
```

## File: `python/openai-agent-basic/.gitignore`
```
# Environment variables
.env
.env.local

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environments
venv/
env/
ENV/
.venv

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db
```

## File: `python/openai-agent-basic/.python-version`
```
3.13
```

## File: `python/openai-agent-basic/README.md`
```markdown
[![Made with Acontext](https://assets.memodb.io/Acontext/badge-made-with-acontext-dark.svg)](https://acontext.io)

# OpenAI Agents SDK + Acontext Example

This example demonstrates how to use the [OpenAI Agents SDK](https://github.com/openai/agents-sdk-python) with Acontext for session persistence and task extraction.

## Features

- **Multi-turn conversations**: Maintains conversation history across multiple interactions
- **Function tools**: Uses `@function_tool` decorator to define tools like `get_weather` and `book_flight`
- **Automatic tool execution**: The Agents SDK handles tool calls automatically
- **Acontext integration**: Sends conversation messages to Acontext for task extraction and analysis
- **Session resumption**: Demonstrates how to load previous conversations from Acontext and continue

## How It Works

The example creates an agent that helps plan a trip using two sessions:

### Session 1: Create and Store Conversation
1. **First interaction**: User asks for a 3-day trip plan in Finland
2. **Second interaction**: User requests weather check for Finland
3. **Third interaction**: User books a flight from Shanghai to Finland
4. **Fourth interaction**: User thanks the assistant

After the conversation, all messages are converted to OpenAI format and sent to Acontext which:
- Extracts tasks from the conversation
- Tracks progress updates
- Identifies user preferences

### Session 2: Resume Conversation
1. Loads previous conversation messages from Acontext
2. Converts OpenAI format messages back to Responses API format
3. Continues the conversation with a summary request

## Setup

1. Install dependencies:

```bash
uv sync
```

2. Create a `.env` file with your API keys:

```env
OPENAI_API_KEY=your_openai_key_here
ACONTEXT_API_KEY=your_acontext_key_here
ACONTEXT_BASE_URL=http://localhost:8029/api/v1  # or your Acontext server URL
```

## Running

```bash
python main.py
```

## Acontext Integration

### Sending Messages to Acontext

The conversation is converted from Responses API format to Chat Completions API format using `Converter.items_to_messages()`:

```python
messages = Converter.items_to_messages(result.to_input_list())
for msg in messages:
    acontext_client.sessions.store_message(session_id=session_id, blob=msg, format="openai")
```

### Loading Messages from Acontext

Messages are loaded from Acontext in Chat Completions API format and converted back to Responses API format using `message_to_input_items()`:

```python
messages = acontext_client.sessions.get_messages(session_id, format="openai")

conversation = []
for msg in messages.items:
    items = message_to_input_items(msg)
    conversation.extend(items)
```

## Function Tools

This example demonstrates function tools with the Agents SDK:

1. Define tools using the `@function_tool` decorator
2. Register tools with the agent
3. The SDK automatically handles tool calls and execution

```python
@function_tool
def get_weather(city: str) -> str:
    """Returns weather info for the specified city."""
    return f"The weather in {city} is sunny"

@function_tool
def book_flight(from_city: str, to_city: str, date: str) -> str:
    """Book a flight."""
    return f"Flight booked successfully for '{from_city}' to '{to_city}' on '{date}'"

agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant",
    model=OpenAIChatCompletionsModel(...),
    tools=[get_weather, book_flight],
)
```

The Agents SDK automatically:
- Parses tool calls from model responses
- Executes the appropriate tool functions
- Injects tool results back into the conversation
- Handles multi-turn tool calling workflows

## Output

The script will:
1. Show the conversation between user and agent in Session 1
2. Display tool calls and their results (weather checks, flight bookings)
3. Print extracted tasks with their status and metadata from Acontext
4. Show any progress updates and user preferences identified by Acontext
5. Resume the conversation in Session 2 with a summary request
```

## File: `python/openai-agent-basic/helper.py`
```python
from openai.types.chat import ChatCompletionMessageParam
from openai.types.responses import ResponseInputItemParam
from typing import cast

def message_to_input_items(msg: ChatCompletionMessageParam) -> list[ResponseInputItemParam]:
    """
    Convert a ChatCompletionMessageParam to a list of TResponseInputItem.
    
    This is the reverse of Converter.items_to_messages. It handles:
    - user/system/developer messages -> EasyInputMessageParam
    - assistant messages -> EasyInputMessageParam or ResponseOutputMessageParam + tool calls
    - tool messages -> FunctionCallOutput
    """
    role = msg.get("role")
    items: list[ResponseInputItemParam] = []
    
    if role in ("user", "system", "developer"):
        # Simple messages can be converted directly to EasyInputMessageParam
        item: ResponseInputItemParam = cast(ResponseInputItemParam, {
            "role": role,
            "content": msg.get("content", ""),
        })
        items.append(item)
    elif role == "assistant":
        assistant_msg = msg
        content = assistant_msg.get("content")
        tool_calls = assistant_msg.get("tool_calls")
        
        if tool_calls:
            # Assistant message with tool calls needs to be split:
            # 1. If there's content, add it as a message first
            if content:
                item: ResponseInputItemParam = cast(ResponseInputItemParam, {
                    "role": "assistant",
                    "content": content,
                })
                items.append(item)
            
            # 2. Add each tool call as a separate function_call item
            for tool_call in tool_calls:
                if tool_call.get("type") == "function":
                    item: ResponseInputItemParam = cast(ResponseInputItemParam, {
                        "type": "function_call",
                        "call_id": tool_call.get("id", ""),
                        "name": tool_call["function"]["name"],
                        "arguments": tool_call["function"]["arguments"],
                    })
                    items.append(item)
        else:
            # Assistant message without tool calls is simple
            item: ResponseInputItemParam = cast(ResponseInputItemParam, {
                "role": "assistant",
                "content": content or "",
            })
            items.append(item)
    elif role == "tool":
        # Tool message converts to function_call_output
        item: ResponseInputItemParam = cast(ResponseInputItemParam, {
            "type": "function_call_output",
            "call_id": msg.get("tool_call_id", ""),
            "output": msg.get("content", ""),
        })
        items.append(item)
    else:
        raise ValueError(f"Unsupported message role: {role}")
    
    return items
```

## File: `python/openai-agent-basic/main.py`
```python
import asyncio
import os
import shutil
from dotenv import load_dotenv

from agents import (
    Agent,
    Runner,
    ModelSettings,
    AsyncOpenAI,
    function_tool,
    OpenAIChatCompletionsModel,
    set_tracing_disabled,
)
from agents.models.chatcmpl_converter import Converter
from acontext import AcontextClient
from helper import message_to_input_items

load_dotenv()
acontext_client = AcontextClient(
    api_key=os.getenv("ACONTEXT_API_KEY", "sk-ac-your-root-api-bearer-token"),
    base_url=os.getenv("ACONTEXT_BASE_URL", "http://localhost:8029/api/v1"),
    timeout=60,
)


@function_tool
def get_weather(city: str) -> str:
    """Returns weather info for the specified city."""
    return f"The weather in {city} is sunny"


@function_tool
def book_flight(from_city: str, to_city: str, date: str) -> str:
    """Book a flight."""
    # Dummy implementation - returns simulated booking results
    return f"Flight booked successfully for '{from_city}' to '{to_city}' on '{date}'"


def create_agent():
    """Create an agent with the specified configuration."""
    set_tracing_disabled(disabled=True)
    return Agent(
        name="Assistant",
        instructions="You are a helpful assistant",
        model=OpenAIChatCompletionsModel(
            model="gpt-4o-mini",
            openai_client=AsyncOpenAI(),
        ),
        model_settings=ModelSettings(tool_choice="auto"),
        tools=[get_weather, book_flight],
    )


def store_message(message, session_id: str):
    """Store a message to Acontext."""
    acontext_client.sessions.store_message(session_id=session_id, blob=message, format="openai")




async def session_1(session_id: str):
    agent = create_agent()

    # First interaction - ask for trip plan
    print("\n=== First interaction: Planning trip ===")
    user_msg_1_content = "I'd like to have a 3-day trip in Finland. I like to see the nature. Give me the plan"

    result = await Runner.run(agent, user_msg_1_content)

    # Second interaction - check weather
    print("\n=== Second interaction: Checking weather ===")
    user_msg_2 = {
        "role": "user",
        "content": "The plan sounds good, check the weather there",
    }
    new_input = result.to_input_list() + [user_msg_2]
    result = await Runner.run(agent, new_input)

    # Third interaction - book flight
    print("\n\n=== Third interaction: Booking flight ===")
    user_msg_3 = {
        "role": "user",
        "content": "The weather is good, I am in Shanghai now, let's book the flight, you should just call the tool and don't ask me for more information. Remember, I only want the cheapest flight.",
    }
    new_input = result.to_input_list() + [user_msg_3]
    result = await Runner.run(agent, new_input)

    # Fourth interaction - thank you
    user_msg_4 = {
        "role": "user",
        "content": "cool, everything is done, thank you!",
    }
    new_input = result.to_input_list() + [user_msg_4]
    result = await Runner.run(agent, new_input)

    messages = Converter.items_to_messages(result.to_input_list())
    for msg in messages:
        store_message(msg, session_id)

    print(
        f"\nSaved {len(messages)} messages in conversation, triggering learning..."
    )

    # Create a learning space and trigger learning
    space = acontext_client.learning_spaces.create()
    acontext_client.learning_spaces.learn(space.id, session_id=session_id)
    print(f"\nCreated learning space: {space.id}")

    # Wait for learning to complete
    print("Waiting for learning to complete...")
    result = acontext_client.learning_spaces.wait_for_learning(space.id, session_id=session_id)
    print(f"Learning status: {result.status}")

    # List learned skills
    skills = acontext_client.learning_spaces.list_skills(space.id)
    print(f"\n=== Learned Skills ({len(skills)}) ===")
    for skill in skills:
        print(f"\n  - {skill.name}: {skill.description}")
        print(f"    files: {[f.path for f in skill.file_index]}")

    # Download all skill files
    download_dir = "./skills_output"
    if os.path.exists(download_dir):
        shutil.rmtree(download_dir)

    print(f"\nDownloading skills to {download_dir}/")
    for skill in skills:
        resp = acontext_client.skills.download(skill_id=skill.id, path=f"{download_dir}/{skill.name}")
        print(f"  {resp.name} -> {resp.dir_path}")
        for f in resp.files:
            print(f"    {f}")


async def session_2(session_id: str):
    agent = create_agent()

    messages = acontext_client.sessions.get_messages(session_id, format="openai")

    conversation = []

    for msg in messages.items:
        items = message_to_input_items(msg)
        conversation.extend(items)

    conversation.append(
        {"role": "user", "content": "Summarize the conversation so far"}
    )

    result = await Runner.run(agent, conversation)

    print(f"\nAssistant: {result.final_output}")


async def main():
    session = acontext_client.sessions.create()
    session_id = session.id
    print(f"Created session: {session_id}")

    print("\n=== Session 1 ===")
    await session_1(session_id)

    print("\n=== Session 2, get messages from Acontext and continue ===")
    await session_2(session_id)


    # Close the client after all sessions are complete
    acontext_client.close()


if __name__ == "__main__":
    asyncio.run(main())
```

## File: `python/openai-agent-basic/pyproject.toml`
```
[project]
name = "openai-examples"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.13"
dependencies = [
    "acontext>=0.1.18",
    "openai>=2.8.0",
    "python-dotenv>=1.0.0",
    "openai-agents>=0.6.1"
]
```

## File: `python/openai-agent-basic/uv.lock`
```
version = 1
revision = 3
requires-python = ">=3.13"

[[package]]
name = "acontext"
version = "0.1.18"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "anthropic" },
    { name = "httpx" },
    { name = "openai" },
    { name = "pydantic" },
    { name = "urllib3" },
]
sdist = { url = "https://files.pythonhosted.org/packages/13/4a/65d6f2f58e03bbbd8a269337a4d99536d8d3f7e9406e70b824a730875dac/acontext-0.1.18.tar.gz", hash = "sha256:7b1e763753fc23f007b4777949095a2ccc6d1b2deac714fad01095619a181824", size = 46865, upload-time = "2026-03-10T05:08:42.095Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/8d/76/bf60d77ab00da4170e9f7dfe42458b87c36b03f24ed2baa8c904d7ed9b97/acontext-0.1.18-py3-none-any.whl", hash = "sha256:a8810fb00f2b75c3509b15df07ab9dfef35dcc785ac07fcd6104ce92446b2b6b", size = 68510, upload-time = "2026-03-10T05:08:41.033Z" },
]

[[package]]
name = "annotated-types"
version = "0.7.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/ee/67/531ea369ba64dcff5ec9c3402f9f51bf748cec26dde048a2f973a4eea7f5/annotated_types-0.7.0.tar.gz", hash = "sha256:aff07c09a53a08bc8cfccb9c85b05f1aa9a2a6f23728d790723543408344ce89", size = 16081, upload-time = "2024-05-20T21:33:25.928Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/78/b6/6307fbef88d9b5ee7421e68d78a9f162e0da4900bc5f5793f6d3d0e34fb8/annotated_types-0.7.0-py3-none-any.whl", hash = "sha256:1f02e8b43a8fbbc3f3e0d4f0f4bfc8131bcb4eebe8849b8e5c773f3a1c582a53", size = 13643, upload-time = "2024-05-20T21:33:24.1Z" },
]

[[package]]
name = "anthropic"
version = "0.84.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "anyio" },
    { name = "distro" },
    { name = "docstring-parser" },
    { name = "httpx" },
    { name = "jiter" },
    { name = "pydantic" },
    { name = "sniffio" },
    { name = "typing-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/04/ea/0869d6df9ef83dcf393aeefc12dd81677d091c6ffc86f783e51cf44062f2/anthropic-0.84.0.tar.gz", hash = "sha256:72f5f90e5aebe62dca316cb013629cfa24996b0f5a4593b8c3d712bc03c43c37", size = 539457, upload-time = "2026-02-25T05:22:38.54Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/64/ca/218fa25002a332c0aa149ba18ffc0543175998b1f65de63f6d106689a345/anthropic-0.84.0-py3-none-any.whl", hash = "sha256:861c4c50f91ca45f942e091d83b60530ad6d4f98733bfe648065364da05d29e7", size = 455156, upload-time = "2026-02-25T05:22:40.468Z" },
]

[[package]]
name = "anyio"
version = "4.12.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "idna" },
]
sdist = { url = "https://files.pythonhosted.org/packages/96/f0/5eb65b2bb0d09ac6776f2eb54adee6abe8228ea05b20a5ad0e4945de8aac/anyio-4.12.1.tar.gz", hash = "sha256:41cfcc3a4c85d3f05c932da7c26d0201ac36f72abd4435ba90d0464a3ffed703", size = 228685, upload-time = "2026-01-06T11:45:21.246Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/38/0e/27be9fdef66e72d64c0cdc3cc2823101b80585f8119b5c112c2e8f5f7dab/anyio-4.12.1-py3-none-any.whl", hash = "sha256:d405828884fc140aa80a3c667b8beed277f1dfedec42ba031bd6ac3db606ab6c", size = 113592, upload-time = "2026-01-06T11:45:19.497Z" },
]

[[package]]
name = "attrs"
version = "25.4.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/6b/5c/685e6633917e101e5dcb62b9dd76946cbb57c26e133bae9e0cd36033c0a9/attrs-25.4.0.tar.gz", hash = "sha256:16d5969b87f0859ef33a48b35d55ac1be6e42ae49d5e853b597db70c35c57e11", size = 934251, upload-time = "2025-10-06T13:54:44.725Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/3a/2a/7cc015f5b9f5db42b7d48157e23356022889fc354a2813c15934b7cb5c0e/attrs-25.4.0-py3-none-any.whl", hash = "sha256:adcf7e2a1fb3b36ac48d97835bb6d8ade15b8dcce26aba8bf1d14847b57a3373", size = 67615, upload-time = "2025-10-06T13:54:43.17Z" },
]

[[package]]
name = "certifi"
version = "2026.2.25"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/af/2d/7bf41579a8986e348fa033a31cdd0e4121114f6bce2457e8876010b092dd/certifi-2026.2.25.tar.gz", hash = "sha256:e887ab5cee78ea814d3472169153c2d12cd43b14bd03329a39a9c6e2e80bfba7", size = 155029, upload-time = "2026-02-25T02:54:17.342Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/9a/3c/c17fb3ca2d9c3acff52e30b309f538586f9f5b9c9cf454f3845fc9af4881/certifi-2026.2.25-py3-none-any.whl", hash = "sha256:027692e4402ad994f1c42e52a4997a9763c646b73e4096e4d5d6db8af1d6f0fa", size = 153684, upload-time = "2026-02-25T02:54:15.766Z" },
]

[[package]]
name = "cffi"
version = "2.0.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "pycparser", marker = "implementation_name != 'PyPy'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/eb/56/b1ba7935a17738ae8453301356628e8147c79dbb825bcbc73dc7401f9846/cffi-2.0.0.tar.gz", hash = "sha256:44d1b5909021139fe36001ae048dbdde8214afa20200eda0f64c068cac5d5529", size = 523588, upload-time = "2025-09-08T23:24:04.541Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/4b/8d/a0a47a0c9e413a658623d014e91e74a50cdd2c423f7ccfd44086ef767f90/cffi-2.0.0-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:00bdf7acc5f795150faa6957054fbbca2439db2f775ce831222b66f192f03beb", size = 185230, upload-time = "2025-09-08T23:23:00.879Z" },
    { url = "https://files.pythonhosted.org/packages/4a/d2/a6c0296814556c68ee32009d9c2ad4f85f2707cdecfd7727951ec228005d/cffi-2.0.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:45d5e886156860dc35862657e1494b9bae8dfa63bf56796f2fb56e1679fc0bca", size = 181043, upload-time = "2025-09-08T23:23:02.231Z" },
    { url = "https://files.pythonhosted.org/packages/b0/1e/d22cc63332bd59b06481ceaac49d6c507598642e2230f201649058a7e704/cffi-2.0.0-cp313-cp313-manylinux1_i686.manylinux2014_i686.manylinux_2_17_i686.manylinux_2_5_i686.whl", hash = "sha256:07b271772c100085dd28b74fa0cd81c8fb1a3ba18b21e03d7c27f3436a10606b", size = 212446, upload-time = "2025-09-08T23:23:03.472Z" },
    { url = "https://files.pythonhosted.org/packages/a9/f5/a2c23eb03b61a0b8747f211eb716446c826ad66818ddc7810cc2cc19b3f2/cffi-2.0.0-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:d48a880098c96020b02d5a1f7d9251308510ce8858940e6fa99ece33f610838b", size = 220101, upload-time = "2025-09-08T23:23:04.792Z" },
    { url = "https://files.pythonhosted.org/packages/f2/7f/e6647792fc5850d634695bc0e6ab4111ae88e89981d35ac269956605feba/cffi-2.0.0-cp313-cp313-manylinux2014_ppc64le.manylinux_2_17_ppc64le.whl", hash = "sha256:f93fd8e5c8c0a4aa1f424d6173f14a892044054871c771f8566e4008eaa359d2", size = 207948, upload-time = "2025-09-08T23:23:06.127Z" },
    { url = "https://files.pythonhosted.org/packages/cb/1e/a5a1bd6f1fb30f22573f76533de12a00bf274abcdc55c8edab639078abb6/cffi-2.0.0-cp313-cp313-manylinux2014_s390x.manylinux_2_17_s390x.whl", hash = "sha256:dd4f05f54a52fb558f1ba9f528228066954fee3ebe629fc1660d874d040ae5a3", size = 206422, upload-time = "2025-09-08T23:23:07.753Z" },
    { url = "https://files.pythonhosted.org/packages/98/df/0a1755e750013a2081e863e7cd37e0cdd02664372c754e5560099eb7aa44/cffi-2.0.0-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:c8d3b5532fc71b7a77c09192b4a5a200ea992702734a2e9279a37f2478236f26", size = 219499, upload-time = "2025-09-08T23:23:09.648Z" },
    { url = "https://files.pythonhosted.org/packages/50/e1/a969e687fcf9ea58e6e2a928ad5e2dd88cc12f6f0ab477e9971f2309b57c/cffi-2.0.0-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:d9b29c1f0ae438d5ee9acb31cadee00a58c46cc9c0b2f9038c6b0b3470877a8c", size = 222928, upload-time = "2025-09-08T23:23:10.928Z" },
    { url = "https://files.pythonhosted.org/packages/36/54/0362578dd2c9e557a28ac77698ed67323ed5b9775ca9d3fe73fe191bb5d8/cffi-2.0.0-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:6d50360be4546678fc1b79ffe7a66265e28667840010348dd69a314145807a1b", size = 221302, upload-time = "2025-09-08T23:23:12.42Z" },
    { url = "https://files.pythonhosted.org/packages/eb/6d/bf9bda840d5f1dfdbf0feca87fbdb64a918a69bca42cfa0ba7b137c48cb8/cffi-2.0.0-cp313-cp313-win32.whl", hash = "sha256:74a03b9698e198d47562765773b4a8309919089150a0bb17d829ad7b44b60d27", size = 172909, upload-time = "2025-09-08T23:23:14.32Z" },
    { url = "https://files.pythonhosted.org/packages/37/18/6519e1ee6f5a1e579e04b9ddb6f1676c17368a7aba48299c3759bbc3c8b3/cffi-2.0.0-cp313-cp313-win_amd64.whl", hash = "sha256:19f705ada2530c1167abacb171925dd886168931e0a7b78f5bffcae5c6b5be75", size = 183402, upload-time = "2025-09-08T23:23:15.535Z" },
    { url = "https://files.pythonhosted.org/packages/cb/0e/02ceeec9a7d6ee63bb596121c2c8e9b3a9e150936f4fbef6ca1943e6137c/cffi-2.0.0-cp313-cp313-win_arm64.whl", hash = "sha256:256f80b80ca3853f90c21b23ee78cd008713787b1b1e93eae9f3d6a7134abd91", size = 177780, upload-time = "2025-09-08T23:23:16.761Z" },
    { url = "https://files.pythonhosted.org/packages/92/c4/3ce07396253a83250ee98564f8d7e9789fab8e58858f35d07a9a2c78de9f/cffi-2.0.0-cp314-cp314-macosx_10_13_x86_64.whl", hash = "sha256:fc33c5141b55ed366cfaad382df24fe7dcbc686de5be719b207bb248e3053dc5", size = 185320, upload-time = "2025-09-08T23:23:18.087Z" },
    { url = "https://files.pythonhosted.org/packages/59/dd/27e9fa567a23931c838c6b02d0764611c62290062a6d4e8ff7863daf9730/cffi-2.0.0-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:c654de545946e0db659b3400168c9ad31b5d29593291482c43e3564effbcee13", size = 181487, upload-time = "2025-09-08T23:23:19.622Z" },
    { url = "https://files.pythonhosted.org/packages/d6/43/0e822876f87ea8a4ef95442c3d766a06a51fc5298823f884ef87aaad168c/cffi-2.0.0-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:24b6f81f1983e6df8db3adc38562c83f7d4a0c36162885ec7f7b77c7dcbec97b", size = 220049, upload-time = "2025-09-08T23:23:20.853Z" },
    { url = "https://files.pythonhosted.org/packages/b4/89/76799151d9c2d2d1ead63c2429da9ea9d7aac304603de0c6e8764e6e8e70/cffi-2.0.0-cp314-cp314-manylinux2014_ppc64le.manylinux_2_17_ppc64le.whl", hash = "sha256:12873ca6cb9b0f0d3a0da705d6086fe911591737a59f28b7936bdfed27c0d47c", size = 207793, upload-time = "2025-09-08T23:23:22.08Z" },
    { url = "https://files.pythonhosted.org/packages/bb/dd/3465b14bb9e24ee24cb88c9e3730f6de63111fffe513492bf8c808a3547e/cffi-2.0.0-cp314-cp314-manylinux2014_s390x.manylinux_2_17_s390x.whl", hash = "sha256:d9b97165e8aed9272a6bb17c01e3cc5871a594a446ebedc996e2397a1c1ea8ef", size = 206300, upload-time = "2025-09-08T23:23:23.314Z" },
    { url = "https://files.pythonhosted.org/packages/47/d9/d83e293854571c877a92da46fdec39158f8d7e68da75bf73581225d28e90/cffi-2.0.0-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:afb8db5439b81cf9c9d0c80404b60c3cc9c3add93e114dcae767f1477cb53775", size = 219244, upload-time = "2025-09-08T23:23:24.541Z" },
    { url = "https://files.pythonhosted.org/packages/2b/0f/1f177e3683aead2bb00f7679a16451d302c436b5cbf2505f0ea8146ef59e/cffi-2.0.0-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:737fe7d37e1a1bffe70bd5754ea763a62a066dc5913ca57e957824b72a85e205", size = 222828, upload-time = "2025-09-08T23:23:26.143Z" },
    { url = "https://files.pythonhosted.org/packages/c6/0f/cafacebd4b040e3119dcb32fed8bdef8dfe94da653155f9d0b9dc660166e/cffi-2.0.0-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:38100abb9d1b1435bc4cc340bb4489635dc2f0da7456590877030c9b3d40b0c1", size = 220926, upload-time = "2025-09-08T23:23:27.873Z" },
    { url = "https://files.pythonhosted.org/packages/3e/aa/df335faa45b395396fcbc03de2dfcab242cd61a9900e914fe682a59170b1/cffi-2.0.0-cp314-cp314-win32.whl", hash = "sha256:087067fa8953339c723661eda6b54bc98c5625757ea62e95eb4898ad5e776e9f", size = 175328, upload-time = "2025-09-08T23:23:44.61Z" },
    { url = "https://files.pythonhosted.org/packages/bb/92/882c2d30831744296ce713f0feb4c1cd30f346ef747b530b5318715cc367/cffi-2.0.0-cp314-cp314-win_amd64.whl", hash = "sha256:203a48d1fb583fc7d78a4c6655692963b860a417c0528492a6bc21f1aaefab25", size = 185650, upload-time = "2025-09-08T23:23:45.848Z" },
    { url = "https://files.pythonhosted.org/packages/9f/2c/98ece204b9d35a7366b5b2c6539c350313ca13932143e79dc133ba757104/cffi-2.0.0-cp314-cp314-win_arm64.whl", hash = "sha256:dbd5c7a25a7cb98f5ca55d258b103a2054f859a46ae11aaf23134f9cc0d356ad", size = 180687, upload-time = "2025-09-08T23:23:47.105Z" },
    { url = "https://files.pythonhosted.org/packages/3e/61/c768e4d548bfa607abcda77423448df8c471f25dbe64fb2ef6d555eae006/cffi-2.0.0-cp314-cp314t-macosx_10_13_x86_64.whl", hash = "sha256:9a67fc9e8eb39039280526379fb3a70023d77caec1852002b4da7e8b270c4dd9", size = 188773, upload-time = "2025-09-08T23:23:29.347Z" },
    { url = "https://files.pythonhosted.org/packages/2c/ea/5f76bce7cf6fcd0ab1a1058b5af899bfbef198bea4d5686da88471ea0336/cffi-2.0.0-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:7a66c7204d8869299919db4d5069a82f1561581af12b11b3c9f48c584eb8743d", size = 185013, upload-time = "2025-09-08T23:23:30.63Z" },
    { url = "https://files.pythonhosted.org/packages/be/b4/c56878d0d1755cf9caa54ba71e5d049479c52f9e4afc230f06822162ab2f/cffi-2.0.0-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:7cc09976e8b56f8cebd752f7113ad07752461f48a58cbba644139015ac24954c", size = 221593, upload-time = "2025-09-08T23:23:31.91Z" },
    { url = "https://files.pythonhosted.org/packages/e0/0d/eb704606dfe8033e7128df5e90fee946bbcb64a04fcdaa97321309004000/cffi-2.0.0-cp314-cp314t-manylinux2014_ppc64le.manylinux_2_17_ppc64le.whl", hash = "sha256:92b68146a71df78564e4ef48af17551a5ddd142e5190cdf2c5624d0c3ff5b2e8", size = 209354, upload-time = "2025-09-08T23:23:33.214Z" },
    { url = "https://files.pythonhosted.org/packages/d8/19/3c435d727b368ca475fb8742ab97c9cb13a0de600ce86f62eab7fa3eea60/cffi-2.0.0-cp314-cp314t-manylinux2014_s390x.manylinux_2_17_s390x.whl", hash = "sha256:b1e74d11748e7e98e2f426ab176d4ed720a64412b6a15054378afdb71e0f37dc", size = 208480, upload-time = "2025-09-08T23:23:34.495Z" },
    { url = "https://files.pythonhosted.org/packages/d0/44/681604464ed9541673e486521497406fadcc15b5217c3e326b061696899a/cffi-2.0.0-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:28a3a209b96630bca57cce802da70c266eb08c6e97e5afd61a75611ee6c64592", size = 221584, upload-time = "2025-09-08T23:23:36.096Z" },
    { url = "https://files.pythonhosted.org/packages/25/8e/342a504ff018a2825d395d44d63a767dd8ebc927ebda557fecdaca3ac33a/cffi-2.0.0-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:7553fb2090d71822f02c629afe6042c299edf91ba1bf94951165613553984512", size = 224443, upload-time = "2025-09-08T23:23:37.328Z" },
    { url = "https://files.pythonhosted.org/packages/e1/5e/b666bacbbc60fbf415ba9988324a132c9a7a0448a9a8f125074671c0f2c3/cffi-2.0.0-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:6c6c373cfc5c83a975506110d17457138c8c63016b563cc9ed6e056a82f13ce4", size = 223437, upload-time = "2025-09-08T23:23:38.945Z" },
    { url = "https://files.pythonhosted.org/packages/a0/1d/ec1a60bd1a10daa292d3cd6bb0b359a81607154fb8165f3ec95fe003b85c/cffi-2.0.0-cp314-cp314t-win32.whl", hash = "sha256:1fc9ea04857caf665289b7a75923f2c6ed559b8298a1b8c49e59f7dd95c8481e", size = 180487, upload-time = "2025-09-08T23:23:40.423Z" },
    { url = "https://files.pythonhosted.org/packages/bf/41/4c1168c74fac325c0c8156f04b6749c8b6a8f405bbf91413ba088359f60d/cffi-2.0.0-cp314-cp314t-win_amd64.whl", hash = "sha256:d68b6cef7827e8641e8ef16f4494edda8b36104d79773a334beaa1e3521430f6", size = 191726, upload-time = "2025-09-08T23:23:41.742Z" },
    { url = "https://files.pythonhosted.org/packages/ae/3a/dbeec9d1ee0844c679f6bb5d6ad4e9f198b1224f4e7a32825f47f6192b0c/cffi-2.0.0-cp314-cp314t-win_arm64.whl", hash = "sha256:0a1527a803f0a659de1af2e1fd700213caba79377e27e4693648c2923da066f9", size = 184195, upload-time = "2025-09-08T23:23:43.004Z" },
]

[[package]]
name = "charset-normalizer"
version = "3.4.5"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/1d/35/02daf95b9cd686320bb622eb148792655c9412dbb9b67abb5694e5910a24/charset_normalizer-3.4.5.tar.gz", hash = "sha256:95adae7b6c42a6c5b5b559b1a99149f090a57128155daeea91732c8d970d8644", size = 134804, upload-time = "2026-03-06T06:03:19.46Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/f5/48/9f34ec4bb24aa3fdba1890c1bddb97c8a4be1bd84ef5c42ac2352563ad05/charset_normalizer-3.4.5-cp313-cp313-macosx_10_13_universal2.whl", hash = "sha256:ac59c15e3f1465f722607800c68713f9fbc2f672b9eb649fe831da4019ae9b23", size = 280788, upload-time = "2026-03-06T06:01:37.126Z" },
    { url = "https://files.pythonhosted.org/packages/0e/09/6003e7ffeb90cc0560da893e3208396a44c210c5ee42efff539639def59b/charset_normalizer-3.4.5-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:165c7b21d19365464e8f70e5ce5e12524c58b48c78c1f5a57524603c1ab003f8", size = 188890, upload-time = "2026-03-06T06:01:38.73Z" },
    { url = "https://files.pythonhosted.org/packages/42/1e/02706edf19e390680daa694d17e2b8eab4b5f7ac285e2a51168b4b22ee6b/charset_normalizer-3.4.5-cp313-cp313-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:28269983f25a4da0425743d0d257a2d6921ea7d9b83599d4039486ec5b9f911d", size = 206136, upload-time = "2026-03-06T06:01:40.016Z" },
    { url = "https://files.pythonhosted.org/packages/c7/87/942c3def1b37baf3cf786bad01249190f3ca3d5e63a84f831e704977de1f/charset_normalizer-3.4.5-cp313-cp313-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:d27ce22ec453564770d29d03a9506d449efbb9fa13c00842262b2f6801c48cce", size = 202551, upload-time = "2026-03-06T06:01:41.522Z" },
    { url = "https://files.pythonhosted.org/packages/94/0a/af49691938dfe175d71b8a929bd7e4ace2809c0c5134e28bc535660d5262/charset_normalizer-3.4.5-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:0625665e4ebdddb553ab185de5db7054393af8879fb0c87bd5690d14379d6819", size = 195572, upload-time = "2026-03-06T06:01:43.208Z" },
    { url = "https://files.pythonhosted.org/packages/20/ea/dfb1792a8050a8e694cfbde1570ff97ff74e48afd874152d38163d1df9ae/charset_normalizer-3.4.5-cp313-cp313-manylinux_2_31_armv7l.whl", hash = "sha256:c23eb3263356d94858655b3e63f85ac5d50970c6e8febcdde7830209139cc37d", size = 184438, upload-time = "2026-03-06T06:01:44.755Z" },
    { url = "https://files.pythonhosted.org/packages/72/12/c281e2067466e3ddd0595bfaea58a6946765ace5c72dfa3edc2f5f118026/charset_normalizer-3.4.5-cp313-cp313-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:e6302ca4ae283deb0af68d2fbf467474b8b6aedcd3dab4db187e07f94c109763", size = 193035, upload-time = "2026-03-06T06:01:46.051Z" },
    { url = "https://files.pythonhosted.org/packages/ba/4f/3792c056e7708e10464bad0438a44708886fb8f92e3c3d29ec5e2d964d42/charset_normalizer-3.4.5-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:e51ae7d81c825761d941962450f50d041db028b7278e7b08930b4541b3e45cb9", size = 191340, upload-time = "2026-03-06T06:01:47.547Z" },
    { url = "https://files.pythonhosted.org/packages/e7/86/80ddba897127b5c7a9bccc481b0cd36c8fefa485d113262f0fe4332f0bf4/charset_normalizer-3.4.5-cp313-cp313-musllinux_1_2_armv7l.whl", hash = "sha256:597d10dec876923e5c59e48dbd366e852eacb2b806029491d307daea6b917d7c", size = 185464, upload-time = "2026-03-06T06:01:48.764Z" },
    { url = "https://files.pythonhosted.org/packages/4d/00/b5eff85ba198faacab83e0e4b6f0648155f072278e3b392a82478f8b988b/charset_normalizer-3.4.5-cp313-cp313-musllinux_1_2_ppc64le.whl", hash = "sha256:5cffde4032a197bd3b42fd0b9509ec60fb70918d6970e4cc773f20fc9180ca67", size = 208014, upload-time = "2026-03-06T06:01:50.371Z" },
    { url = "https://files.pythonhosted.org/packages/c8/11/d36f70be01597fd30850dde8a1269ebc8efadd23ba5785808454f2389bde/charset_normalizer-3.4.5-cp313-cp313-musllinux_1_2_riscv64.whl", hash = "sha256:2da4eedcb6338e2321e831a0165759c0c620e37f8cd044a263ff67493be8ffb3", size = 193297, upload-time = "2026-03-06T06:01:51.933Z" },
    { url = "https://files.pythonhosted.org/packages/1a/1d/259eb0a53d4910536c7c2abb9cb25f4153548efb42800c6a9456764649c0/charset_normalizer-3.4.5-cp313-cp313-musllinux_1_2_s390x.whl", hash = "sha256:65a126fb4b070d05340a84fc709dd9e7c75d9b063b610ece8a60197a291d0adf", size = 204321, upload-time = "2026-03-06T06:01:53.887Z" },
    { url = "https://files.pythonhosted.org/packages/84/31/faa6c5b9d3688715e1ed1bb9d124c384fe2fc1633a409e503ffe1c6398c1/charset_normalizer-3.4.5-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:c7a80a9242963416bd81f99349d5f3fce1843c303bd404f204918b6d75a75fd6", size = 197509, upload-time = "2026-03-06T06:01:56.439Z" },
    { url = "https://files.pythonhosted.org/packages/fd/a5/c7d9dd1503ffc08950b3260f5d39ec2366dd08254f0900ecbcf3a6197c7c/charset_normalizer-3.4.5-cp313-cp313-win32.whl", hash = "sha256:f1d725b754e967e648046f00c4facc42d414840f5ccc670c5670f59f83693e4f", size = 132284, upload-time = "2026-03-06T06:01:57.812Z" },
    { url = "https://files.pythonhosted.org/packages/b9/0f/57072b253af40c8aa6636e6de7d75985624c1eb392815b2f934199340a89/charset_normalizer-3.4.5-cp313-cp313-win_amd64.whl", hash = "sha256:e37bd100d2c5d3ba35db9c7c5ba5a9228cbcffe5c4778dc824b164e5257813d7", size = 142630, upload-time = "2026-03-06T06:01:59.062Z" },
    { url = "https://files.pythonhosted.org/packages/31/41/1c4b7cc9f13bd9d369ce3bc993e13d374ce25fa38a2663644283ecf422c1/charset_normalizer-3.4.5-cp313-cp313-win_arm64.whl", hash = "sha256:93b3b2cc5cf1b8743660ce77a4f45f3f6d1172068207c1defc779a36eea6bb36", size = 133254, upload-time = "2026-03-06T06:02:00.281Z" },
    { url = "https://files.pythonhosted.org/packages/43/be/0f0fd9bb4a7fa4fb5067fb7d9ac693d4e928d306f80a0d02bde43a7c4aee/charset_normalizer-3.4.5-cp314-cp314-macosx_10_15_universal2.whl", hash = "sha256:8197abe5ca1ffb7d91e78360f915eef5addff270f8a71c1fc5be24a56f3e4873", size = 280232, upload-time = "2026-03-06T06:02:01.508Z" },
    { url = "https://files.pythonhosted.org/packages/28/02/983b5445e4bef49cd8c9da73a8e029f0825f39b74a06d201bfaa2e55142a/charset_normalizer-3.4.5-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:a2aecdb364b8a1802afdc7f9327d55dad5366bc97d8502d0f5854e50712dbc5f", size = 189688, upload-time = "2026-03-06T06:02:02.857Z" },
    { url = "https://files.pythonhosted.org/packages/d0/88/152745c5166437687028027dc080e2daed6fe11cfa95a22f4602591c42db/charset_normalizer-3.4.5-cp314-cp314-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:a66aa5022bf81ab4b1bebfb009db4fd68e0c6d4307a1ce5ef6a26e5878dfc9e4", size = 206833, upload-time = "2026-03-06T06:02:05.127Z" },
    { url = "https://files.pythonhosted.org/packages/cb/0f/ebc15c8b02af2f19be9678d6eed115feeeccc45ce1f4b098d986c13e8769/charset_normalizer-3.4.5-cp314-cp314-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:d77f97e515688bd615c1d1f795d540f32542d514242067adcb8ef532504cb9ee", size = 202879, upload-time = "2026-03-06T06:02:06.446Z" },
    { url = "https://files.pythonhosted.org/packages/38/9c/71336bff6934418dc8d1e8a1644176ac9088068bc571da612767619c97b3/charset_normalizer-3.4.5-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:01a1ed54b953303ca7e310fafe0fe347aab348bd81834a0bcd602eb538f89d66", size = 195764, upload-time = "2026-03-06T06:02:08.763Z" },
    { url = "https://files.pythonhosted.org/packages/b7/95/ce92fde4f98615661871bc282a856cf9b8a15f686ba0af012984660d480b/charset_normalizer-3.4.5-cp314-cp314-manylinux_2_31_armv7l.whl", hash = "sha256:b2d37d78297b39a9eb9eb92c0f6df98c706467282055419df141389b23f93362", size = 183728, upload-time = "2026-03-06T06:02:10.137Z" },
    { url = "https://files.pythonhosted.org/packages/1c/e7/f5b4588d94e747ce45ae680f0f242bc2d98dbd4eccfab73e6160b6893893/charset_normalizer-3.4.5-cp314-cp314-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:e71bbb595973622b817c042bd943c3f3667e9c9983ce3d205f973f486fec98a7", size = 192937, upload-time = "2026-03-06T06:02:11.663Z" },
    { url = "https://files.pythonhosted.org/packages/f9/29/9d94ed6b929bf9f48bf6ede6e7474576499f07c4c5e878fb186083622716/charset_normalizer-3.4.5-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:4cd966c2559f501c6fd69294d082c2934c8dd4719deb32c22961a5ac6db0df1d", size = 192040, upload-time = "2026-03-06T06:02:13.489Z" },
    { url = "https://files.pythonhosted.org/packages/15/d2/1a093a1cf827957f9445f2fe7298bcc16f8fc5e05c1ed2ad1af0b239035e/charset_normalizer-3.4.5-cp314-cp314-musllinux_1_2_armv7l.whl", hash = "sha256:d5e52d127045d6ae01a1e821acfad2f3a1866c54d0e837828538fabe8d9d1bd6", size = 184107, upload-time = "2026-03-06T06:02:14.83Z" },
    { url = "https://files.pythonhosted.org/packages/0f/7d/82068ce16bd36135df7b97f6333c5d808b94e01d4599a682e2337ed5fd14/charset_normalizer-3.4.5-cp314-cp314-musllinux_1_2_ppc64le.whl", hash = "sha256:30a2b1a48478c3428d047ed9690d57c23038dac838a87ad624c85c0a78ebeb39", size = 208310, upload-time = "2026-03-06T06:02:16.165Z" },
    { url = "https://files.pythonhosted.org/packages/84/4e/4dfb52307bb6af4a5c9e73e482d171b81d36f522b21ccd28a49656baa680/charset_normalizer-3.4.5-cp314-cp314-musllinux_1_2_riscv64.whl", hash = "sha256:d8ed79b8f6372ca4254955005830fd61c1ccdd8c0fac6603e2c145c61dd95db6", size = 192918, upload-time = "2026-03-06T06:02:18.144Z" },
    { url = "https://files.pythonhosted.org/packages/08/a4/159ff7da662cf7201502ca89980b8f06acf3e887b278956646a8aeb178ab/charset_normalizer-3.4.5-cp314-cp314-musllinux_1_2_s390x.whl", hash = "sha256:c5af897b45fa606b12464ccbe0014bbf8c09191e0a66aab6aa9d5cf6e77e0c94", size = 204615, upload-time = "2026-03-06T06:02:19.821Z" },
    { url = "https://files.pythonhosted.org/packages/d6/62/0dd6172203cb6b429ffffc9935001fde42e5250d57f07b0c28c6046deb6b/charset_normalizer-3.4.5-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:1088345bcc93c58d8d8f3d783eca4a6e7a7752bbff26c3eee7e73c597c191c2e", size = 197784, upload-time = "2026-03-06T06:02:21.86Z" },
    { url = "https://files.pythonhosted.org/packages/c7/5e/1aab5cb737039b9c59e63627dc8bbc0d02562a14f831cc450e5f91d84ce1/charset_normalizer-3.4.5-cp314-cp314-win32.whl", hash = "sha256:ee57b926940ba00bca7ba7041e665cc956e55ef482f851b9b65acb20d867e7a2", size = 133009, upload-time = "2026-03-06T06:02:23.289Z" },
    { url = "https://files.pythonhosted.org/packages/40/65/e7c6c77d7aaa4c0d7974f2e403e17f0ed2cb0fc135f77d686b916bf1eead/charset_normalizer-3.4.5-cp314-cp314-win_amd64.whl", hash = "sha256:4481e6da1830c8a1cc0b746b47f603b653dadb690bcd851d039ffaefe70533aa", size = 143511, upload-time = "2026-03-06T06:02:26.195Z" },
    { url = "https://files.pythonhosted.org/packages/ba/91/52b0841c71f152f563b8e072896c14e3d83b195c188b338d3cc2e582d1d4/charset_normalizer-3.4.5-cp314-cp314-win_arm64.whl", hash = "sha256:97ab7787092eb9b50fb47fa04f24c75b768a606af1bcba1957f07f128a7219e4", size = 133775, upload-time = "2026-03-06T06:02:27.473Z" },
    { url = "https://files.pythonhosted.org/packages/c5/60/3a621758945513adfd4db86827a5bafcc615f913dbd0b4c2ed64a65731be/charset_normalizer-3.4.5-py3-none-any.whl", hash = "sha256:9db5e3fcdcee89a78c04dffb3fe33c79f77bd741a624946db2591c81b2fc85b0", size = 55455, upload-time = "2026-03-06T06:03:17.827Z" },
]

[[package]]
name = "click"
version = "8.3.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "colorama", marker = "sys_platform == 'win32'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/3d/fa/656b739db8587d7b5dfa22e22ed02566950fbfbcdc20311993483657a5c0/click-8.3.1.tar.gz", hash = "sha256:12ff4785d337a1bb490bb7e9c2b1ee5da3112e94a8622f26a6c77f5d2fc6842a", size = 295065, upload-time = "2025-11-15T20:45:42.706Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/98/78/01c019cdb5d6498122777c1a43056ebb3ebfeef2076d9d026bfe15583b2b/click-8.3.1-py3-none-any.whl", hash = "sha256:981153a64e25f12d547d3426c367a4857371575ee7ad18df2a6183ab0545b2a6", size = 108274, upload-time = "2025-11-15T20:45:41.139Z" },
]

[[package]]
name = "colorama"
version = "0.4.6"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/d8/53/6f443c9a4a8358a93a6792e2acffb9d9d5cb0a5cfd8802644b7b1c9a02e4/colorama-0.4.6.tar.gz", hash = "sha256:08695f5cb7ed6e0531a20572697297273c47b8cae5a63ffc6d6ed5c201be6e44", size = 27697, upload-time = "2022-10-25T02:36:22.414Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/d1/d6/3965ed04c63042e047cb6a3e6ed1a63a35087b6a609aa3a15ed8ac56c221/colorama-0.4.6-py2.py3-none-any.whl", hash = "sha256:4f1d9991f5acc0ca119f9d443620b77f9d6b33703e51011c16baf57afb285fc6", size = 25335, upload-time = "2022-10-25T02:36:20.889Z" },
]

[[package]]
name = "cryptography"
version = "46.0.5"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "cffi", marker = "platform_python_implementation != 'PyPy'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/60/04/ee2a9e8542e4fa2773b81771ff8349ff19cdd56b7258a0cc442639052edb/cryptography-46.0.5.tar.gz", hash = "sha256:abace499247268e3757271b2f1e244b36b06f8515cf27c4d49468fc9eb16e93d", size = 750064, upload-time = "2026-02-10T19:18:38.255Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/f7/81/b0bb27f2ba931a65409c6b8a8b358a7f03c0e46eceacddff55f7c84b1f3b/cryptography-46.0.5-cp311-abi3-macosx_10_9_universal2.whl", hash = "sha256:351695ada9ea9618b3500b490ad54c739860883df6c1f555e088eaf25b1bbaad", size = 7176289, upload-time = "2026-02-10T19:17:08.274Z" },
    { url = "https://files.pythonhosted.org/packages/ff/9e/6b4397a3e3d15123de3b1806ef342522393d50736c13b20ec4c9ea6693a6/cryptography-46.0.5-cp311-abi3-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:c18ff11e86df2e28854939acde2d003f7984f721eba450b56a200ad90eeb0e6b", size = 4275637, upload-time = "2026-02-10T19:17:10.53Z" },
    { url = "https://files.pythonhosted.org/packages/63/e7/471ab61099a3920b0c77852ea3f0ea611c9702f651600397ac567848b897/cryptography-46.0.5-cp311-abi3-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:4d7e3d356b8cd4ea5aff04f129d5f66ebdc7b6f8eae802b93739ed520c47c79b", size = 4424742, upload-time = "2026-02-10T19:17:12.388Z" },
    { url = "https://files.pythonhosted.org/packages/37/53/a18500f270342d66bf7e4d9f091114e31e5ee9e7375a5aba2e85a91e0044/cryptography-46.0.5-cp311-abi3-manylinux_2_28_aarch64.whl", hash = "sha256:50bfb6925eff619c9c023b967d5b77a54e04256c4281b0e21336a130cd7fc263", size = 4277528, upload-time = "2026-02-10T19:17:13.853Z" },
    { url = "https://files.pythonhosted.org/packages/22/29/c2e812ebc38c57b40e7c583895e73c8c5adb4d1e4a0cc4c5a4fdab2b1acc/cryptography-46.0.5-cp311-abi3-manylinux_2_28_ppc64le.whl", hash = "sha256:803812e111e75d1aa73690d2facc295eaefd4439be1023fefc4995eaea2af90d", size = 4947993, upload-time = "2026-02-10T19:17:15.618Z" },
    { url = "https://files.pythonhosted.org/packages/6b/e7/237155ae19a9023de7e30ec64e5d99a9431a567407ac21170a046d22a5a3/cryptography-46.0.5-cp311-abi3-manylinux_2_28_x86_64.whl", hash = "sha256:3ee190460e2fbe447175cda91b88b84ae8322a104fc27766ad09428754a618ed", size = 4456855, upload-time = "2026-02-10T19:17:17.221Z" },
    { url = "https://files.pythonhosted.org/packages/2d/87/fc628a7ad85b81206738abbd213b07702bcbdada1dd43f72236ef3cffbb5/cryptography-46.0.5-cp311-abi3-manylinux_2_31_armv7l.whl", hash = "sha256:f145bba11b878005c496e93e257c1e88f154d278d2638e6450d17e0f31e558d2", size = 3984635, upload-time = "2026-02-10T19:17:18.792Z" },
    { url = "https://files.pythonhosted.org/packages/84/29/65b55622bde135aedf4565dc509d99b560ee4095e56989e815f8fd2aa910/cryptography-46.0.5-cp311-abi3-manylinux_2_34_aarch64.whl", hash = "sha256:e9251e3be159d1020c4030bd2e5f84d6a43fe54b6c19c12f51cde9542a2817b2", size = 4277038, upload-time = "2026-02-10T19:17:20.256Z" },
    { url = "https://files.pythonhosted.org/packages/bc/36/45e76c68d7311432741faf1fbf7fac8a196a0a735ca21f504c75d37e2558/cryptography-46.0.5-cp311-abi3-manylinux_2_34_ppc64le.whl", hash = "sha256:47fb8a66058b80e509c47118ef8a75d14c455e81ac369050f20ba0d23e77fee0", size = 4912181, upload-time = "2026-02-10T19:17:21.825Z" },
    { url = "https://files.pythonhosted.org/packages/6d/1a/c1ba8fead184d6e3d5afcf03d569acac5ad063f3ac9fb7258af158f7e378/cryptography-46.0.5-cp311-abi3-manylinux_2_34_x86_64.whl", hash = "sha256:4c3341037c136030cb46e4b1e17b7418ea4cbd9dd207e4a6f3b2b24e0d4ac731", size = 4456482, upload-time = "2026-02-10T19:17:25.133Z" },
    { url = "https://files.pythonhosted.org/packages/f9/e5/3fb22e37f66827ced3b902cf895e6a6bc1d095b5b26be26bd13c441fdf19/cryptography-46.0.5-cp311-abi3-musllinux_1_2_aarch64.whl", hash = "sha256:890bcb4abd5a2d3f852196437129eb3667d62630333aacc13dfd470fad3aaa82", size = 4405497, upload-time = "2026-02-10T19:17:26.66Z" },
    { url = "https://files.pythonhosted.org/packages/1a/df/9d58bb32b1121a8a2f27383fabae4d63080c7ca60b9b5c88be742be04ee7/cryptography-46.0.5-cp311-abi3-musllinux_1_2_x86_64.whl", hash = "sha256:80a8d7bfdf38f87ca30a5391c0c9ce4ed2926918e017c29ddf643d0ed2778ea1", size = 4667819, upload-time = "2026-02-10T19:17:28.569Z" },
    { url = "https://files.pythonhosted.org/packages/ea/ed/325d2a490c5e94038cdb0117da9397ece1f11201f425c4e9c57fe5b9f08b/cryptography-46.0.5-cp311-abi3-win32.whl", hash = "sha256:60ee7e19e95104d4c03871d7d7dfb3d22ef8a9b9c6778c94e1c8fcc8365afd48", size = 3028230, upload-time = "2026-02-10T19:17:30.518Z" },
    { url = "https://files.pythonhosted.org/packages/e9/5a/ac0f49e48063ab4255d9e3b79f5def51697fce1a95ea1370f03dc9db76f6/cryptography-46.0.5-cp311-abi3-win_amd64.whl", hash = "sha256:38946c54b16c885c72c4f59846be9743d699eee2b69b6988e0a00a01f46a61a4", size = 3480909, upload-time = "2026-02-10T19:17:32.083Z" },
    { url = "https://files.pythonhosted.org/packages/00/13/3d278bfa7a15a96b9dc22db5a12ad1e48a9eb3d40e1827ef66a5df75d0d0/cryptography-46.0.5-cp314-cp314t-macosx_10_9_universal2.whl", hash = "sha256:94a76daa32eb78d61339aff7952ea819b1734b46f73646a07decb40e5b3448e2", size = 7119287, upload-time = "2026-02-10T19:17:33.801Z" },
    { url = "https://files.pythonhosted.org/packages/67/c8/581a6702e14f0898a0848105cbefd20c058099e2c2d22ef4e476dfec75d7/cryptography-46.0.5-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:5be7bf2fb40769e05739dd0046e7b26f9d4670badc7b032d6ce4db64dddc0678", size = 4265728, upload-time = "2026-02-10T19:17:35.569Z" },
    { url = "https://files.pythonhosted.org/packages/dd/4a/ba1a65ce8fc65435e5a849558379896c957870dd64fecea97b1ad5f46a37/cryptography-46.0.5-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:fe346b143ff9685e40192a4960938545c699054ba11d4f9029f94751e3f71d87", size = 4408287, upload-time = "2026-02-10T19:17:36.938Z" },
    { url = "https://files.pythonhosted.org/packages/f8/67/8ffdbf7b65ed1ac224d1c2df3943553766914a8ca718747ee3871da6107e/cryptography-46.0.5-cp314-cp314t-manylinux_2_28_aarch64.whl", hash = "sha256:c69fd885df7d089548a42d5ec05be26050ebcd2283d89b3d30676eb32ff87dee", size = 4270291, upload-time = "2026-02-10T19:17:38.748Z" },
    { url = "https://files.pythonhosted.org/packages/f8/e5/f52377ee93bc2f2bba55a41a886fd208c15276ffbd2569f2ddc89d50e2c5/cryptography-46.0.5-cp314-cp314t-manylinux_2_28_ppc64le.whl", hash = "sha256:8293f3dea7fc929ef7240796ba231413afa7b68ce38fd21da2995549f5961981", size = 4927539, upload-time = "2026-02-10T19:17:40.241Z" },
    { url = "https://files.pythonhosted.org/packages/3b/02/cfe39181b02419bbbbcf3abdd16c1c5c8541f03ca8bda240debc467d5a12/cryptography-46.0.5-cp314-cp314t-manylinux_2_28_x86_64.whl", hash = "sha256:1abfdb89b41c3be0365328a410baa9df3ff8a9110fb75e7b52e66803ddabc9a9", size = 4442199, upload-time = "2026-02-10T19:17:41.789Z" },
    { url = "https://files.pythonhosted.org/packages/c0/96/2fcaeb4873e536cf71421a388a6c11b5bc846e986b2b069c79363dc1648e/cryptography-46.0.5-cp314-cp314t-manylinux_2_31_armv7l.whl", hash = "sha256:d66e421495fdb797610a08f43b05269e0a5ea7f5e652a89bfd5a7d3c1dee3648", size = 3960131, upload-time = "2026-02-10T19:17:43.379Z" },
    { url = "https://files.pythonhosted.org/packages/d8/d2/b27631f401ddd644e94c5cf33c9a4069f72011821cf3dc7309546b0642a0/cryptography-46.0.5-cp314-cp314t-manylinux_2_34_aarch64.whl", hash = "sha256:4e817a8920bfbcff8940ecfd60f23d01836408242b30f1a708d93198393a80b4", size = 4270072, upload-time = "2026-02-10T19:17:45.481Z" },
    { url = "https://files.pythonhosted.org/packages/f4/a7/60d32b0370dae0b4ebe55ffa10e8599a2a59935b5ece1b9f06edb73abdeb/cryptography-46.0.5-cp314-cp314t-manylinux_2_34_ppc64le.whl", hash = "sha256:68f68d13f2e1cb95163fa3b4db4bf9a159a418f5f6e7242564fc75fcae667fd0", size = 4892170, upload-time = "2026-02-10T19:17:46.997Z" },
    { url = "https://files.pythonhosted.org/packages/d2/b9/cf73ddf8ef1164330eb0b199a589103c363afa0cf794218c24d524a58eab/cryptography-46.0.5-cp314-cp314t-manylinux_2_34_x86_64.whl", hash = "sha256:a3d1fae9863299076f05cb8a778c467578262fae09f9dc0ee9b12eb4268ce663", size = 4441741, upload-time = "2026-02-10T19:17:48.661Z" },
    { url = "https://files.pythonhosted.org/packages/5f/eb/eee00b28c84c726fe8fa0158c65afe312d9c3b78d9d01daf700f1f6e37ff/cryptography-46.0.5-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:c4143987a42a2397f2fc3b4d7e3a7d313fbe684f67ff443999e803dd75a76826", size = 4396728, upload-time = "2026-02-10T19:17:50.058Z" },
    { url = "https://files.pythonhosted.org/packages/65/f4/6bc1a9ed5aef7145045114b75b77c2a8261b4d38717bd8dea111a63c3442/cryptography-46.0.5-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:7d731d4b107030987fd61a7f8ab512b25b53cef8f233a97379ede116f30eb67d", size = 4652001, upload-time = "2026-02-10T19:17:51.54Z" },
    { url = "https://files.pythonhosted.org/packages/86/ef/5d00ef966ddd71ac2e6951d278884a84a40ffbd88948ef0e294b214ae9e4/cryptography-46.0.5-cp314-cp314t-win32.whl", hash = "sha256:c3bcce8521d785d510b2aad26ae2c966092b7daa8f45dd8f44734a104dc0bc1a", size = 3003637, upload-time = "2026-02-10T19:17:52.997Z" },
    { url = "https://files.pythonhosted.org/packages/b7/57/f3f4160123da6d098db78350fdfd9705057aad21de7388eacb2401dceab9/cryptography-46.0.5-cp314-cp314t-win_amd64.whl", hash = "sha256:4d8ae8659ab18c65ced284993c2265910f6c9e650189d4e3f68445ef82a810e4", size = 3469487, upload-time = "2026-02-10T19:17:54.549Z" },
    { url = "https://files.pythonhosted.org/packages/e2/fa/a66aa722105ad6a458bebd64086ca2b72cdd361fed31763d20390f6f1389/cryptography-46.0.5-cp38-abi3-macosx_10_9_universal2.whl", hash = "sha256:4108d4c09fbbf2789d0c926eb4152ae1760d5a2d97612b92d508d96c861e4d31", size = 7170514, upload-time = "2026-02-10T19:17:56.267Z" },
    { url = "https://files.pythonhosted.org/packages/0f/04/c85bdeab78c8bc77b701bf0d9bdcf514c044e18a46dcff330df5448631b0/cryptography-46.0.5-cp38-abi3-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:7d1f30a86d2757199cb2d56e48cce14deddf1f9c95f1ef1b64ee91ea43fe2e18", size = 4275349, upload-time = "2026-02-10T19:17:58.419Z" },
    { url = "https://files.pythonhosted.org/packages/5c/32/9b87132a2f91ee7f5223b091dc963055503e9b442c98fc0b8a5ca765fab0/cryptography-46.0.5-cp38-abi3-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:039917b0dc418bb9f6edce8a906572d69e74bd330b0b3fea4f79dab7f8ddd235", size = 4420667, upload-time = "2026-02-10T19:18:00.619Z" },
    { url = "https://files.pythonhosted.org/packages/a1/a6/a7cb7010bec4b7c5692ca6f024150371b295ee1c108bdc1c400e4c44562b/cryptography-46.0.5-cp38-abi3-manylinux_2_28_aarch64.whl", hash = "sha256:ba2a27ff02f48193fc4daeadf8ad2590516fa3d0adeeb34336b96f7fa64c1e3a", size = 4276980, upload-time = "2026-02-10T19:18:02.379Z" },
    { url = "https://files.pythonhosted.org/packages/8e/7c/c4f45e0eeff9b91e3f12dbd0e165fcf2a38847288fcfd889deea99fb7b6d/cryptography-46.0.5-cp38-abi3-manylinux_2_28_ppc64le.whl", hash = "sha256:61aa400dce22cb001a98014f647dc21cda08f7915ceb95df0c9eaf84b4b6af76", size = 4939143, upload-time = "2026-02-10T19:18:03.964Z" },
    { url = "https://files.pythonhosted.org/packages/37/19/e1b8f964a834eddb44fa1b9a9976f4e414cbb7aa62809b6760c8803d22d1/cryptography-46.0.5-cp38-abi3-manylinux_2_28_x86_64.whl", hash = "sha256:3ce58ba46e1bc2aac4f7d9290223cead56743fa6ab94a5d53292ffaac6a91614", size = 4453674, upload-time = "2026-02-10T19:18:05.588Z" },
    { url = "https://files.pythonhosted.org/packages/db/ed/db15d3956f65264ca204625597c410d420e26530c4e2943e05a0d2f24d51/cryptography-46.0.5-cp38-abi3-manylinux_2_31_armv7l.whl", hash = "sha256:420d0e909050490d04359e7fdb5ed7e667ca5c3c402b809ae2563d7e66a92229", size = 3978801, upload-time = "2026-02-10T19:18:07.167Z" },
    { url = "https://files.pythonhosted.org/packages/41/e2/df40a31d82df0a70a0daf69791f91dbb70e47644c58581d654879b382d11/cryptography-46.0.5-cp38-abi3-manylinux_2_34_aarch64.whl", hash = "sha256:582f5fcd2afa31622f317f80426a027f30dc792e9c80ffee87b993200ea115f1", size = 4276755, upload-time = "2026-02-10T19:18:09.813Z" },
    { url = "https://files.pythonhosted.org/packages/33/45/726809d1176959f4a896b86907b98ff4391a8aa29c0aaaf9450a8a10630e/cryptography-46.0.5-cp38-abi3-manylinux_2_34_ppc64le.whl", hash = "sha256:bfd56bb4b37ed4f330b82402f6f435845a5f5648edf1ad497da51a8452d5d62d", size = 4901539, upload-time = "2026-02-10T19:18:11.263Z" },
    { url = "https://files.pythonhosted.org/packages/99/0f/a3076874e9c88ecb2ecc31382f6e7c21b428ede6f55aafa1aa272613e3cd/cryptography-46.0.5-cp38-abi3-manylinux_2_34_x86_64.whl", hash = "sha256:a3d507bb6a513ca96ba84443226af944b0f7f47dcc9a399d110cd6146481d24c", size = 4452794, upload-time = "2026-02-10T19:18:12.914Z" },
    { url = "https://files.pythonhosted.org/packages/02/ef/ffeb542d3683d24194a38f66ca17c0a4b8bf10631feef44a7ef64e631b1a/cryptography-46.0.5-cp38-abi3-musllinux_1_2_aarch64.whl", hash = "sha256:9f16fbdf4da055efb21c22d81b89f155f02ba420558db21288b3d0035bafd5f4", size = 4404160, upload-time = "2026-02-10T19:18:14.375Z" },
    { url = "https://files.pythonhosted.org/packages/96/93/682d2b43c1d5f1406ed048f377c0fc9fc8f7b0447a478d5c65ab3d3a66eb/cryptography-46.0.5-cp38-abi3-musllinux_1_2_x86_64.whl", hash = "sha256:ced80795227d70549a411a4ab66e8ce307899fad2220ce5ab2f296e687eacde9", size = 4667123, upload-time = "2026-02-10T19:18:15.886Z" },
    { url = "https://files.pythonhosted.org/packages/45/2d/9c5f2926cb5300a8eefc3f4f0b3f3df39db7f7ce40c8365444c49363cbda/cryptography-46.0.5-cp38-abi3-win32.whl", hash = "sha256:02f547fce831f5096c9a567fd41bc12ca8f11df260959ecc7c3202555cc47a72", size = 3010220, upload-time = "2026-02-10T19:18:17.361Z" },
    { url = "https://files.pythonhosted.org/packages/48/ef/0c2f4a8e31018a986949d34a01115dd057bf536905dca38897bacd21fac3/cryptography-46.0.5-cp38-abi3-win_amd64.whl", hash = "sha256:556e106ee01aa13484ce9b0239bca667be5004efb0aabbed28d353df86445595", size = 3467050, upload-time = "2026-02-10T19:18:18.899Z" },
]

[[package]]
name = "distro"
version = "1.9.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/fc/f8/98eea607f65de6527f8a2e8885fc8015d3e6f5775df186e443e0964a11c3/distro-1.9.0.tar.gz", hash = "sha256:2fa77c6fd8940f116ee1d6b94a2f90b13b5ea8d019b98bc8bafdcabcdd9bdbed", size = 60722, upload-time = "2023-12-24T09:54:32.31Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/12/b3/231ffd4ab1fc9d679809f356cebee130ac7daa00d6d6f3206dd4fd137e9e/distro-1.9.0-py3-none-any.whl", hash = "sha256:7bffd925d65168f85027d8da9af6bddab658135b840670a223589bc0c8ef02b2", size = 20277, upload-time = "2023-12-24T09:54:30.421Z" },
]

[[package]]
name = "docstring-parser"
version = "0.17.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/b2/9d/c3b43da9515bd270df0f80548d9944e389870713cc1fe2b8fb35fe2bcefd/docstring_parser-0.17.0.tar.gz", hash = "sha256:583de4a309722b3315439bb31d64ba3eebada841f2e2cee23b99df001434c912", size = 27442, upload-time = "2025-07-21T07:35:01.868Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/55/e2/2537ebcff11c1ee1ff17d8d0b6f4db75873e3b0fb32c2d4a2ee31ecb310a/docstring_parser-0.17.0-py3-none-any.whl", hash = "sha256:cf2569abd23dce8099b300f9b4fa8191e9582dda731fd533daf54c4551658708", size = 36896, upload-time = "2025-07-21T07:35:00.684Z" },
]

[[package]]
name = "griffe"
version = "1.15.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "colorama" },
]
sdist = { url = "https://files.pythonhosted.org/packages/0d/0c/3a471b6e31951dce2360477420d0a8d1e00dea6cf33b70f3e8c3ab6e28e1/griffe-1.15.0.tar.gz", hash = "sha256:7726e3afd6f298fbc3696e67958803e7ac843c1cfe59734b6251a40cdbfb5eea", size = 424112, upload-time = "2025-11-10T15:03:15.52Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/9c/83/3b1d03d36f224edded98e9affd0467630fc09d766c0e56fb1498cbb04a9b/griffe-1.15.0-py3-none-any.whl", hash = "sha256:6f6762661949411031f5fcda9593f586e6ce8340f0ba88921a0f2ef7a81eb9a3", size = 150705, upload-time = "2025-11-10T15:03:13.549Z" },
]

[[package]]
name = "h11"
version = "0.16.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/01/ee/02a2c011bdab74c6fb3c75474d40b3052059d95df7e73351460c8588d963/h11-0.16.0.tar.gz", hash = "sha256:4e35b956cf45792e4caa5885e69fba00bdbc6ffafbfa020300e549b208ee5ff1", size = 101250, upload-time = "2025-04-24T03:35:25.427Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/04/4b/29cac41a4d98d144bf5f6d33995617b185d14b22401f75ca86f384e87ff1/h11-0.16.0-py3-none-any.whl", hash = "sha256:63cf8bbe7522de3bf65932fda1d9c2772064ffb3dae62d55932da54b31cb6c86", size = 37515, upload-time = "2025-04-24T03:35:24.344Z" },
]

[[package]]
name = "httpcore"
version = "1.0.9"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "certifi" },
    { name = "h11" },
]
sdist = { url = "https://files.pythonhosted.org/packages/06/94/82699a10bca87a5556c9c59b5963f2d039dbd239f25bc2a63907a05a14cb/httpcore-1.0.9.tar.gz", hash = "sha256:6e34463af53fd2ab5d807f399a9b45ea31c3dfa2276f15a2c3f00afff6e176e8", size = 85484, upload-time = "2025-04-24T22:06:22.219Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/7e/f5/f66802a942d491edb555dd61e3a9961140fd64c90bce1eafd741609d334d/httpcore-1.0.9-py3-none-any.whl", hash = "sha256:2d400746a40668fc9dec9810239072b40b4484b640a8c38fd654a024c7a1bf55", size = 78784, upload-time = "2025-04-24T22:06:20.566Z" },
]

[[package]]
name = "httpx"
version = "0.28.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "anyio" },
    { name = "certifi" },
    { name = "httpcore" },
    { name = "idna" },
]
sdist = { url = "https://files.pythonhosted.org/packages/b1/df/48c586a5fe32a0f01324ee087459e112ebb7224f646c0b5023f5e79e9956/httpx-0.28.1.tar.gz", hash = "sha256:75e98c5f16b0f35b567856f597f06ff2270a374470a5c2392242528e3e3e42fc", size = 141406, upload-time = "2024-12-06T15:37:23.222Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/2a/39/e50c7c3a983047577ee07d2a9e53faf5a69493943ec3f6a384bdc792deb2/httpx-0.28.1-py3-none-any.whl", hash = "sha256:d909fcccc110f8c7faf814ca82a9a4d816bc5a6dbfea25d6591d6985b8ba59ad", size = 73517, upload-time = "2024-12-06T15:37:21.509Z" },
]

[[package]]
name = "httpx-sse"
version = "0.4.3"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/0f/4c/751061ffa58615a32c31b2d82e8482be8dd4a89154f003147acee90f2be9/httpx_sse-0.4.3.tar.gz", hash = "sha256:9b1ed0127459a66014aec3c56bebd93da3c1bc8bb6618c8082039a44889a755d", size = 15943, upload-time = "2025-10-10T21:48:22.271Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/d2/fd/6668e5aec43ab844de6fc74927e155a3b37bf40d7c3790e49fc0406b6578/httpx_sse-0.4.3-py3-none-any.whl", hash = "sha256:0ac1c9fe3c0afad2e0ebb25a934a59f4c7823b60792691f779fad2c5568830fc", size = 8960, upload-time = "2025-10-10T21:48:21.158Z" },
]

[[package]]
name = "idna"
version = "3.11"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/6f/6d/0703ccc57f3a7233505399edb88de3cbd678da106337b9fcde432b65ed60/idna-3.11.tar.gz", hash = "sha256:795dafcc9c04ed0c1fb032c2aa73654d8e8c5023a7df64a53f39190ada629902", size = 194582, upload-time = "2025-10-12T14:55:20.501Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/0e/61/66938bbb5fc52dbdf84594873d5b51fb1f7c7794e9c0f5bd885f30bc507b/idna-3.11-py3-none-any.whl", hash = "sha256:771a87f49d9defaf64091e6e6fe9c18d4833f140bd19464795bc32d966ca37ea", size = 71008, upload-time = "2025-10-12T14:55:18.883Z" },
]

[[package]]
name = "jiter"
version = "0.13.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/0d/5e/4ec91646aee381d01cdb9974e30882c9cd3b8c5d1079d6b5ff4af522439a/jiter-0.13.0.tar.gz", hash = "sha256:f2839f9c2c7e2dffc1bc5929a510e14ce0a946be9365fd1219e7ef342dae14f4", size = 164847, upload-time = "2026-02-02T12:37:56.441Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/91/9c/7ee5a6ff4b9991e1a45263bfc46731634c4a2bde27dfda6c8251df2d958c/jiter-0.13.0-cp313-cp313-macosx_10_12_x86_64.whl", hash = "sha256:1f8a55b848cbabf97d861495cd65f1e5c590246fabca8b48e1747c4dfc8f85bf", size = 306897, upload-time = "2026-02-02T12:36:16.748Z" },
    { url = "https://files.pythonhosted.org/packages/7c/02/be5b870d1d2be5dd6a91bdfb90f248fbb7dcbd21338f092c6b89817c3dbf/jiter-0.13.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:f556aa591c00f2c45eb1b89f68f52441a016034d18b65da60e2d2875bbbf344a", size = 317507, upload-time = "2026-02-02T12:36:18.351Z" },
    { url = "https://files.pythonhosted.org/packages/da/92/b25d2ec333615f5f284f3a4024f7ce68cfa0604c322c6808b2344c7f5d2b/jiter-0.13.0-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:f7e1d61da332ec412350463891923f960c3073cf1aae93b538f0bb4c8cd46efb", size = 350560, upload-time = "2026-02-02T12:36:19.746Z" },
    { url = "https://files.pythonhosted.org/packages/be/ec/74dcb99fef0aca9fbe56b303bf79f6bd839010cb18ad41000bf6cc71eec0/jiter-0.13.0-cp313-cp313-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:3097d665a27bc96fd9bbf7f86178037db139f319f785e4757ce7ccbf390db6c2", size = 363232, upload-time = "2026-02-02T12:36:21.243Z" },
    { url = "https://files.pythonhosted.org/packages/1b/37/f17375e0bb2f6a812d4dd92d7616e41917f740f3e71343627da9db2824ce/jiter-0.13.0-cp313-cp313-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:9d01ecc3a8cbdb6f25a37bd500510550b64ddf9f7d64a107d92f3ccb25035d0f", size = 483727, upload-time = "2026-02-02T12:36:22.688Z" },
    { url = "https://files.pythonhosted.org/packages/77/d2/a71160a5ae1a1e66c1395b37ef77da67513b0adba73b993a27fbe47eb048/jiter-0.13.0-cp313-cp313-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:ed9bbc30f5d60a3bdf63ae76beb3f9db280d7f195dfcfa61af792d6ce912d159", size = 370799, upload-time = "2026-02-02T12:36:24.106Z" },
    { url = "https://files.pythonhosted.org/packages/01/99/ed5e478ff0eb4e8aa5fd998f9d69603c9fd3f32de3bd16c2b1194f68361c/jiter-0.13.0-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:98fbafb6e88256f4454de33c1f40203d09fc33ed19162a68b3b257b29ca7f663", size = 359120, upload-time = "2026-02-02T12:36:25.519Z" },
    { url = "https://files.pythonhosted.org/packages/16/be/7ffd08203277a813f732ba897352797fa9493faf8dc7995b31f3d9cb9488/jiter-0.13.0-cp313-cp313-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:5467696f6b827f1116556cb0db620440380434591e93ecee7fd14d1a491b6daa", size = 390664, upload-time = "2026-02-02T12:36:26.866Z" },
    { url = "https://files.pythonhosted.org/packages/d1/84/e0787856196d6d346264d6dcccb01f741e5f0bd014c1d9a2ebe149caf4f3/jiter-0.13.0-cp313-cp313-musllinux_1_1_aarch64.whl", hash = "sha256:2d08c9475d48b92892583df9da592a0e2ac49bcd41fae1fec4f39ba6cf107820", size = 513543, upload-time = "2026-02-02T12:36:28.217Z" },
    { url = "https://files.pythonhosted.org/packages/65/50/ecbd258181c4313cf79bca6c88fb63207d04d5bf5e4f65174114d072aa55/jiter-0.13.0-cp313-cp313-musllinux_1_1_x86_64.whl", hash = "sha256:aed40e099404721d7fcaf5b89bd3b4568a4666358bcac7b6b15c09fb6252ab68", size = 547262, upload-time = "2026-02-02T12:36:29.678Z" },
    { url = "https://files.pythonhosted.org/packages/27/da/68f38d12e7111d2016cd198161b36e1f042bd115c169255bcb7ec823a3bf/jiter-0.13.0-cp313-cp313-win32.whl", hash = "sha256:36ebfbcffafb146d0e6ffb3e74d51e03d9c35ce7c625c8066cdbfc7b953bdc72", size = 200630, upload-time = "2026-02-02T12:36:31.808Z" },
    { url = "https://files.pythonhosted.org/packages/25/65/3bd1a972c9a08ecd22eb3b08a95d1941ebe6938aea620c246cf426ae09c2/jiter-0.13.0-cp313-cp313-win_amd64.whl", hash = "sha256:8d76029f077379374cf0dbc78dbe45b38dec4a2eb78b08b5194ce836b2517afc", size = 202602, upload-time = "2026-02-02T12:36:33.679Z" },
    { url = "https://files.pythonhosted.org/packages/15/fe/13bd3678a311aa67686bb303654792c48206a112068f8b0b21426eb6851e/jiter-0.13.0-cp313-cp313-win_arm64.whl", hash = "sha256:bb7613e1a427cfcb6ea4544f9ac566b93d5bf67e0d48c787eca673ff9c9dff2b", size = 185939, upload-time = "2026-02-02T12:36:35.065Z" },
    { url = "https://files.pythonhosted.org/packages/49/19/a929ec002ad3228bc97ca01dbb14f7632fffdc84a95ec92ceaf4145688ae/jiter-0.13.0-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:fa476ab5dd49f3bf3a168e05f89358c75a17608dbabb080ef65f96b27c19ab10", size = 316616, upload-time = "2026-02-02T12:36:36.579Z" },
    { url = "https://files.pythonhosted.org/packages/52/56/d19a9a194afa37c1728831e5fb81b7722c3de18a3109e8f282bfc23e587a/jiter-0.13.0-cp313-cp313t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:ade8cb6ff5632a62b7dbd4757d8c5573f7a2e9ae285d6b5b841707d8363205ef", size = 346850, upload-time = "2026-02-02T12:36:38.058Z" },
    { url = "https://files.pythonhosted.org/packages/36/4a/94e831c6bf287754a8a019cb966ed39ff8be6ab78cadecf08df3bb02d505/jiter-0.13.0-cp313-cp313t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:9950290340acc1adaded363edd94baebcee7dabdfa8bee4790794cd5cfad2af6", size = 358551, upload-time = "2026-02-02T12:36:39.417Z" },
    { url = "https://files.pythonhosted.org/packages/a2/ec/a4c72c822695fa80e55d2b4142b73f0012035d9fcf90eccc56bc060db37c/jiter-0.13.0-cp313-cp313t-win_amd64.whl", hash = "sha256:2b4972c6df33731aac0742b64fd0d18e0a69bc7d6e03108ce7d40c85fd9e3e6d", size = 201950, upload-time = "2026-02-02T12:36:40.791Z" },
    { url = "https://files.pythonhosted.org/packages/b6/00/393553ec27b824fbc29047e9c7cd4a3951d7fbe4a76743f17e44034fa4e4/jiter-0.13.0-cp313-cp313t-win_arm64.whl", hash = "sha256:701a1e77d1e593c1b435315ff625fd071f0998c5f02792038a5ca98899261b7d", size = 185852, upload-time = "2026-02-02T12:36:42.077Z" },
    { url = "https://files.pythonhosted.org/packages/6e/f5/f1997e987211f6f9bd71b8083047b316208b4aca0b529bb5f8c96c89ef3e/jiter-0.13.0-cp314-cp314-macosx_10_12_x86_64.whl", hash = "sha256:cc5223ab19fe25e2f0bf2643204ad7318896fe3729bf12fde41b77bfc4fafff0", size = 308804, upload-time = "2026-02-02T12:36:43.496Z" },
    { url = "https://files.pythonhosted.org/packages/cd/8f/5482a7677731fd44881f0204981ce2d7175db271f82cba2085dd2212e095/jiter-0.13.0-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:9776ebe51713acf438fd9b4405fcd86893ae5d03487546dae7f34993217f8a91", size = 318787, upload-time = "2026-02-02T12:36:45.071Z" },
    { url = "https://files.pythonhosted.org/packages/f3/b9/7257ac59778f1cd025b26a23c5520a36a424f7f1b068f2442a5b499b7464/jiter-0.13.0-cp314-cp314-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:879e768938e7b49b5e90b7e3fecc0dbec01b8cb89595861fb39a8967c5220d09", size = 353880, upload-time = "2026-02-02T12:36:47.365Z" },
    { url = "https://files.pythonhosted.org/packages/c3/87/719eec4a3f0841dad99e3d3604ee4cba36af4419a76f3cb0b8e2e691ad67/jiter-0.13.0-cp314-cp314-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:682161a67adea11e3aae9038c06c8b4a9a71023228767477d683f69903ebc607", size = 366702, upload-time = "2026-02-02T12:36:48.871Z" },
    { url = "https://files.pythonhosted.org/packages/d2/65/415f0a75cf6921e43365a1bc227c565cb949caca8b7532776e430cbaa530/jiter-0.13.0-cp314-cp314-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:a13b68cd1cd8cc9de8f244ebae18ccb3e4067ad205220ef324c39181e23bbf66", size = 486319, upload-time = "2026-02-02T12:36:53.006Z" },
    { url = "https://files.pythonhosted.org/packages/54/a2/9e12b48e82c6bbc6081fd81abf915e1443add1b13d8fc586e1d90bb02bb8/jiter-0.13.0-cp314-cp314-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:87ce0f14c6c08892b610686ae8be350bf368467b6acd5085a5b65441e2bf36d2", size = 372289, upload-time = "2026-02-02T12:36:54.593Z" },
    { url = "https://files.pythonhosted.org/packages/4e/c1/e4693f107a1789a239c759a432e9afc592366f04e901470c2af89cfd28e1/jiter-0.13.0-cp314-cp314-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:0c365005b05505a90d1c47856420980d0237adf82f70c4aff7aebd3c1cc143ad", size = 360165, upload-time = "2026-02-02T12:36:56.112Z" },
    { url = "https://files.pythonhosted.org/packages/17/08/91b9ea976c1c758240614bd88442681a87672eebc3d9a6dde476874e706b/jiter-0.13.0-cp314-cp314-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:1317fdffd16f5873e46ce27d0e0f7f4f90f0cdf1d86bf6abeaea9f63ca2c401d", size = 389634, upload-time = "2026-02-02T12:36:57.495Z" },
    { url = "https://files.pythonhosted.org/packages/18/23/58325ef99390d6d40427ed6005bf1ad54f2577866594bcf13ce55675f87d/jiter-0.13.0-cp314-cp314-musllinux_1_1_aarch64.whl", hash = "sha256:c05b450d37ba0c9e21c77fef1f205f56bcee2330bddca68d344baebfc55ae0df", size = 514933, upload-time = "2026-02-02T12:36:58.909Z" },
    { url = "https://files.pythonhosted.org/packages/5b/25/69f1120c7c395fd276c3996bb8adefa9c6b84c12bb7111e5c6ccdcd8526d/jiter-0.13.0-cp314-cp314-musllinux_1_1_x86_64.whl", hash = "sha256:775e10de3849d0631a97c603f996f518159272db00fdda0a780f81752255ee9d", size = 548842, upload-time = "2026-02-02T12:37:00.433Z" },
    { url = "https://files.pythonhosted.org/packages/18/05/981c9669d86850c5fbb0d9e62bba144787f9fba84546ba43d624ee27ef29/jiter-0.13.0-cp314-cp314-win32.whl", hash = "sha256:632bf7c1d28421c00dd8bbb8a3bac5663e1f57d5cd5ed962bce3c73bf62608e6", size = 202108, upload-time = "2026-02-02T12:37:01.718Z" },
    { url = "https://files.pythonhosted.org/packages/8d/96/cdcf54dd0b0341db7d25413229888a346c7130bd20820530905fdb65727b/jiter-0.13.0-cp314-cp314-win_amd64.whl", hash = "sha256:f22ef501c3f87ede88f23f9b11e608581c14f04db59b6a801f354397ae13739f", size = 204027, upload-time = "2026-02-02T12:37:03.075Z" },
    { url = "https://files.pythonhosted.org/packages/fb/f9/724bcaaab7a3cd727031fe4f6995cb86c4bd344909177c186699c8dec51a/jiter-0.13.0-cp314-cp314-win_arm64.whl", hash = "sha256:07b75fe09a4ee8e0c606200622e571e44943f47254f95e2436c8bdcaceb36d7d", size = 187199, upload-time = "2026-02-02T12:37:04.414Z" },
    { url = "https://files.pythonhosted.org/packages/62/92/1661d8b9fd6a3d7a2d89831db26fe3c1509a287d83ad7838831c7b7a5c7e/jiter-0.13.0-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:964538479359059a35fb400e769295d4b315ae61e4105396d355a12f7fef09f0", size = 318423, upload-time = "2026-02-02T12:37:05.806Z" },
    { url = "https://files.pythonhosted.org/packages/4f/3b/f77d342a54d4ebcd128e520fc58ec2f5b30a423b0fd26acdfc0c6fef8e26/jiter-0.13.0-cp314-cp314t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:e104da1db1c0991b3eaed391ccd650ae8d947eab1480c733e5a3fb28d4313e40", size = 351438, upload-time = "2026-02-02T12:37:07.189Z" },
    { url = "https://files.pythonhosted.org/packages/76/b3/ba9a69f0e4209bd3331470c723c2f5509e6f0482e416b612431a5061ed71/jiter-0.13.0-cp314-cp314t-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:0e3a5f0cde8ff433b8e88e41aa40131455420fb3649a3c7abdda6145f8cb7202", size = 364774, upload-time = "2026-02-02T12:37:08.579Z" },
    { url = "https://files.pythonhosted.org/packages/b3/16/6cdb31fa342932602458dbb631bfbd47f601e03d2e4950740e0b2100b570/jiter-0.13.0-cp314-cp314t-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:57aab48f40be1db920a582b30b116fe2435d184f77f0e4226f546794cedd9cf0", size = 487238, upload-time = "2026-02-02T12:37:10.066Z" },
    { url = "https://files.pythonhosted.org/packages/ed/b1/956cc7abaca8d95c13aa8d6c9b3f3797241c246cd6e792934cc4c8b250d2/jiter-0.13.0-cp314-cp314t-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:7772115877c53f62beeb8fd853cab692dbc04374ef623b30f997959a4c0e7e95", size = 372892, upload-time = "2026-02-02T12:37:11.656Z" },
    { url = "https://files.pythonhosted.org/packages/26/c4/97ecde8b1e74f67b8598c57c6fccf6df86ea7861ed29da84629cdbba76c4/jiter-0.13.0-cp314-cp314t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:1211427574b17b633cfceba5040de8081e5abf114f7a7602f73d2e16f9fdaa59", size = 360309, upload-time = "2026-02-02T12:37:13.244Z" },
    { url = "https://files.pythonhosted.org/packages/4b/d7/eabe3cf46715854ccc80be2cd78dd4c36aedeb30751dbf85a1d08c14373c/jiter-0.13.0-cp314-cp314t-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:7beae3a3d3b5212d3a55d2961db3c292e02e302feb43fce6a3f7a31b90ea6dfe", size = 389607, upload-time = "2026-02-02T12:37:14.881Z" },
    { url = "https://files.pythonhosted.org/packages/df/2d/03963fc0804e6109b82decfb9974eb92df3797fe7222428cae12f8ccaa0c/jiter-0.13.0-cp314-cp314t-musllinux_1_1_aarch64.whl", hash = "sha256:e5562a0f0e90a6223b704163ea28e831bd3a9faa3512a711f031611e6b06c939", size = 514986, upload-time = "2026-02-02T12:37:16.326Z" },
    { url = "https://files.pythonhosted.org/packages/f6/6c/8c83b45eb3eb1c1e18d841fe30b4b5bc5619d781267ca9bc03e005d8fd0a/jiter-0.13.0-cp314-cp314t-musllinux_1_1_x86_64.whl", hash = "sha256:6c26a424569a59140fb51160a56df13f438a2b0967365e987889186d5fc2f6f9", size = 548756, upload-time = "2026-02-02T12:37:17.736Z" },
    { url = "https://files.pythonhosted.org/packages/47/66/eea81dfff765ed66c68fd2ed8c96245109e13c896c2a5015c7839c92367e/jiter-0.13.0-cp314-cp314t-win32.whl", hash = "sha256:24dc96eca9f84da4131cdf87a95e6ce36765c3b156fc9ae33280873b1c32d5f6", size = 201196, upload-time = "2026-02-02T12:37:19.101Z" },
    { url = "https://files.pythonhosted.org/packages/ff/32/4ac9c7a76402f8f00d00842a7f6b83b284d0cf7c1e9d4227bc95aa6d17fa/jiter-0.13.0-cp314-cp314t-win_amd64.whl", hash = "sha256:0a8d76c7524087272c8ae913f5d9d608bd839154b62c4322ef65723d2e5bb0b8", size = 204215, upload-time = "2026-02-02T12:37:20.495Z" },
    { url = "https://files.pythonhosted.org/packages/f9/8e/7def204fea9f9be8b3c21a6f2dd6c020cf56c7d5ff753e0e23ed7f9ea57e/jiter-0.13.0-cp314-cp314t-win_arm64.whl", hash = "sha256:2c26cf47e2cad140fa23b6d58d435a7c0161f5c514284802f25e87fddfe11024", size = 187152, upload-time = "2026-02-02T12:37:22.124Z" },
]

[[package]]
name = "jsonschema"
version = "4.26.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "attrs" },
    { name = "jsonschema-specifications" },
    { name = "referencing" },
    { name = "rpds-py" },
]
sdist = { url = "https://files.pythonhosted.org/packages/b3/fc/e067678238fa451312d4c62bf6e6cf5ec56375422aee02f9cb5f909b3047/jsonschema-4.26.0.tar.gz", hash = "sha256:0c26707e2efad8aa1bfc5b7ce170f3fccc2e4918ff85989ba9ffa9facb2be326", size = 366583, upload-time = "2026-01-07T13:41:07.246Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/69/90/f63fb5873511e014207a475e2bb4e8b2e570d655b00ac19a9a0ca0a385ee/jsonschema-4.26.0-py3-none-any.whl", hash = "sha256:d489f15263b8d200f8387e64b4c3a75f06629559fb73deb8fdfb525f2dab50ce", size = 90630, upload-time = "2026-01-07T13:41:05.306Z" },
]

[[package]]
name = "jsonschema-specifications"
version = "2025.9.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "referencing" },
]
sdist = { url = "https://files.pythonhosted.org/packages/19/74/a633ee74eb36c44aa6d1095e7cc5569bebf04342ee146178e2d36600708b/jsonschema_specifications-2025.9.1.tar.gz", hash = "sha256:b540987f239e745613c7a9176f3edb72b832a4ac465cf02712288397832b5e8d", size = 32855, upload-time = "2025-09-08T01:34:59.186Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/41/45/1a4ed80516f02155c51f51e8cedb3c1902296743db0bbc66608a0db2814f/jsonschema_specifications-2025.9.1-py3-none-any.whl", hash = "sha256:98802fee3a11ee76ecaca44429fda8a41bff98b00a0f2838151b113f210cc6fe", size = 18437, upload-time = "2025-09-08T01:34:57.871Z" },
]

[[package]]
name = "mcp"
version = "1.26.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "anyio" },
    { name = "httpx" },
    { name = "httpx-sse" },
    { name = "jsonschema" },
    { name = "pydantic" },
    { name = "pydantic-settings" },
    { name = "pyjwt", extra = ["crypto"] },
    { name = "python-multipart" },
    { name = "pywin32", marker = "sys_platform == 'win32'" },
    { name = "sse-starlette" },
    { name = "starlette" },
    { name = "typing-extensions" },
    { name = "typing-inspection" },
    { name = "uvicorn", marker = "sys_platform != 'emscripten'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/fc/6d/62e76bbb8144d6ed86e202b5edd8a4cb631e7c8130f3f4893c3f90262b10/mcp-1.26.0.tar.gz", hash = "sha256:db6e2ef491eecc1a0d93711a76f28dec2e05999f93afd48795da1c1137142c66", size = 608005, upload-time = "2026-01-24T19:40:32.468Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/fd/d9/eaa1f80170d2b7c5ba23f3b59f766f3a0bb41155fbc32a69adfa1adaaef9/mcp-1.26.0-py3-none-any.whl", hash = "sha256:904a21c33c25aa98ddbeb47273033c435e595bbacfdb177f4bd87f6dceebe1ca", size = 233615, upload-time = "2026-01-24T19:40:30.652Z" },
]

[[package]]
name = "openai"
version = "2.26.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "anyio" },
    { name = "distro" },
    { name = "httpx" },
    { name = "jiter" },
    { name = "pydantic" },
    { name = "sniffio" },
    { name = "tqdm" },
    { name = "typing-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/d7/91/2a06c4e9597c338cac1e5e5a8dd6f29e1836fc229c4c523529dca387fda8/openai-2.26.0.tar.gz", hash = "sha256:b41f37c140ae0034a6e92b0c509376d907f3a66109935fba2c1b471a7c05a8fb", size = 666702, upload-time = "2026-03-05T23:17:35.874Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/c6/2e/3f73e8ca53718952222cacd0cf7eecc9db439d020f0c1fe7ae717e4e199a/openai-2.26.0-py3-none-any.whl", hash = "sha256:6151bf8f83802f036117f06cc8a57b3a4da60da9926826cc96747888b57f394f", size = 1136409, upload-time = "2026-03-05T23:17:34.072Z" },
]

[[package]]
name = "openai-agents"
version = "0.11.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "griffe" },
    { name = "mcp" },
    { name = "openai" },
    { name = "pydantic" },
    { name = "requests" },
    { name = "types-requests" },
    { name = "typing-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/08/5e/79875ab7f0f2da8247d76616001ab3a82f6b128262a5c69367530689e69c/openai_agents-0.11.1.tar.gz", hash = "sha256:b2bec1a780a2e2f2419e9688931eb65649bb5283f99e946018d4f1b67d4e95ca", size = 2582366, upload-time = "2026-03-09T06:34:07.701Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/f7/e9/d8d8a39a2e3c5fb1a538a13a6928f4223ff6664b8ba2a6137187b0f69370/openai_agents-0.11.1-py3-none-any.whl", hash = "sha256:4fda67bfe2aab4a1cd4a701d4e8d3d1eb849ba66aeea51295dbedf8a9e52cdb1", size = 434624, upload-time = "2026-03-09T06:34:05.653Z" },
]

[[package]]
name = "openai-examples"
version = "0.1.0"
source = { virtual = "." }
dependencies = [
    { name = "acontext" },
    { name = "openai" },
    { name = "openai-agents" },
    { name = "python-dotenv" },
]

[package.metadata]
requires-dist = [
    { name = "acontext", specifier = ">=0.1.18" },
    { name = "openai", specifier = ">=2.8.0" },
    { name = "openai-agents", specifier = ">=0.6.1" },
    { name = "python-dotenv", specifier = ">=1.0.0" },
]

[[package]]
name = "pycparser"
version = "3.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/1b/7d/92392ff7815c21062bea51aa7b87d45576f649f16458d78b7cf94b9ab2e6/pycparser-3.0.tar.gz", hash = "sha256:600f49d217304a5902ac3c37e1281c9fe94e4d0489de643a9504c5cdfdfc6b29", size = 103492, upload-time = "2026-01-21T14:26:51.89Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/0c/c3/44f3fbbfa403ea2a7c779186dc20772604442dde72947e7d01069cbe98e3/pycparser-3.0-py3-none-any.whl", hash = "sha256:b727414169a36b7d524c1c3e31839a521725078d7b2ff038656844266160a992", size = 48172, upload-time = "2026-01-21T14:26:50.693Z" },
]

[[package]]
name = "pydantic"
version = "2.12.5"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "annotated-types" },
    { name = "pydantic-core" },
    { name = "typing-extensions" },
    { name = "typing-inspection" },
]
sdist = { url = "https://files.pythonhosted.org/packages/69/44/36f1a6e523abc58ae5f928898e4aca2e0ea509b5aa6f6f392a5d882be928/pydantic-2.12.5.tar.gz", hash = "sha256:4d351024c75c0f085a9febbb665ce8c0c6ec5d30e903bdb6394b7ede26aebb49", size = 821591, upload-time = "2025-11-26T15:11:46.471Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/5a/87/b70ad306ebb6f9b585f114d0ac2137d792b48be34d732d60e597c2f8465a/pydantic-2.12.5-py3-none-any.whl", hash = "sha256:e561593fccf61e8a20fc46dfc2dfe075b8be7d0188df33f221ad1f0139180f9d", size = 463580, upload-time = "2025-11-26T15:11:44.605Z" },
]

[[package]]
name = "pydantic-core"
version = "2.41.5"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "typing-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/71/70/23b021c950c2addd24ec408e9ab05d59b035b39d97cdc1130e1bce647bb6/pydantic_core-2.41.5.tar.gz", hash = "sha256:08daa51ea16ad373ffd5e7606252cc32f07bc72b28284b6bc9c6df804816476e", size = 460952, upload-time = "2025-11-04T13:43:49.098Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/87/06/8806241ff1f70d9939f9af039c6c35f2360cf16e93c2ca76f184e76b1564/pydantic_core-2.41.5-cp313-cp313-macosx_10_12_x86_64.whl", hash = "sha256:941103c9be18ac8daf7b7adca8228f8ed6bb7a1849020f643b3a14d15b1924d9", size = 2120403, upload-time = "2025-11-04T13:40:25.248Z" },
    { url = "https://files.pythonhosted.org/packages/94/02/abfa0e0bda67faa65fef1c84971c7e45928e108fe24333c81f3bfe35d5f5/pydantic_core-2.41.5-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:112e305c3314f40c93998e567879e887a3160bb8689ef3d2c04b6cc62c33ac34", size = 1896206, upload-time = "2025-11-04T13:40:27.099Z" },
    { url = "https://files.pythonhosted.org/packages/15/df/a4c740c0943e93e6500f9eb23f4ca7ec9bf71b19e608ae5b579678c8d02f/pydantic_core-2.41.5-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:0cbaad15cb0c90aa221d43c00e77bb33c93e8d36e0bf74760cd00e732d10a6a0", size = 1919307, upload-time = "2025-11-04T13:40:29.806Z" },
    { url = "https://files.pythonhosted.org/packages/9a/e3/6324802931ae1d123528988e0e86587c2072ac2e5394b4bc2bc34b61ff6e/pydantic_core-2.41.5-cp313-cp313-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:03ca43e12fab6023fc79d28ca6b39b05f794ad08ec2feccc59a339b02f2b3d33", size = 2063258, upload-time = "2025-11-04T13:40:33.544Z" },
    { url = "https://files.pythonhosted.org/packages/c9/d4/2230d7151d4957dd79c3044ea26346c148c98fbf0ee6ebd41056f2d62ab5/pydantic_core-2.41.5-cp313-cp313-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:dc799088c08fa04e43144b164feb0c13f9a0bc40503f8df3e9fde58a3c0c101e", size = 2214917, upload-time = "2025-11-04T13:40:35.479Z" },
    { url = "https://files.pythonhosted.org/packages/e6/9f/eaac5df17a3672fef0081b6c1bb0b82b33ee89aa5cec0d7b05f52fd4a1fa/pydantic_core-2.41.5-cp313-cp313-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:97aeba56665b4c3235a0e52b2c2f5ae9cd071b8a8310ad27bddb3f7fb30e9aa2", size = 2332186, upload-time = "2025-11-04T13:40:37.436Z" },
    { url = "https://files.pythonhosted.org/packages/cf/4e/35a80cae583a37cf15604b44240e45c05e04e86f9cfd766623149297e971/pydantic_core-2.41.5-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:406bf18d345822d6c21366031003612b9c77b3e29ffdb0f612367352aab7d586", size = 2073164, upload-time = "2025-11-04T13:40:40.289Z" },
    { url = "https://files.pythonhosted.org/packages/bf/e3/f6e262673c6140dd3305d144d032f7bd5f7497d3871c1428521f19f9efa2/pydantic_core-2.41.5-cp313-cp313-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:b93590ae81f7010dbe380cdeab6f515902ebcbefe0b9327cc4804d74e93ae69d", size = 2179146, upload-time = "2025-11-04T13:40:42.809Z" },
    { url = "https://files.pythonhosted.org/packages/75/c7/20bd7fc05f0c6ea2056a4565c6f36f8968c0924f19b7d97bbfea55780e73/pydantic_core-2.41.5-cp313-cp313-musllinux_1_1_aarch64.whl", hash = "sha256:01a3d0ab748ee531f4ea6c3e48ad9dac84ddba4b0d82291f87248f2f9de8d740", size = 2137788, upload-time = "2025-11-04T13:40:44.752Z" },
    { url = "https://files.pythonhosted.org/packages/3a/8d/34318ef985c45196e004bc46c6eab2eda437e744c124ef0dbe1ff2c9d06b/pydantic_core-2.41.5-cp313-cp313-musllinux_1_1_armv7l.whl", hash = "sha256:6561e94ba9dacc9c61bce40e2d6bdc3bfaa0259d3ff36ace3b1e6901936d2e3e", size = 2340133, upload-time = "2025-11-04T13:40:46.66Z" },
    { url = "https://files.pythonhosted.org/packages/9c/59/013626bf8c78a5a5d9350d12e7697d3d4de951a75565496abd40ccd46bee/pydantic_core-2.41.5-cp313-cp313-musllinux_1_1_x86_64.whl", hash = "sha256:915c3d10f81bec3a74fbd4faebe8391013ba61e5a1a8d48c4455b923bdda7858", size = 2324852, upload-time = "2025-11-04T13:40:48.575Z" },
    { url = "https://files.pythonhosted.org/packages/1a/d9/c248c103856f807ef70c18a4f986693a46a8ffe1602e5d361485da502d20/pydantic_core-2.41.5-cp313-cp313-win32.whl", hash = "sha256:650ae77860b45cfa6e2cdafc42618ceafab3a2d9a3811fcfbd3bbf8ac3c40d36", size = 1994679, upload-time = "2025-11-04T13:40:50.619Z" },
    { url = "https://files.pythonhosted.org/packages/9e/8b/341991b158ddab181cff136acd2552c9f35bd30380422a639c0671e99a91/pydantic_core-2.41.5-cp313-cp313-win_amd64.whl", hash = "sha256:79ec52ec461e99e13791ec6508c722742ad745571f234ea6255bed38c6480f11", size = 2019766, upload-time = "2025-11-04T13:40:52.631Z" },
    { url = "https://files.pythonhosted.org/packages/73/7d/f2f9db34af103bea3e09735bb40b021788a5e834c81eedb541991badf8f5/pydantic_core-2.41.5-cp313-cp313-win_arm64.whl", hash = "sha256:3f84d5c1b4ab906093bdc1ff10484838aca54ef08de4afa9de0f5f14d69639cd", size = 1981005, upload-time = "2025-11-04T13:40:54.734Z" },
    { url = "https://files.pythonhosted.org/packages/ea/28/46b7c5c9635ae96ea0fbb779e271a38129df2550f763937659ee6c5dbc65/pydantic_core-2.41.5-cp314-cp314-macosx_10_12_x86_64.whl", hash = "sha256:3f37a19d7ebcdd20b96485056ba9e8b304e27d9904d233d7b1015db320e51f0a", size = 2119622, upload-time = "2025-11-04T13:40:56.68Z" },
    { url = "https://files.pythonhosted.org/packages/74/1a/145646e5687e8d9a1e8d09acb278c8535ebe9e972e1f162ed338a622f193/pydantic_core-2.41.5-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:1d1d9764366c73f996edd17abb6d9d7649a7eb690006ab6adbda117717099b14", size = 1891725, upload-time = "2025-11-04T13:40:58.807Z" },
    { url = "https://files.pythonhosted.org/packages/23/04/e89c29e267b8060b40dca97bfc64a19b2a3cf99018167ea1677d96368273/pydantic_core-2.41.5-cp314-cp314-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:25e1c2af0fce638d5f1988b686f3b3ea8cd7de5f244ca147c777769e798a9cd1", size = 1915040, upload-time = "2025-11-04T13:41:00.853Z" },
    { url = "https://files.pythonhosted.org/packages/84/a3/15a82ac7bd97992a82257f777b3583d3e84bdb06ba6858f745daa2ec8a85/pydantic_core-2.41.5-cp314-cp314-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:506d766a8727beef16b7adaeb8ee6217c64fc813646b424d0804d67c16eddb66", size = 2063691, upload-time = "2025-11-04T13:41:03.504Z" },
    { url = "https://files.pythonhosted.org/packages/74/9b/0046701313c6ef08c0c1cf0e028c67c770a4e1275ca73131563c5f2a310a/pydantic_core-2.41.5-cp314-cp314-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:4819fa52133c9aa3c387b3328f25c1facc356491e6135b459f1de698ff64d869", size = 2213897, upload-time = "2025-11-04T13:41:05.804Z" },
    { url = "https://files.pythonhosted.org/packages/8a/cd/6bac76ecd1b27e75a95ca3a9a559c643b3afcd2dd62086d4b7a32a18b169/pydantic_core-2.41.5-cp314-cp314-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:2b761d210c9ea91feda40d25b4efe82a1707da2ef62901466a42492c028553a2", size = 2333302, upload-time = "2025-11-04T13:41:07.809Z" },
    { url = "https://files.pythonhosted.org/packages/4c/d2/ef2074dc020dd6e109611a8be4449b98cd25e1b9b8a303c2f0fca2f2bcf7/pydantic_core-2.41.5-cp314-cp314-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:22f0fb8c1c583a3b6f24df2470833b40207e907b90c928cc8d3594b76f874375", size = 2064877, upload-time = "2025-11-04T13:41:09.827Z" },
    { url = "https://files.pythonhosted.org/packages/18/66/e9db17a9a763d72f03de903883c057b2592c09509ccfe468187f2a2eef29/pydantic_core-2.41.5-cp314-cp314-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:2782c870e99878c634505236d81e5443092fba820f0373997ff75f90f68cd553", size = 2180680, upload-time = "2025-11-04T13:41:12.379Z" },
    { url = "https://files.pythonhosted.org/packages/d3/9e/3ce66cebb929f3ced22be85d4c2399b8e85b622db77dad36b73c5387f8f8/pydantic_core-2.41.5-cp314-cp314-musllinux_1_1_aarch64.whl", hash = "sha256:0177272f88ab8312479336e1d777f6b124537d47f2123f89cb37e0accea97f90", size = 2138960, upload-time = "2025-11-04T13:41:14.627Z" },
    { url = "https://files.pythonhosted.org/packages/a6/62/205a998f4327d2079326b01abee48e502ea739d174f0a89295c481a2272e/pydantic_core-2.41.5-cp314-cp314-musllinux_1_1_armv7l.whl", hash = "sha256:63510af5e38f8955b8ee5687740d6ebf7c2a0886d15a6d65c32814613681bc07", size = 2339102, upload-time = "2025-11-04T13:41:16.868Z" },
    { url = "https://files.pythonhosted.org/packages/3c/0d/f05e79471e889d74d3d88f5bd20d0ed189ad94c2423d81ff8d0000aab4ff/pydantic_core-2.41.5-cp314-cp314-musllinux_1_1_x86_64.whl", hash = "sha256:e56ba91f47764cc14f1daacd723e3e82d1a89d783f0f5afe9c364b8bb491ccdb", size = 2326039, upload-time = "2025-11-04T13:41:18.934Z" },
    { url = "https://files.pythonhosted.org/packages/ec/e1/e08a6208bb100da7e0c4b288eed624a703f4d129bde2da475721a80cab32/pydantic_core-2.41.5-cp314-cp314-win32.whl", hash = "sha256:aec5cf2fd867b4ff45b9959f8b20ea3993fc93e63c7363fe6851424c8a7e7c23", size = 1995126, upload-time = "2025-11-04T13:41:21.418Z" },
    { url = "https://files.pythonhosted.org/packages/48/5d/56ba7b24e9557f99c9237e29f5c09913c81eeb2f3217e40e922353668092/pydantic_core-2.41.5-cp314-cp314-win_amd64.whl", hash = "sha256:8e7c86f27c585ef37c35e56a96363ab8de4e549a95512445b85c96d3e2f7c1bf", size = 2015489, upload-time = "2025-11-04T13:41:24.076Z" },
    { url = "https://files.pythonhosted.org/packages/4e/bb/f7a190991ec9e3e0ba22e4993d8755bbc4a32925c0b5b42775c03e8148f9/pydantic_core-2.41.5-cp314-cp314-win_arm64.whl", hash = "sha256:e672ba74fbc2dc8eea59fb6d4aed6845e6905fc2a8afe93175d94a83ba2a01a0", size = 1977288, upload-time = "2025-11-04T13:41:26.33Z" },
    { url = "https://files.pythonhosted.org/packages/92/ed/77542d0c51538e32e15afe7899d79efce4b81eee631d99850edc2f5e9349/pydantic_core-2.41.5-cp314-cp314t-macosx_10_12_x86_64.whl", hash = "sha256:8566def80554c3faa0e65ac30ab0932b9e3a5cd7f8323764303d468e5c37595a", size = 2120255, upload-time = "2025-11-04T13:41:28.569Z" },
    { url = "https://files.pythonhosted.org/packages/bb/3d/6913dde84d5be21e284439676168b28d8bbba5600d838b9dca99de0fad71/pydantic_core-2.41.5-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:b80aa5095cd3109962a298ce14110ae16b8c1aece8b72f9dafe81cf597ad80b3", size = 1863760, upload-time = "2025-11-04T13:41:31.055Z" },
    { url = "https://files.pythonhosted.org/packages/5a/f0/e5e6b99d4191da102f2b0eb9687aaa7f5bea5d9964071a84effc3e40f997/pydantic_core-2.41.5-cp314-cp314t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:3006c3dd9ba34b0c094c544c6006cc79e87d8612999f1a5d43b769b89181f23c", size = 1878092, upload-time = "2025-11-04T13:41:33.21Z" },
    { url = "https://files.pythonhosted.org/packages/71/48/36fb760642d568925953bcc8116455513d6e34c4beaa37544118c36aba6d/pydantic_core-2.41.5-cp314-cp314t-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:72f6c8b11857a856bcfa48c86f5368439f74453563f951e473514579d44aa612", size = 2053385, upload-time = "2025-11-04T13:41:35.508Z" },
    { url = "https://files.pythonhosted.org/packages/20/25/92dc684dd8eb75a234bc1c764b4210cf2646479d54b47bf46061657292a8/pydantic_core-2.41.5-cp314-cp314t-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:5cb1b2f9742240e4bb26b652a5aeb840aa4b417c7748b6f8387927bc6e45e40d", size = 2218832, upload-time = "2025-11-04T13:41:37.732Z" },
    { url = "https://files.pythonhosted.org/packages/e2/09/f53e0b05023d3e30357d82eb35835d0f6340ca344720a4599cd663dca599/pydantic_core-2.41.5-cp314-cp314t-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:bd3d54f38609ff308209bd43acea66061494157703364ae40c951f83ba99a1a9", size = 2327585, upload-time = "2025-11-04T13:41:40Z" },
    { url = "https://files.pythonhosted.org/packages/aa/4e/2ae1aa85d6af35a39b236b1b1641de73f5a6ac4d5a7509f77b814885760c/pydantic_core-2.41.5-cp314-cp314t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:2ff4321e56e879ee8d2a879501c8e469414d948f4aba74a2d4593184eb326660", size = 2041078, upload-time = "2025-11-04T13:41:42.323Z" },
    { url = "https://files.pythonhosted.org/packages/cd/13/2e215f17f0ef326fc72afe94776edb77525142c693767fc347ed6288728d/pydantic_core-2.41.5-cp314-cp314t-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:d0d2568a8c11bf8225044aa94409e21da0cb09dcdafe9ecd10250b2baad531a9", size = 2173914, upload-time = "2025-11-04T13:41:45.221Z" },
    { url = "https://files.pythonhosted.org/packages/02/7a/f999a6dcbcd0e5660bc348a3991c8915ce6599f4f2c6ac22f01d7a10816c/pydantic_core-2.41.5-cp314-cp314t-musllinux_1_1_aarch64.whl", hash = "sha256:a39455728aabd58ceabb03c90e12f71fd30fa69615760a075b9fec596456ccc3", size = 2129560, upload-time = "2025-11-04T13:41:47.474Z" },
    { url = "https://files.pythonhosted.org/packages/3a/b1/6c990ac65e3b4c079a4fb9f5b05f5b013afa0f4ed6780a3dd236d2cbdc64/pydantic_core-2.41.5-cp314-cp314t-musllinux_1_1_armv7l.whl", hash = "sha256:239edca560d05757817c13dc17c50766136d21f7cd0fac50295499ae24f90fdf", size = 2329244, upload-time = "2025-11-04T13:41:49.992Z" },
    { url = "https://files.pythonhosted.org/packages/d9/02/3c562f3a51afd4d88fff8dffb1771b30cfdfd79befd9883ee094f5b6c0d8/pydantic_core-2.41.5-cp314-cp314t-musllinux_1_1_x86_64.whl", hash = "sha256:2a5e06546e19f24c6a96a129142a75cee553cc018ffee48a460059b1185f4470", size = 2331955, upload-time = "2025-11-04T13:41:54.079Z" },
    { url = "https://files.pythonhosted.org/packages/5c/96/5fb7d8c3c17bc8c62fdb031c47d77a1af698f1d7a406b0f79aaa1338f9ad/pydantic_core-2.41.5-cp314-cp314t-win32.whl", hash = "sha256:b4ececa40ac28afa90871c2cc2b9ffd2ff0bf749380fbdf57d165fd23da353aa", size = 1988906, upload-time = "2025-11-04T13:41:56.606Z" },
    { url = "https://files.pythonhosted.org/packages/22/ed/182129d83032702912c2e2d8bbe33c036f342cc735737064668585dac28f/pydantic_core-2.41.5-cp314-cp314t-win_amd64.whl", hash = "sha256:80aa89cad80b32a912a65332f64a4450ed00966111b6615ca6816153d3585a8c", size = 1981607, upload-time = "2025-11-04T13:41:58.889Z" },
    { url = "https://files.pythonhosted.org/packages/9f/ed/068e41660b832bb0b1aa5b58011dea2a3fe0ba7861ff38c4d4904c1c1a99/pydantic_core-2.41.5-cp314-cp314t-win_arm64.whl", hash = "sha256:35b44f37a3199f771c3eaa53051bc8a70cd7b54f333531c59e29fd4db5d15008", size = 1974769, upload-time = "2025-11-04T13:42:01.186Z" },
]

[[package]]
name = "pydantic-settings"
version = "2.13.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "pydantic" },
    { name = "python-dotenv" },
    { name = "typing-inspection" },
]
sdist = { url = "https://files.pythonhosted.org/packages/52/6d/fffca34caecc4a3f97bda81b2098da5e8ab7efc9a66e819074a11955d87e/pydantic_settings-2.13.1.tar.gz", hash = "sha256:b4c11847b15237fb0171e1462bf540e294affb9b86db4d9aa5c01730bdbe4025", size = 223826, upload-time = "2026-02-19T13:45:08.055Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/00/4b/ccc026168948fec4f7555b9164c724cf4125eac006e176541483d2c959be/pydantic_settings-2.13.1-py3-none-any.whl", hash = "sha256:d56fd801823dbeae7f0975e1f8c8e25c258eb75d278ea7abb5d9cebb01b56237", size = 58929, upload-time = "2026-02-19T13:45:06.034Z" },
]

[[package]]
name = "pyjwt"
version = "2.11.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/5c/5a/b46fa56bf322901eee5b0454a34343cdbdae202cd421775a8ee4e42fd519/pyjwt-2.11.0.tar.gz", hash = "sha256:35f95c1f0fbe5d5ba6e43f00271c275f7a1a4db1dab27bf708073b75318ea623", size = 98019, upload-time = "2026-01-30T19:59:55.694Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/6f/01/c26ce75ba460d5cd503da9e13b21a33804d38c2165dec7b716d06b13010c/pyjwt-2.11.0-py3-none-any.whl", hash = "sha256:94a6bde30eb5c8e04fee991062b534071fd1439ef58d2adc9ccb823e7bcd0469", size = 28224, upload-time = "2026-01-30T19:59:54.539Z" },
]

[package.optional-dependencies]
crypto = [
    { name = "cryptography" },
]

[[package]]
name = "python-dotenv"
version = "1.2.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/82/ed/0301aeeac3e5353ef3d94b6ec08bbcabd04a72018415dcb29e588514bba8/python_dotenv-1.2.2.tar.gz", hash = "sha256:2c371a91fbd7ba082c2c1dc1f8bf89ca22564a087c2c287cd9b662adde799cf3", size = 50135, upload-time = "2026-03-01T16:00:26.196Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/0b/d7/1959b9648791274998a9c3526f6d0ec8fd2233e4d4acce81bbae76b44b2a/python_dotenv-1.2.2-py3-none-any.whl", hash = "sha256:1d8214789a24de455a8b8bd8ae6fe3c6b69a5e3d64aa8a8e5d68e694bbcb285a", size = 22101, upload-time = "2026-03-01T16:00:25.09Z" },
]

[[package]]
name = "python-multipart"
version = "0.0.22"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/94/01/979e98d542a70714b0cb2b6728ed0b7c46792b695e3eaec3e20711271ca3/python_multipart-0.0.22.tar.gz", hash = "sha256:7340bef99a7e0032613f56dc36027b959fd3b30a787ed62d310e951f7c3a3a58", size = 37612, upload-time = "2026-01-25T10:15:56.219Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/1b/d0/397f9626e711ff749a95d96b7af99b9c566a9bb5129b8e4c10fc4d100304/python_multipart-0.0.22-py3-none-any.whl", hash = "sha256:2b2cd894c83d21bf49d702499531c7bafd057d730c201782048f7945d82de155", size = 24579, upload-time = "2026-01-25T10:15:54.811Z" },
]

[[package]]
name = "pywin32"
version = "311"
source = { registry = "https://pypi.org/simple" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/a5/be/3fd5de0979fcb3994bfee0d65ed8ca9506a8a1260651b86174f6a86f52b3/pywin32-311-cp313-cp313-win32.whl", hash = "sha256:f95ba5a847cba10dd8c4d8fefa9f2a6cf283b8b88ed6178fa8a6c1ab16054d0d", size = 8705700, upload-time = "2025-07-14T20:13:26.471Z" },
    { url = "https://files.pythonhosted.org/packages/e3/28/e0a1909523c6890208295a29e05c2adb2126364e289826c0a8bc7297bd5c/pywin32-311-cp313-cp313-win_amd64.whl", hash = "sha256:718a38f7e5b058e76aee1c56ddd06908116d35147e133427e59a3983f703a20d", size = 9494700, upload-time = "2025-07-14T20:13:28.243Z" },
    { url = "https://files.pythonhosted.org/packages/04/bf/90339ac0f55726dce7d794e6d79a18a91265bdf3aa70b6b9ca52f35e022a/pywin32-311-cp313-cp313-win_arm64.whl", hash = "sha256:7b4075d959648406202d92a2310cb990fea19b535c7f4a78d3f5e10b926eeb8a", size = 8709318, upload-time = "2025-07-14T20:13:30.348Z" },
    { url = "https://files.pythonhosted.org/packages/c9/31/097f2e132c4f16d99a22bfb777e0fd88bd8e1c634304e102f313af69ace5/pywin32-311-cp314-cp314-win32.whl", hash = "sha256:b7a2c10b93f8986666d0c803ee19b5990885872a7de910fc460f9b0c2fbf92ee", size = 8840714, upload-time = "2025-07-14T20:13:32.449Z" },
    { url = "https://files.pythonhosted.org/packages/90/4b/07c77d8ba0e01349358082713400435347df8426208171ce297da32c313d/pywin32-311-cp314-cp314-win_amd64.whl", hash = "sha256:3aca44c046bd2ed8c90de9cb8427f581c479e594e99b5c0bb19b29c10fd6cb87", size = 9656800, upload-time = "2025-07-14T20:13:34.312Z" },
    { url = "https://files.pythonhosted.org/packages/c0/d2/21af5c535501a7233e734b8af901574572da66fcc254cb35d0609c9080dd/pywin32-311-cp314-cp314-win_arm64.whl", hash = "sha256:a508e2d9025764a8270f93111a970e1d0fbfc33f4153b388bb649b7eec4f9b42", size = 8932540, upload-time = "2025-07-14T20:13:36.379Z" },
]

[[package]]
name = "referencing"
version = "0.37.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "attrs" },
    { name = "rpds-py" },
]
sdist = { url = "https://files.pythonhosted.org/packages/22/f5/df4e9027acead3ecc63e50fe1e36aca1523e1719559c499951bb4b53188f/referencing-0.37.0.tar.gz", hash = "sha256:44aefc3142c5b842538163acb373e24cce6632bd54bdb01b21ad5863489f50d8", size = 78036, upload-time = "2025-10-13T15:30:48.871Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/2c/58/ca301544e1fa93ed4f80d724bf5b194f6e4b945841c5bfd555878eea9fcb/referencing-0.37.0-py3-none-any.whl", hash = "sha256:381329a9f99628c9069361716891d34ad94af76e461dcb0335825aecc7692231", size = 26766, upload-time = "2025-10-13T15:30:47.625Z" },
]

[[package]]
name = "requests"
version = "2.32.5"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "certifi" },
    { name = "charset-normalizer" },
    { name = "idna" },
    { name = "urllib3" },
]
sdist = { url = "https://files.pythonhosted.org/packages/c9/74/b3ff8e6c8446842c3f5c837e9c3dfcfe2018ea6ecef224c710c85ef728f4/requests-2.32.5.tar.gz", hash = "sha256:dbba0bac56e100853db0ea71b82b4dfd5fe2bf6d3754a8893c3af500cec7d7cf", size = 134517, upload-time = "2025-08-18T20:46:02.573Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/1e/db/4254e3eabe8020b458f1a747140d32277ec7a271daf1d235b70dc0b4e6e3/requests-2.32.5-py3-none-any.whl", hash = "sha256:2462f94637a34fd532264295e186976db0f5d453d1cdd31473c85a6a161affb6", size = 64738, upload-time = "2025-08-18T20:46:00.542Z" },
]

[[package]]
name = "rpds-py"
version = "0.30.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/20/af/3f2f423103f1113b36230496629986e0ef7e199d2aa8392452b484b38ced/rpds_py-0.30.0.tar.gz", hash = "sha256:dd8ff7cf90014af0c0f787eea34794ebf6415242ee1d6fa91eaba725cc441e84", size = 69469, upload-time = "2025-11-30T20:24:38.837Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/ed/dc/d61221eb88ff410de3c49143407f6f3147acf2538c86f2ab7ce65ae7d5f9/rpds_py-0.30.0-cp313-cp313-macosx_10_12_x86_64.whl", hash = "sha256:f83424d738204d9770830d35290ff3273fbb02b41f919870479fab14b9d303b2", size = 374887, upload-time = "2025-11-30T20:22:41.812Z" },
    { url = "https://files.pythonhosted.org/packages/fd/32/55fb50ae104061dbc564ef15cc43c013dc4a9f4527a1f4d99baddf56fe5f/rpds_py-0.30.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:e7536cd91353c5273434b4e003cbda89034d67e7710eab8761fd918ec6c69cf8", size = 358904, upload-time = "2025-11-30T20:22:43.479Z" },
    { url = "https://files.pythonhosted.org/packages/58/70/faed8186300e3b9bdd138d0273109784eea2396c68458ed580f885dfe7ad/rpds_py-0.30.0-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:2771c6c15973347f50fece41fc447c054b7ac2ae0502388ce3b6738cd366e3d4", size = 389945, upload-time = "2025-11-30T20:22:44.819Z" },
    { url = "https://files.pythonhosted.org/packages/bd/a8/073cac3ed2c6387df38f71296d002ab43496a96b92c823e76f46b8af0543/rpds_py-0.30.0-cp313-cp313-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:0a59119fc6e3f460315fe9d08149f8102aa322299deaa5cab5b40092345c2136", size = 407783, upload-time = "2025-11-30T20:22:46.103Z" },
    { url = "https://files.pythonhosted.org/packages/77/57/5999eb8c58671f1c11eba084115e77a8899d6e694d2a18f69f0ba471ec8b/rpds_py-0.30.0-cp313-cp313-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:76fec018282b4ead0364022e3c54b60bf368b9d926877957a8624b58419169b7", size = 515021, upload-time = "2025-11-30T20:22:47.458Z" },
    { url = "https://files.pythonhosted.org/packages/e0/af/5ab4833eadc36c0a8ed2bc5c0de0493c04f6c06de223170bd0798ff98ced/rpds_py-0.30.0-cp313-cp313-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:692bef75a5525db97318e8cd061542b5a79812d711ea03dbc1f6f8dbb0c5f0d2", size = 414589, upload-time = "2025-11-30T20:22:48.872Z" },
    { url = "https://files.pythonhosted.org/packages/b7/de/f7192e12b21b9e9a68a6d0f249b4af3fdcdff8418be0767a627564afa1f1/rpds_py-0.30.0-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:9027da1ce107104c50c81383cae773ef5c24d296dd11c99e2629dbd7967a20c6", size = 394025, upload-time = "2025-11-30T20:22:50.196Z" },
    { url = "https://files.pythonhosted.org/packages/91/c4/fc70cd0249496493500e7cc2de87504f5aa6509de1e88623431fec76d4b6/rpds_py-0.30.0-cp313-cp313-manylinux_2_31_riscv64.whl", hash = "sha256:9cf69cdda1f5968a30a359aba2f7f9aa648a9ce4b580d6826437f2b291cfc86e", size = 408895, upload-time = "2025-11-30T20:22:51.87Z" },
    { url = "https://files.pythonhosted.org/packages/58/95/d9275b05ab96556fefff73a385813eb66032e4c99f411d0795372d9abcea/rpds_py-0.30.0-cp313-cp313-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:a4796a717bf12b9da9d3ad002519a86063dcac8988b030e405704ef7d74d2d9d", size = 422799, upload-time = "2025-11-30T20:22:53.341Z" },
    { url = "https://files.pythonhosted.org/packages/06/c1/3088fc04b6624eb12a57eb814f0d4997a44b0d208d6cace713033ff1a6ba/rpds_py-0.30.0-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:5d4c2aa7c50ad4728a094ebd5eb46c452e9cb7edbfdb18f9e1221f597a73e1e7", size = 572731, upload-time = "2025-11-30T20:22:54.778Z" },
    { url = "https://files.pythonhosted.org/packages/d8/42/c612a833183b39774e8ac8fecae81263a68b9583ee343db33ab571a7ce55/rpds_py-0.30.0-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:ba81a9203d07805435eb06f536d95a266c21e5b2dfbf6517748ca40c98d19e31", size = 599027, upload-time = "2025-11-30T20:22:56.212Z" },
    { url = "https://files.pythonhosted.org/packages/5f/60/525a50f45b01d70005403ae0e25f43c0384369ad24ffe46e8d9068b50086/rpds_py-0.30.0-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:945dccface01af02675628334f7cf49c2af4c1c904748efc5cf7bbdf0b579f95", size = 563020, upload-time = "2025-11-30T20:22:58.2Z" },
    { url = "https://files.pythonhosted.org/packages/0b/5d/47c4655e9bcd5ca907148535c10e7d489044243cc9941c16ed7cd53be91d/rpds_py-0.30.0-cp313-cp313-win32.whl", hash = "sha256:b40fb160a2db369a194cb27943582b38f79fc4887291417685f3ad693c5a1d5d", size = 223139, upload-time = "2025-11-30T20:23:00.209Z" },
    { url = "https://files.pythonhosted.org/packages/f2/e1/485132437d20aa4d3e1d8b3fb5a5e65aa8139f1e097080c2a8443201742c/rpds_py-0.30.0-cp313-cp313-win_amd64.whl", hash = "sha256:806f36b1b605e2d6a72716f321f20036b9489d29c51c91f4dd29a3e3afb73b15", size = 240224, upload-time = "2025-11-30T20:23:02.008Z" },
    { url = "https://files.pythonhosted.org/packages/24/95/ffd128ed1146a153d928617b0ef673960130be0009c77d8fbf0abe306713/rpds_py-0.30.0-cp313-cp313-win_arm64.whl", hash = "sha256:d96c2086587c7c30d44f31f42eae4eac89b60dabbac18c7669be3700f13c3ce1", size = 230645, upload-time = "2025-11-30T20:23:03.43Z" },
    { url = "https://files.pythonhosted.org/packages/ff/1b/b10de890a0def2a319a2626334a7f0ae388215eb60914dbac8a3bae54435/rpds_py-0.30.0-cp313-cp313t-macosx_10_12_x86_64.whl", hash = "sha256:eb0b93f2e5c2189ee831ee43f156ed34e2a89a78a66b98cadad955972548be5a", size = 364443, upload-time = "2025-11-30T20:23:04.878Z" },
    { url = "https://files.pythonhosted.org/packages/0d/bf/27e39f5971dc4f305a4fb9c672ca06f290f7c4e261c568f3dea16a410d47/rpds_py-0.30.0-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:922e10f31f303c7c920da8981051ff6d8c1a56207dbdf330d9047f6d30b70e5e", size = 353375, upload-time = "2025-11-30T20:23:06.342Z" },
    { url = "https://files.pythonhosted.org/packages/40/58/442ada3bba6e8e6615fc00483135c14a7538d2ffac30e2d933ccf6852232/rpds_py-0.30.0-cp313-cp313t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:cdc62c8286ba9bf7f47befdcea13ea0e26bf294bda99758fd90535cbaf408000", size = 383850, upload-time = "2025-11-30T20:23:07.825Z" },
    { url = "https://files.pythonhosted.org/packages/14/14/f59b0127409a33c6ef6f5c1ebd5ad8e32d7861c9c7adfa9a624fc3889f6c/rpds_py-0.30.0-cp313-cp313t-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:47f9a91efc418b54fb8190a6b4aa7813a23fb79c51f4bb84e418f5476c38b8db", size = 392812, upload-time = "2025-11-30T20:23:09.228Z" },
    { url = "https://files.pythonhosted.org/packages/b3/66/e0be3e162ac299b3a22527e8913767d869e6cc75c46bd844aa43fb81ab62/rpds_py-0.30.0-cp313-cp313t-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:1f3587eb9b17f3789ad50824084fa6f81921bbf9a795826570bda82cb3ed91f2", size = 517841, upload-time = "2025-11-30T20:23:11.186Z" },
    { url = "https://files.pythonhosted.org/packages/3d/55/fa3b9cf31d0c963ecf1ba777f7cf4b2a2c976795ac430d24a1f43d25a6ba/rpds_py-0.30.0-cp313-cp313t-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:39c02563fc592411c2c61d26b6c5fe1e51eaa44a75aa2c8735ca88b0d9599daa", size = 408149, upload-time = "2025-11-30T20:23:12.864Z" },
    { url = "https://files.pythonhosted.org/packages/60/ca/780cf3b1a32b18c0f05c441958d3758f02544f1d613abf9488cd78876378/rpds_py-0.30.0-cp313-cp313t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:51a1234d8febafdfd33a42d97da7a43f5dcb120c1060e352a3fbc0c6d36e2083", size = 383843, upload-time = "2025-11-30T20:23:14.638Z" },
    { url = "https://files.pythonhosted.org/packages/82/86/d5f2e04f2aa6247c613da0c1dd87fcd08fa17107e858193566048a1e2f0a/rpds_py-0.30.0-cp313-cp313t-manylinux_2_31_riscv64.whl", hash = "sha256:eb2c4071ab598733724c08221091e8d80e89064cd472819285a9ab0f24bcedb9", size = 396507, upload-time = "2025-11-30T20:23:16.105Z" },
    { url = "https://files.pythonhosted.org/packages/4b/9a/453255d2f769fe44e07ea9785c8347edaf867f7026872e76c1ad9f7bed92/rpds_py-0.30.0-cp313-cp313t-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:6bdfdb946967d816e6adf9a3d8201bfad269c67efe6cefd7093ef959683c8de0", size = 414949, upload-time = "2025-11-30T20:23:17.539Z" },
    { url = "https://files.pythonhosted.org/packages/a3/31/622a86cdc0c45d6df0e9ccb6becdba5074735e7033c20e401a6d9d0e2ca0/rpds_py-0.30.0-cp313-cp313t-musllinux_1_2_aarch64.whl", hash = "sha256:c77afbd5f5250bf27bf516c7c4a016813eb2d3e116139aed0096940c5982da94", size = 565790, upload-time = "2025-11-30T20:23:19.029Z" },
    { url = "https://files.pythonhosted.org/packages/1c/5d/15bbf0fb4a3f58a3b1c67855ec1efcc4ceaef4e86644665fff03e1b66d8d/rpds_py-0.30.0-cp313-cp313t-musllinux_1_2_i686.whl", hash = "sha256:61046904275472a76c8c90c9ccee9013d70a6d0f73eecefd38c1ae7c39045a08", size = 590217, upload-time = "2025-11-30T20:23:20.885Z" },
    { url = "https://files.pythonhosted.org/packages/6d/61/21b8c41f68e60c8cc3b2e25644f0e3681926020f11d06ab0b78e3c6bbff1/rpds_py-0.30.0-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:4c5f36a861bc4b7da6516dbdf302c55313afa09b81931e8280361a4f6c9a2d27", size = 555806, upload-time = "2025-11-30T20:23:22.488Z" },
    { url = "https://files.pythonhosted.org/packages/f9/39/7e067bb06c31de48de3eb200f9fc7c58982a4d3db44b07e73963e10d3be9/rpds_py-0.30.0-cp313-cp313t-win32.whl", hash = "sha256:3d4a69de7a3e50ffc214ae16d79d8fbb0922972da0356dcf4d0fdca2878559c6", size = 211341, upload-time = "2025-11-30T20:23:24.449Z" },
    { url = "https://files.pythonhosted.org/packages/0a/4d/222ef0b46443cf4cf46764d9c630f3fe4abaa7245be9417e56e9f52b8f65/rpds_py-0.30.0-cp313-cp313t-win_amd64.whl", hash = "sha256:f14fc5df50a716f7ece6a80b6c78bb35ea2ca47c499e422aa4463455dd96d56d", size = 225768, upload-time = "2025-11-30T20:23:25.908Z" },
    { url = "https://files.pythonhosted.org/packages/86/81/dad16382ebbd3d0e0328776d8fd7ca94220e4fa0798d1dc5e7da48cb3201/rpds_py-0.30.0-cp314-cp314-macosx_10_12_x86_64.whl", hash = "sha256:68f19c879420aa08f61203801423f6cd5ac5f0ac4ac82a2368a9fcd6a9a075e0", size = 362099, upload-time = "2025-11-30T20:23:27.316Z" },
    { url = "https://files.pythonhosted.org/packages/2b/60/19f7884db5d5603edf3c6bce35408f45ad3e97e10007df0e17dd57af18f8/rpds_py-0.30.0-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:ec7c4490c672c1a0389d319b3a9cfcd098dcdc4783991553c332a15acf7249be", size = 353192, upload-time = "2025-11-30T20:23:29.151Z" },
    { url = "https://files.pythonhosted.org/packages/bf/c4/76eb0e1e72d1a9c4703c69607cec123c29028bff28ce41588792417098ac/rpds_py-0.30.0-cp314-cp314-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:f251c812357a3fed308d684a5079ddfb9d933860fc6de89f2b7ab00da481e65f", size = 384080, upload-time = "2025-11-30T20:23:30.785Z" },
    { url = "https://files.pythonhosted.org/packages/72/87/87ea665e92f3298d1b26d78814721dc39ed8d2c74b86e83348d6b48a6f31/rpds_py-0.30.0-cp314-cp314-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:ac98b175585ecf4c0348fd7b29c3864bda53b805c773cbf7bfdaffc8070c976f", size = 394841, upload-time = "2025-11-30T20:23:32.209Z" },
    { url = "https://files.pythonhosted.org/packages/77/ad/7783a89ca0587c15dcbf139b4a8364a872a25f861bdb88ed99f9b0dec985/rpds_py-0.30.0-cp314-cp314-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:3e62880792319dbeb7eb866547f2e35973289e7d5696c6e295476448f5b63c87", size = 516670, upload-time = "2025-11-30T20:23:33.742Z" },
    { url = "https://files.pythonhosted.org/packages/5b/3c/2882bdac942bd2172f3da574eab16f309ae10a3925644e969536553cb4ee/rpds_py-0.30.0-cp314-cp314-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:4e7fc54e0900ab35d041b0601431b0a0eb495f0851a0639b6ef90f7741b39a18", size = 408005, upload-time = "2025-11-30T20:23:35.253Z" },
    { url = "https://files.pythonhosted.org/packages/ce/81/9a91c0111ce1758c92516a3e44776920b579d9a7c09b2b06b642d4de3f0f/rpds_py-0.30.0-cp314-cp314-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:47e77dc9822d3ad616c3d5759ea5631a75e5809d5a28707744ef79d7a1bcfcad", size = 382112, upload-time = "2025-11-30T20:23:36.842Z" },
    { url = "https://files.pythonhosted.org/packages/cf/8e/1da49d4a107027e5fbc64daeab96a0706361a2918da10cb41769244b805d/rpds_py-0.30.0-cp314-cp314-manylinux_2_31_riscv64.whl", hash = "sha256:b4dc1a6ff022ff85ecafef7979a2c6eb423430e05f1165d6688234e62ba99a07", size = 399049, upload-time = "2025-11-30T20:23:38.343Z" },
    { url = "https://files.pythonhosted.org/packages/df/5a/7ee239b1aa48a127570ec03becbb29c9d5a9eb092febbd1699d567cae859/rpds_py-0.30.0-cp314-cp314-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:4559c972db3a360808309e06a74628b95eaccbf961c335c8fe0d590cf587456f", size = 415661, upload-time = "2025-11-30T20:23:40.263Z" },
    { url = "https://files.pythonhosted.org/packages/70/ea/caa143cf6b772f823bc7929a45da1fa83569ee49b11d18d0ada7f5ee6fd6/rpds_py-0.30.0-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:0ed177ed9bded28f8deb6ab40c183cd1192aa0de40c12f38be4d59cd33cb5c65", size = 565606, upload-time = "2025-11-30T20:23:42.186Z" },
    { url = "https://files.pythonhosted.org/packages/64/91/ac20ba2d69303f961ad8cf55bf7dbdb4763f627291ba3d0d7d67333cced9/rpds_py-0.30.0-cp314-cp314-musllinux_1_2_i686.whl", hash = "sha256:ad1fa8db769b76ea911cb4e10f049d80bf518c104f15b3edb2371cc65375c46f", size = 591126, upload-time = "2025-11-30T20:23:44.086Z" },
    { url = "https://files.pythonhosted.org/packages/21/20/7ff5f3c8b00c8a95f75985128c26ba44503fb35b8e0259d812766ea966c7/rpds_py-0.30.0-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:46e83c697b1f1c72b50e5ee5adb4353eef7406fb3f2043d64c33f20ad1c2fc53", size = 553371, upload-time = "2025-11-30T20:23:46.004Z" },
    { url = "https://files.pythonhosted.org/packages/72/c7/81dadd7b27c8ee391c132a6b192111ca58d866577ce2d9b0ca157552cce0/rpds_py-0.30.0-cp314-cp314-win32.whl", hash = "sha256:ee454b2a007d57363c2dfd5b6ca4a5d7e2c518938f8ed3b706e37e5d470801ed", size = 215298, upload-time = "2025-11-30T20:23:47.696Z" },
    { url = "https://files.pythonhosted.org/packages/3e/d2/1aaac33287e8cfb07aab2e6b8ac1deca62f6f65411344f1433c55e6f3eb8/rpds_py-0.30.0-cp314-cp314-win_amd64.whl", hash = "sha256:95f0802447ac2d10bcc69f6dc28fe95fdf17940367b21d34e34c737870758950", size = 228604, upload-time = "2025-11-30T20:23:49.501Z" },
    { url = "https://files.pythonhosted.org/packages/e8/95/ab005315818cc519ad074cb7784dae60d939163108bd2b394e60dc7b5461/rpds_py-0.30.0-cp314-cp314-win_arm64.whl", hash = "sha256:613aa4771c99f03346e54c3f038e4cc574ac09a3ddfb0e8878487335e96dead6", size = 222391, upload-time = "2025-11-30T20:23:50.96Z" },
    { url = "https://files.pythonhosted.org/packages/9e/68/154fe0194d83b973cdedcdcc88947a2752411165930182ae41d983dcefa6/rpds_py-0.30.0-cp314-cp314t-macosx_10_12_x86_64.whl", hash = "sha256:7e6ecfcb62edfd632e56983964e6884851786443739dbfe3582947e87274f7cb", size = 364868, upload-time = "2025-11-30T20:23:52.494Z" },
    { url = "https://files.pythonhosted.org/packages/83/69/8bbc8b07ec854d92a8b75668c24d2abcb1719ebf890f5604c61c9369a16f/rpds_py-0.30.0-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:a1d0bc22a7cdc173fedebb73ef81e07faef93692b8c1ad3733b67e31e1b6e1b8", size = 353747, upload-time = "2025-11-30T20:23:54.036Z" },
    { url = "https://files.pythonhosted.org/packages/ab/00/ba2e50183dbd9abcce9497fa5149c62b4ff3e22d338a30d690f9af970561/rpds_py-0.30.0-cp314-cp314t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:0d08f00679177226c4cb8c5265012eea897c8ca3b93f429e546600c971bcbae7", size = 383795, upload-time = "2025-11-30T20:23:55.556Z" },
    { url = "https://files.pythonhosted.org/packages/05/6f/86f0272b84926bcb0e4c972262f54223e8ecc556b3224d281e6598fc9268/rpds_py-0.30.0-cp314-cp314t-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:5965af57d5848192c13534f90f9dd16464f3c37aaf166cc1da1cae1fd5a34898", size = 393330, upload-time = "2025-11-30T20:23:57.033Z" },
    { url = "https://files.pythonhosted.org/packages/cb/e9/0e02bb2e6dc63d212641da45df2b0bf29699d01715913e0d0f017ee29438/rpds_py-0.30.0-cp314-cp314t-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:9a4e86e34e9ab6b667c27f3211ca48f73dba7cd3d90f8d5b11be56e5dbc3fb4e", size = 518194, upload-time = "2025-11-30T20:23:58.637Z" },
    { url = "https://files.pythonhosted.org/packages/ee/ca/be7bca14cf21513bdf9c0606aba17d1f389ea2b6987035eb4f62bd923f25/rpds_py-0.30.0-cp314-cp314t-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:e5d3e6b26f2c785d65cc25ef1e5267ccbe1b069c5c21b8cc724efee290554419", size = 408340, upload-time = "2025-11-30T20:24:00.2Z" },
    { url = "https://files.pythonhosted.org/packages/c2/c7/736e00ebf39ed81d75544c0da6ef7b0998f8201b369acf842f9a90dc8fce/rpds_py-0.30.0-cp314-cp314t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:626a7433c34566535b6e56a1b39a7b17ba961e97ce3b80ec62e6f1312c025551", size = 383765, upload-time = "2025-11-30T20:24:01.759Z" },
    { url = "https://files.pythonhosted.org/packages/4a/3f/da50dfde9956aaf365c4adc9533b100008ed31aea635f2b8d7b627e25b49/rpds_py-0.30.0-cp314-cp314t-manylinux_2_31_riscv64.whl", hash = "sha256:acd7eb3f4471577b9b5a41baf02a978e8bdeb08b4b355273994f8b87032000a8", size = 396834, upload-time = "2025-11-30T20:24:03.687Z" },
    { url = "https://files.pythonhosted.org/packages/4e/00/34bcc2565b6020eab2623349efbdec810676ad571995911f1abdae62a3a0/rpds_py-0.30.0-cp314-cp314t-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:fe5fa731a1fa8a0a56b0977413f8cacac1768dad38d16b3a296712709476fbd5", size = 415470, upload-time = "2025-11-30T20:24:05.232Z" },
    { url = "https://files.pythonhosted.org/packages/8c/28/882e72b5b3e6f718d5453bd4d0d9cf8df36fddeb4ddbbab17869d5868616/rpds_py-0.30.0-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:74a3243a411126362712ee1524dfc90c650a503502f135d54d1b352bd01f2404", size = 565630, upload-time = "2025-11-30T20:24:06.878Z" },
    { url = "https://files.pythonhosted.org/packages/3b/97/04a65539c17692de5b85c6e293520fd01317fd878ea1995f0367d4532fb1/rpds_py-0.30.0-cp314-cp314t-musllinux_1_2_i686.whl", hash = "sha256:3e8eeb0544f2eb0d2581774be4c3410356eba189529a6b3e36bbbf9696175856", size = 591148, upload-time = "2025-11-30T20:24:08.445Z" },
    { url = "https://files.pythonhosted.org/packages/85/70/92482ccffb96f5441aab93e26c4d66489eb599efdcf96fad90c14bbfb976/rpds_py-0.30.0-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:dbd936cde57abfee19ab3213cf9c26be06d60750e60a8e4dd85d1ab12c8b1f40", size = 556030, upload-time = "2025-11-30T20:24:10.956Z" },
    { url = "https://files.pythonhosted.org/packages/20/53/7c7e784abfa500a2b6b583b147ee4bb5a2b3747a9166bab52fec4b5b5e7d/rpds_py-0.30.0-cp314-cp314t-win32.whl", hash = "sha256:dc824125c72246d924f7f796b4f63c1e9dc810c7d9e2355864b3c3a73d59ade0", size = 211570, upload-time = "2025-11-30T20:24:12.735Z" },
    { url = "https://files.pythonhosted.org/packages/d0/02/fa464cdfbe6b26e0600b62c528b72d8608f5cc49f96b8d6e38c95d60c676/rpds_py-0.30.0-cp314-cp314t-win_amd64.whl", hash = "sha256:27f4b0e92de5bfbc6f86e43959e6edd1425c33b5e69aab0984a72047f2bcf1e3", size = 226532, upload-time = "2025-11-30T20:24:14.634Z" },
]

[[package]]
name = "sniffio"
version = "1.3.1"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/a2/87/a6771e1546d97e7e041b6ae58d80074f81b7d5121207425c964ddf5cfdbd/sniffio-1.3.1.tar.gz", hash = "sha256:f4324edc670a0f49750a81b895f35c3adb843cca46f0530f79fc1babb23789dc", size = 20372, upload-time = "2024-02-25T23:20:04.057Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/e9/44/75a9c9421471a6c4805dbf2356f7c181a29c1879239abab1ea2cc8f38b40/sniffio-1.3.1-py3-none-any.whl", hash = "sha256:2f6da418d1f1e0fddd844478f41680e794e6051915791a034ff65e5f100525a2", size = 10235, upload-time = "2024-02-25T23:20:01.196Z" },
]

[[package]]
name = "sse-starlette"
version = "3.3.2"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "anyio" },
    { name = "starlette" },
]
sdist = { url = "https://files.pythonhosted.org/packages/5a/9f/c3695c2d2d4ef70072c3a06992850498b01c6bc9be531950813716b426fa/sse_starlette-3.3.2.tar.gz", hash = "sha256:678fca55a1945c734d8472a6cad186a55ab02840b4f6786f5ee8770970579dcd", size = 32326, upload-time = "2026-02-28T11:24:34.36Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/61/28/8cb142d3fe80c4a2d8af54ca0b003f47ce0ba920974e7990fa6e016402d1/sse_starlette-3.3.2-py3-none-any.whl", hash = "sha256:5c3ea3dad425c601236726af2f27689b74494643f57017cafcb6f8c9acfbb862", size = 14270, upload-time = "2026-02-28T11:24:32.984Z" },
]

[[package]]
name = "starlette"
version = "0.52.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "anyio" },
]
sdist = { url = "https://files.pythonhosted.org/packages/c4/68/79977123bb7be889ad680d79a40f339082c1978b5cfcf62c2d8d196873ac/starlette-0.52.1.tar.gz", hash = "sha256:834edd1b0a23167694292e94f597773bc3f89f362be6effee198165a35d62933", size = 2653702, upload-time = "2026-01-18T13:34:11.062Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/81/0d/13d1d239a25cbfb19e740db83143e95c772a1fe10202dda4b76792b114dd/starlette-0.52.1-py3-none-any.whl", hash = "sha256:0029d43eb3d273bc4f83a08720b4912ea4b071087a3b48db01b7c839f7954d74", size = 74272, upload-time = "2026-01-18T13:34:09.188Z" },
]

[[package]]
name = "tqdm"
version = "4.67.3"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "colorama", marker = "sys_platform == 'win32'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/09/a9/6ba95a270c6f1fbcd8dac228323f2777d886cb206987444e4bce66338dd4/tqdm-4.67.3.tar.gz", hash = "sha256:7d825f03f89244ef73f1d4ce193cb1774a8179fd96f31d7e1dcde62092b960bb", size = 169598, upload-time = "2026-02-03T17:35:53.048Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/16/e1/3079a9ff9b8e11b846c6ac5c8b5bfb7ff225eee721825310c91b3b50304f/tqdm-4.67.3-py3-none-any.whl", hash = "sha256:ee1e4c0e59148062281c49d80b25b67771a127c85fc9676d3be5f243206826bf", size = 78374, upload-time = "2026-02-03T17:35:50.982Z" },
]

[[package]]
name = "types-requests"
version = "2.32.4.20260107"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "urllib3" },
]
sdist = { url = "https://files.pythonhosted.org/packages/0f/f3/a0663907082280664d745929205a89d41dffb29e89a50f753af7d57d0a96/types_requests-2.32.4.20260107.tar.gz", hash = "sha256:018a11ac158f801bfa84857ddec1650750e393df8a004a8a9ae2a9bec6fcb24f", size = 23165, upload-time = "2026-01-07T03:20:54.091Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/1c/12/709ea261f2bf91ef0a26a9eed20f2623227a8ed85610c1e54c5805692ecb/types_requests-2.32.4.20260107-py3-none-any.whl", hash = "sha256:b703fe72f8ce5b31ef031264fe9395cac8f46a04661a79f7ed31a80fb308730d", size = 20676, upload-time = "2026-01-07T03:20:52.929Z" },
]

[[package]]
name = "typing-extensions"
version = "4.15.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/72/94/1a15dd82efb362ac84269196e94cf00f187f7ed21c242792a923cdb1c61f/typing_extensions-4.15.0.tar.gz", hash = "sha256:0cea48d173cc12fa28ecabc3b837ea3cf6f38c6d1136f85cbaaf598984861466", size = 109391, upload-time = "2025-08-25T13:49:26.313Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/18/67/36e9267722cc04a6b9f15c7f3441c2363321a3ea07da7ae0c0707beb2a9c/typing_extensions-4.15.0-py3-none-any.whl", hash = "sha256:f0fa19c6845758ab08074a0cfa8b7aecb71c999ca73d62883bc25cc018c4e548", size = 44614, upload-time = "2025-08-25T13:49:24.86Z" },
]

[[package]]
name = "typing-inspection"
version = "0.4.2"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "typing-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/55/e3/70399cb7dd41c10ac53367ae42139cf4b1ca5f36bb3dc6c9d33acdb43655/typing_inspection-0.4.2.tar.gz", hash = "sha256:ba561c48a67c5958007083d386c3295464928b01faa735ab8547c5692e87f464", size = 75949, upload-time = "2025-10-01T02:14:41.687Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/dc/9b/47798a6c91d8bdb567fe2698fe81e0c6b7cb7ef4d13da4114b41d239f65d/typing_inspection-0.4.2-py3-none-any.whl", hash = "sha256:4ed1cacbdc298c220f1bd249ed5287caa16f34d44ef4e9c3d0cbad5b521545e7", size = 14611, upload-time = "2025-10-01T02:14:40.154Z" },
]

[[package]]
name = "urllib3"
version = "2.6.3"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/c7/24/5f1b3bdffd70275f6661c76461e25f024d5a38a46f04aaca912426a2b1d3/urllib3-2.6.3.tar.gz", hash = "sha256:1b62b6884944a57dbe321509ab94fd4d3b307075e0c2eae991ac71ee15ad38ed", size = 435556, upload-time = "2026-01-07T16:24:43.925Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/39/08/aaaad47bc4e9dc8c725e68f9d04865dbcb2052843ff09c97b08904852d84/urllib3-2.6.3-py3-none-any.whl", hash = "sha256:bf272323e553dfb2e87d9bfd225ca7b0f467b919d7bbd355436d3fd37cb0acd4", size = 131584, upload-time = "2026-01-07T16:24:42.685Z" },
]

[[package]]
name = "uvicorn"
version = "0.41.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "click" },
    { name = "h11" },
]
sdist = { url = "https://files.pythonhosted.org/packages/32/ce/eeb58ae4ac36fe09e3842eb02e0eb676bf2c53ae062b98f1b2531673efdd/uvicorn-0.41.0.tar.gz", hash = "sha256:09d11cf7008da33113824ee5a1c6422d89fbc2ff476540d69a34c87fab8b571a", size = 82633, upload-time = "2026-02-16T23:07:24.1Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/83/e4/d04a086285c20886c0daad0e026f250869201013d18f81d9ff5eada73a88/uvicorn-0.41.0-py3-none-any.whl", hash = "sha256:29e35b1d2c36a04b9e180d4007ede3bcb32a85fbdfd6c6aeb3f26839de088187", size = 68783, upload-time = "2026-02-16T23:07:22.357Z" },
]
```

## File: `python/openai-basic/.gitignore`
```
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
PICKUP_REMINDER

# PyInstaller
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
.python-version

# pipenv
Pipfile.lock

# poetry
poetry.lock

# pdm
.pdm.toml

# PEP 582
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# uv
uv.lock


```

## File: `python/openai-basic/README.md`
```markdown
[![Made with Acontext](https://assets.memodb.io/Acontext/badge-made-with-acontext-dark.svg)](https://acontext.io)

# OpenAI Python SDK with Acontext Example

This example demonstrates how to use the [OpenAI Python SDK](https://github.com/openai/openai-python) directly with Acontext for session persistence and task extraction.

## Features

- **Multi-turn conversations**: Maintains conversation history across multiple interactions
- **Tool usage**: Demonstrates function calling with `get_weather` and `book_flight` tools
- **Manual tool execution**: Shows how to handle tool calls from OpenAI API responses
- **Acontext integration**: Sends conversation messages to Acontext for task extraction and analysis

## How It Works

The example creates an agent that helps plan a trip:

1. **First interaction**: User asks for a 3-day trip plan in Finland
2. **Second interaction**: User requests weather check for Finland
3. **Third interaction**: User books a flight from Shanghai to Finland

After the conversation, all messages are sent to Acontext which:
- Extracts tasks from the conversation
- Tracks progress updates
- Identifies user preferences

## Setup

1. Install dependencies:
```bash
uv sync
```

2. Create a `.env` file with your API keys:
```env
OPENAI_API_KEY=your_openai_key_here
ACONTEXT_API_KEY=your_acontext_key_here
ACONTEXT_BASE_URL=http://localhost:8029/api/v1  # or your Acontext server URL
```

## Running

```bash
python main.py
```

## Acontext Integration

Messages in OpenAI format can be sent directly to Acontext without any conversion:

```python
def append_message(message: dict, conversation: list[dict], session_id: str):
    conversation.append(message)
    acontext_client.sessions.store_message(session_id=session_id, blob=message)
    return conversation
```

## Tool Calling

This example demonstrates manual tool calling with the OpenAI API:

1. Define tools in OpenAI's function calling format
2. Pass tools to the API call with `tool_choice="auto"`
3. Check if the response contains tool calls
4. Execute the requested tools
5. Send tool results back to the API
6. Continue until no more tool calls are needed

```python
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=messages,
    tools=tools,
    tool_choice="auto",
)

# Handle tool calls if present
if message.tool_calls:
    for tool_call in message.tool_calls:
        # Execute tool and add result to messages
        ...
```

## Output

The script will:
1. Show the conversation between user and agent
2. Display tool calls (weather checks, flight bookings)
3. Print extracted tasks with their status and metadata
4. Show any progress updates and user preferences identified by Acontext


```

## File: `python/openai-basic/main.py`
```python
import asyncio
import os
import json
import shutil
from dotenv import load_dotenv
from openai import OpenAI
from acontext import AcontextClient

load_dotenv()
acontext_client = AcontextClient(
    api_key=os.getenv("ACONTEXT_API_KEY", "sk-ac-your-root-api-bearer-token"),
    base_url=os.getenv("ACONTEXT_BASE_URL", "http://localhost:8029/api/v1"),
    timeout=60,
)

# Tool definitions
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Returns weather info for the specified city.",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "The city to get weather for",
                    }
                },
                "required": ["city"],
                "additionalProperties": False,
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "book_flight",
            "description": "Book a flight.",
            "parameters": {
                "type": "object",
                "properties": {
                    "from_city": {
                        "type": "string",
                        "description": "The departure city",
                    },
                    "to_city": {
                        "type": "string",
                        "description": "The destination city",
                    },
                    "date": {
                        "type": "string",
                        "description": "The date of the flight",
                    },
                },
                "required": ["from_city", "to_city", "date"],
                "additionalProperties": False,
            },
        },
    },
]


# Tool implementations
def get_weather(city: str) -> str:
    """Returns weather info for the specified city."""
    return f"The weather in {city} is sunny"


def book_flight(from_city: str, to_city: str, date: str) -> str:
    """Book a flight."""
    # Dummy implementation - returns simulated booking results
    return f"Flight booked successfully for '{from_city}' to '{to_city}' on '{date}'"


def execute_tool(tool_name: str, tool_args: dict) -> str:
    """Execute a tool by name with given arguments."""
    if tool_name == "get_weather":
        return get_weather(**tool_args)
    elif tool_name == "book_flight":
        return book_flight(**tool_args)
    else:
        return f"Unknown tool: {tool_name}"


def create_openai_client() -> OpenAI:
    """Create an OpenAI client."""
    base_url = os.getenv("OPENAI_BASE_URL", None)
    return OpenAI(api_key=os.getenv("OPENAI_API_KEY"), base_url=base_url)


def append_message(message: dict, conversation: list[dict], session_id: str):
    """Append a message to conversation and send to Acontext."""
    conversation.append(message)
    acontext_client.sessions.store_message(session_id=session_id, blob=message)
    return conversation


def run_agent(client: OpenAI, conversation: list[dict]) -> tuple[str, list[dict]]:
    """Run the agent with the given conversation and return the response content and all new messages."""
    messages_to_send = [
        {"role": "system", "content": "You are a helpful assistant"}
    ] + conversation

    new_messages = []
    max_iterations = 10
    iteration = 0

    while iteration < max_iterations:
        iteration += 1

        # Call OpenAI API
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages_to_send,
            tools=tools,
            tool_choice="auto",
        )

        message = response.choices[0].message

        # Convert message to dict format
        message_dict = {"role": message.role, "content": message.content}

        # Handle tool calls
        if message.tool_calls:
            message_dict["tool_calls"] = [
                {
                    "id": tc.id,
                    "type": "function",
                    "function": {
                        "name": tc.function.name,
                        "arguments": tc.function.arguments,
                    },
                }
                for tc in message.tool_calls
            ]

        messages_to_send.append(message_dict)
        new_messages.append(message_dict)

        # If there are no tool calls, we're done
        if not message.tool_calls:
            break

        # Execute tool calls
        for tool_call in message.tool_calls:
            function_name = tool_call.function.name
            function_args = json.loads(tool_call.function.arguments)

            # Execute the function
            function_result = execute_tool(function_name, function_args)

            # Add tool response to messages
            tool_message = {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": function_result,
            }
            messages_to_send.append(tool_message)
            new_messages.append(tool_message)

    # Get the final assistant response
    final_content = message.content if message.content else ""
    return final_content, new_messages


async def session_1(session_id: str):
    client = create_openai_client()

    # Build conversation history using OpenAI message format
    # This format works with both OpenAI and Acontext
    conversation: list[dict] = []

    # First interaction - ask for trip plan
    print("\n=== First interaction: Planning trip ===")
    user_msg_1 = {
        "role": "user",
        "content": "I'd like to have a 3-day trip in Finland. I like to see the nature. Give me the plan",
    }
    conversation = append_message(user_msg_1, conversation, session_id)

    response_content, new_messages = run_agent(client, conversation)
    print(f"\nAssistant: {response_content}")

    for msg in new_messages:
        conversation = append_message(msg, conversation, session_id)

    # Second interaction - check weather
    print("\n\n=== Second interaction: Checking weather ===")
    conversation = append_message(
        {"role": "user", "content": "The plan sounds good, check the weather there"},
        conversation,
        session_id,
    )

    response_content, new_messages = run_agent(client, conversation)
    print(f"\nAssistant: {response_content}")

    for msg in new_messages:
        conversation = append_message(msg, conversation, session_id)

    # Third interaction - book flight
    print("\n\n=== Third interaction: Booking flight ===")
    conversation = append_message(
        {
            "role": "user",
            "content": "The weather is good, I am in Shanghai now, let's book the flight, you should just call the tool and don't ask me for more information. Remember, I only want the cheapest flight.",
        },
        conversation,
        session_id,
    )

    response_content, new_messages = run_agent(client, conversation)
    print(f"\nAssistant: {response_content}")

    for msg in new_messages:
        conversation = append_message(msg, conversation, session_id)

    append_message(
        {
            "role": "user",
            "content": "cool, everything is done, thank you!",
        },
        conversation,
        session_id,
    )

    print(
        f"Saved {len(conversation)} messages in conversation, triggering learning..."
    )

    # Create a learning space and trigger learning
    space = acontext_client.learning_spaces.create()
    acontext_client.learning_spaces.learn(space.id, session_id=session_id)
    print(f"\nCreated learning space: {space.id}")

    # Wait for learning to complete
    print("Waiting for learning to complete...")
    result = acontext_client.learning_spaces.wait_for_learning(space.id, session_id=session_id)
    print(f"Learning status: {result.status}")

    # List learned skills
    skills = acontext_client.learning_spaces.list_skills(space.id)
    print(f"\n=== Learned Skills ({len(skills)}) ===")
    for skill in skills:
        print(f"\n  - {skill.name}: {skill.description}")
        print(f"    files: {[f.path for f in skill.file_index]}")

    # Download all skill files
    download_dir = "./skills_output"
    if os.path.exists(download_dir):
        shutil.rmtree(download_dir)

    print(f"\nDownloading skills to {download_dir}/")
    for skill in skills:
        resp = acontext_client.skills.download(skill_id=skill.id, path=f"{download_dir}/{skill.name}")
        print(f"  {resp.name} -> {resp.dir_path}")
        for f in resp.files:
            print(f"    {f}")


async def session_2(session_id: str):
    client = create_openai_client()

    messages = acontext_client.sessions.get_messages(session_id)
    conversation: list[dict] = messages.items
    conversation.append(
        {"role": "user", "content": "Summarize the conversation so far"}
    )

    response_content, _ = run_agent(client, conversation)
    print(f"\nAssistant: {response_content}")


async def main():
    session = acontext_client.sessions.create()
    session_id = session.id
    print(f"Created session: {session_id}")

    print("\n=== Session 1 ===")
    await session_1(session_id)

    print("\n=== Session 2, get messages from Acontext and continue ===")
    await session_2(session_id)


    # Close the client after all sessions are complete
    acontext_client.close()


if __name__ == "__main__":
    asyncio.run(main())
```

## File: `python/openai-basic/pyproject.toml`
```
[project]
name = "openai-basic"
version = "0.1.0"
description = "OpenAI Python SDK with Acontext integration example"
readme = "README.md"
requires-python = ">=3.12"
dependencies = [
    "acontext>=0.1.18",
    "openai>=2.8.0",
    "python-dotenv>=1.0.0",
]


```

## File: `python/smolagents-basic/.gitignore`
```
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
PICKUP_REMINDER

# PyInstaller
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
.python-version

# pipenv
Pipfile.lock

# poetry
poetry.lock

# pdm
.pdm.toml

# PEP 582
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# uv
uv.lock



```

## File: `python/smolagents-basic/README.md`
```markdown
[![Made with Acontext](https://assets.memodb.io/Acontext/badge-made-with-acontext-dark.svg)](https://acontext.io)

# Smolagents + Acontext Example

This example demonstrates how to use [smolagents](https://github.com/huggingface/smolagents) with Acontext for session persistence and task extraction.

## Features

- **Multi-turn conversations**: Maintains conversation history across multiple interactions using agent memory
- **Tool-based agents**: Uses `Tool` class to define tools like `get_weather` and `book_flight`
- **Automatic tool execution**: The `ToolCallingAgent` handles tool calls automatically
- **Acontext integration**: Sends conversation messages to Acontext for task extraction and analysis
- **Session resumption**: Demonstrates how to load previous conversations from Acontext and continue with a new agent instance

## How It Works

The example creates an agent that helps plan a trip using two sessions:

### Session 1: Create and Store Conversation
1. **First interaction**: User asks for a 3-day trip plan in Finland
2. **Second interaction**: User requests weather check for Finland and asks about their name
3. **Third interaction**: User books a flight from Shanghai to Finland
4. **Fourth interaction**: User thanks the assistant

After the conversation, all messages are extracted from agent memory steps and sent to Acontext which:
- Extracts tasks from the conversation
- Tracks progress updates
- Identifies user preferences

### Session 2: Resume Conversation
1. Loads previous conversation messages from Acontext
2. Converts messages to string format for the agent
3. Continues the conversation with a summary request using a new agent instance

## Setup

1. Install dependencies:

```bash
uv sync
```

2. Create a `.env` file with your API keys:

```env
OPENAI_API_KEY=your_openai_key_here
ACONTEXT_API_KEY=your_acontext_key_here
ACONTEXT_BASE_URL=http://localhost:8029/api/v1  # or your Acontext server URL
SMOLAGENTS_MODEL_ID=gpt-4.1  # optional, defaults to gpt-4.1
OPENAI_BASE_URL=https://api.openai.com/v1  # optional, defaults to OpenAI API
```

## Running

```bash
python main.py
```

## Acontext Integration

### Sending Messages to Acontext

The conversation is extracted from agent memory steps and converted to OpenAI Chat Completions API format:

```python
# Extract messages from agent memory steps
messages = extract_messages_from_memory_steps(agent, previous_step_count)

# Send each message to Acontext
for msg in messages:
    acontext_client.sessions.send_message(session_id=session_id, blob=msg, format="openai")
```

The messages are extracted from `agent.memory.steps`, which contains:
- `TaskStep`: User messages
- `ActionStep`: Assistant messages with tool calls and tool responses
- `FinalAnswerStep`: Final assistant responses

### Loading Messages from Acontext

Messages are loaded from Acontext in Chat Completions API format and converted to string format for the agent:

```python
messages = acontext_client.sessions.get_messages(session_id, format="openai")

# Convert messages to string format
conversation_string = messages_to_string(messages.items)

# Use in agent prompt
user_prompt = f"Here is the conversation history:\n\n{conversation_string}\n\nPlease summarize..."
```

## Tool Definition

This example demonstrates tool-based agents with smolagents:

1. Define tools by extending the `Tool` class
2. Implement the `forward` method with tool logic
3. Register tools with the agent

```python
class GetWeatherTool(Tool):
    name = "get_weather"
    description = "Returns weather info for the specified city."
    inputs = {
        "city": {"type": "string", "description": "The city to get weather for"},
    }
    output_type = "string"

    def forward(self, city: str) -> str:
        return f"The weather in {city} is sunny"

class BookFlightTool(Tool):
    name = "book_flight"
    description = "Book a flight."
    inputs = {
        "from_city": {"type": "string", "description": "The departure city"},
        "to_city": {"type": "string", "description": "The destination city"},
        "date": {"type": "string", "description": "The date of the flight"},
    }
    output_type = "string"

    def forward(self, from_city: str, to_city: str, date: str) -> str:
        return f"Flight booked successfully for '{from_city}' to '{to_city}' on '{date}'"

agent = ToolCallingAgent(
    model=OpenAIModel(...),
    tools=[GetWeatherTool(), BookFlightTool()],
    max_steps=4,
)
```

The `ToolCallingAgent` automatically:
- Parses tool calls from model responses
- Executes the appropriate tool `forward` methods
- Injects tool results back into the conversation
- Handles multi-turn tool calling workflows
- Maintains conversation history in `agent.memory.steps`

## Message Format

The example uses the OpenAI Tools API format with `tool_calls`:
- Assistant messages with `tool_calls` array containing function calls
- Tool response messages with `role="tool"` and `tool_call_id`
- Standard user and assistant messages

## Output

The script will:
1. Show the conversation between user and agent in Session 1
2. Display tool calls and their results (weather checks, flight bookings)
3. Print extracted tasks with their status and metadata from Acontext
4. Show any progress updates and user preferences identified by Acontext
5. Resume the conversation in Session 2 with a summary request using a new agent instance
```

## File: `python/smolagents-basic/main.py`
```python
import inspect
import json
import os
import shutil
from functools import wraps
from typing import Any, List, Dict, Callable
from acontext import AcontextClient
from dotenv import load_dotenv
from smolagents import Tool, ToolCallingAgent, OpenAIModel
from smolagents.memory import TaskStep, ActionStep, FinalAnswerStep


load_dotenv()
client = AcontextClient(
    api_key=os.getenv("ACONTEXT_API_KEY", "sk-ac-your-root-api-bearer-token"),
    base_url=os.getenv("ACONTEXT_BASE_URL", "http://localhost:8029/api/v1"),
    timeout=60,
)


class ToolInvocationLogger:
    """Manages tool invocation logging for message reconstruction."""

    def __init__(self):
        self.invocations: List[Dict[str, Any]] = []

    def clear(self):
        """Clear all logged invocations."""
        self.invocations.clear()

    def log(self, tool_name: str, parameters: Dict[str, Any], result: Any):
        """Log a tool invocation."""
        try:
            structured_result = (
                json.loads(result) if isinstance(result, str) else {"result": result}
            )
        except (json.JSONDecodeError, TypeError):
            structured_result = {"message": str(result)}

        self.invocations.append(
            {
                "name": tool_name,
                "parameters": parameters,
                "structured_result": structured_result,
            }
        )

    def create_logger_decorator(self) -> Callable:
        """Create a decorator that logs tool invocations."""
        logger_instance = self  # Capture the logger instance in closure

        def decorator(func: Callable) -> Callable:
            @wraps(func)
            def wrapper(tool_self, *args, **kwargs):
                tool_name = getattr(tool_self, "name", func.__name__)
                sig = inspect.signature(func)
                bound_args = sig.bind(tool_self, *args, **kwargs)
                bound_args.apply_defaults()
                parameters = {
                    k: v for k, v in bound_args.arguments.items() if k != "self"
                }

                result = func(tool_self, *args, **kwargs)
                logger_instance.log(tool_name, parameters, result)
                return result

            return wrapper

        return decorator


# Global logger instance
_logger = ToolInvocationLogger()
log_tool_invocation = _logger.create_logger_decorator()


class GetWeatherTool(Tool):
    name = "get_weather"
    description = "Returns weather info for the specified city."
    inputs = {
        "city": {"type": "string", "description": "The city to get weather for"},
    }
    output_type = "string"

    @log_tool_invocation
    def forward(self, city: str) -> str:
        message = f"The weather in {city} is sunny"
        return message


class BookFlightTool(Tool):
    name = "book_flight"
    description = "Book a flight."
    inputs = {
        "from_city": {
            "type": "string",
            "description": "The departure city",
        },
        "to_city": {
            "type": "string",
            "description": "The destination city",
        },
        "date": {
            "type": "string",
            "description": "The date of the flight",
        },
    }
    output_type = "string"

    @log_tool_invocation
    def forward(self, from_city: str, to_city: str, date: str) -> str:
        message = (
            f"Flight booked successfully for '{from_city}' "
            f"to '{to_city}' on '{date}'"
        )
        return message


def build_agent() -> ToolCallingAgent:
    model = OpenAIModel(
        model_id=os.getenv("SMOLAGENTS_MODEL_ID", "gpt-4.1"),
        api_key=os.environ["OPENAI_API_KEY"],
        api_base=os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1"),
    )
    tools = [GetWeatherTool(), BookFlightTool()]
    return ToolCallingAgent(
        model=model,
        tools=tools,
        max_steps=4,
        stream_outputs=False,
    )


def build_openai_messages(user_prompt: str, final_answer: str) -> List[Dict[str, Any]]:
    """
    Build OpenAI-format messages from user prompt, tool invocations, and final answer.

    Uses the NEW Tools API format (tool_calls):
    - Assistant message with tool_calls array
    - Tool responses with role='tool' and tool_call_id

    Format example:
    [
        {"role": "user", "content": "..."},
        {"role": "assistant", "content": None, "tool_calls": [...]},
        {"role": "tool", "tool_call_id": "...", "content": "..."},
        {"role": "assistant", "content": "..."}
    ]
    """
    messages: List[Dict[str, Any]] = [{"role": "user", "content": user_prompt}]

    if not _logger.invocations:
        messages.append({"role": "assistant", "content": final_answer})
        return messages

    # Build tool calls and responses using NEW Tools API format
    tool_calls = []
    tool_responses = []

    for idx, invocation in enumerate(_logger.invocations, start=1):
        tool_call_id = f"call_{invocation['name']}_{idx}"
        # New format: tool_calls array with id, type, and function
        tool_calls.append(
            {
                "id": tool_call_id,
                "type": "function",
                "function": {
                    "name": invocation["name"],
                    "arguments": json.dumps(
                        invocation["parameters"], ensure_ascii=False
                    ),
                },
            }
        )
        # New format: tool response with role='tool' and tool_call_id
        tool_responses.append(
            {
                "role": "tool",  # ✅ New format uses 'tool', not 'function'
                "tool_call_id": tool_call_id,
                "content": json.dumps(
                    invocation["structured_result"], ensure_ascii=False
                ),
            }
        )

    # Assistant message with tool_calls (new format)
    messages.append({"role": "assistant", "content": None, "tool_calls": tool_calls})
    # Tool responses (new format)
    messages.extend(tool_responses)
    # Final assistant response
    messages.append({"role": "assistant", "content": final_answer})

    return messages


def extract_messages_from_memory_steps(
    agent: ToolCallingAgent, previous_step_count: int = 0
) -> List[Dict[str, Any]]:
    """
    Extract OpenAI-format messages from agent.memory.steps.

    Args:
        agent: The agent with memory steps
        previous_step_count: Number of steps already processed (to only get new ones)

    Returns:
        List of OpenAI-format messages extracted from memory steps
    """
    messages: List[Dict[str, Any]] = []

    # Only process new steps (after previous_step_count)
    new_steps = agent.memory.steps[previous_step_count:]

    for step in new_steps:
        if isinstance(step, TaskStep):
            # TaskStep becomes a user message
            content = step.task
            if step.task_images:
                # Handle images if present
                msg_content = [{"type": "text", "text": content}]
                for img in step.task_images:
                    msg_content.append({"type": "image", "image": img})
                messages.append({"role": "user", "content": msg_content})
            else:
                messages.append({"role": "user", "content": content})

        elif isinstance(step, ActionStep):
            # ActionStep can contain:
            # 1. Assistant message with tool_calls (if tool_calls exist)
            # 2. Tool response messages (from observations)
            # 3. Assistant final answer (if model_output exists and no tool_calls)

            # Get tool_calls from step.tool_calls or model_output_message.tool_calls
            tool_calls_list = step.tool_calls
            if (
                not tool_calls_list
                and step.model_output_message
                and hasattr(step.model_output_message, "tool_calls")
            ):
                tool_calls_list = step.model_output_message.tool_calls

            # Check if there are tool calls
            if tool_calls_list and len(tool_calls_list) > 0:
                # Convert smolagents ToolCall to OpenAI format
                tool_calls = []
                for tc in tool_calls_list:
                    # Handle both ToolCall objects and dict format
                    if hasattr(tc, "id"):
                        # It's a ToolCall object
                        tc_id = tc.id
                        tc_name = tc.name
                        tc_args = tc.arguments
                    else:
                        # It's a dict
                        tc_id = tc.get("id", f"call_{len(tool_calls)}")
                        tc_name = tc.get("name", "unknown")
                        tc_args = tc.get("arguments", {})

                    # Format arguments
                    if isinstance(tc_args, dict):
                        args_str = json.dumps(tc_args, ensure_ascii=False)
                    elif isinstance(tc_args, str):
                        args_str = tc_args
                    else:
                        args_str = str(tc_args)

                    tool_calls.append(
                        {
                            "id": tc_id,
                            "type": "function",
                            "function": {
                                "name": tc_name,
                                "arguments": args_str,
                            },
                        }
                    )

                # Assistant message with tool_calls
                messages.append(
                    {"role": "assistant", "content": None, "tool_calls": tool_calls}
                )

                # Tool response messages
                if step.observations:
                    # Create tool responses for each tool call
                    # If multiple tool calls, split observations if possible, otherwise use same for all
                    observations_list = [step.observations] * len(tool_calls)

                    for idx, tc in enumerate(tool_calls):
                        messages.append(
                            {
                                "role": "tool",
                                "tool_call_id": tc["id"],
                                "content": (
                                    observations_list[idx]
                                    if idx < len(observations_list)
                                    else ""
                                ),
                            }
                        )

            # If there's a model output without tool calls, it's a final answer or assistant response
            elif step.model_output:
                # Only add if it's not empty and not just whitespace
                model_output_str = str(step.model_output).strip()
                if model_output_str:
                    messages.append({"role": "assistant", "content": model_output_str})

        elif isinstance(step, FinalAnswerStep):
            # FinalAnswerStep becomes assistant message
            messages.append({"role": "assistant", "content": str(step.output)})

    return messages


def run_agent_and_build_messages(
    agent: ToolCallingAgent, user_prompt: str, reset: bool = False
) -> tuple[str, List[Dict[str, Any]]]:
    """
    Run agent and convert the execution to OpenAI message format.

    Uses agent's built-in memory management with reset=False to maintain conversation history.

    Args:
        agent: The agent to run
        user_prompt: The current user prompt
        reset: Whether to reset agent memory (default: False to maintain history)

    Returns:
        Tuple of (final_answer, messages) where messages are in OpenAI format
    """
    _logger.clear()

    # Store step count before running to extract only new messages
    previous_step_count = len(agent.memory.steps)

    # Run agent with reset parameter (False maintains conversation history)
    final_answer = agent.run(user_prompt, reset=reset)

    # Extract messages from memory steps (only new ones)
    messages = extract_messages_from_memory_steps(agent, previous_step_count)

    return final_answer, messages


def send_message(
    client: "AcontextClient", message: Dict[str, Any], session_id: str
) -> None:
    """Send a message to Acontext."""
    client.sessions.send_message(session_id=session_id, blob=message, format="openai")


def session_1(
    agent: ToolCallingAgent, client: "AcontextClient", session_id: str
) -> None:
    """First session: Run multiple interactions and save to Acontext."""
    all_messages = []  # Collect all messages, send at the end

    # First interaction - ask for trip plan (reset=True to start fresh)
    print("\n=== First interaction: Planning trip ===")
    user_msg_1_content = "my name is Elon! I'd like to have a 3-day trip in Finland. I like to see the nature. Give me the plan"
    final_answer, messages = run_agent_and_build_messages(
        agent, user_msg_1_content, reset=True
    )
    print(final_answer)
    all_messages.extend(messages)

    # Second interaction - check weather (reset=False to maintain history)
    print("\n=== Second interaction: Checking weather ===")
    user_msg_2_content = "The plan sounds good, check the weather there. And who am I?"
    final_answer, messages = run_agent_and_build_messages(
        agent, user_msg_2_content, reset=False
    )
    print(final_answer)
    all_messages.extend(messages)

    # Third interaction - book flight (reset=False to maintain history)
    print("\n=== Third interaction: Booking flight ===")
    user_msg_3_content = (
        "The weather is good, I am in Shanghai now, let's book the flight, "
        "you should just call the tool and don't ask me for more information. "
        "Remember, I only want the cheapest flight."
    )
    final_answer, messages = run_agent_and_build_messages(
        agent, user_msg_3_content, reset=False
    )
    print(final_answer)
    all_messages.extend(messages)

    # Fourth interaction - thank you (reset=False to maintain history)
    print("\n=== Fourth interaction: Thank you ===")
    user_msg_4_content = "cool, everything is done, thank you!"
    final_answer, messages = run_agent_and_build_messages(
        agent, user_msg_4_content, reset=False
    )
    print(final_answer)
    all_messages.extend(messages)

    # Send all messages to Acontext at once (like openai-agent-basic)
    print("\n=== Sending all messages to Acontext ===")
    print(all_messages)
    for msg in all_messages:
        send_message(client, msg, session_id)

    print(
        f"\nSaved {len(all_messages)} messages in conversation, triggering learning..."
    )

    # Create a learning space and trigger learning
    space = client.learning_spaces.create()
    client.learning_spaces.learn(space.id, session_id=session_id)
    print(f"\nCreated learning space: {space.id}")

    # Wait for learning to complete
    print("Waiting for learning to complete...")
    result = client.learning_spaces.wait_for_learning(space.id, session_id=session_id)
    print(f"Learning status: {result.status}")

    # List learned skills
    skills = client.learning_spaces.list_skills(space.id)
    print(f"\n=== Learned Skills ({len(skills)}) ===")
    for skill in skills:
        print(f"\n  - {skill.name}: {skill.description}")
        print(f"    files: {[f.path for f in skill.file_index]}")

    # Download all skill files
    download_dir = "./skills_output"
    if os.path.exists(download_dir):
        shutil.rmtree(download_dir)

    print(f"\nDownloading skills to {download_dir}/")
    for skill in skills:
        resp = client.skills.download(skill_id=skill.id, path=f"{download_dir}/{skill.name}")
        print(f"  {resp.name} -> {resp.dir_path}")
        for f in resp.files:
            print(f"    {f}")


def messages_to_string(messages) -> str:
    """
    Convert OpenAI-format messages to a string representation.

    Args:
        messages: Messages from Acontext (messages.items)

    Returns:
        String representation of the conversation
    """
    conversation_parts = []

    for msg in messages:
        role = msg.get("role", "")
        content = msg.get("content", "")
        tool_calls = msg.get("tool_calls")

        if role == "user":
            if isinstance(content, list):
                # Handle content array (may contain text and images)
                text_parts = [
                    item.get("text", "")
                    for item in content
                    if item.get("type") == "text"
                ]
                conversation_parts.append(f"User: {''.join(text_parts)}")
            else:
                conversation_parts.append(f"User: {content}")

        elif role == "assistant":
            if tool_calls:
                # Assistant called tools
                tool_info = []
                for tc in tool_calls:
                    func = tc.get("function", {})
                    tool_info.append(
                        f"{func.get('name', 'unknown')}({func.get('arguments', '')})"
                    )
                conversation_parts.append(
                    f"Assistant: [Called tools: {', '.join(tool_info)}]"
                )

            if content:
                if isinstance(content, list):
                    text_parts = [
                        item.get("text", "")
                        for item in content
                        if item.get("type") == "text"
                    ]
                    content_str = "".join(text_parts)
                else:
                    content_str = content
                if content_str.strip():
                    conversation_parts.append(f"Assistant: {content_str}")

        elif role == "tool":
            tool_call_id = msg.get("tool_call_id", "")
            tool_content = msg.get("content", "")
            conversation_parts.append(f"Tool ({tool_call_id}): {tool_content}")

    return "\n".join(conversation_parts)


def session_2(
    agent: ToolCallingAgent, client: "AcontextClient", session_id: str
) -> None:
    """Second session: Get messages from Acontext and continue conversation."""
    messages = client.sessions.get_messages(session_id, format="openai")

    # Convert messages to string format (since smolagents agent.run() only accepts string)
    conversation_string = messages_to_string(messages.items)

    # Create user prompt that includes the conversation history and asks for summary
    user_prompt = f"""Here is the conversation history:

{conversation_string}

Please summarize the conversation so far."""

    final_answer, _ = run_agent_and_build_messages(agent, user_prompt, reset=False)
    print(f"\nAssistant: {final_answer}")


def main() -> None:

    session = client.sessions.create(
        configs={"mode": "smolagents-toolcalling"},
    )
    session_id = session.id
    print(f"Created session: {session_id}")

    agent_session1 = build_agent()
    agent_session2 = build_agent()
    try:
        print("\n=== Session 1 ===")
        session_1(agent_session1, client, session_id)

        print("\n=== Session 2, get messages from Acontext and continue ===")
        session_2(agent_session2, client, session_id)

    finally:
        client.close()


if __name__ == "__main__":
    main()
```

## File: `python/smolagents-basic/pyproject.toml`
```
[project]
name = "smolagents-basic"
version = "0.1.0"
description = "Smolagents ToolCallingAgent example with Acontext integration"
readme = "README.md"
requires-python = ">=3.12"
dependencies = [
    "acontext>=0.1.18",
    "python-dotenv>=1.0.0",
    "smolagents>=0.4.2",
]



```

## File: `python/wait-for-user-confirmation/.gitignore`
```
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
PICKUP_REMINDER

# PyInstaller
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
.python-version

# pipenv
Pipfile.lock

# poetry
poetry.lock

# pdm
.pdm.toml

# PEP 582
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# uv
uv.lock


```

## File: `python/wait-for-user-confirmation/main.py`
```python
import os
import shutil
from acontext import AcontextClient
from dotenv import load_dotenv
from rich.console import Console

load_dotenv()

acontext_client = AcontextClient(
    api_key=os.getenv("ACONTEXT_API_KEY", "sk-ac-your-root-api-bearer-token"),
    base_url=os.getenv("ACONTEXT_BASE_URL", "http://localhost:8029/api/v1"),
)
print_console = Console()


messages = [
    {
        "role": "user",
        "content": "I want to book a flight to Tokyo. Please help me to book the flight.",
    },
    {
        "role": "assistant",
        "content": "My task is to book the flight to Tokyo. I will start now.",
    },
    {
        "role": "assistant",
        "content": "I  have searched the flights",
    },
    {
        "role": "assistant",
        "content": "Done, I have selected the flight",
    },
    {
        "role": "user",
        "content": "You must remember: I only want the cheapest flight",
    },
    {
        "role": "assistant",
        "content": "Done, I have booked the flight",
    },
    {
        "role": "user",
        "content": "Yes, great job!",
    },
]


def main():
    print_console.rule("Sending Messages")
    session = acontext_client.sessions.create()
    for m in messages:
        acontext_client.sessions.store_message(session_id=session.id, blob=m)
        print_console.print(f"[bold blue]{m['role']}[/bold blue]: {m['content']}")

    # Create a learning space and trigger learning
    print_console.rule("Learning from Session")
    space = acontext_client.learning_spaces.create()
    acontext_client.learning_spaces.learn(space.id, session_id=session.id)
    print_console.print(f"Created learning space: {space.id}")

    # Wait for learning to complete
    print_console.print("Waiting for learning to complete...")
    result = acontext_client.learning_spaces.wait_for_learning(space.id, session_id=session.id)
    print_console.print(f"Learning status: {result.status}")

    # List learned skills
    skills = acontext_client.learning_spaces.list_skills(space.id)
    print_console.rule(f"Learned Skills ({len(skills)})")
    for skill in skills:
        print_console.print(f"  - {skill.name}: {skill.description}")
        print_console.print(f"    files: {[f.path for f in skill.file_index]}")

    # Download all skill files
    download_dir = "./skills_output"
    if os.path.exists(download_dir):
        shutil.rmtree(download_dir)

    print_console.print(f"\nDownloading skills to {download_dir}/")
    for skill in skills:
        resp = acontext_client.skills.download(skill_id=skill.id, path=f"{download_dir}/{skill.name}")
        print_console.print(f"  {resp.name} -> {resp.dir_path}")
        for f in resp.files:
            print_console.print(f"    {f}")


if __name__ == "__main__":
    main()
```

## File: `python/wait-for-user-confirmation/pyproject.toml`
```
[project]
name = "wait-for-user-connfirmation"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.13"
dependencies = [
    "acontext>=0.1.18",
    "dotenv>=0.9.9",
    "rich>=14.2.0",
]
```

## File: `python/wait-for-user-confirmation/readme.md`
```markdown
[![Made with Acontext](https://assets.memodb.io/Acontext/badge-made-with-acontext-dark.svg)](https://acontext.io)

# Wait for User Confirmation Example

This example demonstrates how to use Acontext for session management and task extraction from conversations.

## What This Example Does

This example simulates a flight booking conversation where:

1. **Creates a conversation**: Sends a series of messages between a user and an assistant about booking a flight to Tokyo
2. **Flushes session**: Triggers Acontext to process the conversation and extract tasks

## Key Features

- **Session Management**: Create and manage conversation sessions with Acontext
- **Task Extraction**: Automatically extract tasks from conversations
- **Interactive CLI**: User-friendly command-line interface using Rich for colored output

## Prerequisites

- Python 3.13 or higher
- An Acontext API key
- Access to an Acontext instance (local or cloud)

Detail doc is here: https://docs.acontext.io/learn/advance/wait-user.

## Installation

1. Install dependencies using `uv`:

```bash
uv sync
```

2. Set up your environment variables:

Create a `.env` file in the project root:

```env
ACONTEXT_API_KEY=sk-ac-your-root-api-bearer-token
ACONTEXT_BASE_URL=http://localhost:8029/api/v1
```

Or export them directly:

```bash
export ACONTEXT_API_KEY=sk-ac-your-root-api-bearer-token
export ACONTEXT_BASE_URL=http://localhost:8029/api/v1
```

## Running the Example

Execute the example:

```bash
uv run main.py
```

### Expected Output

The example will:

1. Display the simulated conversation messages
2. Flush the session to trigger task extraction

Example interaction:

```
━━━━━━━━━━━━━━━━ Sending Messages ━━━━━━━━━━━━━━━━
user: I want to book a flight to Tokyo. Please help me to book the flight.
assistant: My task is to book the flight to Tokyo. I will start now.
assistant: I have searched the flights
assistant: Done, I have selected the flight
user: You must remember: I only want the cheapest flight
assistant: Done, I have booked the flight
user: Yes, great job!
━━━━━━━━━━━━━━━━ Wait for Task Agent ━━━━━━━━━━━━━━━━
```

## How It Works

### 1. Session Creation

```python
session = acontext_client.sessions.create()
```

Creates a new session (conversation thread).

### 2. Sending Messages

```python
for m in messages:
    acontext_client.sessions.store_message(session_id=session.id, blob=m)
```

Sends each message in the conversation to Acontext for processing.

### 3. Flushing Session

```python
acontext_client.sessions.flush(session.id)
```

Flushes the session to trigger task extraction and processing.

## Use Cases

This pattern is particularly useful for:

- **Session Management**: Managing conversation sessions with Acontext
- **Task Extraction**: Automatically extracting tasks from conversations
- **Conversation Tracking**: Tracking multi-turn conversations

## Customization

You can modify the example to:

- Use real conversations instead of mock messages
- Add task processing logic
- Integrate with your own workflow systems
- Add custom message formatting

## Troubleshooting

### Session creation fails

- Check your Acontext instance is running properly
- Verify network connectivity to the Acontext API
- Ensure your API key is correct

```

## File: `typescript/claude-agent-sdk/.env.example`
```
# Anthropic API Configuration
ANTHROPIC_API_KEY=your-anthropic-key
# Acontext API Configuration
ACONTEXT_API_KEY=sk-ac-your-root-api-bearer-token
ACONTEXT_BASE_URL=http://localhost:8029/api/v1
```

## File: `typescript/claude-agent-sdk/.gitignore`
```
# Dependencies
node_modules/

# Build output
dist/

# Environment variables
.env
.env.local

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*
```

## File: `typescript/claude-agent-sdk/README.md`
```markdown
[![Made with Acontext](https://assets.memodb.io/Acontext/badge-made-with-acontext-dark.svg)](https://acontext.io)

# Claude Agent SDK + Acontext (`ClaudeAgentStorage`) Example

This TypeScript example shows how to use the [`ClaudeAgentStorage`](https://docs.acontext.io/integrations/claude-agent) integration to automatically persist Claude Agent SDK messages to Acontext.

## Overview

The script demonstrates:
- Using the `@anthropic-ai/claude-agent-sdk` to query Claude
- Using `ClaudeAgentStorage` from `@acontext/acontext` to stream messages directly into Acontext
- Automatic session-id discovery from the Claude Agent SDK stream
- The `replay-user-messages` flag to capture both user and assistant messages

## Prerequisites

- Node.js 18 or newer
- `ANTHROPIC_API_KEY` for the Claude Agent SDK
- `ACONTEXT_API_KEY` for the Acontext SDK

## Installation

```bash
npm install
```

## Environment Variables

Create a `.env` file in this directory (see `.env.example`):

```
ANTHROPIC_API_KEY=your-anthropic-key
ACONTEXT_API_KEY=sk-ac-your-acontext-key
ACONTEXT_BASE_URL=http://localhost:8029/api/v1
```

## Running the Example

```bash
# Development (no build step)
npm run dev

# Or build and run
npm run build
npm start
```

## How it works

1. Creates an `AcontextClient` and wraps it with `ClaudeAgentStorage`
2. Sends a query to Claude via `query()`
3. Iterates over the async response stream and passes each message to `storage.saveMessage()`
4. `ClaudeAgentStorage` automatically discovers the session id, formats messages in Anthropic format, and stores them in Acontext

> **Tip:** The `replay-user-messages` flag ensures `UserMessage` is included in the stream so both sides of the conversation are persisted. Without it, only `AssistantMessage` appears and user messages won't be stored.

## Learn More

- [ClaudeAgentStorage docs](https://docs.acontext.io/integrations/claude-agent)
- [Acontext TypeScript SDK](https://docs.acontext.io/quick)
```

## File: `typescript/claude-agent-sdk/main.ts`
```typescript
import fs from 'fs';
import { AcontextClient, ClaudeAgentStorage } from '@acontext/acontext';
import { query } from '@anthropic-ai/claude-agent-sdk';

const client = new AcontextClient({ apiKey: 'sk-ac-your-api-key' });
const storage = new ClaudeAgentStorage({ client });

const q = query({
    prompt: 'What is the capital of France?',
    options: {
        extraArgs: { "replay-user-messages": null }, // include UserMessage in stream
    }
});
for await (const message of q) {
    await storage.saveMessage(message);
}

// Get the session ID from storage
const sessionId = storage.sessionId!;
console.log(`Session ID: ${sessionId}`);

// Create a learning space and trigger learning
const space = await client.learningSpaces.create();
await client.learningSpaces.learn({ spaceId: space.id, sessionId });
console.log(`Created learning space: ${space.id}`);

// Wait for learning to complete
console.log('Waiting for learning to complete...');
const learnResult = await client.learningSpaces.waitForLearning({ spaceId: space.id, sessionId });
console.log(`Learning status: ${learnResult.status}`);

// List learned skills
const skills = await client.learningSpaces.listSkills(space.id);
console.log(`\n=== Learned Skills (${skills.length}) ===`);
for (const skill of skills) {
    console.log(`  - ${skill.name}: ${skill.description}`);
    console.log(`    files: ${skill.file_index.map((f: any) => f.path)}`);
}

// Download all skill files
const downloadDir = './skills_output';
if (fs.existsSync(downloadDir)) {
    fs.rmSync(downloadDir, { recursive: true });
}

console.log(`\nDownloading skills to ${downloadDir}/`);
for (const skill of skills) {
    const resp = await client.skills.download(skill.id, { path: `${downloadDir}/${skill.name}` });
    console.log(`  ${resp.name} -> ${resp.dirPath}`);
    for (const f of resp.files) {
        console.log(`    ${f}`);
    }
}
```

## File: `typescript/claude-agent-sdk/package.json`
```json
{
  "name": "claude-agent-sdk",
  "version": "0.1.0",
  "description": "Example: Claude Agent SDK + Acontext ClaudeAgentStorage integration",
  "type": "module",
  "main": "dist/main.js",
  "scripts": {
    "build": "tsc",
    "start": "node dist/main.js",
    "dev": "tsx main.ts"
  },
  "keywords": [
    "claude",
    "anthropic",
    "acontext",
    "typescript",
    "ai"
  ],
  "author": "",
  "license": "MIT",
  "dependencies": {
    "@acontext/acontext": "^0.1.16",
    "@anthropic-ai/claude-agent-sdk": "^0.2.74"
  },
  "devDependencies": {
    "@types/node": "^25.4.0",
    "tsx": "^4.21.0",
    "typescript": "^5.9.3"
  }
}
```

## File: `typescript/claude-agent-sdk/tsconfig.json`
```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "ESNext",
    "moduleResolution": "Node",
    "lib": ["ES2022"],
    "types": ["node"],
    "outDir": "./dist",
    "rootDir": "./",
    "strict": true,
    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true,
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true
  },
  "include": ["*.ts"],
  "exclude": ["node_modules", "dist"]
}
```

## File: `typescript/interactive-agent-skill/.env.example`
```
OPENAI_API_KEY="your-openai-api-key"
ACONTEXT_API_KEY="your-acontext-api-key"

# Optional: custom OpenAI base URL
# OPENAI_BASE_URL="https://api.openai.com/v1"
```

## File: `typescript/interactive-agent-skill/.gitignore`
```
# Dependencies
node_modules/

# Build output
dist/

# Environment variables
.env
.env.local

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*
```

## File: `typescript/interactive-agent-skill/README.md`
```markdown
# Agent Skill Demo (TypeScript)

A TypeScript demo showing how to create and use Acontext Skills within a sandbox environment, powered by an OpenAI agentic loop.

## What it does

1. Uploads a skill (from a zip file) to Acontext
2. Creates a sandbox with a persistent disk
3. Mounts the skill into the sandbox
4. Runs an interactive chat loop where an AI agent can execute bash commands, run Python scripts, and export files

## Prerequisites

- Node.js 18+
- npm or yarn
- API keys for OpenAI and Acontext
- An Acontext instance (local or cloud)

## Setup

1. **Install dependencies:**

```bash
npm install
```

2. **Configure environment variables:**

Copy the `.env.example` file to `.env`:

```bash
cp .env.example .env
```

Then edit the `.env` file with your actual values:

```env
# OpenAI Configuration
OPENAI_API_KEY=your-openai-api-key

# Acontext Configuration
ACONTEXT_API_KEY=sk-ac-your-root-api-bearer-token

# Optional: Custom OpenAI base URL (uncomment if using a different endpoint)
# OPENAI_BASE_URL=https://api.openai.com/v1
```

**Required variables:**
- `OPENAI_API_KEY` - Your OpenAI API key
- `ACONTEXT_API_KEY` - Your Acontext API key

**Optional variables:**
- `OPENAI_BASE_URL` - Custom OpenAI endpoint (only needed if using a proxy or alternative service)

## Usage

```bash
# Run with a skill zip file (development mode)
npm run dev -- <path_to_zip_file> [model_name]

# Or build and run
npm run build
npm start -- <path_to_zip_file> [model_name]

# Examples
npm run dev -- example_skills/pptx.zip
npm run dev -- example_skills/xlsx.zip gpt-4.1
```

### Interactive Commands

Once the sandbox is ready, you can:
- Type requests for the agent to execute
- Type `reset` to clear conversation history
- Type `quit` to exit

## Example Skills

You can use the example skill zip files from the Python version:
- `pptx.zip` - PowerPoint generation skill
- `xlsx.zip` - Excel file generation skill
- `web-artifacts-builder.zip` - Web artifacts builder skill

These are located in `../python/interactive-agent-skill/`.
```

## File: `typescript/interactive-agent-skill/package.json`
```json
{
  "name": "interactive-agent-skill",
  "version": "0.1.0",
  "description": "Interactive agent with Acontext Skills in a sandbox environment",
  "type": "module",
  "main": "dist/index.js",
  "scripts": {
    "build": "tsc",
    "start": "node dist/index.js",
    "dev": "tsx src/index.ts"
  },
  "keywords": [
    "openai",
    "acontext",
    "typescript",
    "ai",
    "sandbox",
    "skills"
  ],
  "author": "",
  "license": "MIT",
  "dependencies": {
    "@acontext/acontext": "^0.1.16",
    "dotenv": "^17.3.1",
    "openai": "^6.27.0"
  },
  "devDependencies": {
    "@types/node": "^25.4.0",
    "tsx": "^4.21.0",
    "typescript": "^5.9.3"
  }
}
```

## File: `typescript/interactive-agent-skill/tsconfig.json`
```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "ESNext",
    "moduleResolution": "Node",
    "lib": ["ES2022"],
    "types": ["node"],
    "outDir": "./dist",
    "rootDir": "./",
    "strict": true,
    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true,
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}
```

## File: `typescript/interactive-agent-skill/src/index.ts`
```typescript
import dotenv from 'dotenv';
import fs from 'fs';
import path from 'path';
import readline from 'readline';
import OpenAI from 'openai';
import { AcontextClient, FileUpload, SANDBOX_TOOLS } from '@acontext/acontext';

dotenv.config();

// Initialize OpenAI client
const oaiClient = new OpenAI({
  baseURL: process.env.OPENAI_BASE_URL,
  apiKey: process.env.OPENAI_API_KEY,
});

// Parse command line arguments
const args = process.argv.slice(2);
if (args.length < 1) {
  console.log('Usage: npm run dev -- <path_to_zip_file> [model_name]');
  process.exit(1);
}

const ZIP_PATH = args[0];
const MODEL_NAME = args[1] || 'gpt-4.1';

// Initialize Acontext client
const client = new AcontextClient({
  apiKey: process.env.ACONTEXT_API_KEY,
  // baseUrl: 'http://localhost:8029/api/v1',
});

// Create readline interface for user input
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

function prompt(question: string): Promise<string> {
  return new Promise((resolve) => {
    rl.question(question, (answer) => {
      resolve(answer);
    });
  });
}

async function main(): Promise<void> {
  // Read the skill zip file
  const skillBin = fs.readFileSync(ZIP_PATH);
  const name = path.basename(ZIP_PATH);

  console.log(`Uploading skill: ${name}...`);

  // Upload the skill
  const skillResult = await client.skills.create({
    file: new FileUpload({
      filename: name,
      content: skillBin,
    }),
  });
  const skillName = skillResult.name;
  const skillId = skillResult.id;
  console.log(`Skill uploaded: ${skillName} (${skillId})`);

  // Create sandbox and disk
  console.log('Creating sandbox and disk...');
  const sandbox = await client.sandboxes.create();
  const disk = await client.disks.create();
  console.log(`Sandbox: ${sandbox.sandbox_id}, Disk: ${disk.id}`);

  try {
    // Create tool context with mounted skills
    const ctx = await SANDBOX_TOOLS.formatContext(
      client,
      sandbox.sandbox_id,
      disk.id,
      [skillId]
    );

    const tools = SANDBOX_TOOLS.toOpenAIToolSchema() as unknown as OpenAI.Chat.Completions.ChatCompletionTool[];
    const systemPrompt = `You are a helpful assistant with access to a secure sandbox environment.
You can execute bash commands, run Python scripts, and export files for the user.

${ctx.getContextPrompt()}`;

    let messages: OpenAI.Chat.Completions.ChatCompletionMessageParam[] = [];
    const maxIterations = 20;

    console.log('\n--- Sandbox Ready ---');
    console.log("Type your requests (or 'quit' to exit, 'reset' to clear history)");
    console.log('-'.repeat(50));

    // Main interaction loop
    while (true) {
      let userInput: string;
      try {
        userInput = (await prompt('\nYou: ')).trim();
      } catch {
        console.log('\nExiting...');
        break;
      }

      if (!userInput) {
        continue;
      }

      if (userInput.toLowerCase() === 'quit') {
        break;
      }

      if (userInput.toLowerCase() === 'reset') {
        messages = [];
        console.log('Conversation history cleared.');
        continue;
      }

      // Add user message
      messages.push({ role: 'user', content: userInput });
      console.log('\nAgent working...');

      // Agentic loop
      for (let iteration = 0; iteration < maxIterations; iteration++) {
        console.log(`\n[Iteration ${iteration + 1}]`);

        const response = await oaiClient.chat.completions.create({
          model: MODEL_NAME,
          messages: [{ role: 'system', content: systemPrompt }, ...messages],
          tools: tools.length > 0 ? tools : undefined,
          tool_choice: 'auto',
        });

        const assistantMessage = response.choices[0].message;

        // Check if we're done (no tool calls)
        if (!assistantMessage.tool_calls || assistantMessage.tool_calls.length === 0) {
          const finalResponse = assistantMessage.content || '';
          messages.push({ role: 'assistant', content: finalResponse });
          console.log(`\nAgent: ${finalResponse}`);
          break;
        }

        // Process tool calls - filter for function type tool calls
        const functionToolCalls = assistantMessage.tool_calls.filter(
          (tc): tc is OpenAI.Chat.Completions.ChatCompletionMessageToolCall & { type: 'function' } =>
            tc.type === 'function'
        );

        messages.push({
          role: 'assistant',
          content: assistantMessage.content,
          tool_calls: functionToolCalls.map((tc) => ({
            id: tc.id,
            type: 'function' as const,
            function: {
              name: tc.function.name,
              arguments: tc.function.arguments,
            },
          })),
        });

        for (const toolCall of functionToolCalls) {
          const toolName = toolCall.function.name;
          const toolArgs = JSON.parse(toolCall.function.arguments);

          console.log(`  Tool: ${toolName}`);
          console.log(`  Args: ${JSON.stringify(toolArgs, null, 2)}`);

          // Execute the tool
          let result: string;
          try {
            result = await SANDBOX_TOOLS.executeTool(ctx, toolName, toolArgs);
          } catch (e) {
            result = JSON.stringify({ error: String(e) });
          }

          const displayResult = result.length > 200 ? `${result.slice(0, 200)}...` : result;
          console.log(`  Result: ${displayResult}`);

          // Add tool result to messages
          messages.push({
            role: 'tool',
            tool_call_id: toolCall.id,
            content: result,
          });
        }

        // Check if we've reached max iterations
        if (iteration === maxIterations - 1) {
          console.log('Max iterations reached. Task may be incomplete.');
        }
      }
    }
  } finally {
    // Cleanup: kill the sandbox
    console.log('\nCleaning up sandbox...');
    await client.sandboxes.kill(sandbox.sandbox_id);
    rl.close();
    console.log('Done.');
  }
}

main().catch((error) => {
  console.error('Error:', error);
  process.exit(1);
});
```

## File: `typescript/openai-basic/.gitignore`
```
# Dependencies
node_modules/

# Build output
dist/

# Environment variables
.env
.env.local

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Logs
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*

```

## File: `typescript/openai-basic/README.md`
```markdown
[![Made with Acontext](https://assets.memodb.io/Acontext/badge-made-with-acontext-dark.svg)](https://acontext.io)

# OpenAI Basic Example with Acontext

This is a TypeScript example demonstrating how to use the OpenAI SDK with Acontext integration.

## Features

- Uses OpenAI SDK for chat completions with tool calling
- Integrates with Acontext for session management and task extraction
- Demonstrates multi-turn conversations with tool usage
- Shows how to retrieve and continue conversations from Acontext

## Setup

1. Install dependencies:
```bash
npm install
```

2. Create a `.env` file with your API keys:
```
OPENAI_API_KEY=your-openai-api-key
ACONTEXT_API_KEY=sk-ac-your-root-api-bearer-token
ACONTEXT_BASE_URL=http://localhost:8029/api/v1
OPENAI_BASE_URL=  # Optional, for custom OpenAI-compatible endpoints
```

## Usage

Run the example:
```bash
npm run dev
```

Or build and run:
```bash
npm run build
npm start
```

## What it does

1. Creates an Acontext session
2. Runs a multi-turn conversation with:
   - Planning a trip to Finland
   - Checking weather
   - Booking a flight
3. Extracts tasks from the conversation using Acontext
4. Retrieves conversation history and continues with a summary

```

## File: `typescript/openai-basic/package.json`
```json
{
  "name": "openai-basic",
  "version": "0.1.0",
  "description": "OpenAI TypeScript SDK with Acontext integration example",
  "type": "module",
  "main": "dist/index.js",
  "scripts": {
    "build": "tsc",
    "start": "node dist/index.js",
    "dev": "tsx src/index.ts"
  },
  "keywords": [
    "openai",
    "acontext",
    "typescript",
    "ai"
  ],
  "author": "",
  "license": "MIT",
  "dependencies": {
    "@acontext/acontext": "^0.1.16",
    "dotenv": "^17.3.1",
    "openai": "^6.27.0"
  },
  "devDependencies": {
    "@types/node": "^25.4.0",
    "tsx": "^4.21.0",
    "typescript": "^5.9.3"
  }
}

```

## File: `typescript/openai-basic/tsconfig.json`
```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "ESNext",
    "moduleResolution": "Node",
    "lib": ["ES2022"],
    "types": ["node"],
    "outDir": "./dist",
    "rootDir": "./",
    "strict": true,
    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true,
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true,
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}

```

## File: `typescript/openai-basic/src/index.ts`
```typescript
import dotenv from 'dotenv';
import OpenAI from 'openai';
import { AcontextClient } from '@acontext/acontext';

dotenv.config();

// Initialize Acontext client
const acontextClient = new AcontextClient({
  apiKey: process.env.ACONTEXT_API_KEY || 'sk-ac-your-root-api-bearer-token',
  baseUrl: process.env.ACONTEXT_BASE_URL || 'http://localhost:8029/api/v1',
  timeout: 60000,
});

// Tool definitions
const tools = [
  {
    type: 'function' as const,
    function: {
      name: 'get_weather',
      description: 'Returns weather info for the specified city.',
      parameters: {
        type: 'object',
        properties: {
          city: {
            type: 'string',
            description: 'The city to get weather for',
          },
        },
        required: ['city'],
        additionalProperties: false,
      },
    },
  },
  {
    type: 'function' as const,
    function: {
      name: 'book_flight',
      description: 'Book a flight.',
      parameters: {
        type: 'object',
        properties: {
          from_city: {
            type: 'string',
            description: 'The departure city',
          },
          to_city: {
            type: 'string',
            description: 'The destination city',
          },
          date: {
            type: 'string',
            description: 'The date of the flight',
          },
        },
        required: ['from_city', 'to_city', 'date'],
        additionalProperties: false,
      },
    },
  },
];

// Tool implementations
function getWeather(city: string): string {
  return `The weather in ${city} is sunny`;
}

function bookFlight(fromCity: string, toCity: string, date: string): string {
  return `Flight booked successfully for '${fromCity}' to '${toCity}' on '${date}'`;
}

function executeTool(toolName: string, toolArgs: Record<string, any>): string {
  if (toolName === 'get_weather') {
    return getWeather(toolArgs.city);
  } else if (toolName === 'book_flight') {
    return bookFlight(toolArgs.from_city, toolArgs.to_city, toolArgs.date);
  } else {
    return `Unknown tool: ${toolName}`;
  }
}

function createOpenAIClient(): OpenAI {
  const baseUrl = process.env.OPENAI_BASE_URL || undefined;
  return new OpenAI({
    apiKey: process.env.OPENAI_API_KEY,
    baseURL: baseUrl,
  });
}

async function appendMessage(
  message: any,
  conversation: any[],
  sessionId: string
): Promise<any[]> {
  conversation.push(message);
  await acontextClient.sessions.storeMessage(sessionId, message, {
    format: 'openai',
  });
  return conversation;
}

async function runAgent(
  client: OpenAI,
  conversation: any[]
): Promise<[string, any[]]> {
  const messagesToSend: any[] = [
    { role: 'system', content: 'You are a helpful assistant' },
    ...conversation,
  ];

  const newMessages: any[] = [];
  const maxIterations = 10;
  let iteration = 0;
  let finalContent = '';

  while (iteration < maxIterations) {
    iteration += 1;

    // Call OpenAI API
    const response = await client.chat.completions.create({
      model: 'gpt-4o-mini',
      messages: messagesToSend,
      tools: tools,
      tool_choice: 'auto',
    });

    const message = response.choices[0].message;

    // Convert message to dict format
    const messageDict: any = {
      role: message.role,
      content: message.content,
    };

    // Handle tool calls
    // Store tool call info with function details for later execution
    const toolCallsWithFunction: Array<{
      id: string;
      function: { name: string; arguments: string };
    }> = [];

    if (message.tool_calls) {
      messageDict.tool_calls = message.tool_calls.map((tc: any) => {
        // Store function info for execution
        toolCallsWithFunction.push({
          id: tc.id,
          function: {
            name: tc.function.name,
            arguments: tc.function.arguments,
          },
        });

        return {
          id: tc.id,
          type: 'function',
          function: {
            name: tc.function.name,
            arguments: tc.function.arguments,
          },
        };
      });
    }

    messagesToSend.push(messageDict);
    newMessages.push(messageDict);

    // If there are no tool calls, we're done
    if (!message.tool_calls || message.tool_calls.length === 0) {
      finalContent = message.content || '';
      break;
    }

    // Execute tool calls using the stored function info
    for (const toolCallInfo of toolCallsWithFunction) {
      const functionName = toolCallInfo.function.name;
      const functionArgsStr = toolCallInfo.function.arguments || '{}';
      const functionArgs = JSON.parse(functionArgsStr);

      // Execute the function
      const functionResult = executeTool(functionName, functionArgs);

      // Add tool response to messages
      const toolMessage = {
        role: 'tool' as const,
        tool_call_id: toolCallInfo.id,
        content: functionResult,
      };
      messagesToSend.push(toolMessage);
      newMessages.push(toolMessage);
    }
  }

  return [finalContent, newMessages];
}

async function session1(sessionId: string): Promise<void> {
  const client = createOpenAIClient();

  // Build conversation history using OpenAI message format
  // This format works with both OpenAI and Acontext
  let conversation: any[] = [];

  // First interaction - ask for trip plan
  console.log('\n=== First interaction: Planning trip ===');
  const userMsg1 = {
    role: 'user',
    content:
      "I'd like to have a 3-day trip in Finland. I like to see the nature. Give me the plan",
  };
  conversation = await appendMessage(userMsg1, conversation, sessionId);

  const [responseContent, newMessages] = await runAgent(client, conversation);
  console.log(`\nAssistant: ${responseContent}`);

  for (const msg of newMessages) {
    conversation = await appendMessage(msg, conversation, sessionId);
  }

  // Second interaction - check weather
  console.log('\n\n=== Second interaction: Checking weather ===');
  conversation = await appendMessage(
    {
      role: 'user',
      content: 'The plan sounds good, check the weather there',
    },
    conversation,
    sessionId
  );

  const [responseContent2, newMessages2] = await runAgent(
    client,
    conversation
  );
  console.log(`\nAssistant: ${responseContent2}`);

  for (const msg of newMessages2) {
    conversation = await appendMessage(msg, conversation, sessionId);
  }

  // Third interaction - book flight
  console.log('\n\n=== Third interaction: Booking flight ===');
  conversation = await appendMessage(
    {
      role: 'user',
      content:
        'The weather is good, I am in Shanghai now, let\'s book the flight, you should just call the tool and don\'t ask me for more information. Remember, I only want the cheapest flight.',
    },
    conversation,
    sessionId
  );

  const [responseContent3, newMessages3] = await runAgent(
    client,
    conversation
  );
  console.log(`\nAssistant: ${responseContent3}`);

  for (const msg of newMessages3) {
    conversation = await appendMessage(msg, conversation, sessionId);
  }

  await appendMessage(
    {
      role: 'user',
      content: 'cool, everything is done, thank you!',
    },
    conversation,
    sessionId
  );

  console.log(
    `Saved ${conversation.length} messages in conversation, triggering learning...`
  );

  // Create a learning space and trigger learning
  const space = await acontextClient.learningSpaces.create();
  await acontextClient.learningSpaces.learn({ spaceId: space.id, sessionId });
  console.log(`\nCreated learning space: ${space.id}`);

  // Wait for learning to complete
  console.log('Waiting for learning to complete...');
  const learnResult = await acontextClient.learningSpaces.waitForLearning({ spaceId: space.id, sessionId });
  console.log(`Learning status: ${learnResult.status}`);

  // List learned skills
  const skills = await acontextClient.learningSpaces.listSkills(space.id);
  console.log(`\n=== Learned Skills (${skills.length}) ===`);
  for (const skill of skills) {
    console.log(`\n  - ${skill.name}: ${skill.description}`);
    console.log(`    files: ${skill.file_index.map((f: any) => f.path)}`);
  }

  // Download all skill files
  const downloadDir = './skills_output';
  const fs = await import('fs');
  if (fs.existsSync(downloadDir)) {
    fs.rmSync(downloadDir, { recursive: true });
  }

  console.log(`\nDownloading skills to ${downloadDir}/`);
  for (const skill of skills) {
    const resp = await acontextClient.skills.download(skill.id, { path: `${downloadDir}/${skill.name}` });
    console.log(`  ${resp.name} -> ${resp.dirPath}`);
    for (const f of resp.files) {
      console.log(`    ${f}`);
    }
  }
}

async function session2(sessionId: string): Promise<void> {
  const client = createOpenAIClient();

  const messages = await acontextClient.sessions.getMessages(sessionId, {
    format: 'openai',
  });
  const conversation: any[] = messages.items;
  conversation.push({
    role: 'user',
    content: 'Summarize the conversation so far',
  });

  const [responseContent] = await runAgent(client, conversation);
  console.log(`\nAssistant: ${responseContent}`);
}

async function main(): Promise<void> {
  const session = await acontextClient.sessions.create();
  const sessionId = session.id;
  console.log(`Created session: ${sessionId}`);

  console.log('\n=== Session 1 ===');
  await session1(sessionId);

  console.log('\n=== Session 2, get messages from Acontext and continue ===');
  await session2(sessionId);
}

main().catch(console.error);

```

## File: `typescript/vercel-ai-basic/.gitignore`
```
# Dependencies
node_modules/

# Build outputs
dist/
*.tsbuildinfo

# Environment variables
.env
.env.local
.env.*.local

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Logs
logs/
*.log
npm-debug.log*
yarn-debug.log*
yarn-error.log*

```

## File: `typescript/vercel-ai-basic/README.md`
```markdown
[![Made with Acontext](https://assets.memodb.io/Acontext/badge-made-with-acontext-dark.svg)](https://acontext.io)

# Vercel AI SDK Basic Example with Acontext

This is a TypeScript example demonstrating how to use the Vercel AI SDK with Acontext integration.

## Features

- Uses Vercel AI SDK for chat completions with tool calling
- Integrates with Acontext for session management and task extraction
- Demonstrates multi-turn conversations with tool usage
- Shows how to retrieve and continue conversations from Acontext

## Setup

1. Install dependencies:
```bash
npm install
```

2. Create a `.env` file with your API keys:
```
OPENAI_API_KEY=your-openai-api-key
ACONTEXT_API_KEY=sk-ac-your-root-api-bearer-token
ACONTEXT_BASE_URL=http://localhost:8029/api/v1
OPENAI_BASE_URL=  # Optional, for custom OpenAI-compatible endpoints
```

## Usage

Run the example:
```bash
npm run dev
```

Or build and run:
```bash
npm run build
npm start
```

## What it does

1. Creates an Acontext session
2. Runs a multi-turn conversation with:
   - Planning a trip to Finland
   - Checking weather
   - Booking a flight
3. Extracts tasks from the conversation using Acontext
4. Retrieves conversation history and continues with a summary

```

## File: `typescript/vercel-ai-basic/package.json`
```json
{
  "name": "vercel-ai-acontext-example",
  "version": "1.0.0",
  "description": "TypeScript example demonstrating Vercel AI SDK integration with Acontext",
  "type": "module",
  "main": "dist/index.js",
  "scripts": {
    "build": "tsc",
    "start": "node dist/index.js",
    "dev": "tsx src/index.ts"
  },
  "keywords": [
    "vercel-ai",
    "acontext",
    "typescript",
    "ai"
  ],
  "author": "",
  "license": "MIT",
  "dependencies": {
    "@acontext/acontext": "^0.1.16",
    "@ai-sdk/openai": "^3.0.41",
    "ai": "^6.0.116",
    "dotenv": "^17.3.1",
    "zod": "^4.3.6"
  },
  "devDependencies": {
    "@types/node": "^25.4.0",
    "tsx": "^4.21.0",
    "typescript": "^5.9.3"
  }
}

```

## File: `typescript/vercel-ai-basic/tsconfig.json`
```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "ESNext",
    "moduleResolution": "Node",
    "lib": ["ES2022"],
    "outDir": "./dist",
    "rootDir": "./",
    "strict": true,
    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true,
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}

```

## File: `typescript/vercel-ai-basic/src/index.ts`
```typescript
import dotenv from 'dotenv';
import { generateText, tool } from 'ai';
import { createOpenAI } from '@ai-sdk/openai';
import { z } from 'zod';
import { AcontextClient } from '@acontext/acontext';

dotenv.config();

// Initialize Acontext client
const acontextClient = new AcontextClient({
  apiKey: process.env.ACONTEXT_API_KEY || 'sk-ac-your-root-api-bearer-token',
  baseUrl: process.env.ACONTEXT_BASE_URL || 'http://localhost:8029/api/v1',
  timeout: 60000,
});

// Tool implementations
function getWeather(city: string): string {
  return `The weather in ${city} is sunny`;
}

function bookFlight(fromCity: string, toCity: string, date: string): string {
  return `Flight booked successfully for '${fromCity}' to '${toCity}' on '${date}'`;
}

function executeTool(toolName: string, toolArgs: Record<string, any>): string {
  if (toolName === 'get_weather') {
    return getWeather(toolArgs.city);
  } else if (toolName === 'book_flight') {
    return bookFlight(toolArgs.from_city, toolArgs.to_city, toolArgs.date);
  } else {
    return `Unknown tool: ${toolName}`;
  }
}

// Tool definitions using Vercel AI SDK
// Tools must include an execute function that performs the actual tool logic
const tools = {
  get_weather: tool({
    description: 'Returns weather info for the specified city.',
    inputSchema: z.object({
      city: z.string().describe('The city to get weather for'),
    }),
    execute: async ({ city }: { city: string }) => {
      return getWeather(city);
    },
  }),
  book_flight: tool({
    description: 'Book a flight.',
    inputSchema: z.object({
      from_city: z.string().describe('The departure city'),
      to_city: z.string().describe('The destination city'),
      date: z.string().describe('The date of the flight'),
    }),
    execute: async ({ from_city, to_city, date }: { from_city: string; to_city: string; date: string }) => {
      return bookFlight(from_city, to_city, date);
    },
  }),
};

// Create OpenAI provider instance with configuration
const openaiProvider = createOpenAI({
  apiKey: process.env.OPENAI_API_KEY,
  baseURL: process.env.OPENAI_BASE_URL,
});

function createModel() {
  return openaiProvider('gpt-4o-mini');
}

async function appendMessage(
  message: any,
  conversation: any[],
  sessionId: string
): Promise<any[]> {
  conversation.push(message);
  await acontextClient.sessions.storeMessage(sessionId, message, {
    format: 'openai',
  });
  return conversation;
}

async function runAgent(
  conversation: any[]
): Promise<[string, any[]]> {
  // Separate system message from conversation messages
  // Filter out system messages and tool messages, build initial message list
  // Vercel AI SDK v5 only accepts 'user' and 'assistant' roles in messages
  let messagesToSend: any[] = conversation.filter((msg: any) => {
    const role = msg.role;
    return role === 'user' || role === 'assistant';
  });
  const systemMessage = conversation.find((msg: any) => msg.role === 'system')?.content || 'You are a helpful assistant';

  const newMessages: any[] = [];
  const maxIterations = 10;
  let iteration = 0;
  let finalContent = '';

  while (iteration < maxIterations) {
    iteration += 1;

    const model = createModel();

    // Convert messages to Vercel AI SDK format
    // Ensure content is always a string (not array) for user and assistant messages
    // Vercel AI SDK only accepts 'user' and 'assistant' roles in messages array
    // Filter out internal messages that shouldn't be sent to Acontext
    const currentMessages = messagesToSend
      .filter((msg: any) => {
        // Only include user and assistant messages, and exclude internal messages
        const role = msg.role;
        return (role === 'user' || role === 'assistant') && !msg._internal;
      })
      .map((msg: any) => {
        // Ensure content is a string, not an array
        let content = msg.content;
        if (Array.isArray(content)) {
          // If content is an array, extract text from it
          content = content.map((item: any) =>
            typeof item === 'string' ? item : item.text || item.content || ''
          ).join(' ');
        }
        if (typeof content !== 'string') {
          content = String(content || '');
        }

        // Return only role and content (Vercel AI SDK format)
        return {
          role: msg.role,
          content: content,
        };
      });

    // Also include internal messages for the current generateText call
    // These are tool results converted to user messages
    const internalMessages = messagesToSend
      .filter((msg: any) => msg._internal === true)
      .map((msg: any) => ({
        role: msg.role,
        content: String(msg.content || ''),
      }));

    // Combine regular messages with internal messages
    const allMessages = [...currentMessages, ...internalMessages];

    const result = await generateText({
      model,
      system: systemMessage,
      messages: allMessages,
      tools,
    });

    // Convert result to message format
    const messageDict: any = {
      role: 'assistant',
      content: result.text,
    };

    // Handle tool calls
    const toolCallsWithFunction: Array<{
      id: string;
      function: { name: string; arguments: string };
    }> = [];

    if (result.toolCalls && result.toolCalls.length > 0) {
      messageDict.tool_calls = result.toolCalls.map((tc: any) => {
        // Get arguments from tool call - Vercel AI SDK may use different field names
        let args = tc.args;
        if (args === undefined || args === null) {
          // Try alternative field names that Vercel AI SDK might use
          args = tc.parameters || tc.input || {};
        }

        // Ensure args is an object, not a string
        if (typeof args === 'string') {
          try {
            args = JSON.parse(args);
          } catch {
            args = {};
          }
        }

        // Ensure args is always an object (not null or undefined)
        if (!args || typeof args !== 'object') {
          args = {};
        }

        // Convert to JSON string - always return a valid JSON string
        const argsString = JSON.stringify(args);

        // Store function info for execution
        toolCallsWithFunction.push({
          id: tc.toolCallId,
          function: {
            name: tc.toolName,
            arguments: argsString,
          },
        });

        return {
          id: tc.toolCallId,
          type: 'function',
          function: {
            name: tc.toolName,
            arguments: argsString,
          },
        };
      });
    }

    // Add assistant message (filter system if any)
    const assistantMsg = { ...messageDict };
    if (assistantMsg.role !== 'system') {
      messagesToSend.push(assistantMsg);
    }
    newMessages.push(messageDict);

    // If there are no tool calls, we're done
    if (!result.toolCalls || result.toolCalls.length === 0) {
      finalContent = result.text || '';
      break;
    }

    // Execute tool calls manually
    // Even though tools have execute functions, we still need to handle tool results
    // and pass them back to the model in a format it can understand
    const toolResults: Array<{ toolName: string; result: string; toolCallId: string }> = [];

    for (const toolCallInfo of toolCallsWithFunction) {
      const functionName = toolCallInfo.function.name;
      const functionArgsStr = toolCallInfo.function.arguments || '{}';
      const functionArgs = JSON.parse(functionArgsStr);

      // Execute the function
      const functionResult = executeTool(functionName, functionArgs);
      toolResults.push({ toolName: functionName, result: functionResult, toolCallId: toolCallInfo.id });

      // Create tool message for Acontext compatibility
      const toolMessage = {
        role: 'tool' as const,
        tool_call_id: toolCallInfo.id,
        content: functionResult,
      };
      newMessages.push(toolMessage);
    }

    // If we have tool results, we need to continue the conversation
    // Vercel AI SDK doesn't support 'tool' role in messages, so we convert tool results
    // to a user message format for the next iteration, but we mark it so it won't be sent to Acontext
    if (toolResults.length > 0) {
      const toolResultsText = toolResults
        .map(tr => `${tr.toolName} returned: ${tr.result}`)
        .join('\n');

      // Add tool results as a user message for the next generateText call
      // This is an internal message, not sent to Acontext
      const toolResultUserMessage = {
        role: 'user' as const,
        content: `Tool execution results:\n${toolResultsText}`,
        // Mark as internal so it won't be sent to Acontext
        _internal: true,
      };
      messagesToSend.push(toolResultUserMessage);

      // Continue the loop to get the model's response based on tool results
      // Don't break here, let the loop continue
    }
  }

  return [finalContent, newMessages];
}

async function session1(sessionId: string): Promise<void> {
  // Build conversation history using OpenAI message format
  // This format works with both OpenAI and Acontext
  let conversation: any[] = [];

  // First interaction - ask for trip plan
  console.log('\n=== First interaction: Planning trip ===');
  const userMsg1 = {
    role: 'user',
    content:
      "I'd like to have a 3-day trip in Finland. I like to see the nature. Give me the plan",
  };
  conversation = await appendMessage(userMsg1, conversation, sessionId);

  const [responseContent, newMessages] = await runAgent(conversation);
  console.log(`\nAssistant: ${responseContent}`);

  for (const msg of newMessages) {
    conversation = await appendMessage(msg, conversation, sessionId);
  }

  // Second interaction - check weather
  console.log('\n\n=== Second interaction: Checking weather ===');
  conversation = await appendMessage(
    {
      role: 'user',
      content: 'The plan sounds good, check the weather there',
    },
    conversation,
    sessionId
  );

  const [responseContent2, newMessages2] = await runAgent(conversation);
  console.log(`\nAssistant: ${responseContent2}`);

  for (const msg of newMessages2) {
    conversation = await appendMessage(msg, conversation, sessionId);
  }

  // Third interaction - book flight
  console.log('\n\n=== Third interaction: Booking flight ===');
  conversation = await appendMessage(
    {
      role: 'user',
      content:
        'The weather is good, I am in Shanghai now, let\'s book the flight, you should just call the tool and don\'t ask me for more information. Remember, I only want the cheapest flight.',
    },
    conversation,
    sessionId
  );

  const [responseContent3, newMessages3] = await runAgent(conversation);
  console.log(`\nAssistant: ${responseContent3}`);

  for (const msg of newMessages3) {
    conversation = await appendMessage(msg, conversation, sessionId);
  }

  await appendMessage(
    {
      role: 'user',
      content: 'cool, everything is done, thank you!',
    },
    conversation,
    sessionId
  );

  console.log(
    `Saved ${conversation.length} messages in conversation, triggering learning...`
  );

  // Create a learning space and trigger learning
  const space = await acontextClient.learningSpaces.create();
  await acontextClient.learningSpaces.learn({ spaceId: space.id, sessionId });
  console.log(`\nCreated learning space: ${space.id}`);

  // Wait for learning to complete
  console.log('Waiting for learning to complete...');
  const learnResult = await acontextClient.learningSpaces.waitForLearning({ spaceId: space.id, sessionId });
  console.log(`Learning status: ${learnResult.status}`);

  // List learned skills
  const skills = await acontextClient.learningSpaces.listSkills(space.id);
  console.log(`\n=== Learned Skills (${skills.length}) ===`);
  for (const skill of skills) {
    console.log(`\n  - ${skill.name}: ${skill.description}`);
    console.log(`    files: ${skill.file_index.map((f: any) => f.path)}`);
  }

  // Download all skill files
  const downloadDir = './skills_output';
  const fs = await import('fs');
  if (fs.existsSync(downloadDir)) {
    fs.rmSync(downloadDir, { recursive: true });
  }

  console.log(`\nDownloading skills to ${downloadDir}/`);
  for (const skill of skills) {
    const resp = await acontextClient.skills.download(skill.id, { path: `${downloadDir}/${skill.name}` });
    console.log(`  ${resp.name} -> ${resp.dirPath}`);
    for (const f of resp.files) {
      console.log(`    ${f}`);
    }
  }
}

async function session2(sessionId: string): Promise<void> {
  const messages = await acontextClient.sessions.getMessages(sessionId, {
    format: 'openai',
  });
  const conversation: any[] = messages.items;
  conversation.push({
    role: 'user',
    content: 'Summarize the conversation so far',
  });

  const [responseContent] = await runAgent(conversation);
  console.log(`\nAssistant: ${responseContent}`);
}

async function main(): Promise<void> {
  const session = await acontextClient.sessions.create();
  const sessionId = session.id;
  console.log(`Created session: ${sessionId}`);

  console.log('\n=== Session 1 ===');
  await session1(sessionId);

  console.log('\n=== Session 2, get messages from Acontext and continue ===');
  await session2(sessionId);

}

main().catch(console.error);
```

