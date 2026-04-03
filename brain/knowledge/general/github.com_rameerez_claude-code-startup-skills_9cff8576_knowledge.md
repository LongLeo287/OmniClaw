---
id: github.com-rameerez-claude-code-startup-skills-9cf
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:17.199654
---

# KNOWLEDGE EXTRACT: github.com_rameerez_claude-code-startup-skills_9cff8576
> **Extracted on:** 2026-04-01 14:36:18
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007524007/github.com_rameerez_claude-code-startup-skills_9cff8576

---

## File: `LICENSE`
```
MIT License

Copyright (c) 2026 Javi

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## File: `README.md`
```markdown
# Startup Skills for Claude Code

Essential [Claude Code](https://claude.ai/code) skills for building startups, SaaS, and software businesses.

## Install

```bash
/plugin marketplace add rameerez/claude-code-startup-skills
/plugin install startup@rameerez-claude-code-startup-skills
```

Done. Now you have access to all skills below.

## Skills

| Skill | What it does |
|-------|--------------|
| `/startup:compress-images` | Compress images to WebP for blazing fast page loads |
| `/startup:customer-empathy` | Deep-dive into customer empathy and user journey thinking |
| `/startup:download-video` | Download videos from X, YouTube, TikTok, Instagram, etc. |
| `/startup:transcribe-video` | Generate subtitles and transcripts from video/audio |
| `/startup:x-post` | Post to X (Twitter) — text, images, and video |

## Usage

```
/startup:compress-images ./images/
/startup:download-video https://x.com/user/status/123
/startup:transcribe-video ./video.mp4
/startup:x-post "Just shipped a new feature!"
/startup:customer-empathy
```

## Contributing

PRs welcome! Add your skill to `skills/<skill-name>/SKILL.md`.

## License

MIT
```

## File: `skills/compress-images/SKILL.md`
```markdown
---
name: compress-images
description: Compress images for web/SEO performance using cwebp. Use when optimizing images for faster page loads, reducing file sizes, or converting JPG/PNG to WebP format.
argument-hint: "[directory]"
allowed-tools: Bash(cwebp:*), Bash(ls:*), Bash(mkdir:*), Bash(mv:*)
---

# Image Compression Skill

Compress all images in `$ARGUMENTS` (or `app/assets/images/content/` if no path provided) to WebP format, optimized for SEO performance (target: under 100KB per image).

## Process

1. **Create originals folder** - Create `originals/` subfolder inside the target directory and move source files there. Never destroy source files.
2. **Compress each image** (JPG, PNG, GIF) from `originals/` to the parent directory as `.webp`
3. **Iterate until all images are under 100KB** - check sizes after each pass, re-compress any that exceed the target
4. **Report results** with before/after sizes
5. **Update references** in content files from old extensions to `.webp`

## File Structure

```
target-directory/
├── originals/           # High-quality source files preserved here
│   ├── hero.jpg
│   └── feature.png
├── hero.webp            # Compressed, web-optimized
└── feature.webp
```

## Iterative Compression Algorithm

**IMPORTANT:** Keep compressing until ALL images are under 100KB. Check sizes after each pass and re-compress any that exceed the target.

### Step 1: Initial pass (q 70)
```bash
cwebp -q 70 -resize 1200 0 originals/image.jpg -o image.webp
ls -lh image.webp  # Check size
```

### Step 2: If still over 100KB, reduce quality progressively
```bash
# Try these in order until under 100KB:
cwebp -q 60 -resize 1200 0 originals/image.jpg -o image.webp
cwebp -q 50 -resize 1200 0 originals/image.jpg -o image.webp
cwebp -q 45 -resize 1200 0 originals/image.jpg -o image.webp
cwebp -q 40 -resize 1200 0 originals/image.jpg -o image.webp
cwebp -q 35 -resize 1200 0 originals/image.jpg -o image.webp
```

### Step 3: For stubborn images, also reduce dimensions
```bash
# If q 35 at 1200px is still over 100KB, reduce to 1000px:
cwebp -q 30 -resize 1000 0 originals/image.jpg -o image.webp
cwebp -q 25 -resize 1000 0 originals/image.jpg -o image.webp
```

## Real-World Results (Reference)

From actual compression run on content images:

| Image | Original | First Try | Final | Settings Used |
|-------|----------|-----------|-------|---------------|
| waves.jpg | 198KB | 33KB | 33KB | q 70, 1200px (1 pass) |
| calendar.jpg | 246KB | 42KB | 42KB | q 70, 1200px (1 pass) |
| floating.jpg | 230KB | 43KB | 43KB | q 70, 1200px (1 pass) |
| cash.jpg | 409KB | 88KB | 88KB | q 70, 1200px (1 pass) |
| knot.jpg | 395KB | 96KB | 96KB | q 70, 1200px (1 pass) |
| floating-dark.jpg | 414KB | 94KB | 94KB | q 70, 1200px (1 pass) |
| keyboard2.jpg | 459KB | 102KB | 102KB | q 70, 1200px (1 pass, acceptable) |
| **perpetual.jpg** | 565KB | 130KB | **96KB** | q 40, 1200px (3 passes) |
| **keyboard.jpg** | 718KB | 196KB | **98KB** | q 25, 1000px (5 passes) |

### Key Insights

1. **Most images** (under 500KB source) compress fine with default settings (q 70, 1200px)
2. **Large detailed images** (500KB+) often need multiple passes
3. **Very large images** (700KB+) may need both lower quality AND smaller dimensions
4. **Keyboard/tech photos** with fine detail are hardest to compress - expect 4-5 passes
5. **Soft/blurry images** compress much better than sharp detailed ones

## After Compression

1. **Verify ALL files under 100KB**: `ls -lh *.webp` - re-run compression on any exceeding target
2. Update content files referencing old extensions (.jpg, .png) to use .webp
3. Test that images render correctly in the application
4. Original files remain in `originals/` folder for future reference or re-compression
```

## File: `skills/customer-empathy/SKILL.md`
```markdown
---
name: customer-empathy
description: Deep-dive into customer empathy and user journey thinking. Use when designing onboarding, improving UX, planning features, or trying to understand how to delight users faster.
---

# Customer Empathy Exercise

Pause and deeply empathize with your users before continuing any work. Think through these questions to clarify who you're building for and how to serve them best.

## The Customer

**Who is our ideal customer?**
- What's their role, context, situation?
- What brings them to us right now?

**What job are they trying to get done?**
- What's the outcome they actually want?
- What would "done" look like for them?

## Their Journey

**What's their mental state at each step of the way before getting to this point?**
- What are they feeling when they first arrive?
- What questions are in their head?
- Where might they feel confused, frustrated, or stuck?
- When do they feel momentum and progress?

**What do they care about?**
- What matters most to them right now?
- What would make them think "yes! This is it!"?

**What do they NOT care about?**
- What features/details are we obsessing over that they'd skip right past?
- What complexity can we remove entirely?

## Delivering Value

**How can we best help them?**
- What's the single most valuable thing we can do for them?

**How do we make them succeed?**
- What does success look like from their perspective?
- What's blocking them from getting there RIGHT NOW?

**How do we make their lives easier?**
- What friction can we eliminate?
- What can we automate or do for them?

## The Magic

**How do we get them to the "aha" moment as fast and easily as humanly possible?**
- What IS the "aha" moment?
- What's the shortest path to it?
- What's currently in the way?

**How can we delight them most?**
- What would make them smile or say "wow!"?
- What unexpected value could we add?

**How can we make this as seamless and magical as humanly possible?**
- What if this just... worked?
- What would "effortless" look like?

**How can we make them "wow!" and provide MOST of the value in the SHORTEST time with the LOWEST effort?**
- What's our 80/20?
- What's the minimum they need to do to get maximum value?

---

*Write your answers. Be specific. Challenge assumptions. Think from their shoes, not ours.*
```

## File: `skills/download-video/SKILL.md`
```markdown
---
name: download-video
description: Download videos from social media URLs (X/Twitter, YouTube, Instagram, TikTok, etc.) using yt-dlp. Use when saving a video locally, extracting content for transcription, or archiving video references.
argument-hint: "[url]"
allowed-tools: Bash(yt-dlp:*), Bash(ls:*), Bash(mkdir:*)
---

# Video Download Skill

Download a video from `$ARGUMENTS` (a social media URL) to the current directory using `yt-dlp`.

Supports X/Twitter, YouTube, Instagram, TikTok, Reddit, and [1400+ other sites](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md).

## Process

1. **Verify yt-dlp is installed** - check with `which yt-dlp`, suggest `brew install yt-dlp` if missing
2. **Download the video** in the best available quality
3. **Report results** with filename, format, and file size

## Download Command

```bash
yt-dlp -o "%(title)s.%(ext)s" "URL"
```

### Options Reference

```bash
# Best video+audio (default)
yt-dlp -o "%(title)s.%(ext)s" "URL"

# List available formats first
yt-dlp -F "URL"

# Pick a specific format
yt-dlp -f "FORMAT_ID" -o "%(title)s.%(ext)s" "URL"

# Audio only (e.g. for podcasts)
yt-dlp -x --audio-format mp3 -o "%(title)s.%(ext)s" "URL"

# Custom output directory
yt-dlp -o "/path/to/dir/%(title)s.%(ext)s" "URL"
```

## Platform-Specific Notes

| Platform | Notes |
|----------|-------|
| X/Twitter | Works with tweet URLs containing video. May need `--cookies-from-browser` for age-restricted content |
| YouTube | Supports playlists, channels, shorts. Use `-F` to pick resolution |
| Instagram | Reels and stories supported. May require authentication for private accounts |
| TikTok | Direct video URLs work. Watermark-free when available |
| Reddit | Handles v.redd.it links with audio merging automatically |

## After Download

1. **Verify the file**: `ls -lh *.mp4` (or whatever extension was downloaded)
2. Report the filename, format, resolution, and file size to the user
3. If the user wants subtitles or a transcript, suggest using `/transcribe-video`
```

## File: `skills/transcribe-video/SKILL.md`
```markdown
---
name: transcribe-video
description: Generate subtitles (SRT/VTT) and plain text transcripts from video or audio files using AWS Transcribe. Use when creating captions, extracting spoken content, generating transcripts for notes, or making video content searchable.
argument-hint: "[file] [language-code]"
allowed-tools: Bash(ffmpeg:*), Bash(aws:*), Bash(ls:*), Bash(rm:*), Bash(which:*)
---

# Video Transcription Skill

Generate subtitles and transcripts from `$ARGUMENTS` (a video or audio file path, optionally followed by a language code like `en-US` or `es-ES`) using AWS Transcribe.

Outputs `.srt`, `.vtt`, and `.txt` files next to the source file.

## Process

1. **Verify prerequisites** - check `ffmpeg` and `aws` CLI are installed and configured
2. **Extract audio** from the video as MP3 using ffmpeg
3. **Create temporary S3 bucket**, upload audio
4. **Run AWS Transcribe** job with SRT and VTT subtitle output
5. **Download results** and generate plain text transcript
6. **Clean up all AWS resources** - delete S3 bucket, Transcribe job, and temp files. No recurring costs.

## Prerequisites

- `ffmpeg` installed (`brew install ffmpeg`)
- `aws` CLI installed and configured with valid credentials (`brew install awscli && aws configure`)
- AWS credentials need permissions for: `s3:*` (create/delete buckets), `transcribe:*` (start/delete jobs)

## Step-by-Step

### Step 1: Extract audio

```bash
ffmpeg -i "input.mp4" -vn -acodec mp3 -q:a 2 "/tmp/transcribe-audio.mp3" -y
```

### Step 2: Create temp S3 bucket and upload

```bash
BUCKET="tmp-transcribe-$(date +%s)"
aws s3 mb "s3://$BUCKET" --region us-east-1
aws s3 cp "/tmp/transcribe-audio.mp3" "s3://$BUCKET/audio.mp3"
```

### Step 3: Start transcription job

```bash
JOB_NAME="tmp-job-$(date +%s)"
aws transcribe start-transcription-job \
  --transcription-job-name "$JOB_NAME" \
  --language-code en-US \
  --media-format mp3 \
  --media "MediaFileUri=s3://$BUCKET/audio.mp3" \
  --subtitles "Formats=srt,vtt" \
  --output-bucket-name "$BUCKET" \
  --region us-east-1
```

**Language codes:** `en-US`, `es-ES`, `fr-FR`, `de-DE`, `pt-BR`, `ja-JP`, `zh-CN`, `it-IT`, `ko-KR`, etc. Default to `en-US` if not specified.

### Step 4: Poll until complete

```bash
while true; do
  STATUS=$(aws transcribe get-transcription-job \
    --transcription-job-name "$JOB_NAME" \
    --region us-east-1 \
    --query 'TranscriptionJob.TranscriptionJobStatus' \
    --output text)
  if [ "$STATUS" = "COMPLETED" ] || [ "$STATUS" = "FAILED" ]; then break; fi
  sleep 5
done
```

### Step 5: Download subtitle files

Save `.srt` and `.vtt` next to the original file:

```bash
aws s3 cp "s3://$BUCKET/$JOB_NAME.srt" "/path/to/input.srt"
aws s3 cp "s3://$BUCKET/$JOB_NAME.vtt" "/path/to/input.vtt"
```

### Step 6: Generate plain text transcript

Download the JSON result and extract the full transcript text:

```bash
aws s3 cp "s3://$BUCKET/$JOB_NAME.json" "/tmp/transcribe-result.json"
```

Then use a tool to extract the `.results.transcripts[0].transcript` field from the JSON and save it as a `.txt` file next to the original.

### Step 7: Clean up everything

**IMPORTANT:** Always clean up to avoid recurring S3 storage costs.

```bash
# Delete S3 bucket and all contents
aws s3 rb "s3://$BUCKET" --force --region us-east-1

# Delete the transcription job
aws transcribe delete-transcription-job --transcription-job-name "$JOB_NAME" --region us-east-1

# Delete temp audio file
rm -f "/tmp/transcribe-audio.mp3" "/tmp/transcribe-result.json"
```

## Real-World Results (Reference)

From actual transcription runs:

| Video | Duration | Audio Size | Transcribe Time | Subtitle Segments |
|-------|----------|------------|-----------------|-------------------|
| X/Twitter clip | 2:40 | 2.5 MB | ~20 seconds | 83 |
| Screen recording | 18:45 | 11.4 MB | ~60 seconds | 500+ |

### Key Insights

1. **AWS Transcribe is fast** - even 19-minute videos complete in about a minute
2. **Short-form content** (tweets, reels) transcribes almost instantly
3. **Cost is negligible** - AWS Transcribe charges ~$0.024/min, so a 19-min video costs ~$0.46
4. **Cleanup is critical** - always delete the S3 bucket to avoid storage charges
5. **SRT is most compatible** - works with most video players and editors; VTT is better for web

## Output Files

```
original-video.mp4
original-video.srt          # Subtitles with timestamps (most compatible)
original-video.vtt          # Web-optimized subtitles (for HTML5 <track>)
original-video.txt          # Plain text transcript (no timestamps)
```

## After Transcription

1. **Verify all output files exist**: `ls -lh /path/to/original-video.{srt,vtt,txt}`
2. Report the number of subtitle segments and total duration
3. Confirm all AWS resources have been cleaned up (no S3 buckets, no Transcribe jobs remaining)
```

## File: `skills/x-post/SKILL.md`
```markdown
---
name: x-post
description: Post to X (Twitter) from the command line. Text, images, and video.
argument-hint: "post \"Your tweet text\" [--media /path/to/file]"
allowed-tools: Bash, Read
model: claude-haiku-4-5-20251001
---

Post to X using the CLI tool at `~/.claude/skills/x-post/x-post.py`.

## Setup

Requires Python packages: `pip install xdk requests_oauthlib`

Credentials file at `~/.claude/skills/x-post/x.key` (JSON):
```json
{
  "api_key": "...",
  "api_secret": "...",
  "access_token": "...",
  "access_token_secret": "..."
}
```

## Commands

**Post text:**
```bash
python ~/.claude/skills/x-post/x-post.py post "Your tweet text"
```

**Post with image:**
```bash
python ~/.claude/skills/x-post/x-post.py post "Your tweet text" --media /path/to/image.jpg
```

**Post with video:**
```bash
python ~/.claude/skills/x-post/x-post.py post "Your tweet text" --media /path/to/video.mp4
```

**Check profile:**
```bash
python ~/.claude/skills/x-post/x-post.py me
```

## Rules

- Always show the user the exact tweet text before posting and get confirmation
- Never post without explicit user approval
- Video uploads use chunked upload (INIT/APPEND/FINALIZE) and may take a minute for processing
- The script auto-detects media type from file extension
```

## File: `skills/x-post/x-post.py`
```python
#!/usr/bin/env python3
"""
CLI tool for posting to X (Twitter) using the xdk Python SDK.
Supports text posts, image posts, and video posts.

Usage:
    python x-post.py post "Hello world"
    python x-post.py post "Check this out" --media /path/to/image.jpg
    python x-post.py post "Watch this" --media /path/to/video.mp4
    python x-post.py me
"""

import argparse
import json
import os
import sys
import time
import mimetypes
import requests

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
KEY_FILE = os.path.join(SCRIPT_DIR, "x.key")

MEDIA_UPLOAD_URL = "https://upload.twitter.com/1.1/media/upload.json"
MEDIA_UPLOAD_V2_URL = "https://api.x.com/2/media/upload"

def load_credentials():
    if not os.path.exists(KEY_FILE):
        print(f"Error: credentials file not found at {KEY_FILE}", file=sys.stderr)
        print("Create x.key with:", file=sys.stderr)
        print(json.dumps({
            "api_key": "YOUR_API_KEY",
            "api_secret": "YOUR_API_SECRET",
            "access_token": "YOUR_ACCESS_TOKEN",
            "access_token_secret": "YOUR_ACCESS_TOKEN_SECRET"
        }, indent=2), file=sys.stderr)
        sys.exit(1)
    with open(KEY_FILE) as f:
        return json.load(f)


def get_client(creds):
    from xdk import Client
    return Client(
        api_key=creds["api_key"],
        api_secret=creds["api_secret"],
        access_token=creds["access_token"],
        access_token_secret=creds["access_token_secret"]
    )


def get_oauth1_session(creds):
    """Create a requests session with OAuth 1.0a for media upload."""
    from requests_oauthlib import OAuth1
    auth = OAuth1(
        creds["api_key"],
        creds["api_secret"],
        creds["access_token"],
        creds["access_token_secret"]
    )
    session = requests.Session()
    session.auth = auth
    return session


def detect_media_type(filepath):
    mime, _ = mimetypes.guess_type(filepath)
    if mime and mime.startswith("video"):
        return "video", mime
    elif mime and mime.startswith("image"):
        if mime == "image/gif":
            return "gif", mime
        return "image", mime
    else:
        ext = os.path.splitext(filepath)[1].lower()
        if ext in (".mp4", ".mov", ".avi", ".webm"):
            return "video", f"video/{ext[1:]}"
        return "image", mime or "image/jpeg"


def upload_image(session, filepath):
    """Upload an image using v1.1 media upload (simple)."""
    media_type = mimetypes.guess_type(filepath)[0] or "image/jpeg"
    with open(filepath, "rb") as f:
        files = {"media_data": None, "media": f}
        resp = session.post(MEDIA_UPLOAD_URL, files={"media": (os.path.basename(filepath), f, media_type)})
    if resp.status_code not in (200, 201, 202):
        print(f"Image upload failed: {resp.status_code} {resp.text}", file=sys.stderr)
        sys.exit(1)
    media_id = resp.json()["media_id_string"]
    print(f"Image uploaded: media_id={media_id}")
    return media_id


def upload_video(session, filepath):
    """Upload a video using chunked media upload (INIT/APPEND/FINALIZE)."""
    file_size = os.path.getsize(filepath)
    media_type = mimetypes.guess_type(filepath)[0] or "video/mp4"

    # INIT
    resp = session.post(MEDIA_UPLOAD_URL, data={
        "command": "INIT",
        "media_type": media_type,
        "total_bytes": file_size,
        "media_category": "tweet_video"
    })
    if resp.status_code not in (200, 201, 202):
        print(f"Video INIT failed: {resp.status_code} {resp.text}", file=sys.stderr)
        sys.exit(1)
    media_id = resp.json()["media_id_string"]
    print(f"Video INIT: media_id={media_id}, size={file_size / 1024 / 1024:.1f}MB")

    # APPEND (4MB chunks)
    segment = 0
    with open(filepath, "rb") as f:
        while True:
            chunk = f.read(4 * 1024 * 1024)
            if not chunk:
                break
            resp = session.post(MEDIA_UPLOAD_URL,
                data={"command": "APPEND", "media_id": media_id, "segment_index": segment},
                files={"media": ("chunk", chunk, "application/octet-stream")}
            )
            if resp.status_code not in (200, 201, 202, 204):
                print(f"Video APPEND failed at segment {segment}: {resp.status_code} {resp.text}", file=sys.stderr)
                sys.exit(1)
            segment += 1
            uploaded = min(f.tell(), file_size)
            print(f"  Uploaded {uploaded / 1024 / 1024:.1f}MB / {file_size / 1024 / 1024:.1f}MB")
    print(f"Video APPEND complete: {segment} segments")

    # FINALIZE
    resp = session.post(MEDIA_UPLOAD_URL, data={
        "command": "FINALIZE",
        "media_id": media_id
    })
    if resp.status_code not in (200, 201, 202):
        print(f"Video FINALIZE failed: {resp.status_code} {resp.text}", file=sys.stderr)
        sys.exit(1)

    result = resp.json()
    processing_info = result.get("processing_info")

    # Wait for processing
    while processing_info and processing_info.get("state") not in ("succeeded", None):
        state = processing_info["state"]
        if state == "failed":
            print(f"Video processing failed: {processing_info}", file=sys.stderr)
            sys.exit(1)
        wait = processing_info.get("check_after_secs", 5)
        print(f"  Processing... ({state}, checking in {wait}s)")
        time.sleep(wait)
        resp = session.get(MEDIA_UPLOAD_URL, params={"command": "STATUS", "media_id": media_id})
        processing_info = resp.json().get("processing_info")

    print(f"Video ready: media_id={media_id}")
    return media_id


def cmd_post(args):
    creds = load_credentials()
    client = get_client(creds)

    body = {"text": args.text}

    if args.media:
        session = get_oauth1_session(creds)
        kind, mime = detect_media_type(args.media)

        if not os.path.exists(args.media):
            print(f"Error: file not found: {args.media}", file=sys.stderr)
            sys.exit(1)

        if kind == "video":
            media_id = upload_video(session, args.media)
        else:
            media_id = upload_image(session, args.media)

        body["media"] = {"media_ids": [media_id]}

    # Post
    response = client.posts.create(body=body)

    if hasattr(response, 'data') and response.data:
        data = response.data
        post_id = data.get("id", "unknown")
        print(f"\nPosted successfully!")
        print(f"  https://x.com/i/status/{post_id}")
        print(f"  Text: {args.text[:80]}{'...' if len(args.text) > 80 else ''}")
        if args.media:
            print(f"  Media: {os.path.basename(args.media)} ({kind})")
    else:
        print(f"Response: {response}")


def cmd_me(args):
    creds = load_credentials()
    client = get_client(creds)
    response = client.users.find_my_user(user_fields=["public_metrics", "description"])
    if hasattr(response, 'data') and response.data:
        d = response.data
        print(f"@{d.get('username', '?')} — {d.get('name', '?')}")
        metrics = d.get("public_metrics", {})
        print(f"  Followers: {metrics.get('followers_count', '?')}")
        print(f"  Following: {metrics.get('following_count', '?')}")
        print(f"  Posts: {metrics.get('tweet_count', '?')}")
    else:
        print(f"Response: {response}")


def main():
    parser = argparse.ArgumentParser(description="Post to X from the command line")
    subparsers = parser.add_subparsers(dest="command")

    post_parser = subparsers.add_parser("post", help="Post a tweet")
    post_parser.add_argument("text", help="Tweet text")
    post_parser.add_argument("--media", help="Path to image or video file")
    post_parser.set_defaults(func=cmd_post)

    me_parser = subparsers.add_parser("me", help="Show your profile info")
    me_parser.set_defaults(func=cmd_me)

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        sys.exit(1)

    args.func(args)


if __name__ == "__main__":
    main()
```

