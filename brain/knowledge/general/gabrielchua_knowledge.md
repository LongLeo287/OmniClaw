---
id: gabrielchua-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:25.802583
---

# KNOWLEDGE EXTRACT: gabrielchua
> **Extracted on:** 2026-03-30 17:37:23
> **Source:** gabrielchua

---

## File: `open-notebooklm.md`
```markdown
# 📦 gabrielchua/open-notebooklm [⭐ ACTIVE]
🔗 https://github.com/gabrielchua/open-notebooklm
🌐 https://huggingface.co/spaces/gabrielchua/open-notebooklm

## Meta
- **Stars:** ⭐ 2575 | **Forks:** 🍴 280
- **Language:** Python | **License:** Apache-2.0
- **Last updated:** 2026-03-25
- **Topics:** (none)
- **Status trong AI OS:** ⭐ ACTIVE

## Description:
Convert any PDF into a podcast episode!

## README (FULL)
```
---
title: Open NotebookLM
emoji: 🎙️
colorFrom: purple
colorTo: red
sdk: gradio
sdk_version: 5.0.1
app_file: app.py
pinned: true
header: mini
short_description: Personalised Podcasts For All - Available in 13 Languages
---

# Open NotebookLM

## Overview

This project is inspired by the NotebookLM tool, and implements it with open-source LLMs and text-to-speech models. This tool processes the content of a PDF, generates a natural dialogue suitable for an audio podcast, and outputs it as an MP3 file.

Built with:
- [Llama 3.3 70B 🦙](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct) via [Fireworks AI 🎆](https://fireworks.ai/) and [Instructor 📐](https://github.com/instructor-ai/instructor) 
- [MeloTTS 🐚](https://huggingface.co/myshell-ai/MeloTTS-English)
- [Bark 🐶](https://huggingface.co/suno/bark)
- [Jina Reader 🔍](https://jina.ai/reader/)

## Features

- **Convert PDF to Podcast:** Upload a PDF and convert its content into a podcast dialogue.
- **Engaging Dialogue:** The generated dialogue is designed to be informative and entertaining.
- **User-friendly Interface:** Simple interface using Gradio for easy interaction.

## Installation

To set up the project, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/gabrielchua/open-notebooklm.git
   cd open-notebooklm
   ```

2. **Create a virtual environment and activate it:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Set up API Key(s):**
   For this project, I am using LLama 3.3 70B hosted on Fireworks API as its JSON Mode supports passing a pydantic object. So, please set the API key as the `FIREWORKS_API_KEY` environment variable

2. **Run the application:**
   ```bash
   python app.py
   ```
   This will launch a Gradio interface in your web browser.

3. **Upload a PDF:**
   Upload the PDF document you want to convert into a podcast.

4. **Generate Audio:**
   Click the button to start the conversion process. The output will be an MP3 file containing the podcast dialogue.

## Acknowledgements

This project is forked from [`knowsuchagency/pdf-to-podcast`](https://github.com/knowsuchagency/pdf-to-podcast)

## License

This project is licensed under the Apache 2.0 License. See the [LICENSE](LICENSE) file for more information.

```

---
*Ingested: 2026-03-27 | Source: GitHub API FULL | Owner: Dept 07 Knowledge*
```

