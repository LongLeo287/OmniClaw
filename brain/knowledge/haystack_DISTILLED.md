---
id: haystack
type: knowledge
owner: OA_Triage
---
# haystack
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<div align="center">
  <a href="https://haystack.deepset.ai/"><img src="https://raw.githubusercontent.com/deepset-ai/haystack/main/images/banner.png" alt="Blue banner with the Haystack logo and the text ‘haystack by deepset – The Open Source AI Framework for Production Ready RAG & Agents’ surrounded by abstract icons representing search, documents, agents, pipelines, and cloud systems."></a>

|         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| CI/CD   | [![Tests](https://github.com/deepset-ai/haystack/actions/workflows/tests.yml/badge.svg)](https://github.com/deepset-ai/haystack/actions/workflows/tests.yml) [![types - Mypy](https://img.shields.io/badge/types-Mypy-blue.svg)](https://github.com/python/mypy) [![Coverage Status](https://coveralls.io/repos/github/deepset-ai/haystack/badge.svg?branch=main)](https://coveralls.io/github/deepset-ai/haystack?branch=main) [![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff) |
| Docs    | [![Website](https://img.shields.io/website?label=documentation&up_message=online&url=https%3A%2F%2Fdocs.haystack.deepset.ai)](https://docs.haystack.deepset.ai)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Package | [![PyPI](https://img.shields.io/pypi/v/haystack-ai)](https://pypi.org/project/haystack-ai/) ![PyPI - Downloads](https://img.shields.io/pypi/dm/haystack-ai?color=blue&logo=pypi&logoColor=gold) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/haystack-ai?logo=python&logoColor=gold) [![Conda Version](https://img.shields.io/conda/vn/conda-forge/haystack-ai.svg)](https://anaconda.org/conda-forge/haystack-ai) [![GitHub](https://img.shields.io/github/license/deepset-ai/haystack?color=blue)](LICENSE) [![License Compliance](https://github.com/deepset-ai/haystack/actions/workflows/license_compliance.yml/badge.svg)](https://github.com/deepset-ai/haystack/actions/workflows/license_compliance.yml) |
| Meta    | [![Discord](https://img.shields.io/discord/993534733298450452?logo=discord)](https://discord.com/invite/xYvH6drSmA) [![Twitter Follow](https://img.shields.io/twitter/follow/haystack_ai)](https://twitter.com/haystack_ai)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
</div>

[Haystack](https://haystack.deepset.ai/) is an open-source AI orchestration framework for building production-ready LLM applications in Python.

Design modular pipelines and agent workflows with explicit control over retrieval, routing, memory, and generation. Build scalable RAG systems, multimodal applications, semantic search, question answering, and autonomous agents, all in a transparent architecture that lets you experiment, customize deeply, and deploy with confidence.

## Table of Contents

- [Installation](#installation)
- [Documentation](#documentation)
- [Features](#features)
- [Haystack Enterprise: Support & Platform](#haystack-enterprise-support--platform)
- [Telemetry](#telemetry)
- [🖖 Community](#-community)
- [Contributing to Haystack](#contributing-to-haystack)
- [Organizations using Haystack](#organizations-using-haystack)


## Installation

The simplest way to get Haystack is via pip:

```sh
pip install haystack-ai
```

Install nightly pre-releases to try the newest features:
```sh
pip install --pre haystack-ai
```

Haystack supports multiple installation methods, including Docker images. For a comprehensive guide, please refer
to the [documentation](https://docs.haystack.deepset.ai/docs/installation).

## Documentation

If you're new to the project, check out ["What is Haystack?"](https://haystack.deepset.ai/overview/intro) then go
through the ["Get Started Guide"](https://haystack.deepset.ai/overview/quick-start) and build your first LLM application
in a matter of minutes. Keep learning with the [tutorials](https://haystack.deepset.ai/tutorials). For more advanced
use cases, or just to get some inspiration, you can browse our Haystack recipes in the
[Cookbook](https://haystack.deepset.ai/cookbook).

At any given point, hit the [documentation](https://docs.haystack.deepset.ai/docs/intro) to learn more about Haystack, what it can do for you, and the technology behind.

## Features

**Built for context engineering**  
Design flexible systems with explicit control over how information is retrieved, ranked, filtered, combined, structured, and routed before it reaches the model. Define pipelines and agent workflows where retrieval, memory, tools, and generation are transparent and traceable.

**Model- and vendor-agnostic**  
Integrate with OpenAI, Mistral, Anthropic, Cohere, Hugging Face, Azure OpenAI, AWS Bedrock, local models, and many others. Swap models or infrastructure components without rewriting your system.

**Modular and customizable**  
Use built-in components for retrieval, indexing, tool calling, memory, and evaluation, or create your own. Add loops, branches, and conditional logic to precisely control how context moves through your pipelines and agent workflows.

**Extensible ecosystem**  
Build and share custom components through a consistent interface that makes it easy for the community and third parties to extend Haystack and contribute to an open ecosystem.

> [!TIP]
> 
> Would you like to deploy and serve Haystack pipelines as **REST APIs** or **MCP servers**? [Hayhooks](https://github.com/deepset-ai/hayhooks) provides a simple way for you to wrap pipelines and agents with custom logic and expose them through HTTP endpoints or MCP. It also supports OpenAI-compatible chat completion endpoints and works with chat UIs like [open-webui](https://openwebui.com/).

## Haystack Enterprise: Support & Platform

Get expert support from the Haystack team, build faster with enterprise-grade templates, and scale securely with deployment guides for cloud and on-prem environments with **Haystack Enterprise Starter**. Read more about it in the [announcement post](https://haystack.deepset.ai/blog/announcing-haystack-enterprise).

👉 [Get Haystack Enterprise Starter](https://www.deepset.ai/products-and-services/haystack-enterprise-starter?utm_source=github.com&utm_medium=referral&utm_campaign=haystack_enterprise)

Need a managed production setup for Haystack? The **Haystack Enterprise Platform** helps you build, test, deploy and operate Haystack pipelines with built-in observability, collaboration, governance, and access controls. It’s available as a managed cloud service or as a self-hosted solution.

👉 Learn more about [Haystack Enterprise Platform](https://www.deepset.ai/products-and-services/haystack-enterprise-platform?utm_campaign=developer-relations&utm_source=haystack&utm_medium=readme) or [try it free](https://www.deepset.ai/haystack-enterprise-platform-trial?utm_campaign=developer-relations&utm_source=haystack&utm_medium=readme)

## Telemetry

Haystack collects **anonymous** usage statistics of pipeline components. We receive an event every time these components are initialized. This way, we know which components are most relevant to our community.

Read more about telemetry in Haystack or how you can opt out in [Haystack docs](https://docs.haystack.deepset.ai/docs/telemetry).

## 🖖 Community

If you have a feature request or a bug report, feel free to open an [issue in GitHub](https://github.com/deepset-ai/haystack/issues). We regularly check these, so you can expect a quick response. If you'd like to discuss a topic or get more general advice on how to make Haystack work for your project, you can start a thread in [Github Discussions](https://github.com/deepset-ai/haystack/discussions) or our [Discord channel](https://discord.com/invite/VBpFzsgRVF). We also check [𝕏 (Twitter)](https://twitter.com/haystack_ai) and [Stack Overflow](https://stackoverflow.com/questions/tagged/haystack).

## Contributing to Haystack

We are very open to the community's contributions - be it a quick fix of a typo, or a completely new feature! You don't need to be a Haystack expert to provide meaningful improvements. To learn how to get started, check out our [Contributor Guidelines](https://github.com/deepset-ai/haystack/blob/main/CONTRIBUTING.md) first.

There are several ways you can contribute to Haystack:
- Contribute to the main Haystack project
- Contribute an integration on [haystack-core-integrations](https://github.com/deepset-ai/haystack-core-integrations)
- Contribute to the documentation in [haystack/docs-website](https://github.com/deepset-ai/haystack/tree/main/docs-website)

> [!TIP]
>👉 **[Check out the full list of issues that are open to contributions](https://github.com/orgs/deepset-ai/projects/14)**

## Organizations using Haystack

Haystack is used by thousands of teams building production AI systems across industries, including:

- **Technology & AI Infrastructure**: [Apple](https://www.apple.com/), [Meta](https://www.meta.com/about), [Databricks](https://www.databricks.com/), [NVIDIA](https://developer.nvidia.com/blog/reducing-development-time-for-intelligent-virtual-assistants-in-contact-centers/), [Intel](https://github.com/intel/open-domain-question-and-answer#readme)
- **Public Sector AI Initiatives**: [European Commission](https://commission.europa.eu/index_en), [German Federal Ministry of Research, Technology, and Space (BMFTR)](https://www.deepset.ai/case-studies/german-federal-ministry-research-technology-space-bmftr), [PD, Baden-Württemberg State](https://www.pd-g.de/)
- **Enterprise & Industrial AI Applications**: [Airbus](https://www.deepset.ai/case-studies/airbus), [Lufthansa Industry Solutions](https://haystack.deepset.ai/blog/lufthansa-user-story), [Infineon](https://www.infineon.com/), [LEGO](https://github.com/larsbaunwall/bricky#readme), [Comcast](https://arxiv.org/html/2405.00801v2), [Accenture](https://www.accenture.com/), [TELUS Agriculture & Consumer Goods](https://www.telus.com/agcg/en)
- **Knowledge & Content Platforms**: [Netflix](https://netflix.com), [ZEIT Online](https://www.deepset.ai/case-studies/zeit-online), [Rakuten](https://www.rakuten.com/), [Oxford University Press](https://corp.oup.com/), [Manz](https://www.deepset.ai/case-studies/manz), [YPulse](https://www.deepset.ai/case-studies/ypulse)


Are you also using Haystack? Open a PR or [tell us your story](https://forms.gle/Mm3G1aEST3GAH2rn8)

```

### File: docker\README.md
```md
<p align="center">
  <a href="https://haystack.deepset.ai/"><img src="https://raw.githubusercontent.com/deepset-ai/.github/main/haystack-logo-colored.png" alt="Haystack by deepset"></a>
</p>

[Haystack](https://github.com/deepset-ai/haystack) is an end-to-end LLM framework that allows you to build applications powered by LLMs, Transformer models, vector search and more. Whether you want to perform retrieval-augmented generation (RAG), document search, question answering or answer generation, Haystack can orchestrate state-of-the-art embedding models and LLMs into pipelines to build end-to-end NLP applications and solve your use case.

## Haystack 2.x

For the latest version of Haystack there's only one image available:

- `haystack:base-<version>` contains a working Python environment with Haystack preinstalled. This image is expected to
  be derived `FROM`.

## Image Development

Images are built with BuildKit and we use `bake` to orchestrate the process.
You can build a specific image by running:
```sh
docker buildx bake base
```

You can override any `variable` defined in the `docker-bake.hcl` file and build custom
images, for example if you want to use a branch from the Haystack repo, run:
```sh
HAYSTACK_VERSION=mybranch_or_tag BASE_IMAGE_TAG_SUFFIX=latest docker buildx bake base --no-cache
```

### Multi-Platform Builds

Haystack images support multiple architectures. But depending on your operating system and Docker
environment, you might not be able to build all of them locally.

You may encounter the following error when trying to build the image:

```
multiple platforms feature is currently not supported for docker driver. Please switch to a different driver
(eg. “docker buildx create --use”)
```

To get around this, you need to override the `platform` option and limit local builds to the same architecture as
your computer's. For example, on an Apple M1 you can limit the builds to ARM only by invoking `bake` like this:

```sh
docker buildx bake base --set "*.platform=linux/arm64"
```

# License

View [license information](https://github.com/deepset-ai/haystack/blob/main/LICENSE) for
the software contained in this image.

As with all Docker images, these likely also contain other software which may be under
other licenses (such as Bash, etc from the base distribution, along with any direct or
indirect dependencies of the primary software being contained).

As for any pre-built image usage, it is the image user's responsibility to ensure that any
use of this image complies with any relevant licenses for all software contained within.

```

### File: examples\README.md
```md
# Examples have been moved!

If you're searching for Haystack examples we moved them into a dedicated repository.

You can find all the example cookbooks [👉 here 👈](https://github.com/deepset-ai/haystack-cookbook/).

```

### File: .pre-commit-config.yaml
```yaml
fail_fast: true

repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v6.0.0
    hooks:
      - id: check-ast # checks Python syntax
      - id: check-json # checks JSON syntax
      - id: check-merge-conflict # checks for no merge conflict strings
      - id: check-shebang-scripts-are-executable # checks all shell scripts have executable permissions
      - id: check-toml # checks TOML syntax
      - id: check-yaml # checks YAML syntax
      - id: end-of-file-fixer # checks there is a newline at the end of the file
      - id: mixed-line-ending # normalizes line endings
      - id: no-commit-to-branch # prevents committing to main
      - id: trailing-whitespace # trims trailing whitespace
        args: [--markdown-linebreak-ext=md, --markdown-linebreak-ext=mdx]

  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.15.2
    hooks:
    - id: ruff-check
      args: [ --fix ]
    - id: ruff-format

  - repo: local
    hooks:
      - id: ruff-format-docs
        name: ruff-format-docs
        language: python
        entry: python scripts/ruff_format_docs.py --line-length=88
        files: ^docs-website/.*\.mdx$
        types: [text]
        additional_dependencies:
          - ruff
          - add-trailing-comma

  - repo: https://github.com/codespell-project/codespell
    rev: v2.4.1
    hooks:
      - id: codespell
        exclude: "haystack/data/abbreviations"
        args: ["--toml", "pyproject.toml"]
        additional_dependencies:
          - tomli

  - repo: https://github.com/rhysd/actionlint
    rev: v1.7.10
    hooks:
      - id: actionlint-docker
        args: ["-ignore", "SC2102"]

```

### File: AGENTS.md
```md
# Haystack Guidelines for AI Agents

## Environment

Haystack uses **Hatch** for environment and dependency management.

Do not run `python` or `pip` directly.

Before running code on this project, you must be able to run `hatch --version` and get a correct output.

If not, ask the user where Hatch is or if they want to install it. For installation instructions, refer to https://hatch.pypa.io/latest/install/#installation.

### Run scripts with test dependencies

hatch -e test run python SCRIPT.py

### Open a shell with test dependencies

hatch -e test shell

### Install temporary dependencies (for experiments only)

uv pip install PACKAGE

### Delete the environment

hatch env prune

## Tests

Tests run via Hatch and support pytest arguments.

Prefer running tests on a specific module or using `-k`, since the full suite is large.

### Run unit tests

hatch run test:unit

### Run integration tests

hatch run test:integration

## Quality Checks

### Type checking with mypy
hatch run test:types

To fix type issues, avoid `type: ignore`, casts, or assertions when possible. If they are necessary, explain why.

### Format and lint
hatch run fmt

## Release Notes

Every user-facing PR (not docs, not CI) must include a release note:

hatch run release-note SHORT_DESCRIPTION

Edit the generated file in `releasenotes/notes/`.

```

### File: CLAUDE.md
```md
# CLAUDE.md

Before you start working on this repository, read the AGENTS.md file and follow all the instructions.

```

### File: code_of_conduct.txt
```txt
CONTRIBUTOR COVENANT CODE OF CONDUCT
====================================

Our Pledge
----------

We as members, contributors, and leaders pledge to make participation in our community a harassment-free experience for
everyone, regardless of age, body size, visible or invisible disability, ethnicity, sex characteristics,
gender identity and expression, level of experience, education, socioeconomic status, nationality, personal appearance,
race, caste, color, religion, or sexual identity and orientation.

We pledge to act and interact in ways that contribute to an open, welcoming, diverse, inclusive, and healthy community.

Our Standards
-------------

Examples of behavior that contributes to a positive environment for our community include:
    - Demonstrating empathy and kindness toward other people
    - Being respectful of differing opinions, viewpoints, and experiences
    - Giving and gracefully accepting constructive feedback
    - Accepting responsibility and apologizing to those affected by our mistakes, and learning from the experience
    - Focusing on what is best not just for us as individuals, but for the overall community

Examples of unacceptable behavior include:
    - The use of sexualized language or imagery, and sexual attention or advances of any kind
    - Trolling, insulting or derogatory comments, and personal or political attacks
    - Public or private harassment
    - Publishing others’ private information, such as a physical or email address, without their explicit permission
    - Other conduct which could reasonably be considered inappropriate in a professional setting

Enforcement Responsibilities
----------------------------

Community leaders are responsible for clarifying and enforcing our standards of acceptable behavior and will take
appropriate and fair corrective action in response to any behavior that they deem inappropriate,
threatening, offensive, or harmful.

Community leaders have the right and responsibility to remove, edit, or reject comments, commits, code, wiki edits,
issues, and other contributions that are not aligned to this Code of Conduct, and will communicate reasons for
moderation decisions when appropriate.

Scope
-----

This Code of Conduct applies within all community spaces, and also applies when an individual is officially
representing the community in public spaces. Examples of representing our community include using an official
e-mail address, posting via an official social media account, or acting as an appointed representative
at an online or offline event.

Enforcement
-----------

Instances of abusive, harassing, or otherwise unacceptable behavior may be reported to the community leaders responsible
for enforcement at engage@deepset.ai. All complaints will be reviewed and investigated promptly and fairly.

All community leaders are obligated to respect the privacy and security of the reporter of any incident.

Enforcement Guidelines
----------------------

Community leaders will follow these Community Impact Guidelines in determining the consequences for any action
they deem in violation of this Code of Conduct:

1. Correction
    Community Impact: Use of inappropriate language or other behavior deemed unprofessional or unwelcome in the community.

    Consequence: A private, written warning from community leaders, providing clarity around the nature of the violation
    and an explanation of why the behavior was inappropriate. A public apology may be requested.

2. Warning
    Community Impact: A violation through a single incident or series of actions.

    Consequence: A warning with consequences for continued behavior. No interaction with the people involved,
    including unsolicited interaction with those enforcing the Code of Conduct, for a specified period of time.
    This includes avoiding interactions in community spaces as well as external channels like social media.
    Violating these terms may lead to a temporary or permanent ban.

3. Temporary Ban
    Community Impact: A serious violation of community standards, including sustained inappropriate behavior.

    Consequence: A temporary ban from any sort of interaction or public communication with the community for a specified
    period of time. No public or private interaction with the people involved, including unsolicited interaction with
    those enforcing the Code of Conduct, is allowed during this period. Violating these terms may lead to a permanent ban.

4. Permanent Ban
    Community Impact: Demonstrating a pattern of violation of community standards, including sustained inappropriate behavior, harassment of an individual, or aggression toward or disparagement of classes of individuals.

    Consequence: A permanent ban from any sort of public interaction within the community.

Attribution
-----------

This Code of Conduct is adapted from the Contributor Covenant, version 2.0, available at https://www.contributor-covenant.org/version/2/0/code_of_conduct.html.

Community Impact Guidelines were inspired by Mozilla’s code of conduct enforcement ladder.

For answers to common questions about this code of conduct, see the FAQ at https://www.contributor-covenant.org/faq.
Translations are available at https://www.contributor-covenant.org/translations.

```

### File: CONTRIBUTING.md
```md
# Contributing to Haystack

First off, thanks for taking the time to contribute! :blue_heart:

All types of contributions are encouraged and valued. See the [Table of Contents](#table-of-contents)
for different ways to help and details about how this project handles them. Please make sure to read
the relevant section before making your contribution. It will make it a lot easier for us maintainers
and smooth out the experience for all involved. The community looks forward to your contributions!

> [!TIP]
> If you like Haystack but just don't have time to contribute, that's fine. There are other easy ways to support the
> project and show your appreciation: star this repository ⭐, mention Haystack at local meetups and tell your
> friends/colleagues, or share what you build and tag [Haystack on X (Twitter)](https://x.com/Haystack_ai) and
> [Haystack on LinkedIn](https://www.linkedin.com/showcase/haystack-ai-framework) — we'd love to see it!

## Your first PR — high-level to-do list

Use this checklist to stay on track for your first code PR:

- **Pick an issue** — Choose one labeled [good first issue](https://github.com/deepset-ai/haystack/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22) or [contributions wanted](https://github.com/deepset-ai/haystack/issues?q=is%3Aissue%20state%3Aopen%20label%3A"Contributions%20wanted!"). Avoid issues marked or commented as [handled internally](#issues-not-open-for-external-contributions).
- **Fork and clone** — [Clone the repository](#clone-the-git-repository), run `pre-commit install`, and create a branch.
- **Set up and run** — [Set up your development environment](#setting-up-your-development-environment), run unit tests with `hatch run test:unit` and run quality checks with `hatch run test:types` and `hatch run fmt`.
- **Implement and test** — Make your changes, add or update tests as needed, and ensure tests and pre-commit checks pass locally.
- **Documentation** — If your change adds or alters user-facing behavior, add a new docs page or update the relevant one in `docs-website/` (edit under `docs/` for the next release; add new pages to `sidebars.js`). See the [Documentation Contributing Guide](docs-website/CONTRIBUTING.md) for where to edit, frontmatter, and navigation.
- **Release notes** — Add a release note under `releasenotes/notes` with `hatch run release-note your-change-name` (see [Release notes](#release-notes)); maintainers can add `ignore-for-release-notes` for tests-only or CI-only changes.
- **Open the PR** — Use a [conventional commit](https://www.conventionalcommits.org/en/v1.0.0/) title, fill the [PR template](.github/pull_request_template.md), and if the PR was fully AI-generated, add a [short disclaimer](#using-ai-assistants-to-contribute). Enable "Allow edits and access to secrets by maintainers" on the PR.
- **Sign the CLA** — A [Contributor Licence Agreement (CLA)](https://cla-assistant.io/deepset-ai/haystack) is required for all contributions. Sign when prompted so your PR is ready for review (see [CLA](#contributor-licence-agreement-cla)).
- **Once the PR is open** — Fix any [CI](#ci-continuous-integration) failures and address review feedback.

**Table of Contents**

- [Contributing to Haystack](#contributing-to-haystack)
  - [Your first PR — high-level to-do list](#your-first-pr--high-level-to-do-list)
  - [Code of Conduct](#code-of-conduct)
  - [I Have a Question](#i-have-a-question)
  - [Reporting Bugs](#reporting-bugs)
    - [Before Submitting a Bug Report](#before-submitting-a-bug-report)
    - [How Do I Submit a Good Bug Report?](#how-do-i-submit-a-good-bug-report)
  - [Suggesting Enhancements](#suggesting-enhancements)
    - [Before Submitting an Enhancement](#before-submitting-an-enhancement)
    - [How Do I Submit a Good Enhancement Suggestion?](#how-do-i-submit-a-good-enhancement-suggestion)
  - [Contributing to Documentation](#contributing-to-documentation)
  - [Contribute code](#contribute-code)
    - [Where to start](#where-to-start)
    - [Issues not open for external contributions](#issues-not-open-for-external-contributions)
    - [Example high-quality contributions](#example-high-quality-contributions)
    - [Using AI assistants to contribute](#using-ai-assistants-to-contribute)
    - [Setting up your development environment](#setting-up-your-development-environment)
    - [Clone the git repository](#clone-the-git-repository)
    - [Run the tests locally](#run-the-tests-locally)
  - [Requirements for Pull Requests](#requirements-for-pull-requests)
    - [Release notes](#release-notes)
  - [CI (Continuous Integration)](#ci-continuous-integration)
  - [Working from GitHub forks](#working-from-github-forks)
  - [Writing tests](#writing-tests)
    - [Unit test](#unit-test)
    - [Integration test](#integration-test)
    - [End to End (e2e) test](#end-to-end-e2e-test)
    - [Slow/unstable integration tests (for maintainers)](#slowunstable-integration-tests-for-maintainers)
  - [Contributor Licence Agreement (CLA)](#contributor-licence-agreement-cla)

## Code of Conduct

This project and everyone participating in it is governed by our [Code of Conduct](code_of_conduct.txt).
By participating, you are expected to uphold this code. Please report unacceptable behavior to haystack@deepset.ai.

## I Have a Question

Before you ask a question, it is best to search for existing [Issues](https://github.com/deepset-ai/haystack/issues) that might help you. In case you have
found a suitable issue and still need clarification, you can write your question in this issue. It is also advisable to
search the internet for answers first.

If you then still feel the need to ask a question and need clarification, you can use [Haystack's Discord Server](https://discord.com/invite/xYvH6drSmA).

## Reporting Bugs

### Before Submitting a Bug Report

A good bug report shouldn't leave others needing to chase you up for more information. Therefore, we ask you to
investigate carefully, collect information, and describe the issue in detail in your report. Please complete the
following steps in advance to help us fix any potential bugs as fast as possible.

- Make sure that you are using the latest version.
- Determine if your bug is really a bug and not an error on your side, for example, using incompatible versions.
  Make sure that you have read the [documentation](https://docs.haystack.deepset.ai/docs/intro). If you are looking
  for support, you might want to check [this section](#i-have-a-question).
- To see if other users have experienced (and potentially already solved) the same issue you are having, check if there
  is not already a bug report existing for your bug or error in the [bug tracker](https://github.com/deepset-ai/haystack/issues).
- Also make sure to search the internet (including Stack Overflow) to see if users outside of the GitHub community have
  discussed the issue.
- Collect information about the bug:
  - OS, Platform and Version (Windows, Linux, macOS, x86, ARM)
  - Version of Haystack and the integrations you're using
  - Possibly your input and the output
  - If you can reliably reproduce the issue, a snippet of code we can use

### How Do I Submit a Good Bug Report?

> [!IMPORTANT]
> You must never report security-related issues, vulnerabilities, or bugs, including sensitive information, to the issue tracker, or elsewhere in public. Instead, sensitive bugs must be reported using [this link](https://github.com/deepset-ai/haystack/security/advisories/new).

We use GitHub issues to track bugs and errors. If you run into an issue with the project:

- Open an [Issue of type Bug Report](https://github.com/deepset-ai/haystack/issues/new?assignees=&labels=bug&projects=&template=bug_report.md&title=).
- Explain the behavior you would expect and the actual behavior.
- Please provide as much context as possible and describe the *reproduction steps* that someone else can follow to
  recreate the issue on their own. This usually includes your code. For good bug reports, you should isolate the problem
  and create a reduced test case.
- Provide the information you collected in the previous section.

Once it's filed:

- The project team will label the issue accordingly.
- A team member will try to reproduce the issue with your provided steps. If there are no reproduction steps or no
  obvious way to reproduce the issue, the team will ask you for those steps.
- If the team is able to reproduce it, the issue will be scheduled for a fix or left to be
  [picked up by a community contributor](https://github.com/deepset-ai/haystack/issues?q=is%3Aissue%20state%3Aopen%20label%3A"Contributions%20wanted!").

## Suggesting Enhancements

This section guides you through submitting an enhancement suggestion, including new integrations and improvements
to existing ones. Following these guidelines will help maintainers and the community to understand your suggestion and
find related suggestions.

### Before Submitting an Enhancement

- Make sure that you are using the latest version.
- Read the [documentation](https://docs.haystack.deepset.ai/docs/intro) carefully and find out if the functionality
  is already covered, possibly via particular configuration parameters.
- Perform a [search](https://github.com/deepset-ai/haystack/issues) to see if the enhancement has already been suggested. If it has, add a comment to the
  existing issue instead of opening a new one.
- Find out whether your idea fits with the scope and aims of the project. It's up to you to make a strong case to
  convince the project's developers of the merits of this feature. Keep in mind that we want features that will be
  useful to the majority of our users and not just a small subset. If you're just targeting a minority of users,
  consider writing and distributing the integration on your own.

### How Do I Submit a Good Enhancement Suggestion?

Enhancement suggestions are tracked as GitHub issues of type [Feature request](https://github.com/deepset-ai/haystack/issues/new?template=feature_request.md).

- Use a **clear and descriptive title** for the issue to identify the suggestion.
- Fill in the issue following the template

## Contributing to Documentation

If you'd like to improve the documentation by fixing errors, clarifying explanations, adding examples, or creating new guides, see the [Documentation Contributing Guide](docs-website/CONTRIBUTING.md).

## Contribute code

> [!IMPORTANT]
> When contributing to this project, you must agree that you have authored or carefully reviewed 100% of the content, that you have the necessary rights to the content and that the content you contribute may be provided under the project license.

### Where to start

If this is your first code contribution, a good starting point is looking for an open issue that's marked with the label
["good first issue"](https://github.com/deepset-ai/haystack/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22).
The core contributors periodically mark certain issues as good for first-time contributors. Those issues are usually
limited in scope, easily fixable and low priority, so there is absolutely no reason why you should not try fixing them.
It's a good excuse to start looking into the project and a safe space to experiment and fail: if you don't get the
grasp of something, pick another one! Once you become comfortable contributing to Haystack, you can have a look at the
list of issues marked as [contributions wanted](https://github.com/orgs/deepset-ai/projects/14/views/1) to look for your
next contribution!

### Issues not open for external contributions

Some issues are handled internally by the core team and are **not open for external contributions**. You may see a
comment on such issues like:

> 👋 Hello there! This issue will be handled internally and isn't open for external contributions. If you'd like to contribute, please take a look at issues labeled **contributions welcome** or **good first issue**. We'd really appreciate it!

> [!WARNING]
> **Please do not open pull requests for issues that are marked or commented as handled internally.** Your work may not be merged. Instead, look for issues labeled [good first issue](https://github.com/deepset-ai/haystack/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22) or [contributions wanted](https://github.com/deepset-ai/haystack/issues?q=is%3Aissue%20state%3Aopen%20label%3A"Contributions%20wanted!") — we'd love your help there!

### Example high-quality contributions

Looking at strong pull requests is a great way to learn our standards. Example high-quality PRs: [#9270](https://github.com/deepset-ai/haystack/pull/9270), [#9227](https://github.com/deepset-ai/haystack/pull/9227), [#9271](https://github.com/deepset-ai/haystack/pull/9271), [#8648](https://github.com/deepset-ai/haystack/pull/8648), [#8767](https://github.com/deepset-ai/haystack/pull/8767). Use them as references for structure, testing, documentation, and how to describe changes in the PR description and release notes.

### Using AI assistants to contribute

You may use AI assistants or agents to help you implement a contribution. Please use them wisely:

- **Review and understand** all generated code before submitting. You are responsible for the contribution.
- **Run tests and checks** locally (e.g. `hatch run test:unit`, `hatch run fmt`) so your PR meets our quality bar.
- **If your PR was fully AI-generated**, add a short disclaimer in the PR description, for example: *"This PR was
  fully generated with an AI assistant. I have reviewed the changes and run the relevant tests."*

This helps maintainers and keeps the project ready for both human and AI contributors.

### Setting up your development environment

*To run Haystack tests locally, ensure your development environment uses Python >=3.10 and <3.14.*

Haystack makes heavy use of [Hatch](https://hatch.pypa.io/latest/), a Python project manager that we use to set up the
virtual environments, build the project, and publish packages. As you can imagine, the first step towards becoming a
Haystack contributor is installing Hatch. There are a variety of installation methods depending on your operating system
platform, version, and personal taste: please have a look at [this page](https://hatch.pypa.io/latest/install/#installation)
and keep reading once you can run from your terminal:

```console
$ hatch --version
Hatch, version 1.14.1
```

You can create a new virtual environment for Haystack with `hatch` by running:

```console
$ hatch shell
```

### Clone the git repository

You won't be able to make changes directly to this repo, so the first step is to [create a fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo).
Once your fork is ready, you can clone a local copy with:

```console
$ git clone https://github.com/YOUR-USERNAME/haystack
```

If everything worked, you should be able to do something like this (the output might be different):

```console
$ cd hayst
... [TRUNCATED]
```

### File: license-header.txt
```txt
SPDX-FileCopyrightText: {{ props["inceptionYear"] }}-present {{ props["copyrightOwner"] }}

SPDX-License-Identifier: Apache-2.0

```

### File: SECURITY.md
```md
# Security Policy

## Report a Vulnerability

If you have found a security vulnerability in Haystack, please report via email to
[opensource-security@deepset.ai](mailto:opensource-security@deepset.ai).

In your message, please include:

1. Reproducible steps to trigger the vulnerability.
2. An explanation of what makes you think there is a vulnerability.
3. Any information you may have on active exploitations of the vulnerability (zero-day).
4. An explanation of why you believe the vulnerability is not out of scope. See the Out of Scope section below.

We encourage reports that are meaningful, high-impact, and reviewed by a human before submission. Fully automated or AI-generated reports submitted without human review and validation are unlikely to meet this bar and risk being declined.

## Out of Scope

Haystack is a framework intended to run inside a trusted execution environment. It assumes that the application built with it has already validated and sanitized user-supplied input before passing it to the framework. Validation and sanitization of input, for example URLs, file paths, filter expressions, and queries, are the responsibility of the application, not Haystack.

Any vulnerability that can only be triggered by passing unsanitized, attacker-controlled input to Haystack is considered out of scope. This reflects a conscious design decision after evaluating the trade-offs and risks: as a framework, Haystack cannot and should not enforce input validation on behalf of every application that uses it.

If you are uncertain whether a finding falls within scope, feel free to reach out before submitting a full report.

## Vulnerability Response

We aim to review your report within 5 business days where we do a preliminary analysis
to confirm that the vulnerability is plausible. Otherwise, we'll decline the report.

We won't disclose any information you share with us but we'll use it to get the issue
fixed or to coordinate a vendor response, as needed.

We'll keep you updated of the status of the issue.

Our goal is to disclose bugs as soon as possible once a user mitigation is available.
Once we get a good understanding of the vulnerability, we'll set a disclosure date after
consulting the author of the report and Haystack maintainers.

```

### File: VERSION.txt
```txt
2.28.0-rc0

```

### File: .github\pull_request_template.md
```md
### Related Issues

- fixes #issue-number

### Proposed Changes:

 <!--- In case of a bug: Describe what caused the issue and how you solved it -->
 <!--- In case of a feature: Describe what did you add and how it works -->

### How did you test it?

<!-- unit tests, integration tests, manual verification, instructions for manual tests -->

### Notes for the reviewer

<!-- E.g. point out section where the reviewer  -->

### Checklist

- I have read the [contributors guidelines](https://github.com/deepset-ai/haystack/blob/main/CONTRIBUTING.md) and the [code of conduct](https://github.com/deepset-ai/haystack/blob/main/code_of_conduct.txt).
- I have updated the related issue with new insights and changes.
- I have added unit tests and updated the docstrings.
- I've used one of the [conventional commit types](https://www.conventionalcommits.org/en/v1.0.0/) for my PR title: `fix:`, `feat:`, `build:`, `chore:`, `ci:`, `docs:`, `style:`, `refactor:`, `perf:`, `test:` and added `!` in case the PR includes breaking changes.
- I have documented my code.
- I have added a release note file, following the [contributors guidelines](https://github.com/deepset-ai/haystack/blob/main/CONTRIBUTING.md#release-notes).
- I have run [pre-commit hooks](https://github.com/deepset-ai/haystack/blob/main/CONTRIBUTING.md#installation) and fixed any issue.

```

### File: e2e\conftest.py
```py
# SPDX-FileCopyrightText: 2022-present deepset GmbH <info@deepset.ai>
#
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path

import pytest

from haystack.testing.test_utils import set_all_seeds

set_all_seeds(0)


@pytest.fixture
def samples_path():
    return Path(__file__).parent / "samples"


@pytest.fixture
def del_hf_env_vars(monkeypatch):
    """
    Delete Hugging Face environment variables for tests.

    Prevents passing empty tokens to Hugging Face, which would cause API calls to fail.
    This is particularly relevant for PRs opened from forks, where secrets are not available
    and empty environment variables might be set instead of being removed.

    See https://github.com/deepset-ai/haystack/issues/8811 for more details.
    """
    monkeypatch.delenv("HF_API_TOKEN", raising=False)
    monkeypatch.delenv("HF_TOKEN", raising=False)

```

### File: e2e\__init__.py
```py
# SPDX-FileCopyrightText: 2022-present deepset GmbH <info@deepset.ai>
#
# SPDX-License-Identifier: Apache-2.0

```

### File: scripts\ruff_format_docs.py
```py
# SPDX-FileCopyrightText: 2022-present deepset GmbH <info@deepset.ai>
#
# SPDX-License-Identifier: Apache-2.0

"""
Pre-commit hook that runs ruff format on Python code blocks in Markdown/MDX files.

Uses the ruff configuration from pyproject.toml automatically.
"""

import argparse
import logging
import os
import re
import subprocess
import sys
import tempfile

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stderr)
handler.setFormatter(logging.Formatter("%(message)s"))
logger.addHandler(handler)

# ANSI color codes (disabled when stderr is not a terminal)
_USE_COLOR = hasattr(sys.stderr, "isatty") and sys.stderr.isatty()

PYTHON_FENCE_RE = re.compile(
    r"(?P<before>^```python\s*\n)"
    r"(?P<code>.*?)"
    r"(?P<after>^```\s*$)",
    re.MULTILINE | re.DOTALL,
)


def _color(code: str, text: str) -> str:
    """Colorize the text"""
    if _USE_COLOR:
        return f"\033[{code}m{text}\033[0m"
    return text


def _find_tool(name: str) -> str:
    """Find a tool installed in the same virtualenv as the running Python."""
    return os.path.join(os.path.dirname(sys.executable), name)


def _ruff(code: str, *, line_length: int) -> str:
    return subprocess.run(
        [
            _find_tool("ruff"),
            "format",
            f"--line-length={line_length}",
            "--config",
            "format.skip-magic-trailing-comma = false",
            "--stdin-filename",
            "block.py",
            "-",
        ],
        input=code,
        capture_output=True,
        text=True,
        check=True,
    ).stdout


def _add_trailing_commas(code: str) -> str:
    """Add trailing commas to multi-line expressions using add-trailing-comma."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".py", delete=False) as f:
        f.write(code)
        tmpfile = f.name
    try:
        subprocess.run([_find_tool("add-trailing-comma"), tmpfile], capture_output=True, check=False)
        with open(tmpfile) as f:
            return f.read()
    finally:
        os.unlink(tmpfile)


def _format_code_block(match: re.Match, *, line_length: int, path: str) -> str:
    """Format a single code block"""
    code = match.group("code")
    try:
        # 1. ruff format (may create new multi-line expressions)
        # 2. add trailing commas to all multi-line expressions
        # 3. ruff format again (respects trailing commas, ensures stable output)
        formatted = _ruff(_add_trailing_commas(_ruff(code, line_length=line_length)), line_length=line_length)
    except subprocess.CalledProcessError as exc:
        snippet = code.strip().splitlines()
        preview = "\n".join(snippet[:5])
        if len(snippet) > 5:
            preview += f"\n... ({len(snippet) - 5} more lines)"
        logger.warning(
            "%s %s\n%s\n%s %s",
            _color("33", "WARNING:"),
            _color("1", path),
            _color("2", preview),
            _color("31", "ruff stderr:"),
            exc.stderr.strip(),
        )
        return match.group(0)
    return match.group("before") + formatted + match.group("after")


def main() -> int:
    """Main entrypoint"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--line-length", type=int, default=120)
    parser.add_argument("files", nargs="*")
    args = parser.parse_args()

    ret = 0
    for path in args.files:
        with open(path) as f:
            original = f.read()
        new = PYTHON_FENCE_RE.sub(
            lambda m, path=path: _format_code_block(m, line_length=args.line_length, path=path), original
        )
        if new != original:
            with open(path, "w") as f:
                f.write(new)
            logger.debug("%s %s", _color("32", "Rewriting:"), _color("1", path))
            ret = 1
    return ret


if __name__ == "__main__":
    raise SystemExit(main())

```

### File: test\conftest.py
```py
# SPDX-FileCopyrightText: 2022-present deepset GmbH <info@deepset.ai>
#
# SPDX-License-Identifier: Apache-2.0

import asyncio
import base64
import time
from collections.abc import Generator
from pathlib import Path
from unittest.mock import Mock

import pytest

from haystack import component, tracing
from haystack.document_stores.in_memory import InMemoryDocumentStore
from haystack.testing.test_utils import set_all_seeds
from test.tracing.utils import SpyingTracer

set_all_seeds(0)


# Tracing is disable by default to avoid failures in CI
tracing.disable_tracing()


@pytest.fixture()
def in_memory_doc_store():
    store = InMemoryDocumentStore()
    yield store
    store.shutdown()


@pytest.fixture()
def waiting_component():
    @component
    class Waiter:
        @component.output_types(waited_for=int)
        def run(self, wait_for: int) -> dict[str, int]:
            time.sleep(wait_for)
            return {"waited_for": wait_for}

        @component.output_types(waited_for=int)
        async def run_async(self, wait_for: int) -> dict[str, int]:
            await asyncio.sleep(wait_for)
            return {"waited_for": wait_for}

    return Waiter


@pytest.fixture()
def mock_tokenizer():
    """
    Tokenizes the string by splitting on spaces.
    """
    tokenizer = Mock()
    tokenizer.encode = lambda text: text.split()
    tokenizer.decode = lambda tokens: " ".join(tokens)  # noqa: PLW0108
    return tokenizer


@pytest.fixture()
def test_files_path():
    return Path(__file__).parent / "test_files"


@pytest.fixture(autouse=True)
def request_blocker(request: pytest.FixtureRequest, monkeypatch):
    """
    This fixture is applied automatically to all tests.
    Those that are not marked as integration will have the requests module
    monkeypatched to avoid making HTTP requests by mistake.
    """
    marker = request.node.get_closest_marker("integration")
    if marker is not None:
        return

    def urlopen_mock(self, method, url, *args, **kwargs):
        raise RuntimeError(f"The test was about to {method} {self.scheme}://{self.host}{url}")

    monkeypatch.setattr("urllib3.connectionpool.HTTPConnectionPool.urlopen", urlopen_mock)


@pytest.fixture()
def spying_tracer() -> Generator[SpyingTracer, None, None]:
    tracer = SpyingTracer()
    tracing.enable_tracing(tracer)
    tracer.is_content_tracing_enabled = True

    yield tracer

    # Make sure to disable tracing after the test to avoid affecting other tests
    tracing.disable_tracing()


@pytest.fixture()
def base64_image_string():
    return "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+ip1sAAAAASUVORK5CYII="


@pytest.fixture()
def base64_pdf_string(test_files_path):
    with open(test_files_path / "pdf" / "sample_pdf_3.pdf", "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


@pytest.fixture
def del_hf_env_vars(monkeypatch):
    """
    Delete Hugging Face environment variables for tests.

    Prevents passing empty tokens to Hugging Face, which would cause API calls to fail.
    This is particularly relevant for PRs opened from forks, where secrets are not available
    and empty environment variables might be set instead of being removed.

    See https://github.com/deepset-ai/haystack/issues/8811 for more details.
    """
    monkeypatch.delenv("HF_API_TOKEN", raising=False)
    monkeypatch.delenv("HF_TOKEN", raising=False)

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
