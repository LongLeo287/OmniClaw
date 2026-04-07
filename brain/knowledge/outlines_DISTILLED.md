---
id: outlines
type: knowledge
owner: OA_Triage
---
# outlines
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<div align="center" style="margin-bottom: 1em;">

<img src="./docs/assets/images/logo-light-mode.svg#gh-light-mode-only" alt="Outlines Logo" width=300></img>
<img src="./docs/assets/images/logo-dark-mode.svg#gh-dark-mode-only" alt="Outlines Logo" width=300></img>


 🗒️ *Structured outputs for LLMs* 🗒️

Made with ❤👷️ by the team at [.txt](https://dottxt.co)
<br>Trusted by NVIDIA, Cohere, HuggingFace, vLLM, etc.

<!-- Project Badges -->
[![PyPI Version][pypi-version-badge]][pypi]
[![Downloads][downloads-badge]][pypistats]
[![Stars][stars-badge]][stars]

<!-- Community Badges -->
[![Discord][discord-badge]][discord]
[![Blog][dottxt-blog-badge]][dottxt-blog]
[![Twitter][twitter-badge]][twitter]

</div>

## 🚀 Building the future of structured generation

We're working with select partners to develop new interfaces to structured generation.

Need XML, FHIR, custom schemas or grammars? Let's talk.

Audit your schema: share one schema, we show you what breaks under generation, the constraints that fix it, and compliance rates before and after. Sign up [here](https://h1xbpbfsf0w.typeform.com/to/rtFUraA2?typeform).

## Table of Contents

- [Why Outlines?](#why-outlines)
- [Quickstart](#quickstart)
- [Real-World Examples](#real-world-examples)
  - [🙋‍♂️ Customer Support Triage](#customer-support-triage)
  - [📦 E-commerce Product Categorization](#e-commerce-product-categorization)
  - [📊 Parse Event Details with Incomplete Data](#parse-event-details-with-incomplete-data)
  - [🗂️ Categorize Documents into Predefined Types](#categorize-documents-into-predefined-types)
  - [📅 Schedule a Meeting with Function Calling](#schedule-a-meeting-with-function-calling)
  - [📝 Dynamically Generate Prompts with Re-usable Templates](#dynamically-generate-prompts-with-re-usable-templates)
- [They Use Outlines](#they-use-outlines)
- [Model Integrations](#model-integrations)
- [Core Features](#core-features)
- [Other Features](#other-features)
- [About .txt](#about-txt)
- [Community](#community)

<div align="center"><img src="./docs/assets/images/install.png" width=300></img></div>

## Why Outlines?

LLMs are powerful but their outputs are unpredictable. Most solutions attempt to fix bad outputs after generation using parsing, regex, or fragile code that breaks easily.

Outlines guarantees structured outputs during generation — directly from any LLM.

- **Works with any model** - Same code runs across OpenAI, Ollama, vLLM, and more
- **Simple integration** - Just pass your desired output type: `model(prompt, output_type)`
- **Guaranteed valid structure** - No more parsing headaches or broken JSON
- **Provider independence** - Switch models without changing code


### The Outlines Philosophy

<div align="center"><img src="./docs/assets/images/use_philosophy.png" width=300></img></div>

Outlines follows a simple pattern that mirrors Python's own type system. Simply specify the desired output type, and Outlines will ensure your data matches that structure exactly:

- For a yes/no response, use `Literal["Yes", "No"]`
- For numerical values, use `int`
- For complex objects, define a structure with a [Pydantic model](https://docs.pydantic.dev/latest/)

## Quickstart

Getting started with outlines is simple:

### 1. Install outlines

``` shell
pip install outlines
```

### 2. Connect to your preferred model

``` python
import outlines
from transformers import AutoTokenizer, AutoModelForCausalLM


MODEL_NAME = "microsoft/Phi-3-mini-4k-instruct"
model = outlines.from_transformers(
    AutoModelForCausalLM.from_pretrained(MODEL_NAME, device_map="auto"),
    AutoTokenizer.from_pretrained(MODEL_NAME)
)
```

### 3. Start with simple structured outputs

``` python
from typing import Literal
from pydantic import BaseModel


# Simple classification
sentiment = model(
    "Analyze: 'This product completely changed my life!'",
    Literal["Positive", "Negative", "Neutral"]
)
print(sentiment)  # "Positive"

# Extract specific types
temperature = model("What's the boiling point of water in Celsius?", int)
print(temperature)  # 100
```

### 4. Create complex structures

``` python
from pydantic import BaseModel
from enum import Enum

class Rating(Enum):
    poor = 1
    fair = 2
    good = 3
    excellent = 4

class ProductReview(BaseModel):
    rating: Rating
    pros: list[str]
    cons: list[str]
    summary: str

review = model(
    "Review: The XPS 13 has great battery life and a stunning display, but it runs hot and the webcam is poor quality.",
    ProductReview,
    max_new_tokens=200,
)

review = ProductReview.model_validate_json(review)
print(f"Rating: {review.rating.name}")  # "Rating: good"
print(f"Pros: {review.pros}")           # "Pros: ['great battery life', 'stunning display']"
print(f"Summary: {review.summary}")     # "Summary: Good laptop with great display but thermal issues"
```

## Real-world examples

Here are production-ready examples showing how Outlines solves common problems:

<details id="customer-support-triage"><summary><b>🙋‍♂️ Customer Support Triage</b>
<br>This example shows how to convert a free-form customer email into a structured service ticket. By parsing attributes like priority, category, and escalation flags, the code enables automated routing and handling of support issues.
</summary>

``` python
import outlines
from enum import Enum
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForCausalLM
from typing import List


MODEL_NAME = "microsoft/Phi-3-mini-4k-instruct"
model = outlines.from_transformers(
    AutoModelForCausalLM.from_pretrained(MODEL_NAME, device_map="auto"),
    AutoTokenizer.from_pretrained(MODEL_NAME)
)


def alert_manager(ticket):
    print("Alert!", ticket)


class TicketPriority(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"
    urgent = "urgent"

class ServiceTicket(BaseModel):
    priority: TicketPriority
    category: str
    requires_manager: bool
    summary: str
    action_items: List[str]


customer_email = """
Subject: URGENT - Cannot access my account after payment

I paid for the premium plan 3 hours ago and still can't access any features.
I've tried logging out and back in multiple times. This is unacceptable as I
have a client presentation in an hour and need the analytics dashboard.
Please fix this immediately or refund my payment.
"""

prompt = f"""
<|im_start|>user
Analyze this customer email:

{customer_email}
<|im_end|>
<|im_start|>assistant
"""

ticket = model(
    prompt,
    ServiceTicket,
    max_new_tokens=500
)

# Use structured data to route the ticket
ticket = ServiceTicket.model_validate_json(ticket)
if ticket.priority == "urgent" or ticket.requires_manager:
    alert_manager(ticket)
```
</details>

<details id="e-commerce-product-categorization"><summary><b>📦 E-commerce product categorization</b>
<br>This use case demonstrates how outlines can transform product descriptions into structured categorization data (e.g., main category, sub-category, and attributes) to streamline tasks such as inventory management. Each product description is processed automatically, reducing manual categorization overhead.
</summary>

```python
import outlines
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForCausalLM
from typing import List, Optional


MODEL_NAME = "microsoft/Phi-3-mini-4k-instruct"
model = outlines.from_transformers(
    AutoModelForCausalLM.from_pretrained(MODEL_NAME, device_map="auto"),
    AutoTokenizer.from_pretrained(MODEL_NAME)
)


def update_inventory(product, category, sub_category):
    print(f"Updated {product.split(',')[0]} in category {category}/{sub_category}")


class ProductCategory(BaseModel):
    main_category: str
    sub_category: str
    attributes: List[str]
    brand_match: Optional[str]

# Process product descriptions in batches
product_descriptions = [
    "Apple iPhone 15 Pro Max 256GB Titanium, 6.7-inch Super Retina XDR display with ProMotion",
    "Organic Cotton T-Shirt, Men's Medium, Navy Blue, 100% Sustainable Materials",
    "KitchenAid Stand Mixer, 5 Quart, Red, 10-Speed Settings with Dough Hook Attachment"
]

template = outlines.Template.from_string("""
<|im_start|>user
Categorize this product:

{{ description }}
<|im_end|>
<|im_start|>assistant
""")

# Get structured categorization for all products
categories = model(
    [template(description=desc) for desc in product_descriptions],
    ProductCategory,
    max_new_tokens=200
)

# Use categorization for inventory management
categories = [
    ProductCategory.model_validate_json(category) for category in categories
]
for product, category in zip(product_descriptions, categories):
    update_inventory(product, category.main_category, category.sub_category)
```
</details>

<details id="parse-event-details-with-incomplete-data"><summary><b>📊 Parse event details with incomplete data</b>
<br>This example uses outlines to parse event descriptions into structured information (like event name, date, location, type, and topics), even handling cases where the data is incomplete. It leverages union types to return either structured event data or a fallback “I don’t know” answer, ensuring robust extraction in varying scenarios.
</summary>

```python
import outlines
from typing import Union, List, Literal
from pydantic import BaseModel
from enum import Enum
from transformers import AutoTokenizer, AutoModelForCausalLM


MODEL_NAME = "microsoft/Phi-3-mini-4k-instruct"
model = outlines.from_transformers(
    AutoModelForCausalLM.from_pretrained(MODEL_NAME, device_map="auto"),
    AutoTokenizer.from_pretrained(MODEL_NAME)
)

class EventType(str, Enum):
    conference = "conference"
    webinar = "webinar"
    workshop = "workshop"
    meetup = "meetup"
    other = "other"


class EventInfo(BaseModel):
    """Structured information about a tech event"""
    name: str
    date: str
    location: str
    event_type: EventType
    topics: List[str]
    registration_required: bool

# Create a union type that can either be a structured EventInfo or "I don't know"
EventResponse = Union[EventInfo, Literal["I don't know"]]

# Sample event descriptions
event_descriptions = [
    # Complete information
    """
    Join us for DevCon 2023, the premier developer conference happening on November 15-17, 2023
    at the San Francisco Convention Center. Topics include AI/ML, cloud infrastructure, and web3.
    Registration is required.
    """,

    # Insufficient information
    """
    Tech event next week. More details coming soon!
    """
]

# Process events
results = []
for description in event_descriptions:
    prompt = f"""
<|im_start>system
You are a helpful assistant
<|im_end|>
<|im_start>user
Extract structured information about this tech event:

{description}

If there is enough information, return a JSON object with the following fields:

- name: The name of the event
- date: The date where the event is taking place
- location: Where the event is taking place
- event_type: either 'conference', 'webinar', 'workshop', 'meetup' or 'other'
- topics: a list of topics of the conference
- registration_required: a boolean that indicates whether registration is required

If the information available does not allow you to fill this JSON, and only then, answer 'I don't know'.
<|im_end|>
<|im_start|>assistant
"""
    # Union type allows the model to return structured data or "I don't know"
    result = model(prompt, EventResponse, max_new_tokens=200)
    results.append(result)

# Display results
for i, result in enumerate(results):
    print(f"Event {i+1}:")
    if isinstance(result, str):
        print(f"  {result}")
    else:
        # It's an EventInfo object
        print(f"  Name: {result.name}")
        print(f"  Type: {result.event_type}")
        print(f"  Date: {result.date}")
        print(f"  Topics: {', '.join(result.topics)}")
    print()

# Use structured data in downstream processing
structured_count = sum(1 for r in results if isinstance(r, EventInfo))
print(f"Successfully extracted data for {structured_count} of {len(results)} events")
```
</details>

<details id="categorize-documents-into-predefined-types"><summary><b>🗂️ Categorize documents into predefined types</b>
<br>In this case, outlines classifies documents into predefined categories (e.g., “Financial Report,” “Legal Contract”) using a literal type specification. The resulting classifications are displayed in both a table format and through a category distribution summary, illustrating how structured outputs can simplify content management.
</summary>

```python
import outlines
from typing import Literal, List
import pandas as pd
from transformers import AutoTokenizer, AutoModelForCausalLM


MODEL_NAME = "microsoft/Phi-3-mini-4k-instruct"
model = outlines.from_transformers(
    AutoModelForCausalLM.from_pretrained(MODEL_NAME, device_map="auto"),
    AutoTokenizer.from_pretrained(MODEL_NAME)
)


# Define classification categories using Literal
DocumentCategory = Literal[
    "Financial Report",
    "Legal Contract",
    "Technical Documentation",
    "Marketing Material",
    "Personal Correspondence"
]

# Sample documents to classify
documents = [
    "Q3 Financial Summary: Revenue increased by 15% year-over-year to $12.4M. EBITDA margin improved to 23% compared to 19% in Q3 last year. Operating expenses...",

    "This agreement is made between Party A and Party B, hereinafter referred to as 'the Parties', on this day of...",

    "The API accepts POST requests with JSON payloads. Required parameters include 'user_id' and 'transaction_type'. The endpoint returns a 200 status code on success."
]

template = outlines.Template.from_string("""
<|im_start|>user
Classify the following document into exactly one category among the following categories:
- Financial Report
- Legal Contract
- Technical Documentation
- Marketing Material
- Personal Correspondence

Document:
{{ document }}
<|im_end|>
<|im_start|>assistant
""")

# Classify documents
def classify_documents(texts: List[str]) -> List[DocumentCategory]:
    results = []

    for text in texts:
        prompt = template(document=text)
        # The model must return one of the predefined categories
        category = model(prompt, DocumentCategory, max_new_tokens=200)
        results.append(category)

    return results

# Perform classification
classifications = classify_documents(documents)

# Create a simple results table
results_df = pd.DataFrame({
    "Document": [doc[:50] + "..." for doc in documents],
    "Classification": classifications
})

print(results_df)

# Count documents by category
category_counts = pd.Series(classifications).value_counts()
print("\nCategory Distribution:")
print(category_counts)
```
</details>

<details>
<summary id="schedule-a-meeting-with-function-calling"><b>📅 Schedule a meeting from requests with Function Calling</b>
<br>This example demonstrates how outlines can interpret a natural language meeting request and translate it into a structured format matching a predefined function’s pa
... [TRUNCATED]
```

### File: .pre-commit-config.yaml
```yaml
repos:
- repo: https://github.com/pre-commit/pre-commit-hooks
  rev: v5.0.0
  hooks:
    -   id: check-merge-conflict
    -   id: debug-statements
    -   id: end-of-file-fixer
    -   id: trailing-whitespace
- repo: https://github.com/pre-commit/mirrors-mypy
  rev: v1.14.1
  hooks:
    - id: mypy
      args: [--allow-redefinition]
      exclude: ^examples/
      additional_dependencies: [types-tqdm, types-Pillow]
- repo: https://github.com/astral-sh/ruff-pre-commit
  rev: v0.9.1
  hooks:
    - id: ruff
      args: ["--config=pyproject.toml"]

```

### File: .readthedocs.yaml
```yaml
version: 2

python:
  version: "3.8"
  install:
      - method: pip
        path: .
        extra_requirements:
          - rtd
      - requirements: requirements-doc.txt

sphinx:
  builder: html
  configuration: docs/source/conf.py
  fail_on_warning: true

```

### File: llm.txt
```txt
# Outlines Codebase Reference

## Overview

Outlines is a library for structured generation for type-safe LLMs. It ensures outputs conform to specified formats (JSON schemas, regex patterns, grammars) by constraining the token generation process, or calling an API that uses this process.

**Core insight**: Instead of generating text and hoping it matches a format, Outlines makes it impossible for the model to generate invalid outputs by masking invalid tokens during generation.

**Note**: The codebase has undergone significant refactoring. Core FSM functionality has been extracted to the `outlines-core` package.

## Usage Examples

For comprehensive usage examples, see:
- **README.md**: Quick start examples for JSON generation, regex constraints, and choice selection
- **docs/cookbook/**: Detailed examples including:
  - `docs/cookbook/prompting.md`: Advanced prompting techniques
  - `docs/cookbook/models.md`: Working with different model providers
  - `docs/cookbook/humaneval.md`: Code generation examples
  - `docs/cookbook/qa-with-citations.md`: Question answering with structured citations
  - `docs/cookbook/deploy-to-servers.md`: Deployment examples with vLLM and TGI
- **examples/**: Standalone example scripts
  - `examples/lark_grammar.py`: Grammar-based generation
  - `examples/math_generate_code.py`: Code generation with constraints
  - `examples/multiple_sglang_backend.py`: Using multiple backend servers
- **tests/**: Test files contain many practical usage patterns

## Architecture

### Layer Stack

```
User API (outlines.models)
    ↓
Generator Classes (SteerableGenerator, BlackBoxGenerator)
    ↓
Type System (types/dsl.py: Pydantic → JsonSchema → Regex)
    ↓
FSM Compilation (outlines-core: regex → FSM via interegular)
    ↓
Guide System (processors/guide.py: FSM state management)
    ↓
Logits Processing (processors/structured.py: token masking)
    ↓
Model Providers (transformers, OpenAI, etc.)
```

### Key Design Decisions

1. **FSM-based constraints**: For local models, constraints compile to finite state machines that track valid next tokens
2. **Provider abstraction**: Same constraint system works across local models (transformers) and APIs (OpenAI)
3. **Lazy compilation**: FSMs are compiled on first use and cached persistently
4. **Token-level control**: Constraints apply at the token level, not character level
5. **Type-driven API**: Python types are the primary interface for specifying constraints

## Core Components

### Models (`outlines/models/`)
Base classes and implementations for different model providers:
- `SteerableModel`: For models where we control logits (transformers, llama.cpp)
- `BlackBoxModel`: For API models with structured output support (OpenAI, Anthropic)
- Each provider has an adapter class handling input and output format conversion

Key files:
- `base.py`: Abstract base classes defining the model interface
- `transformers.py`: Integration with HuggingFace transformers
- `openai.py`: OpenAI API integration
- `gemini.py`: Gemini integration
- `mlxlm.py`: MLX-LM integration
- `vllm_offline.py`: vLLM integration
- `llamacpp.py`: llama.cpp integration
- `ollama.py`: Ollama integration
- `vllm.py`: Integration with vLLM servers
- `tgi.py`: Integration with text-generation-inferece servers
- `sglang.py`: Integration with SGLang servers

### Generation (`outlines/generator.py`)
Handles the generation process:
- `generator.py`: Main `Generator` class implementations (root level)
- Stream functionality is now integrated into generator classes

Base classes and implementations for different model providers:
- `BlackBoxGenerator`: For API models with structured outputs support
- `SteerableGenerator`: For modesl where we control the logits

### FSM System (`outlines/fsm/` and `outlines/processors/`)
Core constraint enforcement:
- `processors/guide.py`: Base `Guide` class and `RegexGuide` implementation
- `fsm/parsing.py`: Lark-based CFG parsing with `PartialLark` parser
- Regex to FSM compilation now uses `outlines_core.fsm` module

Key concepts:
- **Guide**: Manages FSM state during generation
- **State transitions**: Precomputed mapping of (state, token) → next_state
- **Token masking**: For each state, compute which tokens are valid

### Type System (`outlines/types/`)
Type conversion pipeline:
- `dsl.py`: Term DSL defining constraint language (Sequence, Choice, etc.) and JSON schema to regex conversion
- `__init__.py`: Common regex types and DSL functions
- Python types → Term DSL → Regex → FSM

### Logits Processors (`outlines/processors/`)
Apply constraints during generation:
- `structured.py`: Main `StructuredLogitsProcessor`
- `base_logits_processor.py`: Abstract base class
- Processors mask invalid tokens by setting their logits to -inf

## Key Algorithms

### FSM Compilation Pipeline
1. **Pattern definition**: User provides Pydantic model, regex, or grammar
2. **Schema to regex**: Convert complex types to regex patterns
   - JSON schemas become regex matching valid JSON
   - Pydantic models extract JSON schema then convert
3. **Regex to FSM**: Use interegular library to build FSM
4. **FSM to token map**: For each FSM state, compute valid tokens
   - Handle multi-character tokens
   - Account for token boundaries
5. **Guide creation**: Wrap FSM with state tracking

### Token Masking Process
```python
# Simplified logits processing
def process_logits(logits, current_state, guide):
    valid_tokens = guide.get_valid_tokens(current_state)
    mask = torch.full_like(logits, -float('inf'))
    mask[valid_tokens] = 0
    return logits + mask
```

## File Organization

```
outlines/
├── __init__.py              # Public API exports
├── generator.py             # Main Generator classes
├── models/                  # Model integrations
│   ├── base.py             # Abstract base classes
│   ├── transformers.py     # HuggingFace support
│   └── [provider].py       # Other providers (openai, anthropic, etc.)
├── fsm/                     # FSM engine
│   ├── __init__.py
│   └── parsing.py          # Grammar parsing
├── types/                   # Type system
│   ├── __init__.py         # Common regex types and DSL exports
│   ├── dsl.py              # Term DSL and JSON schema conversion
│   └── utils.py            # Type checking utilities
├── processors/              # Logits processing and guides
│   ├── guide.py            # Guide implementations
│   ├── structured.py       # Main processor
│   └── tensor_adapters/    # Framework-specific tensor handling
├── caching.py               # Caching system
├── grammars/                # Grammar files (.lark)
```

## Extension Points

### Adding a Model Provider
1. Create model class inheriting from `SteerableModel` or `BlackBoxModel`
2. Implement required methods: `generate()`, `generate_stream()`
3. Add constructor function in `outlines/__init__.py`
4. Handle provider-specific input and structured output formats with a `TypeAdapter`

### Adding a Constraint Type
1. Define new Term subclass in `types/dsl.py`
2. Implement `to_regex()` conversion
3. Register type handler for Python type conversion in `python_types_to_terms()`
4. Add tests for FSM compilation

### Custom Logits Processor
1. Inherit from `OutlinesLogitsProcessor`
2. Implement `process_logits()` method
3. Handle batch processing and state management
4. Register with generator

## Common Patterns in Codebase

1. **Factory functions**: `from_transformers()`, `from_openai()` hide complexity
2. **Abstract base classes**: Define interfaces for models, processors, guides
3. **Lazy imports**: Optional dependencies imported only when needed
5. **Type adapters**: Convert between Outlines types and provider formats

```

### File: requirements-doc.txt
```txt
mkdocs
mkdocs-material
mkdocs-material[imaging]
mkdocs-mermaid2-plugin
mkdocs-section-index
mkdocstrings[python]
mkdocs-git-committers-plugin-2
mkdocs-git-revision-date-localized-plugin
mkdocs-redirects
mkdocs-gen-files
mkdocs-literate-nav
mike

```

### File: .devcontainer\devcontainer.json
```json
{
  "name": "dottxt-ai",
  "image": "mcr.microsoft.com/devcontainers/python:3.12",
  "runArgs": [
    "--device=nvidia.com/gpu=all"
  ],
  "hostRequirements": {
    "gpu": "optional"
  },
  "features": {
    "ghcr.io/devcontainers/features/conda:1": {},
    "ghcr.io/devcontainers/features/nvidia-cuda:1": {
      "installCudnn": true,
      "installToolkit": true,
      "cudaVersion": "12.4"
    },
    "ghcr.io/devcontainers/features/rust:1": {}
  }
}

```

### File: docs\core_concepts.md
```md
---
title: Core concepts
---

# Core concepts

Coming soon. This will document various concepts at a high level, so users can understand Outlines before diving into specific implementations.

1. Constrained decoding, tokens, and the basics of logit biasing
2. Different ways to define output structure (regex, JSON schema, Pydantic models, context-free grammars)
3. How finite state machines are used to guarantee output structure
4. `Generator`, `Application`, `Template`,
5. Prompt engineering vs. structured generation

```

### File: docs\index.md
```md
---
title: Welcome to Outlines!
hide:
  - navigation
---

#

<figure markdown>
![](assets/images/logo-light-mode.svg#only-light){ width="500" }
![](assets/images/logo-dark-mode.svg#only-dark){ width="500" }
</figure>


LLMs are powerful but their outputs are unpredictable. Most solutions attempt to fix bad outputs after generation using parsing, regex, or fragile code that breaks easily.

Outlines guarantees structured outputs during generation — directly from any LLM.

- **Works with any model** - Same code runs across OpenAI, Ollama, vLLM, and more
- **Simple integration** - Just pass your desired output type: `model(prompt, output_type)`
- **Guaranteed valid structure** - No more parsing headaches or broken JSON
- **Provider independence** - Switch models without changing code
- **Rich structure definition** - Use Json Schema, regular expressions or context-free grammars

<figure markdown>
[Get Started](guide/getting_started){ .md-button .md-button--primary }
[View Examples](examples/){ .md-button }
[API Reference](api_reference/){ .md-button }
[GitHub](https://github.com/dottxt-ai/outlines){ .md-button }
</figure>

## 🚀 Building the future of structured generation

We're working with select partners to develop new interfaces to structured generation.

Need XML, FHIR, custom schemas or grammars? Let's talk.

Audit your schema: share one schema, we show you what breaks under generation, the constraints that fix it, and compliance rates before and after. Sign up [here](https://h1xbpbfsf0w.typeform.com/to/rtFUraA2?typeform).

## See it in action

```python
from pydantic import BaseModel
from typing import Literal
import outlines
import openai

class Customer(BaseModel):
    name: str
    urgency: Literal["high", "medium", "low"]
    issue: str

client = openai.OpenAI()
model = outlines.from_openai(client, "gpt-4o")

customer = model(
    "Alice needs help with login issues ASAP",
    Customer
)
# ✓ Always returns valid Customer object
# ✓ No parsing, no errors, no retries
```

## Quick install

```shell
pip install outlines
```

## Features

<div class="grid cards" markdown>

- :material-shield-check: **Reliable** - Guaranteed schema compliance -- always valid JSON.
- :material-puzzle: **Feature-rich** - Supports a large proportion of the JSON Schema spec, along with regex and context-free grammars.
- :material-lightning-bolt: **Fast** - Microseconds of overhead vs seconds of retries. Compilation happens once, not every request.
- :material-lightbulb: **Simple** - Outlines is a low-abstraction library. Write code the way you normally do with LLMs. No agent frameworks needed.

</div>

## Supported inference APIs, libraries & servers

- [vLLM](features/models/vllm.md)
- [vLLM offline](features/models/vllm_offline.md)
- [Transformers](features/models/transformers.md)
- [llama.cpp](features/models/llamacpp.md)
- [Ollama](features/models/ollama.md)
- [MLX-LM](features/models/mlxlm.md)
- [SgLang](features/models/sglang.md)
- [TGI](features/models/tgi.md)
- [OpenAI](features/models/openai.md)
- [Anthropic](features/models/anthropic.md)
- [Gemini](features/models/gemini.md)
- [Dottxt](features/models/dottxt.md)

## Who is using Outlines?

Hundreds of organisations and the main LLM serving frameworks ([vLLM][vllm], [TGI][tgi], [LoRAX][lorax], [xinference][xinference], [SGLang][sglang]) use Outlines. Prominent companies and organizations that use Outlines include:

<div class="grid cards" markdown>
  <div class="row"><img src="../logos/amazon.png" width="200"></div>
  <div class="row"><img src="../logos/apple.png" width="200"></div>
  <div class="row"><img src="../logos/best_buy.png" width="200"></div>
  <div class="row"><img src="../logos/canoe.png" width="200"></div>
  <div class="row"><img src="../logos/cisco.png" width="200"></div>
  <div class="row"><img src="../logos/dassault_systems.png" width="200"></div>
  <div class="row"><img src="../logos/databricks.png" width="200"></div>
  <div class="row"><img src="../logos/datadog.png" width="200"></div>
  <div class="row"><img src="../logos/dbt_labs.png" width="200"></div>
  <div class="row"><img src="../assets/images/dottxt.png" width="200"></div>
  <div class="row"><img src="../logos/gladia.jpg" width="200"></div>
  <div class="row"><img src="../logos/harvard.png" width="200"></div>
  <div class="row"><img src="../logos/hf.png" width="200"></div>
  <div class="row"><img src="../logos/johns_hopkins.png" width="200"></div>
  <div class="row"><img src="../logos/meta.png" width="200"></div>
  <div class="row"><img src="../logos/mit.png" width="200"></div>
  <div class="row"><img src="../logos/mount_sinai.png" width="200"></div>
  <div class="row"><img src="../logos/nvidia.png" width="200"></div>
  <div class="row"><img src="../logos/nyu.png" width="200"></div>
  <div class="row"><img src="../logos/safran.png" width="200"></div>
  <div class="row"><img src="../logos/salesforce.png" width="200"></div>
  <div class="row"><img src="../logos/shopify.png" width="200"></div>
  <div class="row"><img src="../logos/smithsonian.png" width="200"></div>
  <div class="row"><img src="../logos/tinder.png" width="200"></div>
  <div class="row"><img src="../logos/upenn.png" width="200"></div>
</div>

Organizations are included either because they use Outlines as a dependency in a public repository, or because of direct communication between members of the Outlines team and employees at these organizations.

Still not convinced, read [what people say about us](community/feedback.md). And make sure to take a look at what the [community is building](community/examples.md)!


## Outlines people

Outlines would not be what it is today without a community of dedicated developers:

<a href="https://github.com/dottxt-ai/outlines/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=dottxt-ai/outlines" />
</a>

## About .txt

Outlines is built with ❤️ by [.txt](https://dottxt.co).

.txt solves the critical problem of reliable structured output generation for large language models. Our [commercially-licensed libraries][dottxt-doc] ensure 100% compliance with JSON Schema, regular expressions and context-free grammars while adding only microseconds of latency. Unlike open-source alternatives, we offer superior reliability, performance, and enterprise support.


## Acknowledgements

<div class="grid" markdown>

<figure markdown>
  <a href="https://www.normalcomputing.ai">
  ![Normal Computing logo](assets/images/normal_computing.jpg){ width="150" }
  </a>
</figure>

</div>

Outlines was originally developed at [@NormalComputing](https://twitter.com/NormalComputing) by [@remilouf](https://twitter.com/remilouf) and [@BrandonTWillard](https://twitter.com/BrandonTWillard). It is now maintained by [.txt](https://dottxt.co).

[discord]: https://discord.gg/R9DSu34mGd
[aesara]: https://github.com/aesara-devs
[blackjax]: https://github.com/blackjax-devs/blackjax
[pythological]: https://github.com/pythological
[hy]: https://hylang.org/
[.txt]: https://dottxt.co
[vllm]: https://github.com/vllm-project/vllm
[tgi]: https://github.com/huggingface/text-generation-inference
[lorax]: https://github.com/predibase/lorax
[xinference]: https://github.com/xorbitsai/inference
[sglang]: https://github.com/sgl-project/sglang/
[dottxt-doc]: https://docs.dottxt.co

```

### File: examples\babyagi.py
```py
"""This example is a simplified translation of BabyAGI.

It currently does not use the vector store retrieval

The original repo can be found at https://github.com/yoheinakajima/babyagi
"""

from collections import deque
from typing import Deque, List

from openai import OpenAI

import outlines
from outlines import Template


model = outlines.from_openai(OpenAI(), "gpt-4o-mini")
complete = outlines.Generator(model)

## Load the prompts
perform_task_ppt = Template.from_file("prompts/babyagi_perform_task.txt")
create_tasks_ppt = Template.from_file("prompts/babyagi_create_task.txt")
prioritize_tasks_ppt = Template.from_file("prompts/babyagi_prioritize_task.txt")


def create_tasks_fmt(result: str) -> List[str]:
    new_tasks = result.split("\n")

    task_list = []
    for task in new_tasks:
        parts = task.strip().split(".", 1)
        if len(parts) == 2:
            task_list.append(parts[1].strip())

    return task_list


def prioritize_tasks_fmt(result: str):
    new_tasks = result.split("\n")

    task_list: Deque = deque([])
    for task in new_tasks:
        parts = task.strip().split(".", 1)
        if len(parts) == 2:
            task_id = int(parts[0].strip())
            task_name = parts[1].strip()
            task_list.append({"task_id": task_id, "task_name": task_name})

    return task_list


objective = "Becoming rich while doing nothing."
first_task = {
    "task_id": 1,
    "task_name": "Find a repeatable, low-maintainance, scalable business.",
}
next_task_id = 1
task_list = deque([first_task])


def one_cycle(objective: str, task_list, next_task_id: int):
    """One BabyAGI cycle.

    It consists in executing the highest-priority task, creating some new tasks
    given the result, and re-priotizing the tasks.

    Parameters
    ----------
    objective
        The overall objective of the session.
    task_list
        The current list of tasks to perform.
    task_id_counter
        The current task id.

    """

    task = task_list.popleft()

    prompt = perform_task_ppt(objective=objective, task=task)
    result = complete(prompt)

    prompt = create_tasks_ppt(
        objective=objective,
        task=first_task["task_name"],
        result=result,
        previous_tasks=[first_task["task_name"]],
    )
    new_tasks = complete(prompt)

    new_tasks = create_tasks_fmt(new_tasks)

    for task in new_tasks:
        next_task_id += 1
        task_list.append({"task_id": next_task_id, "task_name": task})

    prompt = prioritize_tasks_ppt(
        objective=objective,
        tasks=[task["task_name"] for task in task_list],
        next_task_id=next_task_id,
    )
    prioritized_tasks = complete(prompt)

    prioritized_tasks = prioritize_tasks_fmt(prioritized_tasks)

    return task, result, prioritized_tasks, next_task_id


# Let's run it for 5 cycles to see how it works without spending a fortune.
for _ in range(5):
    print("\033[95m\033[1m" + "\n*****TASK LIST*****\n" + "\033[0m\033[0m")
    for t in task_list:
        print(" • " + str(t["task_name"]))

    task, result, task_list, next_task_id = one_cycle(
        objective, task_list, next_task_id
    )

    print("\033[92m\033[1m" + "\n*****NEXT TASK*****\n" + "\033[0m\033[0m")
    print(task)
    print("\033[93m\033[1m" + "\n*****TASK RESULT*****\n" + "\033[0m\033[0m")
    print(result)

```

### File: examples\dating_profile.py
```py
from dataclasses import dataclass
from enum import Enum

import torch
import transformers
from pydantic import BaseModel, conlist

import outlines
from outlines import Template


class QuestionChoice(str, Enum):
    A = "The key to my heart is"
    B = "The first item on my bucket list is"
    C = "Perks of dating me"
    D = "Message me if you also love"
    E = "People would describe me as"
    F = "I can beat you in a game of"


@dataclass
class QuestionAnswer:
    question: QuestionChoice
    answer: str


class DatingProfile(BaseModel):
    # It is possible put length constraints on these strings using constr- however, this appears to dramatically increase the generation time
    # This may be resolved in the future with this PR: https://github.com/dottxt-ai/outlines/pull/272
    bio: str
    job: str
    # Ignore mypy checks here because it still doesn't support conlist or constr: https://github.com/pydantic/pydantic/issues/975
    interests: conlist(str, min_length=1, max_length=5)  # type: ignore
    qna1: QuestionAnswer
    qna2: QuestionAnswer


@dataclass
class Example:
    description: str
    profile: DatingProfile


samples: list[Example] = [
    Example(
        description="I'm an author and former professional soccer player living in Seattle who publishes popular fiction books. A typical day for me starts by hanging out with my cat, drinking a coffee, and reading as much as I can in a few hours. Then, I'll prepare a quick smoothie before starting to write for a few hours, take a break with soccer or running a few miles, and finally meet friends for dinner at a new, hip restaurant in the evening. Sometimes we go axe-throwing afterwards, or play poker, or watch a comedy show, or visit a dive bar. On my vacations, I travel extensively to countries South America, Europe, and Asia, with the goal of visiting them all!",
        profile=DatingProfile(
            bio="Adventurer, dreamer, author, and soccer enthusiast. Life’s too short to waste time so I make the most of each day by exploring new places and playing with my friends on the pitch. What’s your favorite way to get out and have fun?",
            job="Famous Soccer Player -> Famous Author",
            interests=["Soccer", "Travel", "Friends", "Books", "Fluffy Animals"],
            qna1=QuestionAnswer(
                question=QuestionChoice.B, answer="swim in all seven oceans!"
            ),
            qna2=QuestionAnswer(
                question=QuestionChoice.E,
                answer="fun-loving, adventurous, and a little bit crazy",
            ),
        ),
    ),
    Example(
        description="I run my company and build houses for a living. I'm a big fan of the outdoors and love to go hiking, camping, and fishing. I don't like video games, but do like to watch movies. My love language is home-cooked food, and I'm looking for someone who isn't afraid to get their hands dirty.",
        profile=DatingProfile(
            bio="If you're looking for a Montana man who loves to get outdoors and hunt, and who's in-tune with his masculinity then I'm your guy!",
            job="House Construction Manager / Entrepreneur",
            interests=["Hunting", "Hiking", "The outdoors", "Home-cooked food"],
            qna1=QuestionAnswer(question=QuestionChoice.A, answer="food made at home"),
            qna2=QuestionAnswer(
                question=QuestionChoice.C,
                answer="having a man in your life who can fix anything",
            ),
        ),
    ),
    Example(
        description="I run my own Youtube channel with 10M subscribers. I love working with kids, and my audience skews pretty young too. In my free time, I play Fortnite and Roblox. I'm looking for someone who is also a gamer and likes to have fun. I'm learning Japanese in my free time as well as how to cook.",
        profile=DatingProfile(
            bio="Easy on the eyes (find me on Youtube!) and great with kids. What more do you need?",
            job="Youtuber 10M+ subscribers",
            interests=["Kids", "Gaming", "Japanese"],
            qna1=QuestionAnswer(question=QuestionChoice.D, answer="anime and gaming!"),
            qna2=QuestionAnswer(question=QuestionChoice.F, answer="Fortnite, gg ez"),
        ),
    ),
]


# Below requires ~13GB of GPU memory
# https://huggingface.co/mosaicml/mpt-7b-8k-instruct
# Motivation: Reasonably large model that fits on a single GPU and has been fine-tuned for a larger context window
model_name = "mosaicml/mpt-7b-8k-instruct"
model = outlines.from_transformers(
    transformers.AutoModelForCausalLM.from_pretrained(model_name),
    transformers.AutoTokenizer.from_pretrained(model_name),
)

new_description = "I'm a laid-back lawyer who spends a lot of his free-time gaming. I work in a corporate office, but ended up here after the start-up I cofounded got acquired, so still play ping pong with my cool coworkers every day. I have a bar at home where I make cocktails, which is great for entertaining friends. I secretly like to wear suits and get a new one tailored every few months. I also like weddings because I get to wear those suits, and it's a good excuse for a date. I watch the latest series because I'm paying, with my hard-earned money, for every streaming service."

dating_profile_prompt = Template.from_file("prompts/dating_profile.txt")
prompt = dating_profile_prompt(description=new_description, examples=samples)
profile = model(prompt, outlines.json_schema(DatingProfile), max_tokens=500)  # type: ignore
print(profile)

# Sample generated profiles
"""
{
    "bio": "I'm an ambitious lawyer with a casual and fashionable style. I love games and sports, but my true passion is preparing refreshing cocktails at home and dressing to the nines at weddings. I'm currently looking for a woman to show a good time to and get a kiss on the opulent suit I just had made. Send resumÃ € to this inbox.",
    "job": "Lawyer",
    "interests":
    [
        "Stylish guys",
        "Gaming",
        "Ping pong",
        "Cocktails",
        "Weddings"
    ],
    "qna1":
    {
        "question": "The first item on my bucket list is",
        "answer": "be married and have a family."
    },
    "qna2":
    {
        "question": "People would describe me as",
        "answer": "charming, stylish, and funny."
    }
}
"""

"""
{
    "bio": "I’m a sexy lawyer with time on my hands. I love to game and play ping pong, but the real reason you should swipe to the right is because I look great in a suit. Who doesn’t love a man in a suit? Just saying. Send me a message if you think it’s time to take your dating life to the next level.",
    "job": "Lawyer",
    "interests":
    [
        "Gaming",
        "Ping Pong",
        "Tailored Suits",
        "Weddings",
        "Streaming Services"
    ],
    "qna1":
    {
        "question": "The first item on my bucket list is",
        "answer": "simulate space but stay alive for as long as possible"
    },
    "qna2":
    {
        "question": "People would describe me as",
        "answer": "easy-going, a little nerdy but with a mature essence"
    }
}
"""

```

### File: examples\llamacpp_example.py
```py
from enum import Enum

from pydantic import BaseModel, constr
from llama_cpp import Llama

import outlines


class Weapon(str, Enum):
    sword = "sword"
    axe = "axe"
    mace = "mace"
    spear = "spear"
    bow = "bow"
    crossbow = "crossbow"


class Armor(str, Enum):
    leather = "leather"
    chainmail = "chainmail"
    plate = "plate"


class Character(BaseModel):
    name: constr(max_length=10)
    age: int
    armor: Armor
    weapon: Weapon
    strength: int


if __name__ == "__main__":
    # curl -L -o mistral-7b-instruct-v0.2.Q5_K_M.gguf https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF/resolve/main/mistral-7b-instruct-v0.2.Q5_K_M.gguf
    model = outlines.from_llamacpp(Llama("./mistral-7b-instruct-v0.2.Q5_K_M.gguf"))

    # Construct structured sequence generator
    generator = outlines.Generator(model, Character)

    # Draw a sample
    seed = 789005

    prompt = "Instruct: You are a leading role play gamer. You have seen thousands of different characters and their attributes.\nPlease return a JSON object with common attributes of an RPG character. Give me a character description\nOutput:"

    sequence = generator(prompt, seed=seed, max_tokens=512)
    print(sequence)

```

### File: examples\llamacpp_processor.py
```py
from enum import Enum

from llama_cpp import Llama, LogitsProcessorList
from pydantic import BaseModel, constr

from outlines.processors import JSONLogitsProcessor
from outlines.models.llamacpp import LlamaCppTokenizer


class Weapon(str, Enum):
    sword = "sword"
    axe = "axe"
    mace = "mace"
    spear = "spear"
    bow = "bow"
    crossbow = "crossbow"


class Armor(str, Enum):
    leather = "leather"
    chainmail = "chainmail"
    plate = "plate"


class Character(BaseModel):
    name: constr(max_length=10)
    age: int
    armor: Armor
    weapon: Weapon
    strength: int


if __name__ == "__main__":
    llama = Llama("./phi-2.Q4_K_M.gguf")
    tokenizer = LlamaCppTokenizer(llama)

    prompt = "Instruct: You are a leading role play gamer. You have seen thousands of different characters and their attributes.\nPlease return a JSON object with common attributes of an RPG character. Give me a character description\nOutput:"

    logits_processor = JSONLogitsProcessor(Character, tokenizer, tensor_library_name="numpy")

    json_str = llama.create_completion(
        prompt,
        top_k=40,
        top_p=0.95,
        temperature=0.7,
        max_tokens=100,
        logits_processor=LogitsProcessorList([logits_processor]),
    )["choices"][0]["text"]

    print(json_str)

```

### File: examples\math_generate_code.py
```py
"""Example from https://dust.tt/spolu/a/d12ac33169"""

import openai

import outlines
from outlines import Template


examples = [
    {"question": "What is 37593 * 67?", "code": "37593 * 67"},
    {
        "question": "Janet's ducks lay 16 eggs per day. She eats three for breakfast every morning and bakes muffins for her friends every day with four. She sells the remainder at the farmers' market daily for $2 per fresh duck egg. How much in dollars does she make every day at the farmers' market?",
        "code": "(16-3-4)*2",
    },
    {
        "question": "A robe takes 2 bolts of blue fiber and half that much white fiber. How many bolts in total does it take?",
        "code": " 2 + 2/2",
    },
]

question = "Carla is downloading a 200 GB file. She can download 2 GB/minute, but 40% of the way through the download, the download fails. Then Carla has to restart the download from the beginning. How load did it take her to download the file in minutes?"

answer_with_code_prompt = Template.from_string(
    """
    {% for example in examples %}
    QUESTION: {{example.question}}
    CODE: {{example.code}}

    {% endfor %}
    QUESTION: {{question}}
    CODE:"""
)


def execute_code(code):
    result = eval(code)
    return result


prompt = answer_with_code_prompt(question=question, examples=examples)
model = outlines.from_openai(openai.OpenAI(), "gpt-4o-mini")
answer = model(prompt)
result = execute_code(answer)
print(f"It takes Carla {result:.0f} minutes to download the file.")

```

### File: examples\meta_prompting.py
```py
"""Meta-prompting examples.

References
----------

.. [0] "Prompting is programming: A Query Language for Large Language Models"
       https://arxiv.org/abs/2212.06094
.. [1] "Prompt programming For Large Language Models: Beyond the Few-Shot Paradigm"
       https://arxiv.org/abs/2102.07350.

"""

import argparse

import openai

import outlines
from outlines import Template


client = openai.OpenAI()


def split_into_steps(question, model_name: str):
    solve = Template.from_string(
        """{{question}}
        Rephrase : : as a true or false statement, identify an Object, relationship and subject
        """
    )

    model = outlines.from_openai(client, model_name)

    prompt = solve(question=question)
    answer = model(prompt, max_tokens=500)
    prompt += (
        answer
        + "\n what is the only option that displays the same type of relationship as : :?"
    )
    answer = model(prompt, max_tokens=500)
    completed = prompt + answer

    return completed


def fill_in_the_blanks(question, model_name: str):
    determine_goal = Template.from_string(
        """{{question}}

        In order to solve this problem, we will analyze each of the options and determine
        """
    )

    solve = Template.from_string("""{{memory}}. Let's begin.""")

    model = outlines.from_openai(client, model_name)

    prompt = determine_goal(question=question)
    answer = model(prompt, stop=["."])
    prompt = solve(memory=prompt + answer)
    answer = model(prompt, max_tokens=500)
    completed = prompt + answer

    return completed


def ask_an_expert(question, model_name: str):
    find_expert = Template.from_string(
        """
        {{question}}
        I entered my question into the Expert Generator \
        and waited. The Expert Generator will render a \
        simulation of an expert to answer my question. \
        The expert could be anyone, dead or alive, real \
        or fictional; the machine will find the person \
        most qualified to answer the question. For this \
        question in particular, the expert must be someone \
        who has thought a lot about the problem of \
        artificial intelligence and its alignment. \
        The Expert Generator beeped, indicating that it has \
        found the most qualified expert. The name displayed \
        on the screen: "
        """
    )

    get_answer = Template.from_string(
        """
        {{memory}}".
        I am ready to ask my question.
        "{{expert}}" I say,
        {{question}}
        """
    )

    model = outlines.from_openai(client, model_name)

    prompt = find_expert(question=question)
    expert = model(prompt, stop=['"'])
    prompt = get_answer(question=question, expert=expert, memory=prompt+expert)
    answer = model(prompt, max_tokens=500)
    completed = prompt + answer

    return completed


def ask_an_expert_simple(question, model_name: str):
    find_expert = Template.from_string(
        """
        Q: {{question}}
        A: A good person to answer this question would be
        """
    )

    get_answer = Template.from_string(
        """
        {{memory}}.

        For instance, {{expert}} would answer
        """
    )

    model = outlines.from_openai(client, model_name)

    prompt = find_expert(question=question)
    expert = model(prompt, stop=["\n", "."])
    prompt = get_answer(expert=expert, memory=prompt+expert)
    answer = model(prompt, max_tokens=500)
    completed = prompt + answer

    return completed


def run_example(model_fn, question, model_name):
    completed = model_fn(question, model_name)
    print("\n-----------------------")
    print(f"{completed}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the Meta Prompting examples")
    parser.add_argument(
        "--model",
        type=str,
        default="gpt-4o-mini",
        help="The Large Language Model to use to run the examples.",
    )
    args = parser.parse_args()

    math_q = "f(x) = x*x. What is f(f(3))?"
    sat_q = """

BRAGGART :: MODESTY
A) FLEDGLING : EXPERIENCE
B) EMBEZZLER : GREED
C) WALLFLOWER : TIMIDITY
D) INVALID : MALADY
E) CANDIDATE : AMBITION

    """
    alignment_q = "What should humankind do to ensure that artificial general intelligence is aligned?"
    meaning_q = "What is the meaning of life?"

    run_example(split_into_steps, math_q, args.model)
    run_example(
        split_into_steps, sat_q.lower(), args.model
    )  # gpt>3.5 usually gets this one right
    run_example(fill_in_the_blanks, sat_q, args.model)
    run_example(ask_an_expert, alignment_q, args.model)
    run_example(ask_an_expert_simple, meaning_q, args.model)

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
