---
id: github.com-fal-ai-community-skills-be23c217-knowle
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:49.124432
---

# KNOWLEDGE EXTRACT: github.com_fal-ai-community_skills_be23c217
> **Extracted on:** 2026-04-01 08:43:38
> **Source:** D:/LongLeo/AI OS CORP/AI OS/core/security/QUARANTINE/KI-BATCH-20260331205007519747/github.com_fal-ai-community_skills_be23c217

---

## File: `.gitignore`
```
node_modules/
.DS_Store
*.zip
.env
```

## File: `README.md`
```markdown
# fal.ai Skills

Agent skills for [fal.ai](https://fal.ai) — ready-to-use bash scripts that let AI agents generate images, videos, audio, 3D models, and more.

Compatible with [Claude.ai Projects](https://claude.ai), [Claude Code](https://claude.ai/claude-code), and any agent platform that supports the community skills format.

## Skills

### Core

| Skill | Description | Scripts |
|-------|-------------|---------|
| **[fal-generate](skills/claude.ai/fal-generate)** | Generate images and videos with queue support | `generate.sh`, `upload.sh`, `search-models.sh`, `get-schema.sh` |
| **[fal-image-edit](skills/claude.ai/fal-image-edit)** | Edit images — style transfer, object removal, background change, inpainting | `edit-image.sh` |
| **[fal-audio](skills/claude.ai/fal-audio)** | Text-to-speech and speech-to-text | `text-to-speech.sh`, `speech-to-text.sh` |
| **[fal-upscale](skills/claude.ai/fal-upscale)** | Upscale and enhance image resolution | `upscale.sh` |

### Specialized Models

| Skill | Description | Scripts |
|-------|-------------|---------|
| **[fal-kling-o3](skills/claude.ai/fal-kling-o3)** | Kling O3 — highest quality photorealistic images and video editing | `kling-generate.sh`, `kling-video.sh` |
| **[fal-realtime](skills/claude.ai/fal-realtime)** | Real-time/streaming generation (~0.3s per image) | `realtime.sh` |

### Video & Animation

| Skill | Description | Scripts |
|-------|-------------|---------|
| **[fal-video-edit](skills/claude.ai/fal-video-edit)** | Edit videos — remix, upscale, remove background, add audio | `edit-video.sh`, `video-audio.sh` |
| **[fal-lip-sync](skills/claude.ai/fal-lip-sync)** | Talking head, lip sync, live portrait | `talking-head.sh`, `lip-sync.sh` |

### Creative & Production

| Skill | Description | Scripts |
|-------|-------------|---------|
| **[fal-3d](skills/claude.ai/fal-3d)** | Text/image to 3D model generation | `generate-3d.sh` |
| **[fal-vision](skills/claude.ai/fal-vision)** | Image analysis — segment, detect, OCR, describe | `analyze.sh` |
| **[fal-restore](skills/claude.ai/fal-restore)** | Restore image quality — deblur, denoise, fix faces | `restore.sh` |
| **[fal-tryon](skills/claude.ai/fal-tryon)** | Virtual clothing try-on | `tryon.sh` |
| **[fal-train](skills/claude.ai/fal-train)** | Train custom LoRA models | `train.sh` |

### Platform & Utilities

| Skill | Description | Scripts |
|-------|-------------|---------|
| **[fal-platform](skills/claude.ai/fal-platform)** | Pricing, usage tracking, cost estimation, API key setup | `pricing.sh`, `usage.sh`, `estimate-cost.sh`, `setup.sh`, `requests.sh` |
| **[fal-workflow](skills/claude.ai/fal-workflow)** | Create multi-step model pipelines | `create-workflow.sh` |

## Setup

### 1. Get your API key

Sign up at [fal.ai/dashboard/keys](https://fal.ai/dashboard/keys).

### 2. Set the key

```bash
export FAL_KEY=your_key_here
```

Or use the built-in setup:

```bash
bash scripts/generate.sh --add-fal-key
```

### 3. Use with Claude.ai

Upload skills to a Claude.ai Project:
1. Go to your project settings
2. Add skills from the `claude.ai/` directory
3. Make sure `*.fal.ai` is in your allowed domains under `claude.ai/settings/capabilities`

### 4. Use with any agent

Every skill is a standalone bash script. Call them directly:

```bash
# Generate an image
bash skills/claude.ai/fal-generate/scripts/generate.sh \
  --prompt "A serene mountain landscape" \
  --model "fal-ai/nano-banana-pro"

# Generate a video
bash skills/claude.ai/fal-generate/scripts/generate.sh \
  --prompt "Ocean waves crashing on rocks" \
  --model "fal-ai/veo3.1" \
  --async

# Edit an image
bash skills/claude.ai/fal-image-edit/scripts/edit-image.sh \
  --image-url "https://example.com/photo.jpg" \
  --prompt "Convert to anime style" \
  --operation style

# Text to speech
bash skills/claude.ai/fal-audio/scripts/text-to-speech.sh \
  --text "Hello world"

# Search for models
bash skills/claude.ai/fal-generate/scripts/search-models.sh \
  --query "text to video"
```

## Skill Format

Each skill follows the community skills standard:

```
claude.ai/
└── skill-name/
    ├── SKILL.md          # Metadata + documentation (YAML frontmatter)
    └── scripts/
        └── script.sh     # Executable bash script
```

The `SKILL.md` contains a YAML frontmatter with `name`, `description`, and `metadata`, followed by usage documentation that the agent reads to understand how to use the skill.

## License

MIT
```

## File: `skills/claude.ai/fal-3d/SKILL.md`
```markdown
---
name: fal-3d
description: Generate 3D models from text or images. Use when the user requests "Create 3D model", "Text to 3D", "Image to 3D", "3D generation", "Generate mesh", "3D asset".
metadata:
  author: fal-ai
  version: "1.0.0"
---

# fal-3d

Generate 3D models (GLB/OBJ/PLY) from text descriptions or images using fal.ai.

## Scripts

| Script | Purpose |
|--------|---------|
| `generate-3d.sh` | Generate a 3D model from text or image |

## Usage

### Image to 3D
```bash
./scripts/generate-3d.sh --image-url "https://example.com/object.jpg" --model fal-ai/hunyuan3d-v3/image-to-3d
```

### Text to 3D
```bash
./scripts/generate-3d.sh --prompt "A medieval sword with ornate handle" --model fal-ai/meshy/v6/text-to-3d
```

## Arguments

| Argument | Description | Required |
|----------|-------------|----------|
| `--image-url` | URL of image to convert to 3D | Yes (or --prompt) |
| `--prompt` / `-p` | Text description for text-to-3D | Yes (or --image-url) |
| `--model` / `-m` | Model endpoint | No (default: fal-ai/hunyuan3d-v3/image-to-3d) |
| `--param` | Extra param as key=value (repeatable) | No |

## Finding Models

To discover the best and latest 3D generation models, use the search API:

```bash
# Search for image-to-3D models
bash /mnt/skills/user/fal-generate/scripts/search-models.sh --category "image-to-3d"

# Search for text-to-3D models
bash /mnt/skills/user/fal-generate/scripts/search-models.sh --query "text to 3d"
```

Or use the `search_models` MCP tool with relevant keywords like "3d", "mesh", "image-to-3d".

## Tips

- For best results from images: use a clear photo with a single object on a plain background
- Remove background first if needed (use fal-image-edit or fal-generate with birefnet)
- Simple, well-defined objects work best — complex scenes don't reconstruct well yet
- 3D generation takes 1-5 minutes — jobs use the queue API

## Output Format
```json
{
  "mesh": {
    "url": "https://fal.media/files/.../model.glb",
    "content_type": "model/gltf-binary",
    "file_name": "model.glb"
  }
}
```
```

## File: `skills/claude.ai/fal-3d/scripts/generate-3d.sh`
```bash
#!/bin/bash
set -e

# generate-3d.sh — Generate a 3D model from text or image

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
MODEL="fal-ai/hunyuan3d-v3/image-to-3d"
IMAGE_URL=""
PROMPT=""
EXTRA_PARAMS=""
POLL_INTERVAL=5
TIMEOUT=600

show_help() {
  echo "Usage: $0 [--image-url URL | --prompt TEXT] [options]"
  echo ""
  echo "Options:"
  echo "  --image-url URL    Image to convert to 3D"
  echo "  --prompt, -p TEXT  Text description for text-to-3D"
  echo "  --model, -m MODEL  Model (default: $MODEL)"
  echo "  --param KEY=VALUE  Extra parameter (repeatable)"
  echo "  --add-fal-key KEY  Store FAL_KEY in .env"
  echo "  --help, -h         Show this help"
  exit 0
}

[ -f "$SCRIPT_DIR/../.env" ] && source "$SCRIPT_DIR/../.env"
[ -f ".env" ] && source ".env"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --image-url) IMAGE_URL="$2"; shift 2;;
    --prompt|-p) PROMPT="$2"; shift 2;;
    --model|-m) MODEL="$2"; shift 2;;
    --param) EXTRA_PARAMS="$EXTRA_PARAMS, \"$(echo "$2" | cut -d= -f1)\": \"$(echo "$2" | cut -d= -f2)\""; shift 2;;
    --add-fal-key) echo "FAL_KEY=$2" > .env; echo "API key saved." >&2; exit 0;;
    --help|-h) show_help;;
    *) echo "Unknown: $1" >&2; exit 1;;
  esac
done

if [ -z "$FAL_KEY" ]; then echo "Error: FAL_KEY not set." >&2; exit 1; fi
if [ -z "$IMAGE_URL" ] && [ -z "$PROMPT" ]; then echo "Error: --image-url or --prompt required" >&2; exit 1; fi

# Build payload
if [ -n "$IMAGE_URL" ]; then
  PAYLOAD="{\"image_url\": \"$IMAGE_URL\"$EXTRA_PARAMS}"
else
  PAYLOAD="{\"prompt\": \"$PROMPT\"$EXTRA_PARAMS}"
fi

echo "Submitting 3D generation to $MODEL..." >&2
SUBMIT=$(curl -s -X POST "https://queue.fal.run/$MODEL" \
  -H "Authorization: Key $FAL_KEY" \
  -H "Content-Type: application/json" \
  -d "$PAYLOAD")

REQUEST_ID=$(echo "$SUBMIT" | jq -r '.request_id // empty')
if [ -z "$REQUEST_ID" ]; then echo "Error: $SUBMIT" >&2; exit 1; fi

echo "Waiting (request: $REQUEST_ID) — 3D generation takes 1-5 min..." >&2
ELAPSED=0
while [ "$ELAPSED" -lt "$TIMEOUT" ]; do
  STATUS=$(curl -s "https://queue.fal.run/$MODEL/requests/$REQUEST_ID/status?logs=1" \
    -H "Authorization: Key $FAL_KEY")
  STATE=$(echo "$STATUS" | jq -r '.status')
  case "$STATE" in
    COMPLETED)
      echo "Completed!" >&2
      curl -s "https://queue.fal.run/$MODEL/requests/$REQUEST_ID" \
        -H "Authorization: Key $FAL_KEY" | jq .
      exit 0;;
    FAILED) echo "Failed: $STATUS" >&2; exit 1;;
    *) echo "  $STATE (${ELAPSED}s)" >&2;;
  esac
  sleep "$POLL_INTERVAL"
  ELAPSED=$((ELAPSED + POLL_INTERVAL))
done
echo "Timed out. Request ID: $REQUEST_ID" >&2; exit 1
```

## File: `skills/claude.ai/fal-audio/SKILL.md`
```markdown
---
name: fal-audio
description: Text-to-speech and speech-to-text using fal.ai audio models. Use when the user requests "Convert text to speech", "Transcribe audio", "Generate voice", "Speech to text", "TTS", "STT", or similar audio tasks.
metadata:
  author: fal-ai
  version: "1.0.0"
---

# fal.ai Audio

Text-to-speech and speech-to-text using state-of-the-art audio models on fal.ai.

## How It Works

1. User provides text (for TTS) or audio URL (for STT)
2. Script selects appropriate model
3. Sends request to fal.ai API
4. Returns audio URL (TTS) or transcription text (STT)

## Finding Models

To discover the best and latest audio models, use the search API:

```bash
# Search for text-to-speech models
bash /mnt/skills/user/fal-generate/scripts/search-models.sh --category "text-to-speech"

# Search for speech-to-text models
bash /mnt/skills/user/fal-generate/scripts/search-models.sh --category "speech-to-text"

# Search for music generation models
bash /mnt/skills/user/fal-generate/scripts/search-models.sh --query "music generation"
```

Or use the `search_models` MCP tool with relevant keywords like "tts", "speech", "music".

## Usage

### Text-to-Speech

```bash
bash /mnt/skills/user/fal-audio/scripts/text-to-speech.sh [options]
```

**Arguments:**
- `--text` - Text to convert to speech (required)
- `--model` - TTS model (defaults to `fal-ai/minimax/speech-2.8-turbo`)
- `--voice` - Voice ID or name (model-specific)

**Examples:**

```bash
# Basic TTS (fast, good quality)
bash /mnt/skills/user/fal-audio/scripts/text-to-speech.sh \
  --text "Hello, welcome to the future of AI."

# High quality with MiniMax HD
bash /mnt/skills/user/fal-audio/scripts/text-to-speech.sh \
  --text "This is premium quality speech." \
  --model "fal-ai/minimax/speech-2.8-hd"

# Natural voices with ElevenLabs
bash /mnt/skills/user/fal-audio/scripts/text-to-speech.sh \
  --text "Natural sounding voice generation" \
  --model "fal-ai/elevenlabs/tts/eleven-v3"

# Multi-language TTS
bash /mnt/skills/user/fal-audio/scripts/text-to-speech.sh \
  --text "Bonjour, bienvenue dans le futur." \
  --model "fal-ai/chatterbox/text-to-speech/multilingual"
```

### Speech-to-Text

```bash
bash /mnt/skills/user/fal-audio/scripts/speech-to-text.sh [options]
```

**Arguments:**
- `--audio-url` - URL of audio file to transcribe (required)
- `--model` - STT model (defaults to `fal-ai/whisper`)
- `--language` - Language code (optional, auto-detected)

**Examples:**

```bash
# Transcribe with Whisper
bash /mnt/skills/user/fal-audio/scripts/speech-to-text.sh \
  --audio-url "https://example.com/audio.mp3"

# Transcribe with speaker diarization
bash /mnt/skills/user/fal-audio/scripts/speech-to-text.sh \
  --audio-url "https://example.com/meeting.mp3" \
  --model "fal-ai/elevenlabs/speech-to-text/scribe-v2"

# Transcribe specific language
bash /mnt/skills/user/fal-audio/scripts/speech-to-text.sh \
  --audio-url "https://example.com/spanish.mp3" \
  --language "es"
```

## MCP Tool Alternative

Use `search_models` MCP tool or `search-models.sh` to find the best current model, then call `mcp__fal-ai__generate` with the discovered `modelId`.

## Output

### Text-to-Speech Output
```
Generating speech...
Model: fal-ai/minimax/speech-2.8-turbo

Speech generated!

Audio URL: https://v3.fal.media/files/abc123/speech.mp3
Duration: 5.2s
```

### Speech-to-Text Output
```
Transcribing audio...
Model: fal-ai/whisper

Transcription complete!

Text: "Hello, this is the transcribed text from the audio file."
Duration: 12.5s
Language: en
```

## Present Results to User

### For TTS:
```
Here's the generated speech:

