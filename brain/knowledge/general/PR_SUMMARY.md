---
id: pr-summary
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:03.951857
---

# CLI Feature - Pull Request Summary

## What This PR Adds

A complete **Command-Line Interface (CLI)** for Antigravity Manager with 18+ commands for power users.

## Key Features

- 📊 **Live Quota Monitoring** - Real-time tracking for Gemini & Claude models
- 🔄 **Account Switching** - Seamless switching without manual token management  
- ✅ **Token Validation** - Auto-refresh expired tokens
- 🎯 **Smart Auto-Switch** - Automatically pick best account by quota
- 🏷️ **Aliases** - Shortcut names for accounts (`work`, `personal`)
- 💾 **Backup/Restore** - Export/import account configurations
- 🎮 **Interactive Mode** - Keyboard-navigated menus for beginners
- 🩺 **Diagnostics** - System health checks

## Technical Highlights

- **Zero Hardcoded Paths**: Intelligently discovers database and executable locations
- **Cross-Platform Ready**: Uses environment variables and checks for Windows/Mac/Linux
- **Secure**: Leverages existing DPAPI + AES-256-GCM encryption (same as GUI)
- **Extensible**: Clean separation between core logic (`core.py`) and commands (`main.py`)

## File Structure

```
cli/
├── README.md           # Full documentation
├── requirements.txt    # Python dependencies
├── core.py            # Database, encryption, API logic
├── main.py            # CLI commands and interactive UI
└── proto_utils.py     # Protobuf encoding helpers
```

## Usage Examples

```powershell
# Interactive mode
agm

# Quick status
agm status

# Switch accounts
agm switch work

# Auto-switch to best account
agm auto-switch --model claude --min-quota 50

# Live monitoring
agm watch
```

## Testing

- ✅ Tested on Windows 10/11
- ✅ No hardcoded paths (uses standard Windows env vars)
- ✅ Works with both installed and development builds
- ✅ Database encryption/decryption verified

## Dependencies

All Python dependencies are self-contained in `cli/requirements.txt`:
- `typer` - CLI framework
- `rich` - Beautiful terminal output
- `questionary` - Interactive menus
- `pywin32` - Windows DPAPI support
- `cryptography` - AES-256-GCM encryption
- `httpx` - Async HTTP client
- `psutil` - Process management
- `protobuf` - Google API protocol buffers

## Platform Support

- **Windows**: Full support (tested)
- **macOS/Linux**: Partial support (no DPAPI, but core features work)

## Breaking Changes

None. This is a pure addition—no changes to existing GUI code.

## Future Enhancements

- OAuth flow for adding new accounts via CLI
- TUI (Terminal UI) with live dashboard
- Scheduled auto-refresh via Windows Task Scheduler
- Config file for user preferences

## Checklist

- [x] Code follows existing style
- [x] All commands have help text
- [x] No hardcoded paths/credentials
- [x] README with examples
- [x] Dependencies in requirements.txt
- [x] .gitignore updated for Python
- [x] Works with fresh installs

---

**Ready to merge!** 🚀
