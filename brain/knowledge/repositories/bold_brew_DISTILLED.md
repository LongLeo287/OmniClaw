---
id: repo-fetched-bold-brew-102317
type: knowledge
owner: OA
registered_at: 2026-04-05T03:59:46.294618
tags: ["auto-cloned", "oa-assimilated"]
---

# FETCHED_bold-brew_102317

## Assimilation Report
Auto-cloned repository: FETCHED_bold-brew_102317

## Application for OmniClaw
No structural integration blueprint provided.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<div align="center">
  <img src="docs/assets/logo/bbrew-logo-rounded.png" alt="Bold Brew Logo" width="200" height="200">
  <h1>Bold Brew (bbrew)</h1>
  <p>A modern Terminal UI for managing Homebrew packages and casks</p>
</div>

<div align="center">

![GitHub release (latest by date)](https://img.shields.io/github/v/release/Valkyrie00/bold-brew)
![GitHub](https://img.shields.io/github/license/Valkyrie00/bold-brew)
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/Valkyrie00/bold-brew/release.yml)
![GolangCI-Lint](https://github.com/Valkyrie00/bold-brew/workflows/Quality/badge.svg)
![Security](https://github.com/Valkyrie00/bold-brew/workflows/Security/badge.svg)
![GitHub all releases](https://img.shields.io/github/downloads/Valkyrie00/bold-brew/total)

[![GitHub stars](https://img.shields.io/github/stars/Valkyrie00/bold-brew?style=social)](https://github.com/Valkyrie00/bold-brew/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/Valkyrie00/bold-brew?style=social)](https://github.com/Valkyrie00/bold-brew/network/members)

[Website](https://bold-brew.com/) • [Changelog](https://github.com/Valkyrie00/bold-brew/releases)

</div>

---

<div align="center">

### 🌟 Official Homebrew TUI for Project Bluefin

Bold Brew is the **official Terminal UI** for managing Homebrew in [**Project Bluefin**](https://projectbluefin.io/) and [**Aurora**](https://getaurora.dev), next-generation Linux desktops that serve tens of thousands of users worldwide.

*"This application features full package management for homebrew in a nice nerdy interface"*  
— [Bluefin Documentation](https://docs.projectbluefin.io/command-line/)

[![Project Bluefin](https://img.shields.io/badge/Featured_in-Project_Bluefin-0091e2?style=for-the-badge&logo=linux)](https://projectbluefin.io/)
[![Aurora](https://img.shields.io/badge/Featured_in-Aurora-9b59b6?style=for-the-badge&logo=linux)](https://getaurora.dev)
[![Universal Blue](https://img.shields.io/badge/Part_of-Universal_Blue-5865f2?style=for-the-badge)](https://universal-blue.org/)

</div>

---

## ✨ Features

- 🚀 **Modern TUI Interface** - Clean and responsive terminal user interface
- 📦 **Complete Package Management** - Manage both Homebrew formulae and casks
- 📋 **Brewfile Mode** - Curated package collections from local or remote Brewfiles
- 🔍 **Advanced Search** - Fast fuzzy search across all packages
- 🎯 **Smart Filters** - Filter by installed, outdated, leaves, or casks
- 📊 **Analytics Integration** - See popular packages based on 90-day download stats
- 🔄 **Real-time Updates** - Live feedback during package operations
- ⌨️ **Keyboard Shortcuts** - Intuitive keybindings for all operations
- 🎨 **Type Indicators** - Visual distinction between formulae [F] and casks [C]
- 🗂️ **XDG Compliance** - Follows XDG Base Directory Specification for cache storage
- 🔒 **Security Scanning** - Automated vulnerability and security checks

## 🛠️ Installation

### Quick Install (Recommended)
Install Homebrew + Bold Brew with a single command:
```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Valkyrie00/bold-brew/main/install.sh)"
```

### Via Homebrew
If you already have Homebrew installed:
```sh
brew install Valkyrie00/homebrew-bbrew/bbrew
```

### Manually
Download the latest version from the [releases page](https://github.com/Valkyrie00/bold-brew/releases)

## 📖 Quick Start

### Standard Mode
Launch the application to browse all Homebrew packages:
```sh
bbrew
```

### Brewfile Mode
Launch with a curated Brewfile to show only specific packages:
```sh
# Local Brewfile
bbrew -f /path/to/Brewfile

# Remote Brewfile (HTTPS)
bbrew -f https://raw.githubusercontent.com/user/repo/main/Brewfile
```

In Brewfile mode, you can:
- View only packages from the Brewfile
- Pick and choose what to install individually
- Use all standard features (search, filters, etc.)
- Load Brewfiles directly from URLs (great for sharing configurations!)

Perfect for creating themed collections like IDE choosers, dev tools, AI tools, K8s tools, etc.

See the `examples/` directory for ready-to-use Brewfiles.

### CLI Options

```sh
bbrew [options]

Options:
  -f <path|url>   Path or URL to Brewfile (local file or HTTPS URL)
  -v, --version   Show version information
  -h, --help      Show help message
```

### Keyboard Shortcuts

#### Navigation & Search
- `/` - Search packages
- `↑/↓` or `j/k` - Navigate package list
- `Enter` - View package details
- `Esc` - Clear search / Back to table
- `?` - Show help screen

#### Filters
- `f` - Filter installed packages
- `o` - Filter outdated packages
- `l` - Filter leaves (explicitly installed)
- `c` - Filter casks only

#### Package Operations
- `i` - Install selected package
- `u` - Update selected package
- `r` - Remove selected package
- `Ctrl+U` - Update all outdated packages

#### Brewfile Mode Only
- `Ctrl+A` - Install all packages from Brewfile
- `Ctrl+R` - Remove all packages from Brewfile

#### Other
- `q` - Quit application

## 🖼️ Screenshots

<div align="center">
  <img src="docs/assets/screenshots/bbrew-installed-screenshot.png" alt="Installed Packages Screenshot" width="800">
  <p><em>Filtered view showing installed packages</em></p>
  
  <img src="docs/assets/screenshots/bbrew-search-screenshot.png" alt="Search Screenshot" width="800">
  <p><em>Fuzzy search in action</em></p>
  
  <img src="docs/assets/screenshots/bbrew-brewfile-screenshot.png" alt="Brewfile Mode Screenshot" width="800">
  <p><em>Brewfile mode with curated package selection</em></p>
</div>

## 📊 Platform Support

| Platform | Support | Notes |
|----------|---------|-------|
| 🍎 **macOS** | ✅ Full | Native Homebrew support |
| 🐧 **Linux** | ✅ Full | Linuxbrew/Homebrew support |

## 🛡️ Security

Security is a priority for Bold Brew. We use:
- **govulncheck** - Go vulnerability database scanning
- **gosec** - Static security analysis
- **Automated CI/CD** - Security checks on every PR and push

Found a security issue? Please report it privately via [GitHub Security Advisories](https://github.com/Valkyrie00/bold-brew/security/advisories).

## 🔧 Development

### Prerequisites
- Go 1.25+
- Homebrew (for testing)
- Podman (optional, for containerized builds)

### Building from Source
```sh
# Clone the repository
git clone https://github.com/Valkyrie00/bold-brew.git
cd bold-brew

# Build locally
make build-local

# Run tests
make test

# Run linter
make quality-local

# Run security scans
make security
```

### Project Structure
```
bold-brew/
├── cmd/bbrew/           # Main application entry point
├── internal/
│   ├── models/          # Data models (Formula, Cask, Package)
│   ├── services/        # Business logic (Brew, App, Search, Input, Brewfile)
│   └── ui/              # TUI components and layout
├── .github/workflows/   # CI/CD pipelines
└── Makefile             # Build automation
```

## 🤝 Contributing

Contributions are welcome! Please:

1. 🍴 Fork the project
2. 🔨 Create your feature branch (`git checkout -b feat/amazing-feature`)
3. 📝 Commit your changes using [Conventional Commits](https://www.conventionalcommits.org/)
4. 🧪 Run tests and linters (`make test quality-local`)
5. 🚀 Push to the branch (`git push origin feat/amazing-feature`)
6. 📬 Open a Pull Request

## 🦸Contributors
Bold Brew exists thanks to the efforts of these wonderful people

<a href="https://github.com/Valkyrie00/bold-brew/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Valkyrie00/bold-brew" />
</a>

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 💖 Support

- 🌟 [Star the project](https://github.com/Valkyrie00/bold-brew)
- 🐛 [Report a bug](https://github.com/Valkyrie00/bold-brew/issues/new?labels=bug)
- 💡 [Request a feature](https://github.com/Valkyrie00/bold-brew/issues/new?labels=enhancement)
- 📣 Share the project with your friends

---

<div align="center">
  <sub>Built with ❤️ for the community and for all developers</sub>
</div>

```

### File: VETTING_REPORT.md
```md
---
title: Auto Vetting Report for bold_brew
date: 2026-04-05
analyst: civ_vetting_pipeline
status: AUTO_VETTED
---

# Auto-Vetted Repository
This repository was automatically swept and vetted by the batch processor. Only documentation remains.

```

### File: docs\robots.txt
```txt
User-agent: *
Allow: /
Allow: /assets/
Allow: /screenshots/
Allow: /sitemap.xml

Disallow: /admin/
Disallow: /private/
Disallow: /tmp/

Sitemap: https://bold-brew.com/sitemap.xml
```