[Download audio](https://v3.fal.media/files/.../speech.mp3)

• Duration: 5.2s | Model: Maya TTS
```

### For STT:
```
Here's the transcription:

"Hello, this is the transcribed text from the audio file."

• Duration: 12.5s | Language: English
```

## Model Selection Tips

- **Text-to-Speech**: Search for `text-to-speech` category. Consider quality vs speed tradeoffs.
- **Text-to-Music**: Search for `music generation`. Some models specialize in vocals, others in instrumental.
- **Speech-to-Text**: Search for `speech-to-text` category. Consider whether you need speaker diarization or multi-language support.

## Troubleshooting

### Empty Audio
```
Error: Generated audio is empty

Check that your text is not empty and contains valid content.
```

### Unsupported Audio Format
```
Error: Audio format not supported

Supported formats: MP3, WAV, M4A, FLAC, OGG
Convert your audio to a supported format.
```

### Language Detection Failed
```
Warning: Could not detect language, defaulting to English

Specify the language explicitly with --language option.
```
```

## File: `skills/claude.ai/fal-audio/scripts/speech-to-text.sh`
```bash
#!/bin/bash

# fal.ai Speech-to-Text Script
# Usage: ./speech-to-text.sh --audio-url URL [--model MODEL] [--language LANG]
# Returns: JSON with transcription

set -e

FAL_API_ENDPOINT="https://fal.run"

# Default values
MODEL="fal-ai/whisper"
AUDIO_URL=""
LANGUAGE=""

# Check for --add-fal-key first
for arg in "$@"; do
    if [ "$arg" = "--add-fal-key" ]; then
        shift
        KEY_VALUE=""
        if [[ -n "$1" && ! "$1" =~ ^-- ]]; then
            KEY_VALUE="$1"
        fi
        if [ -z "$KEY_VALUE" ]; then
            echo "Enter your fal.ai API key:" >&2
            read -r KEY_VALUE
        fi
        if [ -n "$KEY_VALUE" ]; then
            grep -v "^FAL_KEY=" .env > .env.tmp 2>/dev/null || true
            mv .env.tmp .env 2>/dev/null || true
            echo "FAL_KEY=$KEY_VALUE" >> .env
            echo "FAL_KEY saved to .env" >&2
        fi
        exit 0
    fi
done

# Load .env if exists
if [ -f ".env" ]; then
    source .env 2>/dev/null || true
fi

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --audio-url)
            AUDIO_URL="$2"
            shift 2
            ;;
        --model)
            MODEL="$2"
            shift 2
            ;;
        --language)
            LANGUAGE="$2"
            shift 2
            ;;
        --help|-h)
            echo "fal.ai Speech-to-Text Script" >&2
            echo "" >&2
            echo "Usage:" >&2
            echo "  ./speech-to-text.sh --audio-url URL [options]" >&2
            echo "" >&2
            echo "Options:" >&2
            echo "  --audio-url     Audio URL to transcribe (required)" >&2
            echo "  --model         Model ID (default: fal-ai/whisper)" >&2
            echo "  --language      Language code (auto-detected if omitted)" >&2
            echo "  --add-fal-key   Setup FAL_KEY in .env" >&2
            exit 0
            ;;
        *)
            shift
            ;;
    esac
done

# Validate required inputs
if [ -z "$FAL_KEY" ]; then
    echo "Error: FAL_KEY not set" >&2
    echo "" >&2
    echo "Run: ./speech-to-text.sh --add-fal-key" >&2
    echo "Or:  export FAL_KEY=your_key_here" >&2
    exit 1
fi

if [ -z "$AUDIO_URL" ]; then
    echo "Error: --audio-url is required" >&2
    exit 1
fi

# Create temp directory
TEMP_DIR=$(mktemp -d)
trap 'rm -rf "$TEMP_DIR"' EXIT

echo "Transcribing audio..." >&2
echo "Model: $MODEL" >&2
echo "" >&2

# Build payload
if [ -n "$LANGUAGE" ]; then
    PAYLOAD=$(cat <<EOF
{
  "audio_url": "$AUDIO_URL",
  "language": "$LANGUAGE"
}
EOF
)
else
    PAYLOAD=$(cat <<EOF
{
  "audio_url": "$AUDIO_URL"
}
EOF
)
fi

# Make API request
RESPONSE=$(curl -s -X POST "$FAL_API_ENDPOINT/$MODEL" \
    -H "Authorization: Key $FAL_KEY" \
    -H "Content-Type: application/json" \
    -d "$PAYLOAD")

# Check for errors
if echo "$RESPONSE" | grep -q '"error"'; then
    ERROR_MSG=$(echo "$RESPONSE" | grep -o '"message":"[^"]*"' | head -1 | cut -d'"' -f4)
    if [ -z "$ERROR_MSG" ]; then
        ERROR_MSG=$(echo "$RESPONSE" | grep -o '"error":"[^"]*"' | cut -d'"' -f4)
    fi
    echo "Error: $ERROR_MSG" >&2
    exit 1
fi

echo "Transcription complete!" >&2
echo "" >&2

# Extract text
TEXT=$(echo "$RESPONSE" | grep -o '"text":"[^"]*"' | head -1 | cut -d'"' -f4)
echo "Text: $TEXT" >&2

# Output JSON for programmatic use
echo "$RESPONSE"
```

## File: `skills/claude.ai/fal-audio/scripts/text-to-speech.sh`
```bash
#!/bin/bash

# fal.ai Text-to-Speech Script
# Usage: ./text-to-speech.sh --text "..." [--model MODEL] [--voice VOICE]
# Returns: JSON with audio URL

set -e

FAL_API_ENDPOINT="https://fal.run"

# Default values
MODEL="fal-ai/minimax/speech-2.8-turbo"
TEXT=""
VOICE=""

# Check for --add-fal-key first
for arg in "$@"; do
    if [ "$arg" = "--add-fal-key" ]; then
        shift
        KEY_VALUE=""
        if [[ -n "$1" && ! "$1" =~ ^-- ]]; then
            KEY_VALUE="$1"
        fi
        if [ -z "$KEY_VALUE" ]; then
            echo "Enter your fal.ai API key:" >&2
            read -r KEY_VALUE
        fi
        if [ -n "$KEY_VALUE" ]; then
            grep -v "^FAL_KEY=" .env > .env.tmp 2>/dev/null || true
            mv .env.tmp .env 2>/dev/null || true
            echo "FAL_KEY=$KEY_VALUE" >> .env
            echo "FAL_KEY saved to .env" >&2
        fi
        exit 0
    fi
done

# Load .env if exists
if [ -f ".env" ]; then
    source .env 2>/dev/null || true
fi

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --text)
            TEXT="$2"
            shift 2
            ;;
        --model)
            MODEL="$2"
            shift 2
            ;;
        --voice)
            VOICE="$2"
            shift 2
            ;;
        --help|-h)
            echo "fal.ai Text-to-Speech Script" >&2
            echo "" >&2
            echo "Usage:" >&2
            echo "  ./text-to-speech.sh --text \"...\" [options]" >&2
            echo "" >&2
            echo "Options:" >&2
            echo "  --text          Text to convert (required)" >&2
            echo "  --model         Model ID (default: fal-ai/minimax/speech-2.8-turbo)" >&2
            echo "  --voice         Voice ID (model-specific)" >&2
            echo "  --add-fal-key   Setup FAL_KEY in .env" >&2
            exit 0
            ;;
        *)
            shift
            ;;
    esac
done

# Validate required inputs
if [ -z "$FAL_KEY" ]; then
    echo "Error: FAL_KEY not set" >&2
    echo "" >&2
    echo "Run: ./text-to-speech.sh --add-fal-key" >&2
    echo "Or:  export FAL_KEY=your_key_here" >&2
    exit 1
fi

if [ -z "$TEXT" ]; then
    echo "Error: --text is required" >&2
    exit 1
fi

# Create temp directory
TEMP_DIR=$(mktemp -d)
trap 'rm -rf "$TEMP_DIR"' EXIT

echo "Generating speech..." >&2
echo "Model: $MODEL" >&2
echo "" >&2

# Build payload
if [ -n "$VOICE" ]; then
    PAYLOAD=$(cat <<EOF
{
  "text": "$TEXT",
  "voice": "$VOICE"
}
EOF
)
else
    PAYLOAD=$(cat <<EOF
{
  "text": "$TEXT"
}
EOF
)
fi

# Make API request
RESPONSE=$(curl -s -X POST "$FAL_API_ENDPOINT/$MODEL" \
    -H "Authorization: Key $FAL_KEY" \
    -H "Content-Type: application/json" \
    -d "$PAYLOAD")

# Check for errors
if echo "$RESPONSE" | grep -q '"error"'; then
    ERROR_MSG=$(echo "$RESPONSE" | grep -o '"message":"[^"]*"' | head -1 | cut -d'"' -f4)
    if [ -z "$ERROR_MSG" ]; then
        ERROR_MSG=$(echo "$RESPONSE" | grep -o '"error":"[^"]*"' | cut -d'"' -f4)
    fi
    echo "Error: $ERROR_MSG" >&2
    exit 1
fi

echo "Speech generated!" >&2
echo "" >&2

# Extract audio URL
AUDIO_URL=$(echo "$RESPONSE" | grep -o '"url":"[^"]*"' | head -1 | cut -d'"' -f4)
echo "Audio URL: $AUDIO_URL" >&2

# Output JSON for programmatic use
echo "$RESPONSE"
```

## File: `skills/claude.ai/fal-generate/SKILL.md`
```markdown
---
name: fal-generate
description: Generate images and videos using fal.ai AI models with queue support. Use when the user requests "Generate image", "Create video", "Make a picture of...", "Text to image", "Image to video", "Search models", or similar generation tasks.
metadata:
  author: fal-ai
  version: "3.0.0"
---

# fal.ai Generate

Generate images and videos using state-of-the-art AI models on fal.ai.

## Scripts

| Script | Purpose |
|--------|---------|
| `generate.sh` | Generate images/videos (queue-based) |
| `upload.sh` | Upload local files to fal CDN |
| `search-models.sh` | Search and discover models |
| `get-schema.sh` | Get OpenAPI schema for any model |

## Queue System (Default)

All requests use the queue system by default for reliability:

```
User Request → Queue Submit → Poll Status → Get Result
                   ↓
              request_id
```

**Benefits:**
- Long-running tasks (video) won't timeout
- Can check status anytime
- Can cancel queued requests
- Results retrievable even if connection drops

## Generate Content

```bash
bash /mnt/skills/user/fal-generate/scripts/generate.sh [options]
```

### Basic Usage (Queue Mode)

```bash
# Image - submits to queue, waits for completion
bash generate.sh --prompt "A serene mountain landscape" --model "fal-ai/nano-banana-pro"

# Video - same, but takes longer
bash generate.sh --prompt "Ocean waves crashing" --model "fal-ai/veo3.1"

# Image-to-Video
bash generate.sh \
  --prompt "Camera slowly zooms in" \
  --model "fal-ai/kling-video/v2.6/pro/image-to-video" \
  --image-url "https://example.com/image.jpg"
```

### Async Mode (Return Immediately)

For long video jobs, use `--async` to get request_id immediately:

```bash
# Submit and return immediately
bash generate.sh --prompt "Epic battle scene" --model "fal-ai/veo3.1" --async

# Output:
# Request ID: abc123-def456
# Request submitted. Use these commands to check:
#   Status: ./generate.sh --status "abc123-def456" --model "fal-ai/veo3.1"
#   Result: ./generate.sh --result "abc123-def456" --model "fal-ai/veo3.1"
```

### Queue Operations

```bash
# Check status
bash generate.sh --status "request_id" --model "fal-ai/veo3.1"
# → IN_QUEUE (position: 3) | IN_PROGRESS | COMPLETED

# Get result (when COMPLETED)
bash generate.sh --result "request_id" --model "fal-ai/veo3.1"

# Cancel (only if still queued)
bash generate.sh --cancel "request_id" --model "fal-ai/veo3.1"
```

### Show Logs During Generation

```bash
bash generate.sh --prompt "A sunset" --model "fal-ai/nano-banana-pro" --logs
# Status: IN_QUEUE (position: 2)
# Status: IN_PROGRESS
#   > Loading model...
#   > Generating image...
# Status: COMPLETED
```

## File Upload

### Option 1: Auto-upload with --file

```bash
# Local file is automatically uploaded to fal CDN
bash generate.sh \
  --file "/path/to/photo.jpg" \
  --model "fal-ai/kling-video/v2.6/pro/image-to-video" \
  --prompt "Camera zooms in slowly"
```

### Option 2: Manual upload with upload.sh

```bash
# Upload first
URL=$(bash upload.sh --file "/path/to/photo.jpg")
# → https://v3.fal.media/files/xxx/photo.jpg

# Then generate
bash generate.sh --image-url "$URL" --model "..." --prompt "..."
```

### Option 3: Use existing URL

```bash
# Any public URL works
bash generate.sh --image-url "https://example.com/image.jpg" ...
```

**Supported file types:**
- Images: jpg, jpeg, png, gif, webp
- Videos: mp4, mov, webm
- Audio: mp3, wav, flac

**Upload flow (two-step):**
```
1. POST rest.alpha.fal.ai/vault/auth/token?storage_type=fal-cdn-v3
   → {"token": "...", "base_url": "https://v3b.fal.media"}

2. POST {base_url}/files/upload
   Authorization: Bearer {token}
   → {"access_url": "https://v3b.fal.media/files/..."}
```

**Max file size:** 100MB (simple upload)

## Arguments Reference

| Argument | Description | Default |
|----------|-------------|---------|
| `--prompt`, `-p` | Text description | (required) |
| `--model`, `-m` | Model ID | `fal-ai/nano-banana-pro` |
| `--image-url` | Input image URL for I2V | - |
| `--file`, `--image` | Local file (auto-uploads) | - |
| `--size` | `square`, `portrait`, `landscape` | `landscape_4_3` |
| `--num-images` | Number of images | 1 |

**Mode Options:**
| Argument | Description |
|----------|-------------|
| (default) | Queue mode - submit and poll until complete |
| `--async` | Submit to queue, return request_id immediately |
| `--sync` | Synchronous (not recommended for video) |
| `--logs` | Show generation logs while polling |

**Queue Operations:**
| Argument | Description |
|----------|-------------|
| `--status ID` | Check status of a queued request |
| `--result ID` | Get result of a completed request |
| `--cancel ID` | Cancel a queued request |

**Advanced:**
| Argument | Description | Default |
|----------|-------------|---------|
| `--poll-interval` | Seconds between status checks | 2 |
| `--timeout` | Max seconds to wait | 600 |
| `--lifecycle N` | Object expiration in seconds | - |
| `--schema [MODEL]` | Get OpenAPI schema | - |

## Finding Models

To discover the best and latest models, use the search API:

```bash
# Search by category
bash search-models.sh --category "text-to-image"
bash search-models.sh --category "text-to-video"
bash search-models.sh --category "image-to-video"

# Search by keyword
bash search-models.sh --query "flux"
bash search-models.sh --query "kling video"
```

Or use the `search_models` MCP tool with relevant keywords.

**Categories:** `text-to-image`, `image-to-image`, `text-to-video`, `image-to-video`, `text-to-speech`, `speech-to-text`

## Get Model Schema (OpenAPI)

**IMPORTANT:** Fetch schema to see exact parameters for any model.

```bash
# Get schema
bash get-schema.sh --model "fal-ai/nano-banana-pro"

# Show only input parameters
bash get-schema.sh --model "fal-ai/kling-video/v2.6/pro/image-to-video" --input

# Quick schema via generate.sh
bash generate.sh --schema "fal-ai/veo3.1"
```

**API Endpoint:**
```
https://fal.ai/api/openapi/queue/openapi.json?endpoint_id={model-id}
```

## Output

**Queue Submit Response:**
```json
{
  "request_id": "abc123-def456",
  "status": "IN_QUEUE",
  "response_url": "https://queue.fal.run/.../requests/abc123-def456",
  "status_url": "https://queue.fal.run/.../requests/abc123-def456/status",
  "cancel_url": "https://queue.fal.run/.../requests/abc123-def456/cancel"
}
```

**Final Result:**
```json
{
  "images": [{ "url": "https://v3.fal.media/files/...", "width": 1024, "height": 768 }]
}
```

## Present Results to User

**Images:**
```
![Generated Image](https://v3.fal.media/files/...)
• 1024×768 | Generated in 2.2s
```

**Videos:**
```
[Click to view video](https://v3.fal.media/files/.../video.mp4)
• Duration: 5s | Generated in 45s
```

**Async Submission:**
```
Request submitted to queue.
• Request ID: abc123-def456
• Model: fal-ai/veo3
• Check status: --status "abc123-def456"
```

## Object Lifecycle (Optional)

Control how long generated files remain accessible:

```bash
# Files expire after 1 hour (3600 seconds)
bash generate.sh --prompt "..." --lifecycle 3600

# Files expire after 24 hours
bash generate.sh --prompt "..." --lifecycle 86400
```

## Troubleshooting

### Timeout Error
```
Error: Timeout after 600s
Request ID: abc123-def456
```
**Solution:** Use `--status` and `--result` to check manually, or increase `--timeout`.

### API Key Error
```
Error: FAL_KEY not set
```
**Solution:** Run `./generate.sh --add-fal-key` or `export FAL_KEY=your_key`.

### Network Error (claude.ai)
Go to `claude.ai/settings/capabilities` and add `*.fal.ai` to allowed domains.
```

## File: `skills/claude.ai/fal-generate/scripts/generate.sh`
```bash
#!/bin/bash

# fal.ai Generation Script with Queue Support
# Usage: ./generate.sh --prompt "..." [--model MODEL] [options]
# Returns: JSON with generated media URLs
#
# Queue Mode (default): Submits to queue, polls for completion
# Async Mode: Returns request_id immediately
# Sync Mode: Direct request (not recommended for long tasks)

set -e

FAL_QUEUE_ENDPOINT="https://queue.fal.run"
FAL_SYNC_ENDPOINT="https://fal.run"
FAL_TOKEN_ENDPOINT="https://rest.alpha.fal.ai/vault/auth/token?storage_type=fal-cdn-v3"

# Default values
MODEL="fal-ai/nano-banana-pro"
PROMPT=""
IMAGE_URL=""
IMAGE_FILE=""
IMAGE_SIZE="landscape_4_3"
NUM_IMAGES=1
MODE="queue"  # queue (default), async, sync
REQUEST_ID=""
ACTION="generate"  # generate, status, result, cancel
POLL_INTERVAL=2
MAX_POLL_TIME=600
LIFECYCLE=""
SHOW_LOGS=false

# Check for --add-fal-key first
for arg in "$@"; do
    if [ "$arg" = "--add-fal-key" ]; then
        shift
        KEY_VALUE=""
        if [[ -n "$1" && ! "$1" =~ ^-- ]]; then
            KEY_VALUE="$1"
        fi
        if [ -z "$KEY_VALUE" ]; then
            echo "Enter your fal.ai API key:" >&2
            read -r KEY_VALUE
        fi
        if [ -n "$KEY_VALUE" ]; then
            grep -v "^FAL_KEY=" .env > .env.tmp 2>/dev/null || true
            mv .env.tmp .env 2>/dev/null || true
            echo "FAL_KEY=$KEY_VALUE" >> .env
            echo "FAL_KEY saved to .env" >&2
        fi
        exit 0
    fi
done

# Load .env if exists
if [ -f ".env" ]; then
    source .env 2>/dev/null || true
fi

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --prompt|-p)
            PROMPT="$2"
            shift 2
            ;;
        --model|-m)
            MODEL="$2"
            shift 2
            ;;
        --image-url)
            IMAGE_URL="$2"
            shift 2
            ;;
        --file|--image)
            IMAGE_FILE="$2"
            shift 2
            ;;
        --size)
            case $2 in
                square) IMAGE_SIZE="square" ;;
                portrait) IMAGE_SIZE="portrait_4_3" ;;
                landscape) IMAGE_SIZE="landscape_4_3" ;;
                *) IMAGE_SIZE="$2" ;;
            esac
            shift 2
            ;;
        --num-images)
            NUM_IMAGES="$2"
            shift 2
            ;;
        # Mode options
        --async)
            MODE="async"
            shift
            ;;
        --sync)
            MODE="sync"
            shift
            ;;
        --logs)
            SHOW_LOGS=true
            shift
            ;;
        # Queue operations
        --status)
            ACTION="status"
            REQUEST_ID="$2"
            shift 2
            ;;
        --result)
            ACTION="result"
            REQUEST_ID="$2"
            shift 2
            ;;
        --cancel)
            ACTION="cancel"
            REQUEST_ID="$2"
            shift 2
            ;;
        # Polling options
        --poll-interval)
            POLL_INTERVAL="$2"
            shift 2
            ;;
        --timeout)
            MAX_POLL_TIME="$2"
            shift 2
            ;;
        # Object lifecycle (optional)
        --lifecycle)
            LIFECYCLE="$2"
            shift 2
            ;;
        # Schema lookup
        --schema)
            SCHEMA_MODEL="${2:-$MODEL}"
            ENCODED=$(echo "$SCHEMA_MODEL" | sed 's/\//%2F/g')
            echo "Fetching schema for $SCHEMA_MODEL..." >&2
            curl -s "https://fal.ai/api/openapi/queue/openapi.json?endpoint_id=$ENCODED"
            exit 0
            ;;
        --help|-h)
            echo "fal.ai Generation Script (Queue-based)" >&2
            echo "" >&2
            echo "Usage:" >&2
            echo "  ./generate.sh --prompt \"...\" [options]" >&2
            echo "" >&2
            echo "Generation Options:" >&2
            echo "  --prompt, -p    Text description (required for generate)" >&2
            echo "  --model, -m     Model ID (default: fal-ai/nano-banana-pro)" >&2
            echo "  --image-url     Input image URL for I2V models" >&2
            echo "  --file, --image Local file (auto-uploads to fal CDN)" >&2
            echo "  --size          square, portrait, landscape" >&2
            echo "  --num-images    Number of images (default: 1)" >&2
            echo "" >&2
            echo "Mode Options:" >&2
            echo "  (default)       Queue mode - submit and poll until complete" >&2
            echo "  --async         Submit to queue, return request_id immediately" >&2
            echo "  --sync          Synchronous request (not recommended for video)" >&2
            echo "  --logs          Show generation logs while polling" >&2
            echo "" >&2
            echo "Queue Operations:" >&2
            echo "  --status ID     Check status of a queued request" >&2
            echo "  --result ID     Get result of a completed request" >&2
            echo "  --cancel ID     Cancel a queued request" >&2
            echo "" >&2
            echo "Advanced Options:" >&2
            echo "  --poll-interval Seconds between status checks (default: 2)" >&2
            echo "  --timeout       Max seconds to wait (default: 600)" >&2
            echo "  --lifecycle N   Object expiration in seconds (optional)" >&2
            echo "  --schema [MODEL] Get OpenAPI schema for model" >&2
            echo "  --add-fal-key   Setup FAL_KEY in .env" >&2
            echo "" >&2
            echo "Examples:" >&2
            echo "  # Generate image (waits for completion)" >&2
            echo "  ./generate.sh --prompt \"a sunset\" --model \"fal-ai/nano-banana-pro\"" >&2
            echo "" >&2
            echo "  # Generate video async (returns immediately)" >&2
            echo "  ./generate.sh --prompt \"ocean waves\" --model \"fal-ai/veo3\" --async" >&2
            echo "" >&2
            echo "  # Check status" >&2
            echo "  ./generate.sh --status \"request_id\" --model \"fal-ai/veo3\"" >&2
            echo "" >&2
            echo "  # Get result" >&2
            echo "  ./generate.sh --result \"request_id\" --model \"fal-ai/veo3\"" >&2
            exit 0
            ;;
        *)
            shift
            ;;
    esac
done

# Validate FAL_KEY
if [ -z "$FAL_KEY" ]; then
    echo "Error: FAL_KEY not set" >&2
    echo "" >&2
    echo "Run: ./generate.sh --add-fal-key" >&2
    echo "Or:  export FAL_KEY=your_key_here" >&2
    exit 1
fi

# Handle local file upload
if [ -n "$IMAGE_FILE" ]; then
    if [ ! -f "$IMAGE_FILE" ]; then
        echo "Error: File not found: $IMAGE_FILE" >&2
        exit 1
    fi

    FILENAME=$(basename "$IMAGE_FILE")
    EXTENSION="${FILENAME##*.}"
    EXTENSION_LOWER=$(echo "$EXTENSION" | tr '[:upper:]' '[:lower:]')

    # Detect content type
    case "$EXTENSION_LOWER" in
        jpg|jpeg) CONTENT_TYPE="image/jpeg" ;;
        png) CONTENT_TYPE="image/png" ;;
        gif) CONTENT_TYPE="image/gif" ;;
        webp) CONTENT_TYPE="image/webp" ;;
        mp4) CONTENT_TYPE="video/mp4" ;;
        mov) CONTENT_TYPE="video/quicktime" ;;
        *) CONTENT_TYPE="application/octet-stream" ;;
    esac

    echo "Uploading $FILENAME..." >&2

    # Step 1: Get CDN token
    TOKEN_RESPONSE=$(curl -s -X POST "$FAL_TOKEN_ENDPOINT" \
        -H "Authorization: Key $FAL_KEY" \
        -H "Content-Type: application/json" \
        -d '{}')

    CDN_TOKEN=$(echo "$TOKEN_RESPONSE" | grep -o '"token":"[^"]*"' | cut -d'"' -f4)
    CDN_TOKEN_TYPE=$(echo "$TOKEN_RESPONSE" | grep -o '"token_type":"[^"]*"' | cut -d'"' -f4)
    CDN_BASE_URL=$(echo "$TOKEN_RESPONSE" | grep -o '"base_url":"[^"]*"' | cut -d'"' -f4)

    if [ -z "$CDN_TOKEN" ] || [ -z "$CDN_BASE_URL" ]; then
        echo "Error: Failed to get CDN token" >&2
        exit 1
    fi

    # Step 2: Upload file
    UPLOAD_RESPONSE=$(curl -s -X POST "${CDN_BASE_URL}/files/upload" \
        -H "Authorization: $CDN_TOKEN_TYPE $CDN_TOKEN" \
        -H "Content-Type: $CONTENT_TYPE" \
        -H "X-Fal-File-Name: $FILENAME" \
        --data-binary "@$IMAGE_FILE")

    # Check for upload error
    if echo "$UPLOAD_RESPONSE" | grep -q '"error"'; then
        ERROR_MSG=$(echo "$UPLOAD_RESPONSE" | grep -o '"message":"[^"]*"' | head -1 | cut -d'"' -f4)
        echo "Upload error: $ERROR_MSG" >&2
        exit 1
    fi

    # Extract URL
    IMAGE_URL=$(echo "$UPLOAD_RESPONSE" | grep -o '"access_url":"[^"]*"' | cut -d'"' -f4)

    if [ -z "$IMAGE_URL" ]; then
        echo "Error: Failed to get URL from upload response" >&2
        exit 1
    fi

    echo "Uploaded: $IMAGE_URL" >&2
fi

# Build headers
HEADERS=(-H "Authorization: Key $FAL_KEY" -H "Content-Type: application/json")

# Add lifecycle header if specified
if [ -n "$LIFECYCLE" ]; then
    HEADERS+=(-H "X-Fal-Object-Lifecycle-Preference: {\"expiration_duration_seconds\": $LIFECYCLE}")
fi

# Handle queue operations
case $ACTION in
    status)
        if [ -z "$REQUEST_ID" ]; then
            echo "Error: Request ID required for --status" >&2
            exit 1
        fi
        LOGS_PARAM=""
        if [ "$SHOW_LOGS" = true ]; then
            LOGS_PARAM="?logs=1"
        fi
        echo "Checking status for $REQUEST_ID..." >&2
        RESPONSE=$(curl -s -X GET "$FAL_QUEUE_ENDPOINT/$MODEL/requests/$REQUEST_ID/status$LOGS_PARAM" "${HEADERS[@]}")

        # Parse and display status
        STATUS=$(echo "$RESPONSE" | grep -oE '"status"[[:space:]]*:[[:space:]]*"[^"]*"' | sed 's/.*: *"//' | sed 's/"$//')
        echo "Status: $STATUS" >&2

        if [ "$STATUS" = "IN_QUEUE" ]; then
            POSITION=$(echo "$RESPONSE" | grep -o '"queue_position":[0-9]*' | cut -d':' -f2)
            [ -n "$POSITION" ] && echo "Queue position: $POSITION" >&2
        fi

        echo "$RESPONSE"
        exit 0
        ;;
    result)
        if [ -z "$REQUEST_ID" ]; then
            echo "Error: Request ID required for --result" >&2
            exit 1
        fi
        echo "Getting result for $REQUEST_ID..." >&2
        RESPONSE=$(curl -s -X GET "$FAL_QUEUE_ENDPOINT/$MODEL/requests/$REQUEST_ID" "${HEADERS[@]}")

        # Check for error
        if echo "$RESPONSE" | grep -q '"error"'; then
            ERROR_MSG=$(echo "$RESPONSE" | grep -o '"message":"[^"]*"' | head -1 | cut -d'"' -f4)
            echo "Error: $ERROR_MSG" >&2
            exit 1
        fi

        # Extract URL
        if echo "$RESPONSE" | grep -q '"video"'; then
            URL=$(echo "$RESPONSE" | grep -o '"url":"[^"]*"' | head -1 | cut -d'"' -f4)
            echo "Video URL: $URL" >&2
        elif echo "$RESPONSE" | grep -q '"images"'; then
            URL=$(echo "$RESPONSE" | grep -o '"url":"[^"]*"' | head -1 | cut -d'"' -f4)
            echo "Image URL: $URL" >&2
        fi

        echo "$RESPONSE"
        exit 0
        ;;
    cancel)
        if [ -z "$REQUEST_ID" ]; then
            echo "Error: Request ID required for --cancel" >&2
            exit 1
        fi
        echo "Cancelling request $REQUEST_ID..." >&2
        RESPONSE=$(curl -s -X PUT "$FAL_QUEUE_ENDPOINT/$MODEL/requests/$REQUEST_ID/cancel" "${HEADERS[@]}")
        echo "$RESPONSE"
        exit 0
        ;;
esac

# Generate action requires prompt
if [ -z "$PROMPT" ]; then
    echo "Error: --prompt is required" >&2
    exit 1
fi

# Build the request payload based on model type
if [[ "$MODEL" == *"image-to-video"* ]] || [[ "$MODEL" == *"i2v"* ]]; then
    if [ -z "$IMAGE_URL" ]; then
        echo "Error: --image-url is required for image-to-video models" >&2
        exit 1
    fi
    PAYLOAD=$(cat <<EOF
{"prompt": "$PROMPT", "image_url": "$IMAGE_URL"}
EOF
)
elif [[ "$MODEL" == *"video"* ]] || [[ "$MODEL" == *"veo"* ]] || [[ "$MODEL" == *"text-to-video"* ]]; then
    PAYLOAD=$(cat <<EOF
{"prompt": "$PROMPT"}
EOF
)
else
    PAYLOAD=$(cat <<EOF
{"prompt": "$PROMPT", "image_size": "$IMAGE_SIZE", "num_images": $NUM_IMAGES}
EOF
)
fi

# Synchronous mode
if [ "$MODE" = "sync" ]; then
    echo "Generating with $MODEL (sync mode)..." >&2
    RESPONSE=$(curl -s -X POST "$FAL_SYNC_ENDPOINT/$MODEL" "${HEADERS[@]}" -d "$PAYLOAD")

    if echo "$RESPONSE" | grep -q '"error"'; then
        ERROR_MSG=$(echo "$RESPONSE" | grep -o '"message":"[^"]*"' | head -1 | cut -d'"' -f4)
        echo "Error: $ERROR_MSG" >&2
        exit 1
    fi

    echo "Generation complete!" >&2
    if echo "$RESPONSE" | grep -q '"video"'; then
        URL=$(echo "$RESPONSE" | grep -o '"url":"[^"]*"' | head -1 | cut -d'"' -f4)
        echo "Video URL: $URL" >&2
    elif echo "$RESPONSE" | grep -q '"images"'; then
        URL=$(echo "$RESPONSE" | grep -o '"url":"[^"]*"' | head -1 | cut -d'"' -f4)
        echo "Image URL: $URL" >&2
    fi

    echo "$RESPONSE"
    exit 0
fi

# Queue mode (async or poll)
echo "Submitting to queue: $MODEL..." >&2

SUBMIT_RESPONSE=$(curl -s -X POST "$FAL_QUEUE_ENDPOINT/$MODEL" "${HEADERS[@]}" -d "$PAYLOAD")

# Check for submit error
if echo "$SUBMIT_RESPONSE" | grep -q '"error"'; then
    ERROR_MSG=$(echo "$SUBMIT_RESPONSE" | grep -o '"message":"[^"]*"' | head -1 | cut -d'"' -f4)
    echo "Error: $ERROR_MSG" >&2
    exit 1
fi

# Extract request_id and URLs (handle both "key": "value" and "key":"value" formats)
REQUEST_ID=$(echo "$SUBMIT_RESPONSE" | grep -oE '"request_id"[[:space:]]*:[[:space:]]*"[^"]*"' | sed 's/.*: *"//' | sed 's/"$//')
STATUS_URL=$(echo "$SUBMIT_RESPONSE" | grep -oE '"status_url"[[:space:]]*:[[:space:]]*"[^"]*"' | sed 's/.*: *"//' | sed 's/"$//')
RESPONSE_URL=$(echo "$SUBMIT_RESPONSE" | grep -oE '"response_url"[[:space:]]*:[[:space:]]*"[^"]*"' | sed 's/.*: *"//' | sed 's/"$//')
CANCEL_URL=$(echo "$SUBMIT_RESPONSE" | grep -oE '"cancel_url"[[:space:]]*:[[:space:]]*"[^"]*"' | sed 's/.*: *"//' | sed 's/"$//')

if [ -z "$REQUEST_ID" ]; then
    echo "Error: Failed to get request_id" >&2
    echo "$SUBMIT_RESPONSE" >&2
    exit 1
fi

echo "Request ID: $REQUEST_ID" >&2

# Async mode - return immediately
if [ "$MODE" = "async" ]; then
    echo "" >&2
    echo "Request submitted. Use these commands to check:" >&2
    echo "  Status: ./generate.sh --status \"$REQUEST_ID\" --model \"$MODEL\"" >&2
    echo "  Result: ./generate.sh --result \"$REQUEST_ID\" --model \"$MODEL\"" >&2
    echo "  Cancel: ./generate.sh --cancel \"$REQUEST_ID\" --model \"$MODEL\"" >&2
    echo "$SUBMIT_RESPONSE"
    exit 0
fi

# Queue mode - poll until complete
echo "Waiting for completion..." >&2

ELAPSED=0
LAST_STATUS=""

while [ $ELAPSED -lt $MAX_POLL_TIME ]; do
    sleep $POLL_INTERVAL
    ELAPSED=$((ELAPSED + POLL_INTERVAL))

    LOGS_PARAM=""
    if [ "$SHOW_LOGS" = true ]; then
        LOGS_PARAM="?logs=1"
    fi

    STATUS_RESPONSE=$(curl -s -X GET "${STATUS_URL}${LOGS_PARAM}" "${HEADERS[@]}")
    STATUS=$(echo "$STATUS_RESPONSE" | grep -oE '"status"[[:space:]]*:[[:space:]]*"[^"]*"' | sed 's/.*: *"//' | sed 's/"$//')

    # Show status change
    if [ "$STATUS" != "$LAST_STATUS" ]; then
        case $STATUS in
            IN_QUEUE)
                POSITION=$(echo "$STATUS_RESPONSE" | grep -o '"queue_position":[0-9]*' | cut -d':' -f2)
                echo "Status: IN_QUEUE (position: ${POSITION:-?})" >&2
                ;;
            IN_PROGRESS)
                echo "Status: IN_PROGRESS" >&2
                ;;
            COMPLETED)
                echo "Status: COMPLETED" >&2
                ;;
            *)
                echo "Status: $STATUS" >&2
                ;;
        esac
        LAST_STATUS="$STATUS"
    fi

    # Show logs if enabled
    if [ "$SHOW_LOGS" = true ]; then
        LOGS=$(echo "$STATUS_RESPONSE" | grep -o '"logs":\[[^]]*\]' | head -1)
        if [ -n "$LOGS" ] && [ "$LOGS" != "[]" ]; then
            echo "$LOGS" | tr ',' '\n' | grep -o '"message":"[^"]*"' | cut -d'"' -f4 | while read -r log; do
                echo "  > $log" >&2
            done
        fi
    fi

    if [ "$STATUS" = "COMPLETED" ]; then
        break
    fi

    if [ "$STATUS" = "FAILED" ]; then
        echo "Error: Generation failed" >&2
        echo "$STATUS_RESPONSE"
        exit 1
    fi
done

if [ "$STATUS" != "COMPLETED" ]; then
    echo "Error: Timeout after ${MAX_POLL_TIME}s" >&2
    echo "Request ID: $REQUEST_ID" >&2
    echo "Check status with: ./generate.sh --status \"$REQUEST_ID\" --model \"$MODEL\"" >&2
    exit 1
fi

# Get final result
echo "Fetching result..." >&2
RESULT=$(curl -s -X GET "$RESPONSE_URL" "${HEADERS[@]}")

# Check for error in result
if echo "$RESULT" | grep -q '"error"'; then
    ERROR_MSG=$(echo "$RESULT" | grep -o '"message":"[^"]*"' | head -1 | cut -d'"' -f4)
    echo "Error: $ERROR_MSG" >&2
    exit 1
fi

echo "" >&2
echo "Generation complete!" >&2

# Extract and display URL
if echo "$RESULT" | grep -q '"video"'; then
    URL=$(echo "$RESULT" | grep -o '"url":"[^"]*"' | head -1 | cut -d'"' -f4)
    echo "Video URL: $URL" >&2
elif echo "$RESULT" | grep -q '"images"'; then
    URL=$(echo "$RESULT" | grep -o '"url":"[^"]*"' | head -1 | cut -d'"' -f4)
    echo "Image URL: $URL" >&2
fi

# Output JSON
echo "$RESULT"
```

## File: `skills/claude.ai/fal-generate/scripts/get-schema.sh`
```bash
#!/bin/bash

# fal.ai Model Schema Script
# Usage: ./get-schema.sh --model MODEL
# Returns: OpenAPI 3.0 schema for the model

set -e

FAL_SCHEMA_ENDPOINT="https://fal.ai/api/openapi/queue/openapi.json"

# Default values
MODEL=""
OUTPUT_JSON=false
SHOW_INPUT=false
SHOW_OUTPUT=false

# Check for --add-fal-key first
for arg in "$@"; do
    if [ "$arg" = "--add-fal-key" ]; then
        shift
        KEY_VALUE=""
        if [[ -n "$1" && ! "$1" =~ ^-- ]]; then
            KEY_VALUE="$1"
        fi
        if [ -z "$KEY_VALUE" ]; then
            echo "Enter your fal.ai API key:" >&2
            read -r KEY_VALUE
        fi
        if [ -n "$KEY_VALUE" ]; then
            grep -v "^FAL_KEY=" .env > .env.tmp 2>/dev/null || true
            mv .env.tmp .env 2>/dev/null || true
            echo "FAL_KEY=$KEY_VALUE" >> .env
            echo "FAL_KEY saved to .env" >&2
        fi
        exit 0
    fi
done

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --model|-m)
            MODEL="$2"
            shift 2
            ;;
        --input|-i)
            SHOW_INPUT=true
            shift
            ;;
        --output|-o)
            SHOW_OUTPUT=true
            shift
            ;;
        --json)
            OUTPUT_JSON=true
            shift
            ;;
        --help|-h)
            echo "fal.ai Model Schema Script" >&2
            echo "" >&2
            echo "Usage:" >&2
            echo "  ./get-schema.sh --model MODEL [options]" >&2
            echo "" >&2
            echo "Options:" >&2
            echo "  --model, -m     Model ID (required)" >&2
            echo "  --input, -i     Show only input schema" >&2
            echo "  --output, -o    Show only output schema" >&2
            echo "  --json          Output raw JSON" >&2
            echo "  --add-fal-key   Setup FAL_KEY in .env" >&2
            echo "" >&2
            echo "Examples:" >&2
            echo "  ./get-schema.sh --model \"fal-ai/flux-pro/v1.1-ultra\"" >&2
            echo "  ./get-schema.sh --model \"fal-ai/kling-video/v2.6/pro/image-to-video\" --input" >&2
            exit 0
            ;;
        *)
            shift
            ;;
    esac
done

if [ -z "$MODEL" ]; then
    echo "Error: --model is required" >&2
    exit 1
fi

# URL encode the model ID
ENCODED_MODEL=$(echo "$MODEL" | sed 's/\//%2F/g')

echo "Fetching schema for $MODEL..." >&2

# Fetch OpenAPI schema
RESPONSE=$(curl -s -X GET "$FAL_SCHEMA_ENDPOINT?endpoint_id=$ENCODED_MODEL" \
    -H "Content-Type: application/json")

# Check for errors
if echo "$RESPONSE" | grep -q '"error"'; then
    ERROR_MSG=$(echo "$RESPONSE" | grep -o '"message":"[^"]*"' | head -1 | cut -d'"' -f4)
    echo "Error: $ERROR_MSG" >&2
    exit 1
fi

if [ "$OUTPUT_JSON" = true ]; then
    echo "$RESPONSE"
    exit 0
fi

# Parse and display schema summary
if command -v python3 &> /dev/null; then
    python3 << 'PYTHON_EOF' - "$RESPONSE" "$MODEL" "$SHOW_INPUT" "$SHOW_OUTPUT"
import json
import sys

response = json.loads(sys.argv[1])
model = sys.argv[2]
show_input = sys.argv[3] == "true"
show_output = sys.argv[4] == "true"

# Get metadata
info = response.get('info', {})
metadata = info.get('x-fal-metadata', {})
schemas = response.get('components', {}).get('schemas', {})

print("", file=sys.stderr)
print(f"Model: {model}", file=sys.stderr)
print("=" * (len(model) + 7), file=sys.stderr)

# Category
category = metadata.get('category', 'unknown')
print(f"Category: {category}", file=sys.stderr)

# URLs
if metadata.get('playgroundUrl'):
    print(f"Playground: {metadata['playgroundUrl']}", file=sys.stderr)
if metadata.get('documentationUrl'):
    print(f"Docs: {metadata['documentationUrl']}", file=sys.stderr)

# Find input/output schemas
input_schema = None
output_schema = None

for name, schema in schemas.items():
    if 'Input' in name and name != 'QueueStatus':
        input_schema = schema
    elif 'Output' in name and name != 'QueueStatus':
        output_schema = schema

# Show input schema
if input_schema and (show_input or (not show_input and not show_output)):
    print("", file=sys.stderr)
    print("Input Parameters", file=sys.stderr)
    print("-" * 16, file=sys.stderr)

    props = input_schema.get('properties', {})
    required = input_schema.get('required', [])
    order = input_schema.get('x-fal-order-properties', list(props.keys()))

    for prop_name in order:
        if prop_name not in props:
            continue
        prop = props[prop_name]

        # Type
        prop_type = prop.get('type', 'any')
        if 'enum' in prop:
            prop_type = f"enum: {prop['enum']}"
        elif 'anyOf' in prop:
            types = [t.get('type', t.get('enum', ['?'])) for t in prop['anyOf']]
            prop_type = f"oneOf: {types}"

        # Required marker
        req_mark = "*" if prop_name in required else " "

        # Default value
        default = prop.get('default', '')
        default_str = f" (default: {default})" if default != '' else ""

        print(f"  {req_mark} {prop_name}: {prop_type}{default_str}", file=sys.stderr)

        # Description
        desc = prop.get('description', '')
        if desc:
            # Truncate long descriptions
            if len(desc) > 60:
                desc = desc[:57] + "..."
            print(f"      {desc}", file=sys.stderr)

# Show output schema
if output_schema and (show_output or (not show_input and not show_output)):
    print("", file=sys.stderr)
    print("Output Fields", file=sys.stderr)
    print("-" * 13, file=sys.stderr)

    props = output_schema.get('properties', {})
    order = output_schema.get('x-fal-order-properties', list(props.keys()))

    for prop_name in order:
        if prop_name not in props:
            continue
        prop = props[prop_name]

        prop_type = prop.get('type', 'any')
        if prop_type == 'array':
            items = prop.get('items', {})
            item_type = items.get('type', items.get('$ref', '').split('/')[-1])
            prop_type = f"array<{item_type}>"

        print(f"  {prop_name}: {prop_type}", file=sys.stderr)

print("", file=sys.stderr)
print("* = required parameter", file=sys.stderr)
PYTHON_EOF
fi

# Output full JSON for programmatic use
echo "$RESPONSE"
```

## File: `skills/claude.ai/fal-generate/scripts/search-models.sh`
```bash
#!/bin/bash

# fal.ai Model Search Script
# Usage: ./search-models.sh [--query QUERY] [--category CATEGORY] [--limit N]
# Returns: JSON with matching models

set -e

FAL_API_ENDPOINT="https://api.fal.ai/v1/models"

# Default values
QUERY=""
CATEGORY=""
LIMIT=20

# Load .env if exists
if [ -f ".env" ]; then
    source .env 2>/dev/null || true
fi

# Check for --add-fal-key first
for arg in "$@"; do
    if [ "$arg" = "--add-fal-key" ]; then
        shift
        KEY_VALUE=""
        if [[ -n "$1" && ! "$1" =~ ^-- ]]; then
            KEY_VALUE="$1"
        fi
        if [ -z "$KEY_VALUE" ]; then
            echo "Enter your fal.ai API key:" >&2
            read -r KEY_VALUE
        fi
        if [ -n "$KEY_VALUE" ]; then
            grep -v "^FAL_KEY=" .env > .env.tmp 2>/dev/null || true
            mv .env.tmp .env 2>/dev/null || true
            echo "FAL_KEY=$KEY_VALUE" >> .env
            echo "FAL_KEY saved to .env" >&2
        fi
        exit 0
    fi
done

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --query|-q)
            QUERY="$2"
            shift 2
            ;;
        --category|-c)
            CATEGORY="$2"
            shift 2
            ;;
        --limit|-l)
            LIMIT="$2"
            shift 2
            ;;
        --help|-h)
            echo "fal.ai Model Search Script" >&2
            echo "" >&2
            echo "Usage:" >&2
            echo "  ./search-models.sh [options]" >&2
            echo "" >&2
            echo "Options:" >&2
            echo "  --query, -q     Search query (e.g., 'flux', 'video', 'upscale')" >&2
            echo "  --category, -c  Filter by category:" >&2
            echo "                  text-to-image, image-to-image, text-to-video," >&2
            echo "                  image-to-video, text-to-speech, speech-to-text" >&2
            echo "  --limit, -l     Max results (default: 20)" >&2
            echo "  --add-fal-key   Setup FAL_KEY in .env" >&2
            echo "" >&2
            echo "Examples:" >&2
            echo "  ./search-models.sh --query 'flux'" >&2
            echo "  ./search-models.sh --category 'text-to-video'" >&2
            echo "  ./search-models.sh --query 'upscale' --limit 5" >&2
            exit 0
            ;;
        *)
            shift
            ;;
    esac
done

# Validate FAL_KEY
if [ -z "$FAL_KEY" ]; then
    echo "Error: FAL_KEY not set" >&2
    echo "" >&2
    echo "Run: ./search-models.sh --add-fal-key" >&2
    echo "Or:  export FAL_KEY=your_key_here" >&2
    exit 1
fi

echo "Searching fal.ai models..." >&2

# Build query parameters
PARAMS="limit=$LIMIT"

if [ -n "$QUERY" ]; then
    PARAMS="$PARAMS&q=$(echo "$QUERY" | sed 's/ /%20/g')"
fi

if [ -n "$CATEGORY" ]; then
    PARAMS="$PARAMS&category=$CATEGORY"
fi

# Make API request
AUTH_HEADER=""
if [ -n "$FAL_KEY" ]; then
    AUTH_HEADER="-H \"Authorization: Key $FAL_KEY\""
fi

RESPONSE=$(curl -s -X GET "$FAL_API_ENDPOINT?$PARAMS" \
    -H "Content-Type: application/json" \
    -H "Authorization: Key $FAL_KEY")

# Check for errors
if echo "$RESPONSE" | grep -q '"error"'; then
    ERROR_MSG=$(echo "$RESPONSE" | grep -o '"message":"[^"]*"' | head -1 | cut -d'"' -f4)
    echo "Error: $ERROR_MSG" >&2
    exit 1
fi

# Count results
COUNT=$(echo "$RESPONSE" | grep -o '"endpoint_id"' | wc -l | tr -d ' ')
echo "Found $COUNT models" >&2
echo "" >&2

# Display summary to stderr
if command -v python3 &> /dev/null; then
    python3 << 'PYTHON_EOF' - "$RESPONSE"
import json
import sys

response = json.loads(sys.argv[1])
models = response.get('data', response) if isinstance(response, dict) else response

if isinstance(models, list):
    for m in models[:10]:
        name = m.get('display_name', m.get('endpoint_id', 'Unknown'))
        endpoint = m.get('endpoint_id', '')
        category = m.get('category', '')
        print(f"  {name}", file=sys.stderr)
        print(f"    ID: {endpoint}", file=sys.stderr)
        if category:
            print(f"    Category: {category}", file=sys.stderr)
        print("", file=sys.stderr)

    if len(models) > 10:
        print(f"  ... and {len(models) - 10} more", file=sys.stderr)
PYTHON_EOF
fi

# Output JSON for programmatic use
echo "$RESPONSE"
```

## File: `skills/claude.ai/fal-generate/scripts/upload.sh`
```bash
#!/bin/bash

# fal.ai File Upload Script
# Usage: ./upload.sh --file /path/to/file
# Returns: CDN URL for the uploaded file
#
# Upload flow:
#   1. Get CDN token from rest.alpha.fal.ai
#   2. Upload file to CDN (v3b.fal.media)
#   3. Return access_url

set -e

FAL_TOKEN_ENDPOINT="https://rest.alpha.fal.ai/vault/auth/token?storage_type=fal-cdn-v3"

# Default values
FILE_PATH=""
OUTPUT_JSON=false

# Check for --add-fal-key first
for arg in "$@"; do
    if [ "$arg" = "--add-fal-key" ]; then
        shift
        KEY_VALUE=""
        if [[ -n "$1" && ! "$1" =~ ^-- ]]; then
            KEY_VALUE="$1"
        fi
        if [ -z "$KEY_VALUE" ]; then
            echo "Enter your fal.ai API key:" >&2
            read -r KEY_VALUE
        fi
        if [ -n "$KEY_VALUE" ]; then
            grep -v "^FAL_KEY=" .env > .env.tmp 2>/dev/null || true
            mv .env.tmp .env 2>/dev/null || true
            echo "FAL_KEY=$KEY_VALUE" >> .env
            echo "FAL_KEY saved to .env" >&2
        fi
        exit 0
    fi
done

# Load .env if exists
if [ -f ".env" ]; then
    source .env 2>/dev/null || true
fi

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --file|-f)
            FILE_PATH="$2"
            shift 2
            ;;
        --json)
            OUTPUT_JSON=true
            shift
            ;;
        --help|-h)
            echo "fal.ai File Upload Script" >&2
            echo "" >&2
            echo "Usage:" >&2
            echo "  ./upload.sh --file /path/to/file" >&2
            echo "" >&2
            echo "Options:" >&2
            echo "  --file, -f      Local file path (required)" >&2
            echo "  --json          Output raw JSON response" >&2
            echo "  --add-fal-key   Setup FAL_KEY in .env" >&2
            echo "" >&2
            echo "Supported file types:" >&2
            echo "  Images: jpg, jpeg, png, gif, webp, bmp, tiff" >&2
            echo "  Videos: mp4, mov, avi, webm, mkv" >&2
            echo "  Audio:  mp3, wav, flac, ogg, m4a" >&2
            echo "" >&2
            echo "Examples:" >&2
            echo "  ./upload.sh --file photo.jpg" >&2
            echo "  ./upload.sh --file video.mp4" >&2
            echo "" >&2
            echo "Usage with generate.sh:" >&2
            echo "  URL=\$(./upload.sh --file photo.jpg)" >&2
            echo "  ./generate.sh --image-url \"\$URL\" --prompt \"...\"" >&2
            exit 0
            ;;
        *)
            # If no flag, treat as file path
            if [ -z "$FILE_PATH" ] && [ -f "$1" ]; then
                FILE_PATH="$1"
            fi
            shift
            ;;
    esac
done

# Validate FAL_KEY
if [ -z "$FAL_KEY" ]; then
    echo "Error: FAL_KEY not set" >&2
    echo "" >&2
    echo "Run: ./upload.sh --add-fal-key" >&2
    echo "Or:  export FAL_KEY=your_key_here" >&2
    exit 1
fi

# Validate file
if [ -z "$FILE_PATH" ]; then
    echo "Error: --file is required" >&2
    exit 1
fi

if [ ! -f "$FILE_PATH" ]; then
    echo "Error: File not found: $FILE_PATH" >&2
    exit 1
fi

# Get filename
FILENAME=$(basename "$FILE_PATH")

# Detect content type
EXTENSION="${FILENAME##*.}"
EXTENSION_LOWER=$(echo "$EXTENSION" | tr '[:upper:]' '[:lower:]')

case "$EXTENSION_LOWER" in
    jpg|jpeg) CONTENT_TYPE="image/jpeg" ;;
    png) CONTENT_TYPE="image/png" ;;
    gif) CONTENT_TYPE="image/gif" ;;
    webp) CONTENT_TYPE="image/webp" ;;
    bmp) CONTENT_TYPE="image/bmp" ;;
    tiff|tif) CONTENT_TYPE="image/tiff" ;;
    mp4) CONTENT_TYPE="video/mp4" ;;
    mov) CONTENT_TYPE="video/quicktime" ;;
    avi) CONTENT_TYPE="video/x-msvideo" ;;
    webm) CONTENT_TYPE="video/webm" ;;
    mkv) CONTENT_TYPE="video/x-matroska" ;;
    mp3) CONTENT_TYPE="audio/mpeg" ;;
    wav) CONTENT_TYPE="audio/wav" ;;
    flac) CONTENT_TYPE="audio/flac" ;;
    ogg) CONTENT_TYPE="audio/ogg" ;;
    m4a) CONTENT_TYPE="audio/mp4" ;;
    *) CONTENT_TYPE="application/octet-stream" ;;
esac

# Get file size
FILE_SIZE=$(stat -f%z "$FILE_PATH" 2>/dev/null || stat -c%s "$FILE_PATH" 2>/dev/null)
FILE_SIZE_MB=$((FILE_SIZE / 1024 / 1024))

# Check if file is too large (>100MB needs multipart)
if [ "$FILE_SIZE" -gt 104857600 ]; then
    echo "Error: File too large (${FILE_SIZE_MB}MB > 100MB)" >&2
    echo "Large file multipart upload not yet supported." >&2
    echo "Please use the Python client for files >100MB." >&2
    exit 1
fi

echo "Uploading: $FILENAME (${FILE_SIZE_MB}MB)" >&2

# Step 1: Get CDN token
echo "Getting CDN token..." >&2

TOKEN_RESPONSE=$(curl -s -X POST "$FAL_TOKEN_ENDPOINT" \
    -H "Authorization: Key $FAL_KEY" \
    -H "Content-Type: application/json" \
    -d '{}')

# Check for token error
if echo "$TOKEN_RESPONSE" | grep -q '"detail"'; then
    ERROR_MSG=$(echo "$TOKEN_RESPONSE" | grep -o '"msg":"[^"]*"' | head -1 | cut -d'"' -f4)
    echo "Token error: $ERROR_MSG" >&2
    exit 1
fi

TOKEN=$(echo "$TOKEN_RESPONSE" | grep -o '"token":"[^"]*"' | cut -d'"' -f4)
TOKEN_TYPE=$(echo "$TOKEN_RESPONSE" | grep -o '"token_type":"[^"]*"' | cut -d'"' -f4)
BASE_URL=$(echo "$TOKEN_RESPONSE" | grep -o '"base_url":"[^"]*"' | cut -d'"' -f4)

if [ -z "$TOKEN" ] || [ -z "$BASE_URL" ]; then
    echo "Error: Failed to get CDN token" >&2
    echo "$TOKEN_RESPONSE" >&2
    exit 1
fi

# Step 2: Upload file
echo "Uploading to CDN..." >&2

UPLOAD_RESPONSE=$(curl -s -X POST "${BASE_URL}/files/upload" \
    -H "Authorization: $TOKEN_TYPE $TOKEN" \
    -H "Content-Type: $CONTENT_TYPE" \
    -H "X-Fal-File-Name: $FILENAME" \
    --data-binary "@$FILE_PATH")

# Check for upload error
if echo "$UPLOAD_RESPONSE" | grep -q '"error"'; then
    ERROR_MSG=$(echo "$UPLOAD_RESPONSE" | grep -o '"message":"[^"]*"' | head -1 | cut -d'"' -f4)
    if [ -z "$ERROR_MSG" ]; then
        ERROR_MSG=$(echo "$UPLOAD_RESPONSE" | grep -o '"error":"[^"]*"' | cut -d'"' -f4)
    fi
    echo "Upload error: $ERROR_MSG" >&2
    exit 1
fi

# Extract URL
ACCESS_URL=$(echo "$UPLOAD_RESPONSE" | grep -o '"access_url":"[^"]*"' | cut -d'"' -f4)

if [ -z "$ACCESS_URL" ]; then
    echo "Error: Failed to get URL from response" >&2
    echo "$UPLOAD_RESPONSE" >&2
    exit 1
fi

echo "Upload complete!" >&2
echo "URL: $ACCESS_URL" >&2

# Output
if [ "$OUTPUT_JSON" = true ]; then
    echo "$UPLOAD_RESPONSE"
else
    # Output just the URL for easy piping
    echo "$ACCESS_URL"
fi
```

## File: `skills/claude.ai/fal-image-edit/SKILL.md`
```markdown
---
name: fal-image-edit
description: Edit images using AI on fal.ai. Style transfer, object removal, background changes, and more. Use when the user requests "Edit image", "Remove object", "Change background", "Apply style", or similar image editing tasks.
metadata:
  author: fal-ai
  version: "1.0.0"
---

# fal.ai Image Edit

Edit images using AI: style transfer, object removal, background changes, and more.

## How It Works

1. User provides image URL and editing instructions
2. Script selects appropriate model
3. Sends request to fal.ai API
4. Returns edited image URL

## Finding Models

To discover the best and latest image editing models, use the search API:

```bash
# Search for image editing models
bash /mnt/skills/user/fal-generate/scripts/search-models.sh --category "image-to-image"

# Search for specific editing capabilities
bash /mnt/skills/user/fal-generate/scripts/search-models.sh --query "image editing"
bash /mnt/skills/user/fal-generate/scripts/search-models.sh --query "inpainting"
bash /mnt/skills/user/fal-generate/scripts/search-models.sh --query "object removal"
bash /mnt/skills/user/fal-generate/scripts/search-models.sh --query "background removal"
```

Or use the `search_models` MCP tool with relevant keywords.

## Supported Operations

| Operation | Description |
|-----------|-------------|
| Style Transfer | Apply artistic style to image |
| Object Removal | Remove objects from image |
| Background Change | Change/replace background |
| Inpainting | Fill in masked areas |
| General Edit | Instruction-based edits |

## Usage

```bash
bash /mnt/skills/user/fal-image-edit/scripts/edit-image.sh [options]
```

**Arguments:**
- `--image-url` - URL of image to edit (required)
- `--prompt` - Description of desired edit (required)
- `--operation` - Edit operation: `style`, `remove`, `background`, `inpaint` (default: `style`)
- `--mask-url` - URL of mask image (required for inpainting/removal)
- `--strength` - Edit strength 0.0-1.0 (default: 0.75)

**Examples:**

```bash
# Style transfer
bash /mnt/skills/user/fal-image-edit/scripts/edit-image.sh \
  --image-url "https://example.com/photo.jpg" \
  --prompt "Convert to anime style" \
  --operation style

# Remove object
bash /mnt/skills/user/fal-image-edit/scripts/edit-image.sh \
  --image-url "https://example.com/photo.jpg" \
  --prompt "Remove the person on the left" \
  --operation remove

# Change background
bash /mnt/skills/user/fal-image-edit/scripts/edit-image.sh \
  --image-url "https://example.com/portrait.jpg" \
  --prompt "Place in a tropical beach setting" \
  --operation background

# Inpainting with mask
bash /mnt/skills/user/fal-image-edit/scripts/edit-image.sh \
  --image-url "https://example.com/photo.jpg" \
  --mask-url "https://example.com/mask.png" \
  --prompt "Fill with flowers" \
  --operation inpaint
```

## MCP Tool Alternative

Use `search_models` MCP tool or `search-models.sh` to find the best current model for each operation (style transfer, object removal, background change, inpainting), then call `mcp__fal-ai__generate` with the discovered `modelId`.

## Output

```
Editing image...
Model: fal-ai/flux/dev/image-to-image
Operation: style transfer

Edit complete!

Image URL: https://v3.fal.media/files/abc123/edited.png
Dimensions: 1024x1024
```

JSON output:
```json
{
  "images": [
    {
      "url": "https://v3.fal.media/files/abc123/edited.png",
      "width": 1024,
      "height": 1024
    }
  ]
}
```

## Present Results to User

```
Here's your edited image:

![Edited Image](https://v3.fal.media/files/...)

• 1024×1024 | Operation: Style Transfer
```

## Model Selection Tips

- **General Editing**: Search for "image editing" models. Good for instruction-based changes.
- **Style Transfer**: Search for `image-to-image` category. Adjust strength: 0.3-0.5 for subtle, 0.7-0.9 for dramatic.
- **Object Removal**: Search for "eraser" or "object removal". Some work without masks.
- **Background Change**: Search for "background" or "kontext". Look for models that preserve subject identity.
- **Inpainting**: Search for "inpainting" or "fill". Requires binary mask (white = edit area).

## Mask Tips

For inpainting and some removal tasks:
- White pixels = areas to edit
- Black pixels = areas to preserve
- Use PNG format with transparency or solid colors
- Feathered edges create smoother transitions

## Troubleshooting

### Edit Too Subtle
```
The edit is barely visible.

Increase the strength parameter:
--strength 0.85
```

### Edit Too Dramatic
```
The edit changed too much of the image.

Decrease the strength parameter:
--strength 0.3
```

### Object Not Removed
```
The object wasn't fully removed.

Tips:
1. Be more specific in the prompt
2. Try using an explicit mask
3. Use the inpainting model for precise control
```

### Background Artifacts
```
The new background has artifacts around the subject.

Tips:
1. Use a cleaner source image
2. Try FLUX Kontext which handles edges better
3. Adjust the strength for smoother blending
```
```

## File: `skills/claude.ai/fal-image-edit/scripts/edit-image.sh`
```bash
#!/bin/bash

# fal.ai Image Edit Script
# Usage: ./edit-image.sh --image-url URL --prompt "..." [--operation OP] [--mask-url URL] [--strength N]
# Returns: JSON with edited image URL

set -e

FAL_API_ENDPOINT="https://fal.run"

# Default values
IMAGE_URL=""
PROMPT=""
OPERATION="style"
MASK_URL=""
STRENGTH=0.75

# Check for --add-fal-key first
for arg in "$@"; do
    if [ "$arg" = "--add-fal-key" ]; then
        shift
        KEY_VALUE=""
        if [[ -n "$1" && ! "$1" =~ ^-- ]]; then
            KEY_VALUE="$1"
        fi
        if [ -z "$KEY_VALUE" ]; then
            echo "Enter your fal.ai API key:" >&2
            read -r KEY_VALUE
        fi
        if [ -n "$KEY_VALUE" ]; then
            grep -v "^FAL_KEY=" .env > .env.tmp 2>/dev/null || true
            mv .env.tmp .env 2>/dev/null || true
            echo "FAL_KEY=$KEY_VALUE" >> .env
            echo "FAL_KEY saved to .env" >&2
        fi
        exit 0
    fi
done

# Load .env if exists
if [ -f ".env" ]; then
    source .env 2>/dev/null || true
fi

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --image-url)
            IMAGE_URL="$2"
            shift 2
            ;;
        --prompt)
            PROMPT="$2"
            shift 2
            ;;
        --operation)
            OPERATION="$2"
            shift 2
            ;;
        --mask-url)
            MASK_URL="$2"
            shift 2
            ;;
        --strength)
            STRENGTH="$2"
            shift 2
            ;;
        --help|-h)
            echo "fal.ai Image Edit Script" >&2
            echo "" >&2
            echo "Usage:" >&2
            echo "  ./edit-image.sh --image-url URL --prompt \"...\" [options]" >&2
            echo "" >&2
            echo "Options:" >&2
            echo "  --image-url     Image URL to edit (required)" >&2
            echo "  --prompt        Edit description (required)" >&2
            echo "  --operation     Operation: style, remove, background, inpaint" >&2
            echo "  --mask-url      Mask URL (required for inpaint)" >&2
            echo "  --strength      Edit strength 0-1 (default: 0.75)" >&2
            echo "  --add-fal-key   Setup FAL_KEY in .env" >&2
            exit 0
            ;;
        *)
            shift
            ;;
    esac
done

# Validate required inputs
if [ -z "$FAL_KEY" ]; then
    echo "Error: FAL_KEY not set" >&2
    echo "" >&2
    echo "Run: ./edit-image.sh --add-fal-key" >&2
    echo "Or:  export FAL_KEY=your_key_here" >&2
    exit 1
fi

if [ -z "$IMAGE_URL" ]; then
    echo "Error: --image-url is required" >&2
    exit 1
fi

if [ -z "$PROMPT" ]; then
    echo "Error: --prompt is required" >&2
    exit 1
fi

# Select model based on operation
case $OPERATION in
    style)
        MODEL="fal-ai/flux/dev/image-to-image"
        ;;
    remove)
        MODEL="bria/eraser"
        ;;
    background)
        MODEL="fal-ai/flux-pro/kontext"
        ;;
    inpaint)
        MODEL="fal-ai/flux-lora-fill"
        if [ -z "$MASK_URL" ]; then
            echo "Error: --mask-url is required for inpainting" >&2
            exit 1
        fi
        ;;
    *)
        echo "Unknown operation: $OPERATION" >&2
        echo "Supported: style, remove, background, inpaint" >&2
        exit 1
        ;;
esac

# Create temp directory
TEMP_DIR=$(mktemp -d)
trap 'rm -rf "$TEMP_DIR"' EXIT

echo "Editing image..." >&2
echo "Model: $MODEL" >&2
echo "Operation: $OPERATION" >&2
echo "" >&2

# Build payload based on operation
case $OPERATION in
    style)
        PAYLOAD=$(cat <<EOF
{
  "image_url": "$IMAGE_URL",
  "prompt": "$PROMPT",
  "strength": $STRENGTH
}
EOF
)
        ;;
    remove|background)
        PAYLOAD=$(cat <<EOF
{
  "image_url": "$IMAGE_URL",
  "prompt": "$PROMPT"
}
EOF
)
        ;;
    inpaint)
        PAYLOAD=$(cat <<EOF
{
  "image_url": "$IMAGE_URL",
  "mask_url": "$MASK_URL",
  "prompt": "$PROMPT"
}
EOF
)
        ;;
esac

# Make API request
RESPONSE=$(curl -s -X POST "$FAL_API_ENDPOINT/$MODEL" \
    -H "Authorization: Key $FAL_KEY" \
    -H "Content-Type: application/json" \
    -d "$PAYLOAD")

# Check for errors
if echo "$RESPONSE" | grep -q '"error"'; then
    ERROR_MSG=$(echo "$RESPONSE" | grep -o '"message":"[^"]*"' | head -1 | cut -d'"' -f4)
    if [ -z "$ERROR_MSG" ]; then
        ERROR_MSG=$(echo "$RESPONSE" | grep -o '"error":"[^"]*"' | cut -d'"' -f4)
    fi
    echo "Error: $ERROR_MSG" >&2
    exit 1
fi

echo "Edit complete!" >&2
echo "" >&2

# Extract image URL
OUTPUT_URL=$(echo "$RESPONSE" | grep -o '"url":"[^"]*"' | head -1 | cut -d'"' -f4)
echo "Image URL: $OUTPUT_URL" >&2

# Output JSON for programmatic use
echo "$RESPONSE"
```

## File: `skills/claude.ai/fal-kling-o3/SKILL.md`
```markdown
---
name: fal-kling-o3
description: Generate images and videos with Kling O3 — Kling's most powerful model family. Text-to-image, text-to-video, image-to-video, and video-to-video editing. Use when the user requests "Kling", "Kling O3", "Best quality video", "Kling image", "Kling video editing".
metadata:
  author: fal-ai
  version: "1.0.0"
---

# fal-kling-o3

Kling O3 is Kling's most powerful model family — covering image generation, text-to-video, image-to-video, and video-to-video editing/remix. Two tiers: **Standard** (faster, cheaper) and **Pro** (highest quality).

## Scripts

| Script | Purpose |
|--------|---------|
| `kling-generate.sh` | Generate images with Kling O3 |
| `kling-video.sh` | Generate or edit videos with Kling O3 |

## Usage

### Generate Image
```bash
./scripts/kling-generate.sh --prompt "A samurai standing on a cliff at sunset, cinematic lighting"
```

### Text to Video
```bash
./scripts/kling-video.sh --prompt "A drone shot flying over a tropical island at golden hour" --mode text-to-video
```

### Image to Video
```bash
./scripts/kling-video.sh --image-url "https://example.com/photo.jpg" --prompt "Camera slowly zooms in" --mode image-to-video
```

### Edit Video (change content)
```bash
./scripts/kling-video.sh --video-url "https://example.com/video.mp4" --prompt "Change the sky to a starry night" --mode edit
```

### Remix Video (restyle)
```bash
./scripts/kling-video.sh --video-url "https://example.com/video.mp4" --prompt "Transform into watercolor painting style" --mode remix
```

## Arguments

### kling-generate.sh
| Argument | Description | Required |
|----------|-------------|----------|
| `--prompt` / `-p` | Image description | Yes |
| `--aspect-ratio` | square, landscape, portrait, widescreen | No (default: square) |
| `--param` | Extra param as key=value (repeatable) | No |

### kling-video.sh
| Argument | Description | Required |
|----------|-------------|----------|
| `--prompt` / `-p` | Description or edit instructions | Yes |
| `--mode` | text-to-video, image-to-video, edit, remix | Yes |
| `--image-url` | Image URL (for image-to-video) | For I2V |
| `--video-url` | Video URL (for edit/remix) | For edit/remix |
| `--tier` | standard or pro (default: pro) | No |
| `--param` | Extra param as key=value (repeatable) | No |

## Kling O3 Model Endpoints

### Image Generation
| Endpoint | Tier |
|----------|------|
| `fal-ai/kling-image/o3/text-to-image` | Pro (only tier) |

### Video Generation
| Endpoint | Tier | Mode |
|----------|------|------|
| `fal-ai/kling-video/o3/standard/text-to-video` | Standard | Text → Video |
| `fal-ai/kling-video/o3/pro/text-to-video` | Pro | Text → Video |
| `fal-ai/kling-video/o3/standard/image-to-video` | Standard | Image → Video |
| `fal-ai/kling-video/o3/pro/image-to-video` | Pro | Image → Video |

### Video Editing
| Endpoint | Tier | Mode |
|----------|------|------|
| `fal-ai/kling-video/o3/standard/video-to-video/edit` | Standard | Content editing |
| `fal-ai/kling-video/o3/pro/video-to-video/edit` | Pro | Content editing |
| `fal-ai/kling-video/o3/standard/video-to-video/reference` | Standard | Style remix |
| `fal-ai/kling-video/o3/pro/video-to-video/reference` | Pro | Style remix |

## When to use Standard vs Pro

- **Pro**: Best quality. Use for final output, commercial work, when quality matters most.
- **Standard**: ~2x faster, cheaper. Use for drafts, iteration, when speed matters.

## Output Format
```json
{
  "images": [{"url": "https://fal.media/files/...", "content_type": "image/png"}],
  "video": {"url": "https://fal.media/files/...", "content_type": "video/mp4"}
}
```
```

## File: `skills/claude.ai/fal-kling-o3/scripts/kling-generate.sh`
```bash
#!/bin/bash
set -e

# kling-generate.sh — Generate images with Kling O3

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
MODEL="fal-ai/kling-image/o3/text-to-image"
PROMPT=""
ASPECT_RATIO="1:1"
EXTRA_PARAMS=""

show_help() {
  echo "Usage: $0 --prompt TEXT [options]"
  echo ""
  echo "Options:"
  echo "  --prompt, -p TEXT       Image description (required)"
  echo "  --aspect-ratio RATIO    1:1, 16:9, 9:16, 4:3, 3:4 (default: 1:1)"
  echo "  --param KEY=VALUE       Extra parameter (repeatable)"
  echo "  --add-fal-key KEY       Store FAL_KEY in .env"
  echo "  --help, -h              Show this help"
  exit 0
}

[ -f "$SCRIPT_DIR/../.env" ] && source "$SCRIPT_DIR/../.env"
[ -f ".env" ] && source ".env"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --prompt|-p) PROMPT="$2"; shift 2;;
    --aspect-ratio) ASPECT_RATIO="$2"; shift 2;;
    --param) EXTRA_PARAMS="$EXTRA_PARAMS, \"$(echo "$2" | cut -d= -f1)\": \"$(echo "$2" | cut -d= -f2)\""; shift 2;;
    --add-fal-key) echo "FAL_KEY=$2" > .env; echo "API key saved." >&2; exit 0;;
    --help|-h) show_help;;
    *) echo "Unknown: $1" >&2; exit 1;;
  esac
done

if [ -z "$FAL_KEY" ]; then echo "Error: FAL_KEY not set." >&2; exit 1; fi
if [ -z "$PROMPT" ]; then echo "Error: --prompt required" >&2; exit 1; fi

PAYLOAD="{\"prompt\": \"$PROMPT\", \"aspect_ratio\": \"$ASPECT_RATIO\"$EXTRA_PARAMS}"

echo "Generating with Kling O3 Image..." >&2
SUBMIT=$(curl -s -X POST "https://queue.fal.run/$MODEL" \
  -H "Authorization: Key $FAL_KEY" \
  -H "Content-Type: application/json" \
  -d "$PAYLOAD")

REQUEST_ID=$(echo "$SUBMIT" | jq -r '.request_id // empty')
if [ -z "$REQUEST_ID" ]; then echo "Error: $SUBMIT" >&2; exit 1; fi

echo "Waiting (request: $REQUEST_ID)..." >&2
ELAPSED=0
TIMEOUT=300
POLL=3
while [ "$ELAPSED" -lt "$TIMEOUT" ]; do
  STATUS=$(curl -s "https://queue.fal.run/$MODEL/requests/$REQUEST_ID/status" \
    -H "Authorization: Key $FAL_KEY")
  STATE=$(echo "$STATUS" | jq -r '.status')
  case "$STATE" in
    COMPLETED)
      echo "Done!" >&2
      curl -s "https://queue.fal.run/$MODEL/requests/$REQUEST_ID" \
        -H "Authorization: Key $FAL_KEY" | jq .
      exit 0;;
    FAILED) echo "Failed: $STATUS" >&2; exit 1;;
    *) echo "  $STATE (${ELAPSED}s)" >&2;;
  esac
  sleep "$POLL"
  ELAPSED=$((ELAPSED + POLL))
done
echo "Timed out. Request: $REQUEST_ID" >&2; exit 1
```

## File: `skills/claude.ai/fal-kling-o3/scripts/kling-video.sh`
```bash
#!/bin/bash
set -e

# kling-video.sh — Generate or edit videos with Kling O3

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROMPT=""
MODE=""
IMAGE_URL=""
VIDEO_URL=""
TIER="pro"
EXTRA_PARAMS=""
POLL_INTERVAL=5
TIMEOUT=600

show_help() {
  echo "Usage: $0 --mode MODE --prompt TEXT [options]"
  echo ""
  echo "Modes: text-to-video, image-to-video, edit, remix"
  echo ""
  echo "Options:"
  echo "  --prompt, -p TEXT     Description or edit instructions (required)"
  echo "  --mode MODE           Generation mode (required)"
  echo "  --image-url URL       Image for image-to-video"
  echo "  --video-url URL       Video for edit/remix"
  echo "  --tier TIER           standard or pro (default: pro)"
  echo "  --param KEY=VALUE     Extra parameter (repeatable)"
  echo "  --add-fal-key KEY     Store FAL_KEY in .env"
  echo "  --help, -h            Show this help"
  exit 0
}

[ -f "$SCRIPT_DIR/../.env" ] && source "$SCRIPT_DIR/../.env"
[ -f ".env" ] && source ".env"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --prompt|-p) PROMPT="$2"; shift 2;;
    --mode) MODE="$2"; shift 2;;
    --image-url) IMAGE_URL="$2"; shift 2;;
    --video-url) VIDEO_URL="$2"; shift 2;;
    --tier) TIER="$2"; shift 2;;
    --param) EXTRA_PARAMS="$EXTRA_PARAMS, \"$(echo "$2" | cut -d= -f1)\": \"$(echo "$2" | cut -d= -f2)\""; shift 2;;
    --add-fal-key) echo "FAL_KEY=$2" > .env; echo "API key saved." >&2; exit 0;;
    --help|-h) show_help;;
    *) echo "Unknown: $1" >&2; exit 1;;
  esac
done

if [ -z "$FAL_KEY" ]; then echo "Error: FAL_KEY not set." >&2; exit 1; fi
if [ -z "$MODE" ]; then echo "Error: --mode required (text-to-video/image-to-video/edit/remix)" >&2; exit 1; fi
if [ -z "$PROMPT" ]; then echo "Error: --prompt required" >&2; exit 1; fi

# Select endpoint based on mode and tier
case "$MODE" in
  text-to-video)
    MODEL="fal-ai/kling-video/o3/$TIER/text-to-video"
    PAYLOAD="{\"prompt\": \"$PROMPT\"$EXTRA_PARAMS}";;
  image-to-video)
    if [ -z "$IMAGE_URL" ]; then echo "Error: --image-url required for image-to-video" >&2; exit 1; fi
    MODEL="fal-ai/kling-video/o3/$TIER/image-to-video"
    PAYLOAD="{\"prompt\": \"$PROMPT\", \"image_url\": \"$IMAGE_URL\"$EXTRA_PARAMS}";;
  edit)
    if [ -z "$VIDEO_URL" ]; then echo "Error: --video-url required for edit" >&2; exit 1; fi
    MODEL="fal-ai/kling-video/o3/$TIER/video-to-video/edit"
    PAYLOAD="{\"prompt\": \"$PROMPT\", \"video_url\": \"$VIDEO_URL\"$EXTRA_PARAMS}";;
  remix)
    if [ -z "$VIDEO_URL" ]; then echo "Error: --video-url required for remix" >&2; exit 1; fi
    MODEL="fal-ai/kling-video/o3/$TIER/video-to-video/reference"
    PAYLOAD="{\"prompt\": \"$PROMPT\", \"video_url\": \"$VIDEO_URL\"$EXTRA_PARAMS}";;
  *)
    echo "Error: Unknown mode: $MODE" >&2; exit 1;;
esac

echo "Submitting $MODE ($TIER) to $MODEL..." >&2
SUBMIT=$(curl -s -X POST "https://queue.fal.run/$MODEL" \
  -H "Authorization: Key $FAL_KEY" \
  -H "Content-Type: application/json" \
  -d "$PAYLOAD")

REQUEST_ID=$(echo "$SUBMIT" | jq -r '.request_id // empty')
if [ -z "$REQUEST_ID" ]; then echo "Error: $SUBMIT" >&2; exit 1; fi

echo "Waiting (request: $REQUEST_ID)..." >&2
ELAPSED=0
while [ "$ELAPSED" -lt "$TIMEOUT" ]; do
  STATUS=$(curl -s "https://queue.fal.run/$MODEL/requests/$REQUEST_ID/status?logs=1" \
    -H "Authorization: Key $FAL_KEY")
  STATE=$(echo "$STATUS" | jq -r '.status')
  case "$STATE" in
    COMPLETED)
      echo "Done!" >&2
      curl -s "https://queue.fal.run/$MODEL/requests/$REQUEST_ID" \
        -H "Authorization: Key $FAL_KEY" | jq .
      exit 0;;
    FAILED) echo "Failed!" >&2; echo "$STATUS" | jq . >&2; exit 1;;
    IN_QUEUE)
      POS=$(echo "$STATUS" | jq -r '.queue_position // "?"')
      echo "  Queue position: $POS (${ELAPSED}s)" >&2;;
    IN_PROGRESS)
      LOG=$(echo "$STATUS" | jq -r '.logs[-1].message // empty')
      echo "  Processing${LOG:+: $LOG} (${ELAPSED}s)" >&2;;
  esac
  sleep "$POLL_INTERVAL"
  ELAPSED=$((ELAPSED + POLL_INTERVAL))
done
echo "Timed out after ${TIMEOUT}s. Request: $REQUEST_ID" >&2; exit 1
```

## File: `skills/claude.ai/fal-lip-sync/SKILL.md`
```markdown
---
name: fal-lip-sync
description: Create talking head videos, lip sync audio to video, and animate portraits with expressions. Use when the user requests "Talking head", "Lip sync", "Make this person talk", "Animate portrait", "Live portrait", "Avatar video".
metadata:
  author: fal-ai
  version: "1.0.0"
---

# fal-lip-sync

Create talking head videos, sync lips to audio, and animate portraits using fal.ai models.

## Scripts

| Script | Purpose |
|--------|---------|
| `talking-head.sh` | Generate a talking head video from an image + audio/text |
| `lip-sync.sh` | Sync lips in an existing video to new audio |

## Usage

### Talking Head (Image + Audio → Video)
```bash
./scripts/talking-head.sh --image-url "https://example.com/portrait.jpg" --audio-url "https://example.com/speech.mp3" --model veed/fabric-1.0
```

### Talking Head (Image + Text → Video with auto TTS)
```bash
./scripts/talking-head.sh --image-url "https://example.com/portrait.jpg" --text "Hello, welcome to our presentation" --model fal-ai/creatify/aurora
```

### Lip Sync (Video + Audio → Synced Video)
```bash
./scripts/lip-sync.sh --video-url "https://example.com/video.mp4" --audio-url "https://example.com/new-speech.mp3"
```

## Arguments

### talking-head.sh
| Argument | Description | Required |
|----------|-------------|----------|
| `--image-url` | URL of portrait/face image | Yes |
| `--audio-url` | URL of audio to sync | Yes (or --text) |
| `--text` | Text to speak (auto TTS) | Yes (or --audio-url) |
| `--model` / `-m` | Model endpoint | No (default: veed/fabric-1.0) |
| `--tts-model` | TTS model for --text mode | No (default: fal-ai/minimax/speech-2.6-turbo) |
| `--wait` / `-w` | Wait for completion | No (default: true) |
| `--async` / `-a` | Return request ID immediately | No |

### lip-sync.sh
| Argument | Description | Required |
|----------|-------------|----------|
| `--video-url` | URL of video to lip sync | Yes |
| `--audio-url` | URL of audio to sync to | Yes |
| `--model` / `-m` | Model endpoint | No (default: fal-ai/sync-lipsync/v2) |

## Finding Models

To discover the best and latest lip sync and talking head models, use the search API:

```bash
# Search for talking head models
bash /mnt/skills/user/fal-generate/scripts/search-models.sh --query "talking head"

# Search for lip sync models
bash /mnt/skills/user/fal-generate/scripts/search-models.sh --query "lip sync"

# Search for live portrait / expression transfer
bash /mnt/skills/user/fal-generate/scripts/search-models.sh --query "live portrait"
```

Or use the `search_models` MCP tool with relevant keywords like "lip sync", "talking head", "avatar".

## Output Format
```json
{
  "video": {
    "url": "https://fal.media/files/...",
    "content_type": "video/mp4"
  }
}
```

Present the video URL directly to the user.
```

## File: `skills/claude.ai/fal-lip-sync/scripts/lip-sync.sh`
```bash
#!/bin/bash
set -e

# lip-sync.sh — Sync lips in existing video to new audio

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
MODEL="fal-ai/sync-lipsync/v2"
VIDEO_URL=""
AUDIO_URL=""
POLL_INTERVAL=3
TIMEOUT=600

show_help() {
  echo "Usage: $0 --video-url URL --audio-url URL [options]"
  echo ""
  echo "Options:"
  echo "  --video-url URL    Video to lip sync (required)"
  echo "  --audio-url URL    Audio to sync to (required)"
  echo "  --model, -m MODEL  Model endpoint (default: $MODEL)"
  echo "  --add-fal-key KEY  Store FAL_KEY in .env"
  echo "  --help, -h         Show this help"
  exit 0
}

[ -f "$SCRIPT_DIR/../.env" ] && source "$SCRIPT_DIR/../.env"
[ -f ".env" ] && source ".env"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --video-url) VIDEO_URL="$2"; shift 2;;
    --audio-url) AUDIO_URL="$2"; shift 2;;
    --model|-m) MODEL="$2"; shift 2;;
    --add-fal-key) echo "FAL_KEY=$2" > .env; echo "API key saved." >&2; exit 0;;
    --help|-h) show_help;;
    *) echo "Unknown: $1" >&2; exit 1;;
  esac
done

if [ -z "$FAL_KEY" ]; then echo "Error: FAL_KEY not set." >&2; exit 1; fi
if [ -z "$VIDEO_URL" ]; then echo "Error: --video-url required" >&2; exit 1; fi
if [ -z "$AUDIO_URL" ]; then echo "Error: --audio-url required" >&2; exit 1; fi

PAYLOAD="{\"video_url\": \"$VIDEO_URL\", \"audio_url\": \"$AUDIO_URL\"}"

echo "Submitting lip sync to $MODEL..." >&2
SUBMIT=$(curl -s -X POST "https://queue.fal.run/$MODEL" \
  -H "Authorization: Key $FAL_KEY" \
  -H "Content-Type: application/json" \
  -d "$PAYLOAD")

REQUEST_ID=$(echo "$SUBMIT" | jq -r '.request_id // empty')
if [ -z "$REQUEST_ID" ]; then echo "Error: $SUBMIT" >&2; exit 1; fi

echo "Waiting (request: $REQUEST_ID)..." >&2
ELAPSED=0
while [ "$ELAPSED" -lt "$TIMEOUT" ]; do
  STATUS=$(curl -s "https://queue.fal.run/$MODEL/requests/$REQUEST_ID/status" \
    -H "Authorization: Key $FAL_KEY")
  STATE=$(echo "$STATUS" | jq -r '.status')
  case "$STATE" in
    COMPLETED)
      curl -s "https://queue.fal.run/$MODEL/requests/$REQUEST_ID" \
        -H "Authorization: Key $FAL_KEY" | jq .
      exit 0;;
    FAILED) echo "Failed: $STATUS" >&2; exit 1;;
    *) echo "  $STATE (${ELAPSED}s)" >&2;;
  esac
  sleep "$POLL_INTERVAL"
  ELAPSED=$((ELAPSED + POLL_INTERVAL))
done
echo "Timed out. Request ID: $REQUEST_ID" >&2; exit 1
```

## File: `skills/claude.ai/fal-lip-sync/scripts/talking-head.sh`
```bash
#!/bin/bash
set -e

# talking-head.sh — Generate a talking head video from portrait + audio/text

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
MODEL="veed/fabric-1.0"
TTS_MODEL="fal-ai/minimax/speech-2.6-turbo"
IMAGE_URL=""
AUDIO_URL=""
TEXT=""
ASYNC=false
POLL_INTERVAL=3
TIMEOUT=600

show_help() {
  echo "Usage: $0 --image-url URL [--audio-url URL | --text TEXT] [options]"
  echo ""
  echo "Options:"
  echo "  --image-url URL    Portrait/face image URL (required)"
  echo "  --audio-url URL    Audio URL to sync (required, or use --text)"
  echo "  --text TEXT         Text to speak (auto TTS, alternative to --audio-url)"
  echo "  --model, -m MODEL  Model endpoint (default: $MODEL)"
  echo "  --tts-model MODEL  TTS model for --text mode (default: $TTS_MODEL)"
  echo "  --async, -a        Return request ID immediately"
  echo "  --poll-interval N  Seconds between polls (default: $POLL_INTERVAL)"
  echo "  --timeout N        Max wait seconds (default: $TIMEOUT)"
  echo "  --add-fal-key KEY  Store FAL_KEY in .env"
  echo "  --help, -h         Show this help"
  exit 0
}

# Load env
[ -f "$SCRIPT_DIR/../.env" ] && source "$SCRIPT_DIR/../.env"
[ -f ".env" ] && source ".env"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --image-url) IMAGE_URL="$2"; shift 2;;
    --audio-url) AUDIO_URL="$2"; shift 2;;
    --text) TEXT="$2"; shift 2;;
    --model|-m) MODEL="$2"; shift 2;;
    --tts-model) TTS_MODEL="$2"; shift 2;;
    --async|-a) ASYNC=true; shift;;
    --poll-interval) POLL_INTERVAL="$2"; shift 2;;
    --timeout) TIMEOUT="$2"; shift 2;;
    --add-fal-key) echo "FAL_KEY=$2" > .env; echo "API key saved." >&2; exit 0;;
    --help|-h) show_help;;
    *) echo "Unknown: $1" >&2; exit 1;;
  esac
done

if [ -z "$FAL_KEY" ]; then echo "Error: FAL_KEY not set. Use --add-fal-key or set FAL_KEY env var." >&2; exit 1; fi
if [ -z "$IMAGE_URL" ]; then echo "Error: --image-url is required" >&2; exit 1; fi
if [ -z "$AUDIO_URL" ] && [ -z "$TEXT" ]; then echo "Error: --audio-url or --text is required" >&2; exit 1; fi

# If text mode, generate TTS first
if [ -n "$TEXT" ] && [ -z "$AUDIO_URL" ]; then
  echo "Generating TTS audio..." >&2
  TTS_PAYLOAD=$(cat <<EOF
{"text": "$TEXT"}
EOF
)
  TTS_RESULT=$(curl -s -X POST "https://fal.run/$TTS_MODEL" \
    -H "Authorization: Key $FAL_KEY" \
    -H "Content-Type: application/json" \
    -d "$TTS_PAYLOAD")

  AUDIO_URL=$(echo "$TTS_RESULT" | jq -r '.audio.url // .audio_url.url // .url // empty')
  if [ -z "$AUDIO_URL" ]; then
    echo "Error: TTS failed: $TTS_RESULT" >&2; exit 1
  fi
  echo "TTS audio: $AUDIO_URL" >&2
fi

# Build payload
PAYLOAD=$(cat <<EOF
{"image_url": "$IMAGE_URL", "audio_url": "$AUDIO_URL"}
EOF
)

# Submit to queue
echo "Submitting to $MODEL..." >&2
SUBMIT=$(curl -s -X POST "https://queue.fal.run/$MODEL" \
  -H "Authorization: Key $FAL_KEY" \
  -H "Content-Type: application/json" \
  -d "$PAYLOAD")

REQUEST_ID=$(echo "$SUBMIT" | jq -r '.request_id // empty')
if [ -z "$REQUEST_ID" ]; then
  echo "Error: Submit failed: $SUBMIT" >&2; exit 1
fi

if [ "$ASYNC" = true ]; then
  echo "$REQUEST_ID"
  exit 0
fi

# Poll for completion
echo "Waiting for completion (request: $REQUEST_ID)..." >&2
ELAPSED=0
while [ "$ELAPSED" -lt "$TIMEOUT" ]; do
  STATUS=$(curl -s "https://queue.fal.run/$MODEL/requests/$REQUEST_ID/status?logs=1" \
    -H "Authorization: Key $FAL_KEY")

  STATE=$(echo "$STATUS" | jq -r '.status')
  case "$STATE" in
    COMPLETED)
      echo "Completed!" >&2
      curl -s "https://queue.fal.run/$MODEL/requests/$REQUEST_ID" \
        -H "Authorization: Key $FAL_KEY" | jq .
      exit 0;;
    FAILED)
      echo "Failed!" >&2; echo "$STATUS" | jq . >&2; exit 1;;
    IN_QUEUE)
      POS=$(echo "$STATUS" | jq -r '.queue_position // "?"')
      echo "  Queue position: $POS (${ELAPSED}s elapsed)" >&2;;
    IN_PROGRESS)
      echo "  Processing... (${ELAPSED}s elapsed)" >&2;;
  esac
  sleep "$POLL_INTERVAL"
  ELAPSED=$((ELAPSED + POLL_INTERVAL))
done

echo "Error: Timed out after ${TIMEOUT}s. Request ID: $REQUEST_ID" >&2
exit 1
```

## File: `skills/claude.ai/fal-platform/SKILL.md`
```markdown
---
name: fal-platform
description: fal.ai Platform APIs for model management, pricing, usage tracking, and cost estimation. Use when user asks "show pricing", "check usage", "estimate cost", "setup fal", "add API key", or platform management tasks.
metadata:
  author: fal-ai
  version: "1.0.0"
---

# fal.ai Platform

Platform APIs for model management, pricing, usage tracking, and cost estimation.

## Scripts

| Script | Purpose |
|--------|---------|
| `setup.sh` | Setup FAL_KEY and configuration |
| `pricing.sh` | Get model pricing information |
| `usage.sh` | Check usage and billing |
| `estimate-cost.sh` | Estimate costs for operations |
| `requests.sh` | List and manage requests |

## Setup & Configuration

### Add FAL_KEY

```bash
# Interactive setup
bash /mnt/skills/user/fal-platform/scripts/setup.sh --add-fal-key

# Set key directly
bash /mnt/skills/user/fal-platform/scripts/setup.sh --add-fal-key "your_key_here"

# Show current config
bash /mnt/skills/user/fal-platform/scripts/setup.sh --show-config
```

This adds FAL_KEY to your `.env` file for persistent use.

## Model Pricing

Get pricing for any model:

```bash
# Single model pricing
bash /mnt/skills/user/fal-platform/scripts/pricing.sh --model "fal-ai/flux/dev"

# Multiple models
bash /mnt/skills/user/fal-platform/scripts/pricing.sh --model "fal-ai/flux/dev,fal-ai/kling-video/v2/master/text-to-video"

# All pricing for a category
bash /mnt/skills/user/fal-platform/scripts/pricing.sh --category "text-to-image"
```

**Output:**
```
fal-ai/flux/dev
  Price: $0.025 per image
  Unit: image

fal-ai/kling-video/v2/master/text-to-video
  Price: $0.50 per second
  Unit: video_second
```

## Usage Tracking

Check your usage and spending:

```bash
# Current period usage
bash /mnt/skills/user/fal-platform/scripts/usage.sh

# Filter by model
bash /mnt/skills/user/fal-platform/scripts/usage.sh --model "fal-ai/flux/dev"

# Date range
bash /mnt/skills/user/fal-platform/scripts/usage.sh --start "2024-01-01" --end "2024-01-31"

# Specific timeframe
bash /mnt/skills/user/fal-platform/scripts/usage.sh --timeframe "day"
```

**Timeframes:** `minute`, `hour`, `day`, `week`, `month`

## Estimate Cost

Estimate costs before running:

```bash
# Estimate by API calls (historical pricing)
bash /mnt/skills/user/fal-platform/scripts/estimate-cost.sh \
  --model "fal-ai/flux/dev" \
  --calls 100

# Estimate by units
bash /mnt/skills/user/fal-platform/scripts/estimate-cost.sh \
  --model "fal-ai/kling-video/v2/master/text-to-video" \
  --units 60 \
  --type "unit_price"
```

**Output:**
```
Cost Estimate for fal-ai/flux/dev
  Quantity: 100 calls
  Estimated Cost: $2.50
```

## Request Management

List and manage requests:

```bash
# List recent requests
bash /mnt/skills/user/fal-platform/scripts/requests.sh --model "fal-ai/flux/dev" --limit 10

# Delete request payloads (cleanup)
bash /mnt/skills/user/fal-platform/scripts/requests.sh --delete "request_id_here"
```

## API Endpoints Reference

| Operation | Endpoint | Method |
|-----------|----------|--------|
| Model Search | `GET /models` | GET |
| Pricing | `GET /models/pricing` | GET |
| Usage | `GET /models/usage` | GET |
| List Requests | `GET /models/requests/by-endpoint` | GET |
| Delete Payloads | `DELETE /models/requests/{id}/payloads` | DELETE |

**Base URL:** `https://api.fal.ai/v1`

## Common Flags (All Scripts)

All scripts support these common flags:

```bash
--add-fal-key [KEY]   # Add/update FAL_KEY in .env
--help, -h            # Show help
--json                # Output raw JSON
--quiet, -q           # Suppress status messages
```

## Troubleshooting

### API Key Required
```
Error: FAL_KEY required for this operation

Run: bash /mnt/skills/user/fal-platform/scripts/setup.sh --add-fal-key
```

### Permission Denied
```
Error: API key doesn't have permission for this operation

Some operations require admin API keys. Check your key permissions at:
https://fal.ai/dashboard/keys
```
```

## File: `skills/claude.ai/fal-platform/scripts/estimate-cost.sh`
```bash
#!/bin/bash

# fal.ai Cost Estimation Script
# Usage: ./estimate-cost.sh --model MODEL --calls N | --units N
# Returns estimated costs based on pricing data

set -e

FAL_API_BASE="https://api.fal.ai/v1"

# Default values
MODEL=""
CALLS=""
UNITS=""
OUTPUT_JSON=false

# Check for --add-fal-key first
for arg in "$@"; do
    if [ "$arg" = "--add-fal-key" ]; then
        bash "$(dirname "$0")/setup.sh" "$@"
        exit $?
    fi
done

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --model|-m)
            MODEL="$2"
            shift 2
            ;;
        --calls|-c)
            CALLS="$2"
            shift 2
            ;;
        --units|-u)
            UNITS="$2"
            shift 2
            ;;
        --json)
            OUTPUT_JSON=true
            shift
            ;;
        --help|-h)
            echo "fal.ai Cost Estimation Script" >&2
            echo "" >&2
            echo "Usage:" >&2
            echo "  ./estimate-cost.sh --model MODEL --calls N    Estimate by API calls" >&2
            echo "  ./estimate-cost.sh --model MODEL --units N    Estimate by units" >&2
            echo "" >&2
            echo "Options:" >&2
            echo "  --model, -m   Model ID (required)" >&2
            echo "  --calls, -c   Number of API calls to estimate" >&2
            echo "  --units, -u   Number of billing units to estimate" >&2
            echo "  --json        Output raw JSON" >&2
            echo "  --add-fal-key Setup FAL_KEY" >&2
            echo "" >&2
            echo "Examples:" >&2
            echo "  ./estimate-cost.sh --model \"fal-ai/flux/dev\" --calls 100" >&2
            echo "  ./estimate-cost.sh --model \"fal-ai/kling-video/v2/master/text-to-video\" --units 60" >&2
            exit 0
            ;;
        *)
            shift
            ;;
    esac
