---
id: skyvern
type: knowledge
owner: OA_Triage
---
# skyvern
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<!-- DOCTOC SKIP -->

<h1 align="center">
 <a href="https://www.skyvern.com">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="fern/images/skyvern_logo.png"/>
    <img height="120" src="fern/images/skyvern_logo_blackbg.png"/>
  </picture>
 </a>
 <br />
</h1>
<p align="center">
🐉 Automate Browser-based workflows using LLMs and Computer Vision 🐉
</p>
<p align="center">
  <a href="https://www.skyvern.com/"><img src="https://img.shields.io/badge/Website-blue?logo=googlechrome&logoColor=black"/></a>
  <a href="https://www.skyvern.com/docs/"><img src="https://img.shields.io/badge/Docs-yellow?logo=gitbook&logoColor=black"/></a>
  <a href="https://discord.gg/fG2XXEuQX3"><img src="https://img.shields.io/discord/1212486326352617534?logo=discord&label=discord"/></a>
  <!-- <a href="https://pepy.tech/project/skyvern" target="_blank"><img src="https://static.pepy.tech/badge/skyvern" alt="Total Downloads"/></a> -->
  <a href="https://github.com/skyvern-ai/skyvern"><img src="https://img.shields.io/github/stars/skyvern-ai/skyvern" /></a>
  <a href="https://github.com/Skyvern-AI/skyvern/blob/main/LICENSE"><img src="https://img.shields.io/github/license/skyvern-ai/skyvern"/></a>
  <a href="https://twitter.com/skyvernai"><img src="https://img.shields.io/twitter/follow/skyvernai?style=social"/></a>
  <a href="https://www.linkedin.com/company/95726232"><img src="https://img.shields.io/badge/Follow%20 on%20LinkedIn-8A2BE2?logo=linkedin"/></a>
</p>

