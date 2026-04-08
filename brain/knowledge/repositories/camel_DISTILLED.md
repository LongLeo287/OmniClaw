---
id: repo-fetched-camel-151427-151506
type: knowledge
owner: OA
registered_at: 2026-04-05T04:04:51.271192
tags: ["auto-cloned", "oa-assimilated"]
---

# FETCHED_camel_151427_151506

## Assimilation Report
Auto-cloned repository: FETCHED_camel_151427_151506

## Application for OmniClaw
No structural integration blueprint provided.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<div align="center">
  <a href="https://www.camel-ai.org/">
    <img src="docs/images/banner.png" alt="Banner">
  </a>
</div>

</br>

<div align="center">

[![Documentation][docs-image]][docs-url]
[![Discord][discord-image]][discord-url]
[![X][x-image]][x-url]
[![Reddit][reddit-image]][reddit-url]
[![Wechat][wechat-image]][wechat-url]
[![Hugging Face][huggingface-image]][huggingface-url]
[![Star][star-image]][star-url]
[![Package License][package-license-image]][package-license-url]
[![PyPI Download][package-download-image]][package-download-url]
[![][join-us-image]][join-us]

<a href="https://trendshift.io/repositories/649" target="_blank"><img src="https://trendshift.io/api/badge/repositories/649" alt="camel-ai/camel | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

[English](README.md) |
[简体中文](README.zh.md) |
[日本語](README.ja.md)

</div>


<hr>

<div align="center">
<h4 align="center">

