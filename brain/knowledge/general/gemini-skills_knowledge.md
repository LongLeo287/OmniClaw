---
id: gemini-skills-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:26.179949
---

# KNOWLEDGE EXTRACT: gemini-skills
> **Extracted on:** 2026-03-30 13:15:17
> **Source:** gemini-skills

---

## File: `.gitignore`
```
### macOS ###
# General
.DS_Store
.AppleDouble
.LSOverride

# Icon must end with two \r
Icon


# Thumbnails
._*

# Files that might appear in the root of a volume
.DocumentRevisions-V100
.fseventsd
.Spotlight-V100
.TemporaryItems
.Trashes
.VolumeIcon.icns
.com.apple.timemachine.donotpresent

# Directories potentially created on remote AFP share
.AppleDB
.AppleDesktop
Network Trash Folder
Temporary Items
.apdisk

### macOS Patch ###
# iCloud generated files
*.icloud

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
brain/knowledge/docs_legacy/_build/

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
#   https://python-poetry.org/brain/knowledge/docs_legacy/basic-usage/#commit-your-poetrylock-file-to-version-control
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
# Poetry local configuration file - https://python-poetry.org/brain/knowledge/docs_legacy/configuration/#local-configuration
poetry.toml

# ruff
.ruff_cache/

# LSP config files
pyrightconfig.json
```

## File: `LICENSE`
```
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
```

## File: `README.md`
```markdown
# Gemini API skills

A library of skills for the Gemini API, SDK and model interactions.

## About

LLMs have fixed knowledge, being trained at a specific point in time. Software
dev is fast paced and changes often, where new libraries are launched every day
and best practices evolve quickly.

This leaves a knowledge gap that language models can't solve on their own. For
example, models don't know about themselves when they're trained, and they
aren't necessarily aware of subtle changes in best practices (like [thought
circulation](https://ai.google.dev/gemini-api/brain/knowledge/docs_legacy/thinking#signatures)) or SDK
changes.

[Skills](https://agentskills.io/) are a lightweight technique for adding
relevant context to your agents. This repo contains skills related to building
apps powered by the Gemini API.

### Performance

Our evaluations found that adding this skill improved an agent's ability to
generate correct API code following best practices to 87% with Gemini 3 Flash
and 96% with Gemini 3 Pro.

## Skills in this repo

| Skill | Description |
| :--- | :--- |
| [`gemini-api-dev`](skills/gemini-api-dev) | Skill for developing Gemini-powered apps. Provides the best practices for building apps that use the Gemini API. |
| [`vertex-ai-api-dev`](skills/vertex-ai-api-dev) | Skill for developing Gemini-powered apps on Google Cloud Vertex AI using the Gen AI SDK. Covers tools, multimodal generation, caching, and batch prediction. |
| [`gemini-live-api-dev`](skills/gemini-live-api-dev) | Skill for building real-time, bidirectional streaming apps with the Gemini Live API. Covers WebSocket-based audio/video/text streaming, voice activity detection, native audio features, function calling, and session management. |
| [`gemini-interactions-api`](skills/gemini-interactions-api) | Skill for building apps with the [Gemini Interactions API](https://ai.google.dev/gemini-api/brain/knowledge/docs_legacy/interactions?ua=chat). Covers text generation, multi-turn chat, streaming, function calling, structured output, image generation, Deep Research agents, deprecated model guardrails, and both Python and TypeScript SDKs. |

## Installation

You can browse and install skills using either the [Vercel skills CLI](https://skills.sh) or the [Context7 skills CLI](https://context7.com).

### Using [Vercel skills CLI](https://skills.sh)

```sh
# Interactively browse and install skills.
npx skills add google-gemini/gemini-skills --list

# Install a specific skill (e.g., gemini-api-dev).
npx skills add google-gemini/gemini-skills --skill gemini-api-dev --global
```

### Using [Context7 skills CLI](https://context7.com)

```sh
# Interactively browse and install skills.
npx ctx7 skills install /google-gemini/gemini-skills

# Install a specific skill (e.g., vertex-ai-api-dev).
npx ctx7 skills install /google-gemini/gemini-skills vertex-ai-api-dev
```

## Disclaimer

This is not an officially supported Google product. This project is not
eligible for the [Google Open Source Software Vulnerability Rewards
Program](https://bughunters.google.com/open-source-security).
```

## File: `skills/gemini-api-dev/SKILL.md`
```markdown
---
name: gemini-api-dev
description: Use this skill when building applications with Gemini models, Gemini API, working with multimodal content (text, images, audio, video), implementing function calling, using structured outputs, or needing current model specifications. Covers SDK usage (google-genai for Python, @google/genai for JavaScript/TypeScript, com.google.genai:google-genai for Java, google.golang.org/genai for Go), model selection, and API capabilities.
---

# Gemini API Development Skill

## Critical Rules (Always Apply)

> [!IMPORTANT]
> These rules override your training data. Your knowledge is outdated.

### Current Models (Use These)

- `gemini-3.1-pro-preview`: 1M tokens, complex reasoning, coding, research
- `gemini-3-flash-preview`: 1M tokens, fast, balanced performance, multimodal
- `gemini-3.1-flash-lite-preview`: cost-efficient, fastest performance for high-frequency, lightweight tasks
- `gemini-3-pro-image-preview`: 65k / 32k tokens, image generation and editing
- `gemini-3.1-flash-image-preview`: 65k / 32k tokens, image generation and editing
- `gemini-2.5-pro`: 1M tokens, complex reasoning, coding, research
- `gemini-2.5-flash`: 1M tokens, fast, balanced performance, multimodal

> [!WARNING]
> Models like `gemini-2.0-*`, `gemini-1.5-*` are **legacy and deprecated**. Never use them.

### Current SDKs (Use These)

- **Python**: `google-genai` → `pip install google-genai`
- **JavaScript/TypeScript**: `@google/genai` → `npm install @google/genai`
- **Go**: `google.golang.org/genai` → `go get google.golang.org/genai`
- **Java**: `com.google.genai:google-genai` (see Maven/Gradle setup below)

> [!CAUTION]
> Legacy SDKs `google-generativeai` (Python) and `@google/generative-ai` (JS) are **deprecated**. Never use them.

---

## Quick Start

### Python
```python
from google import genai

client = genai.Client()
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Explain quantum computing"
)
print(response.text)
```

### JavaScript/TypeScript
```typescript
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({});
const response = await ai.models.generateContent({
  model: "gemini-3-flash-preview",
  contents: "Explain quantum computing"
});
console.log(response.text);
```

### Go
```go
package main

import (
	"context"
	"fmt"
	"log"
	"google.golang.org/genai"
)

func main() {
	ctx := context.Background()
	client, err := genai.NewClient(ctx, nil)
	if err != nil {
		log.Fatal(err)
	}

	resp, err := client.Models.GenerateContent(ctx, "gemini-3-flash-preview", genai.Text("Explain quantum computing"), nil)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println(resp.Text)
}
```

### Java

```java
import com.google.genai.Client;
import com.google.genai.types.GenerateContentResponse;

