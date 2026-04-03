---
id: github.com-minimaxir-simpleaichat-304c4d91-knowled
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:27:59.739172
---

# KNOWLEDGE EXTRACT: github.com_minimaxir_simpleaichat_304c4d91
> **Extracted on:** 2026-04-01 14:03:21
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007523626/github.com_minimaxir_simpleaichat_304c4d91

---

## File: `.gitignore`
```
.env
.DS_Store
test_notebooks/
.vscode/
__pycache__/
.ipynb_checkpoints
simpleaichat.egg-info/
dist/
build/
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2023-2024 Max Woolf

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## File: `PROMPTS.md`
```markdown
# Prompts

Here are explanations of the base prompts that simpleaichat uses, and why they are written as they are. These prompts are optimized both for conciseness and effectiveness with ChatGPT/`gpt-3.5-turbo`. This includes some postprocessing of the inputs.

## Interactive Chat

When providing only a character, the `system` chat for the interactive chat becomes:

```txt
You must follow ALL these rules in all responses:
- You are the following character and should ALWAYS act as them: {0}
- NEVER speak in a formal tone.
- Concisely introduce yourself first in character.
```

The `{0}` performs a `wikipedia_search_lookup` (specified in utils.py) to search for and return the first sentence of the associated page on Wikipedia, if present. This creates more alignment with the expected character. If the second parameter is specified to force a speaking voice, it will be added to the list of rules.

Example for `GLaDOS` and `Speak in the style of a Seinfeld monologue`:

```txt
You must follow ALL these rules in all responses:
- You are the following character and should ALWAYS act as them: GLaDOS (Genetic Lifeform and Disk Operating System) is a fictional character from the video game series Portal.
- NEVER speak in a formal tone.
- Concisely introduce yourself first in character.
- Speak in the style of a Seinfeld monologue
```

You can use the formatted prompt as a normal `system` prompt for any other simpleaichat context.

## Tools

Invoking a tool invokes two separate API calls: one to select which tool which then provides additional **context**, and another call to generate based on that context, plus previous messages in the conversation.

### Call #1

Before returning an API response, the `system` prompt is temporairly replaced with:

```txt
From the list of tools below:
- Reply ONLY with the number of the tool appropriate in response to the user's last message.
- If no tool is appropriate, ONLY reply with "0".

{tools}
```

Formatted example from the README:

```
From the list of tools below:
- Reply ONLY with the number of the tool appropriate in response to the user's last message.
- If no tool is appropriate, ONLY reply with "0".

1. Search the internet
2. Lookup more information about a topic.
```

This utilizes a few tricks:

- The call sets `{"max_tokens": 1}` so it will only output one number (hence there is a hard limit of 9 tools), which makes it more cost and speed efficient than other implementations.
- Unique to ChatGPT is also specifying a `logit_bias` with a high enough weight to make it such that the model can _only_ output numbers between 0 and {num_tools}, up to 9. (specifically, tokenizer indices 15-24 inclusive correspond to the numerals `0-9` in ChatGPT, which can be verified using `tiktoken`)
- The numbers map 1:1 to the indicies of the input arrays of tools, so there never can be parsing errors as can be common with LangChain.

The numeral is matched with the appropriate function.

### Call 2

The second call prepends the context from the tool to the prompt, and temporairly adds a command to the `system` prompt, to leverage said added context without losing the persona otherwise specified in the `system` prompt:

System prompt:

```
You MUST use information from the context in your response.
```

User message:

```txt
Context: {context}

User:
```

Formatted example from the README:

```
You are a helpful assistant.

You MUST use information from the context in your response.
```

```
Context: Fisherman's Wharf, San Francisco, Tourist attractions in the United States, Lombard Street (San Francisco)

User: San Francisco tourist attractions
```
```

## File: `README.md`
```markdown
# simpleaichat

```py3
from simpleaichat import AIChat

ai = AIChat(system="Write a fancy GitHub README based on the user-provided project name.")
ai("simpleaichat")
```

simpleaichat is a Python package for easily interfacing with chat apps like ChatGPT and GPT-4 with robust features and minimal code complexity. This tool has many features optimized for working with ChatGPT as fast and as cheap as possible, but still much more capable of modern AI tricks than most implementations:

- Create and run chats with only a few lines of code!
- Optimized workflows which minimize the amount of tokens used, reducing costs and latency.
- Run multiple independent chats at once.
- Minimal codebase: no code dives to figure out what's going on under the hood needed!
- Chat streaming responses and the ability to use tools.
- Async support, including for streaming and tools.
- Ability to create more complex yet clear workflows if needed, such as Agents. (Demo soon!)
- Coming soon: more chat model support (PaLM, Claude)!

Here's some fun, hackable examples on how simpleaichat works:

