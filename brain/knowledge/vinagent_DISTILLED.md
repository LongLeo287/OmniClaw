---
id: vinagent
type: knowledge
owner: OA_Triage
---
# vinagent
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "dependencies": {
    "next": "^15.3.4",
    "nextra": "^4.2.17",
    "nextra-theme-docs": "^4.2.17",
    "react": "^19.1.0",
    "react-dom": "^19.1.0"
  }
}

```

### File: README.md
```md
<p align="center">
  <img src="asset/vinagent.png" alt="Vinagent Logo" width="300px" />
</p>

[![Version](https://img.shields.io/pypi/v/vinagent.svg)](https://pypi.org/project/vinagent/)
[![PyPI Downloads](https://static.pepy.tech/badge/vinagent/week)](https://pepy.tech/projects/vinagent)
[![Downloads](https://static.pepy.tech/badge/vinagent/month)](https://pepy.tech/project/vinagent)
[![PyPI Downloads](https://static.pepy.tech/badge/vinagent)](https://pepy.tech/projects/vinagent)
[![Reddit r/vinagent](https://img.shields.io/badge/Reddit-r%2Fvinagent-orange?logo=reddit&logoColor=white)](https://www.reddit.com/r/vinagent/)
[![Discord](https://img.shields.io/badge/Chat-Discord-5865F2?logo=discord&logoColor=white)](https://discord.com/channels/1036147288994758717/1358017320970358864)
![License](https://img.shields.io/github/license/datascienceworld-kan/vinagent)

# 1. Introduction

`vinagent` is a lightweight and flexible library designed for building smart agent assistants across various industries. Whether you're creating an AI-powered customer service bot, a data analysis assistant, or a domain-specific automation agent, vinagent provides a simple yet powerful foundation.

With its modular tool system, you can easily extend your agent's capabilities by integrating a wide range of tools. Each tool is self-contained, well-documented, and can be registered dynamically—making it effortless to scale and adapt your agent to new tasks or environments.

![](asset/agent_system_design_v2.png)


# 2. Version

* Date 25-03-2026: [Version 0.0.9](https://github.com/datascienceworld-kan/vinagent/releases/tag/v0.0.9) target at Autonomous Multi-Agent features:
    - You can add multiple agents as a unique Team.
    - Autonomously planning tasks for agents in the team.
    - Triggering agents to execute tasks according to plan.
    - Aggregating results from all agents.

* Date 12-03-2026: [Version 0.0.7](https://github.com/datascienceworld-kan/vinagent/releases/tag/v0.0.7) is a big upgrade with many new features:
    - Refactor code to decouple Agent class's invoking logic into multiple executors: InvokeExecutor, AsyncInvokeExecutor, - StreamInvokeExecutor, AsyncStreamInvokeExecutor, GraphExecutor.
    - Guardrail System for input, output, and tools
    - Integrate any [Agentskill Anthropic](https://agentskills.io/home) Template as a tool type `agentskill`.
    - LLM with structured AgentResponse.
    - Logic for asynchronous streaming.

* Date 13-09-2025: [Version 0.0.6](https://github.com/datascienceworld-kan/vinagent/releases/tag/v0.0.7) have many new advanced features:
    - Multi-Agent system support: Agents can communicate in static workflow.
    - Knowledge Graph Agent Memory: Transform conversation history into knowledge graph.
    - MCP server support: Agent can connect to MCP server as a tool type `mcp`.

# 3. Installation
To install and use this library please following:

```
git@github.com:datascienceworld-kan/vinagent.git
cd vinagent
pip install -r requirements.txt
poetry install
```

Or you can install by pip command

```
pip install vinagent
```

To use a list of default tools inside [vinagent.tools](vinagent/tools/) you should set environment varibles inside `.env` including `TOGETHER_API_KEY` to use llm models at [togetherai](https://api.together.ai/signin) site and `TAVILY_API_KEY` to use tavily websearch tool at [tavily](https://app.tavily.com/home) site:

```
TOGETHER_API_KEY="Your together API key"
TAVILY_API_KEY="Your Tavily API key"
OPENAI_API_KEY="Your OpenAI API key"
```
Let's create your acounts first and then create your relevant key for each website.


# 4. Set up Agent

`vinagent` is a flexible library for creating intelligent agents. You can configure your agent with tools, each encapsulated in a Python module under `vinagent.tools`. This provides a workspace of tools that agents can use to interact with and operate in the realistic world. Each tool is a Python file with full documentation and it can be independently ran. For example, the [vinagent.tools.websearch_tools](vinagent/tools/websearch_tools.py) module contains code for interacting with a search API.


```python
from langchain_together import ChatTogether 
from langchain_openai import ChatOpenAI
from vinagent.agent.agent import Agent
from dotenv import load_dotenv
load_dotenv()

# You can use togetherai model
llm = ChatTogether(
    model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free"
)

# Or you can you OpenAI model
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7
)


# Step 1: Create Agent with tools
agent = Agent(
    description="You are a Financial Analyst",
    llm = llm,
    skills = [
        "Deeply analyzing financial markets", 
        "Searching information about stock price",
        "Visualization about stock price"],
    tools = ['vinagent.tools.websearch_tools',
             'vinagent.tools.yfinance_tools'],
    tools_path = 'templates/tools.json', # Place to save tools. Default is 'templates/tools.json'
    is_reset_tools = True # If True, it will reset tools every time reinitializing an agent. Default is False
)

# Step 2: invoke the agent
message = agent.invoke("Who you are?")
```

If the answer is a normal message without using any tools, it will be an `AIMessage`. By contrast, it will have `ToolMessage` type. For examples:

```
message
```
```
AIMessage(content='I am a Financial Analyst.', additional_kwargs={'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 7, 'prompt_tokens': 308, 'total_tokens': 315, 'completion_tokens_details': None, 'prompt_tokens_details': None, 'cached_tokens': 0}, 'model_name': 'meta-llama/Llama-3.3-70B-Instruct-Turbo-Free', 'system_fingerprint': None, 'finish_reason': 'stop', 'logprobs': None}, id='run-070f7431-7176-42a8-ab47-ed83657c9463-0', usage_metadata={'input_tokens': 308, 'output_tokens': 7, 'total_tokens': 315, 'input_token_details': {}, 'output_token_details': {}})
```
Access to `content` property to get the string content.

```
message.content
```
```
I am a Financial Analyst.
```

The following function need to use yfinancial tool, therefore the return value will be `ToolMessage` with the a stored pandas.DataFrame in `artifact` property.

```
df = agent.invoke("What is the price of Tesla stock in 2024?")
df
```
```
ToolMessage(content="Completed executing tool fetch_stock_data({'symbol': 'TSLA', 'start_date': '2024-01-01', 'end_date': '2024-12-31', 'interval': '1d'})", tool_call_id='tool_cde0b895-260a-468f-ac01-7efdde19ccb7', artifact=pandas.DataFrame)
```

To access `pandas.DataFrame` value:

```
df.artifact.head()
```

![png](asset/table.png)

Another example, if you visualize a stock price using a tool, the output message is a `ToolMessage` with the saved `artifact` is a plotly plot.

```
# return a ToolMessage which we can access to plot by plot.artifact and content by plot.content.
plot = agent.invoke("Let's visualize Tesla stock in 2024?")
```

![png](asset/test_4_1.png)
    

```
# return a ToolMessage which we can access to plot by plot.artifact and content by plot.content.
plot = agent.invoke("Let's visualize the return of Tesla stock in 2024?")
```
  
![png](asset/return_plot.png)
    

# 5. Register Tool

Vinagent stands out for its flexibility in registering different types of tools, including:

- Function tools: These are integrated directly into your runtime code using the @function_tool decorator, without the need to store them in separate Python module files.
- Module tools: These are added via Python module files placed in the vinagent.tools directory. Once registered, the modules can be imported and used in your runtime environment.
- MCP tools: These are tools registered through an [MCP (Model Context Protocol) server](https://github.com/modelcontextprotocol/servers), enabling external tool integration.

## 5.1. Function Tool

You can customize any function in your runtime code as a powerful tool by using the `@agent.tools_manager.register_function_tool` decorator.

```python
from typing import List

@agent.tools_manager.register_function_tool # Note: agent must be initialized first
def sum_of_series(x: List[float]):
    return f"Sum of list is {sum(x)}"
```
```
INFO:root:Registered tool: sum_of_series (runtime)
```

```python
message = agent.invoke("Sum of this list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]?")
message
```
```
ToolMessage(content="Completed executing tool sum_of_series({'x': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})", tool_call_id='tool_56f40902-33dc-45c6-83a7-27a96589d528', artifact='Sum of list is 55')
```

## 5.2. Module Tool
Many complex tools cannot be implemented within a single function. In such cases, organizing the tool as a python module becomes necessary. To support this, `vinagent` allows tools to be registered via python module files placed in the `vinagent.tools` directory. This approach makes it easier to manage and execute more sophisticated tasks. Once registered, these modules can be imported and used directly in the runtime environment.

```
from langchain_together import ChatTogether 
from vinagent.agent.agent import Agent
from dotenv import load_dotenv
load_dotenv()

llm = ChatTogether(
    model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free"
)

agent = Agent(
    description="You are a Web Search Expert",
    llm = llm,
    skills = [
        "Search the information from internet", 
        "Give an in-deepth report",
        "Keep update with the latest news"
    ],
    tools = ['vinagent.tools.websearch_tools'],
    tools_path = 'templates/tools.json' # Place to save tools. The default path is also 'templates/tools.json',
    is_reset_tools = True # If True, will reset tools every time. Default is False
)
```

## 5.3. MCP Tool

MCP (model context protocal) is a new AI protocal offfered by Anthropic that allows any AI model to interact with any tools distributed acrooss different platforms. These tools are provided by platform's [MCP Server](https://github.com/modelcontextprotocol/servers). There are many MCP servers available out there such as `google drive, gmail, slack, notions, spotify, etc.`, and `vinagent` can be used to connect to these servers and execute the tools within the agent.

You need to start a MCP server first. For example, start with [math MCP Server](vinagent/mcp/examples/math/README.md)

```
cd vinagent/mcp/examples/math
mcp dev main.py
```
```
⚙️ Proxy server listening on port 6277
🔍 MCP Inspector is up and running at http://127.0.0.1:6274 🚀
```

Next, you need to register the MCP server in the agent. You can do this by adding the server's URL to the `tools` list of the agent's configuration.

```
from vinagent.mcp.client import DistributedMCPClient
from vinagent.mcp import load_mcp_tools
from vinagent.agent.agent import Agent
from langchain_together import ChatTogether
from dotenv import load_dotenv

load_dotenv()

# Step 1: Initialize LLM
llm = ChatTogether(
    model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free"
)

# Step 2: Initialize MCP client for Distributed MCP Server
client = DistributedMCPClient(
            {
                "math": {
                    "command": "python",
                    # Make sure to update to the full absolute path to your math_server.py file
                    "args": ["vinagent/mcp/examples/math/main.py"],
                    "transport": "stdio",
                }
             }
        )
server_name = "math"

# Step 3: Initialize Agent
agent = Agent(
    description="You are a Trending News Analyst",
    llm = llm,
    skills = [
        "You are Financial Analyst",
        "Deeply analyzing financial news"],
    tools = ['vinagent.tools.yfinance_tools'],
    tools_path="templates/tools.json",
    is_reset_tools=True,
    mcp_client=client, # MCP Client
    mcp_server_name=server_name, # MCP Server name to resgister. If not set, all tools from all MCP servers available
)

# Step 4: Register mcp_tools to agent
mcp_tools = await agent.connect_mcp_tool()
```

```
# Test sum
agent.invoke("What is the sum of 1993 and 709?")
```

```
# Test product
agent.invoke("Let's multiply of 1993 and 709?")
```

# 6. Invoke and streaming

## 6.1. Synchronous and Asynchronous Invocation
Vinagent offers both synchronous (agent.invoke) and asynchronous (agent.ainvoke) invocation methods. While synchronous calls halt the main thread until a response is returned, asynchronous calls enable the main thread to proceed without waiting. In practice, asynchronous invocations can be up to twice as fast as synchronous ones.

```
# Synchronous invocation
message = agent.invoke("What is the sum of 1993 and 709?")
```

```
# Asynchronous invocation
message = await agent.ainvoke("What is the sum of 1993 and 709?")
```

## 6.2. Streaming Invocation
In addition to synchronous and asynchronous invocation, vinagent also supports streaming invocation. This means that the response is generated in real-time on token-by-token basis, allowing for a more interactive and responsive experience. To use streaming, simply use `agent.stream`:

```
for chunk in agent.stream("Where is the capital of the Vietnam?"):
    print(chunk)
```

## 6.3. Async Streaming Invocation
Vinagent offer an `astream` method that is async version of `stream` to accelerate the speed of response. It is particularly useful for I/O bound tasks that needs waiting for data from external sources.

```
import asyncio
async def run_agent():
    content = ""

    async for chunk in agent.astream(query="Where is the capital of the Vietnam?"):
        content += chunk.content or ""
        print(chunk.content, end="", flush=True)

    print("\nFinal content:", content)

asyncio.run(run_agent())
```

# 7. Advance Features

## 7.1. Deep Search

With vinagent, you can invent a complex workflow by combining multiple tools into a single agent. This allows you to create a more sophisticated and flexible agent that can adapt to different task. Let's see how an agent can be created to help with financial analysis by using `deepsearch` tool, which allows you to search for information in a structured manner. This tool is particularly useful for tasks that require a deep understanding of the data and the ability to navigate through complex information.

```
from langchain_together import ChatTogether 
from vinagent.agent import Agent
from dotenv import load_dotenv
load_dotenv()

llm = ChatTogether(
    model="meta-llama/Llama-3.3-70B-Instruct-Turbo-Free"
)

agent = Agent(
    description="You are a Financial Analyst",
    llm = llm,
    skills = [
        "Deeply analyzing financial markets", 
        "Searching information about stock price",
        "Visualization about stock price"],
    tools = ['vinagent.tools.deepsearch']
)

message = agent.invoke("Let's analyze Tesla stock in 2025?")
print(message.artifact)
```

[![Watch the video](https://img.youtube.com/vi/MUOg7MYGUzE/0.jpg)](https://youtu.be/MUOg7MYGUzE)

The output is available at [vinagent/examples/deepsearch.md](vinagent/examples/deepsearch.md)

## 7.2. Trending Search


... [TRUNCATED]
```

### File: requirements.txt
```txt
langchain-core==0.3.41
langchain-openai==0.3.7
langchain-together==0.3.0
python-dotenv==1.0.0
tavily-python==0.3.1
yfinance==0.2.54
pandas==2.2.3
matplotlib==3.7.1
plotly==5.22.0
googlenewsdecoder==0.1.7
vnstock3==3.2.1

```

### File: docs\README.md
```md
# Vinagent Document

With the target "make the AI community better by inventing AI libraries", I share how [vinagent site](https://datascienceworld-kan.github.io/vinagent) is created with you. I wish that more-and-more useful libraries will be invented from community with a careful and detailed documents.

## Install dependencies
To deploy on your local website on your computer, you need to install mkdoc library first.

```
pip install mkdocs==1.6.1
# Check version
mkdocs --version
```

## Structuring website
Then, structuring your site at `mkdocs.yml` template. For instance, I want to create a header bar including four tabs: `Get started, Guidlines, Reference, Contributing` with their relevant sub sections on the left side. Let's configure `mkdocs.yml` as following:

```
nav:
  - Get started: 
    - index.md
    - Quick Start:
      - Start with basic Agent: get_started/basic_agent.md
      - Build a customization: 
        - 1. Add tools: get_started/add_tool.md
        - 2. Add memory: get_started/add_memory.md
        - 3. Async Invoking: get_started/async_invoke.md
        - - 4. Streaming & Async Streaming: get_started/streaming.md
        - 5. Prebuilt Agent: get_started/react_agent.md
        - 6. Security: get_started/authen_layer.md
        - 7. Observability: get_started/observability.md
      - Run local ReactJS App: get_started/local_run.md
    - Agent Development:
      - Workflow & Agent: get_started/workflow_and_agent.md
      - Agent RAG: get_started/agent_rag.md
    - Multi-Agent Development: 
      - Start with basic Multi-Agent: get_started/multi_agent.md

  - Guidelines: 
    - Financial Usercase:
      - Visualize and Analyze Stock: guides/analyze_stock_trending.md
      - Find Trending New: guides/trending_news.md
    - Banking Agent:
      - Banking SQL: guides/banking_agent.md
    - Research Usercase:
      - Research Agent: guides/paper_research.md
    - Legal Field:
      - Legal Agent: guides/legal_assistant.md
    - Ecommerce Usercase:
      - Customer Care Multi-Agent: guides/customer_care.md
    - RAG:
      - Agent RAG: guides/agent_rag.md
    
  - Reference: 
    - Agent: reference/agent.md
    - Tool: reference/tool.md
    - Memory: reference/memory.md
    - Graph: reference/graph.md
    - MCP: reference/mcp.md
    - Tracing: reference/tracing.md
    - Authenticate: reference/authenticate.md

  - Contributing:
    - How to Contribute: contributing/contributing.md
```

You can add new blogs into  `mkdocs.yml`. 

## Rendering website on local
To test your website rendering on local, let's deploy it as following:

```
mkdocs --serve
```


    INFO    -  Documentation built in 3.15 seconds
    INFO    -  [10:36:51] Watching paths for changes: 'docs', 'mkdocs.yml'
    INFO    -  [10:36:51] Serving on http://127.0.0.1:8000/vinagent/


You can access a new website at `http://127.0.0.1:8000/vinagent`


## Deploy on website
A github action [CI/CD deployment](https://github.com/datascienceworld-kan/vinagent/blob/main/.github/workflows/ci_docs.yaml) pipeline takes responsibility to track new changing in `docs` folder and proceeds auto deployment.

```

### File: .pre-commit-config.yaml
```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 25.9.0
    hooks:
      - id: black

```

### File: .readthedocs.yaml
```yaml
# .readthedocs.yaml
version: 2

build:
  os: ubuntu-22.04
  tools:
    python: "3.10"

python:
  install:
    - method: pip
      path: .
    - requirements: docs/requirements.txt

sphinx:
  configuration: docs/source/conf.py

```

### File: CONTRIBUTING.md
```md
# Contributing to Vinagent

First off, thanks for taking the time to contribute!

All types of contributions are encouraged and valued. See the [Table of Contents](#table-of-contents)
for different ways to help and details about how this project handles them. Please make sure to read
the relevant section before making your contribution. It will make it a lot easier for us maintainers
and smooth out the experience for all involved. The community looks forward to your contributions.

> And if you like the project, but just don't have time to contribute, that's fine. There are other easy
> ways to support the project and show your appreciation, which we would also be very happy about:
> - Star the project
> - Tweet about it
> - Refer this project in your project's readme
> - Mention the project at local meetups and tell your friends/colleagues

<!-- omit in toc -->
## Table of Contents

- [I Have a Question](#i-have-a-question)
- [I Want To Contribute](#i-want-to-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Enhancements](#suggesting-enhancements)
  - [Your First Code Contribution](#your-first-code-contribution)
  - [Improving The Documentation](#improving-the-documentation)
- [Styleguides](#styleguides)
  - [Commit Messages](#commit-messages)




## I Have a Question

> If you want to ask a question, we assume that you have read the available
> [Documentation](https://github.com/datascienceworld-kan/vinagent/blob/main/README.md).

Before you ask a question, it is best to search for existing [Issues](https://github.com/datascienceworld-kan/vinagent/issues)
that might help you. If you find a relevant issue that already exists and still need clarification, please add your question to that existing issue. We also recommend reaching out to the community in the vinagent [Discord](https://discord.com/channels/1036147288994758717/1358017320970358864) server.

If you then still feel the need to ask a question and need clarification, we recommend the following:

- Open an [Issue](https://github.com/datascienceworld-kan/vinagent/issues/new).
- Provide as much context as you can about what you're running into.
- Provide project and platform versions (python, OS, etc.), depending on what seems relevant.

We (or someone in the community) will then take care of the issue as soon as possible.


## I Want To Contribute

> ### Legal Notice <!-- omit in toc -->
> When contributing to this project, you must agree that you have authored 100% of the content, that
> you have the necessary rights to the content and that the content you contribute may be provided
> under the project license.

### Reporting Bugs

<!-- omit in toc -->
#### Before Submitting a Bug Report

A good bug report shouldn't leave others needing to chase you up for more information. Therefore, we ask
you to investigate carefully, collect information and describe the issue in detail in your report. Please
complete the following steps in advance to help us fix any potential bug as fast as possible.

- Make sure that you are using the latest version.
- Determine if your bug is really a bug and not an error on your side e.g. using incompatible environment 
  components/versions (Make sure that you have read the [documentation](https://github.com/datascienceworld-kan/vinagent/blob/main/README.md).
  If you are looking for support, you might want to check [this section](#i-have-a-question)).
- To see if other users have experienced (and potentially already solved) the same issue you are having,
  check if there is not already a bug report existing for your bug or error in the [bug tracker](https://github.com/datascienceworld-kan/vinagent?q=label%3Abug).
- Also make sure to search the internet (including Stack Overflow) to see if users outside of the GitHub
  community have discussed the issue.
- Collect information about the bug:
  - Stack trace (Traceback)
  - OS, Platform and Version (Windows, Linux, macOS, x86, ARM)
  - Version of the interpreter, compiler, SDK, runtime environment, package manager, depending on
    what seems relevant.
  - Possibly your input and the output
  - Can you reliably reproduce the issue? And can you also reproduce it with older versions?

<!-- omit in toc -->
#### How Do I Submit a Good Bug Report?

> You must never report security related issues, vulnerabilities or bugs including sensitive information to
> the issue tracker, or elsewhere in public. Instead sensitive bugs must be sent by email to <datascienceworld.kan@gmail.com>.
<!-- You may add a PGP key to allow the messages to be sent encrypted as well. -->

We use GitHub issues to track bugs and errors. If you run into an issue with the project:

- Open an [Issue](https://github.com/datascienceworld-kan/vinagent/issues/new). (Since we can't be sure at
  this point whether it is a bug or not, we ask you not to talk about a bug yet and not to label the issue.)
- Explain the behavior you would expect and the actual behavior.
- Please provide as much context as possible and describe the *reproduction steps* that someone else can
  follow to recreate the issue on their own. This usually includes your code. For good bug reports you
  should isolate the problem and create a reduced test case.
- Provide the information you collected in the previous section.

Once it's filed:

- The project team will label the issue accordingly.
- A team member will try to reproduce the issue with your provided steps. If there are no reproduction 
  steps or no obvious way to reproduce the issue, the team will ask you for those steps and mark the
  issue as `needs-repro`. Bugs with the `needs-repro` tag will not be addressed until they are reproduced.
- If the team is able to reproduce the issue, it will be marked `needs-fix`, as well as possibly other
  tags (such as `critical`), and the issue will be left to be
  [implemented by someone](#your-first-code-contribution).

Please use the issue templates provided.


### Suggesting Enhancements

This section guides you through submitting an enhancement suggestion for vinagent,
**including completely new features and minor improvements to existing functionality**. Following these
guidelines will help maintainers and the community to understand your suggestion and find related suggestions.

<!-- omit in toc -->
#### Before Submitting an Enhancement

- Make sure that you are using the latest version.
- Read the [documentation](https://github.com/datascienceworld-kan/vinagent/blob/main/README.md) carefully
  and find out if the functionality is already covered, maybe by an individual configuration.
- Perform a [search](https://github.com/datascienceworld-kan/vinagent/issues) to see if the enhancement has
  already been suggested. If it has, add a comment to the existing issue instead of opening a new one.
- Find out whether your idea fits with the scope and aims of the project. It's up to you to make a strong
  case to convince the project's developers of the merits of this feature. Keep in mind that we want features that will be useful to the majority of our users and not just a small subset. If you're just targeting a minority of users, consider writing an add-on/plugin library.

<!-- omit in toc -->
#### How Do I Submit a Good Enhancement Suggestion?

Enhancement suggestions are tracked as [GitHub issues](https://github.com/datascienceworld-kan/vinagent/issues).

- Use a **clear and descriptive title** for the issue to identify the suggestion.
- Provide a **step-by-step description of the suggested enhancement** in as many details as possible.
- **Describe the current behavior** and **explain which behavior you expected to see instead** and why.
  At this point you can also tell which alternatives do not work for you.
- **Explain why this enhancement would be useful** to most Vinagent users. You may also want to
  point out the other projects that solved it better and which could serve as inspiration.


### Your First Code Contribution

#### Pre-requisites

You should first [fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo)
the `vinagent` repository and then clone your forked repository:

```bash
git clone https://github.com/<YOUR_GITHUB_USER>/vinagent.git
```



Once in the cloned repository directory, make a branch on the forked repository with your username and
description of PR:
```bash
git checkout -B <username>/<description>
```

Please install the development and test dependencies:
```bash
poetry install --with dev,test
```

`vinagent` uses pre-commit to ensure the formatting is consistent:
```bash
pre-commit install
```

**Make suggested changes**

Afterwards, our suite of formatting tests will run automatically before each `git commit`. You can also
run these manually:
```bash
pre-commit run --all-files
```

If a formatting test fails, it will fix the modified code in place and abort the `git commit`. After looking
over the changes, you can `git add <modified files>` and then repeat the previous git commit command.

**Note**: a github workflow will check the files with the same formatter and reject the PR if it doesn't
pass, so please make sure it passes locally.


#### Testing
`vinagent` tracks unit tests. Pytest is used to execute said unit tests in `tests/`:

```bash
poetry run pytest tests
```

If your code changes implement a new function, please make a corresponding unit test to the `test/*` files.

#### Contributing Workflow
We actively welcome your pull requests.

1. Create your new branch from main in your forked repo, with your username and a name describing the work
   you're completing e.g. user-123/add-feature-x.
2. If you've added code that should be tested, add tests. Ensure all tests pass. See the testing section
   for more information.
3. If you've changed APIs, update the documentation.
4. Make sure your code lints.



### Improving The Documentation
We welcome valuable contributions in the form of new documentation or revised documentation that provide
further clarity or accuracy. Each function should be clearly documented. Well-documented code is easier
to review and understand/extend.

## Styleguides
For code documentation, please follow the [Google styleguide](https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings).

```

### File: docs\convert_jpynb_to_markdown.sh
```sh
#!/bin/bash
set -e

if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <input_notebook.ipynb> <output_markdown.md>"
  exit 1
fi

INPUT_NOTEBOOK="$1"
OUTPUT_MARKDOWN="$2"
OUTPUT_DIR=$(dirname "$OUTPUT_MARKDOWN")
OUTPUT_NAME=$(basename "$OUTPUT_MARKDOWN" .md)

# Ensure output directory exists
mkdir -p "$OUTPUT_DIR"

# Convert notebook to markdown
jupyter nbconvert --to markdown "$INPUT_NOTEBOOK" --output "$OUTPUT_NAME" --output-dir "$OUTPUT_DIR"

echo "✅ Converted $INPUT_NOTEBOOK to $OUTPUT_MARKDOWN"

```

### File: docs\settings.json
```json
{
    "yaml.schemas": {
      "https://squidfunk.github.io/mkdocs-material/schema.json": "mkdocs.yml"
    },
    "yaml.customTags": [ 
      "!ENV scalar",
      "!ENV sequence",
      "!relative scalar",
      "tag:yaml.org,2002:python/name:material.extensions.emoji.to_svg",
      "tag:yaml.org,2002:python/name:material.extensions.emoji.twemoji",
      "tag:yaml.org,2002:python/name:pymdownx.superfences.fence_code_format",
      "tag:yaml.org,2002:python/object/apply:pymdownx.slugs.slugify mapping"
    ]
  }

```

### File: .github\workflows\black.yaml
```yaml
name: Lint

on: [push, pull_request]

jobs:
    lint:
        runs-on: ubuntu-latest
        steps:
            - name: Checkout repository
              uses: actions/checkout@v4
              with:
                fetch-depth: 0

            - name: Set up Python 3.11
              uses: actions/setup-python@v5
              with:
                python-version: "3.11"

            - name: Run Black
              uses: psf/black@25.9.0
              with:
                options: "--check --diff"

```

### File: .github\workflows\ci_docs.yaml
```yaml
name: Deploy MkDocs to GitHub Pages

on:
  push:
    branches:
      - main

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          fetch-depth: 0
    
      - name: Configure Git Credentials
        run: |
          git config user.name github-actions[bot]
          git config user.email 41898282+github-actions[bot]@users.noreply.github.com

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      
      - run: echo "cache_id=$(date --utc '+%V')" >> $GITHUB_ENV 
      
      - uses: actions/cache@v4
        with:
            key: mkdocs-material-${{ env.cache_id }}
            path: .cache 
            restore-keys: |
                mkdocs-material-

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install mkdocs mkdocs-material mkdocstrings[python]
      
      - name: Debug directory structure
        run: |
            ls -R
            pwd

      - name: Deploy to GitHub Pages
        run: mkdocs gh-deploy --force --config-file ./docs/mkdocs.yml

```

### File: docs\docs\index.md
```md
---
hide_comments: true
title: Vinagent
---

[![Version](https://img.shields.io/pypi/v/vinagent.svg)](https://pypi.org/project/vinagent/)
[![PyPI Downloads](https://static.pepy.tech/badge/vinagent/week)](https://pepy.tech/projects/vinagent)
[![Downloads](https://static.pepy.tech/badge/vinagent/month)](https://pepy.tech/project/vinagent)
[![PyPI Downloads](https://static.pepy.tech/badge/vinagent)](https://pepy.tech/projects/vinagent)
[![Reddit r/vinagent](https://img.shields.io/badge/Reddit-r%2Fvinagent-orange?logo=reddit&logoColor=white)](https://www.reddit.com/r/vinagent/)
[![Discord](https://img.shields.io/badge/Chat-Discord-5865F2?logo=discord&logoColor=white)](https://discord.com/channels/1036147288994758717/1358017320970358864)
![License](https://img.shields.io/github/license/datascienceworld-kan/vinagent)

`Vinagent` is a simple and flexible library designed for building smart agent assistants across various industries. Vinagent towards the AI in multiple-industries like Financial and Banking, Healthcare, Manufacturing, and Autonomous Systems. It is designed based on simplicity, integrability, observability, and optimizablity. Vinagent features a clean syntax, supports individual customization, enhances capabilities through integration with multiple tools, and effectively handles complex tasks through curated workflow creation.

Whether you're creating an AI-powered deep search smart assistant, a financial analysis agent, or any domain-specific automation agent, Vinagent provides a simple yet powerful foundation.

With its modular tool system, you can easily extend your agent's capabilities by integrating a wide range of tools. Each tool is self-contained, well-documented, and can be registered dynamically—making it effortless to scale and adapt your agent to new tasks or environments.

## Feature comparison
<table style="width: 100%;">
    <tr>
      <th align="center">Feature</th>
      <th align="center">Vinagent</th>
      <th align="center">Dify.AI</th>
      <th align="center">LangChain</th>
      <th align="center">Flowise</th>
      <th align="center">OpenAI Assistants API</th>
    </tr>
    <tr>
      <td align="center">Programming Approach</td>
      <td align="center">Python Code</td>
      <td align="center">API + App-oriented</td>
      <td align="center">Python Code</td>
      <td align="center">App-oriented</td>
      <td align="center">API-oriented</td>
    </tr>
    <tr>
      <td align="center">Supported LLMs</td>
      <td align="center">Rich Variety</td>
      <td align="center">Rich Variety</td>
      <td align="center">Rich Variety</td>
      <td align="center">Rich Variety</td>
      <td align="center">OpenAI-only</td>
    </tr>
    <tr>
      <td align="center">Agent</td>
      <td align="center">✅</td>
      <td align="center">✅</td>
      <td align="center">✅</td>
      <td align="center">❌</td>
      <td align="center">✅</td>
    </tr>
     <tr>
      <td align="center">Multi Agent</td>
      <td align="center">✅</td>
      <td align="center">❌</td>
      <td align="center">❌</td>
      <td align="center">✅</td>
      <td align="center">❌</td>
    </tr>
    <tr>
      <td align="center">Workflow</td>
      <td align="center">✅</td>
      <td align="center">✅</td>
      <td align="center">✅</td>
      <td align="center">✅</td>
      <td align="center">❌</td>
    </tr>
    <tr>
        <td align="center">Graph Memory</td>
        <td align="center">✅</td>
        <td align="center">❌</td>
        <td align="center">❌</td>
        <td align="center">❌</td>
        <td align="center">❌</td>
    </tr>
    <tr>
        <td align="center">Personalize</td>
        <td align="center">✅</td>
        <td align="center">❌</td>
        <td align="center">❌</td>
        <td align="center">❌</td>
        <td align="center">❌</td>
    </tr>
    <tr>
        <td align="center">RAG Engine</td>
        <td align="center">✅</td>
        <td align="center">✅</td>
        <td align="center">✅</td>
        <td align="center">✅</td>
        <td align="center">✅</td>
    </tr>
    <tr>
        <td align="center">MCP Connection</td>
        <td align="center">✅</td>
        <td align="center">✅</td>
        <td align="center">✅</td>
        <td align="center">✅</td>
        <td align="center">✅</td>
      </tr>
    <tr>
      <td align="center">Security</td>
      <td align="center">✅</td>
      <td align="center">❌</td>
      <td align="center">❌</td>
      <td align="center">❌</td>
      <td align="center">❌</td>
    </tr>
    <tr>
      <td align="center">Observability</td>
      <td align="center">✅</td>
      <td align="center">✅</td>
      <td align="center">✅</td>
      <td align="center">❌</td>
      <td align="center">❌</td>
    </tr>
    <tr>
      <td align="center">Local Deployment</td>
      <td align="center">✅</td>
      <td align="center">✅</td>
      <td align="center">✅</td>
      <td align="center">✅</td>
      <td align="center">❌</td>
    </tr>
  </table>

## Component Overview

`Vinagent` helps design AI agents to solve various tasks across multiple domains such as Finance and Banking, Healthcare, Manufacturing, and Autonomous Systems. It provides a comprehensive set of components for building agents, including: Model, Tool, Graph Memory, Workflow, and Observability.

![](asset/agent_system_design_v2.png)

The following are specifically designed components:

- **Tools**: Supports a variety of different tools, from user-implemented tools like Function tool and Module tool, to tools from the MCP market. Thus, Vinagent ensures you always have all the necessary features and data for every task.

- **Memory**: Vinagent organizes the short-term and long-term memory of the Agent through graph storage, creating a graph network that compresses information more efficiently than traditional conversation history storage. This innovative approach helps Vinagent save memory and minimize hallucination.

- **Planning and Control**: Based on the graph foundation of Langgraph, Vinagent designs workflows with simpler syntax, using the right shift `>>` operator, which is easy to use for beginers. This makes creating and managing complex workflows much simpler compared to other agent workflow libraries, even for a complex conditional and parallel workflows.

- **Personalize user Experience**: Vinagent supports inference through three methods: asynchronous, synchronous, and streaming. This flexibility allows you to speed up processing and improve user experience when applying agents in AI products that require fast and immediate processing speeds.

- **Security**: Vinagent ensures AI Agent security through OAuth 2.0 authentication, a protocol that allows third-party applications to access Agent resources without exposing any user's credentials. This approach uses access token instread of direct user/password authentication. It works by orchestrating these participants.

- **Prompt Optimization**: Vinagent integrates automatic prompt optimization features, enhancing accuracy for Agents. This ensures the Agent operates effectively even with specialized tasks.
Observability: Allows monitoring of the Agent’s processing information on-premise and is compatible with Jupyter Notebook. You can measure total processing time, the number of input/output tokens, as well as LLM model information at each step in the workflow. This detailed observability feature is crucial for debugging and optimizing the Agent.

## Support Multi-agent

![](asset/multi_agent_architectures.png)

Vinagent designs an advanced multi-agent solution with key strengths:

- Specialized Agents: Each [single agent](https://datascienceworld-kan.github.io/vinagent/#component-overview) is fully equipped with its own LLM, tools, memory, skills, and authentication layer.

- Shared Conversation: Agents collaborate seamlessly in the same conversation, enabling them to capture and utilize each other’s context.

- Human-in-the-Loop: Users can directly participate and interact within the agent workflow.

- Customizable Order: A Crew class allows flexible control over the sequence of agents in a conversation.

## Vinagent ecosystem

Although `Vinagent` can stand as a independent library for agent, it is designed to be integrated with other Vinagent's Ecosystem libraries that expands its capabilities rather than just a simple Agent. The `Vinagent` ecosystem consists of the following components:

- [Aucodb](https://github.com/datascienceworld-kan/AucoDB.git): An open-source database for storing and managing data for AI Agent, providing a flexible solution for storing and retrieving data for Vinagent's agents under multiple format such as collection of tools, messages, graph, vector storage, and logging. Aucodb can ingest and transform various text data into knowledge graph and save to neo4j and adapt various popular vector store databases like `chroma, faiss, milvus, pgvector, pinecone, qdrant, and weaviate`.

- [Mlflow - Extension](https://github.com/datascienceworld-kan/vinagent/tree/main#10-agent-observability): Intergate with mlflow library to log the Agent's information and profile the Agent's performance. This allows you to track the Agent capability and optimize.

```

### File: docs\docs\contributing\contributing.md
```md
# Contributing to Vinagent

First off, thanks for taking the time to contribute!

All types of contributions are encouraged and valued. See the [Table of Contents](#table-of-contents)
for different ways to help and details about how this project handles them. Please make sure to read
the relevant section before making your contribution. It will make it a lot easier for us maintainers
and smooth out the experience for all involved. The community looks forward to your contributions.

> And if you like the project, but just don't have time to contribute, that's fine. There are other easy
> ways to support the project and show your appreciation, which we would also be very happy about:
> - Star the project
> - Tweet about it
> - Refer this project in your project's readme
> - Mention the project at local meetups and tell your friends/colleagues

<!-- omit in toc -->
## Table of Contents

- [I Have a Question](#i-have-a-question)
- [I Want To Contribute](#i-want-to-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Enhancements](#suggesting-enhancements)
  - [Your First Code Contribution](#your-first-code-contribution)
  - [Improving The Documentation](#improving-the-documentation)
- [Styleguides](#styleguides)
  - [Commit Messages](#commit-messages)




## I Have a Question

> If you want to ask a question, we assume that you have read the available
> [Documentation](https://github.com/datascienceworld-kan/vinagent/blob/main/README.md).

Before you ask a question, it is best to search for existing [Issues](https://github.com/datascienceworld-kan/vinagent/issues)
that might help you. If you find a relevant issue that already exists and still need clarification, please add your question to that existing issue. We also recommend reaching out to the community in the vinagent [Discord](https://discord.com/channels/1036147288994758717/1358017320970358864) server.

If you then still feel the need to ask a question and need clarification, we recommend the following:

- Open an [Issue](https://github.com/datascienceworld-kan/vinagent/issues/new).
- Provide as much context as you can about what you're running into.
- Provide project and platform versions (python, OS, etc.), depending on what seems relevant.

We (or someone in the community) will then take care of the issue as soon as possible.


## I Want To Contribute

> ### Legal Notice <!-- omit in toc -->
> When contributing to this project, you must agree that you have authored 100% of the content, that
> you have the necessary rights to the content and that the content you contribute may be provided
> under the project license.

### Reporting Bugs

<!-- omit in toc -->
#### Before Submitting a Bug Report

A good bug report shouldn't leave others needing to chase you up for more information. Therefore, we ask
you to investigate carefully, collect information and describe the issue in detail in your report. Please
complete the following steps in advance to help us fix any potential bug as fast as possible.

- Make sure that you are using the latest version.
- Determine if your bug is really a bug and not an error on your side e.g. using incompatible environment 
  components/versions (Make sure that you have read the [documentation](https://github.com/datascienceworld-kan/vinagent/blob/main/README.md).
  If you are looking for support, you might want to check [this section](#i-have-a-question)).
- To see if other users have experienced (and potentially already solved) the same issue you are having,
  check if there is not already a bug report existing for your bug or error in the [bug tracker](https://github.com/datascienceworld-kan/vinagent?q=label%3Abug).
- Also make sure to search the internet (including Stack Overflow) to see if users outside of the GitHub
  community have discussed the issue.
- Collect information about the bug:
  - Stack trace (Traceback)
  - OS, Platform and Version (Windows, Linux, macOS, x86, ARM)
  - Version of the interpreter, compiler, SDK, runtime environment, package manager, depending on
    what seems relevant.
  - Possibly your input and the output
  - Can you reliably reproduce the issue? And can you also reproduce it with older versions?

<!-- omit in toc -->
#### How Do I Submit a Good Bug Report?

> You must never report security related issues, vulnerabilities or bugs including sensitive information to
> the issue tracker, or elsewhere in public. Instead sensitive bugs must be sent by email to <datascienceworld.kan@gmail.com>.
<!-- You may add a PGP key to allow the messages to be sent encrypted as well. -->

We use GitHub issues to track bugs and errors. If you run into an issue with the project:

- Open an [Issue](https://github.com/datascienceworld-kan/vinagent/issues/new). (Since we can't be sure at
  this point whether it is a bug or not, we ask you not to talk about a bug yet and not to label the issue.)
- Explain the behavior you would expect and the actual behavior.
- Please provide as much context as possible and describe the *reproduction steps* that someone else can
  follow to recreate the issue on their own. This usually includes your code. For good bug reports you
  should isolate the problem and create a reduced test case.
- Provide the information you collected in the previous section.

Once it's filed:

- The project team will label the issue accordingly.
- A team member will try to reproduce the issue with your provided steps. If there are no reproduction 
  steps or no obvious way to reproduce the issue, the team will ask you for those steps and mark the
  issue as `needs-repro`. Bugs with the `needs-repro` tag will not be addressed until they are reproduced.
- If the team is able to reproduce the issue, it will be marked `needs-fix`, as well as possibly other
  tags (such as `critical`), and the issue will be left to be
  [implemented by someone](#your-first-code-contribution).

Please use the issue templates provided.


### Suggesting Enhancements

This section guides you through submitting an enhancement suggestion for vinagent,
**including completely new features and minor improvements to existing functionality**. Following these
guidelines will help maintainers and the community to understand your suggestion and find related suggestions.

<!-- omit in toc -->
#### Before Submitting an Enhancement

- Make sure that you are using the latest version.
- Read the [documentation](https://github.com/datascienceworld-kan/vinagent/blob/main/README.md) carefully
  and find out if the functionality is already covered, maybe by an individual configuration.
- Perform a [search](https://github.com/datascienceworld-kan/vinagent/issues) to see if the enhancement has
  already been suggested. If it has, add a comment to the existing issue instead of opening a new one.
- Find out whether your idea fits with the scope and aims of the project. It's up to you to make a strong
  case to convince the project's developers of the merits of this feature. Keep in mind that we want features that will be useful to the majority of our users and not just a small subset. If you're just targeting a minority of users, consider writing an add-on/plugin library.

<!-- omit in toc -->
#### How Do I Submit a Good Enhancement Suggestion?

Enhancement suggestions are tracked as [GitHub issues](https://github.com/datascienceworld-kan/vinagent/issues).

- Use a **clear and descriptive title** for the issue to identify the suggestion.
- Provide a **step-by-step description of the suggested enhancement** in as many details as possible.
- **Describe the current behavior** and **explain which behavior you expected to see instead** and why.
  At this point you can also tell which alternatives do not work for you.
- **Explain why this enhancement would be useful** to most Vinagent users. You may also want to
  point out the other projects that solved it better and which could serve as inspiration.


### Your First Code Contribution

#### Pre-requisites

You should first [fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo)
the `vinagent` repository and then clone your forked repository:

```bash
git clone https://github.com/<YOUR_GITHUB_USER>/vinagent.git
```



Once in the cloned repository directory, make a branch on the forked repository with your username and
description of PR:
```bash
git checkout -B <username>/<description>
```

Please install the development and test dependencies:
```bash
poetry install --with dev,test
```

`vinagent` uses pre-commit to ensure the formatting is consistent:
```bash
pre-commit install
```

**Make suggested changes**

Afterwards, our suite of formatting tests will run automatically before each `git commit`. You can also
run these manually:
```bash
pre-commit run --all-files
```

If a formatting test fails, it will fix the modified code in place and abort the `git commit`. After looking
over the changes, you can `git add <modified files>` and then repeat the previous git commit command.

**Note**: a github workflow will check the files with the same formatter and reject the PR if it doesn't
pass, so please make sure it passes locally.


#### Testing
`vinagent` tracks unit tests. Pytest is used to execute said unit tests in `tests/`:

```bash
poetry run pytest tests
```

If your code changes implement a new function, please make a corresponding unit test to the `test/*` files.

#### Contributing Workflow
We actively welcome your pull requests.

1. Create your new branch from main in your forked repo, with your username and a name describing the work
   you're completing e.g. user-123/add-feature-x.
2. If you've added code that should be tested, add tests. Ensure all tests pass. See the testing section
   for more information.
3. If you've changed APIs, update the documentation.
4. Make sure your code lints.



### Improving The Documentation
We welcome valuable contributions in the form of new documentation or revised documentation that provide
further clarity or accuracy. Each function should be clearly documented. Well-documented code is easier
to review and understand/extend.

## Styleguides
For code documentation, please follow the [Google styleguide](https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings).

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