[Skyvern](https://www.skyvern.com) automates browser-based workflows using LLMs and computer vision. It provides a Playwright-compatible SDK that adds AI functionality on top of playwright, as well as a no-code workflow builder to help both technical and non-technical users automate manual workflows on any website, replacing brittle or unreliable automation solutions.

<p align="center">
  <img src="fern/images/geico_shu_recording_cropped.gif"/>
</p>

Traditional approaches to browser automations required writing custom scripts for websites, often relying on DOM parsing and XPath-based interactions which would break whenever the website layouts changed.

Instead of only relying on code-defined XPath interactions, Skyvern relies on Vision LLMs to learn and interact with the websites.

# How it works
Skyvern was inspired by the Task-Driven autonomous agent design popularized by [BabyAGI](https://github.com/yoheinakajima/babyagi) and [AutoGPT](https://github.com/Significant-Gravitas/AutoGPT) -- with one major bonus: we give Skyvern the ability to interact with websites using browser automation libraries like [Playwright](https://playwright.dev/).

Skyvern uses a swarm of agents to comprehend a website, and plan and execute its actions:

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="fern/images/skyvern_2_0_system_diagram.png" />
  <img src="fern/images/skyvern_2_0_system_diagram.png" />
</picture>

This approach has a few advantages:

1. Skyvern can operate on websites it's never seen before, as it's able to map visual elements to actions necessary to complete a workflow, without any customized code
1. Skyvern is resistant to website layout changes, as there are no pre-determined XPaths or other selectors our system is looking for while trying to navigate
1. Skyvern is able to take a single workflow and apply it to a large number of websites, as it's able to reason through the interactions necessary to complete the workflow
A detailed technical report can be found [here](https://www.skyvern.com/blog/skyvern-2-0-state-of-the-art-web-navigation-with-85-8-on-webvoyager-eval/).

# Demo
<!-- Redo demo -->
https://github.com/user-attachments/assets/5cab4668-e8e2-4982-8551-aab05ff73a7f

# Quickstart

## Skyvern Cloud
[Skyvern Cloud](https://app.skyvern.com) is a managed cloud version of Skyvern that allows you to run Skyvern without worrying about the infrastructure. It allows you to run multiple Skyvern instances in parallel and comes bundled with anti-bot detection mechanisms, proxy network, and CAPTCHA solvers.

If you'd like to try it out, navigate to [app.skyvern.com](https://app.skyvern.com) and create an account.

## Run Locally (UI + Server)

Choose your preferred setup method:

### Option A: pip install (Recommended)

Dependencies needed:
- [Python 3.11.x](https://www.python.org/downloads/), works with 3.12, not ready yet for 3.13
- [NodeJS & NPM](https://nodejs.org/en/download/)

Additionally, for Windows:
- [Rust](https://rustup.rs/)
- VS Code with C++ dev tools and Windows SDK

#### 1. Install Skyvern

```bash
pip install skyvern
```

#### 2. Run Skyvern

```bash
skyvern quickstart
```

### Option B: Docker Compose

1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop/)
2. Clone the repository:
   ```bash
   git clone https://github.com/skyvern-ai/skyvern.git && cd skyvern
   ```
3. Run quickstart with Docker Compose:
   ```bash
   pip install skyvern && skyvern quickstart
   ```
   When prompted, choose "Docker Compose" for the full containerized setup.
4. Navigate to http://localhost:8080

## SDK

**Skyvern is a Playwright extension that adds AI-powered browser automation.** It gives you the full power of Playwright with additional AI capabilities—use natural language prompts to interact with elements, extract data, and automate complex multi-step workflows.

**Installation:**
- Python: `pip install skyvern` then run `skyvern quickstart` for local setup
- TypeScript: `npm install @skyvern/client`

### AI-Powered Page Commands

Skyvern adds four core AI commands directly on the page object:

| Command | Description |
|---------|-------------|
| `page.act(prompt)` | Perform actions using natural language (e.g., "Click the login button") |
| `page.extract(prompt, schema)` | Extract structured data from the page with optional JSON schema |
| `page.validate(prompt)` | Validate page state, returns `bool` (e.g., "Check if user is logged in") |
| `page.prompt(prompt, schema)` | Send arbitrary prompts to the LLM with optional response schema |

Additionally, `page.agent` provides higher-level workflow commands:

| Command | Description |
|---------|-------------|
| `page.agent.run_task(prompt)` | Execute complex multi-step tasks |
| `page.agent.login(credential_type, credential_id)` | Authenticate with stored credentials (Skyvern, Bitwarden, 1Password) |
| `page.agent.download_files(prompt)` | Navigate and download files |
| `page.agent.run_workflow(workflow_id)` | Execute pre-built workflows |

### AI-Augmented Playwright Actions

All standard Playwright actions support an optional `prompt` parameter for AI-powered element location:

| Action | Playwright | AI-Augmented |
|--------|------------|--------------|
| Click | `page.click("#btn")` | `page.click(prompt="Click login button")` |
| Fill | `page.fill("#email", "a@b.com")` | `page.fill(prompt="Email field", value="a@b.com")` |
| Select | `page.select_option("#country", "US")` | `page.select_option(prompt="Country dropdown", value="US")` |
| Upload | `page.upload_file("#file", "doc.pdf")` | `page.upload_file(prompt="Upload area", files="doc.pdf")` |

**Three interaction modes:**
```python
# 1. Traditional Playwright - CSS/XPath selectors
await page.click("#submit-button")

# 2. AI-powered - natural language
await page.click(prompt="Click the green Submit button")

# 3. AI fallback - tries selector first, falls back to AI if it fails
await page.click("#submit-btn", prompt="Click the Submit button")
```

### Core AI Commands - Examples

```python
# act - Perform actions using natural language
await page.act("Click the login button and wait for the dashboard to load")

# extract - Extract structured data with optional JSON schema
result = await page.extract("Get the product name and price")
result = await page.extract(
    prompt="Extract order details",
    schema={"order_id": "string", "total": "number", "items": "array"}
)

# validate - Check page state (returns bool)
is_logged_in = await page.validate("Check if the user is logged in")

# prompt - Send arbitrary prompts to the LLM
summary = await page.prompt("Summarize what's on this page")
```

### Quick Start Examples

**Run via UI:**
```bash
skyvern run all
```
Navigate to http://localhost:8080 to run tasks through the web interface.

**Python SDK:**
```python
from skyvern import Skyvern

# Local mode
skyvern = Skyvern.local()

# Or connect to Skyvern Cloud
skyvern = Skyvern(api_key="your-api-key")

# Launch browser and get page
browser = await skyvern.launch_cloud_browser()
page = await browser.get_working_page()

# Mix Playwright with AI-powered actions
await page.goto("https://example.com")
await page.click("#login-button")  # Traditional Playwright
await page.agent.login(credential_type="skyvern", credential_id="cred_123")  # AI login
await page.click(prompt="Add first item to cart")  # AI-augmented click
await page.agent.run_task("Complete checkout with: John Snow, 12345")  # AI task
```

**TypeScript SDK:**
```typescript
import { Skyvern } from "@skyvern/client";

const skyvern = new Skyvern({ apiKey: "your-api-key" });
const browser = await skyvern.launchCloudBrowser();
const page = await browser.getWorkingPage();

// Mix Playwright with AI-powered actions
await page.goto("https://example.com");
await page.click("#login-button");  // Traditional Playwright
await page.agent.login("skyvern", { credentialId: "cred_123" });  // AI login
await page.click({ prompt: "Add first item to cart" });  // AI-augmented click
await page.agent.runTask("Complete checkout with: John Snow, 12345");  // AI task

await browser.close();
```

**Simple task execution:**
```python
from skyvern import Skyvern

skyvern = Skyvern()
task = await skyvern.run_task(prompt="Find the top post on hackernews today")
print(task)
```

## Advanced Usage

### Control your own browser (Chrome)
> [!WARNING]
> Since [Chrome 136](https://developer.chrome.com/blog/remote-debugging-port), Chrome refuses any CDP connect to the browser using the default user_data_dir. In order to use your browser data, Skyvern copies your default user_data_dir to `./tmp/user_data_dir` the first time connecting to your local browser.

1. Just With Python Code
```python
from skyvern import Skyvern

# The path to your Chrome browser. This example path is for Mac.
browser_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
skyvern = Skyvern(
    base_url="http://localhost:8000",
    api_key="YOUR_API_KEY",
    browser_path=browser_path,
)
task = await skyvern.run_task(
    prompt="Find the top post on hackernews today",
)
```

2. With Skyvern Service

Add two variables to your .env file:
```bash
# The path to your Chrome browser. This example path is for Mac.
CHROME_EXECUTABLE_PATH="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
BROWSER_TYPE=cdp-connect
```

Restart Skyvern service `skyvern run all` and run the task through UI or code

### Connect Skyvern Cloud to your local browser

Let Skyvern Cloud control a Chrome browser running on your machine — with all your existing cookies, logins, and extensions. Useful for automating sites where you're already logged in or behind a VPN.

```bash
# One command to start Chrome + create a tunnel to Skyvern Cloud
skyvern browser serve --tunnel
```

Then use the tunnel URL in your task:

```python
from skyvern import Skyvern

skyvern = Skyvern(api_key="your-api-key")
task = await skyvern.run_task(
    prompt="Download the latest invoice from my account",
    browser_address="https://abc123.ngrok-free.dev",
)
```

> [!WARNING]
> Always use `--api-key` when exposing your browser via a tunnel. Without it, anyone with the URL has full control of your browser. See the [security docs](https://www.skyvern.com/docs/optimization/browser-tunneling#security).

See the [full documentation](https://www.skyvern.com/docs/optimization/browser-tunneling) for all options, manual tunnel setup, and troubleshooting.

### Get consistent output schema from your run
You can do this by adding the `data_extraction_schema` parameter:
```python
from skyvern import Skyvern

skyvern = Skyvern()
task = await skyvern.run_task(
    prompt="Find the top post on hackernews today",
    data_extraction_schema={
        "type": "object",
        "properties": {
            "title": {
                "type": "string",
                "description": "The title of the top post"
            },
            "url": {
                "type": "string",
                "description": "The URL of the top post"
            },
            "points": {
                "type": "integer",
                "description": "Number of points the post has received"
            }
        }
    }
)
```

### Helpful commands to debug issues


```bash
# Launch the Skyvern Server Separately*
skyvern run server

# Launch the Skyvern UI
skyvern run ui

# Check status of the Skyvern service
skyvern status

# Stop the Skyvern service
skyvern stop all

# Stop the Skyvern UI
skyvern stop ui

# Stop the Skyvern Server Separately
skyvern stop server
```

# Performance & Evaluation

Skyvern has SOTA performance on the [WebBench benchmark](webbench.ai) with a 64.4% accuracy. The technical report + evaluation can be found [here](https://www.skyvern.com/blog/web-bench-a-new-way-to-compare-ai-browser-agents/)

<p align="center">
  <img src="fern/images/performance/webbench_overall.png"/>
</p>

## Performance on WRITE tasks (eg filling out forms, logging in, downloading files, etc)

Skyvern is the best performing agent on WRITE tasks (eg filling out forms, logging in, downloading files, etc), which is primarily used for RPA (Robotic Process Automation) adjacent tasks.

<p align="center">
  <img src="fern/images/performance/webbench_write.png"/>
</p>

# Skyvern Features

## Skyvern Tasks
Tasks are the fundamental building block inside Skyvern. Each task is a single request to Skyvern, instructing it to navigate through a website and accomplish a specific goal.

Tasks require you to specify a `url`, `prompt`, and can optionally include a `data schema` (if you want the output to conform to a specific schema) and `error codes` (if you want Skyvern to stop running in specific situations).

<p align="center">
  <img src="fern/images/skyvern_2_0_screenshot.png"/>
</p>


## Skyvern Workflows
Workflows are a way to chain multiple tasks together to form a cohesive unit of work.

For example, if you wanted to download all invoices newer than January 1st, you could create a workflow that first navigated to the invoices page, then filtered down to only show invoices newer than January 1st, extracted a list of all eligible invoices, and iterated through each invoice to download it.

Another example is if you wanted to automate purchasing products from an e-commerce store, you could create a workflow that first navigated to the desired product, then added it to a cart. Second, it would navigate to the cart and validate the cart state. Finally, it would go through the checkout process to purchase the items.

Sup
... [TRUNCATED]
```

### File: alembic\README.md
```md
<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Creating a new revision](#creating-a-new-revision)
- [Running migrations](#running-migrations)
- [Downgrading migrations](#downgrading-migrations)
- [Check your current alembic setup](#check-your-current-alembic-setup)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Creating a new revision
```
alembic revision --autogenerate -m "enter description here"
```
**Note:** Please read [What does Autogenerate Detect (and what does it not detect?)](https://alembic.sqlalchemy.org/en/latest/autogenerate.html#what-does-autogenerate-detect-and-what-does-it-not-detect) and always make sure to review the generated revision file before running it.

# Running migrations
```
alembic upgrade head
```
# Downgrading migrations
```
alembic downgrade -1
```

# Check your current alembic setup
```
alembic current
```

```

### File: integrations\langchain\README.md
```md
<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Skyvern Langchain](#skyvern-langchain)
  - [Installation](#installation)
  - [Basic Usage](#basic-usage)
    - [Run a task(sync) locally in your local environment](#run-a-tasksync-locally-in-your-local-environment)
    - [Run a task(async) locally in your local environment](#run-a-taskasync-locally-in-your-local-environment)
    - [Get a task locally in your local environment](#get-a-task-locally-in-your-local-environment)
    - [Run a task(sync) by calling skyvern APIs](#run-a-tasksync-by-calling-skyvern-apis)
    - [Run a task(async) by calling skyvern APIs](#run-a-taskasync-by-calling-skyvern-apis)
    - [Get a task by calling skyvern APIs](#get-a-task-by-calling-skyvern-apis)
  - [Agent Usage](#agent-usage)
    - [Run a task(async) locally in your local environment and wait until the task is finished](#run-a-taskasync-locally-in-your-local-environment-and-wait-until-the-task-is-finished)
    - [Run a task(async) by calling skyvern APIs and wait until the task is finished](#run-a-taskasync-by-calling-skyvern-apis-and-wait-until-the-task-is-finished)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Skyvern Langchain

This is a langchain integration for Skyvern.

## Installation

```bash
pip install skyvern-langchain
```

To run the example scenarios, you might need to install other langchain dependencies.
```bash
pip install langchain-openai
pip install langchain-community
```

## Basic Usage

This is the only basic usage of skyvern langchain tool. If you want a full langchain integration experience, please refer to the [Agent Usage](#agent-usage) section to play with langchain agent.

Go to [Langchain Tools](https://python.langchain.com/v0.1/docs/modules/tools/) to see more advanced langchain tool usage.


### Run a task(sync) locally in your local environment
> sync task won't return until the task is finished.

:warning: :warning: if you want to run this code block, you need to run `skyvern init` command in your terminal to set up skyvern first.


```python
import asyncio
from skyvern_langchain.agent import RunTask

run_task = RunTask()

async def main():
    # to run skyvern agent locally, must run `skyvern init` first
    print(await run_task.ainvoke("Navigate to the Hacker News homepage and get the top 3 posts."))


if __name__ == "__main__":
    asyncio.run(main())
```

### Run a task(async) locally in your local environment
> async task will return immediately and the task will be running in the background.

:warning: :warning: if you want to run the task in the background, you need to keep the script running until the task is finished, otherwise the task will be killed when the script is finished.

:warning: :warning: if you want to run this code block, you need to run `skyvern init` command in your terminal to set up skyvern first.

```python
import asyncio
from skyvern_langchain.agent import DispatchTask

dispatch_task = DispatchTask()

async def main():
    # to run skyvern agent locally, must run `skyvern init` first
    print(await dispatch_task.ainvoke("Navigate to the Hacker News homepage and get the top 3 posts."))

    # keep the script running until the task is finished
    await asyncio.sleep(600)


if __name__ == "__main__":
    asyncio.run(main())

```

### Get a task locally in your local environment

:warning: :warning: if you want to run this code block, you need to run `skyvern init` command in your terminal to set up skyvern first.

```python
import asyncio
from skyvern_langchain.agent import GetTask

get_task = GetTask()

async def main():
    # to run skyvern agent locally, must run `skyvern init` first
    print(await get_task.ainvoke("<task_id>"))


if __name__ == "__main__":
    asyncio.run(main())

```

### Run a task(sync) by calling skyvern APIs
> sync task won't return until the task is finished.

no need to run `skyvern init` command in your terminal to set up skyvern before using this integration.

```python
import asyncio
from skyvern_langchain.client import RunTask

run_task = RunTask(
    api_key="<your_organization_api_key>",
)
# or you can load the api_key from SKYVERN_API_KEY in .env
# run_task = RunTask()

async def main():
    print(await run_task.ainvoke("Navigate to the Hacker News homepage and get the top 3 posts."))


if __name__ == "__main__":
    asyncio.run(main())
```

### Run a task(async) by calling skyvern APIs
> async task will return immediately and the task will be running in the background.

no need to run `skyvern init` command in your terminal to set up skyvern before using this integration.

the task is actually running in the skyvern cloud service, so you don't need to keep your script running until the task is finished.

```python
import asyncio
from skyvern_langchain.client import DispatchTask

dispatch_task = DispatchTask(
    api_key="<your_organization_api_key>",
)
# or you can load the api_key from SKYVERN_API_KEY in .env
# dispatch_task = DispatchTask()

async def main():
    print(await dispatch_task.ainvoke("Navigate to the Hacker News homepage and get the top 3 posts."))


if __name__ == "__main__":
    asyncio.run(main())
```


### Get a task by calling skyvern APIs
> async task will return immediately and the task will be running in the background.

no need to run `skyvern init` command in your terminal to set up skyvern before using this integration.

the task is actually running in the skyvern cloud service, so you don't need to keep your script running until the task is finished.

```python
import asyncio
from skyvern_langchain.client import GetTask

get_task = GetTask(
    api_key="<your_organization_api_key>",
)
# or you can load the api_key from SKYVERN_API_KEY in .env
# get_task = GetTask()

async def main():
    print(await get_task.ainvoke("<task_id>"))


if __name__ == "__main__":
    asyncio.run(main())
```

## Agent Usage

Langchain is more powerful when used with [Langchain Agents](https://python.langchain.com/v0.1/docs/modules/agents/).

The following two examples show how to build an agent that executes a specified task, waits for its completion, and then returns the results. For example, the agent is tasked with navigating to the Hacker News homepage and retrieving the top three posts.


### Run a task(async) locally in your local environment and wait until the task is finished

> async task will return immediately and the task will be running in the background. You can use `GetTask` tool to poll the task information until the task is finished.

:warning: :warning: if you want to run this code block, you need to run `skyvern init` command in your terminal to set up skyvern first.

```python
import asyncio
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from skyvern_langchain.agent import DispatchTask, GetTask

from langchain_community.tools.sleep.tool import SleepTool

# load OpenAI API key from .env
load_dotenv()

llm = ChatOpenAI(model="gpt-4o", temperature=0)

dispatch_task = DispatchTask()
get_task = GetTask()

agent = initialize_agent(
    llm=llm,
    tools=[
        dispatch_task,
        get_task,
        SleepTool(),
    ],
    verbose=True,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
)


async def main():
    # use sleep tool to set up the polling logic until the task is completed, if you only want to dispatch a task, you can remove the sleep tool
    print(await agent.ainvoke("Run a task with Skyvern. The task is about 'Navigate to the Hacker News homepage and get the top 3 posts.' Then, get this task information until it's completed. The task information re-get interval should be 60s."))


if __name__ == "__main__":
    asyncio.run(main())

```

### Run a task(async) by calling skyvern APIs and wait until the task is finished

> async task will return immediately and the task will be running in the background. You can use `GetTask` tool to poll the task information until the task is finished.

no need to run `skyvern init` command in your terminal to set up skyvern before using this integration.

```python
import asyncio
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from skyvern_langchain.client import DispatchTask, GetTask

from langchain_community.tools.sleep.tool import SleepTool

# load OpenAI API key from .env
load_dotenv()

llm = ChatOpenAI(model="gpt-4o", temperature=0)

dispatch_task = DispatchTask(
    api_key="<your_organization_api_key>",
)
# or you can load the api_key from SKYVERN_API_KEY in .env
# dispatch_task = DispatchTask()

get_task = GetTask(
    api_key="<your_organization_api_key>",
)
# or you can load the api_key from SKYVERN_API_KEY in .env
# get_task = GetTask()

agent = initialize_agent(
    llm=llm,
    tools=[
        dispatch_task,
        get_task,
        SleepTool(),
    ],
    verbose=True,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
)


async def main():
    # use sleep tool to set up the polling logic until the task is completed, if you only want to dispatch a task, you can remove the sleep tool
    print(await agent.ainvoke("Run a task with Skyvern. The task is about 'Navigate to the Hacker News homepage and get the top 3 posts.' Then, get this task information until it's completed. The task information re-get interval should be 60s."))


if __name__ == "__main__":
    asyncio.run(main())
```
```

### File: integrations\mcp\README.md
```md
<!-- DOCTOC SKIP -->

<h1 align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="images/SkyvernMCP.png"/>
    <img src="images/SkyvernMCP.png" alt="Skyvern MCP Logo" width="75%"/>
  </picture>
</h1>

# Model Context Protocol (MCP)

Skyvern's MCP server implementation helps connect your AI Applications to the browser. This allows your AI applications to do things like: Fill out forms, download files, research information on the web, and more.

You can connect your MCP-enabled applications to Skyvern in two ways:
1. **Local Skyvern Server**
   - Use your favourite LLM to power Skyvern
2. **Skyvern Cloud**
   - Create an account at [app.skyvern.com](https://app.skyvern.com)
   - Get the API key from the settings page which will be used for setup

## Quickstart
> ⚠️ **REQUIREMENT**: Skyvern only runs in Python 3.11 environment today ⚠️

1. **Install Skyvern**
	```bash
	pip install skyvern
	```

2. **Configure Skyvern** Run the setup wizard which will guide you through the configuration process. You can connect to either [Skyvern Cloud](https://app.skyvern.com) or a local version of Skyvern. 
	```bash
	skyvern init
	```

3. **(Optional) Launch the Skyvern Server. Only required in local mode** 
	```bash
	skyvern run server
	```

## Examples
### Skyvern allows Claude to look up the top Hackernews posts today

https://github.com/user-attachments/assets/0c10dd96-c6ff-4b99-ad99-f34a5afd04fe

### Cursor looking up the top programming jobs in your area

https://github.com/user-attachments/assets/084c89c9-6229-4bac-adc9-6ad69b41327d

### Ask Windsurf to do a form 5500 search and download some files 

https://github.com/user-attachments/assets/70cfe310-24dc-431a-adde-e72691f198a7

## Supported Applications
`skyvern init` helps configure the following applications for you:
- Cursor
- Windsurf
- Claude Desktop
- Your custom MCP App?

Use the following config if you want to set up Skyvern for any other MCP-enabled application
```json
{
  "mcpServers": {
    "Skyvern": {
      "env": {
        "SKYVERN_BASE_URL": "https://api.skyvern.com", # "http://localhost:8000" if running locally
        "SKYVERN_API_KEY": "YOUR_SKYVERN_API_KEY" # find the local SKYVERN_API_KEY in the .env file after running `skyvern init` or in your Skyvern Cloud console
      },
      "command": "PATH_TO_PYTHON",
      "args": [
        "-m",
        "skyvern",
        "run",
        "mcp"
      ]
    }
  }
}
```

```

### File: tests\sdk\README.md
```md
# Skyvern SDK Tests

Test suite for Skyvern Python and TypeScript SDKs with shared HTML fixtures in `web/`.

## Python SDK

**Location:** `tests/sdk/python_sdk/`

### Prerequisites
- Requires `.env` with `SKYVERN_API_KEY`
- Browser fixture auto-launches on port 9222
- Web server fixture auto-starts on port 9010

### Running Tests

```bash
# Run all tests
pytest tests/sdk/python_sdk/

# Run specific test file
pytest tests/sdk/python_sdk/test_sdk_simple_actions.py

# Run specific test
pytest tests/sdk/python_sdk/test_sdk_simple_actions.py::test_clicks
```

---

## TypeScript SDK

**Location:** `tests/sdk/typescript_sdk/`

### Prerequisites
- Requires `.env` with `SKYVERN_API_KEY` — copy from the repo root: `cp .env tests/sdk/typescript_sdk/.env`
- Requires the Skyvern server running: `skyvern run server`
- Requires Chrome/Chromium with CDP on `localhost:9222` (see below)
- Web server auto-starts via `run-test.js`

**Launch Chromium with CDP:**
```bash
# Find your Playwright Chromium path
ls ~/Library/Caches/ms-playwright/

# Then launch it (adjust the chromium-XXXX version to match yours)
~/Library/Caches/ms-playwright/chromium-XXXX/chrome-mac/Chromium.app/Contents/MacOS/Chromium \
  --remote-debugging-port=9222 \
  --user-data-dir=~/tmp/chrome-playwright \
  about:blank
```

### Running Tests

```bash
cd tests/sdk/typescript_sdk

# First time setup
npm install

# Run specific test
npm test test_simple_actions.ts testClicks

# Run all tests in a file
npm test test_simple_actions.ts all
```

```

### File: .pre-commit-config.yaml
```yaml
default_language_version:
  python: python3
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v5.0.0
    hooks:
      - id: check-added-large-files
        args: ['--maxkb=15000']
        exclude: 'inputs.*|skyvern_demo_video\.mp4|demo_visualizer.mp4'
      - id: check-byte-order-marker
      - id: check-case-conflict
      - id: check-merge-conflict
      - id: check-symlinks
      - id: debug-statements
      - id: detect-private-key
  - repo: local
    hooks:
      - id: check-python-version
        name: Check Python Version (3.11-3.13)
        entry: uv run python -c "import sys; assert (3,11) <= sys.version_info[:2] <= (3,13), f'Python {sys.version_info[:2]} not supported. Use Python 3.11-3.13'"
        language: system
        pass_filenames: false
        always_run: true
  - repo: https://github.com/astral-sh/ruff-pre-commit
    # Ruff version.
    rev: v0.14.1
    hooks:
      # Run the linter.
      - id: ruff
        args: [--fix]
        exclude: |
          (?x)(
            ^skyvern/client/.*
          )
      # Run the formatter.
      - id: ruff-format
  - repo: https://github.com/pycqa/isort
    rev: 7.0.0
    hooks:
      - id: isort
        language_version: python3
        exclude: |
          (?x)(
            ^skyvern/client/.*|
            ^skyvern/__init__.py
          )
  - repo: https://github.com/pre-commit/pygrep-hooks
    rev: v1.10.0
    hooks:
      - id: python-check-blanket-noqa
      - id: python-check-mock-methods
      - id: python-no-log-warn
      - id: python-use-type-annotations
  - repo: https://github.com/asottile/pyupgrade
    rev: v3.21.0
    hooks:
      - id: pyupgrade
        exclude: |
          (?x)(
          ^skyvern/client/.*
          )
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.18.2
    hooks:
      - id: mypy
        args: [--show-error-codes, --warn-unused-configs, --disallow-untyped-calls, --disallow-untyped-defs, --disallow-incomplete-defs, --check-untyped-defs]
        additional_dependencies:
          - requests
          - types-requests
          - types-cachetools
          - alembic
          - 'sqlalchemy[mypy]'
          - types-PyYAML
          - types-toml
          - types-redis
          - types-aiofiles
        exclude: |
          (?x)(
            ^tests.*|
            ^streamlit_app.*|
            ^alembic.*|
            ^skyvern/client/.*
          )
  - repo: https://github.com/PyCQA/autoflake
    rev: v2.3.1
    hooks:
      - id: autoflake
        name: autoflake
        entry: autoflake --in-place --remove-all-unused-imports --recursive --ignore-init-module-imports
        language: python
        types: [python]
        exclude: |
          (?x)(
            ^skyvern/client/.*
          )
        # Mono repo has bronken this TODO: fix
        # - id: pytest-check
        #   name: pytest-check
        #   entry: pytest
        #   language: system
        #   pass_filenames: false
        #   always_run: true
  - repo: https://github.com/pre-commit/mirrors-prettier
    rev: 'v4.0.0-alpha.8' # Use the sha or tag you want to point at
    hooks:
      - id: prettier
        types: [javascript]
  - repo: local
    hooks:
      - id: frontend-precommit
        name: Frontend Precommit (lint-staged)
        entry: bash -c 'cd skyvern-frontend && npm run precommit'
        language: system
        files: ^skyvern-frontend/src/
        pass_filenames: false
      - id: vitest-type-check
        name: vitest
        entry: bash -c 'cd skyvern-frontend && ([ -d node_modules ] || npm ci) && npm run test'
        language: system
        pass_filenames: false
        files: ^skyvern-frontend/
      - id: alembic-check
        name: Alembic Check
        entry: ./run_alembic_check.sh
        language: script
        stages: [manual]
  - repo: https://github.com/shellcheck-py/shellcheck-py
    rev: v0.10.0.1
    hooks:
      - id: shellcheck
  - repo: https://github.com/google/yamlfmt
    rev: v0.17.2
    hooks:
      - id: yamlfmt

```

### File: AGENTS.md
```md
# Skyvern Agent Guide
This AGENTS.md file provides comprehensive guidance for AI agents working with the Skyvern codebase. Follow these guidelines to ensure consistency and quality in all contributions.

## Project Structure for Agent Navigation

- `/skyvern`: Main Python package
  - `/cli`: Command-line interface components
  - `/client`: Client implementations and integrations
  - `/forge`: Core automation logic and workflows
  - `/library`: Shared utilities and helpers
  - `/schemas`: Data models and validation schemas
  - `/services`: Business logic and service layers
  - `/utils`: Common utility functions
  - `/webeye`: Web interaction and browser automation
- `/skyvern-frontend`: Frontend application
- `/integrations`: Third-party service integrations
- `/alembic`: Database migrations
- `/scripts`: Utility and deployment scripts

## Coding Conventions for Agents

### Python Standards

- Use Python 3.11+ features and type hints
- Follow PEP 8 with a line length of 100 characters
- Use absolute imports for all modules
- Document all public functions and classes with Google-style docstrings
- Use `snake_case` for variables and functions, `PascalCase` for classes

### Asynchronous Programming

- Prefer async/await over callbacks
- Use `asyncio` for concurrency
- Always handle exceptions in async code
- Use context managers for resource cleanup

### Error Handling

- Use specific exception classes
- Include meaningful error messages
- Log errors with appropriate severity levels
- Never expose sensitive information in error messages

## Pull Request Process

1. **Branch Naming**
   - `feature/descriptive-name` for new features
   - `fix/issue-description` for bug fixes
   - `chore/task-description` for maintenance tasks

2. **PR Guidelines**
   - Reference related issues with `Fixes #123` or `Closes #123`
   - Include a clear description of changes
   - Update relevant documentation
   - Ensure all tests pass
   - Get at least one approval before merging

3. **Commit Message Format**
   ```
   [Component] Action: Brief description
   
   More detailed explanation if needed.
   
   - Bullet points for additional context
   - Reference issues with #123
   ```

## Code Quality Checks

Before submitting code, run:
```bash
pre-commit run --all-files
```

## Performance Considerations
- Optimize database queries
- Use appropriate data structures
- Implement caching where beneficial
- Monitor memory usage

## Security Best Practices
- Never commit secrets or credentials
- Validate all inputs
- Use environment variables for configuration
- Follow the principle of least privilege
- Keep dependencies updated

## Getting Help
- Check existing issues before opening new ones
- Reference relevant documentation
- Provide reproduction steps for bugs
- Be specific about the problem and expected behavior

```

### File: CLAUDE.md
```md
# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

### Python Backend Commands
- **Install dependencies**: `uv sync`
- **Run Skyvern service**: `skyvern run all` (starts both backend and UI)
- **Run backend only**: `skyvern run server`
- **Run UI only**: `skyvern run ui`
- **Check status**: `skyvern status`
- **Stop services**: `skyvern stop all`
- **Quickstart**: `skyvern quickstart` (for first-time setup with DB migrations)

### Code Quality & Testing
- **Lint**: `ruff check` and `ruff format`
- **Type checking**: `mypy skyvern`
- **Run tests**: `pytest tests/`
- **Pre-commit hooks**: `pre-commit run --all-files`

### Frontend Commands (in skyvern-frontend/)
- **Install dependencies**: `npm install`
- **Development**: `npm run dev`
- **Build**: `npm run build`
- **Lint**: `npm run lint`
- **Format**: `npm run format`

### Database Management
- **Run migrations**: `alembic upgrade head`
- **Create migration**: `alembic revision --autogenerate -m "description"`

## Architecture Overview

Skyvern is a browser automation platform that uses LLMs and computer vision to interact with websites. The architecture consists of:

### Core Components
- **Agent System** (`skyvern/agent/`): Multi-agent system for web navigation and task execution
- **Browser Engine** (`skyvern/webeye/`): Playwright-based browser automation with computer vision
- **Workflow Engine** (`skyvern/services/`): Orchestrates complex multi-step workflows
- **API Layer** (`skyvern/forge/`): FastAPI-based REST API and WebSocket support

### Key Directories
- `skyvern/agent/`: LLM-powered agents for web interaction
- `skyvern/webeye/`: Browser automation, DOM scraping, action execution
- `skyvern/forge/`: FastAPI server, API endpoints, request handling
- `skyvern/services/`: Business logic for tasks, workflows, and browser sessions
- `skyvern/cli/`: Command-line interface
- `skyvern/client/`: Generated Python client SDK
- `skyvern-frontend/`: React-based UI for task management and monitoring
- `alembic/`: Database migrations

### Workflow System
- **Blocks**: Modular components (navigation, extraction, validation, loops, etc.)
- **Parameters**: Dynamic values passed between blocks
- **Runs**: Execution instances of workflows
- **Browser Sessions**: Persistent browser state across workflow steps

### Data Flow
1. User creates tasks/workflows via UI or API
2. Agent system plans actions using LLM analysis of screenshots
3. Browser engine executes actions via Playwright
4. Results are captured, processed, and stored
5. Workflow orchestrator manages multi-step sequences

## Development Notes

### Environment Setup
- Requires Python 3.11+ and Node.js
- Uses UV for Python dependency management
- PostgreSQL database (managed via Docker or local install)
- Browser dependencies installed via Playwright

### LLM Configuration
Configure via environment variables or `skyvern init llm`:
- Supports OpenAI, Anthropic, Azure OpenAI, AWS Bedrock, Gemini, Ollama
- Uses `LLM_KEY` to specify which model to use
- `SECONDARY_LLM_KEY` for lightweight agent operations

### Testing Strategy
- Unit tests in `tests/unit_tests/`
- Integration tests require browser automation setup
- Use `pytest` with async support for testing

### Code Style
- Python: Ruff for linting and formatting (configured in pyproject.toml)
- TypeScript: ESLint + Prettier (configured in skyvern-frontend/)
- Line length: 120 characters
- Use type hints and async/await patterns
```

### File: CODE_OF_CONDUCT.md
```md
<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Code of Conduct - Skyvern](#code-of-conduct---skyvern)
  - [Our Pledge](#our-pledge)
  - [Our Standards](#our-standards)
  - [Our Responsibilities](#our-responsibilities)
  - [Scope](#scope)
  - [Enforcement](#enforcement)
  - [Enforcement Guidelines](#enforcement-guidelines)
    - [1. Correction](#1-correction)
    - [2. Warning](#2-warning)
    - [3. Temporary Ban](#3-temporary-ban)
    - [4. Permanent Ban](#4-permanent-ban)
  - [Attribution](#attribution)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Code of Conduct - Skyvern

## Our Pledge

In the interest of fostering an open and welcoming environment, we as
contributors and maintainers pledge to make participation in our project and
our community a harassment-free experience for everyone, regardless of age, body
size, disability, ethnicity, sex characteristics, gender identity and expression,
level of experience, education, socio-economic status, nationality, personal
appearance, race, religion, or sexual identity and orientation.

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
  advances
* Trolling, insulting or derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or email
  address, without their explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting

## Our Responsibilities

Project maintainers are responsible for clarifying and enforcing our standards of
acceptable behavior and will take appropriate and fair corrective action in
response to any behavior that they deem inappropriate,
threatening, offensive, or harmful.

Project maintainers have the right and responsibility to remove, edit, or reject
comments, commits, code, wiki edits, issues, and other contributions that are
not aligned to this Code of Conduct, and will
communicate reasons for moderation decisions when appropriate.

## Scope

This Code of Conduct applies within all community spaces, and also applies when
an individual is officially representing the community in public spaces.
Examples of representing our community include using an official e-mail address,
posting via an official social media account, or acting as an appointed
representative at an online or offline event.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported to the community leaders responsible for enforcement at <enforcement@skyvern.com>.
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

This Code of Conduct is adapted from the [Contributor Covenant](https://contributor-covenant.org/), version
[1.4](https://www.contributor-covenant.org/version/1/4/code-of-conduct/code_of_conduct.md) and
[2.0](https://www.contributor-covenant.org/version/2/0/code_of_conduct/code_of_conduct.md),
and was generated by [contributing-gen](https://github.com/bttger/contributing-gen).
```

### File: CONTRIBUTING.md
```md
<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Contributing to Skyvern](#contributing-to-skyvern)
  - [Table of Contents](#table-of-contents)
  - [Code of Conduct](#code-of-conduct)
  - [I Have a Question](#i-have-a-question)
  - [I Want To Contribute](#i-want-to-contribute)
    - [Reporting Bugs](#reporting-bugs)
      - [Before Submitting a Bug Report](#before-submitting-a-bug-report)
      - [How Do I Submit a Good Bug Report?](#how-do-i-submit-a-good-bug-report)
    - [Suggesting Enhancements](#suggesting-enhancements)
      - [Before Submitting an Enhancement](#before-submitting-an-enhancement)
      - [How Do I Submit a Good Enhancement Suggestion?](#how-do-i-submit-a-good-enhancement-suggestion)
    - [Your First Code Contribution](#your-first-code-contribution)
    - [Improving The Documentation](#improving-the-documentation)
  - [Styleguides](#styleguides)
    - [Pre Commit Hooks](#pre-commit-hooks)
    - [Commit Messages](#commit-messages)
  - [Join The Project Team](#join-the-project-team)
  - [Attribution](#attribution)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

<!-- omit in toc -->
# Contributing to Skyvern

First off, thanks for taking the time to contribute! ❤️

All types of contributions are encouraged and valued. See the [Table of Contents](#table-of-contents) for different ways to help and details about how this project handles them. Please make sure to read the relevant section before making your contribution. It will make it a lot easier for us maintainers and smooth out the experience for all involved. The community looks forward to your contributions. 🎉

> And if you like the project, but just don't have time to contribute, that's fine. There are other easy ways to support the project and show your appreciation, which we would also be very happy about:
> - Star the project
> - Tweet about it
> - Refer this project in your project's readme
> - Mention the project at local meetups and tell your friends/colleagues

<!-- omit in toc -->
## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [I Have a Question](#i-have-a-question)
- [I Want To Contribute](#i-want-to-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Enhancements](#suggesting-enhancements)
  - [Your First Code Contribution](#your-first-code-contribution)
  - [Improving The Documentation](#improving-the-documentation)
- [Styleguides](#styleguides)
  - [Commit Messages](#commit-messages)
- [Join The Project Team](#join-the-project-team)


## Code of Conduct

This project and everyone participating in it is governed by the
[Skyvern Code of Conduct](https://github.com/Skyvern-AI/skyvern-agentblob/master/CODE_OF_CONDUCT.md).
By participating, you are expected to uphold this code. Please report unacceptable behavior
to <enforcement@skyvern.com>.


## I Have a Question

> If you want to ask a question, we assume that you have read the available [Documentation](www.skyvern.com/docs).

Before you ask a question, it is best to search for existing [Issues](https://github.com/Skyvern-AI/skyvern-agent/issues) that might help you. In case you have found a suitable issue and still need clarification, you can write your question in this issue. It is also advisable to search the internet for answers first.

If you then still feel the need to ask a question and need clarification, we recommend the following:

- Open an [Issue](https://github.com/Skyvern-AI/skyvern-agent/issues/new).
- Provide as much context as you can about what you're running into.
- Provide project and platform versions (nodejs, npm, etc), depending on what seems relevant.

We will then take care of the issue as soon as possible.

<!--
You might want to create a separate issue tag for questions and include it in this description. People should then tag their issues accordingly.

Depending on how large the project is, you may want to outsource the questioning, e.g. to Stack Overflow or Gitter. You may add additional contact and information possibilities:
- IRC
- Slack
- Gitter
- Stack Overflow tag
- Blog
- FAQ
- Roadmap
- E-Mail List
- Forum
-->

## I Want To Contribute

> ### Legal Notice <!-- omit in toc -->
> When contributing to this project, you must agree that you have authored 100% of the content, that you have the necessary rights to the content and that the content you contribute may be provided under the project license.

### Reporting Bugs

<!-- omit in toc -->
#### Before Submitting a Bug Report

A good bug report shouldn't leave others needing to chase you up for more information. Therefore, we ask you to investigate carefully, collect information and describe the issue in detail in your report. Please complete the following steps in advance to help us fix any potential bug as fast as possible.

- Make sure that you are using the latest version.
- Determine if your bug is really a bug and not an error on your side e.g. using incompatible environment components/versions (Make sure that you have read the [documentation](www.skyvern.com/docs). If you are looking for support, you might want to check [this section](#i-have-a-question)).
- To see if other users have experienced (and potentially already solved) the same issue you are having, check if there is not already a bug report existing for your bug or error in the [bug tracker](https://github.com/Skyvern-AI/skyvern-agentissues?q=label%3Abug).
- Also make sure to search the internet (including Stack Overflow) to see if users outside of the GitHub community have discussed the issue.
- Collect information about the bug:
  - Stack trace (Traceback)
  - OS, Platform and Version (Windows, Linux, macOS, x86, ARM)
  - Version of the interpreter, compiler, SDK, runtime environment, package manager, depending on what seems relevant.
  - Possibly your input and the output
  - Can you reliably reproduce the issue? And can you also reproduce it with older versions?

<!-- omit in toc -->
#### How Do I Submit a Good Bug Report?

> You must never report security related issues, vulnerabilities or bugs including sensitive information to the issue tracker, or elsewhere in public. Instead sensitive bugs must be sent by email to <security@skyvern.com>.
<!-- You may add a PGP key to allow the messages to be sent encrypted as well. -->

We use GitHub issues to track bugs and errors. If you run into an issue with the project:

- Open an [Issue](https://github.com/Skyvern-AI/skyvern-agent/issues/new). (Since we can't be sure at this point whether it is a bug or not, we ask you not to talk about a bug yet and not to label the issue.)
- Explain the behavior you would expect and the actual behavior.
- Please provide as much context as possible and describe the *reproduction steps* that someone else can follow to recreate the issue on their own. This usually includes your code. For good bug reports you should isolate the problem and create a reduced test case.
- Provide the information you collected in the previous section.

Once it's filed:

- The project team will label the issue accordingly.
- A team member will try to reproduce the issue with your provided steps. If there are no reproduction steps or no obvious way to reproduce the issue, the team will ask you for those steps and mark the issue as `needs-repro`. Bugs with the `needs-repro` tag will not be addressed until they are reproduced.
- If the team is able to reproduce the issue, it will be marked `needs-fix`, as well as possibly other tags (such as `critical`), and the issue will be left to be [implemented by someone](#your-first-code-contribution).

<!-- You might want to create an issue template for bugs and errors that can be used as a guide and that defines the structure of the information to be included. If you do so, reference it here in the description. -->


### Suggesting Enhancements

This section guides you through submitting an enhancement suggestion for Skyvern, **including completely new features and minor improvements to existing functionality**. Following these guidelines will help maintainers and the community to understand your suggestion and find related suggestions.

<!-- omit in toc -->
#### Before Submitting an Enhancement

- Make sure that you are using the latest version.
- Read the [documentation](www.skyvern.com/docs) carefully and find out if the functionality is already covered, maybe by an individual configuration.
- Perform a [search](https://github.com/Skyvern-AI/skyvern-agent/issues) to see if the enhancement has already been suggested. If it has, add a comment to the existing issue instead of opening a new one.
- Find out whether your idea fits with the scope and aims of the project. It's up to you to make a strong case to convince the project's developers of the merits of this feature. Keep in mind that we want features that will be useful to the majority of our users and not just a small subset. If you're just targeting a minority of users, consider writing an add-on/plugin library.

<!-- omit in toc -->
#### How Do I Submit a Good Enhancement Suggestion?

Enhancement suggestions are tracked as [GitHub issues](https://github.com/Skyvern-AI/skyvern-agent/issues).

- Use a **clear and descriptive title** for the issue to identify the suggestion.
- Provide a **step-by-step description of the suggested enhancement** in as many details as possible.
- **Describe the current behavior** and **explain which behavior you expected to see instead** and why. At this point you can also tell which alternatives do not work for you.
- You may want to **include screenshots and animated GIFs** which help you demonstrate the steps or point out the part which the suggestion is related to. You can use [this tool](https://www.cockos.com/licecap/) to record GIFs on macOS and Windows, and [this tool](https://github.com/colinkeenan/silentcast) or [this tool](https://github.com/GNOME/byzanz) on Linux. <!-- this should only be included if the project has a GUI -->
- **Explain why this enhancement would be useful** to most Skyvern users. You may also want to point out the other projects that solved it better and which could serve as inspiration.

<!-- You might want to create an issue template for enhancement suggestions that can be used as a guide and that defines the structure of the information to be included. If you do so, reference it here in the description. -->

### Your First Code Contribution
<!-- TODO
include Setup of env, IDE and typical getting started instructions?

-->

### Improving The Documentation
<!-- TODO
Updating, improving and correcting the documentation

-->

## Styleguides

### Pre Commit Hooks
Make sure to install and run the pre-commit hooks before committing your code.
This will help you to automatically format your code and catch CI/CD failures early.
```bash
# Make sure `pre-commit` is installed
pip install pre-commit

# Install the git hook scripts (one-time setup)
pre-commit install

# (Optional) Run pre-commit hooks manually on all files
pre-commit run --all-files
```

Once installed, the hooks will run automatically on `git commit`.

### Commit Messages
<!-- TODO

-->

## Join The Project Team
<!-- TODO -->

<!-- omit in toc -->
## Attribution
This guide is based on the **contributing-gen**. [Make your own](https://github.com/bttger/contributing-gen)!

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
