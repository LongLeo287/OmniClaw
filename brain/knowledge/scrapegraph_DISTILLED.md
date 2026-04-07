---
id: scrapegraph
type: knowledge
owner: OA_Triage
---
# scrapegraph
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
## 🚀 **Looking for an even faster and simpler way to scrape at scale (only 5 lines of code)?** Check out our enhanced version at [**ScrapeGraphAI.com**](https://scrapegraphai.com/?utm_source=github&utm_medium=readme&utm_campaign=oss_cta&ut#m_content=top_banner)! 🚀

---

# 🕷️ ScrapeGraphAI: You Only Scrape Once

[English](https://github.com/VinciGit00/Scrapegraph-ai/blob/main/README.md) | [中文](https://github.com/VinciGit00/Scrapegraph-ai/blob/main/docs/chinese.md) | [日本語](https://github.com/VinciGit00/Scrapegraph-ai/blob/main/docs/japanese.md)
| [한국어](https://github.com/VinciGit00/Scrapegraph-ai/blob/main/docs/korean.md)
| [Русский](https://github.com/VinciGit00/Scrapegraph-ai/blob/main/docs/russian.md) | [Türkçe](https://github.com/VinciGit00/Scrapegraph-ai/blob/main/docs/turkish.md)
| [Deutsch](https://www.readme-i18n.com/ScrapeGraphAI/Scrapegraph-ai?lang=de)
| [Español](https://www.readme-i18n.com/ScrapeGraphAI/Scrapegraph-ai?lang=es)
| [français](https://www.readme-i18n.com/ScrapeGraphAI/Scrapegraph-ai?lang=fr)
| [Português](https://github.com/VinciGit00/Scrapegraph-ai/blob/main/docs/portuguese.md)

[![PyPI Downloads](https://static.pepy.tech/personalized-badge/scrapegraphai?period=total&units=INTERNATIONAL_SYSTEM&left_color=BLACK&right_color=GREEN&left_text=downloads)](https://pepy.tech/projects/scrapegraphai)
[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen?style=for-the-badge)](https://github.com/pylint-dev/pylint)
[![Pylint](https://img.shields.io/github/actions/workflow/status/VinciGit00/Scrapegraph-ai/code-quality.yml?label=Pylint&logo=github&style=for-the-badge)](https://github.com/VinciGit00/Scrapegraph-ai/actions/workflows/code-quality.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/VinciGit00/Scrapegraph-ai/codeql.yml?label=CodeQL&logo=github&style=for-the-badge)](https://github.com/VinciGit00/Scrapegraph-ai/actions/workflows/codeql.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![](https://dcbadge.vercel.app/api/server/gkxQDAjfeX)](https://discord.gg/gkxQDAjfeX)

[![API Banner](https://raw.githubusercontent.com/ScrapeGraphAI/Scrapegraph-ai/main/docs/assets/api_banner.png)](https://scrapegraphai.com/?utm_source=github&utm_medium=readme&utm_campaign=api_banner&utm_content=api_banner_image)

<p align="center">
<a href="https://trendshift.io/repositories/9761" target="_blank"><img src="https://trendshift.io/api/badge/repositories/9761" alt="VinciGit00%2FScrapegraph-ai | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
<p align="center">

[ScrapeGraphAI](https://scrapegraphai.com) is a *web scraping* python library that uses LLM and direct graph logic to create scraping pipelines for websites and local documents (XML, HTML, JSON, Markdown, etc.).

Just say which information you want to extract and the library will do it for you!

<p align="center">
  <img src="https://raw.githubusercontent.com/VinciGit00/Scrapegraph-ai/main/docs/assets/sgai-hero.png" alt="ScrapeGraphAI Hero" style="width: 100%;">
</p>


## 🚀 Integrations
ScrapeGraphAI offers seamless integration with popular frameworks and tools to enhance your scraping capabilities. Whether you're building with Python or Node.js, using LLM frameworks, or working with no-code platforms, we've got you covered with our comprehensive integration options..

You can find more informations at the following [link](https://scrapegraphai.com)

**Integrations**:
- **API**: [Documentation](https://docs.scrapegraphai.com/introduction)
- **SDKs**: [Python](https://docs.scrapegraphai.com/sdks/python), [Node](https://docs.scrapegraphai.com/sdks/javascript)
- **LLM Frameworks**: [Langchain](https://docs.scrapegraphai.com/integrations/langchain), [Llama Index](https://docs.scrapegraphai.com/integrations/llamaindex), [Crew.ai](https://docs.scrapegraphai.com/integrations/crewai), [Agno](https://docs.scrapegraphai.com/integrations/agno), [CamelAI](https://github.com/camel-ai/camel)
- **Low-code Frameworks**: [Pipedream](https://pipedream.com/apps/scrapegraphai), [Bubble](https://bubble.io/plugin/scrapegraphai-1745408893195x213542371433906180), [Zapier](https://zapier.com/apps/scrapegraphai/integrations), [n8n](http://localhost:5001/dashboard), [Dify](https://dify.ai), [Toolhouse](https://app.toolhouse.ai/mcp-servers/scrapegraph_smartscraper)
- **MCP server**:  [Link](https://smithery.ai/server/@ScrapeGraphAI/scrapegraph-mcp)

## 🚀 Quick install

The reference page for Scrapegraph-ai is available on the official page of PyPI: [pypi](https://pypi.org/project/scrapegraphai/).

```bash
pip install scrapegraphai

# IMPORTANT (for fetching websites content)
playwright install
```

**Note**: it is recommended to install the library in a virtual environment to avoid conflicts with other libraries 🐱


## 💻 Usage
There are multiple standard scraping pipelines that can be used to extract information from a website (or local file).

The most common one is the `SmartScraperGraph`, which extracts information from a single page given a user prompt and a source URL.


```python
from scrapegraphai.graphs import SmartScraperGraph

# Define the configuration for the scraping pipeline
graph_config = {
    "llm": {
        "model": "ollama/llama3.2",
        "model_tokens": 8192,
        "format": "json",
    },
    "verbose": True,
    "headless": False,
}

# Create the SmartScraperGraph instance
smart_scraper_graph = SmartScraperGraph(
    prompt="Extract useful information from the webpage, including a description of what the company does, founders and social media links",
    source="https://scrapegraphai.com/",
    config=graph_config
)

# Run the pipeline
result = smart_scraper_graph.run()

import json
print(json.dumps(result, indent=4))
```

> [!NOTE]
> For OpenAI and other models you just need to change the llm config!
> ```python
>graph_config = {
>    "llm": {
>        "api_key": "YOUR_OPENAI_API_KEY",
>        "model": "openai/gpt-4o-mini",
>    },
>    "verbose": True,
>    "headless": False,
>}
>```


The output will be a dictionary like the following:

```python
{
    "description": "ScrapeGraphAI transforms websites into clean, organized data for AI agents and data analytics. It offers an AI-powered API for effortless and cost-effective data extraction.",
    "founders": [
        {
            "name": "",
            "role": "Founder & Technical Lead",
            "linkedin": "https://www.linkedin.com/in/perinim/"
        },
        {
            "name": "Marco Vinciguerra",
            "role": "Founder & Software Engineer",
            "linkedin": "https://www.linkedin.com/in/marco-vinciguerra-7ba365242/"
        },
        {
            "name": "Lorenzo Padoan",
            "role": "Founder & Product Engineer",
            "linkedin": "https://www.linkedin.com/in/lorenzo-padoan-4521a2154/"
        }
    ],
    "social_media_links": {
        "linkedin": "https://www.linkedin.com/company/101881123",
        "twitter": "https://x.com/scrapegraphai",
        "github": "https://github.com/ScrapeGraphAI/Scrapegraph-ai"
    }
}
```
There are other pipelines that can be used to extract information from multiple pages, generate Python scripts, or even generate audio files.

| Pipeline Name           | Description                                                                                                      |
|-------------------------|------------------------------------------------------------------------------------------------------------------|
| SmartScraperGraph       | Single-page scraper that only needs a user prompt and an input source.                                           |
| SearchGraph             | Multi-page scraper that extracts information from the top n search results of a search engine.                  |
| SpeechGraph             | Single-page scraper that extracts information from a website and generates an audio file.                       |
| ScriptCreatorGraph      | Single-page scraper that extracts information from a website and generates a Python script.                     |
| SmartScraperMultiGraph  | Multi-page scraper that extracts information from multiple pages given a single prompt and a list of sources.    |
| ScriptCreatorMultiGraph | Multi-page scraper that generates a Python script for extracting information from multiple pages and sources.     |

For each of these graphs there is the multi version. It allows to make calls of the LLM in parallel.

It is possible to use different LLM through APIs, such as **OpenAI**, **Groq**, **Azure**, **Gemini**, **MiniMax** and more, or local models using **Ollama**.

Remember to have [Ollama](https://ollama.com/) installed and download the models using the **ollama pull** command, if you want to use local models.


## 📖 Documentation

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1sEZBonBMGP44CtO6GQTwAlL0BGJXjtfd?usp=sharing)

The documentation for ScrapeGraphAI can be found [here](https://scrapegraph-ai.readthedocs.io/en/latest/).
Check out also the Docusaurus [here](https://docs-oss.scrapegraphai.com/).

## 🤝 Contributing

Feel free to contribute and join our Discord server to discuss with us improvements and give us suggestions!

Please see the [contributing guidelines](https://github.com/VinciGit00/Scrapegraph-ai/blob/main/CONTRIBUTING.md).

[![My Skills](https://skillicons.dev/icons?i=discord)](https://discord.gg/uJN7TYcpNa)
[![My Skills](https://skillicons.dev/icons?i=linkedin)](https://www.linkedin.com/company/scrapegraphai/)
[![My Skills](https://skillicons.dev/icons?i=twitter)](https://twitter.com/scrapegraphai)

## 🔗 ScrapeGraph API & SDKs
If you are looking for a quick solution to integrate ScrapeGraph in your system, check out our powerful API [here!](https://dashboard.scrapegraphai.com/login)

[![API Banner](https://raw.githubusercontent.com/ScrapeGraphAI/Scrapegraph-ai/main/docs/assets/api_banner.png)](https://dashboard.scrapegraphai.com/login)

We offer SDKs in both Python and Node.js, making it easy to integrate into your projects. Check them out below:

| SDK       | Language | GitHub Link                                                                 |
|-----------|----------|-----------------------------------------------------------------------------|
| Python SDK | Python   | [scrapegraph-py](https://github.com/ScrapeGraphAI/scrapegraph-sdk/tree/main/scrapegraph-py) |
| Node.js SDK | Node.js  | [scrapegraph-js](https://github.com/ScrapeGraphAI/scrapegraph-sdk/tree/main/scrapegraph-js) |

The Official API Documentation can be found [here](https://docs.scrapegraphai.com/).

## 📈 Telemetry
We collect anonymous usage metrics to enhance our package's quality and user experience. The data helps us prioritize improvements and ensure compatibility. If you wish to opt-out, set the environment variable SCRAPEGRAPHAI_TELEMETRY_ENABLED=false. For more information, please refer to the documentation [here](https://scrapegraph-ai.readthedocs.io/en/latest/scrapers/telemetry.html).

## ❤️ Contributors
[![Contributors](https://contrib.rocks/image?repo=VinciGit00/Scrapegraph-ai)](https://github.com/VinciGit00/Scrapegraph-ai/graphs/contributors)

## 🎓 Citations
If you have used our library for research purposes please quote us with the following reference:
```text
  @misc{scrapegraph-ai,
    author = {Lorenzo Padoan, Marco Vinciguerra},
    title = {Scrapegraph-ai},
    year = {2024},
    url = {https://github.com/VinciGit00/Scrapegraph-ai},
    note = {A Python library for scraping leveraging large language models}
  }
```
## Authors

|                    | Contact Info         |
|--------------------|----------------------|
| Marco Vinciguerra  | [![Linkedin Badge](https://img.shields.io/badge/-Linkedin-blue?style=flat&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/marco-vinciguerra-7ba365242/)    |
| Lorenzo Padoan     | [![Linkedin Badge](https://img.shields.io/badge/-Linkedin-blue?style=flat&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/lorenzo-padoan-4521a2154/)  |

## 📜 License

ScrapeGraphAI is licensed under the MIT License. See the [LICENSE](https://github.com/VinciGit00/Scrapegraph-ai/blob/main/LICENSE) file for more information.

## Acknowledgements

- We would like to thank all the contributors to the project and the open-source community for their support.
- ScrapeGraphAI is meant to be used for data exploration and research purposes only. We are not responsible for any misuse of the library.

Made with ❤️ by [ScrapeGraph AI](https://scrapegraphai.com)

[Scarf tracking](https://static.scarf.sh/a.png?x-pxid=102d4b8c-cd6a-4b9e-9a16-d6d141b9212d)

```

### File: requirements.txt
```txt
sphinx>=7.1.2
myst-parser>=2.0.0
sphinx-copybutton>=0.5.2
sphinx-design>=0.5.0
sphinx-autodoc-typehints>=1.25.2
sphinx-autoapi>=3.0.0 
```

### File: docs\requirements.txt
```txt
sphinx>=7.1.2

sphinx-rtd-theme>=1.3.0
myst-parser>=2.0.0
sphinx-copybutton>=0.5.2
sphinx-design>=0.5.0
sphinx-autodoc-typehints>=1.25.2
sphinx-autoapi>=3.0.0
furo>=2024.1.29 
```

### File: examples\readme.md
```md
# 🕷️ Scrapegraph-ai Examples

This directory contains various example implementations of Scrapegraph-ai for different use cases. Each example demonstrates how to leverage the power of Scrapegraph-ai for specific scenarios.

> **Note:** While these examples showcase implementations using OpenAI and Ollama, Scrapegraph-ai supports many other LLM providers! Check out our [documentation](https://docs-oss.scrapegraphai.com/examples) for the full list of supported providers.

## 📚 Available Examples

- 🧠 `smart_scraper/` - Advanced web scraping with intelligent content extraction
- 🔎 `search_graph/` - Web search and data retrieval
- ⚙️ `script_generator_graph/` - Automated script generation
- 🌐 `depth_search_graph/` - Deep web crawling and content exploration
- 📊 `csv_scraper_graph/` - Scraping and processing data into CSV format
- 📑 `xml_scraper_graph/` - XML data extraction and processing
- 🎤 `speech_graph/` - Speech processing and analysis
- 🔄 `omni_scraper_graph/` - Universal web scraping for multiple data types
- 🔍 `omni_search_graph/` - Comprehensive search across multiple sources
- 📄 `document_scraper_graph/` - Document parsing and data extraction
- 🛠️ `custom_graph/` - Custom graph implementation examples
- 💻 `code_generator_graph/` - Code generation utilities
- 📋 `json_scraper_graph/` - JSON data extraction and processing
- 📋 `colab example`:
<a target="_blank" href="https://colab.research.google.com/drive/1sEZBonBMGP44CtO6GQTwAlL0BGJXjtfd?usp=sharing#scrollTo=vGDjka17pqqg">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

## 🚀 Getting Started

1. Choose the example that best fits your use case
2. Navigate to the corresponding directory
3. Follow the README instructions in each directory
4. Configure any required environment variables using the provided `.env.example` files

## ⚡ Quick Setup

```bash
pip install scrapegraphai

playwright install

# choose an example
cd examples/smart_scraper_graph/openai

# run the example
python smart_scraper_openai.py
```

## 📋 Requirements

Each example may have its own specific requirements. Please refer to the individual README files in each directory for detailed setup instructions.

## 📚 Additional Resources

- 📖 [Full Documentation](https://docs-oss.scrapegraphai.com/examples)
- 💡 [Examples Repository](https://github.com/ScrapeGraphAI/ScrapegraphLib-Examples)
- 🤝 [Community Support](https://github.com/ScrapeGraphAI/scrapegraph-ai/discussions)

## 🤔 Need Help?

- Check out our [documentation](https://docs-oss.scrapegraphai.com)
- Join our [Discord community](https://discord.gg/scrapegraphai)
- Open an [issue](https://github.com/ScrapeGraphAI/scrapegraph-ai/issues)

---

⭐ Don't forget to star our repository if you find these examples helpful!

```

### File: tests\Readme.md
```md
# Test section

Regarding the tests for the folder graphs and nodes it was created a specific repo as a example
([link of the repo](https://github.com/VinciGit00/Scrapegrah-ai-website-for-tests)). The test website is hosted [here](https://scrapegrah-ai-website-for-tests.onrender.com).
Remember to activating Ollama and having installed the LLM on your pc

For running the tests run the command:
```python
pytest
```

```

### File: .pre-commit-config.yaml
```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 24.8.0
    hooks:
      - id: black

  - repo: https://github.com/charliermarsh/ruff-pre-commit
    rev: v0.6.9
    hooks:
      - id: ruff

  - repo: https://github.com/pycqa/isort
    rev: 5.13.2
    hooks:
      - id: isort

  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.6.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
        exclude: mkdocs.yml

```

### File: .readthedocs.yaml
```yaml

# Read the Docs configuration file for Sphinx projects
# See https://docs.readthedocs.io/en/stable/config-file/v2.html for details

# Required
version: 2

# Set the OS, Python version and other tools you might need
build:
  os: ubuntu-22.04
  tools:
    python: "3.12"
    # You can also specify other tool versions:
    # nodejs: "20"
    # rust: "1.70"
    # golang: "1.20"

# Build documentation in the "docs/" directory with Sphinx
sphinx:
  configuration: docs/conf.py
  # You can configure Sphinx to use a different builder, for instance use the dirhtml builder for simpler URLs
  # builder: "dirhtml"
  # Fail on all warnings to avoid broken references
  # fail_on_warning: true

# Optionally build your docs in additional formats such as PDF and ePub
# formats:
#   - pdf
#   - epub

# Optional but recommended, declare the Python requirements required
# to build your documentation
# See https://docs.readthedocs.io/en/stable/guides/reproducible-builds.html
# python:
#   install:
#     - requirements: docs/requirements.txt

```

### File: CODE_OF_CONDUCT.md
```md
# Contributor Covenant Code of Conduct

## Our Pledge

We as members, contributors, and leaders pledge to make participation in our
community a harassment-free experience for everyone, regardless of age, body
size, visible or invisible disability, ethnicity, sex characteristics, gender
identity and expression, level of experience, education, socio-economic status,
nationality, personal appearance, race, religion, or sexual identity
and orientation.

We pledge to act and interact in ways that contribute to an open, welcoming,
diverse, inclusive, and healthy community.

## Our Standards

Examples of behavior that contributes to a positive environment for our
community include:

* Demonstrating empathy and kindness toward other people
* Being respectful of differing opinions, viewpoints, and experiences
* Giving and gracefully accepting constructive feedback
* Accepting responsibility and apologizing to those affected by our mistakes,
  and learning from the experience
* Focusing on what is best not just for us as individuals, but for the
  overall community

Examples of unacceptable behavior include:

* The use of sexualized language or imagery, and sexual attention or
  advances of any kind
* Trolling, insulting or derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or email
  address, without their explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting

## Enforcement Responsibilities

Community leaders are responsible for clarifying and enforcing our standards of
acceptable behavior and will take appropriate and fair corrective action in
response to any behavior that they deem inappropriate, threatening, offensive,
or harmful.

Community leaders have the right and responsibility to remove, edit, or reject
comments, commits, code, wiki edits, issues, and other contributions that are
not aligned to this Code of Conduct, and will communicate reasons for moderation
decisions when appropriate.

## Scope

This Code of Conduct applies within all community spaces, and also applies when
an individual is officially representing the community in public spaces.
Examples of representing our community include using an official e-mail address,
posting via an official social media account, or acting as an appointed
representative at an online or offline event.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported to the community leaders responsible for enforcement at
mvincig11@gmail.com.
All complaints will be reviewed and investigated promptly and fairly.

All community leaders are obligated to respect the privacy and security of the
reporter of any incident.

## Enforcement Guidelines

Community leaders will follow these Community Impact Guidelines in determining
the consequences for any action they deem in violation of this Code of Conduct:

### 1. Correction

**Community Impact**: Use of inappropriate language or other behavior deemed
unprofessional or unwelcome in the community.

**Consequence**: A private, written warning from community leaders, providing
clarity around the nature of the violation and an explanation of why the
behavior was inappropriate. A public apology may be requested.

### 2. Warning

**Community Impact**: A violation through a single incident or series
of actions.

**Consequence**: A warning with consequences for continued behavior. No
interaction with the people involved, including unsolicited interaction with
those enforcing the Code of Conduct, for a specified period of time. This
includes avoiding interactions in community spaces as well as external channels
like social media. Violating these terms may lead to a temporary or
permanent ban.

### 3. Temporary Ban

**Community Impact**: A serious violation of community standards, including
sustained inappropriate behavior.

**Consequence**: A temporary ban from any sort of interaction or public
communication with the community for a specified period of time. No public or
private interaction with the people involved, including unsolicited interaction
with those enforcing the Code of Conduct, is allowed during this period.
Violating these terms may lead to a permanent ban.

### 4. Permanent Ban

**Community Impact**: Demonstrating a pattern of violation of community
standards, including sustained inappropriate behavior,  harassment of an
individual, or aggression toward or disparagement of classes of individuals.

**Consequence**: A permanent ban from any sort of public interaction within
the community.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage],
version 2.0, available at
https://www.contributor-covenant.org/version/2/0/code_of_conduct.html.

Community Impact Guidelines were inspired by [Mozilla's code of conduct
enforcement ladder](https://github.com/mozilla/diversity).

[homepage]: https://www.contributor-covenant.org

For answers to common questions about this code of conduct, see the FAQ at
https://www.contributor-covenant.org/faq. Translations are available at
https://www.contributor-covenant.org/translations.

```

### File: CONTRIBUTING.md
```md
# Contributing to ScrapeGraphAI 🚀

Hey there! Thanks for checking out **ScrapeGraphAI**! We're excited to have you here! 🎉

## Quick Start Guide 🏃‍♂️

1. Fork the repository from the **pre/beta branch** 🍴
2. Clone your fork locally 💻
3. Install uv (if you haven't):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```
4. Run `uv sync` (creates virtual env & installs dependencies) ⚡
5. Run `uv run pre-commit install` 🔧
6. Make your awesome changes ✨
7. Test thoroughly 🧪
8. Push & open a PR to the pre/beta branch 🎯

## Contribution Guidelines 📝

Keep it clean and simple:
- Follow our code style (PEP 8 & Google Python Style) 🎨
- Document your changes clearly 📚
- Use these commit prefixes for your final PR commit:
  ```
  feat: ✨ New feature
  fix: 🐛 Bug fix
  docs: 📚 Documentation
  style: 💅 Code style
  refactor: ♻️ Code changes
  test: 🧪 Testing
  perf: ⚡ Performance
  ```
- Be nice to others! 💝

## Need Help? 🤔

Found a bug or have a cool idea? Open an issue and let's chat! 💬

## License 📜

MIT Licensed. See [LICENSE](LICENSE) file for details.

Let's build something amazing together! 🌟

```

### File: requirements-dev.txt
```txt
sphinx>=7.1.2
myst-parser>=2.0.0
sphinx-copybutton>=0.5.2
sphinx-design>=0.5.0
sphinx-autodoc-typehints>=1.25.2
sphinx-autoapi>=3.0.0 
```

### File: SECURITY.md
```md
# Security Policy

## Reporting a Vulnerability

For reporting a vulnerability contact directly mvincig11@gmail.com

```

### File: SEMANTIC_COMMITS.md
```md
# Semantic Commit Format for This PR

## Current Situation

This PR contains commits that need to be rewritten to follow Conventional Commits format for semantic-release compatibility.

**Note:** The timeout documentation is marked as `feat(timeout)` (not `docs`) because it exposes a user-facing feature. Even though the implementation existed, this PR makes the feature discoverable and usable by users through documentation, which warrants a feature-level semantic version bump.

## Commits to Rewrite

### Commit 1: 9439fe5
**Current:** `Fix langchain import issues blocking tests`

**Should be:**
```
fix(imports): update deprecated langchain imports to langchain_core

Update imports from deprecated langchain.prompts to langchain_core.prompts
across 20 files to fix test suite import errors. These changes address
breaking API changes in newer langchain versions.

Fixes #1015
```

**Type:** `fix` - Bug fix for test import errors
**Scope:** `imports` - Changes affect import statements

---

### Commit 2: 323f26a  
**Current:** `Add comprehensive timeout feature documentation`

**Should be:**
```
feat(timeout): add configurable timeout support for FetchNode

Add comprehensive documentation for the timeout configuration feature:
- Configuration examples with different timeout values
- Use cases for HTTP requests, PDF parsing, and ChromiumLoader
- Graph integration examples
- Best practices and troubleshooting guide

The timeout feature enables users to control execution time for blocking
operations (HTTP requests, PDF parsing, ChromiumLoader) to prevent
indefinite hangs. Configurable via node_config with 30s default.

Fixes #1015
```

**Type:** `feat` - New feature documentation/exposure to users
**Scope:** `timeout` - Timeout configuration feature

---

## How to Apply (For Maintainer)

Since automated tools can't force-push to rewrite history, the maintainer needs to manually rewrite these commits:

### Option 1: Interactive Rebase
```bash
git rebase -i 6d13212
# Mark commits 9439fe5 and 323f26a as 'reword'
# Update commit messages with semantic format above
# Force push: git push --force-with-lease
```

### Option 2: Squash and Rewrite
```bash
# Reset to initial commit
git reset --soft 6d13212

# Stage import fixes
git add scrapegraphai/

# Commit with semantic message
git commit -m "fix(imports): update deprecated langchain imports to langchain_core

Update imports from deprecated langchain.prompts to langchain_core.prompts
across 20 files to fix test suite import errors. These changes address
breaking API changes in newer langchain versions.

Fixes #1015"

# Stage documentation
git add docs/

# Commit with semantic message
git commit -m "feat(timeout): add configurable timeout support for FetchNode

Add comprehensive documentation for the timeout configuration feature:
- Configuration examples with different timeout values
- Use cases for HTTP requests, PDF parsing, and ChromiumLoader
- Graph integration examples
- Best practices and troubleshooting guide

The timeout feature enables users to control execution time for blocking
operations (HTTP requests, PDF parsing, ChromiumLoader) to prevent
indefinite hangs. Configurable via node_config with 30s default.

Fixes #1015"

# Force push
git push --force-with-lease origin copilot/add-timeout-to-fetch-node
```

## Semantic Release Configuration

This repository uses `@semantic-release/commit-analyzer` with `conventionalcommits` preset (see `.releaserc.yml`).

Valid types for this repo:
- `feat`: New features → Minor version bump
- `fix`: Bug fixes → Patch version bump
- `docs`: Documentation changes → No version bump (shown in changelog)
- `chore`: Maintenance tasks
- `refactor`: Code refactoring
- `perf`: Performance improvements
- `test`: Test changes

## References

- [Conventional Commits](https://www.conventionalcommits.org/)
- [Semantic Release](https://semantic-release.gitbook.io/)
- Repository config: `.releaserc.yml`

```

### File: TESTING_INFRASTRUCTURE.md
```md
# Enhanced Testing Infrastructure - Implementation Summary

## Overview

A comprehensive testing infrastructure has been implemented for ScrapeGraphAI with support for unit tests, integration tests, performance benchmarking, and automated CI/CD pipelines.

## What Was Added

### 1. Core Testing Configuration

#### `pytest.ini`
- Complete pytest configuration with coverage tracking
- Custom markers for test categorization (integration, slow, benchmark, etc.)
- Code coverage settings with HTML/XML reports
- Test discovery patterns and exclusions

#### `tests/conftest.py`
- Shared fixtures for all LLM providers (OpenAI, Ollama, Anthropic, Groq, Azure, Gemini)
- Mock LLM and embedder fixtures for unit testing
- Test data fixtures (HTML, JSON, XML, CSV)
- Temporary file fixtures
- Performance tracking fixtures
- Custom pytest hooks and CLI options
- Automatic test filtering based on markers

### 2. Mock HTTP Server (`tests/fixtures/mock_server/`)

A fully functional HTTP server for consistent testing without external dependencies:

**Features:**
- Static HTML pages (home, products, projects)
- JSON/XML/CSV API endpoints
- Slow response simulation
- Error condition testing (404, 500)
- Rate limiting simulation
- Dynamic content generation
- Pagination support
- Thread-safe operation

**Endpoints:**
- `/` - Home page
- `/products` - Product listings with prices and stock status
- `/projects` - Project listings with descriptions
- `/api/data.json` - JSON data endpoint
- `/api/data.xml` - XML data endpoint
- `/api/data.csv` - CSV data endpoint
- `/slow` - 2-second delay simulation
- `/error/404` - 404 error page
- `/error/500` - 500 error page
- `/rate-limited` - Rate limit testing (5 requests max)
- `/dynamic` - Dynamically generated content
- `/pagination?page=N` - Paginated content

### 3. Performance Benchmarking (`tests/fixtures/benchmarking.py`)

**Components:**
- `BenchmarkResult` - Individual test result tracking
- `BenchmarkSummary` - Statistical analysis across multiple runs
- `BenchmarkTracker` - Result collection and reporting
- `benchmark()` - Decorator/function for benchmarking
- Baseline comparison utilities
- Performance regression detection

**Metrics Tracked:**
- Execution time (mean, median, std dev, min, max)
- Memory usage
- Token usage
- API call counts
- Success rates

**Features:**
- JSON export of results
- Human-readable reports
- Warmup runs support
- Multiple test runs with statistics
- Baseline comparison for regression detection

### 4. Test Utilities (`tests/fixtures/helpers.py`)

**Assertion Helpers:**
- `assert_valid_scrape_result()` - Validate scraping results
- `assert_execution_info_valid()` - Validate execution metadata
- `assert_response_time_acceptable()` - Performance assertions
- `assert_no_errors_in_result()` - Error detection

**Mock Response Builders:**
- `create_mock_llm_response()` - Generate mock LLM responses
- `create_mock_graph_result()` - Mock graph execution results

**Data Generators:**
- `generate_test_html()` - Customizable HTML generation
- `generate_test_json()` - Test JSON data
- `generate_test_csv()` - Test CSV data

**Validation Utilities:**
- `validate_schema_match()` - Pydantic schema validation
- `validate_extracted_fields()` - Field extraction validation

**Additional Utilities:**
- `RateLimitHelper` - Rate limiting testing
- `retry_with_backoff()` - Retry logic with exponential backoff
- `compare_results()` - Result comparison
- `fuzzy_match_strings()` - Fuzzy string matching
- File loading and saving utilities

### 5. Integration Test Suite

#### `tests/integration/test_smart_scraper_integration.py`
- SmartScraperGraph with multiple LLM providers
- Schema-based scraping tests
- Timeout handling tests
- Error condition tests (404, 500)
- Performance benchmarks
- Real website testing support

#### `tests/integration/test_multi_graph_integration.py`
- SmartScraperMultiGraph tests
- Concurrent scraping tests
- Performance benchmarks for multi-page scraping
- SearchGraph integration tests

#### `tests/integration/test_file_formats_integration.py`
- JSONScraperGraph tests (files and URLs)
- XMLScraperGraph tests (files and URLs)
- CSVScraperGraph tests (files and URLs)
- Performance benchmarks for file format scrapers

### 6. GitHub Actions Workflow (`.github/workflows/test-suite.yml`)

**Jobs:**

1. **Unit Tests**
   - Matrix: Ubuntu, macOS, Windows
   - Python versions: 3.10, 3.11, 3.12
   - Coverage reporting to Codecov
   - Fast execution without external dependencies

2. **Integration Tests**
   - Test groups: smart-scraper, multi-graph, file-formats
   - Real LLM provider testing (with API keys)
   - Artifact uploads for test results

3. **Performance Benchmarks**
   - Track execution time and resource usage
   - Save results as artifacts
   - Compare against baseline (on PRs)

4. **Code Quality**
   - Ruff linting
   - Black formatting check
   - isort import sorting check
   - mypy type checking

5. **Test Coverage Report**
   - Aggregate coverage from all jobs
   - PR comments with coverage changes

6. **Test Summary**
   - Overall test status reporting

**Triggers:**
- Push to main, pre/beta, dev branches
- Pull requests to main, pre/beta
- Manual workflow dispatch

### 7. Documentation

#### `tests/README_TESTING.md`
Comprehensive guide covering:
- Test organization structure
- Running different test types
- Using fixtures and markers
- Performance benchmarking
- Mock server usage
- Environment variables
- Writing new tests (with templates)
- Best practices
- Troubleshooting

## Key Features

### Multi-Provider Support
Test compatibility across all supported LLM providers:
- OpenAI (GPT-3.5, GPT-4)
- Ollama (local models)
- Anthropic Claude
- Groq
- Azure OpenAI
- Google Gemini

### Test Markers
Organized test categorization:
- `@pytest.mark.unit` - Fast unit tests
- `@pytest.mark.integration` - Integration tests
- `@pytest.mark.slow` - Long-running tests
- `@pytest.mark.benchmark` - Performance tests
- `@pytest.mark.requires_api_key` - Needs API credentials

### Flexible Test Execution
```bash
# Unit tests only
pytest -m "unit or not integration"

# Integration tests
pytest --integration

# Performance benchmarks
pytest --benchmark -m benchmark

# Slow tests
pytest --slow

# With coverage
pytest --cov=scrapegraphai --cov-report=html
```

### Mock Server Benefits
- No external dependencies for basic tests
- Consistent, reproducible test conditions
- Simulate error conditions and edge cases
- Test rate limiting and timeouts
- Fast test execution

### Performance Tracking
- Automatic tracking of execution time
- Token usage monitoring
- API call counting
- Regression detection
- Baseline comparison

## Usage Examples

### Basic Unit Test
```python
def test_with_mock(mock_llm_model):
    """Fast test with mocked LLM."""
    result = some_function(mock_llm_model)
    assert result is not None
```

### Integration Test
```python
@pytest.mark.integration
@pytest.mark.requires_api_key
def test_real_scraping(openai_config, mock_server):
    """Test with real LLM and mock server."""
    url = mock_server.get_url("/products")
    scraper = SmartScraperGraph(
        prompt="Extract products",
        source=url,
        config=openai_config
    )
    result = scraper.run()
    assert_valid_scrape_result(result)
```

### Performance Benchmark
```python
@pytest.mark.benchmark
def test_performance(benchmark_tracker, openai_config):
    """Benchmark scraping performance."""
    import time

    start = time.perf_counter()
    # Run operation
    end = time.perf_counter()

    benchmark_tracker.record(BenchmarkResult(
        test_name="my_test",
        execution_time=end - start,
        success=True
    ))
```

## Benefits

1. **Comprehensive Coverage**: Unit, integration, and performance tests
2. **Fast Feedback**: Quick unit tests with extensive mocking
3. **Real-World Testing**: Integration tests with actual LLM providers
4. **Performance Monitoring**: Track and prevent performance regressions
5. **CI/CD Ready**: Automated testing in GitHub Actions
6. **Developer Friendly**: Clear documentation and templates
7. **Flexible Execution**: Run specific test subsets easily
8. **Cross-Platform**: Tested on Linux, macOS, Windows
9. **Multi-Python**: Support for Python 3.10, 3.11, 3.12

## Next Steps

1. **Add more integration tests** for additional graph types
2. **Expand mock server** with more realistic scenarios
3. **Add visual regression testing** for screenshot comparisons
4. **Implement mutation testing** for test quality
5. **Add property-based testing** with Hypothesis
6. **Create performance dashboards** for trend visualization
7. **Add load testing** for concurrent scraping scenarios

## Files Created/Modified

**New Files:**
- `pytest.ini` - Pytest configuration
- `tests/conftest.py` - Shared fixtures
- `tests/fixtures/mock_server/server.py` - Mock HTTP server
- `tests/fixtures/benchmarking.py` - Performance framework
- `tests/fixtures/helpers.py` - Test utilities
- `tests/integration/test_smart_scraper_integration.py`
- `tests/integration/test_multi_graph_integration.py`
- `tests/integration/test_file_formats_integration.py`
- `.github/workflows/test-suite.yml` - CI/CD workflow
- `tests/README_TESTING.md` - Testing documentation
- `TESTING_INFRASTRUCTURE.md` - This file

**Directories Created:**
- `tests/fixtures/`
- `tests/fixtures/mock_server/`
- `tests/integration/`
- `benchmark_results/` (auto-created when running benchmarks)

## Contributing

When adding new tests:
1. Use appropriate fixtures from conftest.py
2. Add proper markers (@pytest.mark.*)
3. Follow existing test structure
4. Update documentation as needed
5. Ensure tests pass in CI

For questions or issues with the testing infrastructure, please open an issue on GitHub.

```

### File: docs\chinese.md
```md
## 🚀 **正在寻找更快、更简单的规模化抓取方式（只需5行代码）？** 查看我们在 [**ScrapeGraphAI.com**](https://scrapegraphai.com/?utm_source=github&utm_medium=readme&utm_campaign=oss_cta&utm_content=top_banner) 的增强版本！🚀

---

# 🕷️ ScrapeGraphAI: 只需抓取一次

[English](https://github.com/VinciGit00/Scrapegraph-ai/blob/main/README.md) | [中文](https://github.com/VinciGit00/Scrapegraph-ai/blob/main/docs/chinese.md) | [日本語](https://github.com/VinciGit00/Scrapegraph-ai/blob/main/docs/japanese.md)
| [한국어](https://github.com/VinciGit00/Scrapegraph-ai/blob/main/docs/korean.md)
| [Русский](https://github.com/VinciGit00/Scrapegraph-ai/blob/main/docs/russian.md) | [Türkçe](https://github.com/VinciGit00/Scrapegraph-ai/blob/main/docs/turkish.md)
| [Deutsch](https://www.readme-i18n.com/ScrapeGraphAI/Scrapegraph-ai?lang=de)
| [Español](https://www.readme-i18n.com/ScrapeGraphAI/Scrapegraph-ai?lang=es)
| [français](https://www.readme-i18n.com/ScrapeGraphAI/Scrapegraph-ai?lang=fr)
| [Português](https://github.com/VinciGit00/Scrapegraph-ai/blob/main/docs/portuguese.md)

[![PyPI Downloads](https://static.pepy.tech/personalized-badge/scrapegraphai?period=total&units=INTERNATIONAL_SYSTEM&left_color=BLACK&right_color=GREEN&left_text=downloads)](https://pepy.tech/projects/scrapegraphai)
[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen?style=for-the-badge)](https://github.com/pylint-dev/pylint)
[![Pylint](https://img.shields.io/github/actions/workflow/status/VinciGit00/Scrapegraph-ai/code-quality.yml?label=Pylint&logo=github&style=for-the-badge)](https://github.com/VinciGit00/Scrapegraph-ai/actions/workflows/code-quality.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/VinciGit00/Scrapegraph-ai/codeql.yml?label=CodeQL&logo=github&style=for-the-badge)](https://github.com/VinciGit00/Scrapegraph-ai/actions/workflows/codeql.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![](https://dcbadge.vercel.app/api/server/gkxQDAjfeX)](https://discord.gg/gkxQDAjfeX)

[![API Banner](https://raw.githubusercontent.com/ScrapeGraphAI/Scrapegraph-ai/main/docs/assets/api_banner.png)](https://scrapegraphai.com/?utm_source=github&utm_medium=readme&utm_campaign=api_banner&utm_content=api_banner_image)

<p align="center">
<a href="https://trendshift.io/repositories/9761" target="_blank"><img src="https://trendshift.io/api/badge/repositories/9761" alt="VinciGit00%2FScrapegraph-ai | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
<p align="center">

[ScrapeGraphAI](https://scrapegraphai.com) 是一个*网络爬虫* Python 库，使用大型语言模型和直接图逻辑为网站和本地文档（XML，HTML，JSON，Markdown 等）创建爬取管道。

只需告诉库您想提取哪些信息，它将为您完成！

<p align="center">
  <img src="https://raw.githubusercontent.com/VinciGit00/Scrapegraph-ai/main/docs/assets/sgai-hero.png" alt="ScrapeGraphAI Hero" style="width: 100%;">
</p>


## 🚀 集成
ScrapeGraphAI 提供与流行框架和工具的无缝集成，以增强您的抓取能力。无论您使用 Python 还是 Node.js 构建，使用 LLM 框架，还是使用无代码平台，我们都为您提供全面的集成选项。

您可以在以下[链接](https://scrapegraphai.com)找到更多信息

**集成**：
- **API**: [文档](https://docs.scrapegraphai.com/introduction)
- **SDKs**: [Python](https://docs.scrapegraphai.com/sdks/python), [Node](https://docs.scrapegraphai.com/sdks/javascript)
- **LLM 框架**: [Langchain](https://docs.scrapegraphai.com/integrations/langchain), [Llama Index](https://docs.scrapegraphai.com/integrations/llamaindex), [Crew.ai](https://docs.scrapegraphai.com/integrations/crewai), [Agno](https://docs.scrapegraphai.com/integrations/agno), [CamelAI](https://github.com/camel-ai/camel)
- **低代码框架**: [Pipedream](https://pipedream.com/apps/scrapegraphai), [Bubble](https://bubble.io/plugin/scrapegraphai-1745408893195x213542371433906180), [Zapier](https://zapier.com/apps/scrapegraphai/integrations), [n8n](http://localhost:5001/dashboard), [Dify](https://dify.ai), [Toolhouse](https://app.toolhouse.ai/mcp-servers/scrapegraph_smartscraper)
- **MCP 服务器**:  [链接](https://smithery.ai/server/@ScrapeGraphAI/scrapegraph-mcp)

## 🚀 快速安装

Scrapegraph-ai 的参考页面可以在 PyPI 的官方网站上找到: [pypi](https://pypi.org/project/scrapegraphai/)。

```bash
pip install scrapegraphai

# 重要（用于获取网站内容）
playwright install
```

**注意**: 建议在虚拟环境中安装该库，以避免与其他库发生冲突 🐱


## 💻 用法
有多种标准抓取管道可用于从网站（或本地文件）提取信息。

最常见的是 `SmartScraperGraph`，它在给定用户提示和源 URL 的情况下从单个页面提取信息。


```python
from scrapegraphai.graphs import SmartScraperGraph

# 定义抓取管道的配置
graph_config = {
    "llm": {
        "model": "ollama/llama3.2",
        "model_tokens": 8192,
        "format": "json",
    },
    "verbose": True,
    "headless": False,
}

# 创建 SmartScraperGraph 实例
smart_scraper_graph = SmartScraperGraph(
    prompt="从网页中提取有用信息，包括公司描述、创始人和社交媒体链接",
    source="https://scrapegraphai.com/",
    config=graph_config
)

# 运行管道
result = smart_scraper_graph.run()

import json
print(json.dumps(result, indent=4))
```

> [!NOTE]
> 对于 OpenAI 和其他模型，您只需要更改 llm 配置！
> ```python
>graph_config = {
>    "llm": {
>        "api_key": "YOUR_OPENAI_API_KEY",
>        "model": "openai/gpt-4o-mini",
>    },
>    "verbose": True,
>    "headless": False,
>}
>```


输出将是一个类似以下的字典：

```python
{
    "description": "ScrapeGraphAI transforms websites into clean, organized data for AI agents and data analytics. It offers an AI-powered API for effortless and cost-effective data extraction.",
    "founders": [
        {
            "name": "",
            "role": "Founder & Technical Lead",
            "linkedin": "https://www.linkedin.com/in/perinim/"
        },
        {
            "name": "Marco Vinciguerra",
            "role": "Founder & Software Engineer",
            "linkedin": "https://www.linkedin.com/in/marco-vinciguerra-7ba365242/"
        },
        {
            "name": "Lorenzo Padoan",
            "role": "Founder & Product Engineer",
            "linkedin": "https://www.linkedin.com/in/lorenzo-padoan-4521a2154/"
        }
    ],
    "social_media_links": {
        "linkedin": "https://www.linkedin.com/company/101881123",
        "twitter": "https://x.com/scrapegraphai",
        "github": "https://github.com/ScrapeGraphAI/Scrapegraph-ai"
    }
}
```
还有其他管道可用于从多个页面提取信息、生成 Python 脚本，甚至生成音频文件。

| 管道名称           | 描述                                                                                                      |
|-------------------------|------------------------------------------------------------------------------------------------------------------|
| SmartScraperGraph       | 单页抓取器，只需要用户提示和输入源。                                           |
| SearchGraph             | 多页抓取器，从搜索引擎的前 n 个搜索结果中提取信息。                  |
| SpeechGraph             | 单页抓取器，从网站提取信息并生成音频文件。                       |
| ScriptCreatorGraph      | 单页抓取器，从网站提取信息并生成 Python 脚本。                     |
| SmartScraperMultiGraph  | 多页抓取器，在给定单个提示和源列表的情况下从多个页面提取信息。    |
| ScriptCreatorMultiGraph | 多页抓取器，生成用于从多个页面和源提取信息的 Python 脚本。     |

对于这些图中的每一个，都有多版本。它允许并行调用 LLM。

可以通过 API 使用不同的 LLM，例如 **OpenAI**、**Groq**、**Azure** 和 **Gemini**，或使用 **Ollama** 的本地模型。

如果您想使用本地模型，请记住安装 [Ollama](https://ollama.com/) 并使用 **ollama pull** 命令下载模型。


## 📖 文档

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1sEZBonBMGP44CtO6GQTwAlL0BGJXjtfd?usp=sharing)

ScrapeGraphAI 的文档可以在[这里](https://scrapegraph-ai.readthedocs.io/en/latest/)找到。
还可以查看 Docusaurus [这里](https://docs-oss.scrapegraphai.com/)。

## 🤝 贡献

欢迎贡献并加入我们的 Discord 服务器与我们讨论改进和提出建议！

请参阅[贡献指南](https://github.com/VinciGit00/Scrapegraph-ai/blob/main/CONTRIBUTING.md)。

[![My Skills](https://skillicons.dev/icons?i=discord)](https://discord.gg/uJN7TYcpNa)
[![My Skills](https://skillicons.dev/icons?i=linkedin)](https://www.linkedin.com/company/scrapegraphai/)
[![My Skills](https://skillicons.dev/icons?i=twitter)](https://twitter.com/scrapegraphai)

## 🔗 ScrapeGraph API & SDKs
如果您正在寻找快速解决方案来将 ScrapeGraph 集成到您的系统中，请查看我们的强大 API [这里！](https://dashboard.scrapegraphai.com/login)

[![API Banner](https://raw.githubusercontent.com/ScrapeGraphAI/Scrapegraph-ai/main/docs/assets/api_banner.png)](https://dashboard.scrapegraphai.com/login)

我们提供 Python 和 Node.js 的 SDK，使您可以轻松集成到您的项目中。请在下面查看：

| SDK       | 语言 | GitHub 链接                                                                 |
|-----------|----------|-----------------------------------------------------------------------------|
| Python SDK | Python   | [scrapegraph-py](https://github.com/ScrapeGraphAI/scrapegraph-sdk/tree/main/scrapegraph-py) |
| Node.js SDK | Node.js  | [scrapegraph-js](https://github.com/ScrapeGraphAI/scrapegraph-sdk/tree/main/scrapegraph-js) |

官方 API 文档可以在[这里](https://docs.scrapegraphai.com/)找到。

## 🔥 基准测试

根据 Firecrawl 基准测试 [Firecrawl benchmark](https://github.com/firecrawl/scrape-evals/pull/3)，ScrapeGraph 是市场上最好的抓取工具！

![here](assets/histogram.png)

## 📈 遥测
我们收集匿名使用指标以增强我们包的质量和用户体验。这些数据帮助我们确定改进的优先级并确保兼容性。如果您希望退出，请设置环境变量 SCRAPEGRAPHAI_TELEMETRY_ENABLED=false。有关更多信息，请参阅[这里](https://scrapegraph-ai.readthedocs.io/en/latest/scrapers/telemetry.html)的文档。

## ❤️ 贡献者
[![Contributors](https://contrib.rocks/image?repo=VinciGit00/Scrapegraph-ai)](https://github.com/VinciGit00/Scrapegraph-ai/graphs/contributors)

## 🎓 引用
如果您将我们的库用于研究目的，请使用以下参考文献引用我们：
```text
  @misc{scrapegraph-ai,
    author = {Lorenzo Padoan, Marco Vinciguerra},
    title = {Scrapegraph-ai},
    year = {2024},
    url = {https://github.com/VinciGit00/Scrapegraph-ai},
    note = {一个利用大型语言模型进行爬取的 Python 库}
  }
```
## 作者

|                    | 联系信息         |
|--------------------|----------------------|
| Marco Vinciguerra  | [![Linkedin Badge](https://img.shields.io/badge/-Linkedin-blue?style=flat&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/marco-vinciguerra-7ba365242/)    |
| Lorenzo Padoan     | [![Linkedin Badge](https://img.shields.io/badge/-Linkedin-blue?style=flat&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/lorenzo-padoan-4521a2154/)  |

## 📜 许可证

ScrapeGraphAI 采用 MIT 许可证。更多信息请查看 [LICENSE](https://github.com/VinciGit00/Scrapegraph-ai/blob/main/LICENSE) 文件。

## 鸣谢

- 我们要感谢所有项目贡献者和开源社区的支持。
- ScrapeGraphAI 仅用于数据探索和研究目的。我们不对任何滥用该库的行为负责。

Made with ❤️ by [ScrapeGraph AI](https://scrapegraphai.com)

[Scarf tracking](https://static.scarf.sh/a.png?x-pxid=102d4b8c-cd6a-4b9e-9a16-d6d141b9212d)

```

### File: docs\japanese.md
```md
## 🚀 **さらに高速でシンプルな大規模スクレイピング方法（わずか5行のコード）をお探しですか？** [**ScrapeGraphAI.com**](https://scrapegraphai.com/?utm_source=github&utm_medium=readme&utm_campaign=oss_cta&utm_content=top_banner) の拡張版をご覧ください！🚀

---

# 🕷️ ScrapeGraphAI: 一度のクロールで完結

[English](https://github.com/VinciGit00/Scrapegraph-ai/blob/main/README.md) | [中文](https://github.com/VinciGit00/Scrapegraph-ai/blob/main/docs/chinese.md) | [日本語](https://github.com/VinciGit00/Scrapegraph-ai/blob/main/docs/japanese.md)
| [한국어](https://github.com/VinciGit00/Scrapegraph-ai/blob/main/docs/korean.md)
| [Русский](https://github.com/VinciGit00/Scrapegraph-ai/blob/main/docs/russian.md) | [Türkçe](https://github.com/VinciGit00/Scrapegraph-ai/blob/main/docs/turkish.md)
| [Deutsch](https://www.readme-i18n.com/ScrapeGraphAI/Scrapegraph-ai?lang=de)
| [Español](https://www.readme-i18n.com/ScrapeGraphAI/Scrapegraph-ai?lang=es)
| [français](https://www.readme-i18n.com/ScrapeGraphAI/Scrapegraph-ai?lang=fr)
| [Português](https://github.com/VinciGit00/Scrapegraph-ai/blob/main/docs/portuguese.md)

[![PyPI Downloads](https://static.pepy.tech/personalized-badge/scrapegraphai?period=total&units=INTERNATIONAL_SYSTEM&left_color=BLACK&right_color=GREEN&left_text=downloads)](https://pepy.tech/projects/scrapegraphai)
[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen?style=for-the-badge)](https://github.com/pylint-dev/pylint)
[![Pylint](https://img.shields.io/github/actions/workflow/status/VinciGit00/Scrapegraph-ai/code-quality.yml?label=Pylint&logo=github&style=for-the-badge)](https://github.com/VinciGit00/Scrapegraph-ai/actions/workflows/code-quality.yml)
[![CodeQL](https://img.shields.io/github/actions/workflow/status/VinciGit00/Scrapegraph-ai/codeql.yml?label=CodeQL&logo=github&style=for-the-badge)](https://github.com/VinciGit00/Scrapegraph-ai/actions/workflows/codeql.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![](https://dcbadge.vercel.app/api/server/gkxQDAjfeX)](https://discord.gg/gkxQDAjfeX)

[![API Banner](https://raw.githubusercontent.com/ScrapeGraphAI/Scrapegraph-ai/main/docs/assets/api_banner.png)](https://scrapegraphai.com/?utm_source=github&utm_medium=readme&utm_campaign=api_banner&utm_content=api_banner_image)

<p align="center">
<a href="https://trendshift.io/repositories/9761" target="_blank"><img src="https://trendshift.io/api/badge/repositories/9761" alt="VinciGit00%2FScrapegraph-ai | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
<p align="center">

ScrapeGraphAIは、大規模言語モデルと直接グラフロジックを使用して、ウェブサイトやローカルドキュメント（XML、HTML、JSON、Markdownなど）のクローリングパイプラインを作成するPythonライブラリです。

クロールしたい情報をライブラリに伝えるだけで、残りはすべてライブラリが行います！

<p align="center">
  <img src="https://raw.githubusercontent.com/VinciGit00/Scrapegraph-ai/main/docs/assets/sgai-hero.png" alt="ScrapeGraphAI Hero" style="width: 100%;">
</p>


## 🚀 統合
ScrapeGraphAIは、人気のあるフレームワークやツールとのシームレスな統合を提供し、スクレイピング機能を強化します。PythonまたはNode.jsで構築する場合でも、LLMフレームワークを使用する場合でも、ノーコードプラットフォームで作業する場合でも、包括的な統合オプションを提供しています。

詳細情報は以下の[リンク](https://scrapegraphai.com)で確認できます

**統合**：
- **API**: [ドキュメント](https://docs.scrapegraphai.com/introduction)
- **SDKs**: [Python](https://docs.scrapegraphai.com/sdks/python), [Node](https://docs.scrapegraphai.com/sdks/javascript)
- **LLMフレームワーク**: [Langchain](https://docs.scrapegraphai.com/integrations/langchain), [Llama Index](https://docs.scrapegraphai.com/integrations/llamaindex), [Crew.ai](https://docs.scrapegraphai.com/integrations/crewai), [Agno](https://docs.scrapegraphai.com/integrations/agno), [CamelAI](https://github.com/camel-ai/camel)
- **ローコードフレームワーク**: [Pipedream](https://pipedream.com/apps/scrapegraphai), [Bubble](https://bubble.io/plugin/scrapegraphai-1745408893195x213542371433906180), [Zapier](https://zapier.com/apps/scrapegraphai/integrations), [n8n](http://localhost:5001/dashboard), [Dify](https://dify.ai), [Toolhouse](https://app.toolhouse.ai/mcp-servers/scrapegraph_smartscraper)
- **MCPサーバー**:  [リンク](https://smithery.ai/server/@ScrapeGraphAI/scrapegraph-mcp)

## 🚀 クイックインストール

Scrapegraph-aiの参照ページはPyPIの公式サイトで見ることができます: [pypi](https://pypi.org/project/scrapegraphai/)。

```bash
pip install scrapegraphai

# 重要（ウェブサイトコンテンツの取得用）
playwright install
```

**注意**: 他のライブラリとの競合を避けるため、このライブラリは仮想環境でのインストールを推奨します 🐱


## 💻 使い方
ウェブサイト（またはローカルファイル）から情報を抽出するために使用できる複数の標準スクレイピングパイプラインがあります。

最も一般的なのは `SmartScraperGraph` で、ユーザープロンプトとソースURLが与えられた場合に単一ページから情報を抽出します。


```python
from scrapegraphai.graphs import SmartScraperGraph

# スクレイピングパイプラインの設定を定義
graph_config = {
    "llm": {
        "model": "ollama/llama3.2",
        "model_tokens": 8192,
        "format": "json",
    },
    "verbose": True,
    "headless": False,
}

# SmartScraperGraphインスタンスを作成
smart_scraper_graph = SmartScraperGraph(
    prompt="ウェブページから有用な情報を抽出してください。会社の説明、創設者、ソーシャルメディアリンクを含めてください",
    source="https://scrapegraphai.com/",
    config=graph_config
)

# パイプラインを実行
result = smart_scraper_graph.run()

import json
print(json.dumps(result, indent=4))
```

> [!NOTE]
> OpenAIやその他のモデルの場合は、llm設定を変更するだけです！
> ```python
>graph_config = {
>    "llm": {
>        "api_key": "YOUR_OPENAI_API_KEY",
>        "model": "openai/gpt-4o-mini",
>    },
>    "verbose": True,
>    "headless": False,
>}
>```


出力は次のような辞書になります：

```python
{
    "description": "ScrapeGraphAI transforms websites into clean, organized data for AI agents and data analytics. It offers an AI-powered API for effortless and cost-effective data extraction.",
    "founders": [
        {
            "name": "",
            "role": "Founder & Technical Lead",
            "linkedin": "https://www.linkedin.com/in/perinim/"
        },
        {
            "name": "Marco Vinciguerra",
            "role": "Founder & Software Engineer",
            "linkedin": "https://www.linkedin.com/in/marco-vinciguerra-7ba365242/"
        },
        {
            "name": "Lorenzo Padoan",
            "role": "Founder & Product Engineer",
            "linkedin": "https://www.linkedin.com/in/lorenzo-padoan-4521a2154/"
        }
    ],
    "social_media_links": {
        "linkedin": "https://www.linkedin.com/company/101881123",
        "twitter": "https://x.com/scrapegraphai",
        "github": "https://github.com/ScrapeGraphAI/Scrapegraph-ai"
    }
}
```
複数のページから情報を抽出したり、Pythonスクリプトを生成したり、さらにはオーディオファイルを生成したりするために使用できる他のパイプラインもあります。

| パイプライン名           | 説明                                                                                                      |
|-------------------------|------------------------------------------------------------------------------------------------------------------|
| SmartScraperGraph       | ユーザープロンプトと入力ソースのみが必要な単一ページスクレイパー。                                           |
| SearchGraph             | 検索エンジンの上位n個の検索結果から情報を抽出する複数ページスクレイパー。                  |
| SpeechGraph             | ウェブサイトから情報を抽出し、オーディオファイルを生成する単一ページスクレイパー。                       |
| ScriptCreatorGraph      | ウェブサイトから情報を抽出し、Pythonスクリプトを生成する単一ページスクレイパー。                     |
| SmartScraperMultiGraph  | 単一のプロンプトとソースのリストが与えられた場合に複数のページから情報を抽出する複数ページスクレイパー。    |
| ScriptCreatorMultiGraph | 複数のページとソースから情報を抽出するためのPythonスクリプトを生成する複数ページスクレイパー。     |

これらのグラフのそれぞれには、マルチバージョンがあります。これにより、LLMの呼び出しを並列で行うことができます。

**OpenAI**、**Groq**、**Azure**、**Gemini**などのAPIを介して、または**Ollama**を使用してローカルモデルを使用して、異なるLLMを使用することができます。

ローカルモデルを使用する場合は、[Ollama](https://ollama.com/)がインストールされていること、および**ollama pull**コマンドを使用してモデルをダウンロードしていることを確認してください。


## 📖 ドキュメント

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1sEZBonBMGP44CtO6GQTwAlL0BGJXjtfd?usp=sharing)

ScrapeGraphAIのドキュメントは[こちら](https://scrapegraph-ai.readthedocs.io/en/latest/)で見ることができます。
Docusaurusの[バージョン](https://docs-oss.scrapegraphai.com/)もご覧ください。

## 🤝 貢献

貢献を歓迎し、Discordサーバーで改善や提案について話し合います！

[貢献ガイド](https://github.com/VinciGit00/Scrapegraph-ai/blob/main/CONTRIBUTING.md)をご覧ください。

[![My Skills](https://skillicons.dev/icons?i=discord)](https://discord.gg/uJN7TYcpNa)
[![My Skills](https://skillicons.dev/icons?i=linkedin)](https://www.linkedin.com/company/scrapegraphai/)
[![My Skills](https://skillicons.dev/icons?i=twitter)](https://twitter.com/scrapegraphai)

## 🔗 ScrapeGraph API & SDKs
システムにScrapeGraphを統合するための迅速なソリューションをお探しの場合は、強力なAPIを[こちら！](https://dashboard.scrapegraphai.com/login)でご確認ください。

[![API Banner](https://raw.githubusercontent.com/ScrapeGraphAI/Scrapegraph-ai/main/docs/assets/api_banner.png)](https://dashboard.scrapegraphai.com/login)

PythonとNode.jsの両方でSDKを提供しており、プロジェクトに簡単に統合できます。以下をご覧ください：

| SDK       | 言語 | GitHubリンク                                                                 |
|-----------|----------|-----------------------------------------------------------------------------|
| Python SDK | Python   | [scrapegraph-py](https://github.com/ScrapeGraphAI/scrapegraph-sdk/tree/main/scrapegraph-py) |
| Node.js SDK | Node.js  | [scrapegraph-js](https://github.com/ScrapeGraphAI/scrapegraph-sdk/tree/main/scrapegraph-js) |

公式APIドキュメントは[こちら](https://docs.scrapegraphai.com/)で見ることができます。

## 🔥 ベンチマーク

Firecrawlベンチマーク [Firecrawl benchmark](https://github.com/firecrawl/scrape-evals/pull/3)によると、ScrapeGraphは市場で最高のフェッチャーです！

![here](assets/histogram.png)

## 📈 テレメトリ
パッケージの品質とユーザーエクスペリエンスを向上させるために、匿名の使用メトリクスを収集しています。このデータは、改善の優先順位付けと互換性の確保に役立ちます。オプトアウトする場合は、環境変数SCRAPEGRAPHAI_TELEMETRY_ENABLED=falseを設定してください。詳細については、[こちら](https://scrapegraph-ai.readthedocs.io/en/latest/scrapers/telemetry.html)のドキュメントを参照してください。

## ❤️ 貢献者
[![Contributors](https://contrib.rocks/image?repo=VinciGit00/Scrapegraph-ai)](https://github.com/VinciGit00/Scrapegraph-ai/graphs/contributors)

## 🎓 引用
研究目的で当社のライブラリを使用する場合は、以下の参考文献を引用してください：
```text
  @misc{scrapegraph-ai,
    author = {Lorenzo Padoan, Marco Vinciguerra},
    title = {Scrapegraph-ai},
    year = {2024},
    url = {https://github.com/VinciGit00/Scrapegraph-ai},
    note = {大規模言語モデルを活用したスクレイピング用のPythonライブラリ}
  }
```
## 作者

|                    | 連絡先         |
|--------------------|----------------------|
| Marco Vinciguerra  | [![Linkedin Badge](https://img.shields.io/badge/-Linkedin-blue?style=flat&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/marco-vinciguerra-7ba365242/)    |
| Lorenzo Padoan     | [![Linkedin Badge](https://img.shields.io/badge/-Linkedin-blue?style=flat&logo=Linkedin&logoColor=white)](https://www.linkedin.com/in/lorenzo-padoan-4521a2154/)  |

## 📜 ライセンス

ScrapeGraphAIはMITライセンスの下で提供されています。詳細は[LICENSE](https://github.com/VinciGit00/Scrapegraph-ai/blob/main/LICENSE)ファイルをご覧ください。

## 謝辞

- プロジェクトの貢献者とオープンソースコミュニティのサポートに感謝します。
- ScrapeGraphAIはデータ探索と研究目的のみに使用されます。このライブラリの不正使用については一切責任を負いません。

Made with ❤️ by [ScrapeGraph AI](https://scrapegraphai.com)

[Scarf tracking](https://static.scarf.sh/a.png?x-pxid=102d4b8c-cd6a-4b9e-9a16-d6d141b9212d)

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
