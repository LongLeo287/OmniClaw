---
id: deepeval
type: knowledge
owner: OA_Triage
---
# deepeval
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<p align="center">
    <img src="https://github.com/confident-ai/deepeval/blob/main/docs/static/img/deepeval.png" alt="DeepEval Logo" width="100%">
</p>

<p align="center">
    <h1 align="center">The LLM Evaluation Framework</h1>
</p>

<p align="center">
<a href="https://trendshift.io/repositories/5917" target="_blank"><img src="https://trendshift.io/api/badge/repositories/5917" alt="confident-ai%2Fdeepeval | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
</p>

<p align="center">
    <a href="https://discord.gg/3SEyvpgu2f">
        <img alt="discord-invite" src="https://dcbadge.vercel.app/api/server/3SEyvpgu2f?style=flat">
    </a>
</p>

<h4 align="center">
    <p>
        <a href="https://deepeval.com/docs/getting-started?utm_source=GitHub">Documentation</a> |
        <a href="#-metrics-and-features">Metrics and Features</a> |
        <a href="#-quickstart">Getting Started</a> |
        <a href="#-integrations">Integrations</a> |
        <a href="https://confident-ai.com?utm_source=GitHub">Confident AI</a>
    <p>
</h4>

<p align="center">
    <a href="https://github.com/confident-ai/deepeval/releases">
        <img alt="GitHub release" src="https://img.shields.io/github/release/confident-ai/deepeval.svg?color=violet">
    </a>
    <a href="https://colab.research.google.com/drive/1PPxYEBa6eu__LquGoFFJZkhYgWVYE6kh?usp=sharing">
        <img alt="Try Quickstart in Colab" src="https://colab.research.google.com/assets/colab-badge.svg">
    </a>
    <a href="https://github.com/confident-ai/deepeval/blob/master/LICENSE.md">
        <img alt="License" src="https://img.shields.io/github/license/confident-ai/deepeval.svg?color=yellow">
    </a>
    <a href="https://x.com/deepeval">
        <img alt="Twitter Follow" src="https://img.shields.io/twitter/follow/deepeval?style=social&logo=x">
    </a>
</p>

<p align="center">
    <!-- Keep these links. Translations will automatically update with the README. -->
    <a href="https://www.readme-i18n.com/confident-ai/deepeval?lang=de">Deutsch</a> | 
    <a href="https://www.readme-i18n.com/confident-ai/deepeval?lang=es">Español</a> | 
    <a href="https://www.readme-i18n.com/confident-ai/deepeval?lang=fr">français</a> | 
    <a href="https://www.readme-i18n.com/confident-ai/deepeval?lang=ja">日本語</a> | 
    <a href="https://www.readme-i18n.com/confident-ai/deepeval?lang=ko">한국어</a> | 
    <a href="https://www.readme-i18n.com/confident-ai/deepeval?lang=pt">Português</a> | 
    <a href="https://www.readme-i18n.com/confident-ai/deepeval?lang=ru">Русский</a> | 
    <a href="https://www.readme-i18n.com/confident-ai/deepeval?lang=zh">中文</a>
</p>

**DeepEval** is a simple-to-use, open-source LLM evaluation framework, for evaluating large-language model systems. It is similar to Pytest but specialized for unit testing LLM apps. DeepEval incorporates the latest research to run evals via metrics such as G-Eval, task completion, answer relevancy, hallucination, etc., which uses LLM-as-a-judge and other NLP models that run **locally on your machine**.

Whether you're building AI agents, RAG pipelines, or chatbots, implemented via LangChain or OpenAI, DeepEval has you covered. With it, you can easily determine the optimal models, prompts, and architecture to improve your AI quality, prevent prompt drifting, or even transition from OpenAI to Claude with confidence.

