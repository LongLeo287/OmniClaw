---
id: oasis
type: knowledge
owner: OA_Triage
---
# oasis
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<div align="center">
  <a href="https://www.camel-ai.org/">
    <img src="assets/banner.png" alt=banner>
  </a>
</div>

</br>

<div align="center">

<h1> OASIS: Open Agent Social Interaction Simulations with One Million Agents
</h1>

[![Documentation][docs-image]][docs-url]
[![Discord][discord-image]][discord-url]
[![X][x-image]][x-url]
[![Reddit][reddit-image]][reddit-url]
[![Wechat][wechat-image]][wechat-url]
[![Wechat][oasis-image]][oasis-url]
[![Hugging Face][huggingface-image]][huggingface-url]
[![Star][star-image]][star-url]
[![Package License][package-license-image]][package-license-url]

<h4 align="center">

[Community](https://github.com/camel-ai/camel#community) |
[Paper](https://arxiv.org/abs/2411.11581) |
[Examples](https://github.com/camel-ai/oasis/tree/main/examples) |
[Dataset](https://huggingface.co/datasets/echo-yiyiyi/oasis-dataset) |
[Citation](https://github.com/camel-ai/oasis#-citation) |
[Contributing](https://github.com/camel-ai/oasis#-contributing-to-oasis) |
[CAMEL-AI](https://www.camel-ai.org/)

</h4>

</div>

<br>

<p align="left">
  <img src='assets/intro.png'>

🏝️ OASIS is a scalable, open-source social media simulator that incorporates large language model agents to realistically mimic the behavior of up to one million users on platforms like Twitter and Reddit. It's designed to facilitate the study of complex social phenomena such as information spread, group polarization, and herd behavior, offering a versatile tool for exploring diverse social dynamics and user interactions in digital environments.

</p>

<br>

<div align="center">
🌟 Star OASIS on GitHub and be instantly notified of new releases.
</div>

<br>

<div align="center">
    <img src="assets/star.gif" alt="Star" width="196" height="52">
  </a>
</div>

<br>

## ✨ Key Features

### 📈 Scalability

OASIS supports simulations of up to ***one million agents***, enabling studies of social media dynamics at a scale comparable to real-world platforms.

### 📲 Dynamic Environments

Adapts to real-time changes in social networks and content, mirroring the fluid dynamics of platforms like **Twitter** and **Reddit** for authentic simulation experiences.

### 👍🏼 Diverse Action Spaces

Agents can perform **23 actions**, such as following, commenting, and reposting, allowing for rich, multi-faceted interactions.

### 🔥 Integrated Recommendation Systems

Features **interest-based** and **hot-score-based recommendation algorithms**, simulating how users discover content and interact within social media platforms.

<br>

## 📺 Demo Video

### Introducing OASIS: Open Agent Social Interaction Simulations with One Million Agents

https://github.com/user-attachments/assets/3bd2553c-d25d-4d8c-a739-1af51354b15a

<br>

For more showcaes:

- Can 1,000,000 AI agents simulate social media?
  [→Watch demo](https://www.youtube.com/watch?v=lprGHqkApus&t=2s)

<br>

## 🎯 Usecase

<div align="left">
    <img src="assets/research_simulation.png" alt=usecase1>
    <img src="assets/interaction.png" alt=usecase2>
   <a href="http://www.matrix.eigent.ai">
    <img src="assets/content_creation.png" alt=usecase3>
   </a>
    <img src="assets/prediction.png" alt=usecase4>
</div>

## ⚙️ Quick Start

1. **Install the OASIS package:**

Installing OASIS is a breeze thanks to its availability on PyPI. Simply open your terminal and run:

```bash
pip install camel-oasis
```

2. **Set up your OpenAI API key:**

```bash
# For Bash shell (Linux, macOS, Git Bash on Windows):
export OPENAI_API_KEY=<insert your OpenAI API key>

# For Windows Command Prompt:
set OPENAI_API_KEY=<insert your OpenAI API key>
```

3. **Prepare the agent profile file:**

Create the profile you want to assign to the agent. As an example, you can download [user_data_36.json](https://github.com/camel-ai/oasis/blob/main/data/reddit/user_data_36.json) and place it in your local `./data/reddit` folder.

4. **Run the following Python code:**

```python
import asyncio
import os

from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType

import oasis
from oasis import (ActionType, LLMAction, ManualAction,
                   generate_reddit_agent_graph)


async def main():
    # Define the model for the agents
    openai_model = ModelFactory.create(
        model_platform=ModelPlatformType.OPENAI,
        model_type=ModelType.GPT_4O_MINI,
    )

    # Define the available actions for the agents
    available_actions = [
        ActionType.LIKE_POST,
        ActionType.DISLIKE_POST,
        ActionType.CREATE_POST,
        ActionType.CREATE_COMMENT,
        ActionType.LIKE_COMMENT,
        ActionType.DISLIKE_COMMENT,
        ActionType.SEARCH_POSTS,
        ActionType.SEARCH_USER,
        ActionType.TREND,
        ActionType.REFRESH,
        ActionType.DO_NOTHING,
        ActionType.FOLLOW,
        ActionType.MUTE,
    ]

    agent_graph = await generate_reddit_agent_graph(
        profile_path="./data/reddit/user_data_36.json",
        model=openai_model,
        available_actions=available_actions,
    )

    # Define the path to the database
    db_path = "./data/reddit_simulation.db"

    # Delete the old database
    if os.path.exists(db_path):
        os.remove(db_path)

    # Make the environment
    env = oasis.make(
        agent_graph=agent_graph,
        platform=oasis.DefaultPlatformType.REDDIT,
        database_path=db_path,
    )

    # Run the environment
    await env.reset()

    actions_1 = {}
    actions_1[env.agent_graph.get_agent(0)] = [
        ManualAction(action_type=ActionType.CREATE_POST,
                     action_args={"content": "Hello, world!"}),
        ManualAction(action_type=ActionType.CREATE_COMMENT,
                     action_args={
                         "post_id": "1",
                         "content": "Welcome to the OASIS World!"
                     })
    ]
    actions_1[env.agent_graph.get_agent(1)] = ManualAction(
        action_type=ActionType.CREATE_COMMENT,
        action_args={
            "post_id": "1",
            "content": "I like the OASIS world."
        })
    await env.step(actions_1)

    actions_2 = {
        agent: LLMAction()
        for _, agent in env.agent_graph.get_agents()
    }

    # Perform the actions
    await env.step(actions_2)

    # Close the environment
    await env.close()


if __name__ == "__main__":
    asyncio.run(main())
```

<br>

> \[!TIP\]
> For more detailed instructions and additional configuration options, check out the [documentation](https://docs.oasis.camel-ai.org/).

### More Tutorials

To discover how to create profiles for large-scale users, as well as how to visualize and analyze social simulation data once your experiment concludes, please refer to [More Tutorials](examples/experiment/user_generation_visualization.md) for detailed guidance.

<div align="center">
  <img src="assets/tutorial.png" alt="Tutorial Overview">
</div>

## 📢 News

### Upcoming Features & Contributions

> We welcome community contributions! Join us in building these exciting features.

- [Support Multi Modal Platform](https://github.com/camel-ai/oasis/issues/47)

<!-- - Public release of our dataset on Hugging Face (November 05, 2024) -->

### Latest Updates

📢 Update the camel-ai version to 0.2.78 and update the dataset HuggingFace link.  - 📆 December 4, 2025

- Add the report post action to mark inappropriate content. - 📆 June 8, 2025
- Add features for creating group chats, sending messages in group chats, and leaving group chats. - 📆 June 6, 2025
- Support Interview Action for asking agents specific questions and getting answers. - 📆 June 2, 2025
- Support customization of each agent's models, tools, and prompts; refactor the interface to follow the PettingZoo style. - 📆 May 22, 2025
- Refactor into the OASIS environment, publish camel-oasis on PyPI, and release the documentation. - 📆 April 24, 2025
- Support OPENAI Embedding model for Twhin-Bert Recommendation System. - 📆 March 25, 2025
  ...
- Slightly refactoring the database to add Quote Action and modify Repost Action - 📆 January 13, 2025
- Added the demo video and oasis's star history in the README - 📆 January 5, 2025
- Introduced an Electronic Mall on the Reddit platform - 📆 December 5, 2024
- OASIS initially released on arXiv - 📆 November 19, 2024
- OASIS GitHub repository initially launched - 📆 November 19, 2024

## 🔎 Follow-up Research

- [MultiAgent4Collusion](https://github.com/renqibing/MultiAgent4Collusion): multi-agent collusion simulation framework in social systems
- [CUBE](https://github.com/echo-yiyiyi/cube): dynamic simulations in customized unity3D-based environments
- [MultiAgent4Fraud](https://github.com/zheng977/MutiAgent4Fraud): financial fraud risks by collaborative LLM agents on social platforms
- More to come...

If your research is based on OASIS, we'd be happy to feature your work here—feel free to reach out or submit a pull request to add it to the [README](https://github.com/camel-ai/oasis/blob/main/README.md)!

## 🥂 Contributing to OASIS🏝️

> We greatly appreciate your interest in contributing to our open-source initiative. To ensure a smooth collaboration and the success of contributions, we adhere to a set of contributing guidelines similar to those established by CAMEL. For a comprehensive understanding of the steps involved in contributing to our project, please refer to the OASIS [contributing guidelines](https://github.com/camel-ai/oasis/blob/master/CONTRIBUTING.md). 🤝🚀
>
> An essential part of contributing involves not only submitting new features with accompanying tests (and, ideally, examples) but also ensuring that these contributions pass our automated pytest suite. This approach helps us maintain the project's quality and reliability by verifying compatibility and functionality.

## 📬 Community & Contact

If you're keen on exploring new research opportunities or discoveries with our platform and wish to dive deeper or suggest new features, we're here to talk. Feel free to get in touch for more details at camel.ai.team@gmail.com.

<br>

- Join us ([*Discord*](https://discord.camel-ai.org/) or [*WeChat*](https://ghli.org/camel/wechat.png)) in pushing the boundaries of finding the scaling laws of agents.

- Join WechatGroup for further discussions!

<div align="">
  <img src="assets/wechatgroup.png" alt="WeChat Group QR Code" width="600">
</div>

## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=camel-ai/oasis&type=Date)](https://star-history.com/#camel-ai/oasis&Date)

## 🔗 Citation

```
@misc{yang2024oasisopenagentsocial,
      title={OASIS: Open Agent Social Interaction Simulations with One Million Agents},
      author={Ziyi Yang and Zaibin Zhang and Zirui Zheng and Yuxian Jiang and Ziyue Gan and Zhiyu Wang and Zijian Ling and Jinsong Chen and Martz Ma and Bowen Dong and Prateek Gupta and Shuyue Hu and Zhenfei Yin and Guohao Li and Xu Jia and Lijun Wang and Bernard Ghanem and Huchuan Lu and Chaochao Lu and Wanli Ouyang and Yu Qiao and Philip Torr and Jing Shao},
      year={2024},
      eprint={2411.11581},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2411.11581},
}
```

## 🙌 Acknowledgment

We would like to thank Douglas for designing the logo of our project.

## 🖺 License

The source code is licensed under Apache 2.0.

[discord-image]: https://img.shields.io/discord/1082486657678311454?logo=discord&labelColor=%20%235462eb&logoColor=%20%23f5f5f5&color=%20%235462eb
[discord-url]: https://discord.camel-ai.org/
[docs-image]: https://img.shields.io/badge/Documentation-EB3ECC
[docs-url]: https://docs.oasis.camel-ai.org/
[huggingface-image]: https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-CAMEL--AI-ffc107?color=ffc107&logoColor=white
[huggingface-url]: https://huggingface.co/camel-ai
[oasis-image]: https://img.shields.io/badge/WeChat-OASISProject-brightgreen?logo=wechat&logoColor=white
[oasis-url]: ./assets/wechatgroup.png
[package-license-image]: https://img.shields.io/badge/License-Apache_2.0-blue.svg
[package-license-url]: https://github.com/camel-ai/oasis/blob/main/licenses/LICENSE
[reddit-image]: https://img.shields.io/reddit/subreddit-subscribers/CamelAI?style=plastic&logo=reddit&label=r%2FCAMEL&labelColor=white
[reddit-url]: https://www.reddit.com/r/CamelAI/
[star-image]: https://img.shields.io/github/stars/camel-ai/oasis?label=stars&logo=github&color=brightgreen
[star-url]: https://github.com/camel-ai/oasis/stargazers
[wechat-image]: https://img.shields.io/badge/WeChat-CamelAIOrg-brightgreen?logo=wechat&logoColor=white
[wechat-url]: ./assets/wechat.JPGwechat.jpg
[x-image]: https://img.shields.io/twitter/follow/CamelAIOrg?style=social
[x-url]: https://x.com/CamelAIOrg

```

### File: .container\README.md
```md
# Install OASIS with Docker

Docker provides a consistent and isolated environment to build, run, and develop oasis without worrying about system dependencies. This guide walks you through setting up oasis using Docker, running it, and developing with it.

## Prerequisites

- Docker：https://docs.docker.com/engine/install/
- Docker Compose：https://docs.docker.com/compose/install/

## Configure Environment

Before starting the container, you need to navigate into the
[.container](../.container) folder and create a `.env` file **with your own
API keys**, so that these keys will be present in the environment variables of
the container, which will later be used by OASIS.

```bash
cd .container

# Create your own .env file by copying the example
cp .env.example .env

# Edit .env to add your API keys or custom settings
```

## Start Container

To build and start the development container:

```bash
docker compose up -d
```

This will:

- Build the image oasis:localdev
- Start the container oasis-localdev
- Set up all necessary dependencies

After the build is complete, you can verify the list of images and all running containers.

```bash
# List all Docker images
docker images
# Check running containers
docker ps
```

## Enter the Container

Once running, you can access the container like this:

```bash
docker compose exec oasis bash
```

You’ll now be inside the oasis dev environment.

From here, you can activate your virtual environment (if used) and run tests:

```bash
# Any other dev/test command
pytest
pre-commit run --all-files
```

## Save Your Progress

Your local code is volume-mounted into the container. That means any changes you make inside the container are reflected in your local project folder — no need to worry about losing your work.

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

For users who only want to have a quick tryout on OASIS, we also provide the
pre-built images on
[our GitHub Container Registry](<>).

## Pre-built Image (Optional)

If you only want to try oasis without setting up the build:

```bash

```

```

### File: docs\README.md
```md
# Mintlify Starter Kit

### Development

Install the [Mintlify CLI](https://www.npmjs.com/package/mintlify) to preview the documentation changes locally. To install, use the following command

```
npm i -g mintlify
```

Run the following command at the root of your documentation (where docs.json is)

```
mintlify dev
```

**Note:** The `docs.json` file is the core configuration that defines your docs' navigation and layout, making it essential for Mintlify to properly run and preview your site.

### Publishing Changes

Our GitHub App is already installed and seamlessly propagates changes from the OASIS repo to https://docs.oasis.camel-ai.org/. Updates are automatically deployed to production whenever changes are pushed to the main branch.

### Troubleshooting

- Mintlify dev isn't running - Run `mintlify install` it'll re-install dependencies.
- Page loads as a 404 - Make sure you are running in a folder with `docs.json`

```

### File: .pre-commit-config.yaml
```yaml
default_language_version:
  python: python3

repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: end-of-file-fixer
        name: End-of-file fixer
      - id: mixed-line-ending
        name: Mixed line ending fixer
        args: [--fix, lf]
      - id: trailing-whitespace
        name: Remove trailing whitespaces
      - id: check-toml
        name: Check toml
      - id: check-yaml
        name: Check yaml
        exclude: |
          (?x)^(
              conda/pytorch-geometric/meta.yaml|
              conda/pyg/meta.yaml
          )$

  - repo: https://github.com/adrienverge/yamllint.git
    rev: v1.35.1
    hooks:
      - id: yamllint
        name: Lint yaml
        args: [-d, '{extends: default, rules: {line-length: disable, document-start: disable, truthy: {level: error}, braces: {max-spaces-inside: 1}}}']

  - repo: https://github.com/pycqa/isort
    rev: 5.13.2
    hooks:
      - id: isort
        name: Sort imports

  - repo: https://github.com/PyCQA/flake8
    rev: 7.0.0
    hooks:
      - id: flake8
        name: Check PEP8
        additional_dependencies: [Flake8-pyproject]

  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.3.5
    hooks:
      - id: ruff
        name: Ruff formatting
        args: [--fix, --exit-non-zero-on-fix]

  - repo: https://github.com/executablebooks/mdformat
    rev: 0.7.17
    hooks:
      - id: mdformat
        name: Format Markdown
        additional_dependencies:
          - mdformat-gfm
          - mdformat_frontmatter
          - mdformat_footnote
  - repo: local
    hooks:
      - id: check-license
        name: Check License
        entry: python licenses/update_license.py . licenses/license_template.txt
        language: system
        types: [python]

```

### File: CONTRIBUTING.md
```md
🏝️ **Welcome to OASIS!** 🏝️

Thank you for your interest in contributing to the OASIS project! 🎉 We're excited to have your support. As an open-source initiative in a rapidly evolving and open-ended field, we wholeheartedly welcome contributions of all kinds. Whether you want to introduce new features, enhance the infrastructure, improve documentation, asking issues, add more examples, implement state-of-the-art research ideas, or fix bugs, we appreciate your enthusiasm and efforts. 🙌  You are welcome to join our [discord](https://discord.com/channels/1115015097560076329/1315102455624892469) or [wechat group](assets/wechatgroup.png) for more efficient communication. 💬

## Join Our Community 🌍

### Developer Meeting Time & Link 💻

- English speakers: Coming soon.
- Chinese Speakers: Thursday at 10 PM UTC+8. Join via TecentMeeting: [Meeting Link](https://meeting.tencent.com/dm/4D2TCb67tTyB)

### Our Communication Channels 💬

- **Discord:** [Join here](https://discord.com/channels/1115015097560076329/1315102455624892469)
- **WeChat:** Scan the QR code [here](assets/wechatgroup.png)

## Guidelines 📝

### Contributing to the Code 👨‍💻👩‍💻

If you're eager to contribute to this project, that's fantastic! We're thrilled to have your support.

- If you are a contributor from the community:
  - Follow the [Fork-and-Pull-Request](https://docs.github.com/en/get-started/quickstart/contributing-to-projects) workflow when opening your pull requests.
- If you are a member of [CAMEL-AI.org](https://github.com/camel-ai) or a collaborator of OASIS:
  - Follow the [Checkout-and-Pull-Request](https://dev.to/ceceliacreates/how-to-create-a-pull-request-on-github-16h1) workflow when opening your pull request; this will allow the PR to pass all tests that require [GitHub Secrets](https://docs.github.com/en/actions/security-guides/encrypted-secrets).

Make sure to mention any related issues and tag the relevant maintainers too. 💪

Before your pull request can be merged, it must pass the formatting, linting, and testing checks. You can find instructions on running these checks locally under the **Common Actions** section below. 🔍

Ensuring excellent documentation and thorough testing is absolutely crucial. Here are some guidelines to follow based on the type of contribution you're making:

- If you fix a bug:
  - Add a relevant unit test when possible. These can be found in the `test` directory.
- If you make an improvement:
  - Update any affected example console scripts in the `examples` directory, and documentation in the `docs` directory.
  - Update unit tests when relevant.
- If you add a feature:
  - Include unit tests in the `test` directory.
  - Add a demo script in the `examples` directory.

We're a small team focused on building great things. If you have something in mind that you'd like to add or modify, opening a pull request is the ideal way to catch our attention. 🚀

### Contributing to Code Reviews 🔍

This part outlines the guidelines and best practices for conducting code reviews in OASIS. The aim is to ensure that all contributions are of high quality, align with the project's goals, and are consistent with our coding standards.

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
- Once the code is approved by at least one reviewer, it can be merged into the main branch.
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
    Currently we use Ruff for format check and take [Google Python Style Guide](%22https://google.github.io/styleguide/pyguide.html%22) as reference.
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

Code reviews are an essential part of maintaining the quality and integrity of our open source project. By following these guidelines, we can ensure that OASIS remains robust, secure, and easy to maintain, while also fostering a collaborative and welcoming community.

### Guideline for Writing Docstrings

This guideline will help you write clear, concise, and structured docstrings for contributing to `OASIS`.

#### 1. Use the Triple-Quoted String with `r"""` (Raw String)

Begin the docstring with `r"""` to indicate a raw docstring. This prevents any issues with special characters and ensures consistent formatting.

#### 2. Provide a Brief Class or Method Description

- Start with a concise summary of the purpose and functionality.
- Keep each line under `79` characters.
- The summary should start on the first line without a linebreak.

Example:

```python
r"""Class for managing conversations of OASIS Agents.
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
    system_message (BaseMessage): The system message for initializing
        the agent's conversation context.
    model (BaseModelBackend, optional): The model backend to use for
        response generation. Defaults to :obj:`OpenAIModel` with
        `GPT_4O_MINI`. (default: :obj:`OpenAIModel` with `GPT_4O_MINI`)
```

### Principles 🛡️

#### Naming Principle: Avoid Abbreviations in Naming

- Abbreviations can lead to ambiguity, especially since variable names and code in OASIS are directly used by agents.
- Use clear, descriptive names that convey meaning without requiring additional explanation. This improves both human readability and the agent's ability to interpret the code.

Examples:

- Bad: msg_win_sz
- Good: message_window_size

By adhering to this principle, we ensure that OASIS remains accessible and unambiguous for both developers and AI agents.

#### Logging Principle: Use `logger` Instead of `print`

Avoid using `print` for output. Use Python's `logging` module (`logger`) to ensure consistent, configurable, and professional logging.

Examples:

- Bad:
  ```python
  print("Process started")
  print(f"User input: {user_input}")
  ```
- Good:
  ```python
  Args:
  logger.info("Process started")
  logger.debug(f"User input: {user_input}")
  ```

### Board Item Create Workflow 🛠️

At OASIS, we manage our project through a structured workflow that ensures efficiency and clarity in our development process. Our workflow includes stages for issue creation and pull requests (PRs), sprint planning, and reviews.

#### Issue Item Stage:

Our [issues](https://github.com/camel-ai/oasis/issues) page on GitHub is regularly updated with bugs, improvements, and feature requests. We have a handy set of labels to help you sort through and find issues that interest you. Feel free to use these labels to keep things organized.

When you start working on an issue, please assign it to yourself so that others know it's being taken care of. If you're unable to assign it to yourself because you're not an OASIS collaborator, feel free to leave a comment on the issue instead.

When creating a new issue, it's best to keep it focused on a specific bug, improvement, or feature. If two issues are related or blocking each other, it's better to link them instead of merging them into one.

We do our best to keep these issues up to date, but considering the fast-paced nature of this field, some may become outdated. If you come across any such issues, please give us a heads-up so we can address them promptly. 👀

Here’s how to engage with our issues effectively:

- Go to [GitHub Issues](https://github.com/camel-ai/oasis/issues), create a new issue, choose the category, and fill in the required information.
- Ensure the issue has a proper title and update the Assignees, Labels, Projects (select Backlog status), Development, and Milestones.
- Discuss the issue during team meetings, then move it to the Analysis Done column.
- At the beginning of each sprint, share the analyzed issue and move it to the Sprint Planned column if you are going to work on this issue in the sprint.

#### Pull Request Item Stage:

- Go to [GitHub Pulls](https://github.com/camel-ai/oasis/pulls), create a new PR, choose the branch, and fill in the information, linking the related issue.
- Ensure the PR has a proper title and update the Reviewers (convert to draft), Assignees, Labels, Projects (select Developing status), Development, and Milestones.
- If the PR is related to a roadmap, link the roadmap to the PR.
- Move the PR item through the stages: Developing, Stuck, Reviewing (click ready for review), Merged. The linked issue will close automatically when the PR is merged.

**Labeling PRs:**

- **feat**: For new features (e.g., `feat: Add new AI model`)
- **fix**: For bug fixes (e.g., `fix: Resolve memory leak issue`)
- **docs**: For documentation updates (e.g., `docs: Update contribution guidelines`)
- **style**: For code style changes (e.g., `style: Refactor code formatting`)
- **refactor**: For code refactoring (e.g., `refactor: Optimize data processing`)
- **test**: For adding or updating tests (e.g., `test: Add unit tests for new feature`)
- **chore**: For maintenance tasks (e.g., `chore: Update dependencies`)

### Sprint Planning & Review 🎯

#### Definition

Sprint planning defines what can be delivered in the sprint and how it will be achieved. Sprint review allows stakeholders to review and provide feedback on recent work.

#### Practice

- **Sprint Duration**: Four weeks for development and review.
- **Sprint Planning & Review**: Conducted biweekly during the dev meeting (around 30 minutes).
- **Planning**: Founder highlights the sprint goal and key points; developers pick items for the sprint.
- **Review**: Feedback on delivered features and identification of improvement areas.

### Getting Help 🆘

Our aim is to make the developer setup as straightforward as possible. If you encounter any challenges during the setup process, don't hesitate to reach out to a maintainer. We're here to assist you and ensure that the experience is smooth not just for you but also for future contributors. 😊

In line with this, we do have specific guidelines for code linting, formatting, and documentation in the codebase. If you find these requirements difficult or even just bothersome to work with, please feel free to get in touch with a maintainer — you can *@doudou_wu in Discord or @张再斌 in the WeChat group*. We don't want these guidelines to hinder the integration of good code into the codebase, so we're more than happy to provide support and find a solution that works for you. 🤝

## Quick Start 🚀

To get started with OASIS, follow these steps:

```sh
# Clone github repo
git clone https://github.com/camel-ai/oasis.git

# Change directory into project directory
cd oasis

# Install oasis from source (this will create the virtual environment if needed)
poetry install

# Activate oasis virtual environment
eval $(poetry env activate)

# The following command installs a pre-commit hook into the local git repo,
# so every commit gets auto-formatted and linted.
pre-commit install

# Run oasis's pre-commit before push
pre-commit run --all-files

# Run oasis's unit tests
pytest test

# Exit the virtual environment
deactivate

# Alternative: You can also use 'poetry run' prefix without activating the environment
# poetry run pytest test
```

These commands will install all the necessary dependencies for running the package, examples, linting, formatting, tests, and coverage.

To verify that everything is set up correctly, run `pytest .` This will ensure that all tests pass successfully. ✅

> \[!TIP\]
> You need to config OPENAI API Keys as environment variables to pass all tests.

## Common Actions 🔄

### Update dependencies

Whenever you add, update, or delete any dependencies in `pyproject.toml`, please run `poetry lock` to synchronize the dependencies with the lock file.

### Coverage 📊

Code coverage measures the extent to which unit tests cover the code, helping identify both robust and less robust areas of the codebase.

To generate a report showing the current code coverage, execute one of the following commands.

To include all source files into coverage:

```bash
coverage erase
coverage run --source=. -m pytest .
coverage html
# Open htmlcov/index.html
```

To include only tested files:

```bash
pytest --cov --cov-report=html
```

The
... [TRUNCATED]
```

### File: deploy.py
```py
# =========== Copyright 2023 @ CAMEL-AI.org. All Rights Reserved. ===========
# Licensed under the Apache License, Version 2.0 (the “License”);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an “AS IS” BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =========== Copyright 2023 @ CAMEL-AI.org. All Rights Reserved. ===========
import subprocess
import threading
import time

import requests


def check_port_open(host, port):
    while True:
        url = f"http://{host}:{port}/health"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                break
            else:
                time.sleep(0.3)
        except Exception:
            time.sleep(0.3)


if __name__ == "__main__":
    host = "10.109.1.8"
    ports = [
        [8002, 8003, 8005],
        [8006, 8007, 8008],
        [8011, 8009, 8010],
        [8014, 8012, 8013],
        [8017, 8015, 8016],
        [8020, 8018, 8019],
        [8021, 8022, 8023],
        [8024, 8025, 8026],
    ]
    gpus = [0]

    all_ports = [port for i in gpus for port in ports[i]]
    print("All ports: ", all_ports, '\n\n')

    t = None
    for i in range(3):
        for j, gpu in enumerate(gpus):
            cmd = (
                f"CUDA_VISIBLE_DEVICES={gpu} python -m "
                f"vllm.entrypoints.openai.api_server --model "
                f"'/ibex/user/yangz0h/open_source_llm/llama-3' "
                f"--served-model-name 'llama-3' "
                f"--host {host} --port {ports[j][i]} --gpu-memory-utilization "
                f"0.3 --disable-log-stats")
            t = threading.Thread(target=subprocess.run,
                                 args=(cmd, ),
                                 kwargs={"shell": True},
                                 daemon=True)
            t.start()
        check_port_open(host, ports[0][i])

    t.join()

```

### File: .container\docker-compose.yaml
```yaml
services:
  oasis:
    image: oasis:localdev
    container_name: oasis-localdev
    build:
      context: ../
      dockerfile: .container/Dockerfile
    volumes:
      - ../:/app/oasis
    env_file:
      - .env
    command: ["tail", "-f", "/dev/null"]

```

### File: .github\PULL_REQUEST_TEMPLATE.md
```md
## Description

Describe your changes in detail (optional if the linked issue already contains a detailed description of the changes).

## Checklist

Go over all the following points, and put an `x` in all the boxes that apply.

- [ ] I have read the [CONTRIBUTION](https://github.com/camel-ai/oasis/blob/master/CONTRIBUTING.md) guide (**required**)
- [ ] I have linked this PR to an issue using the Development section on the right sidebar or by adding `Fixes #issue-number` in the PR description (**required**)
- [ ] I have checked if any dependencies need to be added or updated in `pyproject.toml`
- [ ] I have updated the tests accordingly (*required for a bug fix or a new feature*)
- [ ] I have updated the documentation if needed:
- [ ] I have added examples if this is a new feature

**Note:** If you are developing a new action for `SocialAgent`, please review the checklist below and mark all applicable items with an `x`. If you're not adding a new action, you can skip this section.

- [ ] I have added the new action to `ActionType` in [`typing.py`](https://github.com/camel-ai/oasis/blob/main/oasis/social_platform/typing.py).
- [ ] I have added a corresponding test or a similar function, as shown in [`test_user_create_post.py`](https://github.com/camel-ai/oasis/blob/main/test/infra/database/test_user_create_post.py).
- [ ] I have included the new `ActionType` in both [`test_action_docstring.py`](https://github.com/camel-ai/oasis/blob/main/test/agent/test_action_docstring.py) and [`test_twitter_user_agent_all_actions.py`](https://github.com/camel-ai/oasis/blob/main/test/agent/test_twitter_user_agent_all_actions.py).
- [ ] I have documented the new action in [`actions.mdx`](https://github.com/camel-ai/oasis/blob/main/docs/key_modules/actions.mdx); the Mintlify GitHub app will deploy the changes automatically.

If you are unsure about any of these, don't hesitate to ask. We are here to help!

```

### File: docs\docs.json
```json
{
  "$schema": "https://mintlify.com/docs.json",
  "theme": "mint",
  "name": "OASIS",
  "colors": {
    "primary": "#6D28D9",
    "light": "#A78BFA",
    "dark": "#4C1D95"
  },
  "favicon": "/favicon.svg",
  "navigation": {
    "tabs": [
      {
        "tab": "Guides",
        "groups": [
          {
            "group": "Get Started",
            "pages": [
              "introduction",
              "quickstart"
            ]
          },
          {
            "group": "Overview",
            "pages": [
              "overview"
            ]
          },
          {
            "group": "Key Modules",
            "pages": [
              "key_modules/environments",
              "key_modules/agent_graph",
              "user_generation/generation",
              "key_modules/social_agent",
              "key_modules/models",
              "key_modules/toolkits",
              "key_modules/platform",
              "key_modules/actions"
            ]
          },
          {
            "group": "Cookbooks",
            "pages": [
              "cookbooks/twitter_simulation",
              "cookbooks/reddit_simulation",
              "cookbooks/sympy_tools_simulation",
              "cookbooks/search_tools_simulation",
              "cookbooks/custom_prompt_simulation",
              "cookbooks/twitter_interview"
            ]
          },
          {
            "group": "Visualization",
            "pages": [
              "visualization/visualization"
            ]
          }
        ]
      }
    ],
    "global": {
      "anchors": [
        {
          "anchor": "Documentation",
          "href": "https://docs.oasis.camel-ai.org/",
          "icon": "book-open-cover"
        },
        {
          "anchor": "Community",
          "href": "https://discord.com/invite/CNcNpquyDc",
          "icon": "slack"
        },
        {
          "anchor": "Blog",
          "href": "https://www.camel-ai.org/blogs/oasis",
          "icon": "newspaper"
        }
      ]
    }
  },
  "logo": {
    "light": "/logo/normal_logo.svg",
    "dark": "/logo/white_logo.svg",
    "href": "https://www.camel-ai.org/"
  },
  "footer": {
    "socials": {
      "x": "https://x.com/CamelAIOrg",
      "github": "https://github.com/camel-ai",
      "reddit": "https://www.reddit.com/r/CamelAI/",
      "discord": "https://discord.camel-ai.org/",
      "website": "https://www.camel-ai.org/"
    }
  }
}

```

### File: examples\custom_platform_simulation.py
```py
# =========== Copyright 2023 @ CAMEL-AI.org. All Rights Reserved. ===========
# Licensed under the Apache License, Version 2.0 (the “License”);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an “AS IS” BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =========== Copyright 2023 @ CAMEL-AI.org. All Rights Reserved. ===========
import asyncio
import os

from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType

import oasis
from oasis import (ActionType, LLMAction, ManualAction, Platform,
                   generate_twitter_agent_graph)
from oasis.social_platform.channel import Channel
from oasis.social_platform.typing import RecsysType


async def main():
    # Define the models for agents.
    models = ModelFactory.create(
        model_platform=ModelPlatformType.OPENAI,
        model_type=ModelType.GPT_4O_MINI,
    )

    # Define the available actions for the agents
    available_actions = [
        ActionType.CREATE_POST,
        ActionType.LIKE_POST,
        ActionType.REPOST,
        ActionType.FOLLOW,
        ActionType.DO_NOTHING,
    ]

    agent_graph = await generate_twitter_agent_graph(
        profile_path=("data/twitter_dataset/anonymous_topic_200_1h/"
                      "False_Business_0.csv"),
        model=models,
        available_actions=available_actions,
    )

    # Define the path to the database
    db_path = "./data/twitter_simulation.db"
    os.environ["OASIS_DB_PATH"] = os.path.abspath(db_path)

    # Delete the old database
    if os.path.exists(db_path):
        os.remove(db_path)

    channel = Channel()
    customize_platform = Platform(
        db_path=db_path,
        channel=channel,
        recsys_type=RecsysType.TWHIN,
        allow_self_rating=False,  # Not allow agents to rate themselves
        show_score=True,  # Show the scores of posts for agents, instead of
        # only showing the number of likes and dislikes
    )

    # Make the environment
    env = oasis.make(
        agent_graph=agent_graph,
        platform=customize_platform,
    )

    # Run the environment
    await env.reset()

    actions_1 = {}
    actions_1[env.agent_graph.get_agent(0)] = [
        ManualAction(action_type=ActionType.CREATE_POST,
                     action_args={"content": "I am new in the OASIS world."}),
        ManualAction(action_type=ActionType.CREATE_COMMENT,
                     action_args={
                         "post_id": "1",
                         "content": "Let us follow each other."
                     })
    ]
    actions_1[env.agent_graph.get_agent(1)] = ManualAction(
        action_type=ActionType.FOLLOW, action_args={
            "followee_id": "0",
        })
    await env.step(actions_1)

    actions_2 = {
        agent: LLMAction()
        for _, agent in env.agent_graph.get_agents([1, 2, 3])
    }

    # Perform the actions
    await env.step(actions_2)
    # Close the environment
    await env.close()


if __name__ == "__main__":
    asyncio.run(main())

```

### File: examples\custom_prompt_simulation.py
```py
# =========== Copyright 2023 @ CAMEL-AI.org. All Rights Reserved. ===========
# Licensed under the Apache License, Version 2.0 (the “License”);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an “AS IS” BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =========== Copyright 2023 @ CAMEL-AI.org. All Rights Reserved. ===========
import asyncio
import os

from camel.models import ModelFactory
from camel.prompts import TextPrompt
from camel.types import ModelPlatformType, ModelType

import oasis
from oasis import ActionType, AgentGraph, LLMAction, SocialAgent, UserInfo


async def main():
    # Define the model for the agents
    openai_model = ModelFactory.create(
        model_platform=ModelPlatformType.OPENAI,
        model_type=ModelType.GPT_4O_MINI,
    )

    # Define the available actions for the agents
    available_actions = [
        ActionType.LIKE_POST, ActionType.DISLIKE_POST, ActionType.CREATE_POST,
        ActionType.CREATE_COMMENT, ActionType.LIKE_COMMENT,
        ActionType.DISLIKE_COMMENT, ActionType.FOLLOW, ActionType.MUTE,
        ActionType.PURCHASE_PRODUCT
    ]

    seller_template = TextPrompt('Your aim is: {aim} Your task is: {task}')

    profile = {
        "aim": "Persuade people to buy `GlowPod` lamp.",
        "task": "Using roleplay to tell some story about the product.",
    }

    agent_graph = AgentGraph()
    agent_1 = SocialAgent(
        agent_id=0,
        user_info=UserInfo(
            user_name="snackslut",
            name="Snack Slut",
            description="I taste so you don’t have to.",
            profile=profile,
        ),
        user_info_template=seller_template,
        agent_graph=agent_graph,
        model=openai_model,
        available_actions=available_actions,
    )
    agent_graph.add_agent(agent_1)

    agent_2 = SocialAgent(
        agent_id=1,
        user_info=UserInfo(
            user_name="bubble",
            name="Bob",
            description="A boy",
            profile=None,
            recsys_type="reddit",
        ),
        agent_graph=agent_graph,
        model=openai_model,
        available_actions=available_actions,
    )
    agent_graph.add_agent(agent_2)

    # Define the path to the database
    db_path = "./data/reddit_simulation.db"
    os.environ["OASIS_DB_PATH"] = os.path.abspath(db_path)

    # Delete the old database
    if os.path.exists(db_path):
        os.remove(db_path)

    # Make the environment
    env = oasis.make(
        agent_graph=agent_graph,
        platform=oasis.DefaultPlatformType.REDDIT,
        database_path=db_path,
    )

    # Run the environment
    await env.reset()

    # Sign up the profuct
    await env.platform.sign_up_product(product_id=1, product_name="GlowPod")

    for _ in range(5):
        actions = {
            agent: LLMAction()
            for _, agent in env.agent_graph.get_agents()
        }
        await env.step(actions)

    # Close the environment
    await env.close()


if __name__ == "__main__":
    asyncio.run(main())

```

### File: examples\different_model_simulation.py
```py
# =========== Copyright 2023 @ CAMEL-AI.org. All Rights Reserved. ===========
# Licensed under the Apache License, Version 2.0 (the “License”);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an “AS IS” BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =========== Copyright 2023 @ CAMEL-AI.org. All Rights Reserved. ===========
import asyncio
import os

from camel.models import ModelFactory
from camel.types import ModelPlatformType, ModelType

import oasis
from oasis import (ActionType, AgentGraph, LLMAction, ManualAction,
                   SocialAgent, UserInfo)


async def main():
    # Define the model for the agents
    openai_model = ModelFactory.create(
        model_platform=ModelPlatformType.OPENAI,
        model_type=ModelType.GPT_4O_MINI,
    )
    qwen_model = ModelFactory.create(
        model_platform=ModelPlatformType.QWEN,
        model_type=ModelType.QWEN_PLUS,
    )

    # Define the available actions for the agents
    available_actions = [
        ActionType.LIKE_POST,
        ActionType.DISLIKE_POST,
        ActionType.CREATE_POST,
        ActionType.CREATE_COMMENT,
        ActionType.LIKE_COMMENT,
        ActionType.DISLIKE_COMMENT,
        ActionType.FOLLOW,
        ActionType.MUTE,
    ]

    agent_graph = AgentGraph()
    agent_1 = SocialAgent(
        agent_id=0,
        user_info=UserInfo(
            user_name="ali",
            name="Alice",
            description="A girl",
            profile=None,
            recsys_type="reddit",
        ),
        agent_graph=agent_graph,
        model=openai_model,
        available_actions=available_actions,
    )
    agent_graph.add_agent(agent_1)

    agent_2 = SocialAgent(
        agent_id=1,
        user_info=UserInfo(
            user_name="bubble",
            name="Bob",
            description="A boy",
            profile=None,
            recsys_type="reddit",
        ),
        agent_graph=agent_graph,
        model=qwen_model,
        available_actions=available_actions,
    )
    agent_graph.add_agent(agent_2)

    # Define the path to the database
    db_path = "./data/reddit_simulation.db"
    os.environ["OASIS_DB_PATH"] = os.path.abspath(db_path)

    # Delete the old database
    if os.path.exists(db_path):
        os.remove(db_path)

    # Make the environment
    env = oasis.make(
        agent_graph=agent_graph,
        platform=oasis.DefaultPlatformType.REDDIT,
        database_path=db_path,
    )

    # Run the environment
    await env.reset()

    actions_1 = {
        env.agent_graph.get_agent(0): [
            ManualAction(
                action_type=ActionType.CREATE_POST,
                action_args={
                    "content":
                    "Could you tell me which large language model (LLM) you "
                    "are based on? Please answer with your model name or type."
                }),
            ManualAction(action_type=ActionType.CREATE_COMMENT,
                         action_args={
                             "post_id": "1",
                             "content": "Feel free to share your information!"
                         })
        ]
    }
    await env.step(actions_1)

    actions_2 = {
        agent: LLMAction()
        for _, agent in env.agent_graph.get_agents()
    }
    await env.step(actions_2)

    # Close the environment
    await env.close()


if __name__ == "__main__":
    asyncio.run(main())

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
