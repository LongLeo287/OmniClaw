---
id: OpenOats
type: knowledge
owner: OA_Triage
---
# OpenOats
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# OpenOats

A meeting note-taker that talks back.

<p align="center">
  <a href="https://github.com/yazinsai/OpenOats/releases/latest">
    <img src="https://img.shields.io/badge/Download_for_Mac-DMG-black?style=for-the-badge&logo=apple&logoColor=white" alt="Download for Mac" />
  </a>
</p>

OpenOats sits next to your call, transcribes both sides of the conversation in real time, and searches your own notes to surface things worth saying — right when you need them.

<p align="center">
  <img src="assets/screenshot.png" width="360" alt="OpenOats during a call — suggestions drawn from your own notes appear at the top, live transcript below" />
</p>

## Features

- **Invisible to the other side** — the app window is hidden from screen sharing by default, so no one knows you're using it
- **Fully offline transcription** — speech recognition runs entirely on your Mac; no audio ever leaves the device
- **Runs 100% locally** — pair with [Ollama](https://ollama.com/) for LLM suggestions and local embeddings, and nothing touches the network at all
- **Pick any LLM** — use [OpenRouter](https://openrouter.ai/) for cloud models (GPT-4o, Claude, Gemini) or Ollama for local ones (Llama, Qwen, Mistral)
- **Live transcript** — see both sides of the conversation as it happens, copy the whole thing with one click
- **Auto-saved sessions** — every conversation is automatically saved as a plain-text transcript and a structured session log, no manual export needed
- **Knowledge base search** — point it at a folder of notes and it pulls in what's relevant using [Voyage AI](https://www.voyageai.com/) embeddings, local Ollama embeddings, or any OpenAI-compatible endpoint (llama.cpp, llamaswap, LiteLLM, vLLM, etc.)

## How it works

1. You start a call and hit **Live**
2. OpenOats transcribes both speakers locally on your Mac
3. When the conversation hits a moment that matters — a question, a decision point, a claim worth backing up — it searches your notes and surfaces relevant talking points
4. You sound prepared because you are

## Recording Consent & Legal Disclaimer

**Important:** OpenOats records and transcribes audio from your microphone and system audio. Many jurisdictions have laws requiring consent from some or all participants before a conversation may be recorded (e.g., two-party/all-party consent states in the U.S., GDPR in the EU).

**By using this software, you acknowledge and agree that:**

- **You are solely responsible** for determining whether recording is lawful in your jurisdiction and for obtaining any required consent from all participants before starting a session.
- **The developers and contributors of OpenOats provide no legal advice** and make no representations about the legality of recording in any jurisdiction.
- **The developers accept no liability** for any unauthorized or unlawful recording conducted using this software.

**Do not use this software to record conversations without proper consent where required by law.**

The app will ask you to acknowledge these obligations before your first recording session.

## Download

Install via Homebrew:

```bash
brew tap yazinsai/openoats https://github.com/yazinsai/OpenOats
brew install --cask yazinsai/openoats/openoats
```

To upgrade later:

```bash
brew upgrade --cask yazinsai/openoats/openoats
```

Or grab the latest DMG from the [Releases page](https://github.com/yazinsai/OpenOats/releases/latest).

Or build from source:

```bash
./scripts/build_swift_app.sh
```

## Quick start

1. Open the DMG and drag OpenOats to Applications
2. Launch the app and grant microphone + system audio recording permissions
3. Open Settings (`Cmd+,`) and pick your providers:
   - **Cloud**: add your OpenRouter and Voyage AI API keys
   - **Local**: select Ollama as your LLM and embedding provider (make sure Ollama is running)
   - **OpenAI-compatible**: select "OpenAI Compatible" as your embedding provider and point it at any `/v1/embeddings` endpoint
4. Point it at a folder of `.md` or `.txt` files — that's your knowledge base
5. Click **Idle** to go live

The first run downloads the local speech model (~600 MB).

## What you need

- Apple Silicon Mac, macOS 15+
- Xcode 26 / Swift 6.2
- **For cloud mode**: [OpenRouter](https://openrouter.ai/) API key + [Voyage AI](https://www.voyageai.com/) API key
- **For local mode**: [Ollama](https://ollama.com/) running locally with your preferred models (e.g. `qwen3:8b` for suggestions, `nomic-embed-text` for embeddings)
- **For OpenAI-compatible embeddings**: any server implementing `/v1/embeddings` (llama.cpp, llamaswap, LiteLLM, vLLM, etc.)

## Knowledge base

Point the app at a folder of Markdown or plain text files. That's it. OpenOats chunks, embeds, and caches them locally. When the conversation shifts, it searches your notes and only surfaces what's actually relevant.

Works well with meeting prep docs, research notes, pitch decks, competitive analysis, customer briefs — anything you'd want at your fingertips during a call.

## Privacy

- Speech is transcribed locally — audio never leaves your Mac
- **With Ollama**: everything stays on your machine. Zero network calls.
- **With cloud providers**: KB chunks are sent to Voyage AI (or your chosen OpenAI-compatible endpoint) for embedding (text only, no audio), and conversation context is sent to OpenRouter for suggestions
- API keys are stored in your Mac's Keychain
- The app window is hidden from screen sharing by default
- Transcripts are saved locally to `~/Documents/OpenOats/`

### Cloud mode: what data leaves your Mac

When using cloud providers, OpenOats makes the following network requests. **No audio is ever sent** — only text. In fully-local mode (Ollama for both LLM and embeddings), nothing touches the network at all.

#### 1. Knowledge base indexing — Voyage AI (`api.voyageai.com/v1/embeddings`)

**When:** Each time you index your knowledge base folder (on launch or when files change).

**What is sent:**
- Text chunks from your `.md` / `.txt` knowledge base files (split by markdown headings, 80–500 words each, with the header breadcrumb prepended)
- Model name (`voyage-4-lite`) and requested output dimensions (`256`)
- Input type (`document`)

Chunks are sent in batches of 32. Only new or changed files are embedded — unchanged files use a local cache.

#### 2. Knowledge base search — Voyage AI (`api.voyageai.com/v1/embeddings`)

**When:** Each time the suggestion pipeline runs (triggered by a substantive utterance from the other speaker, subject to a 90-second cooldown).

**What is sent:**
- 1–4 short query strings derived from the conversation: the latest utterance text, the current conversation topic, a short conversation summary, and the top open question
- Model name, dimensions, and input type (`query`)

#### 3. Knowledge base reranking — Voyage AI (`api.voyageai.com/v1/rerank`)

**When:** Immediately after step 2, if Voyage AI is the embedding provider.

**What is sent:**
- The primary search query (the latest utterance text)
- Up to 10 candidate KB chunk texts (from your own notes) for reranking
- Model name (`rerank-2.5-lite`)

#### 4. Conversation state update — OpenRouter (`openrouter.ai/api/v1/chat/completions`)

**When:** Periodically during a session when the conversation state needs refreshing.

**What is sent (as an LLM prompt):**
- The previous conversation state (topic, summary, open questions, tensions, recent decisions, goals — all derived from earlier LLM calls)
- Recent transcript utterances (both speakers, text only — labeled "You" / "Them")
- The latest utterance from the other speaker
- A system prompt instructing the model to update the conversation state

#### 5. Surfacing gate — OpenRouter (`openrouter.ai/api/v1/chat/completions`)

**When:** After the KB search returns relevant results, to decide whether a suggestion is worth showing.

**What is sent (as an LLM prompt):**
- The latest utterance from the other speaker
- Recent transcript exchange (both speakers, text only)
- Current conversation state (topic, summary, open questions, tensions)
- The detected trigger type and excerpt
- Up to 5 KB evidence chunks (text from your notes, with source file and header, plus relevance scores)
- Recently shown suggestion angles (short strings, to avoid repeats)

#### 6. Suggestion generation — OpenRouter (`openrouter.ai/api/v1/chat/completions`)

**When:** Only if the surfacing gate approves (all quality scores above threshold).

**What is sent (as an LLM prompt):**
- The latest utterance from the other speaker
- Current conversation state (topic and summary)
- The gate's reasoning string
- Up to 3 KB evidence chunks (text from your notes, with source file and header)

#### 7. Meeting notes generation — OpenRouter (`openrouter.ai/api/v1/chat/completions`)

**When:** When you click "Generate Notes" after a session.

**What is sent (as an LLM prompt):**
- The full session transcript (both speakers, with timestamps, labeled "You" / "Them") — truncated to ~60,000 characters if very long
- The meeting template's system prompt (e.g., instructions for formatting notes)

#### What is never sent

- **Audio** — transcription is always on-device via Apple Speech
- **File paths or filenames from your system** (only KB source filenames appear in prompts)
- **Your API keys to anyone other than the respective provider** (OpenRouter key to OpenRouter, Voyage key to Voyage)
- **Any data when using Ollama** — all requests go to your local machine

## Build

```bash
# Full build → sign → install to /Applications
./scripts/build_swift_app.sh

# Dev build only
cd OpenOats && swift build -c debug

# Package DMG
./scripts/make_dmg.sh
```

Optional env vars for code signing and notarization: `CODESIGN_IDENTITY`, `APPLE_ID`, `APPLE_TEAM_ID`, `APPLE_APP_PASSWORD`.

## Repo layout

```
OpenOats/             SwiftUI app (Swift Package)
scripts/              Build, sign, and package scripts
assets/               Screenshot and app icon source
```

## License

MIT

```

### File: benchmark\results.json
```json
[
  {
    "model": "large-v3-turbo",
    "language": "polish",
    "file": "polish_0.wav",
    "wer": 0.02631578947368421,
    "cer": 0.00392156862745098,
    "elapsed": 29.61875581741333,
    "ref": "stali\u015bmy wszyscy bezradni wobec tej szalej\u0105cej furii z\u0142o\u015bci kt\u00f3ra sama siebie tr",
    "hyp": "stali\u015bmy wszyscy bezradni wobec tej szalej\u0105cej furyi z\u0142o\u015bci kt\u00f3ra sama siebie tr"
  },
  {
    "model": "large-v3-turbo",
    "language": "polish",
    "file": "polish_1.wav",
    "wer": 0.0,
    "cer": 0.0,
    "elapsed": 27.107510089874268,
    "ref": "nawet w obecno\u015bci matki le\u017c\u0105cej z zawi\u0105zan\u0105 g\u0142ow\u0105 na sofie nie mog\u0142y si\u0119 powstrz",
    "hyp": "nawet w obecno\u015bci matki le\u017c\u0105cej z zawi\u0105zan\u0105 g\u0142ow\u0105 na sofie nie mog\u0142y si\u0119 powstrz"
  },
  {
    "model": "large-v3-turbo",
    "language": "spanish",
    "file": "spanish_0.wav",
    "wer": 0.0,
    "cer": 0.0,
    "elapsed": 38.98723101615906,
    "ref": "y las almas buscando alg\u00fan alivio se revuelven ansiosas y hacen el mundo que as\u00ed",
    "hyp": "y las almas buscando alg\u00fan alivio se revuelven ansiosas y hacen el mundo que as\u00ed"
  },
  {
    "model": "large-v3-turbo",
    "language": "spanish",
    "file": "spanish_1.wav",
    "wer": 0.024390243902439025,
    "cer": 0.0045871559633027525,
    "elapsed": 28.40156626701355,
    "ref": "cuando calla el dolor se oye a la muerte las alas tenebrosas batir en los profun",
    "hyp": "cuando calla el dolor se oye a la muerte las alas tenebrosas batir en los profun"
  },
  {
    "model": "large-v3-turbo",
    "language": "french",
    "file": "french_0.wav",
    "wer": 0.0,
    "cer": 0.0,
    "elapsed": 28.643215894699097,
    "ref": "pendant le second si\u00e8cle je fis serment douvrir tous les tr\u00e9sors de la terre \u00e0 q",
    "hyp": "pendant le second si\u00e8cle je fis serment douvrir tous les tr\u00e9sors de la terre \u00e0 q"
  },
  {
    "model": "large-v3-turbo",
    "language": "french",
    "file": "french_1.wav",
    "wer": 0.03278688524590164,
    "cer": 0.009615384615384616,
    "elapsed": 29.78007411956787,
    "ref": "non ta mort est certaine dit le g\u00e9nie choisis seulement de quelle sorte tu veux ",
    "hyp": "non ta mort est certaine dit le g\u00e9nie choisis seulement de quelle sorte tu veux "
  },
  {
    "model": "large-v3-turbo",
    "language": "german",
    "file": "german_0.wav",
    "wer": 0.125,
    "cer": 0.02127659574468085,
    "elapsed": 31.323474884033203,
    "ref": "denken sie soeben weilten meine gedanken bei ihnen in adelaide und ich w\u00fcnschte ",
    "hyp": "denken sie soeben weilten meine gedanken bei ihnen in adelaide und ich wunschte "
  },
  {
    "model": "large-v3-turbo",
    "language": "german",
    "file": "german_1.wav",
    "wer": 0.0,
    "cer": 0.0,
    "elapsed": 29.706756830215454,
    "ref": "also bei ihren technischen kenntnissen und ihrer erfindungsgabe auf diesem gebie",
    "hyp": "also bei ihren technischen kenntnissen und ihrer erfindungsgabe auf diesem gebie"
  },
  {
    "model": "small",
    "language": "polish",
    "file": "polish_0.wav",
    "wer": 0.02631578947368421,
    "cer": 0.00392156862745098,
    "elapsed": 27.759119033813477,
    "ref": "stali\u015bmy wszyscy bezradni wobec tej szalej\u0105cej furii z\u0142o\u015bci kt\u00f3ra sama siebie tr",
    "hyp": "stali\u015bmy wszyscy bezradni wobec tej szalej\u0105cej furii z\u0142o\u015bci kt\u00f3ra sama siebie tr"
  },
  {
    "model": "small",
    "language": "polish",
    "file": "polish_1.wav",
    "wer": 0.13157894736842105,
    "cer": 0.015267175572519083,
    "elapsed": 29.2135751247406,
    "ref": "nawet w obecno\u015bci matki le\u017c\u0105cej z zawi\u0105zan\u0105 g\u0142ow\u0105 na sofie nie mog\u0142y si\u0119 powstrz",
    "hyp": "nawet wobecno\u015bci matki le\u017c\u0105cej z zawi\u0105zan\u0105 g\u0142ow\u0105 na sofie nie mog\u0142y si\u0119 powstrzy"
  },
  {
    "model": "small",
    "language": "spanish",
    "file": "spanish_0.wav",
    "wer": 0.03225806451612903,
    "cer": 0.006211180124223602,
    "elapsed": 12.09125018119812,
    "ref": "y las almas buscando alg\u00fan alivio se revuelven ansiosas y hacen el mundo que as\u00ed",
    "hyp": "y las almas buscando alg\u00fan alivio se revuelven ansioses y hacen el mundo que as\u00ed"
  },
  {
    "model": "small",
    "language": "spanish",
    "file": "spanish_1.wav",
    "wer": 0.024390243902439025,
    "cer": 0.0045871559633027525,
    "elapsed": 20.607052087783813,
    "ref": "cuando calla el dolor se oye a la muerte las alas tenebrosas batir en los profun",
    "hyp": "cuando calla el dolor se oye a la muerte las alas tenebrosas batir en los profun"
  },
  {
    "model": "small",
    "language": "french",
    "file": "french_0.wav",
    "wer": 0.15555555555555556,
    "cer": 0.064,
    "elapsed": 20.3839590549469,
    "ref": "pendant le second si\u00e8cle je fis serment douvrir tous les tr\u00e9sors de la terre \u00e0 q",
    "hyp": "pendant le second si\u00e8cle je fis serment douvrir tous les tr\u00e9sors de la terre \u00e0 q"
  },
  {
    "model": "small",
    "language": "french",
    "file": "french_1.wav",
    "wer": 0.09836065573770492,
    "cer": 0.03205128205128205,
    "elapsed": 33.21484398841858,
    "ref": "non ta mort est certaine dit le g\u00e9nie choisis seulement de quelle sorte tu veux ",
    "hyp": "non ta mort est certaine dit le g\u00e9nie choisis seulement de quelle sorte tu veux "
  },
  {
    "model": "small",
    "language": "german",
    "file": "german_0.wav",
    "wer": 0.09375,
    "cer": 0.02127659574468085,
    "elapsed": 39.31195306777954,
    "ref": "denken sie soeben weilten meine gedanken bei ihnen in adelaide und ich w\u00fcnschte ",
    "hyp": "denken sie soeben walten meine gedanken bei ihnen in adelaide und ich w\u00fcnschte m"
  },
  {
    "model": "small",
    "language": "german",
    "file": "german_1.wav",
    "wer": 0.07407407407407407,
    "cer": 0.011111111111111112,
    "elapsed": 18.51436424255371,
    "ref": "also bei ihren technischen kenntnissen und ihrer erfindungsgabe auf diesem gebie",
    "hyp": "also bei ihren technischen kenntnissen und ihrer erfindungsgabe auf diesem gebie"
  },
  {
    "model": "base",
    "language": "polish",
    "file": "polish_0.wav",
    "wer": 0.05263157894736842,
    "cer": 0.00784313725490196,
    "elapsed": 7.524443864822388,
    "ref": "stali\u015bmy wszyscy bezradni wobec tej szalej\u0105cej furii z\u0142o\u015bci kt\u00f3ra sama siebie tr",
    "hyp": "stali\u015bmy wszyscy bezradni wobec tej szalej\u0105cej furii z\u0142o\u015bci kt\u00f3ra sama siebie tr"
  },
  {
    "model": "base",
    "language": "polish",
    "file": "polish_1.wav",
    "wer": 0.3157894736842105,
    "cer": 0.03816793893129771,
    "elapsed": 11.547529935836792,
    "ref": "nawet w obecno\u015bci matki le\u017c\u0105cej z zawi\u0105zan\u0105 g\u0142ow\u0105 na sofie nie mog\u0142y si\u0119 powstrz",
    "hyp": "nawet wobecno\u015bci matki le\u017c\u0105cej z zawi\u0105zan\u0105 g\u0142ow\u0105 na sofi\u0119 nie mog\u0142y si\u0119 powstrzy"
  },
  {
    "model": "base",
    "language": "spanish",
    "file": "spanish_0.wav",
    "wer": 0.12903225806451613,
    "cer": 0.037267080745341616,
    "elapsed": 14.672544002532959,
    "ref": "y las almas buscando alg\u00fan alivio se revuelven ansiosas y hacen el mundo que as\u00ed",
    "hyp": "y las almas buscando alguna livio se revuelven ansiosas y hacen el mundo que as\u00ed"
  },
  {
    "model": "base",
    "language": "spanish",
    "file": "spanish_1.wav",
    "wer": 0.17073170731707318,
    "cer": 0.03211009174311927,
    "elapsed": 13.943961143493652,
    "ref": "cuando calla el dolor se oye a la muerte las alas tenebrosas batir en los profun",
    "hyp": "cuando calle el dolor se oye a la muerte las salas tenebrosas batire en los prof"
  },
  {
    "model": "base",
    "language": "french",
    "file": "french_0.wav",
    "wer": 0.2,
    "cer": 0.104,
    "elapsed": 9.866574048995972,
    "ref": "pendant le second si\u00e8cle je fis serment douvrir tous les tr\u00e9sors de la terre \u00e0 q",
    "hyp": "pendant le second si\u00e8cle je fiss\u00e8rement douvrir tous les tr\u00e9sors de la terre \u00e0 q"
  },
  {
    "model": "base",
    "language": "french",
    "file": "french_1.wav",
    "wer": 0.26229508196721313,
    "cer": 0.08653846153846154,
    "elapsed": 23.716958045959473,
    "ref": "non ta mort est certaine dit le g\u00e9nie choisis seulement de quelle sorte tu veux ",
    "hyp": "non ta mort est certaine dit de g\u00e9nie choisi seulement de quel sorte tu veux que"
  },
  {
    "model": "base",
    "language": "german",
    "file": "german_0.wav",
    "wer": 0.1875,
    "cer": 0.05319148936170213,
    "elapsed": 8.058078050613403,
    "ref": "denken sie soeben weilten meine gedanken bei ihnen in adelaide und ich w\u00fcnschte ",
    "hyp": "denken sie so eben walten meine gedanken bei ihnen in adelaide und ich w\u00fcnschte "
  },
  {
    "model": "base",
    "language": "german",
    "file": "german_1.wav",
    "wer": 0.2222222222222222,
    "cer": 0.05555555555555555,
    "elapsed": 7.411097764968872,
    "ref": "also bei ihren technischen kenntnissen und ihrer erfindungsgabe auf diesem gebie",
    "hyp": "also bei ihren technischen kenntnissen und ihre erfindungsgabe auf diesem gebiet"
  }
]
```

### File: benchmark\run_benchmark.py
```py
#!/usr/bin/env python3
"""
Benchmark transcription models against MLS ground truth.

Uses openai-whisper CLI (PyTorch) to test whisper models.
WhisperKit CoreML results track closely with PyTorch at batch scale
(per Newarr's benchmarks: WK turbo 28.8% vs PyTorch turbo 34.3% batch WER),
so PyTorch results are a reasonable proxy.

Usage: python3 run_benchmark.py
"""

import json
import os
import subprocess
import sys
import time
import unicodedata
import re

# jiwer for proper WER calculation
from jiwer import wer as compute_wer, cer as compute_cer

BENCHMARK_DIR = os.path.dirname(os.path.abspath(__file__))
AUDIO_DIR = os.path.join(BENCHMARK_DIR, "audio")
SAMPLES_FILE = os.path.join(BENCHMARK_DIR, "samples.json")

# Models to benchmark (whisper CLI model names)
MODELS = [
    "large-v3-turbo",  # maps to whisperLargeV3Turbo in the app
    "small",           # maps to whisperSmall in the app
    "base",            # maps to whisperBase in the app (excluded from batch, for reference)
]

def normalize_text(text: str) -> str:
    """Normalize text for WER comparison: lowercase, strip punctuation, collapse whitespace."""
    text = text.lower()
    # Remove accents for fairer comparison (some models output unaccented text)
    # Actually keep accents — they matter for non-English
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def run_whisper(audio_path: str, model: str, language: str) -> tuple[str, float]:
    """Run whisper CLI and return (transcript, elapsed_seconds)."""
    lang_map = {
        "polish": "pl",
        "spanish": "es",
        "french": "fr",
        "german": "de",
        "english": "en",
    }
    lang_code = lang_map.get(language, language)

    start = time.time()
    result = subprocess.run(
        [
            "whisper", audio_path,
            "--model", model,
            "--language", lang_code,
            "--output_format", "txt",
            "--output_dir", "/tmp/whisper_bench",
            "--fp16", "False",  # CPU mode
        ],
        capture_output=True,
        text=True,
        timeout=300,
    )
    elapsed = time.time() - start

    # Read output file
    basename = os.path.splitext(os.path.basename(audio_path))[0]
    txt_path = f"/tmp/whisper_bench/{basename}.txt"
    transcript = ""
    if os.path.exists(txt_path):
        with open(txt_path) as f:
            transcript = f.read().strip()
        os.remove(txt_path)

    return transcript, elapsed


def main():
    os.makedirs("/tmp/whisper_bench", exist_ok=True)

    with open(SAMPLES_FILE) as f:
        samples = json.load(f)

    print(f"Loaded {len(samples)} samples")
    print(f"Models: {', '.join(MODELS)}")
    print("=" * 110)

    results = []

    for model in MODELS:
        print(f"\n--- Model: {model} ---")

        for sample in samples:
            wav_file = sample["file"].replace(".opus", ".wav")
            wav_path = os.path.join(BENCHMARK_DIR, wav_file)

            if not os.path.exists(wav_path):
                print(f"  [{sample['language']}] {wav_file}: MISSING")
                continue

            try:
                hypothesis, elapsed = run_whisper(wav_path, model, sample["language"])

                ref_norm = normalize_text(sample["transcript"])
                hyp_norm = normalize_text(hypothesis)

                if ref_norm and hyp_norm:
                    sample_wer = compute_wer(ref_norm, hyp_norm)
                    sample_cer = compute_cer(ref_norm, hyp_norm)
                else:
                    sample_wer = 1.0 if not hyp_norm else 0.0
                    sample_cer = 1.0 if not hyp_norm else 0.0

                results.append({
                    "model": model,
                    "language": sample["language"],
                    "file": os.path.basename(wav_path),
                    "wer": sample_wer,
                    "cer": sample_cer,
                    "elapsed": elapsed,
                    "ref": ref_norm[:80],
                    "hyp": hyp_norm[:80],
                })

                wer_pct = f"{sample_wer*100:.1f}%"
                cer_pct = f"{sample_cer*100:.1f}%"
                print(f"  [{sample['language']}] {os.path.basename(wav_path)}: WER={wer_pct} CER={cer_pct} ({elapsed:.1f}s)")

                if sample_wer > 0.5:
                    print(f"    REF: {ref_norm[:100]}")
                    print(f"    HYP: {hyp_norm[:100]}")

            except Exception as e:
                print(f"  [{sample['language']}] {wav_file}: ERROR {e}")

    # Summary table
    print("\n" + "=" * 110)
    print("BENCHMARK RESULTS")
    print("=" * 110)
    print(f"{'Model':<20} {'Language':<10} {'File':<18} {'WER%':>8} {'CER%':>8} {'Time(s)':>8}")
    print("-" * 110)

    for r in results:
        print(f"{r['model']:<20} {r['language']:<10} {r['file']:<18} {r['wer']*100:>7.1f}% {r['cer']*100:>7.1f}% {r['elapsed']:>7.1f}")

    # Per-model averages
    print("-" * 110)
    for model in MODELS:
        model_results = [r for r in results if r["model"] == model]
        if not model_results:
            continue
        avg_wer = sum(r["wer"] for r in model_results) / len(model_results)
        avg_cer = sum(r["cer"] for r in model_results) / len(model_results)
        avg_time = sum(r["elapsed"] for r in model_results) / len(model_results)
        print(f"{model:<20} {'AVG':<10} {'':18} {avg_wer*100:>7.1f}% {avg_cer*100:>7.1f}% {avg_time:>7.1f}")

    # Per-model per-language averages
    print("\n--- Average WER by Language ---")
    for model in MODELS:
        model_results = [r for r in results if r["model"] == model]
        langs = sorted(set(r["language"] for r in model_results))
        for lang in langs:
            lang_results = [r for r in model_results if r["language"] == lang]
            avg_wer = sum(r["wer"] for r in lang_results) / len(lang_results)
            print(f"  {model:<20} {lang:<10} WER={avg_wer*100:.1f}%")

    # Save results
    results_path = os.path.join(BENCHMARK_DIR, "results.json")
    with open(results_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {results_path}")


if __name__ == "__main__":
    main()

```

### File: benchmark\samples.json
```json
[
  {
    "file": "audio/polish_0.opus",
    "language": "polish",
    "transcript": "staliśmy wszyscy bezradni wobec tej szalejącej furii złości która sama siebie trawiła i pożerała z ubolewaniem patrzyliśmy na smutny przebieg tego paroksyzmu i z pewną ulgą wróciliśmy do naszych zajęć gdy żałosny ten proces dobiegł swego naturalnego końca"
  },
  {
    "file": "audio/polish_1.opus",
    "language": "polish",
    "transcript": "nawet w obecności matki leżącej z zawiązaną głową na sofie nie mogły się powstrzymać robiły perskie oczko dawały sobie znaki mówiły niemym kolorowym alfabetem pełnym sekretnych znaczeń irytowało mnie to szydercze porozumienie ta migotliwa zmowa poza mymi plecami"
  },
  {
    "file": "audio/spanish_0.opus",
    "language": "spanish",
    "transcript": "y las almas buscando algún alivio se revuelven ansiosas y hacen el mundo que así resulta ser del dolor obra el dolor o la nada quien tenga corazón venga y escoja"
  },
  {
    "file": "audio/spanish_1.opus",
    "language": "spanish",
    "transcript": "cuando calla el dolor se oye a la muerte las alas tenebrosas batir en los profundos cual si fuesen las olas del mar de la ilusión en que los seres sin rumbo bogan donde se mecen frágiles barquillas las fugitivas formas"
  },
  {
    "file": "audio/french_0.opus",
    "language": "french",
    "transcript": "pendant le second siècle je fis serment d'ouvrir tous les trésors de la terre à quiconque me mettrait en liberté mais je ne fus pas plus heureux dans le troisième je promis de faire puissant monarque mon libérateur d'être toujours près de lui en esprit"
  },
  {
    "file": "audio/french_1.opus",
    "language": "french",
    "transcript": "non ta mort est certaine dit le génie choisis seulement de quelle sorte tu veux que je te fasse mourir le pêcheur le voyant dans la résolution de le tuer en eut une douleur extrême non pas tant pour l'amour de lui qu'à cause de ses trois enfants dont il plaignait la misère où ils allaient être réduits par sa mort"
  },
  {
    "file": "audio/german_0.opus",
    "language": "german",
    "transcript": "denken sie soeben weilten meine gedanken bei ihnen in adelaide und ich wünschte mir sie herzaubern zu können nun der zauber ist gelungen lachte münchhausen da bin ich und was mich herführt"
  },
  {
    "file": "audio/german_1.opus",
    "language": "german",
    "transcript": "also bei ihren technischen kenntnissen und ihrer erfindungsgabe auf diesem gebiet glaubt der lord keinen besseren ingenieur und kapitän für sein weltschiff finden zu können als sie"
  }
]
```

### File: docs\example_transcript.md
```md
---
schema: openoats/v1
title: "Notification System: Scope and Launch Plan"
date: 2026-03-18T10:30:00+01:00
duration: 11
participants:
  - You
  - Them
recorder: Szymon Sypniewicz
tags:
  - product
  - notifications
  - launch
language: en
engine: parakeet-tdt-v2
app: meet
---

# Notification System: Scope and Launch Plan

## Summary

Discussed the scope and timeline for shipping the in-app notification system. The original plan included real-time push notifications, email digests, and in-app alerts, but the team decided to cut email digests from v1 to avoid the deliverability rabbit hole (SPF, DKIM, reputation management). The notification system will ship with in-app alerts and optional browser push notifications only. Target launch is March 28. A soft rollout to beta users will happen on March 25, with three days of monitoring before the public release. The backend will use a simple polling architecture rather than WebSockets to keep infrastructure costs flat.

## Action Items

- [ ] Write the notification preferences UI component [owner:: You] [due:: 2026-03-21]
- [ ] Set up the notifications database table and API endpoints [owner:: Them] [due:: 2026-03-22]
- [ ] Deploy notification service to staging [owner:: Them] [due:: 2026-03-24]
- [ ] Draft the changelog entry for the notification feature [owner:: You] [due:: 2026-03-25]
- [ ] Run load test simulating 500 concurrent users polling for notifications [owner:: Them] [due:: 2026-03-25]
- [ ] Coordinate with beta users for soft rollout [owner:: You] [due:: 2026-03-25]

## Decisions

- Email digests cut from v1, will revisit in v1.1
- Polling architecture instead of WebSockets for notifications
- 30-second polling interval as default, configurable per user
- Soft rollout to beta users on March 25, public launch March 28
- Notifications auto-expire after 30 days

## Transcript

[00:00:00] **You:** Morning. I wanted to nail down the notification system scope before the weekend so we can start building Monday.

[00:00:06] **Them:** Good timing. I was actually sketching out the data model last night. I think we are overcomplicating this.

[00:00:12] **You:** How so?

[00:00:14] **Them:** The original spec has three channels: in-app alerts, browser push, and email digests. The first two are straightforward. Email digests are a completely different beast. We need a transactional email provider, SPF records, DKIM signing, domain reputation management. It is a whole project on its own.

[00:00:32] **You:** Yeah, I had that thought too. The email setup alone could take a week if we hit deliverability issues.

[00:00:38] **Them:** Exactly. And honestly, who reads email digests? Our users live in the app. If we ship in-app alerts and browser push, that covers 95% of the use case.

[00:00:48] **You:** I agree. Let's cut email digests from v1. We can revisit it in v1.1 if users actually ask for it.

[00:00:55] **Them:** Good. Now, for the delivery mechanism. I know WebSockets are the trendy choice, but I think simple polling is better for us right now.

[00:01:04] **You:** Because of infrastructure cost?

[00:01:07] **Them:** Partly. WebSocket connections are persistent. If we have a thousand users online, that is a thousand open connections our server is maintaining. Polling lets us stay on a basic HTTP setup. No special infrastructure, no connection management, no reconnection logic on the client.

[00:01:22] **You:** What polling interval are you thinking?

[00:01:25] **Them:** 30 seconds default. Fast enough that notifications feel responsive, infrequent enough that we are not hammering the server. We can let power users configure it down to 10 seconds if they want.

[00:01:37] **You:** That sounds reasonable. At 30 seconds, even with a few thousand active users, the load is trivial.

[00:01:44] **Them:** Right. And if we ever need real-time, we can swap polling for WebSockets later without changing the notification data model. The upgrade path is clean.

[00:01:53] **You:** Perfect. Let's talk timeline. We said end of March originally. Is that still realistic with the reduced scope?

[00:02:00] **Them:** More than realistic. Without email digests, I think we can have the backend done by the 22nd. That gives us time to test and do a soft rollout.

[00:02:09] **You:** I want to do a soft rollout to our beta users before the public launch. Maybe three days of monitoring.

[00:02:16] **Them:** So beta on the 25th, public on the 28th?

[00:02:19] **You:** Exactly. That gives us the weekend as a buffer too. If something breaks during beta, we have Monday and Tuesday to fix it.

[00:02:27] **Them:** Works for me. One thing I want to decide now: notification expiry. Do they stay forever or auto-delete?

[00:02:34] **You:** Auto-expire. Stale notifications are worse than no notifications. What is a reasonable window?

[00:02:40] **Them:** 30 days. Long enough that people do not miss things on vacation, short enough that the database does not grow forever.

[00:02:48] **You:** 30 days. Done. Let's split the work. I will take the frontend: the notification bell, the preferences panel, the dropdown list. You take the backend: database schema, API endpoints, the polling service.

[00:03:01] **Them:** Agreed. I will have the database table and endpoints ready by the 22nd so you can start integrating the frontend against real data.

[00:03:10] **You:** Good. And I need to write the changelog entry for this feature. I will do that on the 25th once we have the final build.

[00:03:18] **Them:** One more thing. We should run a load test before the public launch. I want to simulate 500 concurrent users polling at 30-second intervals and make sure response times stay under 200ms.

[00:03:30] **You:** Absolutely. Can you set that up as part of the staging deploy?

[00:03:34] **Them:** Yeah. I will deploy to staging on the 24th and run the load test on the 25th, same day as the beta rollout.

[00:03:42] **You:** Great. I will reach out to the beta group today and give them a heads up about the March 25th date.

[00:03:49] **Them:** Sounds good. I think we are in good shape.

[00:03:52] **You:** Agreed. Nice call on cutting the email digests. That would have derailed the whole timeline.

[00:03:58] **Them:** Every feature you do not build is a feature that cannot break.

[00:04:02] **You:** Words to live by. Talk Monday.

[00:04:05] **Them:** See you then.

```

### File: docs\meeting_format_spec.md
```md
# OpenOats Meeting Format Specification

**Version:** 1.0
**Status:** Draft
**License:** MIT

The key words "MUST", "MUST NOT", "SHOULD", "SHOULD NOT", and "MAY" in this document are to be interpreted as described in RFC 2119.

---

## Table of Contents

- [Overview](#overview)
- [File Naming](#file-naming)
- [YAML Frontmatter](#yaml-frontmatter)
- [Processing Stages](#processing-stages)
- [Body Structure](#body-structure)
- [Transcript Line Format](#transcript-line-format)
- [Speaker Model](#speaker-model)
- [Extensibility](#extensibility)
- [Parsing Guide](#parsing-guide)
- [Versioning](#versioning)
- [Complete Example: Stage 1+2 File (No LLM)](#complete-example-stage-12-file-no-llm)
- [Complete Example: Stage 1+2+3 File (After LLM Processing)](#complete-example-stage-123-file-after-llm-processing)
- [Conformance](#conformance)
- [Security Considerations](#security-considerations)
- [Design Rationale (Non-normative)](#design-rationale-non-normative)
- [Acknowledgments](#acknowledgments)

---

## Overview

The OpenOats Meeting Format (`.md`) is a structured Markdown format for meeting transcripts. It replaces OpenOats' plain `.txt` output with a file that is simultaneously human-readable, grep-friendly, Obsidian-native, and parseable by LLM agents.

### Goals

1. **Human-readable** in any text editor, Obsidian, or GitHub preview
2. **Agent-ready** for LLM consumption (Claude Code, Cursor, RAG pipelines)
3. **CLI-friendly** with predictable patterns for grep/ripgrep
4. **Obsidian-native** with Dataview-queryable frontmatter and Dataview TASK-queryable action items
5. **Adoptable** by other tools as a shared standard for meeting transcripts
6. **Incrementally structured** so files are useful at every processing stage

### Non-goals

- Replacing the JSONL session store (that stays for word-level data, RAG hits, etc.)
- Encoding audio playback offsets with sub-second precision (use JSONL for that)
- Handling real-time streaming (this format describes the finished artifact)

---

## File Naming

Filenames MUST be valid UTF-8. The kebab-case title portion MUST contain only ASCII characters `[a-z0-9-]`. If the title contains non-ASCII characters that produce an empty slug after conversion, use the fallback title `meeting`. The title portion SHOULD NOT exceed 60 characters.

```
YYYY-MM-DD-HHMM-kebab-case-title.md
```

Examples:
```
2026-03-20-1400-weekly-product-sync.md
2026-03-20-0930-investor-update.md
2026-03-21-1600-onboarding-call.md
```

Rules:
- Date and time MUST be the meeting start time in local time
- Time MUST be 24-hour, no separator between hours and minutes
- Title MUST be kebab-case, lowercase, ASCII only
- Filenames MUST NOT contain spaces (CLI-friendly)
- Lexical sort = chronological sort
- The filename is the file's unique identifier. No UUID field needed.
- If a file with the generated name already exists, implementations SHOULD append `-2`, `-3`, etc. before `.md`.

When the app cannot determine a title (no LLM post-processing, no calendar integration), use a fallback:
```
2026-03-20-1400-meeting.md
```

---

## YAML Frontmatter

Every file starts with a YAML frontmatter block.

### Field Reference

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `schema` | string | Yes | Format identifier. Always `openoats/v1` for this version. |
| `title` | string | Yes | Meeting title. Auto-generated from conversation topic, calendar event, or user edit. The H1 heading in the body MUST be identical to the `title` frontmatter value (after YAML string parsing). |
| `date` | ISO 8601 datetime | Yes | Meeting start time. Include timezone offset when available (e.g., `2026-03-20T14:00:00+01:00`). Omit timezone only if unknown. |
| `duration` | integer | Yes | Meeting duration in minutes, rounded to nearest minute. MUST be a positive integer (>= 1). |
| `participants` | string array | Yes | List of participant names. Default: `["You", "Them"]`. MUST contain at least one entry. See Speaker Model below. |
| `recorder` | string | No | Name of the person who recorded the meeting. Maps the speaker `You` to a real identity. The app SHOULD set this automatically from the system user name. |
| `tags` | string array | No | Topic tags. Auto-generated by LLM or user-assigned. Plain strings, no `#` prefix. |
| `language` | string | No | BCP 47 language code (e.g., `en`, `pl`, `de`). Defaults to `en` if omitted. |
| `engine` | string | No | ASR backend used for transcription (e.g., `parakeet-tdt-v2`, `qwen3-asr`, `whisper-large-v3`, `11labs-scribe-2`). |
| `app` | string | No | Detected meeting application, lowercase (e.g., `zoom`, `teams`, `meet`, `slack`, `facetime`). Omit if not detected. |
| `x_*` | any | No | Extension namespace. Any field prefixed with `x_` is valid. See Extensibility. |

### Frontmatter Rules

1. **UTF-8 without BOM, LF line endings.** Files MUST be encoded as UTF-8 without BOM. Lines MUST use LF (`\n`) line endings.
2. **YAML arrays, never comma-separated strings.** Array fields MUST use YAML array syntax (either inline `tags: [product, roadmap]` or block list with `- item` entries), not a comma-separated string like `tags: "product, roadmap"`.
3. **Plain text in frontmatter, wikilinks in body.** Frontmatter fields MUST NOT contain wikilink syntax (`[[Person Name]]`).
4. **Flat structure, no nesting.** Frontmatter MUST NOT use nested YAML objects. Dataview cannot query nested YAML objects without DataviewJS.
5. **Keep under 20 lines.** Frontmatter SHOULD be scannable and SHOULD NOT exceed 20 lines.
6. **The `title` field MUST always be quoted in YAML.** Unquoted titles risk silent coercion by YAML parsers (`yes` becomes boolean, `null` becomes empty, `#` starts a comment that truncates the value).
7. **Consistent types across files.** If `participants` is an array in one file, it MUST be an array in all files.

### Minimal Frontmatter (Stage 1+2, no LLM)

```yaml
---
schema: openoats/v1
title: "Meeting"
date: 2026-03-20T14:00:00+01:00
duration: 32
participants:
  - You
  - Them
engine: parakeet-tdt-v2
---
```

### Full Frontmatter (Stage 3, after LLM processing)

```yaml
---
schema: openoats/v1
title: "Q1 Launch Planning"
date: 2026-03-20T14:00:00+01:00
duration: 47
participants:
  - You
  - Them
recorder: Szymon Sypniewicz
tags:
  - product
  - launch
  - roadmap
language: en
engine: parakeet-tdt-v2
app: zoom
---
```

---

## Processing Stages

OpenOats produces this file in stages. Stage 2 refines Stage 1 output in-place (filler removal, punctuation, speaker correction). Stage 3 inserts new sections without modifying what Stage 1+2 wrote.

### Stage 1: Transcription

Raw ASR output. Produces a file with:
- Frontmatter: `schema`, `title` (fallback), `date`, `duration`, `participants` (`You`/`Them`), `engine`
- Body: `# Title` and `## Transcript` only

### Stage 2: Post-processing

Cleanup applied to Stage 1 output:
- Filler word removal (uh, um, like, you know)
- Punctuation and capitalization correction
- Speaker attribution corrections (echo cancellation artifacts)
- Enrichment from available context (meeting app name from detection, title from conversation state)

Stage 2 modifies the transcript text in-place and may update frontmatter fields (`title`, `app`). The file structure is identical to Stage 1.

### Stage 3: Intelligence (optional, LLM)

User triggers LLM post-processing. The LLM reads the Stage 1+2 file and generates:
- `## Summary` section
- `## Action Items` section
- `## Decisions` section (if applicable)
- `tags` array in frontmatter

These sections are inserted between `# Title` and `## Transcript`. The transcript itself is not modified.

---

## Body Structure

The body follows the title-first, transcript-last principle. Synthesized content (summary, action items, decisions) goes at the top because LLMs weight the beginning and end of documents more heavily, and humans scanning the file want the high-signal content first.

### Section Order

```
# Title

## Summary              <- Stage 3 only (LLM-generated)

## Action Items         <- Stage 3 only (LLM-generated)

## Decisions            <- Stage 3 only (LLM-generated, optional)

## Transcript           <- Stage 1+2 (always present)
```

### Required vs Optional Sections

| Section | Required | Added by |
|---------|----------|----------|
| `# Title` | Yes | Stage 1 |
| `## Transcript` | Yes | Stage 1+2 |
| `## Summary` | No | Stage 3 (LLM) |
| `## Action Items` | No | Stage 3 (LLM) |
| `## Decisions` | No | Stage 3 (LLM) |

A Stage 1+2 file (no LLM post-processing) contains only the title heading and the transcript section. This is a complete, valid file.

A Stage 3 file has the Summary, Action Items, and Decisions sections inserted between the title and the transcript.

Custom `## ` sections are permitted. They MUST appear between `## Decisions` (or `# Title` if no Stage 3 sections exist) and `## Transcript`. Parsers MUST ignore sections they do not recognize.

### Section Details

#### `# Title`

The H1 heading matches the `title` frontmatter field. It appears once, at the top of the body.

```markdown
# Q1 Launch Planning
```

#### `## Summary`

One to three paragraphs. No bullet points in the summary. Written in past tense, describing what happened and what was decided.

```markdown
## Summary

The team discussed moving the v1.0 launch from May 1 to April 15 to stay ahead of
TranscriptPro's desktop release. Engineering confirmed the encryption module is
production-ready but recommended deferring collaborative editing to v1.1 due to CRDT
complexity. The marketing site will lead with privacy-first messaging.
```

#### `## Action Items`

Standard Markdown checkboxes with Obsidian Dataview inline fields for `owner` and `due`.

```markdown
## Action Items

- [ ] Finalize launch announcement blog post [owner:: You] [due:: 2026-03-25]
- [ ] Run load testing on SQLite concurrency [owner:: Them] [due:: 2026-03-28]
- [ ] Send revised timeline to stakeholders [owner:: You] [due:: 2026-03-22]
```

Format per line:
```
- [ ] {task description} [owner:: {name}] [due:: {YYYY-MM-DD}]
```

Rules:
- `owner` MUST use the same name that appears in the `participants` array
- `due` MUST be an ISO 8601 date. Omit the `[due:: ...]` field entirely if no due date was discussed
- Completed items MUST use `[x]` or `[X]` instead of `[ ]`
- Each item MUST be a single line (no multi-line tasks)
- When both `owner` and `due` are present, `owner` MUST precede `due`
- Task descriptions MUST NOT contain Dataview inline field syntax (`[field:: value]`). All metadata goes in the trailing inline fields.

#### `## Decisions`

A flat bullet list of decisions made during the meeting. No IDs, no sub-structure.

```markdown
## Decisions

- Launch date set to April 15, moved up from May 1
- Collaborative editing deferred to v1.1
- Marketing hero copy leads with privacy, not open source
```

This section is optional even in Stage 3 output. If the LLM determines no decisions were made, omit the section entirely.

#### `## Transcript`

The raw transcript. Every utterance is a single line following the transcript line format described below.

---

## Transcript Line Format

Each line in the `## Transcript` section follows this pattern:

```
[HH:MM:SS] **Speaker Name:** Utterance text here.
```

Each utterance MUST be a single line, regardless of length. Line wrapping within an utterance is not supported.

### Formal Pattern

```
[{timestamp}] **{speaker}:** {text}
```

| Component | Format | Example |
|-----------|--------|---------|
| Timestamp | `HH:MM:SS` - hours, minutes, seconds, zero-padded | `[00:05:23]` |
| Speaker | Bold Markdown, followed by colon | `**You:**` |
| Text | Free text, single line | `I think we should launch earlier.` |

### Regex for Parsing

```regex
^\[(\d{2}:\d{2}:\d{2})\] \*\*(.+?):\*\* (.*)$
```

Capture groups:
1. Timestamp (`00:05:23`)
2. Speaker name (`You`)
3. Utterance text (`I think we should launch earlier.`), may be empty

> **Parser note:** Parsers SHOULD normalize speaker names by stripping Markdown bold markers (`**`) before comparison.

### Timestamp Rules

- Timestamps MUST be relative to meeting start, not wall-clock time
- Wall-clock time is in the frontmatter `date` field
- Format MUST always be `HH:MM:SS`, zero-padded (e.g., `00:01:05`, not `0:1:5`)
- For meetings over 24 hours (unlikely), hours MAY exceed 23: `[25:00:00]`

### Blank Lines

Utterances are separated by blank lines for readability:

```markdown
[00:00:00] **You:** Let's get started. The main topic is the launch timeline.

[00:00:08] **Them:** Sure. I looked at the latest metrics and usage is up significantly.

[00:00:15] **You:** That matches what I'm hearing from users too.
```

Parsers SHOULD treat blank lines between transcript entries as cosmetic. They carry no semantic meaning.

---

## Speaker Model

### Current State: You/Them

OpenOats captures two audio streams:
- **Microphone** (your voice) mapped to speaker `You`
- **System audio** (remote participants) mapped to speaker `Them`

There is no diarization between multiple remote speakers. All remote audio is attributed to `Them`.

In Stage 1+2 output, `participants` is always `["You", "Them"]` and the transcript uses `**You:**` and `**Them:**`.

### Future State: Named Participants

When OpenOats gains participant identification (via calendar integration, manual labeling, or diarization), the format supports named speakers with no structural changes:

```yaml
participants:
  - Alice Chen
  - Bob Martinez
  - Carol Wu
```

```markdown
[00:00:00] **Alice Chen:** Let's get started.

[00:00:08] **Bob Martinez:** Sure, I've got the slides ready.
```

The transition is seamless: `You`/`Them` are just speaker names. Named participants are also just speaker names. No format change required.

### Speaker Rules

1. Speaker names in transcript lines MUST match an entry in the `participants` array
2. Speaker names MUST be compared case-sensitively
3. Speaker names MUST NOT contain `*`, `:`, `[`, or `]` characters
4. When the app cannot identify individual remote speakers, all remote audio MUST use `Them`
5. The app SHOULD NOT invent names. Use `You`/`Them` until reliable identification exists

---

## Extensibility

Any field prefixed with `x_` in the frontmatter is a valid extension field. This namespace is reserved for tool-specific or user-specific metadata that is outside the core schema.

### Examples

```yaml
x_openoats_session: "session_2026-03-20_14-00-06"
x_openoats_template: "customer-discovery"
x_calendar_event_id: "abc123def456"
x_project: "OpenOats v1.0"
x_confidence: 0.92
```

### Extension Rules

1. Extension fields MUST start with `x_`
2. Extension fields are always optional. Implementations MUST NOT require any `x_` field for conformance.
3. Parsers MUST ignore extension fields they do not recognize
4. Tools SHOULD namespace their extensions: `x_toolname_field` (e.g., `x_openoats_session`)
5. Extension fields MUST follow all other frontmatter rules (flat structure,
... [TRUNCATED]
```

### File: scripts\build_swift_app.sh
```sh
#!/usr/bin/env bash
set -euo pipefail

# Build macOS .app for OpenOats (Swift)
# Usage:
#   ./scripts/build_swift_app.sh
#
# For CI / explicit identity:
#   CODESIGN_IDENTITY="Developer ID Application: ..." ./scripts/build_swift_app.sh
#
# For smoke checks without code signing or installation:
#   SKIP_SIGN=1 SKIP_INSTALL=1 ./scripts/build_swift_app.sh
#
# For notarization:
#   APPLE_ID="name@example.com"
#   APPLE_TEAM_ID="TEAMID123"
#   APPLE_APP_PASSWORD="xxxx-xxxx-xxxx-xxxx"

cd "$(dirname "$0")/.."
ROOT_DIR="$(pwd)"
SWIFT_DIR="$ROOT_DIR/OpenOats"
APP_NAME="OpenOats"
BUNDLE_ID="com.openoats.app"
SKIP_SIGN="${SKIP_SIGN:-0}"
SKIP_INSTALL="${SKIP_INSTALL:-0}"

echo "=== Building $APP_NAME (Swift) ==="

# Build release binary
cd "$SWIFT_DIR"
swift build -c release 2>&1
BINARY_PATH=".build/release/OpenOats"

if [[ ! -f "$BINARY_PATH" ]]; then
  echo "Build failed: binary not found at $BINARY_PATH"
  exit 1
fi

echo "Binary built: $BINARY_PATH"

# Create .app bundle
APP_DIR="$ROOT_DIR/dist/$APP_NAME.app"
rm -rf "$APP_DIR"
mkdir -p "$APP_DIR/Contents/MacOS"
mkdir -p "$APP_DIR/Contents/Resources"
mkdir -p "$APP_DIR/Contents/Frameworks"

# Copy binary
cp "$BINARY_PATH" "$APP_DIR/Contents/MacOS/OpenOats"

# Make the SwiftPM-built executable behave like a normal app bundle by
# teaching dyld to search the app's embedded Frameworks directory.
APP_BINARY="$APP_DIR/Contents/MacOS/OpenOats"
if ! otool -l "$APP_BINARY" | grep -Fq "@executable_path/../Frameworks"; then
  install_name_tool -add_rpath "@executable_path/../Frameworks" "$APP_BINARY"
  echo "Added app Frameworks rpath to executable"
fi

# Copy Info.plist
cp "$SWIFT_DIR/Sources/OpenOats/Info.plist" "$APP_DIR/Contents/Info.plist"

# Copy app icon
ICON_PATH="$SWIFT_DIR/Sources/OpenOats/Assets/AppIcon.icns"
if [[ -f "$ICON_PATH" ]]; then
  cp "$ICON_PATH" "$APP_DIR/Contents/Resources/AppIcon.icns"
  echo "App icon copied"
fi

# Copy Sparkle framework
SPARKLE_ARTIFACT_DIR="$SWIFT_DIR/.build/artifacts/sparkle"
SPARKLE_FW=$(find "$SPARKLE_ARTIFACT_DIR" -name "Sparkle.framework" -type d 2>/dev/null | head -1)
if [[ -n "$SPARKLE_FW" ]]; then
  cp -R "$SPARKLE_FW" "$APP_DIR/Contents/Frameworks/"
  echo "Sparkle.framework copied"
else
  echo "Warning: Sparkle.framework not found in build artifacts"
fi

# Add PkgInfo
echo -n "APPL????" > "$APP_DIR/Contents/PkgInfo"

echo "App bundle created: $APP_DIR"

if [[ "$SKIP_SIGN" == "1" ]]; then
  echo "Skipping code signing"
else
  # Auto-detect signing identity if not set
  if [[ -z "${CODESIGN_IDENTITY:-}" ]]; then
    CODESIGN_IDENTITY=$(security find-identity -v -p codesigning | grep "Developer ID Application" | head -1 | sed 's/.*"\(.*\)"/\1/' || true)
    if [[ -z "$CODESIGN_IDENTITY" ]]; then
      CODESIGN_IDENTITY=$(security find-identity -v -p codesigning | grep "Apple Development" | head -1 | sed 's/.*"\(.*\)"/\1/' || true)
    fi
  fi

  # Sign the app
  if [[ -n "${CODESIGN_IDENTITY:-}" ]]; then
    ENTITLEMENTS="$SWIFT_DIR/Sources/OpenOats/OpenOats.entitlements"
    echo "Signing with: $CODESIGN_IDENTITY"

    # Sign Sparkle components inside-out (innermost first)
    SPARKLE_FW_BUNDLE="$APP_DIR/Contents/Frameworks/Sparkle.framework"
    if [[ -d "$SPARKLE_FW_BUNDLE" ]]; then
      # Sign XPC service executables, then their bundles
      for xpc in "$SPARKLE_FW_BUNDLE"/Versions/B/XPCServices/*.xpc; do
        if [[ -d "$xpc" ]]; then
          codesign --force --options runtime --sign "$CODESIGN_IDENTITY" --timestamp "$xpc/Contents/MacOS/$(basename "${xpc%.xpc}")"
          codesign --force --options runtime --sign "$CODESIGN_IDENTITY" --timestamp "$xpc"
        fi
      done

      # Sign Autoupdate helper
      AUTOUPDATE="$SPARKLE_FW_BUNDLE/Versions/B/Autoupdate"
      if [[ -f "$AUTOUPDATE" ]]; then
        codesign --force --options runtime --sign "$CODESIGN_IDENTITY" --timestamp "$AUTOUPDATE"
      fi

      # Sign Updater.app
      UPDATER_APP="$SPARKLE_FW_BUNDLE/Versions/B/Updater.app"
      if [[ -d "$UPDATER_APP" ]]; then
        codesign --force --options runtime --sign "$CODESIGN_IDENTITY" --timestamp "$UPDATER_APP/Contents/MacOS/Updater"
        codesign --force --options runtime --sign "$CODESIGN_IDENTITY" --timestamp "$UPDATER_APP"
      fi

      # Sign the framework dylib, then the framework bundle
      codesign --force --options runtime --sign "$CODESIGN_IDENTITY" --timestamp "$SPARKLE_FW_BUNDLE/Versions/B/Sparkle"
      codesign --force --options runtime --sign "$CODESIGN_IDENTITY" --timestamp "$SPARKLE_FW_BUNDLE"
    fi

    # Sign the main app bundle
    codesign --force --options runtime \
      --sign "$CODESIGN_IDENTITY" \
      --entitlements "$ENTITLEMENTS" \
      --timestamp \
      "$APP_DIR"

    echo "Code signing complete"
    codesign -vvv "$APP_DIR"
  else
    echo "Warning: No signing identity found. App will be unsigned."
  fi
fi

if [[ "$SKIP_INSTALL" == "1" ]]; then
  echo "Skipping installation to /Applications"
else
  cp -R "$APP_DIR" /Applications/
  echo "Installed to /Applications/$APP_NAME.app"
fi

echo "=== Build complete ==="

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
