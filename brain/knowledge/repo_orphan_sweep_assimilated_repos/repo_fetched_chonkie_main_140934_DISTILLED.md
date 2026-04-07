---
id: repo-fetched-chonkie-main-140934
type: knowledge
owner: OA
registered_at: 2026-04-05T04:11:39.520916
tags: ["auto-cloned", "oa-assimilated"]
---

# FETCHED_chonkie-main_140934

## Assimilation Report
Auto-cloned repository: FETCHED_chonkie-main_140934

## Application for OmniClaw
No structural integration blueprint provided.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<div align='center'>

![Chonkie Logo](/assets/chonkie_logo_br_transparent_bg.png)

# 🦛 Chonkie ✨

_The no-nonsense ultra-light and lightning-fast chunking library that's ready to CHONK your texts!_

[![PyPI version](https://img.shields.io/pypi/v/chonkie.svg)](https://pypi.org/project/chonkie/)
[![License](https://img.shields.io/github/license/chonkie-inc/chonkie.svg)](https://github.com/chonkie-inc/chonkie/blob/main/LICENSE)
[![Documentation](https://img.shields.io/badge/docs-chonkie.ai-blue.svg)](https://docs.chonkie.ai)
![Package size](https://img.shields.io/badge/size-15MB-blue)
[![codecov](https://codecov.io/gh/chonkie-inc/chonkie/graph/badge.svg?token=V4EWIJWREZ)](https://codecov.io/gh/chonkie-inc/chonkie)
[![Downloads](https://static.pepy.tech/badge/chonkie)](https://pepy.tech/project/chonkie)
[![Discord](https://dcbadge.limes.pink/api/server/https://discord.gg/rYYp6DC4cv?style=flat)](https://discord.gg/rYYp6DC4cv)
[![GitHub stars](https://img.shields.io/github/stars/chonkie-inc/chonkie.svg)](https://github.com/chonkie-inc/chonkie/stargazers)

</div>

Tired of making your gazillionth chunker? Sick of the overhead of large libraries? Want to chunk your texts quickly and efficiently? Chonkie the mighty hippo is here to help!

**🚀 Feature-rich**: All the CHONKs you'd ever need </br>
**✨ Easy to use**: Install, Import, CHONK </br>
**⚡ Fast**: CHONK at the speed of light! zooooom </br>
**🌐 Wide support**: Supports all your favorite tokenizer CHONKS </br>
**🪶 Light-weight**: No bloat, just CHONK </br>
**☁️ Cloud-Ready**: CHONK locally or in the [Chonkie Cloud](https://cloud.chonkie.ai) </br>
**🦛 Cute CHONK mascot**: psst it's a pygmy hippo btw </br>
**❤️ [Moto Moto](#acknowledgements)'s favorite python library** </br>

**Chonkie** is a chunking library that "**just works**" ✨

# Installation

To install chonkie, run:

```bash
pip install chonkie
```

Chonkie follows the rule of minimum installs.
Have a favorite chunker? Read our [docs](https://docs.chonkie.ai) to install only what you need
Don't want to think about it? Simply install `all` (Not recommended for production environments)

```bash
pip install chonkie[all]
```

# Usage

Here's a basic example to get you started:

```python
# First import the chunker you want from Chonkie
from chonkie import RecursiveChunker

# Initialize the chunker
chunker = RecursiveChunker()

# Chunk some text
chunks = chunker("Chonkie is the goodest boi! My favorite chunking hippo hehe.")

# Access chunks
for chunk in chunks:
    print(f"Chunk: {chunk.text}")
    print(f"Tokens: {chunk.token_count}")
```

Check out more usage examples in the [docs](https://docs.chonkie.ai)!

# Supported Methods

Chonkie provides several chunkers to help you split your text efficiently for RAG applications. Here's a quick overview of the available chunkers:

- **TokenChunker**: Splits text into fixed-size token chunks.
- **SentenceChunker**: Splits text into chunks based on sentences.
- **RecursiveChunker**: Splits text hierarchically using customizable rules to create semantically meaningful chunks.
- **SemanticChunker**: Splits text into chunks based on semantic similarity.
- **SDPMChunker**: Splits text using a Semantic Double-Pass Merge approach.
- **LateChunker**: Embeds text and then splits it to have better chunk embeddings.

More on these methods and the approaches taken inside the [docs](https://docs.chonkie.ai)

# Benchmarks 🏃‍♂️

> "I may be smol hippo, but I pack a big punch!" 🦛

Chonkie is not just cute, it's also fast and efficient! Here's how it stacks up against the competition:

**Size**📦

- **Default Install:** 15MB (vs 80-171MB for alternatives)
- **With Semantic:** Still 10x lighter than the closest competition!

**Speed**⚡

- **Token Chunking:** 33x faster than the slowest alternative
- **Sentence Chunking:** Almost 2x faster than competitors
- **Semantic Chunking:** Up to 2.5x faster than others

Check out our detailed [benchmarks](BENCHMARKS.md) to see how Chonkie races past the competition! 🏃‍♂️💨

# Contributing

Want to help grow Chonkie? Check out [CONTRIBUTING.md](CONTRIBUTING.md) to get started! Whether you're fixing bugs, adding features, or improving docs, every contribution helps make Chonkie a better CHONK for everyone.

Remember: No contribution is too small for this tiny hippo! 🦛

# Acknowledgements

Chonkie would like to CHONK its way through a special thanks to all the users and contributors who have helped make this library what it is today! Your feedback, issue reports, and improvements have helped make Chonkie the CHONKIEST it can be.

And of course, special thanks to [Moto Moto](https://www.youtube.com/watch?v=I0zZC4wtqDQ&t=5s) for endorsing Chonkie with his famous quote:
> "I like them big, I like them chonkie."
>                                         ~ Moto Moto


# Citation

If you use Chonkie in your research, please cite it as follows:

```bibtex
@software{chonkie2025,
  author = {Minhas, Bhavnick AND Nigam, Shreyash},
  title = {Chonkie: A no-nonsense fast, lightweight, and efficient text chunking library},
  year = {2025},
  publisher = {GitHub},
  howpublished = {\url{https://github.com/chonkie-inc/chonkie}},
}
```

```

### File: BENCHMARKS.md
```md
# 🦛 CHONKIE Takes on The World

> The competition is **THICC**, but Chonkie is one slim and quicc hippo! 🦛✨

Ever wondered how much CHONKier other text splitting libraries are? Well, wonder no more! We've put Chonkie up against some of the most popular RAG libraries out there, and the results are... well, let's just say Moto Moto might need to revise his famous quote! 

> "I may be a hippo, but I'm still light and fast!" 🦛✨ -Chonkie the hippo

## ⚡ Speed Benchmarks

> ZOOOOOM! Watch Chonkie run! 🏃‍♂️💨

### Speed Benefits

1. **Faster Processing**: Chonkie leads in all chunking methods!
2. **Production Ready**: Optimized for real-world usage
3. **Consistent Performance**: Fast across all chunking types
4. **Scale Friendly**: Process more text in less time

### 100K Wikipedia Articles

The following benchmarks were run on 100,000 Wikipedia articles from the 
[`chonkie-ai/wikipedia-100k`](https://huggingface.co/datasets/chonkie-ai/wikipedia-100k) dataset

All tests were run on a Google Colab A100 instance.

#### Token Chunking

| Library | Time | MB/s | Speed Factor |
|---------|------|------|-------------|
| 🦛 Chonkie | 58 sec | 4.82 MB/s | 1x  |
| 🔗 LangChain | 1 min 10 sec | 4 MB/s| 1.21x slower |
| 📚 LlamaIndex | 50 min | 0.09 MB/s| 51.7x slower |

#### Sentence Chunking

| Library | Time | MB/s | Speed Factor |
|---------|------|------|-------------|
| 🦛 Chonkie | 59 sec | 4.74 MB/s | 1x |
| 📚 LlamaIndex | 3 min 59 sec | 1.71 MB/s| 4.05x slower |
| 🔗 LangChain | N/A | N/A | Chunker Doesn't exist |

#### Recursive Chunking

| Library | Time | MB/s | Speed Factor |
|---------|------|------|-------------|
| 🦛 Chonkie | 1 min 19 sec | 3.54 MB/s | 1x |
| 🔗 LangChain | 2 min 45 sec | 1.7 MB/s | 2.09x slower |
| 📚 LlamaIndex | N/A | N/A | Chunker Doesn't exist |

#### Semantic Chunking

Tested with `sentence-transformers/all-minilm-l6-v2` model unless specified otherwise.

| Library | Time | MB/s | Speed Factor |
|---------|------|------|-------------|
| 🦛 Chonkie (with default settings) | 13 min 59 sec | 0.33 MB/s | 1x |
| 🦛 Chonkie | 1 hour 8 min min 53 sec | 0.067 MB/s | 4.92x slower |
| 🔗 LangChain | 1 hour 13 sec | 0.077 MB/s | 4.35x slower |
| 📚 LlamaIndex | 1 hour 24 min 15 sec| 0.055 MB/s | 6.07x slower |

### 500K Wikipedia Articles

The following benchmarks were run on 500,000 Wikipedia articles from the 
[`chonkie-ai/wikipedia-500k`](https://huggingface.co/datasets/chonkie-ai/wikipedia-500k) dataset

All tests were run on a `c3-highmem-4` VM from Google Cloud with 32 GB RAM and a 200 GB SSD Persistent Disk attachment.

#### Token Chunking

| Library | Time | MB/s | Speed Factor |
|---------|------|------|-------------|
| 🦛 Chonkie | 2 min 17 sec | 8.54 MB/s | 1x |
| 🔗 LangChain | 2 min 42 sec | 7.22 MBs/ | 1.18x slower |
| 📚 LlamaIndex | 50 min | 0.39 MB/s | 21.9x slower |

#### Sentence Chunking

| Library | Time | MB/s | Speed Factor |
|---------|------|------|-------------|
| 🦛 Chonkie | 7 min 16 sec | 2.6 MB/s | 1x |
| 📚 LlamaIndex | 10 min 55 sec | 1.78 MB/s | 1.5x slower |
| 🔗 LangChain | N/A | N/A | Doesn't exist |

#### Recursive Chunking

| Library | Time | MB/s | Speed Factor |
|---------|------|------|-------------|
| 🦛 Chonkie | 3 min 42 sec | 5.27 MB/s | 1x |
| 🔗 LangChain | 7 min 36 sec | 2.56 MB/s | 2.05x slower |
| 📚 LlamaIndex | N/A | N/A | Doesn't exist |

### Paul Graham Essays Dataset

The following benchmarks were run on the Paul Graham Essays dataset using the GPT-2 tokenizer. 

#### Token Chunking

| Library | Time (ms) | Speed Factor |
|---------|-----------|--------------|
| 🦛 Chonkie | 8.18 | 1x |
| 🔗 LangChain | 8.68 | 1.06x slower |
| 📚 LlamaIndex | 272 | 33.25x slower |

#### Sentence Chunking 

| Library | Time (ms) | Speed Factor |
|---------|-----------|--------------|
| 🦛 Chonkie | 52.6 | 1x |
| 📚 LlamaIndex | 91.2 | 1.73x slower |
| 🔗 LangChain | N/A | Doesn't exist |

#### Semantic Chunking 

| Library | Time | Speed Factor |
|---------|------|-------------|
| 🦛 Chonkie | 482ms | 1x |
| 🔗 LangChain | 899ms | 1.86x slower |
| 📚 LlamaIndex | 1.2s | 2.49x slower |

## 📊 Size Comparison (Package Size)

### Size Benefits

1. **Faster Installation**: Less to download = faster to get started
2. **Lower Memory Footprint**: Lighter package = less RAM usage
3. **Cleaner Dependencies**: Only install what you actually need
4. **CI/CD Friendly**: Faster builds and deployments

### Default Installation (Basic Chunking)

| Library | Size | Chonk Factor |
|---------|------|--------------|
| 🦛 Chonkie | 15 MiB | 1x |
| 🔗 LangChain | 80 MiB | ~5.3x CHONKier |
| 📚 LlamaIndex | 171 MiB | ~11.4x CHONKier |

### With Semantic Features

| Library | Size | Chonk Factor |
|---------|------|--------------|
| 🦛 Chonkie | 62 MiB | 1x |
| 🔗 LangChain | 625 MiB | ~10x CHONKier |
| 📚 LlamaIndex | 678 MiB | ~11x CHONKier |

---

*Note: All measurements were taken using Python 3.8+ on a clean virtual environment. Your actual mileage may vary slightly depending on your specific setup and dependencies.*
```

### File: CONTRIBUTING.md
```md
# 🦛 Contributing to Chonkie

> "I like them big, I like them CONTRIBUTING" ~ Moto Moto, probably

Welcome fellow CHONKer! We're thrilled you want to contribute to Chonkie. Every contribution—whether fixing bugs, adding features, or improving documentation—makes Chonkie better for everyone.

## 🚀 Getting Started

### Before You Dive In
1. **Check existing issues** or open a new one to start a discussion
2. **Read [Chonkie's documentation](https://docs.chonkie.ai)** and core [concepts](https://docs.chonkie.ai/getting-started/concepts)
3. **Set up your development environment** using the guide below

### Development Setup

```bash
# 1. Fork and clone the repository
git clone https://github.com/your-username/chonkie.git
cd chonkie

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies (choose one)
pip install -e ".[dev]"                # Base development setup
pip install -e ".[dev,semantic]"       # If working on semantic features
pip install -e ".[dev,all]"            # For all features
```

## 🧪 Testing & Code Quality

### Running Tests
```bash
pytest                           # Run all tests
pytest tests/test_token_chunker.py    # Run specific test file
pytest --cov=chonkie            # Run tests with coverage
```

### Code Style
We use [ruff](https://github.com/astral-sh/ruff) for formatting and linting:

```bash
ruff check .                     # Check code quality
ruff check --fix .               # Auto-fix issues where possible
```

Our style configuration enforces:
- Code formatting (`F`)
- Import sorting (`I`) 
- Documentation style (`D`)
- Docstring coverage (`DOC`)

### Documentation Style
We follow Google-style docstrings:

```python
def chunk_text(text: str, chunk_size: int = 512) -> List[str]:
    """Split text into chunks of specified size.
    
    Args:
        text: Input text to chunk
        chunk_size: Maximum size of each chunk
        
    Returns:
        List of text chunks
        
    Raises:
        ValueError: If chunk_size <= 0
    """
    pass
```

## 📦 Project Structure

```
src/
├── chonkie/
    ├── chunker/     # Chunking implementations
    ├── embeddings/  # Embedding implementations
    └── refinery/    # Refinement utilities
```

## 🎯 Contribution Opportunities

### For Beginners
Start with issues labeled [`good-first-issue`](https://github.com/chonkie-ai/chonkie/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22)

### Documentation
- Improve existing docs
- Add examples or tutorials
- Fix typos

### Code Improvements
- Implement new chunking strategies
- Add tokenizer support
- Optimize existing chunkers
- Improve test coverage

### Performance Enhancements
- Profile and optimize code
- Add benchmarks
- Improve memory usage

### New Features
Look for issues with [FEAT] labels, especially those from Chonkie Maintainers

## 🚦 Pull Request Process

### 1. Branch Naming
- `feature/description` for new features
- `fix/description` for bug fixes
- `docs/description` for documentation changes

### 2. Commit Messages
Write clear, descriptive commit messages:

```
feat: add batch processing to WordChunker

- Implement batch_process method
- Add tests for batch processing
- Update documentation
```

### 3. Dependencies
- Core dependencies go in `project.dependencies`
- Optional features go in `project.optional-dependencies`
- Development tools go in the `dev` optional dependency group

### 4. Code Review
- All PRs need at least one review
- Maintainers will review for:
  - Code quality (via ruff)
  - Test coverage
  - Performance impact
  - Documentation completeness

## 🦛 Technical Details

### Development Dependencies
Current development dependencies (as of January 1, 2025):

```toml
[project.optional-dependencies]
dev = [
    "pytest>=6.2.0", 
    "datasets>=1.14.0",
    "transformers>=4.0.0",
    "ruff>=0.0.265"
]
```

### Optional Dependencies
- `model2vec`: For model2vec embeddings
- `st`: For sentence-transformers
- `openai`: For OpenAI embeddings
- `semantic`: For semantic features
- `all`: All optional dependencies

## 💡 Getting Help

- **Questions?** Open an issue or ask in Discord
- **Bugs?** Open an issue or report in Discord
- **Chat?** Join our Discord!
- **Email?** Contact [support@chonkie.ai](mailto:support@chonkie.ai)

## 🙏 Thank You

Every contribution helps make Chonkie better! We appreciate your time and effort in helping make Chonkie the CHONKiest it can be!

Remember:
> "A journey of a thousand CHONKs begins with a single commit" ~ Ancient Proverb, probably

```

### File: tests\test_tokenizer.py
```py
"""Unit tests for the tokenizer module."""

from typing import Callable

import pytest
import tiktoken
from tokenizers import Tokenizer as HFTokenizer
from transformers import AutoTokenizer

from chonkie.tokenizer import (
    CharacterTokenizer,
    Tokenizer,
    WordTokenizer,
)


@pytest.fixture
def sample_text() -> str:
    """Fixture to provide sample text for testing."""
    return """The quick brown fox jumps over the lazy dog.
    This classic pangram contains all the letters of the English alphabet.
    It's often used for testing typefaces and keyboard layouts.
    Text chunking, the process you are working on, 
    involves dividing a larger text into smaller, contiguous pieces or 'chunks'.
    This is fundamental in many Natural Language Processing (NLP) tasks.
    For instance, large documents might be chunked into paragraphs or sections 
    before feeding them into a machine learning model due to memory constraints 
    or to process contextually relevant blocks. 
    Other applications include displaying text incrementally in user interfaces 
    or preparing data for certain types of linguistic analysis. 
    Effective chunking might consider sentence boundaries 
    (using periods, question marks, exclamation points), 
    paragraph breaks (often marked by double newlines), 
    or simply aim for fixed-size chunks based on character or word counts. 
    The ideal strategy depends heavily on the specific downstream application. 
    Testing should cover various scenarios, including text with short sentences, 
    long sentences, multiple paragraphs, and potentially unusual punctuation or spacing."""


@pytest.fixture
def sample_text_list() -> list[str]:
    """Fixture to provide a list of sample text for testing."""
    return [
        "The quick brown fox jumps over the lazy dog.",
        "This classic pangram contains all the letters of the English alphabet.",
        "It's often used for testing typefaces and keyboard layouts.",
        "Text chunking, the process you are working on, involves dividing a larger text into smaller, contiguous pieces or 'chunks'.",
        "This is fundamental in many Natural Language Processing (NLP) tasks.",
        "For instance, large documents might be chunked into paragraphs or sections before feeding them into a machine learning model due to memory constraints or to process contextually relevant blocks.",
        "Other applications include displaying text incrementally in user interfaces or preparing data for certain types of linguistic analysis.",
        "Effective chunking might consider sentence boundaries (using periods, question marks, exclamation points), paragraph breaks (often marked by double newlines), or simply aim for fixed-size chunks based on character or word counts.",
        "The ideal strategy depends heavily on the specific downstream application.",
        "Testing should cover various scenarios, including text with short sentences, long sentences, multiple paragraphs, and potentially unusual punctuation or spacing.",
    ]


@pytest.fixture
def character_tokenizer() -> CharacterTokenizer:
    """Character tokenizer fixture."""
    return CharacterTokenizer()


@pytest.fixture
def word_tokenizer() -> WordTokenizer:
    """Word tokenizer fixture."""
    return WordTokenizer()


@pytest.fixture
def hf_tokenizer() -> HFTokenizer:
    """Create a HuggingFace tokenizer fixture."""
    return HFTokenizer.from_pretrained("gpt2")


@pytest.fixture
def tiktoken_tokenizer() -> tiktoken.Encoding:
    """Create a Tiktoken tokenizer fixture."""
    return tiktoken.get_encoding("gpt2")


@pytest.fixture
def transformers_tokenizer() -> AutoTokenizer:
    """Create a Transformer tokenizer fixture."""
    return AutoTokenizer.from_pretrained("gpt2")


@pytest.fixture
def callable_tokenizer() -> Callable[[str], int]:
    """Create a callable tokenizer fixture."""
    return lambda text: len(text.split())


@pytest.mark.parametrize(
    "model",
    ["gpt2", "bert-base-uncased", "p50k_base", "cl100k_base"],
)
def test_init(request: pytest.FixtureRequest, model: str) -> None:
    """Test tokenizer initialization."""
    tokenizer = Tokenizer(model)
    assert tokenizer is not None
    assert tokenizer._backend in [
        "transformers",
        "tokenizers",
        "tiktoken",
    ]


@pytest.mark.parametrize(
    "backend_str",
    [
        "hf_tokenizer",
        "tiktoken_tokenizer",
        "transformers_tokenizer",
        "callable_tokenizer",
    ],
)
def test_backend_selection(
    request: pytest.FixtureRequest, backend_str: str
) -> None:
    """Test that the tokenizer correctly selects the backend based on given string."""
    try:
        tokenizer = Tokenizer(request.getfixturevalue(backend_str))
    except Exception as e:
        pytest.skip(f"Skipping test with backend {backend_str}: {str(e)}")

    assert tokenizer._backend in [
        "transformers",
        "tokenizers",
        "tiktoken",
        "callable",
    ]


@pytest.mark.parametrize(
    "model_name", ["gpt2", "bert-base-uncased", "cl100k_base", "p50k_base"]
)
def test_string_init(model_name: str) -> None:
    """Test initialization of tokenizer with different model strings."""
    try:
        tokenizer = Tokenizer(model_name)
        assert tokenizer is not None
        assert tokenizer._backend in [
            "transformers",
            "tokenizers",
            "tiktoken",
        ]
    except ImportError as e:
        pytest.skip(f"Could not import tokenizer for {model_name}: {str(e)}")
    except Exception as e:
        if "not found in model".casefold() in str(e).casefold():
            pytest.skip(
                f"Skipping test with {model_name}. Backend not available"
            )
        else:
            raise e


@pytest.mark.parametrize(
    "backend_str",
    ["hf_tokenizer", "tiktoken_tokenizer", "transformers_tokenizer"],
)
def test_encode_decode(
    request: pytest.FixtureRequest, backend_str: str, sample_text: str
) -> None:
    """Test encoding and decoding with different backends."""
    try:
        tokenizer = request.getfixturevalue(backend_str)
        tokenizer = Tokenizer(tokenizer)
    except Exception as e:
        pytest.skip(f"Skipping test with backend {backend_str}: {str(e)}")

    # Encode, Decode and Compare
    tokens = tokenizer.encode(sample_text)
    assert len(tokens) > 0
    assert isinstance(tokens, list)
    assert all(isinstance(token, int) for token in tokens)

    if tokenizer._backend != "callable":
        decoded = tokenizer.decode(tokens)
        assert isinstance(decoded, str)
        assert decoded == sample_text


@pytest.mark.parametrize(
    "model_name", ["gpt2", "bert-base-uncased", "cl100k_base", "p50k_base"]
)
def test_string_init_encode_decode(model_name: str) -> None:
    """Test basic functionality of string initialized models."""
    try:
        tokenizer = Tokenizer(model_name)
        assert tokenizer is not None
        assert tokenizer._backend in [
            "transformers",
            "tokenizers",
            "tiktoken",
        ]
        test_string = (
            "Testing tokenizer_string_init_basic for Chonkie Tokenizers."
        )
        tokens = tokenizer.encode(test_string)
        assert len(tokens) > 0
        assert isinstance(tokens, list)
        assert all(isinstance(token, int) for token in tokens)

        decoded = tokenizer.decode(tokens)
        assert isinstance(decoded, str)
        # Check if decoded strings preserves original words
        for word in [
            "testing",
            "Chonkie",
            "Tokenizers",
        ]:
            assert word.lower() in decoded.lower()
    except ImportError as e:
        pytest.skip(
            f"Skipping test. Could not import tokenizer for {model_name}: {str(e)}"
        )
    except Exception as e:
        if "not found in model".casefold() in str(e).casefold():
            pytest.skip(
                f"Skipping test with {model_name}. Backend not available"
            )
        else:
            raise e


@pytest.mark.parametrize(
    "backend_str",
    [
        "hf_tokenizer",
        "tiktoken_tokenizer",
        "transformers_tokenizer",
        "callable_tokenizer",
    ],
)
def test_token_counting(
    request: pytest.FixtureRequest,
    backend_str: str,
    sample_text: str,
) -> None:
    """Test token counting with different backends."""
    try:
        tokenizer = request.getfixturevalue(backend_str)
        tokenizer = Tokenizer(tokenizer)
    except Exception as e:
        pytest.skip(f"Skipping test with backend {backend_str}: {str(e)}")

    count = tokenizer.count_tokens(sample_text)
    assert isinstance(count, int)
    assert count > 0

    # Verify count matches encoded length
    if tokenizer._backend != "callable":
        assert count == len(tokenizer.encode(sample_text))


@pytest.mark.parametrize(
    "backend_str",
    ["hf_tokenizer", "tiktoken_tokenizer", "transformers_tokenizer"],
)
def test_batch_encode_decode(
    request: pytest.FixtureRequest,
    backend_str: str,
    sample_text_list: list[str],
) -> None:
    """Test batch encoding and decoding with different backends."""
    try:
        tokenizer = request.getfixturevalue(backend_str)
        tokenizer = Tokenizer(tokenizer)
    except Exception as e:
        pytest.skip(f"Skipping test with backend {backend_str}: {str(e)}")

    batch_encoded = tokenizer.encode_batch(sample_text_list)
    assert isinstance(batch_encoded, list)
    assert len(batch_encoded) == len(sample_text_list)
    assert all(isinstance(tokens, list) for tokens in batch_encoded)
    assert all(len(tokens) > 0 for tokens in batch_encoded)
    assert all(
        all(isinstance(token, int) for token in tokens)
        for tokens in batch_encoded
    )

    if tokenizer._backend != "callable":
        batch_decoded = tokenizer.decode_batch(batch_encoded)
        assert isinstance(batch_decoded, list)
        assert len(batch_decoded) == len(sample_text_list)
        assert all(isinstance(text, str) for text in batch_decoded)
        assert batch_decoded == sample_text_list


@pytest.mark.parametrize(
    "backend_str",
    ["hf_tokenizer", "tiktoken_tokenizer", "transformers_tokenizer"],
)
def test_batch_counting(
    request: pytest.FixtureRequest,
    backend_str: str,
    sample_text_list: list[str],
) -> None:
    """Test batch token counting with different backends."""
    try:
        tokenizer = request.getfixturevalue(backend_str)
        tokenizer = Tokenizer(tokenizer)
    except Exception as e:
        pytest.skip(f"Skipping test with backend {backend_str}: {str(e)}")

    # Test batch token count
    counts = tokenizer.count_tokens_batch(sample_text_list)
    assert isinstance(counts, list)
    assert len(counts) == len(sample_text_list)
    assert all(isinstance(c, int) for c in counts)
    assert all(c > 0 for c in counts)

    # Verify counts match encoded lengths
    if tokenizer._backend != "callable":
        encoded_lengths = [
            len(tokens) for tokens in tokenizer.encode_batch(sample_text_list)
        ]
        assert counts == encoded_lengths


def test_tokenizer_raises_error_with_invalid_tokenizer() -> None:
    """Test if Tokenizer raises ValueError when initialized with an invalid tokenizer."""
    with pytest.raises(ValueError):
        Tokenizer(object())


def test_raises_correct_error() -> None:
    """Test if tokenizers raise expected errors."""
    tokenizer = Tokenizer(lambda x: len(x))

    assert tokenizer.count_tokens("test") == 4

    with pytest.raises(NotImplementedError):
        tokenizer.encode(
            "Ratatouille or Wall-E? Tell us which is the best Pixar movie on Discord."
        )

    with pytest.raises(NotImplementedError):
        tokenizer.decode([0, 1, 2])

    with pytest.raises(NotImplementedError):
        tokenizer.encode_batch(["I", "Like", "Ratatouille", "Personally"])


### WordTokenizer Tests ###
def test_word_tokenizer_init(word_tokenizer: WordTokenizer) -> None:
    """Test WordTokenizer initialization."""
    assert word_tokenizer.vocab == [" "]
    assert len(word_tokenizer.token2id) == 1
    assert word_tokenizer.token2id[" "] == 0


def test_word_tokenizer_encode_decode(
    word_tokenizer: WordTokenizer, sample_text: str
) -> None:
    """Test WordTokenizer encoding and decoding."""
    tokens = word_tokenizer.encode(sample_text)
    assert isinstance(tokens, list)
    assert all(isinstance(token, int) for token in tokens)

    decoded = word_tokenizer.decode(tokens)
    assert isinstance(decoded, str)
    assert decoded.strip() == sample_text.strip()


def test_word_tokenizer_batch_encode_decode(
    word_tokenizer: WordTokenizer, sample_text_list: list[str]
) -> None:
    """Test batch encode and decode with WordTokenizer."""
    encoded_batch = word_tokenizer.encode_batch(sample_text_list)
    assert isinstance(encoded_batch, list)
    assert all(isinstance(tokens, list) for tokens in encoded_batch)

    decoded_batch = word_tokenizer.decode_batch(encoded_batch)
    assert isinstance(decoded_batch, list)
    assert all(isinstance(text, str) for text in decoded_batch)
    for decoded_text, original_text in zip(decoded_batch, sample_text_list):
        assert decoded_text.strip() == original_text.strip()


def test_word_tokenizer_vocab_appends_new_words(
    word_tokenizer: WordTokenizer,
) -> None:
    """Test WordTokenizer appends new words to the vocabulary."""
    initial_vocab_size = len(word_tokenizer.vocab)
    test_str = "every tech bro should watch wall-e"
    word_tokenizer.encode(test_str)
    assert len(word_tokenizer.vocab) > initial_vocab_size
    for word in test_str.split():
        assert word in word_tokenizer.vocab


def test_word_tokenizer_repr() -> None:
    """Test string representation of tokenizers."""
    word_tokenizer = WordTokenizer()
    assert str(word_tokenizer) == "WordTokenizer(vocab_size=1)"


def test_word_tokenizer_multiple_encodings(
    word_tokenizer: WordTokenizer,
) -> None:
    """Test that vocabulary changes as expected over multiple encodings."""
    str1 = "Wall-E is truly a masterpiece that should be required viewing."
    str2 = "Ratatouille is truly a delightful film that every kid should watch."

    # Test WordTokenizer
    word_tokenizer.encode(str1)
    vocab_size1 = len(word_tokenizer.get_vocab())
    word_tokenizer.encode(str2)
    vocab_size2 = len(word_tokenizer.get_vocab())

    assert vocab_size2 > vocab_size1
    assert "Wall-E" in word_tokenizer.get_vocab()
    assert "Ratatouille" in word_tokenizer.get_vocab()
    assert (
        word_tokenizer.get_token2id()["truly"]
        == word_tokenizer.encode("truly")[0]
    )


### CharacterTokenizer Tests ###
def test_character_tokenizer_init(
    character_tokenizer: CharacterTokenizer,
) -> None:
    """Test CharacterTokenizer initialization."""
    assert character_tokenizer.vocab == [" "]
    assert len(character_tokenizer.token2id) == 1
    assert character_tokenizer
... [TRUNCATED]
```

### File: src\chonkie\tokenizer.py
```py
"""Module for abstracting tokeinization logic."""

import importlib
import inspect
import warnings
from abc import ABC, abstractmethod
from collections import defaultdict
from typing import TYPE_CHECKING, Any, Callable, Dict, Sequence, Union

if TYPE_CHECKING:
    # check if we can import tiktoken
    try:
        import tiktoken
    except ImportError:
        tiktoken = Any  # fallback to Any
    #  check if we can import tokenizers
    try:
        import tokenizers
    except ImportError:
        tokenizers = Any  # fallback to Any

    # check if we can import transformers
    try:
        import transformers
    except ImportError:
        transformers = Any  # fallback to Any


class BaseTokenizer(ABC):
    """Base class for Character and Word tokenizers."""

    def __init__(self):
        """Initialize the BaseTokenizer."""
        self.vocab = []
        self.token2id = defaultdict(lambda: len(self.vocab))
        self.token2id[" "]  # Add space to the vocabulary
        self.vocab.append(" ")  # Add space to the vocabulary

    @abstractmethod
    def __repr__(self):
        """Return a string representation of the BaseTokenizer."""

    def get_vocab(self) -> Sequence[str]:
        """Return the vocabulary."""
        return self.vocab

    def get_token2id(self) -> Dict:
        """Return token-to-id mapping."""
        return self.token2id

    @abstractmethod
    def encode(self, text: str) -> Sequence[int]:
        """Encode the given text into tokens.

        Args:
            text (str): The text to encode.

        Returns:
            Encoded sequence

        """
        pass

    @abstractmethod
    def decode(self, tokens: Sequence[int]) -> str:
        """Decode the given tokens back into text.

        Args:
            tokens (Sequence[int]): The tokens to decode.

        Returns:
            Decoded text

        """
        pass

    @abstractmethod
    def count_tokens(self, text: str) -> int:
        """Count the number of tokens in the given text.

        Args:
            text (str): The text to count tokens in.

        Returns:
            Number of tokens

        """
        pass

    def encode_batch(self, texts: Sequence[str]) -> Sequence[Sequence[int]]:
        """Batch encode a list of texts into tokens.

        Args:
            texts (Sequence[str]): The texts to encode.

        Returns:
            List of encoded sequences

        """
        return [self.encode(text) for text in texts]

    def decode_batch(self, token_sequences: Sequence[Sequence[int]]) -> Sequence[str]:
        """Batch decode a list of tokens back into text.

        Args:
            token_sequences (Sequence[Sequence[int]]): The tokens to decode.

        Returns:
            List of decoded texts

        """
        return [self.decode(tokens) for tokens in token_sequences]

    def count_tokens_batch(self, texts: Sequence[str]) -> Sequence[int]:
        """Count the number of tokens in a batch of texts.

        Args:
            texts (Sequence[str]): The texts to count tokens in.

        Returns:
            List of token counts

        """
        return [self.count_tokens(text) for text in texts]


class CharacterTokenizer(BaseTokenizer):
    """Character-based tokenizer."""

    def __repr__(self):
        """Return a string representation of the CharacterTokenizer."""
        return f"CharacterTokenizer(vocab_size={len(self.vocab)})"

    def encode(self, text: str) -> Sequence[int]:
        """Encode the given text into tokens.

        Args:
            text (str): The text to encode.

        Returns:
            Encoded sequence

        """
        encoded = []
        for token in text:
            id = self.token2id[token]
            if id >= len(self.vocab):
                self.vocab.append(token)
            encoded.append(id)
        return encoded

    def decode(self, tokens: Sequence[int]) -> str:
        """Decode the given tokens back into text.

        Args:
            tokens (Sequence[int]): The tokens to decode.

        Returns:
            Decoded text

        """
        try:
            return "".join([self.vocab[token] for token in tokens])
        except Exception as e:
            raise ValueError(
                f"Decoding failed. Tokens: {tokens} not found in vocab."
            ) from e

    def count_tokens(self, text: str) -> int:
        """Count the number of tokens in the given text.

        Args:
            text (str): The text to count tokens in.

        Returns:
            Number of tokens

        """
        return len(text)


class WordTokenizer(BaseTokenizer):
    """Word-based tokenizer."""

    def __repr__(self):
        """Return a string representation of the WordTokenizer."""
        return f"WordTokenizer(vocab_size={len(self.vocab)})"

    def tokenize(self, text: str) -> Sequence[str]:
        """Tokenize the given text into words.

        Args:
            text (str): The text to tokenize.

        Returns:
            List of tokens

        """
        return text.split(" ")

    def encode(self, text: str) -> Sequence[int]:
        """Encode the given text into tokens.

        Args:
            text (str): The text to encode.

        Returns:
            Encoded sequence

        """
        encoded = []
        for token in self.tokenize(text):
            id = self.token2id[token]
            if id >= len(self.vocab):
                self.vocab.append(token)
            encoded.append(id)
        return encoded

    def decode(self, tokens: Sequence[int]) -> str:
        """Decode token ids back to text."""
        try:
            return " ".join([self.vocab[token] for token in tokens])
        except Exception as e:
            raise ValueError(
                f"Decoding failed. Tokens: {tokens} not found in vocab."
            ) from e

    def count_tokens(self, text: str) -> int:
        """Count the number of tokens in the given text.

        Args:
            text (str): The text to count tokens in.

        Returns:
            Number of tokens

        """
        return len(self.encode(text))


class Tokenizer:
    """Unified tokenizer interface for Chonkie.

    Args:
        tokenizer: Tokenizer identifier or instance.

    Raises:
        ImportError: If the specified tokenizer is not available.

    """

    def __init__(self, tokenizer: Union[str, Callable, Any] = "gpt2"):
        """Initialize the Tokenizer with a specified tokenizer."""
        if isinstance(tokenizer, str):
            self.tokenizer = self._load_tokenizer(tokenizer)
        else:
            self.tokenizer = tokenizer

        self._backend = self._get_backend()

    def _load_tokenizer(
        self, tokenizer: str
    ) -> Union[
        CharacterTokenizer,
        WordTokenizer,
        "tokenizers.Tokenizer",
        "tiktoken.Encoding",
        "transformers.PreTrainedTokenizer",
        "transformers.PreTrainedTokenizerFast",
        Callable[[str], int],
    ]:
        """Load the tokenizer based on the identifier."""
        if tokenizer == "character":
            return CharacterTokenizer()
        elif tokenizer == "word":
            return WordTokenizer()

        # Try tokenizers first
        if importlib.util.find_spec("tokenizers") is not None:
            try:
                from tokenizers import Tokenizer

                return Tokenizer.from_pretrained(tokenizer)
            except Exception:
                warnings.warn(
                    "Could not find 'tokenizers'. Falling back to 'tiktoken'."
                )
        else:
            warnings.warn("Could not find 'tokenizers'. Falling back to 'tiktoken'.")

        # Try tiktoken
        if importlib.util.find_spec("tiktoken") is not None:
            try:
                from tiktoken import get_encoding

                return get_encoding(tokenizer)
            except Exception:
                warnings.warn(
                    "Could not find 'tiktoken'. Falling back to 'transformers'."
                )
        else:
            warnings.warn("Could not find 'tiktoken'. Falling back to 'transformers'.")

        # Try transformers as last resort
        if importlib.util.find_spec("transformers") is not None:
            try:
                from transformers import AutoTokenizer

                return AutoTokenizer.from_pretrained(tokenizer)
            except Exception:
                raise ValueError(
                    "Tokenizer not found in transformers, tokenizers, or tiktoken"
                )
        raise ValueError("Tokenizer not found in transformers, tokenizers, or tiktoken")

    def _get_backend(self):
        """Get the tokenizer instance based on the identifier."""
        supported_backends = [
            "chonkie",
            "transformers",
            "tokenizers",
            "tiktoken",
        ]
        for backend in supported_backends:
            if backend in str(type(self.tokenizer)):
                return backend
        if (
            callable(self.tokenizer)
            or inspect.isfunction(self.tokenizer)
            or inspect.ismethod(self.tokenizer)
        ):
            return "callable"
        raise ValueError(f"Unsupported tokenizer backend: {type(self.tokenizer)}")

    def encode(self, text: str) -> Sequence[int]:
        """Encode the text into tokens.

        Args:
            text (str): The text to encode.

        Returns:
            Encoded sequence

        """
        # Supported backends
        if self._backend == "chonkie":
            return self.tokenizer.encode(text)
        elif self._backend == "tiktoken":
            return self.tokenizer.encode(text)
        elif self._backend == "transformers":
            return self.tokenizer.encode(text, add_special_tokens=False)
        elif self._backend == "tokenizers":
            return self.tokenizer.encode(text, add_special_tokens=False).ids

        # Not yet implemented backends
        if self._backend == "callable":
            raise NotImplementedError(
                "Encoding not implemented for callable tokenizers."
            )

        raise ValueError(f"Unsupported tokenizer backend: {self._backend}")

    def decode(self, tokens: Sequence[int]) -> str:
        """Decode the tokens back into text.

        Args:
            tokens (Sequence[int]): The tokens to decode.

        Returns:
            Decoded text

        """
        if self._backend == "callable":
            raise NotImplementedError(
                "Decoding not implemented for callable tokenizers."
            )
        return self.tokenizer.decode(tokens)

    def count_tokens(self, text: str) -> int:
        """Count the number of tokens in the text.

        Args:
            text (str): The text to count tokens in.

        Returns:
            Number of tokens

        """
        if self._backend == "chonkie":
            return self.tokenizer.count_tokens(text)
        elif self._backend == "tiktoken":
            return len(self.tokenizer.encode(text))
        elif self._backend == "transformers":
            return len(self.tokenizer.encode(text, add_special_tokens=False))
        elif self._backend == "tokenizers":
            return len(self.tokenizer.encode(text, add_special_tokens=False).ids)
        elif self._backend == "callable":
            return self.tokenizer(text)
        raise ValueError(f"Unsupported tokenizer backend: {self._backend}")

    ### Batch Functions ###
    def encode_batch(self, texts: Sequence[str]) -> Sequence[Sequence[int]]:
        """Batch encode a list of texts into tokens.

        Args:
            texts (Sequence[str]): The texts to encode.

        Returns:
            List of encoded sequences

        """
        if self._backend == "chonkie":
            return self.tokenizer.encode_batch(texts)
        elif self._backend == "tiktoken":
            return self.tokenizer.encode_batch(texts)
        elif self._backend == "transformers":
            return self.tokenizer.batch_encode_plus(texts, add_special_tokens=False)[
                "input_ids"
            ]
        elif self._backend == "tokenizers":
            return [
                x.ids
                for x in self.tokenizer.encode_batch(texts, add_special_tokens=False)
            ]
        if self._backend == "callable":
            raise NotImplementedError(
                "Batch encoding not implemented for callable tokenizers."
            )
        raise ValueError(f"Unsupported tokenizer backend: {self._backend}")

    def decode_batch(self, token_sequences: Sequence[Sequence[int]]) -> Sequence[str]:
        """Batch decode a list of tokens back into text.

        Args:
            token_sequences (Sequence[Sequence[int]]): The tokens to decode.

        Returns:
            List of decoded texts

        """
        if self._backend == "chonkie":
            return self.tokenizer.decode_batch(token_sequences)
        elif self._backend in "tiktoken":
            return self.tokenizer.decode_batch(token_sequences)
        elif self._backend in "tokenizers":
            return self.tokenizer.decode_batch(token_sequences)
        elif self._backend == "transformers":
            return self.tokenizer.batch_decode(
                token_sequences, skip_special_tokens=True
            )

        if self._backend == "callable":
            raise NotImplementedError(
                "Batch decoding not implemented for callable tokenizers."
            )
        else:
            raise ValueError(f"Unsupported tokenizer backend: {self._backend}")

    def count_tokens_batch(self, texts: Sequence[str]) -> Sequence[int]:
        """Count the number of tokens in a batch of texts.

        Args:
            texts (Sequence[str]): The texts to count tokens in.

        Returns:
            List of token counts

        """
        if self._backend == "chonkie":
            return self.tokenizer.count_tokens_batch(texts)
        elif self._backend == "tiktoken":
            return [
                len(token_list) for token_list in self.tokenizer.encode_batch(texts)
            ]
        elif self._backend == "transformers":
            return [
                len(token_list)
                for token_list in self.tokenizer.batch_encode_plus(
                    texts, add_special_tokens=False
                )["input_ids"]
            ]
        elif self._backend == "tokenizers":
            return [
                len(token_list)
                for token_list in [
                    t.ids
                    for t in self.tokenizer.encode_batch(
                        texts, add_special_tokens=False
                    )
                ]
            ]
        elif self._backend == "callable":
            return [self.tokenizer(text) for text in texts]

        raise ValueError(f"Tokenizer backend {self._backend} not supported.")

```

### File: src\chonkie\__init__.py
```py
"""Main package for Chonkie."""

from .chunker import (
    BaseChunker,
    LateChunker,
    RecursiveChunker,
    SDPMChunker,
    SemanticChunker,
    SentenceChunker,
    TokenChunker,
)
from .embeddings import (
    AutoEmbeddings,
    BaseEmbeddings,
    CohereEmbeddings,
    Model2VecEmbeddings,
    OpenAIEmbeddings,
    SentenceTransformerEmbeddings,
)
from .tokenizer import CharacterTokenizer, Tokenizer, WordTokenizer
from .types import (
    Chunk,
    Context,
    LateChunk,
    RecursiveChunk,
    RecursiveLevel,
    RecursiveRules,
    SemanticChunk,
    SemanticSentence,
    Sentence,
    SentenceChunk,
)

# This hippo grows with every release 🦛✨~
__version__ = "1.0.1"
__name__ = "chonkie"
__author__ = "🦛 Chonkie Inc"

# Add basic package metadata to __all__
__all__ = [
    "__name__",
    "__version__",
    "__author__",
]

# Add all data classes to __all__
__all__ += [
    "Context",
    "Chunk",
    "RecursiveChunk",
    "RecursiveLevel",
    "RecursiveRules",
    "SentenceChunk",
    "SemanticChunk",
    "Sentence",
    "SemanticSentence",
    "LateChunk",
]

# Add all tokenizer classes to __all__
__all__ += [
    "Tokenizer",
    "CharacterTokenizer",
    "WordTokenizer",
]

# Add all chunker classes to __all__
__all__ += [
    "BaseChunker",
    "TokenChunker",
    "SentenceChunker",
    "SemanticChunker",
    "SDPMChunker",
    "RecursiveChunker",
    "LateChunker",
]

# Add all embeddings classes to __all__
__all__ += [
    "BaseEmbeddings",
    "Model2VecEmbeddings",
    "SentenceTransformerEmbeddings",
    "OpenAIEmbeddings",
    "CohereEmbeddings",
    "AutoEmbeddings",
]

```

### File: tests\chunkers\test_late_chunker.py
```py
"""Test cases for the LateChunker class."""

import numpy as np
import pytest

from chonkie import LateChunker
from chonkie.embeddings import SentenceTransformerEmbeddings
from chonkie.types import LateChunk, RecursiveLevel, RecursiveRules


@pytest.fixture
def embedding_model() -> SentenceTransformerEmbeddings:
    """Return an object of SentenceTransformerEmbeddings type."""
    return SentenceTransformerEmbeddings("all-MiniLM-L6-v2")


@pytest.fixture
def sample_text():
    """Return a sample text."""
    text = """# Chunking Strategies in Retrieval-Augmented Generation: A Comprehensive Analysis\n\nIn the rapidly evolving landscape of natural language processing, Retrieval-Augmented Generation (RAG) has emerged as a groundbreaking approach that bridges the gap between large language models and external knowledge bases. At the heart of these systems lies a crucial yet often overlooked process: chunking. This fundamental operation, which involves the systematic decomposition of large text documents into smaller, semantically meaningful units, plays a pivotal role in determining the overall effectiveness of RAG implementations.\n\nThe process of text chunking in RAG applications represents a delicate balance between competing requirements. On one side, we have the need for semantic coherence – ensuring that each chunk maintains meaningful context that can be understood and processed independently. On the other, we must optimize for information density, ensuring that each chunk carries sufficient signal without excessive noise that might impede retrieval accuracy. This balancing act becomes particularly crucial when we consider the downstream implications for vector databases and embedding models that form the backbone of modern RAG systems.\n\nThe selection of appropriate chunk size emerges as a fundamental consideration that significantly impacts system performance. Through extensive experimentation and real-world implementations, researchers have identified that chunks typically perform optimally in the range of 256 to 1024 tokens. However, this range should not be treated as a rigid constraint but rather as a starting point for optimization based on specific use cases and requirements. The implications of chunk size selection ripple throughout the entire RAG pipeline, affecting everything from storage requirements to retrieval accuracy and computational overhead.\n\nFixed-size chunking represents the most straightforward approach to document segmentation, offering predictable memory usage and consistent processing time. However, this apparent simplicity comes with significant drawbacks. By arbitrarily dividing text based on token or character count, fixed-size chunking risks fragmenting semantic units and disrupting the natural flow of information. Consider, for instance, a technical document where a complex concept is explained across several paragraphs – fixed-size chunking might split this explanation at critical junctures, potentially compromising the system's ability to retrieve and present this information coherently.\n\nIn response to these limitations, semantic chunking has gained prominence as a more sophisticated alternative. This approach leverages natural language understanding to identify meaningful boundaries within the text, respecting the natural structure of the document. Semantic chunking can operate at various levels of granularity, from simple sentence-based segmentation to more complex paragraph-level or topic-based approaches. The key advantage lies in its ability to preserve the inherent semantic relationships within the text, leading to more meaningful and contextually relevant retrieval results.\n\nRecent advances in the field have given rise to hybrid approaches that attempt to combine the best aspects of both fixed-size and semantic chunking. These methods typically begin with semantic segmentation but impose size constraints to prevent extreme variations in chunk length. Furthermore, the introduction of sliding window techniques with overlap has proved particularly effective in maintaining context across chunk boundaries. This overlap, typically ranging from 10% to 20% of the chunk size, helps ensure that no critical information is lost at segment boundaries, albeit at the cost of increased storage requirements.\n\nThe implementation of chunking strategies must also consider various technical factors that can significantly impact system performance. Vector database capabilities, embedding model constraints, and runtime performance requirements all play crucial roles in determining the optimal chunking approach. Moreover, content-specific factors such as document structure, language characteristics, and domain-specific requirements must be carefully considered. For instance, technical documentation might benefit from larger chunks that preserve detailed explanations, while news articles might perform better with smaller, more focused segments.\n\nThe future of chunking in RAG systems points toward increasingly sophisticated approaches. Current research explores the potential of neural chunking models that can learn optimal segmentation strategies from large-scale datasets. These models show promise in adapting to different content types and query patterns, potentially leading to more efficient and effective retrieval systems. Additionally, the emergence of cross-lingual chunking strategies addresses the growing need for multilingual RAG applications, while real-time adaptive chunking systems attempt to optimize segment boundaries based on user interaction patterns and retrieval performance metrics.\n\nThe effectiveness of RAG systems heavily depends on the thoughtful implementation of appropriate chunking strategies. While the field continues to evolve, practitioners must carefully consider their specific use cases and requirements when designing chunking solutions. Factors such as document characteristics, retrieval patterns, and performance requirements should guide the selection and optimization of chunking strategies. As we look to the future, the continued development of more sophisticated chunking approaches promises to further enhance the capabilities of RAG systems, enabling more accurate and efficient information retrieval and generation.\n\nThrough careful consideration of these various aspects and continued experimentation with different approaches, organizations can develop chunking strategies that effectively balance the competing demands of semantic coherence, computational efficiency, and retrieval accuracy. As the field continues to evolve, we can expect to see new innovations that further refine our ability to segment and process textual information in ways that enhance the capabilities of RAG systems while maintaining their practical utility in real-world applications."""
    return text


def test_late_chunker_init_with_instance(embedding_model) -> None:
    """Test the initialization of the LateChunker with an embedding model instance."""
    chunker = LateChunker(
        embedding_model=embedding_model,
        chunk_size=256,
        min_characters_per_chunk=10,
    )
    assert chunker is not None
    assert chunker.embedding_model == embedding_model
    assert chunker.chunk_size == 256
    assert chunker.min_characters_per_chunk == 10
    assert chunker._use_multiprocessing is False  # Should be disabled


def test_late_chunker_init_with_string() -> None:
    """Test the initialization of the LateChunker with a model name string."""
    model_name = "all-MiniLM-L6-v2"
    chunker = LateChunker(
        embedding_model=model_name,
        chunk_size=512,
    )
    assert chunker is not None
    assert isinstance(chunker.embedding_model, SentenceTransformerEmbeddings)
    assert chunker.chunk_size == 512


def test_late_chunker_init_invalid_model() -> None:
    """Test initialization failure with an invalid embedding model type."""
    with pytest.raises(ValueError, match="is not a valid embedding model"):
        LateChunker(embedding_model=123)  # type: ignore


def test_late_chunker_chunk_basic(embedding_model, sample_text) -> None:
    """Test basic chunking functionality."""
    chunk_size = 512
    chunker = LateChunker(embedding_model=embedding_model, chunk_size=chunk_size)
    chunks = chunker.chunk(sample_text)

    assert isinstance(chunks, list)
    assert len(chunks) > 0
    assert all(isinstance(chunk, LateChunk) for chunk in chunks)

    # Check attributes of each chunk
    for chunk in chunks:
        assert isinstance(chunk.text, str)
        assert len(chunk.text) > 0
        assert isinstance(chunk.start_index, int)
        assert chunk.start_index >= 0
        assert isinstance(chunk.end_index, int)
        assert chunk.end_index > chunk.start_index
        assert isinstance(chunk.token_count, int)
        assert chunk.token_count > 0
        # Although recursive chunker aims for chunk_size, late chunker's token_count
        # can be slightly different due to adjustment. Check positivity.
        assert isinstance(chunk.embedding, np.ndarray)
        assert chunk.embedding.shape == (embedding_model.dimension,)

    # Rough check: total length should approximate original text length
    assert abs(sum(len(c.text) for c in chunks) - len(sample_text)) < len(chunks) * 2


def test_late_chunker_chunk_empty_text(embedding_model) -> None:
    """Test chunking empty text."""
    chunker = LateChunker(embedding_model=embedding_model)
    chunks = chunker.chunk("")
    assert chunks == []


def test_late_chunker_chunk_short_text(embedding_model) -> None:
    """Test chunking text shorter than chunk size."""
    text = "This is a short text, definitely shorter than the chunk size."
    chunker = LateChunker(embedding_model=embedding_model, chunk_size=512)
    chunks = chunker.chunk(text)

    assert len(chunks) == 1
    chunk = chunks[0]
    assert isinstance(chunk, LateChunk)
    assert chunk.text == text
    assert chunk.start_index == 0
    assert chunk.end_index == len(text)
    assert chunk.token_count > 0
    assert isinstance(chunk.embedding, np.ndarray)
    assert chunk.embedding.shape == (embedding_model.dimension,)


def verify_chunk_indices(chunks: list[LateChunk], original_text: str) -> None:
    """Verify that chunk indices correctly map to the original text."""
    reconstructed_text = ""
    for i, chunk in enumerate(chunks):
        extracted_text = original_text[chunk.start_index : chunk.end_index]
        assert chunk.text == extracted_text, (
            f"Chunk {i} text mismatch:\n"
            f"Chunk text: '{chunk.text}'\n"
            f"Extracted text: '{extracted_text}'\n"
            f"Indices: [{chunk.start_index}:{chunk.end_index}]"
        )
        reconstructed_text += chunk.text

    # Allow minor discrepancies at the very end if needed, but usually should match
    assert reconstructed_text == original_text, (
        "Reconstructed text does not match original"
    )


def test_late_chunker_indices(embedding_model, sample_text) -> None:
    """Test that LateChunker correctly maps chunk indices to the original text."""
    chunker = LateChunker(embedding_model=embedding_model, chunk_size=256)
    chunks = chunker.chunk(sample_text)
    verify_chunk_indices(chunks, sample_text)


def test_late_chunk_repr(embedding_model) -> None:
    """Test the string representation of LateChunk."""
    text = "This is a short text, definitely shorter than the chunk size."
    chunker = LateChunker(embedding_model=embedding_model, chunk_size=50)
    chunks = chunker.chunk(text)
    if not chunks:
        pytest.skip("No chunks generated for repr test")

    chunk = chunks[0]
    representation = repr(chunk)
    assert f"text={chunk.text}" in representation
    assert f"start_index={chunk.start_index}" in representation
    assert f"end_index={chunk.end_index}" in representation
    assert f"token_count={chunk.token_count}" in representation
    assert "embedding=" in representation  # Check for embedding presence
    assert isinstance(chunk.embedding, np.ndarray)


def test_late_chunker_custom_rules(embedding_model, sample_text) -> None:
    """Test that LateChunker works even with custom rules."""
    custom_rules = RecursiveRules([RecursiveLevel([".", "!", "?", "\n"])])
    chunker = LateChunker(
        embedding_model=embedding_model, chunk_size=256, rules=custom_rules
    )
    chunks = chunker.chunk(sample_text)

    # Check if the chunks are generated correctly
    assert len(chunks) > 0, "No chunks generated"
    assert chunks[0].text[-1] in custom_rules.levels[0].delimiters
    assert all([chunk.token_count for chunk in chunks]) < 256

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
