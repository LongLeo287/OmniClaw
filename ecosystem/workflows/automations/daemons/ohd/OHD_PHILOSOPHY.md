# The Philosophy of OmniClaw Health Daemon (OHD)

OHD is the autonomic immune system of OmniClaw. It runs continuously in the background to ensure architectural purity, enforce enterprise standards, and surgically heal user-experience friction.

## Core Directives

### 1. The Split-Encoding Law (Anti-Mojibake Protocol)
To ensure seamless git tracking and system ingestion without alienating human users on Windows, OHD ruthlessly enforces a Split-Encoding heuristic:
- **Human-Facing Vietnamese Files (`*-vn.md`, `*_vn.md`):** OHD guarantees the presence of a Byte Order Mark (`UTF-8-SIG`). This ensures native Windows tools (like Notepad) display Vietnamese text perfectly without ANSI garbling.
- **Machine-Facing System Files (`*.json`, `*.yaml`, `*.md`):** OHD aggressively strips BOM signatures and enforces strict `UTF-8`. This ensures flawless interoperability with Linux containers, LLM Context Windows, and JSON parsers.

### 2. The Double-Barrel IME Vaccine (TUI Healing)
OHD patches Terminal UI libraries to prevent rapid Vietnamese Input Method Editor (Unikey/EVKey) backspace (`\x7f`) sequences from corrupting the display buffer:
- **Node.js:** Dynamically hunts and patches raw `ink` module bytecode via Regex payload.
- **Python:** Injects a protective interceptor (`python_ime_healer`) into Targeted `.py` files that optimizes `prompt_toolkit` key coalescing.

### 3. OS-Agnostic Quarantine
OHD actively scans ALL generated output to detect hardcoded physical paths (e.g., `C:\Users\...` or `D:\LongLeo\...`). Any violation is flagged and sanitized to mandate OmniClaw's ultimate portability across macOS, Linux, and Windows containers.
