---
id: thomasbury-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:22.061443
---

# KNOWLEDGE EXTRACT: ThomasBury
> **Extracted on:** 2026-03-30 17:54:17
> **Source:** ThomasBury

---

## File: `pyragify.md`
```markdown
# 📦 ThomasBury/pyragify [🔖 PENDING/APPROVE]
🔗 https://github.com/ThomasBury/pyragify


## Meta
- **Stars:** ⭐ 63 | **Forks:** 🍴 10
- **Language:** Python | **License:** Unlicense
- **Last updated:** 2026-03-21
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Weaving the structure of your repository into meaningful text for NotebookLM integration

## README (trích đầu)
```
# pyragify: Unlock the Power of Your Code with NotebookLM  

**pyragify** is a Python-based tool designed to **transform your Python code repositories into a format that's ready for analysis with large language models (LLMs), specifically NotebookLM.** It breaks down complex code structures into manageable semantic chunks, making it easier to understand, analyze, and extract insights from your code.

## Why pyragify?

* **Boost Code Comprehension:**  pyragify makes it easier to digest large codebases by dividing them into smaller, logical units.
* **Effortless Analysis:** The structured output simplifies the process of analyzing code, identifying patterns, and extracting knowledge.
* **Unlock the Power of NotebookLM:** pyragify prepares your code for use with NotebookLM, allowing you to leverage the power of LLMs for tasks like code summarization, documentation generation, and question answering.

## Key Features

* **Semantic Chunking:** pyragify intelligently extracts functions, classes, and comments from Python files, as well as headers and sections from Markdown files, preserving the context and meaning.
* **Wide Format Support:** It handles Python (.py), Markdown (.md, .markdown), HTML (.html), CSS (.css), and other common file types, ensuring all your repository content is processed.
* **Smart Parsing:** Uses AST for Python files, regex-based parsing for HTML/CSS, and header-based chunking for Markdown files.
* **Seamless Integration with NotebookLM:** The output format is specifically designed for compatibility with NotebookLM, making it easy to analyze your code with powerful LLMs.
* **Flexible Configuration:** Tailor the processing through a YAML file or command-line arguments to fit your specific needs.
* **File Skipping:** Respect your `.gitignore` and `.dockerignore` files, and define custom skip patterns for even more control.
* **Word Limit Control:** Automatically chunks output files based on a configurable word limit to ensure manageable file sizes.
* **Input Validation:** Validates repository paths and provides clear error messages for invalid inputs.

## Getting Started

### Installation

1. **Using uv (Recommended):**

    ```bash
    uv pip install pyragify
    ```

    `uv` is a blazing fast Python package manager that handles virtual environments and dependencies automatically.

2. **Using pip:**

    ```bash
    pip install pyragify
    ```

3. **From Source:**

    ```bash
    git clone https://github.com/ThomasBury/pyragify.git
    cd pyragify
    uv pip install -e .
    ```

### Usage

1. **Best Practice with uv:**

    ```bash
    uv run pyragify --config-file config.yaml
    ```

See below for details about the configuration file.

2. **Direct CLI Execution:**

    ```bash
    python -m pyragify --config-file config.yaml
    ```

#### Arguments and Options

See `pyragify --help` for a full list of options.

* `--config-file`: Path to the YAML configuration file (default: config.yaml).
* `--repo-path`: Override the repo
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