done

# Load .env if exists
if [ -f ".env" ]; then
    source .env 2>/dev/null || true
fi

# Check for FAL_KEY
if [ -z "$FAL_KEY" ]; then
    echo "Error: FAL_KEY required" >&2
    echo "" >&2
    echo "Run: ./setup.sh --add-fal-key" >&2
    exit 1
fi

if [ -z "$MODEL" ]; then
    echo "Error: --model is required" >&2
    exit 1
fi

if [ -z "$CALLS" ] && [ -z "$UNITS" ]; then
    echo "Error: --calls or --units is required" >&2
    exit 1
fi

echo "Estimating cost for $MODEL..." >&2

# Get pricing info first
ENCODED_MODEL=$(echo "$MODEL" | sed 's/\//%2F/g')

PRICING_RESPONSE=$(curl -s -X GET "$FAL_API_BASE/models/pricing?endpoint_id=$ENCODED_MODEL" \
    -H "Authorization: Key $FAL_KEY" \
    -H "Content-Type: application/json")

# Check for errors
if echo "$PRICING_RESPONSE" | grep -q '"error"'; then
    ERROR_MSG=$(echo "$PRICING_RESPONSE" | grep -o '"message":"[^"]*"' | head -1 | cut -d'"' -f4)
    echo "Error: $ERROR_MSG" >&2
    exit 1
