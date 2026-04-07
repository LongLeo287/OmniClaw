---
id: pyragify
type: knowledge
owner: OA_Triage
---
# pyragify
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
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
* `--repo-path`: Override the repository path.
* `--output-dir`: Override the output directory.
* `--max-words`: Override the maximum words per output file.
* `--max-file-size`: Override the maximum file size (in bytes) to process.
* `--skip-patterns`: Override file patterns to skip.
* `--skip-dirs`: Override directories to skip.
* `--verbose`: Enable detailed logging for debugging.

### Configuration (config.yaml)

```yaml
repo_path: /path/to/repository
output_dir: /path/to/output
max_words: 200000
max_file_size: 10485760 # 10 MB
skip_patterns:
 - "*.log"
 - "*.tmp"
skip_dirs:
 - "__pycache__"
 - "node_modules"
verbose: false
```

## Example Workflow

1. **Prepare Your Repository:** Make sure your repository contains the code you want to process. Utilize `.gitignore` or `.dockerignore` to exclude unwanted files or directories.
2. **Configure pyragify:** Create a `config.yaml` file with your desired settings or use the default configuration.
3. **Process the Repository:** Run pyragify using uv (recommended):

    ```bash
    uv run pyragify --config-file config.yaml
    ```

4. **Check the Output:** Your processed content is neatly organized by file type in the specified output directory.

## Chat with Your Codebase (with NotebookLM)

1. Navigate to NotebookLM.
2. Upload the `chunk_0.txt` file (or other relevant chunks) from the pyragify output directory to a new notebook.
3. Start asking questions and get insights with precise citations! You can even generate a podcast from your code.
    ![code_chat](chat_code_base.png "Chat with your code base")

## Output Structure

The processed content is saved as `.txt` files and categorized into subdirectories based on the file type:

* `python/`:  Contains chunks of Python functions, classes, and their code.
* `markdown/`:  Contains sections of Markdown files split by headers.
* `html/`:  Contains HTML script and style chunks extracted from HTML files.
* `css/`:  Contains CSS rule chunks from CSS files.
* `other/`:  Contains plain-text versions of unsupported file types.

## Advanced Features

* **Input Validation:** Validates repository paths and provides clear error messages for invalid inputs.
* **Respect for Ignore Files:** pyragify automatically honors `.gitignore` and `.dockerignore` patterns.
* **Incremental Processing:** MD5 hashes are used to efficiently skip unchanged files during subsequent runs.

## Contributing

We welcome contributions! To contribute to pyragify:

1. Clone the repository.
2. Install dependencies.
3. Run tests. (Test suite is under development).

## Support

Feel free to create a GitHub issue for any questions, bug reports, or feature requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Example Usages

**Process a Repository with Default Settings:**

```bash
uv run pyragify --config-file config.yaml
```

**Process a Specific Repository with Custom Settings:**

```bash
uv run pyragify \
 --repo-path /my/repo \
 --output-dir /my/output \
 --max-words 100000 \
 --max-file-size 5242880 \
 --skip-patterns "*.log,*.tmp" \
 --skip-dirs "__pycache__,node_modules" \
 --verbose
```

```

### File: config.yaml
```yaml
repo_path: /home/user/project/pyragify/
output_dir: ./output
max_words: 200000
max_file_size: 10485760  # 10 MB
skip_patterns:
 - ".git"
 - "uv.lock"
 - ".gitignore"
skip_dirs: []
verbose: false

```

### File: text2flow_optimized.yaml
```yaml
# Pyragify Config: Optimized for Text2Flow/Visualization.

# Use the current directory as the source for weaving
repo_path: "."

# The folder where the LLM-ready "weaved" text will be saved
output_dir: "./llm_analysis"

# These are the files to ignore so we only push the essential files to the LLM.
skip_patterns:
  - "*.min.js"
  - "*.map"
  - "bundle.js"
  - "*-lock.json"
  - "*.svg"

