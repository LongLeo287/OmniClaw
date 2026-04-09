#!/usr/bin/env python3
"""
Document Text Extraction for TTS

Extracts and cleans text from PDF, DOCX, Markdown, and plain text files.
Optimizes output for text-to-speech readability.

Usage:
    python extract.py /path/to/document.pdf
    python extract.py /path/to/document.docx

Dependencies:
    PyPDF2>=3.0.0 (for PDF extraction)
    python-docx>=1.0.0 (for DOCX extraction)
"""

import re
import sys
from pathlib import Path


def extract_pdf(path: Path) -> str:
    """Extract text from a PDF file."""
    try:
        from PyPDF2 import PdfReader
    except ImportError:
        print("Error: PyPDF2 is required for PDF extraction.", file=sys.stderr)
        print("Install it with: pip install 'PyPDF2>=3.0.0'", file=sys.stderr)
        sys.exit(1)

    reader = PdfReader(str(path))
    pages = []
    for page in reader.pages:
        text = page.extract_text()
        if text:
            pages.append(text)

    if not pages:
        print(f"Warning: No text extracted from {path}", file=sys.stderr)
        return ""

    return "\n\n".join(pages)


def extract_docx(path: Path) -> str:
    """Extract text from a DOCX file."""
    try:
        from docx import Document
    except ImportError:
        print("Error: python-docx is required for DOCX extraction.", file=sys.stderr)
        print("Install it with: pip install 'python-docx>=1.0.0'", file=sys.stderr)
        sys.exit(1)

    doc = Document(str(path))
    paragraphs = []
    for para in doc.paragraphs:
        text = para.text.strip()
        if text:
            paragraphs.append(text)

    if not paragraphs:
        print(f"Warning: No text extracted from {path}", file=sys.stderr)
        return ""

    return "\n\n".join(paragraphs)


def extract_markdown(path: Path) -> str:
    """Extract text from a Markdown file."""
    return path.read_text(encoding="utf-8")


def extract_txt(path: Path) -> str:
    """Extract text from a plain text file."""
    return path.read_text(encoding="utf-8")


EXTRACTORS = {
    ".pdf": extract_pdf,
    ".docx": extract_docx,
    ".md": extract_markdown,
    ".markdown": extract_markdown,
    ".txt": extract_txt,
    ".text": extract_txt,
}


def clean_text(text: str) -> str:
    """Clean text for TTS readability.

    Strips URLs, code blocks, excessive whitespace, and other elements
    that don't translate well to spoken audio.
    """
    # Remove code blocks (fenced)
    text = re.sub(r"```[\s\S]*?```", "", text)

    # Remove inline code
    text = re.sub(r"`[^`]+`", "", text)

    # Remove markdown image syntax ![alt](url)
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)

    # Convert markdown links [text](url) to just text
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)

    # Remove bare URLs
    text = re.sub(r"https?://\S+", "", text)

    # Remove HTML tags
    text = re.sub(r"<[^>]+>", "", text)

    # Remove markdown headers (keep the text)
    text = re.sub(r"^#{1,6}\s+", "", text, flags=re.MULTILINE)

    # Remove markdown bold/italic markers
    text = re.sub(r"\*{1,3}([^*]+)\*{1,3}", r"\1", text)
    text = re.sub(r"_{1,3}([^_]+)_{1,3}", r"\1", text)

    # Remove markdown horizontal rules
    text = re.sub(r"^[-*_]{3,}\s*$", "", text, flags=re.MULTILINE)

    # Remove markdown list markers but keep text
    text = re.sub(r"^[\s]*[-*+]\s+", "", text, flags=re.MULTILINE)
    text = re.sub(r"^[\s]*\d+\.\s+", "", text, flags=re.MULTILINE)

    # Remove markdown blockquote markers
    text = re.sub(r"^>\s*", "", text, flags=re.MULTILINE)

    # Collapse multiple blank lines into one
    text = re.sub(r"\n{3,}", "\n\n", text)

    # Remove leading/trailing whitespace per line
    lines = [line.strip() for line in text.splitlines()]
    text = "\n".join(lines)

    # Final trim
    return text.strip()


def extract_text(path: str, clean: bool = True) -> str:
    """Extract text from a document file.

    Args:
        path: Path to the document file.
        clean: Whether to clean the text for TTS (default: True).

    Returns:
        Extracted (and optionally cleaned) text.
    """
    filepath = Path(path)

    if not filepath.exists():
        print(f"Error: File not found: {filepath}", file=sys.stderr)
        sys.exit(1)

    ext = filepath.suffix.lower()
    extractor = EXTRACTORS.get(ext)

    if not extractor:
        supported = ", ".join(sorted(EXTRACTORS.keys()))
        print(f"Error: Unsupported file type '{ext}'", file=sys.stderr)
        print(f"Supported types: {supported}", file=sys.stderr)
        sys.exit(1)

    text = extractor(filepath)

    if clean:
        text = clean_text(text)

    return text


def main():
    if len(sys.argv) < 2:
        print("Usage: python extract.py <file_path> [--raw]", file=sys.stderr)
        print("\nExtracts text from PDF, DOCX, Markdown, or plain text files.", file=sys.stderr)
        print("Output is cleaned for TTS by default. Use --raw to skip cleaning.", file=sys.stderr)
        sys.exit(1)

    file_path = sys.argv[1]
    raw = "--raw" in sys.argv

    text = extract_text(file_path, clean=not raw)
    print(text)


if __name__ == "__main__":
    main()