fi

# Calculate estimate
QUANTITY="${CALLS:-$UNITS}"
ESTIMATE_TYPE="calls"
if [ -n "$UNITS" ]; then
    ESTIMATE_TYPE="units"
fi

echo "" >&2
if command -v python3 &> /dev/null; then
    python3 << PYTHON_EOF - "$PRICING_RESPONSE" "$MODEL" "$QUANTITY" "$ESTIMATE_TYPE"
import json
import sys

response = json.loads(sys.argv[1])
model = sys.argv[2]
quantity = float(sys.argv[3])
estimate_type = sys.argv[4]

print(f"Cost Estimate: {model}", file=sys.stderr)
print("=" * (len(model) + 15), file=sys.stderr)
print("", file=sys.stderr)

# Extract pricing data
prices = response.get('prices', [response] if isinstance(response, dict) else response)
if isinstance(prices, list) and len(prices) > 0:
    price_info = prices[0]
    unit_price = float(price_info.get('unit_price', 0))
    unit = price_info.get('unit', 'call')
    currency = price_info.get('currency', 'USD')

    # Calculate estimated cost
    estimated_cost = unit_price * quantity

    print(f"  Unit Price: {unit_price} {currency} per {unit}", file=sys.stderr)
    print(f"  Quantity: {quantity:.0f} {estimate_type}", file=sys.stderr)
    print(f"  Estimated Cost: {estimated_cost:.4f} {currency}", file=sys.stderr)

    # Output JSON
    result = {
        "model": model,
        "unit_price": unit_price,
        "unit": unit,
        "quantity": quantity,
        "estimated_cost": estimated_cost,
        "currency": currency
    }
    print(json.dumps(result))
else:
    print("  Unable to calculate estimate - pricing data not found", file=sys.stderr)
    print(json.dumps({"error": "pricing data not found"}))
PYTHON_EOF
else
    echo "  Python3 required for calculation" >&2
fi
```

## File: `skills/claude.ai/fal-platform/scripts/pricing.sh`
```bash
#!/bin/bash

# fal.ai Pricing Script
# Usage: ./pricing.sh --model MODEL [--category CATEGORY]
# Returns pricing information for models

set -e

FAL_API_BASE="https://api.fal.ai/v1"

# Default values
MODELS=""
CATEGORY=""
OUTPUT_JSON=false

# Check for --add-fal-key first
for arg in "$@"; do
    if [ "$arg" = "--add-fal-key" ]; then
        bash "$(dirname "$0")/setup.sh" "$@"
        exit $?
    fi
