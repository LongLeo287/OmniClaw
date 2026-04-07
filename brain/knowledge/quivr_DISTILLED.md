---
id: quivr
type: knowledge
owner: OA_Triage
---
# quivr
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# Quivr - Your Second Brain, Empowered by Generative AI

<div align="center">
    <img src="./logo.png" alt="Quivr-logo" width="31%"  style="border-radius: 50%; padding-bottom: 20px"/>
</div>

[![Discord Follow](https://dcbadge.vercel.app/api/server/HUpRgp2HG8?style=flat)](https://discord.gg/HUpRgp2HG8)
[![GitHub Repo stars](https://img.shields.io/github/stars/quivrhq/quivr?style=social)](https://github.com/quivrhq/quivr)
[![Twitter Follow](https://img.shields.io/twitter/follow/StanGirard?style=social)](https://twitter.com/_StanGirard)

Quivr, helps you build your second brain, utilizes the power of GenerativeAI to be your personal assistant !

## Key Features 🎯

- **Opiniated RAG**: We created a RAG that is opinionated, fast and efficient so you can focus on your product
- **LLMs**: Quivr works with any LLM, you can use it with OpenAI, Anthropic, Mistral, Gemma, etc.
- **Any File**: Quivr works with any file, you can use it with PDF, TXT, Markdown, etc and even add your own parsers.
- **Customize your RAG**: Quivr allows you to customize your RAG, add internet search, add tools, etc.
- **Integrations with Megaparse**: Quivr works with [Megaparse](https://github.com/quivrhq/megaparse), so you can ingest your files with Megaparse and use the RAG with Quivr.

>We take care of the RAG so you can focus on your product. Simply install quivr-core and add it to your project. You can now ingest your files and ask questions.*

**We will be improving the RAG and adding more features, stay tuned!**


This is the core of Quivr, the brain of Quivr.com.

<!-- ## Demo Highlight 🎥

https://github.com/quivrhq/quivr/assets/19614572/a6463b73-76c7-4bc0-978d-70562dca71f5 -->

## Getting Started 🚀

You can find everything on the [documentation](https://core.quivr.com/).

### Prerequisites 📋

Ensure you have the following installed:

- Python 3.10 or newer

### 30 seconds Installation 💽


- **Step 1**: Install the package

  

  ```bash
  pip install quivr-core # Check that the installation worked
  ```


- **Step 2**: Create a RAG with 5 lines of code

  ```python
  import tempfile

  from quivr_core import Brain

  if __name__ == "__main__":
      with tempfile.NamedTemporaryFile(mode="w", suffix=".txt") as temp_file:
          temp_file.write("Gold is a liquid of blue-like colour.")
          temp_file.flush()

          brain = Brain.from_files(
              name="test_brain",
              file_paths=[temp_file.name],
          )

          answer = brain.ask(
              "what is gold? asnwer in french"
          )
          print("answer:", answer)
  ```
## Configuration

### Workflows

#### Basic RAG

![](docs/docs/workflows/examples/basic_rag.excalidraw.png)


Creating a basic RAG workflow like the one above is simple, here are the steps:


1. Add your API Keys to your environment variables
```python
import os
os.environ["OPENAI_API_KEY"] = "myopenai_apikey"

```
Quivr supports APIs from Anthropic, OpenAI, and Mistral. It also supports local models using Ollama.

1. Create the YAML file ``basic_rag_workflow.yaml`` and copy the following content in it
```yaml
workflow_config:
  name: "standard RAG"
  nodes:
    - name: "START"
      edges: ["filter_history"]

    - name: "filter_history"
      edges: ["rewrite"]

    - name: "rewrite"
      edges: ["retrieve"]

    - name: "retrieve"
      edges: ["generate_rag"]

    - name: "generate_rag" # the name of the last node, from which we want to stream the answer to the user
      edges: ["END"]

# Maximum number of previous conversation iterations
# to include in the context of the answer
max_history: 10

# Reranker configuration
reranker_config:
  # The reranker supplier to use
  supplier: "cohere"

  # The model to use for the reranker for the given supplier
  model: "rerank-multilingual-v3.0"

  # Number of chunks returned by the reranker
  top_n: 5

# Configuration for the LLM
llm_config:

  # maximum number of tokens passed to the LLM to generate the answer
  max_input_tokens: 4000

  # temperature for the LLM
  temperature: 0.7
```

3. Create a Brain with the default configuration
```python
from quivr_core import Brain

brain = Brain.from_files(name = "my smart brain",
                        file_paths = ["./my_first_doc.pdf", "./my_second_doc.txt"],
                        )

```

4. Launch a Chat
```python
brain.print_info()

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from quivr_core.config import RetrievalConfig

config_file_name = "./basic_rag_workflow.yaml"

retrieval_config = RetrievalConfig.from_yaml(config_file_name)

console = Console()
console.print(Panel.fit("Ask your brain !", style="bold magenta"))

while True:
    # Get user input
    question = Prompt.ask("[bold cyan]Question[/bold cyan]")

    # Check if user wants to exit
    if question.lower() == "exit":
        console.print(Panel("Goodbye!", style="bold yellow"))
        break

    answer = brain.ask(question, retrieval_config=retrieval_config)
    # Print the answer with typing effect
    console.print(f"[bold green]Quivr Assistant[/bold green]: {answer.answer}")

    console.print("-" * console.width)

brain.print_info()
```

5. You are now all set up to talk with your brain and test different retrieval strategies by simply changing the configuration file!

## Go further

You can go further with Quivr by adding internet search, adding tools, etc. Check the [documentation](https://core.quivr.com/) for more information.


## Contributors ✨

Thanks go to these wonderful people:
<a href="https://github.com/quivrhq/quivr/graphs/contributors">
<img src="https://contrib.rocks/image?repo=quivrhq/quivr" />
</a>

## Contribute 🤝

Did you get a pull request? Open it, and we'll review it as soon as possible. Check out our project board [here](https://github.com/users/StanGirard/projects/5) to see what we're currently focused on, and feel free to bring your fresh ideas to the table!

- [Open Issues](https://github.com/quivrhq/quivr/issues)
- [Open Pull Requests](https://github.com/quivrhq/quivr/pulls)
- [Good First Issues](https://github.com/quivrhq/quivr/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22)

## Partners ❤️

This project would not be possible without the support of our partners. Thank you for your support!


<a href="https://ycombinator.com/">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Y_Combinator_logo.svg/1200px-Y_Combinator_logo.svg.png" alt="YCombinator" style="padding: 10px" width="70px">
</a>
<a href="https://www.theodo.fr/">
  <img src="https://avatars.githubusercontent.com/u/332041?s=200&v=4" alt="Theodo" style="padding: 10px" width="70px">
</a>

## License 📄

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details

```

### File: core\README.md
```md
# quivr-core package

The RAG of Quivr.com

## License 📄

This project is licensed under the Apache 2.0 License

## Installation

```bash
pip install quivr-core
```





```

### File: docs\README.md
```md
# docs

Describe your project here.

```

### File: .pre-commit-config.yaml
```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.6.0
    hooks:
      - id: check-added-large-files
        args: ["--maxkb=5000"]
      - id: check-toml
      - id: check-yaml
      - id: end-of-file-fixer
      - id: trailing-whitespace
      - id: check-merge-conflict
      - id: detect-private-key
      - id: check-case-conflict
  - repo: https://github.com/pre-commit/pre-commit
    rev: v3.6.2
    hooks:
      - id: validate_manifest
  - repo: https://github.com/astral-sh/ruff-pre-commit
    # Ruff version.
    rev: v0.5.1
    hooks:
      # Run the linter.
      - id: ruff
        args: [--fix, --isolated]
        additional_dependencies: []
      # Run the formatter.
      - id: ruff-format
        args: [--isolated]
        additional_dependencies: []
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.10.1
    hooks:
      - id: mypy
        name: mypy
        args: ["--ignore-missing-imports", "--no-incremental", "--follow-imports=skip"]
        additional_dependencies: ["types-aiofiles", "types-pyyaml", "pydantic", "sqlmodel"]
ci:
  autofix_commit_msg: |
    [pre-commit.ci] auto fixes from pre-commit.com hooks

    for more information, see https://pre-commit.ci
  autofix_prs: true
  autoupdate_branch: ""
  autoupdate_commit_msg: "[pre-commit.ci] pre-commit autoupdate"
  autoupdate_schedule: weekly
  skip: []
  submodules: false

```

### File: .readthedocs.yaml
```yaml
# Read the Docs configuration file for MkDocs projects
# See https://docs.readthedocs.io/en/stable/config-file/v2.html for details

# Required
version: 2

# Set the version of Python and other tools you might need
build:
  os: ubuntu-22.04
  tools:
    python: "3.11"
  commands:
    - asdf plugin add uv
    - asdf install uv latest
    - asdf global uv latest
    - uv venv
    - cd docs && UV_INDEX_STRATEGY=unsafe-first-match uv pip install -r requirements.lock
    - cd docs/ && ls -la && NO_COLOR=1 ../.venv/bin/mkdocs build --strict --site-dir $READTHEDOCS_OUTPUT/html --config-file mkdocs.yml

  


mkdocs:
  configuration: backend/docs/mkdocs.yml


```

### File: .release-please-manifest.json
```json
{
    "core": "0.0.33"
}
```

### File: CHANGELOG.md
```md
# Changelog

## 0.0.322 (2024-10-15)

## What's Changed
* feat: Add new documentation files by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3351
* fix: separate english and french ingredients by @chloedia in https://github.com/QuivrHQ/quivr/pull/3358
* docs(core): init by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3365
* docs: quivr core storage by @AmineDiro in https://github.com/QuivrHQ/quivr/pull/3366
* fix: fixing pdf parsing by @jacopo-chevallard in https://github.com/QuivrHQ/quivr/pull/3349
* feat: Improve user credit calculation in get_user_credits by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3367
* fix unwanted parsing effect by @chloedia in https://github.com/QuivrHQ/quivr/pull/3371
* add fallback on llamaparse by @chloedia in https://github.com/QuivrHQ/quivr/pull/3374


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.321...v0.0.322

## 0.0.321 (2024-10-08)

## What's Changed
* feat: Add file name to knowledge properties in crawl_endpoint by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3346
* feat(frontend): add xlsx by @Zewed in https://github.com/QuivrHQ/quivr/pull/3340


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.320...v0.0.321

## 0.0.320 (2024-10-07)

## What's Changed
* Enable Porter Application cdp by @porter-deployment-app in https://github.com/QuivrHQ/quivr/pull/3306
* Enable Porter Application cdp-front by @porter-deployment-app in https://github.com/QuivrHQ/quivr/pull/3307
* feat(assistant): cdp by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3305
* feat: Add debug logging for OCR results by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3309
* feat: Update OCR image scale for better accuracy by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3310
* feat: Update PDFGenerator to include logo in header by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3311
* feat: structlog parseable by @AmineDiro in https://github.com/QuivrHQ/quivr/pull/3312
* Revert "feat: structlog parseable" by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3313
* feat: structlog parseable by @AmineDiro in https://github.com/QuivrHQ/quivr/pull/3314
* Revert "feat: structlog parseable" by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3315
* feat: Update PDFGenerator to include logo in header by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3318
* feat: structlog parseable by @AmineDiro in https://github.com/QuivrHQ/quivr/pull/3319
* feat: Update knowledge status and send notification on task success by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3320
* feat: Update text retranscription instructions by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3321
* feat: update sentry by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3326
* chore: Remove unnecessary assertion in create_modification_report function by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3329
* chore: Add NEXT_PUBLIC_INTERCOM_APP_ID to Dockerfile by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3330
* feat: Update Content Security Policy for PostHog by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3331
* fix(cdp): order naming cdc_etiquette by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3333
* fix(notifications): added a debouncing mechanism by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3327


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.319...v0.0.320

## 0.0.319 (2024-10-01)

## What's Changed
* feat: Add error handling for rate-limited search in fetch_notion_pages by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3298
* feat: Remove syncNotion from ConnectionCards by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3300


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.318...v0.0.319

## 0.0.318 (2024-09-30)

## What's Changed
* feat: add syncNotion from ConnectionCards by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3292


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.317...v0.0.318

## 0.0.317 (2024-09-30)

## What's Changed
* feat: update SyncsUser status field to be optional by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3284
* fix(frontend): onboarding modal by @Zewed in https://github.com/QuivrHQ/quivr/pull/3286
* feat: Remove syncNotion from ConnectionCards by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3289


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.316...v0.0.317

## 0.0.316 (2024-09-30)

## What's Changed
* fix(core): enforce langchain <0.3 for pydantic v1 by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3217
* chore(main): release core 0.0.16 by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3218
* feat(assistants): mock api by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3195
* chore(examples): fix chainlit example  by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3223
* feat(integration): Notion by @chloedia in https://github.com/QuivrHQ/quivr/pull/3173
* fix(migration): order migrations by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3231
* feat: remove n+1 query knowledge by @AmineDiro in https://github.com/QuivrHQ/quivr/pull/3238
* feat: introducing configurable retrieval workflows by @jacopo-chevallard in https://github.com/QuivrHQ/quivr/pull/3227
* fix: wrong default path for CHAT_LLM_CONFIG_PATH env variable by @jacopo-chevallard in https://github.com/QuivrHQ/quivr/pull/3247
* fix(frontend): sync folder for premium users by @Zewed in https://github.com/QuivrHQ/quivr/pull/3251
* fix: correctly passing the prompt provided by the user by @jacopo-chevallard in https://github.com/QuivrHQ/quivr/pull/3252
* fix: add sync user id aget_files by @AmineDiro in https://github.com/QuivrHQ/quivr/pull/3261
* feat: update sync_user.py to include sync user id in aget_files call by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3276
* chore: update Dockerfile dependencies and copy files by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3277
* chore: add wget to Dockerfile dependencies by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3279


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.315...v0.0.316

## 0.0.315 (2024-09-17)

## What's Changed
* chore(main): release core 0.0.15 by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3203
* fix: knowledge user_id fix by @AmineDiro in https://github.com/QuivrHQ/quivr/pull/3216


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.314...v0.0.315

## 0.0.314 (2024-09-16)

## What's Changed
* feat:  CRUD KMS (no syncs)  by @AmineDiro in https://github.com/QuivrHQ/quivr/pull/3162


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.313...v0.0.314

## 0.0.313 (2024-09-13)

## What's Changed
* feat: save and load brain by @AmineDiro in https://github.com/QuivrHQ/quivr/pull/3202


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.312...v0.0.313

## 0.0.312 (2024-09-13)

## What's Changed
* fix: Update LLMEndpoint to include max_tokens parameter by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3201


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.311...v0.0.312

## 0.0.311 (2024-09-12)

## What's Changed
* chore(embeddings): added tests for embeddings by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3183
* feat(uptime): check if connection to db works by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3199


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.310...v0.0.311

## 0.0.310 (2024-09-10)

## What's Changed
* feat: Add Azure OpenAI embeddings support by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3182


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.309...v0.0.310

## 0.0.309 (2024-09-10)

## What's Changed
* chore: Add initial documentation files and configuration by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3126
* chore: Add .readthedocs.yaml configuration file by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3172
* fix(frontend): notion integration in front end by @Zewed in https://github.com/QuivrHQ/quivr/pull/3175
* chore(main): release core 0.0.14 by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2945
* ci(rye): now core is built with rye by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3177
* feat: Add external Supabase URL support for generating file signed URL by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3179
* fix(onboarding): keeps setting it at false by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3180


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.308...v0.0.309

## 0.0.308 (2024-09-06)

## What's Changed
* fix: remove knowledge and idle conn by @AmineDiro in https://github.com/QuivrHQ/quivr/pull/3165


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.307...v0.0.308

## 0.0.307 (2024-09-06)

## What's Changed
* fix: tests pytest-asyncio by @AmineDiro in https://github.com/QuivrHQ/quivr/pull/3157
* fix: remove unused 'models' field in check_premium.py by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3164


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.306...v0.0.307

## 0.0.306 (2024-09-05)

## What's Changed
* feat(readme): trigger deploy by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3159


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.305...v0.0.306

## 0.0.305 (2024-09-05)

## What's Changed
* chore: update next.config.js with PostHog domains by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3155


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.304...v0.0.305

## 0.0.304 (2024-09-05)

## What's Changed
* feat: update Azure login button text by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3152
* fix: url knowledge multiple brain by @AmineDiro in https://github.com/QuivrHQ/quivr/pull/3145
* chore: update Dockerfile with PostHog environment variables by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3154


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.303...v0.0.304

## 0.0.303 (2024-09-04)

## What's Changed
* fix(chat): order of chat history was reversed by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3148


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.302...v0.0.303

## 0.0.302 (2024-09-04)

## What's Changed
* feat(anthropic): add llm by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3146


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.301...v0.0.302

## 0.0.301 (2024-09-03)

## What's Changed
* feat(smtp): not enforcing tls by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3067
* feat: Update send_email.py to conditionally login with SMTP credentials by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3069
* feat: Add NEXT_PUBLIC_PROJECT_NAME environment variable by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3070
* feat: Add Azure login support by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3071
* fix(frontend): only owner can access knowledge and edit brain snippet by @Zewed in https://github.com/QuivrHQ/quivr/pull/3073
* fix(frontend): brain knowledge visibility by @Zewed in https://github.com/QuivrHQ/quivr/pull/3074
* fix(frontend): revamp of settings  by @Zewed in https://github.com/QuivrHQ/quivr/pull/3081
* fix: Update README.md by @Zewed in https://github.com/QuivrHQ/quivr/pull/3084
* fix(frontend): send invitation clearer by @Zewed in https://github.com/QuivrHQ/quivr/pull/3090
* fix(frontend): spacing chats by @Zewed in https://github.com/QuivrHQ/quivr/pull/3091
* fix(frontend): use click delay by @Zewed in https://github.com/QuivrHQ/quivr/pull/3092
* fix(frontend): back buttons by @Zewed in https://github.com/QuivrHQ/quivr/pull/3094
* fix(frontend): change hover delay for tooltips by @Zewed in https://github.com/QuivrHQ/quivr/pull/3095
* fix(frontend): rename search by thread by @Zewed in https://github.com/QuivrHQ/quivr/pull/3099
* feat(frontend): revamp of some basics components by @Zewed in https://github.com/QuivrHQ/quivr/pull/3105
* feat(frontend): interaction with brain items by @Zewed in https://github.com/QuivrHQ/quivr/pull/3106
* fix(frontend): remove intercom on thread page of mobile by @Zewed in https://github.com/QuivrHQ/quivr/pull/3108
* feat:  quivr core 0.1 by @StanGirard in https://github.com/QuivrHQ/quivr/pull/2970
* fix: Blank scrollbar on certain browsers by @adityanandanx in https://github.com/QuivrHQ/quivr/pull/3118
* chore(docs): moved repository by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3123
* fix: knowledge user by @AmineDiro in https://github.com/QuivrHQ/quivr/pull/3124
* chore(readme): increase size icon by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3125
* chore: remove unused syncNotion function in ConnectionCards.tsx by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3129
* chore: update compatibility by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3136
* ci(raise): only on tags by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3140
* feat: using langgraph in our RAG pipeline by @jacopo-chevallard in https://github.com/QuivrHQ/quivr/pull/3130
* fix: knowledge multiple brains by @AmineDiro in https://github.com/QuivrHQ/quivr/pull/3142
* fix: knowledge multiple brains - update knowledge rollback by @AmineDiro in https://github.com/QuivrHQ/quivr/pull/3143

## New Contributors
* @jacopo-chevallard made their first contribution in https://github.com/QuivrHQ/quivr/pull/3130

**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.300...v0.0.301

## 0.0.300 (2024-08-22)

## What's Changed
* feat(smtp&share): implemented smtp support and fixed share brain by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3049


**Full Changelog**: https://github.com/QuivrHQ/quivr/compare/v0.0.299...v0.0.300

## 0.0.299 (2024-08-22)

## What's Changed
* fix: Update Supabase configuration by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3014
* Delete Porter Application theodo-backend by @porter-deployment-app in https://github.com/QuivrHQ/quivr/pull/3022
* Delete Porter Application theodo-frontend by @porter-deployment-app in https://github.com/QuivrHQ/quivr/pull/3023
* feat(frontend): emoji selector component by @Zewed in https://github.com/QuivrHQ/quivr/pull/3024
* feat(frontend): show or hide tokens relative stuff by @Zewed in https://github.com/QuivrHQ/quivr/pull/3017
* feat(frontend): color picker by @Zewed in https://github.com/QuivrHQ/quivr/pull/3027
* fix(frontend): small stuff on mobile by @Zewed in https://github.com/QuivrHQ/quivr/pull/3039
* feat(frontend): handle LaTeX in message thread by @Zewed in https://github.com/QuivrHQ/quivr/pull/3040
* fix(frontend): fix docker build frontend new env by @StanGirard in https://github.com/QuivrHQ/quivr/pull/3041
* feat(frontend): brain snippet selector by @Zewed in https://github.com/Quivr
... [TRUNCATED]
```

### File: release-please-config.json
```json
{
    "packages": {
        "core": {
            "release-type": "python",
            "package-name": "core",
            "bump-patch-for-minor-pre-major": true,
            "include-v-in-tag": false,
            "tag-separator": "-",
            "component": "core"
        }
    }
}
```

### File: vercel.json
```json
{
    "git": {
        "deploymentEnabled": {
            "main": false
        }
    }
}
```

### File: .github\PULL_REQUEST_TEMPLATE.md
```md
# Description

Please include a summary of the changes and the related issue. Please also include relevant motivation and context.

## Checklist before requesting a review

Please delete options that are not relevant.

- [ ] My code follows the style guidelines of this project
- [ ] I have performed a self-review of my code
- [ ] I have commented hard-to-understand areas
- [ ] I have ideally added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes
- [ ] Any dependent changes have been merged

## Screenshots (if appropriate):

```

### File: core\CHANGELOG.md
```md
# Changelog

## [0.0.33](https://github.com/QuivrHQ/quivr/compare/core-0.0.32...core-0.0.33) (2025-02-03)


### Features

* **zendesk:** add zendesk workflow ([#3586](https://github.com/QuivrHQ/quivr/issues/3586)) ([ee9b7a5](https://github.com/QuivrHQ/quivr/commit/ee9b7a5740825bd3fc9186e0a9179959c6525e5e))


### Bug Fixes

* CLI-24 ([ee9b7a5](https://github.com/QuivrHQ/quivr/commit/ee9b7a5740825bd3fc9186e0a9179959c6525e5e))

## [0.0.32](https://github.com/QuivrHQ/quivr/compare/core-0.0.31...core-0.0.32) (2025-01-31)


### Features

* o3-mini ([#3583](https://github.com/QuivrHQ/quivr/issues/3583)) ([a639e0c](https://github.com/QuivrHQ/quivr/commit/a639e0ce50297e0fefa809b7edb57b50863b446d))

## [0.0.31](https://github.com/QuivrHQ/quivr/compare/core-0.0.30...core-0.0.31) (2025-01-30)


### Features

* cache tokenizers ([#3558](https://github.com/QuivrHQ/quivr/issues/3558)) ([699dc2e](https://github.com/QuivrHQ/quivr/commit/699dc2e187abc9986845f591111723088f5bcefe))
* limit tokenizers cache size ([#3577](https://github.com/QuivrHQ/quivr/issues/3577)) ([e2a3bcb](https://github.com/QuivrHQ/quivr/commit/e2a3bcbbdb469348187d986de9ba3901938bed58))
* remove pympler dependency and add better way to calculate size of tokenizer cache ([#3580](https://github.com/QuivrHQ/quivr/issues/3580)) ([2fbd5d4](https://github.com/QuivrHQ/quivr/commit/2fbd5d48443625dd3fe8a37c04275cd760e7285f))
* remove tokenizer load ([#3576](https://github.com/QuivrHQ/quivr/issues/3576)) ([05e212a](https://github.com/QuivrHQ/quivr/commit/05e212a30929ba3c00e31e3364363eb4a4376ad9))

## [0.0.30](https://github.com/QuivrHQ/quivr/compare/core-0.0.29...core-0.0.30) (2025-01-27)


### Features

* adding cache to LLMEndpoint ([#3555](https://github.com/QuivrHQ/quivr/issues/3555)) ([6072907](https://github.com/QuivrHQ/quivr/commit/6072907ca7370be748d2d6845fd674abbb6c83c3))

## [0.0.29](https://github.com/QuivrHQ/quivr/compare/core-0.0.28...core-0.0.29) (2025-01-20)


### Features

* enabling workflows without rewriting step ([#3549](https://github.com/QuivrHQ/quivr/issues/3549)) ([bbe1c18](https://github.com/QuivrHQ/quivr/commit/bbe1c183768bf32945554e679cab737c07bb3dde))
* improving the prompts to always refer to 'tasks' instead of 'questions' ([#3528](https://github.com/QuivrHQ/quivr/issues/3528)) ([e9c72e1](https://github.com/QuivrHQ/quivr/commit/e9c72e15671407290f1a3a9758bf38a3357d2b15))
* langfuse integration ([#3530](https://github.com/QuivrHQ/quivr/issues/3530)) ([c4aae1a](https://github.com/QuivrHQ/quivr/commit/c4aae1a6c21fd7bc7019676d32fa5b2e8fbbe171))
* langfuse user id ([#3533](https://github.com/QuivrHQ/quivr/issues/3533)) ([e0ccd3d](https://github.com/QuivrHQ/quivr/commit/e0ccd3dc04b7527b27520465b2cf179e9789bf3f))
* language detection after chunking ([#3532](https://github.com/QuivrHQ/quivr/issues/3532)) ([d0adb81](https://github.com/QuivrHQ/quivr/commit/d0adb8112a27fb7f25564d328a6f7e50ba27ba3a))
* returning a description of each workflow node ([#3539](https://github.com/QuivrHQ/quivr/issues/3539)) ([d835fc6](https://github.com/QuivrHQ/quivr/commit/d835fc6e4c062bd485a715bc707a902493e092c2))


### Bug Fixes

* langfuse talk to model ([#3535](https://github.com/QuivrHQ/quivr/issues/3535)) ([9681a9e](https://github.com/QuivrHQ/quivr/commit/9681a9ec8b6b09fe20d04bf41d17a57afc5398f9))

## [0.0.28](https://github.com/QuivrHQ/quivr/compare/core-0.0.27...core-0.0.28) (2024-12-17)


### Features

* remove dependencies on Pydantic v1 ([#3526](https://github.com/QuivrHQ/quivr/issues/3526)) ([ebc4eb8](https://github.com/QuivrHQ/quivr/commit/ebc4eb811c258ce0500032bbc52d96f333fabf89))

## [0.0.27](https://github.com/QuivrHQ/quivr/compare/core-0.0.26...core-0.0.27) (2024-12-16)


### Features

* ensuring that max_context_tokens is never larger than what supported by models ([#3519](https://github.com/QuivrHQ/quivr/issues/3519)) ([d6e0ed4](https://github.com/QuivrHQ/quivr/commit/d6e0ed44df0ee7edafea85f704a15fd99969bafd))
* send all to megaparse_sdk ([#3521](https://github.com/QuivrHQ/quivr/issues/3521)) ([e48044d](https://github.com/QuivrHQ/quivr/commit/e48044d36ffda613f65da24641ed8da290195177))


### Bug Fixes

* fixing errors arising when the user input contains no tasks ([#3525](https://github.com/QuivrHQ/quivr/issues/3525)) ([e28f7bc](https://github.com/QuivrHQ/quivr/commit/e28f7bcb9ab9534bc011664525ae1f9c2cf6393e))

## [0.0.26](https://github.com/QuivrHQ/quivr/compare/core-0.0.25...core-0.0.26) (2024-12-10)


### Features

* first version (V0) of the Workflow Management System ([#3493](https://github.com/QuivrHQ/quivr/issues/3493)) ([6450a49](https://github.com/QuivrHQ/quivr/commit/6450a494e3efa8e8c267ca49aa0a7ec682586b4e))


### Bug Fixes

* dealing with empty tool_calls ([#3514](https://github.com/QuivrHQ/quivr/issues/3514)) ([e2f6389](https://github.com/QuivrHQ/quivr/commit/e2f6389189d911a382b2236ab39f28a1270528ac))

## [0.0.25](https://github.com/QuivrHQ/quivr/compare/core-0.0.24...core-0.0.25) (2024-11-28)


### Bug Fixes

* megaparse sdk with nats ([#3496](https://github.com/QuivrHQ/quivr/issues/3496)) ([e68b4f4](https://github.com/QuivrHQ/quivr/commit/e68b4f45698898f6b514d4779c8e5fd7332f2e67))


### Documentation

* Enhance example/chatbot with added instructions ([#3506](https://github.com/QuivrHQ/quivr/issues/3506)) ([d1d608d](https://github.com/QuivrHQ/quivr/commit/d1d608d19ffb9213910575981eff3527f7d232a0))

## [0.0.24](https://github.com/QuivrHQ/quivr/compare/core-0.0.23...core-0.0.24) (2024-11-14)


### Features

* kms-migration ([#3446](https://github.com/QuivrHQ/quivr/issues/3446)) ([1356d87](https://github.com/QuivrHQ/quivr/commit/1356d87098ae84776a5d47b631d07a1c8e92e291))
* **megaparse:** add sdk ([#3462](https://github.com/QuivrHQ/quivr/issues/3462)) ([190d971](https://github.com/QuivrHQ/quivr/commit/190d971bd71333924b88ba747d3c6a833ca65d92))


### Bug Fixes

* added chunk_size in tika processor ([#3466](https://github.com/QuivrHQ/quivr/issues/3466)) ([063bbd3](https://github.com/QuivrHQ/quivr/commit/063bbd323dfca2dfc22fc5416c1617ed61d2e2ab))
* modify megaparse strategy ([#3474](https://github.com/QuivrHQ/quivr/issues/3474)) ([da97b2c](https://github.com/QuivrHQ/quivr/commit/da97b2cf145c86ed577be698ae837b3dc26f6921))
* supported extensions for megaparse ([#3477](https://github.com/QuivrHQ/quivr/issues/3477)) ([72b979d](https://github.com/QuivrHQ/quivr/commit/72b979d4e4d6e6efc45d47c7aba942eb909adc3e))

## [0.0.23](https://github.com/QuivrHQ/quivr/compare/core-0.0.22...core-0.0.23) (2024-10-31)


### Features

* websearch, tool use, user intent, dynamic retrieval, multiple questions ([#3424](https://github.com/QuivrHQ/quivr/issues/3424)) ([285fe5b](https://github.com/QuivrHQ/quivr/commit/285fe5b96065a19c74f0314557e5840d8722099e))

## [0.0.22](https://github.com/QuivrHQ/quivr/compare/core-0.0.21...core-0.0.22) (2024-10-21)


### Features

* **ask:** non-streaming now calls streaming ([#3409](https://github.com/QuivrHQ/quivr/issues/3409)) ([e71e46b](https://github.com/QuivrHQ/quivr/commit/e71e46bcdfbab0d583aef015604278343fd46c6f))

## [0.0.21](https://github.com/QuivrHQ/quivr/compare/core-0.0.20...core-0.0.21) (2024-10-21)


### Features

* **ci:** trigger ([b92774a](https://github.com/QuivrHQ/quivr/commit/b92774aa37ad2051b197daa29fe4b94d57a19986))

## [0.0.20](https://github.com/QuivrHQ/quivr/compare/core-0.0.19...core-0.0.20) (2024-10-21)


### Features

* **ci:** trigger ([#3403](https://github.com/QuivrHQ/quivr/issues/3403)) ([68c09fc](https://github.com/QuivrHQ/quivr/commit/68c09fce85364432da2641d0a8da867516142553))
* **docs:** trigger ci ([5644596](https://github.com/QuivrHQ/quivr/commit/56445967252eac20d17bebc4484d7c00c45d9238))

## [0.0.19](https://github.com/QuivrHQ/quivr/compare/core-0.0.18...core-0.0.19) (2024-10-21)


### Features

* **quivr-core:** beginning ([#3388](https://github.com/QuivrHQ/quivr/issues/3388)) ([7acb52a](https://github.com/QuivrHQ/quivr/commit/7acb52a9637b74d53f3e4cc9dde4ae1ca3f481ad))

## [0.0.18](https://github.com/QuivrHQ/quivr/compare/core-0.0.17...core-0.0.18) (2024-10-16)


### Bug Fixes

* **core:** megaparse config ([#3384](https://github.com/QuivrHQ/quivr/issues/3384)) ([ffe86ca](https://github.com/QuivrHQ/quivr/commit/ffe86ca7bac3d7800913937314170db6f91daf8e))

## [0.0.17](https://github.com/QuivrHQ/quivr/compare/core-0.0.16...core-0.0.17) (2024-10-16)


### Features

* **assistant:** cdp ([#3305](https://github.com/QuivrHQ/quivr/issues/3305)) ([b767f19](https://github.com/QuivrHQ/quivr/commit/b767f19f28b5478cef077b5d1587bf5195f2a668))
* **assistants:** mock api ([#3195](https://github.com/QuivrHQ/quivr/issues/3195)) ([282fa0e](https://github.com/QuivrHQ/quivr/commit/282fa0e3f83f7c6fc8c84ca95f8f4ced4ed34b78))
* introducing configurable retrieval workflows ([#3227](https://github.com/QuivrHQ/quivr/issues/3227)) ([ef90e8e](https://github.com/QuivrHQ/quivr/commit/ef90e8e672ca23d104c7d5bde7496f0929adf5d2))


### Bug Fixes

* fixing pdf parsing ([#3349](https://github.com/QuivrHQ/quivr/issues/3349)) ([367242a](https://github.com/QuivrHQ/quivr/commit/367242a3d5ea2df1928cb2908ad9e1906d1bba6f))


### Documentation

* **core:** init ([#3365](https://github.com/QuivrHQ/quivr/issues/3365)) ([bb572a2](https://github.com/QuivrHQ/quivr/commit/bb572a2a8d060f147461506aadd38704eb029a9a))
* **fix:** fixed warnings from griffe ([#3381](https://github.com/QuivrHQ/quivr/issues/3381)) ([1a38798](https://github.com/QuivrHQ/quivr/commit/1a3879839a2d9e0881e18cb66809564fb76724ef))

## [0.0.16](https://github.com/QuivrHQ/quivr/compare/core-0.0.15...core-0.0.16) (2024-09-17)


### Bug Fixes

* **core:** enforce langchain &lt;0.3 for pydantic v1 ([#3217](https://github.com/QuivrHQ/quivr/issues/3217)) ([4bb4800](https://github.com/QuivrHQ/quivr/commit/4bb4800a76942ee31a939d3cacc94f057682177a))

## [0.0.15](https://github.com/QuivrHQ/quivr/compare/core-0.0.14...core-0.0.15) (2024-09-16)


### Features

* CRUD KMS (no syncs)  ([#3162](https://github.com/QuivrHQ/quivr/issues/3162)) ([71edca5](https://github.com/QuivrHQ/quivr/commit/71edca572ffd2901ed582005ac4b2803d9d95e57))
* save and load brain ([#3202](https://github.com/QuivrHQ/quivr/issues/3202)) ([eda619f](https://github.com/QuivrHQ/quivr/commit/eda619f4547921ab4c50458b2d44c6b5c10e40d1))


### Bug Fixes

* Update LLMEndpoint to include max_tokens parameter ([#3201](https://github.com/QuivrHQ/quivr/issues/3201)) ([13ed225](https://github.com/QuivrHQ/quivr/commit/13ed225b172407ee9826b9c01b2f7b124a8b5a10))

## [0.0.14](https://github.com/QuivrHQ/quivr/compare/core-0.0.13...core-0.0.14) (2024-09-09)


### Features

* Add brain_id and brain_name to ChatLLMMetadata model ([#2968](https://github.com/QuivrHQ/quivr/issues/2968)) ([1112001](https://github.com/QuivrHQ/quivr/commit/111200184b66dc42d75996c6c286474e9c5f8462))
* add chat with models ([#2933](https://github.com/QuivrHQ/quivr/issues/2933)) ([fccd197](https://github.com/QuivrHQ/quivr/commit/fccd197511d8594db257bfddf757bf0d28f7239d))
* Add get_model method to ModelRepository ([#2949](https://github.com/QuivrHQ/quivr/issues/2949)) ([13e9fc4](https://github.com/QuivrHQ/quivr/commit/13e9fc490bc62264de93d2efddf2389126c147fa))
* **anthropic:** add llm ([#3146](https://github.com/QuivrHQ/quivr/issues/3146)) ([8e29218](https://github.com/QuivrHQ/quivr/commit/8e2921886505cea0e72d2e1136a4b8ba862c3ce1))
* **azure:** quivr compatible with it ([#3005](https://github.com/QuivrHQ/quivr/issues/3005)) ([b5f31a8](https://github.com/QuivrHQ/quivr/commit/b5f31a83d4a1c4432943bbbaa0766c46927ef125))
* **frontend:** talk with models and handle code markdown ([#2980](https://github.com/QuivrHQ/quivr/issues/2980)) ([ef6037e](https://github.com/QuivrHQ/quivr/commit/ef6037e665f8d5e9c513d889773419a25f914d83))
* quivr core 0.1 ([#2970](https://github.com/QuivrHQ/quivr/issues/2970)) ([380cf82](https://github.com/QuivrHQ/quivr/commit/380cf8270678453c3dc14ac8665be9b3b5a49dce))
* using langgraph in our RAG pipeline ([#3130](https://github.com/QuivrHQ/quivr/issues/3130)) ([8cfdf53](https://github.com/QuivrHQ/quivr/commit/8cfdf53fe748b884cf44ade274503de3966b1378))


### Bug Fixes

* **chat:** order of chat history was reversed ([#3148](https://github.com/QuivrHQ/quivr/issues/3148)) ([7209500](https://github.com/QuivrHQ/quivr/commit/7209500d0bdaec544fce1e8e9082de3ead4464f4))

## [0.0.13](https://github.com/QuivrHQ/quivr/compare/core-0.0.12...core-0.0.13) (2024-08-01)


### Features

* quivr core tox test + parsers ([#2929](https://github.com/QuivrHQ/quivr/issues/2929)) ([6855585](https://github.com/QuivrHQ/quivr/commit/685558560cc431054fb9d1330c0e27ce5fdf1806))


### Bug Fixes

* processor quivr version ([#2934](https://github.com/QuivrHQ/quivr/issues/2934)) ([2d64962](https://github.com/QuivrHQ/quivr/commit/2d64962ca407d8f2c9e0faedc457548c3ff9921d))
* quivr core fix tests ([#2935](https://github.com/QuivrHQ/quivr/issues/2935)) ([d9c1f3a](https://github.com/QuivrHQ/quivr/commit/d9c1f3add48f354d92f3a21c03eca53add30a773))

## [0.0.12](https://github.com/QuivrHQ/quivr/compare/core-0.0.11...core-0.0.12) (2024-07-23)


### Features

* **dead-code:** removed composite & api ([#2902](https://github.com/QuivrHQ/quivr/issues/2902)) ([a2721d3](https://github.com/QuivrHQ/quivr/commit/a2721d3926df873e10817f948f8f10894ec6c581))
* **frontend:** add knowledge icon when integration ([#2888](https://github.com/QuivrHQ/quivr/issues/2888)) ([733d083](https://github.com/QuivrHQ/quivr/commit/733d083e330fc6e41c089bb9c9cf76289040cab9))

## [0.0.11](https://github.com/QuivrHQ/quivr/compare/core-0.0.10...core-0.0.11) (2024-07-22)


### Features

* move parsers quivr core ([#2884](https://github.com/QuivrHQ/quivr/issues/2884)) ([d3c53e6](https://github.com/QuivrHQ/quivr/commit/d3c53e63539bade5cbd716edf7e9af68ba15ed08))

## [0.0.10](https://github.com/QuivrHQ/quivr/compare/core-0.0.9...core-0.0.10) (2024-07-19)


### Features

* **frontend:** new notifications design ([#2870](https://github.com/QuivrHQ/quivr/issues/2870)) ([ed97004](https://github.com/QuivrHQ/quivr/commit/ed9700426959f3c1502a882263dfb447411d5381))
* **integrations:** dropbox ([#2864](https://github.com/QuivrHQ/quivr/issues/2864)) ([4806dc5](https://github.com/QuivrHQ/quivr/commit/4806dc5809aec9f7f573cb5adddac0e2d0ba600b))
* quivr core brain info + processors registry +  ([#2877](https://github.com/QuivrHQ/quivr/issues/2877)) ([3001fa1](https://github.com/QuivrHQ/quivr/commit/3001fa1475cf119a8b41a176f735f5402f708738))


### Bug Fixes

* Refacto & update dropbox refresh ([#2875](https://github.com/QuivrHQ/quivr/issues/2875)) ([3b68855](https://github.com/QuivrHQ/quivr/commit/3b68855a83c72f3e31c117af0434330383a8a5d7))

## [0.0.9](https://github.com/QuivrHQ/quivr/compare/core-0.0.8...core-0.0.9) (2024-07-15)


### Features

* quivr api use quivr core ([#2868](https://github.com/QuivrHQ/quivr/issues/2868)) ([9d3e9ed](https://github.com/QuivrHQ/quivr/commit/9d3e9edfd2ef24397458cc6556f6080673be96ae))


### Bug Fixes

* quiv core stream duplicate  and quivr-core rag tests ([#2852](https://github.com/QuivrHQ/quivr/issues/2852)) ([35eb07f](
... [TRUNCATED]
```

### File: examples\pdf_document_from_yaml.py
```py
import asyncio
import logging
import os
from pathlib import Path

import dotenv
from quivr_core import Brain
from quivr_core.rag.entities.config import AssistantConfig
from rich.traceback import install as rich_install

ConsoleOutputHandler = logging.StreamHandler()

logger = logging.getLogger("quivr_core")
logger.setLevel(logging.DEBUG)
logger.addHandler(ConsoleOutputHandler)


logger = logging.getLogger("megaparse")
logger.setLevel(logging.DEBUG)
logger.addHandler(ConsoleOutputHandler)


# Install rich's traceback handler to automatically format tracebacks
rich_install()


async def main():
    file_path = [
        Path("data/YamEnterprises_Monotype Fonts Plan License.US.en 04.0 (BLP).pdf")
    ]
    file_path = [
        Path(
            "data/YamEnterprises_Monotype Fonts Plan License.US.en 04.0 (BLP) reduced.pdf"
        )
    ]

    config_file_name = (
        "/Users/jchevall/Coding/quivr/backend/core/tests/rag_config_workflow.yaml"
    )

    assistant_config = AssistantConfig.from_yaml(config_file_name)
    # megaparse_config = find_nested_key(config, "megaparse_config")
    megaparse_config = assistant_config.ingestion_config.parser_config.megaparse_config
    megaparse_config.llama_parse_api_key = os.getenv("LLAMA_PARSE_API_KEY")

    processor_kwargs = {
        "megaparse_config": megaparse_config,
        "splitter_config": assistant_config.ingestion_config.parser_config.splitter_config,
    }

    brain = await Brain.afrom_files(
        name="test_brain",
        file_paths=file_path,
        processor_kwargs=processor_kwargs,
    )

    # # Check brain info
    brain.print_info()

    questions = [
        "What is the contact name for Yam Enterprises?",
        "What is the customer phone for Yam Enterprises?",
        "What is the Production Fonts (maximum) for Yam Enterprises?",
        "List the past use font software according to past use term for Yam Enterprises.",
        "How many unique Font Name are there in the Add-On Font Software Section for Yam Enterprises?",
        "What is the maximum number of Production Fonts allowed based on the license usage per term for Yam Enterprises?",
        "What is the number of production fonts licensed by Yam Enterprises? List them one by one.",
        "What is the number of Licensed Monthly Page Views for Yam Enterprises?",
        "What is the monthly licensed impressions (Digital Marketing Communications) for Yam Enterprises?",
        "What is the number of Licensed Applications for Yam Enterprises?",
        "For Yam Enterprises what is the number of applications aggregate Registered users?",
        "What is the number of licensed servers for Yam Enterprises?",
        "When is swap of Production Fonts available in Yam Enterprises?",
        "Who is the primary licensed monotype fonts user for Yam Enterprises?",
        "What is the number of Licensed Commercial Electronic Documents for Yam Enterprises?",
        "How many licensed monotype fonts users can Yam Enterprises have?",
        "How many licensed desktop users can Yam Enterprises have?",
        "Which contract type does Yam Enterprises follow?",
        "What monotype fonts support does Yam Enterprises have?",
        "Which monotype font services onboarding does Yam Enterprises have?",
        "Which Font/User Management does Yam Enterprises have?",
        "What Add-on inventory set did Yam Enterprises pick?",
        "Does Yam Enterprises have Single sign on?",
        "Is there Brand and Licence protection for Yam Enterprises?",
        "Who is the Third Party Payor's contact in Yam Enterprises?",
        "Does Yam Enterprises contract have Company Desktop License?",
        "What is the Number of Swaps Allowed for Yam Enterprises?",
        "When is swap of Production Fonts available in Yam Enterprises?",
    ]

    answers = [
        "Haruko Yamamoto",
        "81 90-1234-5603",
        "300 Production Fonts",
        "Helvetica Regular",
        "7",
        "300 Production Fonts",
        "Yam Enterprises has licensed a total of 105 Production Fonts.",
        "35,000,000",
        "2,500,000",
        "60",
        "40",
        "2",
        "Once per quarter",
        "Haruko Yamamoto",
        "0",
        "100",
        "60",
        "License",
        "Premier",
        "Premier",
        "Premier",
        "Plus",
        "Yes",
        "Yes",
        """
        Name: Yami Enterprises

        Contact: Mei Mei

        Address: 20-22 Tsuki-Tsuki-dori, Tokyo, Japan

        Phone: +81 71-9336-54023

        E-mail: mei.mei@example.com
        """,
        "Yes",
        "One (1) swap per calendar quarter",
        "The swap of Production Fonts will be available one (1) time per calendar quarter by removing Font Software as a Production Font and choosing other Font Software on the Monotype Fonts Platform.",
    ]

    retrieval_config = assistant_config.retrieval_config
    for i, (question, truth) in enumerate(zip(questions, answers, strict=False)):
        chunk = brain.ask(question=question, retrieval_config=retrieval_config)
        print(
            "\n Question: ", question, "\n Answer: ", chunk.answer, "\n Truth: ", truth
        )
        if i == 5:
            break


if __name__ == "__main__":
    dotenv.load_dotenv()

    # Run the main function in the existing event loop
    asyncio.run(main())

```

### File: examples\pdf_parsing_tika.py
```py
from langchain_core.embeddings import DeterministicFakeEmbedding
from langchain_core.language_models import FakeListChatModel
from quivr_core import Brain
from quivr_core.rag.entities.config import LLMEndpointConfig
from quivr_core.llm.llm_endpoint import LLMEndpoint
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

if __name__ == "__main__":
    brain = Brain.from_files(
        name="test_brain",
        file_paths=["tests/processor/data/dummy.pdf"],
        llm=LLMEndpoint(
            llm=FakeListChatModel(responses=["good"]),
            llm_config=LLMEndpointConfig(model="fake_model", llm_base_url="local"),
        ),
        embedder=DeterministicFakeEmbedding(size=20),
    )
    # Check brain info
    brain.print_info()

    console = Console()
    console.print(Panel.fit("Ask your brain !", style="bold magenta"))

    while True:
        # Get user input
        question = Prompt.ask("[bold cyan]Question[/bold cyan]")

        # Check if user wants to exit
        if question.lower() == "exit":
            console.print(Panel("Goodbye!", style="bold yellow"))
            break

        answer = brain.ask(question)
        # Print the answer with typing effect
        console.print(f"[bold green]Quivr Assistant[/bold green]: {answer.answer}")

        console.print("-" * console.width)

    brain.print_info()

```

### File: examples\save_load_brain.py
```py
import asyncio
import tempfile

from quivr_core import Brain


async def main():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".txt") as temp_file:
        temp_file.write("Gold is a liquid of blue-like colour.")
        temp_file.flush()

        brain = await Brain.afrom_files(name="test_brain", file_paths=[temp_file.name])

        save_path = await brain.save("/home/amine/.local/quivr")

        brain_loaded = Brain.load(save_path)
        brain_loaded.print_info()


if __name__ == "__main__":
    # Run the main function in the existing event loop
    asyncio.run(main())

```

### File: examples\simple_question_megaparse.py
```py
import os

from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from quivr_core import Brain
from quivr_core.llm.llm_endpoint import LLMEndpoint
from quivr_core.rag.entities.config import LLMEndpointConfig
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt

if __name__ == "__main__":
    brain = Brain.from_files(
        name="test_brain",
        file_paths=["./tests/processor/pdf/sample.pdf"],
        llm=LLMEndpoint(
            llm_config=LLMEndpointConfig(model="gpt-4o"),
            llm=ChatOpenAI(model="gpt-4o", api_key=str(os.getenv("OPENAI_API_KEY"))),
        ),
    )
    embedder = embeddings = OpenAIEmbeddings(
        model="text-embedding-3-large",
    )
    # Check brain info
    brain.print_info()

    console = Console()
    console.print(Panel.fit("Ask your brain !", style="bold magenta"))

    while True:
        # Get user input
        question = Prompt.ask("[bold cyan]Question[/bold cyan]")

        # Check if user wants to exit
        if question.lower() == "exit":
            console.print(Panel("Goodbye!", style="bold yellow"))
            break

        answer = brain.ask(question)
        # Print the answer with typing effect
        console.print(f"[bold green]Quivr Assistant[/bold green]: {answer.answer}")

        console.print("-" * console.width)

    brain.print_info()

```

### File: core\scripts\run_tests.sh
```sh
#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Constants
IMAGE_NAME="quivr-core-test"
IMAGE_TAG="latest"
DOCKERFILE="Dockerfile.test"
VOLUME_MAPPING="$PWD:/code"
TOX_DIR="/code/.tox-docker"
CMD="poetry run tox -p auto"

# Functions
build_image() {
    echo "Building Docker image..."
    docker build -f $DOCKERFILE -t $IMAGE_NAME:$IMAGE_TAG .
}

run_container() {
    echo "Running tests in Docker container..."
    docker run -it --rm \
        -e TOX_WORK_DIR=$TOX_DIR \
        -v $VOLUME_MAPPING \
        $IMAGE_NAME:$IMAGE_TAG $CMD
}

# Main script execution
build_image
run_container

echo "Tests completed successfully."

```

### File: core\scripts\run_tests_buildx.sh
```sh
#!/bin/bash

set -e

# Constants
IMAGE_NAME="quivr-core-test"
IMAGE_TAG="latest"
DOCKERFILE="Dockerfile.test"
VOLUME_MAPPING="$PWD:/code"
CMD="poetry run tox"
PLATFORM="linux/amd64"
BUILDER_NAME="amd64_builder"

# Functions
build_image() {
    echo "Building Docker image for $PLATFORM..."
    EXISTING_BUILDER=$(docker buildx ls | grep -w $BUILDER_NAME)

    # Create the builder if it doesn't exist
    if [ -z "$EXISTING_BUILDER" ]; then
        echo "Creating builder: $BUILDER_NAME"
        docker buildx create --use --name $BUILDER_NAME --platform $PLATFORM
    else
        echo "Builder $BUILDER_NAME already exists. Skipping creation."
    fi

    docker buildx build --platform $PLATFORM -f $DOCKERFILE -t $IMAGE_NAME:$IMAGE_TAG --load .
}

run_container() {
    echo "Running tests in Docker container..."
    docker run -it --rm --platform $PLATFORM -v $VOLUME_MAPPING $IMAGE_NAME:$IMAGE_TAG $CMD
}

# Main script execution
build_image
run_container

echo "Tests completed successfully."
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
