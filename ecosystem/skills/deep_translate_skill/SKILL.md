---
name: Deep Translator Integration
author: OmniClaw Academy (OA)
version: 1.0.0
description: "Adapted from an orphaned module. This skill empowers OmniClaw agents to perform multi-engine, multi-lingual text translation via Google Translate, DeepL, Papago, etc., without relying on LLM context windows."
tags: [translation, deep-translator, utility, language, NLP]
dependencies:
  python:
    - deep-translator>=1.11.4
---

# Deep Translator Skill

## Overview
This skill was forged through the **Innovation Clause** (`ki_2026_04_03_vault_legacy_assimilation`). An orphaned copy of `deep_translator` was discovered in the Vault models directory. Instead of discarding it, OmniClaw Academy recognized its utility and permanently integrated it.

This skill provides native translation capabilities to the workforce, saving LLM tokens by delegating simple translation tasks to external APIs.

## Supported Engines
- Google Translate (Default, free)
- MyMemory
- Linguee
- Pons

## Usage (Python Script Example)
Agents can invoke this module in `.py` scripts via:

```python
from deep_translator import GoogleTranslator

def translate_to_english(text):
    """Translates arbitrary text to English using Google Translate API."""
    translator = GoogleTranslator(source='auto', target='en')
    return translator.translate(text)

def translate_to_vietnamese(text):
    """Translates arbitrary text to Vietnamese to bypass 90/10 localized communications."""
    translator = GoogleTranslator(source='auto', target='vi')
    return translator.translate(text)
```

## System Constraints
1. **Dependency:** Ensure `pip install deep-translator` is run on the target host before invoking.
2. **Rate Limits:** Do not abuse free translation APIs in tight `while True` loops.

## AI Instructions
- If the user asks for multi-document translation or bulk string translation, use this skill rather than generating the translation using your own LLM weights to save costs.