done

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --model|-m)
            MODELS="$2"
            shift 2
            ;;
        --category|-c)
            CATEGORY="$2"
            shift 2
            ;;
        --json)
            OUTPUT_JSON=true
            shift
            ;;
        --help|-h)
            echo "fal.ai Pricing Script" >&2
            echo "" >&2
            echo "Usage:" >&2
            echo "  ./pricing.sh --model MODEL           Get pricing for model(s)" >&2
            echo "  ./pricing.sh --category CATEGORY     Get pricing for category" >&2
            echo "" >&2
            echo "Options:" >&2
            echo "  --model, -m     Model ID(s), comma-separated" >&2
            echo "  --category, -c  Filter by category" >&2
            echo "  --json          Output raw JSON" >&2
            echo "  --add-fal-key   Setup FAL_KEY" >&2
            echo "" >&2
            echo "Examples:" >&2
            echo "  ./pricing.sh --model \"fal-ai/flux/dev\"" >&2
            echo "  ./pricing.sh --model \"fal-ai/flux/dev,fal-ai/kling-video/v2/master/text-to-video\"" >&2
            exit 0
            ;;
        *)
            shift
            ;;
    esac
done

# Load .env if exists
if [ -f ".env" ]; then
    source .env 2>/dev/null || true
fi

# Check for FAL_KEY
if [ -z "$FAL_KEY" ]; then
    echo "Error: FAL_KEY required" >&2
    echo "" >&2
    echo "Run: ./setup.sh --add-fal-key" >&2
    exit 1
fi

if [ -z "$MODELS" ] && [ -z "$CATEGORY" ]; then
    echo "Error: --model or --category required" >&2
    exit 1
fi

echo "Fetching pricing information..." >&2

# Build endpoint URL
if [ -n "$MODELS" ]; then
    # URL encode the model IDs
    ENCODED_MODELS=$(echo "$MODELS" | sed 's/,/%2C/g' | sed 's/\//%2F/g')
    ENDPOINT="$FAL_API_BASE/models/pricing?endpoint_id=$ENCODED_MODELS"
else
    ENDPOINT="$FAL_API_BASE/models?category=$CATEGORY&include_pricing=true"
fi

# Make API request
RESPONSE=$(curl -s -X GET "$ENDPOINT" \
    -H "Authorization: Key $FAL_KEY" \
    -H "Content-Type: application/json")

# Check for errors
if echo "$RESPONSE" | grep -q '"error"'; then
    ERROR_MSG=$(echo "$RESPONSE" | grep -o '"message":"[^"]*"' | head -1 | cut -d'"' -f4)
    echo "Error: $ERROR_MSG" >&2
    exit 1
fi

if [ "$OUTPUT_JSON" = true ]; then
    echo "$RESPONSE"
    exit 0
fi

# Parse and display pricing
echo "" >&2
if command -v python3 &> /dev/null; then
    python3 << 'PYTHON_EOF' - "$RESPONSE"
import json
import sys

response = json.loads(sys.argv[1])
data = response.get('data', response)

if isinstance(data, list):
    for item in data:
        endpoint = item.get('endpoint_id', 'Unknown')
        pricing = item.get('pricing', {})
        print(f"{endpoint}", file=sys.stderr)

        if pricing:
            price = pricing.get('price', 'N/A')
            unit = pricing.get('unit', 'call')
            print(f"  Price: ${price} per {unit}", file=sys.stderr)
        else:
            print(f"  Pricing: Not available", file=sys.stderr)
        print("", file=sys.stderr)
elif isinstance(data, dict):
    for endpoint, info in data.items():
        print(f"{endpoint}", file=sys.stderr)
        if isinstance(info, dict):
            price = info.get('price', info.get('unit_price', 'N/A'))
            unit = info.get('unit', info.get('billing_unit', 'call'))
            print(f"  Price: ${price} per {unit}", file=sys.stderr)
        print("", file=sys.stderr)
PYTHON_EOF
fi

echo "$RESPONSE"
```

## File: `skills/claude.ai/fal-platform/scripts/requests.sh`
```bash
#!/bin/bash

# fal.ai Requests Management Script
# Usage: ./requests.sh --model MODEL [--limit N] | --delete REQUEST_ID
# List and manage API requests

set -e

FAL_API_BASE="https://api.fal.ai/v1"

# Default values
MODEL=""
LIMIT=10
DELETE_ID=""
OUTPUT_JSON=false

# Check for --add-fal-key first
for arg in "$@"; do
    if [ "$arg" = "--add-fal-key" ]; then
        bash "$(dirname "$0")/setup.sh" "$@"
        exit $?
    fi
done

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --model|-m)
            MODEL="$2"
            shift 2
            ;;
        --limit|-l)
            LIMIT="$2"
            shift 2
            ;;
        --delete|-d)
            DELETE_ID="$2"
            shift 2
            ;;
        --json)
            OUTPUT_JSON=true
            shift
            ;;
        --help|-h)
            echo "fal.ai Requests Management Script" >&2
            echo "" >&2
            echo "Usage:" >&2
            echo "  ./requests.sh --model MODEL          List requests for model" >&2
            echo "  ./requests.sh --delete REQUEST_ID    Delete request payloads" >&2
            echo "" >&2
            echo "Options:" >&2
            echo "  --model, -m   Model ID to filter" >&2
            echo "  --limit, -l   Max results (default: 10)" >&2
            echo "  --delete, -d  Request ID to delete payloads" >&2
            echo "  --json        Output raw JSON" >&2
            echo "  --add-fal-key Setup FAL_KEY" >&2
            echo "" >&2
            echo "Examples:" >&2
            echo "  ./requests.sh --model \"fal-ai/flux/dev\" --limit 5" >&2
            echo "  ./requests.sh --delete \"req_abc123\"" >&2
            exit 0
            ;;
        *)
            shift
            ;;
    esac
done

# Load .env if exists
if [ -f ".env" ]; then
    source .env 2>/dev/null || true
fi

# Check for FAL_KEY
if [ -z "$FAL_KEY" ]; then
    echo "Error: FAL_KEY required" >&2
    echo "" >&2
    echo "Run: ./setup.sh --add-fal-key" >&2
    exit 1
fi

# Delete request payloads
if [ -n "$DELETE_ID" ]; then
    echo "Deleting payloads for request $DELETE_ID..." >&2

    RESPONSE=$(curl -s -X DELETE "$FAL_API_BASE/models/requests/$DELETE_ID/payloads" \
        -H "Authorization: Key $FAL_KEY" \
        -H "Content-Type: application/json")

    if echo "$RESPONSE" | grep -q '"error"'; then
        ERROR_MSG=$(echo "$RESPONSE" | grep -o '"message":"[^"]*"' | head -1 | cut -d'"' -f4)
        echo "Error: $ERROR_MSG" >&2
        exit 1
    fi

    echo "Payloads deleted successfully" >&2
    echo "$RESPONSE"
    exit 0
fi

# List requests
if [ -z "$MODEL" ]; then
    echo "Error: --model is required for listing requests" >&2
    exit 1
fi

echo "Fetching requests for $MODEL..." >&2

ENCODED_MODEL=$(echo "$MODEL" | sed 's/\//%2F/g')

RESPONSE=$(curl -s -X GET "$FAL_API_BASE/models/requests/by-endpoint?endpoint_id=$ENCODED_MODEL&limit=$LIMIT" \
    -H "Authorization: Key $FAL_KEY" \
    -H "Content-Type: application/json")

# Check for errors
if echo "$RESPONSE" | grep -q '"error"'; then
    ERROR_MSG=$(echo "$RESPONSE" | grep -o '"message":"[^"]*"' | head -1 | cut -d'"' -f4)
    echo "Error: $ERROR_MSG" >&2
    exit 1
fi

if [ "$OUTPUT_JSON" = true ]; then
    echo "$RESPONSE"
    exit 0
fi

# Parse and display requests
echo "" >&2
if command -v python3 &> /dev/null; then
    python3 << 'PYTHON_EOF' - "$RESPONSE"
import json
import sys

response = json.loads(sys.argv[1])
data = response.get('data', response)

if isinstance(data, list):
    print(f"Recent Requests ({len(data)} shown)", file=sys.stderr)
    print("=" * 40, file=sys.stderr)

    for req in data:
        request_id = req.get('request_id', req.get('id', 'unknown'))
        status = req.get('status', 'unknown')
        created = req.get('created_at', req.get('timestamp', ''))[:19]
        duration = req.get('duration', 0)

        print(f"", file=sys.stderr)
        print(f"  ID: {request_id}", file=sys.stderr)
        print(f"  Status: {status}", file=sys.stderr)
        print(f"  Created: {created}", file=sys.stderr)
        if duration:
            print(f"  Duration: {duration:.2f}s", file=sys.stderr)
else:
    print("No requests found", file=sys.stderr)
PYTHON_EOF
fi

echo "$RESPONSE"
```

## File: `skills/claude.ai/fal-platform/scripts/setup.sh`
```bash
#!/bin/bash

# fal.ai Setup Script
# Usage: ./setup.sh --add-fal-key [KEY] | --show-config
# Manages FAL_KEY and configuration

set -e

ENV_FILE=".env"
ACTION=""
FAL_KEY_VALUE=""

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --add-fal-key)
            ACTION="add-key"
            if [[ -n "$2" && ! "$2" =~ ^-- ]]; then
                FAL_KEY_VALUE="$2"
                shift
            fi
            shift
            ;;
        --show-config)
            ACTION="show-config"
            shift
            ;;
        --help|-h)
            echo "fal.ai Setup Script" >&2
            echo "" >&2
            echo "Usage:" >&2
            echo "  ./setup.sh --add-fal-key [KEY]  Add or update FAL_KEY" >&2
            echo "  ./setup.sh --show-config        Show current configuration" >&2
            echo "" >&2
            echo "Examples:" >&2
            echo "  ./setup.sh --add-fal-key                    # Interactive prompt" >&2
            echo "  ./setup.sh --add-fal-key \"your_key_here\"    # Direct set" >&2
            echo "" >&2
            echo "Get your API key at: https://fal.ai/dashboard/keys" >&2
            exit 0
            ;;
        *)
            echo "Unknown option: $1" >&2
            echo "Use --help for usage information" >&2
            exit 1
            ;;
    esac
done

# Show config
if [ "$ACTION" = "show-config" ]; then
    echo "fal.ai Configuration" >&2
    echo "===================" >&2

    if [ -f "$ENV_FILE" ]; then
        echo "Environment file: $ENV_FILE" >&2
        if grep -q "FAL_KEY" "$ENV_FILE" 2>/dev/null; then
            KEY=$(grep "FAL_KEY" "$ENV_FILE" | cut -d'=' -f2 | tr -d '"' | tr -d "'")
            MASKED="${KEY:0:8}...${KEY: -4}"
            echo "FAL_KEY: $MASKED (set)" >&2
        else
            echo "FAL_KEY: not set" >&2
        fi
    else
        echo "Environment file: not found" >&2
    fi

    if [ -n "$FAL_KEY" ]; then
        MASKED="${FAL_KEY:0:8}...${FAL_KEY: -4}"
        echo "FAL_KEY (env): $MASKED" >&2
    fi

    exit 0
fi

# Add FAL_KEY
if [ "$ACTION" = "add-key" ]; then
    # Get key value
    if [ -z "$FAL_KEY_VALUE" ]; then
        echo "Enter your fal.ai API key:" >&2
        echo "(Get it from https://fal.ai/dashboard/keys)" >&2
        read -r FAL_KEY_VALUE
    fi

    if [ -z "$FAL_KEY_VALUE" ]; then
        echo "Error: No API key provided" >&2
        exit 1
    fi

    # Validate key format (basic check)
    if [[ ! "$FAL_KEY_VALUE" =~ ^[a-zA-Z0-9_-]+$ ]]; then
        echo "Warning: API key contains unusual characters" >&2
    fi

    # Update or create .env file
    if [ -f "$ENV_FILE" ]; then
        # Remove existing FAL_KEY line
        grep -v "^FAL_KEY=" "$ENV_FILE" > "$ENV_FILE.tmp" 2>/dev/null || true
        mv "$ENV_FILE.tmp" "$ENV_FILE"
    fi

    # Add new FAL_KEY
    echo "FAL_KEY=$FAL_KEY_VALUE" >> "$ENV_FILE"

    echo "" >&2
    echo "FAL_KEY saved to $ENV_FILE" >&2
    echo "" >&2
    echo "To use in current session, run:" >&2
    echo "  source $ENV_FILE" >&2
    echo "" >&2
    echo "Or export directly:" >&2
    echo "  export FAL_KEY=$FAL_KEY_VALUE" >&2

    # Output JSON
    echo "{\"success\": true, \"env_file\": \"$ENV_FILE\"}"
    exit 0
fi

# Default: show help
echo "fal.ai Setup Script" >&2
echo "" >&2
echo "Usage:" >&2
echo "  ./setup.sh --add-fal-key [KEY]  Add or update FAL_KEY" >&2
echo "  ./setup.sh --show-config        Show current configuration" >&2
echo "" >&2
echo "Get your API key at: https://fal.ai/dashboard/keys" >&2
```

## File: `skills/claude.ai/fal-platform/scripts/usage.sh`
```bash
#!/bin/bash

# fal.ai Usage Script
# Usage: ./usage.sh [--model MODEL] [--start DATE] [--end DATE] [--timeframe TF]
# Returns usage information and billing

set -e

FAL_API_BASE="https://api.fal.ai/v1"

# Default values
MODEL=""
START_DATE=""
END_DATE=""
TIMEFRAME=""
OUTPUT_JSON=false

# Check for --add-fal-key first
for arg in "$@"; do
    if [ "$arg" = "--add-fal-key" ]; then
        bash "$(dirname "$0")/setup.sh" "$@"
        exit $?
    fi
done

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --model|-m)
            MODEL="$2"
            shift 2
            ;;
        --start|-s)
            START_DATE="$2"
            shift 2
            ;;
        --end|-e)
            END_DATE="$2"
            shift 2
            ;;
        --timeframe|-t)
            TIMEFRAME="$2"
            shift 2
            ;;
        --json)
            OUTPUT_JSON=true
            shift
            ;;
        --help|-h)
            echo "fal.ai Usage Script" >&2
            echo "" >&2
            echo "Usage:" >&2
            echo "  ./usage.sh                           Get current usage" >&2
            echo "  ./usage.sh --model MODEL             Filter by model" >&2
            echo "  ./usage.sh --start DATE --end DATE   Date range" >&2
            echo "" >&2
            echo "Options:" >&2
            echo "  --model, -m      Model ID to filter" >&2
            echo "  --start, -s      Start date (ISO8601 or YYYY-MM-DD)" >&2
            echo "  --end, -e        End date" >&2
            echo "  --timeframe, -t  Aggregation: minute, hour, day, week, month" >&2
            echo "  --json           Output raw JSON" >&2
            echo "  --add-fal-key    Setup FAL_KEY" >&2
            echo "" >&2
            echo "Examples:" >&2
            echo "  ./usage.sh" >&2
            echo "  ./usage.sh --model \"fal-ai/flux/dev\"" >&2
            echo "  ./usage.sh --start \"2024-01-01\" --end \"2024-01-31\"" >&2
            exit 0
            ;;
        *)
            shift
            ;;
    esac
done

# Load .env if exists
if [ -f ".env" ]; then
    source .env 2>/dev/null || true
fi

# Check for FAL_KEY
if [ -z "$FAL_KEY" ]; then
    echo "Error: FAL_KEY required" >&2
    echo "" >&2
    echo "Run: ./setup.sh --add-fal-key" >&2
    exit 1
fi

echo "Fetching usage information..." >&2

# Build query parameters
PARAMS="expand=time_series,summary"

if [ -n "$MODEL" ]; then
    ENCODED_MODEL=$(echo "$MODEL" | sed 's/\//%2F/g')
    PARAMS="$PARAMS&endpoint_id=$ENCODED_MODEL"
fi

if [ -n "$START_DATE" ]; then
    PARAMS="$PARAMS&start=$START_DATE"
fi

if [ -n "$END_DATE" ]; then
    PARAMS="$PARAMS&end=$END_DATE"
fi

if [ -n "$TIMEFRAME" ]; then
    PARAMS="$PARAMS&timeframe=$TIMEFRAME"
fi

# Make API request
RESPONSE=$(curl -s -X GET "$FAL_API_BASE/models/usage?$PARAMS" \
    -H "Authorization: Key $FAL_KEY" \
    -H "Content-Type: application/json")

# Check for errors
if echo "$RESPONSE" | grep -q '"error"'; then
    ERROR_MSG=$(echo "$RESPONSE" | grep -o '"message":"[^"]*"' | head -1 | cut -d'"' -f4)
    echo "Error: $ERROR_MSG" >&2
    exit 1
fi

if [ "$OUTPUT_JSON" = true ]; then
    echo "$RESPONSE"
    exit 0
fi

# Parse and display usage
echo "" >&2
if command -v python3 &> /dev/null; then
    python3 << 'PYTHON_EOF' - "$RESPONSE"
import json
import sys

response = json.loads(sys.argv[1])

# Handle both dict and list responses
if isinstance(response, list):
    data = response
else:
    data = response.get('time_series', response.get('data', []))

    # Summary if available
    summary = response.get('summary', {})
    if isinstance(summary, dict) and summary:
        print("Usage Summary", file=sys.stderr)
        print("=============", file=sys.stderr)
        total_cost = summary.get('total_cost', summary.get('cost', 0))
        total_requests = summary.get('total_requests', summary.get('request_count', 0))
        print(f"  Total Cost: ${total_cost:.4f}", file=sys.stderr)
        print(f"  Total Requests: {total_requests}", file=sys.stderr)
        print("", file=sys.stderr)

# Process time_series data
if isinstance(data, list) and len(data) > 0:
    by_endpoint = {}
    for bucket in data:
        results = bucket.get('results', [bucket]) if isinstance(bucket, dict) else [bucket]
        for item in results:
            if not isinstance(item, dict):
                continue
            endpoint = item.get('endpoint_id', '')
            if not endpoint:
                continue
            if endpoint not in by_endpoint:
                by_endpoint[endpoint] = {'cost': 0, 'quantity': 0}
            by_endpoint[endpoint]['cost'] += float(item.get('cost', 0))
            by_endpoint[endpoint]['quantity'] += float(item.get('quantity', item.get('request_count', 0)))

    if by_endpoint:
        print("Usage by Endpoint", file=sys.stderr)
        print("=================", file=sys.stderr)
        for endpoint, stats in by_endpoint.items():
            print(f"  {endpoint}", file=sys.stderr)
            print(f"    Cost: ${stats['cost']:.4f}", file=sys.stderr)
            print(f"    Quantity: {stats['quantity']:.2f}", file=sys.stderr)
    else:
        print("No usage data found for this period", file=sys.stderr)
PYTHON_EOF
fi

echo "$RESPONSE"
```

## File: `skills/claude.ai/fal-realtime/SKILL.md`
```markdown
---
name: fal-realtime
description: Real-time and streaming AI image generation — instant results for interactive use. Use when the user requests "Real-time generation", "Fast generation", "Streaming image", "Instant image", "Live generation", "Realtime".
metadata:
  author: fal-ai
  version: "1.0.0"
---

# fal-realtime

Real-time and streaming image generation using fal.ai's fastest models. Results in under 1 second — ideal for interactive applications, live previews, and rapid iteration.

## Scripts

| Script | Purpose |
|--------|---------|
| `realtime.sh` | Generate images in real-time (sub-second) |

## Usage

### Quick Real-Time Generation
```bash
./scripts/realtime.sh --prompt "A cute cat wearing a top hat"
```

### With LoRA
```bash
./scripts/realtime.sh --prompt "A portrait in sks style" --lora-url "https://example.com/lora.safetensors"
```

### Multiple Rapid Iterations
```bash
./scripts/realtime.sh --prompt "Abstract art with flowing colors, version 1"
./scripts/realtime.sh --prompt "Abstract art with flowing colors, version 2, more vibrant"
./scripts/realtime.sh --prompt "Abstract art with flowing colors, version 3, darker tones"
```

## Arguments

| Argument | Description | Required |
|----------|-------------|----------|
| `--prompt` / `-p` | Image description | Yes |
| `--model` / `-m` | Model endpoint | No (default: fal-ai/flux-2/klein/realtime) |
| `--size` | square, landscape, portrait | No (default: square) |
| `--seed` | Random seed for reproducibility | No |
| `--lora-url` | URL to LoRA weights | No |
| `--lora-scale` | LoRA influence (0.0-1.0, default: 1.0) | No |
| `--num-images` | Number of images (default: 1) | No |

## Finding Models

To discover the best and latest real-time generation models, use the search API:

```bash
# Search for real-time / fast image generation models
bash /mnt/skills/user/fal-generate/scripts/search-models.sh --query "realtime"
bash /mnt/skills/user/fal-generate/scripts/search-models.sh --query "fast image"
bash /mnt/skills/user/fal-generate/scripts/search-models.sh --category "text-to-image"
```

Or use the `search_models` MCP tool with keywords like "realtime", "fast", "schnell", "turbo".

## When to Use Real-Time vs Standard Generation

| Use Case | Use Real-Time | Use Standard |
|----------|--------------|--------------|
| Rapid prototyping / iteration | Yes | |
| Interactive apps / live preview | Yes | |
| Final high-quality output | | Yes (FLUX Dev, Nano Banana Pro) |
| Professional / commercial work | | Yes (FLUX Pro Ultra) |
| Exploring prompt ideas quickly | Yes | |
| Batch generation with variations | Yes | |

## Output Format
```json
{
  "images": [
    {
      "url": "https://fal.media/files/...",
      "content_type": "image/jpeg",
      "width": 1024,
      "height": 1024
    }
  ],
  "seed": 12345,
  "has_nsfw_concepts": [false]
}
```

## Tips

- Real-time models use fewer inference steps — prompts should be clear and concise
- Use `--seed` to lock in a good composition, then iterate on the prompt
- LoRA support works with FLUX Klein Realtime — great for style-locked fast iteration
- These models use the synchronous API (no queue), so results are instant
```

## File: `skills/claude.ai/fal-realtime/scripts/realtime.sh`
```bash
#!/bin/bash
set -e

# realtime.sh — Real-time image generation (sub-second)

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
MODEL="fal-ai/flux-2/klein/realtime"
PROMPT=""
SIZE="square"
SEED=""
LORA_URL=""
LORA_SCALE=""
NUM_IMAGES=1

show_help() {
  echo "Usage: $0 --prompt TEXT [options]"
  echo ""
  echo "Options:"
  echo "  --prompt, -p TEXT       Image description (required)"
  echo "  --model, -m MODEL       Model (default: $MODEL)"
  echo "  --size SIZE             square, landscape, portrait (default: square)"
  echo "  --seed N                Random seed for reproducibility"
  echo "  --lora-url URL          LoRA weights URL"
  echo "  --lora-scale N          LoRA scale 0.0-1.0 (default: 1.0)"
  echo "  --num-images N          Number of images (default: 1)"
  echo "  --add-fal-key KEY       Store FAL_KEY in .env"
  echo "  --help, -h              Show this help"
  exit 0
}

[ -f "$SCRIPT_DIR/../.env" ] && source "$SCRIPT_DIR/../.env"
[ -f ".env" ] && source ".env"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --prompt|-p) PROMPT="$2"; shift 2;;
    --model|-m) MODEL="$2"; shift 2;;
    --size) SIZE="$2"; shift 2;;
    --seed) SEED="$2"; shift 2;;
    --lora-url) LORA_URL="$2"; shift 2;;
    --lora-scale) LORA_SCALE="$2"; shift 2;;
    --num-images) NUM_IMAGES="$2"; shift 2;;
    --add-fal-key) echo "FAL_KEY=$2" > .env; echo "API key saved." >&2; exit 0;;
    --help|-h) show_help;;
    *) echo "Unknown: $1" >&2; exit 1;;
  esac
done

if [ -z "$FAL_KEY" ]; then echo "Error: FAL_KEY not set." >&2; exit 1; fi
if [ -z "$PROMPT" ]; then echo "Error: --prompt required" >&2; exit 1; fi

# Map size to dimensions
case "$SIZE" in
  square) IMAGE_SIZE="{\"width\": 1024, \"height\": 1024}";;
  landscape) IMAGE_SIZE="{\"width\": 1344, \"height\": 768}";;
  portrait) IMAGE_SIZE="{\"width\": 768, \"height\": 1344}";;
  *) IMAGE_SIZE="{\"width\": 1024, \"height\": 1024}";;
esac

# Build payload
PAYLOAD="{\"prompt\": \"$PROMPT\", \"image_size\": $IMAGE_SIZE, \"num_images\": $NUM_IMAGES"
if [ -n "$SEED" ]; then PAYLOAD="$PAYLOAD, \"seed\": $SEED"; fi
if [ -n "$LORA_URL" ]; then
  SCALE="${LORA_SCALE:-1.0}"
  PAYLOAD="$PAYLOAD, \"loras\": [{\"path\": \"$LORA_URL\", \"scale\": $SCALE}]"
fi
PAYLOAD="$PAYLOAD}"

# Real-time = synchronous API (no queue)
echo "Generating (real-time)..." >&2
START_TIME=$(date +%s%N 2>/dev/null || date +%s)

RESULT=$(curl -s -X POST "https://fal.run/$MODEL" \
  -H "Authorization: Key $FAL_KEY" \
  -H "Content-Type: application/json" \
  -d "$PAYLOAD")

END_TIME=$(date +%s%N 2>/dev/null || date +%s)

if echo "$RESULT" | jq -e '.error' > /dev/null 2>&1; then
  echo "Error: $RESULT" >&2; exit 1
fi

# Calculate duration (nanoseconds if available, else seconds)
if [ ${#START_TIME} -gt 10 ]; then
  DURATION_MS=$(( (END_TIME - START_TIME) / 1000000 ))
  echo "Generated in ${DURATION_MS}ms" >&2
else
  DURATION_S=$((END_TIME - START_TIME))
  echo "Generated in ${DURATION_S}s" >&2
fi

echo "$RESULT" | jq .
```

## File: `skills/claude.ai/fal-restore/SKILL.md`
```markdown
---
name: fal-restore
description: Restore and fix image quality — deblur, denoise, dehaze, fix faces, restore documents. Use when the user requests "Fix blurry image", "Remove noise", "Fix face", "Restore photo", "Enhance document", "Deblur", "Denoise".
metadata:
  author: fal-ai
  version: "1.0.0"
---

# fal-restore

Restore and enhance image quality using AI — fix blur, noise, haze, faces, and documents.

## Scripts

| Script | Purpose |
|--------|---------|
| `restore.sh` | Restore an image (deblur, denoise, dehaze, fix-face, document) |

## Usage

### Deblur
```bash
./scripts/restore.sh --image-url "https://example.com/blurry.jpg" --operation deblur
```

### Denoise
```bash
./scripts/restore.sh --image-url "https://example.com/noisy.jpg" --operation denoise
```

### Fix Face
```bash
./scripts/restore.sh --image-url "https://example.com/bad-face.jpg" --operation fix-face
```

### Restore Document
```bash
./scripts/restore.sh --image-url "https://example.com/scan.jpg" --operation document
```

## Arguments

| Argument | Description | Required |
|----------|-------------|----------|
| `--image-url` | URL of image to restore | Yes |
| `--operation` | deblur, denoise, dehaze, fix-face, document | Yes |
| `--model` / `-m` | Override model endpoint | No |
| `--fidelity` | For fix-face: 0.0-1.0 (0=max quality, 1=most faithful) | No |

## Finding Models

To discover the best and latest image restoration models, use the search API:

```bash
# Search for restoration models
bash /mnt/skills/user/fal-generate/scripts/search-models.sh --query "restore"
bash /mnt/skills/user/fal-generate/scripts/search-models.sh --query "deblur"
bash /mnt/skills/user/fal-generate/scripts/search-models.sh --query "denoise"
bash /mnt/skills/user/fal-generate/scripts/search-models.sh --query "face restoration"
bash /mnt/skills/user/fal-generate/scripts/search-models.sh --query "document"
```

Or use the `search_models` MCP tool with keywords like "restore", "deblur", "denoise", "face fix", "document".
```

## File: `skills/claude.ai/fal-restore/scripts/restore.sh`
```bash
#!/bin/bash
set -e

# restore.sh — Restore image quality (deblur, denoise, dehaze, fix-face, document)

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
IMAGE_URL=""
OPERATION=""
MODEL=""
FIDELITY=""

show_help() {
  echo "Usage: $0 --image-url URL --operation OP [options]"
  echo ""
  echo "Operations: deblur, denoise, dehaze, fix-face, document"
  echo ""
  echo "Options:"
  echo "  --image-url URL     Image URL (required)"
  echo "  --operation OP      Restoration operation (required)"
  echo "  --model, -m MODEL   Override model endpoint"
  echo "  --fidelity F        For fix-face: 0.0-1.0 (0=max quality, 1=faithful)"
  echo "  --add-fal-key KEY   Store FAL_KEY in .env"
  echo "  --help, -h          Show this help"
  exit 0
}

[ -f "$SCRIPT_DIR/../.env" ] && source "$SCRIPT_DIR/../.env"
[ -f ".env" ] && source ".env"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --image-url) IMAGE_URL="$2"; shift 2;;
    --operation) OPERATION="$2"; shift 2;;
    --model|-m) MODEL="$2"; shift 2;;
    --fidelity) FIDELITY="$2"; shift 2;;
    --add-fal-key) echo "FAL_KEY=$2" > .env; echo "API key saved." >&2; exit 0;;
    --help|-h) show_help;;
    *) echo "Unknown: $1" >&2; exit 1;;
  esac
done

if [ -z "$FAL_KEY" ]; then echo "Error: FAL_KEY not set." >&2; exit 1; fi
if [ -z "$IMAGE_URL" ]; then echo "Error: --image-url required" >&2; exit 1; fi
if [ -z "$OPERATION" ]; then echo "Error: --operation required" >&2; exit 1; fi

