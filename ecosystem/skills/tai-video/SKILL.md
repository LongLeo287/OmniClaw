---
name: tai-video
description: Download videos from Facebook, YouTube, TikTok and thousands of other sites using yt-dlp. Activate when user requests to download video, save video from any URL.
---

// turbo-all

# Download Video using yt-dlp

**Always use `yt-dlp`** for ALL video download operations. Supports Facebook, YouTube, TikTok, Instagram, Twitter/X, and [thousands of other sites](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md).

## When to activate this skill

- User requests to **download video**, **save video** from URL
- User sends video link and wants to download
- User requests to download music/audio from video

## Dependencies

| Tool | Check | Install |
|------|----------|---------|
| `yt-dlp` | `yt-dlp --version` | `pip install yt-dlp` |
| `ffmpeg` | `ffmpeg -version` | `winget install --id Gyan.FFmpeg -e --accept-package-agreements --accept-source-agreements` |

> [!IMPORTANT]
> After installing ffmpeg with winget, need to refresh PATH:
> ```powershell
> $env:Path = [System.Environment]::GetEnvironmentVariable("Path","Machine") + ";" + [System.Environment]::GetEnvironmentVariable("Path","User")
> ```

## Download video (default — best quality)

```powershell
yt-dlp -o "<output_dir>\%(title).100Bs.%(ext)s" "<URL>"
```

### Output parameter explanation

| Part | Meaning |
|------|---------|
| `%(title).100Bs` | Video title, max 100 bytes (avoid overly long filenames) |
| `%(ext)s` | Auto extension (mp4, webm...) |

## Download audio (only when user requests)

```powershell
yt-dlp -x --audio-format mp3 -o "<output_dir>\%(title).100Bs.%(ext)s" "<URL>"
```

## Download video with quality selection

### List available formats

```powershell
yt-dlp -F "<URL>"
```

### Download specific format

```powershell
yt-dlp -f <format_id> -o "<output_dir>\%(title).100Bs.%(ext)s" "<URL>"
```

## Download playlist / multiple videos

```powershell
yt-dlp -o "<output_dir>\%(playlist_title)s\%(title).100Bs.%(ext)s" "<PLAYLIST_URL>"
```

## Common error handling

| Error | Solution |
|-----|-----------|
| Video requires login | Use `--cookies-from-browser chrome` to get cookies from browser |
| Filename encoding error | Add `--encoding utf-8` or use `%(id)s` instead of `%(title)s` |
| Blocked from downloading | Try `--user-agent "Mozilla/5.0"` or use cookies |
| FFmpeg not found | Install ffmpeg according to Dependencies table above |

## Important Rules

1. **Default save to user's current directory**, unless user specifies otherwise
2. **Always use absolute path** for output directory
3. **Always set `SafeToAutoRun: true`** because this skill has `// turbo-all` annotation
4. **After download complete**, report: filename, size, save location
5. **If filename has encoding issues** (special characters), rename for simplicity