public class GenerateTextFromTextInput {
  public static void main(String[] args) {
    Client client = new Client();
    GenerateContentResponse response =
        client.models.generateContent(
            "gemini-3-flash-preview",
            "Explain quantum computing",
            null);

    System.out.println(response.text());
  }
}
```

**Java Installation:**
- Latest version: https://central.sonatype.com/artifact/com.google.genai/google-genai/versions
- Gradle: `implementation("com.google.genai:google-genai:${LAST_VERSION}")`
- Maven:
  ```xml
  <dependency>
      <groupId>com.google.genai</groupId>
      <artifactId>google-genai</artifactId>
      <version>${LAST_VERSION}</version>
  </dependency>
  ```

---

## Documentation Lookup

### When MCP is Installed (Preferred)

If the **`search_documentation`** tool (from the Google MCP server) is available, use it as your **only** documentation source:

1. Call `search_documentation` with your query
2. Read the returned documentation
2. **Trust MCP results** as source of truth for API details — they are always up-to-date.

> [!IMPORTANT]
> When MCP tools are present, **never** fetch URLs manually. MCP provides up-to-date, indexed documentation that is more accurate and token-efficient than URL fetching.

### When MCP is NOT Installed (Fallback Only)

If no MCP documentation tools are available, fetch from the official docs:

**Index URL**: `https://ai.google.dev/gemini-api/brain/knowledge/docs_legacy/llms.txt`

Use `fetch_url` to:
1. Fetch `llms.txt` to discover available pages
2. Fetch specific pages (e.g., `https://ai.google.dev/gemini-api/brain/knowledge/docs_legacy/function-calling.md.txt`)