> [!IMPORTANT]
> Need a place for your DeepEval testing data to live 🏡❤️? [Sign up to the DeepEval platform](https://confident-ai.com?utm_source=GitHub) to compare iterations of your LLM app, generate & share testing reports, and more.
>
> ![Demo GIF](assets/demo.gif)

> Want to talk LLM evaluation, need help picking metrics, or just to say hi? [Come join our discord.](https://discord.com/invite/3SEyvpgu2f)

<br />

# 🔥 Metrics and Features

- 📐 Large variety of ready-to-use LLM eval metrics (all with explanations) powered by **ANY** LLM of your choice, statistical methods, or NLP models that run **locally on your machine** covering all use cases:

  - **Custom, All-Purpose Metrics:**

    - [G-Eval](https://deepeval.com/docs/metrics-llm-evals) — a research-backed LLM-as-a-judge metric for evaluating on any custom criteria with human-like accuracy
    - [DAG](https://deepeval.com/docs/metrics-dag) — DeepEval's graph-based deterministic LLM-as-a-judge metric builder

  - <details>
    <summary><b>Agentic Metrics</b></summary>

    - [Task Completion](https://deepeval.com/docs/metrics-task-completion) — evaluate whether an agent accomplished its goal
    - [Tool Correctness](https://deepeval.com/docs/metrics-tool-correctness) — check if the right tools were called with the right arguments
    - [Goal Accuracy](https://deepeval.com/docs/metrics-goal-accuracy) — measure how accurately the agent achieved the intended goal
    - [Step Efficiency](https://deepeval.com/docs/metrics-step-efficiency) — evaluate whether the agent took unnecessary steps
    - [Plan Adherence](https://deepeval.com/docs/metrics-plan-adherence) — check if the agent followed the expected plan
    - [Plan Quality](https://deepeval.com/docs/metrics-plan-quality) — evaluate the quality of the agent's plan
    - [Tool Use](https://deepeval.com/docs/metrics-tool-use) — measure quality of tool usage
    - [Argument Correctness](https://deepeval.com/docs/metrics-argument-correctness) — validate tool call arguments

    </details>

  - <details>
    <summary><b>RAG Metrics</b></summary>

    - [Answer Relevancy](https://deepeval.com/docs/metrics-answer-relevancy) — measure how relevant the RAG pipeline's output is to the input
    - [Faithfulness](https://deepeval.com/docs/metrics-faithfulness) — evaluate whether the RAG pipeline's output factually aligns with the retrieval context
    - [Contextual Recall](https://deepeval.com/docs/metrics-contextual-recall) — measure how well the RAG pipeline's retrieval context aligns with the expected output
    - [Contextual Precision](https://deepeval.com/docs/metrics-contextual-precision) — evaluate whether relevant nodes in the RAG pipeline's retrieval context are ranked higher
    - [Contextual Relevancy](https://deepeval.com/docs/metrics-contextual-relevancy) — measure the overall relevance of the RAG pipeline's retrieval context to the input
    - [RAGAS](https://deepeval.com/docs/metrics-ragas) — average of answer relevancy, faithfulness, contextual precision, and contextual recall

    </details>

  - <details>
    <summary><b>Multi-Turn Metrics</b></summary>

    - [Knowledge Retention](https://deepeval.com/docs/metrics-knowledge-retention) — evaluate whether the chatbot retains factual information throughout a conversation
    - [Conversation Completeness](https://deepeval.com/docs/metrics-conversation-completeness) — measure whether the chatbot satisfies user needs throughout a conversation
    - [Turn Relevancy](https://deepeval.com/docs/metrics-turn-relevancy) — evaluate whether the chatbot generates consistently relevant responses throughout a conversation
    - [Turn Faithfulness](https://deepeval.com/docs/metrics-turn-faithfulness) — check if the chatbot's responses are factually grounded in retrieval context across turns
    - [Role Adherence](https://deepeval.com/docs/metrics-role-adherence) — evaluate whether the chatbot adheres to its assigned role throughout a conversation

    </details>

  - <details>
    <summary><b>MCP Metrics</b></summary>

    - [MCP Task Completion](https://deepeval.com/docs/metrics-mcp-task-completion) — evaluate how effectively an MCP-based agent accomplishes a task
    - [MCP Use](https://deepeval.com/docs/metrics-mcp-use) — measure how effectively an agent uses its available MCP servers
    - [Multi-Turn MCP Use](https://deepeval.com/docs/metrics-multi-turn-mcp-use) — evaluate MCP server usage across conversation turns

    </details>

  - <details>
    <summary><b>Multimodal Metrics</b></summary>

    - [Text to Image](https://deepeval.com/docs/multimodal-metrics-text-to-image) — evaluate image generation quality based on semantic consistency and perceptual quality
    - [Image Editing](https://deepeval.com/docs/multimodal-metrics-image-editing) — evaluate image editing quality based on semantic consistency and perceptual quality
    - [Image Coherence](https://deepeval.com/docs/multimodal-metrics-image-coherence) — measure how well images align with their accompanying text
    - [Image Helpfulness](https://deepeval.com/docs/multimodal-metrics-image-helpfulness) — evaluate how effectively images contribute to user comprehension of the text
    - [Image Reference](https://deepeval.com/docs/multimodal-metrics-image-reference) — evaluate how accurately images are referred to or explained by accompanying text

    </details>

  - <details>
    <summary><b>Other Metrics</b></summary>

    - [Hallucination](https://deepeval.com/docs/metrics-hallucination) — check whether the LLM generates factually correct information against provided context
    - [Summarization](https://deepeval.com/docs/metrics-summarization) — evaluate whether summaries are factually correct and include necessary details
    - [Bias](https://deepeval.com/docs/metrics-bias) — detect gender, racial, or political bias in LLM outputs
    - [Toxicity](https://deepeval.com/docs/metrics-toxicity) — evaluate toxicity in LLM outputs
    - [JSON Correctness](https://deepeval.com/docs/metrics-json-correctness) — check whether the output matches an expected JSON schema
    - [Prompt Alignment](https://deepeval.com/docs/metrics-prompt-alignment) — measure whether the output aligns with instructions in the prompt template

    </details>

- 🎯 Supports both end-to-end and component-level LLM evaluation.
- 🧩 Build your own custom metrics that are automatically integrated with DeepEval's ecosystem.
- 🔮 Generate both single and multi-turn synthetic datasets for evaluation.
- 🔗 Integrates seamlessly with **ANY** CI/CD environment.
- 🧬 Optimize prompts automatically based on evaluation results.
- 🏆 Easily benchmark **ANY** LLM on popular LLM benchmarks in [under 10 lines of code.](https://deepeval.com/docs/benchmarks-introduction?utm_source=GitHub), including MMLU, HellaSwag, DROP, BIG-Bench Hard, TruthfulQA, HumanEval, GSM8K.

<br />

# 🔌 Integrations

DeepEval plugs into any LLM framework — OpenAI Agents, LangChain, CrewAI, and more. To scale evals across your team — or let anyone run them without writing code — **Confident AI** gives you a native platform integration.

## Frameworks

- [OpenAI](https://www.deepeval.com/integrations/frameworks/openai?utm_source=GitHub) — evaluate and trace OpenAI applications via a client wrapper
- [OpenAI Agents](https://www.deepeval.com/integrations/frameworks/openai-agents?utm_source=GitHub) — evaluate OpenAI Agents end-to-end in under a minute
- [LangChain](https://www.deepeval.com/integrations/frameworks/langchain?utm_source=GitHub) — evaluate LangChain applications with a callback handler
- [LangGraph](https://www.deepeval.com/integrations/frameworks/langgraph?utm_source=GitHub) — evaluate LangGraph agents with a callback handler
- [Pydantic AI](https://www.deepeval.com/integrations/frameworks/pydanticai?utm_source=GitHub) — evaluate Pydantic AI agents with type-safe validation
- [CrewAI](https://www.deepeval.com/integrations/frameworks/crewai?utm_source=GitHub) — evaluate CrewAI multi-agent systems
- [Anthropic](https://www.deepeval.com/integrations/frameworks/anthropic?utm_source=GitHub) — evaluate and trace Claude applications via a client wrapper
- [AWS AgentCore](https://www.deepeval.com/integrations/frameworks/agentcore?utm_source=GitHub) — evaluate agents deployed on Amazon AgentCore
- [LlamaIndex](https://www.deepeval.com/integrations/frameworks/llamaindex?utm_source=GitHub) — evaluate RAG applications built with LlamaIndex

## ☁️ Platform + Ecosystem

[Confident AI](https://confident-ai.com?utm_source=GitHub) is an all-in-one platform that integrates natively with DeepEval.

- Manage datasets, trace LLM applications, run evaluations, and monitor responses in production — all from one platform.
- Don't need a UI? Confident AI can also be your data persistant layer - run evals, pull datasets, and inspect traces straight from claude code, cursor, via Confident AI's [MCP server](https://github.com/confident-ai/confident-mcp-server).

<p align="center">
  <img src="assets/confident-mcp-architecture.png" alt="Confident AI MCP Architecture" width="500">
</p>

<br />

# 🚀 QuickStart

Let's pretend your LLM application is a RAG based customer support chatbot; here's how DeepEval can help test what you've built.

## Installation

Deepeval works with **Python>=3.9+**.

```
pip install -U deepeval
```

## Create an account (highly recommended)

Using the `deepeval` platform will allow you to generate sharable testing reports on the cloud. It is free, takes no additional code to setup, and we highly recommend giving it a try.

To login, run:

```
deepeval login
```

Follow the instructions in the CLI to create an account, copy your API key, and paste it into the CLI. All test cases will automatically be logged (find more information on data privacy [here](https://deepeval.com/docs/data-privacy?utm_source=GitHub)).

## Write your first test case

Create a test file:

```bash
touch test_chatbot.py
```

Open `test_chatbot.py` and write your first test case to run an **end-to-end** evaluation using DeepEval, which treats your LLM app as a black-box:

```python
import pytest
from deepeval import assert_test
from deepeval.metrics import GEval
from deepeval.test_case import LLMTestCase, LLMTestCaseParams

def test_case():
    correctness_metric = GEval(
        name="Correctness",
        criteria="Determine if the 'actual output' is correct based on the 'expected output'.",
        evaluation_params=[LLMTestCaseParams.ACTUAL_OUTPUT, LLMTestCaseParams.EXPECTED_OUTPUT],
        threshold=0.5
    )
    test_case = LLMTestCase(
        input="What if these shoes don't fit?",
        # Replace this with the actual output from your LLM application
        actual_output="You have 30 days to get a full refund at no extra cost.",
        expected_output="We offer a 30-day full refund at no extra costs.",
        retrieval_context=["All customers are eligible for a 30 day full refund at no extra costs."]
    )
    assert_test(test_case, [correctness_metric])
```

Set your `OPENAI_API_KEY` as an environment variable (you can also evaluate using your own custom model, for more details visit [this part of our docs](https://deepeval.com/docs/metrics-introduction#using-a-custom-llm?utm_source=GitHub)):

```
export OPENAI_API_KEY="..."
```

And finally, run `test_chatbot.py` in the CLI:

```
deepeval test run test_chatbot.py
```

**Congratulations! Your test case should have passed ✅** Let's breakdown what happened.

- The variable `input` mimics a user input, and `actual_output` is a placeholder for what your application's supposed to output based on this input.
- The variable `expected_out
... [TRUNCATED]
```

### File: docs\package.json
```json
{
  "name": "docs",
  "version": "0.0.0",
  "private": true,
  "scripts": {
    "docusaurus": "docusaurus",
    "start": "docusaurus start",
    "build": "docusaurus build",
    "swizzle": "docusaurus swizzle",
    "deploy": "docusaurus deploy",
    "clear": "docusaurus clear",
    "serve": "docusaurus serve",
    "write-translations": "docusaurus write-translations",
    "write-heading-ids": "docusaurus write-heading-ids"
  },
  "dependencies": {
    "@docusaurus/core": "^3.9.2",
    "@docusaurus/plugin-client-redirects": "^3.9.2",
    "@docusaurus/preset-classic": "^3.9.2",
    "@docusaurus/theme-mermaid": "^3.9.2",
    "@mdx-js/react": "3",
    "clsx": "^1.2.1",
    "docusaurus-plugin-sass": "^0.2.5",
    "font-awesome": "^4.7.0",
    "lucide-react": "^0.526.0",
    "posthog-docusaurus": "^2.0.2",
    "posthog-js": "^1.206.1",
    "prism-react-renderer": "2",
    "react": "18",
    "react-dom": "18",
    "react-player": "^2.16.0",
    "rehype-katex": "6",
    "remark-math": "5",
    "sass": "^1.76.0",
    "zwitch": "^2.0.4"
  },
  "devDependencies": {
    "@docusaurus/module-type-aliases": "^3.9.2",
    "@docusaurus/tsconfig": "^3.9.2",
    "@types/react": "^19.2.14",
    "@types/react-router-dom": "^5.3.3",
    "css-loader": "^7.1.2",
    "prettier": "^3.5.3",
    "style-loader": "^4.0.0",
    "typescript": "^6.0.2"
  },
  "browserslist": {
    "production": [
      ">0.5%",
      "not dead",
      "not op_mini all"
    ],
    "development": [
      "last 1 chrome version",
      "last 1 firefox version",
      "last 1 safari version"
    ]
  },
  "engines": {
    "node": ">=18.0"
  }
}

```

### File: docs\README.md
```md
# Website

This website is built using [Docusaurus 2](https://docusaurus.io/), a modern static website generator.

### Installation

```
$ yarn
```

### Local Development

```
$ yarn start
```

This command starts a local development server and opens up a browser window. Most changes are reflected live without having to restart the server.

### Build

```
$ yarn build
```

This command generates static content into the `build` directory and can be served using any static contents hosting service.

### Deployment

Using SSH:

```
$ USE_SSH=true yarn deploy
```

Not using SSH:

```
$ GIT_USER=<Your GitHub username> yarn deploy
```

If you are using GitHub pages for hosting, this command is a convenient way to build the website and push to the `gh-pages` branch.

```

### File: .pre-commit-config.yaml
```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 24.8.0
    hooks:
      - id: black
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.6.9
    hooks:
      - id: ruff
        args: [--fix]   # auto-fix lint issues

```

### File: a.py
```py
from deepeval.tracing import (
    observe,
    update_current_span,
    update_current_trace,
    update_llm_span,
)
import asyncio
from deepeval.prompt import Prompt

prompt = Prompt(alias="Message Prompt")
prompt.pull()


@observe(
    type="llm",
    model="gemini-2.5-flash",
    cost_per_input_token=0.0000003,
    cost_per_output_token=0.0000025,
    metric_collection="default123",
)
async def meta_agent(query: str):
    update_current_span(
        input=query,
        output=query,
        expected_output=query,
        retrieval_context=[query],
        metadata={"query": query},
        name="meta_agent",
    )
    update_llm_span(
        input_token_count=10,
        output_token_count=10,
        # prompt=prompt,
    )
    update_current_trace(
        name="meta_agent",
        thread_id="fetch 11",
        input=query,
        output=query,
        expected_output=query,
        retrieval_context=[query],
        user_id="clickhouse user",
        tags=["test", "example"],
        metadata={"query": {"query": query}},
        test_case_id="ffb10651-010e-4d37-9947-b75324c31971",
    )
    return query


async def run_parallel_examples():
    tasks = [
        meta_agent("How tall is Mount Everest?"),
        # meta_agent("What's the capital of Brazil?"),
        # meta_agent("Who won the last World Cup?"),
        # meta_agent("Explain quantum entanglement."),
        # meta_agent("What's the latest iPhone model?"),
        # meta_agent("How do I cook a perfect steak?"),
        # meta_agent("Tell me a joke about robots."),
        # meta_agent("What causes lightning?"),
        # meta_agent("Who painted the Mona Lisa?"),
        # meta_agent("What's the population of Japan?"),
        # meta_agent("How do vaccines work?"),
        # meta_agent("Recommend a good sci-fi movie."),
    ]
    await asyncio.gather(*tasks)


asyncio.run(run_parallel_examples())

# # ############################################################
# # ############################################################
# # ############################################################

# from deepeval import evaluate
# from deepeval.metrics import AnswerRelevancyMetric
# from deepeval.test_case import LLMTestCase

# evaluate(
#     test_cases=[
#         LLMTestCase(
#             input="How tall is Mount Everest?",
#             actual_output="Mount Everest is 8,848 meters tall.",
#             expected_output="Mount Everest is 8,848 meters tall.",
#         ),
#     ],
#     metrics=[AnswerRelevancyMetric()],
# )

# ############################################################
# ############################################################
# ############################################################

# from deepeval import evaluate
# from deepeval.metrics import TurnRelevancyMetric
# from deepeval.test_case import ConversationalTestCase, Turn

# evaluate(
#     test_cases=[
#         ConversationalTestCase(
#             turns=[
#                 Turn(
#                     role="user",
#                     content="Hello, how are you?",
#                 ),
#                 Turn(
#                     role="assistant",
#                     content="I'm doing well, thanks for asking! How can I help you today?",
#                 ),
#                 Turn(
#                     role="user",
#                     content="Can you explain what answer relevancy means?",
#                 ),
#                 Turn(
#                     role="assistant",
#                     content=(
#                         "Answer relevancy measures how well a response directly addresses "
#                         "the user's question, focusing on usefulness and alignment with intent."
#                     ),
#                 ),
#             ],
#         ),
#     ],
#     metrics=[TurnRelevancyMetric()],
# )

######


# from deepeval.tracing import observe, update_current_trace
# from deepeval.metrics import AnswerRelevancyMetric
# from deepeval.dataset import EvaluationDataset
# from openai import OpenAI


# @observe()
# def llm_app(query: str) -> str:

#     @observe()
#     def retriever(query: str) -> list[str]:
#         chunks = ["List", "of", "text", "chunks"]
#         update_current_trace(retrieval_context=chunks)
#         return chunks

#     @observe(type="llm")
#     def generator(query: str, text_chunks: list[str]) -> str:
#         res = (
#             OpenAI()
#             .chat.completions.create(
#                 model="gpt-4o", messages=[{"role": "user", "content": query}]
#             )
#             .choices[0]
#             .message.content
#         )
#         update_current_trace(input=query, output=res)
#         return res

#     return generator(query, retriever(query))


# dataset = EvaluationDataset()
# dataset.pull(alias="Playground Dataset")

# for golden in dataset.evals_iterator(metrics=[AnswerRelevancyMetric()]):
#     llm_app(golden.input)

```

### File: CONTRIBUTING.md
```md
# Contributing to DeepEval 🥳

Thanks for thinking about contributing to DeepEval! We accept fixes, improvements, or even entire new features. Some reasons why you might want to contribute:

- there's a bug that you want fixed
- there's a cool new feature you're thinking about that might be useful for DeepEval
- there's a metric or benchmark that you want implemented
- there's room for improvement in the docs

## How to contribute

We follow fork and pull request workflow. To know more about it, check out this [guide](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork).

### Set up your development environment

1. Create a python virtual environment.
2. We recommend using Poetry to install dependencies. If you haven't already, see the [Poetry docs](https://python-poetry.org/docs/).
3. Install the dependencies using:

```bash
poetry install
```

## Our expectations (not a lot :)

To contribute, all we ask for is to follow existing patterns within the codebase. For example, if you're looking to add a new benchmark, look at how the different modules in the existing benchmarks are structured and implemented, and we encourage you to reuse helper functions and methods shared by similar modules.

Other than that, there are no strict rules to follow, except for optionally running `black` to ensure good formatting. Also, there's no need to worry about failing test cases in GitHub Actions, as these are mostly for internal use and will only pass if triggered by a user with the correct permissions within Confident AI.

Thank you and come ask any questions or discuss any new PRs you have in mind on our [Discord](https://discord.com/invite/a3K9c8GRGt)!


## Issue lifecycle & staleness policy

- **Stale closure:** We close issues with no activity for **≥ 12 months**.
- **Reopening:** If your issue is still relevant:

  1. Leave a comment mentioning one or more maintainers from [MAINTAINERS.md](./MAINTAINERS.md) and include any new details (version, repro steps, logs).
  2. If you don’t get a response in a few days, open a **new issue** and reference the old one.

**Exclusions:** Labeled issues.

**Why:** Keeps the tracker actionable and reflects the current roadmap. If your issue still matters, please comment and we’ll re-open.

```

### File: LICENSE.md
```md

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

   Copyright [2024] [Confident AI Inc.]

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

### File: MAINTAINERS.md
```md
# Maintainers

For issues in this repo you can mention one or more of:

- @trevor-cai
- @A-Vamshi
- @jeffreyip
- @kritinv

```

### File: docs\babel.config.js
```js
module.exports = {
  presets: [require.resolve("@docusaurus/core/lib/babel/preset")],
};

```

### File: docs\docusaurus.config.ts
```ts
import type { Config } from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
import { themes as prismThemes } from 'prism-react-renderer';

const config: Config = {
  plugins: [
    'docusaurus-plugin-sass',
    [
      '@docusaurus/plugin-content-docs',
      {
        id: 'tutorials',
        path: 'tutorials',
        routeBasePath: 'tutorials',
        sidebarPath: require.resolve('./sidebarTutorials.js'),
        editUrl: 'https://github.com/confident-ai/deepeval/edit/main/docs/',
        showLastUpdateAuthor: true,
        showLastUpdateTime: true,
      },
    ],
    [
      '@docusaurus/plugin-content-docs',
      {
        id: 'guides',
        path: 'guides',
        routeBasePath: 'guides',
        sidebarPath: require.resolve('./sidebarGuides.js'),
        editUrl: 'https://github.com/confident-ai/deepeval/edit/main/docs/',
        showLastUpdateAuthor: true,
        showLastUpdateTime: true,
      },
    ],
    [
      '@docusaurus/plugin-content-docs',
      {
        id: 'integrations',
        path: 'integrations',
        routeBasePath: 'integrations',
        sidebarPath: require.resolve('./sidebarIntegrations.js'),
        editUrl: 'https://github.com/confident-ai/deepeval/edit/main/docs/',
        showLastUpdateAuthor: true,
        showLastUpdateTime: true,
      },
    ],
    [
      '@docusaurus/plugin-content-docs',
      {
        id: 'changelog',
        path: 'changelog',
        routeBasePath: 'changelog',
        sidebarPath: require.resolve('./sidebarChangelog.js'),
        editUrl: 'https://github.com/confident-ai/deepeval/edit/main/docs/',
        showLastUpdateAuthor: true,
        showLastUpdateTime: true,
      },
    ],
    [
      "@docusaurus/plugin-content-blog",
      {
        id: "blogs",
        path: "blog",
        routeBasePath: "blog",
        blogSidebarCount: 0, 
      },
    ],
  ],

  title: 'DeepEval by Confident AI - The LLM Evaluation Framework',
  tagline: 'Evaluation Framework for LLMs',
  favicon: 'img/favicon.ico',

  url: 'https://deepeval.com',
  baseUrl: '/',

  onBrokenLinks: 'warn',
  onBrokenMarkdownLinks: 'warn',

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      '@docusaurus/preset-classic',
      {
        // blog: {
        //   blogTitle: 'DeepEval Blog',
        //   blogDescription: 'The official LLM evaluation blog',
        //   blogSidebarCount: 'ALL',
        // },
        blog: false,
        docs: {
          path: 'docs',
          editUrl: 'https://github.com/confident-ai/deepeval/edit/main/docs/',
          showLastUpdateAuthor: true,
          showLastUpdateTime: true,
          sidebarPath: require.resolve('./sidebars.js'),
          remarkPlugins: [remarkMath],
          rehypePlugins: [rehypeKatex],
        },
        theme: {
          customCss: require.resolve('./src/css/custom.scss'),
        },
        gtag: {
          trackingID: 'G-N2EGDDYG9M',
          anonymizeIP: false,
        },
      } satisfies Preset.Options, // <-- Type checking applied here
    ],
  ],
  themes: ['@docusaurus/theme-mermaid'],
  markdown: {
    mermaid: true,
  },
  scripts: [
    {
      src: 'https://plausible.io/js/script.tagged-events.js',
      defer: true,
      'data-domain': 'deepeval.com',
    },
    {
      src: "https://widget.kapa.ai/kapa-widget.bundle.js",
      "data-website-id": "a3177869-c654-4b86-9c92-e4b4416f66e0",
      "data-project-name": "DeepEval",
      "data-button-position-bottom": "2rem",
      "data-button-position-right": "2rem",
      "data-project-color": "#fff",
      "data-button-text-color": "#000",
      "data-project-logo": "https://pbs.twimg.com/profile_images/1888060560161574912/qbw1-_2g_400x400.png",
      "data-modal-title": "Ask DeepEval",
      "data-modal-disclaimer": "All the following results are AI generated, if you can't find the solution you're looking for, ping us in [Discord](https://discord.gg/a3K9c8GRGt) we'd be happy to have you!",
      "data-modal-example-questions": "Can I create a dataset using my knowledge base?, Can I create a custom metrics for my use-case?",
      "data-uncertain-answer-callout": "It would be better to ask this question directly in DeepEval's [Discord](https://discord.gg/a3K9c8GRGt) channel.",
      async: true,
    },
  ],
  stylesheets: [
    {
      href: 'https://cdn.jsdelivr.net/npm/katex@0.13.24/dist/katex.min.css',
      type: 'text/css',
      integrity:
        'sha384-odtC+0UGzzFL/6PNoE8rX/SPcQDXBJ+uRepguP4QkPCm2LBxH3FA3y+fKSiJ+AmM',
      crossorigin: 'anonymous',
    },
    {
      href: 'https://fonts.googleapis.com/css2?family=Lexend+Deca:wght@500&display=swap',
      type: 'text/css',
    },
  ],
  headTags: [
    {
      tagName: 'script',
      attributes: {
        type: 'application/ld+json',
      },
      innerHTML: JSON.stringify({
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": "DeepEval by Confident AI",
        "alternateName": "DeepEval - The LLM Evaluation Framework",
        "url": "https://deepeval.com",
        "logo": "https://deepeval.com/icons/DeepEval.svg",
        "sameAs": [
          "https://github.com/confident-ai/deepeval",
          "https://x.com/deepeval",
          "https://discord.gg/a3K9c8GRGt",
        ]
      }),
    },
  ],
  themeConfig: {
    image: 'img/social_card.png',
    navbar: {
      logo: {
        alt: 'DeepEval Logo',
        src: 'icons/DeepEval.svg',
      },
      items: [
        {
          to: 'docs/getting-started',
          position: 'left',
          label: 'Docs',
          activeBasePath: 'docs',
        },
        {
          to: 'guides/guides-ai-agent-evaluation',
          position: 'left',
          label: 'Guides',
          activeBasePath: 'guides',
        },
        {
          to: 'tutorials/tutorial-introduction',
          position: 'left',
          label: 'Tutorials',
          activeBasePath: 'tutorials',
        },
        {
          to: 'integrations/models/openai',
          position: 'left',
          label: 'Integrations',
          activeBasePath: 'integrations',
        },
        { to: 'blog', label: 'Blog', position: 'left' },
        {
          to: 'changelog',
          position: 'left',
          label: 'Changelog',
          activeBasePath: 'changelog',
        },
        {
          href: 'https://www.confident-ai.com/docs',
          position: 'left',
          label: 'Cloud Docs',
        },
        {
          href: 'https://discord.gg/a3K9c8GRGt',
          className: 'header-discord-link',
          position: 'right',
        },
        {
          href: 'https://github.com/confident-ai/deepeval',
          position: 'right',
          className: 'header-github-link',
        },
        {
          href: 'https://x.com/deepeval',
          className: 'header-twitter-link',
          position: 'right',
        },
      ],
    },
    algolia: {
      appId: '7U9PQIW1ZA',
      apiKey: 'fb799aeac8bcd0f6b9e0e233a385ad33',
      indexName: 'confident-ai',
      contextualSearch: true,
    },
    colorMode: {
      defaultMode: 'light',
      disableSwitch: false,
      respectPrefersColorScheme: false,
    },
    announcementBar: {
      id: 'announcementBar-1',
      content:
        '⭐️ If you like DeepEval, give it a star on <a target="_blank" rel="noopener noreferrer" href="https://github.com/confident-ai/deepeval">GitHub</a>! ⭐️',
      backgroundColor: '#fff',
      textColor: '#091E42',
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Documentation',
          items: [
            { label: 'Introduction', to: '/docs/getting-started' },
            { label: 'Confident AI', to: 'https://www.confident-ai.com/docs' },
            { label: 'Tutorials', to: '/tutorials/tutorial-introduction' },
            { label: 'Guides', to: '/guides/guides-ai-agent-evaluation' },
          ],
        },
        {
          title: 'Articles You Must Read',
          items: [
            {
              label: 'LLM evaluation metrics',
              to: 'https://www.confident-ai.com/blog/llm-evaluation-metrics-everything-you-need-for-llm-evaluation',
            },
            {
              label: 'LLM-as-a-judge',
              to: 'https://www.confident-ai.com/blog/why-llm-as-a-judge-is-the-best-llm-evaluation-method',
            },
            {
              label: 'LLM testing',
              to: 'https://www.confident-ai.com/blog/llm-testing-in-2024-top-methods-and-strategies',
            },
            {
              label: 'LLM chatbot evaluation',
              to: 'https://www.confident-ai.com/blog/llm-chatbot-evaluation-explained-top-chatbot-evaluation-metrics-and-testing-techniques',
            },
          ],
        },
        {
          title: 'Evaluation Community',
          items: [
            { label: 'GitHub', to: 'https://github.com/confident-ai/deepeval' },
            { label: 'Discord', to: 'https://discord.gg/a3K9c8GRGt' },
            { label: 'Newsletter', to: 'https://confident-ai.com/blog' },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Confident AI Inc. Built with ❤️ and confidence.`,
    },
    prism: {
      theme: prismThemes.nightOwl,
      additionalLanguages: ['python'],
      magicComments: [
        {
          className: 'theme-code-block-highlighted-line',
          line: 'highlight-next-line',
          block: { start: 'highlight-start', end: 'highlight-end' },
        },
        {
          className: 'code-block-error-message',
          line: 'highlight-next-line-error-message',
        },
        {
          className: 'code-block-info-line',
          line: 'highlight-next-line-info',
          block: {
            start: 'highlight-info-start',
            end: 'highlight-info-end',
          },
        },
      ],
    },
  } satisfies Preset.ThemeConfig,
};

export default config;

```

### File: docs\sidebarChangelog.ts
```ts
module.exports = {
  changelog: [
    {
      type: 'category',
      label: 'Changelog',
      className: 'sidebar-item-icon-changelog',
      link: { type: 'doc', id: 'changelog' },
      collapsed: false,
      items: [
        {
          type: 'category',
          label: '🐴 2026',
          link: { type: 'doc', id: 'changelog-2026' },
          collapsed: false,
          items: [],
        },
        {
          type: 'category',
          label: '🐍 2025',
          link: { type: 'doc', id: 'changelog-2025' },
          collapsed: false,
          items: [
            {
              type: 'link',
              label: 'December',
              href: '/changelog/changelog-2025#december',
            },
            {
              type: 'link',
              label: 'November',
              href: '/changelog/changelog-2025#november',
            },
            {
              type: 'link',
              label: 'October',
              href: '/changelog/changelog-2025#october',
            },
            {
              type: 'link',
              label: 'September',
              href: '/changelog/changelog-2025#september',
            },
            {
              type: 'link',
              label: 'August',
              href: '/changelog/changelog-2025#august',
            },
            {
              type: 'link',
              label: 'July',
              href: '/changelog/changelog-2025#july',
            },
            {
              type: 'link',
              label: 'June',
              href: '/changelog/changelog-2025#june',
            },
            {
              type: 'link',
              label: 'May',
              href: '/changelog/changelog-2025#may',
            },
            {
              type: 'link',
              label: 'April',
              href: '/changelog/changelog-2025#april',
            },
            {
              type: 'link',
              label: 'March',
              href: '/changelog/changelog-2025#march',
            },
            {
              type: 'link',
              label: 'February',
              href: '/changelog/changelog-2025#february',
            },
            {
              type: 'link',
              label: 'January',
              href: '/changelog/changelog-2025#january',
            },
          ],
        },
        {
          type: 'category',
          label: '🐲 2024',
          link: { type: 'doc', id: 'changelog-2024' },
          collapsed: true,
          items: [
            {
              type: 'link',
              label: 'December',
              href: '/changelog/changelog-2024#december',
            },
            {
              type: 'link',
              label: 'November',
              href: '/changelog/changelog-2024#november',
            },
            {
              type: 'link',
              label: 'October',
              href: '/changelog/changelog-2024#october',
            },
            {
              type: 'link',
              label: 'September',
              href: '/changelog/changelog-2024#september',
            },
            {
              type: 'link',
              label: 'August',
              href: '/changelog/changelog-2024#august',
            },
            {
              type: 'link',
              label: 'July',
              href: '/changelog/changelog-2024#july',
            },
            {
              type: 'link',
              label: 'June',
              href: '/changelog/changelog-2024#june',
            },
            {
              type: 'link',
              label: 'May',
              href: '/changelog/changelog-2024#may',
            },
            {
              type: 'link',
              label: 'April',
              href: '/changelog/changelog-2024#april',
            },
            {
              type: 'link',
              label: 'March',
              href: '/changelog/changelog-2024#march',
            },
            {
              type: 'link',
              label: 'February',
              href: '/changelog/changelog-2024#february',
            },
            {
              type: 'link',
              label: 'January',
              href: '/changelog/changelog-2024#january',
            },
          ],
        },
      ],
    },
  ],
};

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
