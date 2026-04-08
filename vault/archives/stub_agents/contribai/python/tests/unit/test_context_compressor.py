"""Tests for P1: ContextCompressor."""

from __future__ import annotations

from contribai.analysis.context_compressor import CHARS_PER_TOKEN, ContextCompressor


class TestContextCompressor:
    """Tests for ContextCompressor."""

    def test_compress_text_within_budget(self):
        compressor = ContextCompressor(max_context_tokens=1000)
        text = "Hello " * 100  # ~600 chars = ~150 tokens, well within budget
        result = compressor.compress_text(text)
        assert result == text  # no compression needed

    def test_compress_text_over_budget(self):
        compressor = ContextCompressor(max_context_tokens=50)  # 200 chars budget
        text = "A" * 1000
        result = compressor.compress_text(text)
        assert len(result) < len(text)
        assert "omitted" in result

    def test_compress_files_within_budget(self):
        compressor = ContextCompressor(max_context_tokens=10000)
        files = {
            "a.py": "print('hello')",
            "b.py": "x = 1",
        }
        result = compressor.compress_files(files)
        assert len(result) == 2
        assert result["a.py"] == "print('hello')"

    def test_compress_files_over_budget(self):
        compressor = ContextCompressor(max_context_tokens=100)  # ~400 chars total
        files = {f"file_{i}.py": "x" * 200 for i in range(10)}
        result = compressor.compress_files(files)
        # Should have compressed or skipped some files
        total_chars = sum(len(v) for v in result.values())
        assert total_chars <= 100 * CHARS_PER_TOKEN

    def test_truncate_middle_preserves_head_and_tail(self):
        text = "HEAD" + "x" * 1000 + "TAIL"
        result = ContextCompressor._truncate_middle(text, 200)
        assert result.startswith("HEAD")
        assert result.endswith("TAIL")
        assert "omitted" in result

    def test_extract_python_signatures(self):
        code = '''
import os
from pathlib import Path

CONSTANT = 42

class MyClass:
    """Docstring."""

    def method(self):
        x = 1
        y = 2
        return x + y

@decorator
async def async_func():
    pass
'''
        compressor = ContextCompressor()
        result = compressor.extract_signatures(code, "python")
        assert "import os" in result
        assert "from pathlib import Path" in result
        assert "CONSTANT = 42" in result
        assert "class MyClass:" in result
        assert "def method(self):" in result
        assert "@decorator" in result
        assert "async def async_func():" in result
        # Implementation details should be stripped
        assert "x = 1" not in result
        assert "y = 2" not in result

    def test_summarize_findings_compact_empty(self):
        result = ContextCompressor.summarize_findings_compact([])
        assert result == "No issues."

    def test_extract_signatures_non_python(self):
        code = "\n".join([f"line {i}" for i in range(100)])
        compressor = ContextCompressor()
        result = compressor.extract_signatures(code, "javascript")
        assert "omitted" in result