# Auto-select model
if [ -z "$MODEL" ]; then
  case "$OPERATION" in
    deblur) MODEL="fal-ai/nafnet/deblur";;
    denoise) MODEL="fal-ai/nafnet/denoise";;
    dehaze) MODEL="fal-ai/mix-dehaze-net";;
    fix-face) MODEL="fal-ai/codeformer";;
    document) MODEL="fal-ai/docres";;
    *) echo "Error: Unknown operation: $OPERATION" >&2; exit 1;;
  esac
fi

# Build payload
PAYLOAD="{\"image_url\": \"$IMAGE_URL\""
if [ "$OPERATION" = "fix-face" ] && [ -n "$FIDELITY" ]; then
  PAYLOAD="$PAYLOAD, \"fidelity\": $FIDELITY"
fi
PAYLOAD="$PAYLOAD}"

echo "Running $OPERATION with $MODEL..." >&2
RESULT=$(curl -s -X POST "https://fal.run/$MODEL" \
  -H "Authorization: Key $FAL_KEY" \
  -H "Content-Type: application/json" \
  -d "$PAYLOAD")

if echo "$RESULT" | jq -e '.error' > /dev/null 2>&1; then
  echo "Error: $RESULT" >&2; exit 1
fi

echo "$RESULT" | jq .
```

## File: `skills/claude.ai/fal-train/SKILL.md`
```markdown
---
name: fal-train
description: Train custom AI models (LoRA) on fal.ai — personalize image generation for specific people, styles, objects, or video generation. Use when the user requests "Train model", "Train LoRA", "Fine-tune", "Custom model", "Train on my images", "Portrait training".
metadata:
  author: fal-ai
  version: "1.0.0"
---

# fal-train

Train custom LoRA models on fal.ai for personalized AI generation.

## Scripts

| Script | Purpose |
|--------|---------|
| `train.sh` | Submit a LoRA training job |

## Usage

### Train Image LoRA (Style/Subject/Person)
```bash
./scripts/train.sh --images-url "https://example.com/training-images.zip" --trigger-word "sks style" --model fal-ai/flux-lora-fast-training
```

### Train Portrait LoRA
```bash
./scripts/train.sh --images-url "https://example.com/face-photos.zip" --trigger-word "ohwx person" --model fal-ai/flux-lora-portrait-trainer
```

### Check Training Status
```bash
./scripts/train.sh --status --endpoint fal-ai/flux-lora-fast-training --request-id "abc123"
```

## Arguments

| Argument | Description | Required |
|----------|-------------|----------|
| `--images-url` | URL to zip of training images | Yes |
| `--trigger-word` | Word to activate the LoRA in prompts | Yes |
| `--model` / `-m` | Training model endpoint | No (default: fal-ai/flux-lora-fast-training) |
| `--steps` | Training steps | No (default: 1000) |
| `--status` | Check training job status | No |
| `--endpoint` | Endpoint for status check | With --status |
| `--request-id` | Request ID for status check | With --status |
| `--param` | Extra param as key=value (repeatable) | No |

## Finding Models

To discover the best and latest training/LoRA models, use the search API:

```bash
# Search for LoRA training models
bash /mnt/skills/user/fal-generate/scripts/search-models.sh --query "lora training"
bash /mnt/skills/user/fal-generate/scripts/search-models.sh --query "trainer"
bash /mnt/skills/user/fal-generate/scripts/search-models.sh --query "fine-tune"
```

Or use the `search_models` MCP tool with keywords like "lora", "training", "trainer", "fine-tune".

## Training Data Tips

- **People**: 10-20 photos, varied angles/lighting/expressions, consistent person
- **Styles**: 10-15 images exemplifying the style, diverse subjects
- **Objects**: 5-15 photos from different angles on various backgrounds
- Images should be high quality, at least 512x512
- Zip all images into a single .zip file and host at a URL

## Output Format
```json
{
  "diffusers_lora_file": {
    "url": "https://fal.media/files/.../lora.safetensors",
    "content_type": "application/octet-stream",
    "file_name": "lora.safetensors",
    "file_size": 12345678
  },
  "config_file": {
    "url": "https://fal.media/files/.../config.json"
  }
}
```

Use the `diffusers_lora_file.url` as the `lora_url` parameter when generating images with FLUX models.
```

## File: `skills/claude.ai/fal-train/scripts/train.sh`
```bash
#!/bin/bash
set -e

# train.sh — Submit a LoRA training job to fal.ai

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
MODEL="fal-ai/flux-lora-fast-training"
IMAGES_URL=""
TRIGGER_WORD=""
STEPS=1000
CHECK_STATUS=false
ENDPOINT=""
REQUEST_ID=""
EXTRA_PARAMS=""

show_help() {
  echo "Usage: $0 --images-url URL --trigger-word WORD [options]"
  echo "       $0 --status --endpoint MODEL --request-id ID"
  echo ""
  echo "Options:"
  echo "  --images-url URL      URL to zip of training images (required)"
  echo "  --trigger-word WORD   Trigger word for the LoRA (required)"
  echo "  --model, -m MODEL     Training model (default: $MODEL)"
  echo "  --steps N             Training steps (default: $STEPS)"
  echo "  --status              Check training job status"
  echo "  --endpoint MODEL      Endpoint for status check"
  echo "  --request-id ID       Request ID for status check"
  echo "  --param KEY=VALUE     Extra parameter (repeatable)"
  echo "  --add-fal-key KEY     Store FAL_KEY in .env"
  echo "  --help, -h            Show this help"
  exit 0
}

[ -f "$SCRIPT_DIR/../.env" ] && source "$SCRIPT_DIR/../.env"
[ -f ".env" ] && source ".env"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --images-url) IMAGES_URL="$2"; shift 2;;
    --trigger-word) TRIGGER_WORD="$2"; shift 2;;
    --model|-m) MODEL="$2"; shift 2;;
    --steps) STEPS="$2"; shift 2;;
    --status) CHECK_STATUS=true; shift;;
    --endpoint) ENDPOINT="$2"; shift 2;;
    --request-id) REQUEST_ID="$2"; shift 2;;
    --param) EXTRA_PARAMS="$EXTRA_PARAMS \"$(echo "$2" | cut -d= -f1)\": \"$(echo "$2" | cut -d= -f2)\","; shift 2;;
    --add-fal-key) echo "FAL_KEY=$2" > .env; echo "API key saved." >&2; exit 0;;
    --help|-h) show_help;;
    *) echo "Unknown: $1" >&2; exit 1;;
  esac
done

if [ -z "$FAL_KEY" ]; then echo "Error: FAL_KEY not set." >&2; exit 1; fi

# Status check mode
if [ "$CHECK_STATUS" = true ]; then
  if [ -z "$ENDPOINT" ] || [ -z "$REQUEST_ID" ]; then
    echo "Error: --endpoint and --request-id required for --status" >&2; exit 1
  fi
  curl -s "https://queue.fal.run/$ENDPOINT/requests/$REQUEST_ID/status?logs=1" \
    -H "Authorization: Key $FAL_KEY" | jq .
  exit 0
fi

# Training mode
if [ -z "$IMAGES_URL" ]; then echo "Error: --images-url required" >&2; exit 1; fi
if [ -z "$TRIGGER_WORD" ]; then echo "Error: --trigger-word required" >&2; exit 1; fi

PAYLOAD=$(cat <<EOF
{
  "images_data_url": "$IMAGES_URL",
  "trigger_word": "$TRIGGER_WORD",
  "steps": $STEPS,
  $EXTRA_PARAMS
  "is_style": false
}
EOF
)

echo "Submitting training to $MODEL..." >&2
echo "  Images: $IMAGES_URL" >&2
echo "  Trigger: $TRIGGER_WORD" >&2
echo "  Steps: $STEPS" >&2

SUBMIT=$(curl -s -X POST "https://queue.fal.run/$MODEL" \
  -H "Authorization: Key $FAL_KEY" \
  -H "Content-Type: application/json" \
  -d "$PAYLOAD")

REQ_ID=$(echo "$SUBMIT" | jq -r '.request_id // empty')
if [ -z "$REQ_ID" ]; then echo "Error: $SUBMIT" >&2; exit 1; fi

echo "" >&2
echo "Training submitted!" >&2
echo "Request ID: $REQ_ID" >&2
echo "" >&2
echo "Training takes 5-30 minutes. Check status with:" >&2
echo "  $0 --status --endpoint $MODEL --request-id $REQ_ID" >&2
echo "" >&2
echo "$REQ_ID"
```

## File: `skills/claude.ai/fal-tryon/SKILL.md`
```markdown
---
name: fal-tryon
description: Virtual try-on — see how clothes look on a person. Use when the user requests "Try on clothes", "Virtual try-on", "How does this look on me", "Fashion try-on", "Garment transfer".
metadata:
  author: fal-ai
  version: "1.0.0"
---

# fal-tryon

Virtual try-on — transfer garments onto person photos using fal.ai models.

## Scripts

| Script | Purpose |
|--------|---------|
| `tryon.sh` | Apply a garment onto a person photo |

## Usage

### Basic Try-On
```bash
./scripts/tryon.sh --person-url "https://example.com/person.jpg" --garment-url "https://example.com/dress.jpg"
```

### With Garment Type
```bash
./scripts/tryon.sh --person-url "https://example.com/person.jpg" --garment-url "https://example.com/jacket.jpg" --type top
```

## Arguments

| Argument | Description | Required |
|----------|-------------|----------|
| `--person-url` | URL of person/model photo | Yes |
| `--garment-url` | URL of garment/clothing image | Yes |
| `--type` | Garment type: top, bottom, full-body, dress | No (auto-detect) |
| `--model` / `-m` | Model endpoint | No (default: fal-ai/fashn/tryon/v1.5) |
| `--quality` | speed, balanced, quality | No (default: balanced) |

## Finding Models

To discover the best and latest virtual try-on models, use the search API:

```bash
# Search for try-on models
bash /mnt/skills/user/fal-generate/scripts/search-models.sh --query "try-on"
bash /mnt/skills/user/fal-generate/scripts/search-models.sh --query "virtual tryon"
bash /mnt/skills/user/fal-generate/scripts/search-models.sh --query "garment"
```

Or use the `search_models` MCP tool with keywords like "try-on", "tryon", "garment", "fashion".

## Tips

- Person photo should show clear full or upper body
- Garment image works best on plain/white background (flat-lay or mannequin)
- Remove garment background first for best results
- Specify garment type (top/bottom/dress) for more accurate placement
```

## File: `skills/claude.ai/fal-tryon/scripts/tryon.sh`
```bash
#!/bin/bash
set -e

# tryon.sh — Virtual try-on: apply garment onto person photo

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
MODEL="fal-ai/fashn/tryon/v1.5"
PERSON_URL=""
GARMENT_URL=""
TYPE=""
QUALITY="balanced"

show_help() {
  echo "Usage: $0 --person-url URL --garment-url URL [options]"
  echo ""
  echo "Options:"
  echo "  --person-url URL    Person/model photo URL (required)"
  echo "  --garment-url URL   Garment/clothing image URL (required)"
  echo "  --type TYPE         Garment type: top, bottom, full-body, dress"
  echo "  --quality Q         speed, balanced, quality (default: balanced)"
  echo "  --model, -m MODEL   Model (default: $MODEL)"
  echo "  --add-fal-key KEY   Store FAL_KEY in .env"
  echo "  --help, -h          Show this help"
  exit 0
}

[ -f "$SCRIPT_DIR/../.env" ] && source "$SCRIPT_DIR/../.env"
[ -f ".env" ] && source ".env"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --person-url) PERSON_URL="$2"; shift 2;;
    --garment-url) GARMENT_URL="$2"; shift 2;;
    --type) TYPE="$2"; shift 2;;
    --quality) QUALITY="$2"; shift 2;;
    --model|-m) MODEL="$2"; shift 2;;
    --add-fal-key) echo "FAL_KEY=$2" > .env; echo "API key saved." >&2; exit 0;;
    --help|-h) show_help;;
    *) echo "Unknown: $1" >&2; exit 1;;
  esac
done

if [ -z "$FAL_KEY" ]; then echo "Error: FAL_KEY not set." >&2; exit 1; fi
if [ -z "$PERSON_URL" ]; then echo "Error: --person-url required" >&2; exit 1; fi
if [ -z "$GARMENT_URL" ]; then echo "Error: --garment-url required" >&2; exit 1; fi

PAYLOAD="{\"model_image\": \"$PERSON_URL\", \"garment_image\": \"$GARMENT_URL\""
if [ -n "$TYPE" ]; then PAYLOAD="$PAYLOAD, \"category\": \"$TYPE\""; fi
PAYLOAD="$PAYLOAD}"

echo "Running virtual try-on with $MODEL..." >&2
RESULT=$(curl -s -X POST "https://fal.run/$MODEL" \
  -H "Authorization: Key $FAL_KEY" \
  -H "Content-Type: application/json" \
  -d "$PAYLOAD")

if echo "$RESULT" | jq -e '.error' > /dev/null 2>&1; then
  echo "Error: $RESULT" >&2; exit 1
fi

echo "$RESULT" | jq .
```

## File: `skills/claude.ai/fal-upscale/SKILL.md`
```markdown
---
name: fal-upscale
description: Upscale and enhance image resolution using AI. Use when the user requests "Upscale image", "Enhance resolution", "Make image bigger", "Increase quality", or similar upscaling tasks.
metadata:
  author: fal-ai
  version: "1.0.0"
---

# fal.ai Upscale

Upscale and enhance image resolution using state-of-the-art AI models.

## How It Works

1. User provides image URL and optional scale factor
2. Script selects appropriate upscaling model
3. Sends request to fal.ai API
4. Returns upscaled image URL

## Finding Models

To discover the best and latest upscaling models, use the search API:

```bash
# Search for image upscale models
bash /mnt/skills/user/fal-generate/scripts/search-models.sh --query "upscale image"

# Search for video upscale models
bash /mnt/skills/user/fal-generate/scripts/search-models.sh --query "upscale video"

# Search for super-resolution models
bash /mnt/skills/user/fal-generate/scripts/search-models.sh --query "super resolution"
```

Or use the `search_models` MCP tool with keywords like "upscale", "super resolution", "enhance".

## Usage

```bash
bash /mnt/skills/user/fal-upscale/scripts/upscale.sh [options]
```

**Arguments:**
- `--image-url` - URL of image to upscale (required)
- `--model` - Model ID (defaults to `fal-ai/aura-sr`)
- `--scale` - Upscale factor: 2 or 4 (default: 4)

**Examples:**

```bash
# Image upscale with AuraSR (4x, fast)
bash /mnt/skills/user/fal-upscale/scripts/upscale.sh \
  --image-url "https://example.com/image.jpg"

# Image upscale with Clarity (detail preservation)
bash /mnt/skills/user/fal-upscale/scripts/upscale.sh \
  --image-url "https://example.com/image.jpg" \
  --model "fal-ai/clarity-upscaler" \
  --scale 2

# Video upscale (general purpose)
bash /mnt/skills/user/fal-upscale/scripts/upscale.sh \
  --video-url "https://example.com/video.mp4" \
  --model "fal-ai/video-upscaler"

# Video upscale (premium quality)
bash /mnt/skills/user/fal-upscale/scripts/upscale.sh \
  --video-url "https://example.com/video.mp4" \
  --model "fal-ai/topaz/upscale/video"
```

## MCP Tool Alternative

Use `search_models` MCP tool or `search-models.sh` to find the best current upscaling model, then call `mcp__fal-ai__generate` with the discovered `modelId`.

## Output

```
Upscaling with fal-ai/aura-sr...
Upscale complete!

Image URL: https://v3.fal.media/files/abc123/upscaled.png
Original: 512x512
Upscaled: 2048x2048
```

JSON output:
```json
{
  "image": {
    "url": "https://v3.fal.media/files/abc123/upscaled.png",
    "width": 2048,
    "height": 2048
  }
}
```

## Present Results to User

```
Here's your upscaled image:

![Upscaled Image](https://v3.fal.media/files/...)

• 512×512 → 2048×2048 (4x)
```

## Model Selection Tips

- **Image upscaling**: Search for "upscale image" or "super resolution". Consider speed vs quality tradeoffs.
- **Video upscaling**: Search for "upscale video". Premium models offer better quality but cost more.
- Scale factors typically range from 2x to 4x depending on the model.

## Troubleshooting

### API Key Error
```
Error: FAL_KEY environment variable not set

To fix:
1. Get your API key from https://fal.ai/dashboard/keys
2. Set: export FAL_KEY=your_key_here
```

### Image URL Error
```
Error: Could not fetch image from URL

Make sure:
1. The image URL is publicly accessible
2. The URL points directly to an image file
3. The image format is supported (JPEG, PNG, WebP)
```

### Network Error
```
Network error. To fix on claude.ai:

1. Go to https://claude.ai/settings/capabilities
2. Add *.fal.ai to the allowed domains
3. Try again
```
```

## File: `skills/claude.ai/fal-upscale/scripts/upscale.sh`
```bash
#!/bin/bash

# fal.ai Upscale Script
# Usage: ./upscale.sh --image-url URL [--model MODEL] [--scale SCALE]
# Returns: JSON with upscaled image URL

set -e

FAL_API_ENDPOINT="https://fal.run"

# Default values
MODEL="fal-ai/aura-sr"
IMAGE_URL=""
SCALE=4

# Check for --add-fal-key first
for arg in "$@"; do
    if [ "$arg" = "--add-fal-key" ]; then
        shift
        KEY_VALUE=""
        if [[ -n "$1" && ! "$1" =~ ^-- ]]; then
            KEY_VALUE="$1"
        fi
        if [ -z "$KEY_VALUE" ]; then
            echo "Enter your fal.ai API key:" >&2
            read -r KEY_VALUE
        fi
        if [ -n "$KEY_VALUE" ]; then
            grep -v "^FAL_KEY=" .env > .env.tmp 2>/dev/null || true
            mv .env.tmp .env 2>/dev/null || true
            echo "FAL_KEY=$KEY_VALUE" >> .env
            echo "FAL_KEY saved to .env" >&2
        fi
        exit 0
    fi
done

# Load .env if exists
if [ -f ".env" ]; then
    source .env 2>/dev/null || true
fi

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --image-url)
            IMAGE_URL="$2"
            shift 2
            ;;
        --model)
            MODEL="$2"
            shift 2
            ;;
        --scale)
            SCALE="$2"
            shift 2
            ;;
        --help|-h)
            echo "fal.ai Upscale Script" >&2
            echo "" >&2
            echo "Usage:" >&2
            echo "  ./upscale.sh --image-url URL [options]" >&2
            echo "" >&2
            echo "Options:" >&2
            echo "  --image-url     Image URL to upscale (required)" >&2
            echo "  --model         Model ID (default: fal-ai/aura-sr)" >&2
            echo "  --scale         Scale factor (default: 4)" >&2
            echo "  --add-fal-key   Setup FAL_KEY in .env" >&2
            exit 0
            ;;
        *)
            shift
            ;;
    esac
done

# Validate required inputs
if [ -z "$FAL_KEY" ]; then
    echo "Error: FAL_KEY not set" >&2
    echo "" >&2
    echo "Run: ./upscale.sh --add-fal-key" >&2
    echo "Or:  export FAL_KEY=your_key_here" >&2
    exit 1
fi

if [ -z "$IMAGE_URL" ]; then
    echo "Error: --image-url is required" >&2
    exit 1
fi

# Create temp directory
TEMP_DIR=$(mktemp -d)
trap 'rm -rf "$TEMP_DIR"' EXIT

echo "Upscaling with $MODEL..." >&2

# Build payload based on model
if [[ "$MODEL" == *"aura-sr"* ]]; then
    # AuraSR has fixed 4x scale
    PAYLOAD=$(cat <<EOF
{
  "image_url": "$IMAGE_URL"
}
EOF
)
else
    # Other models support scale parameter
    PAYLOAD=$(cat <<EOF
{
  "image_url": "$IMAGE_URL",
  "scale": $SCALE
}
EOF
)
fi

# Make API request
RESPONSE=$(curl -s -X POST "$FAL_API_ENDPOINT/$MODEL" \
    -H "Authorization: Key $FAL_KEY" \
    -H "Content-Type: application/json" \
    -d "$PAYLOAD")

# Check for errors
if echo "$RESPONSE" | grep -q '"error"'; then
    ERROR_MSG=$(echo "$RESPONSE" | grep -o '"message":"[^"]*"' | head -1 | cut -d'"' -f4)
    if [ -z "$ERROR_MSG" ]; then
        ERROR_MSG=$(echo "$RESPONSE" | grep -o '"error":"[^"]*"' | cut -d'"' -f4)
    fi
    echo "Error: $ERROR_MSG" >&2
    exit 1
fi

echo "Upscale complete!" >&2
echo "" >&2

# Extract and display result
OUTPUT_URL=$(echo "$RESPONSE" | grep -o '"url":"[^"]*"' | head -1 | cut -d'"' -f4)
echo "Image URL: $OUTPUT_URL" >&2

# Output JSON for programmatic use
echo "$RESPONSE"
```

## File: `skills/claude.ai/fal-video-edit/SKILL.md`
```markdown
---
name: fal-video-edit
description: Edit existing videos using AI — remix style, edit content, upscale resolution, remove background, or add audio/sound effects. Use when the user requests "Edit video", "Remix video", "Upscale video", "Remove video background", "Add sound to video", "Video to audio".
metadata:
  author: fal-ai
  version: "1.0.0"
---

# fal-video-edit

Edit, remix, upscale, and enhance existing videos using fal.ai models.

## Scripts

| Script | Purpose |
|--------|---------|
| `edit-video.sh` | Edit or remix a video with AI |
| `video-audio.sh` | Add synchronized audio/sound effects to a video |

## Usage

### Remix / Restyle Video
```bash
./scripts/edit-video.sh --video-url "https://example.com/video.mp4" --prompt "Transform into anime style" --operation remix
```

### Edit Video Content
```bash
./scripts/edit-video.sh --video-url "https://example.com/video.mp4" --prompt "Remove the person in the background" --operation edit
```

### Upscale Video
```bash
./scripts/edit-video.sh --video-url "https://example.com/video.mp4" --operation upscale
```

### Remove Video Background
```bash
./scripts/edit-video.sh --video-url "https://example.com/video.mp4" --operation remove-bg
```

### Add Audio to Video
```bash
./scripts/video-audio.sh --video-url "https://example.com/silent-video.mp4" --prompt "City street ambiance with car horns and people talking"
```

## Arguments

### edit-video.sh
| Argument | Description | Required |
|----------|-------------|----------|
| `--video-url` | URL of video to edit | Yes |
| `--prompt` / `-p` | Edit instructions or style description | For remix/edit |
| `--operation` | remix, edit, upscale, remove-bg | Yes |
| `--model` / `-m` | Override model endpoint | No |

### video-audio.sh
| Argument | Description | Required |
|----------|-------------|----------|
| `--video-url` | URL of video to add audio to | Yes |
| `--prompt` / `-p` | Description of desired audio/sounds | No |
| `--model` / `-m` | Model endpoint | No (default: fal-ai/mmaudio-v2) |

## Finding Models

To discover the best and latest video editing models, use the search API:

```bash
# Search for video editing models
bash /mnt/skills/user/fal-generate/scripts/search-models.sh --query "video editing"
bash /mnt/skills/user/fal-generate/scripts/search-models.sh --query "video-to-video"

# Search for video upscaling
bash /mnt/skills/user/fal-generate/scripts/search-models.sh --query "upscale video"

# Search for video background removal
bash /mnt/skills/user/fal-generate/scripts/search-models.sh --query "video background removal"

# Search for video audio generation
bash /mnt/skills/user/fal-generate/scripts/search-models.sh --query "video to audio"
```

Or use the `search_models` MCP tool with keywords like "video edit", "video remix", "video upscale", "video audio".
```

## File: `skills/claude.ai/fal-video-edit/scripts/edit-video.sh`
```bash
#!/bin/bash
set -e

# edit-video.sh — Edit, remix, upscale, or remove background from a video

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
VIDEO_URL=""
PROMPT=""
OPERATION=""
MODEL=""
POLL_INTERVAL=3
TIMEOUT=600

show_help() {
  echo "Usage: $0 --video-url URL --operation OP [--prompt TEXT] [options]"
  echo ""
  echo "Operations: remix, edit, upscale, remove-bg"
  echo ""
  echo "Options:"
  echo "  --video-url URL       Video URL (required)"
  echo "  --operation OP        Operation to perform (required)"
  echo "  --prompt, -p TEXT     Instructions/style description (for remix/edit)"
  echo "  --model, -m MODEL     Override model endpoint"
  echo "  --add-fal-key KEY     Store FAL_KEY in .env"
  echo "  --help, -h            Show this help"
  exit 0
}

[ -f "$SCRIPT_DIR/../.env" ] && source "$SCRIPT_DIR/../.env"
[ -f ".env" ] && source ".env"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --video-url) VIDEO_URL="$2"; shift 2;;
    --prompt|-p) PROMPT="$2"; shift 2;;
    --operation) OPERATION="$2"; shift 2;;
    --model|-m) MODEL="$2"; shift 2;;
    --add-fal-key) echo "FAL_KEY=$2" > .env; echo "API key saved." >&2; exit 0;;
    --help|-h) show_help;;
    *) echo "Unknown: $1" >&2; exit 1;;
  esac
done

if [ -z "$FAL_KEY" ]; then echo "Error: FAL_KEY not set." >&2; exit 1; fi
if [ -z "$VIDEO_URL" ]; then echo "Error: --video-url required" >&2; exit 1; fi
if [ -z "$OPERATION" ]; then echo "Error: --operation required (remix/edit/upscale/remove-bg)" >&2; exit 1; fi

# Auto-select model based on operation
if [ -z "$MODEL" ]; then
  case "$OPERATION" in
    remix) MODEL="fal-ai/kling-video/o3/standard/video-to-video/reference";;
    edit) MODEL="fal-ai/kling-video/o3/standard/video-to-video/edit";;
    upscale) MODEL="fal-ai/topaz/upscale/video";;
    remove-bg) MODEL="bria/video/background-removal";;
    *) echo "Error: Unknown operation: $OPERATION" >&2; exit 1;;
  esac
fi

# Build payload based on operation
case "$OPERATION" in
  remix|edit)
    if [ -z "$PROMPT" ]; then echo "Error: --prompt required for $OPERATION" >&2; exit 1; fi
    PAYLOAD="{\"video_url\": \"$VIDEO_URL\", \"prompt\": \"$PROMPT\"}";;
  upscale|remove-bg)
    PAYLOAD="{\"video_url\": \"$VIDEO_URL\"}";;
esac

echo "Submitting $OPERATION to $MODEL..." >&2
SUBMIT=$(curl -s -X POST "https://queue.fal.run/$MODEL" \
  -H "Authorization: Key $FAL_KEY" \
  -H "Content-Type: application/json" \
  -d "$PAYLOAD")

REQUEST_ID=$(echo "$SUBMIT" | jq -r '.request_id // empty')
if [ -z "$REQUEST_ID" ]; then echo "Error: $SUBMIT" >&2; exit 1; fi

echo "Waiting (request: $REQUEST_ID)..." >&2
ELAPSED=0
while [ "$ELAPSED" -lt "$TIMEOUT" ]; do
  STATUS=$(curl -s "https://queue.fal.run/$MODEL/requests/$REQUEST_ID/status" \
    -H "Authorization: Key $FAL_KEY")
  STATE=$(echo "$STATUS" | jq -r '.status')
  case "$STATE" in
    COMPLETED)
      echo "Completed!" >&2
      curl -s "https://queue.fal.run/$MODEL/requests/$REQUEST_ID" \
        -H "Authorization: Key $FAL_KEY" | jq .
      exit 0;;
    FAILED) echo "Failed: $STATUS" >&2; exit 1;;
    *) echo "  $STATE (${ELAPSED}s)" >&2;;
  esac
  sleep "$POLL_INTERVAL"
  ELAPSED=$((ELAPSED + POLL_INTERVAL))
done
echo "Timed out. Request ID: $REQUEST_ID" >&2; exit 1
```

## File: `skills/claude.ai/fal-video-edit/scripts/video-audio.sh`
```bash
#!/bin/bash
set -e

# video-audio.sh — Add synchronized audio/sound effects to a video

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
MODEL="fal-ai/mmaudio-v2"
VIDEO_URL=""
PROMPT=""
POLL_INTERVAL=3
TIMEOUT=600

show_help() {
  echo "Usage: $0 --video-url URL [--prompt TEXT] [options]"
  echo ""
  echo "Options:"
  echo "  --video-url URL    Video URL (required)"
  echo "  --prompt, -p TEXT  Description of desired audio/sounds"
  echo "  --model, -m MODEL  Model (default: $MODEL)"
  echo "  --add-fal-key KEY  Store FAL_KEY in .env"
  echo "  --help, -h         Show this help"
  exit 0
}

[ -f "$SCRIPT_DIR/../.env" ] && source "$SCRIPT_DIR/../.env"
[ -f ".env" ] && source ".env"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --video-url) VIDEO_URL="$2"; shift 2;;
    --prompt|-p) PROMPT="$2"; shift 2;;
    --model|-m) MODEL="$2"; shift 2;;
    --add-fal-key) echo "FAL_KEY=$2" > .env; echo "API key saved." >&2; exit 0;;
    --help|-h) show_help;;
    *) echo "Unknown: $1" >&2; exit 1;;
  esac
done

if [ -z "$FAL_KEY" ]; then echo "Error: FAL_KEY not set." >&2; exit 1; fi
if [ -z "$VIDEO_URL" ]; then echo "Error: --video-url required" >&2; exit 1; fi

PAYLOAD="{\"video_url\": \"$VIDEO_URL\""
if [ -n "$PROMPT" ]; then PAYLOAD="$PAYLOAD, \"prompt\": \"$PROMPT\""; fi
PAYLOAD="$PAYLOAD}"

