---
id: godotdec-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:48.542257
---

# OmniClaw Knowledge Report: godotdec

## Tech Stack
Unknown

## File Statistics
```json
{
  "": 2,
  ".txt": 1,
  ".sln": 1,
  ".user": 1,
  ".md": 1,
  ".config": 2,
  ".csproj": 1,
  ".cs": 2
}
```

## README Snippet
```markdown
# godotdec

An unpacker for Godot Engine package files (.pck)

### Usage
`godotdec [<options>] <input_file> [<output_dir>]`

###### Options:

| Flag (short) | Flag (long) | Description                                                  |
| ------------ | ----------- | ------------------------------------------------------------ |
| -c           | --convert   | Convert certain engine-specific file types (textures, some audio streams) to standard formats. |

### Technical details

Godot Engine's package format is specified as:

| Value/Type | Description                                                  |
| ---------- | ------------------------------------------------------------ |
| 0x43504447 | Magic number (GDPC)                                          |
| 4 x Int32  | Engine version: version, major, minor, revision              |
| 16 x Int32 | Reserved space, 0                                            |
| Int32      | Number of files in archive                                   |
|            | ----- Begin of file index, for each file the following data is stored ---- |
| Int32      | Length of path string                                        |
| String     | Path as string, e.g. res://actors/Enemy/enemy.atex           |
| Int64      | File offset                                                  |
| Int64      | File size                                                    |
| 16 bytes   | MD5                                                          |
|            | -----
```

**Processed by OmniClaw Automated Intake**