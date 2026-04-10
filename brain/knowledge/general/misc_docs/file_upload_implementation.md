---
id: file-upload-implementation
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:24.172680
---

# File Upload Implementation

## Overview

File upload uses **HTTP Resumable Upload** – the reliable, headless method.

## HTTP Resumable Upload

### Implementation

Uses Google's 3-step resumable upload protocol:

1. **Register source intent** (RPC: `o4cbdc`) → get SOURCE_ID
2. **Start upload session** (POST to `/upload/_/`) → get upload URL
3. **Stream file content** → upload URL (memory-efficient streaming)

### Code Structure

- `SourceMixin._register_file_source()` - Step 1: Register and get SOURCE_ID
- `SourceMixin._start_resumable_upload()` - Step 2: Get upload URL
- `SourceMixin._upload_file_streaming()` - Step 3: Stream file content
- `SourceMixin.add_file()` - Public API that orchestrates all 3 steps

### Usage

**Python:**
```python
from notebooklm_tools.core.client import NotebookLMClient

with NotebookLMClient() as client:
    result = client.add_file(notebook_id="...", file_path="document.pdf")
# Returns: {"id": "source-id", "title": "document.pdf"}
```

**CLI:**
```bash
nlm source add <notebook-id> --file document.pdf
```

**MCP:**
```python
source_add(notebook_id="...", source_type="file", file_path="/path/to/file.pdf")
```

### Supported File Types

- PDF (`.pdf`)
- Text (`.txt`, `.md`)
- Documents (`.docx`, `.csv`)
- Audio (`.mp3`)
- Video (`.mp4`)
- Images (`.jpg`, `.jpeg`, `.png`)

### Advantages

- ✅ No Chrome dependency
- ✅ Works in headless/server environments
- ✅ Memory-efficient streaming for large files
- ✅ Faster and more reliable
- ✅ No browser fingerprinting issues

## Testing

```bash
# Create a test file
echo "Test content" > test.txt

# Upload the file
nlm source add <notebook-id> --file test.txt

# Verify it was added
nlm source list <notebook-id>
```

## Troubleshooting

### "File not found"
- **Cause**: The file path doesn't exist or is inaccessible
- **Fix**: Check the file path spelling and permissions

### "Unsupported file type"
- **Cause**: File extension is not in the supported list
- **Fix**: Convert the file to a supported format

### Upload times out
- **Cause**: Large file or slow connection
- **Fix**: The upload may still complete on the backend; check notebook sources before retrying

---

## Historical Note

A browser-based upload fallback using Chrome automation was previously available (`--browser` flag) but has been removed. NotebookLM's UI now uses the File System Access API which cannot be automated via CDP. The HTTP method is more reliable anyway.