# Standard heavy folders/files to bypass.
skip_dirs:
  - "node_modules"
  - "dist"
  - "build"
  - "__pycache__"
  - ".git"

# High max_words allows complex flowchart grammars to stay 
# within a single window for better RAG performance.
max_words: 500000

# Required to prevent CLI runtime failure.
max_file_size: 10485760 #10MB

# # Provide essential feedback in the terminal while processing.
verbose: true

```

### File: tests\test_processor.py
```py
import pytest
from pathlib import Path
from pyragify.processor import FileProcessor, compute_file_hash, save_json, load_json, is_documentation_file, read_file_in_chunks

@pytest.fixture
def sample_python_file(tmp_path):
    """Fixture for a sample Python file with function and class."""
    file_path = tmp_path / "sample.py"
    file_path.write_text("""
def test_function(param):
    \"\"\"Docstring for function.\"\"\"
    return param * 2

class TestClass:
    \"\"\"Docstring for class.\"\"\"
    def method(self):
        return "method"
# Comment line
""")
    return file_path

@pytest.fixture
def sample_markdown_file(tmp_path):
    """Fixture for a sample Markdown file with headers."""
    file_path = tmp_path / "sample.md"
    file_path.write_text("""
# Header 1
Content under header 1.

## Header 2
Content under header 2.
""")
    return file_path

@pytest.fixture
def sample_js_file(tmp_path):
    """Fixture for a sample JavaScript file."""
    file_path = tmp_path / "sample.js"
    file_path.write_text("""
function testFunction(param) {
    return param * 2;
}

class TestClass {
    constructor() {}
    method() {
        return 'test';
    }
}

const arrow = (x) => x * 3;
""")
    return file_path

@pytest.fixture
def sample_java_file(tmp_path):
    """Fixture for a sample Java file."""
    file_path = tmp_path / "Sample.java"
    file_path.write_text("""
public class Sample {
    public static void testMethod(String param) {
        return param.length();
    }
}
""")
    return file_path

@pytest.fixture
def sample_cpp_file(tmp_path):
    """Fixture for a sample C++ file."""
    file_path = tmp_path / "sample.cpp"
    file_path.write_text("""
struct TestStruct {
    int x;
};

int testFunction(int param) {
    return param * 2;
}
""")
    return file_path

@pytest.fixture
def sample_html_file(tmp_path):
    """Fixture for a sample HTML file."""
    file_path = tmp_path / "sample.html"
    file_path.write_text("""
<!DOCTYPE html>
<html>
<script>
function jsFunc() { return 'hi'; }
</script>
<style>
body { color: red; }
</style>
</html>
""")
    return file_path

@pytest.fixture
def sample_css_file(tmp_path):
    """Fixture for a sample CSS file."""
    file_path = tmp_path / "sample.css"
    file_path.write_text("""
body {
    color: red;
}

@media screen {
    div { font-size: 12px; }
}
""")
    return file_path

def test_compute_file_hash(sample_python_file):
    """Test file hash computation."""
    hash_value = compute_file_hash(sample_python_file)
    assert isinstance(hash_value, str)
    assert len(hash_value) == 32  # MD5 hex length

def test_save_json_load_json(tmp_path):
    """Test saving and loading JSON."""
    data = {"test": "value"}
    json_path = tmp_path / "test.json"
    save_json(data, json_path, "test data")
    loaded = load_json(json_path, "test data")
    assert loaded == data

def test_is_documentation_file():
    """Test documentation file detection."""
    assert is_documentation_file(Path("README.md")) == True
    assert is_documentation_file(Path("example.py")) == False

def test_read_file_in_chunks(sample_python_file):
    """Test reading file in chunks."""
    chunks = list(read_file_in_chunks(sample_python_file))
    full_content = sample_python_file.read_text()
    assert ''.join(chunks) == full_content

