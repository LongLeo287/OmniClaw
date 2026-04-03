---
id: jthack-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:56.687919
---

# KNOWLEDGE EXTRACT: jthack
> **Extracted on:** 2026-03-30 17:38:13
> **Source:** jthack

---

## File: `ffuf_claude_skill.md`
```markdown
# 📦 jthack/ffuf_claude_skill [🔖 PENDING/APPROVE]
🔗 https://github.com/jthack/ffuf_claude_skill


## Meta
- **Stars:** ⭐ 130 | **Forks:** 🍴 7
- **Language:** Python | **License:** Unknown
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
This is a "skill" for claude to use FFUF.

## README (trích đầu)
```
# FFUF Skill for Claude Code

A Claude Code skill that integrates the powerful web fuzzer [ffuf](https://github.com/ffuf/ffuf) (Fuzz Faster U Fool) for web security testing and reconnaissance tasks.

## Overview

This skill enables Claude Code to perform intelligent web fuzzing operations using ffuf, making it easier to discover hidden directories, files, subdomains, and API endpoints.

## Prerequisites

- [ffuf](https://github.com/ffuf/ffuf) must be installed on your system
- Claude Desktop application
- Appropriate authorization to test target systems

### Installing ffuf

**macOS:**
```bash
brew install ffuf
```

**Linux:**
```bash
go install github.com/ffuf/ffuf/v2@latest
```

**Other methods:** See the [official ffuf repository](https://github.com/ffuf/ffuf)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/jthack/ffuf_claude_skill
```

2. Copy the skill folder to Claude Code's skills directory:
```bash
mkdir -p ~/.claude/skills
cp -r ffuf_claude_skill/ffuf-skill ~/.claude/skills/
```

3. The skill is now available for Claude Code to use!

## Usage

Once installed, you can ask Claude Code to perform ffuf operations naturally:

- "Fuzz the /api endpoint on example.com for hidden paths"
- "Enumerate subdomains for target.com"
- "Find common directories on https://example.com"
- "Test for backup files on the /admin path"

Claude will automatically invoke the ffuf skill and interpret the results for you.

## Features

- **Intelligent Fuzzing**: Claude interprets your testing goals and configures ffuf appropriately
- **Result Analysis**: Automatic filtering and analysis of ffuf output
- **Safe Defaults**: Includes rate limiting and sensible defaults to avoid aggressive testing
- **Wordlist Management**: Helps select appropriate wordlists for different testing scenarios

## Safety & Ethics

**IMPORTANT**: This skill is designed for defensive security purposes only:

- Only test systems you own or have explicit permission to test
- Respect rate limits and avoid causing service disruption
- Follow responsible disclosure practices
- Comply with applicable laws and regulations

Unauthorized testing of systems is illegal and unethical.

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

MIT License - See LICENSE file for details

## Disclaimer

This tool is provided for educational and authorized security testing purposes only. Users are responsible for complying with all applicable laws and obtaining proper authorization before testing any systems.

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