[Community](https://github.com/camel-ai/camel#community) |
[Installation](https://github.com/camel-ai/camel#installation) |
[Examples](https://github.com/camel-ai/camel/tree/HEAD/examples) |
[Paper](https://arxiv.org/abs/2303.17760) |
[Citation](https://github.com/camel-ai/camel#citation) |
[Contributing](https://github.com/camel-ai/camel#contributing-to-camel-) |
[CAMEL-AI](https://www.camel-ai.org/)

</h4>

<p style="line-height: 1.5; text-align: center;"> 🐫 CAMEL is an open-source community dedicated to finding the scaling laws of agents. We believe that studying these agents on a large scale offers valuable insights into their behaviors, capabilities, and potential risks. To facilitate research in this field, we implement and support various types of agents, tasks, prompts, models, and simulated environments.</p>


<br>


Join us ([*Discord*](https://discord.camel-ai.org/) or [*WeChat*](https://ghli.org/camel/wechat.png)) in pushing the boundaries of finding the scaling laws of agents.

🌟 Star CAMEL on GitHub and be instantly notified of new releases.

</div>

<div align="center">
    <img src="docs/images/stars.gif" alt="Star">
  </a>
</div>

<br>

[![][image-join-us]][join-us]

<details>
<summary><kbd>Table of contents</kbd></summary>

<br/>

- [CAMEL Framework Design Principles](#camel-framework-design-principles)
- [Why Use CAMEL for Your Research?](#why-use-camel-for-your-research)
- [What Can You Build With CAMEL?](#what-can-you-build-with-camel)
  - [Data Generation](#1-data-generation)
  - [Task Automation](#2-task-automation)
  - [World Simulation](#3-world-simulation)
- [Quick Start](#quick-start)
  - [Starting with ChatAgent](#starting-with-chatagent)
  - [Seeking Help](#seeking-help)
- [Tech Stack](#tech-stack)
- [Research](#research)
- [Synthetic Datasets](#synthetic-datasets)
- [Cookbooks (Usecases)](#cookbooks-usecases)
  - [Basic Concepts](#1-basic-concepts)
  - [Advanced Features](#2-advanced-features)
  - [Model Training & Data Generation](#3-model-training--data-generation)
  - [Multi-Agent Systems & Applications](#4-multi-agent-systems--applications)
  - [Data Processing](#5-data-processing)
- [Real-World Usecases](#real-world-usecases)
- [🧱 Built with CAMEL (Real-world Producs & Research)](#-built-with-camel-real-world-producs--research)
  - [Research Projects](#research-projects)
  - [Product Projects](#product-projects)
- [🗓️ Events](#️-events)
- [Contributing to CAMEL](#contributing-to-camel)
- [Community & Contact](#community--contact)
- [Citation](#citation)
- [Acknowledgment](#acknowledgment)
- [License](#license)

####

<br/>

</details>


## CAMEL Framework Design Principles

<h3>🧬 Evolvability</h3 >

The framework enables multi-agent systems to continuously evolve by generating data and interacting with environments. This evolution can be driven by reinforcement learning with verifiable rewards or supervised learning.

<h3>📈 Scalability</h3>

The framework is designed to support systems with millions of agents, ensuring efficient coordination, communication, and resource management at scale.

<h3>💾 Statefulness</h3>

Agents maintain stateful memory, enabling them to perform multi-step interactions with environments and efficiently tackle sophisticated tasks.

<h3>📖 Code-as-Prompt</h3>

Every line of code and comment serves as a prompt for agents. Code should be written clearly and readably, ensuring both humans and agents can interpret it effectively.

<br>

## Why Use CAMEL for Your Research?

We are a community-driven research collective comprising over 100 researchers dedicated to advancing frontier research in Multi-Agent Systems. Researchers worldwide choose CAMEL for their studies based on the following reasons.

<table style="width: 100%;">
  <tr>
    <td align="left"></td>
    <td align="left"></td>
    <td align="left"></td>
  </tr>
  <tr>
    <td align="left">✅</td>
    <td align="left" style="font-weight: bold;">Large-Scale Agent System</td>
    <td align="left">Simulate up to 1M agents to study emergent behaviors and scaling laws in complex, multi-agent environments.</td>
  </tr>
  <tr>
    <td align="left">✅</td>
    <td align="left" style="font-weight: bold;">Dynamic Communication</td>
    <td align="left">Enable real-time interactions among agents, fostering seamless collaboration for tackling intricate tasks.</td>
  </tr>
  <tr>
    <td align="left">✅</td>
    <td align="left" style="font-weight: bold;">Stateful Memory</td>
    <td align="left">Equip agents with the ability to retain and leverage historical context, improving decision-making over extended interactions.</td>
  </tr>
  <tr>
    <td align="left">✅</td>
    <td align="left" style="font-weight: bold;">Support for Multiple Benchmarks</td>
    <td align="left">Utilize standardized benchmarks to rigorously evaluate agent performance, ensuring reproducibility and reliable comparisons.</td>
  </tr>
  <tr>
    <td align="left">✅</td>
    <td align="left" style="font-weight: bold;">Support for Different Agent Types</td>
    <td align="left">Work with a variety of agent roles, tasks, models, and environments, supporting interdisciplinary experiments and diverse research applications.</td>
  </tr>
  <tr>
    <td align="left">✅</td>
    <td align="left" style="font-weight: bold;">Data Generation and Tool Integration</td>
    <td align="left">Automate the creation of large-scale, structured datasets while seamlessly integrating with multiple tools, streamlining synthetic data generation and research workflows.</td>
  </tr>
</table>

<br>

## What Can You Build With CAMEL?


### 1. Data Generation

<div align="center">
  <a href="https://github.com/camel-ai/camel/blob/master/camel/datagen/cot_datagen.py">
    <img src="docs/images/cot.png" alt="CoT Data Generation">
  </a>
</div>

<div align="center">
  <a href="https://github.com/camel-ai/camel/tree/master/camel/datagen/self_instruct">
    <img src="docs/images/self_instruct.png" alt="Self-Instruct Data Generation">
  </a>
</div>

<div align="center">
  <a href="https://github.com/camel-ai/camel/tree/master/camel/datagen/source2synth">
    <img src="docs/images/source2synth.png" alt="Source2Synth Data Generation">
  </a>
</div>

<div align="center">
  <a href="https://github.com/camel-ai/camel/blob/master/camel/datagen/self_improving_cot.py">
    <img src="docs/images/self_improving.png" alt="Self-Improving Data Generation">
  </a>
</div>

### 2. Task Automation

<div align="center">
  <a href="https://github.com/camel-ai/camel/blob/master/camel/societies/role_playing.py">
    <img src="docs/images/role_playing.png" alt="Role Playing">
  </a>
</div>

<div align="center">
  <a href="https://github.com/camel-ai/camel/tree/master/camel/societies/workforce">
    <img src="docs/images/workforce.png" alt="Workforce">
  </a>
</div>

<div align="center">
  <a href="https://docs.camel-ai.org/cookbooks/advanced_features/agents_with_rag">
    <img src="docs/images/rag_pipeline.png" alt="RAG Pipeline">
  </a>
</div>


### 3. World Simulation

<div align="center">
  <a href="https://github.com/camel-ai/oasis">
    <img src="docs/images/oasis_case.png" alt="Oasis Case">
  </a>
</div>

<br>

## Quick Start

Installing CAMEL is a breeze thanks to its availability on PyPI. Simply open your terminal and run:

```bash
pip install camel-ai
```

### Starting with ChatAgent

This example demonstrates how to create a `ChatAgent` using the CAMEL framework and perform a search query using DuckDuckGo.

1. **Install the tools package:**

  ```bash
  pip install 'camel-ai[web_tools]'
  ```

2. **Set up your OpenAI API key:**

  ```bash
  export OPENAI_API_KEY='your_openai_api_key'
  ```

   Alternatively, use a `.env` file:

   ```bash
   cp .env.example .env
   # then edit .env and add your keys
   ```

3. **Run the following Python code:**

  ```python
  from camel.models import ModelFactory
  from camel.types import ModelPlatformType, ModelType
  from camel.agents import ChatAgent
  from camel.toolkits import SearchToolkit

  model = ModelFactory.create(
    model_platform=ModelPlatformType.OPENAI,
    model_type=ModelType.GPT_4O,
    model_config_dict={"temperature": 0.0},
  )

  search_tool = SearchToolkit().search_duckduckgo

  agent = ChatAgent(model=model, tools=[search_tool])

  response_1 = agent.step("What is CAMEL-AI?")
  print(response_1.msgs[0].content)
  # CAMEL-AI is the first LLM (Large Language Model) multi-agent framework
  # and an open-source community focused on finding the scaling laws of agents.
  # ...

  response_2 = agent.step("What is the Github link to CAMEL framework?")
  print(response_2.msgs[0].content)
  # The GitHub link to the CAMEL framework is
  # [https://github.com/camel-ai/camel](https://github.com/camel-ai/camel).
  ```

4. **(Optional) Enable model request/response logs:**

  ```bash
  export CAMEL_MODEL_LOG_ENABLED=true
  export CAMEL_MODEL_LOG_MODEL_CONFIG_ENABLED=true
  export CAMEL_LOG_DIR=camel_logs
  ```

  - `CAMEL_MODEL_LOG_ENABLED`: Enables request/response JSON logs.
  - `CAMEL_MODEL_LOG_MODEL_CONFIG_ENABLED`: Controls whether
    `model_config_dict` is logged under `request.model_config_dict`.
    When unset, it defaults to the same value as
    `CAMEL_MODEL_LOG_ENABLED`.
  - `CAMEL_LOG_DIR`: Directory for generated log files
    (default: `camel_logs`).
  - Logs are written as UTF-8 JSON with multilingual text preserved
    (for example Chinese, Japanese, Arabic) without Unicode escape noise.


For more detailed instructions and additional configuration options, check out the [installation section](https://github.com/camel-ai/camel/blob/master/docs/get_started/installation.md).

After running, you can explore our CAMEL Tech Stack and Cookbooks at [docs.camel-ai.org](https://docs.camel-ai.org) to build powerful multi-agent systems.

We provide a [![Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1AzP33O8rnMW__7ocWJhVBXjKziJXPtim?usp=sharing) demo showcasing a conversation between two ChatGPT agents playing roles as a python programmer and a stock trader collaborating on developing a trading bot for stock market.

Explore different types of agents, their roles, and their applications.

- **[Creating Your First Agent](https://docs.camel-ai.org/cookbooks/basic_concepts/create_your_first_agent)**
- **[Creating Your First Agent Society](https://docs.camel-ai.org/cookbooks/basic_concepts/create_your_first_agents_society)**
- **[Embodied Agents](https://docs.camel-ai.org/cookbooks/advanced_features/embodied_agents)**
- **[Critic Agents](https://docs.camel-ai.org/cookbooks/advanced_features/critic_agents_and_tree_search)**

### Seeking Help

Please reach out to us on [CAMEL discord](https://discord.camel-ai.org/) if you encounter any issue set up CAMEL.

<br>

## Tech Stack

<div align="center">
  <a href="https://docs.camel-ai.org">
    <img src="https://camel-ai.github.io/camel_asset/graphics/techstack.png" alt="TechStack">
  </a>
</div>

### Key Modules
Core components and utilities to build, operate, and enhance CAMEL-AI agents and societies.

| Module | Description |
|:---|:---|
| **[Agents](https://docs.camel-ai.org/key_modules/agents)** | Core agent architectures and behaviors for autonomous operation. |
| **[Agent Societies](https://docs.camel-ai.org/key_modules/society)** | Components for building and managing multi-agent systems and collaboration. |
| **[Data Generation](https://docs.camel-ai.org/key_modules/datagen)** | Tools and methods for synthetic data creation and augmentation. |
| **[Models](https://docs.camel-ai.org/key_modules/models)** | Model architectures and customization options for agent intelligence. |
| **[Tools](https://docs.camel-ai.org/key_modules/tools)** | Tools integration for specialized agent tasks. |
| **[Memory](https://docs.camel-ai.org/key_modules/memory)** | Memory storage and retrieval mechanisms for agent state management. |
| **[Storage](https://docs.camel-ai.org/key_modules/storages)** | Persistent storage solutions for agent data and states. |
| **[Benchmarks](https://github.com/camel-ai/camel/tree/master/camel/benchmarks)** | Performance evaluation and testing frameworks. |
| **[Interpreters](https://docs.camel-ai.org/key_modules/interpreters)** | Code and command interpretation capabilities. |
| **[Data Loaders](https://docs.camel-ai.org/key_modules/loaders)** | Data ingestion and preprocessing tools. |
| **[Retrievers](https://docs.camel-ai.org/key_modules/retrievers)** | Knowledge retrieval and RAG components. |
| **[Runtime](https://github.com/camel-ai/camel/tree/master/camel/runtime)** | Execution environment and process management. |
| **[Human-in-the-Loop](https://docs.camel-ai.org/cookbooks/advanced_features/agents_with_human_in_loop_and_tool_approval)** | Interactive components for human oversight and intervention. |
---

## Research

We believe that studying these agents on a large scale offers valuable insights into their behaviors, capabilities, and potential risks.

**Explore our research projects:**

<div align="center">
  <a href="https://github.com/camel-ai/owl">
    <img src="docs/images/owl.png" alt="OWL">
  </a>
</div>

<div align="center">
  <a href="https://oasis.camel-ai.org/">
    <img src="docs/images/oasis.png" alt="OASIS">
  </a>
</div>

<div align="center">
  <a href="https://crab.camel-ai.org/">
    <img src="docs/images/crab.png" alt="CRAB">
  </a>
</div>

<div align="center">
  <a href="https://github.com/camel-ai/loong">
    <img src="docs/images/loong.png" alt="Loong">
  </a>
</div>

<div align="center">
  <a href="https://agent-trust.camel-ai.org/">
    <img src="docs/images/agent_trust.png" alt="Agent Trust">
  </a>
</div>

<div align="center">
  <a href="https://emos-project.github.io/">
    <img src="docs/images/emos.png" alt="Emos">
  </a>
</div>

>### Research with US
>
>We warmly invite you to use CAMEL for your impactful research.
>
> Rigorous research takes time and resources. We are a community-driven research collective with 100+ researchers exploring the frontier research of M
... [TRUNCATED]
```

### File: .container\README.md
```md
# Install CAMEL with Docker

Docker offers an easy way to create a consistent and isolated virtual
environment, containers, for setting up the dependencies of CAMEL. This guide
will show you how to quickly set up CAMEL, run the examples, and also
develop on it, with Docker.

## Prerequisites
- Docker：https://docs.docker.com/engine/install/
- Docker Compose：https://docs.docker.com/compose/install/

## Configure Environment
Before starting the container, you need to navigate into the
[.container](../.container) folder and create a `.env` file **with your own
API
keys**, so that these keys will be present in the environment variables of
the container, which will later be used by CAMEL. The list of API keys that
can be found in the `.env.example` file.

```bash
cd .container

# YOU SHOULD EDIT .env FILE TO ADD YOUR OWN API KEYS AFTER THIS
cp .env.example .env
```

## Start Container
After configuring the API keys, simply run the following command to start
up the working container. This will automatically set up the environment and
dependencies for CAMEL. It may take some time, please be patient.

```bash
docker compose up -d
```

After the build is completed, you can see the image `camel:localdev` in the
list of images, along with a started container, `camel-localdev`.

```bash
# check the list of images
docker images

# check the list of running containers
docker ps
```

## Enter Container
You can enter the container with the following command.

```bash
docker compose exec camel bash
```

Then you will be in the container environment under the CAMEL directory, with
all the dependencies installed.

Then You can try running the
[role_playing.py](../examples/ai_society/role_playing.py)
example.

```bash
python examples/ai_society/role_playing.py
```

If you see the agents interacting with each other, this means you are all set.
Have fun with CAMEL in Docker!

## Save Your Progress
We support volume mounting in the started container, which means that all
of your changes in the CAMEL directory inside the container will be synced
into the CAMEL repo on your host system. Therefore, you don't need to worry
about losing your progress when you exit the container.

## Exit, Stop and Delete the Container
You can simply press `Ctrl + D` or use the `exit` command to exit the
container.

After exiting the container, under normal cases the container will still be
running in the background. If you don't need the container anymore, you can
stop and delete the container with the following command.

```bash
docker compose down
```

## Online Images
For users who only want to have a quick tryout on CAMEL, we also provide the
pre-built images on
[our GitHub Container Registry](https://github.com/camel-ai/camel/pkgs/container/camel).
Considering the size of the image, we only offer the image with the basic
dependencies.

Note that there are some key differences between the local development
image and the pre-built image that you should be aware of.
1. The pre-built image is built upon the source code of each release of CAMEL.
   This means that they are not suitable for development, as they don't
   contain the git support. If you want to develop on CAMEL, please build
   the image by yourself according to the instructions above.
2. The pre-built image only contains the basic dependencies for running the
   examples. If you want to run the examples that require additional
   dependencies, you need to install them according to the
   installation guide in CAMEL's [README](../README.md).
3. The pre-built image doesn't contain the API keys. You need to set up the
   API keys by yourself in the container environment.
4. The pre-built image does not support volume mounting. This means that all
   of your changes in the container will be lost when you delete the container.

To quickly start a container with the pre-built image, you can use the
following command.

```bash
docker run -it -d --name camel ghcr.io/camel-ai/camel:latest
```

Attach to the container with the following command.

```bash
docker exec -it camel bash
```

After setting the environment, you can run the example with the following
command.

```bash
python examples/ai_society/role_playing.py
```

```

### File: docs\README.md
```md
# How to update the documentation

To update the RST files:
```bash
sphinx-apidoc -o docs camel/
```

Helpful article [here](https://towardsdatascience.com/documenting-python-code-with-sphinx-554e1d6c4f6d).

# Building Documentation

To build the documentation:

1. [Install CAMEL](https://github.com/camel-ai/camel/blob/master/README.md) from source.

2. Install required dependencies running the following command in your terminal or command prompt:
```bash
pip install sphinx
pip install sphinx_book_theme
pip install sphinx-autobuild
pip install myst_parser
pip install nbsphinx
```

3. Build the document and launch the HTML documentation.
```bash
cd docs
sphinx-autobuild . _build/html --port 8000
```

This command starts a local HTTP server on port 8080 by default. Once the server is running, open your web browser and enter the following URL:
```bash
127.0.0.1:8000
```
This will load the HTML documentation in your web browser from the local server. The server will watch for changes in your source files and automatically rebuild the documentation and refresh the page in the browser when you make changes – so changes in docs will be immediately reflected in the rendered doc.

You can navigate through the documentation using the links and interact with it as you would with any other web page.

To stop the local server, go back to the terminal or command prompt where it is running and press `Ctrl+C` to terminate the server.

In case the autobuild does not work, you may use the traditional build approach:
```bash
cd docs
make html
cd _build/html
python -m http.server
```

```

### File: CONTRIBUTING.md
```md
🐫 **Welcome to CAMEL!** 🐫

Thank you for your interest in contributing to the CAMEL project! 🎉 We're excited to have your support. As an open-source initiative in a rapidly evolving and open-ended field, we wholeheartedly welcome contributions of all kinds. Whether you want to introduce new features, enhance the infrastructure, improve documentation, asking issues, add more examples, implement state-of-the-art research ideas, or fix bugs, we appreciate your enthusiasm and efforts. 🙌  You are welcome to join our [discord](https://discord.camel-ai.org/) for more efficient communication. 💬

---

## AI-Generated Code Policy

CAMEL is a multi-agent framework designed to deliver high-quality open source solutions. We welcome developers who genuinely use CAMEL to solve real-world problems to engage with us and build together.

**Our goals are:**

1. Pursue quality over quantity — in both code and feature design within the CAMEL repository.
2. Welcome any developer or user who truly uses CAMEL, or shares our mission and vision, to discuss product and technology with us.

### Why This Policy Exists

As AI coding capabilities grow, an increasing number of AI coding bots or vibe-coded submissions are introducing significant noise and risk to open-source repositories:

1. **Code quality risks.** AI-generated code may contain subtle bugs or hallucinations. An excessive volume of unreviewed LLM-generated code dramatically increases maintenance costs.
2. **Community culture.** For CAMEL's community, we uphold the core value of human collaboration and oppose low-effort, low-signal spamming.

### Contribution Requirements

We are taking the following precautionary steps to maintain the integrity of this open-source repository:

1. **PRs must reference a prior discussion.** Every PR must link to a previously discussed and accepted issue, Discord thread, or equivalent. Drive-by PRs with no associated accepted issue will be closed.
2. **No unreviewed LLM-generated submissions.** We will close PRs that are primarily generated by LLMs or chatbots and submitted without meaningful human review, especially "vibe-coded" submissions.
3. **Human-verified testing is required.** Do not submit code that is "theoretically correct but untested." Every PR must include proof of testing (e.g., screenshots, screen recordings, test output logs).
4. **AI-assisted drafts are acceptable for issues, discussions, and prototypes**, but they must be reviewed and edited by a human to reduce verbosity and noise.

### Enforcement: Grounds for Immediate Ban

The following abusive behaviors will result in an immediate ban (PR submission privileges revoked):

1. **Inauthentic contribution activity.** Using AI tools to artificially inflate open-source contribution metrics for personal or commercial gain.
2. **Bulk, low-quality, irrelevant, or misleading AI-generated content.**

---

## Join Our Community 🌍

### Schedule an Introduction Call 📞
- English speakers: [here](https://cal.com/wendong-fan-5yu7x5/30min)
- Chinese speakers: [here](https://cal.com/wendong-fan-5yu7x5/30min)

### Developer Meeting Time & Link 💻
- English speakers: Mondays at 5 PM GMT+1. Join via Discord: [Meeting Link](https://discord.gg/FFe4nB8MJj?event=1313319275708289034)
- Chinese Speakers: Mondays at 9 PM UTC+8. Join via TecentMeeting: [Meeting Link](https://meeting.tencent.com/dm/057wap1eeCSY)

### Our Communication Channels 💬
- **Discord:** [Join here](https://discord.camel-ai.org/)
- **WeChat:** Scan the QR code [here](https://ghli.org/camel/wechat.png)
- **Slack:** [Join here](https://join.slack.com/t/camel-ai/shared_invite/zt-2g7xc41gy-_7rcrNNAArIP6sLQqldkqQ)

## Guidelines 📝

### Contributing to the Code 👨‍💻👩‍💻

If you're eager to contribute to this project, that's fantastic! We're thrilled to have your support.

- If you are a contributor from the community:
  - Follow the [Fork-and-Pull-Request](https://docs.github.com/en/get-started/quickstart/contributing-to-projects) workflow when opening your pull requests.
- If you are a member of [CAMEL-AI.org](https://github.com/camel-ai):
  - Follow the [Checkout-and-Pull-Request](https://dev.to/ceceliacreates/how-to-create-a-pull-request-on-github-16h1) workflow when opening your pull request; this will allow the PR to pass all tests that require [GitHub Secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets).

Make sure to mention any related issues and tag the relevant maintainers too. 💪

Before your pull request can be merged, it must pass the formatting, linting, and testing checks. You can find instructions on running these checks locally under the **Common Actions** section below. 🔍

Ensuring excellent documentation and thorough testing is absolutely crucial. Here are some guidelines to follow based on the type of contribution you're making:

- If you fix a bug:
  - Add a relevant unit test when possible. These can be found in the `test` directory.
- If you make an improvement:
  - Update any affected example console scripts in the `examples` directory, Gradio demos in the `apps` directory, and documentation in the `docs` directory.
  - Update unit tests when relevant.
- If you add a feature:
  - Include unit tests in the `test` directory.
  - Add a demo script in the `examples` directory.

We're a small team focused on building great things. If you have something in mind that you'd like to add or modify, opening a pull request is the ideal way to catch our attention. 🚀

### Contributing to the Cookbook Writing 📚

We are excited that you want to contribute to our cookbook! The CAMEL cookbook is an essential resource for users, and we want to make sure that it remains high-quality, accurate, and helpful.

We use Google Colab as the primary platform for writing and reviewing our cookbooks, and we have a specific [template](https://colab.research.google.com/drive/17SiWWjoK7l8Sy9FBsGKUHC6zuEsLt2yX?usp=sharing) that contributors should follow to maintain consistency. Please feel free to share any suggestions for improvements or additions to the template.

Here’s how you can contribute to writing cookbooks:

#### 1. Writing the Cookbook

- Template Usage: We have a [template](https://colab.research.google.com/drive/17SiWWjoK7l8Sy9FBsGKUHC6zuEsLt2yX?usp=sharing) for cookbook entries. Always use this template to ensure uniformity in style and structure.
- Start in Colab: Begin writing your cookbook in Google Colab. Colab allows us to run interactive code and include explanations side-by-side, which is ideal for a practical, hands-on cookbook.
- Correctness: Ensure that the **LLM-generated responses are correct**. Each recipe in the cookbook should be verified with real code execution, and the results must be accurate.
- Clear and Concise Explanations: Provide clear explanations of the code, its purpose, and how it works. Make sure any complex logic or steps are well documented and explained in simple terms. Avoid installing all optional extras unless they are needed.
- Interactive Elements: Whenever applicable, add interactive code cells in Colab that users can directly run and modify.

##### 1.2. Developing cookbooks for in-progress features
You can install the latest version of CAMEL from the main branch or a topic branch. This allows you to use the latest codebase, or in-progress features in your cookbook.

`!pip install "git+https://github.com/camel-ai/camel.git@master#egg=camel-ai[all]"`

Changing the branch and extras section (e.g. remove `#egg=camel-ai[all]`) will behave as expected.

Remember to change to a release version before sharing the cookbook with the community for long-term stability. Also note that a topic branch will stop working if the branch is deleted.

#### 2. Reviewing the Cookbook
Once the initial draft of the cookbook is ready:

- Review in Colab: The review process for cookbooks is done in Colab. We will leave comments and suggestions directly in the Colab document. Reviewers will focus on:
 - Accuracy: Ensure that the code is correct, performs the expected tasks, and generates the intended results.
 - Clarity: Check that the explanations are clear, detailed, and easy to understand.
 - Structure: Ensure that the flow of the cookbook is logical and easy to follow, with a step-by-step approach.
 - Formatting: Verify that the formatting follows the template guidelines (e.g., headers, code blocks, comments).
 - Feedback Process: If there are issues or suggestions for improvement, the reviewer will leave comments directly in the Colab notebook. The contributor should address these comments and update the Colab file accordingly.

#### 3. Submitting the Cookbook
When the Colab cookbook is ready for integration:

- Download the Cookbook: Once the Colab notebook is finalized and reviewed, download the notebook as a .ipynb file and convert your cookbook from .ipynb to .mdx and add your cookbook file to the appropriate directory under `docs/cookbooks/`.
- Create a Pull Request: Open a pull request to add the cookbook to the docs folder of the repository. This pull request will include the mdx file and also include any necessary documentation or references to integrate the cookbook into the main docs.

#### 4. Principles to Follow
To ensure that the cookbook meets the highest standards, please keep the following principles in mind:

- High Quality: Every cookbook entry must be of high quality. This includes accurate code, well-written explanations, and comprehensive tests (if applicable).
- LLM-Generated Responses: If you use a large language model (LLM) to generate part of the cookbook content, ensure that the responses are correct and validated with real-world examples. Do not include any code that is incorrect or doesn't work as expected.
- Reproducibility: Ensure that all code in the cookbook is reproducible. Any user following the steps should be able to get the same results by running the code on their own machine.
- Accessibility: Make sure the content is accessible to a wide range of users, from beginners to advanced users. Provide context where necessary and define technical terms.

By following these guidelines, you'll help us maintain a high-quality, helpful, and engaging cookbook for the CAMEL community. Thank you for contributing to this valuable resource! 🌟

### Contributing to Code Reviews 🔍
This part outlines the guidelines and best practices for conducting code reviews in CAMEL. The aim is to ensure that all contributions are of high quality, align with the project's goals, and are consistent with our coding standards.

#### Purpose of Code Reviews
- Maintain Code Quality: Ensure that the codebase remains clean, readable, and maintainable.
- Knowledge Sharing: Facilitate knowledge sharing among contributors and help new contributors learn best practices.
- Bug Prevention: Catch potential bugs and issues before they are merged into the main branch.
- Consistency: Ensure consistency in style, design patterns, and architecture across the project.

#### Review Process Overview
- Reviewers should check the code for functionality, readability, consistency, and compliance with the project’s coding standards.
- If changes are necessary, the reviewer should leave constructive feedback.
- The contributor addresses feedback and updates the PR.
- The reviewer re-reviews the updated code.
- Once the code is approved by at least two reviewer, it can be merged into the main branch.
- Merging should be done by a maintainer or an authorized contributor.

#### Code Review Checklist
- Functionality
  - Correctness: Does the code perform the intended task? Are edge cases handled?
  - Testing: Is there sufficient test coverage? Do all tests pass?
  - Security: Are there any security vulnerabilities introduced by the change?
  - Performance: Does the code introduce any performance regressions?

- Code Quality
  - Readability: Is the code easy to read and understand? Is it well-commented where necessary?
  - Maintainability: Is the code structured in a way that makes future changes easy?
  - Style: Does the code follow the project’s style guidelines?
  Currently we use Ruff for format check and take [Google Python Style Guide]("https://google.github.io/styleguide/pyguide.html") as reference.
  - Documentation: Are public methods, classes, and any complex logic well-documented?
- Design
  - Consistency: Does the code follow established design patterns and project architecture?
  - Modularity: Are the changes modular and self-contained? Does the code avoid unnecessary duplication?
  - Dependencies: Are dependencies minimized and used appropriately?

#### Reviewer Responsibilities
- Timely Reviews: Reviewers should strive to review PRs promptly to keep the project moving.
- Constructive Feedback: Provide feedback that is clear, constructive, and aimed at helping the contributor improve.
- Collaboration: Work with the contributor to address any issues and ensure the final code meets the project’s standards.
- Approvals: Only approve code that you are confident meets all the necessary criteria.

#### Common Pitfalls
- Large PRs: Avoid submitting PRs that are too large. Break down your changes into smaller, manageable PRs if possible.
- Ignoring Feedback: Address all feedback provided by reviewers, even if you don’t agree with it—discuss it instead of ignoring it.
- Rushed Reviews: Avoid rushing through reviews. Taking the time to thoroughly review code is critical to maintaining quality.

Code reviews are an essential part of maintaining the quality and integrity of our open source project. By following these guidelines, we can ensure that CAMEL remains robust, secure, and easy to maintain, while also fostering a collaborative and welcoming community.

### Guideline for Writing Docstrings

This guideline will help you write clear, concise, and structured docstrings for contributing to `CAMEL`.

#### 1. Use the Triple-Quoted String with `r"""` (Raw String)
Begin the docstring with `r"""` to indicate a raw docstring. This prevents any issues with special characters and ensures consistent formatting.

#### 2. Provide a Brief Class or Method Description
- Start with a concise summary of the purpose and functionality.
- Keep each line under `79` characters.
- The summary should start on the first line without a linebreak.

Example:
```python
r"""Class for managing conversations of CAMEL Chat Agents.
"""
```

#### 3. Document Parameters in the Args Section
- Use an `Args`: section for documenting constructor or function parameters.
- Maintain the `79`-character limit for each line, and indent continuation lines by 4 spaces.
- Follow this structure:
  - Parameter Name: Match the function signature.
  - Type: Include the type (e.g., `int`, `str`, custom types like `BaseModelBackend`).
  - Description: Provide a brief explanation of the parameter's role.
  - Default Value: Use (`default: :obj:<default_value>`) to indicate default values.

Example:
```markdown
Args:
    system_message (BaseMessage): The system message for 
... [TRUNCATED]
```

### File: README.ja.md
```md
<div align="center">
  <a href="https://www.camel-ai.org/">
    <img src="docs/images/banner.png" alt="Banner">
  </a>
</div>

</br>

<div align="center">

[![Documentation][docs-image]][docs-url]
[![Discord][discord-image]][discord-url]
[![X][x-image]][x-url]
[![Reddit][reddit-image]][reddit-url]
[![Wechat][wechat-image]][wechat-url]
[![Hugging Face][huggingface-image]][huggingface-url]
[![Star][star-image]][star-url]
[![Package License][package-license-image]][package-license-url]
[![PyPI Download][package-download-image]][package-download-url]
[![][join-us-image]][join-us]

<a href="https://trendshift.io/repositories/649" target="_blank"><img src="https://trendshift.io/api/badge/repositories/649" alt="camel-ai/camel | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

[English](README.md) |
[简体中文](README.zh.md) |
[日本語](README.ja.md)

</div>


<hr>

<div align="center">
<h4 align="center">

[Community](https://github.com/camel-ai/camel#community) |
[Installation](https://github.com/camel-ai/camel#installation) |
[Examples](https://github.com/camel-ai/camel/tree/HEAD/examples) |
[Paper](https://arxiv.org/abs/2303.17760) |
[Citation](https://github.com/camel-ai/camel#citation) |
[Contributing](https://github.com/camel-ai/camel#contributing-to-camel-) |
[CAMEL-AI](https://www.camel-ai.org/)

</h4>

<p style="line-height: 1.5; text-align: center;"> 🐫 CAMELは、エージェントのスケーリング法則を発見することに専念するオープンソースコミュニティです。エージェントを大規模に研究することで、その行動、能力、潜在的なリスクについて貴重な洞察が得られると信じています。この分野の研究を促進するため、様々なタイプのエージェント、タスク、プロンプト、モデル、シミュレーション環境を実装・サポートしています。</p>


<br>


エージェントのスケーリング法則を見つけるために、私たち（[*Discord*](https://discord.camel-ai.org/) または [*WeChat*](https://ghli.org/camel/wechat.png)）と共に境界を押し広げましょう。

🌟 GitHubでCAMELにスターを付けると、新しいリリースの通知が即座に受け取れます。

</div>

<div align="center">
    <img src="docs/images/stars.gif" alt="Star">
  </a>
</div>

<br>

[![][image-join-us]][join-us]

<details>
<summary><kbd>目次</kbd></summary>

<br/>

- [CAMELフレームワーク設計原則](#camelフレームワーク設計原則)
- [なぜ研究にCAMELを使うのか？](#なぜ研究にcamelを使うのか)
- [CAMELで何が構築できるか？](#camelで何が構築できるか)
  - [データ生成](#1-データ生成)
  - [タスク自動化](#2-タスク自動化)
  - [世界シミュレーション](#3-世界シミュレーション)
- [クイックスタート](#クイックスタート)
  - [ChatAgentから始める](#chatagentから始める)
  - [ヘルプを求める](#ヘルプを求める)
- [技術スタック](#技術スタック)
- [研究](#研究)
- [合成データセット](#合成データセット)
- [クックブック（ユースケース）](#クックブックユースケース)
  - [基本コンセプト](#1-基本コンセプト)
  - [高度な機能](#2-高度な機能)
  - [モデルトレーニング & データ生成](#3-モデルトレーニング--データ生成)
  - [マルチエージェントシステム & アプリケーション](#4-マルチエージェントシステム--アプリケーション)
  - [データ処理](#5-データ処理)
- [実世界のユースケース](#実世界のユースケース)
- [🧱 CAMELで構築（実世界の製品 & 研究）](#-camelで構築実世界の製品--研究)
  - [研究プロジェクト](#研究プロジェクト)
  - [製品プロジェクト](#製品プロジェクト)
- [🗓️ イベント](#️-イベント)
- [CAMELへの貢献](#camelへの貢献)
- [コミュニティ & コンタクト](#コミュニティ--コンタクト)
- [引用](#引用)
- [謝辞](#謝辞)
- [ライセンス](#ライセンス)

####

<br/>

</details>


## CAMELフレームワーク設計原則

<h3>🧬 進化可能性</h3 >

フレームワークは、データを生成し環境と相互作用することで、マルチエージェントシステムが継続的に進化することを可能にします。この進化は、検証可能な報酬による強化学習または教師あり学習によって駆動されます。

<h3>📈 スケーラビリティ</h3>

フレームワークは、数百万のエージェントを持つシステムをサポートするよう設計されており、大規模な協調、通信、リソース管理を効率的に行います。

<h3>💾 ステートフルネス</h3>

エージェントはステートフルメモリを維持し、環境との多段階の相互作用を実行し、洗練されたタスクを効率的に処理することを可能にします。

<h3>📖 コード・アズ・プロンプト</h3>

すべてのコード行とコメントは、エージェントへのプロンプトとして機能します。コードは明確で読みやすく書かれるべきで、人間とエージェントの両方が効果的に解釈できるようにする必要があります。

<br>

## なぜ研究にCAMELを使うのか？

私たちは、マルチエージェントシステムの最前線研究を進める100人以上の研究者で構成される、コミュニティ主導の研究集団です。世界中の研究者が以下の理由でCAMELを研究に選択しています。

<table style="width: 100%;">
  <tr>
    <td align="left"></td>
    <td align="left"></td>
    <td align="left"></td>
  </tr>
  <tr>
    <td align="left">✅</td>
    <td align="left" style="font-weight: bold;">大規模エージェントシステム</td>
    <td align="left">複雑なマルチエージェント環境での創発的行動とスケーリング法則を研究するために、最大100万のエージェントをシミュレートします。</td>
  </tr>
  <tr>
    <td align="left">✅</td>
    <td align="left" style="font-weight: bold;">動的通信</td>
    <td align="left">エージェント間のリアルタイム相互作用を可能にし、複雑なタスクに取り組むためのシームレスな協力を促進します。</td>
  </tr>
  <tr>
    <td align="left">✅</td>
    <td align="left" style="font-weight: bold;">ステートフルメモリ</td>
    <td align="left">エージェントに履歴コンテキストを保持して活用する能力を装備し、長期間の相互作用における意思決定を改善します。</td>
  </tr>
  <tr>
    <td align="left">✅</td>
    <td align="left" style="font-weight: bold;">複数のベンチマークのサポート</td>
    <td align="left">標準化されたベンチマークを利用してエージェントのパフォーマンスを厳格に評価し、再現性と信頼性の高い比較を保証します。</td>
  </tr>
  <tr>
    <td align="left">✅</td>
    <td align="left" style="font-weight: bold;">異なるエージェントタイプのサポート</td>
    <td align="left">様々なエージェントの役割、タスク、モデル、環境を扱い、学際的な実験と多様な研究応用をサポートします。</td>
  </tr>
  <tr>
    <td align="left">✅</td>
    <td align="left" style="font-weight: bold;">データ生成とツール統合</td>
    <td align="left">大規模で構造化されたデータセットの作成を自動化し、複数のツールとシームレスに統合することで、合成データ生成と研究ワークフローを効率化します。</td>
  </tr>
</table>

<br>

## CAMELで何が構築できるか？


### 1. データ生成

<div align="center">
  <a href="https://github.com/camel-ai/camel/blob/master/camel/datagen/cot_datagen.py">
    <img src="docs/images/cot.png" alt="CoTデータ生成">
  </a>
</div>

<div align="center">
  <a href="https://github.com/camel-ai/camel/tree/master/camel/datagen/self_instruct">
    <img src="docs/images/self_instruct.png" alt="Self-Instructデータ生成">
  </a>
</div>

<div align="center">
  <a href="https://github.com/camel-ai/camel/tree/master/camel/datagen/source2synth">
    <img src="docs/images/source2synth.png" alt="Source2Synthデータ生成">
  </a>
</div>

<div align="center">
  <a href="https://github.com/camel-ai/camel/blob/master/camel/datagen/self_improving_cot.py">
    <img src="docs/images/self_improving.png" alt="Self-Improvingデータ生成">
  </a>
</div>

### 2. タスク自動化

<div align="center">
  <a href="https://github.com/camel-ai/camel/blob/master/camel/societies/role_playing.py">
    <img src="docs/images/role_playing.png" alt="ロールプレイング">
  </a>
</div>

<div align="center">
  <a href="https://github.com/camel-ai/camel/tree/master/camel/societies/workforce">
    <img src="docs/images/workforce.png" alt="ワークフォース">
  </a>
</div>

<div align="center">
  <a href="https://docs.camel-ai.org/cookbooks/advanced_features/agents_with_rag">
    <img src="docs/images/rag_pipeline.png" alt="RAGパイプライン">
  </a>
</div>


### 3. 世界シミュレーション

<div align="center">
  <a href="https://github.com/camel-ai/oasis">
    <img src="docs/images/oasis_case.png" alt="Oasisケース">
  </a>
</div>

<br>

## クイックスタート

CAMELのインストールは、PyPIで利用可能なため非常に簡単です。ターミナルを開いて以下を実行するだけです：

```bash
pip install camel-ai
```

### ChatAgentから始める

この例では、CAMELフレームワークを使用して`ChatAgent`を作成し、DuckDuckGoを使用して検索クエリを実行する方法を示します。

1. **ツールパッケージをインストール：**

  ```bash
  pip install 'camel-ai[web_tools]'
  ```

2. **OpenAI APIキーを設定：**

  ```bash
  export OPENAI_API_KEY='your_openai_api_key'
  ```

   または、`.env`ファイルを使用：

   ```bash
   cp .env.example .env
   # .envファイルを編集してキーを追加
   ```

3. **以下のPythonコードを実行：**

  ```python
  from camel.models import ModelFactory
  from camel.types import ModelPlatformType, ModelType
  from camel.agents import ChatAgent
  from camel.toolkits import SearchToolkit

  model = ModelFactory.create(
    model_platform=ModelPlatformType.OPENAI,
    model_type=ModelType.GPT_4O,
    model_config_dict={"temperature": 0.0},
  )

  search_tool = SearchToolkit().search_duckduckgo

  agent = ChatAgent(model=model, tools=[search_tool])

  response_1 = agent.step("CAMEL-AIとは何ですか？")
  print(response_1.msgs[0].content)
  # CAMEL-AIは最初のLLM（大規模言語モデル）マルチエージェントフレームワークであり、
  # エージェントのスケーリング法則を発見することに焦点を当てたオープンソースコミュニティです。
  # ...

  response_2 = agent.step("CAMELフレームワークのGitHubリンクは何ですか？")
  print(response_2.msgs[0].content)
  # CAMELフレームワークのGitHubリンクは
  # [https://github.com/camel-ai/camel](https://github.com/camel-ai/camel)です。
  ```

4. **（任意）モデルのリクエスト/レスポンスログを有効化：**

  ```bash
  export CAMEL_MODEL_LOG_ENABLED=true
  export CAMEL_MODEL_LOG_MODEL_CONFIG_ENABLED=true
  export CAMEL_LOG_DIR=camel_logs
  ```

  - `CAMEL_MODEL_LOG_ENABLED`: リクエスト/レスポンスの
    JSONログを有効化します。
  - `CAMEL_MODEL_LOG_MODEL_CONFIG_ENABLED`: `request.model_config_dict`
    を記録するかを制御します。未設定の場合は
    `CAMEL_MODEL_LOG_ENABLED` と同じ値が使われます。
  - `CAMEL_LOG_DIR`: ログの出力先ディレクトリ
    （デフォルト: `camel_logs`）。
  - ログはUTF-8 JSONで保存されるため、中国語・日本語・アラビア語
    などの多言語テキストも可読なまま保持されます。


より詳細な手順と追加の設定オプションについては、[インストールセクション](https://github.com/camel-ai/camel/blob/master/docs/get_started/installation.md)をご確認ください。

実行後、[docs.camel-ai.org](https://docs.camel-ai.org)でCAMEL技術スタックとクックブックを探索し、強力なマルチエージェントシステムを構築できます。

私たちは、Pythonプログラマーとストックトレーダーとしてロールプレイする2つのChatGPTエージェント間の会話を示す[![Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1AzP33O8rnMW__7ocWJhVBXjKziJXPtim?usp=sharing)デモを提供しています。株式市場用の取引ボットの開発に協力しています。

さまざまなタイプのエージェント、その役割、およびそれらのアプリケーションを探索してください。

- **[初めてのエージェントを作成](https://docs.camel-ai.org/cookbooks/basic_concepts/create_your_first_agent)**
- **[初めてのエージェント社会を作成](https://docs.camel-ai.org/cookbooks/basic_concepts/create_your_first_agents_society)**
- **[具現化されたエージェント](https://docs.camel-ai.org/cookbooks/advanced_features/embodied_agents)**
- **[批評エージェント](https://docs.camel-ai.org/cookbooks/advanced_features/critic_agents_and_tree_search)**

### ヘルプを求める

CAMELのセットアップで問題が発生した場合は、[CAMEL discord](https://discord.camel-ai.org/)でお気軽にお問い合わせください。

<br>

## 技術スタック

<div align="center">
  <a href="https://docs.camel-ai.org">
    <img src="https://camel-ai.github.io/camel_asset/graphics/techstack.png" alt="TechStack">
  </a>
</div>

### キーモジュール
CAMEL-AIエージェントと社会を構築、運用、強化するためのコアコンポーネントとユーティリティ。

| モジュール | 説明 |
|:---|:---|
| **[エージェント](https://docs.camel-ai.org/key_modules/agents)** | 自律運用のためのコアエージェントアーキテクチャと動作。 |
| **[エージェント社会](https://docs.camel-ai.org/key_modules/society)** | マルチエージェントシステムと協力の構築と管理のためのコンポーネント。 |
| **[データ生成](https://docs.camel-ai.org/key_modules/datagen)** | 合成データの作成と拡張のためのツールと方法。 |
| **[モデル](https://docs.camel-ai.org/key_modules/models)** | エージェントインテリジェンスのためのモデルアーキテクチャとカスタマイズオプション。 |
| **[ツール](https://docs.camel-ai.org/key_modules/tools)** | 専門的なエージェントタスクのためのツール統合。 |
| **[メモリ](https://docs.camel-ai.org/key_modules/memory)** | エージェント状態管理のためのメモリストレージと検索メカニズム。 |
| **[ストレージ](https://docs.camel-ai.org/key_modules/storages)** | エージェントデータと状態のための永続的なストレージソリューション。 |
| **[ベンチマーク](https://github.com/camel-ai/camel/tree/master/camel/benchmarks)** | パフォーマンス評価とテストフレームワーク。 |
| **[インタープリタ](https://docs.camel-ai.org/key_modules/interpreters)** | コードとコマンドの解釈機能。 |
| **[データローダー](https://docs.camel-ai.org/key_modules/loaders)** | データ取り込みと前処理ツール。 |
| **[リトリーバー](https://docs.camel-ai.org/key_modules/retrievers)** | 知識検索とRAGコンポーネント。 |
| **[ランタイム](https://github.com/camel-ai/camel/tree/master/camel/runtime)** | 実行環境とプロセス管理。 |
| **[ヒューマン・イン・ザ・ループ](https://docs.camel-ai.org/cookbooks/advanced_features/agents_with_human_in_loop_and_tool_approval)** | 人間による監視と介入のための対話型コンポーネント。 |
---

## 研究

私たちは、これらのエージェントを大規模に研究することで、その行動、能力、潜在的なリスクについて貴重な洞察が得られると信じています。

**私たちの研究プロジェクトを探索する：**

<div align="center">
  <a href="https://github.com/camel-ai/owl">
    <img src="docs/images/owl.png" alt="OWL">
  </a>
</div>

<div align="center">
  <a href="https://oasis.camel-ai.org/">
    <img src="docs/images/oasis.png" alt="OASIS">
  </a>
</div>

<div align="center">
  <a href="https://crab.camel-ai.org/">
    <img src="docs/images/crab.png" alt="CRAB">
  </a>
</div>

<div align="center">
  <a href="https://github.com/camel-ai/loong">
    <img src="docs/images/loong.png" alt="Loong">
  </a>
</div>

<div align="center">
  <a href="https://agent-trust.camel-ai.org/">
    <img src="docs/images/agent_trust.png" alt="Agent Trust">
  </a>
</div>

<div align="center">
  <a href="https://emos-project.github.io/">
    <img src="docs/images/emos.png" alt="Emos">
  </a>
</div>

>### 私たちと一緒に研究しませんか
>
>CAMELをあなたのインパクトのある研究に使用することを心から歓迎します。
>
> 厳格な研究には時間とリソースが必要です。私たちは、マルチエージェントシステムの最前線の研究を探求する100人以上の研究者からなるコミュニティ主導の研究集団です。私たちの進行中のプロジェクトに参加するか、私たちと新しいアイデアをテストしてください。詳細については[メールでお問い合わせ](mailto:camel-ai@eigent.ai)ください。
>
><div align="center">
>    <img src="docs/images/partners.png" alt="Partners">
></div>

<br>

## 合成データセット

### 1. バックエンドとして様々なLLMを活用

詳細については、[`モデルドキュメント`](https://docs.camel-ai.org/key_modules/models#)をご覧ください。

> **データ（Hugging Faceでホスト）**

| データセット        | チャット形式                                                                                         | インストラクション形式                                                                                               | チャット形式（翻訳済み）                                                                   |
|----------------|-----------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| **AI Society** | [チャット形式](https://huggingface.co/datasets/camel-ai/ai_society/blob/main/ai_society_chat.tar.gz) | [インストラクション形式](https://huggingface.co/datasets/camel-ai/ai_society/blob/main/ai_society_instructions.json) | [チャット形式（翻訳済み）](https://huggingface.co/datasets/camel-ai/ai_society_translated) |
| **Code**       | [チャット形式](https://huggingface.co/datasets/camel-ai/code/blob/main/code_chat.tar.gz)             | [インストラクション形式](https://huggingface.co/datasets/camel-ai/code/blob/main/code_instructions.json)             | x                                                                                          |
| **Math**       | [チャット形式](https://huggingface.co/datasets/camel-ai/math)                                        | x                                                                                                                | x                                                                                          |
| **Physics**    | [チャット形式](https://huggingface.co/datasets/camel-ai/physics)                                     | x                                                                                                                | x                                                                                          |
| **Chemistry**  | [チャット形式](https://huggingface.co/datasets/camel-ai/chemistry)                                   | x                                                                                                                | x                                                                                          |
| **Biology**    | [チャット形式](https://huggingface.co/datasets/camel-ai/biology)                                     | x                                                                                                                | x                                                                                          |

### 2. インストラクションとタスクの可視化

| データセット          | インストラクション                                                                                                         | タスク                                                                                                         |
|------------------|----------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