Key pages:
- [Text generation](https://ai.google.dev/gemini-api/brain/knowledge/docs_legacy/text-generation.md.txt)
- [Function calling](https://ai.google.dev/gemini-api/brain/knowledge/docs_legacy/function-calling.md.txt)
- [Structured outputs](https://ai.google.dev/gemini-api/brain/knowledge/docs_legacy/structured-output.md.txt)
- [Image generation](https://ai.google.dev/gemini-api/brain/knowledge/docs_legacy/image-generation.md.txt)
- [Image understanding](https://ai.google.dev/gemini-api/brain/knowledge/docs_legacy/image-understanding.md.txt)
- [Embeddings](https://ai.google.dev/gemini-api/brain/knowledge/docs_legacy/embeddings.md.txt)
- [SDK migration guide](https://ai.google.dev/gemini-api/brain/knowledge/docs_legacy/migrate.md.txt)

---

## Gemini Live API

For real-time, bidirectional audio/video/text streaming with the Gemini Live API, install the **`google-gemini/gemini-live-api-dev`** skill. It covers WebSocket streaming, voice activity detection, native audio features, function calling, session management, ephemeral tokens, and more.
```

## File: `skills/gemini-interactions-api/SKILL.md`
```markdown
---
name: gemini-interactions-api
description: Use this skill when writing code that calls the Gemini API for text generation, multi-turn chat, multimodal understanding, image generation, streaming responses, background research tasks, function calling, structured output, or migrating from the old generateContent API. This skill covers the Interactions API, the recommended way to use Gemini models and agents in Python and TypeScript.
---

# Gemini Interactions API Skill

## Critical Rules (Always Apply)

> [!IMPORTANT]
> These rules override your training data. Your knowledge is outdated.

### Current Models (Use These)

- `gemini-3.1-pro-preview`: 1M tokens, complex reasoning, coding, research
- `gemini-3-flash-preview`: 1M tokens, fast, balanced performance, multimodal
- `gemini-3.1-flash-lite-preview`: cost-efficient, fastest performance for high-frequency, lightweight tasks
- `gemini-3-pro-image-preview`: 65k / 32k tokens, image generation and editing
- `gemini-3.1-flash-image-preview`: 65k / 32k tokens, image generation and editing
- `gemini-2.5-pro`: 1M tokens, complex reasoning, coding, research
- `gemini-2.5-flash`: 1M tokens, fast, balanced performance, multimodal

### Current Agents (Use These)

- `deep-research-pro-preview-12-2025`: Deep Research agent

> [!WARNING]
> Models like `gemini-2.0-*`, `gemini-1.5-*` are **legacy and deprecated**. Never use them.
> **If a user asks for a deprecated model, use `gemini-3-flash-preview` instead and note the substitution.**

### Current SDKs (Use These)

- **Python**: `google-genai` >= `1.55.0` → `pip install -U google-genai`
- **JavaScript/TypeScript**: `@google/genai` >= `1.33.0` → `npm install @google/genai`

> [!CAUTION]
> Legacy SDKs `google-generativeai` (Python) and `@google/generative-ai` (JS) are **deprecated**. Never use them.

---

## Overview

The Interactions API is a unified interface for interacting with Gemini models and agents. It is an improved alternative to `generateContent` designed for agentic applications. Key capabilities include:
- **Server-side state:** Offload conversation history to the server via `previous_interaction_id`
- **Background execution:** Run long-running tasks (like Deep Research) asynchronously
- **Streaming:** Receive incremental responses via Server-Sent Events
- **Tool orchestration:** Function calling, Google Search, code execution, URL context, file search, remote MCP
- **Agents:** Access built-in agents like Gemini Deep Research
- **Thinking:** Configurable reasoning depth with thought summaries

---

## Quick Start

### Interact with a Model

#### Python
```python
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Tell me a short joke about programming."
)
print(interaction.outputs[-1].text)
```

#### JavaScript/TypeScript
```typescript
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const interaction = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: "Tell me a short joke about programming.",
});
console.log(interaction.outputs[interaction.outputs.length - 1].text);
```

### Stateful Conversation

#### Python
```python
from google import genai

client = genai.Client()

# First turn
interaction1 = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Hi, my name is Phil."
)

# Second turn — server remembers context
interaction2 = client.interactions.create(
    model="gemini-3-flash-preview",
    input="What is my name?",
    previous_interaction_id=interaction1.id
)
print(interaction2.outputs[-1].text)
```

#### JavaScript/TypeScript
```typescript
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

// First turn
const interaction1 = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: "Hi, my name is Phil.",
});

// Second turn — server remembers context
const interaction2 = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: "What is my name?",
    previous_interaction_id: interaction1.id,
});
console.log(interaction2.outputs[interaction2.outputs.length - 1].text);
```

### Deep Research Agent

#### Python
```python
import time
from google import genai

client = genai.Client()

# Start background research
interaction = client.interactions.create(
    agent="deep-research-pro-preview-12-2025",
    input="Research the history of Google TPUs.",
    background=True
)

# Poll for results
while True:
    interaction = client.interactions.get(interaction.id)
    if interaction.status == "completed":
        print(interaction.outputs[-1].text)
        break
    elif interaction.status == "failed":
        print(f"Failed: {interaction.error}")
        break
    time.sleep(10)
```

#### JavaScript/TypeScript
```typescript
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

// Start background research
const initialInteraction = await client.interactions.create({
    agent: "deep-research-pro-preview-12-2025",
    input: "Research the history of Google TPUs.",
    background: true,
});

// Poll for results
while (true) {
    const interaction = await client.interactions.get(initialInteraction.id);
    if (interaction.status === "completed") {
        console.log(interaction.outputs[interaction.outputs.length - 1].text);
        break;
    } else if (["failed", "cancelled"].includes(interaction.status)) {
        console.log(`Failed: ${interaction.status}`);
        break;
    }
    await new Promise(resolve => setTimeout(resolve, 10000));
}
```

### Streaming

#### Python
```python
from google import genai

client = genai.Client()

stream = client.interactions.create(
    model="gemini-3-flash-preview",
    input="Explain quantum entanglement in simple terms.",
    stream=True
)

for chunk in stream:
    if chunk.event_type == "content.delta":
        if chunk.delta.type == "text":
            print(chunk.delta.text, end="", flush=True)
    elif chunk.event_type == "interaction.complete":
        print(f"\n\nTotal Tokens: {chunk.interaction.usage.total_tokens}")
```

#### JavaScript/TypeScript
```typescript
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({});

const stream = await client.interactions.create({
    model: "gemini-3-flash-preview",
    input: "Explain quantum entanglement in simple terms.",
    stream: true,
});

for await (const chunk of stream) {
    if (chunk.event_type === "content.delta") {
        if (chunk.delta.type === "text" && "text" in chunk.delta) {
            process.stdout.write(chunk.delta.text);
        }
    } else if (chunk.event_type === "interaction.complete") {
        console.log(`\n\nTotal Tokens: ${chunk.interaction.usage.total_tokens}`);
    }
}
```

---

## Data Model

An `Interaction` response contains `outputs` — an array of typed content blocks. Each block has a `type` field:

- `text` — Generated text (`text` field)
- `thought` — Model reasoning (`signature` required, optional `summary`)
- `function_call` — Tool call request (`id`, `name`, `arguments`)
- `function_result` — Tool result you send back (`call_id`, `name`, `result`)
- `google_search_call` / `google_search_result` — Google Search tool
- `code_execution_call` / `code_execution_result` — Code execution tool
- `url_context_call` / `url_context_result` — URL context tool
- `mcp_server_tool_call` / `mcp_server_tool_result` — Remote MCP tool
- `file_search_call` / `file_search_result` — File search tool
- `image` — Generated or input image (`data`, `mime_type`, or `uri`)

**Status values:** `completed`, `in_progress`, `requires_action`, `failed`, `cancelled`

---

## Key Differences from generateContent

- `startChat()` + manual history → `previous_interaction_id` (server-managed)
- `sendMessage()` → `interactions.create(previous_interaction_id=...)`
- `response.text` → `interaction.outputs[-1].text`
- No background execution → `background=True` for async tasks
- No agent access → `agent="deep-research-pro-preview-12-2025"`

---

## Important Notes

- Interactions are **stored by default** (`store=true`). Paid tier retains for 55 days, free tier for 1 day.
- Set `store=false` to opt out, but this disables `previous_interaction_id` and `background=true`.
- `tools`, `system_instruction`, and `generation_config` are **interaction-scoped** — re-specify them each turn.
- **Agents require** `background=True`.
- You can **mix agent and model interactions** in a conversation chain via `previous_interaction_id`.

---

## Documentation Lookup

### When MCP is Installed (Preferred)

If the **`search_documentation`** tool (from the Google MCP server) is available, use it as your **only** documentation source:

1. Call `search_documentation` with your query
2. Read the returned documentation
2. **Trust MCP results** as source of truth for API details — they are always up-to-date.

> [!IMPORTANT]
> When MCP tools are present, **never** fetch URLs manually. MCP provides up-to-date, indexed documentation that is more accurate and token-efficient than URL fetching.

### When MCP is NOT Installed (Fallback Only)

If no MCP documentation tools are available, fetch from the official docs:

- [Interactions Full Documentation](https://ai.google.dev/gemini-api/brain/knowledge/docs_legacy/interactions.md.txt)
- [Deep Research Full Documentation](https://ai.google.dev/gemini-api/brain/knowledge/docs_legacy/deep-research.md.txt)

These pages cover function calling, built-in tools (Google Search, code execution, URL context, file search, computer use), remote MCP, structured output, thinking configuration, working with files, multimodal understanding and generation, streaming events, and more.


```

## File: `skills/gemini-live-api-dev/SKILL.md`
```markdown
---
name: gemini-live-api-dev
description: Use this skill when building real-time, bidirectional streaming applications with the Gemini Live API. Covers WebSocket-based audio/video/text streaming, voice activity detection (VAD), native audio features, function calling, session management, ephemeral tokens for client-side auth, and all Live API configuration options. SDKs covered - google-genai (Python), @google/genai (JavaScript/TypeScript).
---

# Gemini Live API Development Skill

## Overview

The Live API enables **low-latency, real-time voice and video interactions** with Gemini over WebSockets. It processes continuous streams of audio, video, or text to deliver immediate, human-like spoken responses.

Key capabilities:
- **Bidirectional audio streaming** — real-time mic-to-speaker conversations
- **Video streaming** — send camera/screen frames alongside audio
- **Text input/output** — send and receive text within a live session
- **Audio transcriptions** — get text transcripts of both input and output audio
- **Voice Activity Detection (VAD)** — automatic interruption handling
- **Native audio** — thinking (with configurable `thinkingLevel`)
- **Function calling** — synchronous tool use
- **Google Search grounding** — ground responses in real-time search results
- **Session management** — context compression, session resumption, GoAway signals
- **Ephemeral tokens** — secure client-side authentication

> [!NOTE]
> The Live API currently **only supports WebSockets**. For WebRTC support or simplified integration, use a [partner integration](#partner-integrations).

## Models

- `gemini-3.1-flash-live-preview` — Optimized for low-latency, real-time dialogue. Native audio output, thinking (via `thinkingLevel`). 128k context window. **This is the recommended model for all Live API use cases.**

> [!WARNING]
> The following Live API models are **deprecated** and will be shut down. Migrate to `gemini-3.1-flash-live-preview`.
> - `gemini-2.5-flash-native-audio-preview-12-2025` — Migrate to `gemini-3.1-flash-live-preview`.
> - `gemini-live-2.5-flash-preview` — Released June 17, 2025. Shutdown: December 9, 2025.
> - `gemini-2.0-flash-live-001` — Released April 9, 2025. Shutdown: December 9, 2025.

## SDKs

- **Python**: `google-genai` — `pip install google-genai`
- **JavaScript/TypeScript**: `@google/genai` — `npm install @google/genai`

> [!WARNING]
> Legacy SDKs `google-generativeai` (Python) and `@google/generative-ai` (JS) are deprecated. Use the new SDKs above.

## Partner Integrations

To streamline real-time audio/video app development, use a third-party integration supporting the Gemini Live API over **WebRTC** or **WebSockets**:

- [LiveKit](https://docs.livekit.io/agents/models/realtime/plugins/gemini/) — Use the Gemini Live API with LiveKit Agents.
- [Pipecat by Daily](https://docs.pipecat.ai/guides/features/gemini-live) — Create a real-time AI chatbot using Gemini Live and Pipecat.
- [Fishjam by Software Mansion](https://docs.fishjam.io/tutorials/gemini-live-integration) — Create live video and audio streaming applications with Fishjam.
- [Vision Agents by Stream](https://visionagents.ai/integrations/gemini) — Build real-time voice and video AI applications with Vision Agents.
- [Voximplant](https://voximplant.com/products/gemini-client) — Connect inbound and outbound calls to Live API with Voximplant.
- [Firebase AI SDK](https://firebase.google.com/brain/knowledge/docs_legacy/ai-logic/live-api?api=dev) — Get started with the Gemini Live API using Firebase AI Logic.

## Audio Formats

- **Input**: Raw PCM, little-endian, 16-bit, mono. 16kHz native (will resample others). MIME type: `audio/pcm;rate=16000`
- **Output**: Raw PCM, little-endian, 16-bit, mono. 24kHz sample rate.

> [!IMPORTANT]
> Use `send_realtime_input` / `sendRealtimeInput` for all real-time user input (audio, video, **and text**). `send_client_content` / `sendClientContent` is **only** supported for seeding initial context history (requires setting `initial_history_in_client_content` in `history_config`). Do **not** use it to send new user messages during the conversation.

> [!WARNING]
> Do **not** use `media` in `sendRealtimeInput`. Use the specific keys: `audio` for audio data, `video` for images/video frames, and `text` for text input.

---

## Quick Start

### Authentication

#### Python

```python
from google import genai

client = genai.Client(api_key="YOUR_API_KEY")
```

#### JavaScript

```js
import { GoogleGenAI } from '@google/genai';

const ai = new GoogleGenAI({ apiKey: 'YOUR_API_KEY' });
```

### Connecting to the Live API

#### Python
```python
from google.genai import types

config = types.LiveConnectConfig(
    response_modalities=[types.Modality.AUDIO],
    system_instruction=types.Content(
        parts=[types.Part(text="You are a helpful assistant.")]
    )
)

async with client.aio.live.connect(model="gemini-3.1-flash-live-preview", config=config) as session:
    pass  # Session is active
```

#### JavaScript
```js
const session = await ai.live.connect({
  model: 'gemini-3.1-flash-live-preview',
  config: {
    responseModalities: ['audio'],
    systemInstruction: { parts: [{ text: 'You are a helpful assistant.' }] }
  },
  callbacks: {
    onopen: () => console.log('Connected'),
    onmessage: (response) => console.log('Message:', response),
    onerror: (error) => console.error('Error:', error),
    onclose: () => console.log('Closed')
  }
});
```

### Sending Text

#### Python
```python
await session.send_realtime_input(text="Hello, how are you?")
```

#### JavaScript
```js
session.sendRealtimeInput({ text: 'Hello, how are you?' });
```

### Sending Audio

#### Python
```python
await session.send_realtime_input(
    audio=types.Blob(data=chunk, mime_type="audio/pcm;rate=16000")
)
```

#### JavaScript
```js
session.sendRealtimeInput({
  audio: { data: chunk.toString('base64'), mimeType: 'audio/pcm;rate=16000' }
});
```

### Sending Video

#### Python
```python
# frame: raw JPEG-encoded bytes
await session.send_realtime_input(
    video=types.Blob(data=frame, mime_type="image/jpeg")
)
```

#### JavaScript
```js
session.sendRealtimeInput({
  video: { data: frame.toString('base64'), mimeType: 'image/jpeg' }
});
```

### Receiving Audio and Text

> [!IMPORTANT]
> A single server event can contain **multiple content parts simultaneously** (e.g., audio chunks and transcript). Always process **all** parts in each event to avoid missing content.

#### Python
```python
async for response in session.receive():
    content = response.server_content
    if content:
        # Audio — process ALL parts in each event
        if content.model_turn:
            for part in content.model_turn.parts:
                if part.inline_data:
                    audio_data = part.inline_data.data
        # Transcription
        if content.input_transcription:
            print(f"User: {content.input_transcription.text}")
        if content.output_transcription:
            print(f"Gemini: {content.output_transcription.text}")
        # Interruption
        if content.interrupted is True:
            pass  # Stop playback, clear audio queue
```

#### JavaScript
```js
// Inside the onmessage callback
const content = response.serverContent;
if (content?.modelTurn?.parts) {
  for (const part of content.modelTurn.parts) {
    if (part.inlineData) {
      const audioData = part.inlineData.data; // Base64 encoded
    }
  }
}
if (content?.inputTranscription) console.log('User:', content.inputTranscription.text);
if (content?.outputTranscription) console.log('Gemini:', content.outputTranscription.text);
if (content?.interrupted) { /* Stop playback, clear audio queue */ }
```

---

## Limitations

- **Response modality** — Only `TEXT` **or** `AUDIO` per session, not both
- **Audio-only session** — 15 min without compression
- **Audio+video session** — 2 min without compression
- **Connection lifetime** — ~10 min (use session resumption)
- **Context window** — 128k tokens (native audio) / 32k tokens (standard)
- **Async function calling** — Not yet supported; function calling is synchronous only. The model will not start responding until you've sent the tool response.
- **Proactive audio** — Not yet supported in Gemini 3.1 Flash Live. Remove any configuration for this feature.
- **Affective dialogue** — Not yet supported in Gemini 3.1 Flash Live. Remove any configuration for this feature.
- **Code execution** — Not supported
- **URL context** — Not supported

## Migrating from Gemini 2.5 Flash Live

When migrating from `gemini-2.5-flash-native-audio-preview-12-2025` to `gemini-3.1-flash-live-preview`:

1. **Model string** — Update from `gemini-2.5-flash-native-audio-preview-12-2025` to `gemini-3.1-flash-live-preview`.
2. **Thinking configuration** — Use `thinkingLevel` (`minimal`, `low`, `medium`, `high`) instead of `thinkingBudget`. Default is `minimal` for lowest latency.
3. **Server events** — A single event can contain multiple content parts simultaneously (audio + transcript). Process **all** parts in each event.
4. **Client content** — `send_client_content` is only for seeding initial context history (set `initial_history_in_client_content` in `history_config`). Use `send_realtime_input` for text during conversation.
5. **Turn coverage** — Defaults to `TURN_INCLUDES_AUDIO_ACTIVITY_AND_ALL_VIDEO` instead of `TURN_INCLUDES_ONLY_ACTIVITY`. If sending constant video frames, consider sending only during audio activity to reduce costs.
6. **Async function calling** — Not yet supported. Function calling is synchronous only.
7. **Proactive audio & affective dialogue** — Not yet supported. Remove any configuration for these features.

## Best Practices

1. **Use headphones** when testing mic audio to prevent echo/self-interruption
2. **Enable context window compression** for sessions longer than 15 minutes
3. **Implement session resumption** to handle connection resets gracefully
4. **Use ephemeral tokens** for client-side deployments — never expose API keys in browsers
5. **Use `send_realtime_input`** for all real-time user input (audio, video, text). Reserve `send_client_content` only for seeding initial context history
6. **Send `audioStreamEnd`** when the mic is paused to flush cached audio
7. **Clear audio playback queues** on interruption signals
8. **Process all parts** in each server event — events can contain multiple content parts

## Documentation Lookup

### When MCP is Installed (Preferred)

If the **`search_documentation`** tool (from the Google MCP server) is available, use it as your **only** documentation source:

1. Call `search_documentation` with your query
2. Read the returned documentation
3. **Trust MCP results** as source of truth for API details — they are always up-to-date.

> [!IMPORTANT]
> When MCP tools are present, **never** fetch URLs manually. MCP provides up-to-date, indexed documentation that is more accurate and token-efficient than URL fetching.

### When MCP is NOT Installed (Fallback Only)

If no MCP documentation tools are available, fetch from the official docs index:

**llms.txt URL**: `https://ai.google.dev/gemini-api/brain/knowledge/docs_legacy/llms.txt`

This index contains links to all documentation pages in `.md.txt` format. Use web fetch tools to:

1. Fetch `llms.txt` to discover available documentation pages
2. Fetch specific pages (e.g., `https://ai.google.dev/gemini-api/brain/knowledge/docs_legacy/live-session.md.txt`)

### Key Documentation Pages 

> [!IMPORTANT]
> Those are not all the documentation pages. Use the `llms.txt` index to discover available documentation pages

- [Live API Overview](https://ai.google.dev/gemini-api/brain/knowledge/docs_legacy/live.md.txt) — getting started, raw WebSocket usage
- [Live API Capabilities Guide](https://ai.google.dev/gemini-api/brain/knowledge/docs_legacy/live-guide.md.txt) — voice config, transcription config, native audio (thinking), VAD configuration, media resolution
- [Live API Tool Use](https://ai.google.dev/gemini-api/brain/knowledge/docs_legacy/live-tools.md.txt) — function calling (sync and async), Google Search grounding
- [Session Management](https://ai.google.dev/gemini-api/brain/knowledge/docs_legacy/live-session.md.txt) — context window compression, session resumption, GoAway signals
- [Ephemeral Tokens](https://ai.google.dev/gemini-api/brain/knowledge/docs_legacy/ephemeral-tokens.md.txt) — secure client-side authentication for browser/mobile
- [WebSockets API Reference](https://ai.google.dev/api/live.md.txt) — raw WebSocket protocol details

## Supported Languages

The Live API supports 70 languages including: English, Spanish, French, German, Italian, Portuguese, Chinese, Japanese, Korean, Hindi, Arabic, Russian, and many more. Native audio models automatically detect and switch languages.
```

## File: `skills/vertex-ai-api-dev/SKILL.md`
```markdown
---
name: vertex-ai-api-dev
description: Guides the usage of Gemini API on Google Cloud Vertex AI with the Gen AI SDK. Use when the user asks about using Gemini in an enterprise environment or explicitly mentions Vertex AI. Covers SDK usage (Python, JS/TS, Go, Java, C#), capabilities like Live API, tools, multimedia generation, caching, and batch prediction.
compatibility: Requires active Google Cloud credentials and Vertex AI API enabled.
---

# Gemini API in Vertex AI

Access Google's most advanced AI models built for enterprise use cases using the Gemini API in Vertex AI.

Provide these key capabilities:

- **Text generation** - Chat, completion, summarization
- **Multimodal understanding** - Process images, audio, video, and documents
- **Function calling** - Let the model invoke your functions
- **Structured output** - Generate valid JSON matching your schema
- **Context caching** - Cache large contexts for efficiency
- **Embeddings** - Generate text embeddings for semantic search
- **Live Realtime API** - Bidirectional streaming for low latency Voice and Video interactions
- **Batch Prediction** - Handle massive async dataset prediction workloads

## Core Directives

- **Unified SDK**: ALWAYS use the Gen AI SDK (`google-genai` for Python, `@google/genai` for JS/TS, `google.golang.org/genai` for Go, `com.google.genai:google-genai` for Java, `Google.GenAI` for C#).
- **Legacy SDKs**: DO NOT use `google-cloud-aiplatform`, `@google-cloud/vertexai`, or `google-generativeai`.

## SDKs

- **Python**: Install `google-genai` with `pip install google-genai`
- **JavaScript/TypeScript**: Install `@google/genai` with `npm install @google/genai`
- **Go**: Install `google.golang.org/genai` with `go get google.golang.org/genai`
- **C#/.NET**: Install `Google.GenAI` with `dotnet add package Google.GenAI`
- **Java**:
  - groupId: `com.google.genai`, artifactId: `google-genai`
  - Latest version can be found here: https://central.sonatype.com/artifact/com.google.genai/google-genai/versions (let's call it `LAST_VERSION`) 
  - Install in `build.gradle`:

    ```
    implementation("com.google.genai:google-genai:${LAST_VERSION}")
    ```

  - Install Maven dependency in `pom.xml`:

    ```xml
    <dependency>
	    <groupId>com.google.genai</groupId>
	    <artifactId>google-genai</artifactId>
	    <version>${LAST_VERSION}</version>
	</dependency>
    ```

> [!WARNING]
> Legacy SDKs like `google-cloud-aiplatform`, `@google-cloud/vertexai`, and `google-generativeai` are deprecated. Migrate to the new SDKs above urgently by following the Migration Guide.

## Authentication & Configuration

Prefer environment variables over hard-coding parameters when creating the client. Initialize the client without parameters to automatically pick up these values.

### Application Default Credentials (ADC)
Set these variables for standard [Google Cloud authentication](https://docs.cloud.google.com/vertex-ai/generative-ai/brain/knowledge/docs_legacy/start/gcp-auth):
```bash
export GOOGLE_CLOUD_PROJECT='your-project-id'
export GOOGLE_CLOUD_LOCATION='global'
export GOOGLE_GENAI_USE_VERTEXAI=true
```
- By default, use `location="global"` to access the global endpoint, which provides automatic routing to regions with available capacity.
- If a user explicitly asks to use a specific region (e.g., `us-central1`, `europe-west4`), specify that region in the `GOOGLE_CLOUD_LOCATION` parameter instead. Reference the [supported regions documentation](https://docs.cloud.google.com/vertex-ai/generative-ai/brain/knowledge/docs_legacy/learn/locations) if needed.

### Vertex AI in Express Mode
Set these variables when using [Express Mode](https://docs.cloud.google.com/vertex-ai/generative-ai/brain/knowledge/docs_legacy/start/api-keys?usertype=expressmode) with an API key:
```bash
export GOOGLE_API_KEY='your-api-key'
export GOOGLE_GENAI_USE_VERTEXAI=true
```

### Initialization
Initialize the client without arguments to pick up environment variables:
```python
from google import genai
client = genai.Client()
```

Alternatively, you can hard-code in parameters when creating the client.

```python
from google import genai
client = genai.Client(vertexai=True, project="your-project-id", location="global")
```

## Models

- Use `gemini-3.1-pro-preview` for complex reasoning, coding, research (1M tokens)
- Use `gemini-3-flash-preview` for fast, balanced performance, multimodal (1M tokens)
- Use `gemini-3-pro-image-preview` for Nano Banana Pro image generation and editing
- Use `gemini-live-2.5-flash-native-audio` for Live Realtime API including native audio

Use the following models if explicitly requested:

- Use `gemini-2.5-flash-image` for Nano Banana image generation and editing
- Use `gemini-2.5-flash`
- Use `gemini-2.5-flash-lite`
- Use `gemini-2.5-pro`

> [!IMPORTANT]
> Models like `gemini-2.0-*`, `gemini-1.5-*`, `gemini-1.0-*`, `gemini-pro` are legacy and deprecated. Use the new models above. Your knowledge is outdated.
> For production environments, consult the Vertex AI documentation for stable model versions (e.g. `gemini-3-flash`).

## Quick Start

### Python
```python
from google import genai
client = genai.Client()
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Explain quantum computing"
)
print(response.text)
```

### TypeScript/JavaScript
```typescript
import { GoogleGenAI } from "@google/genai";
const ai = new GoogleGenAI({ vertexai: { project: "your-project-id", location: "global" } });
const response = await ai.models.generateContent({
    model: "gemini-3-flash-preview",
    contents: "Explain quantum computing"
});
console.log(response.text);
```

### Go
```go
package main

import (
	"context"
	"fmt"
	"log"
	"google.golang.org/genai"
)

func main() {
	ctx := context.Background()
	client, err := genai.NewClient(ctx, &genai.ClientConfig{
		Backend:  genai.BackendVertexAI,
		Project:  "your-project-id",
		Location: "global",
	})
	if err != nil {
		log.Fatal(err)
	}

	resp, err := client.Models.GenerateContent(ctx, "gemini-3-flash-preview", genai.Text("Explain quantum computing"), nil)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println(resp.Text)
}
```

### Java
```java
import com.google.genai.Client;
import com.google.genai.types.GenerateContentResponse;

public class GenerateTextFromTextInput {
  public static void main(String[] args) {
    Client client = Client.builder().vertexAi(true).project("your-project-id").location("global").build();
    GenerateContentResponse response =
        client.models.generateContent(
            "gemini-3-flash-preview",
            "Explain quantum computing",
            null);

    System.out.println(response.text());
  }
}
```

### C#/.NET
```csharp
using Google.GenAI;

var client = new Client(
    project: "your-project-id",
    location: "global",
    vertexAI: true
);

var response = await client.Models.GenerateContent(
    "gemini-3-flash-preview",
    "Explain quantum computing"
);

Console.WriteLine(response.Text);
```

## API spec & Documentation (source of truth)

When implementing or debugging API integration for Vertex AI, refer to the official Google Cloud Vertex AI documentation:
- **Vertex AI Gemini Documentation**: https://cloud.google.com/vertex-ai/generative-ai/brain/knowledge/docs_legacy/
- **REST API Reference**: https://cloud.google.com/vertex-ai/generative-ai/brain/knowledge/docs_legacy/reference/rest

The Gen AI SDK on Vertex AI uses the `v1beta1` or `v1` REST API endpoints (e.g., `https://{LOCATION}-aiplatform.googleapis.com/v1beta1/projects/{PROJECT}/locations/{LOCATION}/publishers/google/models/{MODEL}:generateContent`).

> [!TIP]
> **Use the Developer Knowledge MCP Server**: If the `search_documents` or `get_document` tools are available, use them to find and retrieve official documentation for Google Cloud and Vertex AI directly within the context. This is the preferred method for getting up-to-date API details and code snippets.

## Workflows and Code Samples

Reference the [Python Docs Samples repository](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/genai) for additional code samples and specific usage scenarios.

Depending on the specific user request, refer to the following reference files for detailed code samples and usage patterns (Python examples):

- **Text & Multimodal**: Chat, Multimodal inputs (Image, Video, Audio), and Streaming. See [references/text_and_multimodal.md](references/text_and_multimodal.md)
- **Embeddings**: Generate text embeddings for semantic search. See [references/embeddings.md](../../../core/security/QUARANTINE/incoming/repos/AutoGPT/docs/integrations/block_integrations/jina/embeddings.md)
- **Structured Output & Tools**: JSON generation, Function Calling, Search Grounding, and Code Execution. See [references/structured_and_tools.md](references/structured_and_tools.md)
- **Media Generation**: Image generation, Image editing, and Video generation. See [references/media_generation.md](references/media_generation.md)
- **Bounding Box Detection**: Object detection and localization within images and video. See [references/bounding_box.md](references/bounding_box.md)
- **Live API**: Real-time bidirectional streaming for voice, vision, and text. See [references/live_api.md](references/live_api.md)
- **Advanced Features**: Content Caching, Batch Prediction, and Thinking/Reasoning. See [references/advanced_features.md](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/creative_design/marp_slide/references/advanced_features.md)
- **Safety**: Adjusting Responsible AI filters and thresholds. See [references/safety.md](references/safety.md)
- **Model Tuning**: Supervised Fine-Tuning and Preference Tuning. See [references/model_tuning.md](references/model_tuning.md)
```

## File: `skills/vertex-ai-api-dev/references/advanced_features.md`
```markdown
# Advanced Features

## Content Caching
Cache large documents or contexts to reduce cost and latency.

```python
from google import genai
from google.genai import types

client = genai.Client()

content_cache = client.caches.create(
    model="gemini-3-flash-preview",
    config=types.CreateCachedContentConfig(
        contents=[
            types.Content(
                role="user",
                parts=[types.Part.from_uri(file_uri="gs://your-bucket/large.pdf", mime_type="application/pdf")]
            )
        ],
        system_instruction="You are an expert researcher.",
        display_name="example-cache",
        ttl="86400s",
    ),
)

# Use the cache
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Summarize the pdf",
    config=types.GenerateContentConfig(
        cached_content=content_cache.name
    ),
)
```

## Batch Prediction
For processing large datasets asynchronously.

```python
import time
from google import genai
from google.genai import types

client = genai.Client()

job = client.batches.create(
    model="gemini-3-flash-preview",
    src="gs://your-bucket/prompts.jsonl",
    config=types.CreateBatchJobConfig(dest="gs://your-bucket/outputs"),
)

completed_states = {types.JobState.JOB_STATE_SUCCEEDED, types.JobState.JOB_STATE_FAILED, types.JobState.JOB_STATE_CANCELLED}
while job.state not in completed_states:
    time.sleep(30)
    job = client.batches.get(name=job.name)
```

### Thinking (Reasoning)

Thinking is on by default for `gemini-3.1-pro-preview` and `gemini-3-flash-preview`.
It can be adjusted by using the `thinking_level` parameter.

- **`MINIMAL`:** (Gemini 3 Flash Only) Constrains the model to use as few tokens as possible for thinking and is best used for low-complexity tasks that wouldn't benefit from extensive reasoning.
- **`LOW`**: Constrains the model to use fewer tokens for thinking and is suitable for simpler tasks where extensive reasoning is not required.
- **`MEDIUM`**: Offers a balanced approach suitable for tasks of moderate complexity that benefit from reasoning but don't require deep, multi-step planning.
- **`HIGH`**: (Default) Maximizes reasoning depth. The model may take significantly longer to reach a first token, but the output will be more thoroughly vetted.

```python
from google import genai
from google.genai import types

client = genai.Client()
response = client.models.generate_content(
    model="gemini-3.1-pro-preview",
    contents="solve x^2 + 4x + 4 = 0",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(
            thinking_level=types.ThinkingLevel.HIGH
        )
    )
)

# Access thoughts if returned
for part in response.candidates[0].content.parts:
    if part.thought:
        print(f"Thought: {part.text}")
    else:
        print(f"Final Answer: {part.text}")
```

## Model Context Protocol (MCP) support (experimental)

Built-in [MCP](https://modelcontextprotocol.io/introduction) support is an experimental feature. You can pass a local MCP server as a tool directly.

```python
import os
import asyncio
from datetime import datetime
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from google import genai
from google.genai import types

client = genai.Client()

# Create server parameters for stdio connection
server_params = StdioServerParameters(
    command="npx",  # Executable
    args=["-y", "@philschmid/weather-mcp"],  # MCP Server
    env=None,  # Optional environment variables
)

async def run():
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Prompt to get the weather for the current day in London.
            prompt = f"What is the weather in London in {datetime.now().strftime('%Y-%m-%d')}?"

            # Initialize the connection between client and server
            await session.initialize()

            # Send request to the model with MCP function declarations
            response = await client.aio.models.generate_content(
                model="gemini-3-flash-preview",
                contents=prompt,
                config=types.GenerateContentConfig(
                    tools=[session],  # uses the session, will automatically call the tool using automatic function calling
                ),
            )
            print(response.text)

# Start the asyncio event loop and run the main function
asyncio.run(run())
```
```

## File: `skills/vertex-ai-api-dev/references/bounding_box.md`
```markdown
# Bounding Box Detection

Detect and localize objects within images or videos using bounding boxes. The model returns coordinates in the format `[y_min, x_min, y_max, x_max]`, normalized from 0 to 1000.

## Implementation (Python)

To ensure structured output, define a `BoundingBox` class and provide it as the `response_schema`.

```python
from google import genai
from google.genai.types import (
    GenerateContentConfig,
    Part,
)
from pydantic import BaseModel

# Define the schema for the bounding box
class BoundingBox(BaseModel):
    box_2d: list[int]
    label: str

client = genai.Client()

config = GenerateContentConfig(
    system_instruction="""
    Return bounding boxes as an array with labels.
    Never return masks. Limit to 25 objects.
    """,
    response_mime_type="application/json",
    response_schema=list[BoundingBox],
)

image_uri = "gs://cloud-samples-data/generative-ai/image/socks.jpg"

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[
        Part.from_uri(file_uri=image_uri, mime_type="image/jpeg"),
        "Detect the socks in the image and provide bounding boxes.",
    ],
    config=config,
)

# Access the detected boxes
for bbox in response.parsed:
    print(f"Label: {bbox.label}, Box: {bbox.box_2d}")
```

## Coordinate System
- **Format**: `[y_min, x_min, y_max, x_max]`
- **Normalization**: Coordinates are integers from `0` to `1000`.
- **Origin**: `[0, 0]` is the top-left corner of the image.

## Visualization Helper
To visualize the results, scale the normalized coordinates back to the original image dimensions.

```python
def scale_box(box_2d, width, height):
    y_min, x_min, y_max, x_max = box_2d
    return [
        int(y_min / 1000 * height),
        int(x_min / 1000 * width),
        int(y_max / 1000 * height),
        int(x_max / 1000 * width)
    ]
```
```

## File: `skills/vertex-ai-api-dev/references/embeddings.md`
```markdown
# Text Embeddings

Generate embeddings for text content to perform semantic search, clustering, and other NLP tasks.

## Basic Usage

```python
from google import genai
from google.genai import types

client = genai.Client()
response = client.models.embed_content(
    model="gemini-embedding-001",
    contents=[
        "How do I get a driver's license/learner's permit?",
        "How long is my driver's license valid for?",
    ],
    # Optional Parameters
    config=types.EmbedContentConfig(task_type="RETRIEVAL_DOCUMENT", output_dimensionality=768),
)
print(response.embeddings)
```
```

## File: `skills/vertex-ai-api-dev/references/live_api.md`
```markdown
# Live API

The Live API provides real-time, low-latency bidirectional streaming via WebSockets. It is ideal for interactive voice and video applications.

```python
import asyncio
from google import genai
from google.genai import types

async def generate_content():
    client = genai.Client()
    model_id = "gemini-live-2.5-flash-native-audio"

    config = types.LiveConnectConfig(
        response_modalities=[types.LiveModality.TEXT], # Change to AUDIO for voice responses
    )

    async with client.aio.live.connect(model=model_id, config=config) as session:
        text_input = "Hello? Gemini, are you there?"
        await session.send_client_content(
            turns=types.Content(role="user", parts=[types.Part.from_text(text=text_input)])
        )

        async for message in session.receive():
            if message.text:
                print(message.text, end="")

asyncio.run(generate_content())
```

For sending audio:
```python
await session.send_realtime_input(
    media=Blob(data=audio_bytes, mime_type="audio/pcm;rate=16000")
)
```
```

## File: `skills/vertex-ai-api-dev/references/media_generation.md`
```markdown
# Media Generation

## Image Generation
Generate images using `gemini-2.5-flash-image`.

```python
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash-image",
    contents="A dog reading a newspaper",
)

for part in response.parts:
    if part.text is not None:
        print(part.text)
    elif part.inline_data is not None:
        image = part.as_image()
        image.save("generated_image.png")
```

For high-resolution images or using the Search tool, use `gemini-3-pro-image-preview`.

```python
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-pro-image-preview",
    contents="A dog reading a newspaper",
    config=types.GenerateContentConfig(
        image_config=types.ImageConfig(
            aspect_ratio="16:9",
            image_size="2K"
        )
    )
)

for part in response.parts:
    if part.text is not None:
        print(part.text)
    elif part.inline_data is not None:
        image = part.as_image()
        image.save("generated_image.png")
```

## Image Editing
Editing images is better done using the Gemini native image generation model, and it is recommended to use chat mode.

```python
from google import genai
from PIL import Image

client = genai.Client()

prompt = "A small white ceramic bowl with lemons and limes"
image = Image.open('fruit.png')

# Create the chat
chat = client.chats.create(model='gemini-2.5-flash-image')

# Send the image and ask for it to be edited
response = chat.send_message([prompt, image])

# Get the text and the image generated
for i, part in enumerate(response.candidates[0].content.parts):
    if part.text is not None:
        print(part.text)
    elif part.inline_data is not None:
        image = part.as_image()
        image.save(f'generated_image_{i}.png')

# Continue iterating
chat.send_message('Make the bowl blue')
```

## Video Generation
Generate video using the Veo model. Usage of Veo can be costly, so check pricing for Veo. Start with the fast model (`veo-3.1-fast-generate-001`) since the result quality is usually sufficient, and swap to the larger model if needed.

```python
import time
from google import genai
from google.genai import types
from PIL import Image

client = genai.Client()

image = Image.open('image.png') # Optional initial image

# Video generation is an async operation
operation = client.models.generate_videos(
    model="veo-3.1-fast-generate-001",
    prompt="a cat reading a book",
    image=image,
    config=types.GenerateVideosConfig(
        person_generation="dont_allow",
        aspect_ratio="16:9",
        number_of_videos=1,
        duration_seconds=5,
        output_gcs_uri="gs://your-bucket/your-prefix",
    ),
)

# Poll for completion
while not operation.done:
    time.sleep(20)
    operation = client.operations.get(operation)

if operation.response:
    print(operation.result.generated_videos[0].video.uri)
```
```

## File: `skills/vertex-ai-api-dev/references/model_tuning.md`
```markdown
# Model Tuning

Supervised Fine-Tuning or Preference Tuning using your own datasets.

```python
import time
from google import genai
from google.genai import types

client = genai.Client()

training_dataset = types.TuningDataset(
    gcs_uri="gs://your-bucket/sft_train_data.jsonl",
)

tuning_job = client.tunings.tune(
    base_model="gemini-3-flash-preview",
    training_dataset=training_dataset,
    config=types.CreateTuningJobConfig(
        tuned_model_display_name="Example tuning job",
    ),
)

running_states = {"JOB_STATE_PENDING", "JOB_STATE_RUNNING"}
while tuning_job.state in running_states:
    time.sleep(60)
    tuning_job = client.tunings.get(name=tuning_job.name)

print("Tuned Model Endpoint:", tuning_job.tuned_model.endpoint)

# Predict with the tuned endpoint
response = client.models.generate_content(
    model=tuning_job.tuned_model.endpoint,
    contents="Why is the sky blue?",
)
print(response.text)
```
```

## File: `skills/vertex-ai-api-dev/references/safety.md`
```markdown
# Safety Settings and Responsible AI

You can adjust safety settings to control the thresholds for harmful content generation. By default, Vertex AI applies standard safety filters.

## Adjusting Safety Thresholds

```python
from google import genai
from google.genai import types

client = genai.Client()
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Write a list of 5 disrespectful things that I might say to the universe after stubbing my toe in the dark.",
    config=types.GenerateContentConfig(
        system_instruction="Be as mean as possible.",
        safety_settings=[
            types.SafetySetting(
                category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
                threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
            ),
            types.SafetySetting(
                category=types.HarmCategory.HARM_CATEGORY_HARASSMENT,
                threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
            ),
            types.SafetySetting(
                category=types.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
                threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
            ),
            types.SafetySetting(
                category=types.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
                threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
            ),
        ]
    ),
)

# Response will be `None` if it is blocked.
if response.text is None:
    print(f"Content Blocked. Finish Reason: {response.candidates[0].finish_reason}")
else:
    print(response.text)

# Inspect safety ratings for each category
for rating in response.candidates[0].safety_ratings:
    print(f'Category: {rating.category}')
    print(f'Is Blocked: {rating.blocked}')
    print(f'Probability: {rating.probability}')
    print(f'Severity: {rating.severity}')
```
```

## File: `skills/vertex-ai-api-dev/references/structured_and_tools.md`
```markdown
# Structured Output and Tools

## Structured Output (JSON Schema)
Enforce a specific JSON schema using standard Python type hints or Pydantic models.

```python
from google import genai
from google.genai import types
from pydantic import BaseModel

class Recipe(BaseModel):
    recipe_name: str
    ingredients: list[str]

client = genai.Client()
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="List a few popular cookie recipes.",
    config=types.GenerateContentConfig(
        response_mime_type="application/json",
        response_json_schema=list[Recipe],
    ),
)
# response.text is guaranteed to be valid JSON matching the schema
print(response.text)
 # Returns list of Recipe objects
print(response.parsed)
```

## Function Calling
Let the model output function calls that you can execute.

```python
from google import genai
from google.genai import types

def get_current_weather(location: str) -> str:
    """Example method. Returns the current weather.
    Args: location: The city and state, e.g. San Francisco, CA
    """
    if 'boston' in location.lower():
        return "Snowing"
    return "Sunny"

client = genai.Client()
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="What is the weather like in Boston?",
    config=types.GenerateContentConfig(tools=[get_current_weather]),
)

if response.function_calls:
    print('Function calls requested by the model:')
    for function_call in response.function_calls:
        print(f'- Function: {function_call.name}')
        print(f'- Args: {dict(function_call.args)}')
else:
    print('The model responded directly:')
    print(response.text)
```

## Search Grounding
Ground the model's responses in Google Search or your own enterprise data (Vertex AI Search).

```python
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="When is the next total solar eclipse in the US?",
    config=types.GenerateContentConfig(
        tools=[
            types.Tool(google_search=types.GoogleSearch())
        ],
    ),
)
print(response.text)
# Search details
print(f'Search Query: {response.candidates[0].grounding_metadata.web_search_queries}')
# Inspect grounding metadata
print(response.candidates[0].grounding_metadata.search_entry_point.rendered_content)
# Urls used for grounding
print(f"Search Pages: {', '.join([site.web.title for site in response.candidates[0].grounding_metadata.grounding_chunks])}")
```

## Code Execution
Allow the model to run Python code to calculate answers precisely.

```python
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="Calculate 20th fibonacci number.",
    config=types.GenerateContentConfig(
        tools=[types.Tool(code_execution=types.ToolCodeExecution())],
    ),
)
print(response.executable_code)
print(response.code_execution_result)
```

## Url Context
You can use the URL context tool to provide Gemini with URLs as additional context for your prompt. The model can then retrieve content from the URLs and use that content to inform and shape its response.

```python
from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model=model_id,
    contents="Compare recipes from http://example.com and http://example2.com",
    config=GenerateContentConfig(
        tools=[types.Tool(url_context=types.UrlContext)],
    )
)

print(response.text)
# get URLs retrieved for context
print(response.candidates[0].url_context_metadata)
```
```

## File: `skills/vertex-ai-api-dev/references/text_and_multimodal.md`
```markdown
# Text and Multimodal Generation

## Basic Text Generation
```python
from google import genai

client = genai.Client()
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="How does AI work?"
)
print(response.text)
```

## Chat (Multi-turn conversations)
```python
from google import genai
from google.genai import types

client = genai.Client()
chat_session = client.chats.create(
    model="gemini-3-flash-preview",
    history=[
        types.UserContent(parts=[types.Part.from_text(text="Hello")]),
        types.ModelContent(parts=[types.Part.from_text(text="Great to meet you. What would you like to know?")]),
    ],
)
response = chat_session.send_message("Tell me a story.")
print(response.text)
```

## Synchronous Streaming

Generate content in a streaming format so that the model outputs streams back
to you, rather than being returned as one chunk.

```python
from google import genai
from google.genai import types

client = genai.Client()
for chunk in client.models.generate_content_stream(
    model="gemini-3-flash-preview", contents="Tell me a story in 300 words."
):
    print(chunk.text, end='')
```

## Multimodal Inputs (Images, Audio, Video)
You can provide files natively using Google Cloud Storage URIs or local bytes.

```python
from google import genai
from google.genai import types

client = genai.Client()

gcs_image = types.Part.from_uri(file_uri="gs://cloud-samples-data/generative-ai/image/scones.jpg", mime_type="image/jpeg")

with open("local_image.jpg", "rb") as f:
    local_image = types.Part.from_bytes(data=f.read(), mime_type="image/jpeg")

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[
        "Generate a list of all the objects contained in both images.",
        gcs_image,
        local_image,
    ],
)
print(response.text)
```

### YouTube Videos
```python
from google import genai
from google.genai import types

client = genai.Client()
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=[
        types.Part.from_uri(
            file_uri="https://www.youtube.com/watch?v=3KtWfp0UopM",
            mime_type="video/mp4",
        ),
        "Write a short and engaging blog post based on this video.",
    ],
)
print(response.text)
```
```

