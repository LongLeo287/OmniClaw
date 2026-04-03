---
id: github.com-bhavnicksm-chonkie-main-60923f71-knowle
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:34.113775
---

# KNOWLEDGE EXTRACT: github.com_bhavnicksm_chonkie-main_60923f71
> **Extracted on:** 2026-04-01 10:39:34
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007521023/github.com_bhavnicksm_chonkie-main_60923f71

---

## File: `.gitignore`
```
# Byte-compiled / optimized / DLL files
__pycache__
*.py[cod]
*$py.class

# Distribution / packaging
build/*
dist/
*.egg-info/
*/chonkie.egg-info/*

# Unit test / coverage reports
htmlcov/
.tox/
.coverage
.coverage.*
.cache
coverage.xml
*.cover
.pytest_cache/
.mypy_cache/

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# IDE specific files
.vscode/*
.idea/
*.swp
*.swo

# OS specific files
.DS_Store
Thumbs.db

# Project specific
/tmp/*
/tests/data/*
notebooks/*
```

## File: `BENCHMARKS.md`
```markdown
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

## File: `CONTRIBUTING.md`
```markdown
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
- `brain/knowledge/docs_legacy/description` for documentation changes

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

## File: `LICENSE`
```
MIT License

Copyright (c) 2025 Chonkie

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

## File: `README.md`
```markdown
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

Check out our detailed [benchmarks](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/ai_research/distributed_training_megatron_core/references/benchmarks.md) to see how Chonkie races past the competition! 🏃‍♂️💨

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

## File: `pyproject.toml`
```
[build-system]
requires = ["setuptools>=45", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "chonkie"
version = "1.0.1"
description = "🦛 CHONK your texts with Chonkie ✨ - The no-nonsense chunking library"
readme = "README.md"
requires-python = ">=3.9"
license = { file = "LICENSE" }
keywords = [
    "chunking",
    "rag",
    "retrieval-augmented-generation",
    "nlp",
    "natural-language-processing",
    "text-processing",
    "text-analysis",
    "text-chunking",
    "artificial-intelligence",
    "machine-learning",
]
authors = [
    { name = "Bhavnick Minhas", email = "bhavnick@chonkie.ai" },
    { name = "Shreyash Nigam", email = "shreyash@chonkie.ai" },
]

classifiers = [
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "Intended Audience :: Developers",
    "Intended Audience :: Science/Research",
    "Intended Audience :: Information Technology",
    "Topic :: Scientific/Engineering :: Artificial Intelligence",
    "Topic :: Scientific/Engineering :: Information Analysis",
    "Topic :: Text Processing :: Linguistic",
]
dependencies = ["tokenizers>=0.16.0", "tqdm>=4.64.0"]

[project.urls]
Homepage = "https://github.com/chonkie-inc/chonkie"
Documentation = "https://docs.chonkie.ai"

[project.optional-dependencies]

model2vec = ["model2vec>=0.3.0", "numpy>=2.0.0, <3.0"]
st = ["sentence-transformers>=3.0.0", "numpy>=2.0.0, <3.0", "accelerate>=1.6.0"]
openai = ["tiktoken>=0.5.0", "openai>=1.0.0", "numpy>=2.0.0, <3.0"]
semantic = ["model2vec>=0.3.0", "numpy>=2.0.0, <3.0"]
cohere = ["cohere>=5.13.0", "numpy>=2.0.0, <3.0"]
dev = [
    "tiktoken>=0.5.0",
    "datasets>=1.14.0",
    "transformers>=4.0.0",
    "pytest>=6.2.0",
    "pytest-cov>=4.0.0",
    "coverage",
    "ruff>=0.0.265",
    "mypy>=1.11.0",
]
all = [
    "sentence-transformers>=3.0.0",
    "numpy>=2.0.0, <3.0",
    "openai>=1.0.0",
    "tiktoken>=0.5.0",
    "model2vec>=0.3.0",
    "cohere>=5.13.0",
    "accelerate>=1.6.0",
]

[tool.pytest.ini_options]
pythonpath = "src"

[tool.setuptools]
package-dir = { "" = "src" }
packages = [
    "chonkie",
    "chonkie.chunker",
    "chonkie.types",
    "chonkie.embeddings",
    "chonkie.cloud",
]

[tool.ruff]
exclude = ["*.ipynb"]
lint.select = ["F", "I", "D", "DOC"]
lint.ignore = ["D211", "D213", "D203"]

[tool.ruff.format]
preview = true
indent-style = "space"

[tool.mypy]
disallow_untyped_defs = true
ignore_missing_imports = true
no_implicit_optional = true
check_untyped_defs = true
warn_return_any = true
show_error_codes = true
```

## File: `uv.lock`
```
version = 1
requires-python = ">=3.9"
resolution-markers = [
    "python_full_version < '3.11'",
    "python_full_version == '3.11.*'",
    "python_full_version >= '3.12'",
]

[[package]]
name = "accelerate"
version = "1.6.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "huggingface-hub" },
    { name = "numpy" },
    { name = "packaging" },
    { name = "psutil" },
    { name = "pyyaml" },
    { name = "safetensors" },
    { name = "torch" },
]
sdist = { url = "https://files.pythonhosted.org/packages/8a/6e/c29a1dcde7db07f47870ed63e5124086b11874ad52ccd533dc1ca2c799da/accelerate-1.6.0.tar.gz", hash = "sha256:28c1ef1846e690944f98b68dc7b8bb6c51d032d45e85dcbb3adb0c8b99dffb32", size = 363804 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/63/b1/8198e3cdd11a426b1df2912e3381018c4a4a55368f6d0857ba3ca418ef93/accelerate-1.6.0-py3-none-any.whl", hash = "sha256:1aee717d3d3735ad6d09710a7c26990ee4652b79b4e93df46551551b5227c2aa", size = 354748 },
]

[[package]]
name = "aiohappyeyeballs"
version = "2.6.1"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/26/30/f84a107a9c4331c14b2b586036f40965c128aa4fee4dda5d3d51cb14ad54/aiohappyeyeballs-2.6.1.tar.gz", hash = "sha256:c3f9d0113123803ccadfdf3f0faa505bc78e6a72d1cc4806cbd719826e943558", size = 22760 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/0f/15/5bf3b99495fb160b63f95972b81750f18f7f4e02ad051373b669d17d44f2/aiohappyeyeballs-2.6.1-py3-none-any.whl", hash = "sha256:f349ba8f4b75cb25c99c5c2d84e997e485204d2902a9597802b0371f09331fb8", size = 15265 },
]

[[package]]
name = "aiohttp"
version = "3.11.16"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "aiohappyeyeballs" },
    { name = "aiosignal" },
    { name = "async-timeout", marker = "python_full_version < '3.11'" },
    { name = "attrs" },
    { name = "frozenlist" },
    { name = "multidict" },
    { name = "propcache" },
    { name = "yarl" },
]
sdist = { url = "https://files.pythonhosted.org/packages/f1/d9/1c4721d143e14af753f2bf5e3b681883e1f24b592c0482df6fa6e33597fa/aiohttp-3.11.16.tar.gz", hash = "sha256:16f8a2c9538c14a557b4d309ed4d0a7c60f0253e8ed7b6c9a2859a7582f8b1b8", size = 7676826 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/b8/21/6bd4cb580a323b64cda3b11fcb3f68deba77568e97806727a858de57349d/aiohttp-3.11.16-cp310-cp310-macosx_10_9_universal2.whl", hash = "sha256:fb46bb0f24813e6cede6cc07b1961d4b04f331f7112a23b5e21f567da4ee50aa", size = 708259 },
    { url = "https://files.pythonhosted.org/packages/96/8c/7b4b9debe90ffc31931b85ee8612a5c83f34d8fdc6d90ee3eb27b43639e4/aiohttp-3.11.16-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:54eb3aead72a5c19fad07219acd882c1643a1027fbcdefac9b502c267242f955", size = 468886 },
    { url = "https://files.pythonhosted.org/packages/13/da/a7fcd68e62acacf0a1930060afd2c970826f989265893082b6fb9eb25cb5/aiohttp-3.11.16-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:38bea84ee4fe24ebcc8edeb7b54bf20f06fd53ce4d2cc8b74344c5b9620597fd", size = 455846 },
    { url = "https://files.pythonhosted.org/packages/5d/12/b73d9423253f4c872d276a3771decb0722cb5f962352593bd617445977ba/aiohttp-3.11.16-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:d0666afbe984f6933fe72cd1f1c3560d8c55880a0bdd728ad774006eb4241ecd", size = 1587183 },
    { url = "https://files.pythonhosted.org/packages/75/d3/291b57d54719d996e6cb8c1db8b13d01bdb24dca90434815ac7e6a70393f/aiohttp-3.11.16-cp310-cp310-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:7ba92a2d9ace559a0a14b03d87f47e021e4fa7681dc6970ebbc7b447c7d4b7cd", size = 1634937 },
    { url = "https://files.pythonhosted.org/packages/be/85/4229eba92b433173065b0b459ab677ca11ead4a179f76ccfe55d8738b188/aiohttp-3.11.16-cp310-cp310-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:3ad1d59fd7114e6a08c4814983bb498f391c699f3c78712770077518cae63ff7", size = 1667980 },
    { url = "https://files.pythonhosted.org/packages/2b/0d/d2423936962e3c711fafd5bb9172a99e6b07dd63e086515aa957d8a991fd/aiohttp-3.11.16-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:98b88a2bf26965f2015a771381624dd4b0839034b70d406dc74fd8be4cc053e3", size = 1590365 },
    { url = "https://files.pythonhosted.org/packages/ea/93/04209affc20834982c1ef4214b1afc07743667998a9975d69413e9c1e1c1/aiohttp-3.11.16-cp310-cp310-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:576f5ca28d1b3276026f7df3ec841ae460e0fc3aac2a47cbf72eabcfc0f102e1", size = 1547614 },
    { url = "https://files.pythonhosted.org/packages/f6/fb/194ad4e4cae98023ae19556e576347f402ce159e80d74cc0713d460c4a39/aiohttp-3.11.16-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:a2a450bcce4931b295fc0848f384834c3f9b00edfc2150baafb4488c27953de6", size = 1532815 },
    { url = "https://files.pythonhosted.org/packages/33/6d/a4da7adbac90188bf1228c73b6768a607dd279c146721a9ff7dcb75c5ac6/aiohttp-3.11.16-cp310-cp310-musllinux_1_2_armv7l.whl", hash = "sha256:37dcee4906454ae377be5937ab2a66a9a88377b11dd7c072df7a7c142b63c37c", size = 1559005 },
    { url = "https://files.pythonhosted.org/packages/7e/88/2fa9fbfd23fc16cb2cfdd1f290343e085e7e327438041e9c6aa0208a854d/aiohttp-3.11.16-cp310-cp310-musllinux_1_2_i686.whl", hash = "sha256:4d0c970c0d602b1017e2067ff3b7dac41c98fef4f7472ec2ea26fd8a4e8c2149", size = 1535231 },
    { url = "https://files.pythonhosted.org/packages/f5/8f/9623cd2558e3e182d02dcda8b480643e1c48a0550a86e3050210e98dba27/aiohttp-3.11.16-cp310-cp310-musllinux_1_2_ppc64le.whl", hash = "sha256:004511d3413737700835e949433536a2fe95a7d0297edd911a1e9705c5b5ea43", size = 1609985 },
    { url = "https://files.pythonhosted.org/packages/f8/a2/53a8d1bfc67130710f1c8091f623cdefe7f85cd5d09e14637ed2ed6e1a6d/aiohttp-3.11.16-cp310-cp310-musllinux_1_2_s390x.whl", hash = "sha256:c15b2271c44da77ee9d822552201180779e5e942f3a71fb74e026bf6172ff287", size = 1628842 },
    { url = "https://files.pythonhosted.org/packages/49/3a/35fb43d07489573c6c1f8c6a3e6c657196124a63223705b7feeddaea06f1/aiohttp-3.11.16-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:ad9509ffb2396483ceacb1eee9134724443ee45b92141105a4645857244aecc8", size = 1566929 },
    { url = "https://files.pythonhosted.org/packages/d5/82/bb3f4f2cc7677e790ba4c040db7dd8445c234a810ef893a858e217647d38/aiohttp-3.11.16-cp310-cp310-win32.whl", hash = "sha256:634d96869be6c4dc232fc503e03e40c42d32cfaa51712aee181e922e61d74814", size = 416935 },
    { url = "https://files.pythonhosted.org/packages/df/ad/a64db1c18063569d6dff474c46a7d4de7ab85ff55e2a35839b149b1850ea/aiohttp-3.11.16-cp310-cp310-win_amd64.whl", hash = "sha256:938f756c2b9374bbcc262a37eea521d8a0e6458162f2a9c26329cc87fdf06534", size = 442168 },
    { url = "https://files.pythonhosted.org/packages/b1/98/be30539cd84260d9f3ea1936d50445e25aa6029a4cb9707f3b64cfd710f7/aiohttp-3.11.16-cp311-cp311-macosx_10_9_universal2.whl", hash = "sha256:8cb0688a8d81c63d716e867d59a9ccc389e97ac7037ebef904c2b89334407180", size = 708664 },
    { url = "https://files.pythonhosted.org/packages/e6/27/d51116ce18bdfdea7a2244b55ad38d7b01a4298af55765eed7e8431f013d/aiohttp-3.11.16-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:0ad1fb47da60ae1ddfb316f0ff16d1f3b8e844d1a1e154641928ea0583d486ed", size = 468953 },
    { url = "https://files.pythonhosted.org/packages/34/23/eedf80ec42865ea5355b46265a2433134138eff9a4fea17e1348530fa4ae/aiohttp-3.11.16-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:df7db76400bf46ec6a0a73192b14c8295bdb9812053f4fe53f4e789f3ea66bbb", size = 456065 },
    { url = "https://files.pythonhosted.org/packages/36/23/4a5b1ef6cff994936bf96d981dd817b487d9db755457a0d1c2939920d620/aiohttp-3.11.16-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:cc3a145479a76ad0ed646434d09216d33d08eef0d8c9a11f5ae5cdc37caa3540", size = 1687976 },
    { url = "https://files.pythonhosted.org/packages/d0/5d/c7474b4c3069bb35276d54c82997dff4f7575e4b73f0a7b1b08a39ece1eb/aiohttp-3.11.16-cp311-cp311-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:d007aa39a52d62373bd23428ba4a2546eed0e7643d7bf2e41ddcefd54519842c", size = 1752711 },
    { url = "https://files.pythonhosted.org/packages/64/4c/ee416987b6729558f2eb1b727c60196580aafdb141e83bd78bb031d1c000/aiohttp-3.11.16-cp311-cp311-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:f6ddd90d9fb4b501c97a4458f1c1720e42432c26cb76d28177c5b5ad4e332601", size = 1791305 },
    { url = "https://files.pythonhosted.org/packages/58/28/3e1e1884070b95f1f69c473a1995852a6f8516670bb1c29d6cb2dbb73e1c/aiohttp-3.11.16-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:0a2f451849e6b39e5c226803dcacfa9c7133e9825dcefd2f4e837a2ec5a3bb98", size = 1674499 },
    { url = "https://files.pythonhosted.org/packages/ad/55/a032b32fa80a662d25d9eb170ed1e2c2be239304ca114ec66c89dc40f37f/aiohttp-3.11.16-cp311-cp311-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:8df6612df74409080575dca38a5237282865408016e65636a76a2eb9348c2567", size = 1622313 },
    { url = "https://files.pythonhosted.org/packages/b1/df/ca775605f72abbda4e4746e793c408c84373ca2c6ce7a106a09f853f1e89/aiohttp-3.11.16-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:78e6e23b954644737e385befa0deb20233e2dfddf95dd11e9db752bdd2a294d3", size = 1658274 },
    { url = "https://files.pythonhosted.org/packages/cc/6c/21c45b66124df5b4b0ab638271ecd8c6402b702977120cb4d5be6408e15d/aiohttp-3.11.16-cp311-cp311-musllinux_1_2_armv7l.whl", hash = "sha256:696ef00e8a1f0cec5e30640e64eca75d8e777933d1438f4facc9c0cdf288a810", size = 1666704 },
    { url = "https://files.pythonhosted.org/packages/1d/e2/7d92adc03e3458edd18a21da2575ab84e58f16b1672ae98529e4eeee45ab/aiohttp-3.11.16-cp311-cp311-musllinux_1_2_i686.whl", hash = "sha256:e3538bc9fe1b902bef51372462e3d7c96fce2b566642512138a480b7adc9d508", size = 1652815 },
    { url = "https://files.pythonhosted.org/packages/3a/52/7549573cd654ad651e3c5786ec3946d8f0ee379023e22deb503ff856b16c/aiohttp-3.11.16-cp311-cp311-musllinux_1_2_ppc64le.whl", hash = "sha256:3ab3367bb7f61ad18793fea2ef71f2d181c528c87948638366bf1de26e239183", size = 1735669 },
    { url = "https://files.pythonhosted.org/packages/d5/54/dcd24a23c7a5a2922123e07a296a5f79ea87ce605f531be068415c326de6/aiohttp-3.11.16-cp311-cp311-musllinux_1_2_s390x.whl", hash = "sha256:56a3443aca82abda0e07be2e1ecb76a050714faf2be84256dae291182ba59049", size = 1760422 },
    { url = "https://files.pythonhosted.org/packages/a7/53/87327fe982fa310944e1450e97bf7b2a28015263771931372a1dfe682c58/aiohttp-3.11.16-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:61c721764e41af907c9d16b6daa05a458f066015abd35923051be8705108ed17", size = 1694457 },
    { url = "https://files.pythonhosted.org/packages/ce/6d/c5ccf41059267bcf89853d3db9d8d217dacf0a04f4086cb6bf278323011f/aiohttp-3.11.16-cp311-cp311-win32.whl", hash = "sha256:3e061b09f6fa42997cf627307f220315e313ece74907d35776ec4373ed718b86", size = 416817 },
    { url = "https://files.pythonhosted.org/packages/e7/dd/01f6fe028e054ef4f909c9d63e3a2399e77021bb2e1bb51d56ca8b543989/aiohttp-3.11.16-cp311-cp311-win_amd64.whl", hash = "sha256:745f1ed5e2c687baefc3c5e7b4304e91bf3e2f32834d07baaee243e349624b24", size = 442986 },
    { url = "https://files.pythonhosted.org/packages/db/38/100d01cbc60553743baf0fba658cb125f8ad674a8a771f765cdc155a890d/aiohttp-3.11.16-cp312-cp312-macosx_10_13_universal2.whl", hash = "sha256:911a6e91d08bb2c72938bc17f0a2d97864c531536b7832abee6429d5296e5b27", size = 704881 },
    { url = "https://files.pythonhosted.org/packages/21/ed/b4102bb6245e36591209e29f03fe87e7956e54cb604ee12e20f7eb47f994/aiohttp-3.11.16-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:6ac13b71761e49d5f9e4d05d33683bbafef753e876e8e5a7ef26e937dd766713", size = 464564 },
    { url = "https://files.pythonhosted.org/packages/3b/e1/a9ab6c47b62ecee080eeb33acd5352b40ecad08fb2d0779bcc6739271745/aiohttp-3.11.16-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:fd36c119c5d6551bce374fcb5c19269638f8d09862445f85a5a48596fd59f4bb", size = 456548 },
    { url = "https://files.pythonhosted.org/packages/80/ad/216c6f71bdff2becce6c8776f0aa32cb0fa5d83008d13b49c3208d2e4016/aiohttp-3.11.16-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:d489d9778522fbd0f8d6a5c6e48e3514f11be81cb0a5954bdda06f7e1594b321", size = 1691749 },
    { url = "https://files.pythonhosted.org/packages/bd/ea/7df7bcd3f4e734301605f686ffc87993f2d51b7acb6bcc9b980af223f297/aiohttp-3.11.16-cp312-cp312-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:69a2cbd61788d26f8f1e626e188044834f37f6ae3f937bd9f08b65fc9d7e514e", size = 1736874 },
    { url = "https://files.pythonhosted.org/packages/51/41/c7724b9c87a29b7cfd1202ec6446bae8524a751473d25e2ff438bc9a02bf/aiohttp-3.11.16-cp312-cp312-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:cd464ba806e27ee24a91362ba3621bfc39dbbb8b79f2e1340201615197370f7c", size = 1786885 },
    { url = "https://files.pythonhosted.org/packages/86/b3/f61f8492fa6569fa87927ad35a40c159408862f7e8e70deaaead349e2fba/aiohttp-3.11.16-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:1ce63ae04719513dd2651202352a2beb9f67f55cb8490c40f056cea3c5c355ce", size = 1698059 },
    { url = "https://files.pythonhosted.org/packages/ce/be/7097cf860a9ce8bbb0e8960704e12869e111abcd3fbd245153373079ccec/aiohttp-3.11.16-cp312-cp312-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:09b00dd520d88eac9d1768439a59ab3d145065c91a8fab97f900d1b5f802895e", size = 1626527 },
    { url = "https://files.pythonhosted.org/packages/1d/1d/aaa841c340e8c143a8d53a1f644c2a2961c58cfa26e7b398d6bf75cf5d23/aiohttp-3.11.16-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:7f6428fee52d2bcf96a8aa7b62095b190ee341ab0e6b1bcf50c615d7966fd45b", size = 1644036 },
    { url = "https://files.pythonhosted.org/packages/2c/88/59d870f76e9345e2b149f158074e78db457985c2b4da713038d9da3020a8/aiohttp-3.11.16-cp312-cp312-musllinux_1_2_armv7l.whl", hash = "sha256:13ceac2c5cdcc3f64b9015710221ddf81c900c5febc505dbd8f810e770011540", size = 1685270 },
    { url = "https://files.pythonhosted.org/packages/2b/b1/c6686948d4c79c3745595efc469a9f8a43cab3c7efc0b5991be65d9e8cb8/aiohttp-3.11.16-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:fadbb8f1d4140825069db3fedbbb843290fd5f5bc0a5dbd7eaf81d91bf1b003b", size = 1650852 },
    { url = "https://files.pythonhosted.org/packages/fe/94/3e42a6916fd3441721941e0f1b8438e1ce2a4c49af0e28e0d3c950c9b3c9/aiohttp-3.11.16-cp312-cp312-musllinux_1_2_ppc64le.whl", hash = "sha256:6a792ce34b999fbe04a7a71a90c74f10c57ae4c51f65461a411faa70e154154e", size = 1704481 },
    { url = "https://files.pythonhosted.org/packages/b1/6d/6ab5854ff59b27075c7a8c610597d2b6c38945f9a1284ee8758bc3720ff6/aiohttp-3.11.16-cp312-cp312-musllinux_1_2_s390x.whl", hash = "sha256:f4065145bf69de124accdd17ea5f4dc770da0a6a6e440c53f6e0a8c27b3e635c", size = 1735370 },
    { url = "https://files.pythonhosted.org/packages/73/2a/08a68eec3c99a6659067d271d7553e4d490a0828d588e1daa3970dc2b771/aiohttp-3.11.16-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:fa73e8c2656a3653ae6c307b3f4e878a21f87859a9afab228280ddccd7369d71", size = 1697619 },
    { url = "https://files.pythonhosted.org/packages/61/d5/fea8dbbfb0cd68fbb56f0ae913270a79422d9a41da442a624febf72d2aaf/aiohttp-3.11.16-cp312-cp312-win32.whl", hash = "sha256:f244b8e541f414664889e2c87cac11a07b918cb4b540c36f7ada7bfa76571ea2", size = 411710 },
    { url = "https://files.pythonhosted.org/packages/33/fb/41cde15fbe51365024550bf77b95a4fc84ef41365705c946da0421f0e1e0/aiohttp-3.11.16-cp312-cp312-win_amd64.whl", hash = "sha256:23a15727fbfccab973343b6d1b7181bfb0b4aa7ae280f36fd2f90f5476805682", size = 438012 },
    { url = "https://files.pythonhosted.org/packages/52/52/7c712b2d9fb4d5e5fd6d12f9ab76e52baddfee71e3c8203ca7a7559d7f51/aiohttp-3.11.16-cp313-cp313-macosx_10_13_universal2.whl", hash = "sha256:a3814760a1a700f3cfd2f977249f1032301d0a12c92aba74605cfa6ce9f78489", size = 698005 },
    { url = "https://files.pythonhosted.org/packages/51/3e/61057814f7247666d43ac538abcd6335b022869ade2602dab9bf33f607d2/aiohttp-3.11.16-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:9b751a6306f330801665ae69270a8a3993654a85569b3469662efaad6cf5cc50", size = 461106 },
    { url = "https://files.pythonhosted.org/packages/4f/85/6b79fb0ea6e913d596d5b949edc2402b20803f51b1a59e1bbc5bb7ba7569/aiohttp-3.11.16-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:ad497f38a0d6c329cb621774788583ee12321863cd4bd9feee1effd60f2ad133", size = 453394 },
    { url = "https://files.pythonhosted.org/packages/4b/04/e1bb3fcfbd2c26753932c759593a32299aff8625eaa0bf8ff7d9c0c34a36/aiohttp-3.11.16-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:ca37057625693d097543bd88076ceebeb248291df9d6ca8481349efc0b05dcd0", size = 1666643 },
    { url = "https://files.pythonhosted.org/packages/0e/27/97bc0fdd1f439b8f060beb3ba8fb47b908dc170280090801158381ad7942/aiohttp-3.11.16-cp313-cp313-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:a5abcbba9f4b463a45c8ca8b7720891200658f6f46894f79517e6cd11f3405ca", size = 1721948 },
    { url = "https://files.pythonhosted.org/packages/2c/4f/bc4c5119e75c05ef15c5670ef1563bbe25d4ed4893b76c57b0184d815e8b/aiohttp-3.11.16-cp313-cp313-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:f420bfe862fb357a6d76f2065447ef6f484bc489292ac91e29bc65d2d7a2c84d", size = 1774454 },
    { url = "https://files.pythonhosted.org/packages/73/5b/54b42b2150bb26fdf795464aa55ceb1a49c85f84e98e6896d211eabc6670/aiohttp-3.11.16-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:58ede86453a6cf2d6ce40ef0ca15481677a66950e73b0a788917916f7e35a0bb", size = 1677785 },
    { url = "https://files.pythonhosted.org/packages/10/ee/a0fe68916d3f82eae199b8535624cf07a9c0a0958c7a76e56dd21140487a/aiohttp-3.11.16-cp313-cp313-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:6fdec0213244c39973674ca2a7f5435bf74369e7d4e104d6c7473c81c9bcc8c4", size = 1608456 },
    { url = "https://files.pythonhosted.org/packages/8b/48/83afd779242b7cf7e1ceed2ff624a86d3221e17798061cf9a79e0b246077/aiohttp-3.11.16-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:72b1b03fb4655c1960403c131740755ec19c5898c82abd3961c364c2afd59fe7", size = 1622424 },
    { url = "https://files.pythonhosted.org/packages/6f/27/452f1d5fca1f516f9f731539b7f5faa9e9d3bf8a3a6c3cd7c4b031f20cbd/aiohttp-3.11.16-cp313-cp313-musllinux_1_2_armv7l.whl", hash = "sha256:780df0d837276276226a1ff803f8d0fa5f8996c479aeef52eb040179f3156cbd", size = 1660943 },
    { url = "https://files.pythonhosted.org/packages/d6/e1/5c7d63143b8d00c83b958b9e78e7048c4a69903c760c1e329bf02bac57a1/aiohttp-3.11.16-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:ecdb8173e6c7aa09eee342ac62e193e6904923bd232e76b4157ac0bfa670609f", size = 1622797 },
    { url = "https://files.pythonhosted.org/packages/46/9e/2ac29cca2746ee8e449e73cd2fcb3d454467393ec03a269d50e49af743f1/aiohttp-3.11.16-cp313-cp313-musllinux_1_2_ppc64le.whl", hash = "sha256:a6db7458ab89c7d80bc1f4e930cc9df6edee2200127cfa6f6e080cf619eddfbd", size = 1687162 },
    { url = "https://files.pythonhosted.org/packages/ad/6b/eaa6768e02edebaf37d77f4ffb74dd55f5cbcbb6a0dbf798ccec7b0ac23b/aiohttp-3.11.16-cp313-cp313-musllinux_1_2_s390x.whl", hash = "sha256:2540ddc83cc724b13d1838026f6a5ad178510953302a49e6d647f6e1de82bc34", size = 1718518 },
    { url = "https://files.pythonhosted.org/packages/e5/18/dda87cbad29472a51fa058d6d8257dfce168289adaeb358b86bd93af3b20/aiohttp-3.11.16-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:3b4e6db8dc4879015b9955778cfb9881897339c8fab7b3676f8433f849425913", size = 1675254 },
    { url = "https://files.pythonhosted.org/packages/32/d9/d2fb08c614df401d92c12fcbc60e6e879608d5e8909ef75c5ad8d4ad8aa7/aiohttp-3.11.16-cp313-cp313-win32.whl", hash = "sha256:493910ceb2764f792db4dc6e8e4b375dae1b08f72e18e8f10f18b34ca17d0979", size = 410698 },
    { url = "https://files.pythonhosted.org/packages/ce/ed/853e36d5a33c24544cfa46585895547de152dfef0b5c79fa675f6e4b7b87/aiohttp-3.11.16-cp313-cp313-win_amd64.whl", hash = "sha256:42864e70a248f5f6a49fdaf417d9bc62d6e4d8ee9695b24c5916cb4bb666c802", size = 436395 },
    { url = "https://files.pythonhosted.org/packages/4b/6e/a423a6fd07e651f6078da862128031cff2f333e995f5efe30bb110c97041/aiohttp-3.11.16-cp39-cp39-macosx_10_9_universal2.whl", hash = "sha256:bbcba75fe879ad6fd2e0d6a8d937f34a571f116a0e4db37df8079e738ea95c71", size = 709172 },
    { url = "https://files.pythonhosted.org/packages/bf/8d/925f3c893523118e5dc729d340df2283d68e7adfa77192908ae63f1ec904/aiohttp-3.11.16-cp39-cp39-macosx_10_9_x86_64.whl", hash = "sha256:87a6e922b2b2401e0b0cf6b976b97f11ec7f136bfed445e16384fbf6fd5e8602", size = 469390 },
    { url = "https://files.pythonhosted.org/packages/49/57/8a27b793480887bd23288364138c9db2f58cd3cff28945809aa062d019dc/aiohttp-3.11.16-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:ccf10f16ab498d20e28bc2b5c1306e9c1512f2840f7b6a67000a517a4b37d5ee", size = 456246 },
    { url = "https://files.pythonhosted.org/packages/e8/e5/e8114c5b1336357089cacf5a4ff298335429f0a0e75dea3ffefd3d4d82e5/aiohttp-3.11.16-cp39-cp39-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:fb3d0cc5cdb926090748ea60172fa8a213cec728bd6c54eae18b96040fcd6227", size = 1590764 },
    { url = "https://files.pythonhosted.org/packages/db/49/ec13c0ad70c4843169111265c47dd568437be354aea4ac732dc6f2e79842/aiohttp-3.11.16-cp39-cp39-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:d07502cc14ecd64f52b2a74ebbc106893d9a9717120057ea9ea1fd6568a747e7", size = 1638375 },
    { url = "https://files.pythonhosted.org/packages/0f/0d/78a64579b054fa3c0e72083912d4410f5514dc0cd03bef5644d4f1e4e6ed/aiohttp-3.11.16-cp39-cp39-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:776c8e959a01e5e8321f1dec77964cb6101020a69d5a94cd3d34db6d555e01f7", size = 1672027 },
    { url = "https://files.pythonhosted.org/packages/54/11/06602ab3446fe96519998b79c762cf0921b620e702bd7659a5e8b998d0e0/aiohttp-3.11.16-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:0902e887b0e1d50424112f200eb9ae3dfed6c0d0a19fc60f633ae5a57c809656", size = 1589609 },
    { url = "https://files.pythonhosted.org/packages/34/1b/6bdebdf702d7f339579e9d3c2e784ca6e5867e247dd7b8690c004431ab57/aiohttp-3.11.16-cp39-cp39-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:e87fd812899aa78252866ae03a048e77bd11b80fb4878ce27c23cade239b42b2", size = 1547540 },
    { url = "https://files.pythonhosted.org/packages/88/dd/5d0c0a936baaabbf7467851c0cc9f1aedab67428479a528ea14ab852c730/aiohttp-3.11.16-cp39-cp39-musllinux_1_2_aarch64.whl", hash = "sha256:0a950c2eb8ff17361abd8c85987fd6076d9f47d040ebffce67dce4993285e973", size = 1534880 },
    { url = "https://files.pythonhosted.org/packages/a8/ff/2245148b047833eb7b37f5754ece17ade561a46c40d6fecc3ed3f5eae1c1/aiohttp-3.11.16-cp39-cp39-musllinux_1_2_armv7l.whl", hash = "sha256:c10d85e81d0b9ef87970ecbdbfaeec14a361a7fa947118817fcea8e45335fa46", size = 1557692 },
    { url = "https://files.pythonhosted.org/packages/c4/1c/fe0dd097427c295ae49b6c10e37eda546036fd8de75bc43d69df392b9377/aiohttp-3.11.16-cp39-cp39-musllinux_1_2_i686.whl", hash = "sha256:7951decace76a9271a1ef181b04aa77d3cc309a02a51d73826039003210bdc86", size = 1538918 },
    { url = "https://files.pythonhosted.org/packages/94/58/10af247fb0084327579ebaccfd1f9c2f759ec972b204b31598debfa0829a/aiohttp-3.11.16-cp39-cp39-musllinux_1_2_ppc64le.whl", hash = "sha256:14461157d8426bcb40bd94deb0450a6fa16f05129f7da546090cebf8f3123b0f", size = 1609351 },
    { url = "https://files.pythonhosted.org/packages/d3/91/b1f0928b6d2eb0c47ecee7122067a8ad330f812795d8f16343d206394040/aiohttp-3.11.16-cp39-cp39-musllinux_1_2_s390x.whl", hash = "sha256:9756d9b9d4547e091f99d554fbba0d2a920aab98caa82a8fb3d3d9bee3c9ae85", size = 1630514 },
    { url = "https://files.pythonhosted.org/packages/88/51/3319add72ea4053bee66825aef3e691ee4b26d0a22b7f817d73b0af02d38/aiohttp-3.11.16-cp39-cp39-musllinux_1_2_x86_64.whl", hash = "sha256:87944bd16b7fe6160607f6a17808abd25f17f61ae1e26c47a491b970fb66d8cb", size = 1567084 },
    { url = "https://files.pythonhosted.org/packages/e5/93/e90a84c263f02f01efd6f32042c08d7f7d88338cb18d91c5b1752accffeb/aiohttp-3.11.16-cp39-cp39-win32.whl", hash = "sha256:92b7ee222e2b903e0a4b329a9943d432b3767f2d5029dbe4ca59fb75223bbe2e", size = 417187 },
    { url = "https://files.pythonhosted.org/packages/11/b8/7200f637f223199d8f3e7add720ab19843b9969ffa89b758b5649cab8099/aiohttp-3.11.16-cp39-cp39-win_amd64.whl", hash = "sha256:17ae4664031aadfbcb34fd40ffd90976671fa0c0286e6c4113989f78bebab37a", size = 442378 },
]

[[package]]
name = "aiosignal"
version = "1.3.2"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "frozenlist" },
]
sdist = { url = "https://files.pythonhosted.org/packages/ba/b5/6d55e80f6d8a08ce22b982eafa278d823b541c925f11ee774b0b9c43473d/aiosignal-1.3.2.tar.gz", hash = "sha256:a8c255c66fafb1e499c9351d0bf32ff2d8a0321595ebac3b93713656d2436f54", size = 19424 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/ec/6a/bc7e17a3e87a2985d3e8f4da4cd0f481060eb78fb08596c42be62c90a4d9/aiosignal-1.3.2-py2.py3-none-any.whl", hash = "sha256:45cde58e409a301715980c2b01d0c28bdde3770d8290b5eb2173759d9acb31a5", size = 7597 },
]

[[package]]
name = "annotated-types"
version = "0.7.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/ee/67/531ea369ba64dcff5ec9c3402f9f51bf748cec26dde048a2f973a4eea7f5/annotated_types-0.7.0.tar.gz", hash = "sha256:aff07c09a53a08bc8cfccb9c85b05f1aa9a2a6f23728d790723543408344ce89", size = 16081 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/78/b6/6307fbef88d9b5ee7421e68d78a9f162e0da4900bc5f5793f6d3d0e34fb8/annotated_types-0.7.0-py3-none-any.whl", hash = "sha256:1f02e8b43a8fbbc3f3e0d4f0f4bfc8131bcb4eebe8849b8e5c773f3a1c582a53", size = 13643 },
]

[[package]]
name = "anyio"
version = "4.9.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "exceptiongroup", marker = "python_full_version < '3.11'" },
    { name = "idna" },
    { name = "sniffio" },
    { name = "typing-extensions", marker = "python_full_version < '3.13'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/95/7d/4c1bd541d4dffa1b52bd83fb8527089e097a106fc90b467a7313b105f840/anyio-4.9.0.tar.gz", hash = "sha256:673c0c244e15788651a4ff38710fea9675823028a6f08a5eda409e0c9840a028", size = 190949 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/a1/ee/48ca1a7c89ffec8b6a0c5d02b89c305671d5ffd8d3c94acf8b8c408575bb/anyio-4.9.0-py3-none-any.whl", hash = "sha256:9f76d541cad6e36af7beb62e978876f3b41e3e04f2c1fbf0884604c0a9c4d93c", size = 100916 },
]

[[package]]
name = "async-timeout"
version = "5.0.1"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/a5/ae/136395dfbfe00dfc94da3f3e136d0b13f394cba8f4841120e34226265780/async_timeout-5.0.1.tar.gz", hash = "sha256:d9321a7a3d5a6a5e187e824d2fa0793ce379a202935782d555d6e9d2735677d3", size = 9274 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/fe/ba/e2081de779ca30d473f21f5b30e0e737c438205440784c7dfc81efc2b029/async_timeout-5.0.1-py3-none-any.whl", hash = "sha256:39e3809566ff85354557ec2398b55e096c8364bacac9405a7a1fa429e77fe76c", size = 6233 },
]

[[package]]
name = "attrs"
version = "25.3.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/5a/b0/1367933a8532ee6ff8d63537de4f1177af4bff9f3e829baf7331f595bb24/attrs-25.3.0.tar.gz", hash = "sha256:75d7cefc7fb576747b2c81b4442d4d4a1ce0900973527c011d1030fd3bf4af1b", size = 812032 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/77/06/bb80f5f86020c4551da315d78b3ab75e8228f89f0162f2c3a819e407941a/attrs-25.3.0-py3-none-any.whl", hash = "sha256:427318ce031701fea540783410126f03899a97ffc6f61596ad581ac2e40e3bc3", size = 63815 },
]

[[package]]
name = "certifi"
version = "2025.1.31"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/1c/ab/c9f1e32b7b1bf505bf26f0ef697775960db7932abeb7b516de930ba2705f/certifi-2025.1.31.tar.gz", hash = "sha256:3d5da6925056f6f18f119200434a4780a94263f10d1c21d032a6f6b2baa20651", size = 167577 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/38/fc/bce832fd4fd99766c04d1ee0eead6b0ec6486fb100ae5e74c1d91292b982/certifi-2025.1.31-py3-none-any.whl", hash = "sha256:ca78db4565a652026a4db2bcdf68f2fb589ea80d0be70e03929ed730746b84fe", size = 166393 },
]

[[package]]
name = "charset-normalizer"
version = "3.4.1"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/16/b0/572805e227f01586461c80e0fd25d65a2115599cc9dad142fee4b747c357/charset_normalizer-3.4.1.tar.gz", hash = "sha256:44251f18cd68a75b56585dd00dae26183e102cd5e0f9f1466e6df5da2ed64ea3", size = 123188 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/0d/58/5580c1716040bc89206c77d8f74418caf82ce519aae06450393ca73475d1/charset_normalizer-3.4.1-cp310-cp310-macosx_10_9_universal2.whl", hash = "sha256:91b36a978b5ae0ee86c394f5a54d6ef44db1de0815eb43de826d41d21e4af3de", size = 198013 },
    { url = "https://files.pythonhosted.org/packages/d0/11/00341177ae71c6f5159a08168bcb98c6e6d196d372c94511f9f6c9afe0c6/charset_normalizer-3.4.1-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:7461baadb4dc00fd9e0acbe254e3d7d2112e7f92ced2adc96e54ef6501c5f176", size = 141285 },
    { url = "https://files.pythonhosted.org/packages/01/09/11d684ea5819e5a8f5100fb0b38cf8d02b514746607934134d31233e02c8/charset_normalizer-3.4.1-cp310-cp310-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:e218488cd232553829be0664c2292d3af2eeeb94b32bea483cf79ac6a694e037", size = 151449 },
    { url = "https://files.pythonhosted.org/packages/08/06/9f5a12939db324d905dc1f70591ae7d7898d030d7662f0d426e2286f68c9/charset_normalizer-3.4.1-cp310-cp310-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:80ed5e856eb7f30115aaf94e4a08114ccc8813e6ed1b5efa74f9f82e8509858f", size = 143892 },
    { url = "https://files.pythonhosted.org/packages/93/62/5e89cdfe04584cb7f4d36003ffa2936681b03ecc0754f8e969c2becb7e24/charset_normalizer-3.4.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:b010a7a4fd316c3c484d482922d13044979e78d1861f0e0650423144c616a46a", size = 146123 },
    { url = "https://files.pythonhosted.org/packages/a9/ac/ab729a15c516da2ab70a05f8722ecfccc3f04ed7a18e45c75bbbaa347d61/charset_normalizer-3.4.1-cp310-cp310-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:4532bff1b8421fd0a320463030c7520f56a79c9024a4e88f01c537316019005a", size = 147943 },
    { url = "https://files.pythonhosted.org/packages/03/d2/3f392f23f042615689456e9a274640c1d2e5dd1d52de36ab8f7955f8f050/charset_normalizer-3.4.1-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:d973f03c0cb71c5ed99037b870f2be986c3c05e63622c017ea9816881d2dd247", size = 142063 },
    { url = "https://files.pythonhosted.org/packages/f2/e3/e20aae5e1039a2cd9b08d9205f52142329f887f8cf70da3650326670bddf/charset_normalizer-3.4.1-cp310-cp310-musllinux_1_2_i686.whl", hash = "sha256:3a3bd0dcd373514dcec91c411ddb9632c0d7d92aed7093b8c3bbb6d69ca74408", size = 150578 },
    { url = "https://files.pythonhosted.org/packages/8d/af/779ad72a4da0aed925e1139d458adc486e61076d7ecdcc09e610ea8678db/charset_normalizer-3.4.1-cp310-cp310-musllinux_1_2_ppc64le.whl", hash = "sha256:d9c3cdf5390dcd29aa8056d13e8e99526cda0305acc038b96b30352aff5ff2bb", size = 153629 },
    { url = "https://files.pythonhosted.org/packages/c2/b6/7aa450b278e7aa92cf7732140bfd8be21f5f29d5bf334ae987c945276639/charset_normalizer-3.4.1-cp310-cp310-musllinux_1_2_s390x.whl", hash = "sha256:2bdfe3ac2e1bbe5b59a1a63721eb3b95fc9b6817ae4a46debbb4e11f6232428d", size = 150778 },
    { url = "https://files.pythonhosted.org/packages/39/f4/d9f4f712d0951dcbfd42920d3db81b00dd23b6ab520419626f4023334056/charset_normalizer-3.4.1-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:eab677309cdb30d047996b36d34caeda1dc91149e4fdca0b1a039b3f79d9a807", size = 146453 },
    { url = "https://files.pythonhosted.org/packages/49/2b/999d0314e4ee0cff3cb83e6bc9aeddd397eeed693edb4facb901eb8fbb69/charset_normalizer-3.4.1-cp310-cp310-win32.whl", hash = "sha256:c0429126cf75e16c4f0ad00ee0eae4242dc652290f940152ca8c75c3a4b6ee8f", size = 95479 },
    { url = "https://files.pythonhosted.org/packages/2d/ce/3cbed41cff67e455a386fb5e5dd8906cdda2ed92fbc6297921f2e4419309/charset_normalizer-3.4.1-cp310-cp310-win_amd64.whl", hash = "sha256:9f0b8b1c6d84c8034a44893aba5e767bf9c7a211e313a9605d9c617d7083829f", size = 102790 },
    { url = "https://files.pythonhosted.org/packages/72/80/41ef5d5a7935d2d3a773e3eaebf0a9350542f2cab4eac59a7a4741fbbbbe/charset_normalizer-3.4.1-cp311-cp311-macosx_10_9_universal2.whl", hash = "sha256:8bfa33f4f2672964266e940dd22a195989ba31669bd84629f05fab3ef4e2d125", size = 194995 },
    { url = "https://files.pythonhosted.org/packages/7a/28/0b9fefa7b8b080ec492110af6d88aa3dea91c464b17d53474b6e9ba5d2c5/charset_normalizer-3.4.1-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:28bf57629c75e810b6ae989f03c0828d64d6b26a5e205535585f96093e405ed1", size = 139471 },
    { url = "https://files.pythonhosted.org/packages/71/64/d24ab1a997efb06402e3fc07317e94da358e2585165930d9d59ad45fcae2/charset_normalizer-3.4.1-cp311-cp311-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:f08ff5e948271dc7e18a35641d2f11a4cd8dfd5634f55228b691e62b37125eb3", size = 149831 },
    { url = "https://files.pythonhosted.org/packages/37/ed/be39e5258e198655240db5e19e0b11379163ad7070962d6b0c87ed2c4d39/charset_normalizer-3.4.1-cp311-cp311-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:234ac59ea147c59ee4da87a0c0f098e9c8d169f4dc2a159ef720f1a61bbe27cd", size = 142335 },
    { url = "https://files.pythonhosted.org/packages/88/83/489e9504711fa05d8dde1574996408026bdbdbd938f23be67deebb5eca92/charset_normalizer-3.4.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:fd4ec41f914fa74ad1b8304bbc634b3de73d2a0889bd32076342a573e0779e00", size = 143862 },
    { url = "https://files.pythonhosted.org/packages/c6/c7/32da20821cf387b759ad24627a9aca289d2822de929b8a41b6241767b461/charset_normalizer-3.4.1-cp311-cp311-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:eea6ee1db730b3483adf394ea72f808b6e18cf3cb6454b4d86e04fa8c4327a12", size = 145673 },
    { url = "https://files.pythonhosted.org/packages/68/85/f4288e96039abdd5aeb5c546fa20a37b50da71b5cf01e75e87f16cd43304/charset_normalizer-3.4.1-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:c96836c97b1238e9c9e3fe90844c947d5afbf4f4c92762679acfe19927d81d77", size = 140211 },
    { url = "https://files.pythonhosted.org/packages/28/a3/a42e70d03cbdabc18997baf4f0227c73591a08041c149e710045c281f97b/charset_normalizer-3.4.1-cp311-cp311-musllinux_1_2_i686.whl", hash = "sha256:4d86f7aff21ee58f26dcf5ae81a9addbd914115cdebcbb2217e4f0ed8982e146", size = 148039 },
    { url = "https://files.pythonhosted.org/packages/85/e4/65699e8ab3014ecbe6f5c71d1a55d810fb716bbfd74f6283d5c2aa87febf/charset_normalizer-3.4.1-cp311-cp311-musllinux_1_2_ppc64le.whl", hash = "sha256:09b5e6733cbd160dcc09589227187e242a30a49ca5cefa5a7edd3f9d19ed53fd", size = 151939 },
    { url = "https://files.pythonhosted.org/packages/b1/82/8e9fe624cc5374193de6860aba3ea8070f584c8565ee77c168ec13274bd2/charset_normalizer-3.4.1-cp311-cp311-musllinux_1_2_s390x.whl", hash = "sha256:5777ee0881f9499ed0f71cc82cf873d9a0ca8af166dfa0af8ec4e675b7df48e6", size = 149075 },
    { url = "https://files.pythonhosted.org/packages/3d/7b/82865ba54c765560c8433f65e8acb9217cb839a9e32b42af4aa8e945870f/charset_normalizer-3.4.1-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:237bdbe6159cff53b4f24f397d43c6336c6b0b42affbe857970cefbb620911c8", size = 144340 },
    { url = "https://files.pythonhosted.org/packages/b5/b6/9674a4b7d4d99a0d2df9b215da766ee682718f88055751e1e5e753c82db0/charset_normalizer-3.4.1-cp311-cp311-win32.whl", hash = "sha256:8417cb1f36cc0bc7eaba8ccb0e04d55f0ee52df06df3ad55259b9a323555fc8b", size = 95205 },
    { url = "https://files.pythonhosted.org/packages/1e/ab/45b180e175de4402dcf7547e4fb617283bae54ce35c27930a6f35b6bef15/charset_normalizer-3.4.1-cp311-cp311-win_amd64.whl", hash = "sha256:d7f50a1f8c450f3925cb367d011448c39239bb3eb4117c36a6d354794de4ce76", size = 102441 },
    { url = "https://files.pythonhosted.org/packages/0a/9a/dd1e1cdceb841925b7798369a09279bd1cf183cef0f9ddf15a3a6502ee45/charset_normalizer-3.4.1-cp312-cp312-macosx_10_13_universal2.whl", hash = "sha256:73d94b58ec7fecbc7366247d3b0b10a21681004153238750bb67bd9012414545", size = 196105 },
    { url = "https://files.pythonhosted.org/packages/d3/8c/90bfabf8c4809ecb648f39794cf2a84ff2e7d2a6cf159fe68d9a26160467/charset_normalizer-3.4.1-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:dad3e487649f498dd991eeb901125411559b22e8d7ab25d3aeb1af367df5efd7", size = 140404 },
    { url = "https://files.pythonhosted.org/packages/ad/8f/e410d57c721945ea3b4f1a04b74f70ce8fa800d393d72899f0a40526401f/charset_normalizer-3.4.1-cp312-cp312-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:c30197aa96e8eed02200a83fba2657b4c3acd0f0aa4bdc9f6c1af8e8962e0757", size = 150423 },
    { url = "https://files.pythonhosted.org/packages/f0/b8/e6825e25deb691ff98cf5c9072ee0605dc2acfca98af70c2d1b1bc75190d/charset_normalizer-3.4.1-cp312-cp312-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:2369eea1ee4a7610a860d88f268eb39b95cb588acd7235e02fd5a5601773d4fa", size = 143184 },
    { url = "https://files.pythonhosted.org/packages/3e/a2/513f6cbe752421f16d969e32f3583762bfd583848b763913ddab8d9bfd4f/charset_normalizer-3.4.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:bc2722592d8998c870fa4e290c2eec2c1569b87fe58618e67d38b4665dfa680d", size = 145268 },
    { url = "https://files.pythonhosted.org/packages/74/94/8a5277664f27c3c438546f3eb53b33f5b19568eb7424736bdc440a88a31f/charset_normalizer-3.4.1-cp312-cp312-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:ffc9202a29ab3920fa812879e95a9e78b2465fd10be7fcbd042899695d75e616", size = 147601 },
    { url = "https://files.pythonhosted.org/packages/7c/5f/6d352c51ee763623a98e31194823518e09bfa48be2a7e8383cf691bbb3d0/charset_normalizer-3.4.1-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:804a4d582ba6e5b747c625bf1255e6b1507465494a40a2130978bda7b932c90b", size = 141098 },
    { url = "https://files.pythonhosted.org/packages/78/d4/f5704cb629ba5ab16d1d3d741396aec6dc3ca2b67757c45b0599bb010478/charset_normalizer-3.4.1-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:0f55e69f030f7163dffe9fd0752b32f070566451afe180f99dbeeb81f511ad8d", size = 149520 },
    { url = "https://files.pythonhosted.org/packages/c5/96/64120b1d02b81785f222b976c0fb79a35875457fa9bb40827678e54d1bc8/charset_normalizer-3.4.1-cp312-cp312-musllinux_1_2_ppc64le.whl", hash = "sha256:c4c3e6da02df6fa1410a7680bd3f63d4f710232d3139089536310d027950696a", size = 152852 },
    { url = "https://files.pythonhosted.org/packages/84/c9/98e3732278a99f47d487fd3468bc60b882920cef29d1fa6ca460a1fdf4e6/charset_normalizer-3.4.1-cp312-cp312-musllinux_1_2_s390x.whl", hash = "sha256:5df196eb874dae23dcfb968c83d4f8fdccb333330fe1fc278ac5ceeb101003a9", size = 150488 },
    { url = "https://files.pythonhosted.org/packages/13/0e/9c8d4cb99c98c1007cc11eda969ebfe837bbbd0acdb4736d228ccaabcd22/charset_normalizer-3.4.1-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:e358e64305fe12299a08e08978f51fc21fac060dcfcddd95453eabe5b93ed0e1", size = 146192 },
    { url = "https://files.pythonhosted.org/packages/b2/21/2b6b5b860781a0b49427309cb8670785aa543fb2178de875b87b9cc97746/charset_normalizer-3.4.1-cp312-cp312-win32.whl", hash = "sha256:9b23ca7ef998bc739bf6ffc077c2116917eabcc901f88da1b9856b210ef63f35", size = 95550 },
    { url = "https://files.pythonhosted.org/packages/21/5b/1b390b03b1d16c7e382b561c5329f83cc06623916aab983e8ab9239c7d5c/charset_normalizer-3.4.1-cp312-cp312-win_amd64.whl", hash = "sha256:6ff8a4a60c227ad87030d76e99cd1698345d4491638dfa6673027c48b3cd395f", size = 102785 },
    { url = "https://files.pythonhosted.org/packages/38/94/ce8e6f63d18049672c76d07d119304e1e2d7c6098f0841b51c666e9f44a0/charset_normalizer-3.4.1-cp313-cp313-macosx_10_13_universal2.whl", hash = "sha256:aabfa34badd18f1da5ec1bc2715cadc8dca465868a4e73a0173466b688f29dda", size = 195698 },
    { url = "https://files.pythonhosted.org/packages/24/2e/dfdd9770664aae179a96561cc6952ff08f9a8cd09a908f259a9dfa063568/charset_normalizer-3.4.1-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:22e14b5d70560b8dd51ec22863f370d1e595ac3d024cb8ad7d308b4cd95f8313", size = 140162 },
    { url = "https://files.pythonhosted.org/packages/24/4e/f646b9093cff8fc86f2d60af2de4dc17c759de9d554f130b140ea4738ca6/charset_normalizer-3.4.1-cp313-cp313-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:8436c508b408b82d87dc5f62496973a1805cd46727c34440b0d29d8a2f50a6c9", size = 150263 },
    { url = "https://files.pythonhosted.org/packages/5e/67/2937f8d548c3ef6e2f9aab0f6e21001056f692d43282b165e7c56023e6dd/charset_normalizer-3.4.1-cp313-cp313-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:2d074908e1aecee37a7635990b2c6d504cd4766c7bc9fc86d63f9c09af3fa11b", size = 142966 },
    { url = "https://files.pythonhosted.org/packages/52/ed/b7f4f07de100bdb95c1756d3a4d17b90c1a3c53715c1a476f8738058e0fa/charset_normalizer-3.4.1-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:955f8851919303c92343d2f66165294848d57e9bba6cf6e3625485a70a038d11", size = 144992 },
    { url = "https://files.pythonhosted.org/packages/96/2c/d49710a6dbcd3776265f4c923bb73ebe83933dfbaa841c5da850fe0fd20b/charset_normalizer-3.4.1-cp313-cp313-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:44ecbf16649486d4aebafeaa7ec4c9fed8b88101f4dd612dcaf65d5e815f837f", size = 147162 },
    { url = "https://files.pythonhosted.org/packages/b4/41/35ff1f9a6bd380303dea55e44c4933b4cc3c4850988927d4082ada230273/charset_normalizer-3.4.1-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:0924e81d3d5e70f8126529951dac65c1010cdf117bb75eb02dd12339b57749dd", size = 140972 },
    { url = "https://files.pythonhosted.org/packages/fb/43/c6a0b685fe6910d08ba971f62cd9c3e862a85770395ba5d9cad4fede33ab/charset_normalizer-3.4.1-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:2967f74ad52c3b98de4c3b32e1a44e32975e008a9cd2a8cc8966d6a5218c5cb2", size = 149095 },
    { url = "https://files.pythonhosted.org/packages/4c/ff/a9a504662452e2d2878512115638966e75633519ec11f25fca3d2049a94a/charset_normalizer-3.4.1-cp313-cp313-musllinux_1_2_ppc64le.whl", hash = "sha256:c75cb2a3e389853835e84a2d8fb2b81a10645b503eca9bcb98df6b5a43eb8886", size = 152668 },
    { url = "https://files.pythonhosted.org/packages/6c/71/189996b6d9a4b932564701628af5cee6716733e9165af1d5e1b285c530ed/charset_normalizer-3.4.1-cp313-cp313-musllinux_1_2_s390x.whl", hash = "sha256:09b26ae6b1abf0d27570633b2b078a2a20419c99d66fb2823173d73f188ce601", size = 150073 },
    { url = "https://files.pythonhosted.org/packages/e4/93/946a86ce20790e11312c87c75ba68d5f6ad2208cfb52b2d6a2c32840d922/charset_normalizer-3.4.1-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:fa88b843d6e211393a37219e6a1c1df99d35e8fd90446f1118f4216e307e48cd", size = 145732 },
    { url = "https://files.pythonhosted.org/packages/cd/e5/131d2fb1b0dddafc37be4f3a2fa79aa4c037368be9423061dccadfd90091/charset_normalizer-3.4.1-cp313-cp313-win32.whl", hash = "sha256:eb8178fe3dba6450a3e024e95ac49ed3400e506fd4e9e5c32d30adda88cbd407", size = 95391 },
    { url = "https://files.pythonhosted.org/packages/27/f2/4f9a69cc7712b9b5ad8fdb87039fd89abba997ad5cbe690d1835d40405b0/charset_normalizer-3.4.1-cp313-cp313-win_amd64.whl", hash = "sha256:b1ac5992a838106edb89654e0aebfc24f5848ae2547d22c2c3f66454daa11971", size = 102702 },
    { url = "https://files.pythonhosted.org/packages/7f/c0/b913f8f02836ed9ab32ea643c6fe4d3325c3d8627cf6e78098671cafff86/charset_normalizer-3.4.1-cp39-cp39-macosx_10_9_universal2.whl", hash = "sha256:b97e690a2118911e39b4042088092771b4ae3fc3aa86518f84b8cf6888dbdb41", size = 197867 },
    { url = "https://files.pythonhosted.org/packages/0f/6c/2bee440303d705b6fb1e2ec789543edec83d32d258299b16eed28aad48e0/charset_normalizer-3.4.1-cp39-cp39-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:78baa6d91634dfb69ec52a463534bc0df05dbd546209b79a3880a34487f4b84f", size = 141385 },
    { url = "https://files.pythonhosted.org/packages/3d/04/cb42585f07f6f9fd3219ffb6f37d5a39b4fd2db2355b23683060029c35f7/charset_normalizer-3.4.1-cp39-cp39-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:1a2bc9f351a75ef49d664206d51f8e5ede9da246602dc2d2726837620ea034b2", size = 151367 },
    { url = "https://files.pythonhosted.org/packages/54/54/2412a5b093acb17f0222de007cc129ec0e0df198b5ad2ce5699355269dfe/charset_normalizer-3.4.1-cp39-cp39-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:75832c08354f595c760a804588b9357d34ec00ba1c940c15e31e96d902093770", size = 143928 },
    { url = "https://files.pythonhosted.org/packages/5a/6d/e2773862b043dcf8a221342954f375392bb2ce6487bcd9f2c1b34e1d6781/charset_normalizer-3.4.1-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:0af291f4fe114be0280cdd29d533696a77b5b49cfde5467176ecab32353395c4", size = 146203 },
    { url = "https://files.pythonhosted.org/packages/b9/f8/ca440ef60d8f8916022859885f231abb07ada3c347c03d63f283bec32ef5/charset_normalizer-3.4.1-cp39-cp39-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:0167ddc8ab6508fe81860a57dd472b2ef4060e8d378f0cc555707126830f2537", size = 148082 },
    { url = "https://files.pythonhosted.org/packages/04/d2/42fd330901aaa4b805a1097856c2edf5095e260a597f65def493f4b8c833/charset_normalizer-3.4.1-cp39-cp39-musllinux_1_2_aarch64.whl", hash = "sha256:2a75d49014d118e4198bcee5ee0a6f25856b29b12dbf7cd012791f8a6cc5c496", size = 142053 },
    { url = "https://files.pythonhosted.org/packages/9e/af/3a97a4fa3c53586f1910dadfc916e9c4f35eeada36de4108f5096cb7215f/charset_normalizer-3.4.1-cp39-cp39-musllinux_1_2_i686.whl", hash = "sha256:363e2f92b0f0174b2f8238240a1a30142e3db7b957a5dd5689b0e75fb717cc78", size = 150625 },
    { url = "https://files.pythonhosted.org/packages/26/ae/23d6041322a3556e4da139663d02fb1b3c59a23ab2e2b56432bd2ad63ded/charset_normalizer-3.4.1-cp39-cp39-musllinux_1_2_ppc64le.whl", hash = "sha256:ab36c8eb7e454e34e60eb55ca5d241a5d18b2c6244f6827a30e451c42410b5f7", size = 153549 },
    { url = "https://files.pythonhosted.org/packages/94/22/b8f2081c6a77cb20d97e57e0b385b481887aa08019d2459dc2858ed64871/charset_normalizer-3.4.1-cp39-cp39-musllinux_1_2_s390x.whl", hash = "sha256:4c0907b1928a36d5a998d72d64d8eaa7244989f7aaaf947500d3a800c83a3fd6", size = 150945 },
    { url = "https://files.pythonhosted.org/packages/c7/0b/c5ec5092747f801b8b093cdf5610e732b809d6cb11f4c51e35fc28d1d389/charset_normalizer-3.4.1-cp39-cp39-musllinux_1_2_x86_64.whl", hash = "sha256:04432ad9479fa40ec0f387795ddad4437a2b50417c69fa275e212933519ff294", size = 146595 },
    { url = "https://files.pythonhosted.org/packages/0c/5a/0b59704c38470df6768aa154cc87b1ac7c9bb687990a1559dc8765e8627e/charset_normalizer-3.4.1-cp39-cp39-win32.whl", hash = "sha256:3bed14e9c89dcb10e8f3a29f9ccac4955aebe93c71ae803af79265c9ca5644c5", size = 95453 },
    { url = "https://files.pythonhosted.org/packages/85/2d/a9790237cb4d01a6d57afadc8573c8b73c609ade20b80f4cda30802009ee/charset_normalizer-3.4.1-cp39-cp39-win_amd64.whl", hash = "sha256:49402233c892a461407c512a19435d1ce275543138294f7ef013f0b63d5d3765", size = 102811 },
    { url = "https://files.pythonhosted.org/packages/0e/f6/65ecc6878a89bb1c23a086ea335ad4bf21a588990c3f535a227b9eea9108/charset_normalizer-3.4.1-py3-none-any.whl", hash = "sha256:d98b1668f06378c6dbefec3b92299716b931cd4e6061f3c875a71ced1780ab85", size = 49767 },
]

[[package]]
name = "chonkie"
version = "1.0.0a1"
source = { editable = "." }
dependencies = [
    { name = "tokenizers" },
    { name = "tqdm" },
]

[package.optional-dependencies]
all = [
    { name = "accelerate" },
    { name = "cohere" },
    { name = "model2vec" },
    { name = "numpy" },
    { name = "openai" },
    { name = "sentence-transformers" },
    { name = "tiktoken" },
]
cohere = [
    { name = "cohere" },
    { name = "numpy" },
]
dev = [
    { name = "coverage" },
    { name = "datasets" },
    { name = "mypy" },
    { name = "pytest" },
    { name = "pytest-cov" },
    { name = "ruff" },
    { name = "tiktoken" },
    { name = "transformers" },
]
model2vec = [
    { name = "model2vec" },
    { name = "numpy" },
]
openai = [
    { name = "numpy" },
    { name = "openai" },
    { name = "tiktoken" },
]
semantic = [
    { name = "model2vec" },
    { name = "numpy" },
]
st = [
    { name = "accelerate" },
    { name = "numpy" },
    { name = "sentence-transformers" },
]

[package.metadata]
requires-dist = [
    { name = "accelerate", marker = "extra == 'all'", specifier = ">=1.6.0" },
    { name = "accelerate", marker = "extra == 'st'", specifier = ">=1.6.0" },
    { name = "cohere", marker = "extra == 'all'", specifier = ">=5.13.0" },
    { name = "cohere", marker = "extra == 'cohere'", specifier = ">=5.13.0" },
    { name = "coverage", marker = "extra == 'dev'" },
    { name = "datasets", marker = "extra == 'dev'", specifier = ">=1.14.0" },
    { name = "model2vec", marker = "extra == 'all'", specifier = ">=0.3.0" },
    { name = "model2vec", marker = "extra == 'model2vec'", specifier = ">=0.3.0" },
    { name = "model2vec", marker = "extra == 'semantic'", specifier = ">=0.3.0" },
    { name = "mypy", marker = "extra == 'dev'", specifier = ">=1.11.0" },
    { name = "numpy", marker = "extra == 'all'", specifier = ">=2.0.0,<3.0" },
    { name = "numpy", marker = "extra == 'cohere'", specifier = ">=2.0.0,<3.0" },
    { name = "numpy", marker = "extra == 'model2vec'", specifier = ">=2.0.0,<3.0" },
    { name = "numpy", marker = "extra == 'openai'", specifier = ">=2.0.0,<3.0" },
    { name = "numpy", marker = "extra == 'semantic'", specifier = ">=2.0.0,<3.0" },
    { name = "numpy", marker = "extra == 'st'", specifier = ">=2.0.0,<3.0" },
    { name = "openai", marker = "extra == 'all'", specifier = ">=1.0.0" },
    { name = "openai", marker = "extra == 'openai'", specifier = ">=1.0.0" },
    { name = "pytest", marker = "extra == 'dev'", specifier = ">=6.2.0" },
    { name = "pytest-cov", marker = "extra == 'dev'", specifier = ">=4.0.0" },
    { name = "ruff", marker = "extra == 'dev'", specifier = ">=0.0.265" },
    { name = "sentence-transformers", marker = "extra == 'all'", specifier = ">=3.0.0" },
    { name = "sentence-transformers", marker = "extra == 'st'", specifier = ">=3.0.0" },
    { name = "tiktoken", marker = "extra == 'all'", specifier = ">=0.5.0" },
    { name = "tiktoken", marker = "extra == 'dev'", specifier = ">=0.5.0" },
    { name = "tiktoken", marker = "extra == 'openai'", specifier = ">=0.5.0" },
    { name = "tokenizers", specifier = ">=0.16.0" },
    { name = "tqdm", specifier = ">=4.64.0" },
    { name = "transformers", marker = "extra == 'dev'", specifier = ">=4.0.0" },
]

[[package]]
name = "cohere"
version = "5.14.2"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "fastavro" },
    { name = "httpx" },
    { name = "httpx-sse" },
    { name = "pydantic" },
    { name = "pydantic-core" },
    { name = "requests" },
    { name = "tokenizers" },
    { name = "types-requests" },
    { name = "typing-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/c3/80/3943edee51d24c6cac2ef269f1363dfd6e8f3d45e2661fcf40b67d6c4292/cohere-5.14.2.tar.gz", hash = "sha256:5aaf5a70e619ade2bb991b12f573fd4cc9bd1f3097f0f67acd973d060a7e86c6", size = 134626 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/a0/f3/2b11b4ea8c2e91e3b6fd965e80c123e469d7cae037d2afbb6534efe75180/cohere-5.14.2-py3-none-any.whl", hash = "sha256:fe2cbbf6c79fba21a66731d387647b981ab5ea6dbcfb09beb85386e96695bd64", size = 259249 },
]

[[package]]
name = "colorama"
version = "0.4.6"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/d8/53/6f443c9a4a8358a93a6792e2acffb9d9d5cb0a5cfd8802644b7b1c9a02e4/colorama-0.4.6.tar.gz", hash = "sha256:08695f5cb7ed6e0531a20572697297273c47b8cae5a63ffc6d6ed5c201be6e44", size = 27697 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/d1/d6/3965ed04c63042e047cb6a3e6ed1a63a35087b6a609aa3a15ed8ac56c221/colorama-0.4.6-py2.py3-none-any.whl", hash = "sha256:4f1d9991f5acc0ca119f9d443620b77f9d6b33703e51011c16baf57afb285fc6", size = 25335 },
]

[[package]]
name = "coverage"
version = "7.8.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/19/4f/2251e65033ed2ce1e68f00f91a0294e0f80c80ae8c3ebbe2f12828c4cd53/coverage-7.8.0.tar.gz", hash = "sha256:7a3d62b3b03b4b6fd41a085f3574874cf946cb4604d2b4d3e8dca8cd570ca501", size = 811872 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/78/01/1c5e6ee4ebaaa5e079db933a9a45f61172048c7efa06648445821a201084/coverage-7.8.0-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:2931f66991175369859b5fd58529cd4b73582461877ecfd859b6549869287ffe", size = 211379 },
    { url = "https://files.pythonhosted.org/packages/e9/16/a463389f5ff916963471f7c13585e5f38c6814607306b3cb4d6b4cf13384/coverage-7.8.0-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:52a523153c568d2c0ef8826f6cc23031dc86cffb8c6aeab92c4ff776e7951b28", size = 211814 },
    { url = "https://files.pythonhosted.org/packages/b8/b1/77062b0393f54d79064dfb72d2da402657d7c569cfbc724d56ac0f9c67ed/coverage-7.8.0-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:5c8a5c139aae4c35cbd7cadca1df02ea8cf28a911534fc1b0456acb0b14234f3", size = 240937 },
    { url = "https://files.pythonhosted.org/packages/d7/54/c7b00a23150083c124e908c352db03bcd33375494a4beb0c6d79b35448b9/coverage-7.8.0-cp310-cp310-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:5a26c0c795c3e0b63ec7da6efded5f0bc856d7c0b24b2ac84b4d1d7bc578d676", size = 238849 },
    { url = "https://files.pythonhosted.org/packages/f7/ec/a6b7cfebd34e7b49f844788fda94713035372b5200c23088e3bbafb30970/coverage-7.8.0-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:821f7bcbaa84318287115d54becb1915eece6918136c6f91045bb84e2f88739d", size = 239986 },
    { url = "https://files.pythonhosted.org/packages/21/8c/c965ecef8af54e6d9b11bfbba85d4f6a319399f5f724798498387f3209eb/coverage-7.8.0-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:a321c61477ff8ee705b8a5fed370b5710c56b3a52d17b983d9215861e37b642a", size = 239896 },
    { url = "https://files.pythonhosted.org/packages/40/83/070550273fb4c480efa8381735969cb403fa8fd1626d74865bfaf9e4d903/coverage-7.8.0-cp310-cp310-musllinux_1_2_i686.whl", hash = "sha256:ed2144b8a78f9d94d9515963ed273d620e07846acd5d4b0a642d4849e8d91a0c", size = 238613 },
    { url = "https://files.pythonhosted.org/packages/07/76/fbb2540495b01d996d38e9f8897b861afed356be01160ab4e25471f4fed1/coverage-7.8.0-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:042e7841a26498fff7a37d6fda770d17519982f5b7d8bf5278d140b67b61095f", size = 238909 },
    { url = "https://files.pythonhosted.org/packages/a3/7e/76d604db640b7d4a86e5dd730b73e96e12a8185f22b5d0799025121f4dcb/coverage-7.8.0-cp310-cp310-win32.whl", hash = "sha256:f9983d01d7705b2d1f7a95e10bbe4091fabc03a46881a256c2787637b087003f", size = 213948 },
    { url = "https://files.pythonhosted.org/packages/5c/a7/f8ce4aafb4a12ab475b56c76a71a40f427740cf496c14e943ade72e25023/coverage-7.8.0-cp310-cp310-win_amd64.whl", hash = "sha256:5a570cd9bd20b85d1a0d7b009aaf6c110b52b5755c17be6962f8ccd65d1dbd23", size = 214844 },
    { url = "https://files.pythonhosted.org/packages/2b/77/074d201adb8383addae5784cb8e2dac60bb62bfdf28b2b10f3a3af2fda47/coverage-7.8.0-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:e7ac22a0bb2c7c49f441f7a6d46c9c80d96e56f5a8bc6972529ed43c8b694e27", size = 211493 },
    { url = "https://files.pythonhosted.org/packages/a9/89/7a8efe585750fe59b48d09f871f0e0c028a7b10722b2172dfe021fa2fdd4/coverage-7.8.0-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:bf13d564d310c156d1c8e53877baf2993fb3073b2fc9f69790ca6a732eb4bfea", size = 211921 },
    { url = "https://files.pythonhosted.org/packages/e9/ef/96a90c31d08a3f40c49dbe897df4f1fd51fb6583821a1a1c5ee30cc8f680/coverage-7.8.0-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:a5761c70c017c1b0d21b0815a920ffb94a670c8d5d409d9b38857874c21f70d7", size = 244556 },
    { url = "https://files.pythonhosted.org/packages/89/97/dcd5c2ce72cee9d7b0ee8c89162c24972fb987a111b92d1a3d1d19100c61/coverage-7.8.0-cp311-cp311-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:e5ff52d790c7e1628241ffbcaeb33e07d14b007b6eb00a19320c7b8a7024c040", size = 242245 },
    { url = "https://files.pythonhosted.org/packages/b2/7b/b63cbb44096141ed435843bbb251558c8e05cc835c8da31ca6ffb26d44c0/coverage-7.8.0-cp311-cp311-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:d39fc4817fd67b3915256af5dda75fd4ee10621a3d484524487e33416c6f3543", size = 244032 },
    { url = "https://files.pythonhosted.org/packages/97/e3/7fa8c2c00a1ef530c2a42fa5df25a6971391f92739d83d67a4ee6dcf7a02/coverage-7.8.0-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:b44674870709017e4b4036e3d0d6c17f06a0e6d4436422e0ad29b882c40697d2", size = 243679 },
    { url = "https://files.pythonhosted.org/packages/4f/b3/e0a59d8df9150c8a0c0841d55d6568f0a9195692136c44f3d21f1842c8f6/coverage-7.8.0-cp311-cp311-musllinux_1_2_i686.whl", hash = "sha256:8f99eb72bf27cbb167b636eb1726f590c00e1ad375002230607a844d9e9a2318", size = 241852 },
    { url = "https://files.pythonhosted.org/packages/9b/82/db347ccd57bcef150c173df2ade97976a8367a3be7160e303e43dd0c795f/coverage-7.8.0-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:b571bf5341ba8c6bc02e0baeaf3b061ab993bf372d982ae509807e7f112554e9", size = 242389 },
    { url = "https://files.pythonhosted.org/packages/21/f6/3f7d7879ceb03923195d9ff294456241ed05815281f5254bc16ef71d6a20/coverage-7.8.0-cp311-cp311-win32.whl", hash = "sha256:e75a2ad7b647fd8046d58c3132d7eaf31b12d8a53c0e4b21fa9c4d23d6ee6d3c", size = 213997 },
    { url = "https://files.pythonhosted.org/packages/28/87/021189643e18ecf045dbe1e2071b2747901f229df302de01c998eeadf146/coverage-7.8.0-cp311-cp311-win_amd64.whl", hash = "sha256:3043ba1c88b2139126fc72cb48574b90e2e0546d4c78b5299317f61b7f718b78", size = 214911 },
    { url = "https://files.pythonhosted.org/packages/aa/12/4792669473297f7973518bec373a955e267deb4339286f882439b8535b39/coverage-7.8.0-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:bbb5cc845a0292e0c520656d19d7ce40e18d0e19b22cb3e0409135a575bf79fc", size = 211684 },
    { url = "https://files.pythonhosted.org/packages/be/e1/2a4ec273894000ebedd789e8f2fc3813fcaf486074f87fd1c5b2cb1c0a2b/coverage-7.8.0-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:4dfd9a93db9e78666d178d4f08a5408aa3f2474ad4d0e0378ed5f2ef71640cb6", size = 211935 },
    { url = "https://files.pythonhosted.org/packages/f8/3a/7b14f6e4372786709a361729164125f6b7caf4024ce02e596c4a69bccb89/coverage-7.8.0-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:f017a61399f13aa6d1039f75cd467be388d157cd81f1a119b9d9a68ba6f2830d", size = 245994 },
    { url = "https://files.pythonhosted.org/packages/54/80/039cc7f1f81dcbd01ea796d36d3797e60c106077e31fd1f526b85337d6a1/coverage-7.8.0-cp312-cp312-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:0915742f4c82208ebf47a2b154a5334155ed9ef9fe6190674b8a46c2fb89cb05", size = 242885 },
    { url = "https://files.pythonhosted.org/packages/10/e0/dc8355f992b6cc2f9dcd5ef6242b62a3f73264893bc09fbb08bfcab18eb4/coverage-7.8.0-cp312-cp312-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:8a40fcf208e021eb14b0fac6bdb045c0e0cab53105f93ba0d03fd934c956143a", size = 245142 },
    { url = "https://files.pythonhosted.org/packages/43/1b/33e313b22cf50f652becb94c6e7dae25d8f02e52e44db37a82de9ac357e8/coverage-7.8.0-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:a1f406a8e0995d654b2ad87c62caf6befa767885301f3b8f6f73e6f3c31ec3a6", size = 244906 },
    { url = "https://files.pythonhosted.org/packages/05/08/c0a8048e942e7f918764ccc99503e2bccffba1c42568693ce6955860365e/coverage-7.8.0-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:77af0f6447a582fdc7de5e06fa3757a3ef87769fbb0fdbdeba78c23049140a47", size = 243124 },
    { url = "https://files.pythonhosted.org/packages/5b/62/ea625b30623083c2aad645c9a6288ad9fc83d570f9adb913a2abdba562dd/coverage-7.8.0-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:f2d32f95922927186c6dbc8bc60df0d186b6edb828d299ab10898ef3f40052fe", size = 244317 },
    { url = "https://files.pythonhosted.org/packages/62/cb/3871f13ee1130a6c8f020e2f71d9ed269e1e2124aa3374d2180ee451cee9/coverage-7.8.0-cp312-cp312-win32.whl", hash = "sha256:769773614e676f9d8e8a0980dd7740f09a6ea386d0f383db6821df07d0f08545", size = 214170 },
    { url = "https://files.pythonhosted.org/packages/88/26/69fe1193ab0bfa1eb7a7c0149a066123611baba029ebb448500abd8143f9/coverage-7.8.0-cp312-cp312-win_amd64.whl", hash = "sha256:e5d2b9be5b0693cf21eb4ce0ec8d211efb43966f6657807f6859aab3814f946b", size = 214969 },
    { url = "https://files.pythonhosted.org/packages/f3/21/87e9b97b568e223f3438d93072479c2f36cc9b3f6b9f7094b9d50232acc0/coverage-7.8.0-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:5ac46d0c2dd5820ce93943a501ac5f6548ea81594777ca585bf002aa8854cacd", size = 211708 },
    { url = "https://files.pythonhosted.org/packages/75/be/882d08b28a0d19c9c4c2e8a1c6ebe1f79c9c839eb46d4fca3bd3b34562b9/coverage-7.8.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:771eb7587a0563ca5bb6f622b9ed7f9d07bd08900f7589b4febff05f469bea00", size = 211981 },
    { url = "https://files.pythonhosted.org/packages/7a/1d/ce99612ebd58082fbe3f8c66f6d8d5694976c76a0d474503fa70633ec77f/coverage-7.8.0-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:42421e04069fb2cbcbca5a696c4050b84a43b05392679d4068acbe65449b5c64", size = 245495 },
    { url = "https://files.pythonhosted.org/packages/dc/8d/6115abe97df98db6b2bd76aae395fcc941d039a7acd25f741312ced9a78f/coverage-7.8.0-cp313-cp313-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:554fec1199d93ab30adaa751db68acec2b41c5602ac944bb19187cb9a41a8067", size = 242538 },
    { url = "https://files.pythonhosted.org/packages/cb/74/2f8cc196643b15bc096d60e073691dadb3dca48418f08bc78dd6e899383e/coverage-7.8.0-cp313-cp313-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:5aaeb00761f985007b38cf463b1d160a14a22c34eb3f6a39d9ad6fc27cb73008", size = 244561 },
    { url = "https://files.pythonhosted.org/packages/22/70/c10c77cd77970ac965734fe3419f2c98665f6e982744a9bfb0e749d298f4/coverage-7.8.0-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:581a40c7b94921fffd6457ffe532259813fc68eb2bdda60fa8cc343414ce3733", size = 244633 },
    { url = "https://files.pythonhosted.org/packages/38/5a/4f7569d946a07c952688debee18c2bb9ab24f88027e3d71fd25dbc2f9dca/coverage-7.8.0-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:f319bae0321bc838e205bf9e5bc28f0a3165f30c203b610f17ab5552cff90323", size = 242712 },
    { url = "https://files.pythonhosted.org/packages/bb/a1/03a43b33f50475a632a91ea8c127f7e35e53786dbe6781c25f19fd5a65f8/coverage-7.8.0-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:04bfec25a8ef1c5f41f5e7e5c842f6b615599ca8ba8391ec33a9290d9d2db3a3", size = 244000 },
    { url = "https://files.pythonhosted.org/packages/6a/89/ab6c43b1788a3128e4d1b7b54214548dcad75a621f9d277b14d16a80d8a1/coverage-7.8.0-cp313-cp313-win32.whl", hash = "sha256:dd19608788b50eed889e13a5d71d832edc34fc9dfce606f66e8f9f917eef910d", size = 214195 },
    { url = "https://files.pythonhosted.org/packages/12/12/6bf5f9a8b063d116bac536a7fb594fc35cb04981654cccb4bbfea5dcdfa0/coverage-7.8.0-cp313-cp313-win_amd64.whl", hash = "sha256:a9abbccd778d98e9c7e85038e35e91e67f5b520776781d9a1e2ee9d400869487", size = 214998 },
    { url = "https://files.pythonhosted.org/packages/2a/e6/1e9df74ef7a1c983a9c7443dac8aac37a46f1939ae3499424622e72a6f78/coverage-7.8.0-cp313-cp313t-macosx_10_13_x86_64.whl", hash = "sha256:18c5ae6d061ad5b3e7eef4363fb27a0576012a7447af48be6c75b88494c6cf25", size = 212541 },
    { url = "https://files.pythonhosted.org/packages/04/51/c32174edb7ee49744e2e81c4b1414ac9df3dacfcb5b5f273b7f285ad43f6/coverage-7.8.0-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:95aa6ae391a22bbbce1b77ddac846c98c5473de0372ba5c463480043a07bff42", size = 212767 },
    { url = "https://files.pythonhosted.org/packages/e9/8f/f454cbdb5212f13f29d4a7983db69169f1937e869a5142bce983ded52162/coverage-7.8.0-cp313-cp313t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:e013b07ba1c748dacc2a80e69a46286ff145935f260eb8c72df7185bf048f502", size = 256997 },
    { url = "https://files.pythonhosted.org/packages/e6/74/2bf9e78b321216d6ee90a81e5c22f912fc428442c830c4077b4a071db66f/coverage-7.8.0-cp313-cp313t-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:d766a4f0e5aa1ba056ec3496243150698dc0481902e2b8559314368717be82b1", size = 252708 },
    { url = "https://files.pythonhosted.org/packages/92/4d/50d7eb1e9a6062bee6e2f92e78b0998848a972e9afad349b6cdde6fa9e32/coverage-7.8.0-cp313-cp313t-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:ad80e6b4a0c3cb6f10f29ae4c60e991f424e6b14219d46f1e7d442b938ee68a4", size = 255046 },
    { url = "https://files.pythonhosted.org/packages/40/9e/71fb4e7402a07c4198ab44fc564d09d7d0ffca46a9fb7b0a7b929e7641bd/coverage-7.8.0-cp313-cp313t-musllinux_1_2_aarch64.whl", hash = "sha256:b87eb6fc9e1bb8f98892a2458781348fa37e6925f35bb6ceb9d4afd54ba36c73", size = 256139 },
    { url = "https://files.pythonhosted.org/packages/49/1a/78d37f7a42b5beff027e807c2843185961fdae7fe23aad5a4837c93f9d25/coverage-7.8.0-cp313-cp313t-musllinux_1_2_i686.whl", hash = "sha256:d1ba00ae33be84066cfbe7361d4e04dec78445b2b88bdb734d0d1cbab916025a", size = 254307 },
    { url = "https://files.pythonhosted.org/packages/58/e9/8fb8e0ff6bef5e170ee19d59ca694f9001b2ec085dc99b4f65c128bb3f9a/coverage-7.8.0-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:f3c38e4e5ccbdc9198aecc766cedbb134b2d89bf64533973678dfcf07effd883", size = 255116 },
    { url = "https://files.pythonhosted.org/packages/56/b0/d968ecdbe6fe0a863de7169bbe9e8a476868959f3af24981f6a10d2b6924/coverage-7.8.0-cp313-cp313t-win32.whl", hash = "sha256:379fe315e206b14e21db5240f89dc0774bdd3e25c3c58c2c733c99eca96f1ada", size = 214909 },
    { url = "https://files.pythonhosted.org/packages/87/e9/d6b7ef9fecf42dfb418d93544af47c940aa83056c49e6021a564aafbc91f/coverage-7.8.0-cp313-cp313t-win_amd64.whl", hash = "sha256:2e4b6b87bb0c846a9315e3ab4be2d52fac905100565f4b92f02c445c8799e257", size = 216068 },
    { url = "https://files.pythonhosted.org/packages/60/0c/5da94be095239814bf2730a28cffbc48d6df4304e044f80d39e1ae581997/coverage-7.8.0-cp39-cp39-macosx_10_9_x86_64.whl", hash = "sha256:fa260de59dfb143af06dcf30c2be0b200bed2a73737a8a59248fcb9fa601ef0f", size = 211377 },
    { url = "https://files.pythonhosted.org/packages/d5/cb/b9e93ebf193a0bb89dbcd4f73d7b0e6ecb7c1b6c016671950e25f041835e/coverage-7.8.0-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:96121edfa4c2dfdda409877ea8608dd01de816a4dc4a0523356067b305e4e17a", size = 211803 },
    { url = "https://files.pythonhosted.org/packages/78/1a/cdbfe9e1bb14d3afcaf6bb6e1b9ba76c72666e329cd06865bbd241efd652/coverage-7.8.0-cp39-cp39-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:6b8af63b9afa1031c0ef05b217faa598f3069148eeee6bb24b79da9012423b82", size = 240561 },
    { url = "https://files.pythonhosted.org/packages/59/04/57f1223f26ac018d7ce791bfa65b0c29282de3e041c1cd3ed430cfeac5a5/coverage-7.8.0-cp39-cp39-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:89b1f4af0d4afe495cd4787a68e00f30f1d15939f550e869de90a86efa7e0814", size = 238488 },
    { url = "https://files.pythonhosted.org/packages/b7/b1/0f25516ae2a35e265868670384feebe64e7857d9cffeeb3887b0197e2ba2/coverage-7.8.0-cp39-cp39-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:94ec0be97723ae72d63d3aa41961a0b9a6f5a53ff599813c324548d18e3b9e8c", size = 239589 },
    { url = "https://files.pythonhosted.org/packages/e0/a4/99d88baac0d1d5a46ceef2dd687aac08fffa8795e4c3e71b6f6c78e14482/coverage-7.8.0-cp39-cp39-musllinux_1_2_aarch64.whl", hash = "sha256:8a1d96e780bdb2d0cbb297325711701f7c0b6f89199a57f2049e90064c29f6bd", size = 239366 },
    { url = "https://files.pythonhosted.org/packages/ea/9e/1db89e135feb827a868ed15f8fc857160757f9cab140ffee21342c783ceb/coverage-7.8.0-cp39-cp39-musllinux_1_2_i686.whl", hash = "sha256:f1d8a2a57b47142b10374902777e798784abf400a004b14f1b0b9eaf1e528ba4", size = 237591 },
    { url = "https://files.pythonhosted.org/packages/1b/6d/ac4d6fdfd0e201bc82d1b08adfacb1e34b40d21a22cdd62cfaf3c1828566/coverage-7.8.0-cp39-cp39-musllinux_1_2_x86_64.whl", hash = "sha256:cf60dd2696b457b710dd40bf17ad269d5f5457b96442f7f85722bdb16fa6c899", size = 238572 },
    { url = "https://files.pythonhosted.org/packages/25/5e/917cbe617c230f7f1745b6a13e780a3a1cd1cf328dbcd0fd8d7ec52858cd/coverage-7.8.0-cp39-cp39-win32.whl", hash = "sha256:be945402e03de47ba1872cd5236395e0f4ad635526185a930735f66710e1bd3f", size = 213966 },
    { url = "https://files.pythonhosted.org/packages/bd/93/72b434fe550135869f9ea88dd36068af19afce666db576e059e75177e813/coverage-7.8.0-cp39-cp39-win_amd64.whl", hash = "sha256:90e7fbc6216ecaffa5a880cdc9c77b7418c1dcb166166b78dbc630d07f278cc3", size = 214852 },
    { url = "https://files.pythonhosted.org/packages/c4/f1/1da77bb4c920aa30e82fa9b6ea065da3467977c2e5e032e38e66f1c57ffd/coverage-7.8.0-pp39.pp310.pp311-none-any.whl", hash = "sha256:b8194fb8e50d556d5849753de991d390c5a1edeeba50f68e3a9253fbd8bf8ccd", size = 203443 },
    { url = "https://files.pythonhosted.org/packages/59/f1/4da7717f0063a222db253e7121bd6a56f6fb1ba439dcc36659088793347c/coverage-7.8.0-py3-none-any.whl", hash = "sha256:dbf364b4c5e7bae9250528167dfe40219b62e2d573c854d74be213e1e52069f7", size = 203435 },
]

[package.optional-dependencies]
toml = [
    { name = "tomli", marker = "python_full_version <= '3.11'" },
]

[[package]]
name = "datasets"
version = "3.5.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "aiohttp" },
    { name = "dill" },
    { name = "filelock" },
    { name = "fsspec", extra = ["http"] },
    { name = "huggingface-hub" },
    { name = "multiprocess" },
    { name = "numpy" },
    { name = "packaging" },
    { name = "pandas" },
    { name = "pyarrow" },
    { name = "pyyaml" },
    { name = "requests" },
    { name = "tqdm" },
    { name = "xxhash" },
]
sdist = { url = "https://files.pythonhosted.org/packages/73/dd/6afb1d440a21da104adefb93269a02058bf9f3cf665db6421fe04eceab7d/datasets-3.5.0.tar.gz", hash = "sha256:9e39560e34f83a64e48ceca7adeb645ede3c3055c5cf48ed2b454f8ed2b89754", size = 568325 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/b4/83/50abe521eb75744a01efe2ebe836a4b61f4df37941a776f650f291aabdf9/datasets-3.5.0-py3-none-any.whl", hash = "sha256:b3b7f163acc6ac4e01a1b00eef26d48bd4039288ceea3601d169272bd5581006", size = 491167 },
]

[[package]]
name = "dill"
version = "0.3.8"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/17/4d/ac7ffa80c69ea1df30a8aa11b3578692a5118e7cd1aa157e3ef73b092d15/dill-0.3.8.tar.gz", hash = "sha256:3ebe3c479ad625c4553aca177444d89b486b1d84982eeacded644afc0cf797ca", size = 184847 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/c9/7a/cef76fd8438a42f96db64ddaa85280485a9c395e7df3db8158cfec1eee34/dill-0.3.8-py3-none-any.whl", hash = "sha256:c36ca9ffb54365bdd2f8eb3eff7d2a21237f8452b57ace88b1ac615b7e815bd7", size = 116252 },
]

[[package]]
name = "distro"
version = "1.9.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/fc/f8/98eea607f65de6527f8a2e8885fc8015d3e6f5775df186e443e0964a11c3/distro-1.9.0.tar.gz", hash = "sha256:2fa77c6fd8940f116ee1d6b94a2f90b13b5ea8d019b98bc8bafdcabcdd9bdbed", size = 60722 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/12/b3/231ffd4ab1fc9d679809f356cebee130ac7daa00d6d6f3206dd4fd137e9e/distro-1.9.0-py3-none-any.whl", hash = "sha256:7bffd925d65168f85027d8da9af6bddab658135b840670a223589bc0c8ef02b2", size = 20277 },
]

[[package]]
name = "exceptiongroup"
version = "1.2.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/09/35/2495c4ac46b980e4ca1f6ad6db102322ef3ad2410b79fdde159a4b0f3b92/exceptiongroup-1.2.2.tar.gz", hash = "sha256:47c2edf7c6738fafb49fd34290706d1a1a2f4d1c6df275526b62cbb4aa5393cc", size = 28883 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/02/cc/b7e31358aac6ed1ef2bb790a9746ac2c69bcb3c8588b41616914eb106eaf/exceptiongroup-1.2.2-py3-none-any.whl", hash = "sha256:3111b9d131c238bec2f8f516e123e14ba243563fb135d3fe885990585aa7795b", size = 16453 },
]

[[package]]
name = "fastavro"
version = "1.10.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/f3/67/7121d2221e998706cac00fa779ec44c1c943cb65e8a7ed1bd57d78d93f2c/fastavro-1.10.0.tar.gz", hash = "sha256:47bf41ac6d52cdfe4a3da88c75a802321321b37b663a900d12765101a5d6886f", size = 987970 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/0c/e9/f5813450d672f500c4794a39a7cfea99316cb63d5ea11f215e320ea5243b/fastavro-1.10.0-cp310-cp310-macosx_10_9_universal2.whl", hash = "sha256:1a9fe0672d2caf0fe54e3be659b13de3cad25a267f2073d6f4b9f8862acc31eb", size = 1037355 },
    { url = "https://files.pythonhosted.org/packages/6a/41/3f120f72e65f0c80e9bc4f855ac1c9578c8c0e2cdac4d4d4da1f91ca73b9/fastavro-1.10.0-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:86dd0410770e0c99363788f0584523709d85e57bb457372ec5c285a482c17fe6", size = 3024739 },
    { url = "https://files.pythonhosted.org/packages/e1/e3/7d9b019158498b45c383e696ba8733b01535337136e9402b0487afeb92b6/fastavro-1.10.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:190e80dc7d77d03a6a8597a026146b32a0bbe45e3487ab4904dc8c1bebecb26d", size = 3074020 },
    { url = "https://files.pythonhosted.org/packages/36/31/7ede5629e66eeb71c234d17a799000e737fe0ffd71ef9e1d57a3510def46/fastavro-1.10.0-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:bf570d63be9155c3fdc415f60a49c171548334b70fff0679a184b69c29b6bc61", size = 2968623 },
    { url = "https://files.pythonhosted.org/packages/10/13/d215411ff5d5de23d6ed62a31eb7f7fa53941681d86bcd5c6388a0918fc3/fastavro-1.10.0-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:e07abb6798e95dccecaec316265e35a018b523d1f3944ad396d0a93cb95e0a08", size = 3122217 },
    { url = "https://files.pythonhosted.org/packages/6a/1d/7a54fac3f90f0dc120b92f244067976831e393789d3b78c08f2b035ccb19/fastavro-1.10.0-cp310-cp310-win_amd64.whl", hash = "sha256:37203097ed11d0b8fd3c004904748777d730cafd26e278167ea602eebdef8eb2", size = 497256 },
    { url = "https://files.pythonhosted.org/packages/ac/bf/e7e8e0f841e608dc6f78c746ef2d971fb1f6fe8a9a428d0731ef0abf8b59/fastavro-1.10.0-cp311-cp311-macosx_10_9_universal2.whl", hash = "sha256:d183c075f527ab695a27ae75f210d4a86bce660cda2f85ae84d5606efc15ef50", size = 1040292 },
    { url = "https://files.pythonhosted.org/packages/3a/96/43a65881f061bc5ec6dcf39e59f639a7344e822d4caadae748d076aaf4d0/fastavro-1.10.0-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:d7a95a2c0639bffd7c079b59e9a796bfc3a9acd78acff7088f7c54ade24e4a77", size = 3312624 },
    { url = "https://files.pythonhosted.org/packages/c8/45/dba0cc08cf42500dd0f1e552e0fefe1cd81c47099d99277828a1081cbd87/fastavro-1.10.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:0a678153b5da1b024a32ec3f611b2e7afd24deac588cb51dd1b0019935191a6d", size = 3334284 },
    { url = "https://files.pythonhosted.org/packages/76/e3/3d9b0824e2e2da56e6a435a70a4db7ed801136daa451577a819bbedc6cf8/fastavro-1.10.0-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:67a597a5cfea4dddcf8b49eaf8c2b5ffee7fda15b578849185bc690ec0cd0d8f", size = 3283647 },
    { url = "https://files.pythonhosted.org/packages/a1/dc/83d985f8212194e8283ebae86491fccde8710fd81d81ef8659e5373f4f1b/fastavro-1.10.0-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:1fd689724760b17f69565d8a4e7785ed79becd451d1c99263c40cb2d6491f1d4", size = 3419520 },
    { url = "https://files.pythonhosted.org/packages/fd/7f/21711a9ec9937c84406e0773ba3fc6f8d66389a364da46618706f9c37d30/fastavro-1.10.0-cp311-cp311-win_amd64.whl", hash = "sha256:4f949d463f9ac4221128a51e4e34e2562f401e5925adcadfd28637a73df6c2d8", size = 499750 },
    { url = "https://files.pythonhosted.org/packages/9c/a4/8e69c0a5cd121e5d476237de1bde5a7947f791ae45768ae52ed0d3ea8d18/fastavro-1.10.0-cp312-cp312-macosx_10_13_universal2.whl", hash = "sha256:cfe57cb0d72f304bd0dcc5a3208ca6a7363a9ae76f3073307d095c9d053b29d4", size = 1036343 },
    { url = "https://files.pythonhosted.org/packages/1e/01/aa219e2b33e5873d27b867ec0fad9f35f23d461114e1135a7e46c06786d2/fastavro-1.10.0-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:74e517440c824cb65fb29d3e3903a9406f4d7c75490cef47e55c4c82cdc66270", size = 3263368 },
    { url = "https://files.pythonhosted.org/packages/a7/ba/1766e2d7d95df2e95e9e9a089dc7a537c0616720b053a111a918fa7ee6b6/fastavro-1.10.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:203c17d44cadde76e8eecb30f2d1b4f33eb478877552d71f049265dc6f2ecd10", size = 3328933 },
    { url = "https://files.pythonhosted.org/packages/2e/40/26e56696b9696ab4fbba25a96b8037ca3f9fd8a8cc55b4b36400ef023e49/fastavro-1.10.0-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:6575be7f2b5f94023b5a4e766b0251924945ad55e9a96672dc523656d17fe251", size = 3258045 },
    { url = "https://files.pythonhosted.org/packages/4e/bc/2f6c92c06c5363372abe828bccdd95762f2c1983b261509f94189c38c8a1/fastavro-1.10.0-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:fe471deb675ed2f01ee2aac958fbf8ebb13ea00fa4ce7f87e57710a0bc592208", size = 3418001 },
    { url = "https://files.pythonhosted.org/packages/0c/ce/cfd16546c04ebbca1be80873b533c788cec76f7bfac231bfac6786047572/fastavro-1.10.0-cp312-cp312-win_amd64.whl", hash = "sha256:567ff515f2a5d26d9674b31c95477f3e6022ec206124c62169bc2ffaf0889089", size = 487855 },
    { url = "https://files.pythonhosted.org/packages/c9/c4/163cf154cc694c2dccc70cd6796db6214ac668a1260bf0310401dad188dc/fastavro-1.10.0-cp313-cp313-macosx_10_13_universal2.whl", hash = "sha256:82263af0adfddb39c85f9517d736e1e940fe506dfcc35bc9ab9f85e0fa9236d8", size = 1022741 },
    { url = "https://files.pythonhosted.org/packages/38/01/a24598f5f31b8582a92fe9c41bf91caeed50d5b5eaa7576e6f8b23cb488d/fastavro-1.10.0-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:566c193109ff0ff84f1072a165b7106c4f96050078a4e6ac7391f81ca1ef3efa", size = 3237421 },
    { url = "https://files.pythonhosted.org/packages/a7/bf/08bcf65cfb7feb0e5b1329fafeb4a9b95b7b5ec723ba58c7dbd0d04ded34/fastavro-1.10.0-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:e400d2e55d068404d9fea7c5021f8b999c6f9d9afa1d1f3652ec92c105ffcbdd", size = 3300222 },
    { url = "https://files.pythonhosted.org/packages/53/4d/a6c25f3166328f8306ec2e6be1123ed78a55b8ab774a43a661124508881f/fastavro-1.10.0-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:9b8227497f71565270f9249fc9af32a93644ca683a0167cfe66d203845c3a038", size = 3233276 },
    { url = "https://files.pythonhosted.org/packages/47/1c/b2b2ce2bf866a248ae23e96a87b3b8369427ff79be9112073039bee1d245/fastavro-1.10.0-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:8e62d04c65461b30ac6d314e4197ad666371e97ae8cb2c16f971d802f6c7f514", size = 3388936 },
    { url = "https://files.pythonhosted.org/packages/1f/2c/43927e22a2d57587b3aa09765098a6d833246b672d34c10c5f135414745a/fastavro-1.10.0-cp313-cp313-win_amd64.whl", hash = "sha256:86baf8c9740ab570d0d4d18517da71626fe9be4d1142bea684db52bd5adb078f", size = 483967 },
    { url = "https://files.pythonhosted.org/packages/4b/43/4f294f748b252eeaf07d3540b5936e80622f92df649ea42022d404d6285c/fastavro-1.10.0-cp39-cp39-macosx_10_9_universal2.whl", hash = "sha256:5bccbb6f8e9e5b834cca964f0e6ebc27ebe65319d3940b0b397751a470f45612", size = 1037564 },
    { url = "https://files.pythonhosted.org/packages/64/ce/03f0bfd21ff2ebfc1520eb14101a3ecd9eda3da032ce966e5be3d724809c/fastavro-1.10.0-cp39-cp39-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:b0132f6b0b53f61a0a508a577f64beb5de1a5e068a9b4c0e1df6e3b66568eec4", size = 3024068 },
    { url = "https://files.pythonhosted.org/packages/f8/70/97cb9512be1179b77e1cf382ffbfb5f7fe601237024f8a69d8b44ba1b576/fastavro-1.10.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:ca37a363b711202c6071a6d4787e68e15fa3ab108261058c4aae853c582339af", size = 3069625 },
    { url = "https://files.pythonhosted.org/packages/5c/cb/a1e043319fde2a8b87dff2e0d7751b9de55fca705e1dbb183c805f55fe73/fastavro-1.10.0-cp39-cp39-musllinux_1_2_aarch64.whl", hash = "sha256:cf38cecdd67ca9bd92e6e9ba34a30db6343e7a3bedf171753ee78f8bd9f8a670", size = 2968653 },
    { url = "https://files.pythonhosted.org/packages/07/98/1cabfe975493dbc829af7aa8739f86313a54577290b5ae4ea07501fa6a59/fastavro-1.10.0-cp39-cp39-musllinux_1_2_x86_64.whl", hash = "sha256:f4dd10e0ed42982122d20cdf1a88aa50ee09e5a9cd9b39abdffb1aa4f5b76435", size = 3115893 },
    { url = "https://files.pythonhosted.org/packages/eb/c1/057b6ad6c3d0cb7ab5f23ac44a10cf6676c6c59155c40f40ac93f3c5960a/fastavro-1.10.0-cp39-cp39-win_amd64.whl", hash = "sha256:aaef147dc14dd2d7823246178fd06fc5e477460e070dc6d9e07dd8193a6bc93c", size = 546089 },
]

[[package]]
name = "filelock"
version = "3.18.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/0a/10/c23352565a6544bdc5353e0b15fc1c563352101f30e24bf500207a54df9a/filelock-3.18.0.tar.gz", hash = "sha256:adbc88eabb99d2fec8c9c1b229b171f18afa655400173ddc653d5d01501fb9f2", size = 18075 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/4d/36/2a115987e2d8c300a974597416d9de88f2444426de9571f4b59b2cca3acc/filelock-3.18.0-py3-none-any.whl", hash = "sha256:c401f4f8377c4464e6db25fff06205fd89bdd83b65eb0488ed1b160f780e21de", size = 16215 },
]

[[package]]
name = "frozenlist"
version = "1.5.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/8f/ed/0f4cec13a93c02c47ec32d81d11c0c1efbadf4a471e3f3ce7cad366cbbd3/frozenlist-1.5.0.tar.gz", hash = "sha256:81d5af29e61b9c8348e876d442253723928dce6433e0e76cd925cd83f1b4b817", size = 39930 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/54/79/29d44c4af36b2b240725dce566b20f63f9b36ef267aaaa64ee7466f4f2f8/frozenlist-1.5.0-cp310-cp310-macosx_10_9_universal2.whl", hash = "sha256:5b6a66c18b5b9dd261ca98dffcb826a525334b2f29e7caa54e182255c5f6a65a", size = 94451 },
    { url = "https://files.pythonhosted.org/packages/47/47/0c999aeace6ead8a44441b4f4173e2261b18219e4ad1fe9a479871ca02fc/frozenlist-1.5.0-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:d1b3eb7b05ea246510b43a7e53ed1653e55c2121019a97e60cad7efb881a97bb", size = 54301 },
    { url = "https://files.pythonhosted.org/packages/8d/60/107a38c1e54176d12e06e9d4b5d755b677d71d1219217cee063911b1384f/frozenlist-1.5.0-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:15538c0cbf0e4fa11d1e3a71f823524b0c46299aed6e10ebb4c2089abd8c3bec", size = 52213 },
    { url = "https://files.pythonhosted.org/packages/17/62/594a6829ac5679c25755362a9dc93486a8a45241394564309641425d3ff6/frozenlist-1.5.0-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:e79225373c317ff1e35f210dd5f1344ff31066ba8067c307ab60254cd3a78ad5", size = 240946 },
    { url = "https://files.pythonhosted.org/packages/7e/75/6c8419d8f92c80dd0ee3f63bdde2702ce6398b0ac8410ff459f9b6f2f9cb/frozenlist-1.5.0-cp310-cp310-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:9272fa73ca71266702c4c3e2d4a28553ea03418e591e377a03b8e3659d94fa76", size = 264608 },
    { url = "https://files.pythonhosted.org/packages/88/3e/82a6f0b84bc6fb7e0be240e52863c6d4ab6098cd62e4f5b972cd31e002e8/frozenlist-1.5.0-cp310-cp310-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:498524025a5b8ba81695761d78c8dd7382ac0b052f34e66939c42df860b8ff17", size = 261361 },
    { url = "https://files.pythonhosted.org/packages/fd/85/14e5f9ccac1b64ff2f10c927b3ffdf88772aea875882406f9ba0cec8ad84/frozenlist-1.5.0-cp310-cp310-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:92b5278ed9d50fe610185ecd23c55d8b307d75ca18e94c0e7de328089ac5dcba", size = 231649 },
    { url = "https://files.pythonhosted.org/packages/ee/59/928322800306f6529d1852323014ee9008551e9bb027cc38d276cbc0b0e7/frozenlist-1.5.0-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:7f3c8c1dacd037df16e85227bac13cca58c30da836c6f936ba1df0c05d046d8d", size = 241853 },
    { url = "https://files.pythonhosted.org/packages/7d/bd/e01fa4f146a6f6c18c5d34cab8abdc4013774a26c4ff851128cd1bd3008e/frozenlist-1.5.0-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:f2ac49a9bedb996086057b75bf93538240538c6d9b38e57c82d51f75a73409d2", size = 243652 },
    { url = "https://files.pythonhosted.org/packages/a5/bd/e4771fd18a8ec6757033f0fa903e447aecc3fbba54e3630397b61596acf0/frozenlist-1.5.0-cp310-cp310-musllinux_1_2_i686.whl", hash = "sha256:e66cc454f97053b79c2ab09c17fbe3c825ea6b4de20baf1be28919460dd7877f", size = 241734 },
    { url = "https://files.pythonhosted.org/packages/21/13/c83821fa5544af4f60c5d3a65d054af3213c26b14d3f5f48e43e5fb48556/frozenlist-1.5.0-cp310-cp310-musllinux_1_2_ppc64le.whl", hash = "sha256:5a3ba5f9a0dfed20337d3e966dc359784c9f96503674c2faf015f7fe8e96798c", size = 260959 },
    { url = "https://files.pythonhosted.org/packages/71/f3/1f91c9a9bf7ed0e8edcf52698d23f3c211d8d00291a53c9f115ceb977ab1/frozenlist-1.5.0-cp310-cp310-musllinux_1_2_s390x.whl", hash = "sha256:6321899477db90bdeb9299ac3627a6a53c7399c8cd58d25da094007402b039ab", size = 262706 },
    { url = "https://files.pythonhosted.org/packages/4c/22/4a256fdf5d9bcb3ae32622c796ee5ff9451b3a13a68cfe3f68e2c95588ce/frozenlist-1.5.0-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:76e4753701248476e6286f2ef492af900ea67d9706a0155335a40ea21bf3b2f5", size = 250401 },
    { url = "https://files.pythonhosted.org/packages/af/89/c48ebe1f7991bd2be6d5f4ed202d94960c01b3017a03d6954dd5fa9ea1e8/frozenlist-1.5.0-cp310-cp310-win32.whl", hash = "sha256:977701c081c0241d0955c9586ffdd9ce44f7a7795df39b9151cd9a6fd0ce4cfb", size = 45498 },
    { url = "https://files.pythonhosted.org/packages/28/2f/cc27d5f43e023d21fe5c19538e08894db3d7e081cbf582ad5ed366c24446/frozenlist-1.5.0-cp310-cp310-win_amd64.whl", hash = "sha256:189f03b53e64144f90990d29a27ec4f7997d91ed3d01b51fa39d2dbe77540fd4", size = 51622 },
    { url = "https://files.pythonhosted.org/packages/79/43/0bed28bf5eb1c9e4301003b74453b8e7aa85fb293b31dde352aac528dafc/frozenlist-1.5.0-cp311-cp311-macosx_10_9_universal2.whl", hash = "sha256:fd74520371c3c4175142d02a976aee0b4cb4a7cc912a60586ffd8d5929979b30", size = 94987 },
    { url = "https://files.pythonhosted.org/packages/bb/bf/b74e38f09a246e8abbe1e90eb65787ed745ccab6eaa58b9c9308e052323d/frozenlist-1.5.0-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:2f3f7a0fbc219fb4455264cae4d9f01ad41ae6ee8524500f381de64ffaa077d5", size = 54584 },
    { url = "https://files.pythonhosted.org/packages/2c/31/ab01375682f14f7613a1ade30149f684c84f9b8823a4391ed950c8285656/frozenlist-1.5.0-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:f47c9c9028f55a04ac254346e92977bf0f166c483c74b4232bee19a6697e4778", size = 52499 },
    { url = "https://files.pythonhosted.org/packages/98/a8/d0ac0b9276e1404f58fec3ab6e90a4f76b778a49373ccaf6a563f100dfbc/frozenlist-1.5.0-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:0996c66760924da6e88922756d99b47512a71cfd45215f3570bf1e0b694c206a", size = 276357 },
    { url = "https://files.pythonhosted.org/packages/ad/c9/c7761084fa822f07dac38ac29f841d4587570dd211e2262544aa0b791d21/frozenlist-1.5.0-cp311-cp311-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:a2fe128eb4edeabe11896cb6af88fca5346059f6c8d807e3b910069f39157869", size = 287516 },
    { url = "https://files.pythonhosted.org/packages/a1/ff/cd7479e703c39df7bdab431798cef89dc75010d8aa0ca2514c5b9321db27/frozenlist-1.5.0-cp311-cp311-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:1a8ea951bbb6cacd492e3948b8da8c502a3f814f5d20935aae74b5df2b19cf3d", size = 283131 },
    { url = "https://files.pythonhosted.org/packages/59/a0/370941beb47d237eca4fbf27e4e91389fd68699e6f4b0ebcc95da463835b/frozenlist-1.5.0-cp311-cp311-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:de537c11e4aa01d37db0d403b57bd6f0546e71a82347a97c6a9f0dcc532b3a45", size = 261320 },
    { url = "https://files.pythonhosted.org/packages/b8/5f/c10123e8d64867bc9b4f2f510a32042a306ff5fcd7e2e09e5ae5100ee333/frozenlist-1.5.0-cp311-cp311-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:9c2623347b933fcb9095841f1cc5d4ff0b278addd743e0e966cb3d460278840d", size = 274877 },
    { url = "https://files.pythonhosted.org/packages/fa/79/38c505601ae29d4348f21706c5d89755ceded02a745016ba2f58bd5f1ea6/frozenlist-1.5.0-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:cee6798eaf8b1416ef6909b06f7dc04b60755206bddc599f52232606e18179d3", size = 269592 },
    { url = "https://files.pythonhosted.org/packages/19/e2/39f3a53191b8204ba9f0bb574b926b73dd2efba2a2b9d2d730517e8f7622/frozenlist-1.5.0-cp311-cp311-musllinux_1_2_i686.whl", hash = "sha256:f5f9da7f5dbc00a604fe74aa02ae7c98bcede8a3b8b9666f9f86fc13993bc71a", size = 265934 },
    { url = "https://files.pythonhosted.org/packages/d5/c9/3075eb7f7f3a91f1a6b00284af4de0a65a9ae47084930916f5528144c9dd/frozenlist-1.5.0-cp311-cp311-musllinux_1_2_ppc64le.whl", hash = "sha256:90646abbc7a5d5c7c19461d2e3eeb76eb0b204919e6ece342feb6032c9325ae9", size = 283859 },
    { url = "https://files.pythonhosted.org/packages/05/f5/549f44d314c29408b962fa2b0e69a1a67c59379fb143b92a0a065ffd1f0f/frozenlist-1.5.0-cp311-cp311-musllinux_1_2_s390x.whl", hash = "sha256:bdac3c7d9b705d253b2ce370fde941836a5f8b3c5c2b8fd70940a3ea3af7f4f2", size = 287560 },
    { url = "https://files.pythonhosted.org/packages/9d/f8/cb09b3c24a3eac02c4c07a9558e11e9e244fb02bf62c85ac2106d1eb0c0b/frozenlist-1.5.0-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:03d33c2ddbc1816237a67f66336616416e2bbb6beb306e5f890f2eb22b959cdf", size = 277150 },
    { url = "https://files.pythonhosted.org/packages/37/48/38c2db3f54d1501e692d6fe058f45b6ad1b358d82cd19436efab80cfc965/frozenlist-1.5.0-cp311-cp311-win32.whl", hash = "sha256:237f6b23ee0f44066219dae14c70ae38a63f0440ce6750f868ee08775073f942", size = 45244 },
    { url = "https://files.pythonhosted.org/packages/ca/8c/2ddffeb8b60a4bce3b196c32fcc30d8830d4615e7b492ec2071da801b8ad/frozenlist-1.5.0-cp311-cp311-win_amd64.whl", hash = "sha256:0cc974cc93d32c42e7b0f6cf242a6bd941c57c61b618e78b6c0a96cb72788c1d", size = 51634 },
    { url = "https://files.pythonhosted.org/packages/79/73/fa6d1a96ab7fd6e6d1c3500700963eab46813847f01ef0ccbaa726181dd5/frozenlist-1.5.0-cp312-cp312-macosx_10_13_universal2.whl", hash = "sha256:31115ba75889723431aa9a4e77d5f398f5cf976eea3bdf61749731f62d4a4a21", size = 94026 },
    { url = "https://files.pythonhosted.org/packages/ab/04/ea8bf62c8868b8eada363f20ff1b647cf2e93377a7b284d36062d21d81d1/frozenlist-1.5.0-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:7437601c4d89d070eac8323f121fcf25f88674627505334654fd027b091db09d", size = 54150 },
    { url = "https://files.pythonhosted.org/packages/d0/9a/8e479b482a6f2070b26bda572c5e6889bb3ba48977e81beea35b5ae13ece/frozenlist-1.5.0-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:7948140d9f8ece1745be806f2bfdf390127cf1a763b925c4a805c603df5e697e", size = 51927 },
    { url = "https://files.pythonhosted.org/packages/e3/12/2aad87deb08a4e7ccfb33600871bbe8f0e08cb6d8224371387f3303654d7/frozenlist-1.5.0-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:feeb64bc9bcc6b45c6311c9e9b99406660a9c05ca8a5b30d14a78555088b0b3a", size = 282647 },
    { url = "https://files.pythonhosted.org/packages/77/f2/07f06b05d8a427ea0060a9cef6e63405ea9e0d761846b95ef3fb3be57111/frozenlist-1.5.0-cp312-cp312-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:683173d371daad49cffb8309779e886e59c2f369430ad28fe715f66d08d4ab1a", size = 289052 },
    { url = "https://files.pythonhosted.org/packages/bd/9f/8bf45a2f1cd4aa401acd271b077989c9267ae8463e7c8b1eb0d3f561b65e/frozenlist-1.5.0-cp312-cp312-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:7d57d8f702221405a9d9b40f9da8ac2e4a1a8b5285aac6100f3393675f0a85ee", size = 291719 },
    { url = "https://files.pythonhosted.org/packages/41/d1/1f20fd05a6c42d3868709b7604c9f15538a29e4f734c694c6bcfc3d3b935/frozenlist-1.5.0-cp312-cp312-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:30c72000fbcc35b129cb09956836c7d7abf78ab5416595e4857d1cae8d6251a6", size = 267433 },
    { url = "https://files.pythonhosted.org/packages/af/f2/64b73a9bb86f5a89fb55450e97cd5c1f84a862d4ff90d9fd1a73ab0f64a5/frozenlist-1.5.0-cp312-cp312-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:000a77d6034fbad9b6bb880f7ec073027908f1b40254b5d6f26210d2dab1240e", size = 283591 },
    { url = "https://files.pythonhosted.org/packages/29/e2/ffbb1fae55a791fd6c2938dd9ea779509c977435ba3940b9f2e8dc9d5316/frozenlist-1.5.0-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:5d7f5a50342475962eb18b740f3beecc685a15b52c91f7d975257e13e029eca9", size = 273249 },
    { url = "https://files.pythonhosted.org/packages/2e/6e/008136a30798bb63618a114b9321b5971172a5abddff44a100c7edc5ad4f/frozenlist-1.5.0-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:87f724d055eb4785d9be84e9ebf0f24e392ddfad00b3fe036e43f489fafc9039", size = 271075 },
    { url = "https://files.pythonhosted.org/packages/ae/f0/4e71e54a026b06724cec9b6c54f0b13a4e9e298cc8db0f82ec70e151f5ce/frozenlist-1.5.0-cp312-cp312-musllinux_1_2_ppc64le.whl", hash = "sha256:6e9080bb2fb195a046e5177f10d9d82b8a204c0736a97a153c2466127de87784", size = 285398 },
    { url = "https://files.pythonhosted.org/packages/4d/36/70ec246851478b1c0b59f11ef8ade9c482ff447c1363c2bd5fad45098b12/frozenlist-1.5.0-cp312-cp312-musllinux_1_2_s390x.whl", hash = "sha256:9b93d7aaa36c966fa42efcaf716e6b3900438632a626fb09c049f6a2f09fc631", size = 294445 },
    { url = "https://files.pythonhosted.org/packages/37/e0/47f87544055b3349b633a03c4d94b405956cf2437f4ab46d0928b74b7526/frozenlist-1.5.0-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:52ef692a4bc60a6dd57f507429636c2af8b6046db8b31b18dac02cbc8f507f7f", size = 280569 },
    { url = "https://files.pythonhosted.org/packages/f9/7c/490133c160fb6b84ed374c266f42800e33b50c3bbab1652764e6e1fc498a/frozenlist-1.5.0-cp312-cp312-win32.whl", hash = "sha256:29d94c256679247b33a3dc96cce0f93cbc69c23bf75ff715919332fdbb6a32b8", size = 44721 },
    { url = "https://files.pythonhosted.org/packages/b1/56/4e45136ffc6bdbfa68c29ca56ef53783ef4c2fd395f7cbf99a2624aa9aaa/frozenlist-1.5.0-cp312-cp312-win_amd64.whl", hash = "sha256:8969190d709e7c48ea386db202d708eb94bdb29207a1f269bab1196ce0dcca1f", size = 51329 },
    { url = "https://files.pythonhosted.org/packages/da/3b/915f0bca8a7ea04483622e84a9bd90033bab54bdf485479556c74fd5eaf5/frozenlist-1.5.0-cp313-cp313-macosx_10_13_universal2.whl", hash = "sha256:7a1a048f9215c90973402e26c01d1cff8a209e1f1b53f72b95c13db61b00f953", size = 91538 },
    { url = "https://files.pythonhosted.org/packages/c7/d1/a7c98aad7e44afe5306a2b068434a5830f1470675f0e715abb86eb15f15b/frozenlist-1.5.0-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:dd47a5181ce5fcb463b5d9e17ecfdb02b678cca31280639255ce9d0e5aa67af0", size = 52849 },
    { url = "https://files.pythonhosted.org/packages/3a/c8/76f23bf9ab15d5f760eb48701909645f686f9c64fbb8982674c241fbef14/frozenlist-1.5.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:1431d60b36d15cda188ea222033eec8e0eab488f39a272461f2e6d9e1a8e63c2", size = 50583 },
    { url = "https://files.pythonhosted.org/packages/1f/22/462a3dd093d11df623179d7754a3b3269de3b42de2808cddef50ee0f4f48/frozenlist-1.5.0-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:6482a5851f5d72767fbd0e507e80737f9c8646ae7fd303def99bfe813f76cf7f", size = 265636 },
    { url = "https://files.pythonhosted.org/packages/80/cf/e075e407fc2ae7328155a1cd7e22f932773c8073c1fc78016607d19cc3e5/frozenlist-1.5.0-cp313-cp313-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:44c49271a937625619e862baacbd037a7ef86dd1ee215afc298a417ff3270608", size = 270214 },
    { url = "https://files.pythonhosted.org/packages/a1/58/0642d061d5de779f39c50cbb00df49682832923f3d2ebfb0fedf02d05f7f/frozenlist-1.5.0-cp313-cp313-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:12f78f98c2f1c2429d42e6a485f433722b0061d5c0b0139efa64f396efb5886b", size = 273905 },
    { url = "https://files.pythonhosted.org/packages/ab/66/3fe0f5f8f2add5b4ab7aa4e199f767fd3b55da26e3ca4ce2cc36698e50c4/frozenlist-1.5.0-cp313-cp313-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:ce3aa154c452d2467487765e3adc730a8c153af77ad84096bc19ce19a2400840", size = 250542 },
    { url = "https://files.pythonhosted.org/packages/f6/b8/260791bde9198c87a465224e0e2bb62c4e716f5d198fc3a1dacc4895dbd1/frozenlist-1.5.0-cp313-cp313-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:9b7dc0c4338e6b8b091e8faf0db3168a37101943e687f373dce00959583f7439", size = 267026 },
    { url = "https://files.pythonhosted.org/packages/2e/a4/3d24f88c527f08f8d44ade24eaee83b2627793fa62fa07cbb7ff7a2f7d42/frozenlist-1.5.0-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:45e0896250900b5aa25180f9aec243e84e92ac84bd4a74d9ad4138ef3f5c97de", size = 257690 },
    { url = "https://files.pythonhosted.org/packages/de/9a/d311d660420b2beeff3459b6626f2ab4fb236d07afbdac034a4371fe696e/frozenlist-1.5.0-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:561eb1c9579d495fddb6da8959fd2a1fca2c6d060d4113f5844b433fc02f2641", size = 253893 },
    { url = "https://files.pythonhosted.org/packages/c6/23/e491aadc25b56eabd0f18c53bb19f3cdc6de30b2129ee0bc39cd387cd560/frozenlist-1.5.0-cp313-cp313-musllinux_1_2_ppc64le.whl", hash = "sha256:df6e2f325bfee1f49f81aaac97d2aa757c7646534a06f8f577ce184afe2f0a9e", size = 267006 },
    { url = "https://files.pythonhosted.org/packages/08/c4/ab918ce636a35fb974d13d666dcbe03969592aeca6c3ab3835acff01f79c/frozenlist-1.5.0-cp313-cp313-musllinux_1_2_s390x.whl", hash = "sha256:140228863501b44b809fb39ec56b5d4071f4d0aa6d216c19cbb08b8c5a7eadb9", size = 276157 },
    { url = "https://files.pythonhosted.org/packages/c0/29/3b7a0bbbbe5a34833ba26f686aabfe982924adbdcafdc294a7a129c31688/frozenlist-1.5.0-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:7707a25d6a77f5d27ea7dc7d1fc608aa0a478193823f88511ef5e6b8a48f9d03", size = 264642 },
    { url = "https://files.pythonhosted.org/packages/ab/42/0595b3dbffc2e82d7fe658c12d5a5bafcd7516c6bf2d1d1feb5387caa9c1/frozenlist-1.5.0-cp313-cp313-win32.whl", hash = "sha256:31a9ac2b38ab9b5a8933b693db4939764ad3f299fcaa931a3e605bc3460e693c", size = 44914 },
    { url = "https://files.pythonhosted.org/packages/17/c4/b7db1206a3fea44bf3b838ca61deb6f74424a8a5db1dd53ecb21da669be6/frozenlist-1.5.0-cp313-cp313-win_amd64.whl", hash = "sha256:11aabdd62b8b9c4b84081a3c246506d1cddd2dd93ff0ad53ede5defec7886b28", size = 51167 },
    { url = "https://files.pythonhosted.org/packages/da/4d/d94ff0fb0f5313902c132817c62d19cdc5bdcd0c195d392006ef4b779fc6/frozenlist-1.5.0-cp39-cp39-macosx_10_9_universal2.whl", hash = "sha256:9bbcdfaf4af7ce002694a4e10a0159d5a8d20056a12b05b45cea944a4953f972", size = 95319 },
    { url = "https://files.pythonhosted.org/packages/8c/1b/d90e554ca2b483d31cb2296e393f72c25bdc38d64526579e95576bfda587/frozenlist-1.5.0-cp39-cp39-macosx_10_9_x86_64.whl", hash = "sha256:1893f948bf6681733aaccf36c5232c231e3b5166d607c5fa77773611df6dc336", size = 54749 },
    { url = "https://files.pythonhosted.org/packages/f8/66/7fdecc9ef49f8db2aa4d9da916e4ecf357d867d87aea292efc11e1b2e932/frozenlist-1.5.0-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:2b5e23253bb709ef57a8e95e6ae48daa9ac5f265637529e4ce6b003a37b2621f", size = 52718 },
    { url = "https://files.pythonhosted.org/packages/08/04/e2fddc92135276e07addbc1cf413acffa0c2d848b3e54cacf684e146df49/frozenlist-1.5.0-cp39-cp39-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:0f253985bb515ecd89629db13cb58d702035ecd8cfbca7d7a7e29a0e6d39af5f", size = 241756 },
    { url = "https://files.pythonhosted.org/packages/c6/52/be5ff200815d8a341aee5b16b6b707355e0ca3652953852238eb92b120c2/frozenlist-1.5.0-cp39-cp39-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:04a5c6babd5e8fb7d3c871dc8b321166b80e41b637c31a995ed844a6139942b6", size = 267718 },
    { url = "https://files.pythonhosted.org/packages/88/be/4bd93a58be57a3722fc544c36debdf9dcc6758f761092e894d78f18b8f20/frozenlist-1.5.0-cp39-cp39-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:a9fe0f1c29ba24ba6ff6abf688cb0b7cf1efab6b6aa6adc55441773c252f7411", size = 263494 },
    { url = "https://files.pythonhosted.org/packages/32/ba/58348b90193caa096ce9e9befea6ae67f38dabfd3aacb47e46137a6250a8/frozenlist-1.5.0-cp39-cp39-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:226d72559fa19babe2ccd920273e767c96a49b9d3d38badd7c91a0fdeda8ea08", size = 232838 },
    { url = "https://files.pythonhosted.org/packages/f6/33/9f152105227630246135188901373c4f322cc026565ca6215b063f4c82f4/frozenlist-1.5.0-cp39-cp39-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:15b731db116ab3aedec558573c1a5eec78822b32292fe4f2f0345b7f697745c2", size = 242912 },
    { url = "https://files.pythonhosted.org/packages/a0/10/3db38fb3ccbafadd80a1b0d6800c987b0e3fe3ef2d117c6ced0246eea17a/frozenlist-1.5.0-cp39-cp39-musllinux_1_2_aarch64.whl", hash = "sha256:366d8f93e3edfe5a918c874702f78faac300209a4d5bf38352b2c1bdc07a766d", size = 244763 },
    { url = "https://files.pythonhosted.org/packages/e2/cd/1df468fdce2f66a4608dffe44c40cdc35eeaa67ef7fd1d813f99a9a37842/frozenlist-1.5.0-cp39-cp39-musllinux_1_2_i686.whl", hash = "sha256:1b96af8c582b94d381a1c1f51ffaedeb77c821c690ea5f01da3d70a487dd0a9b", size = 242841 },
    { url = "https://files.pythonhosted.org/packages/ee/5f/16097a5ca0bb6b6779c02cc9379c72fe98d56115d4c54d059fb233168fb6/frozenlist-1.5.0-cp39-cp39-musllinux_1_2_ppc64le.whl", hash = "sha256:c03eff4a41bd4e38415cbed054bbaff4a075b093e2394b6915dca34a40d1e38b", size = 263407 },
    { url = "https://files.pythonhosted.org/packages/0f/f7/58cd220ee1c2248ee65a32f5b4b93689e3fe1764d85537eee9fc392543bc/frozenlist-1.5.0-cp39-cp39-musllinux_1_2_s390x.whl", hash = "sha256:50cf5e7ee9b98f22bdecbabf3800ae78ddcc26e4a435515fc72d97903e8488e0", size = 265083 },
    { url = "https://files.pythonhosted.org/packages/62/b8/49768980caabf81ac4a2d156008f7cbd0107e6b36d08a313bb31035d9201/frozenlist-1.5.0-cp39-cp39-musllinux_1_2_x86_64.whl", hash = "sha256:1e76bfbc72353269c44e0bc2cfe171900fbf7f722ad74c9a7b638052afe6a00c", size = 251564 },
    { url = "https://files.pythonhosted.org/packages/cb/83/619327da3b86ef957ee7a0cbf3c166a09ed1e87a3f7f1ff487d7d0284683/frozenlist-1.5.0-cp39-cp39-win32.whl", hash = "sha256:666534d15ba8f0fda3f53969117383d5dc021266b3c1a42c9ec4855e4b58b9d3", size = 45691 },
    { url = "https://files.pythonhosted.org/packages/8b/28/407bc34a745151ed2322c690b6e7d83d7101472e81ed76e1ebdac0b70a78/frozenlist-1.5.0-cp39-cp39-win_amd64.whl", hash = "sha256:5c28f4b5dbef8a0d8aad0d4de24d1e9e981728628afaf4ea0792f5d0939372f0", size = 51767 },
    { url = "https://files.pythonhosted.org/packages/c6/c8/a5be5b7550c10858fcf9b0ea054baccab474da77d37f1e828ce043a3a5d4/frozenlist-1.5.0-py3-none-any.whl", hash = "sha256:d994863bba198a4a518b467bb971c56e1db3f180a25c6cf7bb1949c267f748c3", size = 11901 },
]

[[package]]
name = "fsspec"
version = "2024.12.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/ee/11/de70dee31455c546fbc88301971ec03c328f3d1138cfba14263f651e9551/fsspec-2024.12.0.tar.gz", hash = "sha256:670700c977ed2fb51e0d9f9253177ed20cbde4a3e5c0283cc5385b5870c8533f", size = 291600 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/de/86/5486b0188d08aa643e127774a99bac51ffa6cf343e3deb0583956dca5b22/fsspec-2024.12.0-py3-none-any.whl", hash = "sha256:b520aed47ad9804237ff878b504267a3b0b441e97508bd6d2d8774e3db85cee2", size = 183862 },
]

[package.optional-dependencies]
http = [
    { name = "aiohttp" },
]

[[package]]
name = "h11"
version = "0.14.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/f5/38/3af3d3633a34a3316095b39c8e8fb4853a28a536e55d347bd8d8e9a14b03/h11-0.14.0.tar.gz", hash = "sha256:8f19fbbe99e72420ff35c00b27a34cb9937e902a8b810e2c88300c6f0a3b699d", size = 100418 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/95/04/ff642e65ad6b90db43e668d70ffb6736436c7ce41fcc549f4e9472234127/h11-0.14.0-py3-none-any.whl", hash = "sha256:e3fe4ac4b851c468cc8363d500db52c2ead036020723024a109d37346efaa761", size = 58259 },
]

[[package]]
name = "httpcore"
version = "1.0.7"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "certifi" },
    { name = "h11" },
]
sdist = { url = "https://files.pythonhosted.org/packages/6a/41/d7d0a89eb493922c37d343b607bc1b5da7f5be7e383740b4753ad8943e90/httpcore-1.0.7.tar.gz", hash = "sha256:8551cb62a169ec7162ac7be8d4817d561f60e08eaa485234898414bb5a8a0b4c", size = 85196 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/87/f5/72347bc88306acb359581ac4d52f23c0ef445b57157adedb9aee0cd689d2/httpcore-1.0.7-py3-none-any.whl", hash = "sha256:a3fff8f43dc260d5bd363d9f9cf1830fa3a458b332856f34282de498ed420edd", size = 78551 },
]

[[package]]
name = "httpx"
version = "0.28.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "anyio" },
    { name = "certifi" },
    { name = "httpcore" },
    { name = "idna" },
]
sdist = { url = "https://files.pythonhosted.org/packages/b1/df/48c586a5fe32a0f01324ee087459e112ebb7224f646c0b5023f5e79e9956/httpx-0.28.1.tar.gz", hash = "sha256:75e98c5f16b0f35b567856f597f06ff2270a374470a5c2392242528e3e3e42fc", size = 141406 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/2a/39/e50c7c3a983047577ee07d2a9e53faf5a69493943ec3f6a384bdc792deb2/httpx-0.28.1-py3-none-any.whl", hash = "sha256:d909fcccc110f8c7faf814ca82a9a4d816bc5a6dbfea25d6591d6985b8ba59ad", size = 73517 },
]

[[package]]
name = "httpx-sse"
version = "0.4.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/4c/60/8f4281fa9bbf3c8034fd54c0e7412e66edbab6bc74c4996bd616f8d0406e/httpx-sse-0.4.0.tar.gz", hash = "sha256:1e81a3a3070ce322add1d3529ed42eb5f70817f45ed6ec915ab753f961139721", size = 12624 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/e1/9b/a181f281f65d776426002f330c31849b86b31fc9d848db62e16f03ff739f/httpx_sse-0.4.0-py3-none-any.whl", hash = "sha256:f329af6eae57eaa2bdfd962b42524764af68075ea87370a2de920af5341e318f", size = 7819 },
]

[[package]]
name = "huggingface-hub"
version = "0.30.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "filelock" },
    { name = "fsspec" },
    { name = "packaging" },
    { name = "pyyaml" },
    { name = "requests" },
    { name = "tqdm" },
    { name = "typing-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/78/be/049689a7197630e75c4bb53021cb209a56617c9bf39b3a0950650d1f96e1/huggingface_hub-0.30.1.tar.gz", hash = "sha256:f379e8b8d0791295602538856638460ae3cf679c7f304201eb80fb98c771950e", size = 400784 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/99/e3/2232d0e726d4d6ea69643b9593d97d0e7e6ea69c2fe9ed5de34d476c1c47/huggingface_hub-0.30.1-py3-none-any.whl", hash = "sha256:0f6aa5ec5a4e68e5b9e45d556b4e5ea180c58f5a5ffa734e7f38c9d573028959", size = 481170 },
]

[[package]]
name = "idna"
version = "3.10"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/f1/70/7703c29685631f5a7590aa73f1f1d3fa9a380e654b86af429e0934a32f7d/idna-3.10.tar.gz", hash = "sha256:12f65c9b470abda6dc35cf8e63cc574b1c52b11df2c86030af0ac09b01b13ea9", size = 190490 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/76/c6/c88e154df9c4e1a2a66ccf0005a88dfb2650c1dffb6f5ce603dfbd452ce3/idna-3.10-py3-none-any.whl", hash = "sha256:946d195a0d259cbba61165e88e65941f16e9b36ea6ddb97f00452bae8b1287d3", size = 70442 },
]

[[package]]
name = "iniconfig"
version = "2.1.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/f2/97/ebf4da567aa6827c909642694d71c9fcf53e5b504f2d96afea02718862f3/iniconfig-2.1.0.tar.gz", hash = "sha256:3abbd2e30b36733fee78f9c7f7308f2d0050e88f0087fd25c2645f63c773e1c7", size = 4793 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/2c/e1/e6716421ea10d38022b952c159d5161ca1193197fb744506875fbb87ea7b/iniconfig-2.1.0-py3-none-any.whl", hash = "sha256:9deba5723312380e77435581c6bf4935c94cbfab9b1ed33ef8d238ea168eb760", size = 6050 },
]

[[package]]
name = "jinja2"
version = "3.1.6"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "markupsafe" },
]
sdist = { url = "https://files.pythonhosted.org/packages/df/bf/f7da0350254c0ed7c72f3e33cef02e048281fec7ecec5f032d4aac52226b/jinja2-3.1.6.tar.gz", hash = "sha256:0137fb05990d35f1275a587e9aee6d56da821fc83491a0fb838183be43f66d6d", size = 245115 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/62/a1/3d680cbfd5f4b8f15abc1d571870c5fc3e594bb582bc3b64ea099db13e56/jinja2-3.1.6-py3-none-any.whl", hash = "sha256:85ece4451f492d0c13c5dd7c13a64681a86afae63a5f347908daf103ce6d2f67", size = 134899 },
]

[[package]]
name = "jiter"
version = "0.9.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/1e/c2/e4562507f52f0af7036da125bb699602ead37a2332af0788f8e0a3417f36/jiter-0.9.0.tar.gz", hash = "sha256:aadba0964deb424daa24492abc3d229c60c4a31bfee205aedbf1acc7639d7893", size = 162604 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/b0/82/39f7c9e67b3b0121f02a0b90d433626caa95a565c3d2449fea6bcfa3f5f5/jiter-0.9.0-cp310-cp310-macosx_10_12_x86_64.whl", hash = "sha256:816ec9b60fdfd1fec87da1d7ed46c66c44ffec37ab2ef7de5b147b2fce3fd5ad", size = 314540 },
    { url = "https://files.pythonhosted.org/packages/01/07/7bf6022c5a152fca767cf5c086bb41f7c28f70cf33ad259d023b53c0b858/jiter-0.9.0-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:9b1d3086f8a3ee0194ecf2008cf81286a5c3e540d977fa038ff23576c023c0ea", size = 321065 },
    { url = "https://files.pythonhosted.org/packages/6c/b2/de3f3446ecba7c48f317568e111cc112613da36c7b29a6de45a1df365556/jiter-0.9.0-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:1339f839b91ae30b37c409bf16ccd3dc453e8b8c3ed4bd1d6a567193651a4a51", size = 341664 },
    { url = "https://files.pythonhosted.org/packages/13/cf/6485a4012af5d407689c91296105fcdb080a3538e0658d2abf679619c72f/jiter-0.9.0-cp310-cp310-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:ffba79584b3b670fefae66ceb3a28822365d25b7bf811e030609a3d5b876f538", size = 364635 },
    { url = "https://files.pythonhosted.org/packages/0d/f7/4a491c568f005553240b486f8e05c82547340572d5018ef79414b4449327/jiter-0.9.0-cp310-cp310-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:5cfc7d0a8e899089d11f065e289cb5b2daf3d82fbe028f49b20d7b809193958d", size = 406288 },
    { url = "https://files.pythonhosted.org/packages/d3/ca/f4263ecbce7f5e6bded8f52a9f1a66540b270c300b5c9f5353d163f9ac61/jiter-0.9.0-cp310-cp310-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:e00a1a2bbfaaf237e13c3d1592356eab3e9015d7efd59359ac8b51eb56390a12", size = 397499 },
    { url = "https://files.pythonhosted.org/packages/ac/a2/522039e522a10bac2f2194f50e183a49a360d5f63ebf46f6d890ef8aa3f9/jiter-0.9.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:d1d9870561eb26b11448854dce0ff27a9a27cb616b632468cafc938de25e9e51", size = 352926 },
    { url = "https://files.pythonhosted.org/packages/b1/67/306a5c5abc82f2e32bd47333a1c9799499c1c3a415f8dde19dbf876f00cb/jiter-0.9.0-cp310-cp310-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:9872aeff3f21e437651df378cb75aeb7043e5297261222b6441a620218b58708", size = 384506 },
    { url = "https://files.pythonhosted.org/packages/0f/89/c12fe7b65a4fb74f6c0d7b5119576f1f16c79fc2953641f31b288fad8a04/jiter-0.9.0-cp310-cp310-musllinux_1_1_aarch64.whl", hash = "sha256:1fd19112d1049bdd47f17bfbb44a2c0001061312dcf0e72765bfa8abd4aa30e5", size = 520621 },
    { url = "https://files.pythonhosted.org/packages/c4/2b/d57900c5c06e6273fbaa76a19efa74dbc6e70c7427ab421bf0095dfe5d4a/jiter-0.9.0-cp310-cp310-musllinux_1_1_x86_64.whl", hash = "sha256:6ef5da104664e526836070e4a23b5f68dec1cc673b60bf1edb1bfbe8a55d0678", size = 512613 },
    { url = "https://files.pythonhosted.org/packages/89/05/d8b90bfb21e58097d5a4e0224f2940568366f68488a079ae77d4b2653500/jiter-0.9.0-cp310-cp310-win32.whl", hash = "sha256:cb12e6d65ebbefe5518de819f3eda53b73187b7089040b2d17f5b39001ff31c4", size = 206613 },
    { url = "https://files.pythonhosted.org/packages/2c/1d/5767f23f88e4f885090d74bbd2755518050a63040c0f59aa059947035711/jiter-0.9.0-cp310-cp310-win_amd64.whl", hash = "sha256:c43ca669493626d8672be3b645dbb406ef25af3f4b6384cfd306da7eb2e70322", size = 208371 },
    { url = "https://files.pythonhosted.org/packages/23/44/e241a043f114299254e44d7e777ead311da400517f179665e59611ab0ee4/jiter-0.9.0-cp311-cp311-macosx_10_12_x86_64.whl", hash = "sha256:6c4d99c71508912a7e556d631768dcdef43648a93660670986916b297f1c54af", size = 314654 },
    { url = "https://files.pythonhosted.org/packages/fb/1b/a7e5e42db9fa262baaa9489d8d14ca93f8663e7f164ed5e9acc9f467fc00/jiter-0.9.0-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:8f60fb8ce7df529812bf6c625635a19d27f30806885139e367af93f6e734ef58", size = 320909 },
    { url = "https://files.pythonhosted.org/packages/60/bf/8ebdfce77bc04b81abf2ea316e9c03b4a866a7d739cf355eae4d6fd9f6fe/jiter-0.9.0-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:51c4e1a4f8ea84d98b7b98912aa4290ac3d1eabfde8e3c34541fae30e9d1f08b", size = 341733 },
    { url = "https://files.pythonhosted.org/packages/a8/4e/754ebce77cff9ab34d1d0fa0fe98f5d42590fd33622509a3ba6ec37ff466/jiter-0.9.0-cp311-cp311-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:5f4c677c424dc76684fea3e7285a7a2a7493424bea89ac441045e6a1fb1d7b3b", size = 365097 },
    { url = "https://files.pythonhosted.org/packages/32/2c/6019587e6f5844c612ae18ca892f4cd7b3d8bbf49461ed29e384a0f13d98/jiter-0.9.0-cp311-cp311-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:2221176dfec87f3470b21e6abca056e6b04ce9bff72315cb0b243ca9e835a4b5", size = 406603 },
    { url = "https://files.pythonhosted.org/packages/da/e9/c9e6546c817ab75a1a7dab6dcc698e62e375e1017113e8e983fccbd56115/jiter-0.9.0-cp311-cp311-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:3c7adb66f899ffa25e3c92bfcb593391ee1947dbdd6a9a970e0d7e713237d572", size = 396625 },
    { url = "https://files.pythonhosted.org/packages/be/bd/976b458add04271ebb5a255e992bd008546ea04bb4dcadc042a16279b4b4/jiter-0.9.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:c98d27330fdfb77913c1097a7aab07f38ff2259048949f499c9901700789ac15", size = 351832 },
    { url = "https://files.pythonhosted.org/packages/07/51/fe59e307aaebec9265dbad44d9d4381d030947e47b0f23531579b9a7c2df/jiter-0.9.0-cp311-cp311-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:eda3f8cc74df66892b1d06b5d41a71670c22d95a1ca2cbab73654745ce9d0419", size = 384590 },
    { url = "https://files.pythonhosted.org/packages/db/55/5dcd2693794d8e6f4889389ff66ef3be557a77f8aeeca8973a97a7c00557/jiter-0.9.0-cp311-cp311-musllinux_1_1_aarch64.whl", hash = "sha256:dd5ab5ddc11418dce28343123644a100f487eaccf1de27a459ab36d6cca31043", size = 520690 },
    { url = "https://files.pythonhosted.org/packages/54/d5/9f51dc90985e9eb251fbbb747ab2b13b26601f16c595a7b8baba964043bd/jiter-0.9.0-cp311-cp311-musllinux_1_1_x86_64.whl", hash = "sha256:42f8a68a69f047b310319ef8e2f52fdb2e7976fb3313ef27df495cf77bcad965", size = 512649 },
    { url = "https://files.pythonhosted.org/packages/a6/e5/4e385945179bcf128fa10ad8dca9053d717cbe09e258110e39045c881fe5/jiter-0.9.0-cp311-cp311-win32.whl", hash = "sha256:a25519efb78a42254d59326ee417d6f5161b06f5da827d94cf521fed961b1ff2", size = 206920 },
    { url = "https://files.pythonhosted.org/packages/4c/47/5e0b94c603d8e54dd1faab439b40b832c277d3b90743e7835879ab663757/jiter-0.9.0-cp311-cp311-win_amd64.whl", hash = "sha256:923b54afdd697dfd00d368b7ccad008cccfeb1efb4e621f32860c75e9f25edbd", size = 210119 },
    { url = "https://files.pythonhosted.org/packages/af/d7/c55086103d6f29b694ec79156242304adf521577530d9031317ce5338c59/jiter-0.9.0-cp312-cp312-macosx_10_12_x86_64.whl", hash = "sha256:7b46249cfd6c48da28f89eb0be3f52d6fdb40ab88e2c66804f546674e539ec11", size = 309203 },
    { url = "https://files.pythonhosted.org/packages/b0/01/f775dfee50beb420adfd6baf58d1c4d437de41c9b666ddf127c065e5a488/jiter-0.9.0-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:609cf3c78852f1189894383cf0b0b977665f54cb38788e3e6b941fa6d982c00e", size = 319678 },
    { url = "https://files.pythonhosted.org/packages/ab/b8/09b73a793714726893e5d46d5c534a63709261af3d24444ad07885ce87cb/jiter-0.9.0-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:d726a3890a54561e55a9c5faea1f7655eda7f105bd165067575ace6e65f80bb2", size = 341816 },
    { url = "https://files.pythonhosted.org/packages/35/6f/b8f89ec5398b2b0d344257138182cc090302854ed63ed9c9051e9c673441/jiter-0.9.0-cp312-cp312-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:2e89dc075c1fef8fa9be219e249f14040270dbc507df4215c324a1839522ea75", size = 364152 },
    { url = "https://files.pythonhosted.org/packages/9b/ca/978cc3183113b8e4484cc7e210a9ad3c6614396e7abd5407ea8aa1458eef/jiter-0.9.0-cp312-cp312-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:04e8ffa3c353b1bc4134f96f167a2082494351e42888dfcf06e944f2729cbe1d", size = 406991 },
    { url = "https://files.pythonhosted.org/packages/13/3a/72861883e11a36d6aa314b4922125f6ae90bdccc225cd96d24cc78a66385/jiter-0.9.0-cp312-cp312-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:203f28a72a05ae0e129b3ed1f75f56bc419d5f91dfacd057519a8bd137b00c42", size = 395824 },
    { url = "https://files.pythonhosted.org/packages/87/67/22728a86ef53589c3720225778f7c5fdb617080e3deaed58b04789418212/jiter-0.9.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:fca1a02ad60ec30bb230f65bc01f611c8608b02d269f998bc29cca8619a919dc", size = 351318 },
    { url = "https://files.pythonhosted.org/packages/69/b9/f39728e2e2007276806d7a6609cda7fac44ffa28ca0d02c49a4f397cc0d9/jiter-0.9.0-cp312-cp312-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:237e5cee4d5d2659aaf91bbf8ec45052cc217d9446070699441a91b386ae27dc", size = 384591 },
    { url = "https://files.pythonhosted.org/packages/eb/8f/8a708bc7fd87b8a5d861f1c118a995eccbe6d672fe10c9753e67362d0dd0/jiter-0.9.0-cp312-cp312-musllinux_1_1_aarch64.whl", hash = "sha256:528b6b71745e7326eed73c53d4aa57e2a522242320b6f7d65b9c5af83cf49b6e", size = 520746 },
    { url = "https://files.pythonhosted.org/packages/95/1e/65680c7488bd2365dbd2980adaf63c562d3d41d3faac192ebc7ef5b4ae25/jiter-0.9.0-cp312-cp312-musllinux_1_1_x86_64.whl", hash = "sha256:9f48e86b57bc711eb5acdfd12b6cb580a59cc9a993f6e7dcb6d8b50522dcd50d", size = 512754 },
    { url = "https://files.pythonhosted.org/packages/78/f3/fdc43547a9ee6e93c837685da704fb6da7dba311fc022e2766d5277dfde5/jiter-0.9.0-cp312-cp312-win32.whl", hash = "sha256:699edfde481e191d81f9cf6d2211debbfe4bd92f06410e7637dffb8dd5dfde06", size = 207075 },
    { url = "https://files.pythonhosted.org/packages/cd/9d/742b289016d155f49028fe1bfbeb935c9bf0ffeefdf77daf4a63a42bb72b/jiter-0.9.0-cp312-cp312-win_amd64.whl", hash = "sha256:099500d07b43f61d8bd780466d429c45a7b25411b334c60ca875fa775f68ccb0", size = 207999 },
    { url = "https://files.pythonhosted.org/packages/e7/1b/4cd165c362e8f2f520fdb43245e2b414f42a255921248b4f8b9c8d871ff1/jiter-0.9.0-cp313-cp313-macosx_10_12_x86_64.whl", hash = "sha256:2764891d3f3e8b18dce2cff24949153ee30c9239da7c00f032511091ba688ff7", size = 308197 },
    { url = "https://files.pythonhosted.org/packages/13/aa/7a890dfe29c84c9a82064a9fe36079c7c0309c91b70c380dc138f9bea44a/jiter-0.9.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:387b22fbfd7a62418d5212b4638026d01723761c75c1c8232a8b8c37c2f1003b", size = 318160 },
    { url = "https://files.pythonhosted.org/packages/6a/38/5888b43fc01102f733f085673c4f0be5a298f69808ec63de55051754e390/jiter-0.9.0-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:40d8da8629ccae3606c61d9184970423655fb4e33d03330bcdfe52d234d32f69", size = 341259 },
    { url = "https://files.pythonhosted.org/packages/3d/5e/bbdbb63305bcc01006de683b6228cd061458b9b7bb9b8d9bc348a58e5dc2/jiter-0.9.0-cp313-cp313-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:a1be73d8982bdc278b7b9377426a4b44ceb5c7952073dd7488e4ae96b88e1103", size = 363730 },
    { url = "https://files.pythonhosted.org/packages/75/85/53a3edc616992fe4af6814c25f91ee3b1e22f7678e979b6ea82d3bc0667e/jiter-0.9.0-cp313-cp313-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:2228eaaaa111ec54b9e89f7481bffb3972e9059301a878d085b2b449fbbde635", size = 405126 },
    { url = "https://files.pythonhosted.org/packages/ae/b3/1ee26b12b2693bd3f0b71d3188e4e5d817b12e3c630a09e099e0a89e28fa/jiter-0.9.0-cp313-cp313-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:11509bfecbc319459647d4ac3fd391d26fdf530dad00c13c4dadabf5b81f01a4", size = 393668 },
    { url = "https://files.pythonhosted.org/packages/11/87/e084ce261950c1861773ab534d49127d1517b629478304d328493f980791/jiter-0.9.0-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:3f22238da568be8bbd8e0650e12feeb2cfea15eda4f9fc271d3b362a4fa0604d", size = 352350 },
    { url = "https://files.pythonhosted.org/packages/f0/06/7dca84b04987e9df563610aa0bc154ea176e50358af532ab40ffb87434df/jiter-0.9.0-cp313-cp313-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:17f5d55eb856597607562257c8e36c42bc87f16bef52ef7129b7da11afc779f3", size = 384204 },
    { url = "https://files.pythonhosted.org/packages/16/2f/82e1c6020db72f397dd070eec0c85ebc4df7c88967bc86d3ce9864148f28/jiter-0.9.0-cp313-cp313-musllinux_1_1_aarch64.whl", hash = "sha256:6a99bed9fbb02f5bed416d137944419a69aa4c423e44189bc49718859ea83bc5", size = 520322 },
    { url = "https://files.pythonhosted.org/packages/36/fd/4f0cd3abe83ce208991ca61e7e5df915aa35b67f1c0633eb7cf2f2e88ec7/jiter-0.9.0-cp313-cp313-musllinux_1_1_x86_64.whl", hash = "sha256:e057adb0cd1bd39606100be0eafe742de2de88c79df632955b9ab53a086b3c8d", size = 512184 },
    { url = "https://files.pythonhosted.org/packages/a0/3c/8a56f6d547731a0b4410a2d9d16bf39c861046f91f57c98f7cab3d2aa9ce/jiter-0.9.0-cp313-cp313-win32.whl", hash = "sha256:f7e6850991f3940f62d387ccfa54d1a92bd4bb9f89690b53aea36b4364bcab53", size = 206504 },
    { url = "https://files.pythonhosted.org/packages/f4/1c/0c996fd90639acda75ed7fa698ee5fd7d80243057185dc2f63d4c1c9f6b9/jiter-0.9.0-cp313-cp313-win_amd64.whl", hash = "sha256:c8ae3bf27cd1ac5e6e8b7a27487bf3ab5f82318211ec2e1346a5b058756361f7", size = 204943 },
    { url = "https://files.pythonhosted.org/packages/78/0f/77a63ca7aa5fed9a1b9135af57e190d905bcd3702b36aca46a01090d39ad/jiter-0.9.0-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:f0b2827fb88dda2cbecbbc3e596ef08d69bda06c6f57930aec8e79505dc17001", size = 317281 },
    { url = "https://files.pythonhosted.org/packages/f9/39/a3a1571712c2bf6ec4c657f0d66da114a63a2e32b7e4eb8e0b83295ee034/jiter-0.9.0-cp313-cp313t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:062b756ceb1d40b0b28f326cba26cfd575a4918415b036464a52f08632731e5a", size = 350273 },
    { url = "https://files.pythonhosted.org/packages/ee/47/3729f00f35a696e68da15d64eb9283c330e776f3b5789bac7f2c0c4df209/jiter-0.9.0-cp313-cp313t-win_amd64.whl", hash = "sha256:6f7838bc467ab7e8ef9f387bd6de195c43bad82a569c1699cb822f6609dd4cdf", size = 206867 },
    { url = "https://files.pythonhosted.org/packages/aa/2c/9bee940db68d8cefb84178f8b15220c836276db8c6e09cbd422071c01c33/jiter-0.9.0-cp39-cp39-macosx_10_12_x86_64.whl", hash = "sha256:9ef340fae98065071ccd5805fe81c99c8f80484e820e40043689cf97fb66b3e2", size = 315246 },
    { url = "https://files.pythonhosted.org/packages/d0/9b/42d5d59585d9af4fe207e96c6edac2a62bca26d76e2471e78c2f5da28bb8/jiter-0.9.0-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:efb767d92c63b2cd9ec9f24feeb48f49574a713870ec87e9ba0c2c6e9329c3e2", size = 312621 },
    { url = "https://files.pythonhosted.org/packages/2e/a5/a64de757516e5531f8d147a32251905f0e23641738d3520a0a0724fe9651/jiter-0.9.0-cp39-cp39-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:113f30f87fb1f412510c6d7ed13e91422cfd329436364a690c34c8b8bd880c42", size = 343006 },
    { url = "https://files.pythonhosted.org/packages/89/be/08d2bae711200d558ab8c5771f05f47cd09b82b2258a8d6fad0ee2c6a1f3/jiter-0.9.0-cp39-cp39-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:8793b6df019b988526f5a633fdc7456ea75e4a79bd8396a3373c371fc59f5c9b", size = 365099 },
    { url = "https://files.pythonhosted.org/packages/03/9e/d137a0088be90ba5081f7d5d2383374bd77a1447158e44c3ec4e142f902c/jiter-0.9.0-cp39-cp39-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:7a9aaa5102dba4e079bb728076fadd5a2dca94c05c04ce68004cfd96f128ea34", size = 407834 },
    { url = "https://files.pythonhosted.org/packages/04/4c/b6bee52a5b327830abea13eba4222f33f88895a1055eff8870ab3ebbde41/jiter-0.9.0-cp39-cp39-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:d838650f6ebaf4ccadfb04522463e74a4c378d7e667e0eb1865cfe3990bfac49", size = 399255 },
    { url = "https://files.pythonhosted.org/packages/12/b7/364b615a35f99d01cc27d3caea8c3a3ac5451bd5cadf8e5dc4355b102aba/jiter-0.9.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:c0194f813efdf4b8865ad5f5c5f50f8566df7d770a82c51ef593d09e0b347020", size = 354142 },
    { url = "https://files.pythonhosted.org/packages/65/cc/5156f75c496aac65080e2995910104d0e46644df1452c20d963cb904b4b1/jiter-0.9.0-cp39-cp39-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:a7954a401d0a8a0b8bc669199db78af435aae1e3569187c2939c477c53cb6a0a", size = 385142 },
    { url = "https://files.pythonhosted.org/packages/46/cf/370be59c38e56a6fed0308ca266b12d8178b8d6630284cc88ae5af110764/jiter-0.9.0-cp39-cp39-musllinux_1_1_aarch64.whl", hash = "sha256:4feafe787eb8a8d98168ab15637ca2577f6ddf77ac6c8c66242c2d028aa5420e", size = 522035 },
    { url = "https://files.pythonhosted.org/packages/ff/f5/c462d994dcbff43de8a3c953548d609c73a5db8138182408944fce2b68c1/jiter-0.9.0-cp39-cp39-musllinux_1_1_x86_64.whl", hash = "sha256:27cd1f2e8bb377f31d3190b34e4328d280325ad7ef55c6ac9abde72f79e84d2e", size = 513844 },
    { url = "https://files.pythonhosted.org/packages/15/39/60d8f17de27586fa1e7c8215ead8222556d40a6b96b20f1ad70528961f99/jiter-0.9.0-cp39-cp39-win32.whl", hash = "sha256:161d461dcbe658cf0bd0aa375b30a968b087cdddc624fc585f3867c63c6eca95", size = 207147 },
    { url = "https://files.pythonhosted.org/packages/4b/13/c10f17dcddd1b4c1313418e64ace5e77cc4f7313246140fb09044516a62c/jiter-0.9.0-cp39-cp39-win_amd64.whl", hash = "sha256:e8b36d8a16a61993be33e75126ad3d8aa29cf450b09576f3c427d27647fcb4aa", size = 208879 },
]

[[package]]
name = "joblib"
version = "1.4.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/64/33/60135848598c076ce4b231e1b1895170f45fbcaeaa2c9d5e38b04db70c35/joblib-1.4.2.tar.gz", hash = "sha256:2382c5816b2636fbd20a09e0f4e9dad4736765fdfb7dca582943b9c1366b3f0e", size = 2116621 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/91/29/df4b9b42f2be0b623cbd5e2140cafcaa2bef0759a00b7b70104dcfe2fb51/joblib-1.4.2-py3-none-any.whl", hash = "sha256:06d478d5674cbc267e7496a410ee875abd68e4340feff4490bcb7afb88060ae6", size = 301817 },
]

[[package]]
name = "markdown-it-py"
version = "3.0.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "mdurl" },
]
sdist = { url = "https://files.pythonhosted.org/packages/38/71/3b932df36c1a044d397a1f92d1cf91ee0a503d91e470cbd670aa66b07ed0/markdown-it-py-3.0.0.tar.gz", hash = "sha256:e3f60a94fa066dc52ec76661e37c851cb232d92f9886b15cb560aaada2df8feb", size = 74596 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/42/d7/1ec15b46af6af88f19b8e5ffea08fa375d433c998b8a7639e76935c14f1f/markdown_it_py-3.0.0-py3-none-any.whl", hash = "sha256:355216845c60bd96232cd8d8c40e8f9765cc86f46880e43a8fd22dc1a1a8cab1", size = 87528 },
]

[[package]]
name = "markupsafe"
version = "3.0.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/b2/97/5d42485e71dfc078108a86d6de8fa46db44a1a9295e89c5d6d4a06e23a62/markupsafe-3.0.2.tar.gz", hash = "sha256:ee55d3edf80167e48ea11a923c7386f4669df67d7994554387f84e7d8b0a2bf0", size = 20537 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/04/90/d08277ce111dd22f77149fd1a5d4653eeb3b3eaacbdfcbae5afb2600eebd/MarkupSafe-3.0.2-cp310-cp310-macosx_10_9_universal2.whl", hash = "sha256:7e94c425039cde14257288fd61dcfb01963e658efbc0ff54f5306b06054700f8", size = 14357 },
    { url = "https://files.pythonhosted.org/packages/04/e1/6e2194baeae0bca1fae6629dc0cbbb968d4d941469cbab11a3872edff374/MarkupSafe-3.0.2-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:9e2d922824181480953426608b81967de705c3cef4d1af983af849d7bd619158", size = 12393 },
    { url = "https://files.pythonhosted.org/packages/1d/69/35fa85a8ece0a437493dc61ce0bb6d459dcba482c34197e3efc829aa357f/MarkupSafe-3.0.2-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:38a9ef736c01fccdd6600705b09dc574584b89bea478200c5fbf112a6b0d5579", size = 21732 },
    { url = "https://files.pythonhosted.org/packages/22/35/137da042dfb4720b638d2937c38a9c2df83fe32d20e8c8f3185dbfef05f7/MarkupSafe-3.0.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:bbcb445fa71794da8f178f0f6d66789a28d7319071af7a496d4d507ed566270d", size = 20866 },
    { url = "https://files.pythonhosted.org/packages/29/28/6d029a903727a1b62edb51863232152fd335d602def598dade38996887f0/MarkupSafe-3.0.2-cp310-cp310-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:57cb5a3cf367aeb1d316576250f65edec5bb3be939e9247ae594b4bcbc317dfb", size = 20964 },
    { url = "https://files.pythonhosted.org/packages/cc/cd/07438f95f83e8bc028279909d9c9bd39e24149b0d60053a97b2bc4f8aa51/MarkupSafe-3.0.2-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:3809ede931876f5b2ec92eef964286840ed3540dadf803dd570c3b7e13141a3b", size = 21977 },
    { url = "https://files.pythonhosted.org/packages/29/01/84b57395b4cc062f9c4c55ce0df7d3108ca32397299d9df00fedd9117d3d/MarkupSafe-3.0.2-cp310-cp310-musllinux_1_2_i686.whl", hash = "sha256:e07c3764494e3776c602c1e78e298937c3315ccc9043ead7e685b7f2b8d47b3c", size = 21366 },
    { url = "https://files.pythonhosted.org/packages/bd/6e/61ebf08d8940553afff20d1fb1ba7294b6f8d279df9fd0c0db911b4bbcfd/MarkupSafe-3.0.2-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:b424c77b206d63d500bcb69fa55ed8d0e6a3774056bdc4839fc9298a7edca171", size = 21091 },
    { url = "https://files.pythonhosted.org/packages/11/23/ffbf53694e8c94ebd1e7e491de185124277964344733c45481f32ede2499/MarkupSafe-3.0.2-cp310-cp310-win32.whl", hash = "sha256:fcabf5ff6eea076f859677f5f0b6b5c1a51e70a376b0579e0eadef8db48c6b50", size = 15065 },
    { url = "https://files.pythonhosted.org/packages/44/06/e7175d06dd6e9172d4a69a72592cb3f7a996a9c396eee29082826449bbc3/MarkupSafe-3.0.2-cp310-cp310-win_amd64.whl", hash = "sha256:6af100e168aa82a50e186c82875a5893c5597a0c1ccdb0d8b40240b1f28b969a", size = 15514 },
    { url = "https://files.pythonhosted.org/packages/6b/28/bbf83e3f76936960b850435576dd5e67034e200469571be53f69174a2dfd/MarkupSafe-3.0.2-cp311-cp311-macosx_10_9_universal2.whl", hash = "sha256:9025b4018f3a1314059769c7bf15441064b2207cb3f065e6ea1e7359cb46db9d", size = 14353 },
    { url = "https://files.pythonhosted.org/packages/6c/30/316d194b093cde57d448a4c3209f22e3046c5bb2fb0820b118292b334be7/MarkupSafe-3.0.2-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:93335ca3812df2f366e80509ae119189886b0f3c2b81325d39efdb84a1e2ae93", size = 12392 },
    { url = "https://files.pythonhosted.org/packages/f2/96/9cdafba8445d3a53cae530aaf83c38ec64c4d5427d975c974084af5bc5d2/MarkupSafe-3.0.2-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:2cb8438c3cbb25e220c2ab33bb226559e7afb3baec11c4f218ffa7308603c832", size = 23984 },
    { url = "https://files.pythonhosted.org/packages/f1/a4/aefb044a2cd8d7334c8a47d3fb2c9f328ac48cb349468cc31c20b539305f/MarkupSafe-3.0.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:a123e330ef0853c6e822384873bef7507557d8e4a082961e1defa947aa59ba84", size = 23120 },
    { url = "https://files.pythonhosted.org/packages/8d/21/5e4851379f88f3fad1de30361db501300d4f07bcad047d3cb0449fc51f8c/MarkupSafe-3.0.2-cp311-cp311-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:1e084f686b92e5b83186b07e8a17fc09e38fff551f3602b249881fec658d3eca", size = 23032 },
    { url = "https://files.pythonhosted.org/packages/00/7b/e92c64e079b2d0d7ddf69899c98842f3f9a60a1ae72657c89ce2655c999d/MarkupSafe-3.0.2-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:d8213e09c917a951de9d09ecee036d5c7d36cb6cb7dbaece4c71a60d79fb9798", size = 24057 },
    { url = "https://files.pythonhosted.org/packages/f9/ac/46f960ca323037caa0a10662ef97d0a4728e890334fc156b9f9e52bcc4ca/MarkupSafe-3.0.2-cp311-cp311-musllinux_1_2_i686.whl", hash = "sha256:5b02fb34468b6aaa40dfc198d813a641e3a63b98c2b05a16b9f80b7ec314185e", size = 23359 },
    { url = "https://files.pythonhosted.org/packages/69/84/83439e16197337b8b14b6a5b9c2105fff81d42c2a7c5b58ac7b62ee2c3b1/MarkupSafe-3.0.2-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:0bff5e0ae4ef2e1ae4fdf2dfd5b76c75e5c2fa4132d05fc1b0dabcd20c7e28c4", size = 23306 },
    { url = "https://files.pythonhosted.org/packages/9a/34/a15aa69f01e2181ed8d2b685c0d2f6655d5cca2c4db0ddea775e631918cd/MarkupSafe-3.0.2-cp311-cp311-win32.whl", hash = "sha256:6c89876f41da747c8d3677a2b540fb32ef5715f97b66eeb0c6b66f5e3ef6f59d", size = 15094 },
    { url = "https://files.pythonhosted.org/packages/da/b8/3a3bd761922d416f3dc5d00bfbed11f66b1ab89a0c2b6e887240a30b0f6b/MarkupSafe-3.0.2-cp311-cp311-win_amd64.whl", hash = "sha256:70a87b411535ccad5ef2f1df5136506a10775d267e197e4cf531ced10537bd6b", size = 15521 },
    { url = "https://files.pythonhosted.org/packages/22/09/d1f21434c97fc42f09d290cbb6350d44eb12f09cc62c9476effdb33a18aa/MarkupSafe-3.0.2-cp312-cp312-macosx_10_13_universal2.whl", hash = "sha256:9778bd8ab0a994ebf6f84c2b949e65736d5575320a17ae8984a77fab08db94cf", size = 14274 },
    { url = "https://files.pythonhosted.org/packages/6b/b0/18f76bba336fa5aecf79d45dcd6c806c280ec44538b3c13671d49099fdd0/MarkupSafe-3.0.2-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:846ade7b71e3536c4e56b386c2a47adf5741d2d8b94ec9dc3e92e5e1ee1e2225", size = 12348 },
    { url = "https://files.pythonhosted.org/packages/e0/25/dd5c0f6ac1311e9b40f4af06c78efde0f3b5cbf02502f8ef9501294c425b/MarkupSafe-3.0.2-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:1c99d261bd2d5f6b59325c92c73df481e05e57f19837bdca8413b9eac4bd8028", size = 24149 },
    { url = "https://files.pythonhosted.org/packages/f3/f0/89e7aadfb3749d0f52234a0c8c7867877876e0a20b60e2188e9850794c17/MarkupSafe-3.0.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:e17c96c14e19278594aa4841ec148115f9c7615a47382ecb6b82bd8fea3ab0c8", size = 23118 },
    { url = "https://files.pythonhosted.org/packages/d5/da/f2eeb64c723f5e3777bc081da884b414671982008c47dcc1873d81f625b6/MarkupSafe-3.0.2-cp312-cp312-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:88416bd1e65dcea10bc7569faacb2c20ce071dd1f87539ca2ab364bf6231393c", size = 22993 },
    { url = "https://files.pythonhosted.org/packages/da/0e/1f32af846df486dce7c227fe0f2398dc7e2e51d4a370508281f3c1c5cddc/MarkupSafe-3.0.2-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:2181e67807fc2fa785d0592dc2d6206c019b9502410671cc905d132a92866557", size = 24178 },
    { url = "https://files.pythonhosted.org/packages/c4/f6/bb3ca0532de8086cbff5f06d137064c8410d10779c4c127e0e47d17c0b71/MarkupSafe-3.0.2-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:52305740fe773d09cffb16f8ed0427942901f00adedac82ec8b67752f58a1b22", size = 23319 },
    { url = "https://files.pythonhosted.org/packages/a2/82/8be4c96ffee03c5b4a034e60a31294daf481e12c7c43ab8e34a1453ee48b/MarkupSafe-3.0.2-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:ad10d3ded218f1039f11a75f8091880239651b52e9bb592ca27de44eed242a48", size = 23352 },
    { url = "https://files.pythonhosted.org/packages/51/ae/97827349d3fcffee7e184bdf7f41cd6b88d9919c80f0263ba7acd1bbcb18/MarkupSafe-3.0.2-cp312-cp312-win32.whl", hash = "sha256:0f4ca02bea9a23221c0182836703cbf8930c5e9454bacce27e767509fa286a30", size = 15097 },
    { url = "https://files.pythonhosted.org/packages/c1/80/a61f99dc3a936413c3ee4e1eecac96c0da5ed07ad56fd975f1a9da5bc630/MarkupSafe-3.0.2-cp312-cp312-win_amd64.whl", hash = "sha256:8e06879fc22a25ca47312fbe7c8264eb0b662f6db27cb2d3bbbc74b1df4b9b87", size = 15601 },
    { url = "https://files.pythonhosted.org/packages/83/0e/67eb10a7ecc77a0c2bbe2b0235765b98d164d81600746914bebada795e97/MarkupSafe-3.0.2-cp313-cp313-macosx_10_13_universal2.whl", hash = "sha256:ba9527cdd4c926ed0760bc301f6728ef34d841f405abf9d4f959c478421e4efd", size = 14274 },
    { url = "https://files.pythonhosted.org/packages/2b/6d/9409f3684d3335375d04e5f05744dfe7e9f120062c9857df4ab490a1031a/MarkupSafe-3.0.2-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:f8b3d067f2e40fe93e1ccdd6b2e1d16c43140e76f02fb1319a05cf2b79d99430", size = 12352 },
    { url = "https://files.pythonhosted.org/packages/d2/f5/6eadfcd3885ea85fe2a7c128315cc1bb7241e1987443d78c8fe712d03091/MarkupSafe-3.0.2-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:569511d3b58c8791ab4c2e1285575265991e6d8f8700c7be0e88f86cb0672094", size = 24122 },
    { url = "https://files.pythonhosted.org/packages/0c/91/96cf928db8236f1bfab6ce15ad070dfdd02ed88261c2afafd4b43575e9e9/MarkupSafe-3.0.2-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:15ab75ef81add55874e7ab7055e9c397312385bd9ced94920f2802310c930396", size = 23085 },
    { url = "https://files.pythonhosted.org/packages/c2/cf/c9d56af24d56ea04daae7ac0940232d31d5a8354f2b457c6d856b2057d69/MarkupSafe-3.0.2-cp313-cp313-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:f3818cb119498c0678015754eba762e0d61e5b52d34c8b13d770f0719f7b1d79", size = 22978 },
    { url = "https://files.pythonhosted.org/packages/2a/9f/8619835cd6a711d6272d62abb78c033bda638fdc54c4e7f4272cf1c0962b/MarkupSafe-3.0.2-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:cdb82a876c47801bb54a690c5ae105a46b392ac6099881cdfb9f6e95e4014c6a", size = 24208 },
    { url = "https://files.pythonhosted.org/packages/f9/bf/176950a1792b2cd2102b8ffeb5133e1ed984547b75db47c25a67d3359f77/MarkupSafe-3.0.2-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:cabc348d87e913db6ab4aa100f01b08f481097838bdddf7c7a84b7575b7309ca", size = 23357 },
    { url = "https://files.pythonhosted.org/packages/ce/4f/9a02c1d335caabe5c4efb90e1b6e8ee944aa245c1aaaab8e8a618987d816/MarkupSafe-3.0.2-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:444dcda765c8a838eaae23112db52f1efaf750daddb2d9ca300bcae1039adc5c", size = 23344 },
    { url = "https://files.pythonhosted.org/packages/ee/55/c271b57db36f748f0e04a759ace9f8f759ccf22b4960c270c78a394f58be/MarkupSafe-3.0.2-cp313-cp313-win32.whl", hash = "sha256:bcf3e58998965654fdaff38e58584d8937aa3096ab5354d493c77d1fdd66d7a1", size = 15101 },
    { url = "https://files.pythonhosted.org/packages/29/88/07df22d2dd4df40aba9f3e402e6dc1b8ee86297dddbad4872bd5e7b0094f/MarkupSafe-3.0.2-cp313-cp313-win_amd64.whl", hash = "sha256:e6a2a455bd412959b57a172ce6328d2dd1f01cb2135efda2e4576e8a23fa3b0f", size = 15603 },
    { url = "https://files.pythonhosted.org/packages/62/6a/8b89d24db2d32d433dffcd6a8779159da109842434f1dd2f6e71f32f738c/MarkupSafe-3.0.2-cp313-cp313t-macosx_10_13_universal2.whl", hash = "sha256:b5a6b3ada725cea8a5e634536b1b01c30bcdcd7f9c6fff4151548d5bf6b3a36c", size = 14510 },
    { url = "https://files.pythonhosted.org/packages/7a/06/a10f955f70a2e5a9bf78d11a161029d278eeacbd35ef806c3fd17b13060d/MarkupSafe-3.0.2-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:a904af0a6162c73e3edcb969eeeb53a63ceeb5d8cf642fade7d39e7963a22ddb", size = 12486 },
    { url = "https://files.pythonhosted.org/packages/34/cf/65d4a571869a1a9078198ca28f39fba5fbb910f952f9dbc5220afff9f5e6/MarkupSafe-3.0.2-cp313-cp313t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:4aa4e5faecf353ed117801a068ebab7b7e09ffb6e1d5e412dc852e0da018126c", size = 25480 },
    { url = "https://files.pythonhosted.org/packages/0c/e3/90e9651924c430b885468b56b3d597cabf6d72be4b24a0acd1fa0e12af67/MarkupSafe-3.0.2-cp313-cp313t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:c0ef13eaeee5b615fb07c9a7dadb38eac06a0608b41570d8ade51c56539e509d", size = 23914 },
    { url = "https://files.pythonhosted.org/packages/66/8c/6c7cf61f95d63bb866db39085150df1f2a5bd3335298f14a66b48e92659c/MarkupSafe-3.0.2-cp313-cp313t-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:d16a81a06776313e817c951135cf7340a3e91e8c1ff2fac444cfd75fffa04afe", size = 23796 },
    { url = "https://files.pythonhosted.org/packages/bb/35/cbe9238ec3f47ac9a7c8b3df7a808e7cb50fe149dc7039f5f454b3fba218/MarkupSafe-3.0.2-cp313-cp313t-musllinux_1_2_aarch64.whl", hash = "sha256:6381026f158fdb7c72a168278597a5e3a5222e83ea18f543112b2662a9b699c5", size = 25473 },
    { url = "https://files.pythonhosted.org/packages/e6/32/7621a4382488aa283cc05e8984a9c219abad3bca087be9ec77e89939ded9/MarkupSafe-3.0.2-cp313-cp313t-musllinux_1_2_i686.whl", hash = "sha256:3d79d162e7be8f996986c064d1c7c817f6df3a77fe3d6859f6f9e7be4b8c213a", size = 24114 },
    { url = "https://files.pythonhosted.org/packages/0d/80/0985960e4b89922cb5a0bac0ed39c5b96cbc1a536a99f30e8c220a996ed9/MarkupSafe-3.0.2-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:131a3c7689c85f5ad20f9f6fb1b866f402c445b220c19fe4308c0b147ccd2ad9", size = 24098 },
    { url = "https://files.pythonhosted.org/packages/82/78/fedb03c7d5380df2427038ec8d973587e90561b2d90cd472ce9254cf348b/MarkupSafe-3.0.2-cp313-cp313t-win32.whl", hash = "sha256:ba8062ed2cf21c07a9e295d5b8a2a5ce678b913b45fdf68c32d95d6c1291e0b6", size = 15208 },
    { url = "https://files.pythonhosted.org/packages/4f/65/6079a46068dfceaeabb5dcad6d674f5f5c61a6fa5673746f42a9f4c233b3/MarkupSafe-3.0.2-cp313-cp313t-win_amd64.whl", hash = "sha256:e444a31f8db13eb18ada366ab3cf45fd4b31e4db1236a4448f68778c1d1a5a2f", size = 15739 },
    { url = "https://files.pythonhosted.org/packages/a7/ea/9b1530c3fdeeca613faeb0fb5cbcf2389d816072fab72a71b45749ef6062/MarkupSafe-3.0.2-cp39-cp39-macosx_10_9_universal2.whl", hash = "sha256:eaa0a10b7f72326f1372a713e73c3f739b524b3af41feb43e4921cb529f5929a", size = 14344 },
    { url = "https://files.pythonhosted.org/packages/4b/c2/fbdbfe48848e7112ab05e627e718e854d20192b674952d9042ebd8c9e5de/MarkupSafe-3.0.2-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:48032821bbdf20f5799ff537c7ac3d1fba0ba032cfc06194faffa8cda8b560ff", size = 12389 },
    { url = "https://files.pythonhosted.org/packages/f0/25/7a7c6e4dbd4f867d95d94ca15449e91e52856f6ed1905d58ef1de5e211d0/MarkupSafe-3.0.2-cp39-cp39-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:1a9d3f5f0901fdec14d8d2f66ef7d035f2157240a433441719ac9a3fba440b13", size = 21607 },
    { url = "https://files.pythonhosted.org/packages/53/8f/f339c98a178f3c1e545622206b40986a4c3307fe39f70ccd3d9df9a9e425/MarkupSafe-3.0.2-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:88b49a3b9ff31e19998750c38e030fc7bb937398b1f78cfa599aaef92d693144", size = 20728 },
    { url = "https://files.pythonhosted.org/packages/1a/03/8496a1a78308456dbd50b23a385c69b41f2e9661c67ea1329849a598a8f9/MarkupSafe-3.0.2-cp39-cp39-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:cfad01eed2c2e0c01fd0ecd2ef42c492f7f93902e39a42fc9ee1692961443a29", size = 20826 },
    { url = "https://files.pythonhosted.org/packages/e6/cf/0a490a4bd363048c3022f2f475c8c05582179bb179defcee4766fb3dcc18/MarkupSafe-3.0.2-cp39-cp39-musllinux_1_2_aarch64.whl", hash = "sha256:1225beacc926f536dc82e45f8a4d68502949dc67eea90eab715dea3a21c1b5f0", size = 21843 },
    { url = "https://files.pythonhosted.org/packages/19/a3/34187a78613920dfd3cdf68ef6ce5e99c4f3417f035694074beb8848cd77/MarkupSafe-3.0.2-cp39-cp39-musllinux_1_2_i686.whl", hash = "sha256:3169b1eefae027567d1ce6ee7cae382c57fe26e82775f460f0b2778beaad66c0", size = 21219 },
    { url = "https://files.pythonhosted.org/packages/17/d8/5811082f85bb88410ad7e452263af048d685669bbbfb7b595e8689152498/MarkupSafe-3.0.2-cp39-cp39-musllinux_1_2_x86_64.whl", hash = "sha256:eb7972a85c54febfb25b5c4b4f3af4dcc731994c7da0d8a0b4a6eb0640e1d178", size = 20946 },
    { url = "https://files.pythonhosted.org/packages/7c/31/bd635fb5989440d9365c5e3c47556cfea121c7803f5034ac843e8f37c2f2/MarkupSafe-3.0.2-cp39-cp39-win32.whl", hash = "sha256:8c4e8c3ce11e1f92f6536ff07154f9d49677ebaaafc32db9db4620bc11ed480f", size = 15063 },
    { url = "https://files.pythonhosted.org/packages/b3/73/085399401383ce949f727afec55ec3abd76648d04b9f22e1c0e99cb4bec3/MarkupSafe-3.0.2-cp39-cp39-win_amd64.whl", hash = "sha256:6e296a513ca3d94054c2c881cc913116e90fd030ad1c656b3869762b754f5f8a", size = 15506 },
]

[[package]]
name = "mdurl"
version = "0.1.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/d6/54/cfe61301667036ec958cb99bd3efefba235e65cdeb9c84d24a8293ba1d90/mdurl-0.1.2.tar.gz", hash = "sha256:bb413d29f5eea38f31dd4754dd7377d4465116fb207585f97bf925588687c1ba", size = 8729 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/b3/38/89ba8ad64ae25be8de66a6d463314cf1eb366222074cfda9ee839c56a4b4/mdurl-0.1.2-py3-none-any.whl", hash = "sha256:84008a41e51615a49fc9966191ff91509e3c40b939176e643fd50a5c2196b8f8", size = 9979 },
]

[[package]]
name = "model2vec"
version = "0.4.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "jinja2" },
    { name = "joblib" },
    { name = "numpy" },
    { name = "rich" },
    { name = "safetensors" },
    { name = "setuptools" },
    { name = "tokenizers" },
    { name = "tqdm" },
]
sdist = { url = "https://files.pythonhosted.org/packages/b8/c1/3cd6cab10e8b7da8c32acebf85672d38a26f5f03165bfeaa617a5ec0bb61/model2vec-0.4.1.tar.gz", hash = "sha256:fc6038416679eebe448951708f2d0bebdee8510f47970af1c81a8f054a3c3f9f", size = 2660626 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/cd/76/c8575f90f521017597c5e57e3bfef61e3f27d9cb6c741a82a24d72b10a60/model2vec-0.4.1-py3-none-any.whl", hash = "sha256:04a397a17da9b967082b6baa4c494f0be48c89ec4e1a3975b4f290f045238a38", size = 41972 },
]

[[package]]
name = "mpmath"
version = "1.3.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/e0/47/dd32fa426cc72114383ac549964eecb20ecfd886d1e5ccf5340b55b02f57/mpmath-1.3.0.tar.gz", hash = "sha256:7a28eb2a9774d00c7bc92411c19a89209d5da7c4c9a9e227be8330a23a25b91f", size = 508106 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/43/e3/7d92a15f894aa0c9c4b49b8ee9ac9850d6e63b03c9c32c0367a13ae62209/mpmath-1.3.0-py3-none-any.whl", hash = "sha256:a0b2b9fe80bbcd81a6647ff13108738cfb482d481d826cc0e02f5b35e5c88d2c", size = 536198 },
]

[[package]]
name = "multidict"
version = "6.3.2"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "typing-extensions", marker = "python_full_version < '3.11'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/fa/2d/6e0d6771cadd5ad14d13193cc8326dc0b341cc1659c306cbfce7a5058fff/multidict-6.3.2.tar.gz", hash = "sha256:c1035eea471f759fa853dd6e76aaa1e389f93b3e1403093fa0fd3ab4db490678", size = 88060 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/4e/9f/96bed056ed3e1fa86fa9880963e21a098e1e94dc6e2ced51a960d56ed802/multidict-6.3.2-cp310-cp310-macosx_10_9_universal2.whl", hash = "sha256:8b3dc0eec9304fa04d84a51ea13b0ec170bace5b7ddeaac748149efd316f1504", size = 62769 },
    { url = "https://files.pythonhosted.org/packages/69/6a/c3197d0ff579d2393bab259c6129c963ebec50014fbd757440645402b4c0/multidict-6.3.2-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:9534f3d84addd3b6018fa83f97c9d4247aaa94ac917d1ed7b2523306f99f5c16", size = 37127 },
    { url = "https://files.pythonhosted.org/packages/a6/d8/21b15813270d56486041452a44b02b4c02cd492edb8eb13c3ce1de7744f1/multidict-6.3.2-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:a003ce1413ae01f0b8789c1c987991346a94620a4d22210f7a8fe753646d3209", size = 36399 },
    { url = "https://files.pythonhosted.org/packages/8f/f6/2ffe2d4b565551bf0b1b1e9630c6f21f728fc24cd7d880f1baf5e7025be3/multidict-6.3.2-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:5b43f7384e68b1b982c99f489921a459467b5584bdb963b25e0df57c9039d0ad", size = 236561 },
    { url = "https://files.pythonhosted.org/packages/c4/d7/935810c224360c63fe3b9233433ea9197399431e362e38ff0daf082624ee/multidict-6.3.2-cp310-cp310-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:d142ae84047262dc75c1f92eaf95b20680f85ce11d35571b4c97e267f96fadc4", size = 249850 },
    { url = "https://files.pythonhosted.org/packages/d0/10/355802a51e4426354b645585a9f0a4a4f0352b7619251da152f0235069ed/multidict-6.3.2-cp310-cp310-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:ec7e86fbc48aa1d6d686501a8547818ba8d645e7e40eaa98232a5d43ee4380ad", size = 245566 },
    { url = "https://files.pythonhosted.org/packages/72/cb/2a2b44b207c05018d0909b7c748983753dc9587699664e10709e27605158/multidict-6.3.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:fe019fb437632b016e6cac67a7e964f1ef827ef4023f1ca0227b54be354da97e", size = 232030 },
    { url = "https://files.pythonhosted.org/packages/8e/e5/3db1745e939f4c02275154a5ed2816ea70eb1625e1d9363881047a0f9620/multidict-6.3.2-cp310-cp310-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:2b60cb81214a9da7cfd8ae2853d5e6e47225ece55fe5833142fe0af321c35299", size = 224255 },
    { url = "https://files.pythonhosted.org/packages/48/2d/f187f506ff5ee3a91a8207a744311649cb1541b180514ea9dc235747ac2a/multidict-6.3.2-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:32d9e8ef2e0312d4e96ca9adc88e0675b6d8e144349efce4a7c95d5ccb6d88e0", size = 233961 },
    { url = "https://files.pythonhosted.org/packages/8f/e3/5023396bb5f1858f897d1a44199d0abc3072bb7b7bb47dec94c10b535568/multidict-6.3.2-cp310-cp310-musllinux_1_2_i686.whl", hash = "sha256:335d584312e3fa43633d63175dfc1a5f137dd7aa03d38d1310237d54c3032774", size = 232430 },
    { url = "https://files.pythonhosted.org/packages/73/d8/f7b80e886af062dbb9d517e5161d841a08bcf44f6bccfccf9cb0ba92e7de/multidict-6.3.2-cp310-cp310-musllinux_1_2_ppc64le.whl", hash = "sha256:b8df917faa6b8cac3d6870fc21cb7e4d169faca68e43ffe568c156c9c6408a4d", size = 243102 },
    { url = "https://files.pythonhosted.org/packages/53/a5/78e3c05c1916ce3e7beca8da8a026c1a4d9e4ce892f472463be22ddd030d/multidict-6.3.2-cp310-cp310-musllinux_1_2_s390x.whl", hash = "sha256:cc060b9b89b701dd8fedef5b99e1f1002b8cb95072693233a63389d37e48212d", size = 235610 },
    { url = "https://files.pythonhosted.org/packages/00/29/97b470984a545d09bc5b6b8534559c48d4c427bd6737dc5a6f516061a581/multidict-6.3.2-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:f2ce3be2500658f3c644494b934628bb0c82e549dde250d2119689ce791cc8b8", size = 232287 },
    { url = "https://files.pythonhosted.org/packages/78/a5/121d40559fceb8d78ffe38ee06519fba8c8300ef1eb796c0a790fa0cfbf3/multidict-6.3.2-cp310-cp310-win32.whl", hash = "sha256:dbcb4490d8e74b484449abd51751b8f560dd0a4812eb5dacc6a588498222a9ab", size = 34895 },
    { url = "https://files.pythonhosted.org/packages/04/b1/e90e666158b2c65567f8bb2c1507e9983c4b1b7156cd67e69349a38bd2b2/multidict-6.3.2-cp310-cp310-win_amd64.whl", hash = "sha256:06944f9ced30f8602be873563ed4df7e3f40958f60b2db39732c11d615a33687", size = 38307 },
    { url = "https://files.pythonhosted.org/packages/b1/e3/443e682e42eaddad0b217b7a59627927fa42b6cd7ba7174f0a01eb3fe6b8/multidict-6.3.2-cp311-cp311-macosx_10_9_universal2.whl", hash = "sha256:45a034f41fcd16968c0470d8912d293d7b0d0822fc25739c5c2ff7835b85bc56", size = 62734 },
    { url = "https://files.pythonhosted.org/packages/b1/4f/2126e9bc37f5be2fdfa36cc192e7ef10b3e9c58eec75a4468706aca96891/multidict-6.3.2-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:352585cec45f5d83d886fc522955492bb436fca032b11d487b12d31c5a81b9e3", size = 37115 },
    { url = "https://files.pythonhosted.org/packages/6a/af/5aae0c05a66fdf8bf015ee6903d3a250a7d9c6cc75c9478d04995e6ff1e2/multidict-6.3.2-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:da9d89d293511fd0a83a90559dc131f8b3292b6975eb80feff19e5f4663647e2", size = 36371 },
    { url = "https://files.pythonhosted.org/packages/94/27/42390b75c20ff63f43fce44f36f9f66be466cd9ee05326051e4caacdb75b/multidict-6.3.2-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:79fa716592224aa652b9347a586cfe018635229074565663894eb4eb21f8307f", size = 243444 },
    { url = "https://files.pythonhosted.org/packages/21/55/77077af851d7678fe0845c4050a537321d82fb12a04d4f6db334a1cc6ff7/multidict-6.3.2-cp311-cp311-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:0326278a44c56e94792475268e5cd3d47fbc0bd41ee56928c3bbb103ba7f58fe", size = 256750 },
    { url = "https://files.pythonhosted.org/packages/f1/09/4c5bfeb2fc8a1e14002239bd6a4d9ba2963fb148889d444b05a20db32a41/multidict-6.3.2-cp311-cp311-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:bb1ea87f7fe45e5079f6315e95d64d4ca8b43ef656d98bed63a02e3756853a22", size = 251630 },
    { url = "https://files.pythonhosted.org/packages/24/a9/286756a1afb8648772de851f8f39d2dd4076506f0c0fc2b751259fcbf0dd/multidict-6.3.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:7cff3c5a98d037024a9065aafc621a8599fad7b423393685dc83cf7a32f8b691", size = 238522 },
    { url = "https://files.pythonhosted.org/packages/c2/03/4bb17df70742aae786fcbc27e89e2e49c322134698cd0739aec93e91c669/multidict-6.3.2-cp311-cp311-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:ed99834b053c655d980fb98029003cb24281e47a796052faad4543aa9e01b8e8", size = 230230 },
    { url = "https://files.pythonhosted.org/packages/53/cc/30df95ba07a9f233ae48d0605b3f72457364836b61a8a8e3d333fdcd32c0/multidict-6.3.2-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:7048440e505d2b4741e5d0b32bd2f427c901f38c7760fc245918be2cf69b3b85", size = 239676 },
    { url = "https://files.pythonhosted.org/packages/25/37/2d9fe2944c2df5b71ba90cf657b90ad65f1542989cdabe4d1bdbf8c51530/multidict-6.3.2-cp311-cp311-musllinux_1_2_i686.whl", hash = "sha256:27248c27b563f5889556da8a96e18e98a56ff807ac1a7d56cf4453c2c9e4cd91", size = 238143 },
    { url = "https://files.pythonhosted.org/packages/ce/13/8f833f9f992eae49f4cb1a1ad05b8fbe183721a154d51c2136b177a41bdb/multidict-6.3.2-cp311-cp311-musllinux_1_2_ppc64le.whl", hash = "sha256:6323b4ba0e018bd266f776c35f3f0943fc4ee77e481593c9f93bd49888f24e94", size = 248817 },
    { url = "https://files.pythonhosted.org/packages/15/d4/4f49c41af6c4cab962ad51436e6c5acfbdab4fa54f5e98faa56f66f89b03/multidict-6.3.2-cp311-cp311-musllinux_1_2_s390x.whl", hash = "sha256:81f7ce5ec7c27d0b45c10449c8f0fed192b93251e2e98cb0b21fec779ef1dc4d", size = 241268 },
    { url = "https://files.pythonhosted.org/packages/af/60/e723a00f7bb44366eab8d02fe6f076ecfad58331e10f6f0ce94cb989819c/multidict-6.3.2-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:03bfcf2825b3bed0ba08a9d854acd18b938cab0d2dba3372b51c78e496bac811", size = 238267 },
    { url = "https://files.pythonhosted.org/packages/62/a6/f6b63fc51c8a4e228e6d2105061be3048b02d490d47e67f7ec2de575f1d0/multidict-6.3.2-cp311-cp311-win32.whl", hash = "sha256:f32c2790512cae6ca886920e58cdc8c784bdc4bb2a5ec74127c71980369d18dc", size = 34986 },
    { url = "https://files.pythonhosted.org/packages/85/56/ea976a5e3ebe0e871e004d9cacfe4c803f8ade353eaf4a247580e9dd7b9d/multidict-6.3.2-cp311-cp311-win_amd64.whl", hash = "sha256:0b0c15e58e038a2cd75ef7cf7e072bc39b5e0488b165902efb27978984bbad70", size = 38427 },
    { url = "https://files.pythonhosted.org/packages/83/ae/bd7518193b4374484c04ba0f6522d0572dc17fcd53d238deb3cb3643c858/multidict-6.3.2-cp312-cp312-macosx_10_13_universal2.whl", hash = "sha256:d1e0ba1ce1b8cc79117196642d95f4365e118eaf5fb85f57cdbcc5a25640b2a4", size = 62680 },
    { url = "https://files.pythonhosted.org/packages/59/e0/a0a9247c32f385ac4c1afefe9c3f2271fb8e235aad72332d42384c41b9cb/multidict-6.3.2-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:029bbd7d782251a78975214b78ee632672310f9233d49531fc93e8e99154af25", size = 37366 },
    { url = "https://files.pythonhosted.org/packages/c3/fa/8c23cdd4492d59bea0e762662285f2163766e69e5ea715fe6a03a8670660/multidict-6.3.2-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:d7db41e3b56817d9175264e5fe00192fbcb8e1265307a59f53dede86161b150e", size = 36103 },
    { url = "https://files.pythonhosted.org/packages/87/35/3bcc3616cb54d3a327b1d26dbec284c3eb7b179e8a78a6075852dbb51dac/multidict-6.3.2-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:1fcab18e65cc555ac29981a581518c23311f2b1e72d8f658f9891590465383be", size = 248231 },
    { url = "https://files.pythonhosted.org/packages/b8/c3/17ddbfd6fc3eed9ab7326a43651e1a97da73f7acc69b78a7bb04b59c073d/multidict-6.3.2-cp312-cp312-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:0d50eff89aa4d145a5486b171a2177042d08ea5105f813027eb1050abe91839f", size = 259423 },
    { url = "https://files.pythonhosted.org/packages/1f/67/64b18180e8f559cc93efaaaac2fe0746b9c978560866b6fdd626d3237129/multidict-6.3.2-cp312-cp312-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:643e57b403d3e240045a3681f9e6a04d35a33eddc501b4cbbbdbc9c70122e7bc", size = 256204 },
    { url = "https://files.pythonhosted.org/packages/21/f6/e81a8e4817c2d32787b33ae58c72dc3fe08e0ba8e56e660a225df3cb8619/multidict-6.3.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:9d17b37b9715b30605b5bab1460569742d0c309e5c20079263b440f5d7746e7e", size = 249663 },
    { url = "https://files.pythonhosted.org/packages/3e/e8/44ca66758df031a8119483cf5385e2ff3b09b9c6df8f3396d626c325b553/multidict-6.3.2-cp312-cp312-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:68acd51fa94e63312b8ddf84bfc9c3d3442fe1f9988bbe1b6c703043af8867fe", size = 232236 },
    { url = "https://files.pythonhosted.org/packages/93/76/d2faabbac582dc100a4d7ecf7d0ab8dd2aadf7f10d5d5a19e9932cf63a2e/multidict-6.3.2-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:347eea2852ab7f697cc5ed9b1aae96b08f8529cca0c6468f747f0781b1842898", size = 252638 },
    { url = "https://files.pythonhosted.org/packages/63/37/f5a6ea10dab96491b7300be940f86a5490dc474d18473c438f2550b78da3/multidict-6.3.2-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:e4d3f8e57027dcda84a1aa181501c15c45eab9566eb6fcc274cbd1e7561224f8", size = 247917 },
    { url = "https://files.pythonhosted.org/packages/d4/b1/2c32b684763b69becbaaa61b7af8a45a6f757fc82d9b4b123ca90cb69f75/multidict-6.3.2-cp312-cp312-musllinux_1_2_ppc64le.whl", hash = "sha256:9ca57a841ffcf712e47875d026aa49d6e67f9560624d54b51628603700d5d287", size = 261754 },
    { url = "https://files.pythonhosted.org/packages/cd/f2/badedad94e1731debe56d076c9e61a1658c5e9d65dfa9c1ee74d1e3d31d7/multidict-6.3.2-cp312-cp312-musllinux_1_2_s390x.whl", hash = "sha256:7cafdafb44c4e646118410368307693e49d19167e5f119cbe3a88697d2d1a636", size = 256389 },
    { url = "https://files.pythonhosted.org/packages/c6/3a/0a3488be2e5a6499f512e748d31e8fb90b753eb35793ecf390b9d8548e66/multidict-6.3.2-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:430120c6ce3715a9c6075cabcee557daccbcca8ba25a9fedf05c7bf564532f2d", size = 251902 },
    { url = "https://files.pythonhosted.org/packages/fe/44/62f76d0a5d836b96168f39a402a75dd3114d0df3cbb5669e0310034b71be/multidict-6.3.2-cp312-cp312-win32.whl", hash = "sha256:13bec31375235a68457ab887ce1bbf4f59d5810d838ae5d7e5b416242e1f3ed4", size = 35101 },
    { url = "https://files.pythonhosted.org/packages/8f/a4/7aaf2313e1766710010c35f9d738fd6309fb71a758f8c0e81853b90afb3d/multidict-6.3.2-cp312-cp312-win_amd64.whl", hash = "sha256:c3b6d7620e6e90c6d97eaf3a63bf7fbd2ba253aab89120a4a9c660bf2d675391", size = 38479 },
    { url = "https://files.pythonhosted.org/packages/b1/b2/15db2b1bec1fe8ab5e7c210e3cd247ed902ef86b58b9f39b0a75476d0e8d/multidict-6.3.2-cp313-cp313-macosx_10_13_universal2.whl", hash = "sha256:b9ca24700322816ae0d426aa33671cf68242f8cc85cee0d0e936465ddaee90b5", size = 62345 },
    { url = "https://files.pythonhosted.org/packages/5f/91/22ea27da2c3ffb8266a92f91f17a84dec2cbdd0f91aa7e5f7d514534dd92/multidict-6.3.2-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:d9fbbe23667d596ff4f9f74d44b06e40ebb0ab6b262cf14a284f859a66f86457", size = 37205 },
    { url = "https://files.pythonhosted.org/packages/23/cb/563a7481ae677531da84aad86c2de7ebc23446d856d2f6d9794ad4fff375/multidict-6.3.2-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:9cb602c5bea0589570ad3a4a6f2649c4f13cc7a1e97b4c616e5e9ff8dc490987", size = 35931 },
    { url = "https://files.pythonhosted.org/packages/7c/b7/98fe4f4cd7a0b77a4a48fd3f619848b9e8af4e692eb681f9df9f58d86456/multidict-6.3.2-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:93ca81dd4d1542e20000ed90f4cc84b7713776f620d04c2b75b8efbe61106c99", size = 246946 },
    { url = "https://files.pythonhosted.org/packages/7e/a3/22dcbd0b58d253719acaf0257a2f35bf609bfd6b73690fcc9e7bdbd3b392/multidict-6.3.2-cp313-cp313-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:18b6310b5454c62242577a128c87df8897f39dd913311cf2e1298e47dfc089eb", size = 260559 },
    { url = "https://files.pythonhosted.org/packages/1c/d4/25eb076f0c2c28d73e7959f3fcc8371e7a029815b5d06e79ea3a265500d2/multidict-6.3.2-cp313-cp313-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:7a6dda57de1fc9aedfdb600a8640c99385cdab59a5716cb714b52b6005797f77", size = 257122 },
    { url = "https://files.pythonhosted.org/packages/28/f8/18c81f5c5b7453dd8d15dc61ceca23d03c55e69f1937842039be2d8c4428/multidict-6.3.2-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:5d8ec42d03cc6b29845552a68151f9e623c541f1708328353220af571e24a247", size = 248535 },
    { url = "https://files.pythonhosted.org/packages/9b/17/c175fab75ecfe1c2dd4f28382dd7e80da6d6f0d73c68036f64b6dce9aeeb/multidict-6.3.2-cp313-cp313-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:80681969cee2fa84dafeb53615d51d24246849984e3e87fbe4fe39956f2e23bf", size = 234013 },
    { url = "https://files.pythonhosted.org/packages/2f/03/1611ecf91d7d6249633cb1dd3fb26d456e0dc0dc80cecccfeb89931a126b/multidict-6.3.2-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:01489b0c3592bb9d238e5690e9566db7f77a5380f054b57077d2c4deeaade0eb", size = 249222 },
    { url = "https://files.pythonhosted.org/packages/66/04/0035b77bbffb55f276f00b427e45870194002f9f42e1e3de785d45880372/multidict-6.3.2-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:522d9f1fd995d04dfedc0a40bca7e2591bc577d920079df50b56245a4a252c1c", size = 245594 },
    { url = "https://files.pythonhosted.org/packages/fe/4c/b52ebcd8ff13a3c833b07cfffa0f50f736b061954a151ee5fe6669bb1bd8/multidict-6.3.2-cp313-cp313-musllinux_1_2_ppc64le.whl", hash = "sha256:2014e9cf0b4e9c75bbad49c1758e5a9bf967a56184fc5fcc51527425baf5abba", size = 258709 },
    { url = "https://files.pythonhosted.org/packages/fd/78/9c4433517e8f09035a14aba469617c9cf41a214ca987d9127b84b3de4848/multidict-6.3.2-cp313-cp313-musllinux_1_2_s390x.whl", hash = "sha256:78ced9fcbee79e446ff4bb3018ac7ba1670703de7873d9c1f6f9883db53c71bc", size = 254015 },
    { url = "https://files.pythonhosted.org/packages/6d/76/8464b4d2e9980bd754aa1850919caef9854453f0400c60f84c79947b799d/multidict-6.3.2-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:1faf01af972bd01216a107c195f5294f9f393531bc3e4faddc9b333581255d4d", size = 249475 },
    { url = "https://files.pythonhosted.org/packages/c4/e2/2b35b7ce226a2ca8c38125f702090faa8d0a35050461fb111fbaa2e023c4/multidict-6.3.2-cp313-cp313-win32.whl", hash = "sha256:7a699ab13d8d8e1f885de1535b4f477fb93836c87168318244c2685da7b7f655", size = 35204 },
    { url = "https://files.pythonhosted.org/packages/c6/c7/09b85dc11cfa83c9a1e3f8367402d56157624e31a05eecd40d5feed1eed1/multidict-6.3.2-cp313-cp313-win_amd64.whl", hash = "sha256:8666bb0d883310c83be01676e302587834dfd185b52758caeab32ef0eb387bc6", size = 38436 },
    { url = "https://files.pythonhosted.org/packages/63/d6/b27f9db9a8dcca95b50911436c9f187047911be0d78ade3352a6bcabb87a/multidict-6.3.2-cp313-cp313t-macosx_10_13_universal2.whl", hash = "sha256:d82c95aabee29612b1c4f48b98be98181686eb7d6c0152301f72715705cc787b", size = 67526 },
    { url = "https://files.pythonhosted.org/packages/2d/23/bbf220b0fa6378526890f37fd9a63d4e2ea990a4a344b221618adc3fb8b0/multidict-6.3.2-cp313-cp313t-macosx_10_13_x86_64.whl", hash = "sha256:f47709173ea9e87a7fd05cd7e5cf1e5d4158924ff988a9a8e0fbd853705f0e68", size = 39390 },
    { url = "https://files.pythonhosted.org/packages/0d/a9/4d1b795b50e6b54609fd7a63db8df30fa0480405b9a46cf8e336f5f28560/multidict-6.3.2-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:0c7f9d0276ceaab41b8ae78534ff28ea33d5de85db551cbf80c44371f2b55d13", size = 38869 },
    { url = "https://files.pythonhosted.org/packages/e4/8c/854ee8ad8921335d0b4e740f373390d85d23f6b3956387562de5891ac503/multidict-6.3.2-cp313-cp313t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:a6eab22df44a25acab2e738f882f5ec551282ab45b2bbda5301e6d2cfb323036", size = 246911 },
    { url = "https://files.pythonhosted.org/packages/40/65/d6ae9fecb61d1c2fa86a2889f8b58dbfb91fa6a6d7754597e472c8523f6c/multidict-6.3.2-cp313-cp313t-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:a947cb7c657f57874021b9b70c7aac049c877fb576955a40afa8df71d01a1390", size = 251680 },
    { url = "https://files.pythonhosted.org/packages/a3/6c/098304889a699f5fbad8e74b723847a38d22547743baacdfcc8a17777b5b/multidict-6.3.2-cp313-cp313t-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:5faa346e8e1c371187cf345ab1e02a75889f9f510c9cbc575c31b779f7df084d", size = 246706 },
    { url = "https://files.pythonhosted.org/packages/da/9f/a58a04ac1d18f0a2431c48763a8948d0ce65f5911000cc425f8778eb6611/multidict-6.3.2-cp313-cp313t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:dc6e08d977aebf1718540533b4ba5b351ccec2db093370958a653b1f7f9219cc", size = 242359 },
    { url = "https://files.pythonhosted.org/packages/40/fd/3a76265f2748f718cc05f313c44440658ecd1939fa2b5e66087a5edd605f/multidict-6.3.2-cp313-cp313t-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:98eab7acf55275b5bf09834125fa3a80b143a9f241cdcdd3f1295ffdc3c6d097", size = 229881 },
    { url = "https://files.pythonhosted.org/packages/22/a9/5780f71e34adf93443ec0660591d877367991badadab9cc6ac02d7a64760/multidict-6.3.2-cp313-cp313t-musllinux_1_2_aarch64.whl", hash = "sha256:36863655630becc224375c0b99364978a0f95aebfb27fb6dd500f7fb5fb36e79", size = 248520 },
    { url = "https://files.pythonhosted.org/packages/f3/72/10988db397e1e819b669213c76a41fde670ba60ecec2c05d5ecdea05526c/multidict-6.3.2-cp313-cp313t-musllinux_1_2_i686.whl", hash = "sha256:d9c0979c096c0d46a963331b0e400d3a9e560e41219df4b35f0d7a2f28f39710", size = 237649 },
    { url = "https://files.pythonhosted.org/packages/29/75/52a7d3d1c0ffb2e8367f72845f309850113ea9201a50e4d4cdf8ac9f7d72/multidict-6.3.2-cp313-cp313t-musllinux_1_2_ppc64le.whl", hash = "sha256:0efc04f70f05e70e5945890767e8874da5953a196f5b07c552d305afae0f3bf6", size = 251467 },
    { url = "https://files.pythonhosted.org/packages/82/24/e42400008eff60d4af53a2ff313abf0b2715fdd3a71b845d85025844f198/multidict-6.3.2-cp313-cp313t-musllinux_1_2_s390x.whl", hash = "sha256:2c519b3b82c34539fae3e22e4ea965869ac6b628794b1eb487780dde37637ab7", size = 245310 },
    { url = "https://files.pythonhosted.org/packages/91/32/8b2e247539d4fdcc6cee36aa71c8898e0acd70e5d0e8a2ce9796a60790e5/multidict-6.3.2-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:329160e301f2afd7b43725d3dda8a7ef8ee41d4ceac2083fc0d8c1cc8a4bd56b", size = 243574 },
    { url = "https://files.pythonhosted.org/packages/d2/86/cc42cfa9b85b7d174948a17f828ebcacb0247e727fbedf06506ba93387ef/multidict-6.3.2-cp313-cp313t-win32.whl", hash = "sha256:420e5144a5f598dad8db3128f1695cd42a38a0026c2991091dab91697832f8cc", size = 41908 },
    { url = "https://files.pythonhosted.org/packages/2a/36/5c015523a7650fb5c55380d1c779b938379bd091968ee822d719e4264ab7/multidict-6.3.2-cp313-cp313t-win_amd64.whl", hash = "sha256:875faded2861c7af2682c67088e6313fec35ede811e071c96d36b081873cea14", size = 45635 },
    { url = "https://files.pythonhosted.org/packages/1a/5b/d8f61f7daa6278e8cd3ed998f1335dacbe9df39366e1cd061859157f86fd/multidict-6.3.2-cp39-cp39-macosx_10_9_universal2.whl", hash = "sha256:2516c5eb5732d6c4e29fa93323bfdc55186895124bc569e2404e3820934be378", size = 62678 },
    { url = "https://files.pythonhosted.org/packages/bd/f8/dc00c5f697a62bdac3131337da26276d9e842cd08a477d4d12bbdf91a312/multidict-6.3.2-cp39-cp39-macosx_10_9_x86_64.whl", hash = "sha256:be5c8622e665cc5491c13c0fcd52915cdbae991a3514251d71129691338cdfb2", size = 37071 },
    { url = "https://files.pythonhosted.org/packages/ea/af/380e238f7340e91d14e543bd592c585994097dec5a06828bafd525675103/multidict-6.3.2-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:3ef33150eea7953cfdb571d862cff894e0ad97ab80d97731eb4b9328fc32d52b", size = 36354 },
    { url = "https://files.pythonhosted.org/packages/45/4c/6f3166e9f7a90f7439dc956cb88d0a51ceb3c423b8f81450ef89870069e7/multidict-6.3.2-cp39-cp39-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:40b357738ce46e998f1b1bad9c4b79b2a9755915f71b87a8c01ce123a22a4f99", size = 235935 },
    { url = "https://files.pythonhosted.org/packages/05/7d/346aa561f3059dd2f2f422b6a704aad2e26094690fb49ada98e71feb1691/multidict-6.3.2-cp39-cp39-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:27c60e059fcd3655a653ba99fec2556cd0260ec57f9cb138d3e6ffc413638a2e", size = 248958 },
    { url = "https://files.pythonhosted.org/packages/df/f3/4c0841ae40ee9de3e8ce14fa6869a53b03a16f5ca580604548d3b85562b6/multidict-6.3.2-cp39-cp39-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:629e7c5e75bde83e54a22c7043ce89d68691d1f103be6d09a1c82b870df3b4b8", size = 244894 },
    { url = "https://files.pythonhosted.org/packages/76/bd/0ba520bec2a08698a9dbece5399c07d6139fc286ad9b411987d1d1b34ee1/multidict-6.3.2-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:ee6c8fc97d893fdf1fff15a619fee8de2f31c9b289ef7594730e35074fa0cefb", size = 231468 },
    { url = "https://files.pythonhosted.org/packages/46/69/2eb69ee27cba740241cdde6ffc6fda10ac4114bf609f186be4406d640a8f/multidict-6.3.2-cp39-cp39-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:52081d2f27e0652265d4637b03f09b82f6da5ce5e1474f07dc64674ff8bfc04c", size = 223744 },
    { url = "https://files.pythonhosted.org/packages/9a/28/e17987087faa1432d434ea071b60fbd69e78c50052590f4f1da92955e165/multidict-6.3.2-cp39-cp39-musllinux_1_2_aarch64.whl", hash = "sha256:64529dc395b5fd0a7826ffa70d2d9a7f4abd8f5333d6aaaba67fdf7bedde9f21", size = 233331 },
    { url = "https://files.pythonhosted.org/packages/9c/d9/a76007808d0d53da570397fc411c93911219f9515b5113a09f90f0ef266b/multidict-6.3.2-cp39-cp39-musllinux_1_2_i686.whl", hash = "sha256:2b7c3fad827770840f5399348c89635ed6d6e9bba363baad7d3c7f86a9cf1da3", size = 231691 },
    { url = "https://files.pythonhosted.org/packages/02/86/12203785d7bd867aaaa570393bf06de7024ab1d7ea5d47439c5f8dc19780/multidict-6.3.2-cp39-cp39-musllinux_1_2_ppc64le.whl", hash = "sha256:24aa42b1651c654ae9e5273e06c3b7ccffe9f7cc76fbde40c37e9ae65f170818", size = 242447 },
    { url = "https://files.pythonhosted.org/packages/bf/38/a040e44f14bd9771cf81aee77b337f28e1515727778013c18c476f401075/multidict-6.3.2-cp39-cp39-musllinux_1_2_s390x.whl", hash = "sha256:04ceea01e9991357164b12882e120ce6b4d63a0424bb9f9cd37910aa56d30830", size = 235109 },
    { url = "https://files.pythonhosted.org/packages/6e/26/80774106c61826ffc680d47de2148c18b78e726599ddc1524065c974c308/multidict-6.3.2-cp39-cp39-musllinux_1_2_x86_64.whl", hash = "sha256:943897a41160945416617db567d867ab34e9258adaffc56a25a4c3f99d919598", size = 231811 },
    { url = "https://files.pythonhosted.org/packages/75/8e/0ca0e1e02ca368bfb4529a513da01b59ec3b00ec5da977d915116a524787/multidict-6.3.2-cp39-cp39-win32.whl", hash = "sha256:76157a9a0c5380aadd3b5ff7b8deee355ff5adecc66c837b444fa633b4d409a2", size = 34972 },
    { url = "https://files.pythonhosted.org/packages/bc/cf/26e91f5237961b803ee524c30bc833d701e288d9a192c22ac57877687a05/multidict-6.3.2-cp39-cp39-win_amd64.whl", hash = "sha256:d091d123e44035cd5664554308477aff0b58db37e701e7598a67e907b98d1925", size = 38425 },
    { url = "https://files.pythonhosted.org/packages/aa/c1/7832c95a50641148b567b5366dd3354489950dcfd01c8fc28472bec63b9a/multidict-6.3.2-py3-none-any.whl", hash = "sha256:71409d4579f716217f23be2f5e7afca5ca926aaeb398aa11b72d793bff637a1f", size = 10347 },
]

[[package]]
name = "multiprocess"
version = "0.70.16"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "dill" },
]
sdist = { url = "https://files.pythonhosted.org/packages/b5/ae/04f39c5d0d0def03247c2893d6f2b83c136bf3320a2154d7b8858f2ba72d/multiprocess-0.70.16.tar.gz", hash = "sha256:161af703d4652a0e1410be6abccecde4a7ddffd19341be0a7011b94aeb171ac1", size = 1772603 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/ef/76/6e712a2623d146d314f17598df5de7224c85c0060ef63fd95cc15a25b3fa/multiprocess-0.70.16-pp310-pypy310_pp73-macosx_10_13_x86_64.whl", hash = "sha256:476887be10e2f59ff183c006af746cb6f1fd0eadcfd4ef49e605cbe2659920ee", size = 134980 },
    { url = "https://files.pythonhosted.org/packages/0f/ab/1e6e8009e380e22254ff539ebe117861e5bdb3bff1fc977920972237c6c7/multiprocess-0.70.16-pp310-pypy310_pp73-manylinux_2_28_x86_64.whl", hash = "sha256:d951bed82c8f73929ac82c61f01a7b5ce8f3e5ef40f5b52553b4f547ce2b08ec", size = 134982 },
    { url = "https://files.pythonhosted.org/packages/d8/94/8638a89f93c80df329116e6781a060506c7e91e1f4370dc831e9d17a041d/multiprocess-0.70.16-pp39-pypy39_pp73-macosx_10_13_x86_64.whl", hash = "sha256:0dfd078c306e08d46d7a8d06fb120313d87aa43af60d66da43ffff40b44d2f41", size = 133497 },
    { url = "https://files.pythonhosted.org/packages/89/21/222066f6bb8d8af287923ae3bd26cf4699a9ce020228ac273caca1de8250/multiprocess-0.70.16-pp39-pypy39_pp73-manylinux_2_28_x86_64.whl", hash = "sha256:e7b9d0f307cd9bd50851afaac0dba2cb6c44449efff697df7c7645f7d3f2be3a", size = 133498 },
    { url = "https://files.pythonhosted.org/packages/bc/f7/7ec7fddc92e50714ea3745631f79bd9c96424cb2702632521028e57d3a36/multiprocess-0.70.16-py310-none-any.whl", hash = "sha256:c4a9944c67bd49f823687463660a2d6daae94c289adff97e0f9d696ba6371d02", size = 134824 },
    { url = "https://files.pythonhosted.org/packages/50/15/b56e50e8debaf439f44befec5b2af11db85f6e0f344c3113ae0be0593a91/multiprocess-0.70.16-py311-none-any.whl", hash = "sha256:af4cabb0dac72abfb1e794fa7855c325fd2b55a10a44628a3c1ad3311c04127a", size = 143519 },
    { url = "https://files.pythonhosted.org/packages/0a/7d/a988f258104dcd2ccf1ed40fdc97e26c4ac351eeaf81d76e266c52d84e2f/multiprocess-0.70.16-py312-none-any.whl", hash = "sha256:fc0544c531920dde3b00c29863377f87e1632601092ea2daca74e4beb40faa2e", size = 146741 },
    { url = "https://files.pythonhosted.org/packages/ea/89/38df130f2c799090c978b366cfdf5b96d08de5b29a4a293df7f7429fa50b/multiprocess-0.70.16-py38-none-any.whl", hash = "sha256:a71d82033454891091a226dfc319d0cfa8019a4e888ef9ca910372a446de4435", size = 132628 },
    { url = "https://files.pythonhosted.org/packages/da/d9/f7f9379981e39b8c2511c9e0326d212accacb82f12fbfdc1aa2ce2a7b2b6/multiprocess-0.70.16-py39-none-any.whl", hash = "sha256:a0bafd3ae1b732eac64be2e72038231c1ba97724b60b09400d68f229fcc2fbf3", size = 133351 },
]

[[package]]
name = "mypy"
version = "1.15.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "mypy-extensions" },
    { name = "tomli", marker = "python_full_version < '3.11'" },
    { name = "typing-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/ce/43/d5e49a86afa64bd3839ea0d5b9c7103487007d728e1293f52525d6d5486a/mypy-1.15.0.tar.gz", hash = "sha256:404534629d51d3efea5c800ee7c42b72a6554d6c400e6a79eafe15d11341fd43", size = 3239717 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/68/f8/65a7ce8d0e09b6329ad0c8d40330d100ea343bd4dd04c4f8ae26462d0a17/mypy-1.15.0-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:979e4e1a006511dacf628e36fadfecbcc0160a8af6ca7dad2f5025529e082c13", size = 10738433 },
    { url = "https://files.pythonhosted.org/packages/b4/95/9c0ecb8eacfe048583706249439ff52105b3f552ea9c4024166c03224270/mypy-1.15.0-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:c4bb0e1bd29f7d34efcccd71cf733580191e9a264a2202b0239da95984c5b559", size = 9861472 },
    { url = "https://files.pythonhosted.org/packages/84/09/9ec95e982e282e20c0d5407bc65031dfd0f0f8ecc66b69538296e06fcbee/mypy-1.15.0-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:be68172e9fd9ad8fb876c6389f16d1c1b5f100ffa779f77b1fb2176fcc9ab95b", size = 11611424 },
    { url = "https://files.pythonhosted.org/packages/78/13/f7d14e55865036a1e6a0a69580c240f43bc1f37407fe9235c0d4ef25ffb0/mypy-1.15.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:c7be1e46525adfa0d97681432ee9fcd61a3964c2446795714699a998d193f1a3", size = 12365450 },
    { url = "https://files.pythonhosted.org/packages/48/e1/301a73852d40c241e915ac6d7bcd7fedd47d519246db2d7b86b9d7e7a0cb/mypy-1.15.0-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:2e2c2e6d3593f6451b18588848e66260ff62ccca522dd231cd4dd59b0160668b", size = 12551765 },
    { url = "https://files.pythonhosted.org/packages/77/ba/c37bc323ae5fe7f3f15a28e06ab012cd0b7552886118943e90b15af31195/mypy-1.15.0-cp310-cp310-win_amd64.whl", hash = "sha256:6983aae8b2f653e098edb77f893f7b6aca69f6cffb19b2cc7443f23cce5f4828", size = 9274701 },
    { url = "https://files.pythonhosted.org/packages/03/bc/f6339726c627bd7ca1ce0fa56c9ae2d0144604a319e0e339bdadafbbb599/mypy-1.15.0-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:2922d42e16d6de288022e5ca321cd0618b238cfc5570e0263e5ba0a77dbef56f", size = 10662338 },
    { url = "https://files.pythonhosted.org/packages/e2/90/8dcf506ca1a09b0d17555cc00cd69aee402c203911410136cd716559efe7/mypy-1.15.0-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:2ee2d57e01a7c35de00f4634ba1bbf015185b219e4dc5909e281016df43f5ee5", size = 9787540 },
    { url = "https://files.pythonhosted.org/packages/05/05/a10f9479681e5da09ef2f9426f650d7b550d4bafbef683b69aad1ba87457/mypy-1.15.0-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:973500e0774b85d9689715feeffcc980193086551110fd678ebe1f4342fb7c5e", size = 11538051 },
    { url = "https://files.pythonhosted.org/packages/e9/9a/1f7d18b30edd57441a6411fcbc0c6869448d1a4bacbaee60656ac0fc29c8/mypy-1.15.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:5a95fb17c13e29d2d5195869262f8125dfdb5c134dc8d9a9d0aecf7525b10c2c", size = 12286751 },
    { url = "https://files.pythonhosted.org/packages/72/af/19ff499b6f1dafcaf56f9881f7a965ac2f474f69f6f618b5175b044299f5/mypy-1.15.0-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:1905f494bfd7d85a23a88c5d97840888a7bd516545fc5aaedff0267e0bb54e2f", size = 12421783 },
    { url = "https://files.pythonhosted.org/packages/96/39/11b57431a1f686c1aed54bf794870efe0f6aeca11aca281a0bd87a5ad42c/mypy-1.15.0-cp311-cp311-win_amd64.whl", hash = "sha256:c9817fa23833ff189db061e6d2eff49b2f3b6ed9856b4a0a73046e41932d744f", size = 9265618 },
    { url = "https://files.pythonhosted.org/packages/98/3a/03c74331c5eb8bd025734e04c9840532226775c47a2c39b56a0c8d4f128d/mypy-1.15.0-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:aea39e0583d05124836ea645f412e88a5c7d0fd77a6d694b60d9b6b2d9f184fd", size = 10793981 },
    { url = "https://files.pythonhosted.org/packages/f0/1a/41759b18f2cfd568848a37c89030aeb03534411eef981df621d8fad08a1d/mypy-1.15.0-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:2f2147ab812b75e5b5499b01ade1f4a81489a147c01585cda36019102538615f", size = 9749175 },
    { url = "https://files.pythonhosted.org/packages/12/7e/873481abf1ef112c582db832740f4c11b2bfa510e829d6da29b0ab8c3f9c/mypy-1.15.0-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:ce436f4c6d218a070048ed6a44c0bbb10cd2cc5e272b29e7845f6a2f57ee4464", size = 11455675 },
    { url = "https://files.pythonhosted.org/packages/b3/d0/92ae4cde706923a2d3f2d6c39629134063ff64b9dedca9c1388363da072d/mypy-1.15.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:8023ff13985661b50a5928fc7a5ca15f3d1affb41e5f0a9952cb68ef090b31ee", size = 12410020 },
    { url = "https://files.pythonhosted.org/packages/46/8b/df49974b337cce35f828ba6fda228152d6db45fed4c86ba56ffe442434fd/mypy-1.15.0-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:1124a18bc11a6a62887e3e137f37f53fbae476dc36c185d549d4f837a2a6a14e", size = 12498582 },
    { url = "https://files.pythonhosted.org/packages/13/50/da5203fcf6c53044a0b699939f31075c45ae8a4cadf538a9069b165c1050/mypy-1.15.0-cp312-cp312-win_amd64.whl", hash = "sha256:171a9ca9a40cd1843abeca0e405bc1940cd9b305eaeea2dda769ba096932bb22", size = 9366614 },
    { url = "https://files.pythonhosted.org/packages/6a/9b/fd2e05d6ffff24d912f150b87db9e364fa8282045c875654ce7e32fffa66/mypy-1.15.0-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:93faf3fdb04768d44bf28693293f3904bbb555d076b781ad2530214ee53e3445", size = 10788592 },
    { url = "https://files.pythonhosted.org/packages/74/37/b246d711c28a03ead1fd906bbc7106659aed7c089d55fe40dd58db812628/mypy-1.15.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:811aeccadfb730024c5d3e326b2fbe9249bb7413553f15499a4050f7c30e801d", size = 9753611 },
    { url = "https://files.pythonhosted.org/packages/a6/ac/395808a92e10cfdac8003c3de9a2ab6dc7cde6c0d2a4df3df1b815ffd067/mypy-1.15.0-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:98b7b9b9aedb65fe628c62a6dc57f6d5088ef2dfca37903a7d9ee374d03acca5", size = 11438443 },
    { url = "https://files.pythonhosted.org/packages/d2/8b/801aa06445d2de3895f59e476f38f3f8d610ef5d6908245f07d002676cbf/mypy-1.15.0-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:c43a7682e24b4f576d93072216bf56eeff70d9140241f9edec0c104d0c515036", size = 12402541 },
    { url = "https://files.pythonhosted.org/packages/c7/67/5a4268782eb77344cc613a4cf23540928e41f018a9a1ec4c6882baf20ab8/mypy-1.15.0-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:baefc32840a9f00babd83251560e0ae1573e2f9d1b067719479bfb0e987c6357", size = 12494348 },
    { url = "https://files.pythonhosted.org/packages/83/3e/57bb447f7bbbfaabf1712d96f9df142624a386d98fb026a761532526057e/mypy-1.15.0-cp313-cp313-win_amd64.whl", hash = "sha256:b9378e2c00146c44793c98b8d5a61039a048e31f429fb0eb546d93f4b000bedf", size = 9373648 },
    { url = "https://files.pythonhosted.org/packages/5a/fa/79cf41a55b682794abe71372151dbbf856e3008f6767057229e6649d294a/mypy-1.15.0-cp39-cp39-macosx_10_9_x86_64.whl", hash = "sha256:e601a7fa172c2131bff456bb3ee08a88360760d0d2f8cbd7a75a65497e2df078", size = 10737129 },
    { url = "https://files.pythonhosted.org/packages/d3/33/dd8feb2597d648de29e3da0a8bf4e1afbda472964d2a4a0052203a6f3594/mypy-1.15.0-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:712e962a6357634fef20412699a3655c610110e01cdaa6180acec7fc9f8513ba", size = 9856335 },
    { url = "https://files.pythonhosted.org/packages/e4/b5/74508959c1b06b96674b364ffeb7ae5802646b32929b7701fc6b18447592/mypy-1.15.0-cp39-cp39-manylinux_2_17_aarch64.manylinux2014_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:f95579473af29ab73a10bada2f9722856792a36ec5af5399b653aa28360290a5", size = 11611935 },
    { url = "https://files.pythonhosted.org/packages/6c/53/da61b9d9973efcd6507183fdad96606996191657fe79701b2c818714d573/mypy-1.15.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:8f8722560a14cde92fdb1e31597760dc35f9f5524cce17836c0d22841830fd5b", size = 12365827 },
    { url = "https://files.pythonhosted.org/packages/c1/72/965bd9ee89540c79a25778cc080c7e6ef40aa1eeac4d52cec7eae6eb5228/mypy-1.15.0-cp39-cp39-musllinux_1_2_x86_64.whl", hash = "sha256:1fbb8da62dc352133d7d7ca90ed2fb0e9d42bb1a32724c287d3c76c58cbaa9c2", size = 12541924 },
    { url = "https://files.pythonhosted.org/packages/46/d0/f41645c2eb263e6c77ada7d76f894c580c9ddb20d77f0c24d34273a4dab2/mypy-1.15.0-cp39-cp39-win_amd64.whl", hash = "sha256:d10d994b41fb3497719bbf866f227b3489048ea4bbbb5015357db306249f7980", size = 9271176 },
    { url = "https://files.pythonhosted.org/packages/09/4e/a7d65c7322c510de2c409ff3828b03354a7c43f5a8ed458a7a131b41c7b9/mypy-1.15.0-py3-none-any.whl", hash = "sha256:5469affef548bd1895d86d3bf10ce2b44e33d86923c29e4d675b3e323437ea3e", size = 2221777 },
]

[[package]]
name = "mypy-extensions"
version = "1.0.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/98/a4/1ab47638b92648243faf97a5aeb6ea83059cc3624972ab6b8d2316078d3f/mypy_extensions-1.0.0.tar.gz", hash = "sha256:75dbf8955dc00442a438fc4d0666508a9a97b6bd41aa2f0ffe9d2f2725af0782", size = 4433 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/2a/e2/5d3f6ada4297caebe1a2add3b126fe800c96f56dbe5d1988a2cbe0b267aa/mypy_extensions-1.0.0-py3-none-any.whl", hash = "sha256:4392f6c0eb8a5668a69e23d168ffa70f0be9ccfd32b5cc2d26a34ae5b844552d", size = 4695 },
]

[[package]]
name = "networkx"
version = "3.2.1"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/c4/80/a84676339aaae2f1cfdf9f418701dd634aef9cc76f708ef55c36ff39c3ca/networkx-3.2.1.tar.gz", hash = "sha256:9f1bb5cf3409bf324e0a722c20bdb4c20ee39bf1c30ce8ae499c8502b0b5e0c6", size = 2073928 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/d5/f0/8fbc882ca80cf077f1b246c0e3c3465f7f415439bdea6b899f6b19f61f70/networkx-3.2.1-py3-none-any.whl", hash = "sha256:f18c69adc97877c42332c170849c96cefa91881c99a7cb3e95b7c659ebdc1ec2", size = 1647772 },
]

[[package]]
name = "numpy"
version = "2.0.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/a9/75/10dd1f8116a8b796cb2c737b674e02d02e80454bda953fa7e65d8c12b016/numpy-2.0.2.tar.gz", hash = "sha256:883c987dee1880e2a864ab0dc9892292582510604156762362d9326444636e78", size = 18902015 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/21/91/3495b3237510f79f5d81f2508f9f13fea78ebfdf07538fc7444badda173d/numpy-2.0.2-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:51129a29dbe56f9ca83438b706e2e69a39892b5eda6cedcb6b0c9fdc9b0d3ece", size = 21165245 },
    { url = "https://files.pythonhosted.org/packages/05/33/26178c7d437a87082d11019292dce6d3fe6f0e9026b7b2309cbf3e489b1d/numpy-2.0.2-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:f15975dfec0cf2239224d80e32c3170b1d168335eaedee69da84fbe9f1f9cd04", size = 13738540 },
    { url = "https://files.pythonhosted.org/packages/ec/31/cc46e13bf07644efc7a4bf68df2df5fb2a1a88d0cd0da9ddc84dc0033e51/numpy-2.0.2-cp310-cp310-macosx_14_0_arm64.whl", hash = "sha256:8c5713284ce4e282544c68d1c3b2c7161d38c256d2eefc93c1d683cf47683e66", size = 5300623 },
    { url = "https://files.pythonhosted.org/packages/6e/16/7bfcebf27bb4f9d7ec67332ffebee4d1bf085c84246552d52dbb548600e7/numpy-2.0.2-cp310-cp310-macosx_14_0_x86_64.whl", hash = "sha256:becfae3ddd30736fe1889a37f1f580e245ba79a5855bff5f2a29cb3ccc22dd7b", size = 6901774 },
    { url = "https://files.pythonhosted.org/packages/f9/a3/561c531c0e8bf082c5bef509d00d56f82e0ea7e1e3e3a7fc8fa78742a6e5/numpy-2.0.2-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:2da5960c3cf0df7eafefd806d4e612c5e19358de82cb3c343631188991566ccd", size = 13907081 },
    { url = "https://files.pythonhosted.org/packages/fa/66/f7177ab331876200ac7563a580140643d1179c8b4b6a6b0fc9838de2a9b8/numpy-2.0.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:496f71341824ed9f3d2fd36cf3ac57ae2e0165c143b55c3a035ee219413f3318", size = 19523451 },
    { url = "https://files.pythonhosted.org/packages/25/7f/0b209498009ad6453e4efc2c65bcdf0ae08a182b2b7877d7ab38a92dc542/numpy-2.0.2-cp310-cp310-musllinux_1_1_x86_64.whl", hash = "sha256:a61ec659f68ae254e4d237816e33171497e978140353c0c2038d46e63282d0c8", size = 19927572 },
    { url = "https://files.pythonhosted.org/packages/3e/df/2619393b1e1b565cd2d4c4403bdd979621e2c4dea1f8532754b2598ed63b/numpy-2.0.2-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:d731a1c6116ba289c1e9ee714b08a8ff882944d4ad631fd411106a30f083c326", size = 14400722 },
    { url = "https://files.pythonhosted.org/packages/22/ad/77e921b9f256d5da36424ffb711ae79ca3f451ff8489eeca544d0701d74a/numpy-2.0.2-cp310-cp310-win32.whl", hash = "sha256:984d96121c9f9616cd33fbd0618b7f08e0cfc9600a7ee1d6fd9b239186d19d97", size = 6472170 },
    { url = "https://files.pythonhosted.org/packages/10/05/3442317535028bc29cf0c0dd4c191a4481e8376e9f0db6bcf29703cadae6/numpy-2.0.2-cp310-cp310-win_amd64.whl", hash = "sha256:c7b0be4ef08607dd04da4092faee0b86607f111d5ae68036f16cc787e250a131", size = 15905558 },
    { url = "https://files.pythonhosted.org/packages/8b/cf/034500fb83041aa0286e0fb16e7c76e5c8b67c0711bb6e9e9737a717d5fe/numpy-2.0.2-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:49ca4decb342d66018b01932139c0961a8f9ddc7589611158cb3c27cbcf76448", size = 21169137 },
    { url = "https://files.pythonhosted.org/packages/4a/d9/32de45561811a4b87fbdee23b5797394e3d1504b4a7cf40c10199848893e/numpy-2.0.2-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:11a76c372d1d37437857280aa142086476136a8c0f373b2e648ab2c8f18fb195", size = 13703552 },
    { url = "https://files.pythonhosted.org/packages/c1/ca/2f384720020c7b244d22508cb7ab23d95f179fcfff33c31a6eeba8d6c512/numpy-2.0.2-cp311-cp311-macosx_14_0_arm64.whl", hash = "sha256:807ec44583fd708a21d4a11d94aedf2f4f3c3719035c76a2bbe1fe8e217bdc57", size = 5298957 },
    { url = "https://files.pythonhosted.org/packages/0e/78/a3e4f9fb6aa4e6fdca0c5428e8ba039408514388cf62d89651aade838269/numpy-2.0.2-cp311-cp311-macosx_14_0_x86_64.whl", hash = "sha256:8cafab480740e22f8d833acefed5cc87ce276f4ece12fdaa2e8903db2f82897a", size = 6905573 },
    { url = "https://files.pythonhosted.org/packages/a0/72/cfc3a1beb2caf4efc9d0b38a15fe34025230da27e1c08cc2eb9bfb1c7231/numpy-2.0.2-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:a15f476a45e6e5a3a79d8a14e62161d27ad897381fecfa4a09ed5322f2085669", size = 13914330 },
    { url = "https://files.pythonhosted.org/packages/ba/a8/c17acf65a931ce551fee11b72e8de63bf7e8a6f0e21add4c937c83563538/numpy-2.0.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:13e689d772146140a252c3a28501da66dfecd77490b498b168b501835041f951", size = 19534895 },
    { url = "https://files.pythonhosted.org/packages/ba/86/8767f3d54f6ae0165749f84648da9dcc8cd78ab65d415494962c86fac80f/numpy-2.0.2-cp311-cp311-musllinux_1_1_x86_64.whl", hash = "sha256:9ea91dfb7c3d1c56a0e55657c0afb38cf1eeae4544c208dc465c3c9f3a7c09f9", size = 19937253 },
    { url = "https://files.pythonhosted.org/packages/df/87/f76450e6e1c14e5bb1eae6836478b1028e096fd02e85c1c37674606ab752/numpy-2.0.2-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:c1c9307701fec8f3f7a1e6711f9089c06e6284b3afbbcd259f7791282d660a15", size = 14414074 },
    { url = "https://files.pythonhosted.org/packages/5c/ca/0f0f328e1e59f73754f06e1adfb909de43726d4f24c6a3f8805f34f2b0fa/numpy-2.0.2-cp311-cp311-win32.whl", hash = "sha256:a392a68bd329eafac5817e5aefeb39038c48b671afd242710b451e76090e81f4", size = 6470640 },
    { url = "https://files.pythonhosted.org/packages/eb/57/3a3f14d3a759dcf9bf6e9eda905794726b758819df4663f217d658a58695/numpy-2.0.2-cp311-cp311-win_amd64.whl", hash = "sha256:286cd40ce2b7d652a6f22efdfc6d1edf879440e53e76a75955bc0c826c7e64dc", size = 15910230 },
    { url = "https://files.pythonhosted.org/packages/45/40/2e117be60ec50d98fa08c2f8c48e09b3edea93cfcabd5a9ff6925d54b1c2/numpy-2.0.2-cp312-cp312-macosx_10_9_x86_64.whl", hash = "sha256:df55d490dea7934f330006d0f81e8551ba6010a5bf035a249ef61a94f21c500b", size = 20895803 },
    { url = "https://files.pythonhosted.org/packages/46/92/1b8b8dee833f53cef3e0a3f69b2374467789e0bb7399689582314df02651/numpy-2.0.2-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:8df823f570d9adf0978347d1f926b2a867d5608f434a7cff7f7908c6570dcf5e", size = 13471835 },
    { url = "https://files.pythonhosted.org/packages/7f/19/e2793bde475f1edaea6945be141aef6c8b4c669b90c90a300a8954d08f0a/numpy-2.0.2-cp312-cp312-macosx_14_0_arm64.whl", hash = "sha256:9a92ae5c14811e390f3767053ff54eaee3bf84576d99a2456391401323f4ec2c", size = 5038499 },
    { url = "https://files.pythonhosted.org/packages/e3/ff/ddf6dac2ff0dd50a7327bcdba45cb0264d0e96bb44d33324853f781a8f3c/numpy-2.0.2-cp312-cp312-macosx_14_0_x86_64.whl", hash = "sha256:a842d573724391493a97a62ebbb8e731f8a5dcc5d285dfc99141ca15a3302d0c", size = 6633497 },
    { url = "https://files.pythonhosted.org/packages/72/21/67f36eac8e2d2cd652a2e69595a54128297cdcb1ff3931cfc87838874bd4/numpy-2.0.2-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:c05e238064fc0610c840d1cf6a13bf63d7e391717d247f1bf0318172e759e692", size = 13621158 },
    { url = "https://files.pythonhosted.org/packages/39/68/e9f1126d757653496dbc096cb429014347a36b228f5a991dae2c6b6cfd40/numpy-2.0.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:0123ffdaa88fa4ab64835dcbde75dcdf89c453c922f18dced6e27c90d1d0ec5a", size = 19236173 },
    { url = "https://files.pythonhosted.org/packages/d1/e9/1f5333281e4ebf483ba1c888b1d61ba7e78d7e910fdd8e6499667041cc35/numpy-2.0.2-cp312-cp312-musllinux_1_1_x86_64.whl", hash = "sha256:96a55f64139912d61de9137f11bf39a55ec8faec288c75a54f93dfd39f7eb40c", size = 19634174 },
    { url = "https://files.pythonhosted.org/packages/71/af/a469674070c8d8408384e3012e064299f7a2de540738a8e414dcfd639996/numpy-2.0.2-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:ec9852fb39354b5a45a80bdab5ac02dd02b15f44b3804e9f00c556bf24b4bded", size = 14099701 },
    { url = "https://files.pythonhosted.org/packages/d0/3d/08ea9f239d0e0e939b6ca52ad403c84a2bce1bde301a8eb4888c1c1543f1/numpy-2.0.2-cp312-cp312-win32.whl", hash = "sha256:671bec6496f83202ed2d3c8fdc486a8fc86942f2e69ff0e986140339a63bcbe5", size = 6174313 },
    { url = "https://files.pythonhosted.org/packages/b2/b5/4ac39baebf1fdb2e72585c8352c56d063b6126be9fc95bd2bb5ef5770c20/numpy-2.0.2-cp312-cp312-win_amd64.whl", hash = "sha256:cfd41e13fdc257aa5778496b8caa5e856dc4896d4ccf01841daee1d96465467a", size = 15606179 },
    { url = "https://files.pythonhosted.org/packages/43/c1/41c8f6df3162b0c6ffd4437d729115704bd43363de0090c7f913cfbc2d89/numpy-2.0.2-cp39-cp39-macosx_10_9_x86_64.whl", hash = "sha256:9059e10581ce4093f735ed23f3b9d283b9d517ff46009ddd485f1747eb22653c", size = 21169942 },
    { url = "https://files.pythonhosted.org/packages/39/bc/fd298f308dcd232b56a4031fd6ddf11c43f9917fbc937e53762f7b5a3bb1/numpy-2.0.2-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:423e89b23490805d2a5a96fe40ec507407b8ee786d66f7328be214f9679df6dd", size = 13711512 },
    { url = "https://files.pythonhosted.org/packages/96/ff/06d1aa3eeb1c614eda245c1ba4fb88c483bee6520d361641331872ac4b82/numpy-2.0.2-cp39-cp39-macosx_14_0_arm64.whl", hash = "sha256:2b2955fa6f11907cf7a70dab0d0755159bca87755e831e47932367fc8f2f2d0b", size = 5306976 },
    { url = "https://files.pythonhosted.org/packages/2d/98/121996dcfb10a6087a05e54453e28e58694a7db62c5a5a29cee14c6e047b/numpy-2.0.2-cp39-cp39-macosx_14_0_x86_64.whl", hash = "sha256:97032a27bd9d8988b9a97a8c4d2c9f2c15a81f61e2f21404d7e8ef00cb5be729", size = 6906494 },
    { url = "https://files.pythonhosted.org/packages/15/31/9dffc70da6b9bbf7968f6551967fc21156207366272c2a40b4ed6008dc9b/numpy-2.0.2-cp39-cp39-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:1e795a8be3ddbac43274f18588329c72939870a16cae810c2b73461c40718ab1", size = 13912596 },
    { url = "https://files.pythonhosted.org/packages/b9/14/78635daab4b07c0930c919d451b8bf8c164774e6a3413aed04a6d95758ce/numpy-2.0.2-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:f26b258c385842546006213344c50655ff1555a9338e2e5e02a0756dc3e803dd", size = 19526099 },
    { url = "https://files.pythonhosted.org/packages/26/4c/0eeca4614003077f68bfe7aac8b7496f04221865b3a5e7cb230c9d055afd/numpy-2.0.2-cp39-cp39-musllinux_1_1_x86_64.whl", hash = "sha256:5fec9451a7789926bcf7c2b8d187292c9f93ea30284802a0ab3f5be8ab36865d", size = 19932823 },
    { url = "https://files.pythonhosted.org/packages/f1/46/ea25b98b13dccaebddf1a803f8c748680d972e00507cd9bc6dcdb5aa2ac1/numpy-2.0.2-cp39-cp39-musllinux_1_2_aarch64.whl", hash = "sha256:9189427407d88ff25ecf8f12469d4d39d35bee1db5d39fc5c168c6f088a6956d", size = 14404424 },
    { url = "https://files.pythonhosted.org/packages/c8/a6/177dd88d95ecf07e722d21008b1b40e681a929eb9e329684d449c36586b2/numpy-2.0.2-cp39-cp39-win32.whl", hash = "sha256:905d16e0c60200656500c95b6b8dca5d109e23cb24abc701d41c02d74c6b3afa", size = 6476809 },
    { url = "https://files.pythonhosted.org/packages/ea/2b/7fc9f4e7ae5b507c1a3a21f0f15ed03e794c1242ea8a242ac158beb56034/numpy-2.0.2-cp39-cp39-win_amd64.whl", hash = "sha256:a3f4ab0caa7f053f6797fcd4e1e25caee367db3112ef2b6ef82d749530768c73", size = 15911314 },
    { url = "https://files.pythonhosted.org/packages/8f/3b/df5a870ac6a3be3a86856ce195ef42eec7ae50d2a202be1f5a4b3b340e14/numpy-2.0.2-pp39-pypy39_pp73-macosx_10_9_x86_64.whl", hash = "sha256:7f0a0c6f12e07fa94133c8a67404322845220c06a9e80e85999afe727f7438b8", size = 21025288 },
    { url = "https://files.pythonhosted.org/packages/2c/97/51af92f18d6f6f2d9ad8b482a99fb74e142d71372da5d834b3a2747a446e/numpy-2.0.2-pp39-pypy39_pp73-macosx_14_0_x86_64.whl", hash = "sha256:312950fdd060354350ed123c0e25a71327d3711584beaef30cdaa93320c392d4", size = 6762793 },
    { url = "https://files.pythonhosted.org/packages/12/46/de1fbd0c1b5ccaa7f9a005b66761533e2f6a3e560096682683a223631fe9/numpy-2.0.2-pp39-pypy39_pp73-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:26df23238872200f63518dd2aa984cfca675d82469535dc7162dc2ee52d9dd5c", size = 19334885 },
    { url = "https://files.pythonhosted.org/packages/cc/dc/d330a6faefd92b446ec0f0dfea4c3207bb1fef3c4771d19cf4543efd2c78/numpy-2.0.2-pp39-pypy39_pp73-win_amd64.whl", hash = "sha256:a46288ec55ebbd58947d31d72be2c63cbf839f0a63b49cb755022310792a3385", size = 15828784 },
]

[[package]]
name = "nvidia-cublas-cu12"
version = "12.4.5.8"
source = { registry = "https://pypi.org/simple" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/7f/7f/7fbae15a3982dc9595e49ce0f19332423b260045d0a6afe93cdbe2f1f624/nvidia_cublas_cu12-12.4.5.8-py3-none-manylinux2014_aarch64.whl", hash = "sha256:0f8aa1706812e00b9f19dfe0cdb3999b092ccb8ca168c0db5b8ea712456fd9b3", size = 363333771 },
    { url = "https://files.pythonhosted.org/packages/ae/71/1c91302526c45ab494c23f61c7a84aa568b8c1f9d196efa5993957faf906/nvidia_cublas_cu12-12.4.5.8-py3-none-manylinux2014_x86_64.whl", hash = "sha256:2fc8da60df463fdefa81e323eef2e36489e1c94335b5358bcb38360adf75ac9b", size = 363438805 },
]

[[package]]
name = "nvidia-cuda-cupti-cu12"
version = "12.4.127"
source = { registry = "https://pypi.org/simple" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/93/b5/9fb3d00386d3361b03874246190dfec7b206fd74e6e287b26a8fcb359d95/nvidia_cuda_cupti_cu12-12.4.127-py3-none-manylinux2014_aarch64.whl", hash = "sha256:79279b35cf6f91da114182a5ce1864997fd52294a87a16179ce275773799458a", size = 12354556 },
    { url = "https://files.pythonhosted.org/packages/67/42/f4f60238e8194a3106d06a058d494b18e006c10bb2b915655bd9f6ea4cb1/nvidia_cuda_cupti_cu12-12.4.127-py3-none-manylinux2014_x86_64.whl", hash = "sha256:9dec60f5ac126f7bb551c055072b69d85392b13311fcc1bcda2202d172df30fb", size = 13813957 },
]

[[package]]
name = "nvidia-cuda-nvrtc-cu12"
version = "12.4.127"
source = { registry = "https://pypi.org/simple" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/77/aa/083b01c427e963ad0b314040565ea396f914349914c298556484f799e61b/nvidia_cuda_nvrtc_cu12-12.4.127-py3-none-manylinux2014_aarch64.whl", hash = "sha256:0eedf14185e04b76aa05b1fea04133e59f465b6f960c0cbf4e37c3cb6b0ea198", size = 24133372 },
    { url = "https://files.pythonhosted.org/packages/2c/14/91ae57cd4db3f9ef7aa99f4019cfa8d54cb4caa7e00975df6467e9725a9f/nvidia_cuda_nvrtc_cu12-12.4.127-py3-none-manylinux2014_x86_64.whl", hash = "sha256:a178759ebb095827bd30ef56598ec182b85547f1508941a3d560eb7ea1fbf338", size = 24640306 },
]

[[package]]
name = "nvidia-cuda-runtime-cu12"
version = "12.4.127"
source = { registry = "https://pypi.org/simple" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/a1/aa/b656d755f474e2084971e9a297def515938d56b466ab39624012070cb773/nvidia_cuda_runtime_cu12-12.4.127-py3-none-manylinux2014_aarch64.whl", hash = "sha256:961fe0e2e716a2a1d967aab7caee97512f71767f852f67432d572e36cb3a11f3", size = 894177 },
    { url = "https://files.pythonhosted.org/packages/ea/27/1795d86fe88ef397885f2e580ac37628ed058a92ed2c39dc8eac3adf0619/nvidia_cuda_runtime_cu12-12.4.127-py3-none-manylinux2014_x86_64.whl", hash = "sha256:64403288fa2136ee8e467cdc9c9427e0434110899d07c779f25b5c068934faa5", size = 883737 },
]

[[package]]
name = "nvidia-cudnn-cu12"
version = "9.1.0.70"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "nvidia-cublas-cu12" },
]
wheels = [
    { url = "https://files.pythonhosted.org/packages/9f/fd/713452cd72343f682b1c7b9321e23829f00b842ceaedcda96e742ea0b0b3/nvidia_cudnn_cu12-9.1.0.70-py3-none-manylinux2014_x86_64.whl", hash = "sha256:165764f44ef8c61fcdfdfdbe769d687e06374059fbb388b6c89ecb0e28793a6f", size = 664752741 },
]

[[package]]
name = "nvidia-cufft-cu12"
version = "11.2.1.3"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "nvidia-nvjitlink-cu12" },
]
wheels = [
    { url = "https://files.pythonhosted.org/packages/7a/8a/0e728f749baca3fbeffad762738276e5df60851958be7783af121a7221e7/nvidia_cufft_cu12-11.2.1.3-py3-none-manylinux2014_aarch64.whl", hash = "sha256:5dad8008fc7f92f5ddfa2101430917ce2ffacd86824914c82e28990ad7f00399", size = 211422548 },
    { url = "https://files.pythonhosted.org/packages/27/94/3266821f65b92b3138631e9c8e7fe1fb513804ac934485a8d05776e1dd43/nvidia_cufft_cu12-11.2.1.3-py3-none-manylinux2014_x86_64.whl", hash = "sha256:f083fc24912aa410be21fa16d157fed2055dab1cc4b6934a0e03cba69eb242b9", size = 211459117 },
]

[[package]]
name = "nvidia-curand-cu12"
version = "10.3.5.147"
source = { registry = "https://pypi.org/simple" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/80/9c/a79180e4d70995fdf030c6946991d0171555c6edf95c265c6b2bf7011112/nvidia_curand_cu12-10.3.5.147-py3-none-manylinux2014_aarch64.whl", hash = "sha256:1f173f09e3e3c76ab084aba0de819c49e56614feae5c12f69883f4ae9bb5fad9", size = 56314811 },
    { url = "https://files.pythonhosted.org/packages/8a/6d/44ad094874c6f1b9c654f8ed939590bdc408349f137f9b98a3a23ccec411/nvidia_curand_cu12-10.3.5.147-py3-none-manylinux2014_x86_64.whl", hash = "sha256:a88f583d4e0bb643c49743469964103aa59f7f708d862c3ddb0fc07f851e3b8b", size = 56305206 },
]

[[package]]
name = "nvidia-cusolver-cu12"
version = "11.6.1.9"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "nvidia-cublas-cu12" },
    { name = "nvidia-cusparse-cu12" },
    { name = "nvidia-nvjitlink-cu12" },
]
wheels = [
    { url = "https://files.pythonhosted.org/packages/46/6b/a5c33cf16af09166845345275c34ad2190944bcc6026797a39f8e0a282e0/nvidia_cusolver_cu12-11.6.1.9-py3-none-manylinux2014_aarch64.whl", hash = "sha256:d338f155f174f90724bbde3758b7ac375a70ce8e706d70b018dd3375545fc84e", size = 127634111 },
    { url = "https://files.pythonhosted.org/packages/3a/e1/5b9089a4b2a4790dfdea8b3a006052cfecff58139d5a4e34cb1a51df8d6f/nvidia_cusolver_cu12-11.6.1.9-py3-none-manylinux2014_x86_64.whl", hash = "sha256:19e33fa442bcfd085b3086c4ebf7e8debc07cfe01e11513cc6d332fd918ac260", size = 127936057 },
]

[[package]]
name = "nvidia-cusparse-cu12"
version = "12.3.1.170"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "nvidia-nvjitlink-cu12" },
]
wheels = [
    { url = "https://files.pythonhosted.org/packages/96/a9/c0d2f83a53d40a4a41be14cea6a0bf9e668ffcf8b004bd65633f433050c0/nvidia_cusparse_cu12-12.3.1.170-py3-none-manylinux2014_aarch64.whl", hash = "sha256:9d32f62896231ebe0480efd8a7f702e143c98cfaa0e8a76df3386c1ba2b54df3", size = 207381987 },
    { url = "https://files.pythonhosted.org/packages/db/f7/97a9ea26ed4bbbfc2d470994b8b4f338ef663be97b8f677519ac195e113d/nvidia_cusparse_cu12-12.3.1.170-py3-none-manylinux2014_x86_64.whl", hash = "sha256:ea4f11a2904e2a8dc4b1833cc1b5181cde564edd0d5cd33e3c168eff2d1863f1", size = 207454763 },
]

[[package]]
name = "nvidia-cusparselt-cu12"
version = "0.6.2"
source = { registry = "https://pypi.org/simple" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/98/8e/675498726c605c9441cf46653bd29cb1b8666da1fb1469ffa25f67f20c58/nvidia_cusparselt_cu12-0.6.2-py3-none-manylinux2014_aarch64.whl", hash = "sha256:067a7f6d03ea0d4841c85f0c6f1991c5dda98211f6302cb83a4ab234ee95bef8", size = 149422781 },
    { url = "https://files.pythonhosted.org/packages/78/a8/bcbb63b53a4b1234feeafb65544ee55495e1bb37ec31b999b963cbccfd1d/nvidia_cusparselt_cu12-0.6.2-py3-none-manylinux2014_x86_64.whl", hash = "sha256:df2c24502fd76ebafe7457dbc4716b2fec071aabaed4fb7691a201cde03704d9", size = 150057751 },
]

[[package]]
name = "nvidia-nccl-cu12"
version = "2.21.5"
source = { registry = "https://pypi.org/simple" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/df/99/12cd266d6233f47d00daf3a72739872bdc10267d0383508b0b9c84a18bb6/nvidia_nccl_cu12-2.21.5-py3-none-manylinux2014_x86_64.whl", hash = "sha256:8579076d30a8c24988834445f8d633c697d42397e92ffc3f63fa26766d25e0a0", size = 188654414 },
]

[[package]]
name = "nvidia-nvjitlink-cu12"
version = "12.4.127"
source = { registry = "https://pypi.org/simple" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/02/45/239d52c05074898a80a900f49b1615d81c07fceadd5ad6c4f86a987c0bc4/nvidia_nvjitlink_cu12-12.4.127-py3-none-manylinux2014_aarch64.whl", hash = "sha256:4abe7fef64914ccfa909bc2ba39739670ecc9e820c83ccc7a6ed414122599b83", size = 20552510 },
    { url = "https://files.pythonhosted.org/packages/ff/ff/847841bacfbefc97a00036e0fce5a0f086b640756dc38caea5e1bb002655/nvidia_nvjitlink_cu12-12.4.127-py3-none-manylinux2014_x86_64.whl", hash = "sha256:06b3b9b25bf3f8af351d664978ca26a16d2c5127dbd53c0497e28d1fb9611d57", size = 21066810 },
]

[[package]]
name = "nvidia-nvtx-cu12"
version = "12.4.127"
source = { registry = "https://pypi.org/simple" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/06/39/471f581edbb7804b39e8063d92fc8305bdc7a80ae5c07dbe6ea5c50d14a5/nvidia_nvtx_cu12-12.4.127-py3-none-manylinux2014_aarch64.whl", hash = "sha256:7959ad635db13edf4fc65c06a6e9f9e55fc2f92596db928d169c0bb031e88ef3", size = 100417 },
    { url = "https://files.pythonhosted.org/packages/87/20/199b8713428322a2f22b722c62b8cc278cc53dffa9705d744484b5035ee9/nvidia_nvtx_cu12-12.4.127-py3-none-manylinux2014_x86_64.whl", hash = "sha256:781e950d9b9f60d8241ccea575b32f5105a5baf4c2351cab5256a24869f12a1a", size = 99144 },
]

[[package]]
name = "openai"
version = "1.70.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "anyio" },
    { name = "distro" },
    { name = "httpx" },
    { name = "jiter" },
    { name = "pydantic" },
    { name = "sniffio" },
    { name = "tqdm" },
    { name = "typing-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/87/f5/ae0f3cd226c2993b4ac1cc4b5f6ca099764689f403c14922c9356accec66/openai-1.70.0.tar.gz", hash = "sha256:e52a8d54c3efeb08cf58539b5b21a5abef25368b5432965e4de88cdf4e091b2b", size = 409640 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/e2/39/c4b38317d2c702c4bc763957735aaeaf30dfc43b5b824121c49a4ba7ba0f/openai-1.70.0-py3-none-any.whl", hash = "sha256:f6438d053fd8b2e05fd6bef70871e832d9bbdf55e119d0ac5b92726f1ae6f614", size = 599070 },
]

[[package]]
name = "packaging"
version = "24.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/d0/63/68dbb6eb2de9cb10ee4c9c14a0148804425e13c4fb20d61cce69f53106da/packaging-24.2.tar.gz", hash = "sha256:c228a6dc5e932d346bc5739379109d49e8853dd8223571c7c5b55260edc0b97f", size = 163950 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/88/ef/eb23f262cca3c0c4eb7ab1933c3b1f03d021f2c48f54763065b6f0e321be/packaging-24.2-py3-none-any.whl", hash = "sha256:09abb1bccd265c01f4a3aa3f7a7db064b36514d2cba19a2f694fe6150451a759", size = 65451 },
]

[[package]]
name = "pandas"
version = "2.2.3"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "numpy" },
    { name = "python-dateutil" },
    { name = "pytz" },
    { name = "tzdata" },
]
sdist = { url = "https://files.pythonhosted.org/packages/9c/d6/9f8431bacc2e19dca897724cd097b1bb224a6ad5433784a44b587c7c13af/pandas-2.2.3.tar.gz", hash = "sha256:4f18ba62b61d7e192368b84517265a99b4d7ee8912f8708660fb4a366cc82667", size = 4399213 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/aa/70/c853aec59839bceed032d52010ff5f1b8d87dc3114b762e4ba2727661a3b/pandas-2.2.3-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:1948ddde24197a0f7add2bdc4ca83bf2b1ef84a1bc8ccffd95eda17fd836ecb5", size = 12580827 },
    { url = "https://files.pythonhosted.org/packages/99/f2/c4527768739ffa4469b2b4fff05aa3768a478aed89a2f271a79a40eee984/pandas-2.2.3-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:381175499d3802cde0eabbaf6324cce0c4f5d52ca6f8c377c29ad442f50f6348", size = 11303897 },
    { url = "https://files.pythonhosted.org/packages/ed/12/86c1747ea27989d7a4064f806ce2bae2c6d575b950be087837bdfcabacc9/pandas-2.2.3-cp310-cp310-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:d9c45366def9a3dd85a6454c0e7908f2b3b8e9c138f5dc38fed7ce720d8453ed", size = 66480908 },
    { url = "https://files.pythonhosted.org/packages/44/50/7db2cd5e6373ae796f0ddad3675268c8d59fb6076e66f0c339d61cea886b/pandas-2.2.3-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:86976a1c5b25ae3f8ccae3a5306e443569ee3c3faf444dfd0f41cda24667ad57", size = 13064210 },
    { url = "https://files.pythonhosted.org/packages/61/61/a89015a6d5536cb0d6c3ba02cebed51a95538cf83472975275e28ebf7d0c/pandas-2.2.3-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:b8661b0238a69d7aafe156b7fa86c44b881387509653fdf857bebc5e4008ad42", size = 16754292 },
    { url = "https://files.pythonhosted.org/packages/ce/0d/4cc7b69ce37fac07645a94e1d4b0880b15999494372c1523508511b09e40/pandas-2.2.3-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:37e0aced3e8f539eccf2e099f65cdb9c8aa85109b0be6e93e2baff94264bdc6f", size = 14416379 },
    { url = "https://files.pythonhosted.org/packages/31/9e/6ebb433de864a6cd45716af52a4d7a8c3c9aaf3a98368e61db9e69e69a9c/pandas-2.2.3-cp310-cp310-win_amd64.whl", hash = "sha256:56534ce0746a58afaf7942ba4863e0ef81c9c50d3f0ae93e9497d6a41a057645", size = 11598471 },
    { url = "https://files.pythonhosted.org/packages/a8/44/d9502bf0ed197ba9bf1103c9867d5904ddcaf869e52329787fc54ed70cc8/pandas-2.2.3-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:66108071e1b935240e74525006034333f98bcdb87ea116de573a6a0dccb6c039", size = 12602222 },
    { url = "https://files.pythonhosted.org/packages/52/11/9eac327a38834f162b8250aab32a6781339c69afe7574368fffe46387edf/pandas-2.2.3-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:7c2875855b0ff77b2a64a0365e24455d9990730d6431b9e0ee18ad8acee13dbd", size = 11321274 },
    { url = "https://files.pythonhosted.org/packages/45/fb/c4beeb084718598ba19aa9f5abbc8aed8b42f90930da861fcb1acdb54c3a/pandas-2.2.3-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:cd8d0c3be0515c12fed0bdbae072551c8b54b7192c7b1fda0ba56059a0179698", size = 15579836 },
    { url = "https://files.pythonhosted.org/packages/cd/5f/4dba1d39bb9c38d574a9a22548c540177f78ea47b32f99c0ff2ec499fac5/pandas-2.2.3-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:c124333816c3a9b03fbeef3a9f230ba9a737e9e5bb4060aa2107a86cc0a497fc", size = 13058505 },
    { url = "https://files.pythonhosted.org/packages/b9/57/708135b90391995361636634df1f1130d03ba456e95bcf576fada459115a/pandas-2.2.3-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:63cc132e40a2e084cf01adf0775b15ac515ba905d7dcca47e9a251819c575ef3", size = 16744420 },
    { url = "https://files.pythonhosted.org/packages/86/4a/03ed6b7ee323cf30404265c284cee9c65c56a212e0a08d9ee06984ba2240/pandas-2.2.3-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:29401dbfa9ad77319367d36940cd8a0b3a11aba16063e39632d98b0e931ddf32", size = 14440457 },
    { url = "https://files.pythonhosted.org/packages/ed/8c/87ddf1fcb55d11f9f847e3c69bb1c6f8e46e2f40ab1a2d2abadb2401b007/pandas-2.2.3-cp311-cp311-win_amd64.whl", hash = "sha256:3fc6873a41186404dad67245896a6e440baacc92f5b716ccd1bc9ed2995ab2c5", size = 11617166 },
    { url = "https://files.pythonhosted.org/packages/17/a3/fb2734118db0af37ea7433f57f722c0a56687e14b14690edff0cdb4b7e58/pandas-2.2.3-cp312-cp312-macosx_10_9_x86_64.whl", hash = "sha256:b1d432e8d08679a40e2a6d8b2f9770a5c21793a6f9f47fdd52c5ce1948a5a8a9", size = 12529893 },
    { url = "https://files.pythonhosted.org/packages/e1/0c/ad295fd74bfac85358fd579e271cded3ac969de81f62dd0142c426b9da91/pandas-2.2.3-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:a5a1595fe639f5988ba6a8e5bc9649af3baf26df3998a0abe56c02609392e0a4", size = 11363475 },
    { url = "https://files.pythonhosted.org/packages/c6/2a/4bba3f03f7d07207481fed47f5b35f556c7441acddc368ec43d6643c5777/pandas-2.2.3-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:5de54125a92bb4d1c051c0659e6fcb75256bf799a732a87184e5ea503965bce3", size = 15188645 },
    { url = "https://files.pythonhosted.org/packages/38/f8/d8fddee9ed0d0c0f4a2132c1dfcf0e3e53265055da8df952a53e7eaf178c/pandas-2.2.3-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:fffb8ae78d8af97f849404f21411c95062db1496aeb3e56f146f0355c9989319", size = 12739445 },
    { url = "https://files.pythonhosted.org/packages/20/e8/45a05d9c39d2cea61ab175dbe6a2de1d05b679e8de2011da4ee190d7e748/pandas-2.2.3-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:6dfcb5ee8d4d50c06a51c2fffa6cff6272098ad6540aed1a76d15fb9318194d8", size = 16359235 },
    { url = "https://files.pythonhosted.org/packages/1d/99/617d07a6a5e429ff90c90da64d428516605a1ec7d7bea494235e1c3882de/pandas-2.2.3-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:062309c1b9ea12a50e8ce661145c6aab431b1e99530d3cd60640e255778bd43a", size = 14056756 },
    { url = "https://files.pythonhosted.org/packages/29/d4/1244ab8edf173a10fd601f7e13b9566c1b525c4f365d6bee918e68381889/pandas-2.2.3-cp312-cp312-win_amd64.whl", hash = "sha256:59ef3764d0fe818125a5097d2ae867ca3fa64df032331b7e0917cf5d7bf66b13", size = 11504248 },
    { url = "https://files.pythonhosted.org/packages/64/22/3b8f4e0ed70644e85cfdcd57454686b9057c6c38d2f74fe4b8bc2527214a/pandas-2.2.3-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:f00d1345d84d8c86a63e476bb4955e46458b304b9575dcf71102b5c705320015", size = 12477643 },
    { url = "https://files.pythonhosted.org/packages/e4/93/b3f5d1838500e22c8d793625da672f3eec046b1a99257666c94446969282/pandas-2.2.3-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:3508d914817e153ad359d7e069d752cdd736a247c322d932eb89e6bc84217f28", size = 11281573 },
    { url = "https://files.pythonhosted.org/packages/f5/94/6c79b07f0e5aab1dcfa35a75f4817f5c4f677931d4234afcd75f0e6a66ca/pandas-2.2.3-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:22a9d949bfc9a502d320aa04e5d02feab689d61da4e7764b62c30b991c42c5f0", size = 15196085 },
    { url = "https://files.pythonhosted.org/packages/e8/31/aa8da88ca0eadbabd0a639788a6da13bb2ff6edbbb9f29aa786450a30a91/pandas-2.2.3-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:f3a255b2c19987fbbe62a9dfd6cff7ff2aa9ccab3fc75218fd4b7530f01efa24", size = 12711809 },
    { url = "https://files.pythonhosted.org/packages/ee/7c/c6dbdb0cb2a4344cacfb8de1c5808ca885b2e4dcfde8008266608f9372af/pandas-2.2.3-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:800250ecdadb6d9c78eae4990da62743b857b470883fa27f652db8bdde7f6659", size = 16356316 },
    { url = "https://files.pythonhosted.org/packages/57/b7/8b757e7d92023b832869fa8881a992696a0bfe2e26f72c9ae9f255988d42/pandas-2.2.3-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:6374c452ff3ec675a8f46fd9ab25c4ad0ba590b71cf0656f8b6daa5202bca3fb", size = 14022055 },
    { url = "https://files.pythonhosted.org/packages/3b/bc/4b18e2b8c002572c5a441a64826252ce5da2aa738855747247a971988043/pandas-2.2.3-cp313-cp313-win_amd64.whl", hash = "sha256:61c5ad4043f791b61dd4752191d9f07f0ae412515d59ba8f005832a532f8736d", size = 11481175 },
    { url = "https://files.pythonhosted.org/packages/76/a3/a5d88146815e972d40d19247b2c162e88213ef51c7c25993942c39dbf41d/pandas-2.2.3-cp313-cp313t-macosx_10_13_x86_64.whl", hash = "sha256:3b71f27954685ee685317063bf13c7709a7ba74fc996b84fc6821c59b0f06468", size = 12615650 },
    { url = "https://files.pythonhosted.org/packages/9c/8c/f0fd18f6140ddafc0c24122c8a964e48294acc579d47def376fef12bcb4a/pandas-2.2.3-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:38cf8125c40dae9d5acc10fa66af8ea6fdf760b2714ee482ca691fc66e6fcb18", size = 11290177 },
    { url = "https://files.pythonhosted.org/packages/ed/f9/e995754eab9c0f14c6777401f7eece0943840b7a9fc932221c19d1abee9f/pandas-2.2.3-cp313-cp313t-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:ba96630bc17c875161df3818780af30e43be9b166ce51c9a18c1feae342906c2", size = 14651526 },
    { url = "https://files.pythonhosted.org/packages/25/b0/98d6ae2e1abac4f35230aa756005e8654649d305df9a28b16b9ae4353bff/pandas-2.2.3-cp313-cp313t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:1db71525a1538b30142094edb9adc10be3f3e176748cd7acc2240c2f2e5aa3a4", size = 11871013 },
    { url = "https://files.pythonhosted.org/packages/cc/57/0f72a10f9db6a4628744c8e8f0df4e6e21de01212c7c981d31e50ffc8328/pandas-2.2.3-cp313-cp313t-musllinux_1_2_aarch64.whl", hash = "sha256:15c0e1e02e93116177d29ff83e8b1619c93ddc9c49083f237d4312337a61165d", size = 15711620 },
    { url = "https://files.pythonhosted.org/packages/ab/5f/b38085618b950b79d2d9164a711c52b10aefc0ae6833b96f626b7021b2ed/pandas-2.2.3-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:ad5b65698ab28ed8d7f18790a0dc58005c7629f227be9ecc1072aa74c0c1d43a", size = 13098436 },
    { url = "https://files.pythonhosted.org/packages/ca/8c/8848a4c9b8fdf5a534fe2077af948bf53cd713d77ffbcd7bd15710348fd7/pandas-2.2.3-cp39-cp39-macosx_10_9_x86_64.whl", hash = "sha256:bc6b93f9b966093cb0fd62ff1a7e4c09e6d546ad7c1de191767baffc57628f39", size = 12595535 },
    { url = "https://files.pythonhosted.org/packages/9c/b9/5cead4f63b6d31bdefeb21a679bc5a7f4aaf262ca7e07e2bc1c341b68470/pandas-2.2.3-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:5dbca4c1acd72e8eeef4753eeca07de9b1db4f398669d5994086f788a5d7cc30", size = 11319822 },
    { url = "https://files.pythonhosted.org/packages/31/af/89e35619fb573366fa68dc26dad6ad2c08c17b8004aad6d98f1a31ce4bb3/pandas-2.2.3-cp39-cp39-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:8cd6d7cc958a3910f934ea8dbdf17b2364827bb4dafc38ce6eef6bb3d65ff09c", size = 15625439 },
    { url = "https://files.pythonhosted.org/packages/3d/dd/bed19c2974296661493d7acc4407b1d2db4e2a482197df100f8f965b6225/pandas-2.2.3-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:99df71520d25fade9db7c1076ac94eb994f4d2673ef2aa2e86ee039b6746d20c", size = 13068928 },
    { url = "https://files.pythonhosted.org/packages/31/a3/18508e10a31ea108d746c848b5a05c0711e0278fa0d6f1c52a8ec52b80a5/pandas-2.2.3-cp39-cp39-musllinux_1_2_aarch64.whl", hash = "sha256:31d0ced62d4ea3e231a9f228366919a5ea0b07440d9d4dac345376fd8e1477ea", size = 16783266 },
    { url = "https://files.pythonhosted.org/packages/c4/a5/3429bd13d82bebc78f4d78c3945efedef63a7cd0c15c17b2eeb838d1121f/pandas-2.2.3-cp39-cp39-musllinux_1_2_x86_64.whl", hash = "sha256:7eee9e7cea6adf3e3d24e304ac6b8300646e2a5d1cd3a3c2abed9101b0846761", size = 14450871 },
    { url = "https://files.pythonhosted.org/packages/2f/49/5c30646e96c684570925b772eac4eb0a8cb0ca590fa978f56c5d3ae73ea1/pandas-2.2.3-cp39-cp39-win_amd64.whl", hash = "sha256:4850ba03528b6dd51d6c5d273c46f183f39a9baf3f0143e566b89450965b105e", size = 11618011 },
]

[[package]]
name = "pillow"
version = "11.1.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/f3/af/c097e544e7bd278333db77933e535098c259609c4eb3b85381109602fb5b/pillow-11.1.0.tar.gz", hash = "sha256:368da70808b36d73b4b390a8ffac11069f8a5c85f29eff1f1b01bcf3ef5b2a20", size = 46742715 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/50/1c/2dcea34ac3d7bc96a1fd1bd0a6e06a57c67167fec2cff8d95d88229a8817/pillow-11.1.0-cp310-cp310-macosx_10_10_x86_64.whl", hash = "sha256:e1abe69aca89514737465752b4bcaf8016de61b3be1397a8fc260ba33321b3a8", size = 3229983 },
    { url = "https://files.pythonhosted.org/packages/14/ca/6bec3df25e4c88432681de94a3531cc738bd85dea6c7aa6ab6f81ad8bd11/pillow-11.1.0-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:c640e5a06869c75994624551f45e5506e4256562ead981cce820d5ab39ae2192", size = 3101831 },
    { url = "https://files.pythonhosted.org/packages/d4/2c/668e18e5521e46eb9667b09e501d8e07049eb5bfe39d56be0724a43117e6/pillow-11.1.0-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:a07dba04c5e22824816b2615ad7a7484432d7f540e6fa86af60d2de57b0fcee2", size = 4314074 },
    { url = "https://files.pythonhosted.org/packages/02/80/79f99b714f0fc25f6a8499ecfd1f810df12aec170ea1e32a4f75746051ce/pillow-11.1.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:e267b0ed063341f3e60acd25c05200df4193e15a4a5807075cd71225a2386e26", size = 4394933 },
    { url = "https://files.pythonhosted.org/packages/81/aa/8d4ad25dc11fd10a2001d5b8a80fdc0e564ac33b293bdfe04ed387e0fd95/pillow-11.1.0-cp310-cp310-manylinux_2_28_aarch64.whl", hash = "sha256:bd165131fd51697e22421d0e467997ad31621b74bfc0b75956608cb2906dda07", size = 4353349 },
    { url = "https://files.pythonhosted.org/packages/84/7a/cd0c3eaf4a28cb2a74bdd19129f7726277a7f30c4f8424cd27a62987d864/pillow-11.1.0-cp310-cp310-manylinux_2_28_x86_64.whl", hash = "sha256:abc56501c3fd148d60659aae0af6ddc149660469082859fa7b066a298bde9482", size = 4476532 },
    { url = "https://files.pythonhosted.org/packages/8f/8b/a907fdd3ae8f01c7670dfb1499c53c28e217c338b47a813af8d815e7ce97/pillow-11.1.0-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:54ce1c9a16a9561b6d6d8cb30089ab1e5eb66918cb47d457bd996ef34182922e", size = 4279789 },
    { url = "https://files.pythonhosted.org/packages/6f/9a/9f139d9e8cccd661c3efbf6898967a9a337eb2e9be2b454ba0a09533100d/pillow-11.1.0-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:73ddde795ee9b06257dac5ad42fcb07f3b9b813f8c1f7f870f402f4dc54b5269", size = 4413131 },
    { url = "https://files.pythonhosted.org/packages/a8/68/0d8d461f42a3f37432203c8e6df94da10ac8081b6d35af1c203bf3111088/pillow-11.1.0-cp310-cp310-win32.whl", hash = "sha256:3a5fe20a7b66e8135d7fd617b13272626a28278d0e578c98720d9ba4b2439d49", size = 2291213 },
    { url = "https://files.pythonhosted.org/packages/14/81/d0dff759a74ba87715509af9f6cb21fa21d93b02b3316ed43bda83664db9/pillow-11.1.0-cp310-cp310-win_amd64.whl", hash = "sha256:b6123aa4a59d75f06e9dd3dac5bf8bc9aa383121bb3dd9a7a612e05eabc9961a", size = 2625725 },
    { url = "https://files.pythonhosted.org/packages/ce/1f/8d50c096a1d58ef0584ddc37e6f602828515219e9d2428e14ce50f5ecad1/pillow-11.1.0-cp310-cp310-win_arm64.whl", hash = "sha256:a76da0a31da6fcae4210aa94fd779c65c75786bc9af06289cd1c184451ef7a65", size = 2375213 },
    { url = "https://files.pythonhosted.org/packages/dd/d6/2000bfd8d5414fb70cbbe52c8332f2283ff30ed66a9cde42716c8ecbe22c/pillow-11.1.0-cp311-cp311-macosx_10_10_x86_64.whl", hash = "sha256:e06695e0326d05b06833b40b7ef477e475d0b1ba3a6d27da1bb48c23209bf457", size = 3229968 },
    { url = "https://files.pythonhosted.org/packages/d9/45/3fe487010dd9ce0a06adf9b8ff4f273cc0a44536e234b0fad3532a42c15b/pillow-11.1.0-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:96f82000e12f23e4f29346e42702b6ed9a2f2fea34a740dd5ffffcc8c539eb35", size = 3101806 },
    { url = "https://files.pythonhosted.org/packages/e3/72/776b3629c47d9d5f1c160113158a7a7ad177688d3a1159cd3b62ded5a33a/pillow-11.1.0-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:a3cd561ded2cf2bbae44d4605837221b987c216cff94f49dfeed63488bb228d2", size = 4322283 },
    { url = "https://files.pythonhosted.org/packages/e4/c2/e25199e7e4e71d64eeb869f5b72c7ddec70e0a87926398785ab944d92375/pillow-11.1.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:f189805c8be5ca5add39e6f899e6ce2ed824e65fb45f3c28cb2841911da19070", size = 4402945 },
    { url = "https://files.pythonhosted.org/packages/c1/ed/51d6136c9d5911f78632b1b86c45241c712c5a80ed7fa7f9120a5dff1eba/pillow-11.1.0-cp311-cp311-manylinux_2_28_aarch64.whl", hash = "sha256:dd0052e9db3474df30433f83a71b9b23bd9e4ef1de13d92df21a52c0303b8ab6", size = 4361228 },
    { url = "https://files.pythonhosted.org/packages/48/a4/fbfe9d5581d7b111b28f1d8c2762dee92e9821bb209af9fa83c940e507a0/pillow-11.1.0-cp311-cp311-manylinux_2_28_x86_64.whl", hash = "sha256:837060a8599b8f5d402e97197d4924f05a2e0d68756998345c829c33186217b1", size = 4484021 },
    { url = "https://files.pythonhosted.org/packages/39/db/0b3c1a5018117f3c1d4df671fb8e47d08937f27519e8614bbe86153b65a5/pillow-11.1.0-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:aa8dd43daa836b9a8128dbe7d923423e5ad86f50a7a14dc688194b7be5c0dea2", size = 4287449 },
    { url = "https://files.pythonhosted.org/packages/d9/58/bc128da7fea8c89fc85e09f773c4901e95b5936000e6f303222490c052f3/pillow-11.1.0-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:0a2f91f8a8b367e7a57c6e91cd25af510168091fb89ec5146003e424e1558a96", size = 4419972 },
    { url = "https://files.pythonhosted.org/packages/5f/bb/58f34379bde9fe197f51841c5bbe8830c28bbb6d3801f16a83b8f2ad37df/pillow-11.1.0-cp311-cp311-win32.whl", hash = "sha256:c12fc111ef090845de2bb15009372175d76ac99969bdf31e2ce9b42e4b8cd88f", size = 2291201 },
    { url = "https://files.pythonhosted.org/packages/3a/c6/fce9255272bcf0c39e15abd2f8fd8429a954cf344469eaceb9d0d1366913/pillow-11.1.0-cp311-cp311-win_amd64.whl", hash = "sha256:fbd43429d0d7ed6533b25fc993861b8fd512c42d04514a0dd6337fb3ccf22761", size = 2625686 },
    { url = "https://files.pythonhosted.org/packages/c8/52/8ba066d569d932365509054859f74f2a9abee273edcef5cd75e4bc3e831e/pillow-11.1.0-cp311-cp311-win_arm64.whl", hash = "sha256:f7955ecf5609dee9442cbface754f2c6e541d9e6eda87fad7f7a989b0bdb9d71", size = 2375194 },
    { url = "https://files.pythonhosted.org/packages/95/20/9ce6ed62c91c073fcaa23d216e68289e19d95fb8188b9fb7a63d36771db8/pillow-11.1.0-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:2062ffb1d36544d42fcaa277b069c88b01bb7298f4efa06731a7fd6cc290b81a", size = 3226818 },
    { url = "https://files.pythonhosted.org/packages/b9/d8/f6004d98579a2596c098d1e30d10b248798cceff82d2b77aa914875bfea1/pillow-11.1.0-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:a85b653980faad27e88b141348707ceeef8a1186f75ecc600c395dcac19f385b", size = 3101662 },
    { url = "https://files.pythonhosted.org/packages/08/d9/892e705f90051c7a2574d9f24579c9e100c828700d78a63239676f960b74/pillow-11.1.0-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:9409c080586d1f683df3f184f20e36fb647f2e0bc3988094d4fd8c9f4eb1b3b3", size = 4329317 },
    { url = "https://files.pythonhosted.org/packages/8c/aa/7f29711f26680eab0bcd3ecdd6d23ed6bce180d82e3f6380fb7ae35fcf3b/pillow-11.1.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:7fdadc077553621911f27ce206ffcbec7d3f8d7b50e0da39f10997e8e2bb7f6a", size = 4412999 },
    { url = "https://files.pythonhosted.org/packages/c8/c4/8f0fe3b9e0f7196f6d0bbb151f9fba323d72a41da068610c4c960b16632a/pillow-11.1.0-cp312-cp312-manylinux_2_28_aarch64.whl", hash = "sha256:93a18841d09bcdd774dcdc308e4537e1f867b3dec059c131fde0327899734aa1", size = 4368819 },
    { url = "https://files.pythonhosted.org/packages/38/0d/84200ed6a871ce386ddc82904bfadc0c6b28b0c0ec78176871a4679e40b3/pillow-11.1.0-cp312-cp312-manylinux_2_28_x86_64.whl", hash = "sha256:9aa9aeddeed452b2f616ff5507459e7bab436916ccb10961c4a382cd3e03f47f", size = 4496081 },
    { url = "https://files.pythonhosted.org/packages/84/9c/9bcd66f714d7e25b64118e3952d52841a4babc6d97b6d28e2261c52045d4/pillow-11.1.0-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:3cdcdb0b896e981678eee140d882b70092dac83ac1cdf6b3a60e2216a73f2b91", size = 4296513 },
    { url = "https://files.pythonhosted.org/packages/db/61/ada2a226e22da011b45f7104c95ebda1b63dcbb0c378ad0f7c2a710f8fd2/pillow-11.1.0-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:36ba10b9cb413e7c7dfa3e189aba252deee0602c86c309799da5a74009ac7a1c", size = 4431298 },
    { url = "https://files.pythonhosted.org/packages/e7/c4/fc6e86750523f367923522014b821c11ebc5ad402e659d8c9d09b3c9d70c/pillow-11.1.0-cp312-cp312-win32.whl", hash = "sha256:cfd5cd998c2e36a862d0e27b2df63237e67273f2fc78f47445b14e73a810e7e6", size = 2291630 },
    { url = "https://files.pythonhosted.org/packages/08/5c/2104299949b9d504baf3f4d35f73dbd14ef31bbd1ddc2c1b66a5b7dfda44/pillow-11.1.0-cp312-cp312-win_amd64.whl", hash = "sha256:a697cd8ba0383bba3d2d3ada02b34ed268cb548b369943cd349007730c92bddf", size = 2626369 },
    { url = "https://files.pythonhosted.org/packages/37/f3/9b18362206b244167c958984b57c7f70a0289bfb59a530dd8af5f699b910/pillow-11.1.0-cp312-cp312-win_arm64.whl", hash = "sha256:4dd43a78897793f60766563969442020e90eb7847463eca901e41ba186a7d4a5", size = 2375240 },
    { url = "https://files.pythonhosted.org/packages/b3/31/9ca79cafdce364fd5c980cd3416c20ce1bebd235b470d262f9d24d810184/pillow-11.1.0-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:ae98e14432d458fc3de11a77ccb3ae65ddce70f730e7c76140653048c71bfcbc", size = 3226640 },
    { url = "https://files.pythonhosted.org/packages/ac/0f/ff07ad45a1f172a497aa393b13a9d81a32e1477ef0e869d030e3c1532521/pillow-11.1.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:cc1331b6d5a6e144aeb5e626f4375f5b7ae9934ba620c0ac6b3e43d5e683a0f0", size = 3101437 },
    { url = "https://files.pythonhosted.org/packages/08/2f/9906fca87a68d29ec4530be1f893149e0cb64a86d1f9f70a7cfcdfe8ae44/pillow-11.1.0-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:758e9d4ef15d3560214cddbc97b8ef3ef86ce04d62ddac17ad39ba87e89bd3b1", size = 4326605 },
    { url = "https://files.pythonhosted.org/packages/b0/0f/f3547ee15b145bc5c8b336401b2d4c9d9da67da9dcb572d7c0d4103d2c69/pillow-11.1.0-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:b523466b1a31d0dcef7c5be1f20b942919b62fd6e9a9be199d035509cbefc0ec", size = 4411173 },
    { url = "https://files.pythonhosted.org/packages/b1/df/bf8176aa5db515c5de584c5e00df9bab0713548fd780c82a86cba2c2fedb/pillow-11.1.0-cp313-cp313-manylinux_2_28_aarch64.whl", hash = "sha256:9044b5e4f7083f209c4e35aa5dd54b1dd5b112b108648f5c902ad586d4f945c5", size = 4369145 },
    { url = "https://files.pythonhosted.org/packages/de/7c/7433122d1cfadc740f577cb55526fdc39129a648ac65ce64db2eb7209277/pillow-11.1.0-cp313-cp313-manylinux_2_28_x86_64.whl", hash = "sha256:3764d53e09cdedd91bee65c2527815d315c6b90d7b8b79759cc48d7bf5d4f114", size = 4496340 },
    { url = "https://files.pythonhosted.org/packages/25/46/dd94b93ca6bd555588835f2504bd90c00d5438fe131cf01cfa0c5131a19d/pillow-11.1.0-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:31eba6bbdd27dde97b0174ddf0297d7a9c3a507a8a1480e1e60ef914fe23d352", size = 4296906 },
    { url = "https://files.pythonhosted.org/packages/a8/28/2f9d32014dfc7753e586db9add35b8a41b7a3b46540e965cb6d6bc607bd2/pillow-11.1.0-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:b5d658fbd9f0d6eea113aea286b21d3cd4d3fd978157cbf2447a6035916506d3", size = 4431759 },
    { url = "https://files.pythonhosted.org/packages/33/48/19c2cbe7403870fbe8b7737d19eb013f46299cdfe4501573367f6396c775/pillow-11.1.0-cp313-cp313-win32.whl", hash = "sha256:f86d3a7a9af5d826744fabf4afd15b9dfef44fe69a98541f666f66fbb8d3fef9", size = 2291657 },
    { url = "https://files.pythonhosted.org/packages/3b/ad/285c556747d34c399f332ba7c1a595ba245796ef3e22eae190f5364bb62b/pillow-11.1.0-cp313-cp313-win_amd64.whl", hash = "sha256:593c5fd6be85da83656b93ffcccc2312d2d149d251e98588b14fbc288fd8909c", size = 2626304 },
    { url = "https://files.pythonhosted.org/packages/e5/7b/ef35a71163bf36db06e9c8729608f78dedf032fc8313d19bd4be5c2588f3/pillow-11.1.0-cp313-cp313-win_arm64.whl", hash = "sha256:11633d58b6ee5733bde153a8dafd25e505ea3d32e261accd388827ee987baf65", size = 2375117 },
    { url = "https://files.pythonhosted.org/packages/79/30/77f54228401e84d6791354888549b45824ab0ffde659bafa67956303a09f/pillow-11.1.0-cp313-cp313t-macosx_10_13_x86_64.whl", hash = "sha256:70ca5ef3b3b1c4a0812b5c63c57c23b63e53bc38e758b37a951e5bc466449861", size = 3230060 },
    { url = "https://files.pythonhosted.org/packages/ce/b1/56723b74b07dd64c1010fee011951ea9c35a43d8020acd03111f14298225/pillow-11.1.0-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:8000376f139d4d38d6851eb149b321a52bb8893a88dae8ee7d95840431977081", size = 3106192 },
    { url = "https://files.pythonhosted.org/packages/e1/cd/7bf7180e08f80a4dcc6b4c3a0aa9e0b0ae57168562726a05dc8aa8fa66b0/pillow-11.1.0-cp313-cp313t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:9ee85f0696a17dd28fbcfceb59f9510aa71934b483d1f5601d1030c3c8304f3c", size = 4446805 },
    { url = "https://files.pythonhosted.org/packages/97/42/87c856ea30c8ed97e8efbe672b58c8304dee0573f8c7cab62ae9e31db6ae/pillow-11.1.0-cp313-cp313t-manylinux_2_28_x86_64.whl", hash = "sha256:dd0e081319328928531df7a0e63621caf67652c8464303fd102141b785ef9547", size = 4530623 },
    { url = "https://files.pythonhosted.org/packages/ff/41/026879e90c84a88e33fb00cc6bd915ac2743c67e87a18f80270dfe3c2041/pillow-11.1.0-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:e63e4e5081de46517099dc30abe418122f54531a6ae2ebc8680bcd7096860eab", size = 4465191 },
    { url = "https://files.pythonhosted.org/packages/e5/fb/a7960e838bc5df57a2ce23183bfd2290d97c33028b96bde332a9057834d3/pillow-11.1.0-cp313-cp313t-win32.whl", hash = "sha256:dda60aa465b861324e65a78c9f5cf0f4bc713e4309f83bc387be158b077963d9", size = 2295494 },
    { url = "https://files.pythonhosted.org/packages/d7/6c/6ec83ee2f6f0fda8d4cf89045c6be4b0373ebfc363ba8538f8c999f63fcd/pillow-11.1.0-cp313-cp313t-win_amd64.whl", hash = "sha256:ad5db5781c774ab9a9b2c4302bbf0c1014960a0a7be63278d13ae6fdf88126fe", size = 2631595 },
    { url = "https://files.pythonhosted.org/packages/cf/6c/41c21c6c8af92b9fea313aa47c75de49e2f9a467964ee33eb0135d47eb64/pillow-11.1.0-cp313-cp313t-win_arm64.whl", hash = "sha256:67cd427c68926108778a9005f2a04adbd5e67c442ed21d95389fe1d595458756", size = 2377651 },
    { url = "https://files.pythonhosted.org/packages/9a/1f/9df5ac77491fddd2e36c352d16976dc11fbe6ab842f5df85fd7e31b847b9/pillow-11.1.0-cp39-cp39-macosx_10_10_x86_64.whl", hash = "sha256:bf902d7413c82a1bfa08b06a070876132a5ae6b2388e2712aab3a7cbc02205c6", size = 3229995 },
    { url = "https://files.pythonhosted.org/packages/a6/62/c7b359e924dca274173b04922ac06aa63614f7e934d132f2fe1d852509aa/pillow-11.1.0-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:c1eec9d950b6fe688edee07138993e54ee4ae634c51443cfb7c1e7613322718e", size = 3101890 },
    { url = "https://files.pythonhosted.org/packages/7b/63/136f21340a434de895b62bcf2c386005a8aa24066c4facd619f5e0e9f283/pillow-11.1.0-cp39-cp39-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:8e275ee4cb11c262bd108ab2081f750db2a1c0b8c12c1897f27b160c8bd57bbc", size = 4310366 },
    { url = "https://files.pythonhosted.org/packages/f6/46/0bd0ca03d9d1164a7fa33d285ef6d1c438e963d0c8770e4c5b3737ef5abe/pillow-11.1.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:4db853948ce4e718f2fc775b75c37ba2efb6aaea41a1a5fc57f0af59eee774b2", size = 4391582 },
    { url = "https://files.pythonhosted.org/packages/0c/55/f182db572b28bd833b8e806f933f782ceb2df64c40e4d8bd3d4226a46eca/pillow-11.1.0-cp39-cp39-manylinux_2_28_aarch64.whl", hash = "sha256:ab8a209b8485d3db694fa97a896d96dd6533d63c22829043fd9de627060beade", size = 4350278 },
    { url = "https://files.pythonhosted.org/packages/75/fb/e330fdbbcbc4744214b5f53b84d9d8a9f4ffbebc2e9c2ac10475386e3296/pillow-11.1.0-cp39-cp39-manylinux_2_28_x86_64.whl", hash = "sha256:54251ef02a2309b5eec99d151ebf5c9904b77976c8abdcbce7891ed22df53884", size = 4471768 },
    { url = "https://files.pythonhosted.org/packages/eb/51/20ee6c4da4448d7a67ffb720a5fcdb965115a78e211a1f58f9845ae15f86/pillow-11.1.0-cp39-cp39-musllinux_1_2_aarch64.whl", hash = "sha256:5bb94705aea800051a743aa4874bb1397d4695fb0583ba5e425ee0328757f196", size = 4276549 },
    { url = "https://files.pythonhosted.org/packages/37/f2/a25c0bdaa6d6fd5cc3d4a6f65b5a7ea46e7af58bee00a98efe0a5af79c58/pillow-11.1.0-cp39-cp39-musllinux_1_2_x86_64.whl", hash = "sha256:89dbdb3e6e9594d512780a5a1c42801879628b38e3efc7038094430844e271d8", size = 4409350 },
    { url = "https://files.pythonhosted.org/packages/12/a7/06687947604cd3e47abeea1b78b65d34ffce7feab03cfe0dd985f115dca3/pillow-11.1.0-cp39-cp39-win32.whl", hash = "sha256:e5449ca63da169a2e6068dd0e2fcc8d91f9558aba89ff6d02121ca8ab11e79e5", size = 2291271 },
    { url = "https://files.pythonhosted.org/packages/21/a6/f51d47675940b5c63b08ff0575b3518428b4acb891f88526fa4ee1edab6f/pillow-11.1.0-cp39-cp39-win_amd64.whl", hash = "sha256:3362c6ca227e65c54bf71a5f88b3d4565ff1bcbc63ae72c34b07bbb1cc59a43f", size = 2625783 },
    { url = "https://files.pythonhosted.org/packages/95/56/97750bd33e68648fa432dfadcb8ede7624bd905822d42262d34bcebdd9d7/pillow-11.1.0-cp39-cp39-win_arm64.whl", hash = "sha256:b20be51b37a75cc54c2c55def3fa2c65bb94ba859dde241cd0a4fd302de5ae0a", size = 2375193 },
    { url = "https://files.pythonhosted.org/packages/fa/c5/389961578fb677b8b3244fcd934f720ed25a148b9a5cc81c91bdf59d8588/pillow-11.1.0-pp310-pypy310_pp73-macosx_10_15_x86_64.whl", hash = "sha256:8c730dc3a83e5ac137fbc92dfcfe1511ce3b2b5d7578315b63dbbb76f7f51d90", size = 3198345 },
    { url = "https://files.pythonhosted.org/packages/c4/fa/803c0e50ffee74d4b965229e816af55276eac1d5806712de86f9371858fd/pillow-11.1.0-pp310-pypy310_pp73-macosx_11_0_arm64.whl", hash = "sha256:7d33d2fae0e8b170b6a6c57400e077412240f6f5bb2a342cf1ee512a787942bb", size = 3072938 },
    { url = "https://files.pythonhosted.org/packages/dc/67/2a3a5f8012b5d8c63fe53958ba906c1b1d0482ebed5618057ef4d22f8076/pillow-11.1.0-pp310-pypy310_pp73-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:a8d65b38173085f24bc07f8b6c505cbb7418009fa1a1fcb111b1f4961814a442", size = 3400049 },
    { url = "https://files.pythonhosted.org/packages/e5/a0/514f0d317446c98c478d1872497eb92e7cde67003fed74f696441e647446/pillow-11.1.0-pp310-pypy310_pp73-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:015c6e863faa4779251436db398ae75051469f7c903b043a48f078e437656f83", size = 3422431 },
    { url = "https://files.pythonhosted.org/packages/cd/00/20f40a935514037b7d3f87adfc87d2c538430ea625b63b3af8c3f5578e72/pillow-11.1.0-pp310-pypy310_pp73-manylinux_2_28_aarch64.whl", hash = "sha256:d44ff19eea13ae4acdaaab0179fa68c0c6f2f45d66a4d8ec1eda7d6cecbcc15f", size = 3446208 },
    { url = "https://files.pythonhosted.org/packages/28/3c/7de681727963043e093c72e6c3348411b0185eab3263100d4490234ba2f6/pillow-11.1.0-pp310-pypy310_pp73-manylinux_2_28_x86_64.whl", hash = "sha256:d3d8da4a631471dfaf94c10c85f5277b1f8e42ac42bade1ac67da4b4a7359b73", size = 3509746 },
    { url = "https://files.pythonhosted.org/packages/41/67/936f9814bdd74b2dfd4822f1f7725ab5d8ff4103919a1664eb4874c58b2f/pillow-11.1.0-pp310-pypy310_pp73-win_amd64.whl", hash = "sha256:4637b88343166249fe8aa94e7c4a62a180c4b3898283bb5d3d2fd5fe10d8e4e0", size = 2626353 },
]

[[package]]
name = "pluggy"
version = "1.5.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/96/2d/02d4312c973c6050a18b314a5ad0b3210edb65a906f868e31c111dede4a6/pluggy-1.5.0.tar.gz", hash = "sha256:2cffa88e94fdc978c4c574f15f9e59b7f4201d439195c3715ca9e2486f1d0cf1", size = 67955 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/88/5f/e351af9a41f866ac3f1fac4ca0613908d9a41741cfcf2228f4ad853b697d/pluggy-1.5.0-py3-none-any.whl", hash = "sha256:44e1ad92c8ca002de6377e165f3e0f1be63266ab4d554740532335b9d75ea669", size = 20556 },
]

[[package]]
name = "propcache"
version = "0.3.1"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/07/c8/fdc6686a986feae3541ea23dcaa661bd93972d3940460646c6bb96e21c40/propcache-0.3.1.tar.gz", hash = "sha256:40d980c33765359098837527e18eddefc9a24cea5b45e078a7f3bb5b032c6ecf", size = 43651 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/20/56/e27c136101addf877c8291dbda1b3b86ae848f3837ce758510a0d806c92f/propcache-0.3.1-cp310-cp310-macosx_10_9_universal2.whl", hash = "sha256:f27785888d2fdd918bc36de8b8739f2d6c791399552333721b58193f68ea3e98", size = 80224 },
    { url = "https://files.pythonhosted.org/packages/63/bd/88e98836544c4f04db97eefd23b037c2002fa173dd2772301c61cd3085f9/propcache-0.3.1-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:d4e89cde74154c7b5957f87a355bb9c8ec929c167b59c83d90654ea36aeb6180", size = 46491 },
    { url = "https://files.pythonhosted.org/packages/15/43/0b8eb2a55753c4a574fc0899885da504b521068d3b08ca56774cad0bea2b/propcache-0.3.1-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:730178f476ef03d3d4d255f0c9fa186cb1d13fd33ffe89d39f2cda4da90ceb71", size = 45927 },
    { url = "https://files.pythonhosted.org/packages/ad/6c/d01f9dfbbdc613305e0a831016844987a1fb4861dd221cd4c69b1216b43f/propcache-0.3.1-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:967a8eec513dbe08330f10137eacb427b2ca52118769e82ebcfcab0fba92a649", size = 206135 },
    { url = "https://files.pythonhosted.org/packages/9a/8a/e6e1c77394088f4cfdace4a91a7328e398ebed745d59c2f6764135c5342d/propcache-0.3.1-cp310-cp310-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:5b9145c35cc87313b5fd480144f8078716007656093d23059e8993d3a8fa730f", size = 220517 },
    { url = "https://files.pythonhosted.org/packages/19/3b/6c44fa59d6418f4239d5db8b1ece757351e85d6f3ca126dfe37d427020c8/propcache-0.3.1-cp310-cp310-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:9e64e948ab41411958670f1093c0a57acfdc3bee5cf5b935671bbd5313bcf229", size = 218952 },
    { url = "https://files.pythonhosted.org/packages/7c/e4/4aeb95a1cd085e0558ab0de95abfc5187329616193a1012a6c4c930e9f7a/propcache-0.3.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:319fa8765bfd6a265e5fa661547556da381e53274bc05094fc9ea50da51bfd46", size = 206593 },
    { url = "https://files.pythonhosted.org/packages/da/6a/29fa75de1cbbb302f1e1d684009b969976ca603ee162282ae702287b6621/propcache-0.3.1-cp310-cp310-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:c66d8ccbc902ad548312b96ed8d5d266d0d2c6d006fd0f66323e9d8f2dd49be7", size = 196745 },
    { url = "https://files.pythonhosted.org/packages/19/7e/2237dad1dbffdd2162de470599fa1a1d55df493b16b71e5d25a0ac1c1543/propcache-0.3.1-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:2d219b0dbabe75e15e581fc1ae796109b07c8ba7d25b9ae8d650da582bed01b0", size = 203369 },
    { url = "https://files.pythonhosted.org/packages/a4/bc/a82c5878eb3afb5c88da86e2cf06e1fe78b7875b26198dbb70fe50a010dc/propcache-0.3.1-cp310-cp310-musllinux_1_2_armv7l.whl", hash = "sha256:cd6a55f65241c551eb53f8cf4d2f4af33512c39da5d9777694e9d9c60872f519", size = 198723 },
    { url = "https://files.pythonhosted.org/packages/17/76/9632254479c55516f51644ddbf747a45f813031af5adcb8db91c0b824375/propcache-0.3.1-cp310-cp310-musllinux_1_2_i686.whl", hash = "sha256:9979643ffc69b799d50d3a7b72b5164a2e97e117009d7af6dfdd2ab906cb72cd", size = 200751 },
    { url = "https://files.pythonhosted.org/packages/3e/c3/a90b773cf639bd01d12a9e20c95be0ae978a5a8abe6d2d343900ae76cd71/propcache-0.3.1-cp310-cp310-musllinux_1_2_ppc64le.whl", hash = "sha256:4cf9e93a81979f1424f1a3d155213dc928f1069d697e4353edb8a5eba67c6259", size = 210730 },
    { url = "https://files.pythonhosted.org/packages/ed/ec/ad5a952cdb9d65c351f88db7c46957edd3d65ffeee72a2f18bd6341433e0/propcache-0.3.1-cp310-cp310-musllinux_1_2_s390x.whl", hash = "sha256:2fce1df66915909ff6c824bbb5eb403d2d15f98f1518e583074671a30fe0c21e", size = 213499 },
    { url = "https://files.pythonhosted.org/packages/83/c0/ea5133dda43e298cd2010ec05c2821b391e10980e64ee72c0a76cdbb813a/propcache-0.3.1-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:4d0dfdd9a2ebc77b869a0b04423591ea8823f791293b527dc1bb896c1d6f1136", size = 207132 },
    { url = "https://files.pythonhosted.org/packages/79/dd/71aae9dec59333064cfdd7eb31a63fa09f64181b979802a67a90b2abfcba/propcache-0.3.1-cp310-cp310-win32.whl", hash = "sha256:1f6cc0ad7b4560e5637eb2c994e97b4fa41ba8226069c9277eb5ea7101845b42", size = 40952 },
    { url = "https://files.pythonhosted.org/packages/31/0a/49ff7e5056c17dfba62cbdcbb90a29daffd199c52f8e65e5cb09d5f53a57/propcache-0.3.1-cp310-cp310-win_amd64.whl", hash = "sha256:47ef24aa6511e388e9894ec16f0fbf3313a53ee68402bc428744a367ec55b833", size = 45163 },
    { url = "https://files.pythonhosted.org/packages/90/0f/5a5319ee83bd651f75311fcb0c492c21322a7fc8f788e4eef23f44243427/propcache-0.3.1-cp311-cp311-macosx_10_9_universal2.whl", hash = "sha256:7f30241577d2fef2602113b70ef7231bf4c69a97e04693bde08ddab913ba0ce5", size = 80243 },
    { url = "https://files.pythonhosted.org/packages/ce/84/3db5537e0879942783e2256616ff15d870a11d7ac26541336fe1b673c818/propcache-0.3.1-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:43593c6772aa12abc3af7784bff4a41ffa921608dd38b77cf1dfd7f5c4e71371", size = 46503 },
    { url = "https://files.pythonhosted.org/packages/e2/c8/b649ed972433c3f0d827d7f0cf9ea47162f4ef8f4fe98c5f3641a0bc63ff/propcache-0.3.1-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:a75801768bbe65499495660b777e018cbe90c7980f07f8aa57d6be79ea6f71da", size = 45934 },
    { url = "https://files.pythonhosted.org/packages/59/f9/4c0a5cf6974c2c43b1a6810c40d889769cc8f84cea676cbe1e62766a45f8/propcache-0.3.1-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:f6f1324db48f001c2ca26a25fa25af60711e09b9aaf4b28488602776f4f9a744", size = 233633 },
    { url = "https://files.pythonhosted.org/packages/e7/64/66f2f4d1b4f0007c6e9078bd95b609b633d3957fe6dd23eac33ebde4b584/propcache-0.3.1-cp311-cp311-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:5cdb0f3e1eb6dfc9965d19734d8f9c481b294b5274337a8cb5cb01b462dcb7e0", size = 241124 },
    { url = "https://files.pythonhosted.org/packages/aa/bf/7b8c9fd097d511638fa9b6af3d986adbdf567598a567b46338c925144c1b/propcache-0.3.1-cp311-cp311-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:1eb34d90aac9bfbced9a58b266f8946cb5935869ff01b164573a7634d39fbcb5", size = 240283 },
    { url = "https://files.pythonhosted.org/packages/fa/c9/e85aeeeaae83358e2a1ef32d6ff50a483a5d5248bc38510d030a6f4e2816/propcache-0.3.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:f35c7070eeec2cdaac6fd3fe245226ed2a6292d3ee8c938e5bb645b434c5f256", size = 232498 },
    { url = "https://files.pythonhosted.org/packages/8e/66/acb88e1f30ef5536d785c283af2e62931cb934a56a3ecf39105887aa8905/propcache-0.3.1-cp311-cp311-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:b23c11c2c9e6d4e7300c92e022046ad09b91fd00e36e83c44483df4afa990073", size = 221486 },
    { url = "https://files.pythonhosted.org/packages/f5/f9/233ddb05ffdcaee4448508ee1d70aa7deff21bb41469ccdfcc339f871427/propcache-0.3.1-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:3e19ea4ea0bf46179f8a3652ac1426e6dcbaf577ce4b4f65be581e237340420d", size = 222675 },
    { url = "https://files.pythonhosted.org/packages/98/b8/eb977e28138f9e22a5a789daf608d36e05ed93093ef12a12441030da800a/propcache-0.3.1-cp311-cp311-musllinux_1_2_armv7l.whl", hash = "sha256:bd39c92e4c8f6cbf5f08257d6360123af72af9f4da75a690bef50da77362d25f", size = 215727 },
    { url = "https://files.pythonhosted.org/packages/89/2d/5f52d9c579f67b8ee1edd9ec073c91b23cc5b7ff7951a1e449e04ed8fdf3/propcache-0.3.1-cp311-cp311-musllinux_1_2_i686.whl", hash = "sha256:b0313e8b923b3814d1c4a524c93dfecea5f39fa95601f6a9b1ac96cd66f89ea0", size = 217878 },
    { url = "https://files.pythonhosted.org/packages/7a/fd/5283e5ed8a82b00c7a989b99bb6ea173db1ad750bf0bf8dff08d3f4a4e28/propcache-0.3.1-cp311-cp311-musllinux_1_2_ppc64le.whl", hash = "sha256:e861ad82892408487be144906a368ddbe2dc6297074ade2d892341b35c59844a", size = 230558 },
    { url = "https://files.pythonhosted.org/packages/90/38/ab17d75938ef7ac87332c588857422ae126b1c76253f0f5b1242032923ca/propcache-0.3.1-cp311-cp311-musllinux_1_2_s390x.whl", hash = "sha256:61014615c1274df8da5991a1e5da85a3ccb00c2d4701ac6f3383afd3ca47ab0a", size = 233754 },
    { url = "https://files.pythonhosted.org/packages/06/5d/3b921b9c60659ae464137508d3b4c2b3f52f592ceb1964aa2533b32fcf0b/propcache-0.3.1-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:71ebe3fe42656a2328ab08933d420df5f3ab121772eef78f2dc63624157f0ed9", size = 226088 },
    { url = "https://files.pythonhosted.org/packages/54/6e/30a11f4417d9266b5a464ac5a8c5164ddc9dd153dfa77bf57918165eb4ae/propcache-0.3.1-cp311-cp311-win32.whl", hash = "sha256:58aa11f4ca8b60113d4b8e32d37e7e78bd8af4d1a5b5cb4979ed856a45e62005", size = 40859 },
    { url = "https://files.pythonhosted.org/packages/1d/3a/8a68dd867da9ca2ee9dfd361093e9cb08cb0f37e5ddb2276f1b5177d7731/propcache-0.3.1-cp311-cp311-win_amd64.whl", hash = "sha256:9532ea0b26a401264b1365146c440a6d78269ed41f83f23818d4b79497aeabe7", size = 45153 },
    { url = "https://files.pythonhosted.org/packages/41/aa/ca78d9be314d1e15ff517b992bebbed3bdfef5b8919e85bf4940e57b6137/propcache-0.3.1-cp312-cp312-macosx_10_13_universal2.whl", hash = "sha256:f78eb8422acc93d7b69964012ad7048764bb45a54ba7a39bb9e146c72ea29723", size = 80430 },
    { url = "https://files.pythonhosted.org/packages/1a/d8/f0c17c44d1cda0ad1979af2e593ea290defdde9eaeb89b08abbe02a5e8e1/propcache-0.3.1-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:89498dd49c2f9a026ee057965cdf8192e5ae070ce7d7a7bd4b66a8e257d0c976", size = 46637 },
    { url = "https://files.pythonhosted.org/packages/ae/bd/c1e37265910752e6e5e8a4c1605d0129e5b7933c3dc3cf1b9b48ed83b364/propcache-0.3.1-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:09400e98545c998d57d10035ff623266927cb784d13dd2b31fd33b8a5316b85b", size = 46123 },
    { url = "https://files.pythonhosted.org/packages/d4/b0/911eda0865f90c0c7e9f0415d40a5bf681204da5fd7ca089361a64c16b28/propcache-0.3.1-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:aa8efd8c5adc5a2c9d3b952815ff8f7710cefdcaf5f2c36d26aff51aeca2f12f", size = 243031 },
    { url = "https://files.pythonhosted.org/packages/0a/06/0da53397c76a74271621807265b6eb61fb011451b1ddebf43213df763669/propcache-0.3.1-cp312-cp312-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:c2fe5c910f6007e716a06d269608d307b4f36e7babee5f36533722660e8c4a70", size = 249100 },
    { url = "https://files.pythonhosted.org/packages/f1/eb/13090e05bf6b963fc1653cdc922133ced467cb4b8dab53158db5a37aa21e/propcache-0.3.1-cp312-cp312-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:a0ab8cf8cdd2194f8ff979a43ab43049b1df0b37aa64ab7eca04ac14429baeb7", size = 250170 },
    { url = "https://files.pythonhosted.org/packages/3b/4c/f72c9e1022b3b043ec7dc475a0f405d4c3e10b9b1d378a7330fecf0652da/propcache-0.3.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:563f9d8c03ad645597b8d010ef4e9eab359faeb11a0a2ac9f7b4bc8c28ebef25", size = 245000 },
    { url = "https://files.pythonhosted.org/packages/e8/fd/970ca0e22acc829f1adf5de3724085e778c1ad8a75bec010049502cb3a86/propcache-0.3.1-cp312-cp312-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:fb6e0faf8cb6b4beea5d6ed7b5a578254c6d7df54c36ccd3d8b3eb00d6770277", size = 230262 },
    { url = "https://files.pythonhosted.org/packages/c4/42/817289120c6b9194a44f6c3e6b2c3277c5b70bbad39e7df648f177cc3634/propcache-0.3.1-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:1c5c7ab7f2bb3f573d1cb921993006ba2d39e8621019dffb1c5bc94cdbae81e8", size = 236772 },
    { url = "https://files.pythonhosted.org/packages/7c/9c/3b3942b302badd589ad6b672da3ca7b660a6c2f505cafd058133ddc73918/propcache-0.3.1-cp312-cp312-musllinux_1_2_armv7l.whl", hash = "sha256:050b571b2e96ec942898f8eb46ea4bfbb19bd5502424747e83badc2d4a99a44e", size = 231133 },
    { url = "https://files.pythonhosted.org/packages/98/a1/75f6355f9ad039108ff000dfc2e19962c8dea0430da9a1428e7975cf24b2/propcache-0.3.1-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:e1c4d24b804b3a87e9350f79e2371a705a188d292fd310e663483af6ee6718ee", size = 230741 },
    { url = "https://files.pythonhosted.org/packages/67/0c/3e82563af77d1f8731132166da69fdfd95e71210e31f18edce08a1eb11ea/propcache-0.3.1-cp312-cp312-musllinux_1_2_ppc64le.whl", hash = "sha256:e4fe2a6d5ce975c117a6bb1e8ccda772d1e7029c1cca1acd209f91d30fa72815", size = 244047 },
    { url = "https://files.pythonhosted.org/packages/f7/50/9fb7cca01532a08c4d5186d7bb2da6c4c587825c0ae134b89b47c7d62628/propcache-0.3.1-cp312-cp312-musllinux_1_2_s390x.whl", hash = "sha256:feccd282de1f6322f56f6845bf1207a537227812f0a9bf5571df52bb418d79d5", size = 246467 },
    { url = "https://files.pythonhosted.org/packages/a9/02/ccbcf3e1c604c16cc525309161d57412c23cf2351523aedbb280eb7c9094/propcache-0.3.1-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:ec314cde7314d2dd0510c6787326bbffcbdc317ecee6b7401ce218b3099075a7", size = 241022 },
    { url = "https://files.pythonhosted.org/packages/db/19/e777227545e09ca1e77a6e21274ae9ec45de0f589f0ce3eca2a41f366220/propcache-0.3.1-cp312-cp312-win32.whl", hash = "sha256:7d2d5a0028d920738372630870e7d9644ce437142197f8c827194fca404bf03b", size = 40647 },
    { url = "https://files.pythonhosted.org/packages/24/bb/3b1b01da5dd04c77a204c84e538ff11f624e31431cfde7201d9110b092b1/propcache-0.3.1-cp312-cp312-win_amd64.whl", hash = "sha256:88c423efef9d7a59dae0614eaed718449c09a5ac79a5f224a8b9664d603f04a3", size = 44784 },
    { url = "https://files.pythonhosted.org/packages/58/60/f645cc8b570f99be3cf46714170c2de4b4c9d6b827b912811eff1eb8a412/propcache-0.3.1-cp313-cp313-macosx_10_13_universal2.whl", hash = "sha256:f1528ec4374617a7a753f90f20e2f551121bb558fcb35926f99e3c42367164b8", size = 77865 },
    { url = "https://files.pythonhosted.org/packages/6f/d4/c1adbf3901537582e65cf90fd9c26fde1298fde5a2c593f987112c0d0798/propcache-0.3.1-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:dc1915ec523b3b494933b5424980831b636fe483d7d543f7afb7b3bf00f0c10f", size = 45452 },
    { url = "https://files.pythonhosted.org/packages/d1/b5/fe752b2e63f49f727c6c1c224175d21b7d1727ce1d4873ef1c24c9216830/propcache-0.3.1-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:a110205022d077da24e60b3df8bcee73971be9575dec5573dd17ae5d81751111", size = 44800 },
    { url = "https://files.pythonhosted.org/packages/62/37/fc357e345bc1971e21f76597028b059c3d795c5ca7690d7a8d9a03c9708a/propcache-0.3.1-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:d249609e547c04d190e820d0d4c8ca03ed4582bcf8e4e160a6969ddfb57b62e5", size = 225804 },
    { url = "https://files.pythonhosted.org/packages/0d/f1/16e12c33e3dbe7f8b737809bad05719cff1dccb8df4dafbcff5575002c0e/propcache-0.3.1-cp313-cp313-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:5ced33d827625d0a589e831126ccb4f5c29dfdf6766cac441d23995a65825dcb", size = 230650 },
    { url = "https://files.pythonhosted.org/packages/3e/a2/018b9f2ed876bf5091e60153f727e8f9073d97573f790ff7cdf6bc1d1fb8/propcache-0.3.1-cp313-cp313-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:4114c4ada8f3181af20808bedb250da6bae56660e4b8dfd9cd95d4549c0962f7", size = 234235 },
    { url = "https://files.pythonhosted.org/packages/45/5f/3faee66fc930dfb5da509e34c6ac7128870631c0e3582987fad161fcb4b1/propcache-0.3.1-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:975af16f406ce48f1333ec5e912fe11064605d5c5b3f6746969077cc3adeb120", size = 228249 },
    { url = "https://files.pythonhosted.org/packages/62/1e/a0d5ebda5da7ff34d2f5259a3e171a94be83c41eb1e7cd21a2105a84a02e/propcache-0.3.1-cp313-cp313-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:a34aa3a1abc50740be6ac0ab9d594e274f59960d3ad253cd318af76b996dd654", size = 214964 },
    { url = "https://files.pythonhosted.org/packages/db/a0/d72da3f61ceab126e9be1f3bc7844b4e98c6e61c985097474668e7e52152/propcache-0.3.1-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:9cec3239c85ed15bfaded997773fdad9fb5662b0a7cbc854a43f291eb183179e", size = 222501 },
    { url = "https://files.pythonhosted.org/packages/18/6d/a008e07ad7b905011253adbbd97e5b5375c33f0b961355ca0a30377504ac/propcache-0.3.1-cp313-cp313-musllinux_1_2_armv7l.whl", hash = "sha256:05543250deac8e61084234d5fc54f8ebd254e8f2b39a16b1dce48904f45b744b", size = 217917 },
    { url = "https://files.pythonhosted.org/packages/98/37/02c9343ffe59e590e0e56dc5c97d0da2b8b19fa747ebacf158310f97a79a/propcache-0.3.1-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:5cb5918253912e088edbf023788de539219718d3b10aef334476b62d2b53de53", size = 217089 },
    { url = "https://files.pythonhosted.org/packages/53/1b/d3406629a2c8a5666d4674c50f757a77be119b113eedd47b0375afdf1b42/propcache-0.3.1-cp313-cp313-musllinux_1_2_ppc64le.whl", hash = "sha256:f3bbecd2f34d0e6d3c543fdb3b15d6b60dd69970c2b4c822379e5ec8f6f621d5", size = 228102 },
    { url = "https://files.pythonhosted.org/packages/cd/a7/3664756cf50ce739e5f3abd48febc0be1a713b1f389a502ca819791a6b69/propcache-0.3.1-cp313-cp313-musllinux_1_2_s390x.whl", hash = "sha256:aca63103895c7d960a5b9b044a83f544b233c95e0dcff114389d64d762017af7", size = 230122 },
    { url = "https://files.pythonhosted.org/packages/35/36/0bbabaacdcc26dac4f8139625e930f4311864251276033a52fd52ff2a274/propcache-0.3.1-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:5a0a9898fdb99bf11786265468571e628ba60af80dc3f6eb89a3545540c6b0ef", size = 226818 },
    { url = "https://files.pythonhosted.org/packages/cc/27/4e0ef21084b53bd35d4dae1634b6d0bad35e9c58ed4f032511acca9d4d26/propcache-0.3.1-cp313-cp313-win32.whl", hash = "sha256:3a02a28095b5e63128bcae98eb59025924f121f048a62393db682f049bf4ac24", size = 40112 },
    { url = "https://files.pythonhosted.org/packages/a6/2c/a54614d61895ba6dd7ac8f107e2b2a0347259ab29cbf2ecc7b94fa38c4dc/propcache-0.3.1-cp313-cp313-win_amd64.whl", hash = "sha256:813fbb8b6aea2fc9659815e585e548fe706d6f663fa73dff59a1677d4595a037", size = 44034 },
    { url = "https://files.pythonhosted.org/packages/5a/a8/0a4fd2f664fc6acc66438370905124ce62e84e2e860f2557015ee4a61c7e/propcache-0.3.1-cp313-cp313t-macosx_10_13_universal2.whl", hash = "sha256:a444192f20f5ce8a5e52761a031b90f5ea6288b1eef42ad4c7e64fef33540b8f", size = 82613 },
    { url = "https://files.pythonhosted.org/packages/4d/e5/5ef30eb2cd81576256d7b6caaa0ce33cd1d2c2c92c8903cccb1af1a4ff2f/propcache-0.3.1-cp313-cp313t-macosx_10_13_x86_64.whl", hash = "sha256:0fbe94666e62ebe36cd652f5fc012abfbc2342de99b523f8267a678e4dfdee3c", size = 47763 },
    { url = "https://files.pythonhosted.org/packages/87/9a/87091ceb048efeba4d28e903c0b15bcc84b7c0bf27dc0261e62335d9b7b8/propcache-0.3.1-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:f011f104db880f4e2166bcdcf7f58250f7a465bc6b068dc84c824a3d4a5c94dc", size = 47175 },
    { url = "https://files.pythonhosted.org/packages/3e/2f/854e653c96ad1161f96194c6678a41bbb38c7947d17768e8811a77635a08/propcache-0.3.1-cp313-cp313t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:3e584b6d388aeb0001d6d5c2bd86b26304adde6d9bb9bfa9c4889805021b96de", size = 292265 },
    { url = "https://files.pythonhosted.org/packages/40/8d/090955e13ed06bc3496ba4a9fb26c62e209ac41973cb0d6222de20c6868f/propcache-0.3.1-cp313-cp313t-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:8a17583515a04358b034e241f952f1715243482fc2c2945fd99a1b03a0bd77d6", size = 294412 },
    { url = "https://files.pythonhosted.org/packages/39/e6/d51601342e53cc7582449e6a3c14a0479fab2f0750c1f4d22302e34219c6/propcache-0.3.1-cp313-cp313t-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:5aed8d8308215089c0734a2af4f2e95eeb360660184ad3912686c181e500b2e7", size = 294290 },
    { url = "https://files.pythonhosted.org/packages/3b/4d/be5f1a90abc1881884aa5878989a1acdafd379a91d9c7e5e12cef37ec0d7/propcache-0.3.1-cp313-cp313t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:6d8e309ff9a0503ef70dc9a0ebd3e69cf7b3894c9ae2ae81fc10943c37762458", size = 282926 },
    { url = "https://files.pythonhosted.org/packages/57/2b/8f61b998c7ea93a2b7eca79e53f3e903db1787fca9373af9e2cf8dc22f9d/propcache-0.3.1-cp313-cp313t-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:b655032b202028a582d27aeedc2e813299f82cb232f969f87a4fde491a233f11", size = 267808 },
    { url = "https://files.pythonhosted.org/packages/11/1c/311326c3dfce59c58a6098388ba984b0e5fb0381ef2279ec458ef99bd547/propcache-0.3.1-cp313-cp313t-musllinux_1_2_aarch64.whl", hash = "sha256:9f64d91b751df77931336b5ff7bafbe8845c5770b06630e27acd5dbb71e1931c", size = 290916 },
    { url = "https://files.pythonhosted.org/packages/4b/74/91939924b0385e54dc48eb2e4edd1e4903ffd053cf1916ebc5347ac227f7/propcache-0.3.1-cp313-cp313t-musllinux_1_2_armv7l.whl", hash = "sha256:19a06db789a4bd896ee91ebc50d059e23b3639c25d58eb35be3ca1cbe967c3bf", size = 262661 },
    { url = "https://files.pythonhosted.org/packages/c2/d7/e6079af45136ad325c5337f5dd9ef97ab5dc349e0ff362fe5c5db95e2454/propcache-0.3.1-cp313-cp313t-musllinux_1_2_i686.whl", hash = "sha256:bef100c88d8692864651b5f98e871fb090bd65c8a41a1cb0ff2322db39c96c27", size = 264384 },
    { url = "https://files.pythonhosted.org/packages/b7/d5/ba91702207ac61ae6f1c2da81c5d0d6bf6ce89e08a2b4d44e411c0bbe867/propcache-0.3.1-cp313-cp313t-musllinux_1_2_ppc64le.whl", hash = "sha256:87380fb1f3089d2a0b8b00f006ed12bd41bd858fabfa7330c954c70f50ed8757", size = 291420 },
    { url = "https://files.pythonhosted.org/packages/58/70/2117780ed7edcd7ba6b8134cb7802aada90b894a9810ec56b7bb6018bee7/propcache-0.3.1-cp313-cp313t-musllinux_1_2_s390x.whl", hash = "sha256:e474fc718e73ba5ec5180358aa07f6aded0ff5f2abe700e3115c37d75c947e18", size = 290880 },
    { url = "https://files.pythonhosted.org/packages/4a/1f/ecd9ce27710021ae623631c0146719280a929d895a095f6d85efb6a0be2e/propcache-0.3.1-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:17d1c688a443355234f3c031349da69444be052613483f3e4158eef751abcd8a", size = 287407 },
    { url = "https://files.pythonhosted.org/packages/3e/66/2e90547d6b60180fb29e23dc87bd8c116517d4255240ec6d3f7dc23d1926/propcache-0.3.1-cp313-cp313t-win32.whl", hash = "sha256:359e81a949a7619802eb601d66d37072b79b79c2505e6d3fd8b945538411400d", size = 42573 },
    { url = "https://files.pythonhosted.org/packages/cb/8f/50ad8599399d1861b4d2b6b45271f0ef6af1b09b0a2386a46dbaf19c9535/propcache-0.3.1-cp313-cp313t-win_amd64.whl", hash = "sha256:e7fb9a84c9abbf2b2683fa3e7b0d7da4d8ecf139a1c635732a8bda29c5214b0e", size = 46757 },
    { url = "https://files.pythonhosted.org/packages/aa/e1/4a782cdc7ebc42dfb44224dabf93b481395a0b6cbc9f0149785edbbab19c/propcache-0.3.1-cp39-cp39-macosx_10_9_universal2.whl", hash = "sha256:ed5f6d2edbf349bd8d630e81f474d33d6ae5d07760c44d33cd808e2f5c8f4ae6", size = 81368 },
    { url = "https://files.pythonhosted.org/packages/18/c6/9a39b2646a71321815d8d616e890851af9fb327af7d1b9fdce7d2d8377ca/propcache-0.3.1-cp39-cp39-macosx_10_9_x86_64.whl", hash = "sha256:668ddddc9f3075af019f784456267eb504cb77c2c4bd46cc8402d723b4d200bf", size = 47037 },
    { url = "https://files.pythonhosted.org/packages/f3/e2/88ad1c4c42861dd09b45924e468c42a1beb2c5267cb960b7a9f6af67dd04/propcache-0.3.1-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:0c86e7ceea56376216eba345aa1fc6a8a6b27ac236181f840d1d7e6a1ea9ba5c", size = 46462 },
    { url = "https://files.pythonhosted.org/packages/ae/7e/3e3b36854e96be2e881bc6e87293d59c74dd734dd038dd4981474be44e26/propcache-0.3.1-cp39-cp39-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:83be47aa4e35b87c106fc0c84c0fc069d3f9b9b06d3c494cd404ec6747544894", size = 209214 },
    { url = "https://files.pythonhosted.org/packages/11/1a/ac0f757cc0babdc8217056fca85150066cf43bf11db9651e6b7d8e0646d6/propcache-0.3.1-cp39-cp39-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:27c6ac6aa9fc7bc662f594ef380707494cb42c22786a558d95fcdedb9aa5d035", size = 224702 },
    { url = "https://files.pythonhosted.org/packages/92/0a/0cf77d0e984b7058019ffa5385b3efd6962cbd5340a8f278ae103032863a/propcache-0.3.1-cp39-cp39-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:64a956dff37080b352c1c40b2966b09defb014347043e740d420ca1eb7c9b908", size = 223085 },
    { url = "https://files.pythonhosted.org/packages/05/fc/cb52a0caf803caff9b95b0a99e7c9c87f15b7e34ba0feebfd2572b49013d/propcache-0.3.1-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:82de5da8c8893056603ac2d6a89eb8b4df49abf1a7c19d536984c8dd63f481d5", size = 209613 },
    { url = "https://files.pythonhosted.org/packages/e5/fc/b1d1fdffbe1e0278ab535f8d21fc6b030889417714a545755bdd5ebe9bb0/propcache-0.3.1-cp39-cp39-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:0c3c3a203c375b08fd06a20da3cf7aac293b834b6f4f4db71190e8422750cca5", size = 199931 },
    { url = "https://files.pythonhosted.org/packages/23/a9/2a2f8d93d8f526c35dd8dbbc4a1ac22a106712cd821e15e2a6530aea8931/propcache-0.3.1-cp39-cp39-musllinux_1_2_aarch64.whl", hash = "sha256:b303b194c2e6f171cfddf8b8ba30baefccf03d36a4d9cab7fd0bb68ba476a3d7", size = 208937 },
    { url = "https://files.pythonhosted.org/packages/ef/71/5247a264b95e8d4ba86757cf9ad6a523d764bd4579a2d80007a2d4d2b0ad/propcache-0.3.1-cp39-cp39-musllinux_1_2_armv7l.whl", hash = "sha256:916cd229b0150129d645ec51614d38129ee74c03293a9f3f17537be0029a9641", size = 202577 },
    { url = "https://files.pythonhosted.org/packages/6f/4e/c8ec771731f1b1e7d07bd8875f1d13c1564b5d60f7483624d021eaef5687/propcache-0.3.1-cp39-cp39-musllinux_1_2_i686.whl", hash = "sha256:a461959ead5b38e2581998700b26346b78cd98540b5524796c175722f18b0294", size = 204669 },
    { url = "https://files.pythonhosted.org/packages/c5/b8/bdfcb1170a7b8504226064d7c0b4deb61acbcc6bb2e754ee25fb36c1b72a/propcache-0.3.1-cp39-cp39-musllinux_1_2_ppc64le.whl", hash = "sha256:069e7212890b0bcf9b2be0a03afb0c2d5161d91e1bf51569a64f629acc7defbf", size = 214334 },
    { url = "https://files.pythonhosted.org/packages/72/c6/fdb9e8ba161a4e12c75a7415cb99314cad195d3b8ae9d770783cec54001e/propcache-0.3.1-cp39-cp39-musllinux_1_2_s390x.whl", hash = "sha256:ef2e4e91fb3945769e14ce82ed53007195e616a63aa43b40fb7ebaaf907c8d4c", size = 218052 },
    { url = "https://files.pythonhosted.org/packages/67/3f/0dd87220f61598b61b590a8b3562142ae475a9c0f694ee32bf97e4e41d44/propcache-0.3.1-cp39-cp39-musllinux_1_2_x86_64.whl", hash = "sha256:8638f99dca15b9dff328fb6273e09f03d1c50d9b6512f3b65a4154588a7595fe", size = 210852 },
    { url = "https://files.pythonhosted.org/packages/7b/4e/e332164372af66992c07b470448beb7e36ce7dba6a06c6c2b6131f112e74/propcache-0.3.1-cp39-cp39-win32.whl", hash = "sha256:6f173bbfe976105aaa890b712d1759de339d8a7cef2fc0a1714cc1a1e1c47f64", size = 41481 },
    { url = "https://files.pythonhosted.org/packages/61/73/d64abb7bb5d18880ecfac152247c0f1a5807256ea21e4737ce3019afffeb/propcache-0.3.1-cp39-cp39-win_amd64.whl", hash = "sha256:603f1fe4144420374f1a69b907494c3acbc867a581c2d49d4175b0de7cc64566", size = 45720 },
    { url = "https://files.pythonhosted.org/packages/b8/d3/c3cb8f1d6ae3b37f83e1de806713a9b3642c5895f0215a62e1a4bd6e5e34/propcache-0.3.1-py3-none-any.whl", hash = "sha256:9a8ecf38de50a7f518c21568c80f985e776397b902f1ce0b01f799aba1608b40", size = 12376 },
]

[[package]]
name = "psutil"
version = "7.0.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/2a/80/336820c1ad9286a4ded7e845b2eccfcb27851ab8ac6abece774a6ff4d3de/psutil-7.0.0.tar.gz", hash = "sha256:7be9c3eba38beccb6495ea33afd982a44074b78f28c434a1f51cc07fd315c456", size = 497003 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/ed/e6/2d26234410f8b8abdbf891c9da62bee396583f713fb9f3325a4760875d22/psutil-7.0.0-cp36-abi3-macosx_10_9_x86_64.whl", hash = "sha256:101d71dc322e3cffd7cea0650b09b3d08b8e7c4109dd6809fe452dfd00e58b25", size = 238051 },
    { url = "https://files.pythonhosted.org/packages/04/8b/30f930733afe425e3cbfc0e1468a30a18942350c1a8816acfade80c005c4/psutil-7.0.0-cp36-abi3-macosx_11_0_arm64.whl", hash = "sha256:39db632f6bb862eeccf56660871433e111b6ea58f2caea825571951d4b6aa3da", size = 239535 },
    { url = "https://files.pythonhosted.org/packages/2a/ed/d362e84620dd22876b55389248e522338ed1bf134a5edd3b8231d7207f6d/psutil-7.0.0-cp36-abi3-manylinux_2_12_i686.manylinux2010_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:1fcee592b4c6f146991ca55919ea3d1f8926497a713ed7faaf8225e174581e91", size = 275004 },
    { url = "https://files.pythonhosted.org/packages/bf/b9/b0eb3f3cbcb734d930fdf839431606844a825b23eaf9a6ab371edac8162c/psutil-7.0.0-cp36-abi3-manylinux_2_12_x86_64.manylinux2010_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:4b1388a4f6875d7e2aff5c4ca1cc16c545ed41dd8bb596cefea80111db353a34", size = 277986 },
    { url = "https://files.pythonhosted.org/packages/eb/a2/709e0fe2f093556c17fbafda93ac032257242cabcc7ff3369e2cb76a97aa/psutil-7.0.0-cp36-abi3-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:a5f098451abc2828f7dc6b58d44b532b22f2088f4999a937557b603ce72b1993", size = 279544 },
    { url = "https://files.pythonhosted.org/packages/50/e6/eecf58810b9d12e6427369784efe814a1eec0f492084ce8eb8f4d89d6d61/psutil-7.0.0-cp37-abi3-win32.whl", hash = "sha256:ba3fcef7523064a6c9da440fc4d6bd07da93ac726b5733c29027d7dc95b39d99", size = 241053 },
    { url = "https://files.pythonhosted.org/packages/50/1b/6921afe68c74868b4c9fa424dad3be35b095e16687989ebbb50ce4fceb7c/psutil-7.0.0-cp37-abi3-win_amd64.whl", hash = "sha256:4cf3d4eb1aa9b348dec30105c55cd9b7d4629285735a102beb4441e38db90553", size = 244885 },
]

[[package]]
name = "pyarrow"
version = "19.0.1"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/7f/09/a9046344212690f0632b9c709f9bf18506522feb333c894d0de81d62341a/pyarrow-19.0.1.tar.gz", hash = "sha256:3bf266b485df66a400f282ac0b6d1b500b9d2ae73314a153dbe97d6d5cc8a99e", size = 1129437 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/36/01/b23b514d86b839956238d3f8ef206fd2728eee87ff1b8ce150a5678d9721/pyarrow-19.0.1-cp310-cp310-macosx_12_0_arm64.whl", hash = "sha256:fc28912a2dc924dddc2087679cc8b7263accc71b9ff025a1362b004711661a69", size = 30688914 },
    { url = "https://files.pythonhosted.org/packages/c6/68/218ff7cf4a0652a933e5f2ed11274f724dd43b9813cb18dd72c0a35226a2/pyarrow-19.0.1-cp310-cp310-macosx_12_0_x86_64.whl", hash = "sha256:fca15aabbe9b8355800d923cc2e82c8ef514af321e18b437c3d782aa884eaeec", size = 32102866 },
    { url = "https://files.pythonhosted.org/packages/98/01/c295050d183014f4a2eb796d7d2bbfa04b6cccde7258bb68aacf6f18779b/pyarrow-19.0.1-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:ad76aef7f5f7e4a757fddcdcf010a8290958f09e3470ea458c80d26f4316ae89", size = 41147682 },
    { url = "https://files.pythonhosted.org/packages/40/17/a6c3db0b5f3678f33bbb552d2acbc16def67f89a72955b67b0109af23eb0/pyarrow-19.0.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:d03c9d6f2a3dffbd62671ca070f13fc527bb1867b4ec2b98c7eeed381d4f389a", size = 42179192 },
    { url = "https://files.pythonhosted.org/packages/cf/75/c7c8e599300d8cebb6cb339014800e1c720c9db2a3fcb66aa64ec84bac72/pyarrow-19.0.1-cp310-cp310-manylinux_2_28_aarch64.whl", hash = "sha256:65cf9feebab489b19cdfcfe4aa82f62147218558d8d3f0fc1e9dea0ab8e7905a", size = 40517272 },
    { url = "https://files.pythonhosted.org/packages/ef/c9/68ab123ee1528699c4d5055f645ecd1dd68ff93e4699527249d02f55afeb/pyarrow-19.0.1-cp310-cp310-manylinux_2_28_x86_64.whl", hash = "sha256:41f9706fbe505e0abc10e84bf3a906a1338905cbbcf1177b71486b03e6ea6608", size = 42069036 },
    { url = "https://files.pythonhosted.org/packages/54/e3/d5cfd7654084e6c0d9c3ce949e5d9e0ccad569ae1e2d5a68a3ec03b2be89/pyarrow-19.0.1-cp310-cp310-win_amd64.whl", hash = "sha256:c6cb2335a411b713fdf1e82a752162f72d4a7b5dbc588e32aa18383318b05866", size = 25277951 },
    { url = "https://files.pythonhosted.org/packages/a0/55/f1a8d838ec07fe3ca53edbe76f782df7b9aafd4417080eebf0b42aab0c52/pyarrow-19.0.1-cp311-cp311-macosx_12_0_arm64.whl", hash = "sha256:cc55d71898ea30dc95900297d191377caba257612f384207fe9f8293b5850f90", size = 30713987 },
    { url = "https://files.pythonhosted.org/packages/13/12/428861540bb54c98a140ae858a11f71d041ef9e501e6b7eb965ca7909505/pyarrow-19.0.1-cp311-cp311-macosx_12_0_x86_64.whl", hash = "sha256:7a544ec12de66769612b2d6988c36adc96fb9767ecc8ee0a4d270b10b1c51e00", size = 32135613 },
    { url = "https://files.pythonhosted.org/packages/2f/8a/23d7cc5ae2066c6c736bce1db8ea7bc9ac3ef97ac7e1c1667706c764d2d9/pyarrow-19.0.1-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:0148bb4fc158bfbc3d6dfe5001d93ebeed253793fff4435167f6ce1dc4bddeae", size = 41149147 },
    { url = "https://files.pythonhosted.org/packages/a2/7a/845d151bb81a892dfb368bf11db584cf8b216963ccce40a5cf50a2492a18/pyarrow-19.0.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:f24faab6ed18f216a37870d8c5623f9c044566d75ec586ef884e13a02a9d62c5", size = 42178045 },
    { url = "https://files.pythonhosted.org/packages/a7/31/e7282d79a70816132cf6cae7e378adfccce9ae10352d21c2fecf9d9756dd/pyarrow-19.0.1-cp311-cp311-manylinux_2_28_aarch64.whl", hash = "sha256:4982f8e2b7afd6dae8608d70ba5bd91699077323f812a0448d8b7abdff6cb5d3", size = 40532998 },
    { url = "https://files.pythonhosted.org/packages/b8/82/20f3c290d6e705e2ee9c1fa1d5a0869365ee477e1788073d8b548da8b64c/pyarrow-19.0.1-cp311-cp311-manylinux_2_28_x86_64.whl", hash = "sha256:49a3aecb62c1be1d822f8bf629226d4a96418228a42f5b40835c1f10d42e4db6", size = 42084055 },
    { url = "https://files.pythonhosted.org/packages/ff/77/e62aebd343238863f2c9f080ad2ef6ace25c919c6ab383436b5b81cbeef7/pyarrow-19.0.1-cp311-cp311-win_amd64.whl", hash = "sha256:008a4009efdb4ea3d2e18f05cd31f9d43c388aad29c636112c2966605ba33466", size = 25283133 },
    { url = "https://files.pythonhosted.org/packages/78/b4/94e828704b050e723f67d67c3535cf7076c7432cd4cf046e4bb3b96a9c9d/pyarrow-19.0.1-cp312-cp312-macosx_12_0_arm64.whl", hash = "sha256:80b2ad2b193e7d19e81008a96e313fbd53157945c7be9ac65f44f8937a55427b", size = 30670749 },
    { url = "https://files.pythonhosted.org/packages/7e/3b/4692965e04bb1df55e2c314c4296f1eb12b4f3052d4cf43d29e076aedf66/pyarrow-19.0.1-cp312-cp312-macosx_12_0_x86_64.whl", hash = "sha256:ee8dec072569f43835932a3b10c55973593abc00936c202707a4ad06af7cb294", size = 32128007 },
    { url = "https://files.pythonhosted.org/packages/22/f7/2239af706252c6582a5635c35caa17cb4d401cd74a87821ef702e3888957/pyarrow-19.0.1-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:4d5d1ec7ec5324b98887bdc006f4d2ce534e10e60f7ad995e7875ffa0ff9cb14", size = 41144566 },
    { url = "https://files.pythonhosted.org/packages/fb/e3/c9661b2b2849cfefddd9fd65b64e093594b231b472de08ff658f76c732b2/pyarrow-19.0.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:f3ad4c0eb4e2a9aeb990af6c09e6fa0b195c8c0e7b272ecc8d4d2b6574809d34", size = 42202991 },
    { url = "https://files.pythonhosted.org/packages/fe/4f/a2c0ed309167ef436674782dfee4a124570ba64299c551e38d3fdaf0a17b/pyarrow-19.0.1-cp312-cp312-manylinux_2_28_aarch64.whl", hash = "sha256:d383591f3dcbe545f6cc62daaef9c7cdfe0dff0fb9e1c8121101cabe9098cfa6", size = 40507986 },
    { url = "https://files.pythonhosted.org/packages/27/2e/29bb28a7102a6f71026a9d70d1d61df926887e36ec797f2e6acfd2dd3867/pyarrow-19.0.1-cp312-cp312-manylinux_2_28_x86_64.whl", hash = "sha256:b4c4156a625f1e35d6c0b2132635a237708944eb41df5fbe7d50f20d20c17832", size = 42087026 },
    { url = "https://files.pythonhosted.org/packages/16/33/2a67c0f783251106aeeee516f4806161e7b481f7d744d0d643d2f30230a5/pyarrow-19.0.1-cp312-cp312-win_amd64.whl", hash = "sha256:5bd1618ae5e5476b7654c7b55a6364ae87686d4724538c24185bbb2952679960", size = 25250108 },
    { url = "https://files.pythonhosted.org/packages/2b/8d/275c58d4b00781bd36579501a259eacc5c6dfb369be4ddeb672ceb551d2d/pyarrow-19.0.1-cp313-cp313-macosx_12_0_arm64.whl", hash = "sha256:e45274b20e524ae5c39d7fc1ca2aa923aab494776d2d4b316b49ec7572ca324c", size = 30653552 },
    { url = "https://files.pythonhosted.org/packages/a0/9e/e6aca5cc4ef0c7aec5f8db93feb0bde08dbad8c56b9014216205d271101b/pyarrow-19.0.1-cp313-cp313-macosx_12_0_x86_64.whl", hash = "sha256:d9dedeaf19097a143ed6da37f04f4051aba353c95ef507764d344229b2b740ae", size = 32103413 },
    { url = "https://files.pythonhosted.org/packages/6a/fa/a7033f66e5d4f1308c7eb0dfcd2ccd70f881724eb6fd1776657fdf65458f/pyarrow-19.0.1-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:6ebfb5171bb5f4a52319344ebbbecc731af3f021e49318c74f33d520d31ae0c4", size = 41134869 },
    { url = "https://files.pythonhosted.org/packages/2d/92/34d2569be8e7abdc9d145c98dc410db0071ac579b92ebc30da35f500d630/pyarrow-19.0.1-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:f2a21d39fbdb948857f67eacb5bbaaf36802de044ec36fbef7a1c8f0dd3a4ab2", size = 42192626 },
    { url = "https://files.pythonhosted.org/packages/0a/1f/80c617b1084fc833804dc3309aa9d8daacd46f9ec8d736df733f15aebe2c/pyarrow-19.0.1-cp313-cp313-manylinux_2_28_aarch64.whl", hash = "sha256:99bc1bec6d234359743b01e70d4310d0ab240c3d6b0da7e2a93663b0158616f6", size = 40496708 },
    { url = "https://files.pythonhosted.org/packages/e6/90/83698fcecf939a611c8d9a78e38e7fed7792dcc4317e29e72cf8135526fb/pyarrow-19.0.1-cp313-cp313-manylinux_2_28_x86_64.whl", hash = "sha256:1b93ef2c93e77c442c979b0d596af45e4665d8b96da598db145b0fec014b9136", size = 42075728 },
    { url = "https://files.pythonhosted.org/packages/40/49/2325f5c9e7a1c125c01ba0c509d400b152c972a47958768e4e35e04d13d8/pyarrow-19.0.1-cp313-cp313-win_amd64.whl", hash = "sha256:d9d46e06846a41ba906ab25302cf0fd522f81aa2a85a71021826f34639ad31ef", size = 25242568 },
    { url = "https://files.pythonhosted.org/packages/3f/72/135088d995a759d4d916ec4824cb19e066585b4909ebad4ab196177aa825/pyarrow-19.0.1-cp313-cp313t-macosx_12_0_arm64.whl", hash = "sha256:c0fe3dbbf054a00d1f162fda94ce236a899ca01123a798c561ba307ca38af5f0", size = 30702371 },
    { url = "https://files.pythonhosted.org/packages/2e/01/00beeebd33d6bac701f20816a29d2018eba463616bbc07397fdf99ac4ce3/pyarrow-19.0.1-cp313-cp313t-macosx_12_0_x86_64.whl", hash = "sha256:96606c3ba57944d128e8a8399da4812f56c7f61de8c647e3470b417f795d0ef9", size = 32116046 },
    { url = "https://files.pythonhosted.org/packages/1f/c9/23b1ea718dfe967cbd986d16cf2a31fe59d015874258baae16d7ea0ccabc/pyarrow-19.0.1-cp313-cp313t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:8f04d49a6b64cf24719c080b3c2029a3a5b16417fd5fd7c4041f94233af732f3", size = 41091183 },
    { url = "https://files.pythonhosted.org/packages/3a/d4/b4a3aa781a2c715520aa8ab4fe2e7fa49d33a1d4e71c8fc6ab7b5de7a3f8/pyarrow-19.0.1-cp313-cp313t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:5a9137cf7e1640dce4c190551ee69d478f7121b5c6f323553b319cac936395f6", size = 42171896 },
    { url = "https://files.pythonhosted.org/packages/23/1b/716d4cd5a3cbc387c6e6745d2704c4b46654ba2668260d25c402626c5ddb/pyarrow-19.0.1-cp313-cp313t-manylinux_2_28_aarch64.whl", hash = "sha256:7c1bca1897c28013db5e4c83944a2ab53231f541b9e0c3f4791206d0c0de389a", size = 40464851 },
    { url = "https://files.pythonhosted.org/packages/ed/bd/54907846383dcc7ee28772d7e646f6c34276a17da740002a5cefe90f04f7/pyarrow-19.0.1-cp313-cp313t-manylinux_2_28_x86_64.whl", hash = "sha256:58d9397b2e273ef76264b45531e9d552d8ec8a6688b7390b5be44c02a37aade8", size = 42085744 },
    { url = "https://files.pythonhosted.org/packages/16/26/0ec396ebe98adefaffc0fff8e0dc14c8912e61093226284cf4b76faffd22/pyarrow-19.0.1-cp39-cp39-macosx_12_0_arm64.whl", hash = "sha256:b9766a47a9cb56fefe95cb27f535038b5a195707a08bf61b180e642324963b46", size = 30701112 },
    { url = "https://files.pythonhosted.org/packages/ba/10/c35d96686bf7f13e55bb87f06fe06e7d95533c271ef7f9a5a76e26b16fc2/pyarrow-19.0.1-cp39-cp39-macosx_12_0_x86_64.whl", hash = "sha256:6c5941c1aac89a6c2f2b16cd64fe76bcdb94b2b1e99ca6459de4e6f07638d755", size = 32117180 },
    { url = "https://files.pythonhosted.org/packages/8c/0d/81881a55302b6847ea2ea187517faa039c219d80b55050904e354c2eddde/pyarrow-19.0.1-cp39-cp39-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:fd44d66093a239358d07c42a91eebf5015aa54fccba959db899f932218ac9cc8", size = 41161334 },
    { url = "https://files.pythonhosted.org/packages/af/17/ea60a07ec6f6bb0740f11715e0d22ab8fdfcc94bc729832321f498370d75/pyarrow-19.0.1-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:335d170e050bcc7da867a1ed8ffb8b44c57aaa6e0843b156a501298657b1e972", size = 42190375 },
    { url = "https://files.pythonhosted.org/packages/f2/87/4ef05a088b18082cde4950bdfca752dd31effb3ec201b8026e4816d0f3fa/pyarrow-19.0.1-cp39-cp39-manylinux_2_28_aarch64.whl", hash = "sha256:1c7556165bd38cf0cd992df2636f8bcdd2d4b26916c6b7e646101aff3c16f76f", size = 40530649 },
    { url = "https://files.pythonhosted.org/packages/59/1e/9fb9a66a64eae4ff332a8f149d803d8c6c556714803d20d54ed2e9524a3b/pyarrow-19.0.1-cp39-cp39-manylinux_2_28_x86_64.whl", hash = "sha256:699799f9c80bebcf1da0983ba86d7f289c5a2a5c04b945e2f2bcf7e874a91911", size = 42081576 },
    { url = "https://files.pythonhosted.org/packages/1b/ee/c110d8da8bdde8e832ccf1ff90be747cb684874e2dc8acf26840058b0c32/pyarrow-19.0.1-cp39-cp39-win_amd64.whl", hash = "sha256:8464c9fbe6d94a7fe1599e7e8965f350fd233532868232ab2596a71586c5a429", size = 25465593 },
]

[[package]]
name = "pydantic"
version = "2.11.2"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "annotated-types" },
    { name = "pydantic-core" },
    { name = "typing-extensions" },
    { name = "typing-inspection" },
]
sdist = { url = "https://files.pythonhosted.org/packages/b0/41/832125a41fe098b58d1fdd04ae819b4dc6b34d6b09ed78304fd93d4bc051/pydantic-2.11.2.tar.gz", hash = "sha256:2138628e050bd7a1e70b91d4bf4a91167f4ad76fdb83209b107c8d84b854917e", size = 784742 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/bf/c2/0f3baea344d0b15e35cb3e04ad5b953fa05106b76efbf4c782a3f47f22f5/pydantic-2.11.2-py3-none-any.whl", hash = "sha256:7f17d25846bcdf89b670a86cdfe7b29a9f1c9ca23dee154221c9aa81845cfca7", size = 443295 },
]

[[package]]
name = "pydantic-core"
version = "2.33.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "typing-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/17/19/ed6a078a5287aea7922de6841ef4c06157931622c89c2a47940837b5eecd/pydantic_core-2.33.1.tar.gz", hash = "sha256:bcc9c6fdb0ced789245b02b7d6603e17d1563064ddcfc36f046b61c0c05dd9df", size = 434395 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/38/ea/5f572806ab4d4223d11551af814d243b0e3e02cc6913def4d1fe4a5ca41c/pydantic_core-2.33.1-cp310-cp310-macosx_10_12_x86_64.whl", hash = "sha256:3077cfdb6125cc8dab61b155fdd714663e401f0e6883f9632118ec12cf42df26", size = 2044021 },
    { url = "https://files.pythonhosted.org/packages/8c/d1/f86cc96d2aa80e3881140d16d12ef2b491223f90b28b9a911346c04ac359/pydantic_core-2.33.1-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:8ffab8b2908d152e74862d276cf5017c81a2f3719f14e8e3e8d6b83fda863927", size = 1861742 },
    { url = "https://files.pythonhosted.org/packages/37/08/fbd2cd1e9fc735a0df0142fac41c114ad9602d1c004aea340169ae90973b/pydantic_core-2.33.1-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:5183e4f6a2d468787243ebcd70cf4098c247e60d73fb7d68d5bc1e1beaa0c4db", size = 1910414 },
    { url = "https://files.pythonhosted.org/packages/7f/73/3ac217751decbf8d6cb9443cec9b9eb0130eeada6ae56403e11b486e277e/pydantic_core-2.33.1-cp310-cp310-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:398a38d323f37714023be1e0285765f0a27243a8b1506b7b7de87b647b517e48", size = 1996848 },
    { url = "https://files.pythonhosted.org/packages/9a/f5/5c26b265cdcff2661e2520d2d1e9db72d117ea00eb41e00a76efe68cb009/pydantic_core-2.33.1-cp310-cp310-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:87d3776f0001b43acebfa86f8c64019c043b55cc5a6a2e313d728b5c95b46969", size = 2141055 },
    { url = "https://files.pythonhosted.org/packages/5d/14/a9c3cee817ef2f8347c5ce0713e91867a0dceceefcb2973942855c917379/pydantic_core-2.33.1-cp310-cp310-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:c566dd9c5f63d22226409553531f89de0cac55397f2ab8d97d6f06cfce6d947e", size = 2753806 },
    { url = "https://files.pythonhosted.org/packages/f2/68/866ce83a51dd37e7c604ce0050ff6ad26de65a7799df89f4db87dd93d1d6/pydantic_core-2.33.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:a0d5f3acc81452c56895e90643a625302bd6be351e7010664151cc55b7b97f89", size = 2007777 },
    { url = "https://files.pythonhosted.org/packages/b6/a8/36771f4404bb3e49bd6d4344da4dede0bf89cc1e01f3b723c47248a3761c/pydantic_core-2.33.1-cp310-cp310-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:d3a07fadec2a13274a8d861d3d37c61e97a816beae717efccaa4b36dfcaadcde", size = 2122803 },
    { url = "https://files.pythonhosted.org/packages/18/9c/730a09b2694aa89360d20756369822d98dc2f31b717c21df33b64ffd1f50/pydantic_core-2.33.1-cp310-cp310-musllinux_1_1_aarch64.whl", hash = "sha256:f99aeda58dce827f76963ee87a0ebe75e648c72ff9ba1174a253f6744f518f65", size = 2086755 },
    { url = "https://files.pythonhosted.org/packages/54/8e/2dccd89602b5ec31d1c58138d02340ecb2ebb8c2cac3cc66b65ce3edb6ce/pydantic_core-2.33.1-cp310-cp310-musllinux_1_1_armv7l.whl", hash = "sha256:902dbc832141aa0ec374f4310f1e4e7febeebc3256f00dc359a9ac3f264a45dc", size = 2257358 },
    { url = "https://files.pythonhosted.org/packages/d1/9c/126e4ac1bfad8a95a9837acdd0963695d69264179ba4ede8b8c40d741702/pydantic_core-2.33.1-cp310-cp310-musllinux_1_1_x86_64.whl", hash = "sha256:fe44d56aa0b00d66640aa84a3cbe80b7a3ccdc6f0b1ca71090696a6d4777c091", size = 2257916 },
    { url = "https://files.pythonhosted.org/packages/7d/ba/91eea2047e681a6853c81c20aeca9dcdaa5402ccb7404a2097c2adf9d038/pydantic_core-2.33.1-cp310-cp310-win32.whl", hash = "sha256:ed3eb16d51257c763539bde21e011092f127a2202692afaeaccb50db55a31383", size = 1923823 },
    { url = "https://files.pythonhosted.org/packages/94/c0/fcdf739bf60d836a38811476f6ecd50374880b01e3014318b6e809ddfd52/pydantic_core-2.33.1-cp310-cp310-win_amd64.whl", hash = "sha256:694ad99a7f6718c1a498dc170ca430687a39894a60327f548e02a9c7ee4b6504", size = 1952494 },
    { url = "https://files.pythonhosted.org/packages/d6/7f/c6298830cb780c46b4f46bb24298d01019ffa4d21769f39b908cd14bbd50/pydantic_core-2.33.1-cp311-cp311-macosx_10_12_x86_64.whl", hash = "sha256:6e966fc3caaf9f1d96b349b0341c70c8d6573bf1bac7261f7b0ba88f96c56c24", size = 2044224 },
    { url = "https://files.pythonhosted.org/packages/a8/65/6ab3a536776cad5343f625245bd38165d6663256ad43f3a200e5936afd6c/pydantic_core-2.33.1-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:bfd0adeee563d59c598ceabddf2c92eec77abcb3f4a391b19aa7366170bd9e30", size = 1858845 },
    { url = "https://files.pythonhosted.org/packages/e9/15/9a22fd26ba5ee8c669d4b8c9c244238e940cd5d818649603ca81d1c69861/pydantic_core-2.33.1-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:91815221101ad3c6b507804178a7bb5cb7b2ead9ecd600041669c8d805ebd595", size = 1910029 },
    { url = "https://files.pythonhosted.org/packages/d5/33/8cb1a62818974045086f55f604044bf35b9342900318f9a2a029a1bec460/pydantic_core-2.33.1-cp311-cp311-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:9fea9c1869bb4742d174a57b4700c6dadea951df8b06de40c2fedb4f02931c2e", size = 1997784 },
    { url = "https://files.pythonhosted.org/packages/c0/ca/49958e4df7715c71773e1ea5be1c74544923d10319173264e6db122543f9/pydantic_core-2.33.1-cp311-cp311-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:1d20eb4861329bb2484c021b9d9a977566ab16d84000a57e28061151c62b349a", size = 2141075 },
    { url = "https://files.pythonhosted.org/packages/7b/a6/0b3a167a9773c79ba834b959b4e18c3ae9216b8319bd8422792abc8a41b1/pydantic_core-2.33.1-cp311-cp311-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:0fb935c5591573ae3201640579f30128ccc10739b45663f93c06796854405505", size = 2745849 },
    { url = "https://files.pythonhosted.org/packages/0b/60/516484135173aa9e5861d7a0663dce82e4746d2e7f803627d8c25dfa5578/pydantic_core-2.33.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:c964fd24e6166420d18fb53996d8c9fd6eac9bf5ae3ec3d03015be4414ce497f", size = 2005794 },
    { url = "https://files.pythonhosted.org/packages/86/70/05b1eb77459ad47de00cf78ee003016da0cedf8b9170260488d7c21e9181/pydantic_core-2.33.1-cp311-cp311-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:681d65e9011f7392db5aa002b7423cc442d6a673c635668c227c6c8d0e5a4f77", size = 2123237 },
    { url = "https://files.pythonhosted.org/packages/c7/57/12667a1409c04ae7dc95d3b43158948eb0368e9c790be8b095cb60611459/pydantic_core-2.33.1-cp311-cp311-musllinux_1_1_aarch64.whl", hash = "sha256:e100c52f7355a48413e2999bfb4e139d2977a904495441b374f3d4fb4a170961", size = 2086351 },
    { url = "https://files.pythonhosted.org/packages/57/61/cc6d1d1c1664b58fdd6ecc64c84366c34ec9b606aeb66cafab6f4088974c/pydantic_core-2.33.1-cp311-cp311-musllinux_1_1_armv7l.whl", hash = "sha256:048831bd363490be79acdd3232f74a0e9951b11b2b4cc058aeb72b22fdc3abe1", size = 2258914 },
    { url = "https://files.pythonhosted.org/packages/d1/0a/edb137176a1f5419b2ddee8bde6a0a548cfa3c74f657f63e56232df8de88/pydantic_core-2.33.1-cp311-cp311-musllinux_1_1_x86_64.whl", hash = "sha256:bdc84017d28459c00db6f918a7272a5190bec3090058334e43a76afb279eac7c", size = 2257385 },
    { url = "https://files.pythonhosted.org/packages/26/3c/48ca982d50e4b0e1d9954919c887bdc1c2b462801bf408613ccc641b3daa/pydantic_core-2.33.1-cp311-cp311-win32.whl", hash = "sha256:32cd11c5914d1179df70406427097c7dcde19fddf1418c787540f4b730289896", size = 1923765 },
    { url = "https://files.pythonhosted.org/packages/33/cd/7ab70b99e5e21559f5de38a0928ea84e6f23fdef2b0d16a6feaf942b003c/pydantic_core-2.33.1-cp311-cp311-win_amd64.whl", hash = "sha256:2ea62419ba8c397e7da28a9170a16219d310d2cf4970dbc65c32faf20d828c83", size = 1950688 },
    { url = "https://files.pythonhosted.org/packages/4b/ae/db1fc237b82e2cacd379f63e3335748ab88b5adde98bf7544a1b1bd10a84/pydantic_core-2.33.1-cp311-cp311-win_arm64.whl", hash = "sha256:fc903512177361e868bc1f5b80ac8c8a6e05fcdd574a5fb5ffeac5a9982b9e89", size = 1908185 },
    { url = "https://files.pythonhosted.org/packages/c8/ce/3cb22b07c29938f97ff5f5bb27521f95e2ebec399b882392deb68d6c440e/pydantic_core-2.33.1-cp312-cp312-macosx_10_12_x86_64.whl", hash = "sha256:1293d7febb995e9d3ec3ea09caf1a26214eec45b0f29f6074abb004723fc1de8", size = 2026640 },
    { url = "https://files.pythonhosted.org/packages/19/78/f381d643b12378fee782a72126ec5d793081ef03791c28a0fd542a5bee64/pydantic_core-2.33.1-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:99b56acd433386c8f20be5c4000786d1e7ca0523c8eefc995d14d79c7a081498", size = 1852649 },
    { url = "https://files.pythonhosted.org/packages/9d/2b/98a37b80b15aac9eb2c6cfc6dbd35e5058a352891c5cce3a8472d77665a6/pydantic_core-2.33.1-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:35a5ec3fa8c2fe6c53e1b2ccc2454398f95d5393ab398478f53e1afbbeb4d939", size = 1892472 },
    { url = "https://files.pythonhosted.org/packages/4e/d4/3c59514e0f55a161004792b9ff3039da52448f43f5834f905abef9db6e4a/pydantic_core-2.33.1-cp312-cp312-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:b172f7b9d2f3abc0efd12e3386f7e48b576ef309544ac3a63e5e9cdd2e24585d", size = 1977509 },
    { url = "https://files.pythonhosted.org/packages/a9/b6/c2c7946ef70576f79a25db59a576bce088bdc5952d1b93c9789b091df716/pydantic_core-2.33.1-cp312-cp312-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:9097b9f17f91eea659b9ec58148c0747ec354a42f7389b9d50701610d86f812e", size = 2128702 },
    { url = "https://files.pythonhosted.org/packages/88/fe/65a880f81e3f2a974312b61f82a03d85528f89a010ce21ad92f109d94deb/pydantic_core-2.33.1-cp312-cp312-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:cc77ec5b7e2118b152b0d886c7514a4653bcb58c6b1d760134a9fab915f777b3", size = 2679428 },
    { url = "https://files.pythonhosted.org/packages/6f/ff/4459e4146afd0462fb483bb98aa2436d69c484737feaceba1341615fb0ac/pydantic_core-2.33.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:d5e3d15245b08fa4a84cefc6c9222e6f37c98111c8679fbd94aa145f9a0ae23d", size = 2008753 },
    { url = "https://files.pythonhosted.org/packages/7c/76/1c42e384e8d78452ededac8b583fe2550c84abfef83a0552e0e7478ccbc3/pydantic_core-2.33.1-cp312-cp312-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:ef99779001d7ac2e2461d8ab55d3373fe7315caefdbecd8ced75304ae5a6fc6b", size = 2114849 },
    { url = "https://files.pythonhosted.org/packages/00/72/7d0cf05095c15f7ffe0eb78914b166d591c0eed72f294da68378da205101/pydantic_core-2.33.1-cp312-cp312-musllinux_1_1_aarch64.whl", hash = "sha256:fc6bf8869e193855e8d91d91f6bf59699a5cdfaa47a404e278e776dd7f168b39", size = 2069541 },
    { url = "https://files.pythonhosted.org/packages/b3/69/94a514066bb7d8be499aa764926937409d2389c09be0b5107a970286ef81/pydantic_core-2.33.1-cp312-cp312-musllinux_1_1_armv7l.whl", hash = "sha256:b1caa0bc2741b043db7823843e1bde8aaa58a55a58fda06083b0569f8b45693a", size = 2239225 },
    { url = "https://files.pythonhosted.org/packages/84/b0/e390071eadb44b41f4f54c3cef64d8bf5f9612c92686c9299eaa09e267e2/pydantic_core-2.33.1-cp312-cp312-musllinux_1_1_x86_64.whl", hash = "sha256:ec259f62538e8bf364903a7d0d0239447059f9434b284f5536e8402b7dd198db", size = 2248373 },
    { url = "https://files.pythonhosted.org/packages/d6/b2/288b3579ffc07e92af66e2f1a11be3b056fe1214aab314748461f21a31c3/pydantic_core-2.33.1-cp312-cp312-win32.whl", hash = "sha256:e14f369c98a7c15772b9da98987f58e2b509a93235582838bd0d1d8c08b68fda", size = 1907034 },
    { url = "https://files.pythonhosted.org/packages/02/28/58442ad1c22b5b6742b992ba9518420235adced665513868f99a1c2638a5/pydantic_core-2.33.1-cp312-cp312-win_amd64.whl", hash = "sha256:1c607801d85e2e123357b3893f82c97a42856192997b95b4d8325deb1cd0c5f4", size = 1956848 },
    { url = "https://files.pythonhosted.org/packages/a1/eb/f54809b51c7e2a1d9f439f158b8dd94359321abcc98767e16fc48ae5a77e/pydantic_core-2.33.1-cp312-cp312-win_arm64.whl", hash = "sha256:8d13f0276806ee722e70a1c93da19748594f19ac4299c7e41237fc791d1861ea", size = 1903986 },
    { url = "https://files.pythonhosted.org/packages/7a/24/eed3466a4308d79155f1cdd5c7432c80ddcc4530ba8623b79d5ced021641/pydantic_core-2.33.1-cp313-cp313-macosx_10_12_x86_64.whl", hash = "sha256:70af6a21237b53d1fe7b9325b20e65cbf2f0a848cf77bed492b029139701e66a", size = 2033551 },
    { url = "https://files.pythonhosted.org/packages/ab/14/df54b1a0bc9b6ded9b758b73139d2c11b4e8eb43e8ab9c5847c0a2913ada/pydantic_core-2.33.1-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:282b3fe1bbbe5ae35224a0dbd05aed9ccabccd241e8e6b60370484234b456266", size = 1852785 },
    { url = "https://files.pythonhosted.org/packages/fa/96/e275f15ff3d34bb04b0125d9bc8848bf69f25d784d92a63676112451bfb9/pydantic_core-2.33.1-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:4b315e596282bbb5822d0c7ee9d255595bd7506d1cb20c2911a4da0b970187d3", size = 1897758 },
    { url = "https://files.pythonhosted.org/packages/b7/d8/96bc536e975b69e3a924b507d2a19aedbf50b24e08c80fb00e35f9baaed8/pydantic_core-2.33.1-cp313-cp313-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:1dfae24cf9921875ca0ca6a8ecb4bb2f13c855794ed0d468d6abbec6e6dcd44a", size = 1986109 },
    { url = "https://files.pythonhosted.org/packages/90/72/ab58e43ce7e900b88cb571ed057b2fcd0e95b708a2e0bed475b10130393e/pydantic_core-2.33.1-cp313-cp313-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:6dd8ecfde08d8bfadaea669e83c63939af76f4cf5538a72597016edfa3fad516", size = 2129159 },
    { url = "https://files.pythonhosted.org/packages/dc/3f/52d85781406886c6870ac995ec0ba7ccc028b530b0798c9080531b409fdb/pydantic_core-2.33.1-cp313-cp313-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:2f593494876eae852dc98c43c6f260f45abdbfeec9e4324e31a481d948214764", size = 2680222 },
    { url = "https://files.pythonhosted.org/packages/f4/56/6e2ef42f363a0eec0fd92f74a91e0ac48cd2e49b695aac1509ad81eee86a/pydantic_core-2.33.1-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:948b73114f47fd7016088e5186d13faf5e1b2fe83f5e320e371f035557fd264d", size = 2006980 },
    { url = "https://files.pythonhosted.org/packages/4c/c0/604536c4379cc78359f9ee0aa319f4aedf6b652ec2854953f5a14fc38c5a/pydantic_core-2.33.1-cp313-cp313-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:e11f3864eb516af21b01e25fac915a82e9ddad3bb0fb9e95a246067398b435a4", size = 2120840 },
    { url = "https://files.pythonhosted.org/packages/1f/46/9eb764814f508f0edfb291a0f75d10854d78113fa13900ce13729aaec3ae/pydantic_core-2.33.1-cp313-cp313-musllinux_1_1_aarch64.whl", hash = "sha256:549150be302428b56fdad0c23c2741dcdb5572413776826c965619a25d9c6bde", size = 2072518 },
    { url = "https://files.pythonhosted.org/packages/42/e3/fb6b2a732b82d1666fa6bf53e3627867ea3131c5f39f98ce92141e3e3dc1/pydantic_core-2.33.1-cp313-cp313-musllinux_1_1_armv7l.whl", hash = "sha256:495bc156026efafd9ef2d82372bd38afce78ddd82bf28ef5276c469e57c0c83e", size = 2248025 },
    { url = "https://files.pythonhosted.org/packages/5c/9d/fbe8fe9d1aa4dac88723f10a921bc7418bd3378a567cb5e21193a3c48b43/pydantic_core-2.33.1-cp313-cp313-musllinux_1_1_x86_64.whl", hash = "sha256:ec79de2a8680b1a67a07490bddf9636d5c2fab609ba8c57597e855fa5fa4dacd", size = 2254991 },
    { url = "https://files.pythonhosted.org/packages/aa/99/07e2237b8a66438d9b26482332cda99a9acccb58d284af7bc7c946a42fd3/pydantic_core-2.33.1-cp313-cp313-win32.whl", hash = "sha256:ee12a7be1742f81b8a65b36c6921022301d466b82d80315d215c4c691724986f", size = 1915262 },
    { url = "https://files.pythonhosted.org/packages/8a/f4/e457a7849beeed1e5defbcf5051c6f7b3c91a0624dd31543a64fc9adcf52/pydantic_core-2.33.1-cp313-cp313-win_amd64.whl", hash = "sha256:ede9b407e39949d2afc46385ce6bd6e11588660c26f80576c11c958e6647bc40", size = 1956626 },
    { url = "https://files.pythonhosted.org/packages/20/d0/e8d567a7cff7b04e017ae164d98011f1e1894269fe8e90ea187a3cbfb562/pydantic_core-2.33.1-cp313-cp313-win_arm64.whl", hash = "sha256:aa687a23d4b7871a00e03ca96a09cad0f28f443690d300500603bd0adba4b523", size = 1909590 },
    { url = "https://files.pythonhosted.org/packages/ef/fd/24ea4302d7a527d672c5be06e17df16aabfb4e9fdc6e0b345c21580f3d2a/pydantic_core-2.33.1-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:401d7b76e1000d0dd5538e6381d28febdcacb097c8d340dde7d7fc6e13e9f95d", size = 1812963 },
    { url = "https://files.pythonhosted.org/packages/5f/95/4fbc2ecdeb5c1c53f1175a32d870250194eb2fdf6291b795ab08c8646d5d/pydantic_core-2.33.1-cp313-cp313t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:7aeb055a42d734c0255c9e489ac67e75397d59c6fbe60d155851e9782f276a9c", size = 1986896 },
    { url = "https://files.pythonhosted.org/packages/71/ae/fe31e7f4a62431222d8f65a3bd02e3fa7e6026d154a00818e6d30520ea77/pydantic_core-2.33.1-cp313-cp313t-win_amd64.whl", hash = "sha256:338ea9b73e6e109f15ab439e62cb3b78aa752c7fd9536794112e14bee02c8d18", size = 1931810 },
    { url = "https://files.pythonhosted.org/packages/49/78/b86bad645cc3e8dfa6858c70ec38939bf350e54004837c48de09474b2b9e/pydantic_core-2.33.1-cp39-cp39-macosx_10_12_x86_64.whl", hash = "sha256:5ab77f45d33d264de66e1884fca158bc920cb5e27fd0764a72f72f5756ae8bdb", size = 2044282 },
    { url = "https://files.pythonhosted.org/packages/3b/00/a02531331773b2bf08743d84c6b776bd6a449d23b3ae6b0e3229d568bac4/pydantic_core-2.33.1-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:e7aaba1b4b03aaea7bb59e1b5856d734be011d3e6d98f5bcaa98cb30f375f2ad", size = 1877598 },
    { url = "https://files.pythonhosted.org/packages/a1/fa/32cc152b84a1f420f8a7d80161373e8d87d4ffa077e67d6c8aab3ce1a6ab/pydantic_core-2.33.1-cp39-cp39-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:7fb66263e9ba8fea2aa85e1e5578980d127fb37d7f2e292773e7bc3a38fb0c7b", size = 1911021 },
    { url = "https://files.pythonhosted.org/packages/5e/87/ea553e0d98bce6c4876f8c50f65cb45597eff6e0aaa8b15813e9972bb19d/pydantic_core-2.33.1-cp39-cp39-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:3f2648b9262607a7fb41d782cc263b48032ff7a03a835581abbf7a3bec62bcf5", size = 1997276 },
    { url = "https://files.pythonhosted.org/packages/f7/9b/60cb9f4b52158b3adac0066492bbadd0b8473f4f8da5bcc73972655b76ef/pydantic_core-2.33.1-cp39-cp39-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:723c5630c4259400818b4ad096735a829074601805d07f8cafc366d95786d331", size = 2141348 },
    { url = "https://files.pythonhosted.org/packages/9b/38/374d254e270d4de0add68a8239f4ed0f444fdd7b766ea69244fb9491dccb/pydantic_core-2.33.1-cp39-cp39-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:d100e3ae783d2167782391e0c1c7a20a31f55f8015f3293647544df3f9c67824", size = 2753708 },
    { url = "https://files.pythonhosted.org/packages/05/a8/fd79111eb5ab9bc4ef98d8fb0b3a2ffdc80107b2c59859a741ab379c96f8/pydantic_core-2.33.1-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:177d50460bc976a0369920b6c744d927b0ecb8606fb56858ff542560251b19e5", size = 2008699 },
    { url = "https://files.pythonhosted.org/packages/35/31/2e06619868eb4c18642c5601db420599c1cf9cf50fe868c9ac09cd298e24/pydantic_core-2.33.1-cp39-cp39-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:a3edde68d1a1f9af1273b2fe798997b33f90308fb6d44d8550c89fc6a3647cf6", size = 2123426 },
    { url = "https://files.pythonhosted.org/packages/4a/d0/3531e8783a311802e3db7ee5a1a5ed79e5706e930b1b4e3109ce15eeb681/pydantic_core-2.33.1-cp39-cp39-musllinux_1_1_aarch64.whl", hash = "sha256:a62c3c3ef6a7e2c45f7853b10b5bc4ddefd6ee3cd31024754a1a5842da7d598d", size = 2087330 },
    { url = "https://files.pythonhosted.org/packages/ac/32/5ff252ed73bacd7677a706ab17723e261a76793f98b305aa20cfc10bbd56/pydantic_core-2.33.1-cp39-cp39-musllinux_1_1_armv7l.whl", hash = "sha256:c91dbb0ab683fa0cd64a6e81907c8ff41d6497c346890e26b23de7ee55353f96", size = 2258171 },
    { url = "https://files.pythonhosted.org/packages/c9/f9/e96e00f92b8f5b3e2cddc80c5ee6cf038f8a0f238c44b67b01759943a7b4/pydantic_core-2.33.1-cp39-cp39-musllinux_1_1_x86_64.whl", hash = "sha256:9f466e8bf0a62dc43e068c12166281c2eca72121dd2adc1040f3aa1e21ef8599", size = 2258745 },
    { url = "https://files.pythonhosted.org/packages/54/1e/51c86688e809d94797fdf0efc41514f001caec982a05f62d90c180a9639d/pydantic_core-2.33.1-cp39-cp39-win32.whl", hash = "sha256:ab0277cedb698749caada82e5d099dc9fed3f906a30d4c382d1a21725777a1e5", size = 1923626 },
    { url = "https://files.pythonhosted.org/packages/57/18/c2da959fd8d019b70cadafdda2bf845378ada47973e0bad6cc84f56dbe6e/pydantic_core-2.33.1-cp39-cp39-win_amd64.whl", hash = "sha256:5773da0ee2d17136b1f1c6fbde543398d452a6ad2a7b54ea1033e2daa739b8d2", size = 1953703 },
    { url = "https://files.pythonhosted.org/packages/9c/c7/8b311d5adb0fe00a93ee9b4e92a02b0ec08510e9838885ef781ccbb20604/pydantic_core-2.33.1-pp310-pypy310_pp73-macosx_10_12_x86_64.whl", hash = "sha256:5c834f54f8f4640fd7e4b193f80eb25a0602bba9e19b3cd2fc7ffe8199f5ae02", size = 2041659 },
    { url = "https://files.pythonhosted.org/packages/8a/d6/4f58d32066a9e26530daaf9adc6664b01875ae0691570094968aaa7b8fcc/pydantic_core-2.33.1-pp310-pypy310_pp73-macosx_11_0_arm64.whl", hash = "sha256:049e0de24cf23766f12cc5cc71d8abc07d4a9deb9061b334b62093dedc7cb068", size = 1873294 },
    { url = "https://files.pythonhosted.org/packages/f7/3f/53cc9c45d9229da427909c751f8ed2bf422414f7664ea4dde2d004f596ba/pydantic_core-2.33.1-pp310-pypy310_pp73-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:1a28239037b3d6f16916a4c831a5a0eadf856bdd6d2e92c10a0da3a59eadcf3e", size = 1903771 },
    { url = "https://files.pythonhosted.org/packages/f0/49/bf0783279ce674eb9903fb9ae43f6c614cb2f1c4951370258823f795368b/pydantic_core-2.33.1-pp310-pypy310_pp73-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:9d3da303ab5f378a268fa7d45f37d7d85c3ec19769f28d2cc0c61826a8de21fe", size = 2083558 },
    { url = "https://files.pythonhosted.org/packages/9c/5b/0d998367687f986c7d8484a2c476d30f07bf5b8b1477649a6092bd4c540e/pydantic_core-2.33.1-pp310-pypy310_pp73-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:25626fb37b3c543818c14821afe0fd3830bc327a43953bc88db924b68c5723f1", size = 2118038 },
    { url = "https://files.pythonhosted.org/packages/b3/33/039287d410230ee125daee57373ac01940d3030d18dba1c29cd3089dc3ca/pydantic_core-2.33.1-pp310-pypy310_pp73-musllinux_1_1_aarch64.whl", hash = "sha256:3ab2d36e20fbfcce8f02d73c33a8a7362980cff717926bbae030b93ae46b56c7", size = 2079315 },
    { url = "https://files.pythonhosted.org/packages/1f/85/6d8b2646d99c062d7da2d0ab2faeb0d6ca9cca4c02da6076376042a20da3/pydantic_core-2.33.1-pp310-pypy310_pp73-musllinux_1_1_armv7l.whl", hash = "sha256:2f9284e11c751b003fd4215ad92d325d92c9cb19ee6729ebd87e3250072cdcde", size = 2249063 },
    { url = "https://files.pythonhosted.org/packages/17/d7/c37d208d5738f7b9ad8f22ae8a727d88ebf9c16c04ed2475122cc3f7224a/pydantic_core-2.33.1-pp310-pypy310_pp73-musllinux_1_1_x86_64.whl", hash = "sha256:048c01eee07d37cbd066fc512b9d8b5ea88ceeb4e629ab94b3e56965ad655add", size = 2254631 },
    { url = "https://files.pythonhosted.org/packages/13/e0/bafa46476d328e4553b85ab9b2f7409e7aaef0ce4c937c894821c542d347/pydantic_core-2.33.1-pp310-pypy310_pp73-win_amd64.whl", hash = "sha256:5ccd429694cf26af7997595d627dd2637e7932214486f55b8a357edaac9dae8c", size = 2080877 },
    { url = "https://files.pythonhosted.org/packages/0b/76/1794e440c1801ed35415238d2c728f26cd12695df9057154ad768b7b991c/pydantic_core-2.33.1-pp311-pypy311_pp73-macosx_10_12_x86_64.whl", hash = "sha256:3a371dc00282c4b84246509a5ddc808e61b9864aa1eae9ecc92bb1268b82db4a", size = 2042858 },
    { url = "https://files.pythonhosted.org/packages/73/b4/9cd7b081fb0b1b4f8150507cd59d27b275c3e22ad60b35cb19ea0977d9b9/pydantic_core-2.33.1-pp311-pypy311_pp73-macosx_11_0_arm64.whl", hash = "sha256:f59295ecc75a1788af8ba92f2e8c6eeaa5a94c22fc4d151e8d9638814f85c8fc", size = 1873745 },
    { url = "https://files.pythonhosted.org/packages/e1/d7/9ddb7575d4321e40d0363903c2576c8c0c3280ebea137777e5ab58d723e3/pydantic_core-2.33.1-pp311-pypy311_pp73-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:08530b8ac922003033f399128505f513e30ca770527cc8bbacf75a84fcc2c74b", size = 1904188 },
    { url = "https://files.pythonhosted.org/packages/d1/a8/3194ccfe461bb08da19377ebec8cb4f13c9bd82e13baebc53c5c7c39a029/pydantic_core-2.33.1-pp311-pypy311_pp73-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:bae370459da6a5466978c0eacf90690cb57ec9d533f8e63e564ef3822bfa04fe", size = 2083479 },
    { url = "https://files.pythonhosted.org/packages/42/c7/84cb569555d7179ca0b3f838cef08f66f7089b54432f5b8599aac6e9533e/pydantic_core-2.33.1-pp311-pypy311_pp73-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:e3de2777e3b9f4d603112f78006f4ae0acb936e95f06da6cb1a45fbad6bdb4b5", size = 2118415 },
    { url = "https://files.pythonhosted.org/packages/3b/67/72abb8c73e0837716afbb58a59cc9e3ae43d1aa8677f3b4bc72c16142716/pydantic_core-2.33.1-pp311-pypy311_pp73-musllinux_1_1_aarch64.whl", hash = "sha256:3a64e81e8cba118e108d7126362ea30e021291b7805d47e4896e52c791be2761", size = 2079623 },
    { url = "https://files.pythonhosted.org/packages/0b/cd/c59707e35a47ba4cbbf153c3f7c56420c58653b5801b055dc52cccc8e2dc/pydantic_core-2.33.1-pp311-pypy311_pp73-musllinux_1_1_armv7l.whl", hash = "sha256:52928d8c1b6bda03cc6d811e8923dffc87a2d3c8b3bfd2ce16471c7147a24850", size = 2250175 },
    { url = "https://files.pythonhosted.org/packages/84/32/e4325a6676b0bed32d5b084566ec86ed7fd1e9bcbfc49c578b1755bde920/pydantic_core-2.33.1-pp311-pypy311_pp73-musllinux_1_1_x86_64.whl", hash = "sha256:1b30d92c9412beb5ac6b10a3eb7ef92ccb14e3f2a8d7732e2d739f58b3aa7544", size = 2254674 },
    { url = "https://files.pythonhosted.org/packages/12/6f/5596dc418f2e292ffc661d21931ab34591952e2843e7168ea5a52591f6ff/pydantic_core-2.33.1-pp311-pypy311_pp73-win_amd64.whl", hash = "sha256:f995719707e0e29f0f41a8aa3bcea6e761a36c9136104d3189eafb83f5cec5e5", size = 2080951 },
    { url = "https://files.pythonhosted.org/packages/2d/a8/c2c8f29bd18f7ef52de32a6deb9e3ee87ba18b7b2122636aa9f4438cf627/pydantic_core-2.33.1-pp39-pypy39_pp73-macosx_10_12_x86_64.whl", hash = "sha256:7edbc454a29fc6aeae1e1eecba4f07b63b8d76e76a748532233c4c167b4cb9ea", size = 2041791 },
    { url = "https://files.pythonhosted.org/packages/08/ad/328081b1c82543ae49d0650048305058583c51f1a9a56a0d6e87bb3a2443/pydantic_core-2.33.1-pp39-pypy39_pp73-macosx_11_0_arm64.whl", hash = "sha256:ad05b683963f69a1d5d2c2bdab1274a31221ca737dbbceaa32bcb67359453cdd", size = 1873579 },
    { url = "https://files.pythonhosted.org/packages/6e/8a/bc65dbf7e501e88367cdab06a2c1340457c785f0c72288cae737fd80c0fa/pydantic_core-2.33.1-pp39-pypy39_pp73-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:df6a94bf9452c6da9b5d76ed229a5683d0306ccb91cca8e1eea883189780d568", size = 1904189 },
    { url = "https://files.pythonhosted.org/packages/9a/db/30ca6aefda211fb01ef185ca73cb7a0c6e7fe952c524025c8782b5acd771/pydantic_core-2.33.1-pp39-pypy39_pp73-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:7965c13b3967909a09ecc91f21d09cfc4576bf78140b988904e94f130f188396", size = 2084446 },
    { url = "https://files.pythonhosted.org/packages/f2/89/a12b55286e30c9f476eab7c53c9249ec76faf70430596496ab0309f28629/pydantic_core-2.33.1-pp39-pypy39_pp73-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:3f1fdb790440a34f6ecf7679e1863b825cb5ffde858a9197f851168ed08371e5", size = 2118215 },
    { url = "https://files.pythonhosted.org/packages/8e/55/12721c4a8d7951584ad3d9848b44442559cf1876e0bb424148d1060636b3/pydantic_core-2.33.1-pp39-pypy39_pp73-musllinux_1_1_aarch64.whl", hash = "sha256:5277aec8d879f8d05168fdd17ae811dd313b8ff894aeeaf7cd34ad28b4d77e33", size = 2079963 },
    { url = "https://files.pythonhosted.org/packages/bd/0c/3391bd5d6ff62ea998db94732528d9bc32c560b0ed861c39119759461946/pydantic_core-2.33.1-pp39-pypy39_pp73-musllinux_1_1_armv7l.whl", hash = "sha256:8ab581d3530611897d863d1a649fb0644b860286b4718db919bfd51ece41f10b", size = 2249388 },
    { url = "https://files.pythonhosted.org/packages/d3/5f/3e4feb042998d7886a9b523b372d83955cbc192a07013dcd24276db078ee/pydantic_core-2.33.1-pp39-pypy39_pp73-musllinux_1_1_x86_64.whl", hash = "sha256:0483847fa9ad5e3412265c1bd72aad35235512d9ce9d27d81a56d935ef489672", size = 2255226 },
    { url = "https://files.pythonhosted.org/packages/25/f2/1647933efaaad61846109a27619f3704929e758a09e6431b8f932a053d40/pydantic_core-2.33.1-pp39-pypy39_pp73-win_amd64.whl", hash = "sha256:de9e06abe3cc5ec6a2d5f75bc99b0bdca4f5c719a5b34026f8c57efbdecd2ee3", size = 2081073 },
]

[[package]]
name = "pygments"
version = "2.19.1"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/7c/2d/c3338d48ea6cc0feb8446d8e6937e1408088a72a39937982cc6111d17f84/pygments-2.19.1.tar.gz", hash = "sha256:61c16d2a8576dc0649d9f39e089b5f02bcd27fba10d8fb4dcc28173f7a45151f", size = 4968581 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/8a/0b/9fcc47d19c48b59121088dd6da2488a49d5f72dacf8262e2790a1d2c7d15/pygments-2.19.1-py3-none-any.whl", hash = "sha256:9ea1544ad55cecf4b8242fab6dd35a93bbce657034b0611ee383099054ab6d8c", size = 1225293 },
]

[[package]]
name = "pytest"
version = "8.3.5"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "colorama", marker = "sys_platform == 'win32'" },
    { name = "exceptiongroup", marker = "python_full_version < '3.11'" },
    { name = "iniconfig" },
    { name = "packaging" },
    { name = "pluggy" },
    { name = "tomli", marker = "python_full_version < '3.11'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/ae/3c/c9d525a414d506893f0cd8a8d0de7706446213181570cdbd766691164e40/pytest-8.3.5.tar.gz", hash = "sha256:f4efe70cc14e511565ac476b57c279e12a855b11f48f212af1080ef2263d3845", size = 1450891 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/30/3d/64ad57c803f1fa1e963a7946b6e0fea4a70df53c1a7fed304586539c2bac/pytest-8.3.5-py3-none-any.whl", hash = "sha256:c69214aa47deac29fad6c2a4f590b9c4a9fdb16a403176fe154b79c0b4d4d820", size = 343634 },
]

[[package]]
name = "pytest-cov"
version = "6.1.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "coverage", extra = ["toml"] },
    { name = "pytest" },
]
sdist = { url = "https://files.pythonhosted.org/packages/25/69/5f1e57f6c5a39f81411b550027bf72842c4567ff5fd572bed1edc9e4b5d9/pytest_cov-6.1.1.tar.gz", hash = "sha256:46935f7aaefba760e716c2ebfbe1c216240b9592966e7da99ea8292d4d3e2a0a", size = 66857 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/28/d0/def53b4a790cfb21483016430ed828f64830dd981ebe1089971cd10cab25/pytest_cov-6.1.1-py3-none-any.whl", hash = "sha256:bddf29ed2d0ab6f4df17b4c55b0a657287db8684af9c42ea546b21b1041b3dde", size = 23841 },
]

[[package]]
name = "python-dateutil"
version = "2.9.0.post0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "six" },
]
sdist = { url = "https://files.pythonhosted.org/packages/66/c0/0c8b6ad9f17a802ee498c46e004a0eb49bc148f2fd230864601a86dcf6db/python-dateutil-2.9.0.post0.tar.gz", hash = "sha256:37dd54208da7e1cd875388217d5e00ebd4179249f90fb72437e91a35459a0ad3", size = 342432 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/ec/57/56b9bcc3c9c6a792fcbaf139543cee77261f3651ca9da0c93f5c1221264b/python_dateutil-2.9.0.post0-py2.py3-none-any.whl", hash = "sha256:a8b2bc7bffae282281c8140a97d3aa9c14da0b136dfe83f850eea9a5f7470427", size = 229892 },
]

[[package]]
name = "pytz"
version = "2025.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/f8/bf/abbd3cdfb8fbc7fb3d4d38d320f2441b1e7cbe29be4f23797b4a2b5d8aac/pytz-2025.2.tar.gz", hash = "sha256:360b9e3dbb49a209c21ad61809c7fb453643e048b38924c765813546746e81c3", size = 320884 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/81/c4/34e93fe5f5429d7570ec1fa436f1986fb1f00c3e0f43a589fe2bbcd22c3f/pytz-2025.2-py2.py3-none-any.whl", hash = "sha256:5ddf76296dd8c44c26eb8f4b6f35488f3ccbf6fbbd7adee0b7262d43f0ec2f00", size = 509225 },
]

[[package]]
name = "pyyaml"
version = "6.0.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/54/ed/79a089b6be93607fa5cdaedf301d7dfb23af5f25c398d5ead2525b063e17/pyyaml-6.0.2.tar.gz", hash = "sha256:d584d9ec91ad65861cc08d42e834324ef890a082e591037abe114850ff7bbc3e", size = 130631 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/9b/95/a3fac87cb7158e231b5a6012e438c647e1a87f09f8e0d123acec8ab8bf71/PyYAML-6.0.2-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:0a9a2848a5b7feac301353437eb7d5957887edbf81d56e903999a75a3d743086", size = 184199 },
    { url = "https://files.pythonhosted.org/packages/c7/7a/68bd47624dab8fd4afbfd3c48e3b79efe09098ae941de5b58abcbadff5cb/PyYAML-6.0.2-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:29717114e51c84ddfba879543fb232a6ed60086602313ca38cce623c1d62cfbf", size = 171758 },
    { url = "https://files.pythonhosted.org/packages/49/ee/14c54df452143b9ee9f0f29074d7ca5516a36edb0b4cc40c3f280131656f/PyYAML-6.0.2-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:8824b5a04a04a047e72eea5cec3bc266db09e35de6bdfe34c9436ac5ee27d237", size = 718463 },
    { url = "https://files.pythonhosted.org/packages/4d/61/de363a97476e766574650d742205be468921a7b532aa2499fcd886b62530/PyYAML-6.0.2-cp310-cp310-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:7c36280e6fb8385e520936c3cb3b8042851904eba0e58d277dca80a5cfed590b", size = 719280 },
    { url = "https://files.pythonhosted.org/packages/6b/4e/1523cb902fd98355e2e9ea5e5eb237cbc5f3ad5f3075fa65087aa0ecb669/PyYAML-6.0.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:ec031d5d2feb36d1d1a24380e4db6d43695f3748343d99434e6f5f9156aaa2ed", size = 751239 },
    { url = "https://files.pythonhosted.org/packages/b7/33/5504b3a9a4464893c32f118a9cc045190a91637b119a9c881da1cf6b7a72/PyYAML-6.0.2-cp310-cp310-musllinux_1_1_aarch64.whl", hash = "sha256:936d68689298c36b53b29f23c6dbb74de12b4ac12ca6cfe0e047bedceea56180", size = 695802 },
    { url = "https://files.pythonhosted.org/packages/5c/20/8347dcabd41ef3a3cdc4f7b7a2aff3d06598c8779faa189cdbf878b626a4/PyYAML-6.0.2-cp310-cp310-musllinux_1_1_x86_64.whl", hash = "sha256:23502f431948090f597378482b4812b0caae32c22213aecf3b55325e049a6c68", size = 720527 },
    { url = "https://files.pythonhosted.org/packages/be/aa/5afe99233fb360d0ff37377145a949ae258aaab831bde4792b32650a4378/PyYAML-6.0.2-cp310-cp310-win32.whl", hash = "sha256:2e99c6826ffa974fe6e27cdb5ed0021786b03fc98e5ee3c5bfe1fd5015f42b99", size = 144052 },
    { url = "https://files.pythonhosted.org/packages/b5/84/0fa4b06f6d6c958d207620fc60005e241ecedceee58931bb20138e1e5776/PyYAML-6.0.2-cp310-cp310-win_amd64.whl", hash = "sha256:a4d3091415f010369ae4ed1fc6b79def9416358877534caf6a0fdd2146c87a3e", size = 161774 },
    { url = "https://files.pythonhosted.org/packages/f8/aa/7af4e81f7acba21a4c6be026da38fd2b872ca46226673c89a758ebdc4fd2/PyYAML-6.0.2-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:cc1c1159b3d456576af7a3e4d1ba7e6924cb39de8f67111c735f6fc832082774", size = 184612 },
    { url = "https://files.pythonhosted.org/packages/8b/62/b9faa998fd185f65c1371643678e4d58254add437edb764a08c5a98fb986/PyYAML-6.0.2-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:1e2120ef853f59c7419231f3bf4e7021f1b936f6ebd222406c3b60212205d2ee", size = 172040 },
    { url = "https://files.pythonhosted.org/packages/ad/0c/c804f5f922a9a6563bab712d8dcc70251e8af811fce4524d57c2c0fd49a4/PyYAML-6.0.2-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:5d225db5a45f21e78dd9358e58a98702a0302f2659a3c6cd320564b75b86f47c", size = 736829 },
    { url = "https://files.pythonhosted.org/packages/51/16/6af8d6a6b210c8e54f1406a6b9481febf9c64a3109c541567e35a49aa2e7/PyYAML-6.0.2-cp311-cp311-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:5ac9328ec4831237bec75defaf839f7d4564be1e6b25ac710bd1a96321cc8317", size = 764167 },
    { url = "https://files.pythonhosted.org/packages/75/e4/2c27590dfc9992f73aabbeb9241ae20220bd9452df27483b6e56d3975cc5/PyYAML-6.0.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:3ad2a3decf9aaba3d29c8f537ac4b243e36bef957511b4766cb0057d32b0be85", size = 762952 },
    { url = "https://files.pythonhosted.org/packages/9b/97/ecc1abf4a823f5ac61941a9c00fe501b02ac3ab0e373c3857f7d4b83e2b6/PyYAML-6.0.2-cp311-cp311-musllinux_1_1_aarch64.whl", hash = "sha256:ff3824dc5261f50c9b0dfb3be22b4567a6f938ccce4587b38952d85fd9e9afe4", size = 735301 },
    { url = "https://files.pythonhosted.org/packages/45/73/0f49dacd6e82c9430e46f4a027baa4ca205e8b0a9dce1397f44edc23559d/PyYAML-6.0.2-cp311-cp311-musllinux_1_1_x86_64.whl", hash = "sha256:797b4f722ffa07cc8d62053e4cff1486fa6dc094105d13fea7b1de7d8bf71c9e", size = 756638 },
    { url = "https://files.pythonhosted.org/packages/22/5f/956f0f9fc65223a58fbc14459bf34b4cc48dec52e00535c79b8db361aabd/PyYAML-6.0.2-cp311-cp311-win32.whl", hash = "sha256:11d8f3dd2b9c1207dcaf2ee0bbbfd5991f571186ec9cc78427ba5bd32afae4b5", size = 143850 },
    { url = "https://files.pythonhosted.org/packages/ed/23/8da0bbe2ab9dcdd11f4f4557ccaf95c10b9811b13ecced089d43ce59c3c8/PyYAML-6.0.2-cp311-cp311-win_amd64.whl", hash = "sha256:e10ce637b18caea04431ce14fabcf5c64a1c61ec9c56b071a4b7ca131ca52d44", size = 161980 },
    { url = "https://files.pythonhosted.org/packages/86/0c/c581167fc46d6d6d7ddcfb8c843a4de25bdd27e4466938109ca68492292c/PyYAML-6.0.2-cp312-cp312-macosx_10_9_x86_64.whl", hash = "sha256:c70c95198c015b85feafc136515252a261a84561b7b1d51e3384e0655ddf25ab", size = 183873 },
    { url = "https://files.pythonhosted.org/packages/a8/0c/38374f5bb272c051e2a69281d71cba6fdb983413e6758b84482905e29a5d/PyYAML-6.0.2-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:ce826d6ef20b1bc864f0a68340c8b3287705cae2f8b4b1d932177dcc76721725", size = 173302 },
    { url = "https://files.pythonhosted.org/packages/c3/93/9916574aa8c00aa06bbac729972eb1071d002b8e158bd0e83a3b9a20a1f7/PyYAML-6.0.2-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:1f71ea527786de97d1a0cc0eacd1defc0985dcf6b3f17bb77dcfc8c34bec4dc5", size = 739154 },
    { url = "https://files.pythonhosted.org/packages/95/0f/b8938f1cbd09739c6da569d172531567dbcc9789e0029aa070856f123984/PyYAML-6.0.2-cp312-cp312-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:9b22676e8097e9e22e36d6b7bda33190d0d400f345f23d4065d48f4ca7ae0425", size = 766223 },
    { url = "https://files.pythonhosted.org/packages/b9/2b/614b4752f2e127db5cc206abc23a8c19678e92b23c3db30fc86ab731d3bd/PyYAML-6.0.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:80bab7bfc629882493af4aa31a4cfa43a4c57c83813253626916b8c7ada83476", size = 767542 },
    { url = "https://files.pythonhosted.org/packages/d4/00/dd137d5bcc7efea1836d6264f049359861cf548469d18da90cd8216cf05f/PyYAML-6.0.2-cp312-cp312-musllinux_1_1_aarch64.whl", hash = "sha256:0833f8694549e586547b576dcfaba4a6b55b9e96098b36cdc7ebefe667dfed48", size = 731164 },
    { url = "https://files.pythonhosted.org/packages/c9/1f/4f998c900485e5c0ef43838363ba4a9723ac0ad73a9dc42068b12aaba4e4/PyYAML-6.0.2-cp312-cp312-musllinux_1_1_x86_64.whl", hash = "sha256:8b9c7197f7cb2738065c481a0461e50ad02f18c78cd75775628afb4d7137fb3b", size = 756611 },
    { url = "https://files.pythonhosted.org/packages/df/d1/f5a275fdb252768b7a11ec63585bc38d0e87c9e05668a139fea92b80634c/PyYAML-6.0.2-cp312-cp312-win32.whl", hash = "sha256:ef6107725bd54b262d6dedcc2af448a266975032bc85ef0172c5f059da6325b4", size = 140591 },
    { url = "https://files.pythonhosted.org/packages/0c/e8/4f648c598b17c3d06e8753d7d13d57542b30d56e6c2dedf9c331ae56312e/PyYAML-6.0.2-cp312-cp312-win_amd64.whl", hash = "sha256:7e7401d0de89a9a855c839bc697c079a4af81cf878373abd7dc625847d25cbd8", size = 156338 },
    { url = "https://files.pythonhosted.org/packages/ef/e3/3af305b830494fa85d95f6d95ef7fa73f2ee1cc8ef5b495c7c3269fb835f/PyYAML-6.0.2-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:efdca5630322a10774e8e98e1af481aad470dd62c3170801852d752aa7a783ba", size = 181309 },
    { url = "https://files.pythonhosted.org/packages/45/9f/3b1c20a0b7a3200524eb0076cc027a970d320bd3a6592873c85c92a08731/PyYAML-6.0.2-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:50187695423ffe49e2deacb8cd10510bc361faac997de9efef88badc3bb9e2d1", size = 171679 },
    { url = "https://files.pythonhosted.org/packages/7c/9a/337322f27005c33bcb656c655fa78325b730324c78620e8328ae28b64d0c/PyYAML-6.0.2-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:0ffe8360bab4910ef1b9e87fb812d8bc0a308b0d0eef8c8f44e0254ab3b07133", size = 733428 },
    { url = "https://files.pythonhosted.org/packages/a3/69/864fbe19e6c18ea3cc196cbe5d392175b4cf3d5d0ac1403ec3f2d237ebb5/PyYAML-6.0.2-cp313-cp313-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:17e311b6c678207928d649faa7cb0d7b4c26a0ba73d41e99c4fff6b6c3276484", size = 763361 },
    { url = "https://files.pythonhosted.org/packages/04/24/b7721e4845c2f162d26f50521b825fb061bc0a5afcf9a386840f23ea19fa/PyYAML-6.0.2-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:70b189594dbe54f75ab3a1acec5f1e3faa7e8cf2f1e08d9b561cb41b845f69d5", size = 759523 },
    { url = "https://files.pythonhosted.org/packages/2b/b2/e3234f59ba06559c6ff63c4e10baea10e5e7df868092bf9ab40e5b9c56b6/PyYAML-6.0.2-cp313-cp313-musllinux_1_1_aarch64.whl", hash = "sha256:41e4e3953a79407c794916fa277a82531dd93aad34e29c2a514c2c0c5fe971cc", size = 726660 },
    { url = "https://files.pythonhosted.org/packages/fe/0f/25911a9f080464c59fab9027482f822b86bf0608957a5fcc6eaac85aa515/PyYAML-6.0.2-cp313-cp313-musllinux_1_1_x86_64.whl", hash = "sha256:68ccc6023a3400877818152ad9a1033e3db8625d899c72eacb5a668902e4d652", size = 751597 },
    { url = "https://files.pythonhosted.org/packages/14/0d/e2c3b43bbce3cf6bd97c840b46088a3031085179e596d4929729d8d68270/PyYAML-6.0.2-cp313-cp313-win32.whl", hash = "sha256:bc2fa7c6b47d6bc618dd7fb02ef6fdedb1090ec036abab80d4681424b84c1183", size = 140527 },
    { url = "https://files.pythonhosted.org/packages/fa/de/02b54f42487e3d3c6efb3f89428677074ca7bf43aae402517bc7cca949f3/PyYAML-6.0.2-cp313-cp313-win_amd64.whl", hash = "sha256:8388ee1976c416731879ac16da0aff3f63b286ffdd57cdeb95f3f2e085687563", size = 156446 },
    { url = "https://files.pythonhosted.org/packages/65/d8/b7a1db13636d7fb7d4ff431593c510c8b8fca920ade06ca8ef20015493c5/PyYAML-6.0.2-cp39-cp39-macosx_10_9_x86_64.whl", hash = "sha256:688ba32a1cffef67fd2e9398a2efebaea461578b0923624778664cc1c914db5d", size = 184777 },
    { url = "https://files.pythonhosted.org/packages/0a/02/6ec546cd45143fdf9840b2c6be8d875116a64076218b61d68e12548e5839/PyYAML-6.0.2-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:a8786accb172bd8afb8be14490a16625cbc387036876ab6ba70912730faf8e1f", size = 172318 },
    { url = "https://files.pythonhosted.org/packages/0e/9a/8cc68be846c972bda34f6c2a93abb644fb2476f4dcc924d52175786932c9/PyYAML-6.0.2-cp39-cp39-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:d8e03406cac8513435335dbab54c0d385e4a49e4945d2909a581c83647ca0290", size = 720891 },
    { url = "https://files.pythonhosted.org/packages/e9/6c/6e1b7f40181bc4805e2e07f4abc10a88ce4648e7e95ff1abe4ae4014a9b2/PyYAML-6.0.2-cp39-cp39-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:f753120cb8181e736c57ef7636e83f31b9c0d1722c516f7e86cf15b7aa57ff12", size = 722614 },
    { url = "https://files.pythonhosted.org/packages/3d/32/e7bd8535d22ea2874cef6a81021ba019474ace0d13a4819c2a4bce79bd6a/PyYAML-6.0.2-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:3b1fdb9dc17f5a7677423d508ab4f243a726dea51fa5e70992e59a7411c89d19", size = 737360 },
    { url = "https://files.pythonhosted.org/packages/d7/12/7322c1e30b9be969670b672573d45479edef72c9a0deac3bb2868f5d7469/PyYAML-6.0.2-cp39-cp39-musllinux_1_1_aarch64.whl", hash = "sha256:0b69e4ce7a131fe56b7e4d770c67429700908fc0752af059838b1cfb41960e4e", size = 699006 },
    { url = "https://files.pythonhosted.org/packages/82/72/04fcad41ca56491995076630c3ec1e834be241664c0c09a64c9a2589b507/PyYAML-6.0.2-cp39-cp39-musllinux_1_1_x86_64.whl", hash = "sha256:a9f8c2e67970f13b16084e04f134610fd1d374bf477b17ec1599185cf611d725", size = 723577 },
    { url = "https://files.pythonhosted.org/packages/ed/5e/46168b1f2757f1fcd442bc3029cd8767d88a98c9c05770d8b420948743bb/PyYAML-6.0.2-cp39-cp39-win32.whl", hash = "sha256:6395c297d42274772abc367baaa79683958044e5d3835486c16da75d2a694631", size = 144593 },
    { url = "https://files.pythonhosted.org/packages/19/87/5124b1c1f2412bb95c59ec481eaf936cd32f0fe2a7b16b97b81c4c017a6a/PyYAML-6.0.2-cp39-cp39-win_amd64.whl", hash = "sha256:39693e1f8320ae4f43943590b49779ffb98acb81f788220ea932a6b6c51004d8", size = 162312 },
]

[[package]]
name = "regex"
version = "2024.11.6"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/8e/5f/bd69653fbfb76cf8604468d3b4ec4c403197144c7bfe0e6a5fc9e02a07cb/regex-2024.11.6.tar.gz", hash = "sha256:7ab159b063c52a0333c884e4679f8d7a85112ee3078fe3d9004b2dd875585519", size = 399494 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/95/3c/4651f6b130c6842a8f3df82461a8950f923925db8b6961063e82744bddcc/regex-2024.11.6-cp310-cp310-macosx_10_9_universal2.whl", hash = "sha256:ff590880083d60acc0433f9c3f713c51f7ac6ebb9adf889c79a261ecf541aa91", size = 482674 },
    { url = "https://files.pythonhosted.org/packages/15/51/9f35d12da8434b489c7b7bffc205c474a0a9432a889457026e9bc06a297a/regex-2024.11.6-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:658f90550f38270639e83ce492f27d2c8d2cd63805c65a13a14d36ca126753f0", size = 287684 },
    { url = "https://files.pythonhosted.org/packages/bd/18/b731f5510d1b8fb63c6b6d3484bfa9a59b84cc578ac8b5172970e05ae07c/regex-2024.11.6-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:164d8b7b3b4bcb2068b97428060b2a53be050085ef94eca7f240e7947f1b080e", size = 284589 },
    { url = "https://files.pythonhosted.org/packages/78/a2/6dd36e16341ab95e4c6073426561b9bfdeb1a9c9b63ab1b579c2e96cb105/regex-2024.11.6-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:d3660c82f209655a06b587d55e723f0b813d3a7db2e32e5e7dc64ac2a9e86fde", size = 782511 },
    { url = "https://files.pythonhosted.org/packages/1b/2b/323e72d5d2fd8de0d9baa443e1ed70363ed7e7b2fb526f5950c5cb99c364/regex-2024.11.6-cp310-cp310-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:d22326fcdef5e08c154280b71163ced384b428343ae16a5ab2b3354aed12436e", size = 821149 },
    { url = "https://files.pythonhosted.org/packages/90/30/63373b9ea468fbef8a907fd273e5c329b8c9535fee36fc8dba5fecac475d/regex-2024.11.6-cp310-cp310-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:f1ac758ef6aebfc8943560194e9fd0fa18bcb34d89fd8bd2af18183afd8da3a2", size = 809707 },
    { url = "https://files.pythonhosted.org/packages/f2/98/26d3830875b53071f1f0ae6d547f1d98e964dd29ad35cbf94439120bb67a/regex-2024.11.6-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:997d6a487ff00807ba810e0f8332c18b4eb8d29463cfb7c820dc4b6e7562d0cf", size = 781702 },
    { url = "https://files.pythonhosted.org/packages/87/55/eb2a068334274db86208ab9d5599ffa63631b9f0f67ed70ea7c82a69bbc8/regex-2024.11.6-cp310-cp310-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:02a02d2bb04fec86ad61f3ea7f49c015a0681bf76abb9857f945d26159d2968c", size = 771976 },
    { url = "https://files.pythonhosted.org/packages/74/c0/be707bcfe98254d8f9d2cff55d216e946f4ea48ad2fd8cf1428f8c5332ba/regex-2024.11.6-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_12_x86_64.manylinux2010_x86_64.whl", hash = "sha256:f02f93b92358ee3f78660e43b4b0091229260c5d5c408d17d60bf26b6c900e86", size = 697397 },
    { url = "https://files.pythonhosted.org/packages/49/dc/bb45572ceb49e0f6509f7596e4ba7031f6819ecb26bc7610979af5a77f45/regex-2024.11.6-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:06eb1be98df10e81ebaded73fcd51989dcf534e3c753466e4b60c4697a003b67", size = 768726 },
    { url = "https://files.pythonhosted.org/packages/5a/db/f43fd75dc4c0c2d96d0881967897926942e935d700863666f3c844a72ce6/regex-2024.11.6-cp310-cp310-musllinux_1_2_i686.whl", hash = "sha256:040df6fe1a5504eb0f04f048e6d09cd7c7110fef851d7c567a6b6e09942feb7d", size = 775098 },
    { url = "https://files.pythonhosted.org/packages/99/d7/f94154db29ab5a89d69ff893159b19ada89e76b915c1293e98603d39838c/regex-2024.11.6-cp310-cp310-musllinux_1_2_ppc64le.whl", hash = "sha256:fdabbfc59f2c6edba2a6622c647b716e34e8e3867e0ab975412c5c2f79b82da2", size = 839325 },
    { url = "https://files.pythonhosted.org/packages/f7/17/3cbfab1f23356fbbf07708220ab438a7efa1e0f34195bf857433f79f1788/regex-2024.11.6-cp310-cp310-musllinux_1_2_s390x.whl", hash = "sha256:8447d2d39b5abe381419319f942de20b7ecd60ce86f16a23b0698f22e1b70008", size = 843277 },
    { url = "https://files.pythonhosted.org/packages/7e/f2/48b393b51900456155de3ad001900f94298965e1cad1c772b87f9cfea011/regex-2024.11.6-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:da8f5fc57d1933de22a9e23eec290a0d8a5927a5370d24bda9a6abe50683fe62", size = 773197 },
    { url = "https://files.pythonhosted.org/packages/45/3f/ef9589aba93e084cd3f8471fded352826dcae8489b650d0b9b27bc5bba8a/regex-2024.11.6-cp310-cp310-win32.whl", hash = "sha256:b489578720afb782f6ccf2840920f3a32e31ba28a4b162e13900c3e6bd3f930e", size = 261714 },
    { url = "https://files.pythonhosted.org/packages/42/7e/5f1b92c8468290c465fd50c5318da64319133231415a8aa6ea5ab995a815/regex-2024.11.6-cp310-cp310-win_amd64.whl", hash = "sha256:5071b2093e793357c9d8b2929dfc13ac5f0a6c650559503bb81189d0a3814519", size = 274042 },
    { url = "https://files.pythonhosted.org/packages/58/58/7e4d9493a66c88a7da6d205768119f51af0f684fe7be7bac8328e217a52c/regex-2024.11.6-cp311-cp311-macosx_10_9_universal2.whl", hash = "sha256:5478c6962ad548b54a591778e93cd7c456a7a29f8eca9c49e4f9a806dcc5d638", size = 482669 },
    { url = "https://files.pythonhosted.org/packages/34/4c/8f8e631fcdc2ff978609eaeef1d6994bf2f028b59d9ac67640ed051f1218/regex-2024.11.6-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:2c89a8cc122b25ce6945f0423dc1352cb9593c68abd19223eebbd4e56612c5b7", size = 287684 },
    { url = "https://files.pythonhosted.org/packages/c5/1b/f0e4d13e6adf866ce9b069e191f303a30ab1277e037037a365c3aad5cc9c/regex-2024.11.6-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:94d87b689cdd831934fa3ce16cc15cd65748e6d689f5d2b8f4f4df2065c9fa20", size = 284589 },
    { url = "https://files.pythonhosted.org/packages/25/4d/ab21047f446693887f25510887e6820b93f791992994f6498b0318904d4a/regex-2024.11.6-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:1062b39a0a2b75a9c694f7a08e7183a80c63c0d62b301418ffd9c35f55aaa114", size = 792121 },
    { url = "https://files.pythonhosted.org/packages/45/ee/c867e15cd894985cb32b731d89576c41a4642a57850c162490ea34b78c3b/regex-2024.11.6-cp311-cp311-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:167ed4852351d8a750da48712c3930b031f6efdaa0f22fa1933716bfcd6bf4a3", size = 831275 },
    { url = "https://files.pythonhosted.org/packages/b3/12/b0f480726cf1c60f6536fa5e1c95275a77624f3ac8fdccf79e6727499e28/regex-2024.11.6-cp311-cp311-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:2d548dafee61f06ebdb584080621f3e0c23fff312f0de1afc776e2a2ba99a74f", size = 818257 },
    { url = "https://files.pythonhosted.org/packages/bf/ce/0d0e61429f603bac433910d99ef1a02ce45a8967ffbe3cbee48599e62d88/regex-2024.11.6-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:f2a19f302cd1ce5dd01a9099aaa19cae6173306d1302a43b627f62e21cf18ac0", size = 792727 },
    { url = "https://files.pythonhosted.org/packages/e4/c1/243c83c53d4a419c1556f43777ccb552bccdf79d08fda3980e4e77dd9137/regex-2024.11.6-cp311-cp311-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:bec9931dfb61ddd8ef2ebc05646293812cb6b16b60cf7c9511a832b6f1854b55", size = 780667 },
    { url = "https://files.pythonhosted.org/packages/c5/f4/75eb0dd4ce4b37f04928987f1d22547ddaf6c4bae697623c1b05da67a8aa/regex-2024.11.6-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:9714398225f299aa85267fd222f7142fcb5c769e73d7733344efc46f2ef5cf89", size = 776963 },
    { url = "https://files.pythonhosted.org/packages/16/5d/95c568574e630e141a69ff8a254c2f188b4398e813c40d49228c9bbd9875/regex-2024.11.6-cp311-cp311-musllinux_1_2_i686.whl", hash = "sha256:202eb32e89f60fc147a41e55cb086db2a3f8cb82f9a9a88440dcfc5d37faae8d", size = 784700 },
    { url = "https://files.pythonhosted.org/packages/8e/b5/f8495c7917f15cc6fee1e7f395e324ec3e00ab3c665a7dc9d27562fd5290/regex-2024.11.6-cp311-cp311-musllinux_1_2_ppc64le.whl", hash = "sha256:4181b814e56078e9b00427ca358ec44333765f5ca1b45597ec7446d3a1ef6e34", size = 848592 },
    { url = "https://files.pythonhosted.org/packages/1c/80/6dd7118e8cb212c3c60b191b932dc57db93fb2e36fb9e0e92f72a5909af9/regex-2024.11.6-cp311-cp311-musllinux_1_2_s390x.whl", hash = "sha256:068376da5a7e4da51968ce4c122a7cd31afaaec4fccc7856c92f63876e57b51d", size = 852929 },
    { url = "https://files.pythonhosted.org/packages/11/9b/5a05d2040297d2d254baf95eeeb6df83554e5e1df03bc1a6687fc4ba1f66/regex-2024.11.6-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:ac10f2c4184420d881a3475fb2c6f4d95d53a8d50209a2500723d831036f7c45", size = 781213 },
    { url = "https://files.pythonhosted.org/packages/26/b7/b14e2440156ab39e0177506c08c18accaf2b8932e39fb092074de733d868/regex-2024.11.6-cp311-cp311-win32.whl", hash = "sha256:c36f9b6f5f8649bb251a5f3f66564438977b7ef8386a52460ae77e6070d309d9", size = 261734 },
    { url = "https://files.pythonhosted.org/packages/80/32/763a6cc01d21fb3819227a1cc3f60fd251c13c37c27a73b8ff4315433a8e/regex-2024.11.6-cp311-cp311-win_amd64.whl", hash = "sha256:02e28184be537f0e75c1f9b2f8847dc51e08e6e171c6bde130b2687e0c33cf60", size = 274052 },
    { url = "https://files.pythonhosted.org/packages/ba/30/9a87ce8336b172cc232a0db89a3af97929d06c11ceaa19d97d84fa90a8f8/regex-2024.11.6-cp312-cp312-macosx_10_13_universal2.whl", hash = "sha256:52fb28f528778f184f870b7cf8f225f5eef0a8f6e3778529bdd40c7b3920796a", size = 483781 },
    { url = "https://files.pythonhosted.org/packages/01/e8/00008ad4ff4be8b1844786ba6636035f7ef926db5686e4c0f98093612add/regex-2024.11.6-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:fdd6028445d2460f33136c55eeb1f601ab06d74cb3347132e1c24250187500d9", size = 288455 },
    { url = "https://files.pythonhosted.org/packages/60/85/cebcc0aff603ea0a201667b203f13ba75d9fc8668fab917ac5b2de3967bc/regex-2024.11.6-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:805e6b60c54bf766b251e94526ebad60b7de0c70f70a4e6210ee2891acb70bf2", size = 284759 },
    { url = "https://files.pythonhosted.org/packages/94/2b/701a4b0585cb05472a4da28ee28fdfe155f3638f5e1ec92306d924e5faf0/regex-2024.11.6-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:b85c2530be953a890eaffde05485238f07029600e8f098cdf1848d414a8b45e4", size = 794976 },
    { url = "https://files.pythonhosted.org/packages/4b/bf/fa87e563bf5fee75db8915f7352e1887b1249126a1be4813837f5dbec965/regex-2024.11.6-cp312-cp312-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:bb26437975da7dc36b7efad18aa9dd4ea569d2357ae6b783bf1118dabd9ea577", size = 833077 },
    { url = "https://files.pythonhosted.org/packages/a1/56/7295e6bad94b047f4d0834e4779491b81216583c00c288252ef625c01d23/regex-2024.11.6-cp312-cp312-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:abfa5080c374a76a251ba60683242bc17eeb2c9818d0d30117b4486be10c59d3", size = 823160 },
    { url = "https://files.pythonhosted.org/packages/fb/13/e3b075031a738c9598c51cfbc4c7879e26729c53aa9cca59211c44235314/regex-2024.11.6-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:70b7fa6606c2881c1db9479b0eaa11ed5dfa11c8d60a474ff0e095099f39d98e", size = 796896 },
    { url = "https://files.pythonhosted.org/packages/24/56/0b3f1b66d592be6efec23a795b37732682520b47c53da5a32c33ed7d84e3/regex-2024.11.6-cp312-cp312-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:0c32f75920cf99fe6b6c539c399a4a128452eaf1af27f39bce8909c9a3fd8cbe", size = 783997 },
    { url = "https://files.pythonhosted.org/packages/f9/a1/eb378dada8b91c0e4c5f08ffb56f25fcae47bf52ad18f9b2f33b83e6d498/regex-2024.11.6-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:982e6d21414e78e1f51cf595d7f321dcd14de1f2881c5dc6a6e23bbbbd68435e", size = 781725 },
    { url = "https://files.pythonhosted.org/packages/83/f2/033e7dec0cfd6dda93390089864732a3409246ffe8b042e9554afa9bff4e/regex-2024.11.6-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:a7c2155f790e2fb448faed6dd241386719802296ec588a8b9051c1f5c481bc29", size = 789481 },
    { url = "https://files.pythonhosted.org/packages/83/23/15d4552ea28990a74e7696780c438aadd73a20318c47e527b47a4a5a596d/regex-2024.11.6-cp312-cp312-musllinux_1_2_ppc64le.whl", hash = "sha256:149f5008d286636e48cd0b1dd65018548944e495b0265b45e1bffecce1ef7f39", size = 852896 },
    { url = "https://files.pythonhosted.org/packages/e3/39/ed4416bc90deedbfdada2568b2cb0bc1fdb98efe11f5378d9892b2a88f8f/regex-2024.11.6-cp312-cp312-musllinux_1_2_s390x.whl", hash = "sha256:e5364a4502efca094731680e80009632ad6624084aff9a23ce8c8c6820de3e51", size = 860138 },
    { url = "https://files.pythonhosted.org/packages/93/2d/dd56bb76bd8e95bbce684326302f287455b56242a4f9c61f1bc76e28360e/regex-2024.11.6-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:0a86e7eeca091c09e021db8eb72d54751e527fa47b8d5787caf96d9831bd02ad", size = 787692 },
    { url = "https://files.pythonhosted.org/packages/0b/55/31877a249ab7a5156758246b9c59539abbeba22461b7d8adc9e8475ff73e/regex-2024.11.6-cp312-cp312-win32.whl", hash = "sha256:32f9a4c643baad4efa81d549c2aadefaeba12249b2adc5af541759237eee1c54", size = 262135 },
    { url = "https://files.pythonhosted.org/packages/38/ec/ad2d7de49a600cdb8dd78434a1aeffe28b9d6fc42eb36afab4a27ad23384/regex-2024.11.6-cp312-cp312-win_amd64.whl", hash = "sha256:a93c194e2df18f7d264092dc8539b8ffb86b45b899ab976aa15d48214138e81b", size = 273567 },
    { url = "https://files.pythonhosted.org/packages/90/73/bcb0e36614601016552fa9344544a3a2ae1809dc1401b100eab02e772e1f/regex-2024.11.6-cp313-cp313-macosx_10_13_universal2.whl", hash = "sha256:a6ba92c0bcdf96cbf43a12c717eae4bc98325ca3730f6b130ffa2e3c3c723d84", size = 483525 },
    { url = "https://files.pythonhosted.org/packages/0f/3f/f1a082a46b31e25291d830b369b6b0c5576a6f7fb89d3053a354c24b8a83/regex-2024.11.6-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:525eab0b789891ac3be914d36893bdf972d483fe66551f79d3e27146191a37d4", size = 288324 },
    { url = "https://files.pythonhosted.org/packages/09/c9/4e68181a4a652fb3ef5099e077faf4fd2a694ea6e0f806a7737aff9e758a/regex-2024.11.6-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:086a27a0b4ca227941700e0b31425e7a28ef1ae8e5e05a33826e17e47fbfdba0", size = 284617 },
    { url = "https://files.pythonhosted.org/packages/fc/fd/37868b75eaf63843165f1d2122ca6cb94bfc0271e4428cf58c0616786dce/regex-2024.11.6-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:bde01f35767c4a7899b7eb6e823b125a64de314a8ee9791367c9a34d56af18d0", size = 795023 },
    { url = "https://files.pythonhosted.org/packages/c4/7c/d4cd9c528502a3dedb5c13c146e7a7a539a3853dc20209c8e75d9ba9d1b2/regex-2024.11.6-cp313-cp313-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:b583904576650166b3d920d2bcce13971f6f9e9a396c673187f49811b2769dc7", size = 833072 },
    { url = "https://files.pythonhosted.org/packages/4f/db/46f563a08f969159c5a0f0e722260568425363bea43bb7ae370becb66a67/regex-2024.11.6-cp313-cp313-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:1c4de13f06a0d54fa0d5ab1b7138bfa0d883220965a29616e3ea61b35d5f5fc7", size = 823130 },
    { url = "https://files.pythonhosted.org/packages/db/60/1eeca2074f5b87df394fccaa432ae3fc06c9c9bfa97c5051aed70e6e00c2/regex-2024.11.6-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:3cde6e9f2580eb1665965ce9bf17ff4952f34f5b126beb509fee8f4e994f143c", size = 796857 },
    { url = "https://files.pythonhosted.org/packages/10/db/ac718a08fcee981554d2f7bb8402f1faa7e868c1345c16ab1ebec54b0d7b/regex-2024.11.6-cp313-cp313-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:0d7f453dca13f40a02b79636a339c5b62b670141e63efd511d3f8f73fba162b3", size = 784006 },
    { url = "https://files.pythonhosted.org/packages/c2/41/7da3fe70216cea93144bf12da2b87367590bcf07db97604edeea55dac9ad/regex-2024.11.6-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:59dfe1ed21aea057a65c6b586afd2a945de04fc7db3de0a6e3ed5397ad491b07", size = 781650 },
    { url = "https://files.pythonhosted.org/packages/a7/d5/880921ee4eec393a4752e6ab9f0fe28009435417c3102fc413f3fe81c4e5/regex-2024.11.6-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:b97c1e0bd37c5cd7902e65f410779d39eeda155800b65fc4d04cc432efa9bc6e", size = 789545 },
    { url = "https://files.pythonhosted.org/packages/dc/96/53770115e507081122beca8899ab7f5ae28ae790bfcc82b5e38976df6a77/regex-2024.11.6-cp313-cp313-musllinux_1_2_ppc64le.whl", hash = "sha256:f9d1e379028e0fc2ae3654bac3cbbef81bf3fd571272a42d56c24007979bafb6", size = 853045 },
    { url = "https://files.pythonhosted.org/packages/31/d3/1372add5251cc2d44b451bd94f43b2ec78e15a6e82bff6a290ef9fd8f00a/regex-2024.11.6-cp313-cp313-musllinux_1_2_s390x.whl", hash = "sha256:13291b39131e2d002a7940fb176e120bec5145f3aeb7621be6534e46251912c4", size = 860182 },
    { url = "https://files.pythonhosted.org/packages/ed/e3/c446a64984ea9f69982ba1a69d4658d5014bc7a0ea468a07e1a1265db6e2/regex-2024.11.6-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:4f51f88c126370dcec4908576c5a627220da6c09d0bff31cfa89f2523843316d", size = 787733 },
    { url = "https://files.pythonhosted.org/packages/2b/f1/e40c8373e3480e4f29f2692bd21b3e05f296d3afebc7e5dcf21b9756ca1c/regex-2024.11.6-cp313-cp313-win32.whl", hash = "sha256:63b13cfd72e9601125027202cad74995ab26921d8cd935c25f09c630436348ff", size = 262122 },
    { url = "https://files.pythonhosted.org/packages/45/94/bc295babb3062a731f52621cdc992d123111282e291abaf23faa413443ea/regex-2024.11.6-cp313-cp313-win_amd64.whl", hash = "sha256:2b3361af3198667e99927da8b84c1b010752fa4b1115ee30beaa332cabc3ef1a", size = 273545 },
    { url = "https://files.pythonhosted.org/packages/89/23/c4a86df398e57e26f93b13ae63acce58771e04bdde86092502496fa57f9c/regex-2024.11.6-cp39-cp39-macosx_10_9_universal2.whl", hash = "sha256:5704e174f8ccab2026bd2f1ab6c510345ae8eac818b613d7d73e785f1310f839", size = 482682 },
    { url = "https://files.pythonhosted.org/packages/3c/8b/45c24ab7a51a1658441b961b86209c43e6bb9d39caf1e63f46ce6ea03bc7/regex-2024.11.6-cp39-cp39-macosx_10_9_x86_64.whl", hash = "sha256:220902c3c5cc6af55d4fe19ead504de80eb91f786dc102fbd74894b1551f095e", size = 287679 },
    { url = "https://files.pythonhosted.org/packages/7a/d1/598de10b17fdafc452d11f7dada11c3be4e379a8671393e4e3da3c4070df/regex-2024.11.6-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:5e7e351589da0850c125f1600a4c4ba3c722efefe16b297de54300f08d734fbf", size = 284578 },
    { url = "https://files.pythonhosted.org/packages/49/70/c7eaa219efa67a215846766fde18d92d54cb590b6a04ffe43cef30057622/regex-2024.11.6-cp39-cp39-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:5056b185ca113c88e18223183aa1a50e66507769c9640a6ff75859619d73957b", size = 782012 },
    { url = "https://files.pythonhosted.org/packages/89/e5/ef52c7eb117dd20ff1697968219971d052138965a4d3d9b95e92e549f505/regex-2024.11.6-cp39-cp39-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:2e34b51b650b23ed3354b5a07aab37034d9f923db2a40519139af34f485f77d0", size = 820580 },
    { url = "https://files.pythonhosted.org/packages/5f/3f/9f5da81aff1d4167ac52711acf789df13e789fe6ac9545552e49138e3282/regex-2024.11.6-cp39-cp39-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:5670bce7b200273eee1840ef307bfa07cda90b38ae56e9a6ebcc9f50da9c469b", size = 809110 },
    { url = "https://files.pythonhosted.org/packages/86/44/2101cc0890c3621b90365c9ee8d7291a597c0722ad66eccd6ffa7f1bcc09/regex-2024.11.6-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:08986dce1339bc932923e7d1232ce9881499a0e02925f7402fb7c982515419ef", size = 780919 },
    { url = "https://files.pythonhosted.org/packages/ce/2e/3e0668d8d1c7c3c0d397bf54d92fc182575b3a26939aed5000d3cc78760f/regex-2024.11.6-cp39-cp39-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:93c0b12d3d3bc25af4ebbf38f9ee780a487e8bf6954c115b9f015822d3bb8e48", size = 771515 },
    { url = "https://files.pythonhosted.org/packages/a6/49/1bc4584254355e3dba930a3a2fd7ad26ccba3ebbab7d9100db0aff2eedb0/regex-2024.11.6-cp39-cp39-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_12_x86_64.manylinux2010_x86_64.whl", hash = "sha256:764e71f22ab3b305e7f4c21f1a97e1526a25ebdd22513e251cf376760213da13", size = 696957 },
    { url = "https://files.pythonhosted.org/packages/c8/dd/42879c1fc8a37a887cd08e358af3d3ba9e23038cd77c7fe044a86d9450ba/regex-2024.11.6-cp39-cp39-musllinux_1_2_aarch64.whl", hash = "sha256:f056bf21105c2515c32372bbc057f43eb02aae2fda61052e2f7622c801f0b4e2", size = 768088 },
    { url = "https://files.pythonhosted.org/packages/89/96/c05a0fe173cd2acd29d5e13c1adad8b706bcaa71b169e1ee57dcf2e74584/regex-2024.11.6-cp39-cp39-musllinux_1_2_i686.whl", hash = "sha256:69ab78f848845569401469da20df3e081e6b5a11cb086de3eed1d48f5ed57c95", size = 774752 },
    { url = "https://files.pythonhosted.org/packages/b5/f3/a757748066255f97f14506483436c5f6aded7af9e37bca04ec30c90ca683/regex-2024.11.6-cp39-cp39-musllinux_1_2_ppc64le.whl", hash = "sha256:86fddba590aad9208e2fa8b43b4c098bb0ec74f15718bb6a704e3c63e2cef3e9", size = 838862 },
    { url = "https://files.pythonhosted.org/packages/5c/93/c6d2092fd479dcaeea40fc8fa673822829181ded77d294a7f950f1dda6e2/regex-2024.11.6-cp39-cp39-musllinux_1_2_s390x.whl", hash = "sha256:684d7a212682996d21ca12ef3c17353c021fe9de6049e19ac8481ec35574a70f", size = 842622 },
    { url = "https://files.pythonhosted.org/packages/ff/9c/daa99532c72f25051a90ef90e1413a8d54413a9e64614d9095b0c1c154d0/regex-2024.11.6-cp39-cp39-musllinux_1_2_x86_64.whl", hash = "sha256:a03e02f48cd1abbd9f3b7e3586d97c8f7a9721c436f51a5245b3b9483044480b", size = 772713 },
    { url = "https://files.pythonhosted.org/packages/13/5d/61a533ccb8c231b474ac8e3a7d70155b00dfc61af6cafdccd1947df6d735/regex-2024.11.6-cp39-cp39-win32.whl", hash = "sha256:41758407fc32d5c3c5de163888068cfee69cb4c2be844e7ac517a52770f9af57", size = 261756 },
    { url = "https://files.pythonhosted.org/packages/dc/7b/e59b7f7c91ae110d154370c24133f947262525b5d6406df65f23422acc17/regex-2024.11.6-cp39-cp39-win_amd64.whl", hash = "sha256:b2837718570f95dd41675328e111345f9b7095d821bac435aac173ac80b19983", size = 274110 },
]

[[package]]
name = "requests"
version = "2.32.3"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "certifi" },
    { name = "charset-normalizer" },
    { name = "idna" },
    { name = "urllib3" },
]
sdist = { url = "https://files.pythonhosted.org/packages/63/70/2bf7780ad2d390a8d301ad0b550f1581eadbd9a20f896afe06353c2a2913/requests-2.32.3.tar.gz", hash = "sha256:55365417734eb18255590a9ff9eb97e9e1da868d4ccd6402399eaf68af20a760", size = 131218 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/f9/9b/335f9764261e915ed497fcdeb11df5dfd6f7bf257d4a6a2a686d80da4d54/requests-2.32.3-py3-none-any.whl", hash = "sha256:70761cfe03c773ceb22aa2f671b4757976145175cdfca038c02654d061d6dcc6", size = 64928 },
]

[[package]]
name = "rich"
version = "14.0.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "markdown-it-py" },
    { name = "pygments" },
    { name = "typing-extensions", marker = "python_full_version < '3.11'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/a1/53/830aa4c3066a8ab0ae9a9955976fb770fe9c6102117c8ec4ab3ea62d89e8/rich-14.0.0.tar.gz", hash = "sha256:82f1bc23a6a21ebca4ae0c45af9bdbc492ed20231dcb63f297d6d1021a9d5725", size = 224078 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/0d/9b/63f4c7ebc259242c89b3acafdb37b41d1185c07ff0011164674e9076b491/rich-14.0.0-py3-none-any.whl", hash = "sha256:1c9491e1951aac09caffd42f448ee3d04e58923ffe14993f6e83068dc395d7e0", size = 243229 },
]

[[package]]
name = "ruff"
version = "0.11.4"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/e8/5b/3ae20f89777115944e89c2d8c2e795dcc5b9e04052f76d5347e35e0da66e/ruff-0.11.4.tar.gz", hash = "sha256:f45bd2fb1a56a5a85fae3b95add03fb185a0b30cf47f5edc92aa0355ca1d7407", size = 3933063 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/9c/db/baee59ac88f57527fcbaad3a7b309994e42329c6bc4d4d2b681a3d7b5426/ruff-0.11.4-py3-none-linux_armv6l.whl", hash = "sha256:d9f4a761ecbde448a2d3e12fb398647c7f0bf526dbc354a643ec505965824ed2", size = 10106493 },
    { url = "https://files.pythonhosted.org/packages/c1/d6/9a0962cbb347f4ff98b33d699bf1193ff04ca93bed4b4222fd881b502154/ruff-0.11.4-py3-none-macosx_10_12_x86_64.whl", hash = "sha256:8c1747d903447d45ca3d40c794d1a56458c51e5cc1bc77b7b64bd2cf0b1626cc", size = 10876382 },
    { url = "https://files.pythonhosted.org/packages/3a/8f/62bab0c7d7e1ae3707b69b157701b41c1ccab8f83e8501734d12ea8a839f/ruff-0.11.4-py3-none-macosx_11_0_arm64.whl", hash = "sha256:51a6494209cacca79e121e9b244dc30d3414dac8cc5afb93f852173a2ecfc906", size = 10237050 },
    { url = "https://files.pythonhosted.org/packages/09/96/e296965ae9705af19c265d4d441958ed65c0c58fc4ec340c27cc9d2a1f5b/ruff-0.11.4-py3-none-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:3f171605f65f4fc49c87f41b456e882cd0c89e4ac9d58e149a2b07930e1d466f", size = 10424984 },
    { url = "https://files.pythonhosted.org/packages/e5/56/644595eb57d855afed6e54b852e2df8cd5ca94c78043b2f29bdfb29882d5/ruff-0.11.4-py3-none-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:ebf99ea9af918878e6ce42098981fc8c1db3850fef2f1ada69fb1dcdb0f8e79e", size = 9957438 },
    { url = "https://files.pythonhosted.org/packages/86/83/9d3f3bed0118aef3e871ded9e5687fb8c5776bde233427fd9ce0a45db2d4/ruff-0.11.4-py3-none-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:edad2eac42279df12e176564a23fc6f4aaeeb09abba840627780b1bb11a9d223", size = 11547282 },
    { url = "https://files.pythonhosted.org/packages/40/e6/0c6e4f5ae72fac5ccb44d72c0111f294a5c2c8cc5024afcb38e6bda5f4b3/ruff-0.11.4-py3-none-manylinux_2_17_ppc64.manylinux2014_ppc64.whl", hash = "sha256:f103a848be9ff379fc19b5d656c1f911d0a0b4e3e0424f9532ececf319a4296e", size = 12182020 },
    { url = "https://files.pythonhosted.org/packages/b5/92/4aed0e460aeb1df5ea0c2fbe8d04f9725cccdb25d8da09a0d3f5b8764bf8/ruff-0.11.4-py3-none-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:193e6fac6eb60cc97b9f728e953c21cc38a20077ed64f912e9d62b97487f3f2d", size = 11679154 },
    { url = "https://files.pythonhosted.org/packages/1b/d3/7316aa2609f2c592038e2543483eafbc62a0e1a6a6965178e284808c095c/ruff-0.11.4-py3-none-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:7af4e5f69b7c138be8dcffa5b4a061bf6ba6a3301f632a6bce25d45daff9bc99", size = 13905985 },
    { url = "https://files.pythonhosted.org/packages/63/80/734d3d17546e47ff99871f44ea7540ad2bbd7a480ed197fe8a1c8a261075/ruff-0.11.4-py3-none-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:126b1bf13154aa18ae2d6c3c5efe144ec14b97c60844cfa6eb960c2a05188222", size = 11348343 },
    { url = "https://files.pythonhosted.org/packages/04/7b/70fc7f09a0161dce9613a4671d198f609e653d6f4ff9eee14d64c4c240fb/ruff-0.11.4-py3-none-musllinux_1_2_aarch64.whl", hash = "sha256:e8806daaf9dfa881a0ed603f8a0e364e4f11b6ed461b56cae2b1c0cab0645304", size = 10308487 },
    { url = "https://files.pythonhosted.org/packages/1a/22/1cdd62dabd678d75842bf4944fd889cf794dc9e58c18cc547f9eb28f95ed/ruff-0.11.4-py3-none-musllinux_1_2_armv7l.whl", hash = "sha256:5d94bb1cc2fc94a769b0eb975344f1b1f3d294da1da9ddbb5a77665feb3a3019", size = 9929091 },
    { url = "https://files.pythonhosted.org/packages/9f/20/40e0563506332313148e783bbc1e4276d657962cc370657b2fff20e6e058/ruff-0.11.4-py3-none-musllinux_1_2_i686.whl", hash = "sha256:995071203d0fe2183fc7a268766fd7603afb9996785f086b0d76edee8755c896", size = 10924659 },
    { url = "https://files.pythonhosted.org/packages/b5/41/eef9b7aac8819d9e942f617f9db296f13d2c4576806d604aba8db5a753f1/ruff-0.11.4-py3-none-musllinux_1_2_x86_64.whl", hash = "sha256:7a37ca937e307ea18156e775a6ac6e02f34b99e8c23fe63c1996185a4efe0751", size = 11428160 },
    { url = "https://files.pythonhosted.org/packages/ff/61/c488943414fb2b8754c02f3879de003e26efdd20f38167ded3fb3fc1cda3/ruff-0.11.4-py3-none-win32.whl", hash = "sha256:0e9365a7dff9b93af933dab8aebce53b72d8f815e131796268709890b4a83270", size = 10311496 },
    { url = "https://files.pythonhosted.org/packages/b6/2b/2a1c8deb5f5dfa3871eb7daa41492c4d2b2824a74d2b38e788617612a66d/ruff-0.11.4-py3-none-win_amd64.whl", hash = "sha256:5a9fa1c69c7815e39fcfb3646bbfd7f528fa8e2d4bebdcf4c2bd0fa037a255fb", size = 11399146 },
    { url = "https://files.pythonhosted.org/packages/4f/03/3aec4846226d54a37822e4c7ea39489e4abd6f88388fba74e3d4abe77300/ruff-0.11.4-py3-none-win_arm64.whl", hash = "sha256:d435db6b9b93d02934cf61ef332e66af82da6d8c69aefdea5994c89997c7a0fc", size = 10450306 },
]

[[package]]
name = "safetensors"
version = "0.5.3"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/71/7e/2d5d6ee7b40c0682315367ec7475693d110f512922d582fef1bd4a63adc3/safetensors-0.5.3.tar.gz", hash = "sha256:b6b0d6ecacec39a4fdd99cc19f4576f5219ce858e6fd8dbe7609df0b8dc56965", size = 67210 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/18/ae/88f6c49dbd0cc4da0e08610019a3c78a7d390879a919411a410a1876d03a/safetensors-0.5.3-cp38-abi3-macosx_10_12_x86_64.whl", hash = "sha256:bd20eb133db8ed15b40110b7c00c6df51655a2998132193de2f75f72d99c7073", size = 436917 },
    { url = "https://files.pythonhosted.org/packages/b8/3b/11f1b4a2f5d2ab7da34ecc062b0bc301f2be024d110a6466726bec8c055c/safetensors-0.5.3-cp38-abi3-macosx_11_0_arm64.whl", hash = "sha256:21d01c14ff6c415c485616b8b0bf961c46b3b343ca59110d38d744e577f9cce7", size = 418419 },
    { url = "https://files.pythonhosted.org/packages/5d/9a/add3e6fef267658075c5a41573c26d42d80c935cdc992384dfae435feaef/safetensors-0.5.3-cp38-abi3-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:11bce6164887cd491ca75c2326a113ba934be596e22b28b1742ce27b1d076467", size = 459493 },
    { url = "https://files.pythonhosted.org/packages/df/5c/bf2cae92222513cc23b3ff85c4a1bb2811a2c3583ac0f8e8d502751de934/safetensors-0.5.3-cp38-abi3-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:4a243be3590bc3301c821da7a18d87224ef35cbd3e5f5727e4e0728b8172411e", size = 472400 },
    { url = "https://files.pythonhosted.org/packages/58/11/7456afb740bd45782d0f4c8e8e1bb9e572f1bf82899fb6ace58af47b4282/safetensors-0.5.3-cp38-abi3-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:8bd84b12b1670a6f8e50f01e28156422a2bc07fb16fc4e98bded13039d688a0d", size = 522891 },
    { url = "https://files.pythonhosted.org/packages/57/3d/fe73a9d2ace487e7285f6e157afee2383bd1ddb911b7cb44a55cf812eae3/safetensors-0.5.3-cp38-abi3-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:391ac8cab7c829452175f871fcaf414aa1e292b5448bd02620f675a7f3e7abb9", size = 537694 },
    { url = "https://files.pythonhosted.org/packages/a6/f8/dae3421624fcc87a89d42e1898a798bc7ff72c61f38973a65d60df8f124c/safetensors-0.5.3-cp38-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:cead1fa41fc54b1e61089fa57452e8834f798cb1dc7a09ba3524f1eb08e0317a", size = 471642 },
    { url = "https://files.pythonhosted.org/packages/ce/20/1fbe16f9b815f6c5a672f5b760951e20e17e43f67f231428f871909a37f6/safetensors-0.5.3-cp38-abi3-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:1077f3e94182d72618357b04b5ced540ceb71c8a813d3319f1aba448e68a770d", size = 502241 },
    { url = "https://files.pythonhosted.org/packages/5f/18/8e108846b506487aa4629fe4116b27db65c3dde922de2c8e0cc1133f3f29/safetensors-0.5.3-cp38-abi3-musllinux_1_2_aarch64.whl", hash = "sha256:799021e78287bac619c7b3f3606730a22da4cda27759ddf55d37c8db7511c74b", size = 638001 },
    { url = "https://files.pythonhosted.org/packages/82/5a/c116111d8291af6c8c8a8b40628fe833b9db97d8141c2a82359d14d9e078/safetensors-0.5.3-cp38-abi3-musllinux_1_2_armv7l.whl", hash = "sha256:df26da01aaac504334644e1b7642fa000bfec820e7cef83aeac4e355e03195ff", size = 734013 },
    { url = "https://files.pythonhosted.org/packages/7d/ff/41fcc4d3b7de837963622e8610d998710705bbde9a8a17221d85e5d0baad/safetensors-0.5.3-cp38-abi3-musllinux_1_2_i686.whl", hash = "sha256:32c3ef2d7af8b9f52ff685ed0bc43913cdcde135089ae322ee576de93eae5135", size = 670687 },
    { url = "https://files.pythonhosted.org/packages/40/ad/2b113098e69c985a3d8fbda4b902778eae4a35b7d5188859b4a63d30c161/safetensors-0.5.3-cp38-abi3-musllinux_1_2_x86_64.whl", hash = "sha256:37f1521be045e56fc2b54c606d4455573e717b2d887c579ee1dbba5f868ece04", size = 643147 },
    { url = "https://files.pythonhosted.org/packages/0a/0c/95aeb51d4246bd9a3242d3d8349c1112b4ee7611a4b40f0c5c93b05f001d/safetensors-0.5.3-cp38-abi3-win32.whl", hash = "sha256:cfc0ec0846dcf6763b0ed3d1846ff36008c6e7290683b61616c4b040f6a54ace", size = 296677 },
    { url = "https://files.pythonhosted.org/packages/69/e2/b011c38e5394c4c18fb5500778a55ec43ad6106126e74723ffaee246f56e/safetensors-0.5.3-cp38-abi3-win_amd64.whl", hash = "sha256:836cbbc320b47e80acd40e44c8682db0e8ad7123209f69b093def21ec7cafd11", size = 308878 },
]

[[package]]
name = "scikit-learn"
version = "1.6.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "joblib" },
    { name = "numpy" },
    { name = "scipy" },
    { name = "threadpoolctl" },
]
sdist = { url = "https://files.pythonhosted.org/packages/9e/a5/4ae3b3a0755f7b35a280ac90b28817d1f380318973cff14075ab41ef50d9/scikit_learn-1.6.1.tar.gz", hash = "sha256:b4fc2525eca2c69a59260f583c56a7557c6ccdf8deafdba6e060f94c1c59738e", size = 7068312 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/2e/3a/f4597eb41049110b21ebcbb0bcb43e4035017545daa5eedcfeb45c08b9c5/scikit_learn-1.6.1-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:d056391530ccd1e501056160e3c9673b4da4805eb67eb2bdf4e983e1f9c9204e", size = 12067702 },
    { url = "https://files.pythonhosted.org/packages/37/19/0423e5e1fd1c6ec5be2352ba05a537a473c1677f8188b9306097d684b327/scikit_learn-1.6.1-cp310-cp310-macosx_12_0_arm64.whl", hash = "sha256:0c8d036eb937dbb568c6242fa598d551d88fb4399c0344d95c001980ec1c7d36", size = 11112765 },
    { url = "https://files.pythonhosted.org/packages/70/95/d5cb2297a835b0f5fc9a77042b0a2d029866379091ab8b3f52cc62277808/scikit_learn-1.6.1-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:8634c4bd21a2a813e0a7e3900464e6d593162a29dd35d25bdf0103b3fce60ed5", size = 12643991 },
    { url = "https://files.pythonhosted.org/packages/b7/91/ab3c697188f224d658969f678be86b0968ccc52774c8ab4a86a07be13c25/scikit_learn-1.6.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:775da975a471c4f6f467725dff0ced5c7ac7bda5e9316b260225b48475279a1b", size = 13497182 },
    { url = "https://files.pythonhosted.org/packages/17/04/d5d556b6c88886c092cc989433b2bab62488e0f0dafe616a1d5c9cb0efb1/scikit_learn-1.6.1-cp310-cp310-win_amd64.whl", hash = "sha256:8a600c31592bd7dab31e1c61b9bbd6dea1b3433e67d264d17ce1017dbdce8002", size = 11125517 },
    { url = "https://files.pythonhosted.org/packages/6c/2a/e291c29670795406a824567d1dfc91db7b699799a002fdaa452bceea8f6e/scikit_learn-1.6.1-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:72abc587c75234935e97d09aa4913a82f7b03ee0b74111dcc2881cba3c5a7b33", size = 12102620 },
    { url = "https://files.pythonhosted.org/packages/25/92/ee1d7a00bb6b8c55755d4984fd82608603a3cc59959245068ce32e7fb808/scikit_learn-1.6.1-cp311-cp311-macosx_12_0_arm64.whl", hash = "sha256:b3b00cdc8f1317b5f33191df1386c0befd16625f49d979fe77a8d44cae82410d", size = 11116234 },
    { url = "https://files.pythonhosted.org/packages/30/cd/ed4399485ef364bb25f388ab438e3724e60dc218c547a407b6e90ccccaef/scikit_learn-1.6.1-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:dc4765af3386811c3ca21638f63b9cf5ecf66261cc4815c1db3f1e7dc7b79db2", size = 12592155 },
    { url = "https://files.pythonhosted.org/packages/a8/f3/62fc9a5a659bb58a03cdd7e258956a5824bdc9b4bb3c5d932f55880be569/scikit_learn-1.6.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:25fc636bdaf1cc2f4a124a116312d837148b5e10872147bdaf4887926b8c03d8", size = 13497069 },
    { url = "https://files.pythonhosted.org/packages/a1/a6/c5b78606743a1f28eae8f11973de6613a5ee87366796583fb74c67d54939/scikit_learn-1.6.1-cp311-cp311-win_amd64.whl", hash = "sha256:fa909b1a36e000a03c382aade0bd2063fd5680ff8b8e501660c0f59f021a6415", size = 11139809 },
    { url = "https://files.pythonhosted.org/packages/0a/18/c797c9b8c10380d05616db3bfb48e2a3358c767affd0857d56c2eb501caa/scikit_learn-1.6.1-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:926f207c804104677af4857b2c609940b743d04c4c35ce0ddc8ff4f053cddc1b", size = 12104516 },
    { url = "https://files.pythonhosted.org/packages/c4/b7/2e35f8e289ab70108f8cbb2e7a2208f0575dc704749721286519dcf35f6f/scikit_learn-1.6.1-cp312-cp312-macosx_12_0_arm64.whl", hash = "sha256:2c2cae262064e6a9b77eee1c8e768fc46aa0b8338c6a8297b9b6759720ec0ff2", size = 11167837 },
    { url = "https://files.pythonhosted.org/packages/a4/f6/ff7beaeb644bcad72bcfd5a03ff36d32ee4e53a8b29a639f11bcb65d06cd/scikit_learn-1.6.1-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:1061b7c028a8663fb9a1a1baf9317b64a257fcb036dae5c8752b2abef31d136f", size = 12253728 },
    { url = "https://files.pythonhosted.org/packages/29/7a/8bce8968883e9465de20be15542f4c7e221952441727c4dad24d534c6d99/scikit_learn-1.6.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:2e69fab4ebfc9c9b580a7a80111b43d214ab06250f8a7ef590a4edf72464dd86", size = 13147700 },
    { url = "https://files.pythonhosted.org/packages/62/27/585859e72e117fe861c2079bcba35591a84f801e21bc1ab85bce6ce60305/scikit_learn-1.6.1-cp312-cp312-win_amd64.whl", hash = "sha256:70b1d7e85b1c96383f872a519b3375f92f14731e279a7b4c6cfd650cf5dffc52", size = 11110613 },
    { url = "https://files.pythonhosted.org/packages/2e/59/8eb1872ca87009bdcdb7f3cdc679ad557b992c12f4b61f9250659e592c63/scikit_learn-1.6.1-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:2ffa1e9e25b3d93990e74a4be2c2fc61ee5af85811562f1288d5d055880c4322", size = 12010001 },
    { url = "https://files.pythonhosted.org/packages/9d/05/f2fc4effc5b32e525408524c982c468c29d22f828834f0625c5ef3d601be/scikit_learn-1.6.1-cp313-cp313-macosx_12_0_arm64.whl", hash = "sha256:dc5cf3d68c5a20ad6d571584c0750ec641cc46aeef1c1507be51300e6003a7e1", size = 11096360 },
    { url = "https://files.pythonhosted.org/packages/c8/e4/4195d52cf4f113573fb8ebc44ed5a81bd511a92c0228889125fac2f4c3d1/scikit_learn-1.6.1-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:c06beb2e839ecc641366000ca84f3cf6fa9faa1777e29cf0c04be6e4d096a348", size = 12209004 },
    { url = "https://files.pythonhosted.org/packages/94/be/47e16cdd1e7fcf97d95b3cb08bde1abb13e627861af427a3651fcb80b517/scikit_learn-1.6.1-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:e8ca8cb270fee8f1f76fa9bfd5c3507d60c6438bbee5687f81042e2bb98e5a97", size = 13171776 },
    { url = "https://files.pythonhosted.org/packages/34/b0/ca92b90859070a1487827dbc672f998da95ce83edce1270fc23f96f1f61a/scikit_learn-1.6.1-cp313-cp313-win_amd64.whl", hash = "sha256:7a1c43c8ec9fde528d664d947dc4c0789be4077a3647f232869f41d9bf50e0fb", size = 11071865 },
    { url = "https://files.pythonhosted.org/packages/12/ae/993b0fb24a356e71e9a894e42b8a9eec528d4c70217353a1cd7a48bc25d4/scikit_learn-1.6.1-cp313-cp313t-macosx_10_13_x86_64.whl", hash = "sha256:a17c1dea1d56dcda2fac315712f3651a1fea86565b64b48fa1bc090249cbf236", size = 11955804 },
    { url = "https://files.pythonhosted.org/packages/d6/54/32fa2ee591af44507eac86406fa6bba968d1eb22831494470d0a2e4a1eb1/scikit_learn-1.6.1-cp313-cp313t-macosx_12_0_arm64.whl", hash = "sha256:6a7aa5f9908f0f28f4edaa6963c0a6183f1911e63a69aa03782f0d924c830a35", size = 11100530 },
    { url = "https://files.pythonhosted.org/packages/3f/58/55856da1adec655bdce77b502e94a267bf40a8c0b89f8622837f89503b5a/scikit_learn-1.6.1-cp313-cp313t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:0650e730afb87402baa88afbf31c07b84c98272622aaba002559b614600ca691", size = 12433852 },
    { url = "https://files.pythonhosted.org/packages/ff/4f/c83853af13901a574f8f13b645467285a48940f185b690936bb700a50863/scikit_learn-1.6.1-cp313-cp313t-win_amd64.whl", hash = "sha256:3f59fe08dc03ea158605170eb52b22a105f238a5d512c4470ddeca71feae8e5f", size = 11337256 },
    { url = "https://files.pythonhosted.org/packages/d2/37/b305b759cc65829fe1b8853ff3e308b12cdd9d8884aa27840835560f2b42/scikit_learn-1.6.1-cp39-cp39-macosx_10_9_x86_64.whl", hash = "sha256:6849dd3234e87f55dce1db34c89a810b489ead832aaf4d4550b7ea85628be6c1", size = 12101868 },
    { url = "https://files.pythonhosted.org/packages/83/74/f64379a4ed5879d9db744fe37cfe1978c07c66684d2439c3060d19a536d8/scikit_learn-1.6.1-cp39-cp39-macosx_12_0_arm64.whl", hash = "sha256:e7be3fa5d2eb9be7d77c3734ff1d599151bb523674be9b834e8da6abe132f44e", size = 11144062 },
    { url = "https://files.pythonhosted.org/packages/fd/dc/d5457e03dc9c971ce2b0d750e33148dd060fefb8b7dc71acd6054e4bb51b/scikit_learn-1.6.1-cp39-cp39-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:44a17798172df1d3c1065e8fcf9019183f06c87609b49a124ebdf57ae6cb0107", size = 12693173 },
    { url = "https://files.pythonhosted.org/packages/79/35/b1d2188967c3204c78fa79c9263668cf1b98060e8e58d1a730fe5b2317bb/scikit_learn-1.6.1-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:b8b7a3b86e411e4bce21186e1c180d792f3d99223dcfa3b4f597ecc92fa1a422", size = 13518605 },
    { url = "https://files.pythonhosted.org/packages/fb/d8/8d603bdd26601f4b07e2363032b8565ab82eb857f93d86d0f7956fcf4523/scikit_learn-1.6.1-cp39-cp39-win_amd64.whl", hash = "sha256:7a73d457070e3318e32bdb3aa79a8d990474f19035464dfd8bede2883ab5dc3b", size = 11155078 },
]

[[package]]
name = "scipy"
version = "1.13.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "numpy" },
]
sdist = { url = "https://files.pythonhosted.org/packages/ae/00/48c2f661e2816ccf2ecd77982f6605b2950afe60f60a52b4cbbc2504aa8f/scipy-1.13.1.tar.gz", hash = "sha256:095a87a0312b08dfd6a6155cbbd310a8c51800fc931b8c0b84003014b874ed3c", size = 57210720 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/33/59/41b2529908c002ade869623b87eecff3e11e3ce62e996d0bdcb536984187/scipy-1.13.1-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:20335853b85e9a49ff7572ab453794298bcf0354d8068c5f6775a0eabf350aca", size = 39328076 },
    { url = "https://files.pythonhosted.org/packages/d5/33/f1307601f492f764062ce7dd471a14750f3360e33cd0f8c614dae208492c/scipy-1.13.1-cp310-cp310-macosx_12_0_arm64.whl", hash = "sha256:d605e9c23906d1994f55ace80e0125c587f96c020037ea6aa98d01b4bd2e222f", size = 30306232 },
    { url = "https://files.pythonhosted.org/packages/c0/66/9cd4f501dd5ea03e4a4572ecd874936d0da296bd04d1c45ae1a4a75d9c3a/scipy-1.13.1-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:cfa31f1def5c819b19ecc3a8b52d28ffdcc7ed52bb20c9a7589669dd3c250989", size = 33743202 },
    { url = "https://files.pythonhosted.org/packages/a3/ba/7255e5dc82a65adbe83771c72f384d99c43063648456796436c9a5585ec3/scipy-1.13.1-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:f26264b282b9da0952a024ae34710c2aff7d27480ee91a2e82b7b7073c24722f", size = 38577335 },
    { url = "https://files.pythonhosted.org/packages/49/a5/bb9ded8326e9f0cdfdc412eeda1054b914dfea952bda2097d174f8832cc0/scipy-1.13.1-cp310-cp310-musllinux_1_1_x86_64.whl", hash = "sha256:eccfa1906eacc02de42d70ef4aecea45415f5be17e72b61bafcfd329bdc52e94", size = 38820728 },
    { url = "https://files.pythonhosted.org/packages/12/30/df7a8fcc08f9b4a83f5f27cfaaa7d43f9a2d2ad0b6562cced433e5b04e31/scipy-1.13.1-cp310-cp310-win_amd64.whl", hash = "sha256:2831f0dc9c5ea9edd6e51e6e769b655f08ec6db6e2e10f86ef39bd32eb11da54", size = 46210588 },
    { url = "https://files.pythonhosted.org/packages/b4/15/4a4bb1b15bbd2cd2786c4f46e76b871b28799b67891f23f455323a0cdcfb/scipy-1.13.1-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:27e52b09c0d3a1d5b63e1105f24177e544a222b43611aaf5bc44d4a0979e32f9", size = 39333805 },
    { url = "https://files.pythonhosted.org/packages/ba/92/42476de1af309c27710004f5cdebc27bec62c204db42e05b23a302cb0c9a/scipy-1.13.1-cp311-cp311-macosx_12_0_arm64.whl", hash = "sha256:54f430b00f0133e2224c3ba42b805bfd0086fe488835effa33fa291561932326", size = 30317687 },
    { url = "https://files.pythonhosted.org/packages/80/ba/8be64fe225360a4beb6840f3cbee494c107c0887f33350d0a47d55400b01/scipy-1.13.1-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:e89369d27f9e7b0884ae559a3a956e77c02114cc60a6058b4e5011572eea9299", size = 33694638 },
    { url = "https://files.pythonhosted.org/packages/36/07/035d22ff9795129c5a847c64cb43c1fa9188826b59344fee28a3ab02e283/scipy-1.13.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:a78b4b3345f1b6f68a763c6e25c0c9a23a9fd0f39f5f3d200efe8feda560a5fa", size = 38569931 },
    { url = "https://files.pythonhosted.org/packages/d9/10/f9b43de37e5ed91facc0cfff31d45ed0104f359e4f9a68416cbf4e790241/scipy-1.13.1-cp311-cp311-musllinux_1_1_x86_64.whl", hash = "sha256:45484bee6d65633752c490404513b9ef02475b4284c4cfab0ef946def50b3f59", size = 38838145 },
    { url = "https://files.pythonhosted.org/packages/4a/48/4513a1a5623a23e95f94abd675ed91cfb19989c58e9f6f7d03990f6caf3d/scipy-1.13.1-cp311-cp311-win_amd64.whl", hash = "sha256:5713f62f781eebd8d597eb3f88b8bf9274e79eeabf63afb4a737abc6c84ad37b", size = 46196227 },
    { url = "https://files.pythonhosted.org/packages/f2/7b/fb6b46fbee30fc7051913068758414f2721003a89dd9a707ad49174e3843/scipy-1.13.1-cp312-cp312-macosx_10_9_x86_64.whl", hash = "sha256:5d72782f39716b2b3509cd7c33cdc08c96f2f4d2b06d51e52fb45a19ca0c86a1", size = 39357301 },
    { url = "https://files.pythonhosted.org/packages/dc/5a/2043a3bde1443d94014aaa41e0b50c39d046dda8360abd3b2a1d3f79907d/scipy-1.13.1-cp312-cp312-macosx_12_0_arm64.whl", hash = "sha256:017367484ce5498445aade74b1d5ab377acdc65e27095155e448c88497755a5d", size = 30363348 },
    { url = "https://files.pythonhosted.org/packages/e7/cb/26e4a47364bbfdb3b7fb3363be6d8a1c543bcd70a7753ab397350f5f189a/scipy-1.13.1-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:949ae67db5fa78a86e8fa644b9a6b07252f449dcf74247108c50e1d20d2b4627", size = 33406062 },
    { url = "https://files.pythonhosted.org/packages/88/ab/6ecdc526d509d33814835447bbbeedbebdec7cca46ef495a61b00a35b4bf/scipy-1.13.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:de3ade0e53bc1f21358aa74ff4830235d716211d7d077e340c7349bc3542e884", size = 38218311 },
    { url = "https://files.pythonhosted.org/packages/0b/00/9f54554f0f8318100a71515122d8f4f503b1a2c4b4cfab3b4b68c0eb08fa/scipy-1.13.1-cp312-cp312-musllinux_1_1_x86_64.whl", hash = "sha256:2ac65fb503dad64218c228e2dc2d0a0193f7904747db43014645ae139c8fad16", size = 38442493 },
    { url = "https://files.pythonhosted.org/packages/3e/df/963384e90733e08eac978cd103c34df181d1fec424de383cdc443f418dd4/scipy-1.13.1-cp312-cp312-win_amd64.whl", hash = "sha256:cdd7dacfb95fea358916410ec61bbc20440f7860333aee6d882bb8046264e949", size = 45910955 },
    { url = "https://files.pythonhosted.org/packages/7f/29/c2ea58c9731b9ecb30b6738113a95d147e83922986b34c685b8f6eefde21/scipy-1.13.1-cp39-cp39-macosx_10_9_x86_64.whl", hash = "sha256:436bbb42a94a8aeef855d755ce5a465479c721e9d684de76bf61a62e7c2b81d5", size = 39352927 },
    { url = "https://files.pythonhosted.org/packages/5c/c0/e71b94b20ccf9effb38d7147c0064c08c622309fd487b1b677771a97d18c/scipy-1.13.1-cp39-cp39-macosx_12_0_arm64.whl", hash = "sha256:8335549ebbca860c52bf3d02f80784e91a004b71b059e3eea9678ba994796a24", size = 30324538 },
    { url = "https://files.pythonhosted.org/packages/6d/0f/aaa55b06d474817cea311e7b10aab2ea1fd5d43bc6a2861ccc9caec9f418/scipy-1.13.1-cp39-cp39-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:d533654b7d221a6a97304ab63c41c96473ff04459e404b83275b60aa8f4b7004", size = 33732190 },
    { url = "https://files.pythonhosted.org/packages/35/f5/d0ad1a96f80962ba65e2ce1de6a1e59edecd1f0a7b55990ed208848012e0/scipy-1.13.1-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:637e98dcf185ba7f8e663e122ebf908c4702420477ae52a04f9908707456ba4d", size = 38612244 },
    { url = "https://files.pythonhosted.org/packages/8d/02/1165905f14962174e6569076bcc3315809ae1291ed14de6448cc151eedfd/scipy-1.13.1-cp39-cp39-musllinux_1_1_x86_64.whl", hash = "sha256:a014c2b3697bde71724244f63de2476925596c24285c7a637364761f8710891c", size = 38845637 },
    { url = "https://files.pythonhosted.org/packages/3e/77/dab54fe647a08ee4253963bcd8f9cf17509c8ca64d6335141422fe2e2114/scipy-1.13.1-cp39-cp39-win_amd64.whl", hash = "sha256:392e4ec766654852c25ebad4f64e4e584cf19820b980bc04960bca0b0cd6eaa2", size = 46227440 },
]

[[package]]
name = "sentence-transformers"
version = "4.0.2"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "huggingface-hub" },
    { name = "pillow" },
    { name = "scikit-learn" },
    { name = "scipy" },
    { name = "torch" },
    { name = "tqdm" },
    { name = "transformers" },
    { name = "typing-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/3c/74/606783c6b2e80a609af25d2c487bbe32eb8f0970b0f7519fbb1a099f3ab8/sentence_transformers-4.0.2.tar.gz", hash = "sha256:d33d0c5a69ae0d682115c90e74fc1dc24c4786aeea78e26f5889b037e5921880", size = 267724 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/32/58/770e1e762893abbfe3cd048f1ed1ea6e00122a195651ea98fb27f55ad17a/sentence_transformers-4.0.2-py3-none-any.whl", hash = "sha256:25f5086d0746c22177f9fb7d431f3eebe6375f3afe1dc7c341c4ca9061e98771", size = 340618 },
]

[[package]]
name = "setuptools"
version = "78.1.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/a9/5a/0db4da3bc908df06e5efae42b44e75c81dd52716e10192ff36d0c1c8e379/setuptools-78.1.0.tar.gz", hash = "sha256:18fd474d4a82a5f83dac888df697af65afa82dec7323d09c3e37d1f14288da54", size = 1367827 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/54/21/f43f0a1fa8b06b32812e0975981f4677d28e0f3271601dc88ac5a5b83220/setuptools-78.1.0-py3-none-any.whl", hash = "sha256:3e386e96793c8702ae83d17b853fb93d3e09ef82ec62722e61da5cd22376dcd8", size = 1256108 },
]

[[package]]
name = "six"
version = "1.17.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/94/e7/b2c673351809dca68a0e064b6af791aa332cf192da575fd474ed7d6f16a2/six-1.17.0.tar.gz", hash = "sha256:ff70335d468e7eb6ec65b95b99d3a2836546063f63acc5171de367e834932a81", size = 34031 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/b7/ce/149a00dd41f10bc29e5921b496af8b574d8413afcd5e30dfa0ed46c2cc5e/six-1.17.0-py2.py3-none-any.whl", hash = "sha256:4721f391ed90541fddacab5acf947aa0d3dc7d27b2e1e8eda2be8970586c3274", size = 11050 },
]

[[package]]
name = "sniffio"
version = "1.3.1"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/a2/87/a6771e1546d97e7e041b6ae58d80074f81b7d5121207425c964ddf5cfdbd/sniffio-1.3.1.tar.gz", hash = "sha256:f4324edc670a0f49750a81b895f35c3adb843cca46f0530f79fc1babb23789dc", size = 20372 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/e9/44/75a9c9421471a6c4805dbf2356f7c181a29c1879239abab1ea2cc8f38b40/sniffio-1.3.1-py3-none-any.whl", hash = "sha256:2f6da418d1f1e0fddd844478f41680e794e6051915791a034ff65e5f100525a2", size = 10235 },
]

[[package]]
name = "sympy"
version = "1.13.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "mpmath" },
]
sdist = { url = "https://files.pythonhosted.org/packages/ca/99/5a5b6f19ff9f083671ddf7b9632028436167cd3d33e11015754e41b249a4/sympy-1.13.1.tar.gz", hash = "sha256:9cebf7e04ff162015ce31c9c6c9144daa34a93bd082f54fd8f12deca4f47515f", size = 7533040 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/b2/fe/81695a1aa331a842b582453b605175f419fe8540355886031328089d840a/sympy-1.13.1-py3-none-any.whl", hash = "sha256:db36cdc64bf61b9b24578b6f7bab1ecdd2452cf008f34faa33776680c26d66f8", size = 6189177 },
]

[[package]]
name = "threadpoolctl"
version = "3.6.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/b7/4d/08c89e34946fce2aec4fbb45c9016efd5f4d7f24af8e5d93296e935631d8/threadpoolctl-3.6.0.tar.gz", hash = "sha256:8ab8b4aa3491d812b623328249fab5302a68d2d71745c8a4c719a2fcaba9f44e", size = 21274 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/32/d5/f9a850d79b0851d1d4ef6456097579a9005b31fea68726a4ae5f2d82ddd9/threadpoolctl-3.6.0-py3-none-any.whl", hash = "sha256:43a0b8fd5a2928500110039e43a5eed8480b918967083ea48dc3ab9f13c4a7fb", size = 18638 },
]

[[package]]
name = "tiktoken"
version = "0.9.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "regex" },
    { name = "requests" },
]
sdist = { url = "https://files.pythonhosted.org/packages/ea/cf/756fedf6981e82897f2d570dd25fa597eb3f4459068ae0572d7e888cfd6f/tiktoken-0.9.0.tar.gz", hash = "sha256:d02a5ca6a938e0490e1ff957bc48c8b078c88cb83977be1625b1fd8aac792c5d", size = 35991 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/64/f3/50ec5709fad61641e4411eb1b9ac55b99801d71f1993c29853f256c726c9/tiktoken-0.9.0-cp310-cp310-macosx_10_12_x86_64.whl", hash = "sha256:586c16358138b96ea804c034b8acf3f5d3f0258bd2bc3b0227af4af5d622e382", size = 1065770 },
    { url = "https://files.pythonhosted.org/packages/d6/f8/5a9560a422cf1755b6e0a9a436e14090eeb878d8ec0f80e0cd3d45b78bf4/tiktoken-0.9.0-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:d9c59ccc528c6c5dd51820b3474402f69d9a9e1d656226848ad68a8d5b2e5108", size = 1009314 },
    { url = "https://files.pythonhosted.org/packages/bc/20/3ed4cfff8f809cb902900ae686069e029db74567ee10d017cb254df1d598/tiktoken-0.9.0-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:f0968d5beeafbca2a72c595e8385a1a1f8af58feaebb02b227229b69ca5357fd", size = 1143140 },
    { url = "https://files.pythonhosted.org/packages/f1/95/cc2c6d79df8f113bdc6c99cdec985a878768120d87d839a34da4bd3ff90a/tiktoken-0.9.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:92a5fb085a6a3b7350b8fc838baf493317ca0e17bd95e8642f95fc69ecfed1de", size = 1197860 },
    { url = "https://files.pythonhosted.org/packages/c7/6c/9c1a4cc51573e8867c9381db1814223c09ebb4716779c7f845d48688b9c8/tiktoken-0.9.0-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:15a2752dea63d93b0332fb0ddb05dd909371ededa145fe6a3242f46724fa7990", size = 1259661 },
    { url = "https://files.pythonhosted.org/packages/cd/4c/22eb8e9856a2b1808d0a002d171e534eac03f96dbe1161978d7389a59498/tiktoken-0.9.0-cp310-cp310-win_amd64.whl", hash = "sha256:26113fec3bd7a352e4b33dbaf1bd8948de2507e30bd95a44e2b1156647bc01b4", size = 894026 },
    { url = "https://files.pythonhosted.org/packages/4d/ae/4613a59a2a48e761c5161237fc850eb470b4bb93696db89da51b79a871f1/tiktoken-0.9.0-cp311-cp311-macosx_10_12_x86_64.whl", hash = "sha256:f32cc56168eac4851109e9b5d327637f15fd662aa30dd79f964b7c39fbadd26e", size = 1065987 },
    { url = "https://files.pythonhosted.org/packages/3f/86/55d9d1f5b5a7e1164d0f1538a85529b5fcba2b105f92db3622e5d7de6522/tiktoken-0.9.0-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:45556bc41241e5294063508caf901bf92ba52d8ef9222023f83d2483a3055348", size = 1009155 },
    { url = "https://files.pythonhosted.org/packages/03/58/01fb6240df083b7c1916d1dcb024e2b761213c95d576e9f780dfb5625a76/tiktoken-0.9.0-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:03935988a91d6d3216e2ec7c645afbb3d870b37bcb67ada1943ec48678e7ee33", size = 1142898 },
    { url = "https://files.pythonhosted.org/packages/b1/73/41591c525680cd460a6becf56c9b17468d3711b1df242c53d2c7b2183d16/tiktoken-0.9.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:8b3d80aad8d2c6b9238fc1a5524542087c52b860b10cbf952429ffb714bc1136", size = 1197535 },
    { url = "https://files.pythonhosted.org/packages/7d/7c/1069f25521c8f01a1a182f362e5c8e0337907fae91b368b7da9c3e39b810/tiktoken-0.9.0-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:b2a21133be05dc116b1d0372af051cd2c6aa1d2188250c9b553f9fa49301b336", size = 1259548 },
    { url = "https://files.pythonhosted.org/packages/6f/07/c67ad1724b8e14e2b4c8cca04b15da158733ac60136879131db05dda7c30/tiktoken-0.9.0-cp311-cp311-win_amd64.whl", hash = "sha256:11a20e67fdf58b0e2dea7b8654a288e481bb4fc0289d3ad21291f8d0849915fb", size = 893895 },
    { url = "https://files.pythonhosted.org/packages/cf/e5/21ff33ecfa2101c1bb0f9b6df750553bd873b7fb532ce2cb276ff40b197f/tiktoken-0.9.0-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:e88f121c1c22b726649ce67c089b90ddda8b9662545a8aeb03cfef15967ddd03", size = 1065073 },
    { url = "https://files.pythonhosted.org/packages/8e/03/a95e7b4863ee9ceec1c55983e4cc9558bcfd8f4f80e19c4f8a99642f697d/tiktoken-0.9.0-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:a6600660f2f72369acb13a57fb3e212434ed38b045fd8cc6cdd74947b4b5d210", size = 1008075 },
    { url = "https://files.pythonhosted.org/packages/40/10/1305bb02a561595088235a513ec73e50b32e74364fef4de519da69bc8010/tiktoken-0.9.0-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:95e811743b5dfa74f4b227927ed86cbc57cad4df859cb3b643be797914e41794", size = 1140754 },
    { url = "https://files.pythonhosted.org/packages/1b/40/da42522018ca496432ffd02793c3a72a739ac04c3794a4914570c9bb2925/tiktoken-0.9.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:99376e1370d59bcf6935c933cb9ba64adc29033b7e73f5f7569f3aad86552b22", size = 1196678 },
    { url = "https://files.pythonhosted.org/packages/5c/41/1e59dddaae270ba20187ceb8aa52c75b24ffc09f547233991d5fd822838b/tiktoken-0.9.0-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:badb947c32739fb6ddde173e14885fb3de4d32ab9d8c591cbd013c22b4c31dd2", size = 1259283 },
    { url = "https://files.pythonhosted.org/packages/5b/64/b16003419a1d7728d0d8c0d56a4c24325e7b10a21a9dd1fc0f7115c02f0a/tiktoken-0.9.0-cp312-cp312-win_amd64.whl", hash = "sha256:5a62d7a25225bafed786a524c1b9f0910a1128f4232615bf3f8257a73aaa3b16", size = 894897 },
    { url = "https://files.pythonhosted.org/packages/7a/11/09d936d37f49f4f494ffe660af44acd2d99eb2429d60a57c71318af214e0/tiktoken-0.9.0-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:2b0e8e05a26eda1249e824156d537015480af7ae222ccb798e5234ae0285dbdb", size = 1064919 },
    { url = "https://files.pythonhosted.org/packages/80/0e/f38ba35713edb8d4197ae602e80837d574244ced7fb1b6070b31c29816e0/tiktoken-0.9.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:27d457f096f87685195eea0165a1807fae87b97b2161fe8c9b1df5bd74ca6f63", size = 1007877 },
    { url = "https://files.pythonhosted.org/packages/fe/82/9197f77421e2a01373e27a79dd36efdd99e6b4115746ecc553318ecafbf0/tiktoken-0.9.0-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:2cf8ded49cddf825390e36dd1ad35cd49589e8161fdcb52aa25f0583e90a3e01", size = 1140095 },
    { url = "https://files.pythonhosted.org/packages/f2/bb/4513da71cac187383541facd0291c4572b03ec23c561de5811781bbd988f/tiktoken-0.9.0-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:cc156cb314119a8bb9748257a2eaebd5cc0753b6cb491d26694ed42fc7cb3139", size = 1195649 },
    { url = "https://files.pythonhosted.org/packages/fa/5c/74e4c137530dd8504e97e3a41729b1103a4ac29036cbfd3250b11fd29451/tiktoken-0.9.0-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:cd69372e8c9dd761f0ab873112aba55a0e3e506332dd9f7522ca466e817b1b7a", size = 1258465 },
    { url = "https://files.pythonhosted.org/packages/de/a8/8f499c179ec900783ffe133e9aab10044481679bb9aad78436d239eee716/tiktoken-0.9.0-cp313-cp313-win_amd64.whl", hash = "sha256:5ea0edb6f83dc56d794723286215918c1cde03712cbbafa0348b33448faf5b95", size = 894669 },
    { url = "https://files.pythonhosted.org/packages/c4/92/4d681b5c066d417b98f22a0176358d9e606e183c6b61c337d61fb54accb4/tiktoken-0.9.0-cp39-cp39-macosx_10_12_x86_64.whl", hash = "sha256:c6386ca815e7d96ef5b4ac61e0048cd32ca5a92d5781255e13b31381d28667dc", size = 1066217 },
    { url = "https://files.pythonhosted.org/packages/12/dd/af27bbe186df481666de48cf0f2f4e0643ba9c78b472e7bf70144c663b22/tiktoken-0.9.0-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:75f6d5db5bc2c6274b674ceab1615c1778e6416b14705827d19b40e6355f03e0", size = 1009441 },
    { url = "https://files.pythonhosted.org/packages/33/35/2792b7dcb8b150d2767322637513c73a3e80833c19212efea80b31087894/tiktoken-0.9.0-cp39-cp39-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:e15b16f61e6f4625a57a36496d28dd182a8a60ec20a534c5343ba3cafa156ac7", size = 1144423 },
    { url = "https://files.pythonhosted.org/packages/65/ae/4d1682510172ce3500bbed3b206ebc4efefe280f0bf1179cfb043f88cc16/tiktoken-0.9.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:3ebcec91babf21297022882344c3f7d9eed855931466c3311b1ad6b64befb3df", size = 1199002 },
    { url = "https://files.pythonhosted.org/packages/1c/2e/df2dc31dd161190f315829775a9652ea01d60f307af8f98e35bdd14a6a93/tiktoken-0.9.0-cp39-cp39-musllinux_1_2_x86_64.whl", hash = "sha256:e5fd49e7799579240f03913447c0cdfa1129625ebd5ac440787afc4345990427", size = 1260610 },
    { url = "https://files.pythonhosted.org/packages/70/22/e8fc1bf9cdecc439b7ddc28a45b976a8c699a38874c070749d855696368a/tiktoken-0.9.0-cp39-cp39-win_amd64.whl", hash = "sha256:26242ca9dc8b58e875ff4ca078b9a94d2f0813e6a535dcd2205df5d49d927cc7", size = 894215 },
]

[[package]]
name = "tokenizers"
version = "0.21.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "huggingface-hub" },
]
sdist = { url = "https://files.pythonhosted.org/packages/92/76/5ac0c97f1117b91b7eb7323dcd61af80d72f790b4df71249a7850c195f30/tokenizers-0.21.1.tar.gz", hash = "sha256:a1bb04dc5b448985f86ecd4b05407f5a8d97cb2c0532199b2a302a604a0165ab", size = 343256 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/a5/1f/328aee25f9115bf04262e8b4e5a2050b7b7cf44b59c74e982db7270c7f30/tokenizers-0.21.1-cp39-abi3-macosx_10_12_x86_64.whl", hash = "sha256:e78e413e9e668ad790a29456e677d9d3aa50a9ad311a40905d6861ba7692cf41", size = 2780767 },
    { url = "https://files.pythonhosted.org/packages/ae/1a/4526797f3719b0287853f12c5ad563a9be09d446c44ac784cdd7c50f76ab/tokenizers-0.21.1-cp39-abi3-macosx_11_0_arm64.whl", hash = "sha256:cd51cd0a91ecc801633829fcd1fda9cf8682ed3477c6243b9a095539de4aecf3", size = 2650555 },
    { url = "https://files.pythonhosted.org/packages/4d/7a/a209b29f971a9fdc1da86f917fe4524564924db50d13f0724feed37b2a4d/tokenizers-0.21.1-cp39-abi3-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:28da6b72d4fb14ee200a1bd386ff74ade8992d7f725f2bde2c495a9a98cf4d9f", size = 2937541 },
    { url = "https://files.pythonhosted.org/packages/3c/1e/b788b50ffc6191e0b1fc2b0d49df8cff16fe415302e5ceb89f619d12c5bc/tokenizers-0.21.1-cp39-abi3-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:34d8cfde551c9916cb92014e040806122295a6800914bab5865deb85623931cf", size = 2819058 },
    { url = "https://files.pythonhosted.org/packages/36/aa/3626dfa09a0ecc5b57a8c58eeaeb7dd7ca9a37ad9dd681edab5acd55764c/tokenizers-0.21.1-cp39-abi3-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:aaa852d23e125b73d283c98f007e06d4595732104b65402f46e8ef24b588d9f8", size = 3133278 },
    { url = "https://files.pythonhosted.org/packages/a4/4d/8fbc203838b3d26269f944a89459d94c858f5b3f9a9b6ee9728cdcf69161/tokenizers-0.21.1-cp39-abi3-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:a21a15d5c8e603331b8a59548bbe113564136dc0f5ad8306dd5033459a226da0", size = 3144253 },
    { url = "https://files.pythonhosted.org/packages/d8/1b/2bd062adeb7c7511b847b32e356024980c0ffcf35f28947792c2d8ad2288/tokenizers-0.21.1-cp39-abi3-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:2fdbd4c067c60a0ac7eca14b6bd18a5bebace54eb757c706b47ea93204f7a37c", size = 3398225 },
    { url = "https://files.pythonhosted.org/packages/8a/63/38be071b0c8e06840bc6046991636bcb30c27f6bb1e670f4f4bc87cf49cc/tokenizers-0.21.1-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:2dd9a0061e403546f7377df940e866c3e678d7d4e9643d0461ea442b4f89e61a", size = 3038874 },
    { url = "https://files.pythonhosted.org/packages/ec/83/afa94193c09246417c23a3c75a8a0a96bf44ab5630a3015538d0c316dd4b/tokenizers-0.21.1-cp39-abi3-musllinux_1_2_aarch64.whl", hash = "sha256:db9484aeb2e200c43b915a1a0150ea885e35f357a5a8fabf7373af333dcc8dbf", size = 9014448 },
    { url = "https://files.pythonhosted.org/packages/ae/b3/0e1a37d4f84c0f014d43701c11eb8072704f6efe8d8fc2dcdb79c47d76de/tokenizers-0.21.1-cp39-abi3-musllinux_1_2_armv7l.whl", hash = "sha256:ed248ab5279e601a30a4d67bdb897ecbe955a50f1e7bb62bd99f07dd11c2f5b6", size = 8937877 },
    { url = "https://files.pythonhosted.org/packages/ac/33/ff08f50e6d615eb180a4a328c65907feb6ded0b8f990ec923969759dc379/tokenizers-0.21.1-cp39-abi3-musllinux_1_2_i686.whl", hash = "sha256:9ac78b12e541d4ce67b4dfd970e44c060a2147b9b2a21f509566d556a509c67d", size = 9186645 },
    { url = "https://files.pythonhosted.org/packages/5f/aa/8ae85f69a9f6012c6f8011c6f4aa1c96154c816e9eea2e1b758601157833/tokenizers-0.21.1-cp39-abi3-musllinux_1_2_x86_64.whl", hash = "sha256:e5a69c1a4496b81a5ee5d2c1f3f7fbdf95e90a0196101b0ee89ed9956b8a168f", size = 9384380 },
    { url = "https://files.pythonhosted.org/packages/e8/5b/a5d98c89f747455e8b7a9504910c865d5e51da55e825a7ae641fb5ff0a58/tokenizers-0.21.1-cp39-abi3-win32.whl", hash = "sha256:1039a3a5734944e09de1d48761ade94e00d0fa760c0e0551151d4dd851ba63e3", size = 2239506 },
    { url = "https://files.pythonhosted.org/packages/e6/b6/072a8e053ae600dcc2ac0da81a23548e3b523301a442a6ca900e92ac35be/tokenizers-0.21.1-cp39-abi3-win_amd64.whl", hash = "sha256:0f0dcbcc9f6e13e675a66d7a5f2f225a736745ce484c1a4e07476a89ccdad382", size = 2435481 },
]

[[package]]
name = "tomli"
version = "2.2.1"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/18/87/302344fed471e44a87289cf4967697d07e532f2421fdaf868a303cbae4ff/tomli-2.2.1.tar.gz", hash = "sha256:cd45e1dc79c835ce60f7404ec8119f2eb06d38b1deba146f07ced3bbc44505ff", size = 17175 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/43/ca/75707e6efa2b37c77dadb324ae7d9571cb424e61ea73fad7c56c2d14527f/tomli-2.2.1-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:678e4fa69e4575eb77d103de3df8a895e1591b48e740211bd1067378c69e8249", size = 131077 },
    { url = "https://files.pythonhosted.org/packages/c7/16/51ae563a8615d472fdbffc43a3f3d46588c264ac4f024f63f01283becfbb/tomli-2.2.1-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:023aa114dd824ade0100497eb2318602af309e5a55595f76b626d6d9f3b7b0a6", size = 123429 },
    { url = "https://files.pythonhosted.org/packages/f1/dd/4f6cd1e7b160041db83c694abc78e100473c15d54620083dbd5aae7b990e/tomli-2.2.1-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:ece47d672db52ac607a3d9599a9d48dcb2f2f735c6c2d1f34130085bb12b112a", size = 226067 },
    { url = "https://files.pythonhosted.org/packages/a9/6b/c54ede5dc70d648cc6361eaf429304b02f2871a345bbdd51e993d6cdf550/tomli-2.2.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:6972ca9c9cc9f0acaa56a8ca1ff51e7af152a9f87fb64623e31d5c83700080ee", size = 236030 },
    { url = "https://files.pythonhosted.org/packages/1f/47/999514fa49cfaf7a92c805a86c3c43f4215621855d151b61c602abb38091/tomli-2.2.1-cp311-cp311-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:c954d2250168d28797dd4e3ac5cf812a406cd5a92674ee4c8f123c889786aa8e", size = 240898 },
    { url = "https://files.pythonhosted.org/packages/73/41/0a01279a7ae09ee1573b423318e7934674ce06eb33f50936655071d81a24/tomli-2.2.1-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:8dd28b3e155b80f4d54beb40a441d366adcfe740969820caf156c019fb5c7ec4", size = 229894 },
    { url = "https://files.pythonhosted.org/packages/55/18/5d8bc5b0a0362311ce4d18830a5d28943667599a60d20118074ea1b01bb7/tomli-2.2.1-cp311-cp311-musllinux_1_2_i686.whl", hash = "sha256:e59e304978767a54663af13c07b3d1af22ddee3bb2fb0618ca1593e4f593a106", size = 245319 },
    { url = "https://files.pythonhosted.org/packages/92/a3/7ade0576d17f3cdf5ff44d61390d4b3febb8a9fc2b480c75c47ea048c646/tomli-2.2.1-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:33580bccab0338d00994d7f16f4c4ec25b776af3ffaac1ed74e0b3fc95e885a8", size = 238273 },
    { url = "https://files.pythonhosted.org/packages/72/6f/fa64ef058ac1446a1e51110c375339b3ec6be245af9d14c87c4a6412dd32/tomli-2.2.1-cp311-cp311-win32.whl", hash = "sha256:465af0e0875402f1d226519c9904f37254b3045fc5084697cefb9bdde1ff99ff", size = 98310 },
    { url = "https://files.pythonhosted.org/packages/6a/1c/4a2dcde4a51b81be3530565e92eda625d94dafb46dbeb15069df4caffc34/tomli-2.2.1-cp311-cp311-win_amd64.whl", hash = "sha256:2d0f2fdd22b02c6d81637a3c95f8cd77f995846af7414c5c4b8d0545afa1bc4b", size = 108309 },
    { url = "https://files.pythonhosted.org/packages/52/e1/f8af4c2fcde17500422858155aeb0d7e93477a0d59a98e56cbfe75070fd0/tomli-2.2.1-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:4a8f6e44de52d5e6c657c9fe83b562f5f4256d8ebbfe4ff922c495620a7f6cea", size = 132762 },
    { url = "https://files.pythonhosted.org/packages/03/b8/152c68bb84fc00396b83e7bbddd5ec0bd3dd409db4195e2a9b3e398ad2e3/tomli-2.2.1-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:8d57ca8095a641b8237d5b079147646153d22552f1c637fd3ba7f4b0b29167a8", size = 123453 },
    { url = "https://files.pythonhosted.org/packages/c8/d6/fc9267af9166f79ac528ff7e8c55c8181ded34eb4b0e93daa767b8841573/tomli-2.2.1-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:4e340144ad7ae1533cb897d406382b4b6fede8890a03738ff1683af800d54192", size = 233486 },
    { url = "https://files.pythonhosted.org/packages/5c/51/51c3f2884d7bab89af25f678447ea7d297b53b5a3b5730a7cb2ef6069f07/tomli-2.2.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:db2b95f9de79181805df90bedc5a5ab4c165e6ec3fe99f970d0e302f384ad222", size = 242349 },
    { url = "https://files.pythonhosted.org/packages/ab/df/bfa89627d13a5cc22402e441e8a931ef2108403db390ff3345c05253935e/tomli-2.2.1-cp312-cp312-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:40741994320b232529c802f8bc86da4e1aa9f413db394617b9a256ae0f9a7f77", size = 252159 },
    { url = "https://files.pythonhosted.org/packages/9e/6e/fa2b916dced65763a5168c6ccb91066f7639bdc88b48adda990db10c8c0b/tomli-2.2.1-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:400e720fe168c0f8521520190686ef8ef033fb19fc493da09779e592861b78c6", size = 237243 },
    { url = "https://files.pythonhosted.org/packages/b4/04/885d3b1f650e1153cbb93a6a9782c58a972b94ea4483ae4ac5cedd5e4a09/tomli-2.2.1-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:02abe224de6ae62c19f090f68da4e27b10af2b93213d36cf44e6e1c5abd19fdd", size = 259645 },
    { url = "https://files.pythonhosted.org/packages/9c/de/6b432d66e986e501586da298e28ebeefd3edc2c780f3ad73d22566034239/tomli-2.2.1-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:b82ebccc8c8a36f2094e969560a1b836758481f3dc360ce9a3277c65f374285e", size = 244584 },
    { url = "https://files.pythonhosted.org/packages/1c/9a/47c0449b98e6e7d1be6cbac02f93dd79003234ddc4aaab6ba07a9a7482e2/tomli-2.2.1-cp312-cp312-win32.whl", hash = "sha256:889f80ef92701b9dbb224e49ec87c645ce5df3fa2cc548664eb8a25e03127a98", size = 98875 },
    { url = "https://files.pythonhosted.org/packages/ef/60/9b9638f081c6f1261e2688bd487625cd1e660d0a85bd469e91d8db969734/tomli-2.2.1-cp312-cp312-win_amd64.whl", hash = "sha256:7fc04e92e1d624a4a63c76474610238576942d6b8950a2d7f908a340494e67e4", size = 109418 },
    { url = "https://files.pythonhosted.org/packages/04/90/2ee5f2e0362cb8a0b6499dc44f4d7d48f8fff06d28ba46e6f1eaa61a1388/tomli-2.2.1-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:f4039b9cbc3048b2416cc57ab3bda989a6fcf9b36cf8937f01a6e731b64f80d7", size = 132708 },
    { url = "https://files.pythonhosted.org/packages/c0/ec/46b4108816de6b385141f082ba99e315501ccd0a2ea23db4a100dd3990ea/tomli-2.2.1-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:286f0ca2ffeeb5b9bd4fcc8d6c330534323ec51b2f52da063b11c502da16f30c", size = 123582 },
    { url = "https://files.pythonhosted.org/packages/a0/bd/b470466d0137b37b68d24556c38a0cc819e8febe392d5b199dcd7f578365/tomli-2.2.1-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:a92ef1a44547e894e2a17d24e7557a5e85a9e1d0048b0b5e7541f76c5032cb13", size = 232543 },
    { url = "https://files.pythonhosted.org/packages/d9/e5/82e80ff3b751373f7cead2815bcbe2d51c895b3c990686741a8e56ec42ab/tomli-2.2.1-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:9316dc65bed1684c9a98ee68759ceaed29d229e985297003e494aa825ebb0281", size = 241691 },
    { url = "https://files.pythonhosted.org/packages/05/7e/2a110bc2713557d6a1bfb06af23dd01e7dde52b6ee7dadc589868f9abfac/tomli-2.2.1-cp313-cp313-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:e85e99945e688e32d5a35c1ff38ed0b3f41f43fad8df0bdf79f72b2ba7bc5272", size = 251170 },
    { url = "https://files.pythonhosted.org/packages/64/7b/22d713946efe00e0adbcdfd6d1aa119ae03fd0b60ebed51ebb3fa9f5a2e5/tomli-2.2.1-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:ac065718db92ca818f8d6141b5f66369833d4a80a9d74435a268c52bdfa73140", size = 236530 },
    { url = "https://files.pythonhosted.org/packages/38/31/3a76f67da4b0cf37b742ca76beaf819dca0ebef26d78fc794a576e08accf/tomli-2.2.1-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:d920f33822747519673ee656a4b6ac33e382eca9d331c87770faa3eef562aeb2", size = 258666 },
    { url = "https://files.pythonhosted.org/packages/07/10/5af1293da642aded87e8a988753945d0cf7e00a9452d3911dd3bb354c9e2/tomli-2.2.1-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:a198f10c4d1b1375d7687bc25294306e551bf1abfa4eace6650070a5c1ae2744", size = 243954 },
    { url = "https://files.pythonhosted.org/packages/5b/b9/1ed31d167be802da0fc95020d04cd27b7d7065cc6fbefdd2f9186f60d7bd/tomli-2.2.1-cp313-cp313-win32.whl", hash = "sha256:d3f5614314d758649ab2ab3a62d4f2004c825922f9e370b29416484086b264ec", size = 98724 },
    { url = "https://files.pythonhosted.org/packages/c7/32/b0963458706accd9afcfeb867c0f9175a741bf7b19cd424230714d722198/tomli-2.2.1-cp313-cp313-win_amd64.whl", hash = "sha256:a38aa0308e754b0e3c67e344754dff64999ff9b513e691d0e786265c93583c69", size = 109383 },
    { url = "https://files.pythonhosted.org/packages/6e/c2/61d3e0f47e2b74ef40a68b9e6ad5984f6241a942f7cd3bbfbdbd03861ea9/tomli-2.2.1-py3-none-any.whl", hash = "sha256:cb55c73c5f4408779d0cf3eef9f762b9c9f147a77de7b258bef0a5628adc85cc", size = 14257 },
]

[[package]]
name = "torch"
version = "2.6.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "filelock" },
    { name = "fsspec" },
    { name = "jinja2" },
    { name = "networkx" },
    { name = "nvidia-cublas-cu12", marker = "platform_machine == 'x86_64' and platform_system == 'Linux'" },
    { name = "nvidia-cuda-cupti-cu12", marker = "platform_machine == 'x86_64' and platform_system == 'Linux'" },
    { name = "nvidia-cuda-nvrtc-cu12", marker = "platform_machine == 'x86_64' and platform_system == 'Linux'" },
    { name = "nvidia-cuda-runtime-cu12", marker = "platform_machine == 'x86_64' and platform_system == 'Linux'" },
    { name = "nvidia-cudnn-cu12", marker = "platform_machine == 'x86_64' and platform_system == 'Linux'" },
    { name = "nvidia-cufft-cu12", marker = "platform_machine == 'x86_64' and platform_system == 'Linux'" },
    { name = "nvidia-curand-cu12", marker = "platform_machine == 'x86_64' and platform_system == 'Linux'" },
    { name = "nvidia-cusolver-cu12", marker = "platform_machine == 'x86_64' and platform_system == 'Linux'" },
    { name = "nvidia-cusparse-cu12", marker = "platform_machine == 'x86_64' and platform_system == 'Linux'" },
    { name = "nvidia-cusparselt-cu12", marker = "platform_machine == 'x86_64' and platform_system == 'Linux'" },
    { name = "nvidia-nccl-cu12", marker = "platform_machine == 'x86_64' and platform_system == 'Linux'" },
    { name = "nvidia-nvjitlink-cu12", marker = "platform_machine == 'x86_64' and platform_system == 'Linux'" },
    { name = "nvidia-nvtx-cu12", marker = "platform_machine == 'x86_64' and platform_system == 'Linux'" },
    { name = "setuptools", marker = "python_full_version >= '3.12'" },
    { name = "sympy" },
    { name = "triton", marker = "platform_machine == 'x86_64' and platform_system == 'Linux'" },
    { name = "typing-extensions" },
]
wheels = [
    { url = "https://files.pythonhosted.org/packages/37/81/aa9ab58ec10264c1abe62c8b73f5086c3c558885d6beecebf699f0dbeaeb/torch-2.6.0-cp310-cp310-manylinux1_x86_64.whl", hash = "sha256:6860df13d9911ac158f4c44031609700e1eba07916fff62e21e6ffa0a9e01961", size = 766685561 },
    { url = "https://files.pythonhosted.org/packages/86/86/e661e229df2f5bfc6eab4c97deb1286d598bbeff31ab0cdb99b3c0d53c6f/torch-2.6.0-cp310-cp310-manylinux_2_28_aarch64.whl", hash = "sha256:c4f103a49830ce4c7561ef4434cc7926e5a5fe4e5eb100c19ab36ea1e2b634ab", size = 95751887 },
    { url = "https://files.pythonhosted.org/packages/20/e0/5cb2f8493571f0a5a7273cd7078f191ac252a402b5fb9cb6091f14879109/torch-2.6.0-cp310-cp310-win_amd64.whl", hash = "sha256:56eeaf2ecac90da5d9e35f7f35eb286da82673ec3c582e310a8d1631a1c02341", size = 204165139 },
    { url = "https://files.pythonhosted.org/packages/e5/16/ea1b7842413a7b8a5aaa5e99e8eaf3da3183cc3ab345ad025a07ff636301/torch-2.6.0-cp310-none-macosx_11_0_arm64.whl", hash = "sha256:09e06f9949e1a0518c5b09fe95295bc9661f219d9ecb6f9893e5123e10696628", size = 66520221 },
    { url = "https://files.pythonhosted.org/packages/78/a9/97cbbc97002fff0de394a2da2cdfa859481fdca36996d7bd845d50aa9d8d/torch-2.6.0-cp311-cp311-manylinux1_x86_64.whl", hash = "sha256:7979834102cd5b7a43cc64e87f2f3b14bd0e1458f06e9f88ffa386d07c7446e1", size = 766715424 },
    { url = "https://files.pythonhosted.org/packages/6d/fa/134ce8f8a7ea07f09588c9cc2cea0d69249efab977707cf67669431dcf5c/torch-2.6.0-cp311-cp311-manylinux_2_28_aarch64.whl", hash = "sha256:ccbd0320411fe1a3b3fec7b4d3185aa7d0c52adac94480ab024b5c8f74a0bf1d", size = 95759416 },
    { url = "https://files.pythonhosted.org/packages/11/c5/2370d96b31eb1841c3a0883a492c15278a6718ccad61bb6a649c80d1d9eb/torch-2.6.0-cp311-cp311-win_amd64.whl", hash = "sha256:46763dcb051180ce1ed23d1891d9b1598e07d051ce4c9d14307029809c4d64f7", size = 204164970 },
    { url = "https://files.pythonhosted.org/packages/0b/fa/f33a4148c6fb46ca2a3f8de39c24d473822d5774d652b66ed9b1214da5f7/torch-2.6.0-cp311-none-macosx_11_0_arm64.whl", hash = "sha256:94fc63b3b4bedd327af588696559f68c264440e2503cc9e6954019473d74ae21", size = 66530713 },
    { url = "https://files.pythonhosted.org/packages/e5/35/0c52d708144c2deb595cd22819a609f78fdd699b95ff6f0ebcd456e3c7c1/torch-2.6.0-cp312-cp312-manylinux1_x86_64.whl", hash = "sha256:2bb8987f3bb1ef2675897034402373ddfc8f5ef0e156e2d8cfc47cacafdda4a9", size = 766624563 },
    { url = "https://files.pythonhosted.org/packages/01/d6/455ab3fbb2c61c71c8842753b566012e1ed111e7a4c82e0e1c20d0c76b62/torch-2.6.0-cp312-cp312-manylinux_2_28_aarch64.whl", hash = "sha256:b789069020c5588c70d5c2158ac0aa23fd24a028f34a8b4fcb8fcb4d7efcf5fb", size = 95607867 },
    { url = "https://files.pythonhosted.org/packages/18/cf/ae99bd066571656185be0d88ee70abc58467b76f2f7c8bfeb48735a71fe6/torch-2.6.0-cp312-cp312-win_amd64.whl", hash = "sha256:7e1448426d0ba3620408218b50aa6ada88aeae34f7a239ba5431f6c8774b1239", size = 204120469 },
    { url = "https://files.pythonhosted.org/packages/81/b4/605ae4173aa37fb5aa14605d100ff31f4f5d49f617928c9f486bb3aaec08/torch-2.6.0-cp312-none-macosx_11_0_arm64.whl", hash = "sha256:9a610afe216a85a8b9bc9f8365ed561535c93e804c2a317ef7fabcc5deda0989", size = 66532538 },
    { url = "https://files.pythonhosted.org/packages/24/85/ead1349fc30fe5a32cadd947c91bda4a62fbfd7f8c34ee61f6398d38fb48/torch-2.6.0-cp313-cp313-manylinux1_x86_64.whl", hash = "sha256:4874a73507a300a5d089ceaff616a569e7bb7c613c56f37f63ec3ffac65259cf", size = 766626191 },
    { url = "https://files.pythonhosted.org/packages/dd/b0/26f06f9428b250d856f6d512413e9e800b78625f63801cbba13957432036/torch-2.6.0-cp313-cp313-manylinux_2_28_aarch64.whl", hash = "sha256:a0d5e1b9874c1a6c25556840ab8920569a7a4137afa8a63a32cee0bc7d89bd4b", size = 95611439 },
    { url = "https://files.pythonhosted.org/packages/c2/9c/fc5224e9770c83faed3a087112d73147cd7c7bfb7557dcf9ad87e1dda163/torch-2.6.0-cp313-cp313-win_amd64.whl", hash = "sha256:510c73251bee9ba02ae1cb6c9d4ee0907b3ce6020e62784e2d7598e0cfa4d6cc", size = 204126475 },
    { url = "https://files.pythonhosted.org/packages/88/8b/d60c0491ab63634763be1537ad488694d316ddc4a20eaadd639cedc53971/torch-2.6.0-cp313-none-macosx_11_0_arm64.whl", hash = "sha256:ff96f4038f8af9f7ec4231710ed4549da1bdebad95923953a25045dcf6fd87e2", size = 66536783 },
    { url = "https://files.pythonhosted.org/packages/40/bb/feb5644baa621fd8e1e88bf51f6fa38ab3f985d472a764144ff4867ac1d6/torch-2.6.0-cp39-cp39-manylinux1_x86_64.whl", hash = "sha256:9ea955317cfcd3852b1402b62af258ce735c2edeee42ca9419b6bc889e5ae053", size = 766680961 },
    { url = "https://files.pythonhosted.org/packages/ee/11/08774a8198a33263947c59e04b8a0bf85a61a44e82100c46cf833bbce35e/torch-2.6.0-cp39-cp39-manylinux_2_28_aarch64.whl", hash = "sha256:bb2c6c3e65049f081940f5ab15c9136c7de40d3f01192541c920a07c7c585b7e", size = 95782656 },
    { url = "https://files.pythonhosted.org/packages/c1/0d/56fb07032accbfebb4555638b6002ec5678d0942da85497e40f9405ab756/torch-2.6.0-cp39-cp39-win_amd64.whl", hash = "sha256:683410f97984103148e31b38a8631acf31c3034c020c0f4d26171e7626d8317a", size = 204061417 },
    { url = "https://files.pythonhosted.org/packages/b3/17/41f681b87290a1d2f1394f943e470f8b0b3c2987b7df8dc078d8831fce5b/torch-2.6.0-cp39-none-macosx_11_0_arm64.whl", hash = "sha256:265f70de5fd45b864d924b64be1797f86e76c8e48a02c2a3a6fc7ec247d2226c", size = 66520446 },
]

[[package]]
name = "tqdm"
version = "4.67.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "colorama", marker = "platform_system == 'Windows'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/a8/4b/29b4ef32e036bb34e4ab51796dd745cdba7ed47ad142a9f4a1eb8e0c744d/tqdm-4.67.1.tar.gz", hash = "sha256:f8aef9c52c08c13a65f30ea34f4e5aac3fd1a34959879d7e59e63027286627f2", size = 169737 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/d0/30/dc54f88dd4a2b5dc8a0279bdd7270e735851848b762aeb1c1184ed1f6b14/tqdm-4.67.1-py3-none-any.whl", hash = "sha256:26445eca388f82e72884e0d580d5464cd801a3ea01e63e5601bdff9ba6a48de2", size = 78540 },
]

[[package]]
name = "transformers"
version = "4.51.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "filelock" },
    { name = "huggingface-hub" },
    { name = "numpy" },
    { name = "packaging" },
    { name = "pyyaml" },
    { name = "regex" },
    { name = "requests" },
    { name = "safetensors" },
    { name = "tokenizers" },
    { name = "tqdm" },
]
sdist = { url = "https://files.pythonhosted.org/packages/38/75/6ebdae4d6f4574f47139a070445245537e43482d006f615af8e23d5bf05e/transformers-4.51.0.tar.gz", hash = "sha256:2d302563ff6c2cc2d0e88ef352cf059f9a21ce18102fd43662bb1246f70b8a84", size = 8925571 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/6f/db/7ee15028d5130929aa0b1b85bab6d8bafe806254d3b5c56c42a0066cceb8/transformers-4.51.0-py3-none-any.whl", hash = "sha256:2e6baa476735ab8adccbaee6961525a0d1ce8c21d49293af30ef5ee4b082f64d", size = 10362017 },
]

[[package]]
name = "triton"
version = "3.2.0"
source = { registry = "https://pypi.org/simple" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/01/65/3ffa90e158a2c82f0716eee8d26a725d241549b7d7aaf7e4f44ac03ebd89/triton-3.2.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:b3e54983cd51875855da7c68ec05c05cf8bb08df361b1d5b69e05e40b0c9bd62", size = 253090354 },
    { url = "https://files.pythonhosted.org/packages/a7/2e/757d2280d4fefe7d33af7615124e7e298ae7b8e3bc4446cdb8e88b0f9bab/triton-3.2.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:8009a1fb093ee8546495e96731336a33fb8856a38e45bb4ab6affd6dbc3ba220", size = 253157636 },
    { url = "https://files.pythonhosted.org/packages/06/00/59500052cb1cf8cf5316be93598946bc451f14072c6ff256904428eaf03c/triton-3.2.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:8d9b215efc1c26fa7eefb9a157915c92d52e000d2bf83e5f69704047e63f125c", size = 253159365 },
    { url = "https://files.pythonhosted.org/packages/c7/30/37a3384d1e2e9320331baca41e835e90a3767303642c7a80d4510152cbcf/triton-3.2.0-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:e5dfa23ba84541d7c0a531dfce76d8bcd19159d50a4a8b14ad01e91734a5c1b0", size = 253154278 },
    { url = "https://files.pythonhosted.org/packages/bc/74/9f12bdedeb110242d8bb1bd621f6605e753ee0cbf73cf7f3a62b8173f190/triton-3.2.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:30ceed0eff2c4a73b14eb63e052992f44bbdf175f3fad21e1ac8097a772de7ee", size = 253057866 },
]

[[package]]
name = "types-requests"
version = "2.32.0.20250328"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "urllib3" },
]
sdist = { url = "https://files.pythonhosted.org/packages/00/7d/eb174f74e3f5634eaacb38031bbe467dfe2e545bc255e5c90096ec46bc46/types_requests-2.32.0.20250328.tar.gz", hash = "sha256:c9e67228ea103bd811c96984fac36ed2ae8da87a36a633964a21f199d60baf32", size = 22995 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/cc/15/3700282a9d4ea3b37044264d3e4d1b1f0095a4ebf860a99914fd544e3be3/types_requests-2.32.0.20250328-py3-none-any.whl", hash = "sha256:72ff80f84b15eb3aa7a8e2625fffb6a93f2ad5a0c20215fc1dcfa61117bcb2a2", size = 20663 },
]

[[package]]
name = "typing-extensions"
version = "4.13.1"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/76/ad/cd3e3465232ec2416ae9b983f27b9e94dc8171d56ac99b345319a9475967/typing_extensions-4.13.1.tar.gz", hash = "sha256:98795af00fb9640edec5b8e31fc647597b4691f099ad75f469a2616be1a76dff", size = 106633 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/df/c5/e7a0b0f5ed69f94c8ab7379c599e6036886bffcde609969a5325f47f1332/typing_extensions-4.13.1-py3-none-any.whl", hash = "sha256:4b6cf02909eb5495cfbc3f6e8fd49217e6cc7944e145cdda8caa3734777f9e69", size = 45739 },
]

[[package]]
name = "typing-inspection"
version = "0.4.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "typing-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/82/5c/e6082df02e215b846b4b8c0b887a64d7d08ffaba30605502639d44c06b82/typing_inspection-0.4.0.tar.gz", hash = "sha256:9765c87de36671694a67904bf2c96e395be9c6439bb6c87b5142569dcdd65122", size = 76222 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/31/08/aa4fdfb71f7de5176385bd9e90852eaf6b5d622735020ad600f2bab54385/typing_inspection-0.4.0-py3-none-any.whl", hash = "sha256:50e72559fcd2a6367a19f7a7e610e6afcb9fac940c650290eed893d61386832f", size = 14125 },
]

[[package]]
name = "tzdata"
version = "2025.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/95/32/1a225d6164441be760d75c2c42e2780dc0873fe382da3e98a2e1e48361e5/tzdata-2025.2.tar.gz", hash = "sha256:b60a638fcc0daffadf82fe0f57e53d06bdec2f36c4df66280ae79bce6bd6f2b9", size = 196380 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/5c/23/c7abc0ca0a1526a0774eca151daeb8de62ec457e77262b66b359c3c7679e/tzdata-2025.2-py2.py3-none-any.whl", hash = "sha256:1a403fada01ff9221ca8044d701868fa132215d84beb92242d9acd2147f667a8", size = 347839 },
]

[[package]]
name = "urllib3"
version = "2.3.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/aa/63/e53da845320b757bf29ef6a9062f5c669fe997973f966045cb019c3f4b66/urllib3-2.3.0.tar.gz", hash = "sha256:f8c5449b3cf0861679ce7e0503c7b44b5ec981bec0d1d3795a07f1ba96f0204d", size = 307268 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/c8/19/4ec628951a74043532ca2cf5d97b7b14863931476d117c471e8e2b1eb39f/urllib3-2.3.0-py3-none-any.whl", hash = "sha256:1cee9ad369867bfdbbb48b7dd50374c0967a0bb7710050facf0dd6911440e3df", size = 128369 },
]

[[package]]
name = "xxhash"
version = "3.5.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/00/5e/d6e5258d69df8b4ed8c83b6664f2b47d30d2dec551a29ad72a6c69eafd31/xxhash-3.5.0.tar.gz", hash = "sha256:84f2caddf951c9cbf8dc2e22a89d4ccf5d86391ac6418fe81e3c67d0cf60b45f", size = 84241 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/bb/8a/0e9feca390d512d293afd844d31670e25608c4a901e10202aa98785eab09/xxhash-3.5.0-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:ece616532c499ee9afbb83078b1b952beffef121d989841f7f4b3dc5ac0fd212", size = 31970 },
    { url = "https://files.pythonhosted.org/packages/16/e6/be5aa49580cd064a18200ab78e29b88b1127e1a8c7955eb8ecf81f2626eb/xxhash-3.5.0-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:3171f693dbc2cef6477054a665dc255d996646b4023fe56cb4db80e26f4cc520", size = 30801 },
    { url = "https://files.pythonhosted.org/packages/20/ee/b8a99ebbc6d1113b3a3f09e747fa318c3cde5b04bd9c197688fadf0eeae8/xxhash-3.5.0-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:7c5d3e570ef46adaf93fc81b44aca6002b5a4d8ca11bd0580c07eac537f36680", size = 220927 },
    { url = "https://files.pythonhosted.org/packages/58/62/15d10582ef159283a5c2b47f6d799fc3303fe3911d5bb0bcc820e1ef7ff4/xxhash-3.5.0-cp310-cp310-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:7cb29a034301e2982df8b1fe6328a84f4b676106a13e9135a0d7e0c3e9f806da", size = 200360 },
    { url = "https://files.pythonhosted.org/packages/23/41/61202663ea9b1bd8e53673b8ec9e2619989353dba8cfb68e59a9cbd9ffe3/xxhash-3.5.0-cp310-cp310-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:5d0d307d27099bb0cbeea7260eb39ed4fdb99c5542e21e94bb6fd29e49c57a23", size = 428528 },
    { url = "https://files.pythonhosted.org/packages/f2/07/d9a3059f702dec5b3b703737afb6dda32f304f6e9da181a229dafd052c29/xxhash-3.5.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:c0342aafd421795d740e514bc9858ebddfc705a75a8c5046ac56d85fe97bf196", size = 194149 },
    { url = "https://files.pythonhosted.org/packages/eb/58/27caadf78226ecf1d62dbd0c01d152ed381c14c1ee4ad01f0d460fc40eac/xxhash-3.5.0-cp310-cp310-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:3dbbd9892c5ebffeca1ed620cf0ade13eb55a0d8c84e0751a6653adc6ac40d0c", size = 207703 },
    { url = "https://files.pythonhosted.org/packages/b1/08/32d558ce23e1e068453c39aed7b3c1cdc690c177873ec0ca3a90d5808765/xxhash-3.5.0-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:4cc2d67fdb4d057730c75a64c5923abfa17775ae234a71b0200346bfb0a7f482", size = 216255 },
    { url = "https://files.pythonhosted.org/packages/3f/d4/2b971e2d2b0a61045f842b622ef11e94096cf1f12cd448b6fd426e80e0e2/xxhash-3.5.0-cp310-cp310-musllinux_1_2_i686.whl", hash = "sha256:ec28adb204b759306a3d64358a5e5c07d7b1dd0ccbce04aa76cb9377b7b70296", size = 202744 },
    { url = "https://files.pythonhosted.org/packages/19/ae/6a6438864a8c4c39915d7b65effd85392ebe22710412902487e51769146d/xxhash-3.5.0-cp310-cp310-musllinux_1_2_ppc64le.whl", hash = "sha256:1328f6d8cca2b86acb14104e381225a3d7b42c92c4b86ceae814e5c400dbb415", size = 210115 },
    { url = "https://files.pythonhosted.org/packages/48/7d/b3c27c27d1fc868094d02fe4498ccce8cec9fcc591825c01d6bcb0b4fc49/xxhash-3.5.0-cp310-cp310-musllinux_1_2_s390x.whl", hash = "sha256:8d47ebd9f5d9607fd039c1fbf4994e3b071ea23eff42f4ecef246ab2b7334198", size = 414247 },
    { url = "https://files.pythonhosted.org/packages/a1/05/918f9e7d2fbbd334b829997045d341d6239b563c44e683b9a7ef8fe50f5d/xxhash-3.5.0-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:b96d559e0fcddd3343c510a0fe2b127fbff16bf346dd76280b82292567523442", size = 191419 },
    { url = "https://files.pythonhosted.org/packages/08/29/dfe393805b2f86bfc47c290b275f0b7c189dc2f4e136fd4754f32eb18a8d/xxhash-3.5.0-cp310-cp310-win32.whl", hash = "sha256:61c722ed8d49ac9bc26c7071eeaa1f6ff24053d553146d5df031802deffd03da", size = 30114 },
    { url = "https://files.pythonhosted.org/packages/7b/d7/aa0b22c4ebb7c3ccb993d4c565132abc641cd11164f8952d89eb6a501909/xxhash-3.5.0-cp310-cp310-win_amd64.whl", hash = "sha256:9bed5144c6923cc902cd14bb8963f2d5e034def4486ab0bbe1f58f03f042f9a9", size = 30003 },
    { url = "https://files.pythonhosted.org/packages/69/12/f969b81541ee91b55f1ce469d7ab55079593c80d04fd01691b550e535000/xxhash-3.5.0-cp310-cp310-win_arm64.whl", hash = "sha256:893074d651cf25c1cc14e3bea4fceefd67f2921b1bb8e40fcfeba56820de80c6", size = 26773 },
    { url = "https://files.pythonhosted.org/packages/b8/c7/afed0f131fbda960ff15eee7f304fa0eeb2d58770fade99897984852ef23/xxhash-3.5.0-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:02c2e816896dc6f85922ced60097bcf6f008dedfc5073dcba32f9c8dd786f3c1", size = 31969 },
    { url = "https://files.pythonhosted.org/packages/8c/0c/7c3bc6d87e5235672fcc2fb42fd5ad79fe1033925f71bf549ee068c7d1ca/xxhash-3.5.0-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:6027dcd885e21581e46d3c7f682cfb2b870942feeed58a21c29583512c3f09f8", size = 30800 },
    { url = "https://files.pythonhosted.org/packages/04/9e/01067981d98069eec1c20201f8c145367698e9056f8bc295346e4ea32dd1/xxhash-3.5.0-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:1308fa542bbdbf2fa85e9e66b1077eea3a88bef38ee8a06270b4298a7a62a166", size = 221566 },
    { url = "https://files.pythonhosted.org/packages/d4/09/d4996de4059c3ce5342b6e1e6a77c9d6c91acce31f6ed979891872dd162b/xxhash-3.5.0-cp311-cp311-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:c28b2fdcee797e1c1961cd3bcd3d545cab22ad202c846235197935e1df2f8ef7", size = 201214 },
    { url = "https://files.pythonhosted.org/packages/62/f5/6d2dc9f8d55a7ce0f5e7bfef916e67536f01b85d32a9fbf137d4cadbee38/xxhash-3.5.0-cp311-cp311-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:924361811732ddad75ff23e90efd9ccfda4f664132feecb90895bade6a1b4623", size = 429433 },
    { url = "https://files.pythonhosted.org/packages/d9/72/9256303f10e41ab004799a4aa74b80b3c5977d6383ae4550548b24bd1971/xxhash-3.5.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:89997aa1c4b6a5b1e5b588979d1da048a3c6f15e55c11d117a56b75c84531f5a", size = 194822 },
    { url = "https://files.pythonhosted.org/packages/34/92/1a3a29acd08248a34b0e6a94f4e0ed9b8379a4ff471f1668e4dce7bdbaa8/xxhash-3.5.0-cp311-cp311-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:685c4f4e8c59837de103344eb1c8a3851f670309eb5c361f746805c5471b8c88", size = 208538 },
    { url = "https://files.pythonhosted.org/packages/53/ad/7fa1a109663366de42f724a1cdb8e796a260dbac45047bce153bc1e18abf/xxhash-3.5.0-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:dbd2ecfbfee70bc1a4acb7461fa6af7748ec2ab08ac0fa298f281c51518f982c", size = 216953 },
    { url = "https://files.pythonhosted.org/packages/35/02/137300e24203bf2b2a49b48ce898ecce6fd01789c0fcd9c686c0a002d129/xxhash-3.5.0-cp311-cp311-musllinux_1_2_i686.whl", hash = "sha256:25b5a51dc3dfb20a10833c8eee25903fd2e14059e9afcd329c9da20609a307b2", size = 203594 },
    { url = "https://files.pythonhosted.org/packages/23/03/aeceb273933d7eee248c4322b98b8e971f06cc3880e5f7602c94e5578af5/xxhash-3.5.0-cp311-cp311-musllinux_1_2_ppc64le.whl", hash = "sha256:a8fb786fb754ef6ff8c120cb96629fb518f8eb5a61a16aac3a979a9dbd40a084", size = 210971 },
    { url = "https://files.pythonhosted.org/packages/e3/64/ed82ec09489474cbb35c716b189ddc1521d8b3de12b1b5ab41ce7f70253c/xxhash-3.5.0-cp311-cp311-musllinux_1_2_s390x.whl", hash = "sha256:a905ad00ad1e1c34fe4e9d7c1d949ab09c6fa90c919860c1534ff479f40fd12d", size = 415050 },
    { url = "https://files.pythonhosted.org/packages/71/43/6db4c02dcb488ad4e03bc86d70506c3d40a384ee73c9b5c93338eb1f3c23/xxhash-3.5.0-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:963be41bcd49f53af6d795f65c0da9b4cc518c0dd9c47145c98f61cb464f4839", size = 192216 },
    { url = "https://files.pythonhosted.org/packages/22/6d/db4abec29e7a567455344433d095fdb39c97db6955bb4a2c432e486b4d28/xxhash-3.5.0-cp311-cp311-win32.whl", hash = "sha256:109b436096d0a2dd039c355fa3414160ec4d843dfecc64a14077332a00aeb7da", size = 30120 },
    { url = "https://files.pythonhosted.org/packages/52/1c/fa3b61c0cf03e1da4767213672efe186b1dfa4fc901a4a694fb184a513d1/xxhash-3.5.0-cp311-cp311-win_amd64.whl", hash = "sha256:b702f806693201ad6c0a05ddbbe4c8f359626d0b3305f766077d51388a6bac58", size = 30003 },
    { url = "https://files.pythonhosted.org/packages/6b/8e/9e6fc572acf6e1cc7ccb01973c213f895cb8668a9d4c2b58a99350da14b7/xxhash-3.5.0-cp311-cp311-win_arm64.whl", hash = "sha256:c4dcb4120d0cc3cc448624147dba64e9021b278c63e34a38789b688fd0da9bf3", size = 26777 },
    { url = "https://files.pythonhosted.org/packages/07/0e/1bfce2502c57d7e2e787600b31c83535af83746885aa1a5f153d8c8059d6/xxhash-3.5.0-cp312-cp312-macosx_10_9_x86_64.whl", hash = "sha256:14470ace8bd3b5d51318782cd94e6f94431974f16cb3b8dc15d52f3b69df8e00", size = 31969 },
    { url = "https://files.pythonhosted.org/packages/3f/d6/8ca450d6fe5b71ce521b4e5db69622383d039e2b253e9b2f24f93265b52c/xxhash-3.5.0-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:59aa1203de1cb96dbeab595ded0ad0c0056bb2245ae11fac11c0ceea861382b9", size = 30787 },
    { url = "https://files.pythonhosted.org/packages/5b/84/de7c89bc6ef63d750159086a6ada6416cc4349eab23f76ab870407178b93/xxhash-3.5.0-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:08424f6648526076e28fae6ea2806c0a7d504b9ef05ae61d196d571e5c879c84", size = 220959 },
    { url = "https://files.pythonhosted.org/packages/fe/86/51258d3e8a8545ff26468c977101964c14d56a8a37f5835bc0082426c672/xxhash-3.5.0-cp312-cp312-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:61a1ff00674879725b194695e17f23d3248998b843eb5e933007ca743310f793", size = 200006 },
    { url = "https://files.pythonhosted.org/packages/02/0a/96973bd325412feccf23cf3680fd2246aebf4b789122f938d5557c54a6b2/xxhash-3.5.0-cp312-cp312-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:f2f2c61bee5844d41c3eb015ac652a0229e901074951ae48581d58bfb2ba01be", size = 428326 },
    { url = "https://files.pythonhosted.org/packages/11/a7/81dba5010f7e733de88af9555725146fc133be97ce36533867f4c7e75066/xxhash-3.5.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:9d32a592cac88d18cc09a89172e1c32d7f2a6e516c3dfde1b9adb90ab5df54a6", size = 194380 },
    { url = "https://files.pythonhosted.org/packages/fb/7d/f29006ab398a173f4501c0e4977ba288f1c621d878ec217b4ff516810c04/xxhash-3.5.0-cp312-cp312-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:70dabf941dede727cca579e8c205e61121afc9b28516752fd65724be1355cc90", size = 207934 },
    { url = "https://files.pythonhosted.org/packages/8a/6e/6e88b8f24612510e73d4d70d9b0c7dff62a2e78451b9f0d042a5462c8d03/xxhash-3.5.0-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:e5d0ddaca65ecca9c10dcf01730165fd858533d0be84c75c327487c37a906a27", size = 216301 },
    { url = "https://files.pythonhosted.org/packages/af/51/7862f4fa4b75a25c3b4163c8a873f070532fe5f2d3f9b3fc869c8337a398/xxhash-3.5.0-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:3e5b5e16c5a480fe5f59f56c30abdeba09ffd75da8d13f6b9b6fd224d0b4d0a2", size = 203351 },
    { url = "https://files.pythonhosted.org/packages/22/61/8d6a40f288f791cf79ed5bb113159abf0c81d6efb86e734334f698eb4c59/xxhash-3.5.0-cp312-cp312-musllinux_1_2_ppc64le.whl", hash = "sha256:149b7914451eb154b3dfaa721315117ea1dac2cc55a01bfbd4df7c68c5dd683d", size = 210294 },
    { url = "https://files.pythonhosted.org/packages/17/02/215c4698955762d45a8158117190261b2dbefe9ae7e5b906768c09d8bc74/xxhash-3.5.0-cp312-cp312-musllinux_1_2_s390x.whl", hash = "sha256:eade977f5c96c677035ff39c56ac74d851b1cca7d607ab3d8f23c6b859379cab", size = 414674 },
    { url = "https://files.pythonhosted.org/packages/31/5c/b7a8db8a3237cff3d535261325d95de509f6a8ae439a5a7a4ffcff478189/xxhash-3.5.0-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:fa9f547bd98f5553d03160967866a71056a60960be00356a15ecc44efb40ba8e", size = 192022 },
    { url = "https://files.pythonhosted.org/packages/78/e3/dd76659b2811b3fd06892a8beb850e1996b63e9235af5a86ea348f053e9e/xxhash-3.5.0-cp312-cp312-win32.whl", hash = "sha256:f7b58d1fd3551b8c80a971199543379be1cee3d0d409e1f6d8b01c1a2eebf1f8", size = 30170 },
    { url = "https://files.pythonhosted.org/packages/d9/6b/1c443fe6cfeb4ad1dcf231cdec96eb94fb43d6498b4469ed8b51f8b59a37/xxhash-3.5.0-cp312-cp312-win_amd64.whl", hash = "sha256:fa0cafd3a2af231b4e113fba24a65d7922af91aeb23774a8b78228e6cd785e3e", size = 30040 },
    { url = "https://files.pythonhosted.org/packages/0f/eb/04405305f290173acc0350eba6d2f1a794b57925df0398861a20fbafa415/xxhash-3.5.0-cp312-cp312-win_arm64.whl", hash = "sha256:586886c7e89cb9828bcd8a5686b12e161368e0064d040e225e72607b43858ba2", size = 26796 },
    { url = "https://files.pythonhosted.org/packages/c9/b8/e4b3ad92d249be5c83fa72916c9091b0965cb0faeff05d9a0a3870ae6bff/xxhash-3.5.0-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:37889a0d13b0b7d739cfc128b1c902f04e32de17b33d74b637ad42f1c55101f6", size = 31795 },
    { url = "https://files.pythonhosted.org/packages/fc/d8/b3627a0aebfbfa4c12a41e22af3742cf08c8ea84f5cc3367b5de2d039cce/xxhash-3.5.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:97a662338797c660178e682f3bc180277b9569a59abfb5925e8620fba00b9fc5", size = 30792 },
    { url = "https://files.pythonhosted.org/packages/c3/cc/762312960691da989c7cd0545cb120ba2a4148741c6ba458aa723c00a3f8/xxhash-3.5.0-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:7f85e0108d51092bdda90672476c7d909c04ada6923c14ff9d913c4f7dc8a3bc", size = 220950 },
    { url = "https://files.pythonhosted.org/packages/fe/e9/cc266f1042c3c13750e86a535496b58beb12bf8c50a915c336136f6168dc/xxhash-3.5.0-cp313-cp313-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:cd2fd827b0ba763ac919440042302315c564fdb797294d86e8cdd4578e3bc7f3", size = 199980 },
    { url = "https://files.pythonhosted.org/packages/bf/85/a836cd0dc5cc20376de26b346858d0ac9656f8f730998ca4324921a010b9/xxhash-3.5.0-cp313-cp313-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:82085c2abec437abebf457c1d12fccb30cc8b3774a0814872511f0f0562c768c", size = 428324 },
    { url = "https://files.pythonhosted.org/packages/b4/0e/15c243775342ce840b9ba34aceace06a1148fa1630cd8ca269e3223987f5/xxhash-3.5.0-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:07fda5de378626e502b42b311b049848c2ef38784d0d67b6f30bb5008642f8eb", size = 194370 },
    { url = "https://files.pythonhosted.org/packages/87/a1/b028bb02636dfdc190da01951d0703b3d904301ed0ef6094d948983bef0e/xxhash-3.5.0-cp313-cp313-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:c279f0d2b34ef15f922b77966640ade58b4ccdfef1c4d94b20f2a364617a493f", size = 207911 },
    { url = "https://files.pythonhosted.org/packages/80/d5/73c73b03fc0ac73dacf069fdf6036c9abad82de0a47549e9912c955ab449/xxhash-3.5.0-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:89e66ceed67b213dec5a773e2f7a9e8c58f64daeb38c7859d8815d2c89f39ad7", size = 216352 },
    { url = "https://files.pythonhosted.org/packages/b6/2a/5043dba5ddbe35b4fe6ea0a111280ad9c3d4ba477dd0f2d1fe1129bda9d0/xxhash-3.5.0-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:bcd51708a633410737111e998ceb3b45d3dbc98c0931f743d9bb0a209033a326", size = 203410 },
    { url = "https://files.pythonhosted.org/packages/a2/b2/9a8ded888b7b190aed75b484eb5c853ddd48aa2896e7b59bbfbce442f0a1/xxhash-3.5.0-cp313-cp313-musllinux_1_2_ppc64le.whl", hash = "sha256:3ff2c0a34eae7df88c868be53a8dd56fbdf592109e21d4bfa092a27b0bf4a7bf", size = 210322 },
    { url = "https://files.pythonhosted.org/packages/98/62/440083fafbc917bf3e4b67c2ade621920dd905517e85631c10aac955c1d2/xxhash-3.5.0-cp313-cp313-musllinux_1_2_s390x.whl", hash = "sha256:4e28503dccc7d32e0b9817aa0cbfc1f45f563b2c995b7a66c4c8a0d232e840c7", size = 414725 },
    { url = "https://files.pythonhosted.org/packages/75/db/009206f7076ad60a517e016bb0058381d96a007ce3f79fa91d3010f49cc2/xxhash-3.5.0-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:a6c50017518329ed65a9e4829154626f008916d36295b6a3ba336e2458824c8c", size = 192070 },
    { url = "https://files.pythonhosted.org/packages/1f/6d/c61e0668943a034abc3a569cdc5aeae37d686d9da7e39cf2ed621d533e36/xxhash-3.5.0-cp313-cp313-win32.whl", hash = "sha256:53a068fe70301ec30d868ece566ac90d873e3bb059cf83c32e76012c889b8637", size = 30172 },
    { url = "https://files.pythonhosted.org/packages/96/14/8416dce965f35e3d24722cdf79361ae154fa23e2ab730e5323aa98d7919e/xxhash-3.5.0-cp313-cp313-win_amd64.whl", hash = "sha256:80babcc30e7a1a484eab952d76a4f4673ff601f54d5142c26826502740e70b43", size = 30041 },
    { url = "https://files.pythonhosted.org/packages/27/ee/518b72faa2073f5aa8e3262408d284892cb79cf2754ba0c3a5870645ef73/xxhash-3.5.0-cp313-cp313-win_arm64.whl", hash = "sha256:4811336f1ce11cac89dcbd18f3a25c527c16311709a89313c3acaf771def2d4b", size = 26801 },
    { url = "https://files.pythonhosted.org/packages/d4/f6/531dd6858adf8877675270b9d6989b6dacfd1c2d7135b17584fc29866df3/xxhash-3.5.0-cp39-cp39-macosx_10_9_x86_64.whl", hash = "sha256:bfc8cdd7f33d57f0468b0614ae634cc38ab9202c6957a60e31d285a71ebe0301", size = 31971 },
    { url = "https://files.pythonhosted.org/packages/7c/a8/b2a42b6c9ae46e233f474f3d307c2e7bca8d9817650babeca048d2ad01d6/xxhash-3.5.0-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:e0c48b6300cd0b0106bf49169c3e0536408dfbeb1ccb53180068a18b03c662ab", size = 30801 },
    { url = "https://files.pythonhosted.org/packages/b4/92/9ac297e3487818f429bcf369c1c6a097edf5b56ed6fc1feff4c1882e87ef/xxhash-3.5.0-cp39-cp39-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:fe1a92cfbaa0a1253e339ccec42dbe6db262615e52df591b68726ab10338003f", size = 220644 },
    { url = "https://files.pythonhosted.org/packages/86/48/c1426dd3c86fc4a52f983301867463472f6a9013fb32d15991e60c9919b6/xxhash-3.5.0-cp39-cp39-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:33513d6cc3ed3b559134fb307aae9bdd94d7e7c02907b37896a6c45ff9ce51bd", size = 200021 },
    { url = "https://files.pythonhosted.org/packages/f3/de/0ab8c79993765c94fc0d0c1a22b454483c58a0161e1b562f58b654f47660/xxhash-3.5.0-cp39-cp39-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:eefc37f6138f522e771ac6db71a6d4838ec7933939676f3753eafd7d3f4c40bc", size = 428217 },
    { url = "https://files.pythonhosted.org/packages/b4/b4/332647451ed7d2c021294b7c1e9c144dbb5586b1fb214ad4f5a404642835/xxhash-3.5.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:a606c8070ada8aa2a88e181773fa1ef17ba65ce5dd168b9d08038e2a61b33754", size = 193868 },
    { url = "https://files.pythonhosted.org/packages/f4/1c/a42c0a6cac752f84f7b44a90d1a9fa9047cf70bdba5198a304fde7cc471f/xxhash-3.5.0-cp39-cp39-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:42eca420c8fa072cc1dd62597635d140e78e384a79bb4944f825fbef8bfeeef6", size = 207403 },
    { url = "https://files.pythonhosted.org/packages/c4/d7/04e1b0daae9dc9b02c73c1664cc8aa527498c3f66ccbc586eeb25bbe9f14/xxhash-3.5.0-cp39-cp39-musllinux_1_2_aarch64.whl", hash = "sha256:604253b2143e13218ff1ef0b59ce67f18b8bd1c4205d2ffda22b09b426386898", size = 215978 },
    { url = "https://files.pythonhosted.org/packages/c4/f4/05e15e67505228fc19ee98a79e427b3a0b9695f5567cd66ced5d66389883/xxhash-3.5.0-cp39-cp39-musllinux_1_2_i686.whl", hash = "sha256:6e93a5ad22f434d7876665444a97e713a8f60b5b1a3521e8df11b98309bff833", size = 202416 },
    { url = "https://files.pythonhosted.org/packages/94/fb/e9028d3645bba5412a09de13ee36df276a567e60bdb31d499dafa46d76ae/xxhash-3.5.0-cp39-cp39-musllinux_1_2_ppc64le.whl", hash = "sha256:7a46e1d6d2817ba8024de44c4fd79913a90e5f7265434cef97026215b7d30df6", size = 209853 },
    { url = "https://files.pythonhosted.org/packages/02/2c/18c6a622429368274739372d2f86c8125413ec169025c7d8ffb051784bba/xxhash-3.5.0-cp39-cp39-musllinux_1_2_s390x.whl", hash = "sha256:30eb2efe6503c379b7ab99c81ba4a779748e3830241f032ab46bd182bf5873af", size = 413926 },
    { url = "https://files.pythonhosted.org/packages/72/bb/5b55c391084a0321c3809632a018b9b657e59d5966289664f85a645942ac/xxhash-3.5.0-cp39-cp39-musllinux_1_2_x86_64.whl", hash = "sha256:c8aa771ff2c13dd9cda8166d685d7333d389fae30a4d2bb39d63ab5775de8606", size = 191156 },
    { url = "https://files.pythonhosted.org/packages/86/2b/915049db13401792fec159f57e4f4a5ca7a9768e83ef71d6645b9d0cd749/xxhash-3.5.0-cp39-cp39-win32.whl", hash = "sha256:5ed9ebc46f24cf91034544b26b131241b699edbfc99ec5e7f8f3d02d6eb7fba4", size = 30122 },
    { url = "https://files.pythonhosted.org/packages/d5/87/382ef7b24917d7cf4c540ee30f29b283bc87ac5893d2f89b23ea3cdf7d77/xxhash-3.5.0-cp39-cp39-win_amd64.whl", hash = "sha256:220f3f896c6b8d0316f63f16c077d52c412619e475f9372333474ee15133a558", size = 30021 },
    { url = "https://files.pythonhosted.org/packages/e2/47/d06b24e2d9c3dcabccfd734d11b5bbebfdf59ceac2c61509d8205dd20ac6/xxhash-3.5.0-cp39-cp39-win_arm64.whl", hash = "sha256:a7b1d8315d9b5e9f89eb2933b73afae6ec9597a258d52190944437158b49d38e", size = 26780 },
    { url = "https://files.pythonhosted.org/packages/ab/9a/233606bada5bd6f50b2b72c45de3d9868ad551e83893d2ac86dc7bb8553a/xxhash-3.5.0-pp310-pypy310_pp73-macosx_10_15_x86_64.whl", hash = "sha256:2014c5b3ff15e64feecb6b713af12093f75b7926049e26a580e94dcad3c73d8c", size = 29732 },
    { url = "https://files.pythonhosted.org/packages/0c/67/f75276ca39e2c6604e3bee6c84e9db8a56a4973fde9bf35989787cf6e8aa/xxhash-3.5.0-pp310-pypy310_pp73-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:fab81ef75003eda96239a23eda4e4543cedc22e34c373edcaf744e721a163986", size = 36214 },
    { url = "https://files.pythonhosted.org/packages/0f/f8/f6c61fd794229cc3848d144f73754a0c107854372d7261419dcbbd286299/xxhash-3.5.0-pp310-pypy310_pp73-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:4e2febf914ace002132aa09169cc572e0d8959d0f305f93d5828c4836f9bc5a6", size = 32020 },
    { url = "https://files.pythonhosted.org/packages/79/d3/c029c99801526f859e6b38d34ab87c08993bf3dcea34b11275775001638a/xxhash-3.5.0-pp310-pypy310_pp73-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:5d3a10609c51da2a1c0ea0293fc3968ca0a18bd73838455b5bca3069d7f8e32b", size = 40515 },
    { url = "https://files.pythonhosted.org/packages/62/e3/bef7b82c1997579c94de9ac5ea7626d01ae5858aa22bf4fcb38bf220cb3e/xxhash-3.5.0-pp310-pypy310_pp73-win_amd64.whl", hash = "sha256:5a74f23335b9689b66eb6dbe2a931a88fcd7a4c2cc4b1cb0edba8ce381c7a1da", size = 30064 },
    { url = "https://files.pythonhosted.org/packages/c2/56/30d3df421814947f9d782b20c9b7e5e957f3791cbd89874578011daafcbd/xxhash-3.5.0-pp39-pypy39_pp73-macosx_10_15_x86_64.whl", hash = "sha256:531af8845aaadcadf951b7e0c1345c6b9c68a990eeb74ff9acd8501a0ad6a1c9", size = 29734 },
    { url = "https://files.pythonhosted.org/packages/82/dd/3c42a1f022ad0d82c852d3cb65493ebac03dcfa8c994465a5fb052b00e3c/xxhash-3.5.0-pp39-pypy39_pp73-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:7ce379bcaa9fcc00f19affa7773084dd09f5b59947b3fb47a1ceb0179f91aaa1", size = 36216 },
    { url = "https://files.pythonhosted.org/packages/b2/40/8f902ab3bebda228a9b4de69eba988280285a7f7f167b942bc20bb562df9/xxhash-3.5.0-pp39-pypy39_pp73-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:fd1b2281d01723f076df3c8188f43f2472248a6b63118b036e641243656b1b0f", size = 32042 },
    { url = "https://files.pythonhosted.org/packages/db/87/bd06beb8ccaa0e9e577c9b909a49cfa5c5cd2ca46034342d72dd9ce5bc56/xxhash-3.5.0-pp39-pypy39_pp73-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:9c770750cc80e8694492244bca7251385188bc5597b6a39d98a9f30e8da984e0", size = 40516 },
    { url = "https://files.pythonhosted.org/packages/bb/f8/505385e2fbd753ddcaafd5550eabe86f6232cbebabad3b2508d411b19153/xxhash-3.5.0-pp39-pypy39_pp73-win_amd64.whl", hash = "sha256:b150b8467852e1bd844387459aa6fbe11d7f38b56e901f9f3b3e6aba0d660240", size = 30108 },
]

[[package]]
name = "yarl"
version = "1.19.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "idna" },
    { name = "multidict" },
    { name = "propcache" },
]
sdist = { url = "https://files.pythonhosted.org/packages/fc/4d/8a8f57caccce49573e567744926f88c6ab3ca0b47a257806d1cf88584c5f/yarl-1.19.0.tar.gz", hash = "sha256:01e02bb80ae0dbed44273c304095295106e1d9470460e773268a27d11e594892", size = 184396 }
wheels = [
    { url = "https://files.pythonhosted.org/packages/96/0f/e5bd0d7d98bb194a30740dea2c4324f85dfc2f8daba9d7bc7e47b45d1034/yarl-1.19.0-cp310-cp310-macosx_10_9_universal2.whl", hash = "sha256:0bae32f8ebd35c04d6528cedb4a26b8bf25339d3616b04613b97347f919b76d3", size = 144954 },
    { url = "https://files.pythonhosted.org/packages/07/bf/2acc4b643dbdfc823d0d2058768197198a3d93b41fffb41b83359c520a4d/yarl-1.19.0-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:8015a076daf77823e7ebdcba474156587391dab4e70c732822960368c01251e6", size = 96613 },
    { url = "https://files.pythonhosted.org/packages/ca/38/c60ccca9aad0bb939e665b63a4e1550fecc922971f1f246dd7ad709a1a72/yarl-1.19.0-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:9973ac95327f5d699eb620286c39365990b240031672b5c436a4cd00539596c5", size = 94408 },
    { url = "https://files.pythonhosted.org/packages/9a/43/2d5b49b4784743d88054e612a97aee2a9d2d463983c6a8e2fa4c872b294a/yarl-1.19.0-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:fd4b5fbd7b9dde785cfeb486b8cca211a0b138d4f3a7da27db89a25b3c482e5c", size = 330774 },
    { url = "https://files.pythonhosted.org/packages/3b/48/7decce219b6eedce321345f61461ee140ee6b3faf4875efe518f0e7b5817/yarl-1.19.0-cp310-cp310-manylinux_2_17_armv7l.manylinux2014_armv7l.manylinux_2_31_armv7l.whl", hash = "sha256:75460740005de5a912b19f657848aef419387426a40f581b1dc9fac0eb9addb5", size = 323399 },
    { url = "https://files.pythonhosted.org/packages/67/2f/d6253528e49ce1c6f5119ec5269314752b06dd670f5a81721648d98b1dc7/yarl-1.19.0-cp310-cp310-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:57abd66ca913f2cfbb51eb3dbbbac3648f1f6983f614a4446e0802e241441d2a", size = 343329 },
    { url = "https://files.pythonhosted.org/packages/fc/6b/efeb1a088e8addbf5841a84b74dad2a06346b0e4a712eb269a0cd9ada8b7/yarl-1.19.0-cp310-cp310-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:46ade37911b7c99ce28a959147cb28bffbd14cea9e7dd91021e06a8d2359a5aa", size = 338275 },
    { url = "https://files.pythonhosted.org/packages/a6/b6/31acc2efcaf6999fd256d11f26ccc95ea773bc790ad1973331d7294b25db/yarl-1.19.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:8346ec72ada749a6b5d82bff7be72578eab056ad7ec38c04f668a685abde6af0", size = 334014 },
    { url = "https://files.pythonhosted.org/packages/79/16/1deb54324842479e4d8b34841a383653587dfcc403c132f88b493f0c513e/yarl-1.19.0-cp310-cp310-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:7e4cb14a6ee5b6649ccf1c6d648b4da9220e8277d4d4380593c03cc08d8fe937", size = 322007 },
    { url = "https://files.pythonhosted.org/packages/80/77/4a073cec4f40ce84897510ee9d347bc10128f715be59b36e5c037463523b/yarl-1.19.0-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:66fc1c2926a73a2fb46e4b92e3a6c03904d9bc3a0b65e01cb7d2b84146a8bd3b", size = 336569 },
    { url = "https://files.pythonhosted.org/packages/73/e1/2f0455379bbee5f4ece8bc0968106386ec4e74237e8d68ced00bbff0a1fc/yarl-1.19.0-cp310-cp310-musllinux_1_2_armv7l.whl", hash = "sha256:5a70201dd1e0a4304849b6445a9891d7210604c27e67da59091d5412bc19e51c", size = 336384 },
    { url = "https://files.pythonhosted.org/packages/74/e0/307aa8ae96bc0e72644855c76e8960019fc24c511a5dda73f05214da46f0/yarl-1.19.0-cp310-cp310-musllinux_1_2_i686.whl", hash = "sha256:e4807aab1bdeab6ae6f296be46337a260ae4b1f3a8c2fcd373e236b4b2b46efd", size = 340454 },
    { url = "https://files.pythonhosted.org/packages/af/19/2dcdb1e5eef26751c9e79369d1f80d6a1162dababb5070f62bc5b1a8f81e/yarl-1.19.0-cp310-cp310-musllinux_1_2_ppc64le.whl", hash = "sha256:ae584afe81a1de4c1bb06672481050f0d001cad13163e3c019477409f638f9b7", size = 355804 },
    { url = "https://files.pythonhosted.org/packages/c1/af/8c1e102c6d61713ed31022ab8f8866d263b87cb8f466c37f20a99019d169/yarl-1.19.0-cp310-cp310-musllinux_1_2_s390x.whl", hash = "sha256:30eaf4459df6e91f21b2999d1ee18f891bcd51e3cbe1de301b4858c84385895b", size = 359877 },
    { url = "https://files.pythonhosted.org/packages/1a/cf/c3c4bd85ecc7f189e14d21c3bea67ce389511d9178a302d97281868477aa/yarl-1.19.0-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:0e617d45d03c8dec0dfce6f51f3e1b8a31aa81aaf4a4d1442fdb232bcf0c6d8c", size = 351282 },
    { url = "https://files.pythonhosted.org/packages/c6/85/0994f1c607b0520ef007717ff74f3317df3f7b7f32756ba2bf26c0c58ddf/yarl-1.19.0-cp310-cp310-win32.whl", hash = "sha256:32ba32d0fa23893fd8ea8d05bdb05de6eb19d7f2106787024fd969f4ba5466cb", size = 86529 },
    { url = "https://files.pythonhosted.org/packages/59/00/39bc8da1f67614633a099a44a5f69d056bb4d65a8e52a4003460e3fa4cc7/yarl-1.19.0-cp310-cp310-win_amd64.whl", hash = "sha256:545575ecfcd465891b51546c2bcafdde0acd2c62c2097d8d71902050b20e4922", size = 92707 },
    { url = "https://files.pythonhosted.org/packages/9b/df/5fa7cd75e46306e0f9baf38a7c8969ff6730ea503b86232e85cb740304cf/yarl-1.19.0-cp311-cp311-macosx_10_9_universal2.whl", hash = "sha256:163ff326680de5f6d4966954cf9e3fe1bf980f5fee2255e46e89b8cf0f3418b5", size = 145126 },
    { url = "https://files.pythonhosted.org/packages/2a/be/c1b52129cd2166ab7337f08e701a61baa7c260c7b03b534098cc8297aecc/yarl-1.19.0-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:a626c4d9cca298d1be8625cff4b17004a9066330ac82d132bbda64a4c17c18d3", size = 96691 },
    { url = "https://files.pythonhosted.org/packages/8d/39/ad62139b45515f9bf129c805aeaaedf86fd93ae57ffe911f4caeabef3e74/yarl-1.19.0-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:961c3e401ea7f13d02b8bb7cb0c709152a632a6e14cdc8119e9c6ee5596cd45d", size = 94505 },
    { url = "https://files.pythonhosted.org/packages/be/be/04e3202cdc9bb5f81761e327af7095cffb0d81e32421a6b87f926052d2ae/yarl-1.19.0-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:a39d7b807ab58e633ed760f80195cbd145b58ba265436af35f9080f1810dfe64", size = 355485 },
    { url = "https://files.pythonhosted.org/packages/00/7d/1463203663ca1ae62af8fb9ebc9601dd07f04dbced7edb1df3141a2cb2fe/yarl-1.19.0-cp311-cp311-manylinux_2_17_armv7l.manylinux2014_armv7l.manylinux_2_31_armv7l.whl", hash = "sha256:c4228978fb59c6b10f60124ba8e311c26151e176df364e996f3f8ff8b93971b5", size = 344569 },
    { url = "https://files.pythonhosted.org/packages/b0/1b/5263203017348669e637bb73856fb9632110538e92d5e9f8214fcc764da9/yarl-1.19.0-cp311-cp311-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:9ba536b17ecf3c74a94239ec1137a3ad3caea8c0e4deb8c8d2ffe847d870a8c5", size = 371426 },
    { url = "https://files.pythonhosted.org/packages/78/59/90ca5f16d56b7741e5383951acc2e065fce41920eb5d8fda3065b5e288dc/yarl-1.19.0-cp311-cp311-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:a251e00e445d2e9df7b827c9843c0b87f58a3254aaa3f162fb610747491fe00f", size = 368102 },
    { url = "https://files.pythonhosted.org/packages/84/f2/5e33aa0251ffd2c2a9041bf887e163eeefdc1dca238fdabac444d9463c3f/yarl-1.19.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:f9b92431d8b4d4ca5ccbfdbac95b05a3a6cd70cd73aa62f32f9627acfde7549c", size = 358740 },
    { url = "https://files.pythonhosted.org/packages/22/9e/ba92d234c81cf94495fc01eaa0b6000175733f76bd63e60ff748bce22c81/yarl-1.19.0-cp311-cp311-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:ec2f56edaf476f70b5831bbd59700b53d9dd011b1f77cd4846b5ab5c5eafdb3f", size = 346965 },
    { url = "https://files.pythonhosted.org/packages/8d/0b/d4f53136ef12ddad540855a886d7503a6cc17cfabb9a03ce0c179f3b9e51/yarl-1.19.0-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:acf9b92c4245ac8b59bc7ec66a38d3dcb8d1f97fac934672529562bb824ecadb", size = 368547 },
    { url = "https://files.pythonhosted.org/packages/31/4b/35ec8622908a728f378a8511f0ab2d47878b2c0b8cbe035f2d907914a5fc/yarl-1.19.0-cp311-cp311-musllinux_1_2_armv7l.whl", hash = "sha256:57711f1465c06fee8825b95c0b83e82991e6d9425f9a042c3c19070a70ac92bf", size = 357610 },
    { url = "https://files.pythonhosted.org/packages/c1/71/1f39f7c55b0684834d945a2bcfdfe59e6e02ca2483a3d33c2f77a0c3b177/yarl-1.19.0-cp311-cp311-musllinux_1_2_i686.whl", hash = "sha256:528e86f5b1de0ad8dd758ddef4e0ed24f5d946d4a1cef80ffb2d4fca4e10f122", size = 365331 },
    { url = "https://files.pythonhosted.org/packages/2e/13/57675964de5c8ccf6427df93ac97f9bb7328f3f8f7ebc31a5f5a286ab1c0/yarl-1.19.0-cp311-cp311-musllinux_1_2_ppc64le.whl", hash = "sha256:3b77173663e075d9e5a57e09d711e9da2f3266be729ecca0b8ae78190990d260", size = 378624 },
    { url = "https://files.pythonhosted.org/packages/d4/c6/5868e40f8da041ed0c3b5fd8c08cece849d9f609e970e6043308767fbb60/yarl-1.19.0-cp311-cp311-musllinux_1_2_s390x.whl", hash = "sha256:d8717924cf0a825b62b1a96fc7d28aab7f55a81bf5338b8ef41d7a76ab9223e9", size = 383981 },
    { url = "https://files.pythonhosted.org/packages/f4/3f/e40124c986d96741d3d341ffac35be42b6df82ef8c18b5984ca2e7d838dd/yarl-1.19.0-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:0df9f0221a78d858793f40cbea3915c29f969c11366646a92ca47e080a14f881", size = 378868 },
    { url = "https://files.pythonhosted.org/packages/01/eb/caf2774c770288bd87a818b11f3a56ada6a855f1987d93421aae01a175bf/yarl-1.19.0-cp311-cp311-win32.whl", hash = "sha256:8b3ade62678ee2c7c10dcd6be19045135e9badad53108f7d2ed14896ee396045", size = 86446 },
    { url = "https://files.pythonhosted.org/packages/4a/97/d4fe6168c1bb789507ffeb58c2e8c675a7e71de732dc02e12bda904c1362/yarl-1.19.0-cp311-cp311-win_amd64.whl", hash = "sha256:0626ee31edb23ac36bdffe607231de2cca055ad3a5e2dc5da587ef8bc6a321bc", size = 93121 },
    { url = "https://files.pythonhosted.org/packages/b8/70/44ef8f69d61cb5123167a4dda87f6c739a833fbdb2ed52960b4e8409d65c/yarl-1.19.0-cp312-cp312-macosx_10_13_universal2.whl", hash = "sha256:7b687c334da3ff8eab848c9620c47a253d005e78335e9ce0d6868ed7e8fd170b", size = 146855 },
    { url = "https://files.pythonhosted.org/packages/c3/94/38c14d6c8217cc818647689f2dd647b976ced8fea08d0ac84e3c8168252b/yarl-1.19.0-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:b0fe766febcf523a2930b819c87bb92407ae1368662c1bc267234e79b20ff894", size = 97523 },
    { url = "https://files.pythonhosted.org/packages/35/a5/43a613586a6255105c4655a911c307ef3420e49e540d6ae2c5829863fb25/yarl-1.19.0-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:742ceffd3c7beeb2b20d47cdb92c513eef83c9ef88c46829f88d5b06be6734ee", size = 95540 },
    { url = "https://files.pythonhosted.org/packages/d4/60/ed26049f4a8b06ebfa6d5f3cb6a51b152fd57081aa818b6497474f65a631/yarl-1.19.0-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:2af682a1e97437382ee0791eacbf540318bd487a942e068e7e0a6c571fadbbd3", size = 344386 },
    { url = "https://files.pythonhosted.org/packages/49/a6/b84899cab411f49af5986cfb44b514040788d81c8084f5811e6a7c0f1ce6/yarl-1.19.0-cp312-cp312-manylinux_2_17_armv7l.manylinux2014_armv7l.manylinux_2_31_armv7l.whl", hash = "sha256:63702f1a098d0eaaea755e9c9d63172be1acb9e2d4aeb28b187092bcc9ca2d17", size = 338889 },
    { url = "https://files.pythonhosted.org/packages/cc/ce/0704f7166a781b1f81bdd45c4f49eadbae0230ebd35b9ec7cd7769d3a6ff/yarl-1.19.0-cp312-cp312-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:3560dcba3c71ae7382975dc1e912ee76e50b4cd7c34b454ed620d55464f11876", size = 353107 },
    { url = "https://files.pythonhosted.org/packages/75/e5/0ecd6f2a9cc4264c16d8dfb0d3d71ba8d03cb58f3bcd42b1df4358331189/yarl-1.19.0-cp312-cp312-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:68972df6a0cc47c8abaf77525a76ee5c5f6ea9bbdb79b9565b3234ded3c5e675", size = 353128 },
    { url = "https://files.pythonhosted.org/packages/ad/c7/cd0fd1de581f1c2e8f996e704c9fd979e00106f18eebd91b0173cf1a13c6/yarl-1.19.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:5684e7ff93ea74e47542232bd132f608df4d449f8968fde6b05aaf9e08a140f9", size = 349107 },
    { url = "https://files.pythonhosted.org/packages/e6/34/ba3e5a20bd1d6a09034fc7985aaf1309976f2a7a5aefd093c9e56f6e1e0c/yarl-1.19.0-cp312-cp312-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:8182ad422bfacdebd4759ce3adc6055c0c79d4740aea1104e05652a81cd868c6", size = 335144 },
    { url = "https://files.pythonhosted.org/packages/1e/98/d9b7beb932fade015906efe0980aa7d522b8f93cf5ebf1082e74faa314b7/yarl-1.19.0-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:aee5b90a5a9b71ac57400a7bdd0feaa27c51e8f961decc8d412e720a004a1791", size = 360795 },
    { url = "https://files.pythonhosted.org/packages/9a/11/70b8770039cc54af5948970591517a1e1d093df3f04f328c655c9a0fefb7/yarl-1.19.0-cp312-cp312-musllinux_1_2_armv7l.whl", hash = "sha256:8c0b2371858d5a814b08542d5d548adb03ff2d7ab32f23160e54e92250961a72", size = 360140 },
    { url = "https://files.pythonhosted.org/packages/d4/67/708e3e36fafc4d9d96b4eecc6c8b9f37c8ad50df8a16c7a1d5ba9df53050/yarl-1.19.0-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:cd430c2b7df4ae92498da09e9b12cad5bdbb140d22d138f9e507de1aa3edfea3", size = 364431 },
    { url = "https://files.pythonhosted.org/packages/c3/8b/937fbbcc895553a7e16fcd86ae4e0724c6ac9468237ad8e7c29cc3b1c9d9/yarl-1.19.0-cp312-cp312-musllinux_1_2_ppc64le.whl", hash = "sha256:a93208282c0ccdf73065fd76c6c129bd428dba5ff65d338ae7d2ab27169861a0", size = 373832 },
    { url = "https://files.pythonhosted.org/packages/f8/ca/288ddc2230c9b6647fe907504f1119adb41252ac533eb564d3fc73511215/yarl-1.19.0-cp312-cp312-musllinux_1_2_s390x.whl", hash = "sha256:b8179280cdeb4c36eb18d6534a328f9d40da60d2b96ac4a295c5f93e2799e9d9", size = 378122 },
    { url = "https://files.pythonhosted.org/packages/4f/5a/79e1ef31d14968fbfc0ecec70a6683b574890d9c7550c376dd6d40de7754/yarl-1.19.0-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:eda3c2b42dc0c389b7cfda2c4df81c12eeb552019e0de28bde8f913fc3d1fcf3", size = 375178 },
    { url = "https://files.pythonhosted.org/packages/95/38/9b0e56bf14026c3f550ad6425679f6d1a2f4821d70767f39d6f4c56a0820/yarl-1.19.0-cp312-cp312-win32.whl", hash = "sha256:57f3fed859af367b9ca316ecc05ce79ce327d6466342734305aa5cc380e4d8be", size = 86172 },
    { url = "https://files.pythonhosted.org/packages/b3/96/5c2f3987c4bb4e5cdebea3caf99a45946b13a9516f849c02222203d99860/yarl-1.19.0-cp312-cp312-win_amd64.whl", hash = "sha256:5507c1f7dd3d41251b67eecba331c8b2157cfd324849879bebf74676ce76aff7", size = 92617 },
    { url = "https://files.pythonhosted.org/packages/cd/a7/222144efa2f4a47363a5fee27d8a1d24851283b5a7f628890805fe7f7a66/yarl-1.19.0-cp313-cp313-macosx_10_13_universal2.whl", hash = "sha256:59281b9ed27bc410e0793833bcbe7fc149739d56ffa071d1e0fe70536a4f7b61", size = 144789 },
    { url = "https://files.pythonhosted.org/packages/72/4f/3ee8de3f94baa33c0716260b0048b1fd5306f104b3efc6e1713693e7063e/yarl-1.19.0-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:d27a6482ad5e05e8bafd47bf42866f8a1c0c3345abcb48d4511b3c29ecc197dc", size = 96685 },
    { url = "https://files.pythonhosted.org/packages/3e/7c/fbeebf875c1ededd872d6fefabd8a8526ef8aba6e9e8bcdf230d895d487b/yarl-1.19.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:7a8e19fd5a6fdf19a91f2409665c7a089ffe7b9b5394ab33c0eec04cbecdd01f", size = 94307 },
    { url = "https://files.pythonhosted.org/packages/f3/ff/b7a9c1d7df37e594b43b7a8030e228ccd4ce361eeff24a92b17fe210e57d/yarl-1.19.0-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:cda34ab19099c3a1685ad48fe45172536610c312b993310b5f1ca3eb83453b36", size = 342811 },
    { url = "https://files.pythonhosted.org/packages/79/e2/9e092876b2156c1d386e4864e85eba541ccabf2b9dcc47da64624bad0cc9/yarl-1.19.0-cp313-cp313-manylinux_2_17_armv7l.manylinux2014_armv7l.manylinux_2_31_armv7l.whl", hash = "sha256:7908a25d33f94852b479910f9cae6cdb9e2a509894e8d5f416c8342c0253c397", size = 336928 },
    { url = "https://files.pythonhosted.org/packages/71/24/648d99c134f2e14fc01ba790ad36ab56815e00069e60a12a4af893448b83/yarl-1.19.0-cp313-cp313-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:e66c14d162bac94973e767b24de5d7e6c5153f7305a64ff4fcba701210bcd638", size = 351021 },
    { url = "https://files.pythonhosted.org/packages/0c/ee/7278d475784d407d1990a5939722e66a0fef057046fb5f1721f0a6eb156c/yarl-1.19.0-cp313-cp313-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:c03607bf932aa4cfae371e2dc9ca8b76faf031f106dac6a6ff1458418140c165", size = 354454 },
    { url = "https://files.pythonhosted.org/packages/15/ae/242546114e052a7de21a75bd7d4860266439f90bbc21c5e4dd696866d91d/yarl-1.19.0-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:9931343d1c1f4e77421687b6b94bbebd8a15a64ab8279adf6fbb047eff47e536", size = 347594 },
    { url = "https://files.pythonhosted.org/packages/46/2c/35f4347f76ea4c986e9c1f774b085f489b3a1bf1503c67a4dfc5d8e68e92/yarl-1.19.0-cp313-cp313-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:262087a8a0d73e1d169d45c2baf968126f93c97cf403e1af23a7d5455d52721f", size = 334113 },
    { url = "https://files.pythonhosted.org/packages/20/89/3086bc8ec8d7bd505531c51056452d7ae6af906d29c427374f1170ac1938/yarl-1.19.0-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:70f384921c24e703d249a6ccdabeb57dd6312b568b504c69e428a8dd3e8e68ca", size = 361037 },
    { url = "https://files.pythonhosted.org/packages/a1/5b/2c9765524a70d1c51922b41c91caa30c8094a416734349166e1a3d8de055/yarl-1.19.0-cp313-cp313-musllinux_1_2_armv7l.whl", hash = "sha256:756b9ea5292a2c180d1fe782a377bc4159b3cfefaca7e41b5b0a00328ef62fa9", size = 361025 },
    { url = "https://files.pythonhosted.org/packages/ca/f8/c4a190bcc3cd98fb428d1dd31519e58004153dc7f2acd1236ecae54e3433/yarl-1.19.0-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:cbeb9c145d534c240a63b6ecc8a8dd451faeb67b3dc61d729ec197bb93e29497", size = 364397 },
    { url = "https://files.pythonhosted.org/packages/6b/fb/f65b1347be8e12ac4e3e37a9bb880e6b9b604f252aaafd88e4879b1e9348/yarl-1.19.0-cp313-cp313-musllinux_1_2_ppc64le.whl", hash = "sha256:087ae8f8319848c18e0d114d0f56131a9c017f29200ab1413b0137ad7c83e2ae", size = 374065 },
    { url = "https://files.pythonhosted.org/packages/1c/c5/102cc3b9baad1a76f9127453ad08e0f5bc9c996c18128b1e28fe03817d6c/yarl-1.19.0-cp313-cp313-musllinux_1_2_s390x.whl", hash = "sha256:362f5480ba527b6c26ff58cff1f229afe8b7fdd54ee5ffac2ab827c1a75fc71c", size = 381341 },
    { url = "https://files.pythonhosted.org/packages/f7/ce/f5dc0439320dfe59fadab8cdd24ac324be19cf6ae4736422c7e2a510ddf3/yarl-1.19.0-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:f408d4b4315e814e5c3668094e33d885f13c7809cbe831cbdc5b1bb8c7a448f4", size = 376552 },
    { url = "https://files.pythonhosted.org/packages/a9/4a/4833a134c76af987eff3ce8cb71e42932234120e6be061eb2555061e8844/yarl-1.19.0-cp313-cp313-win32.whl", hash = "sha256:24e4c367ad69988a2283dd45ea88172561ca24b2326b9781e164eb46eea68345", size = 85878 },
    { url = "https://files.pythonhosted.org/packages/32/e9/59327daab3af8f79221638a8f0d11474d20f6a8fbc41e9da80c5ef69e688/yarl-1.19.0-cp313-cp313-win_amd64.whl", hash = "sha256:0110f91c57ab43d1538dfa92d61c45e33b84df9257bd08fcfcda90cce931cbc9", size = 92448 },
    { url = "https://files.pythonhosted.org/packages/f0/77/38ee2b6ea52fa46efb3a68c17d066760a2e873c99837001922dad3c5d4e5/yarl-1.19.0-cp39-cp39-macosx_10_9_universal2.whl", hash = "sha256:85ac908cd5a97bbd3048cca9f1bf37b932ea26c3885099444f34b0bf5d5e9fa6", size = 146440 },
    { url = "https://files.pythonhosted.org/packages/08/14/4c2f8696bf09d851d299e4af62bf005e6087f162cd34b8c88c332d8580ea/yarl-1.19.0-cp39-cp39-macosx_10_9_x86_64.whl", hash = "sha256:6ba0931b559f1345df48a78521c31cfe356585670e8be22af84a33a39f7b9221", size = 97490 },
    { url = "https://files.pythonhosted.org/packages/8d/b9/a67586d46e9c68ecae6162164539c50fdeab3f4722decda4f6ea9f7bf4fd/yarl-1.19.0-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:5bc503e1c1fee1b86bcb58db67c032957a52cae39fe8ddd95441f414ffbab83e", size = 95236 },
    { url = "https://files.pythonhosted.org/packages/76/01/2f3c33ef91f9292bb4bb59654fc5f6e0c24780de74cc993f583dec7c6adb/yarl-1.19.0-cp39-cp39-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:d995122dcaf180fd4830a9aa425abddab7c0246107c21ecca2fa085611fa7ce9", size = 330624 },
    { url = "https://files.pythonhosted.org/packages/43/fd/64e414ffba8f19e5d151c06e9402a0a0054f0c8f5d5e25519612d5d583ad/yarl-1.19.0-cp39-cp39-manylinux_2_17_armv7l.manylinux2014_armv7l.manylinux_2_31_armv7l.whl", hash = "sha256:217f69e60a14da4eed454a030ea8283f8fbd01a7d6d81e57efb865856822489b", size = 325798 },
    { url = "https://files.pythonhosted.org/packages/7a/84/813be2b6b8c4c5bdafa5e0c0e5b17213f45fd10efbfaaa1279a917201373/yarl-1.19.0-cp39-cp39-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:aad67c8f13a4b79990082f72ef09c078a77de2b39899aabf3960a48069704973", size = 348176 },
    { url = "https://files.pythonhosted.org/packages/4f/06/81f9a80e243e043f0dc6a043d1a89dc004b06e3f71fb7c83f9013959bb5b/yarl-1.19.0-cp39-cp39-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:dff065a1a8ed051d7e641369ba1ad030d5a707afac54cf4ede7069b959898835", size = 343497 },
    { url = "https://files.pythonhosted.org/packages/ec/8a/abbed688dd85b5a29e91ed9a7f4cce9efe925083d7567f341ece0b36cc7e/yarl-1.19.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:ada882e26b16ee651ab6544ce956f2f4beaed38261238f67c2a96db748e17741", size = 336969 },
    { url = "https://files.pythonhosted.org/packages/33/1a/7a6316473afec0b57e1cbf2ccaa02df9f138c0e447b43e85e8b1a4e7a549/yarl-1.19.0-cp39-cp39-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:67a56b1acc7093451ea2de0687aa3bd4e58d6b4ef6cbeeaad137b45203deaade", size = 328910 },
    { url = "https://files.pythonhosted.org/packages/29/07/ba204b362147a04a5e172af726887156ae4e098fab826aa9d7269fbdbf89/yarl-1.19.0-cp39-cp39-musllinux_1_2_aarch64.whl", hash = "sha256:e97d2f0a06b39e231e59ebab0e6eec45c7683b339e8262299ac952707bdf7688", size = 342614 },
    { url = "https://files.pythonhosted.org/packages/e1/43/555be0062c999a610ad2c7b5a78695f25a70890be8c3e9ae555386b20cd3/yarl-1.19.0-cp39-cp39-musllinux_1_2_armv7l.whl", hash = "sha256:a5288adb7c59d0f54e4ad58d86fb06d4b26e08a59ed06d00a1aac978c0e32884", size = 340438 },
    { url = "https://files.pythonhosted.org/packages/26/17/703f82dbac560b9a47cee7c83abad923ac98f062eda9430dab098c28a3c9/yarl-1.19.0-cp39-cp39-musllinux_1_2_i686.whl", hash = "sha256:1efbf4d03e6eddf5da27752e0b67a8e70599053436e9344d0969532baa99df53", size = 343236 },
    { url = "https://files.pythonhosted.org/packages/e7/2c/a73354c4cc84e39a1eb83c1fabce01a75640a7fcf4183e5d3e99b1e510bd/yarl-1.19.0-cp39-cp39-musllinux_1_2_ppc64le.whl", hash = "sha256:f228f42f29cc87db67020f7d71624102b2c837686e55317b16e1d3ef2747a993", size = 358432 },
    { url = "https://files.pythonhosted.org/packages/f2/b5/5213af4695344281637d65005b781151008446bbd852a4b6a1b47b6952fa/yarl-1.19.0-cp39-cp39-musllinux_1_2_s390x.whl", hash = "sha256:c515f7dd60ca724e4c62b34aeaa603188964abed2eb66bb8e220f7f104d5a187", size = 359656 },
    { url = "https://files.pythonhosted.org/packages/d0/7d/00c56abbb3bec635dbe1f0ffb11f04eefc9ec2e1af24f10b34ed5d4e154d/yarl-1.19.0-cp39-cp39-musllinux_1_2_x86_64.whl", hash = "sha256:4815ec6d3d68a96557fa71bd36661b45ac773fb50e5cfa31a7e843edb098f060", size = 353732 },
    { url = "https://files.pythonhosted.org/packages/84/4f/37e5c9162af1a494f9854683869c67be271c5e66f75b0c7010c78a025356/yarl-1.19.0-cp39-cp39-win32.whl", hash = "sha256:9fac2dd1c5ecb921359d9546bc23a6dcc18c6acd50c6d96f118188d68010f497", size = 87082 },
    { url = "https://files.pythonhosted.org/packages/55/7f/ef6a2a6d95671430364ec801286ed748cc9808bd747f038639158b5f308d/yarl-1.19.0-cp39-cp39-win_amd64.whl", hash = "sha256:5864f539ce86b935053bfa18205fa08ce38e9a40ea4d51b19ce923345f0ed5db", size = 93180 },
    { url = "https://files.pythonhosted.org/packages/a4/06/ae25a353e8f032322df6f30d6bb1fc329773ee48e1a80a2196ccb8d1206b/yarl-1.19.0-py3-none-any.whl", hash = "sha256:a727101eb27f66727576630d02985d8a065d09cd0b5fcbe38a5793f71b2a97ef", size = 45990 },
]
```

## File: `src/chonkie/__init__.py`
```python
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

## File: `src/chonkie/tokenizer.py`
```python
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

## File: `src/chonkie/chunker/__init__.py`
```python
"""Module for chunkers."""

from .base import BaseChunker
from .late import LateChunker
from .recursive import RecursiveChunker
from .sdpm import SDPMChunker
from .semantic import SemanticChunker
from .sentence import SentenceChunker
from .token import TokenChunker

__all__ = [
    "BaseChunker",
    "TokenChunker",
    "SentenceChunker",
    "RecursiveChunker",
    "SemanticChunker",
    "SDPMChunker",
    "LateChunker",
]
```

## File: `src/chonkie/chunker/base.py`
```python
"""Base Class for All Chunkers."""

import warnings
from abc import ABC, abstractmethod
from multiprocessing import Pool, cpu_count
from typing import Any, Callable, Sequence, Union

from tqdm import tqdm

from chonkie.tokenizer import Tokenizer
from chonkie.types.base import Chunk


class BaseChunker(ABC):
    """Base class for all chunkers."""

    def __init__(
        self, tokenizer_or_token_counter: Union[str, Callable[[str], int], Any]
    ):
        """Initialize the chunker with any necessary parameters.

        Args:
            tokenizer_or_token_counter (Union[str, Callable[[str], int], Any]): The tokenizer or token counter to use.

        """
        self.tokenizer = Tokenizer(tokenizer_or_token_counter)
        self._use_multiprocessing = True

    def __repr__(self):
        """Return a string representation of the chunker."""
        return f"{self.__class__.__name__}()"

    def __call__(
        self, text: Union[str, Sequence[str]], show_progress: bool = True
    ) -> Union[Sequence[Chunk], Sequence[Sequence[Chunk]]]:
        """Call the chunker with the given arguments.

        Args:
            text (Union[str, Sequence[str]]): The text to chunk.
            show_progress (bool): Whether to show progress.

        Returns:
            If the input is a string, return a list of Chunks.
            If the input is a list of strings, return a list of lists of Chunks.

        """
        if isinstance(text, str):
            return self.chunk(text)
        elif isinstance(text, Sequence):
            return self.chunk_batch(text, show_progress)
        else:
            raise ValueError("Input must be a string or a list of strings.")

    def _get_optimal_worker_count(self) -> int:
        """Get the optimal number of workers for parallel processing."""
        try:
            cpu_cores = cpu_count()
            return min(8, max(1, cpu_cores * 3 // 4))
        except Exception as e:
            warnings.warn(
                f"Proceeding with 1 worker. Error calculating optimal worker count: {e}"
            )
            return 1

    def _sequential_batch_processing(
        self, texts: Sequence[str], show_progress
    ) -> Sequence[Sequence[Chunk]]:
        """Process a batch of texts sequentially."""
        return [
            self.chunk(t)
            for t in tqdm(
                texts,
                desc="🦛",
                disable=not show_progress,
                unit="doc",
                bar_format="{desc} ch{bar:20}nk {percentage:3.0f}% • {n_fmt}/{total_fmt} docs chunked [{elapsed}<{remaining}, {rate_fmt}] 🌱",
                ascii=" o",
            )
        ]

    def _parallel_batch_processing(
        self, texts: Sequence[str], show_progress: bool = True
    ) -> Sequence[Sequence[Chunk]]:
        """Process a batch of texts using multiprocessing."""
        num_workers = self._get_optimal_worker_count()
        total = len(texts)
        chunk_size = max(1, min(total // (num_workers * 16), 10))

        with Pool(processes=num_workers) as pool:
            results = []
            with tqdm(
                total=total,
                desc="🦛",
                disable=not show_progress,
                unit="doc",
                bar_format="{desc} ch{bar:20}nk {percentage:3.0f}% • {n_fmt}/{total_fmt} docs chunked [{elapsed}<{remaining}, {rate_fmt}] 🌱",
                ascii=" o",
            ) as progress_bar:
                for result in pool.imap(self.chunk, texts, chunksize=chunk_size):
                    results.append(result)
                    progress_bar.update()
            return results

    @abstractmethod
    def chunk(self, text: str) -> Sequence[Chunk]:
        """Chunk the given text.

        Args:
            text (str): The text to chunk.

        Returns:
            List of Chunks containing the chunked text and other metadata.

        """
        pass

    def chunk_batch(
        self, texts: Sequence[str], show_progress: bool = True
    ) -> Sequence[Sequence[Chunk]]:
        """Chunk a batch of texts.

        Args:
            texts (Sequence[str]): The texts to chunk.
            show_progress (bool): Whether to show progress.

        Returns:
            List of lists of Chunks containing the chunked text and other metadata.

        """
        # simple handles of empty and single text cases
        if len(texts) == 0:
            return []
        if len(texts) == 1:
            return [self.chunk(texts[0])]

        # Now for the remaining, check the self._multiprocessing bool flag
        if self._use_multiprocessing:
            return self._parallel_batch_processing(texts, show_progress)
        else:
            return self._sequential_batch_processing(texts, show_progress)
```

## File: `src/chonkie/chunker/late.py`
```python
"""Module containing the LateChunker class."""

import importlib.util as importutil
from typing import Any, List, Union

# Get all the Chonkie imports
from chonkie.chunker.recursive import RecursiveChunker
from chonkie.embeddings import BaseEmbeddings
from chonkie.types import LateChunk, RecursiveRules


class LateChunker(RecursiveChunker):
    """A chunker that chunks texts based on late interaction.

    This class extends the RecursiveChunker class and overrides its chunk method to implement late chunking.

    Args:
        embedding_model: The embedding model to use for chunking.
        chunk_size: The maximum size of each chunk.

    """

    def __init__(
        self,
        embedding_model: Union[
            str, BaseEmbeddings, Any
        ] = "sentence-transformers/all-MiniLM-L6-v2",
        chunk_size: int = 512,
        rules: RecursiveRules = RecursiveRules(),
        min_characters_per_chunk: int = 24,
        **kwargs: Any,
    ) -> None:
        """Initialize the LateChunker.

        Args:
            embedding_model: The embedding model to use for chunking.
            chunk_size: The maximum size of each chunk.
            rules: The rules to use for chunking.
            min_characters_per_chunk: The minimum number of characters per chunk.
            **kwargs: Additional keyword arguments.

        """
        # Lazy import all the dependencies on initialization
        self._import_dependencies()

        # set all the additional attributes
        if isinstance(embedding_model, BaseEmbeddings):
            self.embedding_model = embedding_model
        elif isinstance(embedding_model, str):
            from chonkie.embeddings.auto import AutoEmbeddings

            self.embedding_model = AutoEmbeddings.get_embeddings(
                embedding_model, **kwargs
            )
        else:
            raise ValueError(f"{embedding_model} is not a valid embedding model")

        # Probably the dependency hasn't been installed
        if self.embedding_model is None:
            raise ImportError(
                "Oh! seems like you're missing the proper dependency to run this chunker. Please install it using `pip install chonkie[st]`"
            )

        # Initialize the RecursiveChunker with the embedding_model's tokenizer
        super().__init__(
            tokenizer_or_token_counter=self.embedding_model.get_tokenizer_or_token_counter(),
            chunk_size=chunk_size,
            rules=rules,
            min_characters_per_chunk=min_characters_per_chunk,
            return_type="chunks",
        )

        # Disable multiprocessing for this chunker
        self._use_multiprocessing = False

    def _get_late_embeddings(
        self, token_embeddings: "np.ndarray", token_counts: List[int]
    ) -> List["np.ndarray"]:
        # Split the token embeddings into chunks based on the token counts
        embs = []
        cum_token_counts = np.cumsum([0] + token_counts)
        for i in range(len(token_counts)):
            embs.append(
                np.mean(
                    token_embeddings[cum_token_counts[i] : cum_token_counts[i + 1]],
                    axis=0,
                )
            )
        return embs

    def chunk(self, text: str) -> List[LateChunk]:
        """Chunk the text via LateChunking."""
        # This would first call upon the _recursive_chunk method
        # and then use the embedding model to get the token token_embeddings
        # Lastly, we would combine the methods together to create the LateChunk objects
        chunks = self._recursive_chunk(text)
        token_embeddings = self.embedding_model.embed_as_tokens(text)

        # Get the token_counts for all the chunks
        token_counts = [c.token_count for c in chunks]

        # Validate the token_counts with the actual count
        if sum(token_counts) > token_embeddings.shape[0]:
            raise ValueError(
                "The sum of token counts exceeds the number of tokens in the text"
            )
        # Diff would always be positive now~ which it should be considering token_counts
        # doesn't have any special tokens added
        if sum(token_counts) < token_embeddings.shape[0]:
            # Use a little trick to ensure that the token counts get properly adjusted
            diff = token_embeddings.shape[0] - sum(token_counts)
            token_counts[0] = token_counts[0] + diff // 2
            token_counts[-1] = token_counts[-1] + (diff - diff // 2)

        if sum(token_counts) != token_embeddings.shape[0]:
            raise ValueError(
                "The sum of token counts does not match the number of tokens in the text",
                f"Expected {token_embeddings.shape[0]}, got {sum(token_counts)}",
            )

        # Split the token embeddings into chunks based on the token counts
        late_embds = self._get_late_embeddings(token_embeddings, token_counts)

        # Wrap it all up in LateChunks
        result = []
        for chunk, token_count, embedding in zip(chunks, token_counts, late_embds):
            result.append(
                LateChunk(
                    text=chunk.text,
                    start_index=chunk.start_index,
                    end_index=chunk.end_index,
                    token_count=token_count,
                    embedding=embedding,
                )
            )
        return result

    def _import_dependencies(self) -> None:
        """Lazy import dependencies for the chunker implementation.

        This method should be implemented by all chunker implementations that require
        additional dependencies. It lazily imports the dependencies only when they are needed.
        """
        if importutil.find_spec("numpy"):
            global np
            import numpy as np
        else:
            raise ImportError(
                "numpy is not available. Please install it via `pip install chonkie[semantic]`"
            )
```

## File: `src/chonkie/chunker/recursive.py`
```python
"""Chonkie: Recursive Chunker.

Splits text into smaller chunks recursively. Express chunking logic through RecursiveLevel objects.
"""

from bisect import bisect_left
from functools import lru_cache
from itertools import accumulate
from typing import Any, Callable, Literal, Optional, Sequence, Union

from chonkie.chunker.base import BaseChunker
from chonkie.types import (
    RecursiveChunk,
    RecursiveLevel,
    RecursiveRules,
)


class RecursiveChunker(BaseChunker):
    """Chunker that recursively splits text into smaller chunks, based on the provided RecursiveRules.

    Args:
        tokenizer_or_token_counter (Union[str, Callable, Any]): Tokenizer or token counter to use
        rules (list[RecursiveLevel]): List of RecursiveLevel objects defining chunking rules at a level.
        chunk_size (int): Maximum size of each chunk.
        min_characters_per_chunk (int): Minimum number of characters per chunk.
        return_type (str): Type of return value, either 'chunks' or 'texts'.

    """

    def __init__(
        self,
        tokenizer_or_token_counter: Union[str, Callable, Any] = "gpt2",
        chunk_size: int = 512,
        rules: RecursiveRules = RecursiveRules(),
        min_characters_per_chunk: int = 24,
        return_type: Literal["texts", "chunks"] = "chunks",
    ) -> None:
        """Create a RecursiveChunker object.

        Args:
            tokenizer_or_token_counter (Union[str, Callable, Any]): Tokenizer or token counter to use
            rules (list[RecursiveLevel]): List of RecursiveLevel objects defining chunking rules at a level.
            chunk_size (int): Maximum size of each chunk.
            min_characters_per_chunk (int): Minimum number of characters per chunk.
            return_type (str): Type of return value, either 'chunks' or 'texts'.

        Raises:
            ValueError: If chunk_size <=0
            ValueError: If min_characters_per_chunk < 1
            ValueError: If return_type is not 'chunks' or 'texts'.
            ValueError: If recursive_rules is not a RecursiveRules object.

        """
        super().__init__(tokenizer_or_token_counter=tokenizer_or_token_counter)

        if chunk_size <= 0:
            raise ValueError("chunk_size must be greater than 0")
        if min_characters_per_chunk <= 0:
            raise ValueError("min_characters_per_chunk must be greater than 0")
        if return_type not in ["chunks", "texts"]:
            raise ValueError(
                f"return_type {return_type} is invalid. Must be 'chunks' or 'texts'."
            )
        if not isinstance(rules, RecursiveRules):
            raise ValueError("`rules` must be a RecursiveRules object.")


        # Initialize the internal values
        self.chunk_size = chunk_size
        self.min_characters_per_chunk = min_characters_per_chunk
        self.return_type = return_type
        self.rules = rules
        self.sep = "✄"
        self._CHARS_PER_TOKEN = 6.5

    @lru_cache(maxsize=4096)
    def _estimate_token_count(self, text: str) -> int:
        estimate = max(1, len(text) // self._CHARS_PER_TOKEN)
        return (
            self.chunk_size + 1
            if estimate > self.chunk_size
            else self.tokenizer.count_tokens(text)
        )

    def _split_text(self, text: str, recursive_level: RecursiveLevel) -> list[str]:
        """Split the text into chunks using the delimiters."""
        # At every delimiter, replace it with the sep
        if recursive_level.whitespace:
            splits = text.split(" ")
        elif recursive_level.delimiters:
            if recursive_level.include_delim == "prev":
                for delimiter in recursive_level.delimiters:
                    text = text.replace(delimiter, delimiter + self.sep)
            elif recursive_level.include_delim == "next":
                for delimiter in recursive_level.delimiters:
                    text = text.replace(delimiter, self.sep + delimiter)
            else:
                for delimiter in recursive_level.delimiters:
                    text = text.replace(delimiter, self.sep)

            splits = [split for split in text.split(self.sep) if split != ""]

            # Merge short splits
            current = ""
            merged = []
            for split in splits:
                if len(split) < self.min_characters_per_chunk:
                    current += split
                elif current:
                    current += split
                    merged.append(current)
                    current = ""
                else:
                    merged.append(split)

                if len(current) >= self.min_characters_per_chunk:
                    merged.append(current)
                    current = ""

            if current:
                merged.append(current)

            splits = merged
        else:
            # Encode, Split, and Decode
            encoded = self.tokenizer.encode(text)
            token_splits = [
                encoded[i : i + self.chunk_size]
                for i in range(0, len(encoded), self.chunk_size)
            ]
            splits = self.tokenizer.decode_batch(token_splits)

        # Some splits may not be meaningful yet.
        # This will be handled during chunk creation.
        return splits

    # TODO: Remove the make chunks function and calculate the start_index and end_index
    # based on the text lengths --> which would be faster and more accurate indexing than
    # the current approach
    def _make_chunks(
        self,
        text: str,
        token_count: int,
        level: int,
        full_text: Optional[str] = None,
        last_chunk_end_index: int = 0,
    ) -> RecursiveChunk:
        """Form and return a RecursiveChunk object."""
        if full_text is None:
            full_text = text
        try:
            start_index = last_chunk_end_index + full_text[last_chunk_end_index:].index(
                text
            )
            end_index = start_index + len(text)
        except Exception as e:
            print(
                f"Error finding start and end index for text '{text}' in full_text. Error: {e}"
                f"Setting start and end index to 0."
            )
            start_index = 0
            end_index = 0

        return RecursiveChunk(
            text=text,
            start_index=start_index,
            end_index=end_index,
            token_count=token_count,
            level=level,
        )

    def _merge_splits(
        self,
        splits: list[str],
        token_counts: list[int],
        combine_whitespace: bool = False,
    ) -> list[str]:
        """Merge short splits."""
        if not splits or not token_counts:
            return [], []

        # If the number of splits and token counts does not match, raise an error
        if len(splits) != len(token_counts):
            raise ValueError(
                f"Number of splits {len(splits)} does not match number of token counts {len(token_counts)}"
            )

        # If all splits are larger than the chunk size, return them
        if all(counts > self.chunk_size for counts in token_counts):
            return splits, token_counts

        # If the splits are too short, merge them
        merged = []
        if combine_whitespace:
            # +1 for the whitespace
            cumulative_token_counts = list(
                accumulate([0] + token_counts, lambda x, y: x + y + 1)
            )
        else:
            cumulative_token_counts = list(accumulate([0] + token_counts))
        current_index = 0
        combined_token_counts = []

        while current_index < len(splits):
            current_token_count = cumulative_token_counts[current_index]
            required_token_count = current_token_count + self.chunk_size

            # Find the index to merge at
            index = min(
                bisect_left(
                    cumulative_token_counts,
                    required_token_count,
                    lo=current_index,
                )
                - 1,
                len(splits),
            )

            # If current_index == index,
            # we need to move to the next index
            if index == current_index:
                index += 1

            # Merge splits
            if combine_whitespace:
                merged.append(" ".join(splits[current_index:index]))
            else:
                merged.append("".join(splits[current_index:index]))

            # Adjust token count
            combined_token_counts.append(
                cumulative_token_counts[min(index, len(splits))] - current_token_count
            )
            current_index = index

        return merged, combined_token_counts

    def _recursive_chunk(
        self, text: str, level: int = 0, full_text: Optional[str] = None
    ) -> Sequence[RecursiveChunk]:
        """Recursive helper for core chunking."""
        if not text:
            return []

        if level >= len(self.rules):
            if self.return_type == "texts":
                return [text]
            if self.return_type == "chunks":
                return [
                    self._make_chunks(
                        text, self._estimate_token_count(text), level, full_text
                    )
                ]
            raise ValueError(
                f"Invalid return_type {self.return_type}. Must be 'chunks' or 'texts'."
            )

        if full_text is None:
            full_text = text

        curr_rule = self.rules[level]
        splits = self._split_text(text, curr_rule)
        token_counts = [self._estimate_token_count(split) for split in splits]

        # Merge splits
        # If no delimeters and no whitespace, we can just use the splits
        # If no delimeters and whitespace, we need to merge the splits
        # If delimeters and whitespace, we need to merge the splits
        if curr_rule.delimiters is None and not curr_rule.whitespace:
            merged, combined_token_counts = splits, token_counts

        elif curr_rule.delimiters is None and curr_rule.whitespace:
            merged, combined_token_counts = self._merge_splits(
                splits, token_counts, combine_whitespace=True
            )
        else:
            merged, combined_token_counts = self._merge_splits(
                splits, token_counts, combine_whitespace=False
            )

        # Chunk long merged splits
        chunks = []
        last_chunk_end_index = 0
        for split, token_count in zip(merged, combined_token_counts):
            if token_count > self.chunk_size:
                chunks.extend(self._chunk_helper(split, level + 1, full_text))
            else:
                if self.return_type == "chunks":
                    if chunks:
                        last_chunk_end_index = chunks[-1].end_index
                    no_delim = curr_rule.delimiters is None and not curr_rule.whitespace
                    # **Speedup**: Since there are no delimiters we can just join the "merged" result.
                    chunks.append(
                        self._make_chunks(
                            split,
                            token_count,
                            level,
                            ("".join(merged) if no_delim else full_text),
                            last_chunk_end_index,
                        )
                    )
                elif self.return_type == "texts":
                    chunks.append(split)
        return chunks

    def chunk(self, text: str) -> Sequence[RecursiveChunk]:
        """Recursively chunk text.

        Args:
            text (str): Text to chunk.

        """
        return self._recursive_chunk(text=text, level=0, full_text=text)

    def __repr__(self) -> str:
        """Get a string representation of the recursive chunker."""
        return (
            f"RecursiveChunker(tokenizer_or_token_counter={self.tokenizer},"
            f" rules={self.rules}, chunk_size={self.chunk_size}, "
            f"min_characters_per_chunk={self.min_characters_per_chunk}, "
            f"return_type={self.return_type})"
        )
```

## File: `src/chonkie/chunker/sdpm.py`
```python
"""Module containing the SDPMChunker class.

This chunker uses the Semantic Double-Pass Merging algorithm to chunk text.

"""

from typing import List, Literal, Optional, Union

from chonkie.chunker.semantic import SemanticChunker
from chonkie.embeddings import BaseEmbeddings
from chonkie.types import SemanticChunk, Sentence


class SDPMChunker(SemanticChunker):
    """Chunker using the Semantic Double-Pass Merging algorithm.

    This chunker uses the Semantic Double-Pass Merging algorithm to chunk text.

    Args:
        embedding_model: The embedding model to use.
        mode: The mode to use.
        threshold: The threshold to use.
        chunk_size: The chunk size to use.
        similarity_window: The similarity window to use.
        min_sentences: The minimum number of sentences to use.
        min_chunk_size: The minimum chunk size to use.
        min_characters_per_sentence: The minimum number of characters per sentence to use.
        threshold_step: The threshold step to use.
        delim: The delimiters to use.
        include_delim: Whether to include delimiters in chunks.
        skip_window: The skip window to use.
        return_type: The return type to use.
        **kwargs: Additional keyword arguments.

    """

    def __init__(
        self,
        embedding_model: Union[str, BaseEmbeddings] = "minishlab/potion-base-8M",
        chunk_size: int = 512,
        mode: str = "window",
        threshold: Union[str, float, int] = "auto",
        similarity_window: int = 1,
        min_sentences: int = 1,
        min_chunk_size: int = 2,
        min_characters_per_sentence: int = 12,
        threshold_step: float = 0.01,
        delim: Union[str, List[str]] = [".", "!", "?", "\n"],
        include_delim: Optional[Literal["prev", "next"]] = "prev",
        skip_window: int = 1,
        return_type: Literal["chunks", "texts"] = "chunks",
        **kwargs,
    ) -> None:  # type: ignore
        """Initialize the SDPMChunker.

        Args:
            embedding_model: The embedding model to use.
            mode: The mode to use.
            threshold: The threshold to use.
            chunk_size: The chunk size to use.
            similarity_window: The similarity window to use.
            min_sentences: The minimum number of sentences to use.
            min_chunk_size: The minimum chunk size to use.
            min_characters_per_sentence: The minimum number of characters per sentence to use.
            threshold_step: The threshold step to use.
            delim: The delimiters to use.
            include_delim: Whether to include delimiters.
            skip_window: The skip window to use.
            return_type: The return type to use.
            **kwargs: Additional keyword arguments.

        """
        super().__init__(
            embedding_model=embedding_model,
            mode=mode,
            threshold=threshold,
            chunk_size=chunk_size,
            similarity_window=similarity_window,
            min_sentences=min_sentences,
            min_chunk_size=min_chunk_size,
            min_characters_per_sentence=min_characters_per_sentence,
            threshold_step=threshold_step,
            delim=delim,
            include_delim=include_delim,
            return_type=return_type,
            **kwargs,
        )

        self.skip_window = skip_window

        # Disable the multiprocessing flag for this class
        self._use_multiprocessing = False

    def _merge_sentence_groups(self, sentence_groups: List[List[str]]) -> List[str]:
        """Merge sentence groups into a single sentence.

        Args:
            sentence_groups: The sentence groups to merge.

        Returns:
            The merged sentence.

        """
        merged_sentences = []
        for sentence_group in sentence_groups:
            merged_sentences.extend(sentence_group)
        return merged_sentences

    def _skip_and_merge(
        self, groups: List[List[Sentence]], similarity_threshold: float
    ) -> List[List[Sentence]]:
        """Merge similar groups considering skip window."""
        if len(groups) <= 1:
            return groups

        merged_groups = []
        embeddings = [self._compute_group_embedding(group) for group in groups]

        while groups:
            if len(groups) == 1:
                merged_groups.append(groups[0])
                break

            # Calculate skip index ensuring it's valid
            skip_index = min(self.skip_window + 1, len(groups) - 1)

            # Compare current group with skipped group
            similarity = self._get_semantic_similarity(
                embeddings[0], embeddings[skip_index]
            )

            if similarity >= similarity_threshold:
                # Merge groups from 0 to skip_index (inclusive)
                merged = self._merge_sentence_groups(groups[: skip_index + 1])

                # Remove the merged groups
                for _ in range(skip_index + 1):
                    groups.pop(0)
                    embeddings.pop(0)

                # Add merged group back at the start
                groups.insert(0, merged)
                embeddings.insert(0, self._compute_group_embedding(merged))
            else:
                # No merge possible, move first group to results
                merged_groups.append(groups.pop(0))
                embeddings.pop(0)

        return merged_groups

    def chunk(self, text: str) -> List[SemanticChunk]:
        """Split text into semantically coherent chunks using two-pass approach.

        First groups sentences by semantic similarity, then splits groups to respect
        chunk_size while maintaining sentence boundaries.

        Args:
            text: Input text to be chunked

        Returns:
            List of SemanticChunk objects containing the chunked text and metadata

        """
        if not text.strip():
            return []

        # Prepare sentences with precomputed information
        sentences = self._prepare_sentences(text)
        if len(sentences) <= self.min_sentences:
            return [self._create_chunk(sentences)]

        # Calculate similarity threshold
        self.similarity_threshold = self._calculate_similarity_threshold(sentences)

        # First pass: Group sentences by semantic similarity
        sentence_groups = self._group_sentences(sentences)

        # Second pass: Skip and Merge by semantic similarity
        merged_groups = self._skip_and_merge(sentence_groups, self.similarity_threshold)

        # Second pass: Split groups into size-appropriate chunks
        chunks = self._split_chunks(merged_groups)

        return chunks

    def __repr__(self):
        """Return a string representation of the SDPMChunker object."""
        return (
            f"SDPMChunker(model={self.embedding_model}, "
            f"chunk_size={self.chunk_size}, "
            f"mode={self.mode}, "
            f"threshold={self.threshold}, "
            f"similarity_window={self.similarity_window}, "
            f"min_sentences={self.min_sentences}, "
            f"min_chunk_size={self.min_chunk_size}, "
            f"min_characters_per_sentence={self.min_characters_per_sentence}, "
            f"threshold_step={self.threshold_step}, "
            f"delim={self.delim}, "
            f"include_delim={self.include_delim}, "
            f"skip_window={self.skip_window}, "
            f"return_type={self.return_type})"
        )
```

## File: `src/chonkie/chunker/semantic.py`
```python
"""Semantic chunking using sentence embeddings."""

import importlib.util as importutil
import warnings
from typing import TYPE_CHECKING, List, Literal, Union

from chonkie.chunker.base import BaseChunker
from chonkie.embeddings.base import BaseEmbeddings
from chonkie.types.semantic import SemanticChunk, SemanticSentence, Sentence

if TYPE_CHECKING:
    import numpy as np


class SemanticChunker(BaseChunker):
    """Chunker that splits text into semantically coherent chunks using embeddings.

    Args:
        embedding_model: Embedding model to use for semantic chunking
        mode: Mode for grouping sentences, either "cumulative" or "window"
        threshold: Threshold for semantic similarity (0-1) or percentile (1-100), defaults to "auto"
        chunk_size: Maximum tokens allowed per chunk
        similarity_window: Number of sentences to consider for similarity threshold calculation
        min_sentences: Minimum number of sentences per chunk
        min_characters_per_sentence: Minimum number of characters per sentence
        min_chunk_size: Minimum number of tokens per sentence (defaults to 2)
        threshold_step: Step size for similarity threshold calculation
        delim: Delimiters to split sentences on
        include_delim: Whether to include the delimiters in the sentences
        return_type: Whether to return chunks or texts

    Raises:
        ValueError: If parameters are invalid

    """

    def __init__(
        self,
        embedding_model: Union[str, BaseEmbeddings] = "minishlab/potion-base-8M",
        mode: str = "window",
        threshold: Union[str, float, int] = "auto",
        chunk_size: int = 512,
        similarity_window: int = 1,
        min_sentences: int = 1,
        min_chunk_size: int = 2,
        min_characters_per_sentence: int = 12,
        threshold_step: float = 0.01,
        delim: Union[str, List[str]] = [".", "!", "?", "\n"],
        include_delim: Union[Literal["prev", "next"], None] = "prev",
        return_type: Literal["chunks", "texts"] = "chunks",
        **kwargs,
    ) -> None:  # type: ignore
        """Initialize the SemanticChunker.

        SemanticChunkers split text into semantically coherent chunks using embeddings.

        Args:
            embedding_model: Name of the sentence-transformers model to load
            mode: Mode for grouping sentences, either "cumulative" or "window"
            threshold: Threshold for semantic similarity (0-1) or percentile (1-100), defaults to "auto"
            chunk_size: Maximum tokens allowed per chunk
            similarity_window: Number of sentences to consider for similarity threshold calculation
            min_sentences: Minimum number of sentences per chunk
            min_characters_per_sentence: Minimum number of characters per sentence
            min_chunk_size: Minimum number of tokens per chunk (and sentence, defaults to 2)
            threshold_step: Step size for similarity threshold calculation
            delim: Delimiters to split sentences on
            include_delim: Whether to include the delimiters in the sentences
            return_type: Whether to return chunks or texts
            **kwargs: Additional keyword arguments

        Raises:
            ValueError: If parameters are invalid
            ImportError: If required dependencies aren't installed

        """
        if chunk_size <= 0:
            raise ValueError("chunk_size must be positive")
        if min_chunk_size <= 0:
            raise ValueError("min_chunk_size must be positive")
        if min_sentences <= 0:
            raise ValueError("min_sentences must be positive")
        if similarity_window < 0:
            raise ValueError("similarity_window must be non-negative")
        if threshold_step <= 0 or threshold_step >= 1:
            raise ValueError("threshold_step must be between 0 and 1")
        if mode not in ["cumulative", "window"]:
            raise ValueError("mode must be 'cumulative' or 'window'")
        if type(threshold) not in [str, float, int]:
            raise ValueError("threshold must be a string, float, or int")
        if type(delim) not in [str, list]:
            raise ValueError("delim must be a string or list of strings")
        elif type(threshold) == str and threshold not in ["auto"]:
            raise ValueError("threshold must be 'auto', 'smart', or 'percentile'")
        elif type(threshold) == float and (threshold < 0 or threshold > 1):
            raise ValueError("threshold (float) must be between 0 and 1")
        elif type(threshold) == int and (threshold < 1 or threshold > 100):
            raise ValueError("threshold (int) must be between 1 and 100")
        if return_type not in ["chunks", "texts"]:
            raise ValueError("Invalid return_type. Must be either 'chunks' or 'texts'.")

        # Lazy import dependencies to avoid importing them when not needed
        self._import_dependencies()

        self.mode = mode
        self.chunk_size = chunk_size
        self.threshold = threshold
        self.similarity_window = similarity_window if mode == "window" else 1
        self.min_sentences = min_sentences
        self.min_chunk_size = min_chunk_size
        self.min_characters_per_sentence = min_characters_per_sentence
        self.threshold_step = threshold_step
        self.delim = delim
        self.include_delim = include_delim
        self.sep = "✄"
        self.return_type = return_type

        if isinstance(threshold, float):
            self.similarity_threshold = threshold
            self.similarity_percentile = None
        elif isinstance(threshold, int):
            self.similarity_percentile = threshold
            self.similarity_threshold = None
        else:
            self.similarity_threshold = None
            self.similarity_percentile = None

        if isinstance(embedding_model, BaseEmbeddings):
            self.embedding_model = embedding_model
        elif isinstance(embedding_model, str):
            from chonkie.embeddings.auto import AutoEmbeddings

            self.embedding_model = AutoEmbeddings.get_embeddings(
                embedding_model, **kwargs
            )
        else:
            raise ValueError(f"{embedding_model} is not a valid embedding model")

        # Probably the dependency is not installed
        if self.embedding_model is None:
            raise ImportError(
                f"{embedding_model} is not a valid embedding model",
                "Please install the `semantic` extra to use this feature",
            )

        # Keeping the tokenizer the same as the sentence model is important
        # for the group semantic meaning to be calculated properly
        super().__init__(self.embedding_model.get_tokenizer_or_token_counter())

        # Remove the multiprocessing flag from the base class
        self._use_multiprocessing = False

    def _split_sentences(
        self,
        text: str,
    ) -> List[str]:
        """Fast sentence splitting while maintaining accuracy.

        This method is faster than using regex for sentence splitting and is more accurate than using the spaCy sentence tokenizer.

        Args:
            text: Input text to be split into sentences
            delim: Delimiters to split sentences on
            sep: Separator to use when splitting sentences

        Returns:
            List of sentences

        """
        t = text
        for c in self.delim:
            if self.include_delim == "prev":
                t = t.replace(c, c + self.sep)
            elif self.include_delim == "next":
                t = t.replace(c, self.sep + c)
            else:
                t = t.replace(c, self.sep)

        # Initial split
        splits = [s for s in t.split(self.sep) if s != ""]

        # Combine short splits with previous sentence
        current = ""
        sentences = []
        for s in splits:
            # If the split is short, add to current and if long add to sentences
            if len(s) < self.min_characters_per_sentence:
                current += s
            elif current:
                current += s
                sentences.append(current)
                current = ""
            else:
                sentences.append(s)

            # At any point if the current sentence is longer than the min_characters_per_sentence,
            # add it to the sentences
            if len(current) >= self.min_characters_per_sentence:
                sentences.append(current)
                current = ""

        # If there is a current split, add it to the sentences
        if current:
            sentences.append(current)

        return sentences

    def _compute_similarity_threshold(self, all_similarities: List[float]) -> float:
        """Compute similarity threshold based on percentile if specified."""
        if self.similarity_threshold is not None:
            return self.similarity_threshold
        else:
            return float(np.percentile(all_similarities, self.similarity_percentile))

    def _prepare_sentences(self, text: str) -> List[SemanticSentence]:
        """Prepare sentences with precomputed information.

        Args:
            text: Input text to be processed

        Returns:
            List of SemanticSentence objects with precomputed token counts and embeddings

        """
        if not text.strip():
            return []

        # Split text into sentences
        raw_sentences = self._split_sentences(text)

        # Get start and end indices for each sentence
        sentence_indices = []
        current_idx = 0
        for sent in raw_sentences:
            start_idx = text.find(sent, current_idx)
            end_idx = start_idx + len(sent)
            sentence_indices.append((start_idx, end_idx))
            current_idx = end_idx

        # Batch compute embeddings for all sentences
        # The embeddings are computed assuming a similarity window is applied
        # There should be len(raw_sentences) number of similarity groups
        sentence_groups = []
        for i in range(len(raw_sentences)):
            group = []
            # similarity window should consider before and after the current sentence
            for j in range(i - self.similarity_window, i + self.similarity_window + 1):
                if j >= 0 and j < len(raw_sentences):
                    group.append(raw_sentences[j])
            sentence_groups.append("".join(group))
        assert len(sentence_groups) == len(raw_sentences), (
            f"Number of sentence groups ({len(sentence_groups)}) does not match number of raw sentences ({len(raw_sentences)})"
        )
        embeddings = self.embedding_model.embed_batch(sentence_groups)

        # Batch compute token counts
        token_counts = self.tokenizer.count_tokens_batch(raw_sentences)

        # Create Sentence objects with all precomputed information
        sentences = [
            SemanticSentence(
                text=sent,
                start_index=start_idx,
                end_index=end_idx,
                token_count=count,
                embedding=embedding,
            )
            for sent, (start_idx, end_idx), count, embedding in zip(
                raw_sentences, sentence_indices, token_counts, embeddings
            )
        ]

        return sentences

    def _get_semantic_similarity(
        self, embedding1: "np.ndarray", embedding2: "np.ndarray"
    ) -> float:
        """Compute cosine similarity between two embeddings."""
        similarity = self.embedding_model.similarity(embedding1, embedding2)
        return similarity

    def _compute_group_embedding(
        self, sentences: List[SemanticSentence]
    ) -> "np.ndarray":
        """Compute mean embedding for a group of sentences."""
        if len(sentences) == 1:
            return sentences[0].embedding
        else:
            # NOTE: There's a known issue, where while calculating the sentence embeddings special tokens are added
            # but when taking the token count the special tokens are not being counted, which causes a mismatch here.
            # This is a known issue and we're working on a fix. At the moment, the error is minimal and doesn't affect the chunking as much.

            # TODO: Account for embedding model truncating to max_seq_length, which causes a mismatch in the token count.
            return np.divide(
                np.sum(
                    [(sent.embedding * sent.token_count) for sent in sentences],
                    axis=0,
                ),
                np.sum([sent.token_count for sent in sentences]),
                dtype=np.float32,
            )

    def _compute_window_similarities(
        self, sentences: List[SemanticSentence]
    ) -> List[float]:
        """Compute all pairwise similarities between sentences."""
        similarities = [1.0]
        current_sentence_window = [sentences[0]]
        window_embedding = sentences[0].embedding
        for i in range(1, len(sentences)):
            similarities.append(
                self._get_semantic_similarity(window_embedding, sentences[i].embedding)
            )

            # Update the window embedding
            if len(current_sentence_window) < self.similarity_window:
                current_sentence_window.append(sentences[i])
                window_embedding = self._compute_group_embedding(
                    current_sentence_window
                )
            else:
                current_sentence_window.pop(0)
                current_sentence_window.append(sentences[i])
                window_embedding = self._compute_group_embedding(
                    current_sentence_window
                )

        return similarities

    def _get_split_indices(
        self, similarities: List[float], threshold: float = None
    ) -> List[int]:
        """Get indices of sentences to split at."""
        if threshold is None:
            threshold = (
                self.similarity_threshold
                if self.similarity_threshold is not None
                else 0.5
            )

        # get the indices of the sentences that are below the threshold
        splits = [
            i + 1
            for i, s in enumerate(similarities)
            if s <= threshold and i + 1 < len(similarities)
        ]
        # add the start and end of the text
        splits = [0] + splits + [len(similarities)]
        # check if the splits are valid (i.e. there are enough sentences between them)
        i = 0
        while i < len(splits) - 1:
            if splits[i + 1] - splits[i] < self.min_sentences:
                splits.pop(i + 1)
            else:
                i += 1
        return splits

    def _calculate_threshold_via_binary_search(
        self, sentences: List[SemanticSentence]
    ) -> float:
        """Calculate similarity threshold via binary search."""
        # Get the token counts and cumulative token counts
        token_counts = [sent.token_count for sent in sentences]
        cumulative_token_counts = np.cumsum([0] + token_counts)

        # Compute all pairwise similarities
        similarities = self._compute_window_similarities(sentences)

        # get the median and the std for the similarities
        median = np.median(similarities)
        std = np.std(similarities)

        # the threshold is set between 1 std of the median
        low = max(median - 1 * std, 0.0)
        high = min(median + 1 * std, 1.0)

        # set iterations
        iterations = 0

        # initialize threshold
        threshold = (low + high) / 2

        while abs(high - low) > self.threshold_step:
            threshold = (low + high) / 2
            # Get the split indices
            split_indices = self._get_split_indices(similarities, threshold)

            # Get the cumulative token count`s at the split indices

            split_token_counts = np.diff(cumulative_token_counts[split_indices])

            # Get the median of the split token counts
            # median_split_token_count = np.median(split_token_counts)
            # Check if the split respects the chunk size
            # if self.min_chunk_size * 1.1 <= median_split_token_count <= 0.95 * self.chunk_size:
            # break
            # elif median_split_token_count > 0.95 * self.chunk_size:
            # The code is calculating the median of a list of token counts stored in the variable
            # `split_token_counts` using the `np.median()` function from the NumPy library in Python.
            #     low = threshold + self.threshold_step
            # else:
            #     high = threshold - self.threshold_step

            # check if all the split token counts are between the min and max chunk size
            if self.min_chunk_size <= all(split_token_counts) <= self.chunk_size:
                break
            # check if any of the split token counts are greater than the max chunk size
            elif any(split_token_counts) > self.chunk_size:
                low = threshold + self.threshold_step
            # check if any of the split token counts are less than the min chunk size
            else:
                high = threshold - self.threshold_step

            iterations += 1
            if iterations > 10:
                warnings.warn(
                    "Too many iterations in threshold calculation, stopping...",
                    stacklevel=2,
                )
                break

        return threshold

    def _calculate_threshold_via_percentile(
        self, sentences: List[SemanticSentence]
    ) -> float:
        """Calculate similarity threshold via percentile."""
        # Compute all pairwise similarities, since the embeddings are already computed
        # The embeddings are computed assuming a similarity window is applied
        all_similarities = self._compute_window_similarities(sentences)
        return float(np.percentile(all_similarities, 100 - self.similarity_percentile))

    def _calculate_similarity_threshold(
        self, sentences: List[SemanticSentence]
    ) -> float:
        """Calculate similarity threshold either through the smart binary search or percentile."""
        if self.similarity_threshold is not None:
            return self.similarity_threshold
        elif self.similarity_percentile is not None:
            return self._calculate_threshold_via_percentile(sentences)
        else:
            return self._calculate_threshold_via_binary_search(sentences)

    def _group_sentences_cumulative(
        self, sentences: List[SemanticSentence]
    ) -> List[List[SemanticSentence]]:
        """Group sentences based on semantic similarity, ignoring token count limits.

        Args:
            sentences: List of SemanticSentence objects with precomputed embeddings

        Returns:
            List of sentence groups, where each group is semantically coherent

        """
        groups = []
        current_group = sentences[: self.min_sentences]
        current_embedding = self._compute_group_embedding(current_group)

        for sentence in sentences[self.min_sentences :]:
            # Compare new sentence against mean embedding of entire current group
            similarity = self._get_semantic_similarity(
                current_embedding, sentence.embedding
            )

            if similarity >= self.similarity_threshold:
                # Add to current group
                current_group.append(sentence)
                # Update mean embedding
                current_embedding = self._compute_group_embedding(current_group)
            else:
                # Start new group
                if current_group:
                    groups.append(current_group)
                current_group = [sentence]
                current_embedding = sentence.embedding

        # Add final group
        if current_group:
            groups.append(current_group)

        return groups

    def _group_sentences_window(
        self, sentences: List[Sentence]
    ) -> List[List[Sentence]]:
        """Group sentences based on semantic similarity, respecting the similarity window."""
        similarities = self._compute_window_similarities(
            sentences
        )  # NOTE: This is calculating pairwise, but not window.
        split_indices = self._get_split_indices(similarities, self.similarity_threshold)
        groups = [
            sentences[split_indices[i] : split_indices[i + 1]]
            for i in range(len(split_indices) - 1)
        ]
        return groups

    def _group_sentences(self, sentences: List[Sentence]) -> List[List[Sentence]]:
        """Group sentences based on semantic similarity, either cumulatively or by window."""
        if self.mode == "cumulative":
            return self._group_sentences_cumulative(sentences)
        else:
            return self._group_sentences_window(sentences)

    def _create_chunk(self, sentences: List[SemanticSentence]) -> SemanticChunk:
        """Create a chunk from a list of sentences."""
        if not sentences:
            raise ValueError("Cannot create chunk from empty sentence list")
        if self.return_type == "chunks":
            # Compute chunk text and token count from sentences
            text = "".join(sent.text for sent in sentences)
            token_count = sum(sent.token_count for sent in sentences)
            return SemanticChunk(
                text=text,
                start_index=sentences[0].start_index,
                end_index=sentences[-1].end_index,
                token_count=token_count,
                sentences=sentences,
            )
        elif self.return_type == "texts":
            return "".join(sent.text for sent in sentences)
        else:
            raise ValueError("Invalid return_type. Must be either 'chunks' or 'texts'.")

    def _split_chunks(
        self, sentence_groups: List[List[SemanticSentence]]
    ) -> List[SemanticChunk]:
        """Split sentence groups into chunks that respect chunk_size.

        Args:
            sentence_groups: List of semantically coherent sentence groups

        Returns:
            List of SemanticChunk objects

        """
        chunks = []

        for group in sentence_groups:
            current_chunk_sentences = []
            current_tokens = 0

            for sentence in group:
                test_tokens = (
                    current_tokens
                    + sentence.token_count
                    + (1 if current_chunk_sentences else 0)
                )

                if test_tokens <= self.chunk_size:
                    # Add to current chunk
                    current_chunk_sentences.append(sentence)
                    current_tokens = test_tokens
                else:
                    # Create chunk if we have sentences
                    if current_chunk_sentences:
                        chunks.append(self._create_chunk(current_chunk_sentences))

                    # Start new chunk with current sentence
                    current_chunk_sentences = [sentence]
                    current_tokens = sentence.token_count

            # Create final chunk for this group
            if current_chunk_sentences:
                chunks.append(self._create_chunk(current_chunk_sentences))

        return chunks

    def chunk(self, text: str) -> List[SemanticChunk]:
        """Split text into semantically coherent chunks using two-pass approach.

        First groups sentences by semantic similarity, then splits groups to respect
        chunk_size while maintaining sentence boundaries.

        Args:
            text: Input text to be chunked

        Returns:
            List of SemanticChunk objects containing the chunked text and metadata

        """
        if not text.strip():
            return []

        # Prepare sentences with precomputed information
        sentences = self._prepare_sentences(text)
        if len(sentences) <= self.min_sentences:
            return [self._create_chunk(sentences)]

        # Calculate similarity threshold
        self.similarity_threshold = self._calculate_similarity_threshold(sentences)

        # First pass: Group sentences by semantic similarity
        sentence_groups = self._group_sentences(sentences)

        # Second pass: Split groups into size-appropriate chunks
        chunks = self._split_chunks(sentence_groups)

        return chunks

    def _import_dependencies(self) -> None:
        """Lazy import dependencies for the chunker implementation.

        This method should be implemented by all chunker implementations that require
        additional dependencies. It lazily imports the dependencies only when they are needed.
        """
        if importutil.find_spec("numpy"):
            global np
            import numpy as np
        else:
            raise ImportError(
                "numpy is not available. Please install it via `pip install chonkie[semantic]`"
            )

    def __repr__(self) -> str:
        """Return a string representation of the SemanticChunker."""
        return (
            f"SemanticChunker(model={self.embedding_model}, "
            f"chunk_size={self.chunk_size}, "
            f"mode={self.mode}, "
            f"threshold={self.threshold}, "
            f"similarity_window={self.similarity_window}, "
            f"min_sentences={self.min_sentences}, "
            f"min_chunk_size={self.min_chunk_size}, "
            f"return_type={self.return_type})"
        )
```

## File: `src/chonkie/chunker/sentence.py`
```python
"""Sentence chunker."""

import warnings
from bisect import bisect_left
from itertools import accumulate
from typing import Any, Callable, List, Literal, Optional, Union

from chonkie.types.base import Chunk
from chonkie.types.sentence import Sentence, SentenceChunk

from .base import BaseChunker


class SentenceChunker(BaseChunker):
    """SentenceChunker splits the sentences in a text based on token limits and sentence boundaries.

    Args:
        tokenizer_or_token_counter: The tokenizer instance to use for encoding/decoding
        chunk_size: Maximum number of tokens per chunk
        chunk_overlap: Number of tokens to overlap between chunks
        min_sentences_per_chunk: Minimum number of sentences per chunk (defaults to 1)
        min_characters_per_sentence: Minimum number of characters per sentence
        approximate: Whether to use approximate token counting (defaults to True)
        delim: Delimiters to split sentences on
        include_delim: Whether to include delimiters in current chunk, next chunk or not at all (defaults to "prev")
        return_type: Whether to return chunks or texts

    Raises:
        ValueError: If parameters are invalid

    """

    def __init__(
        self,
        tokenizer_or_token_counter: Union[str, Callable, Any] = "gpt2",
        chunk_size: int = 512,
        chunk_overlap: int = 0,
        min_sentences_per_chunk: int = 1,
        min_characters_per_sentence: int = 12,
        approximate: bool = True,
        delim: Union[str, List[str]] = [".", "!", "?", "\n"],
        include_delim: Optional[Literal["prev", "next"]] = "prev",
        return_type: Literal["chunks", "texts"] = "chunks",
    ):
        """Initialize the SentenceChunker with configuration parameters.

        SentenceChunker splits the sentences in a text based on token limits and sentence boundaries.

        Args:
            tokenizer_or_token_counter: The tokenizer instance to use for encoding/decoding (defaults to "gpt2")
            chunk_size: Maximum number of tokens per chunk (defaults to 512)
            chunk_overlap: Number of tokens to overlap between chunks (defaults to 0)
            min_sentences_per_chunk: Minimum number of sentences per chunk (defaults to 1)
            min_characters_per_sentence: Minimum number of characters per sentence (defaults to 12)
            approximate: Whether to use approximate token counting (defaults to True)
            delim: Delimiters to split sentences on (defaults to [".", "!", "?", "newline"])
            include_delim: Whether to include delimiters in current chunk, next chunk or not at all (defaults to "prev")
            return_type: Whether to return chunks or texts (defaults to "chunks")

        Raises:
            ValueError: If parameters are invalid

        """
        super().__init__(tokenizer_or_token_counter=tokenizer_or_token_counter)

        if chunk_size <= 0:
            raise ValueError("chunk_size must be positive")
        if chunk_overlap >= chunk_size:
            raise ValueError("chunk_overlap must be less than chunk_size")
        if min_sentences_per_chunk < 1:
            raise ValueError("min_sentences_per_chunk must be at least 1")
        if min_characters_per_sentence < 1:
            raise ValueError("min_characters_per_sentence must be at least 1")
        if delim is None:
            raise ValueError("delim must be a list of strings or a string")
        if include_delim not in ["prev", "next", None]:
            raise ValueError("include_delim must be 'prev', 'next' or None")
        if return_type not in ["chunks", "texts"]:
            raise ValueError("Invalid return_type. Must be either 'chunks' or 'texts'.")

        # Assign the values if they make sense
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.min_sentences_per_chunk = min_sentences_per_chunk
        self.min_characters_per_sentence = min_characters_per_sentence
        self.approximate = approximate
        self.delim = delim
        self.include_delim = include_delim
        self.sep = "✄"
        self.return_type = return_type

    def _split_sentences(self, text: str) -> List[str]:
        """Fast sentence splitting while maintaining accuracy.

        This method is faster than using regex for sentence splitting and is more accurate than using the spaCy sentence tokenizer.

        Args:
            text: Input text to be split into sentences

        Returns:
            List of sentences

        """
        t = text
        for c in self.delim:
            if self.include_delim == "prev":
                t = t.replace(c, c + self.sep)
            elif self.include_delim == "next":
                t = t.replace(c, self.sep + c)
            else:
                t = t.replace(c, self.sep)

        # Initial split
        splits = [s for s in t.split(self.sep) if s != ""]

        # Combine short splits with previous sentence
        current = ""
        sentences = []
        for s in splits:
            # If the split is short, add to current and if long add to sentences
            if len(s) < self.min_characters_per_sentence:
                current += s
            elif current:
                current += s
                sentences.append(current)
                current = ""
            else:
                sentences.append(s)

            # At any point if the current sentence is longer than the min_characters_per_sentence,
            # add it to the sentences
            if len(current) >= self.min_characters_per_sentence:
                sentences.append(current)
                current = ""

        # If there is a current split, add it to the sentences
        if current:
            sentences.append(current)

        return sentences

    def _estimate_token_counts(self, sentences: Union[str, List[str]]) -> int:
        """Estimate token count using character length."""
        CHARS_PER_TOKEN = 6.0  # Avg. char per token for llama3 is b/w 6-7
        if type(sentences) is str:
            return max(1, len(sentences) // CHARS_PER_TOKEN)
        elif type(sentences) is list and type(sentences[0]) is str:
            return [max(1, len(t) // CHARS_PER_TOKEN) for t in sentences]
        else:
            raise ValueError(
                f"Unknown type passed to _estimate_token_count: {type(sentences)}"
            )

    def _get_feedback(self, estimate: int, actual: int) -> float:
        """Validate against the actual token counts and correct the estimates."""
        estimate, actual = max(1, estimate), max(1, actual)
        feedback = max(0.01, 1 - ((estimate - actual) / estimate))
        return feedback

    def _prepare_sentences(self, text: str) -> List[Sentence]:
        """Split text into sentences and calculate token counts for each sentence.

        Args:
            text: Input text to be split into sentences

        Returns:
            List of Sentence objects

        """
        # Split text into sentences
        sentence_texts = self._split_sentences(text)
        if not sentence_texts:
            return []

        # Calculate positions once
        positions = []
        current_pos = 0
        for sent in sentence_texts:
            positions.append(current_pos)
            current_pos += len(
                sent
            )  # No +1 space because sentences are already separated by spaces

        if not self.approximate:
            # Get accurate token counts in batch
            token_counts = self.tokenizer.count_tokens_batch(sentence_texts)
        else:
            # Estimate token counts using character length
            token_counts = self._estimate_token_counts(sentence_texts)

        # Create sentence objects
        return [
            Sentence(
                text=sent,
                start_index=pos,
                end_index=pos + len(sent),
                token_count=count,
            )
            for sent, pos, count in zip(sentence_texts, positions, token_counts)
        ]

    def _create_chunk(self, sentences: List[Sentence], token_count: int) -> Chunk:
        """Create a chunk from a list of sentences.

        Args:
            sentences: List of sentences to create chunk from
            token_count: Total token count for the chunk

        Returns:
            Chunk object

        """
        chunk_text = "".join([sentence.text for sentence in sentences])
        if self.return_type == "texts":
            return chunk_text
        else:
            return SentenceChunk(
                text=chunk_text,
                start_index=sentences[0].start_index,
                end_index=sentences[-1].end_index,
                token_count=token_count,
                sentences=sentences,
            )

    def chunk(self, text: str) -> List[Chunk]:
        """Split text into overlapping chunks based on sentences while respecting token limits.

        Args:
            text: Input text to be chunked

        Returns:
            List of Chunk objects containing the chunked text and metadata

        """
        if not text.strip():
            return []

        # Get prepared sentences with token counts
        sentences = self._prepare_sentences(text)  # 28mus
        if not sentences:
            return []

        # Pre-calculate cumulative token counts for bisect
        # Add 1 token for spaces between sentences
        token_sums = list(
            accumulate(
                [s.token_count for s in sentences],
                lambda a, b: a + b,
                initial=0,
            )
        )

        chunks = []
        feedback = 1.0
        pos = 0

        while pos < len(sentences):
            # use updated feedback on the token sums
            token_sums = [int(s * feedback) for s in token_sums]

            # Use bisect_left to find initial split point
            target_tokens = token_sums[pos] + self.chunk_size
            split_idx = bisect_left(token_sums, target_tokens) - 1
            split_idx = min(split_idx, len(sentences))

            # Ensure we include at least one sentence beyond pos
            split_idx = max(split_idx, pos + 1)

            # Handle minimum sentences requirement
            if split_idx - pos < self.min_sentences_per_chunk:
                # If the minimum sentences per chunk can be met, set the split index to the minimum sentences per chunk
                # Otherwise, warn the user that the minimum sentences per chunk could not be met for all chunks
                if pos + self.min_sentences_per_chunk <= len(sentences):
                    split_idx = pos + self.min_sentences_per_chunk
                else:
                    warnings.warn(
                        f"Minimum sentences per chunk as {self.min_sentences_per_chunk} could not be met for all chunks. "
                        + f"Last chunk of the text will have only {len(sentences) - pos} sentences. "
                        + "Consider increasing the chunk_size or decreasing the min_sentences_per_chunk."
                    )
                    split_idx = len(sentences)

            # Get the estimated token count
            estimate = token_sums[split_idx] - token_sums[pos]

            # Get candidate sentences and verify actual token count
            chunk_sentences = sentences[pos:split_idx]
            chunk_text = "".join(s.text for s in chunk_sentences)
            actual = self.tokenizer.count_tokens(chunk_text)

            # Given the actual token_count and the estimate, get a feedback value for the next loop
            feedback = self._get_feedback(estimate, actual)
            # print(f"Estimate: {estimate} Actual: {actual} feedback: {feedback}")

            # Back off one sentence at a time if we exceeded chunk size
            while (
                actual > self.chunk_size
                and len(chunk_sentences) > self.min_sentences_per_chunk
            ):
                split_idx -= 1
                chunk_sentences = sentences[pos:split_idx]
                chunk_text = "".join(s.text for s in chunk_sentences)
                actual = self.tokenizer.count_tokens(chunk_text)

            chunks.append(self._create_chunk(chunk_sentences, actual))

            # Calculate next position with overlap
            if self.chunk_overlap > 0 and split_idx < len(sentences):
                # Calculate how many sentences we need for overlap
                overlap_tokens = 0
                overlap_idx = split_idx - 1

                while overlap_idx > pos and overlap_tokens < self.chunk_overlap:
                    sent = sentences[overlap_idx]
                    next_tokens = overlap_tokens + sent.token_count + 1  # +1 for space
                    if next_tokens > self.chunk_overlap:
                        break
                    overlap_tokens = next_tokens
                    overlap_idx -= 1

                # Move position to after the overlap
                pos = overlap_idx + 1
            else:
                pos = split_idx

        return chunks

    def __repr__(self) -> str:
        """Return a string representation of the SentenceChunker."""
        return (
            f"SentenceChunker(tokenizer={self.tokenizer}, "
            f"chunk_size={self.chunk_size}, "
            f"chunk_overlap={self.chunk_overlap}, "
            f"min_sentences_per_chunk={self.min_sentences_per_chunk}, "
            f"min_characters_per_sentence={self.min_characters_per_sentence}, "
            f"approximate={self.approximate}, delim={self.delim}, "
            f"include_delim={self.include_delim}, "
            f"return_type={self.return_type})"
        )
```

## File: `src/chonkie/chunker/token.py`
```python
"""Module containing TokenChunker class.

This module provides a TokenChunker class for splitting text into chunks of a specified token size.

"""

from typing import Any, Generator, List, Literal, Sequence, Union

from tqdm import trange

from chonkie.chunker.base import BaseChunker
from chonkie.types.base import Chunk


class TokenChunker(BaseChunker):
    """Chunker that splits text into chunks of a specified token size.

    Args:
        tokenizer: The tokenizer instance to use for encoding/decoding
        chunk_size: Maximum number of tokens per chunk
        chunk_overlap: Number of tokens to overlap between chunks
        return_type: Whether to return chunks or texts

    """

    def __init__(
        self,
        tokenizer: Union[str, Any] = "gpt2",
        chunk_size: int = 512,
        chunk_overlap: Union[int, float] = 0,
        return_type: Literal["chunks", "texts"] = "chunks",
    ) -> None:
        """Initialize the TokenChunker with configuration parameters.

        Args:
            tokenizer: The tokenizer instance to use for encoding/decoding
            chunk_size: Maximum number of tokens per chunk
            chunk_overlap: Number of tokens to overlap between chunks
            return_type: Whether to return chunks or texts

        Raises:
            ValueError: If chunk_size <= 0 or chunk_overlap >= chunk_size

        """
        super().__init__(tokenizer)
        if chunk_size <= 0:
            raise ValueError("chunk_size must be positive")
        if isinstance(chunk_overlap, int) and chunk_overlap >= chunk_size:
            raise ValueError("chunk_overlap must be less than chunk_size")
        if return_type not in ["chunks", "texts"]:
            raise ValueError("return_type must be either 'chunks' or 'texts'")

        # Assign the values if they make sense
        self.return_type = return_type
        self.chunk_size = chunk_size
        self.chunk_overlap = (
            chunk_overlap
            if isinstance(chunk_overlap, int)
            else int(chunk_overlap * chunk_size)
        )

        self._use_multiprocessing = False

    def _create_chunks(
        self,
        chunk_texts: List[str],
        token_groups: List[List[int]],
        token_counts: List[int],
    ) -> Sequence[Chunk]:
        """Create chunks from a list of texts."""
        # Find the overlap lengths for index calculation
        if self.chunk_overlap > 0:
            # we get the overlap texts, that gives you the start_index for the next chunk
            # if the token group is smaller than the overlap, we just use the whole token group
            overlap_texts = self.tokenizer.decode_batch([
                token_group[-self.chunk_overlap :]
                if (len(token_group) > self.chunk_overlap)
                else token_group
                for token_group in token_groups
            ])
            overlap_lengths = [len(overlap_text) for overlap_text in overlap_texts]
        else:
            overlap_lengths = [0] * len(token_groups)

        # Create the chunks
        chunks = []
        current_index = 0
        for chunk_text, overlap_length, token_count in zip(
            chunk_texts, overlap_lengths, token_counts
        ):
            start_index = current_index
            end_index = start_index + len(chunk_text)
            chunks.append(
                Chunk(
                    text=chunk_text,
                    start_index=start_index,
                    end_index=end_index,
                    token_count=token_count,
                )
            )
            current_index = end_index - overlap_length

        return chunks

    def _token_group_generator(
        self, tokens: List[int]
    ) -> Generator[List[int], None, None]:
        """Generate chunks from a list of tokens."""
        for start in range(0, len(tokens), self.chunk_size - self.chunk_overlap):
            end = min(start + self.chunk_size, len(tokens))
            yield tokens[start:end]
            if end == len(tokens):
                break

    def chunk(self, text: str) -> Sequence[Chunk]:
        """Split text into overlapping chunks of specified token size.

        Args:
            text: Input text to be chunked

        Returns:
            List of Chunk objects containing the chunked text and metadata

        """
        if not text.strip():
            return []

        # Encode full text
        text_tokens = self.tokenizer.encode(text)

        # Calculate token groups and counts
        token_groups = list(self._token_group_generator(text_tokens))

        # if return_type is chunks, we need to decode the token groups into the chunk texts
        if self.return_type == "chunks":
            token_counts = [len(toks) for toks in token_groups]

            # decode the token groups into the chunk texts
            chunk_texts = self.tokenizer.decode_batch(token_groups)

            # Create the chunks from the token groups and token counts
            chunks = self._create_chunks(chunk_texts, token_groups, token_counts)

            return chunks
        # if return_type is texts, we can just return the decoded token groups
        elif self.return_type == "texts":
            return self.tokenizer.decode_batch(token_groups)

    def _process_batch(self, texts: List[str]) -> Sequence[Sequence[Chunk]]:
        """Process a batch of texts."""
        # encode the texts into tokens in a batch
        tokens_list = self.tokenizer.encode_batch(texts)
        result = []

        for tokens in tokens_list:
            if not tokens:
                result.append([])
                continue

            # get the token groups
            token_groups = list(self._token_group_generator(tokens))

            if self.return_type == "chunks":
                # get the token counts
                token_counts = [len(token_group) for token_group in token_groups]

                # decode the token groups into the chunk texts
                chunk_texts = self.tokenizer.decode_batch(token_groups)

                # create the chunks from the token groups and token counts
                chunks = self._create_chunks(chunk_texts, token_groups, token_counts)
                result.append(chunks)
            elif self.return_type == "texts":
                result.append(self.tokenizer.decode_batch(token_groups))
            else:
                raise ValueError(
                    "Invalid return_type. Must be either 'chunks' or 'texts'."
                )

        return result

    def chunk_batch(
        self,
        texts: List[str],
        batch_size: int = 1,
        show_progress_bar: bool = True,
    ) -> Sequence[Sequence[Chunk]]:
        """Split a batch of texts into their respective chunks.

        Args:
            texts: List of input texts to be chunked
            batch_size: Number of texts to process in a single batch
            show_progress_bar: Whether to show a progress bar

        Returns:
            List of lists of Chunk objects containing the chunked text and metadata

        """
        chunks = []
        for i in trange(
            0,
            len(texts),
            batch_size,
            desc="🦛",
            disable=not show_progress_bar,
            unit="batch",
            bar_format="{desc} ch{bar:20}nk {percentage:3.0f}% • {n_fmt}/{total_fmt} batches chunked [{elapsed}<{remaining}, {rate_fmt}] 🌱",
            ascii=" o",
        ):
            batch_texts = texts[i : min(i + batch_size, len(texts))]
            chunks.extend(self._process_batch(batch_texts))
        return chunks

    def __call__(
        self,
        text: Union[str, List[str]],
        batch_size: int = 1,
        show_progress_bar: bool = True,
    ) -> Union[Sequence[Chunk], Sequence[Sequence[Chunk]]]:
        """Make the TokenChunker callable directly.

        Args:
            text: Input text or list of texts to be chunked
            batch_size: Number of texts to process in a single batch
            show_progress_bar: Whether to show a progress bar (for batch chunking)

        Returns:
            List of Chunk objects or list of lists of Chunk

        """
        if isinstance(text, str):
            return self.chunk(text)
        elif isinstance(text, list) and isinstance(text[0], str):
            return self.chunk_batch(text, batch_size, show_progress_bar)
        else:
            raise ValueError(
                "Invalid input type. Expected a string or a list of strings."
            )

    def __repr__(self) -> str:
        """Return a string representation of the TokenChunker."""
        return (
            f"TokenChunker(tokenizer={self.tokenizer}, "
            f"chunk_size={self.chunk_size}, "
            f"chunk_overlap={self.chunk_overlap}, "
            f"return_type={self.return_type})"
        )
```

## File: `src/chonkie/cloud/__init__.py`
```python
"""Module for Chonkie Cloud APIs."""

from chonkie.cloud.chunkers import (
    CloudChunker,
    RecursiveChunker,
    SemanticChunker,
    SentenceChunker,
    TokenChunker,
)

__all__ = [
    "CloudChunker",
    "TokenChunker",
    "RecursiveChunker",
    "SemanticChunker",
    "SentenceChunker",
]
```

## File: `src/chonkie/cloud/chunkers/__init__.py`
```python
"""Module for Chonkie Cloud Chunkers."""

from chonkie.cloud.chunkers.base import CloudChunker
from chonkie.cloud.chunkers.recursive import RecursiveChunker
from chonkie.cloud.chunkers.semantic import SemanticChunker
from chonkie.cloud.chunkers.sentence import SentenceChunker
from chonkie.cloud.chunkers.token import TokenChunker

__all__ = [
    "CloudChunker",
    "RecursiveChunker",
    "SemanticChunker",
    "TokenChunker",
    "SentenceChunker",
]
```

## File: `src/chonkie/cloud/chunkers/base.py`
```python
"""Base class for all cloud chunking algorithms."""

from abc import ABC, abstractmethod
from typing import Dict, List, Union


class CloudChunker(ABC):
    """Base class for all cloud chunking algorithms."""

    BASE_URL = "https://api.chonkie.ai"
    VERSION = "v1"

    @abstractmethod
    def chunk(self, text: Union[str, List[str]]) -> List[Dict]:
        """Chunk the text into a list of chunks."""
        pass

    def __call__(self, text: Union[str, List[str]]) -> List[Dict]:
        """Call the chunker."""
        return self.chunk(text)
```

## File: `src/chonkie/cloud/chunkers/recursive.py`
```python
"""Recursive Chunking for Chonkie API."""

import os
from typing import Callable, Dict, List, Literal, Optional, Union, cast

import requests

from chonkie.cloud.chunkers.base import CloudChunker
from chonkie.types import RecursiveRules


class RecursiveChunker(CloudChunker):
    """Recursive Chunking for Chonkie API."""

    BASE_URL = "https://api.chonkie.ai"
    VERSION = "v1"
    API_KEY = os.getenv("CHONKIE_API_KEY")

    def __init__(
        self,
        tokenizer_or_token_counter: Union[str, Callable] = "gpt2",
        chunk_size: int = 512,
        min_characters_per_chunk: int = 12,
        rules: RecursiveRules = RecursiveRules(),
        return_type: Literal["texts", "chunks"] = "chunks",
        api_key: Optional[str] = None,
    ) -> None:
        """Initialize the RecursiveChunker."""
        # If no API key is provided, use the environment variable
        self.api_key = api_key or os.getenv("CHONKIE_API_KEY")
        if not self.api_key:
            raise ValueError(
                "No API key provided. Please set the CHONKIE_API_KEY environment variable"
                + "or pass an API key to the RecursiveChunker constructor."
            )

        # Check if the chunk size is valid
        if chunk_size <= 0:
            raise ValueError("Chunk size must be greater than 0.")
        if min_characters_per_chunk < 1:
            raise ValueError("Minimum characters per chunk must be greater than 0.")
        if return_type not in ["texts", "chunks"]:
            raise ValueError("Return type must be either 'texts' or 'chunks'.")

        # Add attributes
        self.tokenizer_or_token_counter = tokenizer_or_token_counter
        self.chunk_size = chunk_size
        self.min_characters_per_chunk = min_characters_per_chunk
        self.rules = rules
        self.return_type = return_type

        # Check if the API is up right now
        response = requests.get(f"{self.BASE_URL}/")
        if response.status_code != 200:
            raise ValueError(
                "Oh no! You caught Chonkie at a bad time. It seems to be down right now."
                + "Please try again in a short while."
                + "If the issue persists, please contact support at support@chonkie.ai."
            )

    def chunk(self, text: Union[str, List[str]]) -> List[Dict]:
        """Chunk the text into a list of chunks."""
        # Make the payload
        payload = {
            "text": text,
            "tokenizer_or_token_counter": self.tokenizer_or_token_counter,
            "chunk_size": self.chunk_size,
            "min_characters_per_chunk": self.min_characters_per_chunk,
            "rules": self.rules.to_dict(),
            "return_type": self.return_type,
        }
        # Make the request to the Chonkie API
        response = requests.post(
            f"{self.BASE_URL}/{self.VERSION}/chunk/recursive",
            json=payload,
            headers={"Authorization": f"Bearer {self.api_key}"},
        )

        # Try to parse the response
        try:
            result: List[Dict] = cast(List[Dict], response.json())
        except Exception as error:
            raise ValueError(
                "Oh no! The Chonkie API returned an invalid response."
                + "Please try again in a short while."
                + "If the issue persists, please contact support at support@chonkie.ai."
            ) from error

        return result

    def __call__(self, text: Union[str, List[str]]) -> List[Dict]:
        """Call the RecursiveChunker."""
        return self.chunk(text)
```

## File: `src/chonkie/cloud/chunkers/semantic.py`
```python
"""Semantic Chunking for Chonkie API."""

import os
from typing import Dict, List, Literal, Optional, Union, cast

import requests

from chonkie.cloud.chunkers.base import CloudChunker


class SemanticChunker(CloudChunker):
    """Semantic Chunking for Chonkie API."""

    BASE_URL = "https://api.chonkie.ai"
    VERSION = "v1"
    API_KEY = os.getenv("CHONKIE_API_KEY")

    def __init__(self,
                 embedding_model: str = "minishlab/potion-base-32M",
                 chunk_size: int = 512,
                 threshold: Union[Literal["auto"], float, int] = "auto",
                 similarity_window: int = 1,
                 min_sentences: int = 1,
                 min_chunk_size: int = 2,
                 min_characters_per_sentence: int = 12,
                 threshold_step: float = 0.01,
                 delim: Union[str, List[str]] = [".", "!", "?", "\n"],
                 include_delim: Optional[Literal["prev", "next"]] = "prev",
                 return_type: Literal["chunks", "texts"] = "chunks",
                 api_key: Optional[str] = None,
                 ) -> None:
        """Initialize the Chonkie Cloud Semantic Chunker."""
        # Get the API key
        self.api_key = api_key or os.getenv("CHONKIE_API_KEY")
        if not self.api_key:
            raise ValueError("No API key provided. Please set the CHONKIE_API_KEY environment variable" +
                             "or pass an API key to the SemanticChunker constructor.")
        
        # Check if the chunk size is valid
        if chunk_size <= 0:
            raise ValueError("Chunk size must be greater than 0.")
        
        # Check if the threshold is valid
        if isinstance(threshold, str) and threshold != "auto":
            raise ValueError("Threshold must be either 'auto' or a number between 0 and 1.")
        elif isinstance(threshold, (float, int)) and (threshold <= 0 or threshold > 1):
            raise ValueError("Threshold must be between 0 and 1.")
        
        # Check if the similarity window is valid
        if similarity_window <= 0:
            raise ValueError("Similarity window must be greater than 0.")
        
        # Check if the minimum sentences is valid
        if min_sentences <= 0:
            raise ValueError("Minimum sentences must be greater than 0.")
        
        # Check if the minimum chunk size is valid
        if min_chunk_size <= 0:
            raise ValueError("Minimum chunk size must be greater than 0.")
        
        # Check if the minimum characters per sentence is valid
        if min_characters_per_sentence <= 0:
            raise ValueError("Minimum characters per sentence must be greater than 0.")
        
        # Check if the threshold step is valid
        if threshold_step <= 0 or threshold_step > 1:
            raise ValueError("Threshold step must be greater than 0 and less than or equal to 1.")
        
        # Check if the delim is valid
        if not isinstance(delim, (list, str)):
            raise ValueError("Delim must be a list or a string.")
        
        # Check if the include delim is valid
        if include_delim not in ["prev", "next", None]:
            raise ValueError("Include delim must be either 'prev', 'next', or None.")
        
        # Check if the return type is valid
        if return_type not in ["chunks", "texts"]:
            raise ValueError("Return type must be either 'chunks' or 'texts'.")
        
        # Add all the attributes
        self.embedding_model = embedding_model
        self.chunk_size = chunk_size
        self.threshold = threshold
        self.similarity_window = similarity_window
        self.min_sentences = min_sentences
        self.min_chunk_size = min_chunk_size
        self.min_characters_per_sentence = min_characters_per_sentence
        self.threshold_step = threshold_step
        self.delim = delim
        self.include_delim = include_delim
        self.return_type = return_type

        # Check if the API is up right now
        response = requests.get(f"{self.BASE_URL}/")
        if response.status_code != 200:
            raise ValueError("Oh no! You caught Chonkie at a bad time. It seems to be down right now." +
                             "Please try again in a short while." +
                             "If the issue persists, please contact support at support@chonkie.ai.")
    
    def chunk(self, text: Union[str, List[str]]) -> List[Dict]:
        """Chunk the text into a list of chunks."""
        # Make the payload
        payload = {
            "text": text,
            "embedding_model": self.embedding_model,
            "chunk_size": self.chunk_size,
            "threshold": self.threshold,
            "similarity_window": self.similarity_window,
            "min_sentences": self.min_sentences,
            "min_chunk_size": self.min_chunk_size,
            "min_characters_per_sentence": self.min_characters_per_sentence,
            "threshold_step": self.threshold_step,
            "delim": self.delim,
            "include_delim": self.include_delim,
            "return_type": self.return_type,
        }
        
        # Make the request to the Chonkie API
        response = requests.post(
            f"{self.BASE_URL}/{self.VERSION}/chunk/semantic",
            json=payload,
            headers={"Authorization": f"Bearer {self.api_key}"}
        )
        
        # Try to parse the response
        try:
            result: List[Dict]  = cast(List[Dict], response.json())
        except Exception as error:
            raise ValueError("Oh no! The Chonkie API returned an invalid response." +
                             "Please try again in a short while." +
                             "If the issue persists, please contact support at support@chonkie.ai.") from error

        return result
    
    def __call__(self, text: Union[str, List[str]]) -> List[Dict]:
        """Call the chunker."""
        return self.chunk(text)
```

## File: `src/chonkie/cloud/chunkers/sentence.py`
```python
"""Sentence Chunking for Chonkie API."""

import os
from typing import Dict, List, Literal, Optional, Union, cast

import requests

from chonkie.cloud.chunkers.base import CloudChunker


class SentenceChunker(CloudChunker):
    """Sentence Chunking for Chonkie API."""

    BASE_URL = "https://api.chonkie.ai"
    VERSION = "v1"
    API_KEY = os.getenv("CHONKIE_API_KEY")

    def __init__(
        self,
        tokenizer_or_token_counter: str = "gpt2",
        chunk_size: int = 512,
        chunk_overlap: int = 0,
        min_sentences_per_chunk: int = 1,
        min_characters_per_sentence: int = 12,
        approximate: bool = True,
        delim: Union[str, List[str]] = [".", "!", "?", "\n"],
        include_delim: Union[Literal["prev", "next"], None] = "prev",
        return_type: Literal["texts", "chunks"] = "chunks",
        api_key: Optional[str] = None,
    ) -> None:
        """Initialize the SentenceChunker."""
        # If no API key is provided, use the environment variable
        self.api_key = api_key or os.getenv("CHONKIE_API_KEY")
        if not self.api_key:
            raise ValueError(
                "No API key provided. Please set the CHONKIE_API_KEY environment variable"
                + "or pass an API key to the SentenceChunker constructor."
            )

        # Check if chunk_size and chunk_overlap are valid
        if chunk_size <= 0:
            raise ValueError("Chunk size must be greater than 0.")
        if chunk_overlap < 0:
            raise ValueError("Chunk overlap must be greater than or equal to 0.")
        if min_sentences_per_chunk < 1:
            raise ValueError("Minimum sentences per chunk must be greater than 0.")
        if min_characters_per_sentence < 1:
            raise ValueError("Minimum characters per sentence must be greater than 0.")
        if approximate not in [True, False]:
            raise ValueError("Approximate must be either True or False.")
        if include_delim not in ["prev", "next", None]:
            raise ValueError("Include delim must be either 'prev', 'next' or None.")
        if return_type not in ["texts", "chunks"]:
            raise ValueError("Return type must be either 'texts' or 'chunks'.")

        # Assign all the attributes to the instance
        self.tokenizer_or_token_counter = tokenizer_or_token_counter
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.min_sentences_per_chunk = min_sentences_per_chunk
        self.min_characters_per_sentence = min_characters_per_sentence
        self.approximate = approximate
        self.delim = delim
        self.include_delim = include_delim
        self.return_type = return_type

        # Check if the API is up right now
        response = requests.get(f"{self.BASE_URL}/")
        if response.status_code != 200:
            raise ValueError(
                "Oh no! You caught Chonkie at a bad time. It seems to be down right now."
                + "Please try again in a short while."
                + "If the issue persists, please contact support at support@chonkie.ai or raise an issue on GitHub."
            )

    def chunk(self, text: Union[str, List[str]]) -> List[Dict]:
        """Chunk the text via sentence boundaries."""
        # Define the payload for the request
        payload = {
            "text": text,
            "tokenizer": self.tokenizer_or_token_counter,
            "chunk_size": self.chunk_size,
            "chunk_overlap": self.chunk_overlap,
            "min_sentences_per_chunk": self.min_sentences_per_chunk,
            "min_characters_per_sentence": self.min_characters_per_sentence,
            "approximate": self.approximate,
            "delim": self.delim,
            "include_delim": self.include_delim,
            "return_type": self.return_type,
        }

        # Make the request to the Chonkie API
        response = requests.post(
            f"{self.BASE_URL}/{self.VERSION}/chunk/sentence",
            json=payload,
            headers={"Authorization": f"Bearer {self.api_key}"},
        )

        # Parse the response
        result: List[Dict] = cast(List[Dict], response.json())
        return result

    def __call__(self, text: Union[str, List[str]]) -> List[Dict]:
        """Call the SentenceChunker."""
        return self.chunk(text)
```

## File: `src/chonkie/cloud/chunkers/token.py`
```python
"""Cloud Token Chunking for Chonkie API."""

import os
from typing import Dict, List, Literal, Optional, Union, cast

import requests

from chonkie.cloud.chunkers.base import CloudChunker


class TokenChunker(CloudChunker):
    """Token Chunking for Chonkie API."""

    BASE_URL = "https://api.chonkie.ai"
    VERSION = "v1"
    API_KEY = os.getenv("CHONKIE_API_KEY")

    def __init__(
        self,
        tokenizer: str,
        chunk_size: int,
        chunk_overlap: int,
        return_type: Literal["texts", "chunks"] = "chunks",
        api_key: Optional[str] = None,
    ) -> None:
        """Initialize the Cloud TokenChunker."""
        # If no API key is provided, use the environment variable
        self.api_key = api_key or os.getenv("CHONKIE_API_KEY")
        if not self.api_key:
            raise ValueError(
                "No API key provided. Please set the CHONKIE_API_KEY environment variable"
                + "or pass an API key to the TokenChunker constructor."
            )

        # Check if chunk_size and chunk_overlap are valid
        if chunk_size <= 0:
            raise ValueError("Chunk size must be greater than 0.")
        if chunk_overlap < 0:
            raise ValueError("Chunk overlap must be greater than or equal to 0.")

        # Check if return_type is valid
        if return_type not in ["texts", "chunks"]:
            raise ValueError("Return type must be either 'texts' or 'chunks'.")

        # Assign all the attributes to the instance
        self.tokenizer = tokenizer
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.return_type = return_type

        # Check if the API is up right now
        response = requests.get(f"{self.BASE_URL}/")
        if response.status_code != 200:
            raise ValueError(
                "Oh no! You caught Chonkie at a bad time. It seems to be down right now."
                + "Please try again in a short while."
                + "If the issue persists, please contact support at support@chonkie.ai or raise an issue on GitHub."
            )

    def chunk(self, text: Union[str, List[str]]) -> List[Dict]:
        """Chunk the text into a list of chunks."""
        # Define the payload for the request
        payload = {
            "text": text,
            "tokenizer": self.tokenizer,
            "chunk_size": self.chunk_size,
            "chunk_overlap": self.chunk_overlap,
            "return_type": self.return_type,
        }
        # Make the request to the Chonkie API
        response = requests.post(
            f"{self.BASE_URL}/{self.VERSION}/chunk/token",
            json=payload,
            headers={"Authorization": f"Bearer {self.api_key}"},
        )
        # Check if the response is successful
        if response.status_code != 200:
            raise ValueError(
                f"Error from the Chonkie API: {response.status_code} {response.text}"
            )

        # Parse the response
        try:
            result: List[Dict] = cast(List[Dict], response.json())
        except Exception as error:
            raise ValueError(f"Error parsing the response: {error}") from error

        # Return the result
        return result

    def __call__(self, text: Union[str, List[str]]) -> List[Dict]:
        """Call the chunker."""
        return self.chunk(text)
```

## File: `src/chonkie/embeddings/__init__.py`
```python
"""Embeddings classes for text embedding."""

from .auto import AutoEmbeddings
from .base import BaseEmbeddings
from .cohere import CohereEmbeddings
from .model2vec import Model2VecEmbeddings
from .openai import OpenAIEmbeddings
from .sentence_transformer import SentenceTransformerEmbeddings

# Add all embeddings classes to __all__
__all__ = [
    "BaseEmbeddings",
    "Model2VecEmbeddings",
    "SentenceTransformerEmbeddings",
    "OpenAIEmbeddings",
    "CohereEmbeddings",
    "AutoEmbeddings",
]
```

## File: `src/chonkie/embeddings/auto.py`
```python
"""AutoEmbeddings is a factory class for automatically loading embeddings."""

import warnings
from typing import Any, Union

from .base import BaseEmbeddings
from .registry import EmbeddingsRegistry


class AutoEmbeddings:

    """Factory class for automatically loading embeddings.

    This class provides a factory interface for loading embeddings based on an
    identifier string. It will try to find a matching embeddings implementation
    based on the identifier and load it with the provided arguments.


    Examples:
        # Get sentence transformers embeddings
        embeddings = AutoEmbeddings.get_embeddings("sentence-transformers/all-MiniLM-L6-v2")

        # Get OpenAI embeddings
        embeddings = AutoEmbeddings.get_embeddings("openai://text-embedding-ada-002", api_key="...")

        # Get Anthropic embeddings
        embeddings = AutoEmbeddings.get_embeddings("anthropic://claude-v1", api_key="...")

         # Get Cohere embeddings
        embeddings = AutoEmbeddings.get_embeddings("cohere://embed-english-light-v3.0", api_key="...")

    """

    @classmethod
    def get_embeddings(
        cls, model: Union[str, BaseEmbeddings, Any], **kwargs
    ) -> BaseEmbeddings:
        """Get embeddings instance based on identifier.

        Args:
            model: Identifier for the embeddings (name, path, URL, etc.)
            **kwargs: Additional arguments passed to the embeddings constructor

        Returns:
            Initialized embeddings instance

        Raises:
            ValueError: If no suitable embeddings implementation is found

        Examples:
            # Get sentence transformers embeddings
            embeddings = AutoEmbeddings.get_embeddings("sentence-transformers/all-MiniLM-L6-v2")

            # Get OpenAI embeddings
            embeddings = AutoEmbeddings.get_embeddings("openai://text-embedding-ada-002", api_key="...")

            # Get Anthropic embeddings
            embeddings = AutoEmbeddings.get_embeddings("anthropic://claude-v1", api_key="...")

            # Get Cohere embeddings
            embeddings = AutoEmbeddings.get_embeddings("cohere://embed-english-light-v3.0", api_key="...")

        """
        # Load embeddings instance if already provided
        if isinstance(model, BaseEmbeddings):
            return model
        elif isinstance(model, str):
            # Try to find matching implementation via registry
            try:
                embeddings_cls = EmbeddingsRegistry.match(model)
                if embeddings_cls and embeddings_cls.is_available():
                    try:
                        return embeddings_cls(model, **kwargs)
                    except Exception as e:
                        warnings.warn(
                            f"Failed to load {embeddings_cls.__name__}: {e}. Falling back to default {embeddings_cls} model."
                        )
                        return embeddings_cls(**kwargs)
            except Exception as error:
                warnings.warn(f"Failed to load embeddings via registry: {error}. Falling back to SentenceTransformerEmbeddings.")
                # Fall back to SentenceTransformerEmbeddings if no matching implementation is found
                from .sentence_transformer import SentenceTransformerEmbeddings

                try:
                    return SentenceTransformerEmbeddings(model, **kwargs)
                except Exception as e:
                    raise ValueError(
                        f"Failed to load embeddings via SentenceTransformerEmbeddings: {e}"
                    )
        else:
            # get the wrapped embeddings instance
            try:
                return EmbeddingsRegistry.wrap(model, **kwargs)
            except Exception as e:
                raise ValueError(f"Failed to wrap embeddings instance: {e}")
```

## File: `src/chonkie/embeddings/base.py`
```python
"""Base class for all embeddings implementations."""

import importlib.util as importutil
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any, Callable, List, Union

# for type checking
if TYPE_CHECKING:
    import numpy as np

class BaseEmbeddings(ABC):

    """Abstract base class for all embeddings implementations.

    All embeddings implementations should inherit from this class and implement
    the embed() and similarity() methods according to their specific embedding strategy.
    """

    def __init__(self):
        """Initialize the BaseEmbeddings class.

        This class should be inherited by all embeddings classes and implement the
        abstract methods for embedding text and computing similarity between embeddings.

        It doesn't impose any specific requirements on the embedding model, because
        it can be used for embeddings providers that work via REST APIs or other means.

        Raises:
            NotImplementedError: If any of the abstract methods are not implemented

        """
        # Lazy import dependencies if they are not already imported
        self._import_dependencies()

    @abstractmethod
    def embed(self, text: str) -> "np.ndarray":
        """Embed a text string into a vector representation.

        This method should be implemented for all embeddings models.

        Args:
            text (str): Text string to embed

        Returns:
            np.ndarray: Embedding vector for the text string

        """
        raise NotImplementedError

    def embed_batch(self, texts: List[str]) -> List["np.ndarray"]:
        """Embed a list of text strings into vector representations.

        This method should be implemented for embeddings models that support batch processing.

        By default, it calls the embed() method for each text in the list.

        Args:
            texts (List[str]): List of text strings to embed

        Returns:
            List[np.ndarray]: List of embedding vectors for each text in the list

        """
        return [self.embed(text) for text in texts]

    @abstractmethod
    def count_tokens(self, text: str) -> int:
        """Count the number of tokens in a text string.

        This method should be implemented for embeddings models that require tokenization
        before embedding.

        Args:
            text (str): Text string to count tokens for

        Returns:
            int: Number of tokens in the text string

        """
        raise NotImplementedError

    def count_tokens_batch(self, texts: List[str]) -> List[int]:
        """Count the number of tokens in a list of text strings.

        Args:
            texts (List[str]): List of text strings to count tokens for

        Returns:
            List[int]: List of token counts for each text in the list

        """
        return [self.count_tokens(text) for text in texts]
    
    @classmethod
    def _import_dependencies(cls) -> None:
        """Lazy import dependencies for the embeddings implementation.

        This method should be implemented by all embeddings implementations that require
        additional dependencies. It lazily imports the dependencies only when they are needed.
        """
        if cls.is_available():
            global np
            import numpy as np
        else:
            raise ImportError(
                "numpy is not available. Please install it via `pip install chonkie[semantic]`"
            ) 
        
    def similarity(self, u: "np.ndarray", v: "np.ndarray") -> float:
        """Compute the similarity between two embeddings.

        Most embeddings models will use cosine similarity for this purpose. However,
        other similarity metrics can be implemented as well. Some embeddings models
        may support a similarity() method that computes the similarity between two
        embeddings via dot product or other means.

        Args:
            u (np.ndarray): First embedding vector
            v (np.ndarray): Second embedding vector

        Returns:
            float: Similarity score between the two embeddings

        """
        return float(
            np.dot(u, v.T) / (np.linalg.norm(u) * np.linalg.norm(v))
        )  # cosine similarity

    @property
    @abstractmethod
    def dimension(self) -> int:
        """Return the dimension of the embedding vectors.

        This property should be implemented for embeddings models that have a fixed
        dimension for their embedding vectors.

        Returns:
            int: Dimension of the embedding vectors

        """
        raise NotImplementedError
    
    @classmethod
    def is_available(cls) -> bool:
        """Check if this embeddings implementation is available (dependencies installed).

        Override this method to add custom dependency checks.

        Returns:
            bool: True if the embeddings implementation is available, False otherwise

        """
        return importutil.find_spec("numpy") is not None
    
    def get_tokenizer_or_token_counter(self) -> Union[Any, Callable[[str], int]]:
        """Return the tokenizer or token counter object.

        By default, this method returns the count_tokens() method, which should be
        implemented for embeddings models that require tokenization before embedding.

        Returns:
            Union[Any, Callable[[str], int]]: Tokenizer object or token counter function

        Examples:
            # Get the tokenizer object
            tokenizer = embeddings.get_tokenizer_or_token_counter()

            # Get the token counter function
            token_counter = embeddings.get_tokenizer_or_token_counter()

        """
        return self.count_tokens

    def __repr__(self):
        """Representation of the BaseEmbeddings instance."""
        return self.__class__.__name__ + "()"

    def __call__(
        self, text: Union[str, List[str]]
    ) -> Union["np.ndarray", List["np.ndarray"]]:
        """Embed a text string into a vector representation.

        This method allows the embeddings object to be called directly with a text string
        or a list of text strings. It will call the embed() or embed_batch() method
        depending on the input type.

        Args:
            text (Union[str, List[str]]): Input text string or list of text strings

        Returns:
            Union[np.ndarray, List[np.ndarray]]: Single or list of embedding vectors

        """
        if isinstance(text, str):
            return self.embed(text)
        elif isinstance(text, list):
            return self.embed_batch(text)
        else:
            raise ValueError("Input must be a string or list of strings")
```

## File: `src/chonkie/embeddings/cohere.py`
```python
"""Embeddings implementation using Cohere's API."""

import importlib
import os
import warnings
from typing import TYPE_CHECKING, List, Optional

import requests

if TYPE_CHECKING:
    import numpy as np
    import tokenizers

from .base import BaseEmbeddings


class CohereEmbeddings(BaseEmbeddings):

    """Cohere embeddings implementation using their API."""

    AVAILABLE_MODELS = {
        # cohere v3.0 models
        "embed-english-v3.0": (True, 1024),  # tokenizer from tokenizers
        "embed-multilingual-v3.0": (
            False,
            1024,
        ),  # not listed in the cohere models api list
        "embed-english-light-v3.0": (True, 384),  # from tokenizers
        "embed-multilingual-light-v3.0": (
            False,
            384,
        ),  # not listed in the cohere models api list
        # cohere v2.0 models
        "embed-english-v2.0": (
            False,
            4096,
        ),  # url is not available in the cohere models api list
        "embed-english-light-v2.0": (False, 1024),  # not listed in the models list
        "embed-multilingual-v2.0": (True, 768),  # from tokenizers
    }

    DEFAULT_MODEL = "embed-english-light-v3.0"
    TOKENIZER_BASE_URL = "https://storage.googleapis.com/cohere-public/tokenizers/"

    def __init__(
        self,
        model: str = DEFAULT_MODEL,
        api_key: Optional[str] = None,
        client_name: Optional[str] = None,
        max_retries: int = 3,
        timeout: float = 60.0,
        batch_size: int = 96,
        show_warnings: bool = True,
    ):
        """Initialize Cohere embeddings.

        Args:
            model: name of the Cohere embedding model to use
            api_key: (optional) Cohere API key (if not provided, looks for COHERE_API_KEY environment variable)
            client_name: (optional) client name for API requests
            max_retries: maximum number of retries for failed requests
            timeout: timeout in seconds for API requests
            batch_size: maximum number of texts to embed in one API call (maximum allowed by Cohere is 96)
            show_warnings: whether to show warnings about token usage and truncation

        """
        super().__init__()

        # Lazy import dependencies if they are not already imported
        self._import_dependencies()

        if model not in self.AVAILABLE_MODELS:
            raise ValueError(
                f"Model {model} is not available. Choose from: {list(self.AVAILABLE_MODELS.keys())}"
            )

        self.model = model
        self._dimension = self.AVAILABLE_MODELS[model][1]
        tokenizer_url = (
            self.TOKENIZER_BASE_URL
            + (model if self.AVAILABLE_MODELS[model][0] else self.DEFAULT_MODEL)
            + ".json"
        )
        response = requests.get(tokenizer_url)
        self._tokenizer = tokenizers.Tokenizer.from_str(response.text)
        self._batch_size = min(batch_size, 96)  # max batch size for cohere is 96
        self._show_warnings = show_warnings
        self._max_retries = max_retries
        self._api_key = api_key or os.getenv("COHERE_API_KEY")

        if self._api_key is None:
            raise ValueError(
                "Cohere API key not found. Either pass it as api_key or set COHERE_API_KEY environment variable."
            )

        self.model = model
        self._dimension = self.AVAILABLE_MODELS[model][1]
        tokenizer_url = (
            self.TOKENIZER_BASE_URL
            + (model if self.AVAILABLE_MODELS[model][0] else self.DEFAULT_MODEL)
            + ".json"
        )
        response = requests.get(tokenizer_url)
        self._tokenizer = tokenizers.Tokenizer.from_str(response.text)
        self._batch_size = min(batch_size, 96)  # max batch size for cohere is 96
        self._show_warnings = show_warnings
        self._max_retries = max_retries
        self._api_key = api_key or os.getenv("COHERE_API_KEY")

        if self._api_key is None:
            raise ValueError(
                "Cohere API key not found. Either pass it as api_key or set COHERE_API_KEY environment variable."
            )

        # setup Cohere client
        self.client = ClientV2(
            api_key=api_key or os.getenv("COHERE_API_KEY"),
            client_name=client_name,
            timeout=timeout,
        )

    def embed(self, text: str) -> "np.ndarray":
        """Generate embeddings for a single text."""
        token_count = self.count_tokens(text)
        if (
            token_count > 512 and self._show_warnings
        ):  # Cohere models max_context_length
            warnings.warn(
                f"Text has {token_count} tokens which exceeds the model's context length of 512."
                "Generation may not be optimal"
            )

        for _ in range(self._max_retries):
            try:
                response = self.client.embed(
                    model=self.model,
                    input_type="search_document",
                    embedding_types=["float"],
                    texts=[text],
                )

                return np.array(response.embeddings.float_[0], dtype=np.float32)
            except Exception as e:
                if self._show_warnings:
                    warnings.warn(
                        f"There was an exception while generating embeddings. Exception: {str(e)}. Retrying..."
                    )

        raise RuntimeError("Unable to generate embeddings through Cohere.")

    def embed_batch(self, texts: List[str]) -> List["np.ndarray"]:
        """Get embeddings for multiple texts using batched API calls."""
        if not texts:
            return []

        all_embeddings = []

        # process in batches
        for i in range(0, len(texts), self._batch_size):
            batch = texts[i : i + self._batch_size]

            # check token_counts and warn if necessary
            token_counts = self.count_tokens_batch(batch)
            if self._show_warnings:
                for _, count in zip(batch, token_counts):
                    if count > 512:
                        warnings.warn(
                            f"Text has {count} tokens which exceeds the model's context length of 512."
                            "Generation may not be optimal."
                        )

            try:
                for _ in range(self._max_retries):
                    try:
                        response = self.client.embed(
                            model=self.model,
                            input_type="search_document",
                            embedding_types=["float"],
                            texts=batch,
                        )

                        embeddings = [
                            np.array(e, dtype=np.float32)
                            for e in response.embeddings.float_
                        ]
                        all_embeddings.extend(embeddings)
                        break
                    except Exception as e:
                        if self._show_warnings:
                            warnings.warn(
                                f"There was an exception while generating embeddings. Exception: {str(e)}. Retrying..."
                            )

            except Exception as e:
                # If the batch fails, try one by one
                if len(batch) > 1:
                    warnings.warn(
                        f"Batch embedding failed: {str(e)}. Trying one by one."
                    )
                    individual_embeddings = [self.embed(text) for text in batch]
                    all_embeddings.extend(individual_embeddings)
                else:
                    raise e

        return all_embeddings

    def count_tokens(self, text: str) -> int:
        """Count tokens in text using the model's tokenizer."""
        return len(self._tokenizer.encode(text, add_special_tokens=False))

    def count_tokens_batch(self, texts: List[str]) -> List[int]:
        """Count tokens in multiple texts."""
        tokens = self._tokenizer.encode_batch(texts, add_special_tokens=False)
        return [len(t) for t in tokens]

    def similarity(self, u: "np.ndarray", v: "np.ndarray") -> "np.float32":
        """Compute cosine similarity between two embeddings."""
        return np.divide(
            np.dot(u, v), np.linalg.norm(u) * np.linalg.norm(v), dtype=np.float32
        )

    @property
    def dimension(self) -> int:
        """Return the embedding dimension."""
        return self._dimension

    def get_tokenizer_or_token_counter(self) -> "tokenizers.Tokenizer":
        """Return a tokenizers tokenizer object of the current model."""
        return self._tokenizer

    @classmethod
    def is_available(cls) -> bool:
        """Check if the Cohere package is available."""
        return importlib.util.find_spec("cohere") is not None
    
    @classmethod
    def _import_dependencies(cls) -> None:
        """Lazy import dependencies for the embeddings implementation.

        This method should be implemented by all embeddings implementations that require
        additional dependencies. It lazily imports the dependencies only when they are needed.

        """
        if cls.is_available():
            global np, tokenizers, ClientV2
            import numpy as np
            import tokenizers
            from cohere import ClientV2
        else:
            raise ImportError(
                "cohere is not available. Please install it via `pip install chonkie[cohere]`"
            )
        
    def __repr__(self) -> str:
        """Return a string representation of the CohereEmbeddings object."""
        return f"CohereEmbeddings(model={self.model})"
```

## File: `src/chonkie/embeddings/model2vec.py`
```python
"""Model2Vec embeddings."""

import importlib.util as importutil
from typing import TYPE_CHECKING, List, Union

from chonkie.embeddings.base import BaseEmbeddings

if TYPE_CHECKING:
    import numpy as np
    from model2vec import StaticModel

class Model2VecEmbeddings(BaseEmbeddings):

    """Class for model2vec embeddings.

    This class provides an interface for the model2vec library, which provides a variety
    of pre-trained models for text embeddings.

    Args:
        model (str or StaticModel): Name of the model2vec model to load or a StaticModel instance

    """

    def __init__(
        self, model: Union[str, "StaticModel"] = "minishlab/potion-base-8M"
    ) -> None:
        """Initialize Model2VecEmbeddings with a str or StaticModel instance."""
        super().__init__()

        # Lazy import dependencies if they are not already imported
        self._import_dependencies()

        if isinstance(model, str):
            self.model_name_or_path = model
            self.model = StaticModel.from_pretrained(self.model_name_or_path)
        elif isinstance(model, StaticModel):
            self.model = model

            # TODO: `base_model_name` is mentioned in here -
            # https://github.com/MinishLab/model2vec/blob/b1358a9c2e777800e8f89c7a5f830fa2176c15b5/model2vec/model.py#L165`
            # but its `None` for potion models
            self.model_name_or_path = self.model.base_model_name
        else:
            raise ValueError("model must be a string or model2vec.StaticModel instance")
        self._dimension = self.model.dim

    @property
    def dimension(self) -> int:
        """Dimension of the embedding vectors."""
        return self._dimension

    def embed(self, text: str) -> "np.ndarray":
        """Embed a single text using the model2vec model."""
        return self.model.encode(text, convert_to_numpy=True)

    def embed_batch(self, texts: List[str]) -> List["np.ndarray"]:
        """Embed multiple texts using the model2vec model."""
        return self.model.encode(texts, convert_to_numpy=True)

    def count_tokens(self, text: str) -> int:
        """Count tokens in text using the model's tokenizer."""
        return len(self.model.tokenizer.encode(text))

    def count_tokens_batch(self, texts: List[str]) -> List[int]:
        """Count tokens in multiple texts using the model's tokenizer."""
        encodings = self.model.tokenizer.encode_batch(texts)
        return [len(enc) for enc in encodings]

    def similarity(self, u: "np.ndarray", v: "np.ndarray") -> "np.float32":
        """Compute cosine similarity of two embeddings."""
        return np.divide(
            np.dot(u, v), np.linalg.norm(u) * np.linalg.norm(v), dtype=np.float32
        )

    def get_tokenizer_or_token_counter(self):
        """Get the tokenizer or token counter for the model."""
        return self.model.tokenizer

    @classmethod
    def is_available(cls) -> bool:
        """Check if model2vec is available."""
        return importutil.find_spec("model2vec") is not None
    
    @classmethod
    def _import_dependencies(cls) -> None:
        """Lazy import dependencies for the embeddings implementation.

        This method should be implemented by all embeddings implementations that require
        additional dependencies. It lazily imports the dependencies only when they are needed.
        """
        if cls.is_available():
            global np, StaticModel
            import numpy as np
            from model2vec import StaticModel
        else:
            raise ImportError(
                "model2vec is not available. Please install it via `pip install chonkie[model2vec]`"
            )
        
    def __repr__(self) -> str:
        """Representation of the Model2VecEmbeddings instance."""
        return f"Model2VecEmbeddings(model_name_or_path={self.model_name_or_path})"
```

## File: `src/chonkie/embeddings/openai.py`
```python
"""OpenAI embeddings."""

import importlib.util as importutil
import os
import warnings
from typing import TYPE_CHECKING, List, Optional

from .base import BaseEmbeddings

if TYPE_CHECKING:
    import numpy as np

class OpenAIEmbeddings(BaseEmbeddings):

    """OpenAI embeddings implementation using their API."""

    AVAILABLE_MODELS = {
        "text-embedding-3-small": 1536,  # Latest model, best performance/cost ratio
        "text-embedding-3-large": 3072,  # Latest model, highest performance
        "text-embedding-ada-002": 1536,  # Legacy model
    }

    DEFAULT_MODEL = "text-embedding-3-small"

    def __init__(
        self,
        model: str = DEFAULT_MODEL,
        api_key: Optional[str] = None,
        organization: Optional[str] = None,
        max_retries: int = 3,
        timeout: float = 60.0,
        batch_size: int = 128,
        show_warnings: bool = True,
    ):
        """Initialize OpenAI embeddings.

        Args:
            model: Name of the OpenAI embedding model to use
            api_key: OpenAI API key (if not provided, looks for OPENAI_API_KEY env var)
            organization: Optional organization ID for API requests
            max_retries: Maximum number of retries for failed requests
            timeout: Timeout in seconds for API requests
            batch_size: Maximum number of texts to embed in one API call
            show_warnings: Whether to show warnings about token usage

        """
        super().__init__()

        # Lazy import dependencies if they are not already imported
        self._import_dependencies()

        if model not in self.AVAILABLE_MODELS:
            raise ValueError(
                f"Model {model} not available. Choose from: {list(self.AVAILABLE_MODELS.keys())}"
            )

        self.model = model
        self._dimension = self.AVAILABLE_MODELS[model]
        self._tokenizer = tiktoken.encoding_for_model(model)
        self._batch_size = batch_size
        self._show_warnings = show_warnings

        # Setup OpenAI client
        self.client = OpenAI(
            api_key=api_key or os.getenv("OPENAI_API_KEY"),
            organization=organization,
            timeout=timeout,
            max_retries=max_retries,
        )

        if self.client.api_key is None:
            raise ValueError(
                "OpenAI API key not found. Either pass it as api_key or set OPENAI_API_KEY environment variable."
            )

    def embed(self, text: str) -> "np.ndarray":
        """Get embeddings for a single text."""
        token_count = self.count_tokens(text)
        if token_count > 8191 and self._show_warnings:  # OpenAI's token limit
            warnings.warn(
                f"Text has {token_count} tokens which exceeds the model's limit of 8191. "
                "It will be truncated."
            )

        response = self.client.embeddings.create(
            model=self.model,
            input=text,
        )

        return np.array(response.data[0].embedding, dtype=np.float32)

    def embed_batch(self, texts: List[str]) -> List["np.ndarray"]:
        """Get embeddings for multiple texts using batched API calls."""
        if not texts:
            return []

        all_embeddings = []

        # Process in batches
        for i in range(0, len(texts), self._batch_size):
            batch = texts[i : i + self._batch_size]

            # Check token counts and warn if necessary
            token_counts = self.count_tokens_batch(batch)
            if self._show_warnings:
                for text, count in zip(batch, token_counts):
                    if count > 8191:
                        warnings.warn(
                            f"Text has {count} tokens which exceeds the model's limit of 8191. "
                            "It will be truncated."
                        )

            try:
                response = self.client.embeddings.create(
                    model=self.model,
                    input=batch,
                )
                # Sort embeddings by index as OpenAI might return them in different order
                sorted_embeddings = sorted(response.data, key=lambda x: x.index)
                embeddings = [
                    np.array(e.embedding, dtype=np.float32) for e in sorted_embeddings
                ]
                all_embeddings.extend(embeddings)

            except Exception as e:
                # If the batch fails, try one by one
                if len(batch) > 1:
                    warnings.warn(
                        f"Batch embedding failed: {str(e)}. Trying one by one."
                    )
                    individual_embeddings = [self.embed(text) for text in batch]
                    all_embeddings.extend(individual_embeddings)
                else:
                    raise e

        return all_embeddings

    def count_tokens(self, text: str) -> int:
        """Count tokens in text using the model's tokenizer."""
        return len(self._tokenizer.encode(text))

    def count_tokens_batch(self, texts: List[str]) -> List[int]:
        """Count tokens in multiple texts."""
        tokens = self._tokenizer.encode_batch(texts)
        return [len(t) for t in tokens]

    def similarity(self, u: "np.ndarray", v: "np.ndarray") -> "np.float32":
        """Compute cosine similarity between two embeddings."""
        return np.divide(
            np.dot(u, v), np.linalg.norm(u) * np.linalg.norm(v), dtype=float
        )

    @property
    def dimension(self) -> int:
        """Return the embedding dimension."""
        return self._dimension

    def get_tokenizer_or_token_counter(self):
        """Return a tiktoken tokenizer object."""
        return self._tokenizer

    @classmethod
    def is_available(cls) -> bool:
        """Check if the OpenAI package is available."""
        # We should check for OpenAI package alongside Numpy and tiktoken
        return (
            importutil.find_spec("openai") is not None
            and importutil.find_spec("numpy") is not None
            and importutil.find_spec("tiktoken") is not None
        )

    @classmethod
    def _import_dependencies(cls) -> None:
        """Lazy import dependencies for the embeddings implementation.

        This method should be implemented by all embeddings implementations that require
        additional dependencies. It lazily imports the dependencies only when they are needed.
        """
        if cls.is_available():
            global np, tiktoken, OpenAI
            import numpy as np
            import tiktoken
            from openai import OpenAI
        else:
            raise ImportError(
                "One (or more) of the following packages is not available: openai, numpy, tiktoken. Please install it via `pip install \"chonkie[openai]\"`"
            )
        
    def __repr__(self) -> str:
        """Representation of the OpenAIEmbeddings instance."""
        return f"OpenAIEmbeddings(model={self.model})"
```

## File: `src/chonkie/embeddings/registry.py`
```python
"""Registry for embedding implementations with pattern matching support."""

import re
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Pattern, Type, Union

from .base import BaseEmbeddings
from .cohere import CohereEmbeddings
from .model2vec import Model2VecEmbeddings
from .openai import OpenAIEmbeddings
from .sentence_transformer import SentenceTransformerEmbeddings


@dataclass
class RegistryEntry:

    """Registry entry containing the embeddings class and optional pattern."""

    embeddings_cls: Type[BaseEmbeddings]
    pattern: Optional[Pattern] = None
    supported_types: Optional[List[str]] = None


class EmbeddingsRegistry:

    """Registry for embedding implementations with pattern matching support."""

    _registry: Dict[str, RegistryEntry] = {}

    @classmethod
    def register(
        cls,
        name: str,
        embedding_cls: Type[BaseEmbeddings],
        pattern: Optional[Union[str, Pattern]] = None,
        supported_types: Optional[List[str]] = None,
    ):
        """Register a new embeddings implementation.

        Args:
            name: Unique identifier for this implementation
            embedding_cls: The embeddings class to register
            pattern: Optional regex pattern string or compiled pattern
            supported_types: Optional list of types that the embeddings class supports

        """
        if not issubclass(embedding_cls, BaseEmbeddings):
            raise ValueError(f"{embedding_cls} must be a subclass of BaseEmbeddings")

        # Compile pattern if provided as string
        if isinstance(pattern, str):
            pattern = re.compile(pattern)

        cls._registry[name] = RegistryEntry(
            embeddings_cls=embedding_cls,
            pattern=pattern,
            supported_types=supported_types,
        )

    @classmethod
    def get(cls, name: str) -> Optional[Type[BaseEmbeddings]]:
        """Get embeddings class by exact name match."""
        entry = cls._registry.get(name)
        return entry.embeddings_cls if entry else None

    @classmethod
    def match(cls, identifier: str) -> Optional[Type[BaseEmbeddings]]:
        """Find matching embeddings class using both exact matches and patterns.

        Args:
            identifier: String to match against registry entries

        Returns:
            Matching embeddings class or None if no match found

        Examples:
            # Match exact name
            cls.match("sentence-transformers") -> SentenceTransformerEmbeddings

            # Match OpenAI pattern
            cls.match("openai://my-embedding") -> OpenAIEmbeddings

            # Match model name pattern
            cls.match("text-embedding-ada-002") -> OpenAIEmbeddings

        """
        # First try exact match
        if identifier in cls._registry:
            return cls._registry[identifier].embeddings_cls

        # Then try patterns
        for entry in cls._registry.values():
            if entry.pattern and entry.pattern.match(identifier):
                return entry.embeddings_cls

        # if no match is found, raise ValueError
        raise ValueError(
            f"No matching embeddings implementation found for {identifier}"
        )

    @classmethod
    def wrap(cls, object: Any, **kwargs) -> BaseEmbeddings:
        """Wrap an object in the appropriate embeddings class.

        The objects that are handled here could be either a Model or Client object.

        Args:
            object: Name of the embeddings implementation
            **kwargs: Additional arguments passed to the embeddings constructor

        Returns:
            Initialized embeddings instance

        """
        # Check the object type and wrap it in the appropriate embeddings class
        if isinstance(object, BaseEmbeddings):
            return object
        elif isinstance(object, str):
            embeddings_cls = cls.match(object)
            return embeddings_cls(object, **kwargs)
        else:
            # Loop through all the registered embeddings and check if the object is an instance of any of them
            for entry in cls._registry.values():
                if entry.supported_types and any(
                    t in str(type(object)) for t in entry.supported_types
                ):
                    return entry.embeddings_cls(object, **kwargs)

            raise ValueError(f"Unsupported object type for embeddings: {object}")

    @classmethod
    def list_available(cls) -> List[str]:
        """List names of available embeddings implementations."""
        return [
            name
            for name, entry in cls._registry.items()
            if entry.embeddings_cls.is_available()
        ]


# Register all the available embeddings in the EmbeddingsRegistry!
# This is essential for the `AutoEmbeddings` to work properly.

# Register SentenceTransformer embeddings with pattern
EmbeddingsRegistry.register(
    "sentence-transformer",
    SentenceTransformerEmbeddings,
    pattern=r"^sentence-transformers/|^all-minilm-|^paraphrase-|^multi-qa-|^msmarco-",
    supported_types=["SentenceTransformer"],
)

# Register OpenAI embeddings with pattern
EmbeddingsRegistry.register(
    "openai", OpenAIEmbeddings, pattern=r"^openai|^text-embedding-"
)
EmbeddingsRegistry.register("text-embedding-ada-002", OpenAIEmbeddings)
EmbeddingsRegistry.register("text-embedding-3-small", OpenAIEmbeddings)
EmbeddingsRegistry.register("text-embedding-3-large", OpenAIEmbeddings)

# Register model2vec embeddings
EmbeddingsRegistry.register(
    "model2vec",
    Model2VecEmbeddings,
    pattern=r"^minishlab/|^minishlab/potion-base-|^minishlab/potion-|^potion-",
    supported_types=["Model2Vec", "model2vec"],
)

# Register Cohere embeddings with pattern
EmbeddingsRegistry.register("cohere", CohereEmbeddings, pattern=r"^cohere|^embed-")
EmbeddingsRegistry.register("embed-english-v3.0", CohereEmbeddings)
EmbeddingsRegistry.register("embed-multilingual-v3.0", CohereEmbeddings)
EmbeddingsRegistry.register("embed-english-light-v3.0", CohereEmbeddings)
EmbeddingsRegistry.register("embed-multilingual-light-v3.0", CohereEmbeddings)
EmbeddingsRegistry.register("embed-english-v2.0", CohereEmbeddings)
EmbeddingsRegistry.register("embed-english-light-v2.0", CohereEmbeddings)
EmbeddingsRegistry.register("embed-multilingual-v2.0", CohereEmbeddings)
```

## File: `src/chonkie/embeddings/sentence_transformer.py`
```python
"""SentenceTransformer embeddings."""

import importlib.util as importutil
from typing import TYPE_CHECKING, List, Union

from chonkie.embeddings.base import BaseEmbeddings

if TYPE_CHECKING:
    import numpy as np
    from sentence_transformers import SentenceTransformer
    from tokenizers import Tokenizer
    
class SentenceTransformerEmbeddings(BaseEmbeddings):

    """Class for SentenceTransformer embeddings.

    This class provides an interface for the SentenceTransformer library, which
    provides a variety of pre-trained models for sentence embeddings. This is also
    the recommended way to use sentence-transformers in Chonkie.

    Args:
        model (str): Name of the SentenceTransformer model to load

    """

    def __init__(
        self, model: Union[str, "SentenceTransformer"] = "all-MiniLM-L6-v2", **kwargs
    ) -> None:
        """Initialize SentenceTransformerEmbeddings with a sentence-transformers model.

        Args:
            model (str): Name of the SentenceTransformer model to load
            **kwargs: Additional keyword arguments to pass to the SentenceTransformer constructor

        Raises:
            ImportError: If sentence-transformers is not available
            ValueError: If the model is not a string or SentenceTransformer instance

        """
        super().__init__()

        # Lazy import dependencies if they are not already imported
        self._import_dependencies()

        if isinstance(model, str):
            self.model_name_or_path = model
            self.model = SentenceTransformer(self.model_name_or_path, **kwargs)
        elif isinstance(model, SentenceTransformer):
            self.model = model
            self.model_name_or_path = self.model.model_card_data.base_model
        else:
            raise ValueError("model must be a string or SentenceTransformer instance")

        self._dimension = self.model.get_sentence_embedding_dimension()

    def embed(self, text: str) -> "np.ndarray":
        """Embed a single text using the sentence-transformers model."""
        return self.model.encode(text, convert_to_numpy=True)

    def embed_batch(self, texts: List[str]) -> List["np.ndarray"]:
        """Embed multiple texts using the sentence-transformers model."""
        return self.model.encode(texts, convert_to_numpy=True) # type: ignore

    def embed_as_tokens(self, text: str) -> "np.ndarray":
        """Embed the text as tokens using the sentence-transformers model.

        This method is useful for getting the token embeddings of a text. It
        would work even if the text is longer than the maximum sequence length.
        """
        if text == "":
            return np.array([])

        # Use the model's tokenizer to encode the text
        encodings = self.model.tokenizer(text, add_special_tokens=False)["input_ids"]

        max_seq_length = self.max_seq_length
        token_splits = []
        for i in range(0, len(encodings), max_seq_length):
            if i + max_seq_length <= len(encodings):
                token_splits.append(encodings[i : i + max_seq_length])
            else:
                token_splits.append(encodings[i:])

        split_texts = self.model.tokenizer.batch_decode(token_splits)
        # Get the token embeddings
        token_embeddings = self.model.encode(
            split_texts, output_value="token_embeddings", add_special_tokens=False
        )

        # Since SentenceTransformer doesn't automatically convert embeddings into
        # numpy arrays, we need to do it manually
        if (
            type(token_embeddings) is not list
            and type(token_embeddings) is not np.ndarray
        ):
            token_embeddings = token_embeddings.cpu().numpy()
        elif type(token_embeddings) is list and type(token_embeddings[0]) not in [
            np.ndarray,
            list,
        ]:
            token_embeddings = [
                embedding.cpu().numpy() for embedding in token_embeddings
            ]

        # Concatenate the token embeddings
        token_embeddings = np.concatenate(token_embeddings, axis=0)

        # Assertion always fails because of special tokens added by encode process
        # assert token_embeddings.shape[0] == len(encodings), \
        #     (f"The number of token embeddings should be equal to the number of tokens in the text"
        #      f"Expected: {len(encodings)}, Got: {token_embeddings.shape[0]}")

        return token_embeddings # type: ignore

    def embed_as_tokens_batch(self, texts: List[str]) -> List["np.ndarray"]:
        """Embed multiple texts as tokens using the sentence-transformers model."""
        return [self.embed_as_tokens(text) for text in texts]

    def count_tokens(self, text: str) -> int:
        """Count tokens in text using the model's tokenizer."""
        return len(self.model.tokenizer.encode(text))

    def count_tokens_batch(self, texts: List[str]) -> List[int]:
        """Count tokens in multiple texts using the model's tokenizer."""
        encodings = self.model.tokenizer(texts)
        return [len(enc) for enc in encodings["input_ids"]]

    def similarity(self, u: "np.ndarray", v: "np.ndarray") -> float:
        """Compute cosine similarity between two embeddings."""
        return self.model.similarity(u, v).item()

    def get_tokenizer_or_token_counter(self) -> "Tokenizer":
        """Return the tokenizer or token counter object."""
        return self.model.tokenizer

    @property
    def dimension(self) -> int:
        """Return the embedding dimension."""
        return self._dimension # type: ignore

    @property
    def max_seq_length(self) -> int:
        """Return the maximum sequence length."""
        return self.model.get_max_seq_length() # type: ignore

    @classmethod
    def is_available(cls) -> bool:
        """Check if sentence-transformers is available."""
        return (
            importutil.find_spec("sentence_transformers") is not None
            and importutil.find_spec("numpy") is not None
        )
    
    @classmethod
    def _import_dependencies(cls) -> None:
        """Lazy import dependencies for the embeddings implementation.

        This method should be implemented by all embeddings implementations that require
        additional dependencies. It lazily imports the dependencies only when they are needed.
        """
        if cls.is_available():
            global np, SentenceTransformer
            import numpy as np
            from sentence_transformers import SentenceTransformer
        else:
            raise ImportError(
                "sentence_transformers is not available. Please install it via `pip install chonkie[st]`"
            )

    def __repr__(self) -> str:
        """Representation of the SentenceTransformerEmbeddings instance."""
        return f"SentenceTransformerEmbeddings(model={self.model_name_or_path})"
```

## File: `src/chonkie/types/__init__.py`
```python
"""Module for chunkers."""

from .base import Chunk, Context
from .late import LateChunk
from .recursive import RecursiveChunk, RecursiveLevel, RecursiveRules
from .semantic import SemanticChunk, SemanticSentence
from .sentence import Sentence, SentenceChunk

__all__ = [
    "Chunk",
    "Context",
    "RecursiveChunk",
    "RecursiveLevel",
    "RecursiveRules",
    "Sentence",
    "SentenceChunk",
    "SemanticChunk",
    "SemanticSentence",
    "LateChunk",
]
```

## File: `src/chonkie/types/base.py`
```python
"""Custom base types for Chonkie."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class Context:
    """Context class to hold chunk metadata.

    Attributes:
        text (str): The text of the chunk.
        start_index (Optional[int]): The starting index of the chunk in the original text.
        end_index (Optional[int]): The ending index of the chunk in the original text.
        token_count (int): The number of tokens in the chunk.

    """

    text: str
    token_count: int
    start_index: Optional[int] = None
    end_index: Optional[int] = None

    def __post_init__(self):
        """Validate context attributes."""
        if not isinstance(self.text, str):
            raise ValueError("Text must be a string.")
        if self.token_count is not None and self.token_count < 0:
            raise ValueError("Token count must be a non-negative integer.")
        if self.start_index is not None and self.start_index < 0:
            raise ValueError("Start index must be a non-negative integer.")
        if self.end_index is not None and self.end_index < 0:
            raise ValueError("End index must be a non-negative integer.")
        if (
            self.start_index is not None
            and self.end_index is not None
            and (self.start_index > self.end_index)
        ):
            raise ValueError("Start index must be less than end index.")

    def __len__(self):
        """Return the length of the text."""
        return len(self.text)

    def __str__(self) -> str:
        """Return a string representation of the Context."""
        return self.text

    def __repr__(self) -> str:
        """Return a detailed string representation of the Context."""
        return (
            f"Context(text='{self.text}', token_count={self.token_count}, "
            f"start_index={self.start_index}, end_index={self.end_index})"
        )

    def to_dict(self) -> dict:
        """Return the Context as a dictionary."""
        return self.__dict__.copy()

    @classmethod
    def from_dict(cls, data: dict) -> "Context":
        """Create a Context object from a dictionary."""
        return cls(**data)


@dataclass
class Chunk:
    """Chunks with metadata.

    Attributes:
        text (str): The text of the chunk.
        start_index (int): The starting index of the chunk in the original text.
        end_index (int): The ending index of the chunk in the original text.
        token_count (int): The number of tokens in the chunk.
        context (Optional[Context]): Optional context metadata for the chunk.

    """

    text: str
    start_index: int
    end_index: int
    token_count: int
    context: Optional[Context] = None

    def __len__(self):
        """Return the length of the text."""
        return len(self.text)

    def __str__(self) -> str:
        """Return a string representation of the Chunk."""
        return self.text

    def __repr__(self) -> str:
        """Return a detailed string representation of the Chunk."""
        repr = (
            f"Chunk(text='{self.text}', token_count={self.token_count}, "
            f"start_index={self.start_index}, end_index={self.end_index}"
        )
        if self.context:
            return repr + f", context={self.context})"
        else:
            return repr + ")"

    def __iter__(self):
        """Return an iterator over the chunk's text."""
        return iter(self.text)

    def __getitem__(self, index):
        """Return a slice of the chunk's text."""
        return self.text[index]

    def to_dict(self) -> dict:
        """Return the Chunk as a dictionary."""
        result = self.__dict__.copy()
        result["context"] = self.context.to_dict() if self.context else None
        return result

    @classmethod
    def from_dict(cls, data: dict):
        """Create a Chunk object from a dictionary."""
        context_repr = data.pop("context")
        return cls(
            **data,
            context=Context.from_dict(context_repr) if context_repr else None,
        )

    def copy(self) -> "Chunk":
        """Return a deep copy of the chunk."""
        return Chunk.from_dict(self.to_dict())
```

## File: `src/chonkie/types/late.py`
```python
"""Module containing the associated types for the LateChunker."""

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Dict, Optional

from .base import Chunk

if TYPE_CHECKING:
    import numpy as np


@dataclass
class LateChunk(Chunk):
    """Class to represent the late chunk.

    Attributes:
        text (str): The text of the chunk.
        start_index (int): The start index of the chunk.
        end_index (int): The end index of the chunk.
        token_count (int): The number of tokens in the chunk.
        start_token (int): The start token of the chunk.
        end_token (int): The end token of the chunk.
        sentences (list[LateSentence]): The sentences in the chunk.
        embedding (Optional[np.ndarray]): The embedding of the chunk.

    """

    embedding: Optional["np.ndarray"] = field(default=None)

    def to_dict(self) -> dict:
        """Return the LateChunk as a dictionary."""
        return self.__dict__

    @classmethod
    def from_dict(cls, data: Dict) -> "LateChunk":
        """Create a LateChunk from a dictionary."""
        return cls(**data)

    def __repr__(self) -> str:
        """Return a string representation of the LateChunk."""
        return (
            f"LateChunk(text={self.text}, "
            f"start_index={self.start_index}, "
            f"end_index={self.end_index}, "
            f"token_count={self.token_count}, "
            f"embedding={self.embedding})"
        )
```

## File: `src/chonkie/types/recursive.py`
```python
"""Custom types for recursive chunking."""

from dataclasses import dataclass
from typing import Iterator, List, Literal, Optional, Union

from chonkie.types.base import Chunk


@dataclass
class RecursiveLevel:
    """RecursiveLevels express the chunking rules at a specific level for the recursive chunker.

    Attributes:
        whitespace (bool): Whether to use whitespace as a delimiter.
        delimiters (Optional[Union[str, List[str]]]): Custom delimiters for chunking.
        include_delim (Optional[Literal["prev", "next"]]): Whether to include the delimiter at all, or in the previous chunk, or the next chunk.

    """

    delimiters: Optional[Union[str, List[str]]] = None
    whitespace: bool = False
    include_delim: Optional[Literal["prev", "next"]] = "prev"

    def _validate_fields(self) -> None:
        """Validate all fields have legal values."""
        if self.delimiters is not None and self.whitespace:
            raise NotImplementedError(
                "Cannot use whitespace as a delimiter and also specify custom delimiters."
            )
        if self.delimiters is not None:
            if isinstance(self.delimiters, str) and len(self.delimiters) == 0:
                raise ValueError("Custom delimiters cannot be an empty string.")
            if isinstance(self.delimiters, list):
                if any(
                    not isinstance(delim, str) or len(delim) == 0
                    for delim in self.delimiters
                ):
                    raise ValueError("Custom delimiters cannot be an empty string.")
                if any(delim == " " for delim in self.delimiters):
                    raise ValueError(
                        "Custom delimiters cannot be whitespace only. Set whitespace to True instead."
                    )

    def __post_init__(self) -> None:
        """Validate attributes."""
        self._validate_fields()

    def __repr__(self) -> str:
        """Return a string representation of the RecursiveLevel."""
        return (
            f"RecursiveLevel(delimiters={self.delimiters}, "
            f"whitespace={self.whitespace}, include_delim={self.include_delim})"
        )

    def to_dict(self) -> dict:
        """Return the RecursiveLevel as a dictionary."""
        return self.__dict__.copy()

    @classmethod
    def from_dict(cls, data: dict) -> "RecursiveLevel":
        """Create RecursiveLevel object from a dictionary."""
        return cls(**data)


@dataclass
class RecursiveRules:
    """Expression rules for recursive chunking."""

    levels: Optional[Union[RecursiveLevel, List[RecursiveLevel]]] = None

    def __post_init__(self):
        """Validate attributes."""
        if self.levels is None:
            paragraphs = RecursiveLevel(delimiters=["\n\n", "\r\n", "\n", "\r"])
            sentences = RecursiveLevel(
                delimiters=".!?",
            )
            pauses = RecursiveLevel(
                delimiters=[
                    "{",
                    "}",
                    '"',
                    "[",
                    "]",
                    "<",
                    ">",
                    "(",
                    ")",
                    ":",
                    ";",
                    ",",
                    "—",
                    "|",
                    "~",
                    "-",
                    "...",
                    "`",
                    "'",
                ],
            )
            word = RecursiveLevel(whitespace=True)
            token = RecursiveLevel()
            self.levels = [paragraphs, sentences, pauses, word, token]
        elif isinstance(self.levels, RecursiveLevel):
            self.levels._validate_fields()
        elif isinstance(self.levels, list):
            for level in self.levels:
                level._validate_fields()
        else:
            raise ValueError(
                "Levels must be a RecursiveLevel object or a list of RecursiveLevel objects."
            )

    def __repr__(self) -> str:
        """Return a string representation of the RecursiveRules."""
        return f"RecursiveRules(levels={self.levels})"

    def __len__(self) -> int:
        """Return the number of levels."""
        return len(self.levels)

    def __getitem__(self, index: int) -> RecursiveLevel:
        """Return the RecursiveLevel at the specified index."""
        if isinstance(self.levels, list):
            return self.levels[index]
        raise TypeError(
            "Levels must be a list of RecursiveLevel objects to use indexing."
        )

    def __iter__(self) -> Iterator[RecursiveLevel]:
        """Return an iterator over the RecursiveLevels."""
        if isinstance(self.levels, list):
            return iter(self.levels)
        raise TypeError(
            "Levels must be a list of RecursiveLevel objects to use iteration."
        )

    @classmethod
    def from_dict(cls, data: dict) -> "RecursiveRules":
        """Create a RecursiveRules object from a dictionary."""
        dict_levels = data.pop("levels")
        object_levels = None
        if dict_levels is not None:
            if isinstance(dict_levels, dict):
                object_levels = RecursiveLevel.from_dict(dict_levels)
            elif isinstance(dict_levels, list):
                object_levels = [
                    RecursiveLevel.from_dict(d_level) for d_level in dict_levels
                ]
        return cls(levels=object_levels)

    def to_dict(self) -> dict:
        """Return the RecursiveRules as a dictionary."""
        result = dict()
        result["levels"] = None
        if isinstance(self.levels, RecursiveLevel):
            result["levels"] = self.levels.to_dict()
        elif isinstance(self.levels, list):
            result["levels"] = [level.to_dict() for level in self.levels]
        else:
            raise ValueError(
                "Levels must be a RecursiveLevel object or a list of RecursiveLevel objects."
            )
        return result


@dataclass
class RecursiveChunk(Chunk):
    """Class to represent recursive chunks.

    Attributes:
        level (Optional[int]): The level of recursion for the chunk, if any.

    """

    level: Optional[int] = None

    def str_repr(self) -> str:
        """Return a string representation of the RecursiveChunk."""
        return (
            f"RecursiveChunk(text={self.text}, start_index={self.start_index}, "
            f"end_index={self.end_index}, token_count={self.token_count}, "
            f"level={self.level})"
        )

    def __repr__(self) -> str:
        """Return a string representation of the RecursiveChunk."""
        return self.str_repr()

    def __str__(self):
        """Return a string representation of the RecursiveChunk."""
        return self.str_repr()

    def to_dict(self) -> dict:
        """Return the RecursiveChunk as a dictionary."""
        return self.__dict__.copy()

    @classmethod
    def from_dict(cls, data: dict) -> "RecursiveChunk":
        """Create a RecursiveChunk object from a dictionary."""
        return cls(**data)
```

## File: `src/chonkie/types/semantic.py`
```python
"""Semantic types for Chonkie."""

from dataclasses import dataclass, field
from typing import TYPE_CHECKING, List, Optional

from chonkie.types.sentence import Sentence, SentenceChunk

if TYPE_CHECKING:
    import numpy as np


@dataclass
class SemanticSentence(Sentence):
    """Dataclass representing a semantic sentence with metadata.

    This class is used to represent a sentence with an embedding.

    Attributes:
        text: The text content of the sentence
        start_index: The starting index of the sentence in the original text
        end_index: The ending index of the sentence in the original text
        token_count: The number of tokens in the sentence
        embedding: The sentence embedding

    """

    embedding: Optional["np.ndarray"] = field(default=None)

    def to_dict(self) -> dict:
        """Return the SemanticSentence as a dictionary."""
        result = super().to_dict()
        result["embedding"] = (
            self.embedding.tolist() if self.embedding is not None else None
        )
        return result

    @classmethod
    def from_dict(cls, data: dict) -> "SemanticSentence":
        """Create a SemanticSentence object from a dictionary."""
        embedding_list = data.pop("embedding")
        # NOTE: We can't use np.array() here because we don't import numpy in this file,
        # and we don't want add 50MiB to the package size.
        embedding = embedding_list if embedding_list is not None else None
        return cls(**data, embedding=embedding)

    def __repr__(self) -> str:
        """Return a string representation of the SemanticSentence."""
        return (
            f"SemanticSentence(text={self.text}, start_index={self.start_index}, "
            f"end_index={self.end_index}, token_count={self.token_count}, "
            f"embedding={self.embedding})"
        )


@dataclass
class SemanticChunk(SentenceChunk):
    """SemanticChunk dataclass representing a semantic chunk with metadata.

    Attributes:
        text: The text content of the chunk
        start_index: The starting index of the chunk in the original text
        end_index: The ending index of the chunk in the original text
        token_count: The number of tokens in the chunk
        sentences: List of SemanticSentence objects in the chunk

    """

    sentences: List[SemanticSentence] = field(default_factory=list)

    def to_dict(self) -> dict:
        """Return the SemanticChunk as a dictionary."""
        result = super().to_dict()
        result["sentences"] = [sentence.to_dict() for sentence in self.sentences]
        return result

    @classmethod
    def from_dict(cls, data: dict):
        """Create a SemanticChunk object from a dictionary."""
        sentences_dict = data.pop("sentences")
        sentences = [
            SemanticSentence.from_dict(sentence) for sentence in sentences_dict
        ]
        return cls(**data, sentences=sentences)

    def __repr__(self) -> str:
        """Return a string representation of the SemanticChunk."""
        return (
            f"SemanticChunk(text={self.text}, start_index={self.start_index}, "
            f"end_index={self.end_index}, token_count={self.token_count}, "
            f"sentences={self.sentences})"
        )
```

## File: `src/chonkie/types/sentence.py`
```python
"""Custom types for Sentence Chunking."""

from dataclasses import dataclass, field
from typing import Dict, List, Union

from chonkie.types.base import Chunk


@dataclass
class Sentence:
    """Class to represent a sentence.

    Attributes:
        text (str): The text of the sentence.
        start_index (int): The starting index of the sentence in the original text.
        end_index (int): The ending index of the sentence in the original text.
        token_count (int): The number of tokens in the sentence.

    """

    text: str
    start_index: int
    end_index: int
    token_count: int

    def __post_init__(self):
        """Validate attributes."""
        if not isinstance(self.text, str):
            raise ValueError("Text must be a string.")
        if not isinstance(self.start_index, int) or self.start_index < 0:
            raise ValueError("Start index must be a non-negative integer.")
        if not isinstance(self.end_index, int) or self.end_index < 0:
            raise ValueError("End index must be a non-negative integer.")
        if self.start_index > self.end_index:
            raise ValueError("Start index must be less than end index.")
        if (
            not (
                isinstance(self.token_count, int) or isinstance(self.token_count, float)
            )
            or self.token_count < 0
        ):
            raise ValueError("Token count must be a non-negative integer.")

    def __repr__(self) -> str:
        """Return a string representation of the Sentence."""
        return (
            f"Sentence(text={self.text}, start_index={self.start_index}, "
            f"end_index={self.end_index}, token_count={self.token_count})"
        )

    def to_dict(self) -> Dict[str, Union[str, int]]:
        """Return the Chunk as a dictionary."""
        return self.__dict__.copy()

    @classmethod
    def from_dict(cls, data: Dict[str, Union[str, int]]) -> "Sentence":
        """Create a Sentence object from a dictionary."""
        return cls(**data)


@dataclass
class SentenceChunk(Chunk):
    """Class to represent sentence chunks.

    Attributes:
        text (str): The text of the chunk.
        start_index (int): The starting index of the chunk in the original text.
        end_index (int): The ending index of the chunk in the original text.
        token_count (int): The number of tokens in the chunk.
        sentences (list[Sentence]): List of sentences in the chunk.

    """

    sentences: List[Sentence] = field(default_factory=list)

    def __repr__(self) -> str:
        """Return a string representation of the SentenceChunk."""
        return (
            f"SentenceChunk(text={self.text}, start_index={self.start_index}, "
            f"end_index={self.end_index}, token_count={self.token_count}, "
            f"sentences={self.sentences})"
        )

    def to_dict(self) -> Dict:
        """Return the SentenceChunk as a dictionary."""
        result = super().to_dict()
        result["sentences"] = [sentence.to_dict() for sentence in self.sentences]
        return result

    @classmethod
    def from_dict(cls, data: dict) -> "SentenceChunk":
        """Create a SentenceChunk from dictionary."""
        sentences_dict = data.pop("sentences") if "sentences" in data else None
        sentences = (
            [Sentence.from_dict(sentence) for sentence in sentences_dict]
            if sentences_dict is not None
            else []
        )
        return cls(**data, sentences=sentences)
```

## File: `tests/test_tokenizer.py`
```python
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
    assert character_tokenizer.token2id[" "] == 0


def test_character_tokenizer_encode_decode(
    character_tokenizer: CharacterTokenizer, sample_text: str
) -> None:
    """Test encoding and decoding with CharacterTokenizer."""
    tokens = character_tokenizer.encode(sample_text)
    assert isinstance(tokens, list)
    assert all(isinstance(token, int) for token in tokens)
    assert len(tokens) == len(sample_text)

    decoded = character_tokenizer.decode(tokens)
    assert isinstance(decoded, str)
    assert decoded == sample_text


def test_character_tokenizer_count_tokens(
    character_tokenizer: CharacterTokenizer,
    sample_text: str,
    sample_text_list: list[str],
) -> None:
    """Test token counting with CharacterTokenizer."""
    count = character_tokenizer.count_tokens(sample_text)
    assert count == len(sample_text)


def test_character_tokenizer_batch_encode_decode(
    character_tokenizer: CharacterTokenizer, sample_text_list: list[str]
) -> None:
    """Test batch encoding and decoding with CharacterTokenizer."""
    batch_encoded = character_tokenizer.encode_batch(sample_text_list)
    assert isinstance(batch_encoded, list)
    assert all(isinstance(tokens, list) for tokens in batch_encoded)
    assert all(
        len(tokens) == len(text)
        for tokens, text in zip(batch_encoded, sample_text_list)
    )

    batch_decoded = character_tokenizer.decode_batch(batch_encoded)
    assert isinstance(batch_decoded, list)
    assert all(isinstance(text, str) for text in batch_decoded)
    assert batch_decoded == sample_text_list


def test_character_tokenizer_count_tokens_batch(
    character_tokenizer: CharacterTokenizer,
    sample_text_list: list[str],
) -> None:
    """Test batch token counting with CharacterTokenizer."""
    counts = character_tokenizer.count_tokens_batch(sample_text_list)
    assert counts == [len(text) for text in sample_text_list]


def test_character_tokenizer_repr() -> None:
    """Test string representation of tokenizers."""
    character_tokenizer = CharacterTokenizer()
    assert str(character_tokenizer) == "CharacterTokenizer(vocab_size=1)"


def test_character_tokenizer_vocab_and_mapping(
    character_tokenizer: CharacterTokenizer, sample_text: str
) -> None:
    """Test vocabulary evolution in CharacterTokenizer."""
    # Initial state
    assert character_tokenizer.get_vocab() == [" "]
    assert dict(character_tokenizer.get_token2id()) == {" ": 0}

    character_tokenizer.encode(sample_text)

    # Encoding text should add vocabulary
    # and update token2id mapping
    vocab = character_tokenizer.get_vocab()
    token2id = character_tokenizer.get_token2id()

    # Spot check vocabulary
    assert len(vocab) > 1

    assert isinstance(token2id, dict)
    assert all(isinstance(token, str) for token in token2id.keys())
    assert all(isinstance(idx, int) for idx in token2id.values())
    assert token2id[" "] == 0

    # Verify mapping consistency
    for token in vocab:
        assert token in token2id
        assert vocab[token2id[token]] == token

    for char in sample_text:
        assert char in vocab
        assert char in token2id


def test_character_tokenizer_multiple_encodings(
    character_tokenizer: CharacterTokenizer,
) -> None:
    """Test that vocabulary changes as expected over multiple encodings."""
    text1 = "Wall-E is truly a masterpiece that should be required viewing."
    text2 = (
        "Ratatouille is truly a delightful film that every kid should watch."
    )

    character_tokenizer.encode(text1)
    vocab_size1 = len(character_tokenizer.get_vocab())
    character_tokenizer.encode(text2)
    vocab_size2 = len(character_tokenizer.get_vocab())

    assert vocab_size2 > vocab_size1
    assert "u" in character_tokenizer.get_vocab()
    assert (
        character_tokenizer.get_token2id()["u"]
        == character_tokenizer.encode("u")[0]
    )
```

## File: `tests/chunkers/test_late_chunker.py`
```python
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

## File: `tests/chunkers/test_recursive_chunker.py`
```python
"""Tests for the RecursiveChunker class.

This module contains test cases for the RecursiveChunker class, which implements
a recursive chunking strategy based on configurable rules. The tests verify:

- Initialization with different rule configurations
- Basic chunking functionality with simple and complex texts
- Proper handling of recursive levels
- Token count accuracy
- Index mapping and text reconstruction
- Edge cases and error conditions
"""

import pytest

from chonkie import (
    Chunk,
    RecursiveChunker,
    RecursiveLevel,
    RecursiveRules,
)


@pytest.fixture
def sample_text():
    """Return a sample text."""
    text = """# Chunking Strategies in Retrieval-Augmented Generation: A Comprehensive Analysis\n\nIn the rapidly evolving landscape of natural language processing, Retrieval-Augmented Generation (RAG) has emerged as a groundbreaking approach that bridges the gap between large language models and external knowledge bases. At the heart of these systems lies a crucial yet often overlooked process: chunking. This fundamental operation, which involves the systematic decomposition of large text documents into smaller, semantically meaningful units, plays a pivotal role in determining the overall effectiveness of RAG implementations.\n\nThe process of text chunking in RAG applications represents a delicate balance between competing requirements. On one side, we have the need for semantic coherence – ensuring that each chunk maintains meaningful context that can be understood and processed independently. On the other, we must optimize for information density, ensuring that each chunk carries sufficient signal without excessive noise that might impede retrieval accuracy. This balancing act becomes particularly crucial when we consider the downstream implications for vector databases and embedding models that form the backbone of modern RAG systems.\n\nThe selection of appropriate chunk size emerges as a fundamental consideration that significantly impacts system performance. Through extensive experimentation and real-world implementations, researchers have identified that chunks typically perform optimally in the range of 256 to 1024 tokens. However, this range should not be treated as a rigid constraint but rather as a starting point for optimization based on specific use cases and requirements. The implications of chunk size selection ripple throughout the entire RAG pipeline, affecting everything from storage requirements to retrieval accuracy and computational overhead.\n\nFixed-size chunking represents the most straightforward approach to document segmentation, offering predictable memory usage and consistent processing time. However, this apparent simplicity comes with significant drawbacks. By arbitrarily dividing text based on token or character count, fixed-size chunking risks fragmenting semantic units and disrupting the natural flow of information. Consider, for instance, a technical document where a complex concept is explained across several paragraphs – fixed-size chunking might split this explanation at critical junctures, potentially compromising the system's ability to retrieve and present this information coherently.\n\nIn response to these limitations, semantic chunking has gained prominence as a more sophisticated alternative. This approach leverages natural language understanding to identify meaningful boundaries within the text, respecting the natural structure of the document. Semantic chunking can operate at various levels of granularity, from simple sentence-based segmentation to more complex paragraph-level or topic-based approaches. The key advantage lies in its ability to preserve the inherent semantic relationships within the text, leading to more meaningful and contextually relevant retrieval results.\n\nRecent advances in the field have given rise to hybrid approaches that attempt to combine the best aspects of both fixed-size and semantic chunking. These methods typically begin with semantic segmentation but impose size constraints to prevent extreme variations in chunk length. Furthermore, the introduction of sliding window techniques with overlap has proved particularly effective in maintaining context across chunk boundaries. This overlap, typically ranging from 10% to 20% of the chunk size, helps ensure that no critical information is lost at segment boundaries, albeit at the cost of increased storage requirements.\n\nThe implementation of chunking strategies must also consider various technical factors that can significantly impact system performance. Vector database capabilities, embedding model constraints, and runtime performance requirements all play crucial roles in determining the optimal chunking approach. Moreover, content-specific factors such as document structure, language characteristics, and domain-specific requirements must be carefully considered. For instance, technical documentation might benefit from larger chunks that preserve detailed explanations, while news articles might perform better with smaller, more focused segments.\n\nThe future of chunking in RAG systems points toward increasingly sophisticated approaches. Current research explores the potential of neural chunking models that can learn optimal segmentation strategies from large-scale datasets. These models show promise in adapting to different content types and query patterns, potentially leading to more efficient and effective retrieval systems. Additionally, the emergence of cross-lingual chunking strategies addresses the growing need for multilingual RAG applications, while real-time adaptive chunking systems attempt to optimize segment boundaries based on user interaction patterns and retrieval performance metrics.\n\nThe effectiveness of RAG systems heavily depends on the thoughtful implementation of appropriate chunking strategies. While the field continues to evolve, practitioners must carefully consider their specific use cases and requirements when designing chunking solutions. Factors such as document characteristics, retrieval patterns, and performance requirements should guide the selection and optimization of chunking strategies. As we look to the future, the continued development of more sophisticated chunking approaches promises to further enhance the capabilities of RAG systems, enabling more accurate and efficient information retrieval and generation.\n\nThrough careful consideration of these various aspects and continued experimentation with different approaches, organizations can develop chunking strategies that effectively balance the competing demands of semantic coherence, computational efficiency, and retrieval accuracy. As the field continues to evolve, we can expect to see new innovations that further refine our ability to segment and process textual information in ways that enhance the capabilities of RAG systems while maintaining their practical utility in real-world applications."""
    return text


@pytest.fixture
def default_rules():
    """Return a default set of rules."""
    return RecursiveRules()


@pytest.fixture
def paragraph_rules():
    """Return a paragraph set of rules."""
    paragraph_level = RecursiveLevel(
        delimiters=["\n\n", "\r\n", "\n", "\r", "\t"], whitespace=False
    )
    return RecursiveRules(levels=[paragraph_level])


@pytest.fixture
def sentence_rules():
    """Return a sentence set of rules."""
    sentence_level = RecursiveLevel(delimiters=[".", "?", "!"], whitespace=False)
    return RecursiveRules(levels=[sentence_level])


@pytest.fixture
def subsentence_rules():
    """Return a subsentence set of rules."""
    subsentence_level = RecursiveLevel(
        delimiters=[
            ",",
            ";",
            ":",
            "-",
            "/",
            "|",
            "(",
            ")",
            "[",
            "]",
            "{",
            "}",
            "<",
            ">",
        ],
        whitespace=False,
    )
    return RecursiveRules(levels=[subsentence_level])


@pytest.fixture
def word_rules():
    """Return a word set of rules."""
    word_level = RecursiveLevel(delimiters=None, whitespace=True)
    return RecursiveRules(levels=[word_level])


@pytest.fixture
def token_rules():
    """Return a token set of rules."""
    token_level = RecursiveLevel(delimiters=None, whitespace=False)
    return RecursiveRules(levels=[token_level])


def test_recursive_chunker_initialization(sample_text, default_rules):
    """Test that the RecursiveChunker can be initialized with a sample text."""
    chunker = RecursiveChunker(
        rules=default_rules, chunk_size=512, min_characters_per_chunk=12
    )
    assert chunker is not None
    assert chunker.rules == default_rules
    assert chunker.chunk_size == 512
    assert chunker.min_characters_per_chunk == 12


def test_recursive_chunker_chunking(sample_text, default_rules):
    """Test that the RecursiveChunker can chunk a sample text."""
    chunker = RecursiveChunker(
        rules=default_rules, chunk_size=512, min_characters_per_chunk=12
    )
    chunks = chunker.chunk(sample_text)
    assert len(chunks) > 0
    assert all(isinstance(chunk, Chunk) for chunk in chunks)
    assert all(chunk.text is not None for chunk in chunks)
    assert all(chunk.start_index is not None for chunk in chunks)
    assert all(chunk.end_index is not None for chunk in chunks)
    assert all(chunk.level is not None for chunk in chunks)


def test_recursive_chunker_token_count_default_rules(sample_text, default_rules):
    """Test that the RecursiveChunker can chunk a sample text with default rules."""
    chunker = RecursiveChunker(
        rules=default_rules, chunk_size=512, min_characters_per_chunk=12
    )
    chunks = chunker.chunk(sample_text)
    assert len(chunks) > 0
    assert all(isinstance(chunk, Chunk) for chunk in chunks)
    assert all(chunk.token_count <= 512 for chunk in chunks)
    assert all(len(chunk.text) >= 12 for chunk in chunks)


def test_recursive_chunker_reconstruction_default_rules(sample_text, default_rules):
    """Test that the RecursiveChunker can reconstruct a sample text with default rules."""
    chunker = RecursiveChunker(
        rules=default_rules, chunk_size=512, min_characters_per_chunk=12
    )
    chunks = chunker.chunk(sample_text)
    assert len(chunks) > 0
    assert sample_text == "".join(chunk.text for chunk in chunks)


def test_recursive_chunker_indices_default_rules(sample_text, default_rules):
    """Test that the RecursiveChunker can reconstruct a sample text with default rules."""
    chunker = RecursiveChunker(
        rules=default_rules, chunk_size=512, min_characters_per_chunk=12
    )
    chunks = chunker.chunk(sample_text)
    assert len(chunks) > 0
    assert all(chunk.start_index < chunk.end_index for chunk in chunks)
    assert all(chunk.start_index >= 0 for chunk in chunks)
    assert all(chunk.end_index <= len(sample_text) for chunk in chunks)
    assert all(
        chunk.text == sample_text[chunk.start_index : chunk.end_index]
        for chunk in chunks
    )


def test_recursive_chunker_token_count_paragraph_rules(sample_text, paragraph_rules):
    """Test that the RecursiveChunker can chunk a sample text with paragraph rules."""
    chunker = RecursiveChunker(
        rules=paragraph_rules, chunk_size=512, min_characters_per_chunk=12
    )
    chunks = chunker.chunk(sample_text)
    assert len(chunks) > 0
    assert all(isinstance(chunk, Chunk) for chunk in chunks)
    assert all(chunk.token_count <= 512 for chunk in chunks)
    assert all(len(chunk.text) >= 12 for chunk in chunks)


def test_recursive_chunker_reconstruction_paragraph_rules(sample_text, paragraph_rules):
    """Test that the RecursiveChunker can reconstruct a sample text with paragraph rules."""
    chunker = RecursiveChunker(
        rules=paragraph_rules, chunk_size=512, min_characters_per_chunk=12
    )
    chunks = chunker.chunk(sample_text)
    assert len(chunks) > 0
    assert sample_text == "".join(chunk.text for chunk in chunks)


def test_recursive_chunker_indices_paragraph_rules(sample_text, paragraph_rules):
    """Test that the RecursiveChunker can reconstruct a sample text with paragraph rules."""
    chunker = RecursiveChunker(
        rules=paragraph_rules, chunk_size=512, min_characters_per_chunk=12
    )
    chunks = chunker.chunk(sample_text)
    assert len(chunks) > 0
    assert all(chunk.start_index < chunk.end_index for chunk in chunks)
    assert all(chunk.start_index >= 0 for chunk in chunks)
    assert all(chunk.end_index <= len(sample_text) for chunk in chunks)
    assert all(
        chunk.text == sample_text[chunk.start_index : chunk.end_index]
        for chunk in chunks
    )


def test_recursive_chunker_token_count_sentence_rules(sample_text, sentence_rules):
    """Test that the RecursiveChunker can chunk a sample text with sentence rules."""
    chunker = RecursiveChunker(
        rules=sentence_rules, chunk_size=512, min_characters_per_chunk=12
    )
    chunks = chunker.chunk(sample_text)
    assert len(chunks) > 0
    assert all(isinstance(chunk, Chunk) for chunk in chunks)
    assert all(chunk.token_count <= 512 for chunk in chunks)
    assert all(len(chunk.text) >= 12 for chunk in chunks)


def test_recursive_chunker_reconstruction_sentence_rules(sample_text, sentence_rules):
    """Test that the RecursiveChunker can reconstruct a sample text with sentence rules."""
    chunker = RecursiveChunker(
        rules=sentence_rules, chunk_size=512, min_characters_per_chunk=12
    )
    chunks = chunker.chunk(sample_text)
    assert len(chunks) > 0
    assert sample_text == "".join(chunk.text for chunk in chunks)


def test_recursive_chunker_indices_sentence_rules(sample_text, sentence_rules):
    """Test that the RecursiveChunker can reconstruct a sample text with sentence rules."""
    chunker = RecursiveChunker(
        rules=sentence_rules, chunk_size=512, min_characters_per_chunk=12
    )
    chunks = chunker.chunk(sample_text)
    assert len(chunks) > 0
    assert all(chunk.start_index < chunk.end_index for chunk in chunks)
    assert all(chunk.start_index >= 0 for chunk in chunks)
    assert all(chunk.end_index <= len(sample_text) for chunk in chunks)
    assert all(
        chunk.text == sample_text[chunk.start_index : chunk.end_index]
        for chunk in chunks
    )


def test_recursive_chunker_token_count_subsentence_rules(
    sample_text, subsentence_rules
):
    """Test that the RecursiveChunker can chunk a sample text with subsentence rules."""
    chunker = RecursiveChunker(
        rules=subsentence_rules, chunk_size=512, min_characters_per_chunk=12
    )
    chunks = chunker.chunk(sample_text)
    assert len(chunks) > 0
    assert all(isinstance(chunk, Chunk) for chunk in chunks)
    assert all(chunk.token_count <= 512 for chunk in chunks)
    assert all(len(chunk.text) >= 12 for chunk in chunks)


def test_recursive_chunker_reconstruction_subsentence_rules(
    sample_text, subsentence_rules
):
    """Test that the RecursiveChunker can reconstruct a sample text with subsentence rules."""
    chunker = RecursiveChunker(
        rules=subsentence_rules, chunk_size=512, min_characters_per_chunk=12
    )
    chunks = chunker.chunk(sample_text)
    assert len(chunks) > 0
    assert sample_text == "".join(chunk.text for chunk in chunks)


def test_recursive_chunker_indices_subsentence_rules(sample_text, subsentence_rules):
    """Test that the RecursiveChunker can reconstruct a sample text with subsentence rules."""
    chunker = RecursiveChunker(
        rules=subsentence_rules, chunk_size=512, min_characters_per_chunk=12
    )
    chunks = chunker.chunk(sample_text)
    assert len(chunks) > 0
    assert all(chunk.start_index < chunk.end_index for chunk in chunks)
    assert all(chunk.start_index >= 0 for chunk in chunks)
    assert all(chunk.end_index <= len(sample_text) for chunk in chunks)
    assert all(
        chunk.text == sample_text[chunk.start_index : chunk.end_index]
        for chunk in chunks
    )


def test_recursive_chunker_token_count_word_rules(sample_text, word_rules):
    """Test that the RecursiveChunker can chunk a sample text with word rules."""
    chunker = RecursiveChunker(
        rules=word_rules, chunk_size=512, min_characters_per_chunk=12
    )
    chunks = chunker.chunk(sample_text)
    assert len(chunks) > 0
    assert all(isinstance(chunk, Chunk) for chunk in chunks)
    assert all(chunk.token_count <= 512 for chunk in chunks)
    assert all(len(chunk.text) >= 12 for chunk in chunks)


def test_recursive_chunker_reconstruction_word_rules(sample_text, word_rules):
    """Test that the RecursiveChunker can reconstruct a sample text with word rules."""
    chunker = RecursiveChunker(
        rules=word_rules, chunk_size=512, min_characters_per_chunk=12
    )
    chunks = chunker.chunk(sample_text)
    assert len(chunks) > 0
    assert sample_text == " ".join(chunk.text for chunk in chunks)


def test_recursive_chunker_indices_word_rules(sample_text, word_rules):
    """Test that the RecursiveChunker can reconstruct a sample text with word rules."""
    chunker = RecursiveChunker(
        rules=word_rules, chunk_size=512, min_characters_per_chunk=12
    )
    chunks = chunker.chunk(sample_text)
    assert len(chunks) > 0
    assert all(chunk.start_index < chunk.end_index for chunk in chunks)
    assert all(chunk.start_index >= 0 for chunk in chunks)
    assert all(chunk.end_index <= len(sample_text) for chunk in chunks)
    assert all(
        chunk.text == sample_text[chunk.start_index : chunk.end_index]
        for chunk in chunks
    )


def test_recursive_chunker_indices_token_rules(sample_text, token_rules):
    """Test that the RecursiveChunker can reconstruct a sample text with token rules."""
    chunker = RecursiveChunker(
        rules=token_rules, chunk_size=512, min_characters_per_chunk=12
    )
    chunks = chunker.chunk(sample_text)
    assert len(chunks) > 0
    assert all(chunk.start_index < chunk.end_index for chunk in chunks)
    assert all(chunk.start_index >= 0 for chunk in chunks)
    assert all(chunk.end_index <= len(sample_text) for chunk in chunks)
    assert all(
        chunk.text == sample_text[chunk.start_index : chunk.end_index]
        for chunk in chunks
    )


def test_recursive_chunker_token_count_token_rules(sample_text, token_rules):
    """Test that the RecursiveChunker can chunk a sample text with token rules."""
    chunker = RecursiveChunker(
        rules=token_rules, chunk_size=512, min_characters_per_chunk=12
    )
    chunks = chunker.chunk(sample_text)
    assert len(chunks) > 0
    assert all(isinstance(chunk, Chunk) for chunk in chunks)
    for chunk in chunks:
        assert chunk.token_count <= 512, (
            f"Chunk {chunk} has token count {chunk.token_count}"
        )
    for chunk in chunks:
        assert len(chunk.text) >= 12, (
            f"Chunk {chunk} has character count {chunk.token_count}"
        )


def test_recursive_chunker_reconstruction_token_rules(sample_text, token_rules):
    """Test that the RecursiveChunker can reconstruct a sample text with token rules."""
    chunker = RecursiveChunker(
        rules=token_rules, chunk_size=512, min_characters_per_chunk=12
    )
    chunks = chunker.chunk(sample_text)
    assert len(chunks) > 0
    assert sample_text == "".join(chunk.text for chunk in chunks)


def test_recursive_chunker_empty_text(default_rules):
    """Test that the RecursiveChunker handles empty text correctly."""
    chunker = RecursiveChunker(rules=default_rules, chunk_size=512)
    chunks = chunker.chunk("")
    assert len(chunks) == 0


def test_recursive_chunker_single_character(default_rules):
    """Test that the RecursiveChunker handles single character text correctly."""
    chunker = RecursiveChunker(
        rules=default_rules, chunk_size=512, min_characters_per_chunk=1
    )
    chunks = chunker.chunk("a")
    assert len(chunks) == 1
    assert chunks[0].text == "a"
    assert chunks[0].start_index == 0
    assert chunks[0].end_index == 1
    assert chunks[0].level == 0


def test_recursive_chunker_min_characters_per_chunk(sample_text):
    """Test that the RecursiveChunker handles min_characters_per_chunk correctly."""
    sample_text = "Hello!"
    chunker = RecursiveChunker(chunk_size=512, min_characters_per_chunk=20)
    chunks = chunker.chunk(sample_text)
    assert len(chunks) == 1
    assert chunks[0].text == "Hello!"
```

## File: `tests/chunkers/test_sdpm_chunker.py`
```python
"""Test for SDPMChunker class."""

import os

import pytest

from chonkie import SDPMChunker
from chonkie.embeddings import CohereEmbeddings, Model2VecEmbeddings, OpenAIEmbeddings
from chonkie.types import SemanticChunk


@pytest.fixture
def sample_text():
    """Sample text for testing the SemanticChunker.

    Returns:
        str: A paragraph of text about text chunking in RAG applications.

    """
    text = """The process of text chunking in RAG applications represents a delicate balance between competing requirements. On one side, we have the need for semantic coherence – ensuring that each chunk maintains meaningful context that can be understood and processed independently. On the other, we must optimize for information density, ensuring that each chunk carries sufficient signal without excessive noise that might impede retrieval accuracy. In this post, we explore the challenges of text chunking in RAG applications and propose a novel approach that leverages recent advances in transformer-based language models to achieve a more effective balance between these competing requirements."""
    return text


@pytest.fixture
def embedding_model():
    """Fixture that returns a Model2Vec embedding model for testing.

    Returns:
        Model2VecEmbeddings: A Model2Vec model initialized with 'minishlab/potion-base-8M'

    """
    return Model2VecEmbeddings("minishlab/potion-base-8M")


@pytest.fixture
def openai_embedding_model():
    """Fixture that returns an OpenAI embedding model for testing.

    Returns:
        OpenAIEmbeddings: An OpenAI model initialized with 'text-embedding-3-small'
            and the API key from environment variables.

    """
    api_key = os.environ.get("OPENAI_API_KEY")
    return OpenAIEmbeddings(model="text-embedding-3-small", api_key=api_key)


@pytest.fixture
def cohere_embedding_model():
    """Fixture that returns an Cohere embedding model for testing.

    Returns:
        CohereEmbeddings: An Cohere model initialized with 'embed-english-light-v3.0'
            and the API key from environment variables.

    """
    api_key = os.environ.get("COHERE_API_KEY")
    return CohereEmbeddings(model="embed-english-light-v3.0", api_key=api_key)


@pytest.fixture
def sample_complex_markdown_text():
    """Fixture that returns a sample markdown text with complex formatting.

    Returns:
        str: A markdown text containing various formatting elements like headings,
            lists, code blocks, links, images and blockquotes.

    """
    text = """# Heading 1
    This is a paragraph with some **bold text** and _italic text_.
    ## Heading 2
    - Bullet point 1
    - Bullet point 2 with `inline code`
    ```python
    # Code block
    def hello_world():
        print("Hello, world!")
    ```
    Another paragraph with [a link](https://example.com) and an image:
    ![Alt text](https://example.com/image.jpg)
    > A blockquote with multiple lines
    > that spans more than one line.
    Finally, a paragraph at the end.
    """
    return text


def test_sdpm_chunker_initialization(embedding_model):
    """Test that the SemanticChunker can be initialized with required parameters."""
    chunker = SDPMChunker(
        embedding_model=embedding_model,
        chunk_size=512,
        threshold=0.5,
    )

    assert chunker is not None
    assert chunker.chunk_size == 512
    assert chunker.threshold == 0.5
    assert chunker.mode == "window"
    assert chunker.similarity_window == 1
    assert chunker.min_sentences == 1
    assert chunker.min_chunk_size == 2
    assert chunker.skip_window == 1


def test_sdpm_chunker_initialization_sentence_transformer():
    """Test that the SemanticChunker can be initialized with SentenceTransformer model."""
    chunker = SDPMChunker(
        embedding_model="all-MiniLM-L6-v2",
        chunk_size=512,
        threshold=0.5,
    )

    assert chunker is not None
    assert chunker.chunk_size == 512
    assert chunker.threshold == 0.5
    assert chunker.mode == "window"
    assert chunker.similarity_window == 1
    assert chunker.min_sentences == 1
    assert chunker.min_chunk_size == 2


@pytest.mark.skipif(
    "COHERE_API_KEY" not in os.environ,
    reason="Skipping test because COHERE_API_KEY is not defined",
)
def test_sdpm_chunker_initialization_cohere(cohere_embedding_model):
    """Test that the SemanticChunker can be initialized with required parameters."""
    chunker = SDPMChunker(
        embedding_model=cohere_embedding_model,
        chunk_size=512,
        threshold=0.5,
    )

    assert chunker is not None
    assert chunker.chunk_size == 512
    assert chunker.threshold == 0.5
    assert chunker.mode == "window"
    assert chunker.similarity_window == 1
    assert chunker.min_sentences == 1
    assert chunker.min_chunk_size == 2


def test_sdpm_chunker_chunking(embedding_model, sample_text):
    """Test that the SemanticChunker can chunk a sample text."""
    chunker = SDPMChunker(
        embedding_model="all-MiniLM-L6-v2",
        chunk_size=512,
        threshold=0.5,
    )
    chunks = chunker.chunk(sample_text)

    assert len(chunks) > 0
    assert isinstance(chunks[0], SemanticChunk)
    assert all([chunk.token_count <= 512 for chunk in chunks])
    assert all([chunk.token_count > 0 for chunk in chunks])
    assert all([chunk.text is not None for chunk in chunks])
    assert all([chunk.start_index is not None for chunk in chunks])
    assert all([chunk.end_index is not None for chunk in chunks])
    assert all([chunk.sentences is not None for chunk in chunks])


def test_semantic_chunker_empty_text(embedding_model):
    """Test that the SemanticChunker can handle empty text input."""
    chunker = SDPMChunker(
        embedding_model=embedding_model,
        chunk_size=512,
        threshold=0.5,
    )
    chunks = chunker.chunk("")

    assert len(chunks) == 0


def test_semantic_chunker_single_sentence(embedding_model):
    """Test that the SemanticChunker can handle text with a single sentence."""
    chunker = SDPMChunker(
        embedding_model=embedding_model,
        chunk_size=512,
        threshold=0.5,
    )
    chunks = chunker.chunk("This is a single sentence.")

    assert len(chunks) == 1
    assert chunks[0].text == "This is a single sentence."
    assert len(chunks[0].sentences) == 1


def test_sdpm_chunker_repr(embedding_model):
    """Test that the SemanticChunker has a string representation."""
    chunker = SDPMChunker(
        embedding_model=embedding_model,
        chunk_size=512,
        threshold=0.5,
    )

    expected = (
        f"SDPMChunker(model={chunker.embedding_model}, "
        f"chunk_size={chunker.chunk_size}, "
        f"mode={chunker.mode}, "
        f"threshold={chunker.threshold}, "
        f"similarity_window={chunker.similarity_window}, "
        f"min_sentences={chunker.min_sentences}, "
        f"min_chunk_size={chunker.min_chunk_size}, "
        f"min_characters_per_sentence={chunker.min_characters_per_sentence}, "
        f"threshold_step={chunker.threshold_step}, "
        f"delim={chunker.delim}, "
        f"include_delim={chunker.include_delim}, "
        f"skip_window={chunker.skip_window}, "
        f"return_type={chunker.return_type})"
    )
    assert repr(chunker) == expected


def test_sdpm_chunker_reconstruction(embedding_model, sample_text):
    """Test that the SemanticChunker can reconstruct the original text."""
    chunker = SDPMChunker(
        embedding_model=embedding_model, chunk_size=512, threshold=0.5
    )
    chunks = chunker.chunk(sample_text)
    assert sample_text == "".join([chunk.text for chunk in chunks])


def test_sdpm_chunker_reconstruction_complex_md(
    embedding_model, sample_complex_markdown_text
):
    """Test that the SemanticChunker can reconstruct the original text."""
    chunker = SDPMChunker(
        embedding_model=embedding_model, chunk_size=512, threshold=0.5
    )
    chunks = chunker.chunk(sample_complex_markdown_text)
    assert sample_complex_markdown_text == "".join([chunk.text for chunk in chunks])


def test_sdpm_chunker_reconstruction_batch(embedding_model, sample_text):
    """Test that the SemanticChunker can reconstruct the original text."""
    chunker = SDPMChunker(
        embedding_model=embedding_model, chunk_size=512, threshold=0.5
    )
    chunks = chunker.chunk_batch([sample_text] * 10)[-1]
    assert sample_text == "".join([chunk.text for chunk in chunks])


def test_sdpm_chunker_return_type(embedding_model, sample_text):
    """Test that SemanticChunker's return type is correctly set."""
    chunker = SDPMChunker(
        embedding_model=embedding_model,
        chunk_size=512,
        threshold=0.5,
        return_type="texts",
    )
    chunks = chunker.chunk(sample_text)
    tokenizer = embedding_model.get_tokenizer_or_token_counter()
    assert all([type(chunk) is str for chunk in chunks])
    assert all([len(tokenizer.encode(chunk)) <= 512 for chunk in chunks])
```

## File: `tests/chunkers/test_semantic_chunker.py`
```python
"""Test the SemanticChunker class."""

import os
from typing import List

import pytest

from chonkie import SemanticChunker
from chonkie.embeddings import (
    CohereEmbeddings,
    Model2VecEmbeddings,
    OpenAIEmbeddings,
)
from chonkie.types.base import Chunk
from chonkie.types.semantic import SemanticChunk


@pytest.fixture
def sample_text():
    """Sample text for testing the SemanticChunker.

    Returns:
        str: A paragraph of text about text chunking in RAG applications.

    """
    text = """The process of text chunking in RAG applications represents a delicate balance between competing requirements. On one side, we have the need for semantic coherence – ensuring that each chunk maintains meaningful context that can be understood and processed independently. On the other, we must optimize for information density, ensuring that each chunk carries sufficient signal without excessive noise that might impede retrieval accuracy. In this post, we explore the challenges of text chunking in RAG applications and propose a novel approach that leverages recent advances in transformer-based language models to achieve a more effective balance between these competing requirements."""
    return text


@pytest.fixture
def embedding_model():
    """Fixture that returns a Model2Vec embedding model for testing.

    Returns:
        Model2VecEmbeddings: A Model2Vec model initialized with 'minishlab/potion-base-8M'

    """
    return Model2VecEmbeddings("minishlab/potion-base-8M")


@pytest.fixture
def openai_embedding_model():
    """Fixture that returns an OpenAI embedding model for testing.

    Returns:
        OpenAIEmbeddings: An OpenAI model initialized with 'text-embedding-3-small'
            and the API key from environment variables.

    """
    api_key = os.environ.get("OPENAI_API_KEY")
    return OpenAIEmbeddings(model="text-embedding-3-small", api_key=api_key)


@pytest.fixture
def cohere_embedding_model():
    """Fixture that returns an Cohere embedding model for testing.

    Returns:
        CohereEmbeddings: An Cohere model initialized with 'embed-english-light-v3.0'
            and the API key from environment variables.

    """
    api_key = os.environ.get("COHERE_API_KEY")
    return CohereEmbeddings(model="embed-english-light-v3.0", api_key=api_key)


@pytest.fixture
def sample_complex_markdown_text():
    """Fixture that returns a sample markdown text with complex formatting.

    Returns:
        str: A markdown text containing various formatting elements like headings,
            lists, code blocks, links, images and blockquotes.

    """
    text = """# Heading 1
    This is a paragraph with some **bold text** and _italic text_.
    ## Heading 2
    - Bullet point 1
    - Bullet point 2 with `inline code`
    ```python
    # Code block
    def hello_world():
        print("Hello, world!")
    ```
    Another paragraph with [a link](https://example.com) and an image:
    ![Alt text](https://example.com/image.jpg)
    > A blockquote with multiple lines
    > that spans more than one line.
    Finally, a paragraph at the end.
    """
    return text


def test_semantic_chunker_initialization(embedding_model):
    """Test that the SemanticChunker can be initialized with required parameters."""
    chunker = SemanticChunker(
        embedding_model=embedding_model,
        chunk_size=512,
        threshold=0.5,
    )

    assert chunker is not None
    assert chunker.chunk_size == 512
    assert chunker.threshold == 0.5
    assert chunker.mode == "window"
    assert chunker.similarity_window == 1
    assert chunker.min_sentences == 1
    assert chunker.min_chunk_size == 2


@pytest.mark.skipif(
    "OPENAI_API_KEY" not in os.environ,
    reason="Skipping test because OPENAI_API_KEY is not defined",
)
def test_semantic_chunker_initialization_openai(openai_embedding_model):
    """Test that the SemanticChunker can be initialized with required parameters."""
    chunker = SemanticChunker(
        embedding_model=openai_embedding_model,
        chunk_size=512,
        threshold=0.5,
    )

    assert chunker is not None
    assert chunker.chunk_size == 512
    assert chunker.threshold == 0.5
    assert chunker.mode == "window"
    assert chunker.similarity_window == 1
    assert chunker.min_sentences == 1
    assert chunker.min_chunk_size == 2


def test_semantic_chunker_initialization_sentence_transformer():
    """Test that the SemanticChunker can be initialized with SentenceTransformer model."""
    chunker = SemanticChunker(
        embedding_model="all-MiniLM-L6-v2",
        chunk_size=512,
        threshold=0.5,
    )

    assert chunker is not None
    assert chunker.chunk_size == 512
    assert chunker.threshold == 0.5
    assert chunker.mode == "window"
    assert chunker.similarity_window == 1
    assert chunker.min_sentences == 1
    assert chunker.min_chunk_size == 2


@pytest.mark.skipif(
    "COHERE_API_KEY" not in os.environ,
    reason="Skipping test because COHERE_API_KEY is not defined",
)
def test_semantic_chunker_initialization_cohere(cohere_embedding_model):
    """Test that the SemanticChunker can be initialized with required parameters."""
    chunker = SemanticChunker(
        embedding_model=cohere_embedding_model,
        chunk_size=512,
        threshold=0.5,
    )

    assert chunker is not None
    assert chunker.chunk_size == 512
    assert chunker.threshold == 0.5
    assert chunker.mode == "window"
    assert chunker.similarity_window == 1
    assert chunker.min_sentences == 1
    assert chunker.min_chunk_size == 2


def test_semantic_chunker_chunking(embedding_model, sample_text):
    """Test that the SemanticChunker can chunk a sample text."""
    chunker = SemanticChunker(
        embedding_model="all-MiniLM-L6-v2",
        chunk_size=512,
        threshold=0.5,
    )
    chunks = chunker.chunk(sample_text)

    assert len(chunks) > 0
    assert isinstance(chunks[0], SemanticChunk)
    assert all([chunk.token_count <= 512 for chunk in chunks])
    assert all([chunk.token_count > 0 for chunk in chunks])
    assert all([chunk.text is not None for chunk in chunks])
    assert all([chunk.start_index is not None for chunk in chunks])
    assert all([chunk.end_index is not None for chunk in chunks])
    assert all([chunk.sentences is not None for chunk in chunks])


def test_semantic_chunker_empty_text(embedding_model):
    """Test that the SemanticChunker can handle empty text input."""
    chunker = SemanticChunker(
        embedding_model=embedding_model,
        chunk_size=512,
        threshold=0.5,
    )
    chunks = chunker.chunk("")

    assert len(chunks) == 0


def test_semantic_chunker_single_sentence(embedding_model):
    """Test that the SemanticChunker can handle text with a single sentence."""
    chunker = SemanticChunker(
        embedding_model=embedding_model,
        chunk_size=512,
        threshold=0.5,
    )
    chunks = chunker.chunk("This is a single sentence.")

    assert len(chunks) == 1
    assert chunks[0].text == "This is a single sentence."
    assert len(chunks[0].sentences) == 1


def test_semantic_chunker_repr(embedding_model):
    """Test that the SemanticChunker has a string representation."""
    chunker = SemanticChunker(
        embedding_model=embedding_model,
        chunk_size=512,
        threshold=0.5,
    )

    expected = (
        f"SemanticChunker(model={chunker.embedding_model}, "
        f"chunk_size={chunker.chunk_size}, "
        f"mode={chunker.mode}, "
        f"threshold={chunker.threshold}, "
        f"similarity_window={chunker.similarity_window}, "
        f"min_sentences={chunker.min_sentences}, "
        f"min_chunk_size={chunker.min_chunk_size}, "
        f"return_type={chunker.return_type})"
    )
    assert repr(chunker) == expected


def test_semantic_chunker_similarity_threshold(embedding_model):
    """Test that the SemanticChunker respects similarity threshold."""
    chunker = SemanticChunker(
        embedding_model=embedding_model,
        chunk_size=512,
        threshold=0.9,  # High threshold should create more chunks
    )
    text = (
        "This is about cars. This is about planes. "
        "This is about trains. This is about boats."
    )
    chunks = chunker.chunk(text)

    # With high similarity threshold, we expect more chunks due to low similarity
    assert len(chunks) > 1


def test_semantic_chunker_percentile_mode(embedding_model, sample_text):
    """Test that the SemanticChunker works with percentile-based similarity."""
    chunker = SemanticChunker(
        embedding_model=embedding_model,
        chunk_size=512,
        threshold=50,  # Use median similarity as threshold
    )
    chunks = chunker.chunk(sample_text)

    assert len(chunks) > 0
    assert all([isinstance(chunk, SemanticChunk) for chunk in chunks])


def verify_chunk_indices(chunks: List[Chunk], original_text: str):
    """Verify that chunk indices correctly map to the original text."""
    for i, chunk in enumerate(chunks):
        # Extract text using the indices
        extracted_text = original_text[chunk.start_index : chunk.end_index]
        # Remove any leading/trailing whitespace from both texts for comparison
        chunk_text = chunk.text.strip()
        extracted_text = extracted_text.strip()

        assert chunk_text == extracted_text, (
            f"Chunk {i} text mismatch:\n"
            f"Chunk text: '{chunk_text}'\n"
            f"Extracted text: '{extracted_text}'\n"
            f"Indices: [{chunk.start_index}:{chunk.end_index}]"
        )


def test_sentence_chunker_indices(embedding_model, sample_text):
    """Test that the SentenceChunker correctly maps chunk indices to the original text."""
    chunker = SemanticChunker(
        embedding_model=embedding_model, chunk_size=512, threshold=0.5
    )
    chunks = chunker.chunk(sample_text)
    verify_chunk_indices(chunks, sample_text)


def test_sentence_chunker_indices_complex_md(
    embedding_model, sample_complex_markdown_text
):
    """Test that the SentenceChunker correctly maps chunk indices to the original text."""
    chunker = SemanticChunker(
        embedding_model=embedding_model, chunk_size=512, threshold=0.5
    )
    chunks = chunker.chunk(sample_complex_markdown_text)
    verify_chunk_indices(chunks, sample_complex_markdown_text)


def test_semantic_chunker_token_counts(embedding_model, sample_text):
    """Test that the SemanticChunker correctly calculates token counts."""
    chunker = SemanticChunker(
        embedding_model=embedding_model, chunk_size=512, threshold=0.5
    )
    chunks = chunker.chunk(sample_text)
    assert all([chunk.token_count > 0 for chunk in chunks]), (
        "All chunks must have a positive token count"
    )
    assert all([chunk.token_count <= 512 for chunk in chunks]), (
        "All chunks must have a token count less than or equal to 512"
    )

    token_counts = [chunker.tokenizer.count_tokens(chunk.text) for chunk in chunks]
    for i, (chunk, token_count) in enumerate(zip(chunks, token_counts)):
        assert chunk.token_count == token_count, (
            f"Chunk {i} has a token count of {chunk.token_count} but the encoded text length is {token_count}"
        )


def test_semantic_chunker_reconstruction(embedding_model, sample_text):
    """Test that the SemanticChunker can reconstruct the original text."""
    chunker = SemanticChunker(
        embedding_model=embedding_model, chunk_size=512, threshold=0.5
    )
    chunks = chunker.chunk(sample_text)
    assert sample_text == "".join([chunk.text for chunk in chunks])


def test_semantic_chunker_reconstruction_complex_md(
    embedding_model, sample_complex_markdown_text
):
    """Test that the SemanticChunker can reconstruct the original text."""
    chunker = SemanticChunker(
        embedding_model=embedding_model, chunk_size=512, threshold=0.5
    )
    chunks = chunker.chunk(sample_complex_markdown_text)
    assert sample_complex_markdown_text == "".join([chunk.text for chunk in chunks])


def test_semantic_chunker_reconstruction_batch(embedding_model, sample_text):
    """Test that the SemanticChunker can reconstruct the original text."""
    chunker = SemanticChunker(
        embedding_model=embedding_model, chunk_size=512, threshold=0.5
    )
    chunks = chunker.chunk_batch([sample_text] * 10)[-1]
    assert sample_text == "".join([chunk.text for chunk in chunks])


def test_semantic_chunker_return_type(embedding_model, sample_text):
    """Test that SemanticChunker's return type is correctly set."""
    chunker = SemanticChunker(
        embedding_model=embedding_model,
        chunk_size=512,
        threshold=0.5,
        return_type="texts",
    )
    chunks = chunker.chunk(sample_text)
    tokenizer = embedding_model.get_tokenizer_or_token_counter()
    assert all([type(chunk) is str for chunk in chunks])
    assert all([len(tokenizer.encode(chunk)) <= 512 for chunk in chunks])
```

## File: `tests/chunkers/test_sentence_chunker.py`
```python
"""Test cases for the SentenceChunker."""

from __future__ import annotations

from typing import List

import pytest
from tokenizers import Tokenizer

from chonkie import Chunk, SentenceChunker


@pytest.fixture
def tokenizer():
    """Return a tokenizer instance."""
    return Tokenizer.from_pretrained("gpt2")


@pytest.fixture
def sample_text():
    """Return a sample text."""
    text = """# Chunking Strategies in Retrieval-Augmented Generation: A Comprehensive Analysis\n\nIn the rapidly evolving landscape of natural language processing, Retrieval-Augmented Generation (RAG) has emerged as a groundbreaking approach that bridges the gap between large language models and external knowledge bases. At the heart of these systems lies a crucial yet often overlooked process: chunking. This fundamental operation, which involves the systematic decomposition of large text documents into smaller, semantically meaningful units, plays a pivotal role in determining the overall effectiveness of RAG implementations.\n\nThe process of text chunking in RAG applications represents a delicate balance between competing requirements. On one side, we have the need for semantic coherence – ensuring that each chunk maintains meaningful context that can be understood and processed independently. On the other, we must optimize for information density, ensuring that each chunk carries sufficient signal without excessive noise that might impede retrieval accuracy. This balancing act becomes particularly crucial when we consider the downstream implications for vector databases and embedding models that form the backbone of modern RAG systems.\n\nThe selection of appropriate chunk size emerges as a fundamental consideration that significantly impacts system performance. Through extensive experimentation and real-world implementations, researchers have identified that chunks typically perform optimally in the range of 256 to 1024 tokens. However, this range should not be treated as a rigid constraint but rather as a starting point for optimization based on specific use cases and requirements. The implications of chunk size selection ripple throughout the entire RAG pipeline, affecting everything from storage requirements to retrieval accuracy and computational overhead.\n\nFixed-size chunking represents the most straightforward approach to document segmentation, offering predictable memory usage and consistent processing time. However, this apparent simplicity comes with significant drawbacks. By arbitrarily dividing text based on token or character count, fixed-size chunking risks fragmenting semantic units and disrupting the natural flow of information. Consider, for instance, a technical document where a complex concept is explained across several paragraphs – fixed-size chunking might split this explanation at critical junctures, potentially compromising the system's ability to retrieve and present this information coherently.\n\nIn response to these limitations, semantic chunking has gained prominence as a more sophisticated alternative. This approach leverages natural language understanding to identify meaningful boundaries within the text, respecting the natural structure of the document. Semantic chunking can operate at various levels of granularity, from simple sentence-based segmentation to more complex paragraph-level or topic-based approaches. The key advantage lies in its ability to preserve the inherent semantic relationships within the text, leading to more meaningful and contextually relevant retrieval results.\n\nRecent advances in the field have given rise to hybrid approaches that attempt to combine the best aspects of both fixed-size and semantic chunking. These methods typically begin with semantic segmentation but impose size constraints to prevent extreme variations in chunk length. Furthermore, the introduction of sliding window techniques with overlap has proved particularly effective in maintaining context across chunk boundaries. This overlap, typically ranging from 10% to 20% of the chunk size, helps ensure that no critical information is lost at segment boundaries, albeit at the cost of increased storage requirements.\n\nThe implementation of chunking strategies must also consider various technical factors that can significantly impact system performance. Vector database capabilities, embedding model constraints, and runtime performance requirements all play crucial roles in determining the optimal chunking approach. Moreover, content-specific factors such as document structure, language characteristics, and domain-specific requirements must be carefully considered. For instance, technical documentation might benefit from larger chunks that preserve detailed explanations, while news articles might perform better with smaller, more focused segments.\n\nThe future of chunking in RAG systems points toward increasingly sophisticated approaches. Current research explores the potential of neural chunking models that can learn optimal segmentation strategies from large-scale datasets. These models show promise in adapting to different content types and query patterns, potentially leading to more efficient and effective retrieval systems. Additionally, the emergence of cross-lingual chunking strategies addresses the growing need for multilingual RAG applications, while real-time adaptive chunking systems attempt to optimize segment boundaries based on user interaction patterns and retrieval performance metrics.\n\nThe effectiveness of RAG systems heavily depends on the thoughtful implementation of appropriate chunking strategies. While the field continues to evolve, practitioners must carefully consider their specific use cases and requirements when designing chunking solutions. Factors such as document characteristics, retrieval patterns, and performance requirements should guide the selection and optimization of chunking strategies. As we look to the future, the continued development of more sophisticated chunking approaches promises to further enhance the capabilities of RAG systems, enabling more accurate and efficient information retrieval and generation.\n\nThrough careful consideration of these various aspects and continued experimentation with different approaches, organizations can develop chunking strategies that effectively balance the competing demands of semantic coherence, computational efficiency, and retrieval accuracy. As the field continues to evolve, we can expect to see new innovations that further refine our ability to segment and process textual information in ways that enhance the capabilities of RAG systems while maintaining their practical utility in real-world applications."""
    return text


@pytest.fixture
def sample_complex_markdown_text():
    """Return a sample complex markdown text."""
    text = """# Heading 1
    This is a paragraph with some **bold text** and _italic text_. 
    ## Heading 2
    - Bullet point 1
    - Bullet point 2 with `inline code`
    ```python
    # Code block
    def hello_world():
        print("Hello, world!")
    ```
    Another paragraph with [a link](https://example.com) and an image:
    ![Alt text](https://example.com/image.jpg)
    > A blockquote with multiple lines
    > that spans more than one line.
    Finally, a paragraph at the end.
    """
    return text


def test_sentence_chunker_initialization(tokenizer):
    """Test that the SentenceChunker can be initialized with a tokenizer."""
    chunker = SentenceChunker(
        tokenizer_or_token_counter=tokenizer, chunk_size=512, chunk_overlap=128
    )

    assert chunker is not None
    assert chunker.tokenizer.tokenizer == tokenizer
    assert chunker.chunk_size == 512
    assert chunker.chunk_overlap == 128
    assert chunker.min_sentences_per_chunk == 1
    assert chunker.approximate == True
    assert chunker.delim == [".", "!", "?", "\n"]
    assert chunker.include_delim == "prev"
    assert chunker.return_type == "chunks"


def test_sentence_chunker_chunking(tokenizer, sample_text):
    """Test that the SentenceChunker can chunk a sample text into sentences."""
    chunker = SentenceChunker(
        tokenizer_or_token_counter=tokenizer, chunk_size=512, chunk_overlap=128
    )
    chunks = chunker.chunk(sample_text)

    assert len(chunks) > 0
    assert isinstance(chunks[0], Chunk)
    assert all([chunk.token_count <= 512 for chunk in chunks])
    assert all([chunk.token_count > 0 for chunk in chunks])
    assert all([chunk.text is not None for chunk in chunks])
    assert all([chunk.start_index is not None for chunk in chunks])
    assert all([chunk.end_index is not None for chunk in chunks])


def test_sentence_chunker_empty_text(tokenizer):
    """Test that the SentenceChunker can handle empty text input."""
    chunker = SentenceChunker(
        tokenizer_or_token_counter=tokenizer, chunk_size=512, chunk_overlap=128
    )
    chunks = chunker.chunk("")

    assert len(chunks) == 0


def test_sentence_chunker_single_sentence(tokenizer):
    """Test that the SentenceChunker can handle text with a single sentence."""
    chunker = SentenceChunker(
        tokenizer_or_token_counter=tokenizer, chunk_size=512, chunk_overlap=128
    )
    chunks = chunker.chunk("This is a single sentence.")

    assert len(chunks) == 1
    assert chunks[0].text == "This is a single sentence."


def test_sentence_chunker_single_chunk_text(tokenizer):
    """Test that the SentenceChunker can handle text that fits within a single chunk."""
    chunker = SentenceChunker(
        tokenizer_or_token_counter=tokenizer, chunk_size=512, chunk_overlap=128
    )
    chunks = chunker.chunk("Hello, how are you? I am doing well.")

    assert len(chunks) == 1
    assert chunks[0].text == "Hello, how are you? I am doing well."


def test_sentence_chunker_repr(tokenizer):
    """Test that the SentenceChunker has a string representation."""
    chunker = SentenceChunker(
        tokenizer_or_token_counter=tokenizer, chunk_size=512, chunk_overlap=128
    )

    assert repr(chunker) == (
        f"SentenceChunker(tokenizer={chunker.tokenizer}, "
        f"chunk_size={chunker.chunk_size}, "
        f"chunk_overlap={chunker.chunk_overlap}, "
        f"min_sentences_per_chunk={chunker.min_sentences_per_chunk}, "
        f"min_characters_per_sentence={chunker.min_characters_per_sentence}, "
        f"approximate={chunker.approximate}, "
        f"delim={chunker.delim}, "
        f"include_delim={chunker.include_delim}, "
        f"return_type={chunker.return_type})"
    )


def test_sentence_chunker_overlap(tokenizer, sample_text):
    """Test that the SentenceChunker creates overlapping chunks correctly."""
    chunker = SentenceChunker(
        tokenizer_or_token_counter=tokenizer, chunk_size=512, chunk_overlap=128
    )
    chunks = chunker.chunk(sample_text)

    for i in range(1, len(chunks)):
        assert chunks[i].start_index < chunks[i - 1].end_index


def test_sentence_chunker_min_sentences(tokenizer):
    """Test that the SentenceChunker respects minimum sentences per chunk."""
    chunker = SentenceChunker(
        tokenizer_or_token_counter=tokenizer,
        chunk_size=512,
        chunk_overlap=128,
        min_sentences_per_chunk=2,
    )
    chunks = chunker.chunk("First sentence. Second sentence. Third sentence.")

    assert len(chunks) > 0
    for chunk in chunks:
        # Count sentences by splitting on periods
        sentence_count = len([s for s in chunk.text.split(".") if s.strip()])
        assert (
            sentence_count >= 2 or sentence_count == 1
        )  # Last chunk might have fewer sentences


def verify_chunk_indices(chunks: List[Chunk], original_text: str):
    """Verify that chunk indices correctly map to the original text."""
    for i, chunk in enumerate(chunks):
        # Extract text using the indices
        extracted_text = original_text[chunk.start_index : chunk.end_index]
        # Remove any leading/trailing whitespace from both texts for comparison
        chunk_text = chunk.text.strip()
        extracted_text = extracted_text.strip()

        assert chunk_text == extracted_text, (
            f"Chunk {i} text mismatch:\n"
            f"Chunk text: '{chunk_text}'\n"
            f"Extracted text: '{extracted_text}'\n"
            f"Indices: [{chunk.start_index}:{chunk.end_index}]"
        )


def test_sentence_chunker_indices(tokenizer, sample_text):
    """Test that the SentenceChunker correctly maps chunk indices to the original text."""
    chunker = SentenceChunker(
        tokenizer_or_token_counter=tokenizer, chunk_size=512, chunk_overlap=128
    )
    chunks = chunker.chunk(sample_text)
    verify_chunk_indices(chunks, sample_text)


def test_sentence_chunker_indices_complex_md(
    tokenizer, sample_complex_markdown_text
):
    """Test that the SentenceChunker correctly maps chunk indices to the original text."""
    chunker = SentenceChunker(
        tokenizer_or_token_counter=tokenizer, chunk_size=512, chunk_overlap=128
    )
    chunks = chunker.chunk(sample_complex_markdown_text)
    verify_chunk_indices(chunks, sample_complex_markdown_text)


def test_sentence_chunker_token_counts(tokenizer, sample_text):
    """Test that the SentenceChunker correctly calculates token counts."""
    chunker = SentenceChunker(
        tokenizer_or_token_counter=tokenizer, chunk_size=512, chunk_overlap=128
    )
    chunks = chunker.chunk(sample_text)
    assert all([chunk.token_count > 0 for chunk in chunks]), (
        "All chunks must have a positive token count"
    )
    assert all([chunk.token_count <= 512 for chunk in chunks]), (
        "All chunks must have a token count less than or equal to 512"
    )

    token_counts = [len(tokenizer.encode(chunk.text)) for chunk in chunks]
    assert all([
        chunk.token_count == token_count
        for chunk, token_count in zip(chunks, token_counts)
    ]), (
        "All chunks must have a token count equal to the length of the encoded text"
    )


def test_sentence_chunker_return_type(tokenizer, sample_text):
    """Test that SentenceChunker's return type is correctly set."""
    chunker = SentenceChunker(
        tokenizer_or_token_counter=tokenizer,
        chunk_size=512,
        chunk_overlap=128,
        return_type="texts",
    )
    chunks = chunker.chunk(sample_text)
    assert all([type(chunk) is str for chunk in chunks])
    assert all([len(tokenizer.encode(chunk)) <= 512 for chunk in chunks])


def test_sentence_chunker_min_sentences_per_chunk(tokenizer, sample_text):
    """Test that SentenceChunker respects minimum sentences per chunk."""
    # Test that the minimum sentences per chunk is respected, giving a warning otherwise!
    sample_text = "This is a test."
    chunker = SentenceChunker(
        tokenizer_or_token_counter=tokenizer,
        chunk_size=512,
        chunk_overlap=128,
        min_sentences_per_chunk=2,
    )
    chunks = chunker.chunk(sample_text)
    assert len(chunks) == 1
    assert chunks[0].text == "This is a test."
    assert chunks[0].token_count == len(tokenizer.encode(sample_text))


def test_sentence_chunker_min_characters_per_sentence(tokenizer):
    """Test that SentenceChunker respects minimum characters per sentence and when less than min_characters_per_sentence, it is merged with the next sentence."""
    sample_text = "Hello!"
    chunker = SentenceChunker(
        tokenizer_or_token_counter=tokenizer,
        chunk_size=512,
        min_characters_per_sentence=20,
    )
    chunks = chunker.chunk(sample_text)
    assert len(chunks) == 1
    assert chunks[0].text == "Hello!"


if __name__ == "__main__":
    pytest.main()
```

## File: `tests/chunkers/test_token_chunker.py`
```python
"""Tests for the TokenChunker class."""

from __future__ import annotations

from typing import List

import pytest
import tiktoken
from datasets import load_dataset
from tiktoken import Encoding
from tokenizers import Tokenizer
from transformers import AutoTokenizer, PreTrainedTokenizerFast

from chonkie import Chunk, TokenChunker


@pytest.fixture
def tiktokenizer() -> Encoding:
    """Fixture that returns a GPT-2 tokenizer from the tiktoken library."""
    return tiktoken.get_encoding("gpt2")


@pytest.fixture
def transformers_tokenizer() -> PreTrainedTokenizerFast:
    """Fixture that returns a GPT-2 tokenizer from the transformers library."""
    return AutoTokenizer.from_pretrained("gpt2")


@pytest.fixture
def tokenizer() -> Tokenizer:
    """Fixture that returns a GPT-2 tokenizer from the tokenizers library."""
    return Tokenizer.from_pretrained("gpt2")


@pytest.fixture
def sample_text() -> str:
    """Fixture that returns a sample text for testing the TokenChunker."""
    text = """According to all known laws of aviation, there is no way a bee should be able to fly. Its wings are too small to get its fat little body off the ground. The bee, of course, flies anyway because bees don't care what humans think is impossible. Yellow, black. Yellow, black. Yellow, black. Yellow, black. Ooh, black and yellow! Let's shake it up a little. Barry! Breakfast is ready! Coming! Hang on a second. Hello? - Barry? - Adam? - Can you believe this is happening? - I can't. I'll pick you up. Looking sharp. Use the stairs. Your father paid good money for those. Sorry. I'm excited. Here's the graduate. We're very proud of you, son. A perfect report card, all B's. Very proud. Ma! I got a thing going here."""
    return text


@pytest.fixture
def sample_batch():
    """Fixture that returns a sample batch of texts for testing the TokenChunker."""
    ds = load_dataset("bhavnicksm/fineweb-edu-micro", split="train")
    return list(ds["text"])


@pytest.fixture
def sample_complex_markdown_text():
    """Fixture that returns a sample markdown text with complex formatting."""
    text = """# Heading 1
    This is a paragraph with some **bold text** and _italic text_. 
    ## Heading 2
    - Bullet point 1
    - Bullet point 2 with `inline code`
    ```python
    # Code block
    def hello_world():
        print("Hello, world!")
    ```
    Another paragraph with [a link](https://example.com) and an image:
    ![Alt text](https://example.com/image.jpg)
    > A blockquote with multiple lines
    > that spans more than one line.
    Finally, a paragraph at the end.
    """
    return text


def test_token_chunker_initialization_tok(tokenizer):
    """Test that the TokenChunker can be initialized with a tokenizer."""
    chunker = TokenChunker(
        tokenizer=tokenizer, chunk_size=512, chunk_overlap=128
    )

    assert chunker is not None
    assert chunker.tokenizer.tokenizer == tokenizer
    assert chunker.chunk_size == 512
    assert chunker.chunk_overlap == 128


def test_token_chunker_initialization_hftok(transformers_tokenizer):
    """Test that the TokenChunker can be initialized with a tokenizer."""
    chunker = TokenChunker(
        tokenizer=transformers_tokenizer, chunk_size=512, chunk_overlap=128
    )

    assert chunker is not None
    assert chunker.tokenizer.tokenizer == transformers_tokenizer
    assert chunker.chunk_size == 512
    assert chunker.chunk_overlap == 128


def test_token_chunker_initialization_tik(tiktokenizer):
    """Test that the TokenChunker can be initialized with a tokenizer."""
    chunker = TokenChunker(
        tokenizer=tiktokenizer, chunk_size=512, chunk_overlap=128
    )

    assert chunker is not None
    assert chunker.tokenizer.tokenizer == tiktokenizer
    assert chunker.chunk_size == 512
    assert chunker.chunk_overlap == 128


def test_token_chunker_chunking(tiktokenizer, sample_text):
    """Test that the TokenChunker can chunk a sample text into tokens."""
    chunker = TokenChunker(
        tokenizer=tiktokenizer, chunk_size=512, chunk_overlap=128
    )
    chunks = chunker.chunk(sample_text)

    assert len(chunks) > 0
    assert type(chunks[0]) is Chunk
    assert all([chunk.token_count <= 512 for chunk in chunks])
    assert all([chunk.token_count > 0 for chunk in chunks])
    assert all([chunk.text is not None for chunk in chunks])
    assert all([chunk.start_index is not None for chunk in chunks])
    assert all([chunk.end_index is not None for chunk in chunks])


def test_token_chunker_chunking_hf(transformers_tokenizer, sample_text):
    """Test that the TokenChunker can chunk a sample text into tokens."""
    chunker = TokenChunker(
        tokenizer=transformers_tokenizer, chunk_size=512, chunk_overlap=128
    )
    chunks = chunker.chunk(sample_text)

    assert len(chunks) > 0
    assert type(chunks[0]) is Chunk
    assert all([chunk.token_count <= 512 for chunk in chunks])
    assert all([chunk.token_count > 0 for chunk in chunks])
    assert all([chunk.text is not None for chunk in chunks])
    assert all([chunk.start_index is not None for chunk in chunks])
    assert all([chunk.end_index is not None for chunk in chunks])


def test_token_chunker_chunking_tik(tiktokenizer, sample_text):
    """Test that the TokenChunker can chunk a sample text into tokens."""
    chunker = TokenChunker(
        tokenizer=tiktokenizer, chunk_size=512, chunk_overlap=128
    )
    chunks = chunker.chunk(sample_text)

    assert len(chunks) > 0
    assert type(chunks[0]) is Chunk
    assert all([chunk.token_count <= 512 for chunk in chunks])
    assert all([chunk.token_count > 0 for chunk in chunks])
    assert all([chunk.text is not None for chunk in chunks])
    assert all([chunk.start_index is not None for chunk in chunks])
    assert all([chunk.end_index is not None for chunk in chunks])


def test_token_chunker_empty_text(tiktokenizer):
    """Test that the TokenChunker can handle empty text input."""
    chunker = TokenChunker(
        tokenizer=tiktokenizer, chunk_size=512, chunk_overlap=128
    )
    chunks = chunker.chunk("")

    assert len(chunks) == 0


def test_token_chunker_single_token_text(tokenizer):
    """Test that the TokenChunker can handle text with a single token."""
    chunker = TokenChunker(
        tokenizer=tokenizer, chunk_size=512, chunk_overlap=128
    )
    chunks = chunker.chunk("Hello")

    assert len(chunks) == 1
    assert chunks[0].token_count == 1
    assert chunks[0].text == "Hello"


def test_token_chunker_single_token_text_hf(transformers_tokenizer):
    """Test that the TokenChunker can handle text with a single token."""
    chunker = TokenChunker(
        tokenizer=transformers_tokenizer, chunk_size=512, chunk_overlap=128
    )
    chunks = chunker.chunk("Hello")

    assert len(chunks) == 1
    assert chunks[0].token_count == 1
    assert chunks[0].text == "Hello"


def test_token_chunker_single_token_text_tik(tiktokenizer):
    """Test that the TokenChunker can handle text with a single token."""
    chunker = TokenChunker(
        tokenizer=tiktokenizer, chunk_size=512, chunk_overlap=128
    )
    chunks = chunker.chunk("Hello")

    assert len(chunks) == 1
    assert chunks[0].token_count == 1
    assert chunks[0].text == "Hello"


def test_token_chunker_single_chunk_text(tokenizer):
    """Test that the TokenChunker can handle text that fits within a single chunk."""
    chunker = TokenChunker(
        tokenizer=tokenizer, chunk_size=512, chunk_overlap=128
    )
    chunks = chunker.chunk("Hello, how are you?")

    assert len(chunks) == 1
    assert chunks[0].token_count == 6
    assert chunks[0].text == "Hello, how are you?"


def test_token_chunker_batch_chunking(tiktokenizer, sample_batch):
    """Test that the TokenChunker can chunk a batch of texts into tokens."""
    chunker = TokenChunker(
        tokenizer=tiktokenizer, chunk_size=512, chunk_overlap=128
    )
    chunks = chunker.chunk_batch(sample_batch)

    assert len(chunks) > 0
    assert all([len(chunk) > 0 for chunk in chunks])
    assert all([type(chunk[0]) is Chunk for chunk in chunks])
    assert all([
        all([chunk.token_count <= 512 for chunk in chunks]) for chunks in chunks
    ])
    assert all([
        all([chunk.token_count > 0 for chunk in chunks]) for chunks in chunks
    ])
    assert all([
        all([chunk.text is not None for chunk in chunks]) for chunks in chunks
    ])
    assert all([
        all([chunk.start_index is not None for chunk in chunks])
        for chunks in chunks
    ])
    assert all([
        all([chunk.end_index is not None for chunk in chunks])
        for chunks in chunks
    ])


def test_token_chunker_repr(tiktokenizer):
    """Test that the TokenChunker has a string representation."""
    chunker = TokenChunker(
        tokenizer=tiktokenizer, chunk_size=512, chunk_overlap=128
    )

    assert repr(chunker) == (
        f"TokenChunker(tokenizer={chunker.tokenizer}, "
        f"chunk_size={chunker.chunk_size}, "
        f"chunk_overlap={chunker.chunk_overlap}, "
        f"return_type={chunker.return_type})"
    )


def test_token_chunker_call(tiktokenizer, sample_text):
    """Test that the TokenChunker can be called directly."""
    chunker = TokenChunker(
        tokenizer=tiktokenizer, chunk_size=512, chunk_overlap=128
    )
    chunks = chunker(sample_text)

    assert len(chunks) > 0
    assert type(chunks[0]) is Chunk
    assert all([chunk.token_count <= 512 for chunk in chunks])
    assert all([chunk.token_count > 0 for chunk in chunks])
    assert all([chunk.text is not None for chunk in chunks])
    assert all([chunk.start_index is not None for chunk in chunks])
    assert all([chunk.end_index is not None for chunk in chunks])


def verify_chunk_indices(chunks: List[Chunk], original_text: str):
    """Verify that chunk indices correctly map to the original text."""
    for i, chunk in enumerate(chunks):
        # Extract text using the indices
        extracted_text = original_text[chunk.start_index : chunk.end_index]
        # Remove any leading/trailing whitespace from both texts for comparison
        chunk_text = chunk.text.strip()
        extracted_text = extracted_text.strip()

        assert chunk_text == extracted_text, (
            f"Chunk {i} text mismatch:\n"
            f"Chunk text: '{chunk_text}'\n"
            f"Extracted text: '{extracted_text}'\n"
            f"Indices: [{chunk.start_index}:{chunk.end_index}]"
        )


def test_token_chunker_indices(tiktokenizer, sample_text):
    """Test that TokenChunker's indices correctly map to original text."""
    tokenizer = Tokenizer.from_pretrained("gpt2")
    chunker = TokenChunker(
        tokenizer=tokenizer, chunk_size=512, chunk_overlap=128
    )
    chunks = chunker.chunk(sample_text)
    verify_chunk_indices(chunks, sample_text)


def test_token_chunker_indices_complex_md(sample_complex_markdown_text):
    """Test that TokenChunker's indices correctly map to original text."""
    tokenizer = Tokenizer.from_pretrained("gpt2")
    chunker = TokenChunker(
        tokenizer=tokenizer, chunk_size=512, chunk_overlap=128
    )
    chunks = chunker.chunk(sample_complex_markdown_text)
    verify_chunk_indices(chunks, sample_complex_markdown_text)


def test_token_chunker_token_counts(tiktokenizer, sample_text):
    """Test that the TokenChunker correctly calculates token counts."""
    chunker = TokenChunker(
        tokenizer=tiktokenizer, chunk_size=512, chunk_overlap=128
    )
    chunks = chunker.chunk(sample_text)
    assert all([chunk.token_count > 0 for chunk in chunks]), (
        "All chunks must have a positive token count"
    )
    assert all([chunk.token_count <= 512 for chunk in chunks]), (
        "All chunks must have a token count less than or equal to 512"
    )

    token_counts = [len(tiktokenizer.encode(chunk.text)) for chunk in chunks]
    assert all([
        chunk.token_count == token_count
        for chunk, token_count in zip(chunks, token_counts)
    ]), (
        "All chunks must have a token count equal to the length of the encoded text"
    )


def test_token_chunker_indices_batch(tiktokenizer, sample_text):
    """Test that TokenChunker's indices correctly map to original text."""
    chunker = TokenChunker(
        tokenizer=tiktokenizer, chunk_size=512, chunk_overlap=128
    )
    chunks = chunker.chunk_batch([sample_text] * 10)[-1]
    verify_chunk_indices(chunks, sample_text)


def test_token_chunker_return_type(tiktokenizer, sample_text):
    """Test that TokenChunker's return type is correctly set."""
    chunker = TokenChunker(
        tokenizer=tiktokenizer,
        chunk_size=512,
        chunk_overlap=128,
        return_type="texts",
    )
    chunks = chunker.chunk(sample_text)
    assert all([type(chunk) is str for chunk in chunks])
    assert all([len(tiktokenizer.encode(chunk)) <= 512 for chunk in chunks])
```

## File: `tests/cloud/test_cloud_recursive_chunker.py`
```python
"""Test the Chonkie Cloud Recursive Chunker."""

import os

import pytest

from chonkie.cloud import RecursiveChunker
from chonkie.types import RecursiveRules


@pytest.mark.skipif(
    "CHONKIE_API_KEY" not in os.environ,
    reason="CHONKIE_API_KEY is not set",
)
def test_cloud_recursive_chunker_initialization() -> None:
    """Test that the recursive chunker can be initialized."""
    # Check if the chunk_size < 0 raises an error
    with pytest.raises(ValueError):
        RecursiveChunker(tokenizer_or_token_counter="gpt2", chunk_size=-1)

    # Check if the min_characters_per_chunk < 1 raises an error
    with pytest.raises(ValueError):
        RecursiveChunker(tokenizer_or_token_counter="gpt2", chunk_size=512, min_characters_per_chunk=-1)

    # Check if the return_type is not "texts" or "chunks" raises an error
    with pytest.raises(ValueError):
        RecursiveChunker(tokenizer_or_token_counter="gpt2", chunk_size=512, return_type="not_a_string")
    
    # Finally, check if the attributes are set correctly
    chunker = RecursiveChunker(tokenizer_or_token_counter="gpt2", chunk_size=512)
    assert chunker.tokenizer_or_token_counter == "gpt2"
    assert chunker.chunk_size == 512
    assert chunker.min_characters_per_chunk == 12
    assert chunker.return_type == "chunks"
    assert isinstance(chunker.rules, RecursiveRules)

@pytest.mark.skipif(
    "CHONKIE_API_KEY" not in os.environ,
    reason="CHONKIE_API_KEY is not set",
)
def test_cloud_recursive_chunker_single_sentence() -> None:
    """Test that the Recursive Chunker works with a single sentence."""
    recursive_chunker = RecursiveChunker(
        tokenizer_or_token_counter="gpt2",
        chunk_size=512,
    )

    result = recursive_chunker("Hello, world!")
    assert len(result) == 1
    assert result[0]["text"] == "Hello, world!"
    assert result[0]["token_count"] == 4
    assert result[0]["start_index"] == 0
    assert result[0]["end_index"] == 13


@pytest.mark.skipif(
    "CHONKIE_API_KEY" not in os.environ,
    reason="CHONKIE_API_KEY is not set",
)
def test_cloud_recursive_chunker_batch() -> None:
    """Test that the Recursive Chunker works with a batch of texts."""
    recursive_chunker = RecursiveChunker(
        tokenizer_or_token_counter="gpt2",
        chunk_size=512,
    )

    result = recursive_chunker(["Hello, world!", "This is another sentence.", "This is a third sentence."])
    assert len(result) == 3
    assert result[0][0]["text"] == "Hello, world!"
    assert result[0][0]["token_count"] == 4
    assert result[0][0]["start_index"] == 0
    assert result[0][0]["end_index"] == 13


@pytest.mark.skipif(
    "CHONKIE_API_KEY" not in os.environ,
    reason="CHONKIE_API_KEY is not set",
)
def test_cloud_recursive_chunker_empty_text() -> None:
    """Test that the Recursive Chunker works with an empty text."""
    recursive_chunker = RecursiveChunker(
        tokenizer_or_token_counter="gpt2",
        chunk_size=512,
    )

    result = recursive_chunker("")
    assert len(result) == 0
```

## File: `tests/cloud/test_cloud_semantic_chunker.py`
```python
"""Test the Chonkie Cloud Semantic Chunker."""

import os

import pytest

from chonkie.cloud import SemanticChunker


@pytest.mark.skipif(
    "CHONKIE_API_KEY" not in os.environ,
    reason="CHONKIE_API_KEY is not set",
)
def test_cloud_semantic_chunker_initialization() -> None:
    """Test that the semantic chunker can be initialized."""
    # Check if the chunk_size < 0 raises an error
    with pytest.raises(ValueError):
        SemanticChunker(chunk_size=-1)

    # Check if the threshold is a str but not "auto"
    with pytest.raises(ValueError):
        SemanticChunker(threshold="not_auto")

    # Check if the threshold is a number but not between 0 and 1
    with pytest.raises(ValueError):
        SemanticChunker(threshold=1.1)

    # Check if the threshold is a number but not between 0 and 1
    with pytest.raises(ValueError):
        SemanticChunker(threshold=-0.1)
    
    # Check if the similarity window is not a positive integer
    with pytest.raises(ValueError):
        SemanticChunker(similarity_window=-1)

    # Check if the min_sentences is not a positive integer
    with pytest.raises(ValueError):
        SemanticChunker(min_sentences=-1)

    # Check if the min_chunk_size is not a positive integer
    with pytest.raises(ValueError):
        SemanticChunker(min_chunk_size=-1)

    # Check if the min_characters_per_sentence is not a positive integer
    with pytest.raises(ValueError):
        SemanticChunker(min_characters_per_sentence=-1)

    # Check if the threshold_step is not a number between 0 and 1
    with pytest.raises(ValueError):
        SemanticChunker(threshold_step=-0.1)

    # Check if the threshold_step is not a number between 0 and 1
    with pytest.raises(ValueError):
        SemanticChunker(threshold_step=1.1)

    # Check if the delim is not a string or a list of strings
    with pytest.raises(ValueError):
        SemanticChunker(delim=1)

    # Check if the include_delim is not a string or a list of strings
    with pytest.raises(ValueError):
        SemanticChunker(include_delim=1)

    # Check if the return_type is not "chunks" or "texts"
    with pytest.raises(ValueError):
        SemanticChunker(return_type="not_a_string")

    # Finally, check if the attributes are set correctly
    chunker = SemanticChunker(chunk_size=512)
    assert chunker.embedding_model == "minishlab/potion-base-32M"
    assert chunker.chunk_size == 512
    assert chunker.threshold == "auto"
    assert chunker.similarity_window == 1
    assert chunker.min_sentences == 1
    assert chunker.min_chunk_size == 2
    assert chunker.min_characters_per_sentence == 12
    assert chunker.threshold_step == 0.01
    assert chunker.delim == [".", "!", "?", "\n"]
    assert chunker.include_delim == "prev"
    assert chunker.return_type == "chunks"

@pytest.mark.skipif(
    "CHONKIE_API_KEY" not in os.environ,
    reason="CHONKIE_API_KEY is not set",
)
def test_cloud_semantic_chunker_single_sentence() -> None:
    """Test that the Semantic Chunker works with a single sentence."""
    semantic_chunker = SemanticChunker(
        chunk_size=512,
    )

    result = semantic_chunker("Hello, world!")
    assert len(result) == 1
    assert result[0]["text"] == "Hello, world!"
    assert result[0]["token_count"] == 4
    assert result[0]["start_index"] == 0
    assert result[0]["end_index"] == 13


@pytest.mark.skipif(
    "CHONKIE_API_KEY" not in os.environ,
    reason="CHONKIE_API_KEY is not set",
)
def test_cloud_semantic_chunker_batch() -> None:
    """Test that the Semantic Chunker works with a batch of texts."""
    semantic_chunker = SemanticChunker(
        chunk_size=512,
    )
    result = semantic_chunker(["Hello, world!", "This is another sentence.", "This is a third sentence."])
    assert len(result) == 3
    assert result[0][0]["text"] == "Hello, world!"
    assert result[0][0]["token_count"] == 4
    assert result[0][0]["start_index"] == 0
    assert result[0][0]["end_index"] == 13


@pytest.mark.skipif(
    "CHONKIE_API_KEY" not in os.environ,
    reason="CHONKIE_API_KEY is not set",
)
def test_cloud_semantic_chunker_empty_text() -> None:
    """Test that the Semantic Chunker works with an empty text."""
    semantic_chunker = SemanticChunker(
        chunk_size=512,
    )

    result = semantic_chunker("")
    assert len(result) == 0
```

## File: `tests/cloud/test_cloud_sentence_chunker.py`
```python
"""Test for the Chonkie Cloud Sentence Chunker class."""

import os

import pytest

from chonkie.cloud import SentenceChunker


@pytest.mark.skipif(
    "CHONKIE_API_KEY" not in os.environ,
    reason="CHONKIE_API_KEY is not set",
)
def test_cloud_sentence_chunker_initialization() -> None:
    """Test that the sentence chunker can be initialized."""
    # Check if the chunk_size < 0 raises an error
    with pytest.raises(ValueError):
        SentenceChunker(
            tokenizer_or_token_counter="gpt2", chunk_size=-1, chunk_overlap=0
        )

    # Check if the chunk_overlap < 0 raises an error
    with pytest.raises(ValueError):
        SentenceChunker(
            tokenizer_or_token_counter="gpt2", chunk_size=512, chunk_overlap=-1
        )

    # Check if the min_sentences_per_chunk < 1 raises an error
    with pytest.raises(ValueError):
        SentenceChunker(
            tokenizer_or_token_counter="gpt2",
            chunk_size=512,
            chunk_overlap=0,
            min_sentences_per_chunk=-1,
        )

    # Check if the min_characters_per_sentence < 1 raises an error
    with pytest.raises(ValueError):
        SentenceChunker(
            tokenizer_or_token_counter="gpt2",
            chunk_size=512,
            chunk_overlap=0,
            min_characters_per_sentence=-1,
        )

    # Check if the approximate is not a boolean
    with pytest.raises(ValueError):
        SentenceChunker(
            tokenizer_or_token_counter="gpt2",
            chunk_size=512,
            chunk_overlap=0,
            approximate="not_a_boolean",
        )

    # Check if the include_delim is not a string
    with pytest.raises(ValueError):
        SentenceChunker(
            tokenizer_or_token_counter="gpt2",
            chunk_size=512,
            chunk_overlap=0,
            include_delim="not_a_string",
        )

    # Check if the return_type is not a string
    with pytest.raises(ValueError):
        SentenceChunker(
            tokenizer_or_token_counter="gpt2",
            chunk_size=512,
            chunk_overlap=0,
            return_type="not_a_string",
        )

    # Finally, check if the attributes are set correctly
    chunker = SentenceChunker(
        tokenizer_or_token_counter="gpt2", chunk_size=512, chunk_overlap=0
    )
    assert chunker.tokenizer_or_token_counter == "gpt2"
    assert chunker.chunk_size == 512
    assert chunker.chunk_overlap == 0
    assert chunker.min_sentences_per_chunk == 1
    assert chunker.min_characters_per_sentence == 12
    assert chunker.approximate == True
    assert chunker.delim == [".", "!", "?", "\n"]
    assert chunker.include_delim == "prev"
    assert chunker.return_type == "chunks"


@pytest.mark.skipif(
    "CHONKIE_API_KEY" not in os.environ,
    reason="CHONKIE_API_KEY is not set",
)
def test_cloud_sentence_chunker_simple() -> None:
    """Test that the sentence chunker works."""
    sentence_chunker = SentenceChunker(
        tokenizer_or_token_counter="gpt2",
        chunk_size=512,
        chunk_overlap=0,
    )
    result = sentence_chunker("Hello, world!")

    # Check the result
    assert isinstance(result, list) and isinstance(result[0], dict) and len(result) == 1
    assert result[0]["text"] == "Hello, world!"
    assert result[0]["token_count"] == 4
    assert result[0]["start_index"] == 0
    assert result[0]["end_index"] == 13


@pytest.mark.skipif(
    "CHONKIE_API_KEY" not in os.environ,
    reason="CHONKIE_API_KEY is not set",
)
def test_cloud_sentence_chunker_multiple_sentences() -> None:
    """Test that the sentence chunker works with a complex text."""
    sentence_chunker = SentenceChunker(
        tokenizer_or_token_counter="gpt2",
        chunk_size=5,
        chunk_overlap=0,
    )
    text = "This is one sentence. This is another sentence. This is a third sentence."
    result = sentence_chunker(text)

    # Check the result
    assert len(result) > 1
    assert isinstance(result, list)
    assert all(isinstance(item, dict) for item in result)
    assert all(isinstance(item["text"], str) for item in result)
    assert all(isinstance(item["token_count"], int) for item in result)
    assert all(isinstance(item["start_index"], int) for item in result)
    assert all(isinstance(item["end_index"], int) for item in result)


@pytest.mark.skipif(
    "CHONKIE_API_KEY" not in os.environ,
    reason="CHONKIE_API_KEY is not set",
)
def test_cloud_sentence_chunker_batch() -> None:
    """Test that the sentence chunker works with a batch of texts."""
    sentence_chunker = SentenceChunker(
        tokenizer_or_token_counter="gpt2",
        chunk_size=512,
        chunk_overlap=0,
    )
    texts = ["Hello, world!", "This is another sentence.", "This is a third sentence."]
    result = sentence_chunker(texts)

    # Check the result
    assert len(result) == len(texts)
    assert isinstance(result, list)
    assert all(isinstance(item, list) for item in result)
    assert all(isinstance(item, dict) for item in result[0])
    assert all(isinstance(item["text"], str) for item in result[0])
    assert all(isinstance(item["token_count"], int) for item in result[0])
    assert all(isinstance(item["start_index"], int) for item in result[0])
```

## File: `tests/cloud/test_cloud_token_chunker.py`
```python
"""Test for the Chonkie Cloud Token Chunker class."""

import os

import pytest

from chonkie.cloud import TokenChunker


@pytest.mark.skipif(
    "CHONKIE_API_KEY" not in os.environ,
    reason="CHONKIE_API_KEY is not set",
)
def test_cloud_token_chunker_initialization() -> None:
    """Test that the token chunker can be initialized."""
    # Check if the chunk_size < 0 raises an error
    with pytest.raises(ValueError):
        TokenChunker(tokenizer="gpt2", chunk_size=-1, chunk_overlap=0)

    # Check if the chunk_overlap < 0 raises an error
    with pytest.raises(ValueError):
        TokenChunker(tokenizer="gpt2", chunk_size=512, chunk_overlap=-1)
    
    # Check if the return_type is not "texts" or "chunks" raises an error
    with pytest.raises(ValueError):
        TokenChunker(tokenizer="gpt2", chunk_size=512, chunk_overlap=0, return_type="bad_return_type")

    # Finally, check if the attributes are set correctly
    chunker = TokenChunker(tokenizer="gpt2", chunk_size=512, chunk_overlap=0)
    assert chunker.tokenizer == "gpt2"
    assert chunker.chunk_size == 512
    assert chunker.chunk_overlap == 0
    assert chunker.return_type == "chunks"

@pytest.mark.skipif(
    "CHONKIE_API_KEY" not in os.environ,
    reason="CHONKIE_API_KEY is not set",
)
def test_cloud_token_chunker_simple() -> None:
    """Test that the token chunker works."""
    token_chunker = TokenChunker(
        tokenizer="gpt2",
        chunk_size=512,
        chunk_overlap=0,
    )
    result = token_chunker("Hello, world!")

    # Check the result
    assert isinstance(result, list) and isinstance(result[0], dict) and len(result) == 1
    assert result[0]["text"] == "Hello, world!"
    assert result[0]["token_count"] == 4
    assert result[0]["start_index"] == 0
    assert result[0]["end_index"] == 13

@pytest.mark.skipif(
    "CHONKIE_API_KEY" not in os.environ,
    reason="CHONKIE_API_KEY is not set",
)
def test_cloud_token_chunker_multiple_sentences() -> None:
    """Test that the token chunker works with a complex text."""
    token_chunker = TokenChunker(
        tokenizer="gpt2",
        chunk_size=5,
        chunk_overlap=0,
    )
    text = "This is one sentence. This is another sentence. This is a third sentence."
    result = token_chunker(text)

    # Check the result
    assert len(result) > 1
    assert isinstance(result, list)
    assert all(isinstance(item, dict) for item in result)
    assert all(isinstance(item["text"], str) for item in result)
    assert all(isinstance(item["token_count"], int) for item in result)
    assert all(isinstance(item["start_index"], int) for item in result)
    assert all(isinstance(item["end_index"], int) for item in result)

@pytest.mark.skipif(
    "CHONKIE_API_KEY" not in os.environ,
    reason="CHONKIE_API_KEY is not set",
)
def test_cloud_token_chunker_batch() -> None:
    """Test that the token chunker works with a batch of texts."""
    token_chunker = TokenChunker(
        tokenizer="gpt2",
        chunk_size=512,
        chunk_overlap=0,
    )
    texts = ["Hello, world!", "This is another sentence.", "This is a third sentence."]
    result = token_chunker(texts)

    # Check the result
    assert len(result) == len(texts)
    assert isinstance(result, list)
    assert all(isinstance(item, list) for item in result), \
        f"Expected a list of lists, got {type(result)}"
    assert all(isinstance(item, dict) for item in result[0]), \
        f"Expected a list of dictionaries, got {type(result[0])}"
    assert all(isinstance(item["text"], str) for item in result[0]), \
        f"Expected a list of dictionaries with a 'text' key, got {type(result[0])}"
    assert all(isinstance(item["token_count"], int) for item in result[0]), \
        f"Expected a list of dictionaries with a 'token_count' key, got {type(result[0])}"
    assert all(isinstance(item["start_index"], int) for item in result[0]), \
        f"Expected a list of dictionaries with a 'start_index' key, got {type(result[0])}"
    assert all(isinstance(item["end_index"], int) for item in result[0]), \
        f"Expected a list of dictionaries with a 'end_index' key, got {type(result[0])}"


@pytest.mark.skipif(
    "CHONKIE_API_KEY" not in os.environ,
    reason="CHONKIE_API_KEY is not set",
)
def test_cloud_token_chunker_return_type() -> None:
    """Test that the token chunker works with a return type."""
    token_chunker = TokenChunker(
        tokenizer="gpt2",
        chunk_size=512,
        chunk_overlap=0,
        return_type="texts",
    )
    result = token_chunker("Hello, world!")

    # Check the result
    assert isinstance(result, list)
    assert all(isinstance(item, str) for item in result)
```

## File: `tests/embeddings/test_auto_embeddings.py`
```python
"""Tests for the AutoEmbeddings class."""

import pytest

from chonkie import AutoEmbeddings
from chonkie.embeddings.cohere import CohereEmbeddings
from chonkie.embeddings.model2vec import Model2VecEmbeddings
from chonkie.embeddings.openai import OpenAIEmbeddings
from chonkie.embeddings.sentence_transformer import SentenceTransformerEmbeddings


@pytest.fixture
def model2vec_identifier() -> str:
    """Fixture providing a model2vec identifier."""
    return "minishlab/potion-base-8M"


@pytest.fixture
def sentence_transformer_identifier() -> str:
    """Fixture providing a sentence transformer identifier."""
    return "all-MiniLM-L6-v2"


@pytest.fixture
def sentence_transformer_identifier_small() -> str:
    """Fixture providing a small sentence transformer identifier."""
    return "all-minilm-l6-v2"


@pytest.fixture
def openai_identifier() -> str:
    """Fixture providing an OpenAI identifier."""
    return "text-embedding-3-small"


@pytest.fixture
def cohere_identifier() -> str:
    """Fixture providing an Cohere identifier."""
    return "embed-english-light-v3.0"


@pytest.fixture
def invalid_identifier() -> str:
    """Fixture providing an invalid identifier."""
    return "invalid-identifier-123"


def test_auto_embeddings_model2vec(model2vec_identifier: str) -> None:
    """Test that the AutoEmbeddings class can get model2vec embeddings."""
    embeddings = AutoEmbeddings.get_embeddings(model2vec_identifier)
    assert isinstance(embeddings, Model2VecEmbeddings)
    assert embeddings.model_name_or_path == model2vec_identifier


def test_auto_embeddings_sentence_transformer(sentence_transformer_identifier: str) -> None:
    """Test that the AutoEmbeddings class can get sentence transformer embeddings."""
    embeddings = AutoEmbeddings.get_embeddings(sentence_transformer_identifier)
    assert isinstance(embeddings, SentenceTransformerEmbeddings)
    assert embeddings.model_name_or_path == sentence_transformer_identifier


def test_auto_embeddings_sentence_transformer_alt(
    sentence_transformer_identifier_small: str,
) -> None:
    """Test that the AutoEmbeddings class can get a small sentence transformer embeddings."""
    embeddings = AutoEmbeddings.get_embeddings(sentence_transformer_identifier_small)
    assert isinstance(embeddings, SentenceTransformerEmbeddings)
    assert embeddings.model_name_or_path == sentence_transformer_identifier_small


def test_auto_embeddings_openai(openai_identifier: str) -> None:
    """Test that the AutoEmbeddings class can get OpenAI embeddings."""
    embeddings = AutoEmbeddings.get_embeddings(
        openai_identifier, api_key="your_openai_api_key"
    )
    assert isinstance(embeddings, OpenAIEmbeddings)
    assert embeddings.model == openai_identifier


def test_auto_embeddings_cohere(cohere_identifier: str) -> None:
    """Test that the AutoEmbeddings class can get Cohere embeddings."""
    embeddings = AutoEmbeddings.get_embeddings(
        cohere_identifier, api_key="your_cohere_api_key"
    )
    assert isinstance(embeddings, CohereEmbeddings)
    assert embeddings.model == cohere_identifier


def test_auto_embeddings_invalid_identifier(invalid_identifier: str) -> None:
    """Test that the AutoEmbeddings class raises an error for an invalid identifier."""
    with pytest.raises(ValueError):
        AutoEmbeddings.get_embeddings(invalid_identifier)


if __name__ == "__main__":
    pytest.main()
```

## File: `tests/embeddings/test_cohere_embeddings.py`
```python
"""Test Cohere embeddings."""

import os
from importlib.util import find_spec
from typing import List

import numpy as np
import pytest

from chonkie.embeddings.cohere import CohereEmbeddings


@pytest.fixture
def embedding_model() -> CohereEmbeddings:
    """Fixture to create a CohereEmbeddings instance."""
    api_key = os.environ.get("COHERE_API_KEY")
    return CohereEmbeddings(model="embed-english-light-v3.0", api_key=api_key)


@pytest.fixture
def sample_text() -> str:
    """Fixture to create a sample text."""
    return "This is a sample text for testing."


@pytest.fixture
def sample_texts() -> List[str]:
    """Fixture to create a list of sample texts."""
    return [
        "This is the first sample text.",
        "Here is another example sentence.",
        "Testing embeddings with multiple sentences.",
    ]


@pytest.mark.skipif(
    "COHERE_API_KEY" not in os.environ,
    reason="Skipping test because COHERE_API_KEY is not defined",
)
def test_initialization_with_model_name() -> None:
    """Test initialization with model name."""
    embeddings = CohereEmbeddings(model="embed-english-light-v3.0")
    assert embeddings.model == "embed-english-light-v3.0"
    assert embeddings.client is not None


@pytest.mark.skipif(
    "COHERE_API_KEY" not in os.environ,
    reason="Skipping test because COHERE_API_KEY is not defined",
)
def test_embed_single_text(embedding_model: CohereEmbeddings, sample_text: str) -> None:
    """Test embedding a single text."""
    embedding = embedding_model.embed(sample_text)
    assert isinstance(embedding, np.ndarray)
    assert embedding.shape == (embedding_model.dimension,)


@pytest.mark.skipif(
    "COHERE_API_KEY" not in os.environ,
    reason="Skipping test because COHERE_API_KEY is not defined",
)
def test_embed_batch_texts(embedding_model: CohereEmbeddings, sample_texts: List[str]) -> None:
    """Test embedding a batch of texts."""
    embeddings = embedding_model.embed_batch(sample_texts)
    assert isinstance(embeddings, list)
    assert len(embeddings) == len(sample_texts)
    assert all(isinstance(embedding, np.ndarray) for embedding in embeddings)
    assert all(
        embedding.shape == (embedding_model.dimension,) for embedding in embeddings
    )


@pytest.mark.skipif(
    "COHERE_API_KEY" not in os.environ,
    reason="Skipping test because COHERE_API_KEY is not defined",
)
def test_count_tokens_single_text(embedding_model: CohereEmbeddings, sample_text: str) -> None:
    """Test counting tokens for a single text."""
    token_count = embedding_model.count_tokens(sample_text)
    assert isinstance(token_count, int)
    assert token_count > 0


@pytest.mark.skipif(
    "COHERE_API_KEY" not in os.environ,
    reason="Skipping test because COHERE_API_KEY is not defined",
)
def test_count_tokens_batch_texts(embedding_model: CohereEmbeddings, sample_texts: List[str]) -> None:
    """Test counting tokens for a batch of texts."""
    token_counts = embedding_model.count_tokens_batch(sample_texts)
    assert isinstance(token_counts, list)
    assert len(token_counts) == len(sample_texts)
    assert all(isinstance(count, int) for count in token_counts)
    assert all(count > 0 for count in token_counts)


@pytest.mark.skipif(
    "COHERE_API_KEY" not in os.environ,
    reason="Skipping test because COHERE_API_KEY is not defined",
)
def test_similarity(embedding_model: CohereEmbeddings, sample_texts: List[str]) -> None:
    """Test similarity between two embeddings."""
    embeddings = embedding_model.embed_batch(sample_texts)
    similarity_score = embedding_model.similarity(embeddings[0], embeddings[1])
    assert isinstance(similarity_score, np.float32)
    assert 0.0 <= similarity_score <= 1.0


@pytest.mark.skipif(
    "COHERE_API_KEY" not in os.environ,
    reason="Skipping test because COHERE_API_KEY is not defined",
)
def test_dimension_property(embedding_model: CohereEmbeddings) -> None:
    """Test dimension property."""
    assert isinstance(embedding_model.dimension, int)
    assert embedding_model.dimension > 0


def test_is_available() -> None:
    """Test is_available method."""
    if find_spec("cohere") is not None:
        assert CohereEmbeddings.is_available() is True
    else:
        assert CohereEmbeddings.is_available() is False


@pytest.mark.skipif(
    "COHERE_API_KEY" not in os.environ,
    reason="Skipping test because COHERE_API_KEY is not defined",
)
def test_repr(embedding_model: CohereEmbeddings) -> None:
    """Test repr method."""
    repr_str = repr(embedding_model)
    assert isinstance(repr_str, str)
    assert repr_str.startswith("CohereEmbeddings")


if __name__ == "__main__":
    pytest.main()
```

## File: `tests/embeddings/test_custom_embeddings.py`
```python
"""Contains test cases for the CustomEmbeddings class.

The tests verify:

- Initialization with a specified dimension
- Embedding a single text string
- Embedding a batch of text strings
- Token counting
- Similarity calculation
"""

import numpy as np
import pytest

from chonkie.embeddings.base import BaseEmbeddings


class CustomEmbeddings(BaseEmbeddings):

    """Custom embeddings class."""

    def __init__(self, dimension: int = 4) -> None:
        """Initialize the CustomEmbeddings class."""
        super().__init__()
        self._dimension = dimension

    def embed(self, text: str) -> "np.ndarray":
        """Embed a single text string into a vector representation."""
        # For demonstration, returns a random vector
        return np.random.rand(self._dimension)

    def count_tokens(self, text: str) -> int:
        """Count the number of tokens in a text string."""
        # Very naive token counting—split by whitespace
        return len(text.split())

    def similarity(self, u: "np.ndarray", v: "np.ndarray") -> float:
        """Calculate the cosine similarity between two vectors."""
        return float(np.dot(u, v) / (np.linalg.norm(u) * np.linalg.norm(v)))

    @property
    def dimension(self) -> int:
        """Return the dimension of the embeddings."""
        return self._dimension


def test_custom_embeddings_initialization() -> None:
    """Test the initialization of the CustomEmbeddings class."""
    embeddings = CustomEmbeddings(dimension=4)
    assert isinstance(embeddings, BaseEmbeddings)
    assert embeddings.dimension == 4


def test_custom_embeddings_single_text() -> None:
    """Test the embedding of a single text string."""
    embeddings = CustomEmbeddings(dimension=4)
    text = "Test string"
    vector = embeddings.embed(text)
    assert isinstance(vector, np.ndarray)
    assert vector.shape == (4,)


def test_custom_embeddings_batch_text() -> None:
    """Test the embedding of a batch of text strings."""
    embeddings = CustomEmbeddings(dimension=4)
    texts = ["Test string one", "Test string two"]
    vectors = embeddings.embed_batch(texts)
    assert len(vectors) == 2
    for vec in vectors:
        assert isinstance(vec, np.ndarray)
        assert vec.shape == (4,)


def test_custom_embeddings_token_count() -> None:
    """Test the token counting functionality."""
    embeddings = CustomEmbeddings()
    text = "Test string for counting tokens"
    count = embeddings.count_tokens(text)
    assert isinstance(count, int)
    assert count == len(text.split())


def test_custom_embeddings_similarity() -> None:
    """Test the similarity calculation."""
    embeddings = CustomEmbeddings(dimension=4)
    vec1 = embeddings.embed("Text A")
    vec2 = embeddings.embed("Text B")
    sim = embeddings.similarity(vec1, vec2)
    # Cosine similarity is in [-1, 1]—random vectors often produce a small positive or negative value
    assert -1.0 <= sim <= 1.0


if __name__ == "__main__":
    pytest.main()
```

## File: `tests/embeddings/test_model2vec_embeddings.py`
```python
"""Test the Model2VecEmbeddings class."""

from typing import List

import numpy as np
import pytest
from model2vec import StaticModel

from chonkie import Model2VecEmbeddings


@pytest.fixture
def embedding_model() -> Model2VecEmbeddings:
    """Return a Model2VecEmbeddings instance."""
    return Model2VecEmbeddings("minishlab/potion-base-8M")


@pytest.fixture
def sample_text() -> str:
    """Return a sample text for testing."""
    return "This is a sample text for testing."


@pytest.fixture
def sample_texts() -> List[str]:
    """Return a list of sample texts for testing."""
    return [
        "This is the first sample text.",
        "Here is another example sentence.",
        "Testing embeddings with multiple sentences.",
    ]


def test_initialization_with_model_name(embedding_model: Model2VecEmbeddings) -> None:
    """Test that the Model2VecEmbeddings instance is initialized correctly with a model name."""
    assert embedding_model.model_name_or_path == "minishlab/potion-base-8M"
    assert embedding_model.model is not None


def test_initialization_with_model_instance(embedding_model: Model2VecEmbeddings) -> None:
    """Test that the Model2VecEmbeddings instance is initialized correctly with a model instance."""
    model = StaticModel.from_pretrained("minishlab/potion-base-8M")
    embeddings = Model2VecEmbeddings(model)
    assert embeddings.model_name_or_path == model.base_model_name
    assert embeddings.model is model


def test_embed_single_text(embedding_model: Model2VecEmbeddings, sample_text: str) -> None:
    """Test that the embed method returns a numpy array of the correct shape."""
    embedding = embedding_model.embed(sample_text)
    assert isinstance(embedding, np.ndarray)
    assert embedding.shape == (embedding_model.dimension,)


def test_count_tokens_batch_texts(embedding_model: Model2VecEmbeddings, sample_texts: List[str]) -> None:
    """Test that the count_tokens_batch method returns a list of token counts."""
    token_counts = embedding_model.count_tokens_batch(sample_texts)
    assert isinstance(token_counts, list)
    assert len(token_counts) == len(sample_texts)
    assert all(isinstance(count, int) for count in token_counts)
    assert all(count > 0 for count in token_counts)


def test_similarity(embedding_model: Model2VecEmbeddings, sample_texts: List[str]) -> None:
    """Test that the similarity method returns a float between 0 and 1."""
    embeddings = embedding_model.embed_batch(sample_texts)
    similarity_score = embedding_model.similarity(embeddings[0], embeddings[1])
    assert isinstance(similarity_score, np.float32), (
        f"Similarity score is not a float: {type(similarity_score)}"
    )
    assert 0.0 <= similarity_score <= 1.0, (
        f"Similarity score is not between 0 and 1: {similarity_score}"
    )


def test_dimension_property(embedding_model: Model2VecEmbeddings) -> None:
    """Test that the dimension property returns an integer greater than 0."""
    assert isinstance(embedding_model.dimension, int), (
        f"Dimension is not an integer: {type(embedding_model.dimension)}"
    )
    assert embedding_model.dimension > 0, (
        f"Dimension is not greater than 0: {embedding_model.dimension}"
    )


def test_is_available() -> None:
    """Test that the is_available method returns True."""
    assert Model2VecEmbeddings.is_available() is True


def test_repr(embedding_model: Model2VecEmbeddings) -> None:
    """Test that the repr method returns a string starting with 'Model2VecEmbeddings'."""
    repr_str = repr(embedding_model)
    assert isinstance(repr_str, str), f"repr_str is not a string: {type(repr_str)}"
    assert repr_str.startswith("Model2VecEmbeddings"), (
        f"repr_str does not start with 'Model2VecEmbeddings': {repr_str}"
    )


if __name__ == "__main__":
    pytest.main()
```

## File: `tests/embeddings/test_openai_embeddings.py`
```python
"""Test suite for OpenAIEmbeddings."""

import os
from typing import List

import numpy as np
import pytest

from chonkie.embeddings.openai import OpenAIEmbeddings


@pytest.fixture
def embedding_model() -> OpenAIEmbeddings:
    """Fixture to create an OpenAIEmbeddings instance."""
    api_key = os.environ.get("OPENAI_API_KEY")
    return OpenAIEmbeddings(model="text-embedding-3-small", api_key=api_key)


@pytest.fixture
def sample_text() -> str:
    """Fixture to create a sample text for testing."""
    return "This is a sample text for testing."


@pytest.fixture
def sample_texts() -> List[str]:
    """Fixture to create a list of sample texts for testing."""
    return [
        "This is the first sample text.",
        "Here is another example sentence.",
        "Testing embeddings with multiple sentences.",
    ]


@pytest.mark.skipif(
    "OPENAI_API_KEY" not in os.environ,
    reason="Skipping test because OPENAI_API_KEY is not defined",
)
def test_initialization_with_model_name(embedding_model: OpenAIEmbeddings) -> None:
    """Test that OpenAIEmbeddings initializes with a model name."""
    assert embedding_model.model == "text-embedding-3-small"
    assert embedding_model.client is not None


@pytest.mark.skipif(
    "OPENAI_API_KEY" not in os.environ,
    reason="Skipping test because OPENAI_API_KEY is not defined",
)
def test_embed_single_text(embedding_model: OpenAIEmbeddings, sample_text: str) -> None:
    """Test that OpenAIEmbeddings correctly embeds a single text."""
    embedding = embedding_model.embed(sample_text)
    assert isinstance(embedding, np.ndarray)
    assert embedding.shape == (embedding_model.dimension,)


@pytest.mark.skipif(
    "OPENAI_API_KEY" not in os.environ,
    reason="Skipping test because OPENAI_API_KEY is not defined",
)
def test_embed_batch_texts(embedding_model: OpenAIEmbeddings, sample_texts: List[str]) -> None:
    """Test that OpenAIEmbeddings correctly embeds a batch of texts."""
    embeddings = embedding_model.embed_batch(sample_texts)
    assert isinstance(embeddings, list)
    assert len(embeddings) == len(sample_texts)
    assert all(isinstance(embedding, np.ndarray) for embedding in embeddings)
    assert all(
        embedding.shape == (embedding_model.dimension,) for embedding in embeddings
    )


@pytest.mark.skipif(
    "OPENAI_API_KEY" not in os.environ,
    reason="Skipping test because OPENAI_API_KEY is not defined",
)
def test_count_tokens_single_text(embedding_model: OpenAIEmbeddings, sample_text: str) -> None:
    """Test that OpenAIEmbeddings correctly counts tokens for a single text."""
    token_count = embedding_model.count_tokens(sample_text)
    assert isinstance(token_count, int)
    assert token_count > 0


@pytest.mark.skipif(
    "OPENAI_API_KEY" not in os.environ,
    reason="Skipping test because OPENAI_API_KEY is not defined",
)
def test_count_tokens_batch_texts(embedding_model: OpenAIEmbeddings, sample_texts: List[str]) -> None:
    """Test that OpenAIEmbeddings correctly counts tokens for a batch of texts."""
    token_counts = embedding_model.count_tokens_batch(sample_texts)
    assert isinstance(token_counts, list)
    assert len(token_counts) == len(sample_texts)
    assert all(isinstance(count, int) for count in token_counts)
    assert all(count > 0 for count in token_counts)


@pytest.mark.skipif(
    "OPENAI_API_KEY" not in os.environ,
    reason="Skipping test because OPENAI_API_KEY is not defined",
)
def test_similarity(embedding_model: OpenAIEmbeddings, sample_texts: List[str]) -> None:
    """Test that OpenAIEmbeddings correctly calculates similarity between two embeddings."""
    embeddings = embedding_model.embed_batch(sample_texts)
    similarity_score = embedding_model.similarity(embeddings[0], embeddings[1])
    assert isinstance(similarity_score, float)
    assert 0.0 <= similarity_score <= 1.0


@pytest.mark.skipif(
    "OPENAI_API_KEY" not in os.environ,
    reason="Skipping test because OPENAI_API_KEY is not defined",
)
def test_dimension_property(embedding_model: OpenAIEmbeddings) -> None:
    """Test that OpenAIEmbeddings correctly calculates the dimension property."""
    assert isinstance(embedding_model.dimension, int)
    assert embedding_model.dimension > 0


@pytest.mark.skipif(
    "OPENAI_API_KEY" not in os.environ,
    reason="Skipping test because OPENAI_API_KEY is not defined",
)
def test_is_available() -> None:
    """Test that OpenAIEmbeddings correctly checks if it is available."""
    assert OpenAIEmbeddings.is_available() is True


@pytest.mark.skipif(
    "OPENAI_API_KEY" not in os.environ,
    reason="Skipping test because OPENAI_API_KEY is not defined",
)
def test_repr(embedding_model: OpenAIEmbeddings) -> None:
    """Test that OpenAIEmbeddings correctly returns a string representation."""
    repr_str = repr(embedding_model)
    assert isinstance(repr_str, str)
    assert repr_str.startswith("OpenAIEmbeddings")


if __name__ == "__main__":
    pytest.main()
```

## File: `tests/embeddings/test_sentence_transformer_embeddings.py`
```python
"""Test the SentenceTransformerEmbeddings class."""

from typing import List

import numpy as np
import pytest
from sentence_transformers import SentenceTransformer

from chonkie.embeddings.sentence_transformer import SentenceTransformerEmbeddings


@pytest.fixture
def embedding_model() -> SentenceTransformerEmbeddings:
    """Return a SentenceTransformerEmbeddings instance."""
    return SentenceTransformerEmbeddings("all-MiniLM-L6-v2")


@pytest.fixture
def sample_text() -> str:
    """Return a sample text for testing."""
    return "This is a sample text for testing."


@pytest.fixture
def sample_texts() -> List[str]:
    """Return a list of sample texts for testing."""
    return [
        "This is the first sample text.",
        "Here is another example sentence.",
        "Testing embeddings with multiple sentences.",
    ]


def test_initialization_with_model_name(embedding_model: SentenceTransformerEmbeddings) -> None:
    """Test the initialization with a model name."""
    assert embedding_model.model_name_or_path == "all-MiniLM-L6-v2"
    assert embedding_model.model is not None


def test_initialization_with_model_instance(embedding_model: SentenceTransformerEmbeddings) -> None:
    """Test the initialization with a model instance."""
    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = SentenceTransformerEmbeddings(model)
    assert embeddings.model_name_or_path == model.model_card_data.base_model
    assert embeddings.model is model


def test_embed_single_text(embedding_model: SentenceTransformerEmbeddings, sample_text: str) -> None:
    """Test the embed method with a single text."""
    embedding = embedding_model.embed(sample_text)
    assert isinstance(embedding, np.ndarray)
    assert embedding.shape == (embedding_model.dimension,)


def test_embed_batch_texts(embedding_model: SentenceTransformerEmbeddings, sample_texts: List[str]) -> None:
    """Test the embed_batch method with a list of texts."""
    embeddings = embedding_model.embed_batch(sample_texts)
    assert isinstance(embeddings, np.ndarray)
    assert len(embeddings) == len(sample_texts)
    assert all(isinstance(embedding, np.ndarray) for embedding in embeddings)
    assert all(
        embedding.shape == (embedding_model.dimension,) for embedding in embeddings
    )


def test_count_tokens_single_text(embedding_model: SentenceTransformerEmbeddings, sample_text: str) -> None:
    """Test the count_tokens method with a single text."""
    token_count = embedding_model.count_tokens(sample_text)
    assert isinstance(token_count, int)
    assert token_count > 0


def test_count_tokens_batch_texts(embedding_model: SentenceTransformerEmbeddings, sample_texts: List[str]) -> None:
    """Test the count_tokens_batch method with a list of texts."""
    token_counts = embedding_model.count_tokens_batch(sample_texts)
    assert isinstance(token_counts, list)
    assert len(token_counts) == len(sample_texts)
    assert all(isinstance(count, int) for count in token_counts)
    assert all(count > 0 for count in token_counts)


def test_similarity(embedding_model: SentenceTransformerEmbeddings, sample_texts: List[str]) -> None:
    """Test the similarity method."""
    embeddings = embedding_model.embed_batch(sample_texts)
    similarity_score = embedding_model.similarity(embeddings[0], embeddings[1])
    assert isinstance(similarity_score, float)
    assert 0.0 <= similarity_score <= 1.0


def test_dimension_property(embedding_model: SentenceTransformerEmbeddings) -> None:
    """Test the dimension property."""
    assert isinstance(embedding_model.dimension, int)
    assert embedding_model.dimension > 0


def test_is_available() -> None:
    """Test the is_available method."""
    assert SentenceTransformerEmbeddings.is_available() is True


def test_repr(embedding_model: SentenceTransformerEmbeddings) -> None:
    """Test the repr method."""
    repr_str = repr(embedding_model)
    assert isinstance(repr_str, str)
    assert repr_str.startswith("SentenceTransformerEmbeddings")


if __name__ == "__main__":
    pytest.main()
```

## File: `tests/types/test_base.py`
```python
"""Tests for Base Types."""

from __future__ import annotations

import pytest

from chonkie import Chunk, Context


def test_context_init():
    """Test Context initialization."""
    context = Context(text="test", token_count=1)
    assert context.text == "test"
    assert context.token_count == 1
    assert context.start_index is None
    assert context.end_index is None


def test_context_raises_error():
    """Test Context raises error for illegal field values."""
    with pytest.raises(ValueError):
        Context(text=9000, token_count=1)

    with pytest.raises(ValueError):
        Context(text="test", token_count=-1, start_index="0")

    with pytest.raises(TypeError):
        Context(text="test", token_count="1")

    with pytest.raises(ValueError):
        Context(text="test", token_count=1, start_index=10, end_index=5)


def test_context_serialization():
    """Test Context serialization/deserialization."""
    context = Context(text="test", token_count=1, start_index=0, end_index=4)
    context_dict = context.to_dict()
    restored = Context.from_dict(context_dict)
    assert context.text == restored.text
    assert context.token_count == restored.token_count
    assert context.start_index == restored.start_index
    assert context.end_index == restored.end_index


# Chunk Tests
def test_chunk_init():
    """Test Chunk initialization."""
    chunk = Chunk(text="test chunk", start_index=0, end_index=10, token_count=2)
    assert chunk.text == "test chunk"
    assert chunk.start_index == 0
    assert chunk.end_index == 10
    assert chunk.token_count == 2
    assert chunk.context is None


def test_chunk_with_context():
    """Test Chunk with context."""
    context = Context(text="context", token_count=1)
    chunk = Chunk(
        text="test chunk",
        start_index=0,
        end_index=10,
        token_count=2,
        context=context,
    )
    assert chunk.context == context


def test_chunk_serialization():
    """Test Chunk serialization/deserialization."""
    context = Context(text="context", token_count=1)
    chunk = Chunk(
        text="test chunk",
        start_index=0,
        end_index=10,
        token_count=2,
        context=context,
    )
    chunk_dict = chunk.to_dict()
    restored = Chunk.from_dict(chunk_dict)
    assert chunk.text == restored.text
    assert chunk.token_count == restored.token_count
    assert chunk.context.text == restored.context.text
```

## File: `tests/types/test_recursive.py`
```python
"""Test recursive types."""

import pytest

from chonkie import RecursiveChunk, RecursiveLevel, RecursiveRules


def test_recursive_level_init():
    """Test RecursiveLevel initialization."""
    level = RecursiveLevel(delimiters=["\n", "."])
    assert level.delimiters == ["\n", "."]
    assert not level.whitespace
    assert level.include_delim == "prev"


def test_recursive_level_raises_error():
    """Test RecursiveLevel validation."""
    with pytest.raises(NotImplementedError):
        RecursiveLevel(whitespace=True, delimiters=["."])

    with pytest.raises(ValueError):
        RecursiveLevel(delimiters=[1, 2])

    with pytest.raises(ValueError):
        RecursiveLevel(delimiters=[""])

    with pytest.raises(ValueError):
        RecursiveLevel(delimiters=[" "])


def test_recursive_level_serialization():
    """Test RecursiveLevel serialization and deserialization."""
    level = RecursiveLevel(delimiters=["\n", "."])
    level_dict = level.to_dict()
    reconstructed = RecursiveLevel.from_dict(level_dict)
    assert reconstructed.delimiters == ["\n", "."]
    assert not reconstructed.whitespace
    assert reconstructed.include_delim == "prev"


# RecursiveRules Tests
def test_recursive_rules_default_init():
    """Test RecursiveRules default initialization."""
    rules = RecursiveRules()
    assert len(rules.levels) == 5
    assert all(isinstance(level, RecursiveLevel) for level in rules.levels)


def test_recursive_rules_custom_init():
    """Test RecursiveRules custom initialization."""
    levels = [
        RecursiveLevel(delimiters=["\n"]),
        RecursiveLevel(delimiters=["."]),
    ]
    rules = RecursiveRules(levels=levels)
    assert len(rules.levels) == 2
    assert rules.levels == levels


def test_recursive_rules_serialization():
    """Test RecursiveRules serialization and deserialization."""
    levels = [
        RecursiveLevel(delimiters=["\n"]),
        RecursiveLevel(delimiters=["."]),
    ]
    rules = RecursiveRules(levels=levels)
    rules_dict = rules.to_dict()
    reconstructed = RecursiveRules.from_dict(rules_dict)
    assert len(reconstructed.levels) == 2
    assert all(
        isinstance(level, RecursiveLevel) for level in reconstructed.levels
    )


# RecursiveChunk Tests
def test_recursive_chunk_init():
    """Test RecursiveChunk initialization."""
    chunk = RecursiveChunk(
        text="test chunk",
        start_index=0,
        end_index=10,
        token_count=2,
        level=1,
    )
    assert chunk.text == "test chunk"
    assert chunk.level == 1


def test_recursive_chunk_serialization():
    """Test RecursiveChunk serialization/deserialization."""
    chunk = RecursiveChunk(
        text="test chunk",
        start_index=0,
        end_index=10,
        token_count=2,
        level=1,
    )
    chunk_dict = chunk.to_dict()
    reconstructed = RecursiveChunk.from_dict(chunk_dict)
    assert reconstructed.level == 1
    assert reconstructed.text == chunk.text
```

## File: `tests/types/test_sentence.py`
```python
"""Unit tests for Sentence and SentenceChunk classes."""

import pytest

from chonkie import Sentence, SentenceChunk


def test_sentence_init():
    """Test Sentence initialization."""
    sentence = Sentence(
        text="Ratatouille is a movie.", start_index=0, end_index=14, token_count=3
    )
    assert sentence.text == "Ratatouille is a movie."
    assert sentence.start_index == 0
    assert sentence.end_index == 14
    assert sentence.token_count == 3


def test_sentence_raises_error():
    """Test Sentence raises error for illegal field values."""
    with pytest.raises(ValueError):
        Sentence(text=9000, start_index=0, end_index=14, token_count=3)

    with pytest.raises(ValueError):
        Sentence(
            text="Ratatouille is a movie.", start_index=-1, end_index=14, token_count=3
        )

    with pytest.raises(ValueError):
        Sentence(
            text="Ratatouille is a movie.", start_index=0, end_index=-1, token_count=3
        )

    with pytest.raises(ValueError):
        Sentence(
            text="Ratatouille is a movie.", start_index=0, end_index=14, token_count=-1
        )

    with pytest.raises(ValueError):
        Sentence(
            text="Ratatouille is a movie.",
            start_index=10,
            end_index=5,
            token_count=3,
        )


def test_sentence_serialization():
    """Test Sentence serialization/deserialization."""
    sentence = Sentence(
        text="Ratatouille is a movie.", start_index=0, end_index=14, token_count=3
    )
    sentence_dict = sentence.to_dict()
    restored = Sentence.from_dict(sentence_dict)
    assert sentence.text == restored.text
    assert sentence.token_count == restored.token_count


def test_sentence_chunk_init():
    """Test SentenceChunk initialization."""
    sentences = [
        Sentence("First sentence.", 0, 14, 3),
        Sentence("Second sentence.", 15, 30, 3),
    ]
    chunk = SentenceChunk(
        text="Wall-E is a Pixar movie. Ratatouille is another one.",
        start_index=0,
        end_index=30,
        token_count=6,
        sentences=sentences,
    )
    assert chunk.text == "Wall-E is a Pixar movie. Ratatouille is another one."
    assert len(chunk.sentences) == 2
    assert all(isinstance(s, Sentence) for s in chunk.sentences)


def test_sentence_chunk_serialization():
    """Test SentenceChunk serialization/deserialization."""
    sentences = [
        Sentence("First sentence.", 0, 14, 3),
        Sentence("Second sentence.", 15, 30, 3),
    ]
    chunk = SentenceChunk(
        text="Wall-E is a Pixar movie. Ratatouille is another one.",
        start_index=0,
        end_index=30,
        token_count=6,
        sentences=sentences,
    )
    chunk_dict = chunk.to_dict()
    restored = SentenceChunk.from_dict(chunk_dict)
    assert len(restored.sentences) == 2
    assert all(isinstance(s, Sentence) for s in restored.sentences)
```

