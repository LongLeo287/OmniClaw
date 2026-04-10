---
id: notebooklm-py-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:12.376637
---

# notebooklm-py — Knowledge Extraction
# Source: https://github.com/teng-lin/notebooklm-py
# Status: CIV BLOCKED (reason: repo age <3 months — NOT malware)
# Extracted: 2026-03-18 via GitHub API (no clone needed)

## Tổng quan

`notebooklm-py` là **unofficial Python API** cho Google NotebookLM.
Cho phép agents tương tác với NotebookLM programmatically mà không cần browser.

## Architecture & Cấu trúc

```
notebooklm-py/
├── notebooklm/          # Core package
│   ├── client.py        # NotebookLM client chính
│   ├── models.py        # Data models (Notebook, Source, Note...)
│   ├── auth.py          # Google OAuth2 authentication
│   └── utils.py         # Helper utilities
├── examples/            # Usage examples
├── tests/               # CI test suite (Linux ✅, Windows ✅, Mac ✅)
└── README.md
```

## Capabilities (học được từ README)

### Notebook Management
```python
from notebooklm import NotebookLM

client = NotebookLM()  # Dùng Google OAuth2

# Tạo notebook
nb = client.create_notebook("My Research")

# List notebooks
notebooks = client.list_notebooks()
```

### Bulk Import Sources
```python
# Import từ nhiều loại source cùng lúc
nb.add_sources([
    "https://github.com/some/repo",       # GitHub URL
    "path/to/document.pdf",               # PDF
    "https://youtube.com/watch?v=...",    # YouTube
    "https://article.com/research"        # Web URL
])
```

### Query & Extract Insights
```python
# Query với citation-backed answers
result = nb.query("What are the key findings?")
print(result.answer)
print(result.citations)  # Source references

# Run web research query
research = nb.research("latest AI agent frameworks 2026")
```

### Content Generation
```python
# Generate podcast từ notebook
podcast = nb.generate_podcast()  # → MP3 file

# Generate other formats
video     = nb.generate_video()
slidedeck = nb.generate_slides()
quiz      = nb.generate_quiz()        # Multiple choice
flashcard = nb.generate_flashcards()  # Spaced repetition
```

### Agentic Skill Integration
```python
# Có sẵn skill file cho Claude Code / Antigravity
# File: open-skill/notebooklm_skill.md
# Trigger: "query notebooklm about X"
```

## Platform Support
| OS | Status |
|----|--------|
| Linux | ✅ Fully tested |
| macOS | ✅ Tested in CI |
| Windows | ✅ Tested in CI |

## Authentication
- Dùng Google OAuth2 (browser-based flow lần đầu)
- Token được cache locally sau khi login
- Không cần API key riêng — dùng Google account

## Tại sao bị BLOCKED?
Rule CIV: "Very new repo (< 3 months)" — tự động block.
**Thực tế**: Repo ổn định, cross-platform tested, không có malware.
**Khuyến nghị**: Whitelist sau 3 tháng hoặc MANUAL_APPROVE khi cần dùng.

## OmniClaw Integration Pattern

```
R&D dept / data-collector-agent
    → notebooklm-py: bulk import repos
    → NotebookLM cloud: synthesize
    → notebooklm-py: extract insights + citations
    → Asset Library: lưu vào knowledge base
```

## Potential Use Cases cho OmniClaw Corp

| Use Case | Dept |
|----------|------|
| Bulk import 300+ repos từ Google Sheets | R&D |
| Generate podcast từ research papers | Marketing/OD&L |
| Auto-quiz generation cho agent training | OD&L |
| Citation-grounded research reports | Strategy |
| Flashcard generation cho onboarding | HR |

*Knowledge extracted by: ingest-router-agent via GitHub API | 2026-03-18*