echo "Submitting to $MODEL..." >&2
SUBMIT=$(curl -s -X POST "https://queue.fal.run/$MODEL" \
  -H "Authorization: Key $FAL_KEY" \
  -H "Content-Type: application/json" \
  -d "$PAYLOAD")

REQUEST_ID=$(echo "$SUBMIT" | jq -r '.request_id // empty')
if [ -z "$REQUEST_ID" ]; then echo "Error: $SUBMIT" >&2; exit 1; fi

echo "Waiting (request: $REQUEST_ID)..." >&2
ELAPSED=0
while [ "$ELAPSED" -lt "$TIMEOUT" ]; do
  STATUS=$(curl -s "https://queue.fal.run/$MODEL/requests/$REQUEST_ID/status" \
    -H "Authorization: Key $FAL_KEY")
  STATE=$(echo "$STATUS" | jq -r '.status')
  case "$STATE" in
    COMPLETED)
      curl -s "https://queue.fal.run/$MODEL/requests/$REQUEST_ID" \
        -H "Authorization: Key $FAL_KEY" | jq .
      exit 0;;
    FAILED) echo "Failed: $STATUS" >&2; exit 1;;
    *) echo "  $STATE (${ELAPSED}s)" >&2;;
  esac
  sleep "$POLL_INTERVAL"
  ELAPSED=$((ELAPSED + POLL_INTERVAL))
done
echo "Timed out. Request ID: $REQUEST_ID" >&2; exit 1
```

## File: `skills/claude.ai/fal-vision/SKILL.md`
```markdown
---
name: fal-vision
description: Analyze images using AI — segment objects, detect objects, extract text (OCR), describe images, ask questions about images. Use when the user requests "Segment image", "Detect objects", "OCR", "Extract text from image", "Describe image", "What's in this image", "Image analysis".
metadata:
  author: fal-ai
  version: "1.0.0"
---

# fal-vision

Analyze and understand images using fal.ai vision models — segmentation, detection, OCR, captioning, and visual QA.

## Scripts

| Script | Purpose |
|--------|---------|
| `analyze.sh` | Analyze an image (segment, detect, OCR, describe, QA) |

## Usage

### Segment Objects
```bash
./scripts/analyze.sh --image-url "https://example.com/photo.jpg" --operation segment --query "the red car"
```

### Detect Objects
```bash
./scripts/analyze.sh --image-url "https://example.com/photo.jpg" --operation detect
```

### Extract Text (OCR)
```bash
./scripts/analyze.sh --image-url "https://example.com/document.jpg" --operation ocr
```

### Describe Image
```bash
./scripts/analyze.sh --image-url "https://example.com/photo.jpg" --operation describe
```

### Visual QA
```bash
./scripts/analyze.sh --image-url "https://example.com/photo.jpg" --operation qa --query "How many people are in this image?"
```

## Arguments

| Argument | Description | Required |
|----------|-------------|----------|
| `--image-url` | URL of image to analyze | Yes |
| `--operation` | segment, detect, ocr, describe, qa | Yes |
| `--query` / `-q` | Text prompt for segment/qa operations | For segment/qa |
| `--model` / `-m` | Override model endpoint | No |

## Finding Models

To discover the best and latest vision/analysis models, use the search API:

```bash
# Search for segmentation models
bash /mnt/skills/user/fal-generate/scripts/search-models.sh --query "segmentation"

# Search for object detection models
bash /mnt/skills/user/fal-generate/scripts/search-models.sh --query "object detection"

# Search for OCR models
bash /mnt/skills/user/fal-generate/scripts/search-models.sh --query "ocr"

# Search for image captioning / visual QA models
bash /mnt/skills/user/fal-generate/scripts/search-models.sh --query "caption"
bash /mnt/skills/user/fal-generate/scripts/search-models.sh --query "visual question"
```

Or use the `search_models` MCP tool with keywords like "segmentation", "detection", "ocr", "caption", "vision".
```

## File: `skills/claude.ai/fal-vision/scripts/analyze.sh`
```bash
#!/bin/bash
set -e

# analyze.sh — Analyze an image (segment, detect, OCR, describe, QA)

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
IMAGE_URL=""
OPERATION=""
QUERY=""
MODEL=""

show_help() {
  echo "Usage: $0 --image-url URL --operation OP [--query TEXT] [options]"
  echo ""
  echo "Operations: segment, detect, ocr, describe, qa"
  echo ""
  echo "Options:"
  echo "  --image-url URL     Image URL (required)"
  echo "  --operation OP      Operation to perform (required)"
  echo "  --query, -q TEXT    Query text (for segment/qa)"
  echo "  --model, -m MODEL   Override model endpoint"
  echo "  --add-fal-key KEY   Store FAL_KEY in .env"
  echo "  --help, -h          Show this help"
  exit 0
}

[ -f "$SCRIPT_DIR/../.env" ] && source "$SCRIPT_DIR/../.env"
[ -f ".env" ] && source ".env"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --image-url) IMAGE_URL="$2"; shift 2;;
    --operation) OPERATION="$2"; shift 2;;
    --query|-q) QUERY="$2"; shift 2;;
    --model|-m) MODEL="$2"; shift 2;;
    --add-fal-key) echo "FAL_KEY=$2" > .env; echo "API key saved." >&2; exit 0;;
    --help|-h) show_help;;
    *) echo "Unknown: $1" >&2; exit 1;;
  esac
done

if [ -z "$FAL_KEY" ]; then echo "Error: FAL_KEY not set." >&2; exit 1; fi
if [ -z "$IMAGE_URL" ]; then echo "Error: --image-url required" >&2; exit 1; fi
if [ -z "$OPERATION" ]; then echo "Error: --operation required" >&2; exit 1; fi

# Auto-select model
if [ -z "$MODEL" ]; then
  case "$OPERATION" in
    segment) MODEL="fal-ai/sam-3/image";;
    detect) MODEL="fal-ai/florence-2-large/object-detection";;
    ocr) MODEL="fal-ai/got-ocr/v2";;
    describe) MODEL="fal-ai/florence-2-large/detailed-caption";;
    qa) MODEL="fal-ai/llava-next";;
    *) echo "Error: Unknown operation: $OPERATION" >&2; exit 1;;
  esac
fi

# Build payload
case "$OPERATION" in
  segment)
    if [ -n "$QUERY" ]; then
      PAYLOAD="{\"image_url\": \"$IMAGE_URL\", \"text_prompt\": \"$QUERY\"}"
    else
      PAYLOAD="{\"image_url\": \"$IMAGE_URL\"}"
    fi;;
  qa)
    QUERY="${QUERY:-What is in this image?}"
    PAYLOAD="{\"image_url\": \"$IMAGE_URL\", \"prompt\": \"$QUERY\"}";;
  *)
    PAYLOAD="{\"image_url\": \"$IMAGE_URL\"}";;
esac

echo "Running $OPERATION with $MODEL..." >&2
RESULT=$(curl -s -X POST "https://fal.run/$MODEL" \
  -H "Authorization: Key $FAL_KEY" \
  -H "Content-Type: application/json" \
  -d "$PAYLOAD")

if echo "$RESULT" | jq -e '.error' > /dev/null 2>&1; then
  echo "Error: $RESULT" >&2; exit 1
fi

echo "$RESULT" | jq .
```

## File: `skills/claude.ai/fal-workflow/SKILL.md`
```markdown
---
name: fal-workflow
description: Generate production-ready fal.ai workflow JSON files. Use when user requests "create workflow", "chain models", "multi-step generation", "image to video pipeline", or complex AI generation pipelines.
metadata:
  author: fal-ai
  version: "3.0.0"
---

# fal.ai Workflow Generator

Generate **100% working, production-ready fal.ai workflow JSON files**. Workflows chain multiple AI models together for complex generation pipelines.

**References:**
- [Model Reference](models.md) - Detailed model configurations
- [Common Patterns](PATTERNS.md) - Reusable workflow patterns
- [Code Examples](../claude_bp_repo/examples.md) - Code snippets and partial examples

**Troubleshooting Reference:**
- [Complete Workflows](workflows.md) - Working JSON examples for debugging (use ONLY when user reports errors)

---

## Core Architecture

### Valid Node Types

⚠️ **ONLY TWO VALID NODE TYPES EXIST:**

| Type | Purpose |
|------|---------|
| `"run"` | Execute a model/app |
| `"display"` | Output results to user |

**❌ INVALID:** `type: "input"` - This does NOT exist! Input is defined ONLY in `schema.input`.

### Minimal Working Example

```json
{
  "name": "my-workflow",
  "title": "My Workflow",
  "contents": {
    "name": "workflow",
    "nodes": {
      "output": {
        "type": "display",
        "id": "output",
        "depends": ["node-image"],
        "input": {},
        "fields": { "image": "$node-image.images.0.url" }
      },
      "node-image": {
        "type": "run",
        "id": "node-image",
        "depends": ["input"],
        "app": "fal-ai/flux/dev",
        "input": { "prompt": "$input.prompt" }
      }
    },
    "output": { "image": "$node-image.images.0.url" },
    "schema": {
      "input": {
        "prompt": {
          "name": "prompt",
          "label": "Prompt",
          "type": "string",
          "required": true,
          "modelId": "node-image"
        }
      },
      "output": {
        "image": { "name": "image", "label": "Generated Image", "type": "string" }
      }
    },
    "version": "1",
    "metadata": {
      "input": { "position": { "x": 0, "y": 0 } },
      "description": "Simple text to image workflow"
    }
  },
  "is_public": true,
  "user_id": "",
  "user_nickname": "",
  "created_at": ""
}
```

### Reference Syntax

| Reference | Use Case | Example |
|-----------|----------|---------|
| `$input.field` | Input value | `$input.prompt` |
| `$node.output` | LLM text output | `$node-llm.output` |
| `$node.images.0.url` | First image URL | `$node-img.images.0.url` |
| `$node.image.url` | Single image URL | `$node-upscale.image.url` |
| `$node.video.url` | Video URL | `$node-vid.video.url` |
| `$node.audio_file.url` | Audio URL | `$node-music.audio_file.url` |
| `$node.frame.url` | Extracted frame | `$node-extract.frame.url` |

### CRITICAL: No String Interpolation

**⚠️ NEVER mix text with variables! Variable MUST be the ENTIRE value.**

```json
// ❌ WRONG - WILL BREAK
"prompt": "Create image of $input.subject in $input.style"

// ✅ CORRECT - Variable is the ENTIRE value
"prompt": "$input.prompt"
"prompt": "$node-llm.output"
```

