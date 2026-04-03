---
id: thieung-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:22.029718
---

# KNOWLEDGE EXTRACT: thieung
> **Extracted on:** 2026-03-30 17:54:17
> **Source:** thieung

---

## File: `dotfiles.md`
```markdown
# 📦 thieung/dotfiles [🔖 PENDING/APPROVE]
🔗 https://github.com/thieung/dotfiles


## Meta
- **Stars:** ⭐ 12 | **Forks:** 🍴 2
- **Language:** Shell | **License:** Unknown
- **Last updated:** 2026-03-23
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
My configuration files for cool stuffs

## README (trích đầu)
```
# dotfiles

A macOS dotfiles repository organized with GNU Stow for easy management and deployment.

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/thieung/dotfiles.git ~/.dotfiles
cd ~/.dotfiles

# Complete setup (dotfiles + tools + submodules)
./install.sh all

# Or install components separately
./install.sh install       # Install dotfiles only
./install.sh tools         # Install development tools with mise
./install.sh fish          # Install Fish shell and Fisher plugin manager
./install.sh submodules    # Update git submodules
./install.sh backup        # Backup existing dotfiles only
./install.sh uninstall     # Remove dotfiles
./install.sh restow        # Reinstall dotfiles

# Install with options
./install.sh install --with-tools    # Install dotfiles + tools
./install.sh install --update-subs   # Install dotfiles + update submodules
./install.sh install --no-backup     # Install without backing up existing files
./install.sh install --interactive   # Interactive mode with guided prompts
./install.sh install --simulate      # Dry run - see what would be done

# Safe installation workflow (recommended)
./install.sh install --simulate      # Preview changes first
./install.sh install --interactive   # Then install interactively
```

## 🛠️ Current Setup

This dotfiles configuration is optimized for the following tools:

**Terminal & Shell:**
- **Ghostty** - Modern, fast terminal emulator
- **Fish** - User-friendly shell with auto-suggestions

**Window Management:**
- **FlashSpace** - Quick workspace switching
- **Rectangle** - Window snapping and management

**Development Tools:**
- **Neovim** - Highly customizable text editor
- **Git** - Version control with custom configuration
- Various CLI tools managed via mise (.tool-versions)

## 📁 Repository Structure

```
dotfiles-optimized/
├── common/                    # Cross-platform configurations
│   └── .config/
│       ├── fish/             # Fish shell configuration
│       ├── git/              # Git configuration
│       ├── nvim/             # Neovim configuration
│       └── ...               # Other cross-platform tools
├── macos/                     # macOS-specific configurations
│   ├── .config/
│   │   ├── ghostty/          # Ghostty terminal configuration
│   │   └── ...               # Other macOS-specific tools
├── scripts/                   # Installation and setup scripts
│   ├── install-tools.sh      # Development tools installation
│   ├── setup-fish-plugins.sh # Fish plugin setup
│   └── update-submodules.sh  # Git submodules management
└── install.sh                # Main installation script
```

## 🛠️ Manual Installation

If you prefer manual installation or want to install specific packages:

```bash
# Install GNU Stow first
brew install stow

# Stow common configs (cross-platform tools)
stow common

# Stow macOS-specific configs
stow macos

# Unstow (remove symlinks)
stow -D common macos
```

> 📖 **New to GNU Stow?** Read our comprehens
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