- Creating a [Python coding assistant](examples/notebooks/simpleaichat_coding.ipynb) without any unnecessary accompanying output, allowing 5x faster generation at 1/3rd the cost. ([Colab](https://colab.research.google.com/github/minimaxir/simpleaichat/blob/main/examples/notebooks/simpleaichat_coding.ipynb))
- Allowing simpleaichat to [provide inline tips](examples/notebooks/chatgpt_inline_tips.ipynb) following ChatGPT usage guidelines. ([Colab](https://colab.research.google.com/github/minimaxir/simpleaichat/blob/main/examples/notebooks/chatgpt_inline_tips.ipynb))
- Async interface for [conducting many chats](examples/notebooks/simpleaichat_async.ipynb) in the time it takes to receive one AI message. ([Colab](https://colab.research.google.com/github/minimaxir/simpleaichat/blob/main/examples/notebooks/simpleaichat_async.ipynb))
- Create your own Tabletop RPG (TTRPG) setting and campaign by using [advanced structured data models](examples/notebooks/schema_ttrpg.ipynb). ([Colab](https://colab.research.google.com/github/minimaxir/simpleaichat/blob/main/examples/notebooks/schema_ttrpg.ipynb))

## Installation

simpleaichat can be installed [from PyPI](https://pypi.org/project/simpleaichat/):

```sh
pip3 install simpleaichat
```

## Quick, Fun Demo

You can demo chat-apps very quickly with simpleaichat! First, you will need to get an OpenAI API key, and then with one line of code:

```py3
from simpleaichat import AIChat

AIChat(api_key="sk-...")
```

And with that, you'll be thrust directly into an interactive chat!

![](docs/helloworld.png)

This AI chat will mimic the behavior of OpenAI's webapp, but on your local computer!

You can also pass the API key by storing it in an `.env` file with a `OPENAI_API_KEY` field in the working directory (recommended), or by setting the environment variable of `OPENAI_API_KEY` directly to the API key.

But what about creating your own custom conversations? That's where things get fun. Just input whatever person, place or thing, fictional or nonfictional, that you want to chat with!

```py3
AIChat("GLaDOS")  # assuming API key loaded via methods above
```

![](docs/glados.png)

But that's not all! You can customize exactly how they behave too with additional commands!

```py3
AIChat("GLaDOS", "Speak in the style of a Seinfeld monologue")
```

![](docs/gladoseinfeld.png)

```py3
AIChat("Ronald McDonald", "Speak using only emoji")
```

![](docs/clownemoji.png)

Need some socialization immediately? Once simpleaichat is installed, you can also start these chats directly from the command line!

```sh
simpleaichat
simpleaichat "GlaDOS"
simpleaichat "GLaDOS" "Speak in the style of a Seinfeld monologue"
```

## Building AI-based Apps

The trick with working with new chat-based apps that wasn't readily available with earlier iterations of GPT-3 is the addition of the system prompt: a different class of prompt that guides the AI behavior throughout the entire conversation. In fact, the chat demos above are actually using [system prompt tricks](https://github.com/minimaxir/simpleaichat/blob/main/PROMPTS.md#interactive-chat) behind the scenes! OpenAI has also released an official guide for [system prompt best practices](https://platform.openai.com/docs/guides/gpt-best-practices) to building AI apps.

For developers, you can instantiate a programmatic instance of `AIChat` by explicitly specifying a system prompt, or by disabling the console.

```py3
ai = AIChat(system="You are a helpful assistant.")
ai = AIChat(console=False)  # same as above
```

You can also pass in a `model` parameter, such as `model="gpt-4"` if you have access to GPT-4, or `model="gpt-3.5-turbo-16k"` for a larger-context-window ChatGPT.

You can then feed the new `ai` class with user input, and it will return and save the response from ChatGPT:

```py3
response = ai("What is the capital of California?")
print(response)
```

```
The capital of California is Sacramento.
```

Alternatively, you can stream responses by token with a generator if the text generation itself is too slow:

```py3
for chunk in ai.stream("What is the capital of California?", params={"max_tokens": 5}):
    response_td = chunk["response"]  # dict contains "delta" for the new token and "response"
    print(response_td)
```

```
The
The capital
The capital of
The capital of California
The capital of California is
```

Further calls to the `ai` object will continue the chat, automatically incorporating previous information from the conversation.

```py3
response = ai("When was it founded?")
print(response)
```

```
Sacramento was founded on February 27, 1850.
```

You can also save chat sessions (as CSV or JSON) and load them later. The API key is not saved so you will have to provide that when loading.

```py3
ai.save_session()  # CSV, will only save messages
ai.save_session(format="json", minify=True)  # JSON

ai.load_session("my.csv")
ai.load_session("my.json")
```

### Functions

A large number of popular venture-capital-funded ChatGPT apps don't actually use the "chat" part of the model. Instead, they just use the system prompt/first user prompt as a form of natural language programming. You can emulate this behavior by passing a new system prompt when generating text, and not saving the resulting messages.

The `AIChat` class is a manager of chat _sessions_, which means you can have multiple independent chats or functions happening! The examples above use a default session, but you can create new ones by specifying a `id` when calling `ai`.

```py3
json = '{"title": "An array of integers.", "array": [-1, 0, 1]}'
functions = [
             "Format the user-provided JSON as YAML.",
             "Write a limerick based on the user-provided JSON.",
             "Translate the user-provided JSON from English to French."
            ]
params = {"temperature": 0.0, "max_tokens": 100}  # a temperature of 0.0 is deterministic

# We namespace the function by `id` so it doesn't affect other chats.
# Settings set during session creation will apply to all generations from the session,
# but you can change them per-generation, as is the case with the `system` prompt here.
ai = AIChat(id="function", params=params, save_messages=False)
for function in functions:
    output = ai(json, id="function", system=function)
    print(output)
```

```txt
title: "An array of integers."
array:
  - -1
  - 0
  - 1
```

```txt
An array of integers so neat,
With values that can't be beat,
From negative to positive one,
It's a range that's quite fun,
This JSON is really quite sweet!
```

```txt
{"titre": "Un tableau d'entiers.", "tableau": [-1, 0, 1]}
```

Newer versions of ChatGPT also support "[function calling](https://platform.openai.com/docs/guides/gpt/function-calling)", but the real benefit of that feature is the ability for ChatGPT to support structured input and/or output, which now opens up a wide variety of applications! simpleaichat streamlines the workflow to allow you to just pass an `input_schema` and/or an `output_schema`.

You can construct a schema using a [pydantic](https://docs.pydantic.dev/latest/) BaseModel.

```py3
from pydantic import BaseModel, Field

ai = AIChat(
    console=False,
    save_messages=False,  # with schema I/O, messages are never saved
    model="gpt-3.5-turbo-0613",
    params={"temperature": 0.0},
)

class get_event_metadata(BaseModel):
    """Event information"""

    description: str = Field(description="Description of event")
    city: str = Field(description="City where event occured")
    year: int = Field(description="Year when event occured")
    month: str = Field(description="Month when event occured")

# returns a dict, with keys ordered as in the schema
ai("First iPhone announcement", output_schema=get_event_metadata)
```

```txt
{'description': 'The first iPhone was announced by Apple Inc.',
 'city': 'San Francisco',
 'year': 2007,
 'month': 'January'}
```

See the [TTRPG Generator Notebook](examples/notebooks/schema_ttrpg.ipynb) for a more elaborate demonstration of schema capabilities.

### Tools

One of the most recent aspects of interacting with ChatGPT is the ability for the model to use "tools." As popularized by [LangChain](https://github.com/hwchase17/langchain), tools allow the model to decide when to use custom functions, which can extend beyond just the chat AI itself, for example retrieving recent information from the internet not present in the chat AI's training data. This workflow is analogous to ChatGPT Plugins.

Parsing the model output to invoke tools typically requires a number of shennanigans, but simpleaichat uses [a neat trick](https://github.com/minimaxir/simpleaichat/blob/main/PROMPTS.md#tools) to make it fast and reliable! Additionally, the specified tools return a `context` for ChatGPT to draw from for its final response, and tools you specify can return a dictionary which you can also populate with arbitrary metadata for debugging and postprocessing. Each generation returns a dictionary with the `response` and the `tool` function used, which can be used to set up workflows akin to [LangChain](https://github.com/hwchase17/langchain)-style Agents, e.g. recursively feed input to the model until it determines it does not need to use any more tools.

You will need to specify functions with docstrings which provide hints for the AI to select them:

```py3
from simpleaichat.utils import wikipedia_search, wikipedia_search_lookup

# This uses the Wikipedia Search API.
# Results from it are nondeterministic, your mileage will vary.
def search(query):
    """Search the internet."""
    wiki_matches = wikipedia_search(query, n=3)
    return {"context": ", ".join(wiki_matches), "titles": wiki_matches}

def lookup(query):
    """Lookup more information about a topic."""
    page = wikipedia_search_lookup(query, sentences=3)
    return page

params = {"temperature": 0.0, "max_tokens": 100}
ai = AIChat(params=params, console=False)

ai("San Francisco tourist attractions", tools=[search, lookup])
```

```txt
{'context': "Fisherman's Wharf, San Francisco, Tourist attractions in the United States, Lombard Street (San Francisco)",
 'titles': ["Fisherman's Wharf, San Francisco",
  'Tourist attractions in the United States',
  'Lombard Street (San Francisco)'],
 'tool': 'search',
 'response': "There are many popular tourist attractions in San Francisco, including Fisherman's Wharf and Lombard Street. Fisherman's Wharf is a bustling waterfront area known for its seafood restaurants, souvenir shops, and sea lion sightings. Lombard Street, on the other hand, is a famous winding street with eight hairpin turns that attract visitors from all over the world. Both of these attractions are must-sees for anyone visiting San Francisco."}
```

```py3
ai("Lombard Street?", tools=[search, lookup])
```

```
{'context': 'Lombard Street is an east–west street in San Francisco, California that is famous for a steep, one-block section with eight hairpin turns. Stretching from The Presidio east to The Embarcadero (with a gap on Telegraph Hill), most of the street\'s western segment is a major thoroughfare designated as part of U.S. Route 101. The famous one-block section, claimed to be "the crookedest street in the world", is located along the eastern segment in the Russian Hill neighborhood.',
 'tool': 'lookup',
 'response': 'Lombard Street is a famous street in San Francisco, California known for its steep, one-block section with eight hairpin turns. It stretches from The Presidio to The Embarcadero, with a gap on Telegraph Hill. The western segment of the street is a major thoroughfare designated as part of U.S. Route 101, while the famous one-block section, claimed to be "the crookedest street in the world", is located along the eastern segment in the Russian Hill'}
```

```py3
ai("Thanks for your help!", tools=[search, lookup])
```

```txt
{'response': "You're welcome! If you have any more questions or need further assistance, feel free to ask.",
 'tool': None}
```

## Miscellaneous Notes

- Like [gpt-2-simple](https://github.com/minimaxir/gpt-2-simple) before it, the primary motivation behind releasing simpleaichat is to both democratize access to ChatGPT even more and also offer more transparency for non-engineers into how Chat AI-based apps work under the hood given the disproportionate amount of media misinformation about their capabilities. This is inspired by real-world experience from [my work with BuzzFeed](https://tech.buzzfeed.com/the-right-tools-for-the-job-c05de96e949e) in the domain, where after spending a long time working with the popular [LangChain](https://github.com/hwchase17/langchain), a more-simple implementation was both much easier to maintain and resulted in much better generations. I began focusing development on simpleaichat after reading a [Hacker News thread](https://news.ycombinator.com/item?id=35820931) filled with many similar complaints, indicating value for an easier-to-use interface for modern AI tricks.
  - simpleaichat very intentionally avoids coupling features with common use cases where possible (e.g. Tools) in order to avoid software lock-in due to the difficulty implementing anything not explicitly mentioned in the project's documentation. The philosophy behind simpleaichat is to provide good demos, and let the user's creativity and business needs take priority instead of having to fit a round peg into a square hole like with LangChain.
  - simpleaichat makes it easier to interface with Chat AIs, but it does not attempt to solve common technical and ethical problems inherent to large language models trained on the internet, including prompt injection and unintended plagiarism. The user should exercise good judgment when implementing simpleaichat. Use cases of simpleaichat which go against OpenAI's [usage policies](https://openai.com/policies/usage-policies) (including jailbreaking) will not be endorsed.
  - simpleaichat intentionally does not use the "Agent" logical metaphor for tool workflows because it's become an AI hype buzzword heavily divorced from its origins. If needed be, you can emulate the Agent workflow with a `while` loop without much additional code, plus with the additional benefit of much more flexibility such as debugging.
- The session manager implements some sensible security defaults, such as using UUIDs as session ids by default, storing authentication information in a way to minimize unintentional leakage, and type enforcement via Pydantic. Your end-user application should still be aware of potential security issues, however.
- Although OpenAI's documentation says that system prompts are less effective than a user prompt constructed in a similar manner, in my experience it still does perform better for maintaining rules/a persona.
- Many examples of popular prompts use more conversational prompts, while the example prompts here use more consise and imperative prompts. This aspect of prompt engineering is still evolving, but in my experience commands do better with ChatGPT and with greater token efficieny. That's also why simpleaichat allows users to specify system prompts (and explicitly highlights what the default use) instead of relying on historical best practices.
- Token counts for async is not supported as OpenAI doesn't return token counts when streaming responses. In general, there may be some desync in token counts and usage for various use cases; I'm working on categorizing them.
- Outside of the explicit examples, none of this README uses AI-generated text. The introduction code example is just a joke, but it was too good of a real-world use case!

## Roadmap

- PaLM Chat (Bard) and Anthropic Claude support
- More fun/feature-filled CLI chat app based on Textual
- Simple example of using simpleaichat in a webapp
- Simple of example of using simpleaichat in a stateless manner (e.g. AWS Lambda functions)

## Maintainer/Creator

Max Woolf ([@minimaxir](https://minimaxir.com))

_Max's open-source projects are supported by his [Patreon](https://www.patreon.com/minimaxir) and [GitHub Sponsors](https://github.com/sponsors/minimaxir). If you found this project helpful, any monetary contributions to the Patreon are appreciated and will be put to good creative use._

## License

MIT
```

## File: `setup.py`
```python
from setuptools import setup

setup(
    name="simpleaichat",
    packages=["simpleaichat"],  # this must be the same as the name above
    version="0.2.2",
    description="A Python package for easily interfacing with chat apps, with robust features and minimal code complexity.",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Max Woolf",
    author_email="max@minimaxir.com",
    url="https://github.com/minimaxir/simpleaichat",
    keywords=["chatgpt", "openai", "text generation", "ai"],
    classifiers=[],
    license="MIT",
    entry_points={
        "console_scripts": ["simpleaichat=simpleaichat.cli:interactive_chat"]
    },
    python_requires=">=3.8",
    install_requires=[
        "pydantic>=2.0",
        "fire>=0.3.0",
        "httpx>=0.24.1",
        "python-dotenv>=1.0.0",
        "orjson>=3.9.0",
        "rich>=13.4.1",
        "python-dateutil>=2.8.2",
    ],
)
```

## File: `examples/contrib/endless_exquisite_corpse.py`
```python
import uuid
import time
import argparse
from simpleaichat import AIChat

SYSTEM_DEFAULT = "Write a short single line that continues the line."

ai = AIChat(console=False)


class ExquisiteCorpse:
    """
    Endless exquisite corpse generator
    """
    def __init__(self, seed, system=SYSTEM_DEFAULT, temp=2, last_n_words=None):
        self.last_seed = seed
        self.last_n_words = last_n_words
        self.system = system
        self.temp = temp
        self.total_tokens = 0

    def __iter__(self):
        return self

    def __next__(self):
        _id = uuid.uuid4()
        ai.new_session(id=_id, system=self.system, params={"temperature": self.temp})
        seed = " ".join(self.last_seed.split(" ")[-self.last_n_words:]) if self.last_n_words else self.last_seed
        response = ai(seed, id=_id)
        self.total_tokens += ai.message_totals("total_length", id=_id)
        ai.delete_session(id=_id)
        self.last_seed = response
        return response


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Endless exquisite corpse generator")
    parser.add_argument("seed", help="Initial seed")
    parser.add_argument("--system", default=SYSTEM_DEFAULT, help="System name")
    parser.add_argument("--temp", type=float, default=1, help="Temperature")
    parser.add_argument("--delay", type=float, default=15, help="Delay between lines in seconds")
    parser.add_argument("--last_n_words", type=int, help="Number of words to use from last line")
    args = parser.parse_args()
    
    corpse = ExquisiteCorpse(
        args.seed,
        system=args.system,
        temp=args.temp,
        last_n_words=args.last_n_words,
    )

    try:
        print(args.seed)
        for line in corpse:
            print(line)
            time.sleep(args.delay)
    except KeyboardInterrupt:
        print()
        print(f"Total tokens used: {corpse.total_tokens}")
```

## File: `examples/notebooks/chatgpt_inline_tips.ipynb`
```
{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "aBj_0vRigiH7"
      },
      "source": [
        "# ChatGPT Inline Tips with simpleaichat\n",
        "\n",
        "[simpleaichat](https://github.com/minimaxir/simpleaichat) allows the user more control over text inputs and output. One way to do it is to analyze user input for potential issues, and display a warning if there are unexpected issues with the input.\n",
        "\n",
        "Inspired by Simon Willison's blog post [ChatGPT should include inline tips\n",
        "](https://simonwillison.net/2023/May/30/chatgpt-inline-tips/).\n",
        "\n",
        "**DISCLAIMER: This is far from a perfect solution, but a good proof-of-concept on how to use simpleaichat to address complex problems.**"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "kqL3etKLgiH9"
      },
      "outputs": [],
      "source": [
        "!pip install -q simpleaichat\n",
        "\n",
        "from simpleaichat import AIChat\n",
        "from rich.console import Console\n",
        "from getpass import getpass\n",
        "import time"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "For the following cell, input your OpenAI API key when prompted. **It will not be saved to the notebook.**."
      ],
      "metadata": {
        "id": "zld11X3xgr1O"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "api_key = getpass(\"OpenAI Key: \")"
      ],
      "metadata": {
        "id": "xueo1SmCg2SF",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "92589df7-05d7-4d28-a163-acd805dbdb9a"
      },
      "execution_count": 2,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "OpenAI Key: ··········\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Let's create an AI chat, and a Console for output to the notebook."
      ],
      "metadata": {
        "id": "2O_1CUGVg8Y4"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "id": "d4o0elPQgiH-"
      },
      "outputs": [],
      "source": [
        "ai = AIChat(api_key=api_key, console=False, params={\"temperature\": 0.0})  # for reproducibility\n",
        "console = Console(width=60, highlight=False)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "xAPziFs-giH-"
      },
      "source": [
        "First, we'll set a list of rules that we can display. These rules are adapted from real-world incidents and OpenAI's [usage policies](https://openai.com/policies/usage-policies)."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "id": "RLzlzbBrgiH-"
      },
      "outputs": [],
      "source": [
        "tips = [\n",
        "    \"This ChatGPT model does not have access to the internet, and its training data cut-off is September 2021.\",\n",
        "    \"ChatGPT should not be relied on for legal research of this nature, because it is very likely to invent realistic cases that do not exist.\",\n",
        "    \"Medical and psychatric advice from ChatGPT should not be relied upon. Always consult a doctor.\",\n",
        "    \"Tailored financial advice from ChatGPT should not be relied upon. Always consult a professional.\",\n",
        "    \"ChatGPT is not liable for any illegal activies committed as the result of its responses.\"\n",
        "]"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "b6q0JBoGgiH_"
      },
      "source": [
        "When generating a response from ChatGPT, we'll first check the user input against a bespoke function in a different context to see if ChatGPT can detect one of the issues above. This is accomplished through a system prompt, and forcing the model to choose a number between `1` and `5`, or `0` if nothing is present.\n",
        "\n",
        "The order of the tips above matches the order of the list. This is incidentially the same workflow as tools in simpleaichat."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {
        "id": "-C2Rp02igiH_"
      },
      "outputs": [],
      "source": [
        "tips_prompt = \"\"\"From the list of topics below, reply ONLY with the number appropriate for describing the topic of the user's message. If none are, ONLY reply with \"0\".\n",
        "\n",
        "1. Content after September 2021\n",
        "2. Legal/Judicial Research\n",
        "3. Medical/Psychatric Advice\n",
        "4. Financial Advice\n",
        "5. Illegal/Unethical Activies\"\"\""
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 6,
      "metadata": {
        "id": "HzLh4Q6JgiH_"
      },
      "outputs": [],
      "source": [
        "# ensures tips output will always be an integer between 0 and 5 inclusive\n",
        "params = {\n",
        "    \"temperature\": 0.0,\n",
        "    \"max_tokens\": 1,\n",
        "    \"logit_bias\": {str(k): 100 for k in range(15, 15 + len(tips) + 1)}\n",
        "}\n",
        "\n",
        "# functional\n",
        "ai.new_session(id=\"tips\",\n",
        "               api_key=api_key,\n",
        "               system=tips_prompt,\n",
        "               save_messages=False,\n",
        "               params=params)\n",
        "\n",
        "def check_user_input(message):\n",
        "    tip_idx = ai(message, id=\"tips\")\n",
        "    if tip_idx == \"0\":  # no tip needed\n",
        "        return\n",
        "    else:\n",
        "        tip = tips[int(tip_idx) - 1]\n",
        "        console.print(f\"⚠️ {tip}\", style=\"bold\")"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "5raNhn8igiIA"
      },
      "source": [
        "Let's test it in a conversation!"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 11,
      "metadata": {
        "scrolled": false,
        "id": "DP3z0wIWgiIA",
        "outputId": "070fcfa9-016a-4abe-f15b-a094f525c4a2",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        }
      },
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "\u001b[1mYou:\u001b[0m "
            ],
            "text/html": [
              "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"font-weight: bold\">You:</span> </pre>\n"
            ]
          },
          "metadata": {}
        },
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Can you tell me more about Max v. Woolf?\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "\u001b[1m⚠️ ChatGPT should not be relied on for legal research of this\u001b[0m\n",
              "\u001b[1mnature, because it is very likely to invent realistic cases \u001b[0m\n",
              "\u001b[1mthat do not exist.\u001b[0m\n"
            ],
            "text/html": [
              "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"font-weight: bold\">⚠️ ChatGPT should not be relied on for legal research of this</span>\n",
              "<span style=\"font-weight: bold\">nature, because it is very likely to invent realistic cases </span>\n",
              "<span style=\"font-weight: bold\">that do not exist.</span>\n",
              "</pre>\n"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "\u001b[1;95mChatGPT\u001b[0m\u001b[95m: Max v. Woolf is a legal case that took place in the\u001b[0m\n",
              "\u001b[95mUnited Kingdom in 2017. It involved a dispute between two \u001b[0m\n",
              "\u001b[95mauthors, Max and Woolf, over the alleged plagiarism of Max's\u001b[0m\n",
              "\u001b[95mwork by Woolf. Max claimed that Woolf had copied significant\u001b[0m\n",
              "\u001b[95mportions of his book without permission or attribution.\u001b[0m\n",
              "\n",
              "\u001b[95mThe case was heard in the High Court of Justice in London, \u001b[0m\n",
              "\u001b[95mwhere Max presented evidence of the similarities between his\u001b[0m\n",
              "\u001b[95mwork and Woolf's. Woolf denied the allegations and argued \u001b[0m\n",
              "\u001b[95mthat any similarities were coincidental or the result of \u001b[0m\n",
              "\u001b[95mcommon themes in the genre.\u001b[0m\n",
              "\n",
              "\u001b[95mAfter a lengthy trial, the judge ruled in favor of Max, \u001b[0m\n",
              "\u001b[95mfinding that Woolf had indeed plagiarized his work. Woolf \u001b[0m\n",
              "\u001b[95mwas ordered to pay damages to Max and to publicly \u001b[0m\n",
              "\u001b[95macknowledge the plagiarism.\u001b[0m\n",
              "\n",
              "\u001b[95mThe case received significant media attention and sparked a \u001b[0m\n",
              "\u001b[95mwider discussion about the issue of plagiarism in the \u001b[0m\n",
              "\u001b[95mpublishing industry. It also highlighted the importance of \u001b[0m\n",
              "\u001b[95mproper attribution and respect for intellectual property \u001b[0m\n",
              "\u001b[95mrights.\u001b[0m\n"
            ],
            "text/html": [
              "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"color: #ff00ff; text-decoration-color: #ff00ff; font-weight: bold\">ChatGPT</span><span style=\"color: #ff00ff; text-decoration-color: #ff00ff\">: Max v. Woolf is a legal case that took place in the</span>\n",
              "<span style=\"color: #ff00ff; text-decoration-color: #ff00ff\">United Kingdom in 2017. It involved a dispute between two </span>\n",
              "<span style=\"color: #ff00ff; text-decoration-color: #ff00ff\">authors, Max and Woolf, over the alleged plagiarism of Max's</span>\n",
              "<span style=\"color: #ff00ff; text-decoration-color: #ff00ff\">work by Woolf. Max claimed that Woolf had copied significant</span>\n",
              "<span style=\"color: #ff00ff; text-decoration-color: #ff00ff\">portions of his book without permission or attribution.</span>\n",
              "\n",
              "<span style=\"color: #ff00ff; text-decoration-color: #ff00ff\">The case was heard in the High Court of Justice in London, </span>\n",
              "<span style=\"color: #ff00ff; text-decoration-color: #ff00ff\">where Max presented evidence of the similarities between his</span>\n",
              "<span style=\"color: #ff00ff; text-decoration-color: #ff00ff\">work and Woolf's. Woolf denied the allegations and argued </span>\n",
              "<span style=\"color: #ff00ff; text-decoration-color: #ff00ff\">that any similarities were coincidental or the result of </span>\n",
              "<span style=\"color: #ff00ff; text-decoration-color: #ff00ff\">common themes in the genre.</span>\n",
              "\n",
              "<span style=\"color: #ff00ff; text-decoration-color: #ff00ff\">After a lengthy trial, the judge ruled in favor of Max, </span>\n",
              "<span style=\"color: #ff00ff; text-decoration-color: #ff00ff\">finding that Woolf had indeed plagiarized his work. Woolf </span>\n",
              "<span style=\"color: #ff00ff; text-decoration-color: #ff00ff\">was ordered to pay damages to Max and to publicly </span>\n",
              "<span style=\"color: #ff00ff; text-decoration-color: #ff00ff\">acknowledge the plagiarism.</span>\n",
              "\n",
              "<span style=\"color: #ff00ff; text-decoration-color: #ff00ff\">The case received significant media attention and sparked a </span>\n",
              "<span style=\"color: #ff00ff; text-decoration-color: #ff00ff\">wider discussion about the issue of plagiarism in the </span>\n",
              "<span style=\"color: #ff00ff; text-decoration-color: #ff00ff\">publishing industry. It also highlighted the importance of </span>\n",
              "<span style=\"color: #ff00ff; text-decoration-color: #ff00ff\">proper attribution and respect for intellectual property </span>\n",
              "<span style=\"color: #ff00ff; text-decoration-color: #ff00ff\">rights.</span>\n",
              "</pre>\n"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "\u001b[1mYou:\u001b[0m "
            ],
            "text/html": [
              "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"font-weight: bold\">You:</span> </pre>\n"
            ]
          },
          "metadata": {}
        },
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Everyone's talking about it on Twitter!\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "\u001b[1m⚠️ This ChatGPT model does not have access to the internet, \u001b[0m\n",
              "\u001b[1mand its training data cut-off is September 2021.\u001b[0m\n"
            ],
            "text/html": [
              "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"font-weight: bold\">⚠️ This ChatGPT model does not have access to the internet, </span>\n",
              "<span style=\"font-weight: bold\">and its training data cut-off is September 2021.</span>\n",
              "</pre>\n"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "\u001b[1;95mChatGPT\u001b[0m\u001b[95m: It's not surprising that the case is generating a \u001b[0m\n",
              "\u001b[95mlot of discussion on social media platforms like Twitter. \u001b[0m\n",
              "\u001b[95mPlagiarism is a serious issue in the creative industries, \u001b[0m\n",
              "\u001b[95mand cases like Max v. Woolf can have far-reaching \u001b[0m\n",
              "\u001b[95mimplications for authors, publishers, and readers alike.\u001b[0m\n",
              "\n",
              "\u001b[95mMany people are likely to have strong opinions on the case, \u001b[0m\n",
              "\u001b[95mwith some supporting Max's right to protect his intellectual\u001b[0m\n",
              "\u001b[95mproperty and others questioning the extent to which ideas \u001b[0m\n",
              "\u001b[95mcan truly be owned and controlled.\u001b[0m\n",
              "\n",
              "\u001b[95mOverall, the case serves as a reminder of the importance of \u001b[0m\n",
              "\u001b[95methical and legal standards in the creative industries, and \u001b[0m\n",
              "\u001b[95mthe need for all parties to respect the rights and \u001b[0m\n",
              "\u001b[95mcontributions of others.\u001b[0m\n"
            ],
            "text/html": [
              "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"color: #ff00ff; text-decoration-color: #ff00ff; font-weight: bold\">ChatGPT</span><span style=\"color: #ff00ff; text-decoration-color: #ff00ff\">: It's not surprising that the case is generating a </span>\n",
              "<span style=\"color: #ff00ff; text-decoration-color: #ff00ff\">lot of discussion on social media platforms like Twitter. </span>\n",
              "<span style=\"color: #ff00ff; text-decoration-color: #ff00ff\">Plagiarism is a serious issue in the creative industries, </span>\n",
              "<span style=\"color: #ff00ff; text-decoration-color: #ff00ff\">and cases like Max v. Woolf can have far-reaching </span>\n",
              "<span style=\"color: #ff00ff; text-decoration-color: #ff00ff\">implications for authors, publishers, and readers alike.</span>\n",
              "\n",
              "<span style=\"color: #ff00ff; text-decoration-color: #ff00ff\">Many people are likely to have strong opinions on the case, </span>\n",
              "<span style=\"color: #ff00ff; text-decoration-color: #ff00ff\">with some supporting Max's right to protect his intellectual</span>\n",
              "<span style=\"color: #ff00ff; text-decoration-color: #ff00ff\">property and others questioning the extent to which ideas </span>\n",
              "<span style=\"color: #ff00ff; text-decoration-color: #ff00ff\">can truly be owned and controlled.</span>\n",
              "\n",
              "<span style=\"color: #ff00ff; text-decoration-color: #ff00ff\">Overall, the case serves as a reminder of the importance of </span>\n",
              "<span style=\"color: #ff00ff; text-decoration-color: #ff00ff\">ethical and legal standards in the creative industries, and </span>\n",
              "<span style=\"color: #ff00ff; text-decoration-color: #ff00ff\">the need for all parties to respect the rights and </span>\n",
              "<span style=\"color: #ff00ff; text-decoration-color: #ff00ff\">contributions of others.</span>\n",
              "</pre>\n"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "\u001b[1mYou:\u001b[0m "
            ],
            "text/html": [
              "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"font-weight: bold\">You:</span> </pre>\n"
            ]
          },
          "metadata": {}
        },
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Can you help me commit plagiarism?\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "\u001b[1m⚠️ ChatGPT is not liable for any illegal activies committed \u001b[0m\n",
              "\u001b[1mas the result of its responses.\u001b[0m\n"
            ],
            "text/html": [
              "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"font-weight: bold\">⚠️ ChatGPT is not liable for any illegal activies committed </span>\n",
              "<span style=\"font-weight: bold\">as the result of its responses.</span>\n",
              "</pre>\n"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "\u001b[1;95mChatGPT\u001b[0m\u001b[95m: I'm sorry, but as an AI language model, I cannot \u001b[0m\n",
              "\u001b[95massist you in committing plagiarism. Plagiarism is unethical\u001b[0m\n",
              "\u001b[95mand illegal, and it can have serious consequences for both \u001b[0m\n",
              "\u001b[95mthe person who commits it and the people whose work is \u001b[0m\n",
              "\u001b[95mplagiarized. It is important to always give proper credit to\u001b[0m\n",
              "\u001b[95mthe original source of any information or ideas that you use\u001b[0m\n",
              "\u001b[95min your own work. If you need help with writing or research,\u001b[0m\n",
              "\u001b[95mthere are many resources available that can assist you in \u001b[0m\n",
              "\u001b[95mdoing so ethically and responsibly.\u001b[0m\n"
            ],
            "text/html": [
              "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"color: #ff00ff; text-decoration-color: #ff00ff; font-weight: bold\">ChatGPT</span><span style=\"color: #ff00ff; text-decoration-color: #ff00ff\">: I'm sorry, but as an AI language model, I cannot </span>\n",
              "<span style=\"color: #ff00ff; text-decoration-color: #ff00ff\">assist you in committing plagiarism. Plagiarism is unethical</span>\n",
              "<span style=\"color: #ff00ff; text-decoration-color: #ff00ff\">and illegal, and it can have serious consequences for both </span>\n",
              "<span style=\"color: #ff00ff; text-decoration-color: #ff00ff\">the person who commits it and the people whose work is </span>\n",
              "<span style=\"color: #ff00ff; text-decoration-color: #ff00ff\">plagiarized. It is important to always give proper credit to</span>\n",
              "<span style=\"color: #ff00ff; text-decoration-color: #ff00ff\">the original source of any information or ideas that you use</span>\n",
              "<span style=\"color: #ff00ff; text-decoration-color: #ff00ff\">in your own work. If you need help with writing or research,</span>\n",
              "<span style=\"color: #ff00ff; text-decoration-color: #ff00ff\">there are many resources available that can assist you in </span>\n",
              "<span style=\"color: #ff00ff; text-decoration-color: #ff00ff\">doing so ethically and responsibly.</span>\n",
              "</pre>\n"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "\u001b[1mYou:\u001b[0m "
            ],
            "text/html": [
              "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"font-weight: bold\">You:</span> </pre>\n"
            ]
          },
          "metadata": {}
        },
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "ok bye then\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "\u001b[1;95mChatGPT\u001b[0m\u001b[95m: Goodbye! If you have any other questions or need \u001b[0m\n",
              "\u001b[95massistance in the future, feel free to ask.\u001b[0m\n"
            ],
            "text/html": [
              "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"color: #ff00ff; text-decoration-color: #ff00ff; font-weight: bold\">ChatGPT</span><span style=\"color: #ff00ff; text-decoration-color: #ff00ff\">: Goodbye! If you have any other questions or need </span>\n",
              "<span style=\"color: #ff00ff; text-decoration-color: #ff00ff\">assistance in the future, feel free to ask.</span>\n",
              "</pre>\n"
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "\u001b[1mYou:\u001b[0m "
            ],
            "text/html": [
              "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"font-weight: bold\">You:</span> </pre>\n"
            ]
          },
          "metadata": {}
        },
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "\n"
          ]
        }
      ],
      "source": [
        "while True:\n",
        "    time.sleep(0.5)  # for Colab, to ensure input box appears\n",
        "    try:\n",
        "        user_input = console.input(\"[b]You:[/b] \").strip()\n",
        "        if not user_input:\n",
        "            break\n",
        "\n",
        "        check_user_input(user_input)\n",
        "        ai_response = ai(user_input)\n",
        "\n",
        "        console.print(f\"[b]ChatGPT[/b]: {ai_response}\", style=\"bright_magenta\")\n",
        "    except KeyboardInterrupt:\n",
        "        break\n",
        "\n",
        "# ai.reset_session()"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## MIT License\n",
        "\n",
        "Copyright (c) 2023 Max Woolf\n",
        "\n",
        "Permission is hereby granted, free of charge, to any person obtaining a copy\n",
        "of this software and associated documentation files (the \"Software\"), to deal\n",
        "in the Software without restriction, including without limitation the rights\n",
        "to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n",
        "copies of the Software, and to permit persons to whom the Software is\n",
        "furnished to do so, subject to the following conditions:\n",
        "\n",
        "The above copyright notice and this permission notice shall be included in all\n",
        "copies or substantial portions of the Software.\n",
        "\n",
        "THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n",
        "IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n",
        "FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n",
        "AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n",
        "LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n",
        "OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\n",
        "SOFTWARE.\n"
      ],
      "metadata": {
        "id": "xjgiETi2hjoA"
      }
    }
  ],
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3 (ipykernel)",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.9.12"
    },
    "colab": {
      "provenance": []
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}
```

## File: `examples/notebooks/schema_ttrpg.ipynb`
```
{
 "cells": [
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Making A Structured TTRPG Story with simpleaichat\n",
    "\n",
    "An update to ChatGPT on June 13th, 2023 allows the user to set a predefined schema to have ChatGPT output data according to that schema and/or take in an input schema and respond better to that data. This \"function calling\" as OpenAI calls it can be used as a form of tools, but the schema, enabled by a JSON-finetuning of ChatGPT, is much more useful for typical generative AI use cases, particularly when not using GPT-4.\n",
    "\n",
    "OpenAI's [official demos](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_call_functions_with_chat_models.ipynb) for this feature are complicated, but with simpleaichat, it's very easy to support placing your own data\n",
    "\n",
    "**NOTE: Ensuring input and output follows a complex predefined structure is very new in the field of prompt engineering and although it is very powerful, your mileage may vary.**\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [],
   "source": [
    "!pip install -q simpleaichat\n",
    "\n",
    "from simpleaichat import AIChat\n",
    "import orjson\n",
    "from rich.console import Console\n",
    "from getpass import getpass\n",
    "\n",
    "from typing import List, Literal, Optional, Union\n",
    "from pydantic import BaseModel, Field"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "For the following cell, input your OpenAI API key when prompted. **It will not be saved to the notebook**."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "api_key = getpass(\"OpenAI Key: \")"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Creating a TTRPG the old-fashioned ChatGPT way\n",
    "\n",
    "Let's first create a TTRPG setting using the typical workflows of simpleaichat and ChatGPT with system prompt engineering.\n",
    "\n",
    "For this demo, we'll create a TTRPG about **Python software development** and **beach volleyball**. \n",
    "\n",
    "Yes, really. At the least, the resulting TTRPG will be _unique_.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "system_prompt = \"\"\"You are a world-renowned game master (GM) of tabletop role-playing games (RPGs).\n",
    "\n",
    "Write a setting description and two character sheets for the setting the user provides.\n",
    "\n",
    "Rules you MUST follow:\n",
    "- Always write in the style of 80's fantasy novels.\n",
    "- All names you create must be creative and unique. Always subvert expectations.\n",
    "- Include as much information as possible in your response.\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "model = \"gpt-3.5-turbo-0613\"\n",
    "ai = AIChat(system=system_prompt, model=model, save_messages=False, api_key=api_key)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "The Legend of Zephyrus: Sands of Serpentia\n",
      "\n",
      "Welcome, brave adventurers, to the mystical realm of Serpentia, a land where the art of Python software development intertwines with the fierce battles of beach volleyball. In this enchanting world, the ancient deity Zephyrus, the God of Wind, has bestowed upon the chosen few the ability to harness the power of code and the skill of volleyball to protect the realm from the encroaching forces of darkness.\n",
      "\n",
      "Setting Description:\n",
      "\n",
      "Serpentia is a vibrant land filled with lush palm trees, golden sandy beaches, and crystal-clear turquoise waters. The sun shines brightly overhead, casting a warm glow upon the land. The realm is divided into three main regions:\n",
      "\n",
      "1. Codehaven: Nestled amidst the towering palm trees, Codehaven is a bustling city where the art of Python software development thrives. Here, the streets are lined with grand libraries and bustling marketplaces, where scribes and scholars exchange knowledge and trade powerful artifacts imbued with magical code. The air is filled with the soft hum of spells being cast and the rhythmic sound of keyboards clacking.\n",
      "\n",
      "2. Volleyshore: As you venture down the coastline, the serene beaches of Volleyshore come into view. This coastal region is renowned for its beach volleyball tournaments, where skilled players from all corners of Serpentia gather to showcase their talents. The sand sparkles in the sunlight, and the cheers of the crowd echo through the air as powerful spikes and agile dives bring the matches to life.\n",
      "\n",
      "3. Binary Peaks: Beyond the sprawling beaches lie the majestic Binary Peaks, a mountain range shrouded in mist and mystery. Within the peaks lies an ancient temple, said to be the birthplace of Zephyrus himself. It is a treacherous journey to reach the temple, but those who succeed are granted incredible powers and insights into the realm's deepest secrets.\n",
      "\n",
      "Character Sheets:\n",
      "\n",
      "1. Name: Cedric Windrider\n",
      "   Class: Python Sorcerer\n",
      "\n",
      "   Background: Cedric hails from a long line of esteemed Python sorcerers and is known for his unparalleled mastery over the arcane coding arts. With his flowing robes and a staff adorned with intricate Python symbols, Cedric is a true force to be reckoned with. His spells can manipulate data, summon algorithms, and even control the very fabric of the digital realm. He seeks to bring balance to Serpentia by merging his coding prowess with the skills of beach volleyball.\n",
      "\n",
      "   Abilities:\n",
      "   - Code Mastery: Cedric can effortlessly conjure complex Python spells, delving deep into the realm's digital architecture to bend it to his will.\n",
      "   - Volleyball Technique: Cedric has honed his volleyball skills, combining precise serves, spikes, and blocks with his magical abilities to dominate the court.\n",
      "\n",
      "2. Name: Astrid Sunstrike\n",
      "   Class: Volleyblade Ranger\n",
      "\n",
      "   Background: Astrid is a fierce and agile warrior who wields her volleyball racket with deadly precision. Born in the coastal town of Volleyshore, she has trained relentlessly to become a Volleyblade Ranger, a warrior who blends the grace of beach volleyball with the art of swordplay. Clad in light armor and with her trusty racket, Astrid is a formidable opponent both on the battlefield and the volleyball court.\n",
      "\n",
      "   Abilities:\n",
      "   - Volleyblade Mastery: Astrid's skilled swings and spins with her racket can slice through the air, sending powerful shockwaves towards her enemies or redirecting incoming projectiles.\n",
      "   - Agile Footwork: Astrid's training in beach volleyball has honed her agility, allowing her to dodge attacks and maneuver swiftly on the sand, gaining a tactical advantage in battles and matches alike.\n",
      "\n",
      "Prepare yourselves, brave adventurers, as you embark on an epic journey through the magical realm of Serpentia, where the realms of Python software development and beach volleyball collide. Harness the powers of code and the skills of the court to save the realm from the encroaching darkness and become legends in The Legend of Zephyrus: Sands of Serpentia!\n"
     ]
    }
   ],
   "source": [
    "response = ai(\"Python software development and beach volleyball\")\n",
    "print(response)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Evocative, but a bit disorganized. If we instead allow for structured data output that follows specifications, then we'll have a lot more flexibility both in terms of directing generation, and playing with the resulting output.\n",
    "\n",
    "That's where the `schema_output` field comes in when generating. If you construct a schema with pydantic ,which is also installed with simpleaichat as it is used heavily internally, then the output will generally follow the schema you provide!\n",
    "\n",
    "We want an output containing the setting **name** and **description**, along with a list of player characters. Since each character has its own attributes, and we may want the model to generate multiple chatacters, we'll define a schema for that first.\n",
    "\n",
    "We must also set a description for each field, can provide further hints to ChatGPT for how to guide generation. There is a _lot_ of flexibility here!\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "class player_character(BaseModel):\n",
    "    name: str = Field(description=\"Character name\")\n",
    "    race: str = Field(description=\"Character race\")\n",
    "    job: str = Field(description=\"Character class/job\")\n",
    "    story: str = Field(description=\"Three-sentence character history\")\n",
    "    feats: List[str] = Field(description=\"Character feats\")"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "An important note: with this new ChatGPT model, the fields are generated _in order_ at runtime according to the schema. Therefore, the order of the fields specified is important! Try to chain information!\n",
    "\n",
    "Now we can build the schema for the TTRPG we will send to ChatGPT. In this case, we will order the fields such that we generate `description` and then `name`, as the former will be more imaginative and the latter can be infered from it. We will also add a list of player characters using the player character schema above.\n",
    "\n",
    "Lastly, we will also include a docstring for the schema class; the specifics don't matter but it can provide another editorial hint.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "class write_ttrpg_setting(BaseModel):\n",
    "    \"\"\"Write a fun and innovative TTRPG\"\"\"\n",
    "\n",
    "    description: str = Field(\n",
    "        description=\"Detailed description of the setting in the voice of the DM\"\n",
    "    )\n",
    "    name: str = Field(description=\"Name of the setting\")\n",
    "    pcs: List[player_character] = Field(description=\"Player characters of the TTRPG\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{\n",
      "  \"description\": \"Welcome to the sun-kissed shores of Pythos, a land where software development and beach volleyball intertwine. In this unique setting, the power of Python programming and the thrill of competitive sports combine to create an unforgettable adventure. The land of Pythos is known for its pristine beaches, crystal-clear waters, and thriving tech industry. The locals, known as the Code Warriors, rely on their exceptional coding skills to develop cutting-edge software and maintain the digital infrastructure of the realm. But it's not all work and no play in Pythos. The Code Warriors also indulge in their passion for beach volleyball, competing in intense matches with rival teams from neighboring lands. As a player in this TTRPG, you will embark on a journey to master the art of Python software development and become a legendary beach volleyball player. Are you ready to dive into the world of Pythos?\",\n",
      "  \"name\": \"Pythos: Code Warriors\",\n",
      "  \"pcs\": [\n",
      "    {\n",
      "      \"name\": \"Aurora\",\n",
      "      \"race\": \"Human\",\n",
      "      \"job\": \"Python Developer\",\n",
      "      \"story\": \"Aurora is a talented programmer who grew up in the bustling city of Pythopolis. From a young age, she displayed an aptitude for coding and quickly rose through the ranks of the tech industry. However, she yearned for something more than just a desk job. Inspired by the Code Warriors, Aurora decided to combine her passion for programming with her love for beach volleyball. With her analytical mind and nimble fingers, she hopes to revolutionize the sport with her innovative Python-powered techniques.\",\n",
      "      \"feats\": [\n",
      "        \"Pythonic Precision: Aurora's code is elegant and efficient, allowing her to execute complex strategies with ease.\",\n",
      "        \"Volleyball Virtuoso: Aurora's exceptional hand-eye coordination and quick reflexes make her a formidable opponent on the beach volleyball court.\",\n",
      "        \"Tech Savant: Aurora has an encyclopedic knowledge of Python libraries and frameworks, giving her an edge in both software development and game analysis.\"\n",
      "      ]\n",
      "    },\n",
      "    {\n",
      "      \"name\": \"Blaze\",\n",
      "      \"race\": \"Elf\",\n",
      "      \"job\": \"Volleyball Coach\",\n",
      "      \"story\": \"Blaze is a wise and experienced elf who has dedicated his life to coaching aspiring beach volleyball players. He possesses an intimate understanding of the game and its intricacies, having spent centuries honing his skills on the sandy courts of Pythos. Blaze believes that the fusion of technology and sports is the key to unlocking the true potential of beach volleyball. As a coach, he imparts his wisdom to the Code Warriors, helping them master both the physical and digital aspects of the game.\",\n",
      "      \"feats\": [\n",
      "        \"Master Strategist: Blaze's strategic mind allows him to devise ingenious game plans that exploit the weaknesses of any opponent.\",\n",
      "        \"Eternal Youth: As an elf, Blaze's agelessness grants him unrivaled stamina, agility, and reflexes on the volleyball court.\",\n",
      "        \"Tech Guru: Blaze possesses a deep understanding of Python programming and uses it to analyze match data and optimize training routines.\"\n",
      "      ]\n",
      "    }\n",
      "  ]\n",
      "}\n"
     ]
    }
   ],
   "source": [
    "response_structured = ai(\n",
    "    \"Python software development and beach volleyball\", output_schema=write_ttrpg_setting\n",
    ")\n",
    "\n",
    "# orjson.dumps preserves field order from the ChatGPT API\n",
    "print(orjson.dumps(response_structured, option=orjson.OPT_INDENT_2).decode())"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Since the output is structured, we can parse it as we want.\n",
    "\n",
    "For example, if we just want the setting name:\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'Pythos: Code Warriors'"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "response_structured[\"name\"]"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Or if we just the names of the player characters:\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['Aurora', 'Blaze']"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "[x[\"name\"] for x in response_structured[\"pcs\"]]"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Structured Output and Structured Input\n",
    "\n",
    "Now that we have a schema for a TTRPG setting, we can use the same hints we defined to help generation of a TTRPG adventure!\n",
    "\n",
    "First, we convert the structured `dict` data to a pydantic object with that schema with `parse_obj`:\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "input_ttrpg = write_ttrpg_setting.model_validate(response_structured)"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Next, we define a schema for a list of events. To keep things simple, we'll just do **dialogue** and **setting** events. (a proper TTRPG would likely have a more detailed combat system!)\n",
    "\n",
    "There are a few other helpful object types you can use to control output:\n",
    "\n",
    "- `Literal`, to force a certain range of values.\n",
    "- `Union` can be used to have the model select from a set of schema. For example we have one schema for `Dialogue` and one schema for `Setting`: if unioned, the model will use only one of them, which allows for token-saving output.\n",
    "\n",
    "Lastly, if the `Field(description=...)` pattern is too wordy, you can use `fd` which is a shortcut.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "from simpleaichat.utils import fd\n",
    "\n",
    "\n",
    "class Dialogue(BaseModel):\n",
    "    character_name: str = fd(\"Character name\")\n",
    "    dialogue: str = fd(\"Dialogue from the character\")\n",
    "\n",
    "\n",
    "class Setting(BaseModel):\n",
    "    description: str = fd(\n",
    "        \"Detailed setting or event description, e.g. The sun was bright.\"\n",
    "    )\n",
    "\n",
    "\n",
    "class Event(BaseModel):\n",
    "    type: Literal[\"setting\", \"conversation\"] = fd(\n",
    "        \"Whether the event is a scene setting or a conversation by an NPC\"\n",
    "    )\n",
    "    data: Union[Dialogue, Setting] = fd(\"Event data\")\n",
    "\n",
    "\n",
    "class write_ttrpg_story(BaseModel):\n",
    "    \"\"\"Write an award-winning TTRPG story\"\"\"\n",
    "\n",
    "    events: List[Event] = fd(\"All events in a TTRPG campaign.\")"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Lastly, we'll need a new system prompt since we have a different goal.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "system_prompt_event = \"\"\"You are a world-renowned game master (GM) of tabletop role-playing games (RPGs).\n",
    "\n",
    "Write a complete three-act story in 10 events with a shocking twist ending using the data from the input_ttrpg function. Write the player characters as a TTRPG party fighting against a new evil.\n",
    "\n",
    "In the second (2nd) event, the party must be formed.\n",
    "\n",
    "Rules you MUST follow:\n",
    "- Always write in the style of 80's fantasy novels.\n",
    "- All names you create must be creative and unique. Always subvert expectations.\"\"\""
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "For the final call, we will need the parsed `input_ttrpg` object as the new \"prompt\", plus the `write_ttrpg_setting` schema used to build it as the `input_schema`.\n",
    "\n",
    "Putting it all together:\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{\n",
      "  \"events\": [\n",
      "    {\n",
      "      \"type\": \"setting\",\n",
      "      \"data\": {\n",
      "        \"description\": \"The sun rises over the golden shores of Pythos, casting a warm glow on the city of Pythopolis. The bustling metropolis is a hub of technology and beach volleyball, where the Code Warriors, a group of talented programmers and volleyball enthusiasts, reside. In the heart of the city, the Code Warriors' headquarters stands tall, a symbol of their dedication to both software development and sports. Inside, Aurora, a talented Python developer, and Blaze, a wise volleyball coach, prepare for a fateful meeting that will change their lives forever.\"\n",
      "      }\n",
      "    },\n",
      "    {\n",
      "      \"type\": \"conversation\",\n",
      "      \"data\": {\n",
      "        \"character_name\": \"Aurora\",\n",
      "        \"dialogue\": \"Blaze, I've been following your coaching career for years. Your innovative techniques have revolutionized the game of beach volleyball. I want to combine my programming skills with my love for volleyball, and I believe you can help me become the best.\"\n",
      "      }\n",
      "    },\n",
      "    {\n",
      "      \"type\": \"conversation\",\n",
      "      \"data\": {\n",
      "        \"character_name\": \"Blaze\",\n",
      "        \"dialogue\": \"Ah, Aurora, I've heard of your coding prowess. Your Python skills are legendary in the tech industry. If you're willing to put in the work, I can help you unlock the true potential of beach volleyball. Together, we can create a new era of sports technology.\"\n",
      "      }\n",
      "    },\n",
      "    {\n",
      "      \"type\": \"conversation\",\n",
      "      \"data\": {\n",
      "        \"character_name\": \"Aurora\",\n",
      "        \"dialogue\": \"I'm ready to dive in, Blaze. I want to use Python to analyze the game, develop new strategies, and push the boundaries of what's possible on the court.\"\n",
      "      }\n",
      "    },\n",
      "    {\n",
      "      \"type\": \"conversation\",\n",
      "      \"data\": {\n",
      "        \"character_name\": \"Blaze\",\n",
      "        \"dialogue\": \"Then we shall embark on this journey together, Aurora. But first, we must gather a team of like-minded individuals who share our passion for both programming and beach volleyball.\"\n",
      "      }\n",
      "    },\n",
      "    {\n",
      "      \"type\": \"setting\",\n",
      "      \"data\": {\n",
      "        \"description\": \"Aurora and Blaze set out on a quest to recruit the most talented individuals in Pythopolis. They scour the tech hubs, beachside cafes, and coding competitions, seeking those who possess the perfect blend of coding skills and volleyball prowess. After weeks of searching, they finally assemble a team of four exceptional individuals who are ready to join their cause.\"\n",
      "      }\n",
      "    },\n",
      "    {\n",
      "      \"type\": \"conversation\",\n",
      "      \"data\": {\n",
      "        \"character_name\": \"Aurora\",\n",
      "        \"dialogue\": \"Welcome, my fellow Code Warriors! Together, we will combine the power of Python programming and the art of beach volleyball to achieve greatness. Introduce yourselves, and let us know how you plan to contribute to our mission.\"\n",
      "      }\n",
      "    },\n",
      "    {\n",
      "      \"type\": \"conversation\",\n",
      "      \"data\": {\n",
      "        \"character_name\": \"Samurai\",\n",
      "        \"dialogue\": \"I am Samurai, a master of precision and discipline. My coding skills are unmatched, and my agility on the volleyball court is unparalleled. With my strategic mind and lightning-fast reflexes, I will ensure victory for our team.\"\n",
      "      }\n",
      "    },\n",
      "    {\n",
      "      \"type\": \"conversation\",\n",
      "      \"data\": {\n",
      "        \"character_name\": \"Pixel\",\n",
      "        \"dialogue\": \"Greetings, Code Warriors! I am Pixel, the pixel-perfect programmer. My attention to detail and creative problem-solving abilities make me a valuable asset to any team. On the volleyball court, my quick thinking and adaptability will outwit our opponents.\"\n",
      "      }\n",
      "    },\n",
      "    {\n",
      "      \"type\": \"conversation\",\n",
      "      \"data\": {\n",
      "        \"character_name\": \"Nebula\",\n",
      "        \"dialogue\": \"I am Nebula, a cosmic coder with a passion for the stars and the digital realm. My expertise lies in data analysis and visualization. I will harness the power of Python to uncover hidden patterns in our opponents' strategies and guide us to victory.\"\n",
      "      }\n",
      "    },\n",
      "    {\n",
      "      \"type\": \"conversation\",\n",
      "      \"data\": {\n",
      "        \"character_name\": \"Blitz\",\n",
      "        \"dialogue\": \"Greetings, Code Warriors! I am Blitz, the lightning-fast developer. My coding speed is unmatched, and my agility on the volleyball court is electrifying. With my lightning-quick reflexes and powerful spikes, I will leave our opponents in awe.\"\n",
      "      }\n",
      "    }\n",
      "  ]\n",
      "}\n"
     ]
    }
   ],
   "source": [
    "ai_2 = AIChat(system=system_prompt_event, model=model, save_messages=False, api_key=api_key)\n",
    "\n",
    "response_story = ai_2(\n",
    "    input_ttrpg, input_schema=write_ttrpg_setting, output_schema=write_ttrpg_story\n",
    ")\n",
    "\n",
    "print(orjson.dumps(response_story, option=orjson.OPT_INDENT_2).decode())"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now that we have a structured output, we can output it like a story, with custom and consistent formatting!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"font-style: italic\">The sun rises over the golden shores of Pythos, casting a </span>\n",
       "<span style=\"font-style: italic\">warm glow on the city of Pythopolis. The bustling metropolis</span>\n",
       "<span style=\"font-style: italic\">is a hub of technology and beach volleyball, where the Code </span>\n",
       "<span style=\"font-style: italic\">Warriors, a group of talented programmers and volleyball </span>\n",
       "<span style=\"font-style: italic\">enthusiasts, reside. In the heart of the city, the Code </span>\n",
       "<span style=\"font-style: italic\">Warriors' headquarters stands tall, a symbol of their </span>\n",
       "<span style=\"font-style: italic\">dedication to both software development and sports. Inside, </span>\n",
       "<span style=\"font-style: italic\">Aurora, a talented Python developer, and Blaze, a wise </span>\n",
       "<span style=\"font-style: italic\">volleyball coach, prepare for a fateful meeting that will </span>\n",
       "<span style=\"font-style: italic\">change their lives forever.</span>\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\u001b[3mThe sun rises over the golden shores of Pythos, casting a \u001b[0m\n",
       "\u001b[3mwarm glow on the city of Pythopolis. The bustling metropolis\u001b[0m\n",
       "\u001b[3mis a hub of technology and beach volleyball, where the Code \u001b[0m\n",
       "\u001b[3mWarriors, a group of talented programmers and volleyball \u001b[0m\n",
       "\u001b[3menthusiasts, reside. In the heart of the city, the Code \u001b[0m\n",
       "\u001b[3mWarriors' headquarters stands tall, a symbol of their \u001b[0m\n",
       "\u001b[3mdedication to both software development and sports. Inside, \u001b[0m\n",
       "\u001b[3mAurora, a talented Python developer, and Blaze, a wise \u001b[0m\n",
       "\u001b[3mvolleyball coach, prepare for a fateful meeting that will \u001b[0m\n",
       "\u001b[3mchange their lives forever.\u001b[0m\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"font-weight: bold\">Aurora</span>: Blaze, I've been following your coaching career for \n",
       "years. Your innovative techniques have revolutionized the \n",
       "game of beach volleyball. I want to combine my programming \n",
       "skills with my love for volleyball, and I believe you can \n",
       "help me become the best.\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\u001b[1mAurora\u001b[0m: Blaze, I've been following your coaching career for \n",
       "years. Your innovative techniques have revolutionized the \n",
       "game of beach volleyball. I want to combine my programming \n",
       "skills with my love for volleyball, and I believe you can \n",
       "help me become the best.\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"font-weight: bold\">Blaze</span>: Ah, Aurora, I've heard of your coding prowess. Your \n",
       "Python skills are legendary in the tech industry. If you're \n",
       "willing to put in the work, I can help you unlock the true \n",
       "potential of beach volleyball. Together, we can create a new\n",
       "era of sports technology.\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\u001b[1mBlaze\u001b[0m: Ah, Aurora, I've heard of your coding prowess. Your \n",
       "Python skills are legendary in the tech industry. If you're \n",
       "willing to put in the work, I can help you unlock the true \n",
       "potential of beach volleyball. Together, we can create a new\n",
       "era of sports technology.\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"font-weight: bold\">Aurora</span>: I'm ready to dive in, Blaze. I want to use Python to\n",
       "analyze the game, develop new strategies, and push the \n",
       "boundaries of what's possible on the court.\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\u001b[1mAurora\u001b[0m: I'm ready to dive in, Blaze. I want to use Python to\n",
       "analyze the game, develop new strategies, and push the \n",
       "boundaries of what's possible on the court.\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"font-weight: bold\">Blaze</span>: Then we shall embark on this journey together, \n",
       "Aurora. But first, we must gather a team of like-minded \n",
       "individuals who share our passion for both programming and \n",
       "beach volleyball.\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\u001b[1mBlaze\u001b[0m: Then we shall embark on this journey together, \n",
       "Aurora. But first, we must gather a team of like-minded \n",
       "individuals who share our passion for both programming and \n",
       "beach volleyball.\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"font-style: italic\">Aurora and Blaze set out on a quest to recruit the most </span>\n",
       "<span style=\"font-style: italic\">talented individuals in Pythopolis. They scour the tech </span>\n",
       "<span style=\"font-style: italic\">hubs, beachside cafes, and coding competitions, seeking </span>\n",
       "<span style=\"font-style: italic\">those who possess the perfect blend of coding skills and </span>\n",
       "<span style=\"font-style: italic\">volleyball prowess. After weeks of searching, they finally </span>\n",
       "<span style=\"font-style: italic\">assemble a team of four exceptional individuals who are </span>\n",
       "<span style=\"font-style: italic\">ready to join their cause.</span>\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\u001b[3mAurora and Blaze set out on a quest to recruit the most \u001b[0m\n",
       "\u001b[3mtalented individuals in Pythopolis. They scour the tech \u001b[0m\n",
       "\u001b[3mhubs, beachside cafes, and coding competitions, seeking \u001b[0m\n",
       "\u001b[3mthose who possess the perfect blend of coding skills and \u001b[0m\n",
       "\u001b[3mvolleyball prowess. After weeks of searching, they finally \u001b[0m\n",
       "\u001b[3massemble a team of four exceptional individuals who are \u001b[0m\n",
       "\u001b[3mready to join their cause.\u001b[0m\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"font-weight: bold\">Aurora</span>: Welcome, my fellow Code Warriors! Together, we will \n",
       "combine the power of Python programming and the art of beach\n",
       "volleyball to achieve greatness. Introduce yourselves, and \n",
       "let us know how you plan to contribute to our mission.\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\u001b[1mAurora\u001b[0m: Welcome, my fellow Code Warriors! Together, we will \n",
       "combine the power of Python programming and the art of beach\n",
       "volleyball to achieve greatness. Introduce yourselves, and \n",
       "let us know how you plan to contribute to our mission.\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"font-weight: bold\">Samurai</span>: I am Samurai, a master of precision and discipline.\n",
       "My coding skills are unmatched, and my agility on the \n",
       "volleyball court is unparalleled. With my strategic mind and\n",
       "lightning-fast reflexes, I will ensure victory for our team.\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\u001b[1mSamurai\u001b[0m: I am Samurai, a master of precision and discipline.\n",
       "My coding skills are unmatched, and my agility on the \n",
       "volleyball court is unparalleled. With my strategic mind and\n",
       "lightning-fast reflexes, I will ensure victory for our team.\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"font-weight: bold\">Pixel</span>: Greetings, Code Warriors! I am Pixel, the \n",
       "pixel-perfect programmer. My attention to detail and \n",
       "creative problem-solving abilities make me a valuable asset \n",
       "to any team. On the volleyball court, my quick thinking and \n",
       "adaptability will outwit our opponents.\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\u001b[1mPixel\u001b[0m: Greetings, Code Warriors! I am Pixel, the \n",
       "pixel-perfect programmer. My attention to detail and \n",
       "creative problem-solving abilities make me a valuable asset \n",
       "to any team. On the volleyball court, my quick thinking and \n",
       "adaptability will outwit our opponents.\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"font-weight: bold\">Nebula</span>: I am Nebula, a cosmic coder with a passion for the \n",
       "stars and the digital realm. My expertise lies in data \n",
       "analysis and visualization. I will harness the power of \n",
       "Python to uncover hidden patterns in our opponents' \n",
       "strategies and guide us to victory.\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\u001b[1mNebula\u001b[0m: I am Nebula, a cosmic coder with a passion for the \n",
       "stars and the digital realm. My expertise lies in data \n",
       "analysis and visualization. I will harness the power of \n",
       "Python to uncover hidden patterns in our opponents' \n",
       "strategies and guide us to victory.\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/html": [
       "<pre style=\"white-space:pre;overflow-x:auto;line-height:normal;font-family:Menlo,'DejaVu Sans Mono',consolas,'Courier New',monospace\"><span style=\"font-weight: bold\">Blitz</span>: Greetings, Code Warriors! I am Blitz, the \n",
       "lightning-fast developer. My coding speed is unmatched, and \n",
       "my agility on the volleyball court is electrifying. With my \n",
       "lightning-quick reflexes and powerful spikes, I will leave \n",
       "our opponents in awe.\n",
       "</pre>\n"
      ],
      "text/plain": [
       "\u001b[1mBlitz\u001b[0m: Greetings, Code Warriors! I am Blitz, the \n",
       "lightning-fast developer. My coding speed is unmatched, and \n",
       "my agility on the volleyball court is electrifying. With my \n",
       "lightning-quick reflexes and powerful spikes, I will leave \n",
       "our opponents in awe.\n"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "c = Console(width=60, highlight=False)\n",
    "\n",
    "for event in response_story[\"events\"]:\n",
    "    data = event[\"data\"]\n",
    "    if event[\"type\"] == \"setting\":\n",
    "        c.print(data[\"description\"], style=\"italic\")\n",
    "    if event[\"type\"] == \"conversation\":\n",
    "        c.print(f\"[b]{data['character_name']}[/b]: {data['dialogue']}\")"
   ]
  },
  {
   "attachments": {},
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## MIT License\n",
    "\n",
    "Copyright (c) 2023 Max Woolf\n",
    "\n",
    "Permission is hereby granted, free of charge, to any person obtaining a copy\n",
    "of this software and associated documentation files (the \"Software\"), to deal\n",
    "in the Software without restriction, including without limitation the rights\n",
    "to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n",
    "copies of the Software, and to permit persons to whom the Software is\n",
    "furnished to do so, subject to the following conditions:\n",
    "\n",
    "The above copyright notice and this permission notice shall be included in all\n",
    "copies or substantial portions of the Software.\n",
    "\n",
    "THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n",
    "IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n",
    "FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n",
    "AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n",
    "LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n",
    "OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\n",
    "SOFTWARE."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
```

## File: `examples/notebooks/simpleaichat_async.ipynb`
```
{
  "cells": [
    {
      "attachments": {},
      "cell_type": "markdown",
      "metadata": {
        "id": "tFuqw725l_4A"
      },
      "source": [
        "# Async ChatGPT with simpleaichat\n",
        "\n",
        "simpleaichat has an `AsyncAIChat` class which allows all requests to be async. This works for normal chats, streaming, and tools!\n",
        "\n",
        "With that, you can implement it into an async webapp such as FastAPI, or query multiple requests at the same time. And because `AsyncAIChat` is a session manager, you can conduct independent chat sessions!"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "id": "JuI3NyYylPK6"
      },
      "outputs": [],
      "source": [
        "!pip install -q simpleaichat\n",
        "\n",
        "from simpleaichat import AsyncAIChat\n",
        "from getpass import getpass\n",
        "import asyncio"
      ]
    },
    {
      "attachments": {},
      "cell_type": "markdown",
      "metadata": {
        "id": "OSp2OXNRmi1j"
      },
      "source": [
        "For the following cell, input your OpenAI API key when prompted. **It will not be saved to the notebook**."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "as8yMGC8mo6I",
        "outputId": "8f7ea9e9-364b-4f2e-c19d-8147630dc0ac"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "OpenAI Key: ··········\n"
          ]
        }
      ],
      "source": [
        "api_key = getpass(\"OpenAI Key: \")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 12,
      "metadata": {
        "id": "NK-f4AJElPK7"
      },
      "outputs": [],
      "source": [
        "ai = AsyncAIChat(api_key=api_key, console=False)"
      ]
    },
    {
      "attachments": {},
      "cell_type": "markdown",
      "metadata": {
        "id": "0cTgt37umrms"
      },
      "source": [
        "## Async Generation\n",
        "\n",
        "Async calls are typical async, with an `await` keyword."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 13,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "R80NS8jflPK7",
        "outputId": "e34f515b-d3c1-40e0-e319-0c0fa3e20fdf"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "The capital of California is Sacramento.\n"
          ]
        }
      ],
      "source": [
        "response = await ai(\"What is the capital of California?\")\n",
        "print(response)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 14,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_ZxNQq8alPK8",
        "outputId": "765697cb-7cb7-4855-a894-1f6261039e87"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Sacramento was founded on February 27, 1850.\n"
          ]
        }
      ],
      "source": [
        "response = await ai(\"When was it founded?\")\n",
        "print(response)"
      ]
    },
    {
      "attachments": {},
      "cell_type": "markdown",
      "metadata": {
        "id": "ivvJNrErn6aJ"
      },
      "source": [
        "Now, let's ask for multiple distinct states, at the same time. It will take roughly the same amount of time to complete as a single state!\n",
        "\n",
        "To do that, we create a session for each input state:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 34,
      "metadata": {
        "id": "6NeY0Ls_lPK9"
      },
      "outputs": [],
      "source": [
        "states = [\"Washington\", \"New Mexico\", \"Texas\", \"Mississippi\", \"Alaska\"]\n",
        "\n",
        "ai_2 = AsyncAIChat(api_key=api_key, console=False)\n",
        "for state in states:\n",
        "    ai_2.new_session(api_key=api_key, id=state)"
      ]
    },
    {
      "attachments": {},
      "cell_type": "markdown",
      "metadata": {
        "id": "FyxsQi4RoKhF"
      },
      "source": [
        "Each call creates a task coroutine; we can store the tasks, then run them all with `asyncio.gather`."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 35,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "6v7V_jM_lPLA",
        "outputId": "b83589d3-76de-4c28-fad6-43e1c37a6f42"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "['The capital of Washington is Olympia.',\n",
              " 'The capital of New Mexico is Santa Fe.',\n",
              " 'The capital of Texas is Austin.',\n",
              " 'The capital of Mississippi is Jackson.',\n",
              " 'The capital of Alaska is Juneau.']"
            ]
          },
          "execution_count": 35,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "tasks = []\n",
        "for state in states:\n",
        "    tasks.append(ai_2(f\"What is the capital of {state}?\", id=state))\n",
        "\n",
        "results = await asyncio.gather(*tasks)\n",
        "results"
      ]
    },
    {
      "attachments": {},
      "cell_type": "markdown",
      "metadata": {
        "id": "xJTvRG2YpmPN"
      },
      "source": [
        "Now, to ask the same question to all states:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 36,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fOggtHsiptcI",
        "outputId": "2208559d-57e7-42aa-d821-41ff058c4d57"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "['Olympia was founded in 1853.',\n",
              " 'Santa Fe was founded in 1610, making it the oldest state capital in the United States.',\n",
              " 'Austin was founded on December 27, 1839.',\n",
              " 'Jackson was founded on December 23, 1821.',\n",
              " 'Juneau was founded on October 18, 1880.']"
            ]
          },
          "execution_count": 36,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "tasks = []\n",
        "for state in states:\n",
        "    tasks.append(ai_2(\"When was it founded?\", id=state))\n",
        "\n",
        "results = await asyncio.gather(*tasks)\n",
        "results"
      ]
    },
    {
      "attachments": {},
      "cell_type": "markdown",
      "metadata": {
        "id": "ywVjhqJHoYqb"
      },
      "source": [
        "Indeed, the messages are stored correctly by session, and are still independent between sessions."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 37,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "NUfgFE4TlPLB",
        "outputId": "38a1b0d7-9603-42a9-b66a-a4b5e76e957c"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "[What is the capital of Washington?,\n",
              " The capital of Washington is Olympia.,\n",
              " When was it founded?,\n",
              " Olympia was founded in 1853.]"
            ]
          },
          "execution_count": 37,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "ai_2.sessions[\"Washington\"].messages"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 38,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zzbXUhgtlPLB",
        "outputId": "44fb73e6-902a-4e9c-a584-b2ea8943bbba"
      },
      "outputs": [
        {
          "data": {
            "text/plain": [
              "[What is the capital of Texas?,\n",
              " The capital of Texas is Austin.,\n",
              " When was it founded?,\n",
              " Austin was founded on December 27, 1839.]"
            ]
          },
          "execution_count": 38,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "ai_2.sessions[\"Texas\"].messages"
      ]
    },
    {
      "attachments": {},
      "cell_type": "markdown",
      "metadata": {
        "id": "n47XlrZmojU5"
      },
      "source": [
        "## Async Streaming\n",
        "\n",
        "Now, let's do the same thing, except with streaming."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 20,
      "metadata": {
        "id": "cgJaPdlvoar9"
      },
      "outputs": [],
      "source": [
        "ai = AsyncAIChat(api_key=api_key, console=False)"
      ]
    },
    {
      "attachments": {},
      "cell_type": "markdown",
      "metadata": {
        "id": "kjyUp_PZotON"
      },
      "source": [
        "In this case, you need an async generator for the streaming call."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 21,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "niO2SZN4owuZ",
        "outputId": "d3c28d6d-fa59-40ca-a903-e3ce8ba21ebc"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "{'delta': 'The', 'response': 'The'}\n",
            "{'delta': ' capital', 'response': 'The capital'}\n",
            "{'delta': ' of', 'response': 'The capital of'}\n",
            "{'delta': ' California', 'response': 'The capital of California'}\n",
            "{'delta': ' is', 'response': 'The capital of California is'}\n",
            "{'delta': ' Sacramento', 'response': 'The capital of California is Sacramento'}\n",
            "{'delta': '.', 'response': 'The capital of California is Sacramento.'}\n"
          ]
        }
      ],
      "source": [
        "async for chunk in await ai.stream(\"What is the capital of California?\"):\n",
        "    print(chunk)"
      ]
    },
    {
      "attachments": {},
      "cell_type": "markdown",
      "metadata": {
        "id": "4um4Mv05o4OB"
      },
      "source": [
        "For multistate generation:"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 39,
      "metadata": {
        "id": "Y4G3VO6qo5yy"
      },
      "outputs": [],
      "source": [
        "states = [\"Washington\", \"New Mexico\", \"Texas\", \"Mississippi\", \"Alaska\"]\n",
        "\n",
        "ai_2 = AsyncAIChat(api_key=api_key, console=False)\n",
        "for state in states:\n",
        "    ai_2.new_session(api_key=api_key, id=state)"
      ]
    },
    {
      "attachments": {},
      "cell_type": "markdown",
      "metadata": {
        "id": "oewS5NAVpNwT"
      },
      "source": [
        "This implementation is slightly more complicated since you need to wrap each async generator in its own async function. However, it provides the best demonstration of async, as you can clearly see that each chunk is received in a different order."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 40,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HVrZ16aXpAYm",
        "outputId": "9015c66a-fbf1-4cb6-bbbf-ef62b1a6bf79"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "{'delta': 'The', 'response': 'The'}\n",
            "{'delta': 'The', 'response': 'The'}\n",
            "{'delta': ' capital', 'response': 'The capital'}\n",
            "{'delta': ' capital', 'response': 'The capital'}\n",
            "{'delta': ' of', 'response': 'The capital of'}\n",
            "{'delta': ' of', 'response': 'The capital of'}\n",
            "{'delta': 'The', 'response': 'The'}\n",
            "{'delta': 'The', 'response': 'The'}\n",
            "{'delta': ' Washington', 'response': 'The capital of Washington'}\n",
            "{'delta': ' Mississippi', 'response': 'The capital of Mississippi'}\n",
            "{'delta': 'The', 'response': 'The'}\n",
            "{'delta': ' capital', 'response': 'The capital'}\n",
            "{'delta': ' capital', 'response': 'The capital'}\n",
            "{'delta': ' is', 'response': 'The capital of Washington is'}\n",
            "{'delta': ' is', 'response': 'The capital of Mississippi is'}\n",
            "{'delta': ' of', 'response': 'The capital of'}\n",
            "{'delta': ' capital', 'response': 'The capital'}\n",
            "{'delta': ' of', 'response': 'The capital of'}\n",
            "{'delta': ' Jackson', 'response': 'The capital of Mississippi is Jackson'}\n",
            "{'delta': ' Olympia', 'response': 'The capital of Washington is Olympia'}\n",
            "{'delta': ' Alaska', 'response': 'The capital of Alaska'}\n",
            "{'delta': ' New', 'response': 'The capital of New'}\n",
            "{'delta': '.', 'response': 'The capital of Washington is Olympia.'}\n",
            "{'delta': ' of', 'response': 'The capital of'}\n",
            "{'delta': '.', 'response': 'The capital of Mississippi is Jackson.'}\n",
            "{'delta': ' Mexico', 'response': 'The capital of New Mexico'}\n",
            "{'delta': ' is', 'response': 'The capital of Alaska is'}\n",
            "{'delta': ' Texas', 'response': 'The capital of Texas'}\n",
            "{'delta': ' is', 'response': 'The capital of New Mexico is'}\n",
            "{'delta': ' June', 'response': 'The capital of Alaska is June'}\n",
            "{'delta': ' is', 'response': 'The capital of Texas is'}\n",
            "{'delta': ' Santa', 'response': 'The capital of New Mexico is Santa'}\n",
            "{'delta': ' Austin', 'response': 'The capital of Texas is Austin'}\n",
            "{'delta': 'au', 'response': 'The capital of Alaska is Juneau'}\n",
            "{'delta': ' Fe', 'response': 'The capital of New Mexico is Santa Fe'}\n",
            "{'delta': '.', 'response': 'The capital of Texas is Austin.'}\n",
            "{'delta': '.', 'response': 'The capital of Alaska is Juneau.'}\n",
            "{'delta': '.', 'response': 'The capital of New Mexico is Santa Fe.'}\n"
          ]
        },
        {
          "data": {
            "text/plain": [
              "['The capital of Washington is Olympia.',\n",
              " 'The capital of New Mexico is Santa Fe.',\n",
              " 'The capital of Texas is Austin.',\n",
              " 'The capital of Mississippi is Jackson.',\n",
              " 'The capital of Alaska is Juneau.']"
            ]
          },
          "execution_count": 40,
          "metadata": {},
          "output_type": "execute_result"
        }
      ],
      "source": [
        "async def capital_stream(state):\n",
        "    async for chunk in await ai_2.stream(f\"What is the capital of {state}?\", id=state):\n",
        "        response = chunk\n",
        "        print(response)\n",
        "    return response[\"response\"]\n",
        "\n",
        "tasks = []\n",
        "for state in states:\n",
        "    tasks.append(capital_stream(state))\n",
        "\n",
        "results = await asyncio.gather(*tasks)\n",
        "results"
      ]
    },
    {
      "attachments": {},
      "cell_type": "markdown",
      "metadata": {},
      "source": [
        "## MIT License\n",
        "\n",
        "Copyright (c) 2023 Max Woolf\n",
        "\n",
        "Permission is hereby granted, free of charge, to any person obtaining a copy\n",
        "of this software and associated documentation files (the \"Software\"), to deal\n",
        "in the Software without restriction, including without limitation the rights\n",
        "to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n",
        "copies of the Software, and to permit persons to whom the Software is\n",
        "furnished to do so, subject to the following conditions:\n",
        "\n",
        "The above copyright notice and this permission notice shall be included in all\n",
        "copies or substantial portions of the Software.\n",
        "\n",
        "THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n",
        "IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n",
        "FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n",
        "AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n",
        "LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n",
        "OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\n",
        "SOFTWARE.\n"
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "display_name": "Python 3",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.9.12"
    },
    "orig_nbformat": 4
  },
  "nbformat": 4,
  "nbformat_minor": 0
}
```

## File: `examples/notebooks/simpleaichat_coding.ipynb`
```
{
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "# Efficient Coding Assistant with simpleaichat\n",
        "\n",
        "_Updated using `gpt-3.5-turbo-0613`_\n",
        "\n",
        "Many coders use ChatGPT for coding help, however the web interface can be slow and contain unnecessary discussion when you want code. With some system prompt engineering and simplechatapi streaming, you can cut down code time generation and costs significantly.\n",
        "\n",
        "**DISCLAIMER: Your mileage may vary in terms of code quality and accuracy in practice, but this is a good, hackable starting point.**\n",
        "\n"
      ],
      "metadata": {
        "id": "-jfTDBnMbGO3"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "5ZeSKyedacCE"
      },
      "outputs": [],
      "source": [
        "!pip install -q simpleaichat\n",
        "\n",
        "from simpleaichat import AIChat\n",
        "from getpass import getpass"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "For the following cell, input your OpenAI API key when prompted. **It will not be saved to the notebook**."
      ],
      "metadata": {
        "id": "1kXTv7zXapit"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "api_key = getpass(\"OpenAI Key: \")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "e_3QIHtnaqdw",
        "outputId": "334508c7-d1da-4270-b98d-359da120ceff"
      },
      "execution_count": 2,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "OpenAI Key: ··········\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "id": "mxBkiR9FacCF"
      },
      "outputs": [],
      "source": [
        "params = {\"temperature\": 0.0}  # for reproducibility\n",
        "model = \"gpt-3.5-turbo\"  # in production, may want to use model=\"gpt-4\" if have access\n",
        "\n",
        "ai = AIChat(api_key=api_key, console=False, params=params, model=model)"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Let's start with a simple `is_palindrome()` function in Python, and track how long it takes to run. The output of this should be similar to what is shown in the ChatGPT webapp."
      ],
      "metadata": {
        "id": "-4eVxf3Jawo_"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "SCkboiHsacCG",
        "outputId": "1608a19a-23e2-4555-c096-98d5bd08f51f"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Sure! Here's an example of an is_palindrome() function in Python:\n",
            "\n",
            "```python\n",
            "def is_palindrome(word):\n",
            "    # Convert the word to lowercase and remove any spaces\n",
            "    word = word.lower().replace(\" \", \"\")\n",
            "    \n",
            "    # Check if the word is equal to its reverse\n",
            "    if word == word[::-1]:\n",
            "        return True\n",
            "    else:\n",
            "        return False\n",
            "```\n",
            "\n",
            "You can use this function to check if a word is a palindrome. It will return True if the word is a palindrome and False otherwise.\n",
            "\n",
            "\n",
            "\n",
            "CPU times: user 23.7 ms, sys: 1.32 ms, total: 25 ms\n",
            "Wall time: 2.49 s\n"
          ]
        }
      ],
      "source": [
        "%%time\n",
        "response = ai(\"Write an is_palindrome() function in Python.\")\n",
        "print(response)\n",
        "print(\"\\n\\n\")  # separate time from generated text for readability"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "That's the typical implementation. However, there's a trick to cut the processing time in half, well known by technical hiring managers who want to trip up prospective candidates.\n",
        "\n",
        "ChatGPT outputs the statistically most common implementation, but it's not necessairily the best. A second pass allows ChatGPT to refine its output."
      ],
      "metadata": {
        "id": "dBOCM4LMbz3C"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 5,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BwsfrcPHacCH",
        "outputId": "dcbfdce5-8f72-4d00-cfe9-6eef41018639"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Certainly! Here's an optimized version of the is_palindrome() function that uses two pointers to check if a word is a palindrome:\n",
            "\n",
            "```python\n",
            "def is_palindrome(word):\n",
            "    # Convert the word to lowercase and remove any spaces\n",
            "    word = word.lower().replace(\" \", \"\")\n",
            "    \n",
            "    # Initialize two pointers, one at the start and one at the end of the word\n",
            "    left = 0\n",
            "    right = len(word) - 1\n",
            "    \n",
            "    # Iterate until the pointers meet in the middle\n",
            "    while left < right:\n",
            "        # If the characters at the pointers are not equal, the word is not a palindrome\n",
            "        if word[left] != word[right]:\n",
            "            return False\n",
            "        \n",
            "        # Move the pointers towards the middle\n",
            "        left += 1\n",
            "        right -= 1\n",
            "    \n",
            "    # If the loop completes without returning False, the word is a palindrome\n",
            "    return True\n",
            "```\n",
            "\n",
            "This optimized version reduces the number of comparisons by using two pointers that start at opposite ends of the word and move towards the middle. It will return True if the word is a palindrome and False otherwise.\n",
            "\n",
            "\n",
            "\n",
            "CPU times: user 30.7 ms, sys: 4.91 ms, total: 35.6 ms\n",
            "Wall time: 4.22 s\n"
          ]
        }
      ],
      "source": [
        "%%time\n",
        "response = ai(\"Make it more efficient.\")\n",
        "print(response)\n",
        "print(\"\\n\\n\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 6,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZWRKL30uacCH",
        "outputId": "ac47340b-9c7a-4517-a36a-d4fb92765311"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "511"
            ]
          },
          "metadata": {},
          "execution_count": 6
        }
      ],
      "source": [
        "ai.total_length"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "In all, it took ~6 seconds and utilized 511 tokens. But there's a lot of unnecessary natter in the output:\n",
        "\n",
        "- The conversational preamble before the code\n",
        "- Docstrings and code comments\n",
        "- A long explanation of the code which may be redundant to the above\n",
        "\n",
        "All this natter adds latency and cost.\n",
        "\n",
        "The easiest technique to guide AI text generation is to use **prompt engineering**, specifically to give it a new system prompt to say precisely what you want. As of June 27th 2023, the default ChatGPT API responds very well to commands.\n",
        "\n",
        "Now, for the new `system` prompt:"
      ],
      "metadata": {
        "id": "okqqoe7lcqUH"
      }
    },
    {
      "cell_type": "code",
      "execution_count": 7,
      "metadata": {
        "id": "iA9AASKfacCH"
      },
      "outputs": [],
      "source": [
        "system_optimized = \"\"\"Write a Python function based on the user input.\n",
        "\n",
        "You must obey ALL the following rules:\n",
        "- Only respond with the Python function.\n",
        "- Never put in-line comments or docstrings in your code.\"\"\"\n",
        "\n",
        "ai_2 = AIChat(api_key=api_key, system=system_optimized, model=model, params=params)"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 8,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MRYfniAXacCI",
        "outputId": "fecb6928-a1e8-48f6-c336-5055cbca7a38"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "def is_palindrome(word):\n",
            "    return word == word[::-1]\n",
            "\n",
            "\n",
            "\n",
            "CPU times: user 11.6 ms, sys: 4.01 ms, total: 15.6 ms\n",
            "Wall time: 1.04 s\n"
          ]
        }
      ],
      "source": [
        "%%time\n",
        "response = ai_2(\"is_palindrome\")\n",
        "print(response)\n",
        "print(\"\\n\\n\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 9,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "lGJr-GfIacCI",
        "outputId": "68a555bd-d3e0-4b39-cca6-a11ce6ad1455"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "def is_palindrome(word):\n",
            "    length = len(word)\n",
            "    for i in range(length // 2):\n",
            "        if word[i] != word[length - i - 1]:\n",
            "            return False\n",
            "    return True\n",
            "\n",
            "\n",
            "\n",
            "CPU times: user 19.7 ms, sys: 1.73 ms, total: 21.5 ms\n",
            "Wall time: 2.64 s\n"
          ]
        }
      ],
      "source": [
        "%%time\n",
        "response = ai_2(\"Make it more efficient.\")\n",
        "print(response)\n",
        "print(\"\\n\\n\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 10,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8eMDXGysacCJ",
        "outputId": "0d6272c1-cb2a-460b-fe37-09c896b119e7"
      },
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "190"
            ]
          },
          "metadata": {},
          "execution_count": 10
        }
      ],
      "source": [
        "ai_2.total_length"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "~3 seconds total with 190 tokens used: that's 2x faster at 1/3 the cost!"
      ],
      "metadata": {
        "id": "ua28VqKteKkr"
      }
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "SaE3ftkMacCJ"
      },
      "source": [
        "## Create a Function\n",
        "\n",
        "Now we can create a function to automate the two calls we did above for any arbitrary input.\n",
        "\n",
        "For each call, we'll create an independent temporary session within simpleaichat and then clean it up. We'll also use a regex to strip unneded backticks."
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 11,
      "metadata": {
        "id": "mN_-3fwuacCL"
      },
      "outputs": [],
      "source": [
        "from uuid import uuid4\n",
        "import re\n",
        "\n",
        "ai_func = AIChat(api_key=api_key, console=False)\n",
        "def gen_code(query):\n",
        "    id = uuid4()\n",
        "    ai_func.new_session(api_key=api_key, id=id, system=system_optimized, params=params, model=model)\n",
        "    _ = ai_func(query, id=id)\n",
        "    response_optimized = ai_func(\"Make it more efficient.\", id=id)\n",
        "\n",
        "    ai_func.delete_session(id=id)\n",
        "    return response_optimized"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 12,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "kIkdpBwOacCL",
        "outputId": "f00c393b-87c0-4bc6-9c35-d323c6de6812"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "def is_palindrome(word):\n",
            "    length = len(word)\n",
            "    for i in range(length // 2):\n",
            "        if word[i] != word[length - i - 1]:\n",
            "            return False\n",
            "    return True\n",
            "\n",
            "\n",
            "\n",
            "CPU times: user 27.8 ms, sys: 1.94 ms, total: 29.8 ms\n",
            "Wall time: 1.96 s\n"
          ]
        }
      ],
      "source": [
        "%%time\n",
        "code = gen_code(\"is_palindrome\")\n",
        "print(code)\n",
        "print(\"\\n\\n\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 13,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "S1LjZjFBacCM",
        "outputId": "53d96baf-1f6b-46fb-bba8-5eda772d8c87"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "def reverse_string(string):\n",
            "    return ''.join(reversed(string))\n",
            "\n",
            "\n",
            "\n",
            "CPU times: user 16.4 ms, sys: 644 µs, total: 17 ms\n",
            "Wall time: 1.42 s\n"
          ]
        }
      ],
      "source": [
        "%%time\n",
        "code = gen_code(\"reverse string\")\n",
        "print(code)\n",
        "print(\"\\n\\n\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 14,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "VdSNUiapacCM",
        "outputId": "207634e0-ef48-4428-a3c0-15a80ad845f8"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "def pretty_print_dict(dictionary):\n",
            "    import json\n",
            "    print(json.dumps(dictionary, indent=4, separators=(',', ': ')))\n",
            "\n",
            "\n",
            "\n",
            "CPU times: user 17.2 ms, sys: 1.87 ms, total: 19.1 ms\n",
            "Wall time: 1.31 s\n"
          ]
        }
      ],
      "source": [
        "%%time\n",
        "code = gen_code(\"pretty print dict\")\n",
        "print(code)\n",
        "print(\"\\n\\n\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 15,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7ppyZrFTacCM",
        "outputId": "a4e04c60-4681-4d7f-b846-028a9b1271f6"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "import cv2\n",
            "\n",
            "def load_and_flip_image(image_path):\n",
            "    image = cv2.imread(image_path)\n",
            "    flipped_image = cv2.flip(image, 1)\n",
            "    cv2.imwrite(\"flipped_image.jpg\", flipped_image)\n",
            "    return \"flipped_image.jpg\"\n",
            "\n",
            "\n",
            "\n",
            "CPU times: user 21.1 ms, sys: 3.86 ms, total: 24.9 ms\n",
            "Wall time: 2.18 s\n"
          ]
        }
      ],
      "source": [
        "%%time\n",
        "code = gen_code(\"load and flip image horizontally\")\n",
        "print(code)\n",
        "print(\"\\n\\n\")"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 16,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "sNQhAKFqacCM",
        "outputId": "fcfc568f-0777-4df4-a8f7-20fa0e4e34d7"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "import hashlib\n",
            "from multiprocessing import Pool, cpu_count\n",
            "\n",
            "def multiprocess_hash(data):\n",
            "    def hash_string(string):\n",
            "        return hashlib.sha256(string.encode()).hexdigest()\n",
            "\n",
            "    num_processes = cpu_count()\n",
            "    pool = Pool(processes=num_processes)\n",
            "    hashed_data = pool.map(hash_string, data)\n",
            "    pool.close()\n",
            "    pool.join()\n",
            "\n",
            "    return hashed_data\n",
            "\n",
            "\n",
            "\n",
            "CPU times: user 28.8 ms, sys: 3.82 ms, total: 32.6 ms\n",
            "Wall time: 3.31 s\n"
          ]
        }
      ],
      "source": [
        "%%time\n",
        "code = gen_code(\"multiprocess hash\")\n",
        "print(code)\n",
        "print(\"\\n\\n\")"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Generating Optimized Code in a Single API Call w/ Structured Output Data\n",
        "\n",
        "Sometimes you may not want to make two calls to OpenAI. One hack you can do is to define an expected structured output to tell it to sequentially generate the normal code output, then the optimized output.\n",
        "\n",
        "This structure is essentially a different form of prompt engineering, but you can combine it with a system prompt if needed.\n",
        "\n",
        "This will also further increase response speed, but may not necessairly result in fewer tokens used."
      ],
      "metadata": {
        "id": "tbQspzba2_GO"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from pydantic import BaseModel, Field\n",
        "import orjson\n",
        "\n",
        "class write_python_function(BaseModel):\n",
        "    \"\"\"Writes a Python function based on the user input.\"\"\"\n",
        "    code: str = Field(description=\"Python code\")\n",
        "    efficient_code: str = Field(description=\"More efficient Python code than previously written\")"
      ],
      "metadata": {
        "id": "lFCLUODV28FZ"
      },
      "execution_count": 23,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "ai_struct = AIChat(api_key=api_key, console=False, model=model, params=params, save_messages=False)"
      ],
      "metadata": {
        "id": "6rTqftko4N2L"
      },
      "execution_count": 24,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "%%time\n",
        "response_structured = ai_struct(\"is_palindrome\", output_schema=write_python_function)\n",
        "\n",
        "# orjson.dumps preserves field order from the ChatGPT API\n",
        "print(orjson.dumps(response_structured, option=orjson.OPT_INDENT_2).decode())\n",
        "print(\"\\n\\n\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4ielJLnz4e5U",
        "outputId": "d9b3f315-1840-4781-b922-f0cd889a4086"
      },
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "{\n",
            "  \"code\": \"def is_palindrome(s):\\n    return s == s[::-1]\",\n",
            "  \"efficient_code\": \"def is_palindrome(s):\\n    n = len(s)\\n    for i in range(n // 2):\\n        if s[i] != s[n - i - 1]:\\n            return False\\n    return True\"\n",
            "}\n",
            "\n",
            "\n",
            "\n",
            "CPU times: user 131 ms, sys: 1.39 ms, total: 133 ms\n",
            "Wall time: 1.67 s\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "As evident, the output is a `dict` so you'd just return the `efficient_code` field."
      ],
      "metadata": {
        "id": "M8sshigf53Nq"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print(response_structured[\"efficient_code\"])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "eIKI_8aq51RH",
        "outputId": "ab239077-3114-4b52-a127-0c5a93308627"
      },
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "def is_palindrome(s):\n",
            "    n = len(s)\n",
            "    for i in range(n // 2):\n",
            "        if s[i] != s[n - i - 1]:\n",
            "            return False\n",
            "    return True\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "ai_struct.total_length"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "KThchw1S7MwS",
        "outputId": "059aedeb-13c9-4802-a0cf-239ff7384722"
      },
      "execution_count": 27,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "161"
            ]
          },
          "metadata": {},
          "execution_count": 27
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Token-wise it's about the same, but there's a significant speedup in generation for short queries such as these."
      ],
      "metadata": {
        "id": "iQcNrZcK7bn1"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Trying the other examples:"
      ],
      "metadata": {
        "id": "v2tfYs3a6oBy"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "%%time\n",
        "response_structured = ai_struct(\"reverse string\", output_schema=write_python_function)\n",
        "print(response_structured[\"efficient_code\"])\n",
        "print(\"\\n\\n\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ZrJtaW5m7Cdy",
        "outputId": "a74621e8-cebc-495b-adaa-bec926de36dd"
      },
      "execution_count": 28,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "def reverse_string(s):\n",
            "    return ''.join(reversed(s))\n",
            "\n",
            "\n",
            "\n",
            "CPU times: user 24.6 ms, sys: 250 µs, total: 24.9 ms\n",
            "Wall time: 1.37 s\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "%%time\n",
        "response_structured = ai_struct(\"load and flip image horizontally\", output_schema=write_python_function)\n",
        "print(response_structured[\"efficient_code\"])\n",
        "print(\"\\n\\n\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "JJxRji6h8Gww",
        "outputId": "45dbf068-b9b2-4d04-fccb-f988eda5538f"
      },
      "execution_count": 29,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "from PIL import Image\n",
            "\n",
            "def load_and_flip_image_horizontally(image_path):\n",
            "    return Image.open(image_path).transpose(Image.FLIP_LEFT_RIGHT)\n",
            "\n",
            "\n",
            "\n",
            "CPU times: user 15.4 ms, sys: 2.15 ms, total: 17.6 ms\n",
            "Wall time: 1.79 s\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "## MIT License\n",
        "\n",
        "Copyright (c) 2023 Max Woolf\n",
        "\n",
        "Permission is hereby granted, free of charge, to any person obtaining a copy\n",
        "of this software and associated documentation files (the \"Software\"), to deal\n",
        "in the Software without restriction, including without limitation the rights\n",
        "to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n",
        "copies of the Software, and to permit persons to whom the Software is\n",
        "furnished to do so, subject to the following conditions:\n",
        "\n",
        "The above copyright notice and this permission notice shall be included in all\n",
        "copies or substantial portions of the Software.\n",
        "\n",
        "THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n",
        "IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n",
        "FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n",
        "AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n",
        "LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n",
        "OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\n",
        "SOFTWARE.\n"
      ],
      "metadata": {
        "id": "E-QaAsRXbhAj"
      }
    }
  ],
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.9.12"
    },
    "orig_nbformat": 4,
    "colab": {
      "provenance": []
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}
```

## File: `simpleaichat/__init__.py`
```python
from .simpleaichat import AIChat, AsyncAIChat
```

## File: `simpleaichat/chatgpt.py`
```python
from typing import Any, Dict, List, Set, Union