**To combine values:** Use `fal-ai/text-concat` or `fal-ai/workflow-utilities/merge-text`. See [Model Reference](models.md#text-utilities-critical-for-combining-values).

---

## Critical Rules

### C1: Dependencies Must Match References

```json
// ❌ WRONG
"node-b": {
  "depends": [],
  "input": { "data": "$node-a.output" }
}

// ✅ CORRECT
"node-b": {
  "depends": ["node-a"],
  "input": { "data": "$node-a.output" }
}
```

### C2: ID Must Match Object Key

```json
// ❌ WRONG
"my-node": { "id": "different-id" }

// ✅ CORRECT
"my-node": { "id": "my-node" }
```

### C3: Use Correct LLM Type

- `openrouter/router` → Text only, no image_urls
- `openrouter/router/vision` → ONLY when analyzing images

### C4: Schema modelId Required

```json
"schema": {
  "input": {
    "field": { "modelId": "first-consuming-node" }
  }
}
```

### C5: Output Depends on All Referenced Nodes

```json
"output": {
  "depends": ["node-a", "node-b", "node-c"],
  "fields": {
    "a": "$node-a.video",
    "b": "$node-b.images.0.url"
  }
}
```

---

---

## Quick Reference Card

### Output References

| Model Type | Output Reference |
|------------|------------------|
| LLM | `$node.output` |
| Text Concat | `$node.results` |
| Merge Text | `$node.text` |
| Image Gen (array) | `$node.images.0.url` |
| Image Process (single) | `$node.image.url` |
| Video | `$node.video.url` |
| Music | `$node.audio_file.url` |
| Frame Extract | `$node.frame.url` |

Use `search-models.sh` or `search_models` MCP tool to discover current models. See `references/MODELS.md` for workflow code templates.

---

## Input Schema

```json
"schema": {
  "input": {
    "text_field": {
      "name": "text_field",
      "label": "Display Label",
      "type": "string",
      "description": "Help text",
      "required": true,
      "modelId": "consuming-node"
    },
    "image_urls": {
      "name": "image_urls",
      "type": { "kind": "list", "elementType": "string" },
      "required": true,
      "modelId": "node-id"
    }
  }
}
```

---

## Pre-Output Checklist

Before outputting any workflow, verify:

- [ ] **⚠️ All nodes have `type: "run"` or `type: "display"` ONLY (NO `type: "input"`!)**
- [ ] **⚠️ No string interpolation - variable MUST be ENTIRE value**
- [ ] Every `$node.xxx` has matching `depends` entry
- [ ] Every node `id` matches object key
- [ ] Input schema has `modelId` for each field
- [ ] Output depends on ALL referenced nodes
- [ ] Correct LLM type (router vs router/vision)

---

## Usage

### Using Script

```bash
bash /mnt/skills/user/fal-workflow/scripts/create-workflow.sh \
  --name "my-workflow" \
  --title "My Workflow Title" \
  --nodes '[...]' \
  --outputs '{...}'
```

### Using MCP Tool

```javascript
mcp__fal-ai__create-workflow({
  smartMode: true,
  intent: "Generate a story with LLM, create an illustration, then animate it"
})
```

---

## Troubleshooting

### Invalid Node Type Error (MOST COMMON)
```
Error: unexpected value; permitted: 'run', 'display', field required
```
**Cause:** You created a node with `type: "input"` which does NOT exist.
**Solution:** Remove ANY node with `type: "input"`. Define input fields ONLY in `schema.input`.

### Dependency Error
```
Error: Node references $node-x but doesn't depend on it
```
**Solution:** Add the referenced node to the `depends` array.

### ID Mismatch Error
```
Error: Node key "my-node" doesn't match id "different-id"
```
**Solution:** Ensure the object key matches the `id` field exactly.

### LLM Vision Error
```
Error: image_urls provided but using text-only router
```
**Solution:** Switch to `openrouter/router/vision` when analyzing images.

---

## Finding Model Schemas

Every model's input/output schema:
```
https://fal.ai/api/openapi/queue/openapi.json?endpoint_id=[endpoint_id]
```

Example:
```
https://fal.ai/api/openapi/queue/openapi.json?endpoint_id=fal-ai/nano-banana-pro
```
```

## File: `skills/claude.ai/fal-workflow/references/EXAMPLES.md`
```markdown
# Real-World Workflow Examples

Complete workflow examples for reference.

## Multi-Destination Marketing Campaign Workflow

This workflow creates personalized video content for multiple locations:

1. Takes multiple destinations as input
2. Uses Vision LLM to analyze template and generate edit prompts
3. Creates destination-specific images
4. Removes backgrounds
5. Upscales all images
6. Generates videos with 360° camera tours
7. Merges all videos into final output

### Key Pattern: Edit → Remove Text → Upscale → Video

```json
// Step 1: Vision LLM analyzes template, generates edit prompt
"vision-prompt-dest2": {
  "id": "vision-prompt-dest2",
  "type": "run",
  "depends": ["input"],
  "app": "openrouter/router/vision",
  "input": {
    "image_urls": ["https://example.com/template.jpg"],
    "prompt": "$input.destination_2",
    "system_prompt": "Generate prompt to change background to destination, keep layout...",
    "model": "google/gemini-3-pro-preview",
    "reasoning": true
  }
},

// Step 2: Edit image with new destination
"edit-dest2": {
  "id": "edit-dest2",
  "type": "run",
  "depends": ["vision-prompt-dest2"],
  "app": "fal-ai/nano-banana-pro/edit",
  "input": {
    "image_urls": ["https://example.com/template.jpg"],
    "prompt": "$vision-prompt-dest2.output",
    "aspect_ratio": "16:9"
  }
},

// Step 3: Create text-free version for video background
"edit-notext-dest2": {
  "id": "edit-notext-dest2",
  "type": "run",
  "depends": ["edit-dest2"],
  "app": "fal-ai/nano-banana-pro/edit",
  "input": {
    "image_urls": ["$edit-dest2.images.0.url"],
    "prompt": "Remove all text and logo, leave only background scene"
  }
},

// Step 4: Upscale both versions
"upscale-dest2": {
  "id": "upscale-dest2",
  "type": "run",
  "depends": ["edit-dest2"],
  "app": "fal-ai/seedvr/upscale/image",
  "input": {
    "image_url": "$edit-dest2.images.0.url"
  }
},

// Step 5: Vision LLM creates video prompt from both images
"video-prompt-dest2": {
  "id": "video-prompt-dest2",
  "type": "run",
  "depends": ["upscale-notext-dest2", "upscale-dest2", "input"],
  "app": "openrouter/router/vision",
  "input": {
    "image_urls": [
      "$upscale-notext-dest2.image.url",
      "$upscale-dest2.image.url"
    ],
    "prompt": "$input.destination_2",
    "system_prompt": "Create video prompt: camera tours 360° then transitions to tail image..."
  }
},

// Step 6: Generate video with first/last frame
"video-dest2": {
  "id": "video-dest2",
  "type": "run",
  "depends": ["video-prompt-dest2", "upscale-notext-dest2", "upscale-dest2"],
  "app": "fal-ai/kling-video/o1/image-to-video",
  "input": {
    "prompt": "$video-prompt-dest2.output",
    "image_url": "$upscale-notext-dest2.image.url",
    "tail_image_url": "$upscale-dest2.image.url"
  }
},

// Step 7: Merge all destination videos
"merge-all-videos": {
  "id": "merge-all-videos",
  "type": "run",
  "depends": ["video-dest1", "video-dest2", "video-dest3"],
  "app": "fal-ai/ffmpeg-api/merge-videos",
  "input": {
    "video_urls": [
      "$video-dest1.video.url",
      "$video-dest2.video.url",
      "$video-dest3.video.url"
    ]
  }
}
```

### Input Schema for This Workflow

```json
"schema": {
  "input": {
    "destination_1": {
      "name": "destination_1",
      "label": "Destination 1",
      "type": "string",
      "description": "First destination name (e.g., Paris, Tokyo)",
      "required": true,
      "modelId": "vision-prompt-dest1"
    },
    "destination_2": {
      "name": "destination_2",
      "label": "Destination 2",
      "type": "string",
      "required": true,
      "modelId": "vision-prompt-dest2"
    },
    "destination_3": {
      "name": "destination_3",
      "label": "Destination 3",
      "type": "string",
      "required": true,
      "modelId": "vision-prompt-dest3"
    }
  }
}
```
```

## File: `skills/claude.ai/fal-workflow/references/MODELS.md`
```markdown
# Model Reference

Detailed configuration and usage for all supported models in fal.ai workflows.

## Image Generation

### Nano Banana Pro (DEFAULT)
```json
{
  "app": "fal-ai/nano-banana-pro",
  "input": {
    "prompt": "$node-prompt.output",
    "aspect_ratio": "16:9",
    "num_images": 1
  }
}
```
**Output:** `$node.images.0.url`

### Nano Banana Pro Edit (DEFAULT for editing)
```json
{
  "app": "fal-ai/nano-banana-pro/edit",
  "input": {
    "prompt": "$node-prompt.output",
    "image_urls": ["$input.source_image"],
    "aspect_ratio": "16:9",
    "resolution": "4K"
  }
}
```
**Output:** `$node.images.0.url`

### Other Image Models

| Model | App ID |
|-------|--------|
| FLUX.1 Dev | `fal-ai/flux/dev` |
| FLUX.1 Schnell | `fal-ai/flux/schnell` |
| FLUX.1 Pro | `fal-ai/flux-pro` |
| Ideogram v3 | `fal-ai/ideogram/v3` |
| Recraft v3 | `fal-ai/recraft-v3` |

---

## Video Generation

### Seedance 1.5 Pro (DEFAULT)
```json
{
  "app": "fal-ai/bytedance/seedance/v1.5/pro/image-to-video",
  "input": {
    "prompt": "$node-video-prompt.output",
    "image_url": "$node-image.images.0.url",
    "aspect_ratio": "16:9",
    "resolution": "720p",
    "duration": "5",
    "generate_audio": true
  }
}
```
**Output:** `$node.video.url`

### Kling Video O1 (Image-to-Video with First/Last Frame)
```json
{
  "app": "fal-ai/kling-video/o1/image-to-video",
  "input": {
    "prompt": "$node-prompt.output",
    "image_url": "$node-start-frame.images.0.url",
    "tail_image_url": "$node-end-frame.images.0.url",
    "duration": "5",
    "aspect_ratio": "16:9"
  }
}
```
**Output:** `$node.video.url`

### Kling Video 2.6 Pro (Best I2V)
```json
{
  "app": "fal-ai/kling-video/v2.6/pro/image-to-video",
  "input": {
    "prompt": "$node-prompt.output",
    "start_image_url": "$node-image.images.0.url",
    "duration": "5",
    "negative_prompt": "blur, distort, and low quality",
    "generate_audio": true
  }
}
```
**Output:** `$node.video.url`

**Parameters:**
- `prompt` - Video description (can include speech for lip-sync)
- `start_image_url` - Starting frame image URL
- `duration` - Video length: `"5"` or `"10"` seconds
- `negative_prompt` - What to avoid in generation
- `generate_audio` - Enable audio generation from prompt

**Best for:** High quality image-to-video with optional audio generation and lip-sync support.

### Other Video Models

| Model | App ID | Notes |
|-------|--------|-------|
| Veo 3.1 Fast | `fal-ai/veo3.1/fast/image-to-video` | High quality |
| Kling 2.6 Pro | `fal-ai/kling-video/v2.6/pro/image-to-video` | **Best I2V** |


---

## LLM Models

### Text LLM (DEFAULT - No images)
```json
{
  "app": "openrouter/router",
  "input": {
    "prompt": "$input.user_input",
    "system_prompt": "Your instructions here...",
    "model": "google/gemini-2.5-flash",
    "temperature": 0.7
  }
}
```
**Output:** `$node.output`

### Vision LLM (When image analysis needed)
```json
{
  "app": "openrouter/router/vision",
  "input": {
    "prompt": "$input.user_request",
    "system_prompt": "Analyze the image and...",
    "image_urls": ["$node-image.images.0.url"],
    "model": "google/gemini-3-pro-preview",
    "reasoning": true
  }
}
```
**Output:** `$node.output`

**Available LLM Models:**
- `google/gemini-2.5-flash` - Fast, good quality
- `google/gemini-3-pro-preview` - Best reasoning
- `anthropic/claude-sonnet-4.5` - Best for complex tasks

---

## Audio/Music Generation

### ElevenLabs Music
```json
{
  "app": "fal-ai/elevenlabs/music",
  "input": {
    "prompt": "Mysterious soundtrack, jungle themes, tribal percussion",
    "respect_sections_durations": true,
    "output_format": "mp3_44100_128"
  }
}
```
**Output:** `$node.audio_file.url`

### MMAudio (Video to Audio)
```json
{
  "app": "fal-ai/mmaudio-v2",
  "input": {
    "video_url": "$node-video.video.url",
    "prompt": "Ambient nature sounds"
  }
}
```

### Stable Audio
```json
{
  "app": "fal-ai/stable-audio",
  "input": {
    "prompt": "Cinematic orchestral music"
  }
}
```

### Other Music Models

| Model | App ID |
|-------|--------|
| MiniMax Music v2 | `fal-ai/minimax-music/v2` |

---

## Text-to-Speech

### ElevenLabs TTS v3
```json
{
  "app": "fal-ai/elevenlabs/tts/eleven-v3",
  "input": {
    "text": "$node-llm.output",
    "voice": "Aria",
    "stability": 0.5,
    "similarity_boost": 0.75,
    "speed": 1
  }
}
```
**Output:** `$node.audio.url`

**Parameters:**
- `text` - Text to convert to speech
- `voice` - Voice name (e.g., "Aria", "Roger", "Sarah")
- `stability` - Voice stability (0-1)
- `similarity_boost` - Voice clarity (0-1)
- `speed` - Speech speed multiplier

### MiniMax Speech 2.6 HD (Best Quality)
```json
{
  "app": "fal-ai/minimax/speech-2.6-hd",
  "input": {
    "prompt": "$node-llm.output",
    "voice_setting": {
      "voice_id": "Wise_Woman",
      "speed": 1,
      "vol": 1,
      "pitch": 0
    },
    "output_format": "mp3"
  }
}
```
**Output:** `$node.audio.url`

**Parameters:**
- `prompt` - Text to convert to speech
- `voice_setting.voice_id` - Voice ID (e.g., "Wise_Woman", "Young_Man")
- `voice_setting.speed` - Speech speed (0.5-2)
- `voice_setting.vol` - Volume (0-1)
- `voice_setting.pitch` - Pitch adjustment (-12 to 12)
- `output_format` - Output format: `"mp3"`, `"wav"`, `"hex"`

### MiniMax Voice Clone
Clone a voice from audio sample, then use the cloned voice ID in MiniMax Speech.

```json
{
  "app": "fal-ai/minimax/voice-clone",
  "input": {
    "audio_url": "$input.voice_sample",
    "text": "Preview text for the cloned voice",
    "model": "speech-02-hd"
  }
}
```
**Output:** `$node.audio.url`, `$node.voice_id`

**Use cloned voice in Speech 2.6 HD:**
```json
{
  "app": "fal-ai/minimax/speech-2.6-hd",
  "input": {
    "prompt": "$node-llm.output",
    "voice_setting": {
      "voice_id": "$node-voice-clone.voice_id"
    }
  }
}
```

### Other TTS Models

| Model | App ID | Notes |
|-------|--------|-------|
| MiniMax Speech 2.6 Turbo | `fal-ai/minimax/speech-2.6-turbo` | Fast |
| Chatterbox | `fal-ai/chatterbox/text-to-speech/multilingual` | Multi-language |

---

## Text Utilities (CRITICAL for combining values)

**⚠️ These are the ONLY ways to combine text values - string interpolation is NOT supported!**

### Text Concat (2 texts)
Concatenates exactly TWO text values. `text1` can be static text!

```json
{
  "app": "fal-ai/text-concat",
  "input": {
    "text1": "Brand expert response:",
    "text2": "$node-llm.output"
  }
}
```
**Output:** `$node.results`

**Use Cases:**
- Add a label/prefix to a variable: `"text1": "Scene 1:", "text2": "$node.output"`
- Combine static instruction with dynamic content

### Merge Text (Multiple texts)
Merges an ARRAY of text values with a separator.

```json
{
  "app": "fal-ai/workflow-utilities/merge-text",
  "input": {
    "texts": [
      "$node-a.results",
      "$node-b.results",
      "$node-c.results"
    ],
    "separator": "------"
  }
}
```
**Output:** `$node.text`

**Use Cases:**
- Combine 3+ LLM outputs before passing to next node
- Merge multiple expert responses into single context

### Pattern: Label + Merge
Common pattern for combining multiple labeled outputs:

```json
// Step 1: Add labels with text-concat
"label-brand": {
  "app": "fal-ai/text-concat",
  "input": {
    "text1": "Brand expert:",
    "text2": "$brand-llm.output"
  }
},
"label-visual": {
  "app": "fal-ai/text-concat",
  "input": {
    "text1": "Visual director:",
    "text2": "$visual-llm.output"
  }
},

// Step 2: Merge labeled outputs
"merged-context": {
  "depends": ["label-brand", "label-visual"],
  "app": "fal-ai/workflow-utilities/merge-text",
  "input": {
    "texts": ["$label-brand.results", "$label-visual.results"],
    "separator": "\n\n---\n\n"
  }
},

// Step 3: Use merged context
"final-llm": {
  "depends": ["merged-context"],
  "input": {
    "prompt": "$merged-context.text"
  }
}
```

---

## FFmpeg Utilities (CRITICAL)

### Extract Frame from Video
```json
{
  "app": "fal-ai/ffmpeg-api/extract-frame",
  "input": {
    "video_url": "$node-video.video.url",
    "frame_type": "first"
  }
}
```
**Output:** `$node.frame.url`

**frame_type options:** `"first"` or `"last"`

**Use Cases:**
- Get last frame for video extension
- Get first frame for transitions
- Extract frame for first/last frame video generation

### Merge Multiple Videos
```json
{
  "app": "fal-ai/ffmpeg-api/merge-videos",
  "input": {
    "video_urls": [
      "$node-video-1.video.url",
      "$node-video-2.video.url",
      "$node-video-3.video.url"
    ]
  }
}
```
**Output:** `$node.video.url`

### Merge Audio and Video
```json
{
  "app": "fal-ai/ffmpeg-api/merge-audio-video",
  "input": {
    "video_url": "$node-video.video.url",
    "audio_url": "$node-music.audio_file.url"
  }
}
```
**Output:** `$node.video.url`

---

## Image Utilities

### Crop Image
Crops a portion of an image using percentage-based coordinates.

```json
{
  "app": "fal-ai/workflow-utilities/crop-image",
  "input": {
    "image_url": "$node-image.images.0.url",
    "x_percent": 0,
    "y_percent": 0,
    "width_percent": 33.333333,
    "height_percent": 33.333333
  }
}
```
**Output:** `$node.image.url`

**Parameters:**
- `x_percent`: Starting X position (0-100)
- `y_percent`: Starting Y position (0-100)
- `width_percent`: Width of crop area (0-100)
- `height_percent`: Height of crop area (0-100)

**Use Cases:**
- Split image into grid tiles (3x3, 2x2, etc.)
- Extract specific region from generated image
- Create multiple crops for parallel processing

**Example: 3x3 Grid Split**
```json
// Top-left tile
"crop-1": { "input": { "x_percent": 0, "y_percent": 0, "width_percent": 33.33, "height_percent": 33.33 } }
// Top-center tile
"crop-2": { "input": { "x_percent": 33.33, "y_percent": 0, "width_percent": 33.33, "height_percent": 33.33 } }
// Top-right tile
"crop-3": { "input": { "x_percent": 66.67, "y_percent": 0, "width_percent": 33.33, "height_percent": 33.33 } }
// ... and so on for all 9 tiles
```

---

## Image Processing

### Upscale Image
```json
{
  "app": "fal-ai/seedvr/upscale/image",
  "input": {
    "image_url": "$node-image.images.0.url"
  }
}
```
**Output:** `$node.image.url`

### Remove Background
```json
{
  "app": "fal-ai/bria/background/remove",
  "input": {
    "image_url": "$node-image.images.0.url"
  }
}
```
**Output:** `$node.image.url`

---

## 3D Generation (Image to 3D)

### Hunyuan3D v3 (Recommended)
```json
{
  "app": "fal-ai/hunyuan3d-v3/image-to-3d",
  "input": {
    "input_image_url": "$node-image.images.0.url",
    "face_count": 500000,
    "generate_type": "Normal",
    "polygon_type": "triangle"
  }
}
```
**Output:** `$node.model_mesh.url`

**Parameters:**
- `input_image_url` - Source image URL
- `face_count` - Mesh detail level (default: 500000)
- `generate_type` - Generation mode: `"Normal"`, `"Fast"`
- `polygon_type` - Mesh type: `"triangle"`, `"quad"`

### Rodin v2 (Multi-view)
```json
{
  "app": "fal-ai/hyper3d/rodin/v2",
  "input": {
    "input_image_urls": [
      "$node-front.images.0.url",
      "$node-left.images.0.url",
      "$node-right.images.0.url",
      "$node-back.images.0.url"
    ],
    "quality_mesh_option": "500K Triangle",
    "material": "All"
  }
}
```
**Output:** `$node.model_mesh.url`

**Best for:** Multi-view 3D generation (provide multiple angles for better results)

```

## File: `skills/claude.ai/fal-workflow/references/PATTERNS.md`
```markdown
# Common Workflow Patterns

Reusable patterns for building fal.ai workflows.

## Pattern 1: LLM Prompt → Image → Video

```
[Input] → [LLM: Image Prompt] → [Image Gen]
                ↓
          [LLM: Video Prompt] → [Video Gen] → [Output]
```

---

## Pattern 2: Parallel Processing (Fan-Out)

```
                → [Process A] →
[Hub Node] → [Process B] → [Merge] → [Output]
                → [Process C] →
```

All parallel nodes depend on hub, NOT on each other.

---

## Pattern 3: Video Extension with Extract Frame

```
[Video 1] → [Extract Last Frame] → [Video 2 with Start Frame] → [Merge] → [Output]
```

```json
"node-extract": {
  "depends": ["node-video-1"],
  "app": "fal-ai/ffmpeg-api/extract-frame",
  "input": {
    "video_url": "$node-video-1.video.url",
    "frame_type": "last"
  }
},
"node-video-2": {
  "depends": ["node-extract", "node-prompt-2"],
  "app": "fal-ai/kling-video/o1/image-to-video",
  "input": {
    "prompt": "$node-prompt-2.output",
    "image_url": "$node-extract.frame.url"
  }
}
```

---

## Pattern 4: First/Last Frame Video (Kling O1)

```
[Start Image] →
                → [Kling O1 Video] → [Output]
[End Image]   →
```

```json
"node-video": {
  "depends": ["node-start-frame", "node-end-frame", "node-prompt"],
  "app": "fal-ai/kling-video/o1/image-to-video",
  "input": {
    "prompt": "$node-prompt.output",
    "image_url": "$node-start-frame.images.0.url",
    "tail_image_url": "$node-end-frame.images.0.url"
  }
}
```

---

## Pattern 5: Video with Custom Music

```
[Video Gen] →                    → [Merge Audio/Video] → [Output]
[Music Gen] → [audio_file.url] →
```

```json
"node-music": {
  "depends": ["input"],
  "app": "fal-ai/elevenlabs/music",
  "input": {
    "prompt": "$input.music_style"
  }
},
"node-merge": {
  "depends": ["node-video", "node-music"],
  "app": "fal-ai/ffmpeg-api/merge-audio-video",
  "input": {
    "video_url": "$node-video.video.url",
    "audio_url": "$node-music.audio_file.url"
  }
}
```

---

## Pattern 6: Multi-Destination Campaign (Complex)

Pattern for multi-destination marketing videos:

```
[Input: dest_1] → [Vision LLM: Prompt] → [Edit Image] → [Upscale] →
                                                                    → [Vision LLM: Video Prompt] → [Video Gen]
                  [Edit: Remove Text] → [Upscale] →

[Input: dest_2] → [Same pattern...]
[Input: dest_3] → [Same pattern...]

All Videos → [Merge Videos] → [Output]
```
```

## File: `skills/claude.ai/fal-workflow/references/WORKFLOWS.md`
```markdown
# Complete Working Workflows

Production-ready workflow JSON files that can be directly imported into fal.ai.

## Live-in-Scene (Film POV Experience)

Creates 6 immersive POV video scenes from any film name, with ambient audio, then merges into final video.

**Input:** Film name (e.g., "Titanic", "Blade Runner")
**Output:** 6 scene videos + merged final video (~24 sec)

**Flow:**
```
[Film Name] → [Scene Planner LLM] → [6x Image Prompts] → [6x Images]
                                  → [6x Video Prompts] → [6x Videos] → [Merge] → [Final]
```

```json
{"name":"live-in-scene","title":"live-in-scene","contents":{"name":"workflow","nodes":{"output":{"type":"display","id":"output","depends":["node-merge-videos"],"fields":{"final_video":"$node-merge-videos.video","scene_1":"$node-video-1.video","scene_2":"$node-video-2.video","scene_3":"$node-video-3.video","scene_4":"$node-video-4.video","scene_5":"$node-video-5.video","scene_6":"$node-video-6.video"},"input":{},"metadata":{"position":{"x":5200,"y":0}}},"node-merge-videos":{"type":"run","id":"node-merge-videos","depends":["node-video-1","node-video-2","node-video-3","node-video-4","node-video-5","node-video-6"],"input":{"video_urls":["$node-video-1.video.url","$node-video-2.video.url","$node-video-3.video.url","$node-video-4.video.url","$node-video-5.video.url","$node-video-6.video.url"]},"app":"fal-ai/ffmpeg-api/merge-videos","metadata":{"position":{"x":4600,"y":1500}}},"node-scene-planner":{"type":"run","id":"node-scene-planner","depends":["input"],"input":{"prompt":"$input.film_name","system_prompt":"You are a cinematic experience designer. The user gives you a FILM NAME. Design 6 immersive FIRST-PERSON POV scenes from inside that film.\n\nOutput this exact structure:\n\n**FILM STYLE:** [time period, color palette, visual tone - 1 sentence]\n\n**SCENE 1 - [NAME]:**\nLocation: [where]\nWe are: [POV role]\nWe see: [key visual elements]\nAction: [ONE clear action - keep it simple, 4 seconds only]\nAmbient Sound: [environmental sounds - NO speech]\n\n**SCENE 2-6:** [same format]\n\nIMPORTANT:\n- Each scene has ONE simple, realistic action\n- NO dialogue or speech - only ambient/environmental sounds\n- Sounds: wind, rain, fire, crowd murmur, footsteps, machinery, water, thunder\n\nMake scenes progress: establish world → tension builds → climax.","model":"google/gemini-2.5-flash","temperature":0.8},"app":"openrouter/router","metadata":{"position":{"x":1000,"y":0}}},"node-image-prompt-1":{"type":"run","id":"node-image-prompt-1","depends":["node-scene-planner"],"input":{"prompt":"$node-scene-planner.output","system_prompt":"From the scene plan, create an image prompt for SCENE 1.\n\nFormat: POV first-person perspective, [what we see], [people/objects], [lighting], [atmosphere]. Shot on 35mm film, photorealistic, cinematic, 8K, no text.\n\nOutput ONLY the prompt, max 80 words.","model":"google/gemini-2.5-flash","temperature":0.7},"app":"openrouter/router","metadata":{"position":{"x":1900,"y":0}}},"node-image-1":{"type":"run","id":"node-image-1","depends":["node-image-prompt-1"],"input":{"prompt":"$node-image-prompt-1.output","aspect_ratio":"16:9","num_images":1},"app":"fal-ai/nano-banana-pro","metadata":{"position":{"x":2800,"y":0}}},"node-video-prompt-1":{"type":"run","id":"node-video-prompt-1","depends":["node-scene-planner"],"input":{"prompt":"$node-scene-planner.output","system_prompt":"From the scene plan, create a Seedance video prompt for SCENE 1.\n\nCRITICAL RULES:\n- ONE clear action only (4 seconds is short)\n- NO human speech/dialogue - ambient sounds only\n- Realistic, achievable movement\n- Structure: [Subject + single motion], [camera], [ambient sound]\n\nGOOD: \"Woman slowly turns head, wind blows hair. Camera steady. Wind howling, distant thunder.\"\nBAD: \"Woman turns, walks, picks up item, looks around, speaks...\" (too many actions)\nBAD: \"Man shouts 'Run!'\" (no dialogue allowed)\n\nAmbient sounds: wind, rain, fire crackling, crowd murmur, footsteps, machinery, nature\n\nOutput ONLY the prompt, max 25 words.","model":"google/gemini-2.5-flash","temperature":0.7},"app":"openrouter/router","metadata":{"position":{"x":1900,"y":400}}},"node-video-1":{"type":"run","id":"node-video-1","depends":["node-image-1","node-video-prompt-1"],"input":{"prompt":"$node-video-prompt-1.output","image_url":"$node-image-1.images.0.url","aspect_ratio":"16:9","resolution":"720p","duration":"4","generate_audio":true},"app":"fal-ai/bytedance/seedance/v1.5/pro/image-to-video","metadata":{"position":{"x":3700,"y":0}}},"node-image-prompt-2":{"type":"run","id":"node-image-prompt-2","depends":["node-scene-planner"],"input":{"prompt":"$node-scene-planner.output","system_prompt":"From the scene plan, create an image prompt for SCENE 2.\n\nFormat: POV first-person perspective, [what we see], [people/objects], [lighting], [atmosphere]. Shot on 35mm film, photorealistic, cinematic, 8K, no text.\n\nOutput ONLY the prompt, max 80 words.","model":"google/gemini-2.5-flash","temperature":0.7},"app":"openrouter/router","metadata":{"position":{"x":1900,"y":600}}},"node-image-2":{"type":"run","id":"node-image-2","depends":["node-image-prompt-2"],"input":{"prompt":"$node-image-prompt-2.output","aspect_ratio":"16:9","num_images":1},"app":"fal-ai/nano-banana-pro","metadata":{"position":{"x":2800,"y":600}}},"node-video-prompt-2":{"type":"run","id":"node-video-prompt-2","depends":["node-scene-planner"],"input":{"prompt":"$node-scene-planner.output","system_prompt":"From the scene plan, create a Seedance video prompt for SCENE 2.\n\nRULES:\n- ONE clear action only (4 sec)\n- NO dialogue - ambient sounds only\n- Realistic movement\n- Format: [Subject + motion], [camera], [ambient sound]\n\nMax 25 words.","model":"google/gemini-2.5-flash","temperature":0.7},"app":"openrouter/router","metadata":{"position":{"x":1900,"y":1000}}},"node-video-2":{"type":"run","id":"node-video-2","depends":["node-image-2","node-video-prompt-2"],"input":{"prompt":"$node-video-prompt-2.output","image_url":"$node-image-2.images.0.url","aspect_ratio":"16:9","resolution":"720p","duration":"4","generate_audio":true},"app":"fal-ai/bytedance/seedance/v1.5/pro/image-to-video","metadata":{"position":{"x":3700,"y":600}}},"node-image-prompt-3":{"type":"run","id":"node-image-prompt-3","depends":["node-scene-planner"],"input":{"prompt":"$node-scene-planner.output","system_prompt":"From the scene plan, create an image prompt for SCENE 3.\n\nFormat: POV first-person perspective, [what we see], [people/objects], [lighting], [atmosphere]. Shot on 35mm film, photorealistic, cinematic, 8K, no text.\n\nOutput ONLY the prompt, max 80 words.","model":"google/gemini-2.5-flash","temperature":0.7},"app":"openrouter/router","metadata":{"position":{"x":1900,"y":1200}}},"node-image-3":{"type":"run","id":"node-image-3","depends":["node-image-prompt-3"],"input":{"prompt":"$node-image-prompt-3.output","aspect_ratio":"16:9","num_images":1},"app":"fal-ai/nano-banana-pro","metadata":{"position":{"x":2800,"y":1200}}},"node-video-prompt-3":{"type":"run","id":"node-video-prompt-3","depends":["node-scene-planner"],"input":{"prompt":"$node-scene-planner.output","system_prompt":"From the scene plan, create a Seedance video prompt for SCENE 3.\n\nRULES:\n- ONE clear action only (4 sec)\n- NO dialogue - ambient sounds only\n- Realistic movement\n- Format: [Subject + motion], [camera], [ambient sound]\n\nMax 25 words.","model":"google/gemini-2.5-flash","temperature":0.7},"app":"openrouter/router","metadata":{"position":{"x":1900,"y":1600}}},"node-video-3":{"type":"run","id":"node-video-3","depends":["node-image-3","node-video-prompt-3"],"input":{"prompt":"$node-video-prompt-3.output","image_url":"$node-image-3.images.0.url","aspect_ratio":"16:9","resolution":"720p","duration":"4","generate_audio":true},"app":"fal-ai/bytedance/seedance/v1.5/pro/image-to-video","metadata":{"position":{"x":3700,"y":1200}}},"node-image-prompt-4":{"type":"run","id":"node-image-prompt-4","depends":["node-scene-planner"],"input":{"prompt":"$node-scene-planner.output","system_prompt":"From the scene plan, create an image prompt for SCENE 4.\n\nFormat: POV first-person perspective, [what we see], [people/objects], [lighting], [atmosphere]. Shot on 35mm film, photorealistic, cinematic, 8K, no text.\n\nOutput ONLY the prompt, max 80 words.","model":"google/gemini-2.5-flash","temperature":0.7},"app":"openrouter/router","metadata":{"position":{"x":1900,"y":1800}}},"node-image-4":{"type":"run","id":"node-image-4","depends":["node-image-prompt-4"],"input":{"prompt":"$node-image-prompt-4.output","aspect_ratio":"16:9","num_images":1},"app":"fal-ai/nano-banana-pro","metadata":{"position":{"x":2800,"y":1800}}},"node-video-prompt-4":{"type":"run","id":"node-video-prompt-4","depends":["node-scene-planner"],"input":{"prompt":"$node-scene-planner.output","system_prompt":"From the scene plan, create a Seedance video prompt for SCENE 4.\n\nRULES:\n- ONE clear action only (4 sec)\n- NO dialogue - ambient sounds only\n- Realistic movement\n- Format: [Subject + motion], [camera], [ambient sound]\n\nMax 25 words.","model":"google/gemini-2.5-flash","temperature":0.7},"app":"openrouter/router","metadata":{"position":{"x":1900,"y":2200}}},"node-video-4":{"type":"run","id":"node-video-4","depends":["node-image-4","node-video-prompt-4"],"input":{"prompt":"$node-video-prompt-4.output","image_url":"$node-image-4.images.0.url","aspect_ratio":"16:9","resolution":"720p","duration":"4","generate_audio":true},"app":"fal-ai/bytedance/seedance/v1.5/pro/image-to-video","metadata":{"position":{"x":3700,"y":1800}}},"node-image-prompt-5":{"type":"run","id":"node-image-prompt-5","depends":["node-scene-planner"],"input":{"prompt":"$node-scene-planner.output","system_prompt":"From the scene plan, create an image prompt for SCENE 5.\n\nFormat: POV first-person perspective, [what we see], [people/objects], [lighting], [atmosphere]. Shot on 35mm film, photorealistic, cinematic, 8K, no text.\n\nOutput ONLY the prompt, max 80 words.","model":"google/gemini-2.5-flash","temperature":0.7},"app":"openrouter/router","metadata":{"position":{"x":1900,"y":2400}}},"node-image-5":{"type":"run","id":"node-image-5","depends":["node-image-prompt-5"],"input":{"prompt":"$node-image-prompt-5.output","aspect_ratio":"16:9","num_images":1},"app":"fal-ai/nano-banana-pro","metadata":{"position":{"x":2800,"y":2400}}},"node-video-prompt-5":{"type":"run","id":"node-video-prompt-5","depends":["node-scene-planner"],"input":{"prompt":"$node-scene-planner.output","system_prompt":"From the scene plan, create a Seedance video prompt for SCENE 5.\n\nRULES:\n- ONE clear action only (4 sec)\n- NO dialogue - ambient sounds only\n- Realistic movement\n- Format: [Subject + motion], [camera], [ambient sound]\n\nMax 25 words.","model":"google/gemini-2.5-flash","temperature":0.7},"app":"openrouter/router","metadata":{"position":{"x":1900,"y":2800}}},"node-video-5":{"type":"run","id":"node-video-5","depends":["node-image-5","node-video-prompt-5"],"input":{"prompt":"$node-video-prompt-5.output","image_url":"$node-image-5.images.0.url","aspect_ratio":"16:9","resolution":"720p","duration":"4","generate_audio":true},"app":"fal-ai/bytedance/seedance/v1.5/pro/image-to-video","metadata":{"position":{"x":3700,"y":2286.7341491247616}}},"node-image-prompt-6":{"type":"run","id":"node-image-prompt-6","depends":["node-scene-planner"],"input":{"prompt":"$node-scene-planner.output","system_prompt":"From the scene plan, create an image prompt for SCENE 6 (CLIMAX).\n\nFormat: POV first-person perspective, [what we see], [people/objects], [lighting], [atmosphere]. Shot on 35mm film, photorealistic, cinematic, 8K, no text.\n\nOutput ONLY the prompt, max 80 words.","model":"google/gemini-2.5-flash","temperature":0.7},"app":"openrouter/router","metadata":{"position":{"x":1900,"y":3000}}},"node-image-6":{"type":"run","id":"node-image-6","depends":["node-image-prompt-6"],"input":{"prompt":"$node-image-prompt-6.output","aspect_ratio":"16:9","num_images":1},"app":"fal-ai/nano-banana-pro","metadata":{"position":{"x":2800,"y":3000}}},"node-video-prompt-6":{"type":"run","id":"node-video-prompt-6","depends":["node-scene-planner"],"input":{"prompt":"$node-scene-planner.output","system_prompt":"From the scene plan, create a Seedance video prompt for SCENE 6 (CLIMAX).\n\nRULES:\n- ONE powerful action only (4 sec)\n- NO dialogue - intense ambient sounds only\n- Dramatic but realistic movement\n- Format: [Subject + intense motion], [dynamic camera], [powerful ambient sound]\n\nSounds: explosion, crash, rushing water, roaring fire, screaming crowd, thunder\n\nMax 25 words.","model":"google/gemini-2.5-flash","temperature":0.7},"app":"openrouter/router","metadata":{"position":{"x":1900,"y":3400}}},"node-video-6":{"type":"run","id":"node-video-6","depends":["node-image-6","node-video-prompt-6"],"input":{"prompt":"$node-video-prompt-6.output","image_url":"$node-image-6.images.0.url","aspect_ratio":"16:9","resolution":"720p","duration":"4","generate_audio":true},"app":"fal-ai/bytedance/seedance/v1.5/pro/image-to-video","metadata":{"position":{"x":3700,"y":3000}}}},"output":{"final_video":"$node-merge-videos.video","scene_1":"$node-video-1.video","scene_2":"$node-video-2.video","scene_3":"$node-video-3.video","scene_4":"$node-video-4.video","scene_5":"$node-video-5.video","scene_6":"$node-video-6.video","still_1":"$node-image-1.images.0.url","still_2":"$node-image-2.images.0.url","still_3":"$node-image-3.images.0.url","still_4":"$node-image-4.images.0.url","still_5":"$node-image-5.images.0.url","still_6":"$node-image-6.images.0.url","scene_plan":"$node-scene-planner.output"},"schema":{"input":{"film_name":{"name":"film_name","label":"Film Name","type":"string","description":"Enter any film name to generate 6 immersive POV video experiences","required":true,"examples":["Titanic","The Godfather","Blade Runner","Gladiator","Inception"],"ui":{"placeholder":"e.g., Titanic, The Godfather, Blade Runner..."},"modelId":"node-scene-planner"}},"output":{"final_video":{"name":"final_video","label":"Complete Film Experience","type":"string"},"scene_1":{"name":"scene_1","label":"Scene 1","type":"string"},"scene_2":{"name":"scene_2","label":"Scene 2","type":"string"},"scene_3":{"name":"scene_3","label":"Scene 3","type":"string"},"scene_4":{"name":"scene_4","label":"Scene 4","type":"string"},"scene_5":{"name":"scene_5","label":"Scene 5","type":"string"},"scene_6":{"name":"scene_6","label":"Scene 6","type":"string"}}},"version":"1","metadata":{"input":{"position":{"x":-100,"y":0}},"description":"Film POV Experience Generator v2 - Enter any film, get 6 immersive POV scenes with ambient audio (~24 sec total)"}},"is_public":false,"user_id":"","user_nickname":"","created_at":""}
```

---

## Game Assets (Image to 3D Model)

Converts 2D images into 3D models by generating multiple view angles and feeding them to Rodin 3D generator.

**Input:** Image URLs
**Output:** 3D mesh model (.glb)

**Flow:**
```
[Image] → [Edit: 3D Asset Style] → [Left View]  →
                                 → [Right View] → [Rodin 3D] → [3D Mesh]
                                 → [Back View]  →
```

```json
{"name":"game-assets-wf","title":"Game Assets WF","contents":{"name":"workflow","nodes":{"output":{"type":"display","id":"output","depends":["fal_ai/hyper3d/rodin/v2"],"fields":{"model_mesh":"$fal_ai/hyper3d/rodin/v2.model_mesh"},"metadata":{"position":{"x":2842.5165179706196,"y":254.79605021097325}},"input":{}},"fal_ai/bytedance/seedream/v4/edit":{"type":"run","id":"fal_ai/bytedance/seedream/v4/edit","depends":["input"],"metadata":{"position":{"x":100,"y":200}},"app":"fal-ai/bytedance/seedream/v4/edit","input":{"prompt":"Convert the [OBJECT] in the image into a 3D asset. Transparent background, no shadows, smooth texture","image_urls":"$input.image_urls"}},"fal_ai/bytedance/seedream/v4/edit_2":{"type":"run","id":"fal_ai/bytedance/seedream/v4/edit_2","depends":["fal_ai/bytedance/seedream/v4/edit"],"metadata":{"position":{"x":844.7445043154871,"y":184.9266509044162}},"app":"fal-ai/bytedance/seedream/v4/edit","input":{"image_urls":["$fal_ai/bytedance/seedream/v4/edit.images.0.url"],"prompt":"show this 3d object from left side","image_size":{"width":4000,"height":4000},"num_images":1}},"fal_ai/bytedance/seedream/v4/edit_2_2":{"type":"run","id":"fal_ai/bytedance/seedream/v4/edit_2_2","depends":["fal_ai/bytedance/seedream/v4/edit"],"metadata":{"position":{"x":1000,"y":800}},"app":"fal-ai/bytedance/seedream/v4/edit","input":{"image_urls":["$fal_ai/bytedance/seedream/v4/edit.images.0.url"],"prompt":"show this 3d object from right side","image_size":{"width":4000,"height":4000}}},"fal_ai/bytedance/seedream/v4/edit_2_2_2":{"type":"run","id":"fal_ai/bytedance/seedream/v4/edit_2_2_2","depends":["fal_ai/bytedance/seedream/v4/edit"],"metadata":{"position":{"x":1000,"y":1400}},"app":"fal-ai/bytedance/seedream/v4/edit","input":{"image_urls":["$fal_ai/bytedance/seedream/v4/edit.images.0.url"],"prompt":"show this 3d object from back side","image_size":{"width":4000,"height":4000}}},"fal_ai/hyper3d/rodin/v2":{"type":"run","id":"fal_ai/hyper3d/rodin/v2","depends":["fal_ai/bytedance/seedream/v4/edit_2","fal_ai/bytedance/seedream/v4/edit_2_2","fal_ai/bytedance/seedream/v4/edit_2_2_2","fal_ai/bytedance/seedream/v4/edit"],"metadata":{"position":{"x":1998.2605283937303,"y":379.1449264781792}},"app":"fal-ai/hyper3d/rodin/v2","input":{"input_image_urls":["$fal_ai/bytedance/seedream/v4/edit_2.images.0.url","$fal_ai/bytedance/seedream/v4/edit_2_2.images.0.url","$fal_ai/bytedance/seedream/v4/edit_2_2_2.images.0.url","$fal_ai/bytedance/seedream/v4/edit.images.0.url"],"quality_mesh_option":"500K Triangle","preview_render":false,"prompt":"","material":"All","TAPose":true}}},"output":{"model_mesh":"$fal_ai/hyper3d/rodin/v2.model_mesh"},"schema":{"input":{"image_urls":{"name":"image_urls","label":"Image URLs","type":{"kind":"list","elementType":"string"},"description":"List of URLs of input images for editing. Presently, up to 10 image inputs are allowed. If over 10 images are sent, only the last 10 will be used.","required":true,"examples":[["https://storage.googleapis.com/falserverless/example_inputs/seedream4_edit_input_1.png"]],"ui":{},"modelId":"fal_ai/bytedance/seedream/v4/edit"}},"output":{}},"version":"1","metadata":{"input":{"position":{"x":-731.47950209894,"y":171.83462441548374}}}},"is_public":true,"user_id":"","user_nickname":"","created_at":""}
```

---

## Key Models Used

| Workflow | Models |
|----------|--------|
| Live-in-Scene | `openrouter/router`, `fal-ai/nano-banana-pro`, `fal-ai/bytedance/seedance/v1.5/pro/image-to-video`, `fal-ai/ffmpeg-api/merge-videos` |
| Game Assets | `fal-ai/bytedance/seedream/v4/edit`, `fal-ai/hyper3d/rodin/v2` |
```

## File: `skills/claude.ai/fal-workflow/scripts/create-workflow.sh`
```bash
#!/bin/bash

# fal.ai Workflow Creation Script
# Usage: ./create-workflow.sh --name NAME --title TITLE --description DESC --nodes JSON --outputs JSON
# Returns: Workflow JSON definition

set -e

# Default values
NAME=""
TITLE=""
DESCRIPTION=""
NODES=""
OUTPUTS=""

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --name)
            NAME="$2"
            shift 2
            ;;
        --title)
            TITLE="$2"
            shift 2
            ;;
        --description)
            DESCRIPTION="$2"
            shift 2
            ;;
        --nodes)
            NODES="$2"
            shift 2
            ;;
        --outputs)
            OUTPUTS="$2"
            shift 2
            ;;
        *)
            echo "Unknown option: $1" >&2
            exit 1
            ;;
    esac
done

# Validate required inputs
if [ -z "$NAME" ]; then
    echo "Error: --name is required" >&2
    exit 1
fi

if [ -z "$TITLE" ]; then
    TITLE="$NAME"
fi

if [ -z "$NODES" ]; then
    echo "Error: --nodes is required (JSON array)" >&2
    exit 1
fi

if [ -z "$OUTPUTS" ]; then
    echo "Error: --outputs is required (JSON object)" >&2
    exit 1
fi

# Create temp directory
TEMP_DIR=$(mktemp -d)
trap 'rm -rf "$TEMP_DIR"' EXIT

echo "Creating workflow: $TITLE..." >&2

# Parse nodes array and build workflow structure
# This is a simplified version - the MCP tool handles complex validation
WORKFLOW_FILE="$TEMP_DIR/workflow.json"

# Build the workflow JSON
cat > "$WORKFLOW_FILE" << EOF
{
  "_type": "ComfyApp",
  "version": "0.1.0",
  "name": "$NAME",
  "title": "$TITLE",
  "description": "$DESCRIPTION",
  "nodes": {},
  "outputs": $OUTPUTS
}
EOF

# Process nodes and add to workflow
# Note: This is a basic implementation. For full validation, use the MCP tool.
echo "Processing nodes..." >&2

# Use Python/jq if available for proper JSON manipulation
if command -v python3 &> /dev/null; then
    python3 << PYTHON_EOF
import json
import sys

# Read workflow
with open("$WORKFLOW_FILE", "r") as f:
    workflow = json.load(f)

# Parse nodes
nodes = json.loads('''$NODES''')

# Build nodes object
for node in nodes:
    node_id = node.get("nodeId", "")
    model_id = node.get("modelId", "")
    node_input = node.get("input", {})
    depends_on = node.get("dependsOn", [])

    # Detect dependencies from input references
    for key, value in node_input.items():
        if isinstance(value, str) and value.startswith("\$") and not value.startswith("\$input"):
            ref_node = value.split(".")[0][1:]  # Remove $ and get node name
            if ref_node not in depends_on:
                depends_on.append(ref_node)

    workflow["nodes"][node_id] = {
        "app": model_id,
        "input": node_input
    }

    if depends_on:
        workflow["nodes"][node_id]["dependsOn"] = depends_on

# Write result
print(json.dumps(workflow, indent=2))
PYTHON_EOF
else
    # Fallback: output the basic structure
    echo "Warning: Python not available, outputting basic structure" >&2
    cat "$WORKFLOW_FILE"
fi

echo "" >&2
echo "Workflow created successfully!" >&2
```