class TestFileProcessor:
    def test_chunk_python_file(self, sample_python_file, tmp_path):
        """Test Python chunking."""
        output_dir = tmp_path / "output"
        processor = FileProcessor(tmp_path, output_dir)
        chunks, line_count = processor.chunk_python_file(sample_python_file)
        assert line_count > 0
        assert len(chunks) >= 3  # Function, class, and comments
        func_chunk = next((c for c in chunks if c["type"] == "function"), None)
        assert func_chunk is not None
        assert "test_function" in func_chunk["name"]
        assert "def test_function" in func_chunk["code"]
        assert func_chunk["docstring"] == "Docstring for function."
        class_chunk = next((c for c in chunks if c["type"] == "class"), None)
        assert class_chunk is not None
        assert "TestClass" in class_chunk["name"]
        assert "class TestClass" in class_chunk["code"]
        assert class_chunk["docstring"] == "Docstring for class."

    def test_chunk_markdown_file(self, sample_markdown_file, tmp_path):
        """Test Markdown chunking."""
        output_dir = tmp_path / "output"
        processor = FileProcessor(tmp_path, output_dir)
        chunks, line_count = processor.chunk_markdown_file(sample_markdown_file)
        assert line_count > 0
        assert len(chunks) == 2  # Two headers
        assert chunks[0]["header"] == "# Header 1"
        assert "Content under header 1" in chunks[0]["content"]

    @pytest.mark.parametrize("file_fixture, suffix, expected_types", [
        ("sample_js_file", ".js", ["file"]),
        ("sample_java_file", ".java", ["file"]),
        ("sample_cpp_file", ".cpp", ["file"]),
        ("sample_html_file", ".html", ["html_script", "html_style"]),
        ("sample_css_file", ".css", ["css_rule"]),
    ])
    def test_chunk_tree_sitter_file_real(self, request, file_fixture, suffix, expected_types, tmp_path):
        """Test tree-sitter chunking for multiple languages with real parsers."""
        file_path = request.getfixturevalue(file_fixture)
        output_dir = tmp_path / "output"
        processor = FileProcessor(tmp_path, output_dir)
        chunks, line_count = processor.chunk_tree_sitter_file(file_path, suffix)
        assert line_count > 0
        assert chunks
        found_types = {c["type"] for c in chunks}
        for expected_type in expected_types:
            assert expected_type in found_types

    def test_chunk_file_routing(self, sample_python_file, sample_markdown_file, sample_js_file, tmp_path):
        """Test chunk_file routes to correct method."""
        output_dir = tmp_path / "output"
        processor = FileProcessor(tmp_path, output_dir)
        py_chunks, _ = processor.chunk_file(sample_python_file)
        assert any(c["type"] == "function" for c in py_chunks)
        md_chunks, _ = processor.chunk_file(sample_markdown_file)
        assert "header" in md_chunks[0]
        js_chunks, _ = processor.chunk_file(sample_js_file)
        assert any(c["type"] == "file" for c in js_chunks)

    def test_format_chunk(self):
        """Test formatting various chunk types."""
        processor = FileProcessor(Path("."), Path("."))
        func_chunk = {"type": "function", "name": "test", "code": "def test(): pass", "docstring": "A test function."}
        formatted = processor.format_chunk(func_chunk)
        assert "Function: test" in formatted
        assert "Docstring:\nA test function." in formatted
        assert "def test(): pass" in formatted
        html_chunk = {"type": "html_script", "content": "<script>alert('hi');</script>"}
        formatted_html = processor.format_chunk(html_chunk)
        assert "HTML Script:" in formatted_html

    def test_chunk_file_unreadable(self, tmp_path, caplog):
        """Test that chunking an unreadable file is handled gracefully."""
        output_dir = tmp_path / "output"
        processor = FileProcessor(tmp_path, output_dir)
        bad_file = tmp_path / "bad.txt"
        bad_file.write_bytes(b'\x80') # Invalid utf-8
        chunks, line_count = processor.chunk_file(bad_file)
        assert chunks == []
        assert line_count == 0
        assert "Error reading file" in caplog.text
```