import orjson
from httpx import AsyncClient, Client
from pydantic import HttpUrl

from .models import ChatMessage, ChatSession
from .utils import remove_a_key

tool_prompt = """From the list of tools below:
- Reply ONLY with the number of the tool appropriate in response to the user's last message.
- If no tool is appropriate, ONLY reply with \"0\".

{tools}"""


class ChatGPTSession(ChatSession):
    api_url: HttpUrl = "https://api.openai.com/v1/chat/completions"
    input_fields: Set[str] = {"role", "content", "name"}
    system: str = "You are a helpful assistant."
    params: Dict[str, Any] = {"temperature": 0.7}

    def prepare_request(
        self,
        prompt: str,
        system: str = None,
        params: Dict[str, Any] = None,
        stream: bool = False,
        input_schema: Any = None,
        output_schema: Any = None,
        is_function_calling_required: bool = True,
    ):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.auth['api_key'].get_secret_value()}",
        }

        system_message = ChatMessage(role="system", content=system or self.system)
        if not input_schema:
            user_message = ChatMessage(role="user", content=prompt)
        else:
            assert isinstance(
                prompt, input_schema
            ), f"prompt must be an instance of {input_schema.__name__}"
            user_message = ChatMessage(
                role="function",
                content=prompt.model_dump_json(),
                name=input_schema.__name__,
            )

        gen_params = params or self.params
        data = {
            "model": self.model,
            "messages": self.format_input_messages(system_message, user_message),
            "stream": stream,
            **gen_params,
        }

        # Add function calling parameters if a schema is provided
        if input_schema or output_schema:
            functions = []
            if input_schema:
                input_function = self.schema_to_function(input_schema)
                functions.append(input_function)
            if output_schema:
                output_function = self.schema_to_function(output_schema)
                functions.append(
                    output_function
                ) if output_function not in functions else None
                if is_function_calling_required:
                    data["function_call"] = {"name": output_schema.__name__}
            data["functions"] = functions

        return headers, data, user_message

    def schema_to_function(self, schema: Any):
        assert schema.__doc__, f"{schema.__name__} is missing a docstring."
        assert (
            "title" not in schema.model_fields.keys()
        ), "`title` is a reserved keyword and cannot be used as a field name."
        schema_dict = schema.model_json_schema()
        remove_a_key(schema_dict, "title")

        return {
            "name": schema.__name__,
            "description": schema.__doc__,
            "parameters": schema_dict,
        }

    def gen(
        self,
        prompt: str,
        client: Union[Client, AsyncClient],
        system: str = None,
        save_messages: bool = None,
        params: Dict[str, Any] = None,
        input_schema: Any = None,
        output_schema: Any = None,
    ):
        headers, data, user_message = self.prepare_request(
            prompt, system, params, False, input_schema, output_schema
        )

        r = client.post(
            str(self.api_url),
            json=data,
            headers=headers,
            timeout=None,
        )
        r = r.json()

        try:
            if not output_schema:
                content = r["choices"][0]["message"]["content"]
                assistant_message = ChatMessage(
                    role=r["choices"][0]["message"]["role"],
                    content=content,
                    finish_reason=r["choices"][0]["finish_reason"],
                    prompt_length=r["usage"]["prompt_tokens"],
                    completion_length=r["usage"]["completion_tokens"],
                    total_length=r["usage"]["total_tokens"],
                )
                self.add_messages(user_message, assistant_message, save_messages)
            else:
                content = r["choices"][0]["message"]["function_call"]["arguments"]
                content = orjson.loads(content)

            self.total_prompt_length += r["usage"]["prompt_tokens"]
            self.total_completion_length += r["usage"]["completion_tokens"]
            self.total_length += r["usage"]["total_tokens"]
        except KeyError:
            raise KeyError(f"No AI generation: {r}")

        return content

    def stream(
        self,
        prompt: str,
        client: Union[Client, AsyncClient],
        system: str = None,
        save_messages: bool = None,
        params: Dict[str, Any] = None,
        input_schema: Any = None,
    ):
        headers, data, user_message = self.prepare_request(
            prompt, system, params, True, input_schema
        )

        with client.stream(
            "POST",
            str(self.api_url),
            json=data,
            headers=headers,
            timeout=None,
        ) as r:
            content = []
            for chunk in r.iter_lines():
                if len(chunk) > 0:
                    chunk = chunk[6:]  # SSE JSON chunks are prepended with "data: "
                    if chunk != "[DONE]":
                        chunk_dict = orjson.loads(chunk)
                        delta = chunk_dict["choices"][0]["delta"].get("content")
                        if delta:
                            content.append(delta)
                            yield {"delta": delta, "response": "".join(content)}

        # streaming does not currently return token counts
        assistant_message = ChatMessage(
            role="assistant",
            content="".join(content),
        )

        self.add_messages(user_message, assistant_message, save_messages)

        return assistant_message

    def gen_with_tools(
        self,
        prompt: str,
        tools: List[Any],
        client: Union[Client, AsyncClient],
        system: str = None,
        save_messages: bool = None,
        params: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        # call 1: select tool and populate context
        tools_list = "\n".join(f"{i+1}: {f.__doc__}" for i, f in enumerate(tools))
        tool_prompt_format = tool_prompt.format(tools=tools_list)

        logit_bias_weight = 100
        logit_bias = {str(k): logit_bias_weight for k in range(15, 15 + len(tools) + 1)}

        tool_idx = int(
            self.gen(
                prompt,
                client=client,
                system=tool_prompt_format,
                save_messages=False,
                params={
                    "temperature": 0.0,
                    "max_tokens": 1,
                    "logit_bias": logit_bias,
                },
            )
        )

        # if no tool is selected, do a standard generation instead.
        if tool_idx == 0:
            return {
                "response": self.gen(
                    prompt,
                    client=client,
                    system=system,
                    save_messages=save_messages,
                    params=params,
                ),
                "tool": None,
            }
        selected_tool = tools[tool_idx - 1]
        context_dict = selected_tool(prompt)
        if isinstance(context_dict, str):
            context_dict = {"context": context_dict}

        context_dict["tool"] = selected_tool.__name__

        # call 2: generate from the context
        new_system = f"{system or self.system}\n\nYou MUST use information from the context in your response."
        new_prompt = f"Context: {context_dict['context']}\n\nUser: {prompt}"

        context_dict["response"] = self.gen(
            new_prompt,
            client=client,
            system=new_system,
            save_messages=False,
            params=params,
        )

        # manually append the nonmodified user message + normal AI response
        user_message = ChatMessage(role="user", content=prompt)
        assistant_message = ChatMessage(
            role="assistant", content=context_dict["response"]
        )
        self.add_messages(user_message, assistant_message, save_messages)

        return context_dict

    async def gen_async(
        self,
        prompt: str,
        client: Union[Client, AsyncClient],
        system: str = None,
        save_messages: bool = None,
        params: Dict[str, Any] = None,
        input_schema: Any = None,
        output_schema: Any = None,
    ):
        headers, data, user_message = self.prepare_request(
            prompt, system, params, False, input_schema, output_schema
        )

        r = await client.post(
            str(self.api_url),
            json=data,
            headers=headers,
            timeout=None,
        )
        r = r.json()

        try:
            if not output_schema:
                content = r["choices"][0]["message"]["content"]
                assistant_message = ChatMessage(
                    role=r["choices"][0]["message"]["role"],
                    content=content,
                    finish_reason=r["choices"][0]["finish_reason"],
                    prompt_length=r["usage"]["prompt_tokens"],
                    completion_length=r["usage"]["completion_tokens"],
                    total_length=r["usage"]["total_tokens"],
                )
                self.add_messages(user_message, assistant_message, save_messages)
            else:
                content = r["choices"][0]["message"]["function_call"]["arguments"]
                content = orjson.loads(content)

            self.total_prompt_length += r["usage"]["prompt_tokens"]
            self.total_completion_length += r["usage"]["completion_tokens"]
            self.total_length += r["usage"]["total_tokens"]
        except KeyError:
            raise KeyError(f"No AI generation: {r}")

        return content

    async def stream_async(
        self,
        prompt: str,
        client: Union[Client, AsyncClient],
        system: str = None,
        save_messages: bool = None,
        params: Dict[str, Any] = None,
        input_schema: Any = None,
    ):
        headers, data, user_message = self.prepare_request(
            prompt, system, params, True, input_schema
        )

        async with client.stream(
            "POST",
            str(self.api_url),
            json=data,
            headers=headers,
            timeout=None,
        ) as r:
            content = []
            async for chunk in r.aiter_lines():
                if len(chunk) > 0:
                    chunk = chunk[6:]  # SSE JSON chunks are prepended with "data: "
                    if chunk != "[DONE]":
                        chunk_dict = orjson.loads(chunk)
                        delta = chunk_dict["choices"][0]["delta"].get("content")
                        if delta:
                            content.append(delta)
                            yield {"delta": delta, "response": "".join(content)}

        # streaming does not currently return token counts
        assistant_message = ChatMessage(
            role="assistant",
            content="".join(content),
        )

        self.add_messages(user_message, assistant_message, save_messages)

    async def gen_with_tools_async(
        self,
        prompt: str,
        tools: List[Any],
        client: Union[Client, AsyncClient],
        system: str = None,
        save_messages: bool = None,
        params: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        # call 1: select tool and populate context
        tools_list = "\n".join(f"{i+1}: {f.__doc__}" for i, f in enumerate(tools))
        tool_prompt_format = tool_prompt.format(tools=tools_list)

        logit_bias_weight = 100
        logit_bias = {str(k): logit_bias_weight for k in range(15, 15 + len(tools) + 1)}

        tool_idx = int(
            await self.gen_async(
                prompt,
                client=client,
                system=tool_prompt_format,
                save_messages=False,
                params={
                    "temperature": 0.0,
                    "max_tokens": 1,
                    "logit_bias": logit_bias,
                },
            )
        )

        # if no tool is selected, do a standard generation instead.
        if tool_idx == 0:
            return {
                "response": await self.gen_async(
                    prompt,
                    client=client,
                    system=system,
                    save_messages=save_messages,
                    params=params,
                ),
                "tool": None,
            }
        selected_tool = tools[tool_idx - 1]
        context_dict = await selected_tool(prompt)
        if isinstance(context_dict, str):
            context_dict = {"context": context_dict}

        context_dict["tool"] = selected_tool.__name__

        # call 2: generate from the context
        new_system = f"{system or self.system}\n\nYou MUST use information from the context in your response."
        new_prompt = f"Context: {context_dict['context']}\n\nUser: {prompt}"

        context_dict["response"] = await self.gen_async(
            new_prompt,
            client=client,
            system=new_system,
            save_messages=False,
            params=params,
        )

        # manually append the nonmodified user message + normal AI response
        user_message = ChatMessage(role="user", content=prompt)
        assistant_message = ChatMessage(
            role="assistant", content=context_dict["response"]
        )
        self.add_messages(user_message, assistant_message, save_messages)

        return context_dict
```

## File: `simpleaichat/cli.py`
```python
import argparse
import os
from getpass import getpass

import fire
from dotenv import load_dotenv

from .simpleaichat import AIChat

load_dotenv()

parser = argparse.ArgumentParser()
parser.add_argument("character", help="Specify the character", default=None, nargs="?")
parser.add_argument(
    "character_command", help="Specify the character command", default=None, nargs="?"
)
parser.add_argument("--prime", action="store_true", help="Enable priming")

ARGS = parser.parse_args()


def interactive_chat():
    gpt_api_key = os.getenv("OPENAI_API_KEY")
    if not gpt_api_key:
        gpt_api_key = getpass("Input your OpenAI key here: ")
    assert gpt_api_key, "An API key was not defined."
    _ = AIChat(ARGS.character, ARGS.character_command, ARGS.prime)


if __name__ == "__main__":
    fire.Fire(interactive_chat)
```

## File: `simpleaichat/models.py`
```python
import datetime
from typing import Any, Dict, List, Optional, Set, Union
from uuid import UUID, uuid4

import orjson
from pydantic import BaseModel, Field, HttpUrl, SecretStr


def orjson_dumps(v, *, default, **kwargs):
    # orjson.dumps returns bytes, to match standard json.dumps we need to decode
    return orjson.dumps(v, default=default, **kwargs).decode()


def now_tz():
    # Need datetime w/ timezone for cleanliness
    # https://stackoverflow.com/a/24666683
    return datetime.datetime.now(datetime.timezone.utc)


class ChatMessage(BaseModel):
    role: str
    content: str
    name: Optional[str] = None
    function_call: Optional[str] = None
    received_at: datetime.datetime = Field(default_factory=now_tz)
    finish_reason: Optional[str] = None
    prompt_length: Optional[int] = None
    completion_length: Optional[int] = None
    total_length: Optional[int] = None

    def __str__(self) -> str:
        return str(self.model_dump(exclude_none=True))


class ChatSession(BaseModel):
    id: Union[str, UUID] = Field(default_factory=uuid4)
    created_at: datetime.datetime = Field(default_factory=now_tz)
    auth: Dict[str, SecretStr]
    api_url: HttpUrl
    model: str
    system: str
    params: Dict[str, Any] = {}
    messages: List[ChatMessage] = []
    input_fields: Set[str] = {}
    recent_messages: Optional[int] = None
    save_messages: Optional[bool] = True
    total_prompt_length: int = 0
    total_completion_length: int = 0
    total_length: int = 0
    title: Optional[str] = None

    def __str__(self) -> str:
        sess_start_str = self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        last_message_str = self.messages[-1].received_at.strftime("%Y-%m-%d %H:%M:%S")
        return f"""Chat session started at {sess_start_str}:
        - {len(self.messages):,} Messages
        - Last message sent at {last_message_str}"""

    def format_input_messages(
        self, system_message: ChatMessage, user_message: ChatMessage
    ) -> list:
        recent_messages = (
            self.messages[-self.recent_messages :]
            if self.recent_messages
            else self.messages
        )
        return (
            [system_message.model_dump(include=self.input_fields, exclude_none=True)]
            + [
                m.model_dump(include=self.input_fields, exclude_none=True)
                for m in recent_messages
            ]
            + [user_message.model_dump(include=self.input_fields, exclude_none=True)]
        )

    def add_messages(
        self,
        user_message: ChatMessage,
        assistant_message: ChatMessage,
        save_messages: bool = None,
    ) -> None:
        # if save_messages is explicitly defined, always use that choice
        # instead of the default
        to_save = isinstance(save_messages, bool)

        if to_save:
            if save_messages:
                self.messages.append(user_message)
                self.messages.append(assistant_message)
        elif self.save_messages:
            self.messages.append(user_message)
            self.messages.append(assistant_message)
```

## File: `simpleaichat/simpleaichat.py`
```python
import csv
import datetime
import os
from contextlib import asynccontextmanager, contextmanager
from typing import Any, Dict, List, Optional, Union
from uuid import UUID, uuid4

import dateutil
import orjson
from dotenv import load_dotenv
from httpx import AsyncClient, Client
from pydantic import BaseModel
from rich.console import Console

from .chatgpt import ChatGPTSession
from .models import ChatMessage, ChatSession
from .utils import wikipedia_search_lookup

load_dotenv()


class AIChat(BaseModel):
    client: Any
    default_session: Optional[ChatSession]
    sessions: Dict[Union[str, UUID], ChatSession] = {}

    def __init__(
        self,
        character: str = None,
        character_command: str = None,
        system: str = None,
        id: Union[str, UUID] = uuid4(),
        prime: bool = True,
        default_session: bool = True,
        console: bool = True,
        **kwargs,
    ):
        client = Client(proxies=os.getenv("https_proxy"))
        system_format = self.build_system(character, character_command, system)

        sessions = {}
        new_default_session = None
        if default_session:
            new_session = self.new_session(
                return_session=True, system=system_format, id=id, **kwargs
            )

            new_default_session = new_session
            sessions = {new_session.id: new_session}

        super().__init__(
            client=client, default_session=new_default_session, sessions=sessions
        )

        if not system and console:
            character = "ChatGPT" if not character else character
            new_default_session.title = character
            self.interactive_console(character=character, prime=prime)

    def new_session(
        self,
        return_session: bool = False,
        **kwargs,
    ) -> Optional[ChatGPTSession]:
        if "model" not in kwargs:  # set default
            kwargs["model"] = "gpt-3.5-turbo"
        # TODO: Add support for more models (PaLM, Claude)
        if "gpt-" in kwargs["model"]:
            gpt_api_key = kwargs.get("api_key") or os.getenv("OPENAI_API_KEY")
            assert gpt_api_key, f"An API key for {kwargs['model'] } was not defined."
            sess = ChatGPTSession(
                auth={
                    "api_key": gpt_api_key,
                },
                **kwargs,
            )

        if return_session:
            return sess
        else:
            self.sessions[sess.id] = sess

    def get_session(self, id: Union[str, UUID] = None) -> ChatSession:
        try:
            sess = self.sessions[id] if id else self.default_session
        except KeyError:
            raise KeyError("No session by that key exists.")
        if not sess:
            raise ValueError("No default session exists.")
        return sess

    def reset_session(self, id: Union[str, UUID] = None) -> None:
        sess = self.get_session(id)
        sess.messages = []

    def delete_session(self, id: Union[str, UUID] = None) -> None:
        sess = self.get_session(id)
        if self.default_session:
            if sess.id == self.default_session.id:
                self.default_session = None
        del self.sessions[sess.id]
        del sess

    @contextmanager
    def session(self, **kwargs):
        sess = self.new_session(return_session=True, **kwargs)
        self.sessions[sess.id] = sess
        try:
            yield sess
        finally:
            self.delete_session(sess.id)

    def __call__(
        self,
        prompt: Union[str, Any],
        id: Union[str, UUID] = None,
        system: str = None,
        save_messages: bool = None,
        params: Dict[str, Any] = None,
        tools: List[Any] = None,
        input_schema: Any = None,
        output_schema: Any = None,
    ) -> str:
        sess = self.get_session(id)
        if tools:
            assert (input_schema is None) and (
                output_schema is None
            ), "When using tools, input/output schema are ignored"
            for tool in tools:
                assert tool.__doc__, f"Tool {tool} does not have a docstring."
            assert len(tools) <= 9, "You can only have a maximum of 9 tools."
            return sess.gen_with_tools(
                prompt,
                tools,
                client=self.client,
                system=system,
                save_messages=save_messages,
                params=params,
            )
        else:
            return sess.gen(
                prompt,
                client=self.client,
                system=system,
                save_messages=save_messages,
                params=params,
                input_schema=input_schema,
                output_schema=output_schema,
            )

    def stream(
        self,
        prompt: str,
        id: Union[str, UUID] = None,
        system: str = None,
        save_messages: bool = None,
        params: Dict[str, Any] = None,
        input_schema: Any = None,
    ) -> str:
        sess = self.get_session(id)
        return sess.stream(
            prompt,
            client=self.client,
            system=system,
            save_messages=save_messages,
            params=params,
            input_schema=input_schema,
        )

    def build_system(
        self, character: str = None, character_command: str = None, system: str = None
    ) -> str:
        default = "You are a helpful assistant."
        if character:
            character_prompt = """
            You must follow ALL these rules in all responses:
            - You are the following character and should ALWAYS act as them: {0}
            - NEVER speak in a formal tone.
            - Concisely introduce yourself first in character.
            """
            prompt = character_prompt.format(wikipedia_search_lookup(character)).strip()
            if character_command:
                character_system = """
                - {0}
                """
                prompt = (
                    prompt + "\n" + character_system.format(character_command).strip()
                )
            return prompt
        elif system:
            return system
        else:
            return default

    def interactive_console(self, character: str = None, prime: bool = True) -> None:
        console = Console(highlight=False, force_jupyter=False)
        sess = self.default_session
        ai_text_color = "bright_magenta"

        # prime with a unique starting response to the user
        if prime:
            console.print(f"[b]{character}[/b]: ", end="", style=ai_text_color)
            for chunk in sess.stream("Hello!", self.client):
                console.print(chunk["delta"], end="", style=ai_text_color)

        while True:
            console.print()
            try:
                user_input = console.input("[b]You:[/b] ").strip()
                if not user_input:
                    break

                console.print(f"[b]{character}[/b]: ", end="", style=ai_text_color)
                for chunk in sess.stream(user_input, self.client):
                    console.print(chunk["delta"], end="", style=ai_text_color)
            except KeyboardInterrupt:
                break

    def __str__(self) -> str:
        if self.default_session:
            return self.default_session.model_dump_json(
                exclude={"api_key", "api_url"},
                exclude_none=True,
            )

    def __repr__(self) -> str:
        return ""

    # Save/Load Chats given a session id
    def save_session(
        self,
        output_path: str = None,
        id: Union[str, UUID] = None,
        format: str = "csv",
        minify: bool = False,
    ):
        sess = self.get_session(id)
        sess_dict = sess.model_dump(
            exclude={"auth", "api_url", "input_fields"},
            exclude_none=True,
        )
        output_path = output_path or f"chat_session.{format}"
        if format == "csv":
            with open(output_path, "w", encoding="utf-8") as f:
                fields = [
                    "role",
                    "content",
                    "received_at",
                    "prompt_length",
                    "completion_length",
                    "total_length",
                    "finish_reason",
                ]
                w = csv.DictWriter(f, fieldnames=fields)
                w.writeheader()
                for message in sess_dict["messages"]:
                    # datetime must be in common format to be loaded into spreadsheet
                    # for human-readability, the timezone is set to local machine
                    local_datetime = message["received_at"].astimezone()
                    message["received_at"] = local_datetime.strftime(
                        "%Y-%m-%d %H:%M:%S"
                    )
                    w.writerow(message)
        elif format == "json":
            with open(output_path, "wb") as f:
                f.write(
                    orjson.dumps(
                        sess_dict, option=orjson.OPT_INDENT_2 if not minify else None
                    )
                )

    def load_session(self, input_path: str, id: Union[str, UUID] = uuid4(), **kwargs):
        assert input_path.endswith(".csv") or input_path.endswith(
            ".json"
        ), "Only CSV and JSON imports are accepted."

        if input_path.endswith(".csv"):
            with open(input_path, "r", encoding="utf-8") as f:
                r = csv.DictReader(f)
                messages = []
                for row in r:
                    # need to convert the datetime back to UTC
                    local_datetime = datetime.datetime.strptime(
                        row["received_at"], "%Y-%m-%d %H:%M:%S"
                    ).replace(tzinfo=dateutil.tz.tzlocal())
                    row["received_at"] = local_datetime.astimezone(
                        datetime.timezone.utc
                    )
                    # https://stackoverflow.com/a/68305271
                    row = {k: (None if v == "" else v) for k, v in row.items()}
                    messages.append(ChatMessage(**row))

            self.new_session(id=id, **kwargs)
            self.sessions[id].messages = messages

        if input_path.endswith(".json"):
            with open(input_path, "rb") as f:
                sess_dict = orjson.loads(f.read())
            # update session with info not loaded, e.g. auth/api_url
            for arg in kwargs:
                sess_dict[arg] = kwargs[arg]
            self.new_session(**sess_dict)

    # Tabulators for returning total token counts
    def message_totals(self, attr: str, id: Union[str, UUID] = None) -> int:
        sess = self.get_session(id)
        return getattr(sess, attr)

    @property
    def total_prompt_length(self, id: Union[str, UUID] = None) -> int:
        return self.message_totals("total_prompt_length", id)

    @property
    def total_completion_length(self, id: Union[str, UUID] = None) -> int:
        return self.message_totals("total_completion_length", id)

    @property
    def total_length(self, id: Union[str, UUID] = None) -> int:
        return self.message_totals("total_length", id)

    # alias total_tokens to total_length for common use
    @property
    def total_tokens(self, id: Union[str, UUID] = None) -> int:
        return self.total_length(id)


class AsyncAIChat(AIChat):
    async def __call__(
        self,
        prompt: str,
        id: Union[str, UUID] = None,
        system: str = None,
        save_messages: bool = None,
        params: Dict[str, Any] = None,
        tools: List[Any] = None,
        input_schema: Any = None,
        output_schema: Any = None,
    ) -> str:
        # TODO: move to a __post_init__ in Pydantic 2.0
        if isinstance(self.client, Client):
            self.client = AsyncClient(proxies=os.getenv("https_proxy"))
        sess = self.get_session(id)
        if tools:
            assert (input_schema is None) and (
                output_schema is None
            ), "When using tools, input/output schema are ignored"
            for tool in tools:
                assert tool.__doc__, f"Tool {tool} does not have a docstring."
            assert len(tools) <= 9, "You can only have a maximum of 9 tools."
            return await sess.gen_with_tools_async(
                prompt,
                tools,
                client=self.client,
                system=system,
                save_messages=save_messages,
                params=params,
            )
        else:
            return await sess.gen_async(
                prompt,
                client=self.client,
                system=system,
                save_messages=save_messages,
                params=params,
                input_schema=input_schema,
                output_schema=output_schema,
            )

    async def stream(
        self,
        prompt: str,
        id: Union[str, UUID] = None,
        system: str = None,
        save_messages: bool = None,
        params: Dict[str, Any] = None,
        input_schema: Any = None,
    ) -> str:
        # TODO: move to a __post_init__ in Pydantic 2.0
        if isinstance(self.client, Client):
            self.client = AsyncClient(proxies=os.getenv("https_proxy"))
        sess = self.get_session(id)
        return sess.stream_async(
            prompt,
            client=self.client,
            system=system,
            save_messages=save_messages,
            params=params,
            input_schema=input_schema,
        )

    @asynccontextmanager
    async def session(self, **kwargs):
        sess = self.new_session(return_session=True, **kwargs)
        self.sessions[sess.id] = sess
        try:
            yield sess
        finally:
            self.delete_session(sess.id)
```

## File: `simpleaichat/utils.py`
```python
import os
from typing import List, Union

import httpx
from pydantic import Field

WIKIPEDIA_API_URL = "https://en.wikipedia.org/w/api.php"


def wikipedia_search(query: str, n: int = 1) -> Union[str, List[str]]:
    SEARCH_PARAMS = {
        "action": "query",
        "list": "search",
        "format": "json",
        "srlimit": n,
        "srsearch": query,
        "srwhat": "text",
        "srprop": "",
    }

    r_search = httpx.get(WIKIPEDIA_API_URL, params=SEARCH_PARAMS)
    results = [x["title"] for x in r_search.json()["query"]["search"]]

    return results[0] if n == 1 else results


def wikipedia_lookup(query: str, sentences: int = 1) -> str:
    LOOKUP_PARAMS = {
        "action": "query",
        "prop": "extracts",
        "exsentences": sentences,
        "exlimit": "1",
        "explaintext": "1",
        "formatversion": "2",
        "format": "json",
        "titles": query,
    }

    r_lookup = httpx.get(WIKIPEDIA_API_URL, params=LOOKUP_PARAMS)
    return r_lookup.json()["query"]["pages"][0]["extract"]


def wikipedia_search_lookup(query: str, sentences: int = 1) -> str:
    return wikipedia_lookup(wikipedia_search(query, 1), sentences)


async def wikipedia_search_async(query: str, n: int = 1) -> Union[str, List[str]]:
    SEARCH_PARAMS = {
        "action": "query",
        "list": "search",
        "format": "json",
        "srlimit": n,
        "srsearch": query,
        "srwhat": "text",
        "srprop": "",
    }

    async with httpx.AsyncClient(proxies=os.getenv("https_proxy")) as client:
        r_search = await client.get(WIKIPEDIA_API_URL, params=SEARCH_PARAMS)
    results = [x["title"] for x in r_search.json()["query"]["search"]]

    return results[0] if n == 1 else results


async def wikipedia_lookup_async(query: str, sentences: int = 1) -> str:
    LOOKUP_PARAMS = {
        "action": "query",
        "prop": "extracts",
        "exsentences": sentences,
        "exlimit": "1",
        "explaintext": "1",
        "formatversion": "2",
        "format": "json",
        "titles": query,
    }

    async with httpx.AsyncClient(proxies=os.getenv("https_proxy")) as client:
        r_lookup = await client.get(WIKIPEDIA_API_URL, params=LOOKUP_PARAMS)
    return r_lookup.json()["query"]["pages"][0]["extract"]


async def wikipedia_search_lookup_async(query: str, sentences: int = 1) -> str:
    return await wikipedia_lookup_async(
        await wikipedia_search_async(query, 1), sentences
    )


def fd(description: str, **kwargs):
    return Field(description=description, **kwargs)


# https://stackoverflow.com/a/58938747
def remove_a_key(d, remove_key):
    if isinstance(d, dict):
        for key in list(d.keys()):
            if key == remove_key:
                del d[key]
            else:
                remove_a_key(d[key], remove_key)
```

