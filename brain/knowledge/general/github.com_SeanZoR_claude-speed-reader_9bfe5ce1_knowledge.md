---
id: github.com-seanzor-claude-speed-reader-9bfe5ce1-kn
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:19.682064
---

# KNOWLEDGE EXTRACT: github.com_SeanZoR_claude-speed-reader_9bfe5ce1
> **Extracted on:** 2026-04-01 10:21:14
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007520835/github.com_SeanZoR_claude-speed-reader_9bfe5ce1

---

## File: `LICENSE`
```
MIT License

Copyright (c) 2025 Sean Oliver

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
# claude-speed-reader

Speed read Claude's responses at 600+ WPM using RSVP with Spritz-style ORP highlighting.

![Speed Reader Demo](demo.gif)

## What is this?

A Claude Code skill that lets you speed-read any response. Uses **Rapid Serial Visual Presentation (RSVP)** — displaying one word at a time with the **Optimal Recognition Point (ORP)** highlighted in red. Your eyes stay fixed while your brain processes text at 2-3x normal reading speed.

## Install

```bash
# Clone to your Claude skills directory
git clone https://github.com/SeanZoR/claude-speed-reader.git ~/.claude/skills/speed
```

Or manually copy the `.claude/` folder contents to your `~/.claude/` directory.

## Usage

In Claude Code, after any response:

```
/speed
```

That's it. Opens a minimal dark reader with the last response loaded.

**Custom text:**
```
/speed "Your text here"
```

## Controls

| Key | Action |
|-----|--------|
| `Space` | Play / Pause |
| `←` `→` | Adjust speed (±50 WPM) |
| `R` | Restart |
| `V` | Paste new text |

Click anywhere to toggle play/pause. Drag & drop text files supported.

## How ORP Works

The red highlighted letter is the **Optimal Recognition Point** — positioned ~1/3 into each word where your brain naturally focuses. By keeping this point fixed on screen, you eliminate eye movement (saccades) that consume 80% of reading time.

```
    th[e] quick br[o]wn fox ju[m]ps
       ↑         ↑         ↑
      ORP       ORP       ORP
```

## Customization

Edit `~/.claude/skills/speed/data/reader.html` to customize:
- Default WPM (currently 600)
- Colors and fonts
- Timing multipliers for punctuation

## Requirements

- Claude Code
- macOS (uses `open` command)

## License

MIT

---

Built for humans who want to read Claude's novels faster.
```

