---
id: jupediaz-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:56.752543
---

# KNOWLEDGE EXTRACT: jupediaz
> **Extracted on:** 2026-03-30 17:38:14
> **Source:** jupediaz

---

## File: `chatgpt-prompt-splitter.md`
```markdown
# 📦 jupediaz/chatgpt-prompt-splitter [🔖 PENDING/APPROVE]
🔗 https://github.com/jupediaz/chatgpt-prompt-splitter
🌐 https://chatgpt-prompt-splitter.jjdiaz.dev

## Meta
- **Stars:** ⭐ 566 | **Forks:** 🍴 92
- **Language:** Python | **License:** MIT
- **Last updated:** 2026-03-09
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
ChatGPT PROMPTs Splitter. Tool for safely process chunks of up to 15,000 characters per request

## README (trích đầu)
```
<p align="center">
  <img src="static/chatgpt_prompt_splitter.png" width="150" alt="ChatGPT PROMPTs Splitter" />
  <h1 align="center">ChatGPT PROMPTs Splitter</h1>
</p>

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fjupediaz%2Fchatgpt-prompt-splitter)

### ❓ Have you ever received a message from ChatGPT about sending too much data and needing to send a shorter text?

#### **Here's a great alternative to bypass this limitation!** 🚀

![Error Message Too Long](/static/screenshots/screenshot_error_message_too_long.png)
## Overview

**ChatGPT PROMPTs Splitter** is an open-source tool designed to help you split long text prompts into smaller chunks, making them suitable for usage with ChatGPT (or other language models with character limitations).

The tool ensures that the text is divided into safe chunks of up to 15,000 characters per request as default, although can be changed.

The project includes an easy-to-use web interface for inputting the long text, selecting the maximum length of each chunk, and copying the chunks individually to paste them to ChatGPT.

## Post on Medium

You can read the full article on Medium: [ChatGPT PROMPTs Splitter: Split long text prompts into smaller chunks for ChatGPT](https://medium.com/@josediazmoreno/break-the-limits-send-large-text-blocks-to-chatgpt-with-ease-6824b86d3270)

## How it works

The tool uses a simple algorithm to split the text into smaller chunks. The algorithm is based on the following rules:

1. Divide the prompt into chunks based on the specified maximum length.

2. Add information to the first chunk to instruct the AI on the process of receiving and acknowledging the chunks, and to wait for the completion of chunk transmission before processing subsequent requests.

## Features

- Python 3.9
- Web interface for splitting text into smaller chunks
- Customizable maximum length for each chunk
- Copy chunks individually to send to ChatGPT
- Instructions for ChatGPT on how to process the chunks
- Tests included
- Easy deployment to Vercel included

## Usage example

Follow these simple steps to use the ChatGPT Prompt Splitter web application, illustrated with screenshots.

### Step 1: Access the application
Open your web browser and navigate to the application URL.

https://chatgpt-prompt-splitter.jjdiaz.dev/

You should see the main screen, displaying the input fields for your long text prompt and maximum chunk length.

![Set Max Length](/static/screenshots/screenshot_main_screen.png)

### Step 2: Input the long prompt
Enter the text you want to split into smaller chunks for use with ChatGPT.

You can also specify custom length for each chunk by entering the number of characters in the *"Max chars length..."* field.

In this example, we are gonna split into chunks of just 25 characters.

![Input Text](/static/screenshots/screenshot_example_text.png)

### Step 3: Click "Split"
Click the "Split" button to process the text and 
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

