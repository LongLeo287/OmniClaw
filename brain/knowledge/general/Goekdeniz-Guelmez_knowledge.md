---
id: goekdeniz-guelmez-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:48.556954
---

# KNOWLEDGE EXTRACT: Goekdeniz-Guelmez
> **Extracted on:** 2026-03-30 17:37:59
> **Source:** Goekdeniz-Guelmez

---

## File: `Local-NotebookLM.md`
```markdown
# 📦 Goekdeniz-Guelmez/Local-NotebookLM [🔖 PENDING/APPROVE]
🔗 https://github.com/Goekdeniz-Guelmez/Local-NotebookLM


## Meta
- **Stars:** ⭐ 862 | **Forks:** 🍴 106
- **Language:** Python | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Googles NotebookLM but local

## README (trích đầu)
```
# Local-NotebookLM

![logo](logo.jpeg)

A local AI-powered tool that converts PDF documents into engaging audio—such as podcasts or custom audio content—using local LLMs and TTS models.

## Features

- PDF text extraction and processing
- Customizable audio generation (podcasts, summaries, interviews, and more) with different styles and lengths
- Support for various LLM providers (OpenAI, Groq, LMStudio, Ollama, Azure)
- Text-to-Speech conversion with voice selection
- Flexible pipeline with many options for content, style, and voices
- Programmatic API for integration in other projects
- FastAPI server for web-based access
- Example podcast included for demonstration

#### Here are quick examples, can you guess what paper they're talking about?

<audio controls>
    <source src="https://raw.githubusercontent.com/Goekdeniz-Guelmez/Local-NotebookLM/main/examples/podcast_example_casual.wav" type="audio/wav">
    Your browser does not support the audio element. You can manually listen/download here: <a href="https://raw.githubusercontent.com/Goekdeniz-Guelmez/Local-NotebookLM/main/examples/podcast_example_casual.wav">Casual example</a>.
</audio>

<audio controls>
    <source src="https://raw.githubusercontent.com/Goekdeniz-Guelmez/Local-NotebookLM/main/examples/podcast_example_genz.wav" type="audio/wav">
    Your browser does not support the audio element. You can manually listen/download here: <a href="https://raw.githubusercontent.com/Goekdeniz-Guelmez/Local-NotebookLM/main/examples/podcast_example_genz.wav">Gen-Z example</a>.
</audio>

If your browser still blocks embedded playback on GitHub, use direct links:
- [Casual example (.wav)](https://raw.githubusercontent.com/Goekdeniz-Guelmez/Local-NotebookLM/main/examples/podcast_example_casual.wav)
- [Gen-Z example (.wav)](https://raw.githubusercontent.com/Goekdeniz-Guelmez/Local-NotebookLM/main/examples/podcast_example_genz.wav)

## Prerequisites

- Python 3.9+
- Local LLM server (optional, for local inference)
- Local TTS server (optional, for local audio generation)
- At least 8GB RAM (32GB+ recommended for local models)
- 10GB+ free disk space

## Installation

### From PyPI

```bash
pip install local-notebooklm
```

### From source

1. Clone the repository:

```bash
git clone https://github.com/Goekdeniz-Guelmez/Local-NotebookLM.git
cd Local-NotebookLM
```

2. Create and activate a virtual environment (conda works too):

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

## Running with Docker

You can run Local-NotebookLM using Docker for both the Web UI and API modes.

### Prerequisites

- Docker installed on your system

### Steps

1. **Build the Docker image:**

    ```bash
    docker build -t local-notebooklm-ui .
    ```

2. **Run the Gradio Web UI:**

    ```bash
    docker run -p 7860:7860 local-notebooklm-ui
    ```
    The Web UI will be available at [http://
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

