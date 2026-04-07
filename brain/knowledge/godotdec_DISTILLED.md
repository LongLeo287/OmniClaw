---
id: godotdec
type: knowledge
owner: OA_Triage
---
# godotdec
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
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
|            | ----- Begin of file contents -----                           |

The source code of the .pck packer can be found [here](https://github.com/godotengine/godot/blob/master/core/io/pck_packer.cpp)

### Limitations

- This tool is designed to extract assets. If you are interested in the scripts of a game, check out [Godot RE Tools](https://github.com/bruvzg/gdsdecomp)
- MD5 checksum is not used to verify extracted files
- Format conversion is only supported for .png, .ogg
- Modified engine versions may use a custom package format, which godotdec does not support

### Remarks

No reverse engineering has been used to write this tool.

I released it as a helper for artists to search games for unlicensed use of their assets. It is not meant to encourage extraction with the sole purpose of using assets in your own products without permission of the copyright holder.

Remember: don't steal assets from other people's games. Respect copyrights. And don't protect your own games - it's unnecessary effort.
```

### File: changelog.txt
```txt
2.1.2
  Updated BioLib to 2.5.0

2.1.1
  Changed minimum .NET Framework to 4
  Updated BioLib to 2.0.0

2.1.0
  Added BioLib dependency
  Changed minimum .NET Framework to 4.5

2.0.0
  Added support for bigger archives
  Added command line parameter to convert certain file types after extraction
  Fixed several extraction failures

1.0.0
  Initial release
```

